# Reduction of Uncertainty Propagation in the Airport Operations Network 

Álvaro Rodríguez Sanz, Fernando Gómez Comendador, Rosa Arnaldo Valdés<br>Airspace Systems, Air Transport and Airports Department, ETSIAE-UPM, Spain


#### Abstract

Airport operations are a complex system involving multiple elements (ground access, landside, airside and airspace), stakeholders (ANS providers, airlines, airport managers, policy makers and ground handling companies) and interrelated processes. To ensure appropriate and safe operation it is necessary to understand these complex relationships and how the effects of potential incidents, failures and delays (due to unexpected events or capacity constraints) may propagate throughout the different stages of the system. An incident may easily ripple through the network and affect the operation of the airport as a whole, making the entire system vulnerable. A holistic view of the processes that also takes all of the parties (and the connections between them) into account would significantly reduce the risks associated with airport operations, while at the same time improving efficiency. Therefore, this paper proposes a framework to integrate all relevant stakeholders and reduce uncertainty in delay propagation, thereby lowering the cause-effect chain probability of the airport system (which is crucial for the operation and development of air transport).



Firstly, we developed a model (map) to identify the functional relationships and interdependencies between the different stakeholders and processes that make up the airport operations network. This will act as a conceptual framework. Secondly, we reviewed and characterised the main causes of delay. Finally, we extended the system map to create a probabilistic graphical model, using a Bayesian Network approach and influence diagrams, in order to predict the propagation of unexpected delays across the airport operations network. This will enable us to learn how potential incidents may spread throughout the network creating unreliable, uncertain system states.

Policy makers, regulators and airport managers may use this conceptual framework (and the associated indicators) to understand how delays propagate across the airport network, thereby enabling them to reduce system vulnerability, and increase its robustness and efficiency.

Keywords: Uncertainty, airport operations, process modelling, delays, propagation, Bayesian Networks

# HIGHLIGHTS 

- Airport operations constitute a complex network with multiple facilities, stakeholders and processes.
- Internal delays may propagate throughout the system, amplifying inherited reactionary delays.
- Policy makers need a framework to classify the functional relationships between airport processes.
- Understanding interactions between system nodes will reduce uncertainty in delay propagation.
- A group of predictability indicators will permit regulation of system efficiency.


## 1. INTRODUCTION

Airport operations have been identified as a crucial link in the air transport supply chain: they represent a fundamental step regarding efficiency, safety, passenger experience and sustainable development (Ashford et al., 2013).

Moreover, airport operations define a large, dynamic and complex system, with several facilities, processes and stakeholders that are interrelated and interact with each other (Kazda and Caves, 2007). There are multiple agents involved in the airport environment and they are still communicating in limited ways with each other (EUROCONTROL, 2015a). Because of this, an incident (delay) may easily travel through the network and affect the operation of the airport as a whole (Gulding et al., 2013). To develop a holistic view of the processes, considering all the involved parties and the nexus among them would significantly reduce uncertainty at airport operations (Zografos et al., 2013).

New airspace organisation, strategically increasing air traffic demand, and new Air Traffic Management (ATM) functions and processes arising from research and development (mainly SESAR and NextGen) will generate significant additional load on airport performance, which may become critical with regard to the robustness of the system (FAA, 2015; EUROCONTROL, 2015a). In such a dynamic and challenging operating environment, an active and cooperative strategy will be required to safely adapt demand to expected airport capacity (Evans and Schäfer, 2014).

All participants in airport operations will be confronted with an operational situation that evolves throughout the day, resulting in highly demanding interactive communication between the parties (Price and Forrest, 2016). In order to ensure that the system operates efficiently under these conditions (as regards financial, environmental and safety factors), regulators and policy makers need to properly understand:

- How airport processes relate to and influence one other (framework and taxonomy of functional relationships).
- How potential failures (due to unexpected events or capacity constrains) affect the different elements of the system (delay characterisation).
- How the effect of latent inefficiencies is propagated through the network nodes (delay propagation model).
- How to assess system response to delay propagation (efficiency indicators and measurement of predictability).

Therefore, the aim of this paper is to develop a predictive model in order to understand how delays propagate stochastically across the network (and the probability of this propagation occurring). This may be considered to be the first step in responding to contingencies in the system. The entire network (ground access, landside, airside and airspace) and all the stakeholders (ATS providers, airlines, airport operators, policy makers and ground handling companies) will be involved in adapting the system (holistic vision).

The paper is structured as follows: Section 1 presents the problem and gives the reason for this study, the main objectives and the approach used. Section 2 reviews the state of the art and explains how the different aspects of the problem (network structure, delay categorisation, incident propagation and performance indicators) have been analysed in past studies. This section also sets out the methodology used and provides a theoretical framework to deal with the problem. Section 3 reviews the findings of the analysis and presents a practical application of the model (validation). Then, Section 4 sets out a practical approach for policy makers (to ensure efficient, safe and sustainable airport operations) and reviews the utility and limitations of the study. Finally, Section 5 gives the main conclusions and discusses potential future research on the subject.

# 1.1 Problem statement 

The motivation behind the study is the huge impact that delays (mainly generated by capacity shortfalls in the system, or inefficient use of available resources) have an air transport performance, in terms of efficiency, safety, operations, cost effectiveness and environmentally sustainable development (Cook and Tanner, 2014; Ball et al., 2010; Sandrine et al., 2007). Moreover, there is a need to identify the interdependencies between processes in the airport operations network, which may amplify or absorb delays (Ashford et al., 2013).

During 2014, the average delay per delayed flight in the EUROCONTROL Statistical Reference Area was 26 min , with $10 \%$ of all European flights registering more than 15 min delay (EUROCONTROL, 2015b). According to Cook and Tanner (2014), the average delay cost for a delayed European flight in 2014 was EUR 1,970, resulting in a network average delay cost of EUR 100 per minute, and a network delay total cost of EUR 1,250 million.

Additionally, delays have a substantial impact on the schedule adherence of airports and airlines, passenger experience, customer satisfaction and system reliability (Jetzki, 2009).

Inefficiencies that occur in the airport environment (rotation phase from inbound to outbound flights) contribute significantly (up to $44 \%$ in 2014) to delay propagation throughout the air transport network (EUROCONTROL, 2015b; EUROCONTROL, 2014). Therefore, this study will analyse how the different processes, stakeholders and facilities that interact in the airport operations network contribute to creating, amplifying and propagating delays.

Firstly, when defining a network through which incidents may propagate we must delimit the problem in space and time.

- Space: In the analysis we use a dynamic spatial boundary associated with the Extended Terminal Manoeuvring Area (E-TMA) concept, which allows us to consider inbound and outbound timestamps. This management boundary (airport centric limit of 200-500 NM) has already been implemented at multiple airports, with a horizon that varies from around 190 NM for Stockholm to 250 NM for Rome and 350 NM for Heathrow (Bagieu, 2015).

The E-TMA (and not just the basic on-ground turnaround path in the airport that connects inbound and outbound flights) is selected in order to integrate delay propagation in the airport with global delays in the air traffic network. This approach, which reflects the interaction between airspace, airside and landside processes is in line with the spatial scope of the SESAR TAM project (Spies et al., 2008), as shown in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1 - Spatial scope of the problem

- Time: In the analysis we restrict actions to a tactical phase (day of operations) in order to consider the primary and initial inefficiencies.

Airports are limited in capacity by operational constraints (Montlaur and Delgado, 2015). When there is an important imbalance between capacity and demand, strategies relating to resource allocation at airport facilities and Air Traffic Flow and Capacity Management (ATFCM) initiatives are implemented to smooth traffic arrivals and departures, thereby transferring costly airborne delays (due to holdings and/or path stretching) to pre-departure on-ground delay (Sandrine et al., 2007). During the tactical phase of ATFCM (day of operations), on-ground delay at the airport of origin is handled by assigning slots to flights affected by regulations (EUROCONTROL, 2015c). Therefore, as regards the problem that is the subject of this paper, the ideal temporal scope is the tactical period.

To understand the impact of delays on the air transport network, it is necessary to review how rotation between inbound and outbound flights is usually managed (Hansen and Zou, 2013):

- Figure 2 shows how the system would operate without delays: firstly, a Scheduled Time of Departure (STD) is established, bearing in mind preferred passenger travel times, internal airline constraints (efficient crew schedules and fleet plans), and ATFCM and airport capacity availability (Hansen and Zou, 2013). These considerations lead to a Scheduled Time of Arrival (STA) at the destination airport. Then, after an active turnaround (e.g. deboard passengers, clean and refuel the aircraft, board new passengers), the aircraft is ready for the next leg in the air transport network: this is the Ideal Time of Departure (ITD). Nevertheless, a buffer time is usually added to the operational plan, in order to accommodate statistically foreseeable delays resulting from flight restrictions imposed to handle traffic, congestion, incidents, and a variety of other factors (Cook and Tanner, 2014; ITA, 2000). As previously explained, the goal of ATFCM initiatives is transfer costly airborne delays to on-ground delays (Sandrine et al., 2007), and this is why the buffer time is considered to be on the ground. The buffer time added to the fixed turnaround gives the next STD.

If the spatial boundary in question is extended to the E-TMA, then it will also be necessary to evaluate the Scheduled Time of Arrival at E-TMA (STA-E) and the Scheduled Time of Departure from E-TMA (STD-E), in order to consider the rotation and all the processes at E-TMA. This macroscopic view enables us to assess not only the ground operations but also certain ATC (Air Traffic Control) and ATFCM processes. In this way we can establish a link between the airport (ground) and the air transport network (air).

![img-1.jpeg](img-1.jpeg)

Figure 2 - System operating without delay

- Figure 3 and Figure 4 reflect how the ideal situation is altered by initial departure delays, flight (airborne) delays and delays resulting from internal E-TMA processes (Ciruelos et al., 2015; Hansen and Zou, 2013). If these delays are absorbed by a minimum fixed E-TMA rotation time (ground and air) and the buffer time, the next flight/leg will depart on time. Additional variables are now required to enable us to consider these delays: Actual Time of Departure (ATD) allows us to consider departure delays, Actual Time of Arrival at E-TMA (ATA-E) and Actual Time of Arrival (ATA) permit us consider airborne delays, and Actual Time of Departure (ATD) and Actual Time of Departure from E-TMA (ATD-E) enable us to consider internal primary delays.
![img-2.jpeg](img-2.jpeg)

Figure 3 - Impact of delay on E-TMA rotation (delay is absorbed)

![img-3.jpeg](img-3.jpeg)

Figure 4 - Impact of delay on E-TMA rotation (delay is not absorbed)
This paper considers a flight, which is delayed according to the scheduled flight plan, arriving at the E-TMA boundary, and studies how this delay is amplified and propagated by potential inefficiencies in the internal processes of the E-TMA. This analysis will allow us to evaluate, using a tactical approach, the appropriate buffer and rotation times required to ensure efficient operation (and determine if the system is sufficiently robust to absorb the delay).

Equations (1) and (2) show the rationale behind the analysis: if the Scheduled Time of Departure from E-TMA (STD-E) is "later" than the Actual Time of Departure from E-TMA (ATD-E), this means that the minimum fixed rotation time (ground and air) of the E-TMA and the buffer time are able to absorb delays. This means that the punctuality of the next flight is not affected.

STD-E $=$ STA-E + ROTATION TIME + BUFFER TIME
ATD-E $=$ ATA-E + ADJUSTED ROTATION TIME + DELAY

Therefore, the planning objective for absorbing delays in the E-TMA (ground and air) is given by Equation (3).

ROTATION TIME (scheduled) + BUFFER TIME $\geq$
ROTATION TIME (actual) + REACTIONARY DELAY + PRIMARY DELAY

Delay propagation and the required minimum rotation time in the E-TMA (on-ground

turnaround and air processes) introduce uncertainty into the model.

The problem will be expressed using incremental times $(\Delta t)$, rather than absolute values of time. The aim of this approach is to show how the different processes in the E-TMA contribute to the ATD-E (by registering a partial $\Delta t$ for each phase) without hiding inefficiencies. Otherwise, a process delay $(\Delta t>0)$ could be disguised by a stage that performs better than expected $(\Delta t<0)$.

The main objective of the paper is to provide a conceptual framework that allows us to understand how the different nodes in the airport operations network (processes and elements) relate to one other, and how potential inefficiencies may propagate delays throughout the system (uncertainty reduction).

This research topic is related to several EUROCONTROL and SESAR concepts (EUROCONTROL, 2015a): AOP (Airport Operations Plan), ATV (Airport Transit View), TAM (Total Airport Management), APOC (Airport Operations Centre), A-CDM (Airport Collaborative Decision Making) and SWIM (System Wide Information Management).

# 2. BACKGROUND \& METHODOLOGY 

An assessment of how uncertainty in airport operations may be reduced covers five main areas:

- Airport operations network (structure and interdependencies within the E-TMA).
- Delay characterisation (main causes and types of delay).
- Identification of the E-TMA processes that are affected by each type of delay.
- Delay propagation throughout the system.
- Efficiency and punctuality indicators.

This Section provides an overview of existing literature and sets out the proposed method, for each of the five topics. Figure 5 shows the overall methodology for tackling the issue of uncertainty reduction in airport operations.

![img-4.jpeg](img-4.jpeg)

Figure 5 - High level methodology for the issue of uncertainty propagation

# 2.1 Conceptual framework and taxonomy for the airport operations network 

Airport operations have been widely analysed in a significant number of studies, which illustrate the processes, facilities and agents that shape the system (Ashford et al. 2013; Horonjeff et al., 2010; Kazda and Caves, 2007; Wells and Young, 2004; de Neufville and Odoni, 2003).

IATA (2014), Correia and Wirasinghe (2013), Ashford et al. (2013) and Tošić (1992) provide several detailed performance and operational models that deal with landside processes at airports. Wilke et al. (2014), Norin et al. (2012) and Fricke and Schultz (2009) focused their studies on surface operations and airside procedures (mainly on-ground turnaround). Katsaros et al (2013) proposed a model for integrating landside and airside processes during on-ground turnaround. Finally, airline operations and ATC processes in the airport environment were reviewed by Pérez Sanz et al. (2013) and Tanner (2007).

This paper proposes a holistic view for the whole airport system, combining the different parts and considering the functional dependencies between them. This approach enables us to integrate all the phases in the E-TMA (ground access, landside, airside and airspace) and define all the interactions that make up the network.

The conceptual framework of airport operations (within the spatial boundary of the E-TMA) was developed using Business Process Modelling (BPM). BPM is a management tool that is used to improve the quality and efficiency of a system, by classifying and identifying actors, events, activities, interdependencies and information flows within the main operation

of the organisation (Aguilar-Savén, 2004). A key feature of the BPM methodology is that it provides a graphical representation of system processes. This representation illustrates a sequence of activities and dependencies and enables inefficiencies, deficiencies and redundancies to be identified (Becker et al., 2000). BPM may be applied to all kinds of industries and organisations, and has been successfully implemented in air transport studies: surface operations (Wilke et al., 2014), passenger check-in (Lincoln et al., 2010) and the airline business (Ploesser et al., 2009).

As part of this study, we made a diagram of the airport operations network (E-TMA) using BPM, giving us an accurate definition and representation of the system structure. We then evaluated the main processes that make up E-TMA rotation management giving us a global vision of the different agents and facilities. This BPM framework enables us to organise, analyse and characterise each particular event affecting the network.

In order to develop the conceptual structure of airport operations a variation of the methodology developed by Wilke et al. (2014) was used. This methodology requires input from various sources and consists of four main steps, as shown in Figure 6.

- The first step was a review of relevant literature and existing airport models (Ashford et al. 2013; Pérez Sanz et al., 2013; Horonjeff et al., 2010; Kazda and Caves, 2007; Tanner, 2007; Wells and Young, 2004 and de Neufville and Odoni, 2003).
- Next, practical analysis was carried out (using hierarchical task analysis, as specified in Wilke et al. (2014) and Kirwan and Ainsworth (1992)). This analysis followed a top-down approach, which started by identifying the overall goal of the operation (objective). This main goal was subsequently broken down into sub-operations (phases), which were accomplished through a series of tasks and processes. The resources necessary to accomplish the tasks (i.e. actors and architecture) were defined. This method incorporated several sources of information in order to give a detailed understanding of the processes:
(1) Analysis of operations manuals (IBERIA, 2015a; IBERIA, 2015b and IBERIA, 2014), standards and procedures (IATA (2015, 2014) and ICAO (2013, 2006a, 2006b, 2006c, 2005a, 2005b, 2004)).
(2) Observations at Adolfo Suárez Madrid-Barajas Airport during 2014 and 2015.
(3) Structured communications with relevant stakeholders (see Table 1).
- The previous steps led to an initial process model.
- Finally, the initial model was refined and validated with the help of subject-matter experts (see Table 1).

![img-5.jpeg](img-5.jpeg)

Figure 6 - Methodology for constructing the airport operations (E-TMA) process model


Table 1 - List of informants, interviewees and contributors

We used Unified Modelling Language (UML) to graphically represent the BPM (see Figure 7). UML is a visual modelling language that enables a pattern of a system to be created (Engels et al., 2005). It is the core of the proposed methodology for the theoretical framework. Therefore, the designed conceptual structure for airport operations (E-TMA) is

basically a UML sequence diagram with the following considerations.

The diagram has three major components - architecture, flow units and processes. These elements were completed and subsequently reviewed by the main stakeholders (actors involved in airport operations).

- Architecture (facilities). The architecture may be broken down into three key areas surrounding airspace, airport airside and airport landside (including ground access to the airport). These areas are divided into arrival and departure, as each operation can have different processes. Every component of the architecture framework corresponds to a lifeline (as per UML terminology), which is the backbone of all processes that will occur in the component environment. The vertical bars that make up a lifeline represent the processes occurring in a similar timeframe. The black dot at the end of a lifeline indicates that this series of processes has been completed with respect to the overall operation.
- Flow units. Aircraft, passengers and cargo are represented as agents that interact with all operations and events that arise until the overall process has been completed. In UML terminology, these are known as actors. The length of each actor's bar provides information about its impact on the overall operation.
- Processes. The different procedures and operations, which make up the E-TMA rotation, connect flow units and architecture. Each process is represented by an arrow. If the arrow goes left-to-right, that means that the process can progress naturally. However, if the arrow goes right-to-left (see Figure 7, process 1.8: Missed Approach), the process can no longer progress through the diagram and it is necessary to return to the previous lifeline.

Ongoing messages such as ATC Process, Turnaround, Taxiing and Passenger Flow (see Figure 7) represent the general events that make up the BPM structure. Each of these events are in turn made up of several basic processes. Blue messages are explanatory and refer to certain complex processes that (a) encompass a group of sub-processes or (b) can be managed in different ways.

The operational framework, depicted in Figure 7, has a number of special features that we will now discuss:

- Recurring messages (2.1: Security Control Arrival, 2.2: Passport Control Arrival, 2.3: Baggage Claim, 2.4: Custom Control, 2.5: Connecting and 6.1: Baggage Handling System) indicate processes that occur in the same lifeline and which, therefore, do not progress through the diagram.
- Process 2: Passenger and Baggage Unloading is represented in a different way. The arrow for this process starts at a black dot and ends at a lifeline. This is because there is a difference between the aircraft's On-Block time and the start of the passenger

disembarkation and baggage unloading procedures.

- Processes 3: Airport Exit and 17: Departure correspond to a lost message (as per UML terminology), as there is no subsequent event that is of interest to the overall E-TMA operation.
- Windows on the left-hand side of Airspace Arrival and the right-hand side of Airspace Departure represent E-TMA entrance and exit, respectively, in other words the start and end of the considered operation.
![img-6.jpeg](img-6.jpeg)

Figure 7 - Conceptual framework of airport operations (E-TMA)

Analysis of the overall E-TMA process is completed by adding the main stakeholders in the airport operations network: aircraft operators (airlines), ground handling agents, Air Navigation Service Provider (ANSP), airport operator and policy makers (regulator and supervisor). Each of these stakeholders makes a particular contribution to the different processes depicted in Figure 7.

Having generated the BMP (conceptual framework) we now have a general overview of all relevant processes that will allow us to analyse the airport operations network. To easily handle this information, a taxonomy for airport (E-TMA) operations is proposed in Table 2 in line with the diagram outlined in Figure 8.
![img-7.jpeg](img-7.jpeg)

Figure 8 - Outline for developing a taxonomy for airport operations (E-TMA)

The structure of the taxonomy is given in Table 2. This taxonomy provides identification codes for classifying different procedures; e.g.: security control processes at departure (1-LD-SC-APO), taxiing permission when landing (2-ASiA-TP-ANSP) and cargo loading for departure (3-ASiD-HN-HAND).

Policy makers and airport managers could apply this taxonomy to organise the different ETMA procedures thereby enabling them to structurally analyse, supervise and regulate the operations in the overall process, e.g., locate potential inefficiencies, assess punctuality or adjust service levels.



Table 2 - Taxonomy for airport operations

# 2.2 Identification and characterisation of delays affecting the airport operations network 

In air transport a delay can be defined as the time interval or lapse that arises when a planned event does not occur at the scheduled time (EUROCONTROL, 2015b). Delays can happen during the different phases of a flight: departure, airborne, arrival and ground turnaround (Jetzki, 2009).

Furthermore, disruptions in one part of the air transport network can propagate to many others. A significant portion of these propagations ( $44 \%$ in 2014 according to EUROCONTROL, 2015b and EUROCONTROL, 2014) occurs in airports (i.e. the nodes of the system), where incoming aircraft continue on to the subsequent legs of their planned itineraries, crew members may connect to other flights, and passengers also connect to other flights. Flows of aircraft, crew and passengers at airports are the dominant mechanism by which delays propagate through the air transport system (Rebollo and Balakrishnan, 2014).

In order to unify the reporting of delays among its member airlines, the International Air Transport Association (IATA) has published a standard coding system for delay classification (IATA, 2015; EUROCONTROL, 2015b). The most useful delay classification system, when analysing operated time versus scheduled time, is that which considers primary and reactionary delays (ITA, 2000).

- Primary delays (EUROCONTROL, 2015b; ITA, 2000) correspond to an initial delay caused to a given flight. They are classified according to causes of delay: passenger and baggage, cargo and mail, aircraft and ramp handling, technical and equipment, damage to aircraft, flight operations and crewing, weather, airport facilities and operations, governmental authorities and ATC/ATFCM processes. Late arrivals of connecting flight, connecting passengers, baggage, load or crew members are not to be included in primary causes of delay.
- Reactionary delays (EUROCONTROL, 2015b; ITA, 2000) correspond to delays due to the late arrival of aircraft delayed during its previous leg operation, late arrival of a connecting flight, passengers or load, and late arrival of crew members, expected from another flight.

Reactionary delays occur as a result of primary delays; if there were fewer primary delays there would be a consequent reduction in the number of reactionary delays (ITA, 2000). Initial (primary) delay could indeed cause disturbances across the day (time) and the network (space), due to slightly tight operating schedules, established to achieve economic efficiency, resulting in reactionary delays (Campanelli et al., 2014; Ball et al., 2010).

Reactionary delays (reflecting delayed inbounds, imposed from previous flight legs) usually represent $40 \%-45 \%$ of all generated delay minutes (EUROCONTROL, 2015b; Jetzki, 2009), and consequently most of the previous studies on air transport delays have focused on characterising them (Campanelli et al., 2014; Rebollo and Balakrishnan, 2014; Fleurquin et al, 2014; Xu et al., 2005). Katsaros et al. (2013), Oreschko et al. (2012) and Fricke and Schultz (2009) focussed their studies on primary delays that affect on-ground turnaround.

For the purposes of this paper, we will review the impact of reactionary and primary delays on the E-TMA rotation process. The objective is to predict how the system and the internal (primary) delays amplify or reduce reactionary delays throughout the E-TMA. This approach allows us to connect on-ground operations with the whole air transport network (airborne operations).

The main causes of delays in the E-TMA were classified (see Table 3) by reviewing the IATA Delay Codes (EUROCONTROL, 2015b), the delay coding system developed by Wu and Truong (2014) and data from the EUROCONTROL Central Office of Delay Analysis (EUROCONTROL, 2015b). These delay categories are highly independent as past studies confirm (Fricke and Schultz, 2009).



# Table 3 - Main causes of delay in E-TMA processes 

Figure 9 shows a mind map identifying the main causes of delay in E-TMA processes. Figure 10 gives a diagram that highlights which part of the airport operations network may be affected by each cause of delay (the principal relevant contributing factors that can cause delays in each element have been considered). These maps (Figure 9 and Figure 10) were constructed by analysing previous studies and literature (EUROCONTROL, 2015b; Ashford et al. 2013; Norin et al., 2012; Fricke and Schultz (2009) and Laskey et al, 2005), operations manuals (IBERIA, 2015a; IBERIA, 2015b and IBERIA, 2014), empirical observations and expert judgement followed by validation by the relevant stakeholders (similar to the development of the BPM as set out in Section 2.1). These maps were designed as a means of visualising the relevant factors associated with delay propagation, and were of significant use when devising the propagation model.

![img-8.jpeg](img-8.jpeg)

Figure 9 - Mind map for characterising the delays affecting E-TMA processes
![img-9.jpeg](img-9.jpeg)

Figure 10 - Processes at the E-TMA impacted by main causes of delay

# 2.3 Model of delay propagation 

Delays are generated by elements of the system, but their propagation is a global process fostered by relationships inside the network. Therefore, network analysis provides a global view of the propagation process (Cook et al., 2011).

A review of the literature about delay propagation through the air transport system shows that a large number of studies deal with the complexity of the network (Cook et al., 2015; Ciruelos et al., 2015 and Pyrgiotis et al., 2013) and the potential impact of delays on the system's reliability (Nash, et al. 2012; Abdelghany et al., 2008 and Abdelghany et al., 2004).

As regards the spatial scope of the problem, delay propagation affecting internal E-TMA and airport (airside and landside) processes has received little attention (Norin et al., 2012 and Fricke and Schultz, 2009). Nevertheless, "rotation" (delayed flight cycles) is the stage that has the greatest impact on punctuality within the entire air transport network (EUROCONTROL, 2015b) and accumulates its impact over the day. This paper focuses on the rotation stage.

There have been several attempts to model delay propagation through the air transport network. The inherent complexity of the processes and mechanisms requires the use of different modelling techniques (Ciruelos et al., 2015): queuing theory (Wang et al., 2003), stochastic delay distributions (Tu et al., 2008), propagation trees (Campanelli et al., 2015; Fleurquin et al., 2014 and Ahmadbeygi et al., 2008), periodic patterns (Abdel-Aty et al, 2007), chain effect analysis (Wong and Tsai, 2012) and random forest algorithms (Rebollo and Balakrishnan, 2014).

The theory of statistical estimation provides the necessary tools to develop an uncertainty propagation model (Henrion, 1988). In this paper, delay propagation patterns and influence variables are characterised using a Bayesian Network (BN) approach, including stochastic parameters to reflect the inherent uncertainty of the performance of the airport operations network.

Several studies (Buldyrev et al., 2010 and Laskey et al., 2006) demonstrate the utility of BNs as a methodology for modelling the diffusion of events and incidents from a node-level to a system-level (interdependence of multiple factors). Moreover, Xu et al. (2005) confirmed that BNs can explain how subsystem-level causes propagate to provoke system-level effects, specifically focusing on how delays at an origin airport propagate to create delays at a destination airport.

There are several advantages in using BNs to investigate delay propagation. BNs are a useful tool for analysing complex problems as they can provide support for decision-making and can also enable the system to systematically collate, organise and structure available information, whether it comes from empirical values, model results or expert judgments (Farr et al., 2014; Johnson et al., 2010 and Uusitalo, 2007). Another advantage of BNs is their ability to provide approximate models for complex, poorly understood problems, especially for parts of the problem that have insufficient data to permit traditional statistical analysis (Xu et al., 2005). Moreover, BNs have unique strengths with respect to inference and visualisation (Koller and Friedman, 2009) and have previously been used to tackle air

transport issues (Farr et al., 2014; Yorukoglu and Kayakutlu, 2011; Morales-Napoles et al., 2006; Laskey et al., 2006 and Xu et al., 2005).

Bayesian networks (BNs) are graphical probabilistic models used for reasoning under uncertainty (Korb and Nicholson, 2011; Jensen and Nielsen, 2007; Cowell et al., 1999; Pearl, 1986 and Pearl, 1985). A BN is a directed acyclic graph (DAG), in which each node denotes a random variable, and each arc denotes a direct dependence between variables (nodes that are not connected symbolise variables that are conditionally independent of each other) (Pearl, 1986). The DAG that results from the construction of a BN is quantified through a series of conditional probabilities based on data or information available on the system or problem (Korb and Nicholson, 2011 and Jensen and Nielsen, 2007;) and defines a factorisation of a joint probability distribution over the variables represented in the DAG. The factorisation is represented by the directed links in the DAG (Kjærulff and Madsen, 2008 and Jensen and Nielsen, 2007). That is, each node is associated with a probability function that takes, as input, a particular set of values for the node's parent variables, and gives (as output) the probability (or probability distribution, if applicable) of the variable represented by the node (Neapolitan, 2004). Therefore, the BN model structure (nodes and arcs) encodes conditional dependence relationships between the random variables. Each random variable is associated with a set of local probability distributions (parameters in the Conditional Probability Tables (CPT)). Probability information in a BN is specified via these local distributions (Koller and Friedman, 2009).

Each conditional probability distribution is given by $\mathrm{P}\left(\mathrm{X}_{\mathrm{v}} / \mathrm{X}_{\mathrm{pa}(\mathrm{v})}\right)$, where V is the set of nodes in the DAG; $\mathrm{P}\left(\mathrm{X}_{\mathrm{v}}\right)$ the joint probability distribution over the set of variables $\mathrm{X}_{\mathrm{v}}$; and $\mathrm{X}_{\mathrm{pa}(\mathrm{v})}$ the set of parent variables of variable $\mathrm{X}_{\mathrm{v}}$. The conditional probability represents a set of rules, where each rule, or conditional probability, takes the form:

$$
\mathrm{P}\left(\mathrm{X}_{\mathrm{v}}=\mathrm{x}_{\mathrm{v}} / \mathrm{X}_{\mathrm{pa}(\mathrm{v})}=\mathrm{x}_{\mathrm{pa}(\mathrm{v})}\right)=\mathrm{z} \text {, or more simply } \mathrm{P}\left(\mathrm{x}_{\mathrm{v}} / \mathrm{x}_{\mathrm{pa}(\mathrm{v})}\right)=\mathrm{z}
$$

If the Markov condition is satisfied for the set of nodes (which means that each $X_{i}$ is independent of its non-descendent variables), the probability distribution of a BN is the product of the conditional probabilities of all the variables of a BN, conditioned only by its parents (Pearl, 1985).

Therefore, a BN (Ding, 2010 and Castillo et al., 1999) is a pair (G,P), where G is a directed acyclic graph (DAG) defined on a set of nodes X (the random variables), and $P=$ $\left\{p\left(x_{1} \mid \pi_{1}\right), \ldots, p\left(x_{n} \mid \pi_{n}\right)\right\}$ is a set of $n$ conditional probability densities (CPD), one for each variable. $\Pi_{i}$ is the set of parents of node $\mathrm{X}_{\mathrm{i}}$ in G . The set P defines the associated joint probability density of all nodes as $p(\boldsymbol{x})=p\left(x_{1}, \ldots, x_{n}\right)=\prod_{i=1}^{n} p\left(x_{i} \mid \pi\left(x_{i}\right)\right)$ (the chain rule for BN). The graph $G$ contains all the qualitative information about the relationships between the variables, no matter which probability values are assigned to them. Additionally, the probabilities in P contain quantitative information, i.e., they complement the qualitative properties revealed by the graphical structure. Figure 11 gives an example for a BN, where $\mathrm{P}\left(\mathrm{x}_{1}, \mathrm{x}_{2}, \mathrm{x}_{3}, \mathrm{x}_{4}, \mathrm{x}_{5}\right)=\mathrm{P}\left(\mathrm{x}_{1}\right) \mathrm{P}\left(\mathrm{x}_{2} \mid \mathrm{x}_{1}\right) \mathrm{P}\left(\mathrm{x}_{3} \mid \mathrm{x}_{1}\right) \mathrm{P}\left(\mathrm{x}_{4} \mid \mathrm{x}_{2}, \mathrm{x}_{3}\right) \mathrm{P}\left(\mathrm{x}_{5} \mid \mathrm{x}_{4}\right)$.

![img-10.jpeg](img-10.jpeg)

Figure 11 - Example of causal inferences in a BN

# 2.3.1 Model construction and estimation 

The conceptual propagation model was developed using a two-step procedure. Firstly, the structure was defined according to observations, expert judgement techniques and stakeholder validation (similar to the development of the BPM as set out in Section 2.1). Then, it was tested with real data to ensure the validity of the model, as described in Section 3.1. Therefore, the BN building process is based on a combination of a weighting expert opinions scheme and structure learning with empirical data.

Figure 12 represents the initial structure of the BN propagation model. When developing the framework, the main idea was to include airside, landside and airspace processes in the definition of the airport operations network (a holistic view of the E-TMA architecture). With this approach, the model provides a nexus between airport processes and the whole air transport network.
![img-11.jpeg](img-11.jpeg)

Figure 12 - BN model of delay propagation in the E-TMA rotation process

Lateral nodes represent the main causes of delays in the E-TMA rotation process as set out

in the section on the characterisation of delays (see Section 2.2). These nodes are Reactionary, Passenger and Baggage Processes, Cargo, Airport Management, ATC and ATFCM, and Weather. In the case of Airport Management, this node acts as an intermediate element that integrate other factors, which are Handling, Airport Facilities and Operations, Technical Failures and Airline Operations. These lateral nodes may introduce delay ( $\Delta \mathrm{t}>$ 0 ) into system operation. The precise architecture and processes that are affected by each cause of delay were identified in the previous section (Section 2.2).

Furthermore, the five central nodes (vertical line) represent the basic architecture of the system (E-TMA rotation processes) that absorb $(\Delta t<0)$ or propagate $(\Delta t>0)$ the previous causes of delay (lateral nodes), depending on the system's operational efficiency. This architecture was reviewed when developing the BPM for E-TMA rotation (see Section 2.1):

- Airspace Arrival includes the airborne part of the E-TMA that the aircraft crosses during arrival.
- Airside Arrival includes runways, taxiways and the apron (used by an inbound flight in an arrival process).
- Landside includes passenger terminal building, hangars, cargo facilities and the ground access to the airport.
- Airside Departure includes runways, taxiways and the apron (used by an outbound flight in a departure process).
- Airspace Departure includes the airborne part of the E-TMA that the aircraft crosses during departure.

The DAG depicted in Figure 12 represents the causal relationships between these nodes. A root node in a BN model (i.e. in this case, a lateral node) represents a random variable (i.e. the amount of delay that this cause introduces) and its associated probability distribution. A non-root node (i.e. a central node) has an associated random variable (i.e. accumulated delay in the process) and a conditional probability distribution for its random variable given the values of the parent random variable(s).

Therefore, a conditional probability distribution can be obtained over every domain, where the state of each variable can be determined by knowing the state of its parents. The joint probability of a set of variables D can be computed by applying the "chain rule" (Pearl, 1985): $\mathrm{P}(\mathrm{D})=\mathrm{P}\left(\mathrm{D}_{1}, \ldots, \mathrm{D}_{\mathrm{n}}\right)=\mathrm{P}\left(\mathrm{D}_{\mathrm{n}} /\right.$ parents $\left.\left(\mathrm{D}_{\mathrm{n}}\right)\right) \cdot \ldots \cdot \mathrm{P}\left(\mathrm{D}_{2} / \mathrm{D}_{1}\right) \cdot \mathrm{P}\left(\mathrm{D}_{1}\right)$.

The BNs for this paper were constructed using the Netica ${ }^{\mathrm{TM}}$ program (Norsys, 2015), which is limited to discrete variables. Therefore, the states of the different nodes represent the amount of delay: none $(\Delta t \leq 0 \mathrm{~min}),(0 \mathrm{~min}<\Delta t<20 \mathrm{~min})$ and $(\Delta t>20 \mathrm{~min})$ (i.e. in the case of lateral nodes it is the delay that the node introduces, whereas for central nodes this is the delay the node accumulates with respect to the scheduled time). Interval ranges were selected to represent the dispersion of the sample data (see Section 3.1). The initial BN model

structure (Figure 12) was constructed for a generic example, using expert judgment, but it could be modified depending on the available data, the particular airport layout or the operational configuration and standards. We then carried out a statistical significance test on pairs of nodes connected by an arc in the expert-elicited BN. Associations between the nodes were statistically significant at level 0.05 (p-value test).

This delay propagation model has several practical applications:

- Forward Inference (predictive inference from causes to effects). The inference reasons from new information about causes to new beliefs about effects, following the directions of the network arcs. This approach can be used to identify the expected final delay $(\Delta t>0)$ for a flight leaving the E-TMA, when an internal process (or a delay inherited from a previous leg) has introduced a delay to the system (assuming delay propagation through the network). This information may be used by operators and policy makers to decide how the buffer time and E-TMA rotation (resource allocation) should be managed (in a tactical phase) to ensure that delays are absorbed. When data on the initial (and reactionary) causes of delay has been collected in real time (indicators) the objective of the model is to predict the most likely delay at departure, so that E-TMA rotation can be managed dynamically.
- Backward Inference (diagnostic inference from effects to causes). The inference reasons from symptoms to cause. Note that this reasoning occurs in the opposite direction to the network arcs. This approach can be used to calculate the likelihood of an internal process being delayed $(\Delta t>0)$ when the departure of a flight has a registered delay (it enables the most likely causes of the final delay to be identified). This information may be used by operators and policy makers to reduce inefficiencies by identifying delay amplifiers (operational improvements). The propagation model will evolve and learn with new data (optimisation of operational processes).

The model allows different what-if scenarios to be tested.

Figure 13 gives an example of how a delay due to Reactionary, ATC/ATFCM, Airport Management, Weather, Cargo and Passenger \& Baggage Processes (shaded nodes) is propagated through the network (it predicts the $\Delta t$ at exit given an initial $\Delta t>0$ at the entrance). By assigning delay values (probabilities) to these nodes (input data), it is possible to obtain a distribution of the estimated delays throughout the processes at the E-TMA. An inherited delay from the previous legs of a flight (Reactionary node) is added to the ATC/ATFCM delay in the Airspace Arrival and Airside Arrival nodes. However, the Airport Management node performs optimally, so the accumulated delay is almost mitigated in the Landside node. Finally, the ATC/ATFCM delay also affects the rotation processes and, by impacting on the Airside Departure and Airspace Departure nodes, introduces the likelihood of an outbound delay. This scenario is an example of inter-causal inference (between parallel variables): the inference reasons about the mutual causes (effects) of a common effect (cause).

![img-12.jpeg](img-12.jpeg)

Figure 13 - Delay propagation (Example 1)

Figure 14 shows the most influential players in a possible process to mitigate a flight delay. The network is set (input data) to provide zero delay in the final step (Airside Departure node). The values that feed the model (shaded nodes) represent the cumulative delay of the different processes that make up the E-TMA rotation. The delay in the Airspace Arrival node is a combination of the delays in $A T C / A T F C M$ and Reactionary nodes. The mitigation process is possible due to the "limited" delay at Cargo, Passenger \& Baggage Processes and the cohesive node Airport Management: these nodes act as delay "reducers" by absorbing delay (performing optimally $[\Delta t=0]$ or better than expected $[\Delta t \leq 0]$ ).
![img-13.jpeg](img-13.jpeg)

Figure 14 - Delay propagation (Example 2)

Finally, Figure 15 analyses how delays within the E-TMA network can be generated. This

is the reverse situation in which $\Delta t$ at the entrance nodes is predicted when $\Delta t>0$ at the exit. The central nodes are set so that the delay increases as the operation progresses. The flight does not accumulate previous delays (Reactionary has a strong tendency to zero), and Airport Management, Cargo and Passenger \& Baggage Processes also introduce very limited delay. Therefore, in this case, ATC/ATFCM procedures and Weather are the main causes for amplifying delays through the network.
![img-14.jpeg](img-14.jpeg)

Figure 15 - Delay propagation (Example 3)

This model enables airport planners and policy makers to dynamically manage the tactical phase. When the system receives reactionary or primary delays (or performs inefficiently), this tool estimates where resources should be allocated (processes) and how buffer time should be determined to absorb delays.

# 2.4 Indicators for evaluating the influence of delays on the system 

ICAO (2009) established the foundations with regard to punctuality and predictability indicators in aviation. The generally accepted key performance indicator (KPI) for operational air transport performance is 'punctuality', which can be defined as the proportion of flights delayed by more than fifteen minutes compared to the published schedule (Jeztki, 2009). The fifteen-minute threshold for defining arrival and departure delay has historically been common to both Europe and the US (Cook et al., 2012 and Sherry et al., 2008). SESAR's Performance Targets (SESAR, 2014) significantly refined this approach to delay measurement, by developing new parameters, indicators and targets.

Cook et al. (2012, 2011) and EUROCONTROL (2011) showed that, although delay propagation remains a significant and costly operational challenge to ATM, there is a significant absence of metrics that specifically measure this problem. The classical approach for delay metrics (that reduced the indicators to time intervals between scheduled flight times

and actual operations) was enhanced by Cook et al. (2015) and Gulding et al. (2013), who developed a framework for complexity and new metrics as regards ATM.

For the purposes of this paper, we developed an influence diagram that relates potential delays and the system's response. Influence diagrams offer an intuitive way to identify and display the essential factors that have a, positive or negative, impact on the achievement of a given objective (Katsaros et al., 2013).

The diagram (Figure 16) shows that the main parameters influencing delay reduction are the delays themselves (coming from inefficiencies in the processes or due to external causes) and the mitigation drivers, which affect the reduction of the different delays. All delays (internal and external) are included in the efficiency assessment, as the main goals are to reduce total delay and to limit it to a particular threshold (adjust buffer time) by improving the E-TMA rotation processes (operations management). The influence diagram was constructed with the help of stakeholders expert in E-TMA operations (see development of the BPM in Section 2.1).

The main recovery strategies considered were chosen as a result of a study of the processes (BPM diagram) and the input of stakeholders:

- Reduction of delays due to late changes in the scheduled rotation sub-processes (onground turnaround and ATC processes).
- Accommodation of schedule changes without increasing delays.
- Improvements in gate and resource allocation at short notice.
- Improvements in operations when infrastructure/resources are not available at short notice.

EFFICIENCY
![img-15.jpeg](img-15.jpeg)

[^0]
[^0]:    This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NCND 4.0).

# Figure 16 - Efficiency and flexibility as they relate to delay propagation 

Finally, Table 4 lists the main drivers and indicators used when assessing efficiency and flexibility as they relate to delay propagation.


Table 4 - Performance drivers and indicators

## 3. FINDINGS

To tackle the problem of uncertainty in airport operations, in this paper we first analysed the different agents, processes and facilities (architecture) involved in the system (within the ETMA boundaries) and the dependencies between them. We then characterised potential delays, identifying what processes and elements are impacted by each type of delay. Finally, we designed a model for incident propagation and measurement (indicators).

The proposed model can perform a large number of what-if scenarios (forward, backward and inter-causal inference). By setting the value (probabilities) of some nodes, it provides updated probability distributions of other nodes. Therefore, it reduces uncertainty, by illustrating how different system and external variables interact to cause, amplify or mitigate delays. Specifically, it allows us to calculate the probability of delays, failures and

inefficiencies being amplified (and to what extent) through the airport operations network (forward analysis). This may be used to establish the required buffer time at E-TMA rotation, and to effectively allocate resources in order to improve operations (flexibility - punctuality). It also enables us to infer the most probable causes of delay (backward analysis) and to determine which elements of the system are not contributing to its absorption (locate inefficiencies).

# 3.1 Practical approach and model validation 

In order to validate the propagation model, the BN model had to be supplied with empirical data, to enable it to learn, amend its structure and improve the accuracy of estimations. Therefore, the initial model was tested with data from observations made at Adolfo Suárez Madrid-Barajas Airport in 2014, as well as data on flight schedules with primary delays provided by the Central Office for Delay Analysis (CODA) of EUROCONTROL (2015d). We also included flight data from FlightStats (2014) and Sabre (2014) in the analysis. Madrid airport is large in terms of passengers and aircraft movements (41,833,686 passengers and 342,604 aircraft movements in 2014, according to AENA (2016)). Therefore, there were sufficient operations during the observation period.

A set of 150 turnaround operations (E-TMA rotation) was used to statistically determine process characteristics with respect to delays (data from July to September in 2014 using simple random sampling). The initial dataset was refined by considering only flights (inbound and outbound) with a flight time of less than 120 min (short- and mid-range), in order to ensure effective rotation procedures. For a hub like Madrid, the scheduled on-ground turnaround time for flights such as these is equal to or less than 75 minutes (Fricke and Schultz, 2009). A sub-sample of $90 \%$ of the observations was selected to build the model structure and to estimate parameters (a test sample to establish the model's ability to explain delay propagation). The remaining $10 \%$ of the data was set aside to test the accuracy of the predictions made by the model (a sample to test the model's predictive capacity). The data gave an average delay per departure of 10 min , with 27 min as the average delay for delayed departures and almost $30 \%$ of flights delayed on departure ( $\geq 5 \mathrm{~min}$ ).

We also analysed data on the individual delays of each partial process to allow us to review and correlate the rotation times. We constructed a regression model and evaluated each phase. The dependent variable was the delay at the given phase. The independent variables were the delays from previous phases and other explanatory variables identified in Section 2.2 .

There were two main difficulties with the preliminary validation of the model:

- Firstly, the structure of the model had to be adapted to the existing data and to the particular operating configuration of the airport, resulting in a variation from the general BN structure (Figure 17). This is an important feature of the model as it can be adapted to

different situations depending on the available data or the specific layout of airport in question. The principal changes were related to the absence of data on Cargo processes and the separation of the $A T C / A T F C M$ node into two new nodes: ATC Arrival and ATC/ATFCM Departure (due to their distinct impact on inbound and outbound flights). Finally, these two nodes (ATC Arrival and ATC/ATFCM Departure) were adapted to introduce the direct influence of Weather (this modification arose as a result of analysis into dependence between between causes of delay).

- Secondly, the program used (Netica) is limited to discrete variables. Therefore, we discretised the data in line with the findings of past studies (Laskey et al., 2006; Xu et al. 2005 and Dougherty et al., 1995). Nevertheless, some information may have been lost in the discretisation process, as air traffic delays are better modelled as continuous variables ( Xu et al., 2005).

To construct the simplified model, we carried out the following steps for each rotation element (Airspace Arrival, Airside Arrival, Landside and Apron, Airside Departure and Airspace Departure):

- Identified the most important explanatory factors vis-à-vis delays using the findings of Section 2.2, regression analysis and cross validation of the data in the test sample (correlation and causality between nodes).
- Created a node in the BN structure to represent the rotation element (central nodes).
- Defined the explanatory factors vis-à-vis delays (lateral nodes) as the parent nodes of the given process node.
- Estimated the initial local distributions for the given node by discretising the regression model. In other words, the child node was modelled as normal distribution with a mean equal to the regression mean and a standard deviation equal to the standard deviation of the regression. The delay variables were discretised in 20 min intervals.
![img-16.jpeg](img-16.jpeg)

Figure 17 - Modified BN structure used for the initial validation

We then carried out a preliminary test to validate the model, using a small set of data. In order to improve its accuracy, the model requires more complete and representative data and an improved methodology (especially in regard to the probability distribution of delays).

- Scenario 1 (forward inference): Figure 18 and Table 5 represent the probability of experiencing delay at the system exit (Airspace Departure), when there is only Reactionary delay. The model shows that when reactionary delay (due to the previous leg) is zero (state 1.1 in Figure 18 and Table 5), the system itself introduces a certain amount of delay (due to operational inefficiencies or resonances). When reactionary delay increases (states 1.2 and 1.3), the system is able to absorb part of the inherited delay (the mitigation capacity decreases as reactionary delay increases).
![img-17.jpeg](img-17.jpeg)

Figure 18 - Sensitivity of exit delay to Reactionary delays


Table 5 - Conditional Probability Table (CPT) for Scenario 1

- Scenario 2 (inter-causal inference): Figure 19 represents the probability of experiencing delay at the system exit (Airspace Departure), when there is both Reactionary and ATC Arrival delay. Again, the model shows that when no delay enters the system (state 2.1), then the system itself introduces a certain amount of delay (inefficiencies). Furthermore, when reactionary and primary delay increase (states 2.2 to 2.9), the system is still able to absorb the inherited delay to some extent (the mitigation capacity decreases as reactionary and primary delay increase). Table 6 summarises the different states analysed in Scenario 2.

![img-18.jpeg](img-18.jpeg)

Figure 19 - Sensitivity of exit delay to Reactionary and ATC Arrival delays


Table 6 - Propagation states tested in Scenario 2

- Scenario 3 (inter-causal inference): Figure 20 represents the probability of experiencing delay at the system exit (Airspace Departure), when there is Reactionary delay and ATC/ATFCM Departure delay. In this case, the model shows that when no delay enters the system, the system itself introduces some internal delay (state 3.1). However, in this case the ability of the system to mitigate the inherited reactionary and primary delays is much more limited than in previous cases. This is due to the fact that, in this case, primary delay occurs in the latter stages of the process, when there is less likelihood of recovery. Table 7 gives the different states analysed in Scenario 3.

In the scenarios tested Reactionary, ATC Arrival and ATC/ATFCM Departure were selected as the main causes of delay, as the initial regression analysis showed that they are the most representative explanatory factors (representing more than $50 \%$ of registered delays). Past studies agree with this conclusion (Fricke and Schultz, 2009).

![img-19.jpeg](img-19.jpeg)

Figure 20 - Sensitivity of exit delay to Reactionary and ATC/ATFCM Departure delays


Table 7 - Propagation states tested in Scenario 3

- Scenario 4: This scenario uses backward analysis to identify the probable causes of a delay at the system exit (backward inference). For a delay ( $\Delta t>20$ ) at the system exit (Airspace Departure), Figure 21 gives the probability of the main causes (Reactionary, ATC Arrival or ATC/ATFCM Departure) introducing delay to the system.
![img-20.jpeg](img-20.jpeg)

Figure 21 - Backward analysis to identify critical phases and delay amplifiers

The scenarios tested provided promising results regarding the model's ability to reduce uncertainty (by explaining system performance and predicting delay propagation). The test error ranged from $15 \%-35 \%$, and the average value was $22 \%$.

# 4. APPLICATIONS \& LIMITATIONS OF THE MODEL 

The aim of operational analysis of airports is to:

- Achieve a comprehensive understanding of operations,
- Detect possible incidents or irregularities that may occur during processes, and
- Define and describe the different operational actions that may be carried out to correct the inefficiencies identified.

In line with these objectives, this paper provides a tool that enables planners to investigate the impact of changes in tactical decisions and policies on the management and propagation of delays in the E-TMA system.

Departure delays arise for a variety of reasons such as inherited arrival delays, delayed ETMA processes (ground and air) and/or disruptions in E-TMA processes. Interdependencies exist and may affect the delay chain, for example, an existing delay may result in an even bigger follow-up delay due to scarcity of resources at the airport. On the other hand, delays may be partially compensated by improved efficiency in E-TMA rotation.

For policy makers and airport managers, the main applications of this study relate to uncertainty reduction and are as follows:

- The operations framework and taxonomy may be used to classify airport processes in the E-TMA, which is helpful when optimising operations and performance.
- The propagation model and the proposed indicators may be used by the regulatory agency to ensure that all agents collaborate in reducing delays, guaranteeing some target levels of efficiency.
- Using "Forward" analysis it is possible to estimate the final departure delay (settlement of buffer time and optimal rotation times).
- Using "Backward" analysis it is possible to identify the main contributors (causes) to a final delay (locate inefficiencies).

The principal limitations of the study are that:

- All of the information used to construct the conceptual framework for airport operations (E-TMA rotation) and build the delay propagation model, and all of the data used to test the model, comes from Spain. To ensure that the model is universally valid it would need to be tested in other geographical scenarios. However, given the airport privatisation process currently underway in Spain, the model may still be immediately useful for policy makers.

- Although the initial results appear to be promising, there are a number of methodological issues that need to be addressed in order to improve the accuracy of the predictions and the explanatory ability of the model. Specifically, the model needs to be tested using more complete data and from more than one airport. The discretisation strategies for probability distribution must be improved and process interdependencies need to be identified more precisely. Also, the characterisation of the delays has to be refined.


# 5. CONCLUSIONS 

This paper proposes a new Uncertainty Reduction Model to deal with delay propagation at airports (E- TMAs). We considered E-TMA operations holistically by including all relevant stakeholders, architecture (facilities) and processes. We then combined the framework for the airport operations network with a predictive probabilistic model, which enabled us to estimate delay amplification or reduction (forward analysis) through internal processes at ETMA. Specifically, we characterised and forecast the propagation of delays across the network due to reactionary delays, primary delays and internal inefficiencies. We also used the model to estimate the principal contributors to delay in the event of a departure delay (backward analysis).

We used Business Process Modelling to organise the different events that make up the ETMA rotation process. By combining this with expert judgment techniques, observations and a literature review, and using Unified Modelling Language we produced a diagram (and suggested taxonomy) to give us an overview of all of the elements, procedures and agents in the airport operations network.

We used Bayesian Networks to investigate the causal factors that contribute to delay, and to analyse the influence of each phase on the final departure delay. The proposed model enables us to understand how delays are propagated through E-TMA operations, what the main delay drivers are, what effects delays have on different processes and how delay propagation is likely to happen.

The theoretical Bayesian Network model was constructed with the help of expert opinions and, therefore, the network can be improved by supplying it with new data. Moreover, the model can be modified in order to adapt its structure (nodes, variables and arcs-interactions) to different airport layouts and operational requirements.

Results from a case study on Adolfo Suárez Madrid-Barajas Airport demonstrate the ability of the model to predict delays and explain the performance of the airport operations network. The airport system is capable of mitigating moderate reactionary delays (inherited delays from to a previous flight leg). Furthermore, when a primary delay (that occurs at the initial stages of rotation) is added to reactionary delay, the system still has some ability to absorbing delays, albeit to a lower extent. Nevertheless, when a primary delay is added in the latter

stages of rotation, the network has a limited ability to mitigating the delay, which is usually amplified. Finally, when there are no inherited delays, the system itself introduces a certain amount of delay (due to operational inefficiencies or resonances).

Future work needs to focus on improving the accuracy of the model (more complete testing data and methodological improvements), and to assess whether the model is suitable for use in other airports. We also need to analyse potential response strategies (reduce delays in some process nodes in order to mitigate inefficiencies and optimise operations), and apply the propagation model to other types of incidents (not just delays).

# ACKNOWLEDGEMENTS 

The authors want to express their heartfelt thanks for the insightful ideas, notable contribution and significant collaboration of the academics, organisations, experts and members of the industry, who so openly offered their assistance, help and data.
