# Article 

## Fire Accident Risk Analysis of Lithium Battery Energy Storage Systems during Maritime Transportation

Chunchang Zhang ${ }^{1}$, Hu Sun ${ }^{1}$, Yuanyuan Zhang ${ }^{1}$, Gen $\mathrm{Li}^{1, *}$, Shibo $\mathrm{Li}^{1}$, Junyu Chang ${ }^{1}$ and Gongqian Shi ${ }^{2}$

## check for updates

Citation: Zhang, C.; Sun, H.; Zhang, Y.; Li, G.; Li, S.; Chang, J.; Shi, G. Fire Accident Risk Analysis of Lithium Battery Energy Storage Systems during Maritime Transportation. Sustainability 2023, 15, 14198. https://doi.org/10.3390/ su151914198

Academic Editor: Matjaž Šraml
Received: 18 August 2023
Revised: 15 September 2023
Accepted: 18 September 2023
Published: 26 September 2023

## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Merchant Marine College, Shanghai Maritime University, Shanghai 201306, China; cczhang@shmtu.edu.cn (C.Z.); 202230110120@stu.shmtu.edu.cn (H.S.); 202230110121@stu.shmtu.edu.cn (Y.Z.); sbli@shmtu.edu.cn (S.L.); jychang@shmtu.edu.cn (J.C.)
2 Shanghai Merchant Ship Design Research Institute, Shanghai 201210, China; shigq2633@163.com

* Correspondence: gli@shmtu.edu.cn

Abstract: The lithium battery energy storage system (LBESS) has been rapidly developed and applied in engineering in recent years. Maritime transportation has the advantages of large volume, low cost, and less energy consumption, which is the main transportation mode for importing and exporting LBESS; nevertheless, a fire accident is the leading accident type in the transportation process of LBESS. This paper applied fault tree analysis and Bayesian network methods to evaluate the fire accident risk of LBESS in the process of maritime transportation. The Bayesian network was constructed via GeNIe 2.3 software, and the probability of LBESS fire accidents during maritime transportation was calculated based on the probability of basic events occurring. The results showed that an unsuitable firefighting system for putting out lithium battery fires, high humidity, and monitoring equipment without a real-time alarm function have the most significant influence on the occurrence of LBESS fire accidents during maritime transportation. The research work of this paper provides a theoretical basis for the risk assessment of LBESS during maritime transportation.

Keywords: risk assessment; Bayesian network; lithium battery energy storage system; maritime transportation; fire accident

## 1. Introduction

In order to reduce global greenhouse gas emissions, the use of renewable energy has received more and more attention. Wind and solar power generation are the main ways of renewable energy utilization, and according to statistics, the power generation of both accounted for $10 \%$ of the total global power generation in 2021 [1]. Solar and wind power generation have inherent defects of intermittent power generation. Therefore, it is necessary to use energy storage systems with sufficient capacity to solve the above problems [2,3].

With the continuous progress of battery technology and its cost reduction, the electrochemical energy storage systems mainly based on lithium-ion batteries have been rapidly developed and applied in recent years [4]. As the application demand for lithium battery energy storage systems increases significantly, the transportation demand for lithium battery energy storage systems also rises. Maritime transportation has the advantages of large volume, low cost, and less energy consumption. Therefore, it is the main transportation mode for the import and export of LBESS. A lithium-ion battery energy storage system (LBESS) is usually composed of a low boiling point and a flammable organic electrolyte. High temperature, vibration, and other external environmental factors may trigger the thermal runaway of LBESS, leading to fire accidents [5]. A fire accident is the main type of accident during transportation of LBESS. Maritime transportation is characterized by high vibration, high temperature, high humidity, and possible collision, which may cause fire accidents. Therefore, it is necessary to evaluate the fire risk during the transportation of lithium battery energy storage systems.

At present, there is little research on the fire accident assessment of LBESS during maritime transportation. This paper summarizes the research on the fire risk assessment of lithium batteries and the risk of accidents in maritime transportation. I. Cho et al. used the interquartile range filter method to monitor the fire risk during the operation of a battery pack in real-time. The proposed method was verified via experiment and used to monitor the fire risk of battery packs used for railway vehicles [6]. A local outlier factor method was proposed to detect the abuse conditions of batteries to prevent thermal runaway. The proposed method was verified by detecting faulty cells at different shortcircuit conditions [7]. Fire dynamics software was used to simulate different fire conditions of lithium batteries stored in a warehouse. Based on simulation results, measures to prevent lithium fire accidents were proposed, including an optimal battery state of charge, spacing, and arrangement of fire extinguishing equipment [8]. The thermal runaway risk of lithium-ion batteries was evaluated systematically and quantitatively using a fuzzy analytic hierarchy process. Multi factors were evaluated and ranked using this method [9].

The Bayesian network was employed to estimate the system risk of a smart ship; based on risk assessment, the system theoretic process analysis was used to analyze hazards and identify risk control options. The results indicated that the risk control options, including sensor heat monitoring and software testing, should be prioritized to reduce the risk [10]. M. Kaptan used the fuzzy bow-tie method to analyze risk in anchor handling operations. Measures to prevent potential accidents during anchor handling were proposed based on the findings of the study [11]. The analytic hierarchy process and expert evaluation table were used to evaluate the navigational risk in the waters of offshore wind farms. The weights of influence factors were determined using this method [12]. A fuzzy logic-based modeling method was proposed for regional multi-ship collision risk assessment. The ship crossing angle and navigational environment were considered in the constructed model. The findings of this study provided an important basis for maritime collision risk monitoring [13]. An evidence-based fuzzy Bayesian network approach was used to evaluate the occurrence probabilities of marine accidents. The results showed that maintenance failure was the main influence factor for high-consequence marine accidents [14]. The Bayesian network was used to evaluate human factors causing maritime accidents. The results showed that the most influential human factors were information communication, clear order, and safety culture [15]. The Bayesian network method was used to assess risks during the stowage of vehicles in roll-on/roll-off vessels. The probabilities of contributing causes were identified via the Bayesian network, and uncertainties in risk assessment were evaluated via a fuzzy logic method. [16] The fault tree and Bayesian network analysis were combined to conduct a probabilistic risk analysis of collision incidents in ship-to-ship tanker maneuvering operations. The results showed that the most contributing factors to the ship-to-ship collision accidents were "mooring line breakdown", "main engine failure", and "steering system failure" [17].

The fire accident risk of LBESS is affected by the meteorological environment, human factors, ship factors, cargo factors, and management factors in the process of maritime transportation. Each risk factor is dynamic and changing, which makes the traditional ship accident risk assessment model difficult to apply in the complex and changeable navigational environment. With the extensive application of Bayesian networks in maritime traffic accident risk assessment, this paper developed a pioneering study on the application of Bayesian networks in fire accident risk assessment of LBESS in the process of maritime transportation. The research of this paper will provide a theoretical basis for safe maritime transportation of LBESS.

# 2. Materials and Methods 

### 2.1. Fault Tree Analysis

Fault tree analysis (FTA) is an important method to analyze system reliability and security [18]. It is recognized as a simple and effective reliability analysis and fault diagnosis method and a powerful tool to guide system optimization design, weak link analysis, and

operation and maintenance [19]. FTA is a graphic technique that uses mathematical logic symbols to organically link various causes of failure according to their internal laws. Various possible combinations and probabilities of system failure causes can be determined according to the logic diagram. Failure probability prediction and failure diagnosis can be made via FTA [20].

# 2.2. The Bayesian Network 

The Bayesian network (Bayesian network), also known as the reliability network, derives its theoretical basis from probability theory. For the problem of expression and inference analysis of uncertain knowledge, the Bayesian network has innate advantages and is also one of the most effective theoretical models to deal with such problems [21,22].

The Bayesian network mainly consists of Bayesian network topology (directed acyclic graph) and Bayesian network parameters (conditional probability table) [23]. In the topology of the Bayesian network structure, the relationship between each factor and the degree of mutual influence is illustrated via a directed acyclic graph. The typical Bayesian network structure is shown in Figure 1, where A means root node, B means intermediate node, and C means leaf node [24]. In the network structure, each node represents different variables, and each node's state also corresponds to each node's probability change. Arrow arcs are used to illustrate the relationship between variables. The conditional probability table (CPT) of the Bayesian network is used to describe the relationship between the root node (arc front) and its leaf node (arc tail) [25,26].
![img-0.jpeg](img-0.jpeg)

Figure 1. Typical Bayesian network structure.

### 2.3. Integration of FT into BN

The topology of fault tree analysis is consistent with that of the Bayesian network. Therefore, fault trees can be transformed into Bayesian networks [27]. The Bayesian network analysis method can improve reliability analysis compared with the fault tree analysis method [28]. The transformation rule from the fault tree into Bayesian networks is as follows [21,28,29].
$>$ The nodes in the Bayesian network correspond to the events in the accident tree;
$>$ The relationship between nodes in the Bayesian network topology is also derived from the fault tree structure;
$>$ The prior probability of the node in the Bayesian network corresponds to the basic event probability in the accident tree analysis;
$>$ The conditional probability table of Bayesian networks is derived from the logic gates of the fault tree. The " 1 " or " 0 " of the conditional probability table in the BN correspond to the "and" and "or" logic gates in the FT [28].
The process of converting the fault tree analysis graph into a Bayesian network is shown in Figure 2.

![img-1.jpeg](img-1.jpeg)

Figure 2. Transformation of a fault tree into a Bayesian network.

# 2.4. Failure Probability (FP) of a Basic Event (BE) 

The fuzzy set theory was created by L.A. Zadeh in 1965 to resolve uncertainties that could not be adequately expressed in probability theory [30]. The linguistic judgments of experts can be converted into fuzzy numbers using the fuzzy set theory [31]. The most commonly used fuzzy numbers are triangular and trapezoidal fuzzy numbers. Three and four real numbers are used to represent triangular and trapezoidal fuzzy numbers [32]. Trapezoidal membership functions are easier conceptually and practically and are widely used [33]. Therefore, the membership function shown in Equation (1) was used in this study.

$$
\mu_{A^{\prime}}(x)=\left\{\begin{array}{l}
0, x<a_{1} \\
\frac{x-a_{1}}{a_{2}-a_{1}}, a_{1} \leq x \leq a_{2} \\
1, a_{2} \leq x \leq a_{3} \\
\frac{x-a_{4}}{a_{3}-a_{4}}, a_{3} \leq x \leq a_{4} \\
0, x<a_{4}
\end{array}\right.
$$

In order to evaluate the failure probability of root events in a Bayesian network, it is usually necessary to convert the linguistic judgement of experts into fuzzy numbers and aggregate the converted fuzzy numbers into one using aggregation methods [34,35,36]. Hsu and Chen proposed SAM (similarity agreement method) formulas in 1996 [37]. It is one of the most widely used expert judgment aggregation methods. The steps for SAM are described as follows [17].

Calculation of degree of similarity: The degree of similarity can be calculated via Equation (2):

$$
S(\bar{A}, \bar{B})=1-\frac{1}{4} \sum_{i=1}^{4}\left|a_{i}-b_{i}\right|
$$

Calculation of average agreement $(A A)$ degree $A A\left(E_{u}\right)$ of experts: Equation (3) was used to calculate the average agreement between each expert's opinion. " $M$ " means the number of experts.

$$
\begin{gathered}
A A\left(E_{u}\right)=\frac{1}{M-1} \sum_{v=1}^{M} S\left(\bar{R}_{u}, \bar{R}_{v}\right) \\
u \neq v
\end{gathered}
$$

Calculation of experts' relative agreement $(R A)$ degree, $R A\left(E_{u}\right)$ of the experts. Equation (4) was used to calculate the degree of conformity between different experts' judgments.

$$
E_{u}(u=1,2, \cdots, M) \text { as } R A\left(E_{u}\right)=\frac{A A\left(E_{u}\right)}{\sum_{u=1}^{M} A A\left(E_{u}\right)}
$$

Equation (5) was used to calculate the consensus coefficient of an expert.

$$
C C\left(E_{u}\right)=\beta w\left(E_{u}\right)+(1-\beta) R A\left(E_{u}\right)
$$

The consensus coefficient measures the agreement degree of expert opinions. $\beta$ is the optimism coefficient and indicates the importance of $w\left(E_{u}\right)$ over $R A\left(E_{u}\right)$. Its value varies between 0 and 1 . The " 0 " means a homogeneous expert group is selected. The " 1 " means an expert opinion's degree of consensus is the same as its weight.

Expert judgment assembly $\widetilde{R}_{A G}$ was calculated via Equation (6).

$$
\widetilde{R}_{A G}=C C\left(E_{1}\right) \times \widetilde{R}_{1}+C C\left(E_{2}\right) \times \widetilde{R}_{2}+\cdots+C C\left(E_{M}\right) \times \widetilde{R}_{M}
$$

The center of area (COA) method is used to transform the trapezoidal fuzzy number into a crisp number. It is formulated by Equation (7).

$$
\begin{aligned}
\operatorname{defuzz}\left({ }^{\prime} A\right) & : \frac{\int x \cdot u(x) d x}{\int u(x) d x}=\frac{\int_{a_{1}}^{a_{2}}\left(\frac{x-a_{1}}{a_{2}-a_{1}}\right) x d x+\int_{a_{2}}^{a_{3}} x d x+\int_{a_{3}}^{a_{4}}\left(\frac{a_{4}-x}{a_{4}-a_{3}}\right) x d x}{\int_{a_{1}}^{a_{2}}\left(\frac{x-a_{1}}{a_{2}-a_{1}}\right) d x+\int_{a_{3}}^{a_{4}} d x+\int_{a_{4}}^{a_{4}}\left(\frac{x a_{1}-x}{a_{4}-a_{3}}\right) d x} \\
& =\frac{-a_{1} a_{2}-a_{3} a_{4}+\frac{1}{3}\left(a_{4}-a_{3}\right)^{2}-\frac{1}{3}\left(a_{2}-a_{1}\right)^{2}}{-a_{1}-a_{2}+a_{3}+a_{4}}
\end{aligned}
$$

In the final step, Equation (8), proposed by Onisawa, was used to calculate the fuzzy failure probabilities of root events in the Bayesian network. "FP," means fuzzy failure probabilities, " $F P_{s}$ " means fuzzy failure possibilities, and " $K$ " is a constant coefficient [38].

$$
F P_{r}=\left\{\begin{array}{l}
1 / 10^{K}, F P_{s} \neq 0 \\
0, \quad F P_{s}=0
\end{array}, \quad K=\left(\frac{1-F P_{s}}{F P_{s}}\right)^{\frac{1}{3}} \times 2.301\right.
$$

# 3. Fire Accident Modeling of LBESS Maritime Transportation 

### 3.1. Fault Tree Modelling

Due to the short history of LBESS maritime transportation, the research literature on the causes of LBESS maritime transportation fire accidents is limited and insufficient. Therefore, the cause of the accident is determined by referring to expert opinion, accident reports, and trade publications.

When creating the fire fault tree model of the lithium battery energy storage system, the fire mechanism of the lithium battery was first analyzed. Then, combined with the special external conditions in the process of marine transportation, the basic events and intermediate events that led to the fire accident of the lithium battery energy storage system in the process of marine transportation were formed.

The lithium battery fire accident was caused by the thermal runaway of a battery cell. Some key factors leading to the fire or explosion risk are impact, internal and external short circuits, and high ambient temperature. Impact damage may result in battery damage and the thermal runaway of the cells. During maritime transportation, bad weather conditions, improper storage, improper ballast, high ship speed, defect of binding equipment, a contact accident of the ship, and a collision accident of the ship may lead to the impact damage of a LBESS. Direct sunlight, stowage adjacent to the engine and oil tank, and high ambient temperature may lead to the high temperature of LBESS. Cargo hold flooding, lack of a short-circuit-prevention device, overcharge, over-discharge, and a battery cell defect may lead to the short circuit of a LBESS. These basic events may result in a fire accident of the LBESS. Meanwhile, insufficient fire monitoring devices and firefighting capacity can also lead to fire accidents of the LBESS. There were 31 basic events and 16 intermediate events. The fault tree model of the LBESS fire is shown in Figure 3.
x1: bad weather condition; x2: improper storage; x3: improper ballast; x4: high ship speed; x5: defect of binding equipment; x6: improper maintenance of binding equipment; x7: improper binding; x8: contact accident; x9: collision accident; x10: direct sunlight; x11: stowage adjacent to engine room; x12: stowage adjacent to oil tank; x13: high ambient

temperature; x14: cargo hold flooding; x15: no installation of short-circuit-prevention device; x16: high humidity; x17: lack of insulation; x18: overcharge; x19: over discharge; x20: defect of separate; x21: burrs on the electrode surface; x22: no installation of monitoring devices; x23: monitoring equipment cannot cover all goods; x24: damage of monitoring equipment; x25: the monitoring equipment does not have a real-time alarm function; x26: the crew does not patrol according to regulations; x27: insufficient firefighting equipment; x28: failure of firefighting equipment; x29: firefighting equipment is not suitable for putting out lithium battery fires; x30: crew members are not trained in lithium battery firefighting; x31: the crew did not know the correct way to put out the lithium battery fire.
![img-2.jpeg](img-2.jpeg)

Figure 3. FT diagram.

# 3.2. Basic Event Probabilities Calculation 

In a LBESS fire accident risk assessment, due to insufficient information, the calculation of node failure is probably based on the opinion of experts who use linguistic variables to assess the probability of failure of the basic event [36]. Different numbers of language variables can be used when determining language variables. In this study, seven linguistic variables were used to estimate the probability of root cause [39]. The numerical approximation method proposed by Chen and Hwang was used to convert language variables into their corresponding fuzzy numbers [40]. The corresponding relationship between language variables and fuzzy sets is shown in Table 1.

Table 1. Relationship between linguistic variables and fuzzy sets.


Based on the consideration of all the experts involved in LBESS maritime transport, three experts were selected to judge the basic events. The marine experts' judgments were

aggregated via the SAM method, as shown in Equations (2)-(8). The outcomes of all basic events after aggregation calculation are shown in Table 2.

Table 2. Basic events probabilities calculation based on experts' judgment.


# 4. Quantitative Assessment of a LBESS Fire Accident via Bayesian Network 

The Bayesian network was used to analyze the probability relation of nodes that cause LBESS fire accidents in the process of maritime transportation.

### 4.1. The Bayesian Network Structure Transformed from a Fault Tree Model

The Bayesian network structure can be constructed from the fault tree topology as described in Section 2.3. Nodes in the Bayesian network structure correspond to the events in the fault tree model. The conditional probabilities in the Bayesian network were based on the logical gates of the fault tree model.

The GeNIe program was used to generate the Bayesian network structure, as shown in Figure 4. The prior probability of the nodes in Table 2 and the corresponding conditional probabilities were introduced into the Bayesian network model to calculate the occurrence probability of a LBESS fire accident. The LBESS fire accident probability calculated in this model is $2 \%$.
![img-3.jpeg](img-3.jpeg)

Figure 4. Bayesian network structure constructed via GeNIe program.

### 4.2. Probability Updating

Compared with the fault tree analysis method, the main advantage of the Bayesian network is to modify prior probabilities based on newly acquired information. The revised probability is called posterior probability [41]. The probabilistic update of the Bayesian network structure is completed via backward analysis. The most influential factors of the accident can be obtained via this method. The posterior probabilities of the Bayesian network nodes can then be obtained by setting the occurrence probability of the target node as $100 \%$. The most influential factors leading to the LBESS fire accident can be found by analyzing the difference between the prior probability and posterior probability. This paper takes the top event (fire accident) as evidence to determine the posterior probability of the basic event. Table 3 shows the posterior probability modified using backward analysis,

assuming that the top event occurred. A higher impact on the occurrence of top events can be suggested via the rapid growth between the prior probability and posterior probability.

Table 3. Comparison between prior and posterior probabilities of nodes in the Bayesian network.


As shown in Table 3, it can be observed that the probabilities of some nodes change more than others. This means that the model is sensitive to fire accidents and plays an important role in the occurrence of fire accidents. According to Table 3, the most influential nodes leading to a fire accident were firefighting equipment not suitable for putting out lithium battery fires (x29), high humidity (x16), the monitoring equipment that does not have a real-time alarm function (x25), high ambient temperature (x13), and crew members that are not trained in lithium battery firefighting (x30). Ship monitoring equipment can be modified according to the monitoring equipment operation and management mode of automated container terminals [42], and the sensing data can be properly used via the method mentioned in [43].

# 5. Conclusions 

This paper proposes a risk assessment technique based on the Bayesian network, which combines fault tree analysis with the fuzzy method. Firstly, the fault tree analysis method was used to analyze the events leading to LBESS fire accidents during maritime transportation. Then, expert opinion was used to assess the occurrence probability of basic

events. Finally, the Bayesian network was used to assess the LBESS fire accident risks within the entire maritime transportation process. The findings indicated that firefighting equipment not suitable for putting out lithium battery fires (x29), high humidity (x16), monitoring equipment without a real-time alarm function (x25), high ambient temperature (x13), and crew members not trained in lithium battery firefighting (x30) are the most influential factors leading to a LBESS fire accident. Therefore, the above-mentioned nodes should be verified before the launch of LBESS maritime transportation. According to the characteristics of lithium battery fires, $\mathrm{CO}_{2}$ firefighting systems cannot effectively extinguish lithium battery fires. It is recommended that ships be equipped with waterbased firefighting systems, which should be able to fully cover lithium battery cargo. It is recommended that ships be equipped with temperature monitoring and an alarm device with a real-time transmission function. When the temperature of the lithium battery cargo exceeds the set temperature, the device will automatically start an alarm and alert ship personnel to promptly identify the cause and eliminate the fault.

Author Contributions: Conceptualization, C.Z. and G.L.; methodology, H.S.; software, Y.Z.; validation, S.L. and G.L.; formal analysis, J.C.; investigation, J.C.; data curation, H.S.; writing—original draft preparation, C.Z.; writing-review and editing, G.L.; visualization, H.S.; supervision, C.Z.; project administration, C.Z.; funding acquisition, C.Z. and G.S. All authors have read and agreed to the published version of the manuscript.
Funding: This research was funded by the Ministry of Industry and Information Technology of the People's Republic of China, grant number CBZ2N21-2.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: The data presented in this study are available upon request from the corresponding authors.
Conflicts of Interest: The authors declare no conflict of interest.
