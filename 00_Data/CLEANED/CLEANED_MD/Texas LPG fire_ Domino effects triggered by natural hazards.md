Elsevier required licence: © <2018>. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

# Texas LPG Fire: Domino Effects Triggered by Natural Hazards 

Mohsen Naderpour ${ }^{1}$<br>Centre for Artificial Intelligence (CAI), School of Systems, Management, and Leadership, Faculty of Engineering and IT, University of Technology Sydney (UTS), Sydney, Australia<br>Mohsen.Naderpour@uts.edu.au

## Nima Khakzad

Safety and Security Science Group, Faculty of Technology, Policy, and Management, Delft University of Technology, Delft, The Netherlands
N.KhakzadRostami@tudelft.nl


#### Abstract

On February 2007, a massive fire in a propane de-asphalting unit in an oil refinery in Texas, USA happened due to liquid propane release from a cracked pipe in a control station injuring four people, damaging extensive equipment, causing significant business interruption, and resulting in more than $\$ 50$ million losses. The accident was triggered by a natural hazard: freezing of piping at a control station caused an inlet pipe elbow to crack, which in turn, led to the release of high-pressure liquid propane which was rapidly ignited. In addition, there were two near-miss events due to potential domino effects. In fact, the accident could reasonably have resulted in much more severe consequences due to the exposure of large butane storage spheres and chlorine containers, increasing the possibility of a catastrophic domino effect. This paper develops a Natech (natural hazard triggering technological disasters) risk assessment methodology that relies upon Bayesian network capabilities and takes into account the potential Natech domino effects. The methodology is implemented in the intended refinery and mathematically graphically represents the dynamic cause-effect relations between units involved in the scenario, and handles uncertainties among the interactions. In addition, the methodology can provide a risk value for the entire scenario that can be used further for risk-based decision making.


Keywords: Natech accident, Risk assessment, Domino effect, Bayesian network.

## 1. Introduction

On Friday 16 February 2007, workers at Valero Refinery in Sunray, Texas, USA witnessed a highpressure liquid propane release in a propane de-asphalting (PDA) unit. The propane vapour immediately ignited and injured three employees who were seriously burned, and one fire fighter with minor burn.

[^0]
[^0]:    ${ }^{1}$ Corresponding author, Tel: +61 295142644

The unit piping and equipment were extensively damaged and a major pipe rack nearby collapsed due to the impingement of subsequent jet fire. Adjacent units including four liquefied petroleum gas (LPG) storage tanks and three chlorine (a highly toxic gas) storage cylinders were seriously threatened by the primary fire. High and shifting winds and the rapid spread of the fire hampered fire-fighting efforts. Due to serious consequences, the plant was completely shut down for two months and had to operate for one year with reduced capacity. According to the US Chemical Safety Board (CSB) investigation report (CSB, 2008), the propane release likely happened because of a high-pressure piping failure due to freezing of a control station which had not been in service for approximately 15 years. The control station had been neither completely isolated from the process vessel nor freeze-protected, forming a dead-leg. During cold weather prior to the accident, accumulated water in a pipe elbow of the control station became frozen and cracked the pipe elbow. On the day of the accident, when the air temperature rose, the ice melted and allowed the release of 4,500 pounds per minute of liquid propane from the failed pipe. The propane vapour travelled in wind direction and found an ignition source probably in the boiler house, leading to a flash fire and subsequent jet fires and fire balls. Direct losses of the accident were estimated more than $\$ 50$ million (CSB, 2008). The fire could have created a worse industrial process accident due to the possibility of domino effects.
The event at Valero Refinery is just one example of industrial accidents triggered by natural hazards that nowadays are referred to as "Natech" and are considered as an emerging risk which is likely to be exacerbated by ongoing climate change and growing industrialization (Krausmann et al., 2011). All over the world, Natech accidents occur in the wake of natural hazards such as earthquakes, floods, volcanos, and severe weather, resulting in hazardous substances release leading to human fatalities and injuries, environmental pollution, and economic losses. Some examples among others are the Fukushima power station disaster after the Tohoku earthquake in 2011 (Morino et al., 2011), the fire in a major refinery in Turkey during the Kocaeli earthquake in 1999 (Steinberg and Cruz, 2004), the release of hazardous materials due to the Asian tsunami in 2004, and the ignition of eight tanks due to lightning during a rainstorm in 1994 in Egypt (Renni et al., 2010).
Natechs are even able to create worse consequences due to domino effects (Cozzani et al., 2014) in which a primary accident starting in a unit spreads to adjacent units, causing secondary accidents the total consequence of which could be much more severe than the primary event. Therefore, effective methodologies are required to model and assess Natech risk and evaluate the effectiveness of corresponding safety policies. Currently, there are a number of regulations for building industrial plant structures to resist natural hazards up to the design-level event (Cruz and Okada, 2008). In addition, there are few laws to ensure that the correct emergency responses are conducted during natural hazards concerning the performance of non-structural elements and safety measures (Girgin and Krausmann, 2013). It is worth noting that the releases of chemicals triggered by natural hazards are not always because of structural failures. They can also happen because of the failure of back-up or safety systems that are installed to prevent such accidents in the first place (Cruz and Okada, 2008). In addition, current

Natech risk analysis methodologies are limited only to some guidance for industry and authorities on how to assess risk (Krausmann et al., 2011). All of these highlight the importance of new methodology development to assist industry in dealing with Natechs (Cozzani et al., 2014; Landucci et al., 2014; Necci et al., 2016). Therefore, this paper is aimed at demonstrating the importance of considering the role of Natechs in modelling and risk assessment of domino effects.
The rest of this paper has been organized as follow: Section 2 presents the fundamental backgrounds of Natechs, domino effects, and BNs; the methodology is developed in Section 3 while its demonstration to Valero case study is presented in Section 4; conclusions are presented in Section 5.

# 2. Background 

### 2.1. Natech hazards

Natechs are referred to accidents in which the natural world and technological plants collide, leading to explosions, fires or the release of hazardous materials. Natechs often produce severe consequences as proven by past Natechs, affecting people, properties and the environment (El Hajj et al., 2015). Natural hazards can be categorised into four groups including geological, meteorological, hydrological, and climatic. Each category includes a number of hazards as presented in Table 1.

Table 1. Natural hazard categories (Girgin and Krausmann, 2016).


A recent investigation has identified 347 Natechs from 1986 to 2012 in the US pipeline network used for transferring hazardous liquids such as crude oil, refined petroleum products and other highly volatile liquids. Among these Natechs, 76 accidents (i.e. $21 \%$ ) are attributed to freeze-triggered accidents which are in the focus of this paper (Girgin and Krausmann, 2016).

### 2.2. Natech legal frameworks

In many countries, there are frameworks and programs for major accidents prevention and mitigation. However, only a few countries have taken steps to prevent or prepare for Natech disasters. This section reviews the current Natech risk management practices in the United States, Europe, and Japan:

- In the US, two regulations including the process safety management (PSM) regulation and risk management plan (RMP) rule are playing the major role in preventing major industrial accidents. According to these requirements, industries need to carry out the process safety analysis, maintain the process safety information, evaluate the current mitigation measures and

standards, and develop training and maintenance programs. In addition, human, health and the environment are protected through the emergency response programs by considering safety measures and introducing procedures for notifying the public and local agencies. However, natural hazards are not explicitly considered by these regulations, and there are no specific provisions in the both regulations to prevent, for instance, domino effects triggered by natural disasters. The only legislation in the US which specifically deals with natural hazards is the California accidental release prevention (CalARP) program which calls for the risk assessment of potential releases due to earthquakes and requires prevention and mitigation measures to avoid the release of certain hazardous substances during earthquakes (Cruz and Okada, 2008). However, CalARP does not take into account the possibility of Natech-related domino effects and the protective role of land use planning.

- In Europe, the Seveso III Directive (2012) plays the main role in preventing chemical accidents. Under the Seveso III, industrial facilities which store, use or handle dangerous substances are required to set out major-accident prevention policies, to write and submit safety reports, and to establish emergency plans to deal with accidental releases of hazardous materials. Seveso III mandates the member states to consider the probability of natural disasters in the risk assessment of major accident scenarios when preparing safety reports (Article 10), with an explicit mention of floods and earthquakes in the Annex II. The most of European countries that consider Natechs have thus limited their programs mainly to floods and earthquakes among other natural hazards.

The directive also does not specify any methods or actions to achieve these requirements. Compared to the US regulations, however, the Seveso III considers the analysis of potential domino effects and emphasizes the establishment of land-use policies, both of which are very important in addressing Natech risk assessment as domino effects are more likely during natural disasters than during normal plant operations (Cruz and Okada, 2008).

- In Japan, the prevention and management of chemical accidents are regulated by various laws. The only regulation explicitly addressing Natech risk is the amended high-pressure gas safety (HPGS) law which requires industrial establishments to take all additional measures necessary to reduce the accident risk from earthquakes and tsunamis (Krausmann and Baranzini, 2012). As can be noted from the foregoing regulations and directives, they usually fall short in addressing the Natechs in risk assessment and management studies (e.g., in the US) or have a rather limited scope (e.g., in Europe and Japan), ignoring a wide range of other natural disasters with potentially catastrophic impacts on industrial plants.

# 2.3. Natech risk analysis 

Due to the specific nature of Natech, its risk has been considered as an emerging risk issue in Europe under the iNTeg-Risk program project (Krausmann et al., 2011). There are plenty of risk analysis methodologies to assess the risk of conventional industrial accidents during day-to-day operations. Recently, there have been some attempts for risk assessment of Natechs triggered by earthquake, flood and lighting (Campedel et al., 2008; El Hajj et al., 2015; Landucci et al., 2014; Lanzano et al., 2015; Necci et al., 2013).

For example, Rapid Natech Assessment and Mapping Tool (RAPID-N) has been developed for accidents caused by earthquakes, based on the estimation of on-site natural hazard parameters, determination of damage probabilities of units, and assessment of probability and severity of possible consequences (Girgin and Krausmann, 2013). RAPID-N, however, is merely applicable to earthquakes. Antonioni et al. (2009) have extended the standard quantitative risk assessment procedures to accommodate industrial accidents caused by earthquakes and floods using equipment damage models available in the literature. The damage model of horizontal cylindrical vessels in case of floods has been developed by Landducci et al. (2014). Khakzad and van Gelder (2018) used Bayesian network modelling to fragility assessment of industrial plants exposed to floods. There are also a number of studies that investigate accident databases to explore both the potential of natural hazards in causing Natechs and the characteristics and damage state of affected units; among others is work of Cozzani et al. (2014) and El Hajj et al. (2015), both in the context of flood-induced Natechs. Nevertheless, the methodologies for risk analysis of Natechs triggered by climatic severe conditions such as freezing (Table 1) are very limited, to the best knowledge of authors.

### 2.4. Domino effects

A domino effect also known as cascading events or knock-on accidents is referred to a chain of accidents where physical effects of a primary accident such as the blast wave of an explosion, heat radiation of fire, or fragments projected due to a vessel explosion trigger secondary accidents in nearby units (Reniers and Cozzani, 2013). These physical effects are also known as escalation vectors. Process plants due to high complexity and interdependencies of units containing hazardous materials usually at hightemperature and high-pressure conditions have the potential to be affected by catastrophic domino effects due to an engineering accident or a Natech.

Past accidents analysis indicates that accidental scenarios in the presence of a relevant domino effect share three features (Salzano and Cozzani, 2012): a) there is a primary accident which initiates the domino accidental sequence. In this paper, the primary event is considered to be a freeze-induced Natech; b) there is at least one secondary unit/equipment which is damaged due to the physical effects of the primary incident; c) due to damage of secondary unit/equipment, one or more secondary events such as fire, explosion, or toxic dispersion occur.

A number of factors contribute to the probability of accident propagation or escalation probability. More important factors include: a) the distance between the primary and secondary units, b) the type and storage of chemicals involved, and c) the vulnerability of the secondary units to the exposure of a primary event. In addition, it is usually assumed that for a secondary unit to be impacted by the escalation vector of a primary unit, the escalation vector intensity at the location of the secondary unit should be higher than a corresponding threshold value (Cozzani et al., 2006). Probit models are widely used for calculation of escalation probabilities in a wide variety of accident scenarios involving units with different vulnerabilities and with different escalation vectors. The type of process units, for example pressurized or atmospheric, and the type of escalation vector threatening the secondary units, for example overpressure or heat radiation, play important roles in calculation of probit values. A probit value $Y$ can be defined as follows:

$$
Y=a+b * \ln (D)
$$

where $a$ and $b$ represent probit coefficients, and $D$ is either the escalation vector intensity received by or relevant parameters such as $t t f$ (time to failure) of the secondary unit/equipment. Table 2 presents some probit models that are used for vulnerability analysis of process equipment exposed to heat radiation. As can be seen, the probit value $Y$ is calculated based on $t t f(\mathrm{~s})$ of the secondary unit, the heat radiation $Q\left(\mathrm{~kW} / \mathrm{m}^{2}\right)$ received by target unit, and the volume $V\left(\mathrm{~m}^{3}\right)$ of the secondary unit. After that, the escalation probability can be estimated based on the cumulative density function of the standard normal distribution $\Phi$ as:

$$
P_{E}=\Phi(Y-5)
$$

Table 2. Probit models for heat radiation (Cozzani et al., 2005).


For spreadsheet applications, the escalation probability can alternatively be approximated as:

$$
P_{E}=50\left\{1+\frac{Y-5}{|Y-5|} \operatorname{erf}\left(\frac{|Y-5|}{\sqrt{2}}\right)\right\}
$$

where erf is the error function.

# 2.5. Bayesian networks 

A Bayesian network (BN) is a directed acyclic graph whose nodes represent random variables, and the arcs between nodes represent dependencies or direct causal influences thereof. The conditional probabilities (also known as parameters of BN which are represented within Conditional Probability Tables (CPTs)) assigned to the nodes determine the type and strength of the causal relationships among

the nodes. Each node in the BN has a set of collectively exhaustive and mutually exclusive states with a probability distribution conditional on the states of its parent nodes, or an unconditional probability distribution if the node does not have any parents. The conditional and unconditional probabilities can be learned from available data or elicited from domain experts. Based on the conditional independence resulting from the $d$-separation concept, and using the chain rule, BN represents the joint probability distribution $P(X)$ of the random variables $X=\left\{X_{1}, X_{2} \ldots, X_{n}\right\}$ included in the network as (Neapolitan, 2004):

$$
P(X)=P\left(X_{1}, X_{2}, \ldots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid p a\left(X_{i}\right)\right)
$$

where $p a\left(X_{i}\right)$ is the parent set of $X_{i}$ for $i=1, \ldots, n$. If $p a\left(X_{i}\right)$ is an empty set, then $X_{i}$ is a root node and $P\left(X_{i} \mid p a\left(X_{i}\right)\right)=P\left(X_{i}\right)$. BN uses Bayes theorem to update the prior probability of random variables given new information E (Naderpour et al., 2014b):

$$
P(X \mid E)=\frac{P(X) P(E \mid X)}{\sum_{X} P(X) P(E \mid X)}
$$

E, which is also called evidence, can be in form of equipment malfunction, system failure, or the variation of influential parameters such as temperature, pressure, or flow during system operation (Naderpour et al., 2014a).

# 3. Natech risk analysis methodology 

This section presents the proposed methodology for the Natechs risk assessment. To develop the methodology, a frequency assessment is required to estimate the likelihood of the natural event (e.g., flash flood) and to identify its parameters (e.g., flow velocity) contributing to the failure of impacted equipment. In addition, to have a comprehensive modelling, the consequences of the primary Natech event along with potentially subsequent domino effects need to be assessed. The proposed methodology as summarized in Figure 1 is described in the following steps:
Step 1: Determine the unit(s) of study, the focus is on the units that include the process vessels with credible amounts of hazardous materials.
Step 2: Identify the possible natural hazards at the geographical location of the intended facility. Table 1 provides a list of natural hazards that can be used as a reference at this step.
Step 3: For each possible natural hazard, present the influential parameters as nodes in the BN model. For each possible natural hazard, the following steps should be repeated.
Step 4: The target equipment in the environment is identified. The focus is on equipment with the potential of causing damage to human, assets, and the environment if impacted by the natural hazard. For each equipment, a node is created in the BN model with two states: safe and damaged.

Step 5: Identify the possible Natech scenarios while considering the natural hazard and possible damage to the equipment. For instance, in case of submersion of the storage tanks during floods, their floatation and consequent release of chemical contents should be considered as a scenario.

Step 6: Select one Natech and introduce a corresponding node in the BN model with two states: happening and not happening. The following steps should be completed for each Natech.
Step 7: Assess the frequency of the Natech by connecting the natural hazard node and the equipment node to the Natech node; the CPT of this node is similar to a logical AND gate.

Step 8: A consequence node is added to the BN model. The states of the consequence node are determined using event trees (ETs). For example, Figure 2 shows an ET for liquid release from a pipe with different consequences. An arc is drawn from Natech node to the consequence node.
![img-0.jpeg](img-0.jpeg)

Fig 2. Event tree for pipe release (Adopted from Ramírez-Camacho et al. (2016)).

Step 9: If there are any safety barriers in place to reduce the likelihood or mitigate the severity of Natech, each of them is represented by a node having two states, success and failure of the safety barrier. There are arcs between the nodes of safety barriers and the consequence node and also among the safety barriers themselves if their performance or failure probabilities depend on each other. The CPTs of the consequence node and the safety barrier nodes are completed according to the corresponding ET.

Step 10: According to layout of the process plant, critical units adjacent to the primary units (i.e., units which are more vulnerable to the natural event) are determined. Critical units usually refer to units with relevant inventories of flammable or explosive substances which have the potential to cause credible on-site or off-site damages. These units have potential to facilitate the propagation of primary Natech or an ongoing domino effect. These units are presented as nodes of the BN with two states: safe and accident.

![img-1.jpeg](img-1.jpeg)

Fig 1. Natech risk analysis methodology.

Step 11: Escalation vectors between the primary unit(s) affected by the natural event and the units identified in Step 10 (i.e., target units) are determined. Methods to calculate the intensity of escalation vectors can be found in (CCPS, 2000).
Step 12: Considering the predefined threshold values (e.g. Table 5 shows the threshold values for jet fire scenarios), escalation vectors which exceed the respective threshold will be considered in the modelling by drawing arcs from the primary unit(s) to the target units and so on.
Step 13: Probit functions can be used to estimate the damage probability (escalation probability) of target units.
Step 14: Among affected target units, those with the highest escalation probabilities are selected as secondary units. The secondary events are caused by the Natech; therefore, an arc is directed from the consequence node of the Natech to the secondary target unit(s).
Step 15: Potential accident scenarios considering the type of equipment, the type of substance released, and the type of damage (e.g., catastrophic rupture, vessel collapse, large breach on the shell, and pipe leakage) and their occurrence probabilities considering this fact that they have been damaged by the secondary events are specified.
Step 16: Considering Steps 10 to 14 for all the possible scenarios, the propagation pattern of the domino effect for the intended Natech can be developed in the BN. Therefore, the probabilities of the primary and secondary events can be calculated and the joint probability distribution of the events constituting the Natech-driven domino effect can be derived.
Step 17: If there is no domino effect, the Natech risk is calculated as the product of the probability and the severity of the consequences due to the Natech and the subsequent failure of the equipment. If there is a domino effect, the risk value includes the corresponding losses resulted from the domino effect as well. If there is more than one Natech, the methodology is repeated from Step 6, and if there is possibility of more natural hazards striking the industrial plant, the methodology restarts from Step 3.

# 4. Application 

The application of the proposed methodology is demonstrated to the Natech at Valero refinery, Sunray, Texas in 2007.

### 4.1. Propane de-asphalting unit

The purpose of the PDA unit was to recover fuel feedstock and paving-grade asphalt that were produced in the refinery. The PDA unit included two liquid extraction towers (hereafter, extractors) that used liquid propane as a solvent to extract gas oil from the pitch under an approximate pressure of 500 psi . The recovered gas oil (de-asphalted gas oil) was transmitted to another unit within the refinery to be processed into gasoline and the produced asphalt was sold to other companies to be used in paving materials.

Figure 3 shows the process flow diagram for Extractor 1, including the failure location due to freezing. The dense pitch enters the upper section of the extractor and flows to the bottom. Less dense liquid propane enters the extractor from a lower section and flows to the top. De-asphalted gas oil is extracted from the pitch and flows out of the extractor with much of the propane, which later be separated using a series of flash drums. There is another outflow from the bottom of the extractor that contains a mixture of asphalt and propane. This outflow is also heated and flashed to remove entrained propane from the asphalt. At various flashing steps, propane is extracted and transmitted to a low- and a high-pressure accumulators to be recycled to the extractors. However, a small amount of propane which accounts for about $0.5 \%$ of the circulating propane rate enters the low-pressure accumulator to replace losses. This makeup propane contains a variable amount of entrained water, which is regularly drained from the low points of the accumulator (CSB, 2008). During the days before the accident, water-contained makeup propane accumulated in a dead-leg due to a leaking gate valve, as depicted in Figure 4.
![img-2.jpeg](img-2.jpeg)

Fig 3. Extractor 1 flow diagram (CSB, 2008).
![img-3.jpeg](img-3.jpeg)

Fig 4. Control station flow diagram (CSB, 2008). The piping on left-hand side of the control station was out-of-service, forming a dead-leg.

# 4.2. Events timeline 

According to US National Weather Service, Texas typically experiences some periods of belowfreezing weather during the winter time which often happen in February. In 2007, the freezing temperature began on February $12^{\text {th }}$ for 87 hours. Even a temperature of $-15^{\circ} \mathrm{C}$ was recorded early in the morning of February $15^{\text {th }}$. The extended period of freezing weather and the lack of freeze protection on the control station in Extractor 1 allowed the water content of the accumulated propane to freeze, cracking the elbow pipe upstream of the control valve (see Figure 4). On February $16^{\text {th }}$, the frozen water inside the cracked elbow, which would have prevented propane from leaking out the crack by then, began to thaw due to rising weather temperature, leading to a release of liquid propane at a pressure of 500 psi. The generated vapour cloud was ignited a few minutes later, causing a series of massive fire. Unfortunately, the manual shut-off valves and pump on-off switches that could have been used to control the propane discharge were not accessible due to the size and intensity of the fire. Within minutes, the fire damaged piping and pipe rack supports, spreading further. As a result, the plant was totally evacuated (CSB, 2008).

### 4.3. Near-miss events

In this accident, there have been two extraordinary near-miss events that could have dramatically exacerbated the consequences of the accident. Near-misses resulted from the exposure of nearby equipment to heat radiation. If the wind direction had been different or if the personnel had been nearby, one of the worst industrial disasters in recent US history would have been witnessed (CSB, 2008). The first near miss was the exposure of four large (10,000-barrel capacity) butane storage spheres to the fire at PDA; radiant heat from the intense PDA fire blistered the paint on the closest butane storage sphere located 82 m northwest of Extractor 1 as shown in Figure 5. Fortunately, the wind moved the flames away from the butane storage. Even with the existence of favourable wind, fire fighters did not manage to reach the water deluge system valve which was designed to provide a flow of water over the sphere surface to prevent it from heating. As for the second near miss, three one-ton chlorine containers which were used for the cooling tower water treatment were subjected to radiant heat from the PDA unit. One container vented through its melted fusible plug that was installed to prevent the container rupture. The second container ruptured despite the operation of its fusible plug; the third one developed a leak through a partially melted plug. As a result, more than 2.5 tons of chlorine were released. Emergency responders and other refinery personnel had evacuated the area before the major chlorine release occurred. There is no evidence that personnel on- or off-site were exposed to hazardous levels of chlorine gas. However, if responders had been nearby when the cylinders released their contents, significant exposures could have occurred (CSB, 2008).

![img-4.jpeg](img-4.jpeg)

Fig 5. Aerial picture of the PDA unit after fire (CSB, 2008).

# 4.4. Natech domino effect modelling and risk analysis 

Figure 6 shows Extractor 1 and surrounding units that are considered in this analysis. The characteristics of the units are summarized in Table 3. It is worth noting that in the present study, the chlorine release is not considered as an escalation vector in domino effect analysis since it does not result directly in a loss of containment or damaging of other equipment. However, it needs to be taken into consideration for risk analysis due to its great potential to harm people and the environment. In addition, the nonfireproofed supported pipeline needs to be taken into account as its failure caused pipelines containing flammable materials to collapse, contributing further to the chain of accidents. For the sake of simplicity, all pipes involved are considered as one single pipe.

Table 3. Unit characteristics.


![img-5.jpeg](img-5.jpeg)

Fig 6. Extractor 1 (EX1) and surrounding units. The likely propagation of domino effect scenario, starting from EX1, has been presented in form of a BN.

# 4.4.1. Natech modelling 

To simplify the application of the proposed methodology, only freezing weather is considered as the natural hazard in the intended environment. In addition, the focus is on the dead-leg that caused the accident. To conduct Steps 1 to 9 of the proposed methodology, a preliminary BN with eight nodes is developed in Figure 7. The nodes, their states, and relevant probabilities are reported in Table 4. The weather temperature is considered as a node in the BN with two states: freezing and normal. The freezing probability for the intended area was estimated as 0.09 per year based on 10 years records at the US National Weather Service (www.weather.gov). The dead-leg of interest is represented as another node of the BN. This node has two states: safe and damaged due to freezing weather conditions. The failure probability of the dead-leg due to freezing is determined based on experimental results by Fleming and Lydell (2004), while other hardware failure probabilities were determined based on data available in the Offshore Reliability Data Handbook (OREDA, 2002). The states of the consequence node were identified as the Jet fire, Environmental pollution, and Safe. According to the CSB report, there was no safety barrier in the intended unit to prevent a freeze-triggered accident. In addition, there were safety barriers including manual isolation valve, and fire water monitors in place to reduce the severity of possible accidents, however; due to the fire extent they were damaged or impossible to be activated.

Table 4. The preliminary BN nodes and characteristics in Figure 7.


![img-6.jpeg](img-6.jpeg)

Fig 7. The preliminary BN to represent Steps 1 to 9.

# 4.4.2. Accident escalation modelling 

The preliminary BN is extended by adding nodes for surrounding credible units (Step 10). Considering jet fire scenario in EX1, direct fire impingement and heat radiation are taken into account. The escalation threshold values for heat radiation and fire impingement for atmospheric and pressure units are listed in Table 5 (Cozzani et al., 2006).

Table 5. Escalation thresholds for jet fire scenario (Cozzani et al., 2006).


To determine the possible secondary units, the intensity of heat radiation received by EX2, SP, NC, and BS1 in the case of a jet fire at EX1 are calculated by ALOHA software ${ }^{1}$ (Step 11). The following input data was used in ALOHA to calculate the magnitude of heat radiation at different locations: a wind speed of $10 \mathrm{~m} / \mathrm{s}$ measured at 3 m above the ground and gusting from the north east; air temperature of $10^{\circ} \mathrm{C}$; relative humidity of $50 \%$, a clear sky, and stability class of D. In addition, the diameter and the pressure of the pipe is roughly considered as 254 mm and 50 psia.

[^0]
[^0]:    ${ }^{1}$ www.epa.gov/cameo/aloha-software

The potential secondary units are SP and EX2 due to fire impingement and the heat radiation intensity of $49.9 \mathrm{~kW} / \mathrm{m}^{2}$, respectively (Step 12). The escalation probabilities are calculated by probit functions (Step 13). Accordingly, the causal arcs in the corresponding BN are directed from the node CO to the nodes SP and EX2 as shown in Figure 8 (Step 14). The CPT of these nodes given jet fire in EX1 is formed using calculated escalation probabilities. For example, Table 6 shows the CPT of EX2.

Table 6. The CPT of EX2.


Given that the secondary units have been damaged, potential accident scenarios and their occurrence probabilities are specified. In this case, catastrophic rupture of EX2 and collapse of SP are determined as the damage states of these two units (Step 15). Substituting the secondary units for the primary unit, Steps 11 to 15 are repeated to determine potential tertiary units, and so forth. It is worth noting that when repeating the same procedure for either the secondary units or higher-order units, synergistic effects should be considered (Khakzad et al., 2013). For example, EX1, EX2, and SP can cooperate with each other to trigger an accident in NC as the total heat radiation intensity produced is $19.17 \mathrm{~kW} / \mathrm{m}^{2}$ which is higher than the threshold value. Therefore, causal arcs are directed from CO (i.e. the consequence node of EX1), EX2, and SP to NC showing the conditional dependency of the latter on the former units. The synergistic impact of EX1, EX2, and SP on BS1 is $11.64 \mathrm{~kW} / \mathrm{m}^{2}$, which is less than the threshold value. Similarly, the cooperation of EX1, EX2, SP, and NC on BS1 is $13.56 \mathrm{~kW} / \mathrm{m}^{2}$. Therefore, the total produced heat radiation from primary, secondary, and tertiary events is not sufficient to affect butane spheres. The abovementioned modelling is reflected in Figure 8.
![img-7.jpeg](img-7.jpeg)

Fig 8. The BN model for propagation pattern.

# 4.4.3. Domino probability 

The probability of the domino effect is estimated at different levels by the developed BN. Generally, the probability of the domino effect $\left(P_{D}\right)$ is calculated as the multiplication of the probability of the

primary event $\left(P_{P}\right)$ and the conditional escalation probabilities of the impacted units $\left(P_{E}\right)$ (Khakzad et al., 2013):

$$
P_{D}=P_{P} * P_{E}
$$

The domino effect at the first level is calculated by assuming that the primary jet fire damages at least one of the nearby units, i.e., EX2 or SP. Therefore, the probability of the first-level domino effect is represented as:

$$
P_{L 1}=P(C O) * P(E X 2 \cup S P \mid C O)
$$

The domino effect propagates to the second level when at least a tertiary unit, i.e., NC, is impacted by the first-level domino accidents. Therefore, the probability of the second-level domino effect is as follows:

$$
P_{L 2}=P(C O) * P(E X 2 \cup S P \mid C O) * P(N C \mid C O, E X 2, S P)
$$

To facilitate the modelling, an auxiliary node called A1 with two states accident and safe is added to the BN model to represent $A 1=E X 2 \cup S P$ (see Figure 9). Two corresponding arcs from EX2 and SP are connected to A1 and the CPT of A1 is filled up considering an OR gate. Likewise, two other auxiliary nodes called L1 and L2 with two states accident and safe are added to the BN to calculate the probabilities of levels 1 and 2 of the domino effect.
![img-8.jpeg](img-8.jpeg)

Fig 9. The complete BN model for estimating the domino effect probabilities.

# 4.4.4. Natech risk assessment 

The BN model is analysed by Hugin researcher package $8.5^{1}$. The accident probabilities and the probability of the domino effect at sequential levels are listed in Table 7. Second column shows the prior probabilities before setting any evidence in the BN model. Considering the presence of freezing weather, pipe failure, and safety barriers failure in accordance with CSB report, the posterior probabilities are updated as shown in the third column of Table 7 (Step 16).

[^0]
[^0]:    ${ }^{1}$ www.hugin.com

Table 7. Domino effect probabilities.


* Posterior probability given pipe failure due to freezing weather and failure of safety barriers in accordance with CSB report.
Note: The probability of EX1 is equal to the probability of jet fire state in the CO node.
For any given accident, a total loss in a common currency in which human, asset, and the environmental losses are converted to money, is provided. Therefore, a risk value associated with the freeze-triggered Natech can be estimated. Last column in Table 7 for example shows estimated damages for each unit. The risk of the Natech is then calculated as $\$ 36,430,000$ (Step 17). This risk calculation can benefit risk-based decision making or risk-reducing strategies to be conducted or implemented.
As the BN is able to take new information into account to update the prior probabilities, the posterior probability of the events and also the most probable configuration of events leading to the evidence can be calculated (Khakzad et al., 2013). The probability updating can be conducted given that EX2 has been in safe condition in accordance with CSB report. The posteriors are summarized in Table 8.

Table 8. Domino effect posterior probabilities given that EX2 has been in safe state.


Considering the most probable configuration, it can be seen that the domino effect has proceeded to the first level without passing through the second level, resulting in no escalation of NC.

# 4.4.5. Sensitivity analysis 

To ensure the BN model demonstrates acceptable behavior, a sensitivity analysis is conducted. The sensitivity analysis systematically investigates the influence of variation in the model inputs on the

model's outputs, where inputs can be the BN parameters (i.e., conditional probabilities) or evidence (i.e. information about the states of nodes) (Bednarski et al., 2004). Using sensitivity analysis, it is possible to determine whether a variable is sensitive or insensitive to the changes in other variables in particular contexts.

In this paper, the GeNIe software ${ }^{1}$ which supports one-dimensional sensitivity analysis is utilized. The results are presented as bar charts in Figure 10 which show the most sensitive nodes for NA, L1, and L2 in the happening and accident states in the absence of evidence. The red/green bars show the positive derivative values and the green/red bars represent the negative derivatives. NA is most sensitive to WT, followed by AW. L1 and L2 are most sensitive to FM, followed by IW. As can be seen, after making a small change (i.e. $10 \%$ of current value), the posterior output changes are not significant, therefore the network structure and the prior probability values seem fine. When the evidence of WT=freezing and later $\mathrm{PF}=$ damaged and the safety barrier failures are entered into the network, the sensitivity measures and the ranking of variables are changed. However, the posterior probabilities show normal behavior.
![img-9.jpeg](img-9.jpeg)

[^0]
[^0]:    ${ }^{1}$ www.bayesfusion.com

![img-10.jpeg](img-10.jpeg)

Fig 10. Sensitivity analysis results for NA, L1, and L2 (Parameter spread=10\% of current value).

# 5. Conclusions 

Natural hazards (such as extreme weather conditions) in conjunction with seemingly insignificant equipment malfunctions (such as failure-to-close of a gate valve) can result in catastrophic naturaltechnological (Natech) accidents. It is further possible that the consequences of such Natech accidents in chemical plants become much more severe due to the escalation of accidents exacerbated by failure or unavailability of safety barriers resulting domino effects. This paper develops a new methodology to assess the risk of Natechs considering their possible domino effects. The proposed methodology is relied upon Bayesian network capabilities to graphically represent the Natech domino effect modelling and to capture the uncertainties involved.

The methodology is applied to investigate the accident at Valero refinery in 2007 in Texas, USA that was triggered by severe weather. The accident initiated in a de-asphalting unit in which the freezing of undesirably accumulated water in a control station's dead-leg caused the piping to crack, releasing pressurized liquid propane and leading to massive fire. The accident could have resulted in much more severe consequences due to the possibility of initiating a catastrophic domino effect; a naphtha column, three chlorine containers, and four enormous butane storage spheres were seriously exposed to the primary fire. The modelling of Valero refinery major accident and near misses points out the need for consideration of quantitative risk analysis of Natech domino effects in chemical plants.
