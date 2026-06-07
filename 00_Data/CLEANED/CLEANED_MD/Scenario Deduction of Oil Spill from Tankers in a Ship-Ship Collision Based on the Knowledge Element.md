# Scenario Deduction of Oil Spill from Tankers in a Ship-Ship Collision Based on the Knowledge Element and Dynamic Bayesian Network 

Min Zeng ${ }^{1}$, Yao-yao Wei ${ }^{1}$, Kang-xin Yu ${ }^{1}$, Hai-nan Huang ${ }^{1,2}$, Tian Xie ${ }^{1 *}$<br>${ }^{1}$ School of Economics, Management and Law, University of South China, Hengyang 421001, China<br>${ }^{2}$ School of Management, Jinan University, Guangzhou 510632, China

Received: 1 November 2023
Accepted: 21 December 2023


#### Abstract

Oil tankers carry large quantities of liquefied chemical cargoes that are flammable, explosive and/or toxic. Hence, a collision with a tanker that causes an oil spill poses a severe threat to the marine environment and human life. In order to quantify and analyze the risk factors of ship collision oil spill, this paper adopts a combination of knowledge element (KE) and dynamic Bayesian networks (DBN) to conduct an emergency scenario study based on the "scenario-response" model. Firstly, the key elements of "accident scenario state, human factors, emergency measures, and emergency goals" are selected to represent the accident. Then, the mechanism of accident evolution is analyzed according to the case, and DBN is used to build a scenario model of oil spills from tanker collisions. Finally, to verify the importance of human factors and the scientificity of emergency measures, the oil spill accident due to the collision between the two vessels known as MT "SANCHI" and MV "CF CRYSTAL" is used as an example for analysis. The accident model deduction results are in line with reality, and the research results help relevant decision makers to understand the deduction process of oil spills from tanker collisions, which is of great significance to enhance the safety of oil tanker shipping and marine environmental protection.


Keywords: bayesian network, emergency scenario projection, knowledge element, marine pollution, oil spills

## Introduction

Oil spills have become one of the world's most severe marine ecological disasters. According to International Tanker Owners Pollution Federation [1] survey

[^0]statistics, from 1970 to 2021, about 5.87 million tons of oil were spilled globally due to tanker accidents, and most of the oil spills ( $>7$ tons) were caused by collisions. The collision of oil tankers at sea, especially large ships, often leads to major oil spill accidents, which cause not only huge economic losses to shipping enterprises and endanger public health, but also cause serious pollution to the marine ecological environment, destroy the marine ecosystem, and restrict the sustainable development


[^0]:    *e-mail: thanksky709394@163.com

of the society's economy [2]. Therefore, the maritime regulator (IMO-International Maritime Organization) has adopted strict regulations to regulate the transport of these goods. MARPOL 73/78 (International Convention for the Prevention of Marine Pollution from Ships) is one of the fundamental conventions for preventing marine pollution from ships [3]. These show that it is essential to analyze the risk factors of oil spill collision and its evolution mechanism to prevent accident risks and to improve emergency management decisions for maritime safety and marine environmental protection [4].

From a static perspective, more than $80 \%$ of tanker accidents are caused by human errors [5, 6]. Meanwhile, studies have assessed the contribution of various risk factors from "human-machine-environmental-control" to tanker pollution accidents and confirmed that human factors account for the largest share of ship collision pollution accidents and are the primary consideration [7-9]. In these studies, scholars have analyzed the role of human factors in ship collisions [8] and identified the causal chain of human errors that can help to reduce the accident rate $[5,9]$ assessed the contribution of human error to the risk of chemical spills from tankers and emphasized that improving the safety of human behavior in maritime transport is essential to reduce the risk of marine pollution. Thus, human factors have a significant impact on the development of ship collision oil spills before, during, and after the incident.

From a dynamic perspective, major ship oil spills, as a type of emergency with serious consequences, are typical of unconventional emergencies because their
precursors are not obvious, their evolution paths are complex and uncertain, and they involve a wide range of damage and potential secondary hazards. The essence of scenario construction is to identify accident constituents and states, which can help emergency decision-making subjects identify critical and controllable factors of disaster accidents, reduce information ambiguity, and reduce decision-making errors [10]. Therefore, "emergency decision-making" has become a mainstream trend in emergency analysis [10, 11]. In terms of scenario construction for oil spill accidents, there are methods to construct marine oil spill scenarios based on structural equations [12], flat text for semantic analysis [13], and hydrodynamic model [14]. In terms of accident machine risk analysis and emergency management, Bayesian Networks (BNs) are often used as modeling tools for risk quantification [15]. Goerlandt and Montewka [4] proposed a risk analysis framework for marine transportation systems in the case of oil spill risk in the Gulf of Finland, in which BN was used as a modeling tool for risk quantification, and the study showed that the model is reasonable for ship collision oil spill risk analysis. To improve the accessibility and accuracy of emergency evolutionary reasoning, Wang and Liu [16] constructed a hybrid inference model based on KE for emergency scenario deduction. At present, there are not many studies on sudden oil spills at sea focusing on the assessment of risk factors and causation analysis of accidents, and the corresponding auxiliary emergency decisions for oil spills at sea are mostly based on oil spill trajectory simulation and historical case matching. However, there
![img-0.jpeg](img-0.jpeg)

Fig. 1. Overall framework and approach of this paper.

are almost no scenario deduction studies that directly address tanker oil spill accidents in large ship-ship collisions at sea, and the scenario deduction on ship oil spill accidents is often single, with less consideration of the coupling of risk factors and the interaction between basic scenarios, and without considering the impact of the emergency response capability of ship enterprises and crew on accident development.

In summary, this paper intends to fully consider the human factors in the oil spill accident process. At the same time, the accident belongs to a typical unconventional emergency. Using KE to express its scenario [17], we can concretely analyze the key factors affecting this kind of disaster accident's initial, development, and evolution, which is the premise of constructing DBN. The combination of DBN and fuzzy set theory can solve the problems of dynamic and incomplete information of the evolution of emergency accidents. Combined with the above technical advantages, the scenario inference model constructed in this study can quantitatively and qualitatively analyze the risk factors of major oil spills from tankers and their interaction relationship. By identifying the key risk elements and predicting the accident scenarios that will occur during the development of the accident, it can scientifically describe the evolution path of the accident and the possible scenario results of the final accident, and provide a more accurate assessment of the emergency response and loss prevention of the oil spill accident of the oil tanker in the ship-ship collision. The accident scenario deduction mechanism revealed by the research results will provide a scientific basis for decision-makers to make correct emergency countermeasures in the emergency response process after collision accidents in oil tanker marine transportation, which is significant in reducing the risk of marine environmental pollution.

The rest of this paper is as follows: In the second section, the theory and method of applying the research model are introduced, and by collecting cases of oil spill accidents caused by ship collisions, the evolution law of accident scenarios is analyzed, and the scenario deduction model of oil spill accidents caused by oil tanker collisions is constructed. In the third section, the application of the construction mold in an accident example and the discussion of the results are carried out. Finally, Section 4 gives the conclusion. Fig. 1 shows the details of each step.

## Materials and Methods

Scenario Representation of Oil Spill
from Tankers in Ship-to-Ship Collision

## Knowledge Element Theory

KE is an abstract representation of the basic concepts, characteristics, and properties of objective things and is
the smallest unit of knowledge that cannot be divided anymore [18]. KE can be a concept, rule, fact, or method [19]. KE has the characteristics of good transitivity, extensibility, and relational expression. It does not depend on specific knowledge domains and specific situations, and has a specific and complete representation structure. Therefore, it can better cope with the complex reasoning problem of the evolution of emergencies and interpret the common characteristics and complex laws of the evolution of emergencies [16]. With this technical advantage, knowledge elements have been widely used in emergency management of emergencies across disciplines and fields [10, 16]. Scenario construction for non-conventional emergencies can be applied to the knowledge triad [19], which consists of three sets of concepts and attribute name sets describing the thing, attribute state sets, and interrelationships between attributes, which are described as follows.

$$
k_{m}=\left\{N_{m}, A_{m}, R_{m}\right\}, m \in M
$$

Where $M$ is the set of description objects; $N_{m}$ is the name and concept of emergent event objects, $A_{m}$ is the set of corresponding attribute states, and $R_{m}$ is the set of relationship descriptions between scenario elements.

$$
A_{m}=A_{m}^{l} \cup A_{m}^{s} \cup A_{m}^{o}
$$

where $A_{m}{ }^{l}$ is the input attribute, $A_{m}{ }^{s}$ is the state attribute, and $A_{m}{ }^{\circ}$ is the output attribute.

$$
k_{a}=\left(p_{a}, d_{a}, f_{a}\right), a \in A_{m}
$$

The attribute knowledge element $k_{a}$ corresponds to $A_{m}$, and the thing attribute is $a \in A_{m}$. In this formula, $p_{a}$ is a measurable or describable characteristic, $d_{a}$ is a measurable measure, and $f_{a}$ is a numerical or timevarying function.

$$
k_{r}=\left(p_{r}, A_{r}^{l}, A_{r}^{o}, f_{r}\right), r \in R_{m}
$$

The attribute state relationship in the relational knowledge element $k_{r}$ is $r \in R_{m}, p_{r}$ is the mapping attribute description, $A_{r}{ }^{l}$ is the input attribute state set, $A_{r}{ }^{\circ}$. is the output attribute state set, and $f$ is the mapping function, i.e., for $A_{r}{ }^{\circ}=f_{r}\left(A_{r}{ }^{l}\right)$. When $p_{r} \neq \varnothing, A_{r}{ }^{\circ} \neq \varnothing$ and $f_{r} \neq \varnothing$ of the formula, the generic knowledge metamodel can be described as follows.

$$
K_{f}=\bigcup_{m \in M}\left(k_{m} \bigcup_{a \in A m}\left(k_{a} \bigcup_{r \in R m} k_{r}\right)\right)
$$

## The Constituent Elements of Situational KE and the Law of Situational Evolution

Understanding the evolution process and law of offshore oil tanker collision and oil spill accidents and grasping the critical scenarios and their characteristics are the basis and prerequisites for building accident

extrapolation models. In this paper, we counted 34 (24 in China and 10 in other countries) major oil tanker collision and oil spill accidents worldwide from 1972 to 2021, and some cases are shown in Table 1. The leading causes of tanker oil spill accidents in ship collisions include negligence in the lookout, violation of regulations, failure to take effective avoidance action, and failure to take oil spill emergency measures. Human error is the direct cause of the ship collision accident and the critical factor in promoting the evolution of the accident, so human factors are important factors in the tanker collision oil spill risk. The bulk oil or refined oil carried by tankers is a very complex organic mixture, which is flammable, explosive, and toxic. This disastercausing property is carried out in the whole process of the accident. Therefore, in this study, the object's risk is taken as the hypothetical premise of the accident deduction, and it is not extracted separately as the scene element. In the analysis of the case combined with the SOM network scenario evolution expression proposed by Jiang and Huang [19], the scenario KEs of a ship-ship collision oil spill accident are divided into: (i) scenario state (S), which mainly refers to the state of the emergency object, including the disastercausing body scenario state and the disaster-bearing body scenario state; (ii) human factors, represented by H ; (iii) emergency measures (M) refer to the disposal behaviors and measures taken by the emergency object, such as the crew on duty and the maritime authority oil spill response department; (iv) emergency target (O) (Fig. 2). These four scenario elements interact with each other to form a basic unit of scenario evolution. The human factor acts with the scenario state, the emergency measures constrain the scenario state, and the emergency objectives are both influenced by the scenario state and the following scenario state.

An outbreak undergoes a total of n transitions of scenario states from occurrence to disappearance. The scenario states are denoted as $\mathrm{S} 0, \mathrm{~S} 1, \mathrm{~S} 2, \mathrm{~S} 3, \ldots, \mathrm{Sn}-1$, Sn . The moments of each state are $t_{0}, t_{1}, t_{2}, \ldots, t_{n-1}$, and $\mathrm{t}_{\mathrm{n}}$. Briefly, the overall phase of the accident can be divided into the initial phase, the development phase, and the disappearance phase. As shown in Fig. 3, it is assumed that at a certain moment, the initial scenario S 1 of the accident appears under the influence of some disastercausing factor. If the decision maker takes timely and effective emergency measures (M1) can avoid further development of the accident. In this process, there is a human error H 1 , and with the evolution of the disaster accident itself, various possible intermediate scenarios will appear. If these accident scenarios receive an effective emergency response, the situation can be controlled to continue to evolve so that the accident disappears as soon as possible. Otherwise, these scenario states evolve again, and the next scenario state has multiple possibilities. Assuming that the new state is determined as S 2 , corresponding to having O 2 , the scenario state continues to change under the influence of H 2 and M2. And so on, until the moment $t_{n}$, the scenario disappears, the whole emergency response process ends, and the scenario evolution process is terminated.

## Analysis of the Evolution Path of the Scenario of Major Oil Spills from Tankers

Generally speaking, after an accident occurs, it evolves into multiple possibilities because of its evolution and human intervention response to the disaster. Different decision makers will set different emergency goals and measure each scenario state. At the same time, human errors occur during the intervention of emergency subjects. Improper emergency measures

Table 1. Typical cases of oil spills from tankers collision.


![img-1.jpeg](img-1.jpeg)

Fig. 2. Knowledge elements for tanker spill scenarios.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Schematic diagram of the evolution law of the accident scenario.
can undermine and interfere with emergency goals and situational states. Therefore, it can be roughly divided into two evolutionary paths [20]. One is to reduce human error as much as possible in the process of evolution and take emergency measures to achieve the corresponding emergency target so that the evolution of disaster and accident will develop in the desired direction. The accident will quickly calm down to minimize the loss. The other is not to achieve the corresponding emergency target. The accident continues to deteriorate, causing more severe derivative or secondary disaster accidents.

Constructing the Scenario Network Model of Oil Spill Accidents

$$
B N
$$

BN is based on probability distribution and graph theory and is a directed acyclic graph (DAG) with nodes and directed edges and a conditional probability table (CPT) to represent the strength of dependencies between nodes. Nodal variables can be an abstraction of any problem and are suitable for expressing and analyzing events with ambiguity and probability, enabling relatively accurate reasoning from incomplete,

imprecise, or uncertain information and knowledge. BN is one of the most effective models for uncertain knowledge representation and reasoning [18, 20]. The DBN [21] adds the time factor $t$ to the static Bayesian network, making the temporal reasoning of sudden disaster accidents consistent and continuous with the event development and more aligned with the objective reality. The mathematical basis of inference in DBN is the full probability formula and the conditional probability formula, which is used $x$ to denote the set of causes or the set of parents of causal relationships in DBN, and y to denote the set of outcomes or children of causal relationships in DBN, then there is $x \rightarrow y$. where the set $x$ contains $n$ elements, each element is noted as $x_{i}$, then there is $x_{i} \in x(i=1,2,3, \ldots, n)$ and the full probability formula is

$$
\begin{aligned}
P(y)=P(y x) & =P\left(y x_{1}+y x_{2}+\cdots y^{x_{n}}\right)=P\left(y x_{1}\right) \\
& +P\left(y x_{2}\right)+\cdots P\left(y x_{n}\right)
\end{aligned}
$$

From (Eq. 6), it is clear that full probability is essentially the inference of an outcome from a cause, while the Bayesian formula is the opposite, being the inference of the probability of a cause occurring if the outcome is known.

$$
P\left(x_{i} \mid y\right)=\frac{P\left(x_{i} y\right)}{y} \frac{P\left(x_{i}\right) p(y \mid x)}{\left(x_{i+1}^{n} P\left(x_{i}\right) P\left(y \mid x_{j}\right)\right)}
$$

Since BN inference implicitly assumes a premise of conditional independence, the joint probability of all nodes represented by BN can be expressed as the product of the conditional probabilities of individual nodes.

$$
\begin{gathered}
P\left(x_{1}, x_{2}, \cdots, x_{n}\right)=\Pi_{i=1}^{n} P\left(x_{i} \mid x_{1}, x_{2}, \cdots, x_{i-1}\right) \\
=\Pi_{i=1}^{n} P\left(x_{i} \mid P_{n}\left(x_{i}\right)\right)
\end{gathered}
$$

where is the set of parent nodes. The DBN is essentially the expanded form of the static BN on the time axis. Suppose there are $t$ existing time segments with $n$ hidden nodes and $m$ observed nodes, $x_{i j}$ is a fetching state, $y_{i j}$ is an observation, and $P_{n}\left(y_{i j}\right)$ is the set of parent nodes of $y_{i j}[22]$.

$$
\begin{gathered}
P\left(x_{11}, x_{12}, \ldots, x_{\mathrm{f} 1}, \ldots, x_{\mathrm{fn}} \mid y_{11}, y_{12}, \ldots, y_{\mathrm{tm}}, \ldots, y_{\mathrm{f} 1}, y_{\mathrm{f} 2}, \ldots, y_{\mathrm{fn}}\right) \\
\quad=\frac{\Pi_{12} P\left(y_{12} \mid P_{0}\left(y_{1 j}\right)\right) \Pi_{18} P\left(y_{18} \mid P_{0}\left(y_{18}\right)\right)}{\sum x_{11}, x_{12}, \cdots x_{\mathrm{f} 1}, x_{\mathrm{f} 2} \Pi_{12} P\left(y_{12} \mid P_{0}\left(y_{18}\right)\right)}
\end{gathered}
$$

## Constructing a DBN for Accident Scenario Evolution

The construction of a DBN for an unexpected event scenario can be divided into three steps.

Step 1: Determine the node variables of the network. According to the classification of scenario knowledge
elements, the corresponding network node types are determined by using historical cases or domain expert judgments. The results of the critical elements data table are the variables of network nodes.

Step 2: Determine the causal relationships of the node variables in the network. First, the whole scene elements are connected in series according to the emergency's initial stage, development stage, and disappearance stage. Then, according to the chronological order, it mainly unfolds from two paths. One is the horizontal path: the situation state evolves in the optimistic direction. The second is the longitudinal path: the scenario state evolves in a pessimistic direction. Finally, a complete emergency scenario network is formed by drawing it with directed edges.

Step 3: Determine the probability of network node variables. The prior probabilities of some network node variables are determined according to the historical statistics of such disasters and accidents. Then the state probabilities of scenario states are calculated using the prior probabilities or expert estimation probabilities to deduce the occurrence probability of the following scenario state, and so on to complete the whole scenario inference process.

## Determine the Probability of the BN Model

Due to incomplete representation of the unconventional contingency itself, insufficient data from previous similar cases, and limitations of people's conditions, people are not aware of the conditions or objective causes of the occurrence of the contingency. Almost all unconventional contingency scenario projections are conducted under uncertain conditions, which makes it difficult to use rigorous logical reasoning methods like mathematics and physics. Therefore, fuzzy information processing and its methods are crucial in scenario deduction - the contribution of fuzzy set theory, created by Zadeh [23] is the introduction of the concept of "subordination," a mathematical way of dealing with the fuzziness of things, i.e., using the interval $[0,1]$ as a measure. For cases where data were not directly available, a combination of expert experience and fuzzy theory was used to assist in estimating the conditional probabilities. To ensure the reliability of subjective expert judgments, each expert's background, including factors such as years of work, education, and professional status were graded [5, 24, 25]. Then an average arithmetic method was used to obtain reasonable weighting factors (Table 2). Human memory capacity is generally estimated at seven plus or minus two patches [26], and the number of linguistic expressions that facilitate experts to make appropriate judgment choices is usually five. Therefore, this paper uses trapezoidal fuzzy numbers to represent expert opinions, classifying the likelihood of accidents into five linguistic variables: VH, H, M, L, VL (Table 3).

Four parameters will represent the trapezoidal fuzzy number. And the fuzzy set will be denoted as

Table 2. Weighting scores of experts.


Table 3. Linguistic expressions and corresponding TrFNs.


$A=(a, m, n, b)$, whose affiliation function equation is (Eq. 10):

$$
\mu_{A}(x) \begin{cases}\frac{x-a}{a-m} & (a \leq x<m) \\ \frac{1}{b-x} & (m \leq x<n) \\ \frac{b-n}{0} & (n \leq x<b) \\ & \text { (other) }\end{cases}
$$

Collect the expert data and convert the expert judgments into fuzzy numbers. If n experts' opinions are collected, the probability of the $i$ th node $A i$ given by the $k$ th expert is transformed into a trapezoidal fuzzy number (Table 1), taking into account the experts' weights and processed by arithmetic averaging method thus to an aggregated value.

$$
\begin{gathered}
p_{l}^{\prime}=\left(W_{l}^{1} \times P_{l}^{\prime}\right) \oplus\left(W_{l}^{2} \times P_{l}^{2}\right) \oplus\left(W_{l}^{3} \times P_{l}^{3}\right) \\
\cdots\left(W_{l}^{n} \times P_{l}^{n}\right)=\left(a_{l}^{\prime}, m_{l}^{\prime}, n_{l}^{\prime}, b_{l}^{\prime}\right)
\end{gathered}
$$

The fuzzy number is solved (Eq. 11), and the areamean method is used to denazify the fuzzy results and get the fuzzy values of the nodes (Eq. 12).

$$
M^{*}=\frac{a_{l}^{\prime}+m_{l}^{\prime}+n_{l}^{\prime}+b_{l}^{\prime}}{4}
$$

Normalize the probability information of the nodes to obtain the prior probabilities of the relevant nodes (Eq. 13).

$$
P_{l}=M^{*} / \Sigma_{l=1}^{n} M^{*}
$$

## Results and Discussion

## Case Study

On January 6, 2018, the collision between the oil tanker Sanchi carrying condensate and the bulk carrier CF CRYSTAL occurred in the waters about 160 nautical miles east of the mouth of the Yangtze River, resulting in a total loss of 136,000 tons of condensate and more than 1,000 tons of bunker oil into the East China Sea. It became the first case in the history of world shipping where a tanker carrying condensate was hit and caught fire, resulting in a total loss of the ship. The oil spill caused a large area of oil pollution in the sea, and the combustion and explosion released a large amount of toxic gas. As there is no oil tanker carrying "condensate" in the history of world shipping, there is no precedent for pollution emergency disposal, which is a typical unconventional accident [27]. Through this accident report [28], the time sequence and critical situation of the accident development are sorted out (Fig. 4).

## Accident Scenario Representation and Evolutionary Path Analysis

The development process of an oil spill accident in a tanker collision can be simply divided into the initial phase, development phase, and disappearance phase. The initial phase is the period from the appearance of collision hazard-related causative factors to the occurrence of the accident. In order to identify the human factors and emergency initiatives in this accident prevention phase, the collision avoidance process is subdivided into three phases: perception, decision, and action, according to the human cognitive model (Fig. 5). Based on the 308 ship collision accident investigation reports from the China Maritime Safety Administration and the results of existing studies [9, 29, 30], the knowledge meta-theory was applied to extract key scenarios for the oil spill accident process. As shown in Table 4, 14 accident scenario states, 7 human factors, 7 emergency response objectives, and 7 emergency response activities were identified as BN variables, and the identified node variables were connected to form an accident BN scenario derivation diagram (Fig. 6).

![img-3.jpeg](img-3.jpeg)

Fig. 4. Scenario development process of the oil spill accident of "Sanchi" oil tanker.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Collision avoidance process in disaster accident prevention stage [7].

Table 4. Situational knowledge element.


## Calculating Accident Scenario Probabilities

Taking 34 major oil vessel collision cases as samples and combining them with the tanker oil spill statistical analysis report in 2021, the official website data of the Maritime Safety Administration of the Republic of China, the Guangdong Maritime Safety Administration, and the Shandong Maritime Safety Administration, statistical analysis were conducted to determine the probability of some nodes. The results are shown in

Table 5 [30]. Five experts in related fields determine the probability of other nodes, and the weight of each expert is calculated by Table 2 and Equation (10). The weights of the five experts are $0.26,0.23,0.19,0.17$ and 0.15 . The fuzzy expert language is successively calculated according to Eqs. (11-13) to obtain the conditional probability of each node (Table 6).

Equation (9) was used to obtain the state probability of each node with the help of GeNIe software, and the DBN scenario inference diagram was obtained (Fig. 7).
![img-5.jpeg](img-5.jpeg)

Fig. 6. Evolution path diagram of collision accident scenario.

Table 5. Partial node probabilities.


## Result Analysis

In the initial stage of the accident. Through the BN model, it can be seen that when the cross-encounter situation was formed ( $\mathrm{S} 1=100 \%$ ), the ship had improper lookout (H1), misjudgment of danger (H2), and a slight turn to the right (H4) 15 minutes before the collision of CF Crystal. Furthermore, in terms of emergency measures, the pilot of CF Crystal did not compare and synthesize the AIS information with radar information (M1), which led to the error in information judgment. The ship did not make effective contact with each other (M2) and did not take practical collision avoidance actions in time (M4). The node probability of an oil spill

Table 6. Conditional probabilities of scenario node variables.


Table 6. Continued.


accident due to the collision between the two vessels is $96.23 \%$. Other conditions remain unchanged. When the improper lookout of H 1 is F , scenario S 1 increases to $88.32 \%$ in the optimistic direction, scenario S2, but the occurrence probability of scenario node S6 is $94.11 \%$, showing little change. When H 2 is F , S 6 is reduced to $87.38 \%$. If M2 is adopted simultaneously, S3 is increased to $49.19 \%$, and S 6 is reduced to $83 \%$. When H 4 is F , the probability of S 6 is $93.33 \%$. If the corresponding emergency measure M4 is taken simultaneously, the probability of S6 is $89.43 \%$. Other conditions remain unchanged, $\mathrm{H} 1, \mathrm{H} 2$, and H 3 are all F , and corresponding emergency measures are taken to reduce the occurrence probability of S6 to $51.68 \%$ (Fig. 8). It can be seen that errors in hazard judgment/decision-making pose a significant risk to collisions. The incidence of collision oil spills can be effectively reduced if crew members' human errors in the formation of collision avoidance behavior are reduced at all stages of the process. In addition, it is essential to note that effective avoidance behavior also requires early and timely.

From the result data, we can find that the scenarios with the highest probability of occurrence are collision oil spill (S6), continued oil leakage (S7), fire spreading and explosion (S11), and pollution spreading to the sea (S9), with probabilities of $96.23 \%, 87.5 \%, 74.99 \%$, and $70.66 \%$ respectively. Since the cargo of the oil tanker Sanchi is condensate, which is highly flammable, explosive, and toxic, and the cargo volume is 136,000 tons, the probability of secondary disasters is high. It can be seen that the results of the extrapolation by the BN in this paper are consistent with the actual situation.

The development stage of the accident. After the incident, another condition is unchanged; the probability of scenario S6 toward the pessimistic direction of scenario S11 is reduced by $11.7 \%$ if the ship's enterprise has a primary emergency management mechanism and emergency plan (H6 = False). At the same time, the crew actively isolates the spilled oil from contacting the cargo source (M6 = Ture). Other things being equal, the probability of scenario S7 towards the promising direction of scenario S8 increases by $30.11 \%$ when
![img-6.jpeg](img-6.jpeg)

Fig. 7. State the probability of each node variable for the oil spill accident of "Sanchi" .

![img-7.jpeg](img-7.jpeg)

Fig. 8. Probability diagram when H1, H2 and H3 are F and M1, M2 and M3 are T.
the crew has adequate emergency response training (H7 = False). Other things being equal, the probability of scenario S9 occurring in the promising direction of scenario S10 increases by $24.08 \%$ when the oil spill response team and material response are adequate (H9 = False). Other things being equal, the probability of scenario S11 occurring in the promising direction of scenario S12 increased by $13.87 \%$ when the crew had adequate emergency response training and emergency response drills (H11 = False). Hence, it can be seen that during the accident development stage, the emergency measures of ship enterprises generally prefer to send alarm signals and evacuate people to reduce the danger from secondary hazards. Furthermore, maritime departments tend to clean up and pump oil operations for oil spill accidents. Regarding human factors, emphasis should be placed on emergency training for crew members and strengthening emergency drills, which will help enhance the response capability to oil spill accidents and secondary disasters. At the same time to cope with such unconventional major oil spill accidents, relevant departments should grow the emergency rescue team and improve the reserve of materials to ensure that the scope of pollution impact can be controlled effectively in time.

## Conclusion

From the perspective of "scenario-response" research, this paper adopts the knowledge meta-theory as the basis to express the scenario evolution of major oil tanker collision and oil spill accidents at sea by using four types of knowledge meta-elements: "scenario state, human factors, emergency measures, and emergency goals." It not only clearly represents the key elements that affect the occurrence of such a disaster, but also visually describes the evolution of the scenario in the accident and derives all possible scenario evolution paths in the emergency response process.

Considering that an oil spill from a tanker in a ship-ship collision is different from other types of
marine oil spill accidents, the scenario of this accident is represented as the "oil spill prevention phasedevalopment phase - disappearance phase." BNs are used to quantify the risk factors in the accident, and time nodes are added. The DBN allows for continuity in the extrapolation process.

The empirical application analysis shows that the extrapolation results of the constructed scenario evolution model of tanker oil spill accident in a shipship collision can accurately reflect the actual situation and can be used to sort out the whole process of oil spill accident in a tanker collision. The scenario evolution can predict the most likely scenario in the next moment, which helps emergency decision makers to grasp the evolution path of marine emergencies and predict the probability of derivative disasters to make scientific emergency decisions and effective emergency measures as early as possible. In addition, it also helps ship enterprises and crew members to clearly understand the human-centered risk elements so that they can make scientific emergency decisions and effective emergency measures as early as possible to reduce unsafe human behaviors and improve the safety level of tanker marine transportation.

Since such major oil spill accidents are unconventional emergencies, there is the problem of insufficient information. Although expert judgment and fuzzy mathematics are adopted to quantify some elements' a priori probability and conditional probability, the influencing factors of the evolution process of oil tanker collision and oil spill accidents are complex and diverse. The subsequent research can use IoT technology to optimize the parameters of each node of the BN model's parameters to improve the quasiaccuracy of this model data.

## Acknowledgments

The paper is supported by National Natural Science Foundation of China (No. 71974090); Philosophy and Social Science Foundation of Hunan Province of China

(18YBQ105); Youth talents support program of Hunan Province of China (2018HXQ03); Key scientific research project of Education Department (20A443); Social Science Key Breeding Project of USC (2018XZX16); Doctoral scientific research foundation of USC (No. 2013XQD27); Philosophy and Social Science Foundation Youth Project of Hunan Province of China (19YBQ093); Scientific research project of Education Department (No. 20C1625); State Scholarship Fund (202108430098) from CSC; State Scholarship Fund (202208430061) from CSC; Postgraduate Scientific Research Innovation Project of Hunan Province (QL20210217).

## Conflict of Interest

The authors declare no conflict of interest.
