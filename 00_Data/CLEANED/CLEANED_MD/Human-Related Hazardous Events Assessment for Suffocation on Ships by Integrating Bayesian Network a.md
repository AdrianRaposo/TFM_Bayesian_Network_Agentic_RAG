# Article 

## Human-Related Hazardous Events Assessment for Suffocation on Ships by Integrating Bayesian Network and Complex Network

Weiliang Qiao ${ }^{1, * *}$ (D), Hongtongyang Guo ${ }^{1}$, Enze Huang ${ }^{1}$, Wanyi Deng ${ }^{2}$, Chuanping Lian ${ }^{3}$ and Haiquan Chen ${ }^{1}$

## check for updates

Citation: Qiao, W.; Guo, H.; Huang, E.; Deng, W.; Lian, C.; Chen, H. Human-Related Hazardous Events Assessment for Suffocation on Ships by Integrating Bayesian Network and Complex Network. Appl. Sci. 2022, 12, 6905. https://doi.org/10.3390/ app12146905

Academic Editor: José A. Orosa
Received: 17 June 2022
Accepted: 5 July 2022
Published: 7 July 2022
Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## 0

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Marine Engineering College, Dalian Maritime University, Dalian 116026, China; ghty@dlmu.edu.cn (H.G.); huangenze@dlmu.edu.cn (E.H.); chenapec@dlmu.edu.cn (H.C.)
2 School of Maritime Economics and Management, Dalian Maritime University, Dalian 116026, China; dwy@dlmu.edu.cn
3 COSCO Shipping Seafarer Management Co., Ltd., Dalian Branch, Dalian 116026, China; linlili@sino-ocean.com

* Correspondence: xiaoqiao_fang@dlmu.edu.cn


#### Abstract

To investigate the human-related factors associated with suffocation on ships during docking repair, a comprehensive analysis model composed of a Bayesian network (BN) and a complex network (CN) is proposed in the present study. The principle of event tree analysis (ETA) is firstly applied to identify the hazardous events involved in the accident according to the accident report, based on which the CN would then be developed with the logic relationships among the hazardous events. The improved K-shell decomposition algorithm is utilized to determine the criticality of nodes in the CN , the results of which are then used to develop the BN model within the framework of a human factor analysis classification system (HFACS). Then, the developed BN model can be simulated with the probability distribution of all the nodes within the BN, which are obtained on the basis of node criticality. Finally, the results of the BN simulation are interpreted from the perspectives of a brief analysis, backward analysis and sensitivity analysis. The results are verified with existing studies and the accident investigation report issued by authority, which are presented as evidence to verify the effectiveness of the proposed methodology to evaluate the human-related risk involved in the suffocation on ships. The methodology proposed in this study integrates the advantages of BN and CN to investigate the human-related hazardous events involved in maritime accidents, which can be seen as the main innovation of this work.


Keywords: suffocation on ships; human-related hazardous events; Bayesian network; complex network; HFACS

## 1. Introduction

The operational scenarios in shipyards are characterized by high risk level due to the frequent interaction among various stakeholders and the different work types involved during docking repair [1-3]. During docking repair, it is common that a lot of professional and dangerous operations are carried out simultaneously in the same space, meaning that risk factors are highly interconnected and harmful, especially human-related factors [4]. In Singapore, accidents and incidents which occur during docking repair are receiving attention, and a legislative amendment was passed by the attorney general's chambers [5] to prevent or minimize the occurrence of such accidents. Later, in 2019, the International Labor Organization (ILO) adopted a revised code of practice for safety and health in shipbuilding and ship repair at the 329th session [6], which aimed to improve safety and health practices by providing good practice for governments, employers, and workers. However, occupational incidents and accidents still occur in the shipyard during docking repair, which indicates that safety management processes during docking repair need to be

further improved [7]. In addition, with the influence of some important regulations and codes adopted by International Maritime Organization (IMO), such as the revised MARPOL Annex VI [8] and the International Convention for the Control and Management of Ships Ballast Water and Sediments (BWM) [9], a large number of operating ships have to be refitted during docking repair to satisfy the new regulations. It can be reasonably predicted that the ship repair industry will continue to run with relatively high demand. For instance, according to the statistics of the China Association of the National Shipbuilding Industry (CANSI), in 2019, the shipbuilding industry and ship repair industry accounted for $65.4 \%$ and $4.2 \%$ of the overall business income in China, respectively. Compared with the figures of 2015, the proportion of these increased significantly [10]. It is important and urgent to reduce the rate of occupational accidents and accurately and efficiently promote industrial safety management.

# 1.1. Related Studies 

In the scientific literature, the general characteristics and common causes of accidents can be summarized in terms of the time, place, type of work, age of workers, work experience, etc., through statistics and research on historical accidents [4,11,12]. When the average temperature is above $25^{\circ} \mathrm{C}$ from June to September every year, the death toll is the highest. These aspects can be taken as accident-related risk factors for analyzing the cause and effect of occupational accidents from a comprehensive perspective [13,14]. However, such studies often lack pertinence due to the variety of accident types; thus, some studies began to focus on causal analysis based on a typical accident or operation category [15-17]. Still, accidents that may occur in confined spaces such as cargo holds have not received enough attention. In fact, it is estimated that there are 0.05-0.08 deaths per 100,000 workers in such working conditions [18]. In addition, nearly 38 people die of poisoning or suffocation accidents in confined spaces every year [19]. In Virginia, the highest death rate per million employees is occupational confined-space accidents in shipbuilding and repair facilities, with a probability of $23.2 \%$ [20]. Therefore, it is especially necessary to analyze and solve the safety dilemma surrounding this kind production activity.

When there is a production accident, people tend to investigate the causes of accidents on the surface, rather than analyze the root causes, which leads to simply attributing the accidents to worker violations or errors. As a result, the risk control strategy is always inadequate, and accidents endangering the safety of employees occur repeatedly. Consistent with these observations, organizational and management factors such as the weak safety awareness of workers, high work pressure, inadequate professional familiarization and training, and lax supervision of processes [1,17,21] are increasingly being recognized as the deep-seated causes of accidents that need to be acknowledged. These factors are closely related to human behavior, not only human errors. Here, the related risks are collectively referred to as human factors. It is generally acknowledged that, with the economic environment and advanced science and technology providing technical guarantees and a material basis for the realization of safe conditions, human factors play an increasingly prominent role in the occurrence and evolution of accidents [22,23].

In addition, the risks that lead to incidents and accidents in shipbuilding and repair, including human factors, are extremely complex and uncertain. Therefore, it is crucial to systematically study the formation mechanism of accidents and the causal relationship between risk factors. Risk assessment is a useful technology in the field [3,13,24]. Some qualitative research methods involving literature reviews, field surveys of practitioners, and expert interviews can assist in the identification of potential risk factors related to accidents [25]. They provide factual information about working conditions, occupational characteristics, and management vulnerabilities that may not be covered in official accident reports, promoting a further understanding of the risks and hazards faced by employees. Meanwhile, studies have shown that the causes of accidents are multifaceted and variable [23,26,27]; hence, there is a need to classify these factors from different research perspectives. The decomposition and classification of human factors have been studied

and widely applied in various fields by [28] and other researchers. The HFACS is widely regarded as having great value in the systematic analysis of the causes of accidents, which takes the continuous influence of high-level factors on low-level factors into account [29]. However, the complex logic relationships among factors allocated at different hierarchical layers under the HFACS framework are frequently ignored. Therefore, this study considers the logic relationships among different factors to implement risk evaluation.

The methodologies employed to investigate the causation for shipyard accidents are mainly represented by statistics-based techniques, such as those used in [1,4,12,30,31]. To further analyze shipyard accidents, the hybrid methodologies proposed in recent years for marine accident analysis can be referred to for investigation of the potential risks involved in shipyard accidents. Some of these hybrid methodologies are listed in Table 1.

Table 1. Hybrid methodologies used within the scope of marine accident analysis in recent years.


Lots of complex causal relationships and uncertain risks are involved in shipyard accidents, which can hardly be addressed by statistics-based approaches. Therefore, it is necessary to consider hybrid methodologies to improve the safety management in shipyards by analyzing human-factor-related accidents. With reference to similar studies in the maritime industry, as listed in Table 1, it can be observed that BN is widely accepted as an effective technique to model maritime accidents. To implement the Bayesian inference, the probability distribution for the nodes within the BN is required; for this purpose, fuzzy theory and expert elicitation are frequently applied. However, in these cases, the subjective bias and knowledge limitation may inevitably reduce the accuracy of the Bayesian inference. Therefore, in the present study, the exploratory application of a CN approach is conducted to quantify the probability of all the nodes within BN. The focus of this study is to establish a comprehensive accident analysis and risk assessment model that can reflect the risk propagation path, and then combine with the fuzzy algorithm and information theory to quantify and address the uncertainty of human factors in a ship repair system. Moreover, an accident that occurred in a Chinese shipyard is used as an empirical case to verify the proposed method. A classic method of accident analysis, fault tree analysis (FTA), is used and combined with fuzzy extent AHP to systematically establish the causal relationship of accidents and address the randomness of risk factors in this study. In addition, BN is adopted to predict the probability of risk because of its powerful learning and reasoning capability in many intelligent algorithms. In particular, the introduction of canonical probabilistic models has come to be recognized as an ingenious method to reduce the difficulty of obtaining the conditional probability between nodes in a BN, and it can simplify and deal with the problems of complex systems.

# 1.2. Innovative Contribution 

The purpose of this study is to develop a comprehensive, human-related hazardous events assessment methodology with full consideration of the influences from social and technical aspects. Using this methodology, the risks stemming from on-site operations and management level can be quantitatively analyzed for accidents which occur during docking repair. For this purpose, a suffocation accident which occurred in a Chinese shipyard is exampled as a case study to illustrate the application of the proposed methodology. By the application of the methodology, the accident report is firstly qualitatively interpreted according to the basic principle of ETA to identify the human-related hazardous events involved in the suffocation accident. Additionally, the logic relationships among the identified hazardous events are analyzed to establish the CN, which is then evaluated by the improved K-shell decomposition algorithm to obtain the node criticality. Meanwhile, the identified hazardous events are reorganized within the framework of the HFACS with reference to the node criticality to develop the framework of the BN. Subsequently, the above-obtained node criticality is utilized to calculate the probability distribution of the nodes involved in the BN, which is essential for Bayesian inference. The innovative contribution of the proposed methodology is summarized as follows.

1. Theoretical exploration of quantitatively describing the human-related hazardous events involved in the maritime accidents which have occurred during docking repair with a full consideration of factors from social-technological aspects.
2. The application of the CN in this study is able to conquer the shortage of the ETA, in which it fails to consider the logic relationships among hazardous events allocated at different levels.
3. The determination of prior probability and conditional probability of the Bayesian inference is implemented by the improved K-shell decomposition algorithm.
4. An entire solution to assess human-related hazardous events in shipyard accidents is established, and the consistent precision of this is validated with a case study of a suffocation accident.

### 1.3. Organization

The remainder of this paper is organized as follows. Section 2 describes the materials and methods for the evaluation of human-related hazardous events which contribute to suffocation. The results and discussion are presented in Section 3. Finally, the paper is concluded in Section 4.

## 2. Materials and Methods

### 2.1. Risk Scenario and Overview for the Proposed Methodology

### 2.1.1. Risk Scenario Description

On 5 May 2021, at approximately 14:45, a newly built 180,000-tonnage bulk carrier named "H1502" suffered from a poisoning and suffocation accident caused by high-density nitrogen during docking repair in a shipyard in Shanghai. Unfortunately, this accident caused two deaths. The following details were extracted from the accident report which can be accessed from Office of Emergency Management of Shanghai [43].

In the morning of the 5 May, the operators were assigned to purge the pipes with pure nitrogen in the stem of the ship by the coordinator on site, in the absence of a representative of the ship's owner. After noon, the operators on site implemented the purge in the cabin containing the bathymeter, a space regarded as a typical enclosure space, without taking effective safety measures. At approximately 14:30, two hydraulic pipes which connected together with the "U" pipe, marked as A and B, respectively, were purged fully with nitrogen. Then, the outlet valve of nitrogen was closed. Subsequently, the operators on site dismantled the "U" pipe connecting the hydraulic pipes $A$ and $B$, and intended to purge hydraulic pipe A. For this purpose, the outlet valve of nitrogen was opened again. At this moment, a large amount of nitrogen leaked into the cabin. Five minutes later, the operators were found syncope in the cabin.

# 2.1.2. Overview for the Proposed Methodology 

In the present study, a novel methodology integrated by CN and BN is proposed to investigate the human-related hazardous events involved in the suffocation on ships from the perspective of the complex social-technological system. The general principle for the proposed methodology is illustrated in Figure 1, and there are four main steps for its implementation.
![img-0.jpeg](img-0.jpeg)

Figure 1. Overview for the proposed methodology.
Step 1—Risk scenario description: The human-related hazardous events involved in the accident report are firstly identified based on the principle of ETA. Then, the directed CN is developed on the basis of hazardous events, with the nodes and logic relationships among hazardous events being directed edges. In addition, the topological description for the developed CN is also conducted with the aspects of weights and degrees.

Step 2-Human-related hazardous events: The criticality of the nodes involved in the directed CN is then calculated by means of an improved K-shell decomposition algorithm based on the values of weights and degrees.

Step 3-Development of BN: The framework of the BN is first developed by the integration of HFACS and the results of node criticality. Then, the prior probability distribution for root nodes and the conditional probability tables for other nodes can be determined with application of the probability-related method proposed in this study, on the basis of node criticality.

Step 4-Human-related causation analysis based on BN simulation: The developed BN is finally simulated to investigate the human-related hazardous events involved in the suffocation accident, which is beneficial in improving the safety management for operation on board the ships.

# 2.2. Development of CN 

In the present study, the CN is developed by the human-related hazardous events identification and causal logic analysis among these events. The principle of ETA is utilized to identify the human-related hazardous events involved in the accident report. As a result, these events are considered as the nodes within the CN , and the causal logic among the events would be regarded as the directed edges.

### 2.2.1. Human-Related Hazardous Event Identification

According to the principle of ETA, the suffocation accident report was interpreted in detail to identify the human-related hazardous events contributing to the occurrence of the objective accident. Finally, a total of 40 hazardous events were identified, all of which are presented in Table 2.

Table 2. Hazardous events identified from the accident report.


Table 2. Cont.


# 2.2.2. Topology for the CN 

The logic relationships among various human-related hazardous events listed in Table 2 were used to develop a CN. For this purpose, five experts were employed in this study to determine the logic relationships, whose basic information is summarized in Table 3. To conduct the expert elicitation, a safety meeting was held, during which the accident report was introduced. The logic relationships are summarized in Figure 2.

Table 3. Basic information for the experts employed in the present study.


Table 3. Cont.


![img-1.jpeg](img-1.jpeg)

Figure 2. CN obtained from the accident report.

# 2.3. Calculation for the Node Criticality 

### 2.3.1. Basic Criticality Calculation for Nodes within CN

The topology of the CN can be described by the parameters associated with degree and weight. It is noticeable that the weight-related parameter is equal to 1 in the case of a single accident report. To implement the topological description for the developed directed CN , the network is represented as:

$$
G=(V, E)
$$

where $V=\left\{v_{1}, v_{2}, \ldots, v_{N}\right\}$ and $E=\left\{e_{1}, e_{2}, \ldots, e_{M}\right\}$ represent the set of nodes and the set of edges, respectively. In the present study, $v_{i}$ indicates the identified hazardous event, while $e_{i}$ denotes the logic relationship. Then, an adjacency matrix A is employed to quantitatively describe $G=(V, E)$, and the elements in the adjacency matrix are determined by:

$$
A_{i j}=\left\{\begin{array}{c}
a_{i j} \cdot w_{i j} i \rightarrow j \\
0 \text { else }
\end{array}\right.
$$

where $a_{i j}(i, j \in V)$ is equal to 1 when $v_{j}$ is triggered by $v_{i}$, and is zero otherwise. The weight between the node $v_{i}$ and the node $v_{j}$ is expressed by $w_{i j}$. The meaning of weight is to make the connection strength between the nodes are quantified. The weight is divided into two kinds: in-weight and out-weight. In general, the characteristics of the CN are obtained by node strength and cross-weight and can be determined by the correlation calculation of the weight.

$$
\begin{aligned}
& T_{\mathrm{w}}(i)=S_{\mathrm{in}}(i)+S_{\mathrm{out}}(i)=\sum_{j \in V} w_{j i}+\sum_{j \in V} w_{i j} \\
& C_{\mathrm{w}}(i)=S_{\mathrm{in}}(i) \cdot S_{\mathrm{out}}(i)=\sum_{j \in V} w_{j i} \cdot \sum_{j \in V} w_{i j}
\end{aligned}
$$

Another important parameter for a typical, directed CN refers to the degree of node, which is defined as the sum of nodes connecting or being connected to the objective node. In the present study, the degree of the objective node is denoted by $d(i)$. Similarly, the degree is also divided as in-degree and out-degree, which can be determined, respectively, by:

$$
\begin{aligned}
d_{\text {in }}(i) & =\sum_{j \in V} a_{j i} \\
d_{\text {out }}(i) & =\sum_{j \in V} a_{i j}
\end{aligned}
$$

According to the equations expressed in (5) and (6), the in-degree of a node is the total number of nodes affecting the objective node, and the out-degree of a node refers to the total number of nodes affected by the objective node. Then, the total degree of the objective node can be obtained by:

$$
T_{\mathrm{d}}(i)=d_{\text {in }}(i)+d_{\text {out }}(i)=\sum_{j \in V} a_{j i}+\sum_{j \in V} a_{i j}
$$

The total degree is generally used to evaluate the activeness of nodes within a network according to graph theory; however, the difference between nodes characterized by the same total degree cannot be distinguished from the perspective of activeness. Therefore, the concept of the cross-degree is introduced in this study, which is mainly applied to distinguish nodes with the same total degree:

$$
C_{\mathrm{d}}(i)=d_{\text {in }}(i) \cdot d_{\text {out }}(i)=\sum_{j \in V} a_{j i} \cdot \sum_{j \in V} a_{i j}
$$

In the present study, node criticality was determined by the improved K-shell decomposition algorithm, which is implemented with the precondition of calculating the basic criticality as the input for the improved K-shell decomposition algorithm. To calculate the values of basic criticality for the identified nodes, a group of control equations associated with degree and weight are proposed here, which are expressed as:

$$
\begin{gathered}
f_{1}\left(w_{j i}, w_{i j}\right)=\left|\sum_{j \in V} w_{j i}-\sum_{j \in V} w_{i j}\right| \\
f_{2}\left[d_{\text {in }}(i), d_{\text {out }}(i)\right]=\left|d_{\text {in }}(i)-d_{\text {out }}(i)\right| \\
f_{3}\left(w_{j i}, w_{i j}\right)=\sum_{j \in V} w_{j i}+\sum_{j \in V} w_{i j} \\
f_{4}\left[d_{\text {in }}(i), d_{\text {out }}(i)\right]=d_{\text {in }}(i)+d_{\text {out }}(i)
\end{gathered}
$$

The nodes are generally characterized as critical in case of being valued by larger $f_{3}$ and $f_{4}$, and by smaller $f_{1}$ and $f_{4}$. However, the ideal values of $f_{1}$ and $f_{4}$ cannot be obtained simultaneously. Therefore, it is essential to search for a balance between $f_{1}$ and $f_{4}$. For this purpose, two balance coefficients are defined as [27]:

$$
\begin{aligned}
B_{\mathrm{d}}(i) & =\left[1-\left(\frac{d_{\text {in }}(i)}{d_{\text {in }}(i)+d_{\text {out }}(i)}-0.5\right)^{2}\right] \\
B_{\mathrm{w}}(i) & =\left[1-\left(\frac{\sum_{j \in V} w_{i j}}{\sum_{j \in V} w_{i j}+\sum_{j \in V} w_{j i}}-0.5\right)^{2}\right]
\end{aligned}
$$

where $B_{d}(i)$ is the degree balance coefficient, and $B_{\mathrm{w}}(i)$ is the weight balance coefficient. When the control Equation (10) and cross-strength of the node is considered synthetically, the weight balance index is defined as:

$$
\Psi_{\mathrm{w}}(i)=B_{\mathrm{w}}(i) \cdot\left[T_{\mathrm{w}}(i)+C_{\mathrm{w}}(i)\right]
$$

The degree balance index is similar to the weight balancing index, which can be obtained with the cross-degree and control Equation (11):

$$
\Psi_{\mathrm{d}}(i)=B_{\mathrm{d}}(i) \cdot\left[T_{\mathrm{d}}(i)+C_{\mathrm{d}}(i)\right]
$$

As a result, the basic criticality of node can be determined by:

$$
\Psi_{\mathrm{B}}(i)=\Psi_{\mathrm{d}}(i) \cdot \Psi_{\mathrm{w}}(i)
$$

# 2.3.2. Node Criticality Determination by Improved K-Shell Decomposition Algorithm 

In the present study, the aforementioned basic criticality would be considered as the input of K-shell decomposition algorithm to determine the node criticality. The K-shell decomposition algorithm is widely applied to analyze the node criticality based on the topology of the CN [44]. Generally, the basic K-shell decomposition algorithm is applicable for undirected unweighted networks, and aims to decompose the node set into subsets based on node centrality [45]. Meanwhile, a layer sequence number $\xi_{\mathrm{K}}$ is assigned to each node according to its centrality value in the network and used to assess the criticality of objective nodes [27]. Nodes assigned larger $\xi_{\mathrm{K}}$ values are closer to the center of the network, and nodes assigned smaller $\xi_{\mathrm{K}}$ values tend to be at the periphery of the network. The basic K-shell decomposition algorithm can be improved to be applicable for the directed, weighted CN .

In the present study, the obtained basic criticality of the objective node is considered as the decomposition function, which is then embedded into K-shell decomposition algorithm, as a result, the layer sequence number can be determined as:

$$
\Psi_{\mathrm{K}}(i)=\mathrm{K}\left[\Psi_{\mathrm{B}}(i)\right]
$$

According to the principle of the K-shell decomposition algorithm, $\Psi_{\mathrm{K}}(i)$ is the criticality value of the layer containing the $i$ th node, and the layer sequence number is denoted by $\xi_{\mathrm{K}}$. All the nodes at the same layer are regarded as a set of $G_{\xi_{\mathrm{K}}}=($ node $i \mid \xi_{\mathrm{K}}(i)=\xi_{\mathrm{K}})$. To distinguish the nodes sharing the same layer sequence number, in the present study, an iteration factor is introduced into the traditional K-shell decomposition algorithm. As a result, the improved K-shell decomposition algorithm can be obtained and is expressed as:

$$
\Psi_{\mathrm{K} i}(i)=\Psi_{\mathrm{K}}(i)+\Gamma_{\xi_{\mathrm{K}}}(i)
$$

where $\Psi_{\mathrm{K} i}(i)$ is the criticality of the objective node, and the iteration factor is represented by $\Gamma_{\xi_{\mathrm{K}}}(i)$, which can be obtained by [27]:

$$
\Gamma_{\xi_{\mathrm{K}}}(i)=\left\{\begin{array}{c}
\frac{\left(\sigma_{i}-1\right)}{\gamma} \cdot\left(\Psi_{\mathrm{K}+1}-\Psi_{\mathrm{K}}\right) \text { node } i \in G_{\xi_{\mathrm{K}}}, \xi_{\mathrm{K}} \text { is not the outermost layer } \\
\frac{\left(\sigma_{i}-1\right)}{\gamma} \cdot\left(\Psi_{\mathrm{K}}-\Psi_{\mathrm{K}-1}\right) \text { node } i \in G_{\xi_{\mathrm{K}}}, \xi_{\mathrm{K}} \text { is the outmost layer }
\end{array}\right.
$$

where $\gamma$ is the number of nodes contained in layer $\xi_{\mathrm{K}}(i)$, and $\sigma_{i}$ is the order in which node $v_{i}$ is assigned to layer $\xi_{\mathrm{K}}(i)$.

According to the improved K-shell decomposition algorithm represented by Equations (9)-(20), the algorithm is coded and implemented with the application of MATLAB. Then, the criticality for nodes within the CN can be obtained, and the results of all the nodes in the CN are summarized in Table 4. It is noticeable that the criticality value for the node coded by "N_19" (personnel suffocation) is marked as 1 . Moreover, in this study, the "N_19" node is regarded as the top event in the BN in the following section.

Table 4. Criticality values for nodes.


# 2.4. Bayesian Inference 

### 2.4.1. Development of Topology for BN

It is difficult to transfer the CN directly into BN due to the complex logic relationships in the CN. Therefore, in this study, the HFACS was introduced to connect the CN and the BN. In detail, the human-related hazardous events involved in the CN were categorized under the framework of HFACS in the aspects of unsafe acts, precondition for unsafe acts, unsafe supervision and organizational influences. As a result, in the developed BN, the human-related hazardous events are considered as the root nodes, the four aspects of HFACS serve as the middle nodes and the accident is the top node. It is notable that not all the nodes within the CN can be transferred into the BN as the root nodes.

To develop a BN, the human-related hazardous events listed in Table 2 were first categorized according to the principle of HFACS model. Under the framework of HFACS, all the human-related factors contributing to the accident are summarized in the aspects of unsafe acts, precondition for unsafe acts, unsafe supervision and organization influence. In the present study, those nodes characterized by the least 10 importance are deleted for the establishment of the BN, and the results are summarized in Table 5.

Table 5. HFACS framework for the identified hazardous events.


According to the category illustrated in Table 5, the "N_19" node (personnel suffocation) is regarded as the top node in the BN; the four aspects of HFACS are considered as the intermediate nodes; and the nodes contributing to every aspect of the HFACS are set as the root nodes. As a result, the basic framework of the BN is developed as shown in Figure 3.

![img-2.jpeg](img-2.jpeg)

Figure 3. BN developed for the human-related factors analysis.
2.4.2. Determination of Probability Distribution for Nodes within BN Based on Criticality

The basic principle for Bayesian inference is presented in [23]. In the present study, all the nodes within the BN are considered as simulation nodes rather than discrete nodes. Therefore, the traditional conditional probability tables for the middle nodes are presented as the continuous probability distribution functions. Additionally, the probability distribution of all the nodes needed for the BN simulation in this study are determined with reference to [42]. It is assumed that the probability distribution of all the nodes, including the root nodes, intermediate nodes and top-level nodes, obeys the normal distribution. For the root nodes, the mean value of probability distribution can be calculated by normalizing the maximum value of the criticality for the root nodes, which is expressed as:

$$
P_{\mathrm{Ki}}(i)=\frac{\Psi_{\mathrm{Ki}}(i)}{\operatorname{Max}\left(\Psi_{\mathrm{Ki}}\right)}
$$

where $\Psi_{\mathrm{Ki}}(i)$ denotes the node criticality, and $\Psi_{\mathrm{Ki}}(i)$ can be valued according to the algorithms proposed in Section 2.3. For the intermediate nodes within the BN, the mean values of probability distribution can be obtained on the basis of probability distribution of the parent nodes contributing to the objective intermediate node, which is expressed as:

$$
\chi(j)=\sum \omega_{\mathrm{Ki}}(i) \cdot \Lambda(i)
$$

where $\Lambda(i)$ denotes the sampling value of parent nodes directing to the $j$ th intermediate node. In the present study, $\Lambda(i)$ refers to the mean value of the probability distribution for the $i$ th node. The weight of $i$ th root node is represented by $\omega_{\mathrm{Ki}}(i)$ that can be calculated by:

$$
\omega_{\mathrm{Ki}}(i)=\frac{\Psi_{\mathrm{Ki}}(i)}{\sum \Psi_{\mathrm{Ki}}}
$$

Similarly, the mean value of probability distribution for the top nodes can be calculated by the following equation:

$$
\Omega(t)=\sum \lambda_{\mathrm{Ki}}(j) \cdot \chi(j)
$$

where $\lambda_{\mathrm{Ki}}(j)$ denotes the weight of the intermediate node, and can be calculated by the following equation:

$$
\omega_{\mathrm{Ki}}(j)=\sum_{i \in J} \frac{\Psi_{\mathrm{Ki}}(i)}{\sum_{i \in R} \Psi_{\mathrm{Ki}}(i)}
$$

(1) Determination of probability distribution for root nodes:

According to the methodology proposed here, the prior probability for root nodes can be determined on the basis of the node criticality. In the present study, the prior

probability distribution of the root nodes is assumed to be normal distribution, which can be expressed as:

$$
F_{i} \sim N\left(P_{i}, \sigma\right)
$$

where $F_{i}$ is the prior probability distribution of the $i$ th root node, and $P_{i}$ denotes the mean value of the probability distribution, which is valued as the node criticality presented in Table 4. The variance of normal distribution is donated by $\sigma$, which is determined as onethird of the mean value according to the principle of $3 \sigma$ (standard deviation). According to Equation (26), the prior probability distribution for the root nodes in the BN can be obtained, and the results are summarized in Table 6.

Table 6. The criticality and probability distribution for root nodes.


(2) Determination of probability distribution for intermediate nodes and the top node:

The conditional probability distribution for the child nodes (intermediate nodes and the top node) in the developed BN can be determined based on the algorithm proposed in this section. Specifically, the probability distribution of the root nodes listed in Table 6 is set as the input for Equations (21)-(25). Then, the probability distribution for the four intermediate nodes and the top node can be determined, which is the function of the probability distribution of the root nodes, as shown in Table 7. It is notable that the probability distribution expressions presented in Table 7 can be then entered directly into the software of AgenaRisk for the simulation of BN.

Table 7. Probability distribution expression for intermediate nodes and the top node.


## 3. Results and Discussion

### 3.1. Results

### 3.1.1. Topology Analysis of CN

According to the calculation principle for the degree and weight described in Section 2.3, the degree distribution and weight distribution can be discussed according to [44]. In the present study, the weight is set as 1 because the analysis sample is limited to a single accident report; therefore, the topology analysis for the developed CN is limited to the degree distribution. According to [44], the degree of each node in the developed CN can be determined. Following this, the frequencies for the in-degree and out-degree can be plotted, as illustrated in Figure 4.

![img-3.jpeg](img-3.jpeg)

**Figure 4.** Degree distribution for the developed CN. (**a**) Degree distribution of the CN; (**b**) phase diagram of degree distribution.

The phase diagram of Figure 4b is essentially the projection of Figure 4a along the Y–Z axis. Based on the contents of Figure 4, the in-degree and out-degree of most nodes are less than 4, and the number of nodes with d_{in} = 2, *d*_{out} = 2 is found to be larger than other nodes. In addition, some nodes illustrated in Figure 4 are supposed to receive significant attention. For instance, the nodes with large in-degree are characterized by being caused or affected easily, which indicates that these nodes are difficult to control; meanwhile, the nodes with large out-degree are capable of affecting other nodes easily, which shows that these nodes are important in improving the safety level. To distinguish the nodes with different in-degree and out-degree, the degrees for the nodes involved in the CN are then calculated, and the results are illustrated in Figure 5.

### 3.1.2. Belief Propagation Analysis

According to [46], the belief propagation analysis of Bayesian inference usually contains forward-propagation and backward-propagation analysis. The forward-propagation analysis is mainly aimed at investigating the influence of parent nodes on their child nodes, while the backward-propagation analysis focuses on the sensitivity of the parent nodes to their child nodes, which is implemented by updating the probability distribution of the parent nodes by setting their child nodes as "evidence". In the present study, the criticality-based values are utilized to assess the human-related factors involved in the accident, and the higher values of a node, the more important the objective factors. The results presented in Figure 6 are set as the base for comparison, which can be found in Table 8. According to the results of criticality evaluation summarized in Table 4, the nodes with largest criticality value within each category of human-related factor under the framework of HFACS are selected as the given evidence for the backward-propagation analysis. As a result, these nodes coded by "N_13", "N_16", "N_17", "N_18", "N_25", "N_29" and "N_40" were selected as the given evidence in the present study. Then, different risk scenarios are developed.

oped by decreasing the criticality values of these selected nodes by $50 \%$ one by one, and the different scenarios are summarized in Table 8. Subsequently, the various risk scenarios are simulated by the developed BN on the software of AgenaRisk, and the variations in the node of "personnel suffocation" and the four aspects of HFACS are presented in Table 8.
![img-4.jpeg](img-4.jpeg)

Figure 5. Node evaluation from degree.
![img-5.jpeg](img-5.jpeg)

Figure 6. The results of running the BN model.

Table 8. Different scenarios for propagation analysis.


Note: $\downarrow$ indicates the reduction of a certain variable value in the specific scenario compared with the value in the base case.

# 3.1.3. Sensitivity Analysis 

The sensitivity analysis was implemented in the present study to quantify the sensitivity of the identified human-related hazardous events to the personnel suffocation accident using the backward-propagation analysis of the developed BN. During the sensitivity analysis, the top event, which refers to the personnel suffocation, was set as the given evidence, and the developed BN was simulated with AgenaRisk. In the present study, sensitivity nodes were selected according to the node criticality, and the top ten root nodes were considered as the sensitivity nodes for the sensitivity analysis. The mean value of the target node (referring to personnel suffocation) was selected to indicate the summary statistics. Finally, the results of the sensitivity analysis are presented by the tornado graph, which is illustrated in Figure 7. The criticality of the selected nodes is larger than 0.5526, and some nodes share the same criticality, such as "N_16", "N_17" and "N_18". According to the basic principle of the sensitivity analysis, the sensitivity level of the nodes is represented by the length of the blue bars illustrated in Figure 7. The longer the blue bar is, the more sensitive the objective node is, and the nodes characterized by high sensitivity would be paid much attention to improve the safety management system to prevent the similar accidents.
![img-6.jpeg](img-6.jpeg)

Figure 7. Sensitivity analysis for the root nodes.

In the present study, the sensitivity analysis was implemented to investigate the sensitivity of the intermediate nodes which were set as the sensitivity nodes, while the top event was again regarded as the target node. The results are shown in Figure 8 in the form of a tornado graph, which was obtained by simulating the developed BN with the mean value of the top node criticality representing the summary statistics.
![img-7.jpeg](img-7.jpeg)

Figure 8. Sensitivity analysis of the intermediate nodes.

# 3.2. Discussion 

In the aspect of the topology of the CN, according to Figures 4 and 5, it is clear that the node of "N_25" is valued as the maximum in terms of in-degree, which indicates that the risk-prevention measures taken by the operators on site should have been supervised and instructed by many other stakeholders. In addition, the node of "N_13" can be observed as the maximum in terms of out-degree, and it can be reasonably inferred that the supervision of the operators on the site of the shipyard is critical for accident prevention. Moreover, most operators on site in the shipyard are affiliated with subcontractors, which has been identified as a primary risk according to [12]. In addition, it can also be seen that the safety culture, especially during the holiday season, is essential for safety, which is proved by the second largest out-degree of "N-40", which is similar with the study conducted by the authors of [12]. In their study, the lunch effect attenuated the concentration of the operators on-site, and the holiday effect also functioned by a similar principle.

The results of belief propagation analysis summarized in Table 8 can be utilized to assess the sensitivity of the human-related hazardous events for the suffocation accident. Taking the comparison of the base and scenario 1 as an example, the status of UA would decrease from 0.538 to 0.497 in the case of lowering the node criticality of "N_25" by $50 \%$, which would subsequently cause the change of the top event by $2.1 \%$ (from 0.675 to $0.661)$. According to the above-mentioned principle of the improved K-shell decomposition algorithm, the decrease in the node criticality indicates that the corresponding node would be less active in the network. According to the contents in Table 8, the influence of "N_13" on the top event is the most obvious, which would lower the probability of the "personnel suffocation" by $4.0 \%$. Meanwhile, the node of "N_13" is also identified as the most active node in terms of out-degree discussed in Section 3.1.1. Therefore, the performance of the shipyard's supervision of the operators, strictly implementing the safety management system, is essential for safe operation, which was identified as the most important factor in the field of OI (organization influence under the framework of the HFACS). Similar advice was presented in [12] for ensuring a safe work environment. The second most influential nodes coded by "N_16", "N_17" and "N_18" would lower the probability of personnel suffocation by $3.9 \%$, all of which are categorized as US (unsafe supervision). Even though

it is difficult to distinguish these nodes in terms of their influence on personnel suffocation, the correlation between these nodes and the personnel suffocation accident can be observed according to the results summarized in Table 8, which indicates that the superintendents and the officers of the operation department are critical to the supervision procedures on site. The last influential nodes presented in Table 8 were found to be "N_25" and "N_29", both of which are categorized as UA (unsafe acts), which implies the concentration of unsafe acts from operators in controlling and managing human-related risk factors is difficult to improve the safety level.

In the aspect of sensitivity analysis, according to the tornado graph illustrated in Figure 7, the top three sensitive nodes coded by "N_16", "N_17" and "N_18" are associated with the superintendents and officers in the civil marine project affiliated with the shipyard, especially the risks which occur in relation to the supervision by superintendents and officers of the operators run by subcontractors. Actually, the ILO identified the contracting service of subcontractors as one of main hazards in shipyard operations, and supervision for risk-prevention measures should be implemented at regular intervals [6]. It is interesting to find that, even though the three most sensitive nodes share the same criticality, the sensitivity level of $\mathrm{N} \_18$ is slightly lower than that of " $\mathrm{N} \_16$ " and " $\mathrm{N} \_17$ ", which indicates that the identification and prevention of the risks associated with the planned operation on-site are more important than the management for the potential risks associated with the similar operation, although the latter is also important in the safety management system. In addition, the sensitivity of the node coded by "N_13" is ranked behind that of the nodes of "N_16", "N_17" and "N_18", even though the hazardous event denoted by "N_13" (shipyard failed to supervise operators on-site to implement strictly the safety management system) is regarded as being active in the developed CN . It is also noticeable that the absence of risk-prevention measures taken by the operators on-site coded by "N_25" is characterized by high in-degree and low sensitivity level, which indicates that the humanrelated risk management should focus on the causation for "N_25", such as "N16" and "N_17". It can be observed that the unsafe supervision coded by US in Figure 8 is found as the most sensitive node for the personnel suffocation, which implies the well-implemented safety management system is essential for the operation on-site. The similar conclusions were obtained by Fragiadakis et al., who argued that "bad information of subcontractors about safety rules" played a key role in shipyard injury accidents [13]. Therefore, the supervision for the operators from subcontractors is an effective way to maintain safe operations in a shipyard. The sensitivity level of US is followed by UA, which can be interpreted as the initial causation for the personnel suffocation in the unsafe actions of operators on site. However, the unsafe actions of the operators were not identified as the most active or sensitive events in the present study, which indicates that the consequences caused by the unsafe acts of the operators can be eliminated by the supervision or monitoring arrangements which followed. In addition, according to the contents of Figure 8, the organizational influence (coded by OI) is less sensitive than that of unsafe supervision and unsafe acts based on the accident report, and the difference in terms of sensitivity level between US and OI is as high as 3.17 times; therefore, much more attention should be paid to the factors involved in unsafe supervision rather than factors related to organizational influence. Finally, the least sensitive aspect under the HFACS framework is the preconditions for unsafe acts (UP) which is valued as 0.355 , which is followed by the OI with the sensitivity value of 0.487 . The sensitivity difference between UP and OI is not considerable for the case in this study, which indicates that the external environment has little influence on the occurrence of the personnel suffocation accident.

Overall, the following lessons can be obtained from the case study:
(1) The significance of "N_13" (shipyard failed to supervise the operator on site) was identified by the proposed methodology in relation to risk propagation based on the perspective of the CN analysis. Therefore, the effective supervision of the shipyard operators on site may be able to intercept risk propagation, despite the occurrence of unsafe acts.

(2) The human-related hazardous events coded by "N_16", "N_17" and "N_18" were identified as the most sensitive events for the occurrence of the personnel suffocation accident case study, which indicates that the superintendents or managers of the operators were essential for the safety of the operation. Therefore, an important lesson can be learned: superintendents or managers must pay attention to the behaviors of operators on site.
(3) Another important lesson learned from the personnel suffocation case study is that the focus of safety management or causation investigations should emphasize unsafe supervision instead of the traditional perspective, which focuses on the unsafe acts of operators. Unsafe acts are inevitable without well-implemented supervision. The consequences stemming from unsafe acts can be eliminated by well-designed supervision, which was reflected in the first lesson.

# 4. Conclusions 

The present study proposes an innovative methodology to bridge the CN and the BN on the basis of an event tree analysis under the HFACS framework. This methodology quantitatively assesses the human-related hazardous events involved in maritime accidents. For this purpose, a personnel suffocation accident on board a ship was selected as a case study, and the ETA was applied to identify the human-related hazardous events according to the accident report. Then, the logic relationships among the identified hazardous events were mapped into an event tree. As a result, the CN was developed. The improved K-shell decomposition algorithm was subsequently proposed to quantify the criticality of the nodes contained in the developed CN. Meanwhile, the framework of the BN was established under the framework of the HFACS with reference to the results of the criticality evaluation. To implement the Bayesian inference, the criticality of the root nodes was used to determine their prior probability distribution with the assumption of the normal distribution. The conditional probability distribution for other nodes in the BN can be also determined on the basis of the probability distribution of the root nodes. Finally, the developed BN was simulated in AgenaRisk, by which the scenarios were simulated, and the sensitivity analyses were implemented.

The advantages of the proposed methodology are mainly characterized by its elimination of the traditional potential bias. This is due to the expert elicitation and our compensation of the constraints of the ETA, without considering the logic relationships among hazardous events. However, the performance of the proposed methodology can be improved by further study in the near future. For instance, the logic relationships among hazardous events can be described in greater detail by a more effective method to aggregate the expert elicitation rather than the safety meeting which was adapted in the present study. In addition, the performance of the proposed methodology can be verified by the implementation of numerous accident reports associated within the industry in the near future.

Author Contributions: Methodology and original draft, W.Q.; Formal analysis and modelling, H.G.; Investigation, E.H.; Modelling and calculation, W.D.; Data curation and inveistigation, C.L.; Resource, H.C. All authors have read and agreed to the published version of the manuscript.

Funding: This research was funded by National Key Research and Development program of China (grand No. 2019 YFB1600602), the Fundamental Research Funds for the Central Universities (Grand No. 3132022223) and Program of Innovative Talents of Dalian (Grand No. 2021RQ043).

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Not applicable.
Conflicts of Interest: The authors declare no conflict of interest.
