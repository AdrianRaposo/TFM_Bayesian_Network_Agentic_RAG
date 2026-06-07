# Invited Paper 

## Bayesian deep learning: A model-based interpretable approach

Takashi Matsubara ${ }^{1 a)}$<br>${ }^{1}$ Graduate School of System Informatics, Kobe University, 1-1 Rokkodai-cho, Nada-ku, Kobe-shi, Hyogo 657-8501, Japan<br>${ }^{a}$ ) matsubara@phoenix.kobe-u.ac.jp

Received August 15, 2019; Revised September 9, 2019; Published January 1, 2020


#### Abstract

Deep learning is considered to be a model-free, end-to-end, and black-box approach. It requires numerous data samples instead of expert knowledge on the target domain. Hence, it does not specify the mechanism and reasons for its decision making. This aspect is considered a critical limitation of deep learning. This paper introduces another viewpoint, namely Bayesian deep learning. Deep learning can be installed in any framework, such as Bayesian networks and reinforcement learning. Subsequently, an expert can implement the knowledge as the graph structure, accelerate learning, and obtain new knowledge on the target domain. The framework is termed as the deep generative model. Conversely, we can directly introduce the Bayesian modeling approach to deep learning. Subsequently, it is possible to explore deep learning with respect to the confidence of its decision making via uncertainty quantification of the output and detect wrong decision-making or anomalous inputs. Given the aforementioned approaches, it is possible to adjust the "brightness" of deep learning.


Key Words: Bayesian deep learning, deep generative model, data mining, uncertainty quantification, anomaly detection

## 1. Introduction

Recent advances in deep learning enabled us to recognize and translate unpreprocessed data. Deep learning exhibits extreme flexibility and constructs a high-level recognition system by leveraging a dataset of numerous samples. It outperformed many conventional model-based approaches that rely on sophisticated assumptions about the target domains in many tasks such as image recognition, natural language processing, and reinforcement learning [1].

Historically, it was proven that artificial neural networks can approximate continuous functions on compact subsets of real numbers $\mathbb{R}$ if they exhibit sufficient hidden units and data samples [2]. Recent studies on neural networks revealed that their expressive power grows exponentially with respect to the number of layers, thereby evincing the effectiveness of deep learning [3,4]. Moreover, in contrast to traditional machine learning models, deep learning with significantly more parameters shows a better generalization ability [5-7] while several regularization techniques, such as early stopping and weight decay, are still important [8]. Deep learning requires numerous data samples instead of expert knowledge of the target domain, i.e., it does not require any assumptions of the underlying mechanism and does not state the mechanism and reasons for its decision making. The aspect is considered as a

critical limitation of deep learning [9].
This paper introduces another viewpoint where deep learning is considered as a function $f \in$ $\mathcal{F}$ found under a cost functional $\mathcal{L}(f)$ as opposed to a specific model $f$ parameterized by $\theta$ and optimized using a cost function $\mathcal{L}(\theta)$. From this viewpoint, deep learning can be installed in any framework such as a Bayesian network and reinforcement learning [10, 11]. Bayesian network is a graph composed of factors in interest and their relationships. An expert can implement knowledge and especially dependency between factors as the graph structure. The relationships are expressed as simple probabilistic functions although they can now be expressed by deep learning to obtain a deep generative model (DGM) [12-14]. We can mine the latent variables and obtain new knowledge on the target domain. The model is no longer a black-box but interpretable at a certain level. Moreover, the introduction of the Bayesian modeling approach to deep learning makes it possible to ask the deep neural network (DNN) about the confidence of its decision making via uncertainty quantification of the output [15]. The uncertainty also provides anomaly detection model that is robust to the variability of the target [16-18].
These topics are referred to as Bayesian deep learning ${ }^{1}$. Conventionally, Bayesian neural networks correspond to neural networks whose weight parameters are random variables [19]. Bayesian deep learning is used to refer to a slightly broader range of topics. Their common goal involves evaluating and interpreting the output and internal state of deep learning in the same manner as conventional models.
The remaining part of this paper is organized as follows. Section 2 introduces DGMs and their mechanisms and applications. Section 3 introduces previous studies on the application of DGM to the analysis of a small-sized dataset. Given the DGM, the studies demonstrated a significant diagnostic accuracy of mental disorders and quantified the region-wise relationship to mental disorders, thereby potentially encouraging further medical studies. Section 4 introduces Bayesian neural networks and uncertainty quantification that enables the assessment of reliability of decision making by DNNs. Section 5 introduces previous studies on anomaly detection leveraging uncertainty. Given the disentanglement of the error sources, the proposed method detects the damages of machine components and biological organs more robustly to the variability in the target domain when compared with conventional approaches.

# 2. Deep generative model 

### 2.1 Prehistory and preliminary

### 2.1.1 Graphical Model

Neural networks can approximate arbitrary functions $y=f(x)$. Similarly, there exists a significant demand for approximating probability distributions $p(x)$, and neural networks for probability are currently investigated. (Deep) Boltzmann machines, sigmoid belief networks, and deep belief networks are examples [20-23]. The models are defined as special versions of directed/undirected graphical models and can serve as universal approximators for their domains. The models exhibit units that are defined as binary or continuous random variables, and thus they require special learning algorithms (other than backpropagation) and Monte Carlo sampling for inference and generation, thereby leading to extremely high computational cost and excessive variance.

### 2.1.2 Autoencoder

An autoencoder (AE) is a neural network that aims at dimension reduction and is composed of two sub-networks termed as encoder and decoder [24]. The encoder maps an input $x$ to an intermediate state $z$, and the decoder reconstructs the input $x$ given state $z$. From the Bayesian network viewpoint, the autoencoder exhibits many characteristics in common with a latent variable model $p(x)=\int_{z} p(x \mid z) p(z)$. The decoder corresponds to a generative model $p(x \mid z)$, and the encoder corresponds to a (variational) posterior inference model $q(z \mid x)$ while they are deterministic. When noise is injected to the input or intermediate layers, the input or hidden units can be considered as random

[^0]
[^0]:    ${ }^{1}$ For example, Bayesian Deep Learning Workshop on NIPS2018 http://bayesiandeeplearning.org/

![img-0.jpeg](img-0.jpeg)

Fig. 1. (left) Graphical model of a latent variable model. (right) Diagram of variational autoencoder (VAE) implemented on neural networks.

variables. Subsequently, the output fluctuates and exhibits a distribution [25], and it is possible to draw a sample from a conditional probability distribution over the output that is implicitly defined by the neural network [26–28]. By performing the inference $q(z|x)$ and generation $p(x|z)$ many times sufficiently, the effect of the original input $x$ vanishes, and it is possible to draw a new sample $x$ from the implicitly defined marginal probability distribution $p(x)$.

### 2.1.3 Mixture density networks

An alternative corresponds to mixture density networks (MDNs), which are deterministic neural networks that output the parameters of a predefined probability distribution (typically, a Gaussian mixture model) [29]. Hence, the output corresponds to the conditional probability $p(x|z)$ given the input $z$. When combining the approaches, a neural network can employ a smaller network that outputs the parameters of a predefined probability distribution as a noise source [30]. We consider that a hidden activation $h$ is a drawn sample from a Gaussian distribution whose parameters correspond to the outputs of a neural network given the input $z$;

$$h \sim p(h|x) = \mathcal{N}(\mu(x), \sigma^2(x)).$$

Alternatively, it is expressed as follows:

$$h = \mu(x) + \sigma(x) \cdot \epsilon, \ \epsilon \sim \mathcal{N}(0, 1).$$

The hidden activation $h$ is fed to the latter part of the neural network. An unbiased estimator of the output $y$ is given by Monte Carlo sampling;

$$p(y|x) = \int_h p(y|h)p(h|x) \simeq \frac{1}{N} \sum_{i=1}^N p(y|h^{(i)}), \ h^{(i)} \sim p(h|x).$$

The estimator still requires Monte Carlo sampling although the variance is considerably smaller than that of deep Boltzmann machines due to the limited number of random variables. The network is unbiasedly trainable because the gradient of the hidden activation $h$ exhibits an expected value equal to that in the deterministic case;

$$\mathbb{E}\left[\frac{\partial h}{\partial \theta}\right] = \frac{\partial h}{\partial \mu} \frac{\partial \mu}{\partial \theta} + \mathbb{E}[e] \frac{\partial \sigma}{\partial \theta} = \frac{\partial h}{\partial \mu} \frac{\partial \mu}{\partial \theta}.$$

### 2.2 Variational autoencoder

Under the situation that noise is injected to a neural network, the neural network forms a probabilistic distribution $p(y|x)$ of the output $y$ and is trained using an objective function $\mathcal{L}(x, y)$. There is neither an objective nor constraint for the hidden activation $h$. The variational inference can be introduced as a framework for training the hidden activation $h$ [31]. A stochastic autoencoder trained using the framework is termed as variational autoencoder (VAE) [10]. Its diagram is shown in Fig. 1.

In a manner similar to an MDN, the encoder of a VAE outputs the parameters of a predefined probability distribution. The technique is specifically termed as a reparameterization trick. The decoder corresponds to a conditional generative model $p(x \mid z)$. When input $x$ corresponds to a vector of continuous variables such as an image or sound data, a Gaussian distribution with a diagonal covariance is typically employed as the conditional probability $p(x \mid z)$. When the input $x$ is composed of discrete variables, such as natural language, categorical or Bernoulli distributions are appropriate. With respect to variational inference, the conditional probability $q(z \mid x)$ corresponds to the variational posterior. A Gaussian distribution with a diagonal covariance is typically employed. Subsequently, the objective function is derived by following the variational inference as

$$
\begin{aligned}
\log p(x) & =\log \frac{p(x, z)}{p(z \mid x)} \\
& =\mathbb{E}_{q(z \mid x)}\left[\log \frac{p(x, z) q(z \mid x)}{p(z \mid x) q(z \mid x)}\right] \\
& =\mathbb{E}_{q(z \mid x)}\left[\log \frac{p(x, z)}{q(z \mid x)}\right]+D_{K L}(q(z \mid x) \| p(z \mid x)) \\
& \geq \mathbb{E}_{q(z \mid x)}\left[\log \frac{p(x, z)}{q(z \mid x)}\right] \\
& =\mathbb{E}_{q(z \mid x)}\left[\log \frac{p(x \mid z) p(z)}{q(z \mid x)}\right] \\
& =-D_{K L}(q(z \mid x) \mid p(x))+\mathbb{E}_{q(z \mid x)}[\log p(x \mid z)] \\
& =: \mathcal{L}(x ; p, q)
\end{aligned}
$$

where $p(z)$ denotes a prior of the latent variable $z$ and $D_{K L}$ denotes the Kullback-Leibler divergence. $\mathcal{L}(x ; p, q)$ is termed as the evidence lower bound (ELBO) and corresponds to the typical objective function to be maximized. After a long period of training, the ELBO $\mathcal{L}(x ; p, q)$ is considered to converge to model evidence $\log p(x)$ [32].

The mean and variance of the prior $p(z)$ can be canceled out with the weight parameters of the encoder and decoder, so the prior $p(z)$ is typically set to a standard Gaussian distribution. Given the reparameterization trick, the Kullback-Leibler divergence and log-likelihood can be easily calculated. For example, when the prior $p(z)$ denotes the standard Gaussian distribution and the posterior $q(z \mid x)$ corresponds to a Gaussian distribution with a diagonal covariance matrix (i.e., $\left.f(z ; \mu(x), \operatorname{diag}\left(\sigma^{2}(x)\right)=\mathcal{N}\left(\mu(x), \operatorname{diag}\left(\sigma^{2}(x)\right)\right)\right)$, the Kullback-Leibler divergence is

$$
\begin{aligned}
D_{K L}(q(z \mid x) \mid p(x)) & =\int_{z} f(z ; \mu(x), \operatorname{diag}\left(\sigma^{2}(x)\right) \log \frac{f(z ; \mu(x), \operatorname{diag}\left(\sigma^{2}(x)\right)}{f(z ; \mathbf{0}, I)} \\
& =\sum_{j} \frac{1}{2}\left(-\log \sigma_{j}^{2}(x)-1+\sigma_{j}^{2}(x)+\mu_{j}^{2}(x)\right)
\end{aligned}
$$

where the subscript $j$ denotes the index related to the latent variable $z$. Additionally, when the posterior $p(x \mid z)$ corresponds to a Gaussian distribution with a diagonal covariance matrix, the loglikelihood is

$$
\begin{aligned}
\mathbb{E}_{q(z \mid x)}[\log p(x \mid z)] & =-\mathbb{E}_{q(z \mid x)}\left[\log f(x ; \mu(z), \operatorname{diag}\left(\sigma_{(}^{2} z)\right))\right] \\
& =-\mathbb{E}_{q(z \mid x)}\left[-\sum \frac{1}{2} \log 2 \pi \sigma^{2}(z)-\sum \frac{(\mu(z)-x)^{2}}{2 \sigma^{2}(z)}\right]
\end{aligned}
$$

where the subscript denotes the index related to the input $x$. Other divergences and probability distributions are also acceptable [33].

It is noted that the original authors introduced the VAE as a simple example of deep learning-based variational inference [10]. A neural network can be used to express the variational posterior of any

![img-1.jpeg](img-1.jpeg)

Fig. 2. (left) Graphical model of a conditional variational autoencoder (cVAE) and (right) its diagram of the implementation on neural networks.

kinds of Bayesian networks such as topic model [14]. In other words, the decoder can be replaced with an existing model while the encoder is a neural network. Then, we analyze and interpret the model as usual.

## 2.3 Structured deep generative model

### 2.3.1 Disentanglement of latent variable

The prior $p(z)$ is typically expected to exhibit the zero-covariance, i.e., each element of the latent variable $z$ is independent of each other and represents a single feature (e.g., an element represents the orientation of an object and another represents the size); this characteristic is termed as disentanglement. Several constraints accelerate the disentanglement by improving the mutual information between the visible variable $x$ and latent variable $z$ [34]. Furthermore, the latent variable $z$ can be disentangled into the local and global features of an image via a hierarchical model that leverages the characteristic of a convolutional neural network [35].

### 2.3.2 Better posterior inference

Even when the prior $p(z)$ is Gaussian, the posterior $p(z|x)$ is never Gaussian and the Gaussian approximation of the variational posterior $q(z|x)$ limits the model performance. When introducing an auxiliary variable $a$ [13], a non-Gaussian variational posterior can be expressed via Monte Carlo sampling of the auxiliary variable $a$, i.e., $q(z|x) = \int_{a} q(z|a)q(a|x)$. Other neural networks with special architectures can be universal approximators of probability distributions [36, 37].

### 2.3.3 With a discrete label

The variational inference based on deep learning is not limited to autoencoder but for all types of graphical models. We consider a graphical model where a categorical variable $y$ serves as a latent variable jointly with a continuous variable $z$ [38];

$$p(x) = \int_{y} \int_{z} p(x|y,z) p(y) p(z).$$

The model is termed as conditional VAE (cVAE) and its diagram is shown in Fig. 2. Thus, the categorical variable $y$ represents the class of visible variable $x$ such as a type of character or a species of animal. Subsequently, the continuous variable $z$ represents the remaining individual variability such as a pen that a subject wrote with and the body size of an animal. The variational posteriors $q(y|x)$ and $q(z|x,y)$ are introduced. The inference model can be trained in the same manner employed during ordinary supervised learning when the class label $y$ of a sample $x$ is known, and the whole model is trainable in unsupervised learning, thereby leading to semi-supervised learning. In this case, the structure assumes the disentanglement between the latent variables $z$ and $y$ although this is not always the case. An adversarial regularization accelerates disentanglement [39].

The integral of a continuous latent variable $z$ can be approximated by Monte Carlo sampling. The integral of a categorical variable $y$ simply corresponds to the sum over possible values, e.g.,

$y=0,1, \ldots$ The computational cost is proportional to the number of categories and is typically excessively expensive for natural language processing tasks. As opposed to the sum, Gumbel-Softmax trick approximates a categorical variable by a continuous variable and enables Monte Carlo sampling $[40]$.

The main purpose of this type of DGM is semi-supervised learning. Even when some samples in a dataset do not exhibit class labels, a structured DGM can infer their class labels under the regularization of reconstruction. However, the generation of realistic data is still a challenging problem, and the reconstruction does not always serve as an appropriate regularizer. The state-of-the-art semisupervised methods are based on manifold regularization [41,42].

# 2.3.4 Time-series and set 

The DGM can be extended to a state-space model such as deep state-space model (DSSM), which models a sequence $\boldsymbol{x}=\left\{x_{t}\right\}_{t=1}^{T}$ of a visible variable $x_{t}$ with an internal state $z_{t}$ [43]. The internal state $z_{t}$ transits to another $z_{t+1}$ by following a transition model $p\left(z_{t+1} \mid z_{t}\right)$. The visible variable $x_{t}$ at time $t$ is conditioned by the internal state $z_{t}$ and expressed by a transmit model $p\left(x_{t} \mid z_{t}\right)$. Each model can be modeled as a feedforward neural network with the reparameterization trick. With respect to inference, Kalman smoother $q\left(z_{t} \mid z_{t-1}, x_{t}, \ldots, x_{T}\right)$ can be employed, which outperforms a mean-field approximator $q\left(z_{t} \mid x_{1}, \ldots, x_{T}\right)$.

When a set $\boldsymbol{x}=\left\{x_{t}\right\}_{t=1}^{T}$ of visible variables $x_{t}$ is given, a shared latent variable $s$ can be expected in addition to a per-sample latent variable $\boldsymbol{z}=\left\{z_{t}\right\}_{t=1}^{T}$. Subsequently, the inference model $q\left(s \mid\left\{x_{t}\right\}\right)$ requires a special architecture invariant for the order of the visible variables [44,45].

## 3. Data analysis and mining by a deep generative model

### 3.1 Introduction

The increasing size of neural networks has achieved significant results in image recognition and many other tasks [1]. However, given numerous parameters, they typically overfit the training dataset and are not generalizable to unknown samples. With respect to a small dataset, (variational) autoencoder is employed as an unsupervised dimension reduction [46] instead of supervised learning. Subsequently, a conventional classifier or dynamical model is applied to the extracted features.

Conversely, an extant study proposed a DGM for a supervised analysis that is robust to small sample sizes [47-50]. Theoretical and experimental studies on the generative model revealed that a generative model analyzes a small dataset more accurately than a discriminative counterpart [51, 52]. While there is no theoretical guarantee, the study experimentally demonstrated that the DGM is useful for analyzing a small dataset when compared to straightforward deep learning models.

It is possible to consider a discriminative model (classifier) $q(y \mid x)$ for a direct classification. With respect to classifying the samples, the classifier must only learn a subset of data features to discriminate the sample classes, and this leads to overfitting. Given a generative model $p(x \mid y)$ conditioned by a class label $y$, it is possible to consider the posterior $p(y \mid x)$ of the class label $y$ given sample $x$ using the Bayes rule;

$$
\begin{aligned}
p(y \mid x) & =p(x \mid y) p(y) / p(x) \\
& \propto p(x \mid y) p(y)
\end{aligned}
$$

In contrast to the classifier, if the assumption of the generative model is appropriate, the generative model can classify a given sample $x$ better and the generative model prevents overfitting. This is because a generative model must understand detailed relations between features to express given samples. The generative model does not work if the assumptions are incorrect.

### 3.2 Deep generative model for medical image analysis

Specifically, this section introduces a DGM especially for mental disorder diagnosis based on functional magnetic resonance imaging (fMRI) data.

![img-2.jpeg](img-2.jpeg)

Fig. 3. Proposed deep generative model (DGM) for medical image analysis. (left) Graphical model and (right) a diagram of the implementation on neural networks.

A mental disorder diagnosis based on machine learning techniques potentially yields accurate and early diagnosis to patients, evaluates the effectiveness of treatments, and determines specific biomarkers. Resting-state fMRI (rs-fMRI) received considerable attention because the approach visualizes interactions among brain regions in subjects at rest, namely it requires subjects neither to perform tasks nor to receive stimuli, and thereby eliminating potential confounders such as individual taskskills [53].

Let $\mathcal{D}$ be a dataset of fMRI features (fMRI images or extracted feature vectors) and diagnoses. The dataset $\mathcal{D}$ contains $N$ subjects. Each subject was given a diagnosis; control $y=0$ or patient $y=1$. Each subject is scanned for $T$ frames and provides a subject-wise set $\boldsymbol{x}=\left\{x_{t}\right\}_{t=1}^{T}$ of fMRI features $x_{t}$. A straight-forward approach involves constructing a classifier that accepts a sequence $\boldsymbol{x}=\left\{x_{t}\right\}_{t=1}^{T}$ and provides a diagnosis $y$. Conversely, the author assumed the following model as shown in Fig. 3.

Each fMRI feature $x_{t}$ is conditioned by the subject's class $y$ and an unobservable latent variable $z_{t}$. The latent variable $z_{t}$ is not related to the class label $y$ but represents frame-wise variability and examples include brain activity related to subject's cognition at that moment and body motion not removed successfully by preprocessing. For the purposes of simplicity, the prior of the frame-wise variability $z_{t}$ is set as time-invariant $p(z)$ (i.e., this model ignores the temporal dynamics). Given the above variables, a frame-wise conditional generative model $p$ of fMRI features $x_{t}$ is expressed as follows:

$$
\begin{aligned}
p(\boldsymbol{x}, y) & =\prod_{t} p\left(x_{t} \mid y\right) p(y) \\
& =\prod_{t} \int_{z_{t}} p\left(x_{t} \mid z_{t}, y\right) p(y) p\left(z_{t}\right)
\end{aligned}
$$

The frame-wise conditional model $p\left(x_{t} \mid y\right)$ is modeled as a conditional VAE as follows:

$$
\begin{aligned}
\log p\left(x_{t} \mid y\right)= & \mathbb{E}_{q\left(z_{t} \mid x_{t}, y\right)}\left[\log \frac{p\left(x_{t}, z_{t} \mid y\right)}{p\left(z_{t} \mid x_{t}, y\right)}\right] \\
= & \mathbb{E}_{q\left(z_{t} \mid x_{t}, y\right)}\left[\log \frac{p\left(x_{t}, z_{t} \mid y\right)}{q\left(z_{t} \mid x_{t}, y\right)}\right] \\
& +D_{K L}\left(q\left(z_{t} \mid x_{t}, y\right) \| p\left(z_{t} \mid x_{t}, y\right)\right) \\
\geq & \mathbb{E}_{q\left(z_{t} \mid x_{t}, y\right)}\left[\log \frac{p\left(x_{t}, z_{t} \mid y\right)}{q\left(z_{t} \mid x_{t}, y\right)}\right] \\
= & -D_{K L}\left(q\left(z_{t} \mid x_{t}, y\right) \| p(z)\right) \\
& +\mathbb{E}_{q\left(z_{t} \mid x_{t}, y\right)}\left[\log p\left(x_{t} \mid z_{t}, y\right)\right] \\
= & \mathcal{L}_{g}\left(x_{t} ; y\right)
\end{aligned}
$$

The frame-wise ELBO $\mathcal{L}_{g}\left(x_{t} ; y\right)$ is summed over frames and subjects and results in the ELBO of the

Table I. Balanced diagnostic accuracies cited from [49].


complete dataset $\mathcal{D}$. The generative model $p\left(x_{t} \mid z_{t}, y\right)$ and inference model $q\left(z_{t} \mid x_{t}, y\right)$ are implemented using feedforward neural networks with the reparameterization trick.

Given the DGM, it is possible to approximate the subject likelihood $p(\boldsymbol{x}, y)$ by using the ELBO $\mathcal{L}_{g}\left(x_{t} ; y\right)$ and get a classifier $p(y \mid \boldsymbol{x})$ using the Bayes rule as follows:

$$
\begin{aligned}
p_{\theta}(y \mid \boldsymbol{x}) & =\frac{p(y) p_{\theta}(\boldsymbol{x} \mid y)}{\sum_{y^{\prime} \in\{0,1\}} p\left(y^{\prime}\right) p_{\theta}\left(\boldsymbol{x} \mid y^{\prime}\right)} \\
& \approx \frac{p(y) \exp \mathcal{L}_{g}(\boldsymbol{x}, y)}{\sum_{y^{\prime} \in\{0,1\}} p\left(y^{\prime}\right) \exp \mathcal{L}_{g}\left(\boldsymbol{x}, y^{\prime}\right)} \\
& =: \exp \mathcal{L}_{d}(\boldsymbol{x}, y)
\end{aligned}
$$

The prior probability $p(y)$ of class $y$ is assumed as $p(y=0)=p(y=1)=0.5$. Thus, if the ELBO $\mathcal{L}_{g}(\boldsymbol{x}, y=1)$ exhibits a large value, then the subject is more likely to exhibit disorder and result in a positive diagnosis.

# 3.3 Experiments and results 

In previous studies [48, 49, 54], the DGM was evaluated using a dataset that was obtained from the OpenfMRI database. Its accession number is ds000030 (https://openfmri.org/dataset/ds000030/). Each image was transformed into a feature vector whose element corresponds to a region-of-interest (ROI, i.e., brain subregion). The detailed preprocessing procedure can be found in [49]. Thus, 113 control subjects, 44 patients with the schizophrenia, and 45 patients with the bipolar disorder were obtained. When compared to general-purpose datasets such as ImageNet [55] and MS COCO [56], the dataset is evidently tiny. The study evaluated the performances using the balanced accuracy, which corresponds to the average of the specificity and sensitivity as summarized in the second bottom row of Table I with comparative models. The detailed experimental setting and introduction of the comparative models are also found in [49]. The DGM outperformed the conventional and comparative models by a large margin for both disorders. The study experimentally demonstrated that the DGM can classify a small dataset better than a deep classifier (LSTM) and a conventional model with a deep dimension reduction ( $\mathrm{AE}+\mathrm{HMM})$.

In a manner not limited to diagnosis, the DGM can give interpretable results. Figure 4 shows the time-series of the signal $x_{t, k}$ obtained from a subject with schizophrenia $(y=1)$, where $k$ denotes the index of the ROIs. The left panels show the left thalamus, and the right panels show the right precuneus. The black lines denote the obtained fMRI signals. In top two panels, the colored lines with shaded areas denote the mean and standard deviation of the posterior distribution $p\left(x_{t, k} \mid z_{t}, y\right)$ of the signal where blue and red colors correspond to the assumptions of the correct label $y=1$ and incorrect label $y=0$, respectively. With respect to the left thalamus, the posterior distribution adequately expresses the obtained signal $x_{t, k}$ under the assumption of the correct label $y=1$ and not very adequately with the incorrect label $y=0$. With respect to the right precuneus, the assumption of the class label $y$ does not affect the posterior distribution.

The frame-wise ELBO $\mathcal{L}_{g}\left(x_{t} ; y\right)$ corresponds to the log-likelihood $\mathbb{E}_{q_{\phi}}\left[\log p_{\theta}\left(x_{t} \mid z_{t}, y\right)\right]$ of a feature

![img-3.jpeg](img-3.jpeg)

Fig. 4. Time-series of the signals $x_{t, k}$ and reconstruction errors $\mathcal{W}(t, k ; y)$ of the left thalamus (left panel) and right precuneus (right panel) of a subject with schizophrenia $(y=1)$. The black lines denote the obtained fMRI signals. The colored lines with shaded areas denote the mean and standard deviation of the posterior distribution $p\left(x_{t, k} \mid z_{t}, y\right)$ of the signal where blue and red colors correspond to the correct label $y=1$ and incorrect label $y=0$, respectively. The colored lines in the bottom panels denote the corresponding ROI-wise reconstruction error $\mathcal{W}(t, k ; y)$ after the constant bias $\frac{1}{2} \log 2 \pi$ is subtracted.

vector $x_{t}$ minus the Kullback-Leibler divergence $D_{K L}\left(q_{\phi}\left(z_{t} \mid x_{t}, y\right) \mid p\left(z_{t}\right)\right)$. The negative log-likelihood corresponds to the reconstruction error of an autoencoder. Hence, it is possible to explicitly divide the feature vector $x_{t}$ into signal intensities $x_{t, k}$ of ROIs $k$ and obtain ROI-wise reconstruction errors,

$$
\begin{aligned}
\mathcal{W}(t, k ; y) & =-\mathbb{E}_{q_{\phi}\left(z_{t} \mid x_{t}, y\right)}\left[\log p_{\theta}\left(x_{t, k} \mid z_{t}, y\right)\right] \\
& =-\mathbb{E}_{q_{\phi}\left(z_{t} \mid x_{t}, y\right)}\left[\log \frac{1}{\sqrt{2 \pi \sigma_{x_{t}}^{2}}} \exp \left(-\frac{\left|x_{t}-\mu_{x_{t}}\right|^{2}}{2 \sigma_{x_{t}}^{2}}\right)\right] \\
& =\mathbb{E}_{q_{\phi}\left(z_{t} \mid x_{t}, y\right)}\left[\log \sigma_{x_{t}}+\frac{\left|x_{t}-\mu_{x_{t}}\right|^{2}}{2 \sigma_{x_{t}}^{2}}\right]+\frac{1}{2} \log 2 \pi
\end{aligned}
$$

The DGM gives a diagnosis based on the difference in the sum of ROI-wise reconstruction errors between assumed class labels $y=1$ and $y=0$. When the reconstruction error of an ROI $k$ becomes much larger given the incorrect class label, the ROI $k$ mainly contributes to the correct diagnosis. Thus, the DGM detects the ROIs related to the disorders. In the present case, the DGM detected the left thalamus as an ROI related to the schizophrenia and right precuneus as an unrelated ROI. Furthermore, the difference in the ROI-wise reconstruction errors is used to quantitatively evaluate the relationships between visible signals $x_{t, k}$ and the underlying attribute $y$.

# 3.4 More assumption and more accuracy 

A DGM is based on a graphical model, and thus we can implement our prior knowledge as a graph structure. This is one of the main advantages of DGMs. In [49], a deep generative model dedicatedly structured for fMRI data analysis was proposed and termed as subject-wise DGM (sw-DGM) as shown in Fig. 5.

The proposed sw-DGM considers individual variability (i.e., a subject-wise feature) as an additional latent variable $s$. The subject-wise feature follows a prior distribution $p(s)$ and is shared by and inferred from all fMRI images $\boldsymbol{x}=\left\{x_{t}\right\}_{t=1}^{T}$ obtained from a subject. The graphical model is expressed as

$$
p_{\theta}(\boldsymbol{x} \mid y)=\prod_{t=1}^{T} p_{\theta}\left(x_{t} \mid y\right)=\prod_{t=1}^{T} \int_{s} \int_{z_{t}} p_{\theta}\left(x_{t} \mid z_{t}, y, s\right) p\left(z_{t}\right) p(s)
$$

The variational inference can be performed in the same manner as the original DGM. With respect to accelerating the discrimination between classes, we also maximize the approximation of the log-

![img-4.jpeg](img-4.jpeg)

Fig. 5. Proposed subject-wise deep generative model (sw-DGM) for medical image analysis. (left) Graphical model and (right) a diagram of the implementation on neural networks.

likelihood of the class label (i.e., $\mathcal{L}_d(\mathbf{x}, y)$ in Eq. (1)) directly [51]. We balanced the two objective functions using the coefficient $\omega \in [0, 1]$ as

$$\mathcal{L}(\mathbf{x}, y) = \omega \mathcal{L}_g(\mathbf{x}, y) + (1 - \omega) \mathcal{L}_d(\mathbf{x}, y). \tag{3}$$

The inference model $q_{\phi}(z_t | x_t, y, s)$ and generative model $p_{\theta}(x_t | y, s, z_t)$ can be implemented as before (see the right two panels in Fig. 5). The implementation of the inference model $q_{\phi}(s|\mathbf{x}, y)$ needs some modification because it accepts a variable-length sequence of fMRI images $\mathbf{x} = \{x_t\}_{t=1}^T$ obtained from a subject. The author and co-researchers proposed a neural network architecture termed as *collection-encoder*, which is composed of stacked two sub-networks as depicted in the second left panel in Fig. 5. The first sub-network accepts a preprocessed fMRI signal $x_t$ and the class label $y$ and then outputs a hidden activation $h_t$. The second sub-network accepts the averaged hidden activation $\bar{h} = \frac{1}{T} \sum_{t=1}^{T} [h_t]$ and outputs the variational posterior $q_{\phi}(s|\mathbf{x}, y)$ of the subject-wise feature $s$.

The resultant accuracy is summarized in the bottom row of Table I, indicating that more assumptions lead to a more accurate result.

### 3.5 Conclusion

The study investigates an extension to temporal dynamics [54]. Another study proposed a DGM for stock price prediction [47]. The DGM constructed a model between news articles and stock price movements and found phrases (e.g., "rising yen" and "price fall") related to the movements without any supervised sentimental information.

Deep learning is considered as a model-free, end-to-end, and black-box approach. However, it is possible to adjust the "brightness" of the model. A pure deep learning model is a good solution given a lack of knowledge about the target domain. A conventional model is suitable for experts on the target domain which can express it via a well-defined formulation. However, the case is not always true. Typically, an individual possesses limited albeit certain knowledge and experiences difficulty in expressing the target using a simple mathematical model. In this case, the DGM is certainly helpful.

## 4. Uncertainty in deep learning

### 4.1 Bayesian inference of deep learning

Dropout is a method that randomly masks units [60]. More specifically, $p$ of units are filled with zero, and other units' activations are multiplied by $1/(1 - p)$ to retain the expected value. Dropout corresponds to a special type of noise injection and also works as data augmentation. From a Bayesian perspective, a weight parameter $w$ becomes a random variable following a Bernoulli distribution $Ber(\rho)$ whose expected value corresponds to $\hat{w}$ [61]. Many similar stochastic components are proposed and include dropconnect and dropblock [62]. Batch normalization is a method that normalizes the hidden activation over a mini-batch, which accelerates the learning process via avoiding the internal

![img-5.jpeg](img-5.jpeg)

Fig. 6. Comparison of uncertainties. Blue and red dots denote samples of classes 0 and 1, respectively.

covariate shift [63]. Given the random mini-batch selection, batch normalization works as noise on weight parameters and leads to a Bayesian model [64].

When the aforementioned stochastic components are installed in a DNN, the output y of the DNN given an input x is also stochastic in the training phase. In the inference phase (i.e., in use), the mean values are ordinarily used, and the weight parameter is deterministically set to w = w̃. The probability distribution p(y|x) of the output y after training is

$$p(y|x) = p(y|x;w = \tilde{w}).$$

The ordinary usage is termed as weight averaging.

However, it is possible to use the stochasticity even in the inference phase and obtain a probabilistic distribution p(y|x, w). A more accurate output y is obtained by averaging over the weight distribution q(w) [65, 66]:

$$p(y|x) = \int_{w} p(y|x, w) q(w) = \mathbb{E}_{q(w)} [p(y|x, w)].$$

The is termed as model averaging. Practically, the expectation is approximated via Monte Carlo sampling.

From this viewpoint, the training of a DNN is considered as the variational inference of the weight distribution q(w) [61]. More directly, some studies (including ours [67, 68]) proposed an auxiliary DNN termed as the hypernetwork to inference the weight distribution q(w) in a manner similar to the inference of hidden states of DGMs [69]. Given a seed drawn from a noise source, the hypernetwork outputs a set of weight parameters and implicitly forms a distribution over it. The hypernetwork is jointly trained with the main DNN by the gradient descent.

### 4.2 Uncertainty quantification

The introduction of the Bayesian techniques to deep learning leads to other advantages, namely uncertainty quantification. Uncertainty is an antonym of confidence. With respect to a classification task, a DNN typically employs the softmax function to express the categorical distribution and cross-entropy as the objective function. Any practical datasets are easily separable because samples are distributed in the very high dimensional space while the number of samples is limited. Subsequently, the DNN tends to output probabilities significantly close to 0 or 1 to minimize the cross-entropy with the ground truth 0-1 probabilities [41, 70, 71]. The phenomenon is termed as over-confidence [72]. With model averaging, even when each drawn model p(y|x, w) outputs a 0–1 probability, their decisions are different from each other. Subsequently, the averaged model Eq(w)[p(y|x, w)] outputs an intermediate value with which the uncertainty is quantified and reliability is assessed.

When distributions of two classes overlap each other, the posterior probability is close to 0.5, and the posterior entropy is high (see Figs. 6(a) and (b)). In practical cases, blurred images, noisy observations, outlines of objects, and hand-scrawled texts are also given decision making with large entropies because the samples are ambiguous and intrinsically difficult to make decisions on. The uncertainty is termed as aleatoric uncertainty. This corresponds to an observation noise of Gaussian

![img-6.jpeg](img-6.jpeg)

Fig. 7. Conceptual diagram of uncertainty and mis-retrieval in an embedding-and-retrieval task.

process [61]. Even with significantly more data, the ambiguity of a sample is unchanged, and the aleatoric uncertainty is also unchanged [15, 73, 74]. The aleatoric uncertainty intrinsically exists in samples and is predicted by the model. The aleatoric uncertainty is also termed as data uncertainty or predictive uncertainty. The aleatoric uncertainty can be measured as the maximum value of class posteriors $p(y \mid x)$, the posterior entropy $H[p(y \mid x)]$, and other similar criteria. With respect to a regression task, the posterior entropy can be measured using the reparameterization trick.

Even at a considerable distance from the overlapped area, the posterior probability corresponds to 0.5 on the decision boundary. However, the decision boundary is unreliable because the boundary is "supported" by a limited number of samples. With the stochastic components, the DNN must output consistent outputs, and thus is trained to suppress the stochasticity. However, given an unfamiliar sample, the output of the DNN still fluctuates [61, 72] in a manner similar to the variance of the Gaussian process without an observation noise [61]. The output variance $\operatorname{Var}_{q(w)}[p(y \mid x, w)]$ can correspond to a measure of the uncertainty of decision making. The uncertainty is termed as epistemic uncertainty [15, 73] (see Fig. 6(c)). The epistemic uncertainty is caused by an insufficient amount of data, and thus it appears far from data distribution and can detect out-of-distribution samples that are potentially mis-classified or with excessive errors [65, 66, 75]. With significantly more data samples, the decision of the DNN becomes stable, and the epistemic uncertainty decreases. From another viewpoint, the epistemic uncertainty indicates an insufficient training of the DNN. The epistemic uncertainty is also termed as model uncertainty. The approach is applicable to a regression task. With respect to a classification task, another study proposed mutual information between the posterior and drawn model [76].

A property that the confidence is proportional to the possibility of correct decision making is termed as calibrated [77]. Both uncertainties contribute to good calibration despite the distinct underlying mechanisms. The performance of uncertainty quantification (reliability assessment) is measured via the expected calibration error (ECE) or the area under a precision-recall curve (AUPRC). The ECE corresponds to the difference between the posterior probability (confidence) and true probability of correct prediction. The AUPRC can be used more generally. The recall corresponds to the fraction of the remaining samples after unreliable samples (samples with large uncertainties) are discarded. The precision corresponds to the performance of the target task (accuracy for classification and squared error for regression). In an embedding-and-retrieval task, given a query sample (e.g., a text), an appropriate target sample (e.g., an image) is found among many candidates based on their similarity in an embedding space. With respect to the embedding task as a regression task, the variance of the embedded vector can correspond to a candidate uncertainty measure. However, an extant study indicated that a large variance does not imply a large possibility of a retrieval failure as conceptually shown in Fig. 7 [66]. When many similar samples are included in a dataset, the DNN becomes familiar with their features and outputs consistent embedding vectors. Paradoxically, this indicates that the DNN encounters a difficult task to discriminate small differences among the similar samples in the dataset. The variance of the embedding vector never detects mis-retrieval. Conversely, we treat the

retrieval task as a classification task and propose a method to approximate the posterior probability of the retrieved target samples, thereby achieving better AUPRCs.

# 5. Uncertainty in anomaly detection 

### 5.1 Anomaly detection based on deep generative models

Anomaly detection is a task to determine "anomalous samples" in a given dataset. Generally, the normal samples are similar to each other and distinct from the anomalous samples. A common assumption is that the anomalous samples are rich in variety, and their number is limited. Subsequently, it is difficult to construct a model of anomalous classes, and a supervised classifier is inappropriate; instead, unsupervised methods are employed (see [78] for a survey). Specifically, a probabilistic model is trained to maximize likelihoods assigned to training samples and then applied to test samples. The probabilistic model detects samples with lower likelihoods as anomalies. DGMs are employed for anomaly detection $[79-82]$.

The DGMs are probabilistic models based on deep learning. The VAE's estimate of the negative log-likelihood of a sample $x$ is bounded as

$$
-\log p(x) \leq-\mathcal{L}(x ; p, q)=D_{K L}(q(z \mid x) \mid p(x))-\mathbb{E}_{q(z \mid x)}[\log p(x \mid z)]
$$

From the viewpoint of an autoencoder, the second term $-\mathbb{E}_{q(z \mid x)}[\log p(x \mid z)]$ corresponds to the reconstruction error, and the first term $D_{K L}(q(z \mid x) \mid p(x))$ corresponds to the regularization term. The AE does not learn features of anomalous samples and fails in reconstructing them. The reconstruction errors of anomalous samples exceed those of normal samples. The low likelihood (large reconstruction error) corresponds to an appropriate measure of the anomaly (anomaly score).

The anomaly detection involves several concepts based on the definition of the anomalous samples. Many recent deep learning studies focused on out-of-distribution (OOD) sample detection [15, 74, 8385]. Samples obtained from the domain used for training are referred to as in-distribution samples, and samples obtained from other domains are referred to as OOD samples. For example, SVHN dataset and CIFAR-10 correspond to datasets of digit images and natural images such as animals and vehicles $[86,87]$, and they are in different domains. When a CIFAR-10 sample is fed to a model trained to classify an SVHN dataset, the model attempts to classify the sample into a digit class although the sample is not a digit image. If a model can detect the OOD samples, the model can call for human intervention in this type of a situation. The OOD sample detection is important for safe machine learning [65]. Thus, the epistemic uncertainty is also a good measure of an anomaly because the uncertainty is related to insufficient training data [85].

With respect to industrial use, anomaly detection is typically referred to as the defect detection. Anomaly samples are obtained from the same domain as normal samples although they contain anomalies such as scratch, defect, defacement, crack, and grime [88-90]. With respect to medical use, a similar task to detect damaged tissues is termed as lesion detection [81]. An extant study revealed that the aleatoric uncertainty is also very important [16-18].

### 5.2 Aleatoric uncertainty in deep generative model

When the posterior probability is modeled as a Gaussian distribution, the reconstruction error $-\mathbb{E}_{q(z \mid x)}[\log p(x \mid z)]$ of the VAE is re-expressed as

$$
-\mathbb{E}_{q(z \mid x)}[\log p(x \mid z)]=\mathbb{E}_{q(z \mid x)}\left[\frac{1}{2} \log (2 \pi)^{N_{x}}|\Sigma|+\frac{1}{2}(\mu-x)^{T} \Sigma^{-1}(\mu-x)\right]
$$

When an input $x$ is decomposed into each element (e.g., pixel) $x_{i}$ indexed by $i$ and the covariance matrix $\Sigma$ is diagonal $\left(\Sigma=\operatorname{diag}\left(\sigma_{x_{i}}\right)\right)$, the approximated negative log-likelihood $\mathcal{L}\left(x_{i} ; x\right)$ of a pixel $x_{i}$ of an image $x$ is as follows:

$$
\mathcal{L}\left(x_{i} ; x\right)=\underbrace{\frac{1}{2} \log 2 \pi \sigma_{x_{i}}^{2}(x)}_{\begin{array}{c}
\text { aleatoric uncertainty } \\
\mathcal{U}\left(x_{i} ; x\right)
\end{array}}+\underbrace{\frac{\left(\mu_{x_{i}}(x)-x_{i}\right)^{2}}{2 \sigma_{x_{i}}^{2}(x)}}_{\begin{array}{c}
\text { normalized error } \\
\mathcal{E}\left(x_{i} ; x\right)
\end{array}}
$$

![img-7.jpeg](img-7.jpeg)

Fig. 8. Receiver operating characteristic (ROC) curves of the models with optimal hyper-parameters.

Table II. Resultant ROC-AUCs on ATLAS-T1w.


where the mean $\mu_{x_{i}}$ and variance $\sigma_{x_{i}}^{2}$ correspond to outputs of the decoder given the input $x$. The first term $\mathcal{U}\left(x_{i} ; x\right)$ corresponds to the log-variance of the posterior, and the second term $\mathcal{E}\left(x_{i} ; x\right)$ corresponds to the squared error normalized by the variance $\sigma_{x_{i}}^{2}$. If a pixel $x_{i}$ is suffering from blur, noisy, at a border of two objects, or surrounded by unknown objects, then it is difficult to accurately reconstruct the pixel $x_{i}$; and the expected squared error $\left(\mu_{x_{i}}(x)-x_{i}\right)^{2}$ increases. Subsequently, the VAE outputs a larger variance $\sigma_{x_{i}}^{2}$ to exceed the normalized error $\mathcal{E}\left(x_{i} ; x\right)$ while increasing the logvariance $\mathcal{U}\left(x_{i} ; x\right)$. Thus, VAE can ignore a pixel $x_{i}$ with a penalty $\mathcal{U}\left(x_{i} ; x\right)$. The VAE balances the first term $\mathcal{U}\left(x_{i} ; x\right)$ and second term $\mathcal{E}\left(x_{i} ; x\right)$ based on the uncertainty of the pixel $x_{i}$ given the image $x$. Hence, the log-variance $\mathcal{U}\left(x_{i} ; x\right)$ can be considered as the aleatoric uncertainty. The log-likelihood of a pixel is lower-bounded by the uncertainty of the pixel even if the VAE constructs a good model [1618]. The study proposed the normalized error $\mathcal{E}\left(x_{i} ; x\right)$ as an alternative anomaly score.

# 5.3 Experiments and results

The study evaluated the proposed normalized error $\mathcal{E}\left(x_{i} ; x\right)$ using a dataset of head magnetic resonance imaging (MRI) [18]. Some kinds of tissues can be emphasized by varying the pulse repetition time and the echo time, and each setting is termed as T1, T2, Flair, etc. For example, cerebro-spinal fluid (CSF) is visible as darker pixels in T1-weighted images while it is brighter in T2-weighted images. The IXI dataset was employed as a training dataset of control subjects [91]. The dataset contains T1-weighted MRI images obtained from 579 healthy subjects. Each image is composed of 256 horizontal slices of $150 \times 256$. The Anatomical Tracings of Lesions After Stroke (ATLAS) dataset was employed for evaluation [92]. The T1-weighted image subset (ATLAS-T1w) contains 220 stroke patients wherein each provides 189 horizontal slices of $197 \times 233$. Each image was scaled and padded to a 3-dimensional image of $128 \times 128 \times 128$.

The study involved preparing an AE and VAE, each consisting of 11 convolution layers. With

![img-8.jpeg](img-8.jpeg)

Fig. 9. Sample from the ATLAS-T1w dataset, ground truth of anomalous regions, and reconstruction by the VAE. The other panels depict the corresponding heat maps of the anomaly scores normalized to [0,1].

respect to the first 10 layers of the encoder, the kernel sizes corresponding to 4×4×4 and 5×5×5 and strides corresponding to 2 and 1 were alternately used. Each layer was followed by batch normalization and the ReLU activation function. The 11th layer exhibited a 3×3×3 kernel and a stride 1. The feature map after n-th layer had N_{c}×2^{n-1} channels. The output corresponded to two feature maps of 2×2×2×$\frac{N_{z}}{8}$ for the VAE and one feature map for the AE. The dimension number of the latent space and number of channels were selected from N_{z} ∈{8, 16, 32, 64, 128, 256, 512} and N_{c} ∈{8, 16, 32}. The squared error was used as the objective function and as an anomaly score for the AE [79, 80]. With respect to the VAE, the pixel-wise squared error, pixel-wise negative ELBO L(x_{i}; x), aleatoric uncertainty U(x_{i}; x), and proposed score E(x_{i}; x) were evaluated as anomaly scores. A modified version of the Gaussian generative model was also evaluated as a baseline [93].

The results are summarized in Table II and Fig. 8. Figure 9 exemplifies a typical result. Figures 9(a) and (b) show the input image and ground truth anomaly (stroke lesion), respectively. As shown in Fig. 9(c), the reconstructed image by the VAE becomes blurred and does not depict the brain gyri in detail. Figures 9(e) and (f) show the squared reconstruction error and indicates the same. The brain gyri exhibits a complicated shape and is difficult to express in terms of the AE and VAE. Hence, the AE mistakenly detects the gyri as anomalies. Figure 9(g) shows the pixel-wise negative ELBO L(x_{i}; x) of the VAE. When compared to the squared error, the gyri exhibits relatively smaller scores, and the anomalous region is emphasized. This is because the squared error (μ_{x_{i}}(x) - x_{i})^{2} was normalized by the variance σ_{x_{i}}^2. The VAE learns that he gyri are difficult to express, and the expected error is large. Subsequently, the VAE outputs a large variance (a large aleatoric uncertainty) to surpass the normalized error E(x_{i}; x) (see Fig. 9(h)). The VAE estimates the error and outputs an appropriate variance provided that the target region is known and normal. Hence, at the anomalous regions, the VAE cannot expect the error, the normalized error E(x_{i}; x) becomes larger than expected, thereby

indicating an anomaly. Figure 9(i) shows the normalized error $\mathcal{E}\left(x_{i} ; x\right)$, and this emphasizes the anomaly regions well and achieves optimal ROC-AUC (see also Table I) With respect to industrial use, please refer to the previous publications [16, 17].

# 6. Conclusion 

This paper introduces Bayesian deep learning, which involves a Bayesian network constructed using deep learning (Section 2) and the analysis of deep learning from the Bayesian viewpoint (Section 4). The study also summarizes recent studies on each topic (Sections 3 and 5).

The author thanks his co-researchers including Prof. Jianfei Cai at Nanyang Technological University, Singapore, Prof. Ben Seymour and his research group members at Center for Information and Neural Networks, Japan, and Prof. Kuniaki Uehara at Kobe University, Japan, and his research group students and alumni.

The study is partially supported by the MIC/SCOPE \#172107101.
