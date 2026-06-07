# A Survey on Bayesian Deep Learning 

HAO WANG, Massachusetts Institute of Technology, USA<br>DIT-YAN YEUNG, Hong Kong University of Science and Technology, Hong Kong

A comprehensive artificial intelligence system needs to not only perceive the environment with different "senses" (e.g., seeing and hearing) but also infer the world's conditional (or even causal) relations and corresponding uncertainty. The past decade has seen major advances in many perception tasks, such as visual object recognition and speech recognition, using deep learning models. For higher-level inference, however, probabilistic graphical models with their Bayesian nature are still more powerful and flexible. In recent years, Bayesian deep learning has emerged as a unified probabilistic framework to tightly integrate deep learning and Bayesian models. ${ }^{1}$ In this general framework, the perception of text or images using deep learning can boost the performance of higher-level inference and, in turn, the feedback from the inference process is able to enhance the perception of text or images. This survey provides a comprehensive introduction to Bayesian deep learning and reviews its recent applications on recommender systems, topic models, control, and so on. We also discuss the relationship and differences between Bayesian deep learning and other related topics, such as Bayesian treatment of neural networks.

CCS Concepts: $\cdot$ Mathematics of computing $\rightarrow$ Probabilistic representations; $\cdot$ Information systems $\rightarrow$ Data mining; $\cdot$ Computing methodologies $\rightarrow$ Neural networks;

Additional Key Words and Phrases: Deep learning, Bayesian networks, probabilistic graphical models, generative models

## ACM Reference format:

Hao Wang and Dit-Yan Yeung. 2020. A Survey on Bayesian Deep Learning. ACM Comput. Surv. 53, 5, Article 108 (September 2020), 37 pages.
https://doi.org/10.1145/3409383

## 1 INTRODUCTION

Over the past decade, deep learning has achieved significant success in many popular perception tasks, including visual object recognition, text understanding, and speech recognition. These tasks correspond to artificial intelligence (AI) systems' ability to see, read, and hear, respectively, and they are undoubtedly indispensable for AI to effectively perceive the environment. However, to build a practical and comprehensive AI system, simply being able to perceive is far from sufficient. It should, above all, possess the ability of thinking.



A typical example is medical diagnosis, which goes far beyond simple perception: besides seeing visible symptoms (or medical images from CT) and hearing descriptions from patients, a doctor also has to look for relations among all the symptoms and preferably infer their corresponding etiology. Only after that can the doctor provide medical advice for the patients. In this example, although the abilities of seeing and hearing allow the doctor to acquire information from the patients, it is the thinking part that defines a doctor. Specifically, the ability of thinking here could involve identifying conditional dependencies, causal inference, logic deduction, and dealing with uncertainty, which are apparently beyond the capability of conventional deep learning methods. Fortunately, another machine learning paradigm, probabilistic graphical models (PGM), excels at probabilistic or causal inference and at dealing with uncertainty. The problem is that PGM is not as good as deep learning models at perception tasks, which usually involve large-scale and high-dimensional signals (e.g., images and videos). To address this problem, it is therefore a natural choice to unify deep learning and PGM within a principled probabilistic framework, which we call Bayesian deep learning (BDL) in this article.

In the example above, the perception task involves perceiving the patient's symptoms (e.g., by seeing medical images), while the inference task involves handling conditional dependencies, causal inference, logic deduction, and uncertainty. With the principled integration in Bayesian deep learning, the perception task and inference task are regarded as a whole and can benefit from each other. Concretely, being able to see the medical image could help with the doctor's diagnosis and inference. However, diagnosis and inference can, in turn, help understand the medical image. Suppose the doctor may not be sure about what a dark spot in a medical image is, but if she is able to infer the etiology of the symptoms and disease, it can help her better decide whether the dark spot is a tumor or not.

Take recommender systems [1, 70, 71, 92, 121] as another example. A highly accurate recommender system requires (1) thorough understanding of item content (e.g., content in documents and movies) [85], (2) careful analysis of users' profiles/preferences [126, 130, 134], and (3) proper evaluation of similarity among users [3, 12, 46, 109]. Deep learning with its ability to efficiently process dense high-dimensional data such as movie content is good at the first subtask, while PGM specializing in modeling conditional dependencies among users, items, and ratings (see Figure 7 as an example, where $\mathbf{u}, \mathbf{v}$, and $\mathbf{R}$ are user latent vectors, item latent vectors, and ratings, respectively) excels at the other two. Hence, unifying them two in a single principled probabilistic framework gets us the best of both worlds. Such integration also comes with additional benefit that uncertainty in the recommendation process is handled elegantly. What is more, one can also derive Bayesian treatments for concrete models, leading to more robust predictions [68, 121].

As a third example, consider controlling a complex dynamical system according to the live video stream received from a camera. This problem can be transformed into iteratively performing two tasks, perception from raw images and control based on dynamic models. The perception task of processing raw images can be handled by deep learning while the control task usually needs more sophisticated models such as hidden Markov models and Kalman filters [35, 74]. The feedback loop is then completed by the fact that actions chosen by the control model can affect the received video stream in turn. To enable an effective iterative process between the perception task and the control task, we need information to flow back and forth between them. The perception component would be the basis on which the control component estimates its states and the control component with a dynamic model built in would be able to predict the future trajectory (images). Therefore Bayesian deep learning is a suitable choice [125] for this problem. Note that similar to the recommender system example, both noise from raw images and uncertainty in the control process can be naturally dealt with under such a probabilistic framework.

The above examples demonstrate BDL's major advantages as a principled way of unifying deep learning and PGM: information exchange between the perception task and the inference task, conditional dependencies on high-dimensional data, and effective modeling of uncertainty. In terms of uncertainty, it is worth noting that when BDL is applied to complex tasks, there are three kinds of parameter uncertainty that need to be taken into account:
(1) Uncertainty on the neural network parameters.
(2) Uncertainty on the task-specific parameters.
(3) Uncertainty of exchanging information between the perception component and the taskspecific component.

By representing the unknown parameters using distributions instead of point estimates, BDL offers a promising framework to handle these three kinds of uncertainty in a unified way. It is worth noting that the third uncertainty could only be handled under a unified framework like BDL; training the perception component and the task-specific component separately is equivalent to assuming no uncertainty when exchanging information between them two. Note that neural networks are usually over-parameterized and therefore pose additional challenges in efficiently handling the uncertainty in such a large parameter space. However, graphical models are often more concise and have smaller parameter space, providing better interpretability.

Besides the advantages above, another benefit comes from the implicit regularization built in BDL. By imposing a prior on hidden units, parameters defining a neural network, or the model parameters specifying the conditional dependencies, BDL can to some degree avoid overfitting, especially when we have insufficient data. Usually, a BDL model consists of two components, a perception component that is a Bayesian formulation of a certain type of neural networks and a task-specific component that describes the relationship among different hidden or observed variables using PGM. Regularization is crucial for them both. Neural networks are usually heavily over-parameterized and therefore needs to be regularized properly. Regularization techniques such as weight decay and dropout [103] are shown to be effective in improving performance of neural networks and they both have Bayesian interpretations [22]. In terms of the task-specific component, expert knowledge or prior information, as a kind of regularization, can be incorporated into the model through the prior we imposed to guide the model when data are scarce.

There are also challenges when applying BDL to real-world tasks. (1) First, it is nontrivial to design an efficient Bayesian formulation of neural networks with reasonable time complexity. This line of work is pioneered by References [42, 72, 80], but it has not been widely adopted due to its lack of scalability. Fortunately, some recent advances in this direction $[2,9,31,39,58,119,121]$ seem to shed light ${ }^{2}$ on the practical adoption of Bayesian neural network. ${ }^{3}$ (2) The second challenge is to ensure efficient and effective information exchange between the perception component and the task-specific component. Ideally, both the first-order and second-order information (e.g., the mean and the variance) should be able to flow back and forth between the two components. A natural way is to represent the perception component as a PGM and seamlessly connect it to the task-specific PGM, as done in References [24, 118, 121].

[^0]
[^0]:    ${ }^{2}$ In summary, reduction in time complexity can be achieved via expectation propagation [39], the reparameterization trick [9, 58], probabilistic formulation of neural networks with maximum a posteriori estimates [121], approximate variational inference with natural-parameter networks [119], knowledge distillation [2], and so on. We refer readers to Reference [119] for a detailed overview.
    ${ }^{3}$ Here, we refer to the Bayesian treatment of neural networks as Bayesian neural networks. The other term, Bayesian deep learning, is retained to refer to complex Bayesian models with both a perception component and a task-specific component. See Section 4.1 for a detailed discussion.

This survey provides a comprehensive overview of BDL with concrete models for various applications. The rest of the survey is organized as follows: In Section 2, we provide a review of some basic deep learning models. Section 3 covers the main concepts and techniques for PGM. These two sections serve as the preliminaries for BDL, and the next section, Section 4, demonstrates the rationale for the unified BDL framework and details various choices for implementing its perception component and task-specific component. Section 5 reviews the BDL models applied to various areas such as recommender systems, topic models, and control, showcasing how BDL works in supervised learning, unsupervised learning, and general representation learning, respectively. Section 6 discusses some future research issues and concludes the article.

# 2 DEEP LEARNING 

Deep learning normally refers to neural networks with more than two layers. To better understand deep learning, here we start with the simplest type of neural networks, multilayer perceptrons (MLP), as an example to show how conventional deep learning works. After that, we will review several other types of deep learning models based on MLP.

### 2.1 Multilayer Perceptrons

Essentially, a multilayer perceptron is a sequence of parametric nonlinear transformations. Suppose we want to train a multilayer perceptron to perform a regression task that maps a vector of $M$ dimensions to a vector of $D$ dimensions. We denote the input as a matrix $\mathrm{X}_{0}$ ( 0 means it is the 0 th layer of the perceptron). The $j$ th row of $\mathrm{X}_{0}$, denoted as $\mathrm{X}_{0, j *}$, is an $M$-dimensional vector representing one data point. The target (the output we want to fit) is denoted as Y. Similarly, $\mathrm{Y}_{j *}$ denotes a $D$-dimensional row vector. The problem of learning an $L$-layer multilayer perceptron can be formulated as the following optimization problem:

$$
\begin{gathered}
\min _{\left\{\mathbf{W}_{I}\right\},\left\{\mathbf{b}_{I}\right\}}\left\|\mathbf{X}_{L}-\mathbf{Y}\right\|_{F}+\lambda \sum_{I}\left\|\mathbf{W}_{I}\right\|_{F}^{2} \\
\text { subject to } \mathbf{X}_{I}=\sigma\left(\mathbf{X}_{I-1} \mathbf{W}_{I}+\mathbf{b}_{I}\right), l=1, \ldots, L-1 \\
\mathbf{X}_{L}=\mathbf{X}_{L-1} \mathbf{W}_{L}+\mathbf{b}_{L}
\end{gathered}
$$

where $\sigma(\cdot)$ is an element-wise sigmoid function for a matrix and $\sigma(x)=\frac{1}{1+\exp (-x)} \cdot\|\cdot\|_{F}$ denotes the Frobenius norm. The purpose of imposing $\sigma(\cdot)$ is to allow nonlinear transformation. Normally other transformations like $\tanh (x)$ and $\max (0, x)$ can be used as alternatives of the sigmoid function.

Here, $\mathbf{X}_{I}(l=1,2, \ldots, L-1)$ is the hidden units. As we can see, $\mathbf{X}_{L}$ can be easily computed once $\mathbf{X}_{0}, \mathbf{W}_{I}$, and $\mathbf{b}_{I}$ are given. Since $\mathbf{X}_{0}$ is given as input, one only needs to learn $\mathbf{W}_{I}$ and $\mathbf{b}_{I}$ here. Usually this is done using backpropagation and stochastic gradient descent (SGD). The key is to compute the gradients of the objective function with respect to $\mathbf{W}_{I}$ and $\mathbf{b}_{I}$. Denoting the value of the objective function as $E$, one can compute the gradients using the chain rule as

$$
\begin{aligned}
& \frac{\partial E}{\partial \mathbf{X}_{L}}=2\left(\mathbf{X}_{L}-\mathbf{Y}\right), \quad \frac{\partial E}{\partial \mathbf{X}_{I}}=\left(\frac{\partial E}{\partial \mathbf{X}_{I+1}} \circ \mathbf{X}_{I+1} \circ\left(1-\mathbf{X}_{I+1}\right)\right) \mathbf{W}_{I+1} \\
& \frac{\partial E}{\partial \mathbf{W}_{I}}=\mathbf{X}_{I-1}^{T}\left(\frac{\partial E}{\partial \mathbf{X}_{I}} \circ \mathbf{X}_{I} \circ\left(1-\mathbf{X}_{I}\right)\right), \quad \frac{\partial E}{\partial \mathbf{b}_{I}}=\operatorname{mean}\left(\frac{\partial E}{\partial \mathbf{X}_{I}} \circ \mathbf{X}_{I} \circ\left(1-\mathbf{X}_{I}\right), 1\right)
\end{aligned}
$$

where $l=1, \ldots, L$ and the regularization terms are omitted. $\circ$ denotes the element-wise product and mean $(\cdot, 1)$ is the matlab operation on matrices. In practice, we only use a small part of the data (e.g., 128 data points) to compute the gradients for each update. This is called stochastic gradient descent.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Left: A two-layer SDAE with $L=4$. Right: A convolutional layer with four input feature maps and two output feature maps.

As we can see, in conventional deep learning models, only $\mathbf{W}_{I}$ and $\mathbf{b}_{I}$ are free parameters, which we will update in each iteration of the optimization. $\mathbf{X}_{I}$ is not a free parameter, since it can be computed exactly if $\mathbf{W}_{I}$ and $\mathbf{b}_{I}$ are given.

# 2.2 Autoencoders 

An autoencoder (AE) is a feedforward neural network to encode the input into a more compact representation and reconstruct the input with the learned representation. In its simplest form, an autoencoder is no more than a multilayer perceptron with a bottleneck layer (a layer with a small number of hidden units) in the middle. The idea of autoencoders has been around for decades [10, 29, 43, 63] and abundant variants of autoencoders have been proposed to enhance representation learning, including sparse AE [88], contrastive AE [93], and denoising AE [111]. For more details, please refer to a recent book on deep learning [29]. Here, we introduce a kind of multilayer denoising AE, known as stacked denoising autoencoders (SDAE), both as an example of AE variants and as background for its applications on BDL-based recommender systems in Section 4.

SDAE [111] is a feedforward neural network for learning representations (encoding) of the input data by learning to predict the clean input itself in the output, as shown in Figure 1 (left). The hidden layer in the middle, i.e., $\mathbf{X}_{2}$ in the figure, can be constrained to be a bottleneck to learn compact representations. The difference between traditional AE and SDAE is that the input layer $\mathbf{X}_{0}$ is a corrupted version of the clean input data $\mathbf{X}_{c}$. Essentially, an SDAE solves the following optimization problem:

$$
\begin{gathered}
\min _{\left\{\mathbf{W}_{I}\right\},\left\{\mathbf{b}_{I}\right\}}\left\|\mathbf{X}_{c}-\mathbf{X}_{L}\right\|_{F}^{2}+\lambda \sum_{I}\left\|\mathbf{W}_{I}\right\|_{F}^{2} \\
\text { subject to } \mathbf{X}_{I}=\sigma\left(\mathbf{X}_{I-1} \mathbf{W}_{I}+\mathbf{b}_{I}\right), l=1, \ldots, L-1 \\
\mathbf{X}_{L}=\mathbf{X}_{L-1} \mathbf{W}_{L}+\mathbf{b}_{L}
\end{gathered}
$$

where $\lambda$ is a regularization parameter. Here, SDAE can be regarded as a multilayer perceptron for regression tasks described in the previous section. The input $\mathbf{X}_{0}$ of the MLP is the corrupted version of the data and the target $\mathbf{Y}$ is the clean version of the data $\mathbf{X}_{c}$. For example, $\mathbf{X}_{c}$ can be the raw data matrix, and we can randomly set $30 \%$ of the entries in $\mathbf{X}_{c}$ to 0 and get $\mathbf{X}_{0}$. In a nutshell, SDAE learns a neural network that takes the noisy data as input and recovers the clean data in the last layer. This is what "denoising" in the name means. Normally, the output of the middle layer, i.e., $\mathbf{X}_{2}$ in Figure 1(left), would be used to compactly represent the data.

### 2.3 Convolutional Neural Networks

Convolutional neural networks (CNN) can be viewed as another variant of MLP. Different from AE, which is initially designed to perform dimensionality reduction, CNN is biologically inspired.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Left: A conventional feedforward neural network with one hidden layer, where $\mathbf{x}$ is the input, $\mathbf{z}$ is the hidden layer, and $\mathbf{o}$ is the output, $\mathbf{W}$ and $\mathbf{V}$ are the corresponding weights (biases are omitted here). Middle: A recurrent neural network with input $\left\{\mathbf{x}_{t}\right\}_{t=1}^{T}$, hidden states $\left\{\mathbf{h}_{t}\right\}_{t=1}^{T}$, and output $\left\{\mathbf{o}_{t}\right\}_{t=1}^{T}$. Right: An unrolled RNN that is equivalent to the one in Figure 2 (middle). Here, each node (e.g., $\mathbf{x}_{1}, \mathbf{h}_{1}$, or $\mathbf{o}_{1}$ ) is associated with one particular time step.

According to Reference [53], two types of cells have been identified in the cat's visual cortex. One is simple cells that respond maximally to specific patterns within their receptive field, and the other is complex cells with larger receptive field that are considered locally invariant to positions of patterns. Inspired by these findings, the two key concepts in CNN are then developed: convolution and max-pooling.

Convolution: In CNN, a feature map is the result of the convolution of the input and a linear filter, followed by some element-wise nonlinear transformation. The input here can be the raw image or the feature map from the previous layer. Specifically, with input $\mathbf{X}$, weights $\mathbf{W}^{k}$, bias $b^{k}$, the $k$ th feature map $\mathbf{H}^{k}$ can be obtained as follows:

$$
\mathbf{H}_{i j}^{k}=\tanh \left(\left(\mathbf{W}^{k} * \mathbf{X}\right)_{i j}+b^{k}\right)
$$

Note that in the equation above, we assume one single input feature map and multiple output feature maps. In practice, CNN often has multiple input feature maps as well due to its deep structure. A convolutional layer with four input feature maps and two output feature maps is shown in Figure 1 (right).

Max-Pooling: Traditionally, a convolutional layer in CNN is followed by a max-pooling layer, which can be seen as a type of nonlinear downsampling. The operation of max-pooling is simple. For example, if we have a feature map of size $6 \times 9$, then the result of max-pooling with a $3 \times 3$ region would be a downsampled feature map of size $2 \times 3$. Each entry of the downsampled feature map is the maximum value of the corresponding $3 \times 3$ region in the $6 \times 9$ feature map. Max-pooling layers can not only reduce computational cost by ignoring the non-maximal entries but also provide local translation invariance.

Putting it all together: Usually to form a complete and working CNN, the input would alternate between convolutional layers and max-pooling layers before going into an MLP for tasks such as classification or regression. One classic example is the LeNet-5 [64], which alternates between two convolutional layers and two max-pooling layers before going into a fully connected MLP for target tasks.

# 2.4 Recurrent Neural Network 

When reading an article, one normally takes in one word at a time and try to understand the current word based on previous words. This is a recurrent process that needs short-term memory. Unfortunately conventional feedforward neural networks like the one shown in Figure 2 (left) fail to do so. For example, imagine we want to constantly predict the next word as we read an article. Since the feedforward network only computes the output $\mathbf{o}$ as $\mathbf{V} q(\mathbf{W} \mathbf{x})$, where the function $q(\cdot)$

denotes element-wise nonlinear transformation, it is unclear how the network could naturally model the sequence of words to predict the next word.
2.4.1 Vanilla Recurrent Neural Network. To solve the problem, we need a recurrent neural network [29] instead of a feedforward one. As shown in Figure 2 (middle), the computation of the current hidden states $\mathbf{h}_{t}$ depends on the current input $\mathbf{x}_{t}$ (e.g., the $t$ th word) and the previous hidden states $\mathbf{h}_{t-1}$. This is why there is a loop in the RNN. It is this loop that enables short-term memory in RNNs. The $\mathbf{h}_{t}$ in the RNN represents what the network knows so far at the $t$ th time step. To see the computation more clearly, we can unroll the loop and represent the RNN as in Figure 2 (right). If we use hyperbolic tangent nonlinearity ( $\tanh$ ), then the computation of output $\mathbf{o}_{t}$ will be as follows:

$$
\mathbf{a}_{t}=\mathbf{W} \mathbf{h}_{t-1}+\mathbf{Y} \mathbf{x}_{t}+\mathbf{b}, \quad \mathbf{h}_{t}=\tanh \left(\mathbf{a}_{t}\right), \quad \mathbf{o}_{t}=\mathbf{V} \mathbf{h}_{t}+\mathbf{c}
$$

where $\mathbf{Y}, \mathbf{W}$, and $\mathbf{V}$ denote the weight matrices for input-to-hidden, hidden-to-hidden, and hidden-to-output connections, respectively, and $\mathbf{b}$ and $\mathbf{c}$ are the corresponding biases. If the task is to classify the input data at each time step, then we can compute the classification probability as $\mathbf{p}_{t}=\operatorname{softmax}\left(\mathbf{o}_{t}\right)$, where

$$
\operatorname{softmax}(\mathbf{q})=\frac{\exp (\mathbf{q})}{\sum_{i} \exp \left(\mathbf{q}_{i}\right)}
$$

Similar to feedforward networks, an RNN is trained with a generalized back-propagation algorithm called back-propagation through time (BPTT) [29]. Essentially, the gradients are computed through the unrolled network as shown in Figure 2 (right) with shared weights and biases for all time steps.
2.4.2 Gated Recurrent Neural Network. The problem with the vanilla RNN above is that the gradients propagated over many time steps are prone to vanish or explode, making the optimization notoriously difficult. In addition, the signal passing through the RNN decays exponentially, making it impossible to model long-term dependencies in long sequences. Imagine we want to predict the last word in the paragraph "I have many books... I like reading." To get the answer, we need "long-term memory" to retrieve information (the word "books") at the start of the text. To address this problem, the long short-term memory model (LSTM) is designed as a type of gated RNN to model and accumulate information over a relatively long duration. The intuition behind LSTM is that when processing a sequence consisting of several subsequences, it is sometimes useful for the neural network to summarize or forget the old states before moving on to process the next subsequence [29]. Using $t=1 \ldots T_{j}$ to index the words in the sequence, the formulation of LSTM is as follows (we drop the item index $j$ for notational simplicity):

$$
\mathbf{x}_{t}=\mathbf{W}_{w} \mathbf{e}_{t}, \quad \mathbf{s}_{t}=\mathbf{h}_{t-1}^{f} \odot \mathbf{s}_{t-1}+\mathbf{h}_{t-1}^{i} \odot \sigma\left(\mathbf{Y} \mathbf{x}_{t-1}+\mathbf{W} \mathbf{h}_{t-1}+\mathbf{b}\right)
$$

where $\mathbf{x}_{t}$ is the word embedding of the $t$ th word, $\mathbf{W}_{w}$ is a $K_{W}$-by- $S$ word embedding matrix, and $\mathbf{e}_{t}$ is the 1-of- $S$ representation, $\odot$ stands for the element-wise product operation between two vectors, $\sigma(\cdot)$ denotes the sigmoid function, $\mathbf{s}_{t}$ is the cell state of the $t$ th word, and $\mathbf{b}, \mathbf{Y}$, and $\mathbf{W}$ denote the biases, input weights, and recurrent weights, respectively. The forget gate units $\mathbf{h}_{t}^{f}$ and the input gate units $\mathbf{h}_{t}^{i}$ in Equation (1) can be computed using their corresponding weights and biases $\mathbf{Y}^{f}$, $\mathbf{W}^{f}, \mathbf{Y}^{i}, \mathbf{W}^{i}, \mathbf{b}^{f}$, and $\mathbf{b}^{i}$ :

$$
\mathbf{h}_{t}^{f}=\sigma\left(\mathbf{Y}^{f} \mathbf{x}_{t}+\mathbf{W}^{f} \mathbf{h}_{t}+\mathbf{b}^{f}\right), \quad \mathbf{h}_{t}^{i}=\sigma\left(\mathbf{Y}^{i} \mathbf{x}_{t}+\mathbf{W}^{i} \mathbf{h}_{t}+\mathbf{b}^{i}\right)
$$

The output depends on the output gate $\mathbf{h}_{t}^{o}$, which has its own weights and biases $\mathbf{Y}^{o}, \mathbf{W}^{o}$, and $\mathbf{b}^{o}$ :

$$
\mathbf{h}_{t}=\tanh \left(\mathbf{s}_{t}\right) \odot \mathbf{h}_{t-1}^{o}, \quad \mathbf{h}_{t}^{o}=\sigma\left(\mathbf{Y}^{o} \mathbf{x}_{t}+\mathbf{W}^{o} \mathbf{h}_{t}+\mathbf{b}^{o}\right)
$$

![img-2.jpeg](img-2.jpeg)

Fig. 3. The encoder-decoder architecture involving two LSTMs. The encoder LSTM (in the left rectangle) encodes the sequence "ABC" into a representation and the decoder LSTM (in the right rectangle) recovers the sequence from the representation. "slash dollar" marks the end of a sentence.
![img-3.jpeg](img-3.jpeg)

Fig. 4. The probabilistic graphical model for LDA, $J$ is the number of documents, $D$ is the number of words in a document, and $K$ is the number of topics.

Note that in the LSTM, information of the processed sequence is contained in the cell states $\mathbf{s}_{t}$ and the output states $\mathbf{h}_{t}$, both of which are column vectors of length $K_{W}$.

Similar to References [16, 108], we can use the output state and cell state at the last time step ( $\mathbf{h}_{T_{j}}$ and $\mathbf{s}_{T_{j}}$ ) of the first LSTM as the initial output state and cell state of the second LSTM. This way the two LSTMs can be concatenated to form an encoder-decoder architecture, as shown in Figure 3.

Note that there is a vast literature on deep learning and neural networks. The introduction in this section intends to serve only as the background of Bayesian deep learning. Readers are referred to Reference [29] for a comprehensive survey and more details.

# 3 PROBABILISTIC GRAPHICAL MODELS 

Probabilistic Graphical Models (PGM) use diagrammatic representations to describe random variables and relationships among them. Similar to a graph that contains nodes (vertices) and links (edges), PGM has nodes to represent random variables and links to indicate probabilistic relationships among them.

### 3.1 Models

There are essentially two types of PGM, directed PGM (also known as Bayesian networks) and undirected PGM (also known as Markov random fields) [5]. In this survey, we mainly focus on directed PGM. ${ }^{4}$ For details on undirected PGM, readers are referred to Reference [5].

A classic example of PGM would be latent Dirichlet allocation (LDA), which is used as a topic model to analyze the generation of words and topics in documents [8]. Usually PGM comes with a graphical representation of the model and a generative process to depict the story of how the random variables are generated step by step. Figure 4 shows the graphical model for LDA and the corresponding generative process is as follows:

- For each document $j(j=1,2, \ldots, J)$,
(1) Draw topic proportions $\theta_{j} \sim \operatorname{Dirichlet}(\alpha)$.
(2) For each word $w_{j n}$ of item (document) $\mathbf{w}_{j}$,
(a) Draw topic assignment $z_{j n} \sim \operatorname{Mult}\left(\theta_{j}\right)$,
(b) Draw word $w_{j n} \sim \operatorname{Mult}\left(\beta_{z_{j n}}\right)$.

[^0]
[^0]:    ${ }^{4}$ For convenience, PGM stands for directed PGM in this survey unless specified otherwise.

The generative process above provides the story of how the random variables are generated. In the graphical model in Figure 4, the shaded node denotes observed variables while the others are latent variables $(\boldsymbol{\theta}$ and $\mathbf{z})$ or parameters ( $\alpha$ and $\beta$ ). Once the model is defined, learning algorithms can be applied to automatically learn the latent variables and parameters.

Due to its Bayesian nature, PGM such as LDA is easy to extend to incorporate other information or to perform other tasks. For example, following LDA, different variants of topic models have been proposed. References $[7,113]$ are proposed to incorporate temporal information, and Reference [6] extends LDA by assuming correlations among topics. Reference [44] extends LDA from the batch mode to the online setting, making it possible to process large datasets. On recommender systems, collaborative topic regression (CTR) [112] extends LDA to incorporate rating information and make recommendations. This model is then further extended to incorporate social information $[89,115,116]$.

# 3.2 Inference and Learning 

Strictly speaking, the process of finding the parameters (e.g., $\alpha$ and $\beta$ in Figure 4) is called learning and the process of finding the latent variables (e.g., $\boldsymbol{\theta}$ and $\mathbf{z}$ in Figure 4) given the parameters is called inference. However, given only the observed variables (e.g., w in Figure 4), learning and inference are often intertwined. Usually the learning and inference of LDA would alternate between the updates of latent variables (which correspond to inference) and the updates of the parameters (which correspond to learning). Once the learning and inference of LDA is completed, one could obtain the learned parameters $\alpha$ and $\beta$. If a new document comes, then one can now fix the learned $\alpha$ and $\beta$ and then perform inference alone to find the topic proportions $\theta_{j}$ of the new document. ${ }^{5}$

Similar to LDA, various learning and inference algorithms are available for each PGM. Among them, the most cost-effective one is probably maximum a posteriori (MAP), which amounts to maximizing the posterior probability of the latent variable. Using MAP, the learning process is equivalent to minimizing (or maximizing) an objective function with regularization. One famous example is the probabilistic matrix factorization (PMF) [96], where the learning of the graphical model is equivalent to factorizing a large matrix into two low-rank matrices with L2 regularization.

MAP, as efficient as it is, gives us only point estimates of latent variables (and parameters). To take the uncertainty into account and harness the full power of Bayesian models, one would have to resort to Bayesian treatments such as variational inference and Markov chain Monte Carlo (MCMC). For example, the original LDA uses variational inference to approximate the true posterior with factorized variational distributions [8]. Learning of the latent variables and parameters then boils down to minimizing the KL-divergence between the variational distributions and the true posterior distributions. Besides variational inference, another choice for a Bayesian treatment is MCMC. For example, MCMC algorithms such as Reference [86] have been proposed to learn the posterior distributions of LDA.

## 4 BAYESIAN DEEP LEARNING

With the preliminaries on deep learning and PGM, we are now ready to introduce the general framework and some concrete examples of BDL. Specifically, in this section, we will list some recent BDL models with applications on recommender systems, topic models, control, and so on. A summary of these models is shown in Table 1.

[^0]
[^0]:    ${ }^{5}$ For convenience, we use "learning" to represent both "learning and inference" in the following text.

Table 1. Summary of BDL Models with Different Learning Algorithms (MAP: Maximum a Posteriori, VI: Variational Inference, Hybrid MC: Hybrid Monte Carlo) and Different Variance Types (ZV: Zero-Variance, HV: Hyper-Variance, LV: Learnable-Variance)


# 4.1 A Brief History of Bayesian Neural Networks and Bayesian Deep Learning 

One topic highly related to BDL is Bayesian neural networks (BNN) or Bayesian treatments of neural networks. Similar to any Bayesian treatment, BNN imposes a prior on the neural network's parameters and aims to learn a posterior distribution of these parameters. During the inference phrase, such a distribution is then marginalized out to produce final predictions. In general such a process is called Bayesian model averaging [5] and can be seen as learning an infinite number of (or a distribution over) neural networks and then aggregating the results through ensembling.

The study of BNN dates back to 1990s with notable works from References [42, 72, 80]. Over the years, a large body of works $[2,9,31,39,58,100]$ have emerged to enable substantially better

![img-4.jpeg](img-4.jpeg)

Fig. 5. The PGM for an example BDL. The red rectangle on the left indicates the perception component, and the blue rectangle on the right indicates the task-specific component. The hinge variable $\Omega_{h}=\{\mathbf{H}\}$.
scalability and incorporate recent advancements of deep neural networks. Due to BNN's long history, the term "Bayesian deep learning" sometimes specifically refers to "Bayesian neural networks" [73, 128]. In this survey, we instead use "Bayesian deep learning" in a broader sense to refer to the probabilistic framework subsuming Bayesian neural networks. To see this, note that a BDL model with a perception component and an empty task-specific component is equivalent to a Bayesian neural network (details on these two components are discussed in Section 4.2).

Interestingly, though BNN started in 1990s, the study of BDL in a broader sense started roughly in 2014 [38, 114, 118, 121], slightly after the deep learning breakthrough in the ImageNet LSVRC contest in 2012 [62]. As we will see in later sections, BNN is usually used as a perception component in BDL models.

Today BDL is gaining more and more popularity, has found successful applications in areas such as recommender systems and computer vision, and appears as the theme of various conference workshops (e.g., the NeurIPS BDL workshop ${ }^{6}$ ).

# 4.2 General Framework 

As mentioned in Section 1, BDL is a principled probabilistic framework with two seamlessly integrated components: a perception component and a task-specific component.

Two Components: Figure 5 shows the PGM of a simple BDL model as an example. The part inside the red rectangle on the left represents the perception component and the part inside the blue rectangle on the right is the task-specific component. Typically, the perception component would be a probabilistic formulation of a deep learning model with multiple nonlinear processing layers represented as a chain structure in the PGM. While the nodes and edges in the perception component are relatively simple, those in the task-specific component often describe more complex distributions and relationships among variables. Concretely, a task-specific component can take various forms. For example, it can be a typical Bayesian network (directed PGM) such as LDA, a deep Bayesian network [117], or a stochastic process [51, 94], all of which can be represented in the form of PGM.

Three Variable Sets: There are three sets of variables in a BDL model: perception variables, hinge variables, and task variables. In this article, we use $\Omega_{p}$ to denote the set of perception variables (e.g., $\mathbf{X}_{0}, \mathbf{X}_{1}$, and $\mathbf{W}_{1}$ in Figure 5), which are the variables in the perception component. Usually $\Omega_{p}$ would include the weights and neurons in the probabilistic formulation of a deep learning model. $\Omega_{h}$ is used to denote the set of hinge variables (e.g., H in Figure 5). These variables directly interact with the perception component from the task-specific component. The set of task variables (e.g., A, B, and C in Figure 5), i.e., variables in the task-specific component without direct relation to the perception component, is denoted as $\Omega_{t}$.

[^0]
[^0]:    ${ }^{6}$ http://bayesiandeeplearning.org/.

Generative Processes for Supervised and Unsupervised Learning: If the edges between the two components point toward $\Omega_{h}$, then the joint distribution of all variables can be written as

$$
p\left(\Omega_{p}, \Omega_{h}, \Omega_{t}\right)=p\left(\Omega_{p}\right) p\left(\Omega_{h} \mid \Omega_{p}\right) p\left(\Omega_{t} \mid \Omega_{h}\right)
$$

If the edges between the two components originate from $\Omega_{h}$, then the joint distribution of all variables can be written as

$$
p\left(\Omega_{p}, \Omega_{h}, \Omega_{t}\right)=p\left(\Omega_{t}\right) p\left(\Omega_{h} \mid \Omega_{t}\right) p\left(\Omega_{p} \mid \Omega_{h}\right)
$$

Equations (2) and (3) assume different generative processes for the data and correspond to different learning tasks. The former is usually used for supervised learning, where the perception component serves as a probabilistic (or Bayesian) representation learner to facilitate any downstream tasks (see Section 5.1 for some examples). The latter is usually used for unsupervised learning, where the task-specific component provides structured constraints and domain knowledge to help the perception component learn stronger representations (see Section 5.2 for some examples).

Note that besides these two vanilla cases, it is possible for BDL to simultaneously have some edges between the two components pointing towards $\Omega_{h}$ and some originating from $\Omega_{h}$, in which case the decomposition of the joint distribution would be more complex.

Independence Requirement: The introduction of hinge variables $\Omega_{h}$ and related conditional distributions simplifies the model (especially when $\Omega_{h}$ 's in-degree or out-degree is 1), facilitate learning, and provides inductive bias to concentrate information inside $\Omega_{h}$. Note that hinge variables are always in the task-specific component; the connections between hinge variables $\Omega_{h}$ and the perception component (e.g., $\mathrm{X}_{4} \rightarrow \mathrm{H}$ in Figure 5) should normally be independent for convenience of parallel computation in the perception component. For example, each row in $\mathbf{H}$ is related to only one corresponding row in $\mathbf{X}_{4}$. Although it is not mandatory in BDL models, meeting this requirement would significantly increase the efficiency of parallel computation in model training.

Flexibility of Variance for $\Omega_{h}$ : As mentioned in Section 1, one of BDL's motivations is to model the uncertainty of exchanging information between the perception component and the taskspecific component, which boils down to modeling the uncertainty related to $\Omega_{h}$. For example, such uncertainty is reflected in the variance of the conditional density $p\left(\Omega_{h} \mid \Omega_{p}\right)$ in Equation (2). ${ }^{7}$ According to the degree of flexibility, there are three types of variance for $\Omega_{h}$ (for simplicity, we assume the joint likelihood of BDL is Equation (2), $\Omega_{p}=\{p\}, \Omega_{h}=\{h\}$, and $p\left(\Omega_{h} \mid \Omega_{p}\right)=$ $\mathcal{N}\left(h \mid \mu_{p}, \sigma_{p}^{2}\right)$ in our example):

- Zero-Variance: Zero-Variance (ZV) assumes no uncertainty during the information exchange between the two components. In the example, zero-variance means directly setting $\sigma_{p}^{2}$ to 0 .
- Hyper-Variance: Hyper-Variance (HV) assumes that uncertainty during the information exchange is defined through hyperparameters. In the example, HV means that $\sigma_{p}^{2}$ is a manually tuned hyperparameter.
- Learnable Variance: Learnable Variance (LV) uses learnable parameters to represent uncertainty during the information exchange. In the example, $\sigma_{p}^{2}$ is the learnable parameter.

As shown above, we can see that in terms of model flexibility, $\mathrm{LV}>\mathrm{HV}>\mathrm{ZV}$. Normally, if properly regularized, an LV model outperforms an HV model, which is superior to a ZV model. In Table 1, we show the types of variance for $\Omega_{h}$ in different BDL models. Note that although each

[^0]
[^0]:    ${ }^{7}$ For models with the joint likelihood decomposed as in Equation (3), the uncertainty is reflected in the variance of $p\left(\Omega_{p} \mid \Omega_{h}\right)$.

model in the table has a specific type, one can always adjust the models to devise their counterparts of other types. For example, while CDL in the table is an HV model, we can easily adjust $p\left(\Omega_{h} \mid \Omega_{p}\right)$ in CDL to devise its ZV and LV counterparts. In Reference [121], the authors compare the performance of an HV CDL and a ZV CDL and find that the former performs significantly better, meaning that sophisticatedly modeling uncertainty between two components is essential for performance.

Learning Algorithms: Due to the nature of BDL, practical learning algorithms need to meet the following criteria:
(1) They should be online algorithms to scale well for large datasets.
(2) They should be efficient enough to scale linearly with the number of free parameters in the perception component.

Criterion (1) implies that conventional variational inference or MCMC methods are not applicable. Usually an online version of them is needed [45]. Most SGD-based methods do not work either unless only MAP inference (as opposed to Bayesian treatments) is performed. Criterion (2) is needed because there are typically a large number of free parameters in the perception component. This means methods based on Laplace approximation [72] are not realistic, since they involve the computation of a Hessian matrix that scales quadratically with the number of free parameters.

# 4.3 Perception Component 

Ideally, the perception component should be a probabilistic or Bayesian neural network, to be compatible with the task-specific component, which is probabilistic in nature. This is to ensure the perception component's built-in capability to handle uncertainty of parameters and its output.

As mentioned in Section 4.1, the study of Bayesian neural networks dates back to 1990s [31, 42, 72, 80]. However, pioneering work at that time was not widely adopted due to its lack of scalability. To address the this issue, there has been recent development such as restricted Boltzmann machine (RBM) [40, 41], probabilistic generalized stacked denoising autoencoders (pSDAE) [118, 121], variational autoencoders (VAE) [58], probabilistic back-propagation (PBP) [39], Bayes by Backprop (BBB) [9], Bayesian dark knowledge (BDK) [2], and natural-parameter networks (NPN) [119].

More recently, generative adversarial networks (GAN) [30] prevail as a new training scheme for training neural networks and have shown promise in generating photo-realistic images. Later on, Bayesian formulations (as well as related theoretical results) for GAN have also been proposed [30, 37]. These models are also potential building blocks as the BDL framework's perception component.

In this subsection, we mainly focus on the introduction of recent Baysian neural networks such as RBM, pSDAE, VAE, and NPN. We refer the readers to Reference [29] for earlier work in this direction.
4.3.1 Restricted Boltzmann Machine. Restricted Boltzmann Machine (RBM) is a special kind of BNN in that (1) it is not trained with back-propagation (BP) and that (2) its hidden neurons are binary. Specifically, RBM defines the following energy:

$$
E(\mathbf{v}, \mathbf{h})=-\mathbf{v}^{T} \mathbf{W} \mathbf{h}-\mathbf{v}^{T} \mathbf{b}-\mathbf{h}^{T} \mathbf{a}
$$

where $\mathbf{v}$ denotes visible (observed) neurons, and $\mathbf{h}$ denotes binary hidden neurons. $\mathbf{W}, \mathbf{a}$, and $\mathbf{b}$ are learnable weights. The energy function leads to the following conditional distributions:

$$
p(\mathbf{v} \mid \mathbf{h})=\frac{\exp (-E(\mathbf{v}, \mathbf{h}))}{\sum_{\mathbf{v}} \exp (-E(\mathbf{v}, \mathbf{h}))}, \quad p(\mathbf{h} \mid \mathbf{v})=\frac{\exp (-E(\mathbf{v}, \mathbf{h}))}{\sum_{\mathbf{h}} \exp (-E(\mathbf{v}, \mathbf{h}))}
$$

RBM is trained using "Contrastive Divergence" [40] rather than BP. Once trained, RBM can infer $\mathbf{v}$ or $\mathbf{h}$ by marginalizing out other neurons. One can also stack layers of RBM to form a deep belief network (DBN) [76], use multiple branches of deep RBN for multimodal learning [104], or combine DBN with convolutional layers to form a convolutional DBN [65].
4.3.2 Probabilistic Generalized SDAE. Following the introduction of SDAE in Section 2.2, if we assume that both the clean input $\mathbf{X}_{c}$ and the corrupted input $\mathbf{X}_{0}$ are observed, similar to References $[4,5,13,72]$, then we can define the following generative process of the probabilistic SDAE:
(1) For each layer $l$ of the SDAE network,
(a) For each column $n$ of the weight matrix $\mathbf{W}_{l}$, draw $\mathbf{W}_{l, * n} \sim \mathcal{N}\left(\mathbf{0}, \lambda_{w}^{-1} \mathbf{I}_{K_{l}}\right)$,
(b) Draw the bias vector $\mathbf{b}_{l} \sim \mathcal{N}\left(\mathbf{0}, \lambda_{w}^{-1} \mathbf{I}_{K_{l}}\right)$,
(c) For each row $j$ of $\mathbf{X}_{l}$, draw

$$
\mathbf{X}_{l, j *} \sim \mathcal{N}\left(\sigma\left(\mathbf{X}_{l-1, j *} \mathbf{W}_{l}+\mathbf{b}_{l}\right), \lambda_{s}^{-1} \mathbf{I}_{K_{l}}\right)
$$

(2) For each item $j$, draw a clean input ${ }^{8} \mathbf{X}_{c, j *} \sim \mathcal{N}\left(\mathbf{X}_{L, j *}, \lambda_{n}^{-1} \mathbf{I}_{B}\right)$.

Note that if $\lambda_{s}$ goes to infinity, the Gaussian distribution in Equation (5) will become a Dirac delta distribution [106] centered at $\sigma\left(\mathbf{X}_{l-1, j *} \mathbf{W}_{l}+\mathbf{b}_{l}\right)$, where $\sigma(\cdot)$ is the sigmoid function, and the model will degenerate into a Bayesian formulation of vanilla SDAE. This is why we call it "generalized" SDAE.

The first $L / 2$ layers of the network act as an encoder and the last $L / 2$ layers act as a decoder. Maximization of the posterior probability is equivalent to minimization of the reconstruction error with weight decay taken into consideration.

Following pSDAE, both its convolutional version [132] and its recurrent version [122] have been proposed with applications in knowledge base embedding and recommender systems.
4.3.3 Variational Autoencoders. Variational Autoencoders (VAE) [58] essentially tries to learn parameters $\phi$ and $\theta$ that maximize the evidence lower bound (ELBO):

$$
\mathcal{L}_{\text {vae }}=E_{q_{\phi}(\mathbf{z} \mid \mathbf{x})}\left[\log p_{\theta}(\mathbf{x} \mid \mathbf{z})\right]-K L\left(q_{\phi}(\mathbf{z} \mid \mathbf{x}) \| p(\mathbf{z})\right)
$$

where $q_{\phi}(\mathbf{z} \mid \mathbf{x})$ is the encoder parameterized by $\phi$ and $p_{\theta}(\mathbf{x} \mid \mathbf{z})$ is the decoder parameterized by $\theta$. The negation of the first term is similar to the reconstruction error in vanilla AE, while the KL divergence works as a regularization term for the encoder. During training $q_{\phi}(\mathbf{z} \mid \mathbf{x})$ will output the mean and variance of a Gaussian distribution, from which $\mathbf{z}$ is sampled via the reparameterization trick. Usually $q_{\phi}(\mathbf{z} \mid \mathbf{x})$ is parameterized by an MLP with two branches, one producing the mean and the other producing the variance.

Similar to the case of pSDAE, various VAE variants have been proposed. For example, Importance weighted Autoencoders (IWAE) [11] derived a tighter lower bound via importance weighting, Reference [129] combined LSTM, VAE, and dilated CNN for text modeling, and Reference [17] proposed a recurrent version of VAE dubbed variational RNN (VRNN).
4.3.4 Natural-parameter Networks. Different from vanilla NN, which usually takes deterministic input, NPN [119] is a probabilistic NN taking distributions as input. The input distributions go through layers of linear and nonlinear transformation to produce output distributions. In NPN, all hidden neurons and weights are also distributions expressed in closed form. Note that this is in contrast to VAE where only the middle layer output $\mathbf{z}$ is a distribution.

[^0]
[^0]:    ${ }^{8}$ Note that while generation of the clean input $\mathbf{X}_{c}$ from $\mathbf{X}_{L}$ is part of the generative process of the Bayesian SDAE, generation of the noise-corrupted input $\mathbf{X}_{0}$ from $\mathbf{X}_{c}$ is an artificial noise injection process to help the SDAE learn a more robust feature representation.

As a simple example, in a vanilla linear $\mathrm{NN} f_{w}(x)=w x$ takes a scalar $x$ as input and computes the output based on a scalar parameter $w$; a corresponding Gaussian NPN would assume $w$ is drawn from a Gaussian distribution $\mathcal{N}\left(w_{m}, w_{s}\right)$ and that $x$ is drawn from $\mathcal{N}\left(x_{m}, x_{s}\right)\left(x_{s}\right.$ is set to 0 when the input is deterministic). With $\theta=\left(w_{m}, w_{s}\right)$ as a learnable parameter pair, NPN will then compute the mean and variance of the output Gaussian distribution $\mu_{\theta}\left(x_{m}, x_{s}\right)$ and $s_{\theta}\left(x_{m}, x_{s}\right)$ in closed form (bias terms are ignored for clarity) as

$$
\begin{gathered}
\mu_{\theta}\left(x_{m}, x_{s}\right)=E[w x]=x_{m} w_{m} \\
s_{\theta}\left(x_{m}, x_{s}\right)=D[w x]=x_{s} w_{s}+x_{s} w_{m}^{2}+x_{m}^{2} w_{s}
\end{gathered}
$$

Hence, the output of this Gaussian NPN is a tuple $\left(\mu_{\theta}\left(x_{m}, x_{s}\right), s_{\theta}\left(x_{m}, x_{s}\right)\right)$ representing a Gaussian distribution instead of a single value. Input variance $x_{s}$ to NPN can be set to 0 if not available. Note that since $s_{\theta}\left(x_{m}, 0\right)=x_{m}^{2} w_{s}, w_{m}$ and $w_{s}$ can still be learned even if $x_{s}=0$ for all data points. The derivation above is generalized to handle vectors and matrices in practice [119]. Besides Gaussian distributions, NPN also support other exponential-family distributions such as Poisson distributions and gamma distributions [119].

Following NPN, a light-weight version [26] was proposed to speed up the training and inference process. Another variant, MaxNPN [100], extended NPN to handle max-pooling and categorical layers. ConvNPN [87] enables convolutional layers in NPN. In terms of model quantization and compression, BinaryNPN [107] was also proposed as NPN's binary version to achieve better efficiency.

# 4.4 Task-Specific Component 

In this subsection, we introduce different forms of task-specific components. The purpose of a task-specific component is to incorporate probabilistic prior knowledge into the BDL model. Such knowledge can be naturally represented using PGM. Concretely, it can be a typical (or shallow) Bayesian network [5, 54], a bidirectional inference network [117], or a stochastic process [94].
4.4.1 Bayesian Networks. Bayesian networks are the most common choice for a task-specific component. As mentioned in Section 3, Bayesian networks can naturally represent conditional dependencies and handle uncertainty. Besides LDA introduced above, a more straightforward example is probabilistic matrix factorization (PMF) [96], where one uses a Bayesian network to describe the conditional dependencies among users, items, and ratings. Specifically, PMF assumes the following generative process:
(1) For each item $j$, draw a latent item vector: $\mathbf{v}_{i} \sim \mathcal{N}\left(\mathbf{0}, \lambda_{v}^{-1} \mathbf{I}_{K}\right)$.
(2) For each user $i$, draw a latent user vector: $\mathbf{u}_{i} \sim \mathcal{N}\left(\mathbf{0}, \lambda_{u}^{-1} \mathbf{I}_{K}\right)$.
(3) For each user-item pair $(i, j)$, draw a rating: $\mathbf{R}_{i j} \sim \mathcal{N}\left(\mathbf{u}_{i}^{T} \mathbf{v}_{j}, \mathbf{C}_{i j}^{-1}\right)$.

In the generative process above, $\mathbf{C}_{i j}^{-1}$ is the corresponding variance for the rating $\mathbf{R}_{i j}$. Using MAP estimates, learning PMF amounts to maximize the following log-likelihood of $p\left(\left\{\mathbf{u}_{i}\right\},\left\{\mathbf{v}_{j}\right\} \mid\left\{\mathbf{R}_{i j}\right\},\left\{\mathbf{C}_{i j}\right\}, \lambda_{u}, \lambda_{v}\right):$

$$
\mathscr{L}=-\frac{\lambda_{u}}{2} \sum_{i}\left\|\mathbf{u}_{i}\right\|_{2}^{2}-\frac{\lambda_{v}}{2} \sum_{j}\left\|\mathbf{v}_{j}\right\|_{2}^{2}-\sum_{i, j} \frac{\mathbf{C}_{i j}}{2}\left(\mathbf{R}_{i j}-\mathbf{u}_{i}^{T} \mathbf{v}_{j}\right)^{2}
$$

Note that one can also impose another layer of priors on the hyperparameters with a fully Bayesian treatment. For example, Reference [97] imposes priors on the precision matrix of latent factors and learn the Bayesian PMF with Gibbs sampling.

In Section 5.1, we will show how PMF can be used as a task-specific component along with a perception component defined to significantly improve recommender systems' performance.

![img-5.jpeg](img-5.jpeg)

Fig. 6. Left: A simple example of BIN with each conditional distribution parameterized by a Bayesian neural networks (BNN) or simply a probabilistic neural network. Right: Another example BIN. Shaded and transparent nodes indicate observed and unobserved variables, respectively.
4.4.2 Bidirectional Inference Networks. Typical Bayesian networks assume "shallow" conditional dependencies among random variables. In the generative process, one random variable (which can be either latent or observed) is usually drawn from a conditional distribution parameterized by the linear combination of its parent variables. For example, in PMF the rating $\mathbf{R}_{i j}$ is drawn from a Gaussian distribution mainly parameterized by the linear combination of $\mathbf{u}_{i}$ and $\mathbf{v}_{j}$, i.e., $\mathbf{R}_{i j} \sim \mathcal{N}\left(\mathbf{u}_{i}^{T} \mathbf{v}_{j}, \mathbf{C}_{i j}^{-1}\right)$.

Such "shallow" and linear structures can be replaced with nonlinear or even deep nonlinear structures to form a deep Bayesian network. As an example, bidirectional inference network (BIN) [117] is a class of deep Bayesian networks that enable deep nonlinear structures in each conditional distribution, while retaining the ability to incorporate prior knowledge as Bayesian networks.

For example, Figure 6 (left) shows a BIN, where each conditional distribution is parameterized by a Bayesian neural network. Specifically, this example assumes the following factorization:

$$
p\left(v_{1}, v_{2}, v_{3} \mid X\right)=p\left(v_{1} \mid X\right) p\left(v_{2} \mid X, v_{1}\right) p\left(v_{3} \mid X, v_{1}, v_{2}\right)
$$

A vanilla Bayesian network parameterizes each distribution with simple linear operations. For example, $p\left(v_{2} \mid X, v_{1}\right)=\mathcal{N}\left(v_{2} \mid X w_{0}+v_{1} w_{1}+b, \sigma^{2}\right)$ ). In contrast, BIN (as a deep Bayesian network) uses a BNN. For example, BIN has $p\left(v_{2} \mid X, v_{1}\right)=\mathcal{N}\left(v_{2} \mid \mu_{\theta}\left(X, v_{1}\right), s_{\theta}\left(X, v_{1}\right)\right)$, where $\mu_{\theta}\left(X, v_{1}\right)$ and $s_{\theta}\left(X, v_{1}\right)$ are the output mean and variance of the BNN. The inference and learning of such a deep Bayesian network is done by performing BP across all BNNs (e.g., BNN 1, 2, and 3 in Figure 6 (left)) [117].

Compared to vanilla (shallow) Bayesian networks, deep Bayesian networks such as BIN make it possible to handle deep and nonlinear conditional dependencies effectively and efficiently. Besides, with BNN as building blocks, task-specific components based on deep Bayesian networks can better work with the perception component, which is usually a BNN as well. Figure 6 (right) shows a more complicated case with both observed (shaded nodes) and unobserved (transparent nodes) variables.
4.4.3 Stochastic Processes. Besides vanilla Bayesian networks and deep Bayesian networks, a task-specific component can also take the form of a stochastic process [94]. For example, a Wiener process can naturally describe a continuous-time Brownian motion model $\mathbf{x}_{t+u} \mid \mathbf{x}_{t} \sim \mathcal{N}\left(\mathbf{x}_{t}, \lambda u \mathbf{I}\right)$, where $\mathbf{x}_{t+u}$ and $\mathbf{x}_{t}$ are the states at time $t$ and $t+u$, respectively. In the graphical model literature, such a process has been used to model the continuous-time topic evolution of articles over time [113].

Another example is to model phonemes' boundary positions using a Poisson process in automatic speech recognition (ASR) [51]. Note that this is a fundamental problem in ASR, since speech is no more than a sequence of phonemes. Specifically, a Poisson process defines the generative process $\Delta t_{i}=t_{i}-t_{i-1} \sim g(\lambda(t))$, with $\mathcal{T}=\left\{t_{1}, t_{2}, \ldots, t_{N}\right\}$ as the set of boundary positions, and $g(\lambda(t))$

is a exponential distribution with the parameter $\lambda(t)$ (also known as the intensity). Such a stochastic process naturally models the occurrence of phoneme boundaries in continuous time. The parameter $\lambda(t)$ can be the output of a neural network taking raw speech signals as input [51, 83, 99].

Interestingly, stochastic processes can be seen as a type of dynamic Bayesian networks. To see this, we can rewrite the Poisson process above in an equivalent form, where given $t_{i-1}$, the probability that $t_{i}$ has not occurred at time $t, P\left(t_{i}>t\right)=\exp \left(\int_{t_{i-1}}^{t}-\lambda(t) d t\right)$. Obviously, both the Wiener process and the Poisson process are Markovian and can be represented with a dynamic Bayesian network [78].

For clarity, we focus on using vanilla Bayesian networks as task-specific components in Section 5; they can be naturally replaced with other types of task-specific components to represent different prior knowledge if necessary.

# 5 CONCRETE BDL MODELS AND APPLICATIONS 

In this section, we discuss how the BDL framework can facilitate supervised learning, unsupervised learning, and representation learning in general. Concretely, we use examples in domains such as recommender systems, topic models, control, and so on.

### 5.1 Supervised Bayesian Deep Learning for Recommender Systems

Despite the successful applications of deep learning on natural language processing and computer vision, very few attempts have been made to develop deep learning models for collaborative filtering (CF) before the emergence of BDL. Reference [98] uses restricted Boltzmann machines instead of the conventional matrix factorization formulation to perform CF and Reference [28] extends this work by incorporating user-user and item-item correlations. Although these methods involve both deep learning and CF, they actually belong to CF-based methods, because they ignore users' or items' content information, which is crucial for accurate recommendation. Reference [95] uses low-rank matrix factorization in the last weight layer of a deep network to significantly reduce the number of model parameters and speed up training, but it is for classification instead of recommendation tasks. On music recommendation, References [84, 123] directly use conventional CNN or deep belief networks (DBN) to assist representation learning for content information, but the deep learning components of their models are deterministic without modeling the noise and hence they are less robust. The models achieve performance boost mainly by loosely coupled methods without exploiting the interaction between content information and ratings. Besides, the CNN is linked directly to the rating matrix, which means the models will perform poorly due to serious overfitting when the ratings are sparse.
5.1.1 Collaborative Deep Learning. To address the challenges above, a hierarchical Bayesian model called collaborative deep learning (CDL) as a novel tightly coupled method for recommender systems is introduced in Reference [121]. Based on a Bayesian formulation of SDAE, CDL tightly couples deep representation learning for the content information and collaborative filtering for the rating (feedback) matrix, allowing two-way interaction between the two. From BDL's perspective, a probabilistic SDAE as the perception component is tightly coupled with a probabilistic graphical model as the task-specific component. Experiments show that CDL significantly improves upon the state of the art.

In the following text, we will start with the introduction of the notation used during our presentation of CDL. After that, we will review the design and learning of CDL.

Notation and Problem Formulation: Similar to the work in Reference [112], the recommendation task considered in CDL takes implicit feedback [50] as the training and test data. The entire collection of $J$ items (articles or movies) is represented by a $J$-by- $B$ matrix $\mathbf{X}_{c}$, where row $j$ is the

![img-6.jpeg](img-6.jpeg)

Fig. 7. On the left is the graphical model of CDL. The part inside the dashed rectangle represents an SDAE. An example SDAE with $L=2$ is shown. On the right is the graphical model of the degenerated CDL. The part inside the dashed rectangle represents the encoder of an SDAE. An example SDAE with $L=2$ is shown on its right. Note that although $L$ is still 2, the decoder of the SDAE vanishes. To prevent clutter, we omit all variables $\mathbf{x}_{I}$, except $\mathbf{x}_{0}$ and $\mathbf{x}_{L / 2}$ in the graphical models.
bag-of-words vector $\mathbf{X}_{c, j *}$ for item $j$ based on a vocabulary of size $B$. With $I$ users, we define an $I$-by- $J$ binary rating matrix $\mathbf{R}=\left[\mathbf{R}_{i j}\right]_{I \times J}$. For example, in the dataset citeulike-a [112, 115, 121], $\mathbf{R}_{i j}=1$ if user $i$ has article $j$ in his or her personal library and $\mathbf{R}_{i j}=0$ otherwise. Given part of the ratings in $\mathbf{R}$ and the content information $\mathbf{X}_{c}$, the problem is to predict the other ratings in $\mathbf{R}$. Note that although CDL in its current from focuses on movie recommendation (where plots of movies are considered as content information) and article recommendation like Reference [112] in this section, it is general enough to handle other recommendation tasks (e.g., tag recommendation).

The matrix $\mathbf{X}_{c}$ plays the role of clean input to the SDAE while the noise-corrupted matrix, also a $J$-by- $B$ matrix, is denoted by $\mathbf{X}_{0}$. The output of layer $l$ of the SDAE is denoted by $\mathbf{X}_{I}$, which is a $J$-by- $K_{I}$ matrix. Similar to $\mathbf{X}_{c}$, row $j$ of $\mathbf{X}_{I}$ is denoted by $\mathbf{X}_{l, j *} . \mathbf{W}_{I}$ and $\mathbf{b}_{I}$ are the weight matrix and bias vector, respectively, of layer $l, \mathbf{W}_{l, * n}$ denotes column $n$ of $\mathbf{W}_{I}$, and $L$ is the number of layers. For convenience, we use $\mathbf{W}^{+}$to denote the collection of all layers of weight matrices and biases. Note that an $L / 2$-layer SDAE corresponds to an $L$-layer network.

Collaborative Deep Learning: Using the probabilistic SDAE in Section 4.3.2 as a component, the generative process of CDL is defined as follows:
(1) For each layer $l$ of the SDAE network,
(a) For each column $n$ of the weight matrix $\mathbf{W}_{I}$, draw $\mathbf{W}_{l, * n} \sim \mathcal{N}\left(\mathbf{0}, \lambda_{w}^{-1} \mathbf{I}_{K_{I}}\right)$,
(b) Draw the bias vector $\mathbf{b}_{I} \sim \mathcal{N}\left(\mathbf{0}, \lambda_{w}^{-1} \mathbf{I}_{K_{I}}\right)$,
(c) For each row $j$ of $\mathbf{X}_{I}$, draw $\mathbf{X}_{l, j *} \sim \mathcal{N}\left(\sigma\left(\mathbf{X}_{l-1, j *} \mathbf{W}_{I}+\mathbf{b}_{I}\right), \lambda_{s}^{-1} \mathbf{I}_{K_{I}}\right)$.
(2) For each item $j$,
(a) Draw a clean input $\mathbf{X}_{c, j *} \sim \mathcal{N}\left(\mathbf{X}_{L, j *}, \lambda_{u}^{-1} \mathbf{I}_{J}\right)$,
(b) Draw the latent item offset vector $\epsilon_{j} \sim \mathcal{N}\left(\mathbf{0}, \lambda_{v}^{-1} \mathbf{I}_{K}\right)$ and then set the latent item vector: $\mathbf{v}_{j}=\epsilon_{j}+\mathbf{X}_{\frac{L}{2}, j *}^{T}$.
(3) Draw a latent user vector for each user $i$ : $\mathbf{u}_{i} \sim \mathcal{N}\left(\mathbf{0}, \lambda_{u}^{-1} \mathbf{I}_{K}\right)$.
(4) Draw a rating $\mathbf{R}_{i j}$ for each user-item pair $(i, j): \mathbf{R}_{i j} \sim \mathcal{N}\left(\mathbf{u}_{i}^{T} \mathbf{v}_{j}, \mathbf{C}_{i j}^{-1}\right)$.

Here, $\lambda_{w}, \lambda_{n}, \lambda_{u}, \lambda_{s}$, and $\lambda_{v}$ are hyperparameters and $\mathbf{C}_{i j}$ is a confidence parameter similar to that for CTR [112] ( $\mathbf{C}_{i j}=a$ if $\mathbf{R}_{i j}=1$ and $\mathbf{C}_{i j}=b$, otherwise). Note that the middle layer $\mathbf{X}_{L / 2}$ serves as a bridge between the ratings and content information. This middle layer, along with the latent offset $\epsilon_{j}$, is the key that enables CDL to simultaneously learn an effective feature representation and capture the similarity and (implicit) relationship among items (and users). Similar to the generalized SDAE, we can also take $\lambda_{s}$ to infinity for computational efficiency.

![img-7.jpeg](img-7.jpeg)

Fig. 8. Left: NN representation for degenerated CDL. Right: Sampling as generalized BP in Bayesian CDL.
The graphical model of CDL when $\lambda_{s}$ approaches positive infinity is shown in Figure 7, where, for notational simplicity, we use $\mathbf{x}_{0}, \mathbf{x}_{L / 2}$, and $\mathbf{x}_{L}$ in place of $\mathbf{X}_{0, j *}^{T}, \mathbf{X}_{\frac{L}{2}, j *}^{T}$, and $\mathbf{X}_{L, j *}^{T}$, respectively.

Note that according the definition in Section 4.2, here the perception variables $\Omega_{p}=$ $\left\{\left\{\mathbf{W}_{I}\right\},\left\{\mathbf{b}_{I}\right\},\left\{\mathbf{X}_{I}\right\}, \mathbf{X}_{c}\right\}$, the hinge variables $\Omega_{h}=\{\mathbf{V}\}$, and the task variables $\Omega_{t}=\{\mathbf{U}, \mathbf{R}\}$.

Learning: Based on the CDL model above, all parameters could be treated as random variables so that fully Bayesian methods such as Markov chain Monte Carlo (MCMC) or variational inference [55] may be applied. However, such treatment typically incurs high computational cost. Therefore, CDL uses an EM-style algorithm to obtain the MAP estimates, as in Reference [112].

Concretely, note that maximizing the posterior probability is equivalent to maximizing the joint log-likelihood of $\mathbf{U}, \mathbf{V},\left\{\mathbf{X}_{I}\right\}, \mathbf{X}_{c},\left\{\mathbf{W}_{I}\right\},\left\{\mathbf{b}_{I}\right\}$, and $\mathbf{R}$ given $\lambda_{u}, \lambda_{v}, \lambda_{w}, \lambda_{s}$, and $\lambda_{n}$ :

$$
\begin{aligned}
\mathscr{L}= & -\frac{\lambda_{u}}{2} \sum_{i}\left\|\mathbf{u}_{i}\right\|_{2}^{2}-\frac{\lambda_{w}}{2} \sum_{i}\left(\left\|\mathbf{W}_{i}\right\|_{F}^{2}+\left\|\mathbf{b}_{i}\right\|_{2}^{2}\right)-\frac{\lambda_{v}}{2} \sum_{j}\left\|\mathbf{v}_{j}-\mathbf{X}_{\frac{L}{2}, j *}^{T}\right\|_{2}^{2}-\frac{\lambda_{n}}{2} \sum_{j}\left\|\mathbf{X}_{L, j *}-\mathbf{X}_{c, j *}\right\|_{2}^{2} \\
& -\frac{\lambda_{s}}{2} \sum_{i} \sum_{j}\left\|\sigma\left(\mathbf{X}_{l-1, j *} \mathbf{W}_{l}+\mathbf{b}_{l}\right)-\mathbf{X}_{l, j *}\right\|_{2}^{2}-\sum_{i, j} \frac{\mathbf{C}_{i j}}{2}\left(\mathbf{R}_{i j}-\mathbf{u}_{i}^{T} \mathbf{v}_{j}\right)^{2}
\end{aligned}
$$

If $\lambda_{s}$ goes to infinity, then the likelihood becomes

$$
\begin{aligned}
\mathscr{L}= & -\frac{\lambda_{u}}{2} \sum_{i}\left\|\mathbf{u}_{i}\right\|_{2}^{2}-\frac{\lambda_{w}}{2} \sum_{i}\left(\left\|\mathbf{W}_{i}\right\|_{F}^{2}+\left\|\mathbf{b}_{i}\right\|_{2}^{2}\right)-\frac{\lambda_{v}}{2} \sum_{j}\left\|\mathbf{v}_{j}-f_{e}\left(\mathbf{X}_{0, j *}, \mathbf{W}^{+}\right)^{T}\right\|_{2}^{2} \\
& -\frac{\lambda_{n}}{2} \sum_{i}\left\|f_{r}\left(\mathbf{X}_{0, j *}, \mathbf{W}^{+}\right)-\mathbf{X}_{c, j *}\right\|_{2}^{2}-\sum_{i, j} \frac{\mathbf{C}_{i j}}{2}\left(\mathbf{R}_{i j}-\mathbf{u}_{i}^{T} \mathbf{v}_{j}\right)^{2}
\end{aligned}
$$

where the encoder function $f_{e}\left(\cdot, \mathbf{W}^{+}\right)$takes the corrupted content vector $\mathbf{X}_{0, j *}$ of item $j$ as input and computes its encoding, and the function $f_{r}\left(\cdot, \mathbf{W}^{+}\right)$also takes $\mathbf{X}_{0, j *}$ as input, computes the encoding and then reconstructs item $j$ 's content vector. For example, if the number of layers $L=6$, $f_{e}\left(\mathbf{X}_{0, j *}, \mathbf{W}^{+}\right)$is the output of the third layer while $f_{r}\left(\mathbf{X}_{0, j *}, \mathbf{W}^{+}\right)$is the output of the sixth layer.

From the perspective of optimization, the third term in the objective function, i.e., Equation (9), above is equivalent to a multi-layer perceptron using the latent item vectors $\mathbf{v}_{j}$ as the target while the fourth term is equivalent to an SDAE minimizing the reconstruction error. Seeing from the view of neural networks (NN), when $\lambda_{s}$ approaches positive infinity, training of the probabilistic graphical model of CDL in Figure 7 (left) would degenerate to simultaneously training two neural networks overlaid together with a common input layer (the corrupted input) but different output layers, as shown in Figure 8 (left). Note that the second network is much more complex than typical neural networks due to the involvement of the rating matrix.

When the ratio $\lambda_{n} / \lambda_{v}$ approaches positive infinity, it will degenerate to a two-step model in which the latent representation learned using SDAE is put directly into the CTR. Another extreme happens when $\lambda_{n} / \lambda_{v}$ goes to zero where the decoder of the SDAE essentially vanishes. Figure 7 (right) shows the graphical model of the degenerated CDL when $\lambda_{n} / \lambda_{v}$ goes to zero. As demonstrated in experiments, the predictive performance will suffer greatly for both extreme cases [121].

For $\mathbf{u}_{i}$ and $\mathbf{v}_{j}$, block coordinate descent similar to References [50, 112] is used. Given the current $\mathbf{W}^{+}$, we compute the gradients of $\mathscr{L}$ with respect to $\mathbf{u}_{i}$ and $\mathbf{v}_{j}$ and then set them to zero, leading to the following update rules:

$$
\mathbf{u}_{i} \leftarrow\left(\mathbf{V C}_{i} \mathbf{V}^{T}+\lambda_{u} \mathbf{I}_{K}\right)^{-1} \mathbf{V C}_{i} \mathbf{R}_{i}, \quad \mathbf{v}_{j} \leftarrow\left(\mathbf{U C}_{i} \mathbf{U}^{T}+\lambda_{v} \mathbf{I}_{K}\right)^{-1}\left(\mathbf{U C}_{j} \mathbf{R}_{j}+\lambda_{v} f_{e}\left(\mathbf{X}_{0, j *}, \mathbf{W}^{+}\right)^{T}\right)
$$

where $\mathbf{U}=\left(\mathbf{u}_{i}\right)_{i=1}^{I}, \mathbf{V}=\left(\mathbf{v}_{j}\right)_{j=1}^{J}, \mathbf{C}_{i}=\operatorname{diag}\left(\mathbf{C}_{i 1}, \ldots, \mathbf{C}_{i J}\right)$ is a diagonal matrix, $\mathbf{R}_{i}=\left(\mathbf{R}_{i 1}, \ldots, \mathbf{R}_{i J}\right)^{T}$ is a column vector containing all the ratings of user $i$, and $\mathbf{C}_{i j}$ reflects the confidence controlled by $a$ and $b$ as discussed in Reference [50]. $\mathbf{C}_{j}$ and $\mathbf{R}_{j}$ are defined similarly for item $j$.

Given $\mathbf{U}$ and $\mathbf{V}$, we can learn the weights $\mathbf{W}_{I}$ and biases $\mathbf{b}_{I}$ for each layer using the backpropagation learning algorithm. The gradients of the likelihood with respect to $\mathbf{W}_{I}$ and $\mathbf{b}_{I}$ are as follows:

$$
\begin{aligned}
\nabla_{\mathbf{W}_{I}} \mathscr{L}= & -\lambda_{w} \mathbf{W}_{I}-\lambda_{v} \sum_{j} \nabla_{\mathbf{W}_{I}} f_{e}\left(\mathbf{X}_{0, j *}, \mathbf{W}^{+}\right)^{T}\left(f_{e}\left(\mathbf{X}_{0, j *}, \mathbf{W}^{+}\right)^{T}-\mathbf{v}_{j}\right) \\
& -\lambda_{n} \sum_{j} \nabla_{\mathbf{W}_{I}} f_{r}\left(\mathbf{X}_{0, j *}, \mathbf{W}^{+}\right)\left(f_{r}\left(\mathbf{X}_{0, j *}, \mathbf{W}^{+}\right)-\mathbf{X}_{c, j *}\right) \\
\nabla_{\mathbf{b}_{I}} \mathscr{L}= & -\lambda_{w} \mathbf{b}_{I}-\lambda_{v} \sum_{j} \nabla_{\mathbf{b}_{I}} f_{e}\left(\mathbf{X}_{0, j *}, \mathbf{W}^{+}\right)^{T}\left(f_{e}\left(\mathbf{X}_{0, j *}, \mathbf{W}^{+}\right)^{T}-\mathbf{v}_{j}\right) \\
& -\lambda_{n} \sum_{j} \nabla_{\mathbf{b}_{I}} f_{r}\left(\mathbf{X}_{0, j *}, \mathbf{W}^{+}\right)\left(f_{r}\left(\mathbf{X}_{0, j *}, \mathbf{W}^{+}\right)-\mathbf{X}_{c, j *}\right)
\end{aligned}
$$

By alternating the update of $\mathbf{U}, \mathbf{V}, \mathbf{W}_{I}$, and $\mathbf{b}_{I}$, we can find a local optimum for $\mathscr{L}$. Several commonly used techniques such as using a momentum term may be applied to alleviate the local optimum problem.

Prediction: Let $D$ be the observed test data. Similar to Reference [112], CDL uses the point estimates of $\mathbf{u}_{i}, \mathbf{W}^{+}$and $\epsilon_{j}$ to calculate the predicted rating:

$$
E\left[\mathbf{R}_{i j} \mid D\right] \approx E\left[\mathbf{u}_{i} \mid D\right]^{T}\left(E\left[f_{e}\left(\mathbf{X}_{0, j *}, \mathbf{W}^{+}\right)^{T} \mid D\right]+E\left[\epsilon_{j} \mid D\right]\right)
$$

where $E[\cdot]$ denotes the expectation operation. In other words, we approximate the predicted rating as

$$
\mathbf{R}_{i j}^{*} \approx\left(\mathbf{u}_{j}^{*}\right)^{T}\left(f_{e}\left(\mathbf{X}_{0, j *}, \mathbf{W}^{+*}\right)^{T}+\epsilon_{j}^{*}\right)=\left(\mathbf{u}_{i}^{*}\right)^{T} \mathbf{v}_{j}^{*}
$$

Note that for any new item $j$ with no rating in the training data, its offset $\epsilon_{j}^{*}$ will be $\mathbf{0}$.
Recall that in CDL, the probabilistic SDAE and PMF work as the perception and task-specific components. As mentioned in Section 4, both components can take various forms, leading to different concrete models. For example, one can replace the probabilistic SDAE with a VAE or an NPN as the perception component [68]. It is also possible to use Bayesian PMF [97] rather than PMF [96] as the task-specific component and thereby produce more robust predictions.

In the following subsections, we provide several extensions of CDL from different perspectives.

5.1.2 Bayesian Collaborative Deep Learning. Besides the MAP estimates, a sampling-based algorithm for the Bayesian treatment of CDL is also proposed in Reference [121]. This algorithm turns out to be a Bayesian and generalized version of BP. We list the key conditional densities as follows:

For $\mathbf{W}^{+}$: We denote the concatenation of $\mathbf{W}_{l, * n}$ and $\mathbf{b}_{l}^{(n)}$ as $\mathbf{W}_{l, * n}^{+}$. Similarly, the concatenation of $\mathbf{X}_{l, j *}$ and 1 is denoted as $\mathbf{X}_{l, j *}^{+}$. The subscripts of $\mathbf{I}$ are ignored. Then,

$$
p\left(\mathbf{W}_{l, * n}^{+}\left|\mathbf{X}_{l-1, j *}, \mathbf{X}_{l, j *}, \lambda_{s}\right) \propto \mathcal{N}\left(\mathbf{W}_{l, * n}^{+}\left|0, \lambda_{w}^{-1} \mathbf{I}\right) \cdot \mathcal{N}\left(\mathbf{X}_{l, * n}\left|\sigma\left(\mathbf{X}_{l-1}^{+} \mathbf{W}_{l, * n}^{+}\right), \lambda_{s}^{-1} \mathbf{I}\right)\right.\right.
$$

For $\mathbf{X}_{l, j *}(l \neq L / 2)$ : Similarly, we denote the concatenation of $\mathbf{W}_{l}$ and $\mathbf{b}_{l}$ as $\mathbf{W}_{l}^{+}$and have

$$
\begin{aligned}
& p\left(\mathbf{X}_{l, j *}\left|\mathbf{W}_{l}^{+}, \mathbf{W}_{l+1}^{+}, \mathbf{X}_{l-1, j *}, \mathbf{X}_{l+1, j *} \lambda_{s}\right)\right. \\
\propto & \left.\mathcal{N}\left(\mathbf{X}_{l, j *}\left|\sigma\left(\mathbf{X}_{l-1, j *}^{+} \mathbf{W}_{l}^{+}\right), \lambda_{s}^{-1} \mathbf{I}\right) \cdot \mathcal{N}\left(\mathbf{X}_{l+1, j *}\left|\sigma\left(\mathbf{X}_{l, j *}^{+} \mathbf{W}_{l+1}^{+}\right), \lambda_{s}^{-1} \mathbf{I}\right)\right.\right.
\end{aligned}
$$

where for the last layer $(l=L)$ the second Gaussian would be $\mathcal{N}\left(\mathbf{X}_{c, j *}\left|\mathbf{X}_{l, j *}, \lambda_{s}^{-1} \mathbf{I}\right)\right.$ instead.
For $\mathbf{X}_{l, j *}(l=L / 2)$ : Similarly, we have

$$
\begin{aligned}
& p\left(\mathbf{X}_{l, j *}\left|\mathbf{W}_{l}^{+}, \mathbf{W}_{l+1}^{+}, \mathbf{X}_{l-1, j *}, \mathbf{X}_{l+1, j *}, \lambda_{s}, \lambda_{v}, \mathbf{v}_{j}\right)\right. \\
\propto & \left.\mathcal{N}\left(\mathbf{X}_{l, j *}\left|\sigma\left(\mathbf{X}_{l-1, j *}^{+} \mathbf{W}_{l}^{+}\right), \lambda_{s}^{-1} \mathbf{I}\right) \cdot \mathcal{N}\left(\mathbf{X}_{l+1, j *}\left|\sigma\left(\mathbf{X}_{l, j *}^{+} \mathbf{W}_{l+1}^{+}\right), \lambda_{s}^{-1} \mathbf{I}\right) \cdot \mathcal{N}\left(\mathbf{v}_{j} \mid \mathbf{X}_{l, j *}, \lambda_{v}^{-1} \mathbf{I}\right)\right.\right.
\end{aligned}
$$

For $\mathbf{v}_{j}$ : The posterior $p\left(\mathbf{v}_{j} \mid \mathbf{X}_{L / 2, j *}, \mathbf{R}_{* j}, \mathbf{C}_{* j}, \lambda_{v}, \mathbf{U}\right) \propto \mathcal{N}\left(\mathbf{v}_{j} \mid \mathbf{X}_{L / 2, j *}^{T}, \lambda_{v}^{-1} \mathbf{I}\right) \prod_{i} \mathcal{N}\left(\mathbf{R}_{i j} \mid \mathbf{u}_{i}^{T} \mathbf{v}_{j}, \mathbf{C}_{i j}^{-1}\right)$.
For $\mathbf{u}_{i}$ : The posterior $p\left(\mathbf{u}_{i} \mid \mathbf{R}_{i *}, \mathbf{V}, \lambda_{u}, \mathbf{C}_{i *}\right) \propto \mathcal{N}\left(\mathbf{u}_{i} \mid 0, \lambda_{u}^{-1} \mathbf{I}\right) \prod_{j} \mathcal{N}\left(\mathbf{R}_{i j} \mid \mathbf{u}_{i}^{T} \mathbf{v}_{j}, \mathbf{C}_{i j}^{-1}\right)$.
Interestingly, if $\lambda_{s}$ goes to infinity and adaptive rejection Metropolis sampling (which involves using the gradients of the objective function to approximate the proposal distribution) is used, then the sampling for $\mathbf{W}^{+}$turns out to be a Bayesian generalized version of BP. Specifically, as Figure 8 (right) shows, after getting the gradient of the loss function at one point (the red dashed line on the left), the next sample would be drawn in the region under that line, which is equivalent to a probabilistic version of BP. If a sample is above the curve of the loss function, then a new tangent line (the black dashed line on the right) would be added to better approximate the distribution corresponding to the loss function. After that, samples would be drawn from the region under both lines. During the sampling, besides searching for local optima using the gradients (MAP), the algorithm also takes the variance into consideration. That is why it is called Bayesian generalized back-propagation in Reference [121].
5.1.3 Marginalized Collaborative Deep Learning. In SDAE, corrupted input goes through the encoder and decoder to recover the clean input. Usually, different epochs of training use different corrupted versions as input. Hence, generally, SDAE needs to go through enough epochs of training to see sufficient corrupted versions of the input. Marginalized SDAE (mSDAE) [14] seeks to avoid this by marginalizing out the corrupted input and obtaining closed-form solutions directly. In this sense, mSDAE is more computationally efficient than SDAE.

As mentioned in Reference [66], using mSDAE instead of the Bayesian SDAE could lead to more efficient learning algorithms. For example, in Reference [66], the objective when using a one-layer mSDAE can be written as follows:
$\mathscr{L}=-\sum_{j}\left\|\widetilde{\mathbf{X}}_{0, j *} \mathbf{W}_{1}-\overline{\mathbf{X}}_{c, j *}\right\|_{2}^{2}-\sum_{i, j} \frac{\mathbf{C}_{i j}}{2}\left(\mathbf{R}_{i j}-\mathbf{u}_{i}^{T} \mathbf{v}_{j}\right)^{2}-\frac{\lambda_{u}}{2} \sum_{i}\left\|\mathbf{u}_{i}\right\|_{2}^{2}-\frac{\lambda_{v}}{2} \sum_{j}\left\|\mathbf{v}_{i}^{T} \mathbf{P}_{1}-\mathbf{X}_{0, j *} \mathbf{W}_{1}\right\|_{2}^{2}$,
where $\widetilde{\mathbf{X}}_{0, j *}$ is the collection of $k$ different corrupted versions of $\mathbf{X}_{0, j *}$ (a $k$-by- $B$ matrix) and $\overline{\mathbf{X}}_{c, j *}$ is the $k$-time repeated version of $\mathbf{X}_{c, j *}$ (also a $k$-by- $B$ matrix). $\mathbf{P}_{1}$ is the transformation matrix for item latent factors.

The solution for $\mathbf{W}_{1}$ would be $\mathbf{W}_{1}=E\left(\mathbf{S}_{1}\right) E\left(\mathbf{Q}_{1}\right)^{-1}$, where $\mathbf{S}_{1}=\overline{\mathbf{X}}_{c, j *}^{T} \overline{\mathbf{X}}_{0, j *}+\frac{\lambda_{v}}{2} \mathbf{P}_{1}^{T} \mathbf{V} \mathbf{X}_{c}$ and $\mathbf{Q}_{1}=$ $\overline{\mathbf{X}}_{c, j *}^{T} \overline{\mathbf{X}}_{0, j *}+\frac{\lambda_{v}}{2} \mathbf{X}_{c}^{T} \mathbf{X}_{c}$. A solver for the expectation in the equation above is provided in Reference [14]. Note that this is a linear and one-layer case, which can be generalized to the nonlinear and multi-layer case using the same techniques as in References [13, 14].

Marginalized CDL's perception variables $\Omega_{p}=\left\{\mathbf{X}_{0}, \mathbf{X}_{c}, \mathbf{W}_{1}\right\}$, its hinge variables $\Omega_{h}=\{\mathbf{V}\}$, and its task variables $\Omega_{t}=\left\{\mathbf{P}_{1}, \mathbf{R}, \mathbf{U}\right\}$.
5.1.4 Collaborative Deep Ranking. CDL assumes a collaborative filtering setting to model the ratings directly. Naturally, one can design a similar model to focus more on the ranking among items rather than exact ratings [131]. The corresponding generative process is as follows:
(1) For each layer $l$ of the SDAE network,
(a) For each column $n$ of the weight matrix $\mathbf{W}_{l}$, draw $\mathbf{W}_{l, * n} \sim \mathcal{N}\left(\mathbf{0}, \lambda_{w}^{-1} \mathbf{I}_{K_{l}}\right)$,
(b) Draw the bias vector $\mathbf{b}_{l} \sim \mathcal{N}\left(\mathbf{0}, \lambda_{w}^{-1} \mathbf{I}_{K_{l}}\right)$,
(c) For each row $j$ of $\mathbf{X}_{l}$, draw $\mathbf{X}_{l, j *} \sim \mathcal{N}\left(\sigma\left(\mathbf{X}_{l-1, j *} \mathbf{W}_{l}+\mathbf{b}_{l}\right), \lambda_{s}^{-1} \mathbf{I}_{K_{l}}\right)$.
(2) For each item $j$,
(a) Draw a clean input $\mathbf{X}_{c, j *} \sim \mathcal{N}\left(\mathbf{X}_{l, j *}, \lambda_{n}^{-1} \mathbf{I}_{J}\right)$,
(b) Draw a latent item offset vector $\epsilon_{j} \sim \mathcal{N}\left(\mathbf{0}, \lambda_{v}^{-1} \mathbf{I}_{K}\right)$ and then set the latent item vector to be: $\mathbf{v}_{j}=\epsilon_{j}+\mathbf{X}_{\frac{k}{j}, j *}^{T}$.
(3) For each user $i$,
(a) Draw a latent user vector for each user $i$ : $\mathbf{u}_{i} \sim \mathcal{N}\left(\mathbf{0}, \lambda_{u}^{-1} \mathbf{I}_{K}\right)$,
(b) For each pair-wise preference $(j, k) \in \mathcal{P}_{i}$, where $\mathcal{P}_{i}=\left\{(j, k): \mathbf{R}_{i j}-\mathbf{R}_{i k}>0\right\}$, draw the preference: $\Delta_{i j k} \sim \mathcal{N}\left(\mathbf{u}_{i}^{T} \mathbf{v}_{j}-\mathbf{u}_{i}^{T} \mathbf{v}_{k}, \mathbf{C}_{i j k}^{-1}\right)$.

Following the generative process above, the log-likelihood in Equation (9) becomes

$$
\begin{aligned}
\mathscr{L}= & -\frac{\lambda_{u}}{2} \sum_{i}\left\|\mathbf{u}_{i}\right\|_{2}^{2}-\frac{\lambda_{w}}{2} \sum_{l}\left(\left\|\mathbf{W}_{l}\right\|_{F}^{2}+\left\|\mathbf{b}_{l}\right\|_{2}^{2}\right)-\frac{\lambda_{v}}{2} \sum_{j}\left\|\mathbf{v}_{j}-f_{s}\left(\mathbf{X}_{0, j *}, \mathbf{W}^{+}\right)^{T}\right\|_{2}^{2} \\
& -\frac{\lambda_{n}}{2} \sum_{i}\left\|f_{r}\left(\mathbf{X}_{0, j *}, \mathbf{W}^{+}\right)-\mathbf{X}_{c, j *}\right\|_{2}^{2}-\sum_{i, j, k} \frac{\mathbf{C}_{i j k}}{2}\left(\Delta_{i j k}-\left(\mathbf{u}_{i}^{T} \mathbf{v}_{j}-\mathbf{u}_{i}^{T} \mathbf{v}_{k}\right)\right)^{2}
\end{aligned}
$$

Similar algorithms can be used to learn the parameters in CDR. As reported in Reference [131], using the ranking objective leads to significant improvement in the recommendation performance. Following the definition in Section 4.2, CDR's perception variables $\Omega_{p}=\left\{\left\{\mathbf{W}_{l}\right\},\left\{\mathbf{b}_{l}\right\},\left\{\mathbf{X}_{l}\right\}, \mathbf{X}_{c}\right\}$, the hinge variables $\Omega_{h}=\{\mathbf{V}\}$, and the task variables $\Omega_{t}=\{\mathbf{U}, \Delta\}$.
5.1.5 Collaborative Variational Autoencoders. In CDL, the perception component takes the form of a probabilistic SDAE. Naturally, one can also replace the probabilistic SDAE in CDL with a VAE (introduced in Section 4.3.3), as is done in collaborative variational autoencoders (CVAE) [68]. Specifically, CVAE with a inference network (encoder) denoted as $\left(f_{\mu}(\cdot), f_{s}(\cdot)\right)$ and a generation network (decoder) denoted as $g(\cdot)$ assumes the following generative process:
(1) For each item $j$,
(a) Draw the latent item vector from the VAE inference network: $\mathbf{z}_{j} \sim$ $\mathcal{N}\left(f_{\mu}\left(\mathbf{X}_{0, j *}\right), f_{s}\left(\mathbf{X}_{0, j *}\right)\right)$,
(b) Draw the latent item offset vector $\epsilon_{j} \sim \mathcal{N}\left(\mathbf{0}, \lambda_{v}^{-1} \mathbf{I}_{K}\right)$ and then set the latent item vector: $\mathbf{v}_{j}=\epsilon_{j}+\mathbf{z}_{j}$,
(c) Draw the orignial input from the VAE generation network $\mathbf{X}_{0, j *} \sim \mathcal{N}\left(g\left(\mathbf{z}_{j}\right), \lambda_{n}^{-1} \mathbf{I}_{B}\right)$.
(2) Draw a latent user vector for each user $i$ : $\mathbf{u}_{i} \sim \mathcal{N}\left(\mathbf{0}, \lambda_{u}^{-1} \mathbf{I}_{K}\right)$.
(3) Draw a rating $\mathbf{R}_{i j}$ for each user-item pair $(i, j): \mathbf{R}_{i j} \sim \mathcal{N}\left(\mathbf{u}_{i}^{T} \mathbf{v}_{j}, \mathbf{C}_{i j}^{-1}\right)$.

Similar to CDL, $\lambda_{n}, \lambda_{u}, \lambda_{s}$, and $\lambda_{v}$ are hyperparameters and $\mathbf{C}_{i j}$ is a confidence parameter $\left(\mathbf{C}_{i j}=a\right.$ if $\mathbf{R}_{i j}=1$ and $\mathbf{C}_{i j}=b$ otherwise). Following Reference [68], the ELBO similar to Equation (6) can be derived, using which, one can train the model's parameters using BP and the reparameterization trick.

The evolution from CDL to CVAE demonstrates the BDL framework's flexibility in terms of its components' specific forms. It is also worth noting that the perception component can be a recurrent version of probabilistic SDAE [122] or VAE [17, 68] to handle raw sequential data, while the task-specific component can take more sophisticated forms to accommodate more complex recommendation scenarios (e.g., cross-domain recommendation).
5.1.6 Discussion. Recommender systems are a typical use case for BDL in that they often require both thorough understanding of high-dimensional signals (e.g., text and images) and principled reasoning on the conditional dependencies among users/items/ratings.

In this regard, CDL, as an instantiation of BDL, is the first hierarchical Bayesian model to bridge the gap between state-of-the-art deep learning models and recommender systems. By performing deep learning collaboratively, CDL and its variants can simultaneously extract an effective deep feature representation from high-dimensional content and capture the similarity and implicit relationship between items (and users). The learned representation may also be used for tasks other than recommendation. Unlike previous deep learning models, which use a simple target like classification [56] and reconstruction [111], CDL-based models use CF as a more complex target in a probabilistic framework.

As mentioned in Section 1, information exchange between two components is crucial for the performance of BDL. In the CDL-based models above, the exchange is achieved by assuming Gaussian distributions that connect the hinge variables and the variables in the perception component (drawing the hinge variable $\mathbf{v}_{j} \sim \mathcal{N}\left(\mathbf{X}_{k, j^{*}}^{T}, \lambda_{v}^{-1} \mathbf{I}_{K}\right)$ in the generative process of CDL, where $\mathbf{X}_{k}$ is a perception variable), which is simple but effective and efficient in computation. Among the eight CDL-based models in Table 1, six of them are HV models and the others are LV models, according to the definition of Section 4.2. Since it has been verified that the HV CDL significantly outperforms its ZV counterpart [121], we can expect additional performance boost from the LV counterparts of the six HV models.

Besides efficient information exchange, the model designs also meet the independence requirement on the distribution concerning hinge variables discussed in Section 4.2 and are hence easily parallelizable. In some models to be introduced later, we will see alternative designs to enable efficient and independent information exchange between the two components of BDL.

Note that BDL-based models above use typical static Bayesian networks as their task-specific components. Although these are often sufficient for most use cases, it is possible for the taskspecific components to take the form of deep Bayesian networks such as BIN [117]. This allows the models to handle highly nonlinear interactions between users and items if necessary. One can also use stochastic processes (or dynamic Bayesian networks in general) to explicitly model users purchase or clicking behaviors. For example, it is natural to model a user's purchase of groceries as a Poisson process. In terms of perception components, one can also replace the pSDAE, mSDAE, or VAE above with their convolutional or recurrent counterparts (see Sections 2.3 and 2.4), as is done in Collaborative Knowledge Base Embedding (CKE) [132] or Collaborative Recurrent Autoencoders (CRAE) [122], respectively. Note that for the convolutional or recurrent perception components to be compatible with the task-specific component (which is inherently probabilistic), ideally one would need to formulate probabilistic versions of CNN or RNN as well. Readers are referred to References [132] and [122] for more details.

![img-8.jpeg](img-8.jpeg)

Fig. 9. Graphical model of RSDAE for $L=4$. $\lambda_{s}$ is omitted here to prevent clutter.
In summary, this subsection discusses BDL's applications on supervised leraning, using recommender systems as an example. Section 5.2 below will cover BDL's applications on unsupervised learning.

# 5.2 Unsupervised Bayesian Deep Learning for Topic Models 

To demonstrate how BDL can also be applied to unsupervised learning, we review some examples of BDL-based topic models in this section. These models combine the merits of PGM (which naturally incorporates the probabilistic relations among variables) and NN (which learns deep representations efficiently), leading to significant performance boost. In the case of unsupervised learning, the 'task' for a task-specific component is to describe/characterize the conditional dependencies in the BDL model, thereby improving its interpretability and genearalizability. This is different from the supervised learning setting where the "task" is simply to "match the target."
5.2.1 Relational Stacked Denoising Autoencoders as Topic Models. As a BDL-based topic model, relational stacked denoising autoencoders (RSDAE) essentially tries to learn a hierarchy of topics (or latent factors) while enforcing relational (graph) constraints under an unsupervised learning setting.

Problem Statement and Notation: Assume we have a set of items (articles or movies) $\mathbf{X}_{c}$, with $\mathbf{X}_{i, j *}^{T} \in \mathbb{R}^{B}$ denoting the content (attributes) of item $j$. Besides, we use $\mathbf{I}_{K}$ to denote a $K$ dimensional identity matrix and $\mathbf{S}=\left[\mathbf{s}_{1}, \mathbf{s}_{2}, \ldots, \mathbf{s}_{J}\right]$ to denote the relational latent matrix with $\mathbf{s}_{j}$ representing the relational properties of item $j$.

From the perspective of SDAE, the $J$-by- $B$ matrix $\mathbf{X}_{c}$ represents the clean input to the SDAE and the noise-corrupted matrix of the same size is denoted by $\mathbf{X}_{0}$. Besides, we denote the output of layer $l$ of the SDAE, a $J$-by- $K_{l}$ matrix, by $\mathbf{X}_{l}$. Row $j$ of $\mathbf{X}_{l}$ is denoted by $\mathbf{X}_{l, j *}, \mathbf{W}_{l}$ and $\mathbf{b}_{l}$ are the weight matrix and bias vector of layer $l, \mathbf{W}_{l, * n}$ denotes column $n$ of $\mathbf{W}_{l}$, and $L$ is the number of layers. As a shorthand, we refer to the collection of weight matrices and biases in all layers as $\mathbf{W}^{+}$. Note that an $L / 2$-layer SDAE corresponds to an $L$-layer network.

Model Formulation: In RSDAE, the perception component takes the form of a probabilistic SDAE (introduced in Section 4.3.2) as a building block. At a higher level, RSDAE is formulated as a novel probabilistic model that seamlessly integrates a hierarchy of latent factors and the relational information available. This way, the model can simultaneously learn the feature representation from the content information and the relation among items [118]. The graphical model for RSDAE is shown in Figure 9, and the generative process is listed as follows:
(1) Draw the relational latent matrix $\mathbf{S}$ from a matrix-variate normal distribution [33]:

$$
\mathbf{S} \sim \mathcal{N}_{K, J}\left(0, \mathbf{I}_{K} \otimes\left(\lambda_{l} \mathscr{L}_{a}\right)^{-1}\right)
$$

(2) For layer $l$ of the SDAE where $l=1,2, \ldots, \frac{L}{2}-1$,

(a) For each column $n$ of the weight matrix $\mathbf{W}_{l}$, draw $\mathbf{W}_{l, * n} \sim \mathcal{N}\left(0, \lambda_{w}^{-1} \mathbf{I}_{K_{l}}\right)$,
(b) Draw the bias vector $\mathbf{b}_{l} \sim \mathcal{N}\left(0, \lambda_{w}^{-1} \mathbf{I}_{K_{l}}\right)$,
(c) For each row $j$ of $\mathbf{X}_{l}$, draw $\mathbf{X}_{l, j *} \sim \mathcal{N}\left(\sigma\left(\mathbf{X}_{l-1, j *} \mathbf{W}_{l}+\mathbf{b}_{l}\right), \lambda_{s}^{-1} \mathbf{I}_{K_{l}}\right)$.
(3) For layer $\frac{l}{2}$ of the SDAE, draw the representation vector for item $j$ from the product of two Gaussians (PoG) [23]:

$$
\mathbf{X}_{\frac{l}{2}, j *} \sim \operatorname{PoG}\left(\sigma\left(\mathbf{X}_{\frac{l}{2}-1, j *} \mathbf{W}_{l}+\mathbf{b}_{l}\right), \mathbf{s}_{j}^{T}, \lambda_{s}^{-1} \mathbf{I}_{K}, \lambda_{r}^{-1} \mathbf{I}_{K}\right)
$$

(4) For layer $l$ of the SDAE where $l=\frac{l}{2}+1, \frac{l}{2}+2, \ldots, L$,
(a) For each column $n$ of the weight matrix $\mathbf{W}_{l}$, draw $\mathbf{W}_{l, * n} \sim \mathcal{N}\left(0, \lambda_{w}^{-1} \mathbf{I}_{K_{l}}\right)$,
(b) Draw the bias vector $\mathbf{b}_{l} \sim \mathcal{N}\left(0, \lambda_{w}^{-1} \mathbf{I}_{K_{l}}\right)$,
(c) For each row $j$ of $\mathbf{X}_{l}$, draw $\mathbf{X}_{l, j *} \sim \mathcal{N}\left(\sigma\left(\mathbf{X}_{l-1, j *} \mathbf{W}_{l}+\mathbf{b}_{l}\right), \lambda_{s}^{-1} \mathbf{I}_{K_{l}}\right)$.
(5) For each item $j$, draw a clean input $\mathbf{X}_{c, j *} \sim \mathcal{N}\left(\mathbf{X}_{L, j *}, \lambda_{n}^{-1} \mathbf{I}_{B}\right)$.

Here, $K=K_{\frac{l}{2}}$ is the dimensionality of the learned representation vector for each item, S denotes the $K \times J$ relational latent matrix in which column $j$ is the relational latent vector $\mathbf{s}_{j}$ for item $j$. Note that $\mathcal{N}_{K, J}\left(0, \mathbf{I}_{K} \otimes\left(\lambda_{l} \mathscr{L}_{a}\right)^{-1}\right)$ in Equation (10) is a matrix-variate normal distribution defined as in Reference [33]:

$$
p(\mathrm{~S})=\mathcal{N}_{K, J}\left(0, \mathbf{I}_{K} \otimes\left(\lambda_{l} \mathscr{L}_{a}\right)^{-1}\right)=\frac{\exp \left\{\operatorname{tr}\left[-\frac{\lambda_{l}}{2} \mathrm{~S} \mathscr{L}_{a} \mathrm{~S}^{T}\right]\right\}}{(2 \pi)^{J K / 2}\left|\mathbf{I}_{K}\right|^{J / 2}\left|\lambda_{l} \mathscr{L}_{a}\right|^{-K / 2}}
$$

where the operator $\otimes$ denotes the Kronecker product of two matrices [33], $\operatorname{tr}(\cdot)$ denotes the trace of a matrix, and $\mathscr{L}_{a}$ is the Laplacian matrix incorporating the relational information. $\mathscr{L}_{a}=\mathbf{D}-\mathbf{A}$, where $\mathbf{D}$ is a diagonal matrix whose diagonal elements $\mathbf{D}_{i t}=\sum_{j} \mathbf{A}_{i j}$ and $\mathbf{A}$ is the adjacency matrix representing the relational information with binary entries indicating the links (or relations) between items. $\mathbf{A}_{j j^{\prime}}=1$ indicates that there is a link between item $j$ and item $j^{\prime}$ and $\mathbf{A}_{j j^{\prime}}=0$ otherwise. $\operatorname{PoG}\left(\sigma\left(\mathbf{X}_{\frac{l}{2}-1, j *} \mathbf{W}_{l}+\mathbf{b}_{l}\right), \mathbf{s}_{j}^{T}, \lambda_{s}^{-1} \mathbf{I}_{K}, \lambda_{r}^{-1} \mathbf{I}_{K}\right)$ denotes the product of the Gaussian $\mathcal{N}\left(\sigma\left(\mathbf{X}_{\frac{l}{2}-1, j *} \mathbf{W}_{l}+\mathbf{b}_{l}\right), \lambda_{s}^{-1} \mathbf{I}_{K}\right)$ and the Gaussian $\mathcal{N}\left(\mathbf{s}_{j}^{T}, \lambda_{r}^{-1} \mathbf{I}_{K}\right)$, which is also a Gaussian [23].

According to the generative process above, maximizing the posterior probability is equivalent to maximizing the joint log-likelihood of $\left\{\mathbf{X}_{l}\right\}, \mathbf{X}_{c}, \mathbf{S},\left\{\mathbf{W}_{l}\right\}$, and $\left\{\mathbf{b}_{l}\right\}$ given $\lambda_{s}, \lambda_{w}, \lambda_{l}, \lambda_{r}$, and $\lambda_{n}$ :

$$
\begin{aligned}
\mathscr{L}= & -\frac{\lambda_{l}}{2} \operatorname{tr}\left(\mathbf{S} \mathscr{L}_{a} \mathbf{S}^{T}\right)-\frac{\lambda_{r}}{2} \sum_{j}\left\|\left(\mathbf{s}_{j}^{T}-\mathbf{X}_{\frac{l}{2}, j *}\right)\right\|_{2}^{2}-\frac{\lambda_{w}}{2} \sum_{l}\left(\left\|\mathbf{W}_{l}\right\|_{F}^{2}+\left\|\mathbf{b}_{l}\right\|_{2}^{2}\right) \\
& -\frac{\lambda_{n}}{2} \sum_{j}\left\|\mathbf{X}_{L, j *}-\mathbf{X}_{c, j *}\right\|_{2}^{2}-\frac{\lambda_{s}}{2} \sum_{l} \sum_{j}\left\|\sigma\left(\mathbf{X}_{l-1, j *} \mathbf{W}_{l}+\mathbf{b}_{l}\right)-\mathbf{X}_{l, j *}\right\|_{2}^{2}
\end{aligned}
$$

Similar to the pSDAE, taking $\lambda_{s}$ to infinity, the joint log-likelihood becomes

$$
\mathscr{L}=-\frac{\lambda_{l}}{2} \operatorname{tr}\left(\mathbf{S} \mathscr{L}_{a} \mathbf{S}^{T}\right)-\frac{\lambda_{r}}{2} \sum_{j}\left\|\left(\mathbf{s}_{j}^{T}-\mathbf{X}_{\frac{l}{2}, j *}\right)\right\|_{2}^{2}-\frac{\lambda_{w}}{2} \sum_{l}\left(\left\|\mathbf{W}_{l}\right\|_{F}^{2}+\left\|\mathbf{b}_{l}\right\|_{2}^{2}\right)-\frac{\lambda_{n}}{2} \sum_{j}\left\|\mathbf{X}_{L, j *}-\mathbf{X}_{c, j *}\right\|_{2}^{2}
$$

where $\mathbf{X}_{l, j *}=\sigma\left(\mathbf{X}_{l-1, j *} \mathbf{W}_{l}+\mathbf{b}_{l}\right)$. Note that the first term $-\frac{\lambda_{l}}{2} \operatorname{tr}\left(\mathbf{S} \mathscr{L}_{a} \mathbf{S}^{T}\right)$ corresponds to $\log p(\mathrm{~S})$ in the matrix-variate distribution in Equation (12). Besides, by simple manipulation, we have $\operatorname{tr}\left(\mathrm{S} \mathscr{L}_{a} \mathbf{S}^{T}\right)=\sum_{k=1}^{K} \mathrm{~S}_{k *}^{T} \mathscr{L}_{a} \mathrm{~S}_{k *}$, where $\mathrm{S}_{k *}$ denotes the $k$ th row of S . As we can see, maximizing $-\frac{\lambda_{l}}{2} \operatorname{tr}\left(\mathrm{~S}^{T} \mathscr{L}_{a} \mathrm{~S}\right)$ is equivalent to making $\mathbf{s}_{j}$ closer to $\mathbf{s}_{j^{\prime}}$ if item $j$ and item $j^{\prime}$ are linked (namely, $\left.\mathbf{A}_{j j^{\prime}}=1\right)[115]$.

In RSDAE, the perception variables $\Omega_{p}=\left\{\left\{\mathbf{X}_{l}\right\}, \mathbf{X}_{c},\left\{\mathbf{W}_{l}\right\},\left\{\mathbf{b}_{l}\right\}\right\}$, the hinge variables $\Omega_{h}=\{\mathbf{S}\}$, and the task variables $\Omega_{t}=\{\mathbf{A}\}$.

Learning and Inference: Reference [118] provides an EM-style algorithm for MAP estimation. Below, we review some of the key steps.

For the E step, the challenge lies in the inference of the relational latent matrix $\mathbf{S}$. We first fix all rows of $\mathbf{S}$ except the $k$ th one $\mathbf{S}_{k *}$, and then update $\mathbf{S}_{k *}$. Specifically, we take the gradient of $\mathscr{L}$ with respect to $\mathbf{S}_{k *}$, set it to 0 , and get the following linear system:

$$
\left(\lambda_{l} \mathscr{L}_{a}+\lambda_{r} \mathbf{I}_{J}\right) \mathbf{S}_{k *}=\lambda_{r} \mathbf{X}_{\frac{1}{2}, * k}^{T}
$$

A naive approach is to solve the linear system by setting $\mathbf{S}_{k *}=\lambda_{r}\left(\lambda_{l} \mathscr{L}_{a}+\lambda_{r} \mathbf{I}_{J}\right)^{-1} \mathbf{X}_{\frac{1}{2}, * k}^{T}$. Unfortunately, the complexity is $O\left(J^{5}\right)$ for one single update. Similar to Reference [67], the steepest descent method [101] is used to iteratively update $\mathbf{S}_{k *}$ :
$\mathbf{S}_{k *(} t+1) \leftarrow \mathbf{S}_{k *}(t)+\delta(t) r(t), \quad r(t) \leftarrow \lambda_{r} \mathbf{X}_{\frac{1}{2}, * k}^{T}-\left(\lambda_{l} \mathscr{L}_{a}+\lambda_{r} \mathbf{I}_{J}\right) \mathbf{S}_{k *}(t), \quad \delta(t) \leftarrow \frac{r(t)^{T} r(t)}{r(t)^{T}\left(\lambda_{l} \mathscr{L}_{a}+\lambda_{r} \mathbf{I}_{J}\right) r(t)}$.
As discussed in Reference [67], the steepest descent method dramatically reduces the computation cost in each iteration from $O\left(J^{5}\right)$ to $O(J)$.

The M step involves learning $\mathbf{W}_{l}$ and $\mathbf{b}_{l}$ for each layer using the back-propagation algorithm given $\mathbf{S}$. By alternating the update of $\mathbf{S}, \mathbf{W}_{l}$, and $\mathbf{b}_{l}$, a local optimum for $\mathscr{L}$ can be found. Also, techniques such as including a momentum term may help to avoid being trapped in a local optimum.
5.2.2 Deep Poisson Factor Analysis with Sigmoid Belief Networks. The Poisson distribution with support over nonnegative integers is known as a natural choice to model counts. It is, therefore, desirable to use it as a building block for topic models, which are generally interested in word counts [8]. With this motivation, Reference [136] proposed a model, dubbed Poisson factor analysis (PFA), for latent nonnegative matrix factorization via Poisson distributions.

Poisson Factor Analysis: PFA assumes a discrete $P$-by- $N$ matrix $\mathbf{X}$ containing word counts of $N$ documents with a vocabulary size of $P[24,136]$. In a nutshell, PFA can be described using the equation $\mathbf{X} \sim \operatorname{Pois}(\Phi(\boldsymbol{\Theta} \circ \mathbf{H}))$, where $\Phi$ (of size $P$-by- $K$ where $K$ is the number of topics) denotes the factor loading matrix in factor analysis with the $k$ th column $\boldsymbol{\phi}_{k}$ encoding the importance of each word in topic $k$. The $K$-by- $N$ matrix $\boldsymbol{\Theta}$ is the factor score matrix with the $n$th column $\boldsymbol{\theta}_{n}$ containing topic proportions for document $n$. The $K$-by- $N$ matrix $\mathbf{H}$ is a latent binary matrix with the $n$th column $\mathbf{h}_{n}$ defining a set of topics associated with document $n$.

Different priors correspond to different models. For example, Dirichlet priors on $\boldsymbol{\phi}_{k}$ and $\boldsymbol{\theta}_{n}$ with an all-one matrix $\mathbf{H}$ would recover LDA [8] while a beta-Bernoulli prior on $\mathbf{h}_{n}$ leads to the NBFTM model in Reference [135]. In Reference [24], a deep-structured prior based on sigmoid belief networks (SBN) [79] (an MLP variant with binary hidden units) is imposed on $\mathbf{h}_{n}$ to form a deep PFA model for topic modeling.

Deep Poisson Factor Analysis: In the deep PFA model [24], the generative process can be summarized as follows:

$$
\begin{aligned}
& \boldsymbol{\phi}_{k} \sim \operatorname{Dir}\left(a_{\phi}, \ldots, a_{\phi}\right), \quad \theta_{k n} \sim \operatorname{Gamma}\left(r_{k}, \frac{p_{n}}{1-p_{n}}\right), \quad r_{k} \sim \operatorname{Gamma}\left(\gamma_{0}, \frac{1}{c_{0}}\right), \quad \gamma_{0} \sim \operatorname{Gamma}\left(e_{0}, \frac{1}{f_{0}}\right), \\
& h_{k_{L} n}^{(L)} \sim \operatorname{Ber}\left(\sigma\left(b_{k_{L}}^{(L)}\right)\right), h_{k_{l} n}^{(l)} \sim \operatorname{Ber}\left(\sigma\left(\mathbf{w}_{k_{l}}^{(l)^{T}} \mathbf{h}_{n}^{(l+1)}+b_{k_{l}}^{(l)}\right)\right), x_{p n k} \sim \operatorname{Pois}\left(\phi_{p k} \theta_{k n} h_{k n}^{(1)}\right), x_{p n}=\sum_{k=1}^{K} x_{p n k},
\end{aligned}
$$

where $L$ is the number of layers in SBN, which corresponds to Equation (15). $x_{p n k}$ is the count of word $p$ that comes from topic $k$ in document $n$.

In this model, the perception variables $\Omega_{p}=\left\{\left\{\mathbf{H}^{(l)}\right\},\left\{\mathbf{W}_{l}\right\},\left\{\mathbf{b}_{l}\right\}\right\}$, the hinge variables $\Omega_{h}=\{\mathbf{X}\}$, and the task variables $\Omega_{t}=\left\{\left\{\boldsymbol{\phi}_{k}\right\},\left\{r_{k}\right\}, \boldsymbol{\Theta}, \gamma_{0}\right\} . \mathbf{W}_{l}$ is the weight matrix containing columns of $\mathbf{w}_{k_{l}}^{(l)}$ and $\mathbf{b}_{l}$ is the bias vector containing entries of $b_{k_{l}}^{(l)}$ in Equation (15).

Learning Using Bayesian Conditional Density Filtering: Efficient learning algorithms are needed for Bayesian treatments of deep PFA. Reference [24] proposed to use an online version of MCMC called Bayesian conditional density filtering (BCDF) to learn both the global parameters $\Psi_{g}=\left(\left\{\boldsymbol{\phi}_{k}\right\},\left\{r_{k}\right\}, \gamma_{0},\left\{\mathbf{W}_{l}\right\},\left\{\mathbf{b}_{l}\right\}\right)$ and the local variables $\Psi_{l}=\left(\boldsymbol{\Theta},\left\{\mathbf{H}^{(l)}\right\}\right)$. The key conditional densities used for the Gibbs updates are as follows:

$$
\begin{aligned}
x_{p n k} \mid- & \sim \operatorname{Multi}\left(x_{p n} ; \zeta_{p n 1}, \ldots, \zeta_{p n K}\right), & \phi_{k} \mid-\sim \operatorname{Dir}\left(a_{\phi}+x_{1 \cdot k}, \ldots, a_{\phi}+x_{P \cdot k}\right) \\
\theta_{k n} \mid- & \sim \operatorname{Gamma}\left(r_{k} h_{k n}^{(1)}+x_{\cdot n k}, p_{n}\right), & h_{k n}^{(1)} \mid-\sim \delta\left(x_{\cdot n k}=0\right) \operatorname{Ber}\left(\frac{\widetilde{\pi}_{k n}}{\widetilde{\pi}_{k n}+\left(1-\pi_{k n}\right)}\right)+\delta\left(x_{\cdot n k}>0\right)
\end{aligned}
$$

where $\widetilde{\pi}_{k n}=\pi_{k n}\left(1-p_{n}\right)^{r_{k}}, \pi_{k n}=\sigma\left(\left(\mathbf{w}_{k}^{(1)}\right)^{T} \mathbf{h}_{n}^{(2)}+c_{k}^{(1)}\right), x_{\cdot n k}=\sum_{p=1}^{P} x_{p n k}, x_{p \cdot k}=\sum_{n=1}^{N} x_{p n k}$, and $\zeta_{p n k} \propto \phi_{p k} \theta_{k n}$. For the learning of $h_{k n}^{(l)}$ where $l>1$, the same techniques as in Reference [25] can be used.

Learning Using Stochastic Gradient Thermostats: An alternative way of learning deep PFA is through stochastic gradient Nòse-Hoover thermostats (SGNHT), which is more accurate and scalable. SGNHT is a generalization of the stochastic gradient Langevin dynamics (SGLD) [127] and the stochastic gradient Hamiltonian Monte Carlo (SGHMC) [15]. Compared with the previous two, SGNHT introduces momentum variables into the system, helping the system to jump out of local optima. Specifically, the following stochastic differential equations (SDE) can be used:

$$
d \Psi_{g}=\mathbf{v} d t, \quad d \mathbf{v}=\widetilde{f}\left(\Psi_{g}\right) d t-\xi \mathbf{v} d t+\sqrt{D} d^{r} W, \quad d \xi=\left(\frac{1}{M} \mathbf{v}^{T} \mathbf{v}-1\right) d t
$$

where $\widetilde{f}\left(\Psi_{g}\right)=-\nabla_{\Psi_{g}} \widetilde{U}\left(\Psi_{g}\right)$ and $\widetilde{U}\left(\Psi_{g}\right)$ is the negative log-posterior of the model. $t$ indexes time and ${ }^{r} W$ denotes the standard Wiener process. $\xi$ is the thermostats variable to make sure the system has a constant temperature. $D$ is the injected variance, which is a constant. To speed up convergence, the SDE is generalized to

$$
d \Psi_{g}=\mathbf{v} d t, \quad d \mathbf{v}=\widetilde{f}\left(\Psi_{g}\right) d t-\Xi \mathbf{v} d t+\sqrt{D} d^{r} W, \quad d \Xi=(\mathbf{q}-\mathbf{I}) d t
$$

where $\mathbf{I}$ is the identity matrix, $\Xi=\operatorname{diag}\left(\xi_{1}, \ldots, \xi_{M}\right), \mathbf{q}=\operatorname{diag}\left(v_{1}^{2}, \ldots, v_{M}^{2}\right)$, and $M$ is the dimensionality of the parameters.

SGNHT, SGLD, and SGHMC all belong to a larger class of sampling algorithms called hybrid Monte Carlo (HMC) [5]. The idea is to leverage an analogy with physical systems to guide transitions of system states. Compared to the Metropolis algorithm, HMC can make much larger changes to system states while keeping a small rejection probability. For more details, we refer readers to References $[5,81]$.
5.2.3 Deep Poisson Factor Analysis with Restricted Boltzmann Machine. The deep PFA model above uses SBN as a perception component. Similarly, one can replace SBN with RBM [41] (discussed in Section 4.3.1) to achieve comparable performance. With RBM as the perception component, Equation (15) becomes conditional distributions similar to Equation (4) with the following energy [41]:

$$
E\left(\mathbf{h}_{n}^{(l)}, \mathbf{h}_{n}^{(l+1)}\right)=-\left(\mathbf{h}_{n}^{(l)}\right)^{T} \mathbf{c}^{(l)}-\left(\mathbf{h}_{n}^{(l)}\right)^{T} \mathbf{W}^{(l)} \mathbf{h}_{n}^{(l+1)}-\left(\mathbf{h}_{n}^{(l+1)}\right)^{T} \mathbf{c}^{(l+1)}
$$

Similar learning algorithms as the deep PFA with SBN can be used. Specifically, the sampling process would alternate between $\left\{\left\{\boldsymbol{\phi}_{k}\right\},\left\{\gamma_{k}\right\}, \gamma_{0}\right\}$ and $\left\{\left\{\mathbf{W}^{(l)}\right\},\left\{\mathbf{c}^{(l)}\right\}\right\}$. The former involves similar conditional density as the SBN-based DPFA. The latter is RBM's parameters and can be updated using the contrastive divergence algorithm.
5.2.4 Discussion. Here, we choose topic models as an example application to demonstrate how BDL can be applied in the unsupervised learning setting. In BDL-based topic models, the perception component is responsible for inferring the topic hierarchy from documents, while the taskspecific component is in charge of modeling the word generation, topic generation, word-topic relation, or inter-document relation. The synergy between these two components comes from the bidirectional interaction between them. On the one hand, knowledge on the topic hierarchy facilitates accurate modeling of words and topics, providing valuable information for learning interdocument relation. On the other hand, accurately modeling the words, topics, and inter-document relation can help discover the topic hierarchy and learn compact latent factors for documents.

It is worth noting that the information exchange mechanism in some BDL-based topic models is different from that in Section 5.1. For example, in the SBN-based DPFA model, the exchange is natural, since the bottom layer of SBN, $\mathbf{H}^{(1)}$, and the relationship between $\mathbf{H}^{(1)}$ and $\Omega_{h}=\{\mathbf{X}\}$ are both inherently probabilistic, as shown in Equation (15), which means additional assumptions on the distribution are not necessary. The SBN-based DPFA model is equivalent to assuming that $\mathbf{H}$ in PFA is generated from a Dirac delta distribution (a Gaussian distribution with zero variance) centered at the bottom layer of the SBN, $\mathbf{H}^{(1)}$. Hence, both DPFA models in Table 1 are ZV models, according to the definition in Section 4.2. It is worth noting that RSDAE is an HV model (see Equation (11), where $\mathbf{S}$ is the hinge variable and the others are perception variables), and naively modifying this model to be its ZV counterpart would violate the i.i.d. requirement in Section 4.2.

Similar to Section 5.1, BDL-based topic models above use typical static Bayesian networks as task-specific components. Naturally, one can choose to use other forms of task-specific components. For example, it is straightforward to replace the relational prior of RSDAE in Section 5.2.1 with a stochastic process (e.g., a Wiener process as in Reference [113]) to model the evolution of the topic hierarchy over time.

# 5.3 Bayesian Deep Representation Learning for Control 

In Sections 5.1 and 5.2, we covered how BDL can be applied in the supervised and unsupervised learning settings, respectively. In this section, we will discuss how BDL can help representation learning in general, using control as an example application.

As mentioned in Section 1, Bayesian deep learning can also be applied to the control of nonlinear dynamical systems from raw images. Consider controlling a complex dynamical system according to the live video stream received from a camera. One way of solving this control problem is by iteration between two tasks, perception from raw images and control based on dynamic models. The perception task can be taken care of using multiple layers of simple nonlinear transformation (deep learning) while the control task usually needs more sophisticated models like hidden Markov models and Kalman filters [35, 74]. To enable an effective iterative process between the perception task and the control task, we need two-way information exchange between them. The perception component would be the basis on which the control component estimates its states and, however, the control component with a dynamic model built in would be able to predict the future trajectory (images) by reversing the perception process [125].

As one of the pioneering works in this direction, Reference [125] posed this task as a representation learning problem and proposed a model called Embed to Control to take into account the feedback loop mentioned above during representation learning. Essentially, the goal is to learn

representations that (1) capture semantic information from raw images/videos and (2) preserve local linearity in the state space for convenient control. This is not possible without the BDL framework, since the perception component guarantees the first sub-goal while the task-specific component guarantees the second. Below, we start with some preliminaries on stochastic optimal control and then introduce the BDL-based model for representation learning.
5.3.1 Stochastic Optimal Control. Following Reference [125], we consider the stochastic optimal control of an unknown dynamical system as follows:

$$
\mathbf{z}_{t+1}=f\left(\mathbf{z}_{t}, \mathbf{u}_{t}\right)+\boldsymbol{\xi}, \boldsymbol{\xi} \sim \mathcal{N}\left(0, \Sigma_{\xi}\right)
$$

where $t$ indexes the time steps and $\mathbf{z}_{t} \in \mathbb{R}^{n_{z}}$ is the latent states. $\mathbf{u}_{t} \in \mathbb{R}^{n_{u}}$ is the applied control at time $t$ and $\boldsymbol{\xi}$ denotes the system noise. Equivalently, the equation above can be written as $P\left(\mathbf{z}_{t+1} \mid \mathbf{z}_{t}, \mathbf{u}_{t}\right)=\mathcal{N}\left(\mathbf{z}_{t+1} \mid f\left(\mathbf{z}_{t}, \mathbf{u}_{t}\right), \Sigma_{\xi}\right)$. Hence, we need a mapping function to map the corresponding raw image $\mathbf{x}_{t}$ (observed input) into the latent space:

$$
\mathbf{z}_{t}=m\left(\mathbf{x}_{t}\right)+\omega, \omega \sim \mathcal{N}\left(0, \Sigma_{\omega}\right)
$$

where $\omega$ is the corresponding system noise. Similarly, the equation above can be rewritten as $\mathbf{z}_{t} \sim \mathcal{N}\left(m\left(\mathbf{x}_{t}\right), \Sigma_{\omega}\right)$. If the function $f$ is given, then finding optimal control for a trajectory of length $T$ in a dynamical system amounts to minimizing the following cost:

$$
J\left(\mathbf{z}_{1: T}, \mathbf{u}_{1: T}\right)=\mathbb{E}_{\mathbf{z}}\left(c_{T}\left(\mathbf{z}_{T}, \mathbf{u}_{T}\right)+\sum_{t_{0}}^{T-1} c\left(\mathbf{z}_{t}, \mathbf{u}_{t}\right)\right)
$$

where $c_{T}\left(\mathbf{z}_{T}, \mathbf{u}_{T}\right)$ is the terminal cost and $c\left(\mathbf{z}_{t}, \mathbf{u}_{t}\right)$ is the instantaneous cost. $\mathbf{z}_{1: T}=\left\{\mathbf{z}_{1}, \ldots, \mathbf{z}_{T}\right\}$ and $\mathbf{u}_{1: T}=\left\{\mathbf{u}_{1}, \ldots, \mathbf{u}_{T}\right\}$ are the state and action sequences, respectively. For simplicity, we can let $c_{T}\left(\mathbf{z}_{T}, \mathbf{u}_{T}\right)=c\left(\mathbf{z}_{T}, \mathbf{u}_{T}\right)$ and use the following quadratic cost $c\left(\mathbf{z}_{t}, \mathbf{u}_{t}\right)=\left(\mathbf{z}_{t}-\mathbf{z}_{\text {goal }}\right)^{T} \mathbf{R}_{z}\left(\mathbf{z}_{t}-\right.$ $\mathbf{z}_{\text {goal }}$ ) $+\mathbf{u}_{t}^{T} \mathbf{R}_{u} \mathbf{u}_{t}$, where $\mathbf{R}_{z} \in \mathbb{R}^{n_{z} \times n_{z}}$ and $\mathbf{R}_{u} \in \mathbb{R}^{n_{u} \times n_{u}}$ are the weighting matrices. $\mathbf{z}_{\text {goal }}$ is the target latent state that should be inferred from the raw images (observed input). Given the function $f, \widetilde{\mathbf{z}}_{1: T}$ (current estimates of the optimal trajectory), and $\widetilde{\mathbf{u}}_{1: T}$ (the corresponding controls), the dynamical system can be linearized as

$$
\mathbf{z}_{t+1}=\mathbf{A}\left(\widetilde{\mathbf{z}}_{t}\right) \mathbf{z}_{t}+\mathbf{B}\left(\widetilde{\mathbf{z}}_{t}\right) \mathbf{u}_{t}+\mathbf{o}\left(\widetilde{\mathbf{z}}_{t}\right)+\omega, \omega \sim \mathcal{N}\left(0, \Sigma_{\omega}\right)
$$

where $\mathbf{A}\left(\widetilde{\mathbf{z}}_{t}\right)=\frac{\partial f\left(\widetilde{\mathbf{z}}_{t}, \widetilde{\mathbf{u}}_{t}\right)}{\partial \widetilde{\mathbf{z}}_{t}}$ and $\mathbf{B}\left(\widetilde{\mathbf{z}}_{t}\right)=\frac{\partial f\left(\widetilde{\mathbf{z}}_{t}, \widetilde{\mathbf{u}}_{t}\right)}{\partial \widetilde{\mathbf{u}}_{t}}$ are local Jacobians. $\mathbf{o}\left(\widetilde{\mathbf{z}}_{t}\right)$ is the offset.
5.3.2 BDL-based Representation Learning for Control. To minimize the function in Equation (17), we need three key components: an encoding model to encode $\mathbf{x}_{t}$ into $\mathbf{z}_{t}$, a transition model to infer $\mathbf{z}_{t+1}$ given $\left(\mathbf{z}_{t}, \mathbf{u}_{t}\right)$, and a reconstruction model to reconstruct $\mathbf{x}_{t+1}$ from the inferred $\mathbf{z}_{t+1}$.

Encoding Model: An encoding model $Q_{\phi}(Z \mid X)=\mathcal{N}\left(\boldsymbol{\mu}_{t}, \operatorname{diag}\left(\sigma_{j}^{2}\right)\right)$, where the mean $\boldsymbol{\mu}_{t} \in \mathbb{R}^{n_{z}}$ and the diagonal covariance $\Sigma_{t}=\operatorname{diag}\left(\sigma_{j}^{2}\right) \in \mathbb{R}^{n_{z} \times n_{z}}$, encodes the raw images $\mathbf{x}_{t}$ into latent states $\mathbf{z}_{t}$. Here,

$$
\boldsymbol{\mu}_{t}=\mathbf{W}_{\mu} h_{\phi}^{\mathrm{enc}}\left(\mathbf{x}_{t}\right)+\mathbf{b}_{\mu}, \quad \log \sigma_{t}=\mathbf{W}_{\sigma} h_{\phi}^{\mathrm{enc}}\left(\mathbf{x}_{t}\right)+\mathbf{b}_{\sigma}
$$

where $h_{\phi}\left(\mathbf{x}_{t}\right)^{\text {enc }}$ is the output of the encoding network with $\mathbf{x}_{t}$ as its input.
Transition Model: A transition model like Equation (18) infers $\mathbf{z}_{t+1}$ from $\left(\mathbf{z}_{t}, \mathbf{u}_{t}\right)$. If we use $\widetilde{Q}_{\phi}(\widetilde{Z} \mid Z, \mathbf{u})$ to denote the approximate posterior distribution to generate $\mathbf{z}_{t+1}$, then the generative process of the full model would be

$$
\mathbf{z}_{t} \sim Q_{\phi}(Z \mid X)=\mathcal{N}\left(\boldsymbol{\mu}_{t}, \Sigma_{t}\right), \quad \widetilde{\mathbf{z}}_{t+1} \sim \widetilde{Q}_{\phi}(\widetilde{Z} \mid Z, \mathbf{u})=\mathcal{N}\left(\mathbf{A}_{t} \boldsymbol{\mu}_{t}+\mathbf{B}_{t} \mathbf{u}_{t}+\mathbf{o}_{t}, \mathbf{C}_{t}\right), \quad \widetilde{\mathbf{x}}_{t}, \widetilde{\mathbf{x}}_{t+1} \sim P_{\theta}(X \mid Z)=\operatorname{Bern}\left(\mathbf{p}_{t}\right)
$$

where the last equation is the reconstruction model to be discussed later, $\mathbf{C}_{t}=\mathbf{A}_{t} \Sigma_{t} \mathbf{A}_{t}^{T}+\mathbf{H}_{t}$, and $\mathbf{H}_{t}$ is the covariance matrix of the estimated system noise $\left(\omega_{t} \sim \mathcal{N}\left(0, \mathbf{H}_{t}\right)\right)$. The key here is to learn $\mathbf{A}_{t}$, $\mathbf{B}_{t}$ and $\mathbf{o}_{t}$, which are parameterized as follows:

$$
\operatorname{vec}\left(\mathbf{A}_{t}\right)=\mathbf{W}_{A} h_{\psi}^{\text {trans }}\left(\mathbf{z}_{t}\right)+\mathbf{b}_{A}, \quad \operatorname{vec}\left(\mathbf{B}_{t}\right)=\mathbf{W}_{B} h_{\psi}^{\text {trans }}\left(\mathbf{z}_{t}\right)+\mathbf{b}_{B}, \quad \mathbf{o}_{t}=\mathbf{W}_{o} h_{\psi}^{\text {trans }}\left(\mathbf{z}_{t}\right)+\mathbf{b}_{o}
$$

where $h_{\psi}^{\text {trans }}\left(\mathbf{z}_{t}\right)$ is the output of the transition network.
Reconstruction Model: As mentioned in the last part of Equation (20), the posterior distribution $P_{\theta}(X \mid Z)$ reconstructs the raw images $\mathbf{x}_{t}$ from the latent states $\mathbf{z}_{t}$. The parameters for the Bernoulli distribution $\mathbf{p}_{t}=\mathbf{W}_{p} h_{\theta}^{\operatorname{dec}}\left(\mathbf{z}_{t}\right)+\mathbf{b}_{p}$ where $h_{\theta}^{\operatorname{dec}}\left(\mathbf{z}_{t}\right)$ is the output of a third network, called the decoding network or the reconstruction network. Putting it all together, Equation (20) shows the generative process of the full model.
5.3.3 Learning Using Stochastic Gradient Variational Bayes. With $\mathcal{D}=\left\{\left(\mathbf{x}_{1}, \mathbf{u}_{1}, \mathbf{x}_{2}\right), \ldots\right.$, $\left.\left(\mathbf{x}_{T-1}, \mathbf{u}_{T-1}, \mathbf{x}_{T}\right)\right\}$ as the training set, the loss function is as follows:

$$
\mathcal{L}=\sum_{\left(\mathbf{x}_{t}, \mathbf{u}_{t}, \mathbf{x}_{t+1}\right) \in \mathcal{D}} \mathcal{L}^{\text {bound }}\left(\mathbf{x}_{t}, \mathbf{u}_{t}, \mathbf{x}_{t+1}\right)+\lambda \operatorname{KL}\left(\widetilde{Q}_{\psi}(\widetilde{Z} \mid \boldsymbol{\mu}_{t}, \mathbf{u}_{t})\left\|Q_{\psi}\left(Z \mid \mathbf{x}_{t+1}\right)\right)\right.
$$

where the first term is the variational bound on the marginalized log-likelihood for each data point:

$$
\mathcal{L}^{\text {bound }}\left(\mathbf{x}_{t}, \mathbf{u}_{t}, \mathbf{x}_{t+1}\right)=\underset{\widetilde{\mathbf{z}}_{t+1} \sim \widetilde{Q}_{\psi}}{\mathbb{E}_{\mathbf{z}_{t} \sim Q_{\psi}}}\left(-\log P_{\theta}\left(\mathbf{x}_{t} \mid \mathbf{z}_{t}\right)-\log P_{\theta}\left(\mathbf{x}_{t+1} \mid \widetilde{\mathbf{z}}_{t+1}\right)\right)+\operatorname{KL}\left(Q_{\psi} \| P(Z)\right)
$$

where $P(Z)$ is the prior distribution for $Z$. With the equations above, stochastic gradient variational Bayes can be used to learn the parameters.

According to the generative process in Equation (20) and the definition in Section 4.2, the perception variables $\Omega_{p}=\left\{h_{\varphi}^{\text {enc }}(\cdot), \mathbf{W}_{p}^{*}, \mathbf{x}_{t}, \boldsymbol{\mu}_{t}, \boldsymbol{\sigma}_{t}, \mathbf{p}_{t}, h_{\theta}^{\text {dec }}(\cdot)\right\}$, where $\mathbf{W}_{p}^{*}$ is shorthand for $\left\{\mathbf{W}_{\mu}, \mathbf{b}_{\mu}, \mathbf{W}_{\sigma}, \mathbf{b}_{\sigma}, \mathbf{W}_{p}, \mathbf{b}_{p}\right\}$. The hinge variables $\Omega_{h}=\left\{\mathbf{z}_{t}, \mathbf{z}_{t+1}\right\}$ and the task variables $\Omega_{t}=$ $\left\{\mathbf{A}_{t}, \mathbf{B}_{t}, \mathbf{o}_{t}, \mathbf{u}_{t}, \mathbf{C}_{t}, \boldsymbol{\omega}_{t}, \mathbf{W}_{t}^{*}, h_{\psi}^{\text {trans }}(\cdot)\right\}$, where $\mathbf{W}_{t}^{*}$ is shorthand for $\left\{\mathbf{W}_{A}, \mathbf{b}_{A}, \mathbf{W}_{B}, \mathbf{b}_{B}, \mathbf{W}_{o}, \mathbf{b}_{o}\right\}$.
5.3.4 Discussion. The example model above demonstrates BDL's capability of learning representations that satisfy domain-specific requirements. In the case of control, we are interested in learning representations that can capture semantic information from raw input and preserve local linearity in the space of system states.

To achieve this goal, the BDL-based model consists of two components, a perception component to see the live video and a control (task-specific) component to infer the states of the dynamical system. Inference of the system is based on the mapped states and the confidence of mapping from the perception component, and in turn, the control signals sent by the control component would affect the live video received by the perception component. Only when the two components work interactively within a unified probabilistic framework can the model reach its full potential and achieve the best control performance.

Note that the BDL-based control model discussed above uses a different information exchange mechanism from that in Sections 5.1 and 5.2: it follows the VAE mechanism and uses neural networks to separately parameterize the mean and covariance of hinge variables (e.g., in the encoding model, the hinge variable $\mathbf{z}_{t} \sim \mathcal{N}\left(\boldsymbol{\mu}_{t}, \operatorname{diag}\left(\sigma_{t}^{2}\right)\right)$, where $\boldsymbol{\mu}_{t}$ and $\boldsymbol{\sigma}_{t}$ are perception variables parameterized as in Equation (19)), which is more flexible (with more free parameters) than models like CDL and CDR in Section 5.1, where Gaussian distributions with fixed variance are also used. Note that this BDL-based control model is an LV model as shown in Table 1, and since the covariance is assumed to be diagonal, the model still meets the independence requirement in Section 4.2.

# 5.4 Bayesian Deep Learning for Other Applications 

BDL has found wide applications such as recommender systems, topic models, and control in supervised learning, unsupervised learning, and representation learning in general. In this section, we briefly discuss a few more applications that could benefit from BDL.
5.4.1 Link Prediction. Link prediction has long been a core problem in network analysis and is recently attracting more interest with the new advancements brought by BDL and deep neural networks in general. Reference [120] proposed the first BDL-based model, dubbed relational deep learning (RDL), for link prediction. Graphite [32] extends RDL using a perception component based on graph convolutional networks (GCN) [59]. Reference [75] combines the classic stochastic blockmodel [82] (as a task-specific component) and GCN-based perception component to jointly model latent community structures and link generation in a graph with reported state-of-the-art performance in link prediction.
5.4.2 Natural Language Processing. Besides topic modeling as discussed in Section 5.2, BDL is also useful for natural language processing in general. For example, References [77] and [69] build on top of the BDL principles to define a language revision process. These models typically involve RNN-based perception components and relatively simple task-specific components linking the input and output sequences.
5.4.3 Computer Vision. BDL is particularly powerful for computer vision in the unsupervised learning setting. This is because in the BDL framework, one can clearly define a generative process of how objects in a scene are generated from various factors such as counts, positions, and the content [20]. The perception component, usually taking the form of a probabilistic neural network, can focus on modeling the raw images' visual features, while the task-specific component handles the conditional dependencies among objects' various attributes in the images. One notable work in this direction is Attend, Infer, Repeat (AIR) [20], where the task-specific component involves latent variables on each object' position, scale, appearance, and presence (which is related to counting of objects). Following AIR, variants such as Fast AIR [105] and Sequential AIR [60] are proposed to improve its computational efficiency and performance. Besides unsupervised learning, BDL can also be useful for supervised learning tasks such as action recognition in videos [102], where conditional dependencies among different actions are modeled using a task-specific component.
5.4.4 Speech. In the field of speech recognition and synthesis, researchers have also been adopting the BDL framework to improve both accuracy and interpretability. For example, factorized hierarchical VAE [47, 48] composes VAE with a factorized latent variable model (represented as a PGM) to learn different latent factors in speech data following an unsupervised setting. Similarly, Gaussian mixture VAE [49] uses a Gaussian mixture model as the task-specific component to achieve controllable speech synthesis from text. In terms of speech recognition, recurrent Poisson process units (RPPU) [51] instead adopt a different form of task-specific component; they use a stochastic process (i.e., a Poisson process) as the task-specific component to model boundaries between phonemes and successfully achieve a significantly lower word error rate (WER) for speech recognition. Similarly, deep graph random process (DGP) [52] as another stochastic process operates on graphs to model the relational structure among utterances, further improving performance in speech recognition.
5.4.5 Time Series Forecasting. Time series forecasting is a long-standing core problem in economics, statistics, and machine learning [36]. It has wide applications across multiple areas. For example, accurate forecasts of regional energy consumption can provide valuable guidance to

optimize energy generation and allocation. In e-commerce, retails rely on demand forecasts to decide when and where to replenish their supplies, thereby avoiding items going out of stock and guaranteeing fastest deliveries for customers. During a pandemic such as COVID-19, it is crucial to obtain reasonable forecasts on hospital workload and medical supply demand to best allocate resources across the country. Needless to say, an ideal forecasting model requires both efficient processing of high-dimensional data and sophisticated modeling of different random variables, either observed or latent. BDL-based forecasting models [21, 27, 90, 124] achieve these with an RNN-based perception component and a task-specific component handling the conditional dependencies among different variables, showing substantial improvement over previous non-BDL forecasting models.
5.4.6 Health Care. In health-care-related applications [91], it is often desirable to incorporate human knowledge into models, either to boost performance or more importantly to improve interpretability. It is also crutial to ensure models' robustness when they are used on under-represented data. BDL therefore provides a unified framework to meet all these requirements: (1) with its Bayesian nature, it can impose proper priors and perform Bayesian model averaging to improve robustness; (2) its task-specific component can naturally represents and incorporate human knowledge if necessary; (3) the model's joint training provides interpretability for its both components. For example, Reference [38] proposed a deep Poisson factor model, which essentially stacks layers of Poisson factor models, to analyze electronic health records. Reference [110] built a BDL model with experiment-specific priors (knowledge) to control the false discovery rate during study analysis with applications to cancer drug screening. Reference [61] developed deep nonlinear state space models and demonstrated their effectiveness in processing electronic health records and performing counterfactual reasoning. Task-specific components in the BDL models above all take the form of a typical Bayesian network (as mentioned in Section 4.4.1). In contrast, Reference [117] proposed to use bidirectional inference networks, which are essentially a class of deep Bayesian network, as the task-specific component (as mentioned in Section 4.4.2). This enables deep nonlinear structures in each conditional distribution of the Bayesian network and improves performance for applications such as health profiling.

# 6 CONCLUSIONS AND FUTURE RESEARCH 

BDL strives to combine the merits of PGM and NN by organically integrating them in a single principled probabilistic framework. In this survey, we identified such a current trend and reviewed recent work. A BDL model consists of a perception component and a task-specific component; we therefore surveyed different instantiations of both components developed over the past few years, respectively, and discussed different variants in detail. To learn parameters in BDL, several types of algorithms have been proposed, ranging from block coordinate descent, Bayesian conditional density filtering, and stochastic gradient thermostats to stochastic gradient variational Bayes.

BDL draws inspiration and gains popularity both from the success of PGM and from recent promising advances on deep learning. Since many real-world tasks involve both efficient perception from high-dimensional signals (e.g., images and videos) and probabilistic inference on random variables, BDL emerges as a natural choice to harness the perception ability from NN and the (conditional and causal) inference ability from PGM. Over the past few years, BDL has found successful applications in various areas such as recommender systems, topic models, stochastic optimal control, computer vision, natural language processing, health care, and so on. In the future, we can expect both more in-depth studies on existing applications and exploration on even more complex tasks. Besides, recent progress on efficient BNN (as the perception component of BDL) also lays down the foundation for further improving BDL's scalability.
