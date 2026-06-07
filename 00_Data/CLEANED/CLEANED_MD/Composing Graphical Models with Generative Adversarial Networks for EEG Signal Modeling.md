# UC Irvine 

## UC Irvine Previously Published Works

## Title

Composing Graphical Models with Generative Adversarial Networks for EEG Signal Modeling

## Permalink

https://escholarship.org/uc/item/5dk540r4

## ISBN

9781665405409

## Authors

Vo, Khuong
Vishwanath, Manoj
Srinivasan, Ramesh
et al.

## Publication Date

2022-05-27

## DOI

10.1109/icassp43922.2022.9747783

## Copyright Information

This work is made available under the terms of a Creative Commons Attribution License, available at https://creativecommons.org/licenses/by/4.0/

Peer reviewed

# COMPOSING GRAPHICAL MODELS WITH GENERATIVE ADVERSARIAL NETWORKS FOR EEG SIGNAL MODELING 

Khuong Vo ${ }^{\S}$, Manoj Vishwanath ${ }^{\S}$, Ramesh Srinivasan ${ }^{\dagger \ddagger}$, Nikil Dutt ${ }^{\S \star \dagger}$, and Hung Cao ${ }^{\star \ddagger}$<br>${ }^{\S}$ Department of Computer Science, ${ }^{\star}$ Department of Electrical Engineering and Computer Science, ${ }^{\dagger}$ Department of Cognitive Sciences, ${ }^{\ddagger}$ Department of Biomedical Engineering, University of California, Irvine, USA<br>\{khuongav, manojv, srinivar, dutt, hungcao\}@uci.edu


#### Abstract

Neural oscillations in the form of electroencephalogram (EEG) can reveal underlying brain functions, such as cognition, memory, perception, and consciousness. A comprehensive EEG computational model provides not only a stochastic procedure that directly generates data but also insights to further understand the neurological mechanisms. Here, we propose a generative and inference approach that combines the complementary benefits of probabilistic graphical models and generative adversarial networks (GANs) for EEG signal modeling. We investigate the method's ability to jointly learn coherent generation and inverse inference models on the CHIMIT epilepsy multi-channel EEG dataset. We further study the efficacy of the learned representations in epilepsy seizure detection formulated as an unsupervised learning problem. Quantitative and qualitative experimental results demonstrate the effectiveness and efficiency of our approach.


Index Terms- EEG, GAN, Bayesian networks

## 1. INTRODUCTION

Electroencephalogram (EEG) is a non-invasive technique that measures the spontaneous electrical activity of the brain. EEG has been a driver of studies from basic neurological research to clinical applications. EEG modeling is essential to understanding the underlying mechanisms that generate brain signals and serve to design experiments and test hypotheses in silico. There exist extensive prior works on EEG computational models [1] that derived principled neuroscience laws, empirically validated rules, or other domain expertise. Those are often in the form of general time-dependent and nonlinear partial differential equations. Nevertheless, they rely on strong assumptions which are not always generalizable. Further, those are slow to simulate and often suffer from model misspecifications.

Generative Adversarial Networks (GANs) [2] provide a powerful framework and tools for machine learning, especially for deep representation learning and generative models. Over the past few years, GANs have witnessed tremendous advancements and achieved state-of-the-art performance in a variety of prominent tasks, including photo editing, video prediction, text generation, and signal synthesis [3, 4]. As a data-driven method, GANs are flexible and do not depend on rigid assumptions. Therefore, GANs hold great potential in modeling the inherent stochasticity and extrinsic uncertainty of EEG signals.

Recent work [5, 6, 7] applying GANs in EEG synthesis tend to simply characterize the spatio-temporal characteristics of EEG data
subject to latent spaces of basic distributions, e.g., Gaussian or uniform distributions. Such assumptions impose limitations in capturing the intrinsic dependence among latent variables. Also, the GANs require deeper networks to synthesize longer sequences, which are computationally expensive and challenging to train, e.g., vanishing or exploding gradient problems. Moreover, the lack of inference capability in vanilla GANs hinder insight into structural information of EEG signals. On the other hand, probabilistic graphical models [8] enable inference through structured representations but often lack the capability to model arbitrarily complex distributions.

To address these challenges, we propose a novel GAN-based approach for EEG signal modeling that couples deep implicit likelihoods [9] with structured latent variable representations to combine their complementary strengths. Our method uses graphical models for representing underlying structures of the signals, and applies ideas from the Graphical-GAN [10] for effectively learning not only a generative model mapping from latent distributions to complex high-dimensional EEG data space but also an inverse inference model mapping from the data space to the latent space. Our study paves the way for leveraging implicit probabilistic models to comprehensively investigate the mechanisms that generate brain waves.

## 2. METHODOLOGY

### 2.1. EEG Signal Synthesis with GANs

A GAN is a generative model trained by a pair of neural networks in a game-theoretic approach [2]. In GANs, a discriminator neural network $D$ is trained to distinguish real from synthetic EEG signals, while a neural generator network $G$ is trained to generate EEG signals from a latent space to make them indistinguishable by the discriminator. With EEG signal $x$ drawn from data generating distribution $q(x), z$ drawn from noise prior $p_{z}$, and $p(x)$ is the generator's distribution over synthetic data, $G$ and $D$ jointly optimize the following objective:

$$
\begin{aligned}
\mathcal{L}_{G A N}(G, D) & =\mathbb{E}_{x \sim q(x)}[\log D(x)]+\mathbb{E}_{z \sim p_{z}(z)}[\log (1-D(G(z))] \\
& =\mathbb{E}_{x \sim q(x)}[\log D(x)]+\mathbb{E}_{x \sim p(x)}[\log (1-D(x))]
\end{aligned}
$$

The discriminator is expected to output a high probability for a valid EEG signal and a low probability for a synthesized one, corresponding to the values of $\log D(x)$ and $\log (1-D(G(z))$, respectively. $G$ and $D$ are trained simultaneously until $G$ is able to successfully fool $D$.

Following the proofs in [2], given a fixed generator G, the optimal discriminator is given by $D^{*}(x)=\frac{q(x)}{q(x)+p(x)}$

Under an optimal discriminator $D^{*}$, the generator minimizes the Jensen-Shannon (JS) divergence, which attains its minimum if and only if $p(x)=q(x)$.

### 2.2. Conjoining GANs with Bayesian Networks

2.2.1. Generative and Inverse Inference Process
![img-0.jpeg](img-0.jpeg)
(b) Inverse inference model - $q$

Fig. 1: Directed graphical models for EEG signal modeling. Each time step corresponds to a $\delta$-second multi-channel signal. Shaded nodes represent observed variables. Clear nodes represent latent variables. Directed edges indicate statistical dependencies between variables.

As shown in Figure 1, we model the generative process and the inverse inference process by a generative model and an inverse inference model in the Bayesian network. The framework exploits a Gaussian mixture model (GMM) to characterize the static latent variable structure with its capability to approximate arbitrary distributions, and a Markov model for the dynamic latent characterization. We use the notations $p$ and $q$ to denote the generative and inverse inference models.

The joint distribution of the generative model $p$ is

$$
\begin{aligned}
& p\left(x_{1: T}, v_{1: T}, z, k, c\right) \\
& =p(k) p(z \mid k) p(c) \prod_{t=1}^{T} p\left(v_{t} \mid v_{t-1}\right) p\left(x_{t} \mid z, v_{t}, c\right)
\end{aligned}
$$

where $p(k)$ and $p(c)$ are simple prior distributions for Gaussian mixture indicator $k$ and condition $c$, e.g., a categorical distribution and a uniform distribution, $p(z \mid k)$ models a component selecting procedure for sampling noise $z$ which encodes the temporal-spatial relationships invariant across time, $v_{t}$ 's form a first-order Markov chain, with $p\left(v_{1} \mid v_{0}\right) \sim \mathcal{N}(0, I)$, to encodes the temporal relationships variant across time, $p\left(x_{t} \mid z, v_{t}, c\right)$ specifies the conditional probability of the data at each time step $t$ given noise $z$, state $v_{t}$, and condition $c$, and is of interest for the final generation.

The distribution function $p\left(x_{1: T}, v_{1: T}, z, k, c\right)$ is parametrized as generator neural networks. It consists of three parts: $z^{p}=$ $G_{1}\left(k^{p}\right), v_{t+1}^{p}=G_{2}\left(v_{t}^{p}, \epsilon_{t}\right), \epsilon_{t} \sim \mathcal{N}(0, I)$, and $x_{t}^{p}=G_{3}\left(z, v_{t}^{p}, c\right)$. $G_{1}$ is responsible for a mapping from the input prior to a mixed Gaussian distribution with respect to $k_{p} . G_{2}$ transitions to a new
state $v_{t}^{p}$ given the previous state. $G_{3}$ uses noise $z^{p}$, state $v_{t}^{p}$, and condition $c$ to generate the synthetic $\delta$-second EEG signal $x_{t}^{p}$.

The joint distribution of the inverse inference model $q$ is

$$
\begin{aligned}
& q\left(x_{1: T}, v_{1: T}, z, k, c\right) \\
& =q\left(x_{1: T}\right) q\left(z \mid x_{1: T}, c\right) q(k \mid z) \prod_{t=1}^{T} q\left(v_{t} \mid x_{t}\right)
\end{aligned}
$$

where each latent variable of the Markov structure is assumed to be independent using the mean-field approximation [11]. $q\left(x_{1: T}\right)$ is the empirical data distribution, $q\left(z \mid x_{1: T}, c\right), q\left(v_{t} \mid x_{t}\right)$, and $q(k \mid z)$ are of interest for the inference. Contrary to $p\left(v_{t+1} \mid v_{t}\right), q\left(v_{t} \mid x_{t}\right)$ models a dynamic tracing procedure for reconstructing the hidden features $v_{t}$. In contrast to $p(z \mid k), q(k \mid z)$ models a component tracing procedure for reconstructing the Gaussian mixture indicator $k$.

The distribution function $q\left(x_{1: T}, v_{1: T}, z, k, c\right)$ is parametrized as extractor neural networks. It consists of three parts: $z^{q}=$ $E_{1}\left(x_{1: T}^{q}, c\right), v_{t}^{q}=E_{2}\left(x_{t}^{q}\right)$, and $k^{q}=E_{3}\left(z^{q}\right) . E_{1}$ and $E_{2}$ are responsible for a mapping from original signals to noise $z^{q}$ and state $v_{t}^{q}$, respectively. $E_{3}$ infers within the latent space from $z^{q}$ to $k^{q}$.

### 2.2.2. Learning Process

Our goal is to learn the parameters of the generative model $p$ and the inverse inference model $q$ by jointly minimizing the Jensen-Shannon (JS) divergence

$$
J S\left(q\left(x_{1: T}, v_{1: T}, z, k, c\right) \| p\left(x_{1: T}, v_{1: T}, z, k, c\right)\right)
$$

Expectation Propagation (EP) [12], a deterministic approximation algorithm, is proposed to utilize the locally structured data following [10]. The joint distributions can be factorized in terms of a set of factors $F_{\mathcal{G}}=\left\{( \mathrm{k}, \mathrm{z}),\left(\mathrm{v}_{t}, \mathrm{v}_{t-1}\right),\left(\mathrm{x}_{t}, \mathrm{v}_{t}, \mathrm{z}, c\right)\right\}$. For a factor $a$, the divergence of interest is

$$
J S\left(q(a) \prod_{b \neq a} q(b) \| p(a) \prod_{b \neq a} p(b)\right)
$$

EP iteratively minimize a local divergence in terms of each factor individually with the assumption that $\prod_{b \neq a} q(b) \approx \prod_{b \neq a} p(b)$. The divergence becomes

$$
J S\left(q(a) \prod_{b \neq a} q(b) \| p(a) \prod_{b \neq a} q(b)\right)
$$

Using the same proof sketch as in [10], the divergence for factor $a$ is approximated as

$$
\begin{aligned}
& J S\left(q\left(x_{1: T}, v_{1: T}, z, k, c\right) \| p\left(x_{1: T}, v_{1: T}, z, k, c\right)\right) \\
& \approx \mathbb{E}_{q}\left[\log \frac{2 q(a)}{p(a)+q(a)}\right]+\mathbb{E}_{p}\left[\log \frac{2 p(a)}{p(a)+q(a)}\right]
\end{aligned}
$$

The divergences are further averaged over all local factors as

$$
\frac{1}{\left|F_{\mathcal{G}}\right|}\left[\mathbb{E}_{q}\left[\sum_{a \in F_{\mathcal{G}}} \log \frac{2 q(a)}{p(a)+q(a)}\right]+\mathbb{E}_{p}\left[\sum_{a \in F_{\mathcal{G}}} \log \frac{2 p(a)}{p(a)+q(a)}\right]\right]
$$

Individual parametric discriminators $D_{a}$ can be employed to estimate the local divergences as follows

$\max \frac{1}{\left|F_{\mathcal{G}}\right|} \mathbb{E}_{q}\left[\sum_{a \in F_{\mathcal{G}}} \log \left(D_{a}(a)\right)\right]+\frac{1}{\left|F_{\mathcal{G}}\right|} \mathbb{E}_{p}\left[\sum_{a \in F_{\mathcal{G}}} \log \left(1-D_{a}(a)\right)\right]$
where $\psi$ denotes the parameters in all discriminators. The discriminative models distinguish between the variables from the generative model $p$ and those from the inverse inference model $q$ as synthetic and original, respectively.

### 2.2.3. Optimization Objective

Three discriminators $D_{3}, D_{2}$ and $D_{1}$ receive local variable pairs, i.e., $(k, z),\left(v_{t}, v_{t-1}\right),\left(x_{t}, v_{t}, z, c\right)$, from either the generative model $p$ or the inverse inference model $q$, separately. The adversarial loss is as follows

$$
\begin{aligned}
\mathcal{L}_{G A N} & \left(G_{*}, E_{*}, D_{*}\right) \\
= & \mathbb{E}_{q}\left[\log D_{3}\left(\mathrm{k}^{\mathrm{q}}, \mathrm{z}^{\mathrm{q}}\right)+\log D_{2}\left(\mathrm{v}_{t}^{q}, \mathrm{v}_{t-1}^{q}\right)+\log D_{1}\left(\mathrm{x}_{t}^{q}, \mathrm{v}_{t}^{q}, \mathrm{z}^{q}, c\right)\right] \\
& +\mathbb{E}_{p}\left[\log \left(1-D_{3}\left(\mathrm{k}^{p}, \mathrm{z}^{p}\right)\right)+\log \left(1-D_{2}\left(\mathrm{v}_{t}^{p}, \mathrm{v}_{t-1}^{p}\right)\right)\right. \\
& \left.+\log \left(1-D_{1}\left(\mathrm{x}_{t}^{p}, \mathrm{v}_{t}^{p}, \mathrm{z}^{p}, c\right)\right)\right]
\end{aligned}
$$

All components are trained simultaneously in an adversarial process. Let $\theta$ and $\phi$ denote the parameters of $G_{*}$ and $E_{*}$, respectively. Iteratively, $D_{*}$ learn to maximize Equation 10 by updating $\psi$, while $G_{*}$ and $E_{*}$ learn to minimize Equation 10 by updating corresponding parameters $\theta$ and $\phi$, respectively.

In order to ensure the global consistency of an entire signal across time steps, a frequency domain loss is added as

$$
\mathcal{L}_{f}\left(G_{*}\right)=\left\|\bar{r}\left(x_{i, 1: T}^{q}\right)-\bar{r}\left(x_{i, 1: T}^{p}\right)\right\|_{1}+\left\|\bar{\varphi}\left(x_{i, 1: T}^{q}\right)-\bar{\varphi}\left(x_{i, 1: T}^{p}\right)\right\|_{1}
$$

where $\bar{r}$ and $\bar{\varphi}$ refer to the average magnitude and phase across signals $i$ in a batch, respectively. They are computed by a fast Fourier transform (FFT). Hence, the total objective is

$$
\min _{G_{*}, E_{*}} \max _{D_{*}} \mathcal{L}_{G A N}+\lambda \mathcal{L}_{f}
$$

### 2.3. Network Architectures and Hyperparameters

Table 1 presents the architectures of the deep neural networks. Each time step corresponds to a 1-second EEG signal $(\delta=1)$. All the feature maps have 96 channels. Leaky ReLU activation functions are applied to all layers, with the slope 0.1 to stimulate easier gradient flow. Batch normalizations (BN) [13] are used at each convolutional layer of the generators and extractors. Spectral normalizations (SN) [14] are applied to the discriminators to constrain their Lipschitz constants. $c$ are subject embeddings as one-hot vectors. The sizes of $z, k$, and $v_{t}$ are set at $128,6,32$, and 16 respectively.
$G_{1}$ and $E_{2}$ are single-layer neural networks. We use the reparameterization trick [15] to estimate the gradients with the continuous variable $z$, and the Gumbel-Softmax trick [16] (the temperature of 0.1 ) to estimate the gradients with the discrete variable $k$.
$\lambda$ is set at 0.1 to have the training process driven mainly by the adversarial loss. In order to mitigate the issue of slow learning in regularized discriminators, a higher learning rate is provided to the discriminators than the generators and extractors by the Two Timescale Update Rule (TTUR) [17]. The models are trained with the Adam optimizer with the initial learning rate of 0.0004 for $D_{*}$, the

Table 1: Network architectures. Models having similar architectures are grouped together.


learning rate of 0.0001 for $G_{*}$ and $E_{*}$, and the exponential decay rates $\beta_{1}=0.5$ and $\beta_{2}=0.999$. All weights are initialized using a zero-centered Gaussian distribution with a standard deviation of 0.02 . We make the implementation publicly available ${ }^{1}$.

## 3. EXPERIMENTS

### 3.1. Dataset

The 23-channel interictal EEG recordings from the CHB-MIT epilepsy dataset [18] are used for the experiments. The dataset consists of scalp EEG from pediatric subjects with intractable seizures. We select a subset of 6 patients (chb01-03, chb05-06, chb10) having the same measurement setup, including males and females, 1.5-14 years old. Interictal periods are extracted at least 4-hour away before a seizure onset and after the seizure ends. The signals are low-pass filtered with a cut-off frequency at 50 Hz and scaled to the range $[-1,1]$. Overall, the dataset contains 43593 signals, from which $70 \%$ are used for training and validation, and the other $30 \%$ are used as the test set. Each signal is 10 -second long ( $\mathrm{T}=10$ ), at a sampling rate of 256 Hz . Additionally, 339 ictal EEG signals are extracted for evaluating epilepsy seizure detection performance.

### 3.2. Evaluation Metrics

Sliced 2-Wasserstein distance (SWD) [19, 20] quantifies the cost of transforming one distribution to another. It is an approximation to the 2-Wasserstein distance using 1D projections for a closed-form solution and is defined as

$$
S \mathcal{W} \mathcal{D}_{2}(\mu, \nu)=\underset{\theta \sim \mathcal{U}\left(\mathbb{S}^{d-1}\right)}{\mathbb{E}}\left[\mathcal{W}_{2}^{2}\left(\theta_{\#} \mu, \theta_{\#} \nu\right)\right]^{\frac{1}{2}}
$$

where $\mu$ and $\nu$ are two probability measures, $\theta_{\#} \mu$ stands for the pushforwards of the projection $\mathbb{R}^{d} \ni X \mapsto\langle\theta, X\rangle$, and $\mathcal{U}\left(\mathbb{S}^{d-1}\right)$ is the uniform distribution on the hypersphere of $d$ dimensions.

Spectral entropy (SEN) measures the uniformity the of signal energy distribution in the frequency-domain. It is given by

$$
\mathbb{H}(x)=-\sum_{f=0}^{f_{s} / 2} P(f) \log _{2}[P(f)]
$$

[^0]
[^0]:    ${ }^{1}$ https://github.com/khuongav/Graphical-Adversarial-Modeling-of-EEG

where $P$ is the normalised power spectral density, and $f_{*}$ is the sampling frequency of signal $x$.

Reconstruction error (REC) measures the differences between the values of an original signal and its reconstruction $\tilde{x}$ as

$$
R E C=\left\|x_{1: T}^{q}-\tilde{x}_{1: T}^{q}\right\|_{1}
$$

### 3.3. Results and Discussion

Table 2: Performances of different GAN models in interictal EEG signal synthesis and reconstruction tasks.


![img-1.jpeg](img-1.jpeg)

Fig. 2: Last 10 -second of a 30 -second synthetic 23-channel EEG signal by the GMMarkov-GAN model, conditioned on patient 3.5 channels with the highest standard deviations are shown.

Table 2 presents the performance of our proposed approaches and the comparison with the BiGAN/ALI model [21, 22]. We denote its conditional version as C-BiGAN/ALI. GMMarkov-GAN is our model characterized by Gaussian mixture and Markov latent structures, while Markov-GAN is only with the Markov structure. CBiGAN/ALI is the GAN with an inference capability but without a latent variable structure, in which the latent space is a simple Gaussian, and data at each timestep are generated independently.

Both the graphical GANs achieve significantly lower SWD, REC, and SEN differences than C-BiGAN/ALI, indicating that they are better at capturing the characteristics of EEG in both time and frequency domains. Besides, by encoding the invariant spatialtemporal features of EEG signals subject to the flexibility of a Gaussian mixture, GMMarkov-GAN enjoys better performance (SWD of 0.0173 , REC of 0.0519 , and SEN difference of 0.035 ) than the Markov-GAN. We attribute this to GMMarkov-GAN being able to learn a structured clustering of the latent space as shown in

Figure 4. These results prove the effectiveness of our proposed data structures and confirm our inverse inference strategy.

By training with the additional FFT loss, GMMarkov-GAN enjoys the highest performance (SWD of 0.0116 , REC of 0.0474 , and SEN difference of 0.012 ). It should be noted that the frequencydomain loss added little time for training, yet it noticeably improved the results.
![img-2.jpeg](img-2.jpeg)

Fig. 3: ROC curve for epilepsy seisure detection.
![img-3.jpeg](img-3.jpeg)

Fig. 4: t-SNE visualization of the static latent spaces.
In Figure 2, synthetic multi-channel EEG signals are plotted. The signals are naturally realistic across channels and show good fits in different frequency bands. Although our model is trained on 10 second-long signals, it can generate much longer sequences of 30 seconds, thanks to the Markov structure.

To demonstrate the efficacy of our generative and inverse mapping approach for auxiliary tasks, we further evaluated our approach in epilepsy seizure detection. As the model is trained on the interictal EEG signals, seizure segments are detected with reconstruction error thresholds in an anomaly detection framework. Figure 3 shows a high detection performance from our model by the ROC curve with the area under the curve of 0.92 , competitive with contemporary approaches in supervised learning [23]. We plan to build on these results in our future work for interpreting more encoded features in the low-dimensional manifolds and further investigate the partial mode collapse issue of GANs.

## 4. CONCLUSION

In this work, we proposed an EEG modeling scheme that combines the strengths of probabilistic graphical models and generative adversarial networks. Our experimental results demonstrate that our method effectively characterized EEG latent variable structure via a Gaussian mixture and a Markov model. The structured representations can provide interpretability and encode inductive biases to reduce the data complexity of neural oscillations. Our approach holds promise to new generative applications in neuroscience and neurology. Future directions include generalizing learning and inference algorithms with more complicated structures to truly model the underlying relationships at different scales spanning from the single cell spike train up to macroscopic oscillations.

## 5. ACKNOWLEDGEMENTS

The authors would like to acknowledge the financial support from the NSF grant \#2051186, the NSF CAREER Award \#1917105 (H.C.), and the NIH SBIR grant \#R44OD024874 (H.C.).
