# Research on Fault Diagnosis of ZPW-2000K Track Circuit Based on RS-BN Algorithm 

Junwu LI, Guoning LI


#### Abstract

For problem of complex fault types and uncertain diagnostic features of the ZPW-2000K track circuit, traditional fault diagnosis mainly adopts manual diagnosis methods, which leads to low automatic diagnosis. This paper proposes a fault diagnosis method based on Rough Sets (RS) reduction model and Bayesian Network (BN) structure learning fusion. Firstly, data mining and feature extraction are performed on the fault data table, and expert knowledge is built into the prior knowledge base. Secondly, the K2 algorithm is used to train the fault feature quantity, and the BN model is built by combining the prior knowledge base. Then, a diagnostic decision table is established through the fault instance, and RS is used for attribute reduction, dimensionality reduction, and simplified model. The MLE algorithm is used again to learn the parameters to obtain the conditional probability table of the model, and the complete BN structure is established based on the RS-BN algorithm. Finally, the comparative analysis of the simplified model and the non-simplified model is carried out. Through the experimental simulation of the ZPW-2000K track circuit fault of a high-speed railway station, the accuracy and effectiveness of the diagnostic method are verified.


Keywords: attribute reduction; Bayesian network; fault diagnosis; rough set; ZPW-2000K track circuit

## 1 INTRODUCTION

ZPW-2000K non-insulated track circuit is based on the introduction and localization of French UM71 track circuit technology, combined with China's national conditions, and proposed a system with high security, high transmission and high reliability. It is important equipment for China's high-speed railway signal system, and it is also a key equipment to ensure the smooth and safe operation of railway high-speed trains and efficient transportation. Its main function is the open circuit inspection, occupancy inspection and data transmission of circuit. Its failure will seriously affect the transportation efficiency and lead to safety accidents. Therefore, accurate positioning and diagnostic fault are of great significance for the reliable operation of the train.

The ZPW-2000K track circuit has a complex system, high randomness and high uncertainty between fault causes and representations, which make fault diagnosis difficult. In recent years, fault diagnosis techniques such as expert systems, fault trees and neural networks have been continuously developed, and many scholars have applied this method to the fault diagnosis of track circuits. Literature [1] combined with decision tree and expert system, proposed a decision tree fault diagnosis system, but this method relies too much on expert experience and is easily misdiagnosed. In [2], the fault model of the ZPW2000 track circuit and the fault phenomenon are explored, and the fault model of the system failure tree is established. However, it is extremely difficult to establish an accurate model. In [3], based on the working principle and fault characteristics of the track circuit, the FNN fault diagnosis model is established, but the neural network is easy to fall into local optimum.

The Bayesian Network (BN) is a hotspot in artificial intelligence research and has been successfully applied to many fault diagnoses [4-6]. Rough Sets (RS) is a classical theory for dealing with uncertainty. It can process and analyze incomplete data and has been widely used in many fields such as fault diagnosis, decision control, and pattern recognition [7-9]. Based on the advantages of BN and RS, this paper proposes a RS-BN ZPW-2000K track circuit fault diagnosis method. Firstly, data mining and
feature extraction are performed on faulty instances, and BN data learning and parameter learning are implemented in combination with expert experience. Secondly, RS theory is applied to attribute reduction, dimension reduction and denoising, to obtain minimum diagnostic rules and establish optimal BN. Finally, the BN model was verified and analyzed by the fault instance of the ZPW-2000K track circuit of a high-speed railway station.

### 1.1 ZPW-2000K Track Circuit System

The ZPW-2000K track circuit is specifically designed for passenger dedicated lines and high-speed rail systems. Its structural composition includes: indoor equipment and outdoor equipment. Indoor equipment includes: transmitter, receiver, loss redundant controller and lightning protection analog network disk. Outdoor equipment includes: tuning matching unit, compensation capacitor, equipment connection line, air core coil and air turbulence transformer. Its system structure [10] is shown in Fig. 1.

## 2 THEORIES AND ALGORITHMS

### 2.1 Bayesian Network

BN combines graph theory and probability theory for uncertain reasoning and data analysis. $B N=(G, P)$ consists of two parts: (1) directed acyclic graph $G=(I, E)$, where $I=\left\{A_{1}\right.$, $\left.A_{2}, A_{3}, \ldots, A_{n}\right\}$ is the set of nodes, $E=\left\{E_{1}, E_{2}, E_{3}, \ldots, E_{n}\right\}$ is the set of edges, and the directed edges reflect the inter-node dependencies. (2) The conditional probability table (CPT) represents the prior probability of each node and describes the probability distribution of the nodes. Assuming that the $B N$ nodes are $A_{1}, A_{2}, A_{3}, \ldots, A_{n}$, its joint probability distribution is as shown in Eq. (1).

$$
p=\prod_{i=1}^{n}-p\left[A_{i} \mid \pi\left(A_{i}\right)\right]
$$

The search-scoring method is a common method of BN structure learning. Accurate network structure can be obtained through data learning. Assuming that the sample contains $n$ variables, the number of networks that exist through structure learning is as shown in Eq. (2).

$$
f(n)=\sum_{i=1}^{n}(-1)^{i+1} \frac{n!}{i!(n-i)!} 2^{i(n-1)} f(n-i)
$$

The complexity of the $B N$ structure will grow exponentially following the number of nodes $n$, and the $B N$ structure learning is also considered to be the NP-Hard problem [11]. This paper uses the classical K2 algorithm, as shown in Eqs. (3) and (4).

$$
\begin{aligned}
& P(D \mid B s)=\prod_{i=1}^{n} \operatorname{score}\left(i, p a_{i}\right) \\
& \operatorname{score}\left(i, p a_{i}\right)=\prod_{j=1}^{N_{i}}\left[\frac{\Gamma\left(\partial_{i j}\right)}{\Gamma\left(\partial_{i j}+N_{i j}\right)} \prod_{k=1}^{N} \frac{\Gamma\left(\partial_{i j k}+N_{i j k}\right)}{\Gamma\left(\partial_{i j k}\right)}\right]
\end{aligned}
$$

where $B s$ represents the network structure and $D$ represents the data.

The parameter learning of $B N$ is relatively mature, so the Maximum Likehood Estimation (MLE) is used to study the parameters of $B N$.
![img-0.jpeg](img-0.jpeg)

Figure 1 System structure of ZPW-2000K

### 2.2 Rough Sets

RS is a classical mathematical theory that deals with fuzzy and inaccurate problems [12]. Its attribute reduction can eliminate redundant information, simplify conditional attributes, and generate minimal decision rules without changing decision-making ability. The theory consists of the following three parts:
(1) Knowledge expression system: $S=\{U, R, V, f\}$ is an ordered quaternion, where domain $U=\left\{X_{1}, X_{2}, \ldots, X_{n}\right\}$ is a collection of sample points, $R=C \cup D$ is a set of conditional attributes and a set of decision attributes.
(2) Unresolvable relationship: the type division relationship between objects in $U$. Attribute subset $B \subseteq R$, if objects $X_{i}, X_{j} \in U, \forall r \in B$, if and only if $f\left(X_{i}, r\right)=f\left(X_{i}, r\right), X_{i}$ and $X_{j}$ are indistinguishable, denoted as $\operatorname{Ind}(B)$.
(3) Decision-making: it embodies the diagnostic rules of the sample from conditional attributes to decision attributes. Let $S=\{U, R, V, f\}, a \in R$, if $\operatorname{Ind}(R-\{a\})=\operatorname{Ind}(R)$, it indicates that $a$ is unnecessary in $R$, otherwise it is a necessary attribute.

## 3 FAULT DIAGNOSIS OF ZPW-2000K TRACK CIRCUIT BASED ON RS-BN ALGORITHM

The fault data table used in this paper is derived from the track circuit monitoring warning information and the fault repair form filled out by the maintenance personnel. The fault data table is recorded in natural language and has no rules. Usually, the computer cannot process the data, so data mining and unified coding of the fault data table are required.

### 3.1 Establish a Diagnostic Knowledge Base

The establishment of the fault diagnosis knowledge base is traditionally based on expert experience. It is usually recorded in natural language and script, subjectively biased and not easily accessible. When a certain type of failure occurs, there is no experience to follow. In this paper, data mining and feature extraction are performed on the fault data table, and the diagnostic knowledge base is built by experts prior. Through data mining, the potential implicit relationship between fault points is found, which enriches the prior knowledge and reduces the dependence on expert knowledge. The establishment process is shown in Fig. 2.

![img-1.jpeg](img-1.jpeg)

Figure 2 The process for establishing a diagnostic knowledge base

### 3.2 Determining the Diagnostic Model Node of BN

In this paper, the fault information is divided into three layers: the fault trigger layer, the fault mode layer and the fault feature layer, which represent the fault cause, the fault occurrence module and the fault representation phenomenon. Its hierarchical relationship is shown in Fig. 3.
![img-2.jpeg](img-2.jpeg)

Figure 3 Fault node causal hierarchy
The fault node hierarchy table of the ZPW-2000K track circuit is established according to the causal hierarchical relationship between the diagnostic knowledge base and the faulty node, as shown in Tab. 1, Tab. 2, and Tab. 3.

Table 1 Fault mode node


Table 2 Fault initiating node


Table 3 Fault feature node


### 3.3 Establish a BN Model for a Priori Diagnostic Knowledge Base

Based on the prior diagnosis knowledge base, the fault node causal hierarchy of Fig. 3, and the fault node information of Tabs. 1 to 3, a BN diagnostic model of the ZPW-2000K track circuit is established based on the diagnostic knowledge base. The faulty node adopts discrete coding, and its state value takes values: 1-occurred, 0 -did not occur. The model was built using Matlab's BNT toolbox, as shown in Fig. 4.
![img-3.jpeg](img-3.jpeg)

Figure 4 BN model based on prior diagnosis knowledge base

### 3.4 Establish a BN Model Based on K2 Learning Algorithm

The K2 algorithm is a local search algorithm for data optimization. It combines the hill climbing search algorithm and the Bayesian scoring index to optimize the network model with high accuracy and excellent search efficiency. Because of the established fault data table, the information is relatively complete, so the K2 algorithm is used to mine the potential causal relationship between the fault points. Take the M1-indoor sender as an example, and use the Lean_Struct_K2() function to model, as shown in Fig. 5.

![img-4.jpeg](img-4.jpeg)

Figure 5 M1 module - BN model based on K2 algorithm

### 3.5 Establish a BN Model for Information Fusion

The BN model established by using the a priori diagnostic knowledge base or the K2 algorithm structure is not very accurate. The model based on the prior diagnosis knowledge base has a simple structure, ignoring the potential correlation implied by some faulty nodes, and there is an 'under-fitting'. The model learned through the K2 algorithm structure can deeply discover the potential correlation implied by some faulty nodes, but the established structure is complex, there is redundancy between faulty nodes, and there is 'over-fitting'. Therefore, the advantages of the two can be fully combined, and the two methods are merged to form a BN model based on the prior diagnosis knowledge base and the K2 algorithm structure learning, as shown in Fig. 6.
![img-5.jpeg](img-5.jpeg)

Figure 6 BN model based on diagnostic knowledge base and structural learning fusion

### 3.6 Establish a BN Fault Diagnosis Model Based on RSBN Algorithm

The ZPW-2000K track circuit is complex and uncertain, and the data is noisy, fuzzy, and random. The construction of the model is complicated and the number of nodes is large, which affects the efficiency and accuracy of modeling. The RS algorithm is used to eliminate redundant attributes, reduce kernel attributes, mine the simplest diagnosis rules, reduce the diagnostic scale and algorithm complexity, and improve the diagnostic efficiency. The attribute reduction process of the RS algorithm is shown in Fig. 7.
(1) Establish an initial diagnostic decision table

Taking the diagnostic knowledge base and ZPW2000 K track circuit fault data as decision samples, extract the feature attributes and establish an initial diagnosis decision table, as shown in Tab. 4.
![img-6.jpeg](img-6.jpeg)

Figure 7 The process of RS algorithm attribute reduction
Table 4 Fault diagnosis decision


(2) Establish a difference matrix

Define the difference matrix $M(S)=\left[M_{i j}\right]_{n \times n}$, the value of $m_{i j}$ is shown in Eq. (5).

$$
m_{i j}= \begin{cases}a \in C, & a\left(x_{i}\right) \neq a\left(x_{j}\right) \wedge D\left(x_{i}\right) \neq D\left(x_{j}\right) \\ 0, & D\left(x_{i}\right)=D\left(x_{j}\right) \quad(i, j=1,2, \ldots, n) \\ -1, & a\left(x_{i}\right)=a\left(x_{j}\right) \wedge D\left(x_{i}\right) \neq D\left(x_{j}\right)\end{cases}
$$

The information system $U$ represents the fault information of ZPW-2000K track circuit, the condition attribute set $C=\{S 1, S 2, \cdots, S 18\}$ represents 18 fault features, and the decision attribute $D=\{M 1, M 2, \cdots, M 5\}$ represents 5 fault modes. The difference matrix is an $n$-order square matrix symmetric with respect to the main diagonal. When calculating, only the lower triangular part is considered. The difference matrix is established according to the difference Eq. (5) and Tab. 4, as shown in Eq. (6).
![img-7.jpeg](img-7.jpeg)
(3) RS attribute reduction

Find and remove the single element in the difference matrix and keep the remaining element combinations. Combine the remaining elements with a single attribute element to get a simplified combination of attributes. Use the mutual information formula to calculate element dependencies, for example, calculate the dependency values of attributes $P$ and $Q$, as shown in Eq. (7).

$I(Q, P)=H(Q)-H\left(\frac{Q}{P}\right)=\sum_{x, y} p(x, y) \log _{2} \frac{p(x, y)}{p(x) p(y)}$
Calculate attribute combination dependencies and use the combination of minimum dependent values as the best attribute group. The optimal decision diagnosis rule is obtained based on the optimal attribute group, and an optimal diagnosis decision table is established. The condition attribute reduction in Tab. 4 is: $\{S 2, S 3, S 4, S 5, S 6, S 7, S 8, S 9, S 10, S 11, S 12, S 14, S 15, S 17\}$, and the dimension of the fault feature points is reduced to 14 , which reduces the complexity of the model.
(4) Establish a BN diagnostic model based on RS-BN algorithm

According to the optimal decision diagnosis rule and the information fusion BN model, a BN fault diagnosis model based on RS-BN algorithm is established, as shown in Fig. 8.
![img-8.jpeg](img-8.jpeg)

Figure 8 BN model based on RS-BN algorithm
![img-9.jpeg](img-9.jpeg)

Figure 9 Comparison of parameter learning node probabilities

### 3.7 Determine the Parameter Model of BN

The accuracy of parameter learning depends on the accuracy of the build model. After establishing the optimal BN model, it is necessary to determine the prior probability of each faulty node and establish a conditional probability table (CPT) of the faulty node. In this paper, the MLE algorithm [13] is used to study the parameters of BN. The BN model of the information fusion in Fig. 6 is defined as BN1, and the BN model of the RS attribute reduction in Fig. 8 is defined as BN2, and the prior probability of the faulty node is learned by GenIe2.0 software. The results are shown in Fig. 9 .

It can be seen from the comparison of (a) and (b) in Fig. 9 that, in the case where the number of samples is the same, the reduced BN2 model and the unreduced BN1 model have the same conditional probability for the fault nodes obtained by the MLE parameter learning. It shows that model reduction cannot only simplify the model, but also get the same prior probability.

## 4 INSTANCE VERIFICATION OF FAULT DIAGNOSIS

### 4.1 Instance Verification 1

Select a fault data from the fault instance as a diagnostic example of the BN model, as shown in Tab. 5.

Table 5 Fault data instance


In the fault instance of Tab. 5, extract the fault feature set \{'red band fault', 'derailment out voltage'\}, and the fault feature set for the diagnostic models BN1, BN2: $T 1=\{0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0\}$,
$T 2=\{0,0,0,0,0,0,1,0,0,0,0,0,1,0,0\}$. Add evidence $T 1, T 2$ to the inference engine and infer the probability of failure occurrence: $p(R=1 \mid T=1)$. The BN1 and BN2 models were diagnosed and inferred using the Linked Tree Algorithm (JT) of GenIe2.0 software. The diagnosis results are shown in Fig. 11 .

It can be seen from the diagnosis results of a) and b) in Fig. 10 that under the known evidences $T 1$ and $T 2$, the maximum failure probability diagnosed by the BN1 model and the BN2 model is $R 5$ (receive level line error). It is consistent with the actual cause of the failure and verifies the accuracy of the model. For the BN2 model, the posterior probability of $R 5$ is 0.9125 , which is significantly higher than the 0.8875 of the BN1 model, while the probability values of $R 12$ and $R 13$ are decreased, indicating that the BN2 model is reduced by the attribute of RS, which improves the fault

knowledge clarity and fault diagnosis ability better than BN1.


(b) Diagnosis result of BN2

Figure 10 Comparison of model diagnosis reasoning results

### 4.2 Instance Verification 2

For the 100 pieces of verification data of the ZPW2000K track circuit, the fault is extracted according to the failure mode ratio, and the extracted data is shown in Tab. 6 .

Table 6 Fault verification data extraction


The BN1 and BN2 models are diagnosed and inferred using the $j$ tree_inf_engine () function in Full-BNT toolbox of BN. The comparison of the diagnostic results is shown in Fig. 12.

The comparisons of the fault diagnosis accuracy rates of the BN1 and BN2 model are shown in Tab. 7.

As can be seen from Fig. 11 and Tab. 7, the average diagnostic accuracy of the BN1 model is $89.33 \%$, and that of BN2 is $93.33 \%$. In particular, there are only 3 and 1 misdiagnosis data for $M 5$, and the accuracy rate of fault diagnosis is $92.50 \%$ and $97.50 \%$, which greatly verified the effectiveness of the two models. Although the diagnostic accuracy of $M 2$ is relatively low, it has reached more than $82 \%$. This is because the number of instances of $M 2$ is 75 . The lower number of instances leads to the diagnostic model of this module which is not very accurate. As the sample size continues to increase, the accuracy of fault diagnosis will continue to increase. The diagnostic accuracy of the BN2 model is higher than that of BN1. This is because the RS attribute reduction eliminates model redundancy and unnecessary attributes, eliminates interference and noise, and makes the model diagnosis rules more accurate and clearer. At the same time, the model structure is simplified, the misdiagnosis rate is reduced, and the diagnostic accuracy is improved. The BN2 diagnostic model is more efficient and has high likelihood.

![img-10.jpeg](img-10.jpeg)

Figure 11 Comparison of inference diagnosis

Table 7 Fault diagnosis correct rate comparison


## 5 CONCLUSION

(1) Through the full integration of ZPW-2000K system structure and expert experience, the fault prior diagnosis knowledge base and BN model structure are established. The potential internal hidden relationship between the fault points is mined by using the fault instance of the ZPW-2000K track circuit and the classic K2 algorithm learning BN structure.

(2) The BN model established by the a priori diagnostic knowledge base and learned by the K2 algorithm is used for information fusion, and the advantages of the two are combined to establish a new BN model to further improve the accuracy of the diagnostic model.
(3) We fully combine the advantages of BN and RS. RS theory is used to reduce the attributes of the initial decision table, reduce the dimension, eliminate redundant and non-nuclear attributes, reduce the model, and generate the simplest diagnostic rules to establish the best BN model structure.
(4) Diagnostic analyses of the reduced model and the unreduced model are carried out by taking the actual fault of a high-speed railway station as an example. By comparison, the RS-BN fault diagnosis model proposed in this paper is compact in structure and efficient in diagnosis, with high reliability and high practical likelihood. It provides practical decisionmaking support for on-site electrical maintenance personnel to quickly and effectively diagnose track faults, which has practical significance for the development of fault diagnosis technology for ZPW2000K track circuit.

## Contact information:

Junwu LI, Corresponding author
School of Automation \& Electrical Engineering, Lanzhou Jiaotong University, Lanzhou 730070, China
E-mail: lijunwu_lzjiu@163.com
Guoning LI
School of Automation \& Electrical Engineering, Lanzhou Jiaotong University, Lanzhou 730070, China