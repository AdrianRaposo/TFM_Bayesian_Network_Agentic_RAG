# LJMU Research Online 

Loughney, S, Wang, J and Matellini, DB

Utilising Bayesian networks to demonstrate the potential consequences of a fuel gas release from an offshore gas-driven turbine
http://researchonline.ljmu.ac.uk/id/eprint/9972/

## Article

Citation (please note it is advisable to refer to the publisher's version if you intend to cite from this work)

Loughney, S, Wang, J and Matellini, DB (2018) Utilising Bayesian networks to demonstrate the potential consequences of a fuel gas release from an offshore gas-driven turbine. Proceedings of the Institution of Mechanical Enaineers. Part M: Journal of Enaineering for the Maritime Environment.

LJMU has developed LJMU Research Online for users to access the research output of the University more effectively. Copyright © and Moral Rights for the papers on this site are retained by the individual authors and/or other copyright owners. Users may download and/or print one copy of any article(s) in LJMU Research Online to facilitate their private study or for non-commercial research. You may not engage in further distribution of the material or use it for any profit-making activities or any commercial gain.

The version presented here may differ from the published version or from the version of the record. Please see the repository URL above for details on accessing the published version and note that access may require a subscription.

For more information please contact researchonline@ljmu.ac.uk

# Utilising Bayesian Networks to demonstrate the potential consequences of a fuel gas release from an offshore gas driven turbine 

S. Loughney, J. Wang, D. B. Matellini<br>Liverpool John Moores University, UK


#### Abstract

This research proposes the application of Bayesian Networks in conducting quantitative risk assessment of the integrity of an offshore gas driven turbine, used for electrical power generation. The focus of the research is centred on the potential release of fuel gas from a turbine and the potential consequences that follow said release, such as: fire, explosion and damage to equipment within the electrical generation module. The Bayesian Network demonstrates the interactions of potential initial events \& failures, hazards, barriers and consequences involved in a fuel gas release. This model allows for quantitative analysis to demonstrate partial verification of the model. The verification of the model is demonstrated in a series of test cases and through sensitivity analysis. Test case [1] demonstrates the effects of individual and combined control system failures within the fuel gas release model; [2] demonstrates the effects of the $100 \%$ probability of a gas release on the BN model, along with the effect of the gas detection system not functioning; [3] demonstrates the effects of inserting evidence as a consequence and observing the effects on prior nodes.


Keywords: Offshore safety, Bayesian networks, offshore installations, electrical generation systems, asset integrity.

## 1 Introduction

This research focuses on the development of a Bayesian Network (BN) model for modelling control system and physical failures of a gas turbine utilised in offshore electrical generation. The intention is to model a sequence of events following several component failures, under certain conditions and assumptions. These initial failures are defined in two categories: control system failures and physical or structural failures (1) (2) (3) (4). This should provide a base with which to expand the BN model to facilitate the requirement of having a dynamic risk assessment model that allows for accurate representation of the hazards and consequences associated with gas turbine fuel gas releases.

The research presented within this paper is an expansion of previous research conducted for an electrical generation system of an offshore installation. The initial research focused on creating a dynamic risk assessment model for an electrical generation system, based upon one initial component failure in the form of a Rotor Retaining ring failure. The dynamic risk assessment model is for application in an Asset Integrity Case. An Asset Integrity Case will enable the user to determine the impact of deficiencies in asset integrity on the potential loss of life and demonstrate that integrity is being managed to ensure safe operations. The Asset Integrity Case is, in principle, an extended Safety Case (5). From the initial research conducted by Loughney \& Wang (2017) (5) a sequence of events and a BN were produced to demonstrate the cause and effect relationships between the safety critical elements of the generator. The BN demonstrated a number of potential consequences, such as: Gas Import Riser failure, High Pressure Gas Flare Drum failure and Fuel Gas Release \& fire. These final consequences were not expanded or demonstrated in great detail to keep the complexity of the model as low as possible while achieving valid results (3) (4) (6) (7). The model to be presented here is an expansion of the previous model, focused on the consequence Fuel Gas release and Fire. In (5) fuel gas release and its consequences were represented as one node in the network. This research expands on this by constructing a new network to demonstrate the consequence of a gas turbine Fuel Gas release in much more detail (5) (8).

The overall aim of the research is to investigate how a dynamic risk assessment model for gas turbine fuel gas release can be developed to facilitate safety assessment for the duty holder, the regulatory body and other various parties involved in the oil and gas industry. A key part of the study is that it is the development of a logical and consistent risk assessment model, by applying Bayesian Network techniques to sequence of events based upon several initiating failures within a gas turbine. Furthermore, there is also the possibility of expanding the methodology and BN applications in (5) and this study to other areas and industries, as well as in conjunction with other techniques. For Example, Yan, F. et al. apply Bayesian network-bow-tie (BN-bowtie) analysis, proposed by mapping bow-tie analysis into Bayesian network (BN) for Analysis of gas leaks during biomass gasification (9).

This paper produces a brief literature review for a background into the research (Section 2), outlines a failure scenario on an offshore installation (Section 3), develops a BN model related to the outlined problem as well as data issues (Section 4), provides verification of the model through test cases and a sensitivity analysis (Section 5), and finally presents a brief conclusion (Section 6).

# 2 Background 

Gas turbines are used for a variety of purposes on offshore installations, such as: power generation, compression pumping and water injection, most often in remote locations. Gas turbines are most commonly duel fuelled, they have the ability to run on fuel taken from the production process under normal operations, known as fuel gas. They can also run on diesel fuel in emergency circumstances. Typically, offshore gas turbines operate from 1 to 50 MW and may well be modified from aero-engines or industrial engines. The most often used gas turbines are aeroderivative, particularly for the gas generator. It is known that relatively little information is contained within safety cases regarding the operation and safety of gas turbines (1) (10) (11). What is contained is the turbine model type, manufacture, ISO power rating (in Mega Watts (MW)), the fuel types and the location of the turbine shown on the respective installation's drawings. Additional information can be found on occasion, such as: text regarding the power generation package or back-up generators. However, information in reference to integrity management and maintenance can be very limited (10). This information, or lack of, provides sound reasoning to produce dynamic risk assessment models regarding the integrity and safety of gas turbines.

Industrial power plants are critical systems on board offshore platforms as they supply electrical power to safety critical systems, such as: refrigeration systems, HVAC (Heating, Ventilation and Air Conditioning), detection systems and fire suppression systems. These safety critical systems not only provide safe working for crew and other personnel, they also protect the integrity of the offshore platforms systems and structures. All of this protection stems from power supplied by the electrical generation systems, which is why offshore platforms and marine vessels ensure that they have back-up generators in the event that one or two generators fail to operate (11). Usually, on offshore platforms, there are three electrical generation systems, with two in the same module and the third in a separate module on a higher level which usually acts as the emergency generator. Despite the safety precautions behind the number of generators and their locations, there is still the possibility of all generators failing to operate (2).

Furthermore, in recent years there has been a marked increase in fires associated with fuel gas leaks with offshore gas turbines. A detailed review of offshore gas turbines incidents conducted in 2005 showed that there were 307 hazardous events over 13-year period, from 1991 to 2004. The review concerned itself with over 550 gas turbine machines. The analysis concluded that

the majority of incidents (approximately $40 \%$ ) occurred during normal operations, with approximately $20 \%$ during start-up, another $20 \%$ during or after maintenance, $10 \%$ occur during fuel changeover and the remaining $10 \%$ (approximately) occur during other operations. With the majority of incidents occurring during normal operations, the fuel gas detection is heavily reliant on either turbine fuel detectors and/or fire and gas system detectors. This is due to the modules containing the electrical power generators being almost totally unmanned during normal operation. Similarly, based upon the review conducted on gas turbines from 1991 to 2004, approximately $22 \%$ of gas leaks remained undetected. Subsequently, $60 \%$ of those undetected leaks were found to have ignited (10) (12).

It is situations such as those described that increase the requirement for a dynamic risk assessment model to accurately monitor the consequences of failures within gas driven generators as they are critical in the survival of crew members as well as the integrity of the respective offshore installation.

# 3 Fuel Gas Release Model 

This research does not set to outline the fundamentals of BN theory or give the BN methodology in detail. The methodology presented in the research by (5) is applied to construct this BN model. The model representing the potential for fuel gas release from an offshore gas turbine, along with the further consequences of fire and explosion, begins at the point of several initiating events. These events are the beginning of the sequence of events and continue through the point of potential gas release, the barriers involved in preventing the release and the potential consequences should these barriers fail.

### 3.1 Assumptions and Limitations

There are some underlying assumptions and limitations within the model that must be explained for the model to be valid and understood. These limitations are split into two groups: space \& domain limitations and model data limitations (4) (6) (13) (14).

### 3.1.1 Space and Domain Limitations

The purpose of the model is to show the effects that several component failures have on gas turbine integrity which can lead to a fuel gas release. Hence, the consequences of said fuel release are analysed, and in order to do this, the boundaries of the model need to be defined. These boundaries are concerned with the affected area, the detail of the consequences and the

ignition types \& sources. The outlined assumptions and limitations concerned with the model domain are as follows:

- The model has been built for the situation where the offshore platform contains no crew and hence does not consider fatalities. There are two key reasons for this; the first is that the BN model is formulated for a NUI (Normally Unattended Installation) Integrity Case, where humans are not present on the platform for large periods of time and are monitored from other platforms or onshore. Secondly, the BN is part of continual development of an Integrity Case which shall focus on maintaining the integrity of the equipment as a priority, as well as the effects of incidents on the environment. Hence fatalities are not part of the BN model consequences (8).
- The model is designed to demonstrate the hazards and consequences associated with the fuel gas release from an offshore gas turbine. Hence, the consequences regarding fire and explosion are not concerned with the probability of other hydrocarbon releases contributing to fires and explosions.
- The scope of the model is primarily within the power generation module of a large fixed offshore platform. Therefore, the section of the model assigned to the probability of equipment damage due to fire and explosion is confined to the equipment and machinery located only within the stated module.
- The node "Sensor and Instrumentation Failure" denotes failures within the components and equipment which are responsible for the key parameters of the gas turbine. These parameters include; Fuel flow, pressure, speed, temperature and vibration.
- The model is representative of fuel gas being released into the module and not within the gas turbine itself. This is due to the fact that should there be a gas release within the turbine, it is assumed that the combustion chamber is of sufficient temperature to ignite the fuel. However, the presence of an ignition source within the confines of the module is not a total certainty. The node "Ignition Source" represents this uncertainty and the possibility of an ignition source being present externally of the gas turbine and within the module.
- While the level of consequence is confined to the module, and the presence of an ignition source is not certain, it is still possible for the gas concentration to reach dangerous levels. These dangerous levels do not represent a direct threat to human personnel as it has been stated that humans are not present in the module. The dangerous levels relate to the potential environmental impact of harmful substances being released into the atmosphere. This is in

conjunction with the revised requirement of safety cases for offshore installations to contain precautions for potential environmental impact of offshore incidents and accidents (15).

# 3.1.2 Model Data Limitations 

It is important that some remarks are made regarding the uniformity of the data within the model. Statistics exist in a number of formats and originate from many sources. When formulating a model as specific and confined as the one being created, it is almost impossible to gather data sets from the same consistent sources. There are some differences in terms of data relating to the type of installation operating the same type of gas turbine generator. However, the location of the installations is restricted to the UKCS (United Kingdom Continental Shelf) and the North Sea. Much of the data represented in the model is adapted from gas turbines operating on fixed platforms, yet it is not feasible to obtain data from all sources relating to fixed installations. This limitation with the data relates to either the absence of data or the lack of appropriate data recording. Hence, data is from fixed installations and FPSOs (Floating, Production, Storage and Offloading) which make use of very similar gas turbine machines (16) (17).

There are also differences regarding the age of the data and the data sources used in the Fuel Gas Release model. All data utilised is taken from sources post 2002, with the majority of the data close to 2002 has been obtained from OREDA-2002 (Offshore Reliability Data) as full access to the database at this time was available (18). On the other hand, most of the conditional data used to complete the Conditional Probability Tables (CPTs) for the nodes, in the BN, has come from risk assessment projects conducted on offshore installation for gas turbines, with the main focus of the projects being hydrocarbon and fuel gas release. Such information can be found in (12) (19) (20) (21) (22).

Finally, most of the nodes are based upon hard evidence statistics, while two of the nodes incorporate subjective judgement by utilising a symmetric algorithm from hard evidence. By combining information in this way, it allows for situations where there is little to no data to be overcome. This process does not compromise the verification and analysis of the model; however, it is important to take note of this when interpreting the information presented in the results.

The BN model for a potential fuel gas release is demonstrated by Figure 1. The graphical structure of the model is designed to keep the nodes that fall under the same group together and organised in a "top down" manner. The five root nodes and the inference node are close

together at the top. The categorised nodes are next in the top down sequence. Continuing from the failures there is a potential incident ("Gas Release in Module"), which then leads to the barrier nodes. Pending the probability of success or failure of the barriers there is potentially another incident ("Continuous Gas Release"). Following from the barriers there are further incidents, accidents and consequence nodes which are systematically introduced. One node does remain slightly anomalous from this organisation. The root node "Ignition Source" is grouped along with the incidents, accidents and consequences as it directly affects one of the incidents.
![img-0.jpeg](img-0.jpeg)

Figure 1: BN model demonstrating the cause and effect of a potential fuel gas leak from a gas driven electrical generation system.

Furthermore, there are certain parameters that have been excluded from the model. These parameters have been excluded to prevent the model from becoming overly complex. An example of one such parameter is the level ventilation in the offshore module and the subsequent gas dispersion. This issue of ventilation and dispersion would bring in further parameters such as: automated ventilation systems, i.e. HVAC (Heating Ventilation and Air Conditioning) and natural ventilation and dispersion, i.e. varying types of weather (wind and rain) (10) (12) (23).

These parameters would allow the model to be much more intricate and complete. However, there are many specific parameters that are time based or rely on further specific parameters which exponentially increases the complexity of the model. This in turn can hinder the accuracy of the model due to the large amount of subjective data required. Hence, the initial nodes identified for the BN (nodes $1,2,3,4,5$ and the inference node) are all internal failures within the gas turbine that can be measured accurately, in terms of their reliability and integrity. Despite these additional parameters not being included, the integrity of the BN model is not compromised, as the scope of the model is still valid.

# 4 Data for the Fuel Gas Release Model 

The BN model for fuel gas release has been kept as simple as possible while still maintaining a coherent, accurate and logical pathway from the initial root nodes to the final consequences. This level of complexity has allowed CPTs to be manageable when it comes to gathering data. While the majority of the connections in the model are simple converging and diverging connections, consisting mostly of two arc connections in each connection type, there are two nodes which are the result of triple converging connections (13) (14) (24). In terms of the size of the CPTs, this is not a huge issue. However, due to the subject of these nodes ("Control System Failure" and "Physical/Structural Failures") there is little to no hard data available to complete their CPTs. It is possible to compile data for the rest of the nodes based upon current literature, databases (primarily for the root nodes) and actual risk assessment project data.

As it is not possible to utilise hard data sources to complete the CPTs of nodes 6 and 7 ("Control System Failures" and "Physical/Structural Failures") while still maintaining a high degree of accuracy, other techniques must be used. In this case a variation of the Symmetric Method (demonstrated in (5)) is applied to the CPTs of nodes 6 and 7.

# 4.1 Establishing the Conditional Probabilities 

When constructing a BN the prior probabilities are required to be assigned locally to the probability link, $P\left(\operatorname{Parent}\left(A_{i}\right)\right) \rightarrow P\left(\operatorname{Child}\left(B_{i}\right)\right)$, as a conditional probability, $P\left(B_{i} \mid A_{i}\right)$, where $i$ represents the $i$ th state of the parent node and the child node. However, it is not always a straightforward process to obtain the relevant data. In principle, the majority of the data can be acquired through failure databases or experimentation. However, designing and conducting experiments can prove difficult and historical data does not always satisfy the scope of certain nodes and CPTs within a BN. Therefore, in practice, it is necessary to rely on subjective probabilities provided by expert judgement as an expression of an individual's degree of belief. However, since subjective probabilities are based on informed judgements, it is possible for deviation to occur when the data is expressed as precise numbers (25) (13).

It can be seen in (5) that a fully subjective approach has been applied to construct certain CPTs in the BN. This involved experts providing their judgement through a Pairwise Comparison (PC) method. The data from the PC is further analysed using Analytical Hierarchy Process (AHP) and relative importance weights were determined from this for each parent node in question. These weights are then applied to an algorithm that allows a large child CPT to be constructed cell by cell. This method of compiling data for large CPTs proved simple to implement and produced accurate results for the BN. However, it was found that a timeconsuming part was the gathering of data from domain experts through PC in questionnaires.

Therefore, the data gathering process was amended by utilising hard data from risk assessment experimentation and historical data to determine relative weights of nodes as opposed to applying PC and AHP. This entails utilising hard data from the individual parent and child node relationships, to create relative weights for the parent nodes and apply those to the symmetric method algorithm.

### 4.2 Symmetric Method utilising hard data

The symmetric method provides an input algorithm which consists of a set of relative weights that quantify the relative strengths of the influences of the parent-nodes on the child-node, and a set of probability distributions the number of which grows only linearly, as opposed to exponentially, with the number of associated parent-nodes. Yet the most common method of gathering the required data for the algorithm is to use expert judgements. However, it is also possible to utilise the symmetric method with historic data and experimentation. While it is very difficult or not possible to complete a large CPT in a BN using hard data, it is possible to

obtain key conditional probabilities for a node. For example, node 6, the chance node representing "Control System Failure", has three parent nodes each with two states. This produces a parental distribution in the order of $2^{3}$. While this does not seem a large CPT, the nature of the node's scope limits the level of available data, and hence cannot be completed fully with hard data. However, it is possible to obtain key conditional probabilities and apply them to the symmetric method to complete the CPT.

The symmetric method in its entirety will not be outlined in this paper as this research is an expansion of research conducted in (5) and (24). The work by Loughney \& Wang (2017) and Das (2008) explains how the symmetric method assumes that the CPTs in the BN grow linearly not exponentially. Therefore, it is possible to produce a simple CPT for the child node where the effect of all parents is the identical. The symmetric method then applies these compatible child probabilities to a weighted sum algorithm. This algorithm applies a weight to each of the parent nodes and produces each individual conditional probability in the CPT by combining the compatible probabilities, given the state of the child node, and the relative weights of the parent nodes. The weighted sum algorithm is given in Equation 1.

$$
\begin{gathered}
P\left(D^{1} \mid A^{s_{1}}, B^{s_{2}}, \ldots, n^{s_{n}}\right)=\sum_{j=1}^{n} w_{j} \cdot P\left(D^{1} \mid\left\{\operatorname{Comp}\left(A=a^{S_{j}}\right)\right\}\right) \\
l=0,1, \ldots, m \quad S_{j}=1,2, \ldots, k_{j}
\end{gathered}
$$

Equation 1 demonstrates that the probability of event $D$, in state $l$, is given by the probability of the parents in the states $j$ of the set of states' $S$. In this algorithm the set of states, $S$, is vital as the set of states for each parent must be the same i.e.: "Yes" and "No". This conditional probability of $D^{l}$ is given by the sum of the product of the relative weights of each parent and each linear compatible parental configuration.

# 4.2.1 Calculating the relative weights 

Figure 2 demonstrates the situation in the BN of nodes 1, 2, 3 \& 6 with the notation $A, B, C \&$ $D$ respectively. While it is not possible to accurately obtain $P(D \mid A, B, C)$ or even $P(D \mid A, B)$ through historical or experimental data. It is possible to obtain the conditional probability of event $Z$ given the individual parents, i.e. $P(D \mid A), P(D \mid B)$ and $P(D \mid C)$. These conditional probabilities can be used to develop normalised weights for the parent nodes.

![img-1.jpeg](img-1.jpeg)

Figure 2: Sample BN representing 3 parents and 1 child

As mentioned previously, in the symmetric model the individual local conditional probabilities of the parent to child can be distributed by relative importance for the associated child node, i.e. the normalised weight. Hence, in normal space and using the notation outlined in Table 1, the probability of $D$ being of state "Yes" given that the probability of $A$ being in state "Yes" is equal to $\hat{X}_{A}$, where $\hat{X}_{A}$ is the relative importance of the parent node $A$. This is applied across all of the parent nodes and is demonstrated by Equation 4 (25).
$P\left(D=" Y e s " \mid A=" Y e s "\right)=P\left(\hat{X}_{A}\right)=\frac{P\left(X_{A}\right)}{\sum_{m=A}^{n} P\left(X_{m}\right)}$
$\ldots$
$P\left(D=" Y e s " \mid n=" Y e s "\right)=P\left(\hat{X}_{n}\right)=\frac{P\left(X_{n}\right)}{\sum_{m=A}^{n} P\left(X_{m}\right)}$
Therefore,
$\sum_{m=A}^{n} P\left(X_{m}\right)=P\left(X_{A}\right)+P\left(X_{B}\right)+\cdots+P\left(X_{n}\right)$

In normalised space, based on the influence of each parent node, the conditional probability of a binary child node $D$ given each binary parent node, $X_{r}$, where $r=A, B, \ldots, n$., can be estimated by Equation 5.
$P\left(D=" Y e s " \mid A=" Y e s "\right)=w_{1}$
$P\left(D=" Y e s " \mid B=" Y e s "\right)=w_{2}$

$P\left(D=" Y e s " \mid n=" Y e s "\right)=w_{n}$
$\sum_{r=1}^{n} w_{r}=w_{1}+w_{2}+\cdots+w_{n}=1$
Following from Equations 4 and 5, it is possible to calculate the weights of the parents given the individual parent to child conditional probabilities (25).

In order to demonstrate the calculation of relative weights for parent nodes, the section of the BN containing nodes 1, 2, 3, and 6, shown in Figure 1, shall be used as an example. Table 1 shows the local conditional probabilities for the child node "Control System Failure" given each individual parent node. These values were able to be determined from historical data (18). The notation outlined in Figure 2 is also applied for simplicity.

Table 1: Individual conditional probabilities for Control System Failure


The information presented in Table 2 can be represented as follows:
$P\left(D=" Y e s " \mid A=" Y e s "\right)=0.0584=P\left(X_{A}\right)$
$P\left(D=" Y e s " \mid B=" Y e s "\right)=0.0610=P\left(X_{B}\right)$
$P\left(D=" Y e s " \mid C=" Y e s "\right)=0.1330=P\left(X_{C}\right)$
$\sum_{m=A}^{n} P\left(X_{m}\right)=0.2524$
Hence, with the individual conditional probabilities, the relative weights of the parent nodes can be calculated utilising Equation 4.
$P\left(\hat{X}_{A}\right)=\frac{P\left(X_{A}\right)}{\sum_{m=A}^{n} P\left(X_{m}\right)}=\frac{0.0584}{0.2524}=0.2314=w_{1}$
$P\left(\hat{X}_{B}\right)=\frac{P\left(X_{B}\right)}{\sum_{m=A}^{n} P\left(X_{m}\right)}=\frac{0.0610}{0.2524}=0.2417=w_{2}$

$P\left(\hat{X}_{C}\right)=\frac{P\left(X_{C}\right)}{\sum_{m=A}^{n} P\left(X_{m}\right)}=\frac{0.1330}{0.2524}=0.5269=w_{3}$
Following from this, Equation 3 shows that the summation of the relative weights should be equal to 1 , as follows:
$\sum_{r=1}^{n} w_{r}=0.2314+0.2417+0.5269=1$
As the relative weights for parent nodes $A, B$ and $C$ have been calculated and assigned accordingly, they can be combined with the linear compatible parental configurations identified in Equations 1, 2 and 3. This combination forms the basis of the weighted sum algorithm, and from this the CPT can be calculated.

It is possible to apply the weighted sum algorithm, shown in Equation 1, as the following information has been identified:
i) The relative weights of the parent nodes $w_{1}, \ldots, w_{n}$, and,
ii) The $k_{l}+\ldots+k_{n}$ probability distributions over event $D$, of the linear type, for compatible parental configurations as shown in Table 2.

Table 2: Distribution over $D$ for Compatible Parental Configurations


The relative weight algorithm is applied to all cells within the relevant CPT to obtain the full conditional probability distribution. The completed CPTs for the BN Model can be found in Appendix A. Continuing on from the data acquisition and analysis process, it is possible to complete the BN by completing the CPTs and ascertaining the marginal probabilities for the nodes and conduct several test cases to validate the BN model. Table 3 summarises the origins of the data for each node in the initial BN model. There were several sources of literature. For example, node 10 was determined from historical data sources, such as OREDA and HSE databases, whilst, in comparison, data for node 17 is from (8) (16) (19) and (22).

Table 3 also contains the number of states for each node and the number of permutations to demonstrate an idea of how data had to be broken down before being inserted into the

corresponding CPT. Similarly, Figure 3 shows the marginal probabilities for each node in the BN.

Table 3: details of each nodes CPT and their data sources


${ }^{1}$ DB: Data has been utilised form Failure Databases, such as OREDA and OGP.
${ }^{2} \mathrm{HD}$ : Data has been utilised from Historical Data in literature, such as; Journals and HSE reports.
${ }^{3}$ RA: Data has been utilised from Risk Assessment projects conducted by companies such as: RMRI Plc., Maersk, and Lloyd's Register.

![img-2.jpeg](img-2.jpeg)

Figure 3: Marginal probabilities for each node within the Fuel Gas Release BN

# 5 Fuel Gas Release Model Test Cases and Sensitivity Analysis 

Case studies are important for demonstrating how research can be put into practice. The Fuel Gas Release model is now used to analyse a series of possible real-world scenarios. The variable from the external BN, i.e. the transfer node "Fuel Gas Feed Impact", is to remain unchanged and only those directly linked to the study for Fuel Gas Release shall be altered using the Hugin software. The Hugin software allows for evidence to be inserted to all nodes within the network in its "Run Mode" function. This evidence is to the degree of $100 \%$ in a

given state of a node. It is the posterior probabilities that are of interest and are computed given particular evidence of specific nodes.

The focus of the BN model is on the effects of the initial failures on the likelihood of a gas release, as well as the performance of the barriers designed to mitigate against the escalation of a release to further, more severe incidents. Furthermore, the model analysis shall demonstrate the probability of possible consequences that may arise given that these barriers do not perform their required function. As well as the potential for further escalation given other external factors, such as, the presence of an ignition source. The model also allows for the comparison of combined effects of various, simultaneous failures and their combined effect on the probability of events. There are a number of test cases which shall demonstrate the effects of different scenarios on the potential of a gas release and the possibility of fire and/or explosions. Similarly, to add to the verification of the model through these test cases, the effect of initially observing a consequence, such as, a leak or an ignition, is demonstrated through the change in the probability of the prior nodes. This is a potential route to identifying the main unknown cause of a consequence.

It is important to note that before any evidence is inserted into the model, the probabilities of "Continuous Release $=$ Yes" and "Consequence $=Y$-Leak" are quite high. This is because they are directly affected by the "Gas Detection" node. Before evidence is inserted, the "Gas Detection" node shows a low probability of detection, and hence the model assumes a higher probability of a release. It can be seen in the test cases that once the probability of detection inadvertently increases because of the presence of fuel gas, the probability of a leak (demonstrated by the "Consequence" node) as a consequence reduces. The effects of the detection system failing are demonstrated in the test cases to ascertain the severity of the probability changes to the potential consequences.

The primary purpose of test case 1 is to demonstrate a degree of verification of the model by demonstrating that the behaviour of the probabilities is akin to a real-world scenario. Test case 2 shall demonstrate the effects, on the BN , of a barrier failure along with the presence of an ignition source. Furthermore, test case 3 shall demonstrate the effects on prior probabilities given evidence inserted in the consequence node. Finally, a sensitivity analysis shall provide further verification utilising the Parameter Sensitivity Wizard in the Hugin software.

# 5.1 Test Case 1: Control System and Physical/Structural Failures 

This case study demonstrates the effects of individual and combined control system failures within the fuel gas release model. This case study is split into four test cases: 1A) is a demonstration of the effects of control system failures on the network, 1B) is a demonstration of the control system failures with the presence of an ignition source, 1C) is a demonstration of the effects of Physical/Structural failures on the network, and 1D) is a demonstration of the effects of Physical/Structural failures on the network with the presence of an ignition source. In the analysis of all test cases, the process of "inserting evidence" stipulates that the state in question is assumed to have occurred. This means that the probability within the BN is set to $100 \%$.

### 5.1.1 Test Case 1A: Control System Failures without Ignition

In the context of the presented model, the probability of a fuel gas release from a gas turbine due to the turbines control system, is mostly dependent on three key events: "Exceeding System Capability" (ESC), "Sensor and Instrumentation Failure" (SIF) and "System Defects" (SD). These events can occur either individually or in conjunction with each other. The effect on the likelihood of a gas release is demonstrated along with the effects on the fuel shut off system, with the subsequent consequences also demonstrated. In this case the likelihood of a continuous fuel release is analysed as well as the probability of the "Consequence" node being in states "Y-Leak" and "None". It is not key to analyse the "Y-Ignition" state as this test case does not include the possibility of an ignition source.

The results are presented by means of a bar chart (Figure 4) which shows the probabilities of gas release, fuel shut off, continuous release, the consequences and the effect on the overall control system failure, on the y-axis. The x -axis shows which individual event is presumed to be occurring. From the results it is evident that a major system defect would have the greatest effect on the probability of the gas release, as shown by the increase in probability from $57.85 \%$ without evidence, to $69.5 \%$ when a potential system defect causes a failure. It can be seen that the effect of a system defect in the control system produces significant changes in the likelihood of there not being a consequence due to the increase in the probability in gas release. The key information to be taken is the significance in the change of posterior probability's given the evidence inserted. This method provides a basic sensitivity analysis along with probability interpretation. Furthermore, the likelihood of consequences and continuous release decreases with the inserted evidence in control system failures as it is assumed in the model that the gas detection system has no reason to not function correctly at this stage. Therefore, the increase

in the probability and level of gas release will increase the probability of gas detection and hence the probability that the fuel will be shut off. This is a scenario that would be expected in a real-world situation.
![img-3.jpeg](img-3.jpeg)

Figure 4: Effects of the turbine control system failures on the posterior probabilities of "Gas Release", "Fuel Shut Off", "Continuous Gas Release" and "Consequence: States: Y-Leak \& None"

# 5.1.2 Test Case 1B: Control System Failures with Ignition 

As stated in test case 1A, the probability of a fuel gas release from a gas turbine due to the turbines control system, is dependent on three key initial events: "Exceeding System Capability", "Sensor and Instrumentation Failure" and "System Defects". This test case expands upon the findings in case 1A by demonstrating the control system failures along with the presence of an Ignition Source (IS). This will illustrate the effect the initial failures has on the accident and consequence nodes. The results are again presented in a bar chart (Figure 5) which shows the probability of gas detection, immediate or delayed ignition, explosion, fire, the potential damage incurred and the overall consequences on the y-axis. The x -axis shows the nodes where evidence has been input. The first column in the table in Figure 5 shows the probability of there being no evidence inserted in the control system nodes but does indicate that there is an ignition source.

![img-4.jpeg](img-4.jpeg)

Figure 5: Effects of Turbine Control System failures, with an ignition source present, on the posterior probabilities of "Gas Detection", "Consequences", "Immediate/Delayed Ignition", "Explosion", "Fire" and "Damage due to Fire \& Explosion"

From the graph it can be seen that the probability of there being a gas release, given any of the initial failures, is the same as test case 1A despite there being an ignition source present. This provides some verification to the model as it indicates that the nodes, "Ignition Source" and "Gas Release" should be, and are, independent from each other. Furthermore, as with test case 1A, the initial event "System Defects" demonstrates the largest effects on the model. It can also be seen that the probability of gas detection increases proportionally to the probability of gas release. This affects the relationship between the probability of detection and the probability of accidents and consequence. For example, in the event that there is only an ignition source present the probability of there being either fire or an explosion increases from $0.0113 \%$ to $13.56 \%$ and $0.0187 \%$ to $22.51 \%$ respectively (for marginal probabilities refer to Figure 3). This shows how the significant the presence of an ignition source is to the probability of fire and explosion before any other evidence is inserted. Continually, when evidence is then inserted into the "System Defects" node, the posterior probabilities for fire and explosion decrease from $13.56 \%$ to $12.12 \%$ and $22.51 \%$ to $20.12 \%$. This is because the probability of the gas detection increases with the probability of the gas release, as it is assumed that the gas detectors function as expected. Furthermore, this in turn has an effect on the fuel gas shut off by increasing the probability that fuel gas will be shut off. Hence the probability that a fire or explosion will occur decreases.

# 5.1.3 Test Case 1C: Physical/Structural Failures without Ignition 

Test cases 1C and 1D are similar to the previous cases, 1A and 1B, in that they demonstrate the effects of initial failures on the BN model both with and without an ignition source present. However, test cases 1C and 1D are concerned with the effects that physical and structural failures potentially have on the BN model. It is important to specify that the analysis in the Hugin BN software is applied to only discrete chance nodes and therefore the inference node "Fuel Gas Feed Impact" is not included in the analysis. Figure 6 shows the effects of the individual initial events, "Structural Support Failure" (SSF) and "Corrosion" (Cor.), on the posterior probabilities of gas release, fuel shut off, continuous release, the consequences (states " $Y$-leak" and "None") and the effect on the overall physical failure, on the y-axis. The x-axis shows the individual event which is assumed to be occurring.

From the graph in Figure 6 it can be seen that of the two events, represented as chance nodes, corrosion demonstrates the largest effect on a potential fuel gas release. It is evident that a failure caused by corrosion would have the greatest effect on the probability of the gas release, as shown by the increase in probability from $57.85 \%$ without evidence, to $70.01 \%$ when corrosion potentially causes a failure. Similarly, a failure caused by corrosion also produces the largest percentage change in the likelihood that a consequence will not occur. The effects
![img-5.jpeg](img-5.jpeg)

Figure 6: Effects of the physical and structural failures on the posterior probabilities of "Gas Release", "Fuel Shut Off", "Continuous Gas Release" and "Consequence; States: Y-Leak \& None"

that a failure, due to corrosion, has on the posterior probabilities in the model also represents the largest percentage change out of the five initial events.

As with the previous test cases, the probability of there being a leak consequence and continuous gas release decreases with the insertion of evidence at the root nodes, due to the probability of a release being detected given an increase in the probability that a release will occur. Furthermore, as with test case 1A the key information be taken is the significance in the change of posterior probability's given the evidence inserted. This method provides a basic sensitivity analysis along with probability interpretation, as well as verification to the BN model.

# 5.1.4 Test Case 1D: Physical/Structural Failures with Ignition 

As stated in test case 1C, the probability of a fuel gas release from a gas turbine due to the physical and structural failures, is dependent on key initial events: "Structural Support Failures", and "Corrosion". This test case expands upon the findings in test case 1C by again demonstrating the individual effects of the physical and structural failures along with the presence of an Ignition Source. This will illustrate the effect the initial failures has on the accident and consequence nodes. The results are again presented in a bar chart (Figure 7). This shows the probability of gas detection, immediate or delayed ignition, explosion, fire, the
![img-6.jpeg](img-6.jpeg)

Figure 7: Effects of Physical and Structural failures, with an ignition source present, on the posterior probabilities of "Gas Detection", "Consequences", "Immediate/Delayed Ignition", "Explosion", "Fire" and "Damage due to Fire \& Explosion"

potential damage incurred and the overall consequences on the y-axis. The x -axis shows the nodes where evidence has been input. The first column of the table in Figure 8 shows the probability of there being no evidence inserted in the control system nodes but does indicate that there is an ignition source.

From the graph it can be seen that the probability of there being a gas release, given any of the initial failures, is the same as test case 1 C despite there being an ignition source present. This again provides some partial verification to the model as it indicates the nodes that should be independent from each other, such as, "Ignition Source" and "Gas Release". This has previously been demonstrated in test case 1B. Furthermore, as with test case 1C, the initial event "Corrosion" demonstrates the largest effects on the model. It can also be seen, as with test case 1B, that the probability of gas detection increases proportionally to the probability of gas release. This affects the relationship between the probability of detection and the probability of accidents and consequence. In the event that there is only an ignition source present the probability of there being either fire or an explosion is identical to the percentage increase demonstrated in test case 1C, when only an ignition source is present.

When evidence is then inserted into the "Corrosion" node, the posterior probabilities for fire and explosion decrease from $13.56 \%$ to $12.06 \%$ and $22.51 \%$ to $20.01 \%$, respectively. This is because the probability of the gas detection increases with the probability of the gas release, as with test case 1B. The percentage changes demonstrated in Figure 6 and Figure 7 show that the event "Corrosion" has the greatest effect on posterior probabilities in the BN model of all of the initial events.

Test cases 1A, 1B, 1C and 1D demonstrate the cause and effect relationship that the five initial events have on the posterior probabilities in the BN model. The sixth root node (node 8), "Ignition Source", is also applied to the analysis to demonstrate the combined effects of the initial events with an ignition source present. This established some partial verification to the model as the posterior probabilities are increased and decreased as one would expect given evidence inserted at the root nodes. One key element demonstrated in the four test cases is that of the relationship between gas release and gas detection. As the probability of there being gas released increases, the probability of gas detection proportionally increases. This is because in a real scenario, it is assumed that when gas is present in the offshore module, the gas detectors would sense it and hence the gas would be shut off, either by the Turbine Control System (TCS) or the Fire \& Gas system (F\&G). This, as demonstrated by the test cases, decreases the

probability of an accident or severe consequences. However, it is important to demonstrate the effects a dysfunctional barrier, such as the gas detection system, has on the posterior probabilities of the BN model. Test case 2 outlines this type of scenario.

# 5.2 Test Case 2: Gas Release and No Detection with and without an Ignition Source 

This case study demonstrates the effects of the probability of a gas release being 100\% "Yes" on the BN model. Along with the gas release, the effect of the gas detection not functioning will also be analysed, i.e. Gas Detection being 100\% "No". Therefore, this case study is split into two test cases: 2 A ) is a demonstration of the effects of a gas release and no gas detection without an ignition source, and 2B) is a demonstration of the effects of no gas detection combined with an ignition source being present.

### 5.2.1 Test Case 2A: Gas Release - 100\% "Yes", Gas Detection 100\% "No", without an ignition source

In the context of the presented model, the probability of a fuel gas release from a gas turbine due to the turbines control system, is dependent on five key events: "Exceeding System Capability", "Sensor and Instrumentation Failure", "System Defects", "Structural Support Failure" and "Corrosion". In test case 2A is assumed that one or more of these events have occurred and a Gas Release (GR) is observed. In this case the likelihood of a continuous fuel release is analysed as well as the probability of the "Consequence" node being in states " $Y$ Leak" and "None". It is not key to analyse the " $Y$-Ignition" state as this test case does not include the possibility of an ignition source. The analysis is presented in Figure 8.

From the graph in Figure 8 it can be seen that when there is $100 \%$ chance of a fuel gas release, the probability of gas detection increases from $43.4 \%$ to $74.87 \%$. This is due to the assumption that the gas detection system functions as expected, i.e. in the event of a gas release it is assumed, with some confidence, that the gas detection system will detect the gas in the atmosphere and the fuel will be shut off. This is also demonstrated by the posterior probability of the three fuel shut off nodes: "TCS", "F\&G" and "Fuel Shut Off". Given a 100\% probability of a gas release and hence a $74.866 \%$ probability of gas detection, the posterior probabilities of the fuel being shut off is as follows: i) the probability of TCS shutting off fuel increases from $27.76 \%$ to $47.47 \%$, ii) the probability of F\&G system shutting off fuel increases from $20.37 \%$ to $34.7 \%$, and iii) the probability that the fuel will be shut off completely, increases from $35.39 \%$ to $60.19 \%$.

![img-7.jpeg](img-7.jpeg)

Figure 8: Effects of "Gas Release" being "Yes=100\%" and "Gas Detection" being "No=100\%" on "Consequences", "Continuous Gas Release", "Fuel Shut Off" (TCS, F\&G and Fuel Off) and "Gas Detection"

Similarly, the posterior probabilities of a continuous release and the consequence of a severe leak decrease from $58.81 \%$ to $29.26 \%$ and $64.56 \%$ to $39.78 \%$ respectively. This shows that the BN model can represent the behaviour of safety barriers in the event of a fuel gas leak. Furthermore, while the posterior probabilities of a consequence and continuous release still seem substantial, it is the significance of the change in probability that is of importance. These significant changes demonstrate that the barriers have a large effect on the mitigating of accidents and consequences regarding offshore systems. However, the importance of these barriers can also be demonstrated by assuming that they do not function or are simply not present.

From the graph in Figure 8 it can be seen that the right most column shows the posterior probabilities given that the "Gas Detection" (GD) has a $100 \%$ chance of failing or not functioning. The graph and data table show that in the event that there is a gas release and the gas detectors do not function then there is a very high probability of there being a gas leak as a consequence as well as a continuous leak from the system. The continuous leak would occur because the fuel shut off systems would not react to the gas detection. This effect can be seen in the posterior probabilities of the fuel shut off systems. In the event that gas detection is in state " $N o=100 \%$ ", then the resulting potential probabilities that the fuel will be shut off by either the TCS or the F\&G system are as follows: i) the probability that the TCS shuts off the fuel decreases from $27.76 \%$ to $0.58 \%$, ii) the probability that the F\&G system shuts off the fuel

decreases from $20.37 \%$ to $0.61 \%$, and iii) the probability that the fuel will be shut off by either or both systems decreases from $35.37 \%$ to $1.18 \%$. This illustrates the dependency that the fuel shut off systems have on the operational of the gas detection system. Furthermore, given a gas release and no gas detection, it can be seen that the probability of a continuous gas release increases from $58.81 \%$ to $99.57 \%$, and the probability of a gas leak as a consequence increases from $64.56 \%$ to $98.74 \%$. The significance of these percentage increases in the posterior probabilities indicates that the gas detection system is a vital barrier in the mitigation of accidents resulting from fuel gas releases.

However, this analysis considers only the repercussions of a fuel gas release without the possibility of an ignition source being present. In the event that there is a gas release and the gas detection system fails to operate as required, the fuel has a high probability to continue to be released and accumulate in the offshore module. This poses a huge issue should the gas release not be discovered by means other than the gas detection system. In the event that an ignition source is present, there is potential to cause a fire or an explosion. It is understood that should the gas be allowed to continuously release and accumulate, there is an ever increasing probability that an explosion will occur. Hence, it is vital that this scenario be analysed to show the potential, significant alterations to the occurrence probabilities of accidents and severe consequences. Test case 2B shall analyse the effects of an ignition source given that a fuel gas release is not detected.

# 5.2.2 Test Case 2B: Gas Detection 100\% "No" with an Ignition Source present 

As demonstrated in test case 2A, it is assumed that one or more events has led to a gas release being observed. In this case the likelihood of a continuous fuel release was analysed as well as the probability of the "Consequence" node being in states " $Y$-Leak" and "None". However, in this test case, the emphasis shall be on a gas release not being detected as well as the effects that an ignition source has on the posterior probabilities of several nodes. The nodes in question are: "Consequences" (States: "Y-Ignition" and "Y-Leak"), "Immediate/Delayed Ignition" (States: "Immediate" and "Delayed"), "Explosion", "Fire", "Damage due to Fire \& Explosion" and "Explosion Damage to Adjacent Areas". The effects of the analysis are to be analysed both as individual occurrences and a cumulative occurrence. Figure 9 shows the individual effects of No Gas release Detected (NGD) and the presence of an Ignition Source (IS).

The emphasis in this analysis is on the more severe accidents and consequences in terms of fire, explosion and the damage that they can cause. From the graph in Figure 9 it can be seen that

in the event of a $100 \%$ failure of the gas detection system, the probability of there being and accidents or consequences related to ignition remain virtually negligible. It can been seen that the probability of there being a gas leak as a consequence, however, increases from $64.56 \%$ to $98.74 \%$. This first stage of the test case demonstrates that the ignition related accidents and consequences have a very unlikely occurrence probability, according to the BN model, unless there are both a fuel source and an ignition source present.
![img-8.jpeg](img-8.jpeg)

Figure 9: Effects of "Gas Detection" being "No=100\%" and "Ignition Source" being "Yes=100\%" on "Consequences" (States "Y-Ignition" and "Y-Leak"), "Immediate/Delayed Ignition" (States "Immediate" and "Delayed"), "Explosion", "Fire", "Damage due to Fire \& Explosion"

The third column in Figure 9 demonstrates the effects on the fire \& explosion consequences given only an ignition source present, assuming that the probability of a gas release is at the marginal probability of $57.85 \%$. The purpose of this is to show how sensitive the fire \& explosion consequences are given an ignition source and a likely chance of a gas release. It can be seen that the posterior probabilities increase drastically when an ignition source is present. The probability that there will be a delayed ignition demonstrates the largest percentage change to the posterior probability as it increases from $0.03 \%$ to $44.67 \%$, with the probability of an immediate ignition increasing from $0.02 \%$ to $23.13 \%$. Furthermore, the second largest percentage change to the posterior probabilities is the likelihood of there being ignition as a consequence, as it increases from $0.02 \%$ to $29.34 \%$. Figure 9 also shows that the probability of

there being only a gas leak as a consequence decreases from $64.56 \%$ to $9.29 \%$ due to the increased probability of there being an immediate or delayed ignition.

The second stage of Test Case 2B is to demonstrate the cumulative effects of the fuel gas not being detected and the presence of an ignition source, as shown by Figure 10. It can be seen that the second column in Figure 10 that the probabilities are only the posterior probabilities given no gas detection. This is the same as Figure 9 where the percentage changes are demonstrated when an ignition source is also present. The third column shows the cumulative effects of a failed gas detector and an ignition source. The posterior probabilities display a very similar pattern to the posterior probabilities when there is only an ignition source present as shown in Figure 9. However, in this case (the cumulative effects) the posterior probabilities are much greater, i.e. the probability of there being an ignition as a consequence (" $Y$-Ignition") given an ignition source only is $29.34 \%$ when compared to the cumulative effects of NGD + IS which increases the probability to $44.88 \%$. This shows large percentage increases in the probabilities of potential ignition accidents and consequences. Furthermore, it is important to state that even though there is a gas detection failure and an ignition source present, the probability of there being an ignition accident or consequence is not $100 \%$. This is because the relationships between the nodes in the BN takes into account the fact that for an ignition to
![img-9.jpeg](img-9.jpeg)

Figure 10: Cumulative effects of "Gas Detection" being "No=100\%" and "Ignition Source" being "Yes=100\%" on "Consequences" (States "Y-Ignition" and "Y-Leak"), "Immediate/Delayed Ignition" (States "Immediate" and "Delayed"), "Explosion", "Fire", "Damage due to Fire

occur there must be an ideal air to fuel mixture. This ideal mixture is approximately $5-15 \%$ of fuel in the air (12). The data for the CPTs in the BN was analysed to compensate for the ideal mixture of oxygen to fuel.

# 5.2.3 Test Case 3: Effects of observed Consequences (Y-Leak and Y-Ignition) on prior probabilities 

In order to provide further verification of the BN model it is important to demonstrate the effects of inserting evidence as a consequence and observing the effects on prior nodes. The focus node in this test case is the "Consequence" node, with attention being focused on inserting $100 \%$ evidence to states " $Y$-Leak" and " $Y$-Ignition". The effect of $100 \%$ " $Y$-Leak" focuses on the changes in the probabilities of the gas release barriers and continuous release, whereas, $100 \%$ " $Y$-Ignition" focuses on the probability changes of the ignition, fire and explosion accident and consequence nodes. The " $Y$-Ignition" analysis does not focus on the barriers as the prior probabilities would be the same as the effects demonstrated by $100 \%$ " $Y$ Leak".

Figure 11 demonstrates the effects of $100 \%$ occurrence probability of the state " $Y$-Leak" on the prior probabilities of "Fuel Supply off", "TCS Fuel Shut off", "F\&G Fuel Shut off", "Continuous Gas Release" and "Gas Detection". The graph shows that given $100 \%$ probability of " $Y$-Leak", the prior probabilities concerned with the fuel shut off system nodes (TCS, F\&G and Fuel Supply off), all being in the state "Yes", greatly decrease to almost zero. Similarly, the probability of the gas being detected also decreases, but not to the extent of the three fuel
![img-10.jpeg](img-10.jpeg)

Figure 11: Effects of $100 \%$ "Y-Leak" on the prior probabilities of "Fuel Supply off", "TCS Fuel Shut off", "F\&G Fuel Shut off", "Continuous Gas Release" and "Gas Detection"

shut off nodes. In the event of a gas leak the most likely barrier to fail would be the F\&G shut off system as it demonstrates the lowest posterior probability of 0.03 . However, the barrier that displays the most significant change in probability is the gas detection system. Where the TCS and F\&G system show decreases of $27.76 \%$ to $0.1 \%$ and $20.38 \%$ to $0.03 \%$ respectively, and the gas detection system demonstrates a total decrease of $29.96 \%$ (from $43.4 \%$ to $13.44 \%$ ) This indicates that while the fuel shut off systems are the most likely barriers to fail in the event of a gas leak, the gas detection system demonstrates the most significant effect on a gas release. Finally, the probability of a continuous gas release increases $62.48 \%$ to $96.19 \%$. This significant increase is to be expected as there is a $100 \%$ probability of a leak. The probability of a continuous release is not $100 \%$ as there is a $13.44 \%$ chance that the gas may still be detected.

Figure 12 shows the effects on the prior probabilities of "Ignition Source", "Immediate/Delayed Ignition", "Fire" and "Explosion" given 100\% probability of the consequence state " $Y$-Ignition". The graph in Figure 12 indicates that prior to a $100 \%$ consequence of ignition, the likelihood of any ignition, fire and explosion accidents or consequences are almost negligible. However, when evidence is inserted into the state " $Y$ Ignition" in the consequence node, the prior probabilities greatly increase. The most obvious increase is the probability of an ignition source being present, which increases to $100 \%$. This is due to an ignition source being required along with the fuel gas in order to have an ignition take place. Continually, the probability of there being an immediate or a delayed ignition increases from $0.019 \%$ and $0.027 \%$ to $78.82 \%$ and $21.18 \%$ respectively. The immediate ignition is determined to be the more likely source of the ignition consequence as the delayed ignition is more dependent on the ideal mixture of fuel to oxygen. This is also reflected on the occurrence probabilities of a fire or explosion. As the probability of a delayed ignition is lower than that of an immediate ignition, the probability of a fuel gas fire is greater than the probability of an explosion. The probability of there being a fire increases from $0.011 \%$ to $31.69 \%$ when compared to the increase for an explosion, from $0.019 \%$ to $14.8 \%$. This shows that the accident type that contributes the most to the ignition consequence, given that there is a fuel gas ignition consequence, is a fuel gas fire.

![img-11.jpeg](img-11.jpeg)

Figure 12: Effects of 100\% "Y-Ignition" on the prior probabilities of "Ignition Source", "Immediate/Delayed Ignition", "Fire" and "Explosion"

# 5.3 Sensitivity Analysis 

Sensitivity Analysis (SA) is essentially a measure of how responsive or sensitive the output of the model is when subject to variations from its inputs. Having the understanding of how a model responds to changes in its parameters is important when trying to maximise its potential and ensuring correct use of the model. SA provides a degree of confidence that the BN model has been built correctly and is working as intended. In the context of this research, SA will be used as a demonstration to determine how responsive an event node is to variations in other nodes. Knowing the most influential nodes can assist in the experimentation and further expansion of the model. Similarly, nodes which have very little influence can be altered or discarded (5) (26).

The SA conducted for the fuel gas release model focuses on the node "Consequences", more specifically, its state " $Y$-Leak" and the nodes representing the barriers for fuel gas release. However, the analysis will be conducted using smaller increases and decreases in the probabilities of the parent nodes as opposed to inserting $100 \%$ occurrence probability into the input node CPTs, as demonstrates in test cases 1, 2 and 3.

While it is possible to conduct a sensitivity analysis by manually altering the input probabilities to observe and record the magnitude of change in the output probabilities, it can be time consuming and result in human error regarding the alteration of data. Hence, in this analysis, the parameter sensitivity wizard in the Hugin software has been utilised to produce a sensitivity analysis. In this program wizard the input node is individually paired with the output node in

its desired state. In this case that was "Consequence" in the state " $Y$-Leak". A state for each of the input nodes was purposely selected. The input nodes for the SA are the barrier nodes; "Gas Detection", "TCS Fuel Shut off", "F\&G System Fuel Shut off" and "Fuel Supply off". All nodes are set to state "Yes" in the parameter sensitivity wizard, with the exception of "Fuel Supply off" as this node is the child of "TCS Fuel Shut off" and "F\&G Fuel Shut off". Therefore, this node has been set to states "TCS: Yes, F\&G: No" and "TCS: No, F\&G: Yes". This allows for the sensitivity of this node to be determined given the output of its parent nodes. This method is also necessary as in the event both the parent nodes are in states "Yes" or "No", the probability of "Fuel Supply off" is either 1 or 0 and therefore cannot be analysed in the sensitivity parameter wizard in the Hugin Software. Following this a sensitivity value from Hugin was obtained for each input node, and using Microsoft Excel, a graph was constructed to show the results.

From the graph in Figure 13 it can be seen that the most influential factor on "Consequence: $Y$-Leak" is "Gas Detection", whilst the least influential is "Fuel Supply off: TCS=No, $F \& G=$ Yes". This concurs with the analysis as the node "F\&G System Shut off Fuel" has a smaller effect on the consequences than the node "TCS Shut off Fuel". Continually, if the probability of "Gas Detection: State - Yes" increases by $10 \%$, then the probability of "Consequence: State $-Y$-Leak" decreases by $4.6 \%$. If the probability of "Fuel Supply off: State - $T C S=N o, F \& G=$ Yes" increases by $10 \%$, then the probability of "Consequence: State $-Y$ -
![img-12.jpeg](img-12.jpeg)

Figure 13: Sensitivity Functions for the Input Nodes for Event "Consequence"

Leak" decreases by $0.8 \%$. From the graph it is also apparent that the sensitivity function is a straight line which further adds to the model verification. The sensitivity values computed within Hugin are shown in Table 4.

It is important to state that the sensitivity values are negative as they have a negative effect on the focus node "Consequence". In other words, as the probability of gas detection, for example, increases, then the probability that there will be a gas leak decreases.

Table 4: Sensitivity Values for the Input Nodes for Event "Consequence"


# 6 Conclusion 

This paper has outlined a Bayesian Network model which demonstrates the cause and effect relationships that several initial failures can have on an offshore electrical generation system. With particular attention being focused on the potential for a fuel gas release from the gas turbine which drives the electrical generation system. The research presented here progresses from the work presented by Loughney \& Wang (2017) (5), which illustrates the cause effect relationship of one component failure within an electrical generator and the general consequences that can result. The BN model presented in this research progresses from this research by incorporating part of the demonstrated BN model by Loughney \& Wang (2017) along with several other initial failures in order to analyse specific consequences in further detail. This consequence concerns itself with a possible fuel gas release and the potential fire and explosion hazards that can occur. However, while it is easier to demonstrate the effects of accidents involving fire and explosion, it is not easy to demonstrate the consequences of a leak without an ignition source. These consequences are equally important for offshore platform operators due to the improved HSE regulations within Safety Cases regarding hazards to the environment in any instance (15). Therefore, in the event that there is a fuel gas leak without ignition, it poses a large issue for operators and duty holders given that the release is undetected. While it is not as severe as a hydrocarbon release into the sea, it is still vital as it is the ejection of natural gas into the atmosphere which can result in consequences to the environment depending on the weather conditions.

In relation to the verification of the model a sensitivity analysis was carried out to determine how responsive the output of the model is to various modifications in the inputs and subsequently validate that the model works as expected. This exercise is vital as it provides an indication to what the most important variables. In addition, inputs can be ranked or weighted in terms of their importance upon the output or final consequences. The more advantageous element of conducting SA in BNs is that they take into consideration the chain of events below the input node leading to the output node, which presents a closer approximation to reality (5) (25) (26).

The BN model clearly demonstrates that it can provide an effective and applicable method of determining the likelihood of various events under uncertainty, and more importantly demonstrates its use as a dynamic risk assessment tool. Given the research presented it is now much clearer to see the advantages for BNs and Bayesian Theory being applied to create dynamic risk assessment tools to operate in conjunction with Safety Cases and other offshore installation regulations.

# Acknowledgements 

The author(s) disclosed receipt of the following financial support for the research, authorship, and/or publication of this article: This research was supported by Liverpool John Moores University and RMRI Plc. The authors also thank the EU for its financial support under European Commission funded projects RESET (2017-2020) and PRIGEOC (2016 - 2020).

## Declaration of Conflicting interests

The author(s) declared the following potential conflicts of interest with respect to the research, authorship, and/or publication of this article: This paper is the opinion of the authors and does not represent the belief and policy of their employers.

# Appendix A - CPTs for the BN model 


































Adjacent Areas |  |   |