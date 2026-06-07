# Article 

## Cybersecurity in Automotive: An Intrusion Detection System in Connected Vehicles

Francesco Pascale ${ }^{1, *}$ (D), Ennio Andrea Adinolfi ${ }^{2}$ (D), Simone Coppola ${ }^{2}$ and Emanuele Santonicola ${ }^{2}$

check for updates

Citation: Pascale, F.; Adinolfi, E.A.; Coppola, S.; Santonicola, E. Cybersecurity in Automotive: An Intrusion Detection System in Connected Vehicles. Electronics 2021, 10, 1765. https://doi.org/10.3390/ electronics10151765

Academic Editor:
Krzysztof Szczypiorski

Received: 18 June 2021
Accepted: 21 July 2021
Published: 23 July 2021

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (0)

Copyright: (c) 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Department of Energy, Polytechnic of Milan, 20156 Milan, Italy
2 Department of Industrial Engineering, University of Salerno, 84084 Fisciano, Italy; eadinolfi@unisa.it (E.A.A.); simo992simo@gmail.com (S.C.); santonicolaemanuele@gmail.com (E.S.)

* Correspondence: francesco.pascale@polimi.it

Abstract: Today's modern vehicles are connected to a network and are considered smart objects of IoT, thanks to the capability to send and receive data from the network. One of the greatest challenges in the automotive sector is to make the vehicle secure and reliable. In fact, there are more connected instruments on a vehicle, such as the infotainment system and/or data interchange systems. Indeed, with the advent of new paradigms, such as Smart City and Smart Road, the vision of Internet of Things has evolved substantially. Today, we talk about the V2X systems in which the vehicle is strongly connected with the rest of the world. In this scenario, the main aim of all connected vehicles vendors is to provide a secure system to guarantee the safety of the drive and persons against a possible cyber-attack. So, in this paper, an embedded Intrusion Detection System (IDS) for the automotive sector is introduced. It works by adopting a two-step algorithm that provides detection of a possible cyber-attack. In the first step, the methodology provides a filter of all the messages on the Controller Area Network (CAN-Bus) thanks to the use of a spatial and temporal analysis; if a set of messages are possibly malicious, these are analyzed by a Bayesian network, which gives the probability that a given event can be classified as an attack. To evaluate the efficiency and effectiveness of our method, an experimental campaign was conducted to evaluate them, according to the classic evaluation parameters for a test's accuracy. These results were compared with a common data set on cyber-attacks present in the literature. The first experimental results, obtained in a test scenario, seem to be interesting. The results show that our method has good correspondence in the presence of the most common cyber-attacks (DDoS, Fuzzy, Impersonating), obtaining a good score relative to the classic evaluation parameters for a test's accuracy. These results have decreased performance when we test the system on a Free State Attack.

Keywords: cybersecurity; automotive; Bayesian network; intrusion detection system; CAN-bus; Internet of Things; embedded systems

## 1. Introduction

Modern vehicles are considered smart objects of an IoT ecosystem [1]. Automated and connected vehicles have a complex architecture, as they integrate multiple automated driving functions and a wide variety of communication interfaces [2,3]. An external attack can compromise these functions, not only endangering the safety of motorists, but can have repercussions in the privacy, financial and operational aspects of companies and passengers. Consequently, increased vehicle connectivity increases the potential risk of cyber-attacks [4].

To integrate a safety assessment into connected and automated vehicle prototypes, it is necessary to ensure that threats to the security and privacy of drivers, business models and the operator's intellectual property are well countered [5-7]. An IoT security assessment of automated vehicles allows manufacturers to do the following:

- Strengthen interest in automated vehicles, demonstrating that security risks have been mitigated, the concept of cyber security has been validated and verified, and systems have been systematically tested.
- Protect motorists and manufacturers by ensuring that cybersecurity threats are handled following state-of-the-art standards and best practices.
- Develop safe and state-of-the-art AV technologies by ensuring that the automated guidance systems adopted are developed with security-by-design and defense-indepth in mind.
- Gain a competitive advantage by collaborating with international experts who have up-to-date knowledge on information security, vulnerabilities, and applicable standards.
Today, after various attempts to analyze the problem and find a remedy, the ISO 21434 standard has been introduced: this new standard represents an effort aimed at strengthening the culture and presence of cybersecurity within companies involved in automotive product development. It also integrates the cybersecurity process into existing safety processes, especially in the impact assessment and software development process. ISO 21434 sets the clear objective of ensuring that all major players in the automotive sector, be they vehicle manufacturers (so-called OEMs) or component suppliers (so-called TIERs), are aware of the importance of cybersecurity in the development process of products, creating what is called the "security by design" approach [8].

Taking into account the issues outlined above, a framework aimed at cybersecurity should, therefore, foresee different aspects of the life cycle of a connected vehicle, focusing in particular on the following $[9,10]$ :

- Continuous vulnerability management: defining authorized channels for firmware and application updates that restrict the perimeter of attack.
- Security maintainability: if we want to refer, for example, to the cryptographic protection of data, it is unlikely that the keys and algorithms adopted in the initial phase will guarantee the same level of protection over time. For this reason, Security-by-design must be associated with a modular development approach that allows the creation of products capable of adapting to emerging threats.
- Cybersecurity evolution: from this point of view, it is useful to refer to the experience gained by the aeronautical industry, where the use of partitioned embedded systems and domain segregation have made it possible to achieve particularly high security standards.
- The definition of a chain-of-trust, from the prototyping of the individual components of a vehicle, and the system that drives it, to the cloud infrastructure used for data exchange and communications. Solutions based on distributed technologies and blockchain can provide a fundamental contribution in the certification of the phases that participate in the production chain and in the dynamics of the supply chain.
- The implementation of interfaces dedicated to the sector that refer to specialized security policies. The need to develop such countermeasures is accentuated by the frequent use of technologies borrowed from other sectors, such as OTA and bluetooth connections.
In this work, it is proposed an intrusion detection system capable of analyzing traffic over the CAN-Bus and of understanding whether the messages that transmit over the communication channel are malicious or not. After extracting this information status, a two-step algorithm for identifying possible attacks is used: in the first phase, the parameters of the various ECUs of interest are analyzed, comparing them with spatial and temporal analyses that identify possible anomalies in the values. If positive, through the use of Bayesian networks, it is possible to calculate, through a process of inference, the probability that the combination of messages present over the bus represents an anomalous state given by a possible cyber-attack.

In this article, we want to analyze a subsystem of the onboard network as a case study. In particular, we focus on some units highlighted by experts as critical to the vehicle's correct functioning. In fact, the aim is to have a preliminary analysis of the possible use

of these methodologies inside the connected vehicles [11]. The paper is organized in the following way: In the next section, some related works are presented. After, we discuss the backgrounds of cybersecurity in IoT, machine learning and Bayesian networks, and finally, the automotive sector and CAN-Bus. The next section presents our case of study and follows the proposed approach. Finally, some experimental results are discussed with conclusions.

# 2. Related Works 

With the advent of technology, the automotive sector is progressively equipping vehicles with new features, which were unimaginable a few years ago. In the immediate future, the main news will be linked to the connectivity of such vehicles and the raising of autonomous driving levels based on them. It is estimated that by 2022, new vehicles will be connected and capable of communicating with each other [12]. Nowadays, many connected vehicles exchange information via APIs, Wi-Fi, or ad hoc cloud systems. However, each new communication channel opens up new vulnerabilities, particularly toward what underlies the entire vehicle functioning, that is, the internal network [13,14]. In fact, internet access exposes vehicles to greater possibilities of cyberattacks, increasing the entire system's vulnerability. The reasons behind a cybersecurity attack could be numerous and different from each other. An attacker could, for example, smuggle personal information, monitor a person's movements, and, in the worst case, take remote control of the vehicle. In detail, the internal network of modern vehicles, called CAN-Bus, is composed of about 70 nodes. Each node corresponds to an ECU responsible for controlling a specific vehicle component, such as windows, ventilation system, or engine [15,16]. The ECUs communicate in broadcast mode through an unencrypted communication channel called CAN-bus. If an attacker could access them, the entire vehicle's security would be compromised [17,18]. Securing the CAN-bus problem has been known for some time and has already been addressed in various ways, all somewhat effective but not efficient in terms of performance. Many proposals in the literature aim, in fact, to redesign the CAN standard, making a sort of evolution, both on the hardware and the software side. This type of solution, especially regarding the hardware side, does not ensure the vehicles' already marketed safety since it would be necessary to update all the components involved in communications within the vehicle, from the ECU to the cables [19]. Other approaches aim to create intrusion detection systems by potential attackers. In this case, however, the required computational power exceeds the capacity of the microcontroller of today's vehicles. According to the need to keep the amount of information exchanged unchanged, the low computational capacity does not consider MAC-based solutions [20]. Another exciting work introduces a novel algorithm to extract the CAN bus's real-time model parameters and develop SAIDuCANT, a specification-based intrusion detection system (IDS), using anomaly-based supervised learning with the real-time model as input [21]. Some recent studies have analyzed cyber risk from IoT and existing cyber risk assessment approaches and advancements in IoT cyber risk assessment with artificial intelligence and machine learning [22,23]. Other interesting works are related to vehicle mobility and its management [24,25].

## 3. Backgrounds on Cybersecurity in IoT, Bayesian Networks and Information Security in Automotive

In this section, the principles of security in IoT are illustrated and then specified in the automotive world, with particular attention to intrusion control systems based on probabilistic approaches.

# 3.1. Cybersecurity in IoT 

With the advent of IoT in daily life, the number of vulnerabilities has increased, as has the risk of cyberattacks. In the literature, attention has been paid to the principles and models on which IoT applications are based. At the same time, issues relating to privacy and security have only been treated in a generic way [26-28]. Firstly, the problem of the heterogeneity of devices must be considered. In fact, with the advent of many smart objects connected to the network, we move from the protection of individual computers to the protection of several different devices, built by various manufacturers and each with its level of security. Even if most devices are designed with particular attention paid to safety (which, in reality, often does not happen), few with a few vulnerabilities would be enough to bring down the entire structure. In addition, in many cases, devices must always remain connected, so a possible attacker could launch an attack at any time [29]. Since the IoT security problem has been considered relatively recently, there is no valuable empirical data repository or signatures on the attacks already made.

Furthermore, in IoT applications, the difference between safety and security is very blurred. In general, the concept of "security" indicates the security of data and IT systems; the concept of "safety" indicates physical objects and people's safety. Until now, these two concepts have been separated. Another critical problem concerns user privacy; privacy threats could come from possible attackers and the companies that manage the IoT market. IoT devices, in fact, have become part of daily life in a too pervasive way and collect a large amount of information about people, such as habits, tastes, health, etc. This information can be used both by companies (for example, to profile users) and by hackers with malicious purposes [30]. In order to study effective countermeasures, it is necessary to create a taxonomy of possible attacks. It is possible to group attacks based on possible vulnerabilities present in the three levels of the generic architecture of an IoT application with a perception layer (the bottom layer of the IoT architecture; it interacts with physical devices through smart devices, for example, RFID, sensors, actuators, etc.), network layer (the layer in the middle that is responsible of information transmission) and application layer (the layer on the top of the architecture of IoT. It receives data transmitted from the network layer and uses these data to provide required services or operations) [31-34]:

- Theft or damage of device: (perception layer) physical damage to the device.
- Side-channel attacks: (perception layer) collect information on the running time, power consumption, electromagnetic radiation, or sounds produced by a device during the execution of a particular task to deduce information contained in the device memory;
- Fake Node attacks: (perception layer) inserting into the network nodes created by the attacker in order to transmit bogus information or consume the resources, in terms of energy, of the legitimate nodes;
- Replay attacks: (perception layer) after having intercepted authentic credentials of a node; an attacker then sends them back to the recipient simulating the identity of the issuer;
- Node Tampering attacks: (perception layer) replace part of the node hardware or firmware with components created by the attacker and equipped with malicious functions;
- Jamming attacks: (perception layer) consists, if the nodes communicate via wireless protocols, of disturbing the frequencies used by the protocol;
- Denial-of-Service (DoS): (network layer) its purpose is to prevent reaching the nodes via the network. To achieve this goal, it is possible to use many techniques, such as sending a large number of bogus packets on the network to make sure that the various nodes have more information in input than they can process (flooding), compromising a node in the network in order to modify its topology and degrade its performance (sinkhole attack);
- Man-in-the-middle: (network layer) consists of intercepting the data transmitted by the various nodes before they arrive at the recipient to steal them or retransmit a modified version;

- Storage attacks: (network layer) consist of modifying user information in the device memory or in the cloud;
- Routing attacks: (network layer) a class of attacks (the sinkhole attack is an example) in which an attacker tries to alter the information that the devices use to route packets to create loops, to send error messages, or to lose packets;
- Cross-Site-Scripting (XSS): (application layer), which uses client-side scripting languages (for example, JavaScript) to execute malicious code through a browser that shows a specific web page. This type of attack is also exploited in the IoT field because embedded devices often use web interfaces for configuration, more particularly in this case, we speak of Cross-Channel-Scripting (XCS);
- Malicious Code: (application layer) inject malicious code (malware) into the application for it to execute it;
- Credential theft: (application layer) in order to impersonate legitimate users. This layer can be accomplished through eavesdropping, man-in-the-middle attacks, brute force or dictionary attacks (to try to guess credentials), etc.
Just as the attacks are combined to achieve a goal, the various countermeasures must be combined to hinder the attacker in order to attack as lengthily and expensively as possible. To avoid device damages or violations, a series of actions, which do not necessarily include the use of advanced technologies, can be used [35,36].


# 3.2. Bayesian Network 

A Bayesian network is a probabilistic graph that predicts the dependency relationships between a set of random variables through a probabilistic inference process (using the unit of Bayes' theorem). A Bayesian network can be represented graphically through a direct acyclic graph (direct acyclic graph or DAG), i.e., a graph with oriented arcs and without direct cycles. Each node of the graph is associated with a random variable that can take on various states. The latter, which must be mutually exclusive, is associated with a probability value. The arcs that connect two nodes, on the other hand, indicate a relationship of conditional dependence between the latter. In this case, the node from which the bow starts are called the "parent node", while the node to which the bow points is called the "child node". If two nodes are not connected, they are conditionally independent. Nodes that do not have parents are associated with a priori probability tables that express previous knowledge on the value that the random variable associated with the node can assume. The nodes that have at least one parent, on the other hand, are associated with a conditional probability table (CPT), which contains the probabilities that the states of the node can assume to be conditioned by the possible combinations of the states assumed by the parent nodes. The application areas are innumerable and range from decision support systems to monitoring and diagnostics systems. As seen above, many research works focus on the importance of Bayesian networks in critical systems, as they allow understanding how our network has "reasoned" to obtain a result. It turns out to be crucial for Explainable AI, as, unlike neuronal networks and machine learning and deep learning algorithms, these can provide the modalities that were used to obtain a result.

### 3.3. Information Security in Automotive

The problems previously exposed for a generic IoT application are also valid for the automotive world, in fact, as it has already been said that cars have become, in all respect, smart objects. In this case, there is the problem of the heterogeneity of the devices. To be able to implement all the services in the V2V and V2I areas, many network interfaces are required [37,38]. These interfaces can be divided, according to the range of action:

- Physical access points: allow direct or indirect physical access to the car's internal network (USB, OBD, etc.).
- Short range access points: allow communication with the vehicle at a distance that generally varies from 5 to 300 m . Interfaces such as Wi-Fi, bluetooth, remote keyless entry (RKE), tire pressure monitoring system (TPMS), etc., are part of this class.
- Long range access points: allow communication with the vehicle at a distance greater than 1 km . Its groups interfaces include cellular networks (4G, 5G), global positioning system (GPS), etc.
All this involves an increase in the attack surface and represents a severe problem also because the many ECUs on board the car that offers specific services must necessarily dialogue. Even the countermeasures adopted in the automotive sector and the problems that make their implementation difficult are similar to those already described for the IoT world [39-41]. For example, to solve the CAN protocol's security problem, it is possible to proceed in various ways: with the use of encryption, access control, an authentication system, or an intrusion detection system.


# 3.3.1. Encryption, Access Control and Authentication Systems 

Encryption allows to "obfuscate" data to only be read by the user for whom it is intended. This allows the implementation of systems that guarantee the confidentiality and integrity of data to counter attacks, such as Man-in-the-Middle, Storage Attack, Node Tampering, etc. Two types of cryptography can be distinguished: symmetric and asymmetric. In the first case, the key used to encrypt the message is the same as that used to decrypt it; in the second case, different keys are used to encrypt and decrypt the message. However, many of the cryptographic methods currently used require many resources that, as already mentioned, are not available in IoT nodes. In applications with particularly stringent real-time requirements, the use of cryptography would introduce too-high delays. For these reasons, light cryptographic algorithms have been implemented (elliptical cryptography, a type of asymmetric cryptography), which are less robust but still able to hinder possible attackers. Asymmetric encryption also allows signing a message since the data encrypted with one of the two keys can only be decrypted with the other; thus, it is possible to be sure that the sender has the key used to encrypt. However, there is no information on the sender's identity; this identity is ascertained (always through mechanisms based on asymmetric encryption) by a third party called the certification authority (CA). Implementing authentication and access control systems is particularly important to ensure that only legitimate users or nodes can interact with each other. It is used to face attacks, such as Fake Node, Sybil Attack, etc. As for the authentication of users in the literature, it is proposed to use multi-factor authentication, using, in a combined way, a password, biometric characteristics, smart cards, or physical keys. The authentication between nodes is proposed to use systems based on digital signatures, pre-shared keys between devices, and devices created specifically to act as a certification authority [42,43]. In the literature, there are many works on this subject [44-48]. Another important countermeasure is the message authentication code, a critical cybersecurity measure in the current automotive industries. This type of data authentication method is already used as some industrial standards, such as AUTOSAR.

### 3.3.2. Intrusion Detection System

An intrusion detection system (IDS) is a hardware and/or software system that aims to detect any set of actions that aim to compromise the confidentiality, integrity, or availability of a resource. These systems can be classified into two types, based on the strategy adopted to detect intrusions:

- Signature detection based in which the collected data are compared with traces of already known attacks looking for a correspondence that confirms the fact that there is an attack in progress;
- Anomaly detection based, by which the system's behavior is monitored by checking that its methods of use do not deviate from the regular use.
The first class is very effective against attacks that are already known and well modeled, but it is difficult to recognize new attacks unless it receives costly updates. The IDS belonging to this class comprises rules-based systems, such as expert systems, systems based on fuzzy logic, etc. The second class of IDS, on the other hand, is more likely to detect attacks that are not known a priori but generally have less accuracy. Neural networks, systems based on genetic programming, Bayesian networks, etc., can be used for implementation. In general, to obtain good performance, it can be useful to use a hybrid approach of those described. In the IoT field, the use of IDS is problematic due to the considerable resources required by these systems and the absence of a good number of well-modeled attacks, making it challenging to implement systems belonging to the first class. To solve this latter problem, however, in recent years, many researchers have tried to implement honeypots to obtain and analyze more data [49].


# 4. The Proposed Approach and Methodology 

In this section, the proposed approach is shown. Starting from the case study, in this part are shown what the particular cases deal with in the chosen context.

### 4.1. Case of Study

Once the threat model and the risks associated with it have been identified, a system is devised to mitigate these dangers and test them. Using a two-step detection algorithm that exploits both the variation of the status parameters of the various ECUs over time and the Bayesian networks, it can identify a possible attack. First of all, we have to analyze the domain to understand the parameters and their related ECUs that must be taken into consideration to map the vehicle and all the possible cyber risks associated with it. To obtain the actual conditions of a possible attack on the vehicle, the conditions were defined in which one can be in the presence of a specific attack. In particular, as we will see in the next section, the parameters that, combined, can identify a possible attack situation were identified. We must define the application domain through ontologies. Subsequently, the reference system's architecture was defined as well as the parameters considered for the definition of our case study. Therefore, to identify our application domain, we referred to various reference ontologies in the automotive sector. Among the various ontologies to which we referred, we considered those made available by the Automotive Ontology Community Group, the W3C working group and a group of domain experts of University of Salerno. Other reference ontologies taken into consideration were those present in the research in [50-52]. Once the context was identified, it was necessary to define the taxonomy of a car to identify the characteristics of the system and the identification of the parameters to be monitored. Domain ontologies were then analyzed in order to identify the characteristic parameters and the relationships between them. Figure 1 shows the obtained taxonomy:

![img-0.jpeg](img-0.jpeg)

Figure 1. Obtained taxonomy from domain analysis.
Starting from the analysis of the taxonomy, we have taken into consideration these parameters as being of interest for our case study: RPM, throttle, brake, steering, gears, speedometer, radiator, lidar, and lines. These parameters give us the possibility to evaluate the vehicle dynamics and the conditions of a possible attack. From there, it is possible

to trace the values of speed, acceleration, engine temperature, steering, and presence of obstacles that allow us to understand whether or not we are in the presence of one of the possible attack conditions contemplated. At this point, it is necessary to define the architecture of the reference system. Figure 2 shows the architecture.
![img-1.jpeg](img-1.jpeg)

Figure 2. Proposed architecture.
Through the use of a system on a chip (SoC) connected through a transceiver can to the OBDII port, it is possible to create an embedded intrusion control system (EIDS) capable of analyzing the flow of data present on the vehicle and detecting if there are any cyber-attacks. The system, as we will see later, uses a two-step algorithm where there is first a temporalspatial analysis and then a probabilistic analysis carried out starting from a reference data set. The architecture then provides for the possibility of any future subsequent analysis through a connectivity module that allows interaction with, for example, an external cloud. For this analysis, as we will see later, an experimental data set was implemented starting from a simulated environment and this was then compared with other data sets present in the literature.

# 4.2. Two-Steps Algorithm 

In order to decode a possible attack, a two-step classification algorithm was developed. The algorithm thus conceived works as follows:

- The first step, called pre-processing, analyzes ten state frames (containing each frame the exact values of each car parameter considered for our case study, tab). Moreover, it verifies through spatial and temporal analysis obtained from an analysis of the problem whether it may or may not be a possible attack in that sequence of values. Each status frame is recorded with a unique timestamp, and its recording takes place every 4 ms .

- In the second step, through the use of a Bayesian network, previously trained through a pre-established data set during the simulation phase, it can decide whether we are in the presence or not of an attack, keeping in mind both the parameters that make up the frame values status, and the parameters obtained as information from these parameters.
Figure 3 shows the operating framework of the algorithm proposed. Let us now analyze in detail the two steps of the proposed algorithm.
![img-2.jpeg](img-2.jpeg)

Figure 3. The matching process of two-step algorithm.
As mentioned, the raw information that comes from the state of the system is analyzed. To do this, all the values of the various ECUs that were considered are recorded frame by frame. In groups of 10 frames $(\mathrm{N})$ at a time, the values of the individual parameters are averaged, and the highest and lowest values are excluded from the calculation:

$$
\frac{\sum_{F i}^{F i+N-1}\left[\left(P_{j i}+P_{j i+1}+\cdots+P_{j i+N-1}\right)-\min (P)-\max (P)\right]}{N-2}
$$

where $F_{i}$ represents the i th frame, $P_{j i}, \ldots P_{j i}+N-1$ are the values that the parameter assumes at each frame $i, \min \left(P_{j}\right)$ and $\max \left(P_{j}\right)$ represent the minimum and maximum values that the considered parameter can assume in the interval of frames considered, and $N$ represents the number of frames considered. At this point, a vector of averaged values are obtained for each parameter which constitute the system's state in a period equal to 40 ms . At this point, in order to understand whether or not we are in the presence of a possible attack, the values of these parameters plus those of the information obtained from them are passed to the Bayesian network, which indicates to us with a certain probability as to whether we are under attack or not. If none of the masks are activated, the vehicle status is considered normal, and no action is taken. In the next phase, a Bayesian network is generated, starting from a pre-established data set during the simulation phase with the following parameters (Figure 3 shows the matching process):

- Steer: CAN message related to steering, 7 classes ( $-1: 1$ norm., step variable, very left, middle left, left, center, right, middle right, very right);
- Throttle: CAN message related to acceleration, 4 classes ( $0: 1$ norm., step variable, pedal not pressed, low, medium, high);
- Brake: CAN message related to braking, 4 classes ( $0: 1$ norm., pedal not pressed-low, medium, high);
- RPM: CAN message related to rotations per minute, 5 classes ( $0: 1$, step variable, stop, slow, normal, medium, high);
- Gear: CAN message related to gear of car, 5 classes $(0,1,2,3,4,5)$;
- Radiator: State of ignition of the cooling system, 2 classes (on, off);
- Lidar: Presence or absence of obstacles, 2 classes $(0,1)$;
- Lines: Crossing a road line or not, 2 classes $(0,1)$;
- Speedometer: Speed in absolute value, 6 classes ( $0: 1$ norm., stop, very slowly, slowly, medium, fast, very fast);
- Acceleration: Car acceleration, 5 classes ( $-1: 1$ norm., step variable, deceleration high, deceleration low, no acceleration, acceleration low, acceleration high);
- Speed: Car current speed, 6 classes ( $0: 1$ norm., step variable, stop [ $0 \mathrm{~km} / \mathrm{h}$ ], very slowly [ $0-30 \mathrm{~km} / \mathrm{h}$ ], slowly [ $30-50 \mathrm{~km} / \mathrm{h}$ ], medium [ $50-90 \mathrm{~km} / \mathrm{h}$ ], fast [ $90-130 \mathrm{~km} / \mathrm{h}$ ], very fast $[130-150 \mathrm{~km} / \mathrm{h}]$ );
- Engine Temperature: Car engine temperature, 4 classes ( $0: 150$, step variable, normal operation, low overheating, medium overheating, high overheating);

- Swerve: Car swerve, 7 classes ( $-1: 1$ norm., step 0.285 , very left $\left[-60^{\circ}\right.$ to $\left.-45^{\circ}\right]$, middle left $\left[-45^{\circ}\right.$ to $\left.-30^{\circ}\right]$, left $\left[-30^{\circ}\right.$ to $\left.-5^{\circ}\right]$, center $\left[-5^{\circ}\right.$ to $\left.5^{\circ}\right]$, right $\left[5^{\circ}\right.$ to $\left.30^{\circ}\right]$, middle right $\left[30^{\circ}\right.$ to $\left.45^{\circ}\right]$, very right $\left[45^{\circ}\right.$ to $\left.60^{\circ}\right]$ );
- Obstacle: Presence or absence of generic obstacle within a radius of $20 \mathrm{~m}, 2$ classes (true, false);
- Attack: Presence or absence of attack, 2 classes (true, false).

In the RPM, acceleration, speed, and engine temperature parameters, a normalization was carried out concerning constant values greater than the maximum values reached within the simulation; for the parameters consisting of numerical values, the classes were constructed by dividing the equal whole parts range considered. These parameters constitute the nodes of our Bayesian network. The arches were obtained, taking into account the obtained taxonomy of car (Figure 1) created for this case study according to Colace et al. [53-55] and with Casillo et al. [56]. The net obtained is shown in Figure 4:
![img-3.jpeg](img-3.jpeg)

Figure 4. The obtained Bayesian network.
As can be seen from Figure 4, the Bayesian network presents three different levels: data layer, information layer, and knowledge layer. The data layer level refers to the raw data coming from the vehicle, the information layer level refers to the processed information coming from the data layer, and finally, the knowledge layer level refers to the knowledge starting from the information in our possession. Thus, the network can decode the presence or absence of an attack with a certain probability [57-59]. Through a training process before the network and then the inference one, it was possible to evaluate the method's effectiveness as shown in the next section.

# 5. Experimental Results 

To evaluate our method, we have to define the type of attack that we can take into account for experimental phase. We consider this kind of attack:

1. DoS attack: injecting messages of ' $0 \times 000$ ' CAN ID in a short cycle.
2. Fuzzy attack: injecting messages of spoofed random CAN ID and DATA values.
3. Impersonation attack: injecting messages of Impersonating node, arbitration ID $=$ ' $0 \times 164$ '.
4. Attack Free State: normal CAN messages.

For procedures in the testing phase, it is first necessary to decide which hardware and software components to use in order to test the proposed approach; then, the classification algorithm and the trained Bayesian network must be implemented. The proposed solution consists of a simulator that emulates a real vehicle and its interaction with the environment, CARLA [60]. This is an open-source software used to carry out research to make a simu-

lation test for connected vehicles and autonomous driving. In addition to the simulator, the architecture includes a steering wheel and pedals that allow controlling the vehicle connected to the CAN-Bus through an emulated CAN-Bus; a server that simulates the external environment; an infotainment system that ensures an access point to the CAN-bus; and a board equipped with a SoC that implements the intrusion detection system. To carry out the experimental phase, 4 data sets, one for each kind of attack, were created, containing about 8158 frames, where, at regular intervals, the vehicle was attacked for a total of about 1000 malicious messages. Each frame contains all the status parameters for a specific timestamp interval. To do this, it was simulated through a city track, with the CARLA environment, the driving of a car. It was realized with a Python script, executed for about 24 h . During driving, the vehicle was attacked to simulate a possible intrusion based on the use case. Furthermore, assuming that the channel is ideal and therefore without losses, only the ID and data frame fields of the CAN frame were considered. In this scenario, the attack node uniquely identifies when a frame is labeled as an attack. Once the data set was obtained, the Bayesian network was then implemented. The Bayesian network presented in the previous section was created using Weka software [61]. In order to test the network thus obtained, it then moved on to translate the XML obtained from the Weka into Python code, and through the use of the TensorFlow libraries [62], the Xilinx/PYNQ-Z1 board was then programmed, which, in our case, acted as the IDS of our system. The simple estimator was used as an algorithm to calculate a priori probabilities and conditional probability tables (CPT). To classify the results obtained, the following cases were distinguished:

- True Positives (TP): attack present and correct classification;
- True Negatives (TN): attack not present and correct classification;
- False Positives (FP): attack not present and incorrect classification;
- False Negatives (FN): attack present and incorrect classification.

This classification of merit can be schematized in a confusion matrix observable in Table 1.

Table 1. Confusion matrix.


A confusion matrix is a table used to estimate a classifier's goodness. There are the events considered in the rows, while in the columns, their classification is present. The data on the main diagonal represent correct classifications. From this table are also derived three merit factors that contribute to the analysis of a classifier's performance: the precision (P) (2) merit factor takes into account the number of correct attack identifications concerning the total number of detections. It is obtained with the following formula:

$$
\mathrm{P}=\mathrm{TP} / \mathrm{TP}+\mathrm{FP}
$$

The pecall (R) (3) factor of merit takes into account the number of correct attack identifications compared to the total number of attacks made:

$$
\mathrm{R}=\mathrm{TP} / \mathrm{TP}+\mathrm{FN}
$$

Finally, the F1-Score factor (F1) (4) is given by the harmonic average of precision and recall and measures the accuracy of the classification of events:

$$
\mathrm{F} 1=2 \cdots \mathrm{R} \cdots \mathrm{P} / \mathrm{P}+\mathrm{R}
$$

To evaluate the system performance, we have to decide to compare our solution and the created data set with a common data set present in the literature [63]. In this way, it is possible to see the effectiveness of the proposed methodology. As can be seen in Figure 5, the obtained data sets from the Carla simulation are compared with KIA SOUL data sets presented in the literature. In Figure 5, it is possible to see the experimental results of the second test carried out.
![img-4.jpeg](img-4.jpeg)

Figure 5. Precision, recall and F1-Score of experimental results: (a) Dos Attack, (b) Fuzzy Attack, (c) Impersonating Attack, (d) Free State Attack.

As it is possible to see in Figure 5a-c, we have very high values of precision, recall and F1-score, which gives us a good response from the system. As regards Figure 5d, we have fewer performing results but this is correct, as the last case is more difficult to identify, as it could be easily labeled as a malfunction or other. The thing that encourages us is that our system responds well with real data sets rather than simulated data sets; this bodes well for a possible future test on real simulated environments or vehicles [64-66].

# 6. Conclusions 

This article shows an embedded intrusion control system capable of verifying the presence or absence of cyber attacks on connected vehicles; in practice, by probabilistically analyzing the data traveling in the subsystem of the ECUs connected to each other via the CAN protocol, it is able to identify possible attacks. This system uses a two-step algorithm capable of carrying out a temporal-spatial analysis and a probabilistic analysis through Bayesian networks. Thanks to the ontological study domain and the elaboration of a reference taxonomy, it was possible to identify the critical systems that must be considered in the analysis phase.

The purpose of this research work is to analyze the vulnerabilities inside the connected vehicles and try to find a custom solution in order to limit the vulnerabilities due to the entry into the network of modern vehicles. An embedded intrusion detection system was developed, which is able to analyze the data traffic inside the CAN-Bus and identify those flows that can be labeled as malicious. The study took into consideration what was reported in the literature and was compared with the most common cyber attacks in use

today. In order to evaluate the effectiveness of the method, this was compared with various data sets present in the literature.

The first simulated experimental results compared with data sets present in the literature give us the vision and perception of the effectiveness of this method. Other in-depth studies will have to be conducted in real cases to ascertain their validity.

# 7. Patents 

This research work is a preparatory part of the work carried out within the Italian patent pending No. 102021000009548 registered on 14 April 2021.


#### Abstract

Author Contributions: Conceptualization, F.P., E.A.A., S.C. and E.S.; methodology, F.P., E.A.A., S.C. and E.S.; formal analysis, E.A.A.; investigation, F.P.; resources, E.S.; data curation, F.P.; writingoriginal draft preparation, E.A.A. and E.S.; writing-review and editing. F.P. and S.C.; visualization, E.A.A., S.C. and E.S.; supervision, F.P. All authors have read and agreed to the published version of the manuscript.


Funding: This research received no external funding.
Conflicts of Interest: The authors declare no conflict of interest.
