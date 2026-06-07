# Reliability evaluation of electromechanical braking system of mine hoist based on fault tree analysis and Bayesian network 

Huawei Jin ${ }^{1,2,3, *}$, Xu Wang ${ }^{1,3}$, Huwei Xu ${ }^{1,3}$, and Zhuqi Chen ${ }^{1,3}$ (D)<br>${ }^{1}$ Anhui Key Laboratory of Mine Intelligent Equipment and Technology, Anhui University of Science and Technology, Huainan 232001, China<br>${ }^{2}$ State Key Laboratory of Mining Response and Disaster Prevention and Control in Deep Coal Mines, Anhui University of Science and Technology, Huainan 232001, China<br>${ }^{3}$ School of Mechanical Engineering, Anhui University of Science and Technology, Huainan 232001, China

Received: 31 August 2022 / Accepted: 3 March 2023


#### Abstract

Electromechanical braking system is the key way to improve the braking response ability of mine hoist. At present, the reliability research of electromechanical braking system is less. In order to further analyze and improve the reliability of electro-mechanical braking system, this paper adopts the reliability analysis method of electro-mechanical braking system based on fault tree and Bayesian network. Firstly, the fault tree of the electro-mechanical braking system is established, and then the fault tree is transformed into a Bayesian network, and the posterior probability, probability importance and key importance of each root node are inversely deduced. The diagnosis results show that the ball screw is the weakest link of the electro-mechanical braking system. Then the static simulation and fatigue life simulation of the ball screw are carried out for optimization, and the optimal model of the ball screw is determined. Finally, the electro-mechanical brake installed with the optimized ball screw is tested and analyzed. After the reliable performance test of the electromechanical brake, it is finally determined that the braking effect of the optimized electro-mechanical brake is stable.


Keywords: Mine hoist / electromechanical brake / fault tree / Bayesian network / reliability analysis

## 1 Introduction

As the key engineering equipment in the process of underground coal mining [1], the operation of the mine hoist mainly depends on the stable and reliable execution ability of the braking system. The braking system with reliable structure and performance can reduce the maintenance times of the hoist, increase the operation time and reduce the occurrence of accidents [2,3]. If there is an accident in the braking system, the hoist cannot operate normally, which will seriously affect the mining progress of the coal mine and cause great losses. Therefore, in order to reduce the occurrence of even accidents and avoid unnecessary economic losses, it is extremely important to analyze the reliability of the hoist braking system before performing the work [4].

In the field of reliability research, fault tree analysis and Bayesian network are powerful research tools [5,6]. Li et al. [7] established a multi state multi value decision graph

[^0]model based on each fault sub tree and analyzed the reliability of the decision graph. Cao et al. [8] integrated the accident data provided by the online traffic website, combined with fault tree and Bayesian network, carried out reliability analysis on the road transportation system of hazardous chemicals tanker. Kou et al. [9] used the bi-directional reasoning ability of Bayesian network to analyze the reliability of wind power gearbox and found the weak links of the system. In order to solve the problem of CTCS-3 ATP system polymorphism, Zhang et al. [10] used dynamic Bayesian network to complete the reliability analysis of ATP system, which has very important guiding significance for improving the reliability of ATP system. In the case of incomplete reliability data, Dong et al. [11] combined fuzzy number theory with Bayesian network to solve the problem that traditional Bayesian network could not complete reliability research in the case of missing and incomplete data, and calculated the reliability of automobile soft close system. Li et al. [12] proposed a fault diagnosis method of hoist brake system based on Bayesian network and A-star algorithm, and completed the fault diagnosis of brake system according to the data collected

[^1]
[^0]:    * e-mail: hwjin@mail.ustc.edu.cn

[^1]:    This is an Open Access article distributed under the terms of the Creative Commons Attribution License (https://creativecommons.org/licenses/by/4.0), which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

by sensors. The experimental results show that the correctness and accuracy of this diagnosis method are very stable, which is helpful to improve the system reliability. Hu et al. [13] proposed a braking system fault diagnosis method combining fuzzy theory and neural network. According to the fault data collected by fuzzification processing, the fault state of the braking system was diagnosed. The diagnosis results showed that this method could accurately achieve fault diagnosis and effectively improve the system reliability. Wang et al. [14] proposed a reliability analysis method based on T-S fuzzy fault tree, aiming at the problems of fault event polymorphism and fault data ambiguity of the lifting mechanism moving system, which effectively solved the problems of imprecise probability and complex fault states. Choi [15] and others carried out reliability analysis on the new non explosive separation device of small satellite by fault tree analysis method, and found 10 single point fault modes. Jiang [16] and others combined fuzzy theory and fault tree analysis technology to evaluate the reliability of Wushu competitive robot system and provide theoretical guidance for robot fault diagnosis. However, FTA is not good at determining the possibility of a certain event leading to the failure of the whole system, and it is difficult to analyze complex systems. Compared with FTA, Bayesian network can deal with complex uncertain problems well. Li [17] and others determined the weak links of offshore floating wind turbines using Bayesian networks, and concluded that the reliability analysis results of offshore floating wind turbines using Bayesian networks are more accurate than those using fault tree analysis. Wang [18] and others used the fault diagnosis ability of Bayesian network to find out the main factors leading to the failure of emergency evacuation of offshore platforms, and provided reference for escape, evacuation and rescue (EER) plan. Sun [19] proposed a copula Bayesian network (CBN) model for complex systems. Therefore, Bayesian network has many advantages in dealing with the reliability evaluation and fault diagnosis of complex systems.

In addition to fault tree, there are many other effective tools applied in the field of reliability research. Cardoso et al. [20] proposed a method for calculating structural failure probability combining neural network and Monte Carlo simulation. The advantages of this method were verified by discussing a test function and two structural examples. Papadopoulos et al. [21] proposed a subset simulation method based on neural network, which makes up for the variability of subset simulation and improves the efficiency of subset simulation. Amrin et al. [22] proposed a method for automatically creating Bayesian networks, which improved the reusability of engineering design data, and evaluated and tested 25 different vehicles. Wang et al. [23] proposed a tunnel reliability analysis method combining adaptive radial basis function element modeling technology with first-order reliability method, which improves the accuracy of the model and provides an efficient reliability analysis method for tunnel engineering problems. Peng et al. [24] proposed a new dynamic Petri net model based on Dempster-Shafer evidence theory. By improving the artificial bee colony algorithm and Demp-ster-Shafer evidence theory, the accuracy of the evidence

Petri net model in knowledge reasoning and reliability analysis of complex mechanical systems was improved. Zhao et al. [25] based on the Khristianovic-Geertsma-de Klerk model and Perkins-Kern-Nordgren model, adopted the first-order reliability method to calculate the reliability index of hydraulic fracturing, which provides an effective and scientific method for the uncertainty analysis of hydraulic fracturing.

In order to improve the reliability of the brake system, many scholars have carried out research on the hydraulic brake system. Ma [26] and others designed a constant deceleration compensation device in order to make the brake capable of constant deceleration, so that the brake has a constant deceleration function and greatly improves the safety and reliability of the mine hoist; Popescu [27] and others established a numerical calculation model for the temperature of the moving disk of the mine hoist under emergency braking to ensure the safe operation of the hoist under emergency braking, and determined that the temperature did not exceed the limit value during emergency braking; Li [28] and others adopted the fault diagnosis method of mine hoist braking system based on mechanical learning to realize high-precision fault diagnosis of mine hoist braking system and further improve the reliability of braking system; Xu [29] and others designed a disc brake with real-time monitoring of brake positive pressure and certain brake fault diagnosis function to solve the fault problem of the hydraulic disc brake of the mine hoist, which is used to diagnose the fault of the disc brake in real time and avoid further expansion of the fault accident. However, the research on the reliability of the braking system mainly focuses on the hydraulic braking system, and the research on the reliability of the electro-mechanical braking system is less. Although hydraulic disc brakes are widely used, with the change of the times, more intelligent and safe brakes are needed [30]. However, at present, the problems of hydraulic disc brake oil leakage, brake gap compensation and brake force can not be accurately controlled have not been effectively solved. Compared with the hydraulic brake, the electro-mechanical brake has a high degree of mechanization and automation, and the dynamic response speed of the motor is fast; By controlling the motor input, the braking force can be accurately controlled, which is more in line with the development direction of deep coal intelligent equipment, and is of great significance for the safe and efficient operation of ultra deep mine hoists [31,32]. Therefore, it is very important to evaluate its reliability.

In view of the above investigation, in order to improve the reliability of the electro-mechanical braking system, this research adopts the reliability analysis method of fault tree and Bayesian network to analyze the reliability of the electro-mechanical braking system. The electro-mechanical braking system is divided into several subsystems, and the fault tree of the electro-mechanical braking system is constructed based on the structure and fault mechanism of each part; The fault tree of the electro-mechanical braking system is transformed into a Bayesian network model by the transformation modeling method of fault tree Bayesian network; According to the transformation of the logical relationship of the nodes in the fault tree, the relationship

![img-0.jpeg](img-0.jpeg)

Fig. 1. Structural diagram of electro-mechanical disc brake.

Between the nodes of the Bayesian network is obtained, which is the conditional probability table. The fault probability of the bottom event in the fault tree corresponds to the prior probability of the root node of the Bayesian network. The posterior probability and fault relevance importance of each root node are calculated according to the Bayesian network model. According to the calculation results of the key importance degree, probability importance degree and posterior probability of the root node of the system, the weak links of the braking system and the most influential factors of the system can be accurately and quickly located. After determining the weak link, simulation and optimization are carried out to get the best model of this link. In order to study the reliability performance of the optimized electro-mechanical brake, the electro-mechanical brake installed with the optimized ball screw was taken as the experimental object to carry out the reliability performance test of the electro-mechanical brake. Finally, the experimental results are obtained, thus completing the reliability analysis of the whole system and providing support for the design of the braking system.

## 2 Electro-mechanical brakes and reliability analysis methods

### 2.1 Operating principle of electro-mechanical brake

Figure 1 is the schematic diagram of the structure of the electro-mechanical disc brake. Its mechanical structure consists of DC torque motor, planetary gear reducer, ball screw pair, disc spring, slider, piston and brake shoe, etc. Electro-mechanical disc brakes complete braking based on the "power source – transmission mechanism – actuator" structure. The operation principle of electro-mechanical disc brake is as follows: When the hoist is running, the brake is released. At this time, the motor reverses and the speed is reduced by the reducer to increase the torque. The rotary motion is converted into the linear motion of the piston through the ball screw. The piston compresses the sliding block and then compresses the disc spring to generate a preload. The brake shoe connected with the piston moves backward, and the brake clearance appears between the brake shoe and the brake disc, thus relieving the brake positive pressure on the brake disc. When the hoist is braked, the brake is closed. At this time, the motor rotates forward and the disc spring is released. The preload of the disc spring provides the positive braking pressure. The sliding block acts on the piston to push the brake shoe forward, so that the brake shoe and the brake disc fit to generate braking torque to realize the braking of the hoist. Compared with the complex hydraulic disc brake, the electro-mechanical disc brake uses the torque motor to provide the braking torque, which not only simplifies the structure of the disc brake, but also avoids a series of problems such as leakage caused by hydraulic braking.

### 2.2 Mathematical model of brake

The mathematical model of DC torque motor is as follows:

$$U = I_a R_a + L_a \dot{I}_a + K_c \omega_m, \tag{1}$$

$$I_a = \frac{1}{K_T} \left( J_m \frac{d\omega_m}{\mathrm{~d}t} + B_m \omega_m + T_L \right), \tag{2}$$

where \(U\) is the armature voltage, \(I_a\) is the armature current, \(R_a\) is the armature resistance, \(L_a\) is the armature inductance, \(K_c\) is the back EMF coefficient, \(\omega_m\) is the motor rotor angular speed, \(K_T\) is the torque constant, \(J_m\) is the motor moment of inertia, \(T_L\) is the load torque, \(B_m\) is the motor damping.

In order to meet the torque required by the braking process, it is not enough to rely on the motor alone. Therefore, a torque lifting device is required. Therefore, a planetary gear reducer is adopted. The relationship between the output torque and the input torque is as follows:

$$T_v = T_L \cdot i_v \cdot \eta_v, \tag{3}$$

where \(T_v\) is the planetary reducer outputs torque, \(i_v\) is the planetary gear reduction ratio, \(\eta_v\) is the transmission efficiency of planetary reducer.

The output of the reducer is still rotary motion, and the linear braking of the brake shoe cannot be realized. The ball screw pair is used to convert the rotary motion into the linear motion of the brake shoe. The relationship between the thrust of the nut push rod and the driving torque of the

![img-1.jpeg](img-1.jpeg)

Fig. 2. Transformation of fault tree to BN.

lead screw is as follows:

$$
\left(i_c^2 J_c + m_c\right) \frac{d^2 x_c}{dt^2} + B_c \frac{dx_c}{\mathrm{d}t} = i_c T_v - f, \tag{4}
$$

where $J_c$ is the moment of inertia of lead screw, $m_c$ is the weight of nut push rod and brake shoe, $x_c$ is the nut push rod displacement, $f$ is the load resistance, $B_c$ is the viscous damping coefficient between worktable and slide rail, $i_c$ is the transmission ratio of ball screw pair.

The Belleville spring directly contacts the piston and controls the compression amount of the Belleville spring by controlling the rotation of the motor. The relationship between load and deformation of single disc spring is:

$$
P_t = \frac{4E}{1 - \mu^2} \cdot \frac{h_t^4}{K_1 D^2} \cdot \frac{\Delta x}{h_t} \left[ \left( \frac{h_0}{h_t} - \frac{\Delta x}{h_t} \right) \left( \frac{h_0}{h_t} - \frac{\Delta x}{2h_t} \right) + 1 \right]. \tag{5}
$$

Calculation coefficient:

$$
K_1 = \frac{1}{\pi} \cdot \frac{[(C - 1)/C]^2}{(C + 1)/(C - 1) - 2/\ln C}, \tag{6}
$$

where $P_t$ is the load, $E$ is the modulus of elasticity, $D$ is the disc spring diameter, $\mu$ is the Poisson's ratio, $h_0$ is the deformation of disc spring at ordinary times, $h_t$ is the thickness of the disc spring, $\Delta x$ is the deformation, $d$ is the disc spring inside.

For disc spring without supporting surface, $K_4 = 1$.

### 2.3 Fault tree and Bayesian network method

Fault tree analysis (FTA) and Bayesian network (BN) are common methods for reliability analysis. Both FTA and BN have their own advantages and disadvantages when they are used. When they are combined and converted, they can solve the problem of complex BN model construction and make up for the shortcomings of FTA in complex system analysis [33].

The fault tree model takes the system failure event as the top event, and then looks down to the final cause of the failure and takes it as the bottom event. When the fault tree is converted into a Bayesian network, each node in the Bayesian network corresponds to various events in the fault tree. The logical gate connecting the events in the fault tree is replaced by the conditional probability table of BN. The prior probability of the root node in BN corresponds to the occurrence probability of the bottom event in the fault tree. The fault tree in Figure 2a is composed of bottom events D1, D2, D3, intermediate events C and top events G, where the bottom event D1 and D2 are connected in parallel, and the intermediate event C. and the bottom event D3 are connected in series. The Bayesian network model transformed from the fault tree through the above steps is shown in Figure 2b. 0 and 1 of the conditional probability table represent the normal and fault states of the node respectively.

## 3 Reliability analysis of electro-mechanical braking system

### 3.1 Fault tree analysis of electro-mechanical braking system

The electromechanical braking system of the mine hoist is composed of the control system and the basic braking system. This study takes the electromechanical braking system testbed as the analysis object. Figure 3 shows the layout diagram of the electro-mechanical braking system test bench.

The basic braking system, also known as the electromechanical brake, is mainly located on the test stand, the motor is fixed on the frame, the output end of the motor is connected to the planetary gear reducer, the planetary reducer connects the output end to the ball screw pair through a coupling, and the brake shoe is on the side. The control system is mainly composed of sensor, programmable logic controller (PLC) and motor controller (adjustable power supply). The data collected by the sensor is converted by signal amplifier and AD module and supplied to PLC. PLC processing the received signal to generate the corresponding instructions to the motor controller to control the motor speed and output torque. Figure 4 shows the operation principle of the whole system. The braking system uses PLC as controller and torque motor as power source. In the braking process, the braking torque is adjusted by adjusting the input voltage of the torque motor, so that the mine hoist adaptively adjusts the braking torque according to the change of the load, and achieves the safety braking of the hoist.

![img-2.jpeg](img-2.jpeg)

**Fig. 3.** Electro-mechanical braking system test bench.

![img-3.jpeg](img-3.jpeg)

**Fig. 4.** Operating principle diagram of electro-mechanical braking system.

According to the rule of determining the top event of fault tree, the electro-mechanical braking system fault is selected as the top event. The electro-mechanical braking system is mainly composed of basic braking system and control system. If one of these two systems fails, the braking system will also be affected and will not function properly. Therefore, electro-mechanical braking system can be regarded as composed of base braking system and control system in series. Therefore, the fault tree of the braking system is initially established by taking the two fault events of the system as the next level events.

The basic braking system is mainly composed of transmission unit and execution unit in series. The failure of basic braking system is regarded as the top event, and the failure of transmission unit and execution unit is regarded as the next level event. The failure events of transmission unit mainly include planetary reducer failure and ball screw damage. The failure events of actuator unit mainly include brake shoe wear, brake shoe friction coefficient is too small and disc spring damage. The events leading to brake shoe wear are brake disc swing is too large and brake installation is not correct. The events leading to brake shoe friction coefficient is too small are brake disc overheating and brake disc pollution. The events leading to disc spring damage are spring fatigue and spring fracture. Therefore, the execution unit, transmission unit, brake shoe wear, too small friction coefficient of brake shoe and disk spring damage are taken as intermediate events, while the bottom events are composed of the corresponding failure events of intermediate events.

The fault tree model of the control system is established in the same way as the previous subsystem. The intermediate events are composed of acquisition device failure, PLC failure and output device failure. The failure event of acquisition equipment is mainly sensor failure. PLC mainly includes two failure events: PLC memory card failure and PLC hardware failure. The output device mainly includes two failure events: motor controller failure and motor failure. Therefore, the control system is regarded as the top event of the fault tree, and the acquisition device, PLC and output device are regarded as the intermediate events. The corresponding failure events of the three together constitute the bottom event of the model.

According to the above contents and the construction rules of the fault tree model, the fault tree of the mechanical braking system of mine hoist can be obtained as shown in Figure 5, and the names of all events in the fault tree are shown in Table 1.

### 3.2 Bayesian network analysis

Complete the transformation from fault tree to Bayesian network according to the steps in section above. The occurrence probability of the bottom event is taken as the prior probability of the corresponding root node. Table 2 shows the occurrence probability of each bottom event. Figure 6 shows the transformed BN model.

The conditional probability table is used to express the logical relationship between nodes in BN. According to the transformation rules in section above, logical gates in the

![img-4.jpeg](img-4.jpeg)
(a) Brake system fault tree
![img-5.jpeg](img-5.jpeg)
(b) Basic braking system fault subtree
![img-6.jpeg](img-6.jpeg)
(c) Control system fault subtree

Fig. 5. Fault tree of electro-mechanical braking system.
fault tree are expressed as conditional probability tables in BN. Take the transmission unit of base braking system as an example. The basic braking system consists of transmission and execution units. The failure events of its transmission unit mainly include planetary reducer failure and ball screw damage. When either event occurs, the whole transmission unit cannot work normally. From this, it can be determined
that events are linked together through logic or gates, thus obtaining the conditional probability table of node $\mathrm{B}_{1}$. As shown in Table 3. Where $P\left(\mathrm{~B}_{1}=1\right)$ represents the probability of event occurrence, and $P\left(\mathrm{~B}_{1}=0\right)$ represents the probability of event non-occurrence. There are many intermediate nodes in this paper, and the conditional probability table of other nodes is no longer listed.

Table 1. Fault tree nodes.


Table 2. Occurrence probability of bottom events.


### 3.3 System fault diagnosis

The posterior probability of root node can be obtained by reverse inference of BN. According to the posterior probability of each root node, the importance of the components corresponding to the root node in the electromechanical braking system can be determined. The posterior probability calculation according to the BN model in Figure 5 requires complex inference calculation. In order to reduce the calculation time and improve the accuracy of calculation. This study uses MATLAB to complete the posterior probabilistic inference calculation [34]. The simulation model of electro-mechanical braking system is constructed through MATLAB programming, as shown in Figure 7 Then assign values, input the prior probability of each root node and conditional probability table of other nodes, select the joint tree algorithm for inference calculation, and obtain the posterior probability of all root nodes when the electro-mechanical braking system failure occurs, as shown in Table 4.

In order to more directly observe the size relationship between the posterior probabilities corresponding to each root node, draw the histogram shown in Figure 8. It can be seen from and Figure 8, when electromechanical braking system of mine hoist is faulty, the posterior probabilities of
$\mathrm{X}_{1}$ (Ball screw damaged), $\mathrm{X}_{5}$ (Excessive swing of brake disc) and $\mathrm{X}_{6}$ (Improper brake installation) calculated for each root node are relatively large. Ball screw, brake disc and brake shoe are the weak links in case of problems in electromechanical braking system. During system maintenance, check and maintain these three components more often to improve the maintenance frequency of these three components. In case of system failure, priority can be given to check whether these three components have problems, which can reduce the work of troubleshooting and improve work efficiency.

In the BN, the posterior probability can reflect the importance of the unit in the system, but only relying on the posterior probability to guide the fault diagnosis has incomplete reliability. Therefore, it is necessary to determine the weak unit of electromechanical braking system by combining the posterior probability, probability importance and critical importance of root node.

In the BN of electro-mechanical braking system, the middle node is T , and the root node is $\mathrm{X}_{1}-\mathrm{X}_{15}$, and each node does not intersect each other. The probability of the leaf node T is as follows:

$$
P(T=1)=\sum_{i=1}^{n} P\left(T=1 \mid x_{i}\right) P\left(x_{i}\right)
$$

![img-7.jpeg](img-7.jpeg)

Fig. 6. BN model of electro-mechanical braking system.

Table 3. Conditional probability of node B1.


The calculation formula of the probability importance degree of the occurrence of the leaf node *T* caused by the occurrence of the root node *X_{i}* is as follows:

$$I^P(x_i) = P(T = 1|x_i = 1) - P(T = 1|x_i = 0),$$

where *I^{P}(x_{i})* is the probability importance of the root node *x_{i}*, *P(T=1|x_{i}=1)* is the probability of leaf node occurrence when root node *x_{i}* occurs, *P(T=1|x_{i}=0)* is the probability of leaf node occurrence when root node *xi* does not occur.

The calculation formula of the critical importance of the root node *X_{i}* causing the leaf node *T* state to occur is as follows:

$$I^C(x_i) = \frac{P(x_i = 1)[P(T = 1|x_i = 1) - P(T = 1|x_i = 0)]}{P(T = 1)}. \tag{9}$$

According to formulas (9) and (10), the probability and critical importance of each root node in the event of failure of the electro-mechanical braking system are calculated, as shown in Table 5. In order to more intuitively observe the magnitude relationship between the importance of each root node, the calculated probability and critical importance are plotted in broken lines and bar charts, as shown in Figure 9.

It can be seen from Table 5 and Figure 9 that when the mechanical braking system of mine hoist breaks down, the values of *X_{1}* (ball screw damage), *X_{5}* (excessive brake disc deflection), *X_{6}* (improper brake installation), *X_{11}* (PLC memory card failure) and *X_{12}* (PLC hardware failure) in the calculated probability importance of each root node are relatively large. Among the calculated key importance of each root node, *X_{1}* (ball screw damage), *X_{5}* (excessive brake disc deflection). The values of *X_{6}* (incorrect brake installation) and *X_{11}* (PLC memory card failure) are large.

It can be seen from the above. When the electro-mechanical braking system cannot operate normally, the root node *X_{1}* (ball screw damaged) is the most in terms of posterior probability, probability importance and critical importance. This shows that the ball screw is the weakest link when the electro-mechanical braking system fails, so it is necessary to check the ball screw frequently when the electro-mechanical braking system is running to reduce the probability of failure. At the same time, *X_{5}* (Excessive swing of brake disc) and *X_{6}* (Improper brake installation) values are also large, only less than *X_{1}* (Ball screw damaged), so it is necessary to improve the inspection times of brake disc and brake shoe. When the electro-mechanical braking system is in abnormal working state, priority inspection shall be carried out for these three components, and then check other events one by one, it can effectively shorten the fault diagnosis time of electro-mechanical braking system and improve the maintenance efficiency. By analyzing the results, maintenance personnel can reasonably allocate testing and maintenance resources to maximize resource utilization.

# 4 Simulation and optimization of weak parts

## 4.1 Static simulation

As the weakest part of electro-mechanical braking system, ball screw is the key bearing part of electro-mechanical braking system. It will be deformed due to the main torque of the braking system and the spring preload, which will have an important impact on the braking performance and safety performance. Therefore, it is necessary to ensure that the strength and stiffness of the ball screw of the braking system meet the requirements.

The static analysis of the ball screw is carried out with ANSYS software. After the solution, the stress nephogram and total deformation nephogram of the ball screw pair are obtained, as shown in Figures 10 and 11.

It can be seen from the figure that the maximum deformation is about 0.030158 mm, and the deformation of the lead screw is small. It can be seen from the figure that the overall stress of the ball screw is relatively uniform, and

![img-8.jpeg](img-8.jpeg)

**Fig. 7.** Bayesian network simulation diagram of electromechanical braking system.

**Table 4.** Posterior probability of each root node.


![img-9.jpeg](img-9.jpeg)

**Fig. 8.** Posterior probability of root node.

the maximum stress is mainly concentrated in the area where the ball contacts the nut and the screw. The maximum stress is 577.14 Mpa, which is far less than the yield strength of the material, and the stress of the screw and the nut is small. In general, the strength and rigidity of the ball screw meet the design requirements.

### 4.2 Fatigue life simulation

In the braking system, the ball screw needs to run for many cycles. Under the condition that the strength and stiffness meet the demand, the normal failure form of the ball screw is mainly fatigue damage caused by long-term cycle operation. As the key component of the electro-mechanical braking system, in order to improve the reliability of the whole system, it is necessary to ensure that the fatigue life of the ball screw meets the design requirements. Therefore, it is necessary to analyze the fatigue life of the ball screw.

Ncode software was used to build the fatigue analysis project diagram of ball screw, which mainly included importing the finite element analysis results of ball screw, material setting and S-N curve of the corresponding material of ball screw, setting the fatigue life analysis results of ball screw as the output module, etc. The analysis interface was shown in Figure 12.

The fatigue life analysis cloud diagram of ball screw is obtained by simulation calculation, as shown in Figure 13. It can be seen from the diagram that the minimum fatigue life of ball screw obtained by simulation is 2.773 × 10<sup>6</sup> times, and the stress cycles borne by the material are not up to 1 × 10<sup>7</sup> times. The stiffness and strength of ball screw can meet the design requirements, but the fatigue life of ball screw needs to be further improved. In order to improve the

Table 5. Posterior probability of each root node.


![img-10.jpeg](img-10.jpeg)

Fig. 9. Line chart of root node importance.
fatigue life of ball screw, the fatigue life of ball screw is improved by changing the size of lead. This method can make the optimized ball screw structure meet the size of other parts, and increase the minimum fatigue life of the ball screw.

### 4.3 Ball screw optimization

As the key bearing component of the braking system, the ball screw is subjected to the preloading force from the disc spring in the braking process, which bears 30 KN preloading force, and 35 KN preloading force in the opening stage. Therefore, the maximum preloading force under the ball screw is taken as the equivalent load.

$$
F_{m}=35 \mathrm{kN}
$$

According to the design requirements that the brake gap is 1 mm and the braking time should not be less than 0.2 s , it can be determined that the maximum moving speed of the brake $V_{m \text { - Max }} \geq 5 \mathrm{~mm} / \mathrm{s}$, and the maximum speed of the lead screw is $N_{m \text { - Max }}=60 \mathrm{r} / \mathrm{min}$. Thus, the minimum lead P of the lead screw can be obtained:

$$
P=\frac{V_{m-\max }}{N_{m-\max }}=5 \mathrm{~mm}
$$

In the operation of the braking system, the braking time is very short and far less than the opening time, so the average speed of the lead screw is far lower than the maximum speed, so take one-third of the maximum speed as the equivalent speed of the ball screw, namely $N_{\mathrm{m}}=20 \mathrm{r} / \mathrm{min}$.

In the selection and design stage of ball screw, the minimum rated dynamic load needs to be determined first, and the calculated minimum rated dynamic load is used as the standard to select ball screw. The basic calculation formula is:

$$
C_{a}=\sqrt[3]{60 N_{m} L_{b}} \cdot \frac{F_{m} f_{w}}{100 f_{a} f_{c}}
$$

where: $L_{b}$ is the working life, $f_{w}$ is the load coefficient, $f_{a}$ is the accuracy coefficient, $f_{c}$ is the reliability coefficient. Refer to the design manual and take $L_{b}$ as $1000, f_{w}$ as $1.3, f_{a}$ as $1, f_{c}$ as 1 and substitute it into equation (11) to obtain:

$$
C_{a}=\sqrt[3]{60 N_{m} L_{b}} \cdot \frac{F_{m} f_{w}}{100 f_{a} f_{c}}=48.35 \mathrm{kN}
$$

In order to make the designed ball screw meet the assembly requirements of other parts of the brake, according to the above calculated lead $P \geq 5 \mathrm{~mm}$, rated

![img-11.jpeg](img-11.jpeg)

Fig. 10. Cloud diagram of stress distribution of ball screw.
![img-12.jpeg](img-12.jpeg)

Fig. 11. Cloud diagram of total deformation distribution of ball screw.
![img-13.jpeg](img-13.jpeg)

Fig. 12. Fatigue analysis interface of ball screw.

![img-14.jpeg](img-14.jpeg)

**Fig. 13.** Fatigue life distribution cloud of ball screw.

**Table 6.** The simulation results of each model were compared.


The dynamic load *C_{u}* ≥ 48.35 kN as the design requirements, by looking up the manual, finally determines the model of SFU5010, SFU5020 ball screw.

### 4.4 Comparison of simulation results of ball screw before and after optimization

The above two models of ball screw are simulated and compared with the simulation results of the initial model. The simulation result indexes (maximum stress, maximum deformation, and minimum life) of the initial model and the design model are shown in Table 6.

As can be seen from Table 16, compared with the initial ball screw model, the minimum fatigue life of the ball screw designed according to theory is much higher than that of the initial ball screw, and the minimum fatigue life is higher than 1 × 10<sup>7</sup> times, which meets the design requirements. The maximum deformation is not different, and the maximum stress is one half of the maximum stress of the initial model. Thus, it can be determined that the stiffness and reliability of the designed ball screw are higher than those of the initial model, and among the designed ball screw, the reliability of the SFU5010 ball screw is higher than that of the SFU5020 ball screw, and the optimal model is finally determined to be the SFU5010 ball screw.

### 5 Experimental study

Through the above analysis, the ball screw optimization model is finally determined, and the electro-mechanical braking system is further optimized. In order to study the reliability and braking performance of the optimized electro-mechanical brake, the electro-mechanical brake equipped with the optimized ball screw was used as the experimental object for experimental analysis.

#### 5.1 The composition of the experimental bench

The experimental bench is mainly composed of two parts: electro-mechanical braking system and signal acquisition system.

The electro-mechanical braking system is mainly composed of a dynamic electro-mechanical brake and a control box, which are shown in Figures 14 and 15, respectively.

The information acquisition system studies the reliability and braking performance of the electro-mechanical braking system by collecting data from sensors, including sensors, data acquisition cards, and computers. The data collected by the sensor are transferred to the LabVIEW software of the computer through the data acquisition card. Finally, the data collected are compared and analyzed to study the performance of the electro-mechanical brake.

#### 5.2 Reliability test of electro-mechanical brake

The reliability of the brake is the key link to meet the safety braking of the hoist. Therefore, it is necessary to test the optimized electro-mechanical brake experimentally to study whether the reliability of the braking system meets the requirements.

Therefore, this paper adopts the method of quantitative repetition. Under the condition of ensuring that the input voltage of the motor is 5 V and the rotation speed of the

![img-15.jpeg](img-15.jpeg)

**Fig. 14.** Real picture of dynamic brake. 1. Three-phase asynchronous motor. 2. Frequency converter. 3. Clutch 4. Flywheel. 5. Bearing seat. 6. Brake disc. 7. Brake. 8. Torque sensor. 9. Planetary gear reducer. 10. Torque motor.

![img-16.jpeg](img-16.jpeg)

**Fig. 15.** Physical picture of control box. 1. Transformer. 2. Circuit breaker. 3. FX2N-48MT. 4. Relay group. 5. FX2N-4DA. 6. FX2N-4AD.

Brake disc is 180 r/min, 100 braking experiments are repeated, and the steps of braking and opening are repeated continuously to collect the braking time of each experiment to explore the reliability of the braking system. During the experiment, the temperature sensor shows that the temperature of the brake disc is always around the room temperature, ignoring the influence of the brake disc temperature on the friction coefficient. Because there are too many data, 11 brake tests of the 1st, 10th, 20th, 30th, 40th, 50th, 60th, 70th, 80th, 90th, and 100th are selected for analysis. The specific test data are shown in Table 7.

According to the change law of braking time in the table, the braking time always changes between 2 s and 2.1 s with the increase of braking times. Considering that small-scale fluctuations of instrument accuracy and equipment quality are unavoidable in laboratory situations, such small-scale fluctuations can be ignored. Therefore, it can be seen from the table that the braking time is almost constant with the increase of braking times, the braking effect of the electromechanical brake is still stable after frequent repeated operation, and the reliable performance of the electromechanical brake meets the demand. In order to observe the relationship between brake disc speed and braking time more clearly, 6 groups

Table 7. Data sheet of reliability performance test.


![img-17.jpeg](img-17.jpeg)

Fig. 16. Diagram of reliability performance test results. of data were taken from the 11 groups of data and Origin was used to draw the test data into a dot plot, as shown in Figure 16.

As can be seen from the above figure, the experimental data of these six groups are all relatively close, and there is a certain deviation between 0 s and 1 s for the data of the 60th braking. Considering that the deviation of the processing accuracy and quality of the test equipment cannot be avoided during the test, and the deviation of the speed is within a reasonable range. Through the analysis, it can be seen that the braking times increase, the braking time is unchanged, and the speed of the brake disc is almost in a constant deceleration state, so it can be seen that the optimized electro-mechanical brake braking effect is stable, and its reliability meets the requirements.

## 6 Conclusion

- The combination and application of fault tree and Bayesian network in the reliability analysis of mine hoist mechanical braking system can not only find the weak links in the system and improve the analysis efficiency, but also optimize the system according to the analysis results, so as to improve the reliability of the system.
- Through the fault diagnosis of the electromechanical braking system of the mine hoist, the posterior probability, probability and critical importance of the root node are analyzed, and the weakest link in the system is found to be the ball screw device, which provides suggestions for the overhaul and maintenance of the electromechanical braking system and has certain practical value.

- Under the condition that the input voltage of the motor and the rotation speed of the brake disc are constant, the braking experiment is repeated. The results show that the braking time is constant with the increase of the braking times, and the rotation speed of the brake disc is almost in the constant deceleration state. Therefore, it can be seen that the optimized electro-mechanical brake has stable braking effect and good reliability.


## Nomenclature

4AD 4-channel analog-to-digital signal conversion. 4DA 4-channel digital-to-analog signal conversion.

## Funding

This work was supported by the National Foundation of China (Grant NO.: 51904009), and the Open Fund of Anhui Key Laboratory of Mine Intelligent Equipment and Technology, Anhui University of Science \& Technology (ZKSYS202102).

## Conflicts of interest

The authors declare no conflict of interest.

## Author contributions

Conceptualization, HW.J. and X.W.; data curation, HW.J. and X.W.; formal analysis, HW.J. and X.W.; funding acquisition, HW.J.; investigation, X.W., ZQ.C. and HW.X.; methodology, HW.J. and X.W.; project administration, HW.J.; resources, HW.J. and HW.X.; software, ZQ.C.; supervision, HW.J. and HW.X; validation, X.W. and HW.J.; writing original draft preparation, ZQ.C.; writing review and editing, X.W., HW.J.
