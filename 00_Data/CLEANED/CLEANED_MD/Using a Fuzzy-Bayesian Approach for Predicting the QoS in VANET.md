# Using a Fuzzy-Bayesian Approach for Predicting the QoS in VANET 

Hafida Khalfaoui ${ }^{1 *}$, Abdellah Azmani ${ }^{2}$, Abderrazak Farchane ${ }^{3}$, Said Safi ${ }^{4}$<br>${ }^{1,3,4}$ LIMATI Laboratory, Sultan Moulay Slimane University, Beni Mellal, Morocco<br>${ }^{2}$ Intelligent Automation Laboratory, Abdelmalek Essaadi University, Tetouan, Morocco


#### Abstract

There are considerable obstacles in the transport sector of developing countries, including poor road conditions, poor road maintenance and congestion. The dire impacts of these challenges could be extremely damaging to both human lives and the economies of the countries involved. Intelligent Transportation Systems (ITSs) integrate modern technologies into existing transportation systems to monitor traffic. Adopting Vehicular Adhoc Network (VANET) into the road transport system is one of the most ITS developments demonstrating its benefits in reducing incidents, traffic congestion, fuel consumption, waiting times and pollution. However, this type of network is vulnerable to many problems that can affect the availability of services. This article uses a Fuzzy Bayesian approach that combines Bayesian Networks (BN) and Fuzzy Logic (FL) for predicting the risks affecting the quality of service in VANET. The implementation of this model can be used for different types of predictions in the networking field and other research areas.


Keywords - Bayesian network, fuzzy-Bayesian, fuzzy logic, prediction, quality of service, risk analysis, VANET.

## I. INTRODUCTION

VANET is a Mobile Ad-hoc Network (MANET) subclass. Its objective is to create a communication system for Vehicle-to-Vehicle (V2V), Vehicle-to-Infrastructure (V2I) and Infrastructure to-Infrastructure (I2I) that increases awareness in the route and allows acquiring real-time traffic events, such as accidents, pre-crash warnings and emergency electronic brake lights [1], [2]. The mobile nodes are smart vehicles supplied with flexible computing resources containing computers, geolocation systems (GPS), radars, network devices and various sensors [3]. These vehicles are interconnected and can have an interface that allows the driver to receive and send messages to various network entities. Furthermore, they incorporate a positioning device such as GPS and sensors that detect changed conditions, such as the state of the trailer's doors (open or closed), the temperature inside, violent movements and non-programmed stops [4]. These characteristics give high visibility and control of different operations and activities that occur within the transportation and help predict risks and make right decisions.

This paper aims at measuring the quality of service (QoS) in VANET by implementing a Fuzzy-Bayesian (FB) approach. The latter starts by analysing the risks of VANET in order to

[^0]implement a tool for predicting problems that disrupt the proper functioning of the network. Therefore, this approach allows studying the influence of input parameters, including routing, security and data processing, on the QoS in VANET. After that, the risk can be resolved or even eliminated to safeguard system connectivity and avoid the problems of disruption in the transport, generating additional costs, distribution delays and ultimately dissatisfaction.

The remainder of this article is structured as follows: Section II shows the challenges of VANET. Section III presents the literature related to the QoS in VANET. Section IV explains the construction of the FB model. Section V discusses the approach proposed. The final section concludes this work and presents some future areas of research.

## II. Challenges of VANET

Significant problems appear when using ad-hoc communication between vehicles moving in a road environment. The key challenges are as follow:

## A. Routing Problems

The routing protocol that establishes and maintains routes from source to destination is the most challenging issue in VANET [5]. Since the infrastructure of VANET is limited, the routing mechanism must be executed by the vehicles themselves, and the intermediate route packets sent between distant vehicles [6]. This mechanism suffers from many issues due to the unique features of VANET, such as the dynamic topology caused by high mobility of vehicles and variable network density. Furthermore, the cars may join and quit the network rapidly, causing frequent path disruption. Consequently, developing an efficient protocol that keeps a route is difficult [7]. Besides, some nodes act selfishly and refuse to participate in the routing to save their resources, such as storage and processing time [6], which can degrade and harm the performance of the network [7]. There are additional issues regarding the VANET routing protocols. The most common are: the scalability and limited bandwidth leading to congestion and interference in the network [8], signal transmission attenuations caused by adverse weather and obstacles, also security issues caused by malicious nodes that can launch

[^1]
[^0]:    * Corresponding author's e-mail: hafidakhalfaoui1996@gmail.com

[^1]:    ${ }^{\text {©2022 Hafida Khalfaoui, Abdellah Azmani, Abderrazak Farchane, Said Safi. }}$ This is an open access article licensed under the Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0).

diverse attacks, such as a black hole, eavesdropping, wormhole and rushing attacks [9].

## B. Security Problems

The security aspect is an important pillar in VANET. If an attacker arrives to launch an attack, it can have a significant impact on network operations and services. Passive attacks, such as listening to the communication and using the secret data to execute malicious activities, or active attacks, such as removing, modifying, or repeating messages to disrupt the network, are both possible. It can also program traffic signals to cause traffic jams or block streets [10]. VANET presents several security issues because of its unique characteristics, such as the open network environment and dynamic network topology [11]. The following are the most notable security threats.

## Authentication

In VANET, there are two types of authentication: identity authentication, which determines the legitimacy of nodes, and message authentication, which prevents fraudulent transmission of messages in the network. Several existing authentication algorithms have solved some security problems in VANETs, but their security still needs improvement. Impersonation, identity (ID) disclosure attacks, spoofing attacks, etc., are types of authentication attacks. They are generated when malicious nodes can create false identities or reveal other node identities to act as legitimate vehicles and benefit from or reinforce incorrect data in the network. For example, an attacker may pretend to be an emergency vehicle in order to slow down other cars [12].

## Privacy Protection

Privacy protection has extended concern for VANET. Vehicles in contact with it typically share messages without any privacy or security, which means the message is not encrypted and contains vehicle ID, speed, location and other specific information that is usually linked to the driver's identity. If these private data are open to attackers, this latter can use them to profile users or launch various attacks, such as masquerading and impersonation attacks that can mislead other vehicles and endanger road safety [13], [14].

## Confidentiality

Confidentiality is a necessary security requirement for exchanging safety and non-safety messages between vehicles. The message content should be secure and inaccessible to nonauthenticated users. Confidentiality also prevents malicious activities, such as man-in-the-middle and traffic analysis attacks [15], [16].

## Integrity

Data integrity is one of the VANET security services that focus on conserving and ensuring the precision and accuracy of data during their transmission. There are numerous ways in which the data integrity service can be compromised. The most common data integrity threats are replay, message tampering and illusion attacks [17].

## Availability

Availability is a critical factor that aims at protecting the life of users in VANET. It ensures that the network is operational and useful information is always available [18]. The most famous availability threats are denial of service (DOS) attacks, jamming attacks, malware attacks, greedy behaviour attacks, spamming attacks and so on. Their common goals are to use the bandwidth unnecessarily to cause voluntary collisions, decrease communication quality between vehicles and thus interrupt services or prohibit other nodes from using VANET support and services [17].

## C. Data Processing Problems

In recent years, the VANET environment has been generating massive amounts of data due to sensor and communication technologies. These data are very important in improving productivity, travel comfort, transportation safety and modern society's economic prosperity. As the amount of data generated by VANET grows exponentially, its complexity and processing will present immense challenges due to the lack of intelligent systems that manage the large quantities of data generated.

As a result, VANET requires complementary technologies to help optimize and efficiently process all data collected from disparate sources. Big data and artificial intelligence (AI) provide competitive advantages in this context, allowing organisations to make better decisions, while reducing operational time and costs. However, these technologies present significant challenges in terms of energy, node storage capacity and computation costs [19]. With the recent emergence of new integrated architectures and access technologies, the computation burden of IA algorithms and big data can be alleviated by migrating complex computations to external cloud servers [20]. This solution also presents some problems in terms of time and security. When the scalability of nodes increases, the existing cloud computing can hardly satisfy the needs of end users. In general, uploading to and downloading from the cloud consume time and energy [21].

## III. Related Work

QoS measures the service degree of satisfaction as presented to the end user. In telecommunication networks, QoS aims at achieving better communication behaviour by routing the packets correctly and using resources optimally [22].

Providing QoS support to VANET is an active research area. This network has particular features, such as high mobility, scalability, a lack of centralized control unit, a hidden node issue, limited resources and an insecure medium, which make QoS provisioning very complex.

In VANET, each application has specific QoS requirements; for example, a safety application should have a minimum End-to-End Delay (E2ED) and packet loss because if a warning message does not arrive at a destination quickly, it will not help prevent an accident [23].

In the literature, many efforts and studies are dedicated to the factors that affect the QoS in VANET and the majority are looking into the routing aspect.

The authors of [24] proposed QMM-VANET to maintain security and connectivity in the VANET. It is a clustering routing protocol that considers QoS requirements and mobility constraints. Firstly, this protocol calculates the QoS value of each vehicle and chooses a trustworthy one as the cluster head. Then, it selects gateways among neighbouring nodes and uses a gateway recovery algorithm to pick another gateway if link fails. In comparison to other protocols, this one demonstrated its efficacy in terms of packet delivery ratio and E2ED in the highway scenario.

In [25] and [26], the authors conduct brief analyses on QoS, which include some types of routing protocols that help minimize delay and increase overall QoS in VANET. The authors of [27] also improved various QoS parameters for various scenario networks, such as delay, jitter, throughput and packet loss ratio, by employing various routing algorithms with different mobility patterns, adaptive modulation, multiple-input multiple-output (MIMO) and coding (AMC) techniques.

In [28], the authors exploit Road Side Units (RSUs) to accumulate and transmit traffic data. They attempt to find the shortest route to the destination based on the cost of each transmission path using an effective algorithm called Dijkstra's Dedicated Short Range Communication (DDSRC).

According to the authors of [29], if the number of packets transmitted in the network increases, a queue of packets may be created in the vehicle, and the response time of some packets may expire before being processed, causing a decreased service rate. They attempted to improve VANET performance by removing useless or unused packets, in contrast to related works that investigated the increasing service rate by changing the parameters and properties of scheduler algorithms.

In overall, it can be concluded that none of the previous QoS solutions met all of the QoS criteria.

## IV. MODELLING THE RISK OF QoS IN VANET USING A FUZZYBAYESIAN APPROACH

A Bayesian Network (BN) is a probabilistic graphical model developed by Pearl to aid in reasoning under uncertainty [30]. BN is defined by a pair $(G, O)$ with $G=V$, A is a directed acyclic graph that encodes a joint probability distribution over a finite set of categorical variables $V$, and the arcs A represent direct relationships between them [31]. In addition, a set of parameters $O$ defines the behaviour of each variable caused by its parent in the graph.

In this study, this tool allows for the prediction of problems that disturb the proper functioning of the network by studying the influence of input parameters on such problems. For example, what is the impact of mobility and density on the
![img-0.jpeg](img-0.jpeg)

Fig. 1. Example of a causal relationship.

[^0]E2ED of data transmission and, consequently, on the routing quality in the network?

Fig. 1 represents a hierarchical arrangement, with both mobility and density are being ancestors and parents of E2ED; analogical routing is its descendant and its child.

This study started with exhaustive research to identify the main challenges of a VANET network as follows:

- Risks related to data routing influenced by the route conditions, such as mobility, density of nodes and security attacks.
- Risks related to the security of the data circulated in the network due to the lack of robust mechanisms, such as authentication, confidentiality, privacy and integrity.
- Risks related to data processing facilitating to make decisions in the different activities. Processing is affected by the quality and quantity of data collected from the different entities of the network.
This study also identified all the parameters that could influence the occurrence degree of the above-mentioned risks. This identification led to conceiving the nature of the dependencies between the different events and defining the causal architecture of the Bayesian model. The following steps are proposed for the analysis of QoS in VANET developed by the BN:

Step 1: Define the architecture of the BN (causal graph).
Step 2: Generate conditional probabilities of intermediate effects and final impacts.

## A. Architecture of the Bayesian Network of QoS in VANET

The architecture of the BN is based on the identification of the relations between the nodes constituting the graph, which is divided according to their typology into three classes:

- The input parameters of the graph: these parameters represent the input nodes of the network.
- Intermediate effects: the direct effects that are broken down into input parameters that are the origin of the causes.
- Final impacts: the factors that directly influence the QoS in VANET.
The investigation of the various factors that influence QoS in VANETs aids in identifying input parameters, as described in Table I, and intermediate effects and final impacts, as shown in Table II. The causal graph in Fig. 2 is developed based on the two tables and after studying the nature of the causal dependencies between them.


## B. Generation of Conditional Probabilities of Intermediate Effects and Final Impacts

After constructing the BN graph, the conditional probabilities (CPs) for each variable must be computed. There are numerous sources of probabilistic information available, such as databases ${ }^{2}$ containing road traffic and attacks. In this study, the BN considers a large number of parameters that make the existence of a complete database a difficult task. Unfortunately, the available databases are private and insufficiently rich to permit a reliable examination of the


[^0]:    ${ }^{2}$ https://www.unb.ca/cic/datasets/index.html

needed probabilities [47]. Therefore, FL is proposed for generating these CPs systematically. It is an effective solution for handling imprecise data and linguistic problems. Its strength
lies in its resemblance to human reasoning and natural language.

TABLE I
DESCRIPTION OF THE INPUT PARAMETERS OF THE CAUSAL GRAPH


TABLE II
DESCRIPTION OF INTERMEDIATE EFFECTS AND FINAL IMPACTS



![img-1.jpeg](img-1.jpeg)

Fig. 2. BN modelling the analyses of risk of QoS in VANET.

The implementation of the FL for generating CPs is done in three principal steps [48], [49]:

- Fuzzification: converts the input variables into a fuzzy subset using fuzzy linguistic values and membership functions.
- Inference: evaluates and combines the fuzzy rules to form conclusions that give the fuzzy outputs of the system.
- Defuzzification: transforms the conclusions provided by the inference engine into numeric values representing the final response of the fuzzy system.
The most widely used inference methods are these of Mamdani [50] and Sugeno [39]. The main difference between them lies in the way the crisp output is obtained from the fuzzy inputs. Mamdani uses a defuzzification technique of fuzzy outputs, while Sugeno uses a weighted average to calculate the result values [51]. This study chooses the method of Sugeno because it has a better processing time. As a result, generating CPs is done just with two first steps.


## Fuzzification

To implement the fuzzification step, the fuzzy variables and their linguistic values are presented in Table III.

TABLE III
STATES OF THE BN NODES



The membership function is the graph representing the amplitude of each input participation. The rules use the input membership values as a reference to determine their impact on the final outputs [52].

In this work, the Gaussian type is chosen for all the nodes of the BN because it provides less errors in the prediction of the data compared to the others, notably the triangular and trapezoidal forms [53]. Fig. 3 shows an example of this function for the 'routing' variable.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Membership function for routing variable.

## Inference

In the remaining steps, we will assume that all CPs have been generated and the method used will be explained for the node 'QoS in VANET'. In this case, the inference mechanism aims at calculating the table of CPs of this variable while considering all combinations of its parents: 'routing' and 'quality of data'. Table IV presents the set of fuzzy rules used in this example.

The open-source software Fispro ${ }^{3}$ is used to implement the fuzzy inference, which provides exact values from different subsets of the output variables. Fig. 4 presents the inference of the variable 'QoS in VANET' knowing that 'data quality' is medium and 'routing' is good, which corresponds to rule 3 in Table IV.

TABLE IV
STATES OF THE BN NODES


![img-3.jpeg](img-3.jpeg)

Fig. 4. Fuzzy inference of the 'QoS in VANET' variable.
The next step aggregates different conclusions of the activated rules, as shown in Table V, and combines them into a single value. This value is obtained by the union of all the triggered conclusions, translated by the max operator.

TABLE V
THE ACTIVATED RULES OF THE "QoS IN VANET"


[^0]
[^0]:    ${ }^{3}$ https://www.fispro.org/en/

The 'medium' and 'good' values of the variable 'QoS in VANET' are 0.607 and 0.135 , respectively. However, the lowest value of 0.001 is tolerated in the case where the possibility is zero (here for the 'bad value') since each state of the variable 'QoS in VANET' is possible, and this possibility must be greater than zero.
QoS in VANET (bad) $=0.001$
QoS in VANET (medium) $=\max (0.607,0.135,0.135)=0.607$ QoS in VANET (good) $=0.135$

The sum of probabilities for each variable states must be equal to 1 . The CPs for the different states of the variable ' QoS in VANET' of rule number 3 are calculated as follows:
$P$ (QoS in VANET $=$ bad $\mid$ data quality $=$ medium, routing $=$ high) $=0.001 /(0.001+0.607+0.135)=0.001$
$P$ (QoS in VANET $=$ medium $\mid$ data quality $=$ medium, routing $=$ high $)=0.607 /(0.001+0.607+0.135)=0.817$
$P$ (QoS in VANET $=$ good $\mid$ data quality $=$ medium, routing $=$ high $)=0.135 /(0.001+0.607+0.135)=0.182$

By following this approach, all CPs for the variable 'QoS in VANET' for the different states of its antecedents were computed as presented in Table VI.

TABLE VI
CPS TABLE OF THE VARIABLE "QoS in VANET"


## V. DISCUSSION

The proposed FB model predicts the QoS state in VANET. By varying the values of the input parameters, their effects on the different nodes of the graph are estimated, implementing the fuzzy inference method.

In many domains and studies, the combination of the BN and the FL system is used, for example, predicting the population status of a rare animal using the inference mechanism in the ecological domain [54], determining the severity scale of a disease based on fuzzy medical rules [55], predicting the risks of delays in deliveries in logistic services [56] and others.

To our knowledge, no prior work analyses risks in VANETs and predicts QoS, considering all previously mentioned parameters, which justifies the interest and originality of the research presented in this article. In addition, this study provides an approach for generating massive data that help in making decisions in the transportation domain. Some classical approaches and existing studies give optimal solutions to
improve QoS in VANET but can only consider a few parameters simultaneously. However, in reality, where decisions have to be made based on several criteria, these approaches are insufficient. Consequently, the presented approach is fruitful. It allows risk analysis at any time in the network and provides a massive database that can be extended progressively using deep learning techniques.

## VI. CONCLUSION

One unknown problem can perturb the communication system or block the proper functioning of the network, causing material and human losses. For that reason, equipping with risk prediction tools is very important. This article proposes a FB model combining the BN approach that evaluates the causality relation between its nodes based on different data resources, such as expert estimations or learning databases, and FL used to generate all CPs needed. This model allows calculating the QoS in VANET in the function of multiple criteria and provides a database that helps determine the originality of risk degrading the QoS in the network. The complexity of the proposed approach consists of the integration of all the factors that influence the QoS in VANET, where the absence of some variables can affect the efficacy of the prediction.

The future work will complete the actual model by generating the CPs of all nodes in the causal graph and propose some scenarios for proving the model efficacy. Furthermore, some solutions will be presented in the case of bad QoS in the network.

## ACKNOWLEDGEMENT

The research has been supported by the Ministry of Higher Education, Scientific Research and Innovation, the Digital Development Agency (DDA) and the National Centre for Scientific and Technical Research (CNRST) of Morocco (Smart DLSP Project - AL KHAWARIZMI IA-PROGRAM).
