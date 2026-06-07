# Article 

## An Analytic Method for Power System Fault Diagnosis Employing Topology Description

Biao Xu ${ }^{1, *}$, Xianggen Yin ${ }^{1}$, Dali Wu ${ }^{2}$, Shuai Pang ${ }^{1}$ and Yikai Wang ${ }^{1}$<br>1 State Key Laboratory of Advanced Electromagnetic Engineering and Technology, Huazhong University of Science and Technology, Wuhan 430074, China; xgyin@hust.edu.cn (X.Y.); Shuaipang@hust.edu.cn (S.P.); Yikaiwang@hust.edu.cn (Y.W.)<br>2 Wuhan Second Ship Design and Research Institute, Wuhan 430064, China; zuoyexingfeng@163.com<br>* Correspondence: D201577326@hust.edu.cn; Tel.: +86-151-723-37201

Received: 23 March 2019; Accepted: 9 May 2019; Published: 10 May 2019


#### Abstract

When a fault occurs in a power system, fault section estimation is the primary premise for troubleshooting and power recovery, and an effective fault diagnosis system will play a big role in decision making. However, the topology information is not well employed in existing fault diagnosis methods, and it is complex and time consuming to analyze the relationship between the protective devices and the sections. In this paper, a novel analytic method which employs topology description is proposed for fault diagnosis. The topology descriptions of the sections and the protective devices are firstly established according to the network structure, and based on which the operating logic and the cooperative relationship of the protective devices can be easily analyzed by matrix operation. Considering the factors of logic error and communication error, the fault diagnosis problem is formulated as an integer programming problem and can be solved by intelligent algorithm. The case studies of different power systems show that the proposed method can quickly identify the fault section, even with the abnormal operation or error alarm of protective devices.


Keywords: power system; fault diagnosis; analytic model; topology description; incident matrix

## 1. Introduction

Modern power systems are equipped with redundant protective devices to increase security and reliability. Under this background, a large number of alarms will flow into the dispatch center when fault occurs. The fault diagnosis problem is to interpret the raw alarms into summarized information, which helps dispatchers make the right decisions for troubleshooting and power recovery. This task can be very hard, especially under complex fault scenarios. Thus, it's of great significance to develop an effective fault diagnosis system [1].

To deal with the fault diagnosis problem, many kinds of methods have been proposed, such as the approaches based on expert system [2-4], artificial neural network [5-7], fuzzy theory [8,9], rough sets [10,11], Bayesian network [12-14], Petri nets [15-17] and analytic model [18-21]. Although these methods have advantages in some respects, they have their own disadvantages. For example, the expert system has difficulty in establishing and maintaining the knowledge base; the artificial neural network lacks the ability to interpret the reasoning results; the fuzzy rules and membership functions of the fuzzy theory are subject to subjective influences; the prior probability is difficult to obtain for a Bayesian network; the Petri nets-based method has difficulties in online modeling and thus the adaptability is poor.

The analytic model-based method formulates the fault diagnosis problem as a programming problem, and many well developed intelligent algorithms can be used to solve the problem, such as the genetic algorithm [18,22], Tabu-search [20], ant colony algorithm [23], immune algorithm [24,25],

honey-bee mating algorithm [26], brain storm optimization [27]. Therefore, this kind of method has strong theoretical and mathematical foundations and gets more and more attention in recent years.

At present, the research of analytic model is mainly focused on improving the objective function. In Reference [28], the cooperating relationship of the protective devices is introduced into the objective function, and the GATS algorithm is developed to solve the optimization problem. In [29], the malfunctions of protective relays and circuit breakers are considered in the analytic model, and the results show that the model has better fault tolerance. Based on this research, the operating logic of the protective devices and their coupling relationship with the alarms are further analyzed in [30], and a novel analytic model is established to solve the problem of alarm distortion. In reference [31], different weight coefficients are assigned to the protective devices in the objective function, and the results show that the coefficients can eliminate the problem of multiple solutions. In References [32,33], temporal reasoning is employed to analyze the timing information of the alarms, and the temporal constraints are further introduced into the objective function, which enriches the theoretical connotation of the analytic model. In reference [34], the discrepancy index, temporal conflict index and minimum index are comprehensively considered in the objective function, which can adapt to various protection schemes and wiring modes.

While the above methods are attractive for the fault diagnosis problem, they fail to make full use of the topology information. As a result, the analysis of the operating logic is performed in units of each single section, and it is complex and time consuming to determinate the relationship between the sections and the protective devices as well as their related paths [29]. Besides, additional variables are needed to represent the uncertainties of the alarm, which may lead to the problems of dimension disaster and contradictory hypothesis.

To this end, a novel analytic method for power system fault diagnosis employing topology description is proposed in this paper. According to the network structure, the topology descriptions of the system, sections and protective devices are established based on the incident matrix, and the mapping relationship between the protective devices and the sections is analyzed using matrix operations. In this way, the expected states of protective devices as well as the objective function can be established in matrix form. Finally, the genetic algorithm is used to solve the programing problem in the part of case studies, and the testing results demonstrate the effectiveness and fault tolerance of the proposed method. The following three aspects are the major features of this work.
(1) Based on the incident matrix, the topology description of the power system is established to represent the correlation between the sections and the protective devices, and the expected states of the protection devices can be analyzed by simple matrix operations.
(2) Considering both the operating logic error and the communication error of the protective devices, the improved objective function of the analytic model is constructed, which can adapt to power systems with different structure or connections.
(3) The optimized solution can distinguish the true hypothesis from the false ones with better fault tolerance, and the diagnosis result is helpful to evaluate the abnormal operation of protective device and the communication error of alarm signals.

# 2. Topology Analyses of Power System 

The protection is the first defending line for power system security. If a fault occurs in the power system, the protection will detect the fault by measuring relative electrical quantities, and then trip off the circuit breakers, thus to remove the fault section from the system. Therefore, there is a fixed correspondence between the sections and the protective devices, and the topology description of the power system is of great significance to the analysis of the protection logic.

# 2.1. Topology Description of Power System 

Taking a simple power system with four buses and four transmission lines as an example, the power network and the protection configuration are shown in Figure 1, where the transmission lines are equipped with main protection (m), primary backup protection (p) and secondary backup protection (s), and the buses are equipped with main protection (m). For example, the protection L1Am represent the main protection of line L1 at the bus A side. The detailed operating principle of the protections can be found in $[18,34]$.
![img-0.jpeg](img-0.jpeg)

Figure 1. The sample power system and its protection configuration.
According to the power network theory, a system with $m$ buses and $n$ lines can be described by an $m \times n$ dimensional incident matrix, and the non-zeros of the matrix represent the connection between the buses and lines. For the system in Figure 1, the incident matrix is shown in Figure 2a.

From Figure 1, it is obviously that the location of the protective devices is related to the system topology. For instance, the buses and lines are connected by circuit breakers, if the non-zeros of the incident matrix are replaced with the corresponding circuit breakers, the topology matrix of the circuit breaker can be obtained, as shown in Figure 2b.

Similarly, the protections are equipped to trip off corresponding circuit breakers, and thus they have direct correspondence in location. Therefore, the topology description of different kinds of protections can be obtained by replacing the non-zeros of the circuit breaker matrix with the corresponding relays, as shown in Figure 2c-f.

In order to establish the mapping relationship between the sections and the protective devices, the topology description of the buses and transmission lines is constructed according to their outlet connections, which can be obtained based on the incident matrix, as shown in Equations (1) and (2).

$$
\begin{aligned}
M & =\operatorname{Diag}\left\{M_{1}, \ldots, M_{m}\right\} \times S \\
L & =S \times \operatorname{Diag}\left\{L_{1}, \ldots, L_{n}\right\}
\end{aligned}
$$

where the "Diag" operation generates a $k \times k$ dimensional diagonal matrix which uses $k \times 1$ vectors as the diagonal elements. For the sample system, the topology matrices of the buses and transmission lines are shown in Figure 2g-h.

Note that the denotations of the sections and the protective devices are used to represent their state variables in the topology description, and the value can be 0 or 1 . For example, the value 1 represents the operation of the protective device or the fault state of the section; while the value 0 means the protective device doesn't operate or the section is normal.

$$
\begin{aligned}
& \boldsymbol{M m}=\left[\begin{array}{ccccc}
\mathrm{Am} & 0 & 0 & 0 \\
0 & \mathrm{Bm} & 0 & \mathrm{Bm} \\
\mathrm{Cm} & \mathrm{Cm} & \mathrm{Cm} & 0 \\
0 & 0 & \mathrm{Dm} & \mathrm{Dm}
\end{array}\right] \\
& L p=\left[\begin{array}{ccccc}
\mathrm{L} 1 \mathrm{Ap} & 0 & 0 & 0 \\
0 & \mathrm{~L} 2 \mathrm{Bp} & 0 & \mathrm{~L} 4 \mathrm{Bp} \\
\mathrm{~L} 1 \mathrm{Cp} & \mathrm{~L} 2 \mathrm{Cp} & \mathrm{~L} 3 \mathrm{Cp} & 0 \\
0 & 0 & \mathrm{~L} 3 \mathrm{Dp} & \mathrm{~L} 4 \mathrm{Dp}
\end{array}\right] \\
& M=\left[\begin{array}{cccc}
\mathrm{A} & 0 & 0 & 0 \\
0 & \mathrm{~B} & 0 & \mathrm{~B} \\
\mathrm{C} & \mathrm{C} & \mathrm{C} & 0 \\
0 & 0 & \mathrm{D} & \mathrm{D}
\end{array}\right] \\
& (\mathrm{g})
\end{aligned}
$$

L1 L2 L3 L4
$\boldsymbol{C B}=\begin{gathered}\mathrm{A}\left[\begin{array}{cccc}\mathrm{CB} 1 & 0 & 0 & 0 \\ 0 & \mathrm{CB} 3 & 0 & \mathrm{CB} 7 \\ \mathrm{C}\end{array}\right. \\ \mathrm{CB} 2 \mathrm{CB} 4 \mathrm{CB} 5 & 0 \\ \mathrm{D}\end{gathered}$
(b)
$\boldsymbol{L m}=\left[\begin{array}{cccc}\mathrm{L} 1 \mathrm{Am} & 0 & 0 & 0 \\ 0 & \mathrm{~L} 2 \mathrm{Bm} & 0 & \mathrm{~L} 4 \mathrm{Bm} \\ \mathrm{~L} 1 \mathrm{Cm} & \mathrm{L} 2 \mathrm{Cm} & \mathrm{L} 3 \mathrm{Cm} & 0 \\ 0 & 0 & \mathrm{~L} 3 \mathrm{Dm} & \mathrm{L} 4 \mathrm{Dm}\end{array}\right]$
(d)

$$
L s=\left[\begin{array}{ccccc}
\mathrm{L} 1 \mathrm{As} & 0 & 0 & 0 \\
0 & \mathrm{~L} 2 \mathrm{Bs} & 0 & \mathrm{~L} 4 \mathrm{Bs} \\
\mathrm{~L} 1 \mathrm{Cs} & \mathrm{~L} 2 \mathrm{Cs} & \mathrm{~L} 3 \mathrm{Cs} & 0 \\
0 & 0 & \mathrm{~L} 3 \mathrm{Ds} & \mathrm{~L} 4 \mathrm{Ds}
\end{array}\right]
$$

(f)

$$
L=\left[\begin{array}{cccc}
\mathrm{L} 1 & 0 & 0 & 0 \\
0 & \mathrm{~L} 2 & 0 & \mathrm{~L} 4 \\
\mathrm{~L} 1 & \mathrm{~L} 2 & \mathrm{~L} 3 & 0 \\
0 & 0 & \mathrm{~L} 3 & \mathrm{~L} 4
\end{array}\right]
$$

(h)

Figure 2. Topology description of the power system: (a) Incident matrix; (b) the circuit breaker matrix; (c) The bus protection matrix; (d) the main protection matrix; (e) the primary backup protection matrix; (f) the secondary backup protection matrix; (g) the bus matrix; (h) the transmission line matrix.

# 2.2. Expected States of the Protective Devices 

Considering that the main protection and primary backup protection are both local protection, their expected states are directly related to the local section. Besides, the expected state of the circuit breaker is determined by the corresponding protections. Therefore, the expected states of the main protection, primary backup protection and the circuit breaker can be directly determined by Equations (3)-(6).

$$
\begin{gathered}
\boldsymbol{L} \boldsymbol{m}^{*}=\boldsymbol{L} \\
\boldsymbol{M} \boldsymbol{m}^{*}=\boldsymbol{M} \\
\boldsymbol{L} \boldsymbol{p}^{*}=\boldsymbol{L} \odot \overline{\boldsymbol{L} \boldsymbol{m}} \\
\boldsymbol{C B}^{*}=\boldsymbol{L} \boldsymbol{m} \cup \boldsymbol{L} \boldsymbol{p} \cup \boldsymbol{L} s \cup \boldsymbol{M} \boldsymbol{m}
\end{gathered}
$$

where the superscript " $*$ " represents the expected state of the topology matrices, " $\odot$ " represents the element-by-element multiplication between matrices, " $\cup$ " denotes the logical element-by-element "or" operation of matrices, and the logical "not" operation of matrix is represented by overline. As the zeros

in $S$ are physically meaningless, the "not" operation is implemented by subtraction in this paper, such as $\overline{\boldsymbol{L m}}=\boldsymbol{S}-\boldsymbol{L} \boldsymbol{m}$.

The Equations (3) and (4) represent that if a fault occurs on the line or the bus, then the corresponding main protection should operate. Similarly, the Equation (5) means that if a fault occurs on the line but the local main protection fails to operate, then the primary backup protection should operate. The Equation (6) means that the circuit breaker should trip off if one of the corresponding protections operates.

Specially, the expected state of the secondary backup protection is determined not only by the local line, but also by the protected bus at the end of the line and the adjacent lines. Therefore, it should be separately analyzed according to the protected object.
(1) Protecting the local line: $\boldsymbol{L} \boldsymbol{s}_{1}$

If the fault occurs on the local line, but the corresponding main protection and primary backup protection both fail to remove the fault, then the secondary backup protection should operate. Therefore, the expected state can be determined as in Equation (7).

$$
\boldsymbol{L} \boldsymbol{s}_{1}^{*}=\boldsymbol{L} \odot \overline{\boldsymbol{L m}} \odot \overline{\boldsymbol{L p}}
$$

(2) Protecting the bus at the end of the line: $\boldsymbol{L} \boldsymbol{s}_{2}$

If the fault occurs on the bus at the end of the line, but the bus protection fails to remove the fault, then the secondary backup protection should operate. However, the topology matrices of the secondary backup protection and the bus do not directly correspond to each other in the protection relationship, the mapping transformation between them should be established.

According to the graph theory, the bus incident matrix $S_{M}$ can be obtained easily by the incident matrix as in Equation (8).

$$
S_{M}=S \otimes S^{\mathrm{T}}-I
$$

where " $\otimes$ " represents the logical multiplication operation, $S^{\mathrm{T}}$ is the transpose of $S$, and the identity matrix $\boldsymbol{I}$ is introduced to remove the self-correlation of the bus. For the sample system shown in Figure 1, the bus incident matrix is

$$
S_{M}=\begin{array}{c}
\text { A } \quad \text { B } \quad \text { C } \quad \text { D } \\
\text { A } \quad\left[\begin{array}{llll}
0 & 0 & 1 & 0 \\
0 & 0 & 1 & 1 \\
1 & 1 & 0 & 1 \\
0 & 1 & 1 & 0
\end{array}\right]
\end{array}
$$

Obviously, the non-zeros in $S_{M}$ represents the association between adjacent buses, it can be used to establish the mapping transformation between the secondary backup protection and the protected bus, therefore the expected state of the protection can be determined as in Equation (9).

$$
\boldsymbol{L} \boldsymbol{s}_{2}^{*}=\boldsymbol{S} \odot\left(\boldsymbol{S}_{M} \times(\boldsymbol{M} \odot \overline{\boldsymbol{C B}})\right)
$$

where the $\boldsymbol{C B}$ represents the related path between the secondary backup protection and the protected bus. The incident matrix $S$ is introduced here to ignore the elements without physical meaning. Taking the first column elements of $\boldsymbol{L} \boldsymbol{s}_{2}{ }^{*}$ as examples, according to the matrix multiplication rule, the results are

$$
\left\{\begin{array}{l}
\mathrm{L} 1 \mathrm{As}_{2} *=\mathrm{C} \times \overline{\mathrm{CB} 2} \\
\mathrm{~L} 1 \mathrm{Cs}_{2} *=\mathrm{A} \times \overline{\mathrm{CB} 1}
\end{array}\right.
$$

which mean that if a fault occurs on the bus C , while the breaker CB2 fails to trip off, then the protection L1As should operate; if a fault occurs on the bus A , while the breaker CB1 fails to trip off, then the protection L1Cs should operate. Obviously, the results meet the actual operating logic of the secondary backup protection.
(3) Protecting the adjacent line: $\boldsymbol{L s}_{3}$

If the fault occurs on the adjacent line, but the local protections fail to remove the fault, then the secondary backup protection should operate. Similarly, the topology matrices of the secondary backup protection and the line do not directly correspond to each other in the protection relationship.

To perform the mapping transformation, the three-order incident matrix between the bus and line can be calculated according to graph theory, as in (10).

$$
S_{3}=S \otimes S^{\mathrm{T}} \otimes S-S
$$

The non-zero in values in $S_{3}$ indicate that the corresponding bus and line are structurally separated by three circuit breakers, which is the same as the relationship between the secondary backup protection and the protected line. Therefore, the adjacent line matrix can be established by Equation (11), which is similar to Equation (2).

$$
\boldsymbol{L}_{3}=S_{3} \times \operatorname{diag}\left\{L_{1}, \ldots, L_{n}\right\}
$$

For the sample system, the adjacent line matrix is

$$
S_{3}=\left[\begin{array}{cccc}
0 & \mathrm{~L} 2 & \mathrm{~L} 3 & 0 \\
\mathrm{~L} 1 & 0 & \mathrm{~L} 3 & 0 \\
0 & 0 & 0 & \mathrm{~L} 4 \\
\mathrm{~L} 1 & \mathrm{~L} 2 & 0 & 0
\end{array}\right]
$$

In addition, the related path between the secondary backup protection and the protected adjacent line is constituted by the intermediate circuit breakers [29]. For example, the related path between the L1As and L2 is composed of CB2 and CB4, and the related path between the L1As and L3 is composed of CB2 and CB5. Obviously, the circuit breakers in the related path are all related to the bus at the end of the line, which is the same as the relationship between adjacent lines. Therefore, the related path matrix $\boldsymbol{P}$ can be obtained by applying the transformation of Equation (8) to the circuit break matrix $\boldsymbol{C B}$, as shown in Equation (12).

$$
\boldsymbol{P}=\boldsymbol{C B}^{\mathrm{T}} \otimes \boldsymbol{C B}-\boldsymbol{L}
$$

For the sample system, the related path matrix is:

$$
\boldsymbol{P}=\begin{array}{cccc}
\mathrm{L} 1 & \mathrm{~L} 2 & \mathrm{~L} 3 & \mathrm{~L} 4 \\
\mathrm{~L} 1 & 0 & \mathrm{CB} 4 \cdot \mathrm{CB} 2 & \mathrm{CB} 5 \cdot \mathrm{CB} 2 & 0 \\
\mathrm{~L} 2 & \mathrm{CB} 4 & 0 & \mathrm{CB} 5 \cdot \mathrm{CB} 4 & \mathrm{CB} 7 \cdot \mathrm{CB} 3 \\
\mathrm{~L} 3 & \mathrm{CB} 5 & \mathrm{CB} 4 \cdot \mathrm{CB} 5 & 0 & \mathrm{CB} 8 \cdot \mathrm{CB} 6 \\
\mathrm{~L} 4 & 0 & \mathrm{CB} 3 \cdot \mathrm{CB} 7 & \mathrm{CB} 6 \cdot \mathrm{CB} 8 & 0
\end{array}
$$

Therefore, if the fault occurs on the adjacent line and the circuit breakers on the related path fail to trip off, then the secondary backup protection is expected to operate, as shown in (13).

$$
\boldsymbol{L s}_{3}^{*}=\boldsymbol{S} \odot\left(\boldsymbol{L}_{3} \otimes \overline{\boldsymbol{P}}\right)
$$

Taking the first row and first column element of $\boldsymbol{L s}_{3}{ }^{*}$ as an example, according to the matrix multiplication rule, the result is

$$
\mathrm{L} 1 \mathrm{As}_{3^{*}}=\mathrm{L} 2 \times \overline{\mathrm{CB} 2 \cdot \mathrm{CB} 4}+\mathrm{L} 3 \times \overline{\mathrm{CB} 2 \cdot \mathrm{CB} 5}
$$

which means that if a fault occurs on L2, while both the breakers CB2 and CB4 fail to trip off, then the protection L1As should operate. Similarly, if a fault occurs on L3, while both the breakers CB2 and CB5 fail to trip off, then the protection L1As should also operate. Therefore, the above mapping transformation can effectively reflect the operating logic of secondary backup protection.

In summary, if one of the above three situations occurs, the secondary backup protection should operate. Therefore, the synthesized expected state of the secondary backup protection is determined by (14).

$$
L s^{*}=L s_{1}^{*} \cup L s_{2}^{*} \cup L s_{3}^{*}
$$

# 3. The Analytic Model for Fault Diagnosis Employing Topology Description 

The basic idea of the analytic model-based method is to formulate the fault diagnosis problem as a programming problem, and the key task is to establish an objective function that is able to evaluate the numerous fault hypotheses, so as to distinguish the true hypothesis from the false ones.

### 3.1. Objective Function of the Analytic Model

In the process of troubleshooting and power recovery, the most critical information for the dispatchers is to know where the fault occurred and how the fault was removed by the protection system. Therefore, the states of the sections and the protective devices are chosen as the fault hypothesis in this paper, such as $\boldsymbol{X}=[\boldsymbol{D}, \boldsymbol{R}, \boldsymbol{C}]$, where $\boldsymbol{D}$ represents the states of the sections, $\boldsymbol{R}$ represents the states of the protections and $\boldsymbol{C}$ represents the states of the circuit breakers.

Given this background, the deviation between the expected state and the actual state of the protective device represents the operating logic error, such as refusal-operation or mal-operation; while the deviation between the alarming state and the actual state characterizes the communication error, such as missing or misreporting of the alarm signals. Combining these two aspects, the objective function of the analytic model is constructed as

$$
\min E(\boldsymbol{X})=w_{1} \times E_{1}(\boldsymbol{X})+w_{2} \times E_{2}(\boldsymbol{X})
$$

where $w_{1}$ and $w_{2}$ are the weight factors, $E_{1}(\boldsymbol{X})$ represents the index of operating logic error, and $E_{2}(\boldsymbol{X})$ represents the index of communication error. The specific expressions of the indexes are as given as in Equation (16).

$$
\left\{\begin{aligned}
E_{1}(\boldsymbol{X}) & =\operatorname{Sum}\left(\left|\boldsymbol{L m}-\boldsymbol{L m}^{s}\right| \odot \overline{\boldsymbol{L m}_{P} \cup \boldsymbol{L m}_{S 1} \cup \boldsymbol{L m}_{S 2}}+\left|\boldsymbol{L p}-\boldsymbol{L p}^{s}\right| \odot \overline{\boldsymbol{L p}_{S 1} \cup \boldsymbol{L p}_{S 3}}+\left|\boldsymbol{L s}-\boldsymbol{L s}^{s}\right|\right. \\
& +\boldsymbol{T} \times\left(\left|\boldsymbol{M m}-M m^{s}\right| \odot \overline{\boldsymbol{M m}_{S 2}}\right)+\left|\boldsymbol{C B}-\boldsymbol{C B}^{s}\right|\right) \\
E_{2}(\boldsymbol{X}) & =\operatorname{Sum}\left(\left|\boldsymbol{L m}-\boldsymbol{L m}^{s}\right|+\left|\boldsymbol{L p}-\boldsymbol{L p}^{s}\right|+\boldsymbol{T} \times\left|\boldsymbol{M m}-\boldsymbol{M m}^{s}\right|+\left|\boldsymbol{L s}-\boldsymbol{L s}^{s}\right|+\left|\boldsymbol{C B}-\boldsymbol{C B}^{s}\right|\right) \\
\boldsymbol{T}= & \left(\operatorname{diag}\left(\boldsymbol{S} \times \mathbf{1}_{n}\right)\right)^{-1}
\end{aligned}\right.
$$

where the "Sum" operator implements the summation of all elements in the matrix, and the superscript " $a$ " is introduced to indicate the alarming state of the protective devices, if the alarm signal of the protective device is received, then its alarming state is determined as 1 ; otherwise it is determined as 0 . The intermediate variable $T$ is introduced to merge the influence of the bus protection since it is decomposed in the topology description. $\mathbf{1}_{n}$ represents the $n \times 1$ dimensional vectors with all elements equal to 1 .

Actually, the objective function in Equation (15) is established to evaluate the matching degree between the fault hypothesis and actual fault scenario. The closer the fault hypothesis is to the actual fault scenario, the smaller the objective function. It should be noted that the cooperative relationship between the protections is considered in the index of operating logic error, which is described in the form of corrective matrices, such as the $\boldsymbol{L} \boldsymbol{m}_{\mathrm{P}}, \boldsymbol{L} \boldsymbol{m}_{\mathrm{S} 1}, \boldsymbol{L} \boldsymbol{p}_{\mathrm{S} 1}, \boldsymbol{M} \boldsymbol{m}_{\mathrm{S} 2}, \boldsymbol{L} \boldsymbol{m}_{\mathrm{S} 3}, \boldsymbol{L} \boldsymbol{p}_{\mathrm{S} 3}$ which appeared in Equation (16). The specific meaning of the corrective matrices and their calculating method will be given in the next part.

Since the cooperative relationship between the protections are introduced into the logic error index, the inner logical constraint of the index is stronger than the communication error index. Therefore, the $w_{1}$ should be set greater than $w_{2}$, and in this paper they are set to be 0.6 and 0.4 respectively. A large number of tests show that the parameters can obtain satisfying results.

# 3.2. Determination of the Corrective Matrices 

Since the main protection and primary backup protection have the same protecting range, the operation of the primary backup protection can be used to correct the discrepancy caused by the main protection, as shown in Equation (17). Similarly, if the secondary backup protection is triggered by a fault on the local line, then its corrective matrices for the main protection and the primary backup protection can be determined as in Equation (18).

$$
\begin{gathered}
\boldsymbol{L} \boldsymbol{m}_{P}=\boldsymbol{L} \boldsymbol{p} \odot \boldsymbol{L} \boldsymbol{p}^{*} \\
\boldsymbol{L} \boldsymbol{m}_{S 1}=\boldsymbol{L} \boldsymbol{p}_{S 1}=\boldsymbol{L} \boldsymbol{s} \odot \boldsymbol{L} \boldsymbol{s}_{1}^{*}
\end{gathered}
$$

Noted that in Equations (17) and (18), the variable's meaning is indicated by the subscript. For instance, $\boldsymbol{L} \boldsymbol{m}_{P}$ represents the corrective matrix between the primary backup protection (p) and the line main protection (m), and $\boldsymbol{L} \boldsymbol{m}_{S 1}$ represents the corrective matrix between the secondary backup protection (S1) and the line main protection (m).

If the secondary backup protection is triggered by a fault on the bus at the end of the line, then its operation shall be considered to correct the corresponding bus protection. Since the mapping relationship here is the same as in Equation (9), the corrective matrix can be determined as in Equation (19).

$$
\boldsymbol{M} \boldsymbol{m}_{S 2}=\boldsymbol{S} \odot\left(\boldsymbol{S}_{\boldsymbol{M}} \times\left(\boldsymbol{L} \boldsymbol{s} \odot \boldsymbol{L} \boldsymbol{s}_{2}^{*}\right)\right)
$$

Similarly, if the secondary backup protection is triggered by a fault on the adjacent line, then its operation shall be considered to correct the local protections of the faulted line. According to the topology description, the mapping transformation between the protection and the protected adjacent lines can be divided into the following two steps: (1) mapping to bus at the end of the line, and (2) mapping to the adjacent lines. Obviously, the first step of the mapping transformation is the same as in Equation (19), and could be expressed as in Equation (20).

$$
\boldsymbol{L} s_{31}=\boldsymbol{S} \odot\left(\boldsymbol{S}_{\boldsymbol{M}} \times\left(\boldsymbol{L} \boldsymbol{s} \otimes \boldsymbol{L} \boldsymbol{s}_{3}^{*}\right)\right)
$$

In order to perform the second step of the transformation, the line incident matrix is required. Similar to Equation (8), the line incident matrix can be obtained by the incident matrix $S$, as shown in Equation (21).

$$
\boldsymbol{S}_{\boldsymbol{L}}=\boldsymbol{S}^{\mathrm{T}} \otimes \boldsymbol{S}-\boldsymbol{I}
$$

For the sample system, the result is:

$$
\boldsymbol{S}_{\boldsymbol{L}}=\begin{array}{c}
\text { L1 L2 L3 L4 } \\
\text { L1 } \\
\text { L2 } \\
\text { L3 } \\
\text { L4 }
\end{array}\left[\begin{array}{llll}
0 & 1 & 1 & 0 \\
1 & 0 & 1 & 1 \\
1 & 1 & 0 & 1 \\
0 & 1 & 1 & 0
\end{array}\right]
$$

The non-zeros in $\boldsymbol{S}_{\boldsymbol{L}}$ represent the association between adjacent lines, and thus can be used to perform the second step of the mapping transformation as Equation (22).

$$
\boldsymbol{L} \boldsymbol{s}_{32}=\boldsymbol{S} \odot\left(\boldsymbol{L} \boldsymbol{s}_{31} \times \boldsymbol{S}_{\boldsymbol{L}}\right)
$$

When protecting the adjacent lines, one secondary backup protection may protect multiple downstream lines, and one line may also be protected by many protections locate on the upstream lines. Therefore, the same mapping transformation is applied to the incident matrix $S$ to determine the number of backup protections.

$$
N_{s}=S \odot\left(S \times S_{L}\right)
$$

Finally, the corrective matrices between the main protection and the primary backup protection of the adjacent lines can be determined by Equation (24).

$$
L m_{S 3}=L p_{S 3}=S \odot\left(L s_{32}(c) N_{s}\right)
$$

where the " $\odot$ " operation performs the element by element comparisons between matrices.

# 3.3. Adaptability to Special Sections and Connection Modes 

The above modeling process is described primarily for the lines and buses. In fact, for the other kinds of power sections, such as the generator and the transformer, their protection configuration is similar to the line, that is, the main protection and the primary backup protection are equipped to protect the section itself, while the secondary backup protection operates to remove the fault on the adjacent section. Therefore, they can be thought as the line in the process of modeling (the generator can be considered as a single-ended line).

On the other hand, if the power grid is in $3 / 2$ wiring mode or double-bus mode, it is difficult to describe the topology structure directly by the incident matrix. To this end, the "virtual line" and "virtual bus" can be introduced for topology modeling according to the special connection, such as the L0 and B0 shown in Figure 3.
![img-1.jpeg](img-1.jpeg)

Figure 3. Schematic diagram for virtual line and virtual bus: (a) the virtual line; (b) the virtual bus.
It should be noted that there are no protections equipped for the virtual line and the virtual bus. In this way, it only needs to extend the incident matrix by one column or one row, the topology description of the $3 / 2$ wiring mode or double-bus mode can be realized, and there is no need to make big adjustments to the construction of the objective function.

In summary, all the calculation of the expected state matrices, corrective matrices and the objective functions are carried out based on the topology description, and the relationship between the sections and the protective devices are analyzed by simple matrix operations. Therefore, the objective function of the diagnosis problem can be easily generated online, which avoids the complex process of traversal search.

### 3.4. Framework of the Fault Diagnosis Method

The framework of the proposed fault diagnosis method is shown in Figure 4. When a fault occurs in the power system, the outage area can be firstly determined according to the switch states.

Under this situation, it only needs to establish the diagnosis model for the outage area, and therefore the diagnosis performance is independent with the system scale.
![img-2.jpeg](img-2.jpeg)

Figure 4. Framework of the fault diagnosis method.
Besides, the system only needs to communicate with the SCADA system, and the expected states of the protective devices as well as the objective function can be quickly established by simple matrix operations. The programming problem is then solved by an intelligent algorithm, and, based on the best solution the actual fault section can be estimated and the operating performance of the protective devices can be evaluated. The summarized and synthesized information is finally sent to the dispatcher for decision making.

In this paper, a genetic algorithm is chosen to solve the programming problem, and the number of the population is set to be 30 ; the roulette wheel selection is chosen to update the population in the selection process, and the selection ratio is 0.9 . In order to increase the diversity of the population, the one-point crossover is selected to recombine the population with a probability of 0.7 , and the mutation probability of the chromosome is set to be $0.7 / l$, where $l$ is the length of chromosome. Considering that the probability of communication errors is relatively small, the states of the protective devices in each chromosome (corresponding to the fault hypothesis) are initialized by randomly mutating 1 3 bits on the basis of the alarming states, thus speeding up the convergence of the algorithm.

# 4. Case Studies 

In this part, the IEEE 14-bus power system and a typical four-zone power system were selected to perform the case studies.

# 4.1. Test System \#1 

The IEEE 14-bus system shown in Figure 5 was first selected to illustrate the effectiveness of the method. This system contained 14 buses, 20 lines and 40 circuit breakers, and for easy of description, the sections and the protective devices were numbered according to the bus number. For example, the line connected with bus B09 and B14 was denoted as L0914, the circuit breaker near B09 was denoted as CB0914, and the circuit breaker in the other side was denoted as CB1409. Since the protection configuration is consistent with Figure 1, the modeling process was the same as the sample system except that the dimension of the topology matrices changes from $4 \times 4$ to $14 \times 20$.
![img-3.jpeg](img-3.jpeg)

Figure 5. The tested IEEE 14-bus power system.
A large number of cases were tested by the proposed method, and some of the testing results are listed in Table 1, where the cases 1 and 2 represent single fault scenarios with complete alarms. The case 3 represents a multi-fault scenario with complete alarms. Case 4 and 5 were multi-fault scenarios accompanied with abnormal operation of the protective devices, and case 6 further simulated the impact of information errors.

The convergence graphs of genetic algorithms for the cases are shown in Figure 6. Since the states of the protective devices in each chromosome were initialized by randomly mutating $1-3$ bits on the basis of the alarming states, the increase in dimensionality of the chromosome had little impact on the time-complexity of achieving optimized solution, and the genetic algorithm can converge to the optimal solution in the first 50 iterations for all the fault scenarios. The detailed fault diagnosis results are shown in the Table 1. Form Table 1, it is clear that fault diagnosis result can effectively explain the received alarms for both simple and complex fault scenarios, which demonstrates the correctness and effectiveness of the proposed method preliminary.

Table 1. Case studies of the IEEE 14-bus system.


![img-4.jpeg](img-4.jpeg)

Figure 6. Convergence graphs of the iterative process of the cases in Table 1: (a) case 1; (b) case 2; (c) case 3; (d) case 4; (e) case 5; (f) case 6.

# 4.2. Test System 2 

To further verify the effectiveness of the proposed method, the typical four-zone power system shown in Figure 7 [15] was also chosen to perform the case studies. The system consists of 12 buses, 8 lines, 8 transformers, and 40 circuit breakers. The protection configuration was similar with Figure 1, and the detailed protecting principle can be found in [15]. To describe the protections, the denotation "S" was used to represent the sending end of the line, which means the left or the upper side in Figure 7; similarly, the denotation "R" was used to represent the receiving end of the line, which means the right or the lower side. For example, the protection L2Rs represents the secondary backup protection at the receiving end of L2.

![img-5.jpeg](img-5.jpeg)

Figure 7. The tested four-zone power system.
Considering that four virtual lines should be introduced to establish the topology description, the dimension of the incident matrices was determined as $12 \times 20$, and the topology modeling process was exactly the same as the sample system mentioned above.

Some of the tested scenarios are listed in Table 2, where cases 1 and 2 simulated the single-fault and multi-fault scenarios with malfunction of the protective devices. Furthermore, cases 3-6 are used to simulate the complex fault scenarios with both the malfunction of the protective devices and the error alarm signals. Taking case 1 in Table 2 as an example, the detailed process of fault diagnosis is illustrated as follows.

According to the received alarms, the set of candidate sections in the outage area can be determined as $\{\mathrm{B} 1, \mathrm{~B} 2, \mathrm{~L} 2, \mathrm{~L} 4\}$, which is expressed as $D=\left\{d_{1}, \ldots, d_{4}\right\}$. Correspondingly, it can be further analyzed that there are 26 protections and 21 circuit breakers associated with the candidate sections, which can be expressed as $R=\{\mathrm{B} 1 \mathrm{~m}, \mathrm{~B} 2 \mathrm{~m}, \mathrm{~L} 2 \mathrm{Sm}, \mathrm{L} 2 \mathrm{Rm}, \mathrm{L} 4 \mathrm{Sm}, \mathrm{L} 4 \mathrm{Rm}, \mathrm{L} 2 \mathrm{Sp}, \mathrm{L} 2 \mathrm{Rp}, \mathrm{L} 4 \mathrm{Sp}, \mathrm{L} 4 \mathrm{Rp}, \mathrm{T} 1 \mathrm{Ss}, \mathrm{T} 2 \mathrm{Ss}, \mathrm{L} 1 \mathrm{Rs}$, L3Rs, L2Rs, L4Rs, T3Rs, T4Rs, L1Ss, L5Rs, L6Rs, T5Ss, T6Ss, L3Ss, L7Rs, L8Rs\} $=\left\{r_{1}, \ldots, r_{26}\right\}$ and $C=$ \{CB4, CB5, CB6, CB7, CB8, CB9, CB10, CB12, CB27, CB2, CB3, CB11, CB28, CB16, CB17, CB31, CB32, CB22, CB23, CB39, CB40\} $=\left\{c_{1}, \ldots, c_{21}\right\}$, respectively. Since the alarm of L7Sm has no association with the candidate sections, it is judged to be mal-operated device.

According to the aforementioned analysis, the fault hypothesis can be established as $X=\{D, R, C\}$ $=\left\{d_{1} \sim d_{4}, r_{1} \sim r_{26}, c_{1} \sim c_{21}\right\}$. Substituting the element in $X$ into the topology matrices, and the objective function can be established according to Equations (15) and (16). Finally, the optimization problem was solved by the genetic algorithm, which can converge in the first 100 iterations, and the best solution is

$$
X_{\text {best }}=\left\{\underbrace{1}_{\mathrm{B} 1} 000 \underbrace{1}_{\mathrm{B} 1 \mathrm{~m}} 0000000000000 \underbrace{11}_{\mathrm{L} 2 \mathrm{Rs}, \mathrm{~L} 4 \mathrm{Rs}} 0000000000 \underbrace{11}_{\mathrm{CB} 4, \mathrm{CB} 5} \underbrace{0}_{\mathrm{CB} 6} \underbrace{1}_{\mathrm{CB} 7} 0 \underbrace{1}_{\mathrm{CB} 9} \underbrace{0}_{\mathrm{CB} 12, \mathrm{CB} 27} 000000000000\right\}
$$

According to the best solution, it can be analyzed that only the section $d_{1}$ was equal to 1 , which means that the fault section was B 1 . Similarly, the real states of the corresponding protections and circuit breakers can be determined, from which we can identified that CB6 failed to operate in the fault removing process. The diagnosis process for other cases was similar, and the results of this method as well as some existing methods are shown in Table 2.

Table 2. Diagnosis results of the four-zone power system.


# 5. Discussion 

From the testing results, it can be seen that the method proposed in [28] cannot effectively solve the problem of uncertainty, and may get wrong results if there are missed or misreported alarms accompanied with the fault scenario. However, by introducing the actual states of the protective devices into the fault hypothesis, the method in this paper can effectively deal with the problems such as the malfunctions of the protective devices or the communication errors of the alarm signals, and the correct fault diagnosis results can be obtained.

Although the method proposed in [34] can get the correct diagnosis results, it has to introduce additional variables to represent the malfunctions of the protective devices or the communication errors of the alarm signals, which can increase the calculating dimension and lead to contradictory hypothesis. Compared with the objective function established in this paper, this method takes more time to solve the optimization problem.

Besides, the methods in [28] and [34] need to analyze the relationship between the sections and the protective devices by traversal search, and the process includes the selection of the protected sections as well as the analysis of the cooperative relationship of protections. The objective function can be established only if all protective devices have been traversed. Therefore, the modeling process of these methods will require a lot of computing time, even greatly exceed the solving time by the intelligence algorithm. The proposed method in this paper is based on the topology description of power system, and it only uses simple matrix operations to establish the objective function, and the modeling efficiency is improved.

All the cases listed in Tables 1 and 2 were performed in a personal computer with 2.3 GHz dual-core processor and 2G memory, using MATLAB programming. Including the modeling process and the iterative solution, the average calculating time of the cases in Tables 1 and 2 was no more than 10 s . However, if they are processed by the analytic models introduced in [28] and [34] with the same calculating environment and intelligence algorithm, the calculating time varies from one to three minutes according to the fault complexity, and most of the calculating time is used to generate the

objective function online. Therefore, the proposed method has a clear advantage in fault diagnosis speed, and can meet the demand of the online application.

On the other hand, since the analytic model is constructed based on the topology description, it is easy to adapt to the topology changes of the power system. Taking the sample system shown in Figure 1 as an example, if L4 is out of service due to maintenance, the only change is to set the elements corresponding to L4 in the topology matrices (the non-zeros in the 4th column) to zero, and there is no need to adjust the modeling process and iterative solution.

In summary, the proposed method is suitable for both simple and complex fault scenarios, and the fault section can be identified correctly even under complex conditions, such as the malfunctions of the protective devices or the communication errors of the alarm signals. Compared with the existing methods, the proposed method has better fault tolerance and can get satisfying results, and the topology modeling-based analytic method can greatly improve the effectiveness and flexibility of fault diagnosis. Besides, the operating performance of the protective devices can be effectively evaluated according to the best solution.

# 6. Conclusions 

A novel analytic method for power system fault diagnosis employing topology description is proposed in this paper. The topology description of the system is established based on the incident matrix, and the mapping transformation between the sections and the protective devices is studied by topological analysis. Based on these analyses, the expected state of the protective devices and the objective function of the analytic model can be automatically established by simple matrix operations. The optimization problem is then solved by the intelligent algorithm, and according to the best solution, the actual fault section can be identified and the operating performance of the protective devices can be evaluated. The case studies of the IEEE 14-bus system and the typical four-zone power system demonstrate the effectiveness and fault-tolerance of the proposed method.

In this paper, the typical genetic algorithm is used to solve the optimization problem and verify the effectiveness of the proposed method. Future research will focus on improving the efficiency of the algorithm, so as to further enhance the diagnosis performance. It should be noted that the topology-based modeling method proposed in this paper can also be applied to other kinds of fault diagnosis approaches, such as the expert system or the Petri nets-based methods.

Author Contributions: B.X., X.Y. and D.W. conceived and designed the research and case studies; B.X. performed the case studies and analyzed the results; B.X. and X.Y. contributed materials and analysis tools; B.X. and D.W. wrote and revised the paper; S.P. and Y.W. provided technical support.
Funding: This work was supported by the key project of smart grid technology and equipment of national key research and development plan of China under Grant 2017YFB0902900.
Conflicts of Interest: The authors declare no conflict of interest.
