# UCLA 

## UCLA Electronic Theses and Dissertations

## Title

System-Level Prognosis and Health Monitoring Modeling Framework and Software Implementation for Gas Pipeline System Integrity Management

## Permalink

https://escholarship.org/uc/item/15j13835

## Author

cHALGHAM, Wadie

## Publication Date

2020
Peer reviewed|Thesis/dissertation

# UNIVERSITY OF CALIFORNIA 

Los Angeles

## System-Level Prognosis and Health Monitoring Modeling Framework and Software <br> Implementation for Gas Pipeline System Integrity Management

A dissertation submitted in partial satisfaction of the
requirements for the degree Doctor of Philosophy
in Mechanical Engineering
by

Wadie Chalgham

(C) Copyright by

Wadie Chalgham
2020

# ABSTRACT OF THE DISSERTATION 

System-Level Prognosis and Health Monitoring Modeling Framework and Software<br>Implementation for Gas Pipeline System Integrity Management

by

Wadie Chalgham<br>Doctor of Philosophy in Mechanical Engineering<br>University of California, Los Angeles, 2020<br>Professor Ali Mosleh, Chair

Recurrent pipeline failures continue to be a source of safety and economic risk related to processing, transporting, and distributing natural gas. Studies have shown the lack of comprehensive, integrated, and accessible risk-informed integrity management models and tools for pipeline operators is a major contributor. To address this gap, this research presents a systemlevel Prognosis and Health Monitoring (PHM) modeling framework for gas pipeline system integrity management to prevent or reduce the likelihood of failures. The proposed PHM approach takes into consideration all possible failure modes of the pipeline under study. It leverages the advancement of sensor technology to stream field data in real-time to perform a dynamic systemlevel failure analysis based on Hybrid Causal Logic (HCL) including a Dynamic Bayesian

Network (DBN) corrosion model, to provide cost-effective and optimal mitigation actions such as sensor placement and maintenance schedule optimizations. The developed models are implemented in a software platform where the pipeline operators can observe the real-time and projected health state of the pipeline and the set of suggested actions to enhance the structural integrity of the pipeline system. The platform includes three main modules: Real-Time Health Monitoring, System-Level Reliability, and Optimal Mitigation Actions. From a safety perspective, the proposed PHM can prevent pipeline failures or reduces their likelihood by supporting pipeline operators in optimal decision-making and planning activities. To demonstrate potential benefits and performance of the proposed framework and software implementation, it is applied in a case study involving a corroding gas transmission pipeline.

The dissertation of Wadie Chalgham is approved.
Gregory P. Carman
Ajit K. Mal
Jonathan P. Stewart
Ali Mosleh, Committee Chair

University of California, Los Angeles
2020

# Table of Contents 

1. Introduction ..... 1
1.1 Motivation ..... 1
1.2 Background ..... 3
1.2.1 Gas Pipeline Failure Causes ..... 3
1.2.2 Natural Gas from Production to Customers ..... 3
1.2.3 Wet, Dry, and Sour Natural Gas ..... 5
1.2.4 Natural Gas Transmission Pipeline System ..... 5
1.3 Challenges of current PHM Approaches ..... 6
1.4 Problem Statement ..... 10
1.4.1 Limitations of current Performance Models for Multi-component Systems ..... 11
1.4.2 Limitations of current Mitigation Actions Models ..... 12
1.5 Research Objectives ..... 14
1.6 Research Contributions ..... 15
1.6.1 Components/System Performance Degradation and their Interactions Modeling ..... 15
1.6.2 Cost-effective Sensor Placement to better Detect Damages ..... 17
1.6.3 Cost-effective Maintenance Scheduling to Prevent or Reduce the Likelihood of Failures ..... 17
1.6.4 Optimized Operating Parameters to Increase Profit, Reduce Degradations, and Reduce $\mathrm{CO}_{2}$ Emissions ..... 18
1.7 Organization ..... 18
2. Methodology Overview ..... 20
2.1 Definitions ..... 20
2.1.1 Degradation Model ..... 20
2.1.2 Process Model ..... 20
2.1.3 Performance Metrics ..... 21
2.2 Proposed PHM Modeling Framework ..... 21
2.3 Software Implementation ..... 23
3. System-level Pipeline Network Performance Modeling ..... 24
3.1 Pipeline Network System Modeling ..... 24
3.2 System-Level Failure Analysis ..... 25
3.2.1 Hybrid Causal Logic (HCL) Modeling ..... 25
3.3 Dynamic BN-based Corrosion Predictive Modeling ..... 28
3.3.1 Internal Corrosion Model ..... 30
3.3.2 External Corrosion Model ..... 34
3.3.3 Mechanical Model ..... 36
3.3.4 Reliability Model ..... 38
3.4 Compressor Failure Predictive Modeling ..... 40

3.5 Human Error Modeling ..... 42
4. Failure Propagation Modeling ..... 44
4.1 Complex Network Theory ..... 45
4.2 Centrality Measures ..... 46
4.2.1 Degree Centrality ..... 46
4.2.2 Closeness Centrality ..... 47
4.2.3 Betweenness Centrality ..... 47
4.3 Proposed Failure Propagation Framework ..... 48
4.4 Compressor/Valve Performance Degradation effect on Corrosion Degradation ..... 49
5. Degradation-based Operation and Maintenance Schedule Optimization (DOMSO) ..... 53
5.1 Overall Mitigation Actions Optimization Framework ..... 53
5.2 Objectives of the DOMSO Framework ..... 54
5.3 DOMSO Modeling ..... 56
5.4 Inspection and Maintenance Schedule Optimization ..... 60
5.5 Inspection/Maintenance Measures for Compressor Stations ..... 64
6. Degradation-based Sensor Placement Optimization (DSPO) ..... 65
6.1 Motivation ..... 65
6.2 Optimization Objectives ..... 66
6.3 Proposed Framework ..... 66
6.3.1 Corrosion Predictive Model (Dynamic BN) ..... 67
6.3.2 High-Likelihood Damage Sampling ..... 68
6.3.3 Damage Clustering (Constrained K-means) ..... 69
6.3.4 Damage Detection Probability Quantification ..... 70
6.3.5 Sensor Placement Optimization ..... 71
7. Pipeline System Integrity Management Software Implementation ..... 73
7.1 Real-Time Health Monitoring ..... 76
7.2 System-Level Failure Analysis ..... 77
7.3 Optimal Mitigation Actions ..... 78
8. Case Study: Kern River Transmission Pipeline Network ..... 79
8.1 Pipeline System Network Modeling ..... 80
8.2 System-Level Failure Analysis ..... 84
8.2.1 Hybrid Causal Logic (HCL) Modeling ..... 84
8.2.2 Dynamic BN-based Corrosion Simulation Results ..... 85
8.2.3 System-Level Failure Probability Quantification ..... 91
8.3 Sensor Placement Optimization ..... 94
8.3.1 High-Likelihood Damage Sampling ..... 94
8.3.2 Damage Clustering (Constrained K-means) ..... 95
8.3.3 Damage Detection Probability Quantification ..... 96

8.3.4 Optimization Results ..... 98
8.4 Inspection/Maintenance Schedule Optimization ..... 100
8.5 Operating Parameters Optimization ..... 102
9. Conclusions and Future Work ..... 108
Appendix A ..... 110
Appendix B ..... 114
References ..... 117

# List of Figures 

Figure 1. PHMSA Pipeline Incidents, Fatalities, Injuries, and Damage Cost since 2000 ..... 2
Figure 2. Natural Gas Transmission Pipeline Failure Causes ..... 3
Figure 3. Natural Gas from Production to Customers ..... 4
Figure 4. Natural Gas Transmission Pipeline System ..... 6
Figure 5. Challenges of Current PHM Approaches ..... 7
Figure 6. Literature Gaps: Limitations of Current System-level Performance and Mitigation Actions Models ..... 11
Figure 7. Components/System Performance Degradation ..... 16
Figure 8. Components/System Interactions Modeling ..... 16
Figure 9. Operating Parameters Optimization ..... 18
Figure 10. Performance Metrics ..... 21
Figure 11. Proposed PHM Modeling Framework ..... 22
Figure 12. Software Implementation of the Integration of the PHM Modeling Framework ..... 23
Figure 13. Natural Gas Transmission Pipeline System Segmentation for Modeling ..... 24
Figure 14. Schematic of the HCL Diagram for the System-Level Failure Analysis ..... 26
Figure 15. System-Level Transmission Pipeline Fault Tree Modeling Concept ..... 27
Figure 16. DBN Corrosion Predictive Model Framework ..... 29
Figure 17. DBN Model for Internal Corrosion Prediction ..... 31
Figure 18. DBN Model for External Corrosion Prediction ..... 35
Figure 19. Gas Compressor Failure Probability over Time (after Spüntrup et al., 2018) ..... 40
Figure 20. Compressor Performance Degradation based on Flow Rate Drop (after Safiyullah et al., 2018) ..... 41
Figure 21. Human Error in the Control Room Operations BN ..... 42
Figure 22. Human Error in the Maintenance Operations BN ..... 43
Figure 23. System-Level Failure Propagation Methodology ..... 44
Figure 24. Multiple Centrality Measures of the same Graph: ..... 45
Figure 25. Proposed Failure Propagation Framework ..... 48
Figure 26. Compressor/Valve Performance Degradation effect on Corrosion Degradation ..... 49
Figure 27. Flow Rate effect on Corrosion Rate ..... 50
Figure 28. Overall Mitigation Actions Optimization Framework ..... 54
Figure 29. Objectives of the DOMSO Framework ..... 55
Figure 30. Optimization Objectives: Simultaneously Optimize the Pipeline ..... 56
Figure 31. Optimization Outputs ..... 57
Figure 32. Optimization Constraints ..... 58
Figure 33. Framework of the Inspection/Maintenance Schedule Optimization ..... 60
Figure 34. Framework of the RL-based Maintenance Scheduler ..... 62
Figure 35. Compressor Performance Degradation over time with an Alarm System ..... 64
Figure 36. Optimization Objectives: Maximize Damage Detection at a Minimal Cost ..... 66
Figure 37. Proposed Sensor Placement Optimization Framework ..... 67
Figure 38. K-Means Clustering Methodology ..... 70
Figure 39. Software Platform Modules ..... 75
Figure 40. Pipeline Network Building Module ..... 76

Figure 41. System-Level Failure Analysis Module ..... 77
Figure 42. Kern River Gas Transmission Pipeline ..... 79
Figure 43. Kern River Gas Transmission Pipeline Network Building in the Software Platform ..... 81
Figure 44. Real-time Operating Parameters at Monitoring Point 1 in the Live Data Monitoring Module in the Software Platform ..... 82
Figure 45. System-Level Fault Tree of Kern River Gas Transmission Pipeline ..... 84
Figure 46. Time-evolution Schematics of Predicted Internal Corrosion Degradation and Failure Probability for Phase 1 Transmission Pipeline Segment ..... 86
Figure 47. Location-evolution Schematics of Predicted Internal Corrosion Degradation and Failure Probability for Phase 1 Transmission Pipeline Segment after 30 Years of Operation ..... 89
Figure 48. Time-evolution Schematics of Predicted External Corrosion Degradation and Failure Probability for Phase 1 Transmission Pipeline Segment ..... 90
Figure 49. System-Level Failure Probability Distribution after 5 Years of Operation ..... 91
Figure 50. Time-evolution System-Level Failure Probability for 30 Years of Operation ..... 92
Figure 51. The Criticality Importance Measures of the Pipeline System Failure at $t=10$ years ..... 93
Figure 52. The layout of the Corrosion Damage and Nodes for Phase 1 Transmission Pipeline Segment ..... 95
Figure 53. Damage Clustering Layout ..... 95
Figure 54. Sensor Placement Optimization Layout for a Small Part of Phase 1 Transmission Pipeline Segment ..... 99
Figure 55. Sensor Placement Layout Without Optimization ..... 99
Figure 56. Results of the Inspection Recommendation and Maintenance Schedule Optimization for Phase 1 Transmission Pipeline Segment ..... 100
Figure 57. Corrosion Predictions and Optimal Maintenance Schedule for Different Operating Pressures and Flow Velocities ..... 102
Figure 58. Compared Monthly Average Costs of 12 Cases of Normal (Periodic) Maintenance Schedules and the 6 Cases of Optimal Maintenance Schedules ..... 103
Figure 59. Transmission Pipeline Components. ..... 105

# List of Tables 

Table 1. PHMSA Pipeline Incidents and their Impact over 20 years ..... 2
Table 2. Maintenance Activities and their related Cost and Downtime ..... 58
Table 3. Deterministic Recommended Practices Criteria (DNV-RP-F101) ..... 61
Table 4. Size Classes for Corrosion Defects ..... 68
Table 5. Basic Design Variables of Phase 1 and Phase 2 of the Kern River Gas Transmission Pipeline ..... 81
Table 6. Simulated Operating Parameters of Phase 1 and Phase 2 of the Kern River Gas Transmission Pipeline ..... 82
Table 7. Soil and pipe data of the Kern River gas transmission pipeline ..... 83
Table 8. Probabilities of some basic failure events ..... 85
Table 9. Clusters for Corrosion Defects ..... 96
Table 10. Damage Detection Probability (DDP) Matrix for an Acoustic-Emission Sensor ..... 96
Table 11. Damage Detection Probability (DDP) Matrix for an Ultra-Sonic Sensor ..... 97
Table 12. Operator Inputs to the Optimization ..... 98
Table 13. Output of the Optimization ..... 98
Table 14. Economical and Environmental Benefits of the Optimized Maintenance Schedules ..... 104
Table 15. Optimal Operating Parameters for Phase 1 Transmission Pipelines ..... 106

# Acknowledgments 

I would like to express my deepest gratitude to everyone who helped me during my Ph.D. journey. First of all, I would like to acknowledge the support and encouragement of my family, who helped me in every way possible throughout my academic path.

I would like to acknowledge the support and supervision of Prof. Ali Mosleh and express my gratitude to him for involving me in various research projects and for bringing me into the family of the B. John Garrick Institute for the Risk Sciences (GIRS). I would like to thank Prof. Greg P. Carman, Prof. Ajit K. Mal, and Prof. Jonathan P. Stewart for having served on my committee and providing early guidance in defining the direction and proper scope for my research.

I would like to acknowledge the support, and kindness of my lab-mate, colleague, and friend Keo-Yuan Wu who helped me during every step of my research work. I would like to thank Dr. Mihai Diaconeasa and Arjun also for their helpful advice and assistance on various technical aspects of the modeling framework and the software implementation. In addition, I would like to acknowledge my colleagues Tarannom Parhizkar, Zahra Mahmoodzadeh, Marilia Ramos, and Saeed Nozhati for their assistance with my research work and for providing a friendly and collaborative research environment. I would like to express a special thank you to Joselyne Saldana for her kindness, work ethics, and facilitation of research meetings.

Finally, I would like to acknowledge the sponsorship of the Petroleum Institute, Khalifa University of Science and Technology, Abu Dhabi, UAE, and the University of Maryland (Department of Mechanical Engineering) for the research work presented in this dissertation, which is part of the Pipeline System Integrity Management research project.

# Vita 

## Education


## Research Experience

Graduate Researcher: The Garrick Institute for the Risk Sciences, UCLA

- Lead developer of the Pipeline System Integrity Management (PSIM) platform sponsored in part by the Petroleum Institute, Khalifa University of Science and Technology (UAE) through the University of Maryland.
- Developed the predictive physics of failure models and system-level pipeline health monitoring methodology. The project involves a multi-disciplinary science, engineering, and operational approach to realize a comprehensive and state-of-the-art solution to pipeline integrity. The PSIM platform integrates real-time and historical data, methods, predictive failure models, and systemlevel inference algorithms to form a total system health management support tool to aid in integrity decision making and planning by the pipeline operators. The approach is innovative and unique in its comprehensive integrative perspective and focuses on providing practical solutions while advancing the critical scientific and engineering foundations.
Start Date: 2017/09; End Date: 2020/12
Supervisor's Name: Prof. Ali Mosleh

# Recent Publications 

W. Chalgham, K. Wu, and A. Mosleh A., 2020, "System-Level Prognosis and Health Monitoring Modeling Framework and Software Implementation for Gas Pipeline System Integrity Management," Journal of Natural Gas Science and Engineering.
W. Chalgham, K. Wu, and A. Mosleh, 2020, "Sensor Placement Optimization based on Dynamic Bayesian Network Corrosion Prediction Model," Proceedings of the ASME 2020, International Mechanical Engineering Congress and Exposition, November 15-19, 2020, Portland, OR.
W. Chalgham, and A. Mosleh A., 2020, "System-Level Prognostics and Health Monitoring Methodology for Complex Inter-Dependent Systems," Proceedings of the 30th European Safety and Reliability Conference and the 15th Probabilistic Safety Assessment and Management Conference, November 1-6, 2020, Venice, Italy.
W. Chalgham, M. Diaconeasa, K. Wu, and A. Mosleh A., 2019, "A dynamic pipeline network health assessment software platform for optimal risk-based prioritization of inspection, structural health monitoring, and proactive management," Proceedings of the ASME 2019, International Mechanical Engineering Congress and Exposition, November 11-14, 2019, Salt Lake City, UT.
W. Chalgham, K. Wu, and A. Mosleh, 2019, "External corrosion modeling for an underground natural gas pipeline using COMSOL Multiphysics," Proceedings of the COMSOL Multiphysics 2019, October 2-4, 2019, Boston, MA.
W. Chalgham, G. Carmen, and A. Mosleh, 2019, "Smart pipeline structural health monitoring of crack or fracture propagation using piezoelectric sensors," Proceedings of the COMSOL Multiphysics 2019, October 2-4, 2019, Boston, MA.

## Awards

i) Best Paper Competition winner of the 2020 ASME SERAD (Safety Engineering, Risk and Reliability Analysis Division) Student Safety Innovation Challenge Contest for the paper: "Sensor Placement Optimization based on Dynamic Bayesian Network Corrosion Prediction Model". The paper offers a novel approach for identifying optimal sensor network layout to help oil and gas pipeline operators make risk-informed decisions to enhance pipeline system integrity management through optimal mitigation actions.
ii) Grad Slam Competition winner (Audience Choice Award) at UCLA's 2020 prestigious Grad Slam competition on March 5th at the California Nano-Systems Institute (CNSI). Grad Slam is a UC-wide competition that showcases and awards the best research presentations by graduate students from all departments. The presentation was on "Smart Pipeline Leak Detection and Response System".

# CHAPTER 1 

## 1. Introduction

### 1.1 Motivation

Transporting fuel from production sites to consumers is a vital national need and a complex supply-chain process. In the United States, the length of oil and gas pipeline infrastructures is over 2.6 million miles (Wang et al., 2019), which makes pipeline system integrity management both challenging and crucial to reduce the risks and likelihood of incidents and accidents, as pipeline failures can have a major impact on human lives and property. For instance, on September 9th of 2010, a 30 -inch natural gas line exploded in San Bruno, California, destroying 38 homes, damaging 120 homes, killing 8, and injuring 58 (Ariaratnam, 2014; Peekema, 2013). According to the Pipeline and Hazardous Materials Safety Administration (PHMSA), which is part of the United States Department of Transportation, an average of 287 pipeline incidents, 14 deaths, and 59 injuries happen every year as shown in Table 1 and Figure 1 (U.S. Department of Transportation, PHMSA, 2020). These incidents have caused 281 fatalities, 1183 injuries, and more than $dollar 10$ billion in the US since 2000. The PHMSA regulation $\S 191.3$ defines an incident as an event where gas is released from a pipeline and causes death, injury, property damage of more than $dollar 50,000$, or gas loss of more than three million cubic feet.

These failures could have been prevented or mitigated if appropriate system integrity management techniques were applied. This research focuses on the assessment and management of the transmission pipeline system integrity. The goals are to enhance the safety of gas transportation, maintain pipeline system safety and integrity, and increase the availability of gas for customer consumption in a reliable and safe way.

Table 1. PHMSA Pipeline Incidents and their Impact over 20 years


![img-0.jpeg](img-0.jpeg)

Figure 1. PHMSA Pipeline Incidents, Fatalities, Injuries, and Damage Cost since 2000

# 1.2 Background 

### 1.2.1 Gas Pipeline Failure Causes

Based on the PHMSA data (U.S. Department of Transportation, PHMSA, 2020), the main natural gas transmission pipeline failure causes are equipment failure, corrosion failure, excavation damage, natural force damage, incorrect operation, outside force damage, or other causes. As shown in Figure 2, 36\% of pipeline failures are caused by material, weld, or equipment failure, $19 \%$ by corrosion failure, $14 \%$ by excavation damage, $11 \%$ by natural force damage, $8 \%$ by other causes, $7 \%$ by outside force damage, and $5 \%$ by incorrect operation.
![img-1.jpeg](img-1.jpeg)

Figure 2. Natural Gas Transmission Pipeline Failure Causes

### 1.2.2 Natural Gas from Production to Customers

Transporting fuel from production to consumers is a critical and complex process. In the United States, the length of fuel pipelines is more than 2.6 million miles which makes the pipeline system integrity and assessment very important to avoid any incidents. Energy-related pipelines can carry natural gas, consisting mostly of methane, oil, and certain other hazardous liquids. In order to transport natural gas from production to the consumers, different pipelines and lines are used

namely gathering, transmission, and distribution pipelines as shown in Figure 3. Production lines are used to produce the gas from the production wells, either from onshore or offshore sites. Once the gas is produced, gathering pipelines carry the gas from the wellhead to a processing and treatment plant.

Following refinement, transmission pipelines are used to carry the gas to the city gate. Transmission pipelines have the longest length since they move the gas around the country. In the US, there are more than 300,000 miles of gas transmission pipelines. They also operate under the highest pressures (200-1500 psi usually). They should be buried at least 30 inches deep in rural areas and 36 inches in higher population density areas according to federal regulations. Compressors are placed along these pipelines to preserve the pressure level and account for the pressure drop along the transmission line.

Once the gas reaches the city gate, an odorant is added to the gas (sulfur chemicals called mercaptans) and distribution pipelines that operate at a lower pressure (up to 200 psi for gas mains and up to 10 psi for residential service lines) are used to deliver the natural gas to individual homes, commercial customers, or industrial plants. Distribution pipelines could be made out of plastic whereas gathering and transmission pipelines are made out of steel.
![img-2.jpeg](img-2.jpeg)

Figure 3. Natural Gas from Production to Customers

# 1.2.3 Wet, Dry, and Sour Natural Gas 

The produced natural gas contains different hydrocarbons, mostly methane, and could be classified as wet or dry gas depending on the methane concentration. The gas is classified as "drier" whenever the methane concentration is higher. In addition, the gas can contain other evaporated liquids such as ethane, butane, and pentane, which are collectively referred to as natural gas liquids (NGLs) or condensates.

Moreover, natural gas can be referred to as sour gas whenever it contains a high quantity of hydrogen sulfide. Hydrogen sulfide can cause structural as well as life-threatening consequences. In fact, when hydrogen sulfide is mixed with water, it causes corrosion in pipelines because of the acidic solution formed. It is also very poisonous and can cause severe health problems or death at high concentrations.

### 1.2.4 Natural Gas Transmission Pipeline System

Before transporting natural gas, it needs to be refined by removing the impurities at the gas processing and treatment plant. The goal is to ensure the safety of gas transportation, maintain the pipeline system safety and integrity, and make the gas ready for customer consumption. The most common impurities include hydrocarbons, water, helium, hydrogen sulfide, sulfur, and carbon dioxide. Transmission pipelines carry gas thousands of miles around the country. The transportation force is the pressure differential (i.e., the gas flows from a high to a low-pressure area). However, this force decreases over the length of the pipeline and compressor stations should be built along the transmission line as shown in Figure 4 to push the pressure back to a higher level.

![img-3.jpeg](img-3.jpeg)

Figure 4. Natural Gas Transmission Pipeline System

Compressors are usually powered by natural gas engines or electric motors and are built every 50 to 100 miles along the pipeline to ensure the flowing of the gas at the desired pressure according to PHMSA (U.S. Department of Transportation, PHMSA, 2020). Moreover, gate setting facilities are built along the pipeline every 10 miles to ensure a better control of the gas flow using the installed valves. These facilities can also be used when a specific pipe segment needs to be isolated for maintenance work.

# 1.3 Challenges of current PHM Approaches 

In order to ensure reliable pipeline operations, system integrity is essential to prevent catastrophic failures and expensive downtime. Pipeline system integrity management is a "program that manages methods, tools, and activities for assessing the health conditions of pipelines and scheduling inspection and maintenance activities to reduce the risks and costs" (Xie and Tian, 2018). It is a procedure consisting of three main steps: defect detection and identification, defect growth prediction, and risk-based management. Significant advances are needed in these three steps to accurately evaluate defects and prevent pipeline failures based on inspection data, defect growth prediction, and integrity activities optimization because the current pipeline integrity methods and techniques present multiple limitations and challenges as summarized in Figure 5.

![img-4.jpeg](img-4.jpeg)

Figure 5. Challenges of Current PHM Approaches

First of all, concerning the data gathering methods, Health Monitoring (HM) along with nondestructive evaluation (NDE) techniques have been used over the last few decades to enable the integration and automation of the entire pipeline system for real-time monitoring, inspection, and damage detection. For instance, in-line inspection (ILI), a method used to identify anomalies from the inside of the pipe, is performed periodically using smart "pigging" tools to detect pipeline defects such as corrosion and cracks (Xie and Tian, 2018). Pigging refers to the use of Pipeline Inspection Gauges (PIG) which are devices that can perform various inspection and maintenance operations such as gathering information about the pipeline (e.g. temperature, pressure, or corrosion loss) and debris cleaning without stopping the gas flow. ILI has been considered the most efficient way for a long time to assess the integrity of natural gas transmission pipelines subjected to corrosion attack. However, these data gathering methods and techniques faced a number of challenges and limitations:

- Their implementation is very costly and labor-intensive, especially for transmission pipelines that are typically hundreds of miles in length. In fact, these techniques require

direct contact with the system structure and have to be applied frequently to determine the health condition of the pipelines. For instance, the installation and ongoing monitoring costs of the acoustic fiber-optic monitoring (AFO) inspection method are as high as $dollar 64,000$ per mile and $dollar 150,000$ for hardware monitoring (Chalgham, 2016). As reported in (Faber, 2017), the San Diego County Water Authority has been using acoustic fiber-optic (AFO) systems to monitor pipes in real-time and has spent over $dollar 13$ million since 2006 to install and maintain this system.

- The accuracy of these conventional techniques heavily depends on the measuring equipment and method. For instance, a sensor can provide voltage signals while detecting or measuring damage size in a pipeline, but can introduce noise and bias in the damage measurements (Alaswad and Xiang, 2017; Kishawy and Gabbar, 2010).
- These techniques cannot be used in about half of pipelines today as they are not-piggable (smart pigs and ILI cannot be used) (Xie and Tian, 2018), because of the size of the large assemblies needed (Chalgham, 2016). The complicated and time-consuming installation is another challenge facing these NDE techniques (Chalgham, 2016).

To address the costs and reliability issues related to the field-based data gathering methods and techniques, the industry is increasingly relying lately on probabilistic modeling approaches to quantify the health state of the system and predict its failure path. Given that corrosion is the second main cause of pipeline failure after equipment failure (U.S. Department of Transportation, PHMSA, 2020) and given that it has stochastic properties (Zhang and Zhou, 2014), the probabilistic approaches have focused mainly on developing corrosion predictive models. Above all, the consequence of corrosion failures such as leak, or burst is potentially significant in terms

of economic and life loss. However, these model-based approaches present multiple limitations as well:

- These approaches are not comprehensive and integrated with respect to the failure causes. For instance, sometimes multiple types of corrosion may coexist due to complex operating conditions; therefore, a model that only applies to one kind of corrosion is not sufficient to a basis for corrosion prediction for natural gas transmission pipelines.
- Many corrosion predictive models are data-driven but not dynamic to reflect the stochastic nature of corrosion and dynamic operating conditions (Heidary et al., 2018).
- While some of the research have considered spatial variability of localized damage along a pipeline (De Leon and Macías, 2005; Zhang and Zhou, 2014), temporal variability is often neglected and the integration of both variabilities into one model is lacking in the literature.

The main objective of quantifying the health state of the pipeline through the data gathering methods and probabilistic predictive models is to provide optimal mitigation actions to the operators to prevent or reduce the likelihood of failures. However, the current mitigation actions optimization models present multiple limitations:

- The optimization models are developed and computed for the component-level (e.g., small pipe segment), and the system-level is often neglected due to the complexity of developing such a model; most of the optimization-based pipeline PHM approaches present in the literature only consider a single and relatively small pipeline segment (with less than ten localized damages). In fact, considering large pipe segments with a large number of damages and design variables is computationally expensive and complex (Alaswad and Xiang, 2017; Hou et al., 2019).

- These maintenance methods are not cost-effective which leads to the damages being neglected in pipelines because of the costly health monitoring and corresponding downtime (Kishawy and Gabbar, 2010). In the US alone, the annual cost of corrosion maintenance, repair, and replacement in transmission pipelines is estimated to be about $dollar 125$ billion (Koch et al., 2002) which leads the operators to neglect the optimization results if they suggest huge downtimes and monetary losses.
- No reported pipeline PHM approach has considered dynamic and time-dependent mitigation action suggestions to the operators such as sensor placement and inspection/maintenance schedule optimizations based on streaming sensor data from the multiple segments of a pipeline (Alaswad and Xiang, 2017; Ostachowicz et al., 2019).
- The industry is lacking a software tool that can integrate the sensor data (operating parameters), risk-based models, and optimal mitigation suggestions into a user-friendly software to make it easy for the operators to make timely decisions to prevent failures in a cost-effective way.


# 1.4 Problem Statement 

The recurrent pipeline failures are caused in part by the limited system-level performance modeling and in part by the non-optimal risk-based management. A comprehensive and integrated system modeling along with optimal mitigation actions such as maintenance scheduling and sensor placement could have prevented many of the observed failures. The limitations of the current performance modeling approaches and mitigation actions are summarized in Figure 6.

![img-5.jpeg](img-5.jpeg)

Figure 6. Literature Gaps: Limitations of Current System-level Performance and Mitigation Actions Models

# 1.4.1 Limitations of current Performance Models for Multi-component Systems 

The existing performance/deterioration modeling of multi-component systems are limited in one or more of the following ways: (i) the degradation of components' performance is not considered, (ii) the degradation of the system's performance is not considered, and (iii) their interactions (i.e failure propagation among components) are not considered.

In fact, the literature on multi-component systems deterioration modeling is very thin because of the mathematical and conceptual complexity involved in understanding the stochastic, physical, and functional dependencies among components. As a result, the literature mainly presents research work that treats the degradation of components independently; "The literature has mainly considered single-component systems due to the complexity of the probabilistic analysis for multicomponent systems" (Alaswad and Xiang, 2017).

Dependency among components of any system always exists and should not be ignored. Modeling multi-component systems is complex because degradation or complete failure of a single or multiple components could affect other components in the system in terms of degradation or failure (Nicolai and Dekker, 2008). However, a model to describe these dependencies has not been yet developed. The complexity of multi-component deterioration modeling arises from the

stochasticity of deterioration models and uncertainty in material properties (Hong et al., 2014). A handful of models (Caballé et al., 2015; Castro et al., 2015; Wang, 2002) assume independent degradation processes, without considering physical or functional dependence within the components of the system.

Moreover, "One of the main gaps identified for future research is the addition of directed edges in the system graph representation. This can provide further information about the behavior of a system, representing, for example, the flow of a process fluid in the system to improve diagnostics capabilities or showing its evolution in time for better health-state prognostics" (Ruiz-Tagle Palazuelos et al., 2020; Ruiz-Tagle Palazuelos and Droguett, 2020). In addition, "it is evident from the review that there is a gap in the literature where degradation interactions involving degradation rates of the components are not addressed"(Rasmekomen and Parlikad, 2016).

The main challenges facing the system-level performance modeling that will be addressed in this dissertation are the integrated modeling of complex systems and the degradation dependencies/interactions among system components.

# 1.4.2 Limitations of current Mitigation Actions Models 

The current maintenance schedule optimization models present the following limitations:

- Maintenance schedule of pipeline and its components such as compressors are performed on a periodic basis regardless of the degradation level.
- The downtime cost is often neglected in the maintenance scheduling models.
- The degradation and process models of the pipeline system are not simultaneously considered in the maintenance scheduling models.

- Different objective functions are not considered simultaneously in the optimization in terms of safety, environmental, and operating economic aspects.
- The implication on $\mathrm{CO}_{2}$ emissions are neglected in the maintenance scheduling models.

As for the current sensor placement optimization models, they present the following limitations:

- The sensor locations are placed at fixed intervals because "there is no industry guidance or standard to direct operators in proper sensor placement" according to a report submitted to PHMSA (Baker Inc. and Fessler, 2008).
- The defect detection techniques have different coverage ranges and costs, which should not be neglected in the optimization model (Kishawy and Gabbar, 2010).
- The optimization results are based on static/historic data and are not updated in real-time with changing operating parameters (Alaswad and Xiang, 2017; Ostachowicz et al., 2019).
- Risk and severity of damages are not considered in the optimization algorithms because the current techniques (Alaswad and Xiang, 2017; Younis and Akkaya, 2008) are deterministic and can only provide binary damage detection results. In fact, most of the health monitoring models presented in the literature taking into consideration probabilistic detection metrics such as Probability of Detection (POD) and probabilistic Measurement Error (ME) (Chatterjee and Modarres, 2013; Stephens and Nessim, 2008; Zhang and Zhou, 2014) are deterministic and can only provide binary damage detection results (Alaswad and Xiang, 2017; Younis and Akkaya, 2008) which leads to risk and severity of damage of different sizes and types being neglected and not considered in the modeling approach. As a result, the performance of these deterministic approaches is unsatisfying (Ostachowicz et

al., 2019) because of the lack of uncertainty consideration regarding the information about location, type, and size of the damage.

- The optimization models are based on stochastic corrosion formation models which has multiple uncertainties including defect location uncertainty, temporal uncertainty of the local degradation increments, and damage detectability uncertainty (Heidary et al., 2018).
- The sensor placement algorithms are designed for short and straight pipeline segments (component-level) and are not scalable to system-level complex systems due to computational complexity and limitations (Alaswad and Xiang, 2017; Hou et al., 2019).

The research work presented in this dissertation aims at enhancing PHM modeling by presenting a methodology that covers the discussed limitations of performance modeling and mitigation actions optimizations.

# 1.5 Research Objectives 

In view of the limitations and challenges of the current gas pipeline mitigation actions discussed in the preceding sections, the objective of this dissertation is to develop a system-level Prognosis and Health Monitoring (PHM) methodology for gas pipeline system integrity management based on the various failure and degradation types of the system's components and their inter-dependencies. The proposed PHM methodology should be able to:

- Quantify pipeline-system health level (Reliability) in real-time and over-time.
- Optimize pipeline-system inspection/maintenance and operation schedule.
- Optimize sensor placement along the pipeline system.

The research presented in this dissertation presents a methodology to enhance detection, diagnosis, and prediction of the failure causes of gas pipelines. This methodology aims at

improving pipeline integrity management by going from a reactive troubleshooting to a proactive failure avoidance through optimized mitigation actions. This proposed methodology is based on understanding the complex failure behavior of pipeline systems through system-level failure modeling.

# 1.6 Research Contributions 

In view of the above-mentioned limitations and challenges of the current PHM approaches, this research focuses on saving human lives and preventing economic loss by improving the infrastructure reliability and safety through an advanced and comprehensive PHM methodology. To make it a practical tool, the methodology is embedded in a dynamic and user-friendly software that displays the real-time health state of the pipeline system, its potential failure paths in time, and suggested mitigation actions to prevent those failures.

In achieving the above objectives, the flowing contributions have been made by this research:

### 1.6.1 Components/System Performance Degradation and their Interactions Modeling

In this research work, the components as well as the system performance degradation are taken into consideration in the modeling of the maintenance optimization framework. As shown in Figure 7, the decrease of performance over time is not considered in other frameworks because of the periodic maintenance schedule but will be taken into consideration in the proposed framework. In fact, the dynamic degradation rates based on the different environmental and operational conditions affect the performance of the components and the system which may lead to failures before the periodic maintenance date.

![img-6.jpeg](img-6.jpeg)

Figure 7. Components/System Performance Degradation

In addition, the interactions between the degradation of components of the system such as the compressor, valves, and pipeline corrosion are modeled. In fact, the models presented in this dissertation show how the performance of a component such compressor has an effect on other components' performance, for example the pipeline corrosion rate (and the system's performance as well). In other words, the modeling of interactions between the components' degradation and process models (defined as thermodynamic, economic, or environmental models) and their effect on the system is one of the novelties of the proposed PHM modeling framework as shown in Figure 8.
![img-7.jpeg](img-7.jpeg)

Figure 8. Components/System Interactions Modeling

# 1.6.2 Cost-effective Sensor Placement to better Detect Damages 

In this research work, a and cost-effective sensor placement framework is presented to better detect damages. The proposed optimization framework aims at providing the operators with the optimal locations to place sensors while minimizing the cost. This framework maximizes the damage detection probability by the provided sensor network which captures as much information as possible on the degrading parts of the pipeline. The proposed real-time optimization framework is based on the dynamic Bayesian Network predictive model of corrosion where the changing operating parameters update the system simulation model. The real-time sensor placement optimization will provide the optimal sensor network layout and detects damages that could have been gone undetected and resulted in pipeline failures. While the current sensor placement methodologies are reactive techniques based on the measured corrosion levels, the proposed sensor placement optimization is both reactive and proactive, by utilizing current and projected corrosion levels over the pipeline network.

### 1.6.3 Cost-effective Maintenance Scheduling to Prevent or Reduce the Likelihood of

## Failures

Based on the system-level performance modeling, a cost-effective and optimal maintenance schedule framework is proposed to prevent or reduce the likelihood of pipeline failures by performing risk-based mitigation actions. The maintenance schedule optimization is based on a reinforcement learning (RL) technique and provides optimized maintenance types and times in order to mitigate corrosion risks.

# 1.6.4 Optimized Operating Parameters to Increase Profit, Reduce Degradations, and Reduce $\mathrm{CO}_{2}$ Emissions 

Finally, one of the novelties of the presented research work is the optimization of the operating parameters in order to increase the economic profit, reduce degradations, and reduce $\mathrm{CO}_{2}$ emissions at the same time as shown in Figure 9. The optimization of the operating parameters aims at: (i) extending the lifetime of the pipeline, (ii) minimizing the maintenance cost, (iii) maximizing the economic profit, and (iv) minimizing the $\mathrm{CO}_{2}$ emission.
![img-8.jpeg](img-8.jpeg)

Figure 9. Operating Parameters Optimization

### 1.7 Organization

The rest of the dissertation is organized as follows: In Chapter 2, an overview of the proposed PHM modeling framework and software implementation is presented. In Chapter 3, the pipeline network system modeling framework is explained and the system-level failure analysis along with the dynamic BN-based corrosion predictive models are presented. Chapter 4 presents the failure propagation modeling in complex systems is presented. In Chapter 5, the inspection and maintenance schedule as well as the operating parameters optimization models are presented. The proposed Degradation-based Operation and Maintenance Schedule Optimization (DOMSO) aims at optimizing the inspection/maintenance schedule of the pipeline components as well as the operating parameters such as the mass flow rate and flow pressure to avoid or reduce the likelihood

of failure of the pipeline system at a lower cost. Chapter 6 describes the sensor placement optimization framework to prevent or reduce the likelihood of pipeline failures by optimizing the placement of sensor in the pipeline network in a way that maximizes the damage detection probability at a minimal cost. In Chapter 7, the pipeline system integrity management software implementation based on the models presented in the previous chapters is explained. A case study (Kern River transmission pipeline network) is presented in Chapter 8 to demonstrate use of the models and the software presented in the previous chapters. Chapter 9 summarizes the objectives and contributions of the research and offers ideas for its extension.

# CHAPTER 2 

## 2. Methodology Overview

In this chapter, an overview of the proposed PHM modeling framework and software implementation are presented and explained in detail. We will start with definitions essential for formulating and describing the methods and tools developed by this work.

### 2.1 Definitions

### 2.1.1 Degradation Model

In this dissertation, a degradation is defined as a gradual and possibly irreversible accumulation of damage that occurs during a system's life cycle. There are two types of degradation: Recoverable Degradation (RD) and Non-Recoverable Degradation (NRD). Examples of causes of Recoverable Degradation are clogging, scaling, and buildup of deposits on the working surface. Examples of causes of Non-Recoverable Degradation are tear, loss of working surface, corrosion/oxidation, erosion. As for remedies, maintenance can recover RD. Also, while a replacement is needed for NRD, an optimal inspection or maintenance schedule will delay replacement. A degradation model can be a physics-based model, a system functional logic model such as Fault Tree, or a Bayesian Network. A compressor performance reduction from $100 \mathrm{~m}^{3} / \mathrm{min}$ to $60 \mathrm{~m}^{3} / \mathrm{min}$, for example, is considered a functional degradation.

### 2.1.2 Process Model

In this dissertation, a process model is defined as a thermodynamic, economic, or environmental model. The effect of pressure-drop on the compressor work, mass flow rate on the economic profit, and pressure levels on the $\mathrm{CO}_{2}$ emissions are examples of process models.

# 2.1.3 Performance Metrics 

In this dissertation, the system-level as well as the component-level performance will be discussed. The system-level performance refers to 4 main metrics: system reliability, gas delivery flow rate, economic profit, and $\mathrm{CO}_{2}$ emissions as shown in Figure 10. The component-level performance is quantified by the degradation models. The different causal paths to degradation will be discussed in the next chapters. For instance, the pump or valve performance may have a direct impact on the other components' performance such as pipeline corrosion.
![img-9.jpeg](img-9.jpeg)

Figure 10. Performance Metrics

### 2.2 Proposed PHM Modeling Framework

This research work introduces and demonstrates a new PHM approach to support system integrity management of aging gas transmission pipelines subjected to continuous damage mechanisms such as corrosion. The proposed PHM approach integrates the data gathering methods, probabilistic modeling, and mitigation actions optimization into a comprehensive, dynamic, and integrated system as shown in Figure 11. The methodology consists of a systemlevel performance modeling and mitigation actions optimization models.

![img-10.jpeg](img-10.jpeg)

Figure 11. Proposed PHM Modeling Framework

For the system-level performance modeling, the operating and design parameters (i.e. realtime sensor data) are fed into the system-level failure analysis module. This module contains the Degradation-based Process Model (DPM) and the Hybrid Causal Logic (HCL), both of which are explained in more detail in the following chapters. The DPM connects the process models and degradation models and quantifies their effect on each other in terms of performance or degradation. The HCL model quantifies the failure probability of the system taking into consideration a wide range of failure causes.

Once the analysis is performed, the system performance/deterioration can be quantified in terms of reliability/lifetime, economic profit, and $\mathrm{CO}_{2}$ emissions. These performance metrics are part of the Health Monitoring module.

Finally, the proposed PHM framework offers mitigation actions optimizations to enhance real-time decision-making support. The optimization models for inspection/ maintenance schedule along with the operation parameters increase the pipeline reliability at the lowest cost and $\mathrm{CO}_{2}$

emissions. In addition, the sensor placement optimization is designed to increases the damage detection probability at the lowest cost.

# 2.3 Software Implementation 

The proposed PHM approach is integrated into a software platform that contains three main features, namely, real-time health monitoring, system-level reliability, and mitigation actions optimization, as shown in Figure 12. The software implementation will help the operators visualize the health state of the pipelines and suggested preventive actions.

In short, the proposed methodology enables the integrity management support to be done starting from data collection, to vulnerability assessment, and finally to mitigation and prevention of failures. Each of the modules presented in this chapter will be discussed in detail in the following chapters.

PHM Modeling Framework
![img-11.jpeg](img-11.jpeg)

Figure 12. Software Implementation of the Integration of the PHM Modeling Framework

# CHAPTER 3 

## 3. System-level Pipeline Network Performance Modeling

### 3.1 Pipeline Network System Modeling

In order to study the transmission pipeline system integrity, the pipeline network has to be defined and analyzed. The pipeline system is simplified and defined as the set of equipment, consisting of steel transmission pipeline segments and compressor stations, that will transport the natural gas from the gas processing and treatment plants to the city gate (the starting point for distribution lines). The transmission pipeline system is divided into multiple sub-systems referred to as "transmission phases" as shown in Figure 13. In this work, the transmission phase is defined as the set of equipment that will transport the natural gas from one compressor to another. It consists of steel transmission pipelines, compressor stations, and valves. The pipeline system is assumed to be connected in series because the failure of any single one of them will lead to the system failure.
![img-12.jpeg](img-12.jpeg)

Figure 13. Natural Gas Transmission Pipeline System Segmentation for Modeling

In reality, the natural gas transmission system is more complicated. Compressors are built every 50 to 100 miles along the pipeline to ensure the flowing of the gas at a desired pressure. They receive the gas at pressures ranging from 200 psi to 600 psi and compresses it back up to 1000 psi to 1400 psi (As a reference, the typical vehicle tires work with compressed air at roughly 30 to 50 pounds of pressure per square inch). Moreover, gate setting facilities are built along the pipeline every 10 miles to ensure better control of the gas flow using the installed valves. These facilities can also be used when a specific pipe segment needs to be isolated for maintenance work.

# 3.2 System-Level Failure Analysis 

The integrity of the pipeline system defined in the previous section will be modeled for the identification of all possible paths to failure. The system-level failure analysis quantifies the realtime and projected system-level failure probability taking into consideration all causes of failures that can affect the pipeline system under study. This analysis is based on Hybrid Causal Logic (HCL) and Dynamic Bayesian Networks (DBNs).

### 3.2.1 Hybrid Causal Logic (HCL) Modeling

The integrity of the pipeline system is modeled for identification of possible paths to failure by the HCL methodology (Groth et al., 2010; Wang, 2007; Groen and Mosleh, 2006), a multilayered modeling approach for probabilistic risk analysis (PRA) that allows most of the appropriate modeling techniques to be applied to different domains of the system. HCL combines three modeling tools, namely, Event Sequence Diagrams (ESDs), Fault Trees (FTs), and Bayesian Networks (BNs) to model risks associated with complex systems. In this dissertation, the HCL model is applied to take into consideration all possible failure modes of the system-level failure probability. This HCL model is composed of a FT layer capturing inter-correlated failure modes

and a BN layer, which is added to model the basic events in the FT to represent the common cause failures and soft causal dependencies stemming from human activities, physical environment or socio-economic environment. A schematic of the HCL diagram for the system-level failure analysis is shown in Figure 14.
![img-13.jpeg](img-13.jpeg)

Figure 14. Schematic of the HCL Diagram for the System-Level Failure Analysis

A high-level model of the contributors to pipeline failure is developed using a FT reflecting the empirical evidence presented in the literature (Chalgham et al., 2019a). Figure 15 illustrates a foundation for the system-level FT for natural gas transmission pipelines which covers in detail the possible causes of the pipeline failure.

In the conceptual FT model, the pipeline system is divided into multiple transmission phases. A transmission phase failure can be caused by the compressor failure, the valve failure, the pipe segment failure, the human error in the control room operations, or other causes. A compressor station fails because of the failure of the lubrication system, power system, shaft seal system, or compressor unit (Veritas, 2004). As for the pipe segment, it fails due to external factors, internal factors, or human error in the maintenance operations. External factors include natural force such as flooding, earthquake, or severe weather/subsidence, corrosion (external or internal), or third-

party damage, while internal factors include material or welding defect. The probabilities of basic failure events of the FT are further modeled using a variety of causal models. For instance, the corrosion (i.e., internal and external) failure events are simulated by time-dependent models like the DBN corrosion predictive models for internal and external corrosion, which will be described in the next section.

The corrosion degradation will be simulated by two DBN-based corrosion predictive models designed for natural gas transmission pipelines subject to internal and external corrosion, respectively. Nonparametric models are used for basic events when the reliability data cannot be fitted to the common statistical distributions. Overall, the FT provides a high-level understanding of the pipeline system failure probability based on the likelihood of failure of the different system components.
![img-14.jpeg](img-14.jpeg)

Figure 15. System-Level Transmission Pipeline Fault Tree Modeling Concept

# 3.3 Dynamic BN-based Corrosion Predictive Modeling 

A Bayesian Network (BN) is a probabilistic graphical model that represents a set of variables and their conditional dependencies via a directed acyclic graph. A Dynamic Bayesian Network (DBN) is a BN which relates variables to each other over adjacent time steps. BNs and DBNs are especially suitable to model large-scale and complex failure modes of systems and components, due to their ability to incorporate causal inference relationships and their impact on the probabilities of failure modes, based on information from various sources including physics-based models, field data, expert judgment, and updating failure probability over time steps (Ayello et al., 2014; Chen and Pollino, 2012; Li et al., 2016; Palencia et al., 2019).

DBNs can account for the knowledge uncertainties, a critical element in developing robust risk-informed decision support systems. The construction of a DBN model is similar to a BN model, which requires several steps. First, building a graphical representation of the chain of events in a cause-consequence relationship leading to corrosion failure. Second, developing the conditional probability tables (CPTs) based on available data such as physics-based models, field data, and expert knowledge among which the physics-based models are the most reliable ones with solid science background (Ayello et al., 2014).

The ability to assess the risk of possible threats to pipeline integrity is essential for a PHM model. In this dissertation, estimating the risk of corrosion to which natural gas transmission pipelines are exposed is discussed. To date, many studies have been done on different types of corrosion either qualitatively or quantitatively (Ayello et al., 2014). Empirical/data-driven, semiempirical, or mechanistic (physics-based) models are developed for predicting the severity of corrosion. However, a comprehensive model that includes multiple types of internal and external corrosion simultaneously is missing in the literature and is the main motivation behind developing

the corrosion predictive model presented in this section. In addition, in most cases the operating conditions of a gas transmission pipeline change frequently within an uncertain range, which leads to considerable uncertainties in the corrosion modeling.

In this dissertation, the development of the discretized Conditional Probability Tables (CPTs) is based on tested and validated physics-based, empirical or semi-empirical models. The proposed PHM methodology offers an important feature by which the DBN models are updatable with realtime data, for instance, the data concerning the pipeline physical state from installed sensors and other monitoring and surveillance methods. In addition, the corrosion simulation is done dynamically over time steps by Monte Carlo simulation (MCS) to take into consideration the timedependency and stochastic nature of corrosion. Corrosion modeling exemplifies the benefits of using an updatable real-time model. The dynamically updated DBN model is able to calculate the corrosion rate considering the changing variables and related uncertainties.

The framework of the DBN corrosion predictive model is shown in
Figure 16. The DBN models of internal and external corrosion consist of three parts.
![img-15.jpeg](img-15.jpeg)

Figure 16. DBN Corrosion Predictive Model Framework

The first part contains corrosion models for corrosion rate prediction, the second part is a mechanical model for burst pressure (remaining strength) estimation, and the third part is a reliability model for the probability of failure calculation.

The proposed DBN-based corrosion hazard assessment considers both internal and external corrosion for gas pipelines subjected to aqueous corrosion. The development of the CPTs needed to calculate the combined effects of various mechanisms on the total corrosion rate for each type of corrosion will be based either on semi-empirical, empirical, or physics-based models.

# 3.3.1 Internal Corrosion Model 

The DBN model for internal corrosion is shown in Figure 17 in which the denotation (node) used in the following paragraphs stands for the name of a node of the DBN corrosion model. The corrosion model of internal corrosion considers five types of corrosion, namely, uniform, pitting, microbiologically-influenced corrosion (MIC), erosion corrosion, and corrosion fatigue that commonly take place inside the pipeline. Except for microbiologically-influenced corrosion, which is an empirical model, the other types of internal corrosion are either physics-based or semiempirical. The DBN model takes operating conditions and pipeline information as inputs to predict corrosion degradation in terms of corrosion rate (Corrosion Depth Rate) for every type of corrosion. The presence of water is an essential factor for the corrosion process to take place and proceed; therefore, a wetting factor (Wetting Factor) is applied to each corrosion type for corrosion predictions. The details of the discretized nodes of the DBN internal corrosion model are listed in Appendix A.

![img-16.jpeg](img-16.jpeg)

Figure 17. DBN Model for Internal Corrosion Prediction

# 3.3.1.1 Uniform Corrosion 

Uniform corrosion is attributed to the presence of carbon dioxide $\left(\mathrm{CO}_{2}\right)$ and hydrogen sulfide $\left(\mathrm{H}_{2} \mathrm{~S}\right)$ in an aqueous environment, leading to the uniform reduction of corrosion products. $\mathrm{CO}_{2}$ and $\mathrm{H}_{2} \mathrm{~S}$ become acidic when dissolved in water, and corrosion reactions then take place at steel surfaces. In this dissertation, the uniform corrosion is based on a physics-of-failure (POF)-based semi-empirical model developed by the authors (Wu and Mosleh, 2019), which can predict timedependent corrosion rate given pipeline operating parameters in an aqueous $\mathrm{CO}_{2} / \mathrm{H}_{2} \mathrm{~S}$ environment. The model inputs are temperature (Temperature), the partial pressure of $\mathrm{CO}_{2}$ ( $p C O 2$ ), the partial pressure of $\mathrm{H}_{2} \mathrm{~S}(p H 2 S)$, pH level $(p H)$, and the flow velocity of gas (Flow Velocity). For detailed descriptions of this model, the readers are referred to the original paper (Wu and Mosleh, 2019).

# 3.3.1.2 Pitting Corrosion 

Pitting corrosion is the most common corrosion mechanism in oil and gas pipelines which happens locally and leads to localized pits, which is often referred to as pitting corrosion. The consequence is disastrous and hard to detect without comprehensive and frequent in-line inspection (Papavinasam et al., 2011). In general, it is likely to happen where protective layers are destroyed, and fresh steels are exposed to the corrosive environment. In this dissertation, the Papavinasam model (Papavinasam, 2013; Papavinasam et al., 2010) is adopted to simulate pitting corrosion. Model parameters include wall shear stress (Wall Shear Stress), total operating pressure $(P)$, solids $\left(R_{\text {solids }}\right)$, partial pressure of $\mathrm{H}_{2} \mathrm{~S}(p H 2 S)$, partial pressure of $\mathrm{CO}_{2}(p C O 2)$, temperature (Temperature), sulfate ions concentration ( $\left[\mathrm{SO} 4^{2-}\right]$ ), bicarbonate ions concentration ( $\left[\mathrm{HCO}_{3}{ }^{-}\right]$), and chloride ions concentration ( $\left[C l^{-}\right]$). For detailed descriptions of this model, the readers are referred to the original papers (Papavinasam, 2013; Papavinasam et al., 2010).

### 3.3.1.3 Erosion Corrosion

Erosion corrosion is defined as a degradation mechanism of pipe materials by the synergistic effect of mechanical action for erosion and electrochemical action for corrosion. Although it is not as common as pitting or uniform corrosion, it still poses a threat to the oil and gas industry as it accounts for $9 \%$ of corrosion-related pipeline failure (Shirazi et al., 2015). This dissertation applies the Nesic model (Nešić and Postlethwaite, 1991) to simulate erosion corrosion behaviors in which the presence of solids as well as the flow inside the pipes play an important role. The model inputs include operating parameters such as flow velocity (Flow Velocity) and particle mass (Particle Mass) and pipe design parameters such as pipe yield strength (Yield Strength) and impact angle

(Impact Angle). For detailed descriptions of this model, the readers are referred to the original papers (Nešić and Postlethwaite, 1991).

# 3.3.1.4 Microbiologically-influenced Corrosion 

Bacterial activity by microbes tends to form biofilms that become acidic when they trap electrolytes and acids inside the pipe. Then, corrosive environments are developed that are prone to the occurrence of MIC (Jia et al., 2019). The presence of biofilms on the steel surface forms a galvanic cell, promoting galvanic corrosion locally. In this dissertation, MIC behavior is simulated by the Pots model (Pots et al., 2002), which takes operating parameters, environmental parameters, and mitigation parameters into account that are related to the formation of biofilms by microbes. The model inputs include concentration of carbon from fatty acid ( $[C]$ ), use of biocide (Biocide), concentration of oxygen ( $[O]$ ), frequency of pigging (Pigging), concentration of nitrogen ( $[N]$ ), ratio between concentration of carbon and, nitrogen ( $C: N$ ratio), concentration of dissolved solids ([Solids]), flow velocity ( $F V_{M I C}$ ), presence of debris (Debris), and temperature ( $T_{M I C}$ ), each of which corresponds to a value that is used to calculate corrosion rate. For detailed descriptions of this model, the readers are referred to the original paper (Pots et al., 2002).

### 3.3.1.5 Corrosion Fatigue

The presence of corrosive environments and cyclic loads inside the pipe may lead to corrosion fatigue, the synergistic effect of corrosion and fatigue. The sources of cyclic loads in gas transmission pipelines include mechanical vibrations caused by compressor stations and thermal stresses due to significant changes in operating temperatures caused by shutdowns or seasonal variances. This process starts with pitting nucleation by pitting corrosion and then propagates with

fatigue cracks that finally leads to fracture (Arzaghi et al., 2018). This dissertation adopts the Paris law-based model (Harlow and Wei, 1994) to predict the corrosion fatigue behavior assuming corrosion damage already exists as the nucleation point for fatigue cracks. The model inputs include coefficient (Coefficient) representing material characteristics, exponent (Exponent), reflecting mechanistic dependencies, alternating stress intensity $(K)$, which is influenced by alternating stress (Stress Range) and initial pit length (Defect Length), and frequency of change in cyclic load (Frequency).

# 3.3.2 External Corrosion Model 

External corrosion is usually neglected when simulating corrosion; however, it is very important to consider it in the predictive models as external corrosion is found to be the leading cause for rupture incidents, with a corresponding rupture rate of $1.0 \times 10^{-5}$ per km per year (Lam, 2015). The DBN model for external corrosion is shown in Figure 18. The corrosion model of external corrosion considers two common types of external corrosion, namely, pitting corrosion and stress corrosion cracking (SCC); the pitting corrosion model is empirical while stress corrosion cracking model is physics-based. The details of the discretized nodes of the DBN external corrosion model are listed in Appendix B.

![img-17.jpeg](img-17.jpeg)

Figure 18. DBN Model for External Corrosion Prediction

# 3.3.2.1 Pitting Corrosion 

Underground oil and gas pipelines can suffer pitting corrosion due to inadequate cathodic protection or coating disbandment (Peabody et al., 2001). In this dissertation, the Velazquez et al. model (Velázquez et al., 2009) is used to predict the maximum pit depth caused by pitting corrosion. The pit growth rate is described by a power-law function with its pitting proportionality (Coefficient) and exponent factors (Exponent) determined by a variety of soil and pipe parameters including resistivity (Resistivity), sulfate ions concentration ( $\left[S O 4_{2}\right.$-]), bicarbonate ions concentration ( $\left[H C O_{3}\right.$- $]$, chloride ions concentration ( $\left[C l^{\prime}\right]$ ), water content of the soil (Water Content), pH level of the soil ( $p H$ ), pipe/soil potential (Pipe Soil Potential), bulk density of the soil (Bulk Density), and redox potential (Redox Potential). The mitigation operation parameter included in this model is the lifetime of a coating (Coating Lifetime) above which the corrosion

may take place, whereas the effect of cathodic protection is not individually modeled as it is taken into account in the (Pipe Soil Potential) and (Redox Potential) nodes.

# 3.3.2.2 Stress Corrosion Cracking (SCC) 

SCC occurs when oil and gas pipelines are subjected to corrosive soil environments and small loading cycles where mechanical-electrochemical interaction happens. The source of external loading usually results from the longitudinal strain caused by soil movement. Two types of SCC have been identified, namely, high $\mathrm{pHSCC}(\mathrm{pH}>9.0)$ and near-neutral $\mathrm{pHSCC}(\mathrm{pH} \approx 6.5)$ (Liu et al., 2016). However, although SCC has been studied over the past decades, few equation-based predictive models are developed. This dissertation adopts a finite element model firstly developed via COMSOL Multiphysics [43] and later modified by the authors' previous work (Chalgham et al., 2019b) to simulate SCC behaviors. This model studies the changes of corrosion potential and corrosion current density on an already existing corrosion defect on the outer pipe wall subjected to a tensile strain under near-neutral condition. Model inputs include anodic current density (Anodic is) and cathodic current density (Cathodic is) for electrochemical reactions, strain (Strain (Displacement)) for elastoplastic stress modeling, and defect depth (Defect Depth) and defect length (Defect Length) for a corrosion defect geometry. For detailed descriptions of this model, the readers are referred to the original paper (Chalgham et al., 2019b).

### 3.3.3 Mechanical Model

The mechanical model calculates the burst pressure (or remaining strength) based on the accumulated corrosion damage and pipeline design parameters. In this dissertation, the corrosion length degradation (Corrosion Length Rate) is modeled as an independent variable from depth

degradation because there is no direct evidence that the growths of corrosion length and depth are correlated. A linear growth model (Zhou, 2010) is used to predict the total corrosion length (Corrosion Length) after a certain time of operation. On the other hand, the total corrosion depth (Corrosion Depth) depends on corrosion degradation in depth (Corrosion Depth Rate) by different types of corrosion and the time of operation. It should be mentioned that external corrosion will not propagate within the lifetime of external coatings (Coating Lifetime), whereas internal coating is assumed to be not applicable in this model.

As corrosion defect propagates, not only the thickness of the pipe wall reduces but also the remaining strength of the pipe deteriorates, finally leading to failure. Although a number of burst pressure models have been developed to calculate the remaining strength of corroded pipelines, this dissertation uses ASME B31G (Committee, 2009) and DNV-RP-F101 standards (Veritas, 2004) because they are convenient to implement with decent accuracy. However, ASME B31G is only suitable for low toughness steels while DNV-RP-F101 is suitable for medium to high toughness steels. The burst pressure is controlled by the geometry of corrosion defects including defect depth (Corrosion Depth) and defect length (Corrosion Length) as well as the characteristics of pipe materials including pipe length (Pipe Length), pipe diameter (Pipe Diameter), pipe thickness (Pipe Thickness), and yield stress or flow stress (Yield Strength).

The burst pressure equations for ASME B31G mechanical model are shown in equations (1) to (4) where equations (1) to (2) are used to describe the parabolic defects and equations (3) to (4) are used to describe the rectangular defects:

$$
\diamond \quad P_{b}=\sigma_{h} \frac{2 w}{D}=\sigma_{f}\left[\frac{1-\left(\frac{2}{3}\right) \times\left(\frac{d}{w}\right)}{1-\left(\frac{2}{3}\right) \times\left(\frac{d}{M w}\right)}\right]\left(\frac{2 w}{D}\right)=\left(1.1 \sigma_{y}\right)\left[\frac{1-\left(\frac{2}{3}\right) \times\left(\frac{d}{w}\right)}{1-\left(\frac{2}{3}\right) \times\left(\frac{d}{M w}\right)}\right]\left(\frac{2 w}{D}\right)
$$

where $P_{b}$ is the burst pressure; $\sigma_{h}$ is the hoop stress; $\sigma_{f}$ is the flow stress; $\sigma_{y}$ is the yield stress; $w$ is the pipe wall thickness; $D$ is the pipe outer diameter; $d$ is the depth of a corrosion defect; $M$ is the Folias factor which is defined as:

$$
\diamond \quad M=\sqrt{1+0.8\left(\frac{l}{D}\right)^{2}\left(\frac{D}{w}\right)} \quad \text { for } \sqrt{0.8\left(\frac{l}{D}\right)^{2}\left(\frac{D}{w}\right)} \leq 4
$$

where $l$ is the length of a corrosion defect.

$$
\begin{aligned}
& \diamond \quad P_{b}=\left(1.1 \sigma_{y}\right)\left[1-\left(\frac{d}{w}\right)\right]\left(\frac{2 w}{D}\right) \\
& \diamond M=\infty \quad \text { for } \sqrt{0.8\left(\frac{l}{D}\right)^{2}\left(\frac{D}{w}\right)}>4
\end{aligned}
$$

On the other hand, the burst pressure equations for DNV-RP-F101 mechanical model are shown in equations (5) and (6):

$$
\begin{aligned}
& \diamond \quad P_{b}=\left(\sigma_{f}\right)\left[\frac{1-\left(\frac{d}{w}\right)}{1-\left(\frac{d}{M w}\right)}\right]\left(\frac{2 w}{D-w}\right) \\
& \diamond M=\sqrt{1+0.31\left(\frac{l}{\sqrt{D w}}\right)^{2}}
\end{aligned}
$$

# 3.3.4 Reliability Model 

The reliability model calculates the probability of failure in terms of leak and burst as a result of corrosion failures. It is assumed that leak and burst are two independent events and formularized by two limit state functions of leak $\left(g_{1}\right)$ and burst $\left(g_{2}\right)$, respectively. The expressions of limit state functions are as follows:

$$
\begin{aligned}
& \diamond g_{1}=\Lambda-d_{\max } \\
& \diamond g_{2}=P_{b}-P_{o p}
\end{aligned}
$$

where $\Lambda$ is the corrosion allowance (usually defined as $80 \%$ of wall thickness), $d_{\max }$ is the maximum corrosion depth, $P_{b}$ is the burst pressure, and $P_{o p}$ is the operating pressure.

When the maximum corrosion depth is larger than the corrosion allowance, the leak is likely to happen $\left(g_{1}<0\right)$. On the other hand, when the remaining strength (or burst pressure) is lowered to an extent that cannot withstand the operating pressure, the burst will happen and cause disastrous consequences $\left(g_{2}<0\right)$. In this dissertation, the probability of failure given leak ( $P O F$ Leak) or burst ( $P O F$ Burst) is calculated by MCS to account for the uncertainties of the defined loads and strengths in limit state functions as follows:

$$
\diamond P O F=\frac{n[g<0]}{N}
$$

where $P O F$ is the probability of failure (where $P O F \epsilon\{P O F$ Leak, POF Burst $\}$ ); N is the number of simulations; and $n[g<0]$ is the number of failure events (where $g \epsilon\left\{g_{1}, g_{2}\right\}$ ).

In general, the pipe is regarded as failed when either of these two failure events takes place. Therefore, the one that has a higher probability will be regarded as the probability of failure by corrosion ( $P O F_{-} \operatorname{corr}$ ):

$$
\diamond \text { POF_corr }=\max (P O F \text { Leak, POF Burst })
$$

where POF_corr $\epsilon$ \{POF Internal Corrosion, POF External Corrosion\};
POF Internal Corrosion is the failure probability of internal corrosion; and POF External Corrosion is the failure probability of external corrosion. Note that both POF Leak and POF Burst are different in terms of internal and external corrosion, yielding different POF Internal Corrosion and POF External Corrosion.

To sum up, the HCL methodology along with the corrosion DBNs provides an effective way of dynamically modeling complex systems where the top-down decomposition of the real-time and projected pipeline system failure probability is modeled by FTs while common cause failures or corrosion degradations are modeled by DBNs. Based on the prediction results, optimal mitigation actions will be provided in the next chapters to reduce the risk of pipeline failures in a cost-efficient way.

# 3.4 Compressor Failure Predictive Modeling 

Compressor failure is one of the main contributors to the pipeline network failure as described by the fault tree in Figure 15. The probability of a compressor failure over time is modeled with the compressor reliability data provided in the literature (Spüntrup et al., 2018) and shown in Figure 19.
![img-18.jpeg](img-18.jpeg)

Figure 19. Gas Compressor Failure Probability over Time (after Spüntrup et al., 2018)

The reliability of the compressor over time is not enough to present a dynamic failure prediction model for the compressors. In fact, the change in the volumetric flow rate reflects the performance degradation of the compressor as shown in Figure 20. This figure shows how the drop in flow rate affects the performance degradation of different compressors with different speeds. In the proposed PHM framework, the flow rate is monitored in real-time from the compressors to quantify their reliability with a better precision; as opposed to only considering the degradation over time. Moreover, the compressor degradation affects the corrosion formation. In fact, the change in flow rate is a contributor to the change of corrosion rate as described by the corrosion DBN models. This performance dependency will be explained in more detail in the next chapter.
![img-19.jpeg](img-19.jpeg)

Figure 20. Compressor Performance Degradation based on Flow Rate Drop (after Safiyullah et
al., 2018)

# 3.5 Human Error Modeling 

The human error is one of the causes of pipeline failure. BNs can be used to model the human error in the control room operations and the maintenance operations. As shown in Figure 21, the human error in the control room operations can be caused by the Human System Interface (HSI) or by the team. The time constraint, task load, stress level, bias, knowledge or abilities, level of training, effectiveness, fatigue, resources, and the procedures are all causes that can affect the team.
![img-20.jpeg](img-20.jpeg)

Figure 21. Human Error in the Control Room Operations BN

The human error in the maintenance operations can be caused by internal or external factors as shown in Figure 22. Internal factors include the stress level, fatigue, experience, and level of training. External factors can be environmental (weather conditions or workplace temperature) and operational (lack of reporting and recording system, workload level, noise and vibration, or improper pipeline installation).

The human error in the maintenance operations can be seen as an optimization problem. The increase of the maintenance activities will increase the cost and reduce the likelihood of pipeline failures assuming no human error. However, the increase of the maintenance activities will increase the human error in the maintenance operations which increases the likelihood of pipeline failures. As a result, taking human error into consideration is very important in developing a cost-effective maintenance schedule optimization.
![img-21.jpeg](img-21.jpeg)

Figure 22. Human Error in the Maintenance Operations BN

# CHAPTER 4 

## 4. Failure Propagation Modeling

In this chapter, the failure propagation modeling in systems is presented. A system is a system with multiple inter-dependent components that are connected physically and functionally. In most engineered systems the interdependencies pose a formidable challenge in understanding and prediction of system vulnerabilities in terms of degradation and failure propagation paths. In this chapter a framework is proposed to model the complex inter-dependent system-level failure. The approach views systems as multiple inter-connected layers as shown in Figure 23.

In the physical layer, the components' degradations are modeled by taking into consideration the physics of degradation behavior as well as the interaction between components.
![img-22.jpeg](img-22.jpeg)

Figure 23. System-Level Failure Propagation Methodology

Here, $\alpha_{j i}$ denotes the physical "connection strength between component j and i , in other words, how the degradation of component $j$ is affecting component $i$. The connection strengths along with a complex network mathematical modeling (such as complex network theory and

centrality measure analysis) will model the importance/criticality level of a component in the system.

Once the degradation of a component is quantified, a network model (such as a Fault-Tree analysis), is used to quantify the system failure probability.

# 4.1 Complex Network Theory 

In order to model the physical dependencies between components, complex network theory can be used. Modeling complex systems can be achieved by using a network representation that shows system structure and topology. It is a tool that can be used to enhance system reliability analysis of complex systems by providing a "natural framework for the mathematical representation of system topology" (Lin et al., 2018). The system is represented by a set of nodes connected by edges/links.

Centrality measures are a way to represent the information about the relative importance of nodes and edges in a graph. The goal of this tool is to identify the most important vertices within a graph and helps in modeling and representing complex systems from representation and mathematical perspectives. Figure 24 shows multiple centrality measures of the same graph.
![img-23.jpeg](img-23.jpeg)

Figure 24. Multiple Centrality Measures of the same Graph:
(a) Degree Centrality, (b) Closeness Centrality, and (c) Betweenness Centrality

Degree centrality (Freeman, 1978) measures the number of direct neighbors. Closeness centrality (Sabidussi, 1966) quantifies the average length of the shortest path between the node and all other nodes in the graph. Thus the more central a node is, the closer it is to all other nodes. Betweenness centrality (Brandes, 2001) quantifies the number of times a node acts as a bridge along the shortest path between two other nodes.

# 4.2 Centrality Measures 

### 4.2.1 Degree Centrality

Degree Centrality is a measure of the number of connections a node has with other nodes. The Degree Centrality can be interpreted in terms of the immediate risk of a node getting affected by a failure mechanism of other connected nodes such as vibration. It is a primary metric of significance within its local environment. Degree Centrality is mathematically defined as:

$$
\diamond D C_{i}=\frac{N_{i}}{n-1}
$$

where $N_{i}$ is the number of links connected to node i and $n$ is the total number of nodes in a network. The Degree Centrality is a normalized measure from 0 to 1 , where 1 means that a node is connected to all other nodes.

Degree Centrality captures only what is happening locally around that node, it doesn't really tell us where the node lies in the network, which is needed to get a proper understanding of its importance, influence, or criticality within the network. For this reason, other centrality measures are proposed to quantify the global importance of a node.

# 4.2.2 Closeness Centrality 

Closeness Centrality captures how close a node is to any other node in the network, that is how quickly or easily can the node reach other nodes. It is a measurement of the node's capacity to affect all other elements in the network. It can also be viewed as a measure of how long it will take to spread a failure mode such as overheating from the node of interest to all other nodes sequentially. Closeness Centrality is mathematically defined as:

$$
\diamond C_{i}=\frac{n-1}{\sum_{i \neq j \leq n} d_{i j}}
$$

where $n$ is the total number of nodes in a network and $d_{i j}$ is the shortest path length between nodes i and j. Thus, the more central a node is the lower its total distance to all other nodes. The Closeness Centrality is also a normalized measure from 0 to 1 , where higher measures describe more central nodes.

### 4.2.3 Betweenness Centrality

Betweenness Centrality captures the node's role as a connector or bridge between other groups of nodes. It quantifies the number of times a node acts as a bridge along the shortest path between two other nodes. It can be seen as a measure to quantify how critical a node is to a network in its functioning as a bridging point between other nodes in the network. Betweenness Centrality is mathematically defined as:

$$
\diamond B C_{i}=\frac{2}{(n-1)(n-2)} \sum_{u \neq i \neq w} \frac{\sigma_{u w}(i)}{\sigma_{u w}}
$$

where $n$ is the total number of nodes in a network, $\sigma_{u w}$ is the total number of shortest paths from node $u$ to $w$, and $\sigma_{u w}(i)$ is the number of those paths that pass through node i. $\frac{2}{(n-1)(n-2)}$ is used

to normalize the Betweenness Centrality between 0 and 1 . For example, in an undirected star graph, the center vertex (which is contained in every possible shortest path) would have a betweenness of 1 while the leaves (which are contained in no shortest paths) would have a betweenness of 0 .

# 4.3 Proposed Failure Propagation Framework 

A methodology to model physical degradations' inter-dependencies is important to capture the failure propagation in a system in an accurate way. As shown in Figure 25, components are susceptible to degrade or fail due to degradation or failure of connected components.
![img-24.jpeg](img-24.jpeg)

Figure 25. Proposed Failure Propagation Framework

The degradation rate of a component $j$ is defined as:
$\diamond$ Degradation Rate of component $\mathrm{j}=\mathrm{DR}_{\mathrm{j}}=f\left(\alpha_{j}, \alpha_{x_{j} j}^{\gamma}\right)$

where $\alpha_{j}$ is the inner degradation rate of component $j, x_{j}$ are the set of components connected to component $j$ and $\alpha_{x_{j} j}^{\gamma}$ is the directed degradation rate effect of components $x_{j}$ on component $j$ by failure mechanism $\gamma$ which can be a linear, physics-based, or BN model.

# 4.4 Compressor/Valve Performance Degradation effect on Corrosion Degradation 

For the gas transmission pipeline network, the compressor or valve performance degradation has an effect on the pipeline corrosion degradation as presented in Figure 26. The real-time variation in operating parameters (operating pressure and mass flow rate) affects the compressor or valve performance which affects the gas flow rate which affects the corrosion rate in the pipeline.
![img-25.jpeg](img-25.jpeg)

Figure 26. Compressor/Valve Performance Degradation effect on Corrosion Degradation

![img-26.jpeg](img-26.jpeg)

Figure 27. Flow Rate effect on Corrosion Rate

As explained in Chapter 3 and described by the BN in Figure 27, the gas flow rate affects the flow velocity which affects the uniform and pitting corrosion depth rates.

In fact, based on the physics-of-failure (POF)-based semi-empirical uniform corrosion model (Wu and Mosleh, 2019), the flow velocity affects the corrosion current density in stage I of corrosion as described by equations 15 and 16, and affects the sulfide layer mechanical damage rate in stage II of uniform corrosion as described by equations 17 and 18.

$$
\diamond \quad \mathrm{CR}_{\mathrm{I}}=\frac{\mathrm{i}_{\mathrm{corr}} \mathrm{M}_{\mathrm{Fe}}}{\rho_{\mathrm{Fe}} 2 \mathrm{~F}}
$$

where $\mathrm{CR}_{\mathrm{I}}$ is the corrosion rate at stage $\mathrm{I}, \mathrm{i}_{\text {corr }}$ is the corrosion current density, $\mathrm{M}_{\mathrm{Fe}}$ is the molar mass of iron, $\rho_{\mathrm{Fe}}$ is the density of iron, and F is the Faraday constant.

$$
\diamond \quad \mathrm{i}_{\mathrm{corr}}=\mathrm{f}\left(\mathrm{~V}, \mathrm{~T}, \mathrm{P}_{\mathrm{CO} 2}, \mathrm{P}_{\mathrm{H} 2 \mathrm{~S}}\right)
$$

where V is the flow velocity of gas, T is the temperature, $\mathrm{P}_{\mathrm{CO} 2}$ is the partial pressure of $\mathrm{CO}_{2}$, and $\mathrm{P}_{\mathrm{H} 2 \mathrm{~S}}$ is the partial pressure of $\mathrm{H}_{2} \mathrm{~S}$.

$$
\diamond \quad \mathrm{CR}_{\mathrm{II}}=\frac{\mathrm{SDR}_{\mathrm{M}}}{\alpha}
$$

where $\mathrm{CR}_{\mathrm{II}}$ is the corrosion rate at stage II, $\mathrm{SDR}_{\mathrm{M}}$ is the sulfide layer mechanical damage rate, and $\alpha$ changes over time and is simulated by a BBN.

$$
\diamond \alpha=\mathrm{f}\left(\mathrm{~V}, \mathrm{~T}, \mathrm{P}_{\mathrm{H}_{2} \mathrm{~S}}, \mathrm{pH}\right)
$$

where V is the flow velocity of the gas, T is the temperature, $\mathrm{P}_{\mathrm{H} 2 \mathrm{~S}}$ is the partial pressure of $\mathrm{H}_{2} \mathrm{~S}$, and pH is the pH level.

As a result, the flow velocity has an effect on the uniform corrosion rate.
In addition, based on the Papavinasam pitting corrosion model (Papavinasam, 2013; Papavinasam et al., 2010), the flow velocity affects the pitting corrosion rate. In fact, the flow rate affects the wall shear stress as described by equations 19 and 20, which affects the pitting corrosion rate as described by equation 21 .

$$
\diamond \mathrm{P}_{\text {down }}^{2}=\mathrm{P}_{\mathrm{up}}^{2}-25.2\left(\frac{\mathrm{~S}_{\mathrm{g}}^{\mathrm{S}} \mathrm{ZTfL}}{\mathrm{D}^{\mathrm{S}}}\right)
$$

where $\mathrm{P}_{\text {down }}$ and $\mathrm{P}_{\text {up }}$ are the pressures at the outlet and inlet respectively, S is the specific gravity of gas, $\mathrm{Q}_{\mathrm{g}}$ is the gas volumetric flow rate ( $=$ flow velocity $(\mathrm{V}) *$ cross-section area of the pipe $(\mathrm{A})$ ), Z is the compressibility factor, T is the temperature, f is the Moody friction factor, L is the length of the pipe, and D is the inner diameter of the pipe.

$$
\diamond \text { Wss } \propto \mathrm{dP} * \frac{\mathrm{D}}{\mathrm{~L}}
$$

where Wss is the wall shear stress and dP is the pressure drop $\left(=\mathrm{P}_{\text {up }}-\mathrm{P}_{\text {down }}\right)$.

$$
\begin{aligned}
\diamond \mathrm{PCR}_{\text {mean }} & =\left\{\left(-0.33 \theta_{\mathrm{c}}+55\right)+(0.51 \mathrm{~W} \%+12.13)+\left(0.19 \mathrm{~W}_{\mathrm{ss}}+64\right)\right. \\
& +\left(25 \mathrm{R}_{\text {solid }}+50\right)+(-0.081 \mathrm{P}+88)+\left(-0.54 \mathrm{p}_{\mathrm{H}_{2} \mathrm{~S}}+67\right) \\
& +\left(-0.63 \mathrm{p}_{\mathrm{CO}_{2}}+74\right)+\left(-0.013\left[\mathrm{SO}_{4}^{2-}\right]+57\right)+(0.57 \mathrm{~T}+20) \\
& \left.+\left(-0.014\left[\mathrm{HCO}_{3}\right]+81\right)+\left(0.0007\left[\mathrm{Cl}^{-}\right]+9.2\right)+\mathrm{PCR}_{\text {addition }}\right\} / 12
\end{aligned}
$$

where $\mathrm{PCR}_{\text {mean }}$ is the mean pitting corrosion rate, $\theta_{\mathrm{c}}$ is the contact angle of oil in a water environment, $\mathrm{W} \%$ is the water percentage ( $=$ water production rate/(water + oil production rates) $\times 100$ ), $\mathrm{W}_{\mathrm{ss}}$ is the wall shear stress, $\mathrm{R}_{\text {solid }}$ is 1 if solids exist; otherwise, it is $0, \mathrm{P}$ is the total pressure,

$\mathrm{P}_{\mathrm{H} 2 \mathrm{~S}}$ is the partial pressure of $\mathrm{H}_{2} \mathrm{~S}, \mathrm{P}_{\mathrm{CO} 2}$ is the partial pressure of $\mathrm{CO}_{2},\left[\mathrm{SO}_{4}{ }^{2-}\right]$ is the sulfate concentration, T is the temperature, $\left[\mathrm{HCO}_{3}{ }^{-}\right]$is the bicarbonate concentration, $\left[\mathrm{Cl}^{-}\right]$is the chloride concentration, $\mathrm{PCR}_{\text {addition }}$ is the mean pitting corrosion rate of these 11 individual pitting corrosion rates.

As a result, the flow velocity has an effect on the pitting corrosion rate too.

# CHAPTER 5 

## 5. Degradation-based Operation and Maintenance Schedule Optimization (DOMSO)

In this chapter, the inspection and maintenance schedule as well as the operating parameters optimization models are presented. The proposed Degradation-based Operation and Maintenance Schedule Optimization (DOMSO) aims at optimizing the maintenance schedule of the pipeline components as well as the operating parameters such as the mass flow rate and flow pressure to avoid or reduce the likelihood of failure of the pipeline system at a lower cost.

### 5.1 Overall Mitigation Actions Optimization Framework

After assessing the risk of possible threats to pipeline integrity in the previous chapters, it is essential to take actions to mitigate the system deterioration such as corrosion degradation and prevent pipeline failure. In this dissertation, the integrated predictive models developed in the previous chapters will be incorporated into a dynamic and risk-based decision-support which provides cost-effective and optimal mitigations actions namely inspection/maintenance scheduling, operating parameters, and sensor placement optimizations. The overall mitigation actions optimization framework is shown in Figure 28. It shows how the field data along with the failure mechanism sciences contribute to the optimization models.

The overall goal of the mitigation actions is to avoid or reduce the likelihood of failure of the pipe at a lower cost by the proposed optimal models. The existing field data (historic and realtime) are fed into the corrosion and compressor/valve failure prediction models. Once the failure prediction results are simulated, they are fed into the optimization models.

![img-27.jpeg](img-27.jpeg)

Figure 28. Overall Mitigation Actions Optimization Framework

Since the proposed optimization framework is dynamic, the maintenance schedule and operating parameters optimization results are fed back into the failure prediction models to rerun the simulations, and the sensor placement optimization results are sent to the inspection team for the optimal additional data needed. Once the additional data is received, the flow of the optimization explained above is updated to reflect the most realistic results. One of the novelties of the proposed mitigation actions optimization framework is being proactive by understand the physics of failure of the pipeline-network over time and applying the appropriate/optimized mitigation actions to avoid possible pipeline failures.

# 5.2 Objectives of the DOMSO Framework 

The proposed Degradation-based Operation and Maintenance Schedule Optimization (DOMSO) aims at optimizing the maintenance schedule of the pipeline components as well as the operating parameters such as the mass flow rate and flow pressure to avoid or reduce the likelihood of failure of the pipeline system at a lower cost. In other words, it aims at: (i) reducing the

degradation of the pipeline over time (longer lifetime), and (ii) minimizing the cost of the system in long term operation.

As shown in Figure 29, the pipeline operation cost increases over time due to inspection and maintenance activities, and the income decreases over time as a result. In other studies, the maintenance cost is considered as a constant value such as a constant maintenance cost every 4 years, but in reality, it will increase by the increasing failure rate. In fact, for different mass flow rates or pressures, there are different rates of degradations; increasing the mass flow rate or pressure (by using the valve or the compressor) will increase the rate of pipeline degradation. As a result, by acknowledging the effect of different failure rates, the optimum operating conditions could exist such as the optimum mass flow rate and optimum pressure.

In addition, in other systems, after a time interval of 4 years for instance, a constant amount of money (dashed green bar in Figure 29) is paid to do maintenance but in the proposed DOMSO model, it is split into different amounts; the maintenance cost that depends on operating conditions. For different operating conditions, different failure rates exist and those failure rates affect the maintenance cost and the sum of all these maintenance costs will be equal to the initial maintenance cost at year $\mathrm{t}_{4}$ (as shown in Figure 29) without splitting. The advantage now is that the maintenance date is delayed to year $t_{6}$ for instance, which in the long run has a huge economic benefit.
![img-28.jpeg](img-28.jpeg)

Figure 29. Objectives of the DOMSO Framework

# 5.3 DOMSO Modeling 

From an optimization modeling perspective, the Degradation-based Operation and Maintenance Schedule Optimization (DOMSO) model aims at simultaneously optimizing the pipeline safety, environmental, and operating economic aspects as shown in Figure 30. The complexity of the model arises from the multiple interconnected factors affecting the optimization objectives. The pipeline, compressor, and valve degradations along with the changing operating parameters, corrosion level, and human error affect directly the pipeline reliability. As for the economic profit, it is affected by the gas delivery profit, purchased gas cost, compressor fuel cost, maintenance cost, and downtime cost. Finally, the compressor and pipeline operation affect the $\mathrm{CO}_{2}$ emission amount.
![img-29.jpeg](img-29.jpeg)

Figure 30. Optimization Objectives: Simultaneously Optimize the Pipeline
Safety, Environmental, and Operating Economic aspects

The goal of the optimization model is to maximize the objective function which is defined as:

$$
\begin{aligned}
\lozenge \text { Objective Function }= & w_{P R} * \text { Pipeline Reliability }+w_{C O 2} *\left(1-\mathrm{CO}_{2} \text { Emission Amount }\right) \\
& +w_{E B} * \text { Economic Benefit }
\end{aligned}
$$

where $w_{P R}, w_{C O 2}$, and $w_{E B}$ are the objective function weights for Pipeline Reliability, $\mathrm{CO}_{2}$ Emission Amount, and Economic Benefit respectively.

The optimization outputs are the maintenance intervals and operating parameters (pressure and mass flow rate) as shown in Figure 31. The maintenance intervals include the pipeline as well as the compressor, and valve inspection and maintenance schedules. For the pipeline system, different maintenance activities are considered such as the use of batch corrosion inhibitor, internal coating, cleaning pigging, and replacement. Each of these maintenance activities has a related cost, lifetime, and downtime as presented in Table 2. Maintenance Activities and their related Cost and Downtime. The presented data are extracted from the literature (Mahmoodzadeh et al., 2020).
![img-30.jpeg](img-30.jpeg)

Figure 31. Optimization Outputs

Table 2. Maintenance Activities and their related Cost and Downtime


The last step in the optimization model is to define the constraints. For the DOMSO framework, the optimization constraints consist of degradation, operation, environmental, economic, and process model constraints as described in Figure 32.
![img-31.jpeg](img-31.jpeg)

Figure 32. Optimization Constraints

The equations used in these constraints are described in equations 23 through 29:

# $\diamond$ Average Monthly Profit (dollar) 

$=\mathrm{f}$ (Operating Pressure, Mass Flow Rate)
$=$ Gas Delivery Profit - (Gas Cost + Compressor Fuel Cost + Maintenance Cost)
$\diamond$ Gas Delivery Profit (dollar)
$=$ Gas Flow Rate $\left(\mathrm{ft}^{3} / \mathrm{hr}\right) *$ (Total time - Unavailability time) $(\mathrm{hr}) *$ Selling gas price $\left(dollar / \mathrm{ft}^{3}\right)$
$\diamond$ Gas Cost $(dollar)$
$=$ Gas Flow Rate $\left(\mathrm{ft}^{3} / \mathrm{hr}\right) *$ (Total time - Unavailability time) $(\mathrm{hr}) *$ Buying gas cost $\left(dollar / \mathrm{ft}^{3}\right)$
$\diamond$ Compressor Fuel Cost $(dollar)$
$=$ Compressor Power $(\mathrm{kW}) *$ Operating Time $(\mathrm{hr}) * \frac{3412.14 B t u}{1 k W . h r} * \frac{\text { Gas Fuel cost }(dollar)}{10^{6} B t u}$
$\diamond$ Unavailability time $(\mathrm{hr})$
$=\mathrm{f}($ Operating Pressure, Mass Flow Rate)
$=\sum($ Maintenance type $*$ Downtime $)+$ number of failures $*$ unavailable time
$\diamond$ Compressor Power $(\mathrm{W})=\frac{\dot{m} * P_{i} * k}{(k-1) * \rho_{i} * \eta_{c}}\left[\left(\frac{P_{e}}{P_{i}}\right)^{1-1 / k}-1\right]$
where $P_{i}$ is the inlet or suction pressure $\left(\mathrm{N} / \mathrm{m}^{2}\right), P_{e}$ is the exit or discharge pressure $\left(\mathrm{N} / \mathrm{m}^{2}\right), k$ is the ratio of specific heats $\left(=\mathrm{c}_{\mathrm{p}} / \mathrm{c}_{\mathrm{v}}\right), \rho_{i}$ is the inlet gas density $\left(\mathrm{kg} / \mathrm{m}^{3}\right), \eta_{c}$ is the isentropic compressor efficiency, and $\dot{m}$ is the mass flowrate $(\mathrm{kg} / \mathrm{s})$ defined as:
$\diamond$ Mass Flowrate $\dot{m}(\mathrm{~kg} / \mathrm{s})=\rho^{*} \mathrm{Q}=\rho^{*} \mathrm{~V}^{*} \mathrm{~A}$
where $\rho$ is the density of the fluid $\left(\mathrm{kg} / \mathrm{m}^{3}\right), \mathrm{Q}$ is the volumetric flowrate $\left(\mathrm{m}^{3} / \mathrm{s}\right), \mathrm{V}$ is the average velocity $(\mathrm{m} / \mathrm{s})$, and A is the cross-sectional area $\left(\mathrm{m}^{2}\right)$.

# 5.4 Inspection and Maintenance Schedule Optimization 

The proposed DOMSO framework relies on the development of an inspection and maintenance schedule optimization model as shown in Figure 33. The model presents firstly, the recommended inspection actions based on the corrosion predictions without maintenance taken during the operation and, secondly, the optimal operating parameters and schedule and type of maintenance practices to be performed from a high-reliability and cost-effective point of views.

The inspection recommendation module provides recommended practices given the corrosion risk in terms of failure probability (POF Internal Corrosion) given by Equation (10). Recommended practices include doing nothing, inspection, and repair based on the DNV-RP-F101 standard (Anon, 1999, p. 101). Specifically, it uses the failure probability as a basis to determine the recommended practices. The threshold values of the failure probability together with the corresponding recommended practices are shown in Table 3.
![img-32.jpeg](img-32.jpeg)

Figure 33. Framework of the Inspection/Maintenance Schedule Optimization

Table 3. Deterministic Recommended Practices Criteria (DNV-RP-F101)


The maintenance schedule optimization module provides optimized maintenance types and times in order to mitigate corrosion risks from reliability and cost-effective ways. This module takes advantage of a reinforcement learning (RL)-based maintenance scheduler following the condition-based maintenance (CBM) policy (Mahmoodzadeh et al., 2020). The goal of a RL-based agent is to maximize expected cumulative rewards in the long run. In this dissertation, the goal of the maintenance scheduler is to extend the lifetime of the pipeline at a minimal maintenance cost.

The framework of the maintenance scheduler is shown in Figure 34. The maintenance scheduler consists of a system (i.e., natural gas transmission pipeline segment) and a RL-based agent, both of which are interacting with each to achieve the goal. A pipe model is used to simulate the system in which the pipe model is composed of a corrosion model that can quantify the corrosion degradation and a reliability model that can determine if the pipeline fails by either leak or burst as a result of corrosion degradation.

As for the agent, it can be formularized by Markov decision process $\{$ State $(s)$, Action (a), Reward $(r)$, Time $(t)\}$. Specifically, the agent has access to the state of the pipeline (i.e., State) through monthly inspection and receive cost (i.e., Reward) from the system.

![img-33.jpeg](img-33.jpeg)

Figure 34. Framework of the RL-based Maintenance Scheduler

The state should represent the health condition of the pipelines and can be formularized as:
$s \epsilon\{C D P, C L P, C R P\}$
where $C D P$ is the corrosion depth percentage; $C L P$ is the corrosion length percentage; and $C R P$ is the corrosion rate presence, a binary variable denoting if the corrosion degradation is mitigated. Reward returns the feedback to the agent about how well it performs to achieve the goal and can be represented as:
$r \epsilon\{$ cost of failure, cost of maintenance, life extension reward $\}$
where cost of failure is the cost associated with leak and burst failures, cost of maintenance is the cost associated with maintenance practices, and life extension reward is the bonus to encourage the agent to extend the lifetime of the pipeline.

Based on the generated information, it can select one action which will immediately influence the condition of the pipeline and backpropagate to the agent in terms of reward. Action can be represented as:

a $\epsilon\{$ do nothing, batch corrosion inhibitor, internal coating,
cleaning pigging, replacement $\}$
where do nothing means no mitigation is done, batch corrosion inhibitor drops the corrosion rate based on inhibitor efficiency, internal coating isolates the pipe from the corrosive environment and stops corrosion propagation during its lifetime, cleaning pigging cleans up liquids, solids, and debris, stopping corrosion propagation during its lifetime, and replacement replaces the whole corroded pipe segment.

The algorithm used to train the agent is Q-learning, which aims at learning the optimal actionvalue functions (i.e., Q-values) to derive the optimal maintenance management policy. Q value is a function that estimates the worthiness of each action at each state. In other words, Q value is cumulative discounted future rewards that can be expected if the agent starts from state $s$ then performs action $a$ at time $t$ following the policy $\pi$, which can be represented as:

$$
Q^{\pi}(s, a)=E\left[\sum_{k=0}^{\text {episode length }} \gamma^{k} r_{t+k+1} \mid s_{t}=s, a_{t}=a\right]
$$

where $\gamma$ is the reward decay constant.
The training process is run on a daily granularity in a simulation of the corrosion degradation for 1000 episodes with the simulation time steps of 40 years. Each epoch ends by either replacement, pipeline failure, or end of simulation scope is triggered. After the agent is well trained, the Q-table representing updated Q values with respect to all state spaces of the pipeline system is used in this dissertation to provide the optimized maintenance schedule. For more details about the development of the maintenance scheduler, the readers are referred to (Mahmoodzadeh et al., 2020).

# 5.5 Inspection/Maintenance Measures for Compressor Stations 

Based on the failure analysis of the compressor (Section 4.3) and the literature on compressor maintenance activities (Safiyullah et al., 2018), inspection and maintenance measures are proposed based on the performance degradation of the compressors and the drop in the volumetric flow rate. The inspection and maintenance measures are related to the alarm system for the compressor which is related to its performance degradation as shown in Figure 35. This figure shows the compressor performance degradation over time with the Alarm system.

The alarm system is used to model the limit thresholds for performance degradations. The first alarm (Alarm 1) is triggered when the performance of the compressor is reduced by $20 \%$, and the second alarm (Alarm 2) is triggered when the degradation reaches $30 \%$. At Alarm 1, the maintenance engineers should inspect the compressors and start ordering spare parts required for the maintenance. At Alarm 2, the gas transportation must be terminated, and maintenance or replacement is required for the compressor as the degradation is reduced by $30 \%$. Beyond the $30 \%$ degradation point, the operation of the compressor at any speed is not safe and the failure of the equipment is likely to happen.
![img-34.jpeg](img-34.jpeg)

Figure 35. Compressor Performance Degradation over time with an Alarm System

# CHAPTER 6 

## 6. Degradation-based Sensor Placement Optimization (DSPO)

Maintenance schedule optimization is important to mitigate pipeline failures in an optimal way, but more mitigation actions are still needed to prevent in a more efficient way these pipeline failures. In this dissertation, the sensor placement optimization framework is presented to prevent or reduce the likelihood of pipeline failures by optimizing the sensor placement in the pipeline network in a way that maximizes the damage detection probability at a minimal cost. While the current sensor placement methodologies are reactive techniques based on the measured corrosion levels, the proposed sensor placement optimization is not only reactive but also proactive at the same time because it is based on current and projected corrosion level formation predictions over the pipeline network.

### 6.1 Motivation

Collecting data about the pipe conditions either by sensors or human inspection can be expensive if they are not implemented in an optimal design. The data gathering methods and techniques are very costly as explained in chapter 1 and therefore they cannot be used along all the pipelines for inspection or monitoring purposes, which leads to only some pipeline sections being inspected. This explains why sensor network design and human inspection planning are popular in the domain of PHM research. In the proposed PHM modeling framework, the sensor placement optimization addresses these limitations by suggesting the optimal places to inspect or place sensors, therefore increasing the efficiency of the data gathering methods and techniques in terms of defect detection.

# 6.2 Optimization Objectives 

In view of the above-mentioned challenges and the discussed modeling limitations in the introduction, this dissertation proposes a system-level dynamic and cost-effective sensor placement optimization framework that could be applied to complex systems. As shown in Figure 36, this framework aims at maximizing the damage detection probability at a minimal cost based on physics-based degradation models such as dynamic corrosion Bayesian Network predictive models.
![img-35.jpeg](img-35.jpeg)

Figure 36. Optimization Objectives: Maximize Damage Detection at a Minimal Cost

### 6.3 Proposed Framework

The proposed comprehensive and dynamic sensor placement optimization framework is composed of multiple modules as presented in Figure 37. It consists of 3 main layers, namely user/field inputs, computation engine, and outputs/results. The user/field inputs layer provides the pipeline information, real-time operating parameters, historic sensor data, pipeline segments information, sensor information, and cost budget to the computation engine. The computation engine has 5 connected modules which will be described in the next sub-sections.

![img-36.jpeg](img-36.jpeg)

Figure 37. Proposed Sensor Placement Optimization Framework

# 6.3.1 Corrosion Predictive Model (Dynamic BN) 

The sensor placement optimization makes use of the developed causal models discussed in this dissertation to find the optimal locations to place sensors along the corroded pipelines in order to maximize the likelihood of damage detection at a minimal cost.

The Corrosion Predictive Model module quantifies the damage depth along the pipeline based on a Dynamic Bayesian Network (DBN). The corrosion DBN integrates physics-based models to compute the corrosion damage size (depth) along the pipeline longitudinal axis as it was described in chapter 3 (Figure 17). This model takes into consideration the spatial and temporal variability of operating parameters. The dynamically updated DBN model is able to calculate the corrosion rate considering the changing variables and related uncertainties.

In addition, history data of corrosion defects distributions can provide information such as longitudinal and circumferential location and intensity of corrosion degradation as well as their

size distribution. They are generated based on the corrosion simulation models described in chapter 3. The corrosion models enable the prediction of corrosion propagation, making the future planning of sensor placement feasible based on the current conditions.

# 6.3.2 High-Likelihood Damage Sampling 

The High-Likelihood Damage Sampling module aims at providing a damage and sensor network layout. The damages provided by the Corrosion Predictive Model module are filtered based on high-likelihood corrosion locations. These locations are mainly at the bottom half of the pipeline due to water accumulation causing the corrosion. The stochasticity of the damage locations is also taken into consideration. In addition, this module classifies the damage (corrosion depth) into 4 classes according to its severity. The classification levels are related to the proportion of the corrosion depth to the pipeline wall thickness as shown in equation 34 and Table 4.
$\diamond$ Corrosion Depth Percentage (CDP) $=\frac{\text { Corrosion Depth }}{\text { Pipe Wall Thickness }}$

Table 4. Size Classes for Corrosion Defects


Moreover, this module assigns potential sensor locations that will be used in the next optimization modules. A node is placed near each corrosion defect in which the longitudinal location is the same as that of the corresponding corrosion defect, whereas the circumferential

location is randomly distributed with respect to that of the corresponding corrosion defect. The nodes are placed at possible locations of sensors, and the way of placing nodes is to provide the optimization model flexibility for distinguishing different detection methods.

This module outputs a 2-D layout design of the locations of corrosion damage and sensor nodes for the pipeline under study. The layout is a representation of an unrolled pipeline where the circumferential axis denotes the perimeter, and the longitudinal axis denotes the length of the original pipeline.

# 6.3.3 Damage Clustering (Constrained K-means) 

Once the damage locations are specified by the High-Likelihood Damage Sampling module, the Damage Clustering module groups these damages in optimal clusters. The purpose of the clustering is to make the optimization algorithm scalable, applicable to complex networks, and faster in computation. The clustering algorithm is composed of two steps. The first step is computing the optimal clusters based on the k-means methodology and the second step is to apply the constraints provided by the complex system analysis.

The k-means clustering methodology (Wagstaff et al., 2001) aims at partitioning a data set into k groups (clusters). The clusters should have a center placed in the centroid of the corresponding cluster by performing 2 steps as shown in Figure 38. This method proceeds by selecting k initial cluster centers and then iteratively refining them as follows:

1. Each instance (damage) $x_{i}$ is assigned to its closest cluster center (eq.35):

$$
\diamond C_{k}=\min _{C}\left\|x_{i}-\mu_{C}\right\|^{2} \quad \forall i
$$

where $C_{k}$ is the cluster $k, x_{i}$ is the location of damage $i$, and $\mu_{C}$ is the center of the cluster.

2. Each cluster center $\mu_{C}$ is updated to be the centroid (mean) of its constituent instances (eq.36):

$$
\diamond \mu_{C}=\frac{1}{n} \sum_{i \in S_{C}}^{n} x_{i} \quad \forall C
$$

where $S_{C}$ is the set of all data points in cluster $C$, and $n$ is the total number of damages in $S_{C}$. The algorithm repeats these steps until it converges.

The clustering results provided by the k-means algorithm needs to have some constraints in order to be scalable and be applied to complex systems. The constraints specify which damages should be grouped together in the same cluster and which damages shouldn't be grouped together in the same cluster for optimal results. In order to analyze the system and provide the constraints, complex network theory importance measures which were described in chapter 4 can be used as a way to define constraints.
![img-37.jpeg](img-37.jpeg)

Figure 38. K-Means Clustering Methodology

# 6.3.4 Damage Detection Probability Quantification 

The damage detection probability quantification module computes the detection probability matrices for different sensor types. The matrices quantify the damage detection probability of all possible scenarios of damage and sensor locations. The relationship between damage non-

detection probability and the damage to sensor distance is an exponential function (Chatterjee and Modarres, 2013). The damage non-detection probability (DNDP) is given by:

$$
\diamond \operatorname{DNDP}(\text { dist })=e^{\frac{\text { dist }}{a}+b}
$$

where dist is the distance between the damage and the sensor, and a and b values are specific to the sensor type and obtained by applying the following constraints:

- $\operatorname{DNDP}(0)=0$
- DNDP (Sensor maximum coverage radius) $=1$

The a and b values will also change based on the damage class computed in the High-Likelihood Damage Sampling module and the sensor type (Chatterjee and Modarres, 2013) and is taken into consideration when computing the DNDP matrices.

As a result, the damage detection probability (DDP) is given by:

$$
\diamond D D P=1-\text { DNDP }
$$

This module will provide the DDP matrices for the different sensor types and damage classes to the sensor placement optimization module.

# 6.3.5 Sensor Placement Optimization 

The final step in the computation engine is the Sensor Placement Optimization module which is based on the integration of the results of the previous modules. It combines the bi-objective optimization model developed by Aria et al. (Aria et al., 2020, 2018) with the previously described computation modules. The bi-objective function aims at maximizing the damage detection probability (DDP) at a minimal cost.

The goal of the optimization model is to maximize the bi-objective function which is defined as:

# $\diamond$ Objective Function 

$$
=w_{D D P} * \text { Damage Detection Probability }+w_{E C} *(1-\text { Economic Cost })
$$

where $w_{D D P}$ and $w_{E C}$ are the objective function weights for the Damage Detection Probability and Economic Cost respectively.

The constraints to this bi-objective function are:

- DDP matrices for the different sensor types and damage classes.
- Sensor information: type, coverage radius, cost, and accuracy.
- Cost limit: maximum cost to spend.

Finally, the proposed model generates an optimized layout design for sensor placement based on the optimization results from safety and cost-effective point of views.

# CHAPTER 7 

## 7. Pipeline System Integrity Management Software Implementation

The lack of optimal mitigation strategies in gas pipelines is one of the key factors that could be improved by a health monitoring software to increase the awareness of the safety and reliability levels of the infrastructure over time. The developed predictive models will aid operators with strategic investment and preventive actions such as optimizing sensor placement and maintenance schedules. The proposed PHM approach and the developed causal models developed in this dissertation are implemented into a software platform that is developed as a pipeline system integrity management tool to support pipeline operators in decision-making and planning activities. The software platform is built to be a web application. The frontend is built using the React framework and the backend using the Django and GeoDjango framework, all of which are installed on a cloud server for real-time monitoring and dynamic system modeling. React is an open-source, front end, JavaScript library for building user interfaces and Django is a Pythonbased open-source web framework. GeoDjango is a Django module that makes it possible to create geographic Web applications, like location-based services.

The design of the frontend user interface is enhanced by using Material-UI. Material-UI is an open source user interface library based on a set of React components that implement Google's material design specification. On the backend, a MongoDB and PostGIS databases have been created to store the pipeline information, the sensor data, the HCL models, the corrosion models, the sensor placement optimization models and the maintenance optimization models. The corrosion, sensor placement and maintenance optimization models are coded in Python for a better compatibility with the Django framework.

The software presents multiple interconnected modules which are visible to the pipeline operators.

As shown in Figure 39, these modules are presented in three main parts:

1. Control Panel/Room Dashboard: shows the real-time health monitoring of the system by displaying the pipeline network and the live data being streamed from the sensors.
2. Simulation Results Display: shows the system-level reliability by displaying the hybrid causal logic model, the component-level failure probability, and the system-level failure probability results.
3. Dynamic Risk-based Decision Support: shows the optimal mitigation actions by displaying the sensor placement optimization and inspection/maintenance schedule optimization results.

These three parts are accessible through a top navigation bar featuring Pipeline Network Building, Live Data Monitoring, System-Level Reliability, Sensor Placement Optimization, and Maintenance Schedule Optimization modules. In addition, a left side navigation bar is added to enhance the user interaction with the software by displaying the different pipelines and their segments when their checkbox is clicked. The overlay vector layers are added to display the different pipelines based on geospatial data coordinate system (latitude and longitude). The software connects these points with specific width and color (based on user's preference) and the resulting polyline is displayed in the overlay map layer.

![img-38.jpeg](img-38.jpeg)

Figure 39. Software Platform Modules

# 7.1 Real-Time Health Monitoring 

The Control Room Dashboard contains the Pipeline Network Building and Live Data Monitoring modules.

The Pipeline Network Building module enables the user to add the pipeline system to study. The pipeline network can be added manually by specifying the name, pipeline length, inner and outer diameter, yield strength, and inlet and outlet coordinates, or by inserting a shapefile as shown in Figure 40. In addition, the user can click on a specific pipeline once it is created and a popup will be displayed showing the pipeline information.
![img-39.jpeg](img-39.jpeg)

Figure 40. Pipeline Network Building Module

The Live Data Monitoring module displays real-time as well as historic senor data such as pressure drop, temperature, and flow velocity. The sensor detection data is uploaded to the operating platform by the internet as the software is installed on a cloud server. The real-time data

from sensors and other databases feed the predictive causal models which dynamically updates the simulation results.

# 7.2 System-Level Failure Analysis 

The Simulation Results Display contains the HCL, Component-Level Failure Probability, and System-Level Failure Probability modules. These modules quantify the real-time and projected component-level as well as system-level failure probabilities taking into consideration a wide range of causes of failures that can affect the system under study. Once the user selects one on the pipeline that were built previously and displayed in the left sidebar, a default Fault Tree is generated as shown in Figure 41.
![img-40.jpeg](img-40.jpeg)

Figure 41. System-Level Failure Analysis Module

The user can then edit the Fault Tree and has the capability to add or remove as many nodes as desired. One of the main novelties of this software platform is that the probability of failure of

the corrosion nodes is computed in the backend based on the physics-based models described earlier in this dissertation. These models take the sensor data being streamed as an input to the quantification analysis. The real-time quantification based on the changing sensor filed data provides a dynamic layer to the analysis which makes the results more realistic.

# 7.3 Optimal Mitigation Actions 

The corrosion and HCL quantification results are fed into the Dynamic Risk-based Decision Support which contains the Sensor Placement Optimization and Inspection/Maintenance Schedule Optimization modules.

In the Sensor Placement Optimization module, the user specifies the type of sensors they have and the maximum cost they are willing to pay. In addition to the corrosion data, the information about the sensors and cost are sent as an input to the sensor placement optimization model being stored in the backend. Once the user clicks on the "Optimize" button, the software shows the optimal locations to place sensors in order to maximize the likelihood of defect detection and minimize the corresponding cost. Moreover, the likelihood of damage detection based on the proposed layout is displayed.

The Inspection/Maintenance Schedule Optimization module shows, firstly, the recommended inspection actions based on the corrosion predictions without maintenance taken during the operation and, secondly, the optimal schedule and type of maintenance practices to be performed over time from a high-reliability and cost-effective point of views.

The mitigation actions are another novelty of the software platform because they have ability to suggest proactive measures to the operators to prevent or avoid pipeline failures. In addition, the users are able to extend the simulation time to see how the corrosion levels will increase in future time steps for instance and what are the inspection or mitigation actions that will be needed.

# CHAPTER 8 

## 8. Case Study: Kern River Transmission Pipeline Network

A case study was performed on a natural gas transmission pipeline to demonstrate the proposed PHM modeling approach and display the results on a software platform. In this case, a section of the Kern River Gas Transmission Pipeline in Salt Lake City, Utah was chosen as shown in Figure 42 .
![img-41.jpeg](img-41.jpeg)

Figure 42. Kern River Gas Transmission Pipeline

A few assumptions were made for this case study:

- According to the defined modeling framework of the pipeline system, this 36 -inchdiameter steel pipe has 2 transmission phases (denoted as Phase 1 and Phase 2), each of which is composed of one compressor and one pipeline segment.
- The pipeline is assumed to be straight and buried underground.
- The pipeline is subjected to both internal and external corrosion.

- The inner pipe wall is presumed to be new at the beginning of corrosion simulation, and corrosion defects gradually develop over time depending on the time-varying operating conditions, whereas there are existing corrosion defects on the outer pipe wall.
- Due to the lack of data about operating conditions, time-varying operating parameters are simulated by the stochastic process approach (Wu and Mosleh, 2019) and their values are based on (Hasan et al., 2012). Moreover, partly soil and pipe data is taken from (Caleyo et al., 2009).
- Operating parameters such as temperature, pressure, partial pressure of $\mathrm{H}_{2} \mathrm{~S}$, and partial pressure of $\mathrm{CO}_{2}$ are assumed to be not only time-dependent but also location-dependent, whereas other operating parameters are only time-dependent.
- No valve degradation is assumed to occur.
- No human error is assumed to occur.


# 8.1 Pipeline System Network Modeling 

The first step to model the pipeline system network is to build the pipeline under study into the software by specifying the coordinates or inserting the shapefiles of pipeline segments in the Pipeline Network Building module. Figure 43 displays the Kern River gas transmission pipeline network building in the software platform.

This pipeline system consists of 2 transmission phases in which Phase 1 transmits natural gas from the Daggett compressor station to the Goodsprings compressor station through the 102.56 miles ( 165.05 kilometers) pipeline segment. Phase 2 transmits the gas from the Goodsprings compressor station to the Dry Lake compressor station through the 86.66 miles ( 139.47 kilometers) pipeline segment.

![img-42.jpeg](img-42.jpeg)

Figure 43. Kern River Gas Transmission Pipeline Network Building in the Software Platform

After the pipeline under study is developed, more data is required to continue the further analysis. The basic design variables of Phase 1 and Phase 2, and the simulated operating parameters of Phase 1 and Phase 2 are shown in Table 5 and Table 6 respectively. Note that Table 6 only displays operating parameters that are related to internal corrosion modeling, and they are continuous random variables in a reflection of the random nature of operating conditions.

Table 5. Basic Design Variables of Phase 1 and Phase 2 of the Kern River Gas Transmission Pipeline


Table 6. Simulated Operating Parameters of Phase 1 and Phase 2 of the Kern River Gas Transmission Pipeline


![img-43.jpeg](img-43.jpeg)

Figure 44. Real-time Operating Parameters at Monitoring Point 1 in the Live Data Monitoring Module in the Software Platform

Real-time operating parameters are observable via the Live Data Monitoring module as shown in Figure 44, where the data streaming from the monitoring point 1 for Phase 1 is presented as an example. In addition, pipeline failures as a result of external corrosion depend on the application and the efficiency of cathodic protection and coatings (Ayello et al., 2014) as well as the soil conditions. Table 7 shows soil and pipe data which applies to both Phase 1 and Phase 2. Note that Table 7 only shows the data that is related to external corrosion modeling.

Table 7. Soil and pipe data of the Kern River gas transmission pipeline


${ }^{1}$ Cathodic $\mathrm{i}_{0}$ and Anodic $\mathrm{i}_{0}$ are exchange cathodic current density and exchange anodic current density, respectively, which are related to operating conditions or the applied mitigation methods such as cathodic protection, etc.
${ }^{2}$ Defect depth and defect length are the geometry of the already existing defect prior to the inspection.
${ }^{3}$ Displacement is the longitudinal strain of the pipe due to soil movements.

# 8.2 System-Level Failure Analysis 

This section shows and discusses the results of the corrosion simulation and system-level failure analysis of the case study.

### 8.2.1 Hybrid Causal Logic (HCL) Modeling

In this case study, all possible failure causes that could break the pipeline system were considered and modeled by the HCL methodology. The system-level fault tree of the Kern River gas transmission pipeline is shown in Figure 45. Two transmission phases, namely Phase 1 and Phase 2, are connected by an "OR" gate because the failure of either phase will fail the whole pipeline system. The probabilities of basic events "Compressor 1 Failure" and "Compressor 2 Failure" were modeled dynamically with the compressor reliability data provided in the literature (Spüntrup et al., 2018).
![img-44.jpeg](img-44.jpeg)

Figure 45. System-Level Fault Tree of Kern River Gas Transmission Pipeline

The probabilities of basic events "Natural Force, "Third-Party Damage", "Material Defect", and "Welding Defect" were taken from the research work presented in the literature (Shan et al., 2017) assuming they are time-independent. Due to the lack of empirical input data information in the form of probability distributions, these values were regarded as median values of Lognormal distributions with error factors of 5 to quantify the uncertainties as shown in Table 8. Modeling the failure rate variability (or failure probability) according to a Lognormal distribution has been proved to be a good approximation (Droguett et al., 2004). Specifically, MCS is used to describe the uncertainties of basic events and propagate them through the whole FT (Diaconeasa, 2017). The probabilities of the corrosion basic events "Internal" and "External" are POF Internal Corrosion and POF External Corrosion obtained from the corrosion simulations through the DBNs.

Table 8. Probabilities of some basic failure events


# 8.2.2 Dynamic BN-based Corrosion Simulation Results 

The corrosion simulation module takes operating parameters from the sensors (see Table 6 and Table 7) and the pipe information (see Table 5) as inputs to predict corrosion degradation in terms of corrosion depth and the corresponding failure probability over time. The simulation is

performed for 30 years of operation. Modeling results by the internal corrosion and external corrosion DBN predictive models are discussed in the following sub-sections.

# 8.2.2.1 Internal Corrosion Simulation Results 

Modeling results by the internal corrosion DBN predictive model were plotted. The timeevolution schematic of predicted internal corrosion degradation and failure probability for the Phase 1 transmission pipeline segment is shown in Figure 46. The results show that corrosion depths increase with increasing time; however, the increase rate drops as corrosion rates decrease over time. It is one of the characteristics of internal corrosion (Heidary et al., 2018; Papavinasam, 2013), which can be attributed to many factors such as the reformation of protective layers, change of corrosion potential, local increase in pH , or local solution saturation.
![img-45.jpeg](img-45.jpeg)

Figure 46. Time-evolution Schematics of Predicted Internal Corrosion Degradation and Failure Probability for Phase 1 Transmission Pipeline Segment

In addition, failure probabilities of leak (POF Leak) and burst (POF Burst) as a result of internal corrosion all show an increasing trend over time, but in this case, the leak is more likely to happen than burst.

According to the system definition, each transmission phase consists of a compressor at the inlet to maintain the transmission force for gas transportation, and this force (i.e., pressure) may decrease over the length of the pipe. Moreover, operating temperature is also found to decrease over the length of the pipe (Lawson, 2005) due to heat transfer during transportation. Therefore, among all operating parameters, the temperature, pressure, partial pressure of $\mathrm{H}_{2} \mathrm{~S}$, and partial pressure of $\mathrm{CO}_{2}$ were considered from a time-dependent as well as location-dependent perspectives. In this case study, deterministic physics-based models were used to model temperature and pressure drops. However, it should be noted that once data is available, it is not necessary to predict the temperature and pressure drops based on the operating parameters at the near inlet.

First, the temperature drop was modeled by considering the heat transfer between fluid and its ambient environment (i.e., soil in this case). The expression of temperature profile can be represented as (Lawson, 2005):

$$
\diamond \quad \mathrm{T}(\mathrm{z})=\mathrm{T}_{\mathrm{amb}}+\left(\mathrm{T}_{\text {inlet }}-\mathrm{T}_{\mathrm{amb}}\right) \exp \left(-\beta_{\mathrm{L}}^{\mathrm{z}}\right)
$$

where $T(z)$ is the temperature at distance " $z$ " along the pipeline, $T_{\text {amb }}$ is the ambient temperature of the soil, $\mathrm{T}_{\text {inlet }}$ is the operating temperature of natural gas at the inlet, L is the length of the pipe, z is the distance along the pipe, and $\beta$ is the pipeline thermal decay constant given by:

$$
\diamond \beta=\frac{\pi D U}{C_{p} M_{\text {flow }}}
$$

where D is the inner diameter of the pipe, $\mathrm{C}_{\mathrm{p}}$ is the specific heat capacity of natural gas, $\mathrm{M}_{\text {flow }}$ is the mass flow rate, and $U$ is the overall heat transfer coefficient $\left(=1 / R_{t}\right)$ where $R_{t}$ is the overall thermal resistance.

For a buried pipe system, $R_{t}$ involves the consideration of thermal resistances of fluid $R_{f}$, pipe $R_{p}$, and soil $\mathrm{R}_{\mathrm{s}}$, and they can be expressed as (Li et al., 2012):

$$
\begin{aligned}
& \diamond \mathrm{R}_{\mathrm{f}}=\frac{1}{\mathrm{~h}_{\mathrm{f}}} \\
& \diamond \mathrm{R}_{\mathrm{p}}=\left(\frac{\mathrm{R}_{1}}{\mathrm{k}_{\mathrm{p}}}\right) \ln \left(\frac{\mathrm{R}_{2}}{\mathrm{R}_{1}}\right) \\
& \diamond \mathrm{R}_{\mathrm{s}}=\left(\frac{2 \pi \mathrm{R}_{1} \mathrm{~L}}{\mathrm{k}_{\mathrm{s}} \mathrm{~S}}\right)
\end{aligned}
$$

where $h_{f}$ is the heat transfer coefficient of natural gas, $R_{1}$ is the inner radius of the pipe, $R_{2}$ is the outer radius of the pipe, $\mathrm{k}_{\mathrm{p}}$ is the thermal conductivity of the pipe, L is the length of the pipe, and $\mathrm{k}_{\mathrm{s}}$ is the thermal conductivity of the soil.

Second, the pressure drop was modeled by the following equation (Griffith, 1984; Taitel et al., 1980):

$$
\diamond \quad P_{\text {down }}^{2}=P_{\text {up }}^{2}-25.2\left(\frac{\mathrm{SQ}_{\mathrm{g}}^{2} Z \mathrm{TfL}}{\mathrm{D}^{\mathrm{s}}}\right)
$$

where $P_{\text {down }}$ is the downstream pressure, $P_{\text {up }}$ is the upstream pressure, $S$ is the specific gravity of gas, $\mathrm{Q}_{g}$ is the gas flow rate, Z is the compressibility factor for gas, T is the temperature, f is the Moody friction factor, and L is the length of the pipe.

Location-dependent corrosion simulations for 30 years of operation were conducted with location ratios (i.e., longitudinal axis/length of the pipe) equal to $0,0.25,0.5,0.75$, and 1 . The

location-evolution schematic of predicted internal corrosion degradation and failure probability for the Phase 1 transmission pipeline segment is shown in Figure 47. The results show that corrosion depths decrease with increasing location along the pipeline. This can be explained by the fact that under the current operating conditions, a higher temperature or partial pressure of $\mathrm{H}_{2} \mathrm{~S}$ and $\mathrm{CO}_{2}$ lead to a higher corrosion rate, and corrosion rates decrease as temperature and pressure drop over the length of the pipe. In addition, it is also noted that the decrease of corrosion depths is less remarkable with the increasing length of the pipe because of decreasing heat transfer, leading to the balance of temperature and pressure. The failure probability at the inlet is almost four times larger than that at the outlet. The same corrosion simulations were also performed for the Phase 2 transmission pipeline in the calculation of POF internal corrosion.
![img-46.jpeg](img-46.jpeg)

Figure 47. Location-evolution Schematics of Predicted Internal Corrosion Degradation and Failure Probability for Phase 1 Transmission Pipeline Segment after 30 Years of Operation

# 8.2.2.2 External Corrosion Simulation Results 

Corrosion simulations of external corrosion were only performed in consideration of timedependency because soil and pipe data (see Table 6) were assumed to be location-independent. Modeling results by the external corrosion DBN predictive model were plotted and shown in Figure 48. It can be seen that due to the application of a coating, the corrosion does not propagate until the lifetime of the coating is reached (i.e., 5 years). The regions of the pipe where the coating is broken then suffer external corrosion, leading to an increase of corrosion depths over operation time. As expected, the POF External Corrosion increases with increasing operation time after the coating has broken for several years. The same corrosion simulations were also performed for the Phase 2 transmission pipeline in the calculation of POF External corrosion.
![img-47.jpeg](img-47.jpeg)

Figure 48. Time-evolution Schematics of Predicted External Corrosion Degradation and Failure Probability for Phase 1 Transmission Pipeline Segment

In short, this corrosion simulation module enables the prediction of corrosion (i.e., internal and external corrosion) degradation and the corresponding failure probability. Once real-time sensor data is available, it can be applied to any location along the pipeline to prioritize the regions for inspection or maintenance practices.

# 8.2.3 System-Level Failure Probability Quantification 

The system-level failure probability distribution after 5 years of operation is displayed in Figure 49. Statistics like mean and median values as well as uncertainty bounds in the form of $5^{\text {th }}$ and $95^{\text {th }}$ percentiles are given. Figure 50 shows the time-evolution system-level failure probability for 30 years of operation.

The results show that the failure probability increases over time and reaches almost 1 after 30 years of operation, implying that if no maintenance practices or repairs are applied during the operation, the pipeline system failure is very likely to happen within 30 years.
![img-48.jpeg](img-48.jpeg)

Figure 49. System-Level Failure Probability Distribution after 5 Years of Operation

![img-49.jpeg](img-49.jpeg)

Figure 50. Time-evolution System-Level Failure Probability for 30 Years of Operation

In order to study the causing factors with respect to their influences on system reliability, importance measures analysis was performed. Here the criticality importance measure was used which is the probability that factor $i$ causes system failure at time $t$ :

$$
\diamond I^{\text {criticality }}(i \mid t)=\frac{I^{\text {marginal }}(i \mid t) \cdot p_{i}(t)}{p_{s}(t)}
$$

where $I^{\text {marginal }}(i \mid t)$ is the marginal importance measure of factor $i$ at time $t\left(=\frac{\partial R_{S}(t)}{\partial R_{i}(t)}\right) ; R_{s}(t)$ and $p_{s}(t)$ are system reliability and system failure probability at time $t$, respectively; $R_{i}(t)$ and $p_{i}(t)$ are reliability and system failure probability of factor $i$ at time $t$, respectively. Figure 51 displays the criticality importance measures of the pipeline system failure after 10 years of operation. The results show that "Compressor Failure" is the main contributor to the system failure; this is due to the significant decrease in reliability of compressors over time if no repair is ever done during the operation (see Figure 19).
![img-50.jpeg](img-50.jpeg)

Figure 51. The Criticality Importance Measures of the Pipeline System Failure at $\mathrm{t}=10$ years

# 8.3 Sensor Placement Optimization 

In this case study, the pipeline was presumed to be free of internal corrosion at the beginning; however, corrosion was assumed to take place along the longitudinal and circumferential axis of the pipeline based on the damage density to perform the sensor placement optimization.

### 8.3.1 High-Likelihood Damage Sampling

After computing the corrosion depths along the pipeline in section 8.2.2 (corrosion degradation was simulated by the proposed internal corrosion DBN predictive model), each corrosion damage is categorized into different size classes based on the corrosion depth percentage (CDP) as it was shown in Table 4. CDP was taken as a criterion for categorization because localized corrosion which propagates mainly in depth is the most disastrous.

Assuming a constant longitudinal damage density of 10 corrosion defects per 50 meters and using a Poisson distribution, the 2-D layout of the corrosion damage and nodes for the Phase 1 transmission pipeline segment is shown in Figure 52. The sensor nodes are placed randomly near the damage locations to allow flexibility in the optimization module for sensors with different coverage capabilities. The layout is a representation of an unrolled pipeline where the circumferential axis denotes the perimeter, and the longitudinal axis denotes the length of the original pipeline. Fewer corrosion defects were assumed to form on the top half of the pipeline compared to the bottom half of the pipeline based on the likelihood of water accumulation. Note that all corrosion defects were categorized to be class 2 because the corrosion depth at each location here is the mean corrosion depth in consideration of time-varying operating parameters.

![img-51.jpeg](img-51.jpeg)

Figure 52. The layout of the Corrosion Damage and Nodes for Phase 1 Transmission Pipeline Segment

In addition, only temperature and pressure-drop were considered to be location-dependent. However, once real-time sensor data is available, variability is expected to be observed. The optimization problem aims at maximizing the probability of defect detection at a minimal cost (limited number of sensors).

# 8.3.2 Damage Clustering (Constrained K-means) 

The damages obtained from the High-Likelihood Damage Sampling module are clustered in the Damage Clustering module. The number of desired clusters was assumed to be 3. The resulting optimal grouping is shown in Figure 53 and summarized in Table 9.
![img-52.jpeg](img-52.jpeg)

Figure 53. Damage Clustering Layout

Table 9. Clusters for Corrosion Defects


# 8.3.3 Damage Detection Probability Quantification 

After getting the corrosion damage and sensor nodes layout from the High-Likelihood Damage Sampling module, the Damage Detection Probability (DDP) matrices for the different sensors are computed. In this case study, 2 sensor types are considered: acoustic-emission sensor, and ultra-sonic sensor.

Table 10. Damage Detection Probability (DDP) Matrix for an Acoustic-Emission Sensor


The acoustic-emission sensor is assumed to have a detection radius of 0.4 meters. The ultrasonic sensor is assumed to be used by human inspection and has a coverage of 20 meters. The DDP matrices for the acoustic-emission and ultra-sonic sensors are shown in Table 10 and Table 11 respectively. The DDP matrix shows the damage (D) detection probability by a sensor located at a sensor node (S). Note that the results of the damage detection probabilities take into consideration the corrosion damage depth quantified in the Corrosion Predictive Model module.

Table 11. Damage Detection Probability (DDP) Matrix for an Ultra-Sonic Sensor


# 8.3.4 Optimization Results 

The sensor placement optimization is the final step of the computation engine. The results from the previous modules are integrated into the optimization algorithm as well as the user/operator inputs displayed in Table 12. The inputs include the available type of sensors, their coverage range, accuracy, and cost. In addition, the operator specifies the cost limit desired.

Table 12. Operator Inputs to the Optimization


The optimal layout is displayed in Table 13 and Figure 54. It shows that the provided sensor network has a damage detection probability of $89 \%$ given that:

- 4 acoustic-emission sensors are placed at nodes $0,2,3$, and 10 which corresponds to longitudinal locations of $0.22 \mathrm{~m}, 12.22 \mathrm{~m}, 19.72 \mathrm{~m}$, and 49.22 m respectively.
- 2 ultra-sonic sensors are placed at nodes 4 and 8 which corresponds to longitudinal locations of 24.22 m , and 47.72 m respectively

Table 13. Output of the Optimization


![img-53.jpeg](img-53.jpeg)

Figure 54. Sensor Placement Optimization Layout for a Small Part of Phase 1 Transmission Pipeline Segment

Compared to a layout of fixed sensor intervals as shown in Figure 55, the optimization increased the probability of damage detection by $34 \%$; from $55 \%$ with a fixed interval sensor placement to $89 \%$ with an optimized sensor placement.
![img-54.jpeg](img-54.jpeg)

Figure 55. Sensor Placement Layout Without Optimization

# 8.4 Inspection/Maintenance Schedule Optimization 

This section presents the inspection recommendation and maintenance schedule optimization results for this case study. Figure 56 shows the result of the inspection recommendation for the Phase 1 transmission pipeline segment that can provide recommended practice based on the current condition of the pipeline. POF Internal Corrosion at different operation times along the pipeline are displayed and compared with the DNV-RP-F101 standard. The results show that inspection is recommended between 5 to 10 years of operation, otherwise, the risk of pipeline failure becomes so high that requires repair to be applied after 10 years of operation. The results of the maintenance schedule optimization module for the Phase 1 transmission pipeline segment that provides optimized maintenance schedule from safety and cost-effectiveness viewpoints are also shown in Figure 56.
![img-55.jpeg](img-55.jpeg)

Figure 56. Results of the Inspection Recommendation and Maintenance Schedule Optimization for Phase 1 Transmission Pipeline Segment

This figure visualizes the decision making by the RL-based maintenance scheduler with respect to different levels of corrosion (i.e., corrosion depth percentage ( $C D P$ ) and corrosion length percentage $(C L P)$ ). The results show that the maintenance scheduler decides to perform no maintenance action at the beginning. Until the corrosion becomes slightly severe ( $C D P$ around $13 \%$ ) after 3 years of operation, it starts to apply cleaning pigging every month between 2.75 and 7.83 years of operation, and between 20.58 and 30 years of operation to mitigate the corrosion propagation. According to (Mahmoodzadeh et al., 2020), cleaning pigging can inhibit corrosion for 2 weeks, after which the corrosion environment will develop again. In between, it selects to perform no maintenance actions in which the corrosion levels increase faster. It decides to apply no maintenance at a certain duration because although the corrosion levels may increase faster, it still poses a small risk and no immediate threat to the pipeline integrity from a cost-effective point of view; therefore, performing no maintenance action outweighs performing any maintenance action at this duration. The maintenance schedule optimization module keeps the $90^{\text {th }}$ percentile of $C D P$ to below 0.4 , which is a relatively secure level after 30 years of operation. Note that decision makings by the maintenance scheduler differs depending on the pipe information and operating conditions; therefore, the optimized maintenance schedule for Phase 2 may be different from Phase 1.

# 8.5 Operating Parameters Optimization 

In this section, the pressure and flow rate are optimized from economic, cost, and environmental perspectives. A total of 6 simulations cases are performed with different operating pressures (P) in bar and flow velocities (v) in $\mathrm{m} / \mathrm{s}$ are shown in Figure 57.
![img-56.jpeg](img-56.jpeg)

Figure 57. Corrosion Predictions and Optimal Maintenance Schedule for Different Operating Pressures and Flow Velocities

The corrosion predictions and optimal maintenance schedule for the different operating pressures and flow velocities are shown in Figure 57. The optimal maintenance schedules are costeffective. When comparing the monthly average maintenance cost with 12 normal (periodic) maintenance costs retrieved from the literature (Mahmoodzadeh et al., 2020), the difference is noticeable as shown in Figure 58 and Table 14.
![img-57.jpeg](img-57.jpeg)

Figure 58. Compared Monthly Average Costs of 12 Cases of Normal (Periodic) Maintenance Schedules and the 6 Cases of Optimal Maintenance Schedules

As shown in Table 14, the optimization of the operating parameters aims at: (i) extending the lifetime of the pipeline, (ii) minimizing the maintenance cost, (iii) maximizing the economic profit, and (iv) minimizing the $\mathrm{CO}_{2}$ emission amount. From the optimization results, having a pressure of 30 bar and flow velocity of $30 \mathrm{~m} / \mathrm{s}$ is the optimal combination of operating parameters as it

decreases the average monthly maintenance cost by $72.5 \%$, increases the average monthly profit by $3.67 \%$, and increases the $\mathrm{CO}_{2}$ emission amount by only $3.65 \%$.

Table 14. Economical and Environmental Benefits of the Optimized Maintenance Schedules


The transmission pipeline is more complex in reality as shown in Figure 59. The gas transmission of Phase 1 is actually performed through 2 parallel lines (denoted as Phase 1a, and Phase 1b), each of which is connected to a compressor and a valve. The compressor is responsible for keeping a desired pressure and the valve is responsible for varying the mass flow rate if needed. The variation of pressure and flow rate, even by a small degree, can have a big impact on the economic benefit but also affects the maintenance costs and $\mathrm{CO}_{2}$ emission amounts as shown in the previous results.

The optimization gets more complex with these 2 parallel lines, and the operators need to know which pressures to keep at both compressors and which flow rates are optimal. In addition, the gas delivery constraint needs to be met at the same time. Table 15 shows the optimal operating parameters for the Phase 1 transmission pipelines. This table shows all combinations of the operating parameters between the 2 parallel lines considering the 6 simulation cases. The operators select the desired constraints: $0.066 \mathrm{Bcf} / \mathrm{d}$ for gas delivery demand, $dollar 600,000,000 /$ month for minimum economic profit, and $9,000,000 \mathrm{lb} /$ month for maximum $\mathrm{CO}_{2}$ emissions. The red boxes in Table 15 indicate that the demand constraint is met, the numbers in green indicate that the minimum profit is met, and the purple numbers indicate that the maximum $\mathrm{CO}_{2}$ emissions constraint is met.
![img-58.jpeg](img-58.jpeg)

Figure 59. Transmission Pipeline Components

Table 15. Optimal Operating Parameters for Phase 1 Transmission Pipelines


The 3 case scenarios that meet all of the constraints are:

- Scenario 1: Case 2 for Phase 1a ( $\mathrm{P}=30$ bar, $\mathrm{V}=30 \mathrm{~m} / \mathrm{s}$ ) and Case 2 for Phase $1 \mathrm{~b}(\mathrm{P}=30$ bar, $\mathrm{V}=30 \mathrm{~m} / \mathrm{s})$.
- Scenario 2: Case 2 for Phase 1a ( $\mathrm{P}=30$ bar, $\mathrm{V}=30 \mathrm{~m} / \mathrm{s}$ ) and Case 4 for Phase $1 \mathrm{~b}(\mathrm{P}=75$ bar, $\mathrm{V}=30 \mathrm{~m} / \mathrm{s})$.
- Scenario 3: Case 4 for Phase 1a ( $\mathrm{P}=75$ bar, $\mathrm{V}=30 \mathrm{~m} / \mathrm{s}$ ) and Case 2 for Phase $1 \mathrm{~b}(\mathrm{P}=30$ bar, $\mathrm{V}=30 \mathrm{~m} / \mathrm{s})$.

Scenario 1 is selected as the optimal scenario because of the higher profit and lower $\mathrm{CO}_{2}$ emissions compared to the 2 other scenarios. For this scenario, the operating parameters for the 2 parallels transmission lines should be adjusted to a pressure of 30 bar and flow velocity of $30 \mathrm{~m} / \mathrm{s}$ for optimal pipeline safety, economic profit, and $\mathrm{CO}_{2}$ emission amounts.

# CHAPTER 9 

## 9. Conclusions and Future Work

A Prognosis and Health Monitoring (PHM) approach for pipeline system integrity management embedded in a software platform was proposed. The proposed framework along with the software design was supported by a multi-disciplinary science and engineering approach for a comprehensive, state-of-the-art solution. It integrated the data, methods, and technologies into a dynamic pipeline health monitoring system supported by multiple probabilistic predictive models that analyzed all causal factors that could fail the pipeline. Moreover, it provided dynamic mitigation suggestions such as optimal sensor placement and optimal timings of an inspection or repair of a given pipeline for a better structural health monitoring of the pipeline. The proposed PHM approach, which was embedded in the software platform, showed the ability to quantify the health state of the pipeline over time and help the operators make risk-informed decisions on sensor placement and maintenance schedule via the case study of a corroded gas transmission pipeline. In few words, this dissertation presented a dynamic, comprehensive, proactive, and cost-effective PHM framework embedded in a user-friendly software platform to enhance pipeline safety and system integrity management by preventing or reducing the likelihood of failures through optimal mitigation actions. The software could be deployed in a control room as a dynamic health monitoring dashboard or in a mobile version for field inspection and maintenance purposes.

The contributions of the presented research work include: (i) components/system performance degradation and their interactions modeling, (ii) cost-effective sensor placement to better detect damages, (iii) cost-effective maintenance scheduling to avoid/reduce failures, and (iv) optimized operating parameters to increase profit, reduce degradations, and reduce $\mathrm{CO}_{2}$ emissions.

By applying the proposed PHM modeling framework to the Kern River natural gas transmission pipeline as case study, the optimized mitigation actions successfully prevented any failures from happening within the simulation time step. The sensor placement optimization increased the probability of damage detection by $34 \%$ when compared to a layout of fixed sensor intervals, the maintenance schedule optimization reduced the average monthly maintenance costs by $75 \%$ compared to the best selected periodic maintenance policies from the literature, and the operating parameters optimization increased the average monthly profit by $3.67 \%$.

The use of the methodology described in this dissertation is expected to improve safety by having a more accurate health status of the pipeline infrastructure over time and by increasing the lifetime of the system with the proposed dynamic, cost-effective, and risk-informed mitigation suggestions to the operators. Finally, the application of the models and decision-support will, in return, directly benefit the industry, through access to a cost-optimized pipeline integrity management, based on scientific and engineering foundations.

Future work includes the modeling of a prognosis and health monitoring framework for oil pipeline system integrity management as the presented work in this dissertation is specific to natural gas pipelines. By studying the failure causes of oil pipelines and understanding the required/optimized mitigation actions needed, a more comprehensive PHM methodology will help the oil and gas industry improve the system safety and structural integrity. Finally, future work includes also the validation of the PHM methodology by field data and preforming the analysis on pipelines that failed and pipelines that didn't fail and compare the results.

# Appendix A 

## Discretized Nodes of the DBN Internal Corrosion Model





# Appendix B 

## Discretized Nodes of the DBN External Corrosion Model



