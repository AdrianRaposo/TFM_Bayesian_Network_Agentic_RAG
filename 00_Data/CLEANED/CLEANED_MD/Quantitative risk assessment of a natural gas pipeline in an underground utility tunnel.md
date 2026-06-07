![img-0.jpeg](img-0.jpeg)

This item is the archived peer-reviewed author-version of:

Quantitative risk assessment of a natural gas pipeline in an underground utility tunnel

Reference:

Fang Weipeng, Wu Jiansong, Bai Yiping, Zhang Laobing, Reniers Genserik. - Quantitative risk assessment of a natural gas pipeline in an underground utility tunnel Process safety progress / American Institute of Chemical Engineers - ISSN 1547-5913 - 38:4(2019), e12051

Full text (Publisher's DOI): https://doi.org/10.1002/PRS.12051

To cite this reference: https://hdl.handle.net/10067/1638600151162165141

# Quantitative Risk Assessment of a Gas Pipeline in an 

## Underground Utility Tunnel

Weipeng Fang ${ }^{\mathrm{a}}$, Jiansong Wu ${ }^{\mathrm{a}, \mathrm{b}, *}$, Yiping Bai ${ }^{\mathrm{a}}$, Laobing Zhang ${ }^{\mathrm{c}}$, Genserik Reniers ${ }^{\mathrm{c}}$<br>${ }^{a}$ Department of Safety Technology and Management, China University of Mining \& Technology, Beijing 100083, China<br>${ }^{\mathrm{b}}$ Tsinghua Holdings Co., Ltd., Beijing 100084, China<br>${ }^{\text {c }}$ Safety and Security Science Group, Delft University of Technology, Delft, The Netherlands<br>*Corresponding author: jiansongwu@hotmail.com; Phone: +86-1062339029


#### Abstract

With the rapid urbanization and the pressing demands of efficient utilization of urban underground spaces in China, more and more underground utility tunnels have been established around cities these years. A Chinese utility tunnel normally houses various kinds of city lifelines (e.g. gas pipeline, heat pipeline, sewer pipeline, water supply, telecommunication cables, electricity, etc.). This huge underground construction really facilitates urban life, but may introduce superposed risk into the society since it involves couples of high-risk pipelines. The gas pipeline is considered to be one type of pipelines with catastrophic potential consequence if a gas leakage and subsequent explosion occurs. The potential hazards in the gas compartment of a utility tunnel are quite different from the of the conventional directly buried gas pipeline. This study is aimed to developing a dynamic quantitative risk analysis method for a gas pipeline accident in a utility tunnel. Firstly, potential accident scenarios of a gas pipeline situated in a utility tunnel are identified and implemented in a bow-tie (BT) diagram based on case studies of typical gas pipeline accidents and experts experience. Then, a Bayesian network (BN) is established from the BT diagram through a mapping algorithm. Based on a comprehensive analysis of the results of probability updating and sensitive analysis (SA), the critical influencing factors are identified. The proposed quantitative risk analysis framework can not only perform predictive analysis of the gas pipeline accident evolution process in a utility tunnel from causes to consequences, but can also examine key challenges of gas pipeline risk management in the utility tunnel. This study is helpful for utility tunnel emergency response decision-making and loss prevention.


Keywords: Gas pipeline accident, Utility tunnel, Quantitative risk analysis, Bayesian network, Bow-tie diagram

With the rapid urbanization and the pressing demands of efficient utilization of urban underground spaces in China, urban underground utility tunnels have been developing fast these years. In 2015, the Chinese government selected ten pilot cities for utility tunnel application and demonstration, and the Ministry of Finance of China had started to offer Earmarked Subsidy Funds to them for at least three years (Wang et al., 2018). A Chinese utility tunnel normally houses various kinds of urban lifelines (e.g. gas pipeline, heat pipeline, sewer pipeline, water supply, telecommunication cables, electricity, etc.). A feasible prototype of utility tunnel according to the Chinese Technical Code for Urban Utility Tunnel Engineering (CTCUUTE) is shown in Fig. 1 (MHUD of Shanghai, 2012). The utility tunnel makes underground pipelines centrally settled and avoids repeated road excavation during industrial activities (Broere, 2016). This huge underground construction really facilitates urban life, but may introduce superposed risk into the society since it centrally assembles couples of high-risk pipelines like gas, sewer, heat, high-voltage electricity. Thus, the potential hazard of a utility tunnel cannot be overlooked as the accident consequence could be catastrophic.
![img-1.jpeg](img-1.jpeg)

Fig.1. A prototype of utility tunnel according to CTCUUTE
Among all the city lifelines established in the utility tunnel, the gas pipeline is considered to be one type of pipelines with catastrophic potential consequences if a gas leakage and subsequent explosion occurs (Canto-Perello et al., 2013b). In the past few years, there have been some

catastrophic urban gas pipeline accidents. In Qingdao city in 2013, a gas and oil pipeline explosion accident caused 62 deaths. In Gaoxiong city in 2014, serious successive explosions because of gas pipeline leakage led to about 350 casualties and 3 roads were damaged seriously. Nowadays, by the use of underground utility tunnels, the gas pipeline is housed in a compartment space together with many other city lifelines. Therefore, the consequence of a gas pipeline explosion could be more severe if the cascading effects to other lifelines in the utility tunnel are considered.

In the past decades, many research achievements have been made on risk analysis of directly buried gas pipelines including critical threats identification and consequence analysis based on Fault tree (FT), Event tree (ET), Bow-tie (BT) diagram, Bayesian network (BN) methods, and so on (Han and Weng, 2010; Kabir et al., 2015; Zarei et al., 2016; Li et al., 2016; Wu et al, 2017; Su et al., 2018; Arzaghi et al., 2018). However, few studies have been extended to the analysis of gas pipeline accidents specifically in a utility tunnel. Some attempts have been carried out on studying the impact of crustal movement (earthquake) on utility tunnel structure (Chen et al., 2010, 2012), the analysis of fire smoke temperature distribution in a utility tunnel under different fire situations (Zhao et al., 2018a, 2018b), and the identification of preliminary critical threats of a utility tunnels' structure (not for a utility tunnel accident) (Curiel-Esparza and Canto-perello, 2005; Canto-Perello et al., 2013a, 2013b). However, at present the research work on comprehensive risk analysis of gas pipeline accidents in a utility tunnel (critical hazards identification, the assessment of safety measures and consequence analysis) is still scarce. Besides, potential hazards in the gas compartment of a utility tunnel are different from that of a conventional directly buried gas pipeline, and thus these hazards are essential to be investigated.

In order to establish a comprehensive risk assessment framework for gas pipeline accidents in a utility tunnel, the present paper employs a Bow-tie diagram to identify potential hazards and possible accident scenarios, and applies Bayesian network for dynamic quantitative risk analysis of gas pipeline accidents in a utility tunnel. Compared with conventional risk analysis methods, Bayesian network has been proven to be effective for capturing and integrating qualitative and quantitative information from various sources and can facilitate the accident scenario modeling with multi-state variables (Khakzad et al., 2011; Yuan et al., 2015; Wu et al., 2017), particularly for dynamic risk analysis (Khakzad et al., 2013; Amin et al., 2018). In this study, the proposed BN

for gas pipeline accident in a utility tunnel is transferred from the BT diagram through a developed mapping diagram. A few binary intermediate events of BT are extended to multi-state nodes in order to represent a more realistic accident scenario. The conditional probabilities of the extended Bayesian nodes are collected based on expert experience and the Delphi method. Based on the proposed framework, critical threats of a gas pipeline accident in a utility tunnel can be identified and the evolution process of gas pipeline failures from causes to consequences can be evaluated and presented explicitly. This study could be helpful for utility tunnel emergency response decision-making and loss prevention.

# 2. Methodology 

### 2.1. Bow-tie Method

The Bow-tie (BT) method is a comprehensive risk analysis method, which integrates and represents primary events, intermediate events, top event, safety measures and their causal relationship into the same diagram (Ruijter and Guldenmund, 2016). A simple example of the BT diagram is illustrated in Fig. 2. "X1 to X4" represent the primary events while "A1" and "A2" denote the intermediate events. " $T$ " is the top event of the FT (shown on the left-hand side) and the ET (shown on the right-hand side). The state of safety barrier "S1" is defined as "Good" or "Poor", while for "S2" the state can be either "Yes" or "No". Besides, "C1 to C4" indicate the different accident consequences. The BT diagram, a combination of the FT method (deductive) and the ET method (inductive) with the same top event, is both quantitative and qualitative. The FT is available to calculate the failure probability of the top event based on the probabilities of root events and the identification of critical root events via finding the minimum cut sets. The ET shows a group of possible accident consequences if at least one of the safety barriers does not work well. The probability of each accident scenario can be calculated based on the failure probabilities of safety measures. The Bow-tie diagram has been widely applied to risk analysis, safety management, and reliability assessment in the field of process industry (Ferdous et al., 2011; Khakzad et al., 2012, 2013; Bellamy et al., 2013; Paltrinieri et al., 2013; Martins et al., 2014).

![img-2.jpeg](img-2.jpeg)

Fig. 2. A schematic diagram of Bow-tie method

# 2.2. Bayesian network 

Bayesian network is a popular probabilistic graphical method and is an attractive tool to deal with two kinds of problems in engineering practice: uncertainty and complexity. BN is a directed acyclic graph (DAG) with nodes and arcs. The Bayesian nodes represent the system variables and the directed arcs define the dependencies between nodes. The Bayesian nodes are normally divided into two types: parent nodes and child nodes. If there is an arrow from node A to another node B, A is called a parent of B, and B is a child of A. The BN is a kind of probabilistic tool that can perform both predictive analysis and diagnostic analysis (Wittberg, 2012). The predictive analysis calculates the probability of any child node based on the conditional probability tables (CPTs) of every related node while the diagnostic analysis relies on the information updating from new evidences. In a Bayesian Network, the joint probability distribution of the child nodes can be written as the product of the local conditional probability of each parent node (for the root node, the probability distribution of which is unconditional, and the prior probabilities of root nodes are normally obtained from previous accident data, literatures, and safety reports):

$$
P\left(V_{1}, V_{2}, \cdots, V_{k}\right)=\prod_{1}^{k} P\left(V_{i} / \operatorname{Parent}\left(V_{i}\right)\right)
$$

where $P\left(V_{1}, V_{2}, \cdots, V_{k}\right)$ describes the joint probability of a child node and $P\left(V_{i} / \operatorname{Parent}\left(V_{i}\right)\right.$ is the conditional probability of every parent node of this node. As for the data updating, BN benefits from new information from given evidence, normally called " $e$ ". The probability of every node is updated dynamically based on equation (2):

$$
p(A \mid e)=\frac{p(e \mid A) p(A)}{p(e)}=\frac{p(e \mid A) p(A)}{\sum_{i=1}^{e} p(e \mid A_{i}) p\left(A_{i}\right)}
$$

where $p(A \mid e)$ represents the conditional probability of event $A$, i.e. the posterior probability given the evidence " $e$ "; $p(e \mid A)$ is the evidence likelihood of the given event $A ; p(e)$ is the probability of evidence " $e$ "; $p(A)$ is the prior probability of event $A$; and $\sum_{i=1}^{e} p(e \mid A_{i}) p\left(A_{i}\right)$ indicates the joint probability of evidence " $e$ ".

# 2.3. Mapping Algorithm from BT to BN 

In this study, the Bayesian network for representing gas pipeline accident in utility tunnel is converted from the BT accident scenario analysis. The mapping algorithm developed in this paper is mainly according to the work of Khakzad et al (Khakzad et al., 2013), as shown in Fig. 3. The first step is to generate Bayesian nodes (pivot node, intermediate nodes, root nodes) from the corresponding elements of BT (top event, intermediate events and safety barriers, primary events and consequences). It should be noted that the characteristics of the pivot node and intermediate node are actually the same as the child node. The new name given here is for illustrative purpose of the mapping. A gas pipeline accident scenario in a utility tunnel is complicated. Some of the intermediate nodes (binary states in BT) are modified and extended to multi-state nodes in order to establish a more realistic model. The second step is to connect the BN nodes based on the causal relationship in the BT. Determining the CPTs for each node is the last step. The CPTs for nodes with binary states are collected according to the logic nodes in BT (see Fig. 4), whereas the CPTs for nodes with a multi-state are determined by using expert judgements.

![img-3.jpeg](img-3.jpeg)

Fig. 3. The mapping algorithm from BT to BN
![img-4.jpeg](img-4.jpeg)

Fig. 4. Probability calculation based on logic gate

# 3. Risk analysis of gas pipeline accident in utility tunnel 

### 3.1. BT diagram analysis

The gas pipeline arrangements in traditional ways (directly buried) and in a utility tunnel vary a lot, and thus present different kinds of potential hazards and accident causes. In a solid compartment of a utility tunnel with a relatively steady thermal environment, the gas pipeline will not face many external erosion issues (soil erosion, chemicals erosion, etc.) and could avoid possible external interferences (ground activities, industrial constructions, and other underground pipeline maintenance, etc.). However, a gas pipeline failure in a utility tunnel still occurs due to many other causes. The gas pipeline is considered to be one of the most dangerous lifelines in a utility tunnel, and therefore, it should be settled in an isolated compartment. Gas pipes are normally installed on concrete supports. There are generally some fireproof facilities, like the fire

extinguisher (in the cuboid box), the chemical extinguishing agent (hanging on the wall), and the fire-proof door (see Fig. 5).
![img-5.jpeg](img-5.jpeg)

Fig. 5. The inner structure of the gas compartment.
Considering the differences for the arrangements and working environment of the gas pipeline in utility tunnel, we employ a BT diagram to analyze the causes and evolution process of a gas pipeline accident in a utility tunnel. Based on case studies of typical gas pipeline accidents in a utility tunnel and referring to directly buried gas pipe accidents from accidents reports and a literature review, and further evaluations by expert experience, the BT diagram for a gas pipeline accident in a utility tunnel is determined. In this study, the gas pipeline leakage is identified as a critical accident scenario and is made to be the top event of the BT diagram, as shown in Fig. 6. Table 1 shows the detailed description of the symbols for primary and intermediate events. The failure probabilities of primary (root) events are presented in the third row of Table 1. In this paper, most of the prior probabilities are collected from accident databases like the National Bureau of Statistics (NBS) of China, and from previous studies (Zhang et al., 2014; Shen et al., 2016; Zarei et al., 2016; Li et al., 2016; Wu et al, 2017). However, it is pretty hard to find corresponding references for some subjective events (e.g., "Incorrect Material Selection"), and therefore the prior probabilities of these events were determined by expert judgments. Information about intermediate events and accident consequences is illustrated in Table 2. In the utility tunnel, the ventilation system, ignition sources, fireproof facilities (extinguisher, aerosol instrument, etc.), fire/explosion isolation (fireproof door), and the evacuation system are considered as the overall safety barriers for preventing gas pipeline accidents and the failure probability of each safety barrier is presented in Table 3.

[^0]
[^0]:    166
    167
    168
    169
    170
    171
    172
    173
    174
    175
    176
    177
    178
    179
    180
    181
    182
    183
    184

![img-6.jpeg](img-6.jpeg)

Fig.6. BT diagram for Gas pipeline failure in utility tunnel


191 Table 2
192 Description of Intermediate Events and Consequences


193 Table 3
194 Failure Probability of Safety Barriers


195 3.2. BN establishment

196 3.2.1 Bayesian Nodes

According to the mapping algorithm, a Bayesian network with 43 nodes ( 25 root nodes and 18 intermediate nodes) for representing a gas pipeline accident in a utility tunnel is established. In this study, all of the parent nodes are given binary states (Yes and No), while some child nodes are modified and extended to multiple states. The detailed description of every Bayesian node is listed as follows:

1) Failure of Supporting Structure. The bottom supporting structure (normally a supporting pier) for the gas pipeline is constructed to keep the gas pipes fixed and to avoid erosion by water and other adverse substances. This root node represents the state (i.e., failure or not) of supporting

piers or the stents on the concert wall. The gas pipeline may fall to the ground if the supporting piers fail.
2) Natural Hazards. This root node indicates the influence of extreme meteorological disasters (e.g. typhoon, flood, debris flow) or violent crust motion (earthquake) to the structure of the gas compartment.
3) Third-party Interference. This node describes the possible situation ofdeliberate human activity such as a terrorist attack that mainly focusing on the utility tunnel.
4) Industrial Activity. This node represents potential external interference such as industrial construction, road maintenance and so on. The gas compartment structure could be damaged under overpressure attack (high-intensity of resonance).
5) High Water Content. This node represents high water content in the gas pipeline, which would give rise to inner corrosion. Furthermore, the high water content may cause "water plugging", which would result in a serious pipeline failure.
6) Inhibitor Failure. The inhibitor failure will not well restrain the corrosion rate of gas pipes.
7) Poor Coating Quality. This node indicates the poor construction quality of coating. The coating is a significant part to protect gas pipes from the external environment.
8) Incorrect Material Selection. This node describes the unreasonable selection of coating material.
9) Aging. This node represents major causes for coating spalling. This situation comes up when the coating has been used for many years and has not been replaced timely.
10) $\mathrm{H}_{2} \mathrm{~S}$ Content Overproof. This node represents the high concentration of $\mathrm{H}_{2} \mathrm{~S}$ in gas.
11) $\mathrm{SO}_{2}$ Content Overproof. This node represents the high concentration of $\mathrm{SO}_{2}$ in gas.
12) Others. This node represents the high concentration of other acid media in gas.
13) Incorrect Pipe Material Selection. This node indicates the inappropriate use of materials for making gas pipes.
14) Unreasonable Supporting Structure Design. This node describes the influence of bottom supporting structure on gas pipes. As mentioned above, the failure of supporting structure would cause pipeline falling from the original location and then give rise to pipe damage.
15) Unreasonable Valve Connection Design. This node represents the situation that the valve is at a vulnerable location in the confined pipes. The valverepresents a primary control of gas flow,

and hence its defect may lead serious gas eruption.
16) Weld Flaw. This node indicates the situation of incorrect weld operation including unreasonable weld method, material, and insufficient weld.
17) Mechanical Damage. This root node describes the mechanical damages during the installation, maintenance and inspection, who are mainly caused by an undesired metal crash.
18) Misoperation of Supporting Structure Construction. This node represents there is misoperation in the installation of supporting structure for gas pipes, i.e. the design of the supporting structure of gas pipeline is good but the workman did not install it in good order.
19) Incorrect Maintenance. This node represents maintenance or repairs of facilities in the gas compartment which would not be procedural and/or reasonable.
20) Unreasonable Operation. This node describes wrong operations made by working staff during daily work such as flow and pressure control.
21) Ventilation System. The ventilation system is a significant safety barrier in the gas compartment of utility tunnels. According to the Chinese construction regulation, usually the least air exchange rate in the utility tunnel is two times per hour, and for the gas compartment the rate should not be less than six times per hour. In an emergency situation (accident), the rate is at least twelve times per hour (MHUD of Shanghai, 2012).
22) Ignition Source. Fire is evidently forbidden in the gas compartment of a utility tunnel, but there are still some ways to generate fire such as electric sparks, electrostatic ignition and incidental arson.
23) Fireproof Facility. This node describes various fireproof facilities (extinguisher, aerosol dispenser, etc.) in the gas compartment.
24) Fire/Explosion Isolation. This node indicates the working function of a fireproof door in a utility tunnel when an accident happens. According to Chinese regulation, a utility tunnel should be separated into several fire zones (normally every two hundred meters one fire zone).
25) Evacuation. This node represents the emergency rescue in case of an accident scenario. The effective evacuation would significantly reduce the accident consequence.
26) Pipeline Rupture, state: Slight, Serious. This child node represents that the gas pipeline would be damaged when the concrete wall of gas compartment is destroyed or the bottom supporting structure is destructed. The 'slight state' indicates the gas pipeline is damaged slightly

## fBLE [D2]: Differecne with 14) ? <br> Response: Yes, node 14) <br> represents that the supporting structure of the pipeline is unreasonably designed, while node 18) indicates the design of the supporting structure of the pipeline is good but the workman did not install it in good order.

and only a small amount of gas comes out, while the 'Serious state' represents the gas pipeline is damaged seriously with a large amount of gas diffused.
27) Pipeline Corrosion, state: Slight, Serious. This child node indicates the corrosion level of a gas pipeline. The 'slight state' shows a small crack in the pipes and the gas leakage rate is low, while the 'serious state' indicates that the pipeline is seriously damaged and needs to be replaced, and it cannot transport the pressured gas.
28) Defect of Gas Pipeline, state: Slight, Serious. This child node represents small-scale damage of a gas pipeline. The 'slight state' means that the surface of the pipeline is characterized with slight deformation, but its function is still normal. The 'serious state' indicates that thepipeline is broken, possibly causing a small amount of gas leakage.
29) Misoperation, state: Slight, Serious. This child node describes the consequence level of incorrect human operation. The slight state means that even though the worker makes some incorrect operation the pipeline will not break down. The serious indicates this kind of mistake would directly cause a pipeline accident.
30) Destruction of Gas Compartment, state: Slight, Moderate, Serious. This child node indicates the damage level of gas compartment that can be separated into three states. The slight state means the framework of compartment is fine, only a few of facilities in the utility tunnel are damaged. The moderate state represents the concrete wall has some cracks, while the serious state means the framework and structure of the gas compartment is damaged.
31) Coating Spalling, state: Slight, Moderate, Serious. This child node represents the working situation of coating in the gas pipes. The slight state means the overall coating is good and only a few part is spalling, the moderate state represents the coating is exfoliated, and the serious state means the function of coating is lost.
32) Acid Medium Overproof, state: Yes, No. This child node indicates the effect of different acid medium in the gas pipes.
33) Unreasonable Design, state: Yes, No. This child node indicates the effects of different unit design.
34) Installation Defect, state: Slight, Serious. This child node describes the incorrect action of installation. The slight state means the function of facilities is still normal but the location and height may not reach the standard, while the serious state represents the installed facilities are

35) Gas Pipeline Leakage, state: Slight, Serious. This node is the central event of gas pipeline accident in utility tunnel. A slight gas pipeline leakage would cause a small-scale damage but the serious gas leakage may result in severe secondary events.

In order to represent the consequences of a gas pipeline accident in utility tunnel, five more nodes are implemented: "Near Miss", "Poisoning", "Minor Damage", "Significant Damage", and "Catastrophic Damage". The states of them are set as either Yes or No. "Near Miss" means no human death and only a small amount of economic loss. "Poisoning" represents the consequences of an adverse diffusion of hazardous substances. According to the Chinese Safety Law and Regulation, "Minor Damage" means no more than 10 deaths or 50 injured, "Significant Damage" represents 11 to 30 deaths or 51 to 100 injured, and "Catastrophic Damage" indicates more than 30 deaths or more than 100 injured (State Council Order No. 493 of China, 2007).

# 3.2.2 Conditional Probability Tables (CPTs) 

Normally, the conditional probabilities of Bayesian nodes are obtained by the parameter learning method, the expert scoring method, or the combination of these two methods (Cooper and Herskovits, 1992; Trucco, et al., 2008). The parameter learning technique should be working based on sufficient data. However, there is few historical data or accident records of gas pipeline accidents in a utility tunnel, and therefore it is pretty hard to determine the BN CPTs by parameter learning. In this study, the CPTs of the nodes with binary states are calculated through the logic gate of BT diagram established in Section 3.1. As for the CPTs of the nodes with multi-states, an expert scoring method (the Delphi method) is employed. The Delphi method has been prove to be an alternative and feasible to derive a BN in various areas (Trucco et al., 2008; Nordgard and Sand, 2010; Kim et al., 2013; Mbakwe et al., 2016; Tong et al., 2018).

In the Delphi method, expert judgements are normally collected from experts via questionnaires, and in order to obtain consistent data, sometimes the experts will be consulted for multiple (two to five) times. Compared to the Dempster-Shafer evidence theory, the Delphi method could avoid "one-vote" selecting situation during the process of collecting different opinions from experts (Tong et al., 2018). The Cronbach's Alpha is generally used to examine whether these experts' opinions achieve a consistency (the value equals to or is greater than 0.9 )

In this study, we invited five experts who have professional knowledge and experience in research and engineering practice regarding gas pipeline accidents in a utility tunnel. These experts' data obtained via questionnaires was collected twice, in the case that these five experts didn't reach a consensus in the first round judgement. Herein, we take the process of determining CPTs of node "Installation Defect" as an example. The expert opinions we collected are shown in Table 4. In Table 4, S1 to S5 represent the opinions of five experts and the values below this row are the opinions given by the five experts according to the combination of their three parent nodes' states. In the second round data collecting, the Cronbach's coefficient Alpha gets to 0.995 , which represents that these five experts reach a consensus among the probability distribution of the "Slight" state of "Damage of Gas Compartment". In this case, the probability of CPTs is obtained through calculating the mean value of the data from the five experts' estimation.

Through this methodology, all the CPTs of Bayesian nodes can be obtained, and then the BN of a gas pipeline leakage in a utility tunnel is established, as shown in Fig. 7. In this study, the BN probability inference is conducted using Netica (Netica 4.16, Norsys Software Corp), which has been widely used in Bayesian network analysis.

[^0]
[^0]:    BLEE [LZ-T3]: Has this method been carried out before? Can you add reference for this?
    Response: Actually, we added references above: "The Delphi method has been prove to be an alternative and feasible to derive a BN in various areas (Trucco et al., 2008; Nordgard and Sand, 2010; Kim et al., 2013; Mbakwe et al., 2016; Tong et al., 2018)."

340 Table 4 341 An example of the application of Delphi method

Interference | Industrial Activity | Natural Hazards | S1 | S2 | S3 | S4 | S5 |  |  |   |

![img-7.jpeg](img-7.jpeg)

Fig.7. Bayesian network of a gas pipeline leakage in a utility tunnel

# 3.3. Results and discussion 

In this study, the combination of BT and BN are used to carry out a quantitative risk analysis (QRA) of a gas pipeline leakage. As mentioned above, the probability calculation in BT depends on the logic gate relationship between events. The event tree is processed by "and" gates. BN obtains the corresponding probability based on BN inference by giving specific evidence. In addition, by using the back-deduction function of the Bayesian network that is not available in BT, we can obtain the updated probability of each primary event when the gas pipeline leakage occurs. This is helpful to determine the critical threats of gas pipeline leakage according to the variance of prior and posterior probabilities. Besides, a sensitivity analysis (SA) is used to verify the reasonability of the identified critical threats.

### 3.3.1 Accident consequence probability calculation

An attractive advantage of BT and BN is that they can predict the occurrence probability of various accident scenarios and the corresponding consequences. BT can calculate the probability of accident consequences through the logic gate rule, while BN can obtain the posterior probability through BN inference algorithms by giving evidences of some specific nodes. Based on the proposed BT and BN for gas pipeline leakage in utility tunnel in Section 3.1 and 3.2, the probability of gas pipeline leakage is estimated to be 9.28E-02 and 3.88E-02 respectively, and the estimated probabilities of accident consequences are presented in Table 5. It is shown that the probability of an accident calculated by BT is greater than that from BN. The probability of "Near Miss" calculated by BT is almost twice of that calculated by BN. The interdependence of events of BN is responsible for the difference between the outcomes. In a real-world accident, every event during the accident escalation is related. Therefore, the result of BN is more reliable. Besides, the most likely accident consequence of the two methods is "Poisoning" and "Minor Damage" and the probability of the most serious accident consequence ("Catastrophic Damage") is minimal. The calculated results of the two models are 1.04E-06 and 4.44E-07.

Table 5
371 Estimated probability of consequences of gas pipeline leakage in utility tunnel


# 3.3.2 Critical threats identification and analysis 

An attractive application of the Bayesian network analysis is the back-deduction or probability updating if new evidence comes avaliable, which is limited in BT. Given the fact that a gas pipeline leakage in a utility tunnel has occurred, the probabilities (named posterior probability) of its parent nodes and the corresponding accident consequences can be automatically updated. This is a practical feature as we can quickly get variances of probability changes of the root nodes. The node with the largest probability change could be identified as the critical threat of this gas pipeline leakage accident, based on which we can perform specific risk reduction and mitigation strategies. Table 6 shows the estimated posterior probabilities of the root Bayesian nodes given the gas pipeline leakage accident occurring. The variance level of the posterior probabilities of all the root Bayesian nodes is presented in Fig. 8. The variance level is calculated as follows (Aven and Nøkland, 2010):

$$
R L=\frac{P_{\text {priorit }}-P_{\text {prior }}}{P_{\text {prior }}}
$$

Where $R L$ represents the variance level of the probability changes of each nodes when the new evident comes. $P_{\text {posterior }}$ and $P_{\text {prior }}$ indicate the probability of each node before and after the new evidence given to the BN.

As shown in Fig. 8 and Table 6, the Bayesian nodes that are related to human factor, i.e., "Misoperation of Supporting Structure Construction" (X18), "Incorrect Maintenance" (X19), and "Unreasonable Operation" (X20), are the most critical potential events. The nodes "Natural Hazards" (X2), "Third-party Interference" (X3), and "Industrial Activity" (X4) are the second-level key events of a gas pipeline leakage in a utility tunnel, with variance levels of 1.73, 1.64 and 1.49 , respectively. These factors should therefore obtain more attention during the design, construction, and maintenance procedure of the gas pipeline in utility tunnel.

Table 6
The posterior probability of root nodes



![img-8.jpeg](img-8.jpeg)

Fig.8. The variance level of the root Bayesian nodes (ratio)
Furthermore, we performed a sensitivity analysis (SA) to verify the reasonability of the identified critical threats to a gas pipeline accident in a utility tunnel. SA is a widely used method for examining and ranking critical Bayesian root nodes to the target event (Matellini et al., 2013). In this study, we use the "Sensitivity to Findings" function in Netica (the influence level of every root node can be calculated rapidly) to obtain the maximal percentage contribution of a gas pipeline leakage as shown in Fig. 9 (only the first seven higher influencing nodes are chosen, seen in Fig. 9). To be specific, the contribution of node "Incorrect Maintenance" (X19) is the greatest with the proportion of 0.718 . This result is consistent with the result of the probability updating method (variance level evaluation) as shown in Fig. 8. Besides, in the SA, the node "Weld Flaw" (X16) tends to contribute a lot to a gas pipeline leakage with a calculated value of 0.611 . An explanation is that the repaired parts are weak, and a secondary accident would occur in the weak part. Therefore, "Weld Falw" and "Incorrect Maintenance" are both considered as the critical threats of a gas pipeline leakage. The results show that the combination of these two methodologies can quickly determine the critical threats of a gas leakage accident in a utility tunnel.

![img-9.jpeg](img-9.jpeg)

Fig.9. The sensitivity value (proportion) of some root nodes

# 3.3.3 Accident scenario predictive Analysis 

Predictive analysis is an important characteristic of the BN method, which can quantitatively model a real accident scenario by giving some root nodes with certain states. Through predictive analysis, we can not only obtain the evolution process of a gas pipeline leakage caused by a specific accident scenario, but also obtain the probable consequences of this accident scenario.

In this study, a typical accident scenario with multiple effects of some critical threats and commonly-presented events of a gas pipeline accident in a utility tunnel is examined. In the BN modeling, some root nodes are given certain states (the nodes with one state value set as $100 \%$ as grey background shows in Fig. 10). "High Water Content" and " $\mathrm{H}_{2} \mathrm{~S}$ Content Overproof" generally exist during the transport of gas, and thus are given the "Yes" state. "Weld Flaw" and "Mechanical Damage" are the most contributing factors to the defect of installation, which is vulnerable to give rise to a small-scale gas leakage, and these two nodes are also given "Yes" state. Besides, "Unreasonable Operation" is identified as a critical threat with respect to a gas pipeline leakage, and it is given a "Yes" state, which is also selected by the experts as a common problem in gas pipeline accidents.

As shown in Fig.10, the occurrence probability of a gas pipeline leakage is $29.7 \%$. Besides, "Near Miss" occupies the biggest probability of accident consequence with a probability of $7.17 \%$, while "Significant Damage" holds the probability of $0.43 \%$, and "Poisoning" $0.34 \%$. Although the

total probability of "Significant Damage" is small ( $0.43 \%$ ), the accident consequence could be catastrophic, as this node indicates 11 to 30 deaths or 51 to 100 injured. The proportion of "Minor Damage" is acceptable, and the value is $0.46 \%$. Furthermore, this accident scenario indicates no "Catastrophic Damage" would happen when the "Fireproof Facility", "Fire/Explosion Isolation" and "Evacuation" are under a good situation. Overall, the predictive results are consistent with reality, which implies that we have a reasonable tool for rapid risk assessment under emergency decision making in case of gas pipeline accidents in a utility tunnel.

![img-10.jpeg](img-10.jpeg)

Fig. 10. A real-world accident scenario modeling

# 4. Conclusion 

This study illustrates the application of the combination of Bow-tie diagram and Bayesian network for the risk analysis of a gas pipeline in an underground utility tunnel. The flexible framework overcomes the limitation of the Bow-tie diagram (such as binary nodes and being a static analysis). Furthermore, the BN methodology incorporating previous accident data and expertise are lead toa more reliable probabilistic analysis. The specific conclusions are given below.

A 43-node BN based on the proposed Bow-tie diagram is established to present a dynamic risk assessment of a gas pipeline leakage in a utility tunnel. The probabilities of various accident consequences of a gas pipeline accident in a utility tunnel are calculated through Bayesian inference. The estimated consequences highlight the importance of considering the conditional dependency of each event in the evolution process of gas pipeline accident in a utility tunnel.

Taking advantage of the probability updating and sensitivity analysis, the "Incorrect Maintenance" and "Weld Flaw" are identified to be the critical threats to a gas pipeline accident in a utility tunnel. The predictive analysis results shows that given the occurrence of some critical events (nodes), the gas pipeline accident in a utility tunnel doesn't lead to a "Catastrophic Damage" if the safety barriers like "Fireproof Facility", "Fire/Explosion Isolation" and "Evacuation" are under a good working condition.

## Acknowledgments

This work was supported by the National Key Research and Development Program of China (Grant No. 2017YFC0805001), the National Natural Science Foundation of China (Grant No. 11502283) and the Yue Qi Young Scholar Program of China University of Mining \& Technology, Beijing.

ReferencesAmin, M. T., Khan, F., Imtiaz, S., 2018. Dynamic availability assessment of safety critical systems using a dynamic bayesian network. Reliability Engineering \& System Safety.

178, 108-117.

抵注 [LZ-T4]: don't understand what you want to say. please re-formulate
Response: re-formulate above

Arzaghi, E., Abaei, M. M., Abbassi, R., Garaniya, V., Binns, J. R., Chin, C., Khan, F., 2018. A hierarchical Bayesian approach to modelling fate and transport of oil released from subsea pipelines. Process Safety \& Environmental Protection. 118, 307-315.

Aven, T, Nøkland, T. E. On the use of uncertainty importance measures in reliability and risk analysis, 2010. Reliability Engineering \& System Safety. 95(2), 127-133.

Bellamy, L. J., Mud, M., Manuel, H. J., Oh, J. I. H., 2013. Analysis of underlying causes of investigated loss of containment incidents in Dutch Seveso plants using the story builder method. Journal of Loss Prevention in the Process Industries. 26(6), 1039-1059.

Broere, W., 2016. Urban underground space: solving the problems of today's cities. Tunnelling \& Underground Space Technology Incorporating Trenchless Technology Research. 55, 245-248.

Canto-Perello, J., Curiel-Esparza J., 2013. Assessing governance issues of urban utility tunnels. Tunnelling and Underground Space Technology. 33(1), 82-87.

Canto-Perello, J., Curiel-Esparza, J., Calvo, V., 2013. Criticality and threat analysis on utility tunnels for planning security policies of utilities in urban underground space. Expert Systems with Applications. 40(11), 4707-4714.

Chen, J., Jiang, L., Li, J., Shi, X., 2012. Numerical simulation of shaking table test on utility tunnel under non-uniform earthquake excitation. Tunnelling and Underground Space Technology incorporating Trenchless Technology Research. 30(4), 205-216.

Chen, J., Shi, X., Li, J., 2010. Shaking table test of utility tunnel under non-uniform earthquake wave excitation. Soil Dynamics \& Earthquake Engineering. 30(11), 1400-1416.

Cooper, G. F., Herskovits, E., 1992. A Bayesian method for the induction of probabilistic networks from data. Machine Learning. 9(4), 309-347.

Curiel-Esparza, J., Canto-Perello, J., 2005. Indoor atmosphere hazard identification in person entry urban utility tunnels. Tunnelling \& Underground Space Technology. 20(5), 426-434.

Ferdous, R., Khan, F., Sadiq, R., Amyotte, P., Veitch, B., 2011. Fault and event tree analyses for process systems risk analysis: uncertainty handling formulations. Risk Analysis. 31(1), 86-107.

Han, Z. Y., Weng, W. G., 2010. An integrated quantitative risk analysis method for natural gas pipeline network. Journal of Loss Prevention in the Process Industries. 23(3), 428-436.

Kabir, G., Sadiq, R., Tesfamariam, S., 2015. A fuzzy Bayesian belief network for safety assessment of oil and gas pipelines. Structure \& Infrastructure Engineering. 12(8), 874-889.

Khakzad, N., Khana, F., 2012. Dynamic risk analysis using bow-tie approach. Reliability Engineering \& System Safety. 104(104), 36-44.

Khakzad, N., Khan, F., Amyotte, P., 2011. Safety analysis in process facilities: comparison of fault tree and bayesian network approaches. Reliability Engineering \& System Safety. 96(8), 925-932.

Khakzad, N., Khan, F., Amyotte, P., 2013. Dynamic safety analysis of process systems by mapping bow-tie into Bayesian network. Process Safety \& Environmental Protection. 91(1-2), 46-53.

Kim, S., Kim, Y. E., Bae, K. J., Choi, S. B., Park, J. K., Koo, Y. D., et al. 2013. Nest: a quantitative model for detecting emerging trends using a global monitoring expert network and Bayesian network. Futures. 52(6), 59-73.

Li, X., Chen, G., Zhu, H., 2016. Quantitative risk analysis on leakage failure of submarine oil and gas pipelines using Bayesian network. Process Safety \& Environmental Protection. 103,

Mbakwe, A.C., Saka, A.A., Choi, K., Lee, Y.J., 2016. Alternative method of highway traffic safety analysis for developing countries using delphi technique and Bayesian network. Accident Analysis \& Prevention 93, 135-146.

Matellini, D. B., Wall, A. D., Jenkinson, I. D., Wang, J., Pritchard, R. 2013. Modelling dwelling fire development and occupancy escape using Bayesian network. Reliability Engineering \& System Safety. 114(1), 75-91.

Martins, M. R., Schleder, A. M., Droguett, E. L., 2014. A methodology for risk analysis based on hybrid Bayesian networks: application to the regasification system of liquefied natural gas onboard a floating storage and regasification unit. Risk Analysis. 34(12), 2098.

Ministry of Housing and Urban-Rural Development of Shanghai (MHUD of Shanghai), 2012.
Nordgard, D.E., Sang, K., 2010. Application of Bayesian networks for risk analysis of MV air insulated switch operation. Reliability Engineering \& System Safety. 95(12), 1358-1366.

Paltrinieri, N., Tugnoli, A., Buston, J., Wardman, M., Cozzani, V., 2013. Dynamic procedure for atypical scenarios identification (DyPSI): a new systematic HAZID tool. Journal of Loss Prevention in the Process Industries. 26(4), 683-695.

Ruijter, A. D., Guldenmund, F., 2016. The bowtie method: a review. Safety Science. 88, 211-218.
Su, H., Zio, E., Zhang, J.J., Li, X.Y., 2018. A systematic framework of vulnerability analysis of a natural gas pipeline network. Reliability Engineering \& System Safety. 175, 79-91.

State Council Order No. 493 of China, 2007. Production safety accident report, investigation and handling regulations. (http://www.gssafety.gov.cn/zwxxgk/article.php?id=291)

Shen, K.L., Wang, W.H., Wang, J.Y., Liu, H., Yi, J., 2016. The Failure Probability Analysis of City

Gas Pipeline Network Based on Fault Tree Analysis and Bayesian Network. Academic annual meeting of the Institute of public safety and science and technology. Pp.1:131-138.

Tong, X., Fang, W., Yuan, S., Ma, J., Bai, Y., 2018. Application of Bayesian approach to assessment of mine gas explosion. Journal of Loss Prevention in the Process Industries.54, $238-245$.

Wu, J., Zhou, R., Xu, S., Wu, Z., 2017. Probabilistic analysis of natural gas pipeline network accident based on Bayesian network. Journal of Loss Prevention in the Process Industries. 46, $126-136$.

Wittberg, P., 2012. Overview on Bayesian networks applications for dependability, risk analysis and maintenance areas. Engineering Applications of Artificial Intelligence. 25(4), 671-682.

Wang, T.Y., Tan, L.X., Xie, S.Y., Ma, B.S., 2018. Development and applications of common utility tunnels in China. Tunnelling \& Underground Space Technology. 76:92-106.

Yuan, Z., Khakzad, N., Khan, F., Amyotte, P., 2015. Risk analysis of dust explosion scenarios using Bayesian networks. Risk analysis 35(2): 278-291.

Zarei, E., Azadeh, A., Khakzad, N., Aliabadi, M. M., Mohammadfam, I., 2016. Dynamic safety assessment of natural gas stations using Bayesian network. Journal of Hazardous Materials 321: 830-840.

Zhang, J.W., Ma, Q.C., Zhang, L.B., 2014. Risk analysis of urban gas pipeline failure based on Fault Tree Analysis and Bayesian Network. Journal of Beijing Institute of Petrochemical Technology. 3:32-36.

Zhao, Y. C., Zhu, G. Q., Gao, Y. J., Tao, H. J., 2018a. Study on temperature field of fire smoke in utility tunnel with different cross sections. Procedia Engineering. 211, 1043-1051.

558 Zhao, Y. C., Zhu, G. Q., Gao, Y. J., 2018b. Experimental study on smoke temperature distribution under different power conditions in utility tunnel. Case Studies in Thermal Engineering. 12, $69-76$.

561 Zangenehmadar, Z. Moselhi, O., 2016. Prioritizing deterioration factors of water pipelines using Delphi method. Measurement 90, 491-499.