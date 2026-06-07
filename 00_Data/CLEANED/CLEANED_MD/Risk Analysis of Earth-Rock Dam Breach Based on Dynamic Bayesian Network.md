# Article 

## Risk Analysis of Earth-Rock Dam Breach Based on Dynamic Bayesian Network

Zongkun Li ${ }^{1,2}$, Te Wang ${ }^{1}$, Wei Ge ${ }^{1,3, * *}$, Dong Wei ${ }^{1}$ and Hanyu Li ${ }^{1}$<br>1 School of Water Conservancy Engineering, Zhengzhou University, Zhengzhou 450001, China; lizongkun@zzu.edu.cn (Z.L.); wangte19960911@163.com (T.W.); wd2010@zzu.edu.cn (D.W.); llhy18832040809@163.com (H.L.)<br>2 School of Software, Zhengzhou University, Zhengzhou 450002, China<br>3 Safety and Security Science Group (S3 G), Faculty of Technology, Policy and Management, Delft University of Technology, 2628 BX Delft, The Netherlands<br>* Correspondence: W.Ge@tudelft.nl or gewei@zzu.edu.cn; Tel.: +31-15-278-1776

Received: 27 September 2019; Accepted: 31 October 2019; Published: 3 November 2019


#### Abstract

Despite the fact that the Bayesian network has great advantages in logical reasoning and calculation compared with the other traditional risk analysis methods, there are still obvious shortcomings in the study of dynamic risk. The risk factors of the earth-rock dam breach are complex, which vary with time during the operation period. Static risk analysis, limited to a specific period of time, cannot meet the needs of comprehensive assessment and early warning. By introducing time factors, a dynamic Bayesian network model was established to study the dynamic characteristics of dam-breach probability. Combined with the calculation of the conditional probability of nodes based on the Leaky Noisy-Or gate extended model, the reasoning results of Bayesian networks were modified by updating the data of different time nodes. Taking an earth-rock dam as an example, the results show that it has less possibility to breach and keep stable along the time axis. Moreover, the factors with vulnerability and instability were found effective, which could provide guidance for dam risk management.


Keywords: dynamic Bayesian network; dam breach; conditional probability; earth-rock dam; risk

## 1. Introduction

The earth-rock dam is currently the most widely used and fastest-developing dam type, which is widely favored for its simple construction technology and local material selection. At the end of 2011, there were 98007 dams in China, in which more than $90 \%$ were earth-rock dams [1-3]. Most of these dams were built in the period from the 1950s to 1970s and had potential safety hazards due to specific historical reasons [4,5]. The cases of failure of earth-rock dams are not rare, such as failures of the Banqiao earth dam (clay core dam) and the Shimantan earth dam (homogeneous clay dam) in China, which caused a large number of casualties and huge social impact [5]. In view of the short emergency response time and great harm of the earth-rock dam breach, scientific analysis, and evaluation of the probability of the earth-rock dam breach have become urgent problems to be solved.

A number of scholars have carried out relevant research recently based on some mature methods, such as the Analytic Hierarchy Process (AHP), event tree, the fault tree, and so on [6]. Ren et al. [7] established a hierarchical analysis failure model of the cascade reservoirs by AHP to calculate the overall failure probability of the cascade reservoir group system with weight factors. Fu et al. [8] proposed an event tree analysis method based on the fuzzy set theory to calculate the dam failure probability. Hong et al. [9] used event tree analysis method to analyse the risk probability of an underwater tunnel excavation. However, there are still some limitations in the practical application.

The quantitative analysis of AHP depends too much on experts' experience, meanwhile, the weight difference is not obvious when there are too many indicators at the same level. The analysis system of the event tree and fault tree method, which is generally used to infer the probability of the target event from one direction, is too complex. Moreover, these methods are not ideal in resolving the correlation among events at all levels. Actually, the state of the next event could be affected by the previous, which must be fully considered and analyzed.

The Bayesian network (BN), proposed by Judea Pearl in 1988 [10-12], is often applied to uncertain knowledge reasoning and makes up for the shortcomings of the above methods. With the continuous development and deepening of the Bayesian theory, its practical application scope is becoming wider and wider. The Bayesian theory has also been applied in the field of risk analysis and assessment of water conservancy. Zhou et al. [13] constructed a risk analysis model based on the Bayesian network according to different paths and modes of a dam breach. Peng et al. [11] proposed a new human risk analysis model for dam-breach floods based on Bayesian network. Delgado et al. [14] discussed the safety of earth dams in Mexico by using an improved a Bayesian network. However, the above Bayesian networks are static and did not take the time factor into account, which is not consistent with the engineering practice that the states of risk factors vary with time during the long-term service of earth-rock dams. Therefore, by introducing the time factor, a dynamic Bayesian network (DBN) model is established to study the variation characteristics of a dam breach and risk factors.

# 2. Methods 

### 2.1. Bayesian Network

### 2.1.1. Static Bayesian Network

Bayesian network (BN), also known as a belief network, is a directed acyclic graph to express and calculate the probability relationship between random variables [15,16]. It combines the knowledge of graph and statistics theory and has been proven to be a robust method for risk analysis [17,18]. A simple Bayesian network is mainly composed of parent nodes, child nodes, and the arrows that express the relationship between the nodes. Nodes A and B are the parent nodes of the child node C, as shown in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. A simple Bayesian network.
Bayesian formula and total probability formula are the theoretical bases of the Bayesian network, as shown in Equations (1) and (2):

$$
\begin{gathered}
P(B \mid A)=\frac{P(A \mid B) P(B)}{P(A)} \\
P(A)=\sum_{i} P\left(A \mid B_{i}\right) P\left(B_{i}\right)
\end{gathered}
$$

where $P(B)$ is the priori probability of event $B$, without considering any other factors; $P(B \mid A)$ is the probability of event $B$ under the condition that event $A$ has occurred, also known as a posteriori probability; $P(A \mid B)$ is the likelihood ratio; $i$ is the number of events.

The operation result of a Bayesian network is the joint probability distribution of all variables in the studied problem, which is the probability value under the influence of all factors. For example, the joint probability distribution of the simple Bayesian network in Figure 1 is shown as:

$$
P(A, B, C)=P\left(C \mid A, B\right) P(A, B)=P\left(C \mid A, B\right) P(A) P(B)
$$

Thus, if the prior probability and the corresponding conditional probability distribution of each parent node in Bayesian networks are known, the joint probability distribution that includes all the nodes could be obtained.

The relationship between the parent and child nodes could be roughly divided into two categories. One is a simple logical relationship, such as "and" or "or", in which the conditional probability of such nodes can be calculated directly through logical analysis. The other is that each parent node influences the child node by synthetical action, in which the conditional probability is usually given by sample learning or expert experience [19,20].

# 2.1.2. Dynamic Bayesian Network and Hypotheses 

With the development of risk events, the probabilities of the same event at different time nodes are often distinct. Considering the engineering practice, the time factor is introduced to realize the transition from a static Bayesian network to a dynamic Bayesian network (DBN). In view of the complexity of dynamic systems, most of the current research results simplify the dynamic model based on a certain hypotheses, e.g., the Markov hypothesis and the invariant transition probability hypothesis $[21,22]$.

The analysis process of the whole event can be regarded as a Markov chain according to Markov hypothesis [23], in which the probability of occurrence of the event after $t$-time is only related to the state of $t$-time, whereas not to the state before $t$-time. The transition probability is introduced to characterize the dynamics of the analysis process, which can be defined as the conditional probability that the Markov chain transforms one state to another after several times [21,24]. In the invariant transition probability hypothesis, the transition probability of the same event between any two adjacent time steps is assumed to be equal throughout the time axis.

Based on the above hypotheses, the establishment of the DBN model can be divided into three parts:
(a) Establishing a prior network $B_{0}$ and defining the joint probability distribution $P_{B_{0}}(X)$ at the initial time.
(b) Establishing a transition network and dividing the whole process into several time periods (also known as time steps).
(c) Defining the transition probability $P\left(X_{t+1} \mid X_{t}\right)$ of the same event on the adjacent time steps.

The parent node of event $X_{0}$ at the initial time belongs to a priori network $B_{0}$. The parent node of the event $X_{t+1}$ at time $t+1(t>0)$ is the node in the transfer network, which is related to both time $t$ and time $t+1$, as shown in Figure 2a-c. The joint probability distribution of the event $X$ over $T$ time steps in the DBN network can be expressed as:

$$
P\left(X_{1}, X_{2}, \ldots, X_{T}\right)=P_{B_{0}}\left(X_{1}\right) \times \prod_{t=1}^{T} P_{B} \rightarrow\left(X_{t+1} \mid X_{t}\right)
$$

![img-1.jpeg](img-1.jpeg)

Figure 2. (a) Initial network $B_{0}$ of dynamic Bayesian network. (b) Transfer network of dynamic Bayesian network. (c) Expansion of the DBN on the time axis.

Defining $P\left(X_{t} \mid X_{t-1}\right)$ as the transition probability. The transition probability between any two adjacent time steps in the DBN network is shown in Equation (5).

$$
P\left(X_{t} \mid X_{t-1}\right)=\prod_{i=1}^{n} P\left(X_{t}^{i} \mid P_{a}\left(X_{t}^{i}\right)\right)
$$

The joint probability distribution of any node is shown in Equation (6).

$$
P\left(X_{1: T}^{1: N}\right)=\prod_{i=1}^{N} P_{B_{0}}\left(X_{1}^{i} \mid P_{a}\left(X_{1}^{i}\right)\right) \times \prod_{t=2}^{t} \prod_{i=1}^{N} P_{B} \rightarrow\left(X_{1}^{i} \mid P_{a}\left(X_{1}^{i}\right)\right)
$$

where $X_{t}^{i}$ is the $i$ node in the $t$ time step; $P_{a}\left(X_{t}^{i}\right)$ is the parent node and $N$ is the number of random variables.
A two-step DBN can be displayed in two graphical representations, as shown in Figure 3. In order to simplify the structure, the second representation is more commonly used.
![img-2.jpeg](img-2.jpeg)

Figure 3. (a) A two-step DBN in the extended form. (b) The abstract form of the DBN.
Where the nodes $X_{1}$, and $X_{2}$ are the nodes in the original network; $X_{1}{ }^{\prime}, X_{2}{ }^{\prime}$, and $X^{\prime}$ reflect the state of the same node in the next time steps; the number 1 on the arced arrow represents the number of time steps used for the time dependencies.

Once the probabilities of these nodes are determined, Bayesian network reasoning can be carried out. However, there are many fuzziness and uncertainties in the failure of earth-rock dams. These probabilities

are hard to be obtained by the method of sample statistical learning, and can only be drawn up by experts of hydraulic engineering on the basis of sufficient reference to relevant information [20].

# 2.1.3. Determination of Node Probability 

Because of the limitations of risk identification, there are always some unknown factors that affect the nodes in Bayesian networks. In order to fully consider the influence of various factors on nodes, Henrio proposed the concept of leaky probability, which led to the Leaky Noisy-Or gate extension model [25,26].

The mathematical expression of the Leaky Noisy-Or gate extension model can be expressed as Equations (7) and (8):

$$
\begin{gathered}
P\left(X \mid X_{m}\right)=P_{m}+P_{n}-P_{m} P_{n} \\
P\left(X \mid \overline{X_{m}}\right)=P_{n}
\end{gathered}
$$

where $X_{m}$ and $X_{n}$ are the parent nodes of the event $X ; X_{n}$ is the sum of all factors except $X_{m} ; P_{m}$ and $P_{n}$ are the connection probabilities of $X_{m}$ and $X_{n}$, respectively.

By combining Equations (7) and (8), $P_{m}$ could be obtained, as shown in Equation (9).

$$
P_{m}=\frac{P\left(X \mid X_{m}\right)-P\left(X \mid \overline{X_{m}}\right)}{1-P\left(X \mid \overline{X_{m}}\right)}
$$

Defining $X_{l}$ as an unknown factor that represents all the unrecognized factors in the parent node of each event, the probability of node $X$ can be expressed as:

$$
P(X=x)=1-\left(1-P_{l}\right) \prod_{m: X_{m} \in X_{p}}\left(1-P_{m}\right)
$$

where $x$ represents a certain state of event $X ; P_{l}$ is the connection probability of $X_{l}$.

### 2.2. Probability Assessment of the Earth-Rock Dam Breach

### 2.2.1. Risk Factor Analysis of the Earth-Rock Dam Breach

Risk identification is not only the basis but also the premise of risk assessment and risk management [27-29]. In order to establish a framework for future systematic analysis and quantitative calculation, it is necessary to scientifically identify and classify the factors that may cause a dam breach.

At present, there are plenty of studies on the causes and mechanisms of the earth-rock dam breach. Zhang et al. [30] analyzed the failure modes and causes of earth dams according to the material type. Luo et al. [31] summarized the development characteristics and current research status of earth-rock dam breach research. Santos et al. [32] presented the potential failure modes, corresponding root causes, and the sequence of effects of tailing dams. On the basis of previous studies and statistical analysis of relevant data in China [13], the main risks of dam breach are divided into four categories: "overtopping", "structural instability", "seepage of dam body", and "seepage of dam foundation". Furthermore, the risk factors leading to these four risk events are identified according to the corresponding failure path. The analysis system takes into account the independence and generality of the risk factors so that it can more reasonably reflect the actual situation of the earth-rock dam breach accident, as shown in Table 1.

Among these risk factors, "Improper operation" refers to the overtopping caused by improper flood diversion or unauthorized elevation of flood limit water level in flood season, resulting in flood superimposition or excessive reservoir-carrying capacity. "A sudden drop in the reservoir water level" means that the upstream water level of a reservoir falls sharply due to various emergencies, such as damage of spillway, rapid flood diversion, and discharge, resulting in landslides on the reservoir bank or upstream the dam slope. "Improper seepage control" means that the interception treatment of the dam foundation and mountain joint surface is not thorough enough, or the grouting of the dam foundation does not meet the design standard, which aggravates the possibility of dam foundation leakage.

Table 1. Major risk factors of the earth-rock dam breach.


Among the four types of risk events, "Seepage of dam body" and "Seepage of dam foundation" are classified according to the location of the concentrated seepage. "Overtopping" is not only one of the risk events leading to dam breach but also a risk factor of "Structural instability". In addition, the same risk factor could be included in different kinds of risk events. For example, "storms or earthquakes" can not only cause overtopping through the indirect effect of backwater but also the instability of the dam structure directly.

# 2.2.2. Risk Assessment Model of the Earth-Rock Dam Breach 

As a convenient tool for the construction and analysis of the graphical model, the GeNIe software [24,33] is used to build risk assessment model and data reasoning, in which not only the joint probability distribution of ultimate node but also the probability of each parent node can be inferred through the two-way reasoning of the path.

By inputting basic data into the Bayesian network constructed in the GeNIe software, dynamic Bayesian network reasoning can be carried out. With machine learning, by updating the priori probability of nodes at different time steps, the results of the dynamic reasoning could be modified and integrated, which further improve the rationality of the evaluation. The flow chart is shown in Figure 4.

Combined with the determinant factors and analysis of the dam breach in Table 1, the dynamic Bayesian network model could be constructed. In the DBN model, each risk factor serves as the basic index, corresponding to the parent node at the top of the Bayesian network; "dam breach" serves as the end of reasoning and analysis, which is expressed as the final node; four types of risk events are not only the child nodes of risk factors but also the parent nodes of the final node. The progressive relationships among indicators are represented by directed arrows which are connected between nodes.

It is generally impossible or difficult for experts to directly evaluate the probability of composite indicators in an intuitive way. Furthermore, the dynamic changes of the upper-level indicators inevitably affect the next level of indicators, which realize the dynamic analysis of the whole system.

Based on these two considerations, the transition probabilities are only assigned to the nodes of primary indicators, whereas not to all nodes. The model is shown in Figure 5.
![img-3.jpeg](img-3.jpeg)

Figure 4. Risk assessment procedure for the dam breach of the earth-rock dam.
![img-4.jpeg](img-4.jpeg)

Figure 5. DBN model of the earth-rock dam breach.

The quantitative calculation in this model is accomplished by importing data into the software, which can be summarized as follows.

1. Setting the number of time steps that determined by actual needs in its setup interface.
2. Inputting the state probabilities and initial transition probabilities that have been drafted separately.
3. Inputting the virtual probabilities (the updated prior probabilities) of nodes in each time steps to update the status of them.
4. Running the software to complete the reasoning process.

# 2.2.3. Analysis of Indicators 

In view of the particularity of water engineering accidents and the difficulty in obtaining a large number of accident-related data, the expert scoring method is used to determine the indicator probability. It not only avoids the huge deviation caused by the dependency on historical data statistics purely but also combines the knowledge and experience of expert groups with practical projects.

The seven-level risk probability expression proposed by the Intergovernmental Panel on Climate Change (IPCC) is adopted to unify the probability expression of expert scoring and make the data easy to distinguish [34,35]. Considering the general range of failure probability of the dam breach is $10^{-5}-10^{-4}$ [27], all the probabilities are multiplied by $10^{-4}$ to make sense, as shown in Table 2.

Table 2. Probabilistic characterization of the IPCC (Intergovernmental Panel on Climate Change).


On the basis of the full study of engineering data, water engineering experts are organized to estimate the prior probability, conditional probability, and original transition probability of each node in the Bayesian network model. Considering the fact that expert scoring is an important link and the basis for the quantitative calculation of the model, the following principles should be followed in practical application:
(a) All indicators should be scored on the basis of the actual research data by experts with abundant theoretical knowledge and experience of water conservancy projects.
(b) The questionnaire should be explained in detail to ensure that experts can fully understand the meanings of different levels before the scoring is implemented. Especially in the formulation of conditional probability, the correlation between scoring items and upper indicators should be fully considered so that the scoring of the same items under different conditions can be distinguished.
(c) The items with large differences after scoring should be re-scored until the scoring values of the same index by different experts are in the same or adjacent interval in Table 2.

## 3. Results

Taking Shaheji Reservoir as an example, the dynamic Bayesian network evaluation model is used to evaluate the dam breach probability.

Shaheji Reservoir consists of a river dam, a spillway, an emergency spillway, and a power station at the dam toe. The height of the dam is 27.4 m , and the capacity of the reservoir is 211 million $\mathrm{m}^{3}$. The project was constructed in 1958 and was basically completed in 1979. After reservoir impoundment, many dangerous situations such as seepage behind the dam and dam body cracking have occurred.

Although it has been strengthened for many times, the hidden danger has not been completely eliminated, which brings great risks to the downstream.

# 3.1. Acquisition of Prior Probability and Conditional Probability 

The prior probabilities, conditional probabilities, and initial transition probabilities are evaluated by hydraulic engineering experts according to the scoring principles proposed above. Furthermore, the Leaky Noisy-Or gate extension model is used to take the unrecognized factors into account so as to further improve the accuracy of conditional probability. The probabilities calculations of "Overtopping" and "Seepage of dam foundation" in the DBN model are taken as examples to illustrate.

Setting "Overtopping" as event $X$, the representative parent nodes "Extreme flood", "Improper operation," and "Failure of sluice gate" are $X_{1}, X_{2}$, and $X_{3}$, respectively. The scores of the prior probability, conditional probability, and original transition probability in these parent nodes of event $X$ are shown in Table 3.

Table 3. Expert score table of node "Overtopping" $\left(\times 10^{-4}\right)$.


In the table above, " $X_{i}=1$ " indicates the occurrence of the event, while " $X_{i}=0$ " indicates that the event does not occur. $P\left(X_{i t}\right)$ denotes the original transition probability of event $i$, which can be understood as the probability that event $i$ still occurs in the current time step on the premise that this event has occurred in the previous time step.

The conditional probability of nodes "Overtopping" can be obtained by substituting the numerical values according to the Leaky Noisy-Or gate extension model, as shown in Table 4.

Table 4. Conditional probability parameters of Node "Overtopping" $\left(\times 10^{-4}\right)$.


Similarly, setting the "Seepage of dam foundation" as event $X$, the representative parent nodes "Failure of filter layer", "Paving cracks", and "Improper seepage control" are $X_{1}, X_{2}$, and $X_{3}$, respectively. The scores of the probabilities of these nodes are shown in Table 5, the conditional probability parameters are shown in Table 6.

Table 5. Expert score table of node "Seepage of dam foundation" $\left(\times 10^{-4}\right)$.


Table 6. Conditional probability parameters of Node "Seepage of dam foundation" $\left(\times 10^{-4}\right)$.


# 3.2. Dynamic Bayesian Network Reasoning and Results 

According to the methods of determining the prior probability and conditional probability of each factor mentioned above, the state probability values of each node were obtained in turn. Defining the number of time steps to 10 , the model can be reasoned by running the software.

The dynamic reasoning results of each node in the DBN model are shown in Table 7. The probability time series curves of the dam breach, the risk events, and risk factors are shown in Figures 6-8.

Table 7. Dynamic reasoning results $\left(\times 10^{-4}\right)$.


![img-5.jpeg](img-5.jpeg)

Figure 6. Time series variation curve of the dam breach probability.

![img-6.jpeg](img-6.jpeg)

Figure 7. Time series variation curves of the probability of risk events.
![img-7.jpeg](img-7.jpeg)

Figure 8. Cont.

![img-8.jpeg](img-8.jpeg)

Figure 8. Time series variation curves of probability of risk factors.

# 4. Discussion 

(1) According to the variation curve in Figure 6, the dam-breach risk of this earth-rock dam tends to change steadily on the whole, with a probability mostly below $33 \% \times 10^{-4}$. It can be seen from Table 2 that the dam-breach probability of this earth-rock dam is small and controllable in general. In addition, the probability of a dam breach reaches the highest in the third time step, which can be described as having a "medium probability" to breach. In view of the severe consequence of dam breach, this state means that the risk must be reduced through the intervention of management departments. Correspondingly, an emergency mechanism is also essential to be started up in this time step to prevent accidents.
(2) According to Figure 7, the probabilities of "Seepage of dam body" and "Seepage of dam foundation" are higher and more unstable than "Overtopping" and "Structural instability", which indicate that they are prone to occur and unstable along the time axis. Special attention should be paid to the prevention of these two types of risk events. According to Figure 8, the "Internal erosion" and "Settlement of dam body" show strong fluctuation on the time axis, which indicates that the transfer probability has a greater impact on these risk factors. Therefore, it is necessary to strengthen the monitoring and regular investigation of such hidden risks in future work, with a good job of early warning to prevent these dangers.
(3) Due to the fact that the evaluation of indicators in quantitative calculation is based on expert experience, the node probabilities in this paper do not represent precise values but are intended to concisely reflect the possibility of their occurrence and provide a reference for decision-makers. Likewise, the exact probability can be calculated by combining this model with other methods. In addition, there may be some limitations in the practical engineering of this research method because of the theoretical hypotheses of this study; multiple evaluation methods can be used to verify each other to improve the accuracy of the evaluation results.
(4) Compared with other traditional risk analysis methods, this method does not cause a deviation in the final results due to the lack or distortion of information on a certain time node. Moreover, with the supplement and improvement of the information of each node, the evaluation results will be more accurate and reliable.

## 5. Conclusions

In view of the dynamic characteristics of risk and shortcomings of traditional risk analysis methods, this paper introduces time factors into a static Bayesian network, establishing a dynamic risk evaluation model. In this study, Bayesian theory, machine learning, and expert knowledge are inseparably interconnected. It reflects the dynamic variation by transferring probability and complements mathematical theory with expert knowledge, so as to realize the evaluation and

prediction of probability. In this way, the variation curve of the dam breach probability along the time axis and the risk indexes with strong fluctuation are obtained. Meanwhile, the Leaky Noisy-Or gate extension model was introduced to determine the conditional probability. Taking the Shaheji dam as an example, the characteristics of the dam breach risk variation are obtained, which indicates that the dynamic Bayesian network is preferable and can provide a reference for risk analysis of similar projects.

Author Contributions: Conceptualization-W.G. and T.W.; methodology-T.W.; validation-Z.L., D.W. and T.W.; formal analysis-Z.L. and T.W; investigation-W.G. and H.L.; writing—original draft preparation-W.G. and T.W.; writing-review and editing-W.G. and Z.L.; supervision-Z.L.; funding acquisition-W.G. and Z.L.

Funding: This research was funded by the National Natural Science Foundation of China (Grant No. 51709239, 51679222, 51379192), the China Postdoctoral Science Foundation (Grant No. 2018M632809), the Science and Technology Project of Henan Province of China (Grant No. 182102311070), the Key Project of Science and Technology Research of Education Department of Henan Province of China (Grant No. 18A570007) and the Science and Technology Project of Water Conservancy of Henan Province of China (Grant No. GG201813).
Conflicts of Interest: The authors declare no conflict of interest.
