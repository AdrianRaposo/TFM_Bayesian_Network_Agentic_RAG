# Failure Conditions Assessment of Complex Water Systems Using Fuzzy Logic 

Miloš Milašinović ${ }^{1}$ (D) $\cdot$ Damjan Ivetić ${ }^{1}$ (D) $\cdot$ Milan Stojković ${ }^{2}$ (D) $\cdot$ Dragan Savić ${ }^{1,3,4}$ (D)<br>Received: 19 October 2022 / Accepted: 27 December 2022 / Published online: 30 January 2023<br>(c) The Author(s), under exclusive licence to Springer Nature B.V. 2023


#### Abstract

Climate change, energy transition, population growth and other natural and anthropogenic impacts, combined with outdated (unfashionable) infrastructure, can force Dam and Reservoir Systems (DRS) operation outside of the design envelope (adverse operating conditions). Since there is no easy way to redesign or upgrade the existing DRSs to mitigate against all the potential failure situations, Digital Twins (DT) of DRSs are required to assess system's performance under various what-if scenarios. The current state of practice in failure modelling is that failures (system's not performing at the expected level or not at all) are randomly created and implemented in simulation models. That approach helps in identifying the riskiest parts (subsystems) of the DRS (risk-based approach), but does not consider hazards leading to failures, their occurrence probabilities or subsystem failure exposure. To overcome these drawbacks, this paper presents a more realistic failure scenario generator based on a causal approach. Here, the novel failure simulation approach utilizes fuzzy logic reasoning to create DRS failures based on hazard severity and subsystems' reliability. Combined with the system dynamics (SD) model this general failure simulation tool is designed to be used with any DRS. The potential of the proposed method is demonstrated using the Pirot DRS case study in Serbia over a 10-year simulation period. Results show that even occasional hazards (as for more than $97 \%$ of the simulation there were no hazards), combined with outdated infrastructure can reduce DRS performance by $50 \%$, which can help in identifying possible "hidden" failure risks and support system maintenance prioritization.


Keywords Water resources resilience $\cdot$ Digital twins $\cdot$ Failure modes $\cdot$ System dynamics model

[^0][^1]
[^0]:    Highlights

    - A novel method is proposed to simulate common failure situations for dam and reservoir systems.
    - A fuzzy-logic-based failure simulator uses hazard severity and system reliability as input.
    - The failure simulator provides failure magnitudes on a normalized scale.
    - The failure simulator is coupled with an SD model using a novel failure implementation framework.
    - The failure simulator coupled with an SD model provides a universal simulation tool applicable to any DRS.

[^1]:    Extended author information available on the last page of the article

# 1 Introduction 

In many areas of the world, dams and impounding reservoirs play a significant role in the management of water resources. Reliable management of these systems strongly depends on the capacity and operation of dam and reservoir systems (DRS) (DeNeale et al. 2019). An increasing trend in energy demand along with the energy transition, population growth, the everchanging climate conditions, global market fluctuations and other natural and anthropogenic impacts, put additional pressure on DRSs, leading to a reduction in performance reliability and safety (Gleick 2000; Winz et al. 2009; Chernet et al. 2014; Li et al. 2019; Đorđević et al. 2020; Badr et al. 2021). These impacts, combined with ageing infrastructure, often result in operational drift outside design criteria, into so-called adverse operating conditions. Since natural and anthropogenic impacts (disturbances) are dynamic and stochastic in nature, difficulties arise in the prediction and estimation of plausible dangerous scenarios. Furthermore, there is often no practical way to redesign or upgrade existing DRSs to allow safe mitigation of a potential multitude of unfavourable, worst-case scenarios. Therefore, DRS management must "steer" the system operation toward the narrow space to meet the ever-growing demands while avoiding water shortages, flooding (Bhadra et al. 2015), and dam safety risks. Asset owners and stakeholders need to be prepared to absorb certain risks due to (complete/partial) failure of the system's components. They also need to adapt the system configuration and operation to minimize (or even eliminate) potential losses and recover the full DRS capacity. To analyze the system performance and enable the system to withstand and bounce back from adverse operating conditions DRS operators have to assess the system's reduced performance under various what-if scenarios (Srivastava 2013; Delgado-Hernández et al. 2014; Morales-Nápoles et al. 2014; DeNeale et al. 2019; King et al. 2019).

System analysis, in general, is performed using physical or mathematical models via model experiments. Performing experiments on DRS full-scale or prototype physical models, to evaluate various what-if scenarios, is impractical due to limited capacity, safety and economic reasons. Thus, theoretical and/or empirical methods are the only viable solutions to assess the system's performance in adverse operating conditions. For example, widely used empirical methods in the industry for the evaluation of DRS failure modes are Failure Modes and Effects Analysis - FMEA, Fault Tree Analysis - FTA, Event Tree Analysis - ETA and Partitioning Multiobjective Risk Method - PMRM (Haimes et al. 1988; Hartford and Baecher 2004; Baecher et al. 2013). These methods use inductive reasoning for identifying the potential failures of the system based on previous experience with the system or similar cases, i.e., using expert knowledge. Even though these methods can provide essential information about the DRS failure modes they are unable to deal with component interactions, cascading events and nonlinearity in the system's behavior (Hartford and Baecher 2004; Regan 2010; Leveson 2011; Thomas 2013; King et al. 2019). Nowadays, novel digital technologies, such as digital twins (DT), as a new paradigm in simulation, provide tools capable of solving different issues in the water sector (Seshan et al. 2020; Alzamora et al. 2021; Bartos and Kerkez 2021; Savić, 2022). DT can facilitate a comprehensive analysis of the DRSs' behavior in adverse operating conditions using the system dynamics (SD) modelling approach (Regan 2010; Simonovic and Arunkumar 2016; King et al. 2017; Stojkovic and Simonovic 2019; King 2020; Lee and Kang 2020; Simonovic 2020; Ignjatović et al. 2021; Momeni et al. 2021; Samadi-Foroushani et al. 2022) coupled with expert knowledge. Here, complex, multipurpose DRSs, are represented using the SD model mimicking physical and non-physical components' performance and their interaction.

Utilization of the SD models within digital twins is of great importance due to their flexibility, mainly in terms of allowing the variation of the input parameters, system structure, boundary and initial conditions to simulate different what-if scenarios. Hence, DTs, including the SD models and real-world monitored data, should be utilized for analyzing the behavior and improving the performance of the DRSs in adverse operating conditions. Such an approach relies on the adequate representation of the disturbances, their impact on the components and nonlinear component interactions (Ivetić et al. 2022).

When a DRS digital twin is used to analyze the system behavior under adverse operating conditions, particular attention should be paid to generating plausible disturbances and implementing failure modes in the SD model. The current state of practice suggests creating a DRS failure database (i.e., the operating state database) using a Cartesian product of all the potential operating states (Patev and Putcha 2005; Cleary et al. 2015; King et al. 2019; Ardeshirtanha and Sharafati 2020; King and Simonovic 2020; Badr et al. 2021). In this approach, a failure (presented as a sample from the operating state database) is randomly chosen and coupled with the SD model to evaluate its impact on system performance. That helps decision makers to identify the riskiest subsystems (which subsystem's failure will have the biggest impact on system performance). However, this failure implementation procedure is time consumig and has to be modified for each case study as there could be different types of subsystems for different case studies. Furthermore, that approach can overlook a possible failure occurrence and shift the focus from truly failureexposed subsystems (those subsystems with lower impact on overall system performance, but with higher failure consequence due to its bad condition). Finally, that approach is unable to identify the chain of critical events that can cause the failure.

When there is a necessity to evaluate the true failure risks, and improve investment prioritization accordingly, hazards leading to the failures have to be considered (UNDRR 2020). Hazards occurrence probabilities and severities have to be combined with the system component's reliability (e.g., to represent ageing infrastructure) to evaluate failure risks. Hence, this paper presents a novel failure simulator where the failure magnitude is used to quantify the system component's (i.e., subsystem) failure. It is evaluated using fuzzy logic (Zadeh 1975) as a commonly used approach to evaluate engineering systems' performance (Nabipour et al. 2020; Jeon and Paek 2021; Zayed et al. 2021). The approach considers hazard's severity and subsystem's reliability as the input variables to the fuzzylogic system. Fuzzy logic has already been used for the description of the failure modes, but the applications were site-specific or focused only on dam safety problems (Kutlu and Ekmekçioğlu 2012; Patricio et al. 2012; Singh and Sarkar 2017; Fu et al. 2018; Yang et al. 2020; Ribas et al. 2021; Zhu et al. 2021; Sang et al. 2022). Here, a general fuzzy logicbased simulator is developed to generate failure magnitude values on a universal ( $0-1$ ) scale (applicable to any DRS). This new SD model builds on the previous work (Ignjatović et al. 2021; Ivetić et al. 2022) and completes the holistic framework by implementing the new failure generation model. In this approach, failure magnitude assessment is implemented in the SD model using the functionality indicator. By utilizing the functionality indicator, failures (generated using the novel fuzzy logic failure simulator) can be represented in a time series format (values in the range from 0 to 1 ), showing the percentage of functionality loss for each subsystem. Thus, it represents a powerful simulation tool used with DRS digital twins capable of creating a wide range of realistic adverse operating conditions. Supported by the expert knowledge at the initial stage of application (to define potential hazards and estimate the reliability drop rate for each subsystem), it enables better insight into the failure mechanisms and helps with system maintenance prioritization.

# 2 Materials and Methods 

### 2.1 Fuzzy Logic-based Failure Generator - Overview

To analyze DRS adverse operating conditions, a digital twin can be created using the following elements: hazard database, subsystems database, failure generator, system dynamics model and performance evaluator. In this research, particular focus is placed on disturbance modelling within the DRS digital twin, where a causal approach to generate failure magnitudes for DRS' subsystems is used (Fig. 1). The failure magnitude estimation procedure can be divided into the following steps: (1) hazard sampling, (2) identification of the affected subsystems, and (3) failure magnitude evaluation. At each time step of the analysis, the
![img-0.jpeg](img-0.jpeg)

Fig. 1 Causal failure modelling approach - schematic overview

procedure is re-initiated. In step (1) of the failure generator, a single hazard is selected from the predefined list, using a probabilistic selection. Expert knowledge is used to determine the list of plausible hazards and assign their estimated occurrence probability. A single hazard for a certain time step is sampled using a fitness proportionate selection, i.e., roulette wheel selection (Fig. 1). For the selected hazard, in step (2), a list of directly affected DRS subsystems is provided, using prior knowledge obtained from various sources, e.g., site operators' experience, detailed modelling, and literature. Lastly, in step (3), the failure magnitude is determined for each affected subsystem. Failure magnitude is evaluated using the fuzzy logic-based method. The inputs in the fuzzy logic failure generator are hazard severity and subsystem's reliability, which are evaluated using the data from the subsystems database. A detailed explanation of each failure generator step is presented in the following subsections.

# 2.2 Hazard Generator and Detection of Affected DRS Components 

Generating realistic DRS failure modes within the digital twin requires a reliable database containing information about potential hazards. Initially, expert knowledge from the operators, management and literature should be utilized to formulate the hazard database, linking them to the potentially affected subsystems (Fig. 2).

The first step in applying the failure simulator is to sample a single hazard from the entire list. Even though hazards can be selected randomly, this paper uses non-uniform probabilistic selection to better represent the stochastic nature of potential hazards. The hazard database (used in this research) contains the following attributes used to select a hazard during a simulation:
$F_{i}$ - occurrence probability for each hazard, where $I$ denotes $i$-th hazard.
$S_{i}$ - hazard severity estimated using the custom-made severity scale. Larger values of severity are correlated with a lower probability of occurrence and vice versa.

Hazard severity scales are widely used to describe the devastation potential of hazard events. Recently, efforts have been made to create a uniform, hazard severity scale (Wang and Sebastian 2021). It works with natural hazards by analysing historical events. However, water systems are also affected by anthropogenic hazards. Due to a lack of uniform hazard severity scales (both natural and human-induced), a custom-made scale is used in this work.

Besides $F_{i}$ and $S_{i}$ variables, each hazard contains a list of potentially affected DRS' subsystems. This attribute is assessed using historical data if there are documented historical failures, and/or detailed numerical and theoretical analyses of the DRSs behavior (Rehamnia et al. 2020; Chen et al. 2021; Rakić et al. 2022; Nafchi et al. 2021a, b; Tang et al. 2022). It should be noted that the hazard database contains an event to describe normal conditions (no hazard), which has the highest occurrence probability. The hazard database in this work is created using only single hazards. Because a hazard is selected at each simulation time step, there is a possibility to create a chain of hazards within one timestep lag. Considering that the simulation time step (e.g., hourly) is significantly shorter than the time scale used to analyze DRS behavior (e.g., several years), it can be assumed that the chain of hazards with associated lags can be used to represent multiple hazards occurring at the same time. When larger time steps are used, e.g., days, in similar time scales, the combination of single events (e.g. Cartesian product) should complement the hazards list, where the occurrence probability is estimated by multiplying single events' occurrence probabilities.

At each simulation time step, the roulette wheel (Blickle and Thiele 1996)selects the hazard, where the occurrence probability $F_{i}$ transforms into the roulette selection

Hazards database
![img-1.jpeg](img-1.jpeg)

Fig. 2 Probabilistic hazard generator using the example of the DRS's digital twin hazards database
probability. The hazard selection could be conducted using different sampling techniques (e.g. tournament selection) but it would go beyond the objectives of this paper. Analyzing the effects of different sampling methods could be a subject of separate research.

When a hazard is sampled, severity $S_{i}$ and the list of the affected subsystems is used as an output from this stage (step (2) in Fig. 1). This data is used in the failure magnitude estimation block (step (3) in Fig. 1).

# 2.3 Subsystems Failure Magnitude Evaluation 

### 2.3.1 Reliability Evaluation for the Affected DRS Subsystems

When the affected subsystems are detected, the failure magnitude and failure duration for each affected subsystem are determined. To complete this task, DRS subsystem reliability has to be estimated using the subsystems database (Fig. 3).

The DRS subsystem reliability database (used in this work) has the following attributes:
$\alpha_{j}$ - current functionality level of the subsystem [0-1], where $j$ denotes $j$-th subsystem, described using the following expression:

$$
\alpha=\left[\begin{array}{cc}
1, & \text { subsystem in usual operation }- \text { full functionality } \\
0<\alpha<1, & \text { subsystem is in the failure mode }- \text { partial functionality } \\
0, & \text { subsystem is in the failure mode }- \text { non functional }
\end{array}\right]
$$

![img-2.jpeg](img-2.jpeg)

Fig. 3 Failure magnitude estimation using the DRS subsystem reliability database
$L R D_{j} \quad$ last repair date (variable updated during the simulation)
$L F D_{j} \quad$ last failure date (variable updated during the simulation)
$\lambda_{j}[/]$ cumulative density function shape parameter (used to estimate subsystem's current reliability)
$k_{j}$ cumulative density function scale parameter (used to estimate subsystem's current reliability)
$t_{\text {repair,j }} \quad$ expected repair time in days
$t_{\text {proc,j }} \quad$ expected procurement time in days (used to simulate time required to identify the failure and collect all resources for subsystem repair)

These variables are used during a simulation to evaluate the current reliability level $R(t)[0-1]$ for each affected subsystem. Here, reliability is adopted as a common engineering metric to quantify the current state of the system. It should be mentioned that other mathematical methods (e.g. vulnerability) could be used instead, but the effects of choosing the mathematical method to describe subsystems' state should be analyzed in separate research.

Unlike in the static reliability assessment (Kjeldsen and Rosbjerg 2004), continuous evaluation of the subsystems' reliability is performed here. To assess this variable for each subsystem during a simulation (at each simulation time step), an exponential reliability

function is used (Calixto 2016). Before the reliability is estimated, the current functionality for each affected subsystem is checked. First, there is a possibility that some of the affected subsystems are already in a failure mode (Eq. (1)). For the subsystems in a failure mode (partial functionality), current functionality $\alpha_{j}(t)$ has to be checked and updated. If aggregated procurement and repair times are equal to the difference between current and the time since the last failure date $\left(t_{\text {repair }, j}+t_{\text {proc }, j}=t-L F D_{j}\right)$, the current functionality of the subsystem is fully restored, i.e., equal to 1 . If the current functionality of a subsystem is 0 , it means that the subsystem is still non-functional and should be removed from the affected subsystems list.

For each affected subsystem (those fully or partially functional), reliability $R_{j}(t)$ is evaluated using the customized exponential reliability equation:

$$
R_{j}(t)=\alpha_{j}(t) \cdot e^{-\left(\frac{t-L R D_{j}}{\lambda_{j}}\right)^{k_{j}}}
$$

where $t$ represents simulation time. This equation assumes that the reliability of $j$-th subsystem is 1 at the moment when the repair process is finished. The reliability exponentially decreases with time passing from the last repair. The reliability decrease rate depends on parameters $\lambda_{j}$ and $k_{j}$, which have to be estimated using expert knowledge and historical failure data. As more information regarding the functionality of a particular subsystem is obtained, these parameters should be updated during the DRS lifetime. In this work, the values of parameters $\lambda_{j}$ and $k_{j}$ are selected to demonstrate the failure generation methodology. Additionally, it is assumed that the reliability of the subsystems in partial failure mode decreases more rapidly than in fully functional mode. Therefore, the exponential representation of the reliability is multiplied by the current value of the subsystems' functionality value (Eq. (2)). When the reliability $R_{j}(t)$ is evaluated for each affected subsystem, the next step is to determine the failure magnitude.

# 2.3.2 Evaluation of the DRS Component's Failure Magnitude 

Failure magnitude, for each affected subsystem, $\beta_{j}$ takes a value between 0 and 1 , where 0 means that there is no failure while 1 represents the maximum failure magnitude leading to the complete subsystem failure $\left(\alpha_{j}=0\right)$. The failure magnitude describes the lost value of the current subsystem's functionality $\alpha_{j}(t)$ caused by the generated failure (i.e., the percentage of the current functionality that will be reduced by the failure). When the failure magnitude is estimated, the new value of the current functionality level is calculated using the following equation:

$$
\alpha_{j}(t+\Delta t)=\alpha_{j}(t) \cdot\left(1-\beta_{j}\right)
$$

where $\Delta t$ denotes the simulation time step.
In this approach, the failure magnitude is estimated using the fuzzy logic approach, where the process involves formulating the mapping from a given input to an output using fuzzy logic. Even though this task could be done using some other approach, fuzzy logic has been adopted due to its ability to group many input numerical values into categories and create simple IF-THEN rules using the "natural language". The most common approach for fuzzy logic applications is the Mamdani rule-based fuzzy inference system (Mamdani 1974). In this approach the following steps have to be conducted (Fig. 4):

![img-3.jpeg](img-3.jpeg)

Fig. 4 Estimation of the failure magnitude using the fuzzy logic-based generator

- Fuzzification - where all input variable (crisp) values are transformed into their fuzzy counterparts,
- Inference - where fuzzified input is transformed into fuzzified output using logical (IFTHEN) rules, and
- Defuzzification - where fuzzy output is transformed into crisp (number) values.

The first step in fuzzy system implementation is to apply fuzzification to transform hazard severity $S_{i}$ into fuzzy sets using the "natural language" approach. The custom-made severity scale used in this work assigns a severity value in the range between 0 and 10 to each hazard. To represent this scale in "natural language", those values are transformed into fuzzy sets using the membership functions: mild, moderate or extreme (Fig. 5a). It practically means that each hazard, according to the assigned severity value cannot be unambiguously characterized as a mild, moderate or extreme event, since there is no clear

![img-4.jpeg](img-4.jpeg)

Fig. 5 a) Fuzzification of the hazard severity, b) Fuzzification of the subsystem's reliability and c) Fuzzification of the desired output (failure magnitude)
border between these categories. Therefore, fuzzy logic transforms the hazard severity (represented as a single number) into an array (Fig. 5a). The array size is equal to the number of membership functions. Each array element represents the value of the membership function for the given hazard severity. The membership function takes values between 0 and 1 . If a mild membership function has a value of 1 , for the selected hazard severity, the fuzzified value becomes $[1 ; 0 ; 0]$. If the hazard severity indicates 0.7 for the mild, 0.3 for the moderate and 0 for the extreme membership function, respectively, then the fuzzified value of severity becomes $[0.7 ; 0.3 ; 0]$.

Although the number of membership functions can vary, this work uses three membership functions to describe hazard severity. Values used to describe the membership functions were not obtained by analyzing real data, but were selected to illustrate the approach. For real-world applications, these values should be obtained using expert knowledge and/ or historical data and should be updated during the generator's exploitation phase if some of the failures occur.

The second step in the fuzzification process involves the transformation of reliability values (between 0 and 1) into a fuzzy set for each affected subsystem. Here, three membership functions are used: low, moderate and high (Fig. 5b). This fuzzy set can also be densified by adding additional membership functions (e.g., very low and very high) which can be the subject of separate analysis. In this research, three membership functions are used for demonstration purposes (Fig. 5b).

Once the input variables are fuzzified, membership functions are defined for the output fuzzification. The membership functions are then used to create an output value using the fuzzy rules. The expected output from the fuzzy logic-based failure generator is failure magnitude $\beta$ for each affected subsystem that takes values between 0 and 1 . Here, there are nine possible combinations for fuzzified inputs. To better differentiate

![img-5.jpeg](img-5.jpeg)

Fig. 6 IF-THEN rule set to estimate the fuzzified failure magnitude
the effects of some inputs' combinations, five membership functions are used for failure magnitude fuzzification: very high, high, moderate, low and very low (Fig. 5c). This means that single-value reliability is transformed into an array that contains five numbers, representing the values of the membership function. Failure magnitude fuzzification can also be densified using additional membership functions. The set of membership functions in this research is used only to demonstrate the methodology.

After the fuzzification is complete, the next step (inference) creates fuzzified output using the fuzzified input and custom-made rules. Here, simple IF-THEN rules are used (Rule set in Fig. 6). The rules use logical operators (AND, OR and NOT) for representation. However, AND, OR and NOT are Boolean operators using the truth/false input values often denoted by 1 or 0 . Fuzzy logic, however, assumes values between 0 and 1. Therefore, Boolean operators AND, OR and NOT, in fuzzy logic, are executed using the MIN, MAX and complement functions respectively (rules execution in Fig. 6).

Finally, when the fuzzy inference process is finished, defuzzification is conducted to get crisp values of the failure magnitudes based on the output fuzzy set. Here, defuzzification is conducted using the centroid method (Fig. 7). Defuzzification could be done using other methods, such as the center of area, the center of sums, the weighted average method or maxima methods. However, the centroid method is adopted here as the most frequently utilized approach. The rationale for the choice of the particular defuzzification method could

![img-6.jpeg](img-6.jpeg)

Fig. 7 Failure magnitude defuzzification using the centroid method
only be justified by separate analysis by comparing the results simulation results against historical (real-world) data.

When the failure magnitude has been evaluated, current functionality is updated for each affected subsystem (Eq. (3)). In the next simulation step the entire procedure is repeated. When the failure model run is finished, the final outputs from the simulation are functionality time series $\alpha(t)$ for each DRS' subsystem (Ivetić et al. 2022). The current functionality of the affected subsystem stays reduced while the resources needed for repair are being procured (procurement time $t_{\text {proc }}$ ). After the resources are procured, the subsystem's functionality drops to 0 because most of the subsystems have to be fully disconnected when the repair process begins. Until the repair is finished (repair time elapses), $\alpha(t)$ stays 0 . For those subsystems which do not require full disconnection, the repair time is set to 0 and the subsystem works with reduced functionality until the repair is completed (procurement + repair time).

# 2.4 DRS Pirot Case Study - System Dynamics Model and Failure Implementation 

The proposed failure generator and its implementation within the system dynamics model are tested on the Pirot DRS digital twin. Pirot DRS is located in the southeastern region of Serbia, near the city of Pirot. It is a multi-purpose reservoir system, currently primarily used for hydropower production and flood protection along the Nišava and Visočica rivers. The system also provides environmental flows (to preserve the downstream freshwater ecosystem) and sediment control at the watershed scale and it is planned to augment the water supply in the future. The Pirot DRS includes the following elements: Zavoj reservoir and dam, power tunnel, surge tank, penstock, hydropower plant (HPP), tail race (open channel for hydropower plant discharge) and compensation reservoir (Fig. 8). The compensation reservoir is located on the right bank of the Nišava river and is designed for HPP

discharge release attenuation. The system is presented in more detail in previous publications (Ignjatović et al. 2021; Ivetić et al. 2022; Rakić et al. 2022).

The system is decomposed in one of the many possible ways and the appropriate SD model is created (Fig. 8a) to demonstrate the failure generation methodology. Key subsystems are identified along with failure indication parameters for each subsystem (Table 1). Failure indication parameters are used to easily implement failure for each subsystem according to the failure implementation framework presented in previous research (Ivetić et al. 2022). For each subsystem, reliability parameters, $\lambda$ and $k$, are arbitrarily selected to demonstrate the effects of reliability decrease in failure magnitude Additionally, the last repair date in the subsystems database is also arbitrarily selected to mimic real-world situations where the existing systems are repaired occasionally, and not all subsystems at the same time. For realistic estimation of the subsystems' reliability, experts and operators in charge have to be consulted and a thorough analysis should be conducted to estimate reliability parameters (shape and scale parameters).

The system dynamics model and failure generator are implemented in the MATLAB programming environment (The MathWorks 2022). The mathematical expressions are integrated and used in each time step to calculate the changes in the state and operation of the system. Water balance in the Zavoj reservoir, with inflow from the Visočica river, $Q_{\text {visočica }}^{t}$ (Ignjatović et al. 2021) and HPP, environmental, overflow, seepage, evaporation and forest fire outflows are mathematically represented using the following balance equation:

$$
V_{z a v o j}^{t+\Delta t}=V_{z a v o j}^{t}+\Delta t \cdot\left(Q_{v i s o c ̌ i c a}^{t}-Q_{o u t, H P P}^{t}-Q_{e n v}^{t}-Q_{E}^{t}-Q_{o f}^{t}-Q_{i n f}^{t}-Q_{f f}^{t}-Q_{w d}^{t}\right)
$$

where $V_{z a v o j}^{t}\left(V_{z a v o j}^{t+\Delta t}\right)$ represents the Zavoj reservoir water volume at time $t(t+\Delta t)$, and $\Delta t$ represents the simulation time step $(\Delta t=1 \mathrm{~h})$. The reservoir water level, $Z_{z a v o j}^{t}$, is evaluated using a stage-storage curve (Fig. 8b). $Q_{e n v}^{t}$ represents the environmental flow (Eq. (5)), $Q_{E}^{t}$ is evaporation rate modelled using the input temperature time series (Linacre 1977), $Q_{f f}^{t}$ is the firefighting water extraction which is above 0 only when severe forest fire disturbance occurs while $Q_{w d}^{t}$ is the drinking water extraction. $Q_{e n v}^{t}, Q_{f f}^{t}$ and $Q_{w d}^{t}$ are represented using the following equations:

$$
\begin{gathered}
Q_{e n v}^{t}=\alpha_{e n v}^{t} \cdot Q_{e n v, \text { required }} \\
Q_{f f}^{t}=\left(1-\alpha_{f f}^{t}\right) \cdot Q_{f f, \max } \\
Q_{w d}^{t}=\alpha_{w d}^{t} \cdot Q_{w d, \text { required }}-\left(1-\alpha_{w d, \text { leak }}^{t}\right) \cdot Q_{\text {leak,max }}
\end{gathered}
$$

In Eqs. (5), (6) and (7) the following variables are used:
$\alpha_{e n v}^{t}, \alpha_{f f}^{t}, \alpha_{w d}^{t}, \alpha_{w d, \text { leak }}^{t}[/]$ functionality indicators for environmental, firefighting, water supply demand and water supply leakage subsystems respectively,
$Q_{\text {env,required }}\left[\mathrm{m}^{3} / \mathrm{s}\right]$ required (minimum) environmental flow, $Q_{\text {env,required }}$ is $0.4 \mathrm{~m}^{3} / \mathrm{s}$
$Q_{f f, \text { max }}\left[\mathrm{m}^{3} / \mathrm{s}\right] \quad$ maximum flow used for firefighting $Q_{f f, \text { max }}$ is $0.2 \mathrm{~m}^{3} / \mathrm{s}$
$Q_{w d, \text { required }}\left[\mathrm{m}^{3} / \mathrm{s}\right] \quad$ required water supply flow rate $Q_{w d, \text { required }}$ is $0.15 \mathrm{~m}^{3} / \mathrm{s}$

![img-7.jpeg](img-7.jpeg)

Fig. 8 a) Conceptualization of the decomposed DRS Pirot with interdependency links between subsystems (Ivetić et al. 2022), b) stage-storage curve for the Zavoj reservoir, c) the stage-storage curve for the compensation reservoir and $\mathbf{d})$ the rating curve at the Nisava control point
$Q_{\text {leak,max }}\left[\mathrm{m}^{3} / \mathrm{s}\right] \quad$ max value for leakage in water supply subsystem $Q_{\text {leak,max }}$ is $0.1 \mathrm{~m}^{3} / \mathrm{s}$
Water transport towards the HPP is represented by reservoir outflow $Q_{\text {out,HPP }}^{t}$ using the following equation:

$$
Q_{\text {out }, H P P}^{t}=\underbrace{H P P, O P^{t} \cdot \alpha_{\text {HPP }}^{t} \cdot Q_{\text {HPP, capacity }}}_{Q_{\text {HPP }}^{t}}+\left(1-\alpha_{\text {pen.leak. }}^{t}\right) \cdot Q_{\text {pen.leak. }}^{t}
$$

![img-8.jpeg](img-8.jpeg)
1167

where $H P P, O P^{t}$ is a binary operator determining the command to operate or stand by, $\alpha_{H P P}^{t}$ is the failure indicator used to demonstrate failure potential for turbine operation (e.g., one turbine operational, other non-operational due to the main inlet valve failure $\alpha_{H P P}^{t}=0.5$ ), $Q_{\text {HPP, capacity }}$ is the total HPP capacity (set at $45 \mathrm{~m}^{3} / \mathrm{s}$ ), $\alpha_{\text {pen,leak. }}^{t}$ is the penstock leakage failure indicator and $Q_{\text {pen,leak. }}^{t}$ is the estimated maximum value of leakage set at $1 \mathrm{~m}^{3} / \mathrm{s}$. For the analysis presented here, only penstock leakage is considered (including leakage at the penstock and main inlet valve), although power tunnel leakage is also possible.

HPP discharge $Q_{\text {out,HPP }}^{t}$ flow into the compensation reservoir or directly into the Nišava river, depending on the water level in the compensation reservoir. This reservoir is used for discharge attenuation of the $Q_{\text {out,HPP }}^{t}$ between two successive HPP operation runs. Water volume in the compensation reservoir is evaluated using the following balance equation:

$$
V_{\text {comp,res }}^{t+\Delta t}=V_{\text {comp,res }}^{t}+\Delta t \cdot\left(Q_{\text {comp,in }}^{t}-Q_{\text {comp,out }}^{t}\right)
$$

where $V_{\text {comp,res }}^{t}\left(V_{\text {comp,res }}^{t+\Delta t}\right)$ represents compensation reservoir water volume at time $t(t+\Delta t)$. $Q_{\text {comp,in }}^{t}$ represents compensation reservoir inflow (Eq. (10)), $Q_{\text {comp,out }}^{t}$ represents compensation reservoir outflow (Eq. (12)) and $Z_{\text {comp,res }}^{t}$ represents the water level in the compensation reservoir evaluated using the stage-storage curve (Fig. 8c).

$$
\begin{gathered}
Q_{\text {comp,in }}^{t}=\left\{\begin{array}{cc}
0, & Z_{\text {comp,res }}^{t} \geq Z_{\text {comp,res }}^{\max } \\
Q_{\text {out,HPP }}^{t} & Z_{\text {comp,res }}^{t}<Z_{\text {comp,res }}^{\max }
\end{array}\right\} \\
Q_{\text {comp,out }}^{t}=\left\{\begin{array}{cc}
Q_{\text {out,HPP }}^{t} \cdot \frac{t_{\text {hpp }}}{24 h}, & Z_{\text {comp,res }}^{t} \geq Z_{\text {comp,res }}^{\max } \\
0 & Z_{\text {comp,res }}^{t}<Z_{\text {comp,res }}^{\max }
\end{array}\right\}
\end{gathered}
$$

In Eqs. (10) and (11) $Z_{\text {comp,res }}^{\max }$ represents the maximum water level in the compensation reservoir while $t_{\text {hpp }}$ represents the period in which HPP was active and it is determined using the 1-point discrete hedging rule (Tayebiyan et al. 2019).

If the inflow into the compensation reservoir is disabled, the total Zavoj reservoir outflow (towards HPP) is directly discharged into the Nišava river (Eq. (12)). Finally, the Nišava flow, downstream of HPP outlet $Q_{\text {nisava,ds }}^{t}$, is calculated by Eq. (13):

$$
\begin{gathered}
Q_{\text {hpp,nisava }}^{t}=Q_{\text {out,HPP }}^{t}-Q_{\text {comp,in }}^{t} \\
Q_{\text {nisava,ds }}^{t}=Q_{\text {hpp,nisava }}^{t}+Q_{\text {comp,out }}^{t}+Q_{\text {nisava }}^{t}
\end{gathered}
$$

where $Q_{\text {hpp,nisava }}^{t}$ represents HPP discharge directly to Nišava river and $Q_{\text {nisava }}^{t}$ represents natural flow in Nišava upstream of the HPP outlet. The Nišava River water level at the control point $Z_{\text {nisava }}^{t}$ is evaluated using the rating curve (Fig. 11d).

Spillway overflow $Q_{o f}$ is represented by the following equation:

$$
Q_{o f}^{t}=C_{Q} \cdot \alpha_{B}^{t} \cdot B \cdot \sqrt{2 \cdot g \cdot\left(Z_{z \text { avoj }}^{t}-Z_{s}\right)^{3}}
$$

where the following variables are used:
$C_{Q}[/]$ overflow coefficient set at 0.42 ,

$B[\mathrm{~m}] \quad$ crest length set at $27 \mathrm{~m}(3 \times 9 \mathrm{~m})$,
$g\left[\mathrm{~m} / \mathrm{s}^{2}\right] \quad$ acceleration due to gravity,
$Z_{S}[\mathrm{~m}] \quad$ spillway crest level $(615 \mathrm{~m})$,
$\alpha_{B}[/]$ functionality indicator used to simulate failure of the spillway by decreasing the crest length

Seepage (infiltration) rate $Q_{\text {inf }}$ is represented using the following equation:

$$
Q_{\text {inf }}^{t}=\frac{K}{\alpha_{K}^{t}} \cdot\left(Z_{\text {zavoj }}^{t}\right)^{x}
$$

where seepage coefficient $K$ is set at $3.85 \mathrm{e}-06$ and seepage exponent is set at $x=2$. The seepage coefficient is identified as the failure indication parameter (dam body damage can increase the seepage coefficient value). Hence, the seepage coefficient is multiplied by the failure function $f(\alpha)=1 / \alpha_{k}$ to introduce failure potential.

Power generated by the turbines $P_{\text {HPP }}^{t}$ at a specific time is evaluated using the following equations:

$$
\begin{gathered}
H_{T}^{t}=Z_{\text {zavoj }}^{t}-Z_{\text {tr,HPP }}^{t}-\frac{8 \cdot \lambda_{\text {tun }} \cdot L_{\text {tun }}}{\left(\alpha_{D, \text { tun }}^{t} \cdot D_{\text {tun }}\right)^{2} \cdot \pi^{2}} \cdot Q_{\text {out,HPP }}^{t^{2}} \cdot \frac{8 \cdot \lambda_{\text {pen }} \cdot L_{\text {pen }}}{\left(\alpha_{D, \text { pen }}^{t} \cdot D_{\text {pen }}\right)^{5} \cdot \pi^{2}} \cdot\left(\frac{Q_{\text {out,HPP }}^{t}}{2}\right)^{2} \\
P_{\text {HPP }}^{t}=\alpha_{\text {el,net. }}^{t} \cdot \underbrace{\eta_{T} \cdot \rho \cdot g \cdot Q_{\text {HPP }}^{t} \cdot H_{T}^{t}}_{P_{\text {cap,HPP }}^{t}}
\end{gathered}
$$

where the $H_{T}^{t}$ is the turbine net head ( 0 if the functionality indicator for tunnel or penstock is 0 ), $Z_{\text {tr,HPP }}^{t}$ is the water level at the tailrace, and the values with subscript tun and pen are related to the power tunnel and penstock, respectively. The $P_{\text {HPP }}^{t}$ is generated power at the powerhouse, $P_{\text {cap,HPP }}^{t}$ is the max power of the plant ( 80 MW ) and $\alpha_{\text {el,net }}^{t}$ is the functionality indicator used to model the disconnection of the HPP from the grid. Furthermore, two water level monitoring systems are modelled as shown in Eq. (18). The first one is considering the Zavoj level measurements and is used as one of the process variables for the control of the $Q_{\text {HPP }}^{t}$, and the second is the Nišava river water level measurements at the Hydrological station Pirot, also used as a process variable for the outflow control. Since the water level sensors are identified as an important subsystem, the following equation is used to model this subsystem:

$$
Z_{\text {sensor }, i}^{t}=Z_{i}^{t}+\frac{\operatorname{rand}() \cdot \Delta Z_{\text {noise }}}{\alpha_{\text {noise }}^{t}}+\left(1-\alpha_{\text {drift }}^{t}\right) \Delta Z_{\text {drift }}
$$

where $Z_{i}$ is reservoir water level obtained by the SD model ( $i=$ zavoj for Zavoj water level and $i=$ nisava for Nišava water level), $\Delta Z_{\text {noise }}$ represents noise amplitude, $\Delta Z_{\text {drift }}$ represents the sensor's zero drift, and $\operatorname{rand}()$ should be used to generate a random number between -1 and 1 . Finally, $Z_{\text {sensor }, i}$ is used to simulate the water level sensor output used in the control unit. Here, $\alpha_{\text {noise }}$ denotes functionality indicator considering noise while $\alpha_{\text {drift }}$ represents

functionality indicating the sensor zero drift. In this case study $\Delta Z_{\text {noise }}$ and $\Delta Z_{\text {drift }}$ are set to 0.2 and 0.5 , respectively.

Sensor water levels at the Zavoj reservoir and Nišava control point together with $t_{h p p}$ (obtained from the hedging rule) are used to determine whether the HPP will operate. The HPP is disconnected (i.e., not operating, $H P P, O P^{t}=0$ ) if the following conditions are met: Zavoj reservoir water level is below the minimum working level, Nišava water level is above the maximum water level at the control point or HPP working hours are exceeding the suggested working hours $t_{h p p}$. Otherwise, HPP is active $\left(H P P, O P^{t}=1\right)$.

In this work, global crises (e.g., covid-19 pandemic, financial crisis, conventional and economic wars, etc.) are also considered potential hazards. Therefore, the maintenance unit is identified as the failure-prone subsystem due to the global crisis. In that case, the repair time $t_{\text {repair }}$ and procurement time $t_{\text {proc }}$ are used to represent the effects of such an event. These failure indication parameters for the maintenance unit affect all other subsystems and they are modelled using the following equations:

$$
\begin{aligned}
t_{\text {repair }} & =\frac{t_{\text {repair,exp }}}{\alpha_{\text {repair }}} \\
t_{\text {proc }} & =\frac{t_{\text {proc,exp }}}{\alpha_{\text {proc }}}
\end{aligned}
$$

where $t_{\text {repair,exp }}$ is the expected repair time (when there are no global crisis events, presented in Table 1), $t_{\text {repair,exp }}$ is the expected procurement time necessary to gather all the resources for repairing a subsystem, $\alpha_{\text {repair }}$ is a functionality indicator for repair and $\alpha_{\text {proc }}$ is a functionality indicator for procurement.

To demonstrate the proposed failure generator an example of a hazards database is also presented (Table 2).

Occurrence probability $F$ for each hazard should be estimated using historical data (e.g. Keller et al. 1992) for natural hazards. To demonstrate the new methodology, assumed return periods were used since there is no data available to estimate the return periods of the human-induced hazards. Return periods are given in years (Table 2). However, the failure generator is started at each simulation time step (hourly) and hazard probability has to be adjusted accordingly. In this case, hazard probability in failure generator simulation is given as $F=1 / T / 365 / 24[1 /$ hour $]$.

Finally, to evaluate DRS's response to the created input scenario, an appropriate system performance indicator has to be evaluated. This indicator needs to address all the objectives used for DRS system management. Here, some of the common objectives related to the DRS operation are included: maximising hydropower generation, providing flood protection, meeting water supply needs and preserving environmental flows in the river. A single performance indicator can be used for assessing each objective separately, but for complex, multipurpose systems overall performance has to be evaluated, taking all of the objectives into account. Hence, the system performance indicators are used to evaluate each of the objectives (Eqs. (21)-(24)) and then to combine them into a single, overall performance indicator (Eq. (25)).

$$
P_{e n v}^{t}=\min \left(1, \frac{Q_{e n v}^{t}+Q_{o f}^{t}}{Q_{e n v, \text { required }}}\right)
$$

Table 2 An example of a hazard database for Pirot DRS


$$
\begin{gathered}
P_{\text {flood }}^{t}=\left\{\begin{array}{cc}
1 & Z_{\text {sensor,nisava }}^{t} \leq Z_{\text {nis,rf }} \\
1-\frac{Z_{\text {sensor,nisava }}^{t}-Z_{\text {nis,rf }}}{Z_{\text {nis,rf }}-Z_{\text {nis,rf }}} & Z_{\text {nis,rf }}<Z_{\text {sensor,nisava }}^{t}<Z_{\text {nis,rf }} \\
0 & Z_{\text {sensor,nisava }}^{t} \geq Z_{\text {nis,rf }}
\end{array}\right\} \\
P_{w d}^{t}=\frac{Q_{w d}^{t}}{Q_{w d, \text { required }}} \\
P_{\text {power }}^{t}=\frac{P_{\text {HPP }}^{t}}{P_{\text {cap,ipp }}} \\
P_{\text {system }}^{t}=\frac{P_{\text {env }}^{t}+P_{\text {flood }}^{t}+P_{w d}^{t}+P_{\text {power }}^{t}}{4}
\end{gathered}
$$

$P_{\text {env }}^{t}$ represents the current performance indicator of the system considering environmental criteria downstream of the Zavoj reservoir. If $P_{\text {bio }}^{t}=1$ it means that the system meets completely the environmental criteria and $P_{\text {env }}^{t}=0$ means that the system failed (did not release any water) to meet this objective. $P_{\text {flood }}^{t}$ represents a performance indicator that considers flood protection criteria at the Nišava control point. If the $Z_{\text {sensor,nisava }}^{t}$ is below the flood defence water level $Z_{\text {nis,rf }}$ then $P_{\text {flood }}^{t}$ is 1 . When $Z_{\text {sensor,nisava }}^{t}$ is above $Z_{\text {nis,rf }}$ and below emergency flood defence level $Z_{\text {nis,ef }}$ then $P_{\text {flood }}^{t}$ is between 0 and 1 . When the water level at the Nišava control point reaches or exceeds the emergency flood protection level it means that the system failed to meet the flood protection objective and the indicator is 0 . $P_{\text {wd }}^{t}$ represents the current performance indicator considering the water supply criterion. If $P_{w d}^{t}=1$ it means that the system completely meets the water supply demand and $P_{w d}^{t}=0$ means that the system failed to meet this requirement. If the $P_{w d}^{t}$ takes the value between 0 and 1 it means that the system partially meets the demand (same for all other performance indicators). $P_{\text {power }}^{t}$ represents the performance indicator for power generated at the HPP. When the hydropower plant is working $\left(H P P, O P^{t}=1\right)$ power functionality indicator is evaluated by comparing the actual power generated with the HPP's capacity $P_{\text {cap,HPP }}$ (Eq. (24)). When the HPP is deactivated $\left(H P P, O P^{t}=0\right)$ power functionality indicator takes the last value when HPP was active. Finally, all performance indicators are integrated into the overall performance indicator $P_{\text {system }}^{t}$ which also varies between 0 and 1 (Eq. (25)).

When the simulation is finished, and system performance indicators are estimated, statistical analysis of the simulation results should be conducted. This can be a useful decision support tool for the operators in charge of investment prioritization and reduction of failure risks. For example, the total number of failures, min, max or mean value of the failure magnitudes for each subsystem and accompanying system performance drop can be useful for the initial assessment of the failure potential for each subsystem. However, it should be noted that many system performance drops could be induced by a chain of failures (several subsystems at once, depending on the generated hazard and its targeted subsystems). In that case, the number of simultaneous failures (the number of subsystems that sustained a failure at the same time), which led to a performance drop, has to be considered. To determine the damage potential for each subsystem during the simulation, the sum of performance drops and the number of joint failures should be used, as proposed in the following equation:

$$
D P_{j}=\sum_{i}^{N_{b a z}} \frac{\Delta P_{\text {system }, i}}{N_{\text {joint }, i}}
$$

where $D P_{j}$ represents damage potential for the $j$-th subsystem, $\Delta P_{\text {system }, i}$ represents system performance indicator drop induced by a $i$-th hazard which affects the $j$-th subsystem. The number of joint failures, for the $i$-th hazard is represented by $N_{\text {joint }, i}$ and $N_{\text {haz }}$ represents the total number of (generated) hazards affecting the $j$-th subsystem.

# 3 Results and Discussion 

To demonstrate the application of the fuzzy logic-based failure generator in assessing the system's performance in adverse operating conditions, a simulation of 10 years period is performed starting on 1st January 2022 at 12 AM (simulation starting day is used for initial evaluation of the subsystems' reliability based on the last repair date from Table 1). Hydrological model driving input is created using the historical hydrometeorological data (Visočica and Nišava rivers flow hydrographs) and air temperature time series for estimation of the evaporation rate (Fig. 9a). As the focal point of this analysis, the disturbance part of the input scenario (adverse operating conditions) is implemented in the form of functionality indicator time series for each subsystem (Fig. 9b-e). These functionality indicator time series are created using the proposed fuzzy logic-based failure generator. In this test case, hazards are selected during the simulation using the roulette wheel selection. This selection method provides more frequent occurrences of low-severity hazards (Fig. 10a).

Using the created input scenario, a system dynamics simulation is performed. The system's performance is evaluated using single and overall performance indicators (Fig. 10b, c) based on the system dynamics simulation results.

When hazards, sampled by the roulette wheel selection, are analyzed, it can be noticed that the system was operating under no-hazard conditions for more than $97 \%$ of the simulation period (Fig. 11a). In the remaining period of the simulation (approximately 3\% of the simulation period) hazards occurred but there was no hazard with a severity value above 6. This happens due to the return period for some of the hazards in the database (Table 2) being much longer than the simulation period thus reducing the probability of high-severity hazard occurrence. Extending the simulation period could increase the number of occurrences for the extremely high-severity hazards.

Even though hazards are generated sporadically during the simulation (less than 3\% of the hazard samples in roulette wheel selection are real hazards) and most of them are low-severity, they induced the subsystems' failures with significant effect system performance. For example, failure magnitudes and failure durations forced the system to underperform (single and overall performance indicators below 1) for a significant part of the simulation period, even though there were no extreme hazards during the simulation. The single performance indicators duration curves (Fig. 11b) show that the system met the expected performance level for more than $75 \%$ of the simulation period (out of 10 years) when the environmental criterion is considered. When the flood protection criterion is analyzed, $P_{\text {flood }}$ indicator time series (Fig. 11b) shows that the system relatively frequently failed to meet the required flood protection. However, these were events with short duration, as the system met the expected performance level for almost $95 \%$ of the simulation period, according to the duration curve (Fig. 11b) for the flood protection performance indicator. The system also met the expected performance level

![img-9.jpeg](img-9.jpeg)

Fig. 9 Input scenario: a) Hydrometeorological data time series, b-e) generated functionality indicators time series
![img-10.jpeg](img-10.jpeg)

Fig. 10 System performance indicators for generated failure scenarios: a) failure magnitudes during the simulation, b) single performance indicators, c) overall performance indicator, d) Water levels in Zavoj reservoir and Nišava flood control point

![img-11.jpeg](img-11.jpeg)

Fig. 11 a) hazards occurrence frequency (roulette wheel samples percentage), b) single performance indicators duration curve, c) overall performance indicator - duration curve
when the water supply criterion is analyzed. In that case, the water supply is stable for approximately $80 \%$ of the simulation (the duration curve in Fig. 11b). When $P_{\text {power }} a$ performance indicator is analyzed the duration curve shows that the system was underperforming for almost the entire simulation period. In this case, the performance indicator was between 0.5 and 1 for approximately $55 \%$ of the simulation period. That led to low overall system performance where $P_{\text {system }}$ was below 0.8 for almost $60 \%$ time and with a minimum value of 0.4 .

Based on the overall performance indicator for the generated power objective, the system is underperforming. Unlike the environmental, flood protection and water supply objectives, the hydropower subsystem has a more detailed representation, and thus can be affected by more hazards than other subsystems (Table 2). Additionally, the hydropower subsystem can be indirectly affected by other failures. For example, some failures of the water supply, seepage or firefighting subsystems, will lead to changes in Zavoj reservoir water levels. Those changes affect the water head and eventually impact the power generated by the turbines. Assessing the effects of indirect impacts on different subsystems can be analysed only by system dynamics modelling, which emphasizes the role of this approach in system failure analysis.

Simulation results revealed that the system is frequently underperforming, even though the hazards were occasional and mostly low-severity. This indicates that the ageing and outdated infrastructure significantly increases failure risk and reduces the performance of the system endangered by the considered hazards. Additionally, accelerating the reliability decay during the partial functionality of a subsystem increases the system's vulnerability

Table 3 Subsystems failure magnitudes and induced drop of overall performance indicator - summary statistics


(Eq. (2)). This also amplifies the subsystem failure potential. As a consequence, a chain of low-severity hazards can lead to non-linearly superimposed effects causing significant damage to the system.

Statistical analysis of the simulation results is conducted (Table 3) to help with investment and maintenance prioritization. Several parameters are estimated and can be used to quantify the failure potential of each subsystem. Here, failure potential for each subsystem is analysed using the following parameters: the total number of failures, failure magnitudes (max, min and mean values), performance indicator drops $\Delta P_{\text {system }}$ (max, min and mean values) and damage potential $D P$. The drop in a performance indicator is evaluated prior to subsystem full disconnection, i.e., it considers only the initial performance drop when the hazard occurs. The total number of failures shows that some of the system's components were in failure mode more than 20 times (e.g., spillway, firefighting extraction,) while some other subsystems were affected just a couple of times (seepage, penstock leakage, maintenance unit) or unaffected (power tunnel, penstock diameter, water supply). However, this parameter could be used for some preliminary maintenance plans since it does not show the full effect of the subsystems' failures on system performance. To assess the real effects of the subsystem failures and make decisions accordingly, failure magnitudes and accompanying system performance drops have to be considered.

Failure magnitudes vary between 0.075 and 0.457 during the simulation. The largest failure magnitude was generated for the spillway (Subsystem 3). However, this value does not reflect the true failure potential of the spillway. The maximum performance drop during the spillway failures is 0.094 , which is the same as the max performance drops during the

failures of environmental, seepage, penstock, powerhouse, Zavoj and Nišava water level sensors subsystems. This non-linear relationship between the max failure magnitude and max performance drop (i.e., max failure magnitude does not coincide with the max performance drop) can be explained by the fact that the generated max failure magnitude can happen in the period when some of the subsystems are not used. For example, the spillway can have the max failure magnitude even when there is no overflow. In that case, the failure effect on system performance will be negligible. To quantify the true failure potential of a subsystem, the total number of failures and total performance drop (the sum of the single performance drops during the subsystem's failures) have to be considered. Still, a single performance drop cannot be always assigned to one subsystem as, in many cases, it is induced by a chain of failures. Hence, a total performance drop during the failures of a subsystem cannot be used. The number of simultaneous failures, which induced the single performance drop, should be also used. When all these factors are considered, the true failure potential $D P$ for each subsystem can be quantified (Eq. (25)). In this case study, the firefighting subsystem had the greatest effect on system performance drop $(D P=0.317)$ due to frequent failures during the simulation. Also, $D P$ values between 0.107 and 0.197 show significant effects of the environmental, spillway, powerhouse, and water supply subsystems failures. Based on the simulation results, these subsystems should be prioritized in maintenance plans to increase their reliability and reduce failure potential accordingly. Furthermore, $D P$ is evaluated assuming that each subsystem affected by a generated hazard, equally contributes to a system performance drop. Weighting the contribution of each subsystem requires further insight into the subsystems' failure modes, which will be the subject of future research.

The Pirot DRS case study demonstrates the application of the proposed methodology. Data used in this study pertain to a real system, but some of the data sets were assumed to create the subsystems database and the simulation results are affected by that selection. For a more realistic application, expert knowledge and real-world data have to be used for creating a reliable hazard database.

# 4 Conclusions 

This paper presents a novel failure generation methodology suitable for the creation of the disturbance scenarios for the dam and reservoir system digital twin. The methodology contributes to the assessment of the system's performance under failure conditions. Here, failure modes of the dam and reservoir system are created using a causal approach where each subsystem's failure depends on external disturbance (represented by hazard severity) and subsystem reliability (used to describe ageing). The hazard severity and subsystem's reliability are used as input variables for the fuzzy logic-based failure magnitude simulator. The main output from the simulator is the failure magnitude, which quantifies the subsystem's failure using the universal functionality indicator. The subsystem's functionality is described using the $0-1$ numerical scale, where the subsystem can be (1) fully functional (functionality indicator is 1 ), (2) non-functional (functionality indicator is 0 ) or (3) in partial failure mode (still operating but with reduced capacity, taking values between 0 and 1). This failure estimating procedure can be repeated at each simulation timestep making the failure simulator suitable for coupling with system dynamics models to evaluate failure effects on system performance. The application of the proposed failure generator is demonstrated on the Pirot DRS in Serbia. Based on the results obtained in this study, the following specific conclusions can be derived:

- The probabilistic failure generator based on roulette wheel selection creates disturbances in a realistic way when low-severity hazards occur more often. If it is necessary to estimate the effects of high-severity hazards, the simulation period has to be extended to increase the possibility of those hazards being selected in a roulette wheelbased selection process. Even though it seems that the absence of extreme hazards (in short simulation periods) can be solved by applying random selection, this could lead to the frequent occurrence of extreme events. This can lead to unrealistic total collapse situations (e.g., dam failure which makes the system non-recoverable).
- Even though the failure generator selects hazards occasionally (according to the occurrence probability assigned to each hazard), the SD model reveals significant underperformance in long simulation periods. This is achieved by modelling the effects of ageing and increasing the system's vulnerability when subsystems are partially functional. Using the exponential reliability function yielded an efficient way to represent subsystems' ageing. Increasing subsystems' vulnerability by modifying the exponential reliability function shows a plausible approach to mimicking the amplified failure potential of the subsystems that are already in failure mode.
- Using hazard severity and subsystem reliability scales as the failure generator inputs and subsystem's failure magnitude (and functionality accordingly) as the normalized $(0-1)$ output makes the proposed fuzzy logic-based failure generator general and applicable to different systems.
- Expert knowledge, used here to create causality in the failure process, describes only the direct impacts of the specific subsystems for each hazard. Coupling expert knowledge with the proposed failure generator and SD model helped in assessing the indirect effects of different failures on the overall system's performance.
- The proposed methodology helps in the detection of the riskiest subsystems considering their true failure exposure, unlike the traditional approach where all the subsystems are treated equally (the current state of the subsystem is not considered). True failure potential is evaluated using the parameter describing the current state of the subsystem (reliability) and the hazard leading to the failure (hazard occurrence probability and hazard severity). This approach can support system investment prioritization due to its capability to detect "hidden" failure risks.
- Expert knowledge is used to estimate parameters and membership functions used in the fuzzy logic-based failure generator. SD models allow for the hard-coded variables to be re-evaluated and updated occasionally according to subsequently obtained real failure information. This will enable the generation of more realistic failures.

Considering the specific conclusions derived in this paper, further insights into the DRS digital twin developments are needed to overcome some of the assumptions of this case study and will be a subject of future investigation. Fuzzy logic parameters and membership functions used in failure magnitude estimation have to be analyzed in more detail to determine the optimal level of complexity for the fuzzification process. Variables in the subsystems database, such as procurement and repair times, have to be estimated using real-world data. This can be integrated into occasional updates of the parameter required by the failure generator. Additionally, expert knowledge (previous experience and theoretical knowledge) has to be employed to identify potential hazards and causalities, and for better estimation of the subsystems' reliability over time.

Authors Contribution Conceptualization, methodology, formal analysis (Miloš Milašinović); methodology, writing, review and editing (Miloš Milašinović, Damjan Ivetić, Milan Stojković and Dragan Savić); funding acquisition (Milan Stojković);

Funding This research was funded by the Science Fund of the Republic of Serbia, through the project DyRes_System: "Dynamics resilience as a measure for risk assessment of the complex water, infrastructure and ecological systems: Making a context" of the PROMIS call (Grant No. 6062556). This work was also supported by the Serbian Ministry of Education, Science and Technological Development (Agreement No. $451-03-68 / 2022-14 / 200092$ ).

Data Availability All data and materials used in the research are documented within the manuscript.

# Declarations 

Ethical Approval The authors ensure that this article has not been published elsewhere and that there has been no plagiarism.

Consent to Participate All authors gave explicit consent to participate in this study.
Consent to Publish All authors gave explicit consent to publish this manuscript.
Competing Interest The authors have no relevant financial or non-financial interests to disclose.

# Authors and Affiliations 

## Miloš Milašinović ${ }^{1}$ (D) $\cdot$ Damjan Ivetić ${ }^{1}$ (D) $\cdot$ Milan Stojković ${ }^{2}$ (D) $\cdot$ Dragan Savić ${ }^{1,3,4}$ (D)

Miloš Milašinović
mmilasinovic@grf.bg.ac.rs
Damjan Ivetić
divetic@grf.bg.ac.rs
Milan Stojković
milan.stojkovic@ivi.ac.rs
Dragan Savić
dragan.savic@kwrwater.nl; d.savic@exeter.ac.uk
1 Faculty of Civil Engineering, Department for Hydraulic and Environmental Engineering, University of Belgrade, Belgrade, Serbia
2 The Institute for Artificial Intelligence Research and Development of Serbia, Belgrade, Serbia
3 KWR Water Research Institute, Nieuwegein, The Netherlands
4 Centre for Water Systems, University of Exeter, Exeter, UK