# LJMU Research Online 

Uğurlu, Ö, Yıldız, S, Loughney, S, Wang, J, Kuntchulia, S and Sharabidze, I
Analyzing Collision, Grounding, and Sinking Accidents Occurring in the Black Sea Utilizing HFACS and Bayesian Networks.
http://researchonline.ljmu.ac.uk/id/eprint/13461/

## Article

Citation (please note it is advisable to refer to the publisher's version if you intend to cite from this work)

Uğurlu, Ö, Yıldız, S, Loughney, S, Wang, J, Kuntchulia, S and Sharabidze, I (2020) Analyzing Collision, Grounding, and Sinking Accidents Occurring in the Black Sea Utilizing HFACS and Bayesian Networks. Risk Analysis. ISSN 0272-4332

LJMU has developed LJMU Research Online for users to access the research output of the University more effectively. Copyright © and Moral Rights for the papers on this site are retained by the individual authors and/or other copyright owners. Users may download and/or print one copy of any article(s) in LJMU Research Online to facilitate their private study or for non-commercial research. You may not engage in further distribution of the material or use it for any profit-making activities or any commercial gain.

The version presented here may differ from the published version or from the version of the record. Please see the repository URL above for details on accessing the published version and note that access may require a subscription.

For more information please contact researchonline@ljmu.ac.uk

# Analysing of Collision, Grounding and Sinking Accident Occurring in the Black Sea Utilizing HFACS and Bayesian Networks 

Özkan Uğurlu ${ }^{1 *}$, Serdar Yıldız ${ }^{2}$, Sean Loughney ${ }^{3}$, Jin Wang ${ }^{3}$, Shota Kuntchulia ${ }^{4}$, Irakli Sharabidze ${ }^{4}$<br>${ }^{1}$ Maritime Transportation and Management Engineering Department, Ordu University, Ordu, Turkey.<br>${ }^{2}$ Maritime Transportation and Management Engineering Department, Karadeniz Technical University, Trabzon, Turkey.<br>${ }^{3}$ Liverpool Logistics, Offshore and Marine (LOOM) Research Institute, Faculty of Engineering and Technology, Liverpool John Moores University, Liverpool, UK.<br>${ }^{4}$ Batumi State Maritime Academy, Batumi, Georgia.<br>*Address correspondence to Özkan Uğurlu, Maritime Transportation and Management Engineering Department, Ordu<br>University, Ordu, Turkey; tel:+90 50581798 39; ozkanugurlu24@hotmail.com; ougurlu@odu.edu.tr.

## ABSTRACT

This study examines and analyses marine accidents that have occurred over the past 20 years in the Black Sea. Geographic Information System (GIS), Human Factor Analysis and Classification System (HFACS) and Bayesian Network (BN) models are used to analyse the marine accidents. The most important feature that distinguishes this study from other studies is that this is the first one to analyse accidents that have occurred across the whole Black Sea. Another important feature is the application of a new HFACS structure to reveal accident formation patterns. The results of this study indicate that accidents occurred in high concentrations in coastal regions of the Black Sea, especially in the Kerch Strait, Novorossiysk, Kilyos, Constanta, Riva and Batumi regions. The formation of grounding and sinking accidents has been found to be similar in nature, with the use of inland and old vessels being highlighted as important factors regarding sinking and grounding incidents. However, the sequence of events that lead to collision-contact accidents differs from those events which form grounding and sinking accidents. This study aims to provide information to the maritime industry regarding the occurrence of maritime incidents in the Black Sea, in order to assist with accident reduction and prevention.

KEY WORDS: GIS, HFACS, Bayesian network, accident analysis, marine accident, Black Sea.

## 1. INTRODUCTION

The Black Sea has coastlines in Turkey, Russia, Ukraine, Romania, Bulgaria and Georgia, and is contained by these coastlines, with access to the open sea available through the Straits of Istanbul and Canakkale. These straits are very busy waterways, with 42553 ships having entered

or exited the Black Sea in 2016 (DTGM, 2017). In addition to this number, it can be seen that the Black Sea has a vessel density that cannot be underestimated when one also considers the traffic of fishing vessels and the volume of ships that only operate within the confines of the Black Sea. Accidents that have occurred in the Black Sea threaten not only safety of life and property but also the environment and marine ecosystem.

Marine accidents, especially in terms of sinking, grounding and collision-contact, have always been a major concern. Many accident analysis studies have been conducted in literature in order to understand the causes of these accidents and to prevent them from occurring in the future. In light of these studies the main causes of collision-contact accidents can be listed as: violation of International Regulations for Preventing Collisions at Sea (COLREG), inappropriate lookout, ineffective use of bridge navigation equipment, poor visibility, heavy traffic, darkness, and communication and coordination errors between vessels and bridge team members (Kujala et al., 2009, Montewka et al., 2012, Chauvin et al., 2013, Uğurlu et al., 2015b, Uğurlu et al., 2015c, Yıldırım et al., 2017). Similarly, some identified causes of grounding accidents include: improper passage planning, position fixing errors, interpretation error of conning officer, lack of coordination and communication of bridge team members, inappropriate chart usage, fatigue, and heavy weather and sea conditions (Mullai and Paulsson, 2011, Uğurlu et al., 2015b, Uğurlu et al., 2015c, Uğurlu et al., 2015d, Yıldırım et al., 2017). Finally, in the literature, the number of accident analysis studies relating to sinking accidents appears to be less than the number relating to groundings, and collision-contact accidents. However, it is possible to identify some of the main factors that contribute to sinking accidents as; improper cargo stowage and ship stability, deformed hull structure, and heavy weather and sea conditions (Soares and Teixeira, 2001, Uğurlu et al., 2015a).

Accident analysis studies, based on accident investigations, make it possible to understand the causes of an event or accident, in order to prevent the occurrence of such accidents and to provide improved safety (Doytchev and Szwillus, 2009, Uğurlu et al., 2015a). Several analytical and evaluation methods have been developed to analyse accident data to further improve maritime safety. These include Event Tree Analysis (ETA), Fault Tree Analysis (FTA), The Decision-Making Trial and Evaluation Laboratory (DEMATEL), Analytical Hierarchy Process (AHP), Geographic Information System (GIS) (Uğurlu and Yıldız, 2016), Fuzzy-AHP, Human Factor Analysis and Classification System (HFACS) and Bayesian Network (BN) (Sklet, 2004, Trucco et al., 2008, Matellini et al., 2013, Mentes et al., 2015, Uğurlu et al., 2015b). In this study, HFACS models whose reliability has been proven by many studies are used to analyse marine accidents that have occurred in the Black Sea (Shappell and

Wiegmann, 2004; Wiegmann et al., 2005) and BN (Guikema and Goffelt, 2008; Jones et al., 2010; Cai et al., 2013).

# 2. BACKGROUND 

### 2.1. HFACS

In the Swiss cheese model, accidents are defined as occurrences that cause undesirable consequences, resulting from discrepancies and disturbances between the components of the system (Reason et al., 1990). In the Swiss cheese model, the events that caused the accident are defined on four levels and these four levels are grouped under two main headings; latent factors and active failures. The first three levels represent latent factors and the last level represents active failures. According to this model, there are hidden (latent) factors behind visible (active) failures within an accident, as shown in Figure 1 (Reason et al., 2006).
![img-0.jpeg](img-0.jpeg)

Figure 1. Swiss cheese model

According to Reason's model, accidents occur because of deficiencies in the first three levels paving the way for unsafe acts in the fourth level, i.e., the unsafe acts and behaviours of operators. Latent factors in the system are often unnoticed until the accident occurs. The Human Factors Analysis and Classification System HFACS is a hybrid method, containing human factors and system approaches, as well as integrating Reason's Swiss Cheese model (Reason, 2000; Shappell and Wiegmann, 2000; Uğurlu et al., 2018). HFACS is a useful tool for analysing the effects of human error on devastating events, accidents, dangerous events, and deficiencies in different sectors (Patterson, 2008, Baysari et al., 2008, Patterson and Shappell, 2010, Lenne et al., 2012, Chauvin et al., 2013, Chen et al., 2013, Zhan et al., 2017, Theophilus et al., 2017, Uğurlu et al., 2018).

In many studies carried out with HFACS, revisions were needed within the main structure. In studies conducted by many researchers such as Reinach and Viale (2006), Chen et al., (2013) and Chauvin et al., (2013), changes were made to the main HFACS structure and the structure was adapted to the stated field of application. The latest change in the HFACS structure for the analysis of marine accidents was made by Uğurlu et al., (2018). In their research, the HFACS structure was modified to make it more suitable for analysis of marine accidents by revising the main categories and sub-categories in their study.

In this structure (Uğurlu et al., 2018), the operational conditions (environmental factors) level has been added to the main HFACS structure and evaluated as the last step in the occurrence of marine accidents. Operational conditions include internal (e.g. rudder failure) and external (e.g. restricted visibility) factors that are closely related to the accident, but which cannot be prevented directly by the ship's personnel. For marine accidents that have occurred in the Black Sea and considering the occurrence of the accidents, it would not be appropriate to examine the operational conditions under pre-conditions for unsafe acts. Therefore, operational conditions are not considered as pre-conditions for unsafe acts in accident occurrence, they are to be considered as top-level events. In other words, even if the necessary conditions for the accident occur simultaneously, an accident will not occur unless the appropriate operational conditions occur. From past to the present, in none of the HFACS structures have the accident occurrences been evaluated in this way. For the reasons mentioned above, the new HFACS structure for Passenger Vessels (HFACS-PV) is the most accurate way to describe marine accidents. Therefore, in this study, the new HFACS structure is deemed suitable for the analysis of marine accidents in the Black Sea. The HFACS structure applied in this paper is shown in Figure 2 (Uğurlu et al., 2018).

![img-1.jpeg](img-1.jpeg)

Figure 2. General framework of HFACS structure used in this study

# 2.2. Bayesian Networks 

Bayes' theorem is a conditional probabilistic approach arising from the concept of subjective probability. The Bayesian model or the probabilistic Directed Acyclic Graph (DAG) model yields a network model (Bearfield and Marsh, 2005, Hänninen, 2008, Brooker, 2011, Pristrom et al., 2016). In other words, BN models express a network model with a set of variables that have conditional dependencies among each other. When constructing a BN, it is important to note that the number of permutations in the Conditional Probability Tables (CPTs) increases exponentially with the number of parent nodes and the number of states in the CPT. Similarly, the total number of cells in a CPT is equal to the product of the possible number of states in the node and the number of combinations of parental states (Cai et al., 2014; Fenton and Neil, 2013; Loughney and Wang, 2017).

Conditional probabilities are essential to BNs and they can be expressed by statements such as " $B$ occurs given that $A$ has already occurred" and "given event $A$, the probability of event $B$ is ' $p$ '", which is denoted by $P(B \mid A)=p$. This specifically means that if event A occurs and everything else is unrelated to event $B$ (except event $A$ ), then the probability of B is ' p ' (Eleye-Datubo et al., 2006, Matellini et al., 2013, Fenton and Neil, 2013, Pristrom et al., 2016). Conditional probabilities are part of the joint probability of the intersection of $A$ and $B, P(A \cap B)$, and can be shown as:

$$
P(A \mid B)=P(A \cap B) / P(A)
$$

For any two events A and B:

$$
P(A \cap B)=P(B \mid A) \times P(B)=P(A \mid B) \times P(A)
$$

It should be noted that if $P(A)=0$, then $A$ is an event with no possible outcomes. Therefore, it follows that $A \cap B$ also contains no possible outcomes and $P(A \cap B)=0$. The independence of events can be shown by definition. Let $A$ and $B$ be any events with $P(A) \neq 0$ then $A$ and $B$ can be defined through Equation 4:

$$
P(B)=P(B \mid A)
$$

Similarly, from Equation 4 one can define Equation 5:

$$
P(A \cap B)=P(A) \times P(B)
$$

All of these possibilities are specified in the CPTs by evaluating the relevant parent nodes for each child node. If the node is not a child node, then the initial probability values are specified in the Non-Conditional Probability Table (NCPT) (Pristrom et al., 2016). Determining the probabilities of parent nodes, root nodes and child nodes is very important for the results of the study (Li et al., 2014, Pristrom et al., 2016).

# 3. METHODOLOGY 

This study is an accident analysis that examines marine accidents that have occurred in the Black Sea, over the past 20 years. In this context, a total of 5,655 marine accidents recorded in Global Integrated Shipping Information System (GISIS) were scrutinized, and a total of 109 accidents were deemed to have occurred in the Black Sea. In this study, only grounding, sinking, collision-contact accidents were investigated ( 89 of 109 accidents). This is the first study that analyses the accidents that have occurred in the entire Black Sea area as a collective. This study is aims to provide information to the maritime industry regarding marine accidents that have occurred in the Black Sea in order to mitigate against the occurrence of similar accidents in the future. The flow chart in Figure 3 summarizes the stages of this study. The steps of the methodology in this study are outlined as follows:

![img-2.jpeg](img-2.jpeg)

Figure 3. Flow chart of the study

Step 1 - Gathering the accident data and choosing the appropriate method for accident analysis: The dataset of this study is limited to serious and very serious accidents that have occurred in the Black Sea. A very serious marine casualty involves the total loss of the ship or a death or severe damage to the environment (IMO, 2008). A serious marine casualty results in immobilization of main engines, extensive accommodation damage, severe structural damage, rendering the ship unfit to proceed, pollution or a breakdown necessitating towage or shore assistance (MAIB, 2013).

Accident reports recorded in GISIS, European Maritime Safety Agency (EMSA), Accident Investigation Board (Turkey), Maritime Accident Investigation Bureau (Georgia), Marine Accidents Investigation Department (Romania), Maritime and Railway Accident Investigation (Bulgaria) and Lloyd's Register databases are used to obtain detailed information about these accidents. By scrutinizing these databases, a new database is created by using Microsoft Excel, where there are many items such as accident type, ship type, gross tonnage,

ship size, accident coordinates, and date and time of the accident. With the new database created, examination and interpretation of the accidents have become easier.

An appropriate method is chosen for both qualitative and quantitative analysis of accidents in the Black Sea by taking into account accident reports, accident analysis studies, and qualitative and analytical models used in accident analysis. In order to analyse accident reasons in the Black Sea, HFACS (qualitative) and BN (both qualitative and quantitative) methods, which are widely used in many accident analysis studies, have been chosen.

Step 2 - Spatial analysis of accident data: ArcGIS 10.3 is used for spatial analysis of accidents in the Black Sea. Firstly, accident coordinates in the MS Excel GIS database are digitized. Secondly, digitized accident coordinates and accident information were transferred to ArcGIS 10.3. Thirdly, the marine accident data is overlaid on a map of the Black Sea and evaluated. In this stage, accidents that have occurred in the Black Sea are analysed by spatial density analysis (kernel density estimation) using ArcGIS 10.3. In this regard, hot spots where marine accidents have occurred, have been identified to determine the high-risk areas of the Black Sea, in terms of navigation.

Step 3 - Identification of accident reasons and classification under the HFACS structure: In order to better understand and interpret the occurrence of marine accidents, accident factors are classified under a new HFACS structure (Uğurlu et al., 2018). HFACS is considered one of the best hybrid methods, containing human factors and system approaches, as well as integrating Reason's Swiss Cheese model (Shappell and Wiegmann, 2004; Chauvin et al., 2013; Uğurlu et al., 2018). This allows for accident causes to be conceptualized as interactions among active and latent system failures.

Step 4 - Creating the BN based on main HFACS structure and analysis: In this step of the study, the BN structure is formed, depending on the HFACS framework created in the previous step. The relationship between the nodes in the BN has been established by considering accident reports and occurrence of accidents. In the next step, CPTs are created by using the information in the accident database which is created in the study. Once the relevant nodes and CPTs are identified, they are input into a BN software package, HuginResearcher 7.7 (Hugin, 2018). The network is reviewed to ensure that there are no missing factors.

Hugin software is used to run the model and test for conflicts in data by inserting evidence (probabilities) in various nodes. This step involves the application of sensitivity analysis and entropy reduction. Sensitivity analysis assumes that input parameters to the model are not accurate; it shows the designer the variations in a systems reliability, given some variation of the input parameters values (Cai et al., 2013; Cai et al., 2019). Entropy reduction is applied to

the likelihood of accident categories, and the changes in the involved child nodes and parent nodes are evaluated (Cai et al., 2013; Yang et al., 2009). The purpose of entropy reduction is to determine which nodes will be utilized in the sensitivity analysis, for each HFACS level. Sensitivity analysis reveals the most likely accident combinations and probability values, as well as determining the influence of the most effective active and latent failures under each HFACS level for all accident categories. At this stage of the study, an accident network summarizing the occurrence of accidents in the Black Sea has been developed. The accident network allows users to estimate the risk of an accident occurring on the Black Sea given a variety of factors (weather conditions, vessel's structure, navigation area, unsafe acts, preconditions for unsafe acts). As a result, the key factors that cause accidents can be identified and prioritized in order to assist with accident mitigation.

Step 5 - Validation of the BN Model: Validation is the key aspect of the methodology as it provides a reasonable amount of confidence in the results of the model. In current work and literature, there is a three-axiom based validation procedure, which is used for partial validation of a proposed BN model. The three axioms to be satisfied are given as follows (Jones et al., 2009, Pristrom et al., 2016):

- Axiom 1: A small increase or decrease in the prior subjective probabilities of each parent node should certainly result in the effect of a relative increase or decrease of the posterior probabilities of the child node.
- Axiom 2: Given the variation of subjective probability distributions of each parent node, its influence magnitude to the child node should be kept consistent.
- Axiom 3: The total influence magnitudes of the combination of the probability variations from " $x$ " attributes (evidence) on the values should always be greater than that from the set of " $x-y$ " $(y \in x)$ attributes.


# 4. TEST CASE 

The example of the TOLSTOY accident, used as a test case, explains how the HFACS and BN structures are constructed for each accident by adhering to the research methodology. For the TOLSTOY accident, as with each accident in the dataset of the study a HFACS and BN structure was formed. Eventually all BNs were overlapped and a final BN structure was formed containing all accident data.

Step 1 - Gathering the accident data and choosing the appropriate method for accident analysis: The Tolstoy vessel sinking accident took place in September 2008 (MTITC, 2009); she commenced to navigation from Rostov-Don port (Russia) to Nemrut port (Turkey) with

scrap metal cargo on 22/09/2008. After passing the Kerch channel on 24/09/2008, she was exposed to heavy weather and sea conditions in the Black Sea and sank off Varna. For the purpose of the study, the accident report was examined, and the key accident data is presented in Table 1.

Table 1. TOLSTOY accident data

Carrier | 27.09.2008 | Total loss of ship, loss of life  |

Step 2 - Spatial analysis of accident data: The position data of the Tolstoy accident was placed on the Black Sea map with ArcGIS 10.3, as shown in Figure 4. ![img-3.jpeg](img-3.jpeg)

Figure 4. Position of TOLSTOY accident on Black Sea map

Step 3 - Classification of factors under HFACS structure: Based on the TOLSTOY accident report, latent and active failures that cause accidents are classified under the HFACS structure.

- Operational conditions: Heavy weather and sea conditions (external condition/weather condition), coastal water (external condition/local restriction), old vessel structure (internal condition/vessel structural defects), inland vessel (internal condition/vessel

structural defects) and engine failure (internal condition/non-conformities and failures preventing ship`s motion).
- Unsafe acts: Navigation on storm (errors/decision-based error), inappropriate stability (violations/regulation violation) and use of vessel within limits of design conditions (violations/regulation violation).
- Pre-conditions for unsafe acts: Fatigue (substandard team members/substandard conditions of team members), lack of situational awareness (substandard team members/substandard conditions of team members), lack of internal and external communication (substandard team members/substandard practices of team members), mismanagement of port operation (substandard team members/substandard practices of team members) and mismanagement of vessel navigation operation (substandard team members/substandard practices of team members).
- Unsafe supervision: Inadequate manning (inappropriate planned operations), faulty port cargo operation planning (inappropriate planned operations), inappropriate vessel cargo operation planning (inappropriate planned operations) and lack of planned maintenance (insufficient supervision).
- Organizational influences: Minimum safe manning strategy (organizational climate/organizational culture), unqualified crew assignment (resource management/human resource), lack of training and familiarisation to inland vessel structure (resource management/human resource) and not according to norm in the oversight and control mechanism (organizational process/oversight).
Step 4 - Creating the BN based on main HFACS structure and analysis: In view of the accident report and the occurrence of the accident, a BN was established depending on the HFACS structure. The BN structure for the TOLSTOY accident is presented in Figure 5.

![img-4.jpeg](img-4.jpeg)

Figure 5. BN structure for TOLSTOY accident

# 4.1. Conditional Probability Calculations 

The formulation of the CPT of the child node "Vessel Navigation Operation Planning" (Safe/Unsafe) shall be used an example to demonstrate the general formulation of the CPTs in the BN. This node has 3 parent nodes: "Training and Familiarization" (Sufficient/Insufficient), "Oversight and Control" (Adequate/Inadequate) and "Port or Company Pressure" (No/Yes). The safe or unsafe state of the "Vessel Navigation Operation Planning" node change depending on the three nodes (Figure 6).

![img-5.jpeg](img-5.jpeg)

Figure 6. Bayesian network structure for the "Vessel Navigation Operation Planning" node

The "Port or Company Pressure" node is only the root node. The calculation of initial probability values based on the accident reports of the "Port or Company Pressure" node is presented below.

It was observed that 6 of the total 89 accidents, in the Black Sea, involved "port or company pressure". Therefore, the initial probability value for the "Yes" state of the "Port or Company Pressure" node is calculated as $6 / 89=6.7 \%$. The probability value for the "No" state is $1-0.06 .7=93.3 \%$ (Figure 6). Furthermore, marginal probability value for the "insufficient" state of the "Training and familiarization" node is $56.20 \%$, and the posterior probability value for the "inadequate" state of the "Oversight and Control" node is $35.35 \%$.

Table 2. Conditional probability table for "Vessel Navigation Operation Planning" node


According to the Bayesian network created in the study, there are 8 parental combinations in which "Vessel Navigation Operation Planning" is positive or negative. The conditional probability values for these 8 combinations are presented in Table 2. Based on these conditions, the marginal probability value for the state "safe" of the "Vessel Navigation Operation

Planning" node was calculated as $57.16 \%$ and the posterior probability value for the "unsafe" state is $42.84 \%$.

According to Equations 2 and 3, the probability of the "Vessel Navigation Operation Planning" node to be in the state "unsafe" is calculated as follows (Vessel Navigation Operation Planning: VNOP, Training and Familiarization: TAF, Oversight and Control: OAC, Port or Company Pressure: POCP):

$$
\begin{aligned}
& \mathrm{P}(\mathrm{VNOP}(\text { Unsafe }))=[(\mathrm{P}(\mathrm{VNOP}(\text { Unsafe }) \mid \mathrm{POCP}(\mathrm{Yes}), \mathrm{OAC}(\text { Adequate }), \mathrm{TAF}(\text { Insufficient })) \times \\
& \mathrm{P}(\mathrm{POCP}(\mathrm{Yes})) \times \mathrm{OAC}(\text { Adequate }) \times \mathrm{TAF}(\text { Insufficient })]+ \\
& [(\mathrm{VNOP}(\text { Unsafe }) \mid \mathrm{POCP}(\mathrm{Yes}), \mathrm{AC}(\text { Adequate }), \mathrm{TAF}(\text { Sufficient })) \times \\
& \mathrm{P}(\mathrm{POCP}(\mathrm{Yes}) \times \mathrm{OAC}(\text { Adequate }) \times \mathrm{TAF}(\text { Sufficient })]+ \\
& [(\mathrm{P}(\mathrm{VNOP}(\text { Unsafe }) \mid \mathrm{POCP}(\mathrm{Yes}), \mathrm{OAC}(\text { Inadequate }), \mathrm{TAF}(\text { Insufficient })) \times \\
& (\mathrm{POCP}(\mathrm{Yes})) \times \mathrm{OAC}(\text { Inadequate }) \times \mathrm{TAF}(\text { Insufficient })]+ \\
& [(\mathrm{P}(\mathrm{VNOP}(\text { Unsafe }) \mid \mathrm{POCP}(\mathrm{Yes}), \mathrm{OAC}(\text { Inadequate }), \mathrm{TAF}(\text { Sufficient })) \times \\
& \mathrm{P}(\mathrm{POCP}(\mathrm{Yes})) \times \mathrm{OAC}(\text { Inadequate }) \times \mathrm{TAF}(\text { Insufficient })]+ \\
& [(\mathrm{P}(\mathrm{VNOP}(\text { Unsafe }) \mid \mathrm{POCP}(\mathrm{No}), \mathrm{OAC}(\text { Adequate }), \mathrm{TAF}(\text { Sufficient })) \times \\
& \mathrm{P}(\mathrm{POCP}(\mathrm{No}) \times \mathrm{OAC}(\text { Adequate }) \times \mathrm{TAF}(\text { Insufficient })]+ \\
& [(\mathrm{P}(\mathrm{VNOP}(\text { Unsafe }) \mid \mathrm{POCP}(\mathrm{No}), \mathrm{OAC}(\text { Inadequate }), \mathrm{TAF}(\text { Insufficient })) \times \\
& (\mathrm{POCP}(\mathrm{No})) \times \mathrm{OAC}(\text { Inadequate }) \times \mathrm{TAF}(\text { Insufficient })]+ \\
& [(\mathrm{P}(\mathrm{VNOP}(\text { Unsafe }) \mid \mathrm{POCP}(\mathrm{No}), \mathrm{OAC}(\text { Inadequate }), \mathrm{TAF}(\text { Sufficient })) \times \\
& \mathrm{P}(\mathrm{POCP}(\mathrm{No})) \times \mathrm{OAC}(\text { Inadequate }) \times \mathrm{TAF}(\text { Sufficient })]
\end{aligned}
$$

$\mathrm{P}(\mathrm{VNOP}($ Unsafe $))=(0.7 \times 0.067 \times 0.6465 \times 0.5620)+(0.5 \times 0.067 \times 0.6465 \times 0.4380)+$
$(1 \times 0.067 \times 0.3535 \times 0.5620)+(1 \times 0.067 \times 0.3535 \times 0.4380)+$
$(0.333 \times 0.933 \times 0.6465 \times 0.5620)+(0 \times 0.933 \times 0.6465 \times 0.4380)+$
$(1 \times 0.933 \times 0.3535 \times 0.562)+(0.485 \times 0.933 \times 0.3535 \times 0.438)$
$=0.4284(24.84 \%)$

Probability of "safe" state of "Vessel Navigation Operation Planning" node calculated as:

$$
=1-0.4284=0.5716(57.16 \%)
$$

# 4.2. Marine Accidents on the Black Sea 

Of the 109 accidents in the Black Sea 37 were due to sinking, 32 were due to grounding and 20 were due to collision-contact as shown in Table 3. In the past 20 years there have been a total of 23 fatal accidents where 149 people have lost their lives. Furthermore, within these fatal accidents there have been 54 vessels lost and 12 cases of marine pollution reported. Given the gathered data, sinking and grounding accidents are more concentrated in coastal waters and anchorage areas. On the other hand, collision-contact accidents are more concentrated in ports and open seas. From the data it can also be stated that sinking and grounding accidents occur more frequently ( $70.2 \%$ sinking, $87.5 \%$ grounding) in autumn and winter ( 6 months between October and March). However, this seasonal trend is not apparent for collision-contact accidents. Continually, $86 \%$ of sinking accidents, $78.1 \%$ of grounding accidents and $55 \%$ of collision-contact accidents have involved ships over 20 years old. The average age of the vessels involved in sinking accidents is approximately 29.5 years, while the average age of the vessels involved in grounding accidents was 26.8 years. Finally, a total of $37.7 \%$ of sinking and grounding accidents involved inland waterway vessels operating in the Black Sea.

Table 3. Distribution of marine accidents occurred in the Black Sea



# 5. BAYESIAN THEORY AND BAYESIAN NETWORK STRUCTURE 

### 5.1. Occurrence of BN Developed from Main HFACS Structure

The main structure and sub-elements of the HFACS structure that has been formed for this study, for the accidents that fall under the very serious and serious categories are presented in Figure 7. The BN which has been constructed on the basis of the main HFACS structure is shown in Figure 8. Similarly, the abbreviations used in BN structure are presented in Table 4.
![img-6.jpeg](img-6.jpeg)

Figure 7. Main structure and sub-elements of HFACS developed for this study

![img-7.jpeg](img-7.jpeg)

Figure 8. BN model for collision-contact, grounding and sinking occurring in the Black Sea

Table 4. Abbreviations used in BN structure


# 5.1.1. Latent Failures 

5.1.1.1. Organizational influences. Organizational influence is the first level in the HFACS framework, and it forms the basis of accident occurrence (Wiegmann and Shappell, 2001). Organizational influence includes not according to norm made by top level managers such as, fleet managers, technical managers, operations managers and crew managers etc. Organizational influences lead to the formation of not according to norm under the unsafe

supervision factor in the framework and negatively affect the other top-level factors. In the constructed BN, the nodes of crew assignment (States: "qualified crew/unqualified crew"), personnel training and familiarization ("sufficient/insufficient"), company manning strategy ("minimum safe manning/optimum safe manning"), procedures ("appropriate/inappropriate"), port or company pressure ("yes/no") and oversight and control ("adequate/inadequate") have been examined under this framework.

Table 5 shows the latent factors under this level, along with their abbreviations, probabilities, parent nodes and child nodes. Crew assignment, procedure, port or company pressure and company manning strategy are root nodes. For this reason, these nodes have no conditional probabilities. The prior probabilities of nodes under this level are given in Appendix Table A1. The probabilities in the appendix tables were determined based on the observing frequency of the relevant root node in the 89 accidents investigated. The root node, Procedure (P), was observed in the state "inappropriate" in 5 accidents and "appropriate" in 84 accidents. Therefore, the prior probability value of procedure in the state "inappropriate" is taken as $5 / 89=5.6 \%$ and procedure in the state "appropriate" is taken as $94.4 \%$. The prior probability values of other root nodes are also determined in this way.

Table 5. BN structure of organizational influences

$(\%)$ | Parent nodes | Child nodes  |

5.1.1.2. Unsafe Supervision. Unsafe supervision examines the consequences of leadership, such as, management of staff resources, planning of operations and solving known problems (Patterson and Shappell, 2010). These factors directly affect the occurrence of nonconformities under the level of pre-conditions for unsafe acts. Nodes examined under this level are: inadequate manning ("yes/no"), observation during operation ("clear/unclear"), vessel cargo operation planning ("adequate/inadequate"), vessel navigation operation planning ("safe/unsafe"), port operation planning ("adequate/inadequate") and planned maintenance ("completed/uncompleted") system as shown in Table 6. The conditional probability tables of these nodes are given in Appendix Table A2.

Table 6. BN structure of unsafe supervision


While determining the conditional probability values for the "safe/unsafe" states of the Vessel Navigation Operation Planning (VNOP) node in Table A2, the frequencies of the occurrence of the parent nodes; Port or Company Pressure (POCP), Oversight and Control (OAC), Training and Familiarization (TAF), shown in Figure 9, were investigated. Table 7 shows the number of observations in total accidents for each condition. There are 3 accidents in the data set (POCP/"no"+OAC/"adequate"+TAF/"sufficient") where all POC, OAC and TAF nodes are positive. None of these accidents had unsafe vessel navigation planning, therefore, the probability of VNOP was taken as $1.0(100 \%)$ safe and $0.0(0 \%)$ unsafe for this condition, as shown in Appendix Table A2.
![img-8.jpeg](img-8.jpeg)

Figure 9. BN part of Vessel Navigation Operation Planning (VNOP) node

Table 7. Number of accidents observed for conditions of relevant nodes


${ }^{*} \mathrm{n}=$ The number of accidents.

Based on the database, created in this study, there is 1 accident with the following conditions: "POCP/yes, OAC/inadequate, TAF/sufficient" and in this accident VNOP was observed as unsafe. Therefore, probability of VNOP was taken as $1.0(100 \%)$ unsafe and 0.0 $(0 \%)$ safe for this condition.

Similarly, there are 3 accidents with the following conditions: "POCP/no, OAC/inadequate, TAF/insufficient" and in all of these accidents, VNOP was observed as unsafe. Therefore, the probability of VNOP was taken as $1.0(100 \%)$ unsafe and $0.0(0 \%)$ safe for this condition (Appendix Table A2).

Furthermore, there are 15 accidents with the combination, "POCP/no, OAC/adequate, TAF/insufficient". Five of these accidents are unsafely planned vessel navigation operations. Therefore, VNOP is taken as $5 / 15=0.333$ unsafe and 0.667 safe for this condition (Appendix Table A2).

Continually, 52 accidents demonstrated the following combination: "POCP/no, OAC/inadequate, TAF/sufficient". Twenty-five of these accidents showed unsafe plans for vessel navigation operations. Therefore, VNOP is taken as $25 / 52=0.485$ unsafe and 0.515 (10.485) safe for this condition.

There is a conditional probability state where "POCP/yes, OAC/adequate and TAF/sufficient" was observed in 2 accidents. For only one of these accidents there is a "VNOP/unsafe condition". Therefore, VNOP is taken as $1 / 2=0.5$ unsafe and 0.5 safe for this condition. There were no accidents observed with the combination, "POCP/yes, OAC/adequate, TAF/insufficient". However, in addition to the previous condition, the Training and Familiarization node is also negative in this condition. This increases the likelihood of an accident; therefore, a higher probability is expected. Therefore, VNOP for this condition is taken as 0.7 unsafe and 0.3 safe. All of the combinations outlined here can be seen in Appendix Table A2.

As stated in the previous example, all of the probabilities used in this study have followed the sequences in the accident data during the process of determining the conditional probabilities. All conditional probabilities, shown in other tables in the appendix, were determined through similar calculations.
5.1.1.3. Pre-condition for Unsafe Acts. The pre-condition for unsafe acts explains the operators' substandard conditions and the substandard practices (Li and Harris, 2006), and is the final stage in the HFACS structure that plays a role in the emergence of unsafe actions (the last stage of latent failures). The nodes that are examined under this level are: fatigue ("yes/no"), situational awareness ("sufficient/insufficient"), external and internal communication ("adequate/inadequate"), vessel cargo operation management ("safe/unsafe"), vessel navigation operation management ("safe/unsafe"), port operation management ("safe/unsafe") and pilot operation management ("safe/unsafe"), as shown in Table 8. The CPTs of these nodes are given in Appendix Table A3.

Table 8. BN structure of pre-condition of unsafe acts


# 5.1.2. Active Failures 

5.1.2.1. Unsafe Acts. Unsafe acts are the visible causes of accidents and are the main focus of many researchers conducting accident analyses ( Li and Harris, 2006). Many accident reports contain detailed information on these actions and focusing on these unsafe acts helps us to understand what has happened in the accident formulation. However, the conditions that cause unsafe acts are understood, it is possible to learn how and why an accident has happened, and it is also possible to take more constructive measures to prevent accidents from occurring in the future.

The nodes examined under the level of unsafe acts are: COLREG ("notviolated/violated"), tug boat operation ("operational/faulty"), manoeuvre of pilot ("appropriate/inappropriate"), manoeuvre of captain ("appropriate/inappropriate"), departure from port in heavy weather and sea condition ("no/yes"), anchorage area selection ("appropriate/inappropriate"), manoeuvre of watch-keeping officer ("appropriate/inappropriate"), manoeuvre of Bridge Team Members (BTM) ("appropriate/inappropriate"), navigation on storm ("no/yes"), use of vessel within limits of design conditions ("no/yes"), cargo shifting or inappropriate stability ("no/yes"), triggering event for sinking ("unobserved/observed"), and triggering event for grounding ("unobserved/observed"), triggering event for collision and contact ("unobserved/observed"). The outline of the nodes under unsafe acts is shown in Table 9 and the CPTs of these nodes are given in Appendix Table A4.

Table 9. BN structure of unsafe acts


# 5.1.3. Operational Conditions 

Unsafe actions require events under operational conditions to occur in order for an accident to occur. Operational conditions are examined under two sub-categories, external and internal conditions. Nodes representing internal conditions are determined as: vessel age ("new/old"), inland vessel ("no/yes"), malfunction ("unobserved/observed"), internal operational conditions for collision ("unobserved/observed"), internal operational conditions for grounding ("unobserved/observed") and internal operational conditions for sinking ("unobserved/observed"). In this study, ships that are 20 years old or more fall under the state "old" in the vessel age node.

External operational conditions include external factors that play a key role or are involved in accident occurrence. These factors have been categorized as: navigation area ("narrow water/port/anchorage/coastal water/open sea"), heavy weather and sea conditions ("no/yes"), visibility ("good/poor"), external operational conditions for collision ("unobserved/observed"), external operational conditions for grounding ("unobserved/observed") and external operational conditions for sinking ("unobserved/observed"). The outline of the nodes under operational conditions is shown in Table 10. Vessel age, inland vessel, navigation area, visibility, heavy weather and sea conditions, in this BN, are all root nodes. The probability tables of these nodes are given in Appendix Table A5.

Table 10. Abbreviations, probabilities and parent and child nodes of operational conditions


# 5.1.4. Consequence Nodes 

The final nodes added to the BN are the consequence nodes i.e, the accident events themselves. Accidents in this study are limited to collision-contact, grounding and sinking. The first four levels in the BN represent the formation of unsafe actions, and the 5th level represents the operational conditions. The separate levels in the BN are indicated by the colour changes in Figure 8 with Level 1 starting at the top.

There are three event sets that cause accidents for each accident category: unsafe act, internal operational condition and external operational condition. If an unsafe act comes together with the operational conditions (internal and external) necessary for accident occurrence, accident is inevitable. Therefore, each accident consists of at least one internal operational condition, at least one external operational condition, and at least one unsafe act. The conditional probability tables for the last stage of the BN are arranged according to this data and are demonstrated in Appendix Table A6.

## 6. RESULTS AND VALIDATION OF STUDY

To demonstrate some partial validation of the BN model, it must satisfy the three axioms outlined in the final step of the methodology. These axioms are to be analysed separately in the following sections.

### 6.1. Axiom 1

For validity of the BN to be established, it was first tested as to whether it fulfilled the requirements of Axiom 1. For this axiom, the changes in the posterior probabilities of the accident nodes (grounding, sinking and collision-contact) are observed given the changes in the prior probabilities of their parent nodes. Table 11 shows the changes of the posterior probabilities of the consequences given changes in the prior probabilities of the respective parent nodes.

In terms of grounding accidents, if an unsafe action occurs, the probability of grounding increases from $0.79 \%$ to $3.02 \%$. If unsafe action does not occur, the accident simply does not occur. Furthermore, if bad external conditions are observed (bad weather and sea conditions), then the probability of grounding increases to $9.44 \%$. However, if favourable external conditions are available (good weather conditions), the accident does not occur. Similarly, if internal conditions are observed, the probability of grounding increases to $2.21 \%$, and if they are not observed, grounding will not occur.

Table 11 shows similar results for sinking and collision-contact accidents. Thus, this demonstrates that the BN model satisfies Axiom 1, as alterations made within the prior probabilities of the parent nodes, have a near-real impact on the posterior probabilities of the accident nodes.

Table 11. Test of Axiom 1 for each accident category


# 6.2. Axiom 2 

Axiom 2 states that given the variation of subjective probability distributions of each parent node, its influence magnitude to the child node should be kept consistent. Figure 10 shows the change in the posterior probabilities for the node 'Grounding' given changes made to the prior probabilities of its parent variables 'Internal operational conditions for grounding', 'External operational conditions for grounding' and 'Triggering factor for grounding'. The general trend of the results indicates a proportional increase of the posterior probabilities given the increase in the individual prior probabilities. In other words, there is a consistent increase of probabilities for 'Grounding=Yes' due to the increase of probabilities of 'Internal conditions for grounding=Observed', 'External conditions for grounding=Observed' and 'Triggering factor for grounding=Observed'. A similar observation can be made when analysing the node of 'Sinking' and 'Collision-contact' in Figure 11 and Figure 12. Given the information presented, it can be stated that the BN model satisfies Axiom 2.

![img-9.jpeg](img-9.jpeg)

Figure 10. Change of probabilities for the node 'Grounding'
![img-10.jpeg](img-10.jpeg)

Figure 11. Change of probabilities for the node 'Sinking'

![img-11.jpeg](img-11.jpeg)

Figure 12. Change of probabilities for the node 'Collision and Contact'

# 6.3. Axiom 3 

Axiom 3 requires that sub-evidence should have less influence on the values of a child node than evidence received from the parent nodes, 'Triggering event for grounding' (evidence) is composed of 'Navigation on Storm', 'Use of Vessel within Limits of Design Conditions' and 'Manoeuvre of BTM' (all sub-evidence). When evidence is entered ( $100 \%$ ) into the nodes and states of 'Navigation on Storm=Yes', 'Use of Vessel within Limits of Design Conditions=Yes' and 'Manoeuvre of BTM=Inappropriate', the posterior probabilities of 'Grounding=Yes' are $2.29 \%, 2.50 \%$ and $2.08 \%$ respectively. When 'Use of Vessel within Limits of Design Conditions=Yes', 'Navigation on Storm=Yes' and 'Manoeuvre of BTM=Inappropriate' are entered into the model, the probability of 'Grounding=Yes' increases to $3.02 \%$. Thus, the BN model can be said to satisfy Axiom 3. Further tests were also conducted for all accident nodes together with their corresponding sub-evidence. All the obtained results are in harmony with Axiom 3.

### 6.4. Sensitivity Analysis and Application of the BN Model

Entropy reduction was used to determine the nodes to be subjected to a sensitivity analysis. Hugin software was used for entropy reduction and sensitivity analysis in this study (Hugin, 2018). Entropy reduction allows for the identification of the most important nodes affecting accident occurrence for each HFCAS level. Table 12 shows entropy reduction results for each accident category. Nodes that are independent from the accident nodes in the table are not included.

Table 12. Entropy reduction results for each accident category


Considering the entropy reduction results shown in Table 12, for each HFACS level, sensitivity analysis was applied to the three nodes that demonstrated the greatest effect on each individual accident node. While the other nodes remain constant, the changes in the probability of each accident category was examined inserting evidence into the parent nodes, which are subjected to sensitivity analysis, first at $0 \%$ and then at $100 \%$. The results of the sensitivity

analysis results for sinking, grounding and collision-contact consequence nodes are demonstrated in Figures 13, 14 and 15. At this stage of the study, the aim is to demonstrate the effects that the outlined nodes, in each level of the BN, have on the occurrence of accidents.
![img-12.jpeg](img-12.jpeg)

Figure 13. Sensitivity analysis results for sinking

![img-13.jpeg](img-13.jpeg)

Figure 14. Sensitivity analysis results for grounding
![img-14.jpeg](img-14.jpeg)

Figure 15. Sensitivity analysis results for collision-contact

In the second stage of the sensitivity analysis, with a similar approach mentioned above, considering the occurrence of accidents in the Black Sea, sensitivity analysis has been applied to internal conditions, external conditions and triggering event nodes, which are the final stages of accident formation. The purpose of this step is to identify the three nodes that have the greatest effect on the accident nodes. The results of the sensitivity analysis are presented in Figure 16.
![img-15.jpeg](img-15.jpeg)

Figure 16. Sensitivity analysis results of main nodes

The final step in the sensitivity analysis is to determine the accident combinations and the occurrence probability of an accident. In order to determine this, the probabilities of the nodes demonstrating the greatest effect under 'triggering events', 'external conditions' and 'internal conditions' were evaluated. This evaluation involves inserting $100 \%$ evidence into the probability values of the relevant parent nodes. The purpose of this is to observe the changes in the posterior probability of the consequence nodes. According to the results of the analysis, 51 accident combinations were determined for the accident consequence nodes, 27 accident combinations for sinking accidents, 12 for grounding and 12 for collision-contact. The accident combinations consist of the following: internal_condition + external_condition + triggering_event. Table 13 shows the 10 most likely accident combinations with the highest probabilities and their percentage values.

Table 13. Most likely accident combinations for each accident category


# 6.5. Sinking Accidents 

Sinking accidents are the most common accident type that occur on the Black Sea and demonstrate the most serious consequences in terms of economic loss, loss of life and environmental pollution. The results show that external operational conditions play an important role in the occurrence of all three-accident categories; however, they have the greatest effect on sinking accidents as shown in Figure 16. The nodes that demonstrate the greatest effects in the occurrence of sinking accidents, under external conditions, are: 'navigation in coastal waters' $(0.83 \%)$ and 'heavy weather and sea conditions' $(0.76 \%)$. The internal conditions demonstrating the greatest effect on sinking are: 'malfunctions' (1.7\%), 'old vessel structure' $(0.28 \%)$ and 'river type vessel structure' $(0.05 \%)$ as shown in Figure 13.

Unsafe actions are events that trigger accidents, and according to the results of the study they are the second most important factors in the occurrence of sinking accidents. The most important unsafe acts playing a role in the occurrence of sinking accidents: 'cargo shifting or inappropriate stability' ( $2.87 \%$ ), 'navigation on storm' ( $1.39 \%$ ), and 'Use of Vessel within Limits of Design Conditions' (1.34\%) (Figure 13).

Organizational influences and improper internal-external management activities (latent failures) form the basis for the potential occurrence of unsafe actions. According to the results of the study, the determined latent failures that lead to unsafe acts are: 'navigation operation management' ( $1.12 \%$ ) (Pre-condition for unsafe act), 'port operation planning' (1.17\%) (Unsafe supervision) and 'oversight and control' (1.06\%) (Organizational influence) (Figure 13).

Marine accident occurrences have a compact structure, and according to the BN model, favourable operational conditions are necessary along with unsafe actions in order for an accident to occur. Evaluating the causes of accidents separately, as well as in certain combinations, makes it possible to understand accident occurrence. According to the BN results, the most likely scenarios which cause sinking accidents in the Black Sea involve combinations of: Cargo Shifting Or Inappropriate Stability (CSOIS), Malfunction (MAL) and 'Coastal Waters' (CW)/'Heavy Weather and Sea Conditions' (HWSC)/ 'Anchorage' (ANC). The probability of sinking given the specified combinations increases by a minimum of 8 times and a maximum of 14 times, which can be seen in Table 13. For these combinations, bad weather conditions and navigation area are complementary elements to the accident. When examining other event combinations in the occurrence sinking accidents, it was observed that 'inland vessel structure' and 'old hull structure' also affected the occurrence of sinking accidents. This is also demonstrated in Table 13.

# 6.6. Grounding Accidents 

Grounding accidents are the second most frequent category of marine accidents in the Black Sea. According to the BN results, external conditions ( $9.44 \%$ ) have the greatest effect on the occurrence of grounding accidents, followed by unsafe acts ( $3.02 \%$ ) and internal conditions ( $2.21 \%$ ), as shown in Figure 16. The nodes that demonstrated the greatest effects on the occurrence of grounding accidents, under external conditions, are: 'navigation area/anchorage' $(0.94 \%)$ and 'heavy weather and sea conditions' ( $0.48 \%$ ). Furthermore, when a ship is in an anchorage area and is exposed to bad weather conditions, it is more likely to run aground. Following the examination of the internal conditions, it was observed that the 'use of old vessels' $(0.08 \%)$ and 'use of river type vessels' $(0.05 \%)$ in the Black Sea increase the likelihood of a grounding accident. This is demonstrated in Figure 14.

As with sinking accidents, unsafe actions are the second most important level in the occurrence of grounding accidents following external conditions. The unsafe actions that demonstrate the greatest effect on the occurrence of grounding accidents in the Black Sea are: 'navigation on storm' ( $2.23 \%$ ), and 'the use of vessel within limits of design conditions' ( $1.99 \%$ ) respectively. The use of old vessels or river type vessels in bad weather conditions or in condition of exceeding a vessel`s design limits increase the likelihood of grounding accidents (Figure 14).

The nodes that demonstrate the greatest effects in the formation of unsafe actions, under latent factors are: 'vessel navigation operation management' ( $1.72 \%$ ) (Pre-condition for unsafe act), 'observation during operation' ( $1.5 \%$ ) (Unsafe supervision) and 'oversight and control' (1.37\%) (Organizational influence) (Figure 14).

According to the results of the study, the most likely scenarios for grounding are the combinations of 'Use of Vessel within Limits of Design Conditions' (UVLDC), 'Anchorage' (ANC) and 'Old Vessel' (OV)/'Inland Vessel' (IV). The probability of grounding in the stated combinations increases by approximately 6 times. Old vessel structures or river type vessel structures are important factors in this combination as complementary factors (Table 13). Similarly, as with the previously mentioned accident combinations (UVLDC + ANC + (OV or IV)), there are old vessel structures or river type vessel structures in other accident combinations.

### 6.7. Collision-Contact Accidents

Collision-Contact is the third most common accident category in the Black Sea. It has been observed that the effect of external conditions ( $5.71 \%$ ) on the occurrence of collision-

contact accidents is lower than the effects of external conditions demonstrated with the other accident types. However, it is the most important level that plays a role in the occurrence of collision-contacts (Figure 16). Visibility (1.01\%) is the most important external condition that affects the occurrence of collision-contact accidents. Other important external conditions affecting collision-contact accidents are: 'navigating in port area' ( $0.58 \%$ ), 'anchorage area' $(0.32 \%)$ and 'coastal waters' $(0.32 \%)$. Navigation area and restricted visibility establish a base for the occurrence of collision-contact accidents. Furthermore, it was observed that old vessel structures or river type vessels, under the level of the internal conditions, do not affect the occurrence of collision-contact accidents. However, malfunctions that occur within a ship's components affect collision-contact accident occurrence ( $0.26 \%$ ), as demonstrated in Figure 15 .

The results of the study show that the actions of bridge team members have a greater effect on collision-contact accidents than other accident types. The most influential unsafe acts are: 'inappropriate manoeuvre of BTM' (1.36\%), 'inappropriate manoeuvre of captain' (1.17\%) and 'violation of COLREG' ( $1.03 \%$ ). When the latent failures are examined, unlike grounding and sinking accidents, the most effective pre-condition for collision-contact accidents is 'loss of situational awareness' ( $1.03 \%$ ). According to the results of the BN analysis, loss of situational awareness of bridge team members leads to unsafe acts (error and violations). Similarly, as observed with sinking and grounding accidents, 'unclear observation during operation' ( $1.0 \%$ ) (Unsafe supervision) and 'inadequate oversight and control' ( $0.92 \%$ ) (Organizational influence) are the most effective latent failures in collision-contact accidents (Figure 15).

The most likely accident scenarios for collision-contact accidents are combinations of: 'Malfunction' (MAL) and 'Visibility' (VIS) nodes along with 'Manoeuvre of Bridge Team Members' (MOBTM) or 'Manoeuvre of Captain' (MOC) or COLREG nodes (MAL + VIS + (MOBTM or MOC or COLREG)). In these combinations, the likelihood of collision-contact increases by a minimum of 8 times and a maximum of 10 times as shown by Table 13. This result shows that a mistake made by bridge team members may lead to an accident when there is a malfunction on the ship, as in the case of restricted visibility, such as during the night or in heavy fog. In addition, other important combinations that increase the likelihood of an accident are the MOBTM or MOC or COLREG nodes in conjunction with port, anchorage or coastal waters.

# 7. DISCUSSION 

This is the first study that analyses the accidents that have occurred in the entire Black Sea area as a collective. Many studies in the scope of marine accident analysis emphasize that the most frequent accident categories at sea are collision-contact accidents and grounding accidents, respectively (Uğurlu et al., 2015b; Uğurlu et al., 2015c). However, unlike other studies in the literature, this study has determined that the most frequent accident categories in the Black Sea are sinking, grounding and collision-contact accidents, respectively. In addition, an accident network which summarizes the accident occurrence in the Black Sea has been established by using the Bayesian network method. Using this accident network, the combination of accident occurrences in the Black Sea for all three accident categories has been revealed and interpreted.

Operational conditions play an important role for all three accident categories in the areas of the Black Sea where accidents are heavily concentrated. The results of the study show that the operational conditions have the greatest effect on the occurrence of sinking and grounding accidents. The most common operational conditions that contribute to the occurrence of both grounding and sinking accidents, were determined to be 'navigation area' (coastal water and anchorage) and 'heavy weather and sea conditions'. Many studies carried out in the context of accident analysis have emphasized that 'heavy weather and sea conditions' are the main factor in the occurrence of grounding or sinking accidents (Macrae, 2009; Ulusçu et al., 2009; Schröder-Hinrichs et al., 2011; Mullai and Paulsson, 2011; Uğurlu et al., 2015b; Uğurlu et al., 2015a).

One important feature that distinguishes this study from other studies in the literature is that, malfunctions and old or inland (river type) vessel structures are found to be factors which also greatly affect the occurrence of accidents, heavy weather conditions. When navigating with old vessels or inland vessels in the Black Sea, inappropriate anchorage area selection or navigating in heavy weather conditions, by ignoring the weather reports, or use of vessel within limits of design conditions, or inappropriate cargo stowage, will inevitably result in grounding and sinking accidents.

In addition to the operational conditions and unsafe acts that play a role in the occurrence of grounding, and sinking accidents, latent failures were also identified in the study, within the scope of marine accident analysis. For this reason, in order to prevent accidents in the Black Sea, it is necessary to focus on factors under pre-conditions, unsafe supervision and organizational influences, such as 'inappropriate crew assignment', 'inadequate manning', 'inappropriate planned operations', and 'lack of communication and coordination'.

As a result of this study, accidents were observed to be in high concentrations in the coastal waters of the Black Sea, especially in Kerch Strait North and South Bound (Ukraine), Novorossiysk (Russia), Kilyos (Istanbul-Turkey), Constanta (Romania), Riva (Istanbul Turkey) and Batumi (Georgia). The Black Sea is a maritime area where many ships navigate, and many vessels that operate in the area share common features such as very old vessels, or vessels intended for use on inland waterways (i.e. rivers). The average age of the vessels involved in grounding or sinking accidents was 28.2 years and the average age of the inland vessels was 30.3 years. Therefore, in order to reduce accidents in the Black Sea, the factors under 'internal conditions' ('old vessel structure', 'inland vessel structure' and 'malfunctions') must almost certainly be improved. In order to reduce grounding and sinking accidents in the Black Sea, it is necessary to prevent navigation of river type vessels which are not suitable for heavy weather and sea conditions due to their structure, and vessels with older structures must be renewed or replaced.

The results of the analysis related to collision-contact accidents are similar to the results found in literature (Chauvin et. al., 2013; Uğurlu et. al., 2015c; Uğurlu et al., 2018). Unsafe acts that play a role in the occurrence of collision-contact accidents were determined as: 'inappropriate manoeuvre of captain' or 'BTM', and 'violation of COLREG'. The latent failures underlying these unsafe acts are: 'loss of situational awareness', 'lack of external and internal communication', 'inappropriate navigation operation management', 'unclear observation during operation', and 'inappropriate oversight and control'. In this study, it was observed that unsafe actions are more likely to occur under the external conditions category, under such factors as, 'restricted visibility', 'heavy weather' and 'restricted waterways' (port, anchorage or coastal water). It is not possible to eliminate factors under external conditions, but these risks can be kept under control by assigning experienced team members who have worked in the area for a sufficient period of time.

# 8. CONCLUSION 

The most important feature of this study is an accident network which summarizes the occurrence of accidents in the Black Sea. The accident network enables users to estimate the risk of accidents in variable conditions. The purpose of this is to increase the situational awareness of users and prevent accidents with the established Bayesian Network. Also in this study, risk factors affecting accident occurrence in Black Sea were determined and recommendations were presented to assist with the mitigation of these factors. In this way, ship operators, port/flag state authorities or company owners can estimate the risk of accidents by

taking into account the changing conditions and may intervene in terms of the ships' navigation. The model presented in this study was formulated and validated by the analysis of accidents in the Black Sea. Since the foundation of the network is based on HFACS, it has a highly adaptable and updateable structure. Therefore, it is completely reasonable to suggest that the application of the methodology can be extended to analyses accidents occurring in different marine areas.

HFACS has been used as modified for adaptation to a number of industries such as, aviation (Wiegmann and Shappell, 2001; Shappell and Wiegmann, 2004; Dambier and Hinkelbein, 2006), maritime (Chen et. al., 2013; Uğurlu et. al., 2018), railway (Baysari et. al., 2008), mining (Patterson and Shappell, 2010; Lenné et. al., 2012), and the oil and gas industry (Theophilus ., 2017). Therefore, the network structure presented in this study can be modified and used for risk analysis in cases of uncertainty both in maritime transport and other sectors.

The data collection method utilised, in to develop the BN, proved to be challenging due to the lack of a coherent accident database relating to accidents in the Black Sea. Furthermore, the analysed accident reports were read in four different languages (Turkish, Russian, Georgian, and Ukrainian) since the accidents are not reported and documented in English. For this reason, it is necessary to establish a common EMSA-like accident database, which collects, compiles and standardizes accident reports, as well as integrating maritime safety regulations in countries that have coasts on the Black Sea. This will allow documented accident reports to be standardized. This would open the possibility of accidents to be reported directly to the International Maritime Organization (IMO), via the database, and assisting future researchers by easing the burden of gathering accident statistics in the Black Sea region.

# ACKNOWLEDGEMENTS 

This project has received funding from the European Union's Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No 730888. The study was supported by TÜBITAK (The Scientific and Technological Research Council of Turkey/2219 scientific research support program). The authors would like to thank anonymous reviewers for their constructive suggestions.

## APPENDIX

Table A1. Probabilities of nodes under organizational influences


![img-16.jpeg](img-16.jpeg)

Table A2. Probabilities of nodes under unsafe supervision





Table A3. Probabilities of nodes under pre-conditions for unsafe acts





Vessel Navigation Operation Planning Vessel Navigation Operation Management Vessel Navigation Operation Planning Vessel Navigation Operation Planning Vessel Navigation Operation Management


Table A4. Probabilities of nodes under unsafe acts










Table A5. Probabilities of nodes under operational conditions





















Table A6. Probabilities of accidents





