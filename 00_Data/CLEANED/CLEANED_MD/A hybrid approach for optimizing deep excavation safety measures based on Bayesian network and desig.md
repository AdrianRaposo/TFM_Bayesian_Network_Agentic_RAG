# A hybrid approach for optimizing deep excavation safety measures based on 

Bayesian network and design structure matrix

Yongcheng Zhang ${ }^{\mathrm{a}, *}$ Xuejiao Xing ${ }^{\mathrm{b}}$, Maxwell Fordjour Antwi-Afari ${ }^{\mathrm{c}}$<br>${ }^{a}$ Department of Construction Management, Huaiyin Institute of Technology, Huaian, 223003, China. Email:<br>cquzhych@126.com<br>${ }^{\mathrm{b}}$ Department of Investment, School of Finance, Zhongnan University of Economics and Law, Wuhan 430074,<br>Hubei, China<br>${ }^{\text {c }}$ Department of Civil Engineering, College of Engineering and Physical Sciences, Aston University, Birmingham, B4 7ET, United Kingdom.


#### Abstract

Considering the dynamic risk factors and risk situation throughout the entire deep excavation operations, timely adjustment and optimization of safety measures can enhance the practicality of construction technical plans on sites. A digital and quantitative model representing the practical risk situation of the deep excavation is urgently required for realizing the prediction, optimization, and control of the actual construction state. Thus, this research aims to propose a real-world-oriented model integrating Bayesian network (BN) and design structure matrix (DSM) for decision-making in safety risk management. First, risk factors were identified, and the BN model was established to evaluate the anti-risk ability of the construction site. Then, a multi-objective safety measure optimization model under specific constraints was established. Particularly, the DSM was adopted to express the control relationship between risk factors and safety measures. Moreover, with genetic algorithms applied, the optimal safety measure set for on-site safety risk management can be obtained. For model validation, a deep excavation project of metro construction in Wuhan, China, was selected as a case study. The hybrid optimization model showed the characters of initiative and timeliness in construction risk management. By providing the timely and optimized combination of safety measures, the dynamic decision-making approach can proactively and effectively improve the risk resistance ability of construction sites.


Keywords: deep excavation, dynamic safety risk management, multi-objective optimization, digital twin model

## 1 Introduction

Deep excavation is a complex construction operation with numerous potential risks [1]. For ensuring safety management on sites, construction activities need to be undertaken following the guidance of technical plans [2]. In this process, potential risks can be addressed for proactive management [3]. Especially, the deep excavation construction is a dynamic and comprehensive information system involving the construction method, the construction process, the dynamic risk situation, and the construction cost and duration, etc. For mitigating involved risk factors, safety measures must be adjusted consistently according to the dynamic situations in construction to improve safety performance [1][4]. However, in practice, the determination of safety measures is primarily reliant on the subjective expertise of engineers. Moreover, the static construction technical plans generated prior to the construction phase pose challenges in terms of adaptability to the dynamic nature of the construction site, which may lead to poor performance on risk control, cost, and duration. Addressing the above issues, a digital and quantitative approach is urgently required for supporting the prediction, optimization, and

control of the dynamic practical risk situation of the deep excavation [1].
With the emergence of digital twin and other information technologies [5], novel technical approaches have been stimulated for the management and reuse of construction safety special plans. The application of digital twin in the engineering field can be understood as the representation of digital information-oriented physical systems and support for managing these systems [6]. Based on the semantic and digital expression of construction safety special plans, the utilization of digital twin technology in construction risk management has demonstrated significant potentials [7]. Digital twin models can be used to analyze, predict and diagnose the risk situations. Then the simulation results are fed back to the real construction sites, thus helping to optimize and make decisions on the risk management. The above statement serves as the starting point of this research.

Thus, differing from the conventional research method [8], this research aims to develop a real-world-oriented simulation based on cyber-physical synchronicity for safety risk management in construction scenarios, utilizing data-driven engineering and synchronized physical information. Specifically, a hybrid safety measure optimization model, based on integrating Bayesian network (BN) and design structure matrix (DSM), was established. By synchronously updating and analyzing the dynamic practical risk situation of the deep excavation, the hybrid model can facilitate objective decision-making by providing optimal safety measures for effective safety risk management. It is noted that the model is dynamic and capable of adapting to changes in decisionmaking situations on construction sites. In addition, safety measures can be dynamically adjusted to adapt to the dynamic construction sites and further improve the safety measures planning. Details of the application procedures and key technologies of the proposed approach has been described in this research. Ultimately, a practical deep excavation case was adopted to verify the effectiveness of this approach.

This research represents a novel approach for managers and engineers in the selection of safety measures, aiming to enhance risk factor control and optimize the performance of safety management. From the perspective of optimizing construction safety plans dynamically, the research findings can facilitate the application of digital twin technology in guiding construction safety management on sites.

# 2 Background 

### 2.1 Automatic safety risk management platforms in construction

In recent years, various tools and platforms have been studied and applied to support the automatic safety risk management in construction. These tools and platforms have been extensively studied and applied to address different complex challenges. For example, Zhou et al. proposed a BIM-based 4D model as an integrated tool to present the real-time visualization safety status of related components under changing conditions [9]. Kim et al. proposed a BIM platform that can prevent fall-related accidents by reporting safety measures in advance [10]. In this manner, automated hazard identification and safety checking in construction process can be realized. Moreover, other existing studies have explored potential methods (e.g., Bayesian Networks, fuzzy decisionmaking model) for safety risk identification and management in deep excavation-related fields [11][12]. Ding et al. established an ontology-based methodology for construction risk knowledge management through information model and semantic web technology [13]. Lee et al. developed a risk management system for deep excavation based on BIM-3DGIS framework and optimized grey Verhulst model [14]. Also, information integration and exchange were needed to be considered in the above BIM technology applications. A semantic industry

foundation classes (IFC) data model was proposed for automatic safety risk identification in dynamic deep excavation process [7].

Specially, digital twin technology can provide real-time virtual models and data that accurately reflect both the semantic and geometric attributes and functions of infrastructures. In this process, three prevalent functional categories of digital twins are identified: (1) status twins for monitoring the physical condition of objects and equipment; (2) operation twins for adjusting operating parameters based on linked actions and/or workflows; and (3) simulation twins for predicting how an objective or device responds to operational conditions in the future [15][16]. The integration of data-driven site management and digital twin technology has emerged as a robust problem-solving approach [17][18][19], which has also shown great potentials on risk management in construction [6].

# 2.2 Decision-making on safety measures for risk management 

Few existing studies on the selection of safety measures for risk factor control, as well as methods for establishing anti-risk capabilities of construction sites and identifying optimal solutions, are found within extant literature [1]. Generally, the process of decision-making of safety measures consists of two steps: (1) the network of risk factors and events, which shows the causal relationship matrix between risk factors and safety measures; (2) the combination of optimization models for safety measures. For the former, previous methods such as fuzzy fault trees [20] and Bayesian network (BN) [21][22] have been used to support safety management. Specifically, BN has the advantage of expressing the uncertain knowledge and reasoning simulated by human thought, and has been widely used in fault diagnosis [23] and risk assessment [24]. For the latter, multi-objective models have been proposed. The multi-objective optimization is an effective scientific approach for modeling Pareto frontier optimization problems, which has been widely applied in both practical engineering scenarios and the research field of safety management. Integrating with heuristic algorithms, optimal solutions on construction site layout [25], camera placement [26], and other engineering problems can be obtained. Zhang and Xing proposed a fuzzy multi-objective particle swarm method to model and solve the optimization problem of time-cost-mass equilibrium [27]. Xu and Song analyzed the multi-objective dynamic layout of temporary facilities on construction site under fuzzy random environment [28]. It is proved that the multi-objective optimization has been an effective method to model and solve the dynamic, fuzzy, and multi-factor problems in the engineering and construction field.

### 2.3 Research gaps and objective

The above studies have demonstrated the potential of using different platforms in facilitating automatic risk management in construction projects. Safety risk identification and safety measure decision-making are indeed the two sides of one coin, which should be considered at the onset. Traditionally, the selection of safety measures for risk control often depends on the text of construction technical plans or an expert's experience in deep excavation. For mitigating the potential risk events involved in the deep excavation, safety measures must be applied according to the dynamic construction situations to improve safety performance. How to establish an approach according to the actual decision-making process which supports engineers to achieve a better performance of safety, duration, and cost on complex construction sites such as metro station construction projects is still challenging. It is noted that the dynamic management and application of construction safety

special plans is a crucial aspect of the entire site management system, which involves the seamless integration of the semantic data and the digital information-oriented physical system. Based on the integration of the special plan management data and real-time monitoring data under the construction site information system, the generation and optimization of the "physical system-digital plan" management scheme under the digital twin technology can be realized [9][29][30]. This is a potentially valuable technical approach for the safety management of deep excavation.

Consequently, this research aimed to propose an approach describing and supporting the decision-making process of safety measures. For overcoming the subjectivity and one-sidedness of engineers in decision-making under static construction technical plans, a real-world-oriented intelligent and automatic optimization approach of safety measures was developed in this research, based on cyber-physical synchronicity. Considering the dynamic nature and uncertainty inherent in engineering construction, a multi-objective optimization model of safety measures based on the information feedback on sites was explored. That is, the model was dynamic and adaptable to changes in construction site deep excavation operations. Compared to the static construction technical plans that are produced before the construction stage, the hybrid approach proposed in this research can show characters of initiative and timeliness in construction risk management. It would enable managers and engineers to select optimal safety measures while considering risk control for deep excavation projects.

# 3 Methodology 

### 3.1 Overview

For guiding the deep excavation operations, the dynamic decision-making of safety measure optimization for safety risk management was analyzed and expressed in Fig. 1. In the form of IDEFO model, two main stages were included.

- Stage of construction site management: Under the construction site management system and special construction technical plans, construction activities (i.e., A0) on sites proceed in an orderly manner.
- Stage of safety risk management: Considering the dynamic risks on sites, safety risk management activities (i.e., A1), including risk factor identification, risk event network construction, and accordingly anti-risk ability evaluation were conducted. According to the evaluation results and the requirements of construction site risk control, the influence factors of measure selection and the priority rules of influence factors were analyzed. Then, with the optimization model development, the optimal combination of safety measures can be obtained (i.e., A2) to support the dynamic safety risk management.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Workflow of the dynamic decision-making of safety measure optimization for safety risk management.
In the above process, safety risk management (i.e., A1) and decision-making of safety measures (i.e., A2) were the two core activities involved in the risk management stage. Correspondingly, a hybrid safety measure optimization model integrating Bayesian network (BN) and design structure matrix (DSM) was proposed in this research to implement these two steps. By utilizing this model, the primary steps of safety risk management in deep excavation were listed as follows: (1) the integration of the special plan management data and real-time monitoring data under the construction site information system; (2) risk factor identification; (3) anti-risk ability evaluation; (4) acquisition and implementation of optimal safety measures; (5) safety performance evaluation. Key points for realizing the above steps were expressed in detail in the following subsections.

# 3.2 Bayesian network (BN) for risk factor assessment 

Bayesian network (BN), as a graphical formalism by representing the relationship between events and factors, can effectively carry out multi-source information expression, fusion, and uncertainty reasoning the knowledge or information based on the joint probability distributions [31][32]. BN is composed of network structure and probability parameters. In BN, nodes are connected by the directed line to form the network and are also called variables [33]. The directed line shows the relationship between variables, which is described by using the conditional probability table (CPT). Given that $\mathrm{BN} \mathrm{B}=\langle\mathrm{M}, \mathrm{K}\rangle, \mathrm{M}$ is the directed acyclic graph, and K is the set of the probability of variables. Given that $\mathrm{M}=\left\{\mathrm{X}_{1}, \mathrm{X}_{2}, \ldots, \mathrm{X}_{n}, \mathrm{~V}\right\}, \mathrm{X}_{i}$ represents the node $i(i=1,2, \ldots, n)$; and V is the set of the edges of networks. Given that $\mathrm{X}_{i}$ and $\mathrm{X}_{i+1}$ nodes, if the arrow points from $\mathrm{X}_{i}$ to $\mathrm{X}_{i+1}$ and no other arrow points to $\mathrm{X}_{i}$, the $\mathrm{X}_{i}$ can be called the parent node, and $\mathrm{x}_{i+1}$ is the child node. The probability of the parent node is named prior probability, and the probability of other nodes is named conditional probability. Given node X and parent nodes $\mathrm{X}_{i}$, when nodes $\mathrm{X}_{i}$ is independent of each other, according to the chain rule, the equation is:

$$
P=\left(X_{1}, X_{2}, \cdots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid P_{x}\left(X_{i}\right)\right)
$$

$$
P\left(X_{i} \mid Y\right)=P\left(Y \mid X_{i}\right) P\left(X_{i}\right) / \sum_{i=1}^{n} P\left(Y \mid X_{i}\right) P\left(X_{i}\right)
$$

where the $n$ is the number of child nodes; $P\left(\mathrm{X}_{i}\right)$ is the prior probability of node $i(i=1,2, \ldots, n) ; P\left(\mathrm{Y} \mid \mathrm{X}_{i}\right)$ is the conditional probability; $P\left(\mathrm{X}_{i} \mid \mathrm{Y}\right)$ is the posterior probability.

The occurrence probability of the node Y (i.e. the risk event) can be calculated based on Equation (2) to reason the occurrence of a risk event. In addition, based on the backward reasoning of Equation (2) when given $\mathrm{Y}=1$, key risk factors contributing to the occurrence of risk events can be identified considering the occurrence influence, which is the Sensitivity Analysis of BN. Key risk factors should be paid additional attention to the safety management of deep excavation. In this research, the main steps of BN establishment for risk factor assessment were described as follows:

- Step 1: BN establishment for safety management. In general, the BN can be obtained by transforming the fault tree analysis [20], which is a common approach that identifies and accesses the factors leading to an accident. According to domain expertise and literature, the BN was determined into three levels, namely risk accident, risk event state, and risk factors.
- Step 2: Determination of the occurrence probability of risk factors. The probability of risk factors, also called prior probability, can be computed based on past accident data or experts' experiences. However, in practice, complete data on accidents or events is often difficult to collect, and experts and experienced engineers can also provide a critical review of the risk factor. Questionnaire is used to analyze the risk in this research, and then, the prior probability of risk factors is calculated by a weighted average of questionnaires, which is readjusted by experts and engineers.
- Step 3: Determination of the conditional probability of risk factors. For the children node of BNs, the occurrence probability is described by the CPT. Children nodes are divided into two types based on the value, including $\{0,1\}$ and $(0,1)$, which represent an un-occurrence or occurrence and uncertainty of occurrence, respectively. For the first type, the CPT is achieved by a logical analysis of its parent nodes. For the second type, the CPT can be obtained by network learning or experts' experience.


# 3.3 Causal relationship matrix between safety measures and risk factors 

Design structure matrix (DSM) is introduced as a straightforward and flexible modeling technique that can be used for designing, developing, and managing complex systems [34]. DSM offers network modeling tools that represent the elements of a system and their interactions [35]. A numerical matrix with m rows and n columns is a widely used approach for representing the relationship of a digraph, where m represents the number of nodes while n denotes the number of edges in the digraph [36]. Specifically, the matrix layout is as follows: the system element names are placed down the side of the matrix as row headings and across the top as column headings in the same order. If an edge from node $i$ to $j$ exists, then the value of element $\mathrm{a}_{\mathrm{i j}}$ (row $i$, column $j$ ) is unity and given with a numerical mark.

In this research, the DSM method was modified to establish the relationship matrix of factors and measures. Rows and columns were headed with the complete list of measures to be taken and factors to be controlled in the project. Values in the matrix explain if causal relations exist among the measures and risk factors. It described the reduction of occurrence probability of risk factors when relevant measures were taken. Three main steps are considered in the relationship matrix establishment: (1) list the risk factors and corresponding measures of

accident event; (2) enter marks in the causal relationship matrix; (3) check with engineers and managers to verify CSM. In deep excavation, given risk factors set $\mathrm{X}=<\mathrm{X}_{1}, \mathrm{X}_{2}, \ldots, \mathrm{X}_{i} \ldots, \mathrm{X}_{m}>$ and safety measures set $\mathrm{S}=\left(\mathrm{S}_{1}\right.$, $\left.\mathrm{S}_{2}, \ldots, \mathrm{~S}_{j} \ldots, \mathrm{X}_{n}\right) . \mathrm{X}_{i}$ is the risk factor $i(i=1,2, \ldots, m) . \mathrm{S}_{j}$ is the safety measures $j(j=1,2, \ldots, n)$. Given Q as the causal relationship matrix, the matrix is represented as follows:

$$
\mathrm{Q}=\left[a_{i j}\right]_{m n}
$$

where $a_{i j}$ is the probability reduction of risk factor $i$ when safety measure $j$ is taken.
Table 1 shows the causal relationship matrix. The matrix can be obtained by the case data or questionnaires answered by experienced engineers.

Table 1. Causal relationship matrix.


In this research, considering the difficulties in case data collection, a questionnaire was adopted to obtain the matrix. In addition, the impacts of selected safety measures on the dynamic risk situation, construction cost, and duration were evaluated using the questionnaire to support the objective function calculation. In this process, fuzzy linguistic terms were used to represent the qualitative opinions of the impact on the index into quantitative value [37]. Table 2 shows the fuzzy linguistic terms and their corresponding type-1 fuzzy sets.

Table 2. Linguistic terms of the impaction and their corresponding type-1 fuzzy sets.


Based on Table 2, a questionnaire of safety measures was designed and shown in Table 3, by which the value of the index can be calculated.

Table 3. Questionnaire of safety measures (partly).


$\mathrm{X}_{1}$ : Water seepage $\quad \mathrm{S}_{1}$ : Drain to relieve pressure with diversion pipes.
from sidewall $\quad \mathrm{S}_{2}$ : Grout to seal seepage sites.
Note: The risk factor of water seepage from sidewall $\left(\mathrm{X}_{1}\right)$ can be controlled by the measures of $\mathrm{S}_{1}$ and $\mathrm{S}_{2}$. How about the impact of safety measures on the risk reduction of factors, cost, and duration? The impact of measures on risk reduction, $\mathrm{c}\left(\mathrm{S}_{1}\right)$, and $\mathrm{t}\left(\mathrm{S}_{1}\right)$ was divided into seven levels, including Very-low (VL), Low (L), Medium-low (ML), Mediumn(M), Medium-High (MH), High (H), and Very-High (VH).

# 3.4 Multi-objective optimization model of safety measures 

### 3.4.1 Combination optimization model

The occurrence of risk factors is bound up with the implementation of safety measures on the deep excavation site. In general, if the adopted safety measures are comprehensive, the occurrence probability of risk factors can be low. Nevertheless, more safety measures may cause an increase in risk addition, cost overrun, and duration delay. In addition, the effect of different safety measures controlling the risk factors varies [1][29]. Therefore, the optimization model of safety measures decision-making was designed in this research, with an objective function and achieving the optimal balance among dynamic risk situations, construction costs, and duration impacts while meeting safety management requirements. The risk index was defined as the influence of the occurrence of risk factors on a project under the measures selected and implemented. The cost impact index referred to the ratio of increased cost to the project cost when proposed safety measures were performed, showing the impact on the project. The duration influence index referred to the influence of the increased time on the project when safety measures were implemented.

- Objective function:

$$
\operatorname{Min} Q=w_{1} \sum_{j=1}^{n} k_{j} * c\left(\mathrm{~S}_{j}\right)+w_{2} \sum_{j=1}^{n} k_{j} * t\left(\mathrm{~S}_{j}\right)
$$

- Constraint functions:

$$
\begin{aligned}
& \left\{\begin{array}{l}
P\left(\frac{X_{i}}{S_{j}}\right)=p\left(X_{i}\right) * \sum k_{j} * \Pi\left(1-a_{i j}\right) \\
P(a)=\sum p\left(\frac{X_{i}}{S_{j}}\right) \mathrm{p}\left(\frac{a}{X_{i} / S_{j}}\right) \\
P(a) \leq P(1-\eta) \\
k_{j}=\left\{\begin{array}{l}
1, \mathrm{~S}_{j} \text { is selected; } \\
0, \text { otherwise }
\end{array}\right\}
\end{aligned}
$$

where $\mathrm{S}_{j}$ is the safety measure $j$;
$c\left(\mathrm{~S}_{j}\right)$ is the cost impact index of safety measure $j$, ranging from 0 to 1 ;
$t\left(\mathrm{~S}_{j}\right)$ is the duration impact index of safety measure $j$, ranging from 0 to 1 ;
Q is the composite index of the safety measure $j$ implemented;
$k_{j}$ is the variable of whether safety measure $j$ is selected, and $\mathrm{k}_{j}=\{0,1\}$;
$w_{1}$ and $w_{2}$ are weights of cost impact index and duration impact index, respectively;
$\Pi$ is the value of causal relationship matrix, and $\mathrm{a}_{i j}$ is the reduction degree of occurrence probability of risk factor $i$ when safety measure $j$ is performed, ranging from 0 to 1 ;
$P\left(\mathrm{X}_{i} / \mathrm{S}_{j}\right)$ is the occurrence probability of risk factor $i$ when safety measure $j$ is applied;
$P(a)$ is the occurrence probability of risk accident when safety measures are applied;
$P^{\prime}$ is the value of early warning of risk accidents;
$\eta$ is the redundancy of the occurrence of risk accidents.
In summary, the objective function of Equation (4) aimed to explore the minimal trade-offs between construction cost and duration. Equation (5) represented the occurrence probability of risk events after safety measures were performed, which required to be lower than the value of safety early warning.

# 3.4.2 Genetic algorithm for the multi-objective optimization model 

Finding the optimal safety measures to achieve the best performance of risk management is a combinatorial optimization, which is considered a nondeterministic polynomial-time (NP) hard problem [35]. Genetic algorithm (GA) can be used to identify global near-optimum trade-offs and does not tend to be stuck at a local optimum [38][39]. The main steps of using GA to obtain optimal solutions are as follows:

- Step 1: Coding. The safety measures are encoded in the form of a string with 0 or 1 , which is called a chromosome, or an individual, where 0 represents that the measure is not selected, and 1 indicates that the measure is selected for safety management. The length of the chromosome is $n$.
- Step 2: Initialization. N individuals are generated, forming a population.
- Step 3: Fitness value evaluation of each individual. The fitness value is the indicator that reflects the bad and the good of individuals.

$$
F(\mathrm{I})=c_{\max }-Q(\mathrm{I})
$$

where $F(\mathrm{I})$ and $Q(\mathrm{I})$ are the fitness value and the objective function value of individual I respectively; $c_{\text {max }}$ is a constant. As the fitness value increases, the individual gets better.

- Step 4: Selection. The strategy of best retention option, as a common method, is used to operate individual selection. $\mathrm{M}(\mathrm{M}<\mathrm{N})$ individuals with a larger value than others are chosen for the next generation operation.
- Step 5: Crossover: Crossover is the operation that the genes of the selected two individuals are exchanged according to probability $\left(\mathrm{P}_{\mathrm{c}}\right)$ to produce a new individual, often, $\mathrm{P}_{\mathrm{c}}=[0.4,0.99]$.
- Step 6: Mutation. Some individuals are randomly chosen from the above population for mutation. The gene of selected individuals is randomly changed with the mutation probability Pm to generate new individuals, replacing the original individuals in the population. In general, $\mathrm{P}_{\mathrm{m}}=[0.0001,0.1]$. Turn to step 3.
- Step 7: The iteration stops and the optimal result is outputted. The iteration is stopped when the solution fitness curve exhibits convergence. The optimal solution for problem-solving is obtained by decoding the outputted chromosome.

Integrating the established BN, causal relationship matrix, and multi-objective optimization model, the occurrence probability of risk accidents for the specific project can be predicted, and the key factors can be identified by feedback reasoning under the given occurrence probability of risk accidents. The above multiobjective optimization model can greatly support the optimal safety measure selection. Moreover, the anti-risk ability of construction sites and the risk-cost-duration index under specific safety measure sets can be outputted at the same time.

### 3.5 Evaluation metric of the application effect of the optimized safety measures

For further evaluating the application effect of the optimized safety measures, a safety index was adopted in this research (Eqs. 7 and 8). In this way, the safety performance of the targeted project, relating to the construction specification, can be reflected.

$$
\begin{gathered}
V=1-\frac{1}{t} \sum_{i=1}^{t} r_{i}, \quad i=1,2, \ldots, t \\
r=\left(r_{m}+r_{p}\right) / 2, \quad r_{m}=\sum_{j=1}^{n} r_{n}^{\prime}, \quad j=1,2, \ldots, n
\end{gathered}
$$

where $V$ is the value of the safety index $(V=[0,1]) ; t$ is the duration of construction; $r_{i}$ is the value of risk degree; $r_{m}$ is the level of risk related to each monitoring item; $r_{P}$ is the level of risk as assessed by safety patrol; and $r_{n}{ }^{\prime}$ is the risk associated with monitoring point $n$.

# 4 Case study 

### 4.1 Case background

One deep excavation project was chosen in this research as an example to describe the application process of the proposed approach and evaluate its effectiveness in safety measure decision-making. The example referred to a metro station construction in Wuhan city, Hubei province, China, which is located at the T-junction of the Guanshan Road and Luoyu Road with heavy traffic. The area of the deep excavation is approximately $6,400 \mathrm{~m}^{2}$, and the depth is 17.5 m . An open-cut method is adopted to excavate. Table 4 shows the characteristics of the construction project. At present, the construction process is in the third soil excavation, and the overall situation of safety management on a construction site is well-managed. In this research, the risk event of collapse was selected as the targeted risk to develop the case study.

Table 4. Characteristics of the construction project.


### 4.2 Dynamic decision-making of safety measures

### 4.2.1 BN for the collapse risk of deep excavation

In this research, the collapse risk of deep excavation was chosen as the example to explain the dynamic decision-making of safety measures. Based on the analysis and adjustment of the documents with experts' experience, risk factors and accordingly main safety measures were summarized in Table 5. Concretely, experts and engineering practitioners with rich domain experiences were invited to a seminar. The knowledge sources encompass: (a) practical knowledge derived from design specifications and construction manuals, (b) theoretical knowledge acquired from statistical models in academic papers, and (c) tacit knowledge possessed by domain experts. Especially, for avoiding the subjectivity from experts in the process of determination, safety measures in similar projects were searched in the case database of the construction technology plan [1]. The discussion results were summarized by the seminar.

Table 5. Risk factors and safety measures of the collapse risk of deep excavation.



Based on the seminar results and Table 5, the BN of the collapse risk of deep excavation was established in this research, mainly including ten risk factors (i.e. X1 X10), two risk states (i.e. M1: Poor stability of soil in foundation pit; M2: Failure of support system) and one risk event (i.e. T: Collapse risk). Then, the designed questionnaires were distributed to 100 experienced engineers from 10 station construction projects. The average occurrence probability of risk factors and the conditional probability of risk states in the BN were determined. Fig. 2 depicts the BN of the collapse risk of deep excavation integrating probabilities of nodes, which was generated through Genie 2.0. According to the implication of the Bayesian network structure, the causal relationship between any two points can be presented by the directed arrow. In particular, ten risk factors (i.e. X1 X10) were defined as being independent of each other.

![img-1.jpeg](img-1.jpeg)

Fig. 2. BN of the collapse risk of deep excavation with probabilities of nodes.

# 4.2.2 Causal relationship matrix for the collapse risk management 

Through expert interviews with 20 engineers from 10 projects, the mean value of the causal relationship matrix was calculated based on the fuzzy linguistic terms and fuzzy sets in Table 2. Table 6 presents the causal relationship matrix between safety measures and risk factors.

Table 6. Causal relationship matrix between safety measures and risk factors.


### 4.2.3 Anti-risk ability evaluation of construction sites

Key risk factors that may deeply affect the accident occurrence can be identified by the feedback reasoning of the BN. The sensitivity analysis method was used to test the impaction of change of factors on the occurrence of risk events. Set the occurrence probability of an accident as $100 \%$, and the involved key factors can be identified. Fig. 3 shows that $\mathrm{X} 1, \mathrm{X} 3, \mathrm{X} 4, \mathrm{X} 7, \mathrm{X} 9$, and X 10 are sensitive factors in this construction site situation, which means the occurrence of the risk event is more sensitive to these six risk factors. Effective safety measures should be adopted to control these factors preferentially in the safety management of deep excavation.

![img-2.jpeg](img-2.jpeg)

Fig. 3. Key factor identification in the collapse risk.
According to the latest safety inspection, safety measures that have been implemented on construction sites were confirmed: $\mathrm{S}_{22}$ : Strengthen the survey work and improve the accuracy of survey data; $\mathrm{S}_{23}$ : Strengthen the construction site inspection, and reinforce the support system when problems were found; $\mathrm{S}_{24}$ : Strictly implement monitoring plans, and strengthen early-warning analysis; and $\mathrm{S}_{25}$ : Strengthen the construction site inspection, and find and warn hidden dangers timely., etc. Based on the BN in Fig. 2 and the causal relationship matrix in Table 6 , the anti-risk ability of construction sites was evaluated. In this phase of deep excavation, the occurrence probability of the collapse risk of deep excavation was $11 \%$, which exceeded the safety warning value of $10 \%$. Therefore, it was necessary to take timely and effective safety measures to enhance the anti-risk ability of construction sites.

# 4.2.4 Optimal safety measure set selection 

Considering the safety warning value of the collapse risk (i.e., $10 \%$ ), the multi-objective model was adopted and calculated based on the GA, using Matlab R2016b. In this process, safety measures selection or not was coded as 1 or 0 , and the value of $\eta$ was assigned to $10 \%$ according to the requirements of safety management. In particular, for achieving the optimal safety measure set with appropriate cost-duration tradeoff index, safety warning values of $4 \%, 6 \%, 8 \%$ and $10 \%$ were inputted into the multi-objective model. Accordingly, the iterations of optimal solutions under different safety warning values were shown in Fig. 4.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Results of GA of the multi-objective model (figures of (a)-(d) were under safety warning values of $4 \%$, $6 \%, 8 \%$ and $10 \%$ respectively).
Table 7 shows the output optimal safety measure sets under different safety warning values. Integrated with the cost-duration tradeoff index, safety measure set of No. 2 was adopted in this project as the optimal solution. That is, the optimal safety measures were $\mathrm{S}_{2}, \mathrm{~S}_{3}, \mathrm{~S}_{6}, \mathrm{~S}_{7}, \mathrm{~S}_{8}, \mathrm{~S}_{10}, \mathrm{~S}_{11}, \mathrm{~S}_{12}, \mathrm{~S}_{15}, \mathrm{~S}_{18}, \mathrm{~S}_{25}$, and $\mathrm{S}_{26}$. According to the causal relationship matrix between safety measures and risk factors in Table 6, the above measures mainly aim to control risk factors of $\mathrm{X}_{1}, \mathrm{X}_{2}, \mathrm{X}_{3}, \mathrm{X}_{4}, \mathrm{X}_{5}, \mathrm{X}_{7}$, and $\mathrm{X}_{10}$. Risk factors can be controlled to meet the requirement of collapse risk prevention.

Table 7. Optimal safety measures under different safety warning values.


Through the causal relationship matrix in Table 6 and Equation (4), the occurrence probability of risk factors under the selected safety measures was determined. In this circumstance, the anti-risk ability of the construction site under optimal safety measures was calculated as 5\% (Appendix). It was indicated that the optimal solution can improve the anti-risk ability of collapse and enhance safety management in the deep excavation.

# 5 Results 

According to the generated optimal safety measure sets, engineers on sites can update the safety measure plan, keep track, and implement them as required. The construction site was inspected by engineers for eight times in two months, confirming that safety measures were well-performed. Also, the managers confirmed that no risk

events occurred during this duration. According to the recent on-site safety inspection, safety measures of $\mathrm{S}_{2}, \mathrm{~S}_{6}$, $\mathrm{S}_{8}, \mathrm{~S}_{11}, \mathrm{~S}_{14}, \mathrm{~S}_{17}, \mathrm{~S}_{20}, \mathrm{~S}_{22}, \mathrm{~S}_{23}$, and $\mathrm{S}_{25}$ were implemented to manage risk factors. Based on the multi-objective optimization model, the $P(\mathrm{a})$ (occurrence probability of collapse) is 0.043 , and the Q (negative influence) is 2.85 . The implementation of these safety measures effectively reduced the occurrence probability of risk factors and then made the risk events under control. The performance of the implemented safety measures was better than the decision based on managers' experience, due to the minimal trade-offs among the dynamic risk situation, construction cost, and duration.

At the same time, three deep excavation projects constructed simultaneously were selected in this case study. These three projects are Luoxiong Road Metro Station, Guanggu Road Metro Station, and Jiayuan Road Metro Station, which have similar project background (including weather, duration, location, etc.) and features (e.g., construction size, surrounding environment, etc.) with the targeted project. Above three deep excavation projects were used to compare with the targeted project, under the same BN network, to verify the effectiveness of the proposed approach. Basic information on three projects was obtained from the case database which was numbered as No. 180, No. 182, and No. 183, respectively. Table 8 lists the basic information about the target project and the other three projects.

Table 8. Basic information on four construction projects.

complex | Medium-complex  |
complex | Medium-complex  |

The engineers conducted the safety patrol on four construction sites, and some monitoring data were recorded using the Safety Early-Warning System [28].

![img-4.jpeg](img-4.jpeg)

Fig. 5. Changes in the safety index among four construction projects.
Fig. 5 shows the changes in safety index among four construction projects and that the safety index of the targeted project was higher than the other three construction projects and the mean value of four projects. This result reflected that the safety performance of the targeted project was better than the other three construction projects when guided by a dynamic safety technical plan. The optimized plan can achieve a $100 \%$ risk occurrence reduction with minimal cost and duration, which performed better than similar construction projects without the guidance of dynamic construction technical plans. Integrating the dynamic construction process, the application effect of the dynamic optimized construction technical plan was illustrated as follows:

- During the first phase of enclosure construction, there was no significant difference in the safety performance of the four projects. The risk was without evident accumulation on sites at the beginning of construction. Moreover, the technical plan has not been optimized at this construction stage.
- In the progress of excavation and retaining structure construction, risk cumulated on the construction site gradually with earth excavation and supporting system construction, including the deformation of retaining structure, foundation pit stack, rainfall, poor-quality support, and untimely. Appropriate optimized safety measures must be adopted to control risk factors when the security early warnings are released by the security warning system or engineers' safety inspection on the site.
- With the completion of the enclosure and earthwork excavation, the construction risks were gradually released and controlled by the safety measures of the dynamic optimized construction technical plan during the main structure construction. In addition, site safety performance improved compared with the other three construction projects under the non-dynamically optimized construction technical plan guidance.


# 6 Discussion 

Compared to the static construction technical plans that are produced before the construction stage, it is urgent to realize the dynamic optimized construction technical plans to guide deep excavation operations. The digital twin model was explored in this research to improve the performance and efficiency of safety risk management of deep excavation. Specifically, a hybrid safety measure optimization model was proposed, which demonstrated characteristics of initiative and timeliness in reflecting practical safety risk situation and guiding construction risk management. First, for guiding the deep excavation process, the dynamic decision-making of

safety measure optimization for safety risk management was analyzed. Two main stages were included in this process: construction site management and safety risk management. Then, Considering the dynamic risks on sites, safety risk management activities (e.g., risk factor identification, risk event network construction, and accordingly anti-risk ability evaluation) were analyzed in this research. According to the evaluation results and the requirements of construction site risk control, the influence factors of measure selection and the priority rules of influence factors were explained. Last, with the optimization model development, the optimal combination of safety measures can be obtained to support dynamic safety risk management.

The application effect of the proposed approach was evaluated in a practical project in the case study, with the application process description and the comparison with three other similar projects. By providing the optimized combination of safety measures and supporting decision-making, it was proved the proposed approach can proactively improve the risk resistance ability of the construction site. Especially, different construction stages in the dynamic construction process were considered. The technical plan of the target construction project was deepened and optimized timely in the process of construction engineering under the dynamic evaluation of risk events. At this moment, this plan can provide knowledge and information on optimized measures to meet management objectives and can better reflect the idea of active safety control, which is of great significance to construction site safety management. This dynamic evaluation provides appropriate safety measures for the optimization plan to support construction risk management in site work activities. To some extent, appropriate measures have been taken to control the risk factors before safety pre-warning to enhance safety performance. From the perspective of management, risk can be well controlled at the level of risk factors. According to the research results, potential construction risks can be gradually released and controlled by the safety measures of the dynamic optimized construction technical plan during the main structure construction.

For the practical application, the research outcomes can support the safety risk management stage by providing an innovative and automatic method of safety measure decision-making. Compared to existing studies [11][12], the multi-objective restriction in the safety risk management was considered in this research. Multiobjective optimization was applied to model and solve the dynamic, fuzzy, and multi-factor problems in safety risk management for deep excavations. Under the integration of the special plan management data and real-time monitoring data within the construction site information system, the hybrid model proposed in this research can support the generation and optimization of safety measures. In this process, the synchronization of data-driven engineering and physical information was utilized. That is, with the intelligent "physical system-digital plan" management scheme, the integration of the special plan management data and real-time monitoring data under the construction site information system can be utilized to determine the optimal safety measure set. Combined with existing semantic systems and platforms on risk management [13][14], the research outcomes can be used for enhancing the automatic safety risk management in deep excavation.

# 7 Conclusions and future work 

Considering the potential of digital twin technology in construction risk management, this research aims to develop a real-world-oriented simulation based on cyber-physical synchronicity for safety risk management in deep excavation. A hybrid safety measure optimization approach based on integrating Bayesian network (BN) and design structure matrix (DSM) was proposed in this research, by which the prediction, optimization, and control of the safety risk situation in actual construction procedures can be supported. By synchronously updating

and analyzing the dynamic risk situation on sites, the proposed approach can facilitate the identification of optimal safety measures to achieve safety management objectives, considering the minimal impact on cost and duration. In practice, managers can employ the recommended safety measures to make optimal decisions during the implementation of construction projects. Under the dynamic safety measure solution, the anti-risk ability of potential risks and the entire safety performance of the targeted project can be effectively improved.

Although the research method and outcomes could bring benefits to the safety management of deep excavation on sites, some research limitations still exist. First, except for the dynamic risk situation, construction cost, and duration, other factors (e.g., the feasibility and contextual features of the construction site) which may affect the safety measures decision-making were ignored in this research. For supporting a more comprehensive decision-making of safety measures in practice, the aforementioned factors should be considered at the same time in future studies. Second, the multi-objective optimization model proposed in this research mainly focused on one single critical risk event at one time. In fact, it is suggested that the optimal solution should be decided considering the overall risk situation on construction sites. In addition, safety management is closely related to the application of measures. Especially, for improving safety risk management, the development of a comprehensive method to verify the effectiveness of implemented measures is required in future work. Future research can focus on the above three aspects to promote the safety management of dynamic deep excavation operations. Last, as a dynamic and complex engineering information management activity, this research integrated the concept of digital twin technology to enhance decision-making for safety measures. The generation and optimization of the "physical system-digital plan" management scheme under the digital twin technology was expressed. Based on the research results, the semantic expression of special plans can provide the theoretical and empirical support for the dynamic safety risk management of construction sites. However, further exploration is required in the construction of a digital twin model for physical information systems, as well as the corresponding synchronization application and visual expression.

# Appendix 

The cloud platform of metro construction management established in this research is shown in Fig. 6. The interface in Fig. 6 expresses the results of the anti-risk ability of collapse after safety measure application.
![img-5.jpeg](img-5.jpeg)

# Acknowledgments 

This work was supported by the "National Natural Science Foundation of China (NNSFC)" under Grant number 71901104 and Qinglan Project of Jiangsu Province of China. Special thanks to all our participants involved in this research.
