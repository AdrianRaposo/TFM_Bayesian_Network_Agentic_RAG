"© 2013 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or future media, including reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of this work in other works."

# A Fuzzy Dynamic Bayesian Network-Based Situation Assessment Approach 

Mohsen Naderpour, Jie Lu, Guangquan Zhang<br>Decision Systems and e-Service Intelligence Laboratory<br>Centre for Quantum Computation \& Intelligent Systems, School of Software<br>Faculty of Engineering and IT, University of Technology, Sydney<br>PO Box 123, Broadway NSW 2007 Australia<br>Mohsen.Naderpour@student.uts.edu.au, \{Jie.Lu, Guangquan.Zhang\}@uts.edu.au


#### Abstract

Situation awareness (SA), a state in the mind of a human, is essential to conduct decision-making activities. It is about the perception of the elements in the environment, the comprehension of their meaning, and the projection of their status in the near future. Two decades of investigation and analysis of accidents have showed that SA was behind of many serious large-scale technological systems' accidents. This emphasizes the importance of SA support systems development for complex and dynamic environments. This paper presents a fuzzy dynamic Bayesian network-based situation assessment approach to support the operators in decision making process in hazardous situations. The approach includes a dynamic Bayesian network-based situational network to model the hazardous situations where the existence of the situations can be inferred by sensor observations through the SCADA monitoring system using a fuzzy quantizer method. In addition to generate the assessment result, a fuzzy risk estimation method is proposed to show the risk level of situations. Ultimately a hazardous environment from U.S. Chemical Safety Board investigation reports has been used to illustrate the application of proposed approach.


Keywords-situation awareness; situation assessment; dynamic Bayesian network; fuzzy sets

## I. INTRODUCTION

Since the beginning of the industrial revolution many serious large-scale technological systems' accidents that had grave consequences, such as those of Three Mile Island, Bhopal and Chernobyl, have primarily been attributed to human error. In fact, in the vast majority of these accidents the human operator was striving against significant challenges such as data overload and the task of working with a complex system. Actually, the persons are not the cause of these errors but they have inherited the problems and difficulties from the technologies that engineers have created. Operators generally have no difficulty in physically performing their tasks, and no difficulty in knowing what is the correct thing to do, but they are stressed by the task of understanding what is going on in the situation [1]. Over the last two decades, great deal of research has been undertaken in the area of Situation awareness (SA).

Situation awareness can be described as knowing and understanding what is going on around you and predicting how things will change. In control of complex systems where
multiple goals should be pursued simultaneously, multiple tasks need operator's attention, the operator's performance is under high time stress and negative consequences associated with poor performance is expected, SA is quite likely to be behind many accidents. On 23 March 2005, for instance, 15 workers were killed and 170 injured in the explosion at a refinery located in south-east Texas. An important factor identified in this catastrophic accident was the difficulty experienced by the operator in maintaining an accurate SA while monitoring a complex, dynamic environment.

Today in technological systems, operators have often been moved to a control room far away from the physical process, where automated systems pass more and more information to them, so they have to handle more data and more responsibility. In the presence of all this data, operators are finding that they are even less aware than before about the situations they are controlling. This has led to a huge gap between the massive amount of data produced and disseminated and the operator's ability to effectively assimilate the required data and to make timely, accurate decisions [2]. This emphasizes the importance of designing human-computer interaction (HCI) to support SA in dynamic environments.

This paper considers the applicability of SA concept to safety of complex systems where the degree of automation and complexity are increasing and the number of operators is decreasing, and each operator must be able to comprehend and respond to an ever increasing amount of available risky status and alert information. This paper introduces a fuzzy dynamic Bayesian network-based situation assessment approach which includes three major parts. First, it includes a fuzzy quantizer method to discrete the observable variables extracted from sensors which will be used as soft evidences in the next part. Second, it enjoys a situational network based on dynamic Bayesian network (DBN) to model the hazardous situations. Third, the approach uses a fuzzy risk estimation method to generate the assessment result and show that the risk level is acceptable or not.

The paper is organized as follows. Section II presents background and related works. Section III describes the fuzzy dynamic Bayesian network-based situation assessment approach. A case study from U.S. Chemical Safety Board investigation report is presented in Section IV. Finally, conclusion and future work is provided in Section V.

## II. BACKGROUND AND RELATED WORKS

## A. Situation Awareness

A situation is a collection of objects which have relationships with one another and the environment, and an object is a physical entity that is within the grasp of the senses [3]. Situation awareness can be described as "the perception of the elements in the environment within a volume of time and space, the comprehension of their meaning and the projection of their status in the near future" [2]. This SA model follows a chain of information processing, from perception, through interpretation, to projection. The levels of SA are as follows:

- Perception: Perception includes the sensory detection of important cues (e.g. status, attributes, and dynamic elements) in the environment.
- Comprehension: Comprehension is the understanding of the meaning or significance of that information in the light of goals. This process results in a comprehensive picture of the environment.
- Projection: Projection involves extrapolating information forward in time to understand how it will affect near future states of the environment. The higher level of SA provides a timely and effective manner for operators to function appropriately, even with very complex and challenging tasks.


## B. Situation Assessment

Situation awareness is a state of knowledge that has to be distinguished from the processes underlying the achievement of SA, which should be addressed as situation assessment [1]. The situation assessment models describe basic principles and general features about how people process information or interact with the environment to attain their SA. In fact, awareness information for a situation is derived as the results of situation assessment. Since SA is regarded as a dynamic and collaborative process, assessing a situation is often required data integration or called data fusion with support of computer based intelligent techniques [4-7]. The enhancement of operators' SA in complex systems is a major design goal in developing operator interfaces, automation concepts and training plans in a wide variety of fields $[4,7,8]$. As SA aims to predict the status of a situation in the near future, which is the third level of the SA model, proper and effective situation assessment approaches and tools to conduct the prediction, is required. For example, many studies have reported that machine learning techniques could be an effective method for intelligent prediction by extracting rules from previous data to generate new assessment results [4], however their use has been limited, possibly because of the lack of rich training data for this problem [9]. In command and control applications, Bayesian networks have been considered widely in situations assessment configuration [10]. Some authors considered computational method, but usually computational approaches often do not satisfactorily handle all forms of uncertainty, therefore, some cognitive approaches which use the fuzzy logic system to address the limitations of traditional models in producing the full range of human behaviors, have been developed [11].

## C. Dynamic Bayesian Networks

A BN is a directed acyclic graph whose nodes correspond to random variables and the arcs between nodes represent dependencies or direct causal influences between variables. The force of these dependencies is represented by conditional probabilities. Conventional BN can be considered as a representation of static cause-effect relations among objects in a situation. The BN represents the joint probability distribution $P(X)$ of variables $X=\left\{X_{l}, \ldots, X_{n}\right\}$, included in the network as:

$$
\mathrm{P}(\mathrm{X})=\prod_{\mathrm{i}=1}^{\mathrm{n}} \mathrm{P}\left(\mathrm{X}_{\mathrm{l}} \mid \mathrm{Pa}\left(\mathrm{X}_{\mathrm{i}}\right)\right)
$$

where $\operatorname{Pa}\left(X_{i}\right)$ is the parent set of $X_{i}$ for any $i=1, \ldots, n$. If $\operatorname{Pa}\left(X_{i}\right)$ is an empty set, then $X_{i}$ is a root node and $\mathrm{P}\left(\mathrm{X}_{\mathrm{l}} \mid \mathrm{Pa}\left(\mathrm{X}_{\mathrm{i}}\right)\right)=\mathrm{P}\left(\mathrm{X}_{\mathrm{l}}\right)$ denotes its prior probability. BN takes advantage of Bayes theorem to update the prior occurrence probability of objects given new information, called evidence $E$, thus yielding the posteriors. This new information usually becomes available during the operational life of a system, including occurrence or nonoccurrence of the objects [12]:

$$
\mathrm{P}(\mathrm{X} \mid \mathrm{E})=\frac{\mathrm{P}(\mathrm{X}, \mathrm{E})}{\mathrm{P}(\mathrm{E})}=\frac{\mathrm{P}(\mathrm{X}, \mathrm{E})}{\sum_{\mathrm{E}} \mathrm{P}(\mathrm{X}, \mathrm{E})}
$$

The static BN can be extended to a dynamic BN (DBN) model by introducing relevant temporal dependencies that capture the dynamic behaviors of the domain variables between representations of the static network at different times. Two types of dependencies can be distinguished in a DBN: contemporaneous dependencies and non-contemporaneous. Contemporaneous dependencies refer to arcs among nodes that represent variables within the same time period. Noncontemporaneous refer to arc between nodes which represent variables at different times. A DBN is defined as a pair $\left(B_{1}, 2 T B N\right)$ where $B_{l}$ is a BN which define the prior distribution $P\left(X_{l}\right)$ and $2 T B N$ is a two-slice temporal BN with

$$
\mathrm{P}\left(\mathrm{X}_{\mathrm{t}} \mid \mathrm{X}_{\mathrm{t}-1}\right)=\prod_{\mathrm{i}=1}^{\mathrm{n}} \mathrm{P}\left(\mathrm{X}_{\mathrm{l}}^{\mathrm{t}} \mid \mathrm{Pa}\left(\mathrm{X}_{\mathrm{l}}^{\mathrm{t}}\right)\right)
$$

where $\mathrm{X}_{\mathrm{t}}^{\mathrm{t}}$ is a node at time slice $t$ and $\mathrm{Pa}\left(\mathrm{X}_{\mathrm{t}}^{\mathrm{t}}\right)$ is the set of parent nodes which can be in time slice $t$ or $t-1$. The nodes in the first slice of a $2 T B N$ do not have any parameters associated with them, but each node in the second slice has an associated conditional probability distribution (CPD) for continues variables or conditional probability table (CPT) for discrete variables, which defines $\mathrm{P}\left(\mathrm{X}_{\mathrm{l}}^{\mathrm{t}} \mid \mathrm{Pa}\left(\mathrm{X}_{\mathrm{l}}^{\mathrm{t}}\right)\right)$ for all $\mathrm{t}>1$. The arcs between slices are from left to right, reflecting the casual flow of time. If there is an arc from $\mathrm{X}_{\mathrm{t}-1}^{\mathrm{t}}$ to $\mathrm{X}_{\mathrm{l}}^{\mathrm{t}}$, this node is called persistent. The arcs within a slice are arbitrary. Directed arcs within a slice represent "instantaneous" causation. The semantics of a DBN can be defined by "unrolling" the 2TBN until there are $T$ time-slices. The resulting joint distribution is then given by:

$$
\mathrm{P}\left(\mathrm{X}_{1 / \mathrm{T}}\right)=\prod_{\mathrm{t}=1}^{\mathrm{T}} \prod_{\mathrm{i}=1}^{\mathrm{n}} \mathrm{P}\left(\mathrm{X}_{\mathrm{l}}^{\mathrm{t}} \mid \mathrm{Pa}\left(\mathrm{X}_{\mathrm{l}}^{\mathrm{t}}\right)\right)
$$

Several inference methods for a DBN can be used such as clustering and unrolled junction tree [13].

## III. A FUZZY DYNAMIC BAYESIAN NETWORK-BASED SITUATION ASSESSMENT APPROACH

The main goal of our approach is to provide an actionable base for operators to monitor the hazardous situations and be aware of their risk level, and take appropriate actions to reduce the risk to an acceptable level. The approach consists three major parts as shown in Fig. 1.
![img-0.jpeg](img-0.jpeg)

Fig. 1. A fuzzy DBN-based situation assessment approach.

## A. A Fuzzy Quantizer Method

This part based on online condition and process monitoring system provides the current state of the observable variables, conducts a discretization process and transfers the result to the next part. According to condition and process monitoring, each observable variable value is obtained from field sensors based on SCADA (Supervisory Control and Data Acquisition) systems. As the observable variables extracted from sensors are continuous, to use them in DBN, a discretization process is required. In general, mapping continuous variable to discrete one can be done with a quantizer like a fuzzy partitioning.
Definition 1 (Fuzzy random variable): Let $(\Omega, \mathcal{F}, P)$ be a probability space, $F(\mathbb{R})$ the set of fuzzy numbers in $\mathbb{R}$ with compact supports and $W$ is a mapping $\Omega \rightarrow F(\mathbb{R})$. Then $W$ is a fuzzy random variable if and only if given $\omega \in \Omega, W_{\alpha}(\omega)$ is a random interval for any $\alpha \in[0,1]$ where $W_{\alpha}(\omega)$ is a $\alpha$-level set of the fuzzy set $W(\omega)$ [14].
Definition 2 (Fuzzy state): Let the crisp state set $\mathcal{P}$ consist of the states $p_{1}, p_{2}, \ldots, p_{n}$. Then, each fuzzy state can be written as a vector $q=\left[q_{1}, q_{2}, \ldots, q_{n}\right]$, where $q_{i} \in[0,1]$. This way, each fuzzy state can be considered as a possibility distribution or alternatively as a fuzzy set $q \in \mathcal{F}(\mathcal{P}),(\mathcal{F}(\mathcal{P})$ the set of all fuzzy subsets defined for $\mathcal{P})$ determining the degree $q_{i}$ by which the system participates in each crisp state $p_{i}$, provided it is in the current fuzzy state $q[15]$.

Now suppose $X=\left\{X_{1}, X_{2}, \ldots, X_{n}\right\}$ be the set of variables in a BN. If the variable $X_{i}$ is a continuous variable then it can be transformed into a fuzzy random variable $W_{i}$. The corresponding set $U_{i}$ can be utilized to map the variable $X_{i}$ to fuzzy states:

$$
U_{i}=\left\{\tilde{X}_{i 1}, \tilde{X}_{i 2}, \ldots, \tilde{X}_{i m}\right\}
$$

where $\tilde{X}_{i j}$ is the $j$-th fuzzy state and $m$ denotes the number of the fuzzy states, and fuzzy state $\tilde{X}_{i j}$ can be defined as following:

$$
\tilde{X}_{i j}=\left\{\mu_{\tilde{X}_{i j}}(x) \mid x \in \boldsymbol{X}_{i}\right\}
$$

where $\mu_{\tilde{X}_{i j}}(x)$ is the membership function of fuzzy state $\tilde{X}_{i j}$, $X_{i}$ is the frame of $X_{i}$, and $x$ denotes the value of variable $X_{i}$. For a continues variable $X_{i}$, its condition probability in the BN with its parent can be replaced by $P\left(W_{i} \mid P a\left(W_{i}\right)\right)$ :

$$
P\left(X_{i} \mid P a\left(X_{i}\right)\right) \rightarrow P\left(W_{i} \mid P a\left(W_{i}\right)\right)
$$

where $W_{i}$ is the corresponding fuzzy random variable defined by $X_{i}$. For a node without parents, soft evidence is equivalent to modifying its prior probability; otherwise, soft evidence on a variable $X_{i}$ is represented by a conditional probability vector $P\left(X_{i}=x \mid H_{i}\right)$ for $i=1,2, \ldots, m$, where $H_{i}$ denotes the hypothesis that the true state is the $i$-th state. To simplify the inference process for continues variables, consider the fuzzy random variable $W_{i}$ with states $\left\{\tilde{X}_{i 1}, \tilde{X}_{i 2}, \ldots, \tilde{X}_{i m}\right\}$. Define $H_{i}$, $j=1,2, \ldots, m$ as hypotheses that $W_{i}$ is in state $\tilde{X}_{i j}$. The results of fuzzy function member $\mu_{\tilde{X}_{i j}}(x) \quad j=1,2, \ldots, m$ form the soft evidence vector:

$$
e=\left\{\mu_{\tilde{X}_{i 1}}(x), \mu_{\tilde{X}_{i 2}}(x), \ldots, \mu_{\tilde{X}_{i m}}(x)\right\}
$$

The $\mu_{\tilde{X}_{i j}}(x)$ is approximately considered to be equivalent to the condition probability $P\left(\mu_{\tilde{X}_{i j}} \mid X_{i}=x\right)$ Then the soft evidence vector can be defined as:

$$
e=\left\{P\left(W_{i}=1 \mid H_{1}\right), P\left(W_{i}=1 \mid H_{2}\right), \ldots, P\left(W_{i}=1 \mid H_{m}\right)\right\}
$$

where $P\left(W_{i}=1 \mid H_{j}\right)$ represents that the observed value of $W_{i}$ is " 1 " if the state is $\tilde{X}_{i j}$, which is indeed the probability $P\left(\mu_{\tilde{X}_{i j}} \mid X_{i}=x\right)[16]$.

## B. A DBN-Based Situational Network

A situation is a collection of physical or conceptual objects, or both which have relationships to each other and environment. The emphasis in situation definition is on relationships. The relations are viewed from the point of view of a thing (i.e. focal object), and how other things in the surroundings are related to it. In this part a DBN-based situational network is developed to model the situations of interest into a network while every situation is modeled by a simple BN, based on constitutive objects. To achieve the goal, two types of hazardous situations are considered: 1) first level situations: the objects of a situation and their interactions may create a hazard; 2) higher level situations: relationships among situations may produce a hazard. To find the situations of interest, hazard identification methods and experts' knowledge should be used. In many areas, hazardous situations have been obtained through design and implement phases and various models have been developed to identify them. For example, HAZOP is one of the most powerful methods available and has been well described in the literature.

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

and $S\left(S_{t}\right)$ is the severity of the situation. Due to this modeling, the existence of situation is inferred based on information in the world i.e. the observable variables and objects of configuration space. The first level situation can be illustrated by a simple BN based on its objects. Usually the BN begins by root nodes that include the basic objects. It follows by intermediate nodes, a pivot node and leaf nodes. The pivot node is the focal object which delegates the situation, and relations among root nodes and pivot node defines the relationships among the objects. The leaf nodes are safety barriers which are some physical objects of the environment and will connect to each other if there is relation between their performances. Also one of the leaf nodes may be a consequence node which has some states, and shows the possible accidents of the situation. There are also situations, which can only be inferred by observing the real word over a period of time. Although the situations are characterized by information collected over a time-period, they only exist at a special point in time. Their existence in the next time-point has to be verified again.

The higher level situations can be inferred from other situations. Several situations can exist in parallel or the existence of one situation can exclude the existence of another situation. Fig. 2 shows an example network of situations. As can be seen, there are four situations of interest, namely A, B, C and D , where A and B belong to first level situations category. They can be inferred directly from objects $\mathrm{O}_{1}, \mathrm{O}_{2}$ and $\mathrm{O}_{3}$ and situations C and D are higher level situations and their existence is dependent on the existence of lower level situations.
![img-1.jpeg](img-1.jpeg)

Fig. 2. A network of situations.
The existence probability of first level situation is inferred directly from the values of the configuration space, and the probability of higher level situation is calculated based on the
existence probability of other situations. This also includes temporal dependencies, i.e. that the existence probability of an inferred situation in future can be supported by the earlier existence of the situation itself. The complete modeling of the dependencies results a network of situations. The DBN parameters are defined using historical data and prior knowledge or an expert's judgment.

## C. A Fuzzy Risk Estimation Method

While the previous part provides the modeling of situational network and prior and posterior probability of situations and their objects, this part generates the assessment level of risk for every situation and shows that the current risk level is acceptable or not. As such estimation is highly subjective and related to inexact and vague information, the application of fuzzy set theory is appropriate. Generally, the risk model calculation follows a multi-step process: 1) Estimation of the situation likelihood, 2) Estimation of the situation severity, and 3) Estimation of the situation risk

To determine the prior and posterior likelihood, the DBNbased situational network provides the required quantities. The quantitative analysis of a DBN can proceed along two lines, the forward (or predictive) analysis and backward (or diagnostic) analysis. The occurrence of a hazardous situation may potentially lead to a broad range of consequences, some of which may probabilistically be undesirable events. Generally the loss of a consequence may be categorized into four groups; asset loss, human fatality, environmental loss, and confidence or reputation loss. It is useful for all four components to be converted and expressed in a common currency such as money for potential comparison and aggregation in order to provide a coherent view of the totality of loss associated with a hazardous situation.

To estimate the risk level we use a fuzzy logic system (FLS) as shown in Fig.3. FLS consists of three steps: fuzzification of the input variables, fuzzy inference process and defuzzification. In the fuzzification process, the fuzzy sets are formed for all variables. The inference engine takes into account the input variables i.e. likelihood and severity and uses a risk matrix. The inference process is based on fuzzy logic operations which are the implication in each single rule and the aggregation from all rules. All output functions returned by the implication process for each rule are combined into a single output fuzzy set. Finally, the output fuzzy set of risk is defuzzified into a crisp value. This value is subsequently used for the risk evaluation category [17].
![img-2.jpeg](img-2.jpeg)

Fig. 3. Structures of FLS.

A fuzzy set is determined by the membership function e.g. triangular, trapezoidal and Gaussian. However the selection of a function essentially depends on the variable characteristics, available information and expert's knowledge. In this paper, the shapes of the membership functions are defined as a combination of trapezoidal and triangular numbers to simplify the operation and increase the sensitivity in some bounds. The Alpha level cuts ( $\alpha$ ) provide values of the variable for a specific degree of membership function. The values of degree of membership " 1 " and " 0 " are used to characterize the fuzzy sets for each variable. Table I-III present fuzzification of variables and Fig. 4 illustrates the proposed fuzzy sets. The fuzzy inference engine takes into account the input variables and logic relations between them included 25 rules as shown in Table IV, and uses fuzzy logic operations to generate the output. Mamdani's fuzzy inference method is the most commonly seen fuzzy methodology. The characteristics of the Mamdani model is described in Table V [18].

TABLE I: FUZZIFICATION OF LIKELIHOOD.


TABLE II: FUZZIFICATION OF SEVERITY.


TABLE III: FUZZIFICATION OF RISK.


TABLE IV: RISK MATRIX.


TABLE V: CHARACTERISTICS OF THE MAMDANI MODEL.

(AND) | MIN | $\begin{gathered} \mu_{C}(x)=\min \left(\mu_{A}(x), \mu_{B}(x)\right) \ =\mu_{A}(x) \wedge \mu_{B}(x) \end{gathered}$  |
|  Implication
Aggregation | MIN
MAX | $\max \left(\min \left(\mu_{A}(x), \mu_{B}(x)\right)\right)$  |

$\mu_{C}(x)=$ value of the resultant membership function. $\mu_{A}(x)=$ value of the membership function where the input belongs to the fuzzy set A . $z=$ abscissa value, $\left(\mu_{C}(z)\right.$ is the ordinate $)$. $z=$ abscissa value, $\left(\mu_{C}(z)\right.$ is the ordinate $)$.![img-3.jpeg](img-3.jpeg)

Fig. 4. Membership functions of variables.

## IV. A CASE Study: APPLICATION IN A Mixing TANK

To illustrate the implementation of proposed approach in a real environment, an open top tank which is used for mixing a flammable liquid, is chosen. In similar situation, the ignition of a vapor cloud generated by mixing and heating a flammable liquid, one person was killed and two employees were injured and caused significant business interruption. The accident happened when an operator was mixing and heating a flammable mixture of heptane and mineral spirits in a 2,200gallon open top tank equipped with steam coils (Fig. 5) and the operator could not maintain accurate SA until the vapor overflowed from the tank. [19].

## A. The Case Description

The environment includes a tank which is equipped with steam coils that supplies required heat for the mixing process, a temperature controller includes a temperature sensor and a pneumatic control unit, and the steam valves which are operated based on the mixture temperature. Also there are some safety systems which include a sprinkler system, an ignition barrier and an alarm system. The environment has a

local and an area exhaust ventilation systems which are assumed that have enough capacity to collect a huge volume of vapor. The sprinkler system and the fire alarm system have been designed that if a fire occurs or if there is accumulated vapor, they reduce the damage. An operator checks the temperature using an infrared thermometer, and monitors the situation and conducts appropriate actions when it is necessary.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Mixing tank environment [15].

## B. Situations of Interest

There are some possible hazardous situations in the environment which threaten the system. As the investigation report shows the important hazardous situations are as follow:

- $\mathrm{S}^{\mathrm{AV}}=$ Accumulated vapor in the production building
- $\mathrm{S}^{\mathrm{HT}}=$ High temperature inside the tank
- $\mathrm{S}^{\mathrm{IV}}=$ Inadequate building ventilation

The first situation is not directly inferable from the objects i.e. it is "higher level situation" and it has to be defined by some dependencies to first level situations. Table VI shows the safety barriers and consequence node which are affected by $\mathrm{S}^{\mathrm{AA}}$. The second and third situations can be inferred from their contributor objects and observable variables i.e. they are "first level situation", and to assess them, some physical and conceptual objects are determined as shown in Table VII-VIII respectively [12].

TABLE VI: $\mathrm{S}^{\mathrm{AV}}$ OBJECTS AND SYMBOLS.


TABLE VII: $\mathrm{S}^{\mathrm{IV}}$ OBJECTS AND SYMBOLS.


TABLE VIII: $\mathrm{S}^{\text {HT }}$ ObJeCTS AND SYMBOLS.


## C. The Observable Variables

As noted, there is a sensor which reports the temperature of the inside of the tank every minute. Also there is an environment temperature sensor which shows the temperature of the production unit after a while repeatedly. The SCADA monitoring system transfers the updated information about these variables to our approach where they can store in database and fuzzily get ready as inference evidences to use in next DBN-base situational network.

The process for making Super Clean and Tilt required several hours of mixing and heating, and it needs to be adjusted the temperature controller to maintain the temperature at $73^{\circ} \mathrm{C}$. The environment temperature in normal operation is about $35^{\circ} \mathrm{C}$. The value ranges of temperature variables are divided into two fuzzy states include Safe and Hazardous, and their membership functions are determined as follow as well as showed in Fig. 6:

- The temperature of the inside of the tank (ToI):

$$
\begin{aligned}
& \mu_{\text {ToI }(S)}(x)= \begin{cases}1 & x \leq 73 \\
(77-x) / 4 & 73<x \leq 77\end{cases} \\
& \mu_{\text {ToI }(H)}(x)= \begin{cases}(x-73) / 4 & 73 \leq x<77 \\
1 & x \geq 77\end{cases}
\end{aligned}
$$

- The temperature of the production building (ToB):

$$
\begin{aligned}
& \mu_{\text {ToB }(S)}(x)= \begin{cases}1 & x \leq 35 \\
(40-x) / 5 & 35<x \leq 40\end{cases} \\
& \mu_{\text {ToB }(H)}(x)= \begin{cases}(x-35) / 5 & 35 \leq x<40 \\
1 & x \geq 40\end{cases}
\end{aligned}
$$

![img-5.jpeg](img-5.jpeg)
(a)
![img-6.jpeg](img-6.jpeg)
(b)

Fig. 6. The membership functions of observable variables.

## D. Structure of the DBN-Based Situational Network

A DBN-based situational network is developed and illustrated in Fig. 7. The temporal arc is pointing to the $\mathrm{S}^{\mathrm{AV}}$ situation itself as it is assumed that the situation is formed after a time interval, which is longer than a minute. The interpretation is that the vapor is accumulated when the high temperature last for a while inside the tank and the ventilation system operation cannot evacuate the vapor.
![img-7.jpeg](img-7.jpeg)

Fig. 7. The DBN-based situational network.
At the beginning, the prior probability of the higher level situation i.e. $\mathrm{S}^{\mathrm{AV}}$, is set to " 1 " for safe state and " 0 " for hazardous state as it is assumed that the environment is safe at the start time. To establish other parameters, namely conditional probabilities of the network, historical data and expert's judgment are used. The CPTs of $\mathrm{S}^{\mathrm{AV}}, \mathrm{S}^{\mathrm{HT}}$ and $\mathrm{S}^{\mathrm{IV}}$ are shown in Tables IX, X and XI, and other CPTs are omitted as they are set in similar way.

TABLE IX: CPT OF $\mathrm{P}\left(\mathrm{S}^{\mathrm{AV}} \mid \mathrm{S}^{\mathrm{AV}}, \mathrm{S}^{\mathrm{HT}}, \mathrm{S}^{\mathrm{IV}}\right)$.


TABLE X: CPT OF $\mathrm{P}\left(\mathrm{S}^{\mathrm{IV}} \mid \mathrm{D}, \mathrm{F}, \mathrm{B}\right)$.


TABLE XI: CPT OF $\mathrm{P}\left(\mathrm{S}^{\mathrm{HT}} \mid\right.$ MTC, ATC).


## E. Evaluation of the Proposed Approach

On the morning of June 14, 2006, the internal temperature of mixing tank and production unit started to increase in which the former has deviated from normal value at 9:16 AM while the later has deviated from normal value at 9:24 AM. The trend of observable variables for 60 minutes is illustrated in Fig. 8. These data can be interpreted as ground truth data to evaluate the proposed system's performance.
![img-8.jpeg](img-8.jpeg)

Fig. 8. The observable variables.
By assigning the primary probabilities into the DBN-based situational network, one minute after the start of period i.e. 9:01 AM, the probabilities of $\mathrm{S}^{\mathrm{AV}}$ consequences are calculated as shown in Table XII. As can be seen, the safe state is the most probable consequence of $\mathrm{S}^{\mathrm{AV}}$. The total loss of $\mathrm{S}^{\mathrm{AV}}$ i.e. its severity can be calculated by multiplication of the probabilities and losses of consequences which is about $\$ 2.56 \mathrm{E}+04$. The probability of $\mathrm{S}^{\mathrm{AV}}$ at that time is 0.05 , therefore the estimated risk level is 1.3 which means the current risk level of $\mathrm{S}^{\mathrm{AV}}$ is acceptable (A). It is worth noting that for situations $\mathrm{S}^{\mathrm{HT}}$ and $\mathrm{S}^{\mathrm{IV}}$, the accumulated vapor can be considered as their consequence which its degree of loss is about $\$ 1 \mathrm{E}+06$.

TABLE XII: THE CONSEQUENCES OF $\mathrm{S}^{\mathrm{AV}}$.


The observable variables get ready fuzzily using (13)-(16) as soft evidences every minute. By assigning the fuzzy soft evidences into the DBN-based situational network the posterior probabilities of the situations are updated during the period as shown in Fig. 9. As can be seen from the figure, the $\mathrm{S}^{\mathrm{HT}}$ situation is hazardous from minutes 16 to 31 and the situation $\mathrm{S}^{\mathrm{IV}}$ gets hazardous from minutes 24 to 28 as it was expected

due to observable variables. In parallel the risk estimation component shows that the risk level of $\mathrm{S}^{\mathrm{HT}}$ is 2.95 i.e. tolerable not acceptable (TNA) from minutes 16 to 31 , and the risk level of $\mathrm{S}^{\mathrm{IV}}$ is tolerable not acceptable (TNA) during minutes 24 to 28, as shown in Fig. 9. As it was assumed that the local and area ventilation systems have ability to evacuate the vapor, the risk level of $\mathrm{S}^{\mathrm{IV}}$ is acceptable (A) from minutes 17 to 25 , exactly before ventilation system malfunction, then its risk level has raised from minutes 25 and reached a peak at 3.1 which means it is not acceptable (NA).
![img-9.jpeg](img-9.jpeg)

Fig. 9. The posterior probabilities and risk levels of situations.
The system is set to make an alarm for every situation which has risk level more than 2.5 i.e. tolerable not acceptable (TNA). At 9:16 AM when the risk level of $\mathrm{S}^{\mathrm{HT}}$ raised the system shows that the most probable explanation is the failure of pneumatic unit (PU), but an inspection at 9:18 AM determined the valid performance of PU then with new evidence (success of PU) system showed that the failure of sensor is the most probable factor. This presents the system ability to support the operator to find the most probable explanation leading to an abnormal or hazardous state of a situation.

## V. CONCLUSION AND FUTURE WORK

This paper presented a fuzzy dynamic Bayesian networkbased situation assessment approach based on a fuzzy quantizer method, a DBN-based situational network and a fuzzy risk estimation method. As it was shown, the DBN-based situational network provides useful graphical models that meet the requirements for a practical SA system. The Bayesian probability framework facilitates the inclusion of background (prior) knowledge and the updating of this when new information is available from SCADA monitoring system. In addition, to generate the assessment, a fuzzy risk estimation method was developed to show the risk level of situations.

Today in many safety-critical systems such as chemical plants and nuclear power plants, the safety of system is supervised by several operators who are the members of a team. They have a particular goal to accomplish, they play a specific role in interacting with elements in the task environment and they have a limited amount of time to achieve the goal, so the future direction of the research is to extend the proposed system into a distributed system applying the team SA concept.
