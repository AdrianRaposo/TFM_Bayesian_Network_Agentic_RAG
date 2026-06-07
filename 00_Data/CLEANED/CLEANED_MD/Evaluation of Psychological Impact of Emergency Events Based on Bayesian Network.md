# Evaluation of Psychological Impact of Emergency Events Based on Bayesian Network 

Xin WANG ${ }^{1}$, Zhi Jie SONG ${ }^{2, \mathrm{a}}$, Rui $\mathrm{SHI}^{2}$<br>${ }^{1}$ School of Economics and Management, and School of Science, Yanshan University Qinhuangdao, China<br>${ }^{2}$ School of Economics and Management, Yanshan University, Qinhuangdao, China;


#### Abstract

Representation and inference of uncertain knowledge pose great challenge to the evaluation of the impact of emergency events on public psychology. With the advantages in solving issues on an uncertain basis, Bayesian network exhibits a superioty in effectively coping with the diversity, uncertainty and ambiguity of the evaluative information of emergency events. A model was established in this article to evaluate the impact caused by emergency events on the public's psychological health based on the Bayesian network. Moreover, the method of inference and decision-making was also presented, and an example analysis was performed. The result shows that the proposed model can improve the evaluation accuracy and the responsiveness of the managers when making decisions.


Keywords. Bayesian network; emergency events; public psychology; impact degree

## 1 Introduction

In recent years, the emergencies such as "9.11 Attacks" in the US in 2001, "SARS" outbreak in China in 2003 and Japan Tsunami in 2011 are reported all around the globe[1]. Emergency events bring threats to not only the human life and properties, but also the psychological trauma[1-2]. Many countries have attached great importance to emergency response management, with a release of a series of laws and regulations. The emergency response management is the subject of academic research in recent years[3]. The research and evaluation of the impact of emergency events on public's psychological health are complex and highly important[4]. It lays the basis for the prevention and control, rescue and handling of emergency events. The investigation in this respect also provides the basis for a reasonable decision making for the authorities. At present, some achievements have been made with respect to the evaluation of the impact degree of emergency events. The commonly used methods are fuzzy decision-making method, grey theory, neural network and genetic algorithm[5]. However, these methods can hardly solve the issue of the impact degree of the emergency events. That is, the inference based on uncertain information in combination with expert knowledge. Most of the existing studies concerning the impact of emergency events on the psychological health of the relevant parties are based on questionnaire survey or statistical analysis. Few have treated public psychology as a complex system comprising uncertain information.

Artificial intelligence can be applied to evaluate the impact of emergency events on public's psychological health, and inference is performed according to expert knowledge. Representation and inference of uncertain knowledge are two key processes in the evaluation of the psychological impact of emergency events. Bayesian network has found extensive applications as a framework of knowledge representation and probabilistic reasoning. The abilities to represent the uncertainty of and relevance between variables and to infer on an uncertain basis make the Bayesian network applicable to such evaluation [6]. Recently, the Bayesian network has been already employed in many fields, such as military decisionmaking, intelligent robot, pathological diagnosis, assessment of war situation, threat classification, fault diagnosis and the multi-attribute decision-making in uncertain environment [7-9]. A variety of adverse consequences resulting from emergency events were discussed in this article. The model for the evaluation of the impact of emergency events on public psychology was established based on the Bayesian network. The method of inference was expounded and its effectiveness was verified by example analysis.

## 2. Evaluation of the impact of emergency events on public psychology based on Bayesian network

To evaluate the impact of emergency events on public psychology based on Bayesian network, an evaluation model is first established. As the number of nodes

[^0]
[^0]:    ${ }^{a}$ Corresponding author: songzhj@ysu.edu.cn

increases in the Bayesian network, the establishment of model is a problem of combinatorial explosion. Reasonable principle and method have to be followed. The Bayesian network can be established through learning or artificially. Given the ample training samples, the learning is possible for establishing the network. Due to the small probability of emergency events, there will not be ample training data. Therefore, it is important to study the strategy and method for the establishment of Bayesian network. The evaluation of the impact of emergency events on public psychology based on Bayesian network consists of the following 6 steps.

### 2.1 Determining the contents of nodes

The Bayesian network is composed of nodes corresponding to different events. Hence it is necessary to identify the dimensions of adverse impact brought by emergency events on the psychology of the relevant parties. The adverse consequences of the emergency events can be multi-dimensional, including both direct and indirect impact. The time of post-disaster recovery and the situation of collaboration in post-disaster rescue have to be considered. Thus the psychological impact of emergency events is taken as the root node. The anxiety degree, sensitivity, degree of avoidance, coping style, time of post-disaster recovery and the collaboration in post-disaster rescue are taken as the nodes.

### 2.2 Determining the relationship between the nodes

After the determination of the contents of nodes, the casual relationship between the nodes is determined following a certain method. The evaluation of the psychological impact of emergency events is a highly complex issue. The impact analysis involves a large amount of uncertain knowledge, and the impact is either direct or indirect. The relevant evaluation work should be jointly undertaken by the experts and the decision-makers. The casual relationship between the contents of nodes and the nodes can be used to determine the structure of the Bayesian network. With the psychological impact of the emergency events as the root node and the different dimensions of the adverse consequences as the child nodes, the hierarchical structure of the impact of the emergency events is established, as shown in Fig. 1. The child nodes are subdivided to form more hierarchies of psychological impact of the emergency events. The hierarchical structure shown in Fig. 1 is considered as the topology of the Bayesian network for mapping the psychological impact.

![img-0.jpeg](img-0.jpeg)

Figure 1. Hierarchical structure of psychological impact of emergency events

### 2.3 Classification of node status

In case of disastrous events, the decision makers usually have inaccurate and obscure information at hand. Moreover, due to the limitations of the perception and accumulated knowledge of the decision makers, the subjective judgment of the decision makers plays the decisive role in regard to the impact degree of the emergency events. Here the impact degree of the nodes is divided into different discrete statuses. For example, the psychological impact of the emergency events as the root node (H) is divided into 4 degrees: very low (H1), low (H2), high (H3) and very high (H4). Similarly, the child nodes are also divided into different discrete statuses. For example, the anxiety degree (A) is divided into 3 levels: low (A1), moderate (A2) and high (A3).

### 2.4 Construction of conditional probability matrix for child nodes

With the topology of the Bayesian network, the conditional probability distribution of the child nodes is determined. For data with continuous values, discretization is performed for the nodes. A large number of sample data are required for quantitative data, while for qualitative data, the inference is made based on expert knowledge. The determination of the conditional probability in the Bayesian network is a complex process, designed by expert experience or statistical tests. The row of the conditional probability matrix represents the status of the emergency event as the root node; the column represents the status of the child nodes. The elements in the matrix indicate the impact degree of the reasons on the results, which is estimated by expert knowledge or based on professional literatures and statistical techniques. For example, according to expert knowledge, the status of root nodes is divided into four levels, which are very low (H1), low (H2), high (H3) and very high (H4). The conditional probability of the anxiety degree (A) is expressed as

If the psychological impact of the emergency event is very low (H1), then the probability of the anxiety degree (A) being low (A1), moderate (A2) and high (A3) is, respectively. If the psychological impact of the emergency event is low (H2), then the probability of anxiety degree (A) being low (A1), moderate (A2) and high (A3) is, respectively. If the psychological impact of the emergency event is high (H3), the probability of the anxiety degree (A) being low (A1), moderate (A2) and high (A3) is 0.15, 0.30 and 0.55, respectively. If the psychological impact of the emergency event is very high (H4), then the probability of anxiety degree (A) being low (A1), moderate (A2) and high (A3) is 0.02, 0.03, 0.95, respectively. According to expert knowledge, the conditional probability matrix of the node 'anxiety degree' (A) with respect to the root node is expressed as follows. Similarly, the conditional probability matrices of the nodes 'sensitivity', 'degree of avoidance', 'coping style',

'time of post-disaster recovery' and 'collaboration in post-disaster rescue' with respect to root node are constructed.

![img-1.jpeg](img-1.jpeg)

In the same way, for the hierarchical structure of psychological impact of emergency events shown in Fig. 1, the conditional probability matrix MB, MC, MD, ME, MF of child nodes with respect to the root node is obtained.

![img-2.jpeg](img-2.jpeg)

**Figure 2.** Tree-like Bayesian network structure

![img-3.jpeg](img-3.jpeg)

**Figure 3.** Persuasion propagation of influence degree assessment of emergent event

### 2.5 Algorithm of Bayesian inference

Bayesian inference is carried out based on priori information. With the conditional probability distribution of the leaf nodes being constant, the Bayesian network maintains the equilibrium. Once the status of the leaf nodes changes with the observation information, the status probability distribution will be updated for all the nodes in the entire network according to Peal algorithm. The simplified tree-like Bayesian network is used as the inference model. Every node of the tree-like Bayesian network only has one parent node, as shown in Fig. 2. The variables involved in the algorithm are listed below:

**Bel(X):** the status probability distribution of node reflects the occurrence probability of the event X under a certain scenario. It is a one-dimensional column vector, with the number of elements equal to that of the discrete values of node status.

**λ(X):** the diagnostic information is obtained from the child node, and it supports the diagnosis. It is a one-dimensional column vector, with the number of elements equal to that of the discrete values of X.

**π(X):** the casual information is obtained from the parent node, and it supports the forecast. It is a one-dimensional column vector, with the number of elements equal to that of the discrete values of parent nodes.

Using a single node as the center in the algorithm, **λ(X)** is obtained from the child node, and **π(X)** is obtained from the parent node. On this basis, **Bel(X)**, **λ(X)** and **π(X)** of the current nodes are calculated, and the adjacent nodes are triggered and updated.

These procedures are repeated until the posterior probability of all nodes is equal to the priori probability. At this time, the network reaches a new equilibrium. Based on the hierarchical structure of the psychological impact of the emergency events shown in Fig. 1, the calculation procedures are as follows:

1. The priori information **π(X)** of the root node **H** is determined. The confidence level **B(H)** of the root node **H** is initialized. Let **Bel(H)** = **π(H)**
2. If the diagnostic information of a child node **θ** changes into **λ**<sub>θ</sub>, then the diagnostic information of root node **H** will change accordingly:

**λ**<sub>H</sub> = **M**<sub>θ</sub> × **λ**<sub>θ</sub>

where **θ** represents a child node; **M**<sub>θ</sub> is the conditional probability of a child node with respect to root node, in the form of (3). The element in conditional probability matrix represents the impact degree of root node (**H**) on the child node.

1. The confidence level of the root node (**H**) (**H**) is upwards updated to:

**Bel(H)** = **a** × (**λ**<sub>H</sub> **gr(H)**)

where **R** is inner-product operator. That is, for two column vectors **β** = (**β**<sub>1</sub>, **β**<sub>2</sub>, **K**, **β**<sub>n</sub>), and **γ** = (**γ**<sub>1</sub>, **γ**<sub>2</sub>, **K**, **γ**<sub>n</sub>), the result of executing the operator is

**βgr** = (**β**<sub>1</sub> × **γ**<sub>1</sub>, **β**<sub>2</sub> × **γ**<sub>2</sub>, **K**, **β**<sub>n</sub> × **γ**<sub>n</sub>), ; **a** is the normalization factor, which is responsible for making the sum of confidence intervals of root node (**H**) under different status to be 1.

2. The confidence interval of the child node (**θ**) is downwards updated. The updated confidence interval of the child node (**θ**) is expressed as

**Bel(θ)** = **a** × **M**<sub>θ</sub><sup>T</sup> × **Bel(H)**

where **M**<sub>θ</sub><sup>T</sup> is the transpose of conditional probability matrix **M**<sub>θ</sub>; **a** is the normalization factor.

The process of Bayesian inference in regard to the psychological impact of the emergency events is shown in Fig. 3. In Fig. 3, the bottom-up inference indicates the impact degree of the emergency event inferred from one dimension of the adverse consequence of the emergency events. The top-down inference indicates the influence of the changes of psychological impacts of emergency event on the adverse consequences. In this way, Bayesian inference can be employed for bottom-up diagnostic inference and top-down casual inference, until the posteriori probability is equal to priori probability for all nodes.

Calculation of the degree of psychological impact
Suppose $Q=\left\{H_{i}, \mathrm{~K}, H_{o}\right\}$ is the set of status of root node $(H)$, where is the fuzzy comment made by the decision makers on the psychological impact of the emergency event on public psychology. For example, the fuzzy comment given by the decision makers with respect to the psychological impact of the emergency event may be very low $\left(H_{1}\right)$, low $\left(H_{2}\right)$, high $\left(H_{3}\right)$ and very high $\left(H_{4}\right) . U(Q)=\{u(H), \mathrm{K}, u(H)\}$ is the set of utility values of each status in the comment set. $u\left(H_{i}\right)(l=1, \ldots, n)$ are the fuzzy utility values of status $H_{i}$. Its value range is $0 \leq u\left(H_{i}\right) \leq 1$. For the same set of fuzzy comments, different decision makers may assign different utility values.

The psychological impact of the emergency event is determined by the confidence level of root node status and the fuzzy utility value when the network reaches the equilibrium.

$$
E(H)=\sum_{i=1}^{n}\left(u\left(H_{i}\right) \times \operatorname{Bel}\left(H_{i}\right)\right)
$$

## 3. Example analysis

A stampede occurring during a large-scale activity was studied as an example. The topology of the Bayesian network built for the emergency event and the subsequent adverse events is shown in Fig. 1. For root node $H$, the set of fuzzy comment is $Q \sim\left\{\right.$ very low $\left(H_{1}\right)$, low $\left(H_{2}\right)$, high $\left(H_{3}\right)$ and very high $\left(H_{4}\right\}$. The corresponding set of fuzzy utility values is $U(Q)=\{0.25 ; 0.50 ; 0.75 ; 1.0\}$. The set of anxiety degree $(A)$ is $\left\{\right.$ low $\left(A_{1}\right)$, moderate $\left(A_{2}\right)$, high $\left.A_{3}\right\}$; the set of sensitivity $(B)$ is $\left\{\right.$ low $\left(B_{1}\right)$, moderate $\left(B_{2}\right)$, high $\left(B_{3}\right)$. The set of the degree of avoidance $(C)$ is $\left\{\right.$ low $\left(C_{1}\right)$, moderate $\left(C_{2}\right)$, high $\left.\left(C_{3}\right)\right\}$; the set of coping style $(D)$ is $\{$ positive $\left(D_{1}\right)$, neutral $\left(D_{2}\right)$, negative $\left.\left(D_{3}\right)\right\}$. The set of the time of postdisaster recovery $(E)$ is $\left\{\right.$ short $\left(E_{1}\right)$, moderate $\left(E_{2}\right)$ and long $\left(E_{3}\right)\}$. The set of the status of collaboration in post-disaster rescue $(F)$ is $\{$ positive $\left(F_{1}\right)$, moderate $\left(F_{2}\right)$ and negative $\left(F_{3}\right)\}$. According to expert knowledge, the conditional probability matrix of child node $(A)$ with respect to root node is expressed as formula (3). The conditional probability matrices of child nodes $B, C, D, E$ and $F$ with respect to root node are MB,MC,MD,ME and MF.

Next the impact degree of emergency events on public psychology is calculated based on priori information.
(1) At the early stage of the stampede, the psychological impact caused by this event cannot be judged at all. Thus it is assumed that the probabilities of the impact degree being very low $\left(H_{1}\right)$, low $\left(H_{2}\right)$, high $\left(H_{3}\right)$ and very high $\left(H_{4}\right)$ are equal. That is, the priori information in regard to the psychological influence is
$\pi_{1}(H)=(0.25,0.25,0.25,0.25)^{T}$. At the early stage of the event, it is supposed by experts that the stampede has a considerably influence on the sensitivity, and its influence on the coping style is more likely to be of a moderate degree. However, there is no sufficient information on the child nodes such as degree of avoidance, time of post-disaster recovery and collaboration in post-disaster rescue. Thus the diagnostic information provided by the experts with respect to the child node is $\lambda_{A}=(0,0,1)^{T} ; \lambda_{B}=(0.3,0.4,0.3)^{T}$; $\lambda_{C}=(0.4,0.3,0.3)^{T} ; \lambda_{D}=(0.3,0.6,0.1)^{T} ;$ $\lambda_{E}=(0.3,0.4,0.3)^{T} ; \lambda_{F}=(0.3,0.4,0.3)^{T}$.

Here the confidence level $B(H)$ of the root node $(H)$ is initialized. The child nodes and the root nodes are updated under the given mode of information propagation. Hence the confidence level of the impact on the nodes at the early stage is $\operatorname{Bel}(H)=(0.0051,0.2595,0.4861,0.2480)^{T}$. This indicates that the probability that the impact degree of the event is high is the largest. This is because the confidence level of the status $\left(H_{3}\right)$ is 0.4861 . The probability that the impact degree of the event is low and very high is equal, with the confidence interval being, respectively 0.2595 and 0.2480 . The psychological impact of the emergency event determined by formula (8) is expressed as $E(H)=0.7431$.
(2) With the passage of time, the experts judge that the event has a great influence on the degree of avoidance based on the initial information $\pi_{1}(H)$. Moreover, it is judged that the influence on the time of post-disaster recovery and on the collaboration in post-disaster rescue is greater. Then the diagnostic information given by the experts on each child node is $\lambda_{A}=(0,0,1)^{T} ; \lambda_{B}=(0.3,0.4,0.3)^{T} ; \lambda_{C}=(0.4,0.3,0.3)^{T} ;$ $\lambda_{D}=(0,0,1)^{T} ; \lambda_{E}=(0.1,0.5,0.4)^{T} ; \lambda_{F}=(0.1,0.5,0.4)^{T}$. Hence the confidence level of the influence on the root node at the later stage of the event $(H)$ is expressed as:

$$
\operatorname{Bel}(H)=(0.0000,0.0085,0.2210,0.7711)^{T}
$$

It can be sure that the impact of the emergency event on public psychology is of high and very high degree. According to formula (8), the impact degree of the emergency event is calculated as $E(H)=0.9327$.

By using priori information, the Bayesian network can achieve a dynamic evaluation of the psychological impact of the emergency event. Thus the situation of the emergency event can be better evaluated to provide a basis for decision making.
(3) Priori information is highly important in the application of the Bayesian network. If the priori information is $\pi_{2}(H)=(0.10,0.80,0.10,0.00)^{T}$, the probability of the initial status of emergency event being very low $\left(H_{1}\right)$, low $\left(H_{2}\right)$, high $\left(H_{3}\right)$ and very high $\left(H_{4}\right)$ is $0.1,0.8,0.1$, and 0.0 , respectively. Thus the confidence interval of the psychological impact corresponding to situation (1) $\lambda_{A}=(0,0,1)^{T} ; \lambda_{B}=(0.3,0.4,0.3)^{T} ; \lambda_{C}=(0.4,0.3,0.3)^{T} ;$

$$
\begin{array}{ll}
\lambda_{D}=(0.3,0.6,0.1)^{T} & ; \quad \lambda_{E}=(0.3,0.4,0.3)^{T} \\
\lambda_{F}=(0.3,0.4,0.3)^{T} & \text { is } \\
\operatorname{Bel}(H)=(0.0021,0.8121,0.1765,0.0000)^{T} . \text { From formula }
\end{array}
$$

(8), the impact degree of the emergency event is calculated as $E(H)=0.5402$.

If the priori information is $\pi_{2}(H)=(0.10,0.10,0.80,0.00)^{T}$, the probability of the initial status of emergency event being very low $\left(H_{1}\right)$, low $\left(H_{2}\right)$, high $\left(H_{3}\right)$ and very high $\left(H_{4}\right)$ is $0.1,0.1$, 0.8 , and 0.0 , respectively. Thus the confidence interval of the psychological impact corresponding to situation (1)
$\lambda_{A}=(0,0,1)^{T} ; \lambda_{B}=(0.3,0.4,0.3)^{T} ; \lambda_{C}=(0.4,0.3,0.3)^{T} ;$
$\lambda_{D}=(0.3,0.6,0.1)^{T} ; \quad \lambda_{E}=(0.3,0.4,0.3)^{T} ;$
$\lambda_{F}=(0.3,0.4,0.3)^{T} \quad$ is
$\operatorname{Bel}(H)=(0.0012,0.0612,0.9256,0.0000)^{T} \quad$. From formula (8), the impact degree of the emergency event is calculated as $E(H)=0.7432$.

As seen from the evaluation results based on priori information $\pi_{1}(H), \pi_{2}(H)$ and $\pi_{3}(H)$, the evaluation results differ for the same input information at the child nodes due to the differences in priori information. For the same input information at the child nodes $\lambda_{A}=(0,0,1)^{T} ; \lambda_{B}=(0.3,0.4,0.3)^{T} ; \lambda_{C}=(0.4,0.3,0.3)^{T} ;$ $\lambda_{D}=(0.3,0.6,0.1)^{T} ; \quad \lambda_{E}=(0.3,0.4,0.3)^{T} ;$ $\lambda_{F}=(0.3,0.4,0.3)^{T}$, the confidence interval of the root node corresponding to priori information $\pi_{1}(H), \pi_{2}(H)$ and $\pi_{3}(H)$ is shown in Fig. 4.
![img-4.jpeg](img-4.jpeg)

Figure 4. Confidence of different states corresponding to different priori information

It can be seen from Fig. 4 that using the priori information $\pi_{1}(H)$, the impact degree is mainly of low $\left(H_{2}\right)$, high $\left(H_{3}\right)$ and very high $\left(H_{4}\right)$ level. The probabilities of being very low $\left(H_{2}\right)$ and very high $\left(H_{4}\right)$ are not significantly differed. However, under the priori information $\pi_{2}(H)$ and $\pi_{3}(H)$, there is an obvious difference in the probability of the impact degree, mainly due to the differences in priori information.

## 4. Summary

Bayesian network is a powerful graphical tool to represent the probability-based domain knowledge. With the ability of bidirectional inference, Bayesian network has shown prominent advantages in the evaluation of the impact of emergency events on public psychology. The representation and inference of uncertain knowledge are the main aspects in regard to the evaluation of the psychological impact of the emergency events. The model for the evaluation of the impact degree of emergency events on public psychology was proposed based on Bayesian network. This method not only integrates expert experience and knowledge, but also enables multi-stage inference by utilizing all available information. The model can accurately characterize the impact degree and satisfy the requirements for realtimeliness, dynamics and rapidity of evaluation. The execution of Bayesian network can enhance the degree of intelligence and the effectiveness of decision making during the emergency handling process.

## Acknowledgment

This study was supported by a Grant from National Natural Science Foundation of China for Prof. Zhijie Song (71171175).
