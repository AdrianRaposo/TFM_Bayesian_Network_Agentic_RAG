# Experimental evaluation of quantum Bayesian networks on IBM QX hardware 

Sima E. Borujeni<br>Industrial, Systems, and<br>Manufacturing Engineering<br>Wichita State University<br>Wichita, USA<br>sxborujeni@shockers.wichita.edu<br>Elizabeth C. Behrman<br>Mathematics, Physics, and Statistics<br>Wichita State University<br>Wichita, USA<br>elizabeth.behrman@wichita.edu

Nam H. Nguyen
Boeing Research \& Technology
Huntington Beach, USA
nam.h.nguyen5@boeing.com

Saideep Nannapaneni<br>Industrial, Systems, and<br>Manufacturing Engineering<br>Wichita State University<br>Wichita, USA<br>saideep.nannapaneni@wichita.edu<br>James E. Steck<br>Aerospace Engineering<br>Wichita State University<br>Wichita, USA<br>james.steck@wichita.edu


#### Abstract

Bayesian Networks (BN) are probabilistic graphical models that are widely used for uncertainty modeling, stochastic prediction and probabilistic inference. A Quantum Bayesian Network (QBN) is a quantum version of the Bayesian network that utilizes the principles of quantum mechanical systems to improve the computational performance of various analyses. In this paper, we experimentally evaluate the performance of QBN on various IBM QX hardware against Qiskit simulator and classical analysis. We consider a 4-node BN for stock prediction for our experimental evaluation. We construct a quantum circuit to represent the 4-node BN using Qiskit, and run the circuit on nine IBM quantum devices: Yorktown, Vigo, Ourense, Essex, Burlington, London, Rome, Athens and Melbourne. We will also compare the performance of each device across the four levels of optimization performed by the IBM Transpiler when mapping a given quantum circuit to a given device. We use the root mean square percentage error as the metric for performance comparison of various hardware.


Index Terms-Bayesian Networks, Qiskit, IBM, Quantum circuit, Experimental, Transpiler

## I. INTRODUCTION

Quantum computing is a new paradigm of computing that uses the principles of quantum mechanical systems such as superposition and entanglement. This new paradigm has increasing been used to develop algorithms with superior computational performance when compared to classical counterparts [1], [2]. The principle of amplitude amplification [3] has been used to develop computationally efficient algorithms for risk analysis and inference in the context of Bayesian network models [4], [5]. Bayesian networks are probabilistic graphical models that are widely used for uncertainty representation and propagation, risk analysis, and probabilistic inference with applications in several domains of science, engineering, and healthcare such as transportation, logistics, bioinformatics, civil infrastructure, manufacturing, and radiotherapy treatment [6]. A Quantum Bayesian network (QBN) is a quantum version of the classical Bayesian network. In order to use the
developed quantum algorithms, the Bayesian networks should be represented on a quantum computing hardware.

In our prior work [6], we developed a generic approach to develop a quantum circuit on the IBM quantum gate architecture [7] to represent any given Bayesian network. We referred to this approach as Compositional Quantum Bayesian Network (C-QBN) as the overall circuit is obtained by composing smaller circuits relating to marginal/conditional probabilities of various nodes in the Bayesian network. More details are available in Section III. We demonstrated the developed approach using Qiskit, a Python package from IBM that simulates quantum computing [8].

In addition to the simulator, IBM also provides free access to a number of their real quantum devices with different capacities in terms of the number of qubits [9]. There are several 5 -qubit devices, a 15 qubit device and a simulator available through IBMQ experience, which is an online platform that is used to access the IBM quantum devices.

As these devices are physical systems, they are affected by several types of noise in the qubits, implementation of quantum gates and in the operating environment. Recently, several studies focus on evaluating the effect of noise, including decoherence, on performance of these devices and finding solutions to mitigate the noise[10]-[12]. The computational performance of algorithms that run on the devices also depends on the mapping of variables to various qubits in the devices. Even on the same device, the noise in the implementation of gates on various qubits is different. Since the number of gate operations applied on different qubits is different, it is desired to find the optimal mapping that minimizes the overall error.

To accomplish this, IBM provides a transpiler that outputs an optimal mapping to qubits on devices. Since different devices have different amounts of gate noise and different connectivity between qubits, the optimal mapping is output considering the gate noise and device connectivity. Assuming

all the qubits are connected to each other, the input circuit can be developed using either QASM or Qiskit, and given the choice of device, the transpiler provides a transformed circuit that can be run from that device [13]. Another input to the transpiler is the amount of optimization that needs to be performed to derive the transformed circuit. There are four levels of optimization, and each level results in a different transformed circuit. More details are available in Section IV.

The goal of this paper is to answer the following questions:

1. Can the existing IBM QX hardware simulate Bayesian networks?
2. Is there a variation in the simulation accuracy across various IBM QX hardware?
3. Is there a variation in the simulation accuracy across the four levels of optimization available in the transpiler?

Paper Organization: Section. II provides a brief background to Bayesian networks and various quantum gates. Section III discusses the C-QBN approach for the quantum ciruit representation of a QBN. Section. IV discusses various IBM QX hardware, their errors and different levels of the transpiler. Section. V discusses the evaluation study of executing an illustrative 4-node Bayesian network on various hardware and at different levels of optimization followed by concluding remarks and future work in Section VI.

## II. BACKGROUND

### A. Bayesian networks

A Bayesian Network (BN) is a directed acyclic graphical model with nodes and edges that are used to represent various random variables and dependence among them respectively. Mathematically, a Bayesian network represents a joint probability distribution over a set of random variables as a product of marginal and conditional probability distributions.

In a BN with $s$ nodes given by set $\mathbb{V}=\left\{V_{1},V_{2},...,V_{s}\right\}$, the joint distribution can be written as

$P\left(V_{1},V_{2},...,V_{s}\right)=\prod_{i=1}^{s}{P\left(V_{i} \mid \Pi_{V_{i}}\right)}$ (1)

where $\Pi_{V_{i}}$ refers to the set of parent nodes associated with $V_{i}$. For root nodes (nodes without parent nodes or the nodes at the top of a BN), $P\left(V_{i} \mid \Pi_{V_{i}}\right)$ becomes equal to $P\left(V_{i}\right)$.

Fig. 1 represents a simple BN with two discrete variables A and B, each of which can take two values - 0 and 1. Here, A is a root node and the parent node of B. For each value of the parent node (A=0,1), we will have a conditional probability table of the child node (B).


Fig. 1. An example of a two-node discrete Bayesian Network

### B. Quantum Gates

In this subsection, we will briefly introduce quantum gates that are later used in the development of quantum circuit using the C-QBN approach.

It is a well-known theorem that the set $G=\{H, T, S$, CNOT $\}$ formed a universal set of gates for quantum computing [1]. Any $n$-qubit unitary operation, represented by a $2^{n} \times 2^{n}$ matrix, can be approximated up to an arbitrary precision $\epsilon$ by a sequence of gates consisting of gates from the set $G$. The CNOT (Controlled-NOT) gate is two-qubit gate, where one qubit acts as a control qubit and the other qubit is the target qubit. The matrix representations of various gates using the computational basis of $\left|0\right\rangle$ and $\left|1\right\rangle$ are:

$$
\begin{gathered}
H=\frac{1}{\sqrt{2}}\left[\begin{array}{cc}
1 & 1 \\
1 & -1
\end{array}\right] \quad S=\left[\begin{array}{cc}
1 & 0 \\
0 & i
\end{array}\right] \quad T=\left[\begin{array}{cc}
1 & 0 \\
0 & e^{i \pi / 4}
\end{array}\right] \\
\text { CNOT }=\left[\begin{array}{cc}
I_{2 \times 2} & 0 \\
0 & X
\end{array}\right]
\end{gathered}
$$

Here, $I_{2 \times 2}$ is a $2 \times 2$ identity matrix. The quantum state of the target only changes by a Pauli X gate, when the control is in state $|1\rangle$ and where

$$
X=\left[\begin{array}{ll}
0 & 1 \\
1 & 0
\end{array}\right]
$$

Rather than being able to implement various single-qubit gates, $H, T$ and $S$, IBM hardware can implement an arbitrary single-qubit gate, $U_{3}(\theta, \phi, \lambda)$ by setting the three parameters, $\theta, \phi$ and $\lambda$. Here, $\theta$ represents the angle of rotation about the Y-axis, and $\phi$ and $\lambda$ represent the angles of rotation around the Z-axis in the Bloch sphere [6]. The matrix representation of $U_{3}$ gate is given as

$$
U_{3}(\theta, \phi, \lambda)=\left[\begin{array}{cc}
\cos \left(\frac{\theta}{2}\right) & -e^{i \lambda} \sin \left(\frac{\theta}{2}\right) \\
e^{i \phi} \sin \left(\frac{\theta}{2}\right) & e^{i(\phi+\lambda)} \cos \left(\frac{\theta}{2}\right)
\end{array}\right]
$$

However, any multi-qubit gate other than CNOT must be decomposed into a combination of CNOT and single-qubit gates before it can be implemented on the actual hardware.

The generic $U_{3}$ gate is often called simply $U$ gate. Implementing a general $U_{3}$ gate can be prone to hardware errors; therefore, IBM allows two additional single-qubit gates, $U_{2}$ and $U_{1}$, which are special cases of $U_{3} . U_{2}=U(\pi / 2, \phi, \lambda)$ and $U_{1}=U(0,0, \lambda)$ [9]. We can now represent the singlequbit rotation of $\theta$ around the Y-axis, $R_{Y}$ gate, as

$$
R_{Y}(\theta)=U_{3}(\theta, 0,0)=\left[\begin{array}{cc}
\cos \left(\frac{\theta}{2}\right) & -\sin \left(\frac{\theta}{2}\right) \\
\sin \left(\frac{\theta}{2}\right) & \cos \left(\frac{\theta}{2}\right)
\end{array}\right]
$$

A controlled-U gate, $C U$, is an an application of the gate $U$ to the target qubit(s) when the control qubit is $|1\rangle$. For example, the controlled- $R_{Y}, C R_{Y}$, performs the Y-axis

rotation of $\theta$ to the target qubit when the controlled qubit is in the state $\left|1\right\rangle$. It can be written as,

$$
C R_{Y}(\theta)=\left[\begin{array}{cc}
I_{2 \times 2} & 0 \\
0 & R_{Y}(\theta)
\end{array}\right]
$$

The $C U$ gate can be generalized to a general n-qubit controlled gate denoted as $C^{n} U$ for $n \geq 1$. Hence in general, $C^{n} U$ means a unitary operation $U$ will be applied to the target qubit(s) when all the $n$-controlled qubit(s) are in the state $\left|1\right\rangle$. CCNOT (or CCX or Toffoli) and $C C R_{Y}(\theta)$ are two examples. These are three-qubit gates, with two controlled qubits and one target qubit. The three-qubit gates are not elementary gates; therefore, they are required to be decomposed into a sequence of single-qubit and CNOT gates [13].

## III. Quantum BAYESIAN NETWORKS

In this section, we discuss the general approach to represent a Bayesian network on the IBM gate architecture using the gates discussed in Section II-B, and illustrate the approach for the two-node Bayesian network in Section II-A.
We follow three key ideas when representing a Bayesian network using the gate architecture given below [6].

1) Map each node in a BN to one or more qubits (based on the number of discrete states of the random variable)
2) Map the marginal/conditional probabilities of each node to the probability amplitudes (or probabilities) associated with various states of the qubit(s).
3) Obtain the desired probability amplitudes of various quantum states through (controlled) rotation gates.
In C-QBN approach, we represent the marginal/conditional probabilities of each node using appropriate (controlled) rotation gates, and we obtain the overall circuit of the BN by composing the rotation gates of various nodes in the order of the nodes in BN. We start with the root nodes, then represent all child nodes whose parents are the root nodes, and procedure is continued until all the nodes are represented in the quantum circuit. In Fig. 1, we begin with the root node (A), and then represent the child node (B).
We begin the circuit with the representation of root nodes using $R_{Y}$ gates. Applying the rotation gate $R_{Y}(\theta)$ transforms $\left|0\right\rangle$ to $\cos \left(\frac{\theta}{2}\right)\left|0\right\rangle+\sin \left(\frac{\theta}{2}\right)\left|1\right\rangle$. The probabilities associated with $\left|0\right\rangle$ and $\left|1\right\rangle$ states are $\cos ^{2}\left(\frac{\theta}{2}\right)$ and $\sin ^{2}\left(\frac{\theta}{2}\right)$ respectively. In Fig. 1, A is the root node with states 0 and 1. If $P(A=0)$ and $P(A=1)$ represent the probabilities of states 0 and 1 , then the rotation angle $\left(\theta_{A}\right)$ can be calculated as

$$
\theta_{A}=2 \times \tan ^{-1} \sqrt{\frac{P(\left|1\right\rangle)}{P(\left|0\right\rangle)}}=2 \times \tan ^{-1} \sqrt{\frac{P(A=1)}{P(A=0)}}
$$

Since the probabilities of a child node are dependent on the values of the parent nodes, we calculate rotation angles for every combination of parent node values, and implement these angles using controlled rotation gates, where the parent
nodes act as control qubits and the child node is the target qubit. In Fig. 1, B is the child node with A as the parent node. Since A can take two values, we will have two rotation angles of B $\left(\theta_{B, 0}\right.$ and $\left.\theta_{B, 1}\right)$ representing its probabilities for $A=0$ and $A=1$ respectively. Fig. 2 provides the quantum circuit of the Bayesian network in Fig. 1.
![img-0.jpeg](img-0.jpeg)

Fig. 2. Conceptual quantum circuit associated with the two-node Bayesian network in Fig. 1

In a $C R_{Y}(\theta)$ gate, the $R_{Y}(\theta)$ gate is applied on the target qubit when the control qubit is $\left|1\right\rangle$. Therefore, to represent the conditional probabilities of $B$ when $A=0$, we flip the qubit relating to A using the Pauli X gate (discussed in Section II-B), and flip it back after applying the controlled rotation. It should be noted that $C R_{Y}(\theta)$ is not an elementary gate but Qiskit allows for its application; however, it will be decomposed into a combination of CNOT and $R_{Y}(\theta)$ gates in the backend.
When the number of parent nodes is greater than 1, then the conditional probabilities of a child node are realized using higher-order controlled rotations $\left(C^{n} R_{Y}(\theta)\right)$. When $n>1$, Qiskit does not allow us to represent $C^{n} R_{Y}(\theta)$ gates directly. In order to represent such higher-order rotations, we will use additional qubits called ancilla qubits [6]. The example used in the evaluation study (Section V) uses ancilla qubits. Also, more details on representing higher-order controlled rotations are available in [6].

## IV. IBM QX HARDWARE

The nine quantum devices that are used in this study are Burlington, Ourense, Vigo, Essex, London, Rome, Athens, Yorktown, and Melbourne. Based on the number of qubits and the architecture, these devices can be divided into four groups. The first group consists of devices with five qubits in a T-shaped architecture. Devices in this group are Burlington, Ourense, Vigo, Essex and London. The second group includes devices with five qubits arranged in a line architecture. This group consists of two devices, Rome and Athens. The remaining two devices have two distinct architectures. Yorktown is a five-qubit device with qubits in a bow-tie configuration. Melbourne is a 15-qubit device where the qubits are arranged in a box configuration. In total, we have eight five-qubit devices and one with 15 qubits. The architectures of all the devices are shown in Figure 3. The circles represent the qubits and the arrows indicate the connectivity among the qubits.

Errors: Along with the architectures, Fig. 3 also provides color scales of two types of errors for each device: single-qubit $U_{2}$ and CNOT error rates. The colors of the qubits (circles) represent the $U_{2}$ error while the colors of the connections represent the CNOT error. It can be observed that different devices (even with the same architecture) have different singlequbit and CNOT error rates. The $U_{2}$ error is characterized

![img-1.jpeg](img-1.jpeg)

Fig. 3. IBM QX hardware devices along with the error rates for single-qubit and CNOT gates at the given calibration time

using randomized benchmarking method [14] where a qubit would be taken in a random walk over a route on the Bloch sphere that starts from state |0⟩ and the qubit is expected to go back to |0⟩ in the end. This walk is performed by applying a set of single qubit gates. Increasing the number of these gates will exponentially decrease the chance of going back to the initial state. This decay rate can be used to estimate the average error rate for those single-qubit gates [14]. The CNOT error rate is also estimated using a similar approach but using two-qubit Clifford gates [14].

Moreover, the error rates on various devices are periodically updated. Therefore, the Fig. 3 also provides a timestamp when these error snapshots are taken. From Fig. 3, it can be noticed that the calibration timestamps for Rome and Athens were more recent when compared against the other devices as they are recently made available by IBM to the public with free access.

**Transpiler:** As discussed in Section I, the transpiler is used to transpile a given circuit into a circuit that can be executed on a given quantum device after considering the single-qubit and CNOT error rates. Another input to the transpiler for transpiling a given quantum circuit is the optimization level. The optimization level determines the amount of optimization that needs to be performed in obtaining a transpiled circuit. There are four levels of optimization: *Level 0* (no optimization), *Level 1* (light optimization), *Level 2* (medium optimization), and *Level 3* (heavy optimization). As the optimization level increases, the transpilation time to obtain the optimal implementation of that circuit also increases [13].

At *Level 0*, there would not be any explicit optimization other than mapping a given circuit to the desired backend device. This is useful for characterization experiments such as randomized benchmarking [14] or error amplification where

![img-2.jpeg](img-2.jpeg)

Fig. 4. The Bayesian network of the stock prediction for an oil company [15]

we do not want the transpiler to apply any optimization [13]. At *Level 1*, the transpiler performs light optimization by collapsing adjacent gates; this combines a chain of single qubit gates (such as rotations) to one gate when feasible. *Level 2* optimization includes noise adaptive qubit mapping and gate cancellation by considering commutativity rules for the gates; and finally, *Level 3* optimization includes noise adaptive qubit mapping, gate cancellation using commutativity rules along with unitary synthesis. In Qiskit, the default level of optimization is *Level 1* [13].

## V. EVALUATION STUDY

In our evaluation study, we simulated the 4-node Bayesian network given in Fig. 4 on all the nine quantum devices discussed in Section IV along with IBM Qiskit simulator, and compared the results against classical analysis (performed

using Netica software [16]). The Bayesian network is obtained from [15], and is used for stock price prediction of an oil company. The variables IR (Interest Rate) and OI (Oil Industry) are the root nodes, and SM (Stock Market) and SP (Stock Price) are the child nodes; these are discrete variables with two values, 0 and 1. In this example, we have two root nodes (IR and OI), and two child nodes, one with one parent node (SM) and the other with two parent nodes (SM, OI).

Quantum Circuit: First, we construct the quantum circuit using the Qiskit package following the procedure discussed in Section III. This circuit is then run on all the nine hardware devices and the simulator. We considered 8192 shots in each run, as it is the highest number of shots allowed on the IBM devices. The results from each run are used to compute the marginal probabilities of all the nodes. Since each variable takes two values, we will have two marginal probability values, and the sum of them is equal to unity. Therefore, we computed only the probabilities of all the variables being equal to 0 as the probabilities equal to 1 can be obtained by subtracting from unity. Since the measurements obtained from quantum circuits are probabilistic in nature (probabilities based on probability amplitudes of qubits), we performed 10 runs on each device (each run with 8192 shots) and obtained the mean and standard deviation values of the marginal probabilities across the 10 runs. Moreover, we considered all the four optimization levels for each hardware device. This comparison lets us investigate the effect of hardware noise on the accuracy of the results at different optimization levels.

To ensure that the experimental conditions remain constant throughout the runs, all the experiments for each computer were performed simultaneously at the same calibration for all the runs [17]. In this way, the variation of noise over time would have the minimal effect on the results.

Fig. 5 provides the circuit corresponding to the Bayesian network in Fig. 4. Since SP has two parent nodes, we will need to implement $C C R_{Y}(\theta)$ gates to realize its conditional probabilities. As discussed in Section III, implementation of $C C R_{Y}(\theta)$ requires the use of an ancilla qubit. Therefore, the quantum circuit in Fig. 5 has five qubits, and a measurement bit to store the measurements. In Fig. 5, $q_{1}$ represents the ancilla and qubits $q_{4}, q_{3}, q_{2}$ and $q_{0}$ correspond to variables IR, OI, SM, and SP respectively. $C C R_{Y}(\theta)$ gate is decomposed into a combination of $C R_{Y}(\theta)$ and CCNOT gates using the ancilla qubit.

Results: Table I provides the mean and standard deviation values of marginal probabilities when run of various IBM hardware at different optimization levels compared with the results from Qiskit simulator and classical analysis. The calibration timestamp and the errors of single-qubit and CNOT gates when the runs are performed are the same as given in Fig. 3. Since the simulator is not affected by noise, the results are the same across all the optimization levels.

Performance comparison: For comparison of results in Table I, we calculated the root mean square percentage error (RMSPE) using the expression in Eq. 6. The RMSPE error values are given in Table II.

TABLE I
MEAN AND STANDARD DEVIATION VALUES OF MARGINAL PROBABILITIES OVER 10 RUNS ON 9 IBM QX HARDWARE COMPARED WITH THE QISKIT SIMULATOR AND CLASSICAL ANALYSIS (NETICA)


$$
\epsilon_{T}=100 \%\sqrt{\frac{1}{n} \sum_{i}\left(\frac{p_{i}^{t}-\hat{p}_{i}}{p_{i}^{t}}\right)^{2}}
$$

Here, $\epsilon_{T}$ is the RMSPE, $p_{i}^{t}$ and $\hat{p}_{i}$ are the true and expectation values (over 10 runs). The true values are obtained from classical analysis, using Netica software.

TABLE II
ERROR RATES ON VARIOUS IBM QX HARDWARE AT DIFFERENT OPTIMIZATION LEVELS


![img-3.jpeg](img-3.jpeg)

Fig. 5. Quantum Circuit of the stock prediction Bayesian network (Fig. 4) constructed in IBM Qiskit

![img-4.jpeg](img-4.jpeg)

Fig. 6. Box plots associated with marginal probability values from all the nine IBM QX hardware at Level 3 optimization, Qiskit, and classical analysis

We make the following observations from Table II.

1. The results from the simulator are almost the same as the results from classical analysis.
2. For most devices (Burlington, Ourense, London, Essex, Rome, Athens, and Melbourne), the percentage error decreases with increase in the optimization level.
3. The error rate for Yorktown is the least at all the optimization levels when compared against all the hardware (at *Level 3*, the error rate for Yorktown was slightly higher than Essex but only by 0.7%).
4. The best result across different optimization levels and various hardware is by Yorktown at *Level 0* optimization.
5. Of all the devices, the error rate significantly decreased for Essex across various optimization levels (30.7% at *Level 0* to 9.1% at *Level 3*).

Since most devices have the best performance at *Level 3* optimization, we provided box plots in Fig. 6 for all the marginal probabilities to study the variation in results across the 10 runs. In Fig. 6, the devices are available on the X-axis while probabilities are plotted on the Y-axis. The red line in each plot represents the true probability obtained from classical analysis. For a fair comparison, we used the same scale on Y-axis in all the plots. In Fig. 6, Yorktown has the largest ranges across all devices; this is particularly evident in the first plot corresponding to P(IR=0).

### VI. CONCLUSION

This paper discussed an experimental evaluation of the performance of nine IBM QX hardware (Burlington, Vigo, Ourense, London, Essex, Yorktown, Rome, Athens, and Melbourne) in simulating a Quantum Bayesian network. First, we developed a quantum circuit to represent the Bayesian network using Qiskit, which is Python package for simulating quantum computation. The circuit is then transpiled to run on various hardware, and their performance was compared against that from Qiskit and classical analysis. We also considered all the four levels of optimization (no, light, medium, and heavy optimization) when obtaining a transpiled circuit. On each device, we performed 10 runs, each run with 8192 shots. We used the root mean squared percentage error as a metric to compare the performance of various devices.

We observed that the performance of most devices (6 out of 9) improved with the optimization level. We observed the best performance for Yorktown at all the optimization levels. From the results, we conclude that the existing hardware is not very effective in simulating Quantum Bayesian network due to hardware noise. The error rate is significant even in a small Bayesian network (with 4 nodes), and we can expect the error rates to increase in more complex Bayesian networks. One way to reduce the error rate could be by developing fault-tolerant circuits and performing fault-tolerant computation.

As our future work, we will consider designing fault tolerant circuits to manage the hardware noise and improve the simulation performance of Quantum Bayesian networks. We will also investigate techniques to develop circuits with lower depths as fewer gates can lead to overall less noisy measurements from the designed circuits.
