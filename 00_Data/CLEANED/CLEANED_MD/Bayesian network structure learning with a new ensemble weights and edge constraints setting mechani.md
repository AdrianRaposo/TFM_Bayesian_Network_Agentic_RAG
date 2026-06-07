# Bayesian network structure learning with a new ensemble weights and edge constraints setting mechanism 

Kaiyue Liu ${ }^{1} \cdot$ Yun Zhou ${ }^{1}$ (D) $\cdot$ Hongbin Huang ${ }^{2}$<br>Received: 25 June 2023 / Accepted: 21 January 2024 / Published online: 4 June 2024<br>(c) The Author(s) 2024


#### Abstract

Bayesian networks (BNs) are highly effective in handling uncertain problems, which can assist in decision-making by reasoning with limited and incomplete information. Learning a faithful directed acyclic graph (DAG) from a large number of complex samples of a joint distribution is currently a challenging combinatorial problem. Due to the growing volume and complexity of data, some Bayesian structure learning algorithms are ineffective and lack the necessary precision to meet the required needs. In this paper, we propose a new PCCL-CC algorithm. To ensure the accuracy of the network structure, we introduce the new ensemble weights and edge constraints setting mechanism. In this mechanism, we employ a method that estimates the interaction between network nodes from multiple perspectives and divides the learning process into multiple stages. We utilize an asymmetric weighted ensemble method and adaptively adjust the network structure. Additionally, we propose a causal discovery method that effectively utilizes the causal relationships among data samples to correct the network structure and mitigate the influence of Markov equivalence classes (MEC). Experimental results on real datasets demonstrate that our approach outperforms state-of-the-art methods.


Keywords Curriculum learning $\cdot$ Integrated weight $\cdot$ Structure learning $\cdot$ Causal correction $\cdot$ Robustness

## Introduction

BNs [1], consisting of Directed Acyclic Graphs (DAGs) and Conditional Probability Tables (CPTs), are a subset of probabilistic graphical models. This graphical modeling approach has found widespread applications in diverse domains, including social network analysis [2], biology [2, 3], and logistics planning. Representing a fusion of graph theory and probability theory, BNs utilize graph models to provide intuitive and structural representations of complex issues. In the real world, there are numerous uncertain problems, and the sources of these uncertainties encompass various aspects, such as incomplete information, measurement errors, randomness, variability, complexity, external environ-

[^0]mental changes, and human subjective factors. Uncertainty problems can usually be solved through methods such as probability modeling and inference, robust design, fault detection and tolerance, optimization and decision-making.

Compared to other methods, BNs have a unified modeling framework, powerful inference capabilities, flexible updating and adaptability, interpretability and visualization, and the advantage of integrating domain knowledge when dealing with uncertainty problems. This makes BNs an important tool and method for handling uncertainty problems. For example, in control systems, various factors such as parameters and modeling uncertainties [4], external disturbances and noise [5], nonlinearity and complexity, as well as time delays and communication delays, introduce numerous uncertainties. BNs can provide a probabilistic modeling and inference tool to help deal with uncertainties in the system. They can more accurately represent and infer the state of the system and its uncertainties. They can also design control methods to address these uncertainties, such as adaptive control [6, 7], model predictive control [8, 9], nonlinear control [10], filtering and estimation [11, 12], and robust control [13, 14], among others. With the increasing demand for uncertainty modeling and probabilistic inference, BNs have been widely


[^0]:    1 National Key Laboratory of Information Systems Engineering, National University of Defense Technology, No. 109 Deya Road, Kaifu District, Changsha City, Hunan Province, China
    2 Laboratory for Big Data and Decision, National University of Defense Technology, No. 109 Deya Road, Kaifu District, Changsha City, Hunan Province, China

used in various fields, including risk assessment [15], fault diagnosis [16], decision systems [17], gene sequence analysis [18], biomedical image processing [19], and other areas. BN learning consists of parameter learning and structure learning. Before utilizing BN to tackle real-world problems, it is essential to construct the structure of the BN. The accuracy of this structure directly impacts the accuracy of parameter learning and inference results, making BN structure learning (BNSL) the foundation of parameter learning and a core problem in the learning process.

In the early stages, BN was constructed manually by experts, a process that was not only time-consuming and labor-intensive but also influenced by the subjective judgment of the experts, resulting in strong subjectivity and limitations. With the advancement in data volume and computational power, researchers have focused on methods for automatic learning from data. However, finding the optimal BN structure has been proven to be NP-hard [20]. Additionally, the presence of noise and missing data exacerbates the uncertainty and unreliability in the process of learning the structure. Consequently, efficiently and accurately constructing BN structures from data has become one of the most challenging tasks.

Existing BNSL methods can be categorized into three types: constraint-based (CB), scoreand-search (SS), and hybrid approaches.

CB methods represent the structure learning problem as a constraint satisfaction problem. These algorithms examine the relationships of conditional independence (CI) between different variables to construct the network structure. Some notable algorithms in this category are the PC algorithm [21], grow-shrink (GS) algorithm [22], and IAMB algorithm [23]. The PC algorithm laid the foundation for the development of the CB methods. However, the output of the PC algorithm is dependent on the order and becomes more noticeable in highdimensional environments, leading to highly variable results. Therefore, many researchers have studied and improved the PC algorithm. Li et al. [24] mitigated the issue of high-order CI tests by introducing the FEPC algorithm. Additionally, some scholars have addressed the instability caused by the PC algorithm's dependency on the order of nodes and proposed the PC-stable algorithm [25], PC-parallel [26], the PC-MI algorithm [27], and other algorithms [28]. CB methods can handle a wider range of data types and distributions, and they are computationally efficient, making them highly interpretable. However, the accuracy of the learning process depends on the number of CI tests performed and the size of the constraint set. They are sensitive to CI tests and data noise, and high-order dependencies are unreliable for large networks and complex data.

SS methods design scoring functions to assign scores to all possible structures and utilize search algorithms to find the optimal structure. SS methods transform the problem of structure learning into a combinatorial optimization problem. Representative scoring functions include the BDeu [29], AIC [30], BIC [31], and others [32]. Most BNSL methods search within the space of DAGs. However, the search space for DAGs exhibits exponential growth as the number of nodes increases. Some greedy search algorithms [33, 34] have low efficiency and slow convergence speed. Therefore, researchers have explored various heuristic algorithms to improve search speed, such as genetic algorithms [35], particle swarm algorithms [36], and bee algorithms. The SS method may still be subject to search boundaries and space limitations. Additionally, the scoring function has score equivalence, which means that the resulting network structure may still be influenced by the issue of MEC and display a significant number of reverse edges.

Hybrid approaches combining the above two approaches have gradually become the mainstream of research in BNSL. Hybrid approaches leverage the advantages of both approaches. They first reduce the search space by conducting tests on conditional independence and then utilize SS method for learning. Some notable algorithms in this category are the the classic max-min hill-climbing (MMHC) algorithm [37] and SaiyanH [38]. Hybrid approaches often have a high computational complexity and can be sensitive to the initial network structure. The efficiency of hybrid algorithms depends on the search strategy employed, and in certain instances, it may not be feasible to find the precise global optimum.

In our work, our main focus is on PC algorithm because it has broader applicability and high scalability. Literature has shown that CB algorithms can efficiently learn sparse graphs with hundreds or thousands of variables [39]. We aim to address two challenges. Firstly, the quality of the learned directed graph through constraint-based learning methods is highly influenced by the order of variable pairing and the order of selecting the condition sets used to test conditional independence. Secondly, data noise can strongly interfere with algorithms. Data-driven algorithms often perform poorly when they encounter randomness caused by small sample sizes or a large number of negative samples.

Curriculum learning (CL), as advocated by Bengio [40], suggests that models should initially learn from easier samples and gradually transition to more complex ones. From a data perspective, the CL strategy can adaptively adjust the weights of different samples, effectively reducing the negative impact on the learning process caused by challenging samples. In subsequent years, many researchers have developed CL strategies for specific applications, such as weakly supervised object localization [41], object detection, and neural machine translation [42]. These studies have shown compelling benefits of CL in small-batch sampling. Existing research has also started to investigate the integration of BNSL and CL [43], but the problem of reducing the adverse

effects of samples in the learning process has not been thoroughly addressed. Additionally, in the process of CL, the issue of uneven sample distribution and the propagation of learning errors throughout different stages of the curriculum have not been adequately addressed.

To address these challenges, we propose a more robust mechanism. We first introduce a multi-perspective influence estimation method to assess the degree of interaction among network nodes. We then divide the learning process into different curriculum stages based on the outcome. We employ a progressive weighting and staged learning approach to acquire the network structure. This involves assigning different curriculum weights based on the learning outcomes at each stage and dynamically adjusting the network structure to reduce the impact of negative samples and noisy data on the algorithm. Additionally, we propose effectively utilizing causal relations among data samples to correct the network structure, thereby mitigating the influence of MEC and improving the robustness of the learned network structure.

Contributions. Our work proposes a new method for progressively learning BN structures The specific contributions of this article are emphasized as follows:

1. To mitigate noise interference between samples and account for the stability of individual nodes, as well as the strength of mutual influences between nodes, we propose a multi-perspective influence assessment method. This method aims to evaluate the difficulty level of node learning.
2. Based on this assessment, we divide the learning process into different curriculum stages. By considering multiple perspectives and taking into account both individual node stability and the strength of mutual influences, our method provides a comprehensive evaluation of the learning difficulty of each node, allowing us to design a more effective curriculum for structure learning.
3. In order to prevent error propagation across different stages of the curriculum, we integrate the learning outcomes from each stage and adaptively adjust the final network structure. By combining the learned structures from different curriculum stages, we can effectively utilize the strengths and knowledge obtained at each stage to improve the overall learning performance and reduce the impact of potential errors.
4. In Sect. Causal correction mechanism, we investigate the use of hidden compact representation (HCR) [44] for BNs and propose a causal correction mechanism to capture potential causal relationships between variables and accordingly refine the network structure. This mechanism utilizes causal learning to address the influence of MEC and improve the accuracy and interpretability of the learned BNs.
5. Finally, in Sect.Experiment, we provided under different standard data set of a large number of experiments, compared with a PC, HC, MMHC, NOTEARS [45] algorithm, we show that PCCL-CC is capable of obtaining DAG with better accuracy, namely the lower Structural Hamming Distance (SHD).

## Preliminaries

Definition 1 Bayesian network BN is represented by a pair $(G, \Theta)$, where $G$ and $\Theta$ indicate the structure and the conditional probability distributions, respectively. Let $G=(V, E)$ be a DAG structure, where $V=\left\{X_{1}, \ldots, X_{n}\right\}$ is the set of n nodes, where each node $X_{i}$ corresponds to a random variable of BN, and $E=\left\{\left(X_{1}, X_{2}\right), \ldots,\left(X_{i}, X_{j}\right)\right\}$ represents the set of directed edges that describes the conditional dependencies over $V$.

BNs can represent the joint probability distribution of a large set of variables and analyze the relationship between them. By assuming data independence, when the parent node is known, $X_{i}$ is independent of its non-child nodes. The joint probability distribution of a node can be factorized as the product of each individual node's conditional probability given its parents, following the chain rule of probability:
$p(x)=\prod_{i=1}^{n} p\left(x_{i} \| p a_{i}\right)$
where $p a_{i}$ represents the parent node of mode $x_{i}$.
Definition 2 Mutual Information Entropy (MI) MI is the amount of information contained in one random variable about another random variable, or the reduced uncertainty of one random variable owing to another random variable being known.

Let the joint distribution of two random variables $(X, Y)$ be $p(x, y)$, and the marginal distributions are $p(x), p(y)$. The MI $I(X ; Y)$ is the relative entropy of the joint distribution $p(x, y)$ and the marginal distribution $p(x), p(y)$, viz.
$I(X ; Y)=\sum_{x \in X} \sum_{y \in Y} p(x, y) \log \frac{p(x, y)}{p(x) p(y)}$
Definition 3 Information Entropy Information entropy [46] represents the average amount of information in the information flow. For the information composed of several discrete sources, the information entropy can be represented by the mean of the negative logarithm of the source probability as

$H\left(X_{i}\right)=E\left[-\log p_{i}\right]=-\sum_{i=1}^{n} \log \frac{p_{i}}{n}$.
where $H$ is the information entropy, and $p_{i}$ represents the probability of each source. For the information of a continuous source [47], $p(x)$ is the distribution of $x$, the information entropy can be expressed as

$$
\begin{aligned}
H(X) & =E_{x \sim X}[-\log p(x)]=-\sum_{x} \log \frac{1}{P(x)} \\
& =-\sum_{x} P(x) \log P(x)
\end{aligned}
$$

Definition 4 Conditional independence Two random variables $X$ and $Y$ are conditionally independent given $S$, denoted by $\operatorname{Ind}(X ; Y \mid S)$, if $p(x, y \mid s)=p(x \mid s) p(y \mid s)$, for all values $x \in X, y \in Y$, and $s \in S$ such that $p(s)>0$, where $X, Y$, and $S$ are the domains of $x, y$, and $s$, respectively.

Definition 5 d-separation Given a causal graph $G=(V, E)$, an undirected path $\rho$ between two distinct vertices $X \in V$ and $Y \in V$ given a conditioning set $S \subseteq V\{X, Y\}$ is open, if (i) every collider of $\rho$ is in $S$ or has a descendant in $S$, and (ii) no other nodes of $\rho$ are in $S$. If a path is not open, then it is blocked. Two variables $X$ and $Y$ are d-separated given a conditioning set $S$, denoted by $X \perp Y \mid S$.

Definition 6 Markov Property Given a DAG $G$ and the joint probability distribution $P$ of all nodes, if $X_{i}$ and $X_{j}$ are dseparated by $S \Rightarrow X_{i} \perp X_{j} \mid S$ then this distribution $P$ is said to satisfy the global Markov property with respect to $G$.

The Markov property is a commonly used assumption in the construction of graphical models. When a distribution over a graph is "Markovian", it indicates that the graph can model certain specific independencies in the distribution. These independencies can be utilized for efficient computation or data storage.

The property that is opposite to it is Faithfulness.
Definition 7 Faithfulness Consider a distribution $P$ and a DAG $G$. If $X_{i} \perp X_{j} \mid S \rightarrow X_{i}$ and $X_{j}$ are d-separated by $S$, then $P$ is faithful about $G$.

Consider the following example. Suppose the probability distribution $P$ over a DAG $G$ is Markov and faithful, then determine the Structure G based on the following conditions.

1. $X \perp Z$ (Variables include X, Y, Z)
2. $X \perp Y \mid Z$ (Variables include X, Y, Z)

The express under two conditions are shown in Fig. 1. The first condition is the unique collision combination, which is the V structure. According to previous knowledge, the collision combination makes $X$ and $Z$ independent, but when conditioned on $Y, X$ and $Z$ become dependent. There is more than one combination that satisfies the second condition. These three structures are called MEC.

Definition 8 Markov Equivalence class(MEC) If DAG $G$ and $H$ have the same d-separation properties, then $G$ and $H$ are Markov equivalent and belong to the same MEC. If $G$ and $H$ are Markov equivalent, then they have the same skeleton and V-structures (also known as collider structures), and vice versa.

Definition 9 Bayesian Information Criterion (BIC) BIC [31] uses the log-likelihood to measure the degree of fit between the structure and the data on the premise that the samples satisfy the assumption of independent and identical distribution. The BIC scoring function is as follows:

$$
\begin{aligned}
B I C(S \mid D)= & \sum_{i=1}^{n} \sum_{j=1}^{q_{i}} \sum_{k=1}^{r_{i}} m_{i j k} \log \theta_{i j k} \\
& -\frac{1}{2} \sum_{i=1}^{n} q_{i}\left(r_{i}-1\right) \log m
\end{aligned}
$$

where, $S$ represents the BN structure composed of variables $\left\{X_{1}, \ldots, X_{n}\right\}, q_{i}$ indicates the number of possible values for the parent node of the variable $x_{i}, r_{i}$ is the number of values of the variable $X_{i}, m_{i j k}$ is the number of samples when the parent node of $X_{i}$ takes the value of $j$, and $X_{i}$ takes the value of $k . \theta_{i j k}=\frac{m_{i j k}}{m_{i j}}$ is the likelihood conditional probability, $0 \leq \theta_{i j k} \leq 1, \sum_{k} \theta_{i j k}=1$.

The first component of BIC corresponds to the logarithm of the optimal likelihood, denoted as the likelihood function value, for a given model $S$. This term assesses the compatibility of the model structure $S$, with the observed data $D$. The subsequent term serves as a penalty, mitigating the impact of model complexity to prevent overfitting.

BIC serves as a pivotal criterion for model selection, offering an evaluation of a model's quality within the context of a specific dataset. It integrates maximum likelihood estimation with a penalty factor addressing the complexity inherent in the model. This integration seeks an equilibrium to circumvent the potential pitfall of overfitting. Consequently, BIC facilitates the identification of the most suitable model for a given dataset, considering both the adequacy of fit and the intricacies of the model.

In the realm of BN structures, a reduced BIC value signifies an improved model. The minimal BIC value signifies an optimal equilibrium between the fitness of the model and its complexity. BIC excels by incorporating considerations of

Fig. 1 Markov Equivalence class

![img-0.jpeg](img-0.jpeg)
model complexity into the model selection process, thereby acting as a safeguard against overfitting.

## BN structure learning based on PCCL-CC algorithm

PCCL-CC is based on the concept of CL and causal correction. We propose a framework for asymmetric weighted integration. By measuring the difficulty of node learning between data samples using a multi-perspective difficulty estimation method, the curriculum stages can be divided reasonably. And we assign varying weights to them. By continuously learning, the algorithm can effectively reduce the interference of sample noise. Additionally, asymmetric weight distribution and integration can be utilized to adaptively adjust the learning structure using constraints. This approach helps to avoid the impact of sampling and individual curriculum stage errors on the overall learning effect. Finally, Traditional BNSL algorithms cannot identify MEC. The PCCL-CC algorithm further utilizes causal correction mechanisms to investigate potential causal relationships in the data, thereby mitigating the influence of MEC on the algorithm from the perspective of causality. We obtain the complete BN structure, as depicted in Fig. 2.

The algorithm is roughly divided into three stages:

Stage 1. Division Curriculum Stage: The initial node for this process is selected by calculating the entropy of the dataset. The node with the smallest entropy $H\left(X_{i}\right)$ is chosen as the initial node for the curriculum stage. The next curriculum node is selected using $M I\left(X_{i}, X_{j}\right)$, which identifies the node with the strongest correlation among the candidate nodes and each node in the curriculum.
Stage 2. Weight Allocation and Edge Constraints: Different weights are allocated to various stages of the learning process, integrating the structures learned at each stage of the curriculum and adaptively removing network structures with low reliability.
Stage 3. Causal Correction: Using the HCR model to discover potential causal relationships between data samples and modify the network structure.

## Division curriculum stage

A curriculum is a sequence of training criteria $C=$ $\left\{Q_{1}, \ldots, Q_{t}, \ldots, Q_{T}\right\}$ on $T$ training steps. Each criterion $Q_{t}$ is a reweighting of the target training distribution $P(z)$ :
$Q_{t}(z) \propto W_{t}(z) P(z) \quad \forall$ example $z \in$ training set $D$
such that the following three conditions are satisfied:
(1) The entropy of distributions gradually increases

$$
H\left(Q_{t}\right)<H\left(Q_{t+1}\right)
$$

(2) The weight $W_{t}(z)$ is monotonically in $t$, i.e.,

$$
W_{t}(z)<W_{t+1}(z) \quad \forall z \in D
$$

(3) $Q_{T}(z)=P(z)$.

Taking inspiration from the structural characteristics of BN, we integrate CL into BNSL problems. In accordance with the BN structural properties, we categorize the nodes representing samples in the BN into distinct curriculum stages. This approach aligns with the inherent features of BN and facilitates a more systematic and structured learning process. Figure 3 displays the curriculum-matching mechanism constructed by the BN.

In accordance with the condition 7, the complexity of acquiring the structure between sample nodes is gauged through the assessment of sample entropy within the dataset, leading to the segmentation of curriculum stages.
we introduces a novel approach that amalgamates information entropy $H$ and mutual information entropy $M I$ to assess the interaction among network nodes from diverse vantage points.

In the context of entropy, it is established that the lower the overall probability of an event, the greater the quantity of information it encapsulates. Put simply, information entropy serves as a metric for the uncertainty associated with variables. When applied to nodes within the network, lower information entropy signifies reduced uncertainty pertaining to the nodes, which facilitates easier learning. Motivated by

![img-1.jpeg](img-1.jpeg)

Fig. 2 Overall Architecture of Algorithm Model
Fig. 3 the curriculum-matching mechanism constructed by the BN
![img-2.jpeg](img-2.jpeg)

the concept of moving from shallow to deep, the initial node $X_{i}$ must satisfy the following condition:
$X_{i}^{*}=\arg \min _{X_{i} \in X} H\left(X_{i}\right)$

The nodes in BN have interdependent relationships, and MI can measure the uncertainty of another node's value based on its value, which meets the condition 7. Further from the perspective of BNSL, if there is a directed edge between two nodes, knowing the state of one node will provide lots of information about the other one, which eliminates more uncertainty and means more correlation. In other words, a higher MI between two variables means there is more likely to have an edge connecting them. However, the existence of the edge still cannot be determined with confidence. Thus, Li et al. [48] both introduce the constraint given by (10) to make the relationship between a pair of variables more explicit.
$I(X ; Y) \geqq \alpha_{M I} \cdot \min (M M I(X), M M I(Y))$
where $\alpha_{M I}$ is a binding parameter with the value in the range of $(0,1)$; The maximum mutual information (MMI) between node X and all other nodes in the structure is denoted by $\operatorname{MMI}(\mathrm{X})$.

If the value of MI between two nodes satisfies (10), the nodes are believed to be strongly correlated, and an edge connecting them should be considered. In previous works, the value of $\alpha_{M I}$ was predefined or changed dynamically [49]. For a fixed parameter, a larger value would lead to an insufficient restriction on the search space, and a smaller value would exclude the right edge from the candidate structures, resulting in low accuracy. In our work, we set the constraint value of MI, denoted as $\alpha_{M I}$, to 0.5 in order to ensure the stability of learning effectiveness.

Therefore, the selection of subsequent curriculum nodes is based on the sequentially obtained mutual influence. By calculating the MI between curriculum nodes and candidate nodes, we can estimate the strength of their correlation. The node with the highest MI is selected as the next node in the curriculum. The curriculum nodes to be learned in the next stage should be met:
$X^{*} \leftarrow \arg \max _{X_{i} \in C_{i}, X_{j} \in H_{i}} M I\left(X_{i}, X_{j}\right)$
where $C_{i}$ is the curriculum sets and the $H_{i}$ is the candidate set. We define the CL step as $t$, the number of nodes requiring new learning in the next stage. The $t$ nodes that meet the condition, and the curriculum set are updated as follows:
$C_{i}=C_{i} \cup\left\{X_{1}^{*}, X_{2}^{*}, \ldots, X_{t}^{*}\right\}$

## Weight allocation and edge constraints

Conditions 8 emphasizes the weight allocation between different curriculum stages, assigning higher weights to initial simple curriculum. From the perspective of data classification, CL can effectively reduce the impact of noisy data in samples. Gong et al. [50] hypothesize that training data with noise/incorrect annotations leads to a deviation between the training distribution and the test distribution, demonstrating the denoising mechanism of CL strategies in real-world datasets. To explain the rationality of the model, we will combine the characteristics of BNSL to further provide theoretical explanations for the CL working mechanism proposed by Gong [50]. In this work, we mainly study the establishment of BN structure. We assume that the data distribution of the BN is $P_{\text {target }}$, the data distribution we train is $P_{\text {train }}$, and we can obtain a simulated curriculum formula. Firstly, we will represent $P_{\text {target }}$ the weighted expression of $P_{\text {train }}$ :
$P_{\text {target }}=\frac{1}{\alpha^{*}} W_{\lambda^{*}}(x) P_{\text {train }}$
where $0 \leq W_{\lambda^{*}} \leq 1, \alpha^{*}=\int W_{\lambda^{*}}(x) P_{\text {train }} d x$ represents the normalization factor. Under weight $W_{\lambda^{*}}, P_{\text {target }}$ actually corresponds to the defined curriculum. In the low confidence region of $P_{\text {target }}$ where complex samples are located, smaller weights should be given, and in the high confidence region where easy samples are located, larger values (close to 1) should be given. Therefore, we can express the above equation as:
$P_{\text {train }}(x)=\alpha^{*} P_{\text {target }}+\left(1-\alpha^{*}\right) E(x)$
where $E(x)$ denotes the distribution represented by $P_{\text {train }}(x)$ under weights $\left(1-W_{\lambda^{*}}(x)\right)$, while $E(x)$ signifies the deviation between $P_{\text {target }}(x)$ and $P_{\text {train }}(x)$. Within highconfidence regions, $E(x)$ aligns with $E(x)$ under weights approaching 0 , leading to a diminished deviation. Conversely, within low-confidence regions, $E(x)$ exerts a more substantial influence on $P_{\text {train }}(x)$. The precision of edge judgment between nodes directly influences the magnitude of the deviation between the actual structure and the constructed structure, with more accurate judgments resulting in smaller deviations.

Therefore, the following curriculum sequence is constructed through theory:
$Q_{\lambda}(x)=\alpha_{\lambda} P_{\text {target }}(x)+\left(1-\alpha_{\lambda}\right) E(x)$
where $\alpha_{\lambda}$ increases with the number of courses from 1 to $\alpha^{*}$. Correspondingly, curriculum $Q_{\lambda}$ a simulates the process of change from $P_{\text {target }}$ to $P_{\text {train }}$, where $Q_{\lambda}$ is represented as
$Q_{\lambda}(x) \propto W_{\lambda}(x) P_{\text {train }}$

and,
$W_{\lambda}(x) \propto \frac{\alpha_{\lambda} P_{\text {target }(x)}+\left(1-\alpha_{\lambda}\right) E(x)}{\alpha^{*} P_{\text {target }(x)}+\left(1-\alpha^{*}\right) E(x)}$
where $0 \leq W_{\lambda}(x) \leq 1$,normalize its maximum value to 1 . The initial stage setting of this CL process $W_{\lambda}(x) \propto \frac{P_{\text {target }(x)}}{P_{\text {target }(x)}}$. It has a higher weight in high confidence regions, while it is much smaller in low confidence regions due to heavy tailed issues. As the number of courses increases $\lambda$ With the increase of, the weight of high confidence areas decreases, while the weight of low confidence areas increases, resulting in a more uniform distribution of weights and smaller changes. After normalizing $W_{\lambda}(x)$ to the interval $[0,1]$, its value tends to be expressed as follows: $\lambda$ The unit continues to increase. Therefore, this meets the weight increase criteria defined for the curriculum in condition 8 .

For BNSL problems, we assign different weights to the edges learned in different curriculum stages. To further reduce uncertainty during each sampling process, we introduced the concept of integrated optimization. It samples the original data and constructs an ensemble learning model every 15 iterations. By assigning a weight matrix set $W$ to each edge in the computational network, we can determine the maximum weight $W_{e_{i j}}$ for each edge. The final network structure is adaptively adjusted based on the weights to enhance the reliability of the learning outcomes.

Adaptively adjust the weight of edges $W_{e_{i j}}$ based on the learning situation at different integration stages, the weight distribution function of each edge $W_{e_{i j}}$ is defined as follows:
$W_{e_{i j}}=\sum_{k=1}^{n} \sum_{s=1}^{m} N_{k s}\left(e_{i j}\right)$
where $n$ denotes the number of optimizations. Further, $s$ denotes the number of curriculum, and $N_{k s}\left(e_{i j}\right)$ denotes the number of occurrences of $X_{i}$ and $X_{j}$ in the side $e_{i j}$ in the curriculum after k iterations.

To ensure the accuracy of the learned DAG and reduce the search space, we impose constraints on the learning edges. We compute the average weight $a v g_{w}$ and set the threshold $\alpha$. If $w_{e_{i j}}<\alpha \cdot a v g_{w}$, we set $e_{i j}=0$. Otherwise, we set $e_{i j}=1$. The initial DAG is then traversed, and any edge with $e_{i j}=0$ is deleted. The specific constraints are given as follows.
$e_{i j}= \begin{cases}1, & W_{e_{i j}} \geqslant \alpha \cdot a v g_{W} \\ 0, & W_{e_{i j}}<\alpha \cdot a v g_{W}\end{cases}$
The PCCL-CC algorithm pseudo-code is shown as Algorithm 1.

```
Algorithm 1: \(\mathrm{DAG}=\mathrm{PCCL}-\mathrm{CC}(\) Data, \(\mathrm{n}, \mathrm{X}, \mathrm{t}, \alpha)\)
    Input: Data: training data; n:sample size; X: the collection of nodes for a BN
        structure; corresponding to the dataset \(\mathrm{t}:\) curriculum learning step size;
        m:curriculum stages; \(\alpha\) : constraint threshold; \(C_{i}:\) the set of curriculum
        nodes; \(H_{i}:\) the set of candidate nodes
    Output: DAG: the BN structure corresponding to the dataset
1 for \(k \in(1,15)\) do
    \(\mathrm{N} \leftarrow\{K\} ;\)
    for \(i \in(1, N)\) do
            compute information entropy \(H\left(X_{i}\right)\)
    end
    \(X^{*} \leftarrow \arg \max _{X_{i}} H\left(X_{i}\right) ;\)
    \(C_{1} \leftarrow X^{*}, \quad H_{1} \leftarrow X \backslash X^{*}\)
    \(k \leftarrow 1 ; \quad m \leftarrow \frac{N}{2}+1 ;\)
    for \(i \in(0, m)\) do
        for \(j \in(0, t)\) do
            if \(H_{i} \neq \emptyset\) then
                \(X^{*} \leftarrow \arg \max _{X \in H_{i-1}} M I\left(X, C_{i}\right) ;\)
                \(C_{i}=C_{i-1} \cup X^{*}\)
                \(H_{i} \leftarrow H_{i-1} \backslash X^{*} ; \quad j \leftarrow j+1 ;\)
            end
        end
            \(\operatorname{Data}_{i} \leftarrow \operatorname{getdata}\left(\operatorname{Data}, C_{i}\right) ;\)
            \(D A G_{i}, W_{i} \leftarrow P C\left(X_{i}, C_{i}, D a t a_{i}\right) ;\)
        end
        \(W=W+W_{i}\)
    end
    \(\operatorname{Avg}_{W}=\frac{W}{\operatorname{len}(W)} ;\)
    if \(W_{e_{i j}} \leq \alpha\) then
        \(E=E \backslash E_{i j}\)
    end
    \(D A G \leftarrow \operatorname{Get} D a g(E) ;\)
    return DAG
```


## Causal correction mechanism

BN model the relationship between causal variables as a probabilistic relationship, constructing the causal network structure by considering the independence and conditional dependence between variables. However, this class of methods suffers from the MEC problem.

To distinguish MEC, existing methods introduce a causal function model. Common causal function models are easily perturbed by discrete categorical data and can be challenged by MEC. Presently, most discrete causal discovery models can only be applied to ordered discrete structures, and their assumptions are easily violated for disordered causal relationships.
we proposes applying the HCR model to BNs and correcting the causal directions of the learned directed edges in the model. The main principle is to identify the correct causal direction within the compressed space of causal directions. The details are shown in Fig. 4. By modeling these two stages, we can derive the likelihood of the model and its maximum likelihood estimation method.

Proposition 1 Given joint distribution $P(X)=P\left(X_{1}, X_{2}\right.$, $\left.\ldots, X_{p}\right)$ which is generated from a multivariate HCR model with graph $G . E_{i j}: X_{i} \rightarrow Z_{i j} \rightarrow X_{j}$ is an edge in $G$. If $\left|Z_{i j}\right|=1$, then $X_{i} \perp X j$.

Proof If $\left|Z_{i j}\right|=1$, any value $x_{j}$ in $X_{j}$ and $x_{i}$ in $X_{i}$ satisfying $P\left(X_{j}=x_{j} \mid X_{i}=x_{i}\right)=P\left(X_{j}=x_{j} \mid Z_{i j}\right)=P\left(X_{j}=x_{j}\right)$ which means that $X_{i} \perp X_{j}$.

Proposition 1 shows an alternative way for detecting the independence in the causal graph which could provide a much effective and more robustness score-based independence detecting method. This method will be used in our structure learning algorithm as a correction phase.

Causal relationship correction is performed on the edge $(x, y)$ in the learned BN structure. The compression mapping mechanism and probability mapping mechanism divide $X \rightarrow Y$ into two stages. The conditional independence $X \perp Y \mid Y^{\prime}$ is satisfied. Given observation data for the edge $(x, y)$, the likelihood of $X \rightarrow Y^{\prime} \rightarrow Y$ is obtained as:

$$
\begin{aligned}
L(M ; D)= & \log \prod_{i}^{m} \sum_{y_{i}^{\prime}} P\left(X=x_{i}, Y^{\prime}=y_{i}^{\prime}, Y=y_{i}\right) \\
= & \log \prod_{i}^{m} \sum_{y_{i}^{\prime}} P\left(X=x_{i}\right) P\left(Y^{\prime}=y_{i}^{\prime} \mid X=x_{i}\right) \\
& P\left(Y=y_{i} \mid Y^{\prime}=y_{i}^{\prime}\right) \\
= & \log \prod_{i}^{m} P\left(X=x_{i}\right) P\left(Y=y_{i} \mid Y^{\prime}=f\left(x_{i}\right)\right)
\end{aligned}
$$

where $P\left(Y=y_{i} \mid Y^{\prime}=f\left(x_{i}\right)\right.$ takes the value of 1 when $y^{\prime}=f\left(x_{i}\right)$ is satisfied; otherwise, it is 0 .

The parameters in $M$ include $f$ and $\theta$, where $\theta$ includes the parameters of $P(X)$ and $P\left(Y \mid Y^{\prime}\right)$. By introducing a penalty term for the number of parameters, the complexity of the model is ensured not to be too high, while avoiding overfitting [44]. The optimal score corresponding to edge $(x, y)$ is given by:

$$
\begin{aligned}
\operatorname{Score}_{(x, y)} & =\sup _{f} \max _{\theta} L(\theta ; D)-\frac{n_{p}}{2} \log m \\
& =\sup _{f} \max _{\theta} \log \prod_{i}^{m} P\left(X=x_{i}\right) P\left(Y=y_{i} \mid Y^{\prime}\right. \\
& =f\left(x_{i}\right))-\frac{n_{p}}{2} \log m \\
& =\sup _{f} \max _{\theta} \log \prod_{x} \hat{a}_{x}^{n_{x}} \prod_{y^{\prime}} \prod_{y} \hat{b}_{y^{\prime}, y}^{n_{y^{\prime}}, y}-\frac{n_{p}}{2} \log m
\end{aligned}
$$

where $n_{p}=(|X|-1)+\left|Y^{\prime}\right|(|Y|-1)$ measures the effective number of parameters in the model, $n_{x}=\sum_{i=1}^{m} I\left(x_{i}=x\right)$ and $n_{y^{\prime}, y}=\sum_{i=1}^{m} I\left(y_{i}^{\prime}=y^{\prime}, y_{i}=y\right)$ indicates the frequency in the sample respectively. the $\hat{a}_{x}=\hat{p}(X=x)=$
$\frac{n_{x}}{\sum_{x} n_{x}}, \hat{b}_{y^{\prime}, y}=\hat{p}\left(Y=y \mid Y^{\prime}=y^{\prime}\right)=\frac{n_{y^{\prime}, y}}{\sum_{y} n_{y^{\prime}, y}}$ denotes the maximum likelihood solution of $P_{X}, P_{Y \mid Y^{\prime}}$.

By comparing the scores of the edges $(X, Y)$ and reverse edges $(Y, X)$ of the network structure, the correct direction of the edge can be determined.

$$
\begin{cases}X \rightarrow Y, & \operatorname{Score}_{(X, Y)}>\operatorname{Score}_{(Y, X)} \\ X \leftarrow Y, & \text { other }\end{cases}
$$

Assumption 1 Consider the multivariate HCR model causal relation $X_{P_{i}} \rightarrow X_{i}$ where $X_{P_{i}}$ is a set of parents of $X_{i}$. For each $X_{k} \in X_{P_{i}}$, the conditional distribution $P\left(X_{i} \mid X_{P_{i}}\right)$ is random in the sense that there does not exist values $x_{i} \neq x_{i}^{\prime}$ such that $\forall x_{k} \in X_{k}, P\left(X_{i}=x_{i}^{\prime} \mid X_{k}=x_{k}\right)=C . P\left(X_{i}=\right.$ $\left.x_{i}^{\prime} \mid X_{k}=x_{k}\right)$ holds with some constant C .

Theorem 1 The directions of edges in $B N$ are distinguishable, and the conditional distribution $P(X \mid Y)$ correctly directed edges have the following property under the certain conditions.

There does not exist values $y_{1} \neq y_{2}$ such that $P(Y=$ $\left.y_{1} \mid X\right)$ equals $P\left(Y=y_{2} \mid X\right) \cdot c$ for all possible $X$ values. where the $c$ is the constant. So in the reverse direction there not exist $X^{\prime}=f(Y)$ with $\left|X^{\prime}\right|<|Y|$ for all possible $X$ and $Y$, make the $P(X \mid Y)=P\left(X \mid X^{\prime}\right)$.

Proof For the correct edges, we have $P(X, Y)=P(X)$ $P(Y \mid X)$. Assum that there exist such a $X^{\prime}=\hat{f}(Y)$ to satisfy $P(X \mid Y)=P\left(X \mid X^{\prime}\right)$. Then we have the $P(X, Y)=$ $P(Y) P\left(X \mid X^{\prime}\right)$. So we have
$P\left(X \mid X^{\prime}\right)=\frac{P(X) P(Y \mid X)}{P(Y)}$.
However, $\left|X^{\prime}\right|<|Y|$, there must exist two values $y_{1} \neq y_{2}$ such that $f\left(y_{2}\right)=f\left(y_{1}\right)$, which implies $P\left(X \mid f\left(y_{2}\right)\right)=$ $P\left(X \mid f\left(y_{1}\right)\right)$. So, we have
$\frac{P(X) P\left(Y=y_{1} \mid X\right)}{P\left(Y=y_{1}\right)}=\frac{P(X) P\left(Y=y_{2} \mid X\right)}{P\left(Y=y_{2}\right)}$.
which is contradicts.Therefore, any causal pair in the reverse direction does not admit a low-cardinality hidden representation.

Theorem 2 Assume that in the causal direction there exists the transformation $Y^{\prime}=f(X)$ such that $P(Y \mid X)=$ $P\left(Y \mid Y^{\prime}\right)$, where $\left|Y^{\prime}\right|<|X|$. Then to produce the same distribution $P(X, Y)$, the reverse direction must involve more effective number of parameters in the model than the right direction.

Essentially, Theorem 2 shows that if each pair has the lowcardinality property as well as Assumption 1 holds, then

Fig. 4 Suitable for causal correction mechanism of BN model
![img-3.jpeg](img-3.jpeg)
we can identify the causal relationship even in the multivariate case. Based on Theorem 2, we can further assume the faithfulness and conclude that the causal structure is also identifiable due to the identifiability of HCR model and the faithfulness assumption.

The pseudo-code for causal correction is shown as Algorithm 2.

## Time and space complexity analysis

In this section, we analyze the time and space complexities of the PCCL-CC algorithm which is composed of several parts. Let $n$ be the number of network nodes and $m$ be the sample size. During the curriculum stage division, we need to compute the entropy value $H(X)$ of each node to select the initial node. Since we need to calculate $H(X)$ for all the $n$ nodes, the time complexity is $O(n)$. In the subsequent curriculum stage division, we need to calculate MI between each curriculum node and the candidate node which has at most $O\left(n^{2}\right)$ time complexity. The time complexity of calculating the MI value between nodes is polynomial which is expressed as a $\operatorname{mic}(m, r)$, where $r$ is the maximum possible value of any variable. Thus, the time complexity of calculating the MI value between all nodes is $O\left(n^{2} \cdot \operatorname{mic}(m, r)\right)$. After sorting all the MI values using quick sort, the time complexity becomes $O(\log (n))$. While constructing the initial skeleton according to the curriculum stage, we compute the weight on each side of the weight matrix set, and add constraints, resulting in a time complexity of $O\left(n^{2}\right)$. Hence, the time complexity
of constructing the initial DAG is $O\left(n^{2}\right)$. Assuming that the maximum number of iterations is $M a x_{\text {iter }}$, the causality correction is performed on the learned BN structure, resulting in a time complexity of $O\left(n^{2}\right)$. Therefore, the time complexity of the algorithm is $O\left(\operatorname{mic}\left(m, r\right) \cdot n^{2}\right)$ ). The space complexity of the algorithm remains constant at $O\left(n^{2}\right)$, since the curriculum division and weight distribution are the mountain climbing method, belonging to the local search algorithm, which can find reasonable understanding in a certain space with a constant space complexity.

## Experiment

All the experiments were performed on a computer equipped with an Intel(R) Core(TM) i7-1165G7 CPU at 2.80 GHz , 16GB memory and Compiler Environment is Pycharm 2021.1.2.

Data sets Four standard networks of different sizes have been selected for comparative experiments, and samples of different data sizes have been formed by sampling. The details are shown in Table 1.

Comparison Methods We compared our method against HC, PC [21], MMHC [37], PC-stable [51],PC-paraller [26] and NOTEARS algorithm [45].

Evaluation index We evaluate the proposed PCCL-CC approach in the quality of learned network structures. we use the following measurements:

Table 1 The classical BN data structures


![img-4.jpeg](img-4.jpeg)

Fig. 5 The performance comparison PCCL-CC algorithm and other algorithms on standard network
(1) Structural Hamming Distance(SHD): SHD is a standard distance used to compare graphs by using their adjacency matrices. It involves calculating the differences between two (binary) adjacency matrices: each missing or non-existent edge in the target graph is considered as an error. The smaller the SHD, the fewer incorrect edges are learned, and the better the learning effect.
(2) F1-score: Characterization of learning in the precision rate and recall rate of performance measurement. In BNs, the F1-score can help evaluate the performance of classification tasks and provide a comprehensive assessment of the predictive ability of positive and negative classes. The higher the F1-score, the more accurate the algorithm learns the network structure.
(3) False discovery rate (FDR): The ratio of all discoveries that are incorrect or reversed in direction.FDR can help determine potential false discoveries. The smaller the FDR, the lower the error rate of the learned network structure, and the better the algorithm's performance.
Using the SHD, F1-score, and FDR to measure the benefits of BNs provides a comprehensive evaluation, assessing the structure of the network, classification accuracy, and performance of feature selection from different perspectives.

## Performance comparison between PCCL-CC algorithm and other algorithms under different datasets

In the experiment, We also compared our algorithm with other structural learning algorithms, such as $\mathrm{HC}, \mathrm{PC}, \mathrm{MMHC}$, and NOTEARS. For each group, we used ten sets of data and took the average of the ten results. To verify the effectiveness of the algorithm, we used F1-score and SHD to evaluate the generated network.

Figure 5 displays the changes in SHD and F1-score for the five algorithms on the four standard datasets. As shown in the figure, our proposed PCCL-CC algorithm outperforms the other structural learning algorithms on smaller networks, such as Asia, with sample sizes less than 3 k . When the sample

```
Algorithm 2: \(\mathrm{DAG}=\mathrm{CC}(\mathrm{Data}, \mathrm{DAG})\)
    Input: Data: training data; DAG: The learned directed acyclic graph
    Output: DAG: the BN structure corresponding to the dataset
    \(n o d e s \leftarrow G N(\) Data \() ;\)
    \(A d j\) Matrix \(\leftarrow G A(D A G\), nodes \() ;\)
    for \(\left(X_{i}, X_{j}\right) \in A d j\) Matrix do
        if \(a_{i j}=1\) then
            \(\operatorname{data}_{i j} \leftarrow \operatorname{data}\left(X_{i}, X_{j}\right)\);
            \(X \leftarrow X_{i}, Y \leftarrow X_{j} ;\)
            \(f^{(0)}(x) \leftarrow \arg \max _{x} \hat{P}(X=x, Y=y)\);
            while \(L^{*}\) no longer increases do
                \(t=t+1 ;\)
                for each pair \(\left.<x, y^{\prime}\right\rangle\) do
                    \(L_{i j}^{*} \leftarrow \max _{\theta} L\left(f_{x \leftarrow j^{\prime}}^{t-1}, \theta ; D\right)-\frac{d}{2} \log (m) ;\)
                    if \(\hat{L}_{i j}^{*}<L_{i j}^{*}\) then
                    \(\left(\bar{x}, \bar{y}^{\prime}, \bar{L}_{i j}^{*}\right) \leftarrow\left(x, y^{\prime}, L_{i j}^{*}\right) ;\)
                    end
                    end
                    \(f(\bar{x}) \leftarrow \bar{y}^{\prime} ;\)
                    \(L_{i j}^{*} \leftarrow \hat{L}_{i j}^{*} ;\)
                    end
                \(L^{*}=L^{*} \cup L_{i j}^{*} ;\)
            end
    end
    for \(L_{i j}^{*} \in L^{*}\) do
        if \(L_{i j}^{*} \in L^{*}\) then
            if \(L_{i j}^{*} \in L_{i j}^{*}\) then
                \(a_{i j}=0, a_{j i}=1 ;\)
            else
                \(a_{i j}=1, a_{j i}=0 ;\)
            end
    end
    end
    \(D A G_{0} \leftarrow\) complete graph;
    \(D A G_{0} \leftarrow\) add_nodes(nodes);
    for \(\left(X_{i}, X_{j}\right) \in A d j\) Matrix do
        if \(a_{i j}=1\) then
            \(D A G \leftarrow\) add_edge \(\left(X_{i}, X_{j}\right) ;\)
        end
    end
    return \(D A G\)
```

size is $3 \mathrm{k}, \mathrm{HC}$ and PC algorithms also achieve good learning effects. For the Sachs network, the PCCL-CC algorithm demonstrates better results compared to other algorithms. For the larger and more complex network structures of Child and Alarm, the PCCL-CC algorithm has a significant advantage in learning effects, as evidenced by higher indicators compared to other algorithms.

We have discovered that our proposed PCCL-CC algorithm is effective in performing BN structure learning on networks of different sizes. For smaller networks with fewer nodes, the PCCL-CC algorithm can provide a more comprehensive description of the network and accurately identify the relationships between nodes with a smaller sample size. For larger and more complex networks with multiple nodes, the PCCL-CC algorithm outperforms other algorithms. As the number of nodes in the data set increases, traditional BNSL algorithms rely more on relationships between nodes, making them more susceptible to noise data and resulting in more learning errors. In contrast, incremental learning through stages enables the distribution of nodes to provide
more accurate judgments of higher-weight dependencies and gradually learn more complex dependencies, thereby reducing the occurrence of incorrect results in network learning.

## Impact of curriculum size on networks due to the different sizes of the network

The stage division in the algorithm is affected by the different network scales, which affects the step length of the learning node and determines the size of the learning network. Therefore, we conducted experiments to test the effect of curriculum size $\left(N_{c}\right)$ on the algorithm's performance. For the four standard networks, we set up a contrast experiment from $N_{c}=1$ to $N_{c}=20$ to distinguish the influence of class size for large networks. For the Alarm network, we set up a contrast experiment from $N_{c}=1$ to $N_{c}=30$. The evaluation index used for comparison is SHD. We compared the experimental results for each group by taking the average of ten sets of data, as shown in Fig. 6.

Figure 6 shows the changes in SHD for the PCCL-CC algorithm on the four standard networks with different $N_{c}$. Based on the figure, it is obvious that for the small network models, such as Asia and Sachs, as $N_{c}$ increases, the network nodes are divided into different stages, which decreases the SHD. However, excessive segmentation of network nodes leads to an increase in SHD after reaching a certain degree. The excessive segmentation results in each stage of CL to only one or two nodes, preventing the BNSL algorithm from effectively identifying dependencies between nodes, resulting in an increase in SHD. When the $N_{c}$ increases to a certain degree, the subsequent stages only focus on the original curriculum, causing the SHD to flatten out. For the medium-sized Child network, the network node is gradually subdivided as the $N_{c}$ increases, and the SHD decreases accordingly. This reflects how the phased learning network structure can effectively reduce the emergence of errors and improve the reliability of the algorithm. However, when the $N_{c}$ increases to a certain degree, excessive segmentation leads to an increase in the SHD. For the large-scale Alarm network, we set up a contrast experiment from 1 to 30 and found from the figure that as the $N_{c}$ increases, the SHD initially decreases before showing a trend of increase. When the $N_{c}$ reaches 12 , the SHD is the minimum, reflecting how the division of network scale affects BNSL algorithm. For the four types of standard network structures, the performance is best when $N_{c}$ approaches the degree of the network.

The curriculum stage should not be excessively segmented, as this can lead to a large number of key missing nodes and prevent the identification of nodes with complex dependencies, ultimately resulting in a large number of errors. Therefore, the setting of curriculum stage division should be combined with the degree of the network for effective performance.

![img-5.jpeg](img-5.jpeg)

Fig. 6 Performance Comparison of Numbers of Curriculum on Standard Datasets

Table 2 Influence of different $\theta$ values on each index


The bolded values represent the optimal values within the methods

## The influence degree of threshold setting in edge constraint

Experiments have been performed on the Asia datasets for the sample size 1000 for determining the effect of the threshold $\theta$ on the experimental results, and the results are shown in Table 2.

Table 2 reveals that the choice of $\theta$ has a less significant impact on the final result, as the corresponding value can be selected within a certain range. When the $\theta$ is set to negligible, more redundant edges are introduced to the network. Conversely, when the $\theta$ is set to a large value, fewer edges are selected and added to the network. This exclusion of potentially correct edges can result in a small number of correct edges and severe missing edges, which in turn leads to a relatively high SHD. Therefore, a comprehensive analysis and reasonable selection of $\theta$ are necessary to accurately learn the network structure while ensuring that more correct edges are present, which can make the multilateral and missing edges situation lighter.

## Ablation study

Tailoring our approach to the learning dynamics across distinct integration stages, we dynamically adjusted edge weights to systematically assess the efficacy of both the curriculum learning strategy and the causal correction mechanism in enhancing BNSL algorithms. Ablation experiments were conducted, wherein we juxtaposed the SHD of the classic PC algorithm against variations incorporating curriculum learning (PCCL), causal correction (PCCC), and a combined approach integrating both curriculum learning and further causal correction (PCCL-CC). This comparative evaluation was executed across four benchmark datasets.

Table 3 reveals varying degrees of enhancement in the PC algorithm upon integration with both the CL strategy and the causal correction mechanism. Notably, the performance improvement attributed to the CL strategy surpasses that of the causal correction mechanism. This discrepancy arises from the fact that the CL strategy predominantly mitigates the impact of noise during the learning process, whereas the causal correction mechanism primarily addresses the MEC

Table 3 Ablation experiments on four standard datasets


network structure to a certain extent. For networks with a large number of nodes and more complex network structures such as the Child and Alarm networks, the advantages of the PCCL-CC algorithm and PCCL algorithm are more pronounced compared to smaller networks. They exhibit a much smaller SHD than other algorithms, although the relatively lower FDR performance on the Alarm network is due to the threshold setting, which caused the algorithm to delete some correct edges.

By analyzing the results, it can be concluded that traditional BNSL algorithms are sensitive to sample noise and quantity, especially for networks with more complex node relationships. However, the CL framework effectively mitigates the impact of negative samples in samples by weighting and adapting them, improving the algorithm's robustness. Through the performance of the PCCL-CC and PCCL algorithms, it was shown that the causal correction mechanism can improve the learning effect of the algorithm to a certain extent. However, due to the limitations of the original sample types of BNs, no significant advantages were observed, which is also a direction for future improvements.

## Conclusion

In this study, we propose the PCCL-CC algorithm, which combines the concepts of CL and causal discovery. It introduces a method for measuring the strength of connections between nodes from multiple perspectives. The method divides the curriculum stages and utilizes an asymmetric weighting mechanism to minimize the impact of sample noise on the algorithm. Based on this, causal learning methods are used to discover potential causal relationships and minimize the impact of MEC. The experiments show that the PCCL-CC algorithm is less affected by sample noise and can obtain more accurate network structures compared to other algorithms.

However, our algorithm still has certain limitations. For example, it has higher complexity when dealing with large datasets compared to traditional CB method, requiring more computational resources. It is also sensitive to the initial stage of the curriculum and lacks a feedback updating mechanism during the curriculum stages. One of the future works is to utilize the learning effects between curriculum to guide the algorithm in its own learning process.

Acknowledgements This work was supported in part by the National Natural Science Foundation of China under Grant 62276262; Science and Technology Innovation Program of Hunan Province under Grant 2021RC3076; Training Program for Excellent Young Innovators of Changsha under Grant KQ2009009.

Data Availability The data that support the findings of this study are publicity available in Bayesian Network Repository at https://www. bnlearn.com/.

## Declarations

Conflict of interest The work described has not been submitted else where for publication, in whole or in part, and all the authors listed have approved the manuscript that is enclosed. Moreover, the authors declare that they have no Conflict of interest.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecomm ons.org/licenses/by/4.0/.
