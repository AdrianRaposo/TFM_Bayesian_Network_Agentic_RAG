# Risk Assessment of an Autonomous Underwater Snake Robot in Confined Operations 

Abdelrahman Sayed Sayed

## To cite this version:

Abdelrahman Sayed Sayed. Risk Assessment of an Autonomous Underwater Snake Robot in Confined Operations. OCEANS 2023 - Limerick, Jun 2023, Limerick, Ireland. pp.1-9, 10.1109/OCEANSLimerick52467.2023.10244516 . hal-04721094

## HAL Id: hal-04721094 <br> https://hal.science/hal-04721094v1

Submitted on 4 Oct 2024

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# Risk Assessment of an Autonomous Underwater Snake Robot in Confined Operations 

Abdelrahman Sayed Sayed


#### Abstract

The growing interest in ocean discovery imposes a need for inspection and intervention in confined and demanding environments. Eely's slender shape, in addition to its ability to change its body configurations, makes articulated underwater robots an adequate option for such environments. However, operation of Eely in such environments imposes demanding requirements on the system, as it must deal with uncertain and unstructured environments, extreme environmental conditions, and reduced navigational capabilities. This paper proposes a Bayesian approach to assess the risks of losing Eely during two mission scenarios. The goal of this work is to improve Eely's performance and the likelihood of mission success. Sensitivity analysis results are presented in order to demonstrate the causes having the highest impact on losing Eely.

Index Terms-Autonomous underwater vehicles, Bayesian Belief Network, Decision Network, Dynamic Bayesian Network, Eely, Risk Assessment


## I. INTRODUCTION

The growing interest in ocean discovery imposes a need for inspection and intervention in confined and demanding environments. Underwater confined environments, such as shipwrecks and sunken caves, present unique challenges for exploration. These environments often have limited access points and tight spaces, making it difficult for divers and underwater vehicles to enter and maneuver [1]. Autonomous underwater vehicles (AUVs) are considered to be efficient sensor-carrying platforms for seabed mapping and monitoring [2]. The likelihood of the underwater vehicles being lost while performing these missions can under certain circumstances be high, and some AUVs have been lost during missions due to technical failures [3].

Underwater snake robots, like Eely which is a snake robot from Eelume [4], [5] is a promising option for these environments due to their slender shape and ability to change body configurations. Eely's articulated structure shown in Figure 1 combines the advantages of several types of underwater vehicles, as it has the range of AUVs, the ability to access challenging areas like small Remotely operated underwater vehicles (ROVs), and the intervention capabilities of ROVs [6]. Thereby, Eely covers a broad range of operational scenarios as the vehicle can be configured to follow a torpedo-shaped AUV for platforming missions requiring the robot to map a big area [7] or to vary the joint's modules to follow snake

[^0]configuration to map confined or steep environments which can not be achieved by a normal AUV. However, operation of Eely in such environments imposes demanding requirements on the system, as it must deal with uncertain and unstructured environments, extreme environmental conditions, and reduced navigational capabilities [8].
![img-0.jpeg](img-0.jpeg)

Figure 1. Triple joint snake robot from Eelume
Bayesian networks (BNs) have been widely used to assess the risks associated with Autonomous Underwater Vehicles (AUVs) in operational scenarios, as demonstrated in previous studies [9]-[12]. However, there has been no prior work that has specifically addressed the risks associated with modular underwater snake robots operating in confined environments.

The main scientific contribution in this paper, we present a novel approach to risk assessment for Eely, an underwater snake robot, in confined environments operations. Our aim is to improve Eely's performance and increase the likelihood of mission success. Relevant data are collected to perform a quantitative risk analysis to develop a Bayesian model that considers almost the entire system of Eely, thus avoiding potential risks. We demonstrate that our Bayesian model can be extended to a Decision network (DN), enabling Eely to adapt its behavior autonomously and maximize mission utility [13]. Although our model was developed specifically for Eely, it can be transferred to the operations of other AUVs. To the best of our knowledge, the topic of risk associated with modular underwater snake robots has not been previously explored in existing research. Therefore, our study presents a state of the art contribution to the field of risk assessment of underwater vehicles.


[^0]:    Abdelrahman Sayed Sayed is with Department of Marine Technology, Norwegian University of Science and Technology (NTNU), Otto Nielsens veg 10, 7491 Trondheim, Norway; Université de Toulon, Toulon, France. abdelrahman.s.s.e.ibrahim@ntnu.no, abdelrahman-ibrahim@etud.univ-tln.fr

The paper is organized as follows: Section II presents the background on risk and Bayesian networks. In Section III, the application of the proposed BN risk model for the two case scenarios, including data collection for parameters for these models, dynamic simulation, and sensitivity analysis to identify the causes with the most significant influence on losing Eely. In Section IV the steps to extend the BN to a DN for autonomous risk-based decision making are presented. This is followed by Section V, which gives a brief discussion of the results. Finally, Section VI concludes this paper and presents suggestions for future work.

## II. RISK MODELING USING BNS

## A. Definition of Risk

The definition of risk related to a hazardous event $e_{i}$ [14] can be represented by the following relation:

$r=\left\{e_{i},c_{i},q\right\}|k$ (1)

where $c_{i}$ is the consequence of $e_{i}$, $q$ is the measure of involved uncertainty, and $k$ is the background knowledge for determining $e_{i}$, $c_{i}$ and $q$. This is the most commonly used definition for Bayesian risk modeling. By accounting for previous knowledge about the operational conditions and mission scenarios, events with low background knowledge would not have a strong effect when making a decision in contrast to events with high background knowledge. According to [15], risk assessment is an overall process including risk identification, risk analysis, and risk evaluation. Risk identification identifies and illustrates the possible risks with respect to the mission objective. A common approach for risk identification is to identify the known hazards as a source[s] of prospective harm. These hazards can be later analyzed in the risk analysis step, where the known possible events and their expected outcomes are modeled. Therefore, risk identification is an essential step towards developing a control system with risk management and decision-making capabilities for Eely which is known as supervisory risk control [16]. There are many of risk identification methods, such as hazard identification (HAZID) and preliminary hazard analysis (PHA). In order to have effective supervisory risk control, the most significant mission and operation hazards should be identified and combined into a risk model to aid in the system’s decisionmaking.

## B. Bayesian Networks

A Bayesian network is a graphical model used to address problems involving uncertainty [11], [12]. It describes the dependencies between random variables in a directed acyclic graph, where nodes stand for random variables and directed arcs between nodes signify conditional dependencies between them. The Bayesian network, which is based on probability theory [17], allows for two-way reasoning by handling both causal reasoning, which derives posterior probabilities from prior probabilities, and diagnostic reasoning, which uses a formula to derive prior probabilities from posterior probabilities. The traditional static Bayesian network (SBN) has limitations when it comes to evaluating variables that change over time, but it is useful for analyzing and forecasting data at a specific time. The dynamic Bayesian network was created to overcome this drawback. The dynamic Bayesian network (DBN) incorporates methods that take into account the relationship between moments in time, known as the state transition probability, in contrast to SBN [18]. By considering this relationship, the network can learn to effectively use changes in values over time, producing better results.

## III. CONSTRUCTION OF BAYESIAN RISK MODEL

In the context of risk assessment, Definition (1) may imply a Bayesian approach to probabilities, and hence the use of BN is a suitable approach to estimate the probability of losing Eely during different operational scenarios. HAZID was performed for the two case scenarios: i. Seabed mapping and ii. Confined environments operations in the form of a preliminary hazard analysis (PHA) prior to the development of the Bayesian risk model. Using the five-step method described in [13], the Bayesian risk model is developed.

## A. HAZID

HAZID aims to identify the hazards related to the operation of Eely for the two proposed case scenarios. Detectability is defined as Eely’s ability to detect and monitor a specific hazard during its operation, where a high degree of detectability suggests a strong background knowledge, while a low degree of detectability suggests a weak background knowledge. The collection of hazards was mainly based on [19] as it offered a comprehensive compilation of potential risks and served as the foundation for the identification procedure, along with our own judgment and similar systems [13]. In addition to, previous field trials with Eely in Trondheim Fjord [20] and previous experiments in karstic exploration [21]–[23] were also taken into account.

Table I, adopted from [13] which was used for hazards in the context of AUV operation under ice, the same criteria was selected and modified based on hazards related to Eely’s operation. Then, these hazards were assigned possible consequences depending on each case scenario, and the most noticeable hazards were identified. The risk priority number (rpm) for each hazard is obtained from the categories shown in Table I. The rpm is the product of the frequency rating, the consequence rating, and the detectability rating. To assess the risk, the worst-case scenario is assumed which is losing Eely. Note that this loss may be temporary, as in the case of seabed mapping and deploying a vessel may recover Eely [10], or it can be a permanent loss as in the case of underwater caves. Tables VII - VIII in the Appendix lists the hazards identified for the two case scenarios presented in the study. The assessment sheets design in the tables is based on the PHA sheet from [24].

Table I
Criteria used to rate Frequency, Consequences and Detectability of Events


Table II
FAILURE PROBABILITIES


critical is it in case of the failure of thruster module actuators as shown in red in any case of failure of thruster module actuators the probability of losing Eely is true as in confined environments the robot can't use its neutral buoyancy to float back to the surface. This is further illustrated in the sensitivity analysis subsection. Due to the limit on the number of pages, the CPTs for other nodes are omitted from this version of the paper. Moreover, thrusters were one of the most susceptible components to failure as Eely operators at the Applied Underwater Robotics Laboratory (AUR Lab) have communicated that they have lost on average one thruster per year.

## Table III

CPT FOR FAILURE OF PROPULSION SYSTEM


Table IV
CPT FOR ENVIRONMENTAL COMPLEXITY


## D. Launching the BN Model

After gathering the failure probabilities data, the BN model is constructed using the software GeNIe 4.0, which allows

Table V
CPT FOR REMOTE CONTROL


Table VI
CPT FOR LOSS OF EELY


interactive model building and learning, developed by Bayes Fusion company [33].

## E. Dynamic Simulation

Figure 2 shows one of the developed DBNs for the case of confined environments operations. The simulation results of the DBNs for the two case scenarios can be observed in Figures 3 - 4. The results indicate that the DBN can take into account changes over time and the likelihood of events occurring. In this regard, the probability of losing Eely in confined environments is higher than in seabed mapping due to various factors such as extreme pressures on the thrusters, poor communication with the vehicle, high mission complexity, and the complexity of the environment.

## F. Sensitivity Analysis

The goal of sensitivity analysis is to identify the causes that have the most significant impact on the probability of losing Eely, and to limit these causes by introducing risk reduction measures. It also works as an indicator for adding more constraints and efforts for data collection. Decreasing the uncertainty of a cause that has little or no influence on the probability of losing Eely will result in a negligible change in the overall uncertainty value, making it of little importance. In our case, we aim to identify the top factors that influence the probability of losing Eely. Figures 5 - 6 show the sensitivity analysis results for losing Eely for the two case scenarios.

In the first case of seabed mapping operations shown in Figure 5, it can be seen that the probability of losing Eely is most sensitive to the failure of autonomous control. Other main factors are comprised of failure of thruster module, failure of altitude control, mission complexity, and DVL failure. The
second case of sensitivity analysis is performed for confined environment operations and is shown in Figure 6. It can be seen that the failure of autonomous control is the most sensitive factor for losing Eely as well. Environmental complexity, failure of propulsion system, failure of altitude control, and mission complexity account for the remaining factors to which the loss of Eely is sensitive.

## G. Pros and Cons of the BN Model

The model looks upon almost Eely's entire system to avoid potential risks. Despite the fact that the model was built specifically for Eely, it can be transferred to the operations of other autonomous underwater vehicles. On the other hand, the model has some limitations, such as not including all of the possibilities with details which can cause the loss of Eely and not completely extending some nodes. For instance, nodes such as failure of communication system and failure of operator intervention, the latter being a non-technical node, could be further developed, and other non-trivial factors could have been included in the model. For such expansion, it would require searching for more data including human and organizational factors and their influence on mission risk, which would take a significant amount of time and resources, having the current model seem to be adequate for the two investigated case scenarios. Moreover, DBN is time dependent where the state of a variable at one time depends on its previous states and the states of other variables and it can be computationally expensive to compute more time steps, and GeNIe is only limited to 1000 time step [33].

## IV. RISK-BASED DECISION MAKING

Bayesian probability theory is used by both DNs and DBNs to represent uncertain relationships between variables. The main difference is that DNs do not take into account time dependence and provide a snapshot of the system at a specific moment. DNs are employed to simulate the relationship between choices and results when making decisions. In contrast, DBNs can also include decision-making only as part of a dynamic system that changes over time.

For decision-making, the novel approach presented in [13] can be followed, in which the HAZID results of Eely's operations can be used as a basis for constructing the BN model. The BN model can then be extended to a DN to autonomously adapt Eely's behavior with decision nodes, i.e., by adjusting the altitude set point, speed set point, and control strategy [7]. In our case, the maximum joint angle for dynamically changing the robot's shape can be adjusted based on its belief about the current state of the risk.

## A. Decision Nodes

The decision nodes that should be directly controlled by Eely are: altitude/depth set point, speed set point, the control strategy. In the articulated snake robot case, we can add one more node, "changing shape" based on mission category and

![img-1.jpeg](img-1.jpeg)

Figure 2. DBN for Losing Eely during Confined Environments Operations
![img-2.jpeg](img-2.jpeg)

Figure 3. Dynamic Simulation Results for Seabed Mapping Operations
![img-3.jpeg](img-3.jpeg)

Figure 4. Dynamic Simulation Results for Confined Environments Operations

![img-4.jpeg](img-4.jpeg)

Figure 5. Sensitivity tornado diagram for losing Eely during Seabed Mapping Operations
environmental constraints. Therefore, our decision nodes could be as follows:

- D1 $=a_{s}$ as the altitude set point
- D2 $=v_{s}$ as the speed set point
- D3 $=c_{s}$ as the control strategy
- D4 $=s_{c}$ as the desired/optimum shape configuration


## B. Online Reasoning

The DN continuously updates based on the sensory and temporal contexts. It is also important to include dwelling time based on the task to avoid rapid switching of states generated from sensor noise or in transient situations in-between state transitions. This can also help to avoid sensor outliers that bypassed the filtering process.

## C. Hard Coding Safety/contingency Handling

This will impose predefined safety protocols that override the suggested control actions from the DN and perform strictly defined actions, such as Eely's preexisting safety functions, like collision avoidance.

## V. Discussion

From the results of the DBN and senstivitity analysis, improving the robustness of the autonomous control part would significantly decrease the risk of losing Eely robot during different operations. Regarding the seabed mapping operations, from the sensitivity tornado graph in Figure 5 shows that improving the thruster module actuators and altitude control systems would also substantially reduce the risk of losing Eely. As for confined space operations, the sensitivity tornado graph in Figure 6 indicates that, except for environmental and mission complexity, improving the robustness of the thruster module actuators, propulsion system, and altitude control system would also significantly reduce the risk of losing Eely. The uncertainties associated with confined environments environmental complexity are reflected in the DBN in Figure 2 as they affect critical nodes, and in Tables VII - VIII as they are the main reason for a high $r p n$, mainly for DVL failure and Controller failure.
![img-5.jpeg](img-5.jpeg)

Figure 6. Sensitivity tornado diagram for losing Eely during Confined Environments Operations

## VI. CONCLUSION AND FUTURE WORK

In this paper, a BN model is developed for risk assessment of autonomous operations for Eely underwater snake robot. The model is populated with data to perform a specific quantitative probabilistic estimation of the loss of Eely during two challenging mission scenarios. The data is based on literature, PHA, and our own judgement based on similar systems. The results from the dynamic simulation and sensitivity analysis show that the highest risk of losing Eely was during confined environments operations, which is related to many factors, but the highest of them is the uncertainty of these environments compared to the other case scenario. In the future, this work can be build upon to include more mission scenarios. Also, implementing a behavior tree can allow for more complex mission scenarios and improve the modularity of Eely control systems [34] during different mission scenarios.

## ACKNOWLEDGMENT

I would like to thank my master thesis supervisors from NTNU, Ingrid B. Utne and Asgeir J. Sørensen, for their valuable inputs to this paper. Co-funded by the Erasmus Mundus Joint Master's Degree in Marine and maritime Intelligent Robotics (MIR) a Erasmus+ Programme of the European Union.

## APPENDIX

Table VII
RELEVANT HAZARDS FOR SEABED MAPPING OPERATIONS OF EELY


Table VIII
ReLeVANT HAZARDS FOR CONFINED ENVIRONMENTS OPERATIONS OF EELY
