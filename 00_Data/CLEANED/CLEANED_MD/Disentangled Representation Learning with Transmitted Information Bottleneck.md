# Disentangled Representation Learning with Transmitted Information Bottleneck 

Zhuohang Dang, Minnan Luo*, Chengyou Jia, Guang Dai, Jihong Wang, Xiaojun Chang, and Jingdong Wang,


#### Abstract

Encoding only the task-related information from the raw data, i.e., disentangled representation learning, can greatly contribute to the robustness and generalizability of models. Although significant advances have been made by regularizing the information in representations with information theory, two major challenges remain: 1) the representation compression inevitably leads to performance drop; 2) the disentanglement constraints on representations are in complicated optimization. To these issues, we introduce Bayesian networks with transmitted information to formulate the interaction among input and representations during disentanglement. Building upon this framework, we propose DisTIB (Transmitted Information Bottleneck for Disentangled representation learning), a novel objective that navigates the balance between information compression and preservation. We employ variational inference to derive a tractable estimation for DisTIB. This estimation can be simply optimized via standard gradient descent with a reparameterization trick. Moreover, we theoretically prove that DisTIB can achieve optimal disentanglement, underscoring its superior efficacy. To solidify our claims, we conduct extensive experiments on various downstream tasks to demonstrate the appealing efficacy of DisTIB and validate our theoretical analyses.


Index Terms—disentangled representation learning, information bottleneck, mutual information

## I. INTRODUCTION

[^0]REPRESENTATION learning, a fundamental and significant topic within computer vision and artificial intelligence domains, aims to learn low-dimensional embeddings of raw data for easier exploitation [1]. It serves as the cornerstone of various downstream tasks, such as classification [2], [3], detection [4], [5] and generation [6], [7], etc. Within this realm, traditional supervised learning approaches guide the learning of representations by leveraging corresponding labels, ensuring the learned representations effectively capture label-related parts of the raw data. However, a growing body of literature [8]-[11] has highlighted that only supervised learning may introduce spurious correlations between representations and labels, e.g., background bias [12], thus greatly undermining the robustness and generalizability of representations.

With the help of information theory, recent works have made significant contributions to capturing only label-related information, i.e., disentangled representation learning. These methods assume the information in raw data can be decomposed into two complementary parts: label-related and sample-exclusive, respectively. The former maintains the discriminative information for classification (e.g., the digit content in MNIST [13]), while the latter encodes all remaining label-irrelevant information (e.g., the location, size and writing style in MNIST). These methods mainly have two routes: regularization-based [14]-[18] and disentanglementbased methods [19]-[23]. Regularization-based methods attempt to add heuristic regularizations to the objective function, e.g., information constraints [15], [17] and prior knowledge [18], [24], [25], etc. These regularizers aim to eliminate the redundant information as much as possible without performance loss, i.e., compression. However, searching the performancecompression tradeoff with trivial regularization inevitably decreases the performance [19]. Disentanglement-based methods propose novel training objectives [19], [20] or strategies [22], [23] to fully disentangle the label-related and sampleexclusive information into separate representations. In achieving this, these methods introduce separate variables to capture label-related and sample-exclusive information, together with disentanglement constraints to eliminate information overlap between these variables. Despite their efficacy on realistic datasets, these methods usually employ complex strategies to optimize the disentanglement constraints, such as adversarial training [23], two-step architecture [22] and objective factorization [26], etc. Consequently, they suffer from the unstable and inefficient optimization process [27].

To overcome the aforementioned limitations, we suggest exploring a novel information-theoretic objective to enhance the


[^0]:    "Copyright (c) 2024 IEEE. Personal use of this material is permitted. However, permission to use this material for any other purposes must be obtained from the IEEE by sending an email to pubs-permissions@ieee.org."
    *Corresponding author: Minnan Luo.

    This work is supported by the National Nature Science Foundation of China (No. 62272374, No. 62192781, No. 62250009, No. 62137002), Natural Science Foundation of Shaanxi Province (No. 2024JC-JCQN-62), Project of China Knowledge Center for Engineering Science and Technology, Project of Chinese academy of engineering "The Online and Offline Mixed Educational Service System for 'The Belt and Road' Training in MOOC China", and the K. C. Wong Education Foundation.

    Zhuohang Dang, Minnan Luo, Chengyou Jia and Jihong Wang are with the School of Computer Science and Technology, the Ministry of Education Key Laboratory of Intelligent Networks and Network Security, and the Shaanxi Province Key Laboratory of Big Data Knowledge Engineering, Xi'an Jiaotong University, Xi'an, Shaanxi 710049, China (e-mail: \{dangzhuohang,cp3jia,wang1946456505\}@stu.xjtu.edu.cn, minnhuo@xjtu.edu.cn).

    Guang Dai is with the SGIT AI Laboratory, Xi'an 710048, China, and also with the State Grid Shaanxi Electric Power Company Ltd., State Grid Corporation of China, Xi'an 710048, China (e-mail: guang.gdai@gmail.com). Xiaojun Chang is with the School of Information Science and Technology, University of Science and Technology of China, Hefei 230026, China, and also with the Department of Computer Vision, Mohamed bin Zayed University of Artificial Intelligence (MBZUAI), Abu Dhabi, United Arab Emirates (e-mail: cxj273@gmail.com).

    Jingdong Wang is with Baidu Inc, Beijing 100085, China (e-mail: wangjingdong@outlook.com).

effectiveness of disentangled representation learning. Specifically, we leverage two Bayesian networks to formulate the variable interactions in disentangled representation learning, aligning with the principles of information compression and preservation in information theory. Facilitated by these Bayesian networks, we formalize the transmission of information among variables, which can be optimized to ensure both the compactness and informativeness of the learned representations. Next, we delve into the balance between representation compactness and informativeness, culminating in the introduction of a novel objective based on the information bottleneck principle: Transmitted Information Bottleneck For Disentangled Representation Learning (DisTIB). We then derive a tractable variational approximation for DisTIB, which can be stably optimized. Moreover, we conduct an in-depth theoretical analysis of our DisTIB, in which we prove its convergence to optimal disentanglement and thus avoiding the notorious performance-compression trade-off encountered in prior methods. These theoretical results demonstrate the superiority of DisTIB in stability and efficacy. We empirically demonstrate the efficacy of DisTIB on various downstream tasks, including adversarial robustness, supervised disentangling and more challenging few-shot learning, etc.

Our contributions are as follows:

- By formulating the variable interactions with Bayesian networks and transmitted information, we propose a novel transmitted information bottleneck to disentangle the label-related and sample-exclusive information, whose objective can be stably optimized with standard variational estimation.
- We provide an in-depth theoretical analysis of our DisTIB, in which we prove that it can achieve representations with optimal disentanglement, thereby avoiding the notorious performance-compression trade-off.
- Extensive superior experiment results on adversarial robustness, supervised disentangling and few-shot learning, etc., reveal the effectiveness of DisTIB, and the validity of our theoretical analyses.
The rest of the paper unfolds as follows: Section II introduces related works, notably the disentangled representation learning and information bottleneck. Section III delves into the details of the proposed DisTIB, while Section IV focuses on its optimization. In Section V, we present the datasets, implementation details, and experimental results, including comparisons with state-of-the-art methods and ablation studies. Section VI concludes the paper and outlines avenues for future research.


## II. Related Work

## A. Disentangled Representation Learning

Disentangled representation learning [28]-[30] aims to recover the mutually independent factors from data. For example, $\beta$-VAE [31] learns the factorized representations by controlling the trade-off between the reconstruction and prediction. Hadad et al. [22] propose a two-step framework that extracts label-related and sample-exclusive information sequentially. Information theory is also introduced to regularize information in disentangled representations. InfoGAN [32]
facilitates disentangled representation learning by maximizing the mutual information between input and latent. SPEECHSPLIT [20] leverages three information bottlenecks on different encoders to disentangle speech components. IIAE [26] proposes a novel training objective that combines the conventional evidence lower bound and disentanglement regularizations to extract the domain shared and exclusive information. FactorVAE [33] and TCVAE [34] factorize the training objective of the traditional variational encoder to directly penalize the total correlation term for better disentanglement. Some work [17], [21], [35] introduce mutual information regularization to better maintain the label-related information. Nevertheless, these methods involve complicated optimization strategies, leading to unstable and inefficient optimization procedures. In contrast, our DisTIB can be stably optimized with variational inference, and is proved to exactly control the information amount in representations to ensure optimal disentanglement.

## B. Information Bottleneck

Information bottleneck [36], [37] is introduced to find effective, highly compact features, compressing the information from raw data while only maintaining the information on the label. This is achieved by searching the trade-off between two mutual information (MI) terms: 1) maximizing the MI between features and target, i.e., prediction; 2) minimizing the MI between features and raw data, i.e., compression. Recently, VIB [14] has employed variational inference to derive tractable estimations for the MI terms, making its optimization easier when applied to deep neural networks. Tishby [38] leverages the IB principle to quantify the MI between layers in DNN and gives an information theoretic limit of DNN under finite samples. Some works extend the idea of IB into various downstream tasks, including multiview learning [39], graph representation learning [40] and domain generalization [41], etc. In this paper, we introduce the novel Transmitted Information Bottleneck for Disentangled Representation Learning. Additionally, we provide in-depth theoretical proof of its disentanglement efficacy, confirming the robustness and generalizability of learned representations.

## III. Methodology

In this section, we begin by defining disentangled representation learning, followed by modeling variable interactions using Bayesian networks. We then formulate DisTIB and provide an in-depth theoretical insight.

## A. Transmitted Information Bottleneck

1) Problem Definition: Consider a set of paired data sampled from the joint distribution $(x, y) \sim p(x, y)$, where $x \in X$ is extracted from the observational data and $y \in Y$ is its corresponding label, respectively. Similar to [19], [42], we assume that the observational data $X$ exhibits sample-specific factors of variations while sharing some common factors of variations within a class. For example, samples in the MNIST dataset can share the same semantic content (i.e., digit), while having different styles (i.e., writing, position,

![img-0.jpeg](img-0.jpeg)

Fig. 1. Illustration of Bayesian networks for information compression and preservation. The white and gray nodes denote input and target disentangled variables, respectively. The arrow indicates the direction of information flow, *i.e.*, variable interactions, during the disentangled representation learning.

and size, *etc*.). Given this data, our goal of disentangled representation learning is to seek a pair of complementary structured representations: label-related information *A* that captures the discriminative characteristics of label *Y*, and the sample-exclusive information *Z* that encodes all label-irrelevant factors. Notably, our disentanglement is group-level, eschewing a focus on the specific semantics of each dimension since it requires enormous external knowledge.

*2) Variable Bayesian Networks:* In the framework of disentangled representation learning, it's pivotal to understand the mechanisms behind extracting and preserving representations from raw data *x*. To this end, we focus on two core principles of information theory: 1) information compression that guarantees the representation compactness, 2) information preservation for ensuring the representation informativeness to target variables. Similar to [43]–[45], in Figure 1, we leverage two Bayesian networks *G<sub>in</sub>* and *G<sub>out</sub>* to formulate the graphical model encoding these two structures, where vertices are annotated by names of random variables. Specifically, in the information compression stage, we aim to encode disentangled label-related information *A* and sample-exclusive information *Z* from the original input *X*. Subsequently, *G<sub>in</sub>* identifies variables *X* as root while {*A, Z*} as leaves, where edges denote the compression relation among variables. On the other hand, in the information preservation stage, we aim to ensure that the label-related information *A* captures the discriminative characteristics of the label *Y* (edge *A* → *Y*); the sample-exclusive information *Z* encodes all label-irrelevant factors. Furthermore, *A* and *Z* should be complementary, thereby collectively encoding all input information (edges *A* → *X* and *Z* → *X*). As a result, *G<sub>out</sub>* defines variables they should preserve information about as leaves, indicating the information preservation relation among variables. These two Bayesian networks offer a holistic perspective of the intricate balance between compressing and preserving information.

*3) Formulation:* The Bayesian network *G<sub>in</sub>* encodes the conditional independence among disentanglement variables, *e.g.*, *A* ⊥ *Z* | *X*. Let *pG<sub>in</sub>*(X, Y, A, Z) denote the joint distribution of variables encoding the dependencies implied in *G<sub>in</sub>*, the information variables shared about each other in compression stage can be formulated as:

$$I^{\mathcal{G}\_{in}}=D_{KL}[p^{\mathcal{G}\_{in}}(X, Y, A, Z) \|\boldsymbol{p}(X)\boldsymbol{p}(Y)\boldsymbol{p}(A)\boldsymbol{p}(Z)],\qquad(1)$$

where *D<sub>KL</sub>* refers to KL divergence and *I<sup>G<sub>in</sub></sup>* is the multivariate extension of conventional mutual information, namely multi-information [46]. As in [43], minimizing *I<sup>G<sub>in</sub></sup>* ensures that *A* and *Z* capture the information from *X* while maintaining their mutual disentanglement, corresponding to the desired information compression process. However, the information compression process primarily emphasizes representation compactness, while overlooking the informativeness of the representation, *i.e.*, *Do disentanglement variables capture the target information from original data?* To address this, we further employ *G<sub>out</sub>* that encodes the informativeness dependencies between disentanglement variables and observational data, *e.g.*, *X* ⊥ *Y* | *A*. Similarly, let *pG<sub>out</sub>*(X, Y, A, Z) denote the joint distribution of variables encoding the dependencies implied in *G<sub>out</sub>*. By formulating *I<sup>G<sub>out</sub></sup>*, we aim to maximize it for encouraging the representation informativeness. Finally, inspired by the IB principle, we aim to achieve the optimal disentanglement of representations by the following objective:

$$\min\_{A,Z} L\_{DisTIB} = -I^{\mathcal{G}\_{out}} + \beta I^{\mathcal{G}\_{in}}.\tag{2}$$

The hyperparameter *β* ∈ [0, 1] explores the trade-off between representation compactness and informativeness, akin to conventional IB [14]. We then quantify the multi-information in Equation (2) with the following Theorem 1.

**Theorem 1.** *Given Bayesian networks* *G over variables* *X* = {*X<sub>1</sub>*, · · · , *X<sub>n</sub>*}, *let* *Pa<sup>G</sup><sub>X<sub>i</sub></sub> denotes parents of* *X<sub>i</sub> in* *G, the joint distribution can be factorized as* *p(X)* = Π<sup>n</sup><sub>i=1</sub>*p(X<sub>i</sub>|Pa<sup>G</sup><sub>X<sub>i</sub></sub>), *thus the multi-information* *I<sup>G</sup><sub>i</sub> can be quantified by*

$$\mathcal{I}^{\mathcal{G}} = D_{KL}[p(X\_1, \dots, X\_n) \|p(X\_1) \dots p(X\_n)] = D_{KL} \left[ \Pi\_{i=1}^{n} p(X\_i | \mathbf{Pa}\_{X\_i}^{\mathcal{G}}) \|p(X\_1) \dots p(X\_n) \right] = \sum\_{i} I(X\_{i}; \mathbf{Pa}\_{X\_i}^{\mathcal{G}}), \tag{3}$$

*where* *I(X<sub>i</sub>; Pa<sup>G</sup><sub>X<sub>i</sub></sub>) is the transmitted information, an extension of mutual information that measures the information transmitted from multi-source* **Pa**<sup>G</sup><sub>X<sub>i</sub></sub> *to receiver* *X<sub>i</sub>*. *Proof.* Please see supplementary for detailed proof. ☐

Subsequently, according to Theorem 1 and the Bayesian networks *G<sub>in</sub>* and *G<sub>out</sub>* defined for information compression and preservation, DisTIB is reduced to an IB-based trade-off among the transmitted information [47], resulting in the formulation of *transmitted information bottleneck*, *i.e.*,

$$\min\_{A,Z} L\_{DisTIB} = -I^{\mathcal{G}\_{out}} + \beta I^{\mathcal{G}\_{in}} \quad (4)$$

$$= - \sum\_{X\_i \in \mathcal{G}\_{out}} I(X\_i; \mathbf{Pa}\_{X\_i}^{\mathcal{G}\_{out}}) + \beta \sum\_{X\_i \in \mathcal{G}\_{in}} I(X\_{i}; \mathbf{Pa}\_{X\_i}^{\mathcal{G}\_{in}}).$$

More specifically, by incorporating the graphical structures of $\mathcal{G}_{i n}$ and $\mathcal{G}_{o s t}$ from Figure 1 into Equation (4), we derive the empirical objective of DisTIB as:

$$
\begin{aligned}
\min _{A, Z} L_{D i s T I B}= & -\underbrace{[I(X ; A, Z)+\underbrace{I(A ; Y)}_{S u f f i c i e n c y}]}_{\text {Sufficiency }} \\
& +\beta \underbrace{[I(X ; A)+I(X ; Z)+I(X ; Y)]}_{\text {Compression }}
\end{aligned}
$$

where the compression term indicates the learning process of the disentangled variables, i.e., the model encodes the information of $X$ into $A, Z$ and $Y$, respectively. Moreover, maximizing the sufficiency term $I(X ; A, Z)$ encourages the disentangled representation pair $(A, Z)$ to contain all information about $X$, i.e., $(A, Z)$ can restore $X$ losslessly. For the prediction term, maximizing $I(A ; Y)$ encourages $A$ to preserve information in $X$ about $Y$, i.e., label-related information, as much as possible.

In this paper, we analyze the scenario where the relationship between $Y$ and observational data $X$ is deterministic [48], i.e., there exists a surjective, injective, or bijective function $f$ such that $f(X)=Y$. This assumption is prevalent, covering a wide range of downstream applications. For example, the input maintains definitive class labels and locations in classification and detection tasks, or the output image contains desired input label conditions in controllable image generation, showcasing a deterministic input-label relationship. In this sense, $I(X ; Y)=H(Y)$ is an ignorable constant in optimization, where $H(Y)$ is the entropy of $Y$ specified by the dataset. This constraint, $I(X ; Y)=H(Y)$, offers foundations for analyzing DisTIB's disentanglement efficacy in Theorem 2.

## B. Theoretical Analyses

In this section, we conduct an in-depth theoretical analysis to validate the disentanglement effectiveness of DisTIB in the following three aspects: completeness, mutual disentanglement and minimal sufficiency of $A$.

Theorem 2. Given data $X$ with label $Y$, let $A$ and $Z$ represent the label-related and sample-exclusive information, respectively. Let $A^{*}$ and $Z^{*}$ signify the optimal label-related and sample-exclusive information obtained by minimizing $L_{D i s T I B}$, where $L_{D i s T I B}^{*}$ is the global minimum of $L_{D i s T I B}$. Then for any given $\epsilon>0$, there exists a $\delta>0$ such that $L_{D i s T I B}-L_{D i s T I B}^{*}<\delta$ and we have:

- completeness: The optimal label-related representation $A^{*}$ and sample-exclusive representation $Z^{*}$ are sufficient for data $X$, i.e., $\left|H(X)-I\left(X ; A^{*}, Z^{*}\right)\right|<\epsilon$.
- mutual disentanglement: The optimal label-related representation $A^{*}$ and sample-exclusive representation $Z^{*}$ are disentangled, i.e., $\left|I\left(A^{*} ; Z^{*}\right)\right|<\epsilon$.
- minimal sufficiency of $A$ : Given $I(X ; A) \leq I(X ; Y)$, the optimal label-related representation $A^{*}$ is minimal sufficient, i.e., $\left|I\left(Y ; A^{*}\right)-H(Y)\right|+\left|I\left(X ; A^{*}|Y)\right|<\epsilon$.

Proof. Please see supplementary for detailed proof.
Theorem 2 reveals that the proposed DisTIB can achieve the optimal disentanglement between $A$ and $Z$. Specifically,
![img-1.jpeg](img-1.jpeg)

Fig. 2. Illustration of DisTIB's training procedure on MNIST dataset, where disentangled variables gradually converge to their optimal value. In detail, the solid lines represent the estimation of mutual information between representations. The blue dashed line represents entropy of labels, $H(Y)$, which is the optimal value for the disentangled representation mutual information $I(X ; A)$ and $I(A ; Y)$.
the completeness indicates that the disentangled representation pair $(A, Z)$ captures all input information of $X$, while the mutual disentanglement denotes that there is no overlap between $A$ and $Z$. On the other hand, the minimal sufficiency of $A$ indicates that $A$ captures all label-related information without extra sample-exclusive noise. Moreover, since $I(X ; Z)=$ $H(X)-H(X \mid Z)$ has no analytic solution, Theorem 2 does not impose any specific constraint on the information amount contained within $Z$. However, given Theorem 2, the aforementioned three constraints collaboratively lead $Z$ to capture sample-specific information without label-related noise, i.e., optimal disentanglement of $Z$. In the following, we delve deeper into the disentanglement efficacy of DisTIB for a more thorough understanding.

Compared to previous regularization-based methods [14], [17], [49], DisTIB can avoid the notorious performancecompression trade-off. Specifically, [19] proves that previous regularization techniques inevitably decrease performance as the compression level intensifies. Differently, Figure 2 demonstrates that as the DisTIB training process progresses, the disentangled variables gradually converge to their optimal values, further validating the theoretical analysis of DisTIB's disentanglement performance in Theorem 2. On the other hand, although previous disentanglement-based methods employ explicit disentanglement constraints, i.e., $I(A, Z)$, to directly disentangle features with apparent simplicity, they suffer from training instability and inefficiency due to their complex optimization strategies, e.g., adversarial training [19], objective factorization [26], separate optimization [50], etc. Conversely, DisTIB can be estimated with variational inference, resulting in a more stable and concise optimization process.

## IV. DISTIB OPTIMIZATION AND INFERENCE

In the previous section, we propose DisTIB to optimally disentangle label-related and sample-exclusive information. However, it is intractable to directly optimize Equation (5), since the transmitted information typically consists of integrals on high-dimensional space. Therefore, similar to the previous

Algorithm 1 Pseudo-code for disentangled representation extraction and sample generation with DisTIB.

```
# Encg.EncA: label-irrelevant and -related encoder
# Gs: generators based on disentangled features (A,S)
def inference(input,label): # input:(N,C); label:(N,1)
    # extract disentangled features
    A = EncA.forward(input)# N*dim_A
    S = Encg.forward(input)# N*dim_S
    # generations on different (A,S) combination
    # dimension expansion: (N*N)*dim_A, (N*N)*dim_S
    A_1 = A.repeat(N,1)
    S_1 = S.repeat_interleave(N,0)
    gen = Gs.forward(A_1, S_1)# (N*N)*C
    # determined by A, with shape (N*N)*1
    gen_label = label.repeat(N,1)
    # label-related information, generations, labels
    return A,(gen,gen_label)
```

work [14], we employ variational inference to derive tractable bounds for these terms. The derivation details are shown in supplementary due to the page limits.

## A. Compression Term

To minimize $I(X ; Z)$, we approximate the marginal distribution $p(Z)$ with the parameterized distribution $r(Z)$. In this sense, the variational upper bound for $I(X ; Z)$ is formulated as:

$$
\begin{aligned}
I(X ; Z) & \leq \int p(X, Z) \log \frac{p(Z \mid X)}{r(Z)} d x d z \\
& =\mathbb{E}_{P(X)}\left[D_{K L}(p(Z \mid X) \| r(Z))\right]
\end{aligned}
$$

Similarly, $I(X ; A)$ can be estimated by using variational distribution $r(A)$ (see supplementary materials for details).

## B. Sufficiency Term

For the maximization of $I(X ; A, Z)$, we leverage the parameterized posterior distribution $q_{\phi}(X \mid A, Z)$ to approximate the true posterior distribution $p(X \mid A, Z)$, where $\phi$ are the distribution parameters. The tractable lower bound of $I(X ; A, Z)$ can be derived as

$$
\begin{aligned}
& I(X ; A, Z)=\int p(X, A, Z) \log \frac{p(X \mid A, Z)}{p(X)} d a d x d z \\
& \geq \int p(X, A, Z) \log q_{\phi}(X \mid A, Z) d a d x d z+H(X)
\end{aligned}
$$

where $H(X)$ is an ignorable constant. Moreover, this estimation allows us to implement the sufficiency term as a generator based on disentangled representations $(A, Z)$, enabling DisTIB with end-to-end disentangled generation ability.

## C. Prediction Term

Let the variational distribution $q_{\gamma}(Y \mid A)$ with parameters $\gamma$ be a variational approximation of true posterior distribution $p(Y \mid A)$. The corresponding tractable lower bound of $I(A ; Y)$ is formulated as

$$
\begin{aligned}
I(A ; Y) & =\int p(A, Y) \log \frac{p(Y \mid A)}{p(Y)} d a d y \\
& \geq \int p(A, Y) \log q_{\gamma}(Y \mid A) d a d y+H(Y)
\end{aligned}
$$

The estimations above give a tractable bound for minimizing DisTIB on the basis of standard mini-batch gradient descent with the reparameterization trick, demonstrating the stability of DisTIB's optimization.

## D. Model Inference

Algorithm 1 shows the pseudo-code of DisTIB's inference process, where $N$ is the batchsize; $C_{1}$ and $C_{2}$ are feature dimensions of label-related and sample-exclusive representation. The usage of inference output is task-dependent, e.g., $A$ for disentangled representation learning, while (gen, gen_label) for disentangled sample generation.

## V. EXPERIMENTS

In this section, we conduct extensive experimental studies to evaluate our DisTIB. We first introduce our experimental settings and then discuss the results of the experiments. Specifically, we aim to answer the following questions:

- RQ1: Can our DisTIB achieve superior performance on tasks inherently reliant on the informativeness and compactness of representations [54], [55], such as adversarial robustness, generalization, supervised disentangling and few-shot learning?
- RQ2: Whether the proposed DisTIB achieves the optimal disentanglement?
- RQ3: How does each component of DisTIB facilitate the disentanglement?


## A. Implementation Details

Similar to [14], [19], [49], in DisTIB, all encoders and decoders are implemented using the Deep Gaussian family with LeakyReLU as the activation function, where the dimension of the hidden layer to 4096. In the following, we give details of the corresponding modules.

1) We employ two stochastic encoders, $p(A \mid X)$ and $p(Z \mid X)$, to respectively capture label-relevant and sample-specific information from the input. Each encoder is formulated by the form $N\left(f_{\mu_{*}}(X), f_{\sigma_{*}^{2}}(X)\right)$ and $* \in\{A, Z\}$. Specifically, we employ distinct neural networks to predict the mean $f_{\mu_{*}}(X)$ and variance $f_{\sigma_{*}^{2}}(X)$ of corresponding features, where $f_{\mu_{*}}(X), f_{\sigma_{*}^{2}}(X)$ keeps identical architecture as threelayer fully-connected networks. Additionally, their input size aligns with the feature dimensions, while their output is specifically tailored to the respective sizes of label-related and sample-specific information.
2) The generator $q_{\phi}(X \mid A, Z)$ is designed to generate samples based on disentangled feature pairs $(A, Z)$. It has the form $N\left(f_{\mu_{\phi}}(A, Z), I\right)$ whose variance is fixed and mean is generated from a three-layer fullyconnected network $f_{\mu_{\phi}}(A, Z)$. The input dimensions are determined by the combined sizes of label-related and sample-specific information, whereas the output retains the original feature size.
3) The decoder $q_{\gamma}(Y \mid A)$ is of the form $q(A)=$ $\operatorname{softmax}(A W+b)$, which is a simple classification

TABLE I: GENERALIZATION AND ADVERSARIAL ROBUSTNESS PERFORMANCE (%) ON MNIST, FASHIONMNIST AND CIFAR10 DATASETS. FOR FAIR COMPARISONS, WE EMPLOY THE SAME MODEL ARCHITECTURE AND DIRECTLY REPORT THE CORRESPONDING RESULTS OF [19], WHERE THE HYPERPARAMETERS HAVE BEEN CAREFULLY TUNED FOR BEST EFFICACY.

Robustness | $\epsilon=0.1$ | 74.1 / 73.4 | 75.2 / 75.2 | 61.3 / 62.0 | 54.3 / 54.7 | 74.7 / 72.8 | 94.3 / 90.2 | 97.4 / 92.5 | 98.7 / 94.8  |
Robustness | $\epsilon=0.1$ | 26.3 / 29.0 | 26.7 / 28.7 | 28.0 / 29.4 | 22.4 / 23.5 | 25.4 / 27.6 | 59.6 / 62.0 | 53.4 / 58.7 | 62.5 / 65.1  |
Robustness | $\epsilon=0.1$ | 64.3 / 62.4 | 69.2 / 65.2 | 62.3 / 61.0 | 51.0 / 49.2 | 61.7 / 60.2 | 70.4 / 70.3 | 68.7 / 68.2 | 73.9 / 73.2  |

model to predicts the label $Y$ based on label-related information $A$. Furthermore, the mutual information objective $\mathcal{L}*{D i s T I B}$ is implemented as a combination of standard loss functions. Specifically, the compression term is expressed using the kl-divergence as described in Equation (6). Here, $r(A)$ and $r(Z)$ are treated as fixed spherical Gaussians, represented as $\mathcal{N}(0, I)$. The sufficiency term uses the reconstruction loss between input and $q_{\phi}(X \mid A, Z)$-generated samples, while the prediction term employs the CrossEntropy loss.

## B. Adversarial Robustness and Generalization

In this section, we elucidate how our DisTIB finds a pair of disentangled representations $(A, Z)$ to enhance model generalization. In our implementation, the representation $A$ solely encompasses the label-related information imperative for prediction, sidelining the remaining sample-specific details. Consequently, akin to [14], [19], we assess the model's generalization capability by evaluating the accuracy on the test set using the learned label-related representation $A$. Additionally, [54], [56] highlighted that deterministic models trained with maximum likelihood estimation are susceptible to adversarial samples, i.e., input with slight perturbations that retain the appearance of natural images but are deliberately designed to deceive the model. Building on this understanding, studies such as [57], [58] emphasized the potential benefits of limiting information in representations to bolster adversarial robustness. Aligned with this perspective, we further evaluate our model's adversarial robustness by focusing on the learned label-related representation $A$.

1) Datasets: Following previous works [14], [19], we assess DisTIB using established benchmarks for disentangled representation learning: MNIST, FashionMNIST, and CIFAR10. For MNIST and FashionMNIST, we adhere to the standard split, using 60000 samples for training and 10000 for testing. For CIFAR10, we employ a 50000/10000 split for train/test samples, respectively. 2) Experiment Setting: In this section, we delineate the aforementioned evaluation metrics, i.e., generalization and adversarial robustness, crucial for understanding the efficacy of our DisTIB. Firstly, in line with [14], [19], we gauge generalization by computing the average accuracy on the test set after training on train set. Secondly, we employ the same attack method [54] as in [14], [19] for a fair comparison. This attack strategy synthesizes adversarial samples by taking a single gradient step, where the perturbation magnitude for each pixel is regulated by the hyperparameter $\epsilon$. After training the model, we begin with adversarial sample generation on both train and test sets. We then evaluate the model's adversarial robustness on generated adversarial samples by measuring the mean classification accuracy. 3) Results: Following [19], we evaluate DisTIB against prominent IB-based disentangled representation learning methods, including regularization-based methods [14], [48], [49], [51], [52] and disentanglement-based methods [19], [53]. Table I summarizes our experimental results on both generalization and adversarial robustness. In terms of generalization, the proposed DisTIB showcases superior generalization ability, outperforming previous state-of-the-art (SOTA) methods by around $1 \%$ on average. When evaluating adversarial robustness, our DisTIB consistently achieves the best performance under different perturbation magnitudes across all three datasets. Specifically, taking MNIST as an instance, our DisTIB delivers an impressive $94.8 \%$ accuracy under $\epsilon=0.1$, whereas other competitors fall short, with the closest competitor, DisGenIB, achieving an accuracy of $90.7 \%$. Additionally, although previous regularization based methods explore various mutual information constraints, e.g., combinational [51] or nonlinear [52], for information compression, they inevitably suffer from label-related information loss as the level of compression intensifies [19], i.e., the notorious performance-compression trade-off. As a result, such trade-

![img-2.jpeg](img-2.jpeg)

Fig. 3. Visualization of disentangled sample generation, where samples are generated by the label-related information *A* of the top row and sample-exclusive information *Z* of the leftmost column. The top row and leftmost column images come from the dataset and the diagonal images show reconstructions.

off leads to prediction performance degeneration and weakens their adversarial robustness [19]. In contrast, when comparing with disentanglement based methods, although DisenIB and DisGenIB demonstrate commendable results in adversarial robustness with elaborately designed disentanglement objectives, they still lag behind our DisTIB by more than 3% in classification accuracy. We attribute this performance disparity to the adversarial training in DisenIB and the objective factorization in DisGenIB, *i.e.*, complicated optimization, leading to suboptimal disentanglement and thus limiting the adversarial robustness performance. As a result, these empirical results underscore the appealing generalization and adversarial robustness of our DisTIB, thereby demonstrating its efficacy in disentangled representation learning.

### *C. Supervised Disentangling*

In addition to quantitative evaluations of DisTIB's disentanglement behavior, we further explore supervised disentangling to intuitively demonstrate independent feature manipulation, serving as qualitative benchmarks. Specifically, from a dataset with annotated labels, we first employ specific encoders to obtain disentangled representation pairs from the input. Subsequently, we employ the generator to synthesize samples based on these representations. This visualization provides an intuitive insight into both the label-related and sample-exclusive information captured by our DisTIB.

*1) Datasets:* Following [19], [23], we qualitatively evaluate DisTIB's disentanglement efficacy on widely used benchmark datasets: MNIST [13], Sprites [59] and dSprites [60].

- **MNIST:** This dataset is renowned for its grayscale images of handwritten digits, ranging from 0 to 9. In this dataset, the label-related information refers simply to the class of digit content, while the sample-specific information denotes the writing style.
- **Sprites:** This dataset is composed of 672 characters from 20 different animations. Each sprite image can be characterized by seven distinct attributes: body, gender, hair, armor, arm, greaves, and weapon. In our implementation, we use gender, hair, armor and greave as label-related information, while the remaining attribute as sample-exclusive information.
- **dSprites:** This dataset encompasses three fundamental 2D shapes: squares, circles, and hearts. These shapes are systematically varied across different rotations and positions within each image. For our study, the inherent 2D shape is treated as label-related information. In contrast, variations in rotation and position are considered as sample-exclusive information.

*2) Experiment Setting:* The goal of supervised disentangling is to show that our DisTIB can effectively disentangle the sample-exclusive information from the label-related information of the input and synthesize satisfactory analogies. Following previous works [19], [22], [23], [33], we adopt a qualitative evaluation approach using the "swapping" paradigm. Specifically, given an image pair (*I*<sub>1</sub>, *I*<sub>2</sub>), we leverage specific encoders *p*(*A*|*X*), *p*(*Z*|*X*) to extract disentangled representation pairs (*A*<sub>1</sub>, *Z*<sub>1</sub>) and (*A*<sub>2</sub>, *Z*<sub>2</sub>), respectively. Subsequently, we use generator *q*<sub>σ</sub> to synthesize samples conditioning on the label-related information extracted from one image and sample-exclusive information obtained from the other, resulting in combinations (*A*<sub>1</sub>, *Z*<sub>2</sub>) and (*A*<sub>2</sub>, *Z*<sub>1</sub>). Given this framework, the ideal "swapping" generation should seamlessly incorporate label-related and sample-exclusive information from corresponding original images.

*3) Results:* Figure 3 shows the samples generated in "swapping" setting across all three datasets. Overall, DisTIB generates faithful samples using various disentangled representation pairs (*A*, *Z*). Taking the dSprites as an example, a column-wise observation reveals that the label-related information (shape) from the topmost row, whether square, circle, or heart-shaped, is consistently retained from the original images. On the other hand, a row-wise perspective shows that the sample-specific information (location and rotation) from the leftmost column is seamlessly integrated into the synthesized samples. Significantly, although the label-related and sample-specific information originates from different samples, their integration is seamlessly achieved in the generated images. This attests to DisTIB's optimal disentanglement, ensuring no overlap or

TABLE II: COMPARISON WITH SOTA METHODS ON MINIIMAGENET AND TIEREDIMAGENET. RL AND SG DENOTE REPRESENTATION LEARNING AND SAMPLE GENERATION, RESPECTIVELY. THE TOP TWO RESULTS ARE SHOWN IN BOLD AND UNDERLINED.


(a) Hair $\rightarrow$ Bald. (b) Dark Skin $\rightarrow$ Pale Skin. (c) Unsmile $\rightarrow$ Smile. (d) Female $\rightarrow$ Male; No Beard $\rightarrow$ Mustache; Makeup $\rightarrow$ No Makeup.

Fig. 4. Illustration of applying our DisTIB to disentangle facial attributes. Each row displays the generation results of a specific facial attribute interpolation, where the leftmost/rightmost image has an attribute value of 0/1; intermediate images represent interpolated attributes with a step size of 0.1 . loss of either type of information. Additionally, experiments on the other two datasets show consistent trends: by retaining the label-related information from one image and imposing the sample-specific information from another, the synthesized images display a coherent blend of these attributes. These results highlight DisTIB's efficacy in disentangling labelrelated and sample-specific information.

## D. Facial Attribute Disentangling

We further apply DisTIB to the more challenging and realistic CelebA [80] dataset to qualitatively analyze its disentanglement performance in complex real-world data. Specifically, we focus on disentangling facial attributes in the CelebA dataset to enable controllable facial generation. The specific experimental details are as follows:

1) Implementation Details: We evaluate DisTIB on CelebA [80], a standard facial image benchmark containing 202,599 images of 10,177 identities. Each image is annotated with 40 binary attributes that describe facial features, such as smiling, wearing glasses, and hairstyle. Following previous work [81], we use attribute interpolation to generate new images for showcasing our DisTIB's disentanglement performance. Specifically, given a facial image, we select an attribute to modify and perform interpolation, gradually changing the attribute value with a step size of 0.1 while keeping others constant, resulting in 10 interpolated images. 2) Results: Figure 4 showcases the superior performance of DisTIB on the CelebA dataset by effectively disentangling different facial attributes to control the appearance of generated images, including transitions such as from having hair to being bald, from black hair to blonde hair, and from not wearing glasses to wearing glasses. Furthermore, as shown in Figure 4d, even in multi-attribute interpolation experiments, our images exhibit smooth and natural transitions of facial features while maintaining facial consistency. This highlights that the representations learned by DisTIB effectively capture attribute-related information while ensuring disentanglement among attributes. These results further demonstrate the efficacy of DisTIB when handling complex real-world data, highlighting its appealing applicability.

## E. Few-Shot Learning (FSL)

In this section, beyond traditional disentangled representation learning benchmarks, we further extend DisTIB to the more challenging downstream task of few-shot learning. Specifically, FSL focuses on mining label-related information

TABLE III: Fine-grained classification with few-shot setting results on the CUB dataset, where all results are obtained with ResNet-12 backbone.


From a limited number of labeled samples to match with the unlabeled samples for classification [82]. However, due to the data scarcity inherent in FSL, its performance often suffers from spurious correlations in the learned representations [35], [83]. To this issue, we aim to utilize DisTIB to disentangle label-related information from sample-specific information, thereby facilitating more effective knowledge transfer for FSL.

1. **Datasets**: We evaluate DisTIB on standard FSL benchmarks: miniImageNet [84] and tieredImageNet [85]. MiniImageNet and tieredImageNet comprise 100 classes with 600 (84×84) images each and 608 classes with about 1200 (84×84) images each, respectively. Following [84], miniImageNet is randomly divided into 64, 16, 20 classes for train, valid, and test, respectively. In contrast, tieredImageNet organizes its classes into 34 high-level categories with divisions of 20, 6, and 8 for train, valid, and test, respectively.

In the test stage, FSL tasks are given in the formulation of N-way K-shot, where N classes are sampled with K labeled samples per class, denoted as support set *S*. Meanwhile, a query set *Q* with sufficient samples is sampled from the same support categories for FSL evaluation. Finally, following previous work [55], [64], [67], we report results on 600 randomly sampled standard 5-way 1/5-shot FSL tasks in terms of mean accuracy and 95% confidence interval.

1. **Methods**: Inspired by prior works, we utilize the disentangled representations (*A, Z*) learned by DisTIB in the following manner:
2. Following [64], we train a classifier based on the label-related information *A* and corresponding labels, denoted as the representation learning (RL) method.
3. Inspired by FeLMi [68] and SVAE [71], we tap into DisTIB's capability for disentangled generation to synthesize both discriminative and diverse samples, thereby alleviating the data scarcity in FSL. Specifically, as in Algorithm 1, we combine various *A* and *Z* to synthesize additional samples, whose label is assigned by its corresponding label-related information *A*. Subsequently, as in ProtoNet, we average sample features within classes on both support and synthesized samples to derive the sample generation (SG) prototype. To further eliminate the bias in the prototype, the SG prototype undergoes rectification based on the strategy proposed in [86]. Query samples are then matched using the nearest neighbor classifier to the refined prototype.

![img-3.jpeg](img-3.jpeg)

Fig. 5. The performance-compression trade-off on MNIST, where DisTIB is represented as dots due to its convergence to optimal disentanglement.

1. **Results**: For a fair comparison, we report results of standard FSL competitors in Table II, excluding influences such as priors, enhanced backbones, high-resolution inputs, *etc*. Specifically, even though previous representation learning-based methods have explored various strategies, *e.g.*, self-supervised learning [64] and distribution calibration [77], to enhance the robustness of representations, they still suffer from the entanglement between label-related information and sample-exclusive information. In contrast, "DisTIB + RL" effectively disentangle label-related information with certifiable efficacy, thereby highlighting a 2% performance improvement on average. Furthermore, "DisTIB + SG" is able to synthesize numerous discriminative and diverse extra samples by further utilizing the sample-exclusive information. Notably, it surpasses previous data augmentation based methods [68], [71] by roughly 1%, underscoring the exceptional quality of samples synthesized by DisTIB's disentangled generation. As a result, by adapting DisTIB to few-shot learning, we validate its efficacy in disentangled representation learning and underscore the importance of such representations for downstream tasks.

### *F. Fine-Grained Classification*

In this section, to better showcase the efficacy of our DisTIB, we apply it to the challenging task of fine-grained classification, which involves samples from different classes with highly similar visual features and minimal inter-class differences. Therefore, this task requires representations to capture the subtle differences between categories while reducing feature redundancy and confusion. To address this issue, we employ DisTIB to encode only label-related information while discarding sample-specific information, thereby better handling the fine-grained inter-class differences.

1. **Implementation Details**: We evaluate DisTIB on standard fine-grained classification benchmark with few-shot setting: CUB [91]. Specifically, the CUB dataset consists of 11,788 images spanning 200 bird species. Following [90], we divided the dataset into 100 classes for training, 50 classes for validation, and the remaining 50 classes for testing. Moreover, following ProtoNet [55], we employ the first-order statics (mean) of label-related information *A* learned by our DisTIB as the class prototype, and the evaluation implementation and metrics follow the same protocols used in the FSL setting.

![img-4.jpeg](img-4.jpeg)

Fig. 6. MNIST experiments results of mutual information quantization and classification accuracy on disentangled representations, where the red line denotes the ideal objective. Note that I(X;Z) = H(X) − H(X|Z), where the second term in RHS has no analytical solution, thus we report H(X) as an upper bound of I(X;Z) in (c) and (d).

![img-5.jpeg](img-5.jpeg)

Fig. 7. The left/right part in (a) are Sprites synthesized by DisTIB without/with disentanglement. (b) and (c) are FSL sample generations of DisTIB without or with disentanglement. (d) is the visualization of prototype and query samples, where SG is prototype estimated by our sample generation.

2) **Results:** As summarized in Table III, our DisTIB showcases consistent performance superiority on the CUB dataset. Notably, the strong competitor VFD [90] simply extracts label-related features by averaging pooling the output of the feature extractor for subsequent disentanglement. In contrast, our DisTIB benefits from an elaborately designed disentanglement objective, which enables DisTIB to extract precise label-related information and effectively capture subtle inter-class differences. Thus, DisTIB improves performance by an average of 2%, highlighting the potential and necessity of representation disentanglement in fine-grained tasks.

### G. Discussion and Ablation Study

In this section, we first conduct experiments on the information plane to validate our theoretical analyses (**RQ2**). Subsequently, we ablate different components of DisTIB to elucidate how it facilitates disentanglement (**RQ3**).

1) **Behavior on Information Plane:** To study DisTIB and previous regularization-based competitors [14], [48], [49] in detail, we conduct experiments to explore their performance-compression tradeoff by tuning β. These results form a curve on the information plane shown in Figure 5, defined by the I(X;A) (x-axis, compression) and I(A;Y) (y-axis, performance). Although searching the above trade-off can help previous methods eliminate part of redundant information, their performance drops when further compressing the information to I(X;A) = H(Y), which fails to achieve optimal disentanglement. In contrast, DisTIB is robust to β and closest to the optimal disentanglement, indicating it can effectively disentangle the label-related information. These results qualitatively demonstrate the best performance-compression trade-off and disentanglement performance of DisTIB, and the validity of our theoretical analyses.

2) **Comparison With Explicit Disentanglement Methods:** To substantiate the efficacy of DisTIB's implicit disentanglement, we conduct experiments to quantitatively assess the information control capabilities of DisTIB as mentioned in Theorem 2. In detail, we conduct experiments on MNIST as follows: 1) classification tasks on disentangled features; 2) quantify the information in representations, i.e., I(X;A) and I(X;Z). We also report the results of previous explicit disentanglement methods [19], [22], [23], [53] for a fair comparison. Figure 6 shows that all methods perform well on classification tasks, i.e., good classification performance on A while nearly

![img-6.jpeg](img-6.jpeg)

Fig. 8. Per-batch average training time and GPU memory on MNIST.

Random guess on Z. Intuitively, this observation seemingly suggests that all approaches have acquired effective disentangled representations: label-related information exclusively contains aspects relevant to prediction (i.e., well-classified), whereas sample-specific information solely captures label-irrelevant elements (i.e., random guess).

However, when quantifying the information within the representations, it is evident that previous competitors struggle to regulate the information in their disentangled representations, leading to the leak of redundant input information into A. Notably, though DisenIB and DisGenIB have all theoretically proved their disentanglement efficacy, our DisTIB exhibits greater information control ability. We attribute the performance disparity to the complex optimization strategies introduced by explicit disentanglement of DisenIB (adversarial training) and DisGenIB (objective factorization), leading to sub-optimal solutions. In contrast, DisTIB with implicit disentanglement requires no complex optimization strategies and yields superior results: it not only precisely encodes label-related information but also captures more sample-exclusive information due to the sufficiency term.

### 3) Influence of Disentanglement:

We propose a novel objective in Equation (5), including the conventional prediction term to supervise the extraction of label-related information, and the sufficiency and compression (disentanglement) terms that serve as regularizers. We study the influence of these regularizers as follows.

#### a) Quantitative:

We conduct experiments on adversarial robustness and FSL. Table IV shows performance drops severely without both terms due to insufficient disentanglement. The performance greatly improves with the disentanglement term due to the better disentangled features. However, the performance gap still exists since only prediction and disentanglement terms cannot ensure optimal disentanglement. Moreover, DisTIB loses end-to-end sample generation ability without sufficiency term. The sufficiency term cannot contribute to the disentanglement, which even slightly undermines performance due to the additional optimization. The best results are achieved with both terms, demonstrating the efficacy of DisTIB in disentangling representations.

#### b) Qualitative:

We visualize prototypes and sample generation with/without disentanglement. Figures 7a and 7b show

![img-7.jpeg](img-7.jpeg)

Fig. 9. The performance-$\beta$ and compression-$\beta$ trade-off on MNIST test set, where plots represent mutual information estimation; our DisTIB is represented as dotted lines due to its convergence to optimal disentanglement.

that insufficient disentanglement seriously harms sample generation. In contrast, in Figure 7c, DisTIB can synthesize discriminative and diverse samples that lie coherently with the true labeled samples, effectively alleviating the data scarcity of FSL. Moreover, Figure 7d shows that prototypes generated by SG are more accurate than the conventional mean prototype, leading to more precise decision boundaries.

### 4) Model Complexity:

Given input data dimension $N_D$, disentangled representation dimensions $N_A$ and $N_Z$ (assume $N_A = N_Z$), and the label dimension $N_Y$. Note that for a conventional information bottleneck baseline VIB [14], its optimization involves $I(X; A) - I(A; Y)$ with variational estimations, resulting in a training time complexity of $O(N_A \times (N_D + N_Y))$. Moreover, our DisTIB has a training time complexity of $O(N_A \times (4N_D + N_Y))$, which only involves an increase in constant terms and thus maintains comparable training time complexity with VIB. Furthermore, Figure 8 reports per batch training time and GPU memory on MNIST of our DisTIB and previous competitors to verify our analyses. Specifically, baseline VIB [14] employs the simplest architecture and maintains the least time and memory cost. Differently, DisenIB [19] employs complex adversarial-based density estimation for disentanglement, significantly increasing model complexity [27]. Conversely, our DisTIB introduces an additional encoder to capture the sample-specific information and a generator for disentangled generation. Equation (5) shows the optimization objective is reduced to conventional multi-information constraints with two extra terms compared to baseline, leading to a slight increase in time and memory cost.

### 5) Hyperparameter Analyses:

To study the influence of hyperparameter $\beta$, we first conduct experiments on MNIST with varying $\beta$. In detail, we show the mutual information quantization with various values of $\beta$ in Figure 9. We can observe a similar tendency on $\beta$ with previous works [14], [19], i.e., searching the performance-compression tradeoff inevitably degrades the performance of methods with trivial regularization. In contrast, our DisTIB exhibits a stable performance robust to $\beta$, attributed to its theoretically proven convergence to optimal disentanglement. These results are consistent with Figure 6, showcasing DisTIB's superior information control capability and its resulting enhanced performance-compression tradeoff.

## VI. CONCLUSION AND DISCUSSION

In this paper, we propose a novel transmitted information bottleneck for disentangling label-related and sampleexclusive information, named DisTIB. In detail, using variable interaction Bayesian networks, we extend the information bottleneck principle with transmitted information to formulate DisTIB. Moreover, we provide an in-depth theoretical analysis of DisTIB's disentanglement efficacy. Experimental results reveal that DisTIB outperforms previous methods on various downstream tasks, confirming the validity of our theoretical analyses. We hope our DisTIB offers new insights for future works to further enhance the disentanglement efficacy.
Discussion and Future Work. We aim to highlight the critical role of data disentanglement in enhancing model generalizability, e.g., adversarial robustness, generalization and FSL. Our DisTIB demonstrates impressive empirical and theoretical disentanglement efficacy. More importantly, our DisTIB showcases full scalability as its core principle is input disentanglement independent of the dataset size. Moving forward, we will explore new strategies and DisTIB's disentanglement efficacy on large datasets to enhance data efficiency.
Limitations. Although DisTIB showcases impressive efficacy, it has several limitations. First, DisTIB implicitly assumes that every sample has correct labels for disentanglement, neglecting potential label noise in inputs and thus limiting its real-world applicability. Additionally, DisTIB relies on Bayesian networks to model variable interactions during training. However, in certain problems, the interactions between variables are complex and require expert knowledge to model accurately. We propose employing noise-robust strategies and causality mining methods to mitigate these issues.
