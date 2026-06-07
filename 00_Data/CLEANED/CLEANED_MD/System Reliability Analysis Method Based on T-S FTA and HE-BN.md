# System Reliability Analysis Method Based on T-S FTA and HE-BN 

Qing Xia ${ }^{1}$, Yonghua $\mathbf{L i}^{2, *}$, Dongxu Zhang ${ }^{1}$ and Yufeng Wang ${ }^{2}$<br>${ }^{1}$ School of Mechanical Engineering, Dalian Jiaotong University, Dalian, 116028, China<br>${ }^{2}$ School of Locomotive and Rolling Stock Engineering, Dalian Jiaotong University, Dalian, 116028, China<br>*Corresponding Author: Yonghua Li. Email: yonghuali@163.com

Received: 20 April 2023 Accepted: 22 May 2023 Published: 17 November 2023


#### Abstract

For high-reliability systems in military, aerospace, and railway fields, the challenges of reliability analysis lie in dealing with unclear failure mechanisms, complex fault relationships, lack of fault data, and uncertainty of fault states. To overcome these problems, this paper proposes a reliability analysis method based on T-S fault tree analysis (T-S FTA) and Hyper-ellipsoidal Bayesian network (HE-BN). The method describes the connection between the various system fault events by T-S fuzzy gates and translates them into a Bayesian network (BN) model. Combining the advantages of T-S fault tree modeling with the advantages of Bayesian network computation, a reliability modeling method is proposed that can fully reflect the fault characteristics of complex systems. Experts describe the degree of failure of the event in the form of interval numbers. The knowledge and experience of experts are fused with the D-S evidence theory to obtain the initial failure probability interval of the BN root node. Then, the Hyper-ellipsoidal model (HM) constrains the initial failure probability interval and constructs a HE-BN for the system. A reliability analysis method is proposed to solve the problem of insufficient failure data and uncertainty in the degree of failure. The failure probability of the system is further calculated and the key components that affect the system's reliability are identified. The proposed method accounts for the uncertainty and incompleteness of the failure data in complex multi-state systems and establishes an easily computable reliability model that fully reflects the characteristics of complex faults and accurately identifies system weaknesses. The feasibility and accuracy of the method are further verified by conducting case studies.


## KEYWORDS

System reliability; D-S evidence theory; hyper-ellipsoidal bayesian network; T-S fault tree

## 1 Introduction

The system is a complex of many interacting and connected elements that are capable of performing a specific function. Quantifying the impact of system or human failure on a specific function is the content of system reliability analysis. For the reliability analysis of complex systems in military engineering, aerospace, rail transportation, and other fields, the system structure and operating environment are complex, the test costs are expensive and the historical failure data are insufficient $[1,2]$. So how to build a reliability model that is easy to calculate and completely reflects the failure characteristics of the system? How to overcome the lack of reliability data and effectively

identify the weak points of the system? These are the main problems in the reliability analysis of complex systems. Therefore, it is necessary to propose a new reliability analysis method that can effectively solve these problems.

System reliability is studied for the system as a whole. However, the concept of a system as a whole is relative. The components that make up a whole system can be seen as subsystems of the whole system. This whole system can in turn be seen as subsystems of a larger whole system. The study of system reliability requires the selection of suitable analysis methods according to different applications, different analysis purposes, and different system characteristics. Commonly used traditional system reliability analysis methods include the Reliability block diagram (RBD) method, Fault tree analysis (FTA) method, Bayesian network, Markov analysis, GO method, and Petri net, etc. These traditional reliability analysis methods are mainly based on exact probability theory. However, the reliability information of complex systems is diverse and uncertain, and the reliability data is difficult to obtain [3,4]. So, the above traditional reliability analysis methods are not applicable anymore. Therefore, some scholars have introduced uncertainty characterization methods such as fuzzy theory [5], interval analysis [6], and probabilistic boxes [7] into reliability analysis.

The fault tree is an intuitive reliability modeling method that adequately represents component and system interactions and fault relationships. It has certain advantages for rapid modeling. When complex systems and equipment fail due to multiple causes and the causal relationship between higher and lower-level fault events is unclear, fault trees can be used to describe the links between fault events deterministically through logic gates. The system can then be analyzed qualitatively (to obtain the minimum cut set) and quantitatively (to obtain the top event reliability data and the bottom event importance). It has been widely used in the aerospace [8], transportation [9], and power [10] fields. Based on the fault tree, the Takagi-Sugeno Fault tree analysis (T-S FTA) method is further proposed to solve the problem of system fault polymorphism and uncertainty of the fault mechanism and data [11]. T-S fault tree has been applied to the reliability analysis of multi-state complex systems [12-14]. However, when used to calculate the top event probability of system fault trees in real engineering, the current T-S FTA is computationally intensive and cannot be backward calculated. BN fills exactly this gap and is widely used in reliability analysis $[15,16]$.

BN uses conditional probabilities to describe the relationships between events in a fault tree. It has powerful inference and analysis capabilities. It is more suitable for complex systems in terms of representing polymorphic events, describing node relationships, and computational analysis capabilities. Therefore, the FTA model constructed based on the fault mechanism is transformed into BN inference to diagnose faults. It becomes a hot spot in the field of fault research of complex systems. In [17], the work focused on the use of BN to deal with the uncertainty of accidents and the limitations of the fault tree. In [18], a multistate fault tree was transformed into a BN model. The reliability of a semi-submersible drilling rig system under different fault states was calculated.

In the above study, BN requires large amounts of accurate fault data. Sample data are scarce for most high-reliability systems in practical engineering. The randomness assumption or fuzziness assumption is not satisfied, but it is easy to determine the uncertain information boundaries. Therefore, some scholars have introduced methods such as Fuzzy theory, Interval analysis, and Evidence theory into traditional Bayesian networks. To propose the interval Bayesian network, interval probabilities are used instead of exact probabilities. It is used to solve the problem of the influence of uncertainty and incomplete information on the reliability assessment results. The interval triangular fuzzy number is used to describe Bayesian network node probabilities for the analysis of cognitive uncertainty and failure correlation in complex multistate systems [19]. The fuzzy prior probability interval of BN is

obtained by fusing highly conflicting data through D-S evidence theory to perform risk assessment [20]. In [21], the interval probability was used to quantify the cognitive uncertainty of BN, and the Bayesian posterior interval probabilities were solved using the GL2U (Generalised Loopy 2-Updating) algorithm. The interval Bayesian network calculates the upper-level node failure interval when each root node failure interval is simultaneously taking an interval extreme value. This simultaneous taking of extremes is difficult to achieve in practical engineering. For the interval Bayesian network, only upper and lower bounds on the probability of node intervals are used for system reliability analysis. The correlation of the number of intervals is not taken into account. The results of the calculations are coarse and conservative.

The Hyper-ellipsoidal model is a convex set model. The analytical description of uncertain interval covariate correlations using the HM can effectively circumvent the extreme cases of interval Bayesian models [22-24]. Therefore, the Hyper-ellipsoidal model has been applied to fatigue life analysis [25] and structural reliability analysis [26]. The introduction of convex models into the T-S FTA method to define uncertain covariate boundaries or ranges [27]. Then the problem of relatively conservative interval T-S FTA results can be solved. The HM was used to describe the uncertain interval variables of the system fault tree model for reliability assessment, which is more in line with engineering practice $[28,29]$.

Based on the above considerations, this paper proposes a system reliability analysis method based on T-S FTA and HE-BN. The main contributions of this paper are as follows:

1. A reliability modeling method that reflects complex system failure characteristics is proposed. It improves modeling and computational efficiency over traditional reliability analysis methods.
2. The method can effectively deal with the problem of insufficient system failure data and uncertainty about the degree of failure.
3. The method solves the problem of relatively conservative calculation results when the traditional interval Bayesian network describes uncertainty fault data. It is more in line with engineering practice.

The rest of the paper is organized as follows: In Section 2, the mapping relationship between T-S FTA and BN in terms of structure and working principle is analyzed. The D-S evidence theory and the HM are briefly reviewed. In Section 3, a reliability analysis method based on T-S FTA and HE-BN is proposed. Section 4 presents a case study on the reliability analysis of complex systems. The validity of the proposed method is illustrated. Finally, Section 5 presents the concluding remarks.

# 2 Introduction of Basic Theory 

### 2.1 T-S Fault Tree and Bayesian Network

The T-S FTA is an analysis method that considers the impact of multiple fault levels on the system. It has IF-THEN rules and describes inter-event connections with T-S gates. When the input event fault state of the IF-THEN rule is two-state and the output event satisfies the traditional fault tree logic gates, the T-S Fault tree degenerates to the traditional fault tree. The traditional fault tree is a special case of the T-S Fault tree. The T-S Fault tree model is shown in Fig. 1a, where X1, X2, and X3 are bottom events, M1 is the middle event, M2 is the top event, and T-S gate 1 and T-S gate 2 are T-S fuzzy gates.

![img-0.jpeg](img-0.jpeg)

Figure 1: Model comparison
Considering the fuzziness of the event fault state, the T-S FTA uses the fuzzy number to describe the event fault state. For example, the fault state of the T-S gate input event $x_{i}(i=1,2, \ldots, n)$ is a fuzzy number $x_{i}{ }^{[n]}\left(a_{i}=1,2, \ldots, k_{i}\right)$. The fault state of the output event $y$ is a fuzzy number $y^{[n]}\left(b_{l}=\right.$ $1,2, \ldots, n_{l}$ ). Then the fault logic relationship between the events can be described by the T-S gate rules. Rule $l(l=1,2, \ldots, r)$ : If the input event $x_{1}$ fault state is $x_{1}{ }^{[n]}$, input event $x_{2}$ fault state is $x_{2}{ }^{[n] 1}, \ldots$, and input event $x_{n}$ fault state is $x_{n}{ }^{[n]}$, the probability of output event fault state $y^{[n]}$ is $P^{r}\left(y^{[n]}\right)$. Among them, $r$ is the total number of T-S rules that satisfy $r=k_{1} k_{2} \ldots k_{n}=\prod_{i=1}^{n} k_{i}$.

The Bayesian network is a directed acyclic network composed of a directed acyclic graph and a conditional probability table, as shown in Fig. 1b. Where X1, X2, and X3 are the root nodes, Y1 is the intermediate node, and Y2 is the leaf node. X1, X2, and X3 are the parent nodes of Y1, and Y2 is the child node of Y1. The nodes are connected by directed edges and the strength of the connection is determined by the conditional probability $P . P$ consists of conditional probability parameters between variables. The probability distribution $P(X)$ of the BN in Fig. 1b is:
$P(X)=P\left(X_{1}, X_{2}, X_{3}\right)=\prod_{i=1}^{3} P\left(X_{i} \mid P a\left(X_{i}\right)\right)$
where $P a\left(X_{i}\right)$ is the parent node set of nodes $X_{i}$. When $P a\left(X_{i}\right)$ is an empty set, $P\left(X_{i} \mid P a\left(X_{i}\right)\right)$ is the prior probability $P\left(X_{i}\right)$ of node $X_{i}$.

The T-S FTA solves the problem of uncertainty about the failure mechanism and the degree of failure in complex systems. However, it is computationally complex and cannot be reasoned backward. And BN is superior to T-S FTA in computational analysis [17]. However, it is more difficult to construct BN directly.

# 2.2 D-S Evidence Theory 

The fault tree analysis method based on the fuzzy reliability model is relatively mature. However, in engineering practice, it is often difficult to obtain sufficient data to determine the probability density function or fuzzy affiliation function of parameters [30]. As a mathematical method to deal with uncertainty inference problems, D-S evidence theory quantifies the degree of confidence and likelihood of propositions. It captures the unknown and uncertainty of the problem better than the traditional probability theory. It provides a way to obtain input data in fault tree analysis.

D-S evidence theory is a theory of information fusion [31]. It expresses the uncertainty problem through the belief function and the plausibility function [32]. Define the discernment framework $\Theta$,

which consists of several completely mutually incompatible elements. Denote $A$ as any subset of the discernment framework $\Theta$. Define the basic creditability allocation function for the evidence $i$ to be $m_{i}: 2^{\omega} \rightarrow[0,1]\left(2^{\omega}\right.$ is a powerful set of $\left.\Theta\right)$ satisfying:

$$
\left\{\begin{array}{l}
m(\varnothing)=0 \\
\sum_{A \subseteq \Theta} m(A)=1
\end{array}\right.
$$

Define the belief degree Bel: $2^{\omega} \rightarrow[0,1]$ and plausibility degree $P l: 2^{\omega} \rightarrow[0,1]$. When $\forall A \subseteq \Theta$, and $A \neq \varnothing$, there are $\operatorname{Bel}(A)=\sum_{B \subseteq A} m(B), P l(A)=\sum_{B \cap A \neq \varnothing} m(B), \operatorname{Bel}(A)=1-P l(A)$.

According to the D-S synthesis rule, the synthesis rule for $n$ pieces of independent evidence on the identification frame $\Theta$ as shown in Eq. (3):
$m(A)=\left(m_{1} \oplus m_{2} \oplus \cdots \oplus m_{n}\right)\left(A_{i}\right)=\frac{1}{K} \sum_{A_{1} \cap A_{1} \cap \cdots \cap A_{n}=A} \prod_{j=1}^{n} m_{j}\left(A_{i}\right)$
Among them, $K$ is the normalization factor, which is used to measure the degree of conflict between evidence, and can be obtained by Eq. (4):
$K=\sum_{A_{1} \cap A_{1} \cap \cdots \cap A_{n} \neq \varnothing} \prod_{j=1}^{n} m_{j}\left(A_{i}\right)=1-\sum_{A_{1} \cap A_{1} \cap \cdots \cap A_{n}=\varnothing} \prod_{j=1}^{n} m_{j}\left(A_{i}\right)$

# 2.3 Hyper-Ellipsoidal Model 

The D-S theory of evidence cannot resolve serious conflicts and complete conflicts in the evidence. And the more the number of elements in a subset, the greater the ambiguity of the subset. HM is a convex set model. It has the advantages of continuous parameter variation, simple model structure, and easy correlation analysis. It can better compensate for the lack of too-conservative analysis results of the Interval model [22], as shown in Fig. 2.
![img-1.jpeg](img-1.jpeg)

Figure 2: Two-dimensional interval model and two-dimensional hyper-ellipsoidal model
The HM is a method of reflecting the deviation of a random variable based on the distance between its equivalent unit hypersphere coordinate origin and the failure surface of a structure in normalized vector space. If the random variable $X_{i} \in\left[x_{i}^{L}, x_{i}^{U}\right](i=1,2, \cdots, n)$ in the set of random variables $X$, where $x_{i}^{L}$ and $x_{i}^{U}$ are the lower bound and upper bound of the value of $X_{i}$, respectively. Then the HM of the set of random variables X is described as:

$$
\left[\frac{X_{1}-x_{10}}{x_{1}}, \cdots, \frac{X_{n}-x_{n 0}}{x_{n r}}\right]^{T} \cdot\left[\frac{X_{1}-x_{10}}{x_{1}}, \cdots, \frac{X_{n}-x_{n 0}}{x_{n r}}\right] \leq 1
$$

where, $x_{i 0}=\frac{x_{i}^{L}+x_{i}^{U}}{2}, x_{i r}=\frac{-x_{i}^{L}+x_{i}^{U}}{2}$ are the nominal value and the deviation of $x_{i}$, respectively.

# 3 T-S FTA and HE-BN Reliability Analysis Methods of Coupler System 

Conditional probability tables for BN are difficult to construct. The T-S FTA method is computationally complex and cannot be reasoned backward. Using the Interval model to describe the failure probability of the root node is relatively conservative. To address these problems, a reliability analysis method based on T-S FTA and HE-BN is proposed. Firstly, a T-S fuzzy gate is used to describe the connection between each failure event of the system. Then the BN model of the system is constructed. Secondly, experts describe the event failure degree in the form of interval numbers. The knowledge and experience of several experts are fused using the D-S evidence theory. The initial failure probability interval of each root node of the BN is obtained. Then the Hyper-ellipsoidal Model (HM) constrains the initial failure probability interval. The HE-BN model of the system is constructed. Finally, the probability of failure of the system is inferred and calculated to find out the key components of the system. The analysis process is shown in Fig. 3, and the analysis steps are as follows:
![img-2.jpeg](img-2.jpeg)

Figure 3: T-S FTA and HE-BN reliability analysis process
Step 1: Analyse the system structure and working principle. Determine the top event T and the bottom event $X_{i}(i=1,2,3, \cdots, n)$. Connect them with a T-S gate to construct a T-S fault tree model of the system. Describe the fuzzy fault occurrence probability of the bottom event by the interval number $P\left(X_{i}\right)=\left[x_{i}^{L}, x_{i}^{U}\right](i=1,2, \cdots, n)$. T-S gate rule $l$ is expressed as $P_{(l)}\left(y^{[n]}\right)$.

Step 2: Transform the T-S FTA into a BN model according to Fig. 3.
In the working principle, the T-S FTA and BN can be mapped from one to another. Each event in the T-S FTA corresponds to a BN node. The T-S gate rule and the conditional probability table of

the BN can also be mapped, see Table 1. Therefore, the T-S FTA can be used as a reference to build a BN quickly and efficiently.

Table 1: Comparison of calculation rules


The events in the T-S fault tree are transformed into nodes one by one according to the correspondence in Fig. 3 and Table 1. The state of each event corresponds to the state of each node. The nodes are connected using directed edges according to the logic of T-S gates. The probability of failure $P\left(X_{i}\right)=\left[x_{i}^{L}, x_{i}^{U}\right](i=1,2, \cdots, n)$ of the bottom event is assigned to the root node as the prior probability. The T-S gate rules are described using the conditional probability table $P\left(y=y^{[n]}\left|x_{1}=\right.\right.$ $\left.\left.x_{1}^{\left\lfloor n_{1}\right\rfloor}, \cdots, x_{n}=x_{n}^{\left\lfloor n_{n}\right\rfloor}\right)$.

Step 3: A component or system will go through multiple states from a normal operating state to a complete fault state in actual engineering. This paper assumes that the Bayesian network model component or system has three states. The fault state of the system node in the BN is defined as fault occurrence, fault non-occurrence, and fault in a fuzzy uncertainty state. Then the system discernment framework is $\Theta=\{$ Fault occurrence, Fault non-occurrence, Fault in fuzzy uncertainty state $\}$, denoted as $\Theta=\left\{A_{1}, A_{2},\left(A_{1}, A_{2}\right)\right\}$, see Table 2. There are also two states of nodes in the BN. The fault state of the node is defined as fault occurrence, fault non-occurrence, then the discernment framework is $\Theta=\{$ Fault occurrence, Fault non-occurrence $\}$, denoted as $\Theta=\left\{A_{1}, A_{2}\right\}$. It is calculated in the same way as the three-state node.

Table 2: Basic creditability distribution


Step 4: Adopt expert knowledge and experience as the body of evidence. The two experts make their judgments about the probability of the state of the various root nodes. Denote their judgments as evidence $Z_{1}, Z_{2}$. Construct the basic credibility distribution function for the root node, see Table 2.

Step 5: According to the D-S synthesis rule, the root node $X_{i}$ failure probability interval was calculated under the joint action of two experts' evidence. Calculating the conflict value according to Eq. (6), and the synthesis results are shown in Table 3.
$k=\sum_{A_{i} \cap A_{j}=\varnothing} s_{1}\left(A_{i}\right) s_{2}\left(A_{i}\right)=m_{1}\left(1-m_{2}-n_{2}\right)+m_{2}\left(1-m_{1}-n_{1}\right)$

Table 3: Data fusion table


The failure probability interval of the root node $X_{i}$ is shown in Eq. (7).
$P\left(X_{i}\right)=[B e l, P l]=\left[\frac{m_{1} m_{2}+m_{1} n_{2}+m_{2} n_{1}}{1-k}, \frac{\left(m_{1}+n_{1}\right)\left(m_{2}+n_{2}\right)}{1-k}\right]$
Step 6: Constrain the root node initial failure probability interval using the HM to obtain the root node probability interval $P\left(X_{i}\right)$ in BN analysis.

In BN, the greater the number of BN nodes, the less likely it is that their failure intervals will require simultaneous bounds. This simultaneous taking of bounds is thus negligible in the reliability analysis of complex systems [22]. Therefore, a Hyper-ellipsoidal domain can be used to deal with Bayesian network node intervals. That is, the uniformly distributed points satisfying Eq. (5) are extracted within the interval box model. The failure probability interval of each root node of the BN is obtained.

And for multidimensional variables, to enhance the efficiency of sampling, sampling can be carried out according to Eqs. (8)-(12).

Introduce vector:
$z=D^{-1} P$
$\left\{\begin{array}{l}z=\left(z_{1}, z_{2}, \ldots, \mathrm{z}_{n}\right)^{\mathrm{T}} \\ D=\operatorname{diag}\left(P_{r}\left(X_{1}\right), P_{r}\left(X_{2}\right), \ldots, P_{r}\left(X_{n}\right)\right) \\ P=\left[P\left(X_{1}\right), P\left(X_{2}\right), \ldots, P\left(X_{n}\right)\right]^{T}\end{array}\right.$
Eq. (5) is converted into:
$\left(z-z_{0}\right)^{T} \cdot\left(z-z_{0}\right) \leq 1$
$z_{0}=\left[\frac{P_{0}\left(X_{1}\right)}{P_{r}\left(X_{1}\right)}, \frac{P_{0}\left(X_{2}\right)}{P_{r}\left(X_{2}\right)}, \ldots, \frac{P_{0}\left(X_{n}\right)}{P_{r}\left(X_{n}\right)}\right]^{T}$
From Eq. (10), generating uniformly distributed random numbers in the hyper-ellipsoid is equivalent to uniform sampling in the unit hypersphere of $\Delta z$ space. The interval probability of the root node shall be uniformly taken within the space hyper-ellipsoid $\Delta z=z-z_{0}$. Let the unit hyper-ellipsoidal coordinate be $\left(r, \theta_{1}, \theta_{2}, \cdots, \theta_{n-1}\right)$, where $r \in[0,1], \theta_{i} \in[0,2 \pi]$, then:

$\Delta z=z-z_{0}=\left[\begin{array}{l}r \cos \theta_{1} \\ r \sin \theta_{1} \cos \theta_{2} \\ \vdots \\ r \sin \theta_{1} \sin \theta_{2} \cdots \sin \theta_{n-3} \cos \theta_{n-2} \\ r \sin \theta_{1} \sin \theta_{2} \cdots \sin \theta_{n-2} \cos \theta_{n-1}\end{array}\right]$
The HM of interval probability $P\left(X_{i}\right)$ of the root node $X_{i}$ of BN is:
$\left[\frac{P\left(X_{i}\right)-P_{0}\left(X_{i}\right)}{P_{r}\left(X_{i}\right)}, \cdots, \frac{P\left(X_{n}\right)-P_{0}\left(X_{n}\right)}{P_{r}\left(X_{n}\right)}\right]^{T} \cdot\left[\frac{P\left(X_{i}\right)-P_{0}\left(X_{i}\right)}{P_{r}\left(X_{i}\right)}, \cdots, \frac{P\left(X_{n}\right)-P_{0}\left(X_{n}\right)}{P_{r}\left(X_{n}\right)}\right] \leq 1$
where $P_{0}\left(X_{i}\right)=\frac{B e l\left(X_{i}\right)+P l\left(X_{i}\right)}{2}$ is the nominal value of $P\left(X_{i}\right) ; P_{r}\left(X_{i}\right)=\frac{-B e l\left(X_{i}\right)+P l\left(X_{i}\right)}{2}$ is the deviation of $P\left(X_{i}\right)$.

According to Eqs. (8)-(12), the interval probability $P\left(X_{i}\right)$ of the root node is:

$$
\left\{\begin{array}{c}
P\left(X_{1}\right)=P_{r}\left(X_{1}\right) r \cos \theta_{1}+P_{0}\left(X_{1}\right) \\
P\left(X_{2}\right)=P_{r}\left(X_{2}\right) r \sin \theta_{1} \cos \theta_{2}+P_{0}\left(X_{2}\right) \\
\vdots \\
P\left(X_{n-1}\right)=P_{r}\left(X_{n-1}\right) r \sin \theta_{1} \ldots \sin \theta_{n-2} \sin \theta_{n-1}+P_{0}\left(X_{n-1}\right) \\
P\left(X_{n}\right)=P_{r}\left(X_{n}\right) r \sin \theta_{1} \ldots \sin \theta_{n-2} \sin \theta_{n-1}+P_{0}\left(X_{n}\right)
\end{array}\right.
$$

Step 7: The HE-BN is used for forward calculation, and the failure probability interval of the leaf node $T$ with fault state $T_{q}$ is obtained as shown in (15).

$$
\begin{aligned}
P\left(T=T_{q}\right)= & \sum_{\substack{x_{1}, x_{2}, \ldots, x_{m} \\
y_{1}, y_{2}, \ldots, y_{m}}} P\left(x_{1}, x_{2}, \ldots, x_{n} ; y_{1}, y_{2}, \ldots, y_{m} ; T=T_{q}\right) \\
= & \sum_{\lambda(T)} P\left(T=T_{q} \mid \lambda(T)\right) \times \sum_{\lambda\left(y_{1}\right)} P\left(y_{1} \mid \lambda\left(y_{1}\right)\right) \sum_{\lambda\left(y_{2}\right)} P\left(y_{2} \mid \lambda\left(y_{1}\right)\right) \times \\
& \cdots \times \sum_{\lambda\left(y_{m}\right)} P\left(y_{m} \mid \lambda\left(y_{m}\right)\right) P\left(x_{1}^{\theta_{1}}\right) P\left(x_{2}^{\theta_{2}}\right) \cdots P\left(x_{n}^{\theta_{n}}\right)
\end{aligned}
$$

where $P\left(x_{i}^{\theta_{i}}\right)$ is the interval probability of fault occurs when the fault state of the root node $x_{i}$ is $x_{i}^{\theta_{i}}$.
Step 8: When the fault state of the leaf node is known to be $T_{q}$, the posterior probability $P\left(x_{i}=\right.$ $\left.x_{i}^{\theta_{i}} \mid T=T_{q}\right)$ of the root node $x_{i}$ with fault state $x_{i}{ }^{\theta_{i}}$ is obtained as Eq. (16).

$$
\begin{aligned}
P\left(x_{i}=x_{i}^{\theta_{i}} \mid T=T_{q}\right)= & \frac{P\left(x_{i}=x_{i}^{\theta_{i}}, T=T_{q}\right)}{P\left(T=T_{q}\right)}=\frac{\sum_{x_{1}, x_{2}, \ldots, x_{n}} P\left(x_{1}, \ldots, x_{i}=x_{i}^{\theta_{i}} \ldots x_{n}, T=T_{q}\right)}{P\left(T=T_{q}\right)} \\
= & \frac{P\left(x_{i}^{\theta_{i}}\right)}{P\left(T=T_{q}\right)} \sum_{x_{1}, x_{2}, \ldots, x_{n}} P\left(T=T_{q} \mid x_{1}, \ldots, x_{i}=x_{i}^{\theta_{i}} \ldots x_{n}\right) \cdot P\left(x_{i}^{\theta_{1}}\right) \\
& \left.\ldots P\left(x_{i-1}^{\theta_{i-1}}\right) P\left(x_{i+1}^{\theta_{i+1}}\right) \ldots P\left(x_{n}^{\theta_{n}}\right)\right.
\end{aligned}
$$

where $P\left(x_{i}=x_{i}^{\theta_{i}}, T=T_{q}\right)$ is the joint probability of the root node $x_{i}$ with the fault state $x_{i}{ }^{\theta_{i}}$ and the leaf node $T$ with the fault state $T_{q}$.

# 4 Application Case Analysis 

### 4.1 Multistate Series-Parallel Systems Reliability Analysis

The multistate series-parallel system is shown in Fig. 4. Construct its T-S fault tree as shown in Fig. 5a, where G1 denotes "AND" gates. G2 and G3 denote "OR" gates. The Fault occurrence state, Fault in fuzzy uncertainty state, and Fault non-occurrence state of the system and components are denoted by $A_{1},\left(A_{1}, A_{2}\right)$, and $A_{2}$. The failure rate of the component $X_{i}(i=1,2,3,4)$ in the Fault occurrence state is $5.0 \times 10^{-5} / h, 1.0 \times 10^{-5} / h, 1.5 \times 10^{-5} / h$, and $1.2 \times 10^{-5} / h$, respectively. The failure rate of components in the Fault in fuzzy uncertainty state is $9.0 \times 10^{-5} / h, 1.0 \times 10^{-4} / h, 2.8 \times 10^{-5} / h$, and $3.6 \times 10^{-5} / h$, respectively.
![img-3.jpeg](img-3.jpeg)

Figure 4: Multistate series-parallel systems
![img-4.jpeg](img-4.jpeg)
(a) Multi-state series-parallel system T-S FTA Model
![img-5.jpeg](img-5.jpeg)
(b) Multi-state series-parallel system Bayesian Network

Figure 5: Reliability model for a multi-state series-parallel system
The T-S FTA of the multistate series-parallel system was converted into a BN as shown in Fig. 5b. The T-S gate rules are converted into a conditional probability table. For the G1 gate, see Table 4. Conditional probability tables are the same for G2 and G3, see Table 5. Table 4 rule 1 indicates that under the condition that the S 1 state is $A_{1}$, S 2 state is $A_{1}$, the probability of S 0 state $A_{1}$ is 1 and the probability of $\left(A_{1}, A_{2}\right)$ and $A_{2}$ is 0 . Other rules can be followed in this way.

First, the multistate series-parallel system is analyzed by the traditional Bayesian network method. Based on the conditional probability table and the exact failure rate of each root node, the probability of the Fault occurrence state of the leaf node is calculated to be $P\left(S 0=A_{1}\right)=298299.7969 \times 10^{-14}$, the probability of the Fault in fuzzy uncertainty state is $P\left(S 0=\left(A_{1}, A_{2}\right)\right)=738060.0823 \times 10^{-14}$, and the probability of the Fault non-occurrence state is $P\left(S 0=A_{2}\right)=999999.9963 \times 10^{-6}$. The multistate series-parallel system was analyzed using the interval Bayesian network and the method proposed in this paper. Table 6 shows the failure rates at each root node.

Table 4: Conditional probability table for node S0


Table 5: Conditional probability table for nodes S1 and S2


Table 6: Root node failure rate


Probability at each state of leaf nodes was obtained by the Bayesian inference algorithm. The comparative analysis results of the traditional Bayesian network, the interval Bayesian network, and the method proposed in this paper are shown in Table 7.

The system failure rate is assumed exponentially distributed. The reliability curves of the multistate series-parallel system under the three methods are obtained as shown in Fig. 6.

Table 7: Comparison of leaf node failure rate results


![img-6.jpeg](img-6.jpeg)

Figure 6: Multistate series-parallel system reliability curves
As can be seen from Table 7 and Fig. 6, the traditional Bayesian analysis results using exact failure rates are within the HE-BN method interval results. Also, the length of the analysis result interval for HE-BN is smaller and closer to the exact value than the interval Bayesian results. It proves that the present method can solve the problem of insufficient failure data. It can also make up for the relatively conservative calculation results of the Interval model, which is more in line with engineering practice.

Using the HE-BN method, the posterior probability of each root node is calculated by Eq. (16) when the multistate series-parallel system is in the fault occurrence state. The posterior probability results are sorted by the interval number sorting method based on the order relationship. For the interval number $A\left[a^{-}, a^{+}\right]$, define the measurement $m_{b}(a)=(1-\theta) a^{-}+\theta a^{+}$of the interval numbers, $\theta \in[0,1]$. The larger the value of $m_{b}(a)$, the larger the corresponding interval number. After sorting them by the interval number sorting method [33], a comparison with traditional Bayesian results is shown in Fig. 7.

As can be seen from Fig. 7, the method proposed in this paper is consistent with the results of the posterior probability ranking of the root nodes obtained from the traditional Bayesian method. The results are $\mathrm{X} 1>\mathrm{X} 3>\mathrm{X} 4>\mathrm{X} 2 . \mathrm{X} 1$ is the most important and X 2 is the least important, which corresponds to the actual situation. The failure rate of component X 1 is the highest and the failure rate of X 2 is the lowest, which proves the feasibility of this method.

![img-7.jpeg](img-7.jpeg)

Figure 7: Comparing posterior probability results for multistate series-parallel system root nodes

# 4.2 Shibata-Type Coupler System Reliability Analysis 

The Shibata-type coupler consists of a coupler head, coupler knuckle, uncoupling air cylinder, coupler body, and coupler yoke [34]. The specific structure of the Shibata-type coupler is shown in Fig. 8.
![img-8.jpeg](img-8.jpeg)

Figure 8: Shibata-type coupler
Note: 1-Coupler head; 2-Coupler tongue; 3-Coupler body; 4-Air pipeline; 5-Horizontal pin; 6-Frame joint; 7-Vertical pin; 8 -Front baffle; 9 -Buffer frame; 10 -Rubber buffer; 11-Rear baffle.

As can be seen from Fig. 8, the structure of the Shibata-type coupler can be divided into two parts: the coupler and the buffer. The coupler body includes a coupler head, coupler body, coupler yoke, and other structures. The buffer is composed of the horizontal pin, vertical pin, frame joint, rubber pile, baffle, buffer frame, and bracket.

When two couplers are attached, the convex cone of one of the couplers is inserted into the concave cone of the body of the other coupler. The side of the convex cone presses against the tongue of the coupler in the concave cone and turns $40^{\circ}$ counterclockwise. When the two couplers are fully connected, the convex cone is no longer pressing on the latch and the latch returns to the closed position. The automatic coupling is completed. To de-couple, the driver operates the uncoupling valve or manually pushes the uncoupling lever to turn the coupler tongue counterclockwise to the unlocked position. The two couplers can then be released.

The T-S FTA model is constructed based on the failure of the Shibata-type coupler system as the top event, as shown in Fig. 9. And transformed into a BN as shown in Fig. 10 according to the method in Fig. 3. The event names represented by each node are shown in Table 8.

![img-9.jpeg](img-9.jpeg)

Figure 9: T-S FTA module of Shibata-type coupler system
![img-10.jpeg](img-10.jpeg)

Figure 10: BN of Shibata-type coupler system

Table 8: Names of Shibata-type coupler system nodes


The coupler system discernment framework is $\Theta=\{$ Fault occurrence, Fault non-occurrence, Fault in fuzzy uncertainty state $\}$, which is recorded as $\Theta=\left\{A_{1}, A_{2},\left(A_{1}, A_{2}\right)\right\}$. Using the root node X 1 as an example, calculate the initial failure probability interval. The expert evaluation data for root node X1

of the coupler system is shown in Table 9. Substitute it into Eqs. (6) and (7) to obtain the evidence conflict value $k_{1}$ and the initial failure probability interval $P\left(X_{1}\right)$ of root node X 1 .

Table 9: Expert evaluation data of root node X1


$k_{1}=0.00000929 \times 0.99997089+0.00001345 \times 0.99997822=41.5998 \times 10^{-7}$
$P\left(X_{1}\right)=[B e l, P l]$

$$
\begin{aligned}
= & {\left[\frac{0.00001345 \times 0.00000929+0.00001345 \times 0.00001249+0.00000929 \times 0.00001566}{1-4.15998 \times 10^{-6}}\right.} \\
& \left.\frac{(0.00001345+0.00001566) \times(0.00000929+0.00001249)}{1-4.15998 \times 10^{-6}}\right] \\
= & {\left[4.3843 \times 10^{-10}, 6.3403 \times 10^{-10}\right] }
\end{aligned}
$$

The initial failure probability interval for each root node is obtained by the same calculation as above. The root node failure probability interval after the HM constraint is obtained from Eq. (14), See Table 10 for part of this.

Table 10: Failure probability interval of root nodes


The T-S gate rule of the coupler system is derived from historical data and expert experience. The conditional probability table of the BN is obtained according to the method in Fig. 3. The conditional probability table for the intermediate node Y2 is shown in Table 11 as an example. Where rule 1 indicates that under the condition that X28 has a fault state of $A_{2}$ and X29 has a fault state of $A_{2}$, the possibility that Y2 fault state being $A_{2}$ is 1 , the possibility that Y 2 is $\left(A_{1}, A_{2}\right)$ and $A_{1}$ is 0 . Other rules can be used in this way.

Table 11: Conditional probability table of intermediate node Y2


According to the failure probability interval of X28 and X29 and Table 11, the failure probability interval of Y2 in various states can be obtained by using Eq. (15) as follows:

$$
\begin{aligned}
P\left(y_{2}-A_{1}\right)= & \sum_{x_{28}, x_{29}} P\left(x_{28}, x_{29} ; y_{2}=A_{1}\right)=\sum_{x_{28}, x_{29}} P\left(y_{2}=A_{1} \mid x_{28}, x_{29}\right) \times P\left(x_{28}\right) \times P\left(x_{29}\right) \\
= & {\left[1.3611 \times 10^{-12}, 1.4528 \times 10^{-12}\right] } \\
P\left(y_{2}=\left(A_{1}, A_{2}\right)\right)= & \sum_{x_{28}, x_{29}} P\left(x_{28}, x_{29} ; y_{2}=\left(A_{1}, A_{2}\right)\right) \\
= & \sum_{x_{28}, x_{29}} P\left(y_{2}=\left(A_{1}, A_{2}\right) \mid x_{28}, x_{29}\right) \times P\left(x_{28}\right) \times P\left(x_{29}\right) \\
= & {\left[9.1862 \times 10^{-13}, 9.6967 \times 10^{-13}\right] } \\
P\left(y_{2}-A_{2}\right)= & \sum_{x_{28}, x_{29}} P\left(x_{28}, x_{29} ; y_{2}=A_{2}\right)=\sum_{x_{28}, x_{29}} P\left(y_{2}=A_{2} \mid x_{28}, x_{29}\right) \times P\left(x_{28}\right) \times P\left(x_{29}\right) \\
= & {\left[99999999.9998 \times 10^{-8}, 99999999.9998 \times 10^{-8}\right] }
\end{aligned}
$$

The above results show that Y2 has a small probability of a fault and a fault-indeterminate state and a high probability of no fault. This is consistent with the actual situation. Based on the constructed BN, the probability intervals of failure for leaf node T with fault states $A_{1},\left(A_{1}, A_{2}\right)$, and $A_{2}$ were found using the method and combined with the conditional probability tables of the nodes. The reliability curve of the hook system can be obtained as shown in Fig. 11. As can be seen in Fig. 11, the reliability of the coupler system is in the range $[0.7873,0.8505]$ after $1 \times 10^{8} \mathrm{~h}$ of operation. Based on the results of the reliability assessment of the coupler system, a basis can be provided for subsequent design and maintenance work.

$P\left(T=A_{1}\right)=\left[1.6663 \times 10^{-10}, 1.4425 \times 10^{-9}\right]$
$P\left(T=\left(A_{1}, A_{2}\right)\right)=\left[1.0585 \times 10^{-9}, 1.4525 \times 10^{-9}\right]$
$P\left(T=A_{2}\right)=\left[99999.9997 \times 10^{-5}, 99999.9998 \times 10^{-5}\right]$
![img-11.jpeg](img-11.jpeg)

Figure 11: Coupler system reliability curve
The posterior probability of the root node $x_{i}$ for leaf node T with fault states $A_{1}$ and $\left(A_{1}, A_{2}\right)$ can be calculated according to Eq. (16). After sorting them by the interval number sorting method [33], the posterior probability is shown in Fig. 12.
![img-12.jpeg](img-12.jpeg)

Figure 12: Posterior probability of root nodes
As can be seen from Fig. 12, when the Shibata-type coupler system fails, the root node posterior probabilities are ordered as follows:

X2 $>$ X16 $>$ X9 $>$ X10 $>$ X1 $>$ X3 $>$ X17 $>$ X4 $>$ X15 $>$ X14 $>$ X20 $>$ X21 $>$ X24 $>$ X13 $>$ X11 $>$ X12 $>$ X18 $>$ X22 $>$ X7 $>$ X27 $>$ X25 $>$ X29 $>$ X23 $>$ X19 $>$ X5 $>$ X6 $>$ X8 $>$ X28 $>$ X26.

When the fault of the Shibata-type coupler system is in a fuzzy uncertainty state, the posterior probability of the root node is sorted as follows:

X16>X2>X1>X9>X10>X17>X3>X4>X15>X14>X20>X24>X21>X13>X11>X12>X18>X22 $>$ X7>X27>X25>X29>X23>X19>X5>X6>X8>X26>X28.

A comparison of the failure rates from CRH2 and CRH30A (L) rolling stock operational data [35] with the results obtained from a reliability analysis method based on T-S FTA and HE-BN is shown in Fig. 13.
![img-13.jpeg](img-13.jpeg)

Figure 13: Result comparison
It can be seen from Fig. 13 that in the operation data of CRH2 and CRH380A (L) multiple units, the failure rate of key components of the Shibata-type coupler system is ranked as follows: air duct connector, coupler body, uncoupling air cylinder, electrical connector, horizontal and vertical pin, buffer frame, coupler lock, coupler tongue, uncoupling lever. The results are consistent with the sequence when the coupler system fault state is $A_{1}$ in the reliability analysis method of the T-S FTA and HE-BN, which verifies the correctness and feasibility of the method.

The greater the posterior probability, the greater the impact of the component on the system failure, which is the weak link that the system should focus on. From the analysis results in Figs. 12 and 13, it can be seen that when the coupler system is in a $\left(A_{1}, A_{2}\right)$ state, coupler yoke pin fracture and coupler yoke pin bolt fracture have the greatest impact on the system. This is followed by the Air pipeline leak and uncoupling air cylinder failure. Therefore, these components should be inspected and repaired first when the system is in a half-fault state or has reached the preventive maintenance time point to ensure longer system life. When the system is in the $A_{1}$ fault state, the Air pipeline leak has the greatest impact on the system, followed by the Coupler yoke pin fracture, coupler yoke pin bolt fracture, and the Coupler body crack, and the impact of the Non-standard operation of the maintenance personnel is the smallest.

# 4.3 A Type of Double-Row Tapered Roller Bearing System Reliability Analysis 

The structure of a bogie bearing for a moving train is shown in Fig. 14 and includes the inner ring, the outer ring, the rolling element, and the cage. The inner ring fits with the shaft and rotates

with it. The outer ring fits into the bearing housing and plays a supporting role. The rolling element is evenly distributed between the inner ring and outer ring with the help of the cage. The bogie axle box bearing supports the static load of the vehicle and the longitudinal and transverse impact of the vehicle in operation and other dynamic loads, and its failure mode can be classified as rust, discoloration, surface plastic deformation, fatigue spalling and pitting failure, cracks and defects in five categories.
![img-14.jpeg](img-14.jpeg)

Figure 14: Bearing structure
A T-S fault tree with bearing failure as the top event was constructed for a type of double-row tapered roller bearing used in the bogie of a moving train, as shown in Fig. 15. It is transformed into a BN as shown in Fig. 16. The meanings represented by the symbols in Fig. 16 are shown in Table 12.
![img-15.jpeg](img-15.jpeg)

Figure 15: Bearing system T-S fault tree
![img-16.jpeg](img-16.jpeg)

Figure 16: Bearing system Bayesian network

Table 12: Bearing system node names


Define the identification framework of the bearing system as $\Theta=\{$ Fault occurrence, Fault in fuzzy uncertainty state, Fault non-occurrence\}, denoted as $\Theta=\left\{A_{1},\left(A_{1}, A_{2}\right), A_{2}\right\}$. Substitute the expert evaluation data of the root nodes of the bearing Bayesian network into Eqs. (6) and (7) to obtain the initial failure probability interval of each root node. The failure probability interval of the root node after the HM constraint is obtained from Eq. (14) and is shown in Table 13.

Table 13: Failure probability interval of root nodes


The T-S gate rule for the bearing system is derived from historical data and expert experience, and the conditional probability table for the BN is obtained according to the method in Fig. 3. Take the conditional probability table of the intermediate node M1 as an example, see Table 14.

Based on the constructed BN and the conditional probability tables of the nodes, the probability intervals of failure for leaf node T with fault states $A_{1},\left(A_{1}, A_{2}\right)$, and $A_{2}$ were found. A reliability curve for the bearing system can be obtained, as shown in Fig. 17. As can be seen in Fig. 17, the bearing system reliability interval is $[0.8793,0.8975]$ after 1954 h of system operation, and the reliability decreases sharply within $40,000 \mathrm{~h}$ of operation. Based on the results of the reliability assessment of the bearing system, a basis for subsequent design and maintenance work can be provided.
$P(T=0)=\left[9.9987 \times 10^{-1}, 9.9989 \times 10^{-1}\right]$
$P(T=0.5)=\left[5.4848 \times 10^{-5}, 6.5295 \times 10^{-5}\right]$
$P(T=1)=\left[5.5327 \times 10^{-5}, 6.5835 \times 10^{-5}\right]$

Table 14: Conditional probability table of intermediate node M1


![img-17.jpeg](img-17.jpeg)

Figure 17: Bearing system reliability curve
The posterior probability of the root node $x_{i}$ for leaf node T with fault states $A_{1}$ and $\left(A_{1}, A_{2}\right)$ can be calculated according to Eq. (16). After sorting them by the interval number sorting method [33], they are shown in Fig. 18.
![img-18.jpeg](img-18.jpeg)

Figure 18: Posterior probability of the bearing system root nodes

As can be seen from Fig. 18, when the bearing system failure occurs, the root node posterior probability ranking is as follows: $\mathrm{X} 1>\mathrm{X} 2>\mathrm{X} 11>\mathrm{X} 10>\mathrm{X} 9>\mathrm{X} 4>\mathrm{X} 7>\mathrm{X} 6>\mathrm{X} 8>\mathrm{X} 5>\mathrm{X} 3$.

When the failure of the bearing system is in a state of fuzzy uncertainty, the root node posterior probabilities are ordered as follows: $\mathrm{X} 2>\mathrm{X} 1>\mathrm{X} 11>\mathrm{X} 10>\mathrm{X} 9>\mathrm{X} 4>\mathrm{X} 7>\mathrm{X} 6>\mathrm{X} 8>\mathrm{X} 5>\mathrm{X} 3$.

As can be seen in Fig. 18, X1,X2, and X8 are of greater importance. The main faults of these three basic events are poor lubrication, seal failure, and excessive impact loads. Therefore, the following improvement measures can be prioritized to improve the reliability of this bearing system.

Strengthen and improve the bearing lubrication technology, and bearing seal device maintenance, to ensure that the bearings are subject to good lubrication. In bearing maintenance, develop on-site applicable maintenance and cleaning cycles, improve the operational level of maintenance of bearings, improve maintenance conditions, and ensure the quality of bearing maintenance. In terms of bearing design, improve the structure of the bearing to increase the bearing's impact resistance and improve the internal force condition of the bearing.

# 5 Conclusions 

This paper proposes a system reliability analysis method based on T-S FTA and HE-BN. Combining the advantages of T-S FTA and BN, directed acyclic graphs and conditional probability tables of BN are constructed through T-S gates and T-S rules. Evidence theory and the HM are applied to obtain the fault interval of the system BN root node. The fault interval of the system is obtained by forward calculation based on the directed acyclic graph, the conditional probability table, and the fault interval of the root node. The reverse calculation is then carried out to identify the weak points of the system. The following conclusions were obtained:
(1) Constructing directed acyclic graphs and conditional probability tables for BN by T-S gates and T-S rules. Combines the advantages of simple T-S FTA modeling and easy BN computation. The disadvantage is solved that the BN constructed by traditional fault trees cannot describe the fuzzy logical relationship between nodes. It also solves the shortcomings of the T-S FTA which is complex in operation and cannot reason in both directions. The modeling and computational efficiency of the coupler system reliability model are improved.
(2) The D-S evidence theory is used to fuse expert experience to obtain the failure probability interval for the BN root nodes. The HM is introduced to define the range of values of the uncertainty probability. It can effectively deal with the problems of insufficient failure data and uncertainty of failure degree. And it solves the problem that the calculation results are relatively conservative when the traditional fuzzy interval model describes the uncertain failure mechanism and data. It is more in line with engineering practice.
(3) The application of the proposed method to a real engineering case study shows that the proposed method can establish a reliability model that is easy to calculate and fully reflects the failure characteristics of a complex structural system by integrating the failure modes and causes of the system when dealing with the reliability analysis of a multi-state complex system. It can accurately identify the weak points of the system under the uncertainty and incompleteness of the data.

In addition, the system reliability analysis method based on the T-S FTA and HE-BN proposed in this paper can be applied to other subsystems of rail vehicles, aerospace, and other fields. It can quantify the reliability level of the system, effectively identify the weak links, and has generality. However, this paper only considers the structural complexity of the system, the uncertainty and

incompleteness of the data, and the polymorphic nature of the degree of component failure. A reliability analysis method that considers the dynamic characteristics of the system in operation and fault correlation could be the next step in the research.

Acknowledgement: Thanks to the help of four anonymous reviewers and journal editors, the logical organization and content quality of this paper have been improved.

Funding Statement: This work is supported by the National Natural Science Foundation of China (51875073).

Author Contributions: The authors confirm contribution to the paper as follows: study conception and design: Xia Q., Li Y.; data collection: Wang Y.; analysis and interpretation of results: Xia Q., Zhang D.; draft manuscript preparation: Xia Q., Li Y. All authors reviewed the results and approved the final version of the manuscript.

Availability of Data and Materials: All data generated or analysed during this study are included in this published article.

Conflicts of Interest: The authors declare that they have no conflicts of interest to report regarding the present study.
