# Article 

## A Hybrid Probabilistic Risk Analytical Approach to Ship Pilotage Risk Resonance with FRAM

Yunlong Guo ${ }^{1,2}$, Shenping $\mathrm{Hu}^{1, * *}$, Yongxing Jin ${ }^{1}$, Yongtao $\mathrm{Xi}^{1 *}$ and Wei $\mathrm{Li}^{1,2}$

## check for updates

Citation: Guo, Y.; Hu, S.; Jin, Y.; Xi, Y.; Li, W. A Hybrid Probabilistic Risk Analytical Approach to Ship Pilotage Risk Resonance with FRAM. J. Mar. Sci. Eng. 2023, 11, 1705. https:// doi.org/10.3390/jmse11091705

Academic Editors: Osiris Valdez Banda, Mengxia Li, Pengfei Chen and Lei Du

Received: 8 August 2023
Revised: 27 August 2023
Accepted: 28 August 2023
Published: 29 August 2023

## 0

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Merchant Marine College, Shanghai Maritime University, Shanghai 201306, China; ylguo@jssc.edu.cn (Y.G.); yxjin@shmtu.edu.cn (Y.J.); xiyt@shmtu.edu.cn (Y.X.); weili@jssc.edu.cn (W.L.)
2 School of Nautical Technology, Jiangsu Shipping College, Nantong 226010, China

* Correspondence: sphu@shmtu.edu.cn

Abstract: Collision risk in ship pilotage process has complex characteristics that are dynamic, uncertain, and emergent. To reveal collision risk resonance during ship pilotage process, a hybrid probabilistic risk analysis approach is proposed, which integrates the Functional Resonance Analysis Method (FRAM), Dempster-Shafer (D-S) evidence theory, and Monte Carlo (MC) simulation. First, FRAM is used to qualitatively describe the coupling relationship and operation mechanism among the functions of the pilotage operation system. Then, the D-S evidence theory is used to determine the probability distribution of the function output in the specified pilotage scenario after quantitatively expressing the function variability, coupling effect, and the influence of operation conditions through rating scales. Finally, MC simulation is used to calculate the aggregated coupling variability between functions, and the critical couplings and risk resonance paths under different scenarios are identified by setting the threshold and confidence level. The results show that ship collision risk transmission is caused by function resonance in the pilotage system, and the function resonance paths vary with pilotage scenarios. The critical coupling 'F2-F7(I)' emerges as a consistent factor in both scenarios, emphasizing the significance of maintaining a proper lookout. The hybrid probabilistic risk analytical approach to ship pilotage risk resonance with FRAM can be a useful method for analysing the causative mechanism of ship operational risk.

Keywords: ship pilotage; risk resonance; Functional Resonance Analysis Method (FRAM); Monte Carlo; Dempster-Shafer (D-S) evidence theory

## 1. Introduction

Ship transportation is the primary mode of transportation for bulk goods and accounts for more than $80 \%$ of the freight volume in international trade [1]. To safeguard national sovereignty, ensure the navigational safety of port ships, and prevent water pollution, most countries have implemented compulsory pilotage for foreign ships arriving at ports. However, ships still face significant risks of collision, grounding, contact damage, and other accidents during pilotage owing to limited channel conditions, complex navigation environments, and dense ship traffic in pilotage waters despite the escorting of skilled professionals (i.e., pilots) who are familiar with the environment [2]. In addition, because of the restricted waters in ports and fragile environments, they are more likely to cause significant damage to human life, property loss, and pollution [3]. According to a report published by the International Group of P\&I Clubs (IG), collisions account for more than half of pilot-related accidents [4]. Although there is a higher risk of collision during ship pilotage, it has not received sufficient attention compared to ship accident risk at sea.

As a typical maritime risk, ship collision risk is primarily studied in terms of risk identification, risk assessment, and risk control under the Formal Safety Assessment (FSA) framework advocated by the International Maritime Organization [5]. Risk identification, as the basis of risk assessment and control, aims to reveal the potential causes and mechanisms of accident risks. The key to identifying maritime risks is determining the system's

risk influencing factors (RIFs), which is generally achieved through historical data analysis or expert judgment [6]. The composition and influencing mechanisms of RIFs are constantly changing owing to developments in shipping technology and safety management. The latest investigation on ship accidents shows that more than $80 \%$ of them are related to human and organisational factors [7]. Therefore, they have been widely studied [8]. The Human Factor Analysis and Classification System is a comprehensive human error analysis method based on the Reason model and is currently one of the most widely used human factor identification and modelling methods [9]. The Cognitive Reliability Error Analysis Method, a second-generation reliability analysis method, is combined with other quantitative analysis methods to conduct quantitative research on human error probability [10]. Wu et al. [11] reviewed the research methods and technologies of human and organisational factors in a maritime risk analysis and revealed that the development of maritime autonomous surface ships (MASS) has brought new changes and challenges to maritime risk analysis. MASS significantly contributes to reducing the impact of human factors on ship safety through intelligent technology [12], although it may introduce new risks, such as cyberattacks [13]. The developments of advanced technology, management modes, and the perspectives of research problems all changed the composition and formation mechanisms of RIFs. Moreover, because RIFs are dynamic and coupled during pilotage operations, it is necessary to identify risks based on their characteristics.

Ship pilotage operation risk refers to the risk caused by the dynamic characteristics and coupling effects of system RIFs during the ship pilotage process. The focus of maritime risk has gradually changed from regional macro risk to single-ship operational process risk. Therefore, studying ship operational risks under different scenarios has become an important issue [14]. The identification and analysis of RIFs should not only consider specific scenario factors, such as the operating environment, ship characteristics, and human factors, but also the dynamic variability of RIFs. Fan et al. [8] determined the RIFs of the four operational stages of MASS from the perspectives of humans, ships, technology, and the environment to comprehensively analyse the risks during MASS navigation. Chang et al. [12] identified the significant operational risks of MASS using failure mode and effects analysis. Gil et al. [15] obtained the RIFs of the bow crossing distance encountered by different ships under different sailing scenarios based on 10 years of automatic identification system data learning. In addition, with the development of Arctic shipping routes, safety issues during the navigation of ships in Arctic waters have also become a concern. Considering the influence of special environmental factors such as floating ice and low temperatures during navigation, scholars have identified and studied ship accident risks such as ship besetting [16], ship-ice collision [17], ship-ship collision [9], and grounding [18] in Arctic waters. Yu et al. [14] considered dynamic geometric risk factors related to local traffic factors, in addition to static factors such as ship characteristics, to quantitatively analyse the overall risk of a ship during its voyage. Yu et al. [19] identified the RIFs of navigation and the natural environment from the perspective of geometric risk and used a Bayesian network to assess the collision risk of ships and offshore facilities in real scenarios.

With the development of the technology and safety theory, the accident causation theory has undergone different developmental stages [6]. Traditional theoretical models, such as the domino, epidemiological, and Swiss cheese models, imply a linear thinking mode of system structure decomposition and causality [20], making it difficult to explain the dynamic characteristics of complex system factors and the coupling relationships between factors. According to the dynamic adaptability, evolution, and nonlinearity of a complex system, the coupling between RIFs and the emergence of the system should be fully considered to reveal the causes of risk. System analysis methods, such as Accident Map, Systematic Theoretical Accident Model and Process, and Functional Resonance Analysis Method (FRAM), developed in recent years have been widely used in railway transportation, aviation, maritime, and safety management in other fields and are suitable for a risk analysis of complex socio-technical systems [21]. FRAM analyses the RIFs of dy-

namic systems from the perspective of functional characteristics [22]. As a system analysis method, FRAM has been continuously studied since its creation in 2004 [23] and has been widely used in the risk analysis of complex socio-technical systems in different fields [24], including maritime risk. Patriarca et al. [25] systematically reviewed the state-of-the-art FRAM in terms of methodology, application fields, and potential future research directions. As a typical socio-technical system, FRAM can help identify scenario-based RIFs and their complex coupling relationships during ship operations. Salihoglu and Besæiki [22] used FRAM to conduct a qualitative analysis of the Prestige oil spill accident, effectively identifying the key functions and internal influencing factors of the accident and demonstrating the outstanding advantages of FRAM in a marine accident analysis. The function variability and coupling between functions were examined through the identification and description of the main functions of fishery inspection, and a safe operation path under functional aggregation was explored to improve the safety of artisanal fisheries [26]. However, as a qualitative analysis method, FRAM was inadequate for providing quantitative risk analysis results.

FRAM can be improved by integrating it with other methods to realise a quantitative or semi-quantitative study of system risk. Patriarca et al. [27] proposed a semi-quantitative FRAM analysis framework based on Monte Carlo (MC) simulations and considered the influence of different operating conditions on the safety assessment of air traffic management systems. Kaya et al. [28] combined FRAM with MC simulation and the critical matrix method to model a tram operation system and identified the critical coupling and system risk through semi-quantitative evaluation. Yu et al. [29] developed a data-driven approach that uses high confidence intervals of association rules to quantify functional coupling and identify the causative paths of potentially hazardous scenarios by merging association rules. Consequently, by integrating qualitative analysis of complex system functional mechanisms with complementary quantitative methods [30], FRAM facilitates quantifying functional variability and uncovering the mechanism of risk transmission through analysis of adverse functional resonance.

The remainder of this paper is organised as follows. In Section 2, a probability-based risk resonance analysis framework for ship pilotage operations is proposed by combining the D-S evidence theory and MC simulation with a quantitative improvement of the traditional FRAM, and the scenario and data of studied case are described. In Section 3, the proposed methodology is applied and verified by conducting a resonance analysis of the collision risk during the pilotage operation process of a container ship in Shanghai Port waters. In Section 4, we discuss the proposed method and its application results. Finally, Section 5 concludes the study.

# 2. Methodology 

### 2.1. Problem Description and Framework

### 2.1.1. Problem Description of Ship Pilotage Risk Resonance

In the ship pilotage process, various system functions, such as human, technological, and organisational, are variable and coupled with each other according to the operation scenario to jointly complete various operation tasks. In the routine ship pilotage process, the adverse output of related functions, such as personnel negligence, operational errors, and equipment failures, may cause close-quarters situations and even ship accidents. Ship collisions are among the most common types of accidents during ship pilotage processes.

During the ship pilotage process, various system functions interact with each other through coupling. In daily operations, the output variability of upstream functions may have amplifying, damping, or no impact on the output variability of downstream functions, depending on the way of coupling between functions and the characteristics of functions. Adverse variability in functions, such as human operational errors or equipment malfunctions, do not directly lead to accidents, but rather generate functional resonance through coupling between functions. Resonance paths are formed between different functions resonance at the same time, leading to the occurrence of ship pilotage accidents. For ship

collision avoidance operations, various operational errors when there is a collision risk is transmitted through functional resonance, ultimately leading to a collision due to the close distance between ships. Therefore, quantitative analysis of the variability and coupling effects between the functions of the ship pilotage system helps to reveal the accident cause mechanism under risk resonance.

# 2.1.2. A Hybrid Probabilistic Risk Analytical Approach 

FRAM model, D-S evidence theory, and MC simulation were collectively used to quantitatively simulate the dynamic characteristics of functional variability and the coupling criticality between functions under different pilotage operation scenarios so as to identify the risk transmission path caused by functional resonance. First, FRAM modeling was used to identify the system functions for collision avoidance task during ship pilotage process, and the potential risk transmission paths in the pilotage system were qualitatively described from the perspective of function coupling. Then, the rating scale and probability distribution were used to quantify the dynamic uncertainty of resonance effects between functions, and the D-S evidence theory was introduced to fuse the evaluation results of probability distributions by different experts. Finally, by using MC multiple cyclic sampling simulation, the variability priority number (VPN) distribution between different functions coupling under specific pilotage scenarios can be obtained. By setting thresholds and confidence levels, critical functional couplings may be identified, and the functional resonance path composed of them can be further analysed. The research framework is shown in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. Research framework of ship pilotage risk resonance analysis.
Step 1: Construction of FRAM model. According to the 'goal-action' analysis, the task was decomposed into sub-tasks by the hierarchical task analysis method (HTA). Each sub-task was formalized according to its goal and the actions necessary to achieve it, the action acted as a sub-task of its upper level sub-task, that is, a meta-task. The relationship between a sub-task and its upper task depended on the operation plan, procedure, or timing. For the overall task of ship pilotage safety, HTA was used to divide it into two levels of sub-tasks in this paper, the implementation sequence of main sub-tasks was

defined at the higher level, and each sub-task at the lower level was to be a group of actions (meta-tasks) [31]. The sub-tasks and meta-tasks were identified as system functions, and the function characteristics were described and analysed based on six aspects: input (I), output (O), precondition (P), control (C), resources (R), and time (T). The FRAM model was constructed to qualitatively analyse the operating mechanism of the pilotage system by combining functional hierarchy and logical association.

Step 2: Quantification of function variability and coupling. First, functional variability in the FRAM model was characterised by the timing and precision of the functional output, and the degree of output variability and coupling effect was expressed by setting relevant rating scales. The aggregated coupling between functions was then defined using the upstream function output variability, upstream-downstream function coupling effect, and operation condition effects. A discrete probability distribution was used to quantify functional dynamic characteristics in terms of timing and precision. The acquisition of the discrete probability distribution mainly relied on domain experts to evaluate based on the historical statistical data of piloted waters and relevant research results. The D-S evidence theory was used to fuse the evaluation results.

Step 3: Acquisition of the ship pilotage scenario data and MC simulations. Based on quantifying the function output variability and upstream-downstream function amplification factors by setting rating scales, the discrete probability distribution and operation condition effect of functions were obtained by considering specific pilotage operation scenario data. According to the quantitative expression of aggregated coupling, an MC multiloop simulation was used to obtain the coupling criticality distribution between the functions in the FRAM model.

Step 4: Function resonance path identification and risk transmission analysis. According to the distribution of the aggregated coupling values between system functions in a specific pilotage operation scenario obtained by MC simulation, the critical couplings in the pilotage operation process could be determined by setting the threshold and confidence level to identify the function resonance path in the ship pilotage system and then analysing the risk transmission process.

# 2.2. Modelling 

### 2.2.1. FRAM in Ship Pilotage Risk Resonance

Considering the dynamic and nonlinear coupling characteristics of a ship pilotage system, FRAM revealed the causative mechanism of risk transmission from the perspectives of normal system operation and functional resonance [25]. FRAM is based on four basic principles: the equivalence principles of success and failure, approximate adjustment principle, emergence principle, and functional resonance principle. Generally, functions are identified according to the task decomposition or operation step division of the system. The system functions are divided into three types: technological, human, and organisational, and they are described from six aspects: I, O, T, R, P, and C [32]. The variability of the function output is determined by time and precision, and the aggregation of its variability is determined by examining the output variability of the upstream function, the variable influence of the upstream function on the downstream function, and the influence of the operation conditions [33]. FRAM analysis is used to identify the functional resonance effect and risk transmission during ship pilotage operations through qualitative analysis.

### 2.2.2. Quantitative Analysis Method of Aggregated Coupling

After a qualitative description of the operation mechanism of the ship pilotage system through FRAM modelling, the output variability of the upstream functions, coupling effects of the upstream and downstream functions, and scenario operational conditions were considered. The VPN was used to characterise the criticality of the aggregated coupling between functions. According to the data of a specific pilotage operation scenario, MC simulation was used to calculate the VPN distribution of the coupling between various functions to determine the critical coupling and coupling resonance path between functions.

Accordingly, the risk transmission mechanism during the ship pilotage operation process was analysed [27].

# Quantification of Function Output Variability 

Generally, the variability of function output is characterised based on the two aspects of timing and precision. In terms of timing, the function output is represented as 'Too early', 'Too late', 'On time', and 'Not at all', and in terms of precision, it is represented as 'Precise', 'Acceptable', 'Imprecise', and 'Wrong'. A rating scale may be developed to express the degree of function variability corresponding to different states: the larger the value, the greater the variation in the functional output. Variability of function output in specific pilotage scenarios is dynamically uncertain, a discrete probability distribution may be used to quantify functional dynamic characteristics in terms of timing and precision. Consider an upstream function whose output variability is as shown in Equation (1):

$$
O V_{j}=V_{j}^{T} V_{j}^{P}
$$

where $V_{j}^{T}$ represents the rating value of the upstream function output in terms of timing and $V_{j}^{P}$ represents the rating value of the upstream function output in terms of precision.

## Quantification of Coupling Effects between Functions

The upstream function generated a coupling effect by connecting one of the five aspects (I, P, T, P, or R) of the downstream function. Coupling different types of functions produced different effects, such as amplification, damping, or no influence on the variability of the downstream functions. Based on a qualitative analysis of the coupling effects between the functions, a rating scale was developed to quantitatively evaluate the coupling effects between the upstream and downstream functions. According to the output variability of the upstream function and the corresponding amplification factor, the coupling effect of the upstream function $j$ on the downstream function $i$ was determined, as shown in Equation (2):

$$
C V_{i j}=O V_{j} \cdot a_{i j}^{T} \cdot a_{i j}^{P}
$$

where $a_{i j}^{T}$ represents the amplification factor of the coupling effect between the upstream function $j$ and downstream function $i$ in terms of timing, and $a_{i j}^{P}$ represents the amplification factor of the coupling effect between the upstream function $j$ and downstream function $i$ in terms of precision, which satisfies the requirements of Equation (3).
$a_{i j}^{T}\left(a_{i j}^{P}\right)\left\{\begin{array}{l}>1 \text { upstream output has an amplifying effect on the downstream function } \\ =1 \text { upstream output has no effect on the downstream function } \\ <1 \text { upstream output has a damping effect on the downstream function }\end{array}\right.$
Quantification the Influence of Operation Scenario
When determining the aggregated coupling effect between functions in a specific ship pilotage process, it was necessary to consider not only the function output variability and the coupling effect of the upstream to downstream functions, but also the influence of the operating conditions of the specific pilotage scenario. For example, the hydrometeorological environment, traffic conditions, supervision and management level, and different combinations of these operation conditions constituted different pilotage operation scenarios. The operating conditions in the scenario were defined through the analysis of specific ship pilotage scenarios, and their performance was defined as scenario performance conditions (SPC), that is, $S P C^{k}, k=1, \cdots, m$. Each $S P C^{k}$ had different effects on different functions.

The effects of $S P C^{k}$ on the function $j$ in a specific pilotage scenario are expressed as $b_{j}^{k}$, as shown in Equation (4):

$$
b_{j}^{k} \begin{cases}=1 \text { the } S P C^{k} \text { has a high impact on the } j \text { function } \\ <1 \text { the } S P C^{k} \text { has a moderate impact on the } j \text { function } \\ =0 \text { the } S P C^{k} \text { has no impact on the } j \text { function }\end{cases}
$$

As the different $S P C^{k}$ and their performances differed in different pilotage operation scenario $z(z=1, \cdots, Z)$, it was assumed that the performance of $S P C^{k}$ in operation scenario $z$ was $S P C_{z}^{k}$, and the performance of the operation condition $S P C_{z}^{k}$ was represented by setting a rating scale, as shown in Equation (5). Therefore, the comprehensive effect $e_{j}^{z}$ of all operation conditions on function $j$ under the specified pilotage operating scenario $z$ could be expressed as Equation (6). If $e_{j}^{z}=1$, it indicated that the pilotage operation scenario had no amplification effect on $j$ function variability. The value range of $e_{j}^{z}$ is shown in Equation (7):

$$
\begin{gathered}
S P C_{z}^{k} \begin{cases}4 \text { High variability effect of } S P C^{k} \\
2 \text { Low variability effect of } S P C^{k} \\
1 \text { No variability effect of } S P C^{k}\end{cases} \\
e_{j}^{z}=\frac{\sum_{k=1}^{m} S P C_{z}^{k} \cdot b_{j}^{k}}{m} \\
e_{j}^{z}=\max \left\{1 ; \frac{\sum_{k=1}^{m} S P C_{z}^{k} \cdot b_{j}^{k}}{m}\right\}
\end{gathered}
$$

Considering the output variability of upstream functions, the amplification effect between upstream and downstream functions, and the comprehensive effect of operating conditions in the ship pilotage operation scenario $z$, the $V P N$ between functions could be expressed as Equation (8). This could be used to evaluate the criticality of coupling between functions to identify critical functions and function resonance paths, that is, risk transmission paths.

$$
V P N_{i j}^{z}=V_{j}^{T} \cdot V_{j}^{P} \cdot a_{i j}^{T} \cdot a_{i j}^{P} \cdot e_{j}^{z}
$$

# 2.2.3. Monte Carlo Simulation 

MC is a method of calculating the mean value of a function of random variables based on the large number theorem and the central limit theorem, which can be a specific mean value of a multidimensional probability density function defined on multiple random variables. The speed of convergence and the magnitude of the error are independent of the complexity of the problem or the dimension of the phase space. This renders them ideal for complex systems [34]. Based on the function coupling quantification method introduced in Section 2.2.2, this study used the MATLAB platform to calculate the VPN among various functions in different ship pilotage operation scenarios using 1000 iterations of MC simulation to analyse the coupling effect between different functions [27].

### 2.2.4. D-S Evidence Theory

The key step in calculating the VPN value distribution of function coupling in a specific pilotage scenario through MC simulation is to determine the discrete probability distribution of the output $V_{j}^{T}$ and $V_{j}^{P}$ of each function. Subject matter experts (SMEs) evaluated the discrete probability distribution of each function's output variability according to pilotage operation scenario data, professional knowledge, and benchmark. Considering the differences and uncertainties in expert judgment, the D-S evidence theory was adopted

to fuse the evaluation results of different experts [35]. The general implementation steps of the D-S evidence theory are as follows [36].

Step 1: Identification of the recognition framework and evaluation criteria. It was assumed that in a certain functional output $p$, which had four states, the recognition framework was $\Theta=\left\{p_{1}, p_{2}, p_{3}, p_{4}\right\}$. According to the types of functions and the related research literature, the probability distribution benchmark was determined by experts as the reference of evaluation criteria.

Step 2: Evaluation of probability distribution. $m\left(p_{i}\right)$ represented the basic probability distribution function of different states of functional output $p$ evaluated by experts, as shown in Equation (9). Probability distribution assessments were made by SMEs based on their professional judgment reference benchmarks.

$$
m\left(p_{i}\right) \rightarrow[0,1] ; \sum_{p_{i} \in p} m\left(p_{i}\right)=1
$$

Step 3: Fusion of evaluation results. The probability distribution results under multiple pieces of evidence and the prior probability distribution of functional output $p$ under data fusion may be obtained using the evidence synthesis rule to fuse the reliability judgements of different experts. This is shown in Equations (10) and (11).

$$
\begin{gathered}
k=1-\sum_{p_{a} \cap p_{b}=\varnothing} m_{1}\left(p_{a}\right) \cdot m_{2}\left(p_{b}\right) \\
{\left[m_{1} \oplus m_{2}\right]\left(p_{i}\right)=\frac{1}{k} \sum_{p_{a} \cap p_{b}=p_{i}} m_{1}\left(p_{a}\right) \cdot m_{2}\left(p_{b}\right)}
\end{gathered}
$$

where $m_{1}\left(p_{a}\right)$ and $m_{2}\left(p_{b}\right)$ represent the scores of experts $m_{1}$ and $m_{2}$ on the same factor state, respectively, and $k$ represents the conflict in expert's judgment information.

If a total of $n$ experts participate in the survey, the fusion Equation (12) is as follows.

$$
m_{1-n}=m_{1} \oplus m_{2} \oplus \cdots \oplus m_{n}
$$

# 2.3. Scenario and Data 

This study selected Shanghai Port, one of the busiest ports in the world, as the application area. The case study revealed the critical functions and function couplings of the pilotage system under normal and abnormal operation scenarios through FRAM modelling and quantitative methods to analyse the transmission mechanism of ship collision risk based on functional resonance.

### 2.3.1. Scenario

The ship pilotage process of a large container ship (over 5000 TEU) sailing from the D6 buoy at the Yangtze estuary's pilot embarkation point to the D47 buoy near the Waigaoqiao wharf was selected as a case study to apply and validate the established research framework. During the pilotage process, the ship travelled approximately 42 n miles through the Beicao deep-water channel of the Yangtze river estuary, the Yuanyuansha warning area, and the Waigaoqiao channel (Figure 2), which was the common route for large container ships entering and leaving the Waigaoqiao wharf. The pilotage operation task was difficult because of changeable hydrometeorological conditions, high traffic density, complicated ship encounters, and many collision risk factors.

The pilotage process was analysed from the pilot's perspective to achieve the collision avoidance task of a ship during navigation. According to the historical pilotage process analysis of such ships combined with expert suggestions, task decomposition of the pilotage process was conducted using the HTA method (Figure 3). For the ship collision avoidance task, there were mainly five sub-tasks: 'Position the ship', 'Identify the collision risk', 'Take collision avoidance measures', 'Adjust the ship position', and 'Maintain a safe distance', which could be further divided into more meta-tasks. Figure 3 shows the composition and

logical relationships between the sub-tasks and meta-tasks. The sub-tasks and meta-tasks were identified as 16 system functions, and each function was analysed and described from six aspects, such as I, P, C, R, T, and O. The coupling relationship between the upstream and downstream functions was determined based on the HTA analysis results and the logical relationship between the functions.
![img-1.jpeg](img-1.jpeg)

Figure 2. Illustration of ship pilotage process (D6-D47). The scope of the study is the pilotage process of the ship from the D6 buoy to the D47 buoy, with the blue line indicating the ship's route. The red and yellow lines in the channel represent ship tracks, and the darker the color, the higher the density of ship traffic.
![img-2.jpeg](img-2.jpeg)

Figure 3. HTA analysis of ship pilotage process.
The established FRAM model was checked and proofread by SMEs and finally determined after improvement. Considering the transmission research on collision risk during ship pilotage, some functions with strong correlations with collision risk were selected to model the pilotage operation process to determine the critical coupling better and effectively reduce the complexity of the MC simulation calculation. FRAM Model Visualiser software (version 0.4.2) was used to build the FRAM model of the ship pilotage process (Figure 4). The model could further improve the analysis granularity to decompose some functions or increase the description of some functions and the coupling between them.

![img-3.jpeg](img-3.jpeg)

Figure 4. FRAM model of ship pilotage operations. The hexagons indicate the functions of ship pilotage operation system, and the labels on the lines between the functions indicate their coupling content.

Many scenario conditions affect the ship collision risk in the pilotage operation process, including the status of operators, the ship's technical status, the natural environment, and safety management. This study primarily selected four operation conditions, including traffic condition $S P C^{1}$, hydrometeorological condition $S P C^{2}$, pilot status $S P C^{3}$, and ship technical status $S P C^{4}$, by setting the performance of the four operation conditions to compose six pilotage scenarios (Table 1).

Table 1. Setting of operation conditions for ship pilotage scenarios.


# 2.3.2. Data

## Quantification of Variability in Function Output

Referring to the relevant literature [26], a rating scale (Table 2) was used to measure the variability in the timing and precision of the function output. The greater the value in the table, the greater the variability in the functional performance output and the greater the impact on downstream functions. In the ship pilotage operation process, the output variability of each function exhibited a certain randomness in terms of timing and precision. The probability distributions of the output variability for different types of functions differed, whereas the function outputs of similar systems in the same field were similar. Therefore, with reference to the relevant research results in the field of ship transportation [37] and historical data, the general discrete probability distribution table (Table 3) for different types of functional outputs (technical, human or organisational) was determined as the

Table 2. Variability rating in timing and precision.


Table 3. Benchmark for the probability distribution of the function output.


Quantification of Aggregated Coupling
To determine the output variability of each function and its probability distributions in the ship pilotage process, it was necessary to comprehensively consider the output variability of the upstream function, the upstream amplification effect on the downstream function, and the influence of the operation scenarios to quantify the aggregated coupling effect between system functions, and determine the critical function coupling through MC simulation analysis. The transmission of collision risk was analysed using functional resonance path identification after analysing the form in which the system function variability came together and led to an undesirable result.

First, the value range of $a_{i j}^{f}$ and $a_{i j}^{T}$ of the amplification effect for the upstream function on the downstream function was $[2,1,0.5]$ in reference to the relevant literature [28], indicating that the upstream function output variability had an amplification effect, no effect, and damping effect on the downstream function, respectively. The specific values of $a_{i j}^{f}$ and $a_{i j}^{T}$ depended on the output results of the upstream function and the coupling mode of the upstream and downstream functions. As the output of the upstream function had a probability distribution, the state with the highest probability was considered as the output result for judgment. Second, the effects of the operation conditions in specific pilotage scenarios were quantified. With reference to the relevant literature [28], the value range of $b_{j}^{k}$ for the effects of pilotage conditions $S P C^{k}$ on the output of function $j$ was set as $[1,0.5,0]$, indicating that operation conditions $S P C^{k}$ had a high impact, moderate impact, and no impact on the output variability of function $j$, respectively.

The value range of $S P C^{k}$ for the four pilotage operation conditions was set as $[1,2,4]$, indicating that the operation conditions $S P C^{k}$ had no variability effect, a low variability effect, and a high variability effect in the specific pilotage operation scenario, respectively. The higher the variability effect of the operation conditions, the greater the effect on the relevant functions. In addition, the extent of the effects of the four operation conditions on different system functions was analysed individually using performance analysis of each

operation condition, and the value $b_{j}^{k}$ of different operation conditions on each function was determined (Table 4).

Table 4. The influence of four operation conditions.


# 3. Results 

### 3.1. Quantification of Function Coupling of Ship Pilotage System

The quantitative analysis method introduced in Section 2.2 was used to calculate the variability of various functions and coupling effects in the FRAM model to identify the critical functions and critical coupling under different pilotage operation scenarios based on a qualitative analysis of the collision avoidance operation in the ship pilotage process. Accordingly, the resonance path and transmission mechanism of the ship collision risk in a ship pilotage operation system were analysed.

Six pilotage scenarios (Table 1) were established by assuming the states of the four operation conditions to conduct risk transmission research during the ship pilotage process. First, the SMEs in Table 5 were invited to evaluate the probability distribution of the output variability of each function in the six pilotage scenarios by referring to the benchmark in Table 3. Subsequently, the D-S evidence theory was adopted to fuse the evaluation results of the five SMEs to obtain the corresponding function output probability distribution. Finally, the value distribution of $V P N_{i j}^{c}$ of the coupling between the functions in the six pilotage operation scenarios was obtained using the MC simulation.

The probability distribution of the output 'Encounter situation' of function <Maintain a proper lookout> (F2) in terms of timing was taken as an example to illustrate the application flow of D-S evidence theory in obtaining the probability distribution of function output. First, the output 'Encounter situation' of F2 was divided into 'On time' $\left(\mathrm{p}_{1}\right)$, 'Too early' $\left(\mathrm{p}_{2}\right)$, 'Too late' $\left(\mathrm{p}_{3}\right)$, and 'Not at all' $\left(\mathrm{p}_{4}\right)$. Then, as F2 is a human function, the probability distribution benchmark of its output variability in terms of timing was determined as $\{0.60,0.15,0.20,0.05\}$ according to Table 3. By combining pilotage scenario data and their professional knowledge, five SMEs in Table 5 evaluated the output probability distribution in terms of timing by referring to the benchmark, the results were shown in Table 6. The differences in the evaluation results reflected the diversity in expert experience and cognition. Finally, the coefficient K calculated according to Equation (10) was $3.85 \times 10^{-3}$, and the probability distribution after evidence fusion calculated according to Equations (11) and (12) was shown in the last column of Table 6. The probability distribution of each upstream function output in the FRAM model in terms of timing and precision can be obtained by evaluating and calculating through the method in turn.

Table 5. Details of the panel of SMEs.


Table 6. States probability distribution of 'Encounter situation' in terms of timing.


According to the relevant data of the coupling between the function $<$ Maintain a proper lookout> and <Ship scenario awareness> in row 1 of Table 7, MC simulation obtained the distribution of values of $V P N_{i j}^{*}$ for coupling 'F2-F3(l)' in operation scenarios 1 and 6, as shown in Figure 5.

Table 7. Examples of function coupling values.


![img-4.jpeg](img-4.jpeg)

Figure 5. MC simulation example of VPN distribution (scenario 1,6). The horizontal coordinate indicates the VPN value of the coupling between the function $<$ Maintain a proper lookout $>$ and $<$ Ship scenario awareness $>$. The vertical coordinate indicates the proportion of the value (display in logarithmic form). Where blue histogram indicates scenarios 1 and yellow histogram indicates scenarios 6 .

# 3.2. Risk Resonance Analysis in Ship Pilotage Process 

### 3.2.1. Determination of Threshold and Identification of Critical Coupling

MC simulation was used to obtain the $V P N_{i j}^{z}$ value distribution of the coupling between various functions in different pilotage scenarios by quantifying the corresponding parameters under different operation conditions of the six pilotage scenarios. To determine the critical coupling between the system functions, it was necessary to determine the threshold. The threshold of $V P N_{i j}^{z}$ was calculated by setting a critical situation, i.e., the output of the upstream function was 'Too late' in terms of timing, 'Acceptable' in terms of precision, and the upstream function had an amplification effect on the downstream function. In this case, the value $V P N_{i j}^{z}$ calculation that did not consider the influence of the operation conditions was the minimum threshold $V P N^{*}=24$ (i.e., $V_{j}^{T}=3, V_{j}^{P}=2, a_{i j}^{T}=2$, $a_{i j}^{P}=2, e_{j}^{z}=1$ ). The confidence level of $V P N_{i j}^{z}$ value below the threshold in 1000 iterations of the MC simulation was set to $95 \%$. Therefore, when the MC simulation result of the $V P N_{i j}^{z}$ value of a certain function coupling satisfied $P\left(V P N_{i j}^{z}>V P N^{*}\right)>0.05$, the coupling was considered critical.

After analysing the pilotage process of container ship in six operational scenarios in the studied Shanghai Port waterway, the probability distributions of $V_{j}^{T}$ and $V_{j}^{P}$ of each function in the FRAM model were determined, as along with the corresponding $a_{i j}^{T}$ and $a_{i j}^{P}$ values. Then, the $e_{j}^{z}$ values of the six pilotage operation scenarios were analysed and calculated, and the $V P N_{i j}^{z}$ distributions of different functional couplings in the six operation scenarios were obtained through MC simulation. According to the threshold $V P N^{*}$ and critical coupling criteria specified above, the cumulative probability $P\left(V P N_{i j}^{z}>V P N^{*}\right)$ of each functional coupling exceeding the threshold was statistically calculated. The results are shown in Figure 6, where the critical coupling and function resonance paths under different operation scenarios can be determined, and the collision risk transmission mechanism during ship pilotage operation process can be analysed accordingly.

![img-5.jpeg](img-5.jpeg)

Figure 6. Coupling simulation results under six pilotage scenarios. The values of the blue area indicate the probability that the VPN of functional coupling exceed the threshold. The larger the value, the more critical the coupling is. The probability value of coupling greater than 0.05 is identified as the critical coupling.

# 3.2.2. Analysis of Collision Risk Resonance during Ship Pilotage Process 

The simulation results of ship pilotage operation scenarios 1 and 6 were selected, and their critical couplings were drawn in the FRAM model (red lines in Figures 7 and 8).
![img-6.jpeg](img-6.jpeg)

Figure 7. Ship collision risk resonance paths in scenario 1. These hexagons, e.g., F1, F2, indicate functions in the ship pilotage operation system. The red lines indicate the critical couplings between functions, the blue lines indicate general couplings.

![img-7.jpeg](img-7.jpeg)

Figure 8. Ship collision risk resonance paths in scenario 6. These hexagons, e.g., F1, F2, indicate functions in the ship pilotage operation system. The red lines indicate the critical couplings between functions, the blue lines indicate general couplings.

A comparative analysis could reveal their interaction, the generation of a resonance path for risk transmission, and the causative mechanism of collision risk during ship pilotage operations. The main conclusions are as follows:

1. There are seven critical couplings of the pilotage operation system in scenario 1 (Figure 7) that are relatively dispersed, indicating that the adverse output of some functions may be damped and weakened in the downstream functions. The probability of a collision accident risk arising from the system function resonance was low. In operation scenario 6, new critical couplings emerged in the pilotage system as the variability of traffic conditions, and pilot status increased. Hence, the number of critical couplings increased to twelve in Figure 8, and a relatively continuous function resonance path appeared, such as 'F2-F7(I)-F8(I)-F9(I)-F10(I)'. In the pilotage operation scenario 6 , the adverse output of the system functions was more likely to be transmitted through the function resonance path, causing system function resonance effects and increasing the risk of accidents.
2. The comparative assessment between scenarios 1 and 6 further demonstrated the role of operation conditions in shaping system risks. The critical coupling 'F2-F7(I)' emerged as a consistent factor in both scenarios, emphasizing the significance of maintaining a proper lookout. In scenario 6, where complexities in traffic conditions prevailed, lookout negligence ('F2-F3(I)') became a critical coupling, showcasing the direct impact of operational challenges on risk factors. Moreover, the deterioration of the pilot status further reduced the ability to identify collision risk. Therefore, pilot and crews needed to strengthen their cooperation, fair usage of navigational instruments, and maintain a proper lookout during the entire pilotage process to identify collision risks in time [38].
3. Furthermore, the study identified the necessity of combining 'changing speed' and 'changing course' methods during ship pilotage in narrow waters, as evidenced by the emergence of a new critical coupling ('F13-F12(I)') in scenario 6. This result underscored the alignment between MC simulation outcomes and real-world operational conditions, bolstering the method's effectiveness. In conclusion, the study's comparative analysis of different scenarios showcased the interplay between operational conditions and system risks, affirming the efficacy of the proposed quantitative FRAM

approach. The findings provided valuable insights into collision risk management during ship pilotage operations and laid the groundwork for future studies focused on addressing real-world complexities and temporal risk evaluation.
4. Critical coupling and function resonance paths were identified through a quantitative analysis of the coupling effects for different functions under different operation scenarios to analyse the transmission mechanism of system risks. This method indicated the causative mechanism of system risk from the perspective of the system operation mechanism, emphasising that strong coupling between system functions was the main reason for risk transmission and accidents. The coupling between system functions indicated the amplifying effect of risk transmission and the damping effect. Therefore, the focus of risk management differed from the previous concern about failure factors. However, this was to select appropriate monitoring indicators for the critical coupling and functions of the system, restrain the adverse output of the functions, and improve the ability of functions to address variability. Alternatively, introducing new system functions to manage critical functions could block a function's resonance path.
5. The operation conditions of a real ship pilotage process changed constantly as the ship moved. The ship pilotage system could be represented as a state vector that changed with time, and the state space of the system was determined by the function output and the coupling effect of the functions. Thus, the variability of the function output and the system risk in the ship pilotage process represented a temporal state transition.

# 4. Discussion 

### 4.1. Analysis of Risk Resonance in Ship Pilotage Process

Traditional risk identification methods advocate analysing the causes of accidents based on system decomposition and secondary causality, often ignoring the coupling correlation and dynamic characteristics of system factors. However, as a typical complex socio-technical system, the ship pilotage operation risk is nonlinear, uncertain, time-varying, and emerging. The FRAM system analysis method is introduced and based on qualitative functional modelling and a description of the ship pilotage process, with the quantitative representation of functional variability coupling and MC simulation; the resonance path is identified to reveal the causative mechanism of pilotage risk transmission under functional resonance. The case study proves that this method can effectively identify the functional resonance path under different pilotage operation scenarios. A comparative analysis of the identification results of different operation scenarios can reveal the effects of operation conditions on system risk and the transmission path, providing a theoretical basis for accurately controlling pilotage risk under different operation scenarios.

### 4.2. Analysis of FRAM Quantisation

FRAM is an excellent method for complex system risk causation analysis. However, owing to its qualitative characteristics, it faces problems of heavy workload and considerable uncertainty when analysing the system risk of multiple scenarios. In this study, the system function resonance path and risk transmission in different pilotage operation scenarios were analysed by integrating MC simulation and D-S evidence theory, enriching the quantitative analysis of complex system risk using FRAM and enhancing the ability and effectiveness of FRAM for operational risk analysis. The combination with other quantitative methods should be studied further for the quantitative analysis of FRAM. Therefore, to determine the parameters and obtain the probability distribution of the function output, the fuzzy set theory [37] and N-K theory [39] can be used to deal with the uncertainty of various subjective and objective data.

### 4.3. Human Factors in Ship Collision Risk

Collision avoidance is a critical task in ship pilotage process. The pilot, as the decisionmaker, needs to constantly lookout to find the collision risk, make proper response decisions

according to his professional judgment, and issue orders to the crews to finish the collision avoidance operation to ensure the pilotage safety. Therefore, the human factors, such as the pilot's experience, level, and physical condition, have influence on the identification and judgment of collision risk. In addition, the crew's cooperation ability will also affect the implementation effect of collision avoidance measures. FRAM modeling was used to explain the influence of human factors on function operation from multiple dimensions, such as input, time, resource, precondition, and control, and qualitatively represent the transmission effect of human factors among system functions through the coupling effect between them.

In addition, in the process of quantifying the FRAM model, the influence of human factors was also fully considered. First, the influence of different states of pilot status $\left(S P C^{5}\right)$ on functional variability and coupling effects was fully considered in the setting of six simulated pilotage scenarios. Then, the quantitative process of functional variability and coupling effect also considered the influence of human factors. In particular, experts were required to evaluate the probability distribution of functional variability after analysing the influence of human factors, such as pilot and crews in specific pilotage scenarios. However, this method is based on the assumed states when considering the influence of human factors, which is difficult to characterise the personalized and dynamic characteristics of human factors in a single ship pilotage process. Therefore, in the future, it is necessary to adopt a stochastic process-based modeling method to address the human factor's state transition characteristics in ship pilotage process and deduce the operational risk evolution characteristics under the dynamic multi-factors coupling.

# 4.4. The Uncertainty and Limitation Analysis of This Method 

Integrating FRAM with MC simulation can reveal the coupling resonance between system functions under different pilotage operation scenarios, analyse the transmission of operational risks through resonance path identification, and effectively address the quantitative analysis of scenario risks. This is an excellent system risk analysis method. However, there are still some uncertainties and limitations [40].

First, establishing the FRAM model and obtaining the probability distribution of the functional output rely mainly on domain-expert knowledge. Although this study invited several experts from different institutions to participate in the evaluation and adopted the D-S evidence theory to reduce the subjective bias of experts, certain uncertainties still exist. Second, to reduce computational complexity, this study only considers six pilotage scenarios composed of four operation conditions to conduct the MC simulation. These operation conditions can be further expanded. However, the increase in operation conditions will lead to an exponential growth in the number of operation scenarios, thus greatly increasing computational complexity. Finally, this quantitative analysis method is only a semi-quantitative analysis method used to identify risk transmission in a hypothetical pilotage operation scenario. The real operation scenario is temporal [35], and it is difficult for this method to address the quantitative problem of dynamic risk in a temporal operation scenario.

## 5. Conclusions

Ship pilotage processes have a high collision risk owing to the complex and changing water environment and dense navigation traffic [41]. FRAM modelling was used to describe the operation mechanism of a ship pilotage system from the perspective of functional characteristics. The critical couplings between functions under six pilotage operation scenarios were identified using a quantitative MC simulation method to analyse the resonance path generated by the strong coupling between system functions. Thus, the causative mechanism of risk transmission under dynamic variability of the function and nonlinear coupling was revealed. A case study demonstrated that the VPNs of functional couplings vary with ship pilotage operation scenarios. A comparative analysis of the simulation results of scenarios 1 and 6 showed that with the deterioration of operation conditions,

new functional resonance paths emerged in the pilotage operation system, and the ship collision risk increased. The transmission path of the collision risk could be identified by analysing the resonance path composed of the critical coupling in a specific operation scenario. The FRAM analysis solved the problem of selecting the monitoring indicators and formulated relevant indicators for the ship pilotage process according to risk transmission identification in specific pilotage operation scenarios to strengthen the pertinence and effectiveness of monitoring. Based on this, control measures were formulated to dampen the adverse output of functions and function resonance.

In this study, a quantitative FRAM analysis method was used to reveal the risk transmission mechanism of hypothetical pilotage operation scenarios. However, there are still limitations in the quantitative risk analysis of the real ship pilotage operation process. In future studies, a quantitative risk evaluation analysis method based on a random process may be proposed based on the nonlinear and dynamic characteristics of pilotage operation systems [42]. Based on real operational data and subjective and objective evidence, the temporal risk in the real ship pilotage process will be analysed to explain the evolutionary characteristics of operational risk. This study provides theoretical support for the engineering management of the ship pilotage process.

Author Contributions: Conceptualization, Y.G. and S.H.; methodology, Y.G. and Y.J.; software, Y.G.; validation, Y.X.; formal analysis, S.H.; investigation, W.L.; data curation, Y.G.; writing-original draft preparation, Y.G. and S.H.; writing-review and editing, Y.J.; visualization, Y.G. and W.L.; supervision, Y.J.; funding acquisition, Y.G. and S.H. All authors have read and agreed to the published version of the manuscript.

Funding: The research is financially supported by the National Natural Science Foundation of China (Grant No. 52272353), and also the Jiangsu Qing Lan Project (2023) and Nantong Science and Technology Plan Project (Grant No. JC22022062).

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Not applicable.
Acknowledgments: The authors would like to thank the Shanghai Harbour Pilot Association and Shanghai Maritime Safety Administration for their support in data provision. The authors would also like to thank the subject matter experts for their constructive suggestions.

Conflicts of Interest: The authors declare no conflict of interest.
