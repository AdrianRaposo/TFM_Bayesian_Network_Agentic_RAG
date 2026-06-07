# scientific reports 

## OPEN A dynamic decision-making approach for cabin unlawful interference emergency disposal using dynamic Bayesian network

Yu Wu ${ }^{1 / 2}$, Shiting $\mathrm{He}^{1}$ \& Jinxin Shi ${ }^{2}$


#### Abstract

Disposal of unlawful interference incidents is essential for is crucial for the advancement of aviation security. Effective emergency disposal requires a comprehensive approach that includes the perspectives of airlines, airports, and passengers. In this context, each component of the disposal process can fail randomly. The objective of this research is to optimize emergency disposal decisions to enhance the efficiency of civil aviation operations, reduce accidents, and lower costs. Given the dynamic complexity of unlawful interference incidents, a dynamic fault tree consisting of 26 nodes was constructed to analyze the emergency disposal process. To explore the relationships and priorities of each event, the Dynamic Fault Tree is converted into a dynamic Bayesian network. Based on historical statistical data, simulation analysis is conducted in three aspects: posterior probability, sensitivity, and importance. Simulation results reveal that the top three critical nodes in cabin unlawful interference incidents are "structural damage to the cabin," "inadequate training by airlines," and "untimely airport police takeover of disruptive passengers." Further analysis shows that (1) most of the critical nodes are associated with airlines. (2) The decision-making rationale and pathways of the critical nodes can be clearly observed and prioritized. (3) Besides airlines, other entities such as airports can implement targeted emergency disposal measures. Through quantitative analysis and simulation, this study provides decision-making guidance for participating groups on dynamic emergency disposal, thereby enhancing civil aviation security.


Keywords Unlawful interference incidents, Aviation security, Dynamic emergency disposal, Dynamic Bayesian network, Importance analysis

Unlawful interference incidents in the cabin may be accompanied by fires or explosions, posing a significant threat to aviation security. Preventing unlawful interference incidents is a core task in aviation security. "Unlawful interference incidents" are defined in Annex 17 Aviation Security of the Convention on International Civil Aviation as acts or attempted acts that compromise the security of civil aviation and air transport, including actions such as the destruction or intrusion of aircraft. Due to their suddenness, complexity, destructive potential, and high degree of interconnectedness, these incidents necessitate a focused examination of the mechanisms underlying their occurrence. Between 2007 and 2017, the International Air Transport Association (IATA) received over 66,000 reports of incidents involving disruptive passengers. These incidents are categorized as "minor incidents," "medium incidents," "severe incidents," and "cockpit security incidents" according to the International Civil Aviation Organization (ICAO) classification. In recent years, the number of incidents classified as "severe incidents" or "cockpit security incidents" has been steadily increasing. Of the 8731 incidents reported in 2017, 3 percent were classified as "severe incidents" and 1 percent as "cockpit security incidents," where a passenger either attempted to enter the cockpit or engaged in behavior deemed to jeopardize flight security. According to the Aviation Safety Network (ASN), between 2017 and 2022, there were 100 accidents worldwide caused by disruptive passengers. Of these, 20 resulted in fatal accidents, leading to 152 fatalities and causing the aircraft to be either irreparable or severely damaged. According to the Federal Aviation Administration (FAA), there were 14,392 disruptive passenger incidents reported between 2017 and 2024. According to the China Statistical Communique on the Development of the Civil Aviation Industry in 2022, 7638 security incidents were investigated and addressed. Among these, "destruction or intrusion of aircraft incidents" were particularly likely to result in

[^0]
[^0]:    ${ }^{1}$ College of Safety Science and Engineering, Civil Aviation University of China, Tianjin 300300, China. ${ }^{2}$ Cabin Academy, Civil Aviation University of China, Tianjin 300300, China. ${ }^{3 / 4}$ email: y_wu@cauc.edu.cn

fires or explosions, leading to the most severe consequences. The consequences of unlawful interference incidents in the cabin are serious, and unlawful interference by passengers occurs relatively frequently. If participants fail to address unlawful interference incidents promptly and effectively, it poses a significant threat to the safety and security of the aircraft, crew, and passengers. This requires dynamic decision-making based on a thorough understanding of the incident progression to ensure a swift and effective response. Therefore, international civil aviation authorities, civil aviation operating departments, and airport police are urgently focused on the rapid and effective management of unlawful interference incidents to minimize losses.

Research on unlawful interference incidents has primarily concentrated on enhancing the international legal framework, defining legislative concepts^{3,5}, and addressing the accountability of disruptive passengers^{4,4}. Although some scholars have assessed the risk of unlawful interference incidents^{5}, most studies have approached the issue from a static behavioral perspective, neglecting the need for dynamic decision-making in emergency disposal. Countries emphasize emergency disposal responsibilities and penalties for unlawful interference incidents, yet often overlook the necessity of dynamic decision-making in effectively managing these emergencies. For example, in the United States, incident investigations are conducted under 14 CFR Part 13, with civil penalties enforced according to 49 U.S.C. transportation regulations. In Europe, penalties for disruptive passengers are governed by Regulation (EC) No. 2016/679 of the European Parliament and Council, as well as the EU Aviation Security Regulation. In China, such penalties are enforced under the Law of the People's Republic of China on Administrative Penalties for Public Security (Presidential Decree No. 38).

In summary, the implementation of comprehensive laws and regulations can effectively reduce the occurrence of unlawful interference incidents. However, existing studies have several limitations. Firstly, unlawful interference incidents are often treated as static events, concentrating solely on case-specific reasoning and disposal strategies after a single incident occurs. These studies tend to overlook the ongoing impact of the incident process and the need for dynamic disposal. Secondly, there is a lack of targeted research specifically addressing cabin unlawful interference incidents. The consequences and emergency disposal decision-making for these incidents evolve dynamically with time, events, and the entire disposal process. To address these gaps, this research aims to explore dynamic decision-making processes in emergency disposal procedures for unlawful interference incidents within cabin environments. By analyzing the process of unlawful interference incidents, this study identifies the decision-making challenges faced by participants and emphasizes the dynamics of emergency disposal. This article primarily addresses the following three problems: Problem 1: How should participating groups respond after unlawful interference incidents occur in the cabin? Problem 2: Which events in the emergency disposal process are more likely to exacerbate unlawful interference incidents? Problem 3: What measures can be taken for dynamic decision-making during the emergency disposal of unlawful interference incidents?

The Dynamic Fault Tree (DFT) focuses on the process of incident occurrence^{6}, while Dynamic Bayesian Networks (DBN) are well-suited for solving dynamic decision problems^{7}. Therefore, this research utilizes DFT theory to identify events and their sequence in the emergency disposal process for unlawful interference incidents, thereby enhancing existing emergency response procedures and addressing Problem 1 in Section "Cabin unlawful interference emergency disposal process". Additionally, DBN is employed to quantitatively analyze interrelationships and priorities among different nodes. The analysis results include posterior probability calculations, sensitivity assessments, and importance evaluations for each node. Problem 2 is addressed in Section "Model construction" and Section "Importance analysis". These calculation outcomes reveal key steps involved in handling destruction or intrusion of aircraft incidents during emergency disposal processes, providing a scientific basis for dynamically resolving unlawful interference incidents within cabins. The solution to Problem 3 is presented in Section "Discussion".

## Literature review

### Research of unlawful interference incidents

As a closed and restricted space similar to a subway compartment, the aircraft cabin significantly limits the available methods for emergency disposal of unlawful interference incidents. Unlawful interference incidents on public transportation have serious consequences and negative social impacts. Therefore, research on the disposal of unlawful interference incidents in closed and restricted spaces primarily focuses on the mechanisms of occurrence and the prevention and control of such behaviors.

In researching the occurrence mechanisms of these incidents, it analyzes the regulations related to interfering with normal traffic operations and proposes corresponding countermeasures and suggestions. Based on an analysis of 134 international metro operation accidents, Wang et al.^{8} utilized complex network theory to examine the interference incidents that impact the vulnerability of metro systems. Song et al.^{9} combined and summarized various types of metro operation interference sources by analyzing metro operation accidents and risk lists. In addition, he used the accident chain to describe the relationship between interference sources. Feng et al.^{10} analyzed the impacts of extreme incidents such as extreme weather, mechanical failures, and human damage on transportation networks from the perspective of high-speed railroad and air transportation networks. Based on three characteristic elements of exposure, sensitivity, and adaptability, Duan et al.^{11} identified the factors influencing the vulnerability of subway stations under passenger flow disturbance. Wang^{12} studied the unlawful interference disposal plan before takeoff and during flight, aiming at the problem of unlawful interference disposal at Shandong Airlines.

In the prevention and control of unlawful interference behavior, Zuo^{13} conducted an in-depth analysis on three aspects: airport security personnel, facilities, and organizational management. The prevention and control system for airport unlawful interference behaviors was evaluated using hierarchical analysis to construct an evaluation index system. Walter et al.^{14} focused on researching the impact of airport security personnel's communication style on team coordination strategies. A field investigation was conducted to analyze team and

communication dynamics under both threat and non-threat conditions. They found that team performance significantly benefited from active “push” communication and non-task-related interactions, providing specific measures for the training of airport security personnel. In assessing the efficiency of airport baggage security screening, Jacek et al.^{15} considered both human and technical factors, including subjective elements such as operator assessment, error tendencies, and organizational methods for process control. In addition, passengers' decisions are influenced by various complex factors, such as unobservable human heterogeneity^{16}. Therefore, preventing and controlling passengers' unlawful interference behavior requires dynamic decision-making.

Overall, numerous studies have examined unlawful interference incidents, focusing on both the mechanisms of these incidents and strategies for behavioral prevention and control. These findings have provided valuable research directions for preventing and combating unlawful interference incidents in closed and restricted spaces. However, current research still lacks in-depth analysis of the incident process and the dynamic decision-making involved in emergency disposal. Moreover, the actual situation of these incidents is complex and variable. There is limited literature on quantitative research regarding emergency disposal, making it difficult to assess key events in the process.

### Research on dynamic fault tree and dynamic bayesian network

Emergency disposal of cabin unlawful interference is both dynamic and complex. Assessing dynamic and complex systems requires dynamic approaches. There are many methods of incident analysis, such as Event Tree Analysis (ETA)^{17}, Root Cause Analysis (RCA)^{18}, Failure Mode and Effects Analysis (FMEA)^{19}, and Fault Tree Analysis (FTA)^{20}. ETA is used to analyze the potential consequences of a single initial event^{21}. RCA has limitations in establishing causation for incidents^{22}. FMEA is typically employed during the system design and improvement phases^{23}. Each of these methods presents challenges in identifying key nodes and causal relationships in complex cabin unlawful interference incidents.

In contrast, FTA focuses on analyzing the causal relationships of events. It can systematically identify and illustrate the factors and their interrelationships that lead to unlawful interference incidents in the cabin. This approach aids in developing effective emergency disposal strategies and preventive measures. Additionally, DFT analysis considers the system's dynamic behavior over time, making it more aligned with the real-world scenarios of unlawful interference incidents. Therefore, DFT is widely used for accident analysis. He^{24} and Chen et al.^{25} combined DFT with Markov models to account for the impact of time on the probability of accident occurrence, enhancing reliability analysis. Ahmet et al.^{26} analyzed the risk of fire and explosion accidents in bulk carriers through fuzzy logic, Fault Tree Analysis (FTA), and Cut-Set Importance measurement (CS-I) techniques. Zhao et al.^{27} proposed a DFT technique modeling approach to model ship collision accidents and loss of cold accidents (LOCA). This model described the fault propagation process of a dynamic system and reflected the dynamic changes of the entire accident system.

Although DFT can describe the dynamic behavior of a system, it primarily focuses on the logical relationships and conditional combinations of incident occurrences. It only provides limited support for dynamic emergency decision-making. Therefore, this paper adopts DBN to address the dynamic decision-making problem in emergency disposal of unlawful interference incidents. DBN represents time-series data through probabilistic graphical models, which is able to deal with system state changes and uncertainty. It is well-suited for addressing decision-making issues in dynamic environments. Moreover, it can compute posterior probabilities given observed evidence, providing predictions of future states and supporting decision-making. Currently, many scholars integrate DBN with accident models to develop new assessment methods. These methods analyze the mechanisms of accidents to identify weak nodes, thereby providing valuable decision support for decision-makers. It mainly covers the three aspects of the hardware equipment, the software system, and incident disposal decisions. Firstly, in terms of hardware equipment, DBN has been extensively studied in reliability assessment^{28,29} and maintenance decisions^{30,31}. Researchers used importance, sensitivity, and resilience to assess system performance. Secondly, in terms of software systems, DBN provides an innovative approach to assessing the resilience and toughness of a system^{32,33}. They also provide a novel methodology for evaluating the emergency disposal process for cabin unlawful interference incidents. In addition, Bayesian Network is widely used in influencing factor analysis^{34,35}, and some scholars have applied DBN to risk assessment^{36,37}. These studies utilize posterior probabilities and conditional probabilities to identify factors that impact the DBN. Thirdly, in the realm of incident disposal decision-making, the integration of DBN and scenario projection provides new ideas for crisis emergency decision-making^{38,39}. This combination provides new insights for studying unlawful interference incidents in the cabin.

In this paper, DFT is constructed to identify and illustrate the various possible paths and critical conditions of unlawful interference incidents in the cabin. Based on these paths and conditions, DBN is constructed for dynamic probabilistic reasoning. Posterior probability analysis is used to understand the system's behavior in different states. Sensitivity analysis is conducted to identify which events have the most significant impact on outcomes, guiding decision-making and resource allocation. Importance analysis is performed to determine which events are critical to overall system behavior, providing a foundation for incident management and prevention. Based on the calculation results, targeted recommendations are made to enhance emergency disposal procedures for airlines and aviation security in China.

## Dynamic fault tree of sustainable emergency disposal Cabin unlawful interference emergency disposal process

### Conceptual definition

To clarify the emergency disposal process for cabin unlawful interference incidents and delineate the responsibilities of each participating group, this research will precisely define these groups in accordance with relevant

international laws and regulations. It ensures that clear guidance and guarantees are provided for disposing of unlawful interference incidents, which improves the efficiency and accuracy of emergency disposal and further safeguards aviation security.

According to Chapter I of Annex 17 Aviation Security of the Convention on International Civil Aviation and the Rules for Safety and Security in Flight for the Transport of Passengers by Public Aviation (CCAR-332-R1), “unlawful interference incidents” are defined as acts or attempted acts that endanger the security of civil aviation and air transport. This includes “unlawful hijack aircraft”, “destruction of aircraft in use”, “forced intrusion aircraft”, “hostage-taking on board” and so on.

According to Annex 17 Aviation Security of the Convention on International Civil Aviation, “emergency disposal of cabin unlawful interference incidents” refers to the measures and procedures implemented to ensure the safety and security of airlines and associated airports in response to unlawful interference by passengers. According to article 24 of the Rules for In-Flight Safety and Security of Public Air Transportation of Passengers (CCAR-332-R1), “crew” refers to the members of the flight crew, which is a collective term for the pilots, flight attendants, airline security guards and other aircrew members who perform duties on civil aircraft in flight. The crew is responsible for the safety and security of the flight. According to article 27 of the Civil Aviation Emergency Management Regulations of China (CCAR-397), “Airplane Operating Control” refers to the department within an airline responsible for unified scheduling, command, and centralized management of operational flights. The AOC manages the transmission of information and intelligence between the aircraft and ground operations. According to article 7 of the Law of the People's Republic of China on Penalties for Public Security Administration (Decree No. 38 of the President of the People's Republic of China), “airport police” refers to the public law enforcement officers assigned to airports, responsible for maintaining public security within their jurisdiction. They have the authority to impose administrative penalties and investigate criminal cases. According to article 11 of the Civil Aviation Emergency Management Regulations of China (CCAR-397), “airport emergency command team” refers to the on-site team established by the airport following an unlawful interference incident, responsible for organizing, directing, and coordinating emergency disposal efforts.

According to the definition of disruptive passengers in chapter I of Annex 17 Aviation Security of the Convention on International Civil Aviation, “disruptive passengers” are passengers who violate the rules at aircraft or who fail to comply with the requests of crew, thereby disturbing the order and operation of aircraft.

### Emergency disposal process identification

According to the regulations and actual case analysis, this study analyzes the typical incidents of unlawful interference—destruction or intrusion of aircraft incidents as the research object. When unlawful interference incidents occur in the cabin, the relevant participants perform their respective duties to collaboratively manage the situation. Consequently, a cross-functional emergency disposal flow chart for cabin unlawful interference incidents has been developed, as shown in Fig. 1.

Figure 1 depicts the detailed emergency disposal process. When an unlawful interference incident occurs in the cabin, the crew first assesses the situation. The accuracy of the situational assessment depends on the training of the crew by the airline as well as crew capability^{40}. Next, the crew undertakes an initial response to the incident. The success of the initial disposition depends on the crew's adherence to established procedures for handling disruptive passengers. If disruptive passengers cease their interference, they will be handed over to airport police once the aircraft has landed. Conversely, if the disruptive passengers continue their interference and the situation escalates, the captain will decide to activate the emergency disposal procedures. The crew follows established procedures to dispose of the incident. The captain informs the AOC, which then notifies the airline to provide the appropriate disposal procedure manual and alerts the airport to establish an emergency command team for coordination and response. After the aircraft has landed, the disruptive passengers will be handed over to the airport police for incident investigation and punishment. Whether or not subsequent incidents of unlawful interference occur will depend on the deterrent effect of the punishment administered. Figure 1 aids in constructing the DFT, identifying critical nodes and the cause-and-effect relationships between them. Ultimately, it supports decision-making by clarifying these elements.

## Dynamic fault tree construction

### Model construction

Unlawful interference incidents in the cabin involve multiple causal paths with intricate causal relationships and dependencies between events. These incidents exhibit temporal dynamics, evolving over time. Additionally, these incidents involve a degree of uncertainty, as various factors may occur and interact with different probabilities. Its emergency disposal requires consideration of a variety of factors, such as the interaction between the crews and the passengers^{41}. However, DFT analysis can effectively describe such incidents. DFT is a safety assessment method that integrates Markov theory with combinatorial mathematical techniques. Dynamic logic gates are introduced to describe the timing failure behavior in the system^{42}. It can systematically display the multiple causal paths of unlawful interference incidents through logical relationships and conditional combinations. By incorporating time and probability, DFT analysis can accurately depict changes in system states, offering a comprehensive analysis of the development process of unlawful interference incidents. The method can be applied to fault-tolerant systems with dynamic random faults, sequential correlation redundancy systems, and systems with common repositories^{43}.

When unlawful interference incidents occur in the cabin, disruptive passengers may either choose to comply with the law and cease their interference, or they may choose to continue their unlawful behavior. When disposing of the incidents, the crew may choose to dispose of them in order to minimize losses and safeguard the lives of passengers. Meanwhile, they may also dispose of it incorrectly or fail to dispose due to problems such as

![img-0.jpeg](img-0.jpeg)

**Figure 1.** Cross-functional emergency disposal flow chart of cabin unlawful interference incidents.

blurred law enforcement boundaries and insufficient security capabilities. When the crew hands over the disruptive passenger, the airport police may choose to impose criminal penalties to curb the recurrence of the unlawful interference incident, or there may be no penalties or only fines^{44}. The decision-making actions of disruptive passengers, crew, airline, and airport are complex and dynamic. Therefore, DFT analysis is used to describe the emergency disposal process for cabin unlawful interference incidents. In DFT, failure modes are not only described by combinations of basic events but also consider the sequential relationships between these events^{45}.

Flight delays may be caused by multiple factors, such as weather. Additionally, the enclosed cabin environment and the complexity of the physical situation may contribute to passengers becoming emotionally unstable. Therefore, there is a high risk of unlawful interference incidents. Now, using cabin unlawful interference incidents as the top event, the DFT for these incidents is constructed based on Fig. 1. The top event T is identified as cabin unlawful interference incidents. The next layer of intermediate events is divided into unsafe individual acts and unsafe physical conditions according to 24 modes^{46}. Thus, the next layer of events include improper emergency disposal (A1) and structural damage to the cabin (A2). Here the two events are connected with PAND: Cabin unlawful interference incidents occur when both A1 and A2 occur, and the event A1 occurs first and the event A2 occurs later. A1 is mainly caused by three events: misoperation of crew disposal (A3), violations of airline (A4), and untimely airport ground rescue (A5). Besides, based on the previous accident cause statistics for destruction or intrusion of aircraft incidents, A2 was attributed to inappropriate emergency disposal equipment (A6) and unreasonably designed disposal procedures (A7). Meanwhile, there are three reasons that cause event A6: incorrect crew judgment situations (A8), incorrect airline notification information (A9), and incorrect airport command (A10). Considering the actual scenarios of cabin unlawful interference incidents, the basic events of the DFT are defined as B1 to B15. Based on the above analysis, the DFT of the cabin unlawful interference incidents is constructed, as shown in Fig. 2.

![img-1.jpeg](img-1.jpeg)

**Figure 2.** DFT model of cabin unlawful interference incidents.

### *Importance analysis*

When analyzing Fig. 2 for critical nodes, the events exhibit varying levels of importance. Importance is a quantitative indicator used to assess the significance of an event in the analysis of processes. Importance analysis can provide a basis for identifying critical nodes of processes and improving process reliability^{47,48}. Its methods are all directly or indirectly based on traditional FT. These methods are limited to the static failure behavior that can be described by existing static logic gates such as AND and OR. For systems with complex and diverse failure logics, it is difficult for traditional FT to portray the full range of static failure behaviors^{20}. But in DBN, event importance can be calculated by using its inference algorithm.

1) **Probability importance.** Probability importance indicates the changeable degree of process failure probability caused by the root node state change. It reflects the change of the process failure probability caused by the root nodes when going from non-occurrence to occurrence. When the leaf node Y_{m}(m = 1, ..., M) fails at time t, the probability importance of the root node X_{n}(n = 1, ..., N) is:

$$I_{n}^{P_t} \left(X_n, Y_{m}^{t} = 1\right) = P\left(Y_{m}^{t} = 1 \mid X_n = 1\right) - P\left(Y_{m}^{t} = 1 \mid X_n = 0\right)$$

Herein, P(Y_{m}^{t} = 1|X_{n} = 1) is the conditional probability that the leaf node Y_{m} occurs at time t when the root node X_{n} occurs. P(Y_{m}^{t} = 1|X_{n} = 0) is the conditional probability that the leaf node Y_{m} occurs at time t when the root node X_{n} does not occur.

2) **Critical importance.** Critical importance indicates the ratio of the changeable rate of root node failure probability to the changeable rate of process failure probability. When the leaf node Y_{m} fails at time t, the critical importance of the root node X_{n} is:

$$I_{n}^{C_t} \left(X_n, Y_{m}^{t} = 1\right) = \frac{P(X_n = 1)}{\sum_{t=0}^t P\left(Y_{m}^{t} = 1\right)}I_{n}^{P_t} \left(X_n = 1, Y_{m}^{t} = 1\right)$$

Herein, P(X_{n} = 1) is the occurrence probability of the leaf node Y_{m} corresponding to the root node X_{n}.

### **Dynamic Bayesian network of sustainable emergency disposal Model introduction**

Dynamic Bayesian Networks extend static Bayesian Networks into the temporal domain, incorporating an explicit temporal dimension^{49}. They include common causes and multi-state variables, enhancing the analytical capabilities of traditional Bayesian Networks^{50}. The DBN for cabin unlawful interference incidents is a transition model that relies on stochastic probability distributions. It divides a set of random variables into time segments and defines a set of conditional probability assumptions. Its time-invariant character ensures that the dependency

model between variables remains constant at any moment. DBN provides an applicable framework when multiple time segments are required for cabin unlawful interference incidents to accurately characterize system evolution over time^{53}. The DBN features are a set (V_{1}, V_{--}). Among them, V_{1} is a Bayesian Network that presents a prior probability P(V_{1}). It defines the joint probability distribution of cabin unlawful interference incident nodes in the initial state, which can be obtained as the prior probability of any node. V_{--} is a two-time series time network^{52} that represents the state transfer probabilities of variables between neighboring time segments. It uses directed acyclic graphs to define P(X^{t+Δt}|X^{t}). Assuming that the discrete variable is V = {X_{1}, X_{2}, X_{3}, ....., X_{n}}, the joint probability distribution is:$$P(V)=P\left(X_{1},X_{2},X_{3},...,X_{n}\right)=\prod_{X_{n}\in V}{P\left(X_{n} \mid Y_{m}\right)}$$Herein, Y_{m} represents the leaf node of the node X_{n}.

Assuming that the DBN consists of a finite number of time segments t, and that the directed edges between the segments conform to a first-order Markov process. It is obtained that:$$P\left(X^{t+\Delta t} \mid X^{t}\right)=\prod_{n=1}^{N}{P\left(X_{n}^{t+\Delta t} \mid Y_{m}^{t+\Delta t}\right)}$$Herein, X_{n}^{t+Δt} denotes the nth node of the time fragment t + Δt. Y_{m}^{t+Δt} denotes the leaf node of the node X_{n}^{t+Δt}.

### Conversion rule

After constructing the DFT for cabin unlawful interference incidents, the corresponding DBN can be constructed by conversion rules. DBN parameters include two aspects: for nodes within the same time segment, the conditional probability values are determined based on the logical relationships between events in the DFT. For the same node on adjacent time segments, the conditional probability relationships are determined based on a changeable time function of node performance metrics^{52,53}.

In Fig. 2, the top event T is connected to events A_{1} and A_{2} through PAND. The top event T occurs when both input events A_{1} and A_{2} occur, and A_{1} occurs before A_{2}. Where the conditional probability distribution of each node is 43:$$P\left(A_1(t+\Delta t)=1|A_1(t)=0\right)=\int_{1}^{t+\Delta t} f_{A_1}(t)dt$$$$P(A_1(t+\Delta t)=1|A_1(t)=1)=1$$$$P(A_2(t+\Delta t)=1|A_2(t)=0)=\int_{1}^{t+\Delta t} f_{A_2}(t)dt$$$$P(A_3(t+\Delta t)=1|A_3(t)=1)=1$$$$P(T=1|A_1(t+\Delta t)=1,A_2(t+\Delta t)=1)=1$$$$P(T=1|the)=0$$Herein, f_{A_{1}}(t) represents the failure density function of the intermediate event A_{1}. f_{A_{2}}(t) represents the failure density function of the intermediate event A_{2}.

The intermediate event A_{1} is connected to events A_{3}, A_{4} and A_{5} through SEQ. The input events A_{3}, A_{4}, and A_{5} must occur in left-to-right order for output event A_{1} to occur. Where the conditional probability distribution of each node is:$$P\left(A_3(t+\Delta t)=1|A_3(t)=1\right)=1$$$$P\left(A_3(t+\Delta t)=1|A_3(t)=0\right)=\int_{1}^{t+\Delta t} f_{A_3}(t)dt$$$$P\left(A_4(t+\Delta t)=1|A_3(t)=1,A_4(t)=0\right)=\int_{1}^{t+\Delta t} f_{A_4}(t)dt$$$$P\left(A_4(t+\Delta t)=1|A_4(t)=1\right)=1$$$$P\left(A_5(t+\Delta t)=1|A_4(t)=1,A_5(t)=0\right)=\int_{1}^{t+\Delta t} f_{A_5}(t)dt$$$$P\left(A_5(t+\Delta t)=1|A_5(t)=1\right)=1$$$$P\left(A_5(t+\Delta t)=1|A_4(t+\Delta t)=1,A_5(t+\Delta t)=1\right)=1$$$$P\left(A_5=1|the\right)=0$$Herein, f_{A_{3}}(t) represents the failure density function of the intermediate event A_{3}. f_{A_{4}}(t) represents the failure density function of the intermediate event A_{4}. f_{A_{5}}(t) represents the failure density function of the intermediate event A_{5}.

The intermediate event A_{8} is connected to the basic events B_{10} and B_{11} through WSP. In general, the basic event B_{10} is in normal operation and B_{11} is dormant as a spare part. When the basic event B_{10} fails, B_{11} enters the normal operating state from the dormant state. The failure rate is lower than the normal operating state when the spare part is dormant. Let the ratio of the dormant period failure rate to the operating period failure rate denote the dormancy factor α, then the WSP α is 0 < α < 1. Where the conditional probability distribution of each node is:$$P\left(B_{10}(t+\Delta t)=1|B_{10}(t)=0\right)=\int_{t}^{t+\Delta t} f_{B_{10}}(t)dtP\left(B_{10}(t+\Delta t)=1|B_{10}(t)=1\right)=1$$$$P\left(B_{11}(t+\Delta t)=1|B_{10}(t)=1,B_{11}(t)=0\right)=\int_{t}^{t+\Delta t} f_{\alpha B_{11}}(t)dt$$$$P\left(B_{11}(t+\Delta t)=1|B_{11}(t)=1\right)=1P\left(A_8=1|B_{10}(t+\Delta t)=1,B_{11}(t+\Delta t)=1\right)=1$$Herein, f_{B_{10}}(t) represents the failure density function of the basic event B_{10}. f_{αB11}(t) represents the failure density function of the basic event B_{11} in the dormant period.

The intermediate event A_{2} is connected to events A_{6} and A_{7} through AND. During the conversion to the DBN, the logical relationships between events remain unchanged^{53}. Where the conditional probability distribution of each node is:

$$
\left\{\begin{array}{c}
\mathrm{P}\left(\mathrm{~A}_{6}(t+\Delta t)=1 \mid \mathrm{A}_{6}(t)=0\right)=\int_{4}^{t+\Delta t} \mathrm{f}_{\mathrm{A}_{6}}(t) \mathrm{dt} \\
\mathrm{P}\left(\mathrm{~A}_{6}(t+\Delta t)=1 \mid \mathrm{A}_{6}(t)=1\right)=1 \\
\mathrm{P}\left(\mathrm{~A}_{7}(t+\Delta t)=1 \mid \mathrm{A}_{7}(t)=0\right)=\int_{4}^{t+\Delta t} \mathrm{f}_{\mathrm{A}_{7}}(t) \mathrm{dt} \\
\mathrm{P}\left(\mathrm{~A}_{7}(t+\Delta t)=1 \mid \mathrm{A}_{7}(t)=1\right)=1 \\
\mathrm{P}\left(\mathrm{~A}_{2}=1 \mid \mathrm{A}_{6}(t+\Delta t)=1, \mathrm{~A}_{7}(t+\Delta t)=1\right)=1 \\
\mathrm{P}\left(\mathrm{~A}_{2}=1\right) \mathrm{dse})=0
\end{array}\right.
$$

Herein, $\mathrm{f}_{\mathrm{A}_{6}}(\mathrm{t})$ represents the failure density function of the intermediate event $\mathrm{A}_{6} . \mathrm{f}_{\mathrm{A}_{7}}(\mathrm{t})$ represents the failure density function of the intermediate event $\mathrm{A}_{7}$.

Similarly, intermediate event $\mathrm{A}_{3}$ is connected to basic events $\mathrm{B}_{1}$ and $\mathrm{B}_{2}$ through OR. A DBN is built based on the temporal logic relationship of each DFT gate. Where the conditional probability distribution of each node is:

$$
\left\{\begin{array}{c}
\mathrm{P}\left(\mathrm{~B}_{1}(t+\Delta t)=1 \mid \mathrm{B}_{1}(t)=0\right)=\int_{4}^{t+\Delta t} \mathrm{f}_{\mathrm{B}_{1}}(t) \mathrm{dt} \\
\mathrm{P}\left(\mathrm{~B}_{1}(t+\Delta t)=1 \mid \mathrm{B}_{1}(t)=1\right)=1 \\
\mathrm{P}\left(\mathrm{~B}_{2}(t+\Delta t)=1 \mid \mathrm{B}_{2}(t)=0\right)=\int_{4}^{t+\Delta t} \mathrm{f}_{\mathrm{B}_{2}}(t) \mathrm{dt} \\
\mathrm{P}\left(\mathrm{~B}_{2}(t+\Delta t)=1 \mid \mathrm{B}_{2}(t)=1\right)=1 \\
\mathrm{P}\left(\mathrm{~A}_{3}=1 \mid \mathrm{B}_{1}(t+\Delta t)=0, \mathrm{~B}_{1}(t+\Delta t)=0\right)=0 \\
\mathrm{P}\left(\mathrm{~A}_{3}=1\right) \mathrm{dse})=1
\end{array}\right.
$$

Herein, $\mathrm{f}_{\mathrm{B}_{1}}(\mathrm{t})$ represents the failure density function of the basic event $\mathrm{B}_{1} . \mathrm{f}_{\mathrm{B}_{2}}(\mathrm{t})$ represents the failure density function of the basic event $\mathrm{B}_{2}$.

Based on the above analysis, the DBNs corresponding to the relevant logic gates in Fig. 2 are obtained, as shown in Table 1.

# Model construction 

According to the 2022 CII Science and Technology Report-Case Analysis of Civil Aircraft Cabin Security Incidents and Research Report on Potential Threats, the basic event failure rates of unlawful interference incidents were calculated, as shown in Table 3. The report reviewed and evaluated accidents occurring in FAR Part 25 transport category aircraft, as recorded by the NTSB and FAA, from 1997 to 2017. It extracted data including basic accident information, basic aircraft information, casualty information, engine information, accident process information, and accident cause and factor information to establish a database for analysis and research. The total
![img-2.jpeg](img-2.jpeg)

Table 1. Node conversion diagrams.

number of accidents involved in the database is 1141 (the number of accidents is defined in terms of the number of aircraft involved), and the basic information of the data in the database is listed in Table 2.

Based on the DFT structure in Fig. 2 and the conversion rules in Table 1, the DBN of cabin unlawful interference incidents is established, as shown in Fig. 3.

Based on Fig. 3, the Bayesian Network simulation software GeNIe is used to construct the DBN model of cabin unlawful interference incidents. The specific steps are as follows:
(1) According to the conversion rules, the top, intermediate, and basic events of the DFT are mapped to the leaf and root nodes of the DBN, respectively. The dependency relationships between events, which are represented by logic gates, are captured through directed edges and conditional probabilities.
(2) It is assumed that in the initial state $(\mathrm{t}=0)$, the system is completely reliable, i.e., the basic events correspond to the root nodes with priori probability of zero.
(3) It is assumed that the events are independent of each other and the failure probabilities follow an exponential distribution, i.e., the failure probability density function is $\mathrm{f}(\mathrm{t})=\lambda \mathrm{e}^{-\lambda \mathrm{t}}$. The time interval between neighboring time segments is set to 1 min . The state transfer probabilities of the corresponding root nodes between adjacent time segments are determined to characterize the time dependence of the system. Taking the node "violation of crew disposal of disruptive passengers" as an example, the state transfer probability expression of this node between two adjacent time segments is:

$$
\left\{\begin{array}{c}
P\left(\mathrm{~B}_{1}(\mathrm{t}+\Delta \mathrm{t})=1 \mid \mathrm{B}_{1}(\mathrm{t})=1\right)=\int_{\mathrm{t}}^{\mathrm{t}+\Delta \mathrm{t}} \mathrm{f}_{\mathrm{B}_{1}}(\mathrm{t}) \mathrm{dt}=\mathrm{e}^{-\lambda \Delta \mathrm{t}} \\
P\left(\mathrm{~B}_{1}(\mathrm{t}+\Delta \mathrm{t})=0 \mid \mathrm{B}_{1}(\mathrm{t})=1\right)=1-e^{-\lambda \Delta \mathrm{t}} \\
P\left(\mathrm{~B}_{1}(\mathrm{t}+\Delta \mathrm{t})=1 \mid \mathrm{B}_{1}(\mathrm{t})=0\right)=0 \\
P\left(\mathrm{~B}_{1}(\mathrm{t}+\Delta \mathrm{t})=0 \mid \mathrm{B}_{1}(\mathrm{t})=0\right)=1
\end{array}\right.
$$

According to Eq. (10), the basic event state transfer probabilities for the cabin unlawful interference incidents are calculated, as shown in Table 3.


Table 2. Basic information on the database (1141 accidents).
![img-3.jpeg](img-3.jpeg)

Figure 3. DBN of cabin unlawful interference incidents.


Table 3. Basic event state transfer probabilities. The raw data for calculating the failure rate $\lambda$ comes from 2022 CII Science and Technology Report-Case Analysis of Civil Aircraft Cabin Security Incidents and Research Report on Potential Threats.

# Probability analysis 

The leaf node "cabin unlawful interference incidents" is set as the target node using the probability update function in the GeNle software. By setting this node's state to True at $100 \%$, the posterior probabilities of the root nodes over time are obtained.

The posterior probability of each root node is obtained by DBN inference. When node T occurs, the events corresponding to the root nodes can be sequentially evaluated based on their posterior probabilities. This ordering facilitates informed decision-making for the emergency disposal of incidents. In the DBN for cabin unlawful interference incidents, the leaf node $\mathrm{A}_{2}$ is set to the state "Set Evidence $=\mathrm{T}$ ". The posteriori probability order of the root nodes is obtained by the diagnostic function of the GeNle software, as shown in Fig. 4.

As illustrated in Fig. 4, it can be seen that when the node $\mathrm{A}_{2}$ occurs, the probability order of the root nodes is: $B_{10}>B_{1}>B_{6}>B_{15}>B_{7}>B_{8}$. This ranking indicates that, in the context of addressing cabin unlawful interference incidents, the influence of participating groups is ranked as follows: crew $>$ airport $>$ AOC. This suggests that enhancing crew training by airlines can significantly reduce the probability of structural damage to the cabin. Each entity-airline, airport, and AOC—plays a crucial role in managing cabin unlawful interference incidents. Specifically, airlines should focus on strengthening crew training and management, while airports need to implement robust security management systems and rapid response mechanisms. Additionally, AOCs should improve their capability to interact with information from all relevant parties and ensure equipment stability. These measures enhance the dynamics of emergency disposal and help mitigate structural damage to the cabin.
![img-4.jpeg](img-4.jpeg)

Figure 4. Posterior probability order when $\mathrm{A}_{2}$ is true.

### Sensitivity analysis

DBN sensitivity analysis is a process that quantifies the changeable rate of leaf node fault state and identifies the critical factors of the model. In the GeNIe software, the leaf node T is set to the “Set Target” state, with an uncertainty of 10%. Then, sensitivity analysis is performed to obtain the sensitive nodes in the DBN model, as shown in Fig. 5. The color depth of the nodes is proportional to the sensitivity.

In Fig. 5, the node sensitivities are categorized into six classes based on color depth: high sensitivity, moderate sensitivity, medium sensitivity, slight low sensitivity, low sensitivity, and insensitivity. Among them, the high sensitivity node is node A_{2}. The moderate sensitivity node is node A_{7}. The medium sensitivity nodes are node A_{1} and node B_{6}. This indicates that these nodes are critical to process failure, and enhancing the reliability of the corresponding events is crucial for improving overall process reliability. In the context of addressing emergencies, such as structural damage to the cabin, airlines and airports should prioritize strengthening crew capabilities and optimizing emergency disposal equipment. Airlines can improve collaboration between crews and airport security through targeted training programs and process management. Additionally, regular drills and case studies conducted by airlines and airports can lead to continuous improvements in operational procedures and enhance overall emergency disposal effectiveness.

Further analysis of Fig. 5 obtains Fig. 6. Figure 6 shows the most sensitive parameters for selected state node T, as well as ranked from most sensitive to least sensitive. The bar chart shows the changeable range of the node state as the parameter changes within their range. The color of the bar graph shows the changeable direction of the target node state: red indicates negative change and green indicates positive change. Of these, the impact on “T = True” is greatest under conditions of “A_{1} = False and A_{2} = True”. This suggests that cabin unlawful interference incidents are most likely triggered by structural damage to the cabin. The probability of “T = True” is lower when “A_{1} = False and A_{2} = False”. This indicates that both inadequate emergency disposal and structural damage to the cabin contribute to the likelihood of cabin unlawful interference incidents. When neither event occurs, the probability of cabin unlawful interference incidents remains low. The impact on “A_{2} = True” is greatest under conditions of “A_{6} = False and A_{7} = True”. This suggests that the probability of structural damage to the cabin can be mitigated by optimizing disposal procedures, enhancing crew training, and ensuring the suitability of emergency equipment.

![img-5.jpeg](img-5.jpeg)

Figure 5. Results of sensitivity analysis.

![img-6.jpeg](img-6.jpeg)

Figure 6. Sensitivity node ranking.

# Application for DBN of cabin unlawful interference emergency disposal Data 

In 2023, several airlines worldwide experienced a series of unlawful interference incidents, significantly threatening aviation security. On February 20, India's IndiGo Airlines received "bomb threats" on three separate flights within a single day. On March 10, passengers discovered two bullets under their seats on Korean Air flight KE621, leading to an immediate suspension of the flight. On May 21, Aeolines Argentina's flight in Buenos Aires also received a bomb warning before takeoff. On June 25, a KLM flight made an emergency landing after taking off from Amsterdam due to a terrorist threat. In June, there were two consecutive incidents of Korean civil aviation in which passengers forced open emergency doors in flight. The severity of these incidents largely depends on the emergency decision-making and response actions of the involved parties, such as the crews.

In China, such unlawful interference incidents also occur frequently. The most serious of these are destruction or intrusion of aircraft incidents. On June 29, 2012, Tianjin Airlines flight GS7554, flying from Hotan, Xinjiang Province to Urumqi, was violently hijacked by six criminals. According to the accident investigation report, the criminals used the disguised crutches as weapons and violently attempted to break down the cockpit door with the intention of entering the cockpit for hijacking. The crew and passengers managed to subdue the hijackers, and the aircraft safely returned to Hotan Airport for an emergency landing. A detailed investigation by Civil Aviation Security revealed no failures on the part of airport security screening officers and no explosives were found on the aircraft. Consequently, this incident will be used as a case study to validate the decision-making process developed in this research. According to the DFT nodes of cabin unlawful interference incidents, the probability of having occurred event nodes $B_{2}$ and $B_{11}$ is 1 . The remaining basic event probabilities were calculated according to Table 3. The results are shown in Table 4.

Therefore, the posterior probability of destruction or intrusion of aircraft incidents is shown in Fig. 7.
From Fig. 7, the posteriori probability order of the root nodes is: $B_{10}>B_{1}>B_{6}>B_{15}>B_{7}>B_{8}$. This order matches the posterior probability ranking presented in Section "Probability analysis", indicating that these events are more likely to occur during unlawful interference incidents. Therefore, they should be prioritized in emergency disposal efforts.

## Influence Strength

To compare the direct dependencies between variables at a specific moment with the interactions between variables over time, both BN and DBN are constructed to analyze the influence strength between nodes. The influence strength in the BN and DBN is shown in Fig. 8.

According to Fig. 8, it can be clearly observed that the node $\mathrm{A}_{3}$, with the influence strength of 0.965 , plays the most important role in destruction or intrusion of aircraft incidents. Among the three key nodes related to the node $\mathrm{A}_{1}$, the node $\mathrm{A}_{4}$ had the most significant impact on the incident, with an influence strength of 0.436 . Further analysis reveals that the node exerting the greatest impact on the node $\mathrm{A}_{4}$ is the node $\mathrm{B}_{3}$. This indicates that timely information sharing and coordination by the airline are crucial during emergency disposal, as failure to do so can directly affect the incident's outcome. In addition, two critical nodes that cause the node $\mathrm{A}_{2}$ need to be focused on. Both of these nodes have a significant impact on the event. The node $\mathrm{A}_{7}$ has a $62 \%$ higher impact on aircraft incidents than the node $\mathrm{A}_{6}$. This underscores the importance of designing rational and efficient emergency disposal procedures, which are crucial for preventing structural damage to the cabin and minimizing potential losses.

Comparing the influence strength in the BN and DBN reveals that both Bayesian networks identify similar nodes with high influence. This suggests that these nodes are consistently significant in affecting the outcomes of destruction or intrusion incidents in both types of networks. Both BN and DBN are able to capture the criticality of these nodes accurately. However, the node influence strength in the DBN is generally lower than that in the BN, with the influence strength of node $\mathrm{A}_{2}$ in the DBN being $75 \%$ lower than in the BN. It means that the interaction degree between nodes is relatively weak in the DBN. This disparity reflects the reality that complex


Table 4. Basic event probabilities.

![img-7.jpeg](img-7.jpeg)

**Figure 7.** Posterior probability of destruction or intrusion of aircraft incidents.

![img-8.jpeg](img-8.jpeg)

**Figure 8.** The influence strength in the BN and DBN.

Correlations may not be fully captured by static data alone, and it is essential to account for dynamic changes over time and the interactions between nodes. To ensure the safety of aircraft and the well-being of passengers, airlines and relevant departments must prioritize controlling key nodes related to structural damage to the cabin and improper emergency disposal. Specifically, there should be a focus on enhancing the monitoring and management of AOC information interactions, particularly in addressing airline violations, to ensure timely and accurate information sharing. Additionally, airlines must continuously optimize their emergency disposal processes to handle potential emergencies effectively. Participating groups should also ensure that emergency disposal equipment is suitable and well-maintained to minimize the impact on aviation security and reduce damage from aircraft incidents.

### Importance analysis

In order to measure the importance of the emergency disposal process for destruction or intrusion of aircraft incidents within the dynamic time of the event, the importance of the root node can be calculated according to the importance formula in section "Importance analysis". Based on Eqs. (1) and (2), the root node importance is shown in Fig. 9.

![img-9.jpeg](img-9.jpeg)

**Figure 9.** Importance of root nodes.

Based on the data in Fig. 9, it can be observed that the root nodes B<sub>6</sub> and B<sub>7</sub> have greater probability importance in the DBN, with values of 0.555 and 0.546, respectively. This indicates that changes in these nodes significantly affect the overall failure probability of the system. In disposing aircraft destruction or intrusion incidents, the actions taken by airport police have a direct impact on the incident's outcome. This underscores the crucial role of airport police in the incident management process.

In addition, the critical importance of the root node B<sub>10</sub> is 0.397, which is the highest in the DBN. It indicates that the node has a high importance in disposing destruction or intrusion of aircraft incidents. Airlines should focus on this critical node to enhance their response efficiency. By addressing this key node more quickly and effectively, airlines can make faster decisions and implement emergency measures, thereby minimizing the damage and impact of such incidents.

## Conclusion and discussion

### Conclusion

Through analyzing the emergency disposal process in detail, the DFT for the emergency disposal of unlawful interference incidents in the cabin is constructed. The DFT identifies the critical nodes and interrelationships, leading to the development of a DBN. Based on DBN, probability analysis, sensitivity analysis, and importance analysis were conducted to evaluate the effectiveness of the emergency disposal process for cabin unlawful interference incidents and to address two key issues. Several results are summarized as follows:

In the probability analysis, the posterior probability of node B<sub>10</sub> is 0.733, which has the highest posterior probability. This indicated that the problem of inadequate training invested by airlines can easily exist in unlawful interference incidents, followed by B<sub>1</sub> and B<sub>6</sub>. Most of these nodes were related to crews. The sensitivity analysis demonstrated that the higher sensitivity nodes of cabin unlawful interference incidents were A<sub>2</sub>, followed by A<sub>7</sub> and A<sub>1</sub>.

From the importance analysis, it indicated that the root nodes B<sub>6</sub> and B<sub>7</sub> have greater probability importance in the DBN, 0.555, and 0.546, respectively. The critical importance of the root node B<sub>10</sub> is 0.397, which is the largest in the DBN. Combining probability, sensitivity, and importance analysis, we concluded that the occurrence of "structural damage to the cabin" (A<sub>2</sub>), "inadequate training invested by airlines" (B<sub>10</sub>), and "untimely airport police takeover of disruptive passengers" (B<sub>6</sub>) were more likely to cause unlawful interference incidents.

Comparison of BN and DBN shows that the node A<sub>2</sub> both had the highest influence strength, 0.965, and 0.241, respectively. However, the node influence strength in the DBN is generally lower than that in the BN, with the influence strength of node A<sub>2</sub> in the DBN being 75% lower than in the BN. It means that the interaction degree between nodes is relatively weak in the DBN. This disparity reflects the reality that complex correlations may not be fully captured by static data alone, and it is essential to account for dynamic changes over time and the interactions between nodes.

### Discussion

Based on the above conclusions, the improvement suggestions in dynamic decision-making for emergency disposal are put forward for different participating groups.

Current research predominantly focuses on the post-event phase, and while this paper utilizes DFT to examine incident occurrence mechanisms, it does not address real-time dynamic decision-making. To enhance flight security and optimize resource allocation, airlines should develop efficient real-time dynamic decision-making systems. These systems could leverage artificial intelligence or machine learning to create decision support frameworks. Establishing a real-time data integration platform that consolidates multiple data sources—such as flight information, weather data, passenger details, and equipment status—would assist crews in making informed decisions and adjusting dynamically based on the current situation. Additionally, it is crucial to enhance crew training in safety awareness, emergency disposal, and the management of unlawful interference incidents to

ensure their preparedness for various emergencies. Airlines should also regularly review and update their operation manuals to maintain their effectiveness, comprehensiveness, and alignment with international standards. Furthermore, AOCs should focus on improving the timeliness and accuracy of information exchange with airports to facilitate coordinated emergency disposal and minimize errors.

Access to real-time data necessitates effective real-time monitoring. Airports should leverage the Internet of Things (IoT) to establish a rapid response mechanism, enabling swift reactions and deployments upon receiving incident information. This approach minimizes response time and helps prevent the escalation of incidents. Airport police should develop a comprehensive security management system with clearly defined responsibilities and authority to ensure that disruptive passengers are promptly managed and addressed, thereby preventing incidents from escalating further. Additionally, airport police should enhance punitive measures and implement a rigorous penalty mechanism for disruptive passengers to increase deterrence and prevent similar incidents from recurring. Finally, airports can create a cloud-based collaboration platform to facilitate information sharing among airlines, airports, and air traffic control. This will enhance their intelligence gathering and decisionmaking capabilities, ensuring accurate judgments and effective responses during emergencies.

In response to the regulatory authority side, the main influencing factor for airline security to take action against disruptive passengers is the probability of the regulatory authority choosing support. The regulatory authority could take measures to support airlines in training their flight crews, strengthen publicity and education for passengers, strictly manage blacklisted passengers, and formulate relevant laws to improve the law enforcement deterrence of airline security. The regulatory authority could strengthen airport security checks and passenger identity verification, in order to help airport police to stop unlawful interference before boarding. In addition, on the one hand, the regulatory authority could impose severe legal sanctions and increase the deterrent effect on disruptive passengers, which could reduce the number of disruptive passengers and enhance the security capacity of China's civil aviation. On the other hand, passengers should be publicized and educated to cultivate safety awareness. Regulatory authority could advocate for passengers to report disruptive passengers and encourage the public to participate in monitoring.

## Data availability

The datasets generated and/or analyzed during the current study are not publicly available and are available from the corresponding author on reasonable request.

Received: 2 March 2024; Accepted: 9 August 2024
Published online: 16 August 2024

# Author contributions 

Y. W.: Conceptualization, Methodology, Validation, Formal analysis, Investigation, Resources, Data curation, Writing-original draft preparation, Writing-review \& editing, Visualization, supervision, Project administration, Funding acquisition. S. H.: Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Data curation, Writing-original draft preparation, Writing-review \& editing. J. S.: Investigation, Resources, Visualization, Supervision, Project administration, Funding acquisition.

## Funding

This research is partially sponsored by the Tianjin Special Fund for Technological Innovation Guidance (23YDTPJC00010) and the National Key R\&D Program Subject (2022YFB4301002).

## Competing interests

The authors declare no competing interests.

# Additional information 

Correspondence and requests for materials should be addressed to Y.W.
Reprints and permissions information is available at www.nature.com/reprints.
Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/ licenses/by-nc-nd/4.0/.
(c) The Author(s) 2024