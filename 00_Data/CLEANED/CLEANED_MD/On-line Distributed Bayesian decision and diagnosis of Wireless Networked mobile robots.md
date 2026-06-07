# HAL open science 

## On-line Distributed Bayesian Decision and Diagnosis of Wireless Networked Mobile Robots

Amine Mechraoui, Jean-Marc Thiriet, Sylviane Gentil

## To cite this version:

Amine Mechraoui, Jean-Marc Thiriet, Sylviane Gentil. On-line Distributed Bayesian Decision and Diagnosis of Wireless Networked Mobile Robots. MED 2010 - 18th Mediterranean Conference on Control and Automation, Jun 2010, Marrakech, Morocco. pp.598-603, 10.1109/MED.2010.5547735 . hal-00529299

## HAL Id: hal-00529299 <br> https://hal.science/hal-00529299v1

Submitted on 25 Oct 2010

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# On-line Distributed Bayesian Decision and Diagnosis of Wireless Networked Mobile Robots 

Amine MECHRAOUI, Jean-Marc THIRIET and Sylviane GENTIL


#### Abstract

This paper deals with the problem of co-design of Wireless Networked Control systems (WNCS). The integration of the Wireless Network (WN) in the control loop influences the Quality of Control (QoC) of the system in terms of the Quality of Service (QoS) of the WN. In this paper, a new model of the QoS and its influence on the QoC is proposed. This model is based on a distributed Bayesian Network (BN). The main objective of this model is to diagnose on-line problems related to the QoS and the QoC. According to the diagnosis results and the situation, the system makes on-line decision to reconfigure both the WN in a multi-station environment and the controller in order to avoid the degradation of the QoC. This reconfiguration is justified by the need of adapting the WN to the requirements of the control and diagnosis, and also adapting the control and diagnosis to the capabilities of the WN. The proposed reconfiguration permits to guarantee a sufficient QoC under network limits.


Index Terms-Wireless networked control system, IEEE 802.11, Distributed Bayesian network, Distributed diagnosis, Decision making, Reconfiguration, Mobile robot, Quality of Service, Quality of Control.

## I. INTRODUCTION

Nowadays Networked Control Systems (NCS) is an emerging domain, especially in robotics, which is receiving increasing attention. Introducing a wireless network in control loops presents some disadvantages due to band limited channels, sampling delays and packet dropouts [1]. Furthermore, the mobility in robotic applications also adds some problems, e.g. increasing the distance between the control station and the mobile increases the number of lost packets due to decreased signal strength and increased bit error rate [2].
The communication architecture in mobile robotics may be centralized, in which case there is a fixed or mobile node that communicates with all the other nodes, or decentralized, where individual mobile nodes should ideally operate without any central control [3]. In the decentralized control scheme, each component solves a part of the problem and shares memory without having a global view of the mission. There is less emphasis on computation than communication. In distributed control systems, communication is an important parameter and individual components don't need to share memory [4].
In the literature, several studies are focused only on the Quality of Service (QoS) (capability of a network to provide and guarantee a sufficient service to such application)

[^0]without treating its influence on the Quality of Control (QoC) (performance such as stability, error and response time) [5]. However, other studies are focused on the QoC and consider the network as only a time-varying delay without taking into account the other parameters influencing the QoC [6]. This paper takes both into account in a co-design approach. The reconfiguration of the wireless network is required to fulfill the need of control in the case of degradation of the QoC. The adaptation of control is required too in the case of the degradation of the QoS of the network.
The causality between the different parameters of the wireless network on one hand and the QoS and the QoC on the other hand can be modeled with a graph. According to the stochastic aspect of wireless networks, we propose in this paper to use Bayesian Network (BN) [7], [8] because it brings graph theory and probability theory together. BN is used in this paper to diagnose the WNCS and to make on-line decision to avoid both degradation of the QoS and the QoC. Our ideas are illustrated with two mobile robots moving in a 2D space with n fixed control stations.
The paper is organized as follows. The second section presents a brief description of the model of the Khepera robot. The controller design and the control over a wireless network in the case of one and several robots are presented. Section III presents the proposed model based on Bayesian Network to represent the QoS and its influence on the QoC. The diagnosis using BN and decision making algorithms are presented too. After that, the proposed approach is applied to diagnose faults and two scenarios are simulated and the obtained results are discussed. Finally, a conclusion and further work are given in section V.
In this paper, the robots are simulated with Matlab/Simulink, the wireless network with TrueTime [9] and the bayesian network with the Bayes Net ToolBox (BNT) [10].

## II. KHEPERA ROBOT MODELING AND CONTROL OVER WIRELESS NETWORK

## A. Basic explication

This section presents the study of a unicycle Khepera robot [11] and its control to reach a target. Consider a unicycle robot as shown in Fig. 1. Let $\mathrm{x}, \mathrm{y}$ and $\theta$ be the state variables where $x \in \Re$ and $y \in \Re$ are the Cartesian coordinates, $\theta \in[0,2 \pi[$ is the robot's orientation with respect to the X -axis. $v$ and $\omega$ are respectively the linear and the angular velocities of the robot.
The kinematic model of the mobile robot has two control inputs $\omega_{l e f t}$ and $\omega_{\text {right }}$ i.e. the left and right wheels velocities. Two levels of controllers are required. The first one is needed


[^0]:    The authors are with control systems department, Gipsa-Lab UMR 5216, BP 46, 38402 Saint Martin d'Hères Cedex, France. email: [amine.mechraoui, jean-marc.thiriet, sylviane.gentil] @gipsalab.grenoble-inp.fr

![img-0.jpeg](img-0.jpeg)

Fig. 1. Robot Model

to control the angular velocities of the wheels. PI controllers are implemented. The second one controls the linear and angular velocities of the robot (*v* and *ω* respectively). The controller presented in [12] has been used for this task. The robot must reach a desired target point [*x_{d}* *y_{d}* *θ_{d}*]. The desired control references *ω_{left}* and *ω_{right}* of each motor local control loop are calculated. The measures *x_{mes}*, *y_{mes}* and *θ_{mes}* are provided by odometry using encoder sensors of each motor. The controller is discretized and a Wifi wireless network is integrated (see Fig. 3). We have used WLAN 802.11 b/g that is a part of 802.11 specifications which describe the characteristics of a wireless local area network (WLAN). The basic access mechanism used in this article, called Distributed Coordination Function (DCF), is basically a Carrier Sense Multiple Access with Collision Avoidance (CSMA/CA) [13].

### *B. Simulation condition*

The main control loop of each robot is closed through the Wifi network (Fig. 3). The results presented in this paper are obtained using Matlab/Simulink for the simulation of the robot and the control laws.

TrueTime simulator is used to simulate the Wifi Network.


![img-1.jpeg](img-1.jpeg)

Fig. 2. General control architecture

![img-2.jpeg](img-2.jpeg)

Fig. 3. Control over wireless network of the two robots and one control station

Two tasks are programmed. The first is the controller task that generates the controller flow and the second one is a periodic sensor task that generates sensors flow with a sampling period of *T_{e}* = 0.4*s*. The controller task is event-triggered, which means that the controller calculates and sends the control signals *v* and *ω* only when it has received all measures *x_{mes}*, *y_{mes}* and *θ_{mes}*. To perform this study, the conditions in Table I are considered.

*1) Multi-robot control via the wireless network:* The control of several robots via the wireless network is done by adding other tasks within the control station. One sensor task is programmed for each robot (Fig. 3). As the sensor tasks are time-triggered, they begin at the same time and collision occurs and delay increases which increases also the probability of packet loss. To avoid collision and packet loss, an offset is added to the moment of launching of each sensor task of each robot. This offset attributes the triggering time of sensor task priority to each robot. Trajectories, orientations, linear and angular velocities of the two robots are shown in Fig. 4. In this figure, the initial position of *Robot_{1}* is (*x_{0}^{1}*, *y_{0}^{1}*, *θ_{0}^{1}*) = (0, 0, 0) and it should reach a desired target (*x_{d}^{1}*, *y_{d}^{1}*) = (2, 2). The initial position of *Robot_{2}* is (*x_{0}^{2}*, *y_{0}^{2}*, *θ_{0}^{2}*) = (5, 5, −*γ^{2}*) and it should reach a target (*x_{d}^{2}*, *y_{d}^{2}*) = (3, 3) (We consider those initial conditions for all simulations within this paper). The two robots reach their respective targets in 30*s*, and the linear velocity profile of the two mobiles are the same.

*2) Degraded mode:* The communication between the robot and the control station is not ensured according to the level of the QoS. Therefore, a degraded mode is possible to guarantee at least a degraded QoC. In this case, the same control laws are programmed within the robot (embedded) but with a sampling period of *T_{e} = 1*s*. The decision algorithm to switch the controller is presented in the next section.

# III. BAYESIAN NETWORK REPRESENTATION OF THE WNCS PROPERTIES

### *A. Definition of BN*

A Bayesian Network is a probabilistic graphical model defined by [8] as:

![img-3.jpeg](img-3.jpeg)

Fig. 4. Trajectories, orientations, linear and angular velocities of the two robots using control over wireless network within the nominal case

TABLE II


TABLE III


- a directed acyclic graph $G, G \equiv(V, E)$, where $V$ is the set of nodes of $G$, and $E$ is the set of edges of $G$;
- a finite probabilised space $(\Omega, Z, P)$;
- a set of random variables associated to the nodes of the graph and defined on $(\Omega, Z, P)$, such that:

$$ P\left(V_{1}, V_{2}, \ldots, V_{n}\right)=\prod_{i=1}^{n} P\left(V_{i} \mid C\left(V_{i}\right)\right) $$

where $C\left(V_{i}\right)$ is the set of causes (parents) of $V_{i}$ on the graph $G$.

## B. Modeling the QoS and the QoC of the WNCS

The model of the QoS and the QoC of the WNCS using BN is used to diagnose the degradation cause of the QoC of each robot and also of the QoS of the Wireless network. Variables of the proposed BN are shown in Table II. The modes of each node are presented in Table III. To model the QoS and the QoC of the system presented in section II, two steps are required. The first is the qualitative step, that allows, according to causal relations between the different variables of the system under study, to model the system as an acyclic oriented graph. This graph is completed by the conditional probabilities (quantitative step) for each node of the graph. A priori probabilities of the BN are obtained using a statistical study of results obtained with TrueTime Simulator. These two steps are described in [14]. In view of the fact that a BN needs a lot of memory to compute all a posteriori probabilities of each node, the robot cannot support this computation. Hence, we decided to distribute the BN between the robot and the control station. Fig. 5 shows the distributed BN. Indeed, the nodes QoC, QoS and the state of the robot (R) are programmed in the robot. The rest of the graph is programmed in the control station. The causal relation between the QoS and packet loss are obtained via the wireless network. The node QoS in the control station computes its marginal probability $(P(Q o S))$ and sends it to the node QoS which is programmed in the robot. This node updates its probability according to the message sent by the station and updates consequently all the variables in the BN in the robot. The node QoS in the robot sends message to the one in the control station. This message is calculated by using the marginal law (Eq.2), the Bayes theorem (Eq.3) and the d-separation property [8]. The marginal law used to calculate the marginal probability in the BN is:

$$ P(A)=\sum_{B} P(A, B) $$

and the well known Bayes formula:

$$ P(A \mid B)=\frac{P(B \mid A) P(A)}{P(B)} $$

The d-separation property is used to determine whether a set of nodes $X$ is independent of another set $Y$, given a set of evidence nodes $E$ (for more information see [8]). This property decreases the size and time of computation. To program the BN on-line in the simulator, the toolbox BNT is used to calculate a posteriori probabilities of each node and thus to diagnose the origin of the degradation of the QoC and the QoS. As the proposed BN is a tree, the Junction Tree algorithm is chosen to make bayesian inference within the BN [15]. The influence of the QoS on the QoC is represented in the BN by the conditional probabilities and the influence of the QoC on the QoS is given by the inference in the BN.

## C. Making decision and diagnosis

After modeling the BN and defining all a priori probabilities, the acyclic graph can be used to diagnose the cause of the degradation of the QoC and the QoS and making decision to avoid this degradation of both the QoS and the QoC. To

diagnose the cause of degradation of the QoC, the BN needs information about the QoC. Indeed, to know on-line if the QoC is good, degraded or bad, a QoC criterion is proposed according to Algorithm 1. This algorithm gives the evidence concerning the QoC of the robot. If the distance between the robot and the station increases, the QoC is considered as bad. Now, if the distance decreases, we verify the orientation error. If the orientation error decreases, then the QoC is good, else the QoC is degraded. Using this algorithm, we can calculate the probability of such state of the QoC. Fig. 6 shows the probability of each state (good, degraded or bad) in the best scenario (good QoS that guarantees a low probability of packet loss and collision). In this figure, there are two periods namely a transient period and a steady state. In the transient period, there is not enough information about the state of the QoC, therefore as we go along the probability that the QoC is good increases, in this case, with time and stretches to 1 in the steady state (Fig .6).

```
Algorithm 1 QoC criterion
    if \(d=0\) and \(d=0\) then
        \(Q o C=\) good
    else if \(d<0\) then
        if \(\hat{\theta}(k) \leq 0\) and \(\hat{\theta}(k-1) \leq 0\) then
            \(Q o C=\) good
        else
            \(Q o C=\) degraded
        end if
    else
        \(Q o C=\) bad
    end if
```

According to the information about the QoC and the situation, the robot decides to change the station with which it communicates if there is one that ensures a better QoC [16]. The robot can choose to switch the controller to the embedded one or to stop if it has no choice. The Algorithm 2 illustrates all situations to guarantee always a good QoC or at least a degraded one by reconfiguring either the Control or the wireless network.
In Algorithm 2, $S_{c}$ refers to the set of candidate stations.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Distributed Bayesian Network
![img-5.jpeg](img-5.jpeg)

Fig. 6. $\mathrm{P}(\mathrm{QoC})$ of the two robots in the best scenario

```
Algorithm 2 Decision algorithm
    if \(Q o C=\) bad and \(P(C o l=y e s) \geq C o l_{\text {Threshold }}\) and \(D<$
    \(D_{\text {Threshold }}\) and \(S_{c}=\Phi\) then
        Switch to embedded controller
    else if \(Q o C=\) bad and \(S_{c}=S_{j}\) then
        Execute Horizontal Handoff
    else
        Continue the communication with \(S_{i}\)
    end if
```


## IV. RESULTS AND SIMULATION

To verify the proposed algorithms and the efficiency of the proposed bayesian network either to diagnose or to make decision, two scenarios are presented.

## A. Scenario 1

In the first scenario, two robots communicate with one control station. Those robots are always within the coverage area of the station. Hence, the probability $P(D<$ $D_{\text {Threshold }}=1$ for each robot.
To limit the resource of the wireless network and study under the network limits, the rate of the wireless network is set to $400 b i t s / s$. With this rate, in the better case, the frames of the two sensor tasks of each robot and the controller task can be transmitted successfully. But, if there are collisions, the packets will be lost and hence the QoC will be degraded progressively until it becomes bad. Using Algorithm 1, the robot can qualify the QoC and propagate this information through the proposed BN. So, according to the available information, the BN can locate the cause of a possible degradation of the QoC and the QoS.
In this scenario, the two robots cannot communicate with the control station (see control task in Fig.10) and thus their QoC are bad (Fig.7), the two robots cannot reach a target. We can remark also, in Fig. 8, that the state of the QoC swings between degraded and bad.
During this scenario, the BN calculates the a posteriori probability $P\left(V_{i} \mid Q o C=b a d, D<D_{\text {Threshold }}\right)$ of each node using Bayes theorem, marginal law and joint law (where $V_{i}$ refers to each node of the BN). According to these

![img-6.jpeg](img-6.jpeg)

Fig. 7. Trajectory of the two robots with respect to time (X-axis and Y-axis) with initial position of the two robots (x₀₁, y₀₂, θ₀₁) = (0, 0, 0) and (x₀₂, y₀₂, θ₀₂) = (5, 5, −›₀₁) under network limits

![img-7.jpeg](img-7.jpeg)

Fig. 8. P(QoC) of the two robots in the case of network limits and collision

*a posteriori* probabilities, the most probable cause is that there was a collision with *P(Col = yes|QoC = bad, D < DThreshold) ≈ 0.9*. The *a posteriori* probability *P(Col|QoC = bad, D < DThreshold)* is calculated as

$$\begin{aligned}
P(Col|QoC &= bad, D < DThreshold) = \\
& P(QoC = bad, D < DThreshold|Col)P(Col) \\
& P(QoC = bad, D < DThreshold)
\end{aligned}$$

$$\begin{aligned}
P(QoC &= bad, D < DThreshold|Col) = \\
& \sum_{QoS} \sum_{R} \sum_{PP} \sum_{RSSI} \sum_{S} P(QoC, QoS, R, PP, RSSI, Obst, D, \Delta_t) \\
& \sum_{QoS} \sum_{R} \sum_{PP} \sum_{RSSI} \sum_{S} \sum_{Col} P(QoC, QoS, R, PP, RSSI, Obst, D, \Delta_t, Col)
\end{aligned}$$

$$\begin{aligned}
P(QoC &= bad, D < DThreshold) = \\
P(QoC &= bad|QoS, R, PP, RSSI, Obst, D, \Delta_t, Col) \times \\
P(D & < DThreshold)
\end{aligned}$$

![img-8.jpeg](img-8.jpeg)

Fig. 9. Trajectory of the two robots with respect to time (X-axis and Y-axis) with initial position of the two robots (x₀₁, y₀₂, θ₀₁) = (0, 0, 0) and (x₀₂, y₀₂, θ₀₂) = (5, 5, −›₀₁) under network limits and with the reconfiguration of the control and the communication architecture

After executing Algorithm 2 *Robot₁* decides at *t = 5s* to interrupt the communication with the control station and to reconfigure the control strategy and switch to the embedded degraded controller. With this strategy, the robot holds at least a degraded QoC and reaches the target (Fig. 9). On the other hand, *Robot₂* continues communication with the control station with a good QoS and QoC. Fig. 10 shows the sensor task of both robots before and after the reconfiguration of the controller. In this figure, we notice that after reconfiguring the control and communication architecture of the first robot, the probability of collision decreases and the control station receives the position of *Robot₂* and sends the desired linear and angular velocities to the second robot.

Within this scenario and under the same wireless network conditions, the two robots cannot reach their targets (Fig. 7) whereas with the co-design proposed reconfiguration, the two robots reach their target without problem (Fig. 9).

![img-9.jpeg](img-9.jpeg)

Fig. 10. Schedule of the two sensor tasks of the two robots and the control task

![img-10.jpeg](img-10.jpeg)

Fig. 11. Trajectories of the two robots with a sensor fault of *Robot<sub>1</sub>* at time *t = 5s*

### *B. Scenario 2*

In this scenario, we come back to the default rate of the WN (*rate = 800kbit/s*). We consider also that after *5s* of simulation, *Robot<sub>1</sub>* will be faulty. The fault is simulated by adding a step on *u<sub>right</sub> = 5rad/s* to the right wheel measure thus the QoC will be bad (see Fig.11). With the knowledge of the number of packet loss, the BN has localized the cause of the degradation of the QoC. After executing the bayesian inference, the BN has calculated the *a posteriori* probability *P(R = faulty|QoC = bad, QoS = good) = 1*. Therefore, the BN has localized and isolated the fault.

### V. CONCLUSIONS AND FUTURE WORKS

#### *A. Conclusions*

In this paper, a novel distributed based BN approach has been proposed to model the Quality of Service and the Quality of Control of Wireless Networked Control Systems. This model combines all parameters or variables that modify the Quality of Service of the wireless network and the Quality of Control of the robot. The use of the Bayesian Network is justified by the stochastic behavior of the Wireless Network. The main objective of the Bayesian Network is to diagnose, and then decide, according to the situation, the reconfiguration of either the network or the control strategy. The strongest point of Bayesian Network is that the same model can be used for both diagnosis and decision making. The proposed model achieves the purpose of our approach, which is to identify the degradation of the Quality of Control as coming either from the Robot or from the wireless network to make decision.

In this article, the communication architecture for two mobile robots moving in a 2D space with fixed control station has been considered as an illustrative example. According to the information delivered by the proposed bayesian network, the reconfiguration of both the communication architecture (Horizontal Handoff) and the control strategy is possible. This decision has the objective to guarantee a good QoC. The control law can be off-board in the case of a good QoS of the wireless network, due to the limited memory and resources of the mobile robot. The control law can also be embedded in the case of a bad QoS and the non-disponibility of another control station able to ensure the control of the robot via a wireless network. In this case, the control law should be degraded according to the memory and the processor speed.

#### *B. Future Works*

To avoid the degradation of the Quality of Control and the Quality of Service before its occurrence, the same Bayesian Network will be used adding some dynamic nodes in two time slices. The probability of the Quality of Control and the Quality of Service in time slice *t + 1* given the modes of the Quality of Control and the Quality of Service in time slice *t* can inform the system about the prediction of degradation of the Quality of Control.
