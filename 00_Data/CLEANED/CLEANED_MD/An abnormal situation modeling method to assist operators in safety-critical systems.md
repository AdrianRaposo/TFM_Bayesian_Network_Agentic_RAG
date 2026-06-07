# An Abnormal Situation Modeling Method to Assist Operators in Safety-Critical Systems 

Mohsen Naderpour ${ }^{1}$, Jie Lu, Guangquan Zhang<br>Decision Systems and e-Service Intelligence Laboratory<br>Centre for Quantum Computation \& Intelligent Systems, School of Software<br>Faculty of Engineering and IT, University of Technology Sydney<br>PO Box 123, Broadway NSW 2007 Australia<br>Mohsen.Naderpour@student.uts.edu.au, Jie.Lu@uts.edu.au, Guangquan.Zhang@uts.edu.au


#### Abstract

: One of the main causes of accidents in safety-critical systems is human error. In order to reduce human errors in the process of handling abnormal situations that are highly complex and mentally taxing activities, operators need to be supported, from a cognitive perspective, in order to reduce their workload, stress, and the consequent error rate. Of the various cognitive activities, a correct understanding of the situation, i.e. situation awareness (SA), is a crucial factor in improving performance and reducing errors. Despite the importance of SA in decision-making in time- and safety-critical situations, the difficulty of SA modeling and assessment means that very few methods have as yet been developed. This study confronts this challenge, and develops an innovative abnormal situation modeling (ASM) method that exploits the capabilities of risk indicators, Bayesian networks and fuzzy logic systems. The risk indicators are used to identify abnormal situations, Bayesian networks are utilized to model them and a fuzzy logic system is developed to assess them. The ASM method can be used in the development of situation assessment decision support systems that underlie the achievement of SA. The performance of the ASM method is tested through a real case study at a chemical plant.


Keywords: Situation awareness, Situation assessment, Safety-critical systems, Bayesian networks, Fuzzy logic systems, Risk assessment.

## 1. Introduction

Today, in many safety-critical systems the role of operators has shifted from manual controllers to supervisors or decision-makers who are responsible for extensive cognitive tasks [1]. Operators are often moved to a control room far away from the physical process and have to rely on human computer interaction (HCI) principles to observe and comprehend the overwhelming amount of rapidly changing data for processing. In the presence of all this data, complex interfaces, and dynamic situations, human error could be a serious cause of accidents in these environments. It has been found that in most industries, $70-90 \%$ of accidents are attributed to human error [2]. Traditionally, there are two approaches to prevent human error during operation of safety-critical systems. The first approach aims for the provision of better training programs for operators, and the second aims to improve operator support systems [3]. However, it has been shown that in abnormal time pressure situations, ordinary training does not improve the quality of decision making [4], and therefore, the role of cognitive support systems to assist operators in such situations is highlighted [5].

In abnormal situations, a well-trained operator should comprehend a malfunction in real time by analyzing alarms, assessing values, and recognizing unusual trends indicated by multiple instruments. In such a situation, many alarms from different systems are frequently triggered at the same time, making it difficult for the operator to make a decision within a very short time frame. If several abnormal situations occur at once, decisions have to be made in even less time. Operators are usually unable to judge what situation should be given priority when confronted with complex abnormal situations such as these [6, 7].

[^0]
[^0]:    ${ }^{1}$ Corresponding author, Tell: +61 295144520

To return operational units to normal conditions, operators must respond quickly and make rapid decisions, but under these circumstances, the mental workload of operators rises sharply, and a mental workload that is too high may increase the rate of error.

Despite the importance of human factors, most of the operator support systems focus on the deviation of the process from an acceptable range of operation, the identification of operation faults [8] or the prediction of process variables [9] that will violate an emergency limit in the future. Therefore, quantitative knowledge and hardware failures have been relied on significantly; however, when faults occur, human operators have to rely on their experience under working pressure to understand what is going on and to contribute a solution [10]. These problems highlight the urgency of cognitive human factors in the development of operator support systems to lower workload, stress and consequent error rates of operators. Of the various cognitive features, operators' situation awareness (SA) is considered to be the most important prerequisite for decision-making [11, 12]. To date, several SA models have been developed; however, Endsley's three-level model has undoubtedly received the most attention. This model describes SA as "the perception of the elements in the environment within a volume of time and space, the comprehension of their meaning and the projection of their status in the near future" [11]. The three-level model describes SA as an internally held product, comprising three hierarchical levels (i.e. perception, comprehension, and projection), that is separate from the processes called situation assessment, used to achieve it [11]. Usually, assessing a situation requires data integration with the support of computer-based intelligent techniques. Because SA aims to predict the status of a situation in the near future, which is the third level of the three-level model, proper and effective situation assessment approaches and tools to conduct the prediction are required.

Many studies have reported that machine learning techniques could be effectively used for intelligent prediction by extracting rules from previous data to generate new assessment results [13]. Despite the usefulness of machine learning techniques for situation assessment, their use in real environments, especially in abnormal situations, are very limited because of the lack of appropriate training data [14]. Therefore, a number of quantitative situation assessment models based on probabilistic modeling techniques, such as Miao et al. [15] and Kim and Seong [16], have been proposed. In the former, Miao et al. proposed a computational model of situation assessment using belief networks. Their model consists of developing a structure to represent the SA mental model, and developing a belief update algorithm to reflect SA event propagation and projection [15]. In the latter, Kim and Seong developed a situation assessment model based on Bayesian networks (BNs) for operators of nuclear power plants (NPPs). In their proposed model, the knowledge of operators, i.e. mental models, is elicited for assignation to the CPTs of the network, and when operators receive information from indicators, the probabilities of the states of the environment, i.e. several accidents, are updated [16]. They assume that the occurrences of situations are mutually exclusive, and they therefore provided very finite states, including four accidents for the environment, to avoid a large BN in which the need for essential data increases exponentially, or proportionally.

This paper develops a new abnormal situation modeling (ASM) method that exploits specific capabilities of BNs, risk indicators and fuzzy logic systems to determine abnormal situations, model them in a situational network, and assess them dynamically. The paper defines the situation as a set of circumstance in which a number of objects may have relationships with one another and the environment, and a hazardous situation as a possible circumstance immediately before harm is produced by a hazard. Therefore, an abnormal situation is defined as a hazardous situation if its risk is not acceptable. Conventional BN is considered as a representation of static cause-effect relationships between objects in a situation, and it is assumed that operators use Bayesian inference to process incoming information. In addition, as operators are usually able to form rules for every situation to assess risks, and those rules are an important part of their mental model, then the ASM method needs to resemble their thinking when confronted with abnormal situations. Therefore, to estimate the situational risk level, a fuzzy logic system (FLS) is utilized. Finally, the prototype based on the ASM method can trigger an alarm for every situation

that has an unacceptable risk; therefore, it is assumed that operators consider abnormal situations by considering observable variables and hearing alarms.

In comparison with previous research work, this study has advantages. First, situations in the ASM method might be inclusive, unlike previous studies in which situations are exclusive. Second, unlike previous networks that only include indicators and sensors that are unable to determine the cause of abnormal situations, the ASM method enables the most probable cause of abnormal situations to be obtained from the situation models, thus assisting operators to understand situations. Third, the ASM method is able to generate risk levels for every hazardous situation to show whether a situation is abnormal (i.e. its risk level is unacceptable), and to help operators to understand the hierarchy of investigations (i.e. a situation with a higher risk has priority over other situations to be investigated).

The paper is organized as follows. Section 2 presents the theory of BNs. The proposed ASM method is explained in Section 3. A case study from the US Chemical Safety Board investigation reports (www.csb.gov) is presented in Section 4 to demonstrate the performance of the ASM method. The conclusion and future work are summarized in Section 5.

# 2. Bayesian Networks 

A BN is defined as a couple: $\mathcal{G}=((N, A), \mathcal{P})$, where $(N, A)$ represents the graph; $N$ is a set of nodes; $A$ is a set of arcs; $\mathcal{P}$ represents the set of probability distributions that are associated to each node. When a node is not a root node, the distribution is a conditional probability distribution that quantifies the probabilistic dependency between that node and its parents [17]. A discrete random variable $X$ is represented by a node $n \in N$ with a finite number of mutually exclusive states. States are defined on $S_{n}:\left\{s_{1}^{n}, s_{2}^{n}, \ldots, s_{N}^{n}\right\}$. The set $\mathcal{P}$ is represented with Conditional Probability Tables (CPT), and each node has an associated CPT. For instance, if $n_{i}$ is a parent of $n_{j}$, and the nodes $n_{i}$ and $n_{j}$ are defined over the sets $S_{n_{1}}:\left\{s_{1}^{n_{1}}, s_{2}^{n_{1}}, \ldots, s_{M}^{n_{1}}\right\}$ and $S_{n_{j}}:\left\{s_{1}^{n_{j}}, s_{2}^{n_{j}}, \ldots, s_{L}^{n_{j}}\right\}$, the CPT of $n_{i}$ is then defined as a matrix by the conditional probabilities $p\left(n_{j} \mid n_{i}\right)$ over each $n_{j}$ state knowing its parents states $\left(n_{i}\right)$ :

$$
P\left(n_{j} \mid p a\left(n_{j}\right)\right)=\left[\begin{array}{lll}
p\left(n_{j}=s_{1}^{n_{j}} \mid n_{i}=s_{1}^{n_{i}}\right) & \ldots & p\left(n_{j}=s_{L}^{n_{j}} \mid n_{i}=s_{1}^{n_{i}}\right) \\
\vdots & \vdots & \vdots \\
p\left(n_{j}=s_{1}^{n_{j}} \mid n_{i}=s_{M}^{n_{i}}\right) & \cdots & p\left(n_{j}=s_{L}^{n_{j}} \mid n_{i}=s_{M}^{n_{i}}\right)
\end{array}\right]
$$

Various inference algorithms can be used to compute marginal probabilities for each unobserved node, given information on the states of a set of observed nodes, that the junction tree algorithm is the a classical one. Inference in BN then allows us to take into account any state variable observation (an event) so as to update the probabilities of the other variables. When observations are given, this knowledge is integrated into the network and all the probabilities are updated accordingly. A hard evidence of the random variable $X$ indicates that the state of the node $n \in N$ is one of the states $S_{n}:\left\{s_{1}^{n}, s_{2}^{n}, \ldots, s_{N}^{n}\right\}$. Nevertheless, when this knowledge is uncertain, soft evidence can be used. A soft evidence for a node $n$ is defined as one that enables the updating of the prior probability values for the states of $n[17]$.

### 2.1. Dynamic and Object Oriented Bayesian Networks

A dynamic BN (DBN) is a BN that includes a temporal dimension. This new dimension is managed by time-indexed random variables $X_{i}$, which is represented at time step $k$ by a node $n_{(i, k)} \in N$ with a finite number of states $S_{n_{k}}:\left\{s_{1}^{n_{1}}, s_{2}^{n_{1}}, \ldots, s_{M}^{n_{i}}\right\}$. Several time stages are represented by several sets of nodes and an arc that links two variables belonging to different time slices represents a temporal probabilistic dependence between these variables. DBNs then allow us to model random variables and their impacts on the future distribution of other variables. Defining these impacts as transition probabilities between the states of the variable at time step $k-1$ and those at time step $k$ leads to the definition of CPTs that are relative to inter-time slices. With this model, the future slice $(k)$ is conditionally independent of the past given the present $(k-1)[17]$.

Modeling complex systems with BNs generally leads to complicated models. To avoid this phenomenon, a particular class of BNs, the Object Oriented Bayesian Networks (OOBNs) have been defined [18]. This modeling is based on the decomposition of the global network into hierarchical levels. This representation method allows us to decentralize and to structure the knowledge within BNs of reduced size.

# 2.2. Bayesian Networks Evaluation 

There are three evaluation methods to validate the performance of a BN: sensitivity analysis, databased evaluation and non-quantitative evaluation of model outputs using experts. In the event that large data sets are not available, and the probabilities must be elicited from domain experts, the sensitivity analysis technique is often used to investigate the effect of probability parameter changes on the performance of BNs. This analysis investigates the influence of variation in the model inputs on outcomes, where inputs can be real inputs (i.e. values of observable nodes) or the parameters (i.e. values of conditional probabilities). The output of sensitivity analysis requires evaluation by experts [20].

Sensitivity to findings based on a $d$-separation concept determines whether evidence about one variable may influence belief in a query variable. Using sensitivity to findings, it is possible to rank evidence nodes that allow the expert to identify whether a variable is sensitive or insensitive to other variables in particular contexts. This helps to identify errors in either the network structure or the CPTs. In this regard, entropy is a common measure that assesses the average information required in addition to the current knowledge to specify a particular alternative. The entropy of a distribution over variable $X$ is defined as follows:

$$
H(X)=-\sum_{x \in X} P(x) \log P(x)
$$

and mutual information is used to measure the effect of one variable $(X)$ on another $(Y)$ :

$$
I(X, Y)=H(X)-H(X \mid Y)
$$

where $I(X, Y)$ is the mutual information between variables. This measure reports the expected degree to which the joint probability of $X$ and $Y$ diverges from what it would be if $X$ were independent of $Y$ [20].

Sensitivity to parameters considers altering each of the parameters of query nodes and observing the related changes in the posterior probabilities of the query node. Most sensitivity analyses are onedimensional and, therefore, they only vary one parameter at a time. If models are unaffected by the precision of either the model or the input numbers, they may still be sensitive to changes in combinations of parameters. However, testing all possible combinations of parameters is exponentially complex [21]. The one-dimensional sensitivity analysis can be conducted by a sensitivity function for the output probability $f(x)$ when $x$ is being varied. This sensitivity function is defined as follows [22]:

$$
f(x)=\frac{\alpha x+\beta}{\gamma x+\delta}
$$

where $\alpha, \beta, \gamma, \delta \in \mathbb{R}$ and they are constants built from parameters that are fixed. The sensitivity value of the parameter $x$ and the target probability can be obtained by taking the first derivative from the sensitivity as follows [22]:

$$
f^{\prime}(x)=\frac{\alpha \delta-\beta \gamma}{(\gamma x+\delta)^{2}}
$$

In some cases, finding parameter changes that satisfy constraints on probabilistic queries are required. The most common types of query constraints, given a value $k$ are:

$$
\begin{gathered}
P(y \mid e) \geq k \\
P(y \mid e) \leq k \\
P(y \mid e)-P(z \mid e) \geq k
\end{gathered}
$$

$$
\frac{P(y \mid e)}{P(x \mid e)} \geq k
$$

where evidence $e$ is an instantiation of variables $E$, and events $y$ and $z$ are values of the variables $Y$ and $Z$, respectively. For example, if event $y$ is more likely than event $z$ given evidence $e$, then it can be specified by the constraint $P(y \mid e)-P(x \mid e) \geq 0$. Also, it is possible to make event $y$ at least twice as likely as event $z$, given evidence $e$, by specifying the constraint $P(y \mid e) / P(x \mid e) \geq 2$. For a binary variable $X$ with two values $x$ and $\bar{x}$, there are two parameters $\theta_{x \mid u}$ and $\theta_{\bar{x} \mid u}$ for every parent instantiation $u$. Consider $\tau_{x \mid u}$ as a meta-parameter and assigne $\theta_{x \mid u}=\tau_{x \mid u}$; therefore the goal is to determine the amount of change that must be applied to $\tau_{x \mid u}$, which would lead to complementary changes in $\theta_{x \mid u}$ and $\theta_{\bar{x} \mid u}$ that can enforce the query constraint. To satisfy Inequalities 6 to $9, \tau_{x \mid u}$ should be respectively changed by $\Delta \tau_{x \mid u}$ such that:

$$
\begin{gathered}
p(y, e)-k \cdot p(e) \geq \Delta \tau_{x \mid u}\left(\pi_{x \mid u}^{y, e}+k \cdot \pi_{x \mid u}^{e}\right) \\
p(y, e)-k \cdot p(e) \leq \Delta \tau_{x \mid u}\left(-\pi_{x \mid u}^{y, e}+k \cdot \pi_{x \mid u}^{e}\right) \\
p(y, e)-p(z, e)-k \cdot p(e) \geq \Delta \tau_{x \mid u}\left(-\pi_{x \mid u}^{y, e}+\pi_{x \mid u}^{z, e}+k \cdot \pi_{x \mid u}^{e}\right) \\
p(y, e)-k \cdot p(z, e) \geq \Delta \tau_{x \mid u}\left(-\pi_{x \mid u}^{y, e}+k \cdot \pi_{x \mid u}^{z, e}\right)
\end{gathered}
$$

where $p(e)$ and $p(y, e)$ are the current probabilities of $e$ and $(y, e)$ and the constants $\pi_{x \mid u}^{e}$ are defined as follows [23]:

$$
\pi_{x \mid u}^{e}=\frac{\partial P(e)}{\partial \tau_{x \mid u}}=\frac{P(e, x, u)}{\theta_{x \mid u}}-\frac{P(e, \bar{x}, u)}{\theta_{\bar{x} \mid u}}
$$

and $\pi_{x \mid u}^{y, e}$, as well as $\pi_{x \mid u}^{z, e}$ when applicable, are crucial to the procedure of finding the necessary change in $\tau_{x \mid u}$ to enforce the query constraint [23]. The solutions of $\Delta \tau_{x \mid u}$ in Inequalities 10 to 14 are always in one of the following forms:

- $\Delta \tau_{x \mid u} \leq \delta$, for computed $\delta<0$, in which case the new value of $\tau_{x \mid u}$ must be in the interval $[0, p+\delta]$ where $p$ is the current value of $\tau_{x \mid u}$.
- $\Delta \tau_{x \mid u} \geq \delta$, for computed $\delta<0$, in which case the new value of $\tau_{x \mid u}$ must be in the interval $[p+\delta, 1]$ where $p$ is the current value of $\tau_{x \mid u}$.
Therefore, $\delta$ is the minimum amount of change in $\tau_{x \mid u}$ that can enforce the query constraints. The proof of the above results can be found in [23], as well as the extended binary variable $X$ to a multivalued variable.


# 3. An Abnormal Situation Modeling Method 

When an abnormal situation occurs in a safety-critical system, operators firstly recognize it by an alarm, and secondly, need to perform a situation assessment, which means that they try to understand what is happening in the plant. During the situation assessment process, operators receive information from observable variables or other operators and process the information to establish situation models based on their mental models [16]. Mental models refer to mechanisms whereby humans are able to generate descriptions of the system's purpose and explanations of its functioning [24]. Mental models embody stored long-term knowledge about the systems that can be called upon to interact with the relevant system when needed. In addition, a situation model is described as a schema depicting the current state of the mental model of the system. In this sense, the situation model is the current instantiation of the mental model. Endsley believes that the situation model provides a useful window on the broader mental model [24]. In this sense, the current paper assumes that the operator's mental model can be modeled using BNs as a representation of static cause-effect relationships between objects in the situation. In addition, it is assumed that the operator uses rules to assess the situations in the environment. For instance, if an operator has the rule, 'when the probability of the situation of accumulated vapor in the

production unit is likely, and this situation has a catastrophic severity, therefore the risk level of this situation is not acceptable', this rule helps the operator to understand that 'when the risk level of the situation of accumulated vapor increases, the occurrence of an explosion is possible'. The ASM method is described based on a cycle illustrated in Figure 1 and explained in the following steps:
![img-0.jpeg](img-0.jpeg)

Figure 1: A cycle to describe the ASM method.
Step 1: Identify the situations of interest: To identify hazardous situations, an analysis is carried out using a combination of cognitive engineering procedures and hazard identification methods. Observation of operator performance, analysis of written materials and documentation, expert elicitation and formal questionnaires may be used to conduct the analysis. Previous hazard identification documents may help with this analysis. At the end of this step, there are several proposed situations that have clear operational meaning to the modeler, the domain experts and the operators.
Step 2: Identify the contributing objects: The contributing objects (both physical and conceptual) of every hazardous situation are obtained in a participatory environment to ensure that the breadth of issues and potential inputs are identified. In addition, previous documents of safety studies such as HAZOP, fault tree or event tree analyses help with this identification.
Step 3: Develop situation models: For every hazardous situation, a situation model is developed based on contributing objects using the capabilities of BNs c. The situation model begins with root nodes, which are the basic objects, followed by intermediate nodes, a pivot node and leaf nodes. The pivot node is the focal object that delegates the situation, and relations between the root nodes and the pivot node define the relationships between the objects. The leaf nodes may be safety barriers that are physical objects in the environment that will connect to one another if there is a relationship between their performances. In addition, one of the leaf nodes may be a consequence node that shows the possible accidents of the situation. If the situation is inferred by one observable variable, the focal object is connected to the observable variable.
Step 4: Describe the states of model variables: The states of basic and intermediate objects and safety barriers are defined as Boolean (i.e. success and failure), which refers to the objects working well (success) or not working (failure). The focal node, which delegates the situation, has two states, i.e. safe and hazardous. The states of consequence nodes are usually determined by consequence analysis, which concerns what may follow the occurrence of an abnormal situation. Finally, the states of observables can be determined in terms of operation, six sigma quality and safety set-points.
Step 5: Parameterize the quantitative model: The prior probability of basic objects (nodes without parents) is obtained through failure probability datasets such as the Center for Chemical Process Safety [25], and the Offshore Reliability Data Handbook [26], and if the failure probability is not available, expert judgment can be used. The CPTs of intermediate and focal nodes are set based on the "OR gate" or "AND gate" definition, as represented in Figure 2. The CPTs of consequence nodes are determined by 0 and 1 values corresponding to appropriate states. The CPTs of observable variables are elicited from domain experts. The elicitation process is carried

out with the recursive technique (e.g. Delphi method) to guarantee the convergence of the results.
![img-1.jpeg](img-1.jpeg)

Figure 2: The OR and AND gates in BN representation.
Step 6: Develop a situational network: Several situations can exist in parallel, and the complete modeling of their dependencies results in a network of situations. This may also include temporal dependencies, i.e. that the existence probability of an inferred situation in the future can be supported by the earlier existence of the situation itself, or other situations.
Step 7: Evaluate the situational network: Evaluation of the situational network requires the assessment of model behavior to ensure that the model demonstrates acceptable behavior. The evaluation can be undertaken at several levels. The first level is to ensure that key objects and their relationships have been represented in the network, and the second level should review the determined states to ensure that they have been defined unambiguously. The third level should be performed both through sensitivity analysis as well as by testing how the model behaves when analyzing well-known scenarios.
Step 8: Analyze the situational network over time: Both probability prediction and probability diagnosis are used for this analysis. In predictive analysis, conditional probabilities of the form $P\left(S_{t} \mid V_{t}^{s}\right)$ are calculated, indicating the occurrence probability of situation $S_{t}$ at time $t$, given the current value of observable variable $V_{t}^{s}$. In diagnostic analysis, conditional probabilities of the form $P\left(O_{t}^{s} \mid S_{t}\right)$ are evaluated, showing the occurrence probability of a particular object $O_{t}^{s}$ given the occurrence of situation $S_{t}$. In addition, the risk level of every situation at time $t$, i.e. $R\left(S_{t}\right)$, is calculated as $R\left(S_{t}\right)=P\left(S_{t}\right) * S\left(S_{t}\right)$ where $P\left(S_{t}\right)$ is the probability and $S\left(S_{t}\right)$ is the severity of that situation. Twenty five rules in terms of linguistic variables elicited form operators are shown in Table 1 that use fuzzy logic to mathematically emulate human reasoning and allow an operator to express his/her knowledge in the form of related imprecise inputs and outputs in terms of linguistic variables. For example, IF $P\left(S_{t}\right)$ is Even AND $S\left(S_{t}\right)$ is Major THEN $R\left(S_{t}\right)$ is Not acceptable. The results are obtained using a fuzzy logic system where the membership functions illustrated in Figure 3 and Mamdani's fuzzy logic operations are utilized to generate the output.

Table 1: Operators' rules for assessing the risk of situations.


![img-2.jpeg](img-2.jpeg)

Figure 3: Membership functions of probability, severity, and risk.

# 4. Application of ASM Method at a Chemical Plant 

On 28 August 2008, a runaway chemical reaction at a residue treater used to produce methomyl caused an explosion, and two employees who were investigating why the residue treater pressure was increasing, were killed. Several factors contributed to the accident, but a poor GUI of the new $\mathrm{DCS}^{1}$ was found to be one important factor [27]. In fact, the interface of the new operation system could not provide adequate support for the operator's SA to assist understanding of a dynamic, fast-moving environment.

### 4.1. Case Description

Methomyl is a white, crystalline solid with a slight sulfurous odour that is classified as a carbamate insecticide. Methomyl dust is combustible and can form explosive mixtures when dispersed in the air, with the risk of disrupting central and peripheral nervous system functions. Methyl isocyanate, or MIC, is one of the key chemicals used to make methomyl. It is highly reactive with water and must be stored in stainless steel or glass containers at temperatures below $40^{\circ} \mathrm{C}\left(104^{\circ} \mathrm{F}\right)$ to prevent a highly exothermic reaction. The methomyl production process begins by aldoxime and chlorine reacting to make chloroacetaldoxime, which reacts with sodium methyl mercaptide to produce methylthioacetaldoxime (MSAO). MSAO reacts with methyl isocyanate to produce methomyl. Excess MIC is removed from the methomyl-solvent solution and the solution is pumped to the crystallizers where an anti-solvent is added to cause the methomyl to crystallize. Finally, the crystallized methomyl is separated from the solvents in a centrifuge and the methomyl cake is removed, dried, cooled, packaged in drums, and moved to the warehouse. The liquid residue in the centrifuge contains very small quantities of methomyl and other impurities. Distillation separates the solvents in solvent recovery flashers and recycles the solvents to the beginning of the process. The unvaporized solvents and impurities, which include up to 22 percent methomyl, accumulate in the bottom of the flasher. The flammable liquids can be used as fuel in the facility steam boilers; however, before this flammable waste liquid, which is called "flasher bottoms", can be pumped to an auxiliary fuel tank, the methomyl concentration has to be reduced to not more than 0.5 percent by weight for environmental and processing considerations. The residue treater is used to dilute the incoming flasher bottoms, and designed to operate at a high enough temperature, and with sufficient residence time, to decompose the methomyl in the flasher bottom stream to below 0.5 percent by weight (Figure 4). The solvent and residual waste material is transferred to the auxiliary fuel tank for use as a

[^0]
[^0]:    ${ }^{1}$ DCS is a dedicated system used to control manufacturing processes; it is connected to sensors and actuators, and uses set point controls to control process variables

fuel in the facility steam boiler. Vapor generated in the methomyl decomposition reaction exits through the vent condenser to the process vent system where toxic and flammable vapor are removed [27].
![img-3.jpeg](img-3.jpeg)

Figure 4: The residue treater piping system [27].
Two kinds of operation for a residue treater can be considered: startup and routine. During startup, the residue treater is manually pre-filled with solvent to a minimum level of about 30 percent. This means that the operation will not start at a lower level. The solvent is heated by steam flows through the heater. When the liquid temperature has increased to set-point limit, the steam flow valve is closed, recirculation flow is redirected from the heater to the cooler, and the routine operation is started. The routine operation is considered for modeling in this study.

# 4.2. Observable Variables 

There are four transmitters in the environment that provide the online condition for the residue treater. To use these variables in BN-based models, they have to be discretized. In general, mapping a continuous variable to a discrete variable can be done by a crisp set or a fuzzy set. For instance, the temperature of the inside of a tank defined on the frame $[0,100]^{\circ} \mathrm{C}$ can be discretized to a scheme of three states: Cold, Warm, and Hot corresponding to the intervals $[0,40)^{\circ} \mathrm{C},[40,60)^{\circ} \mathrm{C},[60,100]^{\circ} \mathrm{C}$, respectively. A reading of $39.9^{\circ} \mathrm{C}$ from the thermometer would fall under the discrete state Cold, whereas, $40^{\circ} \mathrm{C}$ would be labeled Warm. As can be seen, there is no meaningful way to determine a crisp boundary between these states. Hence, using classical sets with crisp boundaries to discretize a continuous variable may generate unpredictable results for BNs [28]. In this section, the fuzzy states of the observable variables are determined in terms of operation and safety set-points:

- Liquid level (L): A level transmitter provides the residue treater liquid level. The routine operation is not started at a level lower than 30 percent, and the maximum permissible level of liquid is 50 percent. The value range of the liquid level variable is divided into three fuzzy states: Low, Normal and High. The membership function of L is illustrated in Figure 5 and determined as follows:

$$
\begin{aligned}
\mu_{L(L)}(x) & =\left\{\begin{array}{lc}
1 & x \leq 30 \\
(35-x) / 5 & 30<x \leq 35 \\
\mu_{L(N)}(x) & =\left\{\begin{array}{l}
(x-30) / 5 \\
1
\end{array} & 30 \leq x<35\right. \\
(50-x) / 5 & 35 \leq x<45 \\
\mu_{L(H)}(x) & =\left\{\begin{array}{l}
(x-45) / 5 \\
1
\end{array} & 45 \leq x<50 \\
& x \geq 50
\end{array}\right.
\end{aligned}
$$

![img-4.jpeg](img-4.jpeg)

Figure 5: Membership function of liquid level.

- Recirculation flow (F): During the operation, a pump provides a steady state recirculation, and a flow transmitter measures the flow of liquid through the recirculation pipeline. The value range of recirculation flow is divided into three fuzzy states: Very Low, Low, and Normal. The membership function of F is determined as follows, and is presented in Figure 6.

$$
\begin{aligned}
& \mu_{F(V L)}(x)=\left\{\begin{array}{cc}
1 & x \leq 10 \\
(20-x) / 10 & 10<x \leq 20 \\
(x-10) / 10 & 10 \leq x<20 \\
1 & 20 \leq x<40 \\
(60-x) / 20 & 40 \leq x<60 \\
\mu_{F(N)}(x)= \begin{cases}(x-40) / 20 & 40 \leq x<60 \\
1 & x \geq 60\end{cases} \\
& \mu_{F}(x)
\end{aligned}
$$

![img-5.jpeg](img-5.jpeg)

Figure 6: Membership function of recirculation flow.

- Temperature (T): The content of the residue treater is maintained at approximately $135^{\circ} \mathrm{C}$, which ensures that the incoming methomyl quickly decomposes so as not to accumulate to an unsafe concentration inside the residue treater. A temperature transmitter provides the residue treater temperature. The temperature value range is divided into two fuzzy states, Normal and High. The membership function of T is determined as follows, and shown in Figure 7.

$$
\begin{aligned}
& \mu_{T(N)}(x)=\left\{\begin{array}{lc}
1 & x \leq 135 \\
(140-x) / 5 & 135<x \leq 140 \\
\mu_{T(H)}(x)= \begin{cases}(x-135) / 5 & 135 \leq x<140 \\
1 & x \geq 140\end{cases} \\
& \mu_{T}(x)
\end{aligned}
$$

![img-6.jpeg](img-6.jpeg)

Figure 7: Membership function of temperature.

- Pressure (P): The maximum allowable operating pressure of the residue treater is 50 psig , but it normally operates at 20 psig . A pressure transmitter provides the residue treater pressure. The pressure value range is divided into three fuzzy states: Normal, High, and Very High. The membership function of P is determined as follows, and shown in Figure 8.

$$
\begin{aligned}
& \mu_{P(N)}(x)= \begin{cases}1 & x \leq 20 \\
(25-x) / 5 & 20<x \leq 25 \\
\mu_{P(H)}(x)= \begin{cases}(x-20) / 5 & 20 \leq x<25 \\
(30-x) / 5 & 25 \leq x \leq 30\end{cases} \\
& \mu_{P(\forall H)}(x)= \begin{cases}(x-25) / 5 & 25 \leq x<30 \\
1 & x \geq 30\end{cases}
\end{aligned}
$$

![img-7.jpeg](img-7.jpeg)

Figure 8: Membership function of pressure.

# 4.3. Abnormal Situations 

There are seven abnormal situations in the environment. The contributing objects of situations are elicited and summarized in Table 2, along with symbols and their failure probabilities. The failure probabilities are determined based on data recorded by the Offshore Reliability Data Handbook [26]; however, in limited places the judgement of experts was utilized. The situations are modeled based on the ASM method as shown in Figure 9, and to avoid a long modeling description, the CPTs are omitted. The first three situations are independent situations and modeled based on their objects, and the other four situations are dependent situations and modeled based on their objects and the independent situations:

- Situation of vent condenser failure (SVC): A vent condenser is a plume abatement device that cools and condenses the vented steam by cold plant water. At the residue treater, vapor generated in the methomyl decomposition reaction exits through the vent condenser to the process vent system where toxic and flammable vapor are removed.
- Situation of high liquid level (SHL): Operation at a liquid level higher than 50 percent of vessel capacity is dangerous. Therefore, the residue treater has an automatic level control system and a manual level controller to maintain the liquid level at less than 50 percent. This situation can be inferred by the liquid level variable (L).
- Situation of abnormal recirculation (SAR): The residue treater recirculation system is used to heat the solvent at the beginning of a new production run, mix the incoming flasher bottoms in the partially filled vessel, and remove excess heat generated from the exothermic decomposition of the methomyl inside the vessel. During routine operation, the recirculation flow is directed to the cooler. The cooler is provided with constantly circulating $80^{\circ} \mathrm{C}$ water, which is sufficient to remove excess heat from the decomposing methomyl and maintain the liquid temperature within operating limits, provided that the bulk methomyl average concentration inside the residue treater remains below 0.5 percent. The situation is inferable by the flow variable (F).
- Situation of high pressure (SHP): The residue treater includes a pressure vessel with a maximum allowable operating pressure of 50 psig , and automatic pressure control. The vent condenser at the top of the residue treater, which is prone to blockages during unit operation, passes the gases produced by the methomyl decomposition reaction to the flare system. The gas flow carries trace amounts of solid material into the vent system where they are deposited on the surface of the pipe,

and over time, accumulated deposits can choke the flow and cause the residue treater pressure to climb. The situation can be inferred from the pressure variable (P).

- Situation of high temperature (SHT): During the operation, an automatic temperature control system monitors the bulk liquid temperature inside the vessel. During routine operation, water flows to remove excess heat generated by the exothermic decomposition of the methomyl inside the vessel. The SHT is inferred from temperature variable (T).
- Situation of high concentration of methomyl (SHC): The methomyl safely decomposes inside the residue treater to a concentration of less than 0.5 percent by weight. At normal operating conditions, the temperature of the flasher bottoms liquid is kept at about $80^{\circ} \mathrm{C}$ to prevent uncontrolled auto-decomposition of the more highly concentrated methomyl. The contents of the residue treater are maintained at approximately $135^{\circ} \mathrm{C}$, the temperature that ensures that the incoming methomyl quickly decomposes to avoid accumulation to an unsafe concentration inside the residue treater. If the tank is allowed to cool below $130^{\circ} \mathrm{C}$ for any reason, it must be sampled before being heated again. It is assumed that operators sample the residue treater liquid and the appropriate testing is conducted by the laboratory.
- Situation of runaway reaction (SRR): A runaway reaction is a chemical reaction over which control has been lost. It continues to accelerate in reaction speed until it either runs out of reactants, or the vessel containing it over-pressurizes and containment is lost. The runaway reaction results if methomyl is allowed to accumulate in the residue treater and a high pressure situation exists in the environment.

Table 2: Situations, their objects and symbols.



# 4.4. Situational Network Development 

Table 3 shows the available safety barriers in the environment. A continuous air monitor system is located in and around the production unit with 16 stationary sample points to detect fugitive leaks from process equipment. It detects concentrations of airborne chemical contaminants and alerts facility occupants if air concentration exceeds safe levels ( 1.0 ppm ). In addition, there is an ignition barrier, a fire alarm and several fire cannons in the environment to reduce damage if a fire occurs. The air monitoring system, alarm, and fire cannons are considered as safety barriers, as shown in:

Table 3: Safety barriers.


The situation of runaway reaction (SRR) can have results that range from the boiling over of the reaction mass, to large increases in temperature and pressure that lead to an explosion. Such violent reactions can cause blast and missile damage. If flammable materials are released, fire or a secondary explosion may result. Hot liquids and toxic materials may contaminate the workplace or generate a toxic cloud that may spread off-site. There can be serious risk of injury, even death, to plant operators and the general public, and the local environment may be harmed. Therefore, SRR has a consequence node whose states are determined as shown in Table 4. The table contains the degree of loss corresponding to every state, which is evaluated by the experts.

Table 4: The states of SRR consequences node.


For other situations, the resultant situation is considered as a consequence of the occurrence. The degree of loss in these situations is also calculated and summarized in Table 5.

Table 5: Loss of situations.


A situational network for the case study is developed and illustrated in Figure 9. Based on OOBN characteristics, the situational network is simplified as instance nodes in Figure 10.

![img-8.jpeg](img-8.jpeg)

Figure 9: Dynamic situational network.
![img-9.jpeg](img-9.jpeg)

Figure 10: Collapsed form of dynamic situational network.

# 4.5. Situational Network Evaluation 

Sensitivity analysis is conducted to evaluate the situational network. The investigation is necessary to characterize minimal parameter changes that are needed to ensure the conformance of the situational network with expectations. As the number of variables in the situational network is considerable, it is difficult to manually perform sensitivity analysis, and therefore, software such as Netica [29] to analyze the sensitivities to findings, and SamIam [30] to analyze the sensitivities to parameters, are utilized.

Application of the sensitivity to findings shows that the query variable, SRR, in the absence of other evidence, is most sensitive to SHP, followed by observable variable P, as shown in Table 6. This is what the experts expected because SRR results if methomyl is allowed to accumulate in the residue treater and the pressure relief system is not working properly. When findings for observable variable P (i.e. $\mathrm{P}=\mathrm{High}$ ) are entered into the network, the sensitivity measures and the ranking of variables are changed. With this evidence, SRR is most sensitive to SHC and SHL, followed by observable variable L. Alternatively, when

$\mathrm{P}=$ High and $\mathrm{L}=$ High are entered into the network, some of the remaining variables are more influential. These observations agreed with the experts understanding of the situational network.

Table 6: Sensitivity to findings analysis performed on SRR.


Sensitivity to parameters was analyzed in the CTPs of observable variables, which were determined by the experts. For instance, scenario $\mathrm{S}=(\mathrm{SRR}$, Hazardous, $\mathrm{E}=\{\mathrm{SHP}=$ Hazardous, $\mathrm{T}=$ High $\})$ was investigated, in which the hypothesis under consideration is SRR=Hazardous, while the parameter in focus is $P(\mathrm{~T}=$ High $\mid \mathrm{SHT}=$ Hazardous $)$. Therefore, the sensitivity function $f(t)$ was defined as follows:

$$
f(t)=P(S R R=\text { Hazardous } \mid \text { SHP }=\text { Hazardous }, T=\text { High })=\frac{\alpha t+\beta}{\gamma t+\delta}
$$

The coefficients of denominator and numerator functions were determined separately. Both functions are linear in the parameter $t$. Thus, the coefficients of each function were determined by propagating evidence for two different parameter values. The sensitivity function resulted as follows when $t_{0}=0.1$ and $t_{l}=0.2$ were used to propagate evidence:

$$
f(t)=\frac{6.31 t+0.0001}{6.09 t+1}
$$

The graph of the sensitivity function $f(t)$ for all possible values of $t$, i.e. values between zero and one, is plotted in Figure 11. As can be seen, the minimum value of the probability of the hypothesis is 0.0001 for $t=0$ while the maximum value of the probability of the hypothesis is 0.887 for $t=1$. Clearly, the posterior probability of the hypothesis is more sensitive to variations in the parameter value when the initial parameter value is in the range from 0 to, say, 0.5 , than when the initial parameter is in the range from 0.5 to 1 .
![img-10.jpeg](img-10.jpeg)

Figure 11: The graph of the sensitivity function $\mathrm{f}(\mathrm{t})=P(\mathrm{SRR}=$ Hazardous $] \mathrm{E})$.
A model deficiency was the posterior probability $P(\mathrm{SAR}=$ Hazardous $] \mathrm{F}=$ Low $)=0.4333$. The experts believed that the probability should be no less than 0.65 given this evidence. Therefore, some of the network parameters were changed to satisfy this query constraint (corresponding to Inequality 4). The use of Samlam software for any solution for every network parameter returned seven suggestions of single parameter changes. Four of the parameter changes were ruled out because they were changing the failure probabilities of basic objects. The only sensible parameter change was to decrease $P(\mathrm{~F}=$ Low $]$ SAR=Safe) from 0.1 to $<=0.01374$.

# 4.6. Situational Network Analysis 

The performance of the proposed method is investigated through a scenario retrieved from a real case [27] in the residue treater environment. A virtual plant user interface as shown in Figure 12 (left) along with a developed prototype interface based on the ASM method are used to conduct the simulation. The interfaces display the necessary information for operators to monitor the operation and manipulate the components. The prototype interface (i.e. Figure 12 (right)) that was developed based on the collapsed form of the situational network, triggers an alarm for every situation that has a risk level in excess of 2.5, i.e. tolerable not acceptable. The operator immediately considers the abnormal situations by hearing alarms and observing online variables. Whenever it is necessary, by mouse-clicking any situation in the interface; the operator can see a pop-up window that contains the related sub-network, including contributing objects, their failure probabilities, and the most probable explanation.
![img-11.jpeg](img-11.jpeg)

Figure 12: Virtual plant user interface and the ASM method user interface.

# 4.6.1. Scenario 

To prepare for a routine operation, the vessel was filled with solvent and heated. Methomyl was added into the residue treater, and a normal recirculation loop flow was ensured to mix the concentrated methomyl feed with preheated solvent in the residue treater. At approximately 12 pm , the board operator manually opened the residue treater feed control valve and began feeding flasher bottoms into the vessel. At normal flow rate, it would take approximately 30 minutes to fill the residue treater to 50 percent, the normal operating level. The outside operator started the recirculation pump at $12: 30 \mathrm{pm}$, as directed by the board operator. The residue treater liquid level was approximately 50 percent and the temperature ranged between 130 and $135^{\circ} \mathrm{C}$. The pressure remained constant at 22 psig. The trends of observable variables are illustrated in Figure 13. At 12:41 pm, the temperature began to rise steadily about 1 degree per minute. At 12:49 pm, the level was 51 percent when the recirculation flow suddenly dropped to zero. In less than 3 minutes, the temperature was at $147^{\circ} \mathrm{C}$, the highest safe operating limit.
![img-12.jpeg](img-12.jpeg)

Figure 13: The trend of observable variables.

### 4.6.2. Results

By assigning fuzzy partitioning values of observable variables after starting the routine operation, i.e. after 12:00 pm, to the situational network, the posterior probabilities of the situations are calculated, as shown in Figures 14 and 15. As can be seen, there is a sharp increase in the probabilities of SHL at 12:24 pm, SVC and SAR at 12:44 pm, SHC at 12:40 pm and SHT at 12:43 pm. The posterior probabilities are unable to support the operators' understanding of the current state of the situation. The operators must still rely on their knowledge and mental models to comprehend what is going on; therefore, the use of risk indicators and situational models are used to support their comprehension and projection. The risk level of situations is calculated and summarized in Figures 16 and 17. As can be seen, the estimated risk level of SAR increases at 12:45 pm from 1.32 (acceptable) to 2.95 (tolerable not acceptable) which means this hazardous situation is abnormal at present and needs to be recovered. The risk level of other independent situations, i.e. SHL and SVC, remains acceptable; however, there is a rise in their posterior probabilities. The risk level of SHP is steady and acceptable as expected, i.e. the pressure inside the vessel is almost normal. The risk level of SHT and SHC increases from acceptable at 12:45 pm, i.e. 1.32 and 1.65, respectively, to tolerable not acceptable, i.e. 2.95 and 3, respectively. Likewise, although there is an increase in the risk level of SRR, it remains acceptable during the study period, which means that this hazardous situation does not threaten the system.
![img-13.jpeg](img-13.jpeg)

Figure 14: Posterior probability of independent situations.

![img-14.jpeg](img-14.jpeg)

Figure 15: Posterior probability of dependent situations.
![img-15.jpeg](img-15.jpeg)

Figure 16: Risk level of independent situations.
![img-16.jpeg](img-16.jpeg)

Figure 17: Risk level of dependent situations.

At 12:45 pm when the risk level of SAR rises, the situational network shows that the most probable explanation is the failure of the recirculation pump (RP). The board operator immediately contacts the outside operator and directs him to check the recirculation pump. The outside operator's inspection at 12:47 pm determines the valid performance of the RP. With new evidence (success of the RP), the board operator realized that the failure of the temperature sensor (TS) in the recirculation is the most likely factor. Considering the result of the situation assessment, maintenance decisions are made to recover the situation. The trend of observable variables after abnormal situation recovery is illustrated in Figure 18.
![img-17.jpeg](img-17.jpeg)

Figure 18: The trend of observable variables after abnormal situation recovery.

The prototype helps the operator to prevent accidents in abnormal situations, but it also presents the factors that contribute to the creation of an accident, or a specific consequence. For instance, if at 12:52 pm a fire with low death and moderate property damage (C4) is reported, the posterior probability updating from this evidence shows that the closed cooling water isolation valve (CWC) causes inadequate ventilation, and consequently SHP in the residue treater which, with SHC, creates SRR.

# 5. Conclusion and Future Work 

Situation awareness is a state of knowledge that is distinguished from a process called 'situation assessment'. Situation assessment models explain main features and general principles about how people process information and interact with the environment to maintain their SA. Since situation assessment is a dynamic and collaborative process, it requires data integration with the support of computer-based intelligent techniques. In this regard, the paper introduces an innovative abnormal situation modeling (ASM) method that can be used as a situation assessment decision support for operators in safety-critical systems when confronted with abnormal situations. The paper defines the situation as a set of circumstances in which a number of objects may have relationships with one another and the environment, and a hazardous situation as an event that exists immediately before harm is produced by the hazard. Therefore, the paper uses risk indicators to identify abnormal situations as those hazardous situations where their risk levels are not acceptable.

The ASM method models the operators' mental model using BNs to represent these cause-effect relationships between objects in a situation. It also describes how the states and CPTs of objects in the models should be determined, and how they should be connected to each other to create a situational network. As the situations of interest can be inferred by observable variables, e.g. sensors, distributed in the environment, the ASM method explains how the situations can be connected to observable variables. It then uses a fuzzy logic system to represent the operators' mental model to assess the situational risk. A prototype based on the ASM method and characteristics of OOBNs was developed that triggers an alarm for every situation that has an unacceptable risk and by mouse-clicking any situation in the interface and provides a pop-up window that contains the related sub-network and supplementary information.

As has been shown through a real case study, the ASM method provides a useful graphical model that meets the requirements of a practical SA system. The proposed method has certain advantages over other situation assessment methods that use artificial intelligence tools such as expert systems and neural networks. It includes nodes and directed arcs to express the knowledge, and new information can be transmitted by directed arcs between nodes; whereas updating knowledge in expert systems is difficult and neural networks must learn knowledge via datasets, assuming training data are available. In addition, the cumulative effect of situations based on new evidence is very suitable for the SA continuity, whereas this feature does not exist in other artificial intelligence tools. In comparison with previous BN-based studies, the ASM method is more reasonable because it provides a basis for modeling the situations that might be inclusive, it enables the understanding of situations by providing the contributing objects, it provides the projection of future situations or events, and it assists operators by providing the hierarchy of situation investigations.

The ASM method also has certain limitations. First, it uses the BNs to facilitate the inclusion of prior background knowledge and the updating of this knowledge when new information is available from the SCADA monitoring system. As operators do not perform mathematical calculations while performing a situation assessment, the proposed method provides only an approximation of operator behavior in this process. Second, the ASM method needs to generate warnings when awareness is diminished due to uncertainty or lack of data by failed sensors. Third, in the development of situation models, some data are collected from experts; therefore, some uncertainty associated with the probability distributions is unavoidable.

The direction for future study will be to evaluate the developed human-computer interface based on SA measurements. Situation awareness measurements determine the degree to which design concepts and

new technologies improve or degrade an operator's SA. Therefore, they are a critical part of any system and procedural design process, and evaluation work.

# Acknowledgment 

The research presented in this paper was supported by Australian Research Council (ARC) under Discovery Project DP140101366.
