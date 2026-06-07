# Article 

## Reliability Analysis of High-Voltage Drive Motor Systems in Terms of the Polymorphic Bayesian Network

Weiguang Zheng ${ }^{1,2}$ (D), Haonan Jiang ${ }^{2,3, *}$ (D), Shande $\mathrm{Li}^{4, *}$ (D) and Qiuxiang $\mathrm{Ma}^{3}$

## check for updates

Citation: Zheng, W.; Jiang, H.; Li, S.; Ma, Q. Reliability Analysis of HighVoltage Drive Motor Systems in Terms of the Polymorphic Bayesian Network. Mathematics 2023, 11, 2378. https://doi.org/10.3390/math11102378

Academic Editor: Manuel Alberto M. Ferreira

Received: 16 April 2023
Revised: 13 May 2023
Accepted: 17 May 2023
Published: 19 May 2023

## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 School of Mechanical and Automotive Engineering, Guangxi University of Science and Technology, Liuzhou 545616, China; weiguang.zheng@foxmail.com
2 School of Mechanical and Electrical Engineering, Guilin University of Electronic Technology, Guilin 541004, China
3 Commercial Vehicle Technology Center, Dong Feng Liuzhou Automobile Co., Ltd., Liuzhou 545005, China; maqv@dfizm.com
4 State Key Laboratory of Digital Manufacturing Equipment and Technology, School of Mechanical Science and Engineering, Huazhong University of Science and Technology, Wuhan 430074, China

* Correspondence: hn_jianghn@126.com (H.J.); lishande@hust.edu.cn (S.L.)

Abstract: The reliability of the high-voltage drive motor system for pure electric commercial vehicles is in premium demand. Conventional reliability based on fault tree analysis methods is not suitable for the quantitative assessment of polymorphic systems. As an example of a pure electric commercial vehicle, this paper combines polymorphic theory and Bayesian theory to establish a polymorphic Bayesian network model of a high-voltage drive motor system in terms of a polymorphic fault tree and to quantitatively judge the system. The polymorphic Bayesian network (BN) model can accurately depict the high-voltage drive motor system's miscellaneous fault states and solve the top event's probability in every state, also solving the system and drawing the consistent conclusion that the presence of abrasive particles, high-temperature gluing, moisture, and localized high temperatures are the system's weak links by solving the critical importance, probabilistic importance, and posterior probability of the underlying event, which provides a theoretical reference for structure contrive optimization and fault diagnosis. This is extremely important in terms of improving pure electric commercial vehicles' high-voltage drive motor systems.

Keywords: quantitative assessment; polymorphic fault tree; polymorphic Bayesian network; probability importance; critical importance

MSC: 60A05

## 1. Introduction

Energy and environmental issues have worsened due to increased vehicle ownership. At current, major domestic and foreign manufacturers have focused their attention on energy-saving, environmentally friendly, and high-capacity pure electric commercial vehicles. According to statistical analysis of the GGII (Gao Gong Industrial Research Institute), from January to November 2022, domestic sales of new energy heavy commercial vehicles amounted to more than 19,000 units, a year-on-year increase of $155 \%$, accounting for $6.2 \%$ of the entire heavy commercial vehicle market. In addition, for different types of new energy commercial vehicles, the proportion of pure electric heavy-duty commercial vehicles is also the largest. While pure electric commercial vehicles are being promoted, the number of accidents caused by the reliability of high-voltage drive motor systems is increasing every year; each accident is a harsh reality for the reliability of the high-voltage electrical systems of pure electric commercial vehicles. The complex operating conditions of pure electric commercial vehicles require drive motors that can perform frequent start-stop and acceleration-deceleration characteristics and work reliably in harsh environments.

Therefore, high-voltage drive motor systems have high requirements for reliability, cooling performance, energy density, adaptability, etc.

Reliability analysis techniques have achieved extensive use in the expanding area of engineering. Watson et al. first proposed fault tree analysis (FTA) [1]. Following this, Hasse et al. [2] studied and generalized the FTA algorithm, which made the reliability analysis method not limited to a single FTA. Cao et al. [3] combined fault tree analysis and binary decision diagram (BDD) methods which solved the problem of "combinatorial explosion" results by applying fault tree analysis methods only in fault diagnosis. Li et al. [4] put forward a decision tree based on the method for line fault cause analysis by mining fault causes' time distribution law and the hierarchical structure from fault history, which improved the analysis speed, provided more detailed and accurate conclusions, and illustrated the effectiveness of the algorithm by providing examples. Jiao M et al. [5] transformed the fault tree (FT) into a state transition diagram (STD) to simplify the FT. Multiple fault combinations can be diagnosed and unnecessary operations can be reduced by using the converted STD to handle intermediate and basic events separately when performing fault diagnosis. Waghen K et al. [6] suggested multi-level interpretable logic tree analysis (MILTA) for the fault-level causal analysis of complex systems based on typical fault datasets.

As the complexity of the analysis system becomes progressively greater, the restrictions of traditional FTA methods for the ambiguity of the occurrence of base events are revealed. Using fuzzy probabilities instead of exact probabilities, fuzzy fault tree analysis (FFTA) solves probabilistic uncertainty in fault tree analysis. It was initially put forward by Tanaka et al. [7]. By creating a FFT model for excavation workings and gas explosion in coal mining, Shi et al. [8] determined the FT's minimum path and minimum cut set and evaluated the significance of the fault tree configuration. The probability of gas explosion is calculated, which provides a theoretical basis for the preparation and prevention of coal mine accidents. Nadjafi et al. [9] put forward a fault tree reliability analysis method for complex engineering systems based on fuzzy time-to-failure (FTTF), which showed significant advantages of high accuracy and low workload in aerospace emergency detection systems. By introducing a fuzzy structured element-based method, Cui et al. [10] used the discrete space fault tree (DSFT) to establish an element discrete space fault tree (EDSFT). The element-based EDSFT method can maintain the original fault data's distribution features and lay the groundwork for analyzing large error data, making it appropriate for system reliability analysis when large fault data and multiple factors are at play. Li et al. [11] performed a gas turbine fuel system fuzzy fault tree analysis by combining fuzzy information with the FT from staff feedback to improve the reliability of some components of the system. The theoretical basis was provided for subsequent system design and performance improvement. Yu [12] analyzed the weakest t-norm $\left(T_{w^{\prime}}\right)$ to propose an FFT based on this and derived reliable probability through the evaluation of domain experts. This method is combined with the traditional submarine pipeline leakage failure probability risk assessment method. The results showed that the method has good validity and applicability.

In the practical field of engineering, the state of the system and the bottom events also show polymorphism. In addition, the reliability analysis of intricate polymorphic systems cannot be solved using the straightforward fuzzy fault tree analysis method. Belief networks (BNs) were first introduced by Pearl [13] in 1986 and have been used to deal with uncertain knowledge and polymorphism problems in subsequent developments. Portinale and Bobbio [14] performed a reliability analysis of a digital control system using Bayesian networks (BNs). Mahadevan et al. [15] compared traditional reliability analysis methods with Bayesian networks for parallel and series systems and verified their effectiveness. Liu [16] presented a fuzzy reliability estimation approach in terms of a belief network and T-S (Takagi-Sugeno) FT to evaluate the fuzzy reliability of the injection system. The method solved the problems of difficulty in constructing conditional probabilities for Bayesian network nodes, the difficulty of obtaining accurate fault probability data, and the inability of T-S fault tree analysis methods to reason backwards and provided a basis for improving

system reliability and error judgment. Fuzzy mathematical principles and grey system principles were introduced into Bayesian networks by Wang et al. [17], who established a grey fuzzy Bayesian network model and proposed a reliability analysis method for intricate ambiguity multi-state systems with uncertainty affiliation functions and interval eigenvalues. Feng et al. [18] developed a crane reliability analysis model based on BNs under expert evaluation and verified the validity. Guo et al. [19] used a discrete Bayesian network to present a dynamic system reliability analysis model with common cause failure. A digital safety level distributed control system of a nuclear power plant was applied to verify the validity of this model. Li et al. [20] used BNs to analyze offshore floating wind turbines' reliability to predict the average failure time and system failure rate. The failure rate's prediction error is about one-third of the FTA's prediction error. Bayesian networks are capable of handling uncertainty information. The root nodes in a polymorphic Bayesian network can represent discrete and continuous variables of two or more states, the conditional probability distribution between neighboring nodes can represent deterministic and uncertain logical relationships between variables, and the leaf nodes can be used to represent the top-of-failure events of the system, which is a great advantage in solving probabilistic problems of uncertainty. The research based on the reliability method of polymorphic systems has achieved remarkable results in both theoretical innovation and practical engineering application, and after continuous development, the reliability analysis of polymorphic systems has been used in various engineering fields, e.g., the fatigue analysis of mechanical parts [21,22], rail transit systems [23], mechanical structures and systems [24,25], risk assessment [26], and medical systems [27].

Of the many factors of the high-voltage drive motor system's degraded-state mode, aging, corrosion, and deformation are multi-state events. When a common cause failure occurs between nodes, it leads to a complex Bayesian network structure, and it is too difficult to calculate the failure probability of the target nodes using Bayesian inference algorithms. Consequently, taking into account the logic between events and the polymorphic nature of the high-voltage drive motor system of pure electric commercial vehicles, only the reliability analysis of the system using polymorphic Bayesian networks under non-common cause failure is considered.

This work takes a pure electric commercial vehicle's high-voltage drive motor system as the case study and applies the theory of polymorphic and Bayesian networks to establish a high-voltage drive motor system polymorphic Bayesian network model. The probabilities solved for the top event being in normal, degradation, and failure states are 0.9841 , 0.00712 , and 0.00878 , respectively. In addition, the probability of solved for the system's reliability is 0.9913 . From the bottom event's critical importance, probability importance, and the posterior probability of the presence of abrasive particles, high-temperature gluing, moisture, and localized high temperatures as critical events affecting the system failure were known.

In this paper, the following work has been accomplished: (1) the system's FFT is built by taking a pure electric commercial vehicle's high-voltage drive motor system as the case study. The transformation relationship between the Bayesian network and the FT is used to establish the system's polymorphic Bayesian network model, and the occurrence probability in every state is solved by Bayesian network inference. (2) Through quantitative analysis, the system's weakest links were identified from the view of the bottom event's critical importance, probability importance and the posterior probability.

The polymorphic Bayesian network analysis' basic principles are described in detail in Section 2 of this paper. Section 3 establishes and analyzes the high-voltage drive motor system polymorphic Bayesian network model for pure electric commercial vehicles. Section 4 solves the polymorphic Bayesian network model of the high-voltage drive motor system. Lastly, Section 5 is the conclusion, which summarizes the system reliability analysis in the previous chapters.

# 2. Reliability Analysis Methods in Terms of the Polymorphic Bayesian Networks 

### 2.1. The Method of FTA

FTA [28] is the reliability analysis method that analyses all probable reasons for system failure and draws the "tree", identifies the fundamental causes that lead to system breakdown through qualitative analysis, and calculates the top event's failure probability and the basic events' importance through quantitative analysis.

### 2.1.1. Top Event's Probability

The top event's probability is solved by quantitative analysis based on the structure function and the bottom event's occurrence probability. Assume that $P\left(X_{i}\right)(i=1,2, \ldots, n)$ is the bottom event's occurrence probability $X_{i}(i=1,2, \ldots, n)$. When the basic events' occurrence is mutually independent, the probabilities of the top events under the "OR" and "AND" gates are as follows.

The probability of at least one basic event happening under the "OR" gate condition is:

$$
P_{1, i}=1-\left\{\left[1-P\left(X_{1}\right)\right] \times\left[1-P\left(X_{2}\right)\right] \times \ldots \times\left[1-P\left(X_{n}\right)\right]\right\}=1-\prod_{i=1}^{n}\left[1-P\left(X_{i}\right)\right]
$$

where $P_{1, i}$ is the probability of at least one basic event happening, and $P\left(X_{i}\right)(i=1,2, \ldots, n)$ is the bottom event's occurrence probability.

The basic events' probability occurring in simultaneity under the "AND" gate condition is:

$$
P_{i \uparrow}=P\left(X_{1}\right) \times P\left(X_{2}\right) \times \ldots \times P\left(X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i}\right)
$$

where $P_{i \uparrow}$ is the probability of $n$ basic events occurring simultaneously.

### 2.1.2. Reliability of the System

From classical reliability theory, the formula for the relationship between the failure rate and reliability is:

$$
R(t)=\exp \left(-\int_{0}^{t} \lambda(t) d t\right)
$$

While $\lambda(t)$ is a constancy, i.e., $\lambda(t)=\lambda$, and the system operating time $t$ tends to unit 1 . The system's reliability is:

$$
R(t) \approx \exp (-\lambda)
$$

From the fact that reliability and unreliability are opposing events, the formula between unreliability and the failure rate that can be obtained from Equation (4) is:

$$
F(t)=1-R(t)=1-\exp (-\lambda)
$$

In Equation (5), $F(t)$ is the unreliability, $R(t)$ is the reliability, and $\lambda$ is the failure rate.

### 2.2. Polymorphic Fault Gate

The logic gate is referred to as a polymorphic fault gate when it comprises one or more polymorphic events which are contained in the input to the top event. $X_{i}(i=1,2, \ldots, n)$ with $n$ being the polymorphic input events, that is, the input event satisfies $S_{X_{i}} \in\{0,0.5,1\}$, $S_{X_{i}} \in$ \{normal,degradation,failure\}. Indeed, the top event $U$ conforms to Equation (6).

$$
S_{U}= \begin{cases}0 & \sum_{i=1}^{n} S_{X_{i}}=0 \\ 0.5 & S_{X_{i}} \leq 0.5 \text { and } \sum_{i=1}^{n} S_{X_{i}} \neq 0 \\ 1 & \text { Others }\end{cases}
$$

Equation (6) indicates that the output events' state is also normal for normal input polymorphic events, and when the state of the input polymorphic events is in the degradation state or a combination of normal and degradation, the output events are also in a degradation state. When at least one input polymorphic event is in failure, the system fails [29]. Table 1 shows the description of Equation (6).

Table 1. The relationship between the states of the output events and the input of the polymorphic system.


In Table 1, $\mathrm{I}_{1}$ and $\mathrm{I}_{2}$ are the two input events. O is the output event. $0,0.5$, and 1 represent the three states of normal, degradation, and failure, respectively. In addition, there are only three states of input and output.

# 2.3. Basic Theory of Bayesian Networks 

### 2.3.1. The Foundations of Bayesian Networks Theory

Bayesian networks are built on conditional probability, joint probability, and total probability.

1. Conditional probability

For any two events $X$ and $Y$ and event $X$, the occurrence probability is non-negative, namely $P(X)>0$, and $P(Y \mid X)$ is the probability of event $Y$ happening under the conditions of a given event $X$ happening. The formula is expressed is:

$$
P(Y \mid X)=\frac{P(X Y)}{P(X)}
$$

where $P(X Y)$ is the probability of event $X$ occuring simultaneously with event $Y$.
2. Joint probability

For the probability of events $X$ and $Y$ happening at the same time, Equation (7) is used to obtain the probability:

$$
P(X Y)=P(X) \bullet P(Y \mid X)
$$

where $P(Y \mid X)$ is the probability of event $Y$ occuring conditional on event $X$ occuring.
3. Total probability

Suppose $X_{1}, X_{2}, \ldots, X_{n}$ is a partition of the sample space $X$. Well, for any event $Y$, the chance of occurrence is:

$$
P(Y)=\sum_{i=1}^{n} P\left(X_{i}\right) \bullet P\left(Y \mid X_{i}\right)
$$

4. Bayesian formula

The conditional probability and total probability are used to obtain:

$$
P\left(X_{i} \mid Y\right)=\frac{P\left(X_{i}\right) P\left(Y \mid X_{i}\right)}{\sum_{i=1}^{n} P\left(X_{i}\right) P\left(Y \mid X_{i}\right)}
$$

where $P\left(X_{i} \mid Y\right)$ is the posterior probability; $P\left(X_{i}\right)$ is the prior probability; $P\left(Y \mid X_{i}\right)$ is the likelihood probability [30]; $X_{1}, X_{2}, \ldots, X_{n}$ are mutually independent causes; and Y is the result. In practical engineering, prior probabilities and likelihood probabilities can be predicted. Using the Bayesian formula, it is possible to reason about the probability of the occurrence of a cause $P\left(X_{i} \mid Y\right)$ given the conditions under which the outcome occurs and to determine the cause that has the greatest influence on the outcome.

# 2.3.2. Bayesian Networks' Basic Principles 

$B=<G, P>=<<V, E>, P>$ represents Bayesian networks, which consists of conditional probability distribution (CPD) and a directed acyclic graph (DAG) [31,32]. Where $G=<V, E>$ represents the DAG, the elements in the node set V represent the variables, and E is the association between the variables [33,34]. In a directed acyclic graph of the BN, if nodes $X$ to $Y$ have a directed edge, then $X$ is $Y$ 's parent node. The parent node and children node of a node are called its neighbor node. There is no parent node for the root node and no children node for the leaf node. $p a(\mathrm{X})$ or $\pi(X)$ represent the node X's parent node, the children node is denoted as $c h(\mathrm{X})$, and the neighbour node is denoted as $n b(\mathrm{X})$ [35]. P in Bayesian networks denotes the conditional probability distribution and is represented by the conditional probability table (CPT) when the nodes are discrete random variables.

Semantically, a BN is a representation of the decomposition of the junction probability distribution. $X_{1}, X_{2}, \ldots, X_{n}$ are variables in the Bayesian network, and the joint probability distribution is:

$$
P\left(X_{1}, X_{2}, \ldots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid \pi\left(X_{i}\right)\right)
$$

Figure 1 gives a simple example of a BN, in which $X_{1}$ is the root node and also $X_{2}$ and $\mathrm{X}_{3^{\prime}}$ parent nodes. $\mathrm{X}_{4}$ is a leaf node and also the child node of $\mathrm{X}_{2}$ and $\mathrm{X}_{3} . \mathrm{X}_{2}$ and $\mathrm{X}_{3}$ represent the intermediate nodes. Next to the nodes is a table of conditional probabilities between the nodes. Each node in the Bayesian network has two states, 0 and 1, representing non-occurrence and occurrence, respectively.
![img-0.jpeg](img-0.jpeg)

Figure 1. Simple Bayesian network.
According to Equation (11), the junction probability distribution function comprises all nodes in Figure 1 and is:

$$
P\left(X_{1}, X_{2}, X_{3}, X_{4}\right)=P\left(X_{4} \mid X_{2}, X_{3}\right) P\left(X_{2} \mid X_{1}\right) P\left(X_{3} \mid X_{1}\right) P\left(X_{1}\right)
$$

2.3.3. Bayesian Networks Modelling

1. Bayesian network models for two-state systems

Traditional reliability analysis methods use deterministic expressions of two-state events to represent the logical relationships between events, and the results obtained from logical operations are also deterministic. Figure 2a,b shows the structure of a typical logic "AND" gate and logic "OR" gate in the FTA [36]. The "AND" gate shows top event C, and bottom events A and B appear at the same time. The "OR" gate shows that when bottom events A or B occur, top event C appears. The deterministic relationship between logic gates can be represented by Bayesian networks (Figure 2c,d).

![img-1.jpeg](img-1.jpeg)

**Figure 2.** Deterministic logic gates of two-state events and the corresponding BN model as: (**a**) the "AND" gate; (**b**) the "OR" gate; (**c**) the BN model of the "AND" gate; and (**d**) the BN model of the "OR" gate.

In practical engineering applications, there are often uncertain logical relationships between events, and the logic gates of the FTA are no longer able to represent such uncertain logical relationships. However, Bayesian networks can solve this problem by the probability of manifestation of the uncertainties in the conditional probability table.

Similarly, the Bayesian network model corresponding to the "OR" gate in Figure 2d can be used to represent the logical relationship of uncertainty in terms of probability values (Figure 3).

![img-2.jpeg](img-2.jpeg)

**Figure 3.** The Bayesian network model of the uncertain logic gate.

As can be seen from Figure 3, output C must not occur only if neither input A nor B occur. When A and B occur at the same time, the probability of C occurring is 0.98, which is not necessarily occurring; when one of A and B occurs, C does not necessarily occur, so the interaction between input and output events A, B, and C is not a simple deterministic logic "AND" and logic "OR" but rather an uncertainty relationship between the two. Based on this, the uncertainty logical relationship between events is represented by Bayesian networks.

2. Bayesian network models for polymorphic systems

Bayesian networks can also be used to represent logical relationships between polymorphic systems. According to the definition of multi-state logic gates in Section 2.2, the values 0,0.5 , and 1 denote the normal, degradation, and failed states of the three-state system, respectively. According to Equation (6), the output event state is also normal with the normal input polymorphic events. When the input polymorphic events are in the degradation state or a combination of the degradation and normal states, the output event state is also in the degradation state. The whole system's output fails when one input event fails. Figures 4 and 5 represent the polymorphic logic gates under the FTA and Bayesian network models, respectively.
![img-3.jpeg](img-3.jpeg)

Figure 4. Polymorphic logic gates under the FTA.
![img-4.jpeg](img-4.jpeg)

Figure 5. Polymorphic logic gates under the Bayesian network models.
According to Figure 4, it can be seen that $A$ and $B$ are polymorphic input events with three states, 0,0.5 , and 1 , and C is a polymorphic output event and also has three input states with the same state as the input event, and the polymorphic events $A, B$ and $C$ indicate the logical interaction among the three with polymorphic fault gates.

In comparison with Figure 4, in Figure 5, the polymorphic input events A and B are mapped to the polymorphic Bayesian network as root nodes, and the root nodes A and B also have three states. Output event C maps to a polymorphic Bayesian network as a leaf node of a polymorphic Bayesian network, and the polymorphic fault gate between polymorphic events $A, B$, and $C$ maps to a polymorphic Bayesian network as a conditional probability table for a polymorphic Bayesian network. The one-way arrows of root nodes A and B pointing to C in Figure 5 indicate that root nodes A and B have an influential relationship on leaf node C, i.e., the leaf node's state is affected by root nodes A and B.

# 2.4. Reliability Analysis Based on the BNs 

When using the Bayesian networks' principle to analyze system reliability, the correspondence between the Bayesian networks and the FT is as follows: the basic events in the

FT that cause the system to breakdown is used as the root node in the Bayesian networks, the intermediate node is the middle event of the FT, and the whole system failure event is used as the Bayesian network's leaf node to build the Bayesian networks model. The logical block diagram for maps from the FTA to the BN according to the narrative is shown in Figure 6.
![img-5.jpeg](img-5.jpeg)

Figure 6. Block diagram of the logic for maps from the FTA to the BN.
Assume that the BN model has $T, X_{1}, \ldots, X_{n-1}$ with a total of $n$ nodes. $T$ denotes a leaf node, $X_{1} \sim X_{n-1}$ denote the root and intermediate nodes, respectively. The state of node $T$ is denoted by $T_{q}$, and node $X_{i}(1 \leq i \leq n-1)$ 's actual state value is denoted by $x_{i}$. When the states $T_{q}$ and $i$ take 0 or 1 , this means that the event does not occurs or occurs, i.e., the normal state or the failure state. When the states $T_{q}$ and $i$ take $0,0.5$, and 1 , this signifies that the three-state event corresponds to the normal, degradation, and failure states. Using the junction probability distribution, the whole system's failure probability is:

$$
P(T=1)=\sum_{X_{1}, \ldots, X_{n-1}} P\left(T=1, X_{1}=x_{1}, \ldots, X_{n-1}=x_{n-1}\right)
$$

The posterior probability of other events occuring after event $X_{j}$ is:

$$
P\left(X_{i}=1 \mid X_{j}=1\right)=\frac{P\left(X_{j}=1 \mid X_{i}=1\right) P\left(X_{i}=1\right)}{P\left(X_{j}=1\right)},(1 \leq i \neq j \leq n-1)
$$

Particularly, the posterior probability of node $X_{i}$ 's occurrence is as follows with leaf node $T$ occurrence:

$$
P\left(X_{i}=1 \mid T=1\right)=\frac{P\left(T=1 \mid X_{i}=1\right) P\left(X_{i}=1\right)}{P(T=1)},(1 \leq i \leq n-1)
$$

The inference algorithm is used to solve bottom event $X_{i}$ 's critical importance and probability importance.

1. Probability importance

The basic event $X_{i}$ fault state being $x_{i}^{a \prime}$ s probability importance $I_{T_{q}}^{P r}\left(X_{i}=x_{i}^{a}\right)$ with respect to the top event $T$ fault state being $T_{q}$ is:

$$
I_{T_{q}}^{P r}\left(X_{i}=x_{i}^{a}\right)=\left|P\left(T=T_{q} \mid X_{i}=x_{i}^{a}\right)-P\left(T=T_{q} \mid X_{i}=0\right)\right|
$$

where $P\left(T=T_{q} \mid X_{i}=0\right)$ denotes the conditional probability that the $T$ fault state is $T_{q}$ when the $X_{i}$ fault state is 0 . The probability importance $I_{T_{q}}^{P r}\left(X_{i}\right)$ of event $X_{i}$ with respect to the top event $T$ fault state as $T_{q}$ is:

$$
I_{T_{q}}^{P r}\left(X_{i}\right)=\frac{1}{k_{i}-1} \sum_{a_{i}=1}^{k_{i}} I_{T_{q}}^{P r}\left(X_{i}=x_{i}^{a}\right)
$$

In Equation (17), $k_{i}$ is the number of fault states for event $X_{i}$.
2. Critical importance

The basic event $X_{i}$ fault state being $x_{i}^{a \prime}$ s critical importance $I_{T_{q}}^{C r}\left(X_{i}=x_{i}^{a}\right)$ with respect to the top event $T$ fault state being $T_{q}$ is:

$$
I_{T_{q}}^{C r}\left(X_{i}=x_{i}^{a}\right)=\frac{P\left(X_{i}=x_{i}^{a}\right) I_{T_{q}}^{P r}\left(X_{i}=x_{i}^{a}\right)}{P\left(T=T_{q}\right)}
$$

Then, the critical importance $I_{T_{q}}^{C r}\left(X_{i}\right)$ of event $X_{i}$ with respect to the top event $T$ fault state as $T_{q}$ is:

$$
I_{T_{q}}^{C r}\left(X_{i}\right)=\frac{1}{k_{i}-1} \sum_{a_{i}=1}^{k_{i}} I_{T_{q}}^{C r}\left(X_{i}=x_{i}^{a}\right)
$$

Probability importance indicates the change scope resulting from the occurrence of an event in the system. Critical importance reflects not only the change rate in probability resulting from that of an event occurring, but also the ease of improvement in the failure rate of that event [37]. The system failure's key causes are identified by critical importance and probability importance.

# 3. Establishment of the Polymorphic Bayesian Network for the High-Voltage Drive Motor System 

### 3.1. Establishment of the Polymorphic FT for the High-Voltage Drive Motor System

This manuscript takes the pure electric commercial vehicle L2 model of a vehicle manufacturer as the research object; the motor type chosen for the studied high-voltage drive motor system is a permanent magnet synchronous motor (PMSM), and its motor parameters are shown in Table 2.

Table 2. Basic parameters of the PMSM.


The complex operating conditions of pure electric commercial vehicles require drive motors that can adapt to frequent stopping, starting, accelerating, and decelerating. They also have the peculiarity of low/high torque at high/low speed; therefore, they require a high degree of reliability from the drive motor. The main causes of the functional degradation of drive motors are wear fault in the form of the presence of abrasive particles, excessive speed and high-temperature gluing. Plastic deformation can occur in the form

of indentation, improper lubrication, etc. Corrosion failure can be caused by chemical corrosion, moisture, etc., and insulation deterioration can be caused by high-frequency pulse voltage, localized high temperatures, poor cooling, etc.

According to the cause of system degradation, the high voltage drive system degradation as the top event as well as the system failure event's cause as the bottom event build a polymorphic fault tree and encode the events. The event definitions and codes are shown in Table $3-\mathrm{T}$ is the failure of the pure electric commercial vehicle's high-voltage power battery system. $\mathrm{K}_{1}, \mathrm{~K}_{2}, \mathrm{~K}_{3}$, and $\mathrm{K}_{4}$ are the intermediate events in the failure of a high-voltage drive motor system, where the occurrence of intermediate event $\mathrm{K}_{1}$ can be caused by the occurrence of one of the bottom events $\mathrm{Y}_{1}, \mathrm{Y}_{2}, \mathrm{Y}_{3}, \ldots$, and $\mathrm{Y}_{6}$. Similarly, the occurrence of $\mathrm{K}_{2}$ is caused by one of $\mathrm{Y}_{7}, \mathrm{Y}_{8}$, and $\mathrm{Y}_{9}$, and $\mathrm{K}_{3}$ is caused by one of $\mathrm{Y}_{10}, \mathrm{Y}_{11}$, and $\mathrm{Y}_{12}$, and the occurrence of any one of $\mathrm{Y}_{13}, \mathrm{Y}_{14}, \ldots$, and $\mathrm{Y}_{17}$ can lead to the occurrence of $\mathrm{K}_{4}$.

Table 3. Event codes and definitions.


Based on Table 3, the high-voltage drive motor system's polymorphic FT of a purely electric commercial vehicle is simplified (Figure 7).
![img-6.jpeg](img-6.jpeg)

Figure 7. Polymorphic FT for the high-voltage drive motor system.
In Figure 7, $\mathrm{Y}_{1}, \mathrm{Y}_{2}, \ldots$, and $\mathrm{Y}_{17}$ are the polymorphic FT's polymorphic bottom events, $\mathrm{K}_{1}, \mathrm{~K}_{2}, \mathrm{~K}_{3}$, and $\mathrm{K}_{4}$ are the intermediate events of the polymorphic FT, and T represents the polymorphic FT's top event and the system failure's top event.

# 3.2. Establishment of the Polymorphic Bayesian Network 

When the conventional fault tree analysis method is used to analyse the reliability of a system, it can only analyze the probability of failure of the top event of the system in

the two states of normal and failure of the bottom event represented by 0 and 1, i.e., the conventional fault tree analysis method can only be used to solve the reliability problem of a two-state system. However, bottom events such as surface corrosion and localized high temperatures in the high-voltage drive motor system cannot be accurately described by normal and failure states; they are polymorphic events that can be divided into normal, degradation and failure states, and the insulation deterioration caused by these two polymorphic bottom events is also a polymorphic event, i.e., it can be accurately described by normal, degradation, and failure states. Therefore, the conventional fault tree analysis method is not applicable to the analysis of the polymorphic system. In the polymorphic Bayesian network, the normal, degradation, and failure states of the polymorphic system are represented by 0,0.5 , and 1 , respectively, which can more accurately analyze the reliability of the polymorphic system.

According to the high-voltage drive motor system's polymorphic FT, the root node is the bottom event $\mathrm{Y}_{1}, \mathrm{Y}_{2}, \mathrm{Y}_{3}, \ldots$, and $\mathrm{Y}_{17}$, the middle events $\mathrm{K}_{1}, \mathrm{~K}_{2}, \mathrm{~K}_{3}$, and $\mathrm{K}_{4}$ are the intermediate nodes, and the top event $T$ is the leaf node to build the high-voltage drive motor system polymorphic Bayesian network model (Figure 8). In Figure 8, intermediate node K 1 is a child of root nodes $\mathrm{Y}_{1}, \mathrm{Y}_{2}, \mathrm{Y}_{3}, \mathrm{Y}_{4}, \mathrm{Y}_{5}$, and $\mathrm{Y}_{6}$; intermediate node $\mathrm{K}_{2}$ is a child of root nodes $\mathrm{Y}_{7}, \mathrm{Y}_{8}$, and $\mathrm{Y}_{9}$; intermediate node $\mathrm{K}_{3}$ is a child of root nodes $\mathrm{Y}_{10}, \mathrm{Y}_{11}$, and $\mathrm{Y}_{12}$; intermediate node $\mathrm{K}_{4}$ is a child of root nodes $\mathrm{Y}_{13}, \mathrm{Y}_{14}, \mathrm{Y}_{15}, \mathrm{Y}_{16}$, and $\mathrm{Y}_{17}$; and leaf node T is a child of intermediate nodes $\mathrm{K}_{1}, \mathrm{~K}_{2}, \mathrm{~K}_{3}$, and $\mathrm{K}_{4}$. There are 17 root nodes, 4 middle nodes, and 1 leaf node.
![img-7.jpeg](img-7.jpeg)

Figure 8. Polymorphic Bayesian network model for the high voltage drive motor system.
In Figure 8, according to Equation (6) and Table 1, the input-output relationship between each polymorphic root node and intermediate node and between each intermediate node and leaf node can be obtained as follows: (1) there is a node with a state of 1 between the root nodes $\mathrm{Y}_{1}, \mathrm{Y}_{2}, \ldots$, and $\mathrm{Y}_{17}$, which will cause there to be a state of 1 in the intermediate nodes $\mathrm{K}_{1}, \mathrm{~K}_{2}, \mathrm{~K}_{3}$, and $\mathrm{K}_{4}$, that is, the leaf node has a state of 1. (2) When one of the root nodes $\mathrm{Y}_{1}, \mathrm{Y}_{2}, \ldots$, and $\mathrm{Y}_{17}$ has a state of 0.5 , it will cause the intermediate nodes $\mathrm{K}_{1}, \mathrm{~K}_{2}, \mathrm{~K}_{3}$, and $\mathrm{K}_{4}$ to also have a node with a state of 0.5 , which will eventually lead to a leaf node state of 0.5 . (3) If and only if all root nodes have a state of 0 , the intermediate node state is also 0 , that is, the leaf node state is 0 .

The CPT in Figure 8 can be deduced from Equation (6) and the CPT in the polymorphic logic gate under the Bayesian network model in Figure 5. Taking the conditional probability of node $\mathrm{K}_{2}$ as an example, the CPT of the intermediate node $\mathrm{K}_{2}$ and the root nodes $\mathrm{Y}_{7}, \mathrm{Y}_{8}$, and $\mathrm{Y}_{9}$ is obtained as shown in Table 4. The remaining CPTs between every root node, middle node, intermediate node, and leaf node can be deduced by referring to Equation (6) and Table 1, which are not detailed here.

Table 4. Table of the conditional probabilities for the intermediate node $\mathrm{K}_{2}$.


$\vdots$ - The case of the same conditional probability is omitted.

# 4. Polymorphic Bayesian Network Model Solving

### 4.1. Calculation of the Occurrence Probability of the Top Event's States

The prior probabilities of each root node in the polymorphic Bayesian network model of the high voltage drive motor system are shown in Table 5.

Table 5. Each root node's prior probability.


Based on Figure 8, a simulation model of the polymorphic Bayesian network was built in GenIe simulation software, and the model includes the conditional probabilities in Table 3 and the prior probabilities of each root node in Table 4. Inference on the polymorphic

Bayesian network models is provided by GenIe and Equation (13). The top event $T$ failure probability is gained:

$$
\begin{aligned}
& P\left(T=1\right)=\sum_{Y_{1}, Y_{2}, \ldots, Y_{17}} P\left(Y_{1}, Y_{2}, \ldots, Y_{17}, K_{1}, \ldots, K_{4}, T=1\right)=\sum_{K_{1}, \ldots, K_{4}} P\left(T=1 \mid K_{1}, \ldots, K_{4}\right) \times \sum_{Y_{1}, \ldots, Y_{6}} P\left(K_{1} \mid Y_{1}, \ldots, Y_{6}\right) \times P\left(Y_{1}\right) \ldots P\left(Y_{6}\right) \\
& K_{1}, \ldots K_{4} \\
& \times \sum_{Y_{7}, Y_{8}, Y_{9}} P\left(K_{2} \mid Y_{7}, Y_{8}, Y_{9}\right) \times P\left(Y_{7}\right) \times P\left(Y_{8}\right) \times P\left(Y_{9}\right) \times \ldots \times \sum_{Y_{13}, \ldots, Y_{17}} P\left(K_{4} \mid Y_{13}, \ldots, Y_{17}\right) \times P\left(Y_{13}\right) \times \ldots P\left(Y_{17}\right)
\end{aligned}
$$

Using the conditional probability between the nodes in Table 1 and the a priori probability of each root node, the top event's failure probability is obtained as:

$$
P(T=1)=0.00878
$$

Similarly, the top event's probabilities in the normal and degradation states are:

$$
\begin{aligned}
P(T=0) & =0.9841 \\
P(T=0.5) & =0.00712
\end{aligned}
$$

According to the relationship between the reliability and the failure rate of the system in Equation (4), the system's reliability is:

$$
R_{T}=0.9913
$$

Based on the interaction between the unreliability and the reliability of Equation (5), system's unreliability is:

$$
F_{T}=1-R_{T}=0.0087
$$

# 4.2. Solution of the Basic Event's Posterior Probability 

The failure state's posterior probability $\mathrm{Y}_{1}$ of the bottom event with the top event $T$ as the failure state is derived from Equation (15) as:

$$
P\left(Y_{1}=1 \mid T=1\right)=\frac{P\left(T=1 \mid Y_{1}=1\right) P\left(Y_{1}=1\right)}{P(T=1)}=0.1935
$$

Similarly, the posterior probabilities of the bottom event $Y_{i}(i=0, \ldots, 17)$ state of 0.5 or 1 can be obtained under the condition that the top event $T$ is 0.5 or 1 . According to Table 5, the leaf node is in state 1 when the state of at least one root node is in state 1 , that is, the bottom event's posterior probability $Y_{i}$ in state 1 is 0 when the top event $T$ is in state of 0.5 . The posterior probabilities of the events at the bottom as indicated in Table 6.

Table 6. Posterior probabilities of the bottom event.


According to the conditional probability table in Table 5, when the parent node is in state of 0.5 , the child node state 1 of probability is 0 , that is, when $T$ is 0.5 , the root node $\mathrm{Y}_{i}$ 's posterior probability is 0 . To more intuitively describe the comparative relationship between the posterior probabilities of every basic event, a comparative histogram of the posterior probabilities of each floor event was plotted from Table 6 as shown in Figures 9 and 10.
![img-8.jpeg](img-8.jpeg)

Figure 9. The posterior probabilities of every floor event when the upper layer event state is 0.5 .
![img-9.jpeg](img-9.jpeg)

Figure 10. The posterior probabilities of every floor event when the top event state is 1 .
The system can be anatomized by the bottom's posterior failure probability after the fault of the system, that is, the judgement is found out in the sequence of each bottom event's posterior probability from largest to smallest. According to Figure 9, once system functional degradation has been observed, a fault analysis should be performed on the bottom events in a degraded state in the order: $\mathrm{Y}_{1}, \mathrm{Y}_{5}, \mathrm{Y}_{10}, \mathrm{Y}_{14}, \ldots, \mathrm{Y}_{16}$, and $\mathrm{Y}_{7}$. According to Figure 10, once system functional failure has been observed, a fault analysis should be performed on the basic events in a degraded state in the order: $\mathrm{Y}_{1}, \mathrm{Y}_{5}, \mathrm{Y}_{10}, \mathrm{Y}_{14}, \ldots$, and $\mathrm{Y}_{16}, \mathrm{Y}_{7}$, and a fault analysis should be performed on the floor events in the failure state in the sequence: $\mathrm{Y}_{1}, \mathrm{Y}_{5}, \mathrm{Y}_{10}, \mathrm{Y}_{14}, \ldots, \mathrm{Y}_{17}$, and $\mathrm{Y}_{7}$.

# 4.3. Solution to the Basic Event Importance 

1. Probability importance

The bottom event's probability importance $\mathrm{Y}_{1}$ being in the degradation state of 0.5 with respect to the top event T being in the degradation state of 0.5 is derived from Equation (16) as:

$$
I_{0.5}^{P r}\left(Y_{1}=0.5\right)=\left|P\left(T=0.5 \mid Y_{1}=0.5\right)-P\left(T=0.5 \mid Y_{1}=0\right)\right|=0.9868
$$

The probability importance that the base event $Y_{1}$ is in failed state 1 and is in a degenerate state relative to the top event $T$ being in the state of 0.5 is:

$$
I_{0.5}^{P r}\left(Y_{1}=1\right)=\left|P\left(T=0.5 \mid Y_{1}=1\right)-P\left(T=0.5 \mid Y_{1}=0\right)\right|=0.00614
$$

The basis event's probability importance $Y_{1}$ related to the upper layer event $T$ being in the fault state of 0.5 is derived from Equation (17) as:

$$
I_{0.5}^{P r}\left(Y_{1}\right)=\frac{\left[I_{0.5}^{P r}\left(Y_{1}=0.5\right)+I_{0.5}^{P r}\left(Y_{1}=1\right)\right]}{2}=0.49647
$$

Similarly, the probability importance that the underlying event $Y_{1}$ is in the failed state of 0.5 relative to the top-level event $T$ being in the failed state 1 is:

$$
I_{1}^{P r}\left(Y_{1}=0.5\right)=\left|P\left(T=1 \mid Y_{1}=0.5\right)-P\left(T=1 \mid Y_{1}=0\right)\right|=0
$$

The probability importance that the bottom event $Y_{1}$ is in the fault state 1 relative to the top event $T$ being in the fault state 1 is:

$$
I_{1}^{P r}\left(Y_{1}=1\right)=\left|P\left(T=1 \mid Y_{1}=1\right)-P\left(T=1 \mid Y_{1}=0\right)\right|=0.9929
$$

The floor event's probability importance $Y_{1}$ related to the upper layer event $T$ being in the fault state 1 is derived from Equation (17) as:

$$
I_{1}^{P r}\left(Y_{1}\right)=\frac{\left[I_{1}^{P r}\left(Y_{1}=0.5\right)+I_{1}^{P r}\left(Y_{1}=1\right)\right]}{2}=0.49645
$$

Similarly, the floor event's probability importance $Y_{i}$ related to the upper layer event T being in the fault states 0.5 and 1 is derived from Equations (16) and 17, as pointed out in Table 7.

Table 7. The bottom event's probability importance $Y_{i}$ with respect to the upper layer event $T$ being in the fault states 0.5 and 1 .


The probability importance line chart was drawn according to Table 7 (Figure 11).

![img-10.jpeg](img-10.jpeg)

Figure 11. The probability importance curve of the floor event $Y_{i}$ with respect to the upper layer event $T$ being in the fault states 0.5 and 1 .

# 2. Critical importance 

The critical importance of the bottom event $Y_{1}$ being in the breakdown state of 0.5 with respect to the top event T being in the breakdown state of 0.5 is derived from Equation (18) as:

$$
I_{0.5}^{C r}\left(Y_{1}=0.5\right)=\frac{P\left(Y_{1}=0.5\right) I_{0.5}^{P r}\left(Y_{1}=0.5\right)}{P(T=0.5)}=0.13860
$$

The critical importance of the floor event $Y_{1}$ being in the failure state of 1 with respect to the top event T being in the breakdown state of 0.5 is:

$$
I_{0.5}^{C r}\left(Y_{1}=1\right)=\frac{P\left(Y_{1}=1\right) I_{0.5}^{P r}\left(Y_{1}=1\right)}{P(T=0.5)}=0.001466
$$

The critical importance of the floor event $Y_{1}$ with respect to the upper layer event $T$ being in the fault state of 0.5 is derived from Equation (19) is:

$$
I_{0.5}^{C r}\left(Y_{1}\right)=\frac{\left[I_{0.5}^{C r}\left(Y_{1}=0.5\right)+I_{0.5}^{C r}\left(Y_{1}=1\right)\right]}{2}=0.07003
$$

Similarly, the critical importance of the floor event $Y_{1}$ being in the fault state of 0.5 related to the top event $T$ being in the breakdown state of 1 is:

$$
I_{1}^{C r}\left(Y_{1}=0.5\right)=\frac{P\left(Y_{1}=0.5\right) I_{1}^{P r}\left(Y_{1}=0.5\right)}{P(T=1)}=0
$$

The critical importance of the floor event $Y_{1}$ being in the fault state of 1 with respect to the upper layer event $T$ being in the fault state of 1 is:

$$
I_{1}^{C r}\left(Y_{1}=1\right)=\frac{P\left(Y_{1}=1\right) I_{1}^{P r}\left(Y_{1}=1\right)}{P(T=1)}=0.19225
$$

The critical importance of the floor event $Y_{1}$ with respect to the upper layer event $T$ being in fault state of 1 is derived from Equation (19) is:

$$
I_{1}^{C r}\left(Y_{1}\right)=\frac{\left[I_{1}^{C r}\left(Y_{1}=0.5\right)+I_{1}^{C r}\left(Y_{1}=1\right)\right]}{2}=0.09612
$$

Similarly, the critical importance of the floor event $Y_{i}$ with respect to the upper layer event T being in the fault states of 0.5 and 1 is derived from Equations (18) and (19), as shown in Table 8.

Table 8. The bottom event's critical importance $Y_{i}$ related to the top event $T$ being in the fault states of 0.5 and 1 .


The critical importance line chart shown in Figure 12 was drawn according to the results in Table 8.
![img-11.jpeg](img-11.jpeg)

Figure 12. Critical importance curve of the floor event $Y_{i}$ with respect to the upper layer event $T$ being in fault the states of 0.5 and 1 .

# 4.4. System Reliability Analysis 

Based on each error mode's critical importance and probability importance for the different failure states of the system, it can be shown how much each failure state affects the system and vulnerable points in the system can be confirmed. It can be seen from Figure 11 that the order of the impact extent of the root node $Y_{i}$ on the system's breakdown state in the degradation state is: $Y_{1}=Y_{5}=Y_{10}=Y_{14}>Y_{3}>\ldots>Y_{17}$. The order of the root node's impact extent $Y_{i}$ on the system's error state in the failure state is: $Y_{1}=Y_{5}=Y_{10}=$ $Y_{14}>Y_{3}>\ldots>Y_{17}$. Similarly, as can be seen from the critical importance curve of the basic event with regards to the top-level event fault state in Figure 12, the order of the root node's impact extent $Y_{i}$ on the system's breakdown state in the degradation state is: $Y_{1}=Y_{5}=Y_{10}=Y_{14}>Y_{2}>\ldots>Y_{7}$. The order of the root node's impact extent $Y_{i}$ on the system's breakdown state in the failure state is: $Y_{1}=Y_{5}=Y_{10}=Y_{14}>Y_{2}>\ldots>Y_{17}$.

In summary, according to the conclusions of the floor event's probability importance to the system in different fault states, it can be seen that the breakdown states of the bottom events $\mathrm{Y}_{1}, \mathrm{Y}_{5}, \mathrm{Y}_{10}$, and $\mathrm{Y}_{14}$ have the biggest impact on the system's fault state, and according to the conclusions of the bottom event's critical importance to the system in different breakdown states, it can be seen that the bottom events $\mathrm{Y}_{1}, \mathrm{Y}_{5}, \mathrm{Y}_{10}$, and $\mathrm{Y}_{14}$ as the weak link of the polymorphic system are more difficult to improve, that is, they are the weakest link of the system, and the corresponding bottom events are: the presence of abrasive particles, high-temperature gluing, moisture, and localized high temperatures. The analysis shows that the bottom events $\mathrm{Y}_{1}, \mathrm{Y}_{5}, \mathrm{Y}_{10}$, and $\mathrm{Y}_{14}$ require special attention and improvement to reduce the occurrence of serious failures.

Meanwhile, according to each root node's posterior probabilities in the previous sections, it can be seen that after the system's degradation or failure fault, the root nodes causing the highest fault occurrence probability are $\mathrm{Y}_{1}, \mathrm{Y}_{5}, \mathrm{Y}_{10}$, and $\mathrm{Y}_{14}$, i.e., the presence of abrasive particles, high-temperature gluing, moisture, and localized high temperatures. When carrying out detection and fault diagnosis in a pure electric commercial vehicle's high-voltage drive motor system, whole system detection is enhanced by selecting the bottom event with a high posterior probability according to each basic event's occurrence in the high-voltage drive motor system.

When optimizing the reliability of the system, improvements should be made in the following two areas in case of system wear failure due to the presence of abrasive particles: (1) enhanced lubrication. Filling the frequent friction surface with lubricating oil greatly reduces the friction coefficient, thus contributing to a reduction in frictional resistance and a reduction in mechanical wear. (2) Improve the quality of installation and maintenance. Correctly tightening the motor bearing cover and the bearing seat connection screws, so that the combination of the face is in the center, and adjusting the appropriate bearing clearance, etc., can make the unit load on the surface of the uniform distribution so that its wear is reduced. The system should be improved in the following three ways in case of corrosion failure due to moisture: (1) adopt a sealed design to prevent moisture from entering the motor interior. Clean and dry the inside of the motor casing before sealing and reduce the humidity inside the sealed cavity as much as possible to avoid condensation inside at low temperatures. (2) For large mechanical mechanisms such as motors, design ventilation holes, moisture-proof mats, and other measures to eliminate moisture. (3) Adjust the humidity inside the cavity by adding moisture-regulating plates, moisture absorbers, etc.

Therefore, the bottom event-the presence of abrasive particles, high-temperature gluing, moisture, and localized high temperatures-is the most important and the weakest link in the high-voltage drive motor system, and the above measures can be taken to improve the reliability of the system.

# 5. Conclusions 

The reliability of the high-voltage drive motor system was analyzed by taking a pure electric commercial vehicle as the research object, dividing the system and its bottom event into three states of normal, degradation, and failure, and determining the probability of the top event of the system in the normal state, the degradation state, and the failure state as $0.9841,0.00712$, and 0.00878 , respectively, and solving the reliability of the high-voltage drive motor system as 0.9913 .

In this paper, based on the traditional fault tree analysis method, we mainly accomplish the following: (1) combining the fault tree analysis method with the basic theory of polymorphic Bayesian networks, establishing the polymorphic fault tree of a high-voltage drive motor system, transforming the polymorphic fault tree into a polymorphic Bayesian network model according to the maps relationship between the fault tree and the Bayesian network, and solving the occurrence probability of leaf nodes in each state by Bayesian network inference, and the posterior probability of the occurrence of the polymorphic bottom event when the top event was in different fault states was solved. The posterior probability of the polymorphic bottom event was analyzed to find out the most likely

event after system failure. (2) The quantitative analysis of the polymorphic root node was analyzed from the perspective of probability importance and critical importance to find out that the presence of abrasive particles, high-temperature gluing, moisture, and localized high temperatures are the weakest link in the high-voltage drive motor system and the most difficult bottom event to improve and optimize the system.

Finally, the detection and design optimization of the system based on the probability importance degree and the critical importance degree of the bottom event can improve the efficiency of subsequent fault diagnosis, which is of great significance for improving the high voltage drive motor system of pure electric commercial vehicles.

Author Contributions: Conceptualization, W.Z.; methodology, H.J.; software, W.Z.; validation, Q.M.; formal analysis, S.L.; writing-original draft preparation, H.J.; writing-review and editing, W.Z. and S.L. All authors have read and agreed to the published version of the manuscript.

Funding: This research was funded by the Innovation-Driven Development Special Fund Project of Guangxi, grant number Guike AA22068060; the Science and Technology Planning Project of Liuzhou, grant numbers 2021AAA0104 and 2022AAA0104; and the Liudong Science and Technology Project, grant number 20210117; and the Central Guiding Local Science and Technology Development Fund Projects, grant number 2022BGE180.

Data Availability Statement: No new data were created or analyzed in this study.
Conflicts of Interest: The authors declare no conflict of interest.
