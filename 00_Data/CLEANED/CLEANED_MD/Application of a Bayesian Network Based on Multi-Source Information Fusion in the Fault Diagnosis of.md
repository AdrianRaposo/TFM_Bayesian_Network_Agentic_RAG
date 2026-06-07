# Article 

## Application of a Bayesian Network Based on Multi-Source Information Fusion in the Fault Diagnosis of a Radar Receiver

Boya Liu ${ }^{1,2, *}$, Xiaowen Bi ${ }^{1}$, Lijuan Gu ${ }^{1}$, Jie Wei ${ }^{1}$ and Baozhong Liu ${ }^{2}$

## check for updates

Citation: Liu, B.; Bi, X.; Gu, L.; Wei, J.; Liu, B. Application of a Bayesian Network Based on Multi-Source Information Fusion in the Fault Diagnosis of a Radar Receiver. Sensors 2022, 22, 6396.
https://doi.org/
$10.3390 / s 22176396$
Academic Editor: Stefania Montani
Received: 6 August 2022
Accepted: 23 August 2022
Published: 25 August 2022
Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## 0

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Radar Faculty, Ordnance NCO Academy, Army Engineering University of PLA, Wuhan 430075, China
2 Hubei Key Laboratory of Intelligent Robot, Wuhan Institute of Technology, Wuhan 430073, China

* Correspondence: athrunstar@sina.com; Tel.: +86-138-7143-6931


#### Abstract

A radar is an important part of an air defense and combat system. It is of great significance to military defense to improve the effectiveness of radar state monitoring and the accuracy of fault diagnosis during operation. However, the complexity of radar equipment's structure and the uncertainty of the operating environment greatly increase the difficulty of fault diagnosis in real life situations. Therefore, a Bayesian network diagnosis method based on multi-source information fusion technology is proposed to solve the fault diagnosis problems caused by uncertain factors such as the high integration and complexity of the system during the process of fault diagnosis. Taking a fault of a radar receiver as an example, we study 2 typical fault phenomena and 21 fault points. After acquiring and processing multi-source information, establishing a Bayesian network model, determining conditional probability tables (CPTs), and finally outputting the diagnosis results. The results are convincing and consistent with reality, which verifies the effectiveness of this method for fault diagnosis in radar receivers. It realizes device-level fault diagnosis, which shortens the maintenance time for radars and improves the reliability and maintainability of radars. Our results have significance as a guide for judging the fault location of radars and predicting the vulnerable components of radars.


Keywords: radar system; fault diagnosis; multi-source information fusion; Bayesian network; device-level

## 1. Introduction

With the continuous progress of modern science and technology, an endless variety of new weapons have changed modern combat [1]. In modern war, air attacks are often used as the main means of warfare. Now more than ever, gaining control of the air has become vitally important. Radars have thus become indispensable equipment in the air defense system of various countries.

A radar is an electronic device that can work all day and in all weather conditions [2]. Due to the demanding tasks and long operation time of radars, the equipment failure rate has increased markedly. A radar receiver is an important component of a radar system. It performs pre-selection, amplification, frequency conversion, filtering, demodulation, and digital processing on the echo signal received by the radar antenna while suppressing external interference clutter and internal noise so that the echo signal can maintain the target information as much as possible in order to conduct further specialized signal processing [3]. Once the radar receiver fails, the radar is not able to accurately detect the target, which affects the normal operation of the entire air defense system [4]. Therefore, it is of great significance to strengthen the condition monitoring of radar receivers, analyze and evaluate important parameters, diagnose faults in time, and quickly formulate solutions.

With the development of artificial intelligence technology and the improvement of signal processing accuracy, technologies such as wavelet transform [5,6], support vector machines [7,8], principal component analyses [9,10], artificial neural networks [11-13], and deep learning [14-16] have been widely used in the field of fault diagnosis. These

methods are able to learn and mine historical data under certain functional constraints to discern the corresponding relationship of a data model and then approach the mapping mechanism implied in the system data to carry out fault detection and diagnosis [17]. Based on monitoring data from different sources and types, this method solves the problem of incomplete fault representation and has real-time capabilities. However, this method invariably depends on the accuracy of the mathematical model and the real-time nature of the data and is restricted by factors such as the number of data and the calculation efficiency of the model. In most cases, these models they are unable to explain their reasoning processes and results, and there are different degrees of defects in the treatment of uncertainty problems.

Bayesian networks, proposed by Judea pearl in 1988, have powerful uncertainty problem processing abilities and are widely used in computer intelligence science, industrial control, medical diagnosis, and other fields. Moreover, Bayesian network can effectively express and fuse multi-source information and have great advantages when identifying the faults caused by uncertainty and the correlation of complex equipment [18].

Traditional radar fault diagnosis is realized by built-in test equipment (BITE). BITE is distributed in each function module of the radar. It can detect faults in equipment components and identify the faulty components. The maintenance personnel can then replace the faulty parts to eliminate the fault. The diagnostic process of BITE is shown in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. BITE diagnosis flow chat.
When using BITE technology for maintenance support, the average fault recovery time (MTBR) of a radar is less than 10 min , but this equipment comes with many shortcomings. BITE lacks the ability to detect and isolate intermittent faults. Moreover, due to the direct replacement of the faulty modules, the service life of the components is generally reduced, resulting in an increase of $10-20 \%$ in the manufacturing and maintenance cost of a radar [19]. How to accurately and quickly locate the fault point inside the component and build a circuit board-level or even device-level fault diagnosis system is an unsolved problem that is worthy of study.

However, due to the compact and complex structure of modern radars and the high internal integration of their components [20], if a bite circuit is embedded in the components, it will not only have great requirements in terms of space utilization but may also have a certain impact on the signals passing through the components. The echo signal reflected from the target received by a radar antenna is very weak, unstable, and cluttered [21]. The impact of bit circuit embedding on the echo signal cannot be ignored, which means that BITE embedded in the receiver component is not feasible.

In addition, there is no differentiation between fault phenomena and causes in the system operation. A fault often manifests itself in a variety of fault phenomena, and sometimes several faults will be reflected by only a single fault phenomenon. Therefore,

the uncertainty between the fault phenomenon and the fault cause make fault diagnosis more complex [22].

In order to solve these problems, this paper proposes a Bayesian network fault diagnosis method based on multi-source information fusion technology. This method realizes intelligent fault detection and diagnosis in radar receiver and improves the service life of radar components. The contributions of this paper are summarized as follows:

1. A variety of monitoring sensors are designed in the receiver. Based on multi-source information fusion technology, the prior diagnosis database and the real-time monitoring database reflected by the sensor are analyzed and fused to achieve the diversification, quantification, and standardization of the data.
2. A Bayesian network fault diagnosis model is proposed and applied to the fault diagnosis analysis of a radar receiver. The analysis results show that this method is effective.
3. In contrast to traditional BITE technology, our method can realize accurate devicelevel fault location and fault cause analysis and avoid the replacement of whole components, reducing the maintenance costs of radars.
The remainder of this paper is organized as follows. Section 2 introduces the fault diagnosis system of a radar receiver. Section 3 provides the sample data and calculation results. Section 4 presents an in-depth discussion of the calculation results. Finally, conclusions are drawn in Section 5.

# 2. Fault Diagnosis System of Radar Receiver 

### 2.1. Radar Receiver

The input signal of the receiver is always very weak and needs to be amplified and filtered to meet professional signal processing requirements. Early radar receivers used multistage, high-frequency amplifiers to amplify the receive echo signals, which were called high-frequency amplification receivers [23]. Since then, superheterodyne receivers have become more widely used, which mainly rely on the fixed frequency intermediate frequency (IF) amplifier to amplify the signal. The basic structure of a superheterodyne receiver is shown in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2. Structure Diagram of a Superheterodyne Receiver.
A superheterodyne receiver is generally composed of a limiter, a radio frequency (RF) low noise amplifier (LNA), a sensitivity time control (STC) circuit, a RF filter, a mixer, an IF amplifier, an IF filter, a detection circuit, and a low-frequency power amplifier [24]. The echo signal received by the antenna enters the receiver through the transmitter/receiver $(\mathrm{T} / \mathrm{R})$ switch. The echo signal inherits the RF characteristics of the transmitted signal. The

power of an echo signal is weak, but its frequency is high [25]. Therefore, the power of an echo signal needs to be amplified to meet the normal working power of the detector. However, the frequency of the echo signal needs to be down-converted into an IF signal. In practical radar receiver applications, especially when the working band is high and the bandwidth is wide, a secondary frequency conversion scheme is usually adopted. Once an IF signal that meets the requirements is obtained, the in-phase digital signal and quadrature digital signal are output through gain control and phase detection and sent to the digital signal processor [26]. The two local oscillator signals required for the mixer and the phase reference signal that are required for phase detection are generated by the frequency synthesizer.

# 2.2. Multi-Source Information Fusion Technology 

The traditional fault diagnosis method only analyzes one or a small number of kinds of information from the machine state to extract information about the machine behavior. Practice has proven that although using one kind of information can sometimes identify faults in mechanical equipment, the diagnosis results obtained in many cases are not reliable. Due to the development of computers, signal processing, artificial intelligence, pattern recognition, and other technologies, a new fault diagnosis method based on multi-source information fusion technology has emerged [27].

Information fusion technology can be described as the automatic detection, association, estimation, and combination of multi-source data to obtain more accurate and reliable information or inferences. It is a global method of multi-dimensional data processing [28]. The fusion framework of multi-source information fusion technology is generally divided into three stages: data-level fusion, feature-level fusion, and decision-level fusion [29].

Data-level fusion is the direct fusion of the original data, which is mainly used for the fusion of data with relatively consistent information types, such as image analysis, signal processing, text data format conversion and so on. Data-level fusion maximizes the authenticity of the information, but its fault tolerance is weak. Additionally, the effect is not ideal for the fusion of information that includes many data types and complex relationships [30]. Feature-level fusion is used to conduct feature extraction from the information source and then to carry out association fusion on this basis. Feature-level fusion realizes the structural consistency of different types of information through feature extraction, retains ample information, provides support for later decision analysis, and improves real-time information processing ability, accuracy, and efficiency [31]. Decisionlevel fusion involves high-level fusion. Compared with data-level fusion and feature-level fusion, it has the greatest amount of information loss and the poorest accuracy, but it can process a wide range of data types with high flexibility, strong anti-interference ability, and good fault tolerance [32].

The multi-source information fusion fault diagnosis model used in our system is shown in Figure 3.

![img-2.jpeg](img-2.jpeg)

Figure 3. The multi-source information fusion fault diagnosis model.

# 1. Data Source 

The data sources of the system are divided into prior diagnosis data sources and realtime data sources. The prior diagnosis data are mainly derived from expert experience, a case library, and historical monitoring data. The key points and conclusions of inspections, maintenance means, and maintenance steps summarized by professional maintenance technicians are used to compile the expert experience and case library, which are generally embodied in paper documents, electronic manuals, or oral experience inheritance. The historical detection data source is the operation data of the radar monitoring system or BITE since the radar has been operational. The BITE system of the radar is equipped with a single sensor, which is usually located inside the receiver in order to monitor the most important components in the receiver [33]. The operation data of the radar monitoring system or BITE only locate the fault at the level of the subsystem or the whole unit. The faults recorded in the expert experience and case library also have certain contingencies and cannot accurately reflect the current situation of the radar in real time [34]. If only a priori diagnosis data are used as the data source for the fault diagnostic model, it is unable to meet the requirements of fault diagnostic accuracy. Therefore, a variety of sensors are installed in the radar system to constantly monitor and inform the user of the status of the radar receiver.

An information processing method that uses multiple sensors to monitor the same specific target can overcome the uncertainty and limitations of a single sensor, obtain a consistent interpretation and description of the measured object, and realize the corresponding decision-making and estimation [35]. The type and number of sensors placed in the radar receiver can be determined according to the structure of the receiver and the parameter type of the monitored components.

Considering the complexity of the receiver's high-frequency processing circuit and detection output circuit, as well as the variability of the environment, it can be added voltage sensors, current sensors, detection circuits, temperature sensors, humidity sensors, sound sensors, and cameras to monitor the voltage and current of the transmission path, the amplitude and phase of the signal, the sound of the internal action response in the components, and the temperature and humidity inside the receiver so as to achieve multidirectional and multi-dimension real-time monitoring and recording.

## 2. Information Fusion

The original data collected from the data sources are diverse, so it is necessary to standardize the multi-source information before fusion.

It must carry out data standardization and format conversion on the a priori diagnostic data first, then convert them into a unified data format, and finally screen out useful information for correlation and calibration on the premise of consistent data types [36]. The data collected by various sensors may be waveforms, voltage values, current values, images, and so on. The data must be preprocessed to extract and identify the required information before fusion. Then the redundant, complementary, and conflicting information of the multiple sensors in the system is associated and calibrated by following certain rules. Finally, the information of the two data sources is fused to obtain a consistent description of the real situation of the measured object. This method provides more meaningful and valuable information for decision-making.

# 3. Decision Discrimination 

Effective information and decision theory are used to infer results [37]. Commonly used decision theories include the Kalman filter, the Dempster-Shafer evidence theory, expert knowledge systems, artificial neural networks, etc. Bayesian network reasoning is used in this paper. Bayesian networks have a strong ability to deal with uncertain problems. The construction of a Bayesian network consists of the determination of the network nodes, the directed correlation between the nodes, and the posterior probability. After reasoning through a Bayesian network, the final result of the fault diagnosis is output.

### 2.3. Bayesian Network

### 2.3.1. Brief Description

A Bayesian network is a directed graphic description based on a network structure that is the product of the integration of probability theory, graph theory, and decision theory [38].

It uses a structural directed graph to express the association relationship between the information elements and the influence node variables, uses the directed edge between nodes to connect the association relationship between elements, and uses conditional probability to express the influence degree of each information element.

Let $\mathrm{H}=\mathrm{X}, \mathrm{L}$ denote a directed acyclic graph where $\mathrm{X}=\left\{X_{1}, X_{2}, \cdots, X_{n}\right\}$ denotes the set of random variables and $L$ denotes the set of edges of the Bayesian network, then the joint probability of $X$ can be expressed as:

$$
P\left(X_{1}, X_{2}, \cdots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid \operatorname{Parents}\left(X_{i}\right)=P\left(X_{n} \mid X_{n-1}, \cdots, X_{1}\right) P\left(X_{2} \mid X_{1}\right) P X_{1}\right.
$$

The basis of Bayesian network reasoning is the probability relationship between variables or events.

A Bayesian network can be regarded as the joint probability distribution of a group of random variables, from which reasoning and decision-making can be carried out [39]. All kinds of information related to fault diagnosis and maintenance decisions can be incorporated into a Bayesian network structure, which can handle it uniformly in the form of nodes and fuse different parts effectively according to the correlations between the information.

In addition, it can learn and reason under limited, incomplete, and uncertain information conditions and make reasonable and quantifiable decisions to maximize the decision efficiency [40].

### 2.3.2. Determination of Bayesian Network

The main functions of the receiver are frequency conversion and phase detection [41]. There are many types of faults in these two functions. This paper takes the fault that the IF signal output obtained after the secondary mixing of the receiver is abnormal as an example to analyze the possible factors causing the fault.

Abnormal IF signal output indicates a variety of fault phenomena. The fault phenomena that may be detected include abnormal signal frequency, inconsistent multi-channel signal phase, inconsistent amplitude, low signal power, abnormal control voltage, high

noise, high clutter, ineffective STC modulation, and so on. The corresponding fault points of these fault phenomena are shown in Figure 4.
![img-3.jpeg](img-3.jpeg)

Figure 4. Relationship between abnormal IF signal fault phenomenon and fault points.
The power supply is the energy source of the active devices in electronic circuits. The performance of the power supply directly affects the performance of electronic circuits. The power supply can be said to be the "heart" of electronic systems.

The frequency mixer, amplitude and phase corrector, amplitude limiter, frequency synthesizer, RF STC, power amplifier, and filter in the receiver all require electric energy, as well as a variety of power supplies with different voltages and capacities, to work normally.

The power converter is a special device in the radar receiver. It has two functions: voltage transformation and power supply. The external power supply enters the receiver, is transformed into the voltage values required by each component of the receiver through the power converter, and is then sent to each component to supply it with power. One power converter can convert the power supply to several voltage values, and the fault types of the power converter are also diverse. If a failure occurs in one voltage transformer branch of the power converter, the devices in the receiver that require a power supply from the transformer branch will not work. Once the power converter has a functional fault, there is no normal power supply for any of the electronic devices inside the receiver, meaning that the receiver will be in "paralysis", as is shown in Figure 5.

![img-4.jpeg](img-4.jpeg)

Figure 5. Relationship diagram of power converter fault.
By combining Figures 4 and 5, the nodes and directed edges of the Bayesian network can be preliminarily determined so as to determine the Bayesian network model, as is shown in Figure 6.
![img-5.jpeg](img-5.jpeg)

Figure 6. Bayesian network model.
$\mathrm{F}_{1}$ and $\mathrm{F}_{2}$ are two root nodes, which represent "abnormal IF signal output" and "power converter failure", respectively. There are 21 causes that may lead to the $\mathrm{F}_{1}$ phenomenon, which are represented by $\mathrm{E}_{1}-\mathrm{E}_{21}$. The $\mathrm{F}_{2}$ phenomenon will make all components inoperative, resulting in the failure of the IF signal output and thus indirectly leading to the $\mathrm{F}_{1}$ phenomenon. See Tables 1 and 2 for evidence definition and relevant information.

Table 1. Description of faults.


Table 2. Description of evidence nodes.


# 3. Results 

Using the historical monitoring data of the radar, the conditional probability tables (CPTs) of all nodes can be determined in the fault diagnostic network. The prior probabilities of fault nodes $F_{1}$ and $F_{2}$ are shown in Table 3.

Table 3. The prior probabilities of nodes $F_{1}$ and $F_{2}$.


The parent node of the $\mathrm{E}_{1}, \mathrm{E}_{2}, \mathrm{E}_{3}, \mathrm{E}_{4}, \mathrm{E}_{6}$, and $\mathrm{E}_{7}$ events is $\mathrm{F}_{1}$. The parent node of the $\mathrm{E}_{5}, \mathrm{E}_{10}, \mathrm{E}_{11}, \mathrm{E}_{12}, \mathrm{E}_{13}, \mathrm{E}_{14}, \mathrm{E}_{15}, \mathrm{E}_{17}, \mathrm{E}_{18}, \mathrm{E}_{19}$, and $\mathrm{E}_{21}$ events is $\mathrm{F}_{2} . \mathrm{E}_{1}$ has the child nodes $\mathrm{E}_{8}$, $\mathrm{E}_{9}, \mathrm{E}_{10}$, and $\mathrm{E}_{13}$. If any of the child nodes fails, the fault phenomenon represented by $\mathrm{E}_{1}$ is bound to occur.

The failure of $\mathrm{E}_{10}$ and $\mathrm{E}_{13}$ may be caused by $\mathrm{F}_{2}$ power failure. Similarly, if $\mathrm{E}_{17}, \mathrm{E}_{18}$, or $\mathrm{E}_{19}$ fails, $\mathrm{E}_{16}$ and $\mathrm{E}_{4}$ will occur, resulting in $\mathrm{F}_{1}$ failure. By analogy, the posterior probabilities of other events are also extracted according to sample data processing and calculation. The results are shown in Table 4.

Table 4. The conditional probabilities of evidence nodes $\mathrm{E}_{1}-\mathrm{E}_{21}$.


With the calculations of the monitoring data samples and Bayesian network model, the CPTs can be denoted. Under different conditions of $\mathrm{F}*{1}$ and $\mathrm{F}*{2}$, the conditional probabilities of $\mathrm{E}*{1}-\mathrm{E}*{21}$ are different, and the posterior probabilities in the table can be transformed into a more intuitive chart form, as is shown in Figure 7. ![img-6.jpeg](img-6.jpeg)

Figure 7. Conditional probability distribution diagram.

## 4. Discussion

### 4.1. F1 and F2 Sub-Node Evidence

From the previous analysis, it can be seen that if the IF signal output is abnormal or the power converter fails, six fault phenomena will be directly caused; that is, the first layer child of nodes E1, E2, E3, E4, E6, and E7 events of F1 and F2. According to the CPTs, the relevant conditional probability distribution diagram can be obtained, which is shown in Figure 8.

![img-7.jpeg](img-7.jpeg)

**Figure 8.** Conditional probability distribution diagram of the first layer sub-nodes.

In Figure 8, it can be seen that the event probability of node E4 (low signal power) is the highest under any condition of F1 and F2.

Let *P<sub>t</sub>* be the power of the echo signal, *P<sub>t</sub>* be the power of the transmit signal, *G* be the receiving antenna gain, *λ* be the transmitted electromagnetic wave length, *σ* be the radar cross section, and *R* be the distance from the target to the radar. The Radar Equation can be obtained using the following equation:

$$P_r = \frac{P_t G^2 \sigma \lambda^2}{(4\pi)^3 R^4} \tag{2}$$

According to the radar equation, *P<sub>r</sub>* is inversely proportional to *R*<sup>4</sup>. The farther the target that is detected, the weaker the power of the echo signal [42]. This is because the emitted electromagnetic wave will decay rapidly in the transmission process. The electromagnetic wave emitted by the radar is a radio frequency signal with great power, but the signal energy reflected by the target received by the radar is extremely weak and may be only 10<sup>−7</sup>–10<sup>−6</sup> V. This signal can be received by the signal processor only after it is amplified to at least tens of volts. Therefore, whether the echo signal power can be

amplified to a strength that the signal processor can recognize is one of the key methods of testing the performance of the receiver. The all-weather/all-day characteristics of the radar have higher requirements for the stability of the receiver power amplifier. The power gap between the echo signal received by the antenna and the IF signal transmitted to the signal processor is $10^{7}-10^{8}$ orders of magnitude, which requires power amplifiers. Consequently, the failure of power amplifier efficiency to meet the requirements is the most likely cause of an unsatisfactory output signal from the receiver, which is consistent with the result of the maximum probability of node $\mathrm{E}_{4}$ shown in Figure 8.

# 4.2. $E_{4}$ Sub-Node Evidence 

The direct fault cause of $\mathrm{E}_{4}$ (low signal power) evidence is $\mathrm{E}_{16}$ (power amplifier under power). According to a previous circuit analysis, general superheterodyne receivers have the tertiary power amplifier RF LNA for the 1st IF amplifier and 2nd IF amplifier. If any of the three amplifiers fails, $\mathrm{E}_{4}$ (low signal power) evidence will be observed. The power of the echo is weak, but it inherits the high frequency of the transmitted signal. The RF low-noise amplifier is the first station for echo signal amplification. It should not only be able to withstand high-frequency signals but also undertake power amplifier tasks, which are required to suppress the interference of noise to improve the signal-to-noise ratio. Compared with the 1st IF amplifier and 2nd IF amplifier, the RF LNA is the most vulnerable device in the receiver, and it has a higher probability of failure. $\mathrm{E}_{4}$ has four sub-nodes, $\mathrm{E}_{16}-\mathrm{E}_{19}$, which correspond to power amplifier under power, RF LNA failure, 1st IF amplifier failure, and 2nd IF amplifier failure events, respectively. Their conditional probability distributions are shown in Figure 9.
![img-8.jpeg](img-8.jpeg)

Figure 9. Conditional probability distribution diagram of $\mathrm{E}_{4}$ 's sub-nodes.

In Figure $9, \mathrm{E}_{16}$ has the highest probability because it is the direct cause of the low power of the signal. $\mathrm{E}_{17}-\mathrm{E}_{19}$ are the child nodes of $\mathrm{E}_{16}$. Among them, $\mathrm{E}_{17}$ (RF LNA failure) has the highest probability, which is in line with the circuit analysis results.

# 4.3. $E_{6}$ and $E_{7}$ Sub-Node Evidence 

In addition to $\mathrm{E}_{4}$ (low signal power), which is the most likely fault phenomenon, there may also be abnormal output frequency, inconsistent phase, inconsistent amplitude, abnormal control voltage, more clutter, ineffective STC modulation, etc. It can be seen from Figure 8 that, compared with other fault phenomena, the probabilities of $\mathrm{E}_{6}$ (more clutter) and $\mathrm{E}_{7}$ (ineffective STC modulation) are very low and can basically be ignored. It is indicated that the clutter suppression and STC control effect are the best and the possibility of failure is lowest in the receiver. The conditional probability distribution of an RF STC fault is shown in Figure 10, and the conditional probability distributions of the sub-nodes of $\mathrm{E}_{6}$ (more clutter) are shown in Figure 11.
![img-9.jpeg](img-9.jpeg)

Figure 10. Conditional probability distribution diagram of $\mathrm{E}_{5}$ 's sub-nodes.
If the IF signal output is abnormal and the power converter has no faults, the probability of $\mathrm{E}_{5}$ (RF STC failure) is the highest.

The direct cause of more clutter is $\mathrm{E}_{20}$ (insufficient filtering) in the receiver. The filtering effect is basically subject to the three filters in the receiver. Under the same conditions, the failure probability of these three filters is almost the same, and because the probability of $\mathrm{E}_{6}$ is very low, the failure probability of the filter can also be ignored.

## 4.4. $E_{2}$ and $E_{3}$ Sub-Node Evidence

Generally speaking, the probability of an inconsistent phase or amplitude of the IF signal output by the receiver is not high. The probability of these two phenomena will increase only when the power converter fails, and the electronic components cannot work normally. The inconsistent phase and amplitude may be caused by the poor effect of the amplitude and phase corrector and amplitude limiter. The conditional probability distribution of $\mathrm{E}_{2}$ and $\mathrm{E}_{3}$ sub-nodes is shown in Figure 12.

![img-10.jpeg](img-10.jpeg)

Figure 11. Conditional probability distribution diagram of $\mathrm{E}_{6}$ 's sub-nodes.
![img-11.jpeg](img-11.jpeg)

Figure 12. Conditional probability distribution diagram of sub-nodes of $\mathrm{E}_{2}$ and $\mathrm{E}_{3}$.

In most cases, the probability of limiter failure is higher than that of other kinds of failures. When the power converter fails, the probability of amplitude and phase corrector failure increases.

# 4.5. $E_{1}$ Sub-Node Evidence 

In addition to amplifying the echo signal, the main task of the receiver is to reduce the frequency of the echo signal and convert the RF signal into an IF signal through downconversion [43]. The abnormal frequency of the final IF output signal is uncommon. If the frequency is abnormal, it means that the mixing effect is not ideal; mixers and local oscillator signals are the factors that influence the mixing effect. The local oscillator signals come from the frequency synthesizer. The conditional probability distributions of the sub-nodes of $\mathrm{E}_{1}$ (abnormal signal frequency) are shown in Figure 13.
![img-12.jpeg](img-12.jpeg)

Figure 13. Conditional probability distribution diagram of $\mathrm{E}_{1}$ 's sub-nodes.
In the mixing process of the receiver, if the local oscillator signals are abnormal, it will report a fault in the frequency synthesizer and will not enter the mixer without warning. Therefore, compared with the local oscillator signals, the failure probability of the mixer is higher. The mixer is also an electronic device and needs a power supply. In the case of a power converter failure, the failure probability of the mixer is higher.

## 5. Conclusions

This paper provides a Bayesian fault diagnosis method based on multi-source information fusion. This method determines the Bayesian network model by processing and fusing expert experience data, a case library, historical monitoring data, and data obtained from various sensors according to the relationship between fault phenomena and causes, as well as the circuit structure characteristics of the radar receiver. Then, by calculating

the conditional probability of each node, the device that is most likely to cause the fault is output, which proves the effectiveness of this method. This fault diagnosis method optimizes the component level fault alarm (which is completed by BITE at the moment), locates the fault points at the device level, avoids the waste of resources caused by the replacement of a whole piece during radar maintenance, and improves the efficiency and cost ratio of the maintenance process. In the future, the method proposed in this paper will be applied to the status monitoring and fault diagnosis of radar subsystems, such as transmitters, antenna feeders, recording terminal, power supplies, and so on, and the stability and accuracy of this method will be further improved through data collection and analysis.

Author Contributions: Conceptualization, B.L. (Boya Liu); methodology, B.L. (Boya Liu); validation, B.L. (Boya Liu), X.B. and L.G.; formal analysis, X.B., J.W. and L.G.; investigation, L.G. and X.B.; resources, J.W.; data curation, B.L. (Boya Liu) and X.B.; writing-original draft preparation, B.L. (Boya Liu); writing-review and editing, B.L. (Boya Liu); visualization, B.L. (Boya Liu) and L.G.; supervision, B.L. (Boya Liu); project administration, B.L. (Boya Liu); funding acquisition, B.L. (Boya Liu) and B.L. (Baozhong Liu). All authors have read and agreed to the published version of the manuscript.
Funding: The authors would like to acknowledge funding from Hubei Key Laboratory of Intelligent Robot (Wuhan Institute of Technology), grant number HBIR202107.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Informed consent was obtained from all subjects involved in the study.
Data Availability Statement: Not applicable.
Acknowledgments: The authors also thank everyone involved in the project.
Conflicts of Interest: The authors declare no conflict of interest.
