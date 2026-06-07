# Water Risk-Proofed: Risk Assessment in Water Desalination 

Alyah Alfageh<br>KAUST<br>Thuwal, Saudi Arabia<br>alyah.fageh@kaust.edu.sa

Sridhar Adepu<br>University of Bristol<br>Bristol, United Kingdom<br>sridhar.adepu@bristol.ac.uk

Charalambos Konstantinou<br>KAUST<br>Thuwal, Saudi Arabia<br>charalk@kaust.edu.sa

## ABSTRACT

Desalination plants, heavily reliant on Industrial Control Systems (ICS), have emerged as increasingly vital resources in the wake of escalating global water scarcity. This raises an urgent need to prioritize their security, calling for the implementation of robust risk assessment measures. Recognizing these pressing issues, this paper proposes a risk assessment approach for ICS within water desalination facilities. The strategy integrates the capabilities of Bayesian Networks (BNs) and Dynamic Programming (DP). It evolves BNs into Multilevel Bayesian Networks (MBNs), an innovative form that adeptly navigates the intricacies of system complexity, facilitates efficient inference, and dynamically adapts risk profiles. The proposed methodology considers the perspective of potential attackers, which is critical for a comprehensive risk assessment and a robust defense strategy. The DP aspect enhances this approach by dissecting complex problems and identifying optimal attack paths. The work demonstrates the comprehensive risk assessment by executing multiple attacks on a water desalination plant with various strategies. It takes into account the probabilistic interdependence relationships within the system. Additionally, the paper formulates a mathematical risk assessment using system models and graphical representation, yielding realistic results.

## CCS CONCEPTS

- Computer systems organization $\rightarrow$ Embedded and cyberphysical systems; $\cdot$ Networks $\rightarrow$ Cyber-physical networks; $\cdot$ Security and privacy $\rightarrow$ Information flow control.


## KEYWORDS

Industrial Control Systems Security; Risk Assessment; Bayesian Networks; Water Desalination; Dynamic Programming; Discrete Graphical Modeling.

## ACM Reference Format:

Alyah Alfageh, Sridhar Adepu, and Charalambos Konstantinou. 2023. Water Risk-Proofed: Risk Assessment in Water Desalination. In Proceedings of the 4th Workshop on CPS\&IoT Security and Privacy (CPSIoTSec '23), November 26, 2023, Copenhagen, Denmark. ACM, New York, NY, USA, 13 pages. https://doi.org/10.1145/3605758.3623500

## 1 INTRODUCTION

Industrial Control Systems (ICS) have been transformative in various sectors, particularly those linked to critical infrastructure such
![img-0.jpeg](img-0.jpeg)

This work is licensed under a Creative Commons Attribution International 4.0 License.

CPSIoTSec '23, November 26, 2023, Copenhagen, Denmark
(c) 2023 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-0254-9/23/11.
https://doi.org/10.1145/3605758.3623500
as energy, gas, and water. The ability of ICS to automate, monitor, and control critical processes has significantly improved operational efficiency. Despite these advancements, the dynamic and complex nature of ICS has exposed such systems as prime targets for cyber-attacks $[2,10]$.

Historical instances of such attacks are numerous and alarming. For instance, the 2000 Maroochy water breach in Australia showed how a disgruntled insider could cause significant damage. In 2010, the world witnessed the sophistication of the Stuxnet virus attack that targeted Iran's nuclear facilities. The vulnerability of energy infrastructure was again highlighted by the cyber-attack on Saudi Aramco's network in 2012, followed by a similar attack on the Ukrainian power grid in 2015 and 2016 [2, 10]. In a more recent case in 2021, a cyber-intrusion at a water purification facility in Oldsmar, Florida served as a reminder that the water infrastructure is also not impervious to such attacks [10].

A significant body of research, such as the studies by Kriaa et al., Lindhe et al., and Abdo et al., underscores the importance of risk assessment in securing ICS [1, 18, 21]. Kriaa et al. utilized Boolean logic Driven Markov Processes (BDMP) for a detailed understanding of Cyber-Physical System (CPS) attacks [18]. Lindhe et al. proposed a unique probabilistic risk analysis method specifically for drinking water systems [21]. In [1], the authors aimed for an integrative approach, merging safety and security risk assessments within ICS. A common aspect among these studies is the acknowledgement of inherent challenges such as dependence on expert judgment for probabilities, limitations in fully capturing the impact of failures, and assumptions about system architecture that may constrain real-world applications.

Water desalination plants, as ICS, present unique complexities and risk profiles that require a robust and comprehensive risk assessment. However, most existing risk assessment methodologies for ICS have notable limitations. They often fail to consider the dynamic behavior of these systems under varying conditions as well as the complex interactions among different components. This typically results in risk assessments that are not fully representative of the possible threats and risks. In order to address these shortcomings, this work introduces a comprehensive risk assessment technique that integrates the capabilities of Multilevel Bayesian Networks (MBNs) and Dynamic Programming (DP). This technique acknowledges the dynamic nature of ICS and the complex interactions among components while offering a more accurate and comprehensive risk profile. The main contributions of the paper are as follows:

- The development of a comprehensive risk assessment methodology that utilizes the concepts of MBNs and DP.
- The consideration of a wide array of potential impacts emerging from attacks on ICS, including operational, environmental, and hazardous outcomes.

- The inclusion of the attacker's perspective in the risk assessment process which enables the identification of the most probable attack paths and critical targets.
- The application of this methodology to a real-world scenario, a water desalination plant in the Kingdom of Saudi Arabia, demonstrating its practical relevance and utility.
Organization: The remainder of this paper is organized as follows: Section 2 delves into the related work in the realm of ICS security and risk evaluation. Section 3 offers an overview of the desalination process and the various concepts used in the risk assessment. Section 4 describes the methodology design, while the implementation and corresponding results are presented in Sections 5 and 6 . The paper concludes in Section 7.


## 2 RELATED WORK

In this section, the literature relevant to ICS security is explored. The discussion focuses on two subsections: assessing ICS security and security risk assessment.

Assessing the Security of ICS: The security assessment of ICS is crucial for protecting critical infrastructure, and diverse approaches have been explored to evaluate and mitigate vulnerabilities in these systems. Keliris et al. [15] proposed a comprehensive cybersecurity assessment for ICS that incorporates real hardware components. They advocate the use of Hardware-In-the-Loop (HIL) testbeds, which connect Programmable Logic Controllers (PLCs) and other hardware components to a simulation environment. HIL testbeds offer high accuracy, cost-effectiveness, flexibility, and the ability to represent all layers of the ICS architecture. Including hardware components in the assessment is emphasized to achieve realistic and reliable results, particularly in the context of ICS cybersecurity. In [18], the authors proposed the use of BDMP formalism for modeling CPS attacks, with a focus on the Stuxnet attack as a case study. The BDMP model offers a more detailed analysis of the target architecture and attack stages compared to traditional methods like attack trees. By parameterizing the success rates and probabilities of each attack step, the authors performed quantitative analysis to estimate the overall attack success probability and explore different attack sequences. The approach provides both quantitative and qualitative results, which are valuable for risk assessment. However, the study acknowledges limitations related to real-world scenarios and network architecture assumptions, which may impact the accuracy of quantification results. The work in $[6,7]$ focused specifically on identifying security-critical components within CPS. They proposed a MaxSAT-based methodology that uses the LDA4CPS tool to efficiently pinpoint these crucial components. This tool leverages AND/OR dependency graphs to determine the most likely mission-critical set, demonstrating its effectiveness through performance analysis and application to an aircraft control system. However, it is worth noting that this methodology primarily considers independent failures, with less emphasis on dependent failures or external influences.

Security Risk Assessment: Numerous studies have explored diverse strategies for security risk assessment to counter evolving cybersecurity threats. In [28], the authors presented a comprehensive analysis of the security challenges posed by the interconnection of CPS through Internet-of-Things (IoT) technologies.

They propose a tailored risk assessment approach that takes into account threat levels, vulnerability levels, and impact levels, providing a systematic framework for evaluating the risks associated with IoT-enabled CPS. The authors highlighted the limitations of existing risk assessment methodologies in identifying attack paths that exploit the unique connectivity and functionality features of IoT-enabled CPS. By integrating well-established standards and methodologies, their approach enables the prioritization of security measures and informed decision-making to safeguard such systems. It is important to acknowledge the limitations of the proposed approach, including the reliance on qualitative assessments and subjective values, which may introduce some degree of uncertainty in the risk assessment process. Additionally, the absence of explicit consideration of quantitative probabilities could limit the precision of risk quantification and comparison.

Amro et al. presented a novel risk assessment method for Autonomous Passenger Ships (APS) combining FMECA with the MITRE ATT\&CK framework [5]. This qualitative-based methodology is applied to an APS communication architecture, leveraging graph theory metrics for granular threat identification and impact estimation, thereby minimizing expert judgment reliance. Noteworthy additions include the Techniques-Description Table (TDT) and Component-Description Table (CDT), facilitating more comprehensive risk analysis. The authors employ CVSS-based likelihood estimation for risk probabilities and calculate Risk Priority Numbers (RPNs) for effective risk mitigation. Despite the methodology's limitations, such as its qualitative focus and lack of explicit quantitative considerations, the authors highlight its versatility across different CPS use cases and resilience to evolving attack techniques via proposed system updates. They concluded by proposing future enhancements such as investigating failure mode correlations, refining detection methodologies, and exploring centrality measures to broaden the method's applicability and strengthen its comprehensive nature.

Additionally, Bayes Networks (BNs) have been employed to assess information security risks, prioritize defense-in-depth measures, and evaluate network risks [8, 11, 30]. For example, Zhang et al. presented a novel cybersecurity risk assessment approach for ICS, which leverages an MBN to encapsulate attack, function, and incident models [29]. The network processes two types of inputs: attack evidence from an Intrusion Detection System (IDS) and anomaly evidence from the ICS supervisor system. The assessment procedure is divided into hazardous incident prediction and risk assessment. A simulation of a simplified chemical reactor control system demonstrated the method's effectiveness in dynamically assessing cybersecurity risks, including unknown attacks.

Risk Assessment in ICS: Risk assessment in ICS integrates both qualitative and quantitative methodologies, catering to different facets of the problem [22, 23]. While primarily addressing process and safety aspects, these methods identify, evaluate, and mitigate risks, enhancing understanding of ICS-specific hazards. However, they may not fully cover all cybersecurity risks. Key methodologies include Fault Tree Analysis (FTA), Hazard and Operability Study (HAZOP), Layers of Protection Analysis (LOPA), Quantitative Risk Assessment (QRA), Failure Mode and Effect Analysis (FMEA), Fuzzy Logic Approaches, and the Bow-Tie Model [12, 24].

FTA and HAZOP provide visual insights into potential system failures and operational deviations, while LOPA evaluates protective layer effectiveness. QRA quantifies risk probabilities, and FMEA probes into potential failure modes and effects. Fuzzy Logic handles ambiguity, and the Bow-Tie Model visually connects hazards, causes, and consequences. These methodologies collectively offer a holistic risk assessment toolkit, combining quantitative and qualitative dimensions. This blend is essential in managing the complexity of ICS risk, promoting an in-depth understanding and effective risk mitigation [12, 24, 32].

## 3 BACKGROUND

In this section, we provide a brief description of water desalination technologies, introduce BNs and MBNs as well as frameworks for ICS security risk assessment.

### 3.1 Water Desalination Process

Desalination is the process of removing salt and other minerals from seawater or brackish water. This process is becoming increasingly important due to the escalating water demand and scarcity in various parts of the world [3, 9].
3.1.1 Water Desalination Techniques. Several techniques have been developed for desalinating water including [17]:
(1) Thermal Desalination Techniques:
(a) Seawater Reverse Osmosis (SWRO): SWRO, a widely used technique, involves forcing seawater under high pressure through a semi-permeable membrane to separate minerals.
(b) Multistage Flash (MSF) Distillation: MSF is a thermal process where seawater is heated, often using waste steam from an associated power plant, and then sequentially flashed into steam in a series of stages operating at decreasing pressures. The steam is then condensed to produce fresh water.
(2) Capacitive Deionization (CDI): This technique uses an electrochemical process to remove salt and other minerals. During CDI, water is passed between porous, electrically charged electrodes that attract salt ions, desalinating the water [9].
(3) Electrodialysis (ED): In ED, another electrochemical method, water is passed through a series of charged membranes to separate salt ions from the water [3, 17].
(4) Shock Electrodialysis (SED): This desalination technique uses a pulsed electric field to remove salt and other minerals.
3.1.2 Water Desalination Architecture. The desalination process can be outlined through the following key stages [3, 9]:
(1) Source Water Intake: Water is drawn from sources like the sea or brackish water bodies, with intake methods varying based on location and source quality, such as beach wells or open intakes.
(2) Pre-treatment: Prior to desalination, the water is pre-treated to remove impurities and protect the system.
(3) Desalination Process: Here, the actual separation of salts and impurities from the water takes place. These techniques are mentioned in 3.1.1.
![img-1.jpeg](img-1.jpeg)

Figure 1: Illustration of a BN.
(4) Post-treatment: After desalination, the water undergoes remineralization, disinfection, and pH adjustment to make it suitable for use.
(5) Brine Disposal: Brine, a desalination byproduct, must be properly disposed of to reduce environmental impact.
(6) Distribution: After treatment, the desalinated water is distributed to end users.
(7) Monitoring and Maintenance: The system is continuously monitored and maintained for peak performance.

### 3.2 BNs

BNs are a probabilistic graphical model that represents the relationships between random variables, $X_{1}, X_{2}, \ldots X_{n}$, and their conditional dependencies. The graphical structure of a BN, called a directed acyclic graph (DAG), is used to encode the conditional independencies between the variables. The nodes in the DAG represent the random variables, and the edges represent the relationships between them. The probabilities of the variables are represented as conditional probability distributions, $P\left(X_{i} \mid\right.$ Parents $\left(X_{i}\right)$ ), where Parents $\left(X_{i}\right)$ is the set of parent nodes of $X_{i}$. BNs adjust the likelihoods of events in light of fresh data. When some evidence, $E$, is observed, Bayes theorem is used to update the probabilities of the other variables as follows:

$$
P\left(X_{i} \mid E\right)=\frac{P\left(E \mid X_{i}\right) P\left(X_{i}\right)}{P(E)}
$$

Figure 1 depicts a BN that includes three nodes: A, B, and D. Node A is an observed variable, reflecting real-world measurements or data. Nodes B and D represent variables that are not directly observed. The edges in the figure represent probabilistic dependencies. B and D serve as parents of A, meaning their values influence the value of A . The direction of the edges indicates the direction of the probabilistic influence.
3.2.1 MBNs. A multilevel network typically refers to models that have multiple levels of variables that interact with each other. These models can be used to account for variation at different levels of a system or process. For example, in the case of hierarchical BNs, there may be variables at multiple levels of a hierarchy, such as individual observations within groups or groups within larger populations. In such cases, the model can use the information at both the individual and group levels to improve its predictions or classifications. Similarly, in the case of MBNs, there may be variables at multiple levels of a system, such as individual traits or characteristics and contextual factors [14].

### 3.3 MITRE ATT\&CK and CVSS

The Common Vulnerability Scoring System (CVSS) and MITRE's Adversarial Tactics, Techniques, and Common Knowledge (ATT\&CK) framework are pivotal tools that provide a profound

understanding of the cybersecurity landscape, thereby aiding in the development of effective mitigation strategies [32]. MITRE's ATT\&CK framework is a valuable tool that provides a knowledge base detailing the tactics and techniques adversaries employ in real-world cyber-attacks [16]. It offers insights into various stages of an attack lifecycle, from initial reconnaissance to attack execution, and maintaining presence within the compromised system. This information proves valuable for potential attack path identification, attacker behavior understanding, and proactive defense strategies formulation. Nevertheless, effective utilization of this framework necessitates a nuanced understanding of ICS's unique characteristics.

The CVSS is primarily used to rate the severity of security vulnerabilities. It offers a structured method to assess potential security risks, assisting in resource allocation for security mitigation. However, its direct application in the context of ICS can be complex due to its main focus on confidentiality, integrity, and availability (CIA) of information systems [31], often overlooking the physical consequences critical to ICS. Thus, a comprehensive ICS risk assessment model must account for these unique consequences alongside the standard CIA parameters. Despite CVSS being a prevalent choice for risk assessment, its application is limited by the subjectivity involved in selecting measurement standards and assigning evaluation index weights. Several resources enhance the understanding of vulnerabilities in ICS [16, 27]. This paper adopts a comprehensive approach by integrating insights from CVSS and the aforementioned systems to ensure a thorough understanding of ICS vulnerabilities, thus contributing to the development of robust security management.

## 4 METHODOLOGY

The proposed methodology, incorporating MBNs and DP, offers a comprehensive approach to analyzing the risk landscape in ICS, as shown in Figure 2. The process involves numerous steps designed to thoroughly assess potential risks and associated costs. It starts with the development of a threat model, considering system vulnerabilities and potential exploiting attacks. This model serves as the basis for the formation of an MBN, used for risk estimation. The MBN includes a range of factors, such as potential attacks, their subsequent effects on system components and functionalities, and overall process impact. The methodology employs CVSS to ensure accurate vulnerability assessments.

The CVSS assigns a numerical score and severity rating to each vulnerability, providing a detailed understanding of potential risks. After forming the MBN and assessing vulnerabilities, the methodology moves on to quantify potential losses and risks. This phase starts with the identification of the optimal attack path via DP. The potential loss associated with this path and other alternative paths, encompassing operational, environmental, and hazardous costs related to potential attacks, is then calculated. Risks are determined following loss quantification, based on probabilities of attack impacts and calculated costs. This risk assessment gives a balanced view of potential impacts and the likelihood of various attacks. Lastly, another algorithm balances the probability of a path being chosen by an attacker and the impact cost of the attack for different scenarios, ensuring the selection of an optimal attack. This
![img-2.jpeg](img-2.jpeg)

Figure 2: An overview of the proposed methodology.
stage takes into account both the probability of an attack and its potential impact.

### 4.1 Threat Model

The threat model considered in this work is constructed to defend against remote attacks, incorporating a wide spectrum of intricate tactics utilized by adept adversaries. This model demonstrates efficacy in pinpointing potential risks in diverse areas, including software and hardware, as well as threats emanating from social engineering and insider activities, which could potentially compromise system security [26]. Moreover, this threat model evaluates a variety of attack strategies that aim at key system parameters. These strategies might independently target single components, multiple components concurrently, or adopt a comprehensive method, impacting a combination of actuators, controllers, and sensors.

The executed attacks and their sequence are based on the MITRE ATT\&CK framework. It is assumed that the attacker has already infiltrated both the Information Operational Technology (IT/OT) networks, thereby gaining access to the control system. Hence, the focus of the attacks primarily lies on physical components such as sensors, actuators, and controllers. It is noteworthy to mention that traditional steps emphasized in the MITRE ATT\&CK sequence, like execution and persistence, are the primary focus in this scenario. This threat model is simulated on a water desalination plant, focusing attention on the physical components. The presumption is that the attacker possesses advanced skills and comprehensive knowledge of the process, making the system's physical components especially vulnerable to such sophisticated attacks.

### 4.2 MBN for Risk Assessment

The construction of the MBN for the risk assessment model adheres to a systematic set of steps [29]. In the model, each layer of the MBN is an individual BN. The construction process involves:

(1) Node Definition: Denote the random variables as $X_{i}(i \in$ $V$ ) and their respective states as $s_{i}$. These are represented as nodes within each layer of the network.
(2) Parent-Child Relationships: Establish causal relationships, or dependencies, among the variables within each layer. These dependencies are denoted as parent-child relationships between nodes, with $P\left(X_{i}\right)$ signifying the set of parent nodes for $X_{i}$. The relationships are visualized as directed edges from parent nodes to child nodes in a DAG.
(3) Conditional Probability Distributions (CPDs): For each layer of the MBN, determine the probability of a node's state given the states of its parent nodes. These CPDs are expressed by Conditional Probability Tables (CPTs) or mathematical functions, symbolized as $P\left(X_{i}=s_{i} \mid P\left(X_{i}\right)=s_{P_{i}}\right)$. In the MBN, these CPDs represent the relationships between variables and calculate the probability of a node being in a certain state, given the states of its parent nodes. The conditional probability of node $X_{i}$ being in state $s_{i}$, given that its parent nodes $P\left(X_{i}\right)$ are in states $s_{P_{i}}$, is calculated using Bayes rule:
$P\left(X_{i}=s_{i} \mid P\left(X_{i}\right)=s_{P_{i}}\right)=\frac{P\left(P\left(X_{i}\right)=s_{P_{i}} \mid X_{i}=s_{i}\right) \cdot P\left(X_{i}=s_{i}\right)}{P\left(P\left(X_{i}\right)=s_{P_{i}}\right)}$
(4) Layer Interaction: Determine the interdependencies and interactions between variables across different layers of the MBN. This step involves understanding how each BN layer influences and interacts with the others.
(5) CPD Updates: Update the CPDs in each layer as necessary, in response to changes in the system or incoming new data. The updated CPDs are represented as $P\left(X_{i}=s_{i} \mid P\left(X_{i}\right)=\right.$ $\left.s_{P_{i}}\right)$.
(6) System Behavior Evaluation: Assess the system's behavior under a variety of scenarios, considering different potential states and conditions. Execute simulations and analyze the results for each layer of the MBN.

The outlined construction process of the MBN provides a systematic approach for assessing cybersecurity risk. It follows a hierarchical structure with interconnected layers, representing different stages of a potential cybersecurity breach. These layers address various elements, such as vulnerabilities, attacks, compromised components, operational impact, and overall consequences. The detailed exploration of these layers begins with the attack layer.

Attack Layer: In the initial layer of the model, a connection is established between known system vulnerabilities and potential threats or attacks. This connection is represented by network edges, where the parent node (resources) is denoted as $R$ and the child node (the attack) as $A$. The edge from $R$ to $A$ signifies the relationship, with the associated edge probability indicated as $P(A \mid R)$. This probability represents the conditional likelihood of an attack $A$ occurring given the vulnerabilities $R$, serving as a measure of exploitability that indicates the likelihood of potential attacks within this layer.

Various types of nodes, such as system vulnerabilities and attack nodes, are characterized by probabilities obtained from different sources. For instance, nodes representing vulnerabilities indicate potential security weaknesses within a system that can be exploited by attackers. The BNs is utilized to model the causal dependencies for vulnerability evaluation, following the approach outlined in the study by Poolsappasit et al. [25]. Each network node is assigned a probability that represents the potential likelihood of an attack, enabling a comprehensive risk analysis.

The exploitability score for each edge is calculated using CVSS scores, denoted as $\operatorname{Pr}(e)$. The score is determined as follows:

$$
\text { Exploitability Score }=\mathrm{AV} \times \mathrm{AC} \times \mathrm{PR} \times \mathrm{UI}
$$

The variables in this equation represent the: (i) Attack Vector (AV): indicates the accessibility of the vulnerability, (ii) Attack Complexity (AC): reflects the conditions required for the exploitation to occur, (iii) Privileges Required (PR): indicates the level of access needed for exploitation, and (iv) User Interaction (UI): indicates whether user action is required for exploitation. This score provides a quantitative measure of the likelihood of each system vulnerability being exploited.

Attack nodes represent various attack methods that adversaries might employ to exploit a system, including techniques such as network scanning, phishing, brute force attacks, or spoofing. The likelihood of these specific attacks succeeding depends on both the vulnerabilities present in the system and historical data or expert opinion regarding the success rates of these methods. The probabilities assigned to these nodes initially reflect the success rates of the corresponding attack methods based on historical data or expert opinion. However, these probabilities are dynamic and can be adjusted to account for changes in the system's vulnerabilities or other relevant conditions. The conditional probabilities associated with these vulnerabilities, denoted as $P(e)$, plays a critical role in determining the likelihood of a successful exploit.

Component Layer: In the second layer, the primary focus is on the potential compromise of system components as a result of attacks. The construction of this layer involves consideration of the system's mathematical model and analysis tools such as fault tree analysis. These elements help to understand the interrelationships between the components and system parameters. In this layer, conditional probabilities are used to estimate the likelihood of an attack affecting a specific system component. The conditional probability $P(C \mid A)$ represents the probability of system component $C$ being compromised given the occurrence of attack $A$. System components are represented using a binary state, where a value of "true" or 1 indicates a compromised state, while a value of "false" or 0 indicates a non-compromised state. This binary representation facilitates clear analysis and detection of compromised components.

Functionality Layer: This layer examines the potential repercussions of cyber-attacks on the operational parameters of the system. It leverages the foundational principles of the system's mathematical model and incorporates also tools such as fault tree analysis to establish the intricate relationships between various functionalities and process parameters. Within this layer, conditional probabilities play a crucial role in determining the likelihood of specific functionalities being compromised by cyber-attacks. To

achieve this, a binary scheme is employed, where "true" (1) represents affected functionality and "false" (0) represents unaffected functionality. To illustrate, assuming a functionality denoted as $F$ impacted by an attack $A$ targeted at a component $C$. Their conditional probability $P(F \mid C)$ represents the likelihood of functionality $F$ being affected by an attack $A$ on component $C$.

Impact Layer: The final layer explores the potential effects an attack may inflict on the system. These could range from a complete production shutdown to operator injuries or lower production rates. Constructing this layer involves consolidating insights from expert opinions, process literature, and the system's model. The configuration of this layer relies on the preceding layers - the functionality, component, and attack layers. Using Bayes' rule, as referenced in Eq. (2), these interconnected layers feed into the computation of the impact layer. Denoting a potential impact as $I$ while $A, C$, and $F$ represent the states of attack, component, and functionality, respectively. Their conditional probability $P(I \mid A, C, F)$ then stands for the likelihood of experiencing impact $I$ given an attack $A$, a component state $C$, and a functionality state $F$.

### 4.3 Most Probable Attack Path

Once the MBN is established and the interconnected layers are analyzed, the subsequent task involves selecting the optimal attack path. This is the path that allows the attacker to compromise the system most easily, leading to the intended consequences. It takes into account the exploitability of vulnerabilities, favoring shorter routes (nodes) to produce the desired impact. By assigning priority to these elements, it is possible to pinpoint the optimal attack path, improving the efficacy of risk assessment and mitigation efforts.

In the MBN, probabilities are evaluated using a weighted adjacency matrix, represented as $A$. This matrix expresses the probabilities of transitioning between nodes. Here, $P(X)$ denotes the prior probability of node $X$, and $P(Y \mid X)$ refers to the conditional probability of node $Y$ given node $X$. These probabilities are vital in predicting the values of $X$ and $Y$ based on observed data or prior knowledge about their interrelations. In order to calculate the joint probability of a specific path in a BN, a product of probabilities along the path is utilized. The joint probability, represented as $P$ (path), is calculated as follows:

$$
P(\text { path })=\prod_{i=1}^{n} P(i) \cdot A_{i, i+1}
$$

Here, $P(i)$ stands for the probability of being at node $i$, and $A_{i, i+1}$ signifies the transition probability from node $i$ to node $i+1$. DP is employed based on these joint probabilities to select the optimal path. As Algorithm 1 traverses the graph, it updates and stores the maximum probability for each node while keeping track of each node's parent to reconstruct the highest probability path. The DPbased approach is integral to the risk assessment process as it identifies the highest joint probability path between a start and end node in a directed graph.

### 4.4 Loss Quantification

An ICS attack can have severe consequences on various aspects of the facility's operations. These consequences can range from loss of data, and equipment damage, to operational shutdowns. The primary objective of this paper is to focus on three key aspects of

```
Algorithm 1 DP for finding max probability in a DAG
    Function: MaxProbPath(adj_list, start, end)
        if has cycle(adj_list) then
            return ( \(-\infty,[]\) )
        memo \(\leftarrow[-\infty] *\left(\right.\) max(adj_list.keys \(\left.())+1\right)\)
        memo \([\) start \(] \leftarrow 1\)
        parent \(\leftarrow[-1] *\left(\right.\) max(adj_list.keys \(\left.())+1\right)\)
        parent \([\) start \(] \leftarrow\) start
        for each \(i\) in range(len(adj_list)) do
            for each \(u\) in adj_list.keys() do
                for each \((v, p)\) in adj_list \([u]\) do
                    if \(((m e m o[u] \neq-\infty)\) and
                        \((m e m o[v]<m e m o[u] \neq p)\) ) then
                            memo \([v] \leftarrow\) memo \([u] \neq p\)
                parent \([v] \leftarrow u\)
max_prob \(\leftarrow\) memo[end]
    path \(\leftarrow[]\)
    curr \(\leftarrow\) end
    while curr \(\neq\) start do
        path.append (curr)
        curr \(\leftarrow\) parent \([\) curr \(]\)
    path.append(start)
    path.reverse()
    return (max_prob, path)
```

the consequences resulting from an ICS attack, which have been previously discussed in Eq. (5). The total loss can be calculated as the sum of these individual impacts, as represented by the formula given [19]. For ease of understanding and reference, the terminologies and symbols used in this context are provided in the nomenclature Table 1.

$$
\text { Total Loss }=\sum \text { Operational }+ \text { Environmental }+ \text { Hazardous }
$$

4.4.1 Operational Loss. The operational loss, denoted as $\mathrm{PL}(t)$, is computed based on the difference in the production rate, represented by the distillate flow rate $\left(W_{d}\right)$, before and during the attack [20]. If $p r(t)$ and $p r^{\prime}(t)$ are the production rates under normal and attack conditions, respectively, it can be calculated as:

$$
\mathrm{PL}(t)=\int_{t_{0}}^{t}\left(p r(t)-p r^{\prime}(t)\right) \cdot V p d t
$$

where $V p$ is the unit price of the product. Energy consumption forms a significant part of operational costs, involving both thermal and electric energy [3, 13]. The total energy required in an MSF system can be calculated as the sum of the thermal and electric energy. The thermal energy can be represented as:

$$
Q_{\text {total }}=\sum\left(Q_{i}+W_{i}\right)
$$

The electric energy is the sum of the power inputs to the pumps, compressor, and cooling system, and can be represented as [3, 13]:

$$
E_{\text {total }}=P_{\text {pumps }}+P_{\text {compressor }}+P_{\text {cooler }}
$$

The energy efficiency of the plant can be calculated as [3, 13]:

$$
\text { Energy efficiency }=\left(\frac{\text { Plant capacity }}{\text { Total energy consumption }}\right) \times 100
$$


Table 1: Nomenclature definitions.
4.4.2 MSF Performance Metrics: The MSF system performance is usually monitored by the following primary metrics.

Thermal Performance Ratio (TPR): is a measure of the effectiveness of a desalination system in converting heat energy into distillate. It is calculated as:

$$
P R=\frac{\text { Actual distillate flow rate }}{\text { Theoretical flash evaporation }}
$$

Theoretical flash evaporation is the amount of distillate that could be produced if all the supplied heat was used to evaporate water. This ratio provides a benchmark for the heat utilization efficiency of the system $[4,13,26]$.

Gain Output Ratio (GOR): is a measure of the overall efficiency of the desalination process, calculated as:

$$
G O R=\frac{\text { Distillate flow rate }}{\text { Steam flow rate }}
$$

The ratio of distillate produced to the amount of steam consumed in the system serves as a measure of operational efficiency. It quantifies the amount of distilled water generated per unit of steam utilized, directly indicating the system's effectiveness. [4, 13].

### 4.5 Optimal Attack Scenario

The Optimal Attack Scenario (OAS) will be a function that maps a set of attack scenarios $X$ in the BN, and can be expressed as:

$$
O A S=\arg \max _{X \in B N}\left(P_{(X)} \times Q(X)\right)
$$

where $P_{(X)}$ represents the probability for the attack scenario $X$, and $Q(x)$ represents the quantification of impact for the attack scenario $X$. The symbol $\cap$ denotes the intersection of two sets. The calculation of OAS involves finding the attack scenario $X$ in the network that maximizes the intersection of attack probability $P_{(X)}$ and $Q(x)$, i.e., the attack scenario with the highest attack probability and the highest quantification of impact. The result of the calculation provides a way to prioritize mitigation efforts and identify the most critical attack scenarios in the system. These steps are elaborated in the Algorithm 2.
4.5.1 Formulating Risk Assessment: With the application of the Algorithm 2, the OAS is determined and the maximum potential loss is calculated. This process allows formulating the risk assessment, which can be expressed as below:

$$
\text { Risk }=P_{X} \times Q_{X}
$$

In this equation, $P_{(X)}$ denotes the probability of the risk occurring, while $Q(X)$ signifies the cost or consequences of the risk. The probability $P_{(X)}$ is computed from the joint probability distribution of the BN via the chain rule:

$$
P\left(N_{1}, \ldots, N_{n}\right)=\prod_{i=1}^{n} P\left(N_{i} \mid \operatorname{Pa}\left(N_{i}\right)\right)
$$

In the MBN, the probability of a successful attack is linked to the nodes within the final layer, also known as the impact layer. Upon determining the optimal attack path, which outlines the most probable series of events leading to an attack, focus is shifted towards the impact nodes associated with this path. The probability $P_{(X)}$ for the occurrence of each impact node, in conjunction with the optimal attack path, is taken into consideration. This probability

```
Algorithm 2 Calculation of OAS
    Function: OAS \((X, B N)\)
    \(O A S \leftarrow 0\)
    max_intersection \(\leftarrow 0\)
    for each \(X \in B N\) do
        \(P_{X} \leftarrow \mathrm{P}(X)\)
        \(Q_{X} \leftarrow \mathrm{Q}(X)\)
        intersection \(\leftarrow P_{X} \cap Q_{X}\)
        if (intersection > max_intersection) then
            \(O A S \leftarrow X\)
            \(\max \_\)intersection \(\leftarrow\) intersection
    end for
    return OAS
```

![img-3.jpeg](img-3.jpeg)

Figure 3: Example of the MSF process and components in simulated attacks.
serves as a critical metric, indicating the likelihood of each potential outcome of a successful attack. DP is subsequently utilized to determine the highest risk based on the OAS and the quantification of the associated impact.

## 5 EXPERIMENTAL RESULTS

The implementation of the proposed risk assessment methodology using a MBN is carried out in several interconnected stages. The first stage involves simulating various predefined attack scenarios using MATLAB Simulink [4, 26]. Once the attack simulations are completed, the outcomes of these scenarios are utilized in the next stage - the construction of the MBN.

### 5.1 Experiment Background and Setup

The case study in this paper centered on the security of an MSF water desalination facility. The system simulation reflected the structure of the Khubar II MSF plant in Saudi Arabia, including 3 Heat Rejection Sections, 19 Heat Recovery Sections, and 9 model variables. The focus is on highlighting potential threats, vulnerabilities, and effects of different systems. Figure 3 illustrates an example of the MSF process and its components within the context of simulated attacks [26].

The MSF desalination process consists of three stages: the recovery stage, the brine heater stage, and the reject stage. In the recovery stage, seawater is drawn into the system and undergoes various treatments to remove impurities. Parameters monitored during this stage include the top brine temperature, which indicates the temperature of the concentrated seawater, and the distillate flow rate, which measures the amount of purified water produced. Next, in the brine heater stage, the concentrated seawater
is heated to increase its temperature. This process helps in separating the pure water from the brine solution. Key parameters monitored in this stage include the brine temperature, which signifies the temperature of the concentrated solution, and the heat input, which measures the energy supplied to heat the brine. Finally, in the reject stage, the concentrated brine solution is separated from the pure water, which is the desired output. Parameters of interest during this stage include the reject flow rate, which quantifies the amount of concentrated brine being discharged, and the product water quality, which assesses the purity of the desalinated water $[4,26]$. The variables included in the model and analysis are in Table 2.

### 5.2 Implementation of the Proposed Method

The MBN is constructed as a multilayered network that includes layers representing the simulated attacks, the plant's components, functionalities, and an impact layer representing the consequences of these attacks. The impact layer represents potential financial, operational, energy-related, hazardous, and environmental consequences. This network, built using expert domain knowledge and the specific details of the Khubar II MSF plant, integrated the results from the attack simulations to create a realistic and dynamic representation of the plant's operational state under potential threats.

With the MBN established, DP is applied to identify the optimal attack paths. This process pinpoints the paths with the potential for maximum disruption or damage to the system. The final stage of the implementation process involves calculating the potential costs associated with each identified optimal attack path. These costs represent the potential damages resulting from a successful attack, considering factors such as disruption to plant operation, mitigation or repair costs, and other relevant factors. The


Table 2: Summary of distillation system parameters.
![img-4.jpeg](img-4.jpeg)

Figure 4: Impact of various attacks on the distillate flowrate $\left(W_{d}\right)$.
![img-5.jpeg](img-5.jpeg)

Figure 5: Impact of various attacks on the top brine temp $\left(T B_{0}\right)$.
operational parameters are monitored and recorded closely during these simulations to document the changes induced by the attacks. The recorded values are subsequently compared to their respective
measurements taken prior to the attacks. The impacts of the different attacks on $W_{d}$ and $T B_{0}$ are showcased in Figure 4 and Figure 5, respectively.

### 5.3 Simulated Attacks

The simulation is conducted using MATLAB Simulink. It provides a virtual environment to implement and test the proposed method for detecting and mitigating cyber-attacks in the MSF plant [4, 26]. Based on the simulation model, there are 11 sensors, 3 controllers, and 11 actuators. The execution of the simulation involves implementing a predefined series of 20 attack scenarios. Each attack scenario is executed separately to assess its individual effects on the operational parameters of the plant. These scenarios vary greatly, including actions such as falsifying sensor readings, modifying setpoints, and launching coordinated attacks on multiple components of the system. The details of these attacks are shown in Table 3, which presents a comprehensive overview of the different strategies employed. The attacks discussed in this paper represent only a portion of the 20 executed scenarios, which effectively demonstrate the diverse range of attack strategies utilized. Specifically, the attacks examined in the following subsections focus on strategies that directly target parameters crucial to the plant's performance metrics (as referenced in Section 4.4.2).

### 5.3.1 Attacks on Controllers.

ATTK3: $T B_{0}$ is a crucial parameter, representing the starting temperature at which seawater is heated to stimulate evaporation in the MSF desalination process. It directly influences the initial rate of evaporation, energy efficiency of the process, the rate of scaling and corrosion, and the quality of the produced freshwater. In order to assess its vulnerability, the attack is engineered to periodically inject random variables, leading to a decrease in the $T B_{0}$ setpoint. The manipulation of this setpoint had significant implications on system operations. As the system strove to adjust to the reduced setpoint, its temperature response became erratic, vacillating between 90 and $97^{\circ} \mathrm{C}$ instead of retaining a steady $94^{\circ} \mathrm{C}$. This setpoint disturbance generated a ripple effect on the distillate flow rate, causing it to undulate between 20.64 ton/min and 17.89 ton/min. The reduction in brine heating, instigated by the lowered setpoint, led to a decrease in evaporation rates and, correspondingly, diminished freshwater production. The plant's overall operational efficiency is jeopardized, and there is an escalated risk of equipment damage due to overheating or corrosion.


Table 3: Summary of some of the executed attacks.

ATTK4: $W_{d}$ is an integral parameter in the MSF desalination process, quantifying the volume of freshwater generated per unit of time and providing a key measure of the plant's output. The careful management of this parameter is crucial as it directly affects the volume of freshwater produced, the energy efficiency of the process, and overall system stability. In the experiment, the controller is altered by periodically injecting random variables to artificially decrease the $W_{d}$ setpoint. The system struggled to respond effectively to the reduction in output, resulting in a tangible decrease in freshwater production. Moreover, this attack instigated a periodical drop in temperature, fluctuating between $94^{\circ} \mathrm{C}$ and $90.4^{\circ} \mathrm{C}$. The lowered $W_{d}$ setpoint could lead the system to reduce its heating efforts, potentially resulting in decreased energy consumption but also compromised output and system performance.

### 5.3.2 Attacks on Sensors.

ATTK1: the attack scenario is simulated with an adversary spoofing the sensor reading of $T B_{0}$, causing the system to perceive a higher temperature value. This critical parameter influences the initial evaporation rate, energy efficiency, and the overall quality of the produced freshwater in the MSF desalination process. The system, assuming the input temperature to be higher than actual, responded by lowering its heat contribution, consequently causing a real decrease in temperature. The temperatures fluctuated irregularly between 84 and $93^{\circ} \mathrm{C}$ Celsius, rather than maintaining a steady $94^{\circ} \mathrm{C}$. This disturbance, initiated by the spoofing attack, led to reduced evaporation rates and thus, decreased the overall efficiency of the desalination process and freshwater production.

ATTK2: this attack involves spoofing the distillate flowrate sensor. In the attack, the spoofed sensor signaled a higher flowrate, tricking the control system into believing it is overproducing. Consequently, the system slows down its operations, erroneously aiming to align production with the deceptive setpoint. This caused a tangible decrease in the actual distillate flowrate, from a steady 20.17 ton/min to fluctuating values between 15.95 and 18.4 ton/min.

### 5.4 Constructing Risk Assessment Networks

Following the execution of the attacks and subsequent observation of their implications, the risk assessment network is created following Section 4.2. This process yields a multilayer network that encapsulates a broad array of factors influenced by the executed attack. The network's structure is primarily guided by the various layers representing critical elements including the executed attack strategy, compromised MSF components, affected functionality, and resulting impacts. A clear depiction of this is derived from the adjacency list, which translates to nodes and edges in the network, as shown in Figure 6.

The adjacency list, formulated as a Python dictionary, serves as a fundamental building block for the network. It contains nodes representing various stages in the attack sequence, following MITRE's ATT\&CK framework. The sequence begins with a "Remote Attack", moving through the stages of exploiting different system vulnerabilities such as "Vuln in Access Authentication" and "Vuln in Elevation of Privilege" leading to attack types like "Initial Access Attack" and "Persistent Attack". This would enable the attacker to adjust the setpoint for the controller easily. It finally ends with the attack consequences, such as "Low distillate rate" and "Energy consumption increase". This list also quantifies the likelihood of transitioning from one node (or stage) to another, serving as the weights of the network's directed edges. Each node in the adjacency list is linked to its subsequent nodes along with associated transition probabilities. For instance, the transition from the "Remote Attack" to "Vuln in Access Authentication" has a probability of 1 , suggesting an inevitable progression.

### 5.5 Optimal Path

This process employs a well-defined approach, incorporating the established risk assessment network. The first step involves calculating the base probabilities for each system vulnerability using the Eq. (3). This equation assists in quantifying the likelihood of a specific vulnerability being exploited, derived from the threat model in 4.1. Subsequent to this, the joint probabilities for each potential attack path are computed, where each path through the network is a sequence of system vulnerabilities. Joint probability of a path is calculated as per Eq. (4). It represents the product of the individual probabilities of nodes (vulnerabilities or events) and their transition probabilities along the path. A path with a higher joint probability indicates that these vulnerabilities present an attacker with a more probable and faster route for the attack.

For instance, consider examining the path from "Remote Attack" to "Control Modification" in ATTK3. In the attack layer, each node represents a phase in the attack sequence, exploiting a vulnerability or executing an attack type. The directed edges that connect

![img-6.jpeg](img-6.jpeg)

Figure 6: Depiction of the risk assessment model's layered network.
![img-7.jpeg](img-7.jpeg)

Figure 7: Optimal attack strategy for ATTK3.
these nodes embody the transition probabilities, symbolizing the likelihood of an attacker progressing from one phase to the next. The joint probability of this particular path is computed as the product of the probabilities of each individual phase and their corresponding transition probabilities, as per Eq. (4). Upon successful execution of an attack in the attack layer, the subsequent layers in the network are affected. In the compromised component layer, the nodes represent the system components that are compromised due to the preceding attack layer. For instance, following a "Control Modification" attack, the " $T B_{0}$ Controller" node in the compromised component layer may be affected. Similarly, the functionalities layer contains nodes representing the functional aspects of the system that are affected due to compromised components. For instance, the "Distillate flow rate" might be impacted due to the compromise of the " $T B_{0}$ Controller". Finally, the impacts layer represents the repercussions of the disturbed functionalities on the overall system. Here, the nodes can symbolize various impacts, such as "Low distillate Rate" or "Energy consumption Increase".

In essence, a single path in the attack layer triggers a cascade of events across all subsequent layers, culminating in certain impacts on the system. The joint probability of the path in the attack layer influences the probabilities in all other layers, thereby providing a comprehensive risk assessment. After the joint probabilities of all paths are calculated, DP is applied, as shown in Algorithm 1, to identify the path with the maximum joint probability - the optimal path. DP is used to keep track of the maximum probability for each node and the parent node of each node, allowing us to reconstruct the path with the highest joint probability. In Figure 7, the optimal attack strategy is highlighted in dotted red arrows.

Lastly, the probabilities for each event within the system are computed using Eq. (14). This calculation further refines the understanding of the attack scenarios by emphasizing the events most likely to occur regardless of the status of other variables. In conclusion, the optimal path once identified, reflects the most likely sequence an attacker would follow considering the probabilities associated with each step.

## 6 ANALYSIS AND DISCUSSION OF RESULTS

This section presents a detailed analysis of several experimental attacks on different components of the MSF desalination plant. Using the system's parameters and relevant mathematical models, the potential operational losses prompted by these attacks are computed. The results of this risk assessment are then comprehensively presented. Then, the study concludes with a thorough discussion on the methodology, its strengths and limitations, and an interpretation of the findings.

### 6.1 Risk Assessment

In the context of risk assessment, Eqs. (6), (7), and (8) are utilized to calculate the operational losses. Additionally, the potential environmental and hazardous losses are estimated. Table 4 presents a comprehensive assessment of various potential attacks, including their associated risks and the projected financial losses over a one-year period. One noteworthy example is ATTK3, which could result in an annual loss of $\$ 1,103,128.45$. This scenario may be particularly attractive to skilled attackers capable of executing intricate attacks. However, it is important to note that the complexity of this attack implies that it would require significant expertise for successful execution. The estimated risk associated with ATTK3 over a single year is $\$ 687,737.93$, and the cumulative risk over a span of 5 years amounts to $\$ 3,438,689.65$. This highlights the substantial long-term risk that such an attack can pose if not appropriately managed or mitigated. On the other hand, ATTK1 may be more suitable for less experienced hackers or those with limited resources. With a probability of 0.97 and a yearly loss of $\$ 166,860.90$, this attack presents an option for attackers seeking higher chances of success with lower costs. Ultimately, the choice of the "best" attack depends on the attacker's objectives, available resources, and risk tolerance. Analyzing the table, it is shown that ATTK4 has a moderate probability and annual impact, resulting in relatively lower estimated annual and five-year risks. Conversely, ATTK2 attack exhibits a higher probability and impact, leading to elevated risks. Of particular significance is ATTK3, which stands out due to its exceptionally high annual impact. Consequently, it is associated with significantly higher estimated annual and five-year risks. Conversely, despite having the highest probability, ATTK1 demonstrates a moderate annual impact, resulting in lower annual and five-year risks compared to ATTK3.


Table 4: Risk analysis of simulated cyber-attacks on Khubar II model.

### 6.2 Optimal Attack Path

To determine the OAS, the joint product of attack probability and impact is maximized. The Algorithm 2 is applied to Table 4 to calculate the intersection values for each attack scenario. An example is ATTK4 where the $W_{d}$ controller's set point is modified: $P_{X}=0.6513, Q_{X}=\$ 166,694.81$, resulting in Intersection $=P_{X} \times Q_{X}=0.6513 \times 166,694.81=\$ 108,570.49$. By comparing the intersection values, it is determined that ATTK3 has the highest value and thus is identified as the OAS according to Algorithm 2. This implies that mitigating the risk associated with this attack should be a top priority, as it poses the highest risk in terms of both likelihood and potential impact. These observations emphasize the delicate balance attackers must strike between their capabilities, the probability of success, the potential impact, and their risk tolerance. For defenders, Table 4 serves as a critical tool for understanding where to allocate security efforts effectively to mitigate potential attacks.

### 6.3 Discussion

The research paper introduces a framework for assessing cybersecurity risks. This framework makes use of simulations based on an MSF desalination plant in Saudi Arabia. The goal is to foresee the most effective routes of cyber-attacks and determine the possible impacts of different types of threats. While the method does not focus on "zero-day vulnerabilities", it has the potential to analyze and lessen these vulnerabilities once they have been discovered.

The framework utilizes an adversarial risk analysis with the support of the MITRE ATT\&CK framework. This combination enables the anticipation of attacker actions, identification of system vulnerabilities, and understanding of their interconnectedness. By considering the presence of vulnerabilities and their relationships, the method facilitates realistic and practical risk evaluations. The risk assessment model is based on MBNs, which presents different stages of possible cybersecurity breaches in a hierarchical structure. This aids in the identification and evaluation of vital assets, processes, and the possible impacts of attacks. By using BNs, the model allows for probability-based reasoning and uncertainty management in real-world systems. It also offers a systematic way to update probabilities when new data becomes available. A vital part of the method is the OAS algorithm. This algorithm examines all possible scenarios to find the most likely and damaging attacks, assisting security analysts in prioritizing threats. It enables the development of targeted strategies to reduce the potential impact of an attack effectively, even if the source is unknown.

Despite its thorough approach, the method has several limitations. It depends on expert opinions, which, while helpful for
adding real-world insights, can introduce potential bias and subjectivity. As a result, the method's effectiveness depends on the accuracy and impartiality of the experts involved. Furthermore, the method assumes the availability of accurate historical data and process literature, which may not always be true in real-world industrial control system environments. Additionally, the model's complexity may lead to increased computational demands and could be challenging to handle in settings with limited resources. Finally, despite the OAS algorithm's ability to consider different attack scenarios, the unpredictability of zero-day vulnerabilities may still present a significant challenge.

## 7 CONCLUSIONS

This paper introduces a comprehensive risk assessment method for ICS facilities, which is implemented and evaluated through a desalination water plant simulation. Various attacks are analyzed, and the mathematical model of the desalination plant is incorporated to conduct precise risk calculations. The method combines MBNs with DP to accurately assess and manage the associated risks. The MBNs capture the intricate relationships and interdependencies within the system, while DP facilitates the prioritization of mitigation efforts based on the calculated risks. The implementation of the method in the desalination plant simulation, along with the integration of the plant's mathematical model, enables tangible risk calculations and the consideration of operational and security factors. This approach significantly enhances the accuracy and relevance of the risk assessment, contributing to the overall security and stability of critical infrastructure.

Future research directions include incorporating human factors, addressing physical security threats, and managing interdependencies within facilities. Future studies could explore the time-dependent changes and temporal dependencies. Real-world or testbed-based implementations are necessary to validate and assess the effectiveness of our approach in ensuring the safety, security, and sustainability of critical infrastructure like water desalination plants. Such implementations would provide valuable insights and further validate the practicality and efficiency.
