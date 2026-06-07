# Quantum circuit representation of Bayesian networks 

Sima E. Borujeni ${ }^{\mathrm{a}}$, Saideep Nannapaneni ${ }^{\mathrm{a}, *}$, Nam H. Nguyen ${ }^{\mathrm{b}, 1}$, Elizabeth C. Behrman ${ }^{\mathrm{b}}$, James E. Steck ${ }^{\mathrm{c}}$<br>${ }^{a}$ Department of Industrial, Systems, and Manufacturing Engineering, Wichita State University 1845 Fairmount St, Box 35, Wichita, KS, 67260 USA<br>\{szborujeni@shockers.wichita.edu, saideep.nannapaneni@wichita.edu\}<br>${ }^{\mathrm{b}}$ Department of Mathematics, Statistics, and Physics, Wichita State University 1845 Fairmount St, Box 33, Wichita, KS, 67260 USA<br>\{nhnguyen5@shockers.wichita.edu, elizabeth.behrman@wichita.edu\}<br>${ }^{\text {c }}$ Department of Aerospace Engineering, Wichita State University 1845 Fairmount St, Box 44, Wichita, KS, 67260 USA<br>\{james.steck@wichita.edu\}

## Abstract

Probabilistic graphical models such as Bayesian networks are widely used to model stochastic systems to perform various types of analysis such as probabilistic prediction, risk analysis, and system health monitoring, which can become computationally expensive in large-scale systems. While demonstrations of true quantum supremacy remain rare, quantum computing applications managing to exploit the advantages of amplitude amplification have shown significant computational benefits when compared against their classical counterparts. We develop a systematic method for designing a quantum circuit to represent a generic discrete Bayesian network with nodes that may have two or more states, where nodes with more than two states are mapped to multiple qubits. The marginal probabilities associated with root nodes (nodes without any parent nodes) are represented using rotation gates, and the conditional probability tables associated with non-root nodes are represented using controlled rotation gates. The controlled rotation gates with more than one control qubit are represented using ancilla qubits. The proposed approach is demonstrated for three examples: a 4-node oil company stock prediction, a 10-node network for

[^0]
[^0]:    *Corresponding author. Phone: +1 316-978-6240
    ${ }^{1}$ Present address: Boeing Research \& Technology, Huntington Beach, CA 92647, USA

liquidity risk assessment, and a 9-node naive Bayes classifier for bankruptcy prediction. The circuits were designed and simulated using Qiskit, a quantum computing platform that enables simulations and also has the capability to run on real quantum hardware. The results were validated against those obtained from classical Bayesian network implementations.

Keywords: Bayesian network, Quantum, Circuit, Qiskit, Qubit, Finance

# 1. Introduction 

Bayesian Networks, also known as Bayesian belief networks, are probabilistic graphical models used to represent knowledge about an uncertain domain. A Bayesian network is represented as a directed acyclic graph with nodes and edges, where nodes represent the random variables and edges represent the probabilistic dependence between nodes (Murphy \& Russell, 2002).

Bayesian networks are used to perform two types of analysis: forward analysis, which provides a probabilistic prediction of the lower-level nodes in the Bayesian networks using probability distributions of the higher-level nodes, and inverse analysis, which infers the values of higher-level nodes using data on the lower-level nodes. The inverse analysis is commonly referred to as Bayesian inference since the inference analysis is carried out using the Bayes theorem. The forward analysis is typically performed through Monte Carlo analysis and has been used to perform uncertainty propagation (Nannapaneni et al., 2016), performance evaluation (Zhu \& Deshmukh, 2003), reliability and risk analysis (Garvey et al., 2015), and prognostics (Ferreiro et al., 2012), whereas the inverse analysis has been used for system identification (Lee \& Song, 2016), health monitoring (Kothamasu et al., 2006), and system diagnostics (Li et al., 2017). Bayesian networks have been used to carry out a variety of analyses in several domains of science and engineering such as mechanical ( $\mathrm{Xu}, 2012$ ), aerospace (Li et al., 2017; Nannapaneni et al., 2018a), and manufacturing systems (Büyüközkan et al., 2015; Nannapaneni et al., 2018b), industrial systems (Cai et al., 2016), healthcare (Kahn Jr et al., 1997; Kalet et al., 2015), infrastruc-

ture systems (Hosseini \& Barker, 2016; Nannapaneni et al., 2017), biomedical systems (Miyauchi \& Nishimura, 2018), and transportation (Sun et al., 2006; Pettet et al., 2017).

Some of the issues with the current implementations of Bayesian networks is the high computational expense in the presence of large number of nodes (random variables) for both forward and inverse analyses. One possible way to obviate this difficulty might be to use the principles of quantum computing (sometimes referred to as quantum-assisted computing). This is because quantum computers make use of "superposition" which is the ability of quantum systems to be simultaneously in multiple different states.

Several algorithms have been developed using the principles of quantum mechanics that have demonstrated superior computational performance over the corresponding classical algorithms, and the most notable of these are Shor's algorithm (Shor, 1994) and Grover's algorithm (Grover, 1996). Shor's algorithm is used for the factorization of integers; this algorithm has exponential speedup when compared to the best known classical algorithms. Grover's algorithm is used for search in an unstructured search space (such as an unstructured database), and has quadratic speedup. Due to its computational benefits, the Grover's algorithm has been used as a sub-routine in the development of many quantum algorithms for classification such as quantum support vector machines (Rebentrost et al., 2014), for clustering such as quantum k-means clustering (Aïmeur et al., 2007), and for combinatorial optimization (Baritompa et al., 2005). With regard to Bayesian networks, Ozols et al (Ozols et al., 2013) used the principles of amplitude amplification (Brassard et al., 2002) to develop an algorithm for Bayesian inference (inverse analysis) known as quantum rejection sampling, which is a quantum version of the rejection sampling algorithm (Gilks \& Wild, 1992) used for inference in classical Bayesian networks. Woerner and Egger (Woerner \& Egger, 2019) used the principles of amplitude amplification and estimation (Brassard et al., 2002) to perform risk analysis (forward analysis), and demonstrated it with two toy problems from the financial industry. In this paper, we consider the representation of Bayesian networks in a quan-

tum computing paradigm to facilitate the use of those quantum algorithms for forward and inverse analyses.

There are primarily two types of architectures that have widely been used to realize quantum computing: quantum gate models (Dallaire-Demers \& Wilhelm, 2016) and quantum annealing (Bunyk et al., 2014). The quantum gate architecture uses a series of quantum gates that act on individual qubits to achieve the desired computation.

More details regarding qubits and gates are available in Sections 2.1 and 2.2. A quantum circuit is a graphical representation of the sequence of gates implemented on various qubits to do the desired computation. Quantum annealing architecture uses the principles of quantum annealing (Boixo et al., 2013), which is a quantum equivalent to classical simulated annealing algorithm, to make the desired computation. According to Ajagekar et al (Ajagekar et al., 2020), quantum annealing architecture is better suited for optimization problems whereas quantum gate architecture facilitates universal quantum computation. As the goal of this paper is the representation of Bayesian networks, we use the quantum gate architecture as opposed to the quantum annealing architecture.

Quantum Bayesian networks were first introduced by Tucci (1995) as an analog to classical Bayesian networks . He proposed that the conditional probabilities in a classical Bayesian networks can be represented using quantum complex amplitudes. Tucci argued that there could be infinite possible quantum Bayesian network for a given classical Bayesian network; however, methods to realize a quantum Bayesian network for a classical Bayesian network were not available. Moreira \& Wichert (2016) proposed quantum-like Bayesian networks, where the marginal and conditional probabilities were represented using quantum probability amplitudes. To determine the parameters of a quantum Bayesian network, a similarity heuristic method was used which considered similarity between two dimensional vectors corresponding to the two states of the random variables.

Previous work considered quantum Bayesian networks with binary variables only and considered heuristics approaches for their representation; however, this

paper also considers representation of variables with more than two states. The approach presented in this paper does not consider any heuristics and can be used to represent any generic discrete quantum Bayesian network.

Low et al. (2014) discussed the principles of quantum circuit design to represent a Bayesian network with discrete nodes that have two states, and also discussed the circuit design for implementing quantum rejection sampling for inference. In this paper, we consider the representation of generic discrete Bayesian networks with nodes that may have two or more states, and also discuss the decomposition of complex gates using elementary gates (discussed in Section 2.2) such that they can be implemented on available quantum computing platforms.

Paper Contributions: The overall contributions made through this paper are: (1) Decomposition of a multi-qubit gate into elementary gates to represent a discrete variable with more than two states; (2) A systematic procedure to design a quantum circuit to represent a generic discrete Bayesian network with nodes that may have two or more states; and (3) Illustration of the proposed quantum circuit representation to three Bayesian networks used for oil price stock prediction, liquidity risk assessment, and bankruptcy prediction, and validating the results against classical Bayesian network implementations.

Paper Organization: Section 2 provides a brief background to qubits, quantum gates, and Bayesian networks. Section 3 details the proposed methods for designing a quantum circuit to represent a Bayesian network. Section 4 details the application of the proposed methods to three Bayesian networks from the financial industry followed by concluding remarks in Section 5.

# 2. Background 

In this section, we provide a brief background to qubits, different quantum gates that are used to perform qubit transformations, and Bayesian Networks.

### 2.1. Qubit

A qubit (or a quantum bit) is an elementary unit of information in quantum computing, similar to a classical bit (or simply a bit) in classical computing. A

bit is always in one of the either two basis states, 0 and 1 , whereas a qubit can be in both the basis states simultaneously. This property of a qubit is known as quantum superposition (Nielsen \& Chuang, 2002). In quantum computing, the Dirac notation is used to represent the two basis states as $|0\rangle$ and $|1\rangle$. In general, any two orthonormal states can be used as the basis states but the commonly used basis states or computational basis are $|0\rangle$ and $|1\rangle$. Eq. (1) provides their vector representations as

$$
|0\rangle=\left[\begin{array}{l}
1 \\
0
\end{array}\right] \quad|1\rangle=\left[\begin{array}{l}
0 \\
1
\end{array}\right]
$$

A general pure state of a qubit is a superposition, which is linear combination of the two basis states written as $|\Psi\rangle=c_{1}|0\rangle+c_{2}|1\rangle$ or

$$
\left[\begin{array}{l}
c_{1} \\
c_{2}
\end{array}\right]=c_{1}\left[\begin{array}{l}
1 \\
0
\end{array}\right]+c_{2}\left[\begin{array}{l}
0 \\
1
\end{array}\right]
$$

where $c_{1}$ and $c_{2}$ are complex numbers, which represent the probability amplitudes corresponding to $|0\rangle$ and $|1\rangle$ respectively. When a measurement is made, the qubit collapses to one of the two basis states. The probabilities of observing the qubit in $|0\rangle$ and $|1\rangle$ states are computed as the inner product of their probability amplitudes and their complex conjugates, represented as $c_{1}^{\dagger} c_{1}=\left|c_{1}\right|^{2}$ and $c_{2}^{\dagger} c_{2}=\left|c_{2}\right|^{2}$ respectively, where $c_{1}^{\dagger}$ and $c_{2}^{\dagger}$ are the complex conjugates of $c_{1}$ and $c_{2}$ respectively. Since a qubit can be either in $|0\rangle$ or in $|1\rangle$, the sum of their probabilities is equal to unity $\left(\left|c_{1}\right|^{2}+\left|c_{2}\right|^{2}=1\right)$ (Kopczyk, 2018).

When multiple qubits are used in computing, their joint state can be obtained through a tensor product of individual qubits. If $\left|\Psi_{1}\right\rangle=a_{1}|0\rangle+a_{2}|1\rangle$ and $\left|\Psi_{2}\right\rangle=b_{1}|0\rangle+b_{2}|1\rangle$ represent two qubits with real-valued probability amplitudes, then their joint state is represented as $\left|\Psi_{1}\right\rangle \otimes\left|\Psi_{2}\right\rangle=a_{1} b_{1}|00\rangle+a_{1} b_{2}|01\rangle+$ $a_{2} b_{1}|10\rangle+a_{2} b_{2}|11\rangle$. But the joint state need not always be a product state (tensor product of individual states). There are states of the joint system that can not be written as a product of individual states; these are called entangled states (Horodecki et al., 2009). Entanglement is quantum correlation stronger

![img-0.jpeg](img-0.jpeg)

Figure 1: Bloch sphere representation of a qubit
than any possible classical correlation (Luo \& Luo, 2003).
An example of an entangled state of two qubits is the Bell state, defined as $\frac{1}{\sqrt{2}}|00\rangle+\frac{1}{\sqrt{2}}|11\rangle$ (Nielsen \& Chuang, 2002). Clearly, it can not be written as a tensor product of two qubits, $\left|\Psi_{1}\right\rangle=a_{1}|0\rangle+a_{2}|1\rangle$ and $\left|\Psi_{2}\right\rangle=b_{1}|0\rangle+b_{2}|1\rangle$, because then $a_{1} b_{1}=a_{2} b_{2}=\frac{1}{\sqrt{2}}$ but also $a_{1} b_{2}=a_{2} b_{1}=0$. Thus, neither qubit has an individual state, but the two are perfectly correlated. If one of the two qubits is measured to be in $|0\rangle$ state, then the other qubit is also in $|0\rangle$ due to the presence of entanglement between them.

A Bloch sphere (shown in Figure 1) is often used for geometrical representation of a qubit (Goyal et al., 2016). In a Bloch sphere, the positive Z-axis corresponds to the $|0\rangle$ state while the negative Z-axis corresponds to $|1\rangle$ state. A pure state of a qubit is represented by a point on the Bloch sphere and can be represented as $\cos \left(\frac{\theta}{2}\right)|0\rangle+e^{i \phi} \sin \left(\frac{\theta}{2}\right)|1\rangle$ for given values of $(\theta, \phi)$.

# 2.2. Quantum gates 

Quantum gates are mathematical operations performed on the qubits to change their probability amplitudes to gain the desired computations. The quantum gates are similar to classical gates (such as the AND gate) acting on classical bits. Geometrically, one-qubit gates represent unitary rotations about various axes in the Bloch sphere.

There are two elementary gates in quantum computing - $U_{3}$ and CNOT (McKay et al., 2018), which act on a single qubit and two qubits respectively. Any other multi-qubit gates can be decomposed into these elementary gates. We discuss in detail the one-qubit and two-qubit elementary gates. A more comprehensive review of gates is available in Nielsen \& Chuang (2002).

# 2.2.1. One-qubit gates 

We review the generic $U_{3}$ gate, and some of its special cases - $X$ (sometimes referred to as Pauli- $X$ ), $R_{Y}$ and $R_{Z}$ gates. $U_{3}$ gate has three parameters $\theta, \phi$ and $\lambda$, and it can be used to construct any arbitrary single qubit gate. The matrix representation of this gate is given as

$$
U_{3}(\theta, \phi, \lambda)=\left[\begin{array}{cc}
\cos \left(\frac{\theta}{2}\right) & -e^{i \lambda} \sin \left(\frac{\theta}{2}\right) \\
e^{i \phi} \sin \left(\frac{\theta}{2}\right) & e^{i(\phi+\lambda)} \cos \left(\frac{\theta}{2}\right)
\end{array}\right]
$$

where $\theta$ represents the angle of rotation about the Y-axis, and $\phi$ and $\lambda$ represent the angles of rotation around the Z-axis. The generic $U_{3}$ gate is often represented as the $U$ gate.
$R_{Y}$ gate: The $R_{Y}$ gate is a single-qubit gate, which corresponds to a rotation of angle $\theta$ (radians) about the y-axis on the Bloch sphere. $R_{Y}$ gate can be represented as a special case of $U_{3}$ gate as

$$
R_{Y}(\theta)=U_{3}(\theta, 0,0)=\left[\begin{array}{cc}
\cos \left(\frac{\theta}{2}\right) & -\sin \left(\frac{\theta}{2}\right) \\
\sin \left(\frac{\theta}{2}\right) & \cos \left(\frac{\theta}{2}\right)
\end{array}\right]
$$

$R_{Z}$ gate or Phase-shift gate: $R_{Z}(\lambda)$ is another single qubit gate, which corresponds to rotation about the Z-axis by an angle $\lambda$ on the Bloch sphere. $R_{Z}$ gate can be represented as a special case of $U_{3}$ as

$$
R_{Z}(\lambda)=U_{3}(0,0, \lambda)=\left[\begin{array}{cc}
1 & 0 \\
0 & e^{i \lambda}
\end{array}\right]
$$

Using the matrix representations of $R_{Y}$ and $R_{Z}$ gates, the $U_{3}$ gate given in Eq. (3) can be decomposed into two phase-shift rotations and one rotation

about the Y-axis as

$$
\begin{aligned}
U_{3}(\theta, \phi, \lambda) & =\left[\begin{array}{cc}
1 & 0 \\
0 & e^{i \phi}
\end{array}\right]\left[\begin{array}{cc}
\cos \left(\frac{\theta}{2}\right) & -\sin \left(\frac{\theta}{2}\right) \\
\sin \left(\frac{\theta}{2}\right) & \cos \left(\frac{\theta}{2}\right)
\end{array}\right]\left[\begin{array}{cc}
1 & 0 \\
0 & e^{i \lambda}
\end{array}\right] \\
& =R_{Z}(\phi) R_{Y}(\theta) R_{Z}(\lambda)
\end{aligned}
$$

For more detail about the rotation gates and decomposition of an arbitrary single qubit gate, refer to Nielsen \& Chuang (2002) and Cross et al. (2017).

X gate: The $X$ gate is the quantum-equivalent to the classical NOT gate or sometimes referred to as flip gate, as it flips $|0\rangle$ to $|1\rangle$ and $|1\rangle$ to $|0\rangle$. The matrix notation of the $X$ gate is equal to

$$
X=U_{3}\left(\pi,-\frac{\pi}{2}, \frac{\pi}{2}\right)=\left[\begin{array}{cc}
0 & 1 \\
1 & 0
\end{array}\right]
$$

# 2.2.2. Two-qubit gates 

An elementary two-qubit gate is the controlled-NOT (CNOT or $C X$ ) gate. The two qubits on which the CNOT gate is implemented are referred to as the control qubit and target qubit. When the control qubit is $|0\rangle$, the target qubit remains unchanged whereas when the control qubit is $|1\rangle$, the $X$ gate is implemented on the target qubit. The CNOT gate does not have any effect on the control qubit (Liu et al., 2008). In the usual computational basis $(|00\rangle,|01\rangle,|10\rangle$, and $|11\rangle$ states),the matrix representation of a CNOT gate is given as

$$
C N O T=\left[\begin{array}{llll}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{array}\right]
$$

For example, consider two qubits given as $\left|\Psi_{1}\right\rangle=a_{1}|0\rangle+a_{2}|1\rangle$ and $\left|\Psi_{2}\right\rangle=$ $b_{1}|0\rangle+b_{2}|1\rangle$ on which a CNOT gate is implemented with $\left|\Psi_{1}\right\rangle$ as the control qubit. The combined quantum state before the application of CNOT gate is

given by their tensor product, $\left|\Psi_{1}\right\rangle \otimes\left|\Psi_{2}\right\rangle=a_{1} b_{1}|00\rangle+a_{1} b_{2}|01\rangle+a_{2} b_{1}|10\rangle+$ $a_{2} b_{2}|11\rangle$. The quantum state after the application of the CNOT gate is equal to $a_{1} b_{1}|00\rangle+a_{1} b_{2}|01\rangle+a_{2} b_{1}|11\rangle+a_{2} b_{2}|10\rangle$. The $|00\rangle$ and $|01\rangle$ remain unchanged since the control qubit is $|0\rangle$ whereas $|10\rangle$ and $|11\rangle$ become $|11\rangle$ and $|10\rangle$ respectively as the $X$ gate is applied when the control qubit is $|1\rangle$. Similar to the CNOT gate, we have the $C U$ gate, which implements the $U$ (or the $U_{3}$ ) gate when the control qubit is $|1\rangle$. Given the matrix of the $U$ gate in Eq. (3), the matrix representation of $C U$ can be written as

$$
C U=\left[\begin{array}{cccc}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & \cos \left(\frac{\theta}{2}\right) & -e^{i \lambda} \sin \left(\frac{\theta}{2}\right) \\
0 & 0 & e^{i \phi} \sin \left(\frac{\theta}{2}\right) & e^{i(\phi+\lambda)} \cos \left(\frac{\theta}{2}\right)
\end{array}\right]
$$

A variant of the $C U$ gate is the $C R_{Y}(\theta)$ gate, which implements the rotation gate $R_{Y}(\theta)$ on the target qubit when the control qubit is equal to $|1\rangle$. The matrix representation of the $C R_{Y}(\theta)$ can be written as

$$
C R_{Y}(\theta)=\left[\begin{array}{cccc}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & \cos \left(\frac{\theta}{2}\right) & -\sin \left(\frac{\theta}{2}\right) \\
0 & 0 & \sin \left(\frac{\theta}{2}\right) & \cos \left(\frac{\theta}{2}\right)
\end{array}\right]
$$

# 2.2.3. Three-qubit gates 

We will discuss two three-qubit gates that are later used in the proposed methodology: CCNOT (or $C C X$ or Toffoli) and $C C R_{Y}(\theta)$. Out of the three qubits on which the CCNOT and $C C R_{Y}(\theta)$ are implemented, two qubits act as control qubits and the other is the target qubit. In the case of CCNOT gate, when both control qubits are $|1\rangle$, we implement the $X$ gate on the target qubit. In the case of the $C C R_{Y}(\theta)$ gate, we implement the $R_{Y}(\theta)$ gate when the two control qubits are in the $|1\rangle$ state. The three-qubits are not elementary gates but can be decomposed into a combination of single-qubit and CNOT

gates. For example, the CCNOT can be represented using a combination of nine single qubit gates and six CNOT gates (Shende \& Markov, 2008). Similar to $C C X$ and $C C R_{Y}(\theta)$, we can define an $C^{n} X$ and $C^{n} R_{Y}(\theta)$ gates with $n$ control qubits and one target qubits (Liu et al., 2008). Figure 2 provides the representation of various gates discussed above in a quantum circuit. A quantum circuit represents a graphical representation of a sequence of gates that are implemented on various qubits to obtain a desired computation. Measurement gate in Figure 2 performs the measurement operation on a qubit.
![img-1.jpeg](img-1.jpeg)

Figure 2: Representation of commonly used one, two, and three qubit gates

According to Nielsen \& Chuang (2002), the $C U$ can be decomposed into a combination of single-qubit and CNOT gates as given in Figure 3; this decomposition can mathematically be represented as

$$
C U=(I \otimes A) C X(I \otimes B) C X(I \otimes C)
$$

where $A=R_{Z}(\phi) R_{Y}(\theta / 2), B=R_{Y}(-\theta / 2) R_{Z}(-(\lambda+\phi) / 2), C=R_{Z}((\lambda-\phi) / 2)$, and $I$ represents the identity matrix. $I \otimes A$ represents the tensor product of
![img-2.jpeg](img-2.jpeg)

Figure 3: Decomposition of a CU gate into a combination of single qubit and CNOT gates

two matrices, $I$ and $A$, where $I$ and $A$ are single-qubit gates implemented on the first and second qubits respectively. $I \otimes A$ is the simplified representation of the two gates acting on the two qubits.

# 2.3. Bayesian Networks 

As mentioned in Section 1, Bayesian networks (BNs) are probabilistic graphical models that represent a probabilistic framework to model stochastic/uncertain systems. In a probabilistic framework, a stochastic system can be represented as a joint probability distribution defined over the set of random variables. A BN consists of nodes and edges, where nodes represent the random variables, and edges represent the dependence between nodes, which is quantified using conditional probability tables (CPT, for discrete variables) and conditional probability distributions (CPD, for continuous variables). In this paper, we consider the design of quantum circuits to represent discrete Bayesian networks (Dash \& Cooper, 2004).

Let us consider a Bayesian network with $s$ nodes, where $\mathbb{V}=\left\{V_{1}, V_{2}, \ldots, V_{s}\right\}$ represents the set of all nodes or random variables. An edge from node $V_{i}$ to node $V_{j}$ represents the dependence between the variables $V_{i}$ and $V_{j}$, and that the values of $V_{j}$ are dependent on the values of $V_{i}$. Here, $V_{i}$ is called the parent node and node $V_{j}$ is referred to as the child node. The nodes without any parent nodes are typically referred to as root nodes. Using the graphical representation of a Bayesian network, the joint probability over the nodes (random variables) can be decomposed into a product of marginal and conditional probabilities as (Koller \& Friedman, 2009)

$$
P\left(V_{1}, V_{2}, \ldots, V_{s}\right)=\prod_{i=1}^{s} P\left(V_{i} \mid \Pi_{V_{i}}\right)
$$

where $\Pi_{V_{i}}$ denotes the set of parents nodes associated with $V_{i}$. For root nodes, the $P\left(V_{i} \mid \Pi_{V_{i}}\right)$ becomes equal to the marginal distribution, $P\left(V_{i}\right)$.

Consider a simple Bayesian network with 3 nodes as shown in Figure 4 where A, B and C are discrete random variables with two states True (or " 1 ") and False

![img-3.jpeg](img-3.jpeg)

Figure 4: An illustrative 3-node Bayesian network with binary variables
(or " 0 "). In this $\mathrm{BN}, A$ and $B$ are root nodes whereas $C$ is a child node with $A$ and $B$ as parent nodes. We have the marginal distributions for root nodes (shown in Figure 4 and a CPT for the child node, which represents a probability distribution of the child node conditioned on the values taken by the parent nodes. Given a CPT, we can calculate its marginal distribution by integrating over the distributions of the parent nodes, i.e., $P(C)=\sum_{A, B} P(C \mid A, B) \times$ $P(A, B)$. Due to the independence between nodes A and B (from Figure 4), the joint probabilities of A and B can be written as the product of individual probabilities, i.e., $P(A, B)=P(A) \times P(B)$, and therefore, $P(C)=P(C \mid A, B) \times$ $P(A) \times P(B)$ (Koller \& Friedman, 2009).

We use the marginal probabilities of various nodes in a Bayesian network as a measure to check the accuracy of the proposed quantum circuit representation approach in Section 3. After we design the quantum circuit, we estimate the marginal probabilities by simulating the quantum circuits, and compare them against the values from classical Bayesian network implementations. After providing a brief background to quantum computing and Bayesian networks, we will now discuss the representation of a Bayesian network through a quantum circuit.

# 3. Quantum circuit of a Bayesian network 

We use the following principles for the design of a quantum circuit to represent a Bayesian network.

(i) Map each node in a Bayesian network to one or more qubits (depending on the number of discrete states of the node)
(ii) Map the marginal/conditional probabilities of each node to the probability amplitudes (or probabilities) associated with various states of the qubit(s).
(iii) Realize the required probability amplitudes of quantum states using (controlled) rotation gates.

Let us discuss how these ideas can be used to design a quantum circuit for the 3-node Bayesian network in Figure 4. All the nodes in Figure 4 have two states ( 0 and 1 ), and since a qubit can represent two states $(|0\rangle$ and $|1\rangle)$, we can map each node to a different qubit. Also, let us map state 0 of each node to $|0\rangle$ and state 1 to $|1\rangle$. Let the three nodes $\mathrm{A}, \mathrm{B}$, and C be mapped to three qubits $q_{0}, q_{1}$, and $q_{2}$ respectively. Let the initial state of the three qubits be $|0\rangle$. In the cases of $q_{0}$ and $q_{1}$, we will need to apply rotation gates $\left(R_{Y}\right)$ with angles $\left(\theta_{A}\right.$ and $\theta_{B}$ ) that result in superposed quantum states whose probabilities correspond the probabilities of nodes A and B respectively. The calculation of those angles are later discussed in Section 3.1. In the case of qubit $q_{2}$ (that corresponds to C), we will have a different rotation angle conditioned on the states of $q_{0}$ and $q_{1}$ since we have a different set of probabilities for node C conditioned on the values of parent nodes (A, B). Since there are four combinations of parent node values, we will have four rotation angles, one for each parent node combination. These conditional rotations are implemented using controlled rotation gates, whose angles depend on the conditional probabilities of C ; these rotations are represented as $\theta_{C, i j}$, where $i, j=0,1$ and represent the states of $q_{0}$ and $q_{1}$ respectively.

Figure 5 provides a conceptual quantum circuit for the 3-node Bayesian network. First, we implement the single qubit rotations to obtain the probabilities associated with A and B. Depending on the values of A and B, we implement controlled rotations to realize the conditional probabilities associated with C. In a controlled rotation, since the rotations are applied only when the control

![img-4.jpeg](img-4.jpeg)

Figure 5: Illustrative quantum circuit with three qubits for the 3-node Bayesian network in Figure 4
qubit is $|1\rangle$, we use the $X$ gate to flip the $|0\rangle$ to $|1\rangle$ state to obtain the conditional probabilities when the parent node value(s) are 0 . As there are two parent nodes, we implement a $C C R_{Y}$ gate to realize the conditional probabilities of C for every combination of the parent nodes. If there are $n$ parent nodes, then we would implement a $C^{n} R_{Y}$ gate. The overall quantum circuit can be obtained by composing all the single-qubit and controlled rotations in a sequential manner (as shown in Figure 5). In this paper, we refer to this approach as the C-QBN approach, which stands for Compositional approach for Quantum Bayesian networks.

We discuss below the computation of rotation angles to realize nodal probabilities in Section 3.1, representation of two-state child nodes with one or more parent nodes in Section 3.2, and representation of nodes with more than two states in Section 3.3.

# 3.1. Rotation angle computation 

As mentioned above, we can represent a two-state root node using a single qubit. By applying an $R_{Y}$ gate with an appropriate angle, the probabilities of the root node can be mapped to the probabilities (and thus probability amplitudes) of the basis states, $|0\rangle$ and $|1\rangle$. Let $\theta_{V_{i}}$ represent the rotation angle associated with a two-state root node, $V_{i}$. Given the initial state of a qubit as $|0\rangle$, the application of $R_{Y}(\theta)$ will transform $|0\rangle$ to $\cos \left(\frac{\theta}{2}\right)|0\rangle+\sin \left(\frac{\theta}{2}\right)|1\rangle$. Therefore, the probabilities associated with the $|0\rangle$ and $|1\rangle$ states are equal to $\cos ^{2}\left(\frac{\theta}{2}\right)$ and $\sin ^{2}\left(\frac{\theta}{2}\right)$ respectively. If $P\left(V_{i}=0\right)$ and $P\left(V_{i}=1\right)$ represent the

probabilities of states 0 and 1 of $V_{i}$, then the rotation angle can be computed as

$$
\theta_{V_{i}}=2 \times \tan ^{-1} \sqrt{\frac{P(|1\rangle)}{P(|0\rangle)}}=2 \times \tan ^{-1} \sqrt{\frac{P\left(V_{i}=1\right)}{P\left(V_{i}=0\right)}}
$$

In Eq. (13), $P(|0\rangle)$ and $P(|1\rangle)$ represent the probabilities of a qubit to be in $|0\rangle$ and $|1\rangle$ respectively. Since we map the nodal probabilities to the probabilities of quantum states, $P(|0\rangle)$ and $P(|1\rangle)$ are replaced with $P\left(V_{i}=0\right)$ and $P\left(V_{i}=1\right)$ respectively. Therefore, two-state root nodes can be represented using an $R_{Y}$ gate with a rotation angle of $2 \times \tan ^{-1} \sqrt{\frac{P\left(V_{i}=1\right)}{P\left(V_{i}=0\right)}}$. In Figure 4 , the rotation angle to find the probabilities of A and B can be calculated as $\theta_{A}=2 \times \tan ^{-1} \sqrt{\frac{0.8}{0.2}}=2.214$ and $\theta_{B}=2 \times \tan ^{-1} \sqrt{\frac{0.7}{0.3}}=1.982$.

Eq. (13) can also be used to compute the rotation angles associated with conditional probabilities of two-state child nodes. Let $V_{i}$ and $\Pi_{V_{i}}$ represent a child node and set of its parent nodes respectively. For each combination of parent node values, $\Pi_{V_{i}}=\Pi_{V_{i}}^{*}$, we have probabilities for $V_{i}=0$ and $V_{i}=1$ denoted as $P\left(V_{i}=0 \mid \Pi_{V_{i}}=\Pi_{V_{i}}^{*}\right)$ and $P\left(V_{i}=1 \mid \Pi_{V_{i}}=\Pi_{V_{i}}^{*}\right)$ respectively. The rotation angle associated with $V_{i}$ when $\Pi_{V_{i}}=\Pi_{V_{i}}^{*}$, which is denoted by $\theta_{V_{i}, \Pi_{V_{i}}^{*}}$ can be calculated as

$$
\theta_{V_{i}, \Pi_{V_{i}}^{*}}=2 \times \tan ^{-1} \sqrt{\frac{P\left(V_{i}=1 \mid \Pi_{V_{i}}=\Pi_{V_{i}}^{*}\right)}{P\left(V_{i}=0 \mid \Pi_{V_{i}}=\Pi_{V_{i}}^{*}\right)}}
$$

The rotation angles associated with node C (qubit $q_{2}$ in Figure 5) can be calculated using Eq. (14) as $\theta_{C, 00}=2 \times \tan ^{-1} \sqrt{\frac{0.85}{0.15}}=2.346, \theta_{C, 01}=$ $2 \times \tan ^{-1} \sqrt{\frac{0.7}{0.3}}=1.982, \theta_{C, 10}=2 \times \tan ^{-1} \sqrt{\frac{0.6}{0.4}}=1.772$, and $\theta_{C, 11}=$ $2 \times \tan ^{-1} \sqrt{\frac{0.9}{0.1}}=2.498$. The conditional probabilities associated with child nodes are realized through controlled rotations. As controlled rotation gates are not elementary gates, they need to be decomposed into single-qubit and two-qubit elementary gates; the decomposition is discussed below in Section 3.2 .

# 3.2. Representing two-state child nodes with two-state parent nodes 

First, we consider the representation of child nodes with one parent node, and then we consider the case with multiple parent nodes. A two-state child node with one parent node can be represented using two $C R_{Y}$ gates (assuming the parent node has two states) with rotation angles computed using Eq. (14) conditioned on the parent node value. We consider parent nodes with more than two states in Section 3.3. The $C R_{Y}$ gate is a special case of a $C U$ gate discussed in Section 2.2, where $U=R_{Y}$. In Section 2.2, we discussed the decomposition of a $C U$ gate in terms of elementary single-qubit and CNOT gates shown in Figure 3 and given in Eq. (11). Since $R_{Y}(\theta)=U_{3}\left(\frac{\theta}{2}, 0,0\right)$, the single qubit gates A, B, and C in Figure 3 can be calculated as $A=R_{Z}(0) R_{Y}\left(\frac{\theta}{2}\right)=R_{Y}\left(\frac{\theta}{2}\right), B=$ $R_{Y}\left(-\frac{\theta}{2}\right) R_{Z}\left(-\frac{(0+0)}{2}\right)=R_{Y}\left(-\frac{\theta}{2}\right)$, and $C=R_{Z}\left(\frac{(0-0)}{2}\right)=I$. Figure 6 illustrates the decomposition of the $C R_{Y}$ gate into single-qubit and CNOT gates. After considering child nodes with one parent node, we now consider child nodes with more than one parent nodes.
![img-5.jpeg](img-5.jpeg)

Figure 6: Decomposition of a $C R_{Y}$ gate into single-qubit $R_{y}$ and CNOT gates

Let $n$ represent the number of parent nodes for a child node, $V_{i}$. The conditional probabilities of $V_{i}$ can be stated using $C^{n} R_{Y}$ gate where the $n$ control qubits are the $n$ qubits corresponding to the $n$ parent nodes and the target qubit represents the child node. For the child node C in Figure 4, $\mathrm{n}=2$, and therefore, we used a $C C R_{Y}$ or $C^{2} R_{Y}$ gate to show the conditional probabilities of C in Figure 5. $C^{n} R_{Y}$ is not an elementary gate and will need to be decomposed into elementary gates. One of the techniques to build the $C^{n} R_{Y}$ is the use of additional "dummy" qubits known as ancilla qubits (Nielsen \& Chuang, 2002). Following (Nielsen \& Chuang, 2002), implementation $C^{n} R_{Y}$ requires $n-1$ ancilla qubits. Using ancilla qubits, the $C^{n} R_{Y}$ gate is decomposed into

a combination of $2(n-1)$ CCNOT gates, and one $C R_{Y}$ gate. For illustration, Figure 7 details the representation of $C^{5} R_{Y}$ gate using four ancilla qubits. The $C R_{Y}$ gate can again be decomposed into a combination of single qubit and CNOT gates as detailed in Figure 6.

In Figure 7, $q_{i}, i=0 \ldots 4$ represent the control qubits (parent nodes), and $q_{5}$ is the target qubit (child node). As there are five control qubits, we use four ancilla qubits $\left(a_{j}, j=0 \ldots 3\right)$. In total, we have 8 CCNOT gates $(2 \times(5-1))$, two CNOTs and two single-qubit rotation gates. In Figure 5, there are two control qubits $(n=2)$ for $q_{2}$ (node C ), we will use one ancilla qubit to make the $C C R_{Y}$ gates. Note that we do not need a different set of ancilla qubits for implementing various controlled rotations (conditional probabilities), and we can the same set of ancilla qubits for all the $C^{n} R_{Y}$ rotations. Moreover, we can use the same set of ancilla qubits to build the $C^{n} R_{Y}$ rotations associated with various child nodes. Consider a Bayesian network with $s$ two-state nodes given by $V_{1}, V_{2}, \ldots V_{s}$ and let $|$.$| denote the cardinality operator. For a node V_{i}$, $\left|\Pi_{V_{i}}\right|$ provides the number of parent nodes of a $V_{i}$. For a root node, $\left|\Pi_{V_{i}}\right|=0$ and for a child node, $\left|\Pi_{V_{i}}\right|>0$. Therefore, the total number of qubits required to represent a Bayesian network with two-state nodes (denoted as $m_{B N, 2}$ ) can be calculated as

$$
m_{B N, 2}=s+\max \left(\left|\Pi_{V_{1}}\right|,\left|\Pi_{V_{2}}\right|, \ldots\left|\Pi_{V_{s}}\right|\right)-1
$$

where $s$ qubits are used to represent $s$ nodes in the Bayesian network, and an additional $\max \left(\left|\Pi_{V_{1}}\right|,\left|\Pi_{V_{2}}\right|, \ldots\left|\Pi_{V_{s}}\right|\right)-1$ ancilla qubits are used to represent the multi-qubit conditional rotations.

# 3.3. Representing discrete variables with more than two states 

When a node has more than two states, then we need to use more than one qubit to represent it, as one qubit can represent only two states. Consider a random variable $V_{i}$ with $n_{i}$ states, denoted as $V_{i, j}, j=0,1, \ldots n_{i}-1$, and $P\left(V_{i, j}\right)$ represents the probability of state $V_{i, j}$; therefore, $\sum_{j=0}^{n_{i}-1} P\left(V_{i, j}\right)=1$.

![img-6.jpeg](img-6.jpeg)

Figure 7: Representation of $C^{5} R_{Y}$ gate using four ancilla qubits, single qubit $R_{Y}$, CNOT and CCNOT gates

Let $m_{i}$ represent the number of qubits to represent $V_{i}$. The number of states that are represented by $m_{i}$ qubits is $2^{m_{i}}$, which needs to be greater than or equal to $n_{i}$. Thus, value of $m_{i}$ can be calculated as the smallest integer that is greater than or equal to $\log _{2} n_{i}$, which can be represented using the ceiling function as $m_{i}=\left\lceil\log _{2} n_{i}\right\rceil$, where $\lceil.$ $\rceil$ is the ceiling function. Let $\left|q_{j}\right\rangle j=l \ldots l+m_{i}-1$ represent $m_{i}$ qubits in the quantum circuit used to represent $V_{i}$. In addition to qubits representing node $V_{i}$, there could be other qubits in the quantum circuit, which are used to represent other nodes and/or ancilla qubits. Here, $l$ is used to represent the indices of the qubits used to represent node $V_{i}$. The superposition state, $\left|q_{l} q_{l+1} \ldots q_{l+m_{i}-1}\right\rangle$ can be written in terms of the basis states as

$$
\left|q_{l} q_{l+1} \ldots q_{l+m_{i}-1}\right\rangle=\sum_{j=0}^{2^{m_{i}}-1} \alpha_{t}\left|q_{l} q_{l+1} \ldots q_{l+m_{i}-1}\right\rangle_{j}
$$

In Eq. (16), $\left|q_{l} q_{l+1} \ldots q_{l+k-1}\right\rangle_{j}$ represents a basis state $(|00 \ldots 0\rangle$ for instance) and $\alpha_{j}$ represents its probability amplitude. Let us map the $n_{i}$ states of the variable to $n_{i}$ basis states represented by these $m_{i}$ qubits. Hence, state $V_{i, j}$ can be mapped to the quantum state $\left|q_{l} q_{l+1} \ldots q_{l+m_{i}-1}\right\rangle_{j}$. The probability amplitudes of these $n_{i}$ quantum states can be calculated using the available state probabilities and the probability amplitudes of the remaining quantum states are set to zero. Therefore, $\alpha_{j}=\sqrt{P\left(V_{i, j}\right)}$ when $j<n_{i}$ and $\alpha_{j}=0$ when

![img-7.jpeg](img-7.jpeg)

Figure 8: Decomposing a $m_{i}$ qubit rotation into single qubit and Controlled $m_{i}-1$ qubit rotations
$n_{i} \leq j<2^{m_{i}}$.
Our goal is to identify the gate $U$ that acts on $m_{i}$ qubits and produces the desired state probabilities, i.e., $U|0\rangle^{\otimes m_{i}}=\left|q_{l} q_{l+1} \ldots q_{l+m_{i}-1}\right\rangle$ which is equlal to $\sum_{j=0}^{n_{i}-1} \sqrt{P\left(V_{i, j}\right)}\left|q_{l} q_{l+1} \ldots q_{l+m_{i}-1}\right\rangle_{j}$. Since $U$ is a multi-qubit gate, it needs to be decomposed into a set of elementary gates discussed in Section 2. Our approach is to decompose the probability distribution defined over $m_{i}$ qubits into a combinations of marginal and conditional distributions that can be implemented using single-qubit and controlled-rotations. First, we rotate the first qubit $\left(q_{l}\right)$ to obtain its associated probability values corresponding to its $|0\rangle$ and $|1\rangle$ states respectively using a single-qubit $R_{Y}$ rotation, and we implement a different multi-qubit rotation on the remaining $k-1$ when $q_{l}=|0\rangle$ and $q_{l}=|1\rangle$.

Figure 8 details the decomposition of a $m_{i}$ qubit rotation into a combination of single-qubit and controlled $m_{i}-1$ qubit rotations, where $U_{0,1 \ldots m_{i}-1}$ is the $m_{i}$ qubit rotation, and $U_{1 \ldots m_{i}-1, q_{l}=|1\rangle}$ and $U_{1 \ldots m_{i}-1, q_{1}=|0\rangle}$ are the rotations implemented on $m_{i}-1$ qubits $\left(q_{l+1}, q_{l+2} \ldots q_{l+m_{i}-1}\right)$ when $q_{l}=|1\rangle$ and $q_{l}=|0\rangle$ respectively. $R_{Y}\left(\theta_{l}\right)$ represents the rotation to obtain the probabilities associated with qubit $q_{l}$, and can be calculated using Eq. (13). The probabilities of $|0\rangle$ and $|1\rangle$ states of $q_{l}$ can be calculated using an indicator function, $\mathbb{I}_{q_{l}}$, defined as

Using Eq. (17), the probability that $q_{l}=|1\rangle$ can be calculated as $P\left(q_{l}=\right.$ $|1\rangle)=\sum_{j=0}^{2^{m_{i}}-1} \alpha_{j}^{2} \mathbb{1}_{q_{l}}\left(\left|q_{l} q_{l+1} \ldots q_{l+m_{i}-1}\right\rangle_{j}\right)$, and $P\left(q_{l}=|0\rangle\right)=1-P\left(q_{l}=|1\rangle\right)$. The rotation angle, $\theta_{l}$ in Figure 8 can be calculated using Eq. (13) as

$$
\begin{aligned}
\theta_{l} & =2 \times \tan ^{-1} \sqrt{\frac{P\left(q_{l}=|1\rangle\right)}{P\left(q_{l}=|0\rangle\right)}} \\
& =2 \times \tan ^{-1} \sqrt{\frac{\sum_{j=0}^{2^{m_{i}}-1} \alpha_{j}^{2} \mathbb{1}_{q_{l}}\left(\left|q_{l} q_{l+1} \ldots q_{l+m_{i}-1}\right\rangle_{i}\right)}{1-\sum_{j=0}^{2^{m_{i}}-1} \alpha_{j}^{2} \mathbb{1}_{q_{l}}\left(\left|q_{l} q_{l+1} \ldots q_{l+m_{i}-1}\right\rangle_{j}\right)}}
\end{aligned}
$$

The above procedure for decomposing $m_{i}$ qubit rotation into a single qubit and controlled $m_{i}$-1 qubit rotations can again be used to decompose the controlled $m_{i}$-1 qubit rotation resulting in controlled single-qubit and controlledcontrolled $m_{i}$-2 qubit rotations. We will illustrate the decomposition of $C U_{1 \ldots m_{i}-1, q_{l}=|1\rangle}$ in Figure 9.
![img-8.jpeg](img-8.jpeg)

Figure 9: Decomposing a controlled $m_{i}$-1 qubit rotation into controlled single qubit and controlled-controlled $m_{i}$-2 qubit rotations

First, we implement a $C R_{Y}$ gate on qubit $q_{l+1}$ to obtain the probabilities of $q_{l+1}$ when $q_{l}=|1\rangle$. The probabilities of $q_{l+1}=|0\rangle$ and $q_{l+1}=|1\rangle$ when $q_{l}=|1\rangle$ are calculated using another indicator function defined over $q_{l}$ and $q_{l+1}$ as

$$
\begin{aligned}
& \mathbb{I}_{q_{l}=1, q_{l+1}}\left(\left|q_{l} q_{l+1} \ldots q_{l+m_{i}-1}\right\rangle\right) \\
& = \begin{cases}1 & \text { if }\left|q_{l}\right\rangle=|1\rangle \text { and }\left|q_{l+1}\right\rangle=|1\rangle \\
0 & \text { if }\left|q_{l}\right\rangle=|1\rangle \text { and }\left|q_{l+1}\right\rangle=|0\rangle\end{cases} \\
& \theta_{l+1, q_{l}=|1\rangle}=2 \times \tan ^{-1} \sqrt{\frac{P\left(q_{l+1}=|1\rangle \mid q_{l}=|1\rangle\right)}{P\left(q_{l+1}=|0\rangle \mid q_{l}=|1\rangle\right)}} \\
& =2 \times \tan ^{-1} \sqrt{\frac{P\left(q_{l+1}=|1\rangle, q_{l}=|1\rangle\right)}{P\left(q_{l+1}=|0\rangle, q_{l}=|1\rangle\right)}}=2 \times \\
& \tan ^{-1} \sqrt{\frac{\sum_{j=0}^{2^{m_{i}}-1} \alpha_{j}^{2} \mathbb{I}_{q_{l}=|1\rangle, q_{l+1}}\left(\left|q_{l} q_{l+1} \ldots q_{l+m_{i}-1}\right\rangle_{j}\right)}{1-\sum_{i=0}^{2^{m_{i}}-1} \alpha_{j}^{2} \mathbb{I}_{q_{l}=1, q_{l+1}}\left(\left|q_{l} q_{l+1} \ldots q_{l+m_{i}-1}\right\rangle_{j}\right)}}
\end{aligned}
$$

$C C U_{2 \ldots m_{i}-1, q_{l}=|1\rangle, q_{l+1}=|1\rangle}$ and $C C U_{2 \ldots m_{i}-1, q_{l}=|1\rangle, q_{l+1}=|0\rangle}$ are again decomposed into a set of controlled-controlled single qubit rotations and triply controlled $m_{i}$-3 qubit rotations following the procedure described above. This decomposition is carried out until we reach $m_{i}-1$ controlled qubit rotations implemented on the qubit $q_{l+m_{i}-1}$. In this way, a $m_{i}$-qubit rotation required to realize the probabilities associated with a discrete variable with more than two states is achieved through uncontrolled/controlled/multi-controlled qubit rotations. Multi-controlled qubit rotations can be implemented using ancilla qubits as detailed in Figure 7. When the multi-state variable is a child node, then we will have a different $m_{i}$ qubit rotation for each combination of the parent nodes. Depending on the number of parent nodes, Each controlled/multi-qubit controlled $m_{i}$-qubit rotation can be represented following the above sequential decomposition process.

In Section 3.2, we discussed the implementation of controlled rotations to realize conditional probabilities of a child node when both the parent and child nodes have two states. Here, let us consider the cases when a combination of multi-state variables and two-state variables are parent nodes for a multi-state child node. Consider a variable $V_{i}$ with $n_{i}$ states with $\Pi_{V_{i}}$ as the set of parent nodes. Let $\Pi_{V_{i, j}}$ represent the $j^{t h}$ parent node and $n_{\Pi_{V_{i, j}}}$ represent the number

of discrete states in the $j^{\text {th }}$ parent node. Number of qubits required to represent $\Pi_{V_{i}}$ can be calculated as

$$
m_{q, \Pi_{V_{i}}}=\sum_{i=1}^{\left|\Pi_{V_{i}}\right|}\left\lceil\log _{2} n_{\Pi_{V_{i, j}}}\right\rceil
$$

where $m_{q, \Pi_{V_{i}}}$ is the number of qubits required to represent $\Pi_{V_{i}}$ and $\left|\Pi_{V_{i}}\right|$ represents the cardinality of the set of parent nodes. If $n_{i}$ represents the number of states of child node $V_{i}$, then the highest order of $C^{n} R_{Y}$ gate required to realize the conditional probabilities of $V_{i}$ can be calculated as $n=m_{q, \Pi_{V_{i}}}+\left\lceil\log _{2} n_{i}\right\rceil$. In order to implement this $C^{n} R_{Y}$ gate, we will need $n-1=m_{q, \Pi_{V_{i}}}+\left\lceil\log _{2} n_{i}\right\rceil-1$ ancilla qubits. Therefore, the total number of qubits required to obtain a Bayesian network with a combination of two-state and multi-state variables is given as

$$
m_{B N}=\left(\sum_{i=1}^{m}\left\lceil\log _{2} n_{i}\right\rceil\right)+\max _{i}\left(m_{q, \Pi_{V_{i}}}+\left\lceil\log _{2} n_{i}\right\rceil-1\right)
$$

where $m_{B N}$ denoted the number of qubits required to represent a given BN, $m_{q, \Pi_{V_{i}}}+\left\lceil\log _{2} n_{i}\right\rceil-1$ is the number of ancilla qubits required to realize the conditional probabilities of node $V_{i}$. As mentioned in Section 3.2, the same set of ancilla qubits can be used for various child nodes. Since qubits can represent only discrete states, any continuous variables need to be discretized to be represented using qubits. If a continuous variable is discretized into more than two states, then the above procedure to handle discrete variables with more than two levels can be used. If the discretization involves only two states, a single qubit can be used to represent it.

# 4. Illustration Examples 

For illustration of the proposed methodology, we consider three examples with varying properties from the financial industry: (1) a 4-node Bayesian network for an oil company stock price prediction; (2) a 10-node Bayesian network

used for liquidity risk assessment; and (3) a Naive Bayes classifier with 8 features (a total of 9 nodes) used for bankruptcy prediction.

The goal of the examples is to demonstrate the application of proposed methods to represent generic discrete quantum Bayesian networks on a gatebased quantum computing platform. The proposed approach is generic and can be used to represent any discrete Bayesian network with any number of nodes. Representation of larger Bayesian network will result in quantum circuits with large number of gates but the procedure to construct the quantum circuits remain the same for smaller or larger Bayesian networks.

The first example is a simple 4-node Bayesian network with binary variables; this example was used to demonstrate the fundamental approach for the representation of unconditional and conditional probabilities using single-qubit rotation, controlled rotations, and use of an ancilla qubit to represent conditional probabilities with two parent nodes.

The second example is a slightly larger Bayesian network with ten binary variables, where one of the variables has three parent nodes. This example was used to demonstrate that the proposed approach can be used to demonstrate the scalability of the proposed framework, and also the use of two ancilla qubits to realize higher-order controlled rotations.

The third example is used to demonstrate the representation of Bayesian networks with nodes having more than two states using qubits, which have only two states. The goal of this example is to demonstrate that the proposed framework can be used to represent any generic discrete Bayesian network with nodes having more than two states using qubits.

For each of the three examples, we design quantum circuits using the proposed C-QBN approach. We performed the quantum computing simulations using a Python package called Quantum Information Science kit (Qiskit), which uses Open QASM or Open Quantum Assembly Language developed by IBM, and is used in all the IBM quantum hardware (IBM, 2016). The histograms and box plots are built using the matplotlib library (Hunter, 2007).

We demonstrate the proposed methods on a simulated platform instead of

using real quantum computers as hardware implementation of circuits of large depths (large number of gates) are affected by noise, which leads to incorrect results (Mandviwalla et al., 2018; Martin et al., 2019). Since simulations are not affected by hardware noise, we use them to demonstrate the proposed methods.

The probabilities of various states of the BNs are computed, and these results are compared with the probabilities obtained from simulating the examples on a classical Bayesian network platform such as Netica (Netica, 2019).

Through this paper, we demonstrate the representation of marginal and conditional probabilities of discrete random variables using elementary single-qubit and two-qubit quantum gates. Moreover, we develop a systematic approach to represent nodes with more than two states as previous literature only focused on nodes with two states; this facilitates the representation of any generic discrete Bayesian network.

# 4.1. 4-node BN: Oil Company Stock Price 

This 4-node Bayesian network example to assess an oil company stock price is obtained from (Shenoy \& Shenoy, 2000). The four variables in this network are the interest rate (IR), stock market (SM), oil industry (OI), and oil company stock price (SP). IR has two states - high and low; SM has two states - good and bad; OI has two states - good and bad; and SP has two states - high and low. Here, we represent low/bad with state 0 and high/good with state 1. The dependence between these four variables and associated conditional probability tables are given in Figure 10.

The BN in Figure 10 has two root nodes, i.e. nodes without parent nodes (IR, OI), one node with only one parent node (SM), and one node with two parent nodes (SP). Since SP has two parent nodes, we use one ancilla qubit to represent its conditional probability values as discussed in Section 3.2. This results in a five-qubit system (four qubits to represent four variables in Figure 10 and an ancilla qubit). We discuss below the construction of quantum circuits corresponding to this BN using the C-QBN approach described in Section 3.






Figure 10: A 4-node Bayesian network for an oil company stock price prediction (Shenoy \& Shenoy, 2000)

Quantum circuit: Figure 11 provides the quantum circuit corresponding to the BN in Figure 10 constructed using the C-QBN approach. The five qubits are denoted as $q_{i}, i=0 \ldots 4$ and the measurement bit is denoted as $c$.

The variables - IR, OI, SM, and SP are denoted using the qubits $q_{4}, q_{3}, q_{2}$ and $q_{0}$ respectively, and the ancilla qubit is $q_{1}$. We chose $q_{1}$ as the ancilla qubit for the purpose of illustration. In reality, any qubit can be chosen as an ancilla qubit in Qiskit. We used this mapping as the representation of an n+1-qubit state is given as $\left|q_{n} q_{n-1} \ldots q_{0}\right\rangle$, i.e., the state of the $n+1^{\text {th }}$ qubit $\left(q_{n}\right)$ is written first while the first qubit $\left(q_{0}\right)$ is written at the end. By following this mapping, the parent nodes appear ahead of their associated child nodes.

After mapping the variables to various qubits, we now identify the appropriate gates to be implemented on those qubits to obtain the required marginal or conditional probability values. Let us begin with the root nodes (IR and OI). The rotation angles required to represent those root nodes were calculated using Eq. (13) as $\theta_{I R}=2 \times \tan ^{-1}\left(\sqrt{\frac{0.25}{0.75}}\right)=\frac{\pi}{3}$ and $\theta_{O I}=2 \times \tan ^{-1}\left(\sqrt{\frac{0.4}{0.6}}\right)=$ 1.37. For realizing child nodes, we compute the associated rotation angles for various combinations of the parent node(s).

![img-9.jpeg](img-9.jpeg)

Figure 11: Quantum circuit of the 4-node oil company stock price BN. Variables IR, OI, SM and SP are mapped to $q_{4}, q_{3}, q_{2}$, and $q_{0}$ respectively, $q_{1}$ is the ancilla qubit, and $c$ represents the classical bits used to store of values of qubits after measurement

To represent SM node, we compute its rotation angles when $\mathrm{IR}=0$ and $\mathrm{IR}=1$ as $\theta_{S M, 0}=2 \times \tan ^{-1}\left(\sqrt{\frac{0.7}{0.3}}\right)=1.982$ and $\theta_{S M, 1}=2 \times \tan ^{-1}\left(\sqrt{\frac{0.2}{0.8}}\right)=0.928$ respectively. Here, $\theta_{S M, j}$ corresponds to the rotation angle of SM for a given value $j$ of its parent node, IR. As discussed in Section 3.2, the controlled rotations are decomposed into a combination of uncontrolled rotations and CNOT gates. For example, the conditional probability values of SM when $\mathrm{IR}=1$ are realized by implementing a controlled-rotation gate $C R_{Y}\left(\theta_{S M, 1}\right)$. Following Section 3.2, this gate is implemented as $\left(I \otimes R_{Y}\left(\frac{\theta_{S M, 1}}{2}\right)\right) C X(I \otimes$ $\left.R_{Y}\left(\frac{-\theta_{S M, 1}}{2}\right)\right) C X$. The controlled-rotation when $\mathrm{IR}=0$ is implemented by first flipping the states of the $q_{4}$ (IR) qubit using an $X$ gate, and then applying the $C R_{Y}\left(\theta_{S M, 0}\right)$ gate. Thus, the conditional probability values of SM are realized for various values of its parent node (IR). We now consider the SP node.

Since SP has two parent nodes, we have four rotation angles $\left(\theta_{S P, 00}, \theta_{S P, 01}\right.$, $\left.\theta_{S P, 10}, \theta_{S P, 11}\right)$ for various values of the two parent nodes; these values were calculated using Eq. (13) as $0.644,1.772, \frac{\pi}{2}, 2.22$ respectively. Here, $\theta_{S P, j k}$ corresponds to the rotation angle of SP for given values $j$ and $k$ of parent nodes OI and SM respectively. Following Section 3.3, the controlled-controlled rotations are implemented using an ancilla qubit. At the end of the circuit, we add the measurement gates and stores the measured qubit values in a classical bit register ( $c$ in Figure 11). We consider only four measurements across the qubits associated with various nodes in the BN, and do not consider a measurement gate for the ancilla qubit as it does not represent any variable in the BN.

Circuit simulation: The BN is simulated using the circuit constructed with the C-QBN approach, and the accuracy of the results is compared with those obtained using Netica, which is a classical Bayesian network software. After a simulation is made, the system is measured, which returns a single quantum state (such as $|1010\rangle$ ). A total of 8192 shots were carried out in each simulation, and the measured states after each shot are used to estimate the the probabilities of all the states. We used 8192 shots as that was the maximum number of shots possible on the real IBM quantum computers such as the 5 -

qubit IBM QX5 (Mandviwalla et al., 2018).
When a measurement is made, one of the 16 states is observed as we were measuring only four qubits corresponding to four nodes in the BN. The probability associated with each state $\left(P\left(\left|q_{4} q_{3} q_{2} q_{0}\right\rangle\right)\right)$ can be computed using the Monte Carlo approach as

$$
P\left(\left|q_{4} q_{3} q_{2} q_{0}\right\rangle\right)=\frac{n_{\left|q_{4} q_{3} q_{2} q_{0}\right\rangle}}{N}
$$

where $P\left(\left|q_{4} q_{3} q_{2} q_{0}\right\rangle\right)$ is the probability of state $\left|q_{4} q_{3} q_{2} q_{0}\right\rangle ; n_{\left|q_{4} q_{3} q_{2} q_{0}\right\rangle}$ and $N$ represent the number of times $\left|q_{4} q_{3} q_{2} q_{0}\right\rangle$ is observed and the total number of shots (8192) respectively. The marginal probabilities of each of the nodes can be estimated using Equation by marginalizing over the state probabilities calculated using Eq. (24).

$$
P\left(\left|q_{i}\right\rangle\right)=\sum_{q_{j}, j=4,3,2,0, j \neq i} P\left(\left|q_{4} q_{3} q_{2} q_{0}\right\rangle\right)
$$

Comparison of simulation results: As discussed above, we ran 8192 shots of the quantum circuit to estimate the marginal probabilities. Since the marginal probabilities are estimated from data, there could be variation across multiple runs of the quantum circuit. In order to quantify the variation across runs, we ran the circuit $r$ times and obtained the marginal probability values from each run. Given the simulation results from $r$ runs, we compute the $(1-\alpha)$ confidence intervals of the estimated marginal probabilities and checked if the marginal probabilities from Netica fall within the estimated intervals.

Let $p_{i}^{m}, i=1 \ldots r, m=I R, O I, S M, S P$ represent the marginal probability value of the $m^{t h}$ variable in the $i^{t h}$ run, then the sample mean and standard deviation can be calculated as $\bar{p}^{m}=\frac{\sum_{i=1}^{r} p_{i}^{m}}{r}$ and $s^{m}=\sqrt{\frac{\sum_{i=1}^{r}\left(p_{i}^{m}-\bar{p}^{m}\right)^{2}}{r-1}}$ respectively. Given the sample mean and standard deviation, the $(1-\alpha)$ confidence interval were calculated as $\bar{p}^{m} \pm t_{\frac{\alpha}{2}} \frac{s^{m}}{\sqrt{r}}$. Here, $t_{\frac{\alpha}{2}}$ is the t-statistic corresponding to the $(1-\alpha)$ confidence interval. In this study, we chose $r=10$ and $\alpha=0.05$. The sample mean and standard deviation, and the $95 \%$ CIs of the marginal probabilities using both the methods are provided in Table 1,

Table 1: Comparison of marginal probabilities in the 4-node Bayesian network with Netica (classical computation) and the proposed approach (C-QBN)


along with the marginal probabilities obtained using Netica. The variation in the probability values obtained using the C-QBN approach, can be attributed to the variability in the measurement process.
![img-10.jpeg](img-10.jpeg)

Figure 12: Simulation results of the oil company stock price QBN using Qiskit with 8192 shots (quantum states on the horizontal axis and joint probabilities on the vertical axis)

From Table 1, it can be observed that the marginal probabilities from Netica fall within their estimated confidence intervals obtained from the quantum circuit simulations. Since each node has two states, we provided the probabilities of only one of the states as the probabilities of the other states can be computed from the given states. For example, $P(I R=1)=1-P(I R=0)$. Thus, the

C-QBN approach was used to represent the 4-node Bayesian network.

# 4.2. 10-node BN: Liquidity Risk Assessment 

![img-11.jpeg](img-11.jpeg)

Figure 13: A 10-node Bayesian network for liquidity risk assessment(Tavana et al., 2018)

Here, we consider designing a quantum circuit to represent a 10-node Bayesian network obtained from (Tavana et al., 2018) used for liquidity risk assessment in banking. The 10 variables in the Bayesian network are described in Table 2, and the dependence between various variables are shown in Figure 13, and the conditional probability tables are given in Figure 14.

In Table 2, $\mathbf{B}$ refers to the bank under consideration, and $\mathbf{O}$ refers to other banks. This BN has one root node $\left(X_{6}\right)$, six nodes with one parent node $\left(X_{7}, X_{8}, X_{9}, X_{1}, X_{2}, X_{3}\right)$, two nodes with two parent nodes $\left(X_{4}, X_{5}\right)$, and one node with three parent nodes $\left(X_{10}\right)$. Since the maximum number of parent nodes is three, we need two ancilla qubits to represent the conditional probability values in addition to the ten qubits used to represent the ten nodes in the BN totaling to 12 qubits. The representation of the root node $\left(X_{6}\right)$, child nodes with either one or two parent nodes follows the same procedure as detailed in

Section 4.1. Therefore, we discuss below the representation of $X_{10}$, which is the child node with three parent nodes $\left(X_{1}, X_{2}, X_{4}\right)$ using the C-QBN approach.

Table 2: Variables in the 10-node liquidity risk assessment Bayesian network (Tavana et al., 2018)


Quantum circuit: Figure 21 provides the quantum circuit of the 10node BN constructed the C-QBN approach. The 12 qubits are denoted as $q_{i}, i=0 \ldots 11$ and the measurements of various qubits are stored in classical bits denoted as $c$. In this circuit $X_{1}$ is mapped to qubit $q_{7}, X_{2}$ represented by $q_{3}, X_{3}$ to $q_{4}, X_{4}$ to $q_{6}, X_{5}$ to $q_{5}, X_{6}$ to $q_{11}, X_{7}$ to $q_{10}, X_{8}$ to $q_{9}, X_{9}$ to $q_{8}$. Finally, $X_{10}$ is represented using $q_{0}$, and $q_{1}, q_{2}$ are the ancilla qubits. Since












Figure 14: Marginal and conditional probabilities of various nodes in the liquidity risk assessment Bayesian network (Tavana et al., 2018)
$X_{10}$ are three parent nodes, we need to implement $C^{3} R_{Y}$ gate for each of the $8\left(=2^{3}\right)$ combinations of the parent nodes. Following Section 3.2, the $C^{3} R_{Y}$ gate requires the use of two ancilla qubits, and is build through a combination of one, two, and three-qubit gates $\left(R_{Y}\right.$, CNOT, CCNOT).

For example, the conditional probability values of $X_{5}$ when $X_{8}=1$ and $X_{4}=0$ would be obtained by implementing a controlled-controlled rotation gate $C C R_{Y}$. Since $X_{5}$ has two parent nodes, we have four rotation angles $\left(\theta_{X_{5}, 00}\right.$, $\left.\theta_{X_{5}, 01}, \theta_{X_{5}, 10}, \theta_{X_{5}, 11}\right)$ for various values of the two parent nodes. Following Section 3.3, the controlled-controlled rotations for $X_{5}$ are implemented using one of the two available ancilla qubits ( $q_{2}$ is used here).

Circuit simulation and results: Following the 4-node BN, we ran the quantum circuits obtained using the C-QBN ten times each with 8192 shots. The marginal probabilities of nodes from Netica, along with the sample mean, sample standard deviation and the $95 \%$ confidence intervals of the sample mean are provided in Table 3.

Table 3: Comparison of marginal probabilities in the 10-node Bayesian network with Netica and C-QBN


![img-12.jpeg](img-12.jpeg)

Figure 15: Simulation results of the liquidity risk assessment QBN using Qiskit with 8192 shots (quantum states on the horizontal axis and joint probabilities on the vertical axis)

From the results in Table 3, it can be observed that the true marginal probabilities (obtained from Netica) fall within the confidence intervals obtained using

the C-QBN approach. These results help conclude that the C-QBN approach is able to simulate the 10-node Bayesian network with two and three parent nodes, each with two states.

# 4.3. 9-node Naive Bayes Classifier: Bankruptcy Prediction 

Here, we consider designing a quantum circuit to represent a Naive Bayes classifier used for bankruptcy prediction; this model is obtained from (Sun \& Shenoy, 2007). There are eight features in this classifier that correspond to several financial-accounting, market-based, and other extraneous factors. The financial-accounting factors are Cash/Total Assets (CH), a variable related to the variation in cash and short-term marketable securities (LM), a binary variable to check if the net income was negative in the last two years (IT), and a variable that represents the ratio of the change in net income and the sum of the absolute net income in the last two years ( CHN ). The market-based factors are a variable that represents the natural logarithm of firm's size relative to the CRSP NYSE/AMEX/NASDAQ market capitalization index (M) and a variable that represents the difference of the firm's stock return and the value-weighted CRSP NYSE/AMEX/NASDAQ index return in the previous year (R).
![img-13.jpeg](img-13.jpeg)

Figure 16: A 9-node Naive Bayes classifier for bankruptcy prediction (Sun \& Shenoy, 2007)

The extraneous factors are variables that relate to the Compustat codings (AU) and Industry Failure Rate (IFR). The bankruptcy classification status is denoted with the variable B. Figure 16 shows the Naive Bayes model, and the associated conditional probability tables are provided in Figure 17. The


















Figure 17: Marginal and conditional probabilities of various nodes in the bankruptcy prediction naive Bayes classifier (Sun \& Shenoy, 2007)
variables B, AU and IT have two states $\{0,1\}$ while all the remaining variables have three states $\{0,1,2\}$. We are using this example for the sake of illustration, and the readers are referred to (Sun \& Shenoy, 2007) for more details about the variables and the model. Since each the variables B, AU and IT has two states, it can be represented using a single qubit. Each of the remaining variables has three states; therefore, each node is represented using $\left\lceil\log _{2} 3\right\rceil=2$ qubits. The total number of qubits used to represent the 9-node Naive Bayes classifier is 16 $(3 \times 1+6 \times 2+1)$. The representation of the root node (B), and child nodes with one parent node (AU, IT) follows the procedure described in Section 4.1. Here, we discuss the representation of child nodes with more than two levels (CH, LM, M, R, CHN, IFR) using the C-QBN approach.

Quantum circuit: The 16 qubits are denoted as $q_{i}, i=0 \ldots 15$ and the measurements of various qubits are stored in the classical bit register $c$. The nine variables B, AU, IT, CH, LM, M, R, CHN, and IFR are mapped to $q_{15}, q_{14}, q_{13},\left(q_{12}, q_{11}\right),\left(q_{10}, q_{9}\right),\left(q_{8}, q_{7}\right),\left(q_{6}, q_{5}\right),\left(q_{4}, q_{3}\right)$, and $\left(q_{2}, q_{1}\right)$ respectively. Any qubit can be chosen as the ancilla qubit, and in this example, we chose $q_{0}$ for the sake of illustration. We discuss the representation of CH , and the same

procedure can be applied to other nodes as well. We map the three states of CH $\{0,1,2\}$ to the states $|00\rangle,|01\rangle,|10\rangle$ of qubits $q_{12}$ and $q_{11}$. Figure 22 shows the associated quantum circuit with gates associated with B and CH nodes only. We apply the appropriate $C U$ transformations to realize the conditional probability values for various values of $\mathrm{B}\{0,1\}$. Here, the control qubit is $q_{15}$ and the target is a two-qubit system $\left(q_{12}, q_{11}\right)$.

First, let us consider the case when $q_{15}=|1\rangle$, i.e., $\mathrm{B}=1$. When $q_{15}=|1\rangle$, the transformation $U$ should result in the probability values of $0.19,0.63$ and 0.18 for $\left(q_{12}, q_{11}\right)$ states of $|00\rangle,|01\rangle$ and $|10\rangle$ respectively. The probability of state $|11\rangle$ is fixed at 0 . The multi-qubit rotation $U$ is not an elementary transformation, we will decompose it into a combination of one and two-qubit elementary transformations. The probability of $|0\rangle$ and $|1\rangle$ states of $q_{12}$ can be calculated as $P(|00\rangle)+P(|01\rangle)=0.19+0.63=0.82$ and $P(|10\rangle)+P(|11\rangle)=$ $0.18+0=0.18$ respectively. We realize the marginal probabilities of $q_{12}$ using a single-qubit $R_{Y}$ gate with the rotation angle $\theta_{q_{12}, q_{15}=|1\rangle}=2 \times \tan ^{-1}\left(\sqrt{\frac{0.18}{0.82}}\right)=$ 0.5725 .

After realizing the marginal probabilities of $q_{12}$, we consider the conditional probabilities of $q_{11}$ given $q_{12}$. When $q_{12}=|1\rangle$, the probability of $q_{11}=|0\rangle$ is computed using Eq. (25) as

$$
\begin{aligned}
P\left(q_{11}=|0\rangle \mid q_{12}=|1\rangle\right) & =\frac{P\left(q_{12}=|1\rangle, q_{11}=|0\rangle\right)}{P\left(q_{12}=|1\rangle\right)} \\
& =\frac{0.18}{0.18}=1
\end{aligned}
$$

Therefore, $P\left(q_{11}=|1\rangle \mid q_{12}=|1\rangle\right)=1-P\left(q_{11}=|0\rangle \mid q_{12}=|1\rangle\right)=0$. Thus, the probability values associated with the $|10\rangle$ and $|11\rangle$ states are applied through a $C R_{Y}$ where $q_{12}$ and $q_{11}$ are the control and target qubits respectively, and with a rotation angle, $\theta_{q_{11}, q_{12}=|1\rangle, q_{15}=|1\rangle}=2 \times \tan ^{-1}\left(\sqrt{\frac{1}{0}}\right)=\pi$. Similarly, when $q_{12}=|0\rangle$, the probabilities of $q_{11}=|0\rangle$ and $q_{11}=|1\rangle$ is computed as $P\left(q_{11}=|0\rangle \mid q_{12}=|0\rangle\right)=\frac{P\left(q_{12}=|0\rangle, q_{11}=|0\rangle\right)}{P\left(q_{12}=|0\rangle\right)}=\frac{0.19}{0.82}=0.232$ and $P\left(q_{11}=|1\rangle \mid q_{12}=|0\rangle\right)=1-\frac{P\left(q_{12}=|0\rangle, q_{11}=|0\rangle\right)}{P\left(q_{12}=|0\rangle\right)}=0.768$. Therefore,

the rotation angle to show the conditional probability values when $q_{12}=|0\rangle$ is $\theta_{q_{11}, q_{12}=|0\rangle, q_{15}=|1\rangle}=2 \times \tan ^{-1}\left(\sqrt{\frac{0.768}{0.232}}\right)=2.1365$. In this way, the twoqubit rotation gate $U$ is decomposed into a combination of single and two-qubit $\left(C R_{Y}\right)$ gates. Since $U$ is implemented when $q_{15}=|1\rangle$, the controlled-rotations in $U$ gate decomposition become controlled-controlled rotations with B as an additional control qubit. Following Section 3.2, the controlled-controlled rotations are implemented using an ancilla qubit. Similar decomposition procedure is followed to implement the two-qubit $U$ gate when $q_{15}=|0\rangle$. In this way, the conditional probabilities associated with CH are realized. This procedure is then repeated to show the conditional probability values of three-level nodes LM, M, R, CHN, and IFR. Thus, the quantum circuit of the 9-node naive Bayes classifier is constructed using the C-QBN approach.

Circuit simulation and results: Similar to the previous examples, we ran the circuit 10 times, each with 8192 shots. The mean, standard deviation, and the $95 \%$ CI of the marginal probabilities are given in Table 4, from which it can be observed that the probability values from Netica fall within the $95 \%$ CI obtained from the C-QBN approach. For variables with three states (CH, LM, M, R, CHN, IFR), we provided the probabilities of two states as the probability of the third state can be computed using the probabilities of the given states. For example, $P(M=2)=1-P(M=0)-P(M=1)$. These results help conclude that the proposed circuit construction approach can represent the 9node Naive Bayes classifier. The histogram in Figure 18 shows different quantum state probabilities in the partial circuit using nodes B and CH .

Each state represents a joint probability of the corresponding variables. The first value in each of the states corresponds to B and the other two are used to represent the three states of CH . Since CH has only three states irrespective of the value of $B$, the probability of state $|11\rangle$ is fixed at zero. Therefore, the probabilities associated with $|011\rangle$ and $|111\rangle$ states are equal to zero and do not appear in the histogram.

Table 4: Comparison of marginal probabilities in the 9-node naive Bayes classifier with Netica and C-QBN


![img-14.jpeg](img-14.jpeg)

Figure 18: Simulation results of nodes B and CH in the 9-node naive Bayes classifier using Qiskit with 8192 shots (quantum states on the horizontal axis and joint probabilities on the vertical axis)

We ran each of the three examples to compute the simulation time, and we observed that the simulation time is not constant but changes across each run. The ranges of the simulation times for analyzing the 4 -node, 10 -node and 9 node BNs are [15ms, 23ms], [28ms, 32ms] and [50ms, 66ms] respectively. Here, "ms" stands for milliseconds. Since Netica is a commercial software, we were unable to extract the exact computation time. One of the main advantages of the quantum Bayesian networks is that there have been proven computational benefits in forward and inverse analysis through amplitude amplification and estimation (Low et al., 2014; Woerner \& Egger, 2019).

Noise analysis: In order to understand the effect of hardware noise on the marginal probabilities, we ran the Bayesian network examples after incorporating the hardware noise from real quantum hardware (from IBM) and compared the results when run without incorporating any hardware noise. We considered noise models from seven publicly available quantum hardware: Burlington, Vigo, Ourense, London, Essex, Yorktown and Melbourne (IBM, 2016). All the hardware except for Melbourne have five qubits whereas Melbourne has fifteen qubits. Moreover, in these hardware, there exists limited connectivity between qubits, i.e., every qubit is not connected to every other qubit (IBM, 2016). The connectivity is important when implementing the two-qubit gate (CNOT). CNOT gate can not be applied between qubits that are not connected to each other in the hardware. Therefore, in addition to noise models, we incorporated the connectivity information to simulate the execution on real hardware.

Since the first example requires five qubits (four qubits for the four nodes in the Bayesian network and one ancilla qubit), it can be run on all the hardware whereas the second example which requires eleven qubits (including one ancilla qubit) can only be run on Melbourne as the remaining hardware have only five qubits. The third example requires sixteen qubits and unfortunately as of July 2020, we do not have public access to a hardware which can handle sixteen qubits.

The noise models get updated whenever the quantum hardware are calibrated (IBM, 2016). The noise models that we used for analysis correspond to

the noise models on July 10, 2020.
Table 5 provides the marginal probabilities of the four nodes obtained from Netica, with and without incorporating any hardware noise in Qiskit. Since there exists variation across multiple runs, we provide the mean and standard deviation values for analysis on the simulator. The standard deviation values are available in the parenthesis. The difference between the results obtained from Qiskit and Netica are quantified using the the Root Mean Square Percentage Error (RMSPE), using Eq. 26 .

$$
\epsilon_{T}=100 \% \sqrt{\frac{1}{n} \sum_{i}\left(\frac{p_{i}^{t}-\bar{p}_{i}}{p_{i}^{t}}\right)^{2}}
$$

where $\epsilon_{T}$ is the RMSPE, $p_{i}^{t}$ and $\bar{p}_{i}$ are the true and expectation values (over 10 runs), and $n$ represents the number of nodes in the Bayesian network. The true values are obtained from classical analysis using Netica software.

It can be observed that the simulator results without any hardware noise are close to those of the true values (RMSPE of $0.11 \%$ ). However, the results were noticeably different when the hardware noise models are incorporated with RMSPE ranging from $6.44 \%$ (Vigo) to $10.8 \%$ (Melbourne). The mean and the standard deviation values, box plots showing the variation in marginal probabilities with various hardware noise models and without noise models along with the true values are provided in Figure 19.

Similar to the 4-node example, Table 6 provides the mean and standard deviation values of the the marginal probabilities of various nodes from Netica, with and without incorporating any hardware noise in Qiskit. As metioned above, we provide results with Melbourne noise model as the 10-node Bayesian network cannot be run with other available hardware. It can be observed that adding the noise model produces highly erroneous results with $557.2 \%$ RMSPE when compared to $0.6 \%$ RMSPE without any noise model. Figure 20 provides the box plots of the marginal probabilities from simulator without any hardware noise and with Melbourne noise model along with the true values obtained from Netica. Figure 20 shows the wide variation between the results from Netica and

Table 5: Mean and standard deviation values of marginal probabilities over 10 runs of the 4-node Bayesian network on Qiskit with noise models from different IBM QX hardware, without any noise models, and marginal probabilities from Netica


Table 6: Mean and standard deviation values of marginal probabilities over 10 runs of the 10-node Bayesian network on the simulator with and without including Melbourne noise model, and marginal probabilities from Netica


![img-15.jpeg](img-15.jpeg)

Figure 19: Box plots associated with the marginal probabilities of the 4-node Bayesian network on Qiskit with noise models from different IBM QX hardware, without any noise models, and marginal probabilities from Netica (red lines). Each of the four subplots corresponds to a node in the Bayesian network (IR, OI, SM, SP). Various hardware models are available on the horizontal axis (Simulator represents the case without any noise model) and probabilities on the vertical axis.

![img-16.jpeg](img-16.jpeg)

Figure 20: Box plots associated with marginal probabilities of the 10-node Bayesian network on Qiskit without adding any noise model (left) and with noise model from Melbourne (right) compared with the results from Netica(green points). The variables are on the horizontal axis and their probabilities are on the vertical axis.
those obtained with Melbourne noise model. From this example, we can infer that even though the proposed approach can be used to represent large Bayesian networks, their implementation on real hardware can produce erroneous results due to hardware noise.

# 5. Conclusion 

This paper detailed the design of a quantum circuit to represent a generic discrete Bayesian network with nodes that may have two or more states. The quantum circuit design follows three steps. The first step is to map a Bayesian network node to one or more qubits depending on the number of states. The second step is mapping the marginal or conditional probabilities of nodes to probability amplitudes/probabilities associated with the qubits to be in $|0\rangle$ and $|1\rangle$ states. The third step is to realize the required probability amplitudes using single-qubit and (multi-qubit) controlled rotation gates. We used ancilla qubits for the implementation of multi-qubit rotation gates. When a node is mapped to more than one qubit, the multi-qubit rotations required to realize the required probabilities are decomposed into a combination of single-qubit and multi-qubit

controlled rotations.
The proposed approach was demonstrated with three Bayesian networks: a Bayesian network with four nodes and each with two states used for an oil company stock prediction, a Bayesian network with ten nodes and each with two states used for liquidity risk assessment, and a Naive Bayes classifier with nine nodes (eight features). Of the nine nodes, three nodes had two states and six nodes had three states. The quantum circuits are designed and simulated on Qiskit (McKay et al., 2018), which is a Python-based simulator for quantum computing. We simulated each circuit with 8192 shots, and calculated the marginal probabilities associated with each node. Since the results from quantum circuit are stochastic, we repeated the simulations 10 times, each time with 8192 shots. Using the results from 10 simulations, we estimated the $95 \%$ confidence intervals. To validate the simulation results, we simulated the Bayesian networks using a classical Bayesian network software (Netica) and tested if the Qiskit results match the results from the classical software. We found that the marginal probabilities of all the nodes obtained from the classical implementations were within the $95 \%$ confidence intervals obtained from Qiskit.

All the quantum circuits in this work were designed manually. Future work should consider automating the design of quantum circuit for a given Bayesian network. We used a simulation platform in this work to validate the accuracy of the methods. In future, we will implement the proposed methods on real quantum computers, and study the effect of hardware noise on the circuit implementation.
