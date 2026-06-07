# Article 

## Bayesian Uncertainty Inferencing for Fault Diagnosis of Intelligent Instruments in IoT Systems

Qing Liu ${ }^{1, *}$, Chengcheng Wang ${ }^{2}$ and Qiang Wang ${ }^{1, * *}$ (D)<br>check for updates<br>Citation: Liu, Q.; Wang, C.; Wang, Q. Bayesian Uncertainty Inferencing for Fault Diagnosis of Intelligent Instruments in IoT Systems. Appl. Sci. 2023, 13, 5380. https://doi.org/ 10.3390/app13095380

Academic Editor: Wesley Doorsamy
Received: 21 March 2023
Revised: 7 April 2023
Accepted: 10 April 2023
Published: 25 April 2023

## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 College of Quality and Safety Engineering, China Jiliang University, Hangzhou 310018, China
2 Standard and Test Center, Instrumentation Technology and Economy Institute, Beijing 100055, China

* Correspondence: liuqing@cjlu.edu.cn (Q.L.); qiangwang@cjlu.edu.cn (Q.W.)

Abstract: Intelligent instruments are common components in industrial machinery, and fault diagnosis in IoT systems requires the handling of real-time sensor data and expert knowledge. IoT sensors cannot collect data for the diagnosis of all fault types in a specific instrument, and longdistance data transfer introduces additional uncertainties. However, because industrial equipment has complex fault causes and performances, it is typically difficult or expensive to obtain exact fault probabilities. Therefore, in this study, we proposed an innovative failure detection and diagnosis model for intelligent instruments in an IoT system using a Bayesian network, with a focus on handling uncertainties in expert knowledge and IoT monitoring information. The model addresses the challenge of complex fault causes and performances in industrial equipment, which make the obtainment of exact fault probabilities difficult or expensive. The trapezoidal intuitionistic fuzzy number (TrIFN)-based entropy method was applied in order to aggregate expert knowledge to generate priority probability, and the Leaky-OR gate was used to calculate CPT. The effectiveness of the proposed strategy was demonstrated through its application to an intelligent pressure transmitter (IPT) using the GeNIe software.

Keywords: intelligent instrument; IoT; Bayesian network; TrIFN; Leaky-OR gate

## 1. Introduction

Instrument faults can result in erroneous industrial system control or system shutdown. The fundamental issues in operating and maintaining industrial instruments include minimizing the impact of instrument failure on the overall industrial system, enhancing the continuity of intelligent manufacturing systems, and lowering the industrial instrument system maintenance cost. Therefore, it is essential to use instrument performance signals and existing fault knowledge to quickly detect instrument malfunctions, perform routine instrument fault diagnosis, and identify the failure modes.

Modern intelligent instruments now have on-site data collection and data communication capabilities, due to ongoing advancements in the field of intelligent instrument technology, which enable online monitoring and remote fault diagnostics. Intelligent instruments can gather real-time parameters and signal data after being connected to the IoT to perform remote fault diagnoses.

However, the working circumstances and fault types of intelligent instruments are various, and the obtainment of comprehensive and accurate information regarding all faults is challenging. Additionally, although on-site monitoring data can be acquired via an IoT system, only a limited number of instrument characteristics can be obtained, and there are many uncertainties in IoT data collection and long-distance transmission processes. The fault diagnosis of intelligent instruments in IoT systems needs to efficiently utilize partially accessible fault information and IoT monitoring data. Therefore, this study aims to offer a practical approach for the fault diagnosis of intelligent instruments in an IoT system, that can properly address fault information uncertainty and monitor data uncertainty.

Fault diagnosis can be achieved using data-driven, knowledge-driven, and mathematical-model-based approaches [1]. Among these, knowledge-driven approaches usually focus on the experience or knowledge of machinery or physical systems; they are simple to use and efficient in the detection of faults in expert knowledge. However, knowledge-driven approaches depend heavily on personal understanding of fault mechanisms. Determining the causes of all faults is difficult, and it is difficult to respond appropriately to new faults or faults based on expert knowledge. Data-driven approaches for fault diagnosis include multivariate statistical methods such as PCA, SVM, and deep learning algorithm methods. Nearly all of these require large volume labeled fault data to train a fault model that can respond to target fault types. Unfortunately, fault data are typically insufficient to train a good model. Data-driven models are only useful for faults with large amounts of data. A mathematical-model-based approach simulates a system's behavior using a mathematical function model, and then diagnoses faults by contrasting the model's output with the actual system state/operation data. However, the interaction between the mechanical and the electrical parts of intelligent instruments, makes it impossible to create a clear model for all faults.

Among all fault diagnosis techniques, Bayesian networks (BNs) can handle ambiguous information, such as data and expert knowledge; update probabilities; execute bidirectional reasoning; and handle data scarcity [2,3,4], which means they can be used to effectively reason based on uncertain information, including data and expert knowledge. Therefore, this study attempts to combine a knowledge-driven fault diagnosis approach with a BN framework, in order to build a practical hybrid intelligent instrument fault diagnosis method using IoT monitoring information. A BN-based intelligent instrument fault diagnosis model is constructed by synthesizing the instrument's historical fault data information, IoT online monitoring data, operation and maintenance observation information, and expert experience. When unusual/informal data from online intelligent instruments are detected, the established model can diagnose the possible fault types and instrument operating states.

This approach is practical for the fault diagnosis of intelligent instruments in an IoT system, it effectively utilizes partially accessible fault information and IoT monitoring data to diagnose possible fault types and instrument operating states, and highlights the challenges in operating and maintaining industrial instruments, such as minimizing the impact of instrument failure on the overall industrial system, enhancing the continuity of intelligent manufacturing systems, and lowering the industrial instrument system maintenance cost. The proposed model is illustrated using an IPT (intelligent pressure transmitter) as an example, and a sensitivity analysis and discussion are provided. The paper concludes by highlighting the shortcomings of the proposed model and suggesting avenues for future research.

The content is organized as follows: Section 2 provides a brief overview of BNs in fault diagnosis; Section 3 presents the BN-based hybrid fault diagnosis model for IoT intelligent instruments; Section 4 uses an intelligent pressure transmitter as an example to illustrate the proposed model; Section 5 provides a sensitivity analysis and discussion; and Section 6 concludes with a list of shortcomings and suggestions for future research.

# 2. Overview of Information Uncertainties in Fault Diagnosis Using Bayesian Networks 

Fault diagnosis in industrial scenarios typically requires inferences and reasoning by using structured variables and uncertain information. The probability graph model is a graphical causal model that describes causal relationships among variables. BNs were proposed by Pearl [5] in 1988, as a type of probability graph model. BNs use Bayes' belief concept and (directed acyclic graph) structure to represent probabilistic relationships among variables and execute inferences or predictions. They are applicable in cases in which all problems can be summarized as the probability or degree of interconnection between variables [6]. Therefore, this approach is widely employed in decision making when there are many uncertainties.

Among the various approaches to fault diagnosis, BNs function as a combination of data-driven and knowledge-driven approaches and can handle causal relationships and uncertainties with multiple faults, multiple causes, and multiple models. They have been extensively researched and used in a variety of industrial fault diagnosis scenarios [7,8]. For example, Xue et al. [9] used fuzzy rules to calculate the fuzzy probability of each mode in a BN fault in a gas-monitoring system. Lin et al. [10] dealt with operational uncertainties in evidence and historical information. In their study, the evidence was used as the basis for reasoning, and historical information was used for parameter estimation. The uncertainty mainly originated from the refusing operation rate and incorrect operation rate, which were used in the Monte Carlo simulation to obtain various failure rates.

Faults are identified in the on-site monitoring of a manufacturing process or in the operation of equipment due to the growth of the IoT. Hierarchical BN models and the BN model fusion approach are frequently used in large-scale or more complicated systems in which the likelihood of many faults is significantly increased. Chen et al. [11] developed a hierarchical BN for large-scale process monitoring and decision making, to cope with the increasing amount of process knowledge and the massive divergent variables in large-scale processes. Small-scale local units were monitored using the basic layer, and global monitoring was executed in the functional layer. The basic layer was used for local monitoring and the transfer of raw monitoring results into statistical indices. The functional layer formed the BN structure and integrated the basic layer input. A top-down fault method was used to identify the fault units and most responsible variables.

A BN can also be utilized to address the issues of incomplete data and data overload problems in multisensory data collection. Wu et al. [12] considered sensor data overload and confusion when using a BN for fault diagnosis. They focused on a situation in which a parameter is measured by multiple sensors; it was established that these multiple sensors would generate too many data inputs and lead to information overload, and at the same time, they also needed to consider incomplete sensor data due to sensor hardware failures or data acquisition system malfunctions. In their method, PCA was used to remove the malfunctioning sensor data.

Not all equipment monitoring information is quantifiable, and many failure models are only available as qualitative data. BN data fusion merges various types of data from several sources [13] to increase the effectiveness of BN diagnosis. Ademujimi et al. [14] established a combined BN model for fault diagnosis by using fused numerical and textual data. First, they developed a data fusion method for quantitative sensor data, metrology data, qualitative maintenance data logs, and corrective and preventive action reports. They then constructed a fused BN model with two individual BN models: a text-data BN model, and a numerical-data BN model. Each was constructed using a BN structure algorithm or a heuristic search method. These two models worked together with the fused multisource data. Song et al. [15] investigated a fault diagnosis situation in which the fault diagnosis results were affected by multiple subsystems. They fused abnormal symptoms detected by various types of sensors and different subsystems, and then updated the BN with the fused symptoms in order to diagnose the most likely fault and its cause.

Other studies have highlighted online fault diagnosis/monitoring using BNs. A single fault diagnosis model only had a limited diagnosis effect in a multi-fault system and was insufficient for diagnosing all faults. Yu et al. [16] constructed a purely data-driven probabilistic ensemble learning strategy and used an ensemble index to select classifiers with a better diagnostic performance. Ensemble fault classification models can capture the mixed fault characteristics of multiple faults. A BN was constructed based on selected diagnostic classifiers.

The initial BN models were constructed using previously collected data and expert knowledge and may not be compatible with an actual system. To improve diagnosis accuracy by fully utilizing practical data, Zhang et al. [17] developed a machine learning set for one parameter learning method, and three structure learning methods for delay dynamic coupled fault diagnosis.

Currently, intelligent manufacturing systems are important sources of online sensor data. The status data gathered by the distributed sensor system is crucial for defect detection in complicated multi-station manufacturing systems. He et al. [18] focused on real-time fixture faults and part reorientation faults in a multi-station assembly, complex sensor system, established a BN-based sensor deployment strategy, and used information entropy to diagnose multi-station assembly processes.

These typical research results are summarized in Table 1. In conclusion, the fault diagnosis of intelligent instruments in IoT systems must simultaneously manage online sensor data and professional expertise. However, IoT sensors are unable to gather data for the diagnosis of all fault types of a single instrument because industrial equipment has complicated fault causes and performances. In fact, only a portion of the typical parameters can be monitored. Moreover, long-distance data transfer introduces more uncertainties into the fault diagnosis of equipment in IoT systems and obtaining an exact fault probability is sometimes difficult or expensive.

Table 1. Comparison of previous works.


Among all the fault diagnosis methods, the strength of BNs lies in their ability to perform reasoning and inference in complicated systems with uncertainties, which makes it possible to reduce the complexity of fault diagnosis through probability causal inferencing. The mode proposed in this study uses a BN for fault state inferencing and can effectively handle knowledge uncertainty and sensor data uncertainty in fault diagnosis, making it meaningful for practical fault diagnosis applications in IoT systems.

# 3. The Proposed Methodology 

This study utilized a BN-based fault diagnosis reasoning framework, which is illustrated in Figure 1, and the research content is depicted in Figure 2. The BN model was constructed using the following steps: (1) determine the model scope and develop the fault tree; (2) transform the fault tree into a BN [19]; (3) acquire priority probabilities through expert knowledge; (4) determine CPT with the leaky noisy-OR model; (5) construct the BN model in GeNIe software; and (6) conduct fault diagnosis using the BN model.

![img-0.jpeg](img-0.jpeg)

Figure 1. BN fault reasoning framework.
![img-1.jpeg](img-1.jpeg)

Figure 2. Content of the proposed research.
The accuracy of fault diagnosis using Bayesian networks (BNs) is heavily reliant on the precision of fault priority probabilities assigned to the root node and conditional probability tables (CPTs). These probabilities are commonly formulated based on expert knowledge and experience. Consequently, to address uncertainty in fault diagnosis, effective methods must be identified to determine the probabilities of BN nodes with uncertainty. In this research, fault priority probability values were obtained through the linguistic evaluation of a group of experts, as described in Section A, and the leaky noisy-OR model was used to obtain the CPT of BN nodes, which could simplify the determination of CPT and consider uncontrolled factors in IoT data, as described in Section C.

# 4. Determining Priority Probability with Expert Knowledge Uncertainty 

The determination of fault priority probability in industrial equipment, is a complex process that involves multiple sources of information, such as historical or experimental fault data, as well as expert knowledge and on-site operator decisions. However, due to the diverse and often challenging industrial settings, the acquisition of sufficient data for all fault probability evaluations can be challenging and costly. Thus, expert decisions are commonly used as the primary method to obtain fault priority probabilities.

Nevertheless, it is essential to recognize that expert knowledge can be subject to bias stemming from individual perspectives and objectives [20]. Consequently, to obtain comprehensive expert opinions on fault probability, a heterogeneous group of experts needed to be established, consisting of professionals with diverse job positions and experiences [21]. During the collection of expert opinions, each expert was asked to assess the fault possibility of the root nodes using linguistic terms, with each term corresponding to an intuitionistic fuzzy number (IFN). Subsequently, the IFNs were utilized to calculate the expert aggregating weights and fault probabilities. The expert-group-opinion-based root node fault priority probability could be obtained by following the steps outlined below.

Step 1: Quantification of engineering knowledge
Experts' opinions on root node fault possibilities were classified into seven linguistic terms: very low (VL), low (L), reasonably low (RL), moderate (M), reasonably high (RH), high $(\mathrm{H})$, and very high $(\mathrm{VH})[22,23]$. In order to quantify the linguistic decision terms,

intuitionistic fuzzy numbers (IFNs) were utilized to transfer expert linguistic decision terms, and to obtain the exact probability value.

Intuitionistic fuzzy sets have been proposed as an extension of the traditional fuzzy set theory, as they offer a more effective approach to describing uncertainty and hesitation in linguistic decision making. Various types of intuitionistic fuzzy numbers, including trapezoidal, triangular, Gaussian, or bell-shaped functions, have been employed for the fuzzification of linguistic terms. Among these, the trapezoidal membership function is frequently applied in evaluation situations with high uncertainty. Therefore, when defining the membership function, TrIFN was used in this study to describe the linguistic evaluation level of experts. The linguistic terms and corresponding TrIFNs are listed in Table 2.

Table 2. Linguistic terms and TrIFNS.


If $\bar{a}$ is TrIFN, then its membership function is defined as (1) [24]:

$$
u_{\bar{a}}= \begin{cases}\frac{x-a}{b-a} u_{\bar{a}}, & a \leq x<b \\ u_{\bar{a}}, & b \leq x \leq c \\ \frac{d-x}{d-c} u_{\bar{a}}, & c<x \leq d \\ \overline{0}, & \text { otherwise }\end{cases}
$$

Its non-membership function is defined as (2) [24]:

$$
v_{\bar{a}}= \begin{cases}\frac{(b-x)+v_{\bar{a}}(x-a)}{b-a}, & a \leq x<b \\ v_{\bar{a}}, & b \leq x \leq c \\ \frac{(x-c)+v_{\bar{a}}(d-x)}{d-c}, & c<x \leq d \\ 0, & \text { otherwise }\end{cases}
$$

where $0 \leq u_{\bar{a}} \leq 1,0 \leq v_{\bar{a}} \leq 1$, and here, a TrIFN is denoted as $\bar{a}=\left([a, b, c, d] ; u_{\bar{a}}, v_{\bar{a}}\right)$.
Let $\bar{a}_{1}=\left(\left[a_{1}, b_{1}, c_{1}, d_{1}\right] ; u_{\bar{a}_{1}}, v_{\bar{a}_{1}}\right)$ and $\bar{a}_{2}=\left(\left[a_{2}, b_{2}, c_{2}, d_{2}\right] ; u_{\bar{a}_{2}}, v_{\bar{a}_{2}}\right)$ be two TrIFNs, and $\lambda \geq 0$; then, the calculation rules between $\bar{a}_{1}$ and $\bar{a}_{2}$ are as follows [24,25]:

$$
\begin{gathered}
\bar{a}_{1}+\bar{a}_{2}=\left(\left[a_{1}+a_{2}, b_{1}+b_{2}, c_{1}+c_{2}, d_{1}+d_{2}\right] ; u_{\bar{a}_{1}}+\mu_{\bar{a}_{2}}-u_{\bar{a}_{1}} u_{\bar{a}_{2},} \quad v_{\bar{a}_{1}} v_{\bar{a}_{2}}\right) \\
\bar{a}_{1} \otimes \bar{a}_{2}=\left(\left[a_{1} a_{2}, b_{1} b_{2}, c_{1} c_{2}, d_{1} d_{2}\right] ; u_{\bar{a}_{1}} u_{\bar{a}_{2}}, v_{\bar{a}_{2}}+v_{\bar{a}_{2}}-v_{\bar{a}_{1}} v_{\bar{a}_{2}}\right) \\
\lambda \bar{a}_{1}=\left(\left[\lambda a_{1}, \lambda b_{1}, \lambda c_{1}, \lambda d_{1}\right] ; 1-\left(1-u_{\bar{a}_{1}}\right)^{\lambda}, v_{\bar{a}_{1}}^{\lambda}\right) \\
\bar{a}_{1}^{\lambda}=\left(\left[a_{1}^{\lambda}, b_{1}^{\lambda}, c_{1}^{\lambda}, d_{1}^{\lambda}\right] ; u_{\bar{a}_{1}}^{\lambda}, 1-\left(1-v_{\bar{a}_{1}}\right)^{\lambda}\right)
\end{gathered}
$$

Step 2: Aggregation of expert opinions
Because of the heterogeneity of expert opinions, it was necessary to provide a method for the aggregation of opinions from the expert group. As previously mentioned, the experts' linguistic terms had already been transformed into TrIFNs before being aggregated. Each TrIFN already carried information regarding the uncertainty and hesitation of the

experts; therefore, expert weights were determined using TrIFNs, and the expert opinions were then aggregated using these weights.

Group decision inconsistency and individual hesitation are the main uncertainties in expert group decision making, and they can all be viewed as unordered decision information. Therefore, in this study, entropy was introduced in order to address this issue. TrIFN-based cross-entropy and intuitionistic fuzzy entropy were employed to generate comprehensive expert weights, using the following steps [26,27]:
(1) Assigning the initial intuitionistic fuzzy entropy weight of each expert: To obtain a compound group decision at the beginning, each expert was given an initial weight, and all faults had the same importance.
(2) Calculating the cross-entropy weight of each expert: Cross-entropy was used to measure the inconsistency between individual experts' decisions and group decisions. If the cross-entropy was smaller, the inconsistency was lower, and the expert was assigned a larger weight. To obtain compound group decisions, each expert was given a predetermined initial weight, and the initial expert group decision could be obtained using (3)-(6). Individual evaluation results for $n$ attributes of the expert group with $s$ experts can be expressed as $y_{k}=\left(y_{k 1}, y_{k 2}, \ldots, y_{k n}\right)^{T}$, and the weighted group evaluation results can be expressed as $x=\left(u_{i}, v_{i}\right),)^{T}$, among them being $y_{k i}=\left(u_{k i}, v_{k i}\right), x_{i}=\left(u_{i}, v_{i}\right), k=1,2, \ldots, s, i=1,2, \ldots, n$. The cross-entropy between the individual expert evaluation results and the group expert evaluation results, was calculated using (7):

$$
D\left(y_{k}, x\right)=\sum_{i=1}^{n}\left[u_{k i} \ln \frac{u_{k i}}{\frac{1}{2}\left(u_{k i}+\mu_{i}\right)}+v_{k i} \ln \frac{v_{k i}}{\frac{1}{2}\left(v_{k i}+v_{i}\right)}\right]+\sum_{i=1}^{n}\left[u_{i} \ln \frac{\mu_{i}}{\frac{1}{2}\left(u_{k i}+\mu_{i}\right)}+v_{i} \ln \frac{v_{i}}{\frac{1}{2}\left(v_{k i}+v_{i}\right)}\right]
$$

Then, the cross-entropy weights of one expert $D_{k}$ was defined as (8):

$$
r_{k}=\frac{\frac{1}{D\left(y_{k}, x\right)}}{\sum_{k=1}^{s} \frac{1}{D\left(y_{k}, x\right)}}
$$

Among them, $0 \leq r_{k} \leq 1, k=1,2, \ldots, s, \sum_{k=1}^{s} r_{k}=1$.
(3) Calculating the intuitionistic fuzzy entropy weight of each expert: Burillo and Bustince [28] introduced intuitionistic fuzzy entropy weight. According to the definition of entropy, if the entropy value of an individual expert evaluation was larger, it meant that the expert's individual evaluation results contained more uncertain information, and the expert should have been assigned a smaller weight. Conversely, a larger weight was required. The entropy was calculated using (9), and the entropy weight of each expert was obtained using (10).

$$
\begin{gathered}
E_{k}=\frac{1}{n} \sum_{i=1}^{n} \frac{\min \left\{u_{k i}, v_{k i}\right\}+\pi_{k i}}{\max \left\{u_{k i}, v_{k i}\right\}+\pi_{k i}} \\
e_{k}=\frac{\left(1-E_{k}\right)}{\left(s-\sum_{k=1}^{s} E_{k}\right)}
\end{gathered}
$$

Among them, $\pi_{k i}=1-u_{k i}-v_{k i}, 0 \leq e_{k} \leq 1, k=1,2, \ldots, s, \sum_{k=1}^{s} e_{k}=1$.
(4) Calculating the final weight of each expert: The final weight of each expert had to consider both the cross-entropy and intuitionistic fuzzy weights, which were calculated using (11) [26].

$$
\omega_{k}=\frac{1}{2} r_{k}+\frac{1}{2} e_{k}
$$

Step 3: Determination of root event fault probability
After obtaining the final weights of each expert, the evaluation results of the individual experts were combined with the final expert weights in order to generate weighted expert group evaluation results. The expected value of the weighted group evaluation TrIFN results was calculated using (12) [24]:

$$
I(\vec{a})=\frac{1}{8} \times\left[\left(a+b+c+d\right) \times\left(1+u_{\vec{a}}-v_{\vec{a}}\right)\right]
$$

# 5. Determining Conditional Probability with Information Uncertainty 

The probabilities of the medium and top nodes were calculated after determining the fault priority probabilities of all of the root nodes.

The CPT of the corresponding nodes must be set in BNs in order to express the logical relationship between nodes. To simplify fault reasoning, the noisy-OR gate is the most common form in BN analysis. The OR gate works as in Figure 3. In a noisy-OR gate, each node only has two states, "Yes", or "No", and does not need excessive parameters when determining CPT [21]. With the noisy-OR gate model, the parameter value over the predefined threshold is viewed as in the fault state and is transferred to the fault probability, which is easy to use in a real IoT system. In the noisy-OR gate model, each cause $x_{i}$ is assumed sufficient to cause $y$ in the absence of other causes, where $P_{i}$ is the joint probability of the $i$ th root event and represents the probability that $y$ will be present if only $x_{i}$ is present, and all other explicitly defined causes $x_{j}, j \neq i$ are absent. That is:

$$
P_{i}=P\left(y \mid \bar{x}_{1}, \bar{x}_{2}, \ldots ., x_{i}, \ldots ., \bar{x}_{n-1}, \bar{x}_{n}\right)
$$

![img-2.jpeg](img-2.jpeg)

Figure 3. OR gate.
Then, given a subset $x_{p}$ of $x_{i}$ s that is present, the conditional probability of $y$ can be obtained using (14) [29].

$$
P\left(y \mid x_{p}\right)=1-\prod_{i: x_{i} \in x_{p}}\left(1-P_{i}\right)
$$

However, it is assumed that an IPT BN can satisfy the two conditions of the noisy-OR gate [30]. If $x_{p}$ is empty, then $P\left(y \mid x_{p}\right)=0$. However, $x_{p}$ is the only recognized fault factor in a fault system, and there are many uncertainties that affect sensor data and symptoms in IoT systems [29,31]. These uncertainties are usually unpredicted or unknown factors for faults, and the boot nodes in a fault tree cannot cover all fault factors. Therefore, to describe the impact of these latent factors on IPT faults, the leaky noisy-OR gate model [29] depicted in Figure 4 was applied in this study in order to determine the CPT for the IPT BN model.
![img-3.jpeg](img-3.jpeg)

Figure 4. Leaky noisy-OR model.
In the leaky noisy-OR model, the fault probability caused by latent factors can be expressed by $P_{L}$, which represents the probability that the effect $y$ will occur spontaneously

in the absence of any cause in $x_{p}$ [30,32]. The conditional probability of $y$ was obtained using the following equation, where $P_{L}=P\left(y \mid \bar{x}_{1}, \bar{x}_{2}, \bar{x}_{3}, \ldots, \bar{x}_{n}\right)$ :

$$
P\left(y \mid x_{p}\right)=1-\left(1-P_{L}\right) \prod_{i: x_{i} \in x_{p}}\left(1-P_{i}\right)
$$

When using these functions to obtain BN node probabilities, expert opinions were used to directly determine $P_{i}$. Using the formula above, the CPT of the top nodes could be obtained using the BN model.

# 6. BN Model Example for IPT in an IoT Network 

The Internet of Things (IoT) network is composed of three primary components: devices, networks, and cloud computing. These devices, often referred to as "smart" devices, are equipped with sensors and actuators that enable them to gather data and perform various functions. The network connects these devices, allowing them to share data and communicate with other devices and systems. Data collected by these devices are stored, processed, and analyzed, in the cloud. IoT-based networks have diverse applications across industries. For instance, the implementation of IoT technology in the smart grid has been extensively studied by researchers [33-37], as it has the potential to enhance the efficiency, sustainability, and reliability of the electrical grid. Similarly, in various industries, intelligent instruments are being widely adopted as "smart" devices. For example, in industrial control, intelligent pressure transmitters (IPTs) are extensively used to measure liquid level, pressure, and flow. Compared to traditional pressure transmitters, IPTs can receive and output digital signals, based on specific communication protocols. Given that this transmitter is the most commonly used equipment in industrial control areas, the accuracy and timeliness of IPT fault detection are directly linked to production safety and stability. Therefore, IPTs in IoT systems can serve as models for verification purposes. The overall structure of the IoT system is illustrated in Figure 5.
![img-4.jpeg](img-4.jpeg)

Figure 5. IoT system hardware architecture.
There are numerous types of IPTs, and a certain type of IPT was used as a method verification example in this study. The selected IPT contains a power resource module, a micro control unit (MCU) module, a sensor module, a signal conditioning module, a display module, and structure support components.

The power resource module links the external power supply and converts it into a power supply that is suitable for transmitter operation. The sensor module collects data using on-site sensors. The signal conditioning module adjusts the data signal conditioning circuit.

The MCU module provides and processes measurement data for real-time applications of the human-machine interface and communication interfaces. Functions such as configuration, calibration, rectification, and diagnosis, have been realized using the MCU module.

The display module integrates the display data function on the meter, the output data function, and local buttons for issuing requests. It is the human-machine interface through which the IPT interacts with the operators.

IPTs have a variety of faults in real operation; the failure modes of each IPT module were analyzed and denoted as root events, and "the un-normal performance of IPT" was regarded as a top event. Based on the IPT module structure and failure mechanism, there are 33 typical IPT faults, x1-x33, and they are described in Table 3. However, these faults cannot be directly monitored by IoT sensors, and only a portion of the performance parameters of the functional modules can be monitored. Therefore, a fault tree (FT) for BN construction was defined according to the actual monitoring parameters, and it had five layers: a top node layer, a functional module node layer, a monitoring node layer, an intermediate node layer, and a root node layer, as shown in Figure 6.

Table 3. Fault tree nodes and description of root nodes.


![img-5.jpeg](img-5.jpeg)

Figure 6. IPT fault tree structure and its layers.
The fault tree in Figure 6 was transformed into a BN model using the leaky noisy-OR gate; the BN model has 1 top node, 6 module nodes, 10 monitored nodes, 3 intermediate nodes, and 33 root nodes. Five experts' opinions regarding the joint fault probability level of the root nodes were collected in this study. The first expert specializes in researching faults in industrial instruments, another is responsible for the operation and maintenance of the IoT system in which IPTs are located, a third is an instrument engineer working on-site with IPT, a fourth is an operator who works with IPT on-site, and the fifth is technical personnel from the manufacturer of the IPT. Their opinions were expressed using a sevenlevel linguistic term. The linguistic terms and their corresponding TrIFNs are listed in Table 1. The linguistic evaluation results are presented in Table 4. Their corresponding TrIFNs were used to determine the qualitative fault probability, using the steps outlined in Section 3. Table 5 displays the experts' weight calculations, and the calculated root node fault joint probabilities are shown in Table 6 as the expected values.

Table 4. Experts' opinions of the joint fault probability of basic events in root nodes.


Table 5. Experts' weight calculations.


Table 6. Weighted TrIFN and the expected value.


After obtaining the joint probability, the CPT of the intermediate and top nodes was calculated using the leaky OR gate. For example, node M11 had 3 child nodes: x1, x2, and x3. After obtaining the joint probabilities of $\mathrm{x} 1, \mathrm{x} 2$, and x 3 , as shown in Table 6, M11's CPT could be calculated using Equation (15), as presented in Table 7.

Table 7. CPT of node M11.


The IPT BN model was established using GeNIe software, as shown in Figure 7, where the IPT denotes the top node, M1 to M6 are module nodes, the light green nodes are monitored nodes, M231 and M321 are intermediate nodes, and x1-x33 are the root nodes. When the IPT was in the fault state, its fault state was set to " 0 " in GeNIe, and then, the fault probability of related intermediate nodes and the top node, could be calculated automatically, as shown in Figure 8. A BN model was used to conduct the simulations. When fault states occurred in the root nodes, the fault occurrence probability of the top and intermediate nodes could be obtained, as shown in Figure 9. This demonstrates how the fault states of root nodes x 23 and x 15 , affected the fault states of the related intermediate and top nodes.

![img-6.jpeg](img-6.jpeg)

Figure 7. BN model with fault probability.

![img-7.jpeg](img-7.jpeg)

Figure 8. BN model when IPT is in failure state.

![img-8.jpeg](img-8.jpeg)

Figure 9. BN model when x23 and x15 nodes are in failure state.

# 7. Sensitivity Analysis Overview of Information Uncertainties in Bayesian Networks 

A sensitivity analysis was used to determine how the root node fault state affected the intermediate and top nodes [38,39]. The top event was treated as the target node, and a sensitivity analysis was performed by changing the fault state of the root nodes. The results of the sensitivity analysis are presented in Figures 10-12. Figure 10 shows that the sensitivity of the nodes could be divided into 4 levels. The influence of the nodes on the top node state was divided into 5 levels; the results are listed in Table 8. For example, in the monitored node layer, monitored nodes had different effects on the fault state of the top node. M21, M22, and M23 were the most influential nodes; M11, M32, M41, M51, and M61 were the second-most influential nodes; and M12 and M31 were the third-most influential nodes. In addition, regarding nodes at higher levels, we must pay more attention to their use and maintenance.

![img-9.jpeg](img-9.jpeg)

**Figure 10.** Sensitivity analysis of IPT top node fault probability.

![img-10.jpeg](img-10.jpeg)

**Figure 11.** Sensitivity analysis of M3 node fault probability.

![img-11.jpeg](img-11.jpeg)

Figure 12. BN model when M21 is in fault state.
Table 8. Nodes' influential levels.


Sensitivity analysis could also be used for the module nodes, as shown in Figure 11. It revealed that different root fault events will affect the whole functional module's fault state.

In the established model, monitored nodes are important performance parameters for the corresponding functional modules. If any of these key parameters are in an abnormal or fault state, the possible root event fault probability and overall fault state of the IPT, can be diagnosed. Figure 12 shows the fault probability performance of the root nodes and the top IPT node, when the monitored node M21 was in the fault state. Therefore, the most probable fault type and its qualitative probability can be determined when abnormal data are detected by the IoT.

As mentioned previously, the most influential performance parameters can also be determined through the established BN model. Therefore, the second application of the proposed method is in the identification of important nodes and their influence on the top node fault. This is helpful in the development of a preventive maintenance strategy to reduce possible fault rates. Although an OR gate was used in this study, when the fault probability of the influential nodes and modules decreased, the IPT fault probability also decreased. Therefore, preventive control or more frequent monitoring measures for these node data can be implemented in order to minimize fault probability and improve the stability and reliability of the IPT instrument.

# 8. Conclusions 

In an IoT system, innovative solutions are required to handle the numerous unknowns related to sensors, problem determination, and symptoms. Fault diagnosis for equipment in IoT system must not only consider incomplete fault information and sensor data, but also address uncertainties arising from multiple types of faults. In this study, to tackle these challenges, a novel BN-based fault diagnosis approach for industrial instruments in an IoT system, was presented. This approach places particular emphasis on managing uncertainties in the construction of a BN model. To achieve this, the TrIFN-based entropy method was utilized in order to aggregate the priority probability, and the leaky-OR gate was employed to calculate the CPT. The proposed model was applied to an intelligent pressure transmitter, and a sensitivity analysis was conducted to evaluate its effectiveness. The results highlight the innovative nature of the proposed approach, which was shown to successfully manage fault diagnosis uncertainties, and enhance the accuracy of BN model diagnosis and fault detection.

Although expert knowledge is compiled using intuitionistic fuzzy numbers, there are no standards for expert selection. For simplicity, the node state in this study had two states; however, node signals may have multiple states, or use continuous values. Another drawback is that, while the IPT fault tree covers practically all fault types, current IoT systems can only monitor a portion of the IPT fault tree's root nodes. Therefore, it would be more useful to adjust this method according to monitored IoT parameters.

Author Contributions: Conceptualization, Q.L. and C.W.; methodology, Q.L.; investigation, C.W. and Q.L.; data curation, C.W. and Q.W.; writing—original draft preparation, Q.L.; writing—review and editing, Q.L. and Q.W.; project administration \& funding acquisition, Q.W. All authors have read and agreed to the published version of the manuscript.
Funding: This work was supported in part by the National Key Research and Development Program of China 2020YFB2009400; the Zhejiang Special Support Program for High-Level Personnel Recruitment of China 2019R52017; and The National Natural Science Foundation of China 52175257; "Pioneer" and "Leading Goose" R\&D Program of Zhejiang 2022C03179.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Data supporting reported results is already available in the content.
Conflicts of Interest: The authors declare no conflict of interest.
