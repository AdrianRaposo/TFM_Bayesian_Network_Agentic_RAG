# Information-Theoretic Limits on Compression of Semantic Information 

Jiancheng Tang, Qianqian Yang ${ }^{\dagger}$, Zhaoyang Zhang<br>College of information Science and Electronic Engineering, Zhejiang University, Hangzhou 310007, China<br>Email: \{jianchengtang,qianqianyang20 ${ }^{\dagger}$,ning_ming\}@zju.edu.cn


#### Abstract

As conventional communication systems based on classic information theory have closely approached the limits of Shannon channel capacity, semantic communication has been recognized as a key enabling technology for the further improvement of communication performance. However, it is still unsettled on how to represent semantic information and characterise the theoretical limits. In this paper, we consider a semantic source which consists of a set of correlated random variables whose joint probabilistic distribution can be described by a Bayesian network. Then we give the information-theoretic limit on the lossless compression of the semantic source and introduce a low complexity encoding method by exploiting the conditional independence. We further characterise the limits on lossy compression of the semantic source and the corresponding upper and lower bounds of the rate-distortion function. We also investigate the lossy compression of the semantic source with side information at both the encoder and decoder, and obtain the rate distortion function. We prove that the optimal code of the semantic source is the combination of the optimal codes of each conditional independent set given the side information. Index Terms-Semantic communication, rate distortion, semantic compression.


## I. INTRODUCTION

The classical information theory (CIT) established by Shannon in 1948 is the cornerstone of modern communication systems. Concentrating on the accurate symbol transmission while ignoring the semantic content of communications, Shannon defined the information entropy based on the probabilistic distribution of symbols to measure the size of information quantitatively [1], based on which the theoretical limits on source compression and channel capacity are characterised. With the development of digital communications over the past 70 years, existing communication techniques, such as polar code and multiple-input multiple-output (MIMO) systems, have pushed the current communication systems closely approaching the Shannon capacity [2] [3]. To further improve the communication efficiency in order to meet the ever-growing demands, semantic oriented communication has attracted a lot of research interest lately, and widely recognized as a promising approach to overcome the Shannon limits [4]-[7].

Different from the traditional communication approaches, semantic communication systems only transmit the semantic or task relevant information while remove the redundancy to

[^0]improve transmission efficiency [8]-[11]. Semantic oriented communication methods have been implemented based on deep learning techniques for the efficient transmission of image [12]-[16], text [17], [18], video [19], [20] and speech signals [21]-[23]. These methods have been shown to achieve higher transmission efficiency compared with conventional methods for the specific tasks they are designed for. Despite this success, the design of semantic communication system still lacks theoretical guidance.

The research on semantic information theory can date back to about the time when the classical information theory was proposed. In one of a few early works [24], [25], Carnap and Bar Hillel proposed to use propositional logic sentences to represent semantic information. The semantic information entropy is calculated based on logical probabilities [26], instead of statistical probability as in classical information theory. Bao et al. [27] further extended this theoretical work and derived the semantic channel capacity of discrete memoryless channel based on propositional logic probabilities. De Luca et al. [28], [29] denoted semantic information by fuzzy variable and introduced fuzzy entropy to measure the uncertainty of fuzzy variables. However, neither the propositional logic nor fuzzy variables are expressive enough to describe semantic information of the complex data in today's applications.

Recently, Liu et al. proposed a new source model, where they viewed its semantic information as an intrinsic part of the source that is not observable but can be inferred from the extrinsic state [30]. They characterised the defined the semantic rate-distortion function through classical indirect ratedistortion theory based on this source model. Similarly, Guo et al. also modeled the semantic information as the unobservable information in a source, and characterized the theoretic limits on the rate distortion problem with side information [31]. In [32], the authors argued that the design of semantic language that maps meaning to messages is essentially a joint source-channel coding problem and characterised the trade-off between the rate and a general distortion measure. These works have shed light on developing a generic theory of semantic communication. However, the inner structure of semantic information remains unexplored.

In this paper, we consider a semantic source as a set of correlated semantic elements whose joint distribution can be modeled by a Bayesian network (BN). We characterise the information-theoretic limits on the lossless compression and


[^0]:    *This work is partly supported by the SUTD-ZJU IDEA Grant (SUTD-ZJU (VP) 202102), and partly by the Fundamental Research Funds for the Central Universities under Grant 2021FZZX001-20.

![img-0.jpeg](img-0.jpeg)

Fig. 1. (a) The original image. (b) The BN model of semantic elements of the image.

![img-1.jpeg](img-1.jpeg)

Fig. 2. The BN-enabled semantic communication framework.

lossy compression of semantic sources and derive the lower and upper bounds on the rate-distortion function. We further study the lossy compression problem with side information at both sides and prove that the optimality of compressing each conditionally independent set of variables given the side information. We derive the conditional rate-distortion functions when semantic elements follow binary or Gaussian distributed.

The organization of the rest of the paper is as follows: we introduce the semantic source in Section II. In Section III, we discuss information-theoretic limits on the compression of semantic source. In section IV, we study the problem of lossy compression with two-sided state information. In Section V, we conclude the paper.

## II. SEMANTIC SOURCE MODEL AND SEMANTIC COMMUNICATION SYSTEM

In this paper, we assume that a semantic source consists of a set of correlated semantic elements whose joint probabilistic distribution is modeled by a BN. BN has been widely used in semantic analysis and understanding of various types of data [33]–[35]. For example, Luo *et al.* proposed a scene classification method of images in which the semantic features are represented by a set of correlated semantic elements [37]. An image and the BN model of its semantic elements are shown in Fig. 1(a) and Fig. 1(b), where each node in Fig. 1(b) represents a semantic element. The conditional dependence relations among the semantic elements are obtained by expert knowledge, and the conditional probability matrices (CPMs) of each node are obtained by using the frequency counting approach based on an image dataset. For example, the semantic features *sky* and *grass* are extracted by an object detection algorithm and used as evidences to determine the scene category. In particular, the image is detected as *outdoor* when the posterior probability of the root node is large than a predefined threshold. In addition to the image procession, BN has also widely applied to various tasks representing semantic relations in different type of data such as text [36] and videos [38]. The BN-enabled semantic communication framework is shown in Fig. 2, which consists of four phases: a) semantic extraction and representation, b) semantic compression, c) semantic transmission, and d) original data recovery. In this paper, we assume that the conventional information source has been converted into the semantic source by using modern deep learning techniques in semantic extraction and representation phase. Our focus is on the semantic compression phase, where we provide some information-theoretic limits for compressing the semantic source.

## III. SEMANTIC COMPRESSION FOR CORRELATED SEMANTIC ELEMENTS

In this section, we present the theoretical limits on lossless and lossy compression of semantic sources, i.e., a set of correlated semantic elements whose correlation are modeled by BNs. We consider a *m*-variables semantic source {*X*<sub>1</sub>, *X*<sub>2</sub>, ..., *X*<sub>*m*</sub>} whose joint probabilistic distribution is modeled by BN. We assume that the order of *m* variables is sorted according to their causal relations, i.e., a child node variable always follows its parent node variables.

**Theorem 1. (Lossless Compression of Semantic Sources)** Give a *m*-variables source {*X*<sub>1</sub>, *X*<sub>2</sub>, ..., *X*<sub>*m*</sub>} with entropy *H*(*X*<sub>1</sub>, *X*<sub>2</sub>, ..., *X*<sub>*m*</sub>). For any code rate *R* if *R* > *H*(*X*<sub>1</sub>, *X*<sub>2</sub>, ..., *X*<sub>*m*</sub>), there exists a lossless source code for this source.

*Proof.* The proof of Theorem 1 easily follows from the proof of Shannon's first theorem [1], which is omitted here.

**Remark 1.** By utilizing the conditional independence property of BN, the entropy of this source *H*(*X*<sub>1</sub>, *X*<sub>2</sub>, ..., *X*<sub>*m*</sub>) can be written as

$$
\begin{aligned}
H(X_1, X_2, \dots, X_m) &= \sum_{i=1}^{m} H(X_i | X_{i-1}, \dots, X_1) \\
&= \sum_{i=1}^{m} H(X_i | \text{Parent}(X_i)),
\end{aligned}
\tag{1}
$$

where *Parent*(*X*<sub>*i*</sub>) denotes all parent variables of *X*<sub>*i*</sub>. For an *m*-variables source, the rate of joint coding all the variables is

always less than that of separate compression of each variable. Because

$$
\begin{aligned}
& \sum_{i=1}^{m} H\left(X_{i}\right)-H\left(X_{1}, X_{2}, \ldots, X_{m}\right) \\
& =\sum_{i=2}^{m} I\left(X_{i} ; \operatorname{Parent}\left(X_{i}\right)\right) \\
& \geqslant 0
\end{aligned}
$$

Remark 2. If we directly compress samples generated by the source $\left\{X_{1}, X_{2}, \ldots, X_{m}\right\}$ with Huffman encoding, the time complexity is $\mathcal{O}\left(k^{m} \log k^{m}\right)$, where $k$ is the maximal number of states that each variable has. The computation overhead of sorting algorithm is infeasible when the $m$ is large. We can utilize the conditional relations between parents and child variables to significantly reduce the complexity of Huffman coding. specifically, we can iteratively sort and encode the samples starting from the root node. Then for each node, we utilize the conditional probability with regards to its parent nodes to sort and encode its samples. This avoids the time complexity increasing exponentially with the number of nodes. We assume the maximum number of parent variables among $\left\{X_{1}, X_{2}, \ldots, X_{m}\right\}$ is $L(L$ is usually much smaller than $m$ ). Then the number of samples required to be coded each time is limited by $m k^{L}$. In this way, we have the overall complexity reduced from $\mathcal{O}\left(k^{m} \log k^{m}\right)$ to $\mathcal{O}\left(m k^{L} \log k^{L}\right)$.

Theorem 2. (Lossy Compression of Semantic Sources) The rate-distortion function for an $m$-variables semantic source whose joint distribution can be modeled by a BN, and distortion $D_{1}, D_{2}, \ldots, D_{m}$ is given by

$$
\begin{aligned}
& R_{X_{1}, X_{2}, \ldots, X_{m}}\left(D_{1}, D_{2}, \ldots, D_{m}\right) \\
& =\min _{p\left(\hat{x}_{1}, \hat{x}_{2}, \ldots, \hat{x}_{m}\left(x_{1}, x_{2}, \ldots, x_{m}\right)\right.} I\left(X_{1}, X_{2}, \ldots, X_{m} ; \hat{X}_{1}, \hat{X}_{2}, \ldots, \hat{X}_{m}\right) \\
& \operatorname{Ed}\left(\hat{x}_{1}, x_{1}\right) \leqslant D_{1} \\
& \operatorname{Ed}\left(\hat{x}_{2}, x_{2}\right) \leqslant D_{2} \\
& \operatorname{Ed}\left(\hat{x}_{m}, \hat{x}_{m}\right) \leqslant D_{m}
\end{aligned}
$$

If $R>R_{X_{1}, X_{2}, \ldots, X_{m}}\left(D_{1}, D_{2}, \ldots, D_{m}\right)$, there exists a lossy source code for this $m$-variables source at rate $R$ for a distortion not exceeding $D_{1}, D_{2}, \ldots, D_{m}$.

Proof. This can be proved using a straightforward extension of Shannon's work [41].

Lemma 1. For an $m$-variables semantic source whose joint distribution can be modeled by a BN, the rate-distortion function $R_{X_{1}, X_{2}, \ldots, X_{m}}\left(D_{1}, D_{2}, \ldots, D_{m}\right)$ can be bounded by

$$
\begin{aligned}
\sum_{i=1}^{m} R_{X_{i}}\left(D_{i}\right) & \geqslant R_{X_{1}, X_{2}, \ldots, X_{m}}\left(D_{1}, D_{2}, \ldots, D_{m}\right) \\
& \geqslant \sum_{i=1}^{m} R_{X_{i} \mid \operatorname{Parent}\left(X_{i}\right)}\left(D_{i}\right)
\end{aligned}
$$

where $R_{X_{i} \mid \operatorname{Parent}\left(X_{i}\right)}\left(D_{i}\right)$ represents the conditional ratedistortion function characterized by

$$
\begin{aligned}
& R_{X_{i} \mid \operatorname{Parent}\left(X_{i}\right)}\left(D_{i}\right) \\
& =\min _{\substack{p\left(\hat{x}_{i} \mid x_{i}, \operatorname{Parent}\left(x_{i}\right)\right) \\
Ed\left(\hat{x}_{i}, x_{i}\right) \leqslant D_{i}}} I\left(X_{i} ; \hat{X}_{i} \mid \operatorname{Parent}\left(X_{i}\right)\right)
\end{aligned}
$$

where

$$
\begin{gathered}
E d\left(\hat{x}_{i}, x_{i}\right)=\sum_{x_{i}, \hat{x}_{i}, \operatorname{Parent}\left(x_{i}\right),}\left\{p\left(\hat{x}_{i} \mid x_{i}, \operatorname{Parent}\left(x_{i}\right)\right)\right. \\
\left.p\left(x_{i}, \operatorname{Parent}\left(x_{i}\right)\right) d\left(\hat{x}_{i}, x_{i}\right)\right\}
\end{gathered}
$$

Proof. The upper bound in (4) is a straightforward extension of the upper bound of Wyner and Ziv [42], the proof of which is omitted here. The rigorous proof of the lower bound will be provided in a longer version.

Remark 3. The upper bound in Lemma 1 indicates that the rate of reconstructing all the variables within the given fidelity is always less than that of separate reconstruction of each variable. The rate-distortion of $m$-variables may be infeasible to obtain when $m$ is large. The lower bound in (4) suggests that we can use the summation of conditional rate distortion to guide the design of lossy source coding instead.

## IV. Lossy Compression of Correlated Semantic Elements With Side Information

In semantic communications, the sender and receiver always have access to some background knowledge about the communication contents. This background knowledge can be used as side information to help the compression of intended messages. In this section, we study the compression of correlated semantic elements when side information exists at both the sender and receiver. We further evaluate the corresponding rate-distortion function when the semantic elements follow binary distribution and multi-dimensional Gaussian distribution respectively.

Theorem 3. (Compression With Side Information) Given the bounded distortion measure $\left(d_{1}: \mathcal{X}_{1} \times \overline{\mathcal{X}}_{1} \rightarrow \mathcal{R}^{+}, \ldots\right.$, $d_{m}: \mathcal{X}_{m} \times \overline{\mathcal{X}}_{m} \rightarrow \mathcal{R}^{+}$), where $\mathcal{R}^{+}$denotes the set of nonnegative real numbers. If some variable is observed and revealed to the encoder and decoder as side information, denoted by $Y$, the rate-distortion function for compressing the remaining variables $X_{1}, X_{2}, \ldots, X_{m}$ is given by

$$
\begin{aligned}
& R_{X_{1}, \ldots, X_{m} \mid Y}\left(D_{1}, \ldots, D_{m}\right) \\
& =\min _{\substack{p\left(\hat{x}_{1}, \ldots, \hat{x}_{m} \mid x_{1}, \ldots, \hat{x}_{m}, y\right) \\
Ed\left(\hat{x}_{1}, x_{1}\right) \leqslant D_{1}} I\left(X_{1}, \ldots, X_{m} ; \hat{X}_{1}, \ldots, \hat{X}_{m} \mid Y\right) . \\
& \operatorname{Ed}\left(\hat{x}_{m}, \hat{x}_{m}\right) \leqslant D_{m}}
\end{aligned}
$$

Proof: We first prove the achievability of Theorem 3 by showing that for any rate $R \geq R_{X_{1}, \ldots, X_{m} \mid Y}\left(D_{1}, \ldots, D_{m}\right)$, there exists a lossy source code with the rate $R$ and asymptotic distortion $\left(D_{1}, \ldots, D_{m}\right)$. Let $p\left(\hat{x}_{1}, \ldots, \hat{x}_{m} \mid x_{1}, \ldots, x_{m}, \mathrm{y}\right)$ be the conditional probability that achieves equality in (7) and satisfies the distortion requirements, i.e., $E d\left(\hat{x}_{1}, x_{1}\right) \leqslant D_{1}, \ldots$, $E d\left(\hat{x}_{m}, x_{m}\right) \leqslant D_{m}$.

Generation of codebook: Randomly generate a codebook $\mathcal{C}$ with the help of side information $Y$. The codebook $\mathcal{C}$ consists of $2^{n R}$ sequence triples $\left(\hat{x}_{1}, \ldots, \hat{x}_{m}\right)^{n}$ drawn i.i.d. according to $p\left(\hat{x}_{1}, \ldots, \hat{x}_{m} \mid y\right)$, where $p\left(\hat{x}_{1}, \ldots, \hat{x}_{m} \mid y\right)=$ $\sum_{x_{1}, \ldots, x_{m}} p\left(x_{1}, \ldots, x_{m} \mid y\right) p\left(\hat{x}_{1}, \ldots, \hat{x}_{m} \mid x_{1}, \ldots, x_{m}, y\right)$. These codewords are indexed by $w \in\left\{1,2, \ldots, 2^{n R}\right\}$. The codebook $\mathcal{C}$ is revealed to both the encoder and decoder.

Encoding and Decoding: Encode the observing $\left(x_{1}, \ldots, x_{m}, y\right)^{n}$ by $w$ if its indexing sequence $\left(\hat{x}_{1}, \ldots, \hat{x}_{m}\right)^{n}$ is distortion typical with $\left(x_{1}, \ldots, x_{m}, y\right)^{n}$, i.e., $\left(x_{1}, \ldots, x_{m}, y, \hat{x}_{1}, \ldots, \hat{x}_{m}\right)^{n} \in T_{\epsilon}^{n}$. If there is more then one such index $w$, choose the least. If there is no such index, let $w=1$. After obtaining the index $w$, the receiver chooses the codeword $\left(\hat{x}_{1}, \ldots, \hat{x}_{m}\right)^{n}$ indexed by $w$ to reproduce the sequence.

Calculation of distortion: For an arbitrary codebook $\mathcal{C}$ and any $\epsilon>0$, the sequences $\left(x_{1}, \ldots, x_{m}\right)^{n} \in\left(X_{1}, \ldots, X_{m}\right)^{n}$ can be divided into to two categories:

For one case. Sequences $\left(x_{1}, \ldots, x_{m}, y\right)^{n}$ that is distortion typical with a codeword $\left(\hat{x}_{1}, \ldots, \hat{x}_{m}\right)^{n}$ in the codebook $\mathcal{C}$, i.e., $d\left(\hat{x}_{1}, x_{1}\right)<D_{1}+\epsilon, \ldots, d\left(\hat{x}_{m}, x_{m}\right)<D_{m}+\epsilon$. Because the total occurrence probability of such sequence is less than 1 , the expected distortions contributed by these sequences are no more than $\left(D_{1}+\epsilon, \ldots, D_{m}+\epsilon\right)$.

For the second case. Sequences $\left(x_{1}, \ldots, x_{m}, y\right)^{n}$ that there is no codeword in the codebook $\mathcal{C}$ that is distortion typical with $\left(x_{1}, \ldots, x_{m}\right)^{n}$. The total occurrence probability of such sequences is denoted by $P_{e}$. Since the distortions for $\left(x_{1}, \ldots, x_{m}\right)^{n}$ can be bounded by $\left(d_{\max , 1}, \ldots, d_{\max , m}\right)$, the expected distortions contributed by these sequences are no more than $\left(P_{e} d_{\max , 1}, \ldots, P_{e} d_{\max , m}\right)$, where the bounded distortion measure $d_{\max }$ is defined by

$$
d_{\max , i} \stackrel{\text { def }}{=} \max _{x_{i} \in \hat{X}_{i}, \hat{x}_{i} \in \hat{X}_{i}} d\left(x_{1}, \hat{x}_{i}\right)<\infty
$$

Hence the total distortions can be bound as

$$
\begin{gathered}
E d\left(\hat{x}_{1}, x_{1}\right) \leqslant D_{1}+\epsilon+P_{e} d_{\max , 1} \\
\ldots \\
E d\left(\hat{x}_{m}, x_{m}\right) \leqslant D_{m}+\epsilon+P_{e} d_{\max , m}
\end{gathered}
$$

If $P_{e}$ is small enough, the expected distortions are closed to $\left(D_{1}, \ldots, D_{m}\right)$.

The bound of $P_{e}$ : The coding error probability can be bounded as

$$
\begin{aligned}
P_{e} & =\sum_{\left(x_{1}, \ldots, x_{m}, y\right)^{n}} p\left(\left(x_{1}, \ldots, x_{m}, y\right)^{n}\right) \\
& \cdot p\left\{\left(\left(x_{1}, \ldots, x_{m}, y\right)^{n},\left(\hat{X}_{1}, \ldots, \hat{X}_{m}\right)_{w}^{n}\right) \notin T_{\epsilon}^{n}, \forall w \in\left[1: 2^{n R}\right]\right\} \\
& \leqslant p\left\{\prod_{w=1}^{2^{n R}}\left(\left(x_{1}, \ldots, x_{m}, y\right)^{n},\left(\hat{X}_{1}, \ldots, \hat{X}_{m}\right)_{w}^{n}\right) \notin T_{\epsilon}^{n}\right\} \\
& =\left(1-p\left\{\left(\left(x_{1}, \ldots, x_{m}, y, \hat{X}_{1}, \ldots, \hat{X}_{m}\right)^{n} \in T_{\epsilon}^{n}\right)\right\}\right)^{2^{n R}} \\
& \leqslant\left(1-2^{-n\left[\left(\left(X_{1}, \ldots, X_{n} ; \hat{X}_{1}, \ldots, \hat{X}_{n} \mid Y\right)+\delta(\epsilon)\right]\right)^{2^{n R}}}\right.
\end{aligned}
$$

where (10a) is obtained by applying the joint typicality theorem in [39], (10b) follows from the fact that $p\left(\left(x_{1}, \ldots, x_{m}, y\right)^{n}\right)$ is at most 1 , and (10c) and (10d) are obtained though the property of joint typical sequence. We note that $(1-z)^{t} \leqslant e^{(-\ell z)}$ for $z \in[0,1]$ and $0 \leqslant t$, and (10) can be rewritten as

$$
P_{e} \leqslant \exp \left(2^{-n\left[R-I\left(X_{1}, \ldots, X_{n} ; \hat{X}_{1}, \ldots, \hat{X}_{n} \mid Y\right)-\delta(\epsilon)\right]}\right)
$$

where $\delta(\epsilon) \rightarrow 0$ when $n \rightarrow \infty$. We note that $P_{e}$ goes to zero with $n$ if $R>I\left(X_{1}, \ldots, X_{n} ; \hat{X}_{1}, \ldots, \hat{X}_{n} \mid Y\right)+\delta(\epsilon)$. This proves the rate-distortion pairs $\left(R, D_{1}, \ldots, D_{m}\right)$ is achievable if $R>R\left(D_{1}, \ldots, D_{m}\right)$.

We then prove the converse of Theorem 3 by showing that for any source code meeting the distortion requirements $\left(D_{1}, \ldots, D_{m}\right)$, then the rate $R$ of the code must satisfy $R \geq R_{X_{1}, \ldots, X_{m} \mid Y}\left(D_{1}, \ldots, D_{m}\right)$. We consider any $\left(n, 2^{n R}\right)$ code with an encoding function $f_{n}:\left(X_{1}, \ldots, \mathcal{X}_{m}, \mathcal{Y}\right)^{n} \rightarrow$ $\left\{1,2, \ldots, 2^{n R}\right\}$. Then we have

$$
\begin{aligned}
n R & \geqslant H\left(f_{n}\left(\left(X_{1}, \ldots, X_{m}, Y\right)^{n}\right)\right) \\
& \geqslant H\left(f_{n}\left(\left(X_{1}, \ldots, X_{m}, Y\right)^{n}\right) \mid Y^{n}\right) \\
& \geqslant H\left(f_{n}\left(\left(X_{1}, \ldots, X_{m}, Y\right)^{n}\right) \mid Y^{n}\right) \\
& -H\left(f_{n}\left(\left(X_{1}, \ldots, X_{m}, Y\right)^{n}\right) \mid\left(X_{1}, \ldots, X_{m}, Y\right)^{n}\right) \\
& \geqslant I\left(\left(X_{1}, \ldots, X_{m}\right)^{n} ;\left(\hat{X}_{1}, \ldots, \hat{X}_{m}\right)^{n} \mid Y^{n}\right) \\
& =I\left(\left(X_{1}, \ldots, X_{m}, Y\right)^{n} ;\left(\hat{X}_{1}, \ldots, \hat{X}_{m}\right)^{n}\right) \\
& -I\left(Y^{n} ;\left(\hat{X}_{1}, \ldots, \hat{X}_{m}\right)^{n}\right)
\end{aligned}
$$

where (12a) follows from the fact that the number of codewords is $2^{n R}$, (12b) is obtained by the fact that conditioning reduces entropy, (12c) is obtained by introducing a nonnegative term, (12d) follows from the property of data-processing, and (12e) follows from the property of conditional mutual information. By applying the chain rule of mutual information to (12e), we have

$$
\begin{aligned}
& n R \\
& \geqslant \sum_{i=1}^{n} I\left(X_{1, i}, \ldots, X_{m, i}, Y_{i} ;\left(\hat{X}_{1}, \ldots, \hat{X}_{m}\right)^{n} \mid X_{1}^{i-1}, \ldots, X_{m}^{i-1}, Y^{i-1}\right) \\
& -\sum_{i=1}^{n} I\left(Y_{i} ;\left(\hat{X}_{1}, \ldots, \hat{X}_{m}\right)^{n} \mid Y^{i-1}\right) \\
& =\sum_{i=1}^{n} H\left(X_{1, i}, \ldots, X_{m, i}, Y_{i} \mid X_{1}^{i-1}, \ldots, X_{m}^{i-1}, Y^{i-1}\right) \\
& -\sum_{i=1}^{n} H\left(X_{1, i}, \ldots, X_{m, i}, Y_{i} \mid\left(\hat{X}_{1}, \ldots, \hat{X}_{m}\right)^{n}, X_{1}^{i-1}, \ldots, X_{m}^{i-1}, Y^{i-1}\right) \\
& -\sum_{i=1}^{n} H\left(Y_{i} \mid Y^{i-1}\right)+\sum_{i=1}^{n} H\left(Y_{i} \mid\left(\hat{X}_{1}, \ldots, \hat{X}_{m}\right)^{n}, Y^{i-1}\right) \\
& =\sum_{i=1}^{n} H\left(X_{1, i}, \ldots, X_{m, i}, Y_{i}\right)-\sum_{i=1}^{n} H\left(Y_{i}\right) \\
& -\sum_{i=1}^{n} H\left(Y_{i} \mid\left(\hat{X}_{1}, \ldots, \hat{X}_{m}\right)^{n}\right)+\sum_{i=1}^{n} H\left(Y_{i} \mid\left(\hat{X}_{1}, \ldots, \hat{X}_{m}\right)^{n}\right) \\
& -\sum_{i=1}^{n} H\left(X_{1, i}, \ldots, X_{m, i} \mid Y_{i},\left(\hat{X}_{1}, \ldots, \hat{X}_{m}\right)^{n}\right) \\
& \geqslant \sum_{i=1}^{n} H\left(X_{1, i}, \ldots, X_{m, i} \mid Y_{i}\right) \\
& -\sum_{i=1}^{n} H\left(X_{1, i}, \ldots, X_{m, i} \mid \hat{X}_{1, i}, \ldots, \hat{X}_{m, i}, Y_{i}\right) \\
& =\sum_{i=1}^{n} I\left(X_{1, i}, \ldots, X_{m, i} ; \hat{X}_{1, i}, \ldots, \hat{X}_{m, i} \mid Y_{i}\right) \\
& \geqslant \sum_{i=1}^{n} R\left(E d_{1}\left(X_{1, i}, \hat{X}_{1, i}\right), \ldots, E d_{m}\left(X_{m, i}, \hat{X}_{m, i}\right)\right) \\
& \geqslant n R\left(E d_{1}\left(X_{1}^{n}, \hat{X}_{1}^{n}\right), \ldots, E d_{m}\left(X_{m, i}^{n}, \hat{X}_{m}^{n}\right)\right) \\
& \geqslant n R\left(D_{1}, \ldots, D_{m}\right)
\end{aligned}
$$

![img-2.jpeg](img-2.jpeg)

Fig. 3. Two examples on semantic sources.

where $X_{j}^{i-1}$ denotes the sequence $(X_{j,1}, \ldots, X_{j,i-1})$, (13b) follows from the definition of conditional mutual information. (13c) follows from the chain rule and the fact that the source is memoryless, i.e., $\left(X_{1,i}, \ldots, X_{m,i}, Y_{i}\right)$ and $\left(X_{1}^{i-1}, \ldots, X_{m}^{i-1}, Y^{i-1}\right)$ are independent. (13d) is obtained by the fact that conditioning reduces entropy. And (13e) follows from the definition of $R\left(D_{1}, \ldots, D_{m}\right)$. This proves the converse of Theorem 3.

Lemma 2. Given the known variables $Y$, if an $m$-variables source can be divided into several conditional independent subsets $\mathcal{V}_{1}, \ldots \mathcal{V}_{l}$ by the property of BN, then

$$
R_{\mathcal{V}_{1}, \ldots, \mathcal{V}_{1} \mid Y}\left(D_{1}, \ldots, D_{m}\right)=\sum_{i=1}^{l} R_{\mathcal{V}_{i} \mid Y}\left(D_{j}, j \in \mathcal{V}_{i}\right)
$$

where the term $R_{\mathcal{V}_{i} \mid Y}\left(D_{j, j \in \mathcal{V}_{i}}\right)$ is given by:

$$
R_{\mathcal{V}_{i} \mid Y}\left(D_{j, j \in \mathcal{V}_{i}}\right)=\min _{\substack{p\left(x_{i} \mid x_{i}, y\right): \\ E d_{j}\left(x_{j}, x_{j}\right) \leqslant D_{j}, j \in \mathcal{V}_{i}}} I\left(\mathcal{V}_{i} ; \hat{\mathcal{V}}_{i} \mid Y\right)
$$

Proof: The proof of Lemma 2 will be provided in a longer version.

Remark 4. Lemma 2 implies that if a set of semantic elements can be divided into several conditional independent subsets by using the property of BN with side information $Y$, compressing the source variable set jointly is the same as compressing these conditional independent subsets separately in terms of the distortions and rate. We note that the separate compression of conditional independent subsets can significantly reduce the complexity of coding.

Example 1. Consider two different sources as shown in Fig. 3. The characteristics of BN indicate that the variables $X_{1}$ and $X_{2}$ in both cases of Fig. 3 are conditional independent given $Y$. By Lemma 2, we have that if the variable $Y$ is revealed to the encoder and decoder as side information, then

$$
\begin{aligned}
R\left(D_{1}, D_{2}\right) & =\min _{\substack{p\left(\hat{x}_{1}, \hat{x}_{2} \mid x_{1}, x_{2}, t\right) \\
E d\left(\hat{x}_{1}, x_{1}\right) \leqslant D_{1}} \\
& =R_{X_{1} \mid Y}\left(D_{1}\right)+R_{X_{2} \mid Y}\left(D_{2}\right)
\end{aligned}
$$

Example 2. We first explore the rate-distortion function of a binary semantic source given side information with Hamming distortion measure. This semantic source consists of three semantic elements $\left(X_{1}, X_{2}, Y\right)$ whose probabilistic distribution can be modeled by a BN as shown in Fig. 3(a). The inter-variable dependence structures $\left(X_{1}, Y\right)$ and $\left(X_{2}, Y\right)$
are doubly symmetric binary distributed with parameters $p_{1}$ and $p_{2}$ respectively, where

$$
p\left(x_{1}, y\right)=\left[\begin{array}{cc}
\frac{1-p_{1}}{p_{1}} & \frac{p_{2}}{1-p_{1}} \\
\frac{p_{1}}{2} & \frac{1-p_{1}}{2}
\end{array}\right], p\left(x_{2}, y\right)=\left[\begin{array}{cc}
\frac{1-p_{2}}{p_{2}} & \frac{p_{2}}{2} \\
\frac{p_{2}}{2} & \frac{1-p_{2}}{2}
\end{array}\right]
$$

By summing the joint probability distribution over all values of $x_{1}$ and $x_{2}$, we can obtain the marginal distribution $p(y)$. The the conditional distributions $p\left(x_{1} \mid y\right)$ and $p\left(x_{2} \mid y\right)$ can be obtained through Bayesian criterion as

$$
p\left(x_{1} \mid y\right)=\left[\begin{array}{cc}
1-p_{1} & p_{1} \\
p_{1} & 1-p_{1}
\end{array}\right], p\left(x_{2} \mid y\right)=\left[\begin{array}{cc}
1-p_{2} & p_{2} \\
p_{2} & 1-p_{2}
\end{array}\right]
$$

By Lemma 2, we have $R\left(D_{1}, D_{2}\right)=R_{X_{1} \mid Y}\left(D_{1}\right)+$ $R_{X_{2} \mid Y}\left(D_{2}\right)$. Following the conditional rate-distortion function of binary sources in [40], it yields

$$
\begin{aligned}
R_{X_{1} \mid Y}\left(D_{1}\right) & =\left[h_{b}\left(p_{1}\right)-h_{b}\left(D_{1}\right)\right]_{0 \leqslant D_{1} \leqslant p_{1}} \\
R_{X_{2} \mid Y}\left(D_{2}\right) & =\left[h_{b}\left(p_{2}\right)-h_{b}\left(D_{2}\right)\right]_{0 \leqslant D_{2} \leqslant p_{2}}
\end{aligned}
$$

Thus,

$$
\begin{aligned}
R\left(D_{1}, D_{2}\right) & =\left[h_{b}\left(p_{1}\right)-h_{b}\left(D_{1}\right)\right]_{0 \leqslant D_{1} \leqslant p_{1}} \\
& +\left[h_{b}\left(p_{2}\right)-h_{b}\left(D_{2}\right)\right]_{0 \leqslant D_{2} \leqslant p_{2}}
\end{aligned}
$$

We then consider the conditional rate-distortion function of a Gaussian source whose probabilistic distribution can be modeled by a BN as shown in Fig. 3(a). We use the mean-squared-error distortion measure here. $p\left(x_{1}, y\right)$ is twodimensional Gaussian distribution with parameters $m_{X_{1}}, m_{Y}$, $\sigma_{X_{1}}, \sigma_{Y}, r_{1}$ as

$$
\begin{aligned}
p\left(x_{1}, y\right)= & \frac{1}{2 \pi \sigma_{X_{1}} \sigma_{Y} \sqrt{1-r_{1}^{2}}} \exp \left\{-\frac{1}{2 \sigma_{X_{1}}^{2} \sigma_{Y}^{2}\left(1-r_{1}^{2}\right)}\right\} \\
\cdot & \left\{\left(\frac{x_{1}-m_{X_{1}}}{\sigma_{X_{1}}}\right)^{2}+\left(\frac{y-m_{Y}}{\sigma_{Y}}\right)^{2}\right. \\
& \left.-2 r \frac{\left(x_{1}-m_{X_{1}}\right)\left(y-m_{Y}\right)}{\sigma_{X_{1}} \sigma_{Y}}\right\}
\end{aligned}
$$

The conditional distribution $p\left(x_{1} \mid y\right)$ is also Gaussian distribution as

$$
\begin{aligned}
p\left(x_{1} \mid y\right) & =\left(2 \pi \sigma_{X_{1}}^{2}\left(1-r_{1}^{2}\right)\right)^{-1 / 2} \exp \left\{-\left(2 \sigma_{X_{1}}^{2}\left(1-r^{2}\right)\right)^{-1}\right. \\
& \left.\cdot\left[x_{1}-m_{X_{1}}-r_{1} \frac{\sigma_{X_{1}}}{\sigma_{Y}}\left(y-m_{Y}\right)\right]^{2}\right\}
\end{aligned}
$$

Therefore, we can obtain the rate-distortion function $R_{X_{1} \mid Y}\left(D_{1}\right)$ according to Shannon's work [41]

$$
R_{X_{1} \mid Y}\left(D_{1}\right)=\left[\frac{1}{2} \log \frac{\sigma_{X_{1}}^{2}\left(1-r_{1}^{2}\right)}{D_{1}}\right]_{0 \leq D_{1} \leq \sigma_{X_{1}}^{2}\left(1-r_{1}^{2}\right)}
$$

Similarly, we assume $p\left(x_{2}, y\right)$ also follows two-dimensional Gaussian distribution with parameters $m_{X_{2}}, m_{Y}, \sigma_{X_{2}}, \sigma_{Y}, r_{2}$, and $R_{X_{2} \mid Y}\left(D_{2}\right)$ is given by

$$
R_{X_{2} \mid Y}\left(D_{2}\right)=\left[\frac{1}{2} \log \frac{\sigma_{X_{2}}^{2}\left(1-r_{2}^{2}\right)}{D_{1}}\right]_{0 \leq D_{2} \leq \sigma_{X_{2}}^{2}\left(1-r_{2}^{2}\right)}
$$

By Lemma 2, we can obtain $R\left(D_{1},D_{2}\right)$

$$
\begin{aligned}
R\left(D_{1}, D_{2}\right) & =\left[\frac{1}{2} \log \frac{\sigma_{X_{1}}^{2}\left(1-r_{1}^{2}\right)}{D_{1}}\right]_{0 \leq D_{1} \leq \sigma_{X_{1}}^{2}\left(1-r_{1}^{2}\right)} \\
& +\left[\frac{1}{2} \log \frac{\sigma_{X_{2}}^{2}\left(1-r_{2}^{2}\right)}{D_{1}}\right]_{0 \leq D_{2} \leq \sigma_{X_{2}}^{2}\left(1-r_{2}^{2}\right)}
\end{aligned}
$$

## V. CONCLUSION

In this paper, we investigated compression of a semantic source which consists a set of correlated semantic elements, the joint probabilistic distribution of which can be modeled by a BN. Then we derived the theoretical limits on lossless compression and lossy compression of this semantic source, as well as the lower and upper bounds on the rate-distortion function. We also investigated the lossy compression problem of the semantic source with side information at both the encoder and decoder. We further proved that the conditional rate distribution function is equivalent to the summation of conditional rate distribution function of each conditionally independent set of variables given the side information. We also derived the conditional rate-distortion functions when the semantic elements of source are binary distribution and multidimensional distribution, respectively.
