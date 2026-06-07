# Considering the Human Operator Cognitive Process for the Interpretation of Diagnostic Outcomes Related to Component Failures and Cyber Security Attacks 

Wei Wang ${ }^{1}$, Francesco Di Maio ${ }^{2}$, Enrico Zio ${ }^{2,3,4}$<br>${ }^{1}$ Department of Mechanical Engineering, City University of Hong Kong, Kowloon, Hong Kong, China<br>${ }^{2}$ Department of Energy, Politecnico di Milano, Via La Masa 34, 20156 Milano, Italy<br>${ }^{3}$ MINES ParisTech / PSL Université Paris, Centre de Recherche sur les Risques et les Crises (CRC), Sophia Antipolis, France<br>${ }^{4}$ Eminent Scholar, Department of Nuclear Engineering, Kyung Hee University


#### Abstract

In this work, we consider diagnostics of cyber attacks in Cyber-Physical Systems (CPSs), based on data analytics. For the first time to authors knowledge, the performance of such diagnosis is quantified considering the possible failure of the human operator cognitive process in interpreting and understanding the diagnosis support tool outcomes.

A Non-Parametric CUmulative SUM (NP-CUSUM) approach is used for datadriven diagnostic, and the cognitive process of the human operator who interprets its outputs is modelled by a Bayesian Belief Network (BBN). The overall framework is applied on the digital controller of the Advanced Lead-cooled Fast Reactor European Demonstrator (ALFRED).


Keywords: Cyber-Physical System; Diagnostic; Non-Parametric CUmulative SUM (NP-CUSUM); Human Cognition; Bayesian Belief Network; Nuclear Power Plant.

# ABBREVIATIONS 


## NOMENCLATURE



with empirical distributions $N\left(u\left(e_{i}^{\beta, \beta-\text { oother }}\right), \sigma\left(e_{i}^{\beta, \beta-\text { oother }}\right)\right)$, and $\theta=$ other for the other elements whose missing mean and standard deviation values shall be linearly interpolated

# 1. INTRODUCTION 

Cyber-Physical Systems (CPSs) feature a tight combination of (and coordination between) the physical process that runs in the system and the cyber domain that, by high automation level, real-time monitors, dynamically controls and supports decisionmaking during system operations [1-3].

Despite the benefits of CPSs, such as increased functionality, expanded capability and improved flexibility, the concern exists that their operation can be compromised not only by failures but also by attacks [4-6], that can be both physical or cyber.

Attacks depend on many factors (e.g., attacker profile, skills, motivation, etc.), which makes it difficult for defenders to anticipate and diagnose attack scenarios [4, 7, 8]. This is particularly true for cyber attacks, which are the focus of this work, since the majority of game-theoretic models assume that the defender moves first (e.g. designing a system, as in this work), and that the attacker moves after [9-13]. However, this means that an attacker can maximize the objective (of his/her malevolent act) and cyber attacks might be disguised from random failures, rendering the recovery difficult [14, 15].

Data-driven methods (e.g., the Sequential Probability Ratio Test (SPRT) [16, 17], the Cumulative Sum (CUSUM) chart [14, 18, 19], the Exponentially Weighted Moving Average (EWMA) inspection scheme [20]) have been proposed for the analysis of deviations in the observations from nominal values for diagnosing component stochastic failures. Machine learning techniques, including supervised learning (e.g., Support Vector Machine (SVM) [21], Neural Network (NN) [22]), unsupervised learning [23] and reinforcement learning (e.g., Q-learning [24, 25]), have also been proposed for such diagnosing task [26, 27].

Practically, the outcomes of the diagnosis are made available to operators via digital Human-Machine Interfaces (HMIs). The operator is requested to interpret these outcomes and take decisions on what to do or not do for responding to the effects induced by the diagnosed failures [28-30]. The human cognition process for assessing the system state based on the interpretation of the diagnostic outcomes can improve the diagnostic performance or worsen it [28, 29, 31-34]. This has been analyzed considered

in the literature, using expert judgment [35, 36] and artificial intelligence [37, 38].
Methods and algorithms have been developed also for diagnosing cyber attacks [14, 39, 40]. In this work, without loss of generality, a Non-Parametric CUmulative SUM (NP-CUSUM) method (a sequential anomaly detection technique proposed in the literature for detecting parameter changes in physical systems [14, 41, 42]) is adopted for components failures [43, 44] and cyber attacks [14, 45-47], and the human operator cognition process that interprets the monitoring/detection outcomes for situation assessment (i.e., the operator develops his/her mental representation of the specific current situation), and response planning (i.e., the operator takes decisions for dealing with the assessed situation) [29, 30, 48] is originally modelled by a Bayesian Belief Network (BBN). Specifically, a BBN typically used for structuring expert knowledge, understanding and cognition errors related to component stochastic failures diagnosis [28, 30, 31, 49-53] is here originally tailored for modelling the human operator cognitive process for interpreting of the diagnostic outcomes originated from cyber attacks.

A further novelty of the work consists in the overall framework of analysis, shown in Fig. 1, structured to capitalize the information made available by monitoring a CPS affected by cyber attacks and/or component stochastic failures for diagnosing the occurring events by a data-driven diagnostic tool, such as NP-CUSUM, where considering the human operator cognitive process in the interpretation of the diagnostic outcomes that influence the operator decision.
![img-0.jpeg](img-0.jpeg)

Fig. 1 Overall framework

A case study is considered, concerning stochastic components failures and cyber attacks that can occur in the digital Instrumentation and Control (I\&C) system of the

Advanced Lead Fast Reactor European Demonstrator (ALFRED) [54]. An objectoriented simulator previously developed [55, 56], comprising a multi-loop Proportional-Integral (PI) controller [57], is utilized for simulating the ALFRED dynamic response to failures and cyber attacks. Data are fed to the NP-CUSUM algorithm [15], and the diagnostic outcomes are interpreted by operators, whose cognitive process is modelled by BBN.

The rest of the paper is organized as follows. Section 2 presents the main characteristics of the ALFRED reactor with its digital I\&C system, the MC engine for injection of components failures and cyber breaches, and the NP-CUSUM technique. The operator cognitive process modelled by BBN is presented in Section 3. Section 4 presents the results and Section 5 concludes the paper.

# 2. THE ADVANCED LEAD-COOLED FAST REACTOR EUROPEAN DEMONSTRATOR 

### 2.1 The Reactor and the digital I\&C system

ALFRED is a small-size ( 300 MW ) pool-type fast reactor, cooled by molten lead [54]. During operation, Control Rods (CRs) height $h_{C R}$ is adjusted for thermal power $\left(P_{T h}\right)$ regulation, reactivity swing compensation during the cycle, and scram for safe shutdown when necessary [58].

At full power nominal conditions, the dynamics processing of the primary and secondary cooling systems is controlled by a multi-loop PI (Proportional and Integral) control scheme (see Fig. 2). Such decentralized control scheme allows simplicity of implementation and robustness to malfunctioning of the single control loops [55, 56]. Both feedback and feedforward digital control schemes are used (see Fig. 2 shadowed part). The PI-based feedback control configuration employs four SISO (Single Input Single Output) control loops independent of each other.

![img-1.jpeg](img-1.jpeg)

Fig. 2. ALFRED reactor control scheme

The control system aims at keeping the controlled variables at the steady state values, which give the optimal working conditions at full power nominal conditions. For example, it is expected that the coolant (i.e., lead) flow coming from the cold pool enters the core at temperature $T_{L, \text { cold }}$ equal to $400^{\circ} \mathrm{C}$, controlled by the $T_{L, \text { cold }}-\mathrm{PI}_{3}-G_{\text {water }}$ control loop of Fig. 2.

The parameters specification at full power nominal conditions are reported in Table 1.

Table 1 ALFRED parameters values at full power nominal conditions


Redundancy is commonly applied to sensors and signal processing units of a

digital I\&C system [59]. In the ALFRED digital control scheme, redundancy has been used to design each independent SISO loop.

Fig. 3 shows an example of the redundant design scheme of the $T_{L, \text { cold }}-\mathrm{PI}_{3}-G_{\text {water }}$ control loop. The real values of the coolant SG outlet temperature $T_{L, \text { cold }}(t)$ are measured by a sensor. After collected and converted to quantized (discretized) values by a data acquisition system, the measurements are duplicated by two identical digital-to-analog converters (DACs) to Subsystem 1 for computing (feeding) and 2 for monitoring, respectively. The received measurements of Subsystem $1 T_{\text {L,cold }}^{\text {feed }}(t)$ are fed to the computational unit $\mathrm{PI}_{3}$, whereas those of Subsystem $2 T_{\text {L,cold }}^{\text {monitor }}(t)$ are taken as redundant data, for detecting anomalous conditions.
![img-2.jpeg](img-2.jpeg)

Fig. 3 The redundancy design of the $T_{L, \text { cold }}-\mathrm{PI}_{3}-G_{\text {water }}$ control loop

Measurements are realistically considered to be affected by two types of errors [60, 61]: measurement errors (assumed distributed according to a normal distribution) and quantization errors (which are rooted in the DACs and are assumed uniformly distributed between $-1 / 2$ and $+1 / 2$ Least Significant Bit (LSB)). For simplicity, but without loss of realism, Table 2 lists the reference values of the controlled variables, the distributions of sensor measurement errors and the quantization errors that each control loop is subjected to.

Table 2 List of reference parameters for safety variables


In Fig. 4, measurements from the four control loops of the ALFRED are shown, on a time horizon $t_{M}$ equal to 1000s: the values of the variables are kept approximately at their nominal values, at full power nominal conditions, with some measurement errors (white noise) and quantization errors.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Measurements from the four control loops of ALFRED at full power nominal conditions (star values for computing subsystem and triangle values for monitoring subsystem): (a) Steam SG outlet temperature; (b) SG pressure; (c) Coolant SG outlet temperature; and (d) Thermal power

# 2.2 Failures and cyber breaches 

Both stochastic failures and cyber attacks can compromise the functionality of the ALFRED digital I\&C system. Even if cyber attacks are different from components stochastic failures, they can lead to similar consequences on the system physical processes (e.g., both a stochastic failure and a cyber attack can result in sensor performance degradation $[62,63])$.

To model failures and cyber attacks, a MC sampling scheme is integrated with the ALFRED model for injecting stochastic failures of sensors and cyber breaches, at

uniform random times $t_{R}$ along the mission time $t_{M}$ and of random magnitudes (see [15] for future details).

The occurrence of a sensor failure at random time $t_{R}$ results in an altered sensor measurement $y^{\text {sensor }}(t)$, that can potentially lead the ALFRED to accidents [64-66]. Therefore, if $y(t)$ is the real value of the controlled variable $y$ at time $t, \delta_{y}(t)$ is the nominal measuring error (distributed according to a normal distribution $N(0, \sigma)$ ), and $y^{F, \text { sensor }}(t)$ is the datastream (false measurement) when the sensor that measures $y(t)$ has failed (due to bias, drift, wider noise or freezing $[15,64,67]$ ):

$$
y^{\text {sens }}(t)=\left\{\begin{array}{ll}
y(t)+\delta_{y}(t), & t<t_{R}, \quad \text { normal } \\
y^{F, \text { sensor }}(t), & t \geq t_{R}, \quad \text { sensor failure }
\end{array}\right.
$$

Without loss of generality, we consider the diagnosis of the health state of the $T_{L, \text { cold }}-\mathrm{PI}_{3}-G_{\text {water }}$ control loop of Fig. 3 (all the discussion remains valid for any other control loop of the I\&C system). Stochastic failures of the $T_{L, \text { cold }}$ sensor cause the measurements $T_{\text {L,cold }}^{\text {sens }}(t)$ to differ from the real values that should be measured in the physical system due to bias, drift, wider noise and freezing [15]. Alternatively, a Denial of Service (DoS) attack can cause the blocking of a legitimate packet traffic and its substitution by a malicious packet traffic, preventing the controllers from receiving legitimate measurements and mimicking the stochastic sensor failures. Fig. 5 shows the schematics of a DoS attack, in which the computing unit is fed by a malicious packet traffic, whereas a legitimate packet traffic is fed to the monitoring unit [14, 68-72].
![img-4.jpeg](img-4.jpeg)

Fig. 5 Schematics of DoS attacks

# 2.3 The NP-CUSUM algorithm for data-driven diagnostic 

Data-driven diagnostic capability based on the NP-CUSUM algorithm [14, 15] is

embedded into the control loops, for distinguishing the sensor failures from the DoS attacks. As explained in [15], the diagnostic involves two main functions: (i) reception of measurements by the controllers and feeding to the NP-CUSUM algorithm, which has been (offline) trained on different system behaviors for setting its parameters; and (ii) use of the trained algorithm and rules for discriminate recognition of failures and cyber attacks. With respect to the $T_{L, \text { cold }}-\mathrm{PI}_{3}-G_{\text {water }}$ control loop, without loss of generality:
(i) The redundant Subsystems 1 and 2 collect the measurements of $T_{L, \text { cold }}^{\text {sensor }}(t)$ at each successive time $d t$, namely, $T_{L, \text { cold }}^{f e e d}(t)$ and $T_{L, \text { cold }}^{\text {monitor }}(t)$, respectively, and the NP-CUSUM algorithm calculates the score function-based statistics $S_{T_{L, \text { cold }}}^{f e e d}(t)$ and $S_{T_{L, \text { cold }}}^{\text {monitor }}(t)$ of the collected measurements, to check whether they exceed the offline determined threshold $h_{T_{L, \text { cold }}}$ : if yes, record the time(s) to alarm $\tau_{T_{L, \text { cold }}}^{f e e d}$ or/and $\tau_{T_{L, \text { cold }}}^{\text {monitor }}$ and proceed with the rule-based diagnostics.
(ii) If both $\tau_{T_{L, \text { cold }}}^{f e e d}$ and $\tau_{T_{L, \text { cold }}}^{\text {monitor }}$ are recorded (because both $S_{T_{L, \text { cold }}}^{f e e d}(t)$ and $S_{T_{L, \text { cold }}}^{\text {monitor }}(t)$ have exceeded the threshold), calculate the difference $\Delta \tau_{T_{L, \text { cold }}}$ between the times to alarm, $\tau_{T_{L, \text { cold }}}^{f e e d}$ and $\tau_{T_{L, \text { cold }}}^{\text {monitor }}:$

$$
\Delta \tau_{T_{L, \text { cold }}}=\left|\tau_{T_{L, \text { cold }}}^{\text {feed }}-\tau_{T_{L, \text { cold }}}^{\text {monitor }}\right|
$$

and compare it with a predefined reference difference $\Gamma_{T_{L, \text { cold }}}^{r e f}$ for rule-based decision making:

- If $\Delta \tau_{T_{L, \text { cold }}} \leq \Gamma_{T_{L, \text { cold }}}^{r e f}$, classify the event as " $T_{L, \text { cold sensor failure }}$ ";
- If $\Delta \tau_{T_{L, \text { cold }}}>\Gamma_{T_{L, \text { cold }}}^{r e f}$, classify the event as "DoS attack".

Notice that the NP-CUSUM algorithm requires that its parameters $\varepsilon_{T_{L, \text { cold }}}, h_{T_{L, \text { cold }}}$ and $\Gamma_{T_{L, \text { cold }}}^{r e f}$ are customized to the different system behaviors, to guarantee the capability of discriminating between failures and cyber attacks in the $T_{L, \text { cold }}-\mathrm{PI}_{3}-G_{\text {water }}$ control loop (see [15] for future details). For illustration purpose, Fig. 6 plots $T_{L, \text { cold }}^{f e e d}(t)$ and

$T_{L, \text { cold }}^{\text {monitor }}(t)$ when a bias failure is injected at time $t_{R}=630 \mathrm{~s}$, with a bias factor $b$ equal to $7.569^{\circ} \mathrm{C}$, leading to $T_{L, \text { cold }}^{F, \text { sensor }}(t)=T_{L, \text { cold }}(t)+b+\delta_{T_{L, \text { cold }}}(t)$, where $t \geq t_{R}$. As shown in Fig. 6(a), the $T_{L, \text { cold }}$ sensor bias failure deviates both measurements $T_{L, \text { cold }}^{f e e d}(t)$ and $T_{L, \text { cold }}^{\text {monitor }}(t)$ from the real values of the physical system $T_{L, \text { cold }}(t)$. Fig. 6 shows that the bias results in a very quick response of both statistics $S_{T_{L, \text { cold }}}^{f e e d}(t)$ and $S_{T_{L, \text { cold }}}^{\text {monitor }}(t)$, evaluated on the measurements $T_{L, \text { cold }}^{f e e d}(t)$ and $T_{L, \text { cold }}^{\text {monitor }}(t)$. Indeed, both statistics reach quickly the threshold $h_{T_{L, \text { col }}}$ (dotted line) and the difference $\Delta \tau_{T_{L, \text { cold }}}$ between the times to alarm $\tau_{T_{L, \text { cold }}}^{f e e d}$ and $\tau_{T_{L, \text { cold }}}^{\text {monitor }}$ turns out to be actually equal to zero (i.e., less than $\Gamma_{T_{L, \text { cold }}}^{r e f}$ equal to 9 s ) (see Fig. 6(b)), allowing for the (correct) identification of the event as a sensor failure mode and not as a cyber attack.
![img-5.jpeg](img-5.jpeg)

Fig. $6 T_{L, \text { cold }}$ sensor bias failure mode: (a) the received measurements $T_{L, \text { cold }}^{f e e d}(t)$ and $T_{L, \text { cold }}^{\text {monitor }}(t)$ of feed and monitor Subsystems in which the bias occurs at time $t_{R}$ equal to 630s; (b) the corresponding NP-CUSUM statistics $S_{L, \text { cold }}^{f e e d}(t)$ and $S_{L, \text { cold }}^{\text {monitor }}(t)$ for diagnosing the bias failure

Contrarily, Fig. 7(a) shows a cyber attack to the computing unit, mimicking a bias failure mode at $t_{R}=630 \mathrm{~s}$ (with $b$ again equal to $7.569^{\circ} \mathrm{C}$ ): this leads $T_{L, \text { cold }}^{f e e d}(t)$ to deviate from $T_{L, \text { cold }}^{\text {monitor }}(t)$ (that, indeed, is the legitimate $T_{L, \text { cold }}^{\text {sensor }}(t)$ measured by the $T_{L, \text { cold }}$

sensor). The different values between the malicious and the legitimate measurements, then, lead to a time to alarm difference $\Delta \tau_{T_{L, \text { cold }}}$ equal to 66 s (larger than $\Gamma_{T_{L, \text { cold }}}^{r e f}$ ) between the threshold exceedance of $S_{\text {T, cold }}^{f e e d}(t)$ and $S_{\text {T,cold }}^{\text {monitor }}(t)$ (see Fig. 7(b)), allowing for a (correct) identification of the event as a cyber attack.
![img-6.jpeg](img-6.jpeg)

Fig. 7 Cyber attack to the computing unit mimicking a bias failure mode: (a) the received measurements $T_{\text {L,cold }}^{\text {feed }}(t)$ and $T_{\text {L,cold }}^{\text {monitor }}(t)$ of feed and monitor Subsystems in which the cyber attack occurs at time $t_{R}$ equal to 630s; (b) the corresponding NP-CUSUM statistics $S_{\text {L,cold }}^{\text {feed }}(t)$ and $S_{\text {L,cold }}^{\text {monitor }}(t)$ for diagnosing the cyber attack

# 3. PERFORMANCE OF THE DIAGNOSTIC TOOL 

The NP-CUSUM-based diagnostic is eventually interpreted by human operators, for decision-making on the action to take. The overall performance of the procedure depends on both the capability and the human operator interpretation of the diagnostic outcomes. The human cognition process for diagnostic interpretation is here modelled by BBN to structure the expert knowledge and the dependences among human factors described by Performance Shaping Factors (PSFs) [28, 30, 31, 49-53].

### 3.1 Human operator cognition BBN

The operator cognitive process for interpreting the diagnostic outcomes can be divided into three successive phases [29, 30, 48, 73, 74], namely: (1)

monitoring/detection (i.e., the operator observes the real-time information collected from the HMIs), (2) situation assessment (i.e., the operator develops his/her mental representation of the specific current situation) and (3) response planning (i.e., the operator takes decisions for counteracting the current situation).

When an online diagnostic outcome arrives, the operator develops his/her cognition relying on both the current understanding of the system conditions and its mental representation founded on his/her formal education, system-specific training, and operational experience, namely, the knowledge base available to the operator [75]. The operator current understanding of the real-time system observations influences his/her performance in all three phases (1), (2) and (3), whereas the mental representation responding to the specific diagnostic outcome affects his/her performance at phases (2) and (3). Besides, context variables, such as the system situation level, the human mental level and the human stress level, may impede the operator from completing the diagnostic task [30, 53, 76], as sketched in Fig. 8.
![img-7.jpeg](img-7.jpeg)

Fig. 8 The operator cognitive activity in diagnosing anomalies

To model this, the BBN of Fig. 9 contains the PSFs [30, 77] "Work process", "Diagnosis experience/training" and "Fitness of duty" (related to the operator

diagnostic knowledge base and pertaining to the human mental model), "Available diagnosis time", "Diagnosis complexity" (dependent on the states of "Diagnosis procedure" and "HMI") and "System situation level" (related to the operator understanding of the real-time system observations and, thus, identified as characteristics of the human stress model), "HMI" and "Indication of condition" (related to the system current conditions and, thus, belonging to "System situation level"). Note that the PSF "Indication of condition" is specifically introduced here for the first time, for accounting the possible failure of the human operator cognitive process in the interpretation of the data-driven diagnostic outcomes (component failures or cyber attacks).

Throughout the process, the operator performance is affected by his/her mental and stress levels depending on the diagnostic outcomes received that reflect the system situation [30, 53, 76]. Table 3 lists the PSFs with the respective levels and descriptions, whereas Fig. 9 shows the BBN model that structures, based on expert judgment [51, 78], the relationships (indicated by the arcs) among the PSFs parent nodes $n_{p}^{\alpha}, \alpha=1$, $2, \ldots, 7$, and the child nodes $n_{c}^{\beta}, \beta=1,2, \ldots, 5$, representing the operator cognitive activity, finally, determining the diagnosed state of the system as state in normal condition, under cyber attack or failed due to sensor failures.

In the BBN model, each node represents a random variable associated with discrete states, labeled as $S_{p}^{\alpha, \gamma}$ (for parent node) and $S_{c}^{\beta, \gamma}$ (for child node), hereby $\gamma=1$, 2, 3 (see Fig. 9). The parent nodes $n_{p}^{\alpha}, \alpha=1,2, \ldots, 6$, are assigned with marginal probability distributions, $p\left(S_{p}^{\alpha, \gamma} \mid j\right)\left(\sum_{\gamma=1}^{3} p\left(S_{p}^{\alpha, \gamma} \mid j\right)=1\right)$, conditional on the operator experience to different accidental events $j$ (i.e., sensor failure $(j=\mathrm{a})$, cyber attack $(j=\mathrm{b})$, or normal condition (including missed alarm) $(j=\mathrm{c})$ ). The NP-CUSUM data-driven diagnostic provides the operator with the current specific indication of condition (i.e., $S_{p}^{7, \gamma}=i$, i.e., sensor failure $(i=\mathrm{a})$, cyber attack $(i=\mathrm{b})$, or normal condition (including missed alarm) $(i=\mathrm{c})$ ), such that the marginal distribution of $n_{?}^{\alpha}$ is assigned to be $p\left(S_{p}^{7, \gamma}=i\right)=1$ and $p\left(S_{p}^{7, \gamma} \neq i\right)=0$, given for a specific data-driven diagnostic

outcome $i$. The relationships between nodes, namely, the probabilities of the states of the child nodes for each possible combination of its parent(s) states, are described in the form of Conditional Probability Distributions (CPDs). The CPDs for each child node are distributed in the Conditional Probability Tables (CPTs).

Once the marginal probability distributions $p\left(S_{p}^{\alpha, \gamma} \mid j\right), \alpha=1,2, \ldots, 6, \gamma=1,2,3$, and the CPTs of the child nodes are assigned, the BBN model of Fig. 9 allows calculating the conditional probabilities $p\left(S_{c}^{1, \gamma}=k \mid j, i\right)$ (hereafter referred to $p(k \mid j, i)$ ) of the operator diagnosing the event $k$ to finalize as sensor failure $(k=\mathrm{a})$, cyber attack $(k=\mathrm{b})$, or normal condition (including missed alarm) $(k=\mathrm{c})$, conditional on the combination $(j, i)$ between the NP-CUSUM assignment $i$ and the real accidental event $j$.

As discussed in [15], the NP-CUSUM algorithm may suffer from either a large false alarm rate, if the threshold is set too small (type I error), or a high missed alarm rate, if the threshold is set too large (type II error). The operator may rectify the misclassification of the data-driven diagnostic with $p(k=j \mid j, i \neq j)$, or erroneously respond to a correct data-driven diagnostic with $p(k \neq j \mid j, i=j)[48,79]$.

![img-8.jpeg](img-8.jpeg)

*Fig. 9 The BBN model describing the human operator cognition process for final diagnostic*

Table 3 PSFs affecting the human operator cognition

Normal;
Poor. | The way to diagnose anomalies, e.g., coordination and communication between operators, management support, strategy handling given situations, and corrective action programs, etc. [80-82].  |
Normal;
Low. | The operator knowledge base, experience and training related to the diagnostic task [82].  |
Degraded;
Unfit. | The operator physical and mental fitness to perform the diagnosis task at the time $[80,82]$.  |
Normal;
Inadequate. | The operator available time to diagnose an abnormal event [82].  |
Normal;
Incomplete. | The existence of feasible procedures for the diagnosis and response planning tasks [82, 83].  |
Normal;
Misleading. | The availability of real-time physical information from Human-Machine Interfaces (HMIs) for the operator to carry out the diagnostic task [82].  |
Normal;
Misleading. | The availability of real-time physical information from HMIs for the operator to carry out the diagnostic task [82].  |
$i=b$;
$i=c$. | The clarity of the data-driven diagnostic indications that assist the operator in diagnosing the anomaly [84].  |

Note: $\alpha=1,2,3,4,5,6$ or 7 for parent nodes; $\beta=1,2,3,4$ or 5 for child nodes; $\gamma=1,2$ or 3 for all the nodes;

# 3.2 Overall diagnostic performance 

With reference to a recorded event $j$, the human operator correctly diagnoses the event when his/her assignment $k$ is consistent with $j$, even if the data-driven diagnostic indicates a misclassified system state $i$. Vice versa, if the operator indication $k$ is not consistent with the event $j$, an incorrect diagnostic of the accidental event is made by the operator, regardless of the correctness of the data-driven assignment $i$.

Table 4 summarizes all possible human operator assignments $k$ of the event $j$, with respect to the different data-driven diagnostic assignments $i$. In the Table, conditional on the assignment $i$, the correct diagnostic of the event is tagged by the symbol " $\sqrt{ }$ " (see Column 4), with a conditional probability equal to $p(j, k=j \mid i)$, where $i, j, k=\mathrm{a}, \mathrm{b}$ or c (see Column 5), whereas, the incorrect diagnostic of the event is tagged by the symbol " $x$ ", with a conditional probability equal to $p(j, k \neq j \mid i)$, where $i, j, k=\mathrm{a}, \mathrm{b}$ or c (see Column 5).

In the end, only the consistency of the human operator assignment $k$ with the event $j$ gives a correct diagnostic: then, the probability of correct diagnostic $p_{\text {correct }}^{i}$, conditional on the data-driven diagnostic $i$, is obtained by summing the probabilities of the occurrences tagged by " $\sqrt{ }$ " in Table 4.

$$
p_{\text {correct }}^{i}=\sum_{j=k=a}^{c} p(j, k=j \mid i)
$$

According to the chain rule of conditional probability [85], Eq. (3) can change to:

$$
p_{\text {correct }}^{i}=\sum_{j=k=a}^{c} p(k=j \mid j, i) \cdot p(j \mid i)
$$

where $p(j \mid i)$ is the probability that the event is $j$, when the data-driven diagnostic is $i$ (i.e., the probability of correct diagnosis of the data-driven algorithm if $j=i$ ). This represents the performance of the data-driven diagnostic, which, as discussed in [15], can be empirically estimated from $N_{v}$ tests of (unknown) failures and cyber attacks. On the other hand, $p(k=j \mid j, i)$ is the ability of the operator to interpret the diagnostic outcome $i$ and correctly assign his/her diagnostic $k$ consistent with the occurred event $j$, i.e., $k=j$.

Table 4 All possible diagnostic assignments


Notes:

1) hereafter "a" refers to "sensor failure", "b" refers to "cyber attack", and "c" refers to "normal condition" (including missed alarm);
2) " $\checkmark$ " refers to correct diagnostic, and " $\times$ " refers to incorrect diagnostic.

To practically calculate the overall performance $p_{\text {correct }}^{i}$ for different data-driven diagnostic $i$, a general MC approach (sketched in Fig. 10) is proposed in line with [52, 86] for populating the CPTs at the child nodes of the operator BBN. We proceed as follows:

At the $m$-th MC run, $m=1,2, \ldots, N_{m}$ :
(1) Set the distributions of PSFs for each event $j=a, b$ or $c$ (see Appendix A), i.e., the operator knowledge and experience, relative to the class of events $j$;
(2) Set $i=a, b$ or $c$, and the evidence of the parent node $s_{p}^{7, \gamma}$ as equal to $i$, i.e., $p\left(s_{p}^{7, \gamma}=i\right)=1$ and $p\left(s_{p}^{7, \gamma} \neq i\right)=0$;

(3) Sample the CPDs (i.e., $p_{m}\left(s_{p}^{\alpha, \gamma}\right)$, the conditional probability of the states $s_{p}^{x, \gamma}$ ) of the parent nodes $n_{p}^{\alpha}, \alpha=1,2,3,4,5,6$, from the related distributions;
(4) Populate the CPTs of the child nodes $n_{c}^{\beta}$ by use of the five-step functional interpolation method $[52,86]$ :
(4a) Sample the mean and standard deviation values $\left(u\left(e_{c}^{\beta, \theta}\right)\right.$ or/and $\sigma\left(e_{c}^{\beta, \theta}\right)$, where $e_{c}^{\beta, \theta=\text { anchor }}$ are the selected anchors at the anchor CPT of the child node $n_{c}^{\beta}$, from the expert-judged distributions (see Appendix B);
(4b) Linearly interpolate the missing mean and standard deviation values $\left(u\left(e_{c}^{\beta \text {,other }}\right)\right.$ or/and $\left.\sigma\left(e_{c}^{\beta \text {,other }}\right)\right)$ of the other elements at the anchor CPT of $n_{c}^{\beta}$ and then:
(4c) Assign the normal distribution $N\left(u\left(e_{c}^{\beta, \theta}\right), \sigma\left(e_{c}^{\beta, \theta}\right)\right)$ to the $\theta$-th element of the $\beta$-th child node $n_{c}^{\beta} \mathrm{CPT}, \beta=1,2, \ldots, 5$, and assign the states $s_{c}^{\beta, \gamma}$ of the child node $n_{c}^{\beta}$ with the $N\left(u\left(e_{c}^{\beta, \theta}\right), \sigma\left(e_{c}^{\beta, \theta}\right)\right)$ pdf values at the $s_{c}^{\beta, \gamma}$ states anchor values (i.e., $\gamma$ assigned equal to 1,2 (and 3), respectively (see Appendix B)), being the conditional probability scales of $s_{c}^{\beta, \gamma}$ in $e_{c}^{\beta, \theta}$, i.e., $\eta\left(s_{c}^{\beta, \gamma} \mid e_{c}^{\beta, \theta}\right)$;
(4d) Normalize $\sum_{\gamma} \eta\left(s_{c}^{\beta, \gamma} \mid e_{c}^{\beta, \theta}\right)$ to 1 , leading the scale values to being the conditional probabilities of the $s_{c}^{\beta, \gamma}$ states, i.e., $p\left(s_{c}^{\beta, \gamma} \mid e_{c}^{\beta, \theta}\right)$, in the $\theta$-th element of the child node $n_{c}^{\beta} \mathrm{CPT}$;
(4e) Collect the CPDs of all the elements and, build the CPTs for the $n_{c}^{\beta}$ child node;
(5) Quantify the BBN model with the sampled CPDs of parent nodes and CPTs of child nodes, and estimate the operator correct diagnostic probability

$p_{m}(k=j \mid j, i)$ conditional on the combination $(j, i)$ with current assigned values of $j$ and $i$;
(6) Repeat steps (1) to (5), and collect the estimates of $p_{m}(k=j \mid j, i)$ for the nine combinations $(j, i):(a, a),(a, b),(a, c),(b, a),(b, b),(b, c),(c, a),(c, b)$ and $(c, c)$;
(7) Feed $p_{m}(k=j \mid j, i)$ and the tested $p(j \mid i)$ values to Eq. (4), to obtain the estimates of the performance $p_{\text {correct }, m}^{i}$, with respect to the different datadriven diagnostic indications $i$.

Repeat steps (1) to (7) for $N_{m}$ times, and obtain the confidence intervals of the $p_{\text {correct }}^{i}$, with respect to different data-driven diagnostic $i$.

![img-9.jpeg](img-9.jpeg)

![img-10.jpeg](img-10.jpeg)

*Fig. 10 The flowchart for estimating the diagnostic performance*

# 4. RESULTS 

We generated $389 T_{L, \text { cold }}$ transients due to sensor failures, 392 transients due to DoS attacks and 219 transients of normal operation scenarios out of a total of $N_{v}=1000$ tests scenarios of ALFRED evolution. At each test scenario $j$, the NP-CUSUM-based diagnostic algorithm is applied to both $T_{\text {L,cold }}^{\text {feed }}(t)$ and $T_{\text {L,cold }}^{\text {monitor }}(t)$ to calculate $S_{T_{\text {L,cold }}}^{\text {feed }}(t)$ and $S_{\text {L,cold }}^{\text {monitor }}(t)$, respectively, with the NP-CUSUM parameters randomly sampled from their distributions listed in Table 5.

Table 5 Parameters of the NP-CUSUM algorithm


Table 6 collects the number of the data-driven diagnostic outputs, and lists the estimates of $p(j \mid i)$ : the data-driven diagnostic classifies the $N_{v}$ tests into 386 sensor failures (a), 386 DoS attacks (b) and 228 normal condition (c), resulting in probabilities of correct assignment $p(j=i \mid i)$ equal to $0.9611,0.9819$ and 0.8772 , respectively. It is worth noting that $p(j=c \mid i=c)$ is smaller than $p(j=a \mid i=a)$ and $p(j=b \mid i=b)$, because the NP-CUSUM algorithm suffers of a relatively high missed alarm rate when the occurring events negligibly affect the controlled variables and the system functionality.

Table 6 Performance of the NP-CUSUM diagnostic


The operator cognitive errors in interpreting the diagnostic outcomes have been

calculated as discussed in Section 3.2, by running the operator cognition BBN of Fig. 9: the correct diagnostic probability $p_{\text {correct }}^{i}$, given data-driven diagnostic $i(=a, b$ or $c$ ) is calculated according to Eq. (4), after $N_{m}=1000$ runs, along with the double-sided $95 \%$ confidence intervals of $p_{\text {correct }}^{i}$. As shown in Fig. 11, the mean values of $p_{\text {correct }}^{i}$ (circles in Fig. 11) turn out to be equal to $0.966,0.923$ and 0.943 , with respect to the different data-driven diagnostic $i$ (i.e., $T_{L \text {.cold }}$ sensor failures (a), DoS attacks (b) and normal conditions including missed alarms (c), respectively).
![img-11.jpeg](img-11.jpeg)

Fig. 11 Estimates of the double-sided 95\% confidence intervals of the correct diagnostic probabilities

The results of Fig. 11 show that the mean values of $p_{\text {correct }}^{a}$ (equal to 0.966 ) and $p_{\text {correct }}^{c}$ (equal to 0.943 ) are respectively larger than $p(j=a \mid i=a)$ (equal to 0.961 ) and $p(j=c \mid i=c)$ (equal to 0.877 ) (stars in Fig. 11). This shows that in these cases the operator expertise increases the performance of the data-driven algorithm by correcting events that were misclassified by the NP-CUSUM. The confidence interval of $p_{\text {correct }}^{b}$ turns out to be large and its mean value (equal to 0.923 ) turns out to be smaller than the performance of the data-driven diagnostic tool $(p(j=b \mid i=b)$ equal to 0.982 labeled as star in Fig. 11). Conversely, this shows that, in this case, the lack of operators experience in correctly interpreting the NP-CUSUM outcome results in mistaking the diagnostic and in worsening the diagnosis performance with respect to cyber attacks.

Furthermore, we have repeated the analysis by running $N_{m}=1000$ runs of the BBN,

assuming a fully skilled operator with respect to diagnosing cyber attack events, i.e., $p\left(s_{p}^{2.1} \mid i=b\right)=1$. Double-sided $95 \%$ confidence intervals of the correct diagnostic probabilities $p_{\text {correct }}^{i}$ with respect to the different data-driven diagnostics $i$ (i.e., $a, b$ and $c$, respectively) are shown in solid lines in Fig. 11: the confidence interval of $p_{\text {correct }}^{b}$ turns out to be narrower and its mean value (equal to 0.988 ) (diamond in Fig. 11) turns out to be larger than the performance of the data-driven diagnostic (equal to 0.982 ), as expected.

# 5. CONCLUSIONS 

In this study, we have proposed a framework for the discrimination analysis of cyber attacks and component failures in Cyber-Physical Systems (CPSs). The framework combines, for the first time, a data-driven diagnostic approach (NonParametric CUmulative SUM (NP-CUSUM), in this case) with a Bayesian Belief Network (BBN) that is originally tailored to model the human operator cognition process of interpreting the diagnostic outcomes. The BBN is used to structure the expert knowledge and other factors (in particular, the indication of the data-driven diagnostic outcomes) that influence the human cognition process for diagnostic.

In the application, the work contributes to the process of enabling the interaction between data-driven diagnostic systems and human operators actions for supporting operator decisions with respect to cyber attacks in CPSs, with the aim of reducing false alarms, missed alarms, or misclassifications of cyber attacks as components failures, and vice versa.

We have illustrated the work considering the digital Instrumentation and Control (I\&C) system of the Advanced Lead-cooled Fast Reactor European Demonstrator (ALFRED). The results of the case study show that the proposed diagnostic approach is capable of identifying most of the generated failure/attack scenarios, with low frequency of misclassifications, and that, in the case considered, the operator increases the diagnosis performance for sensors failures, but not for cyber attacks. The results persuasively demonstrate that cyber attacks are less diagnosable compared to

components failures.
A simplistic assumption is done that cyber attacks occur at random times from the viewpoint of the defender; in reality, attacker is likely to launch cyber attacks at preferred times when his/her objectives can be maximized and the investment minimized. This challenges the diagnostic task, and therefore, with due caution, future work will regard the role of the attacker decision making (e.g., based on a cost benefit analysis) for choosing the optimal time of attack.

# APPENDIX A 

With respect to the events of sensor failure $(j=\mathrm{a})$ and normal conditions (including missed alarms, $j=\mathrm{c}$ ), the probability distributions of the PSF states $p\left(s_{p}^{\alpha, \gamma} \mid j\right), \alpha=$ $1,2, \cdots, 6, \gamma=1,2,3$, are taken as uniform (see Table A1), according to expert judgment, whose mean values are given [87]. Under DoS attack events $(j=\mathrm{b})$, the operator is assumed to be less experienced $\left(n_{p}^{2}\right)$ and the diagnosis procedure $\left(n_{p}^{5}\right)$ relatively incomplete, such that the probability distributions $p\left(s_{p}^{2, \gamma} \mid j=b\right)$ and $p\left(s_{p}^{5, \gamma} \mid j=b\right)$ result in those in the last column of Table A1.

It us worth mentioning that, with respect to the MC simulation presented in Section 3.2, the sampled values from the distributions of $p\left(s_{p}^{\alpha, \gamma} \mid j\right), \gamma=1,2,3$, for each parent node $n_{p}^{\alpha}$, given an event $j$, are normalized to the sum equal to 1 (i.e., $\sum_{\gamma=1}^{3} p\left(s_{p}^{\alpha, \gamma} \mid j\right)=$ 1 , given an $\alpha$ and $\mathrm{a} j$ ).

Table A1 Identification of probability distributions for the states of PSFs


# APPENDIX B 

As suggested in [52], we build the anchor CPTs for the child nodes $n_{c}^{\beta}(\beta=1,2$, $3,4,5)$ of the BBN model of Fig. 9, as listed in Tables A2 to A6, respectively. In each Table, the anchor elements are shaded with the expert-judged values or/and distributions of the means and standard deviations (i.e., $u\left(e_{c}^{\beta, \theta=\text { anchor }}\right)$ or/and $\sigma\left(e_{c}^{\beta, \theta=\text { anchor }}\right)$ ). It is noticed that the states of the child nodes $s_{c}^{\beta, \gamma}$ are assigned with the anchor values equal to 1,2 (and 3 ) for identifying the corresponding CPD scales (i.e., pdf values at the anchor values equal to 1,2 (and 3 )), once the uniform distributions at all the elements of the anchor CPTs are generated.

Table A2 The anchor CPT of $n_{c}^{2}$ (Human cognition beliefs)

situation
level | Negligible | $\begin{aligned} & 1.00 ; \ & U[0.20,0.30] \end{aligned}$ |  | $\begin{aligned} & U[1.20,1.50] ; \ & U[0.20,0.40] \end{aligned}$ |  |  |  | $\begin{aligned} & U[1.20,1.50] ; \ & U[0.20,0.25] \end{aligned}$ |  | $\begin{aligned} & 2.00 ; \ & U[0.50,0.70] \end{aligned}$  |

Note:

1) In each shaded anchor element, the first value/distribution refers to the mean value/distribution and, the second one refers to the standard deviation value/distribution; 2) The $n_{c}^{2}$ states $s_{c}^{2, \mathrm{p}}$, correct (i.e., $k \neq j$ ) and incorrect (i.e., $k \neq j$ ) diagnostic are assigned with the anchor values $\gamma$ equal to 1 and 2 , respectively.

Table A3 The anchor CPT of $n_{c}^{2}$ (Human mental level)


Note:

1) In each shaded anchor element, the value refers to the mean value and, the distribution refers to the standard deviation distribution; 2) The $n_{c}^{2}$ states $s_{c}^{2, \mathrm{p}}$, Normal, Moderate and Bad are assigned with the anchor values $\gamma$ equal to 1,2 and 3 , respectively.

Table A4 The anchor CPT of $n_{c}^{3}$ (Human stress level)

situation
level | Negligible | $\begin{aligned} & 1.00 ; \ & \mathrm{U}[0.20,0.30] \end{aligned}$ |  | $\begin{aligned} & 2.00 ; \ & \mathrm{U}[0.20,0.40] \end{aligned}$ |  |  |  | $\begin{aligned} & 1.00 ; \ & \mathrm{U}[0.50,0.80] \end{aligned}$ |  | $\begin{aligned} & 3.00 ; \ & \mathrm{U}[0.70,1.00] \end{aligned}$  |

Note:

1) In each shaded anchor element, the value refers to the mean value and, the distribution refers to the standard deviation distribution; 2) The $n_{c}^{3}$ states $s_{c}^{3, \gamma}$, Low, Moderate and High are assigned with the anchor values $\gamma$ equal to 1,2 and 3 , respectively.

Table A5 The anchor CPT of $n_{c}^{4}$ (System situation level)


Note:

1) In each shaded anchor element, the value refers to the mean value and, the distribution refers to the standard deviation distribution; 2) The $n_{c}^{4}$ states $s_{c}^{4, \gamma}$, Negligible, Moderate and Severe are assigned with the anchor values $\gamma$ equal to 1,2 and 3 , respectively.

Table A6 The anchor CPT of $n_{c}^{5}$ (Diagnosis complexity)


Note:

1) In each shaded anchor element, the value refers to the mean value and, the distribution refers to the standard deviation distribution; 2) The $n_{c}^{5}$ states $s_{c}^{5, \gamma}$, Obvious, Normal and Complex are assigned with the anchor values $\gamma$ equal to 1,2 and 3 , respectively.
