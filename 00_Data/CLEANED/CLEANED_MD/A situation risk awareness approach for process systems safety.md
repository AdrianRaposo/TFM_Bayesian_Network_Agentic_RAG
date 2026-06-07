# A Situation Risk Awareness Approach for Process Systems Safety 

Mohsen Naderpour, Jie Lu, Guangquan Zhang<br>Decision Systems and e-Service Intelligence Laboratory<br>Centre for Quantum Computation \& Intelligent Systems, School of Software<br>Faculty of Engineering and IT, University of Technology, Sydney<br>PO Box 123, Broadway NSW 2007 Australia<br>Mohsen.Naderpour@student.uts.edu.au, Jie.Lu@uts.edu.au, Guangquan.Zhang@uts.edu.au


#### Abstract

: Promoting situation awareness is an important design objective for a wide variety of domains, especially for process systems where the information flow is quite high and poor decisions may lead to serious consequences. In today's process systems, operators are often moved to a control room far away from the physical environment, and increasing amounts of information are passed to them via automated systems, they therefore need a greater level of support to control and maintain the facilities in safe conditions. This paper proposes a situation risk awareness approach for process systems safety where the effect of ever-increasing situational complexity on human decision-makers is a concern. To develop the approach, two important aspects - addressing hazards that arise from hardware failure and reducing human error through decision-making - have been considered. The proposed situation risk awareness approach includes two major elements: an evidence preparation component and a situation assessment component. The evidence preparation component provides the soft evidence, using a fuzzy partitioning method, that is used in the subsequent situation assessment component. The situation assessment component includes a situational network based on dynamic Bayesian networks to model the abnormal situations, and a fuzzy risk estimation method to generate the assessment result. A case from U.S. Chemical Safety Board investigation reports has been used to illustrate the application of the proposed approach.


Keywords: Situation awareness, Situation assessment, Process systems safety, Bayesian networks, Risk assessment.

## 1. Introduction

Since the beginning of the industrial revolution, many serious accidents at large-scale technological systems that have had grave consequences, such as those at Three Mile Island, Bhopal and Chernobyl, have primarily been attributed to human error. In the vast majority of these accidents, the human operator was struggling against significant challenges such as data overload and the task of working with a complex system. In fact, operators are not the cause of these accidents, but they have inherited the problems and difficulties of technologies created by engineers. Operators generally have no difficulty in physically performing their tasks, and no difficulty in knowing the correct action to do, but they are stressed by the task of understanding what is going on in the situation (Endsley, 2006). Over the last two decades, a great deal of research has been undertaken in the area of Situation Awareness (SA).

Situation awareness, a state of mind in humans, is essential for conducting decision-making activities. It concerns the perception of elements in the environment, the comprehension of their meaning, and the projection of their status in the near future (Endsley, 1995b). The primary research in this field was undertaken in the aviation industry, where pilots and air traffic controllers are under considerable pressure to develop better SA. One review of over 200 aircraft accidents found that poor SA was the main causal factor (Endsley, 1997). A review in other domains, such as nuclear power plant, showed that this is not a problem limited to aviation, but one faced by many complex systems (Endsley, 2006). Successful system designs must deal with the challenge of combining and presenting the vast amounts of data now available from many technological systems to provide true SA, whether it is for a pilot, a physician, a business manager, or an automobile driver.

In the process industry, the last two decades have been marked by a significant increase in automation, advanced control, on-line optimization and technologies that have significantly increased the complexity and sensitivity of the role of operators and their teams. Nowadays, process operators have to rely on human computer interaction (HCI) principles to observe and comprehend the overwhelming amount of rapidly changing process data. They are often moved to a control room far away from the physical process, where automated systems pass more and more information to them, so they have to handle more data and more responsibility. In the presence of all this data, operators are finding that they have even less awareness than before about the situations they are controlling. This has led to a huge gap between the massive amount of data produced and disseminated and the operator's ability to effectively assimilate the required data and to make timely, accurate decisions (Endsley and Garland, 2000). This emphasizes the importance of SA in process systems, but paradoxically the literature review shows that the majority of process safety studies have focused on the technical issues and have often neglected SA. This may be due to the increased complexity introduced when dealing with the human factors of a system, while hardware reliability techniques are relatively mature and well understood (Sandom, 2001).

Situation awareness is quite likely to be at the root of many accidents in process control, where multiple goals are pursued simultaneously, multiple tasks need the operator's attention, operator performance is under high time stress, and negative consequences associated with poor performance are expected. Kaber and Endsley (1998) believe that many of the performance and safety problems that currently occur in the process control arena are the result of difficulties with the operator's SA, such as:

- Failure to detect critical cues regarding the state of a process control system.
- Failure to properly interpret the meaning of information perceived through process control interfaces.
- A lack of understanding of individual task responsibilities and the responsibilities of other control operators.
- A lack of communication between operators functioning in teams.

Sneddon et al. (2013) analyzed offshore drilling accidents and their results show that more than $40 \%$ of such accidents are related to SA, and that the majority of those SA errors ( $67 \%$ ) occurred at the perceptual level, $20 \%$ concerned comprehension, and $13 \%$ arose during projection. In the case of the Texas City, TX BP Amoco Refinery explosion on 23 March 2005, 15 workers were killed and 170 injured when a column was overfilled, overheated, and over-pressurized on startup. The key problem identified in this catastrophic event was the difficulty experienced by the operator in maintaining an accurate awareness of the situation while monitoring a complex, fast moving environment (Pridmore, 2007). As can be seen, loss of SA, poor SA and lack of SA as identified causal factors are now popular terms in accident investigation reports (Salmon and Stanton, 2013). However, some researchers such as Dekker (2013), question whether the loss of SA, a psychological construct, can result in human operators being liable for mishaps and argue that SA itself is not the cause of accidents.

In a process system, operators' tasks include information gathering, planning, and decision making. In addition, according to ALARP, operators should demonstrate that the risks associated with the functioning of a facility are sufficiently low (Melchers, 2001), and that they monitor the system continually to ensure that it is stable and functioning normally. During abnormal situations, a well-trained operator should comprehend a malfunction in real time by analyzing alarms, assessing values, or recognizing unusual trends on multiple instruments. Usually, many alarms from different systems are triggered at the same time during an abnormal situation, making it difficult for the operator to make a decision within a very short period of time. If several abnormal situations occur at the same time, decisions need to be made particularly quickly. Operators are frequently unable to judge which situation should be given priority in a short timeframe, when confronted with complex abnormal situations, yet operators must respond and make decisions quickly to recover their units to normal conditions. Under these circumstances, the mental workload of operators rises sharply and too high mental workload possibly increases their error rate (Hsieh et al., 2012; Jou et al., 2011). Therefore, a system is needed to

support operators' SA in understanding and assessing the situation and to assist them to take appropriate actions.

This paper introduces a new situation risk awareness approach for process systems safety where the degree of automation and complexity is increasing and the number of operators is decreasing, and each operator must be able to comprehend and respond to an ever increasing amount of risky status and alert information in abnormal situations. Efforts have been made to develop new SA approaches for military purposes and maritime security (Baader et al., 2009; Farahbod et al., 2011), and other studies have used machine learning, expert systems and ontology (Brannon et al., 2009; Naderpour and Lu, 2012a, b; Nguyen et al., 2009). However, none of these is appropriate for supporting operators' SA in abnormal situations. The situation risk awareness approach includes an evidence preparation component in which, based on the online conditions and process monitoring system, the current state of the observable variables is prepared as soft evidence to use in the next component. The approach also contains a situation assessment component that uses risk indicators to determine abnormal situations, minimize the number of alarms, and determine the investigation priority of abnormal situations. In addition, simple and dynamic Bayesian networks are used to develop the model base of the approach.

The paper is organized as follows. Section 2 presents the background and related works. Section 3 describes the situation risk awareness approach. Section 4 introduces the SA measurement and dealing with uncertainty. A case from the U.S. Chemical Safety Board investigation reports (www.csb.gov) is presented in Section 5 to illustrate the feasibility and benefits of the proposed approach. Finally, the conclusion and future work are provided in Section 6.

# 2. Background and Related Works 

This section describes the background to SA, dynamic Bayesian networks and fuzzy sets, and outlines related works.

### 2.1. Situation Awareness

A situation is a collection of objects which have relationships with one another and the environment, and an object is a physical entity: something that is within the grasp of the senses. Additionally, SA can be described as "the perception of the elements in the environment within a volume of time and space, the comprehension of their meaning and the projection of their status in the near future" (Endsley, 1995b). This SA model follows a chain of information processing from perception, through interpretation, to projection. From the lowest to the highest, the levels of SA are as follows (Endsley, 2006; Stanton et al., 2001):

- Perception: Perception involves the sensory detection of significant environmental cues. For example, operators need to be able to see relevant displays or hear an alarm.
- Comprehension: Comprehension is the understanding of the meaning or significance of that information in relation to goals. This process includes developing a comprehensive picture of the world.
- Projection: Projection consists of extrapolating information forward in time to determine how it will affect future states of the operating environment. Higher levels of SA allow operators to function in a timely and effective manner, even with very complex and challenging tasks.
Figure 1 paves the way to a better understanding of the definition of both 'situation' and 'SA'. It shows four planes, each of which refers to a different level of abstraction. The bottom layer shows the World, which includes physical or conceptual things, or both. To the right of the World plane, a human head depicts the fact that SA is a state of knowledge which takes place in the human brain. The human is unable to observe all aspects of the World, and therefore has to obtain inputs from the computer for better appreciation (i.e. the arrow between the computer and human head). The dots on the next layer (i.e. Perception) represent the objects from the World that are observed through sensors and represented in computer memory. The arrow pointing from the World plane to the radar icon represents the sensory

process, which then feeds the computer. The emphasis in situation definition is on relationships. The relationships are viewed from the point of view of a thing (i.e. focal object), and how other things in the surroundings are related to it. This plane represents Comprehension. The top layer shows the Projection. This layer is defined as the capability of anticipating future events and their implications (Kokar et al., 2009).

The three-level model of SA has been used in a number of studies as the justification for structuring a computer-supported SA process in a variety of complex systems, such as air traffic control, nuclear power plant, military service, electronic warfare, automobile driving, and business decision support systems (Endsley, 2006; Niu et al., 2009; Niu et al., 2013).
![img-0.jpeg](img-0.jpeg)

Figure 1: The situation and SA (Kokar et al., 2009).

# 2.1.1. Situation Assessment 

As noted, SA is a state of knowledge that has to be distinguished from the process underlying the achievement of SA, which is properly termed 'situation assessment' (Endsley, 1995b). Situation assessment models describe basic principles and general features about how people process information or interact with the environment to attain SA. In fact, awareness information for a situation is derived as a result of situation assessment. Since SA is regarded as a dynamic and collaborative process, assessing a situation often requires data integration or so-called data fusion with the support of computer-based intelligent techniques (Lu et al., 2008a). The enhancement of operators' SA in complex systems is a major design goal in developing operator interfaces, automation concepts and training plans in a wide variety of fields.

Because SA aims to predict the status of a situation in the near future, which is the third level of the SA model, proper and effective situation assessment approaches and tools to conduct the prediction are required. Many studies have reported that machine learning techniques could be an effective method for intelligent prediction by extracting rules from previous data to generate new assessment results (Lu et al., 2008a), but their use has been limited, possibly because of the lack of rich training data for SA (Brannon et al., 2009). Kim and Seong (2006a) developed a quantitative model based on Bayesian inference and information theory, and described the process of knowledge-driven monitoring and the revision of operators' understanding of their environments. In command and control applications, Bayesian networks have been widely considered in situation assessment configuration (Chai and Wang, 2011; Das et al., 2002; Shi and Liu, 2009). Kim and Seong (2006b) considered a computational method, but computational approaches often do not satisfactorily handle all forms of uncertainty; therefore, a number of cognitive approaches which use a fuzzy logic system to address the limitations of traditional models in producing the full range of human behaviors, have been developed (Chandana and Leung, 2008; Jones et al., 2009).

# 2.1.2 Situation Awareness Requirements 

A methodology called Goal-Directed Task Analysis (GDTA) is used to determine the aspects of a situation that are important for a particular user's SA requirements. This methodology is a specific form of cognitive task analysis that focuses on identifying goals and critical information needs in a task context. The GDTA process forms an exemplary template for incorporating human cognition into an actionable model by describing in detail not only a user's information data needs (Level 1), but also how that information should be combined to form the comprehension (Level 2) and projection of future events (Level 3) that are critical to SA, thereby providing a critical link between the data input and the decisions to be made in a goal-directed environment (Jones et al., 2011). In this analysis, the major goals of a particular job class are identified, along with the major sub-goals necessary for meeting each goal. The major decisions that need to be made in association with each sub-goal are then identified. The SA requirements for making these decisions and carrying out each sub-goal is identified (Figure 2). These requirements focus not only on what data the operator needs, but also on how that information is integrated, or combined, to address each decision. This type of analysis is based on goals or objectives, not tasks. This is because goals form the basis for decision-making in many complex environments. Conducting such an analysis is usually carried out using a combination of cognitive engineering procedures such as expert elicitation, observation of operator performance and analysis of documentation (Endsley, 2006).
![img-1.jpeg](img-1.jpeg)

Figure 2: Goal-directed task analysis for determining SA requirements (Endsley, 2006).

### 2.2. Dynamic Bayesian Networks

A Bayesian network (BN) as a probability-based knowledge representation method is appropriate for modeling a causal process with uncertainty. A BN is a directed acyclic graph whose nodes correspond to random variables and the arcs between nodes represent dependencies or direct causal influences between variables. The force of these dependencies is represented by conditional probabilities. Conventional BN can be considered as a representation of static cause-effect relations among objects in a situation.

Based on the conditional independence resulting from the $d$-separation concept, and the chain rule, BN represents the joint probability distribution $P(X)$ of variables $X=\left\{X_{1}, X_{2}, \ldots, X_{n}\right\}$, included in the network as:

$$
P(X)=\prod_{i=1}^{n} P\left(X_{i} \mid P a\left(X_{i}\right)\right)
$$

where $P a\left(X_{i}\right)$ is the parent set of $X_{i}$ for any $i=1, \ldots, n$. If $P a\left(X_{i}\right)$ is an empty set, then $X_{i}$ is a root node and $P\left(X_{i} \mid P a\left(X_{i}\right)\right)=P\left(X_{i}\right)$ denotes its prior probability. BN takes advantage of Bayes theorem to update the prior occurrence probability of objects given new information, called evidence $E$, thus yielding the posteriors. This new information usually becomes available during the operational life of a system, including the occurrence or nonoccurrence of objects (Khakzad et al., 2012):

$$
P(X \mid E)=\frac{P(X, E)}{P(E)}=\frac{P(X, E)}{\sum_{X} P(X, E)}
$$

This equation can be used for either probability prediction or probability updating. In predictive analysis, conditional probabilities of the form $P$ (hazard|object) are calculated, indicating the occurrence probability of a particular hazard given the occurrence or non-occurrence of a certain primary object. On the other hand, in updating analysis, those of the form $P$ (object|hazard) are evaluated, showing the occurrence probability of a particular object given the occurrence of a certain hazard.

The static BN can be extended to a dynamic BN (DBN) model by introducing relevant temporal dependencies that capture the dynamic behaviors of the domain variables between representations of the static network at different times. Two types of dependencies can be distinguished in a DBN: contemporaneous and non-contemporaneous. Contemporaneous dependencies refer to arcs among nodes that represent variables within the same time period. Non-contemporaneous dependencies refer to arcs between nodes which represent variables at different times. A DBN is defined as a pair $\left(B_{1}, 2 T B N\right)$ where $B_{l}$ is a BN which defines the prior distribution $P\left(X_{1}\right)$ and $2 T B N$ is a two-slice temporal BN with

$$
P\left(X_{t} \mid X_{t-1}\right)=\prod_{i=1}^{n} P\left(X_{t}^{i} \mid P a\left(X_{t}^{i}\right)\right)
$$

where $X_{t}^{i}$ is a node at time slice $t$ and $P a\left(X_{t}^{i}\right)$ is the set of parent nodes which can be in time slice $t$ or in time slice $t-1$. The nodes in the first slice of a $2 T B N$ do not have any parameters associated with them, but each node in the second slice has an associated conditional probability distribution (CPD) for continuous variables or conditional probability table (CPT) for discrete variables, which defines $P\left(X_{t}^{i} \mid P a\left(X_{t}^{i}\right)\right)$ for all $t>1$. The arcs between slices are from left to right, reflecting the causal flow of time. If there is an arc from $X_{t-1}^{i}$ to $X_{t}^{i}$, this node is called persistent. The arcs within a slice are arbitrary. Directed arcs within a slice represent "instantaneous" causation. The semantics of a DBN can be defined by "unrolling" the $2 T B N$ until there are $T$ time-slices. The resulting joint distribution is then given by:

$$
P\left(X_{1: T}\right)=\prod_{t=1}^{T} \prod_{i=1}^{n} P\left(X_{t}^{i} \mid P a\left(X_{t}^{i}\right)\right)
$$

Several inference methods for a DBN can be used, such as clustering, forward-backward algorithm, unrolled junction tree, and the frontier algorithm (Murphy, 2002).

# 2.3. Fuzzy Sets 

Fuzzy logic, unlike Boolean or crisp logic, deals with problems that have vagueness, uncertainty, or imprecision, and uses membership functions with values varying between 0 and 1. Fuzzy logic tends to mimic human thinking, which is often fuzzy in nature. In conventional set theory based on Boolean logic, a particular object or variable is either a member (logic 1) of a given set or it is not (logic 0). On the other hand, in fuzzy set theory based on fuzzy logic, a particular object has a degree of membership in a given set that may be anywhere in the range of 0 (completely not in the set) to 1 (completely in the set). This property allows fuzzy logic to deal with uncertain situations in a fairly natural way. It may be mentioned that although fuzzy logic deals with imprecise information, it is based on sound quantitative mathematical theory (Bose, 1994). Fuzzy theory was first proposed by Zadeh in 1965. The formal definition of fuzzy sets is that "A fuzzy set is characterized by a membership function mapping the elements of a domain, space or universe to the unit interval $(0,1)$ " (Zadeh, 1965).

Definition 1 (Fuzzy set): Fuzzy set $A$ is defined in terms of a universal set $X$ by a membership function assigning to each element $x \in X$ a value $\mu_{A}(x)$ in the interval $[0,1]$ i.e. $A: X \rightarrow[0,1]$.

Definition 2 (Fuzzy number): A fuzzy set $A$ in $\mathbb{R}$ is called a fuzzy number if it satisfies the following conditions:
(a) $A$ is normal,
(b) $A_{\alpha}$ is a closed interval for every $\alpha \in(0,1]$,
(c) the support of $A$ is bounded.

The general characteristic of a fuzzy number is represented in Figure 3. In the figure, $\mu_{A}(x)$ denotes the membership function of $x$ in the fuzzy set $A$. This shape of the fuzzy number is referred to as a "triangular" fuzzy number and denoted by the triple $\left(a_{1}, a_{2}, a_{3}\right)$. In general, a fuzzy set is a fuzzy number if its height is one (in which case it is said to be normal), it is a convex subset of the real line, and it has only one core (Shapiro, 2009).

Definition 3 ( $\alpha$-cut): Let $A$ be a fuzzy set in the universe $X$. The (crisp) set of elements that belong to the fuzzy set $A$ at least to the degree is called the $\alpha$-cut or $\alpha$-level set and defined by:

$$
A_{\alpha}=\left\{x \in X \mid \mu_{A}(x) \geq \alpha\right\}
$$

An example of an $\alpha$-cut is depicted in Figure 3. As indicated in the figure, the essence of the $\alpha$-cut is that it limits the domain under consideration to the set of elements with degree of membership of at least alpha, that is, the $\alpha$-level set. Thus, while the support of fuzzy set $A$ [all $x$ such that $\mu_{A}(x) \geq 0$ ] is its entire base, its $\alpha$-cut is from $X_{\text {left }}^{\alpha}$ to $X_{\text {right }}^{\alpha}$. Values outside that interval will be considered to have a level of membership that is too insignificant to be relevant and should be excluded from consideration (Shapiro, 2009).
![img-2.jpeg](img-2.jpeg)

Figure 3: A fuzzy number (Shapiro, 2009).

# 3. A Situation Risk Awareness Approach 

Nowadays, maintaining complex and dynamic systems like process systems in safe conditions, i.e., keeping the risks below the acceptance criteria, is a critical challenge because situations change dynamically and every decision has a significant social, economic and environmental impact on society. The key focus must be on keeping the human operator aware of the situation, showing the risk level of hazardous situations and providing the base to reduce risks until they reach a level that is As Low as Reasonably Practicable (ALARP). According to ALARP, it is necessary for operators and intending operators of a potentially hazardous facility to demonstrate that (a) the facility is fit for its intended purpose, (b) the risks associated with its functioning are sufficiently low, and (c) sufficient safety and emergency measures have been instituted (or are proposed) (Melchers, 2001).

Previous researches in the field of process safety have only considered developing scenarios for specific undesirable events from an engineering perspective, whereas in today's process systems, operators face several hazards from different subsystems which dynamically threaten the system, and they

have to comprehend both the current state and the near future state to make correct decisions. A humancentric system is therefore needed to support operators in understanding and assessing the current state of a situation and to assist them to take appropriate actions in abnormal situations. To this end, a new situation risk awareness approach is introduced in this section which provides the basis for developing a SA support system in the future.

To determine the aspects of the situation that are important for an operator's SA, the GDTA methodology is used. The elements of GDTA include goal, subgoals, and decisions, and the SA requirements are determined as shown in Table 1. As mentioned previously, the emphasis on situation definition is on relationships. Any variety of relations - physical, organizational, informational, and perceptual - can be considered as being appropriate to the given information system's mission. As the main goal of the approach is to eliminate or reduce the risk of hazardous situations to an acceptable level, the kinds of relationships that might create hazardous situations are particularly important. A hazardous situation is defined as a circumstance immediately before harm is produced by the hazard. The main goal is followed by two subgoals: risk determination and risk reduction. Associated with each subgoal, the major decisions that need to be made are then identified. The SA requirements to make these decisions and carry out each sub-goal are determined.

Based on SA requirements, the situation risk awareness approach is developed as shown in Figure 4. As can be seen, the proposed approach includes two major components, an evidence preparation component and a situation assessment component. In the following sections, the two components will be explained in detail, and the means of addressing the identified decisions to achieve the subgoals and consequently the main goal based on determined requirements will be clarified.

Table 1: Safety goals, decisions and SA requirements.
Goal: Eliminate or reduce the risks to a level that is as low as reasonably practicable
Subgoal 1: Determine the risks
Decision 1-1: Hazardous situation identification

- L1: Objects and relationships which contribute to create a hazardous situation
- L1: Situations and relationships which contribute to create a hazardous situation
- L2: Hazardous situations that threaten the system

Decision 1-2: Likelihood determination

- L1: Objects which are relevant to contributors to the hazardous situation
- L1: Observable variables which are relevant to the hazardous situation
- L2: Prior likelihood of the hazardous situation
- L3: Posterior likelihood of the hazardous situation

Decision 1-3: Severity determination

- L2: Possible consequences of the hazardous situation
- L3: Degree of loss

Decision 1-4: Risk level estimation

- L2: Likelihood of the hazardous situation (Decision 1-2)
- L2: Severity of the hazardous situation (Decision 1-3)
- L3: Current level of risk

Subgoal 2: Reduce the risks
Decision 2-1: Choosing practical options

- L2: Available reduction and containment options

Decision 2-2: Options impact prediction

- L3: Projecting the new likelihood of the hazardous situation
- L3: Projecting the new severity of the hazardous situation
- L3: New level of risk

Note: L3= Level 3 SA (projection); L2= Level 2 SA (comprehension); L1= Level 1 SA (perception).

![img-3.jpeg](img-3.jpeg)

Figure 4: The situation risk awareness approach.

# 3.1. The Evidence Preparation Component 

The evidence preparation component provides the current state of the observable variables based on the online condition and process monitoring system, stores them in the database, conducts a discretization process and transfers the result to the next component. The observable variables will be used as soft evidence in the next situation assessment component. According to the conditions and process monitoring, each observable variable value is obtained from field sensors based on SCADA ${ }^{1}$ systems. As the observable variables extracted from sensors are continuous, a discretization process is required to use them in DBNs. In general, mapping a continuous variable to a discrete variable can be done with a crisp set or a fuzzy set.

Consider variables such as temperature, age or speed, which are inherently continuous but represented as discrete when included in discrete BNs. For such variables, an implicit mapping is involved whenever an observation (i.e., evidence) about them needs to be introduced to the model. Consider temperature defined on the frame $[0,40]^{\circ} \mathrm{C}$; it can be discrete to a scheme of three states: cold, warm, and hot corresponding to the intervals $[0,10)^{\circ} \mathrm{C},[10,25)^{\circ} \mathrm{C},[25,40]^{\circ} \mathrm{C}$, respectively. A reading of $24.9^{\circ} \mathrm{C}$ from the thermometer would fall under the discrete state 'warm', whereas, $25^{\circ} \mathrm{C}$ would be labeled as 'hot'. As can be seen, there is no meaningful way to determine a crisp boundary between these states, hence using classical sets with crisp boundaries to discretize a continuous variable may generate unpredictable results for BNs (Oztekin and Luxhoj, 2011). Therefore, the concept of fuzzy set theory can provide a smoother structured way to improve on classical discretization techniques. Figure 5 shows a fuzzy partition, however non-symmetric fuzzy sets or sets with a different shape can be used. If $x$ is a value of a variable $X$ happening on the domain partitioned as in Figure 5, then point semantic unification is applied to evaluate the probabilities $P\left(q_{1} \mid x\right), \ldots, P\left(q_{3} \mid x\right)$ that are the distribution corresponding to the value $x$ on sets $q_{1}, \ldots, q_{3}$.
![img-4.jpeg](img-4.jpeg)

Figure 5: A fuzzy partition.

[^0]
[^0]:    ${ }^{1}$ Supervisory Control and Data Acquisition

Definition 4 (Fuzzy partition): A fuzzy partition on the universe $\Omega$ is a set of fuzzy sets $\left\{q_{1}, q_{2}, \ldots, q_{m}\right\}$ such that:

$$
\forall x \in \Omega, \sum_{i=1}^{m} \mu_{q_{i}}(x)=1
$$

where $\mu_{q_{i}}(x)$ is the membership function of $q_{i}$ i.e. $\mu_{q_{i}}: \Omega \rightarrow[0,1]$.
Definition 5 (Fuzzy state): Let $\left\{q_{1}, q_{2}, \ldots, q_{m}\right\}$ be a fuzzy partition on the universe $\Omega$, then every fuzzy set $q_{i}, i=1, \ldots, m$ is defined as a fuzzy state such that:

$$
q_{i}=\left\{\mu_{q_{i}}(x) \mid x \in \Omega\right\}
$$

For a particular BN, every node can be observed as one of its states, called hard evidence; or the evidence may be observed with uncertainty, called soft evidence. For a node without parents, soft evidence is equivalent to modifying its prior probability; otherwise, soft evidence on a variable $X_{i}$ is represented by a conditional probability vector $P\left(X_{i}=x \mid H_{i}\right)$ for $i=1,2, \ldots, n$, where $H_{i}$ denotes the hypothesis that the true state is the $i$-th state. To simplify the inference process for a continuous variable $X_{i}$, consider the fuzzy partition $\left\{q_{1}, q_{2}, \ldots, q_{m}\right\}$. Define $H_{j}(j=1,2, \ldots, m)$ as hypotheses that $X_{i}$ is in fuzzy state $q_{j}$. The results of membership functions $\mu_{q_{j}}(x) j=1,2, \ldots, m$ form the soft evidence vector:

$$
e=\left\{\mu_{q_{1}}(x), \mu_{q_{2}}(x), \ldots, \mu_{q_{m}}(x)\right\}
$$

The $\mu_{q_{j}}(x)$ is considered to be approximately equivalent to the condition probability $P\left(q_{j} \mid X_{i}=x\right)$ (Chai and Wang, 2011).

Table 2 gives an example showing the temperature limits for a chemical plant involving two reactors and two distillation columns (Naderpour and Lu, 2012a), including the limits for the six-sigma quality, high alarm and automatic shut-down.

Table 2: Temperature limits $\left({ }^{\circ} \mathrm{C}\right)$.


The temperature continuous variable of reactor 1 (R1) in terms of operation can be partitioned by fuzzy mapping into the fuzzy states including Low, Normal and High, and the membership function is defined as follows, as well as being shown in Figure 6:

$$
\begin{aligned}
\mu_{T(L)}(x)= & \begin{cases}1 & 0 \leq x \leq t_{1} \\
\left(t_{2}-x\right) /\left(t_{2}-t_{1}\right) & t_{1}<x \leq t_{2} \\
0 & x>t_{2}\end{cases} \\
\mu_{T(N)}(x)= & \begin{cases}0 & 0 \leq x<t_{1} \\
\left(x-t_{1}\right) /\left(t_{2}-t_{1}\right) & t_{1} \leq x<t_{2} \\
\left(t_{3}-x\right) /\left(t_{3}-t_{2}\right) & t_{2} \leq x<t_{3} \\
0 & x \geq t_{3}\end{cases} \\
\mu_{T(H)}(x)= & \begin{cases}0 & 0 \leq x<t_{2} \\
\left(x-t_{2}\right) /\left(t_{3}-t_{2}\right) & t_{2} \leq x<t_{3} \\
1 & x \geq t_{3}\end{cases}
\end{aligned}
$$

where $t_{l}=155^{\circ} \mathrm{C}, t_{2}=160^{\circ} \mathrm{C}$ and $t_{l}=165^{\circ} \mathrm{C}$, and $\mu_{T(L)}(x), \mu_{T(N)}(x)$ and $\mu_{T(H)}(x)$ denote the membership function of fuzzy states Low, Normal and High respectively. At time $T$, the temperature inside the R1 is reported $164^{\circ} \mathrm{C}$ therefore the soft evidence vector will be: $\mathrm{e}=\{\mathrm{Low}=0$, Normal $=0.2$, High $=0.8\}$
![img-5.jpeg](img-5.jpeg)

Figure 6: The membership function of R1 temperature.

# 3.2. The Situation Assessment Component 

The literature shows that the BN-based situation assessment methods have certain advantages. They use nodes and directed arcs to express the knowledge and new information can be propagated by directed arcs among nodes. Information reserved in networks can also be specified by experts or studied from samples. In addition, they already have encoded expert knowledge, and the time propagation algorithm embodies SA's continuity through computing the accumulation effects of situations according to both new evidence and the evidence arriving with time sequences (Su et al., 2011). Therefore, to develop the situation assessment component, DBNs are considered to model abnormal situations individually, and finally to develop one or more situational network.

### 3.2.1. Abnormal Situations

As mentioned previously, a situation is a collection of objects which have relationships to with one another and the environment, and a hazardous situation is defined as a circumstance immediately before harm is produced by the hazard. Therefore, a hazardous situation is defined as an abnormal situation if its risk is not acceptable. To find hazardous situations, an analysis is carried out using a combination of cognitive engineering procedures and hazard identification methods. Observation of operator performance, analysis of written materials and documentation, expert elicitation and formal questionnaires may be used to conduct the analysis (Endsley, 2006). Previous hazard identification documents may help with this analysis. In many areas, hazardous situations have been obtained through the design and implementation phases, and various models have been developed to identify them. For example, HAZOP is one of the most powerful methods available and has been well described in the literature, and fault tree, event tree, and bow-tie have been adopted as knowledge acquisition techniques which can be converted to appropriate BN-based situation models. The hazardous situations are categorized in two groups based on contributed objects:
(a) First level situations: a hazardous situation is first level situation if its objects and their interactions create a hazard;
(b) Higher level situations: a hazardous situation is higher level situation if its objects and their interactions with other situations create a hazard.
The result of this section forms the first step of the modeling process, which is represented in Figure 7. The proposed situations should have clear operational meaning to the modeler, the domain experts and the model users. Where possible, this process should be undertaken in a participatory environment to ensure that the breadth of issues and potential inputs to the models are identified.

![img-6.jpeg](img-6.jpeg)

Figure 7: A cycle to build the situation models using BN.

# 3.2.2. Situation Modeling 

Bayesian networks and DBNs are used to model hazardous situations based on the modeling process demonstrated in Figure7. The first level situation can be modeled by a simple BN, based on its objects, in which each node represents an object. The situation model usually begins with root nodes, which are the basic objects, followed by intermediate nodes, a pivot node and leaf nodes. The pivot node is the focal object which delegates the situation, and relations among the root nodes and the pivot node define the relationships among the objects. The leaf nodes may be safety barriers which are physical objects of the environment and will connect to one another if there is relation between their performances. Also, one of the leaf nodes may be a consequence node which has some states, and shows the possible accidents in this situation. Figure 8(a) shows situation $A$ in which the node $A$ is focal and other nodes are related to it.
![img-7.jpeg](img-7.jpeg)

Figure 8: A simple BN and a dynamic BN.

The states of the objects can conceivably describe any possible state in the real world, but they must be defined as finite in number, discrete, and mutually exclusive. Therefore, in this paper, the states of basic objects are defined as Boolean (i.e. failure and success), which refers to the objects working well (success) or not working (failure). The prior probability of basic objects (nodes without parents) can be obtained through failure probability datasets such as the Center for Chemical Process Safety (CCPS, 1989), and the Offshore Reliability Data Handbook (OREDA, 2002), and if the failure probability of the objects is not available, expert judgment can be used. The states of intermediate nodes are set in a similar way (i.e. failure and success), and their CPTs are set based on "OR gate" or "AND gate" definition, as described in (Bobbio et al., 2001) and represented in Figure 9. The focal node, which delegates the situation, has two states, i.e. safe and hazardous, and its CPT is set by using OR and AND gate definition.

![img-8.jpeg](img-8.jpeg)

Figure 9: The OR and AND gates in BN representation.
Higher level situations also can be modeled by BNs. Several situations can exist in parallel, or the existence of one situation can exclude the existence of another situation. Figure 8(b) shows an example network of situations. As can be seen, there are four situations of interest, namely A, B, C and D, where A and $B$ belong to the first level situations category. They can be inferred directly from objects $\mathrm{O}_{1}, \mathrm{O}_{2}$ and $\mathrm{O}_{3}$, while situations C and D are higher level situations and their existence is dependent on the existence of lower level situations. The temporal dependencies are illustrated by dashed lines. The focal node, which delegates the situation, has two states, i.e. safe and hazardous, and its CPT, if it cannot be set by using OR and AND gate definition, may be determined by scientific data, including the frequency of observed conditions in a monitored field or laboratory. There are various algorithms that rely on statistical dependency tests and automated optimal model searches that represent the given data set. These algorithms yield a BN from the available data set with a minimum degree of human supervision (GarciaHerrero et al., 2012). The conditional probabilities can also be determined by a combination of methods. For example, expert probabilities can be combined with observational data to describe outcomes of extreme events not represented in the dataset (Pollino et al., 2007). If no data is available, the values will need to be assigned through expert judgment, and when objective data become available, this can then update or replace any estimates that have been entered into the model using subjective means.

If the situation is inferred by one or more observable variable, the focal object is connected to the observable variables, whose states are determined as discussed in Section 3.1, and whose CPTs are determined by domain experts. The elicitation process is carried out with recursive technique (e.g. Delphi method) to guarantee the convergence of the results. The final results are commented and adjusted again during further interviews (Li et al., 2012).

There are also situations which can only be inferred by observing the real world over a period of time. Although these situations are characterized by information collected over a time-period, they only exist at a special point in time. Their existence in the next time-point has to be verified again.

# 3.2.3. Situation Evaluation 

An important aspect in building BN-based situation models is evaluation, which can be undertaken at several levels (see Figure 7). Evaluation of a BN requires the assessment of model behavior to ensure that the model demonstrates acceptable behavior. The first level is to ensure that key objects and their relationships have been represented in the model, and the second level should review the determined states to ensure that they have been defined unambiguously. There are three evaluation methods to validate the performance of a model: sensitivity analysis, data-based evaluation and non-quantitative evaluation of model outputs using experts (Pollino et al., 2007). In the event that large data sets are not available, and the probabilities must be elicited from domain experts, the sensitivity analysis technique is often used to investigate the effect of probability parameter changes on the performance of BNs.

Sensitivity analysis is a technique for the systematic investigation of the influence of variation in the model inputs on this model's outcome, where inputs can be the parameters (i.e. values of conditional probabilities) or real inputs (i.e. values of observable nodes). The technique is widely used to investigate the importance of inputs as well as the possible consequence of inaccuracies in models (Bednarski et al.,

2004). The sensitivity analysis in this paper is conducted according to the following three axioms (Jones et al., 2010):

- A slight decrease/increase in the prior probabilities of each parent node should result in the effect of a relative decrease/increase of the posterior probabilities of the child node.
- Given the variation of subjective probability distributions of each parent node, the magnitude of influence of the parent node on the child node values should remain consistent.
- The magnitude of the total influence of the combination of probability variations from $x$ attributes (evidence) on the values should be always greater than the probability variations from the set of $x-y(y \in x)$ attributes (sub-evidence).


# 3.2.4. DBN-Based Situational Network 

Suppose the configuration space $\sigma$ is defined by all possible physical and conceptual objects. Mathematically, a situation at time $t$ can be modeled as a statement about a subset $\tilde{\sigma}$ of the configuration space, which is either hazardous or safe:

$$
S_{t}= \begin{cases}\text { Hazardous } & \text { if } R\left(S_{t}\right)>\text { Risk Criteria } \\ \text { Safe } & \text { if } R\left(S_{t}\right) \leq \text { Risk Criteria }\end{cases}
$$

where the $R\left(S_{t}\right)$ is the current risk level of the situation and is defined:

$$
R\left(S_{t}\right)=P\left(S_{t}\right) * S\left(S_{t}\right)
$$

where $P\left(S_{t}\right)$ is the probability of the situation at a time $t$ and depends on the objects of the subset space $\tilde{\sigma}$ :

$$
P\left(S_{t}\right):=P\left(S_{t} \mid o_{1}, o_{2}, \ldots, o_{m}\right) \text { with } o_{1}, o_{2}, \ldots, o_{m} \in \tilde{\sigma}
$$

and $S\left(S_{t}\right)$ is the severity of the situation. As a result of this modeling, the existence of a situation is inferred based on information in the world, i.e. the observable variables and objects of configuration space.

The probability of the existence of the first level situation is inferred directly from the values of the configuration space, and the probability of a higher level situation is calculated based on the existence probability of other situations. This also includes temporal dependencies, i.e. that the existence probability of an inferred situation in future can be supported by the earlier existence of the situation itself. The complete modeling of the dependencies results a network of situations.

The DBN-based situational network describes the evolution of the states of the system in terms of their joint probability distribution. At each instance in time $t$, the states of the system depend only on the states at the previous time slice $(t-1)$ and possibly the current time instance. Furthermore, the DBN-based situational network is a probability distribution function on the sequence of $T$ variables $X=\left\{x_{i}, \ldots, x_{T}\right\}$ and the sequence of $T$ observables $Y=\left\{y_{i}, \ldots, y_{T}\right\}$ that has the following factorization, which satisfies the requirements for DBNs that state $x_{i}$ depends only on state $x_{i-1}$ :

$$
P(X, Y)=\prod_{t=2}^{T} P\left(x_{t} \mid x_{t-1}\right) \cdot \prod_{t=1}^{T} P\left(y_{t} \mid x_{t}\right) \cdot P\left(x_{1}\right)
$$

The DBN parameters include the state transition pdf $P\left(x_{t+1} \mid x_{t}\right)$, the observation pdf $P\left(y_{t} \mid x_{t}\right)$ and pdf $P\left(x_{1}\right)$ using historical data, and prior knowledge or CPTs according to an expert's judgment should be defined.

### 3.2.5. Situation Risk Estimation

While the DBN-based situational network provides the modeling of situations of interest and the prior and posterior probability of the situations and their objects, the approach needs to generate an assessment

level of risk for every situation and shows whether or not the current risk level is acceptable. As such an estimation is highly subjective and related to inexact information, the application of fuzzy set theory is appropriate. Generally, the risk model calculation follows a multi-step process:

- Estimation of the situation likelihood
- Estimation of the situation severity
- Estimation of the situation risk


# 3.2.5.1 The Situation Likelihood Estimation 

To determine the prior and posterior likelihood, the DBN-based situational network provides the required quantities (i.e. Decision 1-2). The quantitative analysis can proceed along two lines, the forward (or predictive) analysis and backward (or diagnostic) analysis. In forward analysis, the probability of occurrence of any situation of the network is calculated on the basis of the prior probabilities of the objects and the conditional dependence of each node, and backward analysis consists of computing the posterior probability distribution of any situation and object, given the observation of a set of evidence variables. It can also be performed to find the most probable explanation (MPE) of the state of the objects leading to the hazardous situation or specific consequence.

### 3.2.5.2 The Situation Severity Estimation

The consequence states of a hazardous situation are usually determined by consequence analysis which concerns what may follow the occurrence of a hazardous situation. Indeed, such an occurrence may lead to a broad range of consequences, some of which will probabilistically be undesirable events. To project the degree of loss, a loss analysis process should be followed. Loss analysis comprises the systematic investigation of adverse outcomes associated with all incidents and accidents identified through consequence analysis. Generally, the loss of a consequence may be categorized into four groups; asset loss, human fatality, environmental loss, and confidence or reputation loss or a combination thereof (Hessami, 2010). It is useful for all four components to be converted and expressed in a common currency such as monetary value, for potential comparison and aggregation, to provide a coherent view of the totality of loss associated with a hazardous situation (Naderpour and Lu, 2013). Table 3 shows the proposed severity matrix of this paper which includes an equivalent dollar value of damage associated with each consequence category based on the severity of damage (i.e. Decision 1-3).

Table 3: Consequence severity matrix.


### 3.2.5.3 The Situation Risk Estimation

To estimate the risk level of every situation, a fuzzy logic system (FLS) is used. The basic structure of a FLS is shown in Figure 10 and consists of three parts: fuzzification of the input variables, the fuzzy inference process, and defuzzification.

![img-9.jpeg](img-9.jpeg)

Figure 10: Structures of a FLS (Markowski et al., 2011).

In the fuzzification process, fuzzy sets are formed for all input variables. The inference engine takes into account the input variables, i.e. likelihood and severity, and uses a risk matrix. The inference process is based on fuzzy logic operations which comprise the implication in each single rule and the aggregation of all rules. All output functions returned by the implication process for each rule are combined into a single output fuzzy set. Finally, the output fuzzy set of risk is defuzzified into a crisp value. This value is subsequently used for the risk evaluation category (i.e. Decision 1-4) (Markowski et al., 2011). The selection of a function essentially depends on the variable characteristics, available information and expert knowledge. In this paper, the shapes of the membership functions are defined as a combination of trapezoidal and triangular numbers to simplify the operation and increase the sensitivity in some bounds. The $\alpha$-cuts provide values of the variable for a specific degree of membership function. The values of degree of membership " 1 " and " 0 " are used to characterize the fuzzy sets for each variable. Tables 4-6 present the fuzzification of variables and Figure 11 illustrates the proposed fuzzy sets.

Table 4: Fuzzification of likelihood.


Table 5: Fuzzification of severity.


Table 6: Fuzzification of risk.


![img-10.jpeg](img-10.jpeg)

Figure 11: Membership functions of probability, severity and risk variables.

The fuzzy inference engine takes into account the input variables, likelihood and severity, and the logic relations between them, including the 25 rules (e.g. IF likelihood is E AND severity is MA THEN risk is $N A$ ) shown in Table 7, and uses fuzzy logic operations to generate the output. Mamdani's fuzzy inference method is the most commonly seen fuzzy methodology. In this inference, there is a fuzzy set after the aggregation process for each output variable that needs defuzzification. The characteristics of the Mamdani model are described in Table 8 (Mamdani, 1977).

Table 7: Risk matrix.


Table 8: Characteristics of the Mamdani model.


$\mu_{C}(x)=$ value of the resultant membership function.
$\mu_{A}(x)=$ value of the membership function where the input belongs to the fuzzy set A .
$\mathrm{z}=$ abscissa value, $\left(\mu_{C}(z)\right.$ is the ordinate $)$.

# 3.3. The Situation Recovery 

If the estimated risk of the situation is unacceptable, it is necessary to recover the situation. Identifying the risk-reducing measures therefore contributes to decisions about risk elimination, mitigation, transfer, control or an appropriate combination thereof. However the DBN does not provide the risk reduction measures; it helps to simulate the impact of risk recovery decisions on a situation. The options analysis identifies the actions which should be implemented to eliminate or reduce future hazardous situations. For each individually considered risk element, a decision must be made as to whether or not the investment in risk-reducing measures has the effect of reducing the risk to an acceptable level. A list of available reduction and containment options can be presented as decision rules where 'antecedent' is a situation, while 'consequent' is a suggested action to remove or eliminate the risk (i.e. Decision 2-1). Based on the operator's response to previous decision-making options, the situation assessment component has the ability to simulate the situation and estimate the new risk level of situations (i.e. Decision 2-2). The aim is to eliminate or reduce the risk level of situations to an acceptable level.

## 4. SA Measurement and Dealing with Uncertainty

The enhancement of SA is a major goal in the design and development of human-computer interfaces. To determine the degree to, which new technologies and design concepts improve operator's SA, it is necessary to systematically evaluate these technologies and concepts based on a measure of SA (Endsley, 1995a). The literature shows that the SAGAT ${ }^{1}$, which is a freeze probe technique, and the SART ${ }^{2}$, which is a self-rating approach, are the most common SA measurement techniques to have been applied during individual and team SA assessments (Stanton, 2005). In SAGAT, a task is randomly frozen, all displays and screens are blanked and a set of SA queries regarding the situation at the time of the freeze is administered. Operators are required to answer each query based upon their knowledge and understanding of the situation at the point of the freeze. At the end of the trial, the operator's responses are compared to the state of the system at the point of the freeze and an overall SA score is calculated (Endsley and Garland, 2000). However, Dekker (2013) criticizes the use of freeze probe measures for assessing SA, challenging the notion that the elements (i.e. data) in a situation wait for operators to become aware of them, operate on them, and attach meaning to them. Many other researchers Also argue that further investigation to develop the measurement of SA in complex and dynamic systems is required (Gorman et al., 2006; Salmon et al., 2009).

Most of traditional SA measurement studies are conducted through qualitative analysis methods. Qualitative techniques cannot be satisfactorily use to achieve quantitative SA measurements; thus, quantitative techniques based on statistical models (Kirlik and Strauss, 2006) and inference models (Ma and Zhang, 2008) have been merged. However, a common drawback is that these quantitative techniques completely replace qualitative information with numeric values. The existence of uncertainty is another reality of most operational human-machine systems. In the course of processing information, one applies background knowledge (forms a mental model of the situation) and uncertainty reasoning to handle perceptions with uncertainty (referred to as situation models). Therefore, in developing any SA measurement, two important aspects should be considered: 1) independently measuring the contribution of technology to SA, and 2) measuring the contribution of environmental uncertainty to SA (Kirlik and Strauss, 2006).

A graphical user interface (GUI) for the proposed situation risk awareness approach is developed based on SA-oriented design principles (Endsley, 2006) and using SMILE (Structural Modeling, Inference, and Learning Engine), which is a library of C++ classes (Laboratory, 1998) for implementing BNs in intelligent systems. In addition, research on linguistic decision making indicates that using

[^0]
[^0]:    ${ }^{1}$ Situation Awareness Global Assessment Technique
    ${ }^{2}$ Situation Awareness Rating Technique

linguistic terms is an efficient way to describe uncertain qualitative information. Therefore, in the light of research on linguistic information decisions, a SA measurement method that combines a qualitative information process and quantitative computation is being developed for a full validation of our humancomputer interface.

# 5. A Case Study: Application in a Mixing Tank 

To illustrate the implementation of the proposed approach in a real environment, a tank used for mixing flammable liquids is chosen.

### 5.1. The Case Description

According to a U.S. Chemical Safety Board (CSB) report following an incident at a paint manufacturing plant, the explosion and subsequent fire destroyed the facility, heavily damaged dozens of nearby homes and businesses, and shattered windows as far away as two miles. At least 10 residents required hospital treatment for cuts and bruises. Twenty-four homes and six businesses were damaged beyond repair. Dozens of boats at a nearby marina were heavily damaged by blast overpressure and debris strikes. The explosion was fueled by vapor released from a 2000-gallon tank of highly flammable liquid (CSB, 2008). In a similar case, the ignition of the vapor killed one person and injured two employees, as well as causing significant business interruption (CSB, 2007). The accident happened when the operator could not maintain accurate SA and the vapor overflowed the tank.

The environment includes an ink vehicle mix tank, approximately 3000 gallons in capacity, 10 feet tall and eight feet in diameter with a top-mounted mixer and a 12 -inch diameter access hatch that does not prevent air or vapor from passing through the opening. The tank is equipped with a steam heating jacket connected to the steam boiler. An operator controls the temperature of the mixture by opening and closing a turn ball valve on the steam pipe connected to the tank jacket. The operator accesses the tank top, weight and temperature display consoles, mixer control switches, and steam valves from a steel-grated mezzanine deck on the north side of the tank. The operator opens the slide valve on the dust collector suction line during the addition of dusty materials to the mix tank and closes it afterward. There are also eight 500 gallon steel totes in the area for the storage of solvents (Figure 12).

The building heating and ventilation system consists of a number of steam-coil fan units mounted near the ceiling, a fresh air distribution system and production area exhaust fans to remove flammable vapor from around the unsealed ink and paint mixers. It is assumed that the ventilation system has sufficient capacity to collect a huge volume of vapor. There are also safety systems which include a sprinkler system, an ignition barrier and an alarm system. A foam fire suppression sprinkler system is installed in the production area. In the event of a fire, fusible plugs on the $1 / 2$-inch orifice standard sprinkler heads will melt to activate the sprinkler head. Water flow in the fire suppression system will trigger the fire alarm box, which will send a signal to the fire department.

![img-11.jpeg](img-11.jpeg)

Figure 12: The mixing tank environment (CSB, 2008).

# 5.2. Situations of Interest 

There are several possible hazardous situations in the environment which threaten the system. To simplify the demonstration, one tank is chosen. As the investigation report shows, the important hazardous situations are as follow:

- $\mathrm{S}^{\mathrm{AV}}=$ Accumulated vapor in the production area
- $\mathrm{S}^{\mathrm{HT}}=$ High temperature inside the tank
- $\mathrm{S}^{\mathrm{BV}}=$ Building ventilation system malfunction
- $\mathrm{S}^{\mathrm{LS}}=$ Large spill from storage system

The first situation $\left(\mathrm{S}^{\mathrm{AV}}\right)$ is not directly inferable from the objects, i.e. it is "higher level situation" and has to be defined by dependencies on first level situations. The other situations can be inferred from their contributor objects, i.e. they are "first level situations".

### 5.3. Situation Modeling

First, the first level situations (i.e. $\mathrm{S}^{\mathrm{HT}}, \mathrm{S}^{\mathrm{BV}}$, and $\mathrm{S}^{\mathrm{LS}}$ ), which can be inferred from their contributor objects, are modeled. Their contributor objects, which are physical or conceptual, are determined as shown in Tables 9-11. As mentioned, these objects have two states (i.e. failure and success) and the prior probabilities of basic objects are determined based on data recorded by the Center for Chemical Process Safety (CCPS, 1989), and Offshore Reliability Data Handbook (OREDA, 2002). The CPTs of intermediate objects and focal objects are based on AND and OR gates definition. The CPTs of $\mathrm{S}^{\mathrm{HT}}, \mathrm{S}^{\mathrm{BV}}$, and $\mathrm{S}^{\mathrm{LS}}$ are shown in Tables 12-14; the CPTs of intermediate objects are omitted because they are set in a similar way.

Table 9: $\mathrm{S}^{\text {HT }}$ objects and symbols.


Table 10: $\mathrm{S}^{\mathrm{IV}}$ objects and symbols.


Table 11: $\mathrm{S}^{\mathrm{LS}}$ objects and symbols.


Table 12: CPT of $\mathrm{P}\left(\mathrm{S}^{\mathrm{III}}\right]$ MTC, TCS).


Table 13: CPT of $\mathrm{P}\left(\mathrm{S}^{\mathrm{IV}}\right]$ DP, F, B, V).


Table 14: CPT of $\mathrm{P}\left(\mathrm{S}^{\mathrm{LS}} \mid \mathrm{L}, \mathrm{TS}\right)$.


The higher level situation (i.e. $\mathrm{S}^{\mathrm{IV}}$ ), which can be inferred from the first level situations, has three physical objects which are safety barriers in the environment, as shown in Table 15; the states and prior probabilities of these objects are set in the same way as the basic objects of the first level situations. In addition, $\mathrm{S}^{\mathrm{IV}}$ has a consequence node, which has several states representing probable accidents, as shown

in Table 16. Because of the lack of historical data, the CPT of $\mathrm{S}^{\mathrm{AY}}$ is set using expert judgment, as shown in Table 17. The expert judgment has been made by an expert with good knowledge and experience in the oil industry. The prior probability of the higher level situation, i.e. $\mathrm{S}^{\mathrm{AY}}$, is set to 1 for Safe state and 0 for Hazardous state, and it is assumed that the environment is initially safe.

Table 15: $\mathrm{S}^{\mathrm{AY}}$ objects and symbols.


Table 16: The consequences node.


Table 17: CPT of $\mathrm{P}\left(\mathrm{S}^{\mathrm{AY}}\right.$; $\left.\mathrm{S}^{\mathrm{AY}}, \mathrm{S}^{\mathrm{HY}}, \mathrm{S}^{\mathrm{LS}}\right)$.


A temperature controller reports the temperature of the inside of the tank and a temperature sensor reports the temperature of the production unit. In addition, there is a sensor which shows the temperature of the outside environment. $\mathbf{S}^{\mathrm{HY}}$ can be inferred by the sensor which reports the temperature of the inside of the tank, and $\mathbf{S}^{\mathrm{BX}}$ can be inferred by the sensor which reports the temperature of the production unit, however the temperature of the production unit is affected by the outside temperature. Therefore, the appropriate connection between situations and observable variables are set as shown in Figure 14. In the next section, the states of observable variables are determined and their CPTs are set using expert judgment.

# 5.4. The Observable Variables 

The monitoring system provides update information about these observable variables to the evidence preparation component, and they are stored in a database and fuzzily prepared as inference evidence for use in the situation assessment component. The process for mixing 2000-gallons of ink in a tank involves heating for several hours, with the temperature controller being adjusted to maintain the temperature at $32^{\circ} \mathrm{C}\left(90^{\circ} \mathrm{F}\right)$. The temperature of the production unit in normal operation is about $25^{\circ} \mathrm{C}$ and the normal

interval of the outside temperature is $(0,40)$. The value ranges of the temperature variables are divided into fuzzy states as follows and their membership functions are illustrated in Figure 13:

- The temperature of the inside of the tank (ToI): \{Normal, High\}

$$
\begin{array}{lr}
\mu_{T o I(N)}(x)= \begin{cases}1 & x \leq 32 \\
(47-x) / 15 & 32<x \leq 47\end{cases} \\
\mu_{T o I(H)}(x)= \begin{cases}(x-32) / 15 & 32 \leq x<47 \\
1 & x \geq 47\end{cases}
\end{array}
$$

- The temperature of the production unit (ToP): \{Normal, High\}

$$
\begin{array}{lr}
\mu_{T o P(N)}(x)= \begin{cases}1 & x \leq 25 \\
(30-x) / 5 & 25<x \leq 30\end{cases} \\
\mu_{T o P(H)}(x)= \begin{cases}(x-25) / 5 & 25 \leq x<30 \\
1 & x \geq 30\end{cases}
\end{array}
$$

- The temperature of the outside environment (ToE): \{Low, Normal, High\}

$$
\begin{array}{rlrl}
\mu_{T o E(L)}(x) & = & 1 & x \leq 0 \\
& & (10-x) / 10 & 0<x \leq 10 \\
\mu_{T o E(N)}(x) & = & x / 10 & 0 \leq x<10 \\
& 1 & 10 \leq x<30 \\
\mu_{T o E(H)}(x) & = & (40-x) / 10 & 30 \leq x<40 \\
& 1 & 30 \leq x<40 \\
& & x \geq 40
\end{array}
$$

![img-12.jpeg](img-12.jpeg)

Figure 13: The membership functions of the observable variables.

# 5.5. The DBN-Based Situational Network Evaluation 

A DBN-based situational network is developed and illustrated in Figure 14. The figure shows the situations of interest in which higher level situations are colored red and first level situations are colored blue, the objects are shown in yellow, and observable variables are depicted in green. The time difference of one time step is set to one minute. The temporal arc points to the $S^{A V}$ situation itself, as it is assumed that the situation is formed after a time interval which is longer than one minute. The interpretation is that the vapor accumulates when the high temperature persists for a while inside the tank, or there is a large spill from the storage system and operation of the ventilation system is unable to disperse the vapor.


![img-13.jpeg](img-13.jpeg)

Figure 14: The DBN structure for four situations of interest.

The sensitivity analysis is conducted to evaluate the developed situational network. Examination of the model at time $t$ reveals that when the failure probability of $S$ is set to 1 (i.e. failure of sensor), this results in a revised failure probability of 1 from 0.23 for TCS, and a hazardous probability of 0.04 from 0.01 for $\mathrm{S}^{\mathrm{HT}}$. Similarly, at time $t$, when the failure probability of MSV is set to 1 (i.e. failure), the posterior probability of MTC and $\mathrm{S}^{\mathrm{HT}}$ is increased to 1 from 0.04 and 0.043 respectively. Both these failures result a hazardous probability of 0.5 from 0.01 for $\mathrm{S}^{\mathrm{AV}}$ at time $t+1$ (temporal dependency). Likewise, when at time $t$ the failure probability of F is set to 1 , this results an increased hazardous probability of 1 from 0.07 for $\mathrm{S}^{\mathrm{BV}}$, and a hazardous probability of 0.95 from 0.5 for $\mathrm{S}^{\mathrm{AV}}$ at time $t+1$. Equally, when at time $t$ the failure probability of L is set to 1 , the probability of $\mathrm{S}^{\mathrm{LS}}$ and $\mathrm{S}^{\mathrm{AV}}$ are increased to 1 and 0.98 from 0.001 and 0.95 .

# 5.6. The Performance of the Proposed Approach 

On 22 November 2006, the temperature of the mixing tank and the production unit started to increase; the former deviated from normal value at 9:10 AM and the latter deviated from normal value at 9:15 AM. The temperature of the outside environment was steady at $12^{\circ} \mathrm{C}$. The trend of observable variables for 60 minutes is illustrated in Figure 15, together with the fuzzy partitioning values of ToI and ToP. The fuzzy partitioning value of ToE is omitted because it was steady in its normal range. These data can be interpreted as ground truth data to evaluate the performance of the proposed approach.

![img-14.jpeg](img-14.jpeg)

Figure 15: The observable variables and their fuzzy partitioning values.

By assigning the primary probabilities to the DBN-based situational network, one minute after the start of the period, i.e. 9:01 AM, the probability of $\mathrm{S}^{\mathrm{AV}}$ is 0.01 and the probabilities of the consequence states are calculated as shown in Table 16. As can be seen, the safe state is the most probable consequence of $\mathrm{S}^{\mathrm{AV}}$. The total loss of $\mathrm{S}^{\mathrm{AV}}$, i.e. its severity, can be calculated by multiplication of the probabilities and losses of consequence, which are about $\$ 3.82 \mathrm{E}+03$. Therefore the estimated risk level of $\mathrm{S}^{\mathrm{AV}}$ is 1.3 , which means that the current risk level of $\mathrm{S}^{\mathrm{AV}}$ is acceptable. It is worth noting that for first level situations, i.e. $\mathrm{S}^{\mathrm{HT}}, \mathrm{S}^{\mathrm{BV}}$ and $\mathrm{S}^{\mathrm{LS}}$, the accumulated vapor can be considered as their consequence, in which the degree of loss is about $\$ 1 \mathrm{E}+05$.

By assigning the fuzzy soft evidence which the data preparation component provides for the situation assessment component, the posterior probabilities of the situations are updated during the period as well as their risk levels, as shown in Figure 16. As can be seen, the risk level of $\mathrm{S}^{\mathrm{HT}}$ is TNA from minutes 15 to 27 and the risk level of $\mathrm{S}^{\mathrm{BV}}$ is TNA from minutes 20 to 24 . The risk level of $\mathrm{S}^{\mathrm{LS}}$ is acceptable during this period. The risk level of $\mathrm{S}^{\mathrm{AV}}$ is TNA from minutes 22 to 25 exactly after increasing the risk level of $\mathrm{S}^{\mathrm{BV}}$, which is because of the assumption that the local and area ventilation systems have the ability to disperse the vapor. However, there was a one minute delay because of the temporal definition. After minutes 24 , the risk level of $\mathrm{S}^{\mathrm{AV}}$ has been reduced to an acceptable level because the risk level of $\mathrm{S}^{\mathrm{BV}}$ has been decreased to an acceptable level.

![img-15.jpeg](img-15.jpeg)

Figure 16: The posterior probabilities and risk levels of situations.

# 5.7. Situation Recovery 

The system is set to trigger an alarm for every situation which has a risk level more than 2.5, i.e. tolerable not acceptable. At 9:16 AM when the risk level of $S^{\mathrm{HT}}$ rose, the system showed that the most probable explanation was the failure of the pneumatic unit (PU), but an inspection at 9:18 AM determined the valid performance of the PU. New evidence (success of the PU system) showed that the failure of the tank's sensor was the most probable factor. Considering the result of the situation assessment, maintenance decisions were made to recover the situation. The proposed approach helps the operator in hazardous situation to prevent accidents, but it can present the factors which contribute to the creation of an accident or a specific consequence as well. For instance, if at 9:26 AM a fire with low death and moderate property damage (C4) is reported, the posterior probability updating from this evidence shows that the tank sensor failure or leakage from the transfer piping and belt failure cause the accumulated vapor, and the failure of the ignition barrier creates the fire.

## 6. Conclusion and Future Work

This paper has presented a new human-centric situation risk awareness approach to support process operators in abnormal situations. The requirements of the approach were determined based on GDTA methodology which provides an actionable model that accurately supports human cognition. The approach has two major components: an evidence preparation component and a situation assessment component. The former uses a fuzzy partitioning method to provide the soft evidence to use in the next component. The latter includes a DBN-based situational network to model the abnormal situations in a network, and a fuzzy risk estimation method to generate the assessment result and show whether or not the risk level of situations is acceptable. As has been shown, the approach provides a useful graphical model that meets the requirements of a practical SA system. Its probability provides a mathematically consistent framework for dealing with uncertain and incomplete information and, since the reasoning is conducted using one probabilistic model, all the answers derived from a single multi-dimensional distribution are consistent. In addition, the Bayesian probability framework facilitates the inclusion of prior background knowledge and the updating of this knowledge when new information is available from

the SCADA monitoring system. The effectiveness of the proposed approach was demonstrated through a real case study and the application results discussed.

The first direction for future study is to develop a GUI based on the proposed theoretical material and its evaluation based on a developed SA measurement. The second direction is to extend the proposed system to a distributed system that applies the team SA concept, because in many chemical plants, the safety of the process is supervised by operators and engineers from a range of departments (e.g. maintenance) who are members of a team and have a common goal and specific roles in interacting with elements in the task environment.

# Acknowledgment 

The first author sincerely appreciates the advice and suggestions of Professor Faisal Khan form the Process Safety and Risk Engineering Group at Memorial University, Canada.

The work presented in this paper was supported by Australian Research Council (ARC) under the Discovery Projects DP088739 and DP110103733.
