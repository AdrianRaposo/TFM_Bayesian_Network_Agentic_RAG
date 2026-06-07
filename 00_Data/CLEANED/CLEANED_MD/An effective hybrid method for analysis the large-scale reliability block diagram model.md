# Eksploatacja i Niezawodnosc - Maintenance and Reliability Volume 25 (2023), Issue 3 

journal homepage: http://www.ein.org.pl

Article citation info:
Ping Y, Ren Y, Li Z, Yang D, Yang C, An effective hybrid method for analysis the large-scale reliability block diagram model, Eksploatacja i Niezawodnosc - Maintenance and Reliability 2023: 25(3) http://doi.org/10.17531/ein/169408

## An effective hybrid method for analysis the large-scale reliability block diagram model

## Yashi Ping ${ }^{\mathrm{a}}$, Yi Ren ${ }^{\mathrm{a}}$, Zhifeng $\mathrm{Li}^{\mathrm{a}, *}$, Dezhen Yang ${ }^{\mathrm{a}}$, Chao Yang ${ }^{\mathrm{b}}$

${ }^{a}$ School of Reliability and Systems Engineering, Beihang University, China<br>${ }^{\mathrm{b}}$ School of Aeronautical Science and Engineering, Beihang University, China

## Highlights

- This paper proposes extended diagrams (e.g., plus and multi-functional structures).
- A structure identification method is proposed for large-scale RBD.
- An analysis method based on BDD is proposed to enhance the efficiency of RBD.

This is an open access article under the CC BY license (https://creativecommons.org/licenses/by/4.0/)

## Abstract

The reliability block diagram (RBD) is a graphical tool used for reliability modeling and analysis in various industries, including shipbuilding, aviation, and aerospace. Typically, RBDs are transformed into Bayesian networks for quantitative analysis of systems. Bayesian networks are probabilistic graphical models that can capture the uncertainties and causal relationships in complex systems. They can provide various reliability metrics such as failure probability, mean time to failure, availability, etc. However, these techniques have several drawbacks, especially for large-scale models, such as being extremely time and memory-consuming. To address these issues, we propose a hybrid method for quantitative analysis of large-scale RBDs based on the structure identification approach and binary decision diagrams. Theoretical analysis and case verification demonstrate that the proposed method is significantly more efficient than the current one.


## Keywords

reliability block diagram, structure identification, plus structure, binary decision diagram.

## 1. Introduction

The reliability block diagram (RBD) is a widely used graphical modeling tool for analyzing the reliability of a system. It expresses a system as a connection of several components by their logical relation of reliability 6 , and is used in various industries including aerospace 7 ships [9, 15], supply chains 8 and more.

RBDs consist of series, parallel, voting, and bridging compositions, which can also be replaced by parallel-series or series-parallel combinations. Rauzy expanded k-out-of-n gates by applying the decomposition rather than expanding as a sum of products 15 . Rodrigues described the bridge system in its
parallel-series and series-parallel combinations 17. Additionally, in the multi-channel communication, measurement \& control, command system and some military equipment systems, there are a variety of values for the working state. It is not enough to describe its reliability only by using the probability of normal and failure states. Its reliability needs to be described according to the characteristics of the actual working state. However, the classical reliability model theory cannot consider important factors when facing such a special system. In order to solve this problem, Zhou proposed the concept of "plus" system in the 1980s. With the improvement of

[^0]
[^0]:    (*) Corresponding author.

    E-mail addresses:
    Y. Ping, pys@buaa.edu.cn, Y. Ren, renyi@buaa.edu.cn, Z. Li (ORCID: 0009-0006-8991-7115) lizhifeng@buaa.edu.cn, D. Yang, dezhenyang@buaa.edu.cn, C. Yang, yangchao@buaa.edu.cn

technology and military modernization, many other models, including multi-functions and plus structures, have also been added to RBD.

Traditionally, paper-and-pencil proof methods have been used for RBD-based analysis; but these methods are constrained and cannot guarantee $100 \%$ correctness. Laura 1 developed an efficient library for RBD in C programming language, and they demonstrated that their library outperformed SHARPE. However, the tool still relies on mathematical formulas to evaluate the probability of series, parallel, k-out-of-n, and bridging blocks. There are two main drawbacks to this approach: 1) the path sets cannot be directly collected, and 2) It is impossible to determine the reliability of RBD system 5 with repeated events.

In addition to these methods, another approach is to transform the original RBD model into a secondary structure and analyze it there. For instance, an RBD can be transformed into a fault tree, which can subsequently be handled using algorithms designed to solve fault trees. Methods for calculating the reliability of fault tree with repeated events (duplicate nodes) are as follows:

1) Factorizing algorithm 20.
2) Sum of disjoint products (SDP) 20.
3) Binary Decision Diagrams (BDD) algorithm 7.
4) Using (1) and simplifying it 20 .
5) Bayesian networks 13 .

All of these methods can be used directly to solve the fault tree problem, and the fault relationship between the system and its components can also be represented by RBD. Therefore, fault trees are logically equivalent to RBD 2, and these methods can be applied to RBD problems as well. The procedure for converting an RBD to a BN was described by Tchangani 18 and Bobbio 1. For each component of an RBD, a node without parents is first created; marginal probabilities are sufficient for these nodes. Whether the components are arranged in series or parallel determines the conditional probability for all other nodes. Torres-Toledano presented an extension of BN applied to reliability analysis 18. The complex system was represented by a three layers Bayesian network in their method. The blocks in RBD are transformed into the root nodes as the first layer. Then, all path sets of the system are obtained and each path set is treated as a virtual node of the second layer. In the third layer,
one node is created to represent the system.
Bayesian networks can be transformed into secondary structures, and the marginal distributions of each variable can be inferred based on various inference algorithms. According to the reference 23, the method based on the clique tree will take nearly twice as long as the bucket elimination method to obtain the posterior probability distribution of all variables. Owing to the system reliability can be inferred with a variable representing the system, so we just need to query the answer of that variable. In a word, the bucket elimination method is more efficient that the method based on the clique tree. Even so, the solution of BN is still relatively complex, because BN is usually directly solved, and needs to be converted into a secondary structure before proceeding. Compared with BN, BDD solution is less complex. In reference 3, the authors proposed a method equivalent to the BDD, the method can handle and/or logic, which is enough for the simple RBD model. Zhang proposed a BDD/MMDD model by combining the BDD model with the MMDD model, for the reliability evaluation of multiphase mission systems (MPMS)25. According to the reference 23,we can know that the BDD model can be used to analyze non-repairable PMS, but must be combined with state-based methods. Moreover, the issue of state space explosion may arise when dealing with a considerable number of components. To address the issue of BDD explosion, a truncation method based on BDD chains and Markov chains was proposed in reference 11, which also expanded the applicability of the BDD \& Markov method. Reference 20 demonstrated that BDD models can be used to handle static subtrees of dynamic fault trees. Reference 12 stated that BDD had the advantage of being further extended to consider faults in repairable edges and vertices. Elena developed new algorithms for calculating Direct Partial Boolean Derivatives based on BDD, which enables the analysis of functions with large dimensions. Additionally, the author introduced experimental analysis based on BDD algorithms, which demonstrated the high efficiency of the algorithms in terms of computational time and memory consuming for importance analysis25. What's more, this approach facilitated the investigation of practical and large-scale systems.

The remainder of this paper is organized as follows: The reliability block diagrams and binary decision diagram are briefly reviewed in Section 2. Section 3 describes the developed

method for transforming RBD into BDD. The analysis and benchmark test results to demonstrate the efficiency of the proposed method are listed in Section 4. Finally, the last section concludes the paper and suggests potential directions for future research.

## 2. Preliminaries

### 2.1 Reliability block diagram

The Reliability Block Diagram (RBD) is a graphical modeling approach used to describe the logical relationships of reliability among system components. The RBD incorporates several fundamental logical structures, including series, parallel, voting, and plus structures, among others. These structures provide a means of representing the dependencies and interrelationships between system components and enable engineers to evaluate the overall reliability of complex systems.
(1) Series structure

The reliability of the series structure can be calculated using eq. 1 :

$$
R=\prod_{i=1}^{n} R_{i}
$$

where R is the reliability of the series system; i is the index of components in the series system, and $R_{i}$ represents the reliability of the i-th component.
(2) Parallel structure

The reliability of the parallel structure can be calculated using eq. 2 :

$$
R=1-\prod_{i=1}^{n}\left(1-R_{i}\right)
$$

where R is the reliability of the parallel system; i is the index of components in the parallel system, and $R_{i}$ represents the reliability of the i-th component.
(3) Vote structure

The reliability of the vote structure can be calculated using eq. 3 :

$$
R=\sum_{j=k}^{n}\binom{n}{j} r^{j}(1-r)^{n-j}
$$

where R is the reliability of the system; k is the vote value; j is the number of components in functioning state in the vote system, n is the number of components consisting of system, and r represents the reliability of the components which are independent and identically distributed.

Plus structure
![img-0.jpeg](img-0.jpeg)

Fig. 1. The example of plus structures.
The reliability of the plus structure shown in Fig. 1 can be calculated using eq. 4 :

$$
R=\sum_{i=1}^{n} w_{i} R_{i}
$$

where R is the reliability of the plus system; i is the index of components in the plus system; $\omega_{i}$ is the weight of the component, and $R_{i}$ represents the reliability of the i-th component.

Moreover, the RBD can be extended to represent multifunctional systems, as described in various literatures such as GJB813-1900. This extension of RBD can be evaluated using our proposed method.

### 2.2 Binary decision diagram

A binary decision diagram (BDD) is a tree-like structure consisting of nodes, including root nodes, non-terminal nodes, and terminal nodes, connected by directed edges. It is a data structure used to express Boolean functions. The BDD method was first proposed by Lee 10 in 1959. In 1993, Rauzy 15 introduced the BDD method for analyzing fault trees. It has been shown that BDD-based methods typically require less memory and computational time than other methods.

There are three main elements of binary decision diagrams, each of which has the following meaning:

Circle: non-leaf node (non-terminal node), representing an event;

Box: leaf node (terminal node) with two node values ("1" for normal, " 0 " for failure);

Directed line segment: marked with "1" or "0", indicating whether an event occurs or not.

![img-1.jpeg](img-1.jpeg)

Fig. 2. An illustrative example of BDD.
The mathematical expression for the BDD can be represented as follows:

$$
\operatorname{ite}(x, y, z)=x y+\bar{x} z
$$

Fig. 2 is a graphical representation of Eq.5. The high efficiency of the BDD structure can be attributed to several factors. Firstly, BDD is a block diagram encoded based on Shannon theory, which enables the compression of the original block diagram by sharing equivalent subgraphs. Secondly, when commands are executed on the BDD, the generated results are stored synchronously, preventing repeated calls and operations and enhancing efficiency.

## 3. Method

### 3.1 The process of the proposed method

The analysis method of the reliability block diagram model we proposed has the following key features:
(1) Enhanced modeling capability for large-scale complex systems;
(2) Optimized the memory usage for efficient analysis;
(3) Improved the calculation efficiency for large-scale complex systems;
(4) Support the solution of RBD models with plus structures;

And our method consists of the following three steps:
(1) Identify the basic structure of the reliability block diagram, which includes separate structures such as series, parallel, voting, plus, bridging, etc., and create a simple reliability block diagram model with a hierarchical structure.
(2) Transform the hierarchical reliability block diagram model into an equivalent binary decision diagram model.
(3) Assess the reliability level of the complex system using the BDD model that has been created.

### 3.2 Method assumptions and scope of application

Throughout the paper, we present a method for the large-scale RBD model, based on the following assumptions:
(1) The system and affiliated components operate in either of two states: functioning or failed. These states are denoted by the values ' 1 ' and ' 0 ', respectively;
(2) The components within the system are mutually independent, and there is no common cause failure;

In this paper, the method proposed is a generic reliability assessment method that can provide an accurate value of the evaluated system's reliability, it can be applied to various systems. However, it is not suitable for assessing the availability of a system with repairable elements. To address the limitation, we would integrate Markov model into our method to enhance the capability of representing the repairable system.

### 3.3 Structure identification of RBD

To evaluate the reliability of large-scale complex systems, the first step is to identify the structure of the reliability block diagram. This involves recognizing the fundamental components of the model, such as series, parallel, voting, and plus structures. By recursively replacing these basic structures with super components, a hierarchical reliability block diagram can be constructed. The structural identification flow is shown in Fig. 3.
(1) Set the end node of the reliability block diagram as the current node. Then traverse forward from the current node until the hierarchical RBD is fully constructed.
(2) Access the node C, and judge whether the node C has predecessor nodes, if not, the hierarchical RBD is constructed completely, and if so, count the number of predecessor nodes.
(3) If the current node C has only one predecessor P , it means that P and C are connected in series. In this case, P and C can be encapsulated into a virtual node whose predecessor is the same as P's predecessor, and whose successor is the same as C's successor.
(4) If the current node C has multiple predecessors, we need to determine whether they have a common predecessor. If so, the predecessors of C can be encapsulated into a virtual node. If not, we can access the predecessors of C in order and set them as the current node. Once this process is complete, return to node C and continue with step (2).

![img-2.jpeg](img-2.jpeg)

Fig. 3. The flowchart of identifying of the structure of an RBD.

# 3.4 Transform hierarchical RBD model into BDD 

After constructing the hierarchical RBD, we proceed to explain the transformation process of the RBD into binary decision diagrams. The transformation process involves the following steps:
(1) Traverse the hierarchical RBD from top to bottom until an unconverted unit is found;
(2) Move to the lowest module of the unit;
(3) Convert these modules into the corresponding binary decision diagram based on the structure type.
(4) Backtracking upwards and converting layer by layer to form binary decision diagram.
The flowchart for the BDD transformation is depicted in Fig. 4.
![img-3.jpeg](img-3.jpeg)

Fig. 4. The flowchart for the BDD transformation.

The transformation rules of the binary decision diagram are as follows:
a) Series structure

The states of units in a series structure correspond to the edges of the binary decision diagram representing 0 and 1 , respectively. The series structure of the unit is generated according to the logical operation rules of the BDD. A simple concatenated structure converted to a corresponding BDD is shown in Fig. 5.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Binary decision diagram corresponding to the tandem structure.

The transformation is applicable to tandem systems with various numbers of components. Proper operation of tandem system requires that all components work properly. In the corresponding BDD, there is only path that from the root node to the terminal node 1 represents the system proper operation. Therefore, we conclude that the result of BDD is identical to the formula result.
b) Parallel structure

The 0 and 1 states of the units in the parallel structure correspond to the 0 and 1 edges of the binary decision diagram, and the parallel structure composed of the units is generated according to the logical operation rules of the BDD. A simple parallel structure converted to a corresponding BDD is shown in Fig. 6.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Binary decision diagram model corresponding to the parallel structure.

In the corresponding BDD, there is only one path that from
the root node to the terminal node 0 indicates the system failure. The probability of system failure can be calculated by the product of the probability of components failure.
c) Voting structure

The voting structure can be expressed as a combination of series and parallel structures, so that the voting structure can first be converted to a series and parallel structure, and then to a corresponding binary decision diagram model. A simple voting structure converted to a series and parallel structure is shown in Fig. 7.
![img-6.jpeg](img-6.jpeg)

Fig. 7. Series and parallel structure corresponding to the voting structure.

Based on the analysis above, the result of the corresponding BDD of the voting structure can be proved to be identical to the result calculated by exact math formula.
d) Plus structure

The 0 and 1 states of the cells in the plus structure correspond to the 0 and 1 edges of the BDD. In addition, multiple virtual nodes are added to represent the units' weights. Assuming that there are n units in the whole plus structure, n virtual nodes need to be added. The edges of the virtual nodes represent the weight value of the units. An example of the binary decision diagram of a three-unit is shown in Fig. 8.
![img-7.jpeg](img-7.jpeg)

Fig. 8. Binary decision diagram corresponding to the plus structure.

In the same way it can be shown that the calculation of the plus structure is also accurate.

### 3.5 System reliability evaluation based on BDD

After the hierarchical RBD has been converted to BDD, traverse the path where the leaf node is 1 in the BDD, multiply the probabilities on the path, and add the results of the multiplication to get the reliability of a complex system, the calculation process is as follows:

$$
\begin{aligned}
& R(S)=\sum_{i=1}^{H} P\left(T_{i}\right) \\
& P\left(T_{i}\right)=\prod_{j=1}^{n_{i}} P\left(N_{j}=1\right)
\end{aligned}
$$

$$
T_{i}=\left\{\left(N_{j}, N_{k}\right) \mid N_{j}, N_{k} \in N\right\} . j, k=1,2, \cdots, n
$$

Where N is nodes' sets of the $\mathrm{BDD},\left(N_{j}, N_{k}\right)$ is the path in the path sets $T_{i}$.

## 4. Case definition and application

The following case is used to demonstrate that the proposed method takes advantage over the three levels Bayesian networks proposed by Toledano ${ }^{[15]}$.

This reliability block diagram is obtained after the modelling of a complex system, as seen in Fig. 9. The reliability block diagram is identified and hierarchical according to the methods mentioned above, as illustrated in Fig. 10.
![img-8.jpeg](img-8.jpeg)

Fig. 9. Reliability block diagram of a complex system.
![img-9.jpeg](img-9.jpeg)

![img-10.jpeg](img-10.jpeg)

Fig. 10. Reliability block diagram identification process and hierarchical process.
The BDD that corresponds to RBD shown in Fig. 10 is
depicted in Fig. 11, while the Bayesian network is illustrated in Fig. 12.
![img-11.jpeg](img-11.jpeg)

Fig. 11. The BDD corresponding to the complex structure.

![img-12.jpeg](img-12.jpeg)

Fig. 12. The BN corresponding to the complex structure.
The BDD comprises 14 nodes, each with two values indicating the likelihood of an event occurring. Additionally, two terminal nodes can be created by merging the nodes with the labels "one" or "zero". Thus, the BDD is a compact structure for RBD. The Bayesian network has 15 nodes, where the root nodes represent components and intermediate nodes denote identified structures. The entire system is represented by the node V5. The root nodes are binary, while the intermediate and system nodes have large-scale conditional probability tables (CPT). The system node is binary, and its CPT has $2^{4}$ probability values. Based on the above analysis, we can conclude that the Bayesian networks are susceptible to the state exploration problem.

In addition to theory analysis, to demonstrate our method has an advantage over the BN-based method, we create some

RBD models and obtain the run time of the two methods applied to the same model. The RBD structure for efficiency comparison between our method and BN-based method is shown in Fig. 13. The components are connected in parallel then in series. We assume the number of the components in parallel structure and the number of the modules in series structure are $m$ and $n$ respectively.
![img-13.jpeg](img-13.jpeg)

Fig. 13. The RBD structure is used to efficiency comparison.

In the first parameters group, fix the parameter $n$ to 50 and vary the parameter $m$ which is determined from Table 1. In the second parameters group, set parameter $m$ to 10 and the parameter $n$ is variable whose value is as in Table 2.

Table 1. The first parameters group.


Table 2. The second parameter group.


The comparison results between our method and the BNbased method are illustrated in Fig. 14 and Fig. 15. It is obvious that performance of our method is much better than BN-based method. In our case study, the computer configuration used is 11th Gen Intel(R) Core (TM)i7-1165G7 @ $2.80 \mathrm{GHz}, 16 \mathrm{~GB}$ DDR4 RAM, Microsoft Windows 10 professional, and the two methods all were implemented in C# language.
![img-14.jpeg](img-14.jpeg)

Fig. 14. The comparison results of the first parameters group.
![img-15.jpeg](img-15.jpeg)

Fig. 15. The comparison results of the second parameters group.

## 5. Conclusions and future work

To address the lengthy computation time and significant memory consumption associated with large-scale RBDs, we propose a novel approach. Our approach offers several advantages over conventional methods:
(1) The analyst can recognize the system's units in the hierarchical RBD model because it differs little from the original model.
(2) The proposed method is suitable for general RBDs. In addition to series, parallel and voting, plus structures and multifunctional RBDs.
(3) The method is more efficient and uses less memory than previous methods.
(4) By identifying the structure and hierarchy of the RBD, we can generate a modular RBD that facilitates parallel processing, further improving computational efficiency.

In the future, we will integrate the Markov models into our method to overcome the limitation that the method is unsuitable for maintainable systems. Besides, with regards to the issue of model conversion accuracy, we intend to carry out further investigation and verification in subsequent research.
