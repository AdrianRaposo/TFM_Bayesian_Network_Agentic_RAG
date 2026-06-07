# Delay-guaranteed Mobile Augmented Reality Task Offloading in Edge-assisted Environment 

Jia Hao ( $\boldsymbol{\sim}$ haojiaynu@qq.com )
Key Laboratory of Education Informatization for Nationalities, Ministry of Education, Yunnan Normal University
Jianhou Gan
Key Laboratory of Education Informatization for Nationalities, Ministry of Education, Yunnan Normal University

## Research Article

Keywords: Augmented Reality (AR), task offloading, Bayesian Network, particle swarm optimization, genetic algorithm

Posted Date: October 14th, 2022
DOI: https://doi.org/10.21203/rs.3.rs-2101466/v1
License: (3) This work is licensed under a Creative Commons Attribution 4.0 International License. Read Full License

# Delay-guaranteed Mobile Augmented Reality Task 

## Offloading in Edge-assisted Environment

Jia Hao ${ }^{1,2 *}$, Jianhou Gan ${ }^{1,2}$<br>${ }^{1}$ Key Laboratory of Education Informatization for Nationalities, Ministry of Education, Yunnan<br>Normal University, Kunming 650500, China<br>${ }^{2}$ Yunnan Key Laboratory of Smart Education, Yunnan Normal University, Kunming 650500, China<br>*Corresponding Author: Jia Hao<br>Email of the Corresponding Author: haojiaynu@qq.com<br>ORCID of Jia Hao: 0000-0001-8099-9771


#### Abstract

With the introduction of augmented reality (AR) technology into mobile devices, it becomes a trend to develop mobile AR applications in various fields. However, the limited mobile hardware resources, like the CPU frequency, memory capacity, etc., makes it difficult to guarantee the delay of resource-intensive AR applications. In response to this challenge, we propose a mobile AR offloading method under the edge-assisted environment. Firstly, we divide an AR task into multiple consecutive subtasks, and then collect the features of hardware, software, configuration, and runtime environments of edge servers to be offloaded. With the features, we construct an AR subtask Execution delay Prediction Bayesian Network (EPBN) to predict the execution delay of different subtasks on each edge platform. Based on the prediction, we model the AR task offloading as the NP-hard Traveling Salesman Problem (TSP), and then propose a PSO-GA based solution by adopting the heuristic algorithm of Particle Swarm Optimization (PSO) to encode the offloading strategy and using Genetic Algorithm (GA) for particle update. The extensive experiments prove that our proposed method can optimize the AR task offloading strategy with the lowest delay and outperform the other baselines.


Keywords: Augmented Reality (AR), task offloading, Bayesian Network, particle swarm optimization, genetic algorithm

# 1. Introduction 

Nowadays, with the massive popularity of mobile devices, the corresponding support of Augmented Reality (AR), such as the SDKs of Google ARCore [1] and Apple ARKit [2], have been introduced into a variety of mobile terminals. With the ability to seamlessly blend the digital and physical world information, the mobile AR applications will certainly revolutionize the way of human-computer interaction [3-5].

During the running of mobile AR, it is important to ensure the delay is within the specified range for that the low delay can reduce users' dizziness and increase their immersive experiences. However, according to [6], the execution of an AR task can be completed by the following five subtasks executed sequentially, i.e., video acquisition, position tracking, target mapping, object detection, and result presentation, whose implementations require lots of network bandwidth, CPU cycles, memory capacity and the other resources. Thus, it is difficult for the mobile terminals with limited hardware resources to perform AR tasks with the low delay.

In the traditional cloud-centric service mode, the computation-intensive subtasks can be offloaded to the cloud servers so as to use the powerful clusters for processing and analyzing. But the long-distance transmission may increase the transmission delay and the risk of privacy leakage. Luckily, the prevalence of edge computing provides a compromise to alleviate the burden of cloud center, and then provide the richer hardware resources compared with the mobile terminals [7].

However, in the edge-assisted environment, it's challenging to offload the AR subtasks to the edge server, and then minimize the delay of the whole AR task. The main reasons are as follows.
(1) Accurately predicting the delay of AR subtasks offloaded to different edge servers is the prerequisite for edge server selection and subtask offloading, and the delay consists of the time of data transmission and task execution. The former is mainly affected by the mobile terminal transmission power, channel gain and noise, which are relatively fixed and easy to analyze theoretically $[8,9]$.

But for the delay of subtask execution, the affecting features are more complex and diverse [10]. For example, when a subtask is executed on the edge server, in addition to the CPU cycles, the other resources, such like the memory capacity, I/O disk bandwidth, and capacity of the last level cache (LLC), may also have effects. Furthermore, the subtasks, which cannot run on the edge bare metal directly, must run on the virtual machines or the containers deployed on the edge server. But the current

imperfect virtualization technology makes it impossible for several co-located subtasks to run on a completely isolated environment, which will lead the competition for the underlying physical resources and cause the increasing of subtask execution time.

Generally speaking, the features affecting subtask execution are mainly divided into four categories [11], namely the software, hardware, configuration, and the runtime environments, whose partial values are given in Tab.1. Therefore, if we fail to consider these features and ignore the uncertain relationships among them, like the efforts have been put in [12-15], then the prediction error might occur.

Table 1. The features affecting task execution


In response to this challenge, we construct an AR subtask Execution time Prediction Bayesian Network (EPBN). BN, a well-adopted framework of uncertain knowledge representing and analyzing, is a directed acyclic graph (DAG), where the nodes can represent the execution-related features and the edges describe the corresponding relationships [10]. Each node in a BN is associated with a conditional probability table (CPT) including a set of conditional probabilities give the states of its parents' node. With EPBN, we analyze the impacts of multiple features on the subtask execution, and then predict the execution time in the form of probabilities accurately.
(2) It is also challenging to offload several dependent subtasks so as to make the delay of the whole AR task be the lowest.
![img-0.jpeg](img-0.jpeg)
(a) AR Execution Flow
![img-1.jpeg](img-1.jpeg)
(b) Abstraction of AR Execution

Fig. 1 AR task model
Fig.1(a) illustrates the execution flow of an AR task, where the video acquisition and result presentation must be executed at the mobile terminal, but the execution

platforms of the remaining three subtasks includes both the mobile terminal and the edge servers [16]. Different choice varies the execution and transmission time.

Due to the dependencies among several subtasks, the AR task execution flow can be represented by a weighted directed cyclic graph as shown in Fig.1(b), where nodes $T_{1}$ to $T_{5}$ denote the subtasks, and the weighted edges indicate the corresponding delay (i.e., the sum of execution and transmission time) of different subtask offloading strategies. The smaller weights indicate the lower delay.

Therefore, finding a task offloading strategy with minimal delay is to visit the five nodes from $T_{1}$ orderly, and then find the corresponding path between $T_{i}$ and $T_{i+1}$ $(i \in\{1,2, \ldots, 5\})$ so as to make the weight of the cyclic path be the lowest. This is the Traveling Salesman Problem (TSP) and proved to be NP-hard.

Particle Swarm Optimization (PSO), a heuristic algorithm for solving the NP-hard problems, gets the solution by individual optimization and group collaboration [15]. So, in this paper, we propose to adopt PSO to calculate the delay the different subtask (individual optimization), and then optimize the whole AR task offloading decision (group collaboration). But the particle update of traditional PSO is based on the position and velocity, which are more suitable for the continuous optimization problems. AR task offloading, on the other hand, is discrete. Therefore, we further combine the Genetic Algorithm (GA) with the operation of crossover and mutation, to update the particles and then accelerate the optimization convergency while making the PSObased offloading strategies be feasible.

In general, the main contributions of this paper are summarized as follows.
(1) In the edge-assisted environment, we fully consider the impacts of multiple features (including the software/hardware, configuration, and runtime environments) on the execution delay of AR subtasks, and then construct an EPBN to quantify the uncertain relationships and predict the execution delay accurately.
(2) Getting the optimal AR task offloading strategy is described as finding the shortest path in the TSP problem. So, we further propose a PSO-GA based heuristic algorithm to find the optimized solution.
(3) For experiments, we first use two physical hosts to simulate the edge servers, on which we deploy the XEN hypervisor and install several virtual machines (VM) to create a multi-edge-server environment [17]. Then, we modify the edge-related features and run different benchmarks to record their execution time. The benchmark results verify the accuracy of EPBN in predicting execution delay, and the results of Python simulator verify that our proposed task offloading method outperforms the others.

# 2. Related Works 

Currently, the task offloading approaches can be broadly classified into three categories, namely, mathematical optimization-based method, machine learning-based method, and control theory-based method.

## (1) Mathematical Optimization-based Method

The task offloading method based on mathematical optimization mainly involves in establishing a model with the corresponding objects, such as the energy consumption, latency, network bandwidth, and load balancing. Then, these works optimize the targets among candidate solutions by the integer programming, heuristic algorithms, the game theory, etc. [14, 18-20]. For example, Du et al. [13] aimed to minimize the weighted cost of delay and energy consumption, and then used the fractional programming theory and Lagrangian dual decomposition to allocate the resources and optimize the offloading decision. Ma et al. [8] aimed to offload several dependent tasks in the multiaccess edge computing environment while considering both the task completion time and execution cost, and then proposed a queue-based multi-objective particle swarm algorithm to find the solution. Chen et al. [6] treated the layers in a Deep Neural Network (DNN) as the tasks, and then used multiple edges and remote cloud center as task execution ends. After encoding multiple offloading strategies by GA and accelerating the convergence by PSO, each layer of the DNN is reasonably offloaded.

Although the above task offloading methods can obtain the reasonable strategies with lower time complexity, these optimization models for a single objective usually lack the global consideration of the whole task and tends to make the results fall into the local optimum.

## (2) Machine Learning-based Method

Machine learning-based task offloading mainly uses the supervised learning [21, 22], unsupervised learning [23-25], and the reinforcement learning [9, 26, 27] methods to build task offloading models after collecting a large amount of feature-objectives data, so that when a new task comes, the corresponding solution can be given based on the model prediction results. For example, Warley et al. [28] used the resources, such as the number of CPU, as the features of the task, and then applied the classification algorithms, such like J48, to determine whether to offload a new task or not. Ullah et al. [25] used K-means to cluster different tasks into compute-intensive, memoryintensive, and network-intensive applications after characterizing them with the data of resource usage, to offload the task to the corresponding edge server. Lu et al. [9] used

input/output data, network throughput rate, and CPU cycles to characterize the resource execution, and then model the task offloading as a Markov Decision Process (MDP), to use the Deep Q-learning Network (DQN) to optimize the offloading solutions.

However, the offloading granularity of the above-mentioned works are relatively coarse, where the tasks are usually treated as a whole set and the corresponding offloading decision becomes a binary problem (i.e., to offload or not). If the tasks can be further divided into multiple subtasks, then they can be offloaded to different platforms, so that the advantages of distributed computing can be fully exploited and the delay can be reduced greatly.

# (3) Control Theory-based Method 

The control theory-based task offloading approaches are designed to monitor and analyze task implementation in real time by designing an M (Monitor)-A (Analyze)-P (Plan)-E (Execution)-K (Knowledge) loop, and to make timely adjustments to the offloading policy when the QoS violation occurs [29-31]. For example, Marios et al. [29] combine task offloading and fine-grained resource allocation to design a Linear Time Invariant (LTI) system with adaptive resource allocation. After collecting the amount of CPU and memory usage in real time, the system introduces a Holt linear exponential smoothing function to predict whether the QoS of the task will be satisfied in some future time; if not, the resources will be adjusted in time. Daniel et al. [30] design a two-tier task scheduling system, whose first tier is responsible for managing the edge devices with the goal of maximizing their resource utilization, while the second tier is responsible for managing the task offloading with the goal of minimizing the total energy consumption of task offloading. Finally, they used a game theory model to optimize the resource offloading solution.

However, most of the features considered in the above-mentioned works are only the number of CPUs and allocated memory capacity. But the underlying environmental features that affect the execution time also involve the CPU architecture, I/O throughput rate, etc. If these features are not taken into account during task offloading, it is easy to make the offloading solution unsatisfactory.

## (4) Edge Computing for Mobile Augmented Reality

By distributing the centralized cloud resources to the edge of the network, the edge computing platforms provide the ultra-low latency, real-time access and location-aware services for multiple mobile applications [32, 33]. At present, using the edge platforms to supports the mobile AR is still in the exploratory stage.

Ren et al. [16] proposed a hierarchical edge-to-cloud architecture which can

collaborate the computation capacity of edge and cloud servers, and then designed a framework to support the edge-cloud joint communication and computation resource allocation. To improve the energy efficiency of smartphone battery, Wang et al. [34] proposed to transfer the image/video frames from the mobile AR to the edge servers, where several deep learning algorithms were deployed, so as to employ the richer hardware resources to improve the object detection accuracy. Lan et al. [35] aimed to improve the robustness against image distortions thus increase the AR recognition accuracy. To this end, they developed an edge-assisted system which can provide the distortion-tolerant image recognition with the imperceptible latency.

The domestic and international research about the edge-assisted mobile AR mainly focus on the subtasks of object detection and image recognition. Also, there are several works consider to partially offload the AR subtasks to the edge and cloud platforms [6, 12], the related features only include the CPU, bandwidth, etc., and the other underlying physical features, like the CPU microarchitecture (e.g., ARM, X86) of edge servers and the memory type (e.g., DDR3, DDR4) are rarely taken into consideration.

# 3. System Model and Problem Formulation 

The five indispensable AR subtasks and their corresponding workflows are given in Fig.1(a), where the video acquisition clips the raw video from the mobile terminals into the different images, the position tracking determines the users' position under the real environment. Accordingly, the tracking results are transformed as the 3-D geometry coordinates by target mapping, and then the object detection uses the markerless or the marker-based computer vision technologies to detect the virtual objects. Finally, the augmented information is displayed by the result presentation [16]. The symbols used in this paper is given in Table 2.

Table 2 Symbol Definitions



In this paper, we consider a scenario where a single AR application user is under a multi-edge-server environment. The proposed system model is given in Fig.2.
![img-2.jpeg](img-2.jpeg)

Fig. 2 System Model
As shown in Fig.2, the system workflow is mainly composed of four steps. Firstly, the execution process of an AR task is abstracted by a weighted directed graph, where the node $T_{1}$ to $T_{5}$ represents the five subtasks and the corresponding edges indicate the execution order. Since the AR task is in a multi-edge-server environment, in addition to $T_{1}$ and $T_{5}$, each remaining node has multiple directed edges, where the weights represent the delays corresponding to different execution platforms.

Supposed that there are $n$ edge servers, $d_{i m}$ and $d_{i k}(i \in\{1,2, \ldots, 5\}, k \in$ $\{1,2, \ldots n\})$ represent the delay of $T_{i}$ executed on the mobile terminal $m$ and offloaded to the $k$ th edge server respectively. $\omega_{i}(i \in\{1,2, \ldots, 5\})$ denotes the data size of the $i$ th subtask, and if the data size of $T_{1}$ is known, then the sizes of the remaining subtasks can be calculated by $\omega_{i}=\bar{\omega} * \omega_{i-1}(\bar{\omega} \in[0,1])$ [36]. Let $f_{m}$ be the CPU frequency of $m$ and $\phi_{m}$ denote the CPU cycles required by subtask $T_{i}$. Accordingly, the task execution delay $d_{i m}$ can be calculated as $d_{i m}=\frac{\phi_{m} * \omega_{i}}{f_{m}}$.
$d_{i k}$ is composed of the transmission delay $d_{\text {trans }_{i k}}$ and the execution delay

$d_{\text {exe }_{i k}}$ corresponding to edge server $E C_{k}$, namely, $d_{i k}=d_{\text {trans }_{i k}}+d_{\text {exe }_{i k}}$. For $d_{\text {trans }_{i k}}$, we first define the bandwidth between the mobile terminal and edge server $E C_{k}\left(k \in\{1,2, \ldots n\}\right)$ as $B_{m, k}$, and then assume that the mobile devices can only connect to the edge servers within the WIFI radiation range and $B_{m, k}$ is not fluctuate. Therefore, the transmission delay of subtask $T_{i}$ from mobile terminal $m$ to edge server $E C_{k}$ can be calculated by $d_{\text {trans }_{i k}}=\frac{\omega_{i}}{B_{m, k}}$.

For $d_{\text {exe }_{i k}}$, since its value is affected by the features of software, hardware, configuration and runtime environment of the edge servers, we predict its value by EPBN, whose construction and prediction details are given in Sec. 4.

Finally, with $d_{i m}, d_{\text {trans }_{i k}}$ and $d_{\text {exe }_{i k}}$, we can sequentially predict the corresponding delay of subtask $T_{i}$ executed on the mobile terminal $m$ or offloaded to edge server $E C_{k}$ respectively, namely, the weights of directed edges from node $T_{i}$ to $T_{i+1}$ can be calculated. Therefore, we define the whole AR task offloading strategy as $\boldsymbol{X}=\left\{\left(T_{i}, S_{i}\right) \mid T_{i} \in\left(T_{1}, T_{2}, \ldots, T_{5}\right), S_{i} \in\left(m, E C_{1}, E C_{2}, \ldots, E C_{n}\right)\right\}$, and then propose the PSO-GA based AR task offloading strategy to get the corresponding weighted edges with the objective of $\min \sum_{i=1}^{5} d_{i}\left(d_{i} \in\left(d_{i m}, d_{i k}\right)\right)$, whose details are given in Sec. 5 .

# 4. EPBN-Based AR Subtask Execution Delay Prediction 

The execution delay of an AR subtask offloaded to the edge server is affected by the features of software, hardware, configuration and runtime environment, among which there are several uncertain and interdependent relationships. So, we first propose to construct an EPBN to quantify the uncertain relationships in the form of probability, and then predict the execution delay of AR subtasks performed on different edge servers.

### 4.1 Definition and Constraints of EPBN

We first give some definitions of the symbols involved in the construction of EPBN.

- Let $G_{E P B N}(V, E, \theta)$ denote the EPBN, where $V$ and $E$ are the sets of nodes and edges respectively. $V=F \cup d_{\text {exe }}$, where $F=\left\{F_{1}, F_{2}, \ldots, F_{|f|}\right\}$ is the set of features and $F_{i}(i \in\{1,2, \ldots,|f|)$ is the $i$ th feature from the edge servers; $d_{\text {exe }}$ represents the execution delay corresponding to the feature set $F ; E=\left\{e\left(V_{i}, V_{j}\right) \mid V_{i}, V_{j} \in V, i \neq j\right\}$ is

the set of edges representing the interdependencies among the nodes, and $e\left(V_{i}, V_{j}\right)$ is a directed edge from $V_{i}$ to $V_{j} . \theta$ is the set of parameters of EPBN, which consists of conditional probability tables (CPTs) corresponding to node set $V$.

- Let $P a\left(V_{i}\right)$ denote the parent nodes of $V_{i}$ with $\left|P a\left(V_{i}\right)\right|$ combinations, and $P\left(V_{i}=v_{i j} \mid P a\left(V_{i}\right)=k\right)$ represent the conditional probability of $V_{i}=v_{i j}$ when the parents of feature $V_{i}$ are the $k$ th $\left(k \in\left\{1,2, \ldots,\left|P a\left(V_{i}\right)\right|\right\}\right)$ combination. For simplicity, we use $\theta_{i j k}$ to denote $P\left(V_{i}=v_{i j} \mid P a\left(V_{i}\right)=k\right)$, which is a specific entry of CPTs. If node $V_{i}$ has no parents, then $P a\left(V_{i}\right)=1$. Thus, the parameter set $\theta$ is the combination of $\theta_{i j k}$ and can be represented as $\theta=$ $\cup_{i, j \in\{1,2, \ldots|V|\}, k \in\{1,2, \ldots,\mid P a\left(V_{i}\right)\}} \theta_{i j k}$.

A trivial result could be achieved if not impose some constraints during the construction of EPBN with the search and score method. Thus, we further list three constraints during the EPBN construction.
Constraints 1: Initial Structure. Based on the priori knowledge of hardware, we can determine some certain dependencies among several features, e.g., the Microarchitecture of CPU must affect the Capacity of Ll Cache. Similarly, we are able to know the independencies among some features, such like Memory Type and Hard Disk Type must be independent from each other. These kinds of relationships can be reflected by the edges in the EPBN. Therefore, we first create a white list and black list of edges, where the former records the features that are definitely related and the latter contains the features that are certainly independent, so as to create the initial structure of EPBN.
Constraints 2: Structure Construction. Some features from the edge server may have impacts on the delay of AR subtask execution, but the execution delay cannot affect the corresponding features in turn. This kind of relationship in EPBN is expressed as a directed edge $e\left(F_{i}, d_{\text {exe }}\right)$ from feature node $F_{i}$ to delay node $d_{\text {exe }}$, whose orientation cannot be reversed. Besides, the edges are not allowed to form the circles.
Constraints 3: Parameter Calculation. The parameter calculation is to calculate the value of $\theta_{i j k}$. When node $V_{i}$ has no parent, then $P a\left(V_{i}\right)=1$, and the value of $\theta_{i j k}$ can be determined by the prior probability of $P\left(V_{i}=v_{i j}\right)$. Else, if the parent of node $V_{i}$ is the $k$ th combination, then the value of $\theta_{i j k}$ is calculated by the conditional probabilities, namely $\theta_{i j k}=P\left(V_{i}=v_{i j} \mid P a\left(V_{i}\right)=k\right)$ and $\Sigma_{j=1}^{\left|v_{i j}\right|} \theta_{i j}=1$.

These three constraints can reduce the search space of adding, deleting and reversing edges in EPBN, and then guide the parameter calculation based on the observed results, so as to help the search-scoring based EPBN structure construction

method converge better.

# 4.2 EPBN Construction and Delay Prediction 

Firstly, the construction of EPBN involves in the parameter calculation and structure construction. The former one is achieved by the method of Maximum Likelihood Estimation (MLE) and the latter is completed by the hill-climbing method along with the function of Bayesian Information Criterion (BIC)[10]. Given the constructed EPBN and the delay-related features, we can predict the execution delay of AR subtasks on different edge servers, which is the basis for the AR task offloading.

Supposed that there is a dataset $D$ with $|D|$ feature-delay instances, which are independent and identically distributed (i.i.d). Then, we first define a characteristic function of $V_{i}$ with the parents of $P a\left(V_{i}\right)$ in Equ. (1), and then further use $m_{i j k}$ to represent the number of $V_{i}=v_{i j}$ when $P a\left(V_{i}=v_{i j}\right)=k$.

$$
\gamma(i, j, k: D)=\left\{\begin{array}{c}
1, \text { if } V_{i}=v_{i j} \text { and } P a\left(V_{i}=v_{i j}\right)=k \\
0, \text { else }
\end{array}\right.
$$

According to Equ.(1), $m_{i j k}$ can be calculated as $m_{i j k}=\Sigma_{i=1}^{|D|} \gamma(i, j, k: D)$, and then the MLE of $\theta_{i j k}$ can be calculated by Equ. (2).

$$
\theta_{i j k}=\left\{\begin{array}{c}
\frac{m_{i j k}}{\sum_{k=1}^{\left|P a\left(V_{i}=v_{i j}\right)\right|} m_{i j k}}, \text { if } \Sigma_{k=1}^{\left|P a\left(V_{i}=v_{i j}\right)\right|} m_{i j k}>0 \\
\frac{1}{P a\left(V_{i}=v_{i j}\right)}, \text { else }
\end{array}\right.
$$

where $m_{i j k}$ represents the number of instances when the value of node $V_{i}$ is $v_{i j}$ with the parent of the $k$ th combination, and $\Sigma_{\mathrm{k}=1}^{\left|P a\left(V_{i}=v_{i j}\right)\right|} m_{i j k}$ is the number of instances when $P a\left(V_{i}\right)=k$. Thus, the parameter $\theta$ of EPBN can be obtained by combining all the calculation results of $\theta_{i j k}$, namely, $\theta=\Sigma_{i=1}^{|V|} \Sigma_{j=1}^{\left|V_{i}\right|} \sum_{k=1}^{\left|P a\left(V_{i}=v_{i j}\right)\right|} \theta_{i j k}$.

Example 1 gives the processes of the parameter calculation, where Fig.3(a) is an initial structure of EPBN and Fig.3(b) gives a set of i.i.d feature-delay data instances.

As it can be seen from Fig.3(a) that the CPTS of all nodes are calculated by Equ.(2) based on the data instances from $D_{1}$ to $D_{6}$. Besides, all of the nodes are numbered according to the order from the parents to the child, and the combinations of all parents' value are numbered from 1 and arranged in order. For example, node \#3 is LLC Capacity with the parent of \#1 CPU micro-architecture. Thus, as it can be seen from EPBN, the second value of node \#3 is taken as $L L C=32 K$, and the first combination of

its parent is $C P U$ micro-architecture $=A M D$. So, the conditional probability of $\theta_{321}$ can be calculated as $\theta_{321}=P(\# 3=32 K \mid P a(\# 3)=A M D)=$ $P($ LLC Capacity $=32 K \mid C P U$ micro - architecture $=A M D)=1 / 6$.

# Example 1. 

![img-3.jpeg](img-3.jpeg)

Fig. 3 An example of EPBN and the corresponding dataset
Given the calculated parameters $\theta$ and the current EPBN structure $G_{E P B N}(V, E)$, we select the Bayesian Information Criterion (BIC)[10], a well-adopted scoring function which can calculate the score based on the sub-structure of each node and its parents, to calculate the degree of fitness between $G_{E P B N}(V, E, \theta)$ and the dataset $D$. The BIC score is calculated by Equ.(3).
$\operatorname{BIC}\left(G_{E P B N}(V, E, \theta) \mid D\right)=\Sigma_{i=1}^{|V|} \Sigma_{j=1}^{\left|V_{i}\right|} \Sigma_{k=1}^{\left|P a\left(V_{i}=v_{i j}\right)\right|} m_{i j k} \log \left(\frac{m_{i j k}}{m_{i j}}\right)-\frac{\Sigma_{i=1}^{|V|} d+\log |D|}{2}$
where $d=\left|V_{i}\right| *\left(\left|P a\left(V_{i}\right)\right|-1\right)$, and $\frac{\Sigma_{i=1}^{|V|} d+\log |D|}{2}$ can be seen as a penalty for the EPBN complexity. Furthermore, we define the BIC score of node $V_{i}$ and its parents $P a\left(V_{i}\right)$ as show in Equ.(4).
$\operatorname{BIC}\left(<V_{i}, P a\left(V_{i}\right)>|D\right)=\Sigma_{j=1}^{\left|V_{i}\right|} \Sigma_{k=1}^{\left|P a\left(V_{i}=v_{i j}\right)\right|} m_{i j k} \log \left(\frac{m_{i j k}}{m_{i j}}\right)-\frac{d}{2} * \log |D|$
Therefore, based on Equ.(3) and (4), we can derive Equ.(5), which indicates the BIC score of the whole EPBN can be obtained by summing up the BIC values of several sub-structure.

$$
\operatorname{BIC}\left(G_{E P B N}(V, E, \theta) \mid D\right)=\Sigma_{i=1}^{|V|} B I C\left(<V_{i}, P a\left(V_{i}\right)>|D|\right.
$$

Finally, we adopt the hill-climbing method to search for the optimal EPBN structure. Staring from the initial structure given by Constraints (1), we add, delete or reverse edges on the current EPBN iteratively, so that a series of candidate structures can be obtained. Suppose that the parent of node $V_{i}$ is changed from $P a\left(V_{i}\right)$ to

$P a^{\prime}\left(V_{i}\right)$ after the modification, then the change of BIC score corresponding to the candidate structure $G_{E P B N}^{\prime}(V, E, \theta)$ can be calculated by Equ.(6).

$$
\begin{aligned}
B I C\left(G_{E P B N}^{\prime} \mid D\right)= & B I C\left(G_{E P B N} \mid D\right)+B I C\left(<V_{i}, P a^{\prime}\left(V_{i}\right)>\mid D\right) \\
& -B I C\left(<V_{i}, P a\left(V_{i}\right)>\mid D\right)
\end{aligned}
$$

where $B I C\left(<V_{i}, P a^{\prime}\left(V_{i}\right)>\mid D\right)$ and $B I C\left(<V_{i}, P a\left(V_{i}\right)>\mid D\right)$ represent the BIC scores after and before the EPBN structural modification, respectively. If the value of $B I C\left(<V_{i}, P a^{\prime}\left(V_{i}\right)>\mid D\right)-B I C\left(<V_{i}, P a\left(V_{i}\right)>\mid D\right)$ is less than a given threshold $\beta$, then the hill-climbing converges and the corresponding $G_{E P B N}^{\prime}(V, E, \theta)$ is the optimal EPBN structure.

Based on the constructed EPBN $G_{E P B N}(V, E, \theta)$, the conditional probabilities with different delays of AR subtasks $T_{i}$ can be calculated when the features of hardware, software, runtime environment, and the configurations on the edge server $E C_{k}$ are given. Thus, the prediction results of $d_{\text {exe }_{i k}}$ can be obtained by the maximum conditional probabilities, i.e., $d_{\text {exe }_{i k}}=\arg \max \left(P\left(d_{\text {exe }_{i k}}\right) \mid P a\left(d_{\text {exe }_{i k}}\right)\right)$.

The above-mentioned ideas of EPBN construction and delay prediction are given in Algorithm 1.
Algorithm 1: EPBN-based AR Subtask Delay Prediction

# Input 

$V$ : The nodes consisting of edge server-related features and the execution delay.
$D$ : The feature-delay dataset with $|D|$ instances.
$G_{E P B N}^{0}\left(V^{0}, E^{0}, \theta^{0}\right)$ : The initial structure of EPBN.
$\beta$ : The threshold of the difference between the two BIC scores.
$c$ : The number of EPBN candidate structures.
CandStructure[]=null: The set of candidate structures, whose initial value is null.
SearchOperator(): The function to operate the edge adding, deleting or reversing.
SelectParent $\left(V_{i}, G_{E P B N}\right)$ : The function to select the parents of node $V_{i}$ based on $G_{E P B N}(V, E, \theta)$.

## Output

$G_{E P B N}(V, E, \theta)$ : The optimal structure of EPBN.
$d_{\text {exe }_{i k}}$ : The delay of AR subtask $T_{i}$ executed on the $k$ th edge server.

## Steps

1. $G_{E P B N}(V, E, \theta)=G_{E P B N}^{0}\left(V^{0}, E^{0}, \theta^{0}\right)$
2. oldScore $=$ BIC $\left(G_{E P B N}(V, E, \theta) \mid D\right) / /$ Calculate the BIC score of the current EPBN by Equ.(5)
3. While (true) do: //Construct the EPBN
4. $G_{E P B N}^{*}(V, E, \theta) \leftarrow$ null, $\theta^{*} \leftarrow$ null, newScore $\leftarrow-\infty$,
5. for $i$ in $(1: c)$ do:
6. CandStructure[i] $\leftarrow$ SearchOperator() //Generate $c$ candidate structures
7. end for
8. for $i$ in (CandStructure[1] to CandStructure[c]) do:
9. $G_{E P B N}^{i}\left(V^{i}, E^{i}\right) \leftarrow$ CandStructure $[i]$

10. $\quad \theta^{i} \leftarrow \Sigma \theta_{i j k}^{i} / /$ Calculate the parameter of $G_{E P B N}^{i}$ by Equ.(2)
11. tempScore $\leftarrow B I C\left(G_{E P B N}^{i}\left(V^{i}, E^{i}, \theta^{i}\right) \mid D\right) / /$ Calculate the BIC score by Equ.(5)
12. If (tempScore> newScore) then:
13. $G_{E P B N}^{*}\left(V^{*}, E^{*}, \theta^{*}\right) \leftarrow G_{E P B N}^{i}\left(V^{i}, E^{i}, \theta^{i}\right)$
14. newScore $\leftarrow$ tempScore
15. end if
16. end for
17. If $\left(B I C\left(G_{E P B N}^{*}\left(V^{*}, E^{*}, \theta^{*}\right)\right)-B I C\left(G_{E P B N}(V, E, \theta)\right)>\beta\right)$ then:
18. $G_{E P B N}(V, E, \theta) \leftarrow G_{E P B N}^{*}\left(V^{*}, E^{*}, \theta^{*}\right)$
19. oldScore $\leftarrow$ newScore
20. end if
21. end while
22. $P a\left(d_{\text {exe }_{i k}}\right) \leftarrow$ SelectParent $\left(V_{i}, G_{E P B N}\right) / /$ Select the parent of node $d_{\text {exe }}$
23. $d_{\text {exe }_{i k}}=\arg \max \left(P\left(d_{\text {exe }_{i k}}\right) P a\left(d_{\text {exe }_{i k}}\right)\right) / /$ Delay prediction
24. Return $G_{E P B N}(V, E, \theta), d_{\text {exe }_{i k}}$

Theoretically, we suppose that there are $\alpha$ times of iteration till the convergency for each candidate structure with $|D|$ instances, so the time complexity of Algorithm 1 is $O(\alpha * c *|D|)$. However, since Constraint 1 gives a reasonable initial structure according to the characteristics of edge servers, and Constraint 2 gives the whitelist and blacklist of directed edges during the construction, so that the efficiency of Algorithm 1 can be greatly improved by reducing the edge searching space. Also, these Constraints can prevent the structure of EPBN from failing into local optimum to a certain extent.

# 5. PSO-GA Based AR Task Offloading Strategy Optimization 

An optimized AR task offloading decision includes arranging the five subtasks to execute on the mobile terminal or the edge computing platforms with the lowest latency. To this end, we first design the offloading strategy as $\boldsymbol{X}=\left\{\left(T_{i}, S_{j}\right) \mid T_{i} \in\right.$ $\left.\left(T_{1}, T_{2}, \ldots, T_{5}\right), S_{j} \in\left(m, E C_{1}, E C_{2}, \ldots, E C_{n}\right)\right\}\right\}$ with the optimization objective of $\min \sum_{i=1}^{5} d_{i}\left(d_{i} \in\left(d_{i m}, d_{i k}\right)\right)$, and then find the solution with a PSO-GA based heuristic approach, which contains the processes of initial population sel7ection, fitness function designing and the population update.

### 5.1 Problem Encoding

For the traditional PSO algorithm, the $i$ th particle can be represented as $Q_{i}=$ $\left(X_{i}, U_{i}\right)$, where $X_{i}$ and $U_{i}$ indicate the candidate solution and the corresponding

update velocity. Suppose that particle $Q_{i}^{t}$ has been updated for $t$ times, then the $(t+$ 1)th update can be defined by Equ.(7).

$$
\left\{\begin{array}{c}
V_{i+1}^{t}=\omega V_{i}^{t}+c_{1} r_{1}\left(L_{i}^{t}-X_{i}^{t}\right)+c_{2} r_{2}\left(G^{t}-X_{i}^{t}\right) \\
X_{i}^{t+1}=X_{i}^{t}+V_{i+1}^{t}
\end{array}\right.
$$

where $c_{1}, c_{1}$ are the acceleration coefficients, $r_{1}$ and $r_{2}$ are the random numbers within the range of $[0,1) . L_{i}^{t}$ is the local optimized particle of $X_{i}$ at the $t$ th iteration, and $G^{t}$ is the global best within the population. $\omega$ is the inertial weight which defines whether the search strategy prefers the global or the local optimum, and can be calculated by Equ.(8)

$$
\omega=\omega_{\max }-\left(\omega_{\max }-\omega_{\min }\right) * \exp \left[\frac{d_{G^{t}}-d_{X_{i}^{t}}}{\left(d_{G^{t}}-d_{X_{i}^{t}}\right)-1.01}\right]
$$

where $\omega_{\max }$ and $\omega_{\min }$ are the given maximum and minimum values of $\omega, d_{G^{t}}$ and $d_{X_{i}^{t}}$ are the delay corresponding to the particle $G^{t}$ and $X_{i}^{t}[6]$.

According to PSO, the initial population with $n_{i n i}$ particles can be set as $\boldsymbol{X}_{\text {ini }}=$ $\left\{X_{l} \mid X_{l}=\left(<T_{1}, m>,<T_{2}, S_{2 j}>,<T_{3}, S_{3 j}>,<T_{4}, S_{4 j}>,<T_{5}, m>\right), l \in\left[1, n_{i n i}\right]\right.$, $\left.S_{j} \in\left(m, E C_{1}, E C_{2}, \ldots, E C_{n}\right)\right\}$. The $l$ th particle $X_{l}$ represents a feasible task offloading solution, where the subtask $T_{1}$ and $T_{5}$ can only be executed on the mobile terminal $m$. Initially, the offload scheme for $X_{i}$ is randomly assigned.

# 5.2 Fitness Calculation 

Then, we design the fitness function as shown in Equ.(9), so as to evaluate the delays of $n_{i n i}$ feasible particles.

$$
F\left(X_{l}\right)=\Sigma_{i=1}^{5} d_{l i}
$$

where $d_{i i}$ corresponds to the delay of the $i$ th $(i \in\{1,2, \ldots 5\})$ subtask offloading solution. Let $x_{l i}$ be the offloading strategy of subtask $T_{i}$ in the particle $X_{l}$, and $x_{l i}=$ $<T_{i}, m>$ indicates $T_{i}$ executed on the mobile terminal $m$ with the delay of $d_{i i}=$ $\frac{\phi_{m} * \omega_{i}}{f_{m}}, x_{l i}=<T_{i}, S_{j}>$ represents $T_{i}$ is offloaded to edge server $E C_{j}$ with the delay of $d_{i i}=d_{\text {trans }_{i k}}+d_{\text {exe }_{i k}}$, which can be predicted by EPBN.

According to our optimization objective, the particle $X_{l}$ with a smaller fitness value indicates it should be selected as the candidate solution with a greater probability. Thus, we denote the probability of $X_{l}$ being selected as $P_{\text {cand-l }}$, and then calculate it

by Equ.(10). Based on $P_{\text {cand-l }}$, we represent the cumulative probability of $X_{l}$ within the initial population $\boldsymbol{X}_{\text {ini }}$ as $q_{l}=\Sigma_{l=1}^{|i n i|} P_{\text {cand-l }}$.

$$
P_{\text {cand-l }}=1-\frac{F\left(X_{l}\right)}{\Sigma_{l=1}^{|i n i|} F\left(X_{l}\right)}
$$

Then, the Russian Roulette algorithm will be adopted to select $n_{p}\left(n_{p}<n_{i n i}\right)$ updated particles, which are more likely to converge to the optimal solution. Specifically, a uniformly distributed random number $r$ within the range of $[0,1]$ is generated, and if $q_{l}>r$, then the corresponding particle $X_{l}$ is selected. Otherwise, the particle $X_{o}\left(o \in\left\{1,2, \ldots, n_{i n i}\right\}\right)$ which makes the inequality $q_{(o-1)}<r<q_{o}$ hold will be selected.

The above-mentioned processes will be repeated until $n_{p}$ particles are generated.

# 5.3 Particle Update 

The traditional PSO update approach is shown in Equ.(7), which is more suitable for the continuous problems. Therefore, we introduce the GA method to update the individual particles, so that they can be adapted to the discrete AR task offloading.

The particle updated strategy for $X_{i}^{t}$ in the $t$ th iteration is modified by Equ.(11).

$$
\left\{\begin{array}{c}
V_{i+1}^{t}=\omega V_{i}^{t}+C O\left(L_{i}^{t}, X_{i}^{t}, P_{c o}\right)+C O\left(G^{t}, X_{i}^{t}, P_{c o}\right) \\
X_{i}^{t+1}=M U\left(X_{i}^{t}, P_{M U}\right)+V_{i+1}^{t}
\end{array}\right.
$$

where $C O()$ is the function of single point crossover, so that the $C O\left(L_{i}^{t}, X_{i}^{t}, P_{c o}\right)$ and $C O\left(G^{t}, X_{i}^{t}, P_{c o}\right)$ indicate that we swap the AR subtask offloading strategies with the locally optimal particle $L_{i}^{t}$ and the global optimal particle $G^{t}$ with the probability of $P_{c o}$ respectively. In addition, $M U()$ is the function of single point mutation, which represent we randomly select the particle $X_{i}^{t}$, and then change its offloading strategy with the probability of $P_{M U}$. Since the strategy updating is a discrete rather than continuous process, we use the parameter $V^{t}$ to control the number of particles to be updated within the $t$ th iteration. For example, when $V^{t}$ is set to 1 , it means that we select one particle to operate the crossover and mutation respectively.

Repeat the fitness calculation and the particle update till convergency, and then the corresponding global best particle is the optimal AR task offloading solution. The main ideas of PSO-GA based offloading optimization is summarized in Algorithm 2.

Algorithm 2: PSO-GA Based AR Task Offloading Strategy Optimization

## Input

$n_{i n i}$ : The number of particles in the initial population

$n_{p}$ : The number of particles to be updated
$X_{\text {ini }}=\emptyset$ : The initial population
$X_{n_{p}}=\emptyset$ : The population to be updated
$I$ : The times of iteration
$P_{C O}$ : The probability of particle crossover
$P_{M U}$ : The probability of particle mutation

# Output 

$X_{o s}$ : The optimized offloading decision

## Steps

1. for $i=1$ to $n_{\text {ini }}$ do: //Generate the initial population
2. $d_{i}=0$ //Delay of particle $X_{i}$
3. for $j=1$ to 5 do:

Generate $x_{i j}=<T_{j}, S>$ //Generate the initial offloading decision for $T_{j}$ in particle $X_{i}$
$d_{i}=d_{i}+d_{i j} / /$ Calculate the corresponding delay
6. end for
7. $F\left(X_{i}\right)=$ fitnessCalculate $\left(X_{i}\right) / /$ Calculate the fitness by Equ.(8)
8. $\quad \boldsymbol{X}_{\text {ini }}=\boldsymbol{X}_{\text {ini }} \cup X_{i}$
9. $\quad \boldsymbol{X}_{\boldsymbol{n}_{\boldsymbol{p}}}=\operatorname{Sort}\left(\boldsymbol{X}_{\text {ini }}, n_{p}\right) / /$ Sort particles in $\boldsymbol{X}_{\text {ini }}$ by fitness and then select $n_{p}$ ones to be updated
10. $\quad L_{i}, G=X_{1} / /$ Initial local best and global best particle with first particle in $\boldsymbol{X}_{\boldsymbol{n}_{\boldsymbol{p}}}$
11. end for
12. for $i=1$ to $I$ do:
13. for $X_{i}$ in $X_{n_{p}}$ do:
14. if $\operatorname{Randit}(0,1)>P_{C O}$ then:
15. $\quad V_{i}=\omega V+C O\left(L_{i}, X_{i}, P_{C O}\right)+C O\left(G, X_{i}, P_{C O}\right) / /$ Calculate $\omega$ by Equ.(8) and then crossover
16. if $\operatorname{Randit}(0,1)>P_{M U}$ then:

$$
X_{i}=M U\left(X_{i}, P_{M U}\right)+V_{i}
$$

18. else: $X_{i}=V_{i}$
19. $\quad F\left(X_{i}\right)=$ fitnessCalculate $\left(X_{i}\right), X_{i}=$ LocalBest $\left(X_{n_{p}}\right), G=$ GlobalBest $\left(X_{n_{p}}\right)$
20. end for
21. end for
22. Return $X_{o s}=G / /$ The global best particle corresponds to the optimized solution

Technically speaking, the time complexity of Algorithm 2 is $O\left(I * n_{p}\right)$. However, the setting of parameters $\omega_{\min }, \omega_{\max }, P_{C O}$ and $P_{M U}$ has a great impact on the local and global search convergency, and the exact values depends on the specific situations.

# 6. Experiments 

We conduct extensive experiments in response to the following research questions (RQ).
RQ1: When predicting the execution latency of AR subtasks on different edge servers, can the prediction results considering the features of software, hardware, configuration, and the runtime environments be more accurate than the outcomes while only the CPU cycles and CPU frequency involved?

RQ2: Is our proposed EPBN able to predict the execution delay effectively compared with the other baselines on different edge servers?

RQ3: Is our proposed PSO-GA method able to optimize the AR task offloading strategy with different parameters, such as frequency of mobile devices, the number of edge servers, or the transmission bandwidth, to get the lowest execution delay?

### 6.1 Experimental Setup

Firstly, we use two physical hosts and adopt the virtual machine monitor (VMM) $X E N^{1}$ to install three co-located virtual machines (VMs) on each physical host, and then each VM is considered as an edge server node with the Linux kernel 3.18.3420.el7.x86_64. The configurations of the two physical hosts are listed in Table 3.

Table 3. The configuration of physical hosts


Then, we adopt the benchmark program Parsec $^{2}$, which includes the applications of image processing (vips), video encoding (X264), body tracking of a person (bodytrack), online clustering of an input stream (streamcluster) etc., to simulate all kinds of AR subtasks. We deploy each application on the edge servers and then change their configurations to collect different application running time, by which we verify the RQ1 and RQ2. The features influencing the delay execution are selected as follow: Number of $\boldsymbol{v C P U}(1,2,3,4)$, CPU frequency $(3.3 \mathrm{GHz}, 3.6 \mathrm{GHz})$, CPU type (Intel,

[^0]
[^0]:    ${ }^{1}$ https://xenproject.org/
    ${ }^{2}$ https://parsec.cs.princeton.edu/overview.htm

AMD), memory capacity (512MB, 1024MB, 2048MB), memory frequency (1866MHz, 2133 MHz ), LLC size $(4 \mathrm{MB}, 6 \mathrm{MB})$, vCPU-pCPU bound mode $(0,1,2$, while 0 indicates no-bound, 1 indicates the virtual CPU cores bound with the physical CPU cores independently, and 2 indicates several virtual CPU cores bound with a certain physical core), number of co-located VMs (0,1,2,3), load type (CPU-intensive, memory-intensive, I/O intensive), hard disk type (SATA, SSD), and the hard disk capacity $(1 \mathrm{~GB}, 2 \mathrm{~GB})$.

Next, the extensive simulation experiments based on Python3 simulator are conducted on Win10 64bit operating system with CPU of Intel i5-7300HQ, 16GB RAM and 1TB SSD, so as to verify RQ3. All the details can be found in our GitHub project ${ }^{3}$.

# 6.2 RQ1. Delay Prediction Incorporating Multiple Features 

Firstly, we adopt the same approach (given by Equ.(12)) as in literature [6, 16] to estimate the required execution delay of benchmark applications running on the edge server, and then use the calculation results as the ground truth.

$$
d_{\text {exe }}=\frac{\omega}{f_{m}}
$$

where $\omega$ is the size of application and $f_{m}$ is the CPU frequency. Then, we set 6 configurations in Table 4, where each configuration corresponds to an edge server.

Table 4 Configuration and Details


Then, the benchmark applications vips, bodytrack, X264 and streamcluster are selected and repeated 100 times on each edge server respectively, and the average execution time are compared with the ground truth. The results are given in Fig. 4 .

[^0]
[^0]:    ${ }^{3} \mathrm{https}: / /$ github.com/haojiaYNU/simulation

It can be concluded from Fig. 4 that all of the benchmark applications running on the edge servers have longer execution time than the results based on the theoretical analysis. The main reason is that the CPU wall-clock time is composed of four parts, i.e., the user time (the time running the user applications), the system time (the time running the kernel code), the CPU idle time, and the wait time (the time waiting for the I/O tasks). The user time corresponds to the theoretical results, while the others are related with the features such like the memory capacity, the type of tasks being processed, the number of co-located VMs, and the hard disk type.
![img-4.jpeg](img-4.jpeg)

Fig. 4 The execution delay corresponds with different edge servers
Specifically, bodytrack and vips are the CPU-intensive applications, so they are sensitive to the number of CPU cores and has the longest execution time under C3. In addition, there are three VMs deployed on a same physical host in C3, so the competition for the underlying physical resources must be intense, resulting in the longest execution delay for all the benchmark applications. Moreover, the difference of C5 and C6 only lies in the CPU type and the CPU frequency, and C5 adopts an Intel CPU with the frequency of 3.3 GHz while C 6 uses an AMD CPU with the frequency of 3.6 GHz , yet the results show that the execution time of benchmark applications running on C6 are not always lower than which on C5.

The result proves that it is unreliable to analyze the application execution time on the edge servers only by CPU frequency and the number of CPU cores, thus it is necessary to predict the execution delay by incorporating multiple features.

# 6.3 RQ2. Execution Delay Prediction with EPBN 

We run the different types of benchmark applications on the edge servers configured in Table 4, and then repeat the processes for 100 times. Since the execution results are continuous and EPBN cannot handle, we first round the data instances and then further construct the delay prediction models by 5 -fold cross validation.

The EPBN is a machine-learning (ML) method, for the sake of fairness, we choose several ML-based models which have performed well in various scenarios in recent years as the baselines, whose details and the parameters setting are listed as follow.

- CBN (Class parameter augmented Bayesian Network) [11], with the parameters as max-depth $=5$, max-feature $=5$, iteration $=50$, which first clusters multiple features based on the Euclidean distances and classifies the different configurations via the XGboost, then constructs CBN via the classification results.
- RFBN (Random Forest-induced BN) [37], with the parameters as max-depth=5, max-feature $=5$, iteration $=50$, classifies the node values via random forests, and construct the model by the mutual information and maximum likelihood estimation.
- SC-MLP (Stochastic Computational Multi-Layer Perceptron) [38], which implements the backward propagation algorithm for updating the layer weights with the reduced hardware and the power consumption. Its parameters are set as hidden layers $=5$, number of cells in each layer $=8$, learning-rate $=0.1$, iterations $=120$, and the activation function was Sigmoid().
- LightGBM [39], with the parameters as learning-rate $=0.1$, min-child-sample $=20$, max-depth $=5$, num-leaves $=30$, excludes a significant proportion of data instances with small gradients by Gradient-based One-Side Sampling (GOSS), and then bundle mutually exclusive features to reduce the number of training data.
- SVM (Support Vector Machine), a representative machine learning method, whose kernel is set as the radial basis function (RBF).
- LR (Linear Regression), a supervised learning method, and we adopt the Lasso regression as the comparison.

When the $i$-th $(i \in\{1,2, \ldots, 5\})$ round of cross-validation performed, a corresponding confusion matrix can be generated, we then averaged the values and calculated the Micro-Precision, Micro-Recall and Micro-F1 as the evaluation metrics.

$$
\begin{gathered}
\text { Micro }-P=\frac{T P_{\text {ave }}}{T P_{\text {ave }}+F P_{\text {ave }}} \\
\text { Micro }-R=\frac{T P_{\text {ave }}}{T P_{\text {ave }}+F N_{\text {ave }}} \\
\text { Micro }-F 1=\frac{2 *(\text { Micro }-P) *(\text { Micro }-R)}{(\text { Micro }-P)+(\text { Micro }-R)}
\end{gathered}
$$

where $T P_{\text {ave }}, F P_{\text {ave }}$ and $F N_{\text {ave }}$ are the average values of True Positive (TP), False Positive (FP), True Negative (TN), False Negative (FN) within the 5 confusion matrices. Micro-F1 is a comprehensive metric which can evaluate the rates of precision and recall of the current model, and the model with the higher Micro-F1 value indicates the better performance. The experimental results are given in Table 5.

Table 5. Comparison the Evaluation Metrics


It can be concluded from Table 5 that EPBN outperforms all the other methods in most of the edge servers' configurations, with the average metrics as Micro-P=0.884, Micro-R $=0.877$ and Micro-F1 $=0.881$. LightGBM, with the Micro-P $=0.882$, Micro$\mathrm{R}=0.876$ and Micro-F1 $=0.862$, has the next best performance, which accords with the fact that boosting trees can deal with the tabular data with good performance. The performance of lasso is the worst because it is a linear model and uses a first-order parametric as the penalty function, which can simplify the model to some extent but cannot uncover the potential dependencies between the individual features, thus leading to unsatisfactory results.

# 6.4 RQ3. Optimize AR Task Offloading Strategy with PSO-GA 

We adopt the benchmark applications of streamcluster ( 0.74 MB ), bodytrack $(10.27 \mathrm{MB})$, vips $(15.87 \mathrm{MB})$, raytrace $(4.07 \mathrm{MB})$, and $X 264(1.76 \mathrm{MB})$ to simulate the AR subtasks with different resource requirements (the sizes of each application are included in bracket), and then use the VMs with the configurations of C 1 to C 6 as given in Table 4 to simulate the edge servers with different hardware and software features.

If AR subtasks are offloaded to the edge servers, then the corresponding delay consists of the upload/download delay and the execution time on the edge servers, while the latter can be predicted by EPBN. Otherwise, if the AR subtasks are executed on the mobile terminal, we simplify the task execution delay by Equ.(12).

Firstly, we test the convergence of PSO-GA when given different parameter settings as the number of iterations increases, and then give the results in Fig.5.
![img-5.jpeg](img-5.jpeg)
(a) PSO-GA with Different Velocity
![img-6.jpeg](img-6.jpeg)
(c) PSO-GA with different Mutate Probability
![img-7.jpeg](img-7.jpeg)
(b) PSO-GA with different Crossover Probability
![img-8.jpeg](img-8.jpeg)
(b) PSO-GA with different Initial Particles

Fig. 5 PSO-GA Convergence with Different Parameters
It can be seen from Fig.5(a) that when the velocity of PSO-GA is within the range of $[1,4]$, the execution time is decreasing as the values of Velocity increase, while it increases again when Velocity=5. A reasonable explanation is that there are only 5 AR subtasks, and Velocity=5 indicates to crossover and mutate all the strategies in one time

thus leads the uncertainty increases. The rest of the results in Fig. 5 show that PSO-GA converges as the number of iterations and the corresponding probability change.

Based on the results in Fig.5, we set the parameters as follows. Velocity $=3$, Iteration $=100$, the probabilities of crossover and mutation are $P_{C O}=0.4$ and $P_{M U}=0.2$, numbers of initial and updated particles are $n_{i n i}=100$ and $n_{p}=30$, frequency of mobile CPU is $f_{m}=1.8 \mathrm{GHz}$, the required CPU cycles is $\phi_{m}=100$, bandwidth of upload/download is set as $B_{m, k}=10 \mathrm{MB} / \mathrm{S}$.

To evaluate that our proposed PSO-GA method can optimize the AR task offloading strategy, we adopt the following methods as the baselines.

- Local[29], where all of the AR subtasks are executed on the mobile terminal so the results can be considered as the ground truth. We use the total sizes of the benchmark applications to calculate the corresponding delay, and then set the parameters as $\phi_{m}=$ $100, f_{m}=1.8 \mathrm{GHz}$.
- Random[6], where the AR subtasks and the parameter setting are identical with the applications sampled by PSO-GA, and the execution platforms are randomly selected among the mobile terminal and several edge servers.
- Greedy[40], where each subtask doesn't take the delay of the AR task into consideration, so the current subtask is offloaded to the edge server or executed on the mobile terminal with the lowest execution time. Besides, several AR subtasks cannot be co-located on a same edge server to avoid competition.
- GA[40], where offloading strategies are encoded as chromosomes, then converge to the best with the operations of single-point crossover and mutation.

We simulate AR tasks and then calculate the corresponding delay by all the algorithms. The processes are repeated 12 times and the results are shown in Fig.6.
![img-9.jpeg](img-9.jpeg)

Fig. 6 Delay corresponds with different offloading strategies
It can be seen from Fig. 6 that the AR task running under the Local mode has the longest execution delay, i.e., the Local performs the worst. The average, maximum and

minimal execution delay of Local are 130.32s, 252.94s and 56.06s respectively, and the shortest delay is since one of the AR subtasks is streamcluster, which has the smallest size and is best suited to execute on the mobile terminal. Random, with the average delay of 50.02 s , performs a little better than Local. The longest delay of Random is the test5, which runs multiple AR subtasks on mobile terminal, while the test6 performs best, where all the benchmark applications are offloaded to the suitable edge servers, thus making the delay closer to the PSO-GA results. The Greedy, whose average delay is 26.499 s , is deficient since it only makes the choice based on the current optimum and cannot consider the strategies globally. The average delay of GA is 35.166 s , and the biggest difference between GA and PSO-GA is that the latter accelerates the particle update rate by adapting the value of velocity $V$, whereas the GA involves only one update per iteration, and there is no guarantee of crossover chromosomes when performing the single-point crossover. In contrast, PSO-GA, with the average execution delay of 25.289 s , guarantees that the updated particle crossovers with the individual optimum, thus making the updates iterate to a more optimal direction.

Furthermore, to verify that PSO-GA can optimize the offloading strategies under different conditions, we performed multiple tests via changing the calculation power of mobile terminal, the bandwidth between the mobile devices and the edge servers, the number of edge servers, and the workload types. The results are given in Fig.7.
![img-10.jpeg](img-10.jpeg)
(a) PSO-GA with Different Mobile Terminal Frequency
![img-11.jpeg](img-11.jpeg)
(b) PSO-GA with Different Bandwidth

![img-12.jpeg](img-12.jpeg)
(c) PSO-GA with Different Edge Servers
(b) PSO-GA with Different Workload

Fig. 7 The performance of PSO-GA with different parameters
As it can be seen from Fig.7(a) that with the increase of the mobile terminal frequency, except for Local, the execution delay does not change much for the others, since that the applications with the large sizes are inappropriate for running on the mobile terminal. Therefore, even though the main frequency of the mobile terminal has improved, the latency of other algorithms does not show a significant decrease. This also proves the necessity of offloading applications to the edge servers. Moreover, we can conclude from Fig.7(b) that since the relatively small size of each application results in the insignificant changes of the transmission delay.

In conclusion, our proposed PSO-GA, with the average execution delay of 30.23 s , outperforms the others baselines and can yield optimal offloading strategies regardless of the conditions. While the average delay corresponding to the Local, Random, Greedy and GA are $189.57,61.49,31.64$ and 38.34 respectively.

# 7.Conclusion and Discussion 

We first divide a mobile AR task into five subsequent subtasks, namely video acquisition, position tracking, target mapping, object detection and result presentation. By collecting multiple features from edge servers, we construct an EPBN via the hillclimbing method as well as the maximum likelihood estimation, so as to predict the execution delay of each subtask on the different edge servers. Based on the prediction results, we analogize optimizing the task offloading strategy with minimal delay as to find the shortest path in the TSP map, and then propose a PSO-GA based heuristic method to solve this NP-hard problem. The simulation experiments prove the efficiency and effectiveness of our proposed methods.

In the future, we will consider the multi-user scenarios and take the energy

consumption of mobile terminals and the resource allocation of edge servers into consideration. At the same time, we will apply the deep reinforcement learning frameworks, like the deep deterministic policy gradient (DDPG) algorithm, to optimize the task offloading decision.

# Declaration 

Ethics approval and consent to participate: Not applicable.
Consent for publication: Written informed consent was obtained from the patient for publication of this case report and any accompanying images.
Availability of data and material: The datasets generated during the current study are available in the GitHub repository: https://github.com/haojiaYNU/simulation
Competing interests: All of the authors declare no conflicts of interest regarding to publish this paper.
Funding: This work is supported by National Natural Science Foundation of China (No.61862068), Youth Project of Applied Basic Research Program of Yunnan Province (NO.202201AU070050), Key Project of Applied Basic Research Program of Yunnan Province (NO. 202201AS070021)
Authors' contributions: Jia Hao was responsible for proposing the proposal, performing the validation, and the writing of the entire paper. Jianhou Gan is responsible for reviewing the full paper.
Acknowledgements: We thank the editor-in-chief and the reviewers of the Journal of the Grid Computing.
