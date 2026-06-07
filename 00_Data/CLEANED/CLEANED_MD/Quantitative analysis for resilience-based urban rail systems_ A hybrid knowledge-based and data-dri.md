# UNIVERSITY OF LEEDS 

This is a repository copy of Quantitative analysis for resilience-based urban rail systems: A hybrid knowledge-based and data-driven approach.

White Rose Research Online URL for this paper:
https://eprints.whiterose.ac.uk/180768/
Version: Accepted Version

## Article:

Yin, J, Ren, X, Liu, R orcid.org/0000-0003-0627-3184 et al. (2 more authors) (2022) Quantitative analysis for resilience-based urban rail systems: A hybrid knowledge-based and data-driven approach. Reliability Engineering and System Safety, 219. 108183. ISSN 0951-8320
https://doi.org/10.1016/j.ress.2021.108183
(c) 2021 Elsevier Ltd. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/.

## Reuse

This article is distributed under the terms of the Creative Commons Attribution-NonCommercial-NoDerivs (CC BY-NC-ND) licence. This licence only allows you to download this work and share it with others as long as you credit the authors, but you can't change the article in any way or use it commercially. More information and the full terms of the licence here: https://creativecommons.org/licenses/

## Takedown

If you consider content in White Rose Research Online to be in breach of UK law, please notify us by emailing eprints@whiterose.ac.uk including the URL of the record and the reason for the withdrawal request.

Yin J., Ren X., Liu R., Tang T., Su S. Quantitative analysis for resilience-based urban rail systems: A hybrid knowledge-based and data-driven approach. Reliability Engineering \& System Safety, 2021.

# Quantitative Analysis for Resilience-based Urban Rail Systems: A Hybrid 

## Knowledge-Based and Data-driven Approach

Jiateng Yin ${ }^{1}$, Xianliang Ren ${ }^{1}$, Ronghui Liu ${ }^{2}$, Tao Tang ${ }^{1}$, and Shuai $\mathrm{Su}^{1 *}$<br>1. State Key Laboratory of Rail Traffic Control and Safety, Beijing Jiaotong University, Beijing, 100044, China<br>2. Institute for Transport Studies, University of Leeds, UK.

November 20, 2021


#### Abstract

The rapid expansions of urban rail networks are faced with the growing number of disruptions caused by the complex rail signaling systems, incorrect driving behaviors, and extreme weather. Since urban rail systems are inherently complex and many of these disruptions are usually uncertain and inevitable, the rail managers have gradually paid more attention to the ability to withstand and quickly recover. Nevertheless, only a small number of recent developments have tried to address the ability of an urban rail system to recover from disruptions while considering the inherent structures. In this work, we propose a hybrid knowledge-based and data-driven approach for quantitative analysis of resilience. The aim is to model the causal relationships to quantify the importance of different perturbations to the overall resilience criteria. A set of key features related to the risk assessment and system resilience are summarized according to the historical data in Beijing Metro. Then, we develop a training procedure based on the structure of BN and historical data. Finally, we embed this hybrid approach into software that is applied to Beijing Metro. The results demonstrate the quantitative relationships between system resilience and different types of events.


Keywords: Resilience; urban rail systems; Bayesian network; quantitative; transportation.

## 1 Introduction

Resilience refers to the capability of a system to adjust its functionality facing disruption (or fault) [1]. In recent years, the concept of resilience has been successfully applied in many engineering fields, such as infrastructure management $[2,3,4]$, disaster prevention $[5,6]$, and transportation systems $[7,8,9]$, in order to assess the ability of system to withstand a major disruption within acceptable degradation parameters and to recover within a reasonable time,

[^0]
[^0]:    *E-mail address: jtyin@bjtu.edu.cn (J. Yin), shuaisu@bjtu.edu.cn (S. Su)

cost and risk levels [10]. Among them are a series of mathematical models developed ( $[9,11]$ ) to quantify and optimize the resilience of a transport network with uncertain disaster events, such as hurricane and fire disasters.

As the urban rail networks become more dense and complex, it is wide recognition that the disruptions in urban rail systems are uncertain and inevitable events [12]. As such, metro managers in recent years have also gradually shifted their attention from prevention of disruptions to ability to withstand and quick recovery from these disruptions, hence the need for quantifying and enhancing the resilience of an urban rail system. The difficulty in characterizing the resilience of an urban rail system can be attributed to the following two reasons.

First, an urban rail system has a complex composition and coupling relationship, which is typically composed of several sub-systems including rail signaling system, track infrastructures, rolling stocks, platform screen doors (PSDs), etc., and each of these sub-systems also includes several subsystems of this own [13, 14]. It is difficult therefore to construct a comprehensive and accurate physical model to quantify the system performance. For example, the signaling system consists of train-borne automatic train operation (ATO), automatic train protection (ATP), automatic train supervision (ATS), and interlocking subsystems which are installed at each station, all these subsystems are closely coupled with each other.

Second, there are a lot of influencing factors that may lead to unexpected events in the management of complex urban rail systems, e.g., the fault of signaling systems, incorrect driving behaviors (from manual driving to ATO system), and extreme weather [15]. For example, the signaling system is one of the core systems to keep the safety of urban rail systems. With the help of the signaling system, the train can calculate the optimal control strategies based on real-time feedback data, involving the speed limits, length of the track circuit, gradients, and running speed. However, the signaling system is also the most vulnerable part of an urban rail system. According to the practical data in Beijing Metro (as shown in Fig. 1), near half of all disruptions are caused by the broken down of signaling systems (or a subsystem from the signaling system), and such disruption can last anything from 2 minutes to over an hour. On December 13, 2019, the broken down of a switch (one of the subsystems of signaling) in Beijing Metro Line 10 at 9 a.m. causes the delays of all the running trains for at least half an hour. Such disruption significantly reduces the service quality and attractiveness of urban rail transportation to the passengers. Another common disruption is caused by incorrect driving by the train driver (or ATO) to lead to situations such that the train's velocity exceeds the speed limit and the emergency braking is triggered. Once the emergency braking is triggered, a series of safety procedures have to be performed, the train must be confirmed to be safe before it can be re-started to operate again. Extreme weathers are another major cause of disruptions to urban rail operations. For example, in case of heavy rains or storms, reduced temporary speed limits are put in place to ensure safe driving conditions, which then lead to delays and in severe cases cancelation of trains.

This paper conducts a quantitative analysis on the resilience of urban rail systems to disruptions, using historic records of disruptions collected by Beijing Metro. These records contain key characteristics of the disruptions (for

![img-0.jpeg](img-0.jpeg)

Figure 1: Distribution of the failure modes on Beijing Metro lines

example, fault type, position, fault recovery time), as well as the possible causes for the disruption (e.g., weather, passenger volume). Such a big historic disruption database provides opportunities to gain in-depth relationships among these key features of disruptions and to identify the influencing factors that afford the metro systems the ability to withstand and quick recovery from disruptions.

Data on the disruptions and faults that occurred in Beijing Metro from 2013 to 2018 are made available to this study, a total of 50,000 records. We formally present the definition of resilience against disruptions in urban rail systems. Then, a hybrid knowledge-based and data-driven approach based on a probability graph model for quantitative analysis of the systematic resilience is proposed; the aim is to model the causal relationships to quantify the importance of different perturbations to the overall resilience criteria. A Bayesian network (BN) is constructed and several structural learning algorithms are developed to improve the prediction accuracy of the BN model. The hybrid approach is implemented into a python-based software platform and applied to the disruption records from Beijing Metro to identify the quantitative relationships between system resilience and different type of events. We find that the training time of BN can be greatly reduced by combining expert knowledge structure and heuristic rules. From our experiments with field data, we also derive some interesting and practically significant conclusions, for example, the most critical components that affect the resilience of a metro system. These findings enable the rail managers to have a better grasp of the weakness and strengths of the metro system against unexpected disruptions.

The rest of this paper is structured as follows. Section 2 reviews relevant literature and a problem description is given in Section 3. In Section 4, we present the proposed model and training algorithms. Then numerical experiments based on Beijing Metro are conducted in Section 5. Finally, Section 6 concludes this paper.

# Literature review 

In this section, we first review and classify the commonly used methodologies in the assessment of system resilience. Then, we review the related literature that applied resilience in the field of transportation systems. Finally, we summarize the unique contribution of our study with respect to existing literature.

### 2.1 General methodologies in assessing system resilience

In this paper, the concept of the resilience of complex systems was first proposed by Holling [16] for ecological systems as the ability to withstand, absorb and recovery from unexpected disturbances. In recent years, as the requirements for the management of integrated and complex systems get higher, resilience has become a critical indicator for evaluating the performance of complex systems in many fields, such as disaster prevention [5], engineering [7, 8], electric power networks [17], ecological [18], and infrastructure systems [19, 20].

The existing methodologies in the assessment of system resilience can be broadly classified into two categories: qualitative approaches and quantitative approaches. The qualitative approaches assess the resilience of the system using practical experiences and expert knowledge. For example, in the field of chemical plants, Shirali et al. [19] proposed a two-step method, i.e., direct observation and interviewing people, that simultaneously considers preventing accidents by anticipation, surviving disturbance by recovery, and handling disruptive events by adaptation. Speranza et al. [18] discussed and identified key indicators of the livelihood resilience to support the policy and decision-makers, based on a three-dimension framework, involving the buffer capacity, self-organization, and capacity for learning. In the context of the critical infrastructure, Labaka et al. [20] presented a holistic resilience framework that combines internal and external resilience-oriented policies and provides collaborative schemes on the nuclear plant with high system resilience.

The quantitative approaches, on the other hand, use numerical analysis and mathematical models to quantify the resilience of a system. Such methods can be quite effective and accurate to measure the interplay among different subsystems and influencing factors in a large and complex system. In recent years, quantitative methodologies for resilience evaluation have generated a lot of research interest [21]. In general, these methodologies can be divided into three types: numerical analysis-based approaches [4, 5, 22, 23], optimization-based approaches [24, 25] and data-based approaches $[27,28,29,30]$.

### 2.1.1 Numerical analysis based method

This type of method employs deterministic or probabilistic performance indicators to compare the resilience metrics of different systems and is done by constructing mathematical models and understanding underlying system behaviors [21]. Zobel et al. [22] proposed a resilience metric by calculating the total system loss during a certain time interval, where the total system loss is regarded as the quality degradation of system service function and is measured by the

triangular area associated with the system service function.
Others adopt probabilistic performance indicators for evaluating system resilience. For example, Chang and Shinozuka [23] introduced a probabilistic approach measuring two elements: (i) loss of performance and (ii) length of recovery. Resilience is defined as the probability of the initial system performance loss after a disruption being less than the maximum acceptable performance loss and the time to full recovery being less than the maximum acceptable disruption time. Ouyang et al. [4] addressed the urban infrastructure resilience under the situation of multiple hazards, where the occurrence rate of each hazard is correlated with each other. The system performance curve was generated from the perspective of resistant capacity, absorptive capacity, and restorative capacity.

# 2.1.2 Optimization based method 

Optimization based method employs mathematical formulations to examine the influence of system structures to system resilience and to identify the best system structure.

Jin et al. [24] developed a two-stage stochastic programming model to analyze the resilience of a metropolitan public transportation network (involving metros and buses). The authors defined network resilience as the fraction of travel demand that can be satisfied by the disrupted network after the occurrence of a disruptive event. The proposed mathematical model generates the best bus network layout that optimizes the system resilience. Li and Zhao [25] proposed a mathematical model for analyzing supply chain resilience. The model objective function was defined based on resilience cells with self-adaptive and self-recovery abilities. Numerical experiments analyze the relationship between risk influences and system resilience. Liu et al. [26] proposed a hierarchical framework for identifying resilience enhancement strategies (RES) of interdependent critical infrastructures. A bi-objective optimization model was constructed in order to minimize the RES cost and maximize the system resilience.

### 2.1.3 Data-driven method

Data-driven method uses simulation or historical system data to evaluate the resilience of a complex system. Carvalho et al. [27] applied discrete event simulation to assess the resilience of a supply chain for supporting the decisionmaking process. In order to improve the system resilience, the model simulates the system behaviors under normal, redundancy, and flexible scenarios. Sun et al. [28] used an agent-based simulation method to examine the resilience of road networks under earthquake-damages, where each kind of repair approach was represented by an agent in the simulation framework.

For complex systems, however, it is almost impossible to accurately simulate every subsystem, leading to the deviation of resilience assessment. Meanwhile, due to the development of cyber-system in recent years, we notice that more and more accurate and precise data can be collected, resulting in some resilience research shifting to a historical data-based approach. Xu et al. [29] demonstrated the effectiveness to use the historical data sets to

mine the relationship between inherent characteristics and system resilience. They constructed an intelligent business analytic system with the aid of data mining and machine learning techniques, which can assist the operational team for enterprise resilience enhancement. Zhang and Huang [30] collected historical data from natural disasters in 207 different countries throughout the world. From which, they defined 6 primary indices and 38 secondary influencing factors, and employed min-max standardization to process the data. The resilience variation of different countries was analyzed and suggestions to enhanced resilience were also proposed.

Among the data-driven methods, BN is regarded as a highly effective tool for the quantifying of system resilience, due to its superior ability of computing the posterior probability distributions of uncertain variables, for complex systems with interconnected components [2]. Recently, BNs have been successfully deployed in the resilience evaluation of a variety of engineering applications, such as inland waterway ports [2], supplier evaluation and selection [31], chemical process systems [32], sulfuric acid manufacturer [33], deep-water port systems [34] and mechanical structures [35]. For example, Hosseini and Barker [2] proposed a novel BN model to quantify the resilience of critical infrastructure systems, in which the resilience capacity is associated with three key components, i.e., absorptive capacity, adaptive capacity and restorative capacity. Case studies on inland water ports were conducted to test the validity of the constructed BN model. More recently, a multi-layer BN model was developed in [36], which aims to evaluate the impact of COVID-19 pandemic on the supply chains, in the view of system resilience and viability. For better understanding of system resilience with BN models, we can refer to [21, 37], which give a comprehensive review of BN models for the resilience quantification with applications in supply chains.

# 2.2 Literature related to the transportation field 

As a popular and significant tool, resilience is also widely applied to the field of transportation systems, while most existing studies focus on numerical analysis-based or optimization-based methods [7, 9, 38, 39, 40, 41, 42]. Henry et al. [7] proposed time-dependent resilience metrics and also gave a numerical formula based on the system's delivery function to quantify the road network resilience. In railway transportation, Adjetey-Bahun et al. [38] proposed a simulation-based model for quantifying resilience by quantifying passenger delay and passenger load as resilience indicators. The author defines the numerical method to measure the resilience indicators by characterizing and simulating the components and their interdependencies. In the transportation of the airport, Janic [39] proposed a numerical definition of airport resilience as the airport's self-exhausted weight on the condition of large-scale disruption events. Through the numerical definition of self-exhausted weight, the method can quantify the airport resilience to estimate the cost of the disruption event. In order to evaluate the long-term resilience of road transportation systems, Tang et al. developed a hierarchical BN with the data from multi-sources for the sustainable development of large cities in China. Meanwhile, some other researchers have focused on optimization models to improve system resilience. For example, in order to maximize the resilience of a road-rail network against unexpected disruptions, Faturechi and

Miller-Hooks [9] developed a three-stage stochastic programming model to optimize the road-rail network design. The objective function was defined as the average travel time between different nodes in the road-rail network in case of disruptions.

Different from road transportation, where the system resilience is usually quantified through traffic conditions (e.g., travel time and road congestion), railway transportation system is actually a kind of public transportation mode that offers large capacity and high punctuality to passengers. To this end, resilience in railway systems typically refers to the ability to provide disrupted services and quick recovery from disputed events, to provide efficient services to passengers [8]. Christopher and Nikola [40] developed a railway network vulnerability model to assess the vulnerability of railway networks, and the aim is to find the most critical combination of links that cause the most adverse consequences to passengers and trains. Using a mixed-integer linear programming formulation and column-and-row generation methodologies, the framework is applied to a real-world case of a Dutch railway. In the field of freight transportation, Khaled et al. [41] proposed an iterative heuristic algorithm for making up and routing trains in a disruption event to minimize the total cost. The system resilience is measured by the relative criticality level of a link or yard and is used to reduce the total cost in a disruption event. Recently, Tang et al. [11] constructed a linear programming optimization model to investigate the effects of bus-bridging services for enhancing the resilience of urban rail systems.

Table 1: Summary of relevant studies on system resilience


# 2.3 Contribution of this study 

In summary, resilience is a very hot research topic in recent years, and several kinds of methodologies have been developed to assess the resilience of systems in different areas. Nevertheless, However, the literature on resilience in railway systems is quite limited compared to other fields, and most studies in railway focus on the optimization of railway network topology or simulation approach to enhance network resilience. To our best knowledge, there is little research that adopts real-world data to qualitatively assess the resilience of the urban rail system.

In this study, we focus on the quantitative analysis of resilience in the operation of urban rail systems, with the aid of the BN model and historical data in the Beijing metro. It is worth noting that, even though BN models have been applied in resilience analysis in existing literature (e.g., $[36,42]$ ), our study differs from existing literature that: 1) our study considers the resilience analysis of urban rail systems, which is actually different from general transport systems $[8,40] ; 2)$ we customize three methods for constructing BN models according to the unique characteristics of urban rail systems, which enable to analyze the in-depth relationships among different factors that affect the system resilience of urban rail systems. Table 1 lists the detailed characteristics of some closely related works to show the contributions of this study. The usefulness of our study are two-fold: First, our developed model can help rail managers to identify the weakness of the whole system against unexpected disruptions induced by adverse failure events and then enhance the system resilience with proper improvement; second, our model can also be used to predict the time-duration of disruptions in urban rail systems, which can be very beneficial for the real-time decisions of train rescheduling in case of disruptions.

## 3 Problem description

### 3.1 Description of field data in Beijing Metro network

The network of Beijing Metro contains 23 operating lines and 405 stations. On average, the network carries more than 10 million trips a day. As one of the largest and busiest rail transit systems, unexpected events or disruptions happen almost daily. Even a small event can cause significant delays on the network and significant economic loss to the operators and the passengers. Understanding the causality between system failures and resilience is one of the top priorities for Beijing Metro.

In this study, we have gathered field data that record all the unexpected events in the Beijing Metro network from 2013 to 2018. More than 50,000 event records have been collected during this period. The data are recorded and saved in text format. A typical event record is illustrated as follows:
"In morning peak hour (8:35 a.m.), October 23, 2015 (weather: snow and fog), the signal device of line 2 failed. Train running intervals were increased. The fault was recovered in about 10 minutes."

From the data records, we extracted six types of information for each event; they are: (i) event start time, (ii)

weather condition, (iii)line condition, (iv) failure mode, (v) influence of the event and (vi) duration time of the event. More details of the element in these six types are list in Appendix I. This information are then translated into numerical representations, and we use a formal data structure to represent the collected data sets. More specifically, we denote $\mathcal{N}$ as a set of events, which is indexed by event $e_{i} \in \mathcal{N}$. Each event record $e$ is defined by

$$
\begin{gathered}
\mathbf{e}=\left[\mathbf{f}_{\mathbf{1}}, \mathbf{f}_{\mathbf{2}}, \ldots, \mathbf{f}_{\mathbf{n}}, \mathbf{v}_{\mathbf{1}}, \mathbf{v}_{\mathbf{2}}, \cdots, \mathbf{v}_{\mathbf{m}}, \mathbf{d}\right] \\
f_{1}, f_{2}, \ldots, f_{n} \in\{0,1\}, n=21 \\
v_{1}, v_{2}, \ldots, v_{m} \in\{0,1\}, m=16 \\
d \in R^{+}
\end{gathered}
$$

where $f_{1}, \cdots, f_{n}, v_{1}, \cdots, v_{m}$, are binary values that indicate if the corresponding text exists in the event record. According to our collected data, there are 21 elements in the vector of $f$, covering the time, weather, line condition, and failure modes. It is worth noting that the first element $f_{1}=1$ if the event occurs in peak hours ( $7: 30$ a.m. to 9:00 a.m., 17:30 p.m. to 19:30 p.m.); otherwise, $f_{1}=0$. The definition is motivated by the fact that more than half of unexpected failures happen in peak hours (morning peak hour and evening peak hour) according to the practical data, as shown in Fig. 2. The other text information $f$ is transferred in a similar manner. In addition, the vector $v$
![img-1.jpeg](img-1.jpeg)

Figure 2: Number of system failures in Beijing metro during different time periods
represents the index of failure influences of each event $e$, and there are a total of 16 elements in the failure influence vector $v$. Finally, $d$ represents the recovery time (or duration) that the system recovers from event $e$. In Appendix I, we present a full list of these elements in $e$ and describe each element in detail.

Following the above procedure, all text records of the disruption events are translated quantitatively into a table of the event set $\mathcal{N}$. An example with two data records is presented in Table 2. Each row in the table represents one

event $e \in \mathcal{N}$. Each column in $e$ represents the information of this event. By collecting and preprocessing the field data into formal structures, we can define the resilience metric according to the practical requirements of rail managers and then use the historical data to assess the resilience of the metro network in a given time period.

Table 2: Illustration of data representation for event set $\mathcal{N}$


# 3.2 Definition of system resilience 

Resilience has been defined as the capacity of an entity to withstand or recover from one kind of disruptive event[1]. However, this general concept is difficult to evaluate the resilience of complex systems, such as material science and transport systems, since it does not relate the effects of disruptive events to any of the events characteristics [43]. In our study, we employ a multidimensional approach to assess the systematic resilience of an urban rail transit system against uncertain disruptions according to the following definitions.

Definition 1 Given a set of $n$ disruptive events (termed by $\mathcal{N}$ ) that happen from time 0 to time $T$. The overall resilience of a system $\rho_{r}$ against a set of events

$$
\rho_{r}=\frac{\sum_{e \in \mathcal{N}}\left(\int_{0}^{T} R_{x}(e) d t\right)}{n T}
$$

where $R_{x}(e)$ is a resilience function of event $e$.
The definition of resilience in Eq. (2) is derived from existing literature, which focused on the resilience quantification under the situation of multiple hazards, e.g., [4, 21]. In urban rail transit systems, the main focus for both the passengers and the operators is on the recovery time of train delays. According to the specific requirement of Beijing metro operating rules, our study further defines the resilience function $R_{x}$ to an event $e \in \mathcal{N}$ as the ability to efficiently reduce both the magnitude and duration of the deviation from targeted system performance levels, given as follows.

Definition 2 Resilience function $R_{x}(e)$ of event $e$ is defined as

$$
R_{x}(e)=\varphi_{\max }-V(e, \mathcal{N}) * D(e, \mathcal{N})
$$

where $\varphi_{\max }$ is a parameter that represents the system performance under normal conditions, $V(e, \mathcal{N})$ denotes the severity level of each event $e$ in the set of $\mathcal{N}$ and $D(e, \mathcal{N})$ denotes the recovery time of each event $e$ in the set of $\mathcal{N}$.

# 3.2.1 Severity level 

In practice, anyone unexpected event may lead to several different possible consequences, for example, a severe event may lead to trains withdrawal or trains running with larger headway intervals. Likewise, the recorded consequences of each event $e$ can also be caused by more than one factor, thus they are characterized by the failure influence vector, i.e., $\left[v_{1}, \cdots, v_{m}\right]$. In order to quantify the severity of the consequences given the occurrence of each event, the rail managers in Beijing Metro usually define a severity level of each event $e$ using the following equation:

$$
V(e, \mathcal{N})=\left(\sum_{i=1}^{m} v_{i}+\max \left\{\phi\left(v_{1}\right) * v_{1}, \cdots, \phi\left(v_{i}\right) * v_{i}, \cdots \phi\left(v_{m}\right) * v_{m}\right\}\right) * \xi\left(f_{1}\right)
$$

In the above equation, the first term $\sum_{i=1}^{m} v_{i}$ represents the number of types of consequences that are observed in each event $e$. If more than one type of consequence is caused in a single event, the severity level will be enhanced correspondingly.

The second term $\max \left\{\phi\left(v_{1}\right) * v_{1}, \cdots, \phi\left(v_{i}\right) * v_{i}, \cdots \phi\left(v_{m}\right) * v_{m}\right\}$ represents the maximum value of resilience loss factors in each event $e$. Here, the resilience loss factor of each $v_{i}$ is denoted by $\phi\left(v_{i}\right)$, where $i=1, \cdots, m$. In practice, the rail managers define the value of each resilience loss factor according to the influences of $v_{i}$ to the operation of metro systems. For example, in Beijing Metro, a total of 16 failure influences and their corresponding resilience loss factors are depicted in Table 3. The description of the influencing factors $\xi$ presented in Table 3 can be found in Appendix I.

The last term $\xi$ in Eq. (4) represents a penalty ratio function according to the occurring time of each event $e$. If a event $e$ happens at off-peak hours, then we have $f_{1}=0$ and define $\xi\left(f_{1}\right)=0.5$; otherwise, $f_{1}=0$ and $\xi\left(f_{1}\right)=1$. The reason is that there are fewer trains and passengers in the system during off-peak hours and the event can be handled more easily rather than events in peak hours.

### 3.2.2 Discretized recovery time periods

The recovery time of each event $e$ is an important indicator of system resilience. In our study, the recovery of each event $e$ is characterized from the occurring of the event $e$ till the system being recovered to its normal operation state. Here, we also use the measurement rules in Beijing Metro, which define several levels of recovery time of each event. Specifically, we let $D(e, \mathcal{N})=1$ if the system recovers to the normal state after 0 to 5 minutes; let $D(e, \mathcal{N})=2$ if the system recovers to the normal state after 5 to 25 minutes; let $D(e, \mathcal{N})=3$ if the system recovers to the normal state after 25 minutes.

## 4 Hybrid knowledge and data based Bayesain Network

To help understand the underlying system behaviors and quantify the resilience function $R_{x}(e)$ given any unexpected event $e$, in this section, we present our proposed hybrid method encompassing knowledge- and data-based approaches to assess resilience in urban rail transit systems. The method is built in a Bayesian Network framework. As a

Table 3: Failure influence vector and resilience loss factors in Beijing metro


probability graph approach, Bayesian Network (BN) is a powerful tool for transforming the internal relationship of the system [44, 45]. We construct a probability graph-based BN model and propose several model training methods to quantify the relationships in such a high-dimensionality of historical faulty events data as in Beijing Metro. After implementing the structure learning and parameter learning process on the historical data set, we can obtain the conditional probabilities of every nodes in the BN model that are estimated from field data with maximum likelihood.

# 4.1 Evaluation of resilience function with BN model 

As stated in Section 3, each event record $e$ is composed of a series of binary values $f_{1}, f_{2} \cdots, f_{n}$, a series of binary values $v_{1}, v_{2}, \cdots, v_{m}$ and a continuous value $d$. According to Definition 1 and Definition 2, the value of resilience function $R_{x}(e)$ is measured by severity level $V(e, \mathcal{N})$ and discretized recovery time level $D(e, \mathcal{N})$. Thus, we construct a BN model for evaluating the parameter $R_{x}(e), V(e, \mathcal{N})$ and $D(e, \mathcal{N})$.

Our constructed BN model is a directed acyclic graph (DAG) $G=(N, A)$, in which each edge corresponds to a conditional dependent and each node corresponds to a unique random variable [46]. In our model, nodes $N$ represents the set of failure influencing factors, and the factors include weather, failure mode, influence mode, severity level $V(e, \mathcal{N})$ and discretized recovery time $D(e, \mathcal{N}) . A=\{(i, j) \mid i, j \in N\}$ is the set of the directed arcs, which represents the conditional dependency between failure influence factors $i$ and $j$, where $i, j \in N$. For description convenience, let $X=\left\{X_{1}, X_{2}, \cdots, X_{V}, X_{D}, X_{R}\right\}$ be the vector of variables in the BN model, where each variable $X_{i}(i \in N)$ corresponds to the value of node $i$ in BN model. Specifically, notice that $X_{V}$ and $X_{D}$ are the values associated with $V(e, \mathcal{N})$ and $D(e, \mathcal{N})$, while the other values $X_{1}, X_{2}, \cdots$ are correspondingly associated with the elements in $f_{1}, f_{2} \cdots, f_{n}$ and $v_{1}, v_{2}, \cdots, v_{m}$. In other words, each value from the input data record represents one node in the BN model. According to the conditional probability theory, the joint probability of $P\left(X_{1}, X_{2}, \cdots, X_{n}\right)$ can be denoted as follow:

$$
P\left(X_{1}, X_{2}, \cdots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid X_{1}, X_{2}, \cdots, X_{i-1}\right)
$$

Based on the above equation, we can get the joint probability of $X$, which is given by

$$
\begin{aligned}
P\left(X_{1}, X_{2}, \cdots, X_{D}, X_{V}, X_{R}\right)= & P\left(X_{R} \mid X_{1}, \cdots, X_{D}, X_{V}\right) P\left(X_{V} \mid X_{1}, \cdots, X_{D}\right) \\
& P\left(X_{D} \mid X_{1}, \cdots, X_{n}\right) \prod_{i=1}^{n} P\left(X_{i} \mid X_{1}, X_{2}, \cdots, X_{i-1}\right)
\end{aligned}
$$

where $P\left(X_{1}, X_{2}, \cdots, X_{D}, X_{V}, X_{R}\right)$ represents the joint probability $P$ of the constructed network by data set $\mathcal{N}$. According to the conditional independent relationship of BN model [44], Eq. (5) can be further simplified via computing the probability of each node by its parents, i.e.,

$$
P\left(X_{1}, X_{2}, \cdots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid X_{p a(i)}\right)
$$

where $p a(i)$ indicates the parent nodes of $X_{i}$.

According to the above descriptions of BN model given a historical data set $\mathcal{N}$, the posterior probability $P\left(X_{D} \mid e\right)$ and $P\left(X_{V} \mid e\right)$ of data sample $e \in \mathcal{N}$ can be denoted as follow:

$$
\begin{aligned}
& P\left(X_{D} \mid e\right)=\frac{\sum_{X_{R}} \sum_{X_{V}} P_{e}(G, \mathcal{N})}{P(e)} \\
& P\left(X_{V} \mid e\right)=\frac{\sum_{X_{R}} \sum_{X_{D}} P_{e}(G, \mathcal{N})}{P(e)}
\end{aligned}
$$

where

$$
P_{e}(G, \mathcal{N})=P_{e}\left(X_{D} \mid X_{p a(D)}\right) P_{e}\left(X_{V} \mid X_{p a(V)}\right) P_{e}\left(X_{R} \mid X_{p a(R)}\right) \prod_{i=1}^{n} P_{e}\left(X_{i} \mid X_{p a_{(i)}}\right)
$$

In Eq. (10), $P_{e}\left(X_{i} \mid X_{p a(i)}\right)$ represents the conditional probability of node $X_{i}$ when data sample $e$ is observed.
When constructing the BN model, one of the most important and challenging tasks is a structured learning method, in order to learn the connectivity relationships (i.e., conditional dependency) between any two nodes. In other words, for each node $X_{i}$, we need to find its parents $X_{p a(i)}$ according to the collected data set $\mathcal{N}$. Only then can we compute the conditional probability for evaluating $V(e, \mathcal{N})$ and $D(e, \mathcal{N})$ by maximum likelihood estimation. In the rest of this section, we propose three different structural learning methods: (a) a local search-based approach; (b) a knowledge-based approach; and (c) a hybrid approach, to optimize the structure of BN model.

# 4.2 Constructing BN model by local search algorithm 

The optimal structure of BN model can be acquired by using some optimization algorithms. Nevertheless, optimizing the BN structure is actually an NP-hard problem due to the need of enumerating each pair of nodes. There are $2^{n \times(n-1) / 2}$ possibilities for a graph with $n$ nodes. For example, consider a graph of 6 nodes (i.e., $n=6$ ) and the resulted BN structure has a total of $1,073,741,824$ possibilities. Instead, heuristic search algorithms can be used for learning the structure of the BN model.

In our study, we propose a heuristic structural learning method based on local search algorithm. The local search algorithm is a standard heuristic method for solving complex optimization problems. Local search algorithm starts with an initial feasible solution as a candidate solution, and then iteratively improves the candidate solution by searching its neighbors until progress halts. The search is guided by a cost function related to the task (e.g., the number of violated constraints) by evaluating each solution in the neighbor of the candidate solution. In our problem, the aim of BN structural learning method is to find the optimal graph $G^{*}$ given a set of training data samples $\mathcal{N}$, which is given by

$$
G^{*}=\underset{G \in G_{n}}{\operatorname{argmax}} g(G: \mathcal{N})
$$

In Eq. (11), the objective function $g(G: \mathcal{N})$ is defined as a measure of fitness between the graph $G$ and the data set $\mathcal{N}$, and is computed as the posterior probability distribution conditioned to the available data $\mathcal{N}$. Specifically, we employ K2 scoring algorithm, the most famous score-based algorithm in Bayesian Network, as the objective function

of local search algorithm. K2 algorithm is a local greedy search algorithm. The basic idea is as follows: there is no parent node at each starting point; then by continuously adding parent nodes to the nodes to improve the score of the local structure. When adding the parent node alone can no longer improve the score, stop adding the parent node. The K2 algorithm obtains the Bayesian structure by maximizing the following objective function that is given as follow:

$$
g(G: \mathcal{N})=p(G) \prod_{i=1}^{n} \prod_{j=1}^{q_{i}} \frac{\left(r_{i}-1\right)!}{\left(N_{i j}+r_{i}-1\right)!} \prod_{k=1}^{r_{i}} N_{i j k}!
$$

where $p(G)$ represents the prior probability of the $D A G_{G}, r_{i}$ the number of the possible value of each node $X_{i}, N_{i j k}$ the number of cases in $\mathcal{N}$ in which the node $X_{i}$ is instantiated with its $k^{t h}$ value, and the parents of $X_{i}$ are instantiated with the $j^{t h}$ instantiation, and $N_{i j}=\sum_{k=1}^{r_{i}} N_{i j k}$.

In implementing the local search algorithm, we start from an initial solution which is generated randomly by connecting a set of nodes in the network and is setting which as the candidate solution. We iteratively use a hill climbing method to find the local neighbors of the candidate solution. If a better solution is found, we use this solution as a new candidate solution and continue the iteration process. The algorithm terminates if there is no local change can yield an improvement in $g(G: \mathcal{N})$ or the number of iterations exceeds a preset limit. The detailed procedure of the local search algorithm for training BN model is given in Algorithm 1.

```
Algorithm 1 Local search for training BN structure
    Initialization. Set iteration index \(x=1, \mathcal{H}^{0}=\) null, \(f^{*}=U\), and go to (2).
    Generate initial feasible solution \(\mathcal{H}^{0}\), and let \(\mathcal{H}^{x-1,0}=\mathcal{H}^{0}\), go to (3).
    Set \(x=x+1\), if \(x\) is less than the maximum iteration number \(M\), go to (4); otherwise, output \(\mathcal{H}^{*}\) and the optimal
    structure \(D A G_{G^{*}}\) based on \(\mathcal{H}^{*}\), stop.
    Generate neighbor solutions \(\mathcal{H}_{N S}^{x}\) by hill climbing strategy, go to (5).
    Evaluate all of the candidate solutions \(\mathcal{H}^{x, c}\) by Eq. (12) and select the best objective value function \(f^{x}\); then, go
    to (6).
    If \(f^{x}>f^{*}\), let \(f^{*}=f^{x}, \mathcal{H}^{*}=\mathcal{H}^{x}, \mathcal{H}^{x, 0}=\mathcal{H}^{x}\), then go to (3).
```

While the local search algorithm can be applied to solve complex problems, it is easy to fall into a local optimal solution, especially for large-scale problems. In the neighbor searching process, the algorithm is usually trapped at a solution that maximizes $g$ locally rather than globally maximizing. In order to improve the quality of the BN structure and enhance the accuracy of the BN model, we employ expert knowledge to construct the BN model.

# 4.3 Constructing BN model by expert knowledge 

In practice, the managers of rail transit systems usually divide the factors, that affect the resilience of urban rail transit systems against disruptions, into different categories, for example, the weather (normal weather v.s., extreme

Table 4: The five categories of the influence factors


weather), fault types, recovery strategies, etc. Then, the resilience of a system can be qualitatively evaluated by summarizing these factors. As some factors (e.g., rain and thunder) are inherently correlated closely with each other, it is straightforward to extract the relationships from the multi-attribution of the system directly. Thus, instead of using local search optimization, we hereby develop a knowledge-based approach for constructing a BN model, which involves three steps: classification of these factors, connection of potentially related nodes and modification of BN structure.

# 4.3.1 Step 1: Classification of the influence factors 

The influence factors, which are similar to the classification of field data in Section 3.1, are classified into a total of five categories according to the experience of rail managers.

They are: (i) line information (CBTC v.s. fixed-block system); (ii) weather information (normal, rain, snow, etc.); (iii) failure types; (iv) influence types; and (v) recovery strategies according to their attributes and characteristics. The factors covered by each category are summarized in Table 4.

### 4.3.2 Step 2: Connection of potentially related nodes

In the BN model, each influencing factor corresponds to a node, and in Step 1, the nodes have been classified into different categories. In order to connect potentially related nodes, we first consider the connection of nodes in the same category. Each time, we pick two nodes in the same category and judge if these two nodes are related to each other. For example, it is straightforward that "rain" and "thunder" in the category "weather" are closely related. Therefore, we connect the nodes "rain" and "thunder" in the BN model. We use this strategy to check all the nodes in each category to obtain the connectivity of each type of node. Second, we consider the connection relationship between

two different categories. We use a qualitative strategy (similar to [47]) to judge if two categories are related to each other. For example, it is widely recognized that extreme weather (e.g., thunder or snow) will potentially cause more equipment faults. By analyzing the relationship between each two categories according to the expert knowledge, we obtain a general BN structure as shown in Fig. 3. Then, we specifically check the nodes in these connected categories (e.g., nodes rain and signal failure) to construct a BN model.
![img-2.jpeg](img-2.jpeg)

Figure 3: The classification framework of resilience influence factors.

# 4.3.3 Step 3: Adjustment of the network structure 

At this step, we adopt a correlation analysis method to make slight modifications to the BN structure from Step 2. Based on the collected data set $\mathcal{N}$, we construct a constraint-based approach to further determine the basic relationship between pairs of nodes.

The constraint-based approach estimates from the data whether certain conditional independencies between the variables hold using statistical or information-theoretic tests [48]. The conditional independence constraints are propagated throughout the graph and the networks that are inconsistent with them are eliminated from further consideration. If for a pair of variables $X$ and $Y$ it is deemed that $(X, Y \mid Z)$ conditioned on some set of variables $Z$, and assuming the network to be reconstructed is faithful, then there should not be an edge between X and Y in the network according to the definition.

In this paper, we use a constraint-based method to determine whether the resilience influencing factors of Table 4 are conditionally independent under data set $\mathcal{N}$, so as to obtain the coupling pair in data set $\mathcal{N}$.

### 4.4 Hybrid knowledge and data based Bayesain Network

Constructing a BN model with expert knowledge is very time-efficient, and the model accuracy is very limited and highly depends on the data structure. We, therefore, propose a hybrid knowledge and data-driven approach by

combining local search algorithm and expert knowledge, in order to improve the prediction accuracy of the BN model; hereafter, this hybrid approach is named the H-BN approach.

As described in Section 4.2, the original K2 algorithm in the data-driven BN assumes a random order of nodes, which however strongly influence the efficiency of the K2 algorithm. For example, if all the parent nodes are ordered before the children nodes, the K2 algorithm will perform outstanding and the final BN structure will be highly accurate; in contrast, an improper order will give poor results, as indicated in [49]. Therefore, the correct order of nodes is critical to the performance of the K2 algorithm. Unfortunately, in most cases, the input-node ordering is unknown. In our study, we employ the domain knowledge of experts to provide a relatively accurate node ordering in advance. In other words, we use expert knowledge to predefine the order of BN nodes for the K2 algorithm, and then we adopt the local search algorithm to further improve the BN structure.
![img-3.jpeg](img-3.jpeg)

Figure 4: The framework of the H-BN approach.

The basic framework in the training of H-BN is given in Fig. 4. There are two main procedures in the training of H-BN.

- First, a sequential node ordering is constructed. Specifically, we denote $E_{C I}$ as the set of coupling pair, following the constraint search method in Section 4.3. Each element $e=(X, Y)$ in $E_{C I}$ is associated with a value of $M I_{e}$. Here, the value of $M I_{e}$ is determined by the empirical knowledge and a large value of $M I_{e}$ represents that $X$ is more likely to be the parent node of child node $Y$. Then, on the basis of the values of $\left\{M I_{e} \mid e \in E_{C I}\right\}$, the nodes in graph $G$ are ordered from beginning to end, from the highest dependency to the lowest one. For example, consider three nodes $X_{1}, X_{2}$ and $X_{3}$. Suppose that the starting node is $X_{1}$, then node $X_{2}$ will be selected if $M I_{e=\left(X_{1}, X_{2}\right)}>M I_{e=\left(X_{1}, X_{3}\right)}$. And finally node ordering $\left\{X_{1}, X_{2}, X_{3}\right\}$ is determined as input to the K2 algorithm.

- Second, the sequential node ordering is adjusted if the accuracy of BN on the testing data set is not satisfying. After we obtain the initial node ordering, we train the BN model through the K2 algorithm and local search optimization, based on the data set $\mathcal{N}$. Then, the prediction accuracy of BN can be evaluated on the testing data set. If the accuracy cannot meet the requirement, we randomly destroy a part of coupling pairs $E_{D I} \subset E_{C I}$ with relatively low value of $M I_{e}$, in order to generate a new sequence of node ordering. The node ordering is again input to the K2 algorithm to train a new BN structure. This process is iterated until the accuracy of BN meets our requirement.


# 4.5 Sensitivity analysis 

Sensitivity analysis determines how different values of an independent variable affect a particular dependent variable under a given set of assumptions. In a BN model, sensitivity analysis is a vital stage to investigate the most influential variables to the target node [42].

In the context of resilience assessment, sensitivity analysis of BN reveals the importance of each variable that contributes to the system resilience. This is regarded as one of the unique advantages of BN compared with traditional resilience assessment methods (such as deterministic indicators and performance-based tools) [50]. This special feature of BN allows decision-makers to conduct in-depth diagnostics of system performance through backward inferencing, with a clear target level of resilience. In this way, the rail manager can analyze the influencing factors related to the system resilience and find the factors that have the most effect on the system resilience.

In this paper, we adopt a sensitivity measure, termed as Sensitivity Index (SI) [51], to assess the variance of the probability distribution of the target node with respect to the changes of variables $X_{i}$ in the BN model. Specifically, consider a target node $X_{T}$ (e.g., $X_{V}, X_{D}, X_{R}$ ) with state $t$ (i.e., a discrete real-value) and variable $X_{i}$, the value of SI is calculated as follows:

$$
S I\left(X_{i}\right)=\left(\max \left\{P\left(X_{T}=t \mid X_{i}=x_{i}\right)\right\}-\min \left\{P\left(X_{T}=t \mid X_{i}=x_{i}\right)\right\}\right)
$$

where $i=1,2, \cdots, n$. The value of SI gives a rank list of the tested variables of the BN model, in which those at the top are considered as the key factors that affect the system resilience.

## 5 Case studies on Beijing Metro

This section presents two sets of numerical experiments based on the collected data of Beijing Metro (a total of 50,000 data samples, each was converted into a quantitative representation of the characteristics of the events and influence factors as described in Section 3.1 earlier.) In the first set of experiments, we respectively use local search algorithm, expert knowledge, and hybrid method to train the BN models - hereafter termed as LS-BN, EK-BN, and H-BN respectively. We compare the performances of these three approaches with a series of model training and testing.

In the second set of experiments, we conduct sensitivity analysis to demonstrate the importance of different factors in system resilience. The experiments are conducted using Python language (version 3.7) on a personal computer with a dual-core CPU (3.30GHz) and 16 GB memory.

### 5.1 Comparison of the three BN model structures

In this section, we separately employ LS-BN, EK-BN, and H-BN models to evaluate the system resilience according to the data in Beijing Metro. We discretize system resilience into a series of levels. According to Definition 2, the system resilience is determined by the level of severity and discretized recovery time, where we set $\varphi_{\max }=7$ (i.e., the system performance under normal conditions). Thus, we can obtain a matrix with two dimensions: severity and discretized recovery time. As described in Section III, the value of severity is discretized into five levels and the value of discretized recovery time in this paper is ranged from 1 to 3 . Thus, the system resilience can be divided into 6 levels according to the value of severity and discretized recovery time. Fig. 5 illustrates the resilience matrix. Then, we can use the data set $\mathcal{N}$ to train LS-BN, EK-BN, and H-BN as follows.
![img-4.jpeg](img-4.jpeg)

Figure 5: Resilience matrix, where the numbers on the graph represent the system resilience and the curves indicate the average resilience level

# 5.1.1 LS-BN 

In this case, we use a hill climbing search algorithm based on the K2 scoring method (i.e., Algorithm 1) to train the LS-BN model with data set $\mathcal{N}$. The first step of the model training is to construct a K2 scoring function $g(G: \mathcal{N})$ according to Eq. (12) by using the training data set. Then, hill climbing search algorithm is employed to find better BN structures based on K2 scoring function. The parameters of the hill climbing algorithm are set as follow: the

maximum number of iterations is set to $1,000,000$ times; the start point and tabu list are set as none. The training process of LS-BN took 15.3 hours.
![img-5.jpeg](img-5.jpeg)

Figure 6: Illustration structure of LS-BN

The LS-BN resulted from the training process is illustrated in Fig. 6, where each color represents one type of failure influencing factor. The yellow nodes represent the weather of the line and the pink nodes represent the failure mode of the operation and equipments. The influence mode and recovery strategy are represented by the green nodes. The light blue nodes represent the basic information: line condition, peak hour, and month. Finally, the orange nodes represent severity, recovery time, and resilience, respectively. The connection between any two nodes indicates that these two nodes are related, and the thickness of the connection indicates the degree of association. For example, we can see from Fig. 6 that there is a strong correlation between "fire condition" (with red dotted border) and "line stopped operating"(with red dotted border). This is consistent with practical experiences that the whole line needs to be shut down in case of potential fire risks.

# 5.1.2 EK-BN 

Here, we use expert knowledge to construct the EK-BN model. We employ the "three-step" method as described in Section 4.3 to develop the structure of the EK-BN model, and in particular, the constraint-based method for determining the relationship in Step 3. The results of constraint-based method, i.e., the coupling relationship of nodes, is shown in Table 5.

Table 5: The coupling relationship of nodes based on constraint search


These coupling pairs by constraint-based method are obtained directly from historical data, which show statistically the strongly related BN nodes. For example, the coupling of "Haze" and "Month" means that the hazy weather is closely related to certain months of a year since haze usually occurs in the winter months. By adjusting the EK-BN model with these coupling pairs, the constructed EK-BN model is presented in Fig. 7.
![img-6.jpeg](img-6.jpeg)

Figure 7: Illustration of the structure of EK-BN

The value of resilience by EK-BN is smaller than that of LS-BN, and the EK-BN model is relatively simpler than LS-BN. Since the connections between any two nodes are actually defined manually, the accuracy of EK-BN depends on the integrity of the domain expert knowledge. Meanwhile, the training time required by EK-BN is only 31 seconds, which is significantly shorter than that of LS-BN.

# 5.1.3 H-BN 

The parameters for training H-BN are set similar to those in LS-BN and EK-BN. In the H-BN model, the starting point is set as a BN model constructed by EK-BN. The training process of H-BN takes about 2.1 hours, and the generated structure of H-BN is presented in Fig. 8. We see a lot of interesting inner-relationships among different nodes, for example, the direct connection between weather "gale" and "interval failure". This is possible due to the fact that strong wind usually blows sundries (e.g., plastic bags) into the section in Beijing subway (up-ground sections), leading to the emergency braking of trains. We also present detailed information (i.e., the conditional probabilities between any two nodes) in Fig. 11 in Appendix II.

![img-7.jpeg](img-7.jpeg)

Figure 8: Illustration structure of H-BN

# 5.1.4 Performance comparison of KNN, LS-BN, EK-BN, and H-BN 

From the above experiments, we can firstly see that training the EK-BN and H-BN models requires much less computation time compared to training the LS-BN model. The average level of the severity, recovery time, and resilience from the LS-BN, EK-BN, and H-BN model are shown in Table 6, where the models are trained with all the collected historical data. We can see from Table 6 that the resilience level is between 1 and 2, indicating that the system is relatively resilient against disruptions from the training data set.

Table 6: The average level of the severity, recovery time, and resilience based on LS-BN, EK-BN and H-BN.


We observe that from Fig. 6-8 that, even though the general structure of LS-BN, EK-BN and H-BN are similar, we found a lot of differences among these three models. For example, nodes "Gale" and "Equipment failure" are closely connected in LS-BN, while they are not directly connected in H-BN. The previous experiments aim to quantify the resilience of Beijing Metro by analyzing all the collected historical data. In order to test the prediction capability of different models, we also design a series of numerical experiments, described as follows.

In the experiment, 429 disruption/fault event data were sampled from the original data set, and the data were classified into 11 sets randomly. Among these 11 data sets, the first 10 sets of data are used as the training set. We employ these 10 sets of data to train 10 Bayesian network inference models, respectively. The last set of data is used as the testing set to verify the inference model. Here, we also adopt the traditional (k-nearest neighbors) KNN algorithm as a benchmark. Table 7 and Table 8 present the accuracy of model training and model testing with LS-BN, EK-BN, and H-BN, respectively. Here, the accuracy of each model is captured by three indicators, i.e., severity level, recovery time, and resilience level.

Table 7: The prediction accuracy of training data sets by LS-BN, EK-BN and H-BN


Table 7 and Table 8 respectively present the model training and testing results for the considered ten instances, as well as their average values and standard deviations. We see that the model testing results in Table 8 have a little lower predicting accuracies compared with the model training results in Table 7. This is consistent with our experience as the trained models are tested on a different data set. Focusing on the results of resilience level, the prediction accuracy of LS-BN, EK-BN, and H-BN can reach a range of $70 \%$ to $80 \%$, while KNN is not as good as any developed BN models. Expect for KNN, we observe that the accuracy of EK-BN is the worst, which indicates that, even though EK-BN requires the shortest training time as it is based on expert knowledge, the structure of EK-BN is not as good as LS-BN and H-BN. More importantly, we see that the training/prediction accuracy of resilience level by H-BN is noticeably better than those of KNN, LS-BN, EK-BN, which demonstrates that H-BN has the highest prediction accuracy associated with system resilience level, since it combines expert knowledge and local search optimization.

Here, we have two interesting observations from the results. First, the prediction accuracy associated with resilience level is generally lower than that of severity level and recovery time. The possible reason is that the number of resilience levels (a total of six in the experiments) is larger than that of severity level (a total of five) and recovery time

Table 8: The prediction accuracy of testing data set by LS-BN, EK-BN and H-BN


level (a total of three). Another interesting phenomenon can be observed that H-BN is not always better than LS-BN and EK-BN with respect to the other two indicators, i.e., severity level and recovery time level (for example instances 6,7 , and 8 ). This potentially indicates that these two indicators (severity level and recovery time) are correlated with each other.

Finally, in order to test the generalization ability of BN models, we further conduct a new set of experiments: We sample the historical data from 2015 into ten groups, which are respectively used to train the models. Here, the first group of training data (i.e., instance 1) contains all the data records of 2015. Then, the models are tested on the historical data of 2016. We report the model testing results for the ten instances, as well as their average values and standard deviations in Table 9. The results demonstrate that H-BN still outperforms the other models evidently, as it achieves the best performance in 9 instances from 10. More importantly, we observe that BN models improve the prediction accuracy of resilience level by nearly $100 \%$ compared with KNN in these instances. In addition, the overall predicting accuracy of H-BN is between $80 \%$ to $90 \%$, which clearly indicates the good generalization of our BN models in practical usage.

# 5.2 Sensitivity analysis 

In this experiment, we conduct a series of sensitivity analyses on H-BN. Our aim is to identify key factors that have the most influence on the system resilience level, important information for rail decision-makers to help them take actions more precisely to enhance the system resilience.

In the experimental settings, we set "resilience" as the target node in the sensitivity analysis. Then, we use the

Table 9: The predicting accuracy of different models on historical data in 2016


indicator SI defined in Eq. (13) to evaluate the sensitivity of all the other nodes in H-BN with respect to the target node "resilience". We present the sensitivity values of each node with respect to the target node in Fig. 9. In this figure, different colors represent different SI values, where crimson indicates the most influential node (SI value between 0.6 and 0.2 ); red indicates SI values between 0.2 and 0.1 ; and light red indicates SI values between 0.1 and 0.01 ; and grey indicates the most uninfluential nodes (SI value under 0.01 ).

All the factors that may affect the value of system resilience level, and ranks them according to their SIs, as shown in Fig. 10. There are some interesting findings from these results; some of which are counter-intuitive to current experience. For example, the failures of signal equipment and platform screen doors (PSDs) occur very frequently in practice, but both have SI value of "single failure" below 0.005 , suggesting that the system resilience is not sensitive to these factors. This is possible since the recovery time of signal failure is usually fairly short (about 1 to 3 minutes). During such failures, CBTC systems can be downgraded into manual driving and the PSD failure can be a manual shield in few minutes, therefore incur relatively minor disruption to the normal operation of the metro system.

On the other hand, we can see from Fig. 10 that "switch failures" and "fire conditions" have significant impacts on the system resilience level. In case of a fire, the operator must shut the operation following safety procedures and it takes time for the system to return back to normal. It is therefore not surprising to see the significant impact of fire conditions on system resilience. However, it is not previously known, at least not to the expert knowledge of Beijing Metro, that switch failures have a significant impact on system resilience. This is possibly due to the fact that switches tend to be installed at bottlenecks in the network with high traffic density. Once a switch is broken and there is no backup strategy, all the trains have to stop before the switch, which in turn will take time for the system to recover to the normal state. The practical implication of this finding leads to recommendations that resolving switch failures

![img-8.jpeg](img-8.jpeg)

Figure 9: Sensitivity analysis of system resilience. The color of the nodes indicates the range of their SI values.

![img-9.jpeg](img-9.jpeg)

Figure 10: SI value in Sensitivity Analysis

should be put as a priority task in Beijing Metro, and it is also worth installing more digitalized monitoring systems for the real-time monitoring and timely maintenance of switches, in order to improve the overall resilience level of the urban rail systems.

# 6 Conclusion 

This study proposed a hybrid knowledge-based and data-driven approach to assessing qualitatively the resilience of urban rail transit systems. Aided with empirical historical fault data from Beijing Metro, we present three resilience evaluation models, all based on Bayesian Network (BN). Employing the BN approach offers the potential and flexibility for presenting fussy knowledge and for performing reasoning under uncertainty. BN can also relate variables of the system to each other by causal representation in a probability graph, which aids in providing railway managers with visual and analytical insights on important factors that contribute to the overall system resilience. Thus, improvement actions can be planned and executed correspondingly with the aim of designing more resilient urban railway systems.

The three BNs (LS-BN, EK-BN, and H-BN) are respectively based on a data-driven approach, expert knowledge, and a hybrid approach combining data- and expert knowledge-based approaches. The rail transit system resilience is defined as the ability of a railway system to reduce the severity level, as well as to recover quickly from disruptions. We show that H-BN combines the advantages of LS-BN and EK-BN and thus performs the best among these three models in training time and predicting accuracy.

Applying the BNs to data of 50,000 samples that occurred in Beijing Metro over a period of five years, we demonstrate the H-BN model is effective in predicting the severity, recovery time, and resilience of the operational event, by comparing with KNN, LS-BN, and EK-BN. Our results identified "switch failure" and "fire condition" being the two most important factors that affect the system resilience. The results have significant practical implications, for example, it calls for prioritizing switch maintenance, fault diagnosis, and health management in metro systems, which help detect potential break down of switches and thus minimize the fault; on the other hand, it is necessary to properly arrange maintenance personnel to increase the speed of switch repairs, thereby improving system resilience. Moreover, our BN model also visually demonstrates some underlying relevances among different components of a metro system, for example, the direct relationship between weather and equipment failures. These findings using the BN model could empower rail managers to have a better grasp of the inner-relationships of different components and weaknesses of the whole system against unexpected disruptions induced by adverse failure events.

Our study makes an initial step in applying historical fault/disruption data in analyzing the system resilience of urban rail systems. We find that training some of the BN models can take more than 15 hours in our experiments. An important future research direction, therefore, is on developing methodologies to better and more efficiently optimize the BN structure and increase the prediction accuracy, for example with the aid of deep learning techniques. Our current study focuses on the evaluation of resilience only at the "operational level"; for example, we find that

switch failure is the main factor that reduces system resilience. the More in-depth analysis should be devoted at the "equipment level", in the future, for example by analyzing the resilience of switches or other equipment sub-systems.

# Acknowledgement 

This research was supported by the the Fundamental Research Funds for the Central Universities (Nos. 2020JBM080), the State Key Laboratory of Rail Traffic Control and Safety (Nos. RCS2020ZZ004), the National Science Foundation of China (Nos. 71901016), the National Key R\&D Program of China (Nos. SQ2020YFB160102) and the Royal Academy of Engineering, UK (Newton Fund projects UK-CIAPP $\backslash 286$ and TSPC1025).

## 7 Appendix I

From the data records, we extracted six types of information for each event; they are: (i) event start time, (ii) weather condition, (iii)line condition, (iv) failure mode, (v) influence of the event and (vi) recovery time of the event. All these six types mentioned in the Section 3.1 are listed in Table 10.

Table 10: The detail elements of these six types from the data records.


The descriptions of each failure influence in Table 3 are detailed as follows.

- Line stopped operation $(\xi=3)$. Due to some large disruptions (e.g., fire), all the trains in the line stop running and cancel from the operation.
- Section operation $(\xi=3)$. Due to equipment failure of a station or section(e.g., power supply failure), the operation of the line is interrupted. Meanwhile, some sections of the line can still keep running.
- Contact rail power failure $(\xi=3)$. Due to external force or some equipment failure, the contact rail cannot supply power to the train, and all vehicles cannot pass through this section.
- Phone blocked $(\xi=3)$. When a serious signal failure occurs, the signal system cannot continue to support basic train operation. At this time, communication by phone is used to ensure safety, and operation is performed by manual driving.
- Large train interval $(\xi=2)$. Due to equipment failure(e.g., switch failure or serious signal failure), or the initial stage of failure recovery, during the adjustment of the time table, the train operation interval is larger than normal condition.
- Trains run slowly $(\xi=2)$. The train is running below the planned speed on the line due to the disruption event $e$.
- Temporary closure measures $(\xi=2)$. Due to a station failure (such as a fire situation), the station needs to close or restrict passengers access to stations to mitigate station failures.
- Not stopping $(\xi=2)$. Due to a station failure (such as a fire situation), the station needs to be closed, and all trains adopt non-stop measures at this station.
- Downgrade driving $(\xi=1)$. Due to the signal failure, the signal system used the backup system to support the manual driving model.
- Trains delayed $(\xi=1)$. Due to some disruptions (e.g., switch failure), trains can not arrive at time.
- Train interval increased $(\xi=1)$. After the disruption, due to the adjustment of the time table, or the system cannot support high-density operation, the train operation interval increases.
- Gradual recovery $(\xi=1)$. After a failure occurs, rather than recovering the failure directly, the degree of failure is regarded as a continuous variable, and the recovery task is regarded as a gradual process.
- Flow limiting measures $(\xi=1)$. Due to station or line failure, passengers on the platform accumulate, and passengers are restricted from entering the station.
- $\mathrm{EB}(\xi=1)$. Due to the failure of the system(e.g., signal failure), the running train takes emergency braking to ensure safety.

- Empty train measures $(\xi=0.5)$. The vehicle cannot continue the delivery task, so the passengers on the vehicle are emptied.
- Withdraw from operation $(\xi=0.5)$. Due to the train broken down or cannot continue the delivery task, the train leaves the main operation line.


# 8 Appendix II 

Each node in the graph represents an influencing factor, most of which are binary, only "resilience", "severity", "duration", and "month" nodes are non-binary. For binary nodes, where "state0" represents the event or state does not occur, and "state1" represents an event or state occurs. And other nodes state, such as "resilience", "severity" and "duration", represents the level of the event status. The Fig. 11 shows the basic probability distribution of each node state based on the data set $\mathcal{N}$.
![img-10.jpeg](img-10.jpeg)

Figure 11: Model distribution based on data set $\mathcal{N}$
