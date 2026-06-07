# Tutorial 

## A Tutorial on Fire Domino Effect Modeling Using Bayesian Networks

Nima Khakzad (1)

## check for updates

Citation: Khakzad, N. A Tutorial on Fire Domino Effect Modeling Using Bayesian Networks. Modelling 2021, 2, 240-258. https://doi.org/10.3390/ modelling2020013

Academic Editor: Jürgen Pilz

Received: 7 March 2021
Accepted: 19 April 2021
Published: 22 April 2021

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## 0

Copyright: (c) 2021 by the author. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

School of Occupational and Public Health, Ryerson University, Toronto, ON M5B 1Z5, Canada; nima.khakzad@ryerson.ca


#### Abstract

High complexity and growing interdependencies of chemical and process facilities have made them increasingly vulnerable to domino effects. Domino effects, particularly fire dominoes, are spatial-temporal phenomena where not only the location of involved units, but also their temporal entailment in the accident chain matter. Spatial-temporal dependencies and uncertainties prevailing during domino effects, arising mainly from possible synergistic effects and randomness of potential events, restrict the use of conventional risk assessment techniques such as fault tree and event tree. Bayesian networks-a type of probabilistic network for reasoning under uncertainty-have proven to be a reliable and robust technique for the modeling and risk assessment of domino effects. In the present study, applications of Bayesian networks to modeling and safety assessment of domino effects in petroleum tank terminals has been demonstrated via some examples. The tutorial starts by illustrating the inefficacy of event tree analysis in domino effect modeling and then discusses the capabilities of Bayesian network and its derivatives such as dynamic Bayesian network and influence diagram. It is also discussed how noisy OR can be used to significantly reduce the complexity and number of conditional probabilities required for model establishment.


Keywords: domino effect; fire propagation; Bayesian network; noisy OR; decision making

## 1. Introduction

### 1.1. Approaches to Domino Effect Modeling

Domino effects are low probability, high-consequence events the modeling and safety assessment of which are challenging due to their uncertainty and complexity. The uncertainty in the modeling and analysis of domino effects is partly due to the rarity of domino effects and thus the insufficiency of data required for their quantitative assessments. And partly due to the randomness of potential events during domino effects, including the synergistic effects and mutual impact of events. Therefore, modeling of domino effects has been conducted largely under oversimplifying assumptions and by admitting high uncertainty of the outcomes [1,2]. Methods developed for domino effect modeling and risk assessment can generally be divided into analytical models, numerical models, and graphic models [2].

Analytical models [3-9] have been based on the prediction of escalation probabilities based on analytical relationships between heat flux and vulnerability of exposed units. Despite being simple and computationally affordable, the analytical models usually suffer from oversimplified assumptions, and most of them cannot seem to recognize the possibility of high-order domino effects or synergistic effects. This shortcoming not only may give rise to an underestimation of the potential risk but may lead to improper allocation of safety measures $[2,10]$.

Numerical modeling of fire and explosion [11-15] have greatly improved the accuracy of calculated heat fluxes and respective failure probability of exposed units. The past numerical studies of domino effects, which have mostly been based on applications of computational fluid dynamics (CFD) software such as Fire Dynamics Simulator are

computationally expensive and resource-demanding, limiting their applications only to very simple chemical facilities in terms of layout and variety of process units. Due to their deterministic syntax, numerical models should be combined with probabilistic techniques to cope with uncertainty embedded in the variables and escalation scenarios.

Graphic models have become very popular in recent years in modeling and analysis of domino effects mainly due to their structures, which can closely represent domino effects (the units of a chemical facility as the nodes of the graph and the escalation vectors as the arcs of the graph). That most graphic models are probabilistic is a bonus in modeling domino effects where uncertainties play a key role in estimating the escalation probabilities and scenarios. Approaches based on event tree [16,17], Bayesian network (BN) [10,18], event sequence diagram [19], Petri net [20,21], and graph metrics [22,23,24]. Among these graphic techniques, BN has proved as a robust technique for modeling domino effects due to its ability in considering uncertainties (as opposed to graph metrics), considering interdependencies and nonlinear interactions (as opposed to event tree) and performing probability updating (as opposed to Petri net). In the next section, the modeling advantages of BN over a conventional technique-event tree-are demonstrated via an example.

# 1.2. Bayesian Network vs. Conventional Techniques 

To make the discussion more concrete, consider three fuel storage tanks T1, T2, and T3, where a tank fire at T 1 as a primary event can spread to T2, T3, or both, leading to a domino effect (Figure 1). In that case, three different domino scenarios could be envisaged:
(1) The fire spreads from T1 to T2 (a level 1 domino effect: T1 $\rightarrow \mathrm{T} 2$ ). The heat fluxes radiating from fires at T 1 and T 2 can superimpose (known as synergistic effect) to cause damage to T3 and have the fire spread to it, resulting in a level 2 domino effect: $\mathrm{T} 1 \rightarrow \mathrm{~T} 2 \rightarrow \mathrm{~T} 3$.
(2) The fire spreads from T1 to T3 (a level 1 domino effect: T1 $\rightarrow$ T3). The heat fluxes radiating from fires at T 1 and T 3 may superimpose to cause damage to T2 via synergistic effect and have the fire spread to T2, resulting in a level 2 domino effect: $\mathrm{T} 1 \rightarrow \mathrm{~T} 3 \rightarrow \mathrm{~T} 2$.
(3) The fire spreads from T1 to both T2 and T3 almost simultaneously, resulting in a level 1 domino effect: $\mathrm{T} 1 \rightarrow \mathrm{~T} 2 \& \mathrm{~T} 3$
![img-0.jpeg](img-0.jpeg)

Figure 1. A tank farm consisting of three fuel storage tanks. Given a primary tank fire at T1, the possibility of fire spread to the other tanks has been denoted with arrows. The double-head arrow represents the uncertainty regarding the direction of fire spread between T2 and T3.

Moreover, for the sake of exemplification, assume that the fire spread probabilities (generally known as the escalation probabilities) have been calculated as $\mathrm{P}(\mathrm{T} 2=$ fire $\mid \mathrm{T} 1=$ fire, $\mathrm{T} 3=$ safe $)=0.4, \mathrm{P}(\mathrm{T} 2=$ fire $\mid \mathrm{T} 1=$ fire, $\mathrm{T} 3=$ fire $)=0.6, \mathrm{P}(\mathrm{T} 3=$ fire $\mid \mathrm{T} 1=$ fire, $\mathrm{T} 2=$ safe $)=0.3$, and $\mathrm{P}(\mathrm{T} 3=$ fire $\mid \mathrm{T} 1=$ fire, $\mathrm{T} 2=$ fire $)=0.5$.

Considering the event tree as one of the most popular QRA techniques for determining the outcome of an undesired event (initiating event), an analyst may develop the event tree in Figure 2a to identify both the sequence of fires given a fire at T1 and their probabilities while another analyst may choose to employ the event tree in Figure 2b.

![img-1.jpeg](img-1.jpeg)

Figure 2. Event tree analysis for identifying the sequence of events given a tank fire at T1. The sequence of the fires and the respective probabilities are given at the end of the event tree branches. The event trees are logically equivalent but structurally different: (a) T2 is considered as the first top event on the event tree. (b) T3 is considered as the first top event on the event tree.

As can be seen from Figure 2, even though both event trees are logically equivalent, they result in different probabilities for the same sequence of events. For instance, the probability of $\mathrm{P}(\mathrm{T} 1=$ fire, $\mathrm{T} 2=$ fire $)$ is calculated as 0.2 using the event tree in Figure 2a but 0.14 using the event tree in Figure 2b.

Further, in Figure 2a, the most probable sequence of events is identified as $\mathrm{T} 1 \rightarrow \mathrm{~T} 2 \rightarrow \mathrm{~T} 3$ with a respective probability of 0.2 while in Figure 2b the most probable sequence of events is $\mathrm{T} 1 \rightarrow \mathrm{~T} 3 \rightarrow \mathrm{~T} 2$ with a corresponding probability of 0.18 . As pointed out by Khakzad et al. [25], the reason for obtaining different probabilities for the same sequence of events by using conventional QRA techniques (here, event tree analysis) lies in the limitation of such techniques in considering all possible domino scenarios all at once. As a result, a modeler has no choice but to impose their subjective judgement as for which event tree to choose and thus overlooks the other possibilities.

Among the techniques used to model and assess the risk of domino effects [1,2], BN has been demonstrated to be able to more accurately identify the most probable sequence of events given accurate escalation probabilities. Advances in BN approaches and development of a variety of software for modeling and analysing BNs have enabled a more accurate dynamic risk assessment of domino effects [10,18]. Modeling features of BN and its derivatives facilitate the consideration of spatial-temporal dependencies of domino effects and make it possible to identify the most probable sequence of events in more accurately.

Figure 3 depicts a dynamic Bayesian network (DBN) model for modeling the previous domino effect scenarios given the fire at T1. The DBN allows the modeler to recognize the uncertainty embedded in the spread of fire between T2 and T3 via temporal arcs. Applications of BN and DBN to domino effect modeling are discussed in more detail in the next sections.
![img-2.jpeg](img-2.jpeg)

Figure 3. Application of DBN to domino effect modeling which may be initiated by a fire at T1. The uncertainty regarding the direction of fire spread between T2 and T3 is represented using two temporal arcs between T2 and T3, depending on which first catches fire.

Given the same escalation probabilities and taking advantage of probability updating aspect of the BNs, the probabilities of different scenarios are calculated as:

- $\mathrm{P}(\mathrm{T} 1 \rightarrow \mathrm{~T} 2 \rightarrow \mathrm{~T} 3)=0.14$, which is equal the one obtained in Figure 2b.
- $\mathrm{P}(\mathrm{T} 1 \rightarrow \mathrm{~T} 3 \rightarrow \mathrm{~T} 2)=0.0108$, which is equal to the one obtained in Figure 2a.
- $\mathrm{P}(\mathrm{T} 1 \rightarrow \mathrm{~T} 2)=0.28$ and $\mathrm{P}(\mathrm{T} 1 \rightarrow \mathrm{~T} 3)=0.18$, neither of which being equal to those obtained in Figure 2a,b.
- Unlike the event tree, which is incapable of calculating the probability of simultaneous fire spread from T1 to both T2 and T3, the developed DBN calculates such probability as $\mathrm{P}(\mathrm{T} 1 \rightarrow \mathrm{~T} 2 \& \mathrm{~T} 3)=0.12$.
Basics of the BN, DBN, and influence diagram are revisited in Section 2; applications of BN and DBN to domino effect modeling are illustrated in Section 3. In Section 4, applications of DBN and influence diagram to domino effect mitigation and risk management,

including optimal firefighting, are demonstrated. While Sections 3 and 4 are mainly based on the literature, Section 5 is relatively novel, discussing an innovative application of noisy OR to modeling complex domino effects. The work is concluded in Section 6.

# 2. Bayesian Networks 

### 2.1. Conventional Bayesian Network

A BN [26] is a probabilistic model $\mathrm{BN}=(\mathrm{G}, \emptyset)$ for reasoning under uncertainty, where G is the model structure in the form of a directed acyclic graph, and $\emptyset$ is the model parameters in the form of conditional probabilities required to quantify the model. G presents the conditional dependencies among the nodes (random variables) of the graph by means of directed arcs-drawn from the parent nodes to the child nodes-while the conditional probabilities assigned to the child nodes in the form of conditional probability tables (CPTs) determine the type of the dependencies. The nodes with no parents (known as root nodes) are assigned marginal probabilities.

BN takes advantage of the d-separation rule to simplify the joint probability distribution of its nodes. Figure 4 shows a typical BN, and considering the d-separation rule:

- in a serial connection as the one that consists of $\mathrm{X} 1, \mathrm{X} 2$, and $\mathrm{X} 5$, if the state of $\mathrm{X} 2$ is known, X 1 and X 5 become conditionally independent: $\mathrm{P}(\mathrm{X} 5 \mid \mathrm{X} 1, \mathrm{X} 2)=\mathrm{P}(\mathrm{X} 5 \mid \mathrm{X} 2)$;
- in a divergent connection as the one that consists of $\mathrm{X} 2, \mathrm{X} 4$, and $\mathrm{X} 5$, if the state of $\mathrm{X} 2$ is known, X 4 and X 5 become conditionally independent: $\mathrm{P}(\mathrm{X} 5 \mid \mathrm{X} 2, \mathrm{X} 4)=\mathrm{P}(\mathrm{X} 5 \mid \mathrm{X} 2)$;
- in a convergent connection as the one that consists of $\mathrm{X} 1, \mathrm{X} 2$, and $\mathrm{X} 3$, if the state of $\mathrm{X} 2$ is unknown, X 1 and X 3 become independent: $\mathrm{P}(\mathrm{X} 1 \mid \mathrm{X} 3)=\mathrm{P}(\mathrm{X} 1)$.
![img-3.jpeg](img-3.jpeg)

Figure 4. A generic Bayesian network.
The d-separation rule can be manifested as the Markovian property: Given its parents, a node becomes conditionally independent of all its non-descendants. For instance, $\mathrm{P}(\mathrm{X} 5 \mid \mathrm{X} 1, \mathrm{X} 2)=\mathrm{P}(\mathrm{X} 5 \mid \mathrm{X} 2)$ and $\mathrm{P}(\mathrm{X} 5 \mid \mathrm{X} 2, \mathrm{X} 4)=\mathrm{P}(\mathrm{X} 5 \mid \mathrm{X} 2)$. Satisfying the Markovian property, the joint probability distribution of the variables in a BN can be factorized as the product of the nodes' conditional probabilities given their immediate parents. Considering the BN in Figure 2: $\mathrm{P}(\mathrm{X} 1, \mathrm{X} 2, \mathrm{X} 3, \mathrm{X} 4, \mathrm{X} 5)=\mathrm{P}(\mathrm{X} 1) \mathrm{P}(\mathrm{X} 3) \mathrm{P}(\mathrm{X} 2 \mid \mathrm{X} 1, \mathrm{X} 3) \mathrm{P}(\mathrm{X} 4 \mid \mathrm{X} 2) \mathrm{P}(\mathrm{X} 5 \mid \mathrm{X} 2)$. In general:

$$
\mathrm{P}(U)=\prod_{i=1}^{n} \mathrm{P}\left(\mathrm{X}_{i} \mid \pi\left(\mathrm{X}_{i}\right)\right)
$$

where $U=\left\{\mathrm{X}_{1}, \mathrm{X}_{2}, \ldots, \mathrm{X}_{\mathrm{n}}\right\}$, and $\pi\left(\mathrm{X}_{i}\right)$ is the parent set of the node $\mathrm{X}_{i}$, and n is the number of the BN nodes.

The main application of BN is in probability updating. BN takes advantage of Bayes' theorem to update the probability of variables given new information-evidence E-to yield the updated (or posterior) probability:

$$
\mathrm{P}(U \mid E)=\frac{\mathrm{P}(U) \cdot \mathrm{P}(E \mid U)}{\mathrm{P}(E)}
$$

2.2. Dynamic Bayesian Network

A BN can be extended to a DBN to model the dynamic and temporal interdependencies embedded in the sequence of events. To form a DBN, a BN is usually replicated in time slices over a specific time period if the transitional probabilities between the sequential slices could be considered stationary (constant).

Figure 5 displays a two-slice DBN. The arc from X3 to its copy $\mathrm{X3}^{\prime}$ implies the temporal changes of X3 (e.g., aging of X3) while the arc from X5 to $\mathrm{X} 2^{\prime}$ may either indicate a reciprocal cause-effect relationship ( $\mathrm{X} 2 \rightarrow \mathrm{X} 5 \rightarrow \mathrm{X} 2$ ) or represent the uncertainty about the sequence of failures ( $\mathrm{X} 2 \rightarrow \mathrm{X} 5$ or $\mathrm{X} 5 \rightarrow \mathrm{X} 2$ ?). It is worth noting that neither of these modeling features can be accommodated in a conventional (static) BN. The joint probability distribution of the nodes of a DBN can be presented in the same way as in a conventional BN.
![img-4.jpeg](img-4.jpeg)

Figure 5. A generic DBN. The arc from X3 to its copy in the second time slice $\mathrm{X3}^{\prime}$ shows the temporal evolution of X3. The arcs from X2 to X5 to $\mathrm{X} 2^{\prime}$ may either represent the mutual impact of X2 and X5 or model the uncertainty as to whether X2 is the parent of X5 or the opposite.

# 2.3. Influence Diagram 

A BN can be extended to an influence diagram (Figure 6) using two additional types of nodes, i.e., decision and utility nodes [26]. In order to visually distinguish decision and utility nodes from chance nodes, decision nodes are conventionally displayed as a rectangle while utility nodes are presented as a diamond.
![img-5.jpeg](img-5.jpeg)

Figure 6. An influence diagram by adding decision node $D$ and a utility node $U$ to the Bayesian network.
Each decision node consists of a finite set of decision alternatives as its states. A decision node should be assigned as the parent of all those chance nodes whose probability distributions depend on at least one of the decision alternatives (e.g., X4 in Figure 6). Likewise, the decision node should be the child of all those chance nodes the states of

which have to be known to the decision maker before making that specific decision (e.g., X1 in Figure 6).

A utility node expresses the preferences of the decision maker as to the outcomes of the decision alternatives. Each utility node is attributed to a utility table in which the numbers are not probabilities (unlike CPT) but rather utility values (positive or negative) determined by the decision maker for each configuration of parent nodes, either decision nodes or chance nodes [26]. As a result, the decision alternative with the maximum expected utility can be selected as the optimal decision. Utility values are usually determined according to the preferences of the decisionmaker, expressing how much the decision maker prefers one outcome over another outcome.

# 3. Domino Effect Modeling 

### 3.1. Application of Bayesian Network

Khakzad et al. (2013) developed a methodology based on BN for modeling domino effects in process plants, presenting the process units as the nodes of the BN and the possibility of accident propagation among the adjacent nodes as the directed arcs of the BN. In their approach, the conditional probabilities assigned to the nodes were determined using dose-response relationships (probit functions) developed for estimating the damage probability of process units exposed to heat flux (in the event of fire) and shock wave (in the event of explosions) [8].

Given a primary fire or explosion at a process vessel, among two exposed vessels the one with the highest (conditional) escalation probability is chosen as the secondary unit which would be entailed in the chain of accidents. Considering the possible synergistic effects between the primary and secondary vessels, the sequence and the probabilities of tertiary and higher order vessels getting involved in the chain of accidents can be identified in the same way.

It should be noted that since the explosions are sudden and short-lived, the possibility of having multiple coincident explosions is very low, and thus the principle of synergy rarely applies to the explosions. In the event of fires, however, the possibility of concurrent fires is much higher: industrial fires such as tank fires, pool fires, and jet fires usually take a longer time to burnout (depending on the available fuel) or be suppressed, and thus it is more likely that the heat fluxes of contemporary fires can be superimposed, resulting in a synergistic effect.

The application of the BN-based methodology [10] to modeling domino effect can be demonstrated using a tank terminal consisting of five fuel storage tanks as shown in Figure 7a. Considering a primary tank fire at T2, the fire spread between the tanks can be modeled as the BN in Figure 7b.
![img-6.jpeg](img-6.jpeg)

Figure 7. Cont.

![img-7.jpeg](img-7.jpeg)
(b)

Figure 7. (a) A process plant consisting of five atmospheric storage tanks of gasoline, T1-T5. (b) Likely spread of fire given a primary fire at T 2 .

The arc from T 2 to T 3 denotes the possibility of fire spread from T 2 to T 3 with a certain probability, depending on the intensity of the heat flux T3 receives from T2 and the type of T3 (atmospheric or pressurized) and its dimension. Likewise, if T3 catches fire, the fire may spread to T4, indicated by the arc from T3 to T4.

As previously mentioned, the conditional escalation probabilities of type $\mathrm{P}(\mathrm{T} 3=$ fire $\mid \mathrm{T} 2=$ fire $)$ can be determined using dose-response relationships (probit functions). In this example, for illustrative purposes, let's assume that the escalation probabilities can be estimated as $\mathrm{P}_{i j}=1-\frac{15}{\mathrm{Q}_{\mathrm{ij}}}$, where $\mathrm{Q}_{\mathrm{ij}}$ is the intensity of the heat flux tank T j receives from fire at tank Ti. The numerator denotes the heat radiation threshold of $15 \mathrm{~kW} / \mathrm{m}^{2}$ required to cause damage to atmospheric storage tanks [8]. Assuming that the intensity of heat radiation each of the storage tanks may receive from an adjacent tank fire is $40 \mathrm{~kW} / \mathrm{m}^{2}$, the CPT of node T 3 given a tank fire at T 2 can be presented as Table 1, where $\mathrm{P}_{23}=1-\frac{15}{40}=0.63$. Since the tanks are identical and exposed to identical heat radiation intensity ( $40 \mathrm{~kW} / \mathrm{m}^{2}$ ), the same CPT can be assigned to all of them. (Except T2, which is the root node and needs a marginal probability table rather than a CPT).

Table 1. CPT of T3 given a tank fire at T2.


Implementing the BN in the Bayesian network modeling software, GeNIe [27], the probability of fire spread to each storage tank can be calculated as depicted in Figure 8. Rank ordering the units based on their marginal probabilities, T 1 and T 3 can be identified as the secondary units: $\mathrm{P}(\mathrm{T} 1=$ fire $)=\mathrm{P}(\mathrm{T} 3=$ fire $)=0.63 ; \mathrm{T} 4$ as the tertiary unit: $\mathrm{P}(\mathrm{T} 4=$ fire $)=0.39$, and T5 as the quaternary unit: $\mathrm{P}(\mathrm{T} 5=$ fire $)=0.24$. These probabilities make sense as the probability of a lower-order event (e.g., a secondary fire at T3) should be higher than the probability of a higher-order event (e.g., a tertiary fire at T4).
![img-8.jpeg](img-8.jpeg)

Figure 8. Modeling of fire domino using BN given a primary tank fire at T2.
The application of BN to domino effect modeling does not capture the uncertainty arising from different possible accident propagation paths. In the tank terminal in Figure 7, for instance, if there were two simultaneous primary fires at T2 and T5, two different BNs (Figure 9) could be developed to model the fire spread.

![img-9.jpeg](img-9.jpeg)

Figure 9. (a) BN for modeling domino scenario starting from T2 and T5 given that T3 catches fire before T4. (b) BN for modeling the same fire domino given that T4 catches fire before T3.

Having two BNs with the only difference in the direction of the arc between T3 and T4 makes it almost impossible to choose between these two BNs particularly that each BN results in different probabilities for the units. As for developing the CPTs, consider the BN in Figure 9a as an example: the CPTs of T1 and T3 are the same as Table 1, but the CPT of T4 is the same as Table 2 to account for the synergistic effect of T3 and T5 on T4. As such, $P(T 4=$ fire $\mid T 3=$ safe, $T 5=$ fire $)=1-\frac{15}{40}=0.63$ while $P(T 4=$ fire $\mid T 3=$ fire, $T 5=$ fire $)=$ $1-\frac{15}{40 \times 40}=0.81$.

Table 2. CPT of T4 in Figure 9a given the primary tank fires at T2 and T5.


Using the BN in Figure 9a, the probabilities can be calculated as displayed in Figure 10a. Rank ordering the units based on their marginal probabilities, T4 is identified as the secondary unit with a probability of $P(T 4=$ fire $)=0.74$, and both T 1 and T 3 as the tertiary units with an identical probability of $P(T 1=$ fire $)=P(T 3=$ fire $)=0.63$. This result, however, does not comply with the structure of the BN: Since T4 would catch fire as a secondary unit before T3 catches fire as a tertiary unit, the direction of the arc-which also implies the sequence of the fires-should be from T4 to T3 not the opposite, unlike what is shown in Figure 10a.
![img-10.jpeg](img-10.jpeg)

Figure 10. Counterintuitive results obtained for the application of conventional BN to domino effect modeling. (a) T3 has a lower probability, but the arc from T3 to T4 implies that T3 has caught fire before T4, and thus its probability should have been higher than that of T4. (b) T4 has a lower probability, but the arc from T4 to T3 implies that T4 has caught fire before T3.

This may make the modeler wonder if the BN in Figure 9b should have been chosen to model the right order of fires during the domino effect. Using the BN of Figure 9b, the

probabilities can be calculated as in Figure 10b; as can be seen, again the probabilities of the sequential fires do not comply with the sequence of the fires: structurally and considering the direction of the arcs, T4 seems to catch fire before T3 (note the arc from T4 to T3), however the fire probability at T3 (74\%) is higher than that of T4 (63\%), which means, T3 has caught fire before T4!

# 3.2. Application of Dynamic Bayesian Network 

As demonstrated in the previous section, the application of conventional BN to domino effect modeling may result (not always) in counterintuitive results (e.g., the probability of a secondary event is less than that of a tertiary event!) This is mainly because the conventional BN is not capable of considering all possible mutual interactions among the involved units, and thus the propagation paths are imposed by the modeler rather than being identified by the model. In other words, the modeler decides about the direction of arcs instead of letting the model identify the most probable path and subsequently align the direction of arcs [25].

Khakzad [18] modified the BN methodology previously developed by Khakzad et al. [10] by using a DBN, where the most likely sequence of events can be identified by the model by considering all the possible interactions among the units. In this regard, the uncertainty on the temporal sequence of T3 and T4 in Figure 9 can be modeled as the DBN in Figure 11. The arcs in color red denote the uncertainty as to whether the fire would spread from T3 to T4 or the opposite.
![img-11.jpeg](img-11.jpeg)

Figure 11. Modeling fire domino as a DBN given tank fires at T2 and T5. The arcs in color red denote the uncertainty as to whether the fire would spread from T3 to T4 or the opposite.

In Figure 11, the states of T2 and T5 in the first time slice have been instantiated to "fire" as $\mathrm{P}(\mathrm{T} 2(0)=$ fire $)=\mathrm{P}(\mathrm{T} 5(0)=$ fire $)=100 \%$, whereas the states of T1, T3, and T4 have been instantiated to "safe" as $\mathrm{P}(\mathrm{T} 1(0)=$ safe $)=\mathrm{P}(\mathrm{T} 3(0)=$ safe $)=\mathrm{P}(\mathrm{T} 4(0)=$ safe $)=100 \%$ as the initial evidence (observation) required to quantify the DBN. The CPTs of the nodes of the DBN in Figure 11 are similar to Tables 1 and 2. For the sake of clarity, the CPT of T3 in the 2nd time slice, i.e., T3(2), following the tank fires at T2 and T5 in the 0th time slice (the beginning of the modeling) is presented in Table 3.

As can be seen from Figure 11, the DBN results in identical probabilities of fire spread to T3 and T4 at sequential time steps due to the symmetrical position of T3 and T4 to the primary units T2 and T5. In the 1st time step, the probability of fire spread to T1, T3 and T4 is the same as 0.63 mainly because the DBN has not yet be given sufficient time to take into account all the possible fire interactions [25]. Given enough time, the probabilities of fire

spread to T3 and T4 are seen to be identical and slightly higher than that of T1. As such, either all the three tanks (T1, T3, T4) may catch fire as the secondary units in the 1st time step with a probability of 0.63 (this is the worst-case scenario) or T3 and T4 may catch fire before T1 in the 2nd time step.

Table 3. Conditional probability table of T3(2) given tank fires at T2(0) and T5(0).


The developed DBN can also be used to identify the most critical units contributing to the domino scenarios [24,28]. For this purpose, given an equal chance of primary fire for all the units at the 0th time slice ( 0.1 , for illustrative purposes) and considering the mutual interactions among all the units, the (marginal) probability of fire spread to each unit can be calculated as shown in Figure 12.
![img-12.jpeg](img-12.jpeg)

Figure 12. Temporal changes of fire spread probabilities given equal chances of fire $(p=0.1)$ for all the tanks at $\mathrm{t}=0$. Tank T3 has the highest probability of catching fire as time goes by and thus can be identified as the most critical (vulnerable) unit.

As can be seen, T3 has the highest probability of catching fire as time goes by and thus can be identified as the most critical (vulnerable) unit in the terminal. Khakzad and Reniers [28] demonstrated that the isolation of most vulnerable units from the chain of fires, for instance, via fireproofing or by keeping them empty, would dramatically disrupt the domino effect and thus reduce the vulnerability of the facility more than would the isolation of any other tanks.

# 4. Domino Effect Mitigating 

### 4.1. Modeling of Add-On Fire Protection Systems

Fire protection systems such as sprinkler systems, water deluge systems, and fireproofing are commonly known as add-on safety systems and are used in the chemical

and process plants to prevent, control, and mitigate domino effects. Sprinkler systems are typically installed on atmospheric tanks to mitigate the radiating heat in case of burning tanks or to reduce the absorbed heat in case of exposed tanks. Water deluge systems have a similar function but are typically installed on pressurized vessels. A fireproof coating is usually applied to pressurized vessels and is aimed at reducing the absorbed heat for a limited amount of time.

In this section we demonstrate how the impact of add-on fire systems on domino effects can be modeled via DBN. Interested readers may refer to [29] for a more detailed modeling of different types of fire protection systems in BN and DBN. Consider a generic add-on safety system (B) which has been installed on T2 to suppress fire at T2, which would also mitigate the heat T1 and T3 would receive from T2. To model the safety system in the DBN, assume that:

- B has three states: Active, No-active (idle), and Failed.
- By default, B is in the no-active state but can be activated with a certain probability (1-PFD) if T2 catches fire. PFD is B's probability of failure on demand.
- When activated, B may still fail with a constant failure rate $\lambda$ (this assumption can easily be relaxed if need be), resulting in an exponential failure probability of $\mathrm{P}_{\mathrm{B}}=1-\mathrm{e}^{-\lambda \mathrm{t}}$, where $t$ is the time lapse since the activation of $B$.
- Once activated and put into operation, B will mitigate the emitting heat from T 2 with a factor $(\alpha<1)$ as $Q_{m}=\alpha . Q_{o}$ so that the possibility of damage to adjacent tanks (T1 and T3) and hence the probability of fire spread to them can be reduced. $Q_{m}$ is the mitigated heat emitted from T 2 given that B is active; $Q_{o}$ is the original heat emitted from T 2 before the activation of B , and $\alpha$ is the mitigating factor.
- B, if successfully activated and keep operating, may extinguish the fire with a certain probability $\mathrm{P}_{\mathrm{e}}$.
- B cannot be repaired. Thus, once it fails it remains in the failed state throughout the modeling.
- As soon as T2 is extinguished, B is back to the idle state (no_active). This assumption has been made for simplification. In reality, B keeps working for a while to ensure T2 does not reignite.
Considering the exemplary values of $\mathrm{PFD}=0.1, \mathrm{P}_{\mathrm{B}}=0.05\left(\lambda=0.1 \mathrm{hr}^{-1}\right.$, and $\left.\mathrm{t}=30 \mathrm{~min}\right)$, $\alpha=0.5$, and $\mathrm{P}_{\mathrm{e}}=0.2$ for B , the fire spread from T 2 to T 1 can be modeled using the DBN in Figure 13. The CPTs of the barrier at the 0th and 1st time slices are presented in Tables 4 and 5, respectively.
![img-13.jpeg](img-13.jpeg)

Figure 13. Modeling the impact of safety system (B) on the fire spread from T2 to T1.

Table 4. Conditional probability table of the safety system at the 0th time slice, $\mathrm{B}(0)$.


Table 5. Conditional probability table of the safety system at the 1st time slice, $B(1)$.


For the sake of clarity, the CPTs of T1 and T2 at the 1st time slice have been presented in Tables 6 and 7. In Table 6, $\mathrm{P}(\mathrm{T} 1(1)=$ fire $\mid \mathrm{T} 1(0)=$ safe, $\mathrm{T} 2(0)=$ fire, $\mathrm{B}(0)=$ active $)=$ $1-\frac{15}{\mathrm{Q}_{\mathrm{sc}}}=1-\frac{15}{0.5-40}=0.25$. To see the impact of B on the fire escalation of T 2 and T 1 , their fire probabilities with and without the impact of B have been compared in Figure 14a,b.

Table 6. Conditional probability table of T1 at the 1st time slice, T1(1).


Table 7. Conditional probability table of T2 at the 1st time slice, T2(1).


![img-14.jpeg](img-14.jpeg)

Figure 14. (a) Evolution of the temporal probabilities of (a) T2 and (b) T1, with and without the impact of the safety system.

# 4.2. Modeling of Firefighting 

Firefighting plays a key role in preventing or delaying fire spread. The role of firefighting becomes even more important considering the possibility of damage or malfunction of add-on safety systems [29] or insufficient firefighting resources [19,30,31]. The effectiveness of firefighting strongly depends on the number, skills and the level of preparedness of firefighting crews as well as the amount and the type of firefighting equipment.

When the amount of firefighting crews and required equipment are sufficient, a firefighting team can deal with all the burning and exposed vessels to stop or reduce the possibility of fire spread and thus prevent further damage. However, the main challenge arises when the number of vessels in danger-both on fire and exposed to fire-exceeds the available firefighting resources (staff, equipment, etc.). Accordingly, setting optimal firefighting strategies to identify which burning vessels to suppress and which exposed vessels to protect can become challenging due to limited resources [31].

Industrial firefighting strategies can be (i) passive, in which the burning vessels are left to burn out without any intervention (usually in case of jet fires), (ii) defensive, in which the exposed vessels are cooled mainly using water, or (iii) offensive, where attempts are made to extinguish burning vessels using water-based foam.

During an offensive strategy, the emitted heat from a burning vessel that is under extinguishment will gradually decrease until the fire is completely suppressed. Ignoring the temporal variation, the mitigated heat radiation $\left(\mathrm{Q}_{\mathrm{m}}\right)$ can be taken as a fraction $(0<\alpha<1)$ of the original heat radiation $\mathrm{Q}_{\mathrm{m}}=\alpha \times \mathrm{Q}_{\mathrm{o}}$; the lower the $\alpha$, the higher the efficiency of extinguishment. Likewise, during a defensive strategy, the reduced amount of heat received by an exposed vessel $\left(Q_{c}\right)$ can be taken as a fraction $(0<\beta<1)$ of the original heat $Q_{c}=\beta \times Q_{o}$; the lower $\beta$, the higher the efficiency of cooling. As a result, in a mixed strategy, the reduced amount of heat a protected vessel would receive from a burning vessel under suppression would be $\mathrm{Q}_{\mathrm{mc}}=\alpha \times \beta \times \mathrm{Q}_{\mathrm{o}}$.

Consider the same tank terminal in Figure 7a. Assume a case where a fire at T2 has already spread to T3 by the time the firefighters deploy their resources. Further, assume that available resources do not allow the firefighters to work on more than two tanks at a time. As only two tanks can be included in the firefighting endeavor, six strategies can be considered for firefighting as listed in Table 8. Moreover, to account for the possible inefficiency of firefighting, consider these firefighting efficiencies: $\alpha=0.4$ and $\beta=0.7$.

Figure 15 displays the escalation of fire from T2 and T3 to the other tanks. For the sake of clarity, the CPT of node T4 given the fire at T3 is presented in Table 9.

Table 8. Firefighting strategies given fires at T2 and T3.


![img-15.jpeg](img-15.jpeg)

Figure 15. Influence diagram to identify optimal firefighting strategies given fires at T2 and T3. (These two nodes have been highlighted with color yellow). The dotted arcs from T2 and T3 to the decision node "firefighting" imply that the optimal firefighting strategy is identified given the observation of fire at T2 and T3.

Table 9. Conditional probability table of T4 in Figure 15.


As can be noted, the BN has been converted into an influence diagram by adding the decision node "Firefighting" and the utility node "Loss". The node "Firefighting" incorporates the six firefighting strategies listed in Table 8 as the decision alternatives. The effect of the decision policies on the nodes can be reflected by making modifications to the nodes' conditional probability tables (escalation probabilities). The procedure for modifying the conditional probability table of T 4 under the influence of the decision node is presented in Table 10.

Table 10. Conditional probabilities of T4 given fire at T3 and different firefighting strategies for $\alpha=0.4$ and $\beta=0.7$ and. $\mathrm{Q}_{34}$ is the heat flux T 4 receives from T3.


(a) $\mathrm{P}(\mathrm{T} 4=$ Fire $\mid \mathrm{T} 3=$ Fire, $\mathrm{d} 1)=1-\frac{15}{0.4 \times 40}=0.06$.
(b) Since the amount of $\mathrm{Q}_{34}$ is below the threshold $\left(0.4 \times 0.7 \times 40=11.2<15 \mathrm{~kW} / \mathrm{m}^{2}\right)$, it would not cause damage and fire spread to T4.

In Figure 15, the utility node "Loss" has been connected to the still safe storage tanks, T1, T4, and T5, so that only further damage caused from the spread of fire from T2 and T3 can be taken into account in the decision making. Since the storage tanks are identical, any damaged storage tank is assumed to be associated with a loss value of -10 . For example, $\mathrm{U}(\mathrm{T} 1=$ Fire, $\mathrm{T} 4=$ Fire, $\mathrm{T} 5=\mathrm{Safe})=-20$.

Modeling the influence diagram in GeNIe [27], the expected loss of firefighting strategies can be calculated and used to make a comparison among the firefighting strategies in Figure 16. The strategy attributed with the lowest loss, i.e., d1 in this case, can be selected as the optimal strategy. A more complicated application of dynamic influence diagrams to optimal firefighting can be found in [31].
![img-16.jpeg](img-16.jpeg)

Figure 16. Comparison of firefighting strategies based on their expected loss.

# 5. Application of Noisy-OR 

As previously demonstrated, DBN can be used as a robust technique in modeling domino effects by identifying the most contributing events and the sequential entailment of the events in the chain of accidents. Compared to ordinary BN, DBN provides the modeler with much more flexibility in modeling interdependencies both spatially and temporally, which is not feasible in an ordinary BN. However, some modeling issues still need to be addressed to enhance the performance of DBN and increase the accuracy or the results.

The notion of synergistic effects during fire domino effects refers to the confluence of concurrent fires on a target unit. This, in turn, may lead to an exponential growth of the conditional probability table of the target unit as the number of concurrent fires in the vicinity of the unit increases. For example, consider a different but still simple arrangement of tanks T1-T4 in Figure 17, where a burning tank can radiate the heat flux $40 \mathrm{~kW} / \mathrm{m}^{2}$ to the other tanks.

Considering the mutual interactions and possible synergistic effects and only two states for each node (safe, fire), 15 probabilities should be identified for the CPT of T3. Such probabilities are in the form of, for instance:

$$
\mathrm{P}\left(\mathrm{~T} 3^{\mathrm{t}+1}=\text { fire } \mid \mathrm{T} 3^{\mathrm{t}}=\text { safe, } \mathrm{T} 1^{\mathrm{t}}=\text { fire, } \mathrm{T} 2^{\mathrm{t}}=\text { safe, } \mathrm{T} 4^{\mathrm{t}}=\text { fire }\right)=1-\frac{15}{40+0+40}=0.813
$$

![img-17.jpeg](img-17.jpeg)

Figure 17. A hypothetical tank arrangement. Heat fluxes $\left(\mathrm{kW} / \mathrm{m}^{2}\right)$ radiated from and absorbed by the adjacent tanks in case of tank fires are denoted on the arrows.

The size of the CPTs can readily grow out of hand and become intractable for a more complex arrangement of the units. To alleviate the exponential growth of the CPTs due to synergistic effects of simultaneous fires, the Noisy-OR technique can be employed. (Noisy-OR was first proposed by Khakzad et al. [10] to account for the leak probabilityprobability of a unit catching fire during a domino accident due to other unknow reasons than fire spread from adjacent units, for instance, self-ignition of the unit.)

The Noisy-OR takes advantage of causal independency to reduce the number of required conditional probabilities from $2^{\mathrm{m}}-1$ to m , where m is the number of binary parents of the child node. The Noisy-OR model is only applicable to binary variables as a special case of a more general Noisy-MAX model, which is applicable to multi-state variables.

The Noisy-OR model requires all the causes (parents) of an effect (child node) be present in the BN, where each cause $\left(C_{i}\right)$ is capable of causing the effect (e) with a respective probability as:

$$
\mathrm{P}_{i}=\mathrm{P}\left(\mathrm{e}=\text { true } \mid \mathrm{C}_{1}=\text { false }, \mathrm{C}_{2}=\text { false }, \ldots, \mathrm{C}_{i}=\text { true }, \mathrm{C}_{i+1}=\text { false }, \ldots \mathrm{C}_{n}=\text { false }\right)
$$

As such, the probability of the effect given any combination of its active causes can be calculated as:

$$
\mathrm{P}(\mathrm{e} \mid \mathrm{C})=1-\prod\left(1-\mathrm{P}_{i}\right)
$$

where C is the active causes. Thus, when all the causes of the effect are false:

$$
\mathrm{P}\left(\mathrm{e} \mid C_{1}=\text { false }, C_{2}=\text { false }, \ldots, C_{n}=\text { false }\right)=0
$$

Since $\mathrm{P}\left(\mathrm{T} 3^{\mathrm{t}+1}=\right.$ fire $\left|\mathrm{T} 1^{\mathrm{t}}=\text { fire }\right)=\mathrm{P}\left(\mathrm{T} 3^{\mathrm{t}+1}=\right.$ fire $\left|\mathrm{T} 4^{\mathrm{t}}=\text { fire }\right)=1-\frac{15}{40}=0.625$, using the Noisy-OR model, the foregoing conditional probability of $\mathrm{T} 3^{\mathrm{t}+1}$ can be calculated as:
$\mathrm{P}\left(\mathrm{T} 3^{\mathrm{t}+1}=\right.$ fire $\left|\mathrm{T} 3^{\mathrm{t}}=\right.$ safe, $\left.\mathrm{T} 1^{\mathrm{t}}=\right.$ fire, $\left.\mathrm{T} 2^{\mathrm{t}}=\right.$ safe, $\left.\mathrm{T} 4^{\mathrm{t}}=\text { fire }\right)=1-(1-0.625)(1-0.625)=0.859$. As can be seen, the conditional probability of $\mathrm{T} 3^{\mathrm{t}+1}$ which is calculated using the Noisy-OR model, i.e., 0.859 , is in good agreement with the one calculated without the Noisy-OR model, i.e., 0.813 .

Figure 18 displays the fire spread probabilities of the tanks, in which the probabilities calculated for T3 with and without the Noisy-OR model are identical.

![img-18.jpeg](img-18.jpeg)

Figure 18. Fire spread probabilities with and without Noisy-OR model given equal probabilities of fire ( 0.1 ) at the 0th time slice. The probabilities of T1, T2, and T4 grow equally due to their symmetrical position to one another.

# 6. Conclusions 

In the present study, we exemplified some applications of the BN, DBN, and influence diagram in the modeling of fire domino effects. It was illustrated that even for a very simple case study, the application of conventional QRA techniques such as event tree analysis can result in misleading and inconsistent probabilities and chains of accidents.

On the other hand, the BN and particularly DBN were shown to result in more consistent results by considering complicated spatial-temporal interdependencies and uncertainties, which cannot be considered in the event tree analysis. Despite offering a great deal of flexibility and robustness in modeling and reasoning, the application of DBN to highly dynamic and complex domino scenarios may nevertheless result in intractable conditional probability tables (CPTs), which can be too large to handle. This issue, however, was demonstrated to be greatly alleviated via the application of the Noisy-OR model. Nevertheless, the application of Noisy-OR to developing the CPTs still needs further verification via more complex and larger case studies before it can be reliably used for this purpose. Another research topic which is worth investigating in the future studies is the application of dynamic influence diagrams-as an extension of DBN-to dynamic decision making and risk management of domino effects. The models discussed in the present study can readily be extended to modeling and risk management of other types of cascading effects in a variety of systems or infrastructures provided that they can be modeled as networks.

Funding: This research received no external funding.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Conflicts of Interest: The author declares no conflict of interest.
