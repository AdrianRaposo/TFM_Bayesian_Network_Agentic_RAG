# LJMU Research Online 

## Loughney, S and Wang, J

Bayesian network modelling of an offshore electrical generation system for applications within an asset integrity case for normally unattended offshore installations
http://researchonline.ljmu.ac.uk/id/eprint/7988/

## Article

Citation (please note it is advisable to refer to the publisher's version if you intend to cite from this work)

Loughney, S and Wang, J (2017) Bayesian network modelling of an offshore electrical generation system for applications within an asset integrity case for normally unattended offshore installations. Proceedings of the Institution of Mechanical Enqineers. Part M: Journal of Enaineering for the

LJMU has developed LJMU Research Online for users to access the research output of the University more effectively. Copyright © and Moral Rights for the papers on this site are retained by the individual authors and/or other copyright owners. Users may download and/or print one copy of any article(s) in LJMU Research Online to facilitate their private study or for non-commercial research. You may not engage in further distribution of the material or use it for any profit-making activities or any commercial gain.

The version presented here may differ from the published version or from the version of the record. Please see the repository URL above for details on accessing the published version and note that access may require a subscription.

For more information please contact researchonline@ljmu.ac.uk

# Bayesian network modelling of an offshore electrical generation system for applications within an asset integrity case for normally unattended offshore installations 

S. Loughney, J. Wang<br>Liverpool John Moores University, UK


#### Abstract

This paper proposes the initial stages of the application of Bayesian Networks in conducting quantitative risk assessment of the integrity of an offshore system. The main focus is the construction of a Bayesian Network (BN) model that demonstrates the interactions of multiple offshore safety critical elements to analyse asset integrity. The majority of the data required to complete the BN was gathered from various databases and past risk assessment experiments and projects. However, where data was incomplete or non-existent, expert judgement was applied through Pairwise Comparison, Analytical Hierarchy Process (AHP) and a Symmetric Method to fill these data gaps and to complete larger Conditional Probability Tables (CPTs). A NUI (Normally Unattended Installation) - Integrity Case will enable the user to determine the impact of deficiencies in asset integrity and demonstrate that integrity is being managed to ensure safe operations in situations whereby physical human to machine interaction is not occurring. The Integrity Case can be said to be dynamic as it shall be continually updated for an installation as the Quantitative Risk Analysis (QRA) data is recorded. This allows for the integrity of the various systems and components of an offshore installation to be continually monitored. The Bayesian network allows cause-effect relationships to be modelled through clear graphical representation. The model accommodates for continual updating of failure data.


Keywords: Offshore safety, Integrity case, Bayesian networks, Offshore installations, Electrical generation systems

## 1 INTRODUCTION

This research focuses on the development of an Initial Bayesian Network (BN) model for modelling system and component failures on a large offshore installation. The intention of the presented research is to model a sequence of events following a specific component failure, under certain conditions and assumptions. This sequence of events is then applied to a BN

model using a proposed methodology. This should provide a base with which to expand the BN model to facilitate the requirement of having a dynamic risk assessment model within an NUI (Normally Unattended Installation) - Integrity Case. The purpose of the BN model is to demonstrate that it is possible to accurately and sufficiently apply BN techniques to offshore systems and their associated failures and hazard. The aim of this is to apply Bayesian theory and BNs to the integrity case as the basis for modelling various other offshore systems and monitoring their integrity based upon the data and scenarios within the BN models.

An Asset Integrity Case will enable the user to determine the impact of deficiencies in asset integrity on the potential loss of life and demonstrate that integrity is being managed to ensure safe operations. The Integrity Case is an extended Safety Case. Where safety cases demonstrate that safety procedures are in place, the Integrity Case shall ensure that the safety procedures are properly implemented. The Integrity Case can be applicable to operations for any large scale asset, and in the case of this research the large asset for which the Integrity Case shall be developed is an offshore installation [1]. By expanding on this Integrity Case proposal, it is intended that an Integrity Case be developed for a Normally Unattended Installation (NUI) in conjunction with a dynamic risk assessment model to maintain a live representation of an offshore installations integrity. Furthermore, it is proposed that the NUI-Integrity Case be initially developed utilising a manned installation, but modelling failure and risks without human presence on board. This is due to a much larger range of failure data being available regarding manned installations as opposed to unmanned installations. Similarly, should a risk assessment model be feasible for various hazardous zones of an installation, and the dynamic model proves to be effective in the detection of failures and mapping of consequences, it may be possible to reduce the number of personnel on board manned offshore installations, to reduce the risk of injury and fatality.

The paper is structured as follows. Section 2 presents a literature review, outlining the background into the research. An outline of BNs and a proposed methodology of constructing a BN model is shown in section 3. Section 4 outlines and analyses a case study to demonstrate the proposed methodology. Section 5 summarizes the paper.

# 2 LITERATURE REVIEW 

### 2.1 Offshore Safety Assessment

Following the public inquiry into the Piper Alpha disaster, the responsibilities for offshore safety regulations were transferred from the Department of Energy to the Health and Safety

Commission (HSC) through the Health and Safety Executive (HSE) as the singular regulatory body for safety in the offshore industry [2] [3]. In response to this the HSE launched a review of all safety legislation and subsequently implemented changes. The propositions sought to replace the legislations that were seen as prescriptive to a more "goal setting" approach. Several regulations were produced, with the mainstay being the Health and Safety at Work Act [4]. Under this a draft of the offshore installations safety case regulations was produced. The regulations required the preparation of operational safety cases for all offshore installations, both fixed and mobile. In addition, new fixed platforms require a design safety case and in the case for mobile installations the duty holder is the owner [2].

Offshore operators must prepare acceptable operational safety cases (SC) for all existing and new offshore installations which is subject to approval based on an independent reputable organisation's verification, such as; DNV GL (Det Norske Veritas) (Germanischer Lloyd), for acceptance, and it is an offence to operate without an approved SC [5]. The SC must show that it identifies the hazards with potential to produce a serious accident and that these hazards are below a tolerability limit and have been reduced to the ALARP Level (As Low As Reasonably Practicable) [2].

Safety and risk assessment for offshore installations is vigorous and requires demonstration from duty holders that all hazards with potential to cause major accident are identified, all major risks have been evaluated, and measures have been or will be taken to control the major accident risks to ensure compliance with the statutory provisions [6].

This is vitally important as accidents in the offshore industry lead to devastating consequences, such as the explosion on board the Deepwater Horizon rig in the Gulf of Mexico which was caused by the failure of a subsea blowout preventer (BOP), with some failures thought to have occurred before the blowout. This solidifies the use of quantitative risk and reliability analysis, with recent emphasis on Bayesian networks, as the model can perform predictive analysis and diagnostic analysis [7].

In 1996 the regulations surrounding safety cases were expanded to include the verification of Safety Critical Elements (SCEs). In conjunction to this, further regulations were introduced, the so called offshore installations and wells regulations. These regulations dealt with the various stages of an installations life cycle. In terms of SCEs, they are defined by HSE (1996) as parts of an installation, including software programs, whose failure has the potential to cause

or contribute substantially to or whose purpose to prevent or limit effect of a major accident [2] [8].

Recently, however, it is felt that an expansion on Safety Cases is necessary, especially in the offshore and marine industry, as they are static documents that are produced at the inception of offshore installations and contains a structured argument demonstrating that the evidence contained therein is sufficient to show that the system is safe [9]. This is the full extent of Safety Cases. They involve very little updating unless an operational or facility change is made. It can be difficult to navigate through a safety case, as they can be difficult for project teams and regulators to understand, as well as often being monolithic [10]. This is where the e-Safety Case comes into play. e-Safety Cases are html web-based electronic Safety Cases. They are much easier to navigate and have clear concise information about the safety of the facility they are provided for. However, the QRA data (Quantified Risk Assessment) is only updated with the release of updated regulations [11]. Over the past 10 years it has been stated that a dynamic risk assessment model is required within the offshore and process industries. [12] proposed to apply BN to Bow-Tie (BT) analysis. They postulated that the addition of BN to BT would help to overcome the static limitations of BT and show that the combination could be a substantial dynamic risk assessment tool. Similarly, in the oil, gas \& process industry [13] proposed a methodology of Dynamic operational Risk Assessment (DORA). This starts from a conceptual framework design to mathematical modelling and to decision making based on cost-benefit analysis. Finally, [1] proposed the idea of a dynamic decision making tool in an Asset Integrity Case.

The Integrity Case, an idea proposed by RMRI Plc. (Risk Management Research Institute), can be said to be dynamic as it shall be continually updated with the QRA data for an installation as the QRA data is recorded. This allows for the integrity of the various systems and components of a large asset, such as an offshore installation, to be continually monitored. This continual updating of the asset's QRA data allows for the users to have a clearer understanding of the current status of an asset. The updating also allows a user to identify the impact of any deviation from specified performance standards, as well as facilitate more efficient identification of appropriate risk reduction measures. Finally, it identifies key trends within assets (e.g.: failures, failure modes), hence, reporting to regulators would improve greatly and it would provide a historical audit trail for the asset. Furthermore, the integrity of an asset is maintained so that potential loss of life is kept ALARP. This means that an asset may continue

safe operations under circumstances that may have instigated precautionary shutdown, resulting in considerable cost savings for the owner and operator [1].

# 2.2 BN Justification 

Improving offshore safety is a main objective for various offshore organisations such as the HSE and DNV GL. In order to help achieve this improvement in offshore safety risk assessment analysis models need to become more efficient and dynamic. Hence, in this research the development of a potential dynamic risk assessment model is presented, with a focus on specific failure on an offshore installation [14].

The risk of hazards and failures offshore is determined by a large range of factors due to the countless possible scenarios in which incidents and accidents can develop. This makes establishing risk both qualitatively and quantitatively an intimidating task. There are many techniques which can aid risk analysis, yet in this research the focus is to be around BNs, and a large number of studies have been conducted for marine, offshore and process industries. Most studies usually associate themselves around a particular area. For example BNs have been utilised by [7] to conduct quantitative risk assessment of operations in the offshore oil and gas industry. Their method involves translating a flow chart of operations into the BN directly. They then verify their model through the use of a case study involving Subsea Blowout Preventer Operations, in light of the Deepwater Horizon sinking in 2010, whose cause was the failure of the subsea blowout preventer [15]. In another instance [16] applied BN to produce a marine and offshore decision support tool to realistically deal with random uncertainties, while at the same time making risk assessments easier to build and to check [17]. Furthermore, [16] proposed, in their work, an offshore decision-support solution, through BN techniques, to demonstrate that it is necessary to model the assessment domain such that the probabilistic measure of each event becomes more reliable in light of new evidence being received. This is the preferred method as opposed to obtaining data incrementally, causing uncertainty from imperfect understanding and incomplete knowledge of the domain being analysed.

There are a multitude of positive by using BNs over alternate risk assessment methods, for example, in BNs various forms of data can be combined, such as; expert judgement and empirical data. This is particularly useful in situations where there is an absence of data or where data is very sparse. Thus other forms of data and information can be incorporated into the network [18]. The advantageous nature of BNs over other methods is outlined by [12], who investigated the exclusive nature of comparing BNs and Fault Tree Analysis (FTA) in safety

analysis within the process industry. It was concluded by them that a BN is a superior technique in safety analysis due to its flexible structure, which allows for it to fit a wide variety of accident scenarios. In conjunction to this, BNs provide a clear visual representation of what they are representing and can be a highly effective tool for generating ideas and expanding the model in itself [17]. This trait is shared by other risk modelling techniques, however, BNs are particularly adaptable method. BNs also facilitate inference and the ability to update predictions through the insertion of new evidence or observations into its parameters. This makes them a very useful tool when dealing with uncertainty.

The BN methodology provides a substantial way in which the modelling of relationships between variables, within a given domain, through the assignment and linking of nodes. The method also allows for clear graphical representation of a scenario resulting from a series of events. The uncertainty between multiple dependencies of nodes is captured through the assignment of conditional probabilities [19]. It is worth noting that BNs are not without their critics. Bayesianism is analysed by [20] and discussed some of the limitations of BNs. He addressed in particular that the Bayesian approach cannot combine conflicting beliefs that are based on different implicit conditions and cannot carry out inference when the premises are based on different implicit conditions [14]. In terms of the research presented in this work, the BN should be thought of as a probabilistic approach to risk analysis which considers factors and chains of potential events, which can result in an undesired situation or condition.

# 3 METHODOLOGY 

### 3.1 Overview of Bayseian Networks

BNs are a Directed Acyclic Graph (DAG) encoding Conditional Probability Distribution (CPD). There are two main components to BNs. The first is the graphical structure, which provides the qualitative part and the second is the probability distribution which provides the quantitative part [14].

The graphical structure is referred to as the DAG. The DAG contains a set of nodes each representing a random/chance variable which can take the form of an event, the presence of something, a measurable parameter, a latent variable and an unknown parameter or hypothesis. Nodes are connected together by arcs in one-way directions. Arcs can also be referred to as directed edges, and they represent the direct probabilistic dependence relationship between variables. A simple example of a BN is shown in Figure 1. In this example, nodes A and B are the parents of node C. Node C is the parent of nodes D and E and the child of A and B. Nodes

D and E are children of C. Following this logic, nodes $\mathrm{C}, \mathrm{D}$, and E are descendants of A and B. Nodes A and B are the root nodes, while nodes D and E are the leaf nodes [17] [18].
![img-0.jpeg](img-0.jpeg)

Figure 1: A simple BN
Each node in the DAG has a number of possible states which must apply at any one time. Probability distribution indicates the strength of the belief in how the states of parent nodes can affect the states of their child nodes. Nodes can represent either discrete random variables with a finite number of states, (e.g.: 'Yes/No' and 'Low/Medium/High') or they can represent a continuous random variable with a normal density distribution. For root nodes a marginal probability table is defined. Non-root nodes are assigned conditional probability tables (CPTs) (Neapolitan, 2004). If the node is discrete then each cell in the CPT contains a conditional probability for the state of the node given the state of the parent node or combination nodes. When constructing a BN it is important to note that the number of permutations in the CPTs increases exponentially with the number of parent nodes and the number of states in the CPT. For example; If node A has ' X ' parents with ' n ' number of states, then there will be ' Xn ' permutations in the CPT or node A. Similarly, the total number of cells in a CPT is equal to the product of the possible number of states in the node and the number of states in the parent nodes $[17]$.

Conditional probabilities are essential to BNs. They can be expressed by statements such as " $B$ occurs given that A has already occurred" and "given event $A$, the probability of event $B$ is ' $p$ ", which is denoted by $P(A \mid B)=p$. This specifically means that if event $A$ occurs and everything else is unrelated to event $B$ (except event $A$ ), then the probability of $B$ is ' $p$ ' [17]. Conditional probabilities are part of the joint probability of the intersection of $A$ and $B, P(A \cap B)$.

For any two events $A$ and $B$ :

$$
P(A \cap B)=P(B \mid A) \cdot P(B)=P(A \mid B) \cdot P(A)
$$

It should be noted that if $\mathrm{P}(\mathrm{A})=0$ then A is an event with no possible outcomes. Therefore, it follows that $(A \cap B)$ also contains no possible outcomes and $P(A \cap B)=0$. The independence of events can be shown by definition. Let $A$ and $B$ be any events with $P(A) \neq 0$. Then $A$ and $B$ can be defined as independent if $P(B)$ is equal to $P(B \mid A)$.

Thus, it follows from the previous definition, that:

$$
P(A \cap B)=P(A) \cdot P(B) \quad P(A \cap B)=P(A) \cdot P(B)
$$

Bayes Theorem of probability theory is seen as a way of understanding how the probability that a theory is true, is affected by new evidence. For example, the probability of $A$ can be updated if new evidence about event $B$ is known (Matellini, 2012).

$$
P(A \mid B)=(P(B \mid A) \cdot P(A)) / P(B)
$$

# 3.2 Modelling and Analysis Steps 

There are many step-by-step procedures in use that allow for construction of the various parts of the BN model. The procedures are useful as it allows for maintaining consistency throughout the process and offers an element of confidence to the model. The procedures have varying parts depending on the context of the model and how much information is already available [19] [21]. However, there are key elements which all the procedures follow, these are:

### 3.2.1 Establish the domain and project definition

This involves putting boundaries in place for the model. In this analysis the domain is to be defined as a module on a large offshore installation. The model begins with an initial component failure and tracks the cause and effect relationship of this failure on various other components and systems. The model ends with outlined consequences. The objective of the model involves stating what results are expected to be achieved from the model. For the model in this research the focus is on the interaction of the components and their probability of occurrence.

### 3.2.2 Identify the set of variables relative to the problem

This involves filtering possible parameters that are relevant to the description and objective. For the model the initial variables were devised utilising a sequence of events diagram. This sequence of events diagram represents the steps of various events with their order and causality.

The events in the diagram are connected with arcs and arrows. This allows for a straightforward transition to a BN.

# 3.2.3 Form Nodes and Arcs for the BN 

The events and consequences in the sequence of events are translated to corresponding parent and child nodes in the Bayesian Network. The sequence of events, however, is basic and the arcs do not directly translate to the BN and are determined in Step 4. It is possible to express node as positive or negative. The interconnections between the events is translated to the specific CPTs in question. The CPTs are constructed in Step 5. Once the relevant nodes are identified, they are input into a BN software package, HuginResearcher7.7, and connected. This entails referring to the sequence of events from the initial failure to determine the most effective way of connecting the nodes together. The network is reviewed to ensure that there are no missing factors.

### 3.2.4 Data acquisition and analysis

Primarily, data is sought from various sources including: industrial \& academic publications, offshore risk assessment projects, as well as databases such as: the Offshore Reliability Database (OREDA), the HSE and International Association Oil \& Gas Producers (OGP). However, should data not be widely available or the CPT for a node be much too large to construct utilising data from the outlined sources, then expert judgement is to be utilised. The expert judgement is to be obtained using the Pairwise Comparison technique and analysed with the Analytical Hierarchy Process (AHP). The data from the AHP analysis is translated to the CPTs using a Symmetric Method. The data from relevant sources is then used to create the marginal or conditional probability tables.

### 3.2.5 Analysis of BN model and Sensitivity Analysis

This step concerns itself with the analysis of the BN model using Bayesian Inference. The probability of failure given a specific operation is obtained by forward analysis. Hence, it is possible to determine the posterior probabilities of the influencing events through backward analysis, provided some evidence is entered into the nodes of the BN. The propagation of the BN is conducted using Hugin Researcher 7.7. The results of the analysis provide useful information in handling the effect of one failure on multiple components and systems. These results are demonstrated through a Sensitivity Analysis. The data for this analysis is again produced by the Hugin Researcher 7.7 software.

# 3.2.6 Verification of the BN Model 

Verification is a key aspect of the methodology as it provides a reasonable amount of confidence to the results of the model. In carrying out a full verification of the model, the parameters should be closely monitored for a given period of time. For modelling a specific failure within an electrical generator, this exercise is not practical. In current work and literature, there is a three axiom based verification procedure, which is used for partial verification of the proposed BN model. The three axioms to be satisfied are as follows [15]:

## Axiom $i$ :

A small increase or decrease in the prior probabilities of one or more parent nodes should produce a relative increase or decrease in the probability of one specific child node or a number of child nodes. The number of child nodes affected is dependent on the type of BN and the purpose of the analysis.

## Axiom ii:

Given the variation of probability distributions within a parent node, or more than one, the magnitude of the influence to the child node should remain consistent.

## Axiom iii:

The complete influence magnitudes of the arrangement of the variations in probability from " $x$ " attributes on the values should be larger than that of the set " $x-y$ " attributes.

## 4 CASE STUDY

### 4.1 Establish domain and model definition

In order to demonstrate the proposed methodology a case study is applied. The case study undertakes the evaluation of the effects that a rotor retaining ring failure has on an offshore electrical generation unit. The study takes into account systems within a module of a large offshore installation and the key surrounding systems.

The potential damage scenarios from the failure of the retaining rings shall be assessed for one electrical generator contained within a module of a platform, which has significant hydrocarbon inventories adjacent to either side of the module. Hence the potential for damage to key hydrocarbon systems is present and provides an ideal position to model the cause and effect relationship of a retaining ring failure across various systems.

The electrical generation unit is considered to be of a generic layout for electrical generation on a large platform. The generator consists of a primary alternator, driven by a gas turbine. Located after the alternator is the exciter. The alternator rotor and shaft are forged in one piece with the exciter coupled on to one end. The opposite end of the shaft is coupled to the turbine drive shaft, which has an approximate operating speed of $3,600 \mathrm{rpm}$. The main shaft is supported by two main bearings, housed in pedestals, on stools on the baseplate. One bearing is situated between the turbine and the alternator and the other between the alternator and the exciter. An electrical generation unit is illustrated by figure 2.

# 4.2 Identifying the set of variables relative to the problem 

The variables are identified following the failure of one specific component which, in this case, is a Rotor Retaining Ring. Should one of the retaining rings fail, the main shaft would become unbalanced causing potential fragmentation of the rings inside the alternator. Given the extreme tolerances' within the generator construction, the unbalanced shaft could also cause damage to other areas of the equipment, such as: the turbine blades and the exciter. Should the retaining ring fail within the alternator casing and fragment, debris would be created within the casing. Furthermore with the machine operating at approximately 3,600rpm, an out of balance shaft would cause substantial vibrations, which could cause the main bearings to fail. Should the bearings fail, causing the shaft to become misaligned, it would result in increased damage to the turbine, alternator and exciter [22].
![img-1.jpeg](img-1.jpeg)

Figure 2: Schematic of a Generator Unit

From this the most likely point of failure within the turbine is the turbine blades shearing. Multiple blade failure could lead to the turbine casing not fully containing the turbine blade debris. This would result in turbine blades being expelled through the turbine casing as high velocity projectiles. Continually, the violent shaft vibrations and misalignment could have a severe impact on the exciter and may result in the exciter, weighing approximately one tonne, becoming detached from the main shaft. Some catastrophic failures have resulted in the exciter breaking up and some have had the exciter remain mostly intact [22]. Should the bearings not fail, the alternator stator coils \& casing, can provide enough resistance and are substantial enough to prevent the debris from the retaining ring penetrating the alternator casing. However, it is possible for the fragments to be expelled axially towards either the turbine or the exciter or both [23].
![img-2.jpeg](img-2.jpeg)

Figure 3: Outline of a Sequence of Events Diagram.
In the event of one or two rotor retaining ring failures, significant damage could occur within the alternator casing and fragments of the retaining ring could be expelled axially. Should the ring debris be expelled, it is assumed that it will travel in two possible direction; i) towards the turbine or ii) towards the exciter and out of the casing. Should the debris travel to the turbine there is potential for the fragments to impact the fuel gas line within the turbine. This then provides the escalation to a fire (given the location of the potential release, ignition is assumed). Should the debris travel out of the casing towards the exciter, it is considered by RMRL Plc (2009) that while the axial velocity may be considerable, it is likely to be lower than the radial velocity that the debris would be expelled at, were the casing and stator not there. Therefore, while it is possible for the ring debris to penetrate the casing, they would not have the required

velocity to penetrate the module walls or deck. From this it is deemed that if retaining ring failure does not cause a bearing failure, then the consequence of the event is likely to be limited to the damages caused by the retaining ring [23].

However, should the main bearing fail, the potential consequences become much more severe. The significant damage caused by the bearing failure can potentially produce high velocity projectiles from the turbine blades being expelled and/or the exciter becoming detached [22]. In these events, there is potential for the projectiles to impact the hydrocarbon containment around the module.

The series of events stated can be expressed in a sequence of events, by applying the variables to a generic sequence of events diagram, as shown in Figure 3.

# 4.3 Form Nodes and Arcs for the BN 

The model is demonstrated in Figure 4 and is designed around the variables identified in the sequence of events shown in Figure 3 and Section 4.2, and is to represent the cause and effect of one initial component failure has on systems within the stated domain. The Initial BN model is not a direct representation of the sequence of events in terms of the section of the model where possible debris is expelled. Within the sequence of events if the debris is not expelled initially, it is assumed to remain in the alternator, yet if debris expelled, it is assumed to travel towards the exciter. Similarly, if the debris is not expelled to the exciter, it is assumed to be
![img-3.jpeg](img-3.jpeg)

Figure 4: BN model as constructed from the outlined variables.

expelled towards the turbine. While this is all possible, it is more realistic to assume that if the debris is created from the retaining ring failure, it has the potential travel to the turbine and the exciter in the same instance. However, it is possible for debris to be expelled to the exciter and not to the gas turbine, whereby some debris would remain in the alternator. The way in which the BN model is created ensures that it contains all relevant possible outcomes.

In this case the analysis is conducted within an electrical generation module of a large offshore installation. The initial model is made up of seventeen chance nodes labelled 1 to 10 and E1 to E7. The latter nodes represent the possible events that can result from the initial mechanical failure. All nodes have two states ("Yes" and "No") except for event node E6 which has four ("Small", "Medium", "Full-bore" and "None"). The BN constructed from the variables outlined is shown in Figure 4.
![img-4.jpeg](img-4.jpeg)

Figure 5: Marginalised Probabilities for each node in the BN model

# 4.4 Data acquisition and analysis 

It is important to note that the numerical results of the model are not significant in terms of being absolute, but rather to serve in the demonstration of the practicability of the model. Once a full set of verified data is fed into the model, the confidence level associated with planning and decision making under uncertainty will improve. Figure 5 complements Figure 4 by demonstrating the marginal probabilities for each node.

To complete the CPTs within the BN, certain data and knowledge is required regarding each specific node. For some nodes data is limited or not available. For cases where there is an absence of hard data, the CPTs are to be completed through subjective reasoning or the application of expert judgement. This process can be demonstrated by looking at the node "Event Escalation". This node represents the chance of escalation following key component failures. The parents of this node are as follows: "Turbine Blades Expelled", "Exciter Detaches", Gas Import Riser Piping Impact" and "HP Flare Drum Shell Impact". In order to put together an appropriate estimate, experts must judge the situation and provide their opinions. This data acquisition can be either qualitative or quantitative in nature. However, the child node "Event Escalation" has a CPT which is too large for an expert to simply fill with their own judgements and opinions. Therefore, an effective way to gather information, to fill these large CPTs, from experts is to apply the use of a Pairwise Comparison technique in questionnaires and make use of the Analytical Hierarchy Process (AHP) to analyse the results, combined with the symmetric method algorithm to fill the large CPTs [24].

The AHP will produce a weighting for each parent criterion in the pairwise comparison matrix. These weights are applied to the symmetric method which is utilised to fill large CPTs. The symmetric method provides an input algorithm which includes of a set of relative weights that quantify the strengths of the parent-nodes influence on the child-node, and a set of probability distributions. However, in the symmetric method the probability distribution is deemed not to grow exponentially but linearly, with the number of parent-nodes [25] [26]. Figure 5 shows the complete marginal probability distributions for the BN.

Table 1 shows each node in the BN along with the number of states, number of parents, permutations in the probability tables and the sources of data. In addition, the full CPTs for the BN can be found in Appendix 1.

Table 1: Details of each Nodes CPT along with their data origins


${ }^{1}$ Historical Data (HD), ${ }^{2}$ Databases (Db)such as; OREDA, HSE, OGP, ${ }^{3}$ Offshore Risk Assessment Projects, ${ }^{4}$ Pairwise Comparison, Analytical Hierarchy Process \& Symmetric Method

# 4.4.1.1 Pairwise Comparison and $A H P$ 

Pairwise comparison is required as the experts cannot simply analyse the individual nodes and provide their judgements. A specific criterion is required in order for the experts to understand the situation and provide the relevant information. Furthermore, the BN contains some nodes which are at component level and some nodes which are at system level. The pairwise comparison provides a hierarchy for comparisons so the experts can see the breakdown of the situation and compare areas that are system related and those that are component related [25].

The AHP approach is a structured technique for organising and analysing complex decisions. It is based on the well-defined mathematical structure of consistent matrices and their associated right eigenvector's ability to generate true or approximate weights [26] [27]. It enables the comparison of criteria with respect to a benchmark in a similar fashion to the pair-

wise comparison mode. Such a comparison uses a fundamental scale of absolute numbers. For example, in this analysis the scale is as follows: " 1 is equally important", " 3 is a little important", " 5 is important", " 7 is very important", " 9 is extremely important" and " $2,4,6$, and 8 are intermediate values of important". This fundamental scale has been shown to be a scale that captures individual preferences with respect to quantitative and qualitative attributes [28] [29].

A set of questionnaires, applying the fundamental scale for absolute numbers, was sent to selected experts in the offshore industry for their evaluation. The feedback is investigated according to their judgements on the criteria under discussion. This feedback, in the form of a pairwise comparison, is utilised to determine the relative weights of the parent nodes using AHP. The back grounds of the five experts, who shall remain anonymous, is as follows:

Expert 1 is a current member of a national regulatory body with over 20 years of experience in the offshore industry. This person current holds chartered engineer status.

Expert 2 is currently in the employment of a reputable classification society and holds a university qualification at the MSc. Level. This person has 8 years of experience at sea and more than 5 years as an offshore safety manager.

Expert 3 is currently in the employment of a reputable classification society and holds a university degree at PhD level. This person has more than 10 years' experience of working in the offshore industry.

Experts 4 and 5 are both currently colleagues in the employment of a leading energy corporation and have university degrees to MSc. Level. Both also have more than 10 years' experience in the offshore industry.

To find the relative weight of each criterion, an AHP approach containing a pair-wise comparison matrix will be used. To conduct the pairwise comparison matrix, at first, set up $n$ criteria in the row and column of an $n \times n$ matrix.

The judgements on pairs of attributes $A_{i}$ and $A_{j}$ are represented by an $n \times n$ matrix $A$ as shown in (Eq. 4) [30],

$$
A=\left(a_{i j}\right)=\left[\begin{array}{cccc}
1 & a_{12} & \ldots & a_{1 n} \\
a / a_{12} & 1 & \ldots & a_{2 n} \\
1 / a_{1 n} & 1 / a_{2 n} & \ldots & 1
\end{array}\right]
$$

where $i, j=1,2,3, \ldots, n$ and each $a_{i j}$ is the relative importance of attribute $A_{i}$ to attribute $A_{j}$.
For a matrix of order $n,(n \times(n-1) / 2)$ comparisons are required. According to Ahmed et al. (2005), each element in the pair-wise comparison matrix carries a weight vector which indicates their priority in terms of its overall contribution to the decision making process. These weight values are found using (Eq. 5).

$$
w_{k}=\frac{1}{n} \sum_{j=1}^{n}\left(\frac{a_{k j}}{\sum_{i=1}^{n} a_{i j}}\right)(k=1,2,3, \ldots, n)
$$

where $a_{i j}$ is the entry of row $i$ and column $j$ in the comparison matrix of order $n$.
The weight values obtained in the pair-wise comparison matrix are checked for consistency purpose using a Consistency Ratio $(C R)$. The $C R$ value is computed using the following equations [26]:

$$
\begin{aligned}
C R & =C I / R I \\
C I & =\frac{\lambda_{\max }-n}{n-1} \\
\lambda_{\max } & =\frac{\sum_{j=1}^{n} \frac{\sum_{k=1}^{n} w_{k} a_{j k}}{w_{j}}}{n}
\end{aligned}
$$

where $n$ equals the number of items being compared, $\lambda_{\max }$ stands for maximum weight value of the $n \times n \mathrm{n} \times \mathrm{n}$ comparison matrix, $R I$ stands for average random index (Table 2) and $C I$ stands for consistency index [26] [31].
$C R$ is designed so that a value greater than 0.10 illustrates an inconsistency in the pairwise comparison. If the Consistency Ratio is 0.10 or less, then the pair-wise comparison is considered consistent and reasonable. Should the inconsistency level in the pairwise comparison be unacceptably high, a revisit to the expert judgements would be required. It is also possible to approach more domain experts in the elicitation process [26].

Table 2: Saaty's Random Index (RI) Values


# 4.4.1.2 Symmetric Method 

The symmetric method is an ideal solution to compiling data for large CPTs, as it simplifies the problem.

To outline the symmetry method, let us consider part of the initial BN model consisting of nodes 7, 8, 9, 10 and E5. as shown in Figure 6.
![img-5.jpeg](img-5.jpeg)

Figure 6: Small BN Network taken from the Initial BN Model

Also, for ease of explanation, Table 3 shows a simple notation for each parent node.
Table 3: Notation for Parent Nodes in Figure 6


In this example the child node E5 has $2^{4}$ different parental configurations, as there are four parents each with two states (Yes and No). Hence, the CPT will consist of $2^{4}$ probability distributions. This large number of distributions would require a substantial level of effort on the part of the expert to complete the CPT to an acceptable degree of accuracy. The more enigmatic part is that the CPTs are exponentially large. A CPT dependent on $n$ parents with two states would require distributions of the order $2^{n}$ to be deemed to be functional. The exponential growth provides the key issue behind compiling large CPTs. This symmetry method simplifies the problem of exponentially large CPTs.

For calculation of the CPT for the child node (Event E5), assume that the number of distributions grows linearly as opposed to exponentially. i.e.: with the network shown there are $2 \times 4$ distributions linearly as opposed to $2^{4}$ exponentially. If the states of the parents are assumed to have one-to-one capability correspondence (which is an equivalence relation) then the number of 'Questions' regarding the CPT for the child node is reduced [32].

The parent nodes, $\mathrm{W}, \mathrm{X}, \mathrm{Y}$ and Z , in this instance, have the same number of states; $k_{1}=k_{2}$ $=\ldots=k_{4},=k$.

Suppose: $Y=y^{t}$ is compatible with $W=w^{t}$, for $1 \leq t \leq k$.
$Y=y^{t}$ is not compatible with $W=w^{s}$ whenever $t \neq s$ where $t$ and $s$ are the sets of $n$ elements of the parents.

Let $\left\{\operatorname{comp}\left(Y=y^{s}\right)\right\}$ denote the Compatible Parent Configuration where parent $Y$ is in the state $y^{s}$ and the rest of the parents are in states compatible to $Y=y^{s}$

Therefore, using the symbol ' $=$ ' to relate two identical sets, one has;

$$
\begin{gathered}
\left\{\operatorname{comp}\left(Y=y^{s}\right)\right\} \equiv\left\{\operatorname{comp}\left(W=w^{s}\right)\right\} \equiv\left\{\operatorname{comp}\left(X=x^{s}\right)\right\} \equiv\left\{\operatorname{comp}\left(Z=z^{s}\right)\right\} \equiv \\
\left\{W=w^{s}, X=x^{s}, Y=y^{s}, Z=z^{s}\right\}
\end{gathered}
$$

Consider the network shown in Figure 6 where the $2 \times 4$ linear probability distribution has been assigned. Starting with parent $W$ and interpreting the compatible parent configurations as follows in equation 10 (Das, 2008):

$$
\begin{gathered}
\{\operatorname{comp}(W=s)\} \equiv\{\operatorname{comp}(X=s)\} \equiv\{\operatorname{comp}(Y=s)\} \equiv \\
\{\operatorname{comp}(Z=s)\} \equiv\{W=s, X=s, Y=s, Z=s\}
\end{gathered}
$$

where the set contains two states. $s=$ Yes, No
Hence the probability distribution over the child node $E$ will be:

$$
\begin{gathered}
P(E 5 \mid\{\operatorname{comp}(W=s)\})=P(E 5 \mid\{\operatorname{comp}(X=s)\})= \\
P(E 5 \mid\{\operatorname{comp}(Y=s)\})=P(E 5 \mid\{\operatorname{comp}(Z=s)\})
\end{gathered}
$$

where the set contains two states. $s=$ Yes, No
However, all parental configurations, regardless of their compatibility, are needed to complete the required CPT probability distribution. This primes requirement for relative weights. The relative weights established from the AHP results are applied to the algorithm here (Das, 2008).

Given the network in Figure 6 it is possible to assign the relative weights $\left(w_{1}, \ldots, w_{4}\right)$, calculated in Equation 5 (Eq. 5), to the parents $W, X, Y, Z$ respectively, to quantify the relative strengths of their influences on child node E5.

The weights should be positive and normalised, i.e.: $0 \leq \mathrm{w}_{\mathrm{i}} \leq 1$, for $i=1, \ldots, n$, and $w_{1}+\ldots$ $+w_{4}=1$.

Once the key information is determined, i.e.: the relative weights $w_{1}, \ldots, w_{4}$, and, the $k_{1}+\ldots$ $+k_{4}$ probability distributions over E5, of the linear type, for compatible parental configurations. Then the weighted sum algorithm can be used to produce an estimate, based upon expert judgements, of the $k_{1} \times \ldots \times k_{4}$ distribution for child node E5 [32].

$$
P\left(x^{l} \mid y_{1}^{S_{1}}, y_{2}^{S_{2}}, \ldots, y_{n}^{S_{n}}\right)=\sum_{j=1}^{n} w_{j} \cdot P\left(x^{l} \mid\left\{\operatorname{Comp}\left(Y_{j}=y_{j}^{S_{j}}\right)\right\}\right)
$$

where: $l=0,1, \ldots, m$ and $S_{j}=1,2, \ldots, k_{j}$.
This weighted sum algorithm is applied to the distribution over E5 for compatible parental configurations. Table 4 shows the compatible distributions over child node E5, with data obtained from expert judgement through pairwise comparison and AHP.

Table 4: Distribution over E5 for Compatible Parental Configurations $\{\operatorname{Comp}(\mathrm{W}=\mathrm{s})\}$


In addition, Table 5 shows the relative weights for the parents of event E5, which were obtained from expert judgment through pair-wise comparison and AHP.

Table 5: Relative Weights of Parent Nodes of Event E5


Utilising the data shown in Table 4 and Table 5, it is possible to calculate all of the $2^{4}$ parental distributions required to populate the CPT for event E5. Consider an example to demonstrate the algorithm for a specific parental distribution, where the probability of $\mathrm{E} 5=$ Yes is required. One possible distribution is shown in Table 6.

Table 6: Possible Parental Configuration for Parents of Event E5


Given the states of the parents in Table 6, the distribution over E5 is to be:

$$
P(E 5=\text { Yes } \mid W=\text { No }, X=\text { Yes }, Y=\text { No }, Z=\text { Yes })
$$

Once all of the relevant data is known, according to Equation 4-9, the following computation is required:

$$
\begin{aligned}
& P(E 5=\text { Yes } \mid W=\text { No }, X=\text { Yes }, Y=\text { No }, Z=\text { Yes })=w_{1} \cdot P(E=\text { Yes } \mid\{\text { comp }(W=\text { No })\}) \\
& +w_{2} \cdot P(E=\text { Yes } \mid\{\text { comp }(X=\text { Yes })\})+w_{3} \cdot P(E=\text { Yes } \mid\{\text { comp }(Y=\text { No })\}) \\
& +w_{4} \cdot P(E=\text { Yes } \mid\{\text { comp }(Z=\text { Yes })\})
\end{aligned}
$$

From Equation (Eq. 17) is can be deduced that for the parental configuration shown in Table 6 , when the correct compatible probabilities and weights are substituted in, the probability of event E5 being in the state "Yes" is to be:

$$
P(E 5=\text { Yes } \mid W=\text { No }, X=\text { Yes }, Y=\text { No }, Z=\text { Yes })=0.6
$$

Subsequently, according to Axiom 2 shown in Section 3.2.6, the complement of (Eq. 16) $[\mathrm{P}(E 5=N o)]$ is to be:

$$
\begin{gathered}
P(E 5=N o \mid W=N o, X=\text { Yes }, Y=N o, Z=\text { Yes })= \\
1-P(E 5=\text { Yes } \mid W=N o, X=\text { Yes }, Y=N o, Z=\text { Yes })=0.4
\end{gathered}
$$

The relative weight algorithm is applied to all cells within the relevant CPT table to obtain the full conditional probability distribution. This process was completed using the formula function in Microsoft Excel, which also saves time for calculations.

At first, the symmetric method may seem a slightly excessive method for compiling a CPT of this size when compared to Noisy-OR or the ranked node method. However, when compiling

large CPTs it becomes very efficient without becoming more complex. This method is being utilised at this stage of the modelling as similar adaptations of the symmetric method are to be used in further BN models to demonstrate the methods effectiveness with both subjective and hard data.

# 4.5 Results and Disscussions 

### 4.5.1 Analysis of BN model and Sensitivity Analysis

Quantitative analysis is carried out on a specific section of the Initial BN model, shown in Figure 7, concerning the event "E5. Event Escalation" and its parents.
![img-6.jpeg](img-6.jpeg)

Figure 7: A) Specific Section of BN to be analysed. B) Prior Probabilities for Event E5 and its Parent Nodes.

### 4.5.1.1 Quantitative Analysis

This analysis involved systematically inserting evidence into each of the parent nodes and finally the child node. In addition, nodes 7 and 8 have a parent node "Generator Bearings" which has no evidence inserted, and there is no evidence inserted anywhere else within the model. However, in this section of the BN model nodes 7 and 8 are parents of nodes 9 and 10 respectively, and therefore will alter the posterior probabilities of these nodes when evidence is inserted. This relationship has been left in the analysis to give an accurate representation of the posterior probabilities of the event E5, which is the focus node in this analysis.

The scenario shown in Figure 8 illustrates the gas turbine blades being expelled as projectiles from the generator housing. This increases the probability of the events escalating from $25.19 \%$ to $35.09 \%$. This increase would involve some concern as a potential escalation from this is the impact of the turbine blades on the Gas Import Riser. This can also be seen in Figure 8 where the probability of there being a gas import riser impact increases from $6.2 \%$ to $25 \%$.
![img-7.jpeg](img-7.jpeg)

Figure 8: Probability of "Event Escalation" given Turbine Blades are Expelled

Furthermore, as shown in Figure 9, the expulsion of the turbine blades coupled with a gas riser impact, increases the probability of there being event escalation from $35.09 \%$ to $61.42 \%$. This is a very large increase as the impact of a gas riser is the largest threat to escalation, due to the loss of containment of the gas, this hypothesis was also confirmed by expert opinion. It can also be noted that in both Figure 7 and Figure 8 when evidence is inserted into nodes 7 and 9,
![img-8.jpeg](img-8.jpeg)

Figure 9: Probability of "Event Escalation" given both Turbine Blades Expelled and Gas Import Riser Impact

there is no effect on nodes 8 and 10 , which is to be expected as they should be independent from each other. Should this scenario have the potential to occur, immediate action should be taken to prevent a major accident in the form of LOC of hydrocarbons and potential explosion $\&$ fire.

Figure 10 further demonstrates the potential for escalation by showing that the generator's exciter detaches, along with turbine blades expelled and gas riser impact. It shows that again the potential for escalation increases from $61.42 \%$ to $63.86 \%$. This scenario also increases the probability of the HP flare drum being impacted from $1.47 \%$ to $10 \%$ as would be expected.
![img-9.jpeg](img-9.jpeg)

Figure 10: Probability of "Event Escalation" given Turbine Blades Expelled and Gas Import Riser Impact, together with the Exciter Detaching.

Figure 11 demonstrates the final influencing factor on the possibility of event escalation, whereby the HP flare drum is impacted. This increases the potential for escalation from $63.86 \%$ to $77 \%$.

The final scenario, shown in Figure 12, demonstrates the effect of there being an escalated event, for example, observing an explosion or a fire within the area of the platform containing the electrical generator, and the effect this has on the influencing parameters. This serves to obtain areas that would require closer inspection. This scenario has given insight to the possible causes of the event escalation, based upon the data presented. Here the main influencing factors are: "Turbine Blades Expelled" - Yes, increases from $0.12 \%$ to $0.17 \%$; "Exciter Detaches" Yes, increases from $0.15 \%$ to $0.17 \%$; "Gas Import Riser Piping Impact" - Yes, Increases from $6.2 \%$ to $14.31 \%$; and "HP Flare Drum Shell Impact" - Yes, increasing from $0.02 \%$ to $0.03 \%$.

![img-10.jpeg](img-10.jpeg)

Figure 11: Probability of "Event Escalation" given that all Influencing Factors take place.
![img-11.jpeg](img-11.jpeg)

Figure 12: BN Model illustrating the effects on the parent nodes when "Event Escalation" takes place.

# 4.5.1.2 Sensitivity Analysis 

Sensitivity Analysis (SA) is essentially a method to determine how responsive the output of the model is when subject to variations from its inputs. Having the understanding of how a model responds to changes in its parameters is important when trying to maximise its potential and ensuring correct use of the model. SA provides the user with a level of confidence that the BN has been built accurately both in terms of the graphical structure, but more importantly, the probability distribution. It also provides verification that the model is functioning as intended. In this analysis a SA is used to demonstrate how responsive a specific event is given small

percentage increases and decreases in the probability of other nodes. Knowing the most influential nodes can assist in the experimentation and further expansion of the model. Similarly, nodes which have very little influence can be altered or discarded [14].

The SA conducted for the Initial BN model focuses on the event E5 and its parent nodes, shown in Figure 7, to further verify the claims in Section 4.5.1.1. However, the analysis will be conducted using smaller increases and decreases in the probabilities of the parent nodes as opposed to inserting $100 \%$ occurrence probability into the input node CPTs.

A possible way of undertaking this is to manually insert evidence into the input nodes, one by one, and subsequently analyse the effect on the output node via its posterior probability. When doing this the input nodes are increased or decreased by equal percentages, individually. This allows for clear comparison of their impact upon the output node. However, this manual method was not applied to this analysis. Instead a parameter sensitivity wizard within the Hugin BN software was used. In this program wizard the input node is individually paired with the output node in its desired state. In this case that was "E5. Event Escalation" in the state 'Yes'. A state for each of the input nodes was purposely selected. It should be noted that in this analysis, node 6, "Generator bearings" has had evidence input at state - 'Failure' to $100 \%$. This input of evidence allows for nodes $7,8,9 \& 10$ to remain independent from each other, which allows for the values analysed in the sensitivity analysis to remain consistent. Following this the four input nodes (nodes $7,8,9 \& 10$ ) are all set to state - 'No' in the parameter sensitivity wizard. In this way a sensitivity value from Hugin was obtained for each input node and using Microsoft Excel a graph was constructed to show the results

From the graph in Figure 13 it can be seen that the most influential factor on "Event Escalation" is "Gas import Riser Impact", whilst the least influential is "Exciter Detaches". If the probability of State - 'No', "Gas Riser Impact" increases by 10\%, then the probability of "Event Escalation" decreases by $2.63 \%$. Whereas, if the probability of State - 'No', "Exciter Detaches" increases by $10 \%$, then the probability of "Event Escalation" only decreases by $0.29 \%$. From the graph it is also apparent that the sensitivity function is a straight line which adds to the model verification. The sensitivity values computed within Hugin are shown in Table 7.

It should be noted that the sensitivity values within Table 7 are negative as in their current states of 'No', they have a negative effect on the outcome of "Event Escalation" - 'Yes'. For example; with the probability of "Turbine Blades Expelled" increasingly being 'No', it is less likely that "Event Escalation" - 'Yes' occurs.

![img-12.jpeg](img-12.jpeg)

Figure 13: Sensitivity Functions for the four input nodes acting upon Event "E5. Event Escalation"

Table 7: Sensitivity Values for the four input nodes acting upon Event "E5. Event Escalation"


# 4.5.2 Verification of the BN Model 

For partial verification of the model, it should satisfy the three axioms stated in Section 3.2.5. Examination of the model in Figures 7 to 12 shows that when evidence is inserted in the form of a component failing or not failing, the posterior probabilities for the final events decrease or increase depending on whether state in question is positive or negative.

Examination of a specific part of the model, in Figure 8, reveals when "turbine Blades Expelled" is set to $100 \%$ 'Yes', this produces a revised increase in probability for "Event Escalation" occurring from $25.19 \%$ to $35.09 \%$. Figure 9 shows both the change in Figure 8 and "Gas Import Riser Piping Impact" set at $100 \%$ 'Yes'. This resulted in a further increase in the potential for "Event Escalation" occurring. Figure 10 shows the changes in Figure 9 plus the "Exciter Detaches" being set to $100 \%$ 'Yes', again resulting in an increase for the potential for "Event Escalation" being of the state 'Yes'. Finally, Figure 11 shows all of the influencing factors on

"Event Escalation" being set to 100\% 'Yes', resulting in yet another increase in the probability of "Event Escalation" occurring from $63.86 \%$ to $77.00 \%$.

This exercise of increasing each of the influencing nodes as well as the changes displayed when increasing or decreasing the probability of the initial event occurring satisfies the three axioms stated in Section 3.2.5. Given this, it is possible to state that partial verification can be given to the BN model.

# 5 CONCLUSIONS 

This paper has outlined the Bayesian Network technique that has been used to model the cause and effect relationship of a specific component failure of an electrical generation system, within a module of an offshore platform. It has been stated that offshore systems can be very complex and when coupled with the volume of data required to model failures within these systems, it makes BNs a challenge to model effectively. This synopsis of BNs is in conjunction with research conducted by [33], where they apply BNs to produce a predictive model for Autonomous underwater Vehicle (AUV) loss. They state that the use of BNs to model the failures of AUV missions, under sea ice is particularly appropriate as BNs cope well with indeterminate or probabilistic elements and uncertainty. However, in some cases a lack of reliable data means that some risk assessment models cannot always be applied. With this in mind, the BN model demonstrates that BNs can provide an effective and applicable method of determining the likelihood of various events under uncertainty. The model can be used to investigate various scenarios around the systems and components outlined and to show the beginnings of establishing where attention should be focused within the objective of preventing offshore incidents, as well as having a clear representation of specifically where these accidents can originate from. This method of modelling offshore risk assessment is to be improved upon in future research, by potentially modelling larger areas with several systems and an increased number of components. The purpose of this is to gain a wider understanding of how offshore systems interrelate.

A number of tests were generated to verify the hypotheses of the model by applying the methodology to a case study (See Section 4). The BN model has demonstrated the effect a possible retaining ring failure would have on the electrical generation system, and surround area, of an offshore platform. The levels of fatalities have been omitted from the analysis as the objective of the research was to determine whether it is possible to accurately model equipment failures using BN. This is because the BN model is part of the development of NUI-

Integrity Cases, whereby there is very limited physical human presence on board. Furthermore, the BN was constructed utilising equipment on a manned installation as a further objective of the research is to demonstrate whether it is possible to create a dynamic risk assessment model that will allow for humans to not be continuously present on large installations, but monitor its operations from onshore. Hence, the Initial BN model presented in this work provides a base to expand the research and the BN model to achieve this goal.

In relation to the verification of the model a sensitivity analysis was carried out to determine how responsive the output of the model is to various modifications in the inputs and subsequently verify that the model works as expected. This exercise is vital as it provides an indication to what the most important variables. In addition, inputs can be ranked or weighted in terms of their importance upon the output or final consequences. For example, in the Initial BN model "Gas Import Riser piping Impact" had a much larger effect on the possibility of "Event Escalation". The more advantageous element of conducting SA in BNs is that they take into consideration the chain of events below the input node leading to the output node, which presents a closer approximation to reality.

There are several interesting and relevant possibilities that can be considered and explored with relative ease now that the core structure of an initial model has been constructed. However, before expanding the model it is vital to maintain that it must remain practical and close to reality from the perspective of gathering data and generating results. Continually too many variables which display vague information or increasingly irrelevant effects can diminish the quality of results and findings.

# ACKNOWLEGEMENTS 

This research is supported by Liverpool John Moores University and RMRI Plc. Thanks are also given to the EU for its financial support under a European Commission funded project WEASTFLOWS (2011-2016). Thanks are extended to D. Lau and D. Minty of RMRI Consulting Plc., UK for their useful suggestions and comments on the research work.

## DISCLAIMER

This paper is the opinion of the authors and does not represent the belief and policy of their employers.

# APPENDIX 1 COMPLETE CPTS FOR THE BN MODEL 


![img-13.jpeg](img-13.jpeg)


![img-14.jpeg](img-14.jpeg)


![img-15.jpeg](img-15.jpeg)


![img-16.jpeg](img-16.jpeg)


![img-17.jpeg](img-17.jpeg)
