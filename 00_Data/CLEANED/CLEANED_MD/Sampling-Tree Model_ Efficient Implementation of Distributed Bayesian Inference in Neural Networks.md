# UNIVERSITY OF LEEDS 

This is a repository copy of Sampling-Tree Model: Efficient Implementation of Distributed Bayesian Inference in Neural Networks.

White Rose Research Online URL for this paper:
https://eprints.whiterose.ac.uk/176161/
Version: Accepted Version

## Article:

Yu, Z, Chen, F and Liu, JK orcid.org/0000-0002-5391-7213 (2020) Sampling-Tree Model: Efficient Implementation of Distributed Bayesian Inference in Neural Networks. IEEE Transactions on Cognitive and Developmental Systems, 12 (3). pp. 497-510. ISSN 23798920
https://doi.org/10.1109/tcds.2019.2927808

## Reuse

Items deposited in White Rose Research Online are protected by copyright, with all rights reserved unless indicated otherwise. They may be downloaded and/or printed for private study, or other acts as permitted by national copyright laws. The publisher or other rights holders may allow further reproduction and re-use of the full text version. This is indicated by the licence information on the White Rose Research Online record for the item.

## Takedown

If you consider content in White Rose Research Online to be in breach of UK law, please notify us by emailing eprints@whiterose.ac.uk including the URL of the record and the reason for the withdrawal request.

# Sampling-Tree Model: Efficient Implementation of Distributed Bayesian Inference in Neural Networks 

Zhaofei Yu, Member, IEEE, Feng Chen, Member, IEEE, and Jian K. Liu


#### Abstract

Experimental observations from neuroscience have suggested that the cognitive process of human brain is realized as probabilistic reasoning and further modelled as Bayesian inference. However, it remains unclear how Bayesian inference could be implemented by network of neurons in the brain. Here a novel implementation of neural circuit, named sampling-tree model, is proposed to fulfill this aim. By using a deep tree structure to implement sampling with simple and stackable basic neural network motifs for any given Bayesian networks, one can perform local inference while guaranteeing the accuracy of global inference. We show that these task-independent motifs can be used in parallel for fast inference without intensive iteration and scale-limitation. As a result, this model utilizes the structure benefit of neuronal system, i.e., neuronal abundance and multihierarchy, to perform fast inference in an extendable way.


Index Terms-Sampling-tree model, neural network, Bayesian inference, importance sampling, probabilistic population coding

## I. INTRODUCTION

UNDERSTANDING how the brain works is one of the most challenging problems in 21 century. Our brain can represent probability distribution [1], [2], [3]. The cognitive and perceptive process of the brain is a process of probabilistic reasoning, which has been indicated by a number of psychological and neuroscience experiments [4], [5]. From the macroscopic level, Bayesian models have shown their ability of explaining how the brain perceives the world and have been successfully used in various fields of brain science, such as perception [6], [7], [8], [9], cognition [10], [11], [12], sensorimotor control [5], [13], [14], and decision making [15], [16], [17], [18]. Nevertheless, from the microscopic perspective, it

This work is supported in part by the National Natural Science Foundation of China under Grant 61806011, 61671266, 61836004, in part by National Postdoctoral Program for Innovative Talents under Grant BX20180005, in part by China Postdoctoral Science Foundation under Grant 2018M630036, in part by International Talent Exchange Program of Beijing Municipal Commission of Science and Technology under Grant Z181100001018026, in part by Royal Society Newton Advanced Fellowship under Grant NAF/R1/191082, and in part by Tsinghua University Initiative Scientific Research Program under Grant 20161080084. Corresponding author: Feng Chen; Jian K. Liu.
Z. Yu is with the National Engineering Laboratory for Video Technology, Department of Computer Science and Technology, Peking University, Beijing 100871, China, and also with the Department of Automation, Center for BrainInspired Computing Research, Tsinghua University, Beijing 100084, China, and also with Peng Cheng Laboratory, Shenzhen 518055, China. (e-mail: yuzf12@pku.edu.cn).
F. Chen is with the Department of Automation, Center for Brain-Inspired Computing Research, Tsinghua University, Beijing 100084, China, and also with Beijing Innovation Center for Future Chip, Beijing 100084, China, and also with the Beijing Key Laboratory of Security in Big Data Processing and Application, Beijing 100084, China. (e-mail: chenfeng@tsinghua.edu.cn).
J. K. Liu is with the Centre for Systems Neuroscience, Department of Neuroscience, Psychology and Behaviour, University of Leicester, Leicester LE1 7HA, U.K, and also with Peng Cheng Laboratory, Shenzhen 518055, China (e-mail: jian.liu@leicester.ac.uk).
remains largely unknown how Bayesian inference is implemented by our neuronal systems. Or more precisely, how can a network of spiking neurons implement inference algorithms of Bayesian models. Therefore, it is challenging yet of great importance to build the bridge between Bayesian inference models and possible implementations in neural network. For one thing, it would help us understand the process of human cognition theoretically [3]. For another, recent advancements of neuromorphic chips can improve the computation power by utilizing neural circuits implementation of Bayesian inference [19], [20], [21], [22], [23].

According to recent studies, many types of neural networks (circuits) with different architectures have been proposed to perform inference of probabilistic graphical models, especially Bayesian network. These neural networks differ in the way of expressing probability, which can be classified as probability code, log probability code, population code and samplingbased code [24], [25]. Anastasio et al. [26] used explicit probability code to express probabilities by assuming that the probabilities are proportional to the neuronal response in superior colliculus. In this way, the summation of probabilities can be calculated by summing the overall responses of neurons. The same way of coding was also used in [27]. In order to simplify the multiplication of probabilities, Rao [28], [29] proposed to use log probability code and proved that the differential equations of recurrent neural networks are in coincidence with the inference equations of hidden Markov model, in which the computation of sum-logs was used to approximate the computation of log-sum. Beck and Pouget [30] focused on this approximation problem and set up a precise equivalence relation from first principle. Angela and Dayan [31] employed the same way of coding and built a hierarchy neural network to perform inference of posterior probabilities.

Another important way of coding is probabilistic population coding (PPC) [32], [33], which uses a population of neurons to encode a distribution, instead of probability values. Ma et al. [32] showed that cue integration can be implemented by linear combination of each population activity with PPC. The method was exploited thereafter by Beck et al. to realize Bayesian decision-making [15] and inference of marginalization [34]. In addition, Ma and Rahmati [35] implemented causal inference with PPC. The above mentioned probabilistic codes can be summarized as the assumption that the physiological signals of neurons as a whole follow certain probability distribution. And yet there is another coding method, termed samplingbased coding, which treats neuronal spikes as samples from a particular probability distribution. Buesing et al. [36], [37]

proposed a method to perform inference of marginal probability based on Markov chain Monte Carlo as long as the network meets the neural computability condition (NCC). Shi and Griffiths [38] designed a neural network to implement hierarchical Bayesian inference by importance sampling, but it is limited to simple Bayesian models such as the chain model.

Most of the approaches described above consider how posterior probabilities are represented and optimised. There is a final body of work that deal directly with hierarchical Bayesian inference in the brain from a cognitive neurosciences viewpoint, which is called hierarchical predictive coding. This is a Bayesian filtering scheme that can be formally related to hierarchical extended Kalman filtering (and related to sampling approaches such as particle filtering). There is a large amount of anatomical and physiological evidence suggesting that the visual process uses some form of hierarchical predictive coding [39].

In summary, all these works focus on how a single neuron or a group of neurons implement probabilistic inference of probabilistic graphical models with a small number of nodes and edges. Just as concluded in Pouget et al. [1], "Most studies in neuroscience have focused on problems with a small number of variables, all following simple distributions, for which an optimal solution can be easily derived... Real-life problems, however, are almost always far too complicated to allow for optimal behavior." Besides, as most of the previous studies take advantage of task-specific neural circuit, they are hard to be generalized to solve other inference problems [35]. It is worth considering how to build general-purpose neural networks for large-scale Bayesian models, and that is the goal of this paper. In order to achieve this, the neural network should resemble to the organization structure of the brain. Therefore we propose four brain-inspired principles for designing of neural networks to implement Bayesian inference. 1.) Scalability: the large number of neurons should be taken into account given there are about eighty billion neurons in human brain, which brings powerful representation ability. 2.) Hierarchy: the neural network has a hierarchical structure similar to human brain and it could extract information layer by layer. 3.) Locality: a single neuron or a group of neurons should work in a simple style while complex functions could be achieved when they are connected together. 4.) Parallelizability: the distributed neurons are organized to perform parallel computing simultaneously so that the inference is rapid enough for different tasks.

Based on aforementioned principles and our previous work of sampling-based distributed inference algorithm [40], we propose a sampling-tree model (STM) as a neural network model for Bayesian inference. We characterize this model as STM because it is a probabilistic graphical model with hierarchical tree structure on the whole and enormous neurons representing samples at each node. In this model, the root node represents the problem we would like to infer, such as the inference of a stimulus, or the recognition of an object. The leaf nodes are the evidence we receive from the outside world. The branch nodes represent the intermediate variables.

In short, the main idea of the STM is to perform neural sampling on a deep tree-structured neural circuit. By taking
full advantage of the tree structure, the global inference problem can be converted to the local inference problem. In consequence, we are able to design simple and repeatable basic neural network motifs to perform local reasoning while guaranteeing the accuracy of global reasoning. On the local level, importance sampling is introduced to conduct inference, which utilizes massive number of neurons to sample in parallel so that the posterior probabilities can be calculated without iteration. This means that the STM takes the strategy of trading space for time and the inference process could be quite rapid. We also prove that the proposed model is able to approximate Bayesian inference with high accuracy. Experimental simulations, including integration of multi-cue information and object detection with compositional model, demonstrate that the STM is a general-purpose neural network, which can be used for distributed large-scale Bayesian inference.

To summarize, our contributions include the following aspects:

- We propose a neural circuits model that can implement sample-based inference algorithm, and further implement fast and accurate inference of arbitrary Bayesian networks.
- We prove that the particular independence assumptions of the inference algorithm can be effectively ignored.
- We show that our proposed neural circuit can be used to solve practical cognitive problems, like integration of multi-cue information and object detection.
- We give a functional explanation for neuronal abundance and multi-hierarchy of the brain from a computational perspective.

The rest of this paper is organized as follows. We first discuss the definition of the STM and show how to represent Bayesian models with the STM in section II. Then we show how to perform Bayesian inference with importance sampling from the algorithm level in section III. Section IV gives some theoretical analysis of the proposed sampling-based inference algorithm. The detailed implementations of Bayesian inference with the STM from the neural circuits level are proposed in section V. We show the experimental results in section VI and conclude in section VII. Part of the work has been published as a short conference communication [40].

## II. DEFINITION OF SAMPLING-TREE MODEL

In order to build a general-purpose neural network for large-scale Bayesian models, we propose the sampling-tree model (STM) as shown in Fig. 1a. From the macroscopic viewpoint, this model could be treated as a probabilistic graphical model with a hierarchical tree structure. From the neural level, each node includes a single neuron or a group of neurons representing samples and a number of connections between these neurons. In the STM, the root node represents the problem we want to infer, such as inference of outside stimuli or recognition of an object. The leaf nodes are the evidence we receive from the outside world. The branch nodes represent intermediate variables. Each neuron is viewed

![img-0.jpeg](img-0.jpeg)

Fig. 1. Sampling-tree model. (a) Example of sampling-tree model in neural network, where different evidence feeds into the different groups of neurons in a distributed way. Local computations are done by each group. (b) A non-tree structured Bayesian model. (c) A tree-structured Bayesian model corresponding to the sampling-tree model in (a). A non-tree structured Bayesian model can be converted to a tree-structured Bayesian model by combining some variables, $C_{1}$ and $C_{2}$ here, together into one variable $C_{1,2}$.

as a sample from a special distribution<sup>1</sup>. The connections between neurons are the basis of information transmission or probability calculation, which will be explained in the next sections. In summary, the STM we proposed has a hierarchical structure and includes large numbers of neurons, which is in accordance to the first two principles of brain-inspired neural network architecture, *scalability* and *hierarchy*.

The STM is able to represent tree-structured Bayesian inference because it is a hierarchical tree-structured model on the whole. The difficulty is how to represent non-tree structured Bayesian models. Here we use the conclusion that by combining some variables together, one can convert a non-tree structured Bayesian model into a tree-structured Bayesian model at the cost of greater state space (chapter 10 of [41]). This means that in order to express all the states of a new variable, more neurons are needed than before. As long as there are enough neurons, the STM could represent any kind of Bayesian model.

Fig. 1b and 1c give an example to illustrate how to convert a non-tree structured Bayesian model into a tree-structured Bayesian model. Here the non-tree structured model can be converted to a tree-structured Bayesian model by combining variables $C_{1}$ and $C_{2}$ to get a new variable $C_{1,2}$ (shown in Fig. 1c), and this new model is the same as the tree-structured model of the STM in Fig. 1a, where a population of neurons are used to express a node. Consequently, the STM in Fig. 1a represents the non-tree structured Bayesian model in Fig. 1b. Supposing that the number of the states of variables $C_{1}$ and $C_{2}$ are both 10, the number of the states of variable $C_{1,2}$ will be 100. If each neuron represents a special state, then more neurons are needed to represent the combined variable $C_{1,2}$ than to represent variables $C_{1}$ and $C_{2}$. In fact, the Bayesian models used for real-life problems may include many non-tree structures. As a result, the STM needs numerous neurons when representing these Bayesian models.

## III. BAYESIAN INFERENCE WITH IMPORTANCE SAMPLING

In this section, we propose a sampling-based algorithm to perform Bayesian inference. We will explain the neural network architectures of STM that implement this algorithm in section V. The Bayesian models discussed here are tree-structured Bayesian models. There are two reasons to study this kind of model. Firstly, it is easy to perform inference of tree-structured Bayesian models [41]. Variational-based and sampling-based inference methods, like belief propagation (BP) [41], [42] and Markov chain Monte Carlo (MCMC) [43], [44], are able to perform accurate or nearly accurate inference with the benefit of tree structure. Secondly, the tree-structured models are capable of standing for many non-tree structured models as arbitrary Bayesian model could be converted to a tree-structured Bayesian model by combining some variables together [41].

Bayesian models for real-world problems are complex and the scale size can be very large. Although BP and MCMC can get accurate inference results in some Bayesian models, the existing neural network implementing inference of these models with BP [45], [46], [47] or MCMC [36], [37] are very complicated. Each neuron or a group of neurons in these neural networks are commonly required to realize different and complex calculations, which violates the basic principle of neural system that a single neuron or a group of neurons should work in a simple style, whereas complex functions could be achieved when they are connected together. In addition, it takes considerable time for neural network to converge to the inference result as they need multiple iterations. It is imperative to propose a new and fast inference algorithm and the corresponding neural circuits should and could be implemented by simple and basic networks. Thanks to the

<sup>1</sup>As different neurons have different tuning curves, they can represent different states of a variable.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Decomposition of tree-structured Bayesian network. (a) Example of tree-structured Bayesian network. (b) This Bayesian network is composed of basic network motifs. (c) The basic network motif in each box of (b) is a simple two-layer Bayesian network that consists of a parent node and several children nodes. (d) A special case of the basic network in (c).

Tree structure of Bayesian networks, global inference can be converted to local inference with network decomposition. The local inference problem is then performed by importance sampling, which takes advantage of massive numbers of neurons to sample in parallel. This means the STM can trade space for time so that inference would be quite rapid. Besides, this scheme of local inference guarantees that basic neural network of the STM is simple, which makes STM plausible for large-scale distributed computations.

### A. Decomposition of global inference to local inference

The inference problem considered in this paper includes marginal inference and maximum a posterior (MAP) estimation. By marginal inference, we refer to computing the posterior of the root node being in each state given the state of the leaf nodes. Conversely, MAP estimation refers to finding the most probable state of the root node given the state of leaf nodes.

Specifically, we consider the tree-structured Bayesian network shown in Fig. 2a, where *A* represents the root node, *I*<sub>1</sub>, *I*<sub>2</sub> and *I*<sub>3</sub> denote the leaf nodes. The joint distribution defined on this Bayesian network has the form $$P(A, B_1, B_2, C_1, C_2, C_3, I_1, I_2) = P(A)$$ $$P(B_1|A)P(B_2|A)P(C_1|B_1)P(C_2|B_1)P(C_3|B_2)P(I_1|C_1)$$ $$P(I_2|C_2)P(I_3|C_3)$$. If we have known the prior probability *P(A)* and all the conditional probabilities defined on the right-side of the equality defined above, the inference problem becomes the following two steps:

- Marginal inference: $$P(A|I_1, I_2, I_3)$$
- MAP estimation: $$\arg \max_A P(A|I_1, I_2, I_3).$$

As we can see, when performing marginal inference or MAP estimation of a tree-structured Bayesian network, the belief propagates from bottom to up. A direct idea is to decompose the network into simple and similar networks, then design an inference algorithm for each basic network. Each network could receive belief from all the children networks and at the same time pass its belief to the parent network. The similar structure in all the basic networks and the same inference algorithm guarantee that the whole neural network is composed of basic and repeatable neural network motifs. By analyzing the model in Fig. 2a, we find that there is only one basic network, which consists of several children nodes and a parent node (shown in Fig. 2b–d). If we can propose a rapid inference algorithm for the basic network and design a neural network to implement the algorithm, then the basic networks motifs can be combined to implement inference of the whole Bayesian network.

### B. Inference of tree-structured Bayesian models with importance sampling

In this paper we conduct inference for the basic network motif with importance sampling, which is a method to estimate the value of some function by sampling from a simple distribution rather than the distribution of the interest [48], [49]. Actually importance sampling has been used to estimate the conditional expectation of some functions *f(x)* given the variable *y* [38]:

$$\begin{split}
E(f(x)|y) &= \sum_{x} f(x) P(x|y) = \frac{\sum_{x} f(x)P(y|x)P(x)}{\sum_{x} P(y|x)P(x)} \\
&= \frac{E(f(x)P(y|x))_{P(x)}}{E(P(y|x))_{P(x)}} \approx \sum_{x^i} f(x^i) \frac{P(y|x^i)}{\sum_{x^i} P(y|x^i)}, \\
&x^i \sim P(x),
\end{split} \tag{1}$$

where *x*<sup>*i*</sup> ~ *P(x)* denotes that *x*<sup>*i*</sup> follows the distribution *P(x)*. Note that equation (1) converts the conditional expec-

tation $E(f(x) \mid y)$ to the weighted combination of normalized conditional probabilities $\frac{P\left(y \mid x^{i}\right)}{\sum P\left(y \mid x^{i}\right)}$.

We generalize equation (1) to conduct inference of the basic Bayesian network in Fig. 2c, where the problem is to compute $\sum_{B_{1}, B_{2}, \ldots, B_{n}} P\left(A \mid B_{1}, B_{2}, \ldots, B_{n}\right)$. $P\left(B_{1} \mid I_{1}\right) P\left(B_{2} \mid I_{2}\right) \ldots P\left(B_{n} \mid I_{n}\right)$, and $I_{1}, I_{2}, \ldots, I_{n}$ represent evidence variables of $B_{1}, B_{2}, \ldots, B_{n}$ respectively (not shown in Fig. 2c). One can drive the following equation with importance sampling:

$$
\begin{gathered}
\sum_{B_{1}, B_{2}, \ldots, B_{n}} P\left(A \mid B_{1}, B_{2}, \ldots, B_{n}\right) P\left(B_{1} \mid I_{1}\right) \ldots P\left(B_{n} \mid I_{n}\right) \\
\approx \sum_{B_{1}, B_{2}, \ldots, B_{n}} P\left(A \mid B_{1}, B_{2}, \ldots, B_{n}\right) P\left(B_{1}, B_{2}, \ldots B_{n} \mid I_{1}, \ldots I_{n}\right) \\
\approx \sum_{i} P\left(A \mid B_{1}^{i}, B_{2}^{i}, \ldots, B_{n}^{i}\right) \frac{P\left(I_{1}, I_{2}, \ldots I_{n} \mid B_{1}^{i}, B_{2}^{i}, \ldots, B_{n}^{i}\right)}{\sum P\left(I_{1}, I_{2}, \ldots I_{n} \mid B_{1}^{i}, B_{2}^{i}, \ldots, B_{n}^{i}\right)} \\
=\sum_{i} P\left(A \mid B_{1}^{i}, B_{2}^{i}, \ldots, B_{n}^{i}\right) \frac{P\left(I_{1} \mid B_{1}^{i}\right) P\left(I_{2} \mid B_{2}^{i}\right) \ldots P\left(I_{n} \mid B_{n}^{i}\right)}{\sum P\left(I_{1} \mid B_{1}^{i}\right) P\left(I_{2} \mid B_{2}^{i}\right) \ldots P\left(I_{n} \mid B_{n}^{i}\right)} \\
B_{1}^{i}, B_{2}^{i}, \ldots, B_{n}^{i} \sim P\left(B_{1}, B_{2}, \ldots, B_{n}\right)
\end{gathered}
$$

Note that equation (2) is a function of variable $A$, and it can be further utilized when $A$ is a child node of other nodes. Note that an approximation exists in equation (2), which is

$$
\begin{gathered}
P\left(B_{1} \mid I_{1}\right) P\left(B_{2} \mid I_{2}\right) \ldots P\left(B_{n} \mid I_{n}\right) \\
\approx P\left(B_{1}, B_{2}, \ldots, B_{n} \mid I_{1}, I_{2}, \ldots, I_{n}\right)
\end{gathered}
$$

This approximation can be understood like this. According to the total probability formula, $P\left(B_{1}, B_{2}, \ldots, B_{n} \mid I_{1}, I_{2}, \ldots, I_{n}\right)$ equals:

$$
\begin{aligned}
& P\left(B_{1}, B_{2}, \ldots, B_{n} \mid I_{1}, I_{2}, \ldots, I_{n}\right) \\
& =P\left(B_{1} \mid I_{1}, I_{2}, \ldots, I_{n}\right) P\left(B_{2} \mid B_{1}, I_{2}, \ldots, I_{n}\right) \ldots \\
& \quad P\left(B_{n} \mid B_{1}, B_{2}, \ldots, B_{n-1}, I_{n}\right)
\end{aligned}
$$

By comparing equation (3) and equation (4), we obtain:

$$
\begin{aligned}
& P\left(B_{1} \mid I_{1}\right) P\left(B_{2} \mid I_{2}\right) \ldots P\left(B_{n} \mid I_{n}\right) \\
& \approx P\left(B_{1} \mid I_{1}, I_{2}, \ldots, I_{n}\right) P\left(B_{2} \mid B_{1}, I_{2}, \ldots, I_{n}\right) \ldots \\
& \quad P\left(B_{n} \mid B_{1}, B_{2}, \ldots, B_{n-1}, I_{n}\right)
\end{aligned}
$$

Assumptions that satisfy equation (5) include a set equality of the following sort:

$$
\begin{aligned}
& P\left(B_{1} \mid I_{1}\right)=P\left(B_{1} \mid I_{1}, I_{2}, \ldots, I_{n}\right) \\
& P\left(B_{2} \mid I_{2}\right)=P\left(B_{2} \mid B_{1}, I_{2}, \ldots, I_{n}\right) \\
& \ldots \\
& P\left(B_{n} \mid I_{n}\right)=P\left(B_{n} \mid B_{1}, B_{2}, \ldots, B_{n-1}, I_{n}\right)
\end{aligned}
$$

It implies that some conditional independence assumptions exist in equation (3) and equation (5), such as $B_{1} \perp I_{2}, \ldots, I_{n} \mid I_{1}, B_{2} \perp B_{1}, I_{3} \ldots, I_{n} \mid I_{2}, \ldots$, $B_{n} \perp B_{1}, B_{2}, \ldots, B_{n-1} \mid I_{n}$. A special case of the network in Fig. 2c is that the parent node $A$ has only one child node (shown in Fig. 2d) and equation (2) can be converted to:

$$
\begin{aligned}
\sum_{B} P(A \mid B) P(B \mid I) & \approx \sum_{B^{i}} P\left(A \mid B^{i}\right) \frac{P\left(I \mid B^{i}\right)}{\sum_{B^{i}} P\left(I \mid B^{i}\right)} \\
B^{i} & \sim P(B)
\end{aligned}
$$

Note that there are no conditional independence assumptions in equation (7).

As arbitrary tree-structured Bayesian network could be divided into basic networks in Fig. 2c and 2d, inference of tree-structured Bayesian network can be implemented by the composition of equation (2) and equation (7). Here we give an example to illustrate it. The inference problems in Fig. 2a are marginal inference $P\left(A \mid I_{1}, I_{2}, I_{3}\right)$ and MAP estimation $\arg \max _{A} P\left(A \mid I_{1}, I_{2}, I_{3}\right)$, among which marginal inference can be performed by equation (8):
(see next page)
Here $C_{1}^{i}, C_{2}^{i} \sim P\left(C_{1}, C_{2}\right), C_{3}^{j} \sim P\left(C_{3}\right), B_{1}^{k}, B_{2}^{k} \sim$ $P\left(B_{1}, B_{2}\right), A^{l} \sim P(A) . I\left(A^{l}=a_{t}\right)$ is an indicator function, which equals to 1 only when $A^{l}=a_{t}$. Note that $a_{t}$ is the possible state of the variable $A$ and $t=1,2, \ldots, T$. Equation (8) includes some approximations:

$$
\begin{aligned}
& P\left(C_{1}, C_{2} \mid I_{1}, I_{2}, I_{3}\right) \approx P\left(C_{1}, C_{2} \mid I_{1}, I_{2}\right) \\
& P\left(C_{3} \mid C_{1}, C_{2}, I_{3}\right) \approx P\left(C_{3} \mid I_{3}\right) \\
& P\left(B_{1} \mid C_{1}, C_{2}, C_{3}\right) \approx P\left(B_{1} \mid C_{1}, C_{2}\right) \\
& P\left(B_{2} \mid B_{1}, C_{3}\right) \approx P\left(B_{2} \mid C_{3}\right) \\
& P\left(B_{1}, B_{2} \mid C_{1}^{i}, C_{2}^{i}, C_{3}^{j}\right) \approx P\left(B_{1} \mid C_{1}^{i}, C_{2}^{i}\right) P\left(B_{2} \mid C_{3}^{j}\right)
\end{aligned}
$$

which implies that equation (8) includes some conditional independence assumptions, that are $C_{1}, C_{2} \perp I_{3} \mid I_{1}, I_{2}$, $C_{1}, C_{2} \perp C_{3} \mid I_{3}, B_{1} \perp C_{3} \mid C_{1}, C_{2}, B_{1} \perp B_{2} \mid C_{3}, B_{1} \perp C_{3}^{j} \mid C_{1}^{i}, C_{2}^{i}$, $B_{1} \perp B_{2} \mid C_{3}^{j}$.

In addition, MAP estimation is to choose the state that maximizes the posterior probability, which can be implemented easily after we have known the posterior distribution $P\left(A \mid I_{1}, I_{2}, I_{3}\right)$.

## C. Generation of samples from prior distributions with importance sampling

The precondition of the proposed algorithm is that the samples are generated from some special distributions, like prior distributions, however, not all of these special distributions are known. For example, considering the inference problem in Fig. 2a, we suppose that the samples are generated from the distributions $P\left(C_{1}, C_{2}\right), P\left(C_{3}\right), P\left(B_{1}, B_{2}\right)$ and $P(A)$ in equation (8) while we only know the prior distribution $P(A)$. Therefore one should propose an algorithm to sample from these special distributions and it should be able to be implemented by the STM. Interestingly, we find that importance sampling could solve this problem:

$$
\begin{aligned}
P\left(B_{1}, B_{2}\right) & =\sum_{A} P\left(A, B_{1}, B_{2}\right)=\sum_{A} P(A) P\left(B_{1}, B_{2} \mid A\right) \\
& =\frac{1}{L} \sum_{l=1}^{L} P\left(B_{1}, B_{2} \mid A^{l}\right) . \quad A^{l} \sim P(A)
\end{aligned}
$$

Here $A^{l}$ follows the distribution $P(A)$. Then the probabilities $P\left(C_{1}, C_{2}\right)$ and $P\left(C_{3}\right)$ could be computed based on $P\left(B_{1}, B_{2}\right)$. For example, $P\left(C_{3}\right)$ is calculated by:

$$
\begin{aligned}
P\left(C_{3}\right) & =\sum_{B_{2}} P\left(B_{2}, C_{3}\right)=\sum_{B_{2}} P\left(B_{2}\right) P\left(C_{3} \mid B_{2}\right) \\
& =\frac{1}{K} \sum_{i=1}^{K} P\left(C_{3} \mid B_{2}^{k}\right) . \quad B_{2}^{k} \sim P(B)
\end{aligned}
$$

$$
\begin{aligned}
& P\left(A=a_{t} \mid I_{1}, I_{2}, I_{3}\right) \\
= & \sum_{A, B_{1}, B_{2}, C_{1}, C_{2}, C_{3}} I\left(A=a_{t}\right) P\left(A, B_{1}, B_{2}, C_{1}, C_{2}, C_{3} \mid I_{1}, I_{2}, I_{3}\right) \\
= & \sum_{A, B_{1}, B_{2}, C_{1}, C_{2}, C_{3}} I\left(A=a_{t}\right) P\left(C_{1}, C_{2}, C_{3} \mid I_{1}, I_{2}, I_{3}\right) P\left(B_{1}, B_{2} \mid C_{1}, C_{2}, C_{3}\right) P\left(A \mid B_{1}, B_{2}\right) \\
= & \sum_{A, B_{1}, B_{2}, C_{1}, C_{2}, C_{3}} I\left(A=a_{t}\right) P\left(C_{1}, C_{2} \mid I_{1}, I_{2}, I_{3}\right) P\left(C_{3} \mid C_{1}, C_{2}, I_{3}\right) P\left(B_{1}, B_{2} \mid C_{1}, C_{2}, C_{3}\right) P\left(A \mid B_{1}, B_{2}\right) \\
\approx & \sum_{A, B_{1}, B_{2}, C_{1}, C_{2}, C_{3}} I\left(A=a_{t}\right) P\left(C_{1}, C_{2} \mid I_{1}, I_{2}\right) P\left(C_{3} \mid I_{3}\right) P\left(B_{1}, B_{2} \mid C_{1}, C_{2}, C_{3}\right) P\left(A \mid B_{1}, B_{2}\right) \\
\approx & \sum_{A, B_{1}, B_{2}, C_{1}, C_{2}, C_{3}} I\left(A=a_{t}\right) P\left(C_{1}, C_{2} \mid I_{1}, I_{2}\right) P\left(C_{3} \mid I_{3}\right) P\left(B_{1} \mid C_{1}, C_{2}\right) P\left(B_{2} \mid C_{3}\right) P\left(A \mid B_{1}, B_{2}\right) \\
\approx & \sum_{A, B_{1}, B_{2}} I\left(A=a_{t}\right) P\left(A \mid B_{1}, B_{2}\right)\left(\sum_{i} P\left(B_{1} \mid C_{1}^{i}, C_{2}^{i}\right) \frac{P\left(I_{1}, I_{2} \mid C_{1}^{i}, C_{2}^{i}\right)}{\sum_{i} P\left(I_{1}, I_{2} \mid C_{1}^{i}, C_{2}^{i}\right)}\right)\left(\sum_{j} P\left(B_{2} \mid C_{3}^{j}\right) \frac{P\left(I_{3} \mid C_{3}^{j}\right)}{\sum_{j} P\left(I_{3} \mid C_{3}^{j}\right)}\right) \\
\approx & \sum_{A, B_{1}, B_{2}} I\left(A=a_{t}\right) P\left(A \mid B_{1}, B_{2}\right) \sum_{i} \sum_{j} P\left(B_{1}, B_{2} \mid C_{1}^{i}, C_{2}^{i}, C_{3}^{j}\right) \frac{P\left(I_{1}, I_{2} \mid C_{1}^{i}, C_{2}^{i}\right)}{\sum_{i} P\left(I_{1}, I_{2} \mid C_{1}^{i}, C_{2}^{i}\right)} \frac{P\left(I_{3} \mid C_{3}^{j}\right)}{\sum_{j} P\left(I_{3} \mid C_{3}^{i}\right)} \\
\approx & \sum_{A, i, j} I\left(A=a_{t}\right) \sum_{k} P\left(A \mid B_{1}^{k}, B_{2}^{k}\right) \frac{P\left(C_{1}^{i}, C_{2}^{i}, C_{3}^{j} \mid B_{1}^{k}, B_{2}^{k}\right)}{\sum_{k} P\left(C_{1}^{i}, C_{2}^{i}, C_{3}^{j} \mid B_{1}^{k}, B_{2}^{k}\right)} \frac{P\left(I_{1}, I_{2} \mid C_{1}^{i}, C_{2}^{i}\right)}{\sum_{i} P\left(I_{1}, I_{2} \mid C_{1}^{i}, C_{2}^{i}\right)} \frac{P\left(I_{3} \mid C_{3}^{j}\right)}{\sum_{j} P\left(I_{3} \mid C_{3}^{j}\right)} \\
\approx & \sum_{i} I\left(A^{l}=a_{t}\right) \sum_{k} \frac{P\left(B_{1}^{k}, B_{2}^{k} \mid A^{l}\right)}{\sum_{l} P\left(B_{1}^{k}, B_{2}^{k} \mid A^{l}\right)} \sum_{i, j} \frac{P\left(C_{1}^{i}, C_{2}^{i}, C_{3}^{j} \mid B_{1}^{k}, B_{2}^{k}\right)}{\sum_{k} P\left(C_{1}^{i}, C_{2}^{i}, C_{3}^{j} \mid B_{1}^{k}, B_{2}^{k}\right)} \frac{P\left(I_{1}, I_{2} \mid C_{1}^{i}, C_{2}^{i}\right)}{\sum_{i} P\left(I_{1}, I_{2} \mid C_{1}^{i}, C_{2}^{i}\right)} \frac{P\left(I_{3} \mid C_{3}^{j}\right)}{\sum_{j} P\left(I_{3} \mid C_{3}^{j}\right)}
\end{aligned}
$$

## IV. THEORETICAL ANALYSIS OF CONDITIONAL INDEPENDENCE ASSUMPTIONS

To use sampling to optimize the posterior distributions required for inference, we have made a number of simplifying assumptions that enable the sampling to be local. It turns out that the simplifying assumptions are equivalent to conditional independence assumptions within the generative model (that could be regarded as a mean field approximation). We will take some care to illustrate the particular independence assumptions and the conditions under which they can be, effectively, ignored.

Here we consider the simple networks as in Fig. 2a, of which the inference equation (8) is based on two sets of conditional independence assumptions:

Set 1: $B_{1} \perp C_{3} \mid C_{1}, C_{2}, B_{1} \perp B_{2} \mid C_{3}, B_{1} \perp C_{3}^{j} \mid C_{1}^{i}, C_{2}^{i}$, and $B_{1} \perp B_{2} \mid C_{3}^{j}$,

Set 2: $C_{1}, C_{2} \perp I_{3} \mid I_{1}, I_{2}$ and $C_{1}, C_{2} \perp C_{3} \mid I_{3}$.

The following theorems resolve these conditional independence assumptions respectively. Specifically, we first prove by Theorem 1 that the assumptions in Set 1 do not affect the accuracy of the inference algorithm, which means the inference results will converge to the accurate value with
probability 1 as the sample size tends to infinity. Then we prove by Theorem 2 that the assumptions in Set 2 hold approximately if the structure of the STM includes multilayers.

Theorem 1. Considering the Bayesian network shown in Fig. 3a, we define that: $f_{1}\left(Y_{1}, Y_{2}\right)=$ $\sum_{\substack{Z_{1} \mid Z_{2} \\ M}} P\left(Y_{1}, Y_{2} \mid Z_{1}, Z_{2}\right) P\left(Z_{1} \mid T_{1}\right) P\left(Z_{2} \mid T_{2}\right), f_{2}\left(Y_{1}, Y_{2}\right)=$ $\sum_{i=1}^{M} \sum_{j=1}^{N} P\left(Y_{1}, Y_{2} \mid Z_{1}^{i}, Z_{2}^{j}\right) \frac{P\left(T_{1} \mid Z_{1}^{i}\right)}{\sum_{i=1}^{M} P\left(T_{1} \mid Z_{1}^{i}\right)} \frac{P\left(T_{2} \mid Z_{2}^{j}\right)}{\sum_{j=1}^{N} P\left(T_{2} \mid Z_{2}^{j}\right)}$ $Z_{1}^{i} \sim P\left(Z_{1}\right), Z_{2}^{j} \sim P\left(Z_{2}\right)$, then for arbitrary small number $\varepsilon$, we have:

$$
\lim _{\substack{M \rightarrow \infty \\ N \rightarrow \infty}} P\left(\left|f_{2}\left(Y_{1}, Y_{2}\right)-f_{1}\left(Y_{1}, Y_{2}\right)\right|<\varepsilon\right)=1
$$

The proofs of Theorem 1 is in Appendix A. Theorem 1 shows that $f_{2}\left(Y_{1}, Y_{2}\right)$ is an estimator of $f_{1}\left(Y_{1}, Y_{2}\right)$ and converges to $f_{1}\left(Y_{1}, Y_{2}\right)$ with probability 1 when $M$ and $N$ tend to infinite. With Theorem 1, we can demonstrate that the conditional independent assumptions in Set 1 will not affect the accuracy of the proposed algorithm. Specifically, the conditional independence assumptions used in equation (8) include the following four steps:

![img-2.jpeg](img-2.jpeg)

Fig. 3. Basic Bayesian models for illustrating conditional independence assumptions. (a) A simple Bayesian network for illustrating Theorem 1 and the conditional independence assumptions in Set 1. (b) A multi-hierarchy Bayesian network for illustrating Theorem 2 and the conditional independence assumptions in Set 2.

$$
\begin{gathered}
g_{1}=\sum_{A} I\left(A=a_{t}\right) \sum_{B_{1}, B_{2}} P\left(A \mid B_{1}, B_{2}\right) \sum_{C_{1}, C_{2}, C_{3}}\{ \\
\left.\quad P\left(C_{1}, C_{2} \mid I_{1}, I_{2}\right) P\left(C_{3} \mid I_{3}\right) P\left(B_{1}, B_{2} \mid C_{1}, C_{2}, C_{3}\right)\right\}, \\
g_{2}=\sum_{A} I\left(A=a_{t}\right) \sum_{B_{1}, B_{2}} P\left(A \mid B_{1}, B_{2}\right) \sum_{C_{1}, C_{2}, C_{3}}\{ \\
\left.\quad P\left(C_{1}, C_{2} \mid I_{1}, I_{2}\right) P\left(C_{3} \mid I_{3}\right) P\left(B_{1} \mid C_{1}, C_{2}\right) P\left(B_{2} \mid C_{3}\right)\right\}, \\
g_{3}=\sum_{A} I\left(A=a_{t}\right) \sum_{B_{1}, B_{2}}\left\{P\left(A \mid B_{1}, B_{2}\right)\left(\sum_{i} P\left(B_{1} \mid C_{1}^{i}, C_{2}^{i}\right)\right.\right. \\
\left.\left.\frac{P\left(I_{1}, I_{2} \mid C_{1}^{i}, C_{2}^{i}\right)}{\sum_{i} P\left(I_{1}, I_{2} \mid C_{1}^{i}, C_{2}^{i}\right)}\right)\left(\sum_{j} P\left(B_{2} \mid C_{3}^{j}\right) \frac{P\left(I_{3} \mid C_{3}^{j}\right)}{\sum_{j} P\left(I_{3} \mid C_{3}^{j}\right)}\right)\right\} \\
C_{1}^{i}, C_{2}^{i} \sim P\left(C_{1}, C_{2}\right) \quad C_{3}^{j} \sim P\left(C_{3}\right), \\
g_{4}=\sum_{A} I\left(A=a_{t}\right) \sum_{B_{1}, B_{2}} P\left(A \mid B_{1}, B_{2}\right) \sum_{i} \sum_{j}\{ \\
\left.\quad P\left(B_{1}, B_{2} \mid C_{1}^{i}, C_{2}^{i}, C_{3}^{j}\right) \frac{P\left(I_{1}, I_{2} \mid C_{1}^{i}, C_{2}^{i}\right)}{\sum_{i} P\left(I_{1}, I_{2} \mid C_{1}^{i}, C_{2}^{i}\right)} \frac{P\left(I_{3} \mid C_{3}^{j}\right)}{\sum_{j} P\left(I_{3} \mid C_{3}^{j}\right)}\right\} \\
C_{1}^{i}, C_{2}^{i} \sim P\left(C_{1}, C_{2}\right) \quad C_{3}^{j} \sim P\left(C_{3}\right) .
\end{gathered}
$$

The transformation from equation (13) to equation (14) includes the conditional independence assumptions $B_{1} \perp C_{3} \mid C_{1}, C_{2}, \quad B_{1} \perp B_{2} \mid C_{3}$. The transformation from equation (14) to equation (15) is based on importance sampling. Equation (16) includes the assumptions $B_{1} \perp C_{3}^{j} \mid C_{1}^{i}, C_{2}^{i}, \quad B_{1} \perp B_{2} \mid C_{3}^{j}$. With Theorem 1 , one can prove that for arbitrary small number $\varepsilon$, $\lim _{N \rightarrow \infty} P\left(\left|g_{4}-g_{1}\right|<\varepsilon\right)=1$ with $M$ and $N$ representing the sample sizes of $C_{1}^{i}, C_{2}^{i}$ and $C_{3}^{j}$ respectively.

The above results illustrate that the conditional independence assumptions in Set 1 do not affect the accuracy of our algorithm. Thus we are able to regard equation (16) as a generalized importance sampling of equation (13). We show in the next section that this sampling-based inference process can be easily implemented by a network of neurons. However, the mathematical principles behind it are complex. The result is universal in our algorithm for different models as long as it includes structure as that in Fig. 3a.

Theorem 2. Considering the Bayesian network shown in Fig. 3b, the prior distribution $P(X)$ and conditional distribution $P\left(Z_{t} \mid Y_{t, n}\right)$ are created by generated some numbers randomly from a uniform distribution on $[0,1]$ and then normalizing them $(t=1,2)$. Similarly, the conditional distribution $P\left(Y_{t, 1} \mid X\right)$ and $P\left(Y_{t, i+1} \mid Y_{t, i}\right)$ are generated randomly and the probability of each state is non-zero $(i=1,2, \ldots, n-1$ and $t=1,2)$, then we conclude that $Z_{1} \perp Z_{2}$ when $n$ tends to infinite.

The proofs of Theorem 2 is in Appendix B. Theorem 2 shows that the dependence between $Z_{1}$ and $Z_{2}$ decrease as the hierarchy increases and will converge to zero if the hierarchy tends to infinite. We use this theorem to explain that the conditional independence assumptions in Set 2 are reasonable. With Theorem 2, we can prove that the variables $C_{1}, C_{2}$ and $C_{3}$ are approximately independent, which means $P\left(C_{1}, C_{2}, C_{3}\right)=P\left(C_{1}, C_{2}\right) P\left(C_{3}\right)$. Then we can get:

$$
\begin{aligned}
& P\left(C_{1}, C_{2} \mid I_{1}, I_{2}, I_{3}\right) \\
= & \frac{\sum_{C_{3}} P\left(C_{1}, C_{2}, C_{3}, I_{1}, I_{2}, I_{3}\right)}{\sum_{C_{1}, C_{2}, C_{3}} P\left(C_{1}, C_{2}, C_{3}, I_{1}, I_{2}, I_{3}\right)} \\
= & \frac{\sum_{C_{3}} P\left(C_{1}, C_{2}\right) P\left(C_{3}\right) P\left(I_{1}, I_{2} \mid C_{1}, C_{2}\right) P\left(I_{3} \mid C_{3}\right)}{\sum_{C_{1}, C_{2}} P\left(C_{1}, C_{2}\right) P\left(I_{1}, I_{2} \mid C_{1}, C_{2}\right) \sum_{C_{3}} P\left(C_{3}\right) P\left(I_{3} \mid C_{3}\right)} \\
= & \frac{P\left(I_{1}, I_{2}, C_{1}, C_{2}\right) P\left(I_{3}\right)}{P\left(I_{1}, I_{2}\right) P\left(I_{3}\right)} \\
= & P\left(C_{1}, C_{2} \mid I_{1}, I_{2}\right)
\end{aligned}
$$

and

$$
\begin{aligned}
& P\left(C_{3} \mid C_{1}, C_{2}, I_{3}\right)=\frac{P\left(C_{1}, C_{2}, C_{3}, I_{3}\right)}{\sum_{C_{3}} P\left(C_{1}, C_{2}, C_{3}, I_{3}\right)} \\
= & \frac{P\left(C_{1}, C_{2}\right) P\left(C_{3}\right) P\left(I_{3} \mid C_{3}\right)}{\sum_{C_{3}} P\left(C_{1}, C_{2}\right) P\left(C_{3}\right) P\left(I_{3} \mid C_{3}\right)}=P\left(C_{3} \mid I_{3}\right)
\end{aligned}
$$

which means $C_{1}, C_{2} \perp I_{3} \mid I_{1}, I_{2}, C_{1}, C_{2} \perp C_{3} \mid I_{3}$. From the perspective of Bayesian networks, $C_{1}, C_{2}$ and $C_{3}$ are not inde-

![img-3.jpeg](img-3.jpeg)

Fig. 4. Neural network architecture of the STM for the basic network as in Fig. 2c. Computations done by this network are based on PPC (purple) and three types of biologically plausible operations: normalization (red), multiplication (blue) and linear combination (light blue).

pendent. However this independence can happen in neuronal system as neuronal networks are hierarchical.

In conclusion, the hierarchical structure of the brain can ensure that some conditional independence assumptions are satisfied approximately, thus ensuring the accuracy of the inference algorithm. Now we have proved that our proposed STM can approximate Bayesian inference theoretically. The simulation experiments in later section confirm this point.

## V. NEURAL NETWORK IMPLEMENTATION

In this section we introduce the detailed neural network architecture of STM that can implement sampling-based inference algorithm. In [38], Shi and Griffiths used radial basis function (RBF) networks to implement importance sampling and illustrated that the basic operations of the RBF model have neural correlates. However, they did not show how to calculate prior probabilities. In this study, we will calculate prior probabilities and implement inference in the similar network based on probabilistic population coding (PPC) and several biologically plausible operations. We first show how to implement inference in basic network motif with simple STM. Then we use serial and parallel combination of these basic networks to build a large sale STM to calculate prior probabilities from top to down and perform inference for arbitrary tree-structured Bayesian model from bottom to up.

Before we give detailed circuits of STM, we give a brief introduction of PPC. PPC takes advantages of the variability in neuronal responses and considers that a population of neurons can encode the probability distributions, instead of the values of variables. Specifically, for *N* independent Poisson spiking neurons, the distribution of the responses *r* = {*r*1,*r*2,*…,*r*N*} to the input stimulus *S* is $$P(r|S) = \prod_{i} \frac{e^{-f_i(s)} f_i(s)^{r_i}}{r_i!}$$, where *f<sub>i</sub>*(s) represents the tuning curve of the neuron *i* and is a function of the input stimulus *S*, which represents the average firing rate of stimulus *S* over an infinite number of trials.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Top-down process of calculating prior probabilities. This neural network architecture of the STM is used to calculate prior probabilities of the Bayesian model in Fig. 2a.

With this definition, the distribution of the input stimulus *S* is encoded by the neural activities *r* = {*r*1,*r*2,*…,*r*N*}.

Fig. 4 shows the neural network layout of the STM to implement inference for our basic network motif as in Fig. 2c, which includes PPC and three types of plausible neural operations: normalization, multiplication and linear combination that can be realized by computation in neural circuits [50]. To be specific, there are *m* Poisson spiking neurons, each of which has a specific attribute, like tuning curve, and can represent a specific state of variables *B*1, *B*2, ..., *B<sub>n</sub>*. The distributions of these Poisson spiking neurons follows the prior distribution *P*(*B*1, *B*2, ..., *B<sub>n</sub>*), and the tuning curve of the neuron *i* is supposed to be proportional to the conditional distribution *P*(*I*1, *I*2, ..., *I<sub>n</sub> | B*1<sub>1</sub>, *B*2<sub>2</sub>, ..., *B<sub>n</sub>*), where *I*1, *I*2, ..., *I<sub>n</sub>* are input stimuli. Note that the prior and conditional distributions are known. The output of Poisson spiking neurons are normalized by shunting inhibition and/or synaptic depression [51], [38], [52] (refer to figure 1 of [53] for detailed neural circuit). If we use *y<sub>i</sub>* to express the individual output firing rate of Poisson spiking neuron *i* and *Y* to express the total firing rate, i.e., *Y* = ∑<sub>i</sub> *y<sub>i</sub>*, then:

$$E(y_i/Y = n) = \frac{P(I_{1}, I_{2}, ..., I_{2}|B_{1}^i, B_{2}^i, ..., B_{n}^i)}{\sum_i P(I_{1}, I_{2}, ..., I_{2}|B_{1}^i, B_{2}^i, ..., B_{n}^i)}, \tag{19}$$

which is proved in [38]. This result shows the expectation of the individual firing rate relative to total firing rate equals to normalized conditional probability. The normalized results are linearly combined with their synaptic weights *w<sub>i</sub>* = *P*(*A*|*B*1<sub>1</sub>, *B*2<sub>2</sub>, ..., *B<sub>n</sub><sup>i</sup>*) to get a summation output as

$$E(\sum_i w_i y_i/Y = n) = \sum_i w_i E(y_i/Y = n)$$

$$= \sum_i P(A|B_1^i, B_2^i, ..., B_n^i) \frac{P(I_{1}, I_{2}, ..., I_{2}|B_1^i, B_2^i, ..., B_n^i)}{\sum_i P(I_{1}, I_{2}, ..., I_{2}|B_1^i, B_2^i, ..., B_n^i)}, \tag{20}$$

which equals to the inference result in equation (2).

Next, we illustrate a large neural network with a few more components of the STM for the Bayesian model in Fig. 2a. The two processes are shown in Fig. 5 for the top-down process

of calculating prior probabilities and Fig. 6 for the bottom-up process of performing inference. The whole neural network is the serial and parallel combinations of the basic network motifs.

![img-5.jpeg](img-5.jpeg)

Fig. 6. Bottom-up process of performing inference. This neural network architecture of the STM is used to implement inference of the Bayesian model in Fig. 2a.
Here the whole neural network is the serial and parallel combinations of the basic networks.

We first discuss the top-down process as shown in Fig. 5. There are feature detection neurons $A_{1}, A_{2}, \ldots, A_{L}$ with their states proportional to the prior distribution $P(A)$. Supposing that the synaptic weight to the next layer is $P\left(B_{1}, B_{2} \mid A_{l}\right) / L$, the probability $P\left(B_{1}, B_{2}\right)$ could be calculated by $P\left(B_{1}, B_{2}\right)=\frac{1}{L} \sum_{l=1}^{L} P\left(B_{1}, B_{2} \mid A_{l}\right)$. The states of feature detection neurons in the next layer are then decided by the probability $P\left(B_{1}, B_{2}\right)$. The probabilities $P\left(C_{1}, C_{2}\right)$ and $P\left(C_{3}\right)$ could be calculated in a similar way. This topdown process calculate all the prior probabilities $P\left(B_{1}, B_{2}\right)$, $P\left(C_{1}, C_{2}\right), P\left(C_{3}\right)$ and ensure that the frequencies of these feature detection neurons are proportional to the prior probabilities.

On the contrary, the inference process is bottom-up as shown in Fig. 6. There are $I$ Poisson spiking neurons that encode the variable $C_{1}, C_{2}$ and $J$ Poisson spiking neurons that encode the variable $C_{3}$. The distribution of these Poisson spiking neurons follows the prior distributions $P\left(C_{1}, C_{2}\right)$ and $P\left(C_{3}\right)$. Besides, the tuning curves are proportional to $P\left(I_{1}, I_{2} \mid C_{1}^{i}, C_{2}^{i}\right)$ and $P\left(I_{3} \mid C_{3}^{j}\right)$ respectively. The responses of Poisson spiking neurons in the bottom layer are normalized by shunting inhibition and/or synaptic depression [51], [38], [52]. Using the conclusion in [38], we can get that the expectation of mean firing rates of the Poisson spiking neurons $C_{1}^{i}, C_{2}^{i}$ and $C_{3}^{j}$ are $P\left(I_{1}, I_{2} \mid C_{1}^{i}, C_{2}^{i}\right) / \sum_{i} P\left(I_{1}, I_{2} \mid C_{1}^{i}, C_{2}^{i}\right)$ and $P\left(I_{3} \mid C_{3}^{j}\right) / \sum_{j} P\left(I_{3} \mid C_{3}^{j}\right) \quad$ respectively. These firing rates are multiplied together and fed into the next layer with the synaptic weight $P\left(C_{1}^{i}, C_{2}^{i}, C_{3}^{j} \mid B_{1}^{k}, B_{2}^{k}\right) / \sum_{k} P\left(C_{1}^{i}, C_{2}^{i}, C_{3}^{j} \mid B_{1}^{k}, B_{2}^{k}\right)$
and the outputs of the neurons are $\sum_{i, j} \frac{P\left(C_{1}^{i}, C_{2}^{i}, C_{3}^{j} \mid B_{1}^{k}, B_{2}^{k}\right)}{\sum P\left(C_{1}^{i}, C_{2}^{i}, C_{3}^{j} \mid B_{1}^{k}, B_{2}^{k}\right) \sum_{i} P\left(I_{1}, I_{2} \mid C_{1}^{i}, C_{2}^{i}\right) \sum_{i} P\left(I_{3} \mid C_{3}^{j}\right)}$, where $B_{1}^{k}, B_{2}^{k}$ are feature detection neurons with their states proportional to the prior probability $P\left(B_{1}, B_{2}\right)$. The process is similar in other layers and we can get the posterior probability $P\left(A \mid I_{1}, I_{2}, I_{3}\right)$ in the fourth layer, which equals to the result in equation (8). Based on this, MAP estimation $\arg \max A P\left(A \mid I_{1}, I_{2}, I_{3}\right)$ is easy to be calculated since we only need to add a winner-take-all (WTA) circuit ${ }^{2}$ after the fourth layer.

The STM has the feature that most of computations are done by simple neural network motifs. Therefore, it uses massive number of neurons to sample in parallel and calculates only once without iterations, for instance, the STM can use a thousand neurons to sample one time instead of a neuron sampling a thousand times. As a result, the inference is quite fast and efficient. The apparent cost is that the STM needs a large number of neurons. Luckily, there are about eighty billion neurons in human brain, which seems to be reasonable enough for parallel computing, similar to the computational principle of our proposed STM.

## VI. Simulations

We test the accuracy of the STM for Bayesian inference on two cognitive problems: the integration of multi-cue information and object detection with compositional model. The first one is a benchmark problem used to test the accuracy of Bayesian inference method. The second one is a larger and more complex problem, and it is used to examine whether our method can scale up to large-scale Bayesian model.

## A. Integration of multi-cue information

In our daily life, we often receive sensory information from vision, hearing and tough simultaneously. Experimental evidence shows that the human brain is able to integrate them in a Bayesian style [55]. At the neuronal level, Ma et al. [32] explained that linear combinations of different

[^0]
[^0]:    ${ }^{2}$ WTA circuit is an ubiquitous motif of cortical microcircuits in the brain, which consists of ensemble of excitatory cells with lateral inhibition [54]. With the competition between excitatory cells induced by the inhibition, only the excitatory neuron with the largest membrane can fire.

![img-6.jpeg](img-6.jpeg)

Fig. 7. Simulation of multi-cue integration. (a) Left: A Bayesian model for haptic (green line)-visual (purple line)-auditory (black line) integration, Right: Comparison of the inference results with STM (blue dots) and theoretical value (red line). $\sigma_{S_{H}}^{2}=64, \sigma_{S_{V}}^{2}=16$ and $\sigma_{S_{A}}^{2}=36$. Each point is averaged over 10 trials. (b) Similar to (a) but for visual-auditory integration. $\sigma_{S_{H}}^{2}=\sigma_{S_{V}}^{2}=16$.
neuronal population activities with probabilistic population coding correspond to the process of cue integration. Here we show that our proposed STM can solve multi-cue integration with a high accuracy.

The haptic-visual-auditory integration problem is considered in this paper, which could be modelled by the Bayesian network shown in Fig. 7a. Here $S, S_{H}, S_{V}$ and $S_{A}$ denote the location of the stimulus, haptic, visual and auditory cues, respectively. Supposing that $P(S)$ is a uniform distribution, $P\left(S_{H} \mid S\right), P\left(S_{V} \mid S\right)$ and $P\left(S_{A} \mid S\right)$ are three different Gaussian distributions with the same mean value $S$ and different variances $\sigma_{S_{H}}^{2}, \sigma_{S_{V}}^{2}$ and $\sigma_{S_{A}}^{2}$, then we can infer the posterior probability of $S$ given $S_{H}, S_{V}$ and $S_{A}$ with importance sampling:

$$
\begin{gathered}
P\left(S=s \mid S_{H}, S_{V}, S_{A}\right)=\sum_{S} I(S=s) P\left(S \mid S_{H}, S_{V}, S_{A}\right) \\
=\sum_{i} I\left(S_{i}=s\right) \frac{P\left(S_{H}, S_{V}, S_{A} \mid S_{i}\right)}{\sum_{i} P\left(S_{H}, S_{V}, S_{A} \mid S_{i}\right)} \quad S_{i} \sim P(S)
\end{gathered}
$$

In our simulation, there are 5000 Poisson spiking neurons, the states of which follow the distribution $P(S)$. The tuning curve of the neuron $i$ is supposed to be proportional to the distribution $P\left(S_{H}, S_{V}, S_{A} \mid S_{i}\right)$. The output of Poisson spiking neurons are normalized by shunting inhibition and/or synaptic depression. The normalized results are fed into the output neuron with the synaptic weights $I\left(S_{i}=s\right)$. Fig. 7a illustrates the experimental results, where the inference results obtained by STM match the theoretical values very well. Similar to the previous study [38], the case of 2-cue integration is illustrated in Fig. 7b for the completeness.

## B. Object detection with compositional model

Now we test our sampling-based inference algorithm for large-scale Bayesian model with a compositional model for
(a)
![img-7.jpeg](img-7.jpeg)

Fig. 8. Object detection with a large scale Bayesian model. (a) (left) Example of horse can be decomposed into smaller parts layer by layer with a compositional model. (right) Represented Bayesian model. (b) Simulation of three-layer (left) and four-layer (right) compositional models. Max relative error, mean relative error and error rate decay to zero when sample size is large enough.
object detection. Compositional model is a generative model which represents objects similar to human brain [56], [57], [58]. It assumes that an object can be decomposed into small parts and these parts can be decomposed into smaller and smaller parts until we get the smallest parts, such as the horizontal and vertical lines. The process of object detection is on the contrary, which starts from detecting the smallest parts of the picture and then composes these parts to detect the bigger one until the whole object is detected. A typical example of compositional model is shown in Fig. 8a, a horse can be divided into two small parts and each part can be divided into smaller parts, until we get the basic lines. If we want to use the model to detect the location of a horse in a picture, we first detect all the basic lines, then compose these lines to infer the location of bigger part and for the same to the horse at last.

The compositional model can be modeled by Bayesian networks. Specifically, every node in the Bayesian network represents a special part of the object. A parent node $v$ represents a part of the object. It has $r$ children nodes $C h(v)=\left(v_{1}, v_{2}, \ldots, v_{r}\right)$, which represent $r$ compositional parts of the bigger part. Besides, each node has a random variables attached to it, which is specified by $x$, reflecting the location of the part. Similarly, the variables attached to the children nodes are $x_{C h(v)}=\left(x_{v_{1}}, x_{v_{1}}, \ldots, x_{v_{r}}\right)$, here $x_{v_{1}}, x_{v_{1}}, \ldots, x_{v_{r}}$ are the location of the $r$ compositional parts. Supposing that the total hierarchy of the model is $H$ and the total nodes are $V$, it is easy to see that $V=V_{1} \cup V_{2} \ldots \cup V_{H}$, where $V_{1}, V_{2}, \ldots, V_{H}$ are nodes attached to each level. The prior probability of node in $H$ is defined by $P\left(x_{H}\right)$. Here we suppose that there is only one node in the highest level $H$, which represents the object, and the distribution of variable $x_{H}$ is uniform. The conditional probability distribution of

the children nodes under the condition of the parent node is $P\left(x_{C h(v)} \mid x_{v}\right)$.

With the definitions above, the probability distribution of the model can be computed by the formula:

$$
P(x)=\left(\prod_{v \in V / V_{1}} P\left(x_{C h(v)} \mid x_{v}\right)\right) P\left(x_{H}\right)
$$

Supposing that the nodes in the lowest level of the model are connected to the image directly, and then the conditional probability distribution of the image given the state of these nodes is:

$$
P(I \mid x)=\prod_{v \in V_{1}} P\left(I\left(x_{v}\right) \mid x_{v}\right)
$$

where $I$ is the input image and $P\left(I\left(x_{v}\right) \mid x_{v}\right)$ is probability of the image conditioned on the nodes in the lowest level. As the problem is to detect the location of an object, the inference problem is $x_{H}=\arg \max _{x_{H}} P\left(x_{H} \mid I\right)$, that is, inferring the state of the root node given the input variables.

The represented Bayesian model for the horse is in Fig. 8a. The root node represents the location of the horse and the leaf nodes represent the locations of the basic lines in the picture. Here we calculate posterior probability $P\left(x_{H} \mid I\right)$ with STM and express the result as $P^{S T M}\left(x_{H}=i \mid I\right)(i=1,2, \ldots, N)$, where $N$ represents the number of all possible states of variable $x_{H}$. Meanwhile, the truth of $P\left(x_{H} \mid I\right)$ is expressed as $P^{\text {truth }}\left(x_{H}=i \mid I\right)(i=1,2, \ldots, N)$, which is calculated with the elimination method. The relative error is defined as $\frac{\left|P^{S T M}\left(x_{H}=i \mid I\right)-P^{S T M}\left(x_{H}=i \mid I\right)\right|}{\left|P^{S T M}\left(x_{H}=i \mid I\right)\right.}(i=1,2, \ldots, N)$. Fig. 8 b shows the simulation results for three-layer and four-layer compositional models, where max relative error is the maximum value of the relative error for all state $(i=1,2, \ldots, N)$ of the root node, mean relative error expresses the mean value of the relative error for all states of the root node. Error rate is the accuracy rate when we calculate the maximum a posterior with our method compared to the true value. These three indexes show inference accuracy of our method based on STM. All these errors decrease as sample size increase and will be close to zero when sample size is large enough. Therefore, these experimental results show that our method can get accurate inference for large-scale Bayesian models.

## VII. CONCLUSION AND DISCUSSION

It is of great importance to understand how the brain performs Bayesian inference with a network of neurons. In this paper, we proposed sampling-based inference model, termed sample-tree model, which is a distributed neural network that can implement fast and accurate inference of arbitrary Bayesian model.

Our method is composed of a set of simple and basic neural network motifs, and uses a massive number of neurons to sample in parallel and perform computation locally in space. For example, our method can use a set of 1000 neurons to sample one time instead of a single neuron to sample 1000 times. As a result, the inference is quite fast. The apparent cost is that our method needs large numbers of neurons for sampling. Considering the fact that there are billions of neurons in the brain, and we do perform reasoning quite fast, our method
suggests a plausible way for neural implementation of our cognitive behaviors.

With the great advancements of recent hardwares, including neuromorphic chips, it is expected that our method can be implemented with both artificial neural networks and spiking neural networks, that is a direction we are pursuing. The hardware also provides the basis for large-scale distributed Bayesian inference, which is the main feature of our algorithm.

Although most of current neuroscience experiments are conducted for relatively simple cognition behaviors, some more complex tasks have been proposed, for example hierarchical decision-making task [59]. In future work, we will explore these complex tasks with a large-scale of Bayesian network based on our model.

Another important aspect we did not consider here is learning [60]. Here all the results are based on the condition that we have known prior probabilities and conditional probabilities. In fact, our brain does have the ability to learn the probabilities and update them in time [24]. Some recent works have provided reference experiences for unsupervised learning [61], supervised learning [62] and reward-based learning [63] of the brain, which may be used to solve the learning problem in our paper. Besides, how to combine learning with inference is an active research direction [64], [65]. Future work is needed to unify our method and some learning mechanisms, like spike-timing-dependent plasticity [66], [67], into one framework.

## APPENDIX A

## Proof of THEOREM I

Theorem 1. Considering the Bayesian network shown in Fig. 3a, we define that: $f_{1}\left(Y_{1}, Y_{2}\right)=$ $\sum_{\substack{Z_{1}, Z_{2} \\ M}} P\left(Y_{1}, Y_{2} \mid Z_{1}, Z_{2}\right) P\left(Z_{1} \mid T_{1}\right) P\left(Z_{2} \mid T_{2}\right), f_{2}\left(Y_{1}, Y_{2}\right)=$ $\sum_{i=1}^{M} \sum_{j=1}^{N} P\left(Y_{1}, Y_{2} \mid Z_{1}^{i}, Z_{2}^{j}\right) \frac{P\left(T_{1} \mid Z_{1}^{i}\right)}{\sum_{i=1}^{M} P\left(T_{1} \mid Z_{1}^{i}\right)} \frac{P\left(T_{2} \mid Z_{2}^{j}\right)}{\sum_{i=1}^{N} P\left(T_{2} \mid Z_{2}^{j}\right)}$, $Z_{1}^{i} \sim P\left(Z_{1}\right), Z_{2}^{j} \sim P\left(Z_{2}\right)$, then for arbitrary small number $\varepsilon$, we have:

$$
\lim _{\substack{M \rightarrow \infty \\ N \rightarrow \infty}} P\left(\left|f_{2}\left(Y_{1}, Y_{2}\right)-f_{1}\left(Y_{1}, Y_{2}\right)\right|<\varepsilon\right)=1
$$

Proof. We rewrite $f_{2}\left(Y_{1}, Y_{2}\right)$ as

$$
\begin{aligned}
& f_{2}\left(Y_{1}, Y_{2}\right) \\
= & \sum_{i=1}^{M} \sum_{j=1}^{N} P\left(Y_{1}, Y_{2} \mid Z_{1}^{i}, Z_{2}^{j}\right) \frac{P\left(T_{1} \mid Z_{1}^{i}\right)}{\sum_{i=1}^{M} P\left(T_{1} \mid Z_{1}^{i}\right)} \frac{P\left(T_{2} \mid Z_{2}^{j}\right)}{\sum_{j=1}^{N} P\left(T_{2} \mid Z_{2}^{j}\right)} \\
& Z_{1}^{i} \sim P\left(Z_{1}\right) \\
& Z_{2}^{j} \sim P\left(Z_{2}\right) \\
= & \frac{\frac{1}{M N} \sum_{i=1}^{M} \sum_{j=1}^{N} P\left(Y_{1}, Y_{2} \mid Z_{1}^{i}, Z_{2}^{j}\right) P\left(T_{1} \mid Z_{1}^{i}\right) P\left(T_{2} \mid Z_{2}^{j}\right)}{\frac{1}{M N} \sum_{k=1}^{M} \sum_{l=1}^{M} P\left(T_{1} \mid Z_{1}^{k}\right) P\left(T_{2} \mid Z_{2}^{l}\right)} \\
& Z_{1}^{i} \sim P\left(Z_{1}\right) \quad Z_{2}^{j} \sim P\left(Z_{2}\right) \\
& Z_{1}^{k} \sim P\left(Z_{1}\right) \quad Z_{2}^{l} \sim P\left(Z_{2}\right)
\end{aligned}
$$

The expectation and variance take the form

$$
\begin{aligned}
& E\left(P\left(Y_{1}, Y_{2} \mid Z_{1}^{i}, Z_{2}^{j}\right) P\left(T_{1} \mid Z_{1}^{i}\right) P\left(T_{2} \mid Z_{2}^{j}\right)\right) \\
= & \sum_{Z_{1}^{i}} \sum_{Z_{2}^{j}}\left\{P\left(Y_{1}, Y_{2} \mid Z_{1}^{i}, Z_{2}^{j}\right) P\left(T_{1} \mid Z_{1}^{i}\right) P\left(T_{2} \mid Z_{2}^{j}\right)\right. \\
& \left.\cdot P\left(Z_{1}^{i}\right) P\left(Z_{2}^{j}\right)\right\} \\
= & \sum_{Z_{1}} \sum_{Z_{2}} P\left(Y_{1}, Y_{2} \mid Z_{1}, Z_{2}\right) P\left(T_{1}, Z_{1}\right) P\left(T_{2}, Z_{2}\right) \\
= & f_{1}\left(Y_{1}, Y_{2}\right) P\left(T_{1}\right) P\left(T_{2}\right) \\
& E\left(P\left(T_{1} \mid Z_{1}^{k}\right) P\left(T_{2} \mid Z_{2}^{l}\right)\right) \\
= & \sum_{Z_{1}^{k}} \sum_{Z_{2}^{l}} P\left(T_{1} \mid Z_{1}^{k}\right) P\left(T_{2} \mid Z_{2}^{l}\right) P\left(Z_{1}^{k}\right) P\left(Z_{2}^{l}\right) \\
= & P\left(T_{1}\right) P\left(T_{2}\right) \\
& \operatorname{Var}\left(P\left(Y_{1}, Y_{2} \mid Z_{1}^{i}, Z_{2}^{j}\right) P\left(T_{1} \mid Z_{1}^{i}\right) P\left(T_{2} \mid Z_{2}^{j}\right)\right) \\
= & E\left(\left(P\left(Y_{1}, Y_{2} \mid Z_{1}^{i}, Z_{2}^{j}\right) P\left(T_{1} \mid Z_{1}^{i}\right) P\left(T_{2} \mid Z_{2}^{j}\right)\right)^{2}\right) \\
- & E\left(P\left(Y_{1}, Y_{2} \mid Z_{1}^{i}, Z_{2}^{j}\right) P\left(T_{1} \mid Z_{1}^{i}\right) P\left(T_{2} \mid Z_{2}^{j}\right)\right)^{2} \\
= & \sum_{Z_{1}} \sum_{Z_{2}}\left\{P\left(Y_{1}, Y_{2} \mid Z_{1}, Z_{2}\right)^{2} P\left(T_{1} \mid Z_{1}\right)^{2} P\left(T_{2} \mid Z_{2}\right)^{2}\right. \\
& \left.\cdot P\left(Z_{1}\right)^{2} P\left(Z_{2}\right)^{2}\right\}-f_{1}\left(Y_{1}, Y_{2}\right)^{2} P\left(T_{1}\right)^{2} P\left(T_{2}\right)^{2} \\
& \operatorname{Var}\left(P\left(T_{1} \mid Z_{1}^{k}\right) P\left(T_{2} \mid Z_{2}^{l}\right)\right) \\
= & E\left(\left(P\left(T_{1} \mid Z_{1}^{k}\right) P\left(T_{2} \mid Z_{2}^{l}\right)\right)^{2}\right) \\
- & E\left(P\left(T_{1} \mid Z_{1}^{k}\right) P\left(T_{2} \mid Z_{2}^{l}\right)\right)^{2} \\
= & \sum_{Z_{1}} \sum_{Z_{2}} P\left(T_{1} \mid Z_{1}\right)^{2} P\left(T_{2} \mid Z_{2}\right)^{2} P\left(Z_{1}\right) P\left(Z_{2}\right) \\
- & P\left(T_{1}\right)^{2} P\left(T_{2}\right)^{2}
\end{aligned}
$$

Since

$$
f_{1}\left(Y_{1}, Y_{2}\right) P\left(T_{1}\right) P\left(T_{2}\right) / P\left(T_{1}\right) P\left(T_{2}\right)=
$$

$f_{1}\left(Y_{1}, Y_{2}\right)$, it is easy to use Lemma 1 of [68] to show that for arbitrary small number $\varepsilon$,
$\lim _{\substack{M \rightarrow \infty \\ N \rightarrow \infty}} P\left(\left|f_{2}\left(Y_{1}, Y_{2}\right)-f_{1}\left(Y_{1}, Y_{2}\right)\right|<\varepsilon\right)=1$.

## APPENDIX B

Lemma 1. Supposing that $A_{1}, A_{2}, \ldots, A_{n}$ is randomly generated matrices, and $\operatorname{row}\left(A_{i}\right)=\operatorname{col}\left(A_{i+1}\right)$ holds for $i=1,2, \ldots, n$. Each element of the matrices $A_{1}, A_{2}, \ldots, A_{n}$ is in $[\varepsilon, 1-\varepsilon]$, where $\varepsilon$ is a small number. Besides, the sum of each row of the matrices $A_{1}, A_{2}, \ldots, A_{n}$ is 1. If one define that $C_{k}=\left(\prod_{i=1}^{k} A_{i}^{T}\right)^{T}$, one can conclude that all elements in a special col of $C_{k}$ will tend to a same value when $k$ tends to infinity.

Proof of theorem 2: It is easy to prove $C_{i}=A_{i} C_{i-1}$ if $i \geq 2$ and $C_{i}=A_{i}$ if $i=1$. Besides,
$\operatorname{col}\left(C_{i}\right)=\operatorname{col}\left(A_{1}\right), \operatorname{row}\left(C_{i}\right)=\operatorname{row}\left(A_{i}\right)$. Supposing that $A_{i}=\left[\begin{array}{ccccc}a_{i, 1,1} & a_{i, 1,2} & \ldots & a_{i, 1, n(i)} \\ a_{i, 2,1} & a_{i, 2,2} & \ldots & a_{i, 2, n(i)} \\ \cdot & \cdot & \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot & \cdot & \cdot \\ a_{i, m(i), 1} & a_{i, m(i), 2} & \ldots & a_{i, m(i), n(i)}\end{array}\right], C_{i}=$ $\left[\begin{array}{ccccc}c_{i, 1,1} & c_{i, 1,2} & \ldots & c_{i, 1, n(1)} \\ c_{i, 2,1} & c_{i, 2,2} & \ldots & c_{i, 2, n(1)} \\ \cdot & \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot & \cdot \\ c_{i, m(i), 1} & c_{i, m(i), 2} & \ldots & c_{i, m(i), n(1)}\end{array}\right]$, where $m(i)$ and $n(i)$ represents the row and col of the matrix $A_{i}$. If one use $\widehat{c}_{i, j}$ to express the vector of all the elements in col $j$ of matrix $C_{i}$, then $\max \left(\widehat{c}_{i, j}\right)$ represents the maximum element in col $j$ of matrix $C_{i}$ and $\min \left(\widehat{c}_{i, j}\right)$ represents the minimum element in col $j$ of matrix $C_{i}$. Now for arbitrary $c_{i+1, s, t}$, where $s \in(1,2, \ldots, m(i+1)), t \in(1,2, \ldots, n(1))$, we can get:

$$
\begin{aligned}
c_{i+1, s, t} & =a_{i+1, s, 1} c_{i, 1, t}+a_{i+1, s, 2} c_{i, 2, t} \\
& +\ldots+a_{i+1, s, n(i+1)} c_{i, m(i+1), t}
\end{aligned}
$$

As $\sum_{j=1}^{n(i+1)} a_{i+1, s, j}=1$, equation (30) is the weighted average of col $t$ of matrix $C_{i}$. By using the condition that the arbitrary element of $A_{1}, A_{2}, \ldots, A_{n}$ is in $[\varepsilon, 1-\varepsilon]$, one obtain:

$$
\begin{aligned}
(1-\varepsilon) \min \left(\widehat{c}_{i, t}\right) & +\varepsilon \max \left(\widehat{c}_{i, t}\right) \leq c_{i+1, s, t} \\
& \leq \varepsilon \min \left(\widehat{c}_{i, t}\right)+(1-\varepsilon) \max \left(\widehat{c}_{i, t}\right)
\end{aligned}
$$

which is equivalent to

$$
\begin{aligned}
0 \leq \max \left(\widehat{c}_{i+1, t}\right) & -\min \left(\widehat{c}_{i+1, t}\right) \\
& \leq(1-2 \varepsilon)\left(\max \left(\widehat{c}_{i, t}\right)-\min \left(\widehat{c}_{i, t}\right)\right)
\end{aligned}
$$

Equation (32) can be rewritten as

$$
\begin{aligned}
0 \leq \max \left(\widehat{c}_{i+1, t}\right) & -\min \left(\widehat{c}_{i+1, t}\right) \\
& \leq(1-2 \varepsilon)^{i}\left(\max \left(\widehat{c}_{1, t}\right)-\min \left(\widehat{c}_{1, t}\right)\right)
\end{aligned}
$$

If we compute the limitation for both sides of equation (33) when $i$ tends to infinite, we obtain:

$$
\lim _{i \rightarrow \infty}\left(\max \left(\widehat{c}_{i+1, t}\right)-\min \left(\widehat{c}_{i+1, t}\right)\right)=0
$$

which means that all elements in a special col of $C_{i}$ will tend to a same value.

Theorem 2. Considering the Bayesian network shown in Fig. 3b, the prior distribution $P(X)$ and conditional distribution $P\left(Z_{t} \mid Y_{t, n}\right)$ are created by generated some numbers randomly from a uniform distribution on $[0,1]$ and then normalizing them $(t=1,2)$. Similarly, the conditional distribution $P\left(Y_{t, 1} \mid X\right)$ and $P\left(Y_{t, i+1} \mid Y_{t, i}\right)$ are generated randomly and the probability of each state is non-zero $(i=1,2, \ldots, n-1$ and $t=1,2$ ), then we conclude that $Z_{1} \perp Z_{2}$ when $n$ tends to infinite.

Proof. Supposing that $U_{t, 1}(t=1$ or 2$)$ is a matrix with its element in row $i$ and col $j$ expressed as $u_{t, 1, i, j}$, and $u_{t, 1, i, j}=$ $P\left(Y_{t, 1}=Y_{t, 1}(j) \mid X=X(i)\right)$, where $Y_{t, 1}(j)$ stands for $j$ th element of variable $Y_{t, 1}$ and $X(i)$ stands for $i$ thelement of

variable $X$. Similarly, $U_{t, s}(t=1$ or 2 and $s=1,2 ., n)$ is a matrix with its element in row $i$ and col $j$ expressed as $u_{t, s, i, j}$, and $u_{t, s, i, j}=P\left(Y_{t, s}=Y_{t, s}(j) \mid Y_{t, s-1}=Y_{t, s-1}(i)\right)$. Moreover, $U_{t, n+1}(t=1$ or 2$)$ is a matrix with its element in row $i$ and col $j$ expressed as $u_{t, n+1, i, j}$, and $u_{t, n+1, i, j}=$ $P\left(Z_{t, 1}=Z_{t, 1}(j) \mid Y_{t, n}=Y_{t, n}(i)\right)$, then we have:

$$
\begin{aligned}
P\left(Z_{1}\right) & =\sum_{X} \sum_{Y_{1,1}} \sum_{Y_{1,2}} \ldots \sum_{Y_{1, n}} P(X) P\left(Y_{1,1} \mid X\right) P\left(Y_{1,2} \mid Y_{1,1}\right) \\
& \ldots P\left(Y_{1, n} \mid Y_{1, n-1}\right) P\left(Z_{1} \mid Y_{1, n}\right) \\
& =\sum_{X} P(X) \sum_{Y_{1,1}} P\left(Y_{1,1} \mid X\right) \sum_{Y_{1,2}} P\left(Y_{1,2} \mid Y_{1,1}\right) \\
& \ldots \sum_{Y_{1, n}} P\left(Y_{1, n} \mid Y_{1, n-1}\right) P\left(Z_{1} \mid Y_{1, n}\right) \\
& =\sum_{X} P(X) f\left(X, Z_{1}\right)
\end{aligned}
$$

Similarly,

$$
\begin{aligned}
P\left(Z_{2}\right) & =\sum_{X} \sum_{Y_{2,1}} \sum_{Y_{2,2}} \ldots \sum_{Y_{2, n}} P(X) P\left(Y_{2,1} \mid X\right) P\left(Y_{2,2} \mid Y_{2,1}\right) \\
& \ldots P\left(Y_{2, n} \mid Y_{2, n-1}\right) P\left(Z_{2} \mid Y_{2, n}\right) \\
& =\sum_{X} P(X) \sum_{Y_{2,1}} P\left(Y_{2,1} \mid X\right) \sum_{Y_{2,2}} P\left(Y_{2,2} \mid Y_{2,1}\right) \\
& \ldots \sum_{Y_{2, n}} P\left(Y_{2, n} \mid Y_{2, n-1}\right) P\left(Z_{2} \mid Y_{2, n}\right) \\
& =\sum_{X} P(X) g\left(X, Z_{2}\right) \\
P\left(Z_{1}, Z_{2}\right) & =\sum_{X} \sum_{Y_{1,1}} \sum_{Y_{1,2}} \ldots \sum_{Y_{1, n}} \sum_{Y_{2,1}} \ldots \sum_{Y_{2, n}}\left\{P(X) P\left(Y_{1,1} \mid X\right)\right. \\
& \left.\ldots P\left(Y_{1, n} \mid Y_{1, n-1}\right) P\left(Z_{1} \mid Y_{1, n}\right) P(X) P\left(Y_{2,1} \mid X\right)\right. \\
& \left.\cdot P\left(Y_{2,2} \mid Y_{2,1}\right) \ldots P\left(Y_{2, n} \mid Y_{2, n-1}\right) P\left(Z_{2} \mid Y_{2, n}\right)\right\} \\
& =\sum_{X} P(X) \sum_{Y_{1,1}} P\left(Y_{1,1} \mid X\right) \sum_{Y_{1,2}} P\left(Y_{1,2} \mid Y_{1,1}\right) \\
& \ldots \sum_{Y_{1, n}} P\left(Y_{1, n} \mid Y_{1, n-1}\right) P\left(Z_{1} \mid Y_{1, n}\right) \sum_{Y_{2,1}} P\left(Y_{2,1} \mid X\right) \\
& \cdot \sum_{Y_{2,2}} P\left(Y_{2,2} \mid Y_{2,1}\right) \ldots \sum_{Y_{2, n}} P\left(Y_{2, n} \mid Y_{2, n-1}\right) P\left(Z_{2} \mid Y_{2, n}\right) \\
& =\sum_{X} P(X) f\left(X, Z_{1}\right) g\left(X, Z_{2}\right)
\end{aligned}
$$

where $f\left(X=i, Z_{1}=j\right)$ denotes the element in $i$ th row and $j$ th col of the matrix $\prod_{i=1}^{n+1} U_{1, i}$, and $g\left(X=i, Z_{2}=j\right)$ denotes the element in $i$ th row and $j$ th col of the matrix $\prod_{i=1}^{n+1} U_{2, i}$. When $n$ goes to infinite, we can prove that all the elements in each col of $\prod_{i=1}^{n+1} U_{1, i}\left(\prod_{i=1}^{n+1} U_{2, i}\right)$ tend to a same value by using lemma 2. It means that $f\left(X, Z_{1}\right)$ and $g\left(X, Z_{2}\right)$ are independent of $X$ respectively. In other words $f\left(X, Z_{1}\right) \approx$
$f_{1}\left(Z_{1}\right)$ and $g\left(X, Z_{2}\right) \approx g_{1}\left(Z_{2}\right)$. Above all, when $n$ goes to infinite, one obtain:

$$
\begin{aligned}
P\left(Z_{1}, Z_{2}\right) & =\sum_{X} P(X) f\left(X, Z_{1}\right) g\left(X, Z_{2}\right) \\
& =\sum_{X} P(X) f_{1}\left(Z_{1}\right) g_{1}\left(Z_{2}\right) \\
& =f_{1}\left(Z_{1}\right) g_{1}\left(Z_{2}\right) \\
& =\left(\sum_{X} P(X) f_{1}\left(Z_{1}\right)\right)\left(\sum_{X} P(X) g_{1}\left(Z_{2}\right)\right) \\
& =\left(\sum_{X} P(X) f\left(X, Z_{1}\right)\right)\left(\sum_{X} P(X) g\left(X, Z_{2}\right)\right) \\
& =P\left(Z_{1}\right) P\left(Z_{2}\right)
\end{aligned}
$$

which means $Z_{1} \perp Z_{2}$ as $n$ tends to infinite.

## ACKNOWLEDGMENT

We would like to thank Jianwu Dong, Yi Gao and You Zhou for helpful discussion.
