# Multiple Acoustic Source Localization in Microphone Array Networks 

Jielong Yang, Weiguang Chen, Xionghu Zhong, and Wenwu Wang


#### Abstract

The problem of multiple acoustic source localization using observations from a microphone array network is investigated in this paper. Multiple source signals are assumed to be window-disjoint-orthogonal (WDO) on the time-frequency (TF) domain and time delay of arrival (TDOA) measurements are extracted at each TF bin. A Bayesian network model is then proposed to jointly assign the measurements to different sources and estimate the acoustic source locations. Considering that the WDO assumption is usually violated under reverberant and noisy environments, we construct a relational network by coding the distance information between the distributed microphone arrays such that adjacent arrays have higher probabilities of observing the same acoustic source, which is able to mitigate the miss detection issues in adverse environments. A Laplace approximate variational inference method is introduced to estimate the hidden variables in the proposed Bayesian network model. Both simulations and real data experiments are performed. The results show that our proposed method is able to achieve better source localization accuracy than existing methods.


Index Terms-Acoustic Source Localization, Time-Frequency Masking, Time-Delay of Arrival, Bayesian Network, Laplace Approximate Variational Inference

## I. INTRODUCTION

ACOUSTIC source localization (ASL) in a room environment plays an important role in many speech and audio applications such as multimedia, hearing aids, handsfree speech communication, and teleconferencing systems as the location information can be fed into a higher processing stage for high-quality speech acquisition, enhancement of a specific speech signal in the presence of other competing talkers, or directing a camera towards the acoustic source [1], [2], [3], [4], [5], [6]. However, it is a difficult task to provide an accurate position estimate since the received audio signal can be significantly distorted and its statistical properties can be changed drastically due to room reverberation and noise. The difficulty is further increased when multiple sources are simultaneously active in the localization scene. Distributed acoustic sensor networks composed of a number of randomly deployed microphones or microphone arrays have been increasingly attractive for ASL due to their higher flexibility and

[^0]scalability, and better spatial coverage compared to a single microphone or microphone array.

In the past, methods based on time-delay of arrival (TDOA) measurements are extensively employed and studied for ASL [7], [8], [9], [10], [11], [12], [13], [14], [15], [16] due to their simplicity and ease of access in many applications. TDOA measurements can be extracted, for example, by employing the generalized cross-correlation (GCC) function [17] or adaptive eigenvalue decomposition (AED) algorithm [18]. Since each TDOA yields half a hyperholoid of two sheets which, in the far field, can be approximated by an angular segment, multiple TDOA measurements from distributed microphone arrays are usually employed to triangulate a target position [19], [20]. Such a triangulation can be approximated by either using a linear intersection (LI) algorithm [21] or an extended Kalman filter (EKF) [13], [16]. In [22], the authors consider the 2D source localization problem using TDOA at a minimal element monitoring arrays in both Cartesian and polar coordinate systems. However, in the presence of noise and room reverberation, ghost peaks may present in the GCC function and spurious TDOA measurements may be collected and the subsequent triangulation methods can be seriously degraded. In [23], a TDOA denoising method is proposed such that better localization performance can be achieved by using TDOA measurements. In [24], a TDOA outlier removal method is proposed to enhance the localization accuracy. In [25], the authors show the sufficient and necessary conditions of the uniqueness of localizing a single acoustic source and propose a geometric formulation to estimate the sound source using observations from arbitrarily shaped microphone arrays. However, in [23], [24] and [25], only one source is active at each time instance.

In a real conversation, multiple talkers can also be simultaneously active and, under such a scenario, the received signal is a mixture of different speech sources. This significantly increases the complexity of the ASL problem since: $i$ ) TDOAs for multiple sources are no longer easily available; and $i i$ ) given the TDOA measurements for multiple sources, the measurement-to-source assignment is unknown.

Many methods are proposed to obtain TDOAs for multiple sources. Knowing that traditional GCC methods may not yield sharp peaks for TDOAs of multiple sources, a degenerate unmixing estimation technique (DUET) [26], [27] is introduced to extract the measurement set for multiple sources. In DUET, the source signals are assumed to be window-disjointorthogonal (WDO) in the time-frequency (TF) domain. Hence, the TF spectrogram of sources can be considered as separated and the phase difference of the arrived signal due to


[^0]:    J. Yang is with the School of Artificial Intelligence, Jilin University, China. Part of the work was done in Hunan University and PingAn Smart City. Email: jyang022@e.ntu.edu.sg.
    X. Zhong and W. Chen are with the College of Computer Science and Electronic Engineering, Hunan University, China. Emails: \{xzhong, and cwg\}@hnu.edu.cn
    W. Wang is with the Department of Electrical and Electronic Engineering, University of Surrey, United Kingdom. Email: w.wang@surrey.ac.uk
    J. Yang and W. Chen contribute equally to this work.
    X. Zhong is the corresponding author.

each source can be extracted. Mandel et al [28] also built a probabilistic models for phase difference and attenuation ratio information and used an expectation-maximization (EM) algorithm to find the TDOAs of multiple sources. However, the EM algorithm needs a burn-in period to converge to the final estimates. Other multi-source TDOA estimation methods based on signal separation for localization problem can also be found in [29], [30], [31], [32], [33], [34], [35].

Various source localization and data association methods are also studied in the literature. In [36], [37], grid-based methods are proposed to localize multiple sound sources using the DOA estimates of each microphone array. In [38], a versatile blind signal processing framework is proposed, which provides a unified treatment of both blind signal separation problem and multichannel blind deconvolution problem. Blind signal separation is used in [39] to extract DOA measurements and an intersection point selection scheme is introduced to locate multiple sources. However, the method does not consider miss detection issue. In [40], a method called Acoustic Simultaneous Localization and Mapping (aSLAM) is proposed to simultaneously map the 3D positions of multiple sound sources and to passively localize a moving observer. In this method, the observer's spatio-temporal diversity is used to probabilistically triangulate the source positions. In [41], a multi-view soundfield imaging method is proposed, which generalize the previous method from a single array to multiple arrays. In [42], the authors develop a two stage method and the method uses DOA estimates of microphone arrays to first estimate association features that describe how the frequency components of the captured signals are distributed to the sources, then both DOA estimates and association features are used to localize sound sources. In [43], the authors regard the data association problem as a measurement set partition task, which is further transformed into a generalized multidimensional assignment problem. The methods in [42], [43] deal with both the source localization and the missed detection problem. However, all these methods in the literature do not consider the location relationships between microphone arrays.

In the presence of noise and reverberation, and in particular, when the source is located at far-field, signal to noise ratio (SNR) and signal to reverberation ratio (SRR) can be low and the spectrogram is usually smeared and blurred. The WDO assumption is thus violated. However, it is observed from Fig. 1 that adjacent microphones are highly likely to be able to detect the same source, and vice versa. Hence, the information of distance between each pair of sources is essentially important to measurement-to-source association. In this work, such information is coded and exploited such that adjacent arrays have higher detection probabilities to the same acoustic source, which is able to mitigate the miss detection issue in the presence of reverberation. A relational network-based Bayesian network model is constructed and a Laplace approximate variational inference method is then introduced to estimate the hidden variables indicating the measurement-to-source associations and the corresponding source positions.

It is worth mentioning that several source localization methods focusing on the DOA estimation rather than estimation

![img-0.jpeg](img-0.jpeg)

Fig. 1: Illustration of the localization scene using a microphone array network.

of the exact Cartesian (x, y) positions of the sources have been developed. In [44], [45], [46], [47], dynamic sources are considered and a random finite set based Bayesian filtering approach was presented to track the sources. In [48], binaural cues, interal time difference and intensity difference were extracted from a microphone pair, and these observations are compared with predicted reference values obtained from simulations using prior knowledge of a catalogue head-related transfer functions (HRTFs). These reference values are obtained based on the binaural response of a KEMAR dummy head. The target space is modeled as a set of subspaces and switches among them with predefined jump probabilities. In [49], a distributed algorithm is proposed to estimate DOAs of multiple speech sources. In [50], an independent component analysis based approach was introduced to demix the speech mixtures from multiple sources and a probability hypothesis density filter was employed to track the DOAs of the sources.

The main contributions of this paper are: i) We develop a Bayesian-network-based learning method to jointly associate the TDOAs from each spectrogram bin to different sources and estimate the source locations; ii) our method considers both the missed detection problem and the data association problem; and iii) our method incorporates the distance information among arrays to improve the localization performance. The rest of this paper is organized as follows: in Section II, the DUET-based TDOA measurement extraction is introduced and ASL framework is formulated; in Section III, the inference algorithm is presented; the performance of the proposed approach is studied in Section IV. Finally, conclusions are drawn and directions for future work are discussed in Section V. A list of notations is summarized in below to illustrate the meaning of variables and symbols in the measurement extraction and localization algorithms.

*Notations:* We use boldfaced characters to represent vectors and matrices. Suppose that **A** is a matrix, then **A**(m,·), **A**(·, m), and **A**(m, n) denote its m-th row, m-th column, and (m, n)-th element, respectively. The vector (x1,...,xN) is abbreviated as (xi)N1, or (xi), if i is running over the vector index. We use Cat(p1,...,ppK), Dir(α1,...,αK), Unif(a,b), Unif(1,...,R), Be(pp, hp) and N(M, V) to represent the categorical distribution with category probabil-

TABLE I: Summary of commonly-used symbols


ities $p_{1}, \ldots, p_{K}$, the Dirichlet distribution with concentration parameters $\frac{\alpha}{K}, \ldots, \frac{\alpha}{K_{i}}$, the uniform distribution over the interval $(a, b)$, the uniform distribution over the discrete set $\{1, \ldots, R\}$, the beta distribution with shape parameters $\left(g_{0}, h_{0}\right)$, and the normal distribution with mean $\mathbf{M}$ and covariance $\mathbf{V}$, respectively. We use $\Gamma(\cdot)$ and $\Psi(\cdot)$ to denote the gamma function and digamma function, respectively. The notation $\sim$ means equality in distribution. The notation $p(y \mid x)$ denotes a conditional probability density function of a random variable $y$ conditioned on $x$. $\mathbb{E}$ is the expectation operator and $\mathbb{E}_{q}$ is expectation with respect to the probability distribution $q$. We use $I(a, b)$ and $I(a>b)$ to denote the indicator function. $I(a, b)=1$ if $a=b$ and 0 otherwise. $I(a>b)=1$ if $a>b$ and 0 otherwise. The notation $\|\cdot\|$ denotes the $l_{2}$ norm, and $\operatorname{ones}(1, K)$ is a $1 \times K$ vector with all entries equal to one.

## II. Problem Formulation and Model

In this section, the problem of multiple acoustic source localization is formulated. TDOA measurements at each TF bin across different microphone arrays are estimated and a Bayesian network is then developed to jointly assign the measurements to the corresponding sources and estimate the position of each source.

## A. Measurement extraction over distributed arrays

Assume that $N$ microphone arrays are deployed to receive the speech signals emitted by $K$ speakers at a discrete time step $t$. Let $\omega$ be a TF bin index, and $S_{k}=\left(S_{k, \omega}\right)_{\omega}$ denotes the short time Fourier transform (STFT) of the $k$-th source signal. Ignoring the effect of noise and reverberation, the signal model in the TF domain for the $i$-th microphone of the $n$-th array is

$$
Z_{n, i}(\omega)=\sum_{k=1}^{K} a_{n, i}(k) e^{-j \omega \tau_{n, i}(k)} S_{k, \omega}
$$

where $a_{n, i}(k)=\frac{1}{4 \pi r_{n, i}(k)}$ represents the attenuation with $r_{n, i}(k)$ denoting the corresponding distance from source $k$ to the $i$-th microphone of the $n$-th array, and $\tau_{n, i}(k)$ represents
the time-delay of the $k$-th source signal at the $i$-th microphone of $n$-th microphone pair. According to the WDO assumption [26], the TF bins are disjoint. Hence, each TF bin carries either information regarding one of the sources, or simply noise.

Here we consider the case where each array has two microphones. The solution for arrays with more than two microphones can be extended in a straightforward manner. The ratio of the TF bins across a microphone pair is given by

$$
R_{n}(\omega)=\frac{Z_{n, 1}(\omega)}{Z_{n, 2}(\omega)}=a_{n}(\omega) e^{-j \omega y_{n}(\omega)}
$$

where $a_{n}(\omega)$ and $y_{n}(\omega)$ are the gain-ratio (GR) and timedelay of arrival (TDOA) estimates for TF bin $\omega$ respectively. Suppose that the $k$-th source is active on $\omega$ (the contribution of other sources on this TF bin is thus nil), the GR and TDOA are given respectively as

$$
\begin{aligned}
& a_{n}(\omega)=\left|R_{n}(\omega)\right|=\frac{a_{n, 1}(k)}{a_{n, 2}(k)} \triangleq a_{n}(k) \\
& y_{n}(\omega)=\frac{\angle R_{n}(\omega)}{-\omega}=\tau_{n, 1}(k)-\tau_{n, 2}(k) \triangleq \tau_{n}(k)
\end{aligned}
$$

with $|\cdot|$ and $\angle \cdot$ denoting the amplitude and the phase of the estimates respectively, and $a_{n}(k)$ and $\tau_{n}(k)$ are the GR and TDOA information of the $k$-th source, respectively. Note that the TF bin index $\omega$ can be omitted in (3) as the GRs and TDOAs are determined by the geometry of the source and the microphone arrays, and thus the same across different TF bins associated to a source.

Based on the GR and TDOA parameters, a histogram of all TF bins can be generated and the TF bins for each source can thus be clustered and separated in the TF domain. TDOAs for multiple sources can hence be associated and the position of each source can be triangulated accordingly. Assume that at the $n$-th, for $n=1, \ldots, N$ microphone array, a set of TDOAs $\mathbf{y}_{n}(\omega)=\left\{y_{n}(1), \ldots, y_{n}(\Omega)\right\}$ is obtained by using DUET. Such a TDOA set contains the source generated TDOAs as well as false TDOAs when reverberation and noise are considered.

![img-1.jpeg](img-1.jpeg)

Fig. 2: Our proposed Bayesian network model.

Let **l**<sup>*k*</sup> denote the location of the *k*-th source. For the measurement generated by the *k*-th source, its relationship to the location of the source is given by

$$y_n(\omega^k) = \frac{\|\mathbf{l}_k - \mathbf{p}_{n,1}\| - \|\mathbf{l}_k - \mathbf{p}_{n,2}\|}{c}.\tag{4}$$

where **p**<sub>*n*,*i*</sub>, *i* ∈ {1, 2} is the position of the *i*-th microphone of the *n*-th array and ω<sup>*k*</sup> represents that TF bin ω is associated to source *k*. Equation (4) shows that the source positions can be estimated by using correctly assigned measurements. However, in the presence of noise and reverberation, the spectrogram is smeared and blurred. The WDO assumption is violated and such a clustering-based method is no longer valid, i.e., it is very difficult to associate the TDOAs due to the same source and consequently, the location estimates can be significantly deviated from the ground truth.

### *B. Bayesian network model for measurement-to-source association*

Consider *N* microphone arrays monitoring *K* sound sources. The ground truth Cartesian coordinates of sources are **l** = {**l**<sub>*k*</sub>}<sub>*k* = 1</sub>, which is the random variable we want to estimate. Let **l**<sup>*i*</sup> = {**l**<sub>*n*</sub>}<sub>*N*<sup>*i*</sup> = 1</sub> be the locations of arrays. The locations of the arrays and the number of sources are known. We generate *F* frequency bins at each time-frame and use observations of *T* time frames and thus in total Ω ≜ *T* × *F* time frequency bins are considered.

Let **y** = {*y*<sub>*n*</sub>(*ω*)}<sub>*n*,ω</sub> be the collection of the measurements where *y*<sub>*n*</sub>(*ω*) is the observation corresponding to the ω-th time frequency bin of the received signal of array *n*, and *s*<sub>*n*</sub>(*ω*) be the index of the source signal that ω-th time frequency bin of array *n* mainly comes from. Then we have the following observation model

$$p(y_n(\omega) \mid s_n(\omega) = k, \mathbf{l}_k) = \mathcal{N}\left(f(\mathbf{l}_k, \mathbf{l}_n^0, \ \sigma^2), \tag{5}$$

where σ is the known observation variance and *f*(**l**<sub>*k*</sub>, **l**<sup>*i*</sup><sub>*n*</sub>) is a known nonlinear function and depends on the structure of the arrays and the observation *y*<sub>*n*</sub>(ω). Two examples of *f*(**l**<sub>*k*</sub>, **l**<sup>*i*</sup><sub>*n*</sub>) are as follows:

1. If *y*<sub>*n*</sub>(ω) is the DOA of the ω-th TF bin of the signal received by array *n*, then *f*(**l**<sub>*k*</sub>, **l**<sup>*i*</sup><sub>*n*</sub>) ≜

$$\arctan\left(\frac{l_k(2) - l_n^0(2)}{l_k(1) - l_n^0(1)}\right).$$

2. If the number of microphones in each array is 2 and *y*<sub>*n*</sub>(ω) is the TDOA of the ω-th TF bin of array *n*. Then *f*(**l**<sub>*k*</sub>, **l**<sup>*i*</sup><sub>*n*</sub>) ≜

$$\frac{\|\mathbf{l}_k - \mathbf{l}_n^0\|}{c}, \text{ where } c \text{ is the sound speed.}$$

The signal received by array *n* may come from multiple sound sources. Let **π**<sub>*n*</sub> = {*π*<sub>*n*,*k*</sub>}<sub>*k*</sub>, where *π*<sub>*n*,*k*</sub> is the probability of *s*<sub>*n*</sub>(ω) = *k*, namely

$$s_n(\omega) \sim \text{Cat}\left(\pi_n\right).\tag{6}$$

In (6), *s*<sub>*n*</sub>(ω) is a cluster index and in our method. We cluster the observation *y*<sub>*n*</sub>(ω) by estimating *s*<sub>*n*</sub>(ω). In our model, we not only cluster time-frequency bins of the same array, but also cluster time-frequency bins across different arrays. To achieve this, we use the same hierarchical model for any *n* ∈ {1, 2, ..., *N*}, given as

$$\pi_n \sim \text{Dir}\left(\overline{\pi} + \alpha\right),\tag{7}$$

where α is a known hyper parameter and

$$\overline{\pi} \le \{\overline{\pi}_k\}_k=1^K \sim \text{LogNormal}\left(\mathbf{M}, \mathbf{V}\right) \tag{8}$$

with **M** and **V** being known hyper parameters. In (8), the log normal distribution ensures that all the elements of *π̄* are positive. In (7), we use the Dirichlet distribution since the support of a Dirichlet distribution can be regarded as the probabilities of categorical events. Besides, the Dirichlet distribution is the conjugate prior distribution of the categorical distribution in (7), which helps to compute the posterior distribution in Bayesian inference.

Apart from observations **y**, we also use the geometry relationships among arrays as arrays have higher probability to observe the same source when they are closely located. Let *z*<sub>*n*→*m*</sub> be the cluster (i.e., source) index array *n* belongs to under the influence of array *m*. Let **D**(*n*, *m*) be the distance between array *n* and array *m*. We assume *z*<sub>*n*→*m*</sub> | **π**<sub>*n*</sub> ∼ Cat(**π**<sub>*n*</sub>), *z*<sub>*m*→*n*</sub> | **π**<sub>*m*</sub> ∼ Cat(**π**<sub>*m*</sub>), and β<sub>*k*</sub> ∼ **B**<sub>*e*</sub>(*g*<sub>*0*</sub>, *h*<sub>*0*</sub>), where **B**<sub>*e*</sub>(*g*<sub>*0*</sub>, *h*<sub>*0*</sub>) is the beta distribution with parameters *g*<sub>*0*</sub>, *h*<sub>*0*</sub> > 0, ∀ *k* = 1, ..., *K*, and

$$p(\mathbf{D}(n,m) < d \mid z_{n \rightarrow m}, z_{m \rightarrow n}, \beta_{z_{n \rightarrow m}}) \tag{9}$$

$$= \begin{cases} \beta_{z_{n \rightarrow m}}, & \text{if } z_{n \rightarrow m} = z_{m \rightarrow n}, \\ \epsilon, & \text{if } z_{n \rightarrow m} \neq z_{m \rightarrow n}, \end{cases} \tag{9}$$

with ε being a small constant and *d* is the threshold below which we believe that two arrays are near to each other. In (9), when array *n* and array *m* observe the same source (i.e., *z*<sub>*n*→*m*</sub> = *z*<sub>*m*→*n*</sub>), the probability of **D**(*n*, *m*) < *d* (i.e., array *n* and array *m* are near) is β<sub>*z*{*n*→*m*</sub></sub>, which is much larger than ε. Here ε is the probability of **D**(*n*, *m*) < *d* when array *n* and array *m* observe different sources. After integrating out *z*<sub>*n*→*m*</sub>, *z*<sub>*m*→*n*</sub>, we obtain

$$p(\mathbf{D}(n,m) < d \mid \pi_n, \pi_m, \boldsymbol{\beta}) = \sum_{k=1}^K \pi_{n,k} \pi_{m,k} \beta_k. \tag{10}$$

If $\mathbf{D}(n, m)<d$, we say array $n$ and array $m$ are near to each other. From (10), it can be observed that the probability that array $n$ and array $m$ are close to each other will be high when $\boldsymbol{\pi}_{n}$ and $\boldsymbol{\pi}_{m}$ have larger cosine similarity, which means that $\boldsymbol{\sigma}_{n}$ and $\boldsymbol{\sigma}_{m}$ have high probability of being the same prior, i.e., array $n$ and array $m$ have high probability of observing the same acoustic source. The general Bayesian network model is shown in Fig. 2. The notations and their corresponding meanings are shown in Table I.

## III. INFERENCE ALGORITHM

Our proposed model tries to associate the observations in each array and across different arrays and estimate the locations of sound sources. In this section, we will present our inference algorithm for our Bayesian network model. Usually two kinds of methods are used to infer the parameters of the Bayesian network model, namely Markov Chain Monte Carlo (MCMC) and variational inference method. MCMC is a sampling-based method and can achieve global optimal estimation given infinite number of iterations but it is computationally expensive. For sound source localization applications, the variational inference method is employed due to its properties of guaranteed and fast convergence [51]. However, in our model, priors of some variables are not conjugate to their corresponding likelihood distributions, the traditional variational inference method can thus not be directly used and specific approximations are required.

The hidden random variables we need to estimate are $\mathbf{z} \triangleq\left(z_{n \rightarrow m}\right)_{n, m, n \neq m}, \boldsymbol{\beta} \triangleq\left(\beta_{k}\right)_{k}, \boldsymbol{\pi} \triangleq\left(\boldsymbol{\pi}_{n}\right)_{n}, \widetilde{\boldsymbol{\pi}} \triangleq\left(\widetilde{\pi}_{k}\right)_{k}$, $\mathbf{l} \triangleq\left(\mathbf{l}_{k}\right)_{k}$, and $\mathbf{s}=\left(s_{n}(\omega)\right)_{n, \omega}$. Let $\Upsilon \triangleq\{\mathbf{z}, \boldsymbol{\beta}, \boldsymbol{\pi}, \widetilde{\boldsymbol{\pi}}, \mathbf{l}, \mathbf{s}\}$. We aim at obtaining the joint posterior distribution of hidden variables $p(\boldsymbol{\Upsilon} \mid \mathbf{y}, \mathbf{D})$. In the variational inference method, we aim to find a distribution $q(\boldsymbol{\Upsilon})$ from a distribution family $\mathcal{F}$ to minimize the KL-divergence between $q(\boldsymbol{\Upsilon})$ and $p(\boldsymbol{\Upsilon} \mid \mathbf{y}, \mathbf{D})$. $q(\boldsymbol{\Upsilon})$ is called the joint variational distribution. Following [52], we choose $\mathcal{F}$ to be the mean-field distribution family so that the model is efficient to infer, though we need to sacrifice the optimality. Distributions in $\mathcal{F}$ are distinguished by variational parameters (i.e., parameters of the joint variational distribution) and the optimal distribution $q(\boldsymbol{\Upsilon})$ is found by iteratively updating the variational parameters. We assign a variational parameter for each of the hidden variables in $\boldsymbol{\Upsilon}$, they are

$$
\begin{aligned}
\boldsymbol{\Lambda}= & \left\{\boldsymbol{\phi} \triangleq\left(\boldsymbol{\phi}_{n \rightarrow m, k}\right)_{n, m, n \neq m, k}\right. \\
& \boldsymbol{\lambda} \triangleq\left(\boldsymbol{\lambda}_{k}\right)_{k} \\
& \boldsymbol{\gamma} \triangleq\left(\gamma_{n, k}\right)_{n, k} \\
& \boldsymbol{\xi} \triangleq\left(\xi_{k}\right)_{k} \\
& \boldsymbol{\mu} \triangleq\left(\boldsymbol{\mu}_{k}\right)_{k} \\
& \left.\boldsymbol{\psi} \triangleq\left(\psi_{n, k}(\omega)\right)_{n, k, \omega}\right\}
\end{aligned}
$$

respectively. We aim to find

$$
q^{*}(\boldsymbol{\Upsilon})=\underset{q(\boldsymbol{\Upsilon}) \in \mathcal{F}}{\arg \min } \mathcal{D}_{K L}(q(\boldsymbol{\Upsilon})| | p(\boldsymbol{\Upsilon} \mid \mathbf{y}, \mathbf{D}))
$$

where $\mathcal{D}_{K L}(\cdot| | \cdot)$ is the KL divergence. From [52], solving (11) is equivalent to maximizing the evidence lower bound

$$
\mathcal{L}(q) \triangleq \mathbb{E}_{q(\boldsymbol{\Upsilon})}[\log p(\boldsymbol{\Upsilon}, \mathbf{y}, \mathbf{D})]-\mathbb{E}_{q(\boldsymbol{\Upsilon})}[\log q(\boldsymbol{\Upsilon})]
$$

We solve this problem by iteratively updating the variational parameters according to the updating equations shown below. The updating of the variational parameters are derived in the appendix. The pseudo code of our algorithm is shown in Algorithm 1 and the computation complexity of our algorithm in each iteration is $\mathcal{O}\left(N^{2} K\right)$, where $N$ and $K$ represent the number of arrays and sound sources, respectively.

```
Algorithm 1 Proposed multiple ASL method ( \(i\)-th iteration)
Input: Variational parameters in the \((i-1)\)-th iteration, ob-
    servations \(\mathbf{y}\), and distance matrix \(\mathbf{D}\).
Output: Variational parameters in the \(i\)-th iteration.
    for each array \(n\) in \(\{1, \ldots, N\}\) do
        for each array pair \((n, m)\) in \(\{(n, m)\}_{m=1}^{N}\) do
            Update \(\boldsymbol{\phi}_{n \rightarrow m}\) and \(\boldsymbol{\phi}_{m \rightarrow n}\) using (16) and (17).
        end for
        Update \(\psi_{n}\) using (18).
        Update \(\boldsymbol{\gamma}_{n}\) using (19).
    end for
    Update \(\boldsymbol{\xi}\) using (24).
    Update \(\boldsymbol{\lambda}\) using (13) and (14).
    Update \(\boldsymbol{\mu}\) using (22).
    return \(\boldsymbol{\phi}, \boldsymbol{\psi}, \boldsymbol{\gamma}, \boldsymbol{\xi}, \boldsymbol{\lambda}\), and \(\boldsymbol{\mu}\).
```


## A. Hyper parameters $\boldsymbol{\beta}$

We denote $\boldsymbol{\lambda}_{k}$ as $\left(G_{k}, H_{k}\right)$ and let the variational distribution of $\beta_{k}$ be $q\left(\beta_{k}\right) \triangleq \mathcal{B} e\left(G_{k}, H_{k}\right)$. From [52], we have

$$
\begin{aligned}
G_{k}= & \mathbb{E}_{q(\mathbf{z})}\left[\sum_{(n, m)} I(\mathbf{D}(n, m)<d) I\left(z_{n \rightarrow m}, k\right) I\left(z_{m \rightarrow n}, k\right)\right. \\
& \left.+g_{0}\right] \\
= & \sum_{(n, m)} I(\mathbf{D}(n, m)<d) \phi_{n \rightarrow m, k} \phi_{m \rightarrow n, k}+g_{0} \\
H_{k}= & \mathbb{E}_{q(\mathbf{z})}\left[\sum_{(n, m)} I(\mathbf{D}(n, m) \geq d) I\left(z_{n \rightarrow m}, k\right) I\left(z_{m \rightarrow n}, k\right)\right. \\
& \left.+h_{0}\right] \\
= & \sum_{(n, m)} I(\mathbf{D}(n, m) \geq d) \phi_{n \rightarrow m, k} \phi_{m \rightarrow n, k}+h_{0}
\end{aligned}
$$

where $\phi_{n \rightarrow m, k}$ is defined in (15) as $q\left(z_{n \rightarrow m}=k\right) \triangleq \phi_{n \rightarrow m, k}$. We use $\beta_{k}$ to denote how dense the $k$-th group is. From (13) and (14), it is observed that the variational distribution of $\boldsymbol{\beta}$ is related to the group membership of arrays $\mathbf{z}$ and the distance relationships among arrays $\mathbf{D}$. We also have

$$
\begin{aligned}
\mathbb{E}_{q\left(\beta_{k}\right)}\left[\log \left(\beta_{k}\right)\right] & =\Psi\left(G_{k}\right)-\Psi\left(G_{k}+H_{k}\right), \text { and } \\
\mathbb{E}_{q\left(\beta_{k}\right)}\left[\log \left(1-\beta_{k}\right)\right] & =\Psi\left(H_{k}\right)-\Psi\left(G_{k}+H_{k}\right)
\end{aligned}
$$

which will be used in Section III-B.

## B. Group membership indicators $\mathbf{z}$

We let the variational distribution of the group membership index $z$ be

$$
q\left(z_{n \rightarrow m}=k\right) \triangleq \phi_{n \rightarrow m, k}
$$

From equation (17) in [52], we have

$$
\begin{aligned}
& \phi_{n \rightarrow m, k} \mid \mathbf{D}(n, m)<d \\
& \quad \propto \exp \left\{\phi_{m \rightarrow n, k} \mathbb{E}_{q\left(\beta_{k}\right)}\left[\log \left(\beta_{k}\right)\right]+\left(1-\phi_{m \rightarrow n, k}\right) \log \epsilon\right. \\
& \left.\quad+\mathbb{E}_{q\left(\pi_{n, k}\right)}\left[\log \left(\pi_{n, k}\right)\right]\right\}
\end{aligned}
$$

where $\epsilon$ is a small constant. Thus, $\log \epsilon<\mathbb{E}_{q\left(\beta_{k}\right)}\left[\log \left(\beta_{k}\right)\right]<0$ and $\phi_{n \rightarrow m, k}$ (i.e., $q\left(z_{n \rightarrow m}=k\right)$ ) increases with $\phi_{m \rightarrow n, k}$ when array $n$ and array $m$ are close. Equation (16) holds because of the mean field assumption and $\mathbb{E}\left[I\left(z_{m \rightarrow n}, k\right)\right]=\phi_{m \rightarrow n, k}$. Similarly, we have

$$
\begin{aligned}
\phi_{n \rightarrow m, k} & \mid \mathbf{D}(n, m) \geq d \\
\propto & \exp \left\{\phi_{m \rightarrow n, k} \mathbb{E}_{q\left(\beta_{k}\right)}\left[\log \left(1-\beta_{k}\right)\right]\right. \\
& +\left(1-\phi_{m \rightarrow n, k}\right) \log (1-\epsilon) \\
& \left.+\mathbb{E}_{q\left(\pi_{n, k}\right)}\left[\log \left(\pi_{n, k}\right)\right]\right\}
\end{aligned}
$$

Usually the term $\left(1-\phi_{m \rightarrow n, k}\right) \log (1-\epsilon)$ in (17) can be ignored when $\epsilon$ is small.

## C. Source indices s

Let the variational distribution of community index $s$ be $q\left(s_{n}(\omega)=k\right)=\psi_{n, k}(\omega)$. Then, we have

$$
\begin{aligned}
& \psi_{n, k}(\omega) \\
& \propto \exp \left(-\frac{1}{2 \sigma^{2}}\left[V_{n, k}^{\prime}+\left(M_{n, k}^{\prime}-y_{n}(\omega)\right)^{2}\right]+\mathbb{E}_{q\left(\boldsymbol{\pi}_{n}\right)}\left[\log \left(\pi_{n, k}\right)\right]\right)
\end{aligned}
$$

where $\mathbb{E}_{q\left(\boldsymbol{\pi}_{n}\right)}\left[\log \left(\pi_{n, k}\right)\right]$ is computed using (20), $M_{n, k}^{\prime} \triangleq$ $\mathbb{E}_{q\left(\mathbf{l}_{k}\right)}\left[f\left(\mathbf{l}_{k}, \mathbf{l}_{p}^{\prime}\right)\right]$, and $V_{n, k}^{\prime} \triangleq \mathbb{E}_{q\left(\mathbf{l}_{k}\right)}\left[\left(f\left(\mathbf{l}_{k}, \mathbf{l}_{p}^{\prime}\right)-M_{n, k}^{\prime}\right)^{2}\right]$. Both $M_{n, k}^{\prime}$ and $V_{n, k}^{\prime}$ are computed with the Monte Carlo method and the samples of $\mathbf{l}_{k}$ are drawn from (21).

## D. Source weights $\pi$

Let the variational distribution of the mixture weight $\boldsymbol{\pi}_{n}$ be $q\left(\boldsymbol{\pi}_{n}\right) \triangleq \operatorname{Dir}\left(\boldsymbol{\gamma}_{n}\right)$, where $\gamma_{n}$ is a $K$ dimensional vector, $K$ is the number of sources, then we have

$$
\begin{aligned}
\gamma_{n, k} & =\mathbb{E}_{q\left(\widetilde{\pi}_{k}\right)}\left[\widetilde{\pi}_{k}\right]+\sum_{m=1, m \neq n}^{N} \phi_{n \rightarrow m, k}+\sum_{\omega=1}^{\Omega} \psi_{n, k}(\omega) \\
& =\xi_{k}+\sum_{m=1, m \neq n}^{N} \phi_{n \rightarrow m, k}+\sum_{\omega=1}^{\Omega} \psi_{n, k}(\omega)
\end{aligned}
$$

where $\xi_{k}$ is obtained from (24). Equation (24) integrates $\sum_{m} \phi_{n \rightarrow m, k}$ (which is related to the clustering of array network) and $\sum_{\omega=1}^{\Omega} \psi_{n, k}(\omega)$ (which is related to the clustering of observations). Besides, according to the property of the Dirichlet distribution, we have

$$
\mathbb{E}_{q}\left[\log \left(\pi_{n, k}\right)\right]=\Psi\left(\gamma_{n, k}\right)-\Psi\left(\sum_{k=1}^{K} \gamma_{n, k}\right)
$$

## E. Position of sources

We use Laplace approximation method proposed in [53] to find a Gaussian approximation of the variational distribution $q\left(\mathbf{l}_{k}\right)$, given as

$$
q\left(\mathbf{l}_{k}\right) \approx \mathcal{N}\left(\boldsymbol{\mu}_{k},-\frac{1}{\nabla^{2} \log \left(q\left(\boldsymbol{\mu}_{k}\right)\right)}\right)
$$

Laplace approximations adopts a Taylor approximation around the maximum a posterior (MAP) point of the target distribution. Thus $\boldsymbol{\mu}_{k}$ is given by

$$
\boldsymbol{\mu}_{k}=\underset{\mathbf{l}_{k}}{\arg \max } \log q\left(\mathbf{l}_{k}\right)
$$

which can be solved using the gradient descent algorithm.

## F. Prior distribution parameter $\widetilde{\boldsymbol{\pi}}$

We approximate $q(\widetilde{\boldsymbol{\pi}})$ using a normal distribution and obtain

$$
q(\widetilde{\boldsymbol{\pi}}) \approx \mathcal{N}\left(\boldsymbol{\xi},-\frac{1}{\nabla^{2} \log (q(\boldsymbol{\xi}))}\right)
$$

where $\boldsymbol{\xi}$ is given by

$$
\boldsymbol{\xi}=\underset{\widetilde{\boldsymbol{\pi}}}{\arg \max } \log q(\widetilde{\boldsymbol{\pi}})
$$

which can also be solved using the gradient descent algorithm.

## IV. Simulation and EXPERIMENT ReSults

In this section, we evaluate our method on both simulated datasets and real recordings, and compare it with the state-ofart method proposed in [42].

## A. 2D Localization in anechoic environments

In this simulation, 2D localization and anechoic environment are considered. Our objective is to evaluate the data association accuracy and the localization accuracy of our method against the baseline method proposed in [42] in ideal conditions.

1) Simulation settings: To generate the dataset, we consider a 2 D space with length and width both 20 decimeters. 40 microphone arrays are randomly deployed in the space and each array is composed of two microphones. The distance between two microphones in an array is 2 decimeters. The position of each array is fixed at the central position of the corresponding microphone pair. We consider two or three sound source scenarios and the positions of the sound sources are also randomly generated. The observation of each array is divided into 40 TF bins and each TF bin belongs to an acoustic source. In this subsection, the total number of TF bins is 40 and in the simulation of our method and the baseline method, we use all the TF bins. Here we let the total number of TF bins be 40 to show the effectiveness of our method when limited number of observations are available. In Section IV-B, we will show our method performs better than the baseline method when the number of TF bins is much larger. The number and the positions of arrays are assumed to be known and the number of acoustic sources is also known.

TABLE II: Simulation setup and parameter initialization of Algorithm 1.


When performing simulations, The estimated locations of acoustic sources are randomly initialized in the space in our simulation. The values of the hyperparameters and parameter initialization in our model are shown in Table II. The localization performance is evaluated using the Mean Localization Error (MLoE), which is defined as follows:

$$
M L o E=\frac{1}{K} \sum_{k=1}^{K} \min _{j \in\{1, \ldots, K\}}\left\|\hat{\mathbf{l}}_{j}-\mathbf{l}_{k}\right\}
$$

where $\left\{\hat{\mathbf{l}}_{j}\right\}_{j=1}^{K}$ and $\left\{\mathbf{l}_{k}\right\}_{k=1}^{K}$ are the estimations and the ground truths of the source locations. For an element $\mathbf{l}_{k}$ in $\left\{\mathbf{l}_{k}\right\}_{k=1}^{K}$, we choose the closest element to $\mathbf{l}_{k}$ in $\left\{\hat{\mathbf{l}}_{j}\right\}_{j=1}^{K}$ as its estimation and calculate the mean square error over $K$ sources.

Following [42], the mean association error (MAsE) is employed to evaluate the performance of the data association. MAsE counts the percentage of wrong pairwise associations between all pairs of arrays. In essence, the lower the MAsE is, the less impact an erroneous pair will have on the dataassociation and thus to the localization error.
2) Single Experiment Result: In this experiment, we demonstrate how the estimates approach the ground truth in a single implementation. Fig. 3 shows the experiment setup and the result. We use '*', ' $\operatorname{Tr}_{k}$ ' and ' $\mathrm{Es}_{k}$ ' to denote the sensors, the true location of the $k$-th source and the estimated location of the $k$-th source in our algorithm. The three arrows show the trajectories of our estimation results in different iterations. It can be observed that even the sources are randomly initialized to the same position, the algorithm can still converge to the ground truth quickly.
3) Mean Localization Error: We conduct 50 Monte Carlo experiments for both two and three source scenarios and show the localization performances of our method and the baseline method in Fig. 4. The performances are evaluated using Eq. (25). The boxes in the figure show the MLoE distributions of our method and the baseline method. It can be observed that our proposed method achieves lower MLoE median and lower MLoE variance in both two and three source scenarios. In our method, the MLoE medians are 0.07 decimeter and 0.14 decimeter for two sources and three sources separately. In the baseline method, however, the medians are 2.75 decimeter and 3.57 decimeter for corresponding cases. The performance of our method is better than that of the baseline method due to two reasons. First, the distance information between arrays are employed and close arrays have high probability of observing the same sound sources in our model. The other reason is that
![img-2.jpeg](img-2.jpeg)

Fig. 3: Demonstration of the estimates approaching the ground truth in a single implementation. The symbols '*', ' $\operatorname{Tr}_{k}$ ' and ' $\mathrm{Es}_{k}$ ' denote the sensors, the ground truth location of the $k$ th source and the estimated location of the $k$-th source in our algorithm. The three arrows show the trajectories of our estimation results in different iterations.
we only use 40 TF bins and the baseline method cannot obtain accurate histogram based features using such a small number of observations. The result also shows the robustness of our method when the number of TF bins is small.
4) Mean Association Error: The performance of data association is shown in Fig. 5. The mean association error (MAsE) is computed across different arrays. It can be observed that the MAsE medians of our method are $2 \%$ and $6 \%$ for two sources and three sources separately. In comparison, the MAsE medians of the baseline method are $63 \%$ and $55 \%$ correspondingly. The MAsE variances of our method are also significantly lower than those of the baseline method.

## B. 3D localization with Reverberation and Noise

In this dataset, we consider localization of the sources in 3D space with consideration of room reverberation. By considering various reverberation time and signal-to-noise ratio, the robustness of our method against model mismatch can be studied. We do not evaluate the data association performance of our method and the baseline method on this simulation as

![img-3.jpeg](img-3.jpeg)

Fig. 4: Mean localization error comparison between our method and the baseline method under two sources and three sources scenarios. On each box, the central mark indicates the median, and the bottom and top edges of the box indicate the 25th and 75th percentiles separately. The outliers are indicated by '+'.

![img-4.jpeg](img-4.jpeg)

Fig. 5: Mean measurement to source association error comparison between our method and the baseline method under two sources and three sources scenarios. On each box, the central mark indicates the median, and the bottom and top edges of the box indicate the 25th and 75th percentiles separately. The outliers are indicated by '+'.

the ground truth of the data associations is not available due to reverberation and noise.

*1) Data generation process:* We use open source software Pyroomacoustics to generate this simulation dataset. This software provides room impulse response (RIR) simulations via the imaging method. The length, width, and height of the room is set to be [15, 10, 3]m. 20 arrays are randomly deployed in the room with height fixed to 1.5m. The source positions are randomly generated in the localization scene; the distance between the wall and the sources are assumed to be larger than 1m. We perform simulations for both two and three source scenarios. Various reverberation time (RT60) (i.e., 250ms, 400ms, 600ms) and signal to noise ratio (SNR) (i.e., 0dB, 10dB, 20dB) are considered in our experiments.

Pyroomacoustics simulates the sound propagation in the room using our above settings. We obtain the audio signal received by each microphone, which is a mixture of multiple speech signals due to different sources. The audio signals are sampled at 16kHz. We compute short time Fourier transform (STFT) of the received signal of each microphone and obtained the phase of each time frequency bin. For each TF bin, we extract the TDOA and then convert it to the distance difference. The number of time frames is 108 with 50% overlap between adjacent frames. At each array, 108×512 TF bins are available to obtain the observations in our model. We select the TF bins with amplitude higher than a predefined threshold so that non-informative bins due to noise and reverberation can be removed. The localization scenes are illustrated in Fig. 6.

2) *Mean Localization Error Under Different Reverberation Time (RT60):* The estimated locations of acoustic sources are randomly initialized in the space in our experiment. The values of the hyperparameters and initial values of some variables are the same as those shown in Table II except that the number of iterations is set to 100. The observation association becomes more difficult when the reverberation is considered. We set the SNR in our simulation to be 20dB and conduct 20 MC experiments for different RT60 values, namely {250, 400, 600}ms. The results are shown in Fig. 7. It can be observed that the proposed method has lower MLoE median, and is more robust to the reverberation compared with the baseline method. It is worth mentioning that both the baseline method [42] and our proposed method are two stage methods, i.e., extracting the measurements first and then performing the association. Hence, the association algorithms in our method and in the baseline method can directly deal with both DOAs and TDOAs. Besides, when implementing the baseline method, we use the same observation association and localization methods as those in [42].

3) *Mean Localization Error Under Different SNRs:* We use the same settings as in Section IV-B2. In this subsection, we consider the influence of different SNR values on the performance of our method and the baseline method. We set the RT60 in our simulations to be 250ms and conducted 20 MC experiments for different SNRs in {0, 10, 20}dB. The results are shown in Fig. 8. It shows that our method has better performance than the baseline method when SNR are 10dB and 20dB. The performance of our method is worse than the baseline method when SNR is 0dB which is an

<sup>1</sup>https://pypi.org/project/pyroomacoustics/0.4.1/

![img-5.jpeg](img-5.jpeg)

Fig. 6: Rooms with two (left) and three (right) sources. The boxes represent the boundary of the room. The markers represent either a real sound source or a virtual source generated by using the imaging method.
![img-6.jpeg](img-6.jpeg)

Fig. 7: Mean Localization Error (MLoE) under different reverberation time values. On each box, the central mark indicates the median, and the bottom and top edges of the box indicate the 25 th and 75 th percentiles separately. The outliers are indicated by ' + '.
extreme challenge environment that both methods present high localization error.

## C. Real data experiment

To further demonstrate the performance of our method in practice, an experiment with real recordings in a lecture room is conducted.

![img-7.jpeg](img-7.jpeg)

Fig. 8: Mean Localization Error (MLoE) under different SNR values. On each box, the central mark indicates the median, and the bottom and top edges of the box indicate the 25th and 75th percentiles separately. The outliers are indicated by ' + '.

1) Recording Environment: The experiment settings are illustrated in Fig. 9. The data set was recorded in a lecture room of which the size is $[10.5,8.9,3.9] \mathrm{m}$. The room has two wooden doors and tiled floor. Three walls are concrete blocks and the other one is mainly glass windows. There are desks and seats in the room. The measured reverberation time of the room is about 880 ms . Six omni-directional microphone arrays are placed on the table with a height of 0.79 m . Two different types of microphone arrays are employed for recording: three uniform linear arrays with 4 cm spacing and 4 microphones, and three uniform circular arrays with 4.67 cm radius and also 4 microphones. The signals received by the diagonal microphones in the circular array and the signals from the microphones at two ends of the linear array are employed for experiments. Three different talkers ( 1 male and 2 female) are sitting at the given position with height of $[1.50,1.39,1.39] \mathrm{m}$ to speak as acoustic sources. Five different recordings for both two speaker and three speaker simultaneously talking scenarios are considered.
2) Mean Localization Error: The values of the hyperparameters and initial values of variables are the same as those in Section IV-B2. The experiment results are shown in Table III. It can be observed that our method has better performance than the baseline method on all real recordings.

## V. CONCLUSION

In this paper, we propose a Bayesian network model to jointly infer the measurement-source association and locations of multiple speaker sources. The proposed approach is able to incorporate the information of distances between microphone arrays to reduce the performance degradation due to reverberation and noise. Experiments on both simulated environments and real recordings are performed. The mean association error and the mean location error are employed to evaluate the performance of the proposed method. The results show the advantage of our method in assigning TDOAs and localizing sound sources under different environments. However, the number of sources are assumed to be known and fixed in this paper. In our future work, dynamic source and joint detection and localization problem will be considered and Bayesian network based tracking algorithm will be studied.

## ACKNOWLEDGMENT

Thanks Dr. Hongbin Wang and Dr. Fengming Cao for providing useful advice.

## APPENDIX

In the appendix, we show the derivation details of the variational parameter updating equations.

TABLE III: MLoE for the baseline and proposed method in real data experiment.


![img-8.jpeg](img-8.jpeg)

Fig. 9: Real data experiment setting. Top: a schematic of the recording setup; M1, M3 and M6 are three circular microphone arrays. M2, M4 and M5 are three linear microphone arrays. The position of a microphone (marked by a dark dot) in the array is given next to it; L1, L2 and L3 are the positions of three speakers; the coordinate are shown in meter. Bottom: Real lecture room environment.

### A. Hyper parameters β

We use $I(\cdot)$ and $I(\cdot, \cdot)$ to denote the indicator functions and they are defined at the end of Section I. The posterior distribution of $\beta_{k}$ is

$$
\begin{aligned}
& p\left(\beta_{k} \mid \mathbf{D}, \mathbf{z}\right) \\
& \propto \prod_{(n, m)} p(\mathbf{D}(n, m) \mid \beta_{k}, z_{n \rightarrow m}=k, z_{n \leftarrow m}=k) p\left(\beta_{k}\right) \\
& \propto \prod_{(n, m)} \beta_{k}^{I(\mathbf{D}(n, m)<d) I\left(z_{n \rightarrow m}, k\right) I\left(z_{m \rightarrow n}, k\right)} \\
& \quad\left(1-\beta_{k}\right)^{I(\mathbf{D}(n, m) \geq d) I\left(z_{n \rightarrow m}, k\right) I\left(z_{m \rightarrow n}, k\right)} \mathcal{B} e\left(g_{0}, h_{0}\right) \\
& =\beta_{k}^{\sum_{(n, m)} I(\mathbf{D}(n, m)<d) I\left(z_{n \rightarrow m}, k\right) I\left(z_{m \rightarrow n}, k\right)+g_{0}-1} \\
& \quad\left(1-\beta_{k}\right)^{\sum_{(n, m)} I(\mathbf{D}(n, m) \geq d) I\left(z_{n \rightarrow m}, k\right) I\left(z_{m \rightarrow n}, k\right)+h_{0}-1}
\end{aligned}
$$

$$
\begin{aligned}
= & \mathcal{B} e\left(\sum_{(n, m)} I(\mathbf{D}(n, m)<d) I\left(z_{n \rightarrow m}, k\right) I\left(z_{m \rightarrow n}, k\right)+g_{0}\right. \\
& \left.\sum_{(n, m)} I(\mathbf{D}(n, m) \geq d) I\left(z_{n \rightarrow m}, k\right) I\left(z_{m \rightarrow n}, k\right)+h_{0}\right)
\end{aligned}
$$

This posterior distribution is also a beta distribution. The beta distribution is an exponential family distribution and its natural parameter is given by

$$
\begin{aligned}
& \left(\sum_{(n, m)} I(\mathbf{D}(n, m)<d) I\left(z_{n \rightarrow m}, k\right) I\left(z_{m \rightarrow n}, k\right)+g_{0}\right. \\
& \sum_{(n, m)} I(\mathbf{D}(n, m) \geq d) I\left(z_{n \rightarrow m}, k\right) I\left(z_{m \rightarrow n}, k\right)+h_{0})
\end{aligned}
$$

We further denote $\boldsymbol{\lambda}_{k}$ as $\left(G_{k}, H_{k}\right)$ and let the variational distribution of $\beta_{k}$ be $q\left(\beta_{k}\right) \triangleq \mathcal{B} e\left(G_{k}, H_{k}\right)$. From [52], we obtain (13) and (14).

## B. Group membership indicators z

The posterior distribution of $z_{n \rightarrow m}$ is

$$
\begin{aligned}
p\left(z_{n \rightarrow m}=k \mid \pi_{n}, z_{m \rightarrow n}, \mathbf{D}(n, m)<d, \beta_{k}\right) & \\
& \propto p(\mathbf{D}(n, m)<d \mid z_{n \rightarrow m}=k, \pi_{n}, z_{m \rightarrow n}, \beta_{k}) \\
& p\left(z_{n \rightarrow m}=k \mid \pi_{n}\right) \\
& =\beta_{k}^{I\left(z_{m \rightarrow n}, k\right)} \epsilon^{\left(1-I\left(z_{m \rightarrow n}, k\right)\right)} \pi_{n, k}
\end{aligned}
$$

Similarly, we can also derive

$$
\begin{aligned}
& p\left(z_{n \rightarrow m}=k \mid \pi_{n}, z_{m \rightarrow n}, \mathbf{D}(n, m) \geq d, \beta_{k}\right) \\
& \quad \propto\left(1-\beta_{k}\right)^{I\left(z_{m \rightarrow n}, k\right)}(1-\epsilon)^{\left(1-I\left(z_{m \rightarrow n}, k\right)\right)} \pi_{n, k}
\end{aligned}
$$

We let the variational distribution of the group membership index $z$ be

$$
q\left(z_{n \rightarrow m}=k\right) \triangleq \phi_{n \rightarrow m, k}
$$

From [52], we have

$$
\begin{aligned}
& \phi_{n \rightarrow m, k} \mid \mathbf{D}(n, m)<d \\
& \quad \propto \exp \left\{\mathbb{E}_{q\left(\beta_{k}, z_{m \rightarrow n}, \pi_{n, k}\right)}\left[\log \left(\beta_{k}^{I\left(z_{m \rightarrow n}, k\right)} \epsilon^{\left(1-I\left(z_{m \rightarrow n}, k\right)\right)} \pi_{n, k}\right)\right]\right\} \\
& \quad=\exp \left\{\phi_{m \rightarrow n, k} \mathbb{E}_{q\left(\beta_{k}\right)}\left[\log \left(\beta_{k}\right)\right]+\left(1-\phi_{m \rightarrow n, k}\right) \log \epsilon\right. \\
& \left.\quad \quad+\mathbb{E}_{q\left(\pi_{n, k}\right)}\left[\log \left(\pi_{n, k}\right)\right]\right\} .
\end{aligned}
$$

Equation (27) holds because of the mean field assumption and $\mathbb{E}\left[I\left(z_{m \rightarrow n}, k\right)\right]=\phi_{m \rightarrow n, k}$. Similarly, we have

$$
\begin{aligned}
& \phi_{n \rightarrow m, k} \mid \mathbf{D}(n, m) \geq d \\
& \quad \propto \exp \left\{\mathbb{E}_{q\left(\beta_{k}, z_{m \rightarrow n}, \pi_{n, k}\right)}\left[\log \left(\left(1-\beta_{k}\right)^{I\left(z_{m \rightarrow n}, k\right)}\right.\right.\right. \\
& \left.\left.\quad \quad(1-\epsilon)^{\left(1-I\left(z_{m \rightarrow n}, k\right)\right)} \pi_{n, k}\right)\right]\right\} \\
& \quad=\exp \left\{\phi_{m \rightarrow n, k} \mathbb{E}_{q\left(\beta_{k}\right)}\left[\log \left(1-\beta_{k}\right)\right]\right. \\
& \quad+1-\phi_{m \rightarrow n, k}\left\lvert\, \log (1-\epsilon)\right. \\
& \left.\left.\quad \quad+\mathbb{E}_{q\left(\pi_{n, k}\right)}\left[\log \left(\pi_{n, k}\right)\right]\right\}\right.
\end{aligned}
$$

## C. Source indices $\mathbf{s}$

The posterior distribution of $s_{n}(\omega)$ is

$$
\begin{aligned}
& p\left(s_{n}(\omega)=k \mid \pi_{n}, y_{n}(\omega), \mathbf{l}_{k}\right) \\
& \quad \propto p\left(y_{n}(\omega) \mid s_{n}(\omega)=k, \mathbf{l}_{k}\right) p\left(s_{n}(\omega)=k \mid \pi_{n}\right) \\
& \quad=\mathcal{N}\left(f\left(\mathbf{l}_{k}, \mathbf{l}_{n}^{\prime}\right), \sigma^{2}\right) \pi_{n, k}
\end{aligned}
$$

Here $y_{n}(\omega)=$ nan if array $n$ does not observe frequency $\omega . s_{n}(\omega)$ is a discrete variable and follows a categorical distribution and thus we obtain

$$
\begin{aligned}
& p\left(s_{n}(\omega) \mid \pi_{n}, y_{n}(\omega), \mathbf{l}_{k}\right) \\
& \quad=\operatorname{Cat}\left(\left(\frac{\mathcal{N}\left(f\left(\mathbf{l}_{k}, \mathbf{l}_{n}^{\prime}\right), \sigma^{2}\right) \pi_{n, k}}{\sum_{k=1}^{K} \mathcal{N}\left(f\left(\mathbf{l}_{k}, \mathbf{l}_{n}^{\prime}\right), \sigma^{2}\right) \pi_{n, k}}\right)_{k=1}^{K}\right)
\end{aligned}
$$

We let the variational distribution of community index $s$ be $q\left(s_{n}(\omega)=k\right)=\psi_{n, k}(\omega)$. Then, we have

$$
\begin{aligned}
& \psi_{n, k}(\omega) \\
& \propto \exp \left\{\mathbb{E}_{q\left(\mathbf{l}_{k}, \boldsymbol{\pi}_{n}\right)}\left[\log \left(\mathcal{N}\left(f\left(\mathbf{l}_{k}, \mathbf{l}_{n}^{\prime}\right), \sigma^{2}\right) \pi_{n, k}\right)\right]\right\} \\
& =\exp \left(\mathbb{E}_{q\left(\mathbf{l}_{k}\right)}\left[\log \left(\mathcal{N}\left(f\left(\mathbf{l}_{k}, \mathbf{l}_{n}^{\prime}\right), \sigma^{2}\right)\right)\right]+\mathbb{E}_{q\left(\boldsymbol{\pi}_{n}\right)}\left[\log \left(\pi_{n, k}\right)\right]\right) \\
& =\exp \left(\mathbb{E}_{q\left(\mathbf{l}_{k}\right)}\left[\log \left(\frac{1}{\sqrt{2 \pi \sigma^{2}}} \exp \left(-\frac{\left(y_{n}(\omega)-f\left(\mathbf{l}_{k}, \mathbf{l}_{n}^{\prime}\right)\right)^{2}}{2 \sigma^{2}}\right)\right)\right]\right. \\
& +\mathbb{E}_{q\left(\boldsymbol{\pi}_{n}\right)}\left[\log \left(\pi_{n, k}\right)\right]\right) \\
& \propto \exp \left(\mathbb{E}_{q\left(\mathbf{l}_{k}\right)}\left[-\frac{\left(y_{n}(\omega)-f\left(\mathbf{l}_{k}, \mathbf{l}_{n}^{\prime}\right)\right)^{2}}{2 \sigma^{2}}\right]+\mathbb{E}_{q\left(\boldsymbol{\pi}_{n}\right)}\left[\log \left(\pi_{n, k}\right)\right]\right) \\
& \propto \exp \left(\mathbb{E}_{q\left(\mathbf{l}_{k}\right)}\left[-\frac{\left(f\left(\mathbf{l}_{k}, \mathbf{l}_{n}^{\prime}\right)-M_{n, k}^{\prime}+M_{n, k}^{\prime}-y_{n}(\omega)\right)^{2}}{2 \sigma^{2}}\right]\right. \\
& +\mathbb{E}_{q\left(\boldsymbol{\pi}_{n}\right)}\left[\log \left(\pi_{n, k}\right)\right]\right) \\
& =\exp \left(-\frac{1}{2 \sigma^{2}}\left[V_{n, k}^{\prime}+\left(M_{n, k}^{\prime}-y_{n}(\omega)\right)^{2}\right]+\mathbb{E}_{q\left(\boldsymbol{\pi}_{n}\right)}\left[\log \left(\pi_{n, k}\right)\right]\right)
\end{aligned}
$$

where $\mathbb{E}_{q\left(\boldsymbol{\pi}_{n}\right)}\left[\log \left(\pi_{n, k}\right)\right]$ is computed using (20), $M_{n, k}^{\prime} \triangleq$ $\mathbb{E}_{q\left(\mathbf{l}_{k}\right)}\left[f\left(\mathbf{l}_{k}, \mathbf{l}_{n}^{\prime}\right)\right]$, and $V_{n, k}^{\prime} \triangleq \mathbb{E}_{q\left(\mathbf{l}_{k}\right)}\left[\left(f\left(\mathbf{l}_{k}, \mathbf{l}_{n}^{\prime}\right)-M_{n, k}^{\prime}\right)^{2}\right]$. Both $M_{n, k}^{\prime}$ and $V_{n, k}^{\prime}$ are computed with the Monte Carlo method and the samples of $\mathbf{l}_{k}$ are drawn from (21).

## D. Source weights $\pi$

The posterior distribution of $\pi_{n}$ is

$$
\begin{aligned}
& p\left(\pi_{n} \mid\left\{s_{n}(\omega)\right\}_{\omega=1}^{\Omega}, \mathbf{z}, \widetilde{\pi}\right) \\
= & \prod_{\omega=1}^{\Omega} p\left(s_{n}(\omega) \mid \pi_{n}\right) \prod_{m} p\left(z_{n \rightarrow m} \mid \pi_{n}\right) p\left(\pi_{n} \mid \widetilde{\pi}\right) \\
= & \operatorname{Dir}\left(\left\{\widetilde{\pi}_{k}+\sum_{m=1, m \neq n}^{N} I\left(z_{n \rightarrow m}, k\right)+\sum_{\omega=1}^{\Omega} I\left(s_{n}(\omega), k\right)\right\}_{k=1}^{K}\right)
\end{aligned}
$$

where $\sum_{m=1, m \neq n}^{N} I\left(z_{n \rightarrow m}, k\right)$ is corresponding to the clustering of the distance relation network and $\sum_{\omega=1}^{\Omega} I\left(s_{n}(\omega), k\right)$ is corresponding to the clustering of the observations. We let the variational distribution of the mixture weight $\pi_{n}$ be $q\left(\pi_{n}\right) \triangleq \operatorname{Dir}\left(\gamma_{n}\right)$, where $\gamma_{n}$ is a $K$ dimensional vector, $K$ is the maximum number of communities, then we obtain (19).

## E. Position of sources

Assume the prior distributions of sources' locations are uniform distributions. The posterior distribution of $\mathbf{l}_{k}$ is then proportional to its corresponding likelihood. We obtain the posterior distribution of $\mathbf{l}_{k}$ :

$$
\begin{aligned}
& p\left(\mathbf{l}_{k} \mid\left\{y_{n, \omega}\right\}_{n, \omega},\left\{s_{n}(\omega)\right\}_{n, \omega}\right) \\
& \propto \prod_{n=1}^{N} \prod_{\omega=1}^{\Omega} p\left(y_{n}(\omega) \mid s_{n}(\omega), \mathbf{l}_{k}\right)^{I\left(s_{n}(\omega), k\right)} \\
& =\prod_{n=1}^{N} \prod_{\omega=1}^{\Omega} \mathcal{N}\left(y_{n}(\omega) ; f\left(\mathbf{l}_{k}, \mathbf{l}_{n}^{\prime}\right), \sigma^{2}\right)^{I\left(s_{n}(\omega), k\right)}
\end{aligned}
$$

We can see that $p\left(\mathbf{l}_{k} \mid\left\{y_{n, \omega}\right\}_{n, \omega},\left\{s_{n}(\omega)\right\}_{n, \omega}\right)$ is not an exponential family distribution. To find $q\left(\mathbf{l}_{k}\right)$ to minimize (12), we take the functional derivative of the objective function (12) with respect to $q\left(\mathbf{l}_{k}\right)$ and set it to zero, namely $\frac{\partial \mathcal{L}(q)}{\partial q\left(\mathbf{l}_{k}\right)}=0$, we obtain the maximizer as

$$
\begin{aligned}
q\left(\mathbf{l}_{k}\right) & \propto \exp \left(\mathbb{E}_{q(\mathbf{s})}\left[\log p\left(\mathbf{l}_{k} \mid\left\{y_{n, \omega}\right\}_{n, \omega},\left\{s_{n}(\omega)\right\}_{n, \omega}\right)\right]\right) \\
& \propto \exp \left(\mathbb{E}_{q(\mathbf{s})}\left[\sum_{n=1}^{N} \sum_{\omega=1}^{\Omega} \log \left[\mathcal{N}\left(y_{n}(\omega) ; f\left(\mathbf{l}_{k}, \mathbf{l}_{n}^{\prime}\right), \sigma^{2}\right)\right]\right.\right. \\
& \left.\left.I\left(s_{n}(\omega), k\right)\right]\right) \\
& =\prod_{n=1}^{N} \prod_{\omega=1}^{\Omega} \mathcal{N}\left(y_{n}(\omega) ; f\left(\mathbf{l}_{k}, \mathbf{l}_{n}^{\prime}\right), \sigma^{2}\right)^{\psi_{n, k}(\omega)}
\end{aligned}
$$

Equation (30) is difficult to analyze and thus we use Laplace approximation method proposed in [53] to find a Gaussian approximation, given as (21) and (22).

## F. Prior distribution parameter $\widetilde{\pi}$

The posterior distribution of $\widetilde{\pi}=\left\{\pi_{k}\right\}_{k}$ is

$$
\begin{aligned}
p(\widetilde{\pi} \mid \pi) & \propto \prod_{n=1}^{N} p\left(\pi_{n} \mid \widetilde{\pi}\right) p(\widetilde{\pi}) \\
& =\prod_{n=1}^{N} \operatorname{Dir}\left(\pi_{n} ; \widetilde{\pi}\right) \log \operatorname{Normal}(\mathbf{M}, \mathbf{V})
\end{aligned}
$$

Similar to Section III-E, we take the functional derivative of the objective function (12) with respect to $q(\widetilde{\pi})$ and set it to zero, namely $\frac{\partial \mathcal{L}(q)}{\partial q(\widetilde{\pi})}=0$ and obtain

$$
\begin{aligned}
& q(\tilde{\boldsymbol{\pi}}) \propto \exp \left(\sum_{n=1}^{N} \mathbb{E}_{q\left(\boldsymbol{\pi}_{n}\right)}\left[\log p\left(\boldsymbol{\pi}_{n} \mid \tilde{\boldsymbol{\pi}}\right)\right]+\log p(\tilde{\boldsymbol{\pi}})\right) \\
& \propto \exp \left(\sum_{n=1}^{N} \mathbb{E}_{q\left(\boldsymbol{\pi}_{n}\right)}\left[\log \Gamma\left(\sum_{k=1}^{K} \tilde{\pi}_{k}\right)-\sum_{k=1}^{K} \log \Gamma\left(\tilde{\pi}_{k}\right)\right.\right. \\
& \left.\left.+\sum_{k=1}^{K}\left(\tilde{\pi}_{k}-1\right) \mathbb{E}_{q}\left[\log \left(\pi_{n, k}\right)\right]\right] \\
& -\frac{K}{2} \log (2 \pi)-\frac{1}{2} \log (\operatorname{det}(\mathbf{V}))-\sum_{k=1}^{K} \log \left(\tilde{\pi}_{k}\right) \\
& \left.-\frac{1}{2}(\log (\tilde{\boldsymbol{\pi}})-\mathbf{M})^{T} \mathbf{V}^{-1}(\log (\tilde{\boldsymbol{\pi}})-\mathbf{M})\right)
\end{aligned}
$$

The last formula holds due to (7) and (8). We approximate $q(\tilde{\boldsymbol{\pi}})$ using a normal distribution, given as (23) and (24).
