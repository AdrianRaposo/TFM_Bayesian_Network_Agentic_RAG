# Applied Mathematics and Nonlinear Sciences 

## Strategies for improving Chinese language proficiency based on artificial intelligence technology

Yuanyuan Sun ${ }^{\dagger}$<br>Office of Academic Affairs, Shangqiu Polytechnic, Shangqiu, 476000, China

Submission Info
Communicated by Z. Sabir
Received January 29, 2022
Accepted July 19, 2022
Available online March 21, 2023


#### Abstract

In recent years, the development of artificial intelligence technology and theory has been rapid, and the application in language science has been gradually comprehensive and diversified, especially the accuracy rate of artificial intelligence for Chinese language is up to $90 \%$. In the era of artificial intelligence, the effect of different structures and parameters of arithmetic models on Chinese language recognition varies greatly. Language science is an important research area for realizing machine-human communication, and accurate comprehension of the meaning of linguistic expressions is the key to realize communication. In this paper, we construct a speech system that is different from the traditional stable time series for the irreplaceable characteristics of artificial intelligence technology to improve Chinese language ability. A dynamic Bayesian network (DBN) is used for modeling and analysis, and a DBN construction method is investigated to import a hidden Markov model in a speech recognition system to reveal the interactions between nodes within multiple time slices. The accuracy of dynamic Bayesian networks in Chinese dialect inference algorithms is demonstrated using Matlab simulations to characterize the reliability of speech features using a speech spectrogram. It proves that artificial intelligence technology and Chinese language science are complementary and mutually reinforcing, showing a good and rapid development trend.


Keywords: artificial intelligence; Chinese language system; dynamic Bayesian network; speech spectrogram; speech recognition
AMS 2020 codes: 68 T 35

[^0]
[^0]:    $\dagger$ Corresponding author.
    Email address: syy202202@126.com
    ISSN 2444-8656
    s sciendo
    https://doi.org/10.2478/amns.2023.1.00074
    QPED Access © 2023 Yuanyuan Sun, published by Sciendo.
    (C) BY

    This work is licensed under the Creative Commons Attribution alone 4.0 License.

# 1 Introduction 

The rapid development of artificial intelligence technology has strongly promoted the integration of various fields with artificial intelligence, and the field of teaching Chinese as a foreign language is no exception. The application space and development potential of artificial intelligence technology in international Chinese language education is great, and it can innovate the teaching system and form of international Chinese language education [1]. Artificial intelligence technology can currently be used to reconstruct the international Chinese language education system [2]. Expanding the scope of organic integration of AI technology, using AI to change the existing teaching system, and subsuming AI technology into teaching Chinese and HSK tutoring are the current research priorities in the field. The introduction of AI technology in Chinese language learning will strengthen the "learner-centered" educational concept of educational APPs and realize the human-computer interaction experience [35], as well as develop the thinking ability of Chinese as a second language learners and improve their expression ability, so as to achieve the purpose of using Chinese for communication [6]. The future use of AI in education will improve the adaptability to the environment and will strengthen the education of cultural factors, showing a general trend of differentiation and integration, "learning and teaching" [7-8]. The application of artificial intelligence in education can provide effective help and reflection for educational change and innovation [9-11].

In recent years, Chinese speech recognition has been applied to many fields such as automatic control, pattern recognition, and secure communication. Convolutional neural networks are increasingly becoming one of the research hotspots in the field of computational intelligence because of their simple structure, automatic feature extraction, and high computational power, compared with other networks, which are closer to the simulation of neural network functions [12]. At present, most of the implementations and applications of Chinese speech recognition are through software simulation methods. li et al [13] used modeling and simulation of isolated word recognition based on speaker classification and HMM model to demonstrate the possibility of recognizing isolated word pronunciation of Chinese characters in Matlab environment. Lin et al [14] designed a speech recognition system based on maximum mutual information, which effectively improved the speech recognition rate. Seano'neill [15] proposed an algorithm for continuous speech recognition of nonspecific large vocabulary, which can recognize continuous Chinese pronunciation of non-specific people, and used software to build a speech recognition system. Artificial neural networks have become an effective method to achieve speech recognition. There are few examples of applying convolutional neural for Chinese large vocabulary isolated word speech recognition implementation in China, Jiang [16] conducted a large sample of 606 people's isolated word speech recognition based on MFCC using convolutional neural network in 2014, and the recognition rate was around $66.3 \%$. Ke [17] in 2015 also implemented Chinese isolated word speech recognition based on the speech spectrogram for a total of 210 samples from seven speakers, with recognition rates around $96 \%$. More foreign research has been conducted in this area, and Zong [18] authored a book on automatic speech recognition, Deep Learning Methods, which provides insights and theoretical foundations for a series of highly successful deep learning models for automatic speech recognition. Finding suitable speech features is the basis for achieving high level speech recognition, and the recognition method of speech features is the key to speech recognition.

This paper proposes a dynamic Bayesian network (DBN) based phonetic feature representation method for Chinese high-volume isolated words, and uses convolutional neural networks for recognition of speech spectrogram features. The method has high recognition of Chinese dialects, high sensitivity and fault tolerance for Chinese speech recognition, and realizes the organic integration of artificial intelligence field and Chinese language development.

# 2 Construction of DBN structure for Chinese dialect recognition 

### 2.1 Basic recognition principle based on chain classification

Dynamic Bayesian networks [19-21] consist of several pieces of static Bayesian networks strung together. Static Bayesian networks consist of a directed acyclic graph of vertices and directed edges. According to the principle of speech signal generation, the speech signal can be seen as two stochastic processes jointly generated. One of the stochastic processes represents the evolution of the articulatory state, which is unobservable and belongs to the hidden process; the other stochastic process is the observed speech signal, which is controlled by the computer technology with the development of the articulatory state of speech. To clearly represent the association between the two, a DBN network can be used, where each piece of the network consists of two nodes.

In Figure 1, in the first $t$ time slice: the upper node represents the state variable, denoted by $\vec{S}_{t}=\left[S_{t 1}, S_{t 2}, \cdots, S_{t N}\right]^{T}, t=1,2, \cdots, T, T$ is the total number of frames (slices) of the speech signal, and N is the number of states of the speech signal; the lower node represents the observation vector, which consists of the feature vector extracted from the speech after framing, let the $t$ th frame feature vector be $\vec{X}_{t}=\left[x_{t 1}, x_{t 2}, \cdots, X_{t D}\right]^{T}, t=1,2, \cdots, T, T$ is the total number of frames (slices), and $D$ is the dimension of the feature vector. The upper layer nodes determine the observation values of the lower layer nodes. Considering the phonetic association relationship, the lower layer nodes are generally influenced by the upper layer nodes within the same slice or the upper layer nodes within adjacent slices, which are indicated by directed arrows. Jumps exist between upper-level nodes, but the jumps are specified to occur within adjacent slices and only forward.
![img-0.jpeg](img-0.jpeg)

Figure 1. Structure of DBN fragments in Chinese dialect recognition
In order to represent the inter-influence relationship between states and observation variables, three parameters $(k, p, f)$ are introduced to describe them where the first parameter $k$ indicates that the upper-level nodes (state nodes) are influenced by the upper-level nodes in the $t-k, t-k-1, \cdots, t-1$ th time slice; $p$ and $f$ indicate that the lower-level nodes (observation nodes) in the $t$ th slice are influenced by the upper-level nodes in the $t-p, t-p-1, \cdots, t+f$ th time slice. The value of $(k, p, f)$ can be adjusted to change the network structure in the experiment, so that the effect of different network structures on the dialect recognition effect can be explored.

Let the structure and parameters of the DBN network for the N dialects obtained by training be noted as: $G^{\prime}=\left\{V^{\prime}, E^{\prime}\right\}, \theta^{\prime}=\left\{A^{\prime}, B^{\prime}, \lambda^{\prime}\right\}, t=1,2, \cdots, N$. The speech fragments of the dialects to be tested, after feature extraction, get the feature vector as: $O=\left\{\vec{o}_{1}, \vec{o}_{2}, \cdots, \vec{o}_{F}\right\}$, where $\mathrm{o} \rightarrow \mathrm{t}$ is the feature vector of the

$t$ th frame. The feature vector is firstly input into the $i$ th DBN model [22], and then the output probability is calculated as: $P_{i}(O)=\sum_{k} P\left(O, S^{(k)}, G^{i}, \theta^{i}\right)$, where $S^{(k)}=\left\{s_{1}^{k}, s_{2}^{k}, \cdots, s_{T}^{k}\right\}$ denotes the kth possible state sequence and $s_{i}^{k} \in S$ is the state value of the $t$ th frame of the kth state sequence. Finally, the DBN dialect model corresponding to the largest $P_{i}(O)$ is selected as the recognition result.

# 2.2 DBN-based inference algorithm 

Calculating the DBN network model output probabilities can be done using the joint tree algorithm proposed by Liu [23], which first simplifies the network into a tree and then calculates the probabilities based on the resulting tree. In the tree graph for any node $X_{i}$, the graph can be decomposed into three parts, namely: $e_{i}^{0}, e_{i}^{-}$and $e_{i}^{+}$. Where $e_{i}^{0}$ is the observed value of the current node $X_{i}, e_{i}^{-}$is the value of each node with $X_{i}$ as its parent, and $e_{i}^{+}$is the value of the node with $X_{i}$ as its child. Let $\operatorname{CON}\left(e_{i}^{0}\right)$ be all possible values of $e_{i}^{0}$. If it is the observation node, $\operatorname{CON}\left(e_{i}^{0}\right)$ contains only the observation values [24]. Note that:

$$
\begin{aligned}
P\left(e, X_{i}=j\right) & =P\left(e_{i}^{0}, e_{i}^{-}, e_{i}^{+}, X_{i}=j\right) \\
& =P\left(e_{i}^{+}, X_{i}=j\right) P\left(e_{i}^{0}, e_{i}^{-}, X_{i}=j, e_{i}^{+}\right) \\
& =P\left(e_{i}^{+}, X_{i}=j\right) P\left(e_{i}^{0} e_{i}^{-}, X_{i}=j\right)
\end{aligned}
$$

If $X_{i}=j$ is not in $e_{i}^{0}, P\left(e_{i}^{0} e_{i}^{-}, X_{i}=j\right)$ is equal to 0 . The following two variables are key in the derivation and they will be used to calculate each $X_{i}$.

$$
\begin{gathered}
\lambda_{j}^{i}=P\left(e_{i}^{-}, e_{i}^{0}, X_{i}=j\right) \\
\pi_{j}^{i}=P\left(e_{i}^{+}, X_{i}=j\right)
\end{gathered}
$$

As shown in Figure 2, each computed $X_{i}$ will be classified and obtained as an inference graph.
![img-1.jpeg](img-1.jpeg)

Figure 2. DBN inference tree diagram
The definitions of these two variables can be derived:

$$
P(O)=\sum_{j} \lambda_{j}^{i} \pi_{j}^{i}
$$

$$
P\left(X_{i}=j \mid O\right)=\lambda_{j}^{i} \pi_{j}^{i} / \sum_{j, i} \pi_{j}^{i}
$$

This allows the derivation of a network by computing $\lambda$ and $\pi$ to calculate the required joint probabilities and edge probabilities. Here $\lambda$ and $\pi$ are similar to $\alpha$ and $\beta$ of HMM. These two variables can be computed for the child node $\lambda$ by the following method.

If $X_{i}$ has no child nodes:

$$
\lambda_{j}^{i}=1
$$

If $X_{i}$ has child nodes:

$$
\lambda_{j}^{i}=\prod_{c \in \operatorname{Ch}\left(X_{i}\right)} \sum_{f} \lambda_{c}^{f} P\left(X_{c} \mid X_{i}=j\right)
$$

Here $C h\left(X_{i}\right)$ denotes the set of $X_{i}$ sub-nodes, and it can be seen that the $\lambda$ of the sub-nodes has to be calculated first.

The calculation about $\pi$ :
If $X_{i}$ has no parent node

$$
\pi_{j}^{i}=P\left(X_{i}=j\right)
$$

If $X_{i}$ has parent node

$$
\pi_{j}^{i}=\sum_{l} P\left(X_{i}=j \mid X_{p}=v\right) * \prod_{S \in \operatorname{ch}\left(X_{i}\right)} \sum_{f} \lambda_{j}^{v} P\left(X_{S}=f \mid X_{p}=l\right)
$$

# 2.3 Set chain identification principle and DBN algorithm for network parameter learning 

Parameter learning of Bayesian networks is to enable the network to better describe the mathematical distribution of feature variables. A general learning method for Bayesian networks is described in Liu et al [23-25]. In the paper, combining the dialect speech characteristics, the observation nodes are regarded as continuous nodes, and their conditional probability distributions are represented by Gaussian mixture distributions, the state nodes are regarded as discrete nodes, and the node dimension is taken as 32 , i.e., each state node is a 32 -dimensional vector. Because the current state has the greatest influence on the current observed speech frame, the weight of the current node is taken as 0.8 , and the weights of the two nodes before and after are set to 0.1 .

The log-likelihood of the network observation:

$$
L=\sum_{m} \log P\left(D_{m}\right)=\sum_{h} \log \sum_{h} P\left(H=h, D=D_{m}\right)
$$

Here $H$ denotes the hidden node, $O$ denotes the observed node, and $D_{m}$ is the observed value. The basic idea of the EM algorithm is to use Jensen's inequality for a concave function $f$ with:

$$
f\left(\sum_{j} \lambda_{j} \gamma_{j}\right) \geq \sum_{j} \lambda_{j} f\left(\gamma_{j}\right)
$$

Where $\sum_{j} \lambda_{j}=1$. That is, the average of $f$ is greater than the average of $f$. Since the log function is typically concave, it is transformed into according to Eq. (11).

$$
q\left(h \mid O_{\infty}\right)=P_{\theta}\left(h \mid O_{\infty}\right)
$$

Maximizing the lower bound, for what amounts to maximizing the expected log likelihood.

$$
Q\left(\theta^{\prime} \mid \theta\right)=\sum_{\infty} \sum_{h} P\left(h \mid O_{\infty}, \theta\right) \log P\left(h, O_{\infty} \mid \theta^{\prime}\right)
$$

Choosing a suitable $\theta$ such that $Q\left(\theta^{\prime} \mid \theta\right)>Q(\theta \mid \theta)$, then it is guaranteed to make $P\left(D \mid \theta^{\prime}\right)>P(D \mid \theta)$, that is, increasing the expected log likelihood is equivalent to increasing the actual likelihood. This is because Equation $q\left(h \mid O_{\infty}\right)=P_{\theta}\left(h \mid O_{\infty}\right)$ ensures that the lower bound already coincides with the arc of the actual likelihood, so increasing the lower bound is equivalent to increasing the actual likelihood.

# 3 Convolutional neural network-based speech recognition system 

### 3.1 Convolutional neural network construction

Convolutional neural network consists of two convolutional layers, two pooling layers, one fully connected layer and one Softmax regression layer, which can automatically extract and classify the features of speech spectrogram.

The 6-layer convolutional neural network model consists of a convolutional layer and a pooling layer consisting of multiple feature maps (two-dimensional planes).

1) The convolutional layer is the process of extracting some primary visual features by simulating simple cells with local receptive fields through local connections and weight sharing. The above-mentioned set of identical connection strengths is a feature extractor, which is represented as a convolutional kernel during the operation, and the convolutional kernel values are first randomly initialized and finally determined by the training network.
2) The pooling layer simulates complex cells, and the process of filtering and combining primary visual features into more advanced, abstract visual features is implemented in the network by sampling. The pooling layer proposed in this paper uses maximum sampling with a sampling size of $2 \times 2$, so the length and width of the output feature map are half of the input feature map, defining that the neurons in the pooling layer do not have learning functions.
3) To enhance the nonlinear mapping capability of the network while limiting the size of the network, the network is connected to a fully connected layer after the features are extracted in four feature extraction layers.
4) Since the features of the speech spectrogram are complex, a fixed uniform template is established for each Chinese character's speech as much as possible, and the speech sample size is large and the categories are relatively large, so the Softmax classifier with strong

nonlinear classification ability is used for the last layer of the network. The learning algorithm uses batch gradient descent method.

# 3.2 Formation of speech spectrogram 

The principle of speech spectrogram generation: Speech signal is a typical non-smooth signal, but its non-smoothness is generated by the physical motion process of the articulatory organ, the acoustic vibration of this process is relatively slow and can be assumed to be smooth for a short period of $10-30 \mathrm{~ms}$. Short-time Fourier analysis, also called time-dependent Fourier transform, is a method of steady-state analysis to deal with non-smooth signals under the assumption of short-time smoothness [26-29].

Let the discrete time domain sample signal be $x(n), n=0,1,2, \cdots, N-1$, where $n$ is the time domain sample point number and $N$ is the length of the signal. Then the signal is framed, and $x(n)$ is denoted as $X_{n}(m)$, where $n$ is the frame sequence number, $m$ is the time sequence number of frame synchronization, and $m=0,1,2, \cdots, N-1$, where $N$ is the frame length (the number of sampling points in a frame). The schematic diagram of the speech spectrum generation is shown in Figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 3. Schematic diagram of the speech spectrum generation principle
The short-time Fourier transform of signal $\{x(n)\}$ is.

$$
X_{n}\left(e^{j \omega}\right)=\sum_{m=-n}^{n} x(m) \bullet \omega(n-m) \bullet e^{-j \omega m}
$$

Where $\{\omega(n)\}$ is a window sequence, the discrete time domain Fourier transform (DTFT) of signal $x(n)$ is:

$$
X\left(n, e^{j \omega}\right)=\sum_{m=0}^{N-1} x_{n}(m) e^{-j \omega m}
$$

The discrete Fourier transform DFT is used to obtain

$$
X(n, k)=\sum_{m=0}^{N-1} x_{n}(m) e^{-j \frac{2 k(m)}{N}}
$$

Where $0 \leq k \leq N-1$, then $X(n, k)$ is the short-time amplitude spectrum estimate of $x(n)$, and the spectral energy density function (or power spectrum function) at time $m$ is

$$
P(n, k)=|X(n, k)|^{2}=(X(n, k)) \times(\operatorname{conj}(n, k))
$$

Using time $n$ as the horizontal coordinate and $k$ as the vertical coordinate, the two-dimensional image formed by representing the values of $P(n, k)$ as gray levels is the speech spectrum diagram. The dB representation of the speech spectrum map can be obtained by transforming $10 \lg P(n, k)$.

The pseudocolor mapping of $P(n, k)$ results in a pseudocolor speech spectrum with higher resolution and better visual effect. In order to get a better display effect, we can choose an appropriate base value Base, limit the value less than Base to this base level, and mapping the value greater than Base linearly to the normalized color value of $0 \sim 1$, then the mathematical representation of the color matrix value $L=\{l(n, k)\}$ is.

$$
\begin{gathered}
L(n, k)=\frac{B(n, k)-\text { Base }}{\max (B(n, k) \forall(n, k))-\text { Base }} \\
B(n, k)= \begin{cases}P(n, k), P(n, k) \geq \text { Base } \\
\text { Base, } P(n, k) \leq \text { Base }\end{cases}
\end{gathered}
$$

The setting of Base value should be based on actual experience, if there is no special requirement, the default value Base $=0$. The color spectrum and grayscale contrast factor are obtained.

The patterns in the speech spectrogram include horizontal bars, chaotic lines and vertical bars. The horizontal bars are dark black bands parallel to the time axis, which are the resonance peaks. The corresponding resonance peak frequencies and bandwidths can be determined from the corresponding frequencies and widths of the bars. The presence or absence of a horizontal bar in a speech diagram is an important indicator of whether or not a speech segment is a turbid tone. A vertical bar (also called a punch bar) is a narrow black bar that appears perpendicular to the time axis in the speech diagram. Each vertical bar corresponds to a fundamental tone, and the starting point of the bar corresponds to the starting point of the voice-gated pulse, and the distance between the bars indicates the fundamental period. The distance between the stripes indicates the fundamental period, and the denser the stripes, the higher the fundamental frequency.

# 4 Experiments and results analysis 

### 4.1 Corpus and feature extraction

The Chinese dialect database [30-32] is my HFY dialect speech database established by the subject class experts of Chinese dialects, which includes Mandarin, Min dialect, Cantonese dialect and Wu dialect. The speakers are mainly college students, but also include some middle-aged and elderly people. Each recording is generally 20 minutes to half an hour in length. The three dialects were cut into 60 short segments of $5 \mathrm{~s}, 10 \mathrm{~s}$, and 15 s each as test speech, and the training speech was recorded

for about 10 minutes. The speech signals were sampled at 11 KHz and quantized at 16 bit. The above three speech sets do not overlap with each other.

The dialect features used in this paper are mainly SDC features [33-34], which need to be preprocessed before extraction, and the parameters used for speech pre-processing and feature extraction are given in Table 1.

Table 1. Parameters used in the experiment


# 4.2 The effect of DBN structure complexity on recognition rate 

To investigate the effect of the complexity of the structure on the recognition results, different experiments were taken and conducted. The results of the experiments are shown in Figure 4.
![img-3.jpeg](img-3.jpeg)

Figure 4. Comparison of different structural complexity
Experiments on structural complexity can be seen when the change of k has almost no effect on the experimental results. The same complexity $(1,0,1),(1,1,0)$ and $(2,0,1),(2,1,0)$ when p is large have higher recognition rates, which may be due to the fact that the previous state of the speech signal has a greater influence on the follow-up. The recognition rate reaches its highest at $(2,1,1)$ as the complexity of the structure increases, and then decreases instead as the complexity of the structure becomes higher. It shows that the state change of the speech signal is more related to the state immediately before it and almost unrelated to the state further ahead.

Due to the large number of training samples, this paper adopts the batch stochastic gradient descent method which has a faster convergence rate in practice. In the training process for the convolutional neural network, the batch block size is chosen as 40 , the momentum is 0.9 , and the learning rate is constant at 0.12 . Each iteration iterates through all the batch blocks of the training set, and updates the network parameters once after iterating through a batch block. The convolutional neural network algorithm, template matching algorithm, hidden Markov model method, vector quantization algorithm and BP neural network algorithm are used to identify the samples in the pattern library under Matlab 2010a environment. The recognition performance of convolutional neural networks with different structures is also tested. In order to test the effectiveness of using the speech spectrogram to characterize speech features, the convolutional neural network method is directly

applied to the recognition of speech time domain waveforms. The results are shown in Tables 2 (featuring the speech spectrogram) and 3 (featuring the time-domain waveform).

Table 2. Speech recognition rate by changing the speech spectrogram features of fully connected layers


Table 3. Speech recognition rates for changing the time-domain waveform graph features of the fully connected layer


From Tables 2 and 3, it can be seen that increasing the number of neurons in the fully connected layer can speed up the training of the network and improve the correct recognition rate to a certain extent. Tables 4 (features are speech spectrograms) and 5 (features are time-domain waveforms) show the recognition effects of changing the number of neurons in only two convolutional layers.

Table 4. Speech recognition rate by varying the speech spectrogram features of 2 convolutional layers


Table 5. Speech recognition rates for changing the time-domain waveform map features of 2 convolutional layers


It can be seen that the best convolutional neural network model is 20-40-3000 for the speech samples in this paper, and 20-40-3500 for the time-domain waveform as the speech features. At the same time, it can be seen that the recognition result of using speech spectrogram features is significantly better than that of time-domain waveform features. Table 6 shows the comparison between the recognition rate of the convolutional neural network model and other algorithms, which confirms that the speech recognition method proposed in this paper has better recognition rate than other common speech recognition methods.

Table 6. Comparison of the convolutional neural network model with 20-40-3000 and other algorithms


# 5 Conclusion 

Currently, artificial intelligence technology provides Chinese language learning support and Chinese speech recognition services, which play a good effect in recognition and localization. With the development of deep learning technology, artificial neural network becomes an effective method to achieve speech recognition.

In this paper, we use dynamic Bayesian networks to recognize Chinese dialects, and compare the recognition rates of GMM and HMM for Chinese dialects, and find that the differences are not significant. The effect of the complexity of the DBN structure on the recognition rate is also investigated in the paper. A model library with 1605 commonly used Chinese characters, 920 isolated character pronunciations, and 3680 samples is formed by using a speech spectrogram to characterize speech features. A 6-layer convolutional neural network is constructed and applied to the speech recognition of the model library. The recognition effect of different network structures and the recognition effect of different algorithms are compared. The results show that the constructed convolutional neural network with $20-40-3500$ structure has the best recognition effect. The recognition rate of the test samples reached $97.87 \%$, and the recognition rate of all samples reached $99.32 \%$. The experiments show that the recognition rate is better when $(2,1,1)$. In the future, the main research direction will be how to learn the structure of dynamic Bayesian networks from data.
