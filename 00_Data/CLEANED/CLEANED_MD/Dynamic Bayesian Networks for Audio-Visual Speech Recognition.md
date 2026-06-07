# Dynamic Bayesian Networks for Audio-Visual Speech Recognition 

Ara V. Nefian<br>Intel Corporation, Microprocessor Research Labs, 2200 Mission College Blvd., Santa Clara, CA 95052-8119, USA<br>Email: ara.nefian@intel.com

## Luhong Liang

Intel Corporation, Microcomputer Research Labs, Guanghua Road, 100020 Chaoyang District, Beijing, China Email: luhong.liang@intel.com

## Xiaobo Pi

Intel Corporation, Microcomputer Research Labs, Guanghua Road, 100020 Chaoyang District, Beijing, China Email: xiaobo.pi@intel.com

## Xiaoxing Liu

Intel Corporation, Microcomputer Research Labs, Guanghua Road, 100020 Chaoyang District, Beijing, China Email: xiaoxing.liu@intel.com

## Kevin Murphy

Computer Science Division, University of California, Berkeley, Berkeley, CA 94720-1776, USA
Email: murphyk@cs.berkeley.edu

Received 30 November 2001 and in revised form 6 August 2002
The use of visual features in audio-visual speech recognition (AVSR) is justified by both the speech generation mechanism, which is essentially bimodal in audio and visual representation, and by the need for features that are invariant to acoustic noise perturbation. As a result, current AVSR systems demonstrate significant accuracy improvements in environments affected by acoustic noise. In this paper, we describe the use of two statistical models for audio-visual integration, the coupled HMM (CHMM) and the factorial HMM (FHMM), and compare the performance of these models with the existing models used in speaker dependent audio-visual isolated word recognition. The statistical properties of both the CHMM and FHMM allow to model the state asynchrony of the audio and visual observation sequences while preserving their natural correlation over time. In our experiments, the CHMM performs best overall, outperforming all the existing models and the FHMM.

Keywords and phrases: audio-visual speech recognition, hidden Markov models, coupled hidden Markov models, factorial hidden Markov models, dynamic Bayesian networks.

## 1. INTRODUCTION

The variety of applications of automatic speech recognition (ASR) systems for human computer interfaces, telephony, and robotics has driven the research of a large scientific community in recent decades. However, the success of the currently available ASR systems is restricted to relatively controlled environments and well-defined applications such as dictation or small to medium vocabulary voice-based control commands (e.g., hand-free dialing). Often, robust ASR systems require special positioning of the microphone with
respect to the speaker resulting in a rather unnatural humanmachine interface. In recent years, together with the investigation of several acoustic noise reduction techniques, the study of visual features has emerged as attractive solution to speech recognition under less constrained environments. The use of visual features in audio-visual speech recognition (AVSR) is motivated by the speech formation mechanism and the natural ability of humans to reduce audio ambiguity using visual cues [1]. In addition, the visual information provides complementary features that cannot be corrupted by the acoustic noise of the environment. The importance of

![img-0.jpeg](img-0.jpeg)

Figure 1: The audio-visual speech recognition system.
![img-1.jpeg](img-1.jpeg)

Figure 2: The state transition diagram of a left-to-right HMM.
visual features for speech recognition, especially under noisy environments, has been demonstrated by the success of recent AVSR systems [2]. However, problems such as the selection of the optimal set of visual features, or the optimal models for audio-visual integration remain challenging research topics. In this paper, we describe a set of improvements to the existing methods for visual feature selection and we focus on two models for isolated word audio-visual speech recognition: the coupled hidden Markov model (CHMM) [3] and the factorial hidden Markov model (FHMM) [4], which are special cases of the dynamic Bayesian networks [5]. The structure of both models investigated in this paper describes the state synchrony of the audio and visual components of speech while maintaining their natural correlation over time. The isolated word AVSR system illustrated in Figure 1 is used to analyze the performance of the audio-visual models introduced in this paper. First, the audio and visual features (Section 3) are extracted from each frame of the audio-visual sequence. The sequence of visual features, which describe the mouth deformation over consecutive frames, is upsampled to match the frequency of the audio observation vectors. Finally, both the factorial and the coupled HMM (Section 4) are used for audio-visual integration, and their performance for AVSR in terms of parameter complexity, computational efficiency (Section 5), and recognition accuracy (Section 6) is compared to existing models used in current AVSR systems.

## 2. RELATED WORK

Audio-visual speech recognition has emerged in recent years as an active field, gathering researchers in computer vision, signal and speech processing, and pattern recognition [2]. With the selection of acoustic features for speech recognition well understood [6], robust visual feature extraction and selection of the audio-visual integration model are the leading research areas in audio-visual speech recognition.

Visual features are often derived from the shape of the mouth $[7,8,9,10]$. Although very popular, these methods rely exclusively on the accurate detection of the lip contours
which is often a challenging task under varying illumination conditions and rotations of the face. An alternative approach is to obtain visual features from the transformed gray scale intensity image of the lip region. Several intensity or appearance modeling techniques have been studied, including principal component analysis [9], linear discriminant analysis (LDA), discrete cosine transform (DCT), and maximum likelihood linear transform [2]. Methods that combine shape and appearance modeling were presented in $[2,11]$.

Existing techniques for audio-visual (AV) integration [2, 10, 12], consist of feature fusion and decision fusion methods. In feature fusion method, the observation vectors are obtained by the concatenation of the audio and visual features, that can be followed by a dimensionality reduction transform [13]. The resulting observation sequences are modeled using a left-to-right hidden Markov model (HMM) [6] as described in Figure 2. In decision fusion systems the class conditional likelihood of each modality is combined at different levels (state, phone, or word) to generate an overall conditional likelihood used in recognition. Some of the most successful decision fusion models include the multistream HMM, the product HMM, or the independent HMM. The multistream HMM [14] assumes that the audio and video sequences are state synchronous but, unlike the HMM for feature fusion, allows the likelihood of the audio and visual observation sequences to be computed independently. This allows to weigh the relative contribution of the audio and visual likelihood to the overall likelihood based on the reliability of the corresponding stream at different levels of acoustic noise. Although more flexible than the HMM, the multistream HMM cannot accurately describe the natural state asynchrony of the audio-visual speech. The audio-visual multistream product HMM $[11,14,15,16,17]$ illustrated in Figure 3, can be seen as an extension of the previous model by representing each hidden state of the multistream HMM as a pair of one audio and one visual state. Due to its structure, the multistream product HMM allows for audio-video state asynchrony, controlled through the state transition matrix of the model, and forces the audio and video streams to be in synchrony at the model boundaries (phone level in continuous speech recognition systems or word level in isolated word recognition systems). The audio-visual sequences can also be modeled using two independent HMMs [2], one for audio and one for visual features. This model extends the level of asynchrony between the audio and visual states of the previous models, but fails to preserve the natural dependency over time of the acoustic and visual features of speech.

![img-2.jpeg](img-2.jpeg)

Figure 3: The state transition diagram of a product HMM.

## 3. VISUAL FEATURE EXTRACTION

Robust location of the facial features, specially the mouth region, and the extraction of a discriminant set of visual observation vectors are the two key elements of the AVSR system. The cascade algorithm for visual feature extraction used in our AVSR system consists of the following steps: face detection, mouth region detection, lip contour extraction, mouth region normalization and windowing, 2D-DCT and LDA coefficient extraction. Next, we will describe the steps of the cascade algorithm in more detail.

The extraction of the visual features starts with the detection of the speaker's face in the video sequence. The face detector used in our system is described in [18]. The lower half of the detected face (Figure 4a) is a natural choice for the initial estimate of the mouth region.

Next, LDA is used to assign the pixels in the mouth region to the lip and face classes. LDA transforms the pixel values from the RGB chromatic space into a one-dimensional space that best separates the two classes. The optimal linear discriminant space [19] is computed off-line using a set of manually segmented images of the lip and face regions. Figure 4b shows a binary image of the lip segmentation from the lower region of the face in Figure 4a.

The contour of the lips (Figure 4c) is obtained through the binary chain encoding method [20] followed by a smoothing operation. Figures 5a, 5b, 5c, 5d, 5e, 5f, and 5h show several successful results of the lip contour extraction. Due to the wide variety of skin and lip tones, the mouth segmentation and therefore the lip contour extraction may result in inaccurate results (Figures 5i and 5j).

The lip contour is used to estimate the size and the rotation of the mouth in the image plane. Using an affine
![img-3.jpeg](img-3.jpeg)

Figure 4: (a) The lower region of the face used as an initial estimate for the mouth location, (b) binary image representing the mouth segmentation results, (c) the result of the lip contour extraction, (d) the scale and rotation normalized mouth region, (e) the result of the normalized mouth region windowing.
transform a rotation and size normalized grayscale region of the mouth ( $64 \times 64$ pixels) is obtained from each frame of the video sequence (Figure 4d). However, not all the pixels in the mouth region have the same relevance for visual speech recognition. In our experiments we found that, as expected, the most significant information for speech recognition is contained in the pixels inside the lip contour. Therefore, we use an exponential window $w[x, y]=\exp \left(-((x-\right.$ $\left.\left.x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right) / \sigma^{2}$ ), $\sigma=12$, to multiply the pixels values in the grayscale normalized mouth region. The window of size $64 \times 64$ is centered in the center of the mouth region $\left(x_{0}, y_{0}\right)$. Figure 4 e illustrates the result of the mouth region windowing.

Next, the normalized and windowed mouth region is decomposed into eight blocks of height 32 and width 16 , and the 2D-DCT transform is applied to each of these blocks. A set of four 2D-DCT coefficients from a window of size $2 \times 2$ in the lowest frequency in the 2D-DCT domain are extracted from each block. The resulting coefficients extracted are arranged in a vector of size 32 .

In the final stage of the video feature extraction cascade, the multiclass LDA [19] is applied to the vectors of 2D-DCT coefficients. For our isolated word speech recognition system, the classes of the LDA are associated to the words available in the database. A set of 15 coefficients, corresponding to the most significant generalized eigenvalues of the LDA decomposition are used as visual observation vectors.

## 4. THE AUDIO-VISUAL MODEL

The audio-visual models used in existing AVSR systems, as well as the audio-visual models discussed in this paper, are special cases of dynamic Bayesian networks (DBN) [5, 21, 22]. DBNs are directed graphical models of stochastic processes in which the hidden states are represented in

![img-4.jpeg](img-4.jpeg)

Figure 5: Examples of the mouth contour extraction.
![img-5.jpeg](img-5.jpeg)

Figure 6: The audio-visual HMM.
terms of individual variables or factors. A DBN is specified by a directed acyclic graph, which represents the conditional independence assumptions and the conditional probability distributions of each node [23, 24]. With the DBN representation, the classification of the decision fusion models can be seen in terms of independence assumptions of the transition probabilities and of the conditional likelihood of the observed and hidden nodes. Figure 6 represents an HMM as a DBN. The transparent squares represent the hidden discrete nodes (variables), while the shaded circles represent the observed continuous nodes. Throughout this paper, we will refer to the hidden nodes conditioned over time as coupled or backbone nodes and to the remaining hidden nodes as mixture nodes. The variables associated with the backbone nodes represent the states of the HMM, while the values of the mixture nodes represent the mixture component associated with each of the state of the backbone nodes. The parameters of the HMM [6] are

$$
\begin{aligned}
\pi(i) & =P\left(q_{1}=i\right) \\
b_{t}(i) & =P\left(\mathbf{O}_{t} \mid q_{t}=i\right) \\
a(i \mid j) & =P\left(q_{t}=i \mid q_{t-1}=j\right)
\end{aligned}
$$

where $q_{t}$ is the state of the backbone node at time $t, \pi(i)$ is
the initial state distribution for state $i, a(i \mid j)$ is the state transition probability from state $j$ to state $i$, and $b_{t}(i)$ represents the probability of the observation $\mathbf{O}_{t}$ given the $i$ th state of the backbone nodes. The observation probability is generally modeled using a mixture of Gaussian components.

Introduced for audio-only speech recognition, the multistream HMM a (MSHMM) became a popular model for multimodal sequences such as the audio-visual speech. In

$$
b_{t}(i)=\prod_{s=1}^{S}\left[\sum_{m=1}^{M_{i}^{s}} w_{i, m}^{s} N\left(\mathbf{O}_{t}^{s}, \boldsymbol{\mu}_{i, m}^{s}, \mathbf{U}_{i, m}^{s}\right)\right]^{\lambda_{s}}
$$

where $S$ represents the total number of streams, $\lambda_{s}\left(\sum_{t} \lambda_{s}=\right.$ $1, \lambda_{s} \geq 0$ ) are the stream exponents, $\mathbf{O}_{t}^{s}$ is the observation vector of the $s$ th stream at time $t, M_{i}^{s}$ is the number of mixture components in stream $s$ and state $i$, and $\boldsymbol{\mu}_{i, m}^{s}$, $\mathbf{U}_{i, m}^{s}, w_{i, m}^{s}$ are the mean, covariance matrix, and mixture weight for the $s$ th stream, $i$ th state, and $m$ th Gaussian mixture component, respectively. The two streams $(S=2)$ of the audio-visual MSHMM (AV MSHMM) model the audio and the video sequence. For the AV MSHMM, as well as for the HMM used in video-only or audio-only speech recognition, all covariance matrices are assumed diagonal, and the transition probability matrix reflects the left-to-right state evolution

$$
a(i \mid j)=0, \quad \text { if } i \notin\{j, j+1\}
$$

The audio and visual state synchrony imposed by the AV MSHMM can be relaxed using models that allow one hidden backbone node per stream at each time $t$. Figure 7 illustrates a two-stream independent HMM (IHMM) represented as a DBN. Let $\mathbf{i}=\left\{i_{1}, \ldots, i_{S}\right\}$ be some set of states of the backbone nodes, $N$, the number of states of the backbone nodes in stream $s, q_{t}^{s}$ the state of the backbone node in stream $s$ at time $t$ and $\mathbf{q}_{t}=\left\{q_{t}^{1}, \ldots, q_{t}^{S}\right\}$. Formally, the parameters of an

![img-6.jpeg](img-6.jpeg)

Figure 7: A two-stream independent HMM.
![img-7.jpeg](img-7.jpeg)

Figure 8: The audio-visual product HMM.

IHMM are

$$
\begin{aligned}
\pi(\mathbf{i}) & =\prod_{s} \pi^{s}\left(i_{s}\right)=\prod_{s} P\left(q_{1}^{s}=i_{s}\right) \\
b_{t}(\mathbf{i}) & =\prod_{s} b_{t}^{s}\left(i_{s}\right)=\prod_{s} P\left(\mathbf{O}_{t}^{s} \mid q_{t}^{s}=i_{s}\right) \\
a(\mathbf{i} \mid \mathbf{j}) & =\prod_{s} a^{s}\left(i_{s} \mid j_{s}\right)=\prod_{s} P\left(q_{t}^{s}=i_{s} \mid q_{t-1}^{s}=j_{s}\right)
\end{aligned}
$$

where $\pi^{s}\left(i_{s}\right)$ and $b_{t}^{s}\left(i_{s}\right)$ are the initial state distribution and the observation probability of state $i_{s}$ in stream $s$, respectively, and $a^{s}\left(i_{s} \mid j_{s}\right)$ is the state transition from state $j_{s}$ to state $i_{s}$ in stream $s$. For the audio-visual IHMM (AV IHMM) each of the two HMMs, describing the audio or video sequence, is constrained to a left-to-right structure, and the observation likelihood $b_{t}^{s}(i)$ is computed using a mixture of Gaussian density functions, with diagonal covariance matrices. The AV IHMM allows for more flexibility than the AV MSHMM in modeling the state asynchrony but fails to model the natural correlation in time between the audio and visual components of speech. This is a result of the independent modeling of the transition probabilities (see (6)) and of the observation likelihood (see (5)).

A product HMM (PHMM) can be seen as a standard HMM, where each backbone state is represented by a set of states, one for each stream [17]. The parameters of a PHMM
are

$$
\begin{aligned}
\pi(\mathbf{i}) & =P\left(\mathbf{q}_{1}=\mathbf{i}\right) \\
b_{t}(\mathbf{i}) & =P\left(\mathbf{O}_{t} \mid \mathbf{q}_{t}=\mathbf{i}\right) \\
a(\mathbf{i} \mid \mathbf{j}) & =P\left(\mathbf{q}_{t}=\mathbf{i} \mid \mathbf{q}_{t-1}=\mathbf{j}\right)
\end{aligned}
$$

where $\mathbf{O}_{t}$ can be obtained through the concatenation of the observation vectors in each stream

$$
\mathbf{O}_{t}=\left[\left(\mathbf{O}_{t}^{1}\right)^{T}, \ldots,\left(\mathbf{O}_{t}^{S}\right)^{T}\right]^{T}
$$

The observation likelihood can be computed using a Gaussian density or a mixture with Gaussian components. The use of PHMM in AVSR is justified primarily because it allows for state asynchrony, since each of the coupled nodes can be in any combination of audio and visual states. In addition, unlike the IHMM, the PHMM preserves the natural correlation of the audio and visual features due the joint probability modeling of both the observation likelihood (see (8)) and transition probabilities (see (9)). For the PHMM used in AVSR, denoted in this paper as the audio-visual PHMM (AV PHMM), the audio and visual state asynchrony is limited to a maximum of one state. Formally, the transition probability matrix from state $\mathbf{j}=\left[j_{a}, j_{v}\right]$ to state $\mathbf{i}=\left[i_{a}, i_{v}\right]$ is given by

$$
a(\mathbf{i} \mid \mathbf{j})=0 \quad \text { if }\left\{\begin{array}{l}
i_{s} \notin\left[j_{s}, j_{s}+1\right], \\
\left|i_{a}-i_{v}\right| \geq 2,
\end{array} \quad s \in\{a, v\}\right.
$$

where indices $a$ and $v$ denote the audio and video stream, respectively. In the AV PHMM described in this paper (Figure 8) the observation likelihood is computed using

$$
b_{t}(\mathbf{i})=\sum_{m=1}^{M_{\mathbf{i}}} w_{\mathbf{i}, m} \prod_{s}\left[N\left(\mathbf{O}_{t}^{s}, \boldsymbol{\mu}_{\mathbf{i}, m}^{s}, \mathbf{U}_{\mathbf{i}, m}^{s}\right)\right]^{\lambda_{s}}
$$

where $M_{\mathbf{i}}$ represents the number of mixture components associated with state $\mathbf{i}, \boldsymbol{\mu}_{\mathbf{i}, m}^{s}$ and $\mathbf{U}_{\mathbf{i}, m}^{s}$ are the mean and the diagonal covariance matrices corresponding to stream $s$ given the state $\mathbf{i}$ and mixture component $m$, and $w_{\mathbf{i}, m}$ are the mixture weights corresponding to the state $\mathbf{i}$. Unlike the MSHMM (see (2)) the likelihood representation for the PHMM used in (12) models the stream observations jointly through the dependency of the same mixture node. In this paper, the model parameters are trained for fixed values of the stream exponents $\lambda_{s}=1$. For testing, the stream exponents are chosen to maximize the average recognition rate at different acoustic signal-to-noise ratio (SNR) levels. Since in the PHMM both the transition and observation likelihood are jointly computed, and in the IHMM both transition and observation likelihood in each stream are independent, these models can be considered extreme cases of a range of models that combine the joint and independent modeling of the transition probabilities and observation likelihoods. Two of these models, namely the factorial HMM and the coupled HMM, and their application in audio-visual integration will be discussed next.

![img-8.jpeg](img-8.jpeg)

Figure 9: The audio-visual factorial HMM.

### 4.1. The audio-visual factorial hidden Markov model

The factorial HMM (FHMM) [4] is a generalization of the HMM suitable for a large range of multimedia applications that integrate two or more streams of data. The FHMM generalizes an HMM by representing the hidden state by a set of variables or factors. In other words, it uses a distributed representation of the hidden state. These factors are assumed to be independent of each other, but they all contribute to the observations, and hence become coupled indirectly due to the "explaining away" effect [23]. The elements of a factorial HMM are described as

$$
\begin{aligned}
\pi(\mathbf{i}) & =P\left(\mathbf{q}_{1}=\mathbf{i}\right) \\
b_{t}(\mathbf{i}) & =P\left(\mathbf{O}_{t} \mid \mathbf{q}_{t}=\mathbf{i}\right) \\
a(\mathbf{i} \mid \mathbf{j}) & =\prod_{s} a^{s}\left(i_{s} \mid j_{s}\right)=\prod_{s} P\left(q_{t}^{s}=i_{s} \mid q_{t-1}^{s}=j_{s}\right)
\end{aligned}
$$

It can be seen that as with the IHMM, the transition probabilities of the FHMM are computed using the independence assumption between the hidden states or factors in each of the HMMs (see (15)). However, as with the PHMM, the observation likelihood is jointly computed from all the hidden states (see (14)). The observation likelihood can be computed using a continuous mixture with Gaussian components. The FHMM used in AVSR, denoted in this paper as the audio-visual FHMM (AV FHMM), has a set of modifications from the general model. In the AV FHMM used in this paper (Figure 9), the observation likelihoods are obtained from the multistream representation as described in (12). To model the causality in speech generation, the following constraint on the transition probability matrices of the AV FHMM is imposed:

$$
a^{s}\left(i_{s} \mid j_{s}\right)=0, \quad \text { if } i_{s} \notin\left\{j_{s}, j_{s}+1\right\}
$$

where $s \in\{a, v\}$.

### 4.1.1 Training factorial HMMs

As is well known, DBNs can be trained using the expectationmaximization (EM) algorithm (see, e.g., [22]). The EM algorithm for the FHMM is described in Appendix A. However, this only converges to a local optimum, making the choice
of the initial parameters of the model a critical issue. In this paper, we present an efficient method for initialization using a Viterbi algorithm derived for the FHMM. The Viterbi algorithm for FHMMs is described below for an utterance $\mathbf{O}_{1}, \ldots, \mathbf{O}_{T}$ of length $T$.
(i) Initialization

$$
\begin{aligned}
& \delta_{1}(\mathbf{i})=\pi(\mathbf{i}) b_{1}(\mathbf{i}) \\
& \psi_{1}(\mathbf{i})=0
\end{aligned}
$$

(ii) Recursion

$$
\begin{aligned}
& \delta_{t}(\mathbf{i})=\max _{\mathbf{j}}\left\{\delta_{t-1}(\mathbf{j}) a(\mathbf{i} \mid \mathbf{j})\right\} b_{t}(\mathbf{i}) \\
& \psi_{t}(\mathbf{i})=\arg \max _{\mathbf{j}}\left\{\delta_{t-1}(\mathbf{j}) a(\mathbf{i} \mid \mathbf{j})\right\}
\end{aligned}
$$

(iii) Termination

$$
\begin{aligned}
& P^{*}=\max _{\mathbf{i}}\left\{\delta_{T}(\mathbf{i})\right\} \\
& \mathbf{q}_{T}=\arg \max _{\mathbf{i}}\left\{\delta_{T}(\mathbf{i})\right\}
\end{aligned}
$$

(iv) Backtracking

$$
\mathbf{q}_{t}=\psi_{t+1}\left(\mathbf{q}_{t+1}\right)
$$

where $P^{*}=\max _{\mathbf{q}_{1}, \ldots, \mathbf{q}_{T}} P\left(\mathbf{O}_{1}, \ldots, \mathbf{O}_{T}, \mathbf{q}_{1}, \ldots, \mathbf{q}_{T}\right)$, and $a(\mathbf{i} \mid \mathbf{j})$ is obtained using (15). Note that, as with the HMM, the Viterbi algorithm can be computed using the logarithms of the model parameters, and additions instead of multiplication.

The initialization of the training algorithm iteratively updates the initial parameters of the model from the optimal segmentation of the hidden states. The state segmentation algorithm described in this paper reduces the complexity of the search for the optimal sequence of backbone and mixture nodes using the following steps. First, we use the Viterbi algorithm, as described above, to determine the optimal sequence of states for the backbone nodes. Second, we obtain the most likely assignment to the mixture nodes. Given these optimal assignments to the hidden nodes, the appropriate sets of parameters are updated. For the FHMM with $\lambda_{s}=1$ and general covariance matrices the initialization of the training algorithm is described below.

Step 1. Let $R$ be the number of training examples and let $\mathbf{O}_{r, 1}^{s}, \ldots, \mathbf{O}_{r, T_{r}}^{s}$ be the observation sequence of length $T_{r}$ corresponding to the $s$ th stream of the $r$ th $(1 \leq r \leq R)$ training example. First, the observation sequences $\mathbf{O}_{r, 1}^{s}, \ldots, \mathbf{O}_{r, T_{r}}^{s}$ are uniformly segmented according to the number of states of the backbone nodes $N_{s}$. Then, a new sequence of observation vectors is obtained by concatenating the observation vectors assigned to each state $i_{s}, s=1, \ldots, S$. For each state set $\mathbf{i}$ of the backbone nodes, the mixture parameters are initialized using the K-means algorithm [19] with $M_{\mathrm{i}}$ clusters.

Step 2. The new parameters of the model are estimated from the segmented data

$$
\begin{aligned}
\boldsymbol{\mu}_{\mathbf{i}, m}^{s} & =\frac{\sum_{r, t} \gamma_{r, t}(\mathbf{i}, m) \mathbf{O}_{r, t}^{s}}{\sum_{r, t} \gamma_{r, t}(\mathbf{i}, m)} \\
\mathbf{U}_{\mathbf{i}, m}^{s} & =\frac{\sum_{r, t} \gamma_{r, t}(\mathbf{i}, m)\left(\mathbf{O}_{r, t}^{s}-\boldsymbol{\mu}_{\mathbf{i}, m}^{s}\right)\left(\mathbf{O}_{r, t}^{s}-\boldsymbol{\mu}_{\mathbf{i}, m}^{s}\right)^{T}}{\sum_{r, t} \gamma_{r, t}(\mathbf{i}, m)} \\
w_{\mathbf{i}, m} & =\frac{\sum_{r, t} \gamma_{r, t}(\mathbf{i}, m)}{\sum_{r, t} \sum_{m^{\prime}} \gamma_{r, t}\left(\mathbf{i}, m^{\prime}\right)} \\
a^{s}(i \mid j) & =\frac{\sum_{r, t} \epsilon_{r, t}^{s}(i, j)}{\sum_{r, t} \sum_{l} \epsilon_{r, t}^{s}(i, l)}
\end{aligned}
$$

where

$$
\begin{aligned}
\gamma_{r, t}(\mathbf{i}, m) & = \begin{cases}1, & \text { if } \mathbf{q}_{r, t}=\mathbf{i}, c_{r, t}=m \\
0, & \text { otherwise }\end{cases} \\
\epsilon_{r, t}^{s}(i, j) & = \begin{cases}1, & \text { if } q_{r, t}^{s}=i, q_{r, t-1}^{s}=j \\
0, & \text { otherwise }\end{cases}
\end{aligned}
$$

where $q_{r, t}^{s}$ represents the state of the $t$ th backbone node in the $s$ th stream of the $r$ th observation sequence, and $c_{r, t}$ is the mixture component of the $r$ th observation sequence at time $t$.

Step 3. An optimal state sequence $\mathbf{q}_{r, 1}, \ldots, \mathbf{q}_{r, T_{r}}$ of the backbone nodes is obtained for the $r$ th observation sequence using the Viterbi algorithm (see below). The mixture component $c_{r, t}$ is obtained as

$$
c_{r, t}=\max _{m=1, \ldots, M_{k}} P\left(\mathbf{O}_{r, t} \mid \mathbf{q}_{r, t}=\mathbf{i}, c_{r, t}=m\right)
$$

Step 4. The iterations in Steps 2, 3, and 4 are repeated until the difference between the observation probabilities of the training sequences at consecutive iterations falls below a convergence threshold.

### 4.1.2 Recognition using the factorial HMM

To classify a word, the log likelihood of each model is computed using the Viterbi algorithm described in the previous section. The parameters of the FHMM corresponding to each word in the database are obtained in the training stage using clean audio signals ( $\mathrm{SNR}=30 \mathrm{~dB}$ ). In the recognition stage, the audio tracks of the testing sequences are altered by white noise with different SNR levels. The influence of the audio and visual observation streams is weighted based on the relative reliability of the audio and visual features for different levels of the acoustic SNR. Formally, the observation likelihoods are computed using the multistream representation in (12). The values of the audio and visual exponents $\lambda_{s}, s \in\{a, v\}$, corresponding to a specific acoustic SNR level are obtained experimentally to maximize the average recognition rate. Figure 10 illustrates the variation of the audiovisual speech recognition rate for different values of the audio exponent $\lambda_{a}$ and different values of SNR. Note that each of the AVSR curves at all SNR levels reaches smooth maximum levels. This is particularly important in designing robust AVSR systems and allows for the exponents to be chosen in a relatively large range of values. Table 1 describes the

Table 1: The optimal set of exponents for the audio stream $\lambda_{a}$ for the FHMM at different SNR values of the acoustic speech.


audio exponents $\lambda_{a}$ used in our system which were derived from Figure 10. As expected, the value of the optimal audio exponents decays with the decay of the SNR levels, showing the increased reliability of the video at low acoustic SNR.

### 4.2. The audio-visual coupled hidden Markov model

The coupled HMM (CHMM) [3] is a DBN that allows the backbone nodes to interact, and at the same time to have their own observations. In the past, CHMM have been used to model hand gestures [3], the interaction between speech and hand gestures [25], or audio-visual speech [26, 27]. Figure 11 illustrates a continuous mixture two-stream CHMM used in our audio-visual speech recognition system. The elements of the coupled HMM are described as

$$
\begin{aligned}
\pi(\mathbf{i}) & =\prod_{s} \pi^{s}\left(i_{s}\right)=\prod_{s} P\left(q_{s}^{s}=i_{s}\right) \\
b_{t}(\mathbf{i}) & =\prod_{s} b_{t}^{s}\left(i_{s}\right)=\prod_{s} P\left(\mathbf{O}_{t}^{s} \mid q_{t}^{s}=i_{s}\right) \\
a(\mathbf{i} \mid \mathbf{j}) & =\prod_{s} a^{s}\left(i_{s} \mid \mathbf{j}\right)=\prod_{s} P\left(q_{t}^{s}=i_{s} \mid \mathbf{q}_{t-1}=\mathbf{j}\right)
\end{aligned}
$$

Note that in general, to decrease the complexity of the model, the dependency of a backbone node at time $t$ is restricted to its neighbor backbone nodes at time $t-1$. As with the IHMM, in the CHMM the computation of the observation likelihood assumes the independence of the observation likelihoods in each stream. However, the transition probability of each coupled node is computed as joint probability of the set of states at previous time. With the constraint $a^{s}\left(i_{s} \mid \mathbf{j}\right)=a^{s}\left(i_{s} \mid j_{s}\right)$ a CHMM is reduced to an IHMM.

For the audio-visual CHMM (AV CHMM) the observation likelihoods of the audio and video streams are computed using a mixture of Gaussians with diagonal covariance matrices, and the transition probability matrix is constrained to reflect the natural audio-visual speech dependencies

$$
a^{s}\left(i_{s} \mid \mathbf{j}\right)=0 \quad \text { if } \begin{cases}i_{s} \notin\left[j_{s}, j_{s}+1\right] \\ \left|i_{s}-j_{s^{\prime}}\right| \geq 2, & s^{\prime} \neq s\end{cases}
$$

where $s, s^{\prime} \in\{a, v\}$. The CHMM relates also to the Boltzmann zipper [28] used in audio-visual speech recognition. The Boltzmann zipper consists of two linear Boltzmann networks connected such that they can influence each other. Figure 12 illustrates a Boltzmann zipper where each of the Boltzmann chains is represented as an HMM. Note that although the connections between nodes within the same Boltzmann chain can be seen as transition probabilities of an HMM, the connections between nodes of different chains do not have the same significance [19]. Due to its structure, the

![img-9.jpeg](img-9.jpeg)

Figure 10: The FHMM recognition rate against SNR for different audio exponents.

![img-10.jpeg](img-10.jpeg)

Figure 11: The audio-visual coupled HMM.
![img-11.jpeg](img-11.jpeg)

Figure 12: The Boltzmann zipper used in audio-visual integration.

Boltzmann zipper can address the problem of "fast" (audio) and "slow" (visual) observation vector integration.

### 4.2.1 Training the coupled HMM

In the past, several training techniques for the CHMM were proposed including the Monte Carlo sampling method and the $N$-head dynamic programming method [3, 26]. The CHMM in this paper is trained using EM (Appendix B) which makes the choice of robust initial parameters very important. In this section we describe an efficient initialization method of the CHMM parameters, which is similar to the initialization of the FHMM parameters described previously. The initialization of the training algorithm for the CHMM is described by the following steps:

Step 1. Given $R$ training examples, the observation sequence of length $T_{r}$ corresponding to the $r$ th example $(1 \leq r \leq$ $R$ ) and $s$ th stream, $\mathbf{O}_{r, 1}^{s}, \ldots, \mathbf{O}_{r, T_{r}}^{s}$, is uniformly segmented according to the number of states of the backbone nodes $N_{i}$. Hence an initial state sequence for the backbone nodes $q_{r, 1}^{s}, \ldots, q_{r, t}^{s}, \ldots, q_{r, T_{r}}^{s}$ is obtained for each data stream $s$. For each state $i$ in stream $s$ the mixture segmentation of the data assigned to it is obtained using the K-means algorithm [19] with $M_{i}^{s}$ clusters. Consequently the mixture components $c_{r, t}^{s}$
for the $r$ th observation sequence at time $t$ and stream $s$ is obtained.

Step 2. The new parameters of the model are estimated from the segmented data

$$
\begin{aligned}
\boldsymbol{\mu}_{i, m}^{s} & =\frac{\sum_{r, t} \gamma_{r, t}^{s}(i, m) \mathbf{O}_{r, t}^{s}}{\sum_{r, t} \gamma_{r, t}^{s}(i, m)} \\
\mathbf{U}_{i, m}^{s} & =\frac{\sum_{r, t} \gamma_{r, t}^{s}(i, m)\left(\mathbf{O}_{r, t}^{s}-\boldsymbol{\mu}_{i, m}^{s}\right)\left(\mathbf{O}_{r, t}^{s}-\boldsymbol{\mu}_{i, m}^{s}\right)^{T}}{\sum_{r, t} \gamma_{r, t}^{s}(i, m)} \\
w_{i, m}^{s} & =\frac{\sum_{r, t} \gamma_{r, t}^{s}(i, m)}{\sum_{r, t} \sum_{m^{\prime}} \gamma_{r, t}^{s}\left(i, m^{\prime}\right)} \\
a^{s}(i \mathbf{j}) & =\frac{\sum_{r, t} \epsilon_{r, t}^{s}(i, \mathbf{j})}{\sum_{r, t} \sum_{\mathbf{j}} \epsilon_{r, t}^{s}(i, \mathbf{j})}
\end{aligned}
$$

where

$$
\begin{aligned}
\gamma_{r, t}^{s}(i, m) & = \begin{cases}1, & \text { if } q_{r, t}^{s}=i, c_{r, t}^{s}=m \\
0, & \text { otherwise }\end{cases} \\
\epsilon_{r, t}^{s}(i, \mathbf{j}) & = \begin{cases}1, & \text { if } q_{r, t}^{s}=i, \mathbf{q}_{r, t-1}=\mathbf{j} \\
0, & \text { otherwise }\end{cases}
\end{aligned}
$$

where $c_{r, t}^{s}$ is the mixture component for the $s$ th stream of the $r$ th observation sequence at time $t$.

Step 3. An optimal state sequence of the backbone nodes $\mathbf{q}_{r, 1}, \ldots, \mathbf{q}_{r, T_{r}}$ is obtained using the Viterbi algorithm for the CHMM [29]. The steps of the Viterbi segmentation for the CHMM are described by (17), (18), (19), (20), and (21), where the initial state probability $\pi(\mathbf{i})$, the observation likelihood $b(\mathbf{i})$ and transition probabilities $a(\mathbf{i} \mid \mathbf{j})$ are computed using (25), (26), and (27), respectively. The mixture components $c_{r, t}^{s}$ are obtained using

$$
c_{r, t}^{s}=\max _{m=1, \ldots, M_{i}} P\left(\mathbf{O}_{r, t}^{s} \mid q_{r, t}^{s}=i, c_{r, t}^{s}=m\right)
$$

Step 4. The iterations in Steps 2, 3, and 4 are repeated until the difference between the observation probabilities of the training sequences at consecutive iterations falls below a convergence threshold.

### 4.2.2 Recognition using the coupled HMM

The isolated word recognition is carried out via the Viterbi algorithm for CHMM, where the observation probability for each observation conditional likelihood is modified to handle different levels of noise

$$
\hat{b}_{t}^{s}\left(i_{s}\right)=b_{t}\left(\mathbf{O}_{t}^{s} \mid q_{t}^{s}=i_{s}\right)^{\lambda_{s}}
$$

where $\lambda_{s}, s \in\{a, v\}$, are the exponents of the audio and video streams respectively obtained experimentally to maximize the average recognition rate for a specific acoustic SNR level. Table 2 describes the audio exponents $\lambda_{a}$ used in our system, and Figure 13 shows the variation of CHMM-based audiovisual recognition rate for different values of the audio exponent $\lambda_{a}$ and different values of SNR. In all our experiments

Table 2: The optimal set of exponents for the audio stream $\lambda_{a}$ at different SNR values of the acoustic speech for the CHMM.


the audio sequences were perturbed by white noise. The average audio-only, video-only, and CHMM-based audio-visual recognition rates for different levels of SNR are shown in Figure 14.

## 5. MODEL COMPLEXITY ANALYSIS

Together with the recognition accuracy, the number of parameters of the model and the computational complexity required by the recognition process are very important in the analysis of a model. Models with a small number of parameters produce better estimates for the same amount of training data. Tables $3,4,5$, and 6 describe the size of the parameter space and the computational complexity required for recognition using the PHMM, IHMM, FHMM, and CHMM. We consider both the general case as well as the specific models used in AVSR (i.e., AV PHMM, AV IHMM, AV FHMM, and AV CHMM) which include the use of diagonal covariance matrices, and sparse transition probability matrices as described in Section 4. In addition to the notations introduced in the previous section, the size of the observation vector in modality $s$ is denoted by $V_{s}$. For simplification, for the IHMM and CHMM, we consider that all the mixture nodes in stream $s$ have the same number of components $M_{s}$, independent of the state of the parent backbone nodes. For the PHMM and FHMM we assume that all state sets have the same number of mixture components $M$.

In terms of the space required by the parameters of the models, we count the elements of the transition probability matrices ( $\mathbf{A}$ ), the mean vectors $(\boldsymbol{\mu})$, covariance matrices $(\mathbf{U})$, and the weighting coefficients $(w)$ per HMM word. From Tables 3 and 6 we see that the IHMM and CHMM as well as the AV IHMM and AV CHMM, require the same number of parameters for $\boldsymbol{\mu}, \mathbf{U}$, and $w$. This is due to the fact that in these models, the probability of the observation vector $\mathbf{O}_{t}^{t}$ in stream $s$ at time $t$ depends only on its private mixture and backbone node. Due to the coupling of the backbone nodes, the space required by the $\mathbf{A}$ parameters of the CHMM and AV CHMM is larger than that for the IHMM and AV IHMM, respectively. However, if $V_{s} \gg N_{s}$, the space required by the $\mathbf{A}$ parameters is negligible compared to $\boldsymbol{\mu}, \mathbf{U}$ and $w$, making the AV CHMM and AV IHMM very similar from the point of view of the parameter space requirements. The joint dependency of the observation vector $\mathbf{O}_{t}$ on all backbone nodes at time $t$ for the PHMM, FHMM increases significantly the number of parameters of these models compared to the IHMM and CHMM (Tables 4 and 5). Note that the left-to-right topology of each HMM in an AV FHMM (see (16)) does not reduce the number of audio-visual state combinations which remains of the order of $\prod_{s=1}^{2} N_{s}$. On the

Table 3: The number of parameters and running time needed for independent HMMs, and for the specific model used in AVSR.


Table 4: The number of parameters and running time needed for the product HMM, and for the specific model used in AVSR.


Table 5: The number of parameters and running time needed for the factorial HMM, and for the specific model used in AVSR.


other hand, the sparse transition probability matrix of the AV PHMM (see (11)) only allows a number of audio-visual states of the order of $\sqrt{ } \prod_{s=1}^{2} N_{s}$. This reduces the parameter space of the AV PHMM compared to the AV FHMM while still remaining more complex than the AV IHMM or AV CHMM.

In terms of time required by the recognition process, we count the number of log-likelihood additions required by the Viterbi algorithm per time instant (in the row labeled "Viterbi") and the number of operations required for the evaluation of the observation likelihoods. The Viterbi algorithm with the lowest complexity is obtained with the AV IHMM where the transition and observation probabilities in one stream are independent from the transition and observation probabilities in the other stream. On the other hand, the

![img-12.jpeg](img-12.jpeg)

Figure 13: The coupled HMM-based audio-visual speech recognition rate dependency on the audio exponent for different values of the SNR.

![img-13.jpeg](img-13.jpeg)

Figure 14: Comparison of the recognition rate of the audio-only, video-only and CHMM-based audio-visual speech recognition.

Table 6: The number of parameters and running time needed for the coupled HMM, and for the specific model used in AVSR.


joint dependency of the observation node from all the backbone nodes in the same time slice $t$ for the AV FHMM and AV PHMM, or the joint state transition probabilities from all the backbone nodes at time $t-1$ for the AV PHMM and AV CHMM increases significantly the complexity of the Viterbi algorithm for these models. Unlike the AV FHMM, in the AV PHMM and AV CHMM the total number of possible audiovisual states is restricted by the sparse transition probability matrix (see (11) and (28)) reducing the stated decoding complexity of these models. Note that with $M_{s} \approx N_{s}$, which is the case for our experiments, or $M_{s} \gg N_{s}$, which is the case in large vocabulary applications, the dominant role in the complexity required by the recognition process is played by the number of calls to the exponential function needed per time step to evaluate the observation likelihoods. This number equals the total number of elements of mixture weights shown in the row labeled $w$. Therefore, we can conclude that in terms of both the size of the parameter space and the recognition complexity, the AV CHMM and AV IHMM

Table 7: A comparison of the video-only speech recognition rates for different video feature extraction techniques.


compare closely and outperform the AV PHMM, especially the AV FHMM. However, unlike the AV IHMM, the coupling of the backbone nodes in the AV CHMM can model the correlation of the audio-visual components of speech. In the next section, we will complete the analysis of the above models with the experimental results in audio-visual speech recognition.

## 6. EXPERIMENTAL RESULTS

We tested the speaker dependent isolated word audio visual recognition system on the CMU database [18]. Each word in the database is repeated ten times by each of the ten speakers in the database. For each speaker, nine examples of each word were used for training and the remaining example was used for testing. In our experiments we compared the accuracy of the audio-only, video-only and audiovisual speech recognition systems using the AV MSHMM, AV CHMM, AV FHMM, AV PHMM, and AV IHMM described in Section 4. For each of the audio-only and videoonly recognition tasks, we model the observation sequences using a left-to-right HMM with five states, three Gaussian mixtures per state and diagonal covariance matrices. In the audio-only and all audio-visual speech recognition experiments, the audio sequences used in training are captured in clean acoustic conditions and the audio track of the testing sequences was altered by white noise at various SNR levels from 30 dB (clean) to 12 dB . The audio observation vectors consist of 13 MFC coefficients [6], extracted from overlapping frames of 20 ms . The visual observations are obtained using the cascade algorithm described in Section 3.

Table 7 shows the effect of the mouth region windowing and 2D-DCT coefficients extraction (window, 2D-DCT, LDA) on the visual-only recognition rate. It can be seen that the cascade algorithm that uses 2D-DCT coefficients extracted from eight non overlapping blocks of the mouth region followed by LDA (2D-DCT, LDA) outperforms the system that uses 32 1D-DCT coefficients extracted from the mouth region followed by LDA with the same number of coefficients (1D-DCT, LDA). In addition the use of mouth region windowing in the cascade algorithm (window, 1D-DCT, LDA or window, 2D-DCT, LDA) increases the recognition rate of the system without data windowing (1D-DCT, LDA and 2D-DCT, LDA, respectively).

In all audio-visual models the backbone nodes have five states and all mixture nodes are modeled using a mixture of

Table 8: A comparison of the speech recognition rate at different levels of acoustic SNR using an HMM for video-only features (V HMM), an HMM for audio-only features (A HMM), an MSHMM for audio-visual features (AV MSHMM), the independent audio-visual HMM (AV IHMM), the product audio-visual HMM (AV PHMM), the factorial audio-visual HMM (AV FHMM) and the coupled audio-visual HMM (AV CHMM).


three Gaussian density functions, with diagonal covariance matrices. We trained all AV models using equal stream exponents $\left(\lambda_{a}=\lambda_{v}=1\right)$. In testing, the value of the stream exponents were chosen to maximize the average recognition rate for each value of the acoustic SNR. Our experimental results shown in Table 8 indicate that the CHMM-based audio-visual speech recognition system performs best overall, achieving the highest recognition rates in a wide range of SNR from 12 dB to 30 dB . As expected, all the audio-visual systems outperform significantly the audio-only recognition rate in noisy conditions, reaching about $50 \%$ reduction in the word error rate at $\mathrm{SNR}=10 \mathrm{~dB}$. Note that at $\mathrm{SNR}=10 \mathrm{~dB}$ the AVSR recognition rate is practically bounded by the videoonly recognition.

## 7. CONCLUSIONS

This paper studies the use of two types of dynamic Bayesian networks, the factorial and the coupled HMM, and compares their performances with existing models for audiovisual speech recognition. Both the FHMM and CHMM are generalizations of the HMM suitable for a large variety of multimedia applications that involve two or more streams of data. The parameters of the CHMM and FHMM, as special cases of DBN, can be trained using EM. However, EM is a local optimization algorithm that makes the choice of the initial parameters a critical issue. In this paper, we present an efficient method for the parameter initialization, using a Viterbi algorithm derived for each of the two models. For AVSR, the CHMM and the FHMM with two streams, one for audio and one for visual observation sequences, are particularly interesting. Both models allow for audio and visual state asynchrony, while still preserving the natural correlation of the audio and visual observations over time. With the FHMM, the audio and visual states are independent of each other, but they jointly model the likelihood of the audiovisual observation vector, and hence become correlated indirectly. On the other hand, with the CHMM, the likelihoods of the audio and visual observation vectors are modeled
independently of each other, but each of the audio and visual states are conditioned jointly by the previous set of audio and visual states. The performance of the FHMM and the CHMM for speaker dependent isolated word AVSR was compared with existing models such as the multistream HMM, the independent HMM and the product HMM. The coupled HMM-based system outperforms all the other models at all SNR levels from 12 dB to 30 dB . The lower performance of the FHMM can be an effect of the large number of parameters required by this model, and the relatively limited amount of data in our experiments. In contrast, the efficient structure of the CHMM requires a small number of parameters, comparable to the independent HMM, without reducing the flexibility of the model. The best recognition accuracy in our experiments, the low parameter space, and the ability to exploit parallel computation make the CHMM a very attractive choice for audio visual integration. Our preliminary experimental results [30] show that the CHMM is a viable tool for speaker independent audio-visual continuous speech recognition.

## APPENDICES

## A. THE EM ALGORITHM FOR FHMM

The EM algorithm for the multistream FHMM (see (12)) with $\lambda_{s}=1$ and general covariance matrices is described by the following steps.

E Step. The forward probability, defined as $\alpha_{t}(\mathbf{i})=$ $P\left(\mathbf{O}_{1}, \ldots, \mathbf{O}_{t}, \mathbf{q}_{t}=\mathbf{i}\right)$, and the backward probability $\beta_{t}(\mathbf{i})=$ $P\left(\mathbf{O}_{t+1}, \ldots, \mathbf{O}_{T} \mid \mathbf{q}_{t}=\mathbf{i}\right)$ are computed as follows. Starting with the initial conditions

$$
\alpha_{1}(\mathbf{i})=\pi(\mathbf{i}) b_{1}(\mathbf{i})
$$

the forward probabilities are computed recursively from

$$
\alpha_{t}(\mathbf{i})=b_{t}(\mathbf{i}) \sum_{\mathbf{j}} a(\mathbf{i} \mid \mathbf{j}) \alpha_{t-1}(\mathbf{j})
$$

for $t=2,3, \ldots, T$. Similarly, from the initial conditions

$$
\beta_{T}(\mathbf{i})=1
$$

the backward probabilities are computed recursively from

$$
\beta_{t}(\mathbf{j})=\sum_{\mathbf{i}} b_{t+1}(\mathbf{i}) a(\mathbf{i} \mid \mathbf{j}) \beta_{t+1}(\mathbf{i})
$$

for $t=T-1, T-2, \ldots, 1$. The transition probability $a(\mathbf{i} \mid \mathbf{j})$ is computed according to (15). The probability of the $r$ th observation sequence $\mathbf{O}_{r}$ of length $T_{r}$, is computed as $P_{r}=$ $\alpha_{r, T_{r}}\left(N_{1}, \ldots, N_{S}\right)=\beta_{r, 1}(1, \ldots, 1)$ where $\alpha_{r, t}$, and $\beta_{r, t}$ are the forward and backward variables for the $r$ th observation sequence.

M Step. The forward and backward probabilities obtained in the E step are then used to re-estimate the state parameters using

$$
\begin{aligned}
& \boldsymbol{\mu}_{\mathbf{i}, m}^{t}=\frac{\sum_{r}\left(1 / P_{r}\right) \sum_{t} \gamma_{r, t}(\mathbf{i}, m) \mathbf{O}_{r, t}^{t}}{\sum_{r}\left(1 / P_{r}\right) \sum_{t} \gamma_{r, t}(\mathbf{i}, m)} \\
& \mathbf{U}_{\mathbf{i}, m}^{t}=\frac{\sum_{r}\left(1 / P_{r}\right) \sum_{t} \gamma_{r, t}(\mathbf{i}, m)\left(\mathbf{O}_{r, t}^{t}-\boldsymbol{\mu}_{\mathbf{i}, m}^{t}\right)\left(\mathbf{O}_{r, t}^{t}-\boldsymbol{\mu}_{\mathbf{i}, m}^{t}\right)^{T}}{\sum_{r}\left(1 / P_{r}\right) \sum_{t} \gamma_{r, t}(\mathbf{i}, m)} \\
& w_{\mathbf{i}, m}=\frac{\sum_{r}\left(1 / P_{r}\right) \sum_{t} \gamma_{r, t}(\mathbf{i}, m)}{\sum_{r}\left(1 / P_{r}\right) \sum_{t} \sum_{m^{\prime}} \gamma_{r, t}\left(\mathbf{i}, m^{\prime}\right)}
\end{aligned}
$$

where

$$
\begin{aligned}
\gamma_{r, t}(\mathbf{i}, m)= & \frac{\alpha_{r, t}(\mathbf{i}) \beta_{r, t}(\mathbf{i})}{\sum_{\mathbf{i}} \alpha_{r, t}(\mathbf{i}) \beta_{r, t}(\mathbf{i})} \\
& \times \frac{w_{\mathbf{i}, m} \prod_{t} N\left(\mathbf{O}_{r, t}^{t}, \boldsymbol{\mu}_{\mathbf{i}, m}^{t}, \mathbf{U}_{\mathbf{i}, m}^{t}\right)}{\sum_{m^{\prime}} w_{\mathbf{i}, m^{\prime}} \prod_{t} N\left(\mathbf{O}_{r, t}^{t}, \boldsymbol{\mu}_{\mathbf{i}, m^{\prime}}^{t}, \mathbf{U}_{\mathbf{i}, m^{\prime}}^{t}\right)}
\end{aligned}
$$

The state transition probabilities can be estimated using

$$
\tilde{a}^{s}(i \mid j)=\frac{\sum_{r}\left(1 / P_{r}\right) \sum_{\mathbf{i}, \mathbf{j}} \sum_{t} \alpha_{r, t}(\mathbf{j}) a(\mathbf{i} \mid \mathbf{j}) b_{r, t+1}(\mathbf{i}) \beta_{r, t+1}(\mathbf{i})}{\sum_{r}\left(1 / P_{r}\right) \sum_{t} \sum_{\mathbf{j}} \alpha_{r, t}(\mathbf{j}) \beta_{r, t}(\mathbf{j})}
$$

where vectors $\mathbf{i}$ and $\mathbf{j}$ in (A.7) can be any state vectors such that $i_{s}=i$ and $j_{s}=j$, respectively.

## B. THE EM ALGORITHM FOR CHMM

The EM algorithm for the CHMM is described by the following steps.

E Step. The forward probability and backward probability and the observation probability $P_{r}$ are computed as in Appendix A, where the initial state probability $\pi(\mathbf{i})$, the observation probability $b_{i}(\mathbf{i})$, and the transition probability $a(\mathbf{i} \mid \mathbf{j})$ are computed as in (25), (26), and (27).
M Step. The forward and backward probabilities obtained in the E step are used to re-estimate the state parameters as follows:

$$
\begin{aligned}
& \boldsymbol{\mu}_{i, m}^{t}=\frac{\sum_{r}\left(1 / P_{r}\right) \sum_{t} \gamma_{r, t}^{t}(i, m) \mathbf{O}_{r, t}^{t}}{\sum_{r}\left(1 / P_{r}\right) \sum_{t} \gamma_{r, t}^{t}(i, m)} \\
& \mathbf{U}_{i, m}^{t}=\frac{\sum_{r}\left(1 / P_{r}\right) \sum_{t} \gamma_{r, t}^{t}(i, m)\left(\mathbf{O}_{r, t}^{t}-\boldsymbol{\mu}_{i, m}^{t}\right)\left(\mathbf{O}_{r, t}^{t}-\boldsymbol{\mu}_{i, m}^{t}\right)^{T}}{\sum_{r}\left(1 / P_{r}\right) \sum_{t} \gamma_{r, t}^{t}(i, m)} \\
& w_{i, m}^{t}=\frac{\sum_{r}\left(1 / P_{r}\right) \sum_{t} \gamma_{r, t}^{t}(i, m)}{\sum_{r}\left(1 / P_{r}\right) \sum_{t} \sum_{m^{\prime}} \gamma_{r, t}^{t}\left(i, m^{\prime}\right)}
\end{aligned}
$$

where

$$
\begin{aligned}
\gamma_{r, t}^{s}(i, m)= & \frac{\sum_{\mathbf{i} \times \mathbf{t}, i_{s}=i} \alpha_{r, t}(\mathbf{i}) \beta_{r, t}(\mathbf{i})}{\sum_{\mathbf{i}} \alpha_{r, t}(\mathbf{i}) \beta_{r, t}(\mathbf{i})} \\
& \times \frac{w_{i, m}^{s} N\left(\mathbf{O}_{r, t}^{s}, \boldsymbol{\mu}_{i, m}^{s}, \mathbf{U}_{i, m}^{s}\right)}{\sum_{m^{\prime}} w_{i, m^{\prime}}^{s} N\left(\mathbf{O}_{r, t}^{s}, \boldsymbol{\mu}_{i, m^{\prime}}^{s}, \mathbf{U}_{i, m^{\prime}}^{s}\right)}
\end{aligned}
$$

The state transition probabilities can be estimated using

$$
\tilde{a}^{s}(i \mid \mathbf{j})=\frac{\sum_{r}\left(1 / P_{r}\right) \sum_{\mathbf{i}} \sum_{t} \alpha_{r, t}(\mathbf{j}) a(\mathbf{i} \mid \mathbf{j}) b_{r, t+1}(\mathbf{i}) \beta_{r, t+1}(\mathbf{i})}{\sum_{r}\left(1 / P_{r}\right) \sum_{t} \alpha_{r, t}(\mathbf{j}) \beta_{r, t}(\mathbf{j})}
$$

where $\mathbf{i}$ in (B.3) can be any state vector such that $i_{s}=i$.
