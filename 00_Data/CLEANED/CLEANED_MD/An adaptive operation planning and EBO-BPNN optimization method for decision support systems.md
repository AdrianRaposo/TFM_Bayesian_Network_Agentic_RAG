# OPEN An adaptive operation planning and EBO-BPNN optimization method for decision support systems 

Yunxiao Liu ${ }^{1,4}$, Yiming Wang ${ }^{1,4}$, Han Li ${ }^{1,4,1,2}$, Guangyao Wang ${ }^{2}$ \& Jianliang $\mathrm{Ai}^{1}$<br>Formulating a course of action (COA) before a combat is crucial for operational command. Research in command and control (C2) artificial intelligence is currently focused on using intelligent auxiliary decision-making methods to implement COA. This paper proposes a COA planning method based on line of operation (LOO) and uses planning domain definition language (PDDL) to describe combat scenarios and COA. Following the effect-based optimization (EBO) principle, an effect evaluation model for COA was constructed, and dynamic bayesian networks (DBNs) was used to determine the reasoning and calculate the results of the effect evaluation network. To further improve the execution efficiency of the effect evaluation model in practical applications, the network was optimized through a back propagation neural network (BPNN). Relevant experiments based on the coordinated distributed air defense and anti-missile scenario were carried out using the LOO model to complete the planning of COA. A BPNN evaluation model based on the DBNs evaluation model was built. After training and finetuning, it achieved similar evaluation results, with a mean absolute percentage error (MAPE) of less than $0.02 \%$. Compared with the DBNs model, the BPNN model achieved an efficiency improvement of no less than $65 \%$, effectively reducing the consumption of computing resources. This research is the first time to realize the modeled description of COA planning, automatic evaluation, and calculation optimization of COA effects. It can support the development of decision support systems (DSS) and has the potential for practical application.

Automatic planning of COA is a typical application of DSS. DSS is widely used in various industrial scenarios that require fast and efficient decision-making ${ }^{1-3}$. The development of DSS capable of tactical-level COA planning represents a current research focus within the C2 domain. Tactical commanders' command and decision-making process often face highly complex and contentious battlefield situations. Giving full play to the advantages of COA intelligent planning in tactical planning will play an essential role in promoting crossdomain joint combat operation command.

The COA approach converts the commander's intention into a specific combat action plan. In recent years, with the increasing use of artificial intelligence technology in combat decision-making, developing combat DSS with intelligent COA planning and optimization has become a crucial focus in C2 intelligence. COA optimization is the optimization process of feasible combat action plans. In tactical planning, COA optimization aims to find the most effective and workable action plan to achieve mission objectives to the greatest extent and ultimately achieve the best combat effect under limited resources. Using machine learning algorithms to solve optimization problems in combat action planning can achieve scene adaptation, data-driven intelligent decision-making and computing resource optimization, thereby improving the decision-making speed and tactical flexibility of the combat auxiliary DSS. Using machine learning algorithms to achieve COA optimization is a critical technology that urgently needs breakthroughs in intelligent combat decision-making ${ }^{4}$.

In recent years, relevant COA planning and optimization research has focused on modelling process research based on rules ${ }^{5}$, probabilistic networks, or classic planning-solving algorithms. Wang et al. ${ }^{6}$ proposed an intelligent planning method for combat missions based on probability graphs. This method determines the causal relationship between tasks through statistical analysis, uses Graph Neural Networks (GNN) to extract critical events in the task to construct a probability map, and then calculates the mission planning solution or the probability of success. He et al. ${ }^{7}$ proposed a model based on heterogeneous networks to represent the

[^0]
[^0]:    ${ }^{1}$ Department of Aeronautics and Astronautics, Fudan University, Shanghai 200433, China. ${ }^{2}$ Shenyang Aircraft Design and Research Institute, Shenyang 110035, China. ${ }^{4}$ These authors contributed equally: Yunxiao Liu, Yiming Wang and Han Li. ${ }^{1,2}$ email: hanli20@fudan.edu.cn

relationships among various elements and to generate COA by decomposing combat tasks. It provides auxiliary control and offers network-based information to the commander. This method provides conditional support for command and decision-making. Marques et al.^{8} proposed an ontology-based COA planning method. The core of this work is to solve and generate combat actions based on hierarchical network planning technology. Bayesian networks can convert dynamic decision-making problems into probabilistic inference problems, and many recent studies have been carried out on this. Pang et al^{9}. proposed a Role-based Bayesian decision framework for autonomous unmanned systems. This framework can realize situation awareness based on multi-entity Bayesian networks to describe action scenarios and uncertainties semantically. It was verified through virtual mission scenarios, and the application of Bayesian networks in situation awareness was explored. Kim et al.^{10} proposed a situational awareness model based on DBN, which can quantify the uncertainty in the battlefield and then predict the enemy's intentions. They also further studied the interaction between the predicted enemy intentions and COA. Several COA effect evaluation methods based on Wargaming have been proposed regarding COA optimization. Yuksek et al.^{11} implemented a high-precision intelligent wargaming method to implement COA analysis, which was verified by the simulation. The simulation environment includes a grid-world representation of the operation area, performance models of military units and combat models. DeBerry et al.^{12} proposed a wargaming commodity COA automated method under uncertainty, which models a wargame scenario as a stochastic multi-commodity flow problem and produces an optimal COA that minimizes risk when the enemy force amounts are unknown. This method can help commanders observe the Correlation between COA success rate and risk to help evaluate COA. The above research content provides a theoretical and practical basis for COA intelligent planning. However, traditional COA planning methods based on rules or probabilistic networks may bring specific challenges in developing and applying intelligent combat auxiliary DSS. It is difficult to adapt to highly dynamic saturation attack combat scenarios. The main reason is that in the execution process of reasoning methods based on rules or probabilistic networks, there may be a surge in computational complexity caused by the rapid expansion of the network, which significantly affects the optimization efficiency of COA development.

In 2021, the Rand Corporation report on machine learning assisted command and control decision-making^{13}. The report summarized representative classic and modern artificial intelligence algorithms. It divides intelligent auxiliary decision-making tasks into planning, classification and reaction. The applicability of various typical artificial intelligence algorithms for different decision-making tasks is analyzed. In 2023, the Causal Adaptive Combat Decision Assistance System (CADA) research report proposed the causal concept of using machine learning algorithms to carry out intelligent generation and recommendation of COA. A combat auxiliary decision-making method was explored based on causal feature learning and domain expertise display. Therefore, in the defence industry, DSS that can realize the intelligent generation of COA has application requirements. The research proposed in this paper is precisely to solve the critical issues in the application process.

The paper makes the following main contributions:We propose an adaptive COA planning method based on the LOO model. To define the inputs of the model, decision areas, decision points, and specific elements related to the combat operation, PDDL was used according to the execution logic and constraints of the combat operation. This method accurately enables the adaptive description of the COA planning process and its necessary elements.Based on the LOO model, a DBNs effect evaluation network was created using the EBO theory, and a systematic evaluation method for COA was established. This method constructs an interpretable and inferential effect evaluation model, which represents the action and effect nodes and the influence relationships between nodes in the evaluation networks.Based on the DBNs evaluation method, the EBO-BPNN evaluation model was proposed. A BPNN evaluation model was established to optimize the calculation efficiency of the COA optimization process.As described above, a coordinated distributed air defense and the anti-missile scenario were created to test the method's effectiveness. The scenario modelling and COA planning process were completed, and optional COAs were effectively generated. Subsequently, the EBO-BPNN evaluation method for COAs proposed in this paper was experimentally verified.

## LOO-based COA generation method

The process of planning a COA is typically divided into three categories based on the driving factors of the generation process: Threat-Based Planning (TBP), Capability-Based Planning (CBP) and Scenario-Based Planning (SBP). There have been many research results in this field. Planning a COA can provide a feasible sequence of actions for the current battlefield situation. COA optimization extends the COA planning link in the intelligent tactical planning auxiliary decision-making process. The core content of COA optimization is to analyze and select the optimal COA from this set.

## Modeling of COA planning and optimization

After analysis, it was found that at the tactical level COA planning level, the TBP planning method^{14} is usually used to drive the generation of our COA by clarifying the centre of gravity (COG), the enemy's combat capabilities, and our feasible methods to deal with the enemy's combat capabilities^{7,15}. The premise of COA planning is to realize the intelligent generation of COA reasonably and accurately. The JP 5-0 outline comprehensively analyzes the relevant elements that may be involved in the COA planning and optimization process. It describes the action planning process with COA generation and optimization as the main content. This paper references the action planning process in JP 5-0. It fully considers the interface and input and output issues involved in the design and development process of the intelligent tactical auxiliary decision-making system. The implementation process is shown in Fig. 1.

![img-0.jpeg](img-0.jpeg)

Fig. 1. The process of intelligent tactical auxiliary decision-making implementation.

Among them, this paper divides the implementation of intelligent tactical decision-making into six steps: (a) threat assessment, (b) intent analysis, (c) COG analysis, (d) mission analysis, (e) COA planning, (f) COA optimization. By running the functions (a) to (d), the necessary elements required for COA planning can be obtained. That is the enemy target group and threat assessment results, the enemy target group intention, our combat focus and our combat missions. The preorder process in implementing intelligent tactical auxiliary decision-making can output the necessary input required for the COA planning process.

## Modeling and implementation of LOO method

As shown in Fig. 2, this paper proposes a COA planning framework based on the LOO model, which explains the COA planning logical operation process and core elements.

This framework implements the COA planning method based on TBP, and our combat focus serves as an essential input to the framework. It also clarified the enemy targets that must be attacked or intercepted under the current battlefield. Our operational COG is based on the analytic hierarchy process, which fully integrates the results of the enemy's threat ranking and intentions. This framework constructs a COA planning method based on our combat resources and combat areas for our combat COG. The LOO model is the critical driving means for COA planning, which can realize dynamic and feasible kill chain and assessment chain. The reconstruction under the guidance of the theoretical framework of F2T2EA (Find, Fix, Track, Target, Engage, Assess), a coordinated, integrated kill-web^{16,17} can be constructed, giving full play to the advantages of tactical flexibility in coordinated combat scenarios.

To build a coordinated, integrated kill net based on LOO, it is first necessary to clearly define the COG, decision-making area, combat resources, mission, decisive condition (DC), DC points, effects, actions and other elements and application processes in the process of building the operation line. Considering the diverse characteristics of the tactical decision-making process in different combat scenarios and the general need for generated models, the use of PDDL can define the key elements and relationships required in building combat lines^{18}. Thus, PDDL has been widely used in intelligent planning to form an updateable domain knowledge file^{19}.

![img-1.jpeg](img-1.jpeg)

Fig. 2. COA generation framework driven by the LOO model.

# Phase 1: clarify and get external input 

Construct the external input entity after obtaining the COG, decision area, combat resources, and tasks processed by the external module.

## Phase 2: decision area and decision point generation

The entire battlefield area is divided into different decision-making areas. Decision points define the boundaries of the decision area. Each combat unit or formation can perform corresponding actions by tactical rules in different areas.

```
(define (domain planning _ input)
    (:objects
    ? \(\operatorname{cog}-\operatorname{COG}\)
    ? region - decision _ region
    ? decision _ point - decision _ point
    ? resource - combat _ resource
    ? task - mission _ task
    )
    (:types
    COG decision _ region decision _ point combat _ resource mission _ task
    )
    (:predicates
    (target - of ?c - COG ?r - combat _ resource)
    (task - target ?t - mission _ task ?c - COG)
    (task - in - region ?t - mission _ task ?r - decision _ region)
    (at - decision - point ?r - decision _ region ?dp - decision _ point)
    )
    (:init
    (target - of ?cog ?resource)
    (task - target ?task ?cog)
    (task - in - region ?task ?region)
    (at - decision - point ?region ?decision)
    )
```

Algorithm 1. Definition of phase 1 and 2

External input elements are defined as "objects", the object type is clarified with "types", and the relationship, attributes, or conditions between objects are represented with the predicate "predicates". The initial state is defined with "init".

# Phase3 determination of DC and DC point 

DC is a combination of combat action effects that, when achieved, will give the commander a significant advantage over an opponent or contribute significantly to achieving combat objectives. The DC point corresponds to the critical point for completing a tactical action goal. In applying the LOO model for intelligent tactical planning, it is first necessary to determine the goals and objectives of combat operations based on the COG. Moreover, based on this, the corresponding decisive conditions and the DC point at which the DCs are completed and established.

## Phase 4: generation of actions, effects and feasible actions

The effect is an identifiable change in an operational process or physical state caused by one or more actionable actions. The operational line connects the DCs to achieving operational objectives and the effects impact the completion of the DCs. The key to implementing the LOO model is determining the sequence and influence relationship of feasible actions, effects and DCs.

```
(define (domain line _ of _ operation)
    (:objects
    ? \(\operatorname{cog}-\operatorname{COG}\)
    ? task - mission _ task
    ? \(u\) - unit
    ? \(a\) - action
    ? \(e\) - effect
    ? dc - decisive _ condition
    ? \(d c p-d c \_\)point
    )
    (:types
    COG unit mission _ task action effect decisive _ condition dc _ point
    )
    (:predicates
    ((achieves - COG ?c - COG ?dc - decisive _ condition))
    (drives - dc ?a - action ?e - effect ?dc - decisive _ condition)
    (achieves - dcp ?dc - decisive _ condition ?dcp - dc _ point))
    (composes - task ?mission _ task ?action - action)
    (has - effect ?a - action ?e - effect)
    (action - end ?a - action ?dcp - dc _ point)
    )
)
```

Algorithm 2. Definition of phase 3 and 4


Fig. 3. Tactical level COA standard format for combat formations.
![img-2.jpeg](img-2.jpeg)

Fig. 4. The structure of DBNs.

The key points and object processing logic flow when applying the LOO model are described through predicates composed of "achieves, drives, composes, has, and action-end". When using PDDL to represent a tactical planning instance, it can be described as a two-tuple:

$$
D=\{\text { planning_input, line_of_operation }\}
$$

Among them, "planning _ input" is the external input domain knowledge description file, and "line _ of _ operation" is the planning process description file under the current combat mission. Combat scenarios and planning models can be modularized by simply predefining different description files.

# Phase 5: obtain a feasible COA that complies with tactical rules 

After completing phases 1 to 4 , the COAs based on combat formations and divided into time segments can be obtained according to the constraints of the tactical planning process. These optional COAs need to be further optimized. Figure 3 shows the standard style of a COA.

## Effect-based optimization of COA

In most cases, the COA planning method based on the LOO model can obtain several alternative COAs that comply with tactical rules based on the battlefield situation and available combat resources. Each optional COA has different advantages and disadvantages, and COA optimization helps to comprehensively understand each COA and determine the best $\mathrm{COA}^{20}$. At the level of COA optimization implementation based on $\mathrm{EBO}^{8}$, there are mainly methods such as DBNs ${ }^{21,22}$, genetic algorithm ${ }^{23}$, and probability graphs ${ }^{6}$. The above methods have advantages in the interpretability of combat operations and their effects. Combined with the assessment of impact probability by C2 experts, a more accurate prior probability of inference can be obtained, which lays a good foundation for achieving highly robust combat auxiliary decision-making. However, it also has the disadvantages of high computational complexity and slow convergence speed, so optimizing this problem is crucial.

This paper fully uses the advantages of DBNs in the interpretability of reasoning logic to model the effect chain of the LOO model. Combined with the action-effect conditional probability evaluated by experts, the effect inference results of a single COA are generated, and a training sample data set necessary for the machine learning optimization algorithm is established.

## Construction of COA effect evaluation model

A complete optional COA can be obtained based on the LOO model. At the same time, the effect evaluation chain of each operation line can be obtained. Multiple effect evaluation chains can be aggregated to form an

![img-3.jpeg](img-3.jpeg)

**Fig. 5.** COA effect evaluation network based on DBNs.

effect evaluation network[^24]. The effect evaluation network's construction process is divided into three steps: network node identification, impact relationship analysis, and determining impact intensity.

### **Phase 1: effect evaluation network node identification**

The construction of the effect evaluation network requires first clarifying which nodes it consists of. According to the LOO model designed in this paper, actions, direct effects produced by actions, intermediate effects, DC point effects, and COA evaluation results are used as five types of nodes in the effect evaluation network. Therefore, type 5 nodes can be described as the following five-tuple:

$$
\mathcal{N} = \{\mathcal{N}_a, \mathcal{N}_c, \mathcal{N}_{me}, \mathcal{N}_{dc}, \mathcal{N}_{coa}\} \tag{2}
$$

where, $\mathcal{N}_a$ is the action node-set, which represents several actions that the combat node may perform; $\mathcal{N}_c$ represents the action-effect node-set, which expresses the direct effects produced by the combat node after executing the combat action; $\mathcal{N}_{me}$ represents the intermediate effect set, which cannot be directly observed. The indirect effect; $\mathcal{N}_{dc}$ represents the DC point effect-set, which is the final effect-set of the execution of a series of combat operations in a critical area or time segment. $\mathcal{N}_{coa}$ represents the effect evaluation node set of the complete COA.

### **Phase 2: effect evaluation network relationship analysis**

After determining the nodes in the effect evaluation network through the above steps, further determining the influence relationship between the nodes is necessary. The connection relationship between the five types of nodes can be described as the following five-tuple:

$$
\mathcal{R} = \{\mathcal{R}_{ac}, \mathcal{R}_{cme}, \mathcal{R}_{medc}, \mathcal{R}_{dcdc}, \mathcal{R}_{coa}\} \tag{3}
$$

where, $\mathcal{R}_{ac}$ defines the set of connecting relationships from action nodes to action-effect nodes. For any $n_b \in \mathcal{N}_b$, there exists $n_a \in \mathcal{N}_a$ that satisfies $\langle n_a, n_b \rangle \in \mathcal{R}_{ac}$:

$$
\mathcal{R}_{ac} \subseteq \{\langle n_a, n_b \rangle \mid n_a \in \mathcal{N}_a \land n_b \in \mathcal{N}_c\} \tag{4}
$$

$\mathcal{R}_{cme}$ is a collection of connecting relationships between action-effect and intermediate effect nodes. It describes the influence of action effects on intermediate effects. The intermediate effect may be affected by multiple action-effect nodes simultaneously, satisfying:

$$
\mathcal{R}_{cme} \subseteq \{\langle n_c, n_d \rangle \mid n_c \in \mathcal{N}_c \land n_d \in \mathcal{N}_{me}\} \tag{5}
$$

$\mathcal{R}_{medc}$ is the set of relationships connecting intermediate effect nodes and DC points. It describes the impact of intermediate effects on DC point effects and satisfies:

$$
\mathcal{R}_{medc} \subseteq \{\langle n_c, n_f \rangle \mid n_c \in \mathcal{N}_{me} \land n_f \in \mathcal{N}_{dc}\} \tag{6}
$$

$\mathcal{R}_{dcdc}$ is the set of connecting relationships between different DC points. It describes the impact of the DC point effects and satisfies:

$$
\mathcal{R}_{dcdc} \subseteq \{\langle n_d, n_f \rangle \mid n_d \in \mathcal{N}_{medc} \land n_d \in \mathcal{N}_{dc}\} \tag{7}
$$

$$
\boldsymbol{R}_{\mathrm{ccs}} \subseteq\left\{\left\langle n_{g}, n_{h}\right\rangle \mid n_{g} \in \boldsymbol{N}_{d c} \wedge n_{h} \in \boldsymbol{N}_{d c} \wedge n_{g} \neq n_{h}\right\}
$$

$\boldsymbol{R}_{\text {cos }}$ represents the connecting relationships between DC points and COA effect evaluation nodes. It describes the influence relationship of multiple DC points on the final effect evaluation of COA and satisfies the following:

$$
\boldsymbol{R}_{\mathrm{cos}} \subseteq\left\{\left\langle n_{i}, n_{j}\right\rangle \mid n_{i} \in \boldsymbol{N}_{d c} \wedge n_{j} \in \boldsymbol{N}_{\mathrm{cos}}\right\}
$$

# Phase 3: determine the intensity of the impact 

Impact intensity refers to the degree of influence of the intensity change of the parent node on the child nodes. The prior and baseline probability are used as the impact intensity parameters. The prior probability refers to the execution probability of the combat operation at the initial moment. The base probability is the probability that an effect node achieves the expected effect when taking action. The impact intensity is described as follows:

$$
S=\left\{S_{a}, S_{c}\right\}
$$

$S_{a}$ represents the intensity of the direct effect produced by the implementation of combat operations on the combat target, and $S_{c}$ represents the intensity of the intermediate effect on the DC point. They can usually be calculated based on the preset values of C 2 command experts.

## COA effect calculation based on DBNs

DBNs is developed based on bayesian network (BN) and belongs to the category of probability graphical model. DBNs add event sequence data or variables that evolve to BN, allowing the modelling of relationships that change over time. The COA effect evaluation network can be modelled and implemented through DBNs, and the DBNs can infer the evaluation results for COA. BN is a directed acyclic graph, represented by $G=(V, E)$, where $V$ and $E$ are the node set and the relationship set connecting the nodes. DBNs can be decomposed into a static BN and a time transfer network, defined as $\left(B_{0}, B_{2 i}\right) . B_{0}$ represents the static BN at the initial moment, and $B_{2 i l}$ represents the BN, including two adjacent time slices. The joint probability of the static BN at the initial moment is defined as $P\left(x_{0}\right)$, and the dynamic variable set of the DBNs is defined as $X=\left\{X^{1}, X^{2}, \ldots X^{n}\right\}$. Among them, $X_{t}^{i}$ represents the state of the corresponding variable $X^{i}$ at time $t$, and $\pi\left(X_{t}^{i}\right)=\left\{\mathbb{N}_{t-1}, P a^{j}(X)\right\}(j=1,2, \cdots, N-1)$ is the set of parent nodes of $X_{t}^{i} . P\left(X_{t} \mid X_{t-1}\right)$ is used to describe the transition probability of a node from $t-1$ to $t$, which can be obtained:

$$
\begin{aligned}
P\left(X_{t}^{i} \mid X_{t-1}^{i}\right) & =\prod_{j=1}^{n} P\left[X_{t}^{i}, \pi\left(X_{t}^{i}\right)\right] \\
& =P\left[X_{t}^{i} \mid X_{t-1}^{i}, P a^{1}\left(X_{t}^{i}\right), \cdots, P a^{N-1}\left(X_{t}^{i}\right)\right] \cdot P\left(X_{t-1}^{i}\right) \prod_{j=1}^{N-1} P\left[P a^{j}\left(X_{t}^{i}\right)\right]
\end{aligned}
$$

The joint probability calculation of DBNs can be realized by tracking the time series ${ }^{24}$. Assuming that $T$ represents the length of the time series, the joint probability at time $T$ can be obtained:

$$
P\left(X_{T} \mid X_{0}\right)=\prod_{t=1}^{T} P\left(X_{t} \mid X_{t-1}\right)
$$

Figure 4 shows the DBNs structure expanded by time slices. The solid lines connect the directed dependencies in the static BN, and the dotted lines connect the probability transfer relationships of nodes between time slices. The joint probability of DBNs can be obtained from (11) distributed.

Based on the joint probability evaluation and comparison of DBNs, the combat effectiveness assessment of different COAs can be realized. As shown in Fig. 5, the COAs effect evaluation model based on DBNs is driven by the LOO model. The effect evaluation network covers action nodes, action-effect nodes, intermediate effect nodes, DC point effect nodes and COA evaluation result nodes, represented by $a_{t}^{i}, e_{t}^{i}, m e_{t}^{i}, d e_{t}^{i}$ and $c o a_{n}$ respectively. Among them, the action-effect node may be composed of two parts in the actual application process: the direct effect of our actions and the impact of the enemy's actions and changes on our actions to achieve a more comprehensive COA adversarial assessment. The probability calculation process of each node can be expressed as:

$$
\begin{gathered}
P\left(e_{t}^{j}\right)=P\left(e_{t}^{j} \mid e_{t-1}^{j}, a_{t}^{1}, \cdots, a_{t}^{j}\right) \cdot P\left(e_{t-1}^{j}\right) \prod_{i=1}^{t} P\left(a_{t}^{i}\right) \\
P\left(m e_{t}^{i}\right)=P\left(m e_{t}^{i_{i}} \mid m e_{t-1}^{i}, e_{t}^{1}, \cdots, e_{t}^{j}\right) \cdot P\left(m e_{t-1}^{i_{i}}\right) \prod_{j=1}^{t} P\left(e_{t}^{j}\right)
\end{gathered}
$$

In applying DBNs to realize COA evaluation, the inference calculation of the joint probability of COA evaluation can be realized by dynamically adjusting the node structure and related node probability values according to the preset expert rules or conditional probabilities for each node.

# COA optimization method based on EBO-BPNN COA optimization process based on EBO-BPNN 

Applying DBNs can realize the effect evaluation of COA. However, in the actual application process, the computing performance requirements are high when the number of DBNs nodes is enormous. By applying machine learning algorithms combined with model pretraining based on DBNs inference, the performance improvement of the COA optimization model can be better achieved. Some scholars have carried out relevant research on the application of machine learning algorithms in the field of intelligent decision-making. BPNN is a typical supervised learning algorithm in machine learning ${ }^{25}$. It uses the back-propagation algorithm to train the network and establish the mapping relationship between input data and output. BPNN can learn complex nonlinear relationships and is suitable for processing such as DBNs data migration and optimization calculations in the COA optimization process. It has good fitting ability and flexibility and can be applied to COA effect evaluation. The COA optimization process based on BPNN is divided into three phases, as shown in Fig. 6.

## Phase 1: construction of the training dataset

Before constructing the EBO-BPNN model, it is necessary first to construct a training dataset through the COA effect evaluation model based on DBNs. First, determine the enemy's target in the current combat scenario, the upper limit of our available resources, and the possible enemy actions. Then, we will use the LOO model to create feasible COAs for our formation and use DBNs for evaluation. As a result, a sufficient training dataset is obtained. The input of the training dataset is our COA and the enemy's action, and the output is the evaluation result of COA using DBNs.

## Phase 2: development of the EBO-BPNN model

Create an EBO-BPNN model. The input of the model is the combat actions of our side and the enemy, and the output is the evaluation result of the effectiveness of our actions. The training dataset generated in phase 1 is used as the learning process input and output of the neural network model, and the network parameters are continuously adjusted to achieve model tuning that can meet accuracy requirements.

## Phase 3: application of the EBO-BPNN model

After training and tuning the EBO-BPNN model, the model is deployed and used. The LOO model creates COAs during the application stage based on the current combat situation. The actions of the own and the enemy are then input into the EBO-BPNN model, which allows for the quick determination of the impact of COAs, thus aiding in making efficient decisions.
![img-4.jpeg](img-4.jpeg)

Fig. 6. COA optimization implementation process based on BPNN.

# Application of EBO-BPNN in COA optimization process 

## Basic principles of BPNN

BPNN is a neural network algorithm with signal feedforward propagation and error back-propagation. In the signal feedforward propagation stage, the input signal is transmitted from the first hidden layer to the output layer, and the output signal is generated at the output layer. If the actual output is inconsistent with the expected output, the algorithm enters the error back-propagation stage. The error is propagated back from the output layer to the first hidden layer and distributed to all units in each layer. The network learning process is realized through continuous forward propagation and reverse adjustment, and the weights between neurons are continuously revised until the network output error meets the accuracy requirements ${ }^{26}$. This paper uses a BPNN with two hidden layers to analyze its principle. The network structure is shown in Fig. 7.

Among them, let the number of signals contained in the input layer be $h$, and use $o$ as the symbol of any neuron. The first hidden layer contains $l$ neurons, and $p$ represents any neuron. The output layer has $n$ output neurons, and $r$ represents any neuron. $v_{\mathrm{qp}}(p=1,2, \ldots, l \mid q=1,2, \ldots, m)$ represents the weight between the input and first hidden layers, and $w_{r q}(q=1,2, \ldots, m \mid r=1,2, \ldots, n)$ represents the weight between the second and output layers. The input and output of the first hidden layer are represented by layer $_{1} i n_{p}(p=1,2, \ldots, l)$ and $x_{p}(p=1,2, \ldots, l)$, respectively, and the activation function is represented by $f(\cdot)$. layer $_{2} i n_{e}(q=1,2, \ldots, m)$ and $y_{q}(q=1,2, \ldots, m)$ represent the input and output of the second hidden layer, and the activation function is represented by $g(\cdot)$ . The input and output of the output layer are represented by layer $_{3} i n_{r}(r=1,2, \ldots, n)$ and $z_{r}(r=1,2, \ldots, n)$ , respectively, and the activation function is represented by $h(\cdot)$. The training data set is represented by $\boldsymbol{T}=\left[T_{1}, T_{2}, \ldots, T_{n}, \ldots, T_{i}\right]$, and any sample can be represented by $\boldsymbol{T}_{\boldsymbol{a}}=\left[t_{1 a}, t_{1 a}, t_{2 a}, \ldots, t_{2 a}\right]^{\mathrm{T}}(a=1,2, \ldots, Z)$.

The actual output and expected output during the neural network operation are represented by $\boldsymbol{z}_{\boldsymbol{a}}=\left[z_{1 a}, z_{2 a}, \ldots, z_{n a}\right]^{\mathrm{T}}$ and $\boldsymbol{d}_{\boldsymbol{a}}=\left[d_{1 a}, d_{2 a}, \ldots, d_{n a}\right]^{\mathrm{T}}$, respectively. The network weight and output are num functions when num is the number of iterations. According to the feedforward propagation process of the input signal, assuming that the input training sample is $\boldsymbol{T}_{\boldsymbol{a}}$, then have

$$
\begin{gathered}
\text { layer }_{1} i n_{p a}=\sum_{a=1}^{h} u_{p a} t_{a a} \\
x_{p a}=f\left(\text { layer }_{1} i n_{p a}\right)=f\left(\sum_{\alpha=1}^{h} u_{p \alpha} t_{\alpha a}\right) \\
\text { layer }_{2} i n_{q a}=\sum_{p=1}^{l} v_{q p} x_{p a} \\
y_{q a}=g\left(\text { layer }_{2} i n_{q a}\right)=g\left(\sum_{p=1}^{l} v_{q p} x_{p a}\right)
\end{gathered}
$$

![img-5.jpeg](img-5.jpeg)

Fig. 7. BPNN structure.

$$
\begin{gathered}
\operatorname{layer}_{3} i n_{r a}=\sum_{q=1}^{m} w_{r q} y_{q a} \\
z_{r a}=h\left(\operatorname{layer}_{3} i n_{r a}\right)=h\left(\sum_{q=1}^{m} w_{r q} y_{q a}\right)
\end{gathered}
$$

The matrix form of the above formulas is expressed as follows:

$$
\begin{gathered}
\operatorname{layer}_{1} i n_{a}=\boldsymbol{U} \boldsymbol{T}_{\boldsymbol{a}} \quad \boldsymbol{U}=\left[u_{p a}\right]_{l \times h}, \boldsymbol{T}_{\boldsymbol{a}}=\left[t_{o a}\right]_{h \times 1} \\
\boldsymbol{X}_{\boldsymbol{a}}=f\left(\text { layer }_{1} i n_{a}\right)=f\left(\boldsymbol{U} \boldsymbol{T}_{\boldsymbol{a}}\right)=\left[x_{p a}\right]_{l \times 1} \\
\text { layer }_{2} i n_{a}=\boldsymbol{V} \boldsymbol{X}_{\boldsymbol{a}} \quad \boldsymbol{V}=\left[v_{q p}\right]_{m \times l}, \boldsymbol{X}_{\boldsymbol{a}}=\left[x_{p a}\right]_{l \times 1} \\
\boldsymbol{Y}_{a}=g\left(\text { layer }_{2} i n_{a}\right)=g\left(\boldsymbol{V} \boldsymbol{X}_{a}\right)=\left[y_{q a}\right]_{m \times 1} \\
\text { layer }_{3} i n_{a}=\boldsymbol{W} \boldsymbol{Y}_{\boldsymbol{a}} \quad \boldsymbol{W}=\left[w_{r q}\right]_{n \times m}, \boldsymbol{Y}=\left[y_{q a}\right]_{m \times 1} \\
\boldsymbol{Z}_{a}=h\left(\text { layer }_{3} i n_{a}\right)=h\left(\boldsymbol{W} \boldsymbol{Y}_{a}\right)=\left[z_{r a}\right]_{n \times 1}
\end{gathered}
$$

The $r$-th neuron of the output layer neuron it satisfies the following:

$$
\operatorname{err}_{r a}(n u m)=d_{r a}(n u m)-z_{r a}(n u m)
$$

$\operatorname{err}_{r a}^{2}(n u m) / 2$ is defined as the error energy of the $r$-th neuron, and the sum of the error energy of all neurons in the output layer is defined as $E_{a}(n u m)$, then:

$$
E_{a}(n u m)=\frac{1}{2} \sum_{r=1}^{n} \operatorname{err}_{r a}^{2}(n u m)
$$

The error signal is the difference between the network output and the desired output. This error signal will be passed from the output to the first hidden layer. This process is called the feedforward propagation stage of the error signal. The network's weights and biases are adjusted at this stage through error feedback. The actual network output gradually approaches the expected output by repeatedly modifying the weights and biases. The calculation process of the error feedforward propagation stage is as follows:

$$
\begin{aligned}
\Delta w_{r q}(n u m)= & -\eta \frac{\partial E_{a}(n u m)}{\partial w_{r q}(n u m)} \\
= & -\eta \sum_{r=1}^{n} \frac{\partial\left[d_{r a}(n u m)-z_{r a}(n u m)\right]^{2} / 2}{\partial z_{r a}(n u m)} \cdot \frac{\partial z_{r a}(n u m)}{\partial \text { layer }_{3} i n_{r a}(n u m)} \frac{\partial \text { layer }_{3} i n_{r a}(n u m)}{\partial w_{r q}(n u m)} \\
= & \eta \sum_{r=1}^{n}\left[d_{r a}(n u m)-z_{r a}(n u m)\right] \cdot h^{\prime}\left[\text { layer }_{3} i n_{r a}(n u m)\right] y_{q a}(n u m) \\
& \quad w_{r q}(n u m+1)=w_{r q}(n u m)+\Delta w_{r q}(n u m) \\
\Delta v_{q p}(n u m)= & -\eta \frac{\partial E_{a}(n u m)}{\partial v_{q p}(n u m)} \\
= & -\eta \sum_{r=1}^{n} \frac{\partial\left[d_{r a}(n u m)-z_{r a}(n u m)\right]^{2} / 2}{\partial z_{r a}(n u m)} \cdot \frac{\partial z_{r a}(n u m)}{\partial \text { layer }_{3} i n_{r a}(n u m)} \frac{\partial \text { layer }_{3} i n_{r a}(n u m)}{\partial y_{q a}(n u m)} \\
& \frac{\partial y_{q a}(n u m)}{\partial \text { layer }_{2} i n_{q a}(n u m)} \frac{\partial \text { layer }_{2} i n_{q a}(n u m)}{\partial v_{q p}(n u m)} \\
= & \eta \sum_{r=1}^{n}\left[d_{r a}(n u m)-z_{r a}(n u m)\right] \cdot h^{\prime}\left[\text { layer }_{3} i n_{r a}(n u m)\right] w_{r a}(n u m) \\
& \cdot g^{\prime}\left[\text { layer }_{2} i n_{q a}(n u m)\right] x_{p a}(n u m) \\
& \quad v_{q p}(n u m+1)=v_{q p}(n u m)+\Delta v_{q p}(n u m)
\end{aligned}
$$

$$
\begin{aligned}
\Delta u_{p o}(n u m)= & -\eta \frac{\partial E_{a}(n u m)}{\partial u_{p p}(n u m)} \\
= & -\eta \sum_{r=1}^{n} \frac{\partial\left[d_{r a}(n u m)-z_{r a}(n u m)\right]^{2} / 2}{\partial z_{r a}(n u m)} \cdot \frac{\partial z_{r a}(n u m)}{\partial l a y e r_{3} i n_{r a}(n u m)} \frac{\partial l a y e r_{3} i n_{r a}(n u m)}{\partial y_{q o}(n u m)} \\
& \cdot \frac{\partial y_{q o}(n u m)}{\partial l a y e r_{2} i n_{q o}(n u m)} \frac{\partial l a y e r_{2} i n_{q o}(m \iota m)}{\partial x_{p o}(n u m)} \cdot \frac{\partial x_{p o}(n u m)}{\partial l a y e r_{1} i n_{p o}(n u m)} \frac{\partial l a y e r_{1} i n_{p o}(n u m)}{\partial u_{p o}(n u m)} \\
= & \eta \sum_{r=1}^{n}\left[d_{r a}(n u m)-z_{r a}(n u m)\right] \cdot h^{t}\left[l a y e r_{3} i n_{r a}(n u m)\right] w_{r a}(n u m) \\
& \cdot g^{t}\left[l a y e r_{2} i n_{q o}(n u m)\right] v_{q o}(n u m) \cdot f^{t}\left[l a y e r_{1} i n_{p o}(m u m)\right] t_{o n} \\
& u_{p o}(n u m+1)=u_{p o}(n u m)+\Delta u_{p o}(n u m)
\end{aligned}
$$

The matrix form of the above process is as follows:

$$
\begin{gathered}
\boldsymbol{\Delta} \boldsymbol{W}_{\boldsymbol{a}}(n u m)=-\eta \frac{\partial E_{a}(n u m)}{\partial \boldsymbol{W}_{\boldsymbol{a}}(\boldsymbol{n u m})} \\
\boldsymbol{W}_{\boldsymbol{a}}(n u m+1)=\boldsymbol{W}_{\boldsymbol{a}}(n u m)+\boldsymbol{\Delta} \boldsymbol{W}_{\boldsymbol{a}}(n u m) \\
\boldsymbol{\Delta} \boldsymbol{V}_{\boldsymbol{a}}(n u m)=-\eta \frac{\partial E_{a}(n u m)}{\partial \boldsymbol{V}_{\boldsymbol{a}}(n u m)} \\
\boldsymbol{V}_{\boldsymbol{a}}(n u m+1)=\boldsymbol{V}_{\boldsymbol{a}}(n u m)+\boldsymbol{\Delta} \boldsymbol{V}_{\boldsymbol{a}}(n u m) \\
\boldsymbol{\Delta} \boldsymbol{U}_{\boldsymbol{a}}(n u m)=-\eta \frac{\partial E_{a}(n u m)}{\partial \boldsymbol{U}_{\boldsymbol{a}}(n u m)} \\
\boldsymbol{U}_{\boldsymbol{a}}(n u m+1)=\boldsymbol{U}_{\boldsymbol{a}}(n u m)+\boldsymbol{\Delta} \boldsymbol{U}_{\boldsymbol{a}}(n u m)
\end{gathered}
$$

Where $\eta$ is the learning rate that exists as a given constant, BPNN has completed the feedforward propagation and reverse adjustment process. This process is an iteration. BPNN needs to go through multiple iterations to converge the learning error to the preset accuracy.

# Construction of EBO-BPNN in COA optimization 

To optimize and evaluate COA using BPNN, it is necessary to first identify the input and output parameters of the network. When using DBNs to evaluate COA, the focus is primarily on the impact of combat formation actions on DC. Therefore, the input for the EBO-BPNN model consists of COA for all combat formations in the combat area, with the probability of DC impact on a specific COG being used as the network output. Based on the current battlefield situation, we have developed a comprehensive EBO-BPNN evaluation model for each COG to assess its potential impact. The final outcome of the EBO-BPNN is determined by the collective evaluation of all targets. Our objective is to select the most effective COA through optimization.

## Application case analysis

## Application and combat scenario design

To test the LOO planning model and EBO-BPNN evaluation method, we propose and verify a coordinated distributed air defense and anti-missile scenario ${ }^{27-29}$. In Fig. 8, the battlefield is divided into four decision areas, with the Vessel positioned at the center of areas. Red icons represent our combat formations, while blue icons represent the enemy's formations. When an enemy target enters one of these areas and is detected by our formations, we assess the battlefield situation, the capabilities of each combat formations, and the status of available combat resources. Then, we will select the appropriate combat formations and complete COA planning based on above information.

## LOO based COA planning

The LOO model is used to plan COA for each decision area. Based on the missions assigned by the commander, the chosen COG, and the available resources of the combat formations, COA planning can be carried out for a single combat formation, or multiple formations can be combined. Combat formations carry out coordinated operations planning. Figure 9 illustrates the complete establishment process of the LOO model in the current coordinated air defense and anti-missile scenario. In the LOO model, to simplify the description, the names of the own formations are simplified and replaced with early warning UAV - E1, communication UAV - C, fighter UAV 1 - A1, fighter UAV 2 - A2, and vessel - V.

Then, we use PDDL language to complete an interception of missile 1 in area 2.

![img-6.jpeg](img-6.jpeg)

Fig. 8. Coordinated distributed air defense and anti-missile scenarios.

![img-7.jpeg](img-7.jpeg)

Fig. 9. Coordinated distributed air defense and antimissile scenarios.

```
(define (domain planning _ input)
    (:objects
        ? cog - Missile 1
        ? region - combat area 2
        ? decision _ point - 200 km
        ? resource - E1, C, Al
        ? task -intercept missile
    )
    (:types
    COG region decision _ point resource task
    )
    (:predicates
    ((target - of ?c - Missile 1 ?r - E1, C, Al))
    (task - target ?t - intercept missile ?c - Missile 1)
    (task - in - region ?t - intercept missile ?r - combat area 2))
    (at - decision - point ?r - combat area 2 ?dp - 200 km)
    )
    (:init
    (target - of ?cog ?resource)
    (task - target ?task ?cog)
    (task - in - region ?task ?region)
    (at - decision - point ?region ?decision)
)
(define (domain line _ of _ operation)
    (:objects
    ? cog - Missile 1
    ? unit 1 - E1
    ? unit 2 - C
    ? unit 3 - Al
    ? task 1 - track
    ? task 2 - communication
    ? task 3 - damage
    ? action 1 - Find, Fix
    ? action 2 - Share
    ? action 3 - Engage, Guide
    ? e 1 - effect of track
    ? e 2 - effect of communication
    ? e 3 - effect of damage
    ? dc - Attack Target
    ? dcp - 200 km
    )
    (:types
    COG unit unit unit mission _ task mission _ task mission _ task action action action effect effect effect decisive _
condition dc _ point
    )
    (:predicates
    (achieves - Missile 1 ?c - Missile 1 ?dc - Attack Target)
    (drives - dc ?unit 1 - E1 ? action 1 - Find, Fix ?e 1 - effect of track ?dc - Attack Target)
    (drives - dc ?unit 2 - C ? action 2 - Share ?e 2 - effect of communication ?dc - Attack Target)
    (drives - dc ?unit 3 - Al ? action 3 - Engage, Guide ?e 3 - effect of damage ?dc - Attack Target)
    (achieves - dcp ?dc - Attack Target ?dcp - 200 km)
    (composes - task 1 ? track ?action 1 - Find, Fix)
    (composes - task 2 ? communication ?action 2 - Share)
    (composes - task 3 ? damage ?action 3 - Engage, Guide)
    (has - effect 1 ?action 1 - Find, Fix ?e 1 - effect of track)
    (has - effect 2 ?action 2 - Share ?e 2 - effect of communication)
    (has - effect 3 ?action 3 - Engage, Guide ?e 3 - effect of damage)
    )
)
```

Algorithm 3. Definition of interception to missile 1

The LOOs for other COG targets are also created using the PDDL language. Once the LOO model for all enemy targets in the current situation is completed, the COA for each combat formation can be determined. Figure 10 displays one of the potential combinations of COAs, with Missile1 being the target for this set of COAs.

# DBNs evaluation model establishment 

According to the LOO model, we can obtain each decision area's effect evaluation chain and effect evaluation network. Figure 11 displays the effect evaluation network of the four decision areas.


Fig. 10. COA sample for target missile 1.
![img-8.jpeg](img-8.jpeg)

Fig. 11. EBO effect evaluation networks based on DBNs.

An evaluation network is created according to the combat areas divided in the LOO model. The LOO model determines the type and number of nodes. In the evaluation network of each stage, the parent node represents the direct effect of the action. When the action occurs, its value changes. The middle layer shows the action's intermediate effect, and each area's bottom node represents the DC point effect of each COG. The connecting lines in each area depict the relationship of influence between nodes.

Each stage's intermediate and DC effects will affect the effects of other stages. A static BN represents the network effect of each decision area. In the current scenario, since the combat stage is divided into four in the LOO model, the number and definition of BNs are determined accordingly. The dotted connecting line shows the probability transfer relationship of nodes between time slices. The intermediate and DC effects of the current decision area will influence the intermediate and DC effects of the following area. The last area's DC evaluation result is the current COA's evaluation result. To clearly illustrate the transfer relationship between Stage 2 and Stage 3, a schematic diagram of the connection between the two has been added in the lower left corner of Fig. 11 .

# Construction of EBO-BPNN optimization model 

This section outlines the construction of the EBO-BPNN optimization evaluation model under current combat scenarios. It includes the conversion from the DBNs model, the determination of input and output parameters, and the collection of datasets.


Fig. 12. Sample datasets of BPNN-Combat.


Table 1. Hyperparameter settings of EBO-BPNNs.

# Collection of the datasets

We utilized Visual Studio to construct a DBN network that encompasses the current combat scenario. Randomly generated data will be used as input for the EBO-BPNN evaluation network dataset for each decision area, and the DBNs evaluation network will calculate the intermediate and DC effects of each decision area as the output of the dataset. For each evaluation network, 10,000 samples are generated, with $70 \%$ randomly selected as the training set, $15 \%$ as the validation set, and $15 \%$ as the test set. Figure 12 displays the input and output formats of some datasets of the BPNN-Combat network.

## Determination of parameters

Based on the current combat scenario and the evaluation network for the DBNs effect, it is necessary to construct four networks for each enemy target. These networks will be used to evaluate and predict the COAs in decision areas. The EBO-BPN in four decision areas are defined as BPNN-Warning, BPNN-Combat, BPNN-Cooperate, and BPNN-Vessel. They will be used to evaluate the impact of coordinated actions in decision areas to complete DC successfully.

The inputs of EBO-BPNN include our actions and the potential actions that the enemy may take. The intermediate and DC effects of different time segments are additional inputs.

In the BPNN-Cooperate example, the network's input layer consists of 13 nodes. Nodes 1 to 8 represent the actions of multiple combat formations in the current decision area, while the ninth node represents the potential actions taken by the enemy target. The values of these nine nodes representing actions are 1.0 or 0.0 , with 1.0 indicating the execution of the action. The 10th to 12th nodes represent the intermediate effect of the previous regional stage, and the 13th node represents the DC effect of the previous decision area on a specific COG target. The network's output layer consists of four nodes, Node 1 representing the DC effect of the combat formation's action on a specific COG target in the current regional stage. Nodes 2 to 4 represent the intermediate effect of the current area.

The network's hidden layer determines the robustness and accuracy of the network evaluation. This study utilizes a single hidden layer network structure. Typically, a single hidden layer can solve most problems ${ }^{30}$, and the effectiveness of a single hidden layer was also confirmed during subsequent experiments.

In order to obtain more accurate evaluation results, it is essential to reasonably determine the number of neurons in the hidden layer when building a network. A reasonable number of neurons can ensure sufficient fitting and local optimal solutions. In this study, the initial setting for the number of neurons in the hidden layer is $2 / 3$ of the number of input nodes plus the number of output nodes. The number of neurons is adjusted during subsequent training and testing to achieve optimal prediction results. Specifically, the number of neurons is at most twice the number of input nodes.

The learning rate is a critical parameter that affects the training speed and stability. A more significant learning rate may lead to an unstable model training process, while a smaller learning rate will slow down the training speed ${ }^{31}$. Our study selected a lower learning rate for a more stable training result. Table 1 shows the the hyperparameter settings.

## Model training and tuning

After collecting and processing the datasets, it is essential to build a neural network and tune the training parameters to improve the accuracy of evaluating the effect of the COA. We will use MATLAB code to construct the EBO-BPNN model, and randomly divide and import the datasets. Various measures are available to compare

the accuracy of a network's evaluation of the effects of COAs. However, no universal standard method exists, so using multiple metrics to evaluate the network is essential [32]. This study utilizes three indicators: mean absolute error (MAE), mean squared error (MSE) and mean absolute percentage error (MAPE) [33,34].

$$
\begin{gathered}
M A E=\frac{1}{N} \sum_{n=1}^{N}\left|y_{n}-\hat{y}_{n}\right| \\
M S E=\frac{1}{N} \sum_{n=1}^{N}\left|y_{n}-\hat{y}_{n}\right|^{2} \\
M A P E=\frac{1}{N} \sum_{n=1}^{N}\left|\frac{y_{n}-\hat{y}_{n}}{y_{n}}\right| \times 100 \%
\end{gathered}
$$

Where $y_{n}$ is the actual evaluation result calculated using the DBN network, $\hat{y}_{n}$ is the action sequence evaluation result predicted by the EBO-BPNN network, and $N$ is the total number of data used to test the network.

# Performance analysis 

This section introduces the experimental results of four networks for evaluating the effect of COAs. All networks have been tuned multiple times, and the appropriate number of hidden layer neurons has been selected to achieve the required training accuracy. Fig. 13 illustrates the training process of the four networks.

The training environment is configured with Core i7-11800H, 16GB RAM, and GeForce RTX3060 6GB GPU. All four networks can reach the required training accuracy before reaching the maximum number of iterations. Specifically, BPNN-Warning converges in 173 epochs, BPNN-Combat in 140 epochs, BPNN-Cooperate in 243 epochs, and BPNN-Vessel in 131 epochs. To assess the predictive capability of the network, we randomly created 50 extra sets of data for testing purposes and employed the trained network for testing.
![img-9.jpeg](img-9.jpeg)

Fig. 13. The training processes of EBO-BPNNs.

![img-10.jpeg](img-10.jpeg)

Fig. 14. Comparison of observed and predicted data.


Table 2. The evaluation indicators of the models.

Figure 14 compares the test and predicted data of DC effects, it shows the regression of the model data. The X -axis represents the actual value of the dataset, and the Y -axis represents the model's predicted value. The higher the overlap between the actual and predicted values, the better the model's performance. The results show that the model can obtain good prediction results within the value range of the data set. The model's performance meets the use requirements and can accurately evaluate COA. Figure 15 illustrates the absolute errors of DC effects in four networks. The absolute errors of the selected test data are all less than $2.5 \times 10^{4}$.

In addition, Table 2 contains additional evaluation indicators for the models, all results are for DC effect. These indicators are derived from the test set used during training. The results indicate that BPNN-Combat has the lowest MAPE at $0.006733 \%$, and the MAPE of the other three networks is also less than $0.02 \%$, which meets the requirements and demonstrates the ability to effectively evaluate the COAs.

More importantly, using the BPNN-EBO method can effectively reduce the consumption of computing resources. Table 3 compares the COA evaluation results obtained using the BPNN-EBO and the DBNs methods. It is important to note that the outcomes presented for both models reflect the performance of a singular target. The five selected sets of data are randomly generated. It can be seen that using the BPNN-EBO method can obtain evaluation results similar to DBNs, and its MAPE is $0.0143798 \%$. At the same time, using the same computing resources, the average time consumed is reduced by, resulting in a $69.83 \%$ improvement in efficiency, which

![img-11.jpeg](img-11.jpeg)

Fig. 15. Absolute errors of the test data.


Table 3. Comparison of EBO-BPNN and DBNs performance.
can effectively improve the efficiency of COA evaluation for airborne scenarios where computing resources are constrained. Model training took less than 10 hours during our experiments, allowing for quick retraining and adjustment to new scenarios.

# Conclusions 

This paper proposes the LOO-based COA planning and EBO-BPNN evaluation methods. The COAs were determined using the LOO model, and prediction experiments were carried out on the EBO-BPNN model. The effectiveness of developing tactical-level COA was verified. The main conclusions are as follows:

1. The LOO model, established in this paper using PDDL language, accurately defines the input of combat elements, including decision areas, decision points, and other characteristic information related to COA generation. The model can adapt to battlefield environments and rapidly generate optional COAs.
2. This paper established a DBNs evaluation model to evaluate and optimize COA and modeled each node in the DBNs evaluation network to make it interpretable and scalable.

3. Based on the DBNs evaluation network, we constructed the EBO-BPNN evaluation model, which can further optimize and improve the computational efficiency of the COA optimization process. After testing and verification, the EBO-BPNN model can achieve similar evaluation results to the DBNs model, with MAPE of less than $0.02 \%$. Compared with the DBNs model, the EBO-BPNN model can achieve an efficiency improvement of no less than $65 \%$, effectively reducing the consumption of computing resources. Experts have verified the process and results.In summery, the methods proposed in this paper achieve the modeled description and generation of COA development, automatic evaluation, and calculation optimization of COA effects. It is worth noting that this method can be adapted to different combat scenarios during application. We can quickly model new scenarios by redefining and expanding relevant elements in the LOO model, updating and expanding nodes in the evaluation network, and completing the training and tuning of the EBOBPNN model, which allows us to complete the compliance COA planning and optimization with different scene constraints. It can effectively support the development and application of intelligent auxiliary DSS.

# Data availability 

The datasets used and/or analysed during the current study available from the corresponding author on reasonable request.

Received: 6 August 2024; Accepted: 10 September 2024
Published online: 18 September 2024

# Author contributions 

All authors contributed to the study conception and design. Y.L. was involved with software, methodology, data collection and preparation, and drafting. Y.W. contributed to programming, visualization. H.L. contributed to writing and editing. G.W. contributed to methodology. J.A. contributed to supervision, reviewing, and validation.

## Declarations

## Competing interests

The authors declare no competing interests.

## Additional information

Correspondence and requests for materials should be addressed to H.L.
Reprints and permissions information is available at www.nature.com/reprints.
Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/ licenses/by-nc-nd/4.0/.
(c) The Author(s) 2024, corrected publication 2024