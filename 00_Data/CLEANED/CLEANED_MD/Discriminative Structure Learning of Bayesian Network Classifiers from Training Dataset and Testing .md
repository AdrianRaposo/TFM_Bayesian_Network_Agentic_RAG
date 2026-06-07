# Article 

## Discriminative Structure Learning of Bayesian Network Classifiers from Training Dataset and Testing Instance

Limin Wang ${ }^{1,2}$ (D) Yang Liu ${ }^{1,2}$, Musa Mammadov ${ }^{3}$, Minghui Sun ${ }^{1,2, *}$ and Sikai Qi ${ }^{1,2}$<br>1 Key Laboratory of Symbolic Computation and Knowledge Engineering of Ministry of Education, Jilin University, Changchun 130012, China; wanglim@jlu.edu.cn (L.W.); yliu15@mails.jlu.edu.cn (Y.L.); qisk18@mails.jlu.edu.cn (S.Q.)<br>2 College of Computer Science and Technology, Jilin University, Changchun 130012, China<br>3 Faculty of Science, Engineering \& Built Environment, Deakin University, Burwood, VIC 3125, Australia; musa.mammadov@deakin.edu.au<br>* Correspondence: smh@jlu.edu.cn; Tel.: +86-188-4411-4720

Received: 12 February 2019; Accepted: 6 May 2019; Published: 13 May 2019


#### Abstract

Over recent decades, the rapid growth in data makes ever more urgent the quest for highly scalable Bayesian networks that have better classification performance and expressivity (that is, capacity to respectively describe dependence relationships between attributes in different situations). To reduce the search space of possible attribute orders, $k$-dependence Bayesian classifier (KDB) simply applies mutual information to sort attributes. This sorting strategy is very efficient but it neglects the conditional dependencies between attributes and is sub-optimal. In this paper, we propose a novel sorting strategy and extend KDB from a single restricted network to unrestricted ensemble networks, i.e., unrestricted Bayesian classifier (UKDB), in terms of Markov blanket analysis and target learning. Target learning is a framework that takes each unlabeled testing instance $\mathcal{P}$ as a target and builds a specific Bayesian model Bayesian network classifiers (BNC) ${ }_{\mathcal{P}}$ to complement $\mathrm{BNC}_{\mathcal{T}}$ learned from training data $\mathcal{T}$. UKDB respectively introduced $\mathrm{UKDB}_{\mathcal{P}}$ and $\mathrm{UKDB}_{\mathcal{T}}$ to flexibly describe the change in dependence relationships for different testing instances and the robust dependence relationships implicated in training data. They both use UKDB as the base classifier by applying the same learning strategy while modeling different parts of the data space, thus they are complementary in nature. The extensive experimental results on the Wisconsin breast cancer database for case study and other 10 datasets by involving classifiers with different structure complexities, such as Naive Bayes ( 0 -dependence), Tree augmented Naive Bayes ( 1 -dependence) and KDB (arbitrary $k$-dependence), prove the effectiveness and robustness of the proposed approach.


Keywords: Bayesian network classifiers; Markov blanket; target learning

## 1. Introduction

Since 1995, researchers have proposed to embed machine-learning techniques into a computer-aided system, such as medical diagnosis system [1-4]. Andres et al. [5] proposed an ensemble of fuzzy system and evolutionary algorithm for breast cancer diagnosis, which can evaluate the confidence level to which the system responds and clarifies the working mechanism of how it derives its outputs. Huang et al. [6] constructed a hybrid SVM-based strategy with feature selection to find the important risk factor for breast cancer. Generally speaking, without domain-specific expertise in medicine, researchers in data mining prefer models with high classification accuracy and low computational complexity. In contrast, common people (including patients and their relatives) hope that the models can have high-level interpretability simultaneously. Bayesian network classifiers (BNCs) are such

models that can graphically describe the conditional dependence between attributes (or variables) and be considered to be one of the most promising graph models [7,8]. It can mine statistical knowledge from data and infer under conditions of uncertainty [9,10]. BNCs, from 0-dependence Naive Bayes (NB) [11] to 1-dependence tree augmented Naive Bayes (TAN) [12], then to arbitrary $k$-dependence Bayesian classifier (KDB) [13], can represent the knowledge with complex or simple network structure. KDB can theoretically represent conditional dependence relationships of arbitrary complexity. However, this approach is not effective for some specific cases. The model learned from training data may not definitely fit all testing instances. Otherwise, its bias and variance will always be 0 , which is against the bias-variance dilemma [14]. In the case of breast cancer, for different specific cases, the dependence relationships between attributes may be different. For BNCs, conditional mutual information (CMI) [15], $I\left(X_{i} ; X_{j} \mid C\right)$, is commonly used to measure the conditional dependence relationship between attributes $X_{i}$ and $X_{j}$ given class variable $C$ :

$$
\begin{aligned}
I\left(X_{i} ; X_{j} \mid C\right) & =\sum_{x_{i} \in X_{i}} \sum_{x_{j} \in X_{j}} \sum_{c \in C} P\left(x_{i}, x_{j}, c\right) \log \frac{P\left(x_{i}, x_{j} \mid c\right)}{P\left(x_{i} \mid c\right) * P\left(x_{j} \mid c\right)} \\
& =\sum_{x_{i} \in X_{i}} \sum_{x_{j} \in X_{j}} \sum_{c \in C} I\left(x_{i} ; x_{j} \mid c\right)
\end{aligned}
$$

$I\left(X_{i} ; X_{j} \mid C\right)$ can measure the conditional dependence between attributes between attributes $X_{i}$ and $X_{j}$ given class $C$. Correspondingly, $I\left(x_{i} ; x_{j} \mid c\right)$ can measure the conditional dependence between them when they take specific values. When $P\left(x_{i}, x_{j} \mid c\right)>P\left(x_{i} \mid c\right) * P\left(x_{j} \mid c\right)$ or $\log \left(P\left(x_{i}, x_{j} \mid c\right) /\left(P\left(x_{i} \mid c\right)\right.\right.$ * $\left.\left.P\left(x_{j} \mid c\right)\right)>0, I\left(x_{i} ; x_{j} \mid c\right)>0$ holds and the relationship between attribute values $x_{i}$ and $x_{j}$ can be considered to be conditional dependence. In contrast, when $P\left(x_{i}, x_{j} \mid c\right)<P\left(x_{i} \mid c\right) * P\left(x_{j} \mid c\right)$ or $\log \left(P\left(x_{i}, x_{j} \mid c\right) /\left(P\left(x_{i} \mid c\right) * P\left(x_{j} \mid c\right)\right)<0, I\left(x_{i} ; x_{j} \mid c\right)<0\right.$ holds and we argue that the relationship between attribute values $x_{i}$ and $x_{j}$ can be considered to be conditional independence. When $P\left(x_{i}, x_{j} \mid c\right)=$ $P\left(x_{i} \mid c\right) * P\left(x_{j} \mid c\right)$ and $I\left(x_{i} ; x_{j} \mid c\right)=0$, the relationship between attribute values $x_{i}$ and $x_{j}$ just turns from conditional dependence to conditional independence. On dataset WBC (breast cancer), $I\left(X_{1} ; X_{2} \mid C\right)$ achieves the largest value of CMI ( 0.4733 ) among all attribute pairs. The distribution of $I\left(x_{i} ; x_{j} \mid c\right)$, which correspond to different attribute value pairs of $X_{1}$ and $X_{2}$, are shown in Figure 1. As shown in Figure 1, the relationship between attributes $X_{1}$ and $X_{2}$ is dependent in general because the positive values of $I\left(x_{1} ; x_{2} \mid c\right)$, which represent conditional dependence, have a high proportion among all the values. In addition, some $I\left(x_{1} ; x_{2} \mid c\right)$ values are especially large. In contrast, there also exist some negative values of $I\left(x_{1} ; x_{2} \mid c\right)$ that represent conditional independence, i.e., the dependence relationship may be different rather than invariant when attributes take different values. However, general BNCs (like NB, TAN and KDB), which only build one model to fit training instances, cannot capture this difference and cannot represent the dependence relationships flexibly.

To meet the needs of experts in machine learning or in medicine, common people (including patients and their relatives) and the problem of breast cancer mentioned above, we propose a novel sorting strategy and extend KDB from a single restricted network to unrestricted ensemble networks, i.e., unrestricted $k$-dependence Bayesian classifier (UKDB), in terms of Markov blanket analysis and target learning. Target learning [16] is a framework that takes each unlabeled testing instance $\mathcal{P}$ as a target and builds a specific Bayesian model $\mathrm{BNC}_{\mathcal{P}}$ to complement $\mathrm{BNC}_{\mathcal{T}}$ learned from training data $\mathcal{T}$.

To clarify the basic idea of UKDB, we introduce two concepts: "Domain knowledge", which expresses a general knowledge framework learned from the training data, it focuses on describing interdependencies between attributes, such as attribute $A_{1}$ and $B_{1}$. In addition, "Personalized knowledge", which expresses a specific knowledge framework learned from the attribute values in the testing instance, such as attribute $A_{1}=a_{1}$ and $B_{1}=b_{1}$. Take breast cancer as an example, there is a strong correlation between attributes "Clump Thickness" and "Uniformity of Cell Size" (corresponding CMI achieves the maximum value, i.e., 0.4733 ), which can be considered to be the

domain knowledge. In contrast, for a testing instance with attribute values "Clump Thickness = 1" and "Uniformity of Cell Size = 3", the dependence relationship between those attribute values is approximately independent (corresponding value of CMI is 0.0002), which can be regarded as the personalized knowledge. The personalized knowledge with clear expressivity (capacity to respectively describe dependence relationships between attributes in different situations.) and tight coupling (capacity to describe the most significant dependencies between attributes.) makes ever more urgent the quest for highly scalable learners.
![img-0.jpeg](img-0.jpeg)

Figure 1. The distribution of $I\left(x_{i} ; x_{j} \mid c\right)$ between attributes $X_{1}$ and $X_{2}$ on dataset WBC.
UKDB contains two sub-models: $\mathrm{UKDB}_{\mathcal{T}}$ and $\mathrm{UKDB}_{\mathcal{P}}$. $\mathrm{UKDB}_{\mathcal{T}}$ is learned from training data $\mathcal{T}$, which can be thought of as a spectrum of dependencies and is a statistical form of domain knowledge. $\mathrm{UKDB}_{\mathcal{P}}$ is a specific BNC to mine the personalized knowledge implicated in each single testing instance $\mathcal{P}$, i.e., the specific knowledge that describes the conditional dependency between the attribute values in each single testing instance $\mathcal{P} . \mathrm{UKDB}_{\mathcal{P}}$ and $\mathrm{UKDB}_{\mathcal{T}}$ apply the same strategy to build the network structure, but they apply different probability distributions and target different data spaces, thus they are complementary in nature, i.e., in contrast to restricted BNC, e.g., KDB, UKDB can discriminatively learn different unrestricted Bayesian network structures to represent different knowledge from training dataset and testing instance, respectively.

The Wisconsin breast cancer (WBC) database [17] is usually used as a benchmark dataset [1-4] and is also selected in our main experiments for case study to demonstrate personalized Bayesian networks (BN) structures. The case study on the WBC database, as well as an extensive experimental comparison on additional 10 UCI datasets by involving some benchmark BNCs, show the advantages of the proposed approach.

# 2. Bayesian Network and Markov Blanket 

All the symbols used in this paper are shown in Table 1. We wish to build a Bayesian network classifier from labeled training dataset $\mathcal{T}$ such that the classifier can estimate the probability $P(c \mid \mathbf{x})$ and assign a discrete class label $c \in \Omega_{C}$ to a testing instance $\mathbf{x}=\left(x_{1}, \cdots, x_{n}\right)$. BNs are powerful tools for knowledge representation and inference under conditions of uncertainty. A BN consists of two parts: the qualitative one in the form of a directed acyclic graph. Each node of the graph represents a variable in the training data and the directed edges between pairs of nodes represent dependence relationships between them; and the quantitative one based on local probability distributions for specifying the


dependence relationships. Even though BNs can deal with continuous variables, we exclusively discuss BNs with discrete nodes in this paper. Directed edges represent statistical or causal dependencies among the variables. The directions are used to define the parent-children relationships. For example, given an edge $X \rightarrow Y, X$ is the parent node of $Y$, and $Y$ is the children node.

Table 1. List of symbols used.

A node is conditionally independent of every other node in the graph given its parents $\left(X_{p}\right)$, its children $\left(X_{c}\right)$, and the other parents of its children $\left(X_{c p}\right) .\left\{X_{p}, X_{c}, X_{c p}\right\}$ forms the Markov blanket of the node [7], which contains all necessary information or knowledge to describe the relationships between that node and other nodes. BNCs are special type of BNs. By applying different learning strategies, BNCs encode the dependence relationships between predictive attributes $X=\left\{X_{1}, \cdots, X_{n}\right\}$ and class variable $C$. Thus, the Markov blanket for variable $C$ can provide the necessary knowledge for classification.

Suppose that $X$ is divided into three parts, i.e., $X=\left\{X_{p}, X_{c}, X_{c p}\right\}$, the joint probability distribution $P(\mathbf{x}, c)$ can be described in the form of chain rule,

$$
\begin{aligned}
P(\mathbf{x}, c) & =P\left(x_{p}, x_{c p}, x_{c}, c\right) \\
& =P\left(x_{p}\right) P\left(c \mid x_{p}\right) P\left(x_{c p} \mid x_{p}, c\right) P\left(x_{c} \mid x_{c p}, x_{p}, c\right)
\end{aligned}
$$

The unrestricted BNC shown in Figure 2, which corresponds to (2), is a full Bayesian classifier (i.e., no independencies). The computational complexity in such an unrestricted model is an NP-hard problem.
![img-1.jpeg](img-1.jpeg)

Figure 2. Unrestricted Bayesian classifier corresponding to joint probability distribution.
NB is the simplest of the BNCs. Given the class variable $C$, the predictive attributes are supposed to be conditionally independent of one another, i.e.,

$$
P_{\mathrm{NB}}(\mathbf{x} \mid c)=\prod_{i=1}^{n} P\left(x_{i} \mid c\right)
$$

Even though the supposition rarely holds, its classification performance is competitive to some benchmark algorithms, e.g., decision tree, due to the insensitivity to the changes in training data and approximate estimation of the conditional probabilities $P\left(x_{i} \mid c\right)$ [10]. Figure 3 shows the structure of NB. In contrast to Figure 2, there exists no edge between attribute nodes for NB and thus it can represent 0 conditional dependencies. It is obvious that the conditional independence assumption is too strict to be true in reality. When dealing with complex attribute dependencies, that will result in classification bias.
![img-2.jpeg](img-2.jpeg)

Figure 3. An example of Naive Bayes.
TAN relaxes the independence assumption and extends NB from 0 -dependence tree to 1-dependence maximum weighted spanning tree [12]. The joint probability for TAN turns to be

$$
P_{\mathrm{TAN}}(\mathbf{x}, c)=P(c) P\left(x_{1} \mid c\right) \prod_{i=2}^{n} P\left(x_{i} \mid c, x_{j}\right)
$$

where $X_{i}$ is the parent attribute of $X_{i}$. The constraint on the number of parents intensively requires that only the most significant, i.e., $0+1+\cdots+1=n-1$, conditional dependencies are allowed to be represented. By comparing CMI, the edge between $X_{i}$ and $X_{j}$ will be added to the network in turn to build a maximal spanning tree. Once the conditional independence assumption does not hold, TAN is supposed to achieve better classification performance than NB. An example of TAN is shown in Figure 4.
![img-3.jpeg](img-3.jpeg)

Figure 4. An example of Tree augmented Naive Bayes.
KDB can represent arbitrary degree of dependence and control its bias/variance trade-off with a single parameter, $k$. By comparing mutual information (MI) $I\left(X_{i} ; C\right)$ [15], attributes will be sorted in descending order and enter the network structure in turn.

$$
I\left(X_{i} ; C\right)=\sum_{x_{i} \in X_{i}} \sum_{c \in C} P\left(x_{i}, c\right) \log \frac{P\left(x_{i}, c\right)}{P\left(x_{i}\right) P(c)}
$$

To control the structure complexity, each attribute $X_{i}$ is required to have no more than $k$ parent attributes. Thus, for any of the first $k+1$ attributes in the order, they will indiscriminately select all the attributes already in the model as its parents. For the other attributes, they will select $k$ parent attributes which correspond to the highest values of $I\left(X_{i} ; X_{j} \mid C\right)$ where $X_{j}$ ranks before $X_{i}$.

Suppose that the attribute order is $\left\{X_{1}, \cdots, X_{n}\right\}$, the joint probability for KDB turns to be

$$
P_{\mathrm{KDB}}(\mathbf{x}, c)=P(c) \prod_{i=1}^{n} P\left(x_{i} \mid c, \pi_{x_{i}}\right)
$$

where $\pi_{x_{i}}=\left\{X_{i_{1}}, \cdots, X_{i_{j}}\right\}$ are the $j$ parent attributes of $X_{i}$ in the structure, where $j=\min \{i-$ $1, k\}$. KDB can represent $n k-\frac{k^{2}}{2}-\frac{k}{2}$ conditional dependencies. When $k=1$, KDB represents the same number of conditional dependencies of TAN. As $k$ increases, KDB can represent increasingly conditional dependencies. Figure 5 shows an example of KDB when $k=2$.
![img-4.jpeg](img-4.jpeg)

Figure 5. An example of $k$-dependence Bayesian classifier when $k=2$.
Since KDB can be extended to describe dependence relationships of arbitrary degree and thus demonstrates its flexibility, researchers proposed many important refinements to improve its performance [18-21]. Pernkopf and Bilmes [22] proposed a greedy heuristic strategy to determine the attribute order by comparing $I\left(C ; X_{i} \mid X_{j}\right)$ where $X_{j}$ ranks higher than $X_{i}$ in the order, i.e., $i>j$. Taheri et al. [23] proposed to build a dynamic structure without specifying $k$ a priori, and they proved that the resulting BNC is optimal.

# 3. The UKDB Algorithm 

According to generative approach, the restricted BNCs, which take class variable $C$ as the common parent of all predictive attributes, define a unique joint probability distribution $P(\mathbf{x}, c)$ in the form of chain rule of lower-order conditional probabilities,

$$
P(\mathbf{x}, c)=P(c) P\left(x_{1} \mid c\right) P\left(x_{2} \mid x_{1}, c\right) \cdots P\left(x_{n} \mid x_{1}, \cdots, x_{n-1}, c\right)
$$

The corresponding classification rule is

$$
c^{*}=\arg \max P(\mathbf{x}, c)=\arg \max P(c) P\left(x_{1} \mid c\right) \cdots P\left(x_{n} \mid x_{1}, \cdots, x_{n-1}, c\right)
$$

To maximize $P(\mathbf{x}, c)$, an ideal condition is that each factor $P\left(x_{i} \mid x_{1}, \cdots, x_{i-1}, c\right)$ will be maximized. In other words, $X_{i}$ should be strongly dependent on its parents, especially on class variable $C$. Given limited number of training instances, the reliability of conditional probability estimation $P\left(x_{i} \mid \Pi_{i}, c\right)$ will increase as the dependence relationships between $X_{i}$ and its parent attributes increases. To achieve the trade-off between classification performance and structure complexity,

only limited number of dependence relationships will be represented by BNs, e.g., KDB. In addition, the classification rule for KDB turns to be

$$
c^{*}=\arg \max \hat{P}(\mathbf{x}, c)=\arg \max P(c) \prod_{i=1}^{n} P\left(x_{i} \mid \Pi_{i}, c\right)
$$

where $\Pi_{i}$ is one subset of $\left\{X_{1}, \cdots, X_{i-1}\right\}$ and contains at most $k$ attributes. Obviously, $P(\mathbf{x}, c) \neq \hat{P}(\mathbf{x}, c)$. No matter what the attribute order is, the full BNC represents the same joint distribution, i.e., $P(\mathbf{x}, c)$. In contrast, from Equation (8) we can see that for different attribute orders, the candidate parents for $X_{i}$ may differ greatly. The joint distributions $\hat{P}(\mathbf{x}, c)$ represented by KDBs learned from different attribute orders may not surely be same. The key issue for structure learning of restricted BNC is how to describe the most significant conditional dependence relationships among predictive attributes, or more precisely, the relationships between $X_{i}$ and its parent attribute $X_{j}(i>j)$. However for KDB , the attributes are sorted in descending order of $I\left(X_{i} ; C\right)$, which only considers the dependence relationship between $X_{i}$ and class variable $C$ while neglecting the conditional dependence relationships between $X_{i}$ and its parents. If the first few attributes in the order are relatively independent of each other, the robustness of the network structure will be damaged from the beginning of structure learning. To address this issue, UKDB selects the parents of variable $C$, or $X_{p}$, which are also the parents of the other attributes from the viewpoint of Markov blanket. In addition, there exist strong conditional dependence relationships between $X_{p}$ and the other attributes. On the other hand, $k$ corresponds to the maximum allowable degree of attribute dependence, thus the number of attributes in $X_{p}$ is $k$.

Suppose that attribute set $X_{p}$ contains $k$ attributes $\left\{X_{n-k+1}, \cdots, X_{n}\right\}$ and the order of attributes in $X$ is $\left\{X_{p}, X_{1}, \cdots, X_{n-k}\right\}$, Formula (7) can be rewritten in another form,

$$
P(\mathbf{x}, c)=P\left(x_{p}\right) P\left(c \mid x_{p}\right) \cdots P\left(x_{n-k} \mid x_{p}, x_{1}, \cdots, x_{n-k-1}, c\right)(k \geq 1)
$$

The relationships between $X_{i}$ and its parents corresponding to Equations (7) and (10) are shown in Table 2.

Table 2. The relationships between $X_{i}$ and its parents corresponding to the restricted and unrestricted BNC.


Since $P\left(x_{p}\right)$ is irrelevant to the classification, then

$$
P(c, \mathbf{x}) \propto P\left(c \mid x_{p}\right) P\left(x_{1} \mid x_{p}, c\right) \cdots P\left(x_{n-k} \mid x_{p}, x_{1}, \cdots, x_{n-k-1}, c\right)
$$

Thus, UKDB uses the following formula for classification,

$$
c^{*}=\arg \max \hat{P}(\mathbf{x}, c)=\arg \max P\left(c \mid x_{p}\right) \prod_{i=1}^{n-k} P\left(x_{i} \mid \hat{\Pi}_{i}, c\right)
$$

where $\hat{\Pi}_{i}$ is one subset of $\left\{X_{p}, X_{1}, \cdots, X_{i-1}\right\}$ and contains $k$ attributes. For any attribute $X_{i}\left(X_{i} \in X_{p}\right)$, $X_{i}$ is the parent of the other attributes, then there should exist strong conditional dependencies, or tight

coupling, between them. To this end, we sort the attributes by comparing the sum of CMI. To express this clearly in the following discussion, we sort the attributes by comparing the sum of CMI (SCMI) and $\operatorname{SCMI}\left(X_{i}\right)=\sum_{j} I\left(X_{i} ; X_{j} \mid C\right)\left(X_{i} \neq X_{j}\right)$. The first $k$ attributes in the order with the largest SCMI are selected as $X_{p}$. To control the structure complexity, UKDB also require that $X_{i}$ should select at most $k$ parents from $\Pi_{i}$ as shown in Table 2. The attribute sets $X_{c}$ and $X_{c p}$ will be determined thereafter. Figure 6 shows two examples of UKDB when $k=1$ and $k=2$.
![img-5.jpeg](img-5.jpeg)

Figure 6. Two examples of UKDB when $k=1$ and $k=2$.
In the real world, when attributes take different values the same dependence relationships between them may lead to wrong diagnosis or therapy. Considering attributes Sex and Pregnant, Sex = "Female" and Pregnant = "Yes" are highly related, whereas Sex = "female" and Pregnant = "No" also hold for some instances. Obviously, treatment of breast cancer during pregnancy should be different to that during non-pregnancy. CMI can weigh the conditional dependency between Sex and Pregnant, but cannot discriminately weigh the dependencies when these two attributes take different values. Target learning takes each testing instance $\mathcal{P}=\left\{x_{1}, \cdots, x_{n}, c=?\right\}$ as a target and tries to mine the dependence relationships between these attribute values [16]. From Equations (1) and (5), we have the following equations:

$$
\left\{\begin{array}{l}
I\left(X_{i} ; C\right)=\sum_{x_{i} \in X_{i}} I\left(x_{i} ; C\right) \\
I\left(X_{i} ; X_{j} \mid C\right)=\sum_{x_{i} \in X_{i}} \sum_{x_{j} \in X_{j}} I\left(x_{i} ; x_{j} \mid C\right)
\end{array}\right.
$$

where

$$
\left\{\begin{array}{l}
I\left(x_{i} ; C\right)=\sum_{c \in \mathrm{C}} P\left(c, x_{i}\right) \log \frac{P\left(c, x_{i}\right)}{P(c) P\left(x_{i}\right)} \\
I\left(x_{i} ; x_{j} \mid C\right)=\sum_{c \in C} P\left(x_{i}, x_{j}, c\right) \log \frac{P\left(x_{i}, x_{j} \mid c\right)}{P\left(x_{i} \mid c\right) P\left(x_{j} \mid c\right)}
\end{array}\right.
$$

The definitions of MI and CMI are measures of the average dependence between attributes implicated in the training data. In contrast to those, local mutual information (LMI) $I\left(x_{i} ; C\right)$ and conditional local mutual information (CLMI) $I\left(x_{i} ; x_{j} \mid C\right)$ can weigh the direct dependence and conditional dependence relationships between attribute values implicated in each instance [16,24]. Similarly, we sort the attribute values by comparing the sum of CLMI (SCLMI) and $\operatorname{SCLMI}\left(x_{i}\right)=\sum_{j} I\left(x_{i} ; x_{j} \mid C\right)\left(x_{i} \neq x_{j}\right)$.

For Bayesian inference, LMI refers to the event when $X_{i}=x_{i}$ and can be used to measure the expected value of mutual dependence between $X_{i}$ and $C$ after observing that $X_{i}=x_{i}$. CLMI can be used to weigh the conditional dependence between attribute values $x_{i}$ and $x_{j}$ while considering all possible values of variable $C$.

From Equations (1) and (5), to compute $I\left(X_{i} ; C\right)$ or $I\left(X_{i} ; X_{j} \mid C\right)$, all possible values of attribute $X_{i}$ need to be considered. If there exist missing or unknown value for attribute $X_{i}$ and $X_{j}$ in any instance, they will be replaced by some values and noise may be artificially introduced into the computation of $I\left(X_{i} ; C\right)$ or $I\left(X_{i} ; X_{j} \mid C\right)$. These missing or unknown values are regarded as noisy because the conditional dependence relationships between them and other non-noisy attribute values may be incorrectly measured. If the noisy part only account for a small portion of the non-noisy part,

the dependence relationships learned from training data may be still of high-confidence level and the network structure of $\mathrm{UKDB}_{\mathcal{T}}$ may be still robust. In contrast, from the definitions of LMI and CLMI (Equation (14)) we can see that for specific instance $\mathbf{x}$, to compute $I\left(x_{i} ; C\right)$ or $I\left(x_{i} ; x_{j} \mid C\right)$ only these attribute values in $\mathbf{x}$ need to be considered. The computation of $I\left(x_{i} ; C\right)$ or $I\left(x_{i} ; x_{j} \mid C\right)$ concerning noisy values will not be needed. Thus, neglecting these noisy conditional dependence relationships may make the network structure of $\mathrm{UKDB}_{\mathcal{P}}$ more robust.

We propose to use the Markov blanket and target learning to build an ensemble of two unrestricted $\mathrm{BNCs}$, i.e., $\mathrm{UKDB}_{\mathcal{T}}$ and $\mathrm{UKDB}_{\mathcal{P}}$. $\mathrm{UKDB}_{\mathcal{T}}$ and $\mathrm{UKDB}_{\mathcal{P}}$ learn from different parts data space and their learning procedures are almost the same, thus they are complementary in nature. In the training phase, by calculating MI and CMI, UKDB $_{\mathcal{T}}$ describes the global conditional dependencies implicated in training data $\mathcal{T}$. Correspondingly, in the classification phase, by calculating LMI and CLMI, UKDB ${ }_{\mathcal{P}}$ describes the local conditional dependencies implicated in unlabeled testing instance $\mathcal{P}$. Breiman [25] revealed that ensemble learning brings improvement in accuracy only to those "unstable" learning algorithms, in the sense that small variations in the training set would lead them to produce very different models. UKDB $_{\mathcal{T}}$ and UKDB $_{\mathcal{P}}$ are such algorithms. UKDB $_{\mathcal{T}}$ tries to learn the certain domain knowledge implicated in training dataset, whereas the domain knowledge may not describe the conditional dependencies in testing instance $\mathcal{P}$. It may cause overfitting on the training set and underfitting on the testing instance. In contrast, UKDB $_{\mathcal{P}}$ can describe the conditional dependencies implicated in testing instance $\mathcal{P}$, whereas the personalized knowledge is uncertain since the class label of $\mathcal{P}$ is unknown. It may cause underfitting on the training set and overfitting on the testing instance. Thus, an ensemble of $\mathrm{UKDB}_{\mathcal{T}}$ and $\mathrm{UKDB}_{\mathcal{P}}$ may be much more appropriate for making the final prediction.

The learning procedures of $\mathrm{UKDB}_{\mathcal{T}}$ is described by Algorithm 1 as follows:

```
Algorithm 1: The \(\mathrm{UKDB}_{\mathcal{T}}\) algorithm
    Input: Training set \(\mathcal{T}\) with attributes \(\left\{X_{1}, \cdots, X_{n}\right\}, k\).
    Output: The \(B N\) of \(\mathrm{UKDB}_{\mathcal{T}}\).
    Let Bayesian network \(B N=\{\mathcal{N}, \mathcal{A}\}\), where \(\mathcal{N}\) denotes the node set and \(\mathcal{A}\) the edge set.
    Calculate SCMI and sort predictive attributes into list \(\mathcal{L}\) in descending order of SCMI.
    Calculate MI and sort predictive attributes into list \(\hat{\mathcal{L}}\) in descending order of MI.
    Let \(\hat{\mathcal{L}}=\left\{\mathcal{L}_{1}, \cdots, \mathcal{L}_{k}, \hat{\mathcal{L}}_{1}, \cdots, \hat{\mathcal{L}}_{n-k}\right\}\).
    \(\mathcal{N}=\{C\} ; \mathcal{A}=\varnothing\);
    for \(i=1 \rightarrow k\) do
        \(\mathcal{N}=\mathcal{N} \cup \hat{\mathcal{L}}[i]\);
        \(\mathcal{A}=\mathcal{A} \cup(\hat{\mathcal{L}}[i] \rightarrow C)\);
    end
    for \(i=k+1 \rightarrow n\) do
        \(\mathcal{N}=\mathcal{N} \cup \hat{\mathcal{L}}[i]\);
        \(\mathcal{A}=\mathcal{A} \cup(C \rightarrow \hat{\mathcal{L}}[i])\);
        \(S=\varnothing\);
        \(\hat{k}=k\);
        while ( \(\hat{k}>0\) ) do
            \(m=\arg \max _{j}\{I(\hat{\mathcal{L}}[i] ; \hat{\mathcal{L}}[j] \mid C): 1 \leq j<i, j \notin S\} ;\)
            \(\hat{k}=\hat{k}-1 ;\)
            \(S=S \cup\{m\} ;\)
            \(\mathcal{A}=\mathcal{A} \cup(\hat{\mathcal{L}}[m] \rightarrow \hat{\mathcal{L}}[i])\);
        end
    end
    return \(B N\)

Since the class label of testing instance $\mathcal{P}$ is unknown, we can get all possible class labels from training set $\mathcal{T}$. Assume that the probability the testing instance $\mathcal{P}$ in class $c$ is $1 / \mathrm{m}$ for each $c \in\left\{c_{1}, \cdots, c_{m}\right\}$, there will be $m$ "pseudo" instances. By adding these $m$ "pseudo" instances to training set $\mathcal{T}$, we can estimate the joint or conditional probabilities between arbitrary attribute value pairs by using Equation (14) to achieve the aim of learning conditional independence from a testing instance $\mathcal{P}$.

The learning procedures of $\mathrm{UKDB}_{\mathcal{P}}$ is shown in Algorithm 2, where "?" is represented the missing value in the dataset. To estimate the marginal and joint probabilities $P(c), P\left(x_{i}, c\right)$ and $P\left(x_{i}, x_{j}, c\right)$, at training time UKDB needs one pass through the training data to collect the base statistics of co-occurrence counts. Calculating MI and CMI respectively need $O(\mathrm{Nmnv})$ and $O\left(\mathrm{Nm}(n v)^{2}\right)$ time, where $N$ is the number of training instances, $m$ is the number of classes, $n$ is the number of attributes and $v$ is the number of values that discrete attributes may take on average. The procedure of parent assignment for each attribute needs $O\left(n^{2} \log n\right)$. Thus, the time complexity for $\mathrm{UKDB}_{\mathcal{T}}$ to build the actual network structure is $O\left(\mathrm{Nm}(n v)^{2}\right)$. Since $\mathrm{UKDB}_{\mathcal{P}}$ only needs to consider the attribute values in the testing instance, calculating LMI and CLMI respectively need $O(\mathrm{Nmn})$ and $O\left(\mathrm{Nmn}^{2}\right)$ time. The procedure of parent assignment for each attribute in $\mathrm{UKDB}_{\mathcal{P}}$ needs the same time, $O\left(n^{2} \log n\right)$. Thus, the time complexity for $\mathrm{UKDB}_{\mathcal{P}}$ is only $O\left(\mathrm{Nmn}^{2}\right)$. $\mathrm{UKDB}_{\mathcal{T}}$ and $\mathrm{UKDB}_{\mathcal{P}}$ use different variations of $P(\mathbf{x}, c)$ to classify each single instance and corresponding time complexities are the same, $O(m n k)$.

```
Algorithm 2: The \(\mathrm{UKDB}_{\mathcal{P}}\) algorithm
    Input: Testing instance \(\mathcal{P}=\left\{x_{1}, \cdots, x_{n}\right\}, k\).
    Output: The \(B N\) of \(\mathrm{UKDB}_{\mathcal{P}}\).
    Let Bayesian network \(B N=\{\mathcal{N}, \mathcal{A}\}\), where \(\mathcal{N}\) denotes the node set and \(\mathcal{A}\) the edge set.
    Calculate SCLMI and sort predictive attribute values into list \(\mathcal{L}\) in descending order of SCLMI.
    Calculate LMI and sort predictive attribute values into list \(\overline{\mathcal{L}}\) in descending order of LMI.
    Let \(\overline{\mathcal{L}}=\left\{\mathcal{L}_{1}, \cdots, \mathcal{L}_{k}, \overline{\mathcal{L}}_{1}, \cdots, \overline{\mathcal{L}}_{n-k}\right\}\).
    \(\mathcal{N}=\{C\} ; \mathcal{A}=\varnothing ;\)
    for \(i=1 \rightarrow k\) do
        if \(\left(\overline{\mathcal{L}}[i] \neq^{\prime} ?^{\prime}\right)\) then
            \(\mathcal{N}=\mathcal{N} \cup \overline{\mathcal{L}}[i] ;\)
            \(\mathcal{A}=\mathcal{A} \cup\left(\overline{\mathcal{L}}[i] \rightarrow C\right) ;\)
        end
    end
    for \(i=k+1 \rightarrow n\) do
        if \(\left(\overline{\mathcal{L}}[i] \neq^{\prime} ?^{\prime}\right)\) then
            \(\mathcal{N}=\mathcal{N} \cup \overline{\mathcal{L}}[i] ;\)
            \(\mathcal{A}=\mathcal{A} \cup(C \rightarrow \overline{\mathcal{L}}[i])\);
            \(S=\varnothing ;\)
            \(\bar{k}=k ;\)
            for \(i=k+1 \rightarrow n\) do
                \(m=\arg \max _{j}\left\{I\left(\overline{\mathcal{L}}[i] ; \overline{\mathcal{L}}[j] \mid C\right): 1 \leq j<i, j \notin S\right\} ;\)
                \(\bar{k}=\bar{k}-1 ;\)
                \(S=S \cup\{m\} ;\)
                \(\mathcal{A}=\mathcal{A} \cup\left(\overline{\mathcal{L}}[m] \rightarrow \overline{\mathcal{L}}[i]\right) ;\)
            end
        end
    end
    return \(B N\)

$\mathrm{UKDB}_{\mathcal{T}}$ learned from training data $\mathcal{T}$ describes the general conditional dependencies, thus $\mathrm{UKDB}_{\mathcal{T}}$ corresponds to the domain knowledge that may be suitable for most cases. In contrast, $\mathrm{UKDB}_{\mathcal{P}}$ learned from testing instance $\mathcal{P}$ describes local conditional dependencies with uncertainty because all class labels are considered, thus $\mathrm{UKDB}_{\mathcal{P}}$ corresponds to the personalized knowledge that may be suitable for $\mathcal{P}$ only [16].

When facing an expected case, it is difficult to judge which kind of knowledge should be considered in priority. Precision knowledge may provide some statistical information that the expert does not recognize and help him use the domain knowledge to confirm or rule out the decision. For different cases, the weights of $\mathrm{UKDB}_{\mathcal{P}}$ and $\mathrm{UKDB}_{\mathcal{T}}$ may differ greatly. In this paper, without any prior knowledge we simply use the uniformly weighted average instead of the nonuniformly weighted one. The final probability estimate for the ensemble of $\mathrm{UKDB}_{\mathcal{T}}$ and $\mathrm{UKDB}_{\mathcal{P}}$ is,

$$
\hat{P}(c \mid \mathbf{x})=\frac{P\left(c \mid \mathbf{x}, \mathrm{UKDB}_{\mathcal{T}}\right)+P\left(c \mid \mathbf{x}, \mathrm{UKDB}_{\mathcal{P}}\right)}{2}
$$

# 4. Results and Discussion 

### 4.1. Data

Breast cancer is the leading life-threatening cancer for women, especially for those aged between 40 and 55 in US and Europe [26]. American Cancer Society (ACS) estimated that [27], in 2017 about 252,000 women were diagnosed with invasive breast cancer and over 60,000 with noninvasive breast cancer. Sometimes it is too late for those women to be treated since no obvious symptoms appear before the diagnosis and among them about $12.8 \%$ will die of breast cancer after diagnosis [27]. Thus, there is strong demand for improved classification/detection systems in medical science community.

Dr William H. Wolberg collected data relevant to breast cancer during his stay at the University of Wisconsin-Madison Hospitals from 1989 to 1991, and provided the data to the UCI repository of machine learning [17]. This WBC database is relatively small, containing only 699 instances of breast cancer. In this database, $458(65.5 \%)$ instances are benign and $241(34.5 \%)$ instances are malignant. Each instance has 10 predictive attributes and the detailed introduction of the 10 attributes is shown in Table 3. Please note that some instances have missing values. In addition, attribute "Sample code number" is not considered in experimental study because it represents the id number and is not helpful for classification.

Table 3. Attributes in WBC database.


In the last decade, larger datasets are not scarce resources anymore [28-30]. Larger data quantities can help make the estimation of conditional probabilities more accurate. BNCs need higher-degree representation of attribute dependence and more accurate estimation of probability distribution to deal with them. Ten large datasets (size $>3000$ ) with different number of attributes $(n \geq 10)$ are selected

from the UCI repository of machine learning [17] for experimental study. Table 4 describes the details of each dataset, including the number of instances, attributes and classes.

Table 4. Datasets.


# 4.2. Evaluation Function 

In machine learning, zero-one loss [31] is one of the standard measures for evaluating the classification performance. The bias-variance decomposition [32] for zero-one loss can help analyze the expected generalization error of trained models. To achieve bias-variance trade-off is a key issue in supervised learning. Zero-one loss can measure the extent to which a classifier correctly identifies the class label of an unlabeled instance. Given $M$ testing instances, the zero-one loss function can be calculated as follows:

$$
\xi(c, \hat{c})=\frac{\sum_{i=1}^{M}\left\{1-\delta\left(c_{i}, \hat{c}_{i}\right)\right\}}{M}
$$

where $c_{i}$ and $\hat{c}_{i}$ are respectively the true class label and predicted label of the $i$-th instance, besides $\delta\left(c_{i}, \hat{c}_{i}\right)=1$ if $c_{i}=\widehat{c_{i}}$ and 0 otherwise. While dealing with highly imbalanced datasets where "positive" class has very low proportion as compared to the "negative" class, $F 1$ score can help to judge whether the classifier tends to be biased towards the majority class or not. The $F 1$ score is defined as follows,

$$
F 1=\frac{2 T P}{2 T P+F P+F N}
$$

where $T P$ is equal to the number of positive instances that have been classified correctly, $F P$ and $F N$ are equal to the numbers of positive instances that have been misclassified and the numbers of negative instances that have been misclassified.

We also has been introduced the ROC (Receiver Operating Characteristics) cure [33,34] to evaluate performance of machine-learning algorithms. The ROC curve is created by plotting the true-positive rate (TPR) against the false-positive rate (FPR) at various threshold settings. The TPR is also known as sensitivity or recall in machine learning. The FPR is also known as the fall-out or probability of false alarm and can be calculated as ( 1 - specificity), where specificity is the true negative rate (TNR). All formula involved are defined as follows:

$$
\begin{gathered}
T P R=\frac{T P}{T P+F N} \\
T N R=\frac{T N}{T N+F P} \\
F P R=\frac{F P}{F P+T N}=1-T N R
\end{gathered}
$$

We compared the proposed algorithm when $k=1,2$ with several benchmark classifiers [12,13,23] that were presented in the literature. The statistical results of all evaluated functions using 20 rounds of 10 -fold cross validation are shown in Table 5. For each fold, $9 / 10$ of the data was used for training and $1 / 10$ of the data was used for testing. In addition, all experiments have been conducted on a desktop computer with an Intel(R) Xeon(R) CPU X5680 @ $3.33 \mathrm{GHz}, 64$ bits and 8192 MiB of memory. In addition, for training data, missing values for qualitative attributes are replaced with modes and those for quantitative attributes are replaced with means from the training data [35-37]. In addition, for testing data, $\mathrm{UKDB}_{P}$ proposes a natural way for dealing with missing values, not considering the dependence relationships related to missing values. The negative effect caused by missing values for $\mathrm{UKDB}_{P}$ can be mitigated by removing noisy dependence relationships, and the learned network structure may be more robust.

Sampling is one of the main methods used for handling the problem of imbalanced dataset, which follows two different approaches: undersampling and oversampling [38-40]. Undersampling methods aim to decrease the size of the majority class. On the contrary to undersampling, oversampling algorithms tend to balance class distributions through the increase of the minority class. Since undersampling may cause the classifier to miss important concepts pertaining to the majority class, we conduct all experiments with oversampling. In the preprocessing stages of datasets, we add a set of randomly selected minority instances in the set of minority class instances and augment the original set by replicating the selected instances and adding them to it. In this way, the number of total instances in the set of minority class instances is increased and the class distribution balance is adjusted accordingly.

We also employ the Win/Draw/Loss records to summary the experimental results. Cell $[i, j]$ in each table contains the number of datasets for which the BNC on the $i$ th-row performs better (Win), equally well (Draw) or worse (Loss) than the other on the $j$ th-column. In the following experiments, we assess a difference as significant if the outcome of a one-tailed binomial sign test is less than 0.05 .

Table 5. Comparison of various algorithms from literature based on the WBC dataset.


# 4.3. Experimental Study on WBC Dataset 

From Table 5 we can see that except NB, UKDB $(k=1)$ has a remarkably obvious prediction superiority compared to the other algorithms in terms of zero-one loss and UKDB $(k=2)$ achieves slightly improved $F 1$ score than other algorithms. Although NB achieves lower errors than other algorithms on WBC, it is just a special case. As Sahami [13] argued that there would be expected to achieve optimal Bayesian accuracy if more "right" dependencies are captured. In most cases, BNCs with simple structure perform worse than those with complex structure. We will further demonstrate it in the Section 4.4.3.
$\mathrm{UKDB}_{T}$, which is learned from all training instances, can describe the general conditional dependence relationships. However, it is not all the dependence relationships but only some of them that may hold for a certain instance. In contrast, $\mathrm{UKDB}_{P}$ can encode the most possible local conditional dependencies implicated in one single testing instance. UKDB can use the knowledge learned from the training set and testing instances by applying the aggregating mechanism. If $\mathrm{UKDB}_{T}$ and $\mathrm{UKDB}_{P}$ are complementary to each other for classification, an ideal phenomenon is that they focus

on different key points. To prove this, we take an instance from WBC dataset for case study, and the detail of the instance is shown as follows,

$$
\mathcal{P}=\left\{x_{1}=9, x_{2}=5, x_{3}=8, x_{4}=1, x_{5}=2, x_{6}=3, x_{7}=2, x_{8}=1, x_{9}=5\right\}
$$

By comparing MI $I\left(X_{i} ; C\right), \tilde{X}=\left\{X_{2}, X_{3}, X_{6}\right\}$ are the first three key attributes for $\mathrm{UKDB}_{\mathcal{T}}$. Whereas by comparing $I\left(x_{i} ; C\right), \tilde{X}=\left\{X_{4}, X_{5}, X_{8}\right\}$ are the first three for $\mathrm{UKDB}_{\mathcal{P}}$. The marginal probabilities of each attribute value in $\mathcal{P}$ are shown in Table 6. From Table 6, for any attribute value $x_{i}\left(X_{i} \in \tilde{X}\right)$ and $x_{j}\left(X_{j} \in \tilde{X}\right), P\left(x_{i}\right)>P\left(x_{j}\right)$ always holds. Then for attribute $X_{k}$, it is more possible that $P\left(x_{k} \mid x_{i}, c\right)>$ $P\left(x_{k} \mid x_{j}, c\right)(k \neq i$ and $k \neq j)$. To maximize the joint probability $P(\mathbf{x}, c)$, as (10) suggests, an ideal condition is that each underlying conditional probability will be maximized. Obviously, $\mathrm{UKDB}_{\mathcal{P}}$ can achieve a much more reasonable attribute order.

Table 6. Attribute values in $\mathcal{P}$ and corresponding marginal probabilities.


Generally, as Figure 7 shows, dependency types in BNCs can be divided into two types: one is the direct dependence relationship (indicated in the Figure 7a by the solid line), such as the relationships between variables $U$ and $V$; another is the conditional dependence relationship (indicated in the Figure 7b by the dotted line), such as the relationships between variables $V$ and $W$ given $U$. To interpret the effect of dependency types to UKDB, a simulation study has been carried out on dataset WBC.
![img-6.jpeg](img-6.jpeg)

Figure 7. The dependency types in BNCs.
Figures 8 and 9 respectively show the network structures of $\mathrm{UKDB}_{\mathcal{T}}$ and $\mathrm{UKDB}_{\mathcal{P}}$ on dataset WBC when $k=1$, where $\mathrm{UKDB}_{\mathcal{P}}$ is based on testing instance $\mathcal{P}$. The parent attribute of class variable is annotated in black. We can see clearly the differences in direct and conditional dependencies between them. For $\mathrm{UKDB}_{\mathcal{T}}$, attribute $X_{8}$ and class $C$ have direct dependence relationships with other attributes, and $X_{2}$ is the key attribute that has conditional dependence relationships with almost all the other attributes. In contrast, for $\mathrm{UKDB}_{\mathcal{P}}, X_{3}$ and $C$ have direct dependence relationships with other attributes, and $X_{4}$ plays the main role instead and is the common parent of only 3 out of 8 other attributes. In Figure 10 another structure is presented for the testing instance $\mathcal{P}^{\prime}=\{5,3,3,3,6,10,3,1,1\}$ that is different from the structure obtained for instance $\mathcal{P}=\{9,5,8,1,2,3,2,1,5\}$. These examples illustrate the personalized structure (e.g., Figure 9) generated from our targeted learning for given testing instance are discriminative not only with the domain structure (e.g., Figure 8) but also other personalized structure (e.g., Figure 10) learned from other testing instance. In the next section, we will prove that the ensemble of these discriminative BNCs can use the knowledge learned from the training set and testing instances to achieve better classification performance.

![img-7.jpeg](img-7.jpeg)

Figure 8. The network structure of $\mathrm{UKDB}_{T}$ corresponding to breast cancer dataset.
![img-8.jpeg](img-8.jpeg)

Figure 9. The network structure of $\mathrm{UKDB}_{\mathcal{P}}$ corresponding to testing instance $\mathcal{P}={9,5,8,1,2,3,2,1,5}$ in breast cancer dataset.
![img-9.jpeg](img-9.jpeg)

Figure 10. The network structure of $\mathrm{UKDB}_{\mathcal{P}}$ corresponding to testing instance $\mathcal{P}^{\prime}={5,3,3,3,6,10,3,1,1}$ in breast cancer dataset.

# 4.4. Further Experiments on Other Datasets 

### 4.4.1. The Effect of Values of $k$

We firstly compared the classification performance of KDB and UKDB with the same values of $k$. Since the restrictions of currently available hardware place some requirements on the software and the complexity of the probability table increases exponentially as $k$ increases, to achieve the trade-off between classification performance and efficiency, we respectively compared KDB and UKDB with $k=1$ and $k=2$ on 10 datasets (described in Table 4). The detailed results in terms of zero-one loss can be found in Table A1 in Appendix A.

As shown in Table 7, for UKDB, the model with $k=2$ achieves significant advantages over the one with $k=1$ and results in Win/Draw/Loss of $6 / 2 / 2$. In addition, there are only two datasets, i.e., Dis and Mushroom, have larger results of zero-one loss with UKDB, which indicates that UKDB $(k=2)$ seldom performs worse than UKDB $(k=1)$. In addition, for many datasets, UKDB $(k=2)$ substantially improved the classification performance of UKDB $(k=1)$, for example, the decrease from 0.0644 to 0.0414 for the datasets Adult.

Table 7. Win/Draw/Loss comparison results of UKDB $(k=1)$ and UKDB $(k=2)$ in terms of zero-one loss.


# 4.4.2. The Effect of Missing Values 

As mentioned above, for training data, missing values for qualitative attributes are replaced with modes and those for quantitative attributes are replaced with means from the training data [35-37]. In addition, for testing data, UKDB $_{P}$ proposes a natural way for dealing with missing values, not considering the dependence relationships related to missing values. The negative effect caused by missing values for $\mathrm{UKDB}_{P}$ can be mitigated by removing noisy dependence relationships, and the learned network structure may be more robust.

In this section, to prove that UKDB has the ability to mitigate the negative effect caused by missing values in testing instance, we also present a simulation experiment to investigate the effect of missing values to UDKB. We choose datasets with no missing values from Table 4. In addition, there are three datasets satisfying this conditions, i.e., Chess, Magic and Spambase. To compare the algorithm on a controlled situation, when classifying testing instances, we manually and randomly delete $5 \%$ of attribute values in each instance.

Table 8 shows the detailed results of UKDB $(k=2)$ on two sets of data with and without missing values in terms of zero-one loss. As can be seen, although some attribute values of testing instances have been deleted, the results of zero-one loss on these 3 datasets are similar to the one without missing values (we assess a difference as significant if the outcome of a one-tailed binomial sign test is less than 0.05), i.e., UKDB has the ability to mitigate the negative effect caused by missing values in testing instance.

Table 8. Detailed results of UKDB $(k=2)$ on two sets of data with and without missing values in terms of zero-one loss.


4.4.3. The Effect of Criterion Used to Measure the Strength of the Dependence between the Variables

Our proposed algorithm, UKDB, is using MI and CMI (or LMI and CLMI) to measure the strength of the dependence between attributes. Actually, UKDB could use others. Since the efficiency of the UKDB depends on the efficiency of MI and CMI, we use another criterion, pointwise mutual information (PMI) and pointwise conditional mutual information (PCMI) to compare and to show in which situations MI and CMI is more (or less) efficient. In contrast to MI and CMI, PMI and PCMI refer to single events, whereas MI and CMI refer to the average of all possible events [41].

In computational linguistics, PMI and PCMI have been used for finding collocations and associations between words [41]. They can be calculated as follows:

$$
\begin{aligned}
\operatorname{PMI}(x ; c) & =\log \frac{P(x, c)}{P(x) P(c)} \\
\operatorname{PCMI}\left(x_{i} ; x_{j} \mid c\right) & =\log \frac{P\left(x_{i}, x_{j} \mid c\right)}{P\left(x_{i} \mid c\right) P\left(x_{j} \mid c\right)}
\end{aligned}
$$

Table 9 shows the Win/Draw/Loss comparison results of UKDB $(k=2)$ with $\{\mathrm{MI}, \mathrm{CMI}\}$ and $\{\mathrm{PMI}, \mathrm{PCMI}\}$. The corresponding detailed results can be found in Table A2 in Appendix A. As can be seen, UKDB $(k=2)$ with $\{\mathrm{MI}, \mathrm{CMI}\}$ achieves lower error more often than the one with $\{\mathrm{PMI}, \mathrm{PCMI}\}$. To identify the efficiency between UKDB $(k=2)$ with different information-based criteria to measure the dependence relationships between attributes, we present the results of average running computational time for UKDB $(k=2)$ with $\{\mathrm{MI}, \mathrm{CMI}\}$ and $\{\mathrm{PMI}, \mathrm{PCMI}\}$ in Table 10. The results in Table 10 reinforce what the orders of complexity for these two algorithms indicated, i.e., UKDB $(k=2)$ with $\{\mathrm{MI}, \mathrm{CMI}\}$ needs more time to build model than the one with $\{\mathrm{PMI}, \mathrm{PCMI}\}$ on most datasets. For example, on dataset Census-Income, the running computational time of UKDB with $\{\mathrm{PMI}, \mathrm{PCMI}\}$ is almost 1.84 times faster than the one with $\{\mathrm{MI}, \mathrm{CMI}\}$ (as highlighted in bold in the table). Thus, although UKDB with $\{\mathrm{PMI}, \mathrm{PCMI}\}$ is more efficient than the one with $\{\mathrm{MI}, \mathrm{CMI}\}$ in terms of average running computational time, UKDB with $\{\mathrm{MI}, \mathrm{CMI}\}$ has better classification performance in terms of zero-one loss at the cost of increasing less computational time.

Table 9. Win/Draw/Loss comparison results of UKDB $(k=2)$ with $\{\mathrm{MI}, \mathrm{CMI}\}$ and $\{\mathrm{PMI}, \mathrm{PCMI}\}$.


Table 10. The average results of running computational time for UKDB $(k=2)$ with $\{\mathrm{MI}, \mathrm{CMI}\}$ and $\{\mathrm{PMI}, \mathrm{PCMI}\}$.


# 4.4.4. UKDB vs. NB, TAN and KDB 

Although NB ranked the highest among all algorithms on WBC database in terms of zero-one loss and F1, the conditional independence assumption of NB is not true in most cases, furthermore, many researchers found that general algorithm performs better than NB in most cases [12,13,18-20]. Thus, it is necessary to have more general algorithm even if NB works the best in some cases.

In this section, we will demonstrate that the advantages of UKDB are due to its flexible high-dependence representation when dealing with large datasets. Since UKDB with $k=2$ achieves lower results of zero-one loss more often than the one with $k=1$, we compare UKDB $(k=2)$ with

other lower-dependence BNCs, i.e., NB (0-dependence) and TAN (1-dependence). The experimental results of KDB (2-dependence when $k=2$ ) are also shown for object reference. The derailed results of the average zero-one loss, bias and variance on 10 datasets (described in Table 4) are presented in Appendix A, respectively.

Table 11 shows the corresponding Win/Draw/Loss comparison results of different BNCs.
The results of zero-one loss in Table 11 reveal some patterns that confirm the hypothesis proposed above. As can be seen, TAN performs better than NB on 8 datasets and never worse. KDB performs better than TAN on 5 datasets and never worse. UKDB performs the best among all classifiers. It proved that the superior classification performance of NB on dataset WBC is just a special case. NB, TAN, KDB and UKDB can represent different degrees of dependence relationship. In general, as structure complexity increases, higher-dependence BNCs enjoy significant advantage in classification over lower-dependence BNCs on most cases.

From Table 11, in terms of bias, TAN still performs better than NB, and KDB performs better than TAN. However, the advantage of UKDB over KDB is not so significant. Higher-dependence BNCs can represent more conditional dependencies, which in general help these models to approximate the correct value of conditional probability $P\left(x_{i} \mid \Pi_{i}, c\right)$. From Table 11, in terms of variance, NB achieves the lowest variance because there exists no structure learning for it and its structure remains the same regardless of the change of training data. TAN performs better than KDB on 5 datasets and worse on 3 datasets. UKDB performs better than TAN on 5 datasets and worse on 3 datasets, and it performs better than KDB on 7 datasets and worse on 2 datasets. This also emphasizes that the robustness of UKDB is only second to NB. UKDB enjoys significant advantage over TAN and KDB in terms of bias and variance. Simple network structure may result in underfitting whereas complex one may result in overfitting. It is very difficult for a BNC to achieve the trade-off between structure complexity and classification performance. However, mining the possible dependence relationships implicated in testing instance helps to alleviate the negative effect caused by overfitting while improving the classification accuracy.

Table 11. The Win/Draw/Loss comparison results of different BNCs in terms of zero-one loss, Bias and Variance.


To attest the effective superiority of the UKDB, we use the Friedman test [42] for comparison of all alternative algorithms on other 10 datasets in Table 4. The null hypothesis of the Friedman test is that there is no difference in average ranks. With 4 algorithms and 10 datasets, the Friedman test is distributed according to the $F$ distribution with $4-1=3$ and $(4-1) \times(10-1)=27$ degrees of freedom. The critical value of $F(3,27)$ for $\alpha=0.05$ is 2.9603 . The result of Friedman test for zero-one loss is $22.25>2.9603$ with $p<0.001$. Hence, we reject the null hypothesis. That is to say, the seven algorithms are not equivalent in terms of zero-one loss results. The average ranks of zero-one loss of different classifiers are $\{$ NB(3.8000), TAN(2.8000), KDB(2.2000), UKDB(1.2000) $\}$, and the minimum

required difference of mean rank is 0.6701 , i.e., the rank of UKDB is better than that of other algorithms, followed by KDB, TAN and NB. UKDB has significant statistical difference with NB, TAN and KDB.

The ROC cures for NB, TAN, KDB $(k=2)$ and UKDB $(k=2)$ on 10 datasets are presented in Figure 11, respectively. The X-axis represents ( 1 - specificity) and Y-axis represents sensitivity. The area under the curve (AUC) is an effective and combined measure of sensitivity and specificity for assessing inherent validity of a diagnostic test [33]. The value of AUC closer to 1 indicates better performance of the test. According to the values of AUC, UKDB performs lower results more often than other algorithms, especially on datasets Adult, Chess, Magic, Musk and Sick. Compared with KDB, UKDB achieves similar values of AUC on 4 datasets (Dis, Hypothyroid, Mushroom and Spambase), i.e., UKDB also has significant advantages with NB, TAN and KDB in terms of ROC cures.
![img-10.jpeg](img-10.jpeg)

Figure 11. The ROC cures for NB, TAN, KDB $(k=2)$ and UKDB $(k=2)$ on 10 datasets.

To further demonstrate the performance of UKDB over KDB, we employ the goal difference (GD) [19,21]. Suppose there are two classifiers $A$ and $B$, the value of $G D$ can be computed as follow:

$$
G D(A ; B \mid \mathcal{T})=|\operatorname{win}|-|\operatorname{loss}|
$$

where $\mathcal{T}$ is the datasets, $|\operatorname{win}|$ and $|\operatorname{loss}|$ represent the number of datasets on which $A$ performs better or worse than $B$, respectively.

Figure 12 shows the fitting curve of $G D\left(\right.$ UKDB;KDB $\left.\mid \mathcal{S}_{t}\right)$ in terms of 0-1 loss. The X-axis shows the indexes of different datasets, referred to as $t$, which correspond to that described in Table 4. In addition, the Y-axis corresponds to the value of $G D\left(\right.$ UKDB;KDB $\left.\mid \mathcal{S}_{t}\right)$, where $\mathcal{S}_{t}=\left\{D_{m} \mid m \leq t\right\}$ and $D_{m}$ is the dataset with index $m$. As can be seen, UKDB enjoys significant advantages over KDB in terms of 0-1 loss when the number of instances $\leq 4000$ ( 3 wins and 1 draw) or $>10,000$ ( 3 wins), otherwise the advantage is not significant ( 2 draws and 1 loss).

Figure 13 shows the fitting curve of $G D\left(\right.$ UKDB;KDB $\left.\mid \mathcal{S}_{n}\right)$ in terms of 0-1 loss. The X-axis shows the number of attributes for different datasets, referred to as $n$, which correspond to that described in Table 4. In addition, the Y-axis corresponds to the value of $G D\left(\right.$ UKDB;KDB $\left.\mid \mathcal{S}_{n}\right)$, where $\mathcal{S}_{n}=\left\{D_{n^{\prime}} \mid n^{\prime} \leq n\right\}$ and $D_{n^{\prime}}$ is the dataset with $n^{\prime}$ attributes. We can see that when the number of attributes $>22$, the advantage of UKDB over KDB is significant in terms of 0-1 loss ( 4 wins and 3 draws), otherwise the advantage is not significant ( 2 wins and 1 loss).
![img-11.jpeg](img-11.jpeg)

Figure 12. The fitting curve of $G D\left(\right.$ UKDB;KDB $\left.\mid \mathcal{S}_{t}\right)$ in terms of 0-1 loss.
![img-12.jpeg](img-12.jpeg)

Figure 13. The fitting curve of $G D\left(\right.$ UKDB;KDB $\left.\mid \mathcal{S}_{n}\right)$ in terms of 0-1 loss.

# 4.4.5. UKDB vs. Target Learning 

Target learning [16] is a framework that takes each unlabeled testing instance $\mathcal{P}$ as a target and builds a specific Bayesian model $\mathrm{BNC}_{\mathcal{P}}$ to complement $\mathrm{BNC}_{\mathcal{T}}$ learned from training data $\mathcal{T}$. It respectively uses TAN and KDB as the base classifier to clarify the superiority of target learning (which referred to as $\mathrm{TAN}^{e}$ and $\mathrm{KDB}^{e}$ ).

We have conducted experiments with $\mathrm{TAN}^{e}$ and $\mathrm{KDB}^{e}(k=2)$ on 10 datasets (described in Table 4). The detailed zero-one loss results of all alternative algorithms are presented in Table A6 in Appendix A.

Table 12 shows the Win/Draw/Loss comparison results of $\mathrm{TAN}^{c}, \mathrm{KDB}^{c}$ and $\operatorname{UKDB}(k=2)$ in terms of zero-one loss. As can be seen, UKDB achieves lower values of zero-one loss more often than $\mathrm{TAN}^{c}$ and $\mathrm{KDB}^{c}$, for example, the decrease from $0.4821 \pm 0.0037\left(\mathrm{TAN}^{c}\right)$ or $0.4781 \pm 0.0039\left(\mathrm{KDB}^{c}\right)$ to $0.1537 \pm 0.0045$ (UKDB) for the dataset Abalone.

Table 12. Win/Draw/Loss comparison results of $\mathrm{TAN}^{c}, \mathrm{KDB}^{c}$ and $\operatorname{UKDB}(k=2)$ in terms of zero-one loss.


The Friedman test was also performed for these three algorithms on 10 datasets. The final result is $5.6862>F(2,18)=3.5546$ with $p<0.001$. This means that at $\alpha=0.05$, there is evidence to reject the null hypothesis that all algorithms are equivalent. The average ranks of zero-one loss of these three algorithms are $\left\{\mathrm{TAN}^{c}(2.4500), \mathrm{KDB}^{c}(2.2500), \mathrm{UKDB}(1.3000)\right\}$, and the minimum required difference of mean rank is 0.7655 , which demonstrates that UKDB has significant statistical difference with $\mathrm{TAN}^{c}$ and $\mathrm{KDB}^{c}$.

# 4.4.6. UKDB vs. ETAN 

Cassio P. de Campos et al. [43] proposed an extended version of the TAN, ETAN, which also does not require attributes to be connected to the class. Based on a modification of Edmonds' algorithm, its structure learning procedure explores a superset of the structures that are considered by TAN, yet achieves global optimality of the learning score function in a very efficient way.

Since it shares similarities with UKDB $(k=1)$, we have conducted experiments with ETAN on 10 datasets (described in Table 4). The detailed zero-one loss results can be found in Table A7 in Appendix A. The Win/Draw/Loss comparison results are presented in Table 13. As can be seen, UKDB obtains lower error than ETAN more often than the reverse. Although ETAN is an efficient algorithm and has similar unrestricted Bayesian network structure with UKDB $(k=1)$, it is a single model. On the contrary, UKDB is an ensemble algorithm.

Table 13. Win/Draw/Loss comparison results of ETAN, UKDB $(k=1)$ and UKDB $(k=2)$ in terms of zero-one loss.


The corresponding results of Friedman test for these three algorithms on 10 datasets is $4.0435>F(2,18)=3.5546$ with $p<0.001$. The corresponding average ranks in terms of zero-one loss are $\{\operatorname{ETAN}(2.5000), \operatorname{UKDB}(k=1)(2.1000), \operatorname{UKDB}(k=2)(1.3000)\}$, and the minimum required difference of mean rank is 0.8227 , which demonstrates that the rank of $\operatorname{UKDB}(k=2)$ is better than that of other algorithms, followed by $\operatorname{UKDB}(k=1)$ and ETAN. UKDB $(k=2)$ has significant statistical difference with ETAN.

# 5. Conclusions 

In this paper, we have proposed to extend KDB from restricted BNC to unrestricted one by applying Markov blanket. The final classifier, called UKDB, demonstrates better classification performance with high expressivity, enhanced robustness and tight coupling. For each testing instance $\mathcal{P}$, an appropriate local Bayesian classifier $\mathrm{UKDB}_{\mathcal{P}}$ is built using the same learning strategy as that of $\mathrm{UKDB}_{\mathcal{T}}$ learned from training data $\mathcal{T}$. Compared with other state-of-the-art BNCs, the novelty of UKDB is that it can use the information mined from labeled and unlabeled data to make joint decisions. From the case study we can see that given testing instances $\mathcal{P}_{1}$ and $\mathcal{P}_{2}$, the weights of dependence relationships between the same pair of attribute values may differ that makes the topology of $\mathrm{UKDB}_{\mathcal{P}_{1}}$ distinguish from that of $\mathrm{UKDB}_{\mathcal{P}_{2}}$. Besides, the model is learned directly from the data in some field, and it can only express part of domain knowledge, i.e., datasets are only part of the field, and the knowledge of statistics may be contrary to expert knowledge. Some of the mined knowledge does not conform to the knowledge of medical experts, which requires the discrimination of expert knowledge. Thus, if given expertise in medicine, the network structures of $\mathrm{UKDB}_{\mathcal{P}}$ and $\mathrm{UKDB}_{\mathcal{T}}$ will be improved.

Given a limited number of instances, the accuracy of probability estimation determines the robustness of dependence relationships, and then determines the structure complexity of BNCs. The characteristic of tight coupling helps UKDB improve the probability estimation. UKDB has been compared experimentally with some state-of-the-art BNCs with different structure complexities. Although KDB and UKDB are of the same structure complexity, UKDB presents superior advantage over KDB in terms of classification accuracy (zero-one loss) and robustness (bias and variance). The independence assumption of NB rarely holds for all instances but may hold for specific instance. However, high-dependence BNCs, e.g., TAN, KDB and UKDB focus on the interdependence between attributes but disregard the independence between attribute values. If the independence in testing instance can be measured and identified, $\mathrm{UKDB}_{\mathcal{P}}$ can provide a much more competitive representation.

Target learning is related to dependence evaluation when attributes take specific values. Because the proposed $\mathrm{UKDB}_{\mathcal{P}}$ is based on UKDB, it needs enough data to learn accurate conditional probability during structure learning. Thus, in practical applications, the inaccurate estimate of conditional probability for some attribute values, e.g., $P\left(x_{i} \mid \Pi_{i} c\right)$, may lead to noise propagation in the estimate of joint probability $P(c, \mathbf{x})$. This situation is more obvious while dealing with datasets with less attributes. Therefore, our further research is to decide the appropriate estimate of conditional probability needed for this purpose and to seek alternative methods, e.g., Laplace correction.

Author Contributions: All authors have contributed to the study and preparation of the article. All authors have read and approved the final manuscript.
Funding: This work was supported by the National Science Foundation of China (Grant No. 61272209 and No. 61872164).
Conflicts of Interest: The authors declare no conflict of interest.

## Appendix A

Table A1 shows the detailed results of zero-one loss for $\operatorname{KDB}(k=1), \operatorname{KDB}(k=2), \operatorname{UKDB}(k=1)$ and $\operatorname{UKDB}(k=2)$ on 10 datasets (described in Table 4). Table A2 shows the detailed results of zero-one loss for UKDB $(k=2)$ with $\{\mathrm{MI}, \mathrm{CMI}\}$ and $\{\mathrm{PMI}, \mathrm{PCMI}\}$ on 10 datasets (described in Table 4). Tables A3-A5 show the detailed experimental results of average zero-one loss, bias and variance for NB, TAN, KDB and UKDB $(k=2)$ on 10 datasets (described in Table 4), respectively. Table A6 shows the detailed zero-one loss results of $\mathrm{TAN}^{e}, \mathrm{KDB}^{e}$ and UKDB. In addition, Table A7 shows the detailed zero-one loss results of ETAN, UKDB $(k=1)$ and UKDB $(k=2)$.

Table A1. Detailed zero-one loss results of $\operatorname{KDB}(k=1), \operatorname{KDB}(k=2), \operatorname{UKDB}(k=1)$ and UKDB $(k=2)$. The lowest results from all these BNCs are highlighted in bold.


Table A2. Detailed zero-one loss results of UKDB $(k=2)$ with $\{\mathrm{MI}, \mathrm{CMI}\}$ and $\{\mathrm{PMI}, \mathrm{PCMI}\}$. The lowest results from all these BNCs are highlighted in bold.


Table A3. Experimental results of average zero-one loss for 10-cross validation. The lowest results from all these BNCs are highlighted in bold.


Table A4. Experimental results of average bias for 10-cross validation. The lowest results from all these BNCs are highlighted in bold.


Table A5. Experimental results of average variance for 10-cross validation. The lowest results from all these BNCs are highlighted in bold.


Table A6. Detailed zero-one loss results of $\mathrm{TAN}^{p}, \mathrm{KDB}^{p}(k=2)$ and $\operatorname{UKDB}(k=2)$. The lowest results from all these BNCs are highlighted in bold.


Table A7. Detailed zero-one loss results of ETAN, UKDB $(k=1)$ and UKDB $(k=2)$. The lowest results from all these BNCs are highlighted in bold.

