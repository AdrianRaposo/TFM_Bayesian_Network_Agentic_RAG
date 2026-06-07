# Article 

## Communication Fault Maintenance Decision of Information System Based on Inverse Symmetry Algorithm

Qing Li *, Chaoxuan Shang and Zhaorui Li<br>Department of Electronic and Optical Engineering, Army Engineering University, Shijiazhuang 050003, China; scx1207@sina.com (C.S.); 13933011227@139.com (Z.L.)<br>* Correspondence: liqing652@sina.cn

Received: 13 November 2019; Accepted: 23 December 2019; Published: 8 January 2020


#### Abstract

In view of the characteristics of various types of information system integrated hardware and software systems, complex network topology, complex causes of fault alarm and uncertainty, this paper studies the communication fault maintenance decision-making based on the inverse symmetry algorithm. Based on the principle of the inverse symmetry algorithm, the modulation and demodulation process of information system is determined, the redundant system attributes in the information system are reduced by rough set, and the Bayesian network model with minimum diagnosis set is obtained by combining the prior knowledge in the operation process of the information system. The input and output of the network are the condition attributes and decision attributes of the decision table, respectively. Through the above process, the optimal fault diagnosis rules are established. After the communication fault is diagnosed, different communication fault maintenance decisions of the information system are used to eliminate the fault. The experimental results show that this method can effectively diagnose the communication fault of the information system and make effective maintenance decisions. The average accuracy of data transmission of the information system using this method is over $99.5 \%$ under different operating distances, which has better communication performance.


Keywords: inverse symmetry algorithm; information system; communication; fault; maintenance; decision

## 1. Introduction

With the improvement of the automatic operation level of information systems and the development of communication technology, information systems have the ability to transmit and obtain fault information online in the form of data communication. Many institutions have already completed or are building communication protection fault information systems, and many companies have developed corresponding products [1]. As an immature product, the communication fault maintenance system has many problems such as inconsistent traffic regulations, inconsistent data structures, and inconsistent protection information. Classical communication theory usually assumes that the noise in the channel is white Gaussian noise, and most of the current wireless communication systems have artificial noise with strong correlation, whose power far exceeds natural noise [2]. They believe that noise is not subject to Gaussian distribution and has a strong correlation. Using classic theory to analyze modern communication systems will bring large errors. Therefore, it is significant to study the channel model and noise cancellation methods under the noise of communication faults in information systems. The inverse symmetric method (PISM) uses the correlation between band-limited noise and its digital features to eliminate noise. It can extract weak signals from strong noise and greatly improve the signal-to-noise ratio.

At present, there are many kinds of communication methods that can communicate under the condition of small signal-to-noise ratio, such as DSSS (Spread Spectrum), FHSS (Frequency-Hopping Spread Spectrum), etc., but they are all completed under the premise of greatly expanding the bandwidth. Many people in China and abroad are looking for new ways of communication, in order to save bandwidth and communicate in a strong noise environment [3,4]. There are three methods to overcome the strong noise, and all of them can communicate when the SNR (SIGNAL-NOISE RATIO) is less than one. The first is the "spectrum inversion method" proposed by Taylor et al. in October 1979. The second is the "Monett mixing method" proposed by Monett in March 2000. The third is the "anti-relative law" proposed by China, all of which have been patented. The signal submerged in noise can be detected by spectrum inversion, Monett mixing, and anti-relative symmetry. The spectrum inversion method makes use of the uncorrelation of inversion noise and non-inversion noise, while the inverse relative multiplication uses the correlation of band limited noise and its digital characteristics to eliminate noise. Because most channels belong to the constant parameter channel, that is, noise belongs to stationary or wide stationary random process [5], its digital characteristics do not change with time. When we divide the channel in the frequency domain or time domain, the noise between adjacent frequency bands or adjacent time slots has a strong statistical correlation. Both the spectrum inversion method and the anti-relative method can improve the signal-to-noise ratio, but the equipment of the anti-relative method is simpler. Both the Monett mixing method and the anti-relativism method make use of the fact that the noise and the signal are uncorrelated. The Monett mixer can greatly improve the signal-to-noise ratio, and it can display its advantages, especially in microwave communication. The spectrum inversion method is suitable for military wireless communication with double sided pseudo noise signal. The anti-relative symmetry method and Monett mixing method are applicable to aerospace communication and portable mobile communication [6]. These three new methods can make the equipment smaller, lighter, and more energy-efficient, thus prolonging the battery life of cellular mobile phones. All these three technologies are beyond the theoretical upper bound of the Shannon formula and have a very broad application prospect.

In order to make the communication technology reflect the ideal practicability, it is necessary to focus on detailed analysis of various common fault problems. Understanding their common types and basic causes can make processing and control methods more reasonable. It can reduce the possibility of accident threat and increase the application value of communication technology. more reasonable methods and methods for processing control, reduce the probability of accident threats, and promote the application value of communication technology. At present, there is much research on communication faults in information systems. Related scholars have proposed a new scheme that combines fuzzy sets and fuzzy inference methods with fault diagnosis, using fuzzy sets to represent voltage and current characteristic information when faults occur and using fuzzy reasoning to improve the accuracy and availability of diagnostic results. At the same time, a fuzzy set learning platform was developed to alleviate the problem of knowledge acquisition of expert systems. Other researchers use network communication technology to solve system fault diagnosis problems and segment system faults through rule representation, providing decision-making schemes according to human logical thinking rules, which is easy for people to understand. However, this method takes a long time to analyze and has poor real-time performance. The method in [7] optimizes the deployment of near-space communication systems and introduces a multi-objective evolutionary algorithm to segment the internal space of the communication system, obtaining a relatively stable signal through effective partitioning, effectively removing interference, and performing fault location. However, due to the complicated process, the fault location time of this method is long, and the efficiency is not good. Reference [8] proposed an optimization method for fault diagnosis of high-voltage circuit breakers in power supply systems, which diagnosed high-voltage circuit breaker faults through a probabilistic neural network algorithm. The energy of vibration signal is quantified, and the causes and types of faults are analyzed. The method has high accuracy, but this method has poor timeliness.

In order to solve the problem of difficult decision-making of information system fault maintenance, this paper studies the information system communication fault maintenance decision-making based on the inverse symmetry algorithm. This method first realizes the information system based on the inverse symmetry algorithm. Based on this information system, it studies the communication fault diagnosis method and maintenance decision-making and puts forward ideas for the stable operation of the information system.

# 2. Definition of Algorithm 

### 2.1. Principle of Inverse Symmetry Algorithm

The basic idea of the inverse symmetric algorithm (PISM) is to divide the channel in frequency domain or time domain, so that the noise between adjacent frequency bands or adjacent time slots has strong correlation [9-12], and then use the correlation of band limited noise and its digital characteristics to eliminate the noise. The basic principle block diagram of the inverse symmetry algorithm is shown in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. Basic principle block diagram of inverse symmetric algorithm.
In Figure 1, $\mathrm{C}_{1}$ and $\mathrm{C}_{2}$ are two adjacent subchannels, which can be adjacent frequency bands, adjacent time slots, or adjacent space. The so-called "inverse phase" refers to sending two mutually opposite signals, $s_{1}(t)$ and $s_{2}(t)$, into two adjacent channels, $\mathrm{C}_{1}$ and $\mathrm{C}_{2}$ respectively, at the transmitting end, where $s_{1}(t)=-s_{2}(t)=s(t)$. The so-called "symmetry" means that the transmission characteristics of the two channels are basically the same.

In order to simplify the calculation, let the gain of these two channels be one, and assume that they have zero mean additive noise [13], which is recorded as $n_{1}(t)$ and $n_{2}(t)$. If the channel attenuation and delay are ignored, the output of $\mathrm{C}_{1}$ and $\mathrm{C}_{2}$ are respectively.

$$
\begin{gathered}
r_{1}(t)=\sum_{i=1,3,5}^{\infty} \frac{4}{\pi} \frac{\delta}{i} \sin (i \alpha) \cos (i \theta)+n_{1}(t) \\
\mathrm{r}_{2}(t)=\frac{4}{\pi} \frac{\delta}{i} \sin (i \alpha)=\frac{4}{\pi} \frac{\delta}{i} \sin \left(i \alpha_{p} \frac{\pi}{2}\right)+n_{2}(t)
\end{gathered}
$$

where $\sin (i \alpha)$ and $\cos (i \theta)$ are the included angles of corresponding adjacent time slots and adjacent frequency bands respectively, and $\delta$ is the harmonic amplitude. In the process of denoising in frequency domain, the elimination effect of the channel depends on the attenuation power of the subchannel. The signal output result can be calculated according to the following formula.Send them to the subtracter and the total output is:

$$
r(t)=r_{1}(t)\left[\sum_{j=1,2,3}^{\infty} \frac{\sin (j \beta)}{j} \cos (j \theta)\right]-r_{2}(t) \beta S_{o}(t)+n_{0}(t)
$$

$s_{o}(t)$ and $n_{o}(t)$ are the total output signal and noise, respectively. According to the output results, the whole cluster center is obtained, and the average value of training samples in cluster set $\beta$ is calculated. The final basis function center of the RBF (Radial Basis Function) neural network is obtained, and the total output signal power is:

$$
s_{o}=E\left[(2 s(t))^{2}\right]=4 E\left[s^{2}(t)\right] \approx 4 S
$$

In Equation (4), $s \approx E\left[s^{2}(t)\right]$ is the power of single output signal.
The total output noise power is:

$$
\begin{aligned}
& N_{o}=E\left[\left(n_{1}(t)-n_{2}(t)\right)^{2}\right] \\
& =N_{1}+N_{2}-2 \rho\left(N_{1} N_{2}\right)^{1 / 2}
\end{aligned}
$$

In Equation (5), $N_{1}$ and $N_{2}$ are the output noise power of C 1 and C 2 , respectively, and $\rho$ is the correlation coefficient of the two channels of noise. Then, ADMM (Alternating Direction Methodof Multipliers) alternating multiplier method is used to update the center frequency, modal components, and $\theta(\mathrm{t})$ alternately to find the saddle point of the above formula. According to the gradient of demodulation signal, the bandwidth is:

$$
\mathrm{N}_{1}=\frac{N_{0}-\sum_{k=1}^{K} \sin (i \alpha)+\frac{\theta(t)}{2}}{1+2 \alpha(i \alpha-j \theta)}
$$

Suppose that the noise power of two channels is equal, that is to say, substituting in Equation (5) can get:

$$
N_{o}=2(1-\rho) N
$$

According to the above formula, the output SNR formula is as follows:

$$
S_{o} / N_{o} \approx 2 S /[(1-\rho) N]
$$

As the channel gain is one, the total input signal power of the subtractor is $S_{i} \approx 2 S$, and the total input noise power of the subtractor is $N_{i} \approx 2 N$. Therefore, we can get:

$$
S_{o} / N_{o} \approx(2 /(1-\rho)) \cdot\left(S_{i} / N_{i}\right)
$$

The SNR gain of the inverse symmetry algorithm is as follows:

$$
G_{P I S M}=\left(S_{o} / N_{o}\right) /\left(S_{i} / N_{i}\right) \approx 2 /(1-\rho)
$$

The SNR gain is only related to the correlation coefficient of the two noises, but not to the SNR. In the actual communication system, most of the noise meets $0<\rho<1$, so $G_{P I S M} \approx 2 /(1-\rho)>2$.

# 2.2. Implementation of Information Systems Based on the Inverse Symmetry Algorithm 

The modulation process of the information system based on the inverse symmetry algorithm is shown in Figure 2.

![img-1.jpeg](img-1.jpeg)
(a) Upper and lower sidebands separated
![img-2.jpeg](img-2.jpeg)
(b) Folded spectrum shift

Figure 2. The modulation process of the information system.
In Figure 2a, double-sideband modulation is used, and the upper and lower sidebands are separated by two bandpass filters (BPF). Then the lower sideband is inverted, and finally the upper sideband is superimposed into the system shown in Figure 2b. In Figure 2b, a pair of orthogonal pre-carriers causes the lower sideband to fold, while the upper sideband is not affected by low-pass filter (LPF) suppression. A pair of orthogonal carriers are used to move the folded spectrum to the ideal position [14], and then two signals are added or subtracted to complete the modulation process. The demodulation process is the reverse of the above process.

The modulation and demodulation process of the information system based on the inverse symmetry algorithm shall meet the following requirements:

$$
\begin{aligned}
v_{1}=\sin \omega_{2} t \sin \omega_{1} t & =\frac{1}{2}\left[\cos \left(\omega_{2}-\omega_{1}\right) t-\cos \left(\omega_{2}+\omega_{1}\right) t\right] \\
v_{2}=\cos \omega_{2} t \sin \omega_{1} t & =\frac{1}{2}\left[\sin \left(\omega_{2}-\omega_{1}\right) t+\sin \left(\omega_{2}+\omega_{1}\right) t\right] \\
v_{3} & =\frac{1}{2} \cos \left(\omega_{2}-\omega_{1}\right) t
\end{aligned}
$$

$$
\begin{gathered}
v_{4}=\frac{1}{2} \sin \left(\omega_{2}-\omega_{1}\right) t \\
v_{5}=\sin \omega_{3} t \cos \left(\omega_{2}-\omega_{1}\right) t=\frac{1}{2}\left[\sin \left(\omega_{3}+\omega_{2}+\omega_{1}\right) t+\sin \left(\omega_{3}-\omega_{2}+\omega_{1}\right) t\right] \\
v_{6}=\cos \omega_{3} t \sin \left(\omega_{2}-\omega_{1}\right) t=\frac{1}{2}\left[\sin \left(\omega_{3}+\omega_{2}-\omega_{1}\right) t-\sin \left(\omega_{3}-\omega_{2}+\omega_{1}\right) t\right] \\
y_{1}(t)=v_{5}-v_{6}=\sin \left[\left(\omega_{3}-\omega_{2}\right)+\omega_{1}\right] t \\
y_{2}(t)=v_{5}+v_{6}=\sin \left[\left(\omega_{3}+\omega_{2}\right)-\omega_{1}\right] t
\end{gathered}
$$

# 2.3. Information System Communication Fault Diagnosis 

There are many system attributes and fault types in the information system based on the inverse symmetry algorithm. Therefore, the advantages of Bayesian network and rough set are integrated. Removing redundant attributes in the system through rough sets. On this basis, the Bayesian network model with the minimum diagnosis set is obtained by combining the prior knowledge in the operation of the information system [15,16]. The input of the network is the condition attribute of the decision table, and the output is the decision attribute of decision table. Through the above operations, the optimal fault diagnosis rules are established, so as to improve the efficiency and accuracy of diagnosis. The detailed algorithm steps of realizing communication fault diagnosis of information system are shown in Figure 3.
![img-3.jpeg](img-3.jpeg)

Figure 3. Trouble shooting algorithm flow chart.
The specific steps of the algorithm are as follows:
(1) Sort out and analyze the original data of fault records of the system operation, extract characteristic attribute items, combine synonyms and synonyms, and make word frequency statistics.
(2) According to the prior knowledge, a fault decision table including all system attribute values is formed.
(3) Rough set theory is used to reduce the characteristic attribute of the decision table, to form the minimum decision rule set, and to establish the fault diagnosis knowledge base.
(4) According to the word frequency statistics and the number of faults of the characteristic attributes retained in the diagnosis knowledge base, the prior probability information of the characteristic attributes is obtained.
(5) A systematic Bayesian network fault information diagnosis model is established, including the conditional probability or joint conditional probability of all nodes in the network structure with associated relationships, the connection between nodes, the reason node to the intermediate node, and the fault node [17].

Using the communication fault diagnosis model established above, when the information system fault diagnosis is carried out, the probability calculation method of all fault cause nodes is as follows:
(1) Input the result node vector into the Bayesian network.
(2) For each node n that has not been processed in the network, if it has the fact (evidence) of occurrence, mark it as processed, otherwise continue to execute downward.

(3) If one of its child nodes has not been processed, the node will not be processed, otherwise continue to execute downward.
(4) According to the probability of all the sub nodes of node n and the conditional probability or joint conditional probability, the probability distribution of node n is calculated according to the conditional probability formula, and node n is marked as processed.
(5) Repeat (2) to (4) and handle all nodes.

At this time, the probability distribution of each cause node is its probability of occurrence/non-occurrence. According to the probability distribution of the cause node, the failure causes are sorted according to the probability [18]. If the probability is similar, the failure causes are processed according to the parallel events, and then the system attributes corresponding to the failure causes are detected in the information system in order to make the communication failure maintenance decision quickly.

# 2.4. Failure Maintenance Decision 

There are different kinds, phenomena and processing methods of communication faults in the information system based on the inverse symmetry algorithm. The maintenance decisions of different communication faults in information system are summarized as follows.

### 2.4.1. Power Problem

The function of power supply for information systems is critical. There are two kinds of field equipment for information system connection, one is the information system equipment with independent power supply, the other is the information system equipment with bus power supply. For the information system equipment with independent power supply, if the equipment is a network node, the unstable power supply can make the communication of the node appear or even disappear completely, but it has little impact on the key communication equipment of other nodes, and the information system will automatically start the bypass function to avoid the impact on other nodes. For the key equipment [19], such as the repeater, photoelectric conversion module, transceiver, hub, and other equipment, the instability of the power system will inevitably lead to the paralysis of the whole communication system. Therefore, in the case of high reliability and long communication distance, ring topology, multi power supply, or centralized power supply should be considered to isolate the interference of information system. The other is bus power supply equipment, whose power supply is also very important. Power supply problems are often the primary factor of communication system failure. Therefore, in addition to confirming the voltage ripple of the power supply, it is necessary to further confirm whether the voltage of each node reaches the allowable range, and carefully check whether the capacity of the power supply equipment meets the requirements of power consumption of each node, and the power supply in the network communication position cannot be ignored.

### 2.4.2. Medium Problem

Communication media can be a twisted pair cable, coaxial cable, optical fiber, infrared, and laser media, usually twisted pair and optical fiber. For the twisted pair cable, the key troubleshooting factors for communication failure are as follows:
a. Polarity: It is necessary to ensure that the transmission, reception, and other signals of the media signal are connected one by one. Especially for the bus powered information system, the signal also has polarity, and reverse wiring will lead to communication interruption after the signal is reversed.
b. Shielding: The communication network cable screen layer shall be reliably grounded, and the grounding resistance shall be less than 10 N . Especially for systems with different bus equipment grounding points, the cable laying must be single ended grounded [20,21]. It is recommended

to connect multiple cables in the sequence of "shield out—shield person—shield out—shield
c. Grounding: Grounding the signal line of communication medium anywhere will lead to communication failure of the information system. For places with intrinsic safety requirements, the cable shield shall be grounded outside the explosion-proof area and connected to the neutral point of a safety barrier [20-23]. The grounding of the information system shall be separated from the protection grounding of the device, transmission system grounding, and power system grounding.
d. Quality: The cable signal core of each network section shall not be short circuited or open circuited. Short circuit will lead to the interruption of all communication, and open circuits can cause most communication failures. At the same time, the cable impedance shall be generally less than $0.16 \Omega / \mathrm{m}$. Each signal line of the cable shall be well insulated, and the insulation resistance between them shall be greater than $200 \mathrm{k} \Omega$. For important occasions, it is necessary to test the characteristic impedance (recommended: 100 kHz ), electrostatic capacity (recommended: 1 kHz ), withstand voltage ( DC 200 V ), and other parameters of the cable.
e. Terminal resistance: As an impedance matching element, two terminal resistors are required in each network segment of the bus. The purpose of using the terminal resistor is to reduce the signal attenuation and deformation by applying the principle of signal transmitting wave. Therefore, at the head and tail nodes of each network segment, it is important to check whether the connected terminal resistance or the node connector terminal is at the "on" position, and at the same time, other nodes in the middle segment shall not have the terminal resistance or the node connector terminal is at the "off" position.
f. Others: In the information system, the number of repeaters in a bus shall be less than four, and the distance of network transmission shall not exceed the maximum length allowed by the theory of the communication cable used. For the mixed use of various cables, it is necessary to ensure that:

$$
L_{1} / \operatorname{Max}_{1}+L_{2} / \operatorname{Max}_{2}+\cdots+L_{n} / \operatorname{Max}_{n}<1
$$

In Equation (19), $L_{1}, L_{2}$, and $L_{n}$ are the actual lengths of 1,2 , and $n$ segments of the communication cables used; $\operatorname{Max}_{1}, \operatorname{Max}_{2}$, and $\operatorname{Max}_{n}$ are the longest distances allowed by the theory of communication cables used in 1,2 , and $n$ segments, respectively.

For optical fiber and other media signals, the processing of communication fault is similar. Although it is simple and effective to judge the quality of optical fiber by means of a flashlight and other tools, it is not a substitute for special inspection. When troubleshooting, it is also important to check the minimum bending radius of the optical fiber and the quality of the optical joint. It is very important to test the quality of optical cable by using a signal attenuation tester.

# 2.4.3. Device problem 

The failure of the communication master, slave station, and network communication line equipment of the information system will inevitably lead to communication failure. For the master-slave structure, the failure of the master card and program will cause the whole system to crash, while the failure of the slave only stops the communication of its local equipment. For multi master structure, master station fault is also local communication fault. It is also very important for the device failure of the slave card.

### 2.4.4. Parameter Problem

The field bus of the information system meets the OSI/RM (Open system Interconnection/Reference Model) network protocol, which is generally applied to the physical layer and data link layer protocols. At the same time, the user protocol layer of the eighth layer is specially formulated. Therefore, all communication protocols in the whole network must be coordinated. Any node of the bus network with different communication rate settings (not necessarily the same) will cause the system to be

paralyzed, and there cannot be two nodes with the same address in the network. The address range should meet the relevant technical requirements. In addition, the setting of parameters should fully consider the communication medium, network segment, communication distance, and other factors, and the configuration information should also be consistent with the relevant parameters of the actual equipment.

# 2.4.5. Anti-Interference Problems 

The anti-interference ability is embodied in the stability index of the communication system under electromagnetic compatibility, lightning impulse, strong magnetism, vibration, and high temperature shock, which is a comprehensive and complex system problem. In order to improve the anti-interference ability of the communication system, the communication cable and the power cable shall be laid vertically through pipes. For the fault handling of the field bus network, the problem of system interference can be considered when all factors are considered, and the fault cannot be handled. Therefore, in addition to taking effective measures in power supply, grounding, shielding, signal isolation, and other aspects to ensure the card quality and communication parameters are correct, the communication system should also give full consideration to electromagnetic compatibility (such as smelting area), vibration (various driving), and high temperature factors. In addition, the more devices that are connected to the bus and the faster the communication speed is, the heavier the system load is and the worse the anti-interference ability of the system is.

### 2.4.6. Others

Whether the arrangement order of network nodes and the distribution of stations are reasonable or not may affect the network communication. It is also very important for the position of special function nodes (such as with IPD (Integrated Product Development) regulation function) in the network.

## 3. Experimental Analysis

In order to test the effectiveness of the information system's communication fault maintenance decision-making based on the inverse symmetry algorithm, the information system based on the inverse symmetry algorithm is applied to the power information system, which includes dozens of power information systems, dozens of servers, switches, and other information equipment, nearly 2000 km of communication network lines and its ancillary communication equipment. When a subordinate city visits an information system, it is difficult to determine whether it is the communication equipment or the information equipment software and equipment. Taking the access fault of the communication fault in a power information system as an example, this paper uses the diagnosis model to diagnose the fault cause and make maintenance decision.

### 3.1. Failure Cause Node Analysis

First, feature attribute items are extracted from the raw data of the fault records of all information communication systems

The directed connection diagram of three module nodes "information equipment", "communication equipment", and "platform software" when an access failure occurs in a power information system is given, and 15 failure cause nodes corresponding to these three modules are established. The schematic diagram of the communication failure cause node is shown in Figure 4.

![img-4.jpeg](img-4.jpeg)

Figure 4. Schematic diagram of the fault cause node.
Diagnose the communication failure of the information system based on Figure 4. The prior probability of an attribute is the number of times the attribute value appears in the existing fault diagnosis report divided by the sum of all attribute values.

The probability value of each attribute is calculated by using the method of text information statistics. After applying rough set attribute reduction, the minimum attribute set can be obtained, thus the diagnosis rule of the minimum attribute set can be obtained. The minimum attribute set of fault reason reduction is shown in Figure 5.
![img-5.jpeg](img-5.jpeg)

Figure 5. Fault cause reduction minimum attribute set.
According to the statistical analysis of Figure 5, the probability of the minimum attribute set of each fault cause is obtained, and then the probability information of all connecting lines in the Bayesian network is calculated. According to the fault diagnosis model, the probability of the fault being caused by each system attribute is calculated. The attribute with high probability has a high probability of failure, so as to realize the rapid location of failure causes and improve the diagnosis efficiency.

# 3.2. Effectiveness of Fault Diagnosis 

The validity of the fault diagnosis is verified by comparing with the actual operation data. Take five groups of information systems in Table 1 as an example. Where " 1 " indicates abnormal test and " 0 " indicates normal test. See Table 1 for statistical results of test data.

Table 1. Test data statistics.


In the first group of fault test data, abnormal alarms occur in load balancing, SDH (Synchronous Digital Hierarchy), application program, database, and interface program. According to the method in this paper, the possibility of platform software failure is the highest. In the second group of fault test data, abnormal alarms are generated in the host, switch, pigtail, PDH (Plesiochronous Digital Hierarchy), and disaster recovery program. According to the method in this paper, abnormal alarms can be calculated. In the third group of test data, the storage, switch, optical cable, pigtail, middleware, and interface program all send out abnormal alarms. According to the traditional manual judgment method, all system attributes with alarm information need to be searched. In the actual operation process of the power information system, information equipment, communication equipment, and platform software are relatively independent, so it is difficult to determine which group of problems it is according to the manual judgment method. It takes time and effort to find out the cause of the accident one by one. According to the method in this paper, the communication equipment in the third group of fault state is the most likely to fail, and the equipment that fails can be found quickly. In the fourth group of test data that fails, the load balance, optical cable, SDH, application degree, and middleware all send abnormal alarms, and according to the method in this paper, the communication equipment is the most likely to fail; in the same way, in the fifth group of failure test data, many attributes have alarm information. According to this method, we can quickly determine that the communication equipment has the highest failure probability, followed by the platform software. At the same time, according to the result of the attribute reduction of the fuzzy set, load balancing, pigtail, interface program, and disaster recovery program cannot be considered or arranged in the final troubleshooting, which saves time when troubleshooting.

After confirming the specific location of the communication fault, corresponding maintenance decision are made according to different communication fault types, as shown in Table 2.

Table 2. Communication fault repair decision.


From the experimental results in Table 2, it can be seen that this method can effectively diagnose the communication fault of the information system based on the inverse symmetry algorithm, and make the maintenance decision in the shortest time, which verifies the effectiveness of this method in improving the communication performance of the information system.

# 3.3. Effectiveness of Fault Maintenance Decision Methods 

In order to further test the effectiveness of the communication fault maintenance decision-making method of the information system, this method is compared with the binary decision diagram method and the fault tree analysis method, and the comparison of the information system communication situation using the three methods is made. The performance of this method is tested by the average accuracy of data transmission and communication delay of the three methods under different operating distances, and the comparison results are shown in Figures 6 and 7.

![img-6.jpeg](img-6.jpeg)

Figure 6. Data transmission average correct rate comparison result.
![img-7.jpeg](img-7.jpeg)

Figure 7. Communication delay comparison results.
The experimental results in Figure 6 show that the average accuracy of data transmission of the information system using this method to maintain the communication failure decision-making is more than $99.5 \%$ under different operating distances, while the average accuracy of data transmission of the information systems using the binary decision diagram method and fault tree analysis method is only $98.5 \%$ under different operating distances. The experimental results show that the information system using this method to maintain the communication failure has better communication performance.

The experimental results in Figure 7 show that the data transmission delay of the information system using this method to maintain the communication failure decision-making is less than 50 ms under different action distances, while the data transmission delay of the information systems using the binary decision diagram method and the fault tree analysis method under different action distances is at least 78 ms and 80 ms , and the data transmission delay is an important index to evaluate the performance of the information system. The results show that the information system using this method to maintain the communication failure decision-making has better data transmission performance.

It can be seen from the results in Figures 6 and 7 that the method in this paper can effectively improve the average accuracy of information system data transmission under different operating distances and reduce the communication data transmission delay.

# 4. Discussion 

The inverse symmetry algorithm is a good noise suppression method through theoretical analysis and practical verification, which can improve the quality of communication systems to a large extent, and is a good treatment for the increasingly tense communication environment. It is a good method to extract weak signal from strong noise, and it is easy to realize. Through the inverse symmetry algorithm and noise correlation, the noise correlation coefficients of adjacent time domain, frequency domain, and spatial domain are measured quantitatively, which has attracted the attention of scholars in China and abroad. In this paper, the algorithm is applied to an information system and has achieved good results, effectively improving the anti-noise performance of the information system.

With the progress of science and technology, human life has become inseparable from information transmission. This paper analyzes the common failures of information system communication and their causes, in order to provide the basis for further development of information systems.

### 4.1. Hardware Failure of Information System and Its Causes

### 4.1.1. Line Fault and Its Causes

In the practical application process of information system communication technology, the specific line is one of the core aspects. Reasonably arrange the production line to obtain the ideal value in actual operation, so as to ensure that its follow-up application value is reflected, and the problems in this line aspect must be a greater threat. Based on this kind of line fault analysis, it is mainly due to the obvious aging and damage of communication lines, which will inevitably affect the stability effect of power supply, and also have a more obvious threat and impact on data transmission [24]. There are many reasons for this kind of line damage. In addition to the erosion or damage caused by the unreasonable external environment, the human impact is also a more common aspect. Because of the instantaneous high voltage or low voltage in the power supply process, the stability of the line itself may also be affected, resulting in obvious line failure.

### 4.1.2. Port Failure and Its Causes

For the effective application and layout of information system communication technology, the computer port can be said to be an important part. If there is a problem with this computer port, it is easy to cause the communication to fail, and the transmission of information data presents a more obvious threat [25]. Combined with the problem of port failure in this computer network communication technology, the main problem is port pollution, which can easily result in a more obvious transmission problem. This kind of port pollution problem is mainly due to the use of different ports for mixed use, which leads to the information system not being able to communicate normally, and finally forms a large interference. In addition, in the specific layout of the port, the application of the corresponding crystal head is unreasonable, which will bring more obvious problems and a greater threat.

### 4.1.3. Module Failure and Its Causes

In the specific arrangement of information system communication technology, the problem of hardware failure is also reflected in the specific operation of the module. Although the probability of such module failure is relatively small, the threat is relatively large. Once there is a threat of loss in this area, it will easily affect its overall improper operation, bring serious economic losses, and even cause information leakage [26]. Based on the occurrence of this kind of module fault, the causes are also various, such as voltage instability of the whole system, or a problem in the switch, or even the destruction of human factors, which may affect the operation effect of the module, and the resulting threat is more prominent.

# 4.1.4. Other Hardware Faults 

For the operation of information system communication technology, the problems in hardware are also reflected in many small hardware aspects. For example, a circuit board is a common basic element, and the causes of its failure are also diverse. For example, the short circuit problem of circuit board, or the humidity of its own environment, may affect the operation effect of the circuit board. This will also form a more obvious threat, leading to the formation of circuit board defects, and ultimately affect the orderly operation of the entire computer network communication technology. In addition, for the laying and operation of some basic cable structures, if there is any damage, it will also lead to the damage of the working fluency of the whole system, and the threat brought by it is also relatively prominent.

### 4.2. Information System Software Failure and Its Causes

### 4.2.1. Switch Failure and Its Causes

The application failure of information system communication technology is also closely related to the software system, in which switch failure is relatively common. The switch system failure is mainly due to the software operation of the corresponding switch not being smooth, which can easily cause a greater threat to the application of information data [27]. For this reason, it is necessary to comprehensively strengthen equipment maintenance, reduce various hidden dangers, and avoid data loss.

### 4.2.2. Configuration Failure and Its Causes

In the application process of information system communication technology, the probability of configuration problems is relatively high, and the performance of this configuration problem is also multifaceted, which has a close relationship with many system links and needs to be paid more attention. The problems in this configuration are mainly closely related to the relevant management personnel, because there are obvious mistakes in the operation of the management personnel, which will affect the operation effect of the relevant software systems, such as the current common unreasonable VLAN (Virtual Local Area Network) division and improper setting of the end port, which may bring a greater threat.

### 4.2.3. Password Faults and Causes

The related problems existing in the operation of information system communication technology are also reflected in the application of passwords, because the settings of passwords are unreasonable, or the failure defects caused by the loss of passwords are relatively obvious, so it is easy to cause the occurrence of large defect failures, even the threat of information loss, which also needs to be paid enough attention. Combined with the failure of this kind of password, it has a close relationship with the relevant configuration of the whole system, especially in the setting of the link to retrieve the password, it is more likely to cause problems and affect the orderly operation of the system.

### 4.3. Information System Communication Technology Troubleshooting Measures

### 4.3.1. Daily Maintenance of Hardware Equipment

For the effective use of information system communication technology means, the fault problems shown are various [28]. In view of the defects and faults in hardware, we must focus on strengthening daily maintenance and repair, so as to effectively prevent the related problems, timely detect the generated threats and control the degree of loss. In the process of daily maintenance and management of hardware equipment, first of all, we should ensure that it has an ideal comprehensive effect and can focus on all the hardware components of the entire information system in an all-round way. In this way, we can better solve all kinds of potential problems and promote the operation of related hardware

in a more reliable and orderly manner, especially for the more critical network cables. The common components such as computer equipment and switch equipment need to be checked and replaced regularly, so as ensure they have ideal working conditions and avoid possible big threats. In addition, the daily maintenance of such hardware equipment also needs to focus on relevant organizational arrangements, conduct timely inspection and analysis around the corresponding management and monitoring objectives whether there are obvious corrosive problems and damage phenomena, so as to prevent and deal with failure problems, strangle all kinds of hidden dangers in the cradle state, and avoid the formation of large losses. Finally, in the maintenance and management of hardware equipment, we need to pay attention to the introduction and update of all kinds of new equipment, so as to promote the corresponding computer network communication system. It is reliable and efficient to realize the maximum value.

# 4.3.2. Improve the Security System 

Combined with the effective application of information system communication technology, in order to better improve its running fluency and reliability, it also needs to focus on the continuous updating and improvement of the software system, so as to ensure it has the ideal security and integrity effect and solve various possible loopholes or unreasonable configuration problems. In view of all kinds of security threats existing in the application of the above information system communication technology, it is necessary to ensure that its security assurance system is more comprehensive and appropriate, and is able to be continuously updated and maintained. It fills in all kinds of potential security vulnerability threats, does a good job in the maintenance and repair of network security, and makes its overall operation smoother. In addition, in order to better improve the effect of its security, we can also effectively strengthen it with the help of firewall technology, so that the application of firewall technology can form an ideal security effect in the whole network environment, realize the comprehensive coverage and effective separation of the information system, and avoid the possible threat and interference. With the continuous innovation and development of current software technology, in order to better improve the security and guarantee effect of communication, the reasonable use of encryption technology is also an important part, which can realize the encryption protection of key information, avoid the threat of some information leakage or theft, and finally improve the communication security level of information systems.

## 5. Conclusions

At present, there are many methods for the maintenance of communication faults. The role of oscilloscopes, network analyzers, and multimeters should be brought into full play during the processing of communication faults. Domestic information system communication generally uses the number of failures during the assessment period as the assessment index. There is no rigorous system testing method to evaluate the communication capability of information systems, which cannot effectively reduce the probability of communication failures. Therefore, in the occasions where communication is very important (such as for blast furnaces, power plants, chemical industries, etc.), users of various enterprises should carry out in-depth information system communication restoration capabilities, security, strength, and performance testing when they are put into operation. They should also require system integration and suppliers to provide relevant test methods, and analyze in detail the replaceability, maintainability, scalability, load rate, fault conditions, and exception handling of communication systems. This is very helpful for the daily maintenance and troubleshooting of information systems.

This paper studies information system communication fault maintenance decisions based on reverse symmetry algorithm and establishes an information system based on the reverse symmetry algorithm. The advantages of Bayesian networks and rough sets are integrated to effectively diagnose communication faults in information systems and take effective maintenance decision-making measures for communication faults. The following conclusions are reached through simulation experiments:

(1) The method in this paper has lower fault detection time and higher detection efficiency. This is because this method will order the faults of load balancing, pigtail, interface program, and disaster recovery program based on the fuzzy set attribute reduction results. This method saves time in troubleshooting.
(2) By adopting the method in this paper, the communication fault maintenance decision of the information system can effectively improve the average accuracy rate of data transmission of the information system under different working distances, and reduce the delay of communication data transmission.

To sum up, the method in this paper has good performance, low communication data transmission delay, accurate fault detection results, and can give reasonable decision-making methods.

In addition, the inverse symmetry algorithm can also be applied to the network's physical system security and smart city information communication with little change, which will be further studied in the future. At the same time, improving the accuracy of fault maintenance and realizing the intelligent decision system will be the research goal of the future method.

Author Contributions: In this paper, an information system is established based on the inverse symmetry algorithm; the advantages of Bayesian network and rough set are combined to effectively diagnose the communication failure of the information system. Establish optimal fault diagnosis rules, use fault maintenance decisions of information systems to eliminate faults, and effectively improve the communication performance of information systems. This method can effectively diagnose the communication failure of the information system and make effective maintenance decisions. The average accuracy of data transmission under different working distances is more than $99.5 \%$, which has superior communication performance. Q.L. and C.S. completed the method and concept parts of this article. Q.L. and Z.L. review the experimental analysis of this article. Q.L., C.S. and Z.L. jointly completed the writing of the article. All authors have read and agreed to the published version of the manuscript.
Funding: This research received no external funding.
Conflicts of Interest: The authors declare no conflicts of interest.
