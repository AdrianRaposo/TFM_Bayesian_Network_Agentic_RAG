# HAL open science 

## Identifying product failure rate based on a conditional Bayesian network classifier

Zhiqiang Cai, Shudong Sun, Shubin Si, Bernard Yannou

## To cite this version:

Zhiqiang Cai, Shudong Sun, Shubin Si, Bernard Yannou. Identifying product failure rate based on a conditional Bayesian network classifier. Expert Systems with Applications, 2011, 38 (5), pp.5036-5043. 10.1016/j.eswa.2010.09.146 . hal-00748716

## HAL Id: hal-00748716 <br> https://hal.science/hal-00748716v1

Submitted on 25 Mar 2013

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# Identifying product failure rate based on a conditional Bayesian network classifier 

Zhiqiang Cai ${ }^{\text {a, }}$, Shudong Sun ${ }^{\text {a }}$, Shubin $\mathrm{Si}^{\text {a }}$, Bernard Yannou ${ }^{\text {b }}$<br>${ }^{a}$ Ministry of Education, Key Laboratory of Contemporary Design and Integrated Manufacturing Technology, School of Mechantronics, Northwestern Polytechnical University, Xi'an 710072, China<br>${ }^{\mathrm{b}}$ Laboratoire Genie Industriel, Ecole Centrale Paris, Chatenay-Malabry 92290, France

## A R T I C L E I N F O

Keywords:
Maintenance management
Failure rate
Classifier
Bayesian network
Conditional independence

## A B S T R A C T

To identify the product failure rate grade under diverse configuration and operation conditions, a new conditional Bayesian networks (CBN) model is brought forward. By indicating the conditional independence relationship between attribute variables given the target variable, this model could provide an effective approach to classify the grade of failure rate. Furthermore, on the basis of the CBN model, the procedure of building product failure rate grade classifier is elaborated with modeling and application. At last, a case study is carried out and the results show that, with comparison to other Bayesian networks classifiers and traditional decision tree C4,5, the CBN model not only increases the total classification accuracy, but also reduces the complexity of network structure.
(c) 2010 Elsevier Ltd. All rights reserved.

## 1. Introduction

In recent years, maintenance has been playing a more and more important role in industrial fields due to the high demand for system safety, operational efficiency and life cycle cost control. In China, we cooperated with some aircraft corporations to develop a maintenance management system for years. This maintenance system daily collects bulky failure data during the airplane operation which is in different formats. The challenge faced currently is how to discover the potential failure knowledge from these data for prediction and decision making.

Data mining, which is also referred to as knowledge discovery, means the process of extracting nontrivial, implicit, previously unknown and potentially useful information from databases (Witten \& Frank, 2005). Depending on the types of knowledge derived, mining approaches may be classified as association rules mining, clustering, classification, prediction and others. In the area of product failure data mining, it has been used widely for the purpose of failure prediction, failure classification, and failure association. Al-Garni, Jamal, Ahmad, Al-Garni, and Tozan (2006) developed an artificial neural network (ANN) model for predicting the failure rate of De Havilland Dash-8 airplane tires utilizing the two layer feed-forward back-propagation algorithm. Using 6 years of data, the results show that the failure rate predicted by the ANN is closer to the actual data than the failure rate predicted by the Weibull regression model. Chen, Tseng, and Wang (2005) defined the

[^0]root-cause machine set identification problem of analyzing correlations between combinations of machines and the defective products and then proposed the Root-cause Machine Identifier (RMI) method using the technique of associating rule mining to solve the problem efficiently and effectively. Han, Kim, and Sohn (2007) applied sequential association rules to extract the failure patterns and forecast failure sequences of Republic of Korea Air Force (ROKAF) aircrafts for various combinations of aircraft types, location, mission and season, which could improve the utilization of aircrafts by properly forecasting the future demand of aircraft spare parts.

Because of the variety of each failure dataset and the diversity of each knowledge discovery mission, researchers have to build proper data mining models and processes according to the characteristic of target dataset and request. In this study, we limit the focus to product failure rate classification. Traditional product failure rate enactment is used to theoretically calculate the system reliability thanks to a static mathematical formula that ignores the actual application of each batch of products. Using the historical product failure data, we could provide a more accurate and effective classification of failure rate according to the configuration and operation. With such results, this model could satisfy the expectations of maintenance scheduling, spare parts supply chain management and product operation optimization.

From recent classification literature, with the characteristics of causality and conditional independence, the Bayesian networks (BN) have been recommended as a comprehensive method of indicating relationships among and influences of variables in system reliability domains (Boudali \& Dugan, 2005; Langseth \& Portinale, 2007; Mahadevan, Zhang, \& Smith, 2001; Muller, Suhner, \& Iung, 2008; Weber \& Jouffe, 2006). It is a powerful technique for handling system uncertainty and it shows a high performance in


[^0]:    * Corresponding author. Tel.: +86 13709247090.

    E-mail addresses: caizhiqiang@nwpu.edu.cn, zhiqiangcai@hotmail.com (Z. Cai), sdsun@nwpu.edu.cn (S. Sun), sisb@nwpu.edu.cn (S. Si), bernard.yannou@ecp.fr (B. Yannou).

prediction and classification tasks. Friedman, Geiger, and Goldszmidt (1997) evaluated approaches for inducing classifiers from data, based on the theory of learning general Bayesian networks (GBN) and put forward a tree augmented Naïve Bayes (TAN) method, which outperforms Naïve Bayes (NB), yet at the same time maintains the computational simplicity and robustness that characterize NB. Cheng and Greiner (1999) learned BN augmented Naïve Bayes (BAN) and GBN using a conditional-independence (CI) based BN learning algorithm and evaluated the algorithms with NB and TAN. Experimental results show that the obtained classifiers are competitive with (or superior to) the other two classifiers. Madden (2002) introduced a new partial Bayesian network (PBN) and describes its constructing algorithm. The algorithm constructs an approximate Markov blanket around a classification node and the results indicate that PBN performs better than other Bayesian network classification structures on some problem domains. Because of the variety of collected data and application domains, researchers also have to focus on the individual case and choose the most effective classifier and modelling process. Baesens et al. (2004) compared and evaluated several Bayesian network classifiers with statistical and artificial intelligence techniques for the purpose of classifying customers in the binary classification problem. The experimental evidence showed that Bayesian network classifiers offer an interesting and viable alternative for customer lifecycle slope estimation problem.

This paper is organized as follows. In Sections 2.1 and 2.2, we discuss the principle of Bayesian networks and common Bayesian network classifiers. To deal with the weakness of present BN classifiers, a new conditional Bayesian network (CBN) classifier and its modeling process are described in Sections 2.3 and 2.4. In Section 3, the case study, the performance criteria and the comparison results are presented. Finally, Section 4 concludes the paper.

## 2. Modeling

### 2.1. Bayesian networks

Bayesian networks are directed acyclic graphs (DAGs) used to represent uncertain knowledge in artificial intelligence (Jensen, 1996). A Bayesian network is defined as a couple: $\mathrm{BN}=(5, \Theta)$, where $S=(N, A)$ represents the network structure.
$\mathbf{N}$ describes the set of all the nodes in a BN. Each node represents a discrete variable having a finite number of mutually exclusive states. In our example, a node may be failure cause, failure mode or other factors.

A is the set of all edges in a BN. Each edge represents the relationship of father and child by linking two nodes. In our example, an edge interprets as a causal relation such as failure cause node affects failure mode node.
$\Theta$ represents the set of probability distributions that are associated with each node. When node is a root node (i.e. it does not have a parent), $\Theta$ corresponds to the prior probability distribution of the node states. When a node is not a root node (i.e. when it has some parent nodes), $\Theta$ corresponds to a conditional probability distribution that quantifies the probabilistic dependency between that node and its parents. It is represented by a conditional probability table (CPT).

Fig. 1 illustrates the nodes, edges and probability distribution through an example. The piston valve has one failure mode which is locked in a closed position. The high temperature and high vibration are two failure causes of valve locked closure, and their joint probability of leading to a locked valve is given by CPT. At last, the closure of valve will result in high gas pressure as a failure effect. From the CPT of high gas pressure, we can see that this node is separated from high temperature and high vibration by the node of valve locked close, which means they are conditionally independent.

Through the complex application of the Bayesian probability theory, Bayesian networks are designed to obtain probabilities of unknown variables from known probabilistic relationships. It is believed that they are well suited for prediction and classification research.

With the network structure and probability distributions mentioned in Fig. 1, it is convenient to compute the posterior probability of target variable. For example, according to the Bayesian theory $P(A / B)=\frac{P(A, A, P(A)}{P(B)}$, where $P(A)$ is prior probability, $P(B / A)$ is conditional probability, $P(A / B)$ is the posterior probability, we could compute $P(C=\operatorname{True} / G=\operatorname{True})$ by $\frac{P(G=\operatorname{True} / C, \operatorname{True} / P(C, \operatorname{True}))}{P(C)}$. Then, we calculate the original variable probability distributions as follows:

$$
\begin{aligned}
P(C & =\text { True })=\sum_{\mathrm{TE}, V} P(\text { TE }, V, C=\text { True })=\sum_{\mathrm{TE}, V} P(\text { TE }) P(V) P(C \\
& =\text { True } / \text { TE }, V)=P(\text { TE }=\text { True }) P(V=\text { True }) P(C=\text { True } / \text { TE } \\
& =\text { True }, V=\text { Ture })+P(\text { TE }=\text { True }) P(V=\text { False }) P(C \\
& =\text { True } / \text { TE }=\text { True }, V=\text { False })+P(\text { TE }=\text { False }) P(V \\
& =\text { True }) P(C=\text { True } / \text { TE }=\text { False }, V=\text { Ture })+P(\text { TE } \\
& =\text { False }) P(V=\text { False }) P(C=\text { True } / \text { TE }=\text { False }, V=\text { False }) \\
& =0.318
\end{aligned}
$$

$$
\begin{aligned}
P(G & =\text { True })=\sum_{\mathrm{TE}, V, C} P(\text { TE }, V, C, G=\text { True }) \\
& =\sum_{C} P(G=\text { True } / C) \sum_{\mathrm{TE}, V} P(\text { TE }) P(V) P(C / T E, V) \\
& =\sum_{C} P(C) P(G=\text { True } / C)=P(C=\text { True }) P(G=\text { True } / C=\text { Ture }) \\
& \quad+P(C=\text { False }) P(G=\text { True } / C=\text { False })=0.3172
\end{aligned}
$$

Finally, we got the posterior distribution easily as $P(C=$ True $/$ $G=$ True $)=\frac{0.8 \cdot 0.318}{0.3172}=0.802$.

In another case, suppose we have detected the evidence of high temperature and low vibration, the probability of bringing a high gas pressure is shown as:

$$
\begin{aligned}
P(G & =\text { true } / \text { TE }=\text { true }, V=\text { false })=P(G=\text { true } / C=\text { true }) \\
& \cdot P(C=\text { true } / \text { TE }=\text { true }, V=\text { false })+P(G=\text { true } / C=\text { false }) \\
& \cdot P(C=\text { false } / \text { TE }=\text { true }, V=\text { false }) \\
& =0.8 * 0.4+0.1 * 0.6=0.38
\end{aligned}
$$

But with the hypothesis of conditional independence, we could ignore the affections of $(T E, V)$ on node $G$ when $C$ is detected. So, if we already know $(V=$ true,$C=$ false $)$, the result could be calculated directly as $P(G=$ True $/ V=$ True,$C=$ False $)=P(G=$ True $/ C=$ False $)$ $=0.1$.

Because of the characteristics of causality and conditional independence, the Bayesian network provides a comprehensive method of representing relationships and influences among variables. It is also a powerful technique for handling uncertainty and shows a high performance in prediction domain. In addition, by presenting with graphical diagrams of nodes and edges, Bayesian network models can be more easily understood than many other techniques (Lee \& Abbott, 2003).

### 2.2. Bayesian network classifiers

The application of Bayesian network classifiers is divided into two stages. First, the structure and parameters of Bayesian network are derived based on learning algorithm and some constraints. Secondly, the inference process is applied to compute the conditional probability of the target variable and classify it into certain classes based on the probability threshold. The time cost of classifier

![img-0.jpeg](img-0.jpeg)

**Fig. 1.** A simple example of Bayesian networks.

Learning and inference mainly depends on the numbers of variables and of the potential relationships among them. So it is usual to add some relationship constraints to simplify the Bayesian network learning process in actual applications.

The NB (Duda & Hart, 1973) proposes that all attribute variables **X** are conditionally independent given the target variable while it is not true in practice. The TAN (Friedman et al., 1997) makes a great improvement by relaxing the NB assumption with attribute variables to form a tree. But it is unnecessary to build such a complex structure with too many edges which could lead to the overfitting problems. The CBN learns the structure for global optimization not target node, so some weak but useful connections between target node and attribute variables are dismissed for the lowest minimum description length (MDL) (Friedman & Goldszmidt, 1996) score function. Because the target node is conditionally independent to all other variables given its MB, it could not apply all the useful information hidden in the dataset.

### 2.3. Conditional Bayesian Network Classifier

From the descriptions of traditional Bayesian network classifiers, we could find that they all have their own weakness when dealing with different classification missions. We propose a new kind of Bayesian network classifier building algorithm named as conditional Bayesian networks (CBN). The CBN could utilize the conditional independence relationships among attribute variables given the target variable effectively. It could not only enhance the classification accuracy but also lower the network structure complexity at the same time.

With a dataset including variables set, a DAG could be learned from it, see Fig. 2. If there is an arc from node *X* to node *Y*, then we name *X* as the parent node of *Y* (N<sup>*Y*</sup><sub>*P*</sub>) while *Y* is the child node of *X* (N<sup>*C*</sup><sub>*C*</sub>). The other parent nodes of a node's child node are spouse nodes (N<sup>*S*</sup><sub>*N*</sub>), like node *J*. The set of all the child nodes and parent nodes of one node *X* is called neighbor nodes (N<sup>*S*</sup><sub>*N*</sub> = (N<sup>*S*</sup><sub>*P*</sub>, N<sup>*S*</sup><sub>*C*</sub>)) and all the child nodes, parent nodes and spouse nodes of one node *X* are called its Markov Blanket nodes (N<sup>*S*</sup><sub>*N*</sub><sup>*R*</sup> = (N<sup>*S*</sup><sub>*P*</sub>, N<sup>*S*</sup><sub>*C*</sub>, N<sup>*S*</sup><sub>*N*</sub>)). When a node has no parent node, it is called root node while a node without child node is named as leaf node. The ancestor nodes of a node are defined as its parent nodes and the parent nodes' ancestor nodes (N<sup>*L*</sup><sub>*L*</sub> = (N<sup>*L*</sup><sub>*P*</sub>, N<sup>*N*</sup><sub>*N*</sub><sup>*C*</sup><sub>*L*</sub>, ...)), like nodes *A* and *E*. The descendent nodes of a node are defined as its child nodes and the child nodes' descendent nodes (N<sup>*L*</sup><sub>*L*</sub> = (N<sup>*L*</sup><sub>*C*</sub>, N<sup>*N*</sup><sub>*C*</sub><sup>*N*</sup>, ...)), like nodes *N*, *Y* and *P*.

![img-1.jpeg](img-1.jpeg)

**Fig. 2.** An example of variables set and its directed acyclic graph.

For the purpose of describing the principle, algorithm and building process of CBN easily, we defined some other kinds of nodes.

**Definition 1.** Among all the original variables, the nodes that are independent of the learned Bayesian network, which means there is no arc to connect them, are defined as independent nodes (N<sub>*I*</sub>), like node *K*.

**Definition 2.** In a BN, the nodes that are connected with node *X* with edges are called the BN nodes of node *X* (N<sup>*S*</sup><sub>*BN*</sub>). When we delete one node *Y* and its edges from the BN, the rest nodes connected with *X* are named as *X*'s non-*Y* BN nodes (N<sup>*S*</sup><sub>*BN*−*Y*</sub>).

**Definition 3.** The N<sup>*X*</sup><sub>*P*</sub>'s descendent nodes which do not belong to nodes set (X, N<sup>*S*</sup><sub>*N*</sub>, N<sup>*S*</sup><sub>*A*</sub>, N<sup>*S*</sup><sub>*D*</sub>, N<sup>*N*</sup><sub>*A*</sub><sup>*D*</sup><sub>*B*</sub>, N<sup>*N*</sup><sub>*D*</sub><sup>*B*</sup><sub>*B*</sub>) are defined as sideward nodes (N<sup>*S*</sup><sub>*P*</sub><sup>*B*</sup><sub>*B*</sub>, N<sup>*S*</sup><sub>*E*</sub> ∉ (X, N<sup>*S*</sup><sub>*N*</sub><sup>*R*</sup>, N<sup>*S*</sup><sub>*A*</sub>, N<sup>*S*</sup><sub>*D*</sub>, N<sup>*N*</sup><sub>*A*</sub><sup>*D*</sup><sub>*B*</sub>, N<sup>*N*</sup><sub>*D*</sub><sup>*B*</sup><sub>*B*</sub>)), like node *F* in Fig. 3. They have at least one common ancestor node with node *X*.

**Definition 4.** The non-*X* BN nodes of N<sup>*S*</sup><sub>*I*</sub> which do not belong to nodes set (X, N<sup>*S*</sup><sub>*N*</sub>, N<sup>*S*</sup><sub>*A*</sub>, N<sup>*S*</sup><sub>*D*</sub>, N<sup>*N*</sup><sub>*A*</sub><sup>*D*</sup><sub>*B*</sub>, N<sup>*N*</sup><sub>*D*</sub><sup>*B*</sup><sub>*B*</sub>, N<sup>*N*</sup><sub>*E*</sub>) are defined as non ancestor nodes (N<sup>*S*</sup><sub>*N*</sub><sup>*R*</sup><sub>*N*</sub>, N<sup>*N*</sup><sub>*R*</sup><sub>*B*</sub>, N<sup>*B*</sup><sub>*B*</sub>, ∉ (X, N<sup>*S*</sup><sub>*N*</sub><sup>*R*</sup>, N<sup>*S*</sup><sub>*A*</sub>, N<sup>*S*</sup><sub>*D*</sub>, N<sup>*N*</sup><sub>*D*</sub><sup>*B*</sup><sub>*B*</sub>, N<sup>*N*</sup><sub>*D*</sub><sup>*B*</sup><sub>*B*</sub>, N<sup>*N*</sup><sub>*E*</sub>)), like nodes *B* and *G* in Fig. 3. Normally, they are the spouse nodes of

![img-2.jpeg](img-2.jpeg)

**Fig. 3.** Three kinds of connection relationships.

ancestor nodes and the spouse nodes' family member. So they do not have a kinship with node *X*.

**Definition 5.** All the non-*X* BN nodes of **N**<sub>0</sub><sup>X</sup> which do not belong to nodes set (X, **N**<sub>M</sub><sup>X</sup>, **N**<sub>S</sub><sup>X</sup>, **N**<sub>S</sub><sup>X</sup>, **N**<sub>M</sub><sup>X</sup>, **N**<sub>S</sub><sup>X</sup>) are defined as non-descendent nodes (**N**<sub>M0</sub><sup>X</sup> = **N**<sub>M0–X</sub><sup>X</sup>, **N**<sub>M0</sub><sup>X</sup> ∉ (X, **N**<sub>M</sub><sup>X</sup>, **N**<sub>S</sub><sup>X</sup>, **N**<sub>S</sub><sup>X</sup>, **N**<sub>M</sub><sup>X</sup>, **N**<sub>M</sub><sup>X</sup>))<sup>X</sup>, like nodes *C*, *H* and *M* in Fig. 3.

All conditional independence statements can be derived from a BN structure by using the rules of directed separation (Charniak, 1991). In a BN, a path *P* between *X* and *Y* represents a set of nodes with edges connecting them from *X* to *Y*. There are three kinds of connections between a random variable *Z* and its two immediate neighbors in the path, *X* and *Y*. The three possibilities are shown in Fig. 4 and correspond to the possible combinations of arrow directions from *Z* to *X* and *Y*. In the first case, all the edges are in the same direction; in the second case, both are leaving *Z*; and in the third, both point at *Z*. We can name *Z* as a linear, diverging or converging node in a path *P* depending on the situations according to Fig. 3.

The description of a block condition in the path is as below. A path *P* from *X* to *Y* is blocked with respect to the evidence nodes **Z** if **Z** has the property that either.

1. There is at least one linear node in *P* that belongs to **Z**.
2. There is at least one diverging node in *P* that belongs to **Z**.
3. There is a converging node in *P*, it and its descendent nodes do not belong to **Z**.

If all the paths between *X* and *Y* are blocked by **Z**, then we may say that **Z** directed separate *X* and *Y*, which means that *X* is conditionally independent of *Y* given **Z**, marked as *X⊥Y*|**Z**.

According to the description of conditional independence, we give the definition of CBN and infer some deductions for the purpose of building a CBN.

**Definition 6.** For a node *X* in the nodes set and the learned BN, its conditional Bayesian network is defined as CBN<sup>X</sup> = (**N**<sub>CBN</sub><sup>X</sup>, **A**<sub>CBN</sub><sup>X</sup>). The nodes set **N**<sub>CBN</sub><sup>X</sup> include *X*, **N**<sub>MB</sub><sup>X</sup> and the set of nodes which are conditionally independent with **N**<sub>MB</sub><sup>X</sup> given *X*; the edges set **A**<sub>CBN</sub><sup>X</sup> include the edges in **N**<sub>MB</sub><sup>X</sup>, the edges from *X* to all conditionally independent nodes and the edges among the conditionally independent nodes themselves.

**Deduction 1.** With a BN learned from nodes set and a node *X* in it, **N**<sub>I</sub> are conditionally independent with **N**<sub>MB</sub><sup>X</sup> given *X*.

Because any node in **N**<sub>I</sub> does not connect with the BN with arc and could not form a path to **N**<sub>MB</sub><sup>X</sup>, **N**<sub>MB</sub><sup>X</sup> could not affect it given *X*.

![img-3.jpeg](img-3.jpeg)

**Fig. 4.** The structures of learned Bayesian network classifiers.

**Deduction 2.** With a BN learned from nodes set and the node *X* in it, node *X*'s **N**<sub>NA</sub><sup>X</sup> are conditionally independent with **N**<sub>NA</sub><sup>X</sup> given *X*.

For any node in **N**<sub>NA</sub><sup>X</sup>, because the BN does not have a loop in it, all the paths from the node to (**N**<sub>I</sub><sup>X</sup>, **N**<sub>I</sub><sup>X</sup>, **N**<sub>M</sub><sup>X</sup>) will have at least one converging node in (**N**<sub>I</sub><sup>X</sup>, **N**<sub>I</sub><sup>X</sup>, **N**<sub>I</sub><sup>M</sup><sup>X</sup>, **N**<sub>I</sub><sup>I</sup><sup>X</sup>). Since (**N**<sub>I</sub><sup>X</sup>, **N**<sub>I</sub><sup>X</sup>, **N**<sub>I</sub><sup>M</sup><sup>X</sup>) do not belong to *X*, we could say that *X* directed separate **N**<sub>NA</sub><sup>X</sup> and (**N**<sub>I</sub><sup>X</sup>, **N**<sub>I</sub><sup>X</sup>, **N**<sub>I</sub><sup>X</sup>). It is proven that **N**<sub>NA</sub><sup>X</sup> are independent with (**N**<sub>I</sub><sup>X</sup>, **N**<sub>I</sub><sup>X</sup>, **N**<sub>I</sub><sup>X</sup>) given node *X*.

**Deduction 3.** With a BN learned from nodes set and the node *X* in it, node *X*'s **N**<sub>ND</sub><sup>X</sup> are conditionally independent with **N**<sub>ND</sub><sup>X</sup> given *X*.

For any node in **N**<sub>ND</sub><sup>X</sup>, because the BN does not have a loop in it, all the paths from the node to (**N**<sub>I</sub><sup>X</sup>, **N**<sub>I</sub><sup>X</sup>, **N**<sub>I</sub><sup>X</sup>) will have at least one converging node in (**N**<sub>I</sub><sup>X</sup>, **N**<sub>I</sub><sup>X</sup>, **N**<sub>I</sub><sup>M</sup><sup>X</sup>, **N**<sub>I</sub><sup>M</sup><sup>X</sup>). Since (**N**<sub>I</sub><sup>X</sup>, **N**<sub>I</sub><sup>X</sup>, **N**<sub>I</sub><sup>M</sup><sup>X</sup>, **N**<sub>I</sub><sup>M</sup><sup>X</sup>)

do not belong to $X$, we could say that $X$ directed separate $\mathbf{N}*{N D}^{\mathrm{p}}$ and $\left(\mathbf{N}*{i j}^{\mathrm{p}}, \mathbf{N}*{i j}^{\mathrm{p}}, \mathbf{N}*{\mathrm{sp}}^{\mathrm{p}}\right)$. Then any node in set $\mathbf{N}*{N D}^{\mathrm{p}}$ is independent with $\left(\mathbf{N}*{i j}^{\mathrm{p}}, \mathbf{N}*{i j}^{\mathrm{p}}, \mathbf{N}*{\mathrm{sp}}^{\mathrm{p}}\right)$ given node $X$.

Generally speaking, when we learn a directed acyclic graph form dataset, there are still some nodes which are conditionally independent with the target node's MB given target node. These nodes could also provide part mutual information for a more effective classification.

### 2.4. Product failure rate classification modeling

There are two main kinds of prediction technologies in machine prognostics. The most obvious and widely used prognostic is to predict the remaining useful life (RUL) before a failure occurs given the current machine condition and operation profile. Second it would be more interesting to predict the probability that a machine operates without a fault or a failure up to some future time given the current machine condition and operation profile (Jardine, Lin, \& Banjevic, 2006). In our research, we focus on classification of product failure rate when a series of products with diverse configurations operate in different conditions. With this prediction, it could provide solid support for maintenance decision making, spare parts supply chain management and product optimization.

The procedure of built product failure rate classification model based on Bayesian networks is as shown below.

1. For the whole product family of a company, choose the $i$ th series product $\left(P^{i}, i=1,2, \ldots\right)$ as the object of product failure rate classification.
2. According to $P^{i}$, search the related failure records from history failure database (including product configuration and application information variables set $C$, product failure rate variable $R$ ). Each record is marked as $\mathbf{D}*{j}^{i}=\left(\mathbf{C}*{i}^{i}, R*{i}^{i}\right), j=$ $1,2, \ldots, n$.
3. To avoid training over fitting and perform well for new record, randomly divide failure dataset $\mathbf{D}_{i}$ into two parts. While $2 / 3$ of the dataset are used as a training set $\mathbf{D}*{\text {train }}^{\mathrm{p}}$ for learning the classifier, the remaining $1 / 3$ are used as a test set $\mathbf{D}*{\text {Test }}^{\mathrm{p}}$ for testing the general behavior of the classifier.
4. With the product failure rate $R$ as target node, based on the train set $\mathbf{D}*{\text {Train }}^{\mathrm{p}}$, learn the Bayesian networks classifier's structure $\mathbf{G}$ and compute the conditional probability distributions $\Theta$ with Munteanu's EQ algorithm (Munteanu \& Bendou, 2001).

Table 1 Variables used in the case study.


Table 2 Data set characteristics.


1. For the learned BN, set the failure rate node as the target node and search the nodes set $\left(\mathbf{N}*{N A}^{\mathrm{p}}, \mathbf{N}*{N D}^{\mathrm{p}}, \mathbf{N}_{i}\right)$ according to their definitions.
2. Lock the nodes set $\left(R, \mathbf{N}*{\mathrm{AB}}^{p}, \mathbf{N}*{\mathrm{NA}}^{p}, \mathbf{N}*{\mathrm{ND}}^{p}, \mathbf{N}*{i}\right)$ and delete all other nodes and their edges.
3. According to the deductions before, $\left(\mathbf{N}*{\mathrm{NA}}^{p}, \mathbf{N}*{\mathrm{ND}}^{p}, \mathbf{N}*{i}\right)$ are conditionally independent with $\mathbf{N}*{\mathrm{AB}}^{p}$ given $R$. So adding edges from $R$ to every node in nodes set $\left(\mathbf{N}*{N A}^{p}, \mathbf{N}*{N D}^{p}, \mathbf{N}*{i}\right)$ does not affect the original conditional independence relationship.
4. Use the Maximum Likelihood Estimation (MLE) algorithm to update the conditional probability distributions of $\left(\mathbf{N}*{\mathrm{NA}}^{p}, \mathbf{N}*{\mathrm{ND}}^{p}, \mathbf{N}*{i}\right)$ resulting from the added edges. Finally, the CBN model for product failure rate classification is built and we could test and implement it for the practical applications.
5. According to the performance evaluation criteria, test the performance of learned CBN classifier with test set $\mathbf{D}*{\text {Test }}^{\mathrm{p}}$ and compare the results with other classifiers.
6. Input the new product configuration and application record $\mathbf{C}*{\text {new }}$ into CBN classifier and calculate the posterior probability distribution of target variable $R$ to set its failure rate $R*{\text {new }}$

## 3. Case study

### 3.1. Data set

The data we used for case study are all gathered from a French product manufacturer in a certain period (Ben Ahmed, Beranger, \& Geslin, 2008). It describes the failure rate of product with different configurations and application conditions. The target variable is failure rate and the attribute variables include COUNTRY, TYPE, USE, AIR_CON, POWER and GEAR_BOX, see Table 1. Because of commercial confidence, we replace the original attribute variables states with corresponding symbols. To avoid over fitting, we split the data set according to process before and the detailed characteristics are shown in Table 2.

### 3.2. Evaluation criteria for classification

The confusion matrix (Hand, Mannila, \& Smyth, 2001) is undoubtedly the most commonly used criteria for measuring performance of classifiers which is defined as $\mathbf{P}=\left[p_{i j}\right], i, j=1,2, \ldots, n$. Number $n$ represents the number of classes and $p_{i j}$ represents the number of records which have been predicted to be in class $j$ but which are actually in class $i$. When $i=j, p_{i j}$ means the number of correct classification records and the total accuracy of model is $\operatorname{Total}=\frac{\sum_{i=1}^{n} p_{i j}}{\sum_{i=1}^{n} \sum_{i=1}^{n} p_{i j}}$. Besides accuracy, we use classification precision $P_{i j}=\frac{p_{i j}}{\sum_{i=1}^{n} p_{i j}}, i, j=1,2, \ldots, n \quad$ and classification reliability $R_{i j}=\frac{p_{i j}}{\sum_{i=1} p_{i j}}, i, j=1,2, \ldots, n$ to describe distributions of true-positive rate, true-negative rate, false-positive rate and false-negative rate in detail.

Because the target variable has only two states, we also apply Receiver Operating Characteristic (ROC) to estimate the classification results. By moving the classification threshold, it could get coordinate points with true-positive rate as $Y$-axis and false-positive rate as $X$-axis. With a ROC curve connecting these points, we could evaluate the classifiers by comparing the curve to the $45^{\circ}$ straight line and computing the area under the ROC curve (AUROC). It is calculated according to the curve displayed at the top of the graphic and represents the surface under the ROC curve divided by the total surface. If the curve is far from the $45^{\circ}$ straight

Table 3 Comparison of classifiers' accuracy.

$(\%)$ | False-negative
$(\%)$ | True-negative
$(\%)$ | False-positive
$(\%)$ | Total accuracy (\%)  |

line, it means that the AUROC is larger and the performance of classifier is better (Bamber, 1975).

Moreover, the Bayesian network classifiers predict the target class label with its own probability, so the evaluation of the model could also be realized by using the gain curve and the lift curve (Bayesia Limited Company, 2010a). Cumulative gain curve and lift curve are graphical representations of the advantage of using a predictive model by measuring the difference between the results obtained with and without classifier model. The information can be used to determine whether we should use this model or one similar to it in the future.

The gain curve is generated by sorting the test individuals according to the target value probability returned by the classifier in the increasing order. We draw it using the actual positive rates to see how much the classifier model would have helped in this situation. The $X$-axis represents the rate of individuals that are taken into account. The $Y$-axis represents the rate of individuals with the target value that have been identified as such. In the gain curve, the yellow ${ }^{1}$ line represents the percentage of individuals that have the target value in fact; the blue curve represents the gain curve of a pure random policy; the red curve represents the gain curve corresponding to the classifier. The Gini Index is computed according to the curve and displayed at the top of the graphic. It means the ratio of the surface under the red curve and above the blue curve divided by the surface above the blue curve. This interactive curve is not only an evaluation tool, but also a decision support tool that allows defining the best probability threshold by balancing gains and costs of the classification result.

The lift curve comes from the gain curve and highlights the improvement between the result returned by the current classifier and the result using no model. The $X$-axis represents the rate of test individuals that are taken into account. The $Y$-axis represents the lift factor defined as the ratio between the rate of the targeted population obtained with the current policy and the rate obtained with the random policy. The larger the lift factor value the better the accuracy, for a given model.

### 3.3. Simulation results

According to the modeling process listed in Section 2.4, we learn and test the data set with NB, CBN and GBN algorithms with BayesiaLab (Bayesia Limited Company, 2010b). The structures of four learned Bayesian network classifiers are show in Fig. 4. The confusion matrixes of classification results are listed in Table 3. For the purpose of comparison, we also train the decision tree induction algorithm C4.5 with Matlab toolbox. The Gain curves and Lift curves of all Bayesian network classifiers are shown in Figs.

[^0]5 and 6, respectively. The ROC curves of each Bayesian network classifiers are shown as in Fig. 7.

From Table 3, we could see that the NB performs poorest with an accuracy of $70.89 \%$. It is because its assumption ignores of the

![img-4.jpeg](img-4.jpeg)

Fig. 5. The gain curves of four learned BN classifiers.

[^0]: ${ }^{1}$ For interpretation of color in Figs. 4-7, the reader is referred to the web version of this article.

![img-5.jpeg](img-5.jpeg)

**Fig. 6.** The lift curves of four learned BN classifiers.

relationships among attributes variables. The C4.5's result is moderate with 74.68% and still has a gap with the better ones. The GBN works better, but it pays more attention on full structure optimization and balance between the precision and complexity. The TAN gets a good result of 81.01% since it relaxes the conditional independence assumption by considering the edges between attribute

Table 4 The structure complexity of BN classifiers.


nodes. The CBN gets the highest score of $83.54 \%$ since it not only considers the conditional independence between attribute variables but also dismisses the useless direct relationships between attribute variables.

In the aspect of AUROC, the areas of TAN and GBN are almost the same but are much larger than NB's $77.06 \%$. The AUROC of CBN is the best and reaches $85.70 \%$. For the criteria of Gain curve and the Lift curve, the CBN also gets the highest performance with $28.9 \%$ in Gini index and 1.41 in mean Lift comparing to other three normal BN classifiers.

Besides, as shown in Fig. 4 and Table 4, the GBN classifier has the simplest structure with only three nodes and two edges because of a lowest MDL score. The TAN model has the most complex structure since it considers the relationship between the attribute nodes on the basis of a NB classifier. The CBN's structure complexity is in between with five nodes and four edges for an effective but economical utilization of all variables' information.

## 4. Conclusions

The paper proposes a new kind of conditional Bayesian network classifier on the basis of traditional NB, TAN and GBN model. The principle, algorithm and modeling of CBN are described in details to guide the application of identifying the product failure rate. Because it considers the conditional independence between attribute nodes and target node's Markov Blanket given the target node, the CBN could provide a more effective classification result. The case study shows that, with comparison to the BN classifiers and decision tree C4.5 classifier, the CBN got the highest performance in the all criteria of total accuracy, AUROC, Gini index and mean Lift.

Although the GBN classifier had the simplest network structure, the CBN made an acceptable balance between network complexity and promotion of classification performance. It may satisfy the expectations for maintenance decision making, spare parts supply chain management and product configuration optimization.

## Acknowledgment

The authors gratefully acknowledge the financial support for this research from the China Civil Aircraft Advanced Research Project, the China Aeronautical Science Foundations (Grant No. 2009ZE53052), the Science and Technology Project of Shaanxi Province (Grant No. 2010KB-11) and the Hover Star project of Northwestern Polytechnical University, China (Grant No. 07XE0152).
