# HIAL open science 

## Sustainable management of end-of-life systems

Matthieu Godichaud, Ayele Tchangani, François Pérès, Benoît Iung

## To cite this version:

Matthieu Godichaud, Ayele Tchangani, François Pérès, Benoît Iung. Sustainable management of end-of-life systems. Production Planning and Control, 2012, Sustainable Manufacturing, 23 (2-3), pp.216-236. 10.1080/09537287.2011.591656 . hal-00669018

## HAL Id: hal-00669018 <br> https://hal.science/hal-00669018v1

Submitted on 17 Jan 2022

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# OATAO 

## Open Archive TOULOUSE Archive Ouverte (OATAO)

OATAO is an open access repository that collects the work of Toulouse researchers and makes it freely available over the web where possible.

This is an author-deposited version published in : http://oatao.univ-toulouse.fr/ Eprints ID : 15537

To link to this article : DOI : 10.1080/09537287.2011.591656
URL : http://dx.doi.org/10.1080/09537287.2011.591656

To cite this version : Godichaud, Matthieu and Tchangani, Ayeley and Pérès, François and Iung, Benoît Sustainable management of end-of-life systems. (2012) Production Planning and Control, vol. 23 (n²3). pp. 216-236. ISSN 0953-7287

Any correspondence concerning this service should be sent to the repository administrator: staff-oatao@listes-diff.inp-toulouse.fr

# Sustainable management of end-of-life systems 

Matthieu Godichaud ${ }^{\mathrm{a}}$, Ayeley Tchangani ${ }^{\mathrm{b}}$, François Pérès ${ }^{\text {b }}$ * and Benoît Iung ${ }^{\mathrm{c}}$<br>${ }^{a}$ Laboratoire d'Analyse et d'Architecture des systèmes (LAAS CNRS), 7 avenue du Colonel Roche 31077 Toulouse Cedex 4, France; ${ }^{\text {b }}$ Laboratoire Génie de Production, Ecole Nationale d'Ingénieurs de Tarbes, 47, Avenue d'Azereix - BP 1629 - Tarbes Cedex, France; ${ }^{\text {c }}$ Centre de Recherche en Automatique de Nancy, Campus Sciences BP 70239 Vandoeuvre Cedex, France


#### Abstract

In a sustainable development context, the stakes of the last stage of system life cycle, the end-of-life stage, have increased over recent years. End-of-life systems have to be de-manufactured in order to be valued so as to respond to environmental concerns. The aim of a disassembly strategy consists in issuing a solution to the whole decision problem raised during the end-of-life stage of systems. Indeed, decision makers have to select valuable components according to technical, economical and environmental criteria and then design and optimise a disassembly support system that will generate these products. The solution obtained is what we refer to in this article as a disassembly trajectory. The work presented in this article is about planning these trajectories on different horizons integrating several arrivals of end-of-life systems. The proposed approach, with Bayesian networks and influence diagrams as the underlying mathematical tools, enables dynamically defined uncertainties to be taken into account.


Keywords: disassembly; reverse logistic; modelling; Bayesian networks; optimisation; uncertainties

## 1. Introduction

For many years now, the end-of-life stage of systems has become the subject of more and more studies. This is due, on the one hand, to legislative pressures in terms of environmental protection and, on the other hand, to possible economical profits that may be gained by increasing the value of products obtained from the disassembly of these systems. These stakes compel manufacturers to set up disassembly processes in order to increase the value of their systems. Indeed, end-oflife systems must be disassembled in order to increase the value of their components responding so to environmental constraints. It is a designer's responsibility to integrate these constraints by proposing disassembly processes for their systems at the design stage. Increasing value strategies must respond to all decisional problems raised during the retirement step. Mainly, valuable products must be selected according to technical, economical and environmental criteria and disassembly systems enabling the products to be obtained have to be defined and optimised (Inderfurth and van der Laan 2001, Inderfurth et al. 2001).

Within this framework three types of decisions are considered. The first relates to the determination disassembly level i.e. the best option of valorisation
and, for the subsets, the choice between disassembling or recycling. The second relates to operation sequencing which aims at fixing how to obtain the products and the logical sequence of the operations to obtain them. Finally, planning consists in determining the quantities of products and their obtaining dates on a given horizon. The decision support in disassembly must make it possible to handle these three types of decision and to establish the link between them to keep a total control of the strategy. A disassembly trajectory leads to the identification of valuable products of an end-of-life system, of their value-increasing channels and of the ways to obtain them (dismantling operations, separation operations...). Modelling of disassembly trajectories is a key point in the decision support in disassembly since it makes it possible to structure data, to model the process and to propose disassembly solutions. We propose in this article a trajectory model which allows handling these key factors and also makes it possible to manage uncertainties inherent in disassembly.

We show in the example of Figure 1 a system which can be described by a connection diagram. It is made up of seven elements. A subassembly named SA3 regroups five elements and is itself made of two

![img-0.jpeg](img-0.jpeg)

Figure 1. Example of disassembly trajectory.
subassemblies $S A 2$ and $S A 3$ that share a component. Optimisation can show that it is more profitable to valuate components $1, S A 1$ and 7 for instance (trajectory 1) or conclude that the better decision consists in performing one more disassembly in order to valuate components $1,2,4, S A 3$ and 7 (trajectory 2) ....

We present in the first part the context of this study and the disassembly planning problem. The second part is devoted to the modelling of industrial processes that integrate temporal uncertainties. The model will be used in the third part as a support for disassembly trajectory planning.

## 2. Problem statement on disassembly trajectory planning

### 2.1. Context

The following activities treating an end-of-life system from its retirement from service to its total disappearance constitute the disassembly process. A disassembly process constitutes three principal stages requiring the realisation of many activities (Figure 2). The first stage concerns reverse logistics activities consecutive to the retirement of an industrial system. It is then packed and transported to the disassembly place. The second stage is the disassembly process; many disassembly techniques (dismantling operations, dislocation operations...) may be considered here according to the objectives. Usually, three value-increasing channels are considered for the treatment purposes of end-of-life systems, namely:

- functional recycling that consists in introducing products obtained from deconstruction process
into the process of new systems production or into the exploitation process (maintenance for instance) of existing systems;
- material recycling: the purpose here is to reuse the material obtained from components of the end-of-life system in the production process of new systems;
- energy-oriented valorisation: products that cannot be recycled by one of the previous channels may be burnt to produce energy.

Products and/or components that cannot be recycled may be stocked in safe places that respect environmental issues.

The disassembly system enables activities related to the second stage of the disassembly process to be carried out. Its design may constitute a complex task mainly when many disassembly options and valueincreasing options are possible for each component of the considered system. The decision maker has then to determine the best disassembly trajectory. A disassembly trajectory characterises all the generated products along with the way to obtain them and their valueincreasing channels. An end-of-life system is composed of a certain number of interconnected components. Each identified element of such a system may have one or many disassembly options. Two main options are generally considered when defining a disassembly strategy: disassembly operations that make it possible to generate many products from one single product and value-increasing actions that concern the engagement of a product into a value-increasing channel. An element to which both of these options may apply is known as a subset. Disassembly operations for subsets can be considered only in order to recuperate and to valorise components. Elements not concerned by disassembly operations are referred to as elementary components. They may be considered by valueincreasing actions.

Risks related to developing a disassembly system are similar to those of any industrial production system development. But risk management during the exploitation stage of the disassembly system has some specific features (Figure 2):
(1) Before the system is retired from service: risk here is related to the extension of the life duration and to the determination of the appropriate retirement date using safety and economic criteria.
(2) Upstream of the disassembly chain: risks here concern different collecting and repatriating modes.
(3) On the disassembly chain: risk is related to possible environmental and human

![img-1.jpeg](img-1.jpeg)

Figure 2. Disassembly process representation.
contamination by dangerous products (gas, asbestos, lead,...) and necessitates setting up a dependability process.
(4) Downstream of disassembly chain: risk is associated with the introducing of spare parts into the production of new systems or maintenance of existing ones that necessitate certifying these components and/or re-establishing their operational conditions in terms of reliability.

We are mainly concerned here with managing risks induced by uncertainties during the disassembly stage and their economic consequences. These uncertainties are characterised by probability distributions related to a certain number of parameters commonly encountered in the disassembly operational process. To improve the decision aid process, we consider it necessary to manage uncertainties related to the following elements:

- random state of the end-of-life system and its components that may be in varying states of degradation,
- demands of products obtained once the disassembly process has been performed that are often uncertain mainly in terms of diversity and nature (spare parts),
- arrival instants of systems at their disassembly place that cannot be planned in a deterministic manner,
- inventory management of products (valuable or intermediary products) that are waiting for a demand to be issued,
- disassembly operations duration that are generally uncertain because they may depend on the state of the system and/or the subsets to be disassembled,
- availability of resources needed to carry out the disassembly operations.

The disassembly trajectories taking into account these parameters apply to a time horizon covering the arrivals of many end-of-life systems. The decision maker is then facing a situation of disassembly system planning in the presence of uncertainties; the main elements of this planning problem will be presented in the next section.

### 2.2. Disassembly system specification

From the context described so far, disassembly planning helps determine the quantities of valuable products and their obtaining dates on a given horizon according to a certain number of criteria. To this end, the decision maker must establish:
(1) the structure of the end-of-life system in order to identify valuable components,
(2) the elements describing the disassembly system.

Input data for a disassembly plan definition concerns, first, the structure of the end-of-life system. They may be represented by value-increasing nomenclature as in Lambert and Gupta (2005). This nomenclature is composed of a tree representation of the system and complementary information describing the increasing value of each component (elementary components, subsets...). This tree is constituted by a set of nodes representing valuable components and a set of arcs between these nodes traducing 'subset-components' relation. Further information is added to describe each component more precisely. This information enables the description of materials, recovery modes, recycling channels or quantities of components contained in a subset.

The main objective here is to determine disassembly trajectories on horizons covering the arrivals of many end-of-life systems. It is necessary in this case to

consider a certain number of parameters that might influence the planning (inventory level, resources usage...):
(1) Arrivals of end-of-life systems: they characterise the relations between the system user and the place of disassembly.
(2) Obtaining operations of valuable products: they are realised by the disassembly system.
(3) Valuable product demands: they characterise the relations between the disassembly system and the increasing value channels.

Arrivals of end-of-life systems containing valuable products can be considered as an input of the disassembly system. Decision to stop the exploitation of a system is normally made by its user according to criteria such as performance, safety or legislation. Thus, arrivals are not controlled by the disassembly planning system and therefore represent a constraint. Parameters characterising the arrivals may then be arrival mean values, quantities and dates.

Demands result from the value-increasing channels. They are analysed by the disassembly planning system (determination disassembly depth) and are characterised by variables defining quantities and due dates or by frequency rates (number of demands per unit time). This characterisation must take into account the diversity of sources encountered in the disassembly context and the uncertainties related to these sources. In this article, we manage the uncertainties through the use of probability methods as a risk-based decision aid approach (Tang 2006).

The disassembly system is described by some variables. First of all, the disassembly system state is characterised by different product inventories with level and capacity variables. Other variables representing a disassembly system concern resources (personals, test resources, disassembly resources,...) described in a planning context by their number and their availability.

Resources and storage capacities are defined at a strategic level. At the operational level they are considered as constraints to be satisfied in order to maximise increasing value of an end-of-life system arriving on the planning horizon. The disassembly system sets up operations that make it possible to obtain different products. These operations may be described in the planning framework by rates (number of products per unit time) or by the realisation duration.

### 2.3. Trajectory planning models

### 2.3.1. Planning models

Different criteria may be used to evaluate disassembly trajectories. Some of them are particularly
common like:
(1) Economic profit: this is the commonly used criterion to balance generated revenues by valuable products and costs engaged to obtain them; other costs can be integrated into this criterion such as value-increasing options costs (re-assembly, re-conditioning,...) or logistic costs (storage, transportation...).
(2) Valorisation rate: this criterion corresponds to the percentage of recycled material when realising a valorisation action on end-of-life system components; it depends on the homogeneity of material contained in the component or to the impurity rate (a rate of $100 \%$ is generally associated with a functional recycling option).
(3) Ecological balance: each option for end-of-life can be ecologically evaluated according to life cycle analysis principles; by making an inventory of different materials released by the system into the environment, one can give an ecological score to each option.

From an economic point of view, a disassembly trajectory may be evaluated first by the disassembly costs it generates. These costs are associated with each identified disassembly operation. They are constituted by fixed costs related to the realisation of the environment of operations decided at a strategic level and varying costs related to the realisation of the operation (use of resources) at an operational level. These varying disassembly costs may depend on the realisation duration and/or on the number of disassembled units.

Inventory level management is an essential element in a disassembly optimisation process (Addouche 2003). Determining a disassembly trajectory will make it possible to balance inventories of different components of a disassembly system. To do so, the decision maker will define parameters related to storage costs; they are composed of fixed costs (storage place organisation costs) defined at a strategic level and varying costs that depend on the inventory level.

Evaluation of a disassembly plan must also integrate the revenues it generates. These revenues are generated when demands for valuable products are satisfied. When the disassembly depth is a decision variable (recycling a subset or disassembling it in order to increase its components value), the revenues that each component can generate play an important role in the optimisation process.

Besides the three main parameters evoked in the previous sections, other indicators may be considered

according to hypotheses and objectives formulated for the disassembly system.

These hypotheses may concern demand satisfaction: they may be viewed as an admissibility constraint for a plan (unsatisfied demands are not permitted) or as an indicator to optimise (unsatisfied demands are allowed). In the particular situation of disassembly systems, other constraints may concern the management of the acceptation of end-of-life systems at the place of disassembly. Indeed, when storage capacity is limited the disassembly system is full. New arrivals of end-of-life systems may be refused or stocked in annexe places, creating supplementary costs. This hypothesis may be taken into account in the optimisation process as a saturation cost.

One of the first planning models for the disassembly process of an end-of-life system has been the one developed in Gupta and Taleb (1994). The authors propose reverse material requirement planning (MRP) approaches, which consist in taking into account divergent aspects of the disassembly process as opposed to convergent aspects in the case of classical MRP. In Barba-Gutiérrez and Adenso-Díaz (2008), the authors solve a basic planning problem to which they apply later economic approaches. The algorithm has been modified in Barba-Gutierrez et al. (2008) to take into account demand uncertainties and imprecision. An approach using fuzzy logic enables these two features to be integrated in order to determine the needs for each period. Because of these uncertainties, demands may not be fulfilled within a given period and may be postponed for upcoming periods as deterministic demands. An MRP approach is also used in Taleb and Gupta (1997) and Taleb et al. (1997) in order to determine quantities and due dates of products to disassemble to fulfil component demands. The authors propose to take into account components contained in different subsets of the same end-of-life system (Taleb and Gupta 1997) or contained in different end-of-life systems (Taleb et al. 1997). The problem is then more complex and the authors suggest a heuristic to solve this problem but this may lead to impracticable solutions.

Other authors suggest formulating the disassembly planning problem as a linear programming problem in order to optimise different costs related to inventory management. In Lee et al. (2002), the variables of the model correspond, for each period of the planning horizon, to disassembled products quantities (variables associated with each subset), to quantities of stocked products (variables associated with all products identified in the nomenclature) and to the quantities of end-of-life systems to be treated; the objective function to minimise is the total cost over the planning horizon.

The model constraints are represented by the conservation of products from a period to another, by the demand satisfaction on each period and by the disassembly capacity limitation. In Lee and Xirouchakis (2004), the authors propose a heuristic in order to solve large problems. Furthermore, they introduce preparation costs into the objective function. A similar formulation of planning problem has been analysed in Kim (2005). Optimisation goal here is to balance disassembly costs, preparation costs and storage costs. An exact method to solve the problem has been first considered and a heuristic is further proposed to deal with general cases with multilevel structures, common components for one or more end-of-life systems (Kim et al. 2006) and limited capacity constraint. In Langella (2007), the author proposes first a linear programming formulation of the planning problem so to raise its limitation for large dimension problems; a heuristic is then proposed. Inderfurth and Langella (2006) propose a model that takes into account uncertainties related to the number of components that can be obtained from each subset of an end-of-life system.

A single-period approach is proposed in Veerakamolmal and Gupta (1998a, b) and Lambert and Gupta (2002). The goal is to determine which end-of-life system among different types must be disassembled in order to satisfy elementary component demands considering that components may be contained in different types of systems.

The objective function considers on the one hand the revenues generated by the satisfaction of the demand and on the other hand the costs of buying the end-of-life system as well as the costs of disassembly and the costs of elimination of waste products. This idea of a disassembly planning problem has been considered in Kongar and Gupta (2002a, b) using a multi-criteria approach. Decision variables correspond to quantities of end-of-life systems purchased, quantities of reused components, quantities of stocked components, quantities of recycled components and quantities of waste components. In order to determine these variables, the authors propose different criteria related to revenues generated by reuse and recycling components, to the costs of disassembly as well as to the costs related to other disassembly activities (logistics, storage, transportation...). Solving methods proposed are multi-criteria methods: goal programming and linear physical programming. The model has been extended in Kongar and Gupta (2006) in order to take into account uncertainties using fuzzy logic goal programming.

None of the disassembly planning models evoked so far considers the problem related to the

determination of disassembly trajectory. In these models, valuable products and their end-of-life options are fixed before the planning process - that is the disassembly depth - is known in advance. However, it seems interesting to consider different possible trajectories when realising the disassembly of an end-of-life system in order to be able to adjust the decisions according to the forecast demands and arrivals of systems to be disassembled. Another aspect that is not usually considered by the planning models is the limited number of systems that can be disassembled over a planning horizon. In those models, all demands can be satisfied by disassembling end-of-life systems that are assumed to exist. When the arrivals are limited over a planning horizon, as is the case in some fields such as aeronautics, decision makers must select the demands to be met according to arrivals.

The problem to be tackled is then similar to the determination of the disassembly trajectory of each arrival forecast over the planning horizon.

The following sections aim to face most of these challenges and in particular to tackle the problem of performing the disassembly process in an uncertain context related to parameters which are going to be introduced.

### 2.3.2. Handling uncertainties

Uncertainties are rarely taken into account when establishing models for disassembly planning although they are inherent features of the end-of-life systems management field. Integrating uncertainties to disassembly planning models in order to obtain a robust solution is important. The management of uncertainties in planning systems is often made through stochastic approaches aiming to determine inventory management policies. These approaches are mainly used in the planning of re-manufacturing activities. The reuse or recycling of components is the most beneficial option, be it for economical or environmental reasons. This option necessitates some activities downstream of the disassembly system and they are generally referred to as re-manufacturing (Inderfurth 1997, Fleischmann et al. 2002, Mahadevan et al. 2003, Takahashi et al. 2008).

Uncertainties are inherent to disassembly problems. We showed in Godichaud (2009) that the Bayesian networks could be an interesting modelling tool to represent disassembly trajectories and uncertainties related to them. A Bayesian network is a graphic model in which knowledge is represented with variables and relations between these variables (Naïm et al. 1999). It enables the determination of the probabilities of various variables using inference
![img-2.jpeg](img-2.jpeg)

Figure 3. Example of a Bayesian network and an influence diagram.
![img-3.jpeg](img-3.jpeg)

Figure 4. Modelling of the temporal evolution of a variable.
mechanisms (Huang and Darwiche 1996, Naïm et al. 1999). In Medina-Oliva et al. (2009), the authors present a survey of using Bayesian network to model complex systems.

In order to model decision problems, decision and utility nodes can be introduced into the model. An influence diagram is thus obtained which corresponds to the Bayesian network extension to model a decision problem with uncertainties (Jensen and Nielsen 2007). The graphic view makes the implication of all actors in the modelling of the decision problem easier. Chance nodes (circles in Figure 3b) represent problem variables; decision nodes (squares) represent possible choices and utility nodes (diamonds) enable the evaluation of the various possible decisions. Arcs connecting a chance node to a decision node correspond to information available at the time of the decision making. Different solving algorithms of decision problems are associated with influence diagram models (Lauritzen and Nilsson 2001, Jensen and Nielsen 2007).

Uncertainties handled in disassembly trajectory planning are time dependent. The use of the dynamic Bayesian network (DBN) makes it possible to shift from a 'static' description of the trajectories to a 'dynamic' representation (i.e. considering a temporal dimension). An illustration of the use of DBNs to model an industrial process can be found in Muller et al. (2008).

DBNs are an extension of Bayesian networks enabling the representation of the temporal evolution of the variables on a given horizon (Murphy 2002). Temporal dimension is divided into $t$ time steps. Network variables are then characterised at each time step and a variable influences other variables over the horizon (Figure 4). The variable $X_{t}$ represents the variable $X$ at the time $t$ and the DBN makes a compact

representation possible here between times $t$ and $t+1$ with a limited number of variables.

A reliability block diagram (RBD) is defined by two types of elements (Tchangani and Noyes 2006):

- Its structure: as for a Bayesian network, is characterised by an acyclic directed graph representing the relations between the variables; there are two types of relations:
- intra-period relations: they correspond to the arcs between the variables defined in the same time step $t$ (these relations are the same as in 'static' Bayesian networks). Instantaneous relations are represented in this way.
- Inter-period relations: they represent temporal relations between variables defined at different time steps.
- Its parameters: as for the Bayesian network, DBN parameters correspond to conditional or a priori probability distributions which can be represented in the form of conditional probability table (CPT) for discrete variables; parameters induced by inter-periods arcs characterise the dynamics of the variables.

Given input variables at $t=0$, temporal evolution can then be determined by inference. Specific DBN inference mechanisms RBD are possible (Murphy 2002). Within the framework of complex system or industrial process simulation and for large horizons, an approach consists in making iterative inferences (Weber and Jouffe 2005). Indeed, from $t=0$ the probability distribution on the states of $X_{t}=1,2, \ldots$ is calculated by successive inferences as displayed in Figure 5.

We propose to model disassembly trajectories on temporal horizons with DBN. Our objective is to propose a trajectory modelling tool in order to compare them by taking into account the uncertainties defined with respect to temporal dimension (activity durations, demand and arrival dates, ...).

## 3. Industrial process modelling with DBNs

Disassembly processes are industrial processes. They are defined by a set of interactive activities coordinated in order to gradually transform input elements into output elements. These elements can be material or immaterial (information for example).

Within the framework of the disassembly trajectory representation, two types of activities are considered. The first corresponds to disassembly operations generating several products (output elements) from a
![img-4.jpeg](img-4.jpeg)

Figure 5. DBN inference principle.
![img-5.jpeg](img-5.jpeg)

Figure 6. Activity modelling with DBN.
single one (input element). The second corresponds to increasing value actions consisting in treating a product (input element) to obtain a valuable result (output element).

We established a disassembly trajectory model representing the chaining of both activities according to the flows of disassembled products (Godichaud 2009). The model enables the setting of the activities to be carried out to disassemble a system at the end of its lifetime. It is a minimal representation of disassembly processes. Indeed, it characterises the disassembly process framework by identifying disassembly operations and increasing value actions and by formalising logical relations (precedence, parallelism...) between them.

The DBN we are going to introduce now enables the characterisation of the temporal realisation of the disassembly process in the presence of uncertainties and disturbances.

### 3.1. Representation of an activity

In the case of a process being characterised by a set of inter-connected activities, its characterisation requires each activity to be considered. An activity model is presented in Figure 6. Index $t$ associated with each variable indicates that it is characterised at time $t$.

Nodes presented in Figure 6 characterising an activity at a time $t$, correspond to:

- $A_{t}$ : activity realisation at time $t$,
- $N_{E_{t}}$ : elements transformed by the activity (inputs),
- $N_{S_{t}}$ : activity result (outputs),
- $N_{C_{t}}$ : constraints, controls or disturbances influencing the activity realisation,
- $N_{R_{t}}$ : resources enabling the realisation of the activity.

These different nodes describe the state of the activity flow and the activity realisation. The user (decision maker, analyst...) can introduce as many variables as there are flows to consider. The arcs characterise the interactions between flows and activities. This model makes it possible to take into account and handle uncertainties from various origins as well as the characterisation of causes and effects relating to the disturbances on the activities.

After having defined variables and their relations, the node parameter setting enables the specification of the logic chaining of the activities.

### 3.2. Characterisation of variables

The modality set of an activity node has to characterise the realisation of the activity at $t$. Two modalities at least are necessary to this end:
(1) ' $r$ ': the activity is carried out at $t$,
(2) ' $n r$ ': the activity is not carried out at $t$.

An activity can begin only when all these inputs are activated. The outputs are activated when the activity is finished. Modalities of nodes describing an activity input/output are at least:

- ' $a$ ': the element is activated at $t$ i.e. a beginning condition of activity is validated,
- ' $n a$ ': the element is not activated at $t$.

Other activity realisation conditions can be taken into account, such as the availability of a resource (node included in $N_{R}$ ), a realisation policy (monitoring decision) or other constraints (nodes included in $N_{R}$ ). For the description of these various situations, the decision maker may introduce new variables.

### 3.3. Specification of activity sequences

Activity sequences are specified with node parameters. The basic mechanism to be modelled is characterised by the repetition of the following steps: element
activation (obtaining the products, activation of a flow) and activity realisation.

- when the activity is not carried out (node taking modality ' $n r$ '), the product is not generated (modality ' $n a$ ' corresponding to a nonactivation),
- when the activity is carried out (node taking the method ' $r$ '), the product is generated (modality ' $a$ ').

The modelling primitive resulting from the generic model of Figure 6 and characterising these mechanisms is presented in Figure 7.

From this primitive, an activity realisation can be specified and connected to other activities.

Indeed, the activity realisation is characterised through the connections (arcs) between the nodes:

- $P E_{t} \rightarrow A_{t}: P E_{t}$ correspond to the product to be treated, this relation stands for the representation of the activity beginning conditions (presence of the product),
- $A_{t-1} \rightarrow A_{t}$ : this relation represents the activity realisation from time $t$ according to the activity history.

Parameters associated with $A_{t}$ characterise uncertainties related to the activity duration (e.g. parameter $\alpha_{t}$ in the CPT presented in Table 1 with $0 \leq \alpha_{t} \leq 1$ ). Parameter $\alpha_{t}$ stands for the probability of carrying out the activity over the period $(t-1, t)$.

Node $P S_{t}$ characterises an activity output. It is generated when the upstream activity is finished; a CPT of this variable is presented in Table 2.
![img-6.jpeg](img-6.jpeg)

Figure 7. Modelling primitive to characterise an activity.

Table 1. Activity node parameters.


Other types of elements, in particular economic ones, can also be modelled as shown later.

### 3.4. Example: comparison of two solutions for the process realisation

Based on the modelling principles presented so far, an example is proposed to illustrate the different solutions likely to be used to perform the process represented in Figure 8. The process begins when activating a product modelled by node $P_{1 t}$. The objective of the process is to generate one of the products modelled by $P_{3 t}$ and $P_{4 t}$, and it ends with the activation of these elements.

To generate product $P_{3}$, it is necessary to carry out the activities modelled by nodes $A_{1 t}$ and $A_{2 t}$ by generating intermediate product $P_{2}$. To generate product $P_{4}$, it is necessary to carry out the activity modelled by node $A_{3 t}$. One of these two solutions has to be selected (decision node $C_{i}$ ). The model enables the decision maker to evaluate and compare them according to various criteria.

Let us consider, for instance, the objective of satisfying a demand for products $P_{3}$ and $P_{4}$ with the risks of the customer being kept waiting for the product, characterised by delay penalties. $T_{D}^{P_{3}}$ is

Table 2. Output node parameters.


noted as the demand date for product $P_{3}$. The goal is to evaluate the probability of obtaining $P_{3}$ at date $T_{D}^{P_{3}}$. If the product is obtained after this date, a penalty, higher or lower according to the delay, is generated. Same notations will be used for $P_{4}$.

Uncertainties relating to activity durations are specified in CPT of nodes $A_{1 t}, A_{2 t}$ and $A_{3 t}$ with the numerical values of parameters $\alpha_{t}$ presented in Table 3. Parameters $\alpha_{t}$ are not time dependent in this example.

We carried out a simulation on a horizon of 3000 time steps by considering that variable $P_{1 t}$ was activated from $t=0$ (i.e. the product is available). Results are presented in Figure 9. They correspond to the probabilities that products $P_{3}$ and $P_{4}$ are activated on the time horizon. One can then compare the probabilities of realisation ending for both solutions at singular times. These times (expressed in time unit, tu) correspond in particular to the demand dates $T_{D}^{P_{3}}=1500 \mathrm{tu}$ and $T_{D}^{P_{4}}=1000 \mathrm{tu}$ as well as the demand cancellation date: $T_{D F}^{P_{3}}=2500 \mathrm{tu}$ and $T_{D F}^{P_{4}}=2000 \mathrm{tu}$.

From Figure 9, the probabilities of obtaining the products, respectively, after the demand dates and cancellation dates can then be evaluated (Table 4). To compare both solutions, penalty values are introduced to model the consequences of obtaining the products after specific dates. The solutions are then evaluated by first multiplying the probabilities of getting the product by the associated penalties for each date and then by summing the different values. The results are presented in Table 4. The adopted solution is that which will minimise the expected penalties, corresponding here to solution 2 (realisation of $A 3$ and generation of $P 4$ ).

We have proposed a generic activity model taking into account different uncertainty sources.
![img-7.jpeg](img-7.jpeg)

Figure 8. Process representation example with two realisation solutions.

Disassembly processes are realised within an uncertain context. We thus use the proposed model in the next section to optimise disassembly plans on horizons covering the arrivals of several end-of-life systems.

## 4. Application to disassembly process

### 4.1. Model structure

The trajectory model presented is divided into modules standing for the representation of the physical and economical environment. It can thus be adapted to various situations by the modification of the

Table 3. Activity uncertainties example.


![img-8.jpeg](img-8.jpeg)

Figure 9. A process simulation. parameters associated with each module. The set of modules represents the basic structure for simulation of several disassembly trajectories. It can be considered as a modelling primitive on which one can integrate other elements for the description of specific environments. The global model structure of the model is presented in Figure 10.

The model is structured according to the products which have to be recycled. An arrival module is associated with the product module characterising the complete system. Each product can be subject to an arrival according to the context. The identified products are concerned by one or more increasing value options which are described by option modules. Each option module is then broken up into four modules for the modelling of an activity realisation, the demand, the option satisfaction management and its economical evaluation. The modelling steps are articulated around the modules positioned in Figure 10. Before creating the variables, the user must indeed determine, for a given trajectory, the products to be treated. For each product, it will then identify the set of possible increasing value options. After the first phase of analysis, the variable specification can be carried out for each option module. Thereafter, the various modules are detailed. They characterise an increasing value option of a given product. A summary of variables and parameters of the model is presented in Figure 11.

### 4.2. Module presentation

Within the framework of the disassembly trajectory determination on horizons integrating several arrivals of systems, elementary modules aim to represent uncertainties more particularly related to:

- activity duration;
- demand dates for disassembled products;
- system end-of-life dates.

Table 4. Example of evaluation of two solutions.

of obtaining
a product
after a
demand date
$1-\operatorname{Pr}\left(P_{T_{D}^{E}}=a\right)$ | Penalties
after a
demand date | Probabilities
of obtaining
a product
after a
cancellation
date
$1-\operatorname{Pr}\left(P_{T_{D}^{E}}=a\right)$ | Penalties
after a
cancellation
date | Evaluation  |

By following the modelling principles introduced so far, the user will be able to introduce new modules corresponding to his context.

### 4.2.1. Activity module

'Activity' modules characterise the disassembly operations and the increasing value actions. They are built
![img-9.jpeg](img-9.jpeg)

Figure 10. General model structure.
from the modelling primitive presented in Figure 7. The definition of the 'activity' modules and their interconnections sets the model framework. The other modules are then determined accordingly.

Several arrivals of end-of-life systems and consequently several activity realisations have to be modelled. The nodes modality sets are modified as follows:
(1) Nodes $A_{t}$ representing the activities correspond to the number of products treated at time $t$ and the definition domain of these variables is $\left\{n r, r_{1}, \ldots, r_{N_{M A X}^{d}}\right\}$ where $N_{M A X}^{d}$ is the maximum number of activity expected realisations.
(2) Nodes representing the input and output elements of activities noted $P_{t}\left(P E_{t}\right.$ and $\left.P s_{t}\right)$ correspond to the element activation number at time $t$ and the definition domain of these variables is $\left\{n a, a_{1}, \ldots, a_{N_{M A X}^{d}}\right\}$ where $N_{M A X}^{d}$ is the maximum number of expected element activations.

The CPT of a node $A_{t}$ specifies the probability $\operatorname{Pr}\left\{A_{t}=r u /\left(A_{t-1}=r_{v}, P E_{t}=a_{w}\right\}\right)$ to have realised $u$ times the activity at $t$ given that $w$ products have arrived and the activity had been carried out $v$ times at $t-1$.
![img-10.jpeg](img-10.jpeg)

Figure 11. Summary of module elements.

Table 5. Activity node CPT with two possible realisations.


![img-11.jpeg](img-11.jpeg)

Figure 12. Graphic representation of a demand.

The activity realisation mechanism to be characterised is as follows:

- If the number of products arrived at $t\left(P E_{t}\right)$ is lower or equal to the number of realisations of the downstream activity $\left(A_{t}\right)$, then all the products have been treated.
- Otherwise the activity is in progress.

If we assume, for instance, that the activity can be carried out once during a period and that $\alpha_{t}$ corresponds to the probability of carrying out the activity during one time step knowing that it was already in progress at the previous period, the CPT can be established. It is presented in Table 5 with two possible realisations. However, the flexibility of the model makes it possible to consider other situations such as the possibility of carrying out several times the activity during each time step.

### 4.2.2. Demand modules

Demand modules enable the representation of uncertainties relating to product demand dates. The module graphic representation is given in Figure 12, given that nodes $D_{t}$ represent the demand at instant $t$. Two modalities can be taken into account for these

Table 6. CPT relating to the demand modelling.


Table 7. Example of demand modelling with cancellation policy.


nodes:

- ' $y$ ': indicates there is indeed a demand at instant $t$.
- ' $n$ ' indicates there is no demand at instant $t$.

The temporal relation between variables $D_{t-1}$ and $D_{t}$ characterising the demands at instants $t-1$ and $t$, respectively, enables the characterisation of the law of probability related to the demand. Parameter $\beta_{t}$ stands for the probability of observing a demand during period $t$ (Table 6).

The model also enables the characterisation of other demand profiles. In particular, it is possible to take into account the cancellation of a demand when, for instance, the waiting time for a product becomes too long. A further modality has then to be added to variables $D_{t}$. It is labelled 'ca' and indicates that the demand is indeed cancelled at instant $t$.

The CPT of variable $D_{t}$ in this case is presented in Table 7. Parameter $\gamma_{t}$ corresponds to the probability that a demand is cancelled at instant $t$ given that it was taken at $t-1$.

Within the framework of characterisation of trajectories on horizons covering the arrival of different end-of-life systems, the nodes representing the demand must accept as many requests (i.e. demand modules), as there are demands to be considered. Each demand is noted $D_{i}^{t}$ ( $i$ standing for the $i$ th demand). A node $D_{t}$ is introduced to represent the number of demands taken at instant $t$ (Figure 13).

![img-12.jpeg](img-12.jpeg)

Figure 13. Characterisation of multiple demands.

Table 8. TPC of multiple demand characterisation.


Each node $D_{t}$ takes its modalities in $\{0,1, \ldots, N M A X D\}$ where $N M A X D$ corresponds to the maximal number of demands on the considered planning horizon. An example of specification of a variable $D_{t}$ is given in Table 8. Parameters $\beta_{t}^{1}$ and $\beta_{t}^{2}$ correspond, respectively, to the probabilities of having a first and a second demand on record.

### 4.2.3. Management module

The management module regroups the set of nodes representing indicators relating to the deconstruction process realisation (Figure 14). The validation of a valuation action depends on the demand and the realisation of the activity associated with this option: there is a demand and the product is available. The other specific situations correspond to the waiting time for a product (activity not realised although there is a demand) and to the waiting time for a demand (activity realised but there is no demand).

The decision maker may be interested in characterising the options validation, the intermediate stocks, the valuable product stocks and the waiting demand for an available product.

For a deconstruction option, the following nodes are used:

- A variable $V O_{t}$ represents the number of products to be valuated at instant $t$. It depends on the
number (of available products (node $A_{t}$ ) and on the number of recorded demands (node $D_{t}$ ):
$V O_{t}=\min$ (number of available products;
number of recorded demands).

- variable $S_{t}$ characterises a stock of intermediate products i.e. located upstream of an activity (disassembly operation or valuation action):
- Its definition domain $\left\{0,1, \ldots, N_{M A X}^{S}\right\}$ corresponds to the number of products likely to be in stock at each instant $t$.
- It depends on the number of products located at instant $t\left(P E_{t}\right)$ upstream of the activity and on the number of realisation of the activity at instant $t\left(A_{t}\right)$ :
$S_{t}=\min (0 ;$ number of arrived products
- number of activity realisations).

- Variable $A D_{t}$ characterises a stock of valuable products, that is products waiting for a demand:
- Its definition domain $\left\{0,1, \ldots, N_{M A X}^{D}\right\}$ corresponds to the number of products waiting for a demand at each instant $t$.
- It depends on the number of demands at instant $t\left(D_{t}\right)$ and on the number of activity realisations at instant $t\left(A_{t}\right)$ :
$A D_{t}=\min (0 ;$ number of activity realisations
- number of recorded demands).

- variable $A P_{t}$ characterises the number of not satisfied demands at instant $t$ :
- Its definition domain $\left\{0,1, \ldots, N_{M A X}^{A P}\right\}$ corresponds to the number of demands waiting for a product at each instant $t$.
- It depends on the number of demands at instant $t\left(D_{t}\right)$ and on the number of activity realisations at instant $t\left(A_{t}\right)$ :
$A P_{t}=\min (0 ;$ number of recorded demands
- number of activity realisations).

The graphic representation describing these different indicators is given in Figure 13. The valuable product stock management is modelled with nodes $V O_{t}, A D_{t}$ and $A P_{t}$. The arcs represent the dependency relations with the modules that have just been introduced, namely 'activity' and 'demand' modules.

Evolution of intermediate stocks is modelled with node $S_{t}$ connected to nodes $A_{t}$ and $P E_{t}$.

![img-13.jpeg](img-13.jpeg)

Figure 14. Graphic representation of a management module.

The CPT of the nodes of Figure 13 is established from Equations (1)-(4).

### 4.2.4. Economic module

So far, we have been describing the modules enabling the development of the evaluation indicators of the activities belonging to a deconstruction trajectory with temporal uncertainties related to activity and demand durations. We are now focusing more particularly on the evaluation and the comparison of trajectories from an economic point of view.

We introduce the economic criterion modelling based on four components that are the most common costs and incomes in the field of deconstruction management. Other types of economic measures can, however, be introduced according to the same principles. To evaluate each activity, the following parameters have to be considered:
(1) Realisation cost: based on a temporal dimension, the dynamic model enables the evaluation of the periodical realisation cost and the determination of the expected cost varying according to the lengthening probability of the realisation activity duration.
(2) Product storage or locking up costs: from an $A D_{t}$ variable, the dynamic model enables the specification of this type of cost according to
the time between the production obtaining and the demand record with the associated uncertainties.
(3) Delay penalties: from an $A P_{t}$ variable, the dynamic model enables the specification of a function standing for the representation of penalties due to a delay in satisfying the demand.
(4) Incomes: they are generated when the product is available and there is a demand; the dynamic model enables the definition of an income function from a $V O_{t}$ variable.

Based on these parameters, a generic representation of an economic module used for the estimation of a valuation activity is given in Figure 15. The economic parameters are described with utility nodes (diamonds): $C R_{t}$ characterises the activity realisation cost at instant $i, C S_{t}$ represents the storing cost, $P N_{t}$ correspond to the penalties and $G_{t}$ stands for the activity income generated on the planning horizon. With regard to deconstruction activities, the only parameter taken into account is the realisation cost.

Economic indicator values are determined thanks to the cost models. They are specified in the utility nodes tables. An example of a cost model for each type of utility node is given in Table 9. The cost models used are of the proportional type i.e. the costs and incomes on each period are a linear function of the number of

![img-14.jpeg](img-14.jpeg)

Figure 15. Graphic representation of an economic criterion.

Table 9. Cost model specification.


stored products. The criteria used for the economic evaluation of the deconstruction trajectories correspond to the cumulated costs at a given time. They vary according to the expected costs per period which are specified in the utility tables. Parameters $c r, c s, p n$ and $g$ of Table 9 represent the unit costs per period and per product. Evaluation of a given deconstruction trajectory corresponds to the sum of the costs related to each activity.

### 4.2.5. Arrival module

Uncertainties related to the end-of-life systems arrival have not been taken into account yet. This is, however, an essential aspect of planning which has to be
considered with respect to the nature and the diversity of dismantling modes. Our objective in this section is to take into account these uncertainties in order to evaluate and compare the deconstruction trajectory expected profits. To this end, uncertainties relating to system arrivals are introduced into the model through the specification of an 'arrival' module.

The arrival module is made of nodes $A R_{t}$ characterising the number of end-of-life systems to be deconstructed at instant $t$. Its definition domain is $\left\{0,1, \ldots, N_{M A X}^{A R}\right\}$ where each element of the set is an integer and $N_{M A X}^{A R}$ stands for the maximal number of arrivals planned on the considered horizon.

The graphical representation of an arrival module is proposed in Figure 16. At instant $t$, a node $A R_{t}$ is

![img-15.jpeg](img-15.jpeg)

Figure 16. Graphic representation of an 'arrival' module.

Table 10. CPT of an arrival node.


specified in relation to a node $A R_{t-1}$. Other variables prior to $A R_{t}$ are likely to be taken into account to characterise different probability distribution types. An 'arrival' module is integrated into the model through the connection to a variable $P E_{t}$ of an activity module. An arrival indeed leads to the activation of an activity input (available product).

An example of CPT for variables $A R_{t}$ is presented in Table 10. The CPT variable $A R_{t}$ is defined in the case where two system arrivals are forecast on the planning horizon. Parameters $\theta_{t}^{1}$ and $\theta_{t}^{2}$ correspond, respectively, to the arrival probabilities of the first and second end-of-life systems.

The different modules characterising the deconstruction option for each constituent of an end-of-life system have been described. They enable the representation of the different trajectories considering the uncertainties related to the dates of demand, to the dates of system end-of-life and to the duration of the activity.

### 4.3. Example of deconstruction policy determination

### 4.3.1. Presentation of the case

At the moment the model is being applied in the field of airplane recycling. Indeed in the next 4 years, 6500 aircrafts will have reached their end-of-life date and
![img-16.jpeg](img-16.jpeg)

Figure 17. System representation.
![img-17.jpeg](img-17.jpeg)

Figure 18. Model structure.
will have to be disassembled. The industrial partner is the company Tarmac Aerosave (Tarbes Advanced Recycling and Maintenance Aircraft Company). The illustration here concerns a small turbine (Figure 17). It is made up of five elements, namely $P 1$ (rotor blade), $P 2$ (drive train), $P 4$ (screwing device), a subassembly $S A 3$ (main body) and $P 7$ (nacelle).

We focus in particular on the deconstruction of subset $S A_{3}$ made up of elementary components $P_{3}$ (fixing elements), $P_{5}$ (crankcase) and $P_{6}$ (motor). Two options are possible for this subset. The first one consists in deconstructing $S A_{3}$ (deconstruction operation noted $D O_{4}$ ) and in valuating its components ( $P_{3}$, $P_{5}$ and $P_{6}$ ) through material recycling (named $R M_{1}$, $R M_{2}, R M_{3}$, respectively). The second option aims at valuating $S A_{3}$ by way of functional recycling (named $R F$ ). The dynamic model of the deconstruction trajectory for $S A_{3}$ is structured, as represented in Figure 18. The different variables and parameters are generated for each identified 'option' module.

In order to represent the decision-maker's action at the level of each product, decision nodes representing the deconstruction policy are introduced. They characterise the options to be selected for each of both end-of-life system arrivals forecasted on the

![img-18.jpeg](img-18.jpeg)

Figure 19. Deconstruction policy model.
planning horizon. For subset $S A_{3}$, the policy consists in choosing between:

- functional recycling for both systems (Policy $\mathrm{PL}_{1}$ ),
- functional recycling for the first system and dismantling for the second one (policy $\mathrm{PL}_{2}$ ),
- dismantling for both systems (Policy $\mathrm{PL}_{3}$ ).

The modelling objective is the determination of the policy to be selected according to an economical criterion characterising the expected profits. Each policy is described by the same type of costs and incomes introduced previously.

### 4.3.2. Model deployment

Within this framework, the deconstruction trajectory model of product $S A_{3}$ is given in Figure 19. A Matlab toolbox for Bayesian networks has been used. The different modules used so far are given. The 'policy' decision node represents the selection of an option for $S A_{3}$ by the decision maker. The node modalities correspond to the three possible policies foreseen in the previous section (the 'policy' domain is $\left\{\mathrm{PL}_{1}, \mathrm{PL}_{2}, \mathrm{PL}_{3}\right\}$ ). Its instantiation is realised when the decision maker selects a given policy in order to
proceed to its evaluation. In an optimisation context, the simulation result (calculation of the expected profit) is associated with each policy and the one which maximises the expected profit may be selected.

The CPT nodes $A_{t}\left(D O_{4}\right)$ and $A_{t}(R F)$ differ with respect to the selected policy. Indeed, the possible realisation number of both activities at a given time varies accordingly to the policy:

- For policy $\mathrm{PL}_{1}$ : two realisations may be undertaken for $A_{t}\left(R F_{2}\right)$ but none is possible for $A_{t}\left(D O_{4}\right)$.
- For policy $\mathrm{PL}_{2}$ : one realisation is likely to be carried out for each activity $A_{t}\left(R F_{2}\right)$ and $A_{t}\left(D O_{4}\right)$.
- For policy $\mathrm{PL}_{3}$ : two realisations are possible for $A_{t}\left(D O_{4}\right)$ and none is envisaged for $A_{t}\left(R F_{2}\right)$.

We have been simulating the model on 3000 periods of time by noting down at each instant $t$ the policy expected profit called $\operatorname{PRT}\left(\mathrm{PL}_{1}\right), \operatorname{PRT}\left(\mathrm{PL}_{2}\right)$, $\operatorname{PRT}\left(\mathrm{PL}_{3}\right)$. Numerical values used are presented in Table 11 by considering for the arrival module a first arrival at time $t=0$ and an uncertainty on the second arrival described by parameter $\theta_{k}^{2}$ with $\theta_{k}^{2}=0.001$.

The results are presented in Figure 20. The planning horizon starts at time $t=0$ and ends at $T_{h}$. First of

Table 11. Simulation parameters.


![img-19.jpeg](img-19.jpeg)

Figure 20. Simulation of expected profits for each deconstruction policy.
all, one can notice that whatever the planning horizon is considered, the $\mathrm{PL}_{3}$ policy makes lower profits than policies $\mathrm{PL}_{1}$ and $\mathrm{PL}_{2}$. On the other hand, the comparison between $\mathrm{PL}_{1}$ and $\mathrm{PL}_{2}$ depends on the horizon. Three types of planning horizons are identified:
(1) $T_{H}<855$ : both policies $\mathrm{PL}_{1}$ and $\mathrm{PL}_{2}$ can be considered as identical (in terms of expected profits).
(2) $855<T_{H}<2288$ : policy $\mathrm{PL}_{1}$ is 'better' than policy $\mathrm{PL}_{2}$.
(3) $T_{H}>2288$ : policy $\mathrm{PL}_{2}$ is 'better' than policy $\mathrm{PL}_{1}$.

Several comments have to be made about this case and the model used to perform it:
(1) The model is a useful guide for the decision maker to choose the best deconstruction options. Different policies can be evaluated that may eventually represent a big difference in term of profits.
(2) Like every modelling tool, the Bayesian networks however suffer some limitations. The first difficulty concerns the data to be introduced, which are not always easy to identify. Nevertheless, Bayesian networks offer the

possibility to combine a priori estimation with $a$ posteriori observation and learning principles which allow the model to be refined all along the system lifetime.
(3) The second difficulty may appear if the decision maker deals with a complex system made up of many components. At this level, the risk of combinatorial explosion is sizeable. If the analytical evaluation mode of the Bayesian networks makes a rapid assessment possible, the model definition may take long. Consequently, the model developed will have to be used at a decomposition level enabling the handling of a reasonable amount of components. This can be made by regrouping components and reusing the results as an input for the evaluation of the next level. However, this form of assessment may hide some optimal trajectories.

# 5. Conclusion 

We present in this article a model for the deconstruction trajectories planning within an uncertain context. By characterising the trajectory realisation mode, the objective was to assist the decision maker to evaluate and compare different policies for a given end-of-life system with several possible arrivals in the planning horizon. We have highlighted the events to be taken into account. They correspond to the end-of-life systems arrivals, to the realisation modes of the deconstruction activity and to the demand for the products likely to be obtained. For the decision maker, these events imply managing various situations corresponding to the validation or not of the valuation options, to the waiting for a demanded product and to the waiting for a product demand. The use of DBNs enabled the modelling of temporal evolution of variables characterising a deconstruction trajectory and the specification of uncertainties varying with time. The working perspectives are about the consideration of criteria other than the economic profit (valuation rate, ecological balance). Multi-criteria methods could be used to this end. The model introduced is based on various parameters (probabilities, costs...). They have to be determined after a preliminary analysis. The problem of obtaining these parameters has not been tackled in this article. It would thus be interesting to develop information management systems enabling this knowledge to be obtained. Eventually, the model developed in this article can be performed for the modelling of other industrial processes where the uncertainty level is high.
