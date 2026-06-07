# Bayesian graphical model based optimal decision-making for fault diagnosis of critical induction motors in industrial applications 

A. LAKEHAL*<br>Department of Mechanical Engineering, Mohamed Cherif Messaadia University, P.O. Box 1553, Souk-Ahras, 41000, Algeria


#### Abstract

In an effort to achieve an optimal availability time of induction motors via fault probabilities reduction and improved prediction or diagnostic tools responsiveness, a conditional probabilistic approach was used. So, a Bayesian network (BN) has been developed in this paper. The objective will be to prioritize predictive and corrective maintenance actions based on the definition of the most probable fault elements and to see how they serve as a foundation for the decision framework. We have explored the causes of faults for an induction motor. The influence of different power ranges and the criticality of the electric induction motor are also discussed. With regard to the problem of induction motor faults monitoring and diagnostics, each technique developed in the literature concerns one or two faults. The model developed, through its unique structure, is valid for all faults and all situations. Application of the proposed approach to some machines shows promising results on the practical side. The model developed uses factual information (causes and effects) that is easy to identify, since it is best known to the operator. After that comes an investigation into the causal links and the definition of the a priori probabilities. The presented application of Bayesian networks is the first of its kind to predict faults of induction motors. Following the results of the inference obtained, prioritizations of the actions can be carried out.


Key words: maintenance plan, predictive actions, prioritization, critical asynchronous motor, Bayesian approach.

## 1. Introduction

For many facilities using induction motors, the machines play a critical role in the overall process flow. Unavailability of an induction motor often means a significant reduction in or loss of plant output. That lost production translates into very costly downtime. Thus, corrective maintenance costs are not the only driving factor that can help justify a monitoring system. Lost production costs also factor heavily into the economic benefits a monitoring system can deliver. To minimize these costs and optimize the availability of induction motors, several research projects have been carried out in recent years for early detection of faults. Each fault has one or more symptoms, and for each symptom the researchers tried to define precursors. Faults in the induction motor result in a change in current signature, vibration signature, or both signatures at the same time [1, 2]. Other effects may also appear, such as torque fluctuations, reduced efficiency or overheating at the winding level.

In vibration analysis, the FFT tool (fast Fourier transform) allows the diagnosis of faults due to electromagnetic anomalies on the stator as well as on the rotor. In case there is a random change in the signal or change in the speed, vibration analysis technique may fail to provide accurate information. This mask effect represents a weakness of this technique. The current signal analysis technique has the advantages of being non-invasive and easy to implement. However, under certain conditions, its application is not sensitive enough because it has a low signal-to-noise ratio and its other disadvantages are related to spectral

[^0]leakage and its low-frequency resolution [3]. By analyzing the ultrasonic noise spectrum, it becomes possible to monitor and diagnose some faults, such as contact between rolling elements and air gap eccentricity. This technique also has some disadvantages, for example, the noisy background from the other machines and Maxwell's stresses that act on the iron surfaces. The sensitivity of one of the three methods depends on the nature of the fault. The stator current method is sensitive to the broken rotor bar fault, while the vibration method is sensitive to bearing faults. The acoustic method is likewise very attractive since it contains less noise and interference within the analyzing frequency band $[4,5]$.

Other techniques also exist: temperature (infrared thermography or/ and thermocouples) [6], magnetic flux [7], instantaneous angular speed [8], partial discharge [9] and air-gap torques [10]. Yet these techniques are specific to just a handful of faults, and the majority of them cannot, in any case, diagnose faults in electrical machines by themselves. Thus they are usually combined together to become exact and precise. Faced with this problem of uncertainty, most researchers have developed techniques that use artificial intelligence methods. The most widely used artificial intelligence methods for monitoring and diagnosis of induction motors include: expert systems, artificial neural networks (ANN), fuzzy logic and fuzzy neural networks. The knowledge contained in the expert system comes from the designer and the users' experience during maintenance operations. They have been used for online diagnosis of induction motors [11]. Electrical and vibration signals constitute, in most applications, elements of the knowledge base. And also the thresholds for the healthy and faulty case form the basis of the expert system.

ANNs have been one of the most used methods of artificial intelligence in recent years and have shown high performance,


[^0]:    *e-mail: lakehal21@yahoo.fr
    Manuscript submitted 2019-08-18, revised 2020-01-02, initially accepted for publication 2020-01-24, published in June 2020

especially in diagnostic automation. Bazan et al. have developed a pattern recognition model for the detection of stator winding short circuits [12]. The model uses current signals of two phases and allows detection with an accuracy of about $93 \%$. Another work, published by Verma et al. [13], presents a misalignment fault detection methodology by using an ANN whose inputs are vibration and current signals.

In yet another contribution, a fuzzy model was developed by [14] to diagnose two faults and their severity: broken bar and dynamic eccentricity. Vibration signals have also been used as input data in fuzzy algorithms. The fuzzy method has its insufficiencies if current or vibration signals are, separately, considered as input data; data hybridization shows promising results [15].

Fuzzy-neural approaches have been also used in fault diagnosis of induction motors. The purpose of these techniques is early fault detection and diagnosis. For example, a strategy for stator inter-turn faults detection from an adaptive neuro-fuzzy inference system is presented in [16]. Like other artificial intelligence methods, the data, used for fuzzy-neural algorithms and other algorithms derived from a combination of artificial intelligence methods (support vector machines, genetic algorithms), are mainly derived from current or/and vibration signals [17-19].

After this introduction, it is possible to conclude that the performance of the induction motor can be affected by one of the faults that are given, for indicative purposes, above and that will be discussed extensively in the rest of this article. Furthermore, intervention by the expert, when formulating the conditional rules, is unavoidable. One more thing is to be mentioned: most of the works that exist in the literature only deal with a single fault, despite the fact that in everyday practical cases, combined faults can occur in the same motor and at the same time. In such case, uncertainty increases and only extensive experience of the operator and knowledge of the specific behavior of the machine can solve the problem and allow for decision making. So, to help predict faults that will affect availability of the machine and efficiency of its maintenance schedule, we present a strategic decision framework that will aid maintenance staff in the decision-making process. This decision framework is based on expert knowledge and practical experience in the field of diagnosis.

Probabilities will be defined from several sources of information (measurement, expertise, feedback, tests). The probabilities of calculated faults are the key elements that will allow establishing the predictive maintenance plan. Indeed, if we manage to estimate the probabilities of faults, by means of the proposed Bayesian approach, we can guarantee reliability of the machine, and optimize its availability by anticipating corrective and predictive actions. It should be noticed, once again, that several faults can appear simultaneously on the induction machine, and in this case identification of the problem becomes difficult [20]. The effects of the combined faults may be the same, and again the diagnosis becomes more complicated.

In this paper, the causes and effects of various faults in induction motors are discussed qualitatively, via the structure of the Bayesian network (BN), and quantitatively, via the parame-
ters of the network. By ranking the faults, from most likely to the one with the lowest probability of occurrence, it is possible to prioritize maintenance interventions and make the induction machine park more reliable. Also, it is possible to make certain decisions regarding maintenance and spare parts replacement.

## 2. Bayesian networks

BNs, also called belief networks or causal networks, include graph theory and probability theory. BNs are causal graphical models that model links between a set of variables, where variables are represented by nodes and links by arcs. They are widely used, especially in the field of industrial diagnosis [21]. BNs have found other fields of application in recent years such as: reliability [22], fault prediction [23] and decision-making [24]. A network is called Bayesian if it checks for the Markov conditions. A BN can be described as a directed acyclic graph (DAG) that defines factorization of joint probability distribution on the variables that are represented by the nodes of the DAG, where factorization is given by the directed links of the DAG.

The objective of using the Bayesian approach is to model causality from the causes and their effects: we must, however, consider two cases:

- the causalities are strict, which implies acyclic graphs
- variables, which represent causes and their effects, are dependent (dependence on probabilities).
A BN, modeling a given problem, allows for qualitative analysis, via its structure (variables and causal relations between them), and for quantitative analysis, given by joint probability distribution that factorizes into a set of conditional probability distributions governed by the structure of the DAG (Fig. 1). Nodes without parents are defined by a priori probabilities, while the other nodes are defined from conditional probability tables (CPT).

Inference in the BN gives a posteriori probabilities. As BNs represent causal statements of the $\mathrm{A} \rightarrow \mathrm{C}$ type, where A is the cause of C , and C often takes the role of an observable effect of A , which typically cannot be observed itself; we need to derive the a posteriori probability distribution $\mathrm{P}(\mathrm{A} \mid \mathrm{C}=\mathrm{c})$, given the observation $\mathrm{C}=\mathrm{c}$, using the a priori distribution $\mathrm{P}(\mathrm{A})$ and the conditional probability distribution $\mathrm{P}(\mathrm{C} \mid \mathrm{A})$ specified in the model. The Bayes' theorem generates the following calculation:

$$
P(A \mid C=c)=\frac{P(C=c \mid A) P(A)}{P(C=c)}
$$

![img-0.jpeg](img-0.jpeg)

Fig. 1. Example of simple Bayesian network

The CPT defines the causality links in Bayesian formalism. For example, Table 1 shows a CPT for variable D .

Table 1
Conditional probability table for variable D


The inference rules are given by the CPT. Some readings are as follows:

- If variable A is True, then variable D exists.
- If variable A is False, then variable D exists if and only if variable B is True.
After inference in the network of Fig. 1, the a posteriori probabilities for each variable can be found. An example is given as follows:

$$
\begin{aligned}
& \mathrm{P}(\mathrm{D}=\text { True })=\mathrm{P}(\mathrm{D}=\text { True } / \mathrm{A}=\text { True }, \mathrm{B}=\text { True }) \times \\
& \times \mathrm{P}(\mathrm{~A}=\text { True }) \times \mathrm{P}(\mathrm{~B}=\text { True })+\mathrm{P}(\mathrm{D}=\text { True } / \mathrm{A}=\text { True } \\
& \mathrm{B}=\text { False }) \times \mathrm{P}(\mathrm{~A}=\text { True }) \times \mathrm{P}(\mathrm{~B}=\text { False })+\mathrm{P}(\mathrm{D}=\text { True } / \mathrm{A}= \\
& =\text { False }, \mathrm{B}=\text { True }) \times \mathrm{P}(\mathrm{~A}=\text { False }) \times \mathrm{P}(\mathrm{~B}=\text { True })+\mathrm{P}(\mathrm{D}= \\
& =\text { True } / \mathrm{A}=\text { False }, \mathrm{B}=\text { False }) \times \mathrm{P}(\mathrm{~A}=\text { False }) \times \mathrm{P}(\mathrm{~B}=\text { False })
\end{aligned}
$$

In a general context, a network is called a Bayesian network if it checks for the Markov factorization condition. So a BN is defined by:

$$
P\left(V 1, V 2, \cdots, V_{n}\right)=\prod_{i=1}^{n} P\left(V_{i} / C\left(V_{i}\right)\right)
$$

The procedure to be followed is given as follows (Fig. 2).
![img-1.jpeg](img-1.jpeg)

Fig. 2. Flowchart of Bayesian network based prediction methodology

## 3. Development of Bayesian network model

A BN is constructed through a combination of a manual and data-driven process, where partial knowledge about structure as well as parameters (conditional probabilities) blend with statistical information extracted from databases of cases (previous joint observations of values of the variables). Table 2 and

Table 2
Stator faults and their causes


Table 3
Rotor faults and their causes


Table 3 present, respectively, a census of the causes of stator and rotor faults in induction motors. Also in the same tables, a codification is adopted, each code representing a variable in the BNs developed in the rest of this article. A wound rotor may be affected by the same faults as the stator. For a cage rotor, faults are limited to the breaking of rods or breakage of short-circuit rings.

Statistically, a review of the IEEE 493-1997 standard [25] shows that $42 \%$ of faults are due mainly to bearing faults. Another more recent study conducted by [26] showed that bearing faults account for more than $50 \%$ of faults. Again according to the IEEE 493-1997 standard, the rotor represents $8 \%$ of
faults, while faults in the stator represent a percentage of $28 \%$. In this study, bearings will be considered a part of the rotor, and therefore the definition of the faults, given in Table 2 and Table 3, will concern only the rotor and the stator of the induction machine. Several faults can affect the induction machine [27], they have internal sources, such as bearing faults and broken rotor bars, and external causes, such as unbalanced power supply and humidity. In the following, seven major faults have been defined for the stator part [27] (Table 2): Vibration of the support, a fault between the stator and the carcass, insulation fault, short circuit between turns, short circuit between phases, displacement of conductors, and failure of electrical connections. For each fault, an investigation of the causes, which may give rise to these faults, allowed to identify the causes $\mathrm{C}(\mathrm{SFi}) \mathrm{j}$, where the index $i$ represents the faults and the index $j$ represents the causes associated with each fault.

Table 3 gives the probable causes of seven faults for the rotor: bearing fault, broken rotor bars, magnetic circuit fault, bearings misalignment, rotor misalignment, mechanical imbalance and bearings' loss of lubrication. In general, faults are mainly due to electrical, thermal, mechanical and environmental constraints.

Appropriate technical consultation with experts is a simple way to identify the causes and effects, and determine the links between them. All the faults (effects) that can appear on the induction machine are coded from F1 to Fi. In addition to this coding of faults, a coding of the causes $\mathrm{C}(\mathrm{Fi})$, specific to each Fi , must be established. Each fault Fi is connected to cause $\mathrm{C}(\mathrm{Fi})$. A priori probabilities have been defined from a computerized maintenance Management system (CMMS) database. Existing data, within the database, on causes $\mathrm{C}(\mathrm{Fi})$ allow to estimate that $\mathrm{P}(\mathrm{C}(\mathrm{Fi}))$ and $\mathrm{P}(\mathrm{Fi})$ will be evaluated by the Bayes' theorem:

$$
P(F / C(F))=\frac{P(C(F) / F) P(F)}{P(C(F))}
$$

If the a priori probabilities of faults $\mathrm{P}(\mathrm{F})$ and prior conditional probabilities $\mathrm{P}(\mathrm{C}(\mathrm{F}) / \mathrm{F})$ that the fault F is generated by the causes $\mathrm{C}(\mathrm{F})$ are known, it is possible from equation 3 to calculate the a posteriori probability $\mathrm{P}(\mathrm{F} / \mathrm{C}(\mathrm{F}))$ that cause $\mathrm{C}(\mathrm{F})$ generates fault F . Formally, a BN is defined by a DAG G , $\mathrm{G}=(\mathrm{V}, \mathrm{E})$, where F is the set of nodes of G , and E is the set of edges of G. Furthermore, in a probabilistic space $(\Omega, Z, P)$, with a non-empty finite set, $Z$ is a set of subspaces of $\Omega$, and P is a probability measure within Z , with $\mathrm{P}(\Omega)=1$.

With a combination of Fi and $\mathrm{C}(\mathrm{Fi})$, it is possible to obtain $\mathrm{P}(\mathrm{Fi})$ via the following equation:

$$
P\left(F_{1}, F_{2}, \ldots, F_{n}\right)=\prod_{i=1}^{n} P\left(F_{i} / C\left(F_{i}\right)\right)
$$

where $\mathrm{C}(\mathrm{Fi})$ is the set of causes of Fi in graph G .
Even if the causes are of different origins (electrical, mechanical, thermal and environmental), the faults can still have the same origins. On the one hand, BNs of Fig. 3 and Fig. 4 will allow for understanding their genesis to predict their

![img-2.jpeg](img-2.jpeg)

Fig. 3. Bayesian model for predicting stator faults
![img-3.jpeg](img-3.jpeg)

Fig. 4. Bayesian model for predicting rotor faults
severity and development. On the other hand, they will enable analyzing their impact on the behavior of the machine, and to deduce the probabilities allowing, a posteriori, to go up to the element of the machine.

In Fig. 3, we notice four common causes; unbalanced power supply can cause vibration and short circuit between phases. The shock or vibration cause can provoke fault between the stator and the carcass, short circuit between turns, displacement of conductors and connectors failure. Frequent startup can cause insulation faults and displacement of conductors. Finally, extreme temperature can cause insulation faults, short circuit between turns and short circuit between phases.

In Fig. 4, the unbalanced magnetic pull cause represents a common cause of bearing faults, broken rotor bars and rotor
misalignment. Thermal fatigue can cause broken rotor bars and magnetic circuit fault. Finally, overloading can cause magnetic circuit fault and bearings misalignment.

## 4. Validation of the model by case study

Most operators and maintenance managers refer to real-time and non-real-time measurements to assess the machine state and predict faults. In order to do this, a variety of standards are developed and published by international organizations. For example, according to vibration severity, these standards define four (04) classes of machines in terms of power [28]. The standard alone remains insufficient to predict faults. Another classification is based on the operating characteristics [29]. Induction motors are classified as:

- Class A: normal starting torque, high starting current and low operating slip,
- Class B: normal starting torque, low starting current and low operating slip,
- Class C: high starting torque and low starting current,
- Class D: high starting torque, low starting current and high operating slip.
The work presented in this paper is the continuation of the works done previously on elements of the induction machine separately [30-32]. In this contribution, real practical industrial application for indicating all stator and rotor faults together with their causes at the same time is presented. The novelty of this work is the definition of priorities in terms of intervention regarding six vital induction motors. Which is the motor that must be programmed in the first place for maintenance? Answers backed by numbers in the form of probabilities are given.

The six induction motors studied in the following part of this paper are three-phase motors. They are of different power ranges and are used in a petrochemical plant. Table 4 provides a description of these machines. It is important to mention that the choice of these 6 motors for the case study was mainly based on their high number of breakdowns and their importance and criticality.

Table 4
Description of 6 induction motors studied


It should be noted here that only field practice and experience represent a reliable and effective alternative for induction

motors monitoring and diagnosis. In this context and in order to obtain a permanent update of the predictive maintenance plan of induction motors, priorities will be defined based on the determination of the most probable faults on each machine.

To ensure fault prediction reliability, the starting information (model inputs) must be accurate and defined with maximum precision. The a priori probabilities, given by Table 5 and Table 6, are defined on the basis of the factual information, on

Table 5
A priori probabilities of causes for stator fault


Table 6
A priori probabilities of causes for rotor fault


the one hand, and the more or less complex measures recorded in the historical files on the other.

If we define action on the nature of the fault as the first stage of prediction, then, at this level, we will study the influence of different power ranges of machines. In this context and in order to obtain a permanent update of the predictive maintenance plan of the six (6) induction motors, priorities, based on
the determination of the most probable faults on each machine, have been defined. Fig. 5 and Fig. 6 present the distribution of probability of faults for the rotor and stator of each motor as well as the associated priorities.

An example of calculation for the stator element of motor M2 is given for the "Displacement of conductors" variable as follows:
![img-4.jpeg](img-4.jpeg)

Fig. 5. A posteriori probabilities for stator fault types
![img-5.jpeg](img-5.jpeg)

Fig. 6. A posteriori probabilities for rotor fault types

$\mathbf{P}(\mathbf{S F 6}=\underline{\text { True })}=$
$=\mathrm{P}(\mathrm{SF} 6=\underline{\text { True }} / \mathrm{C}(\mathrm{SF} 3) 2=\underline{\text { True}}, \mathrm{C}(\mathrm{SF} 2) 5=\underline{\text { True }) \times}$
$\mathrm{P}(\mathrm{C}(\mathrm{SF} 3) 2=\text { True }) \times \mathrm{P}(\mathrm{C}(\mathrm{SF} 2) 5=\text { True })+$
$+\mathrm{P}(\mathrm{SF} 6=\underline{\text { True }} / \mathrm{C}(\mathrm{SF} 3) 2=\underline{\text { True}}, \mathrm{C}(\mathrm{SF} 2) 5=\underline{\text { False }) \times}$
$\mathrm{P}(\mathrm{C}(\mathrm{SF} 3) 2=\underline{\text { True }) \times \mathrm{P}(\mathrm{C}(\mathrm{SF} 2) 5=\underline{\text { False })+}}$
$+\mathrm{P}(\mathrm{SF} 6=\underline{\text { True }} / \mathrm{C}(\mathrm{SF} 3) 2=\underline{\text { False}}, \mathrm{C}(\mathrm{SF} 2) 5=\underline{\text { True }) \times}$
$\mathrm{P}(\mathrm{C}(\mathrm{SF} 3) 2=\underline{\text { False }) \times \mathrm{P}(\mathrm{C}(\mathrm{SF} 2) 5=\underline{\text { True })+}}$
$+\mathrm{P}(\mathrm{SF} 6=\underline{\text { True }} / \mathrm{C}(\mathrm{SF} 3) 2=\underline{\text { False}}, \mathrm{C}(\mathrm{SF} 2) 5=\underline{\text { False }) \times}$
$\mathrm{P}(\mathrm{C}(\mathrm{SF} 3) 2=\underline{\text { False }) \times \mathrm{P}(\mathrm{C}(\mathrm{SF} 2) 5=\underline{\text { False })}}$
$\mathbf{P}(\mathbf{S F 6}=\underline{\text { True }})=(1 \times 0.065 \times 0.075)+(1 \times 0.065 \times 0.925)+$
$+(1 \times 0.935 \times 0.075)+(0 \times 0.935 \times 0.925)$
$\mathbf{P}(\mathbf{S F 6}=\underline{\text { True }})=0.004875+0.060125+0.070125+0$
$\mathbf{P}(\mathbf{S F 6}=\underline{\text { True })}=\mathbf{0 . 1 3 5 1 2 5}$.
The conditional probability table of the "Displacement of conductors" variable is provided by Table 7.

Table 7
Conditional probability table for "Displacement of conductors" variable


Another example of calculation for the rotor element of motor M4 is given for the "Bearing loss of lubrication" variable as follows:

$$
\begin{aligned}
& \mathbf{P}(\mathbf{R F 7}=\underline{\text { True })}= \\
& =\mathrm{P}(\mathrm{RF} 7=\underline{\text { True }} / \mathrm{C}(\mathrm{RF} 7) 1=\underline{\text { True}}, \mathrm{C}(\mathrm{RF} 7) 2=\underline{\text { True }) \times} \\
& \mathrm{P}(\mathrm{C}(\mathrm{RF} 7) 1=\underline{\text { True }) \times \mathrm{P}(\mathrm{C}(\mathrm{RF} 7) 2=\underline{\text { True })}} \\
& +\mathrm{P}(\mathrm{RF} 7=\underline{\text { True }} / \mathrm{C}(\mathrm{RF} 7) 1=\underline{\text { True}}, \mathrm{C}(\mathrm{RF} 7) 2=\text { False }) \times \\
& \mathrm{P}(\mathrm{C}(\mathrm{RF} 7) 1=\underline{\text { True } \times \mathrm{C}(\mathrm{RF} 7) 2=\text { False })} \\
& +\mathrm{P}(\mathrm{RF} 7=\underline{\text { True }} / \mathrm{C}(\mathrm{RF} 7) 1=\text { False }, \mathrm{C}(\mathrm{RF} 7) 2=\underline{\text { True }) \times} \\
& \mathrm{P}(\mathrm{C}(\mathrm{RF} 7) 1=\text { False }) \times \mathrm{P}(\mathrm{C}(\mathrm{RF} 7) 2=\underline{\text { True })} \\
& +\mathrm{P}(\mathrm{RF} 7=\underline{\text { True }} / \mathrm{C}(\mathrm{RF} 7) 1=\text { False }, \mathrm{C}(\mathrm{RF} 7) 2=\text { False }) \times \\
& \mathrm{P}(\mathrm{C}(\mathrm{RF} 7) 1=\text { False }) \times \mathrm{P}(\mathrm{C}(\mathrm{RF} 7) 2=\text { False }) \\
& \mathbf{P}(\mathbf{R F 7}=\text { True })=(1 \times 0.054 \times 0.032)+(1 \times 0.054 \times 0.968)+ \\
& +(1 \times 0.946 \times 0.032)+(0 \times 0.946 \times 0.968) \\
& \mathbf{P}(\mathbf{R F 7}=\text { True })=0.001728+0.052272+0.030272+0 \\
& \mathbf{P}(\mathbf{R F 7}=\text { True })=\mathbf{0 . 0 8 4 2 7 2}
\end{aligned}
$$

The conditional probability table of the "Bearing loss of lubrication" variable is provided by Table 8.

It is natural that the size of the machine and its power justify the nature of the fault. Priorities in terms of maintenance action are given in Table 9.

Table 8
Conditional probability table for "Bearing loss of lubrication" variable


Table 9
Most likely fault for each motor


The reliability of the entire motor is the product of all the elementary reliabilities of the rotor and stator. However, to improve this reliability, maintenance actions can be applied to the less reliable elements, which have a strong probability of breaking down. Fig. 7 gives the probabilities of detecting a fault in the rotor and stator of each motor. It is clear that the low probability of fault for the 6 motors is justified, given the importance of these machines and the level of monitoring applied, but we still have to look for improvements. The practical work done in this last section (through quantitative analysis) serves as a gateway to give a forecast vision on the availability of all the induction motors of the company. The 6 motors studied represent samples of the machine park that we want to apprehend.

Induction motors have the particularity that certain faults can affect the rotor and others can affect the stator separately. Also, the action may concern one of these two elements or the other. Now, for the establishment of maintenance plans, the inference results given by Table 5 and Table 6 and summarized in Table 9 can be used. In the case of the stator, priority in

![img-6.jpeg](img-6.jpeg)

Fig. 7. Probability of failure of each induction motor element

Intervention must be given to M1, M2, M6, M3, M4, and M5, respectively. For the rotor, priority in intervention must be given to M1, M5, M2, M4, M3, and M6, respectively. The results of this study can also be used to help the maintenance engineer draw up a prediction strategy oriented to the most likely faults and common symptoms. From Tables 5, Table 6, and Table 9, priority is given to bearing fault and rotor misalignment for motors M1, M3, M4, M5, and M6. For the stator element: stator carcass fault for motors M1 and M3, and stator turn-turn faults for motors M5 and M6.

Now, if the network structure is defined as causality links and the parameters are calculated based on the fault history, then it can be concluded that there is no difference between the different motors and the structure remains unchanged, but the parameters vary from one motor to another and the results do, too. This conclusion is motivated by the *a posteriori* probabilities, according to which most of the faults on the rotors of the 6 motors (Table 9) are related to the bearing fault and rotor misalignment. For the stator of the machine, most of the faults of the 6 motors are related to the stator carcass fault and short circuit between turns. Care must be taken in extrapolating the conclusions of this study to smaller motor sizes, to those with lower power or those working under specific environmental conditions. There are special motors whose windings can withstand temperatures higher than those used in the petrochemical field.

The prediction is based on the interpretation of the causes that represent the input variables, and the accuracy of the *a posteriori* probabilities depends on the richness of this interpretation. Moreover, in most cases of faults, these inputs are only partially defined, which increases uncertainty.

### 5. Conclusions

The proposed Bayesian approach does not replace the artificial intelligence techniques that exist in the literature, but makes a strong contribution towards decision-making. Throughout our long introduction, we attempted to discuss the main contribution in this research field. Also, and through the developed BN, we have been able to analyze information coming from various sources (sensor, behavior, yield, torque, expertise). Also, we were able to define the probabilities of each fault, and, consequently, the fault that represents potential danger for the machine. The case study presented focused on the power of the machine. Bearing faults and stator faults are most probable for large size motors. For low power motors, the highest probability is related to the stator. The strength contribution of the proposed method is to make decisions, on repair and maintenance, based on forecast data, and to also analyze the most favorable path of fault.

In addition to the prediction of faults and prioritization of maintenance actions, the Bayesian approach, presented in this paper, provides the possibility to perform quantitative analysis of faults and makes contributions for:

- **Experience feedback**: according to the criticality of the machine, the periods of update of the probabilities will be defined. The highest probabilities P(F) must be analyzed, then either eliminated or minimized, where appropriate. By selecting the highest probability, i.e., the one that penalizes the machine's availability the most, it is possible to plot the Pareto graphs in a manner that diagnoses the causes of unavailability.
- **Preparation and validation of the actions**: the preceding analysis allows targeting the correction and improvement actions that must be prepared, implemented, and then validated. Measuring P(F), over the next period, will enable measuring the effectiveness of the actions performed.
- **The consequences**: application of this Bayesian approach leads to constant search for progress; each problem solved will reveal new sources of information. Also, the results obtained streamline the preparation and planning of actions. The BN developed in this paper is truly useful and is easily personalized. With this tool, operators are able to reflect their specific operating and maintenance practices.

Acknowledgements. The author would like to thank the Directorate General for Scientific Research and Technological Development (DGRSDT) for financial support (PRFU code: A01L09UN410120190002). Also, he would like to express his appreciation for the valuable time that anonymous reviewers have dedicated to the review process.
