# Article 

## Dynamic Failure Risk Assessment of Wastewater Treatment and Reclamation Plant: An Industrial Case Study

Razieh Analouei ${ }^{1}$, Masoud Taheriyoun ${ }^{1, *}$ and Md Tanjin Amin ${ }^{2}$

## check for updates

Citation: Analouei, R.; Taheriyoun, M.; Amin, M.T. Dynamic Failure Risk Assessment of Wastewater Treatment and Reclamation Plant: An Industrial Case Study. Safety 2022, 8, 79. https://doi.org/10.3390/ safety8040079

Academic Editor: Raphael Grzebieta
Received: 2 October 2022
Accepted: 1 December 2022
Published: 4 December 2022
Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## 0

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Department of Civil Engineering, Isfahan University of Technology, Isfahan 8415683111, Iran
2 Mary Kay O'Connor Process Safety Center, Artie McFerrin Department of Chemical Engineering, Texas A\&M University, College Station, TX 77843, USA

* Correspondence: taheriyoun@iut.ac.ir


#### Abstract

Due to the growing scarcity of water resources, wastewater reuse has become one of the most effective solutions for industrial consumption. However, various factors can detrimentally affect the performance of a wastewater treatment plant (WWTP), which is considered a risk of not fulfilling the effluent requirements. Thus, to ensure the quality of treated wastewater, it is essential to analyze system failure causes and their potential outcomes and mitigation measures through a systematic dynamic risk assessment approach. This work shows how a dynamic Bayesian network (DBN) can be effectively used in this context. Like the conventional Bayesian network (BN), the DBN can capture complex interactions between failure contributory factors. Additionally, it can forecast the upcoming failure likelihood using a prediction inference. This proposed methodology was applied to a WWTP of the Moorchekhort Industrial Complex (MIC), located in the center of Iran. A total of 15 years' time frame (2016-2030) has been considered in this work. The first six years' data have been used to develop the DBN model and to identify the crucial risk factors that are further used to reduce the risk in the remaining nine years. The risk increased from $21 \%$ to $42 \%$ in 2016-2021. Applying the proposed risk mitigation measures can decrease the failure risk from $33 \%$ to $9 \%$ in 2022-2030. The proposed model showed the capability of the DBN in risk management of a WWTP system which can help WWTPs' managers and operators achieve better performance for higher reclaimed water quality.


Keywords: wastewater treatment plant; reclaimed water; dynamic risk assessment; dynamic Bayesian network; operational safety

## 1. Introduction

Reclaimed water for various purposes is a suitable and cost-effective option to compensate for water shortages, preserve existing water resources, and prevent water loss and environmental pollution [1]. Iran is increasingly experiencing scarcity because of climate changes, reduced rainfall, inappropriate management and wasting water. Moreover, Iran, as a developing country, faces rapid industrial development, leading to high water demand in industrial sectors. Thus, it is evident that replacing alternative water sources like recycled wastewater is paramount for industrial usage. Typical industrial water uses include process water, boiler, cooling tower, cleaning and stripping agent. The quality of industrial wastewater depends on the kind of industries, including mining, food and agriculture, tanneries, refineries and pharmaceuticals. It can have toxic contaminants like ammonia, heavy metals, phenols, organic contaminants, solvents and other materials [2,3]. In addition, the quantity of recycled water usage varies from process to process of industries and needs substantially higher quality for boilers and cooling towers, especially in pharmaceutical industries.

Given the growing use of treated wastewater and environmental concerns, it is necessary to assess the risk of industrial wastewater treatment plants to reach standard water quality [4]. If the recycled water does not meet the required standard, it can cause detrimental impacts on industrial facilities like sedimentation, fouling, corrosion, scaling and biofilm formation in the pipes and equipment of the industries.

In a WWTP, various factors can cause degraded performance, considered a risk of not fulfilling the effluent requirements for reuse purposes. Hence, it is pivotal to analyze distinct failure modes and their impacts on a WWTP through a systematic risk-based approach [5,6]. There are notable risk factors related to an industrial WWTP, which can fall into different categories: equipment failures, human errors, design failures and wet weather conditions. Given that a WWTP has complicated parts and various dynamic performances and faces operational challenges, static models are insufficient for risk analysis. Therefore, a dynamic risk assessment of a WWTP is needed to identify and mitigate system errors and failures to increase system reliability and treated water quality [7].

In the current literature, fault tree analysis (FTA), bow-tie (BT), and Bayesian network (BN) are used for risk assessment of water and wastewater treatment plants. The FTA is a deductive approach to determining the potential causes of an adverse event. Beauchamp et al. developed a method for technical and operational hazard identification of the water treatment plant based on FTA [8].

For the operational assessment of a reverse osmosis system in a water treatment plant, Bourouni used FTA and reliability block diagram for risk assessment of the reverse osmosis plant [9]. Taheriyoun et al. employed the FTA and Monte Carlo simulation to evaluate the reliability of a WWTP. It was determined that the most significant contribution to the system failure was human errors, climatic and mechanical factors, and sewer system problems, respectively [10]. Piadeh et al. proposed the combined FTA and event tree analysis (ETA) for reliability analysis of advanced treatment unit alternatives. The lowest failure probability was found for the coagulation-flocculation units, while reverse osmosis and ozonation units had the highest failure probabilities [11].

Tabesh et al. used two methods, including fuzzy fault tree analysis (FFTA) and Monte Carlo-based FTA, to evaluate the risk of a water treatment plant in Tehran. They found inappropriate reservoir design, power equipment failure and transfer pipe failure as the most effective factors in the plant's risk [12]. While FTA provides good performance to assess a hazard probability, it cannot describe the consequences. The event tree analysis (ETA) is capable of showing the consequences. Nonetheless, it cannot show how the initiating events' failure probability has been estimated. The bow-tie (BT) method can overcome the weakness of FTA and ETA by integrating both. It is composed of a fault tree, recognizing the possible basic events causing the critical event, and an event tree, representing the potential consequences of the critical event based on the failure or success [13].

Analouei et al. evaluated the risk of an industrial WWTP using the BT. They calculated the WWTP risk by about $41 \%$ and found operator errors as the most critical risk factor [14]. Tušer \& Oulehlová applied the BT method to identify the causes and consequences of risks in a WWTP based on documentation reviews, safety audits, interviews and check-list methods. The results showed that the low level of safety measures and the age of the WWTP technology could lead to unacceptable and undesirable risks [15].

Although FTA, ETA and BT have contributed significantly to the WWTP risk assessment, they cannot show conditional dependency between the variables and the dynamic nature of a system. Moreover, all these tools suffer from uncertainty handling problems [16]. In this regard, the BN is a method that can solve dependence modeling and uncertainty handling problems. It is a probabilistic reasoning network of conditional probabilities [17]. Kabir et al. estimated the risk of an urban water distribution system using BN-based data fusion. The goal of data fusion was to obtain a lower prediction error and higher reliability by using data from multiple distributed sources. The proposed technique was used to identify vulnerable and sensitive water pipes [18].

Anbari et al. proposed a risk assessment BN model to prioritize sewer pipes inspection by identifying high-failure risk areas. The results showed that about $62 \%$ of sewers had moderate risk while $12 \%$ were critical [19]. Zarei et al. mapped the BT method into the BN for the risk assessment of a gas transmission system. The proposed framework was used to evaluate the risk and determine the most critical accident scenarios in the system [20]. Shafiee Neyestanak and Roozbahani investigated the risk assessment of treated wastewater

using a novel hybrid BN. The method was applied for risk analysis of Iran's 27 wastewater treatment plants in four sectors: agriculture, landscape irrigation, groundwater artificial recharge and industry. The results demonstrated the capability of the method to predict the risks, and the risk of using treated wastewater in agriculture ( $26.9 \%$ ) was the highest compared to other sectors [21].

The conventional BN is static and cannot capture time dependency. Hence, the risk analysis methods mentioned above are not efficient for dynamic risk assessment. In other words, they cannot use time-dependent information to update the probability of events and consequent risk profile [22,23]. Therefore, it is more viable to develop a dynamic Bayesian network (DBN)-based methodology for dynamic risk assessment of WWTPs to overcome the existing methods' limitations. It will help to understand the time-dependent behaviors of risk factors and ensure the quality of water reclamation.

The DBN is an extension of the conventional BN that helps dynamically analyze a system's risk. It is possible to obtain the trend of the variables' failure probabilities across the period using the DBN [23,24]. The DBN-based approaches have successfully been used in the risk assessment of different systems and facilities in previous studies. Dawsey et al. developed a methodology based on DBN for real-time water distribution system's state parameter estimation. They presented an approach for drinking water monitoring using DBN to infer knowledge about the current state of a water distribution system [25].

Li et al. used the DBN in the risk analysis of an earth-rock dam breach [26]. Chen et al. conducted a multi-reservoir system's risk assessment. The authors utilized the DBN to predict the probability of wellhead fatigue failure during the service life [23]. Fam et al. applied DBN for analyzing well-decommissioning failures and long-term monitoring of decommissioned wells [24]. Kammouh et al. proposed an approach based on the BN and DBN to assess the time-dependent resilience of engineering systems [22]. Liu et al. showed how the DBN could be effectively used to model a WWTP. In this regard, a fuzzy partial least squares-based dynamic Bayesian network was presented to improve the prediction of the quality indices in WWTPs when confronting uncertainty, nonlinearity, and time-dependent characteristics [27]. Zhang et al. proposed a model integrating variable importance in in projection with dynamic Bayesian networks (VIP-DBN) to reach better prediction results, optimizing current approaches to handling dynamic characteristics, nonlinearity, and uncertainty simultaneously in papermaking WWTPs. The method was evaluated through two case studies. They showed that the model is an accurate and reliable approach to dealing with the shortcoming of existing soft sensor methods [28].

There are other risk assessment techniques that are used to risk analysis of diverse systems. Yari et al. used Data Envelopment Analysis (DEA) to evaluate blasting patterns in mining. In fact, incorrect blasting patterns can result in many safety problems. This study showed the ability of the DEA to blast operations [29]. Yu et al. proposed a comprehensive industrial wastewater treatment plant project evaluation approach based on the improved entropy- Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) method. A case study in china was evaluated using this method to solve the difficulties in accurate quantization and objective evaluation of an industrial sewage treatment project [30].

Yari et al. proposed a structure to evaluate the hazards of main decorative stone quarrying by implementing the Preference Ranking Organization Method. They found that economic, management and schedule risks are the most intimidating hazards in this field [31]. Ekmekcioğlu et al. produced district-based vulnerability, hazard and flood risk maps for Istanbul with a hybrid fuzzy analytic hierarchy process (AHP)-TOPSIS model [32]. Yari et al. presented a comprehensive model for ranking mines in the sense of all imposing attributes with an emphasis on safety parameters. In this paper, mines have been ranked using AHP-TOPSIS and fuzzy environment [33]. Hayaty et al. used the fuzzy Delphi analytic hierarchy process and TOPSIS method to risk assessment of $\mathrm{Co}, \mathrm{Cu}$, $\mathrm{Mo}, \mathrm{Zn}, \mathrm{Cr}, \mathrm{Mn}, \mathrm{Ni}, \mathrm{Pb}, \mathrm{Ti}$, and Fe in the mining sediment released to the tailings dam. In this research, the metals like copper, iron, and zinc had the highest pollution and critical risk [34]. Lane et al. used a sanitation safety plan (SSP) framework for risk assessment

of wastewater treatment systems. This framework identified potential hazards in 29 First Nations wastewater systems in Atlantic Canada. They found that 7% of hazardous events were high-risk while 69% had an unknown level of risk [35].

From the above literature review, it is evident that the current progress in the failure risk assessment of WWTP is noteworthy. However, it lacks a methodology that can handle complex interdependence among contributory risk factors, their multistate modeling, uncertainty, and the dynamic nature of risk and reliability. Therefore, this work aims to overcome these gaps. Since the BN does not accurately capture dynamic systems' behavior, the DBN can be used to model this temporal process's nature as a time-dependent probabilistic reasoning approach. Therefore, it can give an accurate estimate of the dynamic risk of a system. The current authors feel it is worth examining DBN's efficacy in dynamic risk assessment in a WWTP to bridge the existing knowledge gaps and propose a DBN-based methodology for risk assessment and management of industrial wastewater treatment and reclamation plants.

In this work, the risk factors were first identified through a comprehensive evaluation with the help of process flow diagrams (PFDs) and industrial experts, followed by developing the network structure and quantifying the probabilities. The overall study considered an operation for 15 years (2016-2030). The first six years' data were used to develop the DBN model, and the smoothing inference was used to identify the crucial risk factors. Based on these results, a prevention strategy was developed to effectively reduce the risk factors, which was further applied to the remaining nine years of operation. The results suggest significant improvement in failure risk reduction when the suggested measures are employed.

# 2. Materials and Methods 

### 2.1. Bayesian Network

The BN, also known as the Bayesian belief network (BBN), is a directed acyclic model based on the probabilistic relationships between the variables of a complex system [36]. This probability-based approach has predictive features to help decision-makers when complete information about a system is unavailable [37,38]. A BN has both qualitative and quantitative parts. The qualitative part of the model consists of a non-rotating graph in which the nodes represent the variables, and the arcs illustrate the cause-and-effect relationships between two nodes [39,40]. The parent/child relationship expresses the dependency between two variables in a BN. The link between two variables starts from a parent node and points toward a child node.

The quantitative part of a BN consists of the prior and conditional probabilities. The conditional probabilities are presented in a tabular form known as the conditional probability table (CPT). The CPT determines the degree of influence on the nodes [22]. The probability amount for each variable in the CPT is supplemented by the existing system information and expert opinions [41,42]. Figure 1 shows a simple example of a BN, where A and B are the parent (root) nodes of the child node C. Table 1 shows a CPT related to Figure 1. According to Table 1, each variable has two states: success and failure, which show how child node C is affected by the parent nodes A and B. For example, node C will have a $100 \%$ success rate if nodes A and B work successfully. It is worth noting that a node can have multiple states depending on the physical phenomenon that needs to be captured.
![img-0.jpeg](img-0.jpeg)

Figure 1. A simple flow diagram of the BN.

Table 1. A sample of the CPT related to Figure 1.


Bayes' theorem is used to analyze a BN model, as shown in Equation (1).

$$
P(X / Y)=\frac{P(Y / X) P(X)}{P(Y)}
$$

where $P(X)$ and $P(Y)$ show the probability of $X$ and $Y$, respectively. $P(X / Y)$ is a conditional probability; it depicts the likelihood of event $X$ occurring upon observing evidence $Y$. $P(Y / X)$ represents the likelihood of happening $Y$ given that $X$ has happened. $P(X / Y)$ is also known as the posterior probability.

# 2.2. Dynamic Bayesian Network (DBN) 

A DBN is an advanced version of a BN, capable of analyzing a system over time. It does not mean restructuring the BN or analyzing its parameters dynamically, but the overall system evaluation can be updated dynamically [23,43]. DBN uses nodes to indicate variables in a graph like the conventional BN. Moreover, dynamic causal relationships between the variables are shown by the arcs. It should also be noted that some nodes may not change over time and thus should not be expressed dynamically. The conceptual model and the causal relationships between the nodes are established based on expert knowledge and analyzing PFDs.

A simple structure of the unrolled DBN is shown in Figure 2a. In this figure, the temporal variables are the parent nodes, A and B, connected through temporal arcs that appear from time steps 0 to $N$. The child node $C$ depends on these parent nodes: $A$ and $B$, at each time slice. Figure 2b shows a brief diagram of DBN using self-rolling arcs at the parent nodes. The written number " 1 " on the arcs represents an influence spanning over one time-step called a first-order self-rolling arc. For example, the variable $A_{t}$ can only influence $A_{t+1,}$ not $A_{t+2}$ [22].
![img-1.jpeg](img-1.jpeg)

Figure 2. (a) A simple diagram of an unrolled three-node DBN. (b) DBN diagram with self-rolling nodes corresponding to Figure 2a.

The transition model from the former to the current time step for $F$ as a set of random variables $x_{1}, x_{2}, x_{3}, \ldots, x_{n}$ in a DBN $\left(x_{i} \in F\right)$ is presented in Equation (2) [44].

$$
P\left(F_{t} / F_{t-1}\right)=\prod_{i=1}^{n} P\left(F_{i, t} / P a\left(F_{i, t}\right)\right)
$$

where $F_{i, t}$ represents $i$ th node at time $t, P a\left(F_{i, t}\right)$ is the parent node of $F_{i, t}$ from the same and previous time steps, and $n$ is the number of nodes in the network. The process in a DBN repeats after the second time slice, so the variables for the slice $t=2,3, \ldots, N$ do not change. It permits expressing the system using only two slices, including the firstand second-time-slices. The joint probability distribution for a sequence of time-slices, including $F$ set from $t=1$ to $N$, can be expressed in Equation (3) [45].

$$
P\left(F_{1: N}\right)=\prod_{t=1}^{N} \prod_{i=1}^{n} P\left(F_{i, t} / P a\left(F_{i, t}\right)\right)
$$

In a DBN, time dependency must be included in the CPTs since variables depend on the previous time slice. Additionally, two sets of CPTs are needed to describe a dynamic node. The second set gives the result of dynamic variation. A DBN has two notable features: smoothing and prediction inferences. Smoothing refers to a node probability estimation in the past based on the collected evidence up to the current time slice.

On the other hand, prediction forecasts a node state's future probability based on the current evidence. The DBN can be updated with both hard and likelihood evidence. Hard evidence is updating any state of a node in a DBN with a $100 \%$ success value, and likelihood evidence implies updating the DBN with probabilistic evidence (i.e., $\mathrm{P}($ failure $)=0.50$ ) [43,46].

In this study, the qualitative and quantitative parts of the DBN model related to the MIC WWTP are established based on expert knowledge and PFDs. A first-order self-rolling arc is considered for the parent nodes of the DBN model, and the corresponding nodes are updated using the likelihood evidence to predict the risk of the WWTP. The GeNle 2.4 software is used to develop the DBN.

# 2.3. Proposed DBN-Based Methodology 

Figure 3 shows the flowchart of the proposed model summarized in seven steps. These steps are discussed below.

Step 1: The methodology starts with analyzing the process flow diagram of the WWTP plant. It is crucial to study the process flow to understand the interaction among different components and their potential vulnerability to failure.

Step 2: Identifying the major risk factors and understanding how these factors can bring adverse outcomes is necessary. The historical data gives an overall idea about the persistent failure causes. However, it is impossible to obtain all the factors from the data since many of them may not have been experienced during the considered time frame. The experts can aid in this context by sharing their operational experience. They can suggest additional factors on top of the ones from historical data. This step aims to find all the possible factors that may result in complete or partial WWTP failure.

Step 3: The qualitative model is constructed based on risk factors, their dependencies, causal relationships and consequences determined in step 2.

Step 4: The qualitative network needs to be inserted with the prior and conditional probabilities for quantitative risk assessment. In the current work, to obtain these, a survey was used. A set of questionnaires was sent to experts who provided their feedback, which was incorporated into the DBN.

Though the DBN nodes can have multiple states, we have considered binary states: success and failure. The leaf (final) node indicates the overall consequences used in risk calculation. According to the water quality requirement for industrial reuse, as mentioned in the plant description section, three scenarios are selected for leaf node.

1. Without the fouling, corrosion, scale and biofilm in the facilities of an industry (C1)
2. Long-term creation of the fouling, corrosion, scale and biofilm in the industrial facilities (C2)
3. Short-term and severe creation the fouling, corrosion, scale and biofilm in the industrial facilities (C3)
![img-2.jpeg](img-2.jpeg)

Figure 3. The framework of the proposed model.
Accordingly, the risk is the summation of C 2 and C 3 probabilities, while the C 1 probability equals the reliability, as shown in Equations (4) and (5). It is worth noting that reliability is the non-failure operational state. In the obtained consequences, C 1 indicates a non-failure condition. Consequently, it has been used to predict dynamic reliability.

$$
\begin{gathered}
\text { Risk }=P(C 2)+P(C 3) \\
\text { Reliability }=P(C 1)
\end{gathered}
$$

Step 5: Significant factors (SFs) contributing to system failure are determined in this step. It is performed by importance analysis (IA), giving failure evidence to the leaf node in a network and observing percentage change in the prior probability of the root nodes. Such analysis determines the significance of each parent node in the occurrence probability of the leaf node [45]. Mathematically, it can be expressed as:

$$
I A_{i}=\frac{P\left(T=1 / E_{i}=1\right)-P\left(T=1 / E_{i}=0\right)}{P(T=1)} \times 100 \%
$$

where $E_{i}$ corresponds to the parent nodes, and $T$ represents the leaf node in the DBN.
Step 6: The mitigation measures are proposed in this step to increase the system's reliability. According to the factors that have the most significant impact on the risk captured from step 5, we contacted the experts to examine the results obtained through the DBN. Obtaining their feedback, the DBN was updated with evidence (to see how the risk profile would be, had these factors been well managed).

Step 7: The updated BN is analyzed from two different perspectives. The first one is to see how effective these mitigation measures could be for managing the past period. The

smoothing inference has been used in this regard. Given that the measures were effective in reducing risk, these were further used to forecast the risk in the coming years. This step is important to help managers and operators to boost the system performance.

# 3. Results and Discussion 

### 3.1. Case Study

The MIC WWTP has a capacity of $1000 \mathrm{~m}^{3} / \mathrm{d}$ and is located in Isfahan province, the center of Iran. The geographic location $\left(33^{\circ} 03^{\prime} 27.9^{\prime \prime} \mathrm{N} 51^{\circ} 30^{\prime} 15.4^{\prime \prime} \mathrm{E}\right)$ is shown in Figure 4. This plant is mainly composed of two parts. The first part contains the primary and secondary biological treatment processes, and the second includes the advanced treatment processes that provide high-quality reclaimed water for industrial use. Figure 5 shows the PFD of the plant. According to the wastewater flow path, the first part includes the inlet pump station, emergency tank, bar screen, grit chamber, and equalization tank as the physical treatment unit. Then, secondary biological treatment consists of upflow anaerobic baffled reactor (UABR) and moving bed biofilm reactor (MBBR), followed by secondary sedimentation and chlorination unit. The advanced treatment consists of chemical pretreatment and sand filtration, reducing the effluent's suspended solids and turbidity. Then, ultrafiltration (UF), activated carbon and reverse osmosis (RO) are used to remove the residual organics and mineral solvents as total dissolved solids (TDS).

The reclaimed water is used in the cooling towers and boilers as process water, cleaning and stripping agent in various industries in the MIC, including mining, food and agriculture, tanneries, refineries, and pharmaceuticals. Water quality requirements for reclaimed water include electric conductivity (EC) $<500 \mu \mathrm{~s} / \mathrm{cm}$, turbidity $<1$ NTU, chemical oxygen demand $(\mathrm{COD})<5 \mathrm{mg} / \mathrm{L}$ and pH range $6-9$. The challenges associated with satisfying these water quality requirements stem from the probable failure in each treatment unit.
![img-3.jpeg](img-3.jpeg)

Figure 4. The geographic location of MIC WWTP.
![img-4.jpeg](img-4.jpeg)

Figure 5. Process flow diagram of the MIC WWTP.

# 3.2. Qualitative Model Development 

The PFD is first analyzed, and associated risk factors are identified. In this study, six major factors, including operator error, improper design, wet weather conditions, equipment service failure, high inflow rate and emergency storage tank failure, were defined as the most important causes of system failure. Moreover, the variables affected by these factors and the consequences were determined based on historical data and experts' judgment.

According to the key role of operators in a WWTP, such as controlling and monitoring unit processes, sampling, chemical addition and emergency repairments, we included operator errors in all the parts of WWTP. The dynamic assessment of the system, changes in operator numbers, professional training, passing related tests and gaining experiences over the years can substantially affect the risk of a WWTP.

Equipment service failure is another key factor in creating a risk that causes system failure. Many equipment and facilities experience natural aging of infrastructures like wear and tear during the different years. With systems aging and technology changes, meeting standard with existing equipment and processes becomes more difficult [47]. Moreover, inappropriate and irregular services can have considerable impacts on a WWTP. As mentioned, the design problems in a WWTP play an essential role in declining reliability. For instance, industrial development, urban growth and improper and inaccurate design are design factors that can cause a system failure.

The water quality requirement for industrial use is based on fouling, corrosion, scaling and biofilm prevention. In general, boilers need a higher quality of feed water because of operating at high temperatures and pressure [48]. Parameters such as TDS, alkalinity, silica, iron, manganese, copper, nitrogen, phosphorus and COD should be controlled to prevent operational problems. As discussed in the methodology section, three scenarios are expected due to reclaimed water consumption.

The qualitative DBN model of the MIC WWTP was constructed in three parts, as shown in Figures 6-8. The network consists of the leaf node as the consequence node, 34 events at the intermediate level, and 32 parent nodes at the bottom level of the network. Figure 6 shows the conditional relationship between parent and child nodes related to aerobic reactor failure. There are two kinds of nodes: static and dynamic nodes. Static nodes' prior are time-invariant, while it is the opposite for the dynamic nodes (indicated by the self-rolling arcs).

In addition, three types of dependencies are available between nodes which are defined: (i) from dynamic node to dynamic node, (ii) from static node to static node and (iii) from static node to dynamic node [49]. In this study, all parent nodes except improper design are identified as the first-order dynamic nodes-the probability of the current time step depends on the previous time step. The intermediate and leaf nodes are considered static. However, these can give dynamic failure estimates, obtaining the time-variant probabilities from the root nodes.

The network, which corresponds to anaerobic and aerobic reactors' performance (Figure 6), has eight, three, four, two and one parent nodes for operator error, improper designs, equipment service failure, emergency reservoir tank failure and wet weather conditions, respectively. The improper design node highlighted in yellow is the static variable that does not change throughout the time steps. As shown in Figure 6, secondary sedimentation tank failure has been affected by the parent nodes consisting of seven operator error variables, three improper design nodes, one equipment service failure variable and two high inflow rate nodes. The normal arcs connect the intermediate nodes, while the self-rolling arcs connect a root node's current probability to the past time-step.

Figure 7 illustrates the relationships among the leaf node, the first part of the MIC WWTP performance and the units of the advanced treatment part. The performance failure and advanced treatment parts nodes were connected to the consequence node using normal arcs.

![img-5.jpeg](img-5.jpeg)

**Figure 6.** The DBN model of the MIC WWTP (part 1—anaerobic and aerobic reactors' performance).

![img-6.jpeg](img-6.jpeg)

**Figure 7.** The DBN model of the MIC WWTP (part 2—Performance of the secondary sedimentation tank).

![img-7.jpeg](img-7.jpeg)

Figure 8. The DBN model of the MIC WWTP (part 3).

# 3.3. Prior and Conditional Probability Estimation 

In the current study, the prior and conditional probabilities were determined using the average value of the experts' opinions extracted from the questionnaires (scored in the range of $0-1$ ). With a modification according to the case-based experiences, the questionnaires were provided based on the operation and maintenance problems of different treatment units of the case study discussed in the literature [14,49,50]. The questionnaires were sent to the selected experts, including the manager and vice-manager of the MIC WWTP, three operators of the WWTP, the WWTP design engineer and four environmental engineering faculties. All the probabilities in the CPTs are the average values of the aggregated expert opinions. A sample of the filled-out questionnaire related to E16 (emergency storage tank failure) and E17 (operator error) is presented in Table A1 (Appendix A).

As an example of the estimated conditional probabilities, the CPT of the high toxic entry related to the secondary sedimentation tank from Figure 6 is presented in Table 2. As this node is static, its CPT is constant for all the time steps. However, its only parent node, operator error (E30), is modeled using a first-order self-rolling arc. The probability of successful high toxic entry is 0.99 , considering the success of both parent nodes: operator error and improper design, while it is zero for the failure case of both parent nodes.

Table 2. The transition CPT for the highly toxic entry related to the secondary sedimentation tank.


As mentioned in Section 2.2, each parent node at time-slice $t$ is influenced by itself at time-slice $t-1$. Two sets of CPTs at $t=0$ and $t=1$ are needed to describe the dynamic variation of a self-rolling node. For illustration, the prior probabilities of E1 (operator error related to anaerobic reactor failure for times 0 and 1 are shown in Table 3. Once all the priors and CPTs are inserted, the DBN model can be used for failure risk assessment.

Table 3. The prior probabilities of the E1.


# 3.4. Quantitative Analysis of the Model 

The DBN model was analyzed for 15 time-slices divided into two parts of past and future periods. The past period was considered from the beginning of the operation in 2016 up to 2021 (6 time-slices). It used the smoothing feature of the DBN to predict the associated risk in the stated period. On the contrary, the forecasted risk from 2022 to 2030 ( 9 time-slices) was estimated using the prediction inference. The average risk values and trend of variations of both periods were compared to assess the impact of mitigation measures on risk reduction to show how the current work can give a good means of risk management.

### 3.5. The Past Period Risk (2016-2021)

The probabilities of the consequences node from 2016 to 2021 (6 time-slices) were calculated by analyzing the DBN model. The probability of C 1 in the first year of operation was $79 \%$, reaching $58 \%$ at the end of the sixth year (2021). The consequence of C 2 in the first and sixth year of operation are $15 \%$ and $28 \%$, respectively, while the C3 probability increases from $6 \%$ to $14 \%$. As mentioned earlier, C 1 and the sum of C 2 and C 3 are the reliability and risk estimates, respectively. From an operational perspective, these two measures are vital for decision-makers. The risk and reliability assessment results are presented in Figure 9. The risk increased from $21 \%$ to $42 \%$ in 2016-2021, with an average of $31 \%$. The risk trend shows that the system performance declined during the past period, and it is vital to control the risk factors and improve the system reliability. As expected, system reliability degraded over the years.

## Past risk and reliability

![img-8.jpeg](img-8.jpeg)

Figure 9. The dynamic failure risk of the MIC WWTP between 2016 and 2021.
As mentioned in Section 3.1, The MIC WWTP has a capacity of $1000 \mathrm{~m}^{3} / \mathrm{d}$, and the treated wastewater is completely reused for receiving sectors. The removal rate and other parameters, such as standard effluent limit, COD, biochemical oxygen demand (BOD) and total suspended solids (TSS) for 2016 and 2021, are presented in Table 4. The higher level of failure risk and lower reliability level can be perceived through the decreasing removal rate. For instance, the BOD removal rate in 2016 was $92 \mathrm{mg} / \mathrm{L}$. In contrast, this rate is $67 \mathrm{mg} / \mathrm{L}$ in 2021-a significant reduction from the earlier level, an indication of a reduction in operational reliability, and an increase in higher failure risk. The results in Figure 9 also suggest the same risk and reliability patterns, which shows the validity of the developed DBN model for dynamic failure risk assessment.

The next task is to identify the SFs that could help to improve performance. Equation (6) and the DBN model were utilized in this context. The results suggest human errors have the most important role in risk growth. The important SFs based on average values for each factor from 2016 to 2021 are shown in Figure 10. It can be seen that human errors at 50% and inappropriate weather conditions at 0.3% have the most and least contribution to the risk of the system, respectively. It indicates that more attention is required to develop an effective protocol for the operators to follow. Nature has an impact; however, it is much lower than man-made impacts.

Table 4. WWTP parameters with removal rate for 2016 and 2021.


Signficant risk factors
![img-9.jpeg](img-9.jpeg)

Figure 10. Significant risk factor identification, where X1, X2, X3 and X4 denote operator errors, improper design, emergency reservoir tank failure and high inflow rate, equipment service failure, and wet weather conditions, respectively.

The suggested mitigation measures are presented in Table 5, considering the risk priorities in the 2016-2021 period. The operator error that played the most pivotal role in creating and growing the risk of the MIC WWTP gets the highest priority, and several mitigation measures have been proposed based on the discussion with the industrial experts. When it comes to wastewater treatment, the most important persons are operators because of their responsibilities for treating the wastewater to meet available standards. Thus it seems logical to pay special attention to decreasing operator errors-one of the effective solutions is to use modern technology and automatic devices for wastewater treatment plants. However, it is worth noting that human factor analysis is a specialized field obtaining significant attention due to humans' role in several accidents in the past few decades.

Table 5. The proposed risk-mitigating measures of the MIC WWTP.


# 3.6. The Future Period Risk (2022-2030) 

The risk mitigation measures were inserted into the DBN in terms of evidence extracted by averaging the expert opinions. The questionnaires were provided to the same experts who suggested mitigation measures of $0-100 \%$. These feedbacks were averaged, and the mean value for each mitigation measure was used to update the DBN. Table 6 shows the updated probabilities of node E1 (operator error related to anaerobic reactor failure) during the prediction period. Similarly, the updated probabilities of the other nodes can be obtained for the period 2022-2030. Moreover, the dynamic risk value for each time slice can be predicted.

Table 6. The updated probability of E1.


The reliability starts at $67 \%$ in 2022 and ends at $91 \%$ in 2030. The probability of C 2 in the seventh year of operation will be $20 \%$ and degrade to $9 \%$ at the end of the fifteenth year of system operation. Likewise, a declining profile is observed for C3 if the preventive measures are properly applied, as suggested by the experts. The risk of the MIC WWTP using the risk reduction schemes will decrease from $33 \%$ to $9 \%$ in 2030 (Figure 11). The average risk in this period was calculated as about $20 \%$. Compared to the risk of the system in the 2016-2021 period, it can be understood that the average risk of the MIC WWTP will be reduced by $11 \%$, which shows the efficiency of the proposed mitigation measures.

Forecasted risk and reliability
![img-10.jpeg](img-10.jpeg)

Figure 11. Dynamic risk probability of the MIC WWTP for the future period (2022-2030).

# 4. Conclusions 

Given that there are many risks and uncertainties during the operation period of a WWTP, a dynamic risk assessment of the system can be a suitable way to identify and reduce failures. The present study conducted an industrial WWTP risk assessment using the DBN-based systematic methodology, with an aim to capture complex interdependence among failure factors, uncertainty, multistate analysis and modeling dynamic risk and reliability. The model of DBN related to the MIC WWTP located in the center of Iran was established based on expert knowledge and PFD. The model was analyzed to determine the dynamic risk probabilities in the two periods of 2016-2021 and 2022-2030. The aim was to evaluate the past risk and identify the factors that need attention to minimize the failure risk.

The significance factor identification showed that operator error was the most effective factor in the risk. The risk of the future period (2022-2030) was predicted by considering proposed mitigation measures based on the prioritized risk factors. The suggested measures can decrease the failure risk from $33 \%$ in 2022 to $9 \%$ in 2030, with an average of $20 \%$. The proposed model showed an application of DBN in the dynamic risk management of a complex WWTP system. It can help WWTPs' managers and operators achieve better performance for higher reclaimed water quality during operation.

This work holds practical significance since the DBN model has been developed using data from a real industrial operation (Moorchekhort Industrial Complex). The framework has been developed based on several consultations and feedback from experts from industry and academia. The findings were shared with the industry to improve their performance. The industrial personnel provided a positive impression of the findings of this study. For the reproducibility of this work, a sample questionnaire has been provided with this paper which will help the industries to implement the current work in their facilities. Therefore, this work can help the WWTPs' managers to improve system operation by identifying and predicting the risk of violating effluent water quality requirements.

During plant visits and consultations with industrial personnel, it was noticed that they often used linguistic terms to express the operating condition (i.e., high-low). Such issues can be handled by integrating fuzzy theory with the current framework. A fuzzy DBN would be the best solution to reduce uncertainty and capture such linguistic terms. Instead of using average values of feedback, a weighted average could be used to give proper weight to the received feedback based on the relevant experience. The current work has not considered waste removal failure, which significantly impacts economic performance [52,53,54]. These will help improve and apply the current work.

Author Contributions: R.A.; conceptualization, methodology, software, validation, formal analysis, investigation, writing-original draft preparation, M.T.; investigation, resources, writing-review and editing, visualization, supervision, project administration, data curation, funding acquisition, M.T.A.; conceptualization, methodology, software, writing-review and editing, supervision, project administration. All authors have read and agreed to the published version of the manuscript.
Funding: This research received no external funding.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Data will be made available upon request.
Acknowledgments: We thank Seyed Alireza Momeni, Mahnaz Heydari, and Hamideh Ebrahimi from the MIC WWTP for preparing the plant's operational data and completing the questionnaires. We also acknowledge the contribution of Eng. Hamidreza Oroomieh for sharing his experience in wastewater treatment plant design and operation.
Conflicts of Interest: The authors declare no conflict of interest.

# Appendix A 

Table A1. Sample of filled-out questionnaire.

