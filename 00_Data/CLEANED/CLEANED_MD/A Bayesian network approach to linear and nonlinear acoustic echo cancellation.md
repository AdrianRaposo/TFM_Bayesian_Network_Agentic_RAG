# A Bayesian network approach to linear and nonlinear acoustic echo cancellation 

Christian Huemmer*, Roland Maas, Christian Hofmann and Walter Kellermann


#### Abstract

This article provides a general Bayesian approach to the tasks of linear and nonlinear acoustic echo cancellation (AEC). We introduce a state-space model with latent state vector modeling all relevant information of the unknown system. Based on three cases for defining the state vector (to model a linear or nonlinear echo path) and its mathematical relation to the observation, it is shown that the normalized least mean square algorithm (with fixed and adaptive stepsize), the Hammerstein group model, and a numerical sampling scheme for nonlinear AEC can be derived by applying fundamental techniques for probabilistic graphical models. As a consequence, the major contribution of this Bayesian approach is a unifying graphical-model perspective which may serve as a powerful framework for future work in linear and nonlinear AEC.


Keywords: Bayesian networks, Acoustic echo cancellation, Graphical models

## 1 Introduction

The problem of acoustic echo cancellation (AEC) is one of the earliest applications of adaptive filtering to acoustic signals and yet is still an active research topic [1, 2]. Especially in applications like teleconferencing and handsfree communication systems, it is of vital importance to compensate acoustic echos and thus prevent the users from listening to delayed version of their own speech [3]. Since the invention of the normalized least mean square (NLMS) algorithm in 1960 [4], the acoustic coupling between loudspeakers and microphones is often modeled by adaptive linear finite impulse response (FIR) filters. However, the statistical properties of speech signals (being wide-sense stationary only for short time frames) and challenging properties of the acoustic environment (such as speech signals as interference, non-stationary background noise and time-varying acoustic echo paths) complicate the filter adaptation and motivated various concepts improving the performance of linear FIR filters in many practical scenarios [5-7]. Despite these challenges, single-channel linear AEC has already reached a mature state as vital part of modern communication

[^0]devices. On the other hand, the nonlinear distortions created by amplifiers and transducers in miniaturized loudspeakers require dedicated nonlinear echo-path models and are still a very active research topic [8, 9]. In this context, a variety of concepts for nonlinear AEC have been proposed based on artificial neural networks [10, 11], Volterra filters [12, 13], or Kernel methods $[14,15]$. A commonly used model, which is also considered in this article, is a cascade of a nonlinear memoryless preprocessor (to model the loudspeaker signal distortions) and an adaptive linear FIR filter (to model the acoustic sound propagation and the microphone) $[9,16-19]$.
Recently, the application of machine learning techniques to signal processing tasks attracted increasing interest [20-22]. In particular, graphical models provide a powerful framework for deriving (links between) numerous existing algorithms based on probabilistic inference [23-25]. Besides the widely used factor graphs, which capture detailed information about the factorization of a joint probability distribution [23, 26, 27], especially directed graphical models, such as Bayesian networks, have been shown to be well-suited for modeling causal probabilistic relationships of sequential data like speech [28, 29].
This article provides a concise overview on different algorithms for linear and nonlinear AEC from a unifying


[^0]:    *Correspondence: huemmer@lnt.de
    Multimedia Communications and Signal Processing, University of Erlangen-Nuremberg, Cauerstraße 7, Erlangen, Germany

Bayesian network perspective. For this, we consider a state-space model with a latent (unobserved) state vector capturing all relevant information of the unknown system. Depending on the definition of the state vector (modeling a linear or nonlinear echo path) and its mathematical relation to the observation, we illustrate that the application of different probabilistic inference techniques to the same graphical model straightforwardly leads to the NLMS algorithm with fixed/adaptive stepsize value, the Hammerstein group model (considered from this perspective here for the first time), and a numerical sampling scheme for nonlinear AEC. This consistent Bayesian view on conceptually different algorithms highlights the probabilistic assumptions underlying the respective derivations and provides a powerful framework for further research in linear and nonlinear AEC.

Throughout this article, the problem of AEC is considered in the time domain (time index *n*), where we denote scalars *z<sub>n</sub>* by lowercase italic letters, column vectors **z<sub>n</sub>** by lower case bold letters, and matrices **C<sub>z,n</sub>** by upper case bold letters. Furthermore, sequences of variables are written as *z<sub>1:N</sub>* = {*z<sub>1</sub>*, . . . , *z<sub>N</sub>*}. For a normally distributed random vector **z<sub>n</sub>** with mean vector **µz<sub>n</sub>** and covariance matrix **C<sub>z,n</sub>**, we write

$$
\mathbf{z}_n \sim \mathcal{N}\left\{\mathbf{z}_n \mid \mathbf{\mu}_{\mathbf{z}_n}, \mathbf{C}_{\mathbf{z}_n}\right\}. \tag{1}
$$

Note that **C<sub>z,n</sub>** = *C<sub>z,n</sub>***I** (identity matrix **I**) implies the elements of **z<sub>n</sub>** to be mutually statistically independent and of equal variance *C<sub>z,n</sub>*. Finally, we distinguish between the probability density function (PDF) *p(z<sub>n</sub>*) and realizations *z<sub>n</sub><sup>(l)</sup>* (samples drawn from *p(z<sub>n</sub>*)) of a random variable *z<sub>n</sub>*, where *l* is the sample index.

This article is structured as follows: First, we briefly review Bayesian networks and introduce a general state-space model in Section 2. This state-space model will be further specified in Section 3 for the tasks of linear and nonlinear AEC. This is followed by applying several fundamental probabilistic inference techniques for deriving the NLMS algorithm with fixed/adaptive stepsize value (linear AEC, Section 4), as well as the Hammerstein group model and a numerical sampling scheme (nonlinear AEC, Section 5). Finally, the practical performance of the algorithms is illustrated in Section 6 and conclusions are drawn in Section 7.

## 2 Review of Bayesian networks and state-space modeling

This section provides a concise review of Bayesian networks and state-space modeling following the detailed discussions in [30].

### 2.1 Bayesian networks

Bayesian networks are graphical descriptions of joint probability distributions and provide a powerful framework for many kinds of regression and classification problems. Consisting of nodes (random variables) and directed links (probabilistic relationships), they define the factorization properties of a joint PDF *p(z<sub>1:K</sub>*) through the following rule:

$$
p(z_{1:K}) = \prod_{k=1}^{K} p(z_k|\text{par}(z_k))\,, \tag{1}
$$

where {par(*z<sub>k</sub>*)} is the set of nodes (so-called parent nodes of *z<sub>k</sub>*) from which a link is going to the node *z<sub>k</sub>*. We illustrate this basic definition by the example shown in Fig. 1: the joint PDF *p(z<sub>1</sub>*, *z<sub>2</sub>*, *z<sub>3</sub>*) over the random variables *z<sub>1</sub>*, *z<sub>2</sub>*, *z<sub>3</sub>* factorizes to

$$
p(z_1, z_2, z_3) = p(z_1) p(z_2|z_1) p(z_3|z_1, z_2), \tag{2}
$$

where the PDF of each random variable is conditioned on its parent nodes (if any). This fundamental factorization property of Bayesian networks can be employed to derive several rules of conditional dependence and independence for Bayesian networks. As an example, we consider three independent random variables *z<sub>1</sub>*, *η*, *ε* defining two further random variables *z<sub>2</sub>* and *z<sub>3</sub>* through the following observation model:

$$
z_2 = z_1 + \varepsilon, \quad z_3 = z_2 + \eta. \tag{3}
$$

The probabilistic relationship of *z<sub>1</sub>*, *z<sub>2</sub>*, *z<sub>3</sub>* can be represented by the Bayesian network depicted in Fig. 2a, where the variables *η* and *ε* have been omitted to focus on the *head-to-tail* relationship in *z<sub>2</sub>*. Although *z<sub>1</sub>* and *z<sub>3</sub>* are statistically dependent, we can exploit (1) to show that *z<sub>1</sub>* and *z<sub>3</sub>* are conditionally independent given *z<sub>2</sub>*:

$$
p(z_1, z_3|z_2) = \frac{p(z_1, z_2, z_3)}{p(z_2)} \tag{4}
$$

$$
\begin{aligned}
\frac{(1)}{(2)} \frac{p(z_1) p(z_2|z_1) p(z_3|z_2)}{p(z_2)} \\
= p(z_1|z_2) p(z_3|z_2).
\end{aligned} \tag{5}
$$

The same property of conditional independence can be derived for the case of a *tail-to-tail* relationship in *z<sub>2</sub>* as shown in Fig. 2b. In contrast, two independent random variables *z<sub>1</sub>* and *z<sub>3</sub>* are conditionally dependent given *z<sub>2</sub>* if they share a *head-to-head* relationship as in Fig. 2c, which would, e.g., be the case if *z<sub>2</sub>* was defined as *z<sub>2</sub>* = *z<sub>1</sub>* + *z<sub>3</sub>*.

![img-0.jpeg](img-0.jpeg)

**Fig. 1** Example of a Bayesian network

![img-1.jpeg](img-1.jpeg)

**Fig. 2** Bayesian networks with **a**) head-to-tail, **b**) tail-to-tail, and **c**) head-to-head relationship in *z*2 [31]

Generalizing the above, it can be shown that two random variables *z*1 and *z*3 are conditionally independent given a set of random variables *C* if all paths leading from *z*1 to *z*3 contain a node, where the

- arrows meet head-to-tail or tail-to-tail, and the node is in the set *C*
- arrows meet head-to-head and neither the node, nor any of its descendants, are in the set *C* [30].

### 2.2 State-space modeling

In this part, we introduce a general probabilistic model (later applied to linear and nonlinear AEC) and review fundamental techniques which are commonly employed in Bayesian network modeling.

**Probabilistic model:** Assume all relevant information of an unknown system at time instant *n* is captured by a latent (unobserved) state vector

$$
\mathbf{z}_n = [z_{0,n}, z_{1,n}, \dots, z_{R-1,n}]^{\mathrm{T}}.
\tag{6}
$$

In general, a state-space model is defined by the process equation (modeling the temporal evolution of the state vector) and the observation equation (modeling the relation between state vector and observation). The remainder of this article is based on the following observation equation and state equation, respectively,

$$
d_n = \mathbf{g}(\mathbf{x}_n, \mathbf{z}_n) + v_n \quad \text{and} \quad \mathbf{z}_n = \mathbf{z}_{n-1} + \mathbf{w}_n, \tag{7}
$$

where the temporal evolution of the state vector **z***n* is captured by the additive uncertainty **w***n*. Furthermore, the observation *d**n* in (7) is modeled by adding a scalar uncertainty *v**n* to the output of the function **g**(**x**_n, **z**_n), which depends on the state vector **z***n* and the input signal vector **x**_n = [*x**n*, *x**n*−1, ..., *x**n*−*M*+1] T (time-domain samples *x**n* at time instant *n*). The state-space model of (7) is represented by the Bayesian network in Fig. 3, where observed variables, such as *d**n*, are marked by shaded circles. Note that the input signal vector **x**_n is regarded as an observed random variable (without explicitly estimated statistics) and thus omitted in Fig. 3 for notational convenience in the later probabilistic calculus. The conditional

![img-2.jpeg](img-2.jpeg)

**Fig. 3** Bayesian network of the state-space model in (7), where the observations *d*1*n* are marked by coloration [30]

independence rules of Section 2 reveal two major properties of the Bayesian network in Fig. 3:

- With respect to the latent state vector **z***n*−1, the head-to-tail relationships of all paths from *d*1*n*−2 to **z***n* and the tail-to-tail relationship of the path from *d**n*−1 to **z***n* together imply the current state vector **z***n* to depend on all previous observations *d*1*n*−1. For the conditional PDF of **z***n* given {**z**_n−1, *d*1;n−1}, this leads to:

$$
p\left(\mathbf{z}_n \mid \mathbf{z}_{n-1}, d_{1:n-1}\right) = p\left(\mathbf{z}_n \mid \mathbf{z}_{n-1}\right).
\tag{8}
$$

- The current observation *d**n* depends on all previous observations *d*1*n*−1 following the head-to-tail relationship in the latent state vector **z***n*. This allows to reformulate the conditional PDF of *d**n* given {**z**_n, *d*1;n−1} as

$$
p\left(d_n \mid \mathbf{z}_n, d_{1:n-1}\right) = p\left(d_n \mid \mathbf{z}_n\right).
\tag{9}
$$

The state-space model in (7) is a fundamental probabilistic model and will be employed to derive well-known methods for linear and nonlinear AEC in Sections 4 and 5. For this, we make the following assumptions on the PDFs of the additive uncertainties in (7) [32]:

- **w***n* is normally distributed with mean vector **0** and covariance matrix **C**_{w,n} defined by the scalar variance *C*_{w,n}:

$$
\mathbf{w}_n \sim \mathcal{N}\left\{\mathbf{w}_n \mid \mathbf{0}, \mathbf{C}_{\mathbf{w},n}\right\}, \quad \mathbf{C}_{\mathbf{w},n} = C_{\mathbf{w},n} \mathbf{I}.
\tag{10}
$$

- *v**n* is assumed to be normally distributed with variance *C**v,n* and zero mean:

$$
v_n \sim \mathcal{N}\{v_n \mid 0, C_{v,n}\}.
\tag{11}
$$

To derive estimates for the state vector and the hyperparameters *C**v,n* and *C*_{w,n}, we recall the steps of probabilistic inference and learning in the next part.

**Inference/Learning:** In the inference stage, the mean vector of the posterior PDF *p*(**z**_n|*d*1;n) can be identified as minimum mean square error (MMSE) estimate for the state vector [30]:

$$ \hat{\mathbf{z}}_n = \underset{\hat{\mathbf{z}}_n}{\text{argmin}} \mathcal{E}\left\{ ||\hat{\mathbf{z}}_n - \mathbf{z}_n||_2^2 \right\} = \mathcal{E}\left\{\mathbf{z}_n|d_{1:n}\right\}, \tag{12} $$

where ||·||_{2} is the Euclidean norm and $\mathcal{E}$[·] the expectation operator. Note that this MMSE estimate can be calculated in an analytically closed form in case of linear relations between the variables in (7) and is optimal in the Bayesian sense for jointly normally distributed random variables $\mathbf{z}_n$ and $d_{1:n}$.

In the *learning* stage, the hyperparameters $C_{v,n}$ and $C_{\mathbf{w},n}$ of the state-space model in (7) are estimated by solving a maximum likelihood (ML) problem (see Section 4.1 for more details).

## 3 State-space model for linear and nonlinear AEC

To identify the electroacoustic echo path (from the loudspeaker to the microphone), a physically justifiable model has to be selected first. As the sound propagation through air can be modeled by a linear system [1], the acoustic path at time $n$ between loudspeaker and microphone is estimated by the linear FIR filter

$$ \hat{\mathbf{h}}_n = \left[ \hat{h}_{0,n}, \hat{h}_{1,n}, \dots, \hat{h}_{M-1,n} \right]^{\mathrm{T}} \tag{13} $$

of length $M$. Ideally, the error signal

$$ e_n = d_n - \hat{d}_n \tag{14} $$

between the observation $d_n$ and the linear transformation of the input vector $\mathbf{y}_n$:

$$ \hat{d}_n = \hat{\mathbf{h}}_n-1^{\mathrm{T}} \mathbf{y}_n \tag{15} $$

equals zero, which means that the estimated impulse response matches the actual physical one. In many practical applications, nonlinear loudspeaker signal distortions created by amplifiers and transducers in minituarized loudspeakers prior to the linear acoustic impulse response limit the practical performance of linear echo path models. This justifies to model the overall echo path by a nonlinear-linear cascade of a memoryless preprocessor (to model nonlinear loudspeaker signal distortions) preceding the linear FIR filter $\hat{\mathbf{h}}_n$ (to model the sound propagation through air) [9, 16, 17], see Fig. 4. Motivated by the good performance in nonlinear AEC [18, 19, 32], we choose a polynomial preprocessor

$$ \mathbf{y}_n = \mathbf{f}(\mathbf{x}_n, \hat{\mathbf{a}}_n-1) = \mathbf{x}_n + \sum_{v=1}^P \hat{a}_{v,n-1} \Phi_v \{\mathbf{x}_n\}, \tag{16} $$

defined as weighted superposition of nonlinear functions $\Phi_v$[·] parameterized by the estimated vector

$$ \hat{\mathbf{a}}_n-1 = \left[ \hat{a}_{1,n-1}, \hat{a}_{2,n-1}, \dots, \hat{a}_{P,n-1} \right]^{\mathrm{T}}, \tag{17} $$

to perform an element-wise transformation of the loudspeaker signal vector $\mathbf{x}_n$ to the input vector $\mathbf{y}_n$ of the linear

![img-3.jpeg](img-3.jpeg)

**Fig. 4** Nonlinear AEC scenario with memoryless preprocessor $\mathbf{f}(\mathbf{x}_n, \hat{\mathbf{a}}_n-1)$ and linear FIR filter $\hat{\mathbf{h}}_n-1$

FIR filter in (15). In particular, odd-order Legendre functions of the first kind (inserted for $\Phi_v$[·] in (16)) have been shown to be efficient for specific applications [18, 19]. By combining (15) and (16), the error signal $e_n$ resulting from the nonlinear-linear cascade in Fig. 4 is given as:

$$ \hat{d}_n = \hat{\mathbf{h}}_n-1^{\mathrm{T}} \left( \mathbf{x}_n + \sum_{v=1}^P \hat{a}_{v,n-1} \Phi_v \{\mathbf{x}_n\} \right). \tag{18} $$

It is obvious that the nonlinear-linear cascade in Fig. 4 simplifies to a linear AEC system when setting the estimated preprocessor coefficients equal to zero because:

$$ \mathbf{y}_n \stackrel{(16)}{=} \mathbf{x}_n, \quad \text{for} \quad \hat{\mathbf{a}}_n-1 = [0, 0, \dots, 0]^{\mathrm{T}}. \tag{19} $$

In the following, we describe the tasks of linear and nonlinear AEC from a Bayesian network perspective by further specializing the general state-space model in (7). This is summarized in Fig. 5 as guidance through the following derivations.

*Linear AEC*: The observation equation for linear AEC follows the definition of $\hat{d}_n$ in (15):

$$ d_n = \mathbf{z}_n^{\mathrm{T}} \mathbf{x}_n + v_n, \quad \text{with} \quad \mathbf{z}_n = \mathbf{h}_n, \tag{20} $$

where the latent length-$M$ vector $\mathbf{h}_n$ models the acoustic path between the loudspeaker and the microphone. Note that the observation equation in (20) is denoted as a model which is linear in the coefficients (LIC model) due to the linear relation between the elements of the state vector $\mathbf{z}_n$ and the observation $d_n$.

*Nonlinear AEC*: For the task of nonlinear AEC, we derive the observation equation from (18):

$$ d_n = \mathbf{h}_n^{\mathrm{T}} \left( \mathbf{x}_n + \sum_{v=1}^P a_{v,n} \Phi_v \{\mathbf{x}_n\} \right) + v_n, \tag{21} $$

where the latent variables $a_{v,n}(v = 1, \dots, P)$ model the preprocessor coefficients and represent the entries of the length-$P$ vector $\mathbf{a}_n$, which is identically defined as in (17). Depending on the choice of the state vector, the observation equation in (21) represents a LIC model or a model

![img-4.jpeg](img-4.jpeg)

**Fig. 5** Overview of the following sections including the different observation equations and respective state-vector definitions for the tasks of linear and nonlinear AEC, where the process equation equals **z**<sub>*n*</sub> = **z**<sub>*n*−1</sub> + **w**<sub>*n*</sub> for all cases

which is nonlinear in the coefficients (NIC model) of the state vector. To start with the latter case, we specify:

$$
\mathbf{z}_n = \left[ \mathbf{a}_n^T \mathbf{h}_n^T \right]^T \tag{22}
$$

as state vector of length *M* + *P*. Thereby, the observation equation in (21) becomes a NIC model due to the nonlinear relation between the entries of the state vector **z**<sub>*n*</sub> and the observation *d*<sub>*n*</sub>. Alternatively, we can express the same input-output relation by the length *M* · (*P* + 1) state vector

$$
\mathbf{z}_n = \left[ \mathbf{h}_n^T, a_{1,n} \mathbf{h}_n^T, \dots, a_{P,n} \mathbf{h}_n^T \right]^T \tag{23}
$$

together with the observation equation

$$
d_n = \mathbf{z}_n^T \left[ \mathbf{x}_n^T, \Phi_1 \{\mathbf{x}_n\}^T, \dots, \Phi_P \{\mathbf{x}_n\}^T \right]^T + v_n. \tag{24}
$$

This represents a LIC model as the output *d*<sub>*n*</sub> linearly depends on the coefficients of **z**<sub>*n*</sub>. The three previously described pairs of observation equations and state vector definitions represent special cases of the state-space model in (7) and will be employed in the subsequent sections to derive algorithms for linear and nonlinear AEC following the schematic overview in Fig. 5.

### 4 A Bayesian view on linear AEC

Consider the task of linear AEC using the state-space model (see left part of Fig. 5)

$$
d_n = \mathbf{h}_n^T \mathbf{x}_n + v_n, \quad \mathbf{h}_n = \mathbf{h}_{n-1} + \mathbf{w}_n, \tag{25}
$$

which can be represented by the Bayesian network shown in Fig. 6. To derive an NLMS-like filter adaptation, we assume the PDFs *p*(**h**<sub>*n*</sub>|**h**<sub>*n*−1</sub>), *p*(*d*<sub>*n*</sub>|**h**<sub>*n*</sub>), and *p*(**h**<sub>*n*</sub>|*d*<sub>1:*n*</sub>) to be Gaussian probability distributions [30], where the latter is denoted as:

$$
p\left(\mathbf{h}_n \mid d_{1:n}\right) \stackrel{(12)}{=} \mathcal{N}\left\{\mathbf{h}_n \mid \tilde{\mathbf{h}}_n, \mathbf{C}_{\mathbf{h}_n}\right\}. \tag{26}
$$

Therein, we restrict the covariance matrix of *p*(**h**<sub>*n*</sub>|*d*<sub>1:*n*</sub>) to be diagonal [33]

$$
\mathbf{C}_{\mathbf{h}_n} = C_{\mathbf{h}_n} \mathbf{I} \quad \text{with} \quad C_{\mathbf{h}_n} = \operatorname{tr}\{\mathbf{C}_{\mathbf{h}_n}\} / M, \tag{27}
$$

where tr{·} represents the trace of a matrix. This implies the filter taps to be uncorrelated and of equal estimation uncertainty. The assumption (27) will be the basis for deriving the NLMS algorithm with adaptive (Section 4.1) and fixed (Section 4.2) stepsize value.

### 4.1 NLMS algorithm with adaptive stepsize value [32]

The NLMS algorithm with optimal stepsize calculation has been initially proposed by Yamamoto and Kitayama in 1982 [34]. Since then, the derivation of the adaptive stepsize NLMS algorithm with filter update

$$
\hat{\mathbf{h}}_n = \tilde{\mathbf{h}}_{n-1} + \frac{1}{M} \frac{\mathcal{E}\left\{\left| \left| \mathbf{h}_n - \tilde{\mathbf{h}}_{n-1} \right| \right|_2^2 \right\}}{\mathcal{E}\left\{ e_n^2 \right\}} \mathbf{x}_n e_n \tag{28}
$$

has been adopted in many textbooks [35]. As the true echo path **h**<sub>*n*</sub> is not observable, the numerator in (28) can be approximated by introducing a delay of *N*<sub>*T*</sub> coefficients to the echo path **h**<sub>*n*</sub> [36, 37]. Then, it is assumed that the leading *N*<sub>*T*</sub> coefficients *h̃*<sub>*κ*, *n*−1</sub>, with *κ* = 0, ..., *N*<sub>*T*</sub> − 1, should be zero for causal systems and any nonzero coefficient values are representative for the system error norm $\mathcal{E}\left\{\left| \left| \mathbf{h}_n - \tilde{\mathbf{h}}_{n-1} \right| \right|_2^2 \right\}$. Typically, the denominator in (28) is recursively approximated using a smoothing factor *η* [35, 37]. Thus, the filter update is realized as follows:

![img-5.jpeg](img-5.jpeg)

**Fig. 6** Bayesian network of the state-space model in (25), where the observations *d*<sub>*1:n*</sub> are marked by coloration [30]

$$
\begin{aligned}
\tilde{\mathbf{h}}_{n} & =\tilde{\mathbf{h}}_{n-1}+\frac{1}{N_{T}} \frac{\sum_{k=0}^{N_{T}-1} \hat{h}_{k, n-1}^{2}}{(1-\eta) e_{n}^{2}+\eta \mathcal{E}\left\{e_{n-1}^{2}\right\}} \mathbf{x}_{n} e_{n} \\
& =\tilde{\mathbf{h}}_{n-1}+\beta_{n} \mathbf{x}_{n} e_{n}
\end{aligned}
$$

However, the approximations in (29) often lead to oscillations which have to be addressed by limiting the absolute value of $\beta_{n}[36]$.
In the following, we employ Bayesian network modeling to derive the filter update of (28) (in the inference stage) and an estimation scheme for the adaptive stepsize $\beta_{n}$ (in the learning stage).
Inference: To derive the MMSE estimate of the state vector following (12), we rewrite the posterior PDF as

$$
\begin{aligned}
p\left(\mathbf{h}_{n} \mid d_{1: n}\right) & =\frac{p\left(d_{n}, \mathbf{h}_{n} \mid d_{1: n-1}\right)}{p\left(d_{n} \mid d_{1: n-1}\right)} \\
& =\frac{p\left(d_{n} \mid \mathbf{h}_{n}, d_{1: n-1}\right) p\left(\mathbf{h}_{n} \mid d_{1: n-1}\right)}{p\left(d_{n} \mid d_{1: n-1}\right)} \\
& \stackrel{(8)}{=} \frac{p\left(d_{n} \mid \mathbf{h}_{n}\right) p\left(\mathbf{h}_{n} \mid d_{1: n-1}\right)}{p\left(d_{n} \mid d_{1: n-1}\right)}
\end{aligned}
$$

Then, the product rules of linear Gaussian models ([30] p. 639) can be applied to derive recursive updates for the mean vector $\tilde{\mathbf{h}}_{n}=\mathcal{E}\left(\mathbf{h}_{n} \mid d_{1: n}\right)$ and the covariance matrix $\mathbf{C}_{\mathbf{h}, n}$, resulting in a special case of the well-known Kalman filter equations:

$$
\begin{aligned}
& \tilde{\mathbf{h}}_{n}=\tilde{\mathbf{h}}_{n-1}+\frac{\left(\mathbf{C}_{\mathbf{h}, n-1}+\mathbf{C}_{\mathbf{w}, n}\right) \mathbf{x}_{n} e_{n}}{\mathbf{x}_{n}^{\mathrm{T}}\left(\mathbf{C}_{\mathbf{h}, n-1}+\mathbf{C}_{\mathbf{w}, n}\right) \mathbf{x}_{n}+C_{v, n}} \\
& \mathbf{C}_{\mathbf{h}, n}=\left(\mathbf{I}-\mathbf{A}_{n} \mathbf{x}_{n} \mathbf{x}_{n}^{\mathrm{T}}\right)\left(\mathbf{C}_{\mathbf{h}, n-1}+\mathbf{C}_{\mathbf{w}, n}\right)
\end{aligned}
$$

By inserting the assumptions (10) and (27), we can rewrite the filter update as:

$$
\begin{aligned}
& \tilde{\mathbf{h}}_{n}=\tilde{\mathbf{h}}_{n-1}+\frac{\left(C_{\mathbf{h}, n-1}+C_{\mathbf{w}, n}\right) \mathbf{x}_{n} e_{n}}{\mathbf{x}_{n}^{\mathrm{T}} \mathbf{x}_{n}\left(C_{\mathbf{h}, n-1}+C_{\mathbf{w}, n}\right)+C_{v, n}} \\
& C_{\mathbf{h}, n}=\left(1-\lambda_{n} \frac{\mathbf{x}_{n}^{\mathrm{T}} \mathbf{x}_{n}}{M}\right)\left(C_{\mathbf{h}, n-1}+C_{\mathbf{w}, n}\right)
\end{aligned}
$$

The equivalence between the filter updates of (34) and (28) can be illustrated by exploiting the equalities

$$
\begin{aligned}
& C_{\mathbf{h}, n} \mathbf{I} \stackrel{(27)}{=} \mathbf{C}_{\mathbf{h}, n} \stackrel{(26)}{=} \mathcal{E}\left\{\left(\mathbf{h}_{n}-\tilde{\mathbf{h}}_{n}\right)\left(\mathbf{h}_{n}-\tilde{\mathbf{h}}_{n}\right)^{\mathrm{T}}\right\} \\
& C_{\mathbf{w}, n} \mathbf{I} \stackrel{(10)}{=} \mathbf{C}_{\mathbf{w}, n}=\mathcal{E}\left\{\mathbf{w}_{n} \mathbf{w}_{n}^{\mathrm{T}}\right\}
\end{aligned}
$$

which lead to:

$$
\begin{aligned}
& C_{\mathbf{h}, n}=\frac{\mathcal{E}\left\{\left\|\mathbf{h}_{n}-\tilde{\mathbf{h}}_{n}\right\|_{2}^{2}\right\}}{M} \\
& C_{\mathbf{w}, n}=\frac{\mathcal{E}\left\{\mathbf{w}_{n}^{\mathrm{T}} \mathbf{w}_{n}\right\}}{M}=\frac{\mathcal{E}\left\{\left\|\mathbf{w}_{n}\right\|_{2}^{2}\right\}}{M}
\end{aligned}
$$

Furthermore, $\mathbf{h}_{n-1}$ and $\mathbf{w}_{n}$ are statistically independent due to the head-to-head relationship with respect to the latent vector $\mathbf{h}_{n}$ in Fig. 6. Thus, we rewrite:

$$
\begin{aligned}
& \frac{\mathcal{E}\left\{\left\|\mathbf{h}_{n}-\tilde{\mathbf{h}}_{n-1}\right\|_{2}^{2}\right\}}{\frac{M}{2 \overline{2}}} \frac{\mathcal{E}\left\{\left\|\mathbf{h}_{n-1}+\mathbf{w}_{n}-\tilde{\mathbf{h}}_{n-1}\right\|_{2}^{2}\right\}}{M} \\
& =\frac{\mathcal{E}\left\{\left\|\mathbf{h}_{n-1}-\tilde{\mathbf{h}}_{n-1}\right\|_{2}^{2}\right\}}{M}+\frac{\mathcal{E}\left\{\left\|\mathbf{w}_{n}\right\|_{2}^{2}\right\}}{M} \\
& \stackrel{(37)}{=} C_{\mathbf{h}, n-1}+C_{\mathbf{w}, n}
\end{aligned}
$$

Furthermore, one can use the fact that $v_{n}$ is statistically independent from $\mathbf{h}_{n-1}$ and $\mathbf{w}_{n}$ (head-to-head relationship in $d_{n}$ in Fig. 6) to express $\mathcal{E}\left\{e_{n}^{2}\right\}$ as:

$$
\begin{aligned}
& \mathcal{E}\left\{e_{n}^{2}\right\} \stackrel{(14)(15)}{=} \mathcal{E}\left\{\left(\mathbf{x}_{n}^{\mathrm{T}}\left(\mathbf{h}_{n}-\tilde{\mathbf{h}}_{n-1}\right)+v_{n}\right)^{2}\right\} \\
& =\mathcal{E}\left\{\mathbf{x}_{n}^{\mathrm{T}}\left(\mathbf{h}_{n}-\tilde{\mathbf{h}}_{n-1}\right)\left(\mathbf{h}_{n}-\tilde{\mathbf{h}}_{n-1}\right)^{\mathrm{T}} \mathbf{x}_{n}\right\}+\mathcal{E}\left\{v_{n}^{2}\right\} \\
& =\mathbf{x}_{n}^{\mathrm{T}} \mathcal{E}\left\{\left(\mathbf{h}_{n}-\tilde{\mathbf{h}}_{n-1}\right)\left(\mathbf{h}_{n}-\tilde{\mathbf{h}}_{n-1}\right)^{\mathrm{T}}\right\} \mathbf{x}_{n}+C_{v, n} \\
& \stackrel{(25)(36)}{=} \mathbf{x}_{n}^{\mathrm{T}} \mathbf{x}_{n}\left(C_{\mathbf{h}, n-1}+C_{\mathbf{w}, n}\right)+C_{v, n}
\end{aligned}
$$

Inserting (38) and (39) into (28) finally yields the identical expression for the filter update as in (34). All together, we thus derived the adaptive stepsize NLMS algorithm (initially heuristically proposed in 1982 [34]) by applying fundamental techniques of Bayesian network modeling to a special realization of the fundamental state-space model in (7). Next, we estimate the hyperparameters $C_{v, n}$ and $C_{\mathbf{w}, n}$ in the learning stage to realize the adaptive stepsize NLMS algorithm in (34) without exploiting the approximations of (28).
Learning: For deriving an update of the model parameters from $\theta_{n}=\left\{C_{v, n}, C_{\mathbf{w}, n}\right\}$ to $\left\{C_{v, n}^{\text {new }}, C_{\mathbf{w}, n}^{\text {new }}\right\}$, we determine the joint PDF

$$
p\left(d_{1: n}, \mathbf{h}_{1: n}\right)=\prod_{m=1}^{n} p\left(\mathbf{h}_{m} \mid \mathbf{h}_{m-1}\right) p\left(d_{m} \mid \mathbf{h}_{m}\right)
$$

based on the factorization rules of Section 2. Although the ML problem

$$
\left\{C_{v, n}^{\text {new }}, C_{\mathbf{w}, n}^{\text {new }}\right\}=\underset{C_{v, n}^{\text {new }}, C_{\mathbf{w}, n}^{\text {new }}}{\operatorname{argmax}} p\left(d_{1: n}\right)
$$

is analytically tractable, marginalizing over the joint PDF in (40) to calculate $p\left(d_{1: n}\right)$ leads to a computational complexity exponentially growing with $n$ [30]. Thus, we iteratively approximate the ML solution to derive an online estimator based on the lower bound [30]

$$
\begin{aligned}
\ln p\left(d_{1: n}\right) & =\ln p\left(d_{1: n}\right) \int p\left(\mathbf{h}_{1: n} \mid d_{1: n}\right) d \mathbf{h}_{1: n} \\
& \geq \int p\left(\mathbf{h}_{1: n} \mid d_{1: n}\right) \ln p\left(d_{1: n}, \mathbf{h}_{1: n}\right) d \mathbf{h}_{1: n} \\
& =\mathcal{E}\left\{\ln \left(p\left(d_{1: n}, \mathbf{h}_{1: n}\right)\right)\right\}
\end{aligned}
$$

Taking the natural logarithm $\ln (\cdot)$ of the joint PDF defined in (40) and maximizing the right-hand side of (42) with respect to the new parameters leads to two separate optimization problems caused by the conditional independence properties in (8) and (9):

$$
\begin{aligned}
& C_{\mathbf{w}, n}^{\text {new }}=\underset{C_{\mathbf{w}, n}^{\text {new }}}{\operatorname{argmax}} \mathcal{E}\left\{\ln \left(p\left(\mathbf{h}_{n} \mid \mathbf{h}_{n-1}\right)\right)\right\} \\
& C_{v, n}^{\text {new }}=\underset{C_{v, n}^{\text {new }}}{\operatorname{argmax}} \mathcal{E}\left\{\ln \left(p\left(d_{n} \mid \mathbf{h}_{n}\right)\right)\right\}
\end{aligned}
$$

For the estimation of $C_{v, n}^{\text {new }}$, we insert

$$
\ln \left(p\left(d_{n} \mid \mathbf{h}_{n}\right)\right) \stackrel{(25)}{=}-\frac{\ln \left(2 \pi C_{v, n}^{\text {new }}\right)}{2}-\frac{\left(d_{n}-\mathbf{x}_{n}^{\mathrm{T}} \mathbf{h}_{n}\right)^{2}}{2 C_{v, n}^{\text {new }}}
$$

into (44) and thus derive the instantaneous estimate by equating the derivation with respect to $C_{v, n}^{\text {new }}$ to zero:

$$
\begin{aligned}
C_{v, n}^{\text {new }} & =\mathcal{E}\left\{\left(d_{n}-\mathbf{x}_{n}^{\mathrm{T}} \mathbf{h}_{n}\right)^{2}\right\} \\
& =d_{n}^{2}+\mathbf{x}_{n}^{\mathrm{T}} \mathcal{E}\left\{\mathbf{h}_{n} \mathbf{h}_{n}^{\mathrm{T}}\right\} \mathbf{x}_{n}-2 \mathbf{x}_{n}^{\mathrm{T}} \hat{\mathbf{h}}_{n} \\
& =d_{n}^{2}+\mathbf{x}_{n}^{\mathrm{T}}\left(C_{\mathbf{h}, n} \mathbf{I}+\hat{\mathbf{h}}_{n} \hat{\mathbf{h}}_{n}^{\mathrm{T}}\right) \mathbf{x}_{n}-2 \mathbf{x}_{n}^{\mathrm{T}} \hat{\mathbf{h}}_{n} \\
& =\left(d_{n}-\mathbf{x}_{n}^{\mathrm{T}} \hat{\mathbf{h}}_{n}\right)^{2}+\mathbf{x}_{n}^{\mathrm{T}} \mathbf{x}_{n} C_{\mathbf{h}, n}
\end{aligned}
$$

which can be interpreted as follows [31]: The first term in (45) (squared error signal after filter adaptation) is influenced by near-end interferences like background noise. The second term in (45) depends on the signal energy $\mathbf{x}_{n}^{\mathrm{T}} \mathbf{x}_{n}$ and the variance $C_{\mathbf{h}, n}$ which means that it considers the input signal power and uncertainties in the linear echo path model. Similar to the derivation for $C_{v, n}^{\text {new }}$, we insert

$$
\begin{aligned}
\ln \left(p\left(\mathbf{h}_{n} \mid \mathbf{h}_{n-1}\right)\right) & \stackrel{(25)}{=}-\frac{M \ln \left(2 \pi C_{\mathbf{w}, n}^{\text {new }}\right)}{2} \\
& -\frac{\left(\mathbf{h}_{n}-\mathbf{h}_{n-1}\right)^{\mathrm{T}}\left(\mathbf{h}_{n}-\mathbf{h}_{n-1}\right)}{2 C_{\mathbf{w}, n}^{\text {new }}}
\end{aligned}
$$

into (43), to derive the instantaneous estimate

$$
\begin{aligned}
C_{\mathbf{w}, n}^{\text {new }} & =\frac{1}{M} \mathcal{E}_{\mathbf{h}_{1: n} \mid \theta_{n}}\left\{\left(\mathbf{h}_{n}-\mathbf{h}_{n-1}\right)^{\mathrm{T}}\left(\mathbf{h}_{n}-\mathbf{h}_{n-1}\right)\right\} \\
& \stackrel{(27)}{=} C_{\mathbf{h}, n}-C_{\mathbf{h}, n-1} \\
& +\frac{1}{M}\left(\hat{\mathbf{h}}_{n}^{\mathrm{T}} \hat{\mathbf{h}}_{n}-\hat{\mathbf{h}}_{n-1}^{\mathrm{T}} \hat{\mathbf{h}}_{n-1}\right)
\end{aligned}
$$

where we employed the statistical independence between $\mathbf{w}_{n}$ and $\mathbf{h}_{n-1}$. Equation (46) states that $C_{\mathbf{w}, n}^{\text {new }}$ is estimated as difference of the filter tap autocorrelations between the time instants $n$ and $n-1$. Finally, the updated parameter values are used as initialization for the following time step, so that

$$
C_{\mathbf{w}, n+1}:=C_{\mathbf{w}, n}^{\text {new }}, \quad C_{v, n+1}:=C_{v, n}^{\text {new }}
$$

Note that this approximated ML solution is only guaranteed to converge to a locally but not necessarily globally optimum solution [32].

### 4.2 NLMS algorithm with fixed stepsize value [38]

In the previous section, we estimated the model parameters $\theta_{n}$ by approximating the ML problem in (41). For some applications, it might be promising to manually set the values of $C_{v, n}$ and $C_{\mathbf{w}, n}$. This is done in the following leading to the NLMS algorithm with a fixed stepsize value:

- The uncertainty $\mathbf{w}_{n}$ is equal to zero by choosing $C_{\mathbf{w}, n}=0$ in (10).
- The variance of the microphone signal uncertainty $C_{v, n}$ is proportional to the current loudspeaker power and the estimation uncertainty $C_{\mathbf{h}, n-1}$ :

$$
C_{v, n}=\tilde{\alpha} \mathbf{x}_{n}^{\mathrm{T}} \mathbf{x}_{n} C_{\mathbf{h}, n-1}, \quad \text { where } \quad \tilde{\alpha} \geq 0
$$

Inserting both assumptions into (34) leads to the filter update of the NLMS algorithm

$$
\begin{aligned}
\hat{\mathbf{h}}_{n} & =\hat{\mathbf{h}}_{n-1}+\frac{C_{\mathbf{h}, n-1} \mathbf{x}_{n} e_{n}}{\mathbf{x}_{n}^{\mathrm{T}} \mathbf{x}_{n} C_{\mathbf{h}, n-1}+\tilde{\alpha} \mathbf{x}_{n}^{\mathrm{T}} \mathbf{x}_{n} C_{\mathbf{h}, n-1}} \\
& =\hat{\mathbf{h}}_{n-1}+\frac{\alpha}{\mathbf{x}_{n}^{\mathrm{T}} \mathbf{x}_{n}} \mathbf{x}_{n} e_{n}
\end{aligned}
$$

with fixed stepsize value

$$
\alpha=(1+\tilde{\alpha})^{-1}
$$

Interestingly, the resulting stepsize $\alpha$ is from the interval typically chosen for an NLMS algorithm: if the additive uncertainty is equal to zero $\left(C_{v, n} \stackrel{(48)}{=} 0\right.$ for $\tilde{\alpha}=0$ ), the stepsize reaches the maximum value of $\alpha \stackrel{(50)}{=} 1$. With increasing additive uncertainty $\left(C_{v, n} \stackrel{(48)}{=} \infty\right.$ for $\left.\tilde{\alpha} \rightarrow \infty\right)$, the stepsize decreases and tends to zero.

## 5 A Bayesian view on nonlinear AEC

In this section, we consider the nonlinear AEC scenario of Fig. 4 and compare both realizations of the state vector in (22) and (23) to compare models having a linear (LIC

models) or nonlinear (NIC models) relation between the observation and the coefficients of the state vector.

### 5.1 LIC model: Hammerstein group models

Following the definition of the state vector in (23), we define the state-space model as follows:

$$d_n \stackrel{(24)}{=} \mathbf{x}_n^T \mathbf{y}_n + v_n, \quad \mathbf{z}_n = \mathbf{z}_{n-1} + \mathbf{w}_n, \tag{51}$$

where $\mathbf{y}_n = \left[\mathbf{x}_n^T, \Phi_1[\mathbf{x}_n]^T, \ldots, \Phi_P[\mathbf{x}_n]^T\right]^T$.

Note that (51) is similar to (25) with the difference that the state vector $\mathbf{z}_n$, the input signal vector $\mathbf{y}_n$, and the uncertainty $\mathbf{w}_n$ are extended by $M$. $P$ values. Thus, applying equivalent assumptions as in Section 4.2 leads to the filter update

$$\hat{\mathbf{z}}_n = \hat{\mathbf{z}}_{n-1} + \frac{\alpha}{\mathbf{y}_n^T \mathbf{y}_n} \mathbf{y}_n \left( d_n - \hat{\mathbf{z}}_n-1^T \mathbf{y}_n \right) \tag{53}$$

for $\hat{\mathbf{z}}_n \stackrel{(23)}{=} \left[ \hat{\mathbf{z}}_n,1^T, \hat{\mathbf{z}}_n,2^T, \ldots, \hat{\mathbf{z}}_n,P+1 \right]^T$.

As illustrated in Fig. 7, this represents the realization of $P + 1$ parallel NLMS algorithms with individually preprocessed loudspeaker signal $\mathbf{x}_n$. One advantage of this Hammerstein group model is the application of well-known linear FIR filters to identify a nonlinear electroacoustic echo path. However, this is at the cost of an increased number of coefficients to be estimated. It should be emphasized that this Bayesian network view on the Hammerstein group model is considered here for the first time.

### 5.2 NIC model: numerical sampling

In cases where the observation equation of (21) represents an NIC model due to the definition of the state vector in (22), we cannot analytically derive the Bayesian estimate of $\hat{\mathbf{z}}_n$ in a closed form. Thus, we employ particle filtering to approximate the posterior PDF in (32) by a discrete distribution [30, 39]:

![img-6.jpeg](img-6.jpeg)

**Fig. 7** Hammerstein group model to estimate $\hat{d}_n = \hat{\mathbf{z}}_n-1^T \mathbf{y}_n$ with $\hat{\mathbf{z}}_n$ and $\mathbf{y}_n$ defined in (54) and (52), respectively

$$\begin{aligned}
p\left(\mathbf{z}_n \mid d_{1:n}\right) &\stackrel{(32)}{=} \frac{p(d_n \mid \mathbf{z}_n) p(\mathbf{z}_n \mid d_{1:n-1})}{\int p(d_n \mid \mathbf{z}_n) p(\mathbf{z}_n \mid d_{1:n-1}) \mathrm{d}\mathbf{z}_n} \\
&\approx \sum_{l=1}^{L} \frac{p\left(d_n \mid \mathbf{z}_n^{(l)}\right) \delta\left(\mathbf{z}_n - \mathbf{z}_n^{(l)}\right)}{\sum_{l=1}^{L} \int p\left(d_n \mid \mathbf{z}_n^{(l)}\right) \delta\left(\mathbf{z}_n - \mathbf{z}_n^{(l)}\right) \mathrm{d}\mathbf{z}_n} \\
&= \sum_{l=1}^{L} \omega_n^{(l)} \delta\left(\mathbf{z}_n - \mathbf{z}_n^{(l)}\right),
\end{aligned} \tag{55}$$

where $\delta(\cdot)$ is the Dirac delta distribution. Based on (55), the set of $L$ realizations of the state vector $\mathbf{z}_n^{(l)}$ (so-called particles) is characterized by the weights

$$\omega_n^{(l)} = \frac{p\left(d_n \mid \mathbf{z}_n^{(l)}\right)}{\sum_{l=1}^{L} p\left(d_n \mid \mathbf{z}_n^{(l)}\right)} \stackrel{(7)}{=} \frac{\mathcal{N}\left(d_n \mid d_n^{(l)}, C_{v,n}\right)}{\sum_{l=1}^{L} \mathcal{N}\left(d_n \mid d_n^{(l)}, C_{v,n}\right)},\tag{56}$$

which describe the likelihoods that the observation is obtained by the corresponding particle (as measures for the probability of the samples to be drawn from the true PDF [40]). To calculate the weights in (56), the particles are plugged into (18) to determine the estimated microphone samples $d_n^{(l)}$.

Due to the definition of the discrete posterior PDF in (55), the MMSE estimate for the state vector is given by the mean vector

$$\hat{\mathbf{z}}_n \stackrel{(12)}{=} \mathcal{E}\left\{\mathbf{z}_n \mid d_{1:n}\right\} \approx \sum_{l=1}^{L} \omega_n^{(l)} \mathbf{z}_n^{(l)}. \tag{57}$$

This fundamental concept is illustrated in Fig. 8 and can be summarized as follows [9]:

- **Starting point:** $L$ particles $\mathbf{z}_n^{(l)}$.
- **Measurement update:** Calculate the weights $\omega_n^{(l)}$ and determine the posterior PDF $p\left(\mathbf{z}_n \mid d_{1:n}\right)$ (see (56) and (55), respectively).
- **Time update:** Replace all particles by $L$ new samples drawn from the posterior PDF [30]

$$p\left(\mathbf{z}_{n+1} \mid d_{1:n}\right) = \sum_{l=1}^{L} \omega_n^{(l)} p\left(\mathbf{z}_{n+1} \mid \mathbf{z}_n^{(l)}\right),\tag{58}$$

![img-7.jpeg](img-7.jpeg)

**Fig. 8** Concept of the classical particle filter

which is equivalent to sampling from *p*(**z**_{*n*}|*d*_{1:}_{*n*}) and subsequently adding one realization of the uncertainty **w**_{*n*+1} defined in (10)^{1}. This is the starting point for the next iteration step.

Unfortunately, the classical particle filter (initially proposed for tracking applications) is conceptually ill-suited for the task of nonlinear AEC: it is well known that the performance degrades with increasing search space and that the local optimization problem is solved without generalizing the instantaneous solution (see the weight calculation in (56)) [41–43]. These properties of the classical particle filter are severe limitations for the task of nonlinear AEC with its high-dimensional state vector (see (22)). To cope with these conceptional limitations without introducing sophisticated resampling methods [40, 44], the elitist particle filter based on evolutionary strategies (EPFES) has been recently proposed in [9]. As major modifications for the task of nonlinear AEC, an evolutionary selection process facilitates to evaluate realizations of the state vector based on recursively calculated particle weights to generalize the instantaneous solution of the optimization problem [9]. These fundamental properties of the EPFES will be illustrated for the state-space model of (7) in the next part.

*EPFES* [9]: As first modification with respect to the classical particle filter, the particle weights are recursively calculated

$$
\omega_n^{(l)} = \gamma \omega_{n-1}^{(l)} + (1 - \gamma) \frac{p\left(d_n \mid \mathbf{z}_n^{(l)}\right)}{\sum_{l=1}^L p\left(d_n \mid \mathbf{z}_n^{(l)}\right)}, \tag{59}
$$

where *γ* is the so-called forgetting factor. Following concepts from the field of evolutionary strategies (ES) [45], we subsequently select *Q*_{*n*} elitist particles **z̃**_{*n*}^{(q_{n})} with weights larger than a threshold *ω*_{th} to determine the posterior PDF *p*(**z**_{*n*}|*d*_{1:}_{*n*}) (and the MMSE estimate **z̃**_{*n*} as its mean vector) by replacing {**z**_{*n*}^{(l)}, *ω*_{*n*}^{(l)}} in (55) by the set of elitist particles and respective weights {**z̃**_{*n*}^{(q_{n})}, *ω̃* (_{*n*}^{(q_{n})}}. Subsequently, *L* − *Q*_{*n*} new samples drawn from the posterior PDF *p*(**z**_{*n*}|*d*_{1:}_{*n*}) replace the non-elitist particles and complete the set of particles for realizing the time update. These steps are illustrated in Fig. 9 and can be summarized as follows:

- *Starting point*: *L* particles **z**_{*n*}^{(l)} with weights *ω*_{*n*−1}^{(l)} determined in the previous time step.
- *Measurement update*: Update weights *ω*_{*n*}^{(l)} in (59), select elitist particles, and determine *p*(**z**_{*n*}|*d*_{1:}_{*n*}) by inserting the set of elitist particles **z̃**_{*n*}^{(q_{n})} and weights *ω̃* (_{*n*}^{(q_{n})} into (55).
- *Time update*: Replace the non-elitist particles by new samples drawn from the posterior PDF *p*(**z**_{*n*}|*d*_{1:}_{*n*}).

![img-8.jpeg](img-8.jpeg)

**Fig. 9** Concept of the EPFES

Furthermore, add realizations of **w**_{*n*+1} (following (7)) to the set of particles (containing *Q*_{*n*} elitist particles and *L* − *Q*_{*n*} new samples). This is the starting point for the next iteration step^{2}.

It has been shown that these modifications of the classical particle filter generalize the instantaneous solution of the optimization problem and thus allow to identify the nonlinear-linear cascade in Fig. 4 [9]. However, the EPFES evaluates realizations of the state vector based on long-term fitness measures. This leads to a high computational complexity due to the high dimension of the state vector in (22). Although many real-time implementations of particle filters have been proposed using parallel processing units [46, 47], it might be necessary for typical applications of nonlinear AEC (e.g., in mobile devices) to reduce the computational complexity to meet specific hardware constraints. Note that a very efficient solution for this problem is the so-called significance-aware EPFES (SA-EPFES) proposed in [19], where the NLMS algorithm (to estimate the linear component of the AEC scenario) is combined with the EPFES (to estimate the loudspeaker signal distortions) by applying significance-aware (SA) filtering. In short, the fundamental idea of SA filtering is to reduce the computational complexity by exploiting physical knowledge about the most significant part of the linear subsystem to estimate the coefficients of the nonlinear preprocessor [18]. Thus, the state vector in (22) underlying the derivation of the SA-EPFES models the coefficients of the nonlinear preprocessor and a small part of the impulse response around the highest energy peak (to capture estimation errors of the NLMS algorithm in the direct-path region).

## 6 Experimental performance

This overview article establishes a unifying Bayesian network view on linear and nonlinear AEC with the goal to drive future research by highlighting the idealizations and limitations in the probabilistic models of existing methods. Note that a detailed analysis of the adaptive

algorithms described in the previous sections has already been performed in [18, 19]. Therefore, we briefly summarize the main findings without explicitly detailing the practical realizations of the algorithms (see $[18,19]$ for more details). For a recorded female speech signal (commercial smartphone placed on a table with display facing the desk) in a medium-size room with moderate background noise ( $\mathrm{SNR} \approx 40 \mathrm{~dB}$ ), the NLMS algorithm (length-256 FIR filter at 16 kHz ) achieved an average echo return loss enhancement (ERLE) of 8.2 dB in a time interval of 9 s [19]. Compared to this, the Hammerstein group model and the SA-EPFES improve the average ERLE by 34 and $68 \%$ at a computational complexity increased by 27 and $50 \%$, respectively [19]. To achieve these results, the Hammerstein group model (termed as SA-HGM in [18]) and the SA-EPFES are realized based on the concept of SA filtering [18] (11 filter taps for the direct-path region of the RIR) by using length-256 FIR filters and a third-order memoryless preprocessor (inserting odd-order Legendre functions into (18)).

## 7 Conclusions

In this article, we derived a set of conceptually different algorithms for linear and nonlinear AEC from a unifying graphical model perspective. Based on a concise review of Bayesian networks, we introduced a state-space model with latent state vector capturing all relevant information of the unknown system. After this, we employed three combinations of state-vector definitions (to model a linear or nonlinear echo path) and observation equations (mathematical relation between state vector and observation) to apply fundamental techniques of machine learning research. Thereby, it is shown that the NLMS algorithm, the Hammerstein group model (considered from this perspective here for the first time), and a numerical sampling scheme for nonlinear AEC can be derived from a unifying Bayesian network perspective. This viewpoint highlights probabilistic assumptions underlying different derivations and serves as a basis for developing new algorithms for linear and nonlinear AEC and similar tasks. An example for future work is a Bayesian view on a nonlinear AEC scenario, where the nonlinear loudspeaker signal distortions are modeled by a nonlinear preprocessor with memory.

## Endnotes

${ }^{1}$ Note that sampling from the posterior PDF $p\left(\mathbf{z}_{n+1} \mid d_{1: n}\right) \stackrel{(1)}{=} \sum_{i=1}^{L} \omega_{n}^{(i)} \mathcal{N}\left(\mathbf{z}_{n+1} \mid \mathbf{z}_{n}^{(i)}, C_{\mathbf{w}, n+1} \mathbf{I}\right)$ is equivalent to adding samples drawn from the discrete $\operatorname{PDF} p\left(\mathbf{z}_{n} \mid d_{1: n}\right)$ in (55) and the Gaussian PDF $p\left(\mathbf{w}_{n+1}\right)$ in (10).
${ }^{2}$ In practice, the weights of the new samples for the recursive update in (56) are initialized by the value $\omega_{1 h}$.

## Competing interests

The authors declare that they have no competing interests.

## Authors' information

RM was with the University of Erlangen-Nuremberg while the work has been conducted. He is now with Amazon, Seattle, WA.

## Acknowledgements

The authors would like to thank the Deutsche Forschungsgemeinschaft (DFG) for supporting this work (contract number KE 890/4-2).

Received: 25 June 2015 Accepted: 6 November 2015
Published online: 25 November 2015

## Submit your manuscript to a SpringerOpen ${ }^{\circledR}$ journal and benefit from:

- Convenient online submission
- Rigorous peer review
- Immediate publication on acceptance
- Open access: articles freely available online
- High visibility within the field
- Retaining the copyright to your article

Submit your next manuscript at $\rightarrow$ springeropen.com