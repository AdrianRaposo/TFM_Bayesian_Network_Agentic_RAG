# Performance of Hidden Markov Model and Dynamic Bayesian Network 

## Classifiers on Handwritten Arabic Word Recognition

Jawad H AlKhateeb ${ }^{1,2}$, Olivier Pauplin ${ }^{2}$, Jinchang Ren ${ }^{3}$, and Jianmin Jiang ${ }^{2}$<br>${ }^{1}$ Dept. of Multimedia Systems, Al-Zaytoonah University, Amman, Jordan<br>${ }^{2}$ Digital Media and System Research Institute, University of Bradford, Bradford, U.K.<br>${ }^{3}$ Centre for excellence in Signal and Image Processing, University of Strathclyde, Glasgow, U.K.

$$
\begin{aligned}
& \text { jawadalkhatib@yahoo.com o.pauplin@bradford.ac.uk } \\
& \text { jinchang.ren@eee.strath.ac.uk j.jiang1@bradford.ac.uk }
\end{aligned}
$$

# Performance of Hidden Markov Model and Dynamic Bayesian 

## Network Classifiers on Handwritten Arabic Word Recognition

Jawad H AlKhateeb ${ }^{1,2}$, Olivier Pauplin ${ }^{2}$, Jinchang Ren ${ }^{3}$, and Jianmin Jiang ${ }^{2}$<br>${ }^{1}$ Dept. of Multimedia Systems, Al-Zaytoonah University, Amman, Jordan<br>${ }^{2}$ Digital Media and System Research Institute, University of Bradford, Bradford, U.K.<br>${ }^{3}$ Centre for excellence in Signal and Image Processing, University of Strathclyde, Glasgow, U.K.

$$
\begin{aligned}
& \text { jawadalkhatib@yahoo.com o.pauplin@bradford.ac.uk } \\
& \text { jinchang.ren@eee.strath.ac.uk j.jiang1@bradford.ac.uk }
\end{aligned}
$$

Abstract: This paper presents a comparative study of two machine learning techniques for recognizing handwritten Arabic words, where hidden Markov models (HMMs) and dynamic Bayesian networks (DBNs) were evaluated. The work proposed is divided into three stages, namely preprocessing, feature extraction and classification. Preprocessing includes baseline estimation and normalization as well as segmentation. In the second stage, features are extracted from each of the normalized words, where a set of new features for handwritten Arabic words is proposed, based on a sliding window approach moving across the mirrored word image. The third stage is for classification and recognition, where machine learning is applied using HMMs and DBNs. In order to validate the techniques, extensive experiments were conducted using the IFN/ENIT database which contains 32492 Arabic words. Experimental results and quantitative evaluations showed that HMM outperforms DBN in terms of higher recognition rate and lower complexity.

Keywords: Off-line handwritten recognition; Hidden Markov model (HMM); dynamic Bayesian Network (DBN); performance evaluation; IFN/ENIT database.

# 1. Introduction 

Handwriting Recognition (HWR) is a mechanism for transforming the written text into a symbolic representation, which plays an essential role in many human computer interaction applications including cheque verification, automatic mail sorting, office automation as well as natural humancomputer interaction [1]. HWR for Latin languages has been conducted and significant achievements have been made. However, there has been less work in Arabic handwriting recognition. This is due to the complexity of the Arabic language and lack of public Arabic handwriting databases. In general, HWR can be categorized into two distinct types: online and off-line based systems. Recognition in online systems uses the dynamics of writing by following the pen movement. Recognition in off-line based systems is based solely on an image of the written text. Online recognition is easier because it can make use of the additional information not available to the off-line systems such as the strength and sequential order of the writing [2]. However, online recognition is not possible in many applications so in this paper, we focus on the off-line recognition of handwritten Arabic text.

The recognition of handwritten Arabic scripts can be divided into segmentation based or segmentation free approaches. The former segments words into characters or letters for recognition and can be regarded as an analytical approach. The latter, which can be regarded as a global approach, takes the whole word image for recognition and therefore needs no segmentation. Although the global approach makes the recognition process simpler, it requires a larger input vocabulary than analytical approach [3].

This paper focuses on the Arabic handwritten word recognition phase and introduces new methods for extracting features. Several experiments have been conducted using the IFN/ENIT benchmark database [4] and our algorithm showed the best recognition rate among the existing work reported using the same database. The remainder of this paper is structured as follows: Section 2 presents the literature review while

Sections 3 and 4 describe the proposed method in terms of pre-processing and feature extraction; Section 5 describes the HMM classification process in details; experimental results are presented in Section 6. The paper ends with conclusions and suggestions for further work.

# 2. Literature Review 

Khorsheed and Clocksin [5] presented a technique for the word can be recognized as single unit which depends on a predefined lexicon. Using the skeleton of the word based on the Stentiford's algorithm [6], all segments were extracted for recognition into feature vector. The extracted the structural features from Arabic cursive text in three consecutive steps: segment extraction, loop extraction and segment transformation. A 8dimensional feature vector was created for each segment. Using Vector quantization (VQ) [7], each vector was mapped to the nearest symbol in the codebook resulting in a sequence of observation which is fed into HMM. The Viterbi algorithm [8] is used to form a codebook of 76 symbols by apportioning the training samples into several classes. The technique was tested with a lexicon of 294 words acquired from a different text sources using the HMM. Recognition rates of up to $97 \%$ were achieved.

Khorsheed [9] presented another holistic recognition system for recognizing Arabic handwritten words. Pre-processing tasks performed included using the Zhang-Suen thinning algorithm [10] to generate the skeleton graph. Structural features for the handwritten script were extracted after skeletonization by decomposing the word skeleton into a sequence of links with an order similar to the word writing order. Using the line approximation [6], each line was broken into small line segments, which were transferred into a sequence of discrete symbols using VQ [7]. Then an HMM recognizer was applied with image skeletonization to the recognition of an old Arabic manuscript which can be found in [11]. One HMM was performed using 296 states on the 32 character models. Each model is left to right HMM with no restriction jump margin. The system was tested on 12960 recognition tests associated with 405 character samples of a single font extracted from the single manuscript. The recognition rates achieved was $72 \%$ without spelling check and $87 \%$ with spelling check.

Paechwitz and Margner [12] presented an off-line recognition system for the Arabic isolated handwritten words. They validated their system using the IFN/ENIT benchmark database [4] which consists of four sets (a,b,c,and d). They used a sliding window based on the image representation of the word image using pixel values as main features. The sliding window is shifted across the word image from right to left and generates the feature vector. The word image is a gray normalized image. The Karhunen Loeve Transformation (KLT) is performed in order to reduce the feature vector dimension. They used Semi Continuous HMMs (SCHMM) classifier for recognition. They used sets a, b, and c for training and set d for testing their system. The recognition rate achieved was $89 \%$.

ElAbed and Magner [13] presented an Arabic isolated handwritten word recognition based on HMM. They used the sliding window approach for extracting the pixel features. They used the skeleton direction based feature extraction technique where each word image was splitting into uniform vertical frames and each word image was split into five horizontal zones with equal height. The lengths of all lines in each zone frame were calculated in four directions to form a 20 dimensional feature. They used HMM for recognition and they validated their system using the IFN/ENIT benchmark database [4]. They used sets a, b, and c for training and set d for testing their system. The recognition rate achieved was $89.1 \%$ for top1 and $96.4 \%$ for top 10.

In El-Hajj et al. [14], a similar sliding window is used in such a window, the word image is divided into vertical overlapping frames with a constant width and variable heights. They validated their system using the IFN/ENIT benchmark database [4]. The sliding window is shifted from right to left and a feature vector is calculated for each frame. For each frame, 24 features are extracted using foreground pixel densities and concavity features. In addition there are 15 baseline independent features. They used HMMs classifier for recognition based on character modeling. Each character has a left right topology. Their HMM model had four states for each character model resulting 159

character models in total. They used sets a, b, and c for training and set d for testing their system. The recognition rate achieved was $75.41 \%$.

Al-Hajj et al. [15] presented a two stage system for recognizing Arabic handwritten words. The first stage system was based on three HMM based classifiers which used pixel features in [14]. Each HMM classifier produces the best ten candidates (Top 10) based on the likelihood. The second stage combined the three HMM classifiers by fusing the candidates provided by the HMM classifiers. They used three schemes for combining the classifiers: the sum rule, the majority vote rule, and the neural network based combining classifier. Different combinations were experimented using the IFN/ENIT benchmark database [4] and the recognition rate achieved was $90.96 \%$.

Al-Hajj et al.[16] presented an off-line recognition system for handwritten Arabic words of city names using the IFN/ENIT benchmark database [4] based on HMM. They used the sliding approach for extracting the features [14]. Their system relies on combining three homogeneous HMM classifiers in order to increase the system performance. They used the same three schemes for combining the classifiers in [15]. The recognition rate achieved was higher than $90 \%$ depends on the candidates. It is $90.26 \%$ for top1, 94.71 for top2, and $95.68 \%$ for top3. It is important to mention that this system used sets a, b, and c for training and set d for testing

Benouareth et al [17, 18] presented an off-line unconstrained handwritten Arabic word recognition based on semi-continuous hidden Markov models (SCHMMs) with explicit state duration. Statistical and structural features were utilized on the basis of the adopted segmentation in which implicit word segmentation is used to divide images into vertical frames of constant and variable width for feature extraction. Based on maxima and minima analysis of the vertical projection histogram, morphological complexity of the Arabic handwritten characters is further considered. They used SCHMM for recognition and they validated their system using the IFN/ENIT benchmark database [4]. They used sets

a, b, and c for training and set d for testing their system. The recognition rate achieved with uniform segmentation was $81.02 .1 \%$ for top1 and $91.74 \%$ for top 10 . The recognition rate achieved with non uniform segmentation was $83.791 \%$ for top1 and $92.12 \%$ for top 10 .

Likforman-Sulem et al. [19, 20] presented a new approach for off-line printed character recognition based on DBN. Their model consists of coupling two HMMs in various DBN architectures. The image rows and image columns of the coupled HMMs were used as the main observations. Their system has been evaluated using various DBN architectures and achieved a recognition rate of $98.3 \%$ with the vertical HMM, and $93.7 \%$ with the horizontal HMM. However, when testing degraded letters the recognition rate went down such as $93.8 \%$ with the vertical HMM and $88.1 \%$ with the horizontal HMM.

In this paper, we proposed an off-line recognition system for the handwritten Arabic cursive using HMM. We split the description of the system into three stages: preprocessing, feature extraction, and classification.

# 3. Preprocessing 

The main aim of the preprocessing is to enhance the inputted signal and to represent it in a way which can be measured consistently for robust recognition. Here the preprocessing stage involves scanning the paper document, removing noise, binarizing the images, segmenting lines and words and estimating baselines. These steps are strongly dependent on the quality of the paper document. As samples of words provided in the IFN/ENIT database have been manually separated and binarized during the development stage [4], the only processes still needed are estimation of the baseline and normalization. Although not needed here, we have investigated how to generally segment words and this and our technique to estimate the baseline can be found in [21].

In an ideal handwriting model, the word has to be written in a horizontal way with both ascenders and descenders aligned along the vertical direction. These conditions in real data are rarely found. So normalization is essential task to remove the variation in the handwritten images for consistent analysis and robust recognition. Among the many algorithms proposed for this purpose, the skeletonization technique is the most popular and likewise the normalization algorithm in [12] has been employed in this research. A sample image in binary format is shown in Figure 1(a), along with its normalized counterpart in Figure 1(b).

# 4. Feature Extraction 

The main goal for feature extraction is to remove the redundancy from the data and gain a more effective representation of the word image by a set of numerical characteristics. Feature extractions deals with extracting most of the essential information from image raw data. Depending on the problem to be solved and its data, different techniques can be applied to extract the features. Features are then mapped into a classifier in order to separate the input words into classes since the features have to be invariant to the variations of the members of each class. Based on [22] features used in off-line recognition are classified into high level ones which are extracted from the whole word image, medium level ones extracted from the letters, and low level ones extracted from sub letters.

Features can be also classified into structural and statistical ones. Structural features describe the topological and geometrical characteristics of a pattern; these include strokes, endpoints, loops, dots and their position related to the baseline. While statistical features are derived from the statistical distribution of pixels and describing the characteristic measurements of a pattern; these include zoning, density distribution of pixels that counts the ones and zeros, moments [23].

This paper implements the HMMs to recognize an unknown Arabic handwritten word. Ideally, this implies that the feature vectors extracted from the Arabic handwritten word is computed as a function of independent variable similar to the feature extracted in speech recognition [24]. Many researchers used the sliding windows/frames technique for extracting the feature vectors in off-line Arabic text recognition from right to left based on the Arabic writing direction [24-26]. In this paper, the sliding window technique used in speech recognition has been applied [25]. In order to speed both training and testing process, each image has been reversed using the mirror tool as shown in Figure 1(c). It is worth mention that all the word images were normalized to have a height 45 pixels. Starting from the first pixel of the word, a sliding window is applied to the mirror word image to estimate the number of black pixels. In this phase the feature vectors for each word mirror image is performed by applying a horizontal sliding window having the same height of the word image, three pixels in width and one pixel overlap. The word mirror image is divided into fifteen horizontal uniform frames; the sliding window is shifted across the word mirror image from left to right as shown in Figure 2, and the feature vector is computed for each window strip. Here, each window is divided into fifteen uniform areas. Each sliding window has 30 features and the first fifteen features $\left(\mathrm{F}_{1}-\mathrm{F}_{15}\right)$ are estimated by averaging the pixels in each region, i.e.

$$
F_{i}=\left(\text { Avg of pixels in the } \mathrm{i}^{\text {th }} \text { vertical area }\right) \mid \mathrm{i} \in[1,15]
$$

The sixteenth feature $\mathrm{F}_{16}$ is the average of all the first fifteen features as follows:

$$
F_{16}=A v g\left(\sum_{i=1}^{15} F_{i}\right)
$$

Then, fourteen additional features $\left(\mathrm{F}_{17}-\mathrm{F}_{30}\right)$ can be determined as follows:

$$
F_{i+16}=A v g\left\{\left(F_{i}+F_{i+1}\right) \mid \mathrm{i} \in[1,14]\right\}
$$

The features extracted by the sliding window can be summarized as follows:

```
Algorithm FEATEXTWINDOWSLIDE
    for k=1 to number of images
    Img_in=Read the normalized image
    Img_in=resize the Img_in into \(45 \times 270\)
    Mirror_image=flip_left_right (Img_in)
    Divide the Mirror_image into 15 horizonatal frame (width \(=3\) pixels)
    Apply Sliding window width \(=3\) and overlap \(=1\) from right to left
        featX( 1:15,:) = featX( 1:15,:) / 18;
        featX( 16 ,: ) = featX( 16 ,:) / 270;
        featX(17:30,:) = featX(17:30,:) / 36;
    end
```


# 5. Classifiers 

### 5.1 Hidden Markov Models

There are several techniques for classifying the text; among these techniques is the Hidden Markov Models (HMMs) which is used for recognizing character, words, and lines. HMMs are widely used in the field of text recognition [25, 27]. The HMMs are statistical models which originally used for speech recognition effectively. Due to the success of the HMMs in speech recognition and due to the similarities between the recognition of speech and cursive handwriting, HMMs were extended for online and off-line handwriting recognition [3, 28].

In off-line recognition systems based on HMMs, the main concept is to transform the word image into a sequence of observations. Several researchers in speech recognition computed the feature vector as a function of independent variable from the speech signal with respect to time by dividing it into frames to simulate the HMMs using sliding windows/frames [24-27, 29]. This technique was used in off-line text recognition where the feature vector is computed as a function of independent variable where the horizontal position along the text line is the independent variable. In this paper, a sliding window is moving across the normalized word image to compute the features based on the pixels of the whole Arabic word.

The Hidden Markov Model is a finite set of states $(N)$, each of which is associated with a probability distribution. Transitions among the states are governed by a set of probabilities called transition probabilities. In order to develop a word recognition system based on the HMMs, the following procedures must be completed: i) Choose the Number of states and observation, ii) Choose the HMM topology, iii) Select the training and the samples, iv) Train the system using the training data, and v) Test the system using the testing data. In this paper, we use the HMM classifier which was implemented on the HMM Toolkit (HTK) for speech recognition [30]. In the literature, many different model topologies were proposed using HMMs. In this paper, a left to right Bakis topology is implemented for the handwriting Arabic word recognition. Figure 3 shows the case of seven states HMM allowing the transition to the same state, next state, and to the following states only. Each state has three different paths the transitions to the same state, next state, and to the state after the next state [31]. The sequence of state transition in training and testing the model depends on the feature observation of the Arabic word.

Generally, HMMs are denoted by $\lambda$ and it is defined by three sets of parameters $\lambda=(\pi, A, B)$ where $A, B$, and $\pi$ represent the following parameters:

1) Matrix of transition probabilities ( $\mathbf{A}$ ):

$$
\begin{gathered}
\mathbf{A}=\left[\begin{array}{ll}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{array}\right] \\
\mathbf{A}=\left\{a_{i j} \mid a_{i j}=P\left(S_{t}=j \mid S_{t-1}=i\right)\right\} \\
a_{m n}=P\left(S_{n} \mid S_{m}\right) ; \quad m, n=1,2
\end{gathered}
$$

Where $a_{m n}$ is the probability that the current state is $S_{n}$ given that the previous state is $S_{m}$. This is calculated as the expected number of transitions from state $S_{m}$ to state $S_{n}$ divided by the expected number of transitions out of state $S_{m}$.
2) Matrix of emission probabilities (B):

$$
\begin{aligned}
& \mathbf{B}=\left[\begin{array}{lll}
b_{11} & b_{12} & b_{13} \\
b_{31} & b_{22} & b_{23}
\end{array}\right] \\
& \mathbf{B}=\left\{b_{j}\left(o_{k}\right) \mid b_{j}\left(o_{k}\right)=P\left(O_{t}=o_{k} \mid S_{t}=j\right)\right\} \\
& b_{n p}=b_{n}(p)=P\left(O_{p} \mid S_{n}\right) ; \quad n=1,2 ; p=1,2,3
\end{aligned}
$$

where $b_{n}(p)$ is the probability that the current observation is $O_{p}$ given that the current state is $S_{n}$. It can be calculated as the expected number of times where $O_{p}$ observed with $S_{n}$ divided by the expected number of times in state $S_{u}$.
3) Initial states probabilities $(\pi)$ :

$$
\begin{aligned}
& \pi=\left[\begin{array}{l}
\pi_{1} \\
\pi_{2}
\end{array}\right] \\
& \pi=\left\{\pi_{i} \mid \pi_{i}=P\left(S_{1}=i\right)\right\} \\
& \pi_{m}=P\left(S_{m}\right) ; \quad m=1,2
\end{aligned}
$$

Due to the several advantages of the HMMs, HMMs have been used in recognizing the Arabic text by many researchers. Among these advantages,

1) There is no need for segmenting the Arabic text.
2) HMMs are capable to tolerate the writing variation due to its resistant to noise,

3) The HMM tools are available freely [25], where $\pi_{m}$ is the expected number of times being in state $S_{m}$ at the start time.

While using the HMMs, there are three main problems associated with:

1. The evaluation problem: Calculating the probability that a model $\lambda=(\pi, A, B)$ created a given sequence of observations.
2. The decoding problem: Finding the most likely sequence of hidden states, in a given model $\lambda=(\pi, A, B)$, that is created by a given sequence of observations.
3. The learning problem: Estimating the model parameters $\lambda=(\pi, A, B)$ so that they best fit a given training sequences of observations.

More details about these problems are discussed in [8, 31]. In addition, a detailed tutorial on the use of HMMs in Speech Recognition is provided in [31]. HMMs have been used for recognizing Arabic handwritten words [1, 12], off-line Arabic handwritten digits [26, 27, 32] and Arabic characters [26]. In this research, we use the HMM classifier which was implemented on the HMM Toolkit (HTK) for speech recognition [30].

In the training phase, the model needs to be optimized using the training data. This is done by applying an iterative optimization method. The Baum-Welch algorithm iterative optimization method is applied to maximize the observation sequence probability $P(O \mid \lambda)$ of the chosen model $\lambda=(\pi, A, B)$. The Baum-Welch algorithm is a variant of the Expectation Maximization (EM) algorithm used to optimize an HMM model parameters $\pi, A$, and $B$ based on the training data. Here, all the model parameters are re-estimated in order to improve the model quality.

The Baum-Welch algorithm is used to adjust the model parameters $\lambda=(\pi, A, B)$ to best fit the observed data. If we have a training dataset of $L$ observation sequences $V=V_{1} V_{2} \ldots V_{L}$ and a known

values for the number of hidden states $(N)$ and the number of possible observations $(M)$, then we aim to maximize the term $P(V \mid \lambda)$.

The set of hidden states is $S=\left\{S_{1}, S_{2}, \ldots, S_{N}\right\}$ with the sequence $Q=q_{1} q_{2} \ldots q_{t}$ representing a sequence of hidden states up to time $t$. In addition, an observed sequence from the set of possible observations $\left\{O_{1}, O_{2}, \ldots, O_{M}\right\}$ can be represented by
$O=o_{1} o_{2} \ldots o_{T}$ which is a sequence of $T$ observations.
According to [31], the following variables need to be defined:

- $\alpha_{t}(m)=P\left(o_{1} o_{1} \ldots o_{t}, q_{t}=S_{m} \mid \lambda\right)$
which is the joint probability of the partial observation sequence up to time $t$ and that the hidden state at time $t$ is $S_{m}$ given $\lambda$.
- $\beta_{t}(m)=P\left(o_{t+1} o_{t+1} \ldots o_{T} \mid q_{t}=S_{m}, \lambda\right)$
which is the probability of the partial observation sequence from time $t+1$ till $T$ given $\lambda$ and that the hidden state at time $t$ is $S_{m}$.
- $\xi_{t}(m, n)=P\left(q_{t}=S_{m}, q_{t+1}=S_{n} \mid o_{1} o_{2} \ldots o_{T}, \lambda\right)$

$$
\begin{aligned}
& =\frac{P\left(q_{t}=S_{m}, q_{t+1}=S_{n}, o_{1} o_{2} \ldots o_{T}\right)}{P\left(o_{1} o_{2} \ldots o_{T} \mid \lambda\right)} \\
& =\frac{\alpha_{t}(m) a_{m n} b_{n}\left(O_{t+1}\right) \beta_{t+1}(n)}{\sum_{m=1}^{N} \sum_{n=1}^{N} \alpha_{t}(m) a_{m n} b_{n}\left(O_{t+1}\right) \beta_{t+1}(n)}
\end{aligned}
$$

which is the probability that the hidden state at time $t$ is $S_{m}$ and at time $t+1$ is $S_{n}$ given the observation sequence and $\lambda$.

- $\gamma_{t}(m)=P\left(q_{t}=S_{m} \mid o_{1} o_{1} \ldots o_{T}, \lambda\right)$

$$
\begin{aligned}
& =\frac{P\left(q_{t}=S_{m}, o_{1} o_{2} \ldots o_{T}\right)}{P\left(o_{1} o_{2} \ldots o_{T} \mid \lambda\right)} \\
& =\frac{\alpha_{t}(m) \beta_{t}(m)}{\sum_{m=1}^{N} \alpha_{t}(m) \beta_{t}(m)} \\
& =\sum_{n=1}^{N} \xi_{t}(m, n)
\end{aligned}
$$

which is the probability that the hidden state at time $t$ is $S_{m}$ given the observation sequence and $\lambda$.

As explained in [33], the Baum-Welch algorithm and the iterative Expectation Maximization (EM) algorithm are identical (have the same solution) for the current problem. Hence, the adjustment process for the parameters $\lambda=(A, B, \pi)$ is started as follows:

1. Initialize the parameters $\lambda=(A, B, \pi)$ randomly: $a_{m n}$ is initialized to $1 / N, b_{m p}$ is initialized to $1 / M$, and $\pi_{\mathrm{m}}$ is initialized to $1 / N$.
2. From the equations (13) through (16), calculate the parameters $\alpha_{t}(m), \beta_{t}(m), \xi_{t}(m, n)$ and $\gamma_{t}(m)$.
3. Calculate the new parameters of the model $\lambda^{*}=\left(A^{*}, B^{*}, \pi^{*}\right)$ according to the values calculated in step 2 as follows:

$$
a_{m n}^{*}=\frac{\sum_{t=1}^{T} \xi_{t}(m, n)}{\sum_{t=1}^{T} \gamma_{t}(m)}, \quad b_{n}^{*}(p)=\frac{\sum_{t=1}^{T} \gamma_{t}(n)}{\sum_{t=1}^{T} \gamma_{t}(n)} \quad \pi_{m}^{*}=\gamma_{1}(m)
$$

4. Calculate $P\left(V \mid \lambda^{*}\right)$. While the probability $P\left(V \mid \lambda^{*}\right)$ is increasing repeat steps 2 and 3 .

After the model parameters converge to some values, these parameters will be describing a model that best fits the training observation sequences.

In the testing phase, the modified Viterbi algorithm is used for recognition. Given the HMM parameter as $\lambda=(A, B, \pi)$, and the observation sequence $\mathrm{O}=\left\{\mathrm{o}_{1}, \mathrm{o}_{2}, \ldots \ldots \ldots \ldots, \mathrm{o}_{\mathrm{N}}\right\}$ was fed into the HTK. The HTK models the observation (feature vector) with a mixture of Gaussian, and it uses the Viterbi algorithm in recognition phase which searches for the highest model probability of a word given the input feature vector $P(O \mid \lambda)$ as

$$
Q=\arg \max P(O \mid \lambda)
$$

# 5.2 Dynamic Bayesian Networks 

Before discussing Dynamic Bayesian Networks (DBNs) the basic foundation of Bayesian networks (BN) is outlined below. BNs are directed probabilistic graphical models. The random variables are represented by nodes, and the conditional dependences among the variables are represented by the arcs between the nodes [34]. BNs are graphical structures that represent the probabilistic relationships among large number of variables. Formally, a Bayesian network for a set of variables $\mathrm{X}=\left\{X_{1}, X_{2}, \ldots, X_{n}\right\}$ is a pair $B=(G, \theta)$ [35]. The first parameter, $G$, is the BN structure, i.e. a directed acyclic graph (DAG) whose nodes correspond to the variables $X_{i} \in X$ and whose edges present their conditional dependencies. For example, if there is an edge from node $\mathrm{X}_{1}$ to node $X_{2}$, then $\mathrm{X}_{1}$ is parent of $X_{2}$ Hence, the value of $X_{2}$ is conditionally dependent on the value of $\mathrm{X}_{1}$. The second parameter $(\theta)$ indicates the set of parameters encoding the conditional probabilities of each node variable $\mathrm{X}_{\mathrm{i}}$ given its parents $\mathrm{Pa}\left(\mathrm{X}_{\mathrm{i}}\right)$. These distributions are represented either by conditional probability tables (CPT) or by conditional probability distributions (CPDs). The CPT is represented when a node and it parents represent discrete variables. In contrast, the CPDs are represented for Gaussian continuous variables [19].

In this paper, the application of DBNs is investigated to the handwritten Arabic word recognition. To our knowledge, this is the first time that the DBN is created to carry out Arabic recognition. The coupled HMMs architectures to be represented as a single DBN [19].

Several coupled HMMs architectures can be constructed by adding directed edges between the two streams within the same time slice [19]. In order to enhance the influence of the vertical stream, the edges are directed from the vertical stream to the horizontal one. Experimentally, it has been proved that the vertical HMM is more reliable than the horizontal one [19]. Due to the fact that both streams are synchronized at each time slice, it is required that both observation sequences in the proposed coupled HMMs architectures have the same length. Therefore, all the normalized word images are resized to be $45 \times 270$.

In the coupled models, there are two states: vertical and horizontal states. The vertical states correspond to the column observations, while the horizontal states correspond to the row observations respectively. Similar to the classic left right HMMs, a transition to the vertical state $X_{t}^{1}$ is depending only on the preceding state value $X_{t-1}^{1}$. However, a transition to the horizontal state $X_{t}^{2}$ is depending on both the preceding state value $X_{t-1}^{2}$ and the current vertical state value $X_{t}^{1}$. The observation dependences are expressed by the dependences between the horizontal and vertical states.

Figure 4 shows three main coupled architectures; the state coupled model (ST_CPL), the general coupled model (GNL_CPL), and the auto regressive coupled model (AR_CPL). Those models were suggested by Likforman-Sulem and Sigelle [19]. The (ST_CPL) is obtained by adding the directed edges between the hidden state nodes of both vertical and horizontal HMMs as shown in Figure 4(a). The GNL_CPL is obtained by adding an edge from hidden states in the horizontal stream $X_{t}^{2}$ to the observation variables in the vertical stream $Y_{t}^{1}$ as shown in Figure 4(b). The AR_CPL is obtained by

coupling both vertical and horizontal streams as shown in Figure 4(c). More details about these three models are found in [19].

In this research, the AR_CPL model is chosen to be used since it is superior and it has achieved the highest recognition rate compared to other coupled models [19].

# 6. Experimental Results 

Any recognition system needs a large database to train and test the system. Real data from banks or the post code are confidential and inaccessible for non commercial research. Although some work was conducted in Arabic handwritten words, but generally they had small databases of their own or the presented results on databases which were unavailable to the public. Consequently, there was no benchmark to compare the results obtained by researches. The work for Arabic script recognition has started more than three decades ago. There was no standard database till 2002 when the IFN/ENIT database (www.ifnenit.com) became available free for non commercial research [4]. This database is very important in this context as it has been used as a standard test database in such a context [4]. In total more than 1000 different people were selected as writers to put their names. In addition, each writer was asked to fill one or more than one form with handwritten pre-selected names of Tunisian town/villages with the corresponding postcode. All the forms were scanned with 300dpi and converted to binary images. The images are divided into five sets so that researches can use some of them for training or testing respectively.

In order to evaluate the performance of our recognition system, several experiments are conducted on the IFN/ENIT database [4] which contains 32492 Arabic words handwritten by more than 1000 different writers and divided into five distinct sets a, b, c, d, and e. In our experiments, we use cross validation to verify the performance of our neural classifier. Each time $80 \%$ of the samples in the

database (sets A, B, C, and D) are used for training and the remaining 20\% (set E) for testing. The HMM classifier was trained and then tested.

# 6.2 HMM Experiments 

In off-line recognition systems based on HMMs, the main concept is to transform the word image into a sequence of observations. In speech recognition, several researchers computed the feature vector as a function of independent variable from the speech signal with respect to time by dividing it into frames to simulate the HMMs using sliding windows/frames [24-27, 29]. This technique was used in off-line text recognition where the feature vector was computed as a function of the horizontal position along the text line as the independent variable. In this HMM research, different techniques have been used to extract the features of the Arabic word as a whole rather than a sliding window, which computes the features based on the DCT coefficients or the mean values of the overlapping blocks of the whole Arabic word.

In this paper, a left to right HMM was used for the Arabic handwritten word. Each word is represented by its feature vector, and each word requires a number of observations for training and testing the HMM. In quantizing the data, experiments were conducted using four codebook size parameter values: $8,16,32$, and 64 . Figure 5 shows the result for the different codebook size values. This suggests that an increase in codebook size yields to a better recognition rate, but it increases the training and testing times. Several numbers of states were tested and the best performance was found using 25 states to represent the word.

Different number of states could be assigned to different words, but in fact the same number of states was chosen for all words. It has been noted that the recognition rate improves as the number of states increases till the HTK reaches the maximum possible state for specific feature set. This

makes the training data independent of the testing data, and hence avoids over fitting the classifier to test the data. To test the effectiveness of different features, two groups of features were mapped separately into the HMM classifier, and the results are reported in Figure 6. Several experiments were carried out based on $80 \%$ cross validation using the HMM and the average recognition rate was recorded.

# 6.2 DBN Experiments 

The DBN experiments have been conducted with the BayesNet Toolbox for Matlab [37], which provides source code to perform several operations on BNs and DBNs. The DBN parameters are learned using the EM algorithm. Again the first four set (a-d) of the IFN/ENIT database are used for training and the remaining one (set e) is used for testing.

Since DBN is working based on time slice, this is consistent with our features extracted from sliding windows. To test the effectiveness of the DBN, the pixel features extracted using the sliding window were mapped into the DBN. The DBN requires a balanced database for training and testing which is not the case in the IFN/ENIT database. To overcome this problem, the training and testing samples from the IFN/ENIT were randomly selected and used in our experiments. This process repeated five times, and an average recognition rate is then obtained. Table 1 summarizes the recognition results, where in general the results from the five tests are quite similar to each other. An average recognition rate of abut $66 \%$ is achieved.

### 6.3 Comparing with Other Systems

We compared our results with other systems tested in the same data set and conditions in ICDAR 2005 Arabic handwriting [36]. Figure 7 summarizes this comparison. As seen from Figure 7, our algorithm performs better in classifying the word image with an improved recognition rate of

about $7 \%$. In addition, it is found that HMM yields much better results than DBN in terms of recognition rate, despite of complicated modeling used in DBN.

It is worth noting that in the reference systems three of them have produced good results with recognition rate over $65 \%$, i.e. the first, the fourth and the sixth. In fact, a two-tier neural classifier is employed in the first system, where modeling of subwords and lexicon aided classification are utilized. In the fourth system, baseline dependent features are extracted and fed into a 1-D HMM, and character model is learnt with support of language knowledge modeling for effective word recognition. In the sixth system [12], semi-continuous 1-D HMM is employed for word recognition, using pixel value features collected from a sliding window approach. To reduce writing variability, several normalization steps are adopted involving normalized height, length and baseline skew. Using HMM classifier, the fourth and the sixth produce higher recognition rate of about $75 \%$, i.e. $10 \%$ more than that of the first one using neural classifier.

The effectiveness of our proposed techniques and their potential applications are analyzed as follows. First of all, it is the proposed features which contribute more to the good performance of the proposed system. When the similar HMM classifier is used, our system has gained over $7 \%$ in terms of recognition rate. Unlike pure pixel value features used in [12], average pixel values and their cross-frame combinations in our system are useful to overcome variability in writing towards more robust recognition. Such features and concepts can be also applied in other pattern recognition and machine learning tasks where signals contain continuous nature, such as speech recognition, gesture recognition and recognition of other handwritten languages.

Secondly, it is worth noting that it seems HMM is among the best classifiers as it produces much higher recognition rate than those using neural network and DBN. Again, this is due to the fact that the probabilistic state transfer in HMM has the intrinsic capacity in modelling connected nature

of Arabic cursive script [12, 14, 24]. On the other hand, it is surprising to find that DBN performs much worse than HMM, although HMM is regarded as a much simplified version of DBN [19]. The reason behind probably can be explained as follows. Generally, DBN is capable of modelling more complicated cases like spatial and temporal structure, even in multi-resolution. On the contrast, HMM is suitable for modelling linear cases such as speech. As a result, DBN has the potential to deal well with handwritten recognition tasks as images of handwritten words are in 2-D. However, features extracted using average pixel values from sliding window schemes might have simplified handwritten recognition to a linear case, hence HMM works more effectively than DBN. How to extract useful features and fully make use of the potential of DBN needs further investigation.

# 7. Conclusions 

In this paper, the performance of both HMMs and DBNs classifiers were compared in terms of recognizing the handwritten Arabic words. Both classifiers are superior in classifying handwritten and printed scripts. The performance of both HMMs and DBNs classifiers on handwritten Arabic word recognition are reported. Actually, HMM is an excellent in classifying Arabic handwritten words. The system has been applied to the well-known IFN/ENIT database containing handwriting words written by different writers. We have found that the pixel density features are effective in our classifiers, and good results of recognition rate have been achieved. In addition, this system can be applied to other patterns for recognition with slightly adaptation. The result obtained in this research show that the best performances are always reached by the HMMs. This shows the superiority of the HMMs over all various classifiers used. Regarding the speed, HMMs were faster in training and testing time. For future investigation, we may consider introducing fuzzy logic in classification [38], exploring the possibility for more efficiency [39] and adding feature selection [40] in our system.
