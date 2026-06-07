# Towards Bayesian Deep Learning: A Framework and Some Existing Methods 

Hao Wang, Dit-Yan Yeung Senior Member, IEEE


#### Abstract

While perception tasks such as visual object recognition and text understanding play an important role in human intelligence, subsequent tasks that involve inference, reasoning and planning require an even higher level of intelligence. The past few years have seen major advances in many perception tasks using deep learning models. For higher-level inference, however, probabilistic graphical models with their Bayesian nature are still more powerful and flexible. To achieve integrated intelligence that involves both perception and inference, it is naturally desirable to tightly integrate deep learning and Bayesian models within a principled probabilistic framework, which we call Bayesian deep learning. In this unified framework, the perception of text or images using deep learning can boost the performance of higher-level inference and in return, the feedback from the inference process is able to enhance the perception of text or images. This paper proposes a general framework for Bayesian deep learning and reviews its recent applications on recommender systems, topic models, and control. In this paper, we also discuss the relationship and differences between Bayesian deep learning and other related topics such as the Bayesian treatment of neural networks.


Index Terms-Artificial Intelligence, Data Mining, Bayesian Networks, Neural Networks, Deep Learning, Machine Learning

## 1 INTRODUCTION

Deep learning has achieved significant success in many perception tasks including seeing (visual object recognition), reading (text understanding), and hearing (speech recognition). These are undoubtedly fundamental tasks for a functioning comprehensive artificial intelligence (AI) or data engineering (DE) system. However, in order to build a real AI/DE system, simply being able to see, read, and hear is far from enough. It should, above all, possess the ability to think.

Take medical diagnosis as an example. Besides seeing visible symptoms (or medical images from CT) and hearing descriptions from patients, a doctor has to look for relations among all the symptoms and preferably infer the corresponding etiology. Only after that can the doctor provide medical advice for the patients. In this example, although the abilities of seeing and hearing allow the doctor to acquire information from the patients, it is the thinking part that defines a doctor. Specifically, the ability to think here could involve causal inference, logic deduction, and dealing with uncertainty, which is apparently beyond the capability of conventional deep learning methods. Fortunately, another type of models, probabilistic graphical models (PGM), excels at causal inference and dealing with uncertainty. The problem is that PGM is not as good as deep learning models at perception tasks. To address the problem, it is, therefore, a natural choice to tightly integrate deep learning and PGM within a principled probabilistic framework, which we call Bayesian deep learning (BDL) in this paper.

[^0]With the tight and principled integration in BDL, perception tasks and inference tasks are regarded as a whole and can benefit from each other. In the example above, being able to see the medical image could help with the doctor's diagnosis and inference. On the other hand, diagnosis and inference can in return help with understanding the medical image. Suppose a doctor is not sure what a dark spot in a medical image is. However, if she is able to infer the etiology of the symptoms and disease, it can help her better decide whether the dark spot is a tumor or not.

As another example, to achieve high accuracy in recommender systems (RS) [1], [39], [40], [50], [67], we need to fully understand the content of the items (e.g., documents and movies) [46], analyze the profile and preferences of users [70], [73], and evaluate the similarity among the users [3], [11], [29]. Deep learning is good at the first subtask while PGM excels at the other two. Besides the fact that better understanding of item content would help with the analysis of user profiles, the estimated similarity among users could also provide valuable information for understanding item content in return. In order to fully utilize this bidirectional effect to boost recommendation accuracy, we might wish to unify deep learning and PGM in one single principled probabilistic framework, as seen in [67].

Besides recommender systems, the need for BDL may also arise when we are dealing with the control of non-linear dynamic systems with raw images as input. Consider controlling a complex dynamical system according to the live video stream received from a camera. This problem can be transformed into iteratively performing two tasks, perception from raw images and control based on dynamic models. The perception task can be taken care of using multiple layers of simple nonlinear transformation (deep learning) while the control task usually needs more sophisticated models like hidden Markov models and Kalman filters [22]. The feedback loop is then completed


[^0]:    - Hao Wang is with the Department of Computer Science and Engineering, the Hong Kong University of Science and Technology. E-mail: hwang@cse.ust.hk
    - Dit-Yan Yeung is with the Department of Computer Science and Engineering, the Hong Kong University of Science and Technology. E-mail: dyyeung@cse.ust.hk

by the fact that actions chosen by the control model can affect the received video stream in return. To enable an effective iterative process between the perception task and the control task, we need two-way information exchange between them. The perception component would be the basis on which the control component estimates its states and the control component with a built-in dynamic model would be able to predict the future trajectory (images). In such cases, BDL is a suitable choice [69].

As mentioned in the examples above, BDL is particularly useful for tasks that involve both understanding of content (e.g., text, images, and videos) and inference/reasoning among variables. In such complex tasks, the perception component of BDL is responsible for the understanding of the content, and the task-specific component (e.g., the control component in dynamical systems) models the probabilistic relationship among different variables. Furthermore, the interaction between these two components creates synergy and further boosts the performance.

Apart from the major advantage of BDL providing a principled way of unifying deep learning and PGM, another benefit comes from the implicit regularization built into BDL. Through imposing a prior on hidden units, parameters defining a neural network, or the model parameters specifying the causal inference, to some degree BDL can avoid overfitting, especially when there is not sufficient data. Usually, a BDL model consists of two components: (1) a perception component that is a Bayesian formulation of a certain type of neural networks and (2) a task-specific component that describes the relationship among different hidden or observed variables using PGM. Regularization is crucial for them both. Neural networks usually have large numbers of free parameters that need to be regularized properly. Regularization techniques such as weight decay and dropout [57] are shown to be effective in improving performance of neural networks and they both have Bayesian interpretations [15]. In terms of the task-specific component, expert knowledge or prior information, as a kind of regularization, can be incorporated into the model through the prior we imposed to guide the model when data are scarce.

Yet another advantage of using BDL for complex tasks (tasks that need both perception and inference) is that it provides a principled Bayesian approach of handling parameter uncertainty. When BDL is applied to complex tasks, there are three kinds of parameter uncertainties that need to be taken into account:

1) Uncertainty about the neural network parameters.
2) Uncertainty about the task-specific parameters.
3) Uncertainty about the exchange of information between the perception component and the task-specific component.
Through representing the unknown parameters using distributions instead of point estimates, BDL offers a promising framework to handle these three kinds of uncertainty in a unified way. It is worth noting that the third uncertainty could only be handled under a unified framework such as BDL. If we train the perception component and the task-specific component separately, it is equivalent to assuming no uncertainty when exchanging information between the two components.

Of course, there are challenges when applying BDL to real-world tasks. (1) First, it is nontrivial to design an efficient Bayesian formulation of neural networks with reasonable time complexity. This line of work has been pioneered by [25], [41], [44], but it has not been widely adopted due to its lack of scalability. Fortunately, some recent advances in this direction [2], [9], [23], [34], [66] seem to shed light on the practical adoption of Bayesian neural networks ${ }^{1}$. (2) The second challenge is to ensure efficient and effective information exchange between the perception component and the task-specific component. Ideally both the first-order and second-order information (e.g., the mean and the variance) should be able to flow back and forth between the two components. A natural way is to represent the perception component as a PGM and seamlessly connect it to the task-specific PGM, as done in [17], [64], [67].

In this paper, we aim to give a comprehensive overview of BDL models for applications like recommender systems, topic models (and representation learning), and control. The rest of the paper is organized as follows: In Section 2, we provide a review of some basic deep learning models. Section 3 covers the main concepts and techniques for PGM. These two sections serve as the background for BDL, and the next section, Section 4, proposes a unified BDL framework and surveys the BDL models applied to areas such as recommender systems and topic models. Section 5 discusses some future research issues and concludes the paper.

## 2 DEEP LEARNING

Deep learning normally refers to neural networks with more than two layers. To better understand deep learning, here we start with the simplest type of neural networks, multilayer perceptrons (MLP), as an example to show how conventional deep learning works. After that, we will review several other types of deep learning models based on MLP.

### 2.1 Multilayer Perceptron

Essentially a multilayer perceptron is a sequence of parametric nonlinear transformations. Suppose we want to train a multilayer perceptron to perform a regression task which maps a vector of $M$ dimensions to a vector of $D$ dimensions. We denote the input as a matrix $\mathbf{X}_{0}$ ( 0 means it is the 0 -th layer of the perceptron). The $j$-th row of $\mathbf{X}_{0}$, denoted as $\mathbf{X}_{0, j *}$, is an $M$-dimensional vector representing one data point. The target (the output we want to fit) is denoted as $\mathbf{Y}$. Similarly $\mathbf{Y}_{j *}$ denotes a $D$-dimensional row vector. The problem of learning an $L$-layer multilayer perceptron can be formulated as the following optimization problem:

$$
\begin{gathered}
\min _{\left\{\mathbf{W}_{l}\right\},\{b_{l}\}}\left\|\mathbf{X}_{L}-\mathbf{Y}\right\|_{F}+\lambda \sum_{l}\left\|\mathbf{W}_{l}\right\|_{F}^{2} \\
\text { subject to } \begin{aligned}
\mathbf{X}_{l} & =\sigma\left(\mathbf{X}_{l-1} \mathbf{W}_{l}+\mathbf{b}_{l}\right), l=1, \ldots, L-1 \\
\mathbf{X}_{L} & =\mathbf{X}_{L-1} \mathbf{W}_{L}+\mathbf{b}_{L}
\end{aligned}
\end{gathered}
$$

[^0]
[^0]:    1. Here we refer to Bayesian treatment of neural networks as Bayesian neural networks. The other term, Bayesian deep learning, is retained to refer to complex Bayesian models with both a perception component and a task-specific component.

![img-0.jpeg](img-0.jpeg)

Fig. 1. A 2-layer SDAE with L = 4.

where σ(·) is an element-wise sigmoid function for a matrix and σ(x) = 1/1 + exp(-x). λ is a regularization parameter and ||·||F denotes the Frobenius norm. The purpose of imposing σ(·) is to allow nonlinear transformation. Normally other transformations like tanh(x) and max(0, x) can be used as alternatives of the sigmoid function.

Here X<sup>l</sup> (l = 1, 2, ..., L − 1) is the hidden units. As we can see, X<sup>L</sup> can be easily computed once X<sub>0</sub>, W<sub>l</sub>, and b<sub>l</sub> are given. Since X<sub>0</sub> is given by the data, we only need to learn W<sub>l</sub> and b<sub>l</sub> here. Usually this is done using backpropagation and stochastic gradient descent (SGD). The key is to compute the gradients of the objective function with respect to W<sub>l</sub> and b<sub>l</sub>. If we denote the value of the objective function as E, we can compute the gradients using the chain rule as:

$$
\begin{aligned}
\frac{\partial E}{\partial \mathbf{X}_L} &= 2(\mathbf{X}_L - \mathbf{Y}) \\
\frac{\partial E}{\partial \mathbf{X}_l} &= (\frac{\partial E}{\partial \mathbf{X}_{l+1}} \circ \mathbf{X}_{l+1} \circ (1 - \mathbf{X}_{l+1})) \mathbf{W}_{l+1} \\
\frac{\partial E}{\partial \mathbf{W}_l} &= \mathbf{X}_l-1^T (\frac{\partial E}{\partial \mathbf{X}_l} \circ \mathbf{X}_l \circ (1 - \mathbf{X}_l)) \\
\frac{\partial E}{\partial \mathbf{b}_l} &= \text{mean}(\frac{\partial E}{\partial \mathbf{X}_l} \circ \mathbf{X}_l \circ (1 - \mathbf{X}_l), 1),
\end{aligned} \tag{3}
$$

where l = 1, ..., L and the regularization terms are omitted. The element-wise product is denoted as ∘ and mean(·, 1) is the Matlab operation on matrices. In practice, we only use a small part of the data (e.g., 128 data points) to compute the gradients for each update. This is called stochastic gradient descent.

As we can see, in conventional deep learning models, only W<sub>l</sub> and b<sub>l</sub> are free parameters, which we will update in each iteration of the optimization. X<sup>l</sup> is not a free parameter since it can be computed exactly if W<sub>l</sub> and b<sub>l</sub> are given.

### 2.2 Autoencoders

An autoencoder (AE) is a feedforward neural network to encode the input into a more compact representation and reconstruct the input with the learned representation. In its simplest form, an autoencoder is no more than a multilayer perceptron with a bottleneck layer (a layer with a small number of hidden units) in the middle. The idea of autoencoders has been around for decades [10], [20], [35] and abundant variants of autoencoders have been proposed to enhance representation learning including sparse AE [48], contractive AE [51], and denoising AE [59]. For more details, please refer to a nice recent book on deep learning [20]. Here we introduce a kind of multilayer denoising AE, known as stacked denoising autoencoders (SDAE), both as an example of AE variants and as background for its applications on BDL-based recommender systems in Section 4.

SDAE [59] is a feedforward neural network for learning representations (encoding) of the input data by learning to predict the clean input itself in the output, as shown in Figure 1. The hidden layer in the middle, i.e., X<sup>2</sup> in the figure, can be constrained to be a bottleneck to learn compact representations. The difference between traditional AE and SDAE is that the input layer X<sup>0</sup> is a corrupted version of the clean input data. Essentially an SDAE solves the following optimization problem:

$$
\begin{aligned}
\min_{\{\mathbf{W}_l\},\{\mathbf{b}_l\}} \|\mathbf{X}_c - \mathbf{X}_L\|_F^2 + \lambda \sum_{l} \|\mathbf{W}_l\|_F^2 \\
\text{subject to} \quad \mathbf{X}_l = \sigma(\mathbf{X}_{l-1} \mathbf{W}_l + \mathbf{b}_l), l = 1, \dots, L - 1 \\
\mathbf{X}_L = \mathbf{X}_{L-1} \mathbf{W}_L + \mathbf{b}_L,
\end{aligned}
$$

Here SDAE can be regarded as a multilayer perceptron for regression tasks described in the previous section. The input X<sup>0</sup> of the MLP is the corrupted version of the data and the target Y is the clean version of the data X<sub>c</sub>. For example, X<sub>c</sub> can be the raw data matrix, and we can randomly set 30% of the entries in X<sub>c</sub> to 0 and get X<sub>0</sub>. In a nutshell, SDAE learns a neural network that takes the noisy data as input and recovers the clean data in the last layer. This is what 'denoising' means. Normally, the output of the middle layer, i.e., X<sup>2</sup> in Figure 1, would be used to compactly represent the data.

### 2.3 Other Deep Learning Models

Other commonly used deep learning models include convolutional neural networks (CNN) [31], [36], which apply convolution operators and pooling operators to process image or video data, and recurrent neural networks (RNN) [20], [26], which use recurrent computation to imitate human memory, and restricted Boltzmann machines (RBM) [24], which are undirected probabilistic neural networks with binary hidden and visible layers. Note that there is a vast literature on deep learning and neural networks. The introduction in this section intends to serve only as the background of BDL. Readers are referred to [20] for a comprehensive survey and more details.

# 3 PROBABILISTIC GRAPHICAL MODELS

Probabilistic Graphical Models (PGM) use diagrammatic representations to describe random variables and relationships among them. Similar to a graph that contains nodes (vertices) and links (edges), PGM has nodes to represent random variables and links to express probabilistic relationships among them.

### 3.1 Models

As pointed out in [5], there are two main types of PGMs, directed PGMs (also known as Bayesian networks) and undirected PGMs (also known as Markov random fields), although there exist hybrid ones. In this paper we mainly focus on directed PGMs<sup>2</sup>. For details on undirected PGMs, readers are referred to [5].

<sup>2</sup> For convenience, PGM stands for directed PGM in this paper unless specified otherwise.

![img-1.jpeg](img-1.jpeg)

Fig. 2. The probabilistic graphical model for LDA, *J* is the number of documents and *D* is the number of words in a document.

A classic example of a PGM would be latent Dirichlet allocation (LDA), which is used as a topic model to analyze the generation of words and topics in documents. Usually PGM comes with a graphical representation of the model and a generative process to depict the story of how the random variables are generated step by step. Figure 2 shows the graphical model for LDA and the corresponding generative process is as follows:

- For each document *j* (*j* = 1, 2, ..., *J*),

  1) Draw topic proportions θ<sup>*j*</sup> ∼ Dirichlet(α). 2) For each word *w*<sub>*jn*</sub> of item (paper) **w**<sub>*j*</sub>,

  a) Draw topic assignment *z*<sub>*jn*</sub> ∼ Mult(θ<sub>*j*</sub>). b) Draw word *w*<sub>*jn*</sub> ∼ Mult(β<sub>*z*<sub>*jn*</sub></sub>). The generative process above gives the story of how the random variables are generated. In the graphical model in Figure 2, the shaded node denotes observed variables while the others are latent variables (θ and z) or parameters (α and β). As we can see, once the model is defined, learning algorithms can be applied to automatically learn the latent variables and parameters.

Due to its Bayesian nature, PGM like LDA is easy to extend to incorporate other information or to perform other tasks. For example, after LDA, different variants of topic models based on it have been proposed. The authors in [7], [61] proposed to incorporate temporal information and [6] extends LDA by assuming correlations among topics. To make it possible to process large datasets, [27] extends LDA from the batch mode to the online setting. On recommender systems, [60] extends LDA to incorporate rating information and make recommendations. This model is then further extended to incorporate social information [49], [62], [63].

### 3.2 Inference and Learning

Strictly speaking, the process of finding the parameters (e.g., α and β in Figure 2) is called learning and the process of finding the latent variables (e.g., θ and z in Figure 2) given the parameters is called inference. However, given only the observed variables (e.g., w in Figure 2), learning and inference are often intertwined. Usually, the learning and inference of LDA would alternate between the updates of latent variables (which correspond to inference) and the updates of the parameters (which correspond to learning). Once the learning and inference of LDA is completed, we would have the parameters α and β. If a new document arrives, we can now fix the learned α and β and then perform inference alone to find the topic proportions θ<sup>*j*</sup> of the new document.<sup>3</sup>

As in LDA, various learning and inference algorithms are available for each PGM. Among them, the most cost-effective one is probably maximum a posteriori (MAP), which amounts to maximizing the posterior probability of the latent variable. Using MAP, the learning process is equivalent to minimizing (or maximizing) an objective function with regularization. One famous example is the probabilistic matrix factorization (PMF) [53]. The learning of the graphical model in PMF is equivalent to the factorization of a large matrix into two low-rank matrices with L2 regularization.

MAP, as efficient as it is, gives us only *point estimates* of latent variables (and parameters). In order to take the uncertainty into account and harness the full power of Bayesian models, one would have to resort to Bayesian treatments such as variational inference and Markov chain Monte Carlo (MCMC). For example, the original LDA uses variational inference to approximate the true posterior with factorized variational distributions [8]. Learning of the latent variables and parameters then boils down to minimizing the KL-divergence between the variational distributions and the true posterior distributions. Besides variational inference, another choice for a Bayesian treatment is to use MCMC. For example, MCMC algorithms such as [47] have been proposed to learn the posterior distributions of LDA.

# 4 BAYESIAN DEEP LEARNING

With the background on deep learning and PGM, we are now ready to introduce the general framework and some concrete examples of BDL. Specifically, in this section we will list some recent BDL models with applications on recommender systems and topic models. A summary of these models is shown in Table 1.

### 4.1 General Framework

As mentioned in Section 1, BDL is a principled probabilistic framework with two seamlessly integrated components: a *perception component* and a *task-specific component*.

**PGM for BDL:** Figure 3 shows the PGM of a simple BDL model as an example. The part inside the red rectangle on the left represents the perception component and the part inside the blue rectangle on the right is the task-specific component. Typically, the perception component would be a probabilistic formulation of a deep learning model with multiple nonlinear processing layers represented as a chain structure in the PGM. While the nodes and edges in the perception component are relatively simple, those in the task-specific component often describe more complex distributions and relationships among variables (as in LDA).

**Three Sets of Variables:** There are three sets of variables in a BDL model: perception variables, hinge variables, and task variables: (1) In this paper, we use Ω<sup>*p*</sup> to denote the set of perception variables (e.g., A, B, and C in Figure 3), which are the variables in the perception component. Usually Ω<sup>*p*</sup> would include the weights and neurons in the probabilistic formulation of a deep learning model. (2) We use Ω<sup>*h*</sup> to

<sup>3</sup> For convenience, we use 'learning' to represent both 'learning and inference' in the following text.

TABLE 1
Summary of BDL Models. $\Omega_{h}$ is the set of hinge variables mentioned in Section 4.1. V and $\mathbf{U}$ are the item latent matrix and the user latent matrix (Section 4.2.1). $\mathbf{S}$ is the relational latent matrix (Section 4.3.1), and $\mathbf{X}$ is the content matrix (Section 4.3.2).


![img-2.jpeg](img-2.jpeg)

Fig. 3. The PGM for an example BDL. The red rectangle on the left indicates the perception component, and the blue rectangle on the right indicates the task-specific component. The hinge variable $\Omega_{h}=\{\mathbf{J}\}$.
denote the set of hinge variables (e.g. $\mathbf{J}$ in Figure 3). These variables directly interact with the perception component from the task-specific component. Table 1 shows the set of hinge variables $\Omega_{h}$ for each listed BDL models. (3) The set of task variables (e.g. $\mathbf{G}, \mathbf{I}$, and $\mathbf{H}$ in Figure 3), i.e., variables in the task-specific component without direct relation to the perception component, is denoted as $\Omega_{t}$.

The LLD. Requirement: Note that hinge variables are always in the task-specific component. Normally, the connections between hinge variables $\Omega_{h}$ and the perception component (e.g., $\mathbf{C} \rightarrow \mathbf{J}$ in Figure 3) should be i.i.d. for convenience of parallel computation in the perception component. For example, each row in $\mathbf{J}$ is related to only one corresponding row in $\mathbf{C}$. Although it is not mandatory in BDL models, meeting this requirement would significantly increase the efficiency of parallel computation in model training.

Joint Distribution Decomposition: If the edges between the two components point towards $\Omega_{h}$ (as shown in Figure 3, where $\left.\Omega_{p}=\{\mathbf{A}, \mathbf{B}, \mathbf{C}, \mathbf{D}, \mathbf{E}, \mathbf{F}\}, \Omega_{h}=\{J\}$, and $\Omega_{t}=\right.$ $\{\mathbf{I}, \mathbf{G}, \mathbf{H}\}$ ), the joint distribution of all variables can be written as:

$$
p\left(\boldsymbol{\Omega}_{p}, \boldsymbol{\Omega}_{h}, \boldsymbol{\Omega}_{t}\right)=p\left(\boldsymbol{\Omega}_{p}\right) p\left(\boldsymbol{\Omega}_{h} \mid \boldsymbol{\Omega}_{p}\right) p\left(\boldsymbol{\Omega}_{t} \mid \boldsymbol{\Omega}_{h}\right)
$$

If the edges between the two components originate from $\boldsymbol{\Omega}_{h}$ (similar to Figure 3 except that the edge points from $\mathbf{J}$ to C), the joint distribution of all variables can be written as:

$$
p\left(\boldsymbol{\Omega}_{p}, \boldsymbol{\Omega}_{h}, \boldsymbol{\Omega}_{t}\right)=p\left(\boldsymbol{\Omega}_{t}\right) p\left(\boldsymbol{\Omega}_{h} \mid \boldsymbol{\Omega}_{t}\right) p\left(\boldsymbol{\Omega}_{p} \mid \boldsymbol{\Omega}_{h}\right)
$$

Apparently, it is possible for BDL to have some edges between the two components pointing towards $\boldsymbol{\Omega}_{h}$ and some originating from $\boldsymbol{\Omega}_{h}$, in which case the decomposition of the joint distribution would be more complex.

Variance Related to $\boldsymbol{\Omega}_{h}$ : As mentioned in Section 1, one of the motivations for BDL is to model the uncertainty of exchanging information between the perception component and the task-specific component, which boils down to modeling the uncertainty related to $\boldsymbol{\Omega}_{h}$. For example, this kind of uncertainty is reflected in the variance of the conditional density $p\left(\boldsymbol{\Omega}_{h} \mid \boldsymbol{\Omega}_{p}\right)$ in Equation (5) ${ }^{4}$. According
4. For models with the joint likelihood decomposed as in Equation (6), the uncertainty is reflected in the variance of $p\left(\boldsymbol{\Omega}_{p} \mid \boldsymbol{\Omega}_{h}\right)$.
to the degree of flexibility, there are three types of variance for $\boldsymbol{\Omega}_{h}$ (for simplicity we assume the joint likelihood of BDL is Equation (5), $\boldsymbol{\Omega}_{p}=\{p\}, \boldsymbol{\Omega}_{h}=\{h\}$, and $p\left(\boldsymbol{\Omega}_{h} \mid \boldsymbol{\Omega}_{p}\right)=$ $\mathcal{N}(h \mid p, s)$ in our example):

- Zero-Variance: Zero-Variance (ZV) assumes no uncertainty during the information exchange between the two components. In the example, zero-variance means directly setting $s$ to 0 .
- Hyper-Variance: Hyper-Variance (HV) assumes that uncertainty during the information exchange is defined through hyperparameters. In the example, HV means that $s$ is a hyperparameter that is manually tuned.
- Learnable Variance: Learnable Variance (LV) uses learnable parameters to represent uncertainty during the information exchange. In the example, $s$ is the learnable parameter.

As shown above, we can see that in terms of model flexibility, LV $>$ HV $>$ ZV. Normally, if the models are properly regularized, an LV model would outperform an HV model, which is superior to a ZV model. In Table 1, we show the types of variance for $\boldsymbol{\Omega}_{h}$ in different BDL models. Note that although each model in the table has a specific type, one can always adjust the models to devise their counterparts of other types. For example, while CDL in the table is an HV model, we can easily adjust $p\left(\boldsymbol{\Omega}_{h} \mid \boldsymbol{\Omega}_{p}\right)$ in CDL to devise its ZV and LV counterparts. In [67], authors compare the performance of an HV CDL and a ZV CDL and finds that the former performs significantly better, meaning that sophisticatedly modeling uncertainty between two components is essential for performance.

Learning Algorithms: Due to the nature of BDL, practical learning algorithms need to meet these criteria:

1) They should be online algorithms in order to scale well for large datasets.
2) They should be efficient enough to scale linearly with the number of free parameters in the perception component.

Criterion (1) implies that conventional variational inference or MCMC methods are not applicable. Usually an online version of them is needed [28]. Most SGD-based methods do not work either unless only MAP inference (as opposed to Bayesian treatments) is performed. Criterion (2) is needed because there are typically a large number of free parameters in the perception component. This means methods based on Laplace approximation [41] are not realistic since they involve the computation of a Hessian matrix that scales quadratically with the number of free parameters.

### 4.2 Bayesian Deep Learning for Recommender Systems

Despite the successful applications of deep learning on natural language processing and computer vision, very few attempts have been made to develop deep learning models for CF. The authors in [54] use restricted Boltzmann machines instead of the conventional matrix factorization formulation to perform CF and [19] extends this work by incorporating user-user and item-item correlations. Although these methods involve both deep learning and CF, they actually belong to CF-based methods because they do not incorporate content information as in CTR [60], which is crucial for accurate recommendation. The authors in [52] use low-rank matrix factorization in the last weight layer of a deep network to significantly reduce the number of model parameters and speed up training, however it is for classification instead of recommendation tasks. On music recommendation, [45], [68] directly use conventional CNN or deep belief networks (DBN) to assist representation learning for content information, but the deep learning components of their models are deterministic without modeling the noise and hence they are less robust. The models achieve performance boost mainly by loosely coupled methods without exploiting the interaction between content information and ratings. Besides, the CNN is linked directly to the rating matrix, which means the models will perform poorly due to serious overfitting when the ratings are sparse.

### 4.2.1 Collaborative Deep Learning

To address the challenges above, a hierarchical Bayesian model called collaborative deep learning (CDL) as a novel tightly coupled method for RS is introduced in [67]. Based on a Bayesian formulation of SDAE, CDL tightly couples deep representation learning for the content information and collaborative filtering for the rating (feedback) matrix, allowing two-way interaction between the two. Experiments show that CDL significantly outperforms the state of the art.

In the following text, we will start with the introduction of the notation used during our presentation of CDL. After that we will review the design and learning of CDL.

Notation and Problem Formulation: Similar to the work in [60], the recommendation task considered in CDL takes implicit feedback [30] as the training and test data. The entire collection of $J$ items (articles or movies) is represented by a $J$-by- $B$ matrix $\mathbf{X}_{c}$, where row $j$ is the bag-of-words vector $\mathbf{X}_{c, j *}$ for item $j$ based on a vocabulary of size $B$. With $I$ users, we define an $I$-by- $J$ binary rating matrix $\mathbf{R}=\left[\mathbf{R}_{i j}\right]_{I \times J}$. For example, in the dataset citeulike-a [60], [62], [67] $\mathbf{R}_{i j}=1$ if user $i$ has article $j$ in his or her personal library and $\mathbf{R}_{i j}=0$ otherwise. Given part of the ratings in $\mathbf{R}$ and the content information $\mathbf{X}_{c}$, the problem is to predict the other ratings in $\mathbf{R}$. Note that although CDL in its current form focuses on movie recommendation (where plots of movies are considered as content information) and article recommendation like [60] in this section, it is general enough to handle other recommendation tasks (e.g., tag recommendation).

Matrix $\mathbf{X}_{c}$ plays the role of clean input to the SDAE while the noise-corrupted matrix, also a $J$-by- $B$ matrix, is
denoted by $\mathbf{X}_{0}$. The output of layer $l$ of the SDAE is denoted by $\mathbf{X}_{l}$ which is a $J$-by- $K_{l}$ matrix, where $K_{l}$ is the number of units in layer $l$. Similar to $\mathbf{X}_{c}$, row $j$ of $\mathbf{X}_{l}$ is denoted by $\mathbf{X}_{l, j *} . \mathbf{W}_{l}$ and $\mathbf{b}_{l}$ are the weight matrix and bias vector, respectively, of layer $l, \mathbf{W}_{l, * n}$ denotes column $n$ of $\mathbf{W}_{l}$, and $L$ is the number of layers. For convenience, we use $\mathbf{W}^{+}$to denote the collection of all layers of weight matrices and biases. Note that an $L / 2$-layer SDAE corresponds to an $L$-layer network.

Generalized Bayesian SDAE: Following the introduction of SDAE in Section 2.2, if we assume that both the clean input $\mathbf{X}_{c}$ and the corrupted input $\mathbf{X}_{0}$ are observed, similar to [4], [5], [12], [41], we can define the following generative process of generalized Bayesian SDAE:

1) For each layer $l$ of the SDAE network,
a) For each column $n$ of the weight matrix $\mathbf{W}_{l}$, draw

$$
\mathbf{W}_{l, * n} \sim \mathcal{N}\left(\mathbf{0}, \lambda_{w}^{-1} \mathbf{I}_{K_{l}}\right)
$$

b) Draw the bias vector $\mathbf{b}_{l} \sim \mathcal{N}\left(\mathbf{0}, \lambda_{w}^{-1} \mathbf{I}_{K_{l}}\right)$.
c) For each row $j$ of $\mathbf{X}_{l}$, draw

$$
\mathbf{X}_{l, j *} \sim \mathcal{N}\left(\sigma\left(\mathbf{X}_{l-1, j *} \mathbf{W}_{l}+\mathbf{b}_{l}\right), \lambda_{s}^{-1} \mathbf{I}_{K_{l}}\right)
$$

2) For each item $j$, draw a clean input ${ }^{5}$

$$
\mathbf{X}_{c, j *} \sim \mathcal{N}\left(\mathbf{X}_{L, j *}, \lambda_{n}^{-1} \mathbf{I}_{B}\right)
$$

Note that if $\lambda_{s}$ goes to infinity, the Gaussian distribution in Equation (7) will become a Dirac delta distribution [58] centered at $\sigma\left(\mathbf{X}_{l-1, j *} \mathbf{W}_{l}+\mathbf{b}_{l}\right)$, where $\sigma(\cdot)$ is the sigmoid function. The model will degenerate to be a Bayesian formulation of SDAE. That is why we call it generalized SDAE.

Note that the first $L / 2$ layers of the network act as an encoder and the last $L / 2$ layers act as a decoder. Maximization of the posterior probability is equivalent to minimization of the reconstruction error with weight decay taken into consideration.

Collaborative Deep Learning: Using the Bayesian SDAE as a component, the generative process of CDL is defined as follows:

1) Generate variables of generalized Bayesian SDAE.
2) For each item $j$,
a) Draw the latent item offset vector $\boldsymbol{\epsilon}_{j} \sim \mathcal{N}\left(\mathbf{0}, \lambda_{s}^{-1} \mathbf{I}_{K}\right)$ and then set the latent item vector: $\mathbf{v}_{j}=\boldsymbol{\epsilon}_{j}+\tilde{\mathbf{X}}_{\frac{L}{2}, j *}^{T}$.
3) Draw a latent user vector for each user $i$ :

$$
\mathbf{u}_{i} \sim \mathcal{N}\left(\mathbf{0}, \lambda_{u}^{-1} \mathbf{I}_{K}\right)
$$

4) Draw a rating $\mathbf{R}_{i j}$ for each user-item pair $(i, j)$ : $\mathbf{R}_{i j} \sim \mathcal{N}\left(\mathbf{u}_{i}^{T} \mathbf{v}_{j}, \mathbf{C}_{i j}^{-1}\right)$.
Here $\lambda_{w}, \lambda_{n}, \lambda_{u}, \lambda_{s}$, and $\lambda_{v}$ are hyperparameters and $\mathbf{C}_{i j}$ is a confidence parameter similar to that for CTR [60] $\left(\mathbf{C}_{i j}=a\right.$ if $\mathbf{R}_{i j}=1$ and $\mathbf{C}_{i j}=b$ otherwise). Note that the middle layer $\mathbf{X}_{L / 2}$ serves as a bridge between the ratings and content information. This middle layer, along with the latent offset $\boldsymbol{\epsilon}_{j}$, is the key that enables CDL to simultaneously learn an effective feature representation and capture the
[^0]
[^0]:    5. Note that while generation of the clean input $\mathbf{X}_{c}$ from $\mathbf{X}_{L}$ is part of the generative process of the Bayesian SDAE, generation of the noise-corrupted input $\mathbf{X}_{0}$ from $\mathbf{X}_{c}$ is an artificial noise injection process to help the SDAE learn a more robust feature representation.

![img-3.jpeg](img-3.jpeg)

Fig. 4. On the left is the graphical model of CDL. The part inside the dashed rectangle represents an SDAE. An example SDAE with L = 2 is shown. On the right is the graphical model of the degenerated CDL. The part inside the dashed rectangle represents the encoder of an SDAE. An example SDAE with L = 2 is shown on its right. Note that although L is still 2, the decoder of the SDAE vanishes. To prevent clutter, we omit all variables x<sup>l</sup> except x<sup>0</sup> and x<sup>L/2</sup> in the graphical models.

similarity and (implicit) relationship between items (and users). Similar to the generalized SDAE, for computational efficiency, we can also take λ<sup>s</sup> to infinity.

The graphical model of CDL when λ<sup>s</sup> approaches positive infinity is shown in Figure 4, where, for notational simplicity, we use x<sup>0</sup>, x<sup>L/2</sup>, and x<sup>C</sup> in place of X<sup>T</sup><sub>0,j∗</sub>, X<sup>T</sup><sub>i,j∗</sub>, and X<sup>T</sup><sub>c,j∗</sub>, respectively.

Note that according the definition in Section 4.1, here the perception variables Ω<sup>p</sup> = {{W<sup>l</sup>}, {b<sup>l</sup>}, {X<sup>l</sup>}, X<sup>c</sup>}, the hinge variables Ω<sup>h</sup> = {V}, and the task variables Ω<sup>t</sup> = {U, R}, where V = (v<sub>j</sub>)<sup>j</sup><sub>j=1</sub> and U = (u<sub>i</sub>)<sup>l</sup><sub>i=1</sub>.

**Learning**: Based on the CDL model above, all parameters could be treated as random variables so that fully Bayesian methods such as Markov chain Monte Carlo (MCMC) or variational approximation methods [32] may be applied. However, such treatment typically incurs high computational cost. Consequently, CDL uses an EM-style algorithm for obtaining the MAP estimates, as in [60].

As in CTR [60], maximizing the posterior probability is equivalent to maximizing the joint log-likelihood of U, V, {X<sup>l</sup>}, X<sup>c</sup>, {W<sup>l</sup>}, {b<sup>l</sup>}, and R given λ<sup>u</sup>, λ<sup>v</sup>, λ<sup>w</sup>, λ<sup>s</sup>, and λ<sup>n</sup>:

$$
\mathscr{L} = -\frac{\lambda_u}{2} \sum_i \|\mathbf{u}_i\|_2^2 - \frac{\lambda_w}{2} \sum_l (\|\mathbf{W}_l\|_F^2 + \|\mathbf{b}_l\|_2^2)
$$

$$
-\frac{\lambda_v}{2} \sum_j \|\mathbf{v}_j - \mathbf{X}_{\frac{L}{2},j*}^T\|_2^2 - \frac{\lambda_n}{2} \sum_j \|\mathbf{X}_{L,j*} - \mathbf{X}_{c,j*}\|_2^2
$$

$$
-\frac{\lambda_s}{2} \sum_j \sum_j \|\sigma(\mathbf{X}_{l-1,j*} \mathbf{W}_l + \mathbf{b}_l) - \mathbf{X}_{l,j*}\|_2^2
$$

$$
-\sum_{i,j} \frac{\mathbf{C}_{ij}}{2} (\mathbf{R}_{ij} - \mathbf{u}_i^T \mathbf{v}_j)^2
$$

If λ<sup>s</sup> goes to infinity, the likelihood becomes:

$$
\mathscr{L} = -\frac{\lambda_u}{2} \sum_i \|\mathbf{u}_i\|_2^2 - \frac{\lambda_w}{2} \sum_l (\|\mathbf{W}_l\|_F^2 + \|\mathbf{b}_l\|_2^2)
$$

$$
-\frac{\lambda_v}{2} \sum_j \|\mathbf{v}_j - f_e(\mathbf{X}_{0,j*}, \mathbf{W}^+)^T\|_2^2
$$

$$
-\frac{\lambda_n}{2} \sum_j \|\mathbf{v}_j - \mathbf{W}^+ - \mathbf{X}_{c,j*}\|_2^2
$$

$$
-\sum_{i,j} \frac{\mathbf{C}_{ij}}{2} (\mathbf{R}_{ij} - \mathbf{u}_i^T \mathbf{v}_j)^2
$$

where the encoder function f<sub>e</sub>(·, W<sup>+</sup>) takes the corrupted content vector X<sub>0,j*} of item j as input and computes the encoding of the item, and the function f<sub>r</sub>(·, W<sup>+</sup>) also takes

![img-4.jpeg](img-4.jpeg)

Fig. 5. NN representation for degenerated CDL.

X<sub>0,j*} as input, computes the encoding and then reconstructs the content vector of item j. For example, if the number of layers L = 6, f<sub>e</sub>(X<sub>0,j*</sub>, W<sup>+</sup>) is the output of the third layer while f<sub>r</sub>(X<sub>0,j*</sub>, W<sup>+</sup>) is the output of the sixth layer.

From the optimization perspective, the third term in the objective function (8) above is equivalent to a multi-layer perceptron using the latent item vectors v<sub>j</sub> as the target while the fourth term is equivalent to an SDAE minimizing the reconstruction error. From the perspective of neural networks (NN), when λ<sup>s</sup> approaches positive infinity, training of the probabilistic graphical model of CDL in Figure 4(left) would degenerate to simultaneously training two neural networks overlaid together with a common input layer (the corrupted input) but different output layers, as shown in Figure 5. Note that the second network is much more complex than typical neural networks due to the involvement of the rating matrix.

When the ratio λ<sup>n</sup>/λ<sup>v</sup> approaches positive infinity, it will degenerate to a two-step model in which the latent representation learned using SDAE is put directly into the CTR. The interaction between the perception component and the task-specific component is one-way (from the perception component to the task-specific component), meaning that the perception component will not be affected by the task-specific component. Another extreme happens when λ<sup>n</sup>/λ<sup>v</sup> goes to zero where the decoder of the SDAE essentially vanishes. On the right of Figure 4 is the graphical model of the degenerated CDL when λ<sup>n</sup>/λ<sup>v</sup> goes to zero. As demonstrated in the experiments, the predictive performance will suffer greatly for both extreme cases [67]. This verifies that (1) the information from the task-specific component can improve the perception component, and (2) mutual boosting effect is crucial to BDL.

For u<sup>i</sup> and v<sub>j</sub>, block coordinate descent similar to [30],

TABLE 2 Recall@300 on the dataset citeulike-a (%)


[60] is used. Given the current **W**^{+}, we compute the gradients of **L** with respect to **u**_{i} and **v**_{j} and then set them to zero, leading to the following update rules:

$$
\begin{aligned}
\mathbf{u}*i & \leftarrow \left( \mathbf{V} \mathbf{C}*i \mathbf{V}^T + \lambda*{u} \mathbf{I}*{K} \right)^{-1} \mathbf{V} \mathbf{C}*i \mathbf{R}*i \\
\mathbf{v}*{j} & \leftarrow \left( \mathbf{U} \mathbf{C}*i \mathbf{U}^T + \lambda*{v} \mathbf{I}*{K} \right)^{-1} \left( \mathbf{U} \mathbf{C}*{j} \mathbf{R}*{j} + \lambda*{v} f_{e}\left( \mathbf{X}_{0,j\ast}, \mathbf{W}^{+}\right)^T \right),
\end{aligned}
$$

where **U** = (**u**_{i}), **i**_{i=1}, **V** = (**v**_{j}), **j**_{i=1}, **C**_{i} = diag(**C**_{i1}, ..., **C**_{iJ}) is a diagonal matrix, **R**_{i} = (**R**_{i1}, ..., **R**_{iJ})^{T} is a column vector containing all the ratings of user i, and **C**_{ij} reflects the confidence controlled by a and b as discussed in [30]. **C**_{j} and **R**_{j} are defined similarly for item j.

Given **U** and **V**, we can learn the weights **W**_{l} and biases **b**_{l} for each layer using the back-propagation learning algorithm. The gradients of the likelihood with respect to **W**_{l} and **b**_{l} are as follows:

$$
\begin{aligned}
\nabla_{\mathbf{W}_l} \mathcal{L} &= -\lambda_{w} \mathbf{W}_l \\
- & \lambda_v \sum_{j} \nabla_{\mathbf{W}_l} f_{e}\left(\mathbf{X}_{0,j\ast}, \mathbf{W}^{+}\right)^T (f_{e}\left(\mathbf{X}_{0,j\ast}, \mathbf{W}^{+}\right)^T - \mathbf{v}_{j}) \\
- & \lambda_n \sum_{j} \nabla_{\mathbf{W}_l} f_{r}\left(\mathbf{X}_{0,j\ast}, \mathbf{W}^{+}\right) (f_{r}\left(\mathbf{X}_{0,j\ast}, \mathbf{W}^{+}\right) - \mathbf{X}_{c,j\ast})
\end{aligned}
$$

$$
\nabla_{\mathbf{b}_l} \mathcal{L} = -\lambda_{w} \mathbf{b}_l
$$

$$
-\lambda_v \sum_{j} \nabla_{\mathbf{b}_l} f_{e}\left(\mathbf{X}_{0,j\ast}, \mathbf{W}^{+}\right)^T (f_{e}\left(\mathbf{X}_{0,j\ast}, \mathbf{W}^{+}\right)^T - \mathbf{v}_{j})
$$

$$
-\lambda_n \sum_{j} \nabla_{\mathbf{b}_l} f_{r}\left(\mathbf{X}_{0,j\ast}, \mathbf{W}^{+}\right) (f_{r}\left(\mathbf{X}_{0,j\ast}, \mathbf{W}^{+}\right) - \mathbf{X}_{c,j\ast})
$$

By alternating the update of **U**, **V**, **W**_{l}, and **b**_{l}, we can find a local optimum for **L**. Several commonly used techniques such as using a momentum term may be applied to alleviate the local optimum problem. Note that a carefully designed BDL model (according to the i.i.d. requirement and with proper variance models as stated in Section 4.1) can minimize the overhead of seamlessly combining the perception component and the task-specific component. In CDL, the computational complexity (per iteration) of the perception component is O(JBK_{1}) and that of the task-specific component is O(K^{2}N_{R} + K^{3}), where N_{R} is the number of non-zero entries in the rating matrix and K = K_{k}. The computational complexity (per iteration) for the whole model is O(JBK_{1} + K^{2}N_{R} + K^{3}) [67]. No significant overhead is introduced.

**Prediction**: Let D be the observed test data. Similar to [60], CDL uses the point estimates of **u**_{i}, **W**^{+} and **e**_{j} to calculate the predicted rating:

$$E[\mathbf{R}_{ij}|D] \approx E[\mathbf{u}*i|D]^T (E[f*{e}\left(\mathbf{X}_{0,j\ast}, \mathbf{W}^{+}\right)^T|D] + E[\mathbf{e}_{j}|D]),$$

where E[·] denotes the expectation operation. In other words, we approximate the predicted rating as:

$$\mathbf{R}_{ij}^* \approx (\mathbf{u}_j^*)^T (f_{e}\left(\mathbf{X}_{0,j\ast}, \mathbf{W}^{+}\right)^T + \mathbf{e}_j^*) = (\mathbf{u}_i^*)^T \mathbf{v}_j^*.$$

Note that for any new item j with no rating in the training data, its offset **e**_{j} will be **0**.

![img-5.jpeg](img-5.jpeg)

Fig. 6. Sampling as generalized BP.

Table 2 shows the recall of recommendation with 300 recommended items for different methods in the dataset citeulike-a. Please refer to [67] for more details.

In the following text, we provide several extensions of CDL from different perspectives.

### 4.2.2 Bayesian Collaborative Deep Learning

Besides the MAP estimates, a sampling-based algorithm for the Bayesian treatment of CDL is also proposed in [67]. This algorithm turns out to be a Bayesian and generalized version of the well-known back-propagation (BP) learning algorithm. We list the key conditional densities as follows:

**For W**+: We denote the concatenation of **W**_{l,*n} and **b**_{l}^{(n)} as **W**_{l,*n}^{+}. Similarly, the concatenation of **X**_{l,j∗} and 1 is denoted as **X**_{l,j∗}^{+}. The subscripts of **I** are ignored. Then

$$p(\mathbf{W}_{l,\ast n}^{+}|\mathbf{X}_{l-1,j\ast}, \mathbf{X}_{l,j\ast}, \lambda_s) \propto \mathcal{N}(\mathbf{W}_{l,\ast n}^{+}|0, \lambda_{w}^{-1}\mathbf{I}) \mathcal{N}(\mathbf{X}_{l,\ast n}|\sigma(\mathbf{X}_{l-1}^{*}\mathbf{W}_{l,\ast n}^{+}), \lambda_{s}^{-1}\mathbf{I}).$$

**For X**_{l,j∗} **(l** ≠ L/2**):** Similarly, we denote the concatenation of **W**_{l} and **b**_{l} as **W**_{l}^{+} and have

$$p(\mathbf{X}_{l,j\ast}|\mathbf{W}_{l}^{+}, \mathbf{W}_{l+1}^{+}, \mathbf{X}_{l-1,j\ast}, \mathbf{X}_{l+1,j\ast}, \lambda_s) \propto \mathcal{N}(\mathbf{X}_{l,j\ast}|\sigma(\mathbf{X}_{l-1,j\ast}^{+}\mathbf{W}_{l}^{+}), \lambda_{s}^{-1}\mathbf{I}) \cdot \mathcal{N}(\mathbf{X}_{l+1,j\ast}|\sigma(\mathbf{X}_{l,j\ast}^{+}\mathbf{W}_{l+1}^{+}), \lambda_{s}^{-1}\mathbf{I}).$$

Note that for the last layer (l = L) the second Gaussian would be **N**(**X**_{v,j∗}|**X**_{l,j∗}, **λ**_{s}^{-1}**I**) instead.

**For X**_{l,j∗} **(l** = L/2**):** Similarly, we have

$$p(\mathbf{X}_{l,j\ast}|\mathbf{W}_{l}^{+}, \mathbf{W}_{l+1}^{+}, \mathbf{X}_{l-1,j\ast}, \mathbf{X}_{l+1,j\ast}, \lambda_s, \lambda_v, \mathbf{v}_{j}) \propto \mathcal{N}(\mathbf{X}_{l,j\ast}|\sigma(\mathbf{X}_{l-1,j\ast}^{+}\mathbf{W}_{l}^{+}), \lambda_{s}^{-1}\mathbf{I}) \cdot \mathcal{N}(\mathbf{X}_{l+1,j\ast}|\sigma(\mathbf{X}_{l,j\ast}^{+}\mathbf{W}_{l+1}^{+}), \lambda_{s}^{-1}\mathbf{I}) \cdot \mathcal{N}(\mathbf{v}_{j}|\mathbf{X}_{l,j\ast}, \lambda_{v}^{-1}\mathbf{I}).$$

**For v**_{j}:** The posterior p(**v**_{j}|**X**_{L/2,j∗}, **R**_{∗j}, **C**_{∗j}, **λ**_{v}, **U**) ∑_{j} **N**(**v**_{j}|**X**_{L/2,j∗}, **λ**_{v}^{-1}**I**) ∏_{i} **N**(**R**_{ij}|**u**_{i}^{T} **v**_{j}, **C**_{ij}^{-1}).

**For u**_{i}:** The posterior p(**u**_{i}|**R**_{i∗}, **V**, **λ**_{u}, **C**_{i∗}) ∑_{i} **N**(**u**_{i}|0, **λ**_{u}^{-1}**I**) ∏_{j} **N**_{ij} (**u**_{i}^{T} **v**_{j}|**C**_{ij}^{-1}).

Interestingly, if **λ**_{s} goes to infinity and adaptive rejection Metropolis sampling (which involves using the gradients of the objective function to approximate the proposal distribution) is used, the sampling for **W**^{+} turns out to be a *Bayesian generalized* version of BP. Specifically, as Figure 6 shows, after getting the gradient of the loss function at one point (the red dashed line on the left), the next sample would be drawn in the region under that line, which is

equivalent to a probabilistic version of BP. If a sample is above the curve of the loss function, a new tangent line (the black dashed line on the right) would be added to better approximate the distribution corresponding to the joint log-likelihood. After that, samples would be drawn from the region under both lines. During the sampling, besides searching for local optima using the gradients (MAP), the algorithm also takes the variance into consideration. That is why it is called Bayesian generalized back-propagation.

### 4.2.3 Marginalized Collaborative Deep Learning

In SDAE, corrupted input goes through encoding and decoding to recover the clean input. Usually, different epochs of training use different corrupted versions as input. Hence generally, SDAE needs to go through enough epochs of training to see sufficient corrupted versions of the input. Marginalized SDAE (mSDAE) [13] seeks to avoid this by marginalizing out the corrupted input and obtaining closed-form solutions directly. In this sense, mSDAE is more computationally efficient than SDAE.

As mentioned in [37], using mSDAE instead of the Bayesian SDAE could lead to more efficient learning algorithms. For example, in [37], the objective when using a one-layer mSDAE can be written as follows:

$$
\begin{aligned}
\mathscr{L}= & -\sum_{j}\left\|\overline{\mathbf{X}}_{0, j *} \mathbf{W}_{1}-\overline{\mathbf{X}}_{c, j *}\right\|_{2}^{2}-\sum_{i, j} \frac{\mathbf{C}_{i j}}{2}\left(\mathbf{R}_{i j}-\mathbf{u}_{i}^{T} \mathbf{v}_{j}\right)^{2} \\
& -\frac{\lambda_{u}}{2} \sum_{i}\left\|\mathbf{u}_{i}\right\|_{2}^{2}-\frac{\lambda_{v}}{2} \sum_{j}\left\|\mathbf{v}_{j}^{T} \mathbf{P}_{1}-\mathbf{X}_{0, j *} \mathbf{W}_{1}\right\|_{2}^{2}
\end{aligned}
$$

where $\overline{\mathbf{X}}_{0, j *}$ is the collection of $k$ different corrupted versions of $\mathbf{X}_{0, j *}$ (a $k$-by- $B$ matrix) and $\overline{\mathbf{X}}_{c, j *}$ is the $k$-time repeated version of $\mathbf{X}_{c, j *}$ (also a $k$-by- $B$ matrix). $\mathbf{P}_{1}$ is the transformation matrix for item latent factors.

The solution for $\mathbf{W}_{1}$ would be:

$$
\mathbf{W}_{1}=E\left(\mathbf{S}_{1}\right) E\left(\mathbf{Q}_{1}\right)^{-1}
$$

where $\mathbf{S}_{1}=\overline{\mathbf{X}}_{c, j *}^{T} \overline{\mathbf{X}}_{0, j *}+\frac{\lambda_{u}}{2} \mathbf{P}_{1}^{T} \mathbf{V} \mathbf{X}_{c}$ and $\mathbf{Q}_{1}=$ $\overline{\mathbf{X}}_{c, j *}^{T} \overline{\mathbf{X}}_{0, j *}+\frac{\lambda_{v}}{2} \mathbf{X}_{c}^{T} \mathbf{X}_{c}$. A solver for the expectation in the equation above is provided in [13]. Note that this is a linear and one-layer case which can be generalized to the nonlinear and multi-layer case using the same techniques as in [12], [13].

As we can see, in marginalized CDL, the perception variables $\boldsymbol{\Omega}_{p}=\left\{\mathbf{X}_{0}, \mathbf{X}_{c}, \mathbf{W}_{1}\right\}$, the hinge variables $\boldsymbol{\Omega}_{h}=$ $\{\mathbf{V}\}$, and the task variables $\boldsymbol{\Omega}_{t}=\left\{\mathbf{P}_{1}, \mathbf{R}, \mathbf{U}\right\}$.

### 4.2.4 Collaborative Deep Ranking

CDL assumes a collaborative filtering setting to model the ratings directly. However, the output of recommender systems is often a ranked list, which means it would be more natural to use ranking rather than ratings as the objective. With this motivation, collaborative deep ranking (CDR) is proposed [71] to jointly perform representation learning and collaborative ranking. The corresponding generative process is the same as that of CDL except for Step 3 and 4 , which should be replaced with:

- For each user $i$,

1) Draw a latent user vector for each user $i$ :

$$
\mathbf{u}_{i} \sim \mathcal{N}\left(\mathbf{0}, \lambda_{u}^{-1} \mathbf{I}_{K}\right)
$$

2) For each pair-wise preference $(j, k) \in \mathcal{P}_{i}$, where $\mathcal{P}_{i}=\left\{(j, k): \mathbf{R}_{i j}-\mathbf{R}_{i k}>0\right\}$, draw the preference: $\boldsymbol{\Delta}_{i j k} \sim \mathcal{N}\left(\mathbf{u}_{i}^{T} \mathbf{v}_{j}-\mathbf{u}_{i}^{T} \mathbf{v}_{k}, \mathbf{C}_{i j k}^{-1}\right)$.

Following the generative process, the last term of Equation (8) becomes $-\sum_{i, j, k} \frac{\mathbf{C}_{i j k}}{2}\left(\boldsymbol{\Delta}_{i j k}-\left(\mathbf{u}_{i}^{T} \mathbf{v}_{j}-\mathbf{u}_{i}^{T} \mathbf{v}_{k}\right)\right)^{2}$. Similar algorithms can be used to learn the parameters in CDR. As reported in [71], using the ranking objective leads to significant improvement in the recommendation performance.

Following the definition in Section 4.1, CDR's perception variables $\boldsymbol{\Omega}_{p}=\left\{\left\{\mathbf{W}_{l}\right\},\left\{\mathbf{b}_{l}\right\},\left\{\mathbf{X}_{l}\right\}, \mathbf{X}_{c}\right\}$, the hinge variables $\boldsymbol{\Omega}_{h}=\{\mathbf{V}\}$, and the task variables $\boldsymbol{\Omega}_{t}=\{\mathbf{U}, \boldsymbol{\Delta}\}$.

### 4.2.5 Symmetric Collaborative Deep Learning

Models like [67], [71] focus the deep learning component on modeling the item content. Besides the content information from the items, attributes of users sometimes contain much more important information. It is therefore desirable to extend CDL to model user attributes as well [37]. We call this variant symmetric CDL. For example, using an extra mSDAE on the user attributes adds two extra terms in Equation (9), $-\frac{\lambda_{u}}{2} \sum_{i}\left\|\mathbf{u}_{i}^{T} \mathbf{P}_{2}-\mathbf{Y}_{0, j *} \mathbf{W}_{2}\right\|_{2}^{2}$ and $-\sum_{i}\left\|\overline{\mathbf{Y}}_{0, i *} \mathbf{W}_{2}-\overline{\mathbf{Y}}_{c, i *}\right\|_{2}^{2}$, where $\overline{\mathbf{Y}}_{0, j *}$ (a $k$-by- $D$ matrix for user attributes) is the collection of $k$ different corrupted versions of $\mathbf{Y}_{0, j *}$ and $\overline{\mathbf{Y}}_{c, i *}$ (also a $k$-by- $D$ matrix) is the $k$-time repeated version of $\mathbf{Y}_{c, i *}$ (the clean user attributes). $\mathbf{P}_{2}$ is the transformation matrix for user latent factors and $D$ is the number of user attributes. Similar to the marginalized CDL, the solution for $\mathbf{W}_{2}$ given other parameters is:

$$
\mathbf{W}_{2}=E\left(\mathbf{S}_{2}\right) E\left(\mathbf{Q}_{2}\right)^{-1}
$$

where $\mathbf{S}_{2}=\overline{\mathbf{Y}}_{c, i *}^{T} \overline{\mathbf{Y}}_{0, i *}+\frac{\lambda_{u}}{2} \mathbf{P}_{2}^{T} \mathbf{U} \mathbf{Y}_{c}$ and $\mathbf{Q}_{2}=\overline{\mathbf{Y}}_{c, i *}^{T} \overline{\mathbf{Y}}_{0, i *}+$ $\frac{\lambda_{v}}{2} \mathbf{Y}_{c}^{T} \mathbf{Y}_{c}$.

In symmetric CDL, the perception variables $\boldsymbol{\Omega}_{p}=$ $\left\{\mathbf{X}_{0}, \mathbf{X}_{c}, \mathbf{W}_{1}, \mathbf{Y}_{0}, \mathbf{Y}_{c}, \mathbf{W}_{2}\right\}$, the hinge variables $\boldsymbol{\Omega}_{h}=$ $\{\mathbf{V}, \mathbf{U}\}$, and the task variables $\boldsymbol{\Omega}_{t}=\left\{\mathbf{P}_{1}, \mathbf{P}_{2}, \mathbf{R}\right\}$.

### 4.2.6 Discussion

CDL is the first hierarchical Bayesian model to bridge the gap between state-of-the-art deep learning models and RS. By performing deep learning collaboratively, CDL and its variants can simultaneously extract an effective deep feature representation from the content and capture the similarity and implicit relationship between items (and users). This way, the perception component and the task-specific component are able to interact with each other to create synergy and further boost the recommendation accuracy. The learned representation may also be used for tasks other than recommendation. Unlike previous deep learning models which use a simple target such as classification [33] and reconstruction [59], CDL-based models ${ }^{6}$ use CF as a more complex target in a probabilistic framework.

As mentioned in Section 1, the synergy created by information exchange between two components is crucial
6. During the review process of this paper, there are some newly published works based on BDL (e.g., some CDL-based works [65], [72]).

to the performance of BDL. In the CDL-based models above, the exchange is achieved by assuming Gaussian distributions that connect the hinge variables and the variables in the perception component (drawing the hinge variable $\mathbf{v}_{j} \sim \mathcal{N}\left(\mathbf{X}_{\frac{L}{2}, j *}^{T}, \lambda_{r}^{-1} \mathbf{I}_{K}\right)$ in the generative process of CDL, where $\mathbf{X}_{\frac{L}{2}}$ is a perception variable), which is simple but effective and efficient in computation. Among the five CDL-based models in Table 1, three of them are HV models and the others are LV models, according to the definition in Section 4.1. Since it has been verified that the HV CDL significantly outperforms its ZV counterpart [67], we can expect extra performance boosts from the LV counterparts of the three HV models.

Besides efficient information exchange, the designs of the models also meet the i.i.d. requirement of the distribution concerning hinge variables discussed in Section 4.1 and are hence easily parallelizable. In some models to be introduced later, we will see alternative designs to enable efficient and i.i.d. information exchange between the two components of BDL.

### 4.3 Bayesian Deep Learning for Topic Models

In this section, we review some examples of using BDL for topic models. These models combine the merits of PGM (which naturally incorporates the probabilistic relationships among variables) and NN (which learns deep representations efficiently), leading to significant performance boost.

### 4.3.1 Relational Stacked Denoising Autoencoders as Topic Models

Problem Statement and Notation: Assume we have a set of items (articles or movies) $\mathbf{X}_{c}$, with $\mathbf{X}_{c, j *}^{T} \in \mathbb{R}^{B}$ denoting the content (attributes) of item $j$. Besides, we use $\mathbf{I}_{K}$ to denote a $K$-dimensional identity matrix and $\mathbf{S}=\left[\mathbf{s}_{1}, \mathbf{s}_{2}, \cdots, \mathbf{s}_{J}\right]$ to denote the relational latent matrix with $\mathbf{s}_{j}$ representing the relational properties of item $j$.

From the perspective of SDAE, the $J$-by- $B$ matrix $\mathbf{X}_{c}$ represents the clean input to the SDAE and the noise-corrupted matrix of the same size is denoted by $\mathbf{X}_{0}$. Besides, we denote the output of layer $l$ of the SDAE, a $J$-by- $K_{l}$ matrix, by $\mathbf{X}_{l}$. Row $j$ of $\mathbf{X}_{l}$ is denoted by $\mathbf{X}_{l, j *}$, $\mathbf{W}_{l}$ and $\mathbf{b}_{l}$ are the weight matrix and bias vector of layer $l$, $\mathbf{W}_{l, * n}$ denotes column $n$ of $\mathbf{W}_{l}$, and $L$ is the number of layers. As a shorthand, we refer to the collection of weight matrices and biases in all layers as $\mathbf{W}^{+}$. Note that an $L / 2$-layer SDAE corresponds to an $L$-layer network.

Model Formulation: Here we will use the Bayesian SDAE introduced before as a building block for the relational stacked denoising autoencoder (RSDAE) model.

As mentioned in [64], RSDAE is formulated as a novel probabilistic model which can seamlessly integrate layered representation learning and the relational information available. This way, the model can simultaneously learn the feature representation from the content information and the relation between items. The graphical model of RSDAE is shown in Figure 7 and the generative process is listed as follows:
![img-6.jpeg](img-6.jpeg)

Fig. 7. Graphical model of RSDAE for $L=4 . \lambda_{s}$ is not shown here to prevent clutter.

1) Draw the relational latent matrix $\mathbf{S}$ from a matrix variate normal distribution [21]:

$$
\mathbf{S} \sim \mathcal{N}_{K, J}\left(0, \mathbf{I}_{K} \otimes\left(\lambda_{l} \mathscr{L}_{a}\right)^{-1}\right)
$$

2) For layer $l$ of the SDAE where $l=1,2, \ldots, \frac{L}{2}-1$,
a) For each column $n$ of the weight matrix $\mathbf{W}_{l}$, draw $\mathbf{W}_{l, * n} \sim \mathcal{N}\left(0, \lambda_{w}^{-1} \mathbf{I}_{K_{l}}\right)$
b) Draw the bias vector $\mathbf{b}_{l} \sim \mathcal{N}\left(0, \lambda_{w}^{-1} \mathbf{I}_{K_{l}}\right)$.
c) For each row $j$ of $\mathbf{X}_{l}$, draw

$$
\mathbf{X}_{l, j *} \sim \mathcal{N}\left(\sigma\left(\mathbf{X}_{l-1, j *} \mathbf{W}_{l}+\mathbf{b}_{l}\right), \lambda_{s}^{-1} \mathbf{I}_{K_{l}}\right)
$$

3) For layer $\frac{L}{2}$ of the SDAE network, draw the representation vector for item $j$ from the product of two Gaussians (PoG) [16]:

$$
\mathbf{X}_{\frac{L}{2}, j *} \sim \operatorname{PoG}\left(\sigma\left(\mathbf{X}_{\frac{L}{2}-1, j *} \mathbf{W}_{l}+\mathbf{b}_{l}\right), \mathbf{s}_{j}^{T}, \lambda_{s}^{-1} \mathbf{I}_{K}, \lambda_{r}^{-1} \mathbf{I}_{K}\right)
$$

4) For layer $l$ of the SDAE network where $l=\frac{L}{2}+1, \frac{L}{2}+$ $2, \ldots, L$,
a) For each column $n$ of the weight matrix $\mathbf{W}_{l}$, draw $\mathbf{W}_{l, * n} \sim \mathcal{N}\left(0, \lambda_{w}^{-1} \mathbf{I}_{K_{l}}\right)$
b) Draw the bias vector $\mathbf{b}_{l} \sim \mathcal{N}\left(0, \lambda_{w}^{-1} \mathbf{I}_{K_{l}}\right)$.
c) For each row $j$ of $\mathbf{X}_{l}$, draw

$$
\mathbf{X}_{l, j *} \sim \mathcal{N}\left(\sigma\left(\mathbf{X}_{l-1, j *} \mathbf{W}_{l}+\mathbf{b}_{l}\right), \lambda_{s}^{-1} \mathbf{I}_{K_{l}}\right)
$$

5) For each item $j$, draw a clean input

$$
\mathbf{X}_{c, j *} \sim \mathcal{N}\left(\mathbf{X}_{L, j *}, \lambda_{n}^{-1} \mathbf{I}_{B}\right)
$$

Here $K=K_{\frac{L}{2}}$ is the dimensionality of the learned representation vector for each item, $\mathbf{S}$ denotes the $K \times J$ relational latent matrix in which column $j$ is the relational latent vector $\mathbf{s}_{j}$ for item $j$. Note that $\mathcal{N}_{K, J}\left(0, \mathbf{I}_{K} \otimes\left(\lambda_{l} \mathscr{L}_{a}\right)^{-1}\right)$ in Equation (10) is a matrix variate normal distribution defined as in [21]:

$$
\begin{aligned}
p(\mathbf{S}) & =\mathcal{N}_{K, J}\left(0, \mathbf{I}_{K} \otimes\left(\lambda_{l} \mathscr{L}_{a}\right)^{-1}\right) \\
& =\frac{\exp \left\{\operatorname{tr}\left[-\frac{\lambda_{l}}{2} \mathbf{S} \mathscr{L}_{a} \mathbf{S}^{T}\right]\right\}}{(2 \pi)^{J K / 2}\left|\mathbf{I}_{K}\right|^{J / 2}\left|\lambda_{l} \mathscr{L}_{a}\right|^{-K / 2}}
\end{aligned}
$$

where the operator $\otimes$ denotes the Kronecker product of two matrices [21], $\operatorname{tr}(\cdot)$ denotes the trace of a matrix, and $\mathscr{L}_{a}$ is the Laplacian matrix incorporating the relational information. $\mathscr{L}_{a}=\mathbf{D}-\mathbf{A}$, where $\mathbf{D}$ is a diagonal matrix whose diagonal elements $\mathbf{D}_{i i}=\sum_{j} \mathbf{A}_{i j}$ and $\mathbf{A}$ is the adjacency matrix representing the relational information with binary entries indicating the links (or relations) between items. $\mathbf{A}_{j j^{\prime}}=1$ indicates that there is a link between item $j$ and item $j^{\prime}$ and $\mathbf{A}_{j j^{\prime}}=0$ otherwise. $\operatorname{PoG}\left(\sigma\left(\mathbf{X}_{\frac{L}{2}-1, j *} \mathbf{W}_{l}+\mathbf{b}_{l}\right), \mathbf{s}_{j}^{T}, \lambda_{s}^{-1} \mathbf{I}_{K}, \lambda_{r}^{-1} \mathbf{I}_{K}\right)$ denotes the product of the Gaussian $\mathcal{N}\left(\sigma\left(\mathbf{X}_{\frac{L}{2}-1, j *} \mathbf{W}_{l}+\mathbf{b}_{l}\right), \lambda_{s}^{-1} \mathbf{I}_{K}\right)$

TABLE 3
Recall@300 on the dataset movielens-plot (\%)


and the Gaussian $\mathcal{N}\left(\mathbf{s}_{j}^{T}, \lambda_{r}^{-1} \mathbf{I}_{K}\right)$, which is also a Gaussian [16].

According to the generative process above, maximizing the posterior probability is equivalent to maximizing the joint log-likelihood of $\left\{\mathbf{X}_{l}\right\}, \mathbf{X}_{c}, \mathbf{S},\left\{\mathbf{W}_{l}\right\}$, and $\left\{\mathbf{b}_{l}\right\}$ given $\lambda_{s}, \lambda_{w}, \lambda_{l}, \lambda_{r}$, and $\lambda_{n}$ :

$$
\begin{aligned}
\mathscr{L}= & -\frac{\lambda_{l}}{2} \operatorname{tr}\left(\mathbf{S} \mathscr{L}_{a} \mathbf{S}^{T}\right)-\frac{\lambda_{r}}{2} \sum_{j}\left\|\left(\mathbf{s}_{j}^{T}-\mathbf{X}_{\frac{L}{2}, j^{*}}\right)\right\|_{2}^{2} \\
& -\frac{\lambda_{w}}{2} \sum_{l}\left(\left\|\mathbf{W}_{l}\right\|_{F}^{2}+\left\|\mathbf{b}_{l}\right\|_{2}^{2}\right) \\
& -\frac{\lambda_{n}}{2} \sum_{j}\left\|\mathbf{X}_{L, j^{*}}-\mathbf{X}_{c, j *}\right\|_{2}^{2} \\
& -\frac{\lambda_{s}}{2} \sum_{l} \sum_{j}\left\|\sigma\left(\mathbf{X}_{l-1, j *} \mathbf{W}_{l}+\mathbf{b}_{l}\right)-\mathbf{X}_{l, j *}\right\|_{2}^{2}
\end{aligned}
$$

where $\mathbf{X}_{l, j *}=\sigma\left(\mathbf{X}_{l-1, j *} \mathbf{W}_{l}+\mathbf{b}_{l}\right)$. Note that the first term $-\frac{\lambda_{l}}{2} \operatorname{tr}\left(\mathbf{S} \mathscr{L}_{a} \mathbf{S}^{T}\right)$ corresponds to $\log p(\mathbf{S})$ in the matrix variate distribution in Equation (12). By simple manipulation, we have $\operatorname{tr}\left(\mathbf{S} \mathscr{L}_{a} \mathbf{S}^{T}\right)=\sum_{k=1}^{K} \mathbf{S}_{k *}^{T} \mathscr{L}_{a} \mathbf{S}_{k *}$, where $\mathbf{S}_{k *}$ denotes the $k$-th row of $\mathbf{S}$. As we can see, maximizing $-\frac{\lambda_{l}}{2} \operatorname{tr}\left(\mathbf{S}^{T} \mathscr{L}_{a} \mathbf{S}\right)$ is equivalent to making $\mathbf{s}_{j}$ closer to $\mathbf{s}_{j^{\prime}}$ if item $j$ and item $j^{\prime}$ are linked (namely $\mathbf{A}_{j j^{\prime}}=1$ ).

In RSDAE, the perception variables $\boldsymbol{\Omega}_{p}=$ $\left\{\left\{\mathbf{X}_{l}\right\}, \mathbf{X}_{c},\left\{\mathbf{W}_{l}\right\},\left\{\mathbf{b}_{l}\right\}\right\}$, the hinge variables $\boldsymbol{\Omega}_{h}=\{\mathbf{S}\}$, and the task variables $\boldsymbol{\Omega}_{t}=\{\mathbf{A}\}$.

Learning Relational Representation and Topics: [64] provides an EM-style algorithm for MAP estimation. Here we review some of the key steps as follows.

In terms of the relational latent matrix $\mathbf{S}$, we first fix all rows of $\mathbf{S}$ except the $k$-th one $\mathbf{S}_{k *}$ and then update $\mathbf{S}_{k *}$. Specifically, we take the gradient of $\mathscr{L}$ with respect to $\mathbf{S}_{k *}$, set it to 0 , and get the following linear system:

$$
\left(\lambda_{l} \mathscr{L}_{a}+\lambda_{r} \mathbf{I}_{J}\right) \mathbf{S}_{k *}=\lambda_{r} \mathbf{X}_{\frac{L}{2}, * k}^{T}
$$

A naive approach is to solve the linear system by setting $\mathbf{S}_{k *}=\lambda_{r}\left(\lambda_{l} \mathscr{L}_{a}+\lambda_{r} \mathbf{I}_{J}\right)^{-1} \mathbf{X}_{\frac{L}{2}, * k}^{T}$. Unfortunately, the complexity is $O\left(J^{3}\right)$ for one single update. Similar to [38], the steepest descent method [55] is used to iteratively update $\mathbf{S}_{k *}$ :

$$
\begin{aligned}
\mathbf{S}_{k *}(t+1) & \leftarrow \mathbf{S}_{k *}(t)+\delta(t) r(t) \\
r(t) & \leftarrow \lambda_{r} \mathbf{X}_{\frac{L}{2}, * k}^{T}-\left(\lambda_{l} \mathscr{L}_{a}+\lambda_{r} \mathbf{I}_{J}\right) \mathbf{S}_{k *}(t) \\
\delta(t) & \leftarrow \frac{r(t)^{T} r(t)}{r(t)^{T}\left(\lambda_{l} \mathscr{L}_{a}+\lambda_{r} \mathbf{I}_{J}\right) r(t)}
\end{aligned}
$$

As discussed in [38], the use of steepest descent method dramatically reduces the computation cost in each iteration from $O\left(J^{3}\right)$ to $O(J)$.

Given $\mathbf{S}$, we can learn $\mathbf{W}_{l}$ and $\mathbf{b}_{l}$ for each layer using the back-propagation algorithm. By alternating the update of $\mathbf{S}, \mathbf{W}_{l}$, and $\mathbf{b}_{l}$, a local optimum for $\mathscr{L}$ can be found. Also, techniques such as including a momentum term may help to avoid being trapped in a local optimum. The computational
complexity for each iteration is $O\left(J B K_{1}+K J\right)$. Similar to CDL, no significant overhead is introduced.

Table 3 shows the recall for different methods in the dataset movielens-plot when the learned representation is used for tag recommendation (with 300 recommended tags for each item). As we can see, RSDAE significantly outperforms SDAE, which means that the relational information from the task-specific component is crucial to the performance boost. Please refer to [64] for more details.

### 4.3.2 Deep Poisson Factor Analysis with Sigmoid Belief Networks

The Poisson distribution with support over nonnegative integers is known as a natural choice to model counts. It is, therefore, desirable to use it as a building block for topic models [8]. With this motivation, [75] proposed a model, dubbed Poisson factor analysis (PFA), for latent nonnegative matrix factorization via Poisson distributions.

Poisson Factor Analysis: PFA assumes a discrete $N$-by- $P$ matrix $\mathbf{X}$ containing word counts of $N$ documents with a vocabulary size of $P$ [17], [75]. In a nutshell, PFA can be described using the following equation:

$$
\mathbf{X} \sim \operatorname{Pois}((\boldsymbol{\Theta} \circ \mathbf{H}) \boldsymbol{\Phi})
$$

where $\boldsymbol{\Phi}$ (of size $K$-by- $P$ where $K$ is the number of topics) denotes the factor loading matrix in factor analysis with the $k$-th row $\boldsymbol{\phi}_{k}$ encoding the importance of each word in topic $k$. The $N$-by- $K$ matrix $\boldsymbol{\Theta}$ is the factor score matrix with the $n$-th row $\boldsymbol{\theta}_{n}$ containing topic proportions for document $n$. The $N$-by- $K$ matrix $\mathbf{H}$ is a latent binary matrix with the $n$-th row $\mathbf{h}_{n}$ defining a set of topics associated with document $n$.

Different priors correspond to different models. For example, Dirichlet priors on $\boldsymbol{\phi}_{k}$ and $\boldsymbol{\theta}_{n}$ with an all-one matrix $\mathbf{H}$ would recover LDA [8] while a beta-Bernoulli prior on $\mathbf{h}_{n}$ leads to the negative binomial focused topic model (NB-FTM) model in [74]. In [17], a deep-structured prior based on sigmoid belief networks (SBN) [43] (an MLP variant with binary hidden units) is imposed on $\mathbf{h}_{n}$ to form a deep PFA model for topic modeling.

Deep Poisson Factor Analysis: In the deep PFA model [17], the generative process can be summarized as follows:

$$
\begin{aligned}
\boldsymbol{\phi}_{k} & \sim \operatorname{Dir}\left(a_{\phi}, \ldots, a_{\phi}\right), \theta_{n k} \sim \operatorname{Gamma}\left(r_{k}, \frac{p_{n}}{1-p_{n}}\right) \\
r_{k} & \sim \operatorname{Gamma}\left(\gamma_{0}, \frac{1}{c_{0}}\right), \gamma_{0} \sim \operatorname{Gamma}\left(c_{0}, \frac{1}{f_{0}}\right) \\
h_{n k_{L}}^{(L)} & \sim \operatorname{Ber}\left(\sigma\left(b_{k_{L}}^{(L)}\right)\right) \\
h_{n k_{l}}^{(l)} & \sim \operatorname{Ber}\left(\sigma\left(\mathbf{h}_{n}^{(l+1)} \mathbf{w}_{k_{l}}^{(l)}+b_{k_{l}}^{(l)}\right)\right) \\
x_{n p k} & \sim \operatorname{Pois}\left(\phi_{k p} \theta_{n k} h_{n k}^{(1)}\right), x_{n p}=\sum_{k=1}^{K} x_{n p k}
\end{aligned}
$$

where $L$ is the number of layers in SBN, which corresponds to Equation (15) and (16). $x_{n p}$ is an entry in the matrix $\mathbf{X}$, $\mathbf{h}_{n}^{(l)}$ is the $n$-th row of $\mathbf{H}_{l}$, and $x_{n p k}$ is the count of word $p$ that comes from topic $k$ in document $n$.

In this model, the perception variables $\boldsymbol{\Omega}_{p}=$ $\left\{\left\{\mathbf{H}_{l}\right\},\left\{\mathbf{W}_{l}\right\},\left\{\mathbf{b}_{l}\right\}\right\}$, the hinge variables $\boldsymbol{\Omega}_{h}=\{\mathbf{X}\}$, and the task variables $\boldsymbol{\Omega}_{t}=\left\{\left\{\boldsymbol{\phi}_{k}\right\},\left\{r_{k}\right\}, \boldsymbol{\Theta}, \gamma_{0}\right\}$. $\mathbf{W}_{l}$ is the weight matrix containing columns of $\mathbf{w}_{k_{l}}^{(l)}$ and $\mathbf{b}_{l}$ is the bias vector containing entries of $b_{k_{l}}^{(l)}$ in Equation (16).

Learning Using Bayesian Conditional Density Filtering: Efficient learning algorithms are needed for Bayesian treatments of deep PFA. [17] proposed to use an online version of MCMC called Bayesian conditional density filtering (BCDF) to learn both the global parameters $\boldsymbol{\Psi}_{g}=\left(\left\{\boldsymbol{\phi}_{k}\right\},\left\{r_{k}\right\}, \gamma_{0},\left\{\mathbf{W}_{l}\right\},\left\{\mathbf{b}_{l}\right\}\right)$ and the local variables $\boldsymbol{\Psi}_{l}=\left(\boldsymbol{\Theta},\left\{\mathbf{H}_{l}\right\}\right)$. The key conditional densities used for the Gibbs updates are as follows:

$$
\begin{aligned}
x_{n p k} & \left|-\sim \operatorname{Multi}\left(x_{n p} ; \zeta_{n p 1}, \ldots, \zeta_{n p K}\right)\right. \\
\boldsymbol{\phi}_{k} & \left|-\sim \operatorname{Dir}\left(a_{\phi}+x_{.1 k}, \ldots, a_{\phi}+x_{. P k}\right)\right. \\
\theta_{n k} & \left|-\sim \operatorname{Gamma}\left(r_{k} h_{n k}^{(1)}+x_{n \cdot k}, p_{n}\right)\right. \\
h_{n k}^{(1)} & \left|-\sim \delta\left(x_{n \cdot k}=0\right) \operatorname{Ber}\left(\frac{\bar{\pi}_{n k}}{\bar{\pi}_{n k}+\left(1-\pi_{n k}\right)}\right)+\delta\left(x_{n \cdot k}>0\right)\right.
\end{aligned}
$$

where $\bar{\pi}_{n k}=\pi_{n k}\left(1-p_{n}\right)^{r_{k}}, \pi_{n k}=\sigma\left(\mathbf{h}_{n}^{(2)} \mathbf{w}_{k}^{(1)}+b_{k}^{(1)}\right)$, $x_{n \cdot k}=\sum_{p=1}^{P} x_{n p k}, x_{\cdot p k}=\sum_{n=1}^{N} x_{n p k}$, and $\zeta_{n p k} \propto \phi_{k p} \theta_{n k}$. For the learning of $h_{n k}^{(l)}$ where $l>1$, the same techniques as in [18] can be used.

Learning Using Stochastic Gradient Thermostats: An alternative way of learning deep PFA is through the use of stochastic gradient Nòse-Hoover thermostats (SGNHT), which is more accurate and scalable. Specifically, the following stochastic differential equations (SDE) can be used:

$$
\begin{aligned}
d \boldsymbol{\Psi}_{g} & =\mathbf{v} d t, d \mathbf{v}=\widetilde{f}\left(\boldsymbol{\Psi}_{g}\right) d t-\xi \mathbf{v} d t+\sqrt{D} d \mathcal{W} \\
d \xi & =\left(\frac{1}{M} \mathbf{v}^{T} \mathbf{v}-1\right) d t
\end{aligned}
$$

where $\widetilde{f}\left(\boldsymbol{\Psi}_{g}\right)=-\nabla_{\boldsymbol{\Psi}_{g}} \widetilde{U}\left(\boldsymbol{\Psi}_{g}\right)$ and $\widetilde{U}\left(\boldsymbol{\Psi}_{g}\right)$ is the negative log-posterior of the model. $t$ indexes time and $\mathcal{W}$ denotes the standard Wiener process. $\xi$ is the thermostats variable to make sure the system has a constant temperature. $D$ is the injected variance which is a constant.

### 4.3.3 Deep Poisson Factor Analysis with Restricted Boltzmann Machine

Similar to the deep PFA above, the restricted Boltzmann machine (RBM) [24] can be used in place of SBN [17]. If RBM is used, Equation (15) and (16) would be defined using the energy [24]:

$$
\begin{aligned}
E\left(\mathbf{h}_{n}^{(l)}, \mathbf{h}_{n}^{(l+1)}\right)= & -\mathbf{h}_{n}^{(l)} \mathbf{b}_{l}^{T}-\mathbf{h}_{n}^{(l)} \mathbf{W}^{(l)} \mathbf{h}_{n}^{(l+1)^{T}} \\
& -\mathbf{h}_{n}^{(l+1)} \mathbf{b}_{l+1}^{T}
\end{aligned}
$$

For the learning, similar algorithms as the deep PFA with SBN can be used. Specifically, the sampling process would alternate between $\left\{\left\{\boldsymbol{\phi}_{k}\right\},\left\{\gamma_{k}\right\}, \gamma_{0}\right\}$ and $\left\{\left\{\mathbf{W}_{l}\right\},\left\{\mathbf{b}_{l}\right\}\right\}$. For $\left\{\left\{\boldsymbol{\phi}_{k}\right\},\left\{\gamma_{k}\right\}, \gamma_{0}\right\}$, similar conditional density as the SBN-based DPFA is used. For $\left\{\left\{\mathbf{W}_{l}\right\},\left\{\mathbf{b}_{l}\right\}\right\}$, they use the contrastive divergence algorithm.

### 4.3.4 Discussion

In BDL-based topic models, the perception component is responsible for inferring the topic hierarchy from documents while the task-specific component is in charge of modeling the word generation, topic generation, word-topic relation, or inter-document relation. The synergy between these two components comes from the bidirectional interaction between them. On the one hand, knowledge
of the topic hierarchy would facilitate accurate modeling of words and topics, providing valuable information for learning inter-document relations. On the other hand, accurately modeling the words, topics, and inter-document relations could help with the discovery of topic hierarchy and learning of compact document representations.

As we can see, the information exchange mechanism in some BDL-based topic models is different from that in Section 4.2. For example, in the SBN-based DPFA model, the exchange is natural since the bottom layer of SBN, $\mathbf{H}_{1}$, and the relationship between $\mathbf{H}_{1}$ and $\boldsymbol{\Omega}_{h}=\{\mathbf{X}\}$ are both inherently probabilistic, as shown in Equation (16) and (17), which means additional assumptions about the distribution are not necessary. The SBN-based DPFA model is equivalent to assuming that $\mathbf{H}$ in PFA (see Equation (14)) is generated from a Dirac delta distribution (a Gaussian distribution with zero variance) centered at the bottom layer of the SBN, $\mathbf{H}_{1}$. Hence both DPFA models in Table 1 are ZV models, according to the definition in Section 4.1. It is worth noting that RSDAE is an HV model (see Equation (11), where $\mathbf{S}$ is the hinge variable and the others are perception variables), and naively modifying this model to be its ZV counterpart would violate the i.i.d. requirement in Section 4.1.

### 4.4 Other Applications

As mentioned in Section 1, BDL can also be applied to applications beyond data engineering and data mining (e.g., the control of nonlinear dynamical systems from raw images or medical diagnosis with medical images).

Consider controlling a complex dynamical system according to the live video stream received from a camera. One way of solving this control problem is by iteration between two tasks, perception from raw images and control based on dynamic models. The perception task can be taken care of using multiple layers of simple nonlinear transformation (deep learning) while the control task usually needs more sophisticated models such as hidden Markov models and Kalman filters [22], [42]. To enable an effective iterative process between the perception task and the control task, two-way information exchange between them is often necessary. The perception component would be the basis on which the control component estimates its states and on the other hand, the control component with a built-in dynamic model would be able to predict the future trajectory (images) by reversing the perception process. For example, [69] proposed a BDL-based model that performs control based on the received raw images (videos). Their key generative process is as follows:

$$
\begin{aligned}
\mathbf{z}_{t} & \sim \quad Q_{\phi}(Z \mid X)=\mathcal{N}\left(\boldsymbol{\mu}_{t}, \mathbf{\Sigma}_{t}\right) \\
\widetilde{\mathbf{z}}_{t+1} & \sim \quad \widetilde{Q}_{\psi}(\widetilde{Z} \mid Z, \mathbf{u})=\mathcal{N}\left(\mathbf{A}_{t} \boldsymbol{\mu}_{t}+\mathbf{B}_{t} \mathbf{u}_{t}+\mathbf{o}_{t}, \mathbf{C}_{t}\right) \\
\widetilde{\mathbf{x}}_{t}, \widetilde{\mathbf{x}}_{t+1} & \sim \quad P_{\theta}(X \mid Z)=\text { Bernoulli }\left(\mathbf{p}_{t}\right)
\end{aligned}
$$

where $Q_{\phi}(Z \mid X)$ is the encoding model which encodes the raw images $X$ into latent states $Z . \widetilde{Q}_{\psi}(\widetilde{Z} \mid Z, \mathbf{u})$ is the transition model which predicts the next latent state $\widetilde{Z}$ given the current latent state $Z$ and the applied control $\mathbf{u} . P_{\theta}(X \mid Z)$ is the reconstruction (decoding) model which reconstructs the raw images $X$ from latent states $Z$. The parameters $\boldsymbol{\mu}_{t}$, $\boldsymbol{\Sigma}_{t}, \mathbf{A}_{t}, \mathbf{B}_{t}, \mathbf{o}_{t}, \mathbf{C}_{t}$, and $\mathbf{p}_{t}$ are then further parameterized by neural networks.

It is worth noting that in terms of information exchange between the two components, this BDL-based control model uses a different mechanism from the ones in Section 4.2 and Section 4.3: it uses neural networks to separately parameterize the mean and covariance of hinge variables (e.g., $\mu_{t}$ and $\Sigma_{t}$ in the encoding model), which is more flexible (with more free parameters) than models such as CDL and CDR in Section 4.2, where Gaussian distributions with fixed variance are also used. Note that this BDL-based control model is an LV model, and since the covariance is assumed to be diagonal [69], the model still meets the i.i.d. requirement in Section 4.1.

## 5 CONCLUSIONS AND FUTURE RESEARCH

In this paper, we identified a current trend of merging probabilistic graphical models and neural networks (deep learning), proposed a BDL framework, and reviewed relevant recent work on BDL, which strives to combine the merits of PGM and NN by organically integrating them in a single principled probabilistic framework. To learn parameters in BDL, several algorithms have been proposed, ranging from block coordinate descent, Bayesian conditional density filtering, and stochastic gradient thermostats to stochastic gradient variational Bayes.

BDL has gained its popularity both from the success of PGM and from recent promising advances in deep learning. Since many real-world tasks involve both perception and inference, BDL is a natural choice for harnessing the perception ability from NN and the (causal and logical) inference ability from PGM. Although current applications of BDL focus on recommender systems, topic models, and stochastic optimal control, in the future, we can expect an increasing number of other applications such as link prediction, community detection, active learning, Bayesian reinforcement learning, and many other complex tasks that need interaction between perception and causal inference. In these complex tasks, BDL with interconnected perception components (to handle perception) and task-specific components (to handle inference/reasoning) possesses great performance-boosting potential. Besides, with the advances of efficient Bayesian neural networks (BNN), BDL with BNN as an important component is expected to be more and more scalable.

## PLACE

PHOTO
HERE

Dit-Yan Yeung received his BEng degree in electrical engineering and MPhil degree in computer science from the University of Hong Kong, and PhD degree in computer science from the University of Southern California. He started his academic career as an assistant professor at the Illinois Institute of Technology in Chicago. He then joined the Hong Kong University of Science and Technology where he is now a full professor in the Department of Computer science and Engineering, with joint appointment in the Department of Electronic and Computer Engineering. His research interests are in computational and statistical approaches to machine learning and artificial intelligence.