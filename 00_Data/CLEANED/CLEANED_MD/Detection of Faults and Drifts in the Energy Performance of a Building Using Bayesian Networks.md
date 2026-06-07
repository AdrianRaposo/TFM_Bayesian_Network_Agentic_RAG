# HIAL open science 

## Detection of Faults and Drifts in the Energy Performance of a Building Using Bayesian Networks

David Bigaud, Abdérafi Charki, Antoine Caucheteux, Fally Titikpina, Téodor<br>Tiplica

## To cite this version:

David Bigaud, Abdérafi Charki, Antoine Caucheteux, Fally Titikpina, Téodor Tiplica. Detection of Faults and Drifts in the Energy Performance of a Building Using Bayesian Networks. Journal of Dynamic Systems, Measurement, and Control, 2019, 141 (10), pp.101011. 10.1115/1.4043922 . hal-02556347

## HAL Id: hal-02556347 <br> https://univ-angers.hal.science/hal-02556347v1

Submitted on 8 Nov 2022

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

David Bigaud
LARIS (Laboratoire Angevin de Recherche en Ingénierie des Systèmes), University of Angers, 62 Avenue Notre Dame du Lac, Angers 49000, France
e-mail: david.bigaud@univ-angers.fr

## Abderafi Charki ${ }^{1}$

LARIS (Laboratoire Angevin de Recherche en Ingénierie des Systèmes), University of Angers, 62 Avenue Notre Dame du Lac, Angers 49000, France
e-mail: abderafi.charki@univ-angers.fr

## Antoine Caucheteux

CEREMA (Centre d'Etudes et d'expertise sur les Risques, l'Environnement, la Mobilité et l'Aménagement), 23 Avenue de l'Artrite Chauvin BP 20069, Les Ponts-de-Cé 49136, France
e-mail: antoine.Caucheteux@cerema.fr

## Fally Titikpina

LARIS (Laboratoire Angevin de Recherche en Ingénierie des Systèmes), University of Angers, 62 Avenue Notre Dame du Lac, Angers 49000, France
e-mail: tally.titikpina@univ-angers.fr

## Teodor Tiplica

LARIS (Laboratoire Angevin de Recherche en Ingénierie des Systèmes), University of Angers, 62 avenue Notre Dame du Lac, Angers 49000, France
e-mail: teodor.tiplica@univ-angers.fr

## Detection of Faults and Drifts in the Energy Performance of a Building Using Bayesian Networks

Despite improved commissioning practices, malfunctions or degradation of building systems still contribute to increase up to $20 \%$ the energy consumption. During operation and maintenance stage, project and building technical managers need appropriate methods for the detection and diagnosis of faults and drifts of energy performances in order to establish effective preventive maintenance strategies. This paper proposes a hybrid and multilevel fault detections and diagnosis (FDD) tool dedicated to the identification and prioritization of corrective maintenance actions helping to ensure the energy performance of buildings. For this purpose, we use dynamic Bayesian networks (DBN) to monitor the energy consumption and detect malfunctions of building equipment and systems by considering both measured occupancy and the weather conditions (number of persons on site, temperature, relative humidity (RH), etc.). The hybrid FDD approach developed makes possible the use of both measured and simulated data. The training of the Bayesian network for functional operating mode relies on on-site measurements. As far as dysfunctional operating modes are concerned, they rely mainly on knowledge extracted from dynamic thermal analysis simulating various operational faults and drifts. The methodology is applied to a real building and demonstrates the way in which the prioritization of most probable causes can be set for a fault affecting energy performance. The results have been obtained for a variety of simulated situations with faults deliberately injected, such as increase in heating preset temperature and deterioration of the transmission coefficient of the building's glazing. The limitations of the methodology are discussed and are translated in terms of the ability to optimize the experiment design, control period, or threshold adjustment on the control charts used. [DOI: 10.1115/1.4043922]

Keywords: energy performance, fault detection and diagnosis, Bayesian network, weather conditions, occupancy

## 1 Introduction

According to different sources, it is commonly considered that buildings are responsible for about $30-40 \%$ of the energy consumption in Western countries. Many studies have demonstrated that, in the operational and maintenance (O\&M) stage, buildings actually use more energy than estimated by energy simulations in the design stage [1]. In Ref. [2], a difference of performance of more than $30 \%$ has been estimated. This difference is due to uncertainty in the modeling of energy simulations [3], as well as to differences in occupant behavior and in building use over time (e.g., modifying room functions and building occupancy). Malfunctions/degradation and a bad control of systems also contribute to reduction in comfort and increase in energy consumption (in some cases, $10-20 \%$ higher than necessary) [4]. Recently, in Ref. [5], it has been demonstrated that the averaged cooling energy in office buildings was about $16 \%$ higher than designed due to operational errors. Even if the efforts are made to improve the continuous commissioning [6], energy consumption is still higher than

[^0]expected and, therefore, the development of effective preventive maintenance strategies for building systems is very important. Thus, condition-based maintenance plans the maintenance according to the need determined by the system conditions [7]. Nevertheless, despite examples of preventive maintenance for heating, ventilation, air conditioning, and refrigeration [8], automated energy performance diagnosis features are currently scarcely applied in building energy management systems practices. A keystep within the condition-based maintenance process is the ability to monitor the system malfunctioning from the available signals, hereafter referred to as fault detections and diagnosis (FDD). The automated FDD tools are useful to alarm and identify faults promptly and to identify the variables that cause the degradation of performances, with due regard to the level of accepted risk.

Over the last decades, a significant number of researches had been carried out in the developments of FDD methods for building's systems (see, e.g., Ref. [9] for air handling units, [10] for chiller and [11] for HVAC systems). Building energy HVAC FDD has been proved efficient to reduce energy consumption in buildings during O\&M stages. Some field observations show that energy savings of $5-30 \%$ can be achievable by correcting faults diagnosed in buildings [12]. Recent FDD case studies in Australia [13] show that energy savings between $15 \%$ and $28 \%$ are possible by implementing HVAC FDD systems. Despite all these benefits,


[^0]:    ${ }^{1}$ Corresponding author.
    Contributed by the Dynamic Systems Division of ASME for publication in the Journal of Dynamic Systems, Measurement, and Control. Manuscript received February 3, 2018; final manuscript received May 27, 2019; published online xx xx, xxx. Assoc. Editor: Umesh Vaidya.

81 FDD tools are still not broadly used in practice due to the timeconsuming nature of the tasks (which must be repeated for each building) and to the complexities of FDD algorithms.
According to Ref. [14], FDD methods can be categorized into three types of approaches: quantitative or model-based, qualitative or rule-based, and process-history-based or data-driven.
Quantitative or model-based approaches are usually based on the knowledge of the physical laws describing the system (e.g., heat and mass balances). The common method in the quantitative FDD approach is the residual generation and analysis (difference between measured and simulated values). Model-based approaches do not rely on past data for training; therefore, they are considered efficient for the detection of unknown abnormalities. They can be used at the component as well as the whole building levels.
Qualitative approaches require a prior knowledge of the system from which simplified relationships (e.g., the rule-based method) are developed. This kind of method is rather simple, but it is also specific to the system under study and often requires a "customized" implementation, which mainly relies on experts and developers' knowledge [15].
Process-history-based or data-driven methodologies are also relatively easy to implement, but they require a significant amount of data to be efficient. Since they rely on historical data, one has to study a whole range of various system operations. In addition, they generally cannot be directly applied on another system without taking into account the specificities of the system [16,17]. Process-history-based approaches include methods such as artificial neural network (e.g., Ref. [18]), principal component analysis [19], support vector machine (e.g., Refs. [20] and [21]), Bayesian classifiers (e.g., Ref. [22]), Fisher discriminant analysis (e.g., Ref. [23]), etc.
In Ref. [24], the authors propose to consider a fourth category of approaches: hybrid approaches obtained by connecting several of the aforementioned approaches in order to improve the overall FDD accuracy and robustness. For example, model-based FDD approaches are often connected to data-driven methods. The present research proposes a hybrid approach (data-driven + modelbased). Our purpose is to train the FDD tool based on a large data collection and completing knowledge through dynamic energy simulations (DES) in order to study the effect of complementary unobserved/dysfunctional operations.
Bayesian networks (BNs) can be considered as an appropriate method to accurately represent a building, which is considered as a complex system with uncertain, incomplete, and conflicting information. They are deemed a powerful tool to develop expert systems, and they have the potential to detect and diagnose faults or drifts. A BN is a probabilistic graphical model that represents relationships of probabilistic dependence within variables by means of directed acyclic graphs (see Sec. 2). BNs used as a FDD tool offer a number of undeniable advantages: the ability to manipulate continuous and discrete variables, the ability to take into account time through dynamic Bayesian networks (DBNs), object modeling via the formalism of object-oriented Bayesian networks, and the possibility to expand into decision optimization techniques through the use of influence diagrams (extension of Bayesian networks) [25]. Beyond being able to identify the causes of drift or dysfunction, one remarkable aspect of the BNs, that we cannot find in other methods (such as artificial neural network or support vector machine), is the ability to sort them from the most to the least probable and hence to prioritize inspection and maintenance actions. In the frame of research for increasing the energy performances of buildings, BNs have proved their interest and rel-

## 2 Creation of a Bayesian Network to Monitor the Performance of a Building

2.1 Principle and Properties of Bayesian Networks. A BN is a statistical modeling tool whose formalism makes it possible to deal with uncertainties. The most useful application of BN is to assess hierarchically the possible causes of risks, failures or operational drifts [31]. Today, BN can be considered as a key modeling framework in decision making in a wide variety of domains such as social sciences [32,33], robotics [34,35], biochemistry or biology [36,37], medicine [38,39], engineering [40,41] and, of course, energy.

In order to understand fully the properties of BNs, it must first be clear that they are a hybrid of two different fields: the theory of graphs and the theory of probabilities. In short, a BN is a graphical representation of a probabilistic model revealing the different relationships that the variables of a model can have. It expresses and factorizes the joint probability of $m$ variables in $m$ conditional independences and its structure enables local calculations of prob- ability using all the information about the joint distributions, These conditional independences make it possible to reduce the number of calculations necessary for the inference and learning of a probabilistic model by simply reducing the size of its structure. For example, a joint probability of $m$ variables is written using the chain rule (or "general product" rule) as follows:

$$
p\left(x_{1}, x_{2}, \ldots, x_{m}\right)=p\left(x_{m} \mid x_{m-1}, \ldots, x_{1}\right) \ldots p\left(x_{2} \mid x_{1}\right) p\left(x_{1}\right)
$$

This equation can be shortened by introducing or defining the conditional independences between its variables. Moreover, by illustrating these independences in the form of a BN, it becomes possible simply to increase the number of conditional probability distributions for each variable in accordance with the parents and rewrite the joint distribution as follows, where $p a\left(x_{i}\right)$ refers to the parents of $x_{i}$ :

$$
p\left(x_{1}, x_{2}, \ldots, x_{m}\right)=\prod_{i=1}^{i=m} p\left(x_{i} \mid p a\left(x_{i}\right)\right)
$$

Nevertheless, the fact that the conditional distribution for each variable is defined according to its parents does not signify that no other variables influence it. In other words, nodes other than its parents in the BN can influence a node. These nodes are consistent with the Markov condition, which states that a variable is isolated by a subset of variables of the overall set $V$ known as the Markov blanket [42]. A variable is therefore conditionally independent of

![img-0.jpeg](img-0.jpeg)

Fig. 1 The Markov Blanket. The shaded nodes (parents, coparents, children nodes) are inside the Markov Blanket of node "A." The white ones are outside the blanket.

213 other variables outside its blanket if the nodes of the blanket are observed. This includes its parent and child nodes and the coparents of its children (see Fig. 1). These nodes, if observed, "block" the node in question from other nodes outside its periphery (see Sec. 4.2 and the discussion related to Fig. 6 for an illustration).

In the example illustrated in Fig. 1, Eq. (2) is developed as

$$
\begin{aligned}
p(V)= & p\left(C h_{1}, C h_{2}, C P_{1}, C P_{2}, P_{0}, P_{1}, P_{2}\right) \\
= & p\left(P_{0} \mid P_{1}, P_{2}\right) \cdot p\left(C h_{1} \mid C P_{1}, P_{0}\right) \cdot p\left(C h_{2} \mid C P_{2}, P_{0}\right) \cdot p\left(P_{1}\right) \\
& \cdot p\left(P_{2}\right) \cdot p\left(C P_{1}\right) \cdot p\left(C P_{2}\right)
\end{aligned}
$$

220 This property of the BN is not only useful but also essential for inference calculation, and makes it possible to determine instantaneously and visually whether a set of variables is conditionally independent of another one.
The most recent developments in BNs have essentially focused on the inference algorithms [43-45] and on the learning of the structure and parameters of the network [46]. We will concentrate on these aspects in constructing BNs to describe functional and dysfunctional modes in the energy systems of a test building.
2.2 Construction Stages of a Bayesian Network for the Simulation of a Building. Building management is increasingly relying on automated procedures with sophisticated instrumentation on systems and equipment, allowing the collection of considerable quantities of data. In fact, the volume of data collected is so vast that it would be impossible for an operator to monitor directly each variable involved in the procedure. It seems perfectly logical, therefore, to monitor the technical systems of a building using data-driven methods such as the BN.
The modeling procedure for a building system comprises three stages [47]:

- The first stage consists in collecting a database of measured/ real inputs (climate, envelope, energy systems, occupants), and outputs (energy needs) calculated from actual data and/ or derived from DES. An approach founded entirely on measured inputs and outputs is possible when characterizing an existing building. For a new building, insofar as the energy performance of its equipment and systems cannot be measured on long periods, it is very difficult to characterize the functional and dysfunctional modes. Therefore, the
hybrid approach, of real inputs and simulated outputs, proves 249 to be very effective in the majority of situations.
- The second stage consists in learning from the created database to construct a BN (i.e., to model casual relationships and conditional probability distributions between the variables that will influence the energy performance) enables to mimic the building and its energy systems in their normal operational modes. That is to establish a "baseline," essentially, from which to observe operational drifts. This stage is regarded as the inductive part of the BN's construction in that we use the effects/causes to faults/consequences relationships.

Constructing the BN involves making certain choices. For example, continuous nodes may be preferred to discrete ones, the choice here being a matter of compromise between complexity (and thus calculation time) and precision of the model. Whatever the decision made, the robustness of the learning methods of the BN needs to be tested and the physical representativeness evaluated by appropriate experts.

- The third stage consists in adapting the model to the dysfunctional operating modes based on the consolidated architecture obtained at the previous stage. Here, the detection capacity of the BN is tested. In other words, an analysis of its sensitivity to operational drifts and consequently its ability to detect faults. The dysfunctional operating mode database is created from DES by simulating preset multiple input faults (see Sec. 4.6 for details). The conditional probability matrices logically constitute the main output of this so-called deductive stage, since the inference rules now relate faults/ consequences to effects/causes.

Once the model is consolidated, it will be operated to sort the possible causes of detected energy performance defects into hierarchical order [48].

### 2.3 Modeling of Energy Performance in Functional and

Dysfunctional Modes. The modeling the building's energy performance in its functional and dysfunctional modes (corresponding to the second and third stages mentioned previously) is itself divided into six steps (detailed in Sec. 4). The first step will consist in collecting the problem data. The inputs, i.e., the external and internal loads factors that influence the energy performance, are measured on-site. The outputs (heating needs), however, are simulated via TRNSYS v17/type 56). A calibration sub-step had to be carried out in order to adjust the DES results to measured data from the test building. The second step will concern the choice and use of the accurate algorithm to learn from calibrated input and output data values, which have been first discretized in order to reduce calculation times. The third step tests the robustness of the BN; a process aided by the judgment of experts. The fourth step explores the effectiveness and influence of continuous nodes rather than discrete ones. The fifth step consists in developing a DBN from which we provide updated baselines from calibrated data. The sixth and final step is dedicated to the simulation of dysfunctional modes. We create new databases by means of DES with different faults situations from which the DBNs can be updated.

Figures 2(a)-2(c) give a conceptual representation of a BN modeling functional and dysfunctional modes. Occ_i (i = 1 to 3), Zone_j (j = 1 to 3), Syst_k (k = 1 to 3), Sens_n (n = 1 to 5) represented respectively the occupants, zones (or rooms) of the building, technical systems, and measurement sensors.
2.4 Control Charts for the Detection of Performance 306 Faults and Drifts. The principle behind the proposed modeling is that the fault detection can be viewed as a binary classification task: an observed state belongs to either the normal operation class ("under statistical control (SC)") or the faulty operation class ("dysfunctional" or "out-of-control"). A $T^{2}$ hotelling multivariate control chart $[49,50]$ was used.

![img-1.jpeg](img-1.jpeg)

Fig. 2 Three stages of the proposed approach: (a) modeling principle for functional mode-inductive stage to establish "baseline" of behavior in functional (nonfaulty) mode, (b) modeling principle for dysfunctional mode-inductive stage to characterize effects of faults, and (c) modeling principle for dysfunctional modedeductive stage to identify and hierarchize causes of performance drift

The detection of faults (dysfunctional or "out of control" states) in the Bayesian network modeling the system can therefore be considered by adding extra discrete nodes to the time-monitored variables-that means inserting control charts at key points for monitoring purposes. In this way, it is possible for example to detect abnormally high heating consumption compared with normal performance for the considered period, which might suggest a fault.

3 Case Study of a Building
3.1 Presentation of the Building. The building we choose 321 for our case study belongs to CEREMA in Ponts-de-Cé, in France. 322 A surface area of $105 \mathrm{~m}^{2}$ was instrumented for the purpose of our 323 study (see Fig. 3). This building was erected in the 1970s and is 324 constituted of common aggregate blocks without insulation. 325

![img-2.jpeg](img-2.jpeg)

Fig. 3 Modeling using Sketchup 3D ${ }^{\circledR}$ of CEREMA building

326 Insulation was added to the suspended ceilings in the 1990s. The windows are double-glazed $(4 / 6 / 4)$ with aluminum frames. The building uses mechanically controlled single flow ventilation. The heating is supplied by a standard high-temperature water loop system.
330 Some hundred sensors were installed to monitor temperature, 331 caloric requirements, and occupancy level (see sensors installation 332 in Fig. 4). Temperature gauges were placed in each room at a height of 1.50 m on interior partition walls, away from windows and doors. The caloric requirements were monitored using ultrasonic calorimeters placed at the entry of the heating water loop, meaning we may consider that the energy measured is used entirely for heating and that heating network losses are moreover recovered. In view of its complexity, it was decided to monitor the occupancy level using presence (passive infrared motion detection sensors) and windows' opening/opening sensors. The status of artificial lighting is also checked (with luxometers), and the loads due to plug-connected equipment are measured.
343 The TROXYS tool was used to model the thermal performances of the building. The model was calibrated/trained with data collected
by Caucheteux et al. [51] during a whole year from Jan. 1, 2013 to 345 Dec. 31, 2013. Once trained, we have applied the model for a new 346 heating period ( 151 days between the Oct. 1, 2015 and the Mar. 1, 347 2016) in order to assess the accuracy of our thermal model. We 348 defined multizone models from the instrumented zones, and the 349 Contam tool was coupled to TROXYS for the airflow modeling (Contam is a multizone airflow and contaminant transport analysis pro- 351 gram. It can help determine airflows such as infiltration, 352 exfiltration, and room-to-room airflows in building systems driven 353 by mechanical means, wind pressures acting on the exterior of the 354 building, and buoyancy effects induced by the indoor and outdoor 355 air temperature difference). The model included mechanical ventilation, air infiltration, and all opening of doors and windows. As 357 regards air tightness, it was found that the majority of leaks came 358 from windows. Therefore, for the purposes of the modeling, infiltrations were considered not just as proportional to the surface of 360 walls but also linked to the quality of the openings. Finally, the 361 occupants were modeled as "persons seated in thermal comfort at 362 their workplace." The simulations were carried out to determine 363 the caloric requirements in each zone (instrumented $\div$ modeled). 364 In Figs. 5(a)-5(c), we present comparisons between simulated and 365 real measurements for temperatures and required heat quantity 366 (HQ). Specifically, Fig. 5(a) presents the variation of the required 367 heat quantity as a function of the difference between indoor and 368 outdoor temperatures for both simulated and real data. In Figs. 369 $5(b)$ and $5(c)$, we give the details of the variation of the difference 370 between indoor and outdoor temperatures and of the required 371 daily heat quantity as functions of time (from the Oct. 1, 2015 to 372 the Mar. 1, 2016). To assess the agreement between simulations 373 and real results, we calculate the normalized mean bias error 374 (NMBE) and the coefficient of variation of the root-mean-squared 375 error (CV(RMSE)) which are two metrics recommended by both 376 ASHRAE and IPMVP [52, 53]. Based on hourly measurements, 377 we calculate a NMBE of $\sim 2.82 \%$ and a CV(RMSE) of $27.02 \%$. 378 ASHRAE guideline 14 and IPMVP, respectively, require that 379 these values should not exceed $10 \%$ and $5 \%$ for NMBE, and 30380
![img-3.jpeg](img-3.jpeg)

Fig. 4 Positioning of different sensors installed by CEREMA

![img-4.jpeg](img-4.jpeg)

Fig. 5 Comparisons between the results obtained from DES model and actual data: (a) Variation of the required HQ (for the whole surface area of $105 \mathrm{~m}^{2}$ ) as a function of the difference between indoor and OTs for both simulated and actual data, (b) variation of the difference between indoor and OTs as a function of time, and (c) variation of the required daily HQ (for the whole surface area of $105 \mathrm{~m}^{2}$ ) as a function of time

381 and $20 \%$ for CV(RMSE). We must note that the CV(RMSE) calculated for our DES model is beyond the limit recommended by IPMVP. However, since we mainly use the model to detect differences between functional and dysfunctional situations and not to predict exact energy consumption, we finally consider that the DES is accurate in terms of our objective.
3.2 Characterization of External Loads-Meteorological 387 Data. All variables of interest related to outdoor physical phe- 388 nomena influencing the energy performances of the building were 389 considered as external load factors. The first and best known of 390 these phenomena is climatic conditions, which, with year-to-year 391 variability, seasonality effects, and variations over time, 392

Table 1 Monitored variables


${ }^{a}$ This variable is deduced from the measurements but is not considered as an internal load. It is used along with the permeability, wind velocity, and relative pressure data to characterize the leakages.

393 determine the performance level required for a building and its 394 equipment to ensure the comfort of its occupants.
395 In our study, dynamic meteorological data were collected via a 396 weather station installed on-site. This was equipped with the temperature, relative humidity, global horizontal radiation, wind 398 speed, and direction sensors.
399 The station location must be chosen in such a way that it com390 ply with WMO recommendations [54], i.e., away from obstacles 401 and in a grassy area. Wind speed measurements may sometimes 402 by affected by certain external phenomena. The measurements 403 taken were therefore broken down into two: light winds and strong 404 winds. If the anemometer has a resolution of $1 \mathrm{~m} / \mathrm{s}$, only wind 405 speeds above $1 \mathrm{~m} / \mathrm{s}$ can be measured.
406 To complete the meteorological data, the renewal of air was 407 monitored through the ventilation flow rates and the air permeability of the building. The flow-rate measurement of the single 408 flow ventilation installed was achieved via by an air flow-rate 410 measurement cone connected to a hot wire sensor or anemometer.
3.3 Characterization of Internal Loads. The behavior of 412 building occupants can make it difficult to follow the conventional 413 scenarios outlined by the regulations in place. People interact with 414 their immediate environment searching for desired comfort level 415 of which the most direct indicator is indoor temperature. In adjusting this temperature (or other systems), occupants influence the 417 energy consumption.
418 Electrical equipment and appliances are supplementary sources 419 of energy. These variables-indoor or preset temperature, number 420 of occupants, internal sources-contribute to the building dynam421 ics and have to be considered as internal loads. These interdependent variables are indirectly characterized via the installed sensors. 423 Table 1 lists all variables that are directly measured or (indirectly) calculated.
425 Occupancy can become a significant internal load. By "occupancy" is meant the number of persons present in the building at a given time in conjunction with their behavior. The energy 428 consumption of a building is directly linked to the occupancy rate 429 as well as the behavior of the users. Workplace occupants can be 430 a serious source of loss and this is a factor that affects the building dynamics: for instance, opening doors and windows necessitates 432 an additional supply of heat energy in order to balance thermal losses. However, occupants can also be a source of energy by their activity. In our study, we have considered that every occupants 435 are sitting persons in thermal comfort. Their metabolic rate is about $58 \mathrm{~W} / \mathrm{m}^{2} /$ person ( 1 Met ) [55] with a body surface for average adult of $1.7 \mathrm{~m}^{2}$; therefore, the energy released by metabolism 438 is taken at $100 \mathrm{~W} /$ person (direct energy source). Devices used by 439 occupant (household appliances in a residential building and IT440 related in a tertiary building) also supply energy to the building 441 that can be quantified as an internal source (indirect energy source). This indirect energy source is dissociated from the occupancy and dealt with independently in the form of internal 444 sources.
445 To estimate the occupancy level of a building, several estimators are used based on different measurement protocols that have 447 been established [51-56]. They can be based on video recordings,
measurement of $\mathrm{CO}_{2}$ concentration, motion detection, noise anal- 448 ysis, or electricity consumption data [57,58]. The combination of 449 several of these measurements provides more detailed information 450 regarding the occupancy level and thus a reduction of the uncertainty of the estimation [59]. In our study, the occupancy level is 452 characterized via measurements from motion detection sensors 453 (passive infrared), $\mathrm{CO}_{2}$ sensors, lux meters for artificial lighting, 454 sensors for opening/closing of windows, and electricity consumption sensors for socket loads. As far as internal heat sources are 456 concerned, it is quite a complex matter to measure the quantity of 457 heat effectively released by occupants and electrical equipment. 458 The most common practice consists in measuring electricity consumption and assuming that all the power consumed by electrical 460 equipment is totally released within the building.
461
The indoor temperature is the ambient temperature of a room 462 that is regulated via a preset temperature in order to achieve the 463 desired thermal comfort. The indoor temperature can be measured 464 in every room. In addition, surface temperature measurements can 465 be taken, as well as measurements of the air temperature at the 466 exit of the heating supply devices.

## 4 Construction of the Bayesian Network

The construction of the BN follows the six steps mentioned in 469 the previous Sec. 2.3.

### 4.1 Step 1-Collection of Data and Prediction of Heat 471 Quantities by Means of Dynamic Energy Simulations. The 472 inputs and outputs of the model are shown in Table 2.

The indoor data were collected from a floor of the building with 474 sensors installed according to the measurement plan shown in 475 Fig. 4. The outdoor data were mainly obtained from our meteorological station and completed with data from a regional station. 477 All the data were recorded from Jan. 1, 2013 to Dec. 31, 2013. 478 The outputs are the predicted heat quantities in each room of the 479 building; predictions were made through the DES model.
4.2 Step 2-Choice of the Learning Algorithm for the 481 Construction of the Bayesian Networks. The construction of a 482 BN consists mainly in finding the set of relationships (links) 483 between variables (nodes) and the conditional probabilities tables 484 between the thus linked variables. The goal here is to find the BN, 485 with a controlled level of complexity, which best fits the training 486 database and can give accurate predictions. We typically have to 487 deal with a complex combinatorial problem, which first requires 488 specific algorithms to detect conditional independences and then 489 heuristic search in the solutions space. We have tested several current learning algorithms to find the one(s) that are the most appro- 491 priate for our problem. Table 3 shows all the different alternatives 492 we have compared. Most of these inference algorithms dedicated 493 to discrete nodes are available in the HIGH software or toolboxes 494 like BNT computed with MATLAB by Murphy [60].
495
From the same database, an algorithm alone can provide multi- 496 ple nearly optimal solutions, and, another algorithm can give dif- 497 ferent candidate solutions. A way to compare the efficiency of the 498 algorithms is to calculate the biased variances for each model 499

Table 2 Input and output variables of the model constructed by BN






Table 3 The different combined or hybrid learning algorithms


![img-5.jpeg](img-5.jpeg)

AL: Air Leakage
AP : Atmospheric Pressure
DR : Diffuse Radiation
HQ : required Heat Quantity
IG : internal heat gains
IT : Indoor Temperature
OT : Outdoor Temperature
Pre : Presence sensing
RH : Relative Humidity
SA : Sun Azimuth
SG : Solar heat Gains
SH : Solar Height
THR : Total Horizontal Radiation
WD : Wind Direction
WS : Wind Speed
Fig. 6 Bayesian network for operational mode solely for Office \#5 (with hourly measurements over a period of a year)
using an information criterion for the selection of the model (e.g., 501 akaike information criterion (AIC)—or Bayesian information criterion (BIC)); the main concern here is to use the same score 503 when comparing the BN architectures in order to choose the one 504 which is the best in an objective way.
505 In order to test our method, we applied it to a single office (see 506 Fig. 4-corner office \#5) for which a large range of sensors and 507 data were available.
508 Figure 6 shows the inputs (parent nodes) taken from meteoro509 logical data (upper part of the diagram) and those taken from 510 measurements obtained from sensors inside the rooms (lower 511 part). This figure reports one of the best candidate solution 512 obtained, considering hourly measurements over the whole year, 513 with nodes discretized via an algorithm based on AIC. The mar514 ginal probabilities and tables of conditional probabilities for the 515 nodes were learned from a no-fault data file (since we are in oper516 ating mode).

It needs to be specified clearly that the purpose of our method- 517 ology is not to establish automatically the final BN architecture 518 but just to give to the user a starting point reflecting visually the 519 causal relationships between the various variables. Experts from a 520 physical understanding of various phenomena must validate these 521 conditionally dependences and independences. Their expertise is 522 essential in the construction of the final BN architecture. More- 523 over, the experts may add or delete some arcs in the network if 524 they consider that necessary.
525
As an example of causal relationships explanation, the network 526 in Fig. 6 shows that the energy need (output of the child node) 527 HQ, equivalent to the heating consumption, is directly dependent 528 on indoor temperature IT but equally on the air leakage (AL) level 529 AL of the envelope. However, the fact that the conditional distri- 530 bution for each variable is defined according to its parents does 531 not signify that no other variables influence it. Indeed, nodes IG 532 and HQ are conditionally independent if and only if all the nodes 533

![img-6.jpeg](img-6.jpeg)

Fig. 7 Bayesian network for operational mode for whole floor (with hourly measurements over a period of a year)

belonging to the Markov blanket of IG (or HQ) are observed (i.e., one knows theirs values). Thus, in Fig. 6, HQ is conditionally independent of IG if the nodes IT and AL are observed. That means that knowing IG when IT and AL are observed does not change anything in the computation of the probabilities of the various modalities of the node HQ. Nevertheless, if AL is not observed, then IG influences the probabilities of the modalities of the node HQ because of the path: IG-Pre-SA-THR-OT-AL-HQ. In addition, the OT node influences the HQ if AL is not observed. From a physical point of view, if the AL is inexistent (perfect airsealing quality) the OT should not influence the HQ (i.e., HQ is influenced by OT only if AL exists).

The same task of modeling the operational mode by BN was carried out for a whole floor by "forcing," during the network architectural stage, the grouping together of variables of the sametype (for example, heating consumption HQ for offices nos. 2-7 combined). The relationships between nodes of the same type are shown with thin-lined arrows. The relationships between nodes of different types (for example, OT and air leakage in the office \#6 AL_Office\#6) are shown with thick-lined arrows. Of course, many number of different BN models for operational mode are possible, limited only by the extent to which the physical coherence of the relationships established between the network variables can be justified. In Fig. 7, we show the BN adopted based upon a minimized BIC index, from which we can discuss some examples of causal relationships. Physically, there is a link between outdoor (OT, RH) and indoor (indoor temperature (IT)) conditions. The network shown in Fig. 7 proposes a link between RH and the AL. It is not what was first expected, but the link is consistent. Indeed, considering that AL can be regarded as a heat loss by air leakage, there is an obvious link with the outdoor conditions. Some links are less intuitive. For example, the link between Solar Azimuth (SA) and people presence (Pre) was unexpected. Nevertheless, if we consider the correlation between SA and the hour of the day, it is now obvious to see a relationship between the hour of the day and the presence of people. Of course, all relationships can be discussed but a coherent explanation can be provided for most of them and the BN can be consider as acceptable.
4.3 Step 3-Study of the Bayesian Networks Robustness Against Database Reduction. The ability of a BN to detect and diagnose faults is conditional upon its robustness against parameters related to the data exploitation or extraction. We need to check if the general architecture of the BN and its capacity to model the data is deeply modified when we consider only a part of
the database or when we take the average of the hourly measure- 578 ments on a daily base. The main objective is to see eventually if we can construct a BN with equivalent quality but with fewer data 580 to process.

First, keeping to the same hourly measurements, we have 582 reduced the database to data for which heating consumption was 583 different from zero for all offices. We thus excluded data for 584 which an energy need had not been calculated for at least one of 585 the six offices. The new BN obtained in this case is presented in 586 Fig. 8. Comparison to the equivalent BN with the complete data- 587 base shows only minor changes in the relationships between variables of the same type and in the relationships between types. Only 589 one significant relationship appears (see black thick arrow), 590 between the indoor temperature in office \#6, IT_office\#6, and the 591 energy need in this office HQ_office\#6. Therefore, this first modi- 592 fication of the quantity of data taken into account and the very 593 slight change of the BN seems to demonstrate the robustness of 594 our method and that we can reduce the database to the periods 595 recording energy needs.

The second test consists in modifying the frequency of data 597 acquisition. Here, we examined the sensitivity of the BN to a 598 change from hourly to daily measurements; the inputs are the 599 averages of the values recorded over a day for all characteristics 600 measured (including, e.g., wind direction, in degrees). In Fig. 9, 601 we show the new BN modeling the relationships between variabels for the whole floor \#1 reducing data to daily measurements 603 over a period of a year. The results are interesting: although a 604 large majority of the internal relationships between nodes remains 605 after change of frequency of measurement, one can see a higher 606 number of new links between characteristics of different types 607 (see black thick arrows).

The two BN's robustness tests we have conducted allow us to 609 conclude that we can use a reduced part of averaged data with 610 small disturbances of the BN architecture and of its efficiency. 611 The calculation time decreases which will be useful when we will 612 adopt continuous nodes rather than discrete ones in step 4 (Sec. 613 4.4) and when we will need to develop DBNs in step 5 (Sec. 4.5). 614
4.4 Step 4-Choice of Type of Nodes. In the following 615 steps, having confirmed the effectiveness of the construction 616 method of the BNs for the purposes our study, we choose to not 617 discretize the nodes in order to avoid any loss of information; all 618 the nodes will be modeled from continuous statistical distribu- 619 tions. We maintained the assumption that they follow a Gaussian 620 distribution law and that they are not interlinked via linear 621

![img-7.jpeg](img-7.jpeg)

Fig. 8 Bayesian network for operational mode for whole floor (using hourly measurements during period of heating only)
![img-8.jpeg](img-8.jpeg)

Fig. 9 Bayesian network for whole floor (using daily measurements over a period of a year). Implementation of a $7^{\text {e }}$ Hotelling multivariate control chart to detect drifts of the energy needs is also illustrated.

622 dependency relationships. It should be noted that these assumptions can change depending on whether one deals with a discrete or a specific inference node (nonlinear non-Gaussian).
625 Once the network structure and its parameters are defined, it is essential to use propagation algorithms that are appropriate to the chosen structure in order to calculate marginal distributions as well as probability distributions for each variable. Several inference algorithms have been suggested in the literature for Gaussian conditional networks. We used two algorithms based on the junction tree [61,62]. We implemented them with the $R$ scientific computing environment. These algorithms allow accurate inference in Gaussian conditional networks.
634 We also wanted to guarantee better AIC or BIC scores (information criterion) for the choice of BN models. It is therefore necessary to reduce the impact of local optima during optimization of the architectures and parameters of the BNs. We thus adopted the bootstrap resampling method already used in Sachs et al. [63]. In practical terms, this consists in repeating the learning of the structure several times, which allowed us to explore a large number of
networks, to average the networks obtained (see Ref. [64]) and to 641 finally conserve only the relationships (links) that were present in 642 at least $85 \%$ of the networks. Figure 10 illustrates the final BN 643 obtained with continuous nodes. Some changes are observed 644 between this BN and the one obtained with discrete nodes, but the 645 general architecture remains. The BIC score for this BN with con- 646 tinuous nodes is nearly the same that for discrete nodes $(-49,727647$ versus $-50,523$, i.e., a sensible loss of $1.6 \%$ ). We will use contin- 648 uous nodes for the upcoming simulations with the aim to obtain 649 results that are more accurate.
4.5 Step 5-Creation of Bayesian Network in Dynamic 651 Mode. The DBNs are a special class of BNs; it includes the effect 652 of time by considering that the value of a variable at a given time 653 can influence its own value at the next time [65]. If we consider a 654 set of $n$ variables $\boldsymbol{D}(t)=\left\{D_{1}(t)\right.$; $\left.D_{2}(t)\right\} \ldots ; D_{n}(t)\}$ varying with 655 time, a DBN adds the joint probability distribution of these variables for a bounded interval $[0 ; T]$. Generally, this distribution can 657

![img-9.jpeg](img-9.jpeg)

Fig. 10 The Bayesian network for whole floor (using daily measurements over a period of a year) with continuous nodes
![img-10.jpeg](img-10.jpeg)

Fig. 11 Illustrations of a dynamic Bayesian network with two different levels of significance: (a) Relationships between variables at $(t-1)$ and $(t)$ for a level of significance $p$-value $<0.01$ and $(b)$ relationships between variables at $(t-1)$ and $(t)$ for a level of significance $p$-value $<0.001$
be expressed as a static BN with $T \times n$ variables where $T$ is the number of time intervals considered. If the process we consider to model is stationary, the assumptions of independence and the associated conditional probabilities are identical for all time intervals $\Delta t=(t)-(t-1)$. In this case, the DBN can be represented by a BN whose structure is duplicated for each time-step. A node therefore represents a random variable whose value indicates its state at time $t$.
The DBN are widely studied by researchers. In the domain of energy optimization, DBN are used as a prognostic approach for modeling aggregated load of HVAC systems [66,67], for detecting occupant's interactions with windows [68] or for evaluating the reliability of grid-connected photovoltaic systems [69]. In our case, the prognostic capacity of DBNs is an important improvement in the anticipated detection of operational faults and drifts. Given that the number of dimensions rises as a result of the introduction of the time factor, the problem of optimization related to this choice of BN model may be dealt with via the "least absolute shrinkage and selection operator" or LASSO algorithm explained
in [70]. Interested readers may use the "lars" package for $R$ soft- 677 ware in order to make computations.

Figures $11(a)$ and $11(b)$ present the (repeatable) relationships 679 between the variables of the BN at times $(t-1)$ and $t$ for two lev- 680 els of significance $p$. This $p$-value corresponds to the probability 681 that the hypothesis of an existing relationship between two variables at two consecutive times is null. In the following simulations, 683 we have only considered the relationships with a $p$-value of 0.001 , 684 which in addition contributes to reduce the complexity of the 685 DBN and the simulations time.

Figure 12 illustrates how a DBN can be used to predict energy 687 needs or the heat quantity in office \#6 (HQ_office\#6) using rela- 688 tionships of dependence between time $t$ and $t-1$. The curve with 689 the continuous orange line shows the results of simulation by 690 DBN for the predicted/probable values of heat quantity HQ_of- 691 lice\#6 with time (for a time sequence $t$ ), considering the values for 692 all other variables at instants $t-1$ and $t$. The inputs are daily 693 measurements, and the curve shows energy needs over a year. The 694 dashed blue line on the same figure gives real heat quantity 695

![img-11.jpeg](img-11.jpeg)

Fig. 12 Energy needs (or HQ) of office \#6 (HQ_Office\#6)

HQ_office\#6 measured over the year. The fit between the two curves is very good as long as the target variable HQ_office\#6 is calculated with all the available information (including the heat quantities of other offices, HQ_office\#j). In terms of metrics of comparison between the actual and simulated heat quantities, we found values of NMBE and CV(RMSE) respectively at $-3.8 \%$ and $18.7 \%$ which are still below the threshold values recommended by ASHRAE Guideline [52] and IPMVP [53]. For complete information, the Frechet distance between actual and predicted values is estimated at 2703 . Regarding more precisely the fit of the two curves, it is worth pointing out that the simulations give a lot of noise for the "warm" period, which, however, is of no consequence in the context of assessment of the overall performances guarantee. Therefore, we can estimate that the use of DBNs for this inductive stage to setup a "baseline" (see Fig. 2(b)), from which to detect faults and drifts, is relevant.
4.6 Step 6: Experiment Design Used for Simulating the Effects of Fault Situations. Once the baseline corresponding to the normal operating conditions has been obtained, the following step is used to simulate the effects of small faults on the dynamic performances of the building. Then, we create a new database by means of DES with different faults situations from which the DBNs can be updated. It is important to underline that, for this step, we consider that the architecture of the previous DBNs obtained in step 5 is stable; the updating will only concern the conditional probability tables. This makes the assumption that the faults effects, of which amplitudes still remain controlled at the (early) time of detection, had a priori been modeled by the previous DBNs, considering the whole ranges of the variables values of the learning database that encompass the faults amplitudes.
From the 14 input variables (the 15 th variable is the output heat quantity) constituting the basis of the DBN, only a part of them are directly requested as factors for the dynamic energy simulations. All other variables depend on additional factors. Table 4 summarizes the 13 factors for which we have studied the effects of possible deviations from normal conditions. The fourth first factors are variables from the DBN, the nine others are factors on which depend the remaining ten variables of the DBN. In our DESs, the deviation could be either positive or negative depending on whether the fault corresponds to a deficit or an excess (i.e., to a high or low performance threshold). In order to update the DBN, 104 multiple-fault situations have been simulated by DES.

These situations are summed up in Table 10 in Appendix; all the assumptions and data shown in this table are reported in Ref. [56]. 739

## 5 Simulation and Results

5.1 Results for Certain Simulated Faults. Once the 104 fault situations are simulated by DES, we have studied various fault situations in order to test the FDD capabilities of the updated DBNs. In order to avoid overloading the display of the results, only the consumption in office 2, HQ_office\#2, is analyzed here.
Because of the density of the measurements, it is difficult to distinguish the differences between the fault situations and the baseline, referenced as "E0." Therefore, we limit the comparison of the results to the period from 900 to 1800 h .

Figures 13 and 14 illustrate two examples of simulation of energy consumption deviations in office 2 following the appearance of faults. These figures show the deviations of the energy consumption between the baseline E0 and two fault cases. The first one (referenced as "case_1") consists in an increase in the preset temperature of +1 K (see Fig. 13) and the second one (references as "case_2") is a drift of the glazing transmission coefficient of $-0.5 \mathrm{~W} / \mathrm{m}^{2} \mathrm{~K}$ (see Fig. 14). In case_1, the injected fault on IT leads to an average relative discrepancy of performance equal to $+7.64 \%$ (with a standard deviation of $+6.34 \%$. In case_2 (injected fault on Uwi), we observe respectively values of $+1.86 \%$ and $+2.02 \%$ for the average discrepancy and the stand- 761 ard deviation. One will note that the first fault has a higher effect than the second one.

Figure 15 illustrates the probability of a process being under SC $P(\mathrm{SC} / x)$ over time in the case of an increase in preset temperature. The faults are injected independently at time $t_{1}=1000 \mathrm{~h}$ and the simulations are stopped at $t_{2}=1800 \mathrm{~h}$. Here, it is worth pointing out, since only one variable-HQ_office\#2-is analyzed, that the $T^{2}$ Hotelling chart is reduced to one chart, "Xbar and S." Given that case_1 is a simulated fault situation, a very rapid and very clear drop of probability $P(\mathrm{SC} \mid x)$ can be seen after the injection of faults at $t_{1}=1000 \mathrm{~h}$. It is therefore very quick and easy to detect fault situations. But, what is really of interest, and this is the advantage of using BNs, is the ability to carry out a diagnosis, i.e., to determine the most probable initial cause of the fault.

For the same detection threshold (here, for example, $P(\mathrm{SC} / x)=0.6)$ and measurements obtained over a control period of 6 h (c.f. Sec. 5.4. Influence of control period below for a

Table 4 Simulation variables for fault situations


${ }^{a}$ AL: the air permeability coefficient of the nominal situation was taken to be equal to $1.7 \mathrm{~m}^{3} / \mathrm{h} . \mathrm{m}^{2}$. The dispersion typically observed on buildings erected between 1948 and 2000 was retained, which corresponds to a disturbance of the default value by a multiplicative coefficient of between 0.5 and 2 . For instance, the low performance level corresponds here to an air permeability of $3.4 \mathrm{~m}^{3} / \mathrm{h} . \mathrm{m}^{2}$.
${ }^{\mathrm{c}}$ Indoor or preset temperature: the preset temperature uncertainty equates to the measurement uncertainty of the indoor temperature, which covers sensor uncertainty and spatial sampling uncertainty, i.e., $\pm 1^{\circ} \mathrm{C}$.
${ }^{\mathrm{e}}$ Internal heat gains: it corresponds to heat power from electrical devices use. Its uncertainty can be large if not precisely measured.
${ }^{\mathrm{f}}$ Level of occupancy: The occupancy measurement procedure (via motion detection) was affected by a bias consistently tending toward underestimation, due to the possible absence of motion during occupancy as well as the possible presence of multiple individuals in a single office. A disturbance of hourly occupancy of a factor of between 1 and 2 was therefore applied.
${ }^{\mathrm{i}}$ Albedo: it is a coefficient (between 0 and 1) that corresponds to the reflective power of external surfaces around the building. The dispersion comes from the uncertainty of the value (that is usual not measured) and the diversity of surfaces around the building.
${ }^{\mathrm{j}}$ Characteristics of the bays: to represent the uncertainty of the thermal and radiation characteristics of the bays, the modeling variables of the glazing system (woodwork included) are disturbed by the method described in the appendix. The transmission (total and visible) multiplication coefficient for the glazing was considered to be between 0.8 and 1.2: this corresponds to a solar disturbance factor of $\pm 20 \%$ around the basic value of 0.81 .
${ }^{\mathrm{k}}$ Low and high ceilings: the corrective coefficients applied correspond to an insulation thickness of between $10 \mathrm{~cm}(0.5 \times 20 \mathrm{~cm})$ and $24 \mathrm{~cm}(1.2 \times 20 \mathrm{~cm})$; 20 cm being the nominal thickness.
${ }^{\mathrm{l}}$ Thermal bridges: the chosen dispersion deals with uncertainty of the materials and its implementation in the building.
${ }^{\mathrm{i}}$ Exterior walls: the maximum dispersion of the thermal resistance of the air knives from the ThU rules was retained, i.e., between 0.11 and $0.23 \mathrm{~m}^{2} \mathrm{~K} / \mathrm{W}$ (nominal value $U_{\text {wall }}=7 \mathrm{~W} / \mathrm{m}^{2} \mathrm{~K}$ ).
${ }^{\mathrm{j}}$ Windows: The amplitude of the disturbances applied to the conductivity of the filling gas and the thermal transmission coefficient of the woodwork resulted in a variation of transmission coefficient for the glazing system $\left(U_{\text {windows }}\right)$ of between 3.2 and $4.2 \mathrm{~W} / \mathrm{m}^{2} \mathrm{~K}$.
${ }^{\mathrm{k}}$ Nominal ventilation flow rate: ventilation flow rate was measured by the cone method. The measured value was $150 \mathrm{~m}^{3} / \mathrm{h}$. The experimental measurement conditions led us to increase this uncertainty and retain a dispersion of between 100 and $200 \mathrm{~m}^{3} / \mathrm{h}$.

Case_1: Simulated effect of a drift of the preset temperature
![img-12.jpeg](img-12.jpeg)

Fig. 13 Simulation of consumption deviations for an increase in preset temperature (case_1)

779 definition), the fault is more rapidly identified in fault case_1 780 (21 h) than in fault case_2 ( $463 \mathrm{~h} \approx 19$ days). This fact is intrinsically linked to the amplitude of the faults effects. In case-1 we 782 have a simulated average deviation of 249.7 and standard deviation of 53.5 , and in case_2, a mean and standard deviation of 56.1 784 and 34.1 , respectively.

Detection time is an important performance indicator. It 785 depends on various factors; of course, on the amplitude of the 786 fault effect on heat or energy needs HQ , but also on the value of 787 the detection threshold $P(\mathrm{SC} \mid x)$, and on the width of the control 788 period. Detection time is also stochastic in that it depends on the 789 fault injection time. Figure 16 presents the distribution laws of 790

Case_2: Simulated effect of a drift of the glazing transmission coefficient
![img-13.jpeg](img-13.jpeg)

Fig. 14 Simulation of consumption deviations for a deterioration in glazing transmission coefficient (case_2)

Simulations of individual drift effects (both Cases $1 \& 2$ )
$\longrightarrow$ preset temperature +1 K - Case_1 $\qquad$ $\downarrow$ glazing transmission coef. $-0,5 \mathrm{~W} / \mathrm{m}^{2} \mathrm{~K}$ - Case_2
![img-14.jpeg](img-14.jpeg)

Fig. 15 Probability of being under SC after an increase in the preset temperature (case_1) or a decrease in the glazing transmission coefficient (case_2)

791 detection times for a preset temperature and a glazing transmission coefficient drifts for statistically injected fault times taken, 793 for example, between 1000 and 2000 h and for the same detection 794 threshold of 0.6 and with a control period of 6 h . For a very significant effect on energy needs (case_1 of a positive drift of the preset temperature), detection times are short and their distribution 797 follows an exponential law. For a less significant effect (case_2 of 798 negative drift of glazing transmission coefficient), detection times 799 are longer and their distribution follows a lognormal law.
800 If the detection time in case_1 is shorter, it is more difficult to 801 identify the possible causes (and hierarchize them). In fact, the 802 more quickly the fault is identified, the more limited the quantity 803 of available information is, and the more random the characteriza804 tion of the fault will be. Table 5 shows a sorted list, obtained via a 805 BN coupled with control chart, of probable causes of faults. The 806 results have been standardized, and the sum of all the percentages 807 for all 13 variables should equal $100 \%$.
808 A lack of discrimination of possible causes is plainly evident in 809 case_1: while the first six causes listed do represent $82.8 \%$ of the
possibilities, the cause at the top of the list is only 2.3 times more 810 likely than the sixth one. Moreover, the IT variable which is the 811 actual cause of the fault [IT for indoor temperature (or preset)- 812 see Table 4] is not identified as being the most possible cause. In 813 this specific case_1, we think that the weakness in characterizing 814 the fault is due to the fact that the deviations generated by the simulation in the first times after $t_{1}$ were greater than the average of 816 249.7 (which is what was measured between the time the fault 817 was generated at 1000 h and the end of the simulation at 3400 h ). 818

In case_2, the drift has been characterized correctly. The detection threshold is still 0.6 , and the drift is identified after 463 h of 820 operation in degraded mode: having recourse to more comprehensive information, the BN offers clear identification of the cause of 822 drift, which is $U w i$ ( $U_{\text {window }}$ coefficient). $U w a$ is identified as the 823 second most possible cause, however, with 2.8 times less likelihood of being the cause. It seems logical to assume that $U w a \quad 825$ appears as a probable cause because the effect of injecting the 826 fault into $U w a$ only (in a simulation not shown here) gave a simulated mean deviation of 61.8 and standard deviation of 39.8 , in 828

Distribution of detection times after fault injection (detection threshold $P(S C / x)=0.6$ and control period $\delta_{c}=6 \mathrm{~h}$ )
![img-15.jpeg](img-15.jpeg)

Fig. 16 Statistical distributions of detection times after an increase in the preset temperature (case_1) or a decrease in the glazing transmission coefficient (case_2)

Table 5 Ranking in descending order of possible causes of faults or drifts [detection threshold $=0.6-$ control period $=6 \mathrm{~h}$ ]


where AL is the air leakage, IT is the indoor or preset temperature, IG is the internal heat gains, Pre is the level of occupancy, Alb is the albedo, GF is the glazing solar factor, GT is the ground temperature, LC is the low ceiling, TB is the thermal bridges, UR is $U_{\text {roof }}$ or high ceiling, Uwa is $U_{\text {wall }}$, Uwi is $U_{\text {window }}$, and Ve is the ventilation.

![img-16.jpeg](img-16.jpeg)

Fig. 17 Influence of the preset temperature drift amplitude on the probability of process being under SC

Table 6 Influence of drift amplitude (case_1 of preset temperature) on ranking of probable causes of faults [detection threshold $=0.6$; control period $=6 \mathrm{~h}$ ]


where AL is the air leakage, IT is the indoor or preset temperature, IG is the internal heat gains, Pre is the level of occupancy, Alb is the albedo, GF is the glazing solar factor, GT is the ground temperature, LC is the low ceiling, TB is the thermal bridges, UR is $U_{\text {red }}$ or high ceiling, Uwa is $U_{\text {watt }}$, Uwi is $\mathrm{U}_{\text {window }}$, and Ve is the ventilation.

Table 7 Influence of threshold value on ranking of probable causes of faults [control period of 6 h]


where AL is the air leakage, IT is the indoor or preset temperature, IG is the internal heat gains, Pre is the level of occupancy, Alb is the albedo, GF is the glazing solar factor, GT is the ground temperature, LC is the low ceiling, TB is the thermal bridges, UR is $U_{\text {red }}$ or high ceiling, Uwa is $U_{\text {watt }}$, Uwi is $\mathrm{U}_{\text {window }}$, and Ve is the ventilation.
![img-17.jpeg](img-17.jpeg)

Fig. 18 Principle of the fault characterization moving time-window
829 other words, values that are very close to the simulated ones for 830 Uwi only: 56.1 and 34.1 .
831 5.2 Influence of Drift Amplitude. The influence of the drift 832 amplitude has been suggested in the previous paragraphs. Here,
we study this influence by considering the effect of different 833 values of positive preset temperature drifts. To some extent, this 834 parallels to a steady decline of preset temperature control. Figure 835 17 shows the probability $P(\mathrm{SC} \mid x)$ that the process is still under sta- 836 tistical control over time for different drift values from +0.5 K to 837

Table 8 Influence of control period on the ranking of possible causes of faults [threshold of 0.6]


where AL is the air leakage, IT is the indoor or preset temperature, IG is the internal heat gains, Pre is the level of occupancy, Alb is the albedo, GF is the glazing solar factor, GT is the ground temperature, LC is the low ceiling, TB is the thermal bridges, UR is $U_{\text {inof }}$ or high ceiling, Uwa is $U_{\text {wall }}$, Uwi is $U_{\text {window }}$, and Ve is the ventilation.

Influence of control period on the ranking of possible causes of faults [threshold of 0.6]
![img-18.jpeg](img-18.jpeg)

Fig. 19 Simulations of consumption deviations for the case with two simultaneous faults (IT and Uwi)

Table 9 Influence of threshold and control period on ranking of possible causes of faults for two faults appearing simultaneously (IT and Uwi)


where AL is the air leakage, IT is the indoor or preset temperature, IG is the internal heat gains, Pre is the level of occupancy, Alb is the albedo, GF is the glazing solar factor, GT is the ground temperature, LC is the low ceiling, TB is the thermal bridges, UR is $U_{\text {inof }}$ or high ceiling, Uwa is $U_{\text {wall }}$, Uwi is $U_{\text {window }}$, and Ve is the ventilation.
$838+2 \mathrm{~K}$ with a step of 0.5 K . We still consider that, as an example, the detection threshold is 0.6 and the control period is 6 h . We also indicate the different detection times after fault injection (here, fault is arbitrarily injected at 1000 h ).

Of course, detection time decreases when the value of drift increases but, as suggested in the previous paragraphs, there is a negative impact on the ability to identify the possible cause leading to the detected fault. The results of simulations presented in Table 6 show this negative impact that will push to focus on the
necessary optimization of the control parameters (detection 847 threshold, control period ...).
5.3 Influence of Detection Threshold of Control Chart. 849 The results presented previously (see primarily comments on 850 case_1) suggest that the detection time has an impact on the qual- 851 ity of fault characterization. A short detection time mechanically 852 reduces the quantity of information available to the BN coupled 853

Cases_1\&2: Effects of drifts of preset temperature and glazing transmission coef.
![img-19.jpeg](img-19.jpeg)

Fig. 20 Simulations of consumption deviations for the case with two simultaneous faults (IT and Uwi)

Cases_1\&2: Effects of drifts of set-point temperature and glazing transmission coef.
![img-20.jpeg](img-20.jpeg)

Fig. 21 Probability of process being under SC for a case with two faults appearing simultaneously (IT and Uwi)

854 with control chart, thus increasing the ultimate risk of poor characterization of the fault or drift. This detection time, which we cannot a priori fully control, is linked to the detection threshold of the control chart, which, however, can be controlled/chosen. In Table 7 can be seen the influence of the chosen control chart detection threshold on the characterization of the fault for the first case_1, dealt with previously. The threshold values of $0.6,0.5$, and 0.4 were chosen arbitrarily to illustrate this influence.
862 We can see that the injected IT fault is identified at the 0.5 threshold (with a corresponding detection time of around 53 h ) as the most likely one (and 2.8 times more likely than the second fault, IG). For a threshold value of 0.4 (with a corresponding detection time of roughly 114 h ), the first probable cause is unambiguously identified; the probability of the IT fault occurring effectively overtakes that of IG with a ratio of over 15 . This high level of discrimination is because the impact of the IT fault alone on consumption deviations is intrinsically far greater than the effects of the other variables.

Finally, we must point out that in the example given in our 872 study the characterization error for low threshold values grows in 873 proportion to the degree to which the first simulated values differ 874 from the mean value calculated between times $t_{1}$ and $t_{2}$, i.e., the 875 start and end times of the simulation.
5.4 Influence of the Control Period. The previous simulacions have demonstrated that modification of the threshold value 878 can improve the characterization of a fault. The aim of adjusting 879 the threshold value in this way is to mechanically increase the 880 duration over which consumption deviations are measured, thus 881 ensuring that comprehensive information is available and used. 882 Another strategy is possible, namely the adjustment of the control 883 period. The idea is that once a fault has been detected, the measurement of deviations continues for a certain time period $\delta_{c}$ in order to obtain a better fault "signature." In practical terms, that 886 means to increase the time duration of the signal analysis, i.e., to 887 insert a time window into the signal (see Fig. 18).

889 For the threshold of 0.6 , which evidently caused problems for 890 the characterization of the fault in simulation case_1, we tested the 891 influence of the control period, i.e., duration $\delta_{c}$, on the identification 892 of probable causes. Table 8 sums up the results obtained for five val-
893 ues of control period. It shows the impact of the control period on 894 the rank and scale of the probabilities achieved when identifying 895 fault causes. The more the length of the control period $\delta_{c}$ increases, 896 the better the actual cause of fault is detected. In Fig. 19, we show 897 the variation of the probability of being the cause of fault (for the sixth first most probable causes) as a function of $\delta_{c}$. Factor IT is con6989 sidered to be the most probable cause of fault as soon as $\delta_{c}$ reaches about 16 h . After 60 h of control period, the probability of factor IT 900 to be the cause of fault is five times higher than the one of the second 902 ranked possible cause of fault. This ratio exceed ten for $\delta_{c}$ beyond 903 140 h . We might finally be inclined to choose a large control period 904 to be certain to detect the actual cause, but if this control period is 905 too long the consequence of the ongoing deterioration of perform606 ance might be too critical. The choice of the control period length is 907 always a matter of compromise (see Table 9).
908 The results of simulations in Table 9 show that the cause IT is 909 indeed identified as most likely regardless of the control combina910 tion (threshold/period). This is primarily due to the fact that fault 911 IT has a greater impact on consumption deviations than do the 912 other variables. As for cause $U w i$, it does feature among the most 913 likely causes of drift but is never ranked in first or second place, 914 where it should be.
915 5.5 Influence of Number of Faults. We have demonstrated 916 the rich potential of BNs coupled to a control chart in the presence of a single fault-a potential conditional upon an appropriate 918 degree of adjustment of the thresholds and control period. Here, 919 we examine the appearance, after a period of 1000 h , of two faults 920 simultaneously, on variables IT and Uwi. The simulations that we 921 present for office 2 were carried out with two threshold values 922 ( 0.75 and 0.6 ) and two control periods ( 48 and 144 h ). Figures 20 923 and 21 show the results obtained by simulation via BN. Table 9 924 synthesizes the ranking of probable causes of faults.
925 In this situation where two faults on IT and Uwi are simultaneously injected, we have found that the value of the average rela927 tive discrepancy reaches $+9.06 \%$ with a standard deviation of $+7.41 \%$. One remark that the two effects of the fault taken indi929 vidually are almost added together (we recall that the average discrepancies for case_1 and case_2 have been found, respectively, 931 at $+7.64 \%$ and $1.86 \%$ (see Sec. 5.1 )).

## 9326 Conclusion

933 This paper proposes a hybrid FDD method for detecting faults 934 and energy performance drifts in buildings during its operation
and maintenance stage. The method is based on the graphical 935 method of BNs. It is referred as hybrid since we use actual data 936 for the BN construction in functional state and DES to create a 937 complementary database in dysfunctional states. We have shown 938 the potential of the BN in the process of detection and ranking of 939 the probable causes of a fault or drift of energy performance for 940 an actual building located in Les Ponts-de-Cé, France.

Our modeling approach is divided into three stages. In the first 942 one, we compile a whole-year database of hourly measured/actual 943 input variables related to environmental conditions, building 944 envelope and energy systems performances, level of occupancy 945 and outputs (energy needs) extracted from actual data and/or pre- 946 dicted from DES. The DES model of the building is validated by 947 comparisons with the measured energy needs.

In the second stage, we explore a number of alternative Bayes- 949 ian networks designed for the modeling of a building in opera- 950 tional mode. The BN is used to simulate a baseline of the energy 951 needs variations in this operational mode, as a function of input 952 variables. A robustness study allows us to reduce the size of the 953 database with small disturbances on the BN architecture and on 954 its efficiency. This database reduction and the consequent 955 decrease in the computation time facilitate the development of 956 DBN with continuous nodes for more accurate simulations and 957 better diagnosis and prognostic performances. This DBN is 958 updated in a third stage using DES simulating several types of 959 faults or drifts of the model inputs. Once the inference rules for 960 dysfunctional operating modes are constructed, we carry out FDD 961 simulations. We show the potential but also the limitations of 962 using this approach for the ranking of probable causes of an 963 energy performance fault. Some of these limitations can be 964 explained by imperfect optimization of the control period and the 965 threshold adjustments of the control charts. The suggested 966 approach seems to have a lower degree of accuracy when several 967 faults appear simultaneously. In our further works, we will try to 968 address these shortcomings.

## Acknowledgement

This study was funded by the grants from the National Associa- 971 tion of Research (ANR) in France within the OMEGA project and 972 the data were provided by CEREMA (Centre d'Etudes et d'exper- 973 tise sur les Risques, l'Environnement, la Mobilité et 974 l'Aménagement).

Funding Data

- National Association of Research (10.13039/ 501100001665).

Table 10 The 104 fault situations simulated to update the DBN [low, high, and nominal level of performance are respectively coded by numbers $(-1),(+1)$ and $(0)]$.


Journal of Dynamic Systems, Measurement, and Control
MONTH 2019, Vol. 00 / 000000-19

Table 10 (continued)


Table 10 (continued)

