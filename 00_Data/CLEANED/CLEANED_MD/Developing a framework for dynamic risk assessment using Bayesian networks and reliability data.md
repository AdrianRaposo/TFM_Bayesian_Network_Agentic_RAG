# 19 $^{\text {th }}$ Annual International Symposium October 25-27, 2016 ・ College Station, Texas 

## Developing a Framework for Dynamic Risk Assessment Using Bayesian Networks and Reliability Data

Rym Kanes ${ }^{\mathrm{a}^{*}}$ and Clementina Ramirez-Marengo ${ }^{\mathrm{b}}$, Hazem Abdel-Moati ${ }^{\mathrm{a}}$, Jack Cranefield ${ }^{\mathrm{a}}$ and Luc Véchot ${ }^{\mathrm{b}}$<br>${ }^{a}$ ExxonMobil Research Qatar Science and Technology Park, PO Box 22500, Doha, Qatar<br>${ }^{\mathrm{b}}$ Mary Kay O'Connor Process Safety Center at Qatar, Texas A\&M University at Qatar, PO Box 27874, Doha, Qatar<br>* Corresponding author: rym.kanes@exxonmobil.com


#### Abstract

Process Safety in the oil and gas industry is managed through a robust Process Safety Management (PSM) system that involves the assessment of the risks associated with a facility in all steps of its life cycle. Risk levels tend to fluctuate throughout the life cycle of many processes due to several time varying risk factors (performances of the safety barriers, equipment conditions, staff competence, incidents history, etc.). While current practices for quantitative risk assessments (e.g. Bow-tie analysis, LOPA, etc.) have brought significant improvements in the management of major hazards, they are static in nature and do not fully take into account the dynamic nature of risk and how it improves risk-based decision making


In an attempt to continually enhance the risk management in process facilities, the oil and gas industry has put in very significant efforts over the last decade toward the development of process safety key performance indicators (KPI or parameters to be observed) to continuously measure or gauge the efficiency of safety management systems and reduce the risks of major incidents. This has increased the sources of information that are used to assess risks in real-time. The use of such KPIs has proved to be a major step forward in the improvement of process safety in major hazards facilities. Looking toward the future, there appears to be an opportunity to use the multiple KPIs measured at a process plant to assess the quantitative measure of risk levels at the facility on a time-variant basis.

ExxonMobil Research Qatar (EMRQ) has partnered with the Mary Kay O'Connor Process Safety Center - Qatar (MKOPSC-Q) to develop a methodology that establishes a framework for a tool that monitors in real time the potential increases in risk levels as a result of pre-identified risk factors that would include the use of KPIs (leading or lagging) as observations or evidence using Bayesian Belief Networks (BN).

In this context, the paper presents a case study of quantitative risk assessment of a process unit using BN. The different steps of the development of the BN are detailed, including: translation of a Bowtie into a skeletal BBN, modification of the skeletal BN to incorporate KPIs (loss of primary containment (LOPC), equipment, management and human related), and testing of the BBN with forward and backward inferences. The outcomes of the dynamic modeling of the BN with real time insertion of evidence are discussed and recommendation for the framework for a dynamic risk assessment tool are made.

Keywords Bowtie analysis, Bayesian Networks Applications, Reliability, Process Safety Performance Metrics

# 1 Introduction 

Chemical process industries are complex networks that involve various equipment and control loops, along with skilled operators all working together to harmonize production throughout the process lifecycle. In order to ensure smooth operation, it is necessary to understand the hazards and risks associated, as well as any possible accident scenarios and their mitigation. It follows that the dynamic nature of these chemical processes extend to their accompanying risks as seen in Figure 1. Risk levels in a process facility tend to fluctuate due to several time-varying factors including: variations in the integrity and vulnerability of safety barriers, equipment aging, planned activities and maintenance, shutdown, start-up, simultaneous operations, changes in the safety culture of the company, health and efficiency of the management system, commitment to safety of the leadership and process safety incidents (incidents or near misses).

It is important to quantify these time-dependent factors and their relationships using engineering and mathematical techniques, in order to develop quantitative estimates of risk that are then compared to some defined risk criteria that translates a company's risk tolerability. Traditional quantitative risk assessment (QRA) methods include HAZOP, What-if Analysis, Bow-Tie Analysis, Fault and Event Trees, Layer of Protection Analysis (LOPA). However, these methods are limited in that they tend to convey static values of risk at a given time and are simply not designed to capture the dynamic nature of risk. It is therefore important to focus research on this area of dynamic risk and its measure, as way forward for improving current risk assessment methodologies.

![img-0.jpeg](img-0.jpeg)

Figure 1. Dynamic behavior of risk

More recently, Bayesian Belief Networks (BNs) which are probabilistic graphical models that allow for the quantification of complex relational dependencies using Bayes' theorem, have gained traction in various engineering fields, including the area of process safety. BNs represent a set of random variables and their relationship through a directed acyclic graph (DAG). Each node of the DAG represents a random variable. The directed arcs connect pairs of nodes which follow a causeeffect relationship. A node is called a "parent node" if there is a directed arc connecting it to another node, the "child node". Nodes which have no parent are known as "root nodes" as seen in Figure $2[1]$.
![img-1.jpeg](img-1.jpeg)

Figure 2. Bayesian network - directed acyclic graph

Probability values are assigned to each node of the BN. The main objective of BNs is to estimate and update the distribution probabilities of the random variables based on given evidence and prior knowledge. The calculation of the probabilities of the "child" nodes are based on a combination of the probability of the "parent" nodes and conditional probability tables according to the wellknown "Bayes rule" of conditional probability. The analysis of the probability associated to the nodes can follow two paths:

- Predictive analysis or forward approach: Probability values are defined a priori for root nodes and calculated by inference for the other nodes.

- Diagnostic analysis or backward approach: Probability values of the nodes are calculated a posteriori when observations become available. For example, BNs therefore provide a method to update our beliefs about the occurrence of an event "A" given the information of an observed event "B".

The way probability nodes are treated in a BN and its capability to represent dependencies between variables and provide updated probability values makes BNs a very interesting method to use real time data to update values of risks in process facilities. Hence, BNs have been applied for risk analysis and decision making and risk management. Weber et al. (2012) conducted a literature review over the application of Bayesian Networks to dependability, risk analysis, risk management and maintenance and showed a raising trend of the literature related to these domains [2]. This increasing trend is due to the advantages that Bayesian Networks provide in contrast to other static classical analysis methods such as fault trees, event trees and Bowties. BNs are also becoming one of the preferred tools for risk management applications [3]

Currently, there has been significant work carried out on the use of BN to overcome the limitations of classical risk analysis. In this context, BNs have been applied for predicting the probability of occurrence of undesired consequences. This application involves the mapping of classical risk analysis techniques such as the Fault Tree (FT), Layer of Protection Analysis (LOPA) and Bowtie into a BN [4].

Khakzad et al. (2011) presented a mapping algorithm to translate a FT into a BN, based on the algorithm developed by Bobbio et. al. (2001) [1]. The resulting BN was used to assess the performance of a feeding control system transferring propane from an evaporator to a scrubbing column [5]. Later, Khakzad et al. (2013) presented a dynamic approach where a bowtie was mapped into a BN. BNs were used to update the probability of occurrence of a vapor cloud explosion based on observed evidence. Evidence such as loss of containment events and near misses registered during 4 years were used to update the probability of a vapor cloud explosion [6].

Cai et. al. (2013) used BNs to perform a risk assessment that takes into account human factors in an offshore blowout scenario. Individual, organizational and group factors were represented in the bowtie that was mapped into a BN [7]. Ayello et. al (2014) applied BNs to assess the of different types of oil pipeline corrosion (Internal, external, stress induced). The variables included in the analysis were soil conditions, wetting and drying cycles, presence of organic decay products, coating types, pipe surface conditions, temperature, cathodic protection, chemistry under coating, etc. $[8,10]$.

Dynamic Bayesian Networks (DBNs) are an extension of BNs where variables are correlated to each other over time steps. DBNs often consist of two different time steps and are called two-timeslice BNs. In a two-time slice BN the value of a variable can be calculated from the immediate prior value (time t-1) at any point in time " $t$. Lately, DBNs have been applied in risk assessment for estimating probabilities over different periods of time. Abimbola et al. (2014) mapped a Bowtie into a DBN in order to gain a real-time estimate of the probability of failure of barriers related to preventing a hydrocarbon blowout, thereby ensuring safe offshore drilling operations [11].

Khakzad (2015) developed a DBN to estimate the propagation of heat radiation in a scenario where one of 3 atmospheric storage tanks containing acetone and benzene is under fire. The BN allowed for estimation of the most probable sequence of events that would result in a domino effect within

the facility [12]. Barua et al. (2016) proposed a Bayesian Network model for dynamic operational risk assessment. The BN model was developed from a dynamic fault tree, where Boolean states (failure and success) were used to indicate the probability of failure of specific process equipment [13]. Later on, Wu et al. (2016) developed a Dynamic Bayesian Network Model (DBN) based on a Bowtie model for predicting the change of the probability potentially hazardous scenarios with time. Boolean states (Yes and No) were used for represent if and event or equipment failure occurs[14].

Current work in the literature demonstrates the capability of BNs for updating the values of risk based on observed evidence. Primarily, the random variables have Boolean states (i.e. failure or success of safety barriers). The type of evidence used for updating was either the observation of equipment failure or consequences over a certain period of time. However, in a process plant many other parameters or process safety indicators (PSIs) can be used as evidence. These indicators could be of different natures, and may include reliability related, operational indicators, human and organizational, demands on safety systems, etc.

The purpose of this work is to develop a framework for a BN that calculates the dynamic risk with time based reliability data (failure rate, probability of failure on demand, time horizon until the next scheduled maintenance, and the characteristic life of equipment) and updates risk based on insertion of evidence such as equipment failures and time to failure (TTF) for continuous operation. The BN will also be used to demonstrate the effect of maintenance on the overall probability of consequences. The BN method used in this study incorporates the use of both Boolean and continuous random variables, as well as the Boolean and continuous causal relationships between them, which is one of the main differences between this work and others within this field. A proprietary Bayesian Networks software was used for the estimation of updated probabilities. This work is a collaborative effort between ExxonMobil Research Qatar and the Mary Kay O'Connor Process Safety Center at Texas A\&M University in Qatar and aims to establish the framework for developing a dynamic risk assessment tool to determine the current risk level for a given process area or facility.

# 2 Reliability Modeling 

Over the last decade the process industry put very significant efforts in the development of process safety key performance indicators (KPIs) (or parameters to be observed) to continuously monitor the health of safety management systems, the integrity of safety barriers and reduce the risk of major incidents [15,19]. However, there still seems to be no clear links between the multiple parameters measured at a process plant and the quantitative measure of risk levels (through a QRA) at the facility.

Monitoring meaningful reliability indicators drive an increment in equipment and active safety barriers reliability. Reliability and risk are linked, increasing reliability can reduce the risk of undesired events in process facilities. The term reliability is associated to the probability that equipment or a system will perform as intended for a specific time horizon. Whereas, the probability that a piece of equipment or a system will fail at a given time is known as probability of failure. The probability of failure can be assessed through different parameters and functions such as the time to failure and the failure rate function.

The time to failure (TTF) is the time elapsing from when a piece of equipment/safety barrier are put into operations until they fail for the first time [20]. TTF is a random variable that can be

represented through probability distributions. The failure rate function is related to the time to failure probability distribution and it provides an estimate on how the probability of failure of equipment changes over time. The failure rate can be considered as constant or time dependent.

The failure rate time-dependency is well represented by the so-called bathtub curve as seen in Figure 3. The bathtub curve profile represents the three stage of the life cycle of equipment or safety barriers: wear-in, useful life and wear-out modes. The wear-in mode has a decreasing failure rate and it well represents the early stages of the lifecycle of equipment (where it can fail mainly due to the manufacturing defects). The useful life accounts for failures caused by random events; in this mode, the failure rate is constant. The wear-out mode represent the failures caused by equipment aging.
![img-2.jpeg](img-2.jpeg)

Figure 3. The bathtub curve
Equipment and safety barriers in process plants are at different stages of their life cycle. Hence, when moving towards a dynamic risk assessment it is critical to address the characteristic stage of the lifecycle of these barriers. In system reliability, the Weibull distribution is widely used for modelling each one of the lifecycle stages of equipment. This probability distribution is a function of two different parameters: shape and scale. The shape parameter ( $\beta$ ) indicates the stage of the lifecycle of equipment, where $\beta<1$, represents the wear-in stage, $\beta<1$ represents the useful life, $1<\beta<4$ represents the wear-out stage, and $\beta \geq 4$ represents the rapid wear-out stage. On the other hand, the scale parameter is an indicator of the failure rate per hour of equipment/safety barriers [20].

# 3 Framework for Dynamic Risk Assessment 

The proposed methodology is comprised of different steps for the construction of a DBN with discrete-continuous variables as seen in Figure 4. The resulting BN is called a hybrid (discretecontinuous nodes) DBN and it can be constructed from an existing bowtie diagram by mapping the fault tree (FT) and event tree (ET).

![img-3.jpeg](img-3.jpeg)

Figure 4. Framework for performing a dynamic risk assessment using BN

# 3.1 Development of the Skeletal BN 

In order to develop the skeletal BN, an algorithm exists to map a fault tree into a BN, including graphical and numerical translation of the fault tree. Graphically, the structure of the BN is developed from the fault tree such that the top event and the causes shown in the fault tree are represented by nodes and arcs in the BN. The relationships within the causes and the top event in the fault tree are modeled with two types of gates: OR Gate and AND Gate. According to the type of gate, conditional probabilities are assigned to each one of the nodes as seen in Figure 5.
![img-4.jpeg](img-4.jpeg)

Figure 5. AND/OR gates conditional probability tables

The procedure of mapping a FT into a BN consists of a nodal representation of each safety barrier of the FT in the BN. Each of the nodes will have two possible states: failure or success. A nodal representations of the consequences (from ET) was used as well. The consequence node has many states, each one of them representing the possible consequences shown in the ET.

# 3.2 Modification of the BN to Incorporate Reliability Data 

For equipment that operates continuously, it is important to consider different parameters such as the probability of failure within a specified horizon " $t$ " (i.e. the time before the next inspection/preventive maintenance) and the time to failure (TTF) for equipment under continuous operation. The TTF for equipment can be represented by continuous probability density functions such as the Exponential, Weibull or Gamma Distribution. In this work, nodes represented by continuous distributions are introduced into the BN. Therefore, the resulting BN is a hybrid type with a mixed of continuous- discrete nodes.

For equipment still in the useful life stage, the time to failure can be calculated as the inverse of the constant failure rate of a system, equipment or safety barrier. On the other hand, for cases where the failure rate is time dependent (for equipment during the wear-in and wear-out stages its lifecycle), the Weibull distribution with appropriate shape parameters can be used.

The simple mapping of a bowtie described earlier cannot be used when continuous nodes are introduced into the BN. In order to build the hybrid BN, deterministic functions are used as conditional node probability tables for translating the OR and AND gates. These functions are summarized in Table 1 [21]. After the continuous TTF distributions and the deterministic functions for the AND/OR gate are provided as inputs into the BN nodes, the probability of failure for each continuous node can be computed.

Table 1. AND/OR gate functions for continuous TTF distributions


# 3.3 Creation of the DBN 

To transform the hybrid BN into a hybrid DBN, it is necessary to modify the structure of the BN for discrete nodes as follows:

- Identification of the parent nodes in the BN
- Creation of prior and posterior nodes for each parent nodes.

Connected prior and posterior nodes associated to a given parent node are used to capture the change of probability with time. For each time step, evidence is first set and the posterior probability values of each node are calculated, given the inserted evidence and the prior probability value of the node.

### 3.4 Evaluation of the Dynamic Risk Profile

## As a function of time

Continuous probability distributions are used to represent the TTF of equipment under continuous operation can be included in the BN. The probability of the consequences is calculated for different specified time horizons $t$ (i.e. the probability of the consequences if no inspection/maintenance are given in a period of 3 months, 6 months, etc.). The different specified time periods are 1, 3, 6, 9, 12,15 and 18 months.

## As a function of time and insertion of evidence

Continuous probability distributions are used to represent the TTF of equipment under continuous operation, and can also be included in the BN. The probability of the consequences is calculated for different specified time horizons $t$ (monthly time intervals can be used). In addition, evidence of failure of equipment is inserted every month for the sake of simplicity (other time units can be used). Thus, the risk profile is generated taking into account the effect of time and the observed evidence.

## 4 Case Study

This section presents a case study that applies the proposed framework for a dynamic risk assessment using Bayesian Networks. The scenario of choice is an extension of the case study performed by M. Tweeddale, Managing Risk and Reliability of Process Plants, Gulf Professional Publishing, 2003 [22], which focused on the heating oil section of a plant delivering hot oil to

heating coils of bitumen tanks. The oil is returned to the bitumen tanks by the circulating pump through a gas-fired heater.

The flow should be controlled through the heater, or the heater coils may overheat and rupture, resulting in a large fire. The flow control system is composed of a transducer (FE), a flow controller (FC) and a flow control valve (FCV). A manual bypass valve (MBV), which normally remains in a closed position, is used if FCV is down for routine maintenance. If the flow of the heating oil is below the desired level, the solenoid valve (SV) will be activated by the signal of the transducer FE and the temperature control valve (TCV) will be closed. The flow switch activates the lowflow alarm (FAL), to alert the operator for opening the MBV or closing the manual gas isolation valve (GIV). In addition to the flow control system, a high-temperature switch (TSH) is placed in the oil delivery line. In case an increased temperature is measured by the TSH, it will activate the solenoid valve SV and close the temperature control valve [22].

The corresponding bowtie diagram was constructed with the Heater Coils Burn Out as the Top Event, and is shown in Figure 6. In this example, the possible consequences, as seen in Table 2, depend on different factors: i) if the leaking oil finds an ignition source, the leak is isolated very quickly and ii) if the oil contacts operator.
![img-5.jpeg](img-5.jpeg)

Figure 6. Heater coils burn-out scenario - Schematic Bowi

Table 2. Possible Consequences


The probability of failure values mentioned in Table 3, which were used for constructing the BN, were taken from the original case study [22]. The BN obtained from mapping the bowtie is shown in Figure 7, while the estimated values of the probability consequences are summarized in Table 4, and These results are the initial values of risk obtained by mapping the traditional bowtie in a BN and do not include any updates on probability values.

Table 3. Probability of failure of equipment and safety barriers


![img-6.jpeg](img-6.jpeg)

Figure 7. Resulting BN from mapping the Bowtie

Table 4. Initial values of the probability of the consequence


# 4.1 Modification of the BN to Incorporate Reliability Data 

The following reliability data is incorporated into the BN:

- The time to failure of equipment operating continuously
- The horizon time until next maintenance is schedule $t$
- Failure rate
- The characteristic stage of equipment
- Probability of failure for equipment which works upon demand

The BN was modified to incorporate the use of TTF distribution. A Weibull distribution is used for representing the TTF distribution of the pump, FE and FS. The Weibull distribution parameters were taken from available literature data of equipment failure rates in the useful life as seen in Table $5[23]$.

Table 5. Equipment/Safety barriers Weibull distribution parameters


When using TTF continuous distributions, the conditional probability tables (CPTs) are obtained as deterministic functions of the parents. The probability of failure of the system at a given time, $t$, can be obtained from the TTF distribution e.g. $P\left(\right.$ Pump $=$ Fail $)=P\left(T T F_{\text {Pump }} \leq t\right)$. The resulting BN will be hybrid with both continuous (time-dependent variables) and discrete variables (probability of success/failure) as seen in Figure 8. The TTF distribution functions for the AND/OR gates CPTs and the probability of failure functions are summarized in Table 1.

![img-7.jpeg](img-7.jpeg)

Figure 8. Hybrid BN with continuous TTF distributions

# 4.2 Evaluation of the Dynamic Risk Profile 

## Evaluation of the risk increment as a function of time

Continuous TTF distributions for the pump, FE and FS are included in the BN. The probability of the consequences if no inspection/maintenance was calculated for these specified intervals of time, $t: 1,3,6,9,12,15$ and 18 months.

## Evaluation of the risk increment as a function of time and the insertion of evidence

Continuous TTF distributions for the pump, FE and FS are included in the BN. The probability of the consequences was calculated for these specified intervals of time, $t: 1,2$ and 3 months. In addition, evidence of equipment failure is inserted as described in Table 6. The modified BN with the insertion of evidence can be seen in Figure 9- Figure 11.

Table 6. Observed evidence


![img-8.jpeg](img-8.jpeg)

Figure 9. BN with SV failure used as evidence
![img-9.jpeg](img-9.jpeg)

Figure 10. BN with FE failure (after 1440 hours of operation) used as evidence

![img-10.jpeg](img-10.jpeg)

Figure 11. BN with pump failure (after 2160 hours of operation) used as evidence

To obtain the dynamic risk profile, the calculation of updated risk values, based on observation or evidence, over time is necessary. For equipment with discrete nodes, this requires a two-step process which includes:

- The insertion of evidence in the BN and the recalculation of the probability of the nodes (variables) of the BN given equipment failure evidence.
- The calculation of the probability of each node of the BN at a given time step given the probability of the node at the previous time step. The conditional probability values for posterior nodes are presented in Table 7 and were obtained from expert judgment. For the sake of simplicity, the same conditional probability table (CPT) was used for each one of the parent nodes. CPTs can be assigned based on expert opinion or literature data if available.

Table 7. CPT for posterior nodes calculation


Figure 12 shows how prior and posterior nodes are connected to capture the change of probability with time. For each time step, evidence is first set and the posterior probability values of each node is calculated given the evidence and the prior probability value of the node.

![img-11.jpeg](img-11.jpeg)

Figure 12. Prior and posterior nodes associated to a given parent node

For equipment, it was assumed that once a failure occurs, the equipment is repaired and it returns to an "as good as new" condition.

# 5 Results 

For comparison purposes, the initial risk values (at time 0 ) were estimated using two modeling approaches: a discrete BN and a hybrid BN Figure 13. The obtained results show that when TTF continuous distributions (hybrid BN) are included into the BN, the initial predicted risk values are lower by three orders of magnitude for the consequences, when compared to values obtained by using just discrete nodes (discrete BN). The difference among the predicted values can be explained by the fact that the probability of failure of equipment/safety barriers increases as function of time and thus, lower probability values would be expected at early stages of a plant. The calculated values are summarized in Table 8.
![img-12.jpeg](img-12.jpeg)

Figure 13. Probability of the consequences for discrete and hybrid BNs

Table 8. Initial probability of the consequences for the Discrete and Hybrid BNs


In addition, by incorporating TTF continuous distributions, risk can be calculated as a function of time for the case where no inspection or maintenance is provided as shown in Figure 14 and Figure 15. The calculated values are summarized in Table 9. For example, if no maintenance is scheduled in 3 months, the value of the probability of the consequences increases by almost three order of magnitudes for each one of the possible consequences. Thus, predicting the risk increase becomes highly important as this information can be used in decision-making to optimize the time intervals between inspection and preventive maintenance.
![img-13.jpeg](img-13.jpeg)

Figure 14. Risk as a function of time

![img-14.jpeg](img-14.jpeg)

Figure 15. Probability of the consequences as a function of time

Table 9. Probability of the consequence values as a function of time


When equipment failure information is inserted as evidence in addition to the effect of time, the predicted values of risk increase considerably in various order of magnitude. For example, the probability of the most severe consequence "C3-Operator burnt, major plant damage", went from $2.1236 \times 10^{-6}$ to $1.9458 \times 10^{-1}$, after the failure of the pump and the flow control components. The obtained dynamic profile is shown in Figure 16 and the increasing risk values can be observed in Figure 17. The obtained values for the probability of the consequences are summarized in Table 10 .

![img-15.jpeg](img-15.jpeg)

Figure 16. Risk profile as a function of time and insertion of evidence
![img-16.jpeg](img-16.jpeg)

Figure 17. Probability of the consequences as a function of time and the insertion of evidence

Table 10. Probability of the consequences as a function of time and evidence


# 6 Conclusions 

The application of Bayesian Networks provides several advantages towards the development of a tool for real-time risk assessment due to their capability for updating probability values given observations. This property of BN can be used to overcome the limitations of current QRA techniques which are static in nature and does not provide a real-time estimation of risk.

Measuring meaningful reliability indicators improve the performance of equipment and active safety barriers. Reliability and risk are linked, increasing reliability can reduce the risk of undesired events in process plants. Nevertheless, there still seems to be no clear link between the reliability data measured at a process plant and the quantitative measure of risk. This work incorporates reliability related data such as failure rate, time to failure, life cycle stage of equipment and different time horizons for scheduled maintenance into the risk assessment.

The increasing probability of failure of equipment as a function of time if no inspection/maintenance is provided, has an important effect in the estimated risk values. Risk can increase two or three orders of magnitude if a good maintenance program is not in place. The proposed approach provides a useful tool to support decision making, since it can be used to optimize the maintenance intervals.

Results demonstrate the importance of updating the estimated risk values given real-time observed risk factors (equipment failure and effect of time) in the facility. The updated probability of the consequence values can be several order of magnitudes higher than the initial predicted values (obtained from the static analysis). When evidence of equipment failure is used to update the value of risk, this approach can be applied to identify equipment and safety barriers that are critical to maintain safe operations and to quantify the increment of risk in case their failure. The identification critical equipment and safety barrier in combination with the evaluation of risk over time can be used to support decision-makers to point out the equipment that will require continuous inspection and maintenance.

Future research work includes the extension of this approach to repairable systems for including the time to repair (TTR). In addition, the approach must also be extended to include human factors KPIs.
