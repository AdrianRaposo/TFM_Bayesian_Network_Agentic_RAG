# HAI <br> open science 

## Reliability assessment of generic geared wind turbines by GTST-MLD model and Monte Carlo simulation

Yan-Fu Li, S. Valla, Enrico Zio

## To cite this version:

Yan-Fu Li, S. Valla, Enrico Zio. Reliability assessment of generic geared wind turbines by GTST-MLD model and Monte Carlo simulation. Renewable Energy, 2015, 83, pp.222-233. 10.1016/j.renene.2015.04.035 . hal-01176996

## HAL Id: hal-01176996 <br> https://hal.science/hal-01176996v1

Submitted on 16 Jul 2015

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# Reliability Assessment of Generic Geared Wind 

Turbines by GTST-MLD Model and Monte Carlo Simulation

Y.F. $\mathrm{Li}^{1}$, S. Valla ${ }^{1}$, E. Zio ${ }^{1,2}$<br>${ }^{1}$ Chair on Systems Science and the Energetic Challenge, Fondation EDF, at<br>CentraleSupelec, France<br>${ }^{2}$ Dipartimento di Energia, Politecnico di Milano, Italy


#### Abstract

In the last decade, the installed capacity of wind turbines has increased far more than other renewable energy sources such as solar, biomass or geothermal. As for any energy equipment, reliability is the fundamental attribute that needs to be guaranteed. A number of studies have been carried out for wind turbine reliability assessment. Most of them model the wind turbine system as a whole, without investigating its interior structure and failure logic. In this paper, a modeling and simulation framework is proposed for the reliability assessment of generic geared wind turbine systems. It is based on a Goal Tree, Success Tree and Master Logic Diagram for modeling the relationships among components and functions in a wind turbine system, and the impact of factors and mechanisms influencing the failure of the components. The modeling framework is customized to represent the strength of the relationships and the uncertainty of the impact of failures of these components on other components and functions. The model is eventually integrated in a Monte Carlo simulation framework for the computation of the wind turbine system reliability. Finally, model validation is performed by comparing the simulation results with those obtained by a Bayesian network model developed for this purpose.

Keywords: reliability, wind turbine, goal tree, success tree, master logic diagram, Monte Carlo simulation

# 1. Introduction 

In recent years, technological advances have led to the development of small-scale, userfriendly, easily installed renewable energy systems. These types of systems enable energy end-users to install renewable generators on-site, connect them to the distribution network and trade energy on the electricity market. The functionality of these systems is dependent on the functions provided by different components, whose reliability must be properly designed and availability carefully maintained [1-3].

Wind is a resource that can be used in excess without threatening to reduce its natural stock. In fact, wind can be found almost anywhere on Earth. Even though wind power systems are only used within a certain range of wind speeds, this type of energy production is quite efficient. Although the power outputs depend on wind speed, a wind turbine on land can often generate a certain percentage of its theoretical maximum energy output, e.g. $20 \%$ to $30 \%$ in the case of a onshore small wind turbine located in UK [4]. In addition, a wind turbine produces enough electricity in six to eight months to "pay back" the energy used to manufacture and install the equipment [5].

Wind turbine operation and maintenance represent an important part of the cost of wind power production. In fact, the share of operation and maintenance costs represents $20 \%$ to $25 \%$ in the lifetime of a wind turbine. Actually, these costs are limited to $10 \%$ to $15 \%$ when the wind turbine is fairly new, but they increase to at least $20 \%$ to $35 \%$ by the end of its lifetime [6]. Modeling can help reduce these costs, as it provides information for the development of maintenance and repair policies.

The goal of the work presented in this paper is to develop a modeling and simulation framework to evaluate the reliability of a generic geared wind turbine system. The power law process [7] and exergy analysis [8] have been used in the past to model the wind turbine system as a whole. However, these reliability modeling frameworks fail to account for the complexity of the interior structure of the wind turbine system. For example, Guo et al. [9] assume that the failure of any subassembly leads directly to the failure of the wind turbine. However, in reality the failure logic of wind turbine systems is more elaborated because of its interior structure. For example, if the anemometer fails during the operation of the wind

turbine system, it can certainly affect the electronic control but there is uncertainty surrounding the extent to which this failure affects the performance of the wind turbine system. The system logic of the wind turbine is such that it can still produce electricity even though some of its components have failed, although possibly in a less efficient way. In the example stated above, the failure of the anemometer can lead to inaccurate readings of the wind speed, which leads to providing less reliable information on which to base the system adjustments.

In order to describe these conditions, a third state of degraded operation is introduced whereby the wind turbine system is performing its function but less efficiently. This is done to extend the common binary state description of system function (operating or failure). Actually, in practice, different minor failures of components could lead to various degradations, and correspondingly different performance levels. In this case, the state of degraded operation could be further discretized in levels of performance depending on the extent of the impact the components failures have on the wind turbine system. The transition dynamics would, then, be governed by the corresponding transition probabilities (see Section 4). To this day, however, it is difficult to quantify the impact of components failures on the wind turbine system in practice and, even more so, to obtain the related field data necessary to estimate the degradation model parameters. For this reason, we limit the description to the three states in this work, as discussed previously, which render the model feasible in the current situation. Furthermore, by neglecting the interior structure of the wind turbine system, the reliability models proposed in the literature do not consider the logic and functional relationships between the different components in the system. On the contrary, this is quite relevant to the electricity production function of the wind turbine. For example, if a sensor fails it can affect the electronic control which commands the system operation adjustments with respect to the signal measured by the sensor; in turn, the actuating hydraulic system controlled by the electronic control can fail and this can impact the functionality of the mechanical brake; failure of the mechanical brake to fulfill its function can lead to the failure of the low speed shaft of the turbine, and this can force the wind turbine system to a stop.

Reliability models focusing on specific components or subassemblies have been developed, including Miner's rule approach [10-12], neural networks [13], 3D finite element formulations [14,15], non-homogeneous Poisson processes [16] and Markov processes [17-

19]. They allow reliability assessment to be performed at the component/subassembly level but not at the wind turbine system level.

In the end, the wind turbine system has a certain logic complexity and the relationships within and between its subsystems must be considered and described for a proper evaluation of system reliability and availability. Approaches to do this can be function-oriented or object-oriented. Function-oriented approaches, such as structured analysis and design technique (SADT) [20] and multilevel flow modeling (MFM) [21], allow the system to be analysed according to goals and functions which are to be attained by all parts of the system in order to perform its function. On the other hand, object-oriented approaches such as the dynamic flowgraph methodology (DFM) [22] may be used to describe either the static or the dynamic structure of a system by defining the material elements and their interactions [23].

In this paper, the Goal Tree, Success Tree and Master Logic Diagram (GTST-MLD) framework is used to model a wind turbine system for its reliability evaluation. The Goal Tree, Success Tree (GTST) and Master Logic Diagram (MLD) is a relatively recent approach, which has the advantage of integrating both of these points of view and has proven to be a powerful hierarchic method to represent the system [24-29]. The framework provided allows the modeling of the relationships between components and functions in a wind turbine system, as well as the impact of factors and mechanisms influencing the failure of the components. The modeling framework is further customised to represent the strength of the relationships and the uncertainty of the impact of failures of these components on other components and functions. These aspects are eventually integrated in the simulation framework for the computation of the wind turbine system reliability. Finally, the model is validated by comparing the simulation results with those obtained by a Bayesian network developed for this purpose.

The rest of the paper is organised as follows. Section 2 presents background information on a generic geared wind turbine system architecture and the definition of its reliability. Section 3 presents the GTST-MLD modeling framework and its customisation to the wind turbine system. Section 4 presents the simulation framework for the quantification of the model and the results obtained; also, a comparison is given with the results of a Bayesian network developed for this purpose. Finally, Section 5 offers the conclusions on the modeling framework proposed and recommendations for future work.

# 2. Wind Turbine System Architecture and Reliability 

### 2.1 Architecture of A Generic Geared Wind Turbine and Functionalities of Components

A generic geared horizontal-axis wind turbine (HAWT) of Figure 1 is used as reference system for the model and simulation framework development presented in this work. Naturally, the framework can be extended to other types of system designs. For the comprehensiveness of the paper, we give a short description of the system hereafter.

With respect to its operation, the wind acts on the turbine blades as it does on an airplane wing. The shape of the blade causes the air pressure to be uneven around the blade. This is what makes the rotor hub spin at the center of the turbine. On the top of the nacelle - which is part of the structural parts and housing of the wind turbine - a wind vane connected to a controller ensures that the turbine is turned into the wind using the yaw drive in order to capture the most energy. Next to this wind vane is an anemometer which is also connected to the controller. Most wind turbines are only efficient over a certain range of wind speeds, e.g. 4 to $25 \mathrm{~m} / \mathrm{s}$ [30], dependent on the operating concept and the adopted generator technology. Therefore, the anemometer measures the wind speed and the controller acts on the pitch to turn the blades parallel to the wind direction if the wind speed is too low or too high. The blades are connected to a low-speed shaft, which turns around 18 rpm on average [30]. In order to generate electricity with the HAWT, the rotor shaft spins a series of gears in the gearbox to increase the rotation up to around 1800 rpm [30]. Note that the mentioned rotation speeds are applicable only to geared wind turbines. The high-speed shaft delivers mechanical energy from the gearbox to the generator; the generator, then, transforms the mechanical energy into electricity, which is sent to the grid via the electrical system. A vital subassembly in the wind turbine electrical system is the power converter: an electronic device that modifies electrical signals from one kind of level to another. Namely, this can be any of the following conversions: AC to AC, DC to DC, AC to DC, or DC to AC [31]. The electrical system also includes the control unit that it regulates the supply of the power to the grid and provides protection functions [37].

With respect to its logic structure, Figure 2 shows the system logic diagram for the HAWT. The components in grey rectangles represent the primary components: the blades, the rotor, the low-speed shaft, the gearbox, the high-speed shaft, the generator, the yaw system and the electrical system. The wind turbine cannot produce electricity or unable to fulfill the interconnection and the grid code requirements if any of these components have failed. Note that the logic diagram is developed mainly based on the generic WTG architecture defined by

the US Department of Energy as shown in Figure 1 [36] and the WTG decomposition scheme presented in Table II, taken from [7]. This is coming directly from the Windstats database, and provides failure information from each component of the WTGs used in Germany and Denmark. In this decomposition scheme, the WTG components are generic, i.e. no specific types or modes are considered. For example, the generator failure rate counts different types of generators ranging from doubly-fed induction generator to direct-drive synchronous generator. Following [7], the WTGs considered are of the capacities ranging from 100 kW to 2.5 MW.

In this same figure, the secondary components are represented in a white oval: the hydraulic system, the electronic control, some sensors (anemometer and wind vane) and the mechanical brake. The wind turbine system can still produce electricity when some of these components have failed; however, the electricity production would be inefficient. For additional information, Table 1 presents all the components of the HAWT, their functionality, their classification and the factors and mechanisms influencing their roles. The influencing factors are also summarized in Figure 2. These factors can affect the goal function of wind production either directly (by affecting the primary components) or indirectly (by affecting secondary components which, then, can affect the primary components).

The relationships between the different types of components are represented by lines and arrows. First, primary components are connected by lines. These represent the fact that if one of them fails, then the wind turbine system no longer produces electricity and, as such, the system enters in a state of failure. Then, secondary components are connected by directional lines, either solid or dashed. In essence, an arrow going from one secondary component to another represents the fact that the failure of the initial component can affect the state of the other component. For example, the failure of the electronic control can affect the hydraulic system and the rotor. More specifically, the dashed lines represent potential relationships between sensors and components - either primary or secondary. In our model, only the anemometer and the wind vane were considered. However, depending on the wind turbine system, more sensors may exist. For example, accelerometers can be installed to measure the vibration created by a component like the low speed shaft, the gearbox, the high speed shaft or the generator [15].

# 2.2 Reliability of the Wind Turbine System

Reliability is an attribute of a component or system which describes the ability to perform the required function for a given amount of time and under specific conditions [32]. In practical reliability, availability and maintenance (RAM) evaluations, a component or system is often assumed to have only two states - 'operating' and 'failure' - and the underlying stochastic process of failure is described quantitatively by a power law process (PLP) characterized by the failure rate $\lambda(t)$, usually described as a combination of Weibull distribution that takes the shape of a bathtub curve [7].

However, in real components and systems, the process from operating to failure goes through multiple degradation states, and this should be taken into account in the models for reliability analysis. Looking at this from the system level, every component in the wind turbine system has a role that allows it to produce electricity in an efficient manner: if one component fails, then the wind turbine system does not have all the elements required to produce electricity at the planned level of performance. For this reason, three states for the wind turbine system are considered in the model developed in this work: normal operation, degraded operation and failure, denoted by ' $O_{S}$ ', ' $D_{S}$ ' and ' $F_{S}$ ', respectively. If one of the primary components fails, the system enters in a state of failure; if at least one secondary component has failed, the system is in a state of degraded operation. In literature, multi-state modeling has been adopted for WTG reliability/adequacy assessment [38-39]. Most of them model the WTG as a whole without investigating its failure logic and the complexity of its interior structure.

Also, as discussed in Section 2.1, the failure of secondary components can affect the state of the primary components, which impacts the productivity of the wind turbine system. For example, if the hydraulic system fails due to an excessive fluid temperature it can directly impact the state of the mechanical brake, the yaw system and the rotor (cf. Figure 2). In turn, if the mechanical brake fails, it can affect the low speed shaft. Since the low speed shaft, the yaw system and the rotor are primary components, if one of them enters in a state of failure, then it can directly affect the efficient production of electricity by the wind turbine system. This is the assumed logic of operation, degradation and failure with respect to the wind turbine system.

As for the quantification of the model, the aim is to obtain the system state probability vector at time $t\left[P\left(s=O_{S}, t\right), P\left(s=D_{S}, t\right), P\left(s=F_{S}, t\right)\right]$, where $s$ denotes the system state (normal operation, degraded operation and failure).

# 3. GTST-MLD Model of the Generic Geared Wind Turbine System 

In this work, a GTST-MLD is originally used to model the wind turbine system. GTST can logically and hierarchically represent the functions, sub-functions and interactions among the different parts of the wind turbine system that enable it to produce electricity. The goal tree (GT) focuses on the qualities of the system while the success tree (ST) focuses on its parts. Incidentally, a dependency matrix can be used to display the underlying hierarchy of the MLD of the system [33]. The step-by-step process of developing such a model is presented in the following subsections.

### 3.1. Goal Tree

The GT focuses on the qualities of the system. These are composed of its goals and functions. The top function of the GT is named the goal function. In essence, it describes the principal purpose of the system [23]. This function should be carefully defined according to the scope of interest. Then, the goal function is decomposed into sub-functions at increasing levels of detail. The realisation of specified combinations of these sub-functions - named global functions - ensures that the goal function is achieved. A main difference with a fault tree (FT) representation of the logic relationships is that the GT focuses on the functions of the system whereas the FT concentrates on its components.

As explained in Section 2, the goal function of the wind turbine system is to generate electricity and to send it to the grid. This goal function can be decomposed into the following four independent global functions, as illustrated in Figure 3.

- Capture the wind energy;
- Convert the wind energy into mechanical energy;
- Convert the mechanical energy into electrical energy; and
- Send the electrical energy to the grid.

These four global functions represent the four steps of the power generation process in physically unambiguous terms. In Figure 3, these functions are linked by AND logic. In fact, the goal function of producing electricity and sending it to the grid can only be fulfilled if all four steps are completed simultaneously. First, the energy needs to be captured; then, it must be converted into a manageable resource, which requires two steps in this system; finally, the energy must be sent to the consumers. The decomposition of functions of the GT is the starting point of the GTST-MLD and is therefore important to grasp since the rest of the model builds on this concept.

# 3.2. Success Tree 

The ST focuses on the physical aspects of the system and is developed from top to bottom, looking at all levels at which the system can be analysed. In essence, the physical elements collect all the components of the system necessary to achieve any of the functions present in the GT [23].

In the wind turbine system, the ST can be broken down into two sections. First, the component tree includes all the primary components of the wind turbine: the system cannot accomplish its goal function without all of these components correctly functioning. If any one of these components fails then the wind turbine system enters a state of failure. These components are the blades, the rotor, the low speed shaft, the gearbox, the high speed shaft, the generator, the structural parts and housing, the electrical system and the yaw system. These parts are considered as the main elements of the ST.

Then, the supporting tree includes all secondary components, which are required for the efficient production of electricity. If any one of these components fails, the wind turbine system enters a state of degraded operation rather than a state of failure. This state of degraded operation is introduced in order to define the wind turbine system state in which the goal function of producing electricity is still fulfilled but in an inefficient manner. These secondary components are the mechanical brake, the hydraulic system, the electronic control, the anemometer and the wind vane. These are considered as the supporting components of the system. Figure 4 presents the ST developed in this work.

The impacts of the failures of the secondary components onto the primary components are explained as follows. There are analyzed and quantified in the development of GTST-MLD in section 3.5 .

- Mechanical brake: its failure can lead to the failure of the low speed shaft of the turbine, and this can force the wind turbine system to a stop.
- Hydraulic system: its failure can directly impact the state of the mechanical brake, the yaw system and the rotor. In turn, if the mechanical brake fails, it can affect the low speed shaft.
- Electronic control: it commands the system operation adjustments. Its failure can affect the hydraulic system.
- Wind vane: its failure can lead to inaccurate readings of the wind direction and, thus, affect the commands of the electronic control.
- Anemometer: its failure can lead to inaccurate readings of the wind speed and, thus, affect the commands of the electronic control.


# 3.3. Faults and Failures 

Faults and failures are introduced as a third part of the system model to describe the dysfunctional aspects [23]. Defined by the IEC 61508 functional safety standards [34], a fault is an abnormal condition that may cause a reduction in, or loss of, the capacity of an entity to perform a required function; a failure is the termination of the ability of an entity to perform a required function - or in any way other than as required. In this work, all possible causes of failure of the system components are considered as failure-influencing factors. For example, influencing factors are the wear of the mechanical brake, the formation of cracks on the blades, the break of a toothed wheel in the gearbox, the random shocks on a sensor, and the eccentricity of the low speed shaft.

### 3.4. Master Logic Diagram

The master logic diagram (MLD) connects the GT and ST in a clear and logically ordered manner. As seen in Figure 5, a grid is formed and rectangular bars are placed at the intersection between connecting sub-parts of the ST and sub-functions of the GT: a rectangular bar represents the fact that the sub-part of the ST acts on the sub-function of the GT, or that the sub-function of the GT depends on the sub-part of the ST.

### 3.5. Relationship Analysis of the GTST-MLD

Figures 6 and 7 present the complete GTST-MLD modeling framework of the wind turbine system developed in this work. Dependence relationships using a black rectangle are stronger

than those using a grey one. For example, the failure of a blade will have a strong impact on the ability of the system to capture the wind energy. In fact, blades are vital in ensuring the capture of the wind energy since it is the primary contact between the wind and the wind turbine system.

In addition, uncertainty is represented by asterisks: the more uncertain the relationship is, the more asterisks are associated to it in the graphical representation. Using the same example, the relationship between the blades and the capturing of the wind energy is not ambiguous. Therefore, the relationship between the blades and the global function of capturing the wind energy is certain as well as strong and is represented by a black rectangle with one asterisk.

The reasoning behind the greyscale and asterisk assignments in the GTST-MLD developed in this work is that uncertainty is as important to define as relationship strength when modeling a complex system. In fact, these factors are fundamental in developing a reliability model for the wind turbine system.

Using the same logic, the following relationships are represented in Figure 6:

- The relationship between the rotor and the global function of capturing the wind energy is certain as well as strong.
- The relationship between the low-speed shaft and the global function of converting wind energy into mechanical energy is certain as well as strong.
- The relationship between the gearbox and the global function of converting wind energy into mechanical energy is certain as well as strong.
- The relationship between the high-speed shaft and the global function of converting wind energy into mechanical energy is certain as well as strong.
- The relationship between the generator and the global function of converting the mechanical energy into electrical energy is certain as well as strong.
- The relationship between the electrical system (and its back-up) and the global function of sending the electrical energy to the grid is certain as well as strong.
- The relationship between the structural parts / housing and all the global functions is of medium strength and highly uncertain.
- The relationship between the yaw system and the global function of capturing the wind energy is of medium strength and highly uncertain.

The following relationships are represented in Figure 7 between the Supporting Material Elements and the Main System (Figure 6):

- The relationship between the hydraulic system and the yaw system if of medium strength and yet certain.
- The relationship between the hydraulic system and the rotor is of medium strength and uncertain.
- The relationship between the mechanical brake and the low-speed shaft is of medium strength and uncertain.

The following relationships are represented in Figure 7 within the Supporting Material Elements:

- The relationship between the hydraulic system and the mechanical brake is of medium strength and certain.
- The relationship between the electronic control and the hydraulic system is of medium strength and certain.
- The relationship between the wind vane and the electronic control is of medium strength and uncertain.
- The relationship between the anemometer and the electronic control is of medium strength and uncertain.

The following relationships are represented in Figure 7 between the Faults and Failures (influencing factors) and the Supporting Material Elements:

- The relationship between the wear of the mechanical brake and the failure of the mechanical brake is of medium strength and uncertain.
- The relationship between random shock on the anemometer and the failure of the anemometer is strong and yet uncertain.
- The relationship between random shock on the wind vane and the failure of the wind vane is strong and yet uncertain.
- The relationship between wiring issues in the electronic control and the failure of the electronic control is of medium strength and uncertain.
- The relationship between overheating of the electronic control and the failure of the electronic control is of medium strength and uncertain.

- The relationship between high fluid temperature in the hydraulic system and the failure of the hydraulic system is of medium strength and uncertain.
- The relationship between aeration / cavitation in the hydraulic system and the failure of the hydraulic system is of medium strength and uncertain.
- The relationship between the loss of flow in the hydraulic system and the failure of the hydraulic system is of medium strength and uncertain.

The following relationships are represented in Figure 7 between the Faults and Failures (influencing factors) and the Main System (in Figure 6):

- The relationship between the eccentricity of the yaw shafts and the failure of the yaw system is of medium strength and uncertain.
- The relationship between crack formation and the failure of the yaw system is of medium strength and uncertain.
- The relationship between a break in teeth in the yaw wheel and the failure of the yaw system is of medium strength and uncertain.
- The relationship between a toothed wheel displacement in the yaw system and the failure of the yaw system is of medium strength and uncertain.
- The relationship between a random shock on the structural parts / housing and the failure of the structural parts / housing is of medium strength and uncertain.
- The relationship between crack formation on the structural parts / housing and the failure of the structural parts / housing is of medium strength and uncertain.
- The relationship between a wiring issue in the electrical system and the failure of the electrical system is of medium strength and uncertain.
- The relationship between a wiring issue in the generator unit and the failure of the generator is of medium strength and uncertain.
- The relationship between winding damage in the generator and the failure of the generator is of medium strength and uncertain.
- The relationship between the overheating of the generator and the failure of the generator is of medium strength and uncertain.
- The relationship between the wear of the high-speed shaft and the failure of the highspeed shaft is of medium strength and uncertain.
- The relationship between the eccentricity of high-speed shaft and the failure of the high-speed shaft is of medium strength and uncertain.

- The relationship between the wear of the gearbox wheels and the failure of the gearbox is of medium strength and uncertain.
- The relationship between crack formation in the gearbox and the failure of the gearbox is of medium strength and uncertain.
- The relationship between the break in teeth of the gearbox wheels and the failure of the gearbox is of medium strength and uncertain.
- The relationship between toothed wheel displacement in the gearbox and the failure of the gearbox is of medium strength and uncertain.
- The relationship between the wear of the low-speed shaft and the failure of the lowspeed shaft is of medium strength and uncertain.
- The relationship between the eccentricity of low-speed shaft and the failure of the low-speed shaft is of medium strength and uncertain.
- The relationship between random shock on the rotor and the failure of the rotor is of high strength and uncertain.
- The relationship between crack formation on the rotor and the failure of the rotor is of medium strength and uncertain.
- The relationship between a blade adjustment error in the rotor pitch and the failure of the rotor is of medium strength and uncertain.
- The relationship between random shock on the blades and the failure of the blades is of high strength and uncertain.
- The relationship between crack formation on the blades and the failure of the blades is of high strength and uncertain.

Based on the GTST-MLD, the relationships between system elements were analysed (i.e. influencing factors, supporting material elements, primary components and global functions). For this, the approach presented in Brissaud et al [23] was followed.

Let $D_{d}$ represent an influencing factor $d$ (fault or failure) that occurs, where $d=1, \ldots, n_{d}$ and $n_{d}$ is the number of influencing factors. Let $P_{p}$ represent a secondary component $p$ that is in a state of failure, where $p=1, \ldots, n_{p}$ and $n_{p}$ is the number of secondary components. Let $M_{m}$ represent a primary component $m$ that is in a state of failure, where $m=1, \ldots, n_{m}$ and $n_{m}$ is the number of primary components. Let $F_{f}$ represent a global function $f$ that fails to be delivered, where $f=1, \ldots, n_{f}$ and $n_{f}$ is the number of global functions that the system is intended to provide.

Relationships among system elements - which can be direct, indirect or total - are defined in a relationship matrix $A B$. As a general notation, the direct relationship between an element $a$ and an element $b$ in the GTST-MLD hierarchy is indicated at row $a$, column $b$ of the matrix, with the following meaning: $A B_{a, b}$ represents the fact that element $A_{a}$ directly implies (i.e. by itself, without the need of any other element) element $B_{b}$.

Following the approach in Brissaud et al [23], direct relationships are: $D P_{d, p}$, an occurrence of fault or failure $d$ directly implies a failed state of secondary component $p ; D M_{d, m}$, an occurrence of fault or failure $d$ directly implies a failed state of primary component $m ; P M_{p, m}$, a failed state of secondary component $p$ directly implies a failed state of primary component $m ; M F_{m, f}$, a failed state of unit $m$ directly implies a loss of global function $f$.

All these direct relationships are assumed to be independent. As a general notation, their probabilities of occurrence are denoted $P\left[A B_{a, b}\right]$. Note that $P\left[A B_{a, b}\right]$ can be interpreted as a conditional probability: the probability that $B_{b}$ occurs given that $A_{a}$ has occurred. These probabilities describe the uncertainty in the influence $A_{a}$ can have on $B_{b}$ (see Section 4.3).

Other relationships are indirect. For example, the occurrence of fault or failure $d$ can directly imply the failure state of secondary component $p$ and the component $p$ failure state can directly imply the failure state of primary component $m$. Then, the occurrence of $d$ can imply the failure state of $m$ through the failure of $p$. In general, indirect relationship events are combinations of direct relationship events. In the developed GTST-MLD model, only direct relationships are filled in. Then, the total relationships, which logically integrate both direct and indirect relationships, are obtained by the logic expressions of Equations 1 and 2 below:
$D M t o t_{d, m}=D M_{d, m} \cup_{p}\left(D P_{d, p} \cap P M_{p, m}\right)$
$D F t o t_{d, f}=\mathrm{U}_{m}\left(D M t o t_{d, m} \cap M F_{m, f}\right)$
where $D M t o t_{d, m}$ represents an occurrence of fault or failure $d$ (directly or indirectly) implying a failed state of primary component $m$, and $D F t o t_{d, f}$ represents an occurrence of fault or failure $d$ (directly or indirectly) implying a loss of global function $f$.

From the logic expressions (Eq. 1) and (Eq. 2), the system failure probability, (i.e. the probability of failing to supply the global functions) can be computed:
$P\left[F_{f}\right]=P\left[\cup_{d}\left(D_{d} \cap D F t o t_{d, f}\right)\right]$

# 4. Simulation and Validation 

Monte Carlo simulation was used to generate time-dependent state probability results of the wind turbine system from the GTST-MLD. The annual failure frequencies of the wind turbine components in Figure 8 were used for the Monte Carlo simulation of the system failure behavior with respect to time, assuming exponential probability distributions:

$$
F(t)=1-\exp (-\lambda t)
$$

where $\lambda$ is the transition rate in failures per year.

For those components whose failure depends on multiple influencing factors, a uniform distribution of the influencing factor occurrence has been assumed. In other words, if a component functional failure can be due to three direct influencing factors, to each of these factors is assigned an equal probability of occurrence equal to one-third of the functional failure probability of that specific component calculated with (Eq. 4). Furthermore, repairs were assumed as-good-as-new, i.e. after a repair the wind turbine system has the same timedependent state probabilities as a newly installed wind turbine system.

The simulation of system evolution runs in two successive phases: initiation and propagation.

In the initiation phase, the simulation runs as follows:

1) Set time $t$ after last repair, in years.
2) Generate a realisation of a uniform random variable, $v_{i}$ in $[0,1]$
3) Compare the value of $v_{i}$ with the annual probability of influencing factor occurrence, $p_{A}$,
a) If $v_{i}<p_{A}$, then the state of the influencing factor is set to " 0 ", meaning occurrence
b) If $v_{i}>p_{A}$, then the state of the influencing factor is set to " 1 ", meaning no occurrence.

The propagation step of the simulation framework consists in answering the following questions through the GTST-MLD:

- If an influencing factor occurs, how does it affect the components on which it acts on (see Section 3)?
- If a component enters in a state of failure, how does it affect other components?

- If a component enters in a state of failure, how does it affect the system global functions?

This is done by introducing a probability of propagation, $p_{P}$, which represents the probability that the failure of one component will lead another component, or a global function, to enter a state of failure as well. This variable is introduced in order to quantify and model the relationships in the GTST-MLD and is essential to run the Monte Carlo simulation developed in this work. Furthermore, this variable is one of the factors that make the GTST-MLD appealing in that it can be updated when more accurate data are available.

Then, for the first question with respect to each influencing factor of a specific component the simulation proceeds as follows:

1) Generate a realisation of a uniform random variable, $v_{P 1}$ in $[0,1]$.
2) If the state of the influencing factor is " 0 " (occurrence):
a) If $v_{P 1}<p_{P}$, then the state of the component is set to " 0 " (failed).
b) If $v_{P 1}>p_{P}$, then the state of the component is set to " 2 " (operating)

If the state of the specific component considered is " 0 " (failed), then, for the second question with respect to components related to the each other:

1) Generate a realisation of a uniform random variable, $v_{P 2}$ in $[0,1]$.
a) If $v_{P 2}<p_{P}$, then the state of the related component is set to " 0 " (failed).
b) If $v_{P 2}>p_{P}$, then the state of the related component is set to " 2 " (operating)

Finally, with respect to the third question on the effects of component failures on the system global functions:

1) If the state of any primary component is " 0 " (failed):
a) Generate a realisation of a uniform random variable, $v_{P 3}$ in $[0,1]$.
i) If $v_{P 3}<p_{P}$, then the state of the associated global functions are set to " 0 " (unfulfilled).
ii) If $v_{P 3}>p_{P}$, then the state of the associated global functions are set to " 2 " (fulfilled).
2) If the state of all primary components is " 2 " (operating):
a) If any secondary component is in state " 0 " (failed), then the state of the associated global functions is set to " 1 " (degraded).

Propagation needs to be carried out through each relationship defined in the GTST-MLD of the wind turbine system from the primary and secondary components to the global functions (see Section 3). Table 2 illustrates an example of propagation. As seen in the second line, the state of the component is set to " 1 " since the influencing factor occurs (" 0 ") but the random variable realisation is larger than the probability of propagation. Therefore, the associated global function is in a degraded state. On the other hand, as seen in the fourth line, the state of the associated global function is set to " 0 " since the influencing factor occurs (" 0 ") and the random variable generated is lower than the probability of propagation. Therefore, the component is in a state of failure - a state denoted by " 0 " in this work.

# 4.1. Relationship Strength and Data Uncertainty 

Defining relationship strength and data uncertainty is crucial for the quantitative reliability evaluation of the wind turbine system, in which failures can propagate from one component to another. In fact, the impact of a component failure on another component's functionality can be more or less relevant and known with more or less certainty. For example, the impact of a blade failure on the global function of capturing the wind energy is very strong and certain; on the other hand, the impact of a wind vane failure on the electronic control is of medium level and not always certain. More specifically, the failure of the wind vane in a wind turbine system has an impact on the electronic control since the latter, then, would not have accurate wind direction readings to base its adjustments on; however, the wind turbine system could still function without the wind vane, which is the logic in defining the effect of such a component failure to be of medium value.

The impact of a component failure can be more or less important depending on different factors that are known (e.g. extreme change in wind direction) or unknown. This fact is accounted for by introducing an uncertainty description on the variable measuring the strength of the relationship, i.e. the probability of propagation of the failure from one component to another.

In the simulation framework proposed in this work, the uncertainty of the strength of relationship driving the failure propagation is implemented by generating realizations of the uncertain (random) variable 'probability of propagation', representing the strength of the relationship.

The values used in the particular simulation framework here proposed are presented in Table 3. Thus, for example, the probability of propagation representing a medium yet

uncertain relationship - like the one between the wind vane and the electronic control - is represented by a random variable uniformly distributed between 0.25 and 0.75 .

# 4.2. Results 

A total of 10,000 simulations of system behavior were run for different points in time. Figure 9 illustrates the state probabilities as a function of time. As can be expected, the probability of normal operation decreases with time and the probability of failure increases with time. A notable point is that the probability of the wind turbine system of being in a state of degraded operation seems to plateau around 0.2 after 1 year of installation.

### 4.3. Validation by Bayesian Network

Figure 10 shows a Bayesian network developed for the reliability analysis of the wind turbine system considered. It was developed using Microsoft Belief Networks. A Bayesian network is a probabilistic graphical model that represents the conditional dependencies of a set of random variables [35]. The nodes of the graph are random variables in the Bayesian sense observable quantities, latent variables, unknown parameters or even hypotheses. In essence, a Bayesian network is an influence graph.

Bayesian networks allow for the direct computation of the probability that one event (or state) will lead to another. Even though it could seem like a simpler modeling solution for some applications, the conditional probabilities at each node of the Bayesian network must be computed for each possible scenario and entered in the network in order to compute the global state probabilities of the system. This makes it less appealing for the modeling of complex systems with multiple states that require many preliminary calculations that would need to be repeated for any update in the data. On the other hand, the GTST-MLD simulation framework developed in this work does not require these preliminary calculations and, therefore, makes it a flexible modeling tool for complex systems modeling.

In addition, the GTST-MLD developed in this work takes into account relationship strengths and uncertainty factors while keeping the presentation of the complex logic of the wind turbine system clear and unambiguous. As can be seen in Figure 10, a Bayesian network for such a system can be cluttered and the relationships between components can be unclear.

For the numerical comparison, the probabilities of occurrence of each influencing factor presented in Figure 8 were used as prior probabilities in the Bayesian network. Since the program used to develop the Bayesian network simulation did not allow for the generation of

random variables for the uncertain relationships as explained in Section 4.1, it was assumed that the probability of propagation used for uncertain relationships in the Bayesian network simulation was equivalent to the mean of the range defined in Table 3.

For example, with respect to the effect that the failure of the mechanical brake can have on the state of the low speed shaft, which is of medium value and uncertain, instead of generating realizations of a random variable uniformly distributed between the lower and upper bounds, respectively 0.25 and 0.75 , as done in the GTST-MLD Monte Carlo simulation, the probability of such occurrence in the Bayesian network simulation is set to the mean value of the interval of variability, i.e. 0.5 .

Table 4 reports the state probability values at one year, obtained with the Bayesian network and by Monte Carlo simulation. The absolute difference between the results is less than $2.4 \%$, which is judged satisfactory given the slight differences in the assumption made in running the two models.

# 5. Conclusion and Future Work 

In order to analyse the reliability of a generic geared wind turbine system, a novel GTSTMLD modeling framework was developed and quantified by Monte Carlo simulation. The developed framework allows for the representation of the relationships among all functional and material elements of the system in a systematic, clear and effective manner. The global functions that the wind turbine system must fulfill are connected to the components, supporting systems and influencing factors that can affect their state. A systematic and logic relationship analysis can then be performed to determine the direct effect of each influencing factor on each global function. Strength and uncertainty in the failure propagation relationships of the system components can be considered explicitly, which makes the developed model most appealing for a realistic representation and analysis of complex systems.

Then, quantification of the system functional reliability by Monte Carlo simulation becomes straightforward. In order to validate the numerical results obtained, a Bayesian network of the wind turbine system was used, and the results compared satisfactorily with those obtained by simulation.

In this study, a generic geared WTG model is considered for reliability assessment. The level of abstraction of the model achieves a balance between complexity and accuracy for a pilot

study of this kind. However, specific WTG components need to be considered in future works, from the practical point of view. For examples, the different types of generators, e.g. DFIG or SCIG, and the components of the electrical system, e.g. control unit and protection function/components, will be taken into account. This will be done in connection with the redefinition of the goal function(s) of WTGs, e.g. based on the relevant grid code. For example E. ON German grid code may be considered in the identification of the steady state operation goals. The grid code requirements are expected to significantly alter the classification of components. For example, the control unit will become a primary component. A failure in such unit of a DFIG may lead to severe stability problems and actions of protection devices.
