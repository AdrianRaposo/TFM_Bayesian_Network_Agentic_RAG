# Article 

## Research on Collapse Risk Assessment of Karst Tunnels Based on BN Self-Learning

Jinglai Sun ${ }^{1}$ (D) Yan Wang ${ }^{2,3, *}$ (D), Xu Wu ${ }^{1}$, Xinling Wang ${ }^{1}$, Hui Fang ${ }^{1}$ and Yue Su ${ }^{1}$<br>check for updates

Citation: Sun, J.; Wang, Y.; Wu, X.; Wang, X.; Fang, H.; Su, Y. Research on Collapse Risk Assessment of Karst Tunnels Based on BN Self-Learning. Buildings 2024, 14, 685. https:// doi.org/10.3390/buildings14030685

Academic Editor: Honggui Di
Received: 31 January 2024
Revised: 24 February 2024
Accepted: 1 March 2024
Published: 5 March 2024

## (0)

Copyright: (c) 2024 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Beijing Municipal Engineering Research Institute, Beijing 100037, China; sunjinglai83@163.com (J.S.); 13051510807@163.com (X.W.); 18253162834@163.com (X.W.); 15026661985@163.com (H.F.); suyue110227@163.com (Y.S.)
2 School of Civil Engineering, Qingdao University of Technology, Qingdao 266520, China
3 Engineering Research Center of Concrete Technology under Marine Environment, Ministry of Education, Qingdao 266520, China

* Correspondence: wangyantumu@qut.edu.cn

Abstract: The high risk of collapse is a key issue affecting the construction safety of karst tunnels. A risk assessment method for karst tunnel collapse based on data-driven Bayesian Network (BN) selflearning is proposed in this study. The finite element calculation is used to analyze the distribution law of the plastic zone of the tunnel and the karst cave surrounding rock under different combinations of parameters, and a four-factor three-level data case database is established. Through the self-learning of the BN database, a Bayesian Network model of karst tunnel collapse risk assessment with nodes of four types of karst cave parameters is established. The specific probability distribution state and sensitivity of the parameters of different types of karst caves under the condition of whether the tunnel and the karst cave plastic zone are connected or not are studied. The research results show that the distance and angle of the karst cave are the main influencing parameters of the tunnel collapse probability, and the diameter and number of the karst cave are the secondary influencing parameters. Among them, the distance, diameter, and number of karst caves are proportional to the probability of tunnel collapse, and the most unfavorable orientation of karst caves is $45^{\circ}$ above the tunnel. When the tunnel passes through the karst area, it should avoid the radial intersection with the karst cave at the arch waist while staying away from the karst cave. The results of this work can provide a reference for the construction safety of karst tunnels under similar conditions.

Keywords: karst tunnel; BN self-learning; finite element analysis; Bayesian Network; risk assessment

## 1. Introduction

With the large-scale construction of tunnel projects in China, the focus of Chinese tunnel engineering has gradually shifted from the characteristics of large cross-sections and long distances to overcoming complex geological conditions and harsh climatic environments. A large number of tunnel projects have been constructed in areas with rich karst formations, high altitudes, high ground stress, strong rock bursts, and high gas content [1].

The karst topography is widely distributed in the central and western regions of China [2]. Therefore, constructing tunnels in karst areas has become an inevitable reality. The challenges in tunneling through karst formations primarily arise from the randomness in the locations of caves, the uncertainty in the size of these caves, and the diversity of karst's hydrogeological structures and water bodies. These factors mainly bring risks of collapse, water inrush, and mud outburst during tunnel excavation, threatening construction safety. Currently, in China's karst topography areas, there are already many successful cases of tunnel construction [3,4], which have provided important information clarifying the safety control mechanisms, construction experience, and management strategies in tunnel construction in karst regions. Fan et al. [5] addressed the challenges associated with karst geology in the construction of the YW railway tunnel in China. Risks such as water

inrushes and mud bursts, prevalent in karst regions, were evaluated, and strategies for their management were outlined, drawing upon experiences from the YW project. The significance of advanced prediction and monitoring technologies in enhancing the safety of tunneling projects situated in karst areas was underscored, providing valuable insights for future construction. Hence, researching the mechanisms of collapse accidents during tunnel construction in karst formations and accurately assessing the risk of collapse in karst tunnels are key to ensuring the safety of tunnel construction in these areas.

Currently, research on the safety of karst tunnel construction primarily focuses on the mechanisms and the prevention and prediction methods of water inrush and mud outburst accidents, the parameters of karst caves, and the safety of the tunnel lining and surrounding rock structures, with numerous research achievements being made in these areas. In the context of the mechanism and prediction of water inrush and mud outburst in karst tunnels, Li et al. [6-11] conducted studies on high-pressure, high-flow karst fracture water in water-conducting tunnels, proposing a comprehensive advanced geological prediction method and an early warning mechanism suitable for high-risk karst tunnels. Based on the attribute mathematical model, they developed a theory and method for attribute interval evaluation that allows quantitative evaluation, established the principles for the application of the attribute recognition analysis method, and achieved the quantitative identification of the disaster risk levels. Li et al. [12] put forward the influence factors of water inrush from the perspective of karst hydrogeological factors, engineering disturbances caused by human factors, and the relationship between water inrush and geological conditions. From the perspective of the damage mode of water inrush channels, water inrush can be divided into three types. These three types are geological-defect-type water inrush, non-geological-defect-type water inrush, and a combination of the above two forms.

In terms of the influence of the karst cave parameters on the stability of the tunnel lining and surrounding rock structures, Wu et al. [13] used the limit analysis upper limit method combined with reliability theory to explore the stability and reliability of the rock and soil mass around the karst tunnel face and the karst cave. The research indicated that the self-supporting capability of the rock and soil mass at the tunnel face was substantially improved when the ratio of the tunnel's buried depth to its diameter exceeded 2, especially as the tunnel passed through layers of moderately or slightly weathered dolomite. Additionally, the stability of the rock and soil mass adjacent to the left side of the karst cave was significantly increased when the ratio of the clear distance between the cave's bottom and the tunnel to the cave's diameter was more than 2. Due to the presence of karst caves and water fillings within them, the effect of stress redistribution after tunnel excavation has a significant impact on the tunnel structure [14-16]. Ma et al. [17] examined the impact of karst caves on tunnel stability through the Distinct Lattice Spring Model (DLSM), identifying key factors such as the cave size, position, and proximity to the tunnel. It was found that the stability of tunnels decreases as the distance between the tunnel and a cave diminishes, with the effects becoming negligible when the distance exceeds twice the tunnel's arc radius. Xu et al. [18] analyzed the hydro-mechanical coupling response behaviors of tunnels influenced by water-filled karst caves. The impact of cave characteristics on tunnel stability, specifically through the principal stress and displacement of the surrounding rock, was examined using a numerical model. The research provides essential insights for the prediction of karst caves' effects on tunnel engineering, emphasizing the importance of considering the cave dimensions, locations, and proximity in design and construction within karst regions.

Fan et al. [19] conducted research on the mechanical response characteristics of the lining structure of pipeline-type karst tunnels using a combination of model experiments and numerical simulation methods. The effects of the positions of pipeline-type cavities, the diameters of these cavities, and the height of the water head inside the cavities on the internal forces in tunnel lining structures were explored. Wang et al. [20] analyzed the impact of semi-exposed karst caves of different sizes and at different positions on the stability of tunnel surrounding rock and the stress on the initial support structure through

experimental methods. In the context of shield tunneling construction, scholars have used the FEM, field test, and model test to study the impact of karst caves of various sizes, spacings, and orientations on the stability of the surrounding rock during the excavation of shield tunnels [21,22,23]. Li et al. [24] conducted a comprehensive geomechanical model test to examine the stability of the surrounding rock during the excavation of a shield tunnel and to uncover the causes of delayed water inrush in tunnels excavated near caves containing confined water. This study successfully determined the developmental patterns of early warning indicators such as soil moisture, ground subsidence, internal displacement, stress, and the seepage pressure associated with water inrush throughout the tunnel excavation process. Cui et al. [25] explored the complexities faced during shield tunneling within karst terrains, specifically highlighting buried karst caves in Guangdong Province, China. Identified risks, including sinkholes and the ingress of water or stone, which pose threats to tunnel stability and safety, were discussed. The application of a grouting treatment to fill karst caves was examined through a Guangdong case study, showcasing its efficacy in meeting engineering standards and ensuring tunnel integrity in karst landscapes. Kang et al. [26] conducted a detailed analysis of the impact of distribution characteristics such as joints, the karst distribution, and surrounding rock fractures on the prevention of water inrush during the construction of earth pressure balance shield tunnels in karst regions. Lyu et al. [27] established the collapse failure mechanism for circular tunnels under karst caves. By employing variational methods and limit analysis, an expression for tunnel collapse that accounted for seismic forces and seepage forces was derived. Furthermore, the impact of the vertical seismic coefficient on the collapsed mass was analyzed.

In terms of the intelligent risk assessment of karst tunnels, many mathematical theoretical methods for decision support have also been used in the risk assessment of karst tunnels [28,29,30,31,32]. Bai [33] established three types of intelligent prediction models for water and mud inrush disasters in karst tunnels based on a case database with risk grading labels for such disasters. These models included a decision tree model, a support vector machine model, and a random forest model. Additionally, an intelligent prediction system for water and mud inrush disaster risks in karst tunnels was developed. Wang et al. [34], addressing the uncertainty characteristics of water inrush in karst tunnels, employed the Set Pair Analysis (SPA) method for risk assessment. The assessment comprehensively considered the karst hydrology and engineering geological conditions, selecting several key influencing factors as evaluation indicators, including the stratum lithology, adverse geological conditions, groundwater level, and solubility contact zone. The assessment results not only aligned with those derived from the attribute mathematical theory but also corresponded well with the actual conditions. Li et al. [35] proposed an attribute synthetic evaluation system based on the mathematical theory of attributes to systematically assess the risk of water inrush in karst tunnels. This method comprises two types of attribute recognition models: one named the attribute recognition model in the design stage (ARM-D) and another named the attribute recognition model in the construction stage (ARM-C).

Furthermore, commonly used numerical simulation methods, including the finite difference method (FDM) [36], finite element method (FEM) [37], particle flow code (PFC) [38], peridynamics (PD) [39], etc., have often been utilized to study the deformation mechanisms of the surrounding rock and support structures in karst tunnels, the protective layer thickness, the karst water seepage patterns, and risk assessment. Due to the simplification of tunnels, surrounding rocks, and karst caves as homogeneous, isotropic, and continuous media in modeling, the FEM method is able to better demonstrate its advantages [30].

The majority of the studies mentioned above focus on the analysis of accident mechanisms under specific karst conditions and the prediction of accident risks. However, in terms of risk assessment, they often emphasize the qualitative or quantitative evaluation of the overall risk of karst tunnel construction using one or several evaluation methods. Such approaches are not only highly subjective but also lack in-depth research on the intrinsic relationships between different karst cave parameters. A data-driven Bayesian Network approach, conducting numerical calculations of the distribution of the plastic

zone in drill-and-blast tunnel construction under different karst cave parameters with four factors at three levels, was adopted in this work. Through the self-learning of the Bayesian Network, a method for the evaluation of the risk of collapse in karst tunnels was established. Posterior probability analysis was used to explore the impact mechanisms of four types of parameters, the number of karst caves, the distance of karst caves, the size of karst caves, and the angle of karst caves, on the risk of tunnel collapse. The results of this study can provide a reference for the construction safety of similar karst tunnels. Through the quantitative analysis of the probability changes of various factors, an inference is made regarding the potential disaster-causing factors and mechanisms of karst tunnel collapse accidents under the conditions of the study, providing theoretical reference significance for the effective prevention and control of the occurrence of accidents.

# 2. Bayesian Network Self-Learning Probability Prediction Method 

The Bayesian Network (BN) model is a graphical model based on probability theory, representing a credibility network with self-learning and reasoning capabilities [40-42]. The primary structure of the model consists of root nodes, intermediate nodes, and target nodes, along with the logical relationships between these nodes, their value ranges, and prior probability values [43]. A karst tunnel collapse risk assessment model through Bayesian Network self-learning is established and a data-driven risk evaluation method for tunnel collapse under various karst conditions is proposed in this paper.

The establishment of a Bayesian Network requires the consideration of two key issues: determining the logical relationships of each node and the value ranges and prior probabilities of each node. Traditional methods primarily rely on referencing expert experience, using artificially designated approaches to determine nodes' logical relationships and value ranges. The size of each node's prior probabilities is subjectively determined through certain mathematical processing methods, resulting in a significant influence of human subjectivity. To overcome the excessive subjectivity in establishing Bayesian Network models, a self-learning method for Bayesian Networks is adopted in this paper. Through learning from a certain number of cases, the method autonomously determines the size of prior probabilities. Drawing comprehensively from previous research achievements and considering the characteristics and universality of the karst distribution, four types of factors as the main karst condition parameters are selected in this study: the number of karst caves, the distance to the karst caves, the diameter of the karst caves, and the angle of the karst caves. Each type of parameter is considered at three levels, as shown in Table 1. The four types of factors, A, B, C, and D, serve as the root nodes of the Bayesian Network. The specific values of these parameters at the three levels constitute the value ranges of each node. The target node E represents the likelihood of tunnel collapse. A schematic diagram of the Bayesian Network model constructed is shown in Figure 1.

Table 1. Dataset summary.


In Bayesian inference theory, the prior probability and posterior probability are relative concepts for a given set of evidence. Suppose that $S$ and $W$ are two random variables, where $S=s$ represents a certain hypothesis and $W=w$ represents a set of evidence. The relationship between the prior probability and posterior probability is as follows [44]:

$$
P(S=s \mid W=w)=\frac{P(S=s) P(W=w \mid S=s)}{P(W=w)}
$$

where $P=(S=s \mid W=w)$ is the posterior probability, $P(S=s)$ is the prior probability, and $P(W=w \mid S=s)$ is the likelihood of $S=s$. In relation to the evidence $W=w$, suppose that $T$ is a certain research variable, and it follows that [44]

$$
P(X \mid W=w)=\frac{P(X) P(W=w \mid X)}{P(W=w)}
$$

where $P(X)$ is the prior probability distribution of $X, P(X \mid W=w)$ is the posterior probability distribution of $X$, and $P(W=w \mid X)$ is referred to as the likelihood function of $X$.
![img-0.jpeg](img-0.jpeg)

Figure 1. Bayesian Network model.
Equation (2) represents the variable form of Bayes' theorem. $P(W=w)$ is a normalizing constant, functioning as a probability distribution, which is defined by Equation (3) [44]:

$$
P(W=w)=\sum P(X) P(W=w \mid X)
$$

When $P(W=w)$ is independent of $X$, Equation (2) can be rewritten as $P(X \mid W=w) \propto$ $P(X) L(X \mid W=w)$, which means that the posterior probability distribution is proportional to the product of the prior distribution and the likelihood function.

Therefore, by constructing a certain number of factual-based parameter variable and result combinations and utilizing Bayesian Network self-learning, the likelihood of research variable outcomes under specific parameter conditions is continuously improved, producing inference results that are as close to reality as possible. The basic concept of this method is illustrated in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2. BN self-learning probability prediction method.

# 3. Deformation Laws of Surrounding Rock during Tunnel Excavation under Different Karst Cave Parameters 

To study the risk level of tunnel collapse during karst tunnel excavation under different combinations of karst cave parameters, a numerical model based on a four-factor, threelevel parameter combination was established using FEM simulation. The distribution of plastic zones in the tunnel body, surrounding rock, and karst caves after the excavation of the tunnel was obtained through numerical calculations. The plastic zone refers to the area where the material undergoes permanent deformation upon exceeding its elastic limit when subjected to external forces. In tunnel engineering, following the excavation of a tunnel, the redistribution of stress results in the formation of plastic zones in the surrounding rock, within which the surrounding rock loses its load-bearing capacity. Therefore, the presence or absence of connectivity in the plastic zones was used as the basis for the determination of tunnel collapse, providing data for the self-learning of the Bayesian Network.

### 3.1. Construction of the Numerical Model

The Yanglin tunnel, as an integral part of the Kunming Ring Expressway, is predominantly situated in geological strata characterized by karst and weak, fractured surrounding rock, extending over a length of 9.4 km . The segment from $\mathrm{K} 19+30$ to $\mathrm{K} 19+130$ (mileage marker K stands for kilometers, indicating a segment spanning from 19 km plus 30 m to 19 km plus 130 m from the starting point, totaling 100 m ) in the Yanglin tunnel, representative of karst conditions, was selected for study. This segment predominantly consists of limestone and is classified as Grade V surrounding rock, accompanied by karst development. The average burial depth is approximately 390 m , as depicted in Figure 3. The mechanical parameters of the surrounding rock are listed in Table 2. A three-centered horseshoe-shaped cross-section is adopted for the tunnel in this section, with a span of 17.24 m and a height of 11.73 m , as shown in Figure 4. It should be pointed out that the numerical model established is a simplified two-dimensional model, and the size effect is not considered.
![img-2.jpeg](img-2.jpeg)

Figure 3. Cross-section of $\mathrm{K} 19+30-\mathrm{K} 19+130$ in Yanglin tunnel.

Table 2. Strata parameters.


![img-3.jpeg](img-3.jpeg)

Figure 4. Tunnel section.
Due to the Yanglin tunnel's burial depth nearing 400 m , classifying it as a typical deep-buried tunnel, the equivalent load height needed to be calculated when establishing the numerical model. According to the Specifications for Design of Highway Tunnels [45], the equivalent load height for a deep-buried tunnel is determined as $h=0.45 \times 2^{5-1} \omega$, where $\omega=1+i(B-5)$ is the width influence coefficient, $B$ is the tunnel width, and $i$ is the rate of increase or decrease in the surrounding rock pressure. When the cross-sectional parameters of the Yanglin tunnel are inserted into the formula, the equivalent load height $h$ is calculated to be 17.78 m . To mitigate edge effects, the model dimensions $x \times y$ are set at $160 \times 100 \mathrm{~m}$, with fixed constraints on the boundaries and the converted load applied to the strata. Based on the combinations of karst cave parameters, 81 distinct numerical models were established.

# 3.2. Deformation Laws of Surrounding Rock 

Based on the numerical models established with different karst cave parameter combinations, the distribution of the plastic zones of tunnels and karst caves under each combination was determined through finite element calculations. Due to space limitations, only the cases of single karst caves with diameters of $2 \mathrm{~m}, 3 \mathrm{~m}$, and 4 m and angles of $0^{\circ}, 45^{\circ}$, and $90^{\circ}$ at a distance of 1 m , namely combination scenarios $1-9$, are presented as examples. The resulting distributions of the plastic zones in tunnels and surrounding karst caves are shown in Figure 5. The connectivity of plastic zones for all 81 scenarios with four factors at three levels is indicated in Table 3. The calculations reveal that with a single karst cave present, the interval between the plastic zones increases with distance under the same cave radius, thereby reducing the likelihood of connectivity. With the same angle and distance, the plastic zone is more likely to connect as the karst cave radius increases. When two karst caves are present, the plastic zones gradually move away from each other as the distance increases when the caves are located at $0^{\circ}$ and $90^{\circ}$ to the tunnel, with the highest likelihood of connectivity at a $45^{\circ}$ angle. With three karst caves, under the selected distance parameters, the likelihood of plastic zone connectivity increases with the karst cave radius and also grows with the number of karst caves.

![img-4.jpeg](img-4.jpeg)

**Figure 5.** Distribution of plastic zones for combinations 1 to 9.

**Table 3.** Connectivity of the plastic zone.

Karst Caves
A | Distance to
Karst Caves
B | Diameter of
Karst Caves
C | Angle of
Karst Caves
D | Plastic Zone
Connectivity
E | No. | Number of
Karst Caves
A | Distance to
Karst Caves
B | Diameter of
Karst Caves
C | Angle of
Karst Caves
D | Plastic Zone
Connectivity
E  |

• indicates connectivity of the plastic zone; ○ represents non-connectivity of the plastic zone.

# 4. Construction of Bayesian Network Model 

### 4.1. Bayesian Network Model

The establishment of a Bayesian Network initially requires the determination of the network structure's constituent nodes and their logical relationships. Following the basic principles of the Bayesian Network self-learning probability prediction method, the number of karst caves, the distance to the karst caves, the diameter of the karst caves, and the angle of the karst caves were selected as the root nodes of the Bayesian Network, with the probability of tunnel collapse as the target node. The value range of each root node was determined in reference to the respective karst cave parameters, corresponding to the four-factor, three-level values, as shown in Table 4.

Table 4. Node ranges.


As illustrated in Figure 1, the root nodes are assumed to have a parallel relationship and do not include intermediate nodes. Under this structure, a learning case library was generated using the results of surrounding rock deformation for the four-factor, threelevel random combinations of karst cave parameters obtained from numerical calculations. Through the self-learning characteristics of the Bayesian Network, the maximum likelihood function for updating prior probabilities was continually refined. Consequently, the prior probability values of each node in the Bayesian Network were determined, resulting in the Bayesian Network model for karst tunnel collapse risk assessment, as shown in Figure 6. The calculations mentioned above were quickly completed using the Netica software (v5.18). As can be seen from the figure, under the current conditions of the karst cave parameter learning case library, each combination appears randomly and uniformly, meaning that the occurrence probability of each parameter is equal. Therefore, in the Bayesian Network, the probability of each node's value range is $33.3 \%$. At the initial state, the distribution probabilities of the target node are $84 \%$ and $16 \%$, representing the probabilities of plastic zone connectivity and non-connectivity in the initial state, respectively.
![img-5.jpeg](img-5.jpeg)

Figure 6. The Bayesian Network model for risk assessment.

### 4.2. Network Validation and Robustness Test

The robustness of the Bayesian Network constructed was tested using a confusion matrix according to the methods described in reference [46]. When creating the confusion matrix, the columns represented the values predicted by the BN, while the rows represented the actual values of the numerical simulation results. The confusion matrix utilized crossing

table operations to tally the predicted and actual values, used to calculate the error rate. The error rate, indicating the accuracy of the results derived, served as an assessment of the predictive capability on the state of a set of nodes. To increase the number of cases in the dataset, the Case Simulate function of the Netica software (v5.18) was used to generate 1000 sets of cases under an approximately $10 \%$ missing data rate, ultimately resulting in 903 valid cases. The plastic zone connectivity was used as the output for the confusion matrix, and the confusion matrix obtained for the Bayesian network robustness test is shown in Table 5.

Table 5. Confusion matrix of robustness test.


Based on the test results, the error rate for plastic zone connectivity with an actual value of Yes was found to be $1.22 \%$, and the error rate for plastic zone connectivity with an actual value of No was found to be $19.02 \%$. With a $10 \%$ missing data rate, the total error rate of the model was $4.43 \%$, indicating good predictive accuracy.

Another indicator for the evaluation of the consistency between a model's predicted values and actual values is the scoring rules [47]. Scoring rules do not merely take the most probable state as the prediction but also consider the actual confidence levels of the states to determine their degree of consistency with the values in the cases. Scoring rules are measured by three parameters, the logarithmic loss, quadratic loss, and spherical payoff, with their formulas being [48]

$$
\begin{gathered}
\text { Logarithmic loss }=M O A C\left[-\log \left(P_{c}\right)\right] \\
\text { Quadratic loss }=M O A C\left[1-2 P_{c}+\sum_{j=1}^{n} P_{j}^{2}\right] \\
\text { Spherical payoff }=M O A C\left[\frac{P_{c}}{\sqrt{\sum_{j=1}^{n} P_{j}^{2}}}\right]
\end{gathered}
$$

where $P_{c}$ is the probability predicted for the correct state, $P_{j}$ is the probability predicted for state $j, n$ is the number of states, and $M O A C$ stands for the mean over all cases (i.e., all cases for which the case file provides a value for the node in question) [49].

The logarithmic loss ranges from 0 to infinity, where zero signifies optimal performance. The quadratic loss spans from 0 to 2 , with 0 indicating the highest achievement, and spherical payoff varies from 0 to 1 , where 1 denotes the best outcome. Based on the calculation results, the value of logarithmic loss was determined to be 0.07913 and the value of quadratic loss was 0.05523 , both approaching 0 . The value of spherical payoff was found to be 0.9681 , nearing 1 . All three parameters indicated that the model possessed good predictive performance.

# 5. Collapse Risk Assessment of Karst Tunnels 

Based on the established Bayesian Network model for karst tunnel collapse risk assessment, the posterior probability values of each root node and the target node under different parameter distributions can be analyzed through Bayesian Network inference. This allows for an examination of the impact of different karst cave parameters on the tunnel collapse risk and the composition of parameters in the event of a tunnel collapse accident.

### 5.1. Posterior Probability Analysis

By fixing the value range distribution of the target node, the probability distribution of each root node's value range can be reverse-calculated under the current target node state. This reflects the possible combinations and probabilities of different karst cave parameters under the specified state of the target node.

Firstly, the probability value of the target node for plastic zone connectivity was set to 100%. Following this, inference calculations using the Bayesian Network were conducted to ascertain the probability distribution for each parameter in this state, as depicted in Figure 7. It is illustrated in the figure that, with the target node's probability value for plastic zone connectivity established at 100%, the associated probability values for having 1, 2, and 3 karst caves are determined to be 30.9%, 33.8%, and 35.3%, respectively. Similarly, for karst cave distances of 1 m, 3 m, and 5 m, the probability values are calculated to be 39.7%, 36.8%, and 23.5%, respectively. For karst cave diameters of 2 m, 3 m, and 4 m, the probability values are found to be 29.4%, 33.8%, and 36.8%, respectively. Furthermore, for karst cave angles of 0°, 45°, and 90°, the probability values are identified as 29.4%, 39.7%, and 30.9%, respectively. The analysis indicates that the likelihood of a tunnel collapse increases with the number of karst caves, with closer proximity, and particularly when positioned at a 45° angle above the tunnel.

![img-6.jpeg](img-6.jpeg)

**Figure 7.** Bayesian Network state with connected plastic zone.

Secondly, the probability value for plastic zone connectivity of the target node was set to 0, and, under this condition, the probability distribution of each parameter within the Bayesian Network is as depicted in Figure 8. The figure demonstrates that, with the state of no plastic zone connectivity established for the target node, the resulting probability values for having 1, 2, and 3 karst caves are found to be 46.2%, 30.8%, and 23.1%, respectively. For distances of karst caves of 1 m, 3 m, and 5 m, the probability values are calculated to be 0%, 15.4%, and 84.6%, respectively. Regarding the diameters of karst caves of 2 m, 3 m, and 4 m, the probability values are determined to be 53.8%, 30.8%, and 15.4%, respectively. Additionally, for karst cave angles of 0°, 45°, and 90°, the probability values are identified as 53.8%, 0%, and 46.2%, respectively. The analysis suggests that the tunnel maintains its safest condition when there is a single karst cave with a 5 m distance and a 2 m diameter, and karst caves located at angles of 0° and 90° relative to the tunnel are deemed to be comparatively safer.

### 5.2. Comparative Analysis

In order to analyze the patterns of variation in karst cave parameter states under two different tunnel conditions, a comparative analysis was conducted on the probability distributions of various node value ranges corresponding to the root node state of plastic zone connectivity. The probability distributions of the four karst cave parameters under the two states of the plastic zone are depicted in Figure 9. The figure reveals that when the plastic zone is not connected, indicating a safe state for the tunnel, there are value ranges

with a probability of 0 for both the karst cave distance and angle, implying that a karst cave distance of 1 m and an angle of $45^{\circ}$ are potential major factors influencing tunnel collapse. Conversely, when the plastic zone is connected, indicating a state of tunnel collapse, the probability shares for a karst cave distance of 1 m and an angle of $45^{\circ}$ both rise to $40 \%$, representing the highest probability values for both nodes. This consistency in risk factors is observed in both scenarios. The changes in probability share for the number of karst caves and karst cave diameter parameters are relatively minor in comparison.
![img-7.jpeg](img-7.jpeg)

Figure 8. Bayesian Network state with non-connected plastic zone.
![img-8.jpeg](img-8.jpeg)

Figure 9. Probability distribution of node range.
Under both tunnel conditions, the numerical and trend changes in the probability of each node's value range are depicted in Figure 10. In terms of the number of karst caves, the probability fluctuations for all three quantities are generally small. A decrease of $15.2 \%$ in the probability of plastic zone connectivity is observed when there is only one karst cave, while, in other scenarios, the probability increases, indicating a minor impact of the number of karst caves on tunnel stability. In terms of the karst cave distance, the probability of plastic zone connectivity significantly increases by nearly $40 \%$ when the distance is 1 m , but substantially decreases by $61 \%$ at a distance of 5 m , highlighting the dramatic effect of distance on tunnel stability and indicating a greatly reduced likelihood of tunnel collapse as the distance increases. Regarding the karst cave diameter, the sensitivity to changes in diameter is more pronounced when the plastic zone is not connected, with probability

changes exceeding $20 \%$ for diameters of 2 m and 4 m . As the karst cave angle increases from $0^{\circ}$ to $90^{\circ}$, the probability of plastic zone connectivity first rises and then decreases, with the angle of $45^{\circ}$ being the most unsafe. The patterns of probability changes for each node's value range in the two states are oppositely distributed, and the state with no plastic zone connectivity is more sensitive to changes in the karst cave parameters.
![img-9.jpeg](img-9.jpeg)

Figure 10. Probability changes of node range.
The values of the probability changes are shown in Table 6. In terms of the change rate, the highest change rate compared to the initial state, after the plastic zone becomes continuous, is $6.97 \%$ when the number of karst caves is three. Similarly, a maximal change rate of $28.97 \%$ is observed when the proximity to the karst stands at 5 m ; a principal increase of $11.52 \%$ is noted for karst cave diameters set at 4 m ; and the angle of the karst cave being $45^{\circ}$ leads to the largest change rate, recorded at $20.3 \%$. After analyzing the changes in the probability states of various factors following the connectivity of the plastic zone, it was determined that the most adverse combination of possibilities leading to tunnel collapse under the current state involves three karst caves, a distance of 1 m , a karst cave diameter of 4 m , and an angle of $45^{\circ}$. This implies that the greater the number of karst caves, the closer their proximity, the larger their size, and the closer their location to the tunnel waist (in the $45^{\circ}$ direction), the closer it aligns with common understanding. When the plastic zone was not continuous, the highest change rate was observed to be $39.7 \%$ with only one karst cave. With a karst distance of 5 m , the maximum rate of change reached $156.36 \%$. A karst cave diameter of 2 m resulted in the highest rate of change at $63.03 \%$, and, at a karst cave angle of $45^{\circ}$, the rate of change was found to be $100 \%$. From the probability states of various factors when the plastic zone was not continuous, it was discerned that the optimal combination to maintain the tunnel in a safe state consisted of one karst cave, a distance of 5 m , a karst cave diameter of 2 m , and a karst cave angle of $90^{\circ}$. This indicates that fewer karst caves, greater distances, smaller karst cave sizes, and locations directly above the tunnel similarly align with practical engineering realities.

Table 6. Probability change.


The change rate in the probability of node states can reveal the most favorable or least favorable combinations under different tunnel safety conditions, and, by analyzing the total change in the probability of each node state, it is possible to reflect which parameters have the greatest impact on the model. The ranking of total change is shown in Table 7. It is evident that the model is primarily influenced by the distance and angle of the karst caves, with the distance and angle accounting for more than $70 \%$ (5 out of 7 ) of the parameters with a total change exceeding 20.

Table 7. Total change ranking.


Furthermore, by fixing the probability of node value ranges at $100 \%$, the impact of individual node value ranges on the probability state of the target node was analyzed. By consecutively fixing the probability of each node value range at $100 \%$ while keeping others at the default, the summarized probability of the target node being Yes is as shown in Table 8. As shown in the table, when the distance of the karst cave is 1 m and the angle of the karst cave is $45^{\circ}$, the probability of the plastic zone being continuous is $100 \%$, indicating that the tunnel will collapse under this condition, which is consistent with the conclusions mentioned earlier. Under conditions where the karst cave distance is 3 m , the karst cave diameter is 4 m , the number of karst caves is three and two, and the karst cave diameter is 3 m , the probability of the plastic zone being continuous exceeds $85 \%$ (ranging from $85.2 \%$ to $92.6 \%$ ). This indicates that, in the current model, the occurrence of these individual parameters can lead to a high incidence of collapse accidents.

Table 8. Probability of the target node being Yes.


# 5.3. Sensitivity Analysis 

A sensitivity analysis is utilized to study the extent of each karst cave parameter's impact on tunnel collapse. By calculating the sensitivity coefficients of the Bayesian Network nodes, the sensitivity of each parameter can be determined, as shown in Table 9. The table indicates that the distance of the karst caves has the most significant impact on the target node, followed by the angle and diameter of the karst caves. The number of karst caves has the least impact on the target node, consistent with the previously observed probability distribution changes of each node's value range under the two plastic zone states.

Table 9. Sensitivity coefficient.


## 6. Limitations and Prospects

In this work, a data-driven method of predicting the risk of karst tunnel collapse, which integrates numerical simulation and Bayesian self-learning, was proposed. This method is capable of learning from cases of datasets established by numerical simulations under the conditions described in this paper and constructing a Bayesian Network model. It infers and analyzes the potential risk factors and mechanisms of karst tunnel collapse accidents. Due to certain simplifications and defects in the process of numerical simulation and Bayesian Network construction, it is necessary to provide the following explanations.
(1) In the numerical model, the fillings within the karst caves (such as water, mud, etc.) were not considered. The impacts of this simplification on the distribution of the plastic zones after tunnel excavation were not taken into account.
(2) In reality, the distribution patterns, locations, sizes, and shapes of karst caves follow no predictable pattern. The numerical model employed in this work has chosen only a limited set of specific distribution parameters, rendering it limited in generality. Nonetheless, the outcomes of these numerical simulations are utilized chiefly as the base data for the subsequent Bayesian Network model's learning process, a role that remains commendable.
(3) The node value ranges in the Bayesian Network were non-continuous and nonstandardized quantities, which presented certain defects during the annotation of the dataset. Improvements to subsequent models can be made from this perspective.
(4) The reduction in strength associated with an increase in size was not considered in the numerical model. Arched structures in tunnel construction, such as vaults and inverts, are influenced by the size effect. This aspect should be taken into consideration in future research.

(5) To illustrate the principles of the method proposed in the paper, the Bayesian Network model was constructed using only a single-layer parallel network structure. In reality, the logical relationships among various karst parameters are intricate and complex. It is considered for future research to combine the construction process of the Bayesian Network model's structure with methods such as the analytic hierarchy process (AHP) and analytic network process (ANP) to enhance its accuracy.

# 7. Conclusions 

In this study, a Bayesian Network model for the risk assessment of karst tunnel collapse was established with the Yanglin tunnel as the engineering background, utilizing a self-learning method based on BN case data. The analysis was conducted on the probability distribution and impact of four types of karst cave parameters. The following main conclusions are obtained.
(1) A numerical model comprising 81 parameter combinations based on four factors at three levels was established using the finite element numerical simulation method. The plastic zone distribution of the tunnel body, surrounding rock, and karst caves during excavation was obtained through numerical calculations. When a single karst cave is present, the likelihood of plastic zone connectivity decreases as the distance increases under the same cave radius. With the same angle and distance, the plastic zone is more likely to connect as the karst cave radius increases. In scenarios with two karst caves, when the caves are located at $0^{\circ}$ and $90^{\circ}$ to the tunnel, the plastic zones gradually move away from each other as the distance increases, with the highest likelihood of connectivity at a $45^{\circ}$ angle. In scenarios with three karst caves, under the selected distance parameters, the likelihood of plastic zone connectivity increases with the karst cave radius and also grows with the number of karst caves.
(2) Based on the data case library obtained from the numerical simulation results, each node corresponded to specific karst cave parameters. A Bayesian Network model for the risk assessment of karst tunnel collapse was established through self-learning from the BN data cases, resulting in the determination of the probability distribution of each node's state in the initial condition. The robustness of the Bayesian Network model was tested, and the results indicated that with a missing data rate of $10 \%$, the total error rate of the predictions was $4.43 \%$, demonstrating that the model possessed good predictive accuracy.
(3) Through the established Bayesian Network model for karst tunnel collapse risk assessment, a quantitative and sensitivity analysis was performed on the probability of various karst cave parameters during instances of tunnel collapse and non-collapse. It was found that the distance of the karst caves has the greatest impact on the probability of tunnel collapse, followed by the angle and diameter of the karst caves. The number of karst caves has the least impact on the target node. An analysis was conducted on the changes in node probabilities and the impact of individual node value ranges on the probability state of the target node. Under conditions where the karst cave distance is 3 m , the karst cave diameter is 4 m , the number of karst caves is three and two, and the karst cave diameter is 3 m , the probability of the plastic zone being continuous exceeds $85 \%$ (ranging from $85.2 \%$ to $92.6 \%$ ). This indicates that, in the current model, the occurrence of these individual parameters can lead to a high incidence of collapse accidents.

Author Contributions: Conceptualization, J.S.; Methodology, J.S., Y.W. and X.W. (Xu Wu); Software, Y.W. and X.W. (Xinling Wang); Formal analysis, Y.W., H.F. and Y.S.; Writing—original draft, Y.W.; Writing-review and editing, Y.W., X.W. (Xu Wu), X.W. (Xinling Wang), H.F. and Y.S.; Supervision, J.S.; Funding acquisition, Y.W. All authors have read and agreed to the published version of the manuscript.

Funding: We are grateful for the support of the Open Fund of Engineering Research Center of Concrete Technology under Marine Environment (Grant No. TMduracon2022016), Shandong Provincial Natural Science Foundation (Grant No. ZR2023QE136), and Chunhui Program of Ministry of Education (Grant No. 202201798).

Data Availability Statement: The data presented in this study are available on request from the corresponding author.

Conflicts of Interest: The authors declare no conflicts of interest.
