# A Diagnostic Bayesian Network Method To Diagnose Building Energy Performance 

Arie Taal ${ }^{1}$, Laure Itard ${ }^{2}$, Wim Zeiler ${ }^{3}$<br>${ }^{1}$ The Hague University of Applied Sciences, Delft, The Netherlands<br>${ }^{2}$ Delft University of Technology, Delft, The Netherlands<br>${ }^{3}$ Technical University of Eindhoven, Eindhoven, The Netherlands


#### Abstract

In this paper the implementation of a diagnostic Bayesian network (DBN) method is presented which helps to overcome the problem that automated energy performance diagnosis in building energy management systems (BEMS) are seldom applied in practice despite many proposed methods in studies about this subject. Based on the 4S3F framework, which contains 4 types of symptoms and 3 types of faults, an energy performance diagnosis model can be built in a DBN tool to simulate the probabilities of faults based on the presence and absence symptoms which are related to conservation laws, energy performance and operational state of the heating, ventilation and air condition (HVAC) systems. Symptoms of all kinds of detection methods, based on models and rules or data-driven, can also be implemented. The structure of the building energy performance DBN models consists of symptom and fault nodes which are linked to each other by arcs. At diagnosis the probabilities of faults can be estimated by the presence of symptoms. This paper demonstrates how these DBN models can be setup using schematics for HVAC systems.


## Introduction

Despite many studies related to energy performance, see for instance Djuric (2009), building energy performance diagnosis is not common use in practice. Recent research (Jing, 2017) demonstrated that energy performance of buildings is still lower than expected which shows the need for energy diagnosis.
We find there are two main reasons why automated energy performance diagnosis is missing in practice. One reason why these systems are not applied in practice is that identification of faults which lead to high energy consumption is often difficult because connecting symptoms and faults to each other is not a straightforward exercise. Detected symptoms can be caused by a variety of faults or a combination of faults. And a specific fault in turn, can lead to a variety of symptoms. In addition to this, errors in diagnosis systems can occur because of uncertainties in the applied methods or in the measured energy data. These can be errors of type I, finding a nonexistent fault or type II, missing an existent fault. See for instance Tran (2016) who describes these types of errors in more detail for fault detection in centrifugal chiller systems.

The second reason for which implementation of diagnosis methods is complicated is that most methods are designed for a certain heating, ventilation or air-conditioning (HVAC) system, like specific types of air handling units, chillers and variable air volume systems. This leads to time-consuming implementation in practice because many different methods have to be combined. In addition, it is difficult for HVAC engineers to set up energy performance diagnosis systems .
Zhao (2017) and Verbert (2017) presented recently diagnostic Bayesian networks (DBN) for HVAC diagnosis. In this paper a DBN method is presented which will overcome the problems named here above. The proposed DBN method is an expert system which diagnoses as an HVAC expert does and demands little IT (information technology) knowledge to set up diagnosis models. In addition the DBN models for energy performance fault diagnosis are congruent to HVAC schematics.
First we address the 4S3F framework on which the energy performance diagnosis is based. Then we present the 4 types of symptoms in the 4S3F framework, followed by an explanation of diagnosis by DBNs. Next, we present the structure of the DBN models in the 4S3F framework and we show the application of the method on a thermal energy plant. Finally, we will present conclusions and recommendations for further research.

## The 4S3F framework for energy performance diagnosis

In this paper, we focus on the detection and diagnosis of faults in the energy performance of buildings. This section presents the headlines of the 4S3F architecture -- see Taal (2018) in which this architecture is explained in more detail--implemented in this article. Figure 1 presents the detection and diagnosis processes in the 4S3F framework. Measurements from the HVAC system, which can be stored in a database of the building management system (BMS), is used to detect symptoms that a fault can be present.
The presence of faults is determined by analysing 4 different types of symptoms which are shown in Figure 1: Balance symptoms (energy, mass and pressure), energy performance (EP) symptoms, operational state (OS) symptoms and additional symptoms (based on additional information as maintenance information).

![img-0.jpeg](img-0.jpeg)

Figure 1: Architecture for automated energy performance diagnosis.
The results of the detection phase are entered in a DBN model. In this model symptoms are linked to possible faults. We distinguish 3 types of faults: faults of models used for missing energy data and for balances, component faults and faults of control of components. Figure 2 shows the relationships between the 4 types of symptoms and the 3 types of faults which are implemented in DBN models. For instance, a control fault can lead to EP, OS or Additional symptoms.
![img-1.jpeg](img-1.jpeg)

Figure 2: 4S3F structure.

## Detection of symptoms

## Balance symptoms

Physical balance symptoms can be applied to estimate faults in sensors and models for missing energy states by virtual sensors. The balances are based on conservation laws, like energy and mass balances. They have to be true otherwise a sensor (which is a component) fault could be present.

## EP symptoms

The energy performance of HVAC (sub)systems can be estimated by energy performance indicators like coefficients of performances (COPs) and efficiencies. This symptoms indicate for instance a control fault.

## OS symptoms

Next to EP symptoms OS symptoms depict faults. As shown in the project BuildingEQ (2018) OS symptoms can be visualized by energy signatures, like time series plots, scatter plots and carpet plots. Figure 3 presents an example in which the relationship between the supply water temperature of the heat pump and the outdoor temperature is shown in a scatter plot. Green lines depict upper and under control values. Symptom are present when measured values deviates from this bandwidth.
![img-2.jpeg](img-2.jpeg)

Figure 3: Supply hot water temperature versus outdoor temperature.

## Additional symptoms

Additional symptoms could be obtained from maintenance or inspection of the HVAC system to exclude faults. See Zhao (2017) who included this type of symptoms for air handling units (AHU) fault detection and diagnosis (FDD). In addition results from other FDD methods, for instance data-driven methods based on regression formulas, principal component analysis (PCA), support vector machine (SVM), artificial neural networks (ANN) or other pattern recognition methods, can be added. See Kim (2017) who recently presented an overview of FDD methods for HVAC systems. To the authors view component specific FDD methods for HVAC products could be delivered by component suppliers, for instance for heat pumps, boilers and pumps and included in the overall architecture

## Diagnosis by DBNs

Almost all FDD methods are specific for one type of component or system. Some methods support a top-down or a bottom-up approach to estimate sequentially faults in aggregated or sub systems. However, not simultaneously. Diagnosis by DBN overcomes this problem because the faults in sub and aggregated systems are estimated simultaneously. Another advantage of the DBN method is that the outcomes are probabilities and not Booleans which is more realistic because of uncertainties by inaccuracies of measurements and assumptions in the detection models and in the parameters of the DBN model. Especially when few detection results and contrary symptoms are present, a probability outcome is more realistic. In addition the DBN works how experts diagnose. Based on experience they estimate the fault probabilities and they first address the faults with the highest probability. In this paper we show that DBN models are congruent to models in HVAC schematics which simplifies the setup of a DBN model, and makes possible to design it at the same time the HVAC schematics is developed.

## DBN method

In the DBN method Bayesian statistics is applied which is based on relations between state probabilities of events. When the probability that event B is true $(\mathrm{P}(\mathrm{B})>0)$, the

![img-3.jpeg](img-3.jpeg)

conditional probability P(A|B) that event A occurs while B is true, can be estimated using the DBN model.

The DBN model can be represented in a graphical model in which the relations between variables are displayed. This graphical model consists of nodes, which represents the variables, and arrows, which display the relations between the nodes. Every node contains a probability table in which the state probabilities are represented depending on the connected parent nodes.

### **DBN Example**

Figure 4 shows a black box model for the COP of a heat pump. Wcompr is the electricity consumption of the compressor of the heat pump, Qcond is the supplied heat by the condenser of the heat pump and Qevap is the heat at the evaporator of the heat pump during the diagnosis time period.

![img-4.jpeg](img-4.jpeg)

*Figure 4: Black box model heat pump.*

The COP of a heat pump can be calculated from Eq. (1).

$$COP = \frac{Q_{cond}}{W_{compr}} \tag{1}$$

The reliability of the calculated COP depends on the reliabilities of the energy values Qcond and Wcompr.

As a simplification we assume in this example that COP is only true (reliable) when Qcond and Wcompr are both true. So we neglect the small possibility that COP can be true while Qcond and Wcompr are false and the faults compensate each other.

In a thought experiment the probability that Qcond (P(Qcond)) is correct, has an arbitrary value of 90 % which can be based on historical values of flow rate and temperature sensors from the BMS. The probability P(Wcompr) is set to 95 % because Wcompr is directly measured. In this case we can easily calculate the probability that COP is true (P(COP) because Wcompr and Qcond are statically independent of each other:

$$P(COP) = P(Qcond \land Wcompr) = P(Qcond) \cdot P(Wcompr) = 0.95 \times 0.9 = 0.855 = 85.5\%$$

A graphical representation of the corresponding DBN model is shown in Figure 5.

![img-5.jpeg](img-5.jpeg)

*Figure 5: DBN model for the COP of a heat pump.*

The nodes Qcond and Wcompr have prior probabilities and node COP has conditional probabilities. Table 1 shows the conditional probability table for COP and shows our assumption that COP is true when both Qcond and Wcompr are true. This table is implemented in Genie (2016), a DBN software tool.

The set prior probabilities of the fault nodes are shown between brackets.

*Table 1: The conditional probability table for COP.*

(0.05) | True
(0.95) | False
(0.05) | True
(0.95)  |

Conversely, it is also possible to use Table 1 to determine P(B|A) when state A is known, which is wanted for fault diagnosis. When the value of COP is false, so P(COP) = 0 (in reality this would be the result of the detection of a symptom, in this case an incorrect COP), then the probability from the DBN model is 69% that this happens because Qcond is false. The probability that this happens while Wcompr is false is 34.5 %. See Taal (2016) where this calculation is explained. In other words, it is more likely that the fault arises because of an incorrect value of Qcond than because of an incorrect value of Wcompr. This is logical because in our example the reliability of Qcond (90%) is lower than that of Wcompr (95%).

### **Structure of the DBN models in the 4S3F framework**

In DBNs fault nodes (purple in Figure 2) are linked to symptom nodes (yellow in Figure 2) by arcs. The direction of the arcs is from the fault nodes to the symptom nodes as shown in Figure 2.

Connection nodes can be present between the fault and symptom nodes. See Figure 6 wherein an example of a DBN model for an energy balance for a heat pump is given in which fault and symptom nodes are linked by calculation nodes. Q1 is the condenser heat and Q2 is the evaporator heat which are calculated from temperature and flow rate sensor values. W is the compressor work available for compression of the refrigerant in the heat pump.

![img-6.jpeg](img-6.jpeg)

*Figure 6: DBN model with calculation nodes.*

### **Node types**

As can be seen in Figure 6, fault nodes are parent nodes which have prior probabilities which are independent of the state of other nodes. For instance, in the DBN example we see that the prior true probability of Wcompr is 95 % while the prior false probability is 5 %. Symptom nodes are child nodes with conditional probabilities which means that the state depends on the parent nodes. See Table 1 which shows the probabilities of the true and false COP state depending on the states of Qcond and Wcompr.

In Figure 6 a calculation layer is introduced which increases the readability of DBN models by separating faults in components from faults in models. In addition less arcs to symptom nodes are needed. In the calculation layer enthalpy nodes (H) and heat nodes (Q) are encountered.
We propose to implement the DBN in a graphical oriented software tool like Genie (2016). In Genie the type of the child nodes can be selected. The standard type has the structure as presented in Table 1. Table 1 contains only Boolean probabilities for the symptom node COP. However in reality COP could be true while Qcond or Wcompr is false by faulty measurements. Most of the time it is impossible or time consuming to define the fault probabilities of all combinations. We propose to apply socalled Noisy-Max nodes in which the false parent state indicates the chances of the child states. Table 2 presents this for our DBN example. We see that COP can be $2 \%$ true when Qcond or Wcompr is false. LEAK shows here the chance of the COP states when Qcond and Wcompr are both true. Adjustment of the DBN example with the Noisy-Max node presented in Table 2 leads to $1 \%$ and $2 \%$ false values for Wcompr and Qcond when COP is true, while the false values ( 34.5 and $69 \%$ ) remain the same when COP is wrong.

Table 2: Noisy-Max type for node COP in the DBN example.


We propose to apply Noisy-Max nodes for all child nodes. The fault nodes have as first state the false state because it is difficult to estimate the probabilities of the child node when one of the parent nodes is true independent of the state of the other parent nodes. In this way the Noisy-Max probabilities can be set up easily because the true state of LEAK can be set to 1.
For the sake of demonstration, only false and true states are proposed for parent and child nodes in this paper. However it can be extended with more states when necessary.
A sensitivity analysis, which is not presented here, showed that relative values are more important than absolute values for the prior and conditional probabilities. We saw that the diagnosis outcomes were relatively the same, meaning isolation of faults remained the same, when prior or conditional fault probabilities were changed with $100-300 \%$, for instance from 2 to $5 \%$. In the DBN example the false probability of Qcond was set higher than Wcompr because one knows that Qcond is more inaccurate by calculation from several sensors. Detailed historical data on probabilities of the states is therefore not necessary, thus no training data, but expertise about the relative frequency of errors occurring which is known by design and maintenance HVAC engineers. Also component knowledge can be taken into account.

## HVAC mode nodes

An extensive HVAC installation contains many components. When a component is not active, its false probability should be ignored during the diagnosis time period to avoid it being incorrectly marked as false. Therefore a mode node is present which is a kind of OS node. The mode node is set to true when a subsystem is not active. Table 3 shows an example in which the flow rate FT1 and the temperatures TT1 and TT2 are set to true when the mode node is true.

Table 3: Example noisy-max type for a mode node.


## Subsystems

The proposed 4S3F architecture consists of systems and sub-systems with similar characteristics. Each system contains one or more of the four generic types of symptoms (balance, EP, OS and additional symptoms), as well as one or more of the three types of faults (component, control and model faults).
An example of a possible hierarchical level structure for the systems, is presented in Figure 7 in which HVAC controls are not depicted. At least five levels can be distinguished. For all levels DBN models can be set up based on the three types of faults and the four types of symptoms.
![img-7.jpeg](img-7.jpeg)

Figure 7: Example of homologous multi-level systems.
The HVAC system (the first level) can be divided into generation systems, distribution systems and end-user systems (the second level), which contain aggregated subsystems, for instance heat-pump and boiler systems (the third level) which are part of a heat generation system. These systems contain trade products (e.g. the heat pump), as well as combined systems, including the evaporator and condenser modules (the fourth level). The systems in the fourth level can consist of components including pumps, valves and heat exchangers (the fifth level). All levels can contain control systems, which are not shown here. For example, a heat pump has its own control system (for safety purposes), and it can contain an embedded control for supply temperature, which in turn involves the evaporator and condenser modules. Higherlevel controls can also be connected by lower-level sensors and actuators. For example, the heat pump can be

![img-8.jpeg](img-8.jpeg)

![img-9.jpeg](img-9.jpeg)

*Figure 8: Example of an HVAC DBN model on level 1 and 2.*

Genie has the capability to build subsystems from the DBN models. Figure 8 shows a DBN model on level 1 and 2. Three heat balance symptoms on level 1 are present in this model. Furthermore three generation submodels (an aquifer thermal energy storage (ATES) system, a heat pump system and a boiler system) are presented, two hydronic systems (cold and hot water) and three end-user systems (cold water groups, hot water groups and roof collector).

The hydronic systems connect generator and end-user systems together by exchanged energy.

![img-10.jpeg](img-10.jpeg)

*Figure 9: Schematic of heat pump system (from Taal, 2018).*

An example of a DBN model on level 3, a heat pump system which schematic is shown in Figure 9, is presented in Figure 10. DBN models on levels 4 (heat pump, condenser and evaporator module) and 5 (pumps, pipes, valves, condenser, evaporator) are not presented. To the authors view these levels could be implemented by product suppliers who could apply FDD methods to diagnose faults within their products.

![img-11.jpeg](img-11.jpeg)

*Figure 10: Example of a heat pump system DBN model at level 3.*

### **Application of the 4S3F method on a thermal energy plant**

The 4S3F method was tested on the building of The Hague University of Applied Sciences (THUAS) in Delft. In Figure 11 a simplified block schematic of the generator (heat pump, boiler and ATES), hydronic (hot and cold water) and end-user (hot and cold water) systems in the thermal energy plant is presented. See for instance the P&ID (piping & instrumentation diagram) in Figure 9 how these systems are composed.

*Figure 11: Simplified Block schematic of the thermal energy plant of the THUAS building.*

The heat pump system delivers heat when the hot water system in the THUAS building demands heat. The boiler system supplies additional heat when the heat pump has reached its nominal capacity. The heat pump extracts its heat from the warm well of an ATES system by a heat exchanger. Cold is supplied by the cold well of the ATES system. When the ATES system cannot supply enough cold, the heat pump, which functions then as cooling machine, can deliver cold.

Figure 11 shows the calculated annual exchanged energy between main systems in 2013. This annual energy amounts at level 3 are calculated by 16 minutes data which was stored by the BMS in a database.

#### **EP symptoms**

For EP symptoms, performance factors are applied which do not take into account (thermal) energy which is freely available from the environment. As indicators Seasonal Performance Factors (SPFs) are used, like the Seasonal Coefficient Of Performance (SCOP) for heating and the Seasonal Energy Efficiency Ratio (SEER) for cooling for year 2013. Eqs. (2) to (6) show the SPF's which are analyzed in the case study. See Figure 11 in which the annual exchanged energy amounts are depicted.

$$
\text{SCOPhw} = \frac{\text{GPW}}{\text{Whp, heating + Wpump, heating + WATES + Ggas}} \tag{2}
$$

$$
\begin{gathered}
S E E R c w=\frac{\eta c o w}{W h p, \text { cooling }+W p u m p, \text { cooling }+W p u m p, A T E S} \\
S C O P r e g=\frac{\eta r e g}{W p u m p, r o o f+W p u m p s, r e g+W p u m p s, A T E S} \\
S C O P h p=\frac{\text { gcond, mod }}{W h p} \\
S E E R h p=\frac{\text { group, mod }}{W h p}
\end{gathered}
$$

Whp is equal to Whp,heating when the heat pump is in heating mode and to Whp,cooling when it is in cooling mode. When the heat pump is simultaneously generating cold and heat for the cold water and the hot water systems A and E (see Figure 11), the electricity is divided proportionally based on the supplied thermal energy to systems A and E. SCOPreg can be considered as a generic energy performance factor for ATES systems. These measured performance factors are compared with expected ones from guidelines. In this paper, we assume that symptoms are present when the measured SCOP or SEER is $5 \%$ lower than the expected one which is reasonable considering the inaccuracies in calculated energy amount (sensor inaccuracies, ignored transient behaviour, 16 minutes calculation interval, energy model assumptions). In this case study most of the measured performance factors were true. For instance the SCOPhp of the heat pump was 4.5 compared to 4 , the SCOPhw for heating the hot water system was 3 compared to 3 and the SEERcw for cooling the cold water system was 60 compared to 40 . Also the SCOPreg of the regeneration of heat for the ATES system 22.3 was higher than the expected value of 20 .
In addition to SPFs also efficiencies are taken into account. An important performance indicator for the ATES system is $\eta$ reg, see Eq. (7), which denotes the thermal energy balance in the ATES system. Dutch regulations demands that thermal equilibration is present undergrounds which means that the extraction of cold and heat are the same during a year.

$$
\eta r e g=1-\frac{\text { obs }(\text { (heatwell }-(\text { coldwell })}{\text { max }(\text { (heatwell, (coildwell })}
$$

This heat regeneration efficiency was only $63 \%$ which means that $37 \%$ too less heat was regenerated. Thus a symptom for $\eta$ reg was found.

## OS symptoms

In the case study supply and return temperatures to the systems at level 3 were analysed. This led to 3 symptoms: the ingoing and outgoing warm well temperatures were lower than expected and the cold water return temperatures were too high.
All energy amounts and the EP and OS symptoms are estimated in the software tool Matlab, using the BMS data. The actual EP and OS values are compared to reference values based on guidelines and design information. Generally, also results from benchmarks and models (see Verhelst, 2017 for such models) can be used.

## Diagnosis

Based on the schematic of Figure 11 DBN models are built in Genie like in Figure 8. In the generator systems their own SCOP symptoms are present, see Figure 10. The detection results are entered in Genie. Diagnosis showed successfully that two faults with high fault probability
were present. The first one is that the control of the regeneration was faulty with fault probability $100 \%$, the second one that the control of the ATES system was faulty (98\%).
Based on the schematic of Figure 11 DBN models are built in Genie like in Figure 8. In the generator systems their own SCOP symptoms are present, see Figure 10. The detection results are entered in Genie. Diagnosis showed successfully that two faults with high fault probability were present. The first one is that the control of the regeneration was faulty with fault probability $100 \%$, the second one that the control of the ATES system was faulty $(98 \%)$.

## Conclusions and recommendations

In this paper the implementation of a diagnostic Bayesian network (DBN) method is presented which helps to overcome the problem that automated energy performance diagnosis in building energy management systems (BEMS) are seldom applied in practice despite many proposed methods in studies about this subject. This method is based on the 4S3F framework, which contains 4 types of symptoms and 3 types of faults. In the proposed DBNs faults are parent nodes and symptoms are child nodes from Noisy-Max type.
The proposed DBN structure contains sub-models on several levels in the same way engineers design HVAC and control systems:

1. HVAC systems
2. Generator, Hydronic and end-user systems
3. Component systems, like a heat pump system
4. Main components, like heat pumps
5. Subcomponents of main components

Models can be set up for HVAC components and systems as designed by HVAC engineers and implemented by control engineers based on HVAC schematics. Caused by this system approach it is possible to set up once a library of DBN models which can be extended with models for new components and systems.
In addition, the DBN can be set up by HVAC experts without IT expertise relating to FDD methods.
A disadvantage of the proposed DBN method could be that the exact error is not estimated, for example a heat exchanger has too low capacity due to a too small heat exchange surface or due to contamination. It is only found that a fault is present in the heat exchanger. However, this concerns faults at level 4 or 5 for which specific FDD methods are available and could be combined in the 4S3F architecture.
In this paper an application on a real HVAC system was presented using historical 16 minutes data all over the year 2013. The same method can be applied on real-time BNS data.

## Recommendations

DBN applied in the 4S3F framework has as the advantage that detection of symptoms and diagnosis by DBN can be automated. The case study for the thermal energy plant of the THUAS building showed its value. We recommend to

set up a library of generic DBN (sub)models on levels 1 to 3 .
Further research is needed to define the input and output of the DBN models at several levels. For instance, at what level sensor and symptom nodes should be present.
In addition, a software shell is needed which

- process automatically BMS data into symptoms
- implement models from the DBN library in a DBN software tool such as Genie.
- has an user-interface for the estimated fault probabilities.
Furthermore, research is needed for diagnosis at several time periods: monthly, daily and hourly scale with real life BMS data instead of historical data with annual diagnosis. And dynamic setpoint values for symptom detection could also be derived from physical (simulation) models instead from guidelines as used in this paper.
Finally, we propose to extend BEMSs with this 4S3F method. The energy data can be derived from BMSs. The BEMS can be setup simultaneously with the implementation of the control of the HVAC in the BMS because HVAC schematics are applied in both cases.

