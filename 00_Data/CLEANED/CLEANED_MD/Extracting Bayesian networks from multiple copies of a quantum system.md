LETTER $\cdot$ OPEN ACCESS

## Extracting Bayesian networks from multiple copies of a quantum system

To cite this article: Kaonan Micadei et al 2023 EPL 14460002

View the article online for updates and enhancements.

## You may also like

- The entropic approach to causal correlations

Nikolai Miklin, Alastair A Abbott, Cyril
Branciard et al.

- Bayesian network models for error detection in radiotherapy plant: Alan M Kalet, John H Gennari, Eric C Ford et al.
- A Bayesian network approach for modeling local failure in lung cancer Jung Huri Oh, Jeffrey Craft, Rawan Al Lozi et al.

# Extracting Bayesian networks from multiple copies of a quantum system 

Kaonan Micadei ${ }^{1}$, Gabriel T. Landi ${ }^{2,3}$ and Eric Lutz ${ }^{1(\mathrm{a})}$<br>${ }^{1}$ Institute for Theoretical Physics I, University of Stuttgart - D-70550 Stuttgart, Germany<br>${ }^{2}$ Instituto de Física da Universidade de São Paulo - 05314-970 São Paulo, Brazil<br>${ }^{3}$ Department of Physics and Astronomy, University of Rochester - Rochester, NY 14627, USA

received 10 October 2023; accepted in final form 20 December 2023 published online 10 January 2024


#### Abstract

Despite their theoretical importance, dynamic Bayesian networks associated with quantum processes are currently not accessible experimentally. We here describe a general scheme to determine the multi-time path probability of a Bayesian network based on local measurements on independent copies of a composite quantum system combined with postselection. We further show that this protocol corresponds to a nonprojective measurement. It thus allows the investigation of the multi-time properties of a given local observable while fully preserving all its quantum features.


Copyright (c) 2024 The author(s)
Published by the EPLA under the terms of the Creative Commons Attribution 4.0 International License (CC BY). Further distribution of this work must maintain attribution to the author(s) and the published article's title, journal citation, and DOI.

Introduction. - Transition probabilities between eigenstates of an operator play a central role in quantum mechanics. Assuming that a driven system is at time $t_{1}$ in a given eigenstate $\left|j_{1}\right\rangle$, the probability to find the system at a later time $t_{2}$ in eigenstate $\left|j_{2}\right\rangle$ is $P_{j_{1}, j_{2}}=\left|\left\langle j_{2}\right| U\left(t_{2}-t_{1}\right)\left|j_{1}\right\rangle\right|^{2}$, with the time evolution operator $U\left(t_{2}-t_{1}\right)$ [1]. The probability to measure the corresponding eigenvalues $j_{1}$ and $j_{2}$ is then $P_{j_{1}, j_{2}} P_{j_{1}}$, where $P_{j_{1}}$ is the occupation probability of the initial state. Such joint probabilities are commonly determined via projective measurements [1]. Yet, coherent superpositions of eigenstates, that may deeply affect the dynamics, are ubiquitous in quantum theory [2]. Since projective measurements destroy linear combinations, it is crucial to develop nonprojective methods to measure joint probabilities between (multiple) arbitrary states.

In this regard, dynamic Bayesian networks offer a powerful formalism to analyze conditional dependences in a set of time-dependent random quantities. In this approach, relationships between dynamical variables are specified through conditional probabilities evaluated via Bayes' rule [3-6]. They have found widespread application in statistics, engineering and computer science to model time series in probabilistic models. Concrete applications include prediction of future events, inference of hidden

[^0]variables and decision making [3-6]. Hidden Markov models and Kalman filters are special cases of such networks [3-6]. In the past decade, Bayesian networks have been successfully employed to investigate the nonequilibrium thermodynamics of small, composite systems, both in the classical $[7-14]$ and quantum [15-18] regimes. They have, in particular, been used to obtain fluctuation theorems, generalizations of the second law that characterize fluctuations of the entropy production arbitrarily far from equilibrium [19], for multiple interacting systems [7-18]. They have also been used to derive thermodynamic uncertainty relations [13].

An interesting property of dynamic Bayesian networks is that they allow to specify the local dynamics of a composite quantum system conditioned on its global state. The Bayesian network framework thus preserves all the quantum features of the system, especially quantum correlations and quantum coherences [15-18]. As a result, it permits to go beyond the standard two-pointmeasurement (TPM) scheme [20-22], which, owing to its projective nature, destroys off-diagonal density matrix elements. This characteristic has recently been exploited to derive fully quantum fluctuation theorems that not only account for the quantum nonequilibrium dynamics of a driven system, as in the two-projective-measurement approach [23], but also fully capture both quantum correlations and quantum coherence at arbitrary times [15-17].


[^0]:    ${ }^{(a)}$ E-mail: eric.lutz@itp1.uni-stuttgart.de (corresponding author)

However, while a number of methods to implement the two-projective-measurement approach (and its variants) have been both theoretically developed [24-27] and experimentally demonstrated [28-34], to date, no such protocol exists for dynamic Bayesian networks.

In this paper, we introduce a general experimental scheme to extract dynamic Bayesian networks using identical copies of a quantum system. Multiple copies have been used in quantum information theory to perform entanglement detection [35-43] and quantum state estimation [44-49]. They have recently been considered in quantum thermodynamics to reduce back action [50,51]. In the following, we first employ independent copies of a quantum system combined with postselection [52] to reconstruct the path probability of a dynamic Bayesian network. The latter quantity determines the multi-time properties of a given local observable without requiring full state tomography, which is in general extremely costly to realize [53]. We moreover introduce a positive-operatorvalued measure (POVM) [52] such that the path probability directly results from global measurements of correlated copies in a broadcast state [54]. We further show that a no-go theorem for the characterization of work fluctuations in coherent quantum systems discussed in ref. [50] does not apply to such a POVM. A well-defined nonequilibrium quantum work distribution may consequently be obtained for driven systems with initial coherence. We finally illustrate our findings by concretely evaluating the two-point path probabilities for a coherent qubit and for a quantum correlated pair of qubits.

Dynamic Bayesian networks. - We consider an isolated quantum system initially prepared in a generic state with spectral decomposition, $\rho=\sum_{s} P_{s}|s\rangle\langle s|$. The system may be multipartite or single partite, but often, we will think about it as a global, quantum correlated, state of a multipartite system (as, for instance, in ref. [17]). As a consequence, the basis elements $|s\rangle$ can be highly nonlocal. During its unitary evolution, $\rho_{t}=U_{t} \rho U_{t}^{\dagger}$, the populations $P_{s}$ remain constant and the basis elements rotate from $|s\rangle$ to $\left|s_{t}\right\rangle=U_{t}|s\rangle$. Let us now introduce arbitrary basis sets $\left\{\left|x_{0}\right\rangle\right\},\left\{\left|x_{1}\right\rangle\right\}, \ldots,\left\{\left|x_{N}\right\rangle\right\}$ at $(N+1)$ specific points in time, $t=t_{0}, t_{1}, \ldots, t_{N}$ (fig. 1). These bases are not necessarily compatible with each other, nor with the bases $\left\{\left|s_{t}\right\rangle\right\}$. To give an example, in a multipartite system, the basis $|x\rangle$ could refer to a product state of local basis elements for local operators, while $|s\rangle$ would be a global (entangled) basis. Because of this picture, for concreteness we will henceforth refer to $\left|s_{t}\right\rangle$ and $\left|x_{t}\right\rangle$ as "global" and "local" bases, respectively. We emphasize, though, that this need not be the case and the two sets are, in fact, general.

The central quantity of a dynamic Bayesian network is the joint distribution [3-6]

$$
P\left(x_{0}, x_{1}, \cdots, x_{N}\right)=\sum_{s} P_{s} \prod_{n=0}^{N} p\left(x_{n} \mid s_{n}\right)
$$

![img-0.jpeg](img-0.jpeg)

Fig. 1: (a) Diagrammatic representation of the unitary evolution of a (possibly composite) quantum system with (global) states $\left|s_{t}\right\rangle=U_{t}|s\rangle$, and the set of all possible (local) paths $\left|x_{0}\right\rangle \rightarrow\left|x_{1}\right\rangle \rightarrow\left|x_{2}\right\rangle$ which can be associated with this evolution. (b) The path probability $P\left(x_{0}, x_{1}, \cdots, x_{N}\right)$, eq. (1), may be determined by performing local measurements $M_{s}$ on independent copies of a quantum system and postselecting the outcomes, eq. (5). (c) Alternatively, one may obtain the same statistics by performing a global measurement on correlated copies prepared in a broadcast state, eq. (7).
associated with a (local) path $\left|x_{0}\right\rangle \rightarrow\left|x_{1}\right\rangle \rightarrow\left|x_{2}\right\rangle \rightarrow \cdots$. The conditionalprobability of finding the system in the (local) state $\left|x_{t}\right\rangle$ given that it is in the (global) state $\left|s_{t}\right\rangle$ at time $t$ is $p\left(x_{t}\left|s_{t}\right\rangle\right)=\left|\left\langle x_{t} \mid U_{t}\right| s\right\rangle\left.\right|^{2}$ [15]. Equation (1) is a sum over all (global) trajectories $s$ of the path probability $P_{s} \prod_{n} p\left(x_{n} \mid s_{n}\right)$ of the conditional trajectory $\left(s, x_{0}, x_{1}, \cdots, x_{N}\right)$. It is a proper probability distribution, in the sense that it is non-negative and all its marginals are non-negative. It also contains the complete information about the multi-time properties of the (local) variable $x$, while fully preserving the quantum features of the system, in contrast to the two-projective measurement scheme [20-22]. It is the key quantity involved in the study of the nonequilibrium properties of small composite systems $[7-18]$. We next describe an experimental protocol to determine eq. (1) based on multiple identical copies of the quantum system and postselection.

Experimental scheme. - We begin, for simplicity, by treating the case of the two-point distribution $P\left(x_{0}, x_{1}\right)$ at time $t_{0}=0$ and a later time $t_{1}$. To this end, we consider two independent copies $\rho \otimes \rho$ of the system. We assume, as done in the two-point-measurement scheme, that the eigenbasis of the system has been determined. The protocol consists of two stages: In a first step, each copy is measured in the (global) eigenstate $|s\rangle$ by applying the projector $\Pi_{s} \otimes \Pi_{s}$ with $\Pi_{s}=|s\rangle\langle s|$. This results in the state $\left(\Pi_{s} \otimes \Pi_{s}\right)(\rho \otimes \rho)=P_{s}^{2} \Pi_{s} \otimes \Pi_{s}$. In a second step, half of the copies are projected at $t=t_{0}$ in the (local) state $\left|x_{0}\right\rangle$, while the second half is projected at $t=t_{1}$ in the (local) state $\left|x_{1}\right\rangle$, for a given (global) state $|s\rangle$. The corresponding measurement operator reads $M_{x_{0}, x_{1}}=\left|x_{0}\right\rangle\left\langle x_{0}\right| \otimes U_{t_{1}}^{\dagger}\left|x_{1}\right\rangle\left\langle x_{1}\right| U_{t_{1}}$, with $\sum_{x_{0}, x_{1}} M_{x_{0}, x_{1}}=I$, and we obtain

$$
\frac{\operatorname{Tr}\left[M_{x_{0}, x_{1}}\left(\Pi_{s} \otimes \Pi_{s}\right)(\rho \otimes \rho)\right]}{\operatorname{Tr}\left[\Pi_{s} \rho\right]}=P_{s}\left|\left\langle x_{0} \mid s\right\rangle\right|^{2}\left|\left\langle x_{1} \mid U_{t_{1}} \mid s\right\rangle\right|^{2}
$$

The joint probability distribution $P\left(x_{0}, x_{1}\right)$ of the dynamic Bayesian network then follows by summing eq. (2)

over all (global) trajectories $s$ :

$$
P\left(x_{0}, x_{1}\right)=\sum_{s} P_{s}\left|\left\langle x_{0} \mid s\right\rangle\right|^{2}\left|\left\langle x_{1} \mid U_{t_{1}} \mid s\right\rangle\right|^{2}
$$

We emphasize that this protocol only relies on local measurements of each copy. Moreover, since two-pointmeasurement experiments already determine distributions by repeating measurements on many identically prepared systems [28-34], the above scheme may be realized without much additional experimental effort. This result can also be compared with the two-point-measurement (TPM) distribution, in which a single copy of the system is measured sequentially, first in $\left|x_{0}\right\rangle$ and then in $\left|x_{1}\right\rangle$. In this case the outcome $x_{0}$ in the first measurement occurs with probability $\sum_{s} P_{s}\left|\left\langle x_{0} \mid s\right\rangle\right|^{2}$. But afterwards, the system state is updated to $\left|x_{0}\right\rangle$, so the resulting distribution reads

$$
P_{\mathrm{TPM}}\left(x_{0}, x_{1}\right)=\sum_{s} P_{s}\left|\left\langle x_{0} \mid s\right\rangle\right|^{2}\left|\left\langle x_{1} \mid U_{t_{1}} \mid x_{0}\right\rangle\right|^{2}
$$

If the basis set $\left|x_{0}\right\rangle$ is compatible with $|s\rangle$, the two distributions coincide. Otherwise, we see that they are clearly different because of the last term.

The generalization to an arbitrary sequence of times, $t_{0}, t_{1}, \cdots, t_{N}$, is straightforward. It involves $(N+1)$ independent copies, $\rho_{\text {ind }}=\otimes_{n} \rho$, and the measurement operator $M_{\left\{x_{n}\right\}}=\otimes_{n}\left(U_{t_{n}}^{\dagger}\left|x_{n}\right\rangle\left\langle x_{n}\right| U_{t_{n}}\right)$. In this case, the multipoint joint probability distribution (1) is

$$
P\left(x_{0}, \cdots, x_{N}\right)=\sum_{s} \frac{1}{\operatorname{Tr}\left(\Pi_{s} \rho\right)} \operatorname{Tr}\left[M_{\left\{x_{n}\right\}}\left(\otimes_{n} \Pi_{s}\right) \rho_{\mathrm{ind}}\right]
$$

The path probability (1) is thus obtained from the conditional expectation value of $M_{x}$ on postselected states.

We also mention here that, as shown theoretically in ref. [15] and experimentally in ref. [17], Bayesian networks of the above form satisfy fluctuation theorems, and also reproduce the correct averages for changes of observables, as is typical when talking about heat and work. To illustrate the latter point, suppose $\left|x_{0}\right\rangle$ and $\left|x_{1}\right\rangle$ are the eigenbasis of two observables $X_{0}=\sum_{x_{0}} x_{0}\left|x_{0}\right\rangle\left\langle x_{0}\right|$ and $X_{1}=\sum_{x_{1}} x_{1}\left|x_{1}\right\rangle\left\langle x_{1}\right|$. These could represent, for instance, the energy of a system at two different times. It then follows from eq. (3) that

$$
\sum_{x_{0}, x_{1}}\left(x_{1}-x_{0}\right) P\left(x_{0}, x_{1}\right)=\operatorname{Tr}\left[X_{1} \rho\left(t_{1}\right)-X_{0} \rho(0)\right]
$$

which is what one would expect for the average change of the observables in the absence of back action. The same is not true for the TPM distribution (4), unless $\left[X_{0}, \rho(0)\right]=0$.

Generalized measurement operators. - The most general measurements in quantum theory are the socalled positive-operator-valued measures (POVMs) [52]. Such quantum measurements may always be realized as ordinary projective measurements on an enlarged system [52]. In order to derive the POVM corresponding
to the measurement of the path probability (1), we note that eq. (5) may be written as the expectation value

$$
P\left(x_{0}, \cdots, x_{N}\right)=\operatorname{Tr}\left[M_{\left\{x_{n}\right\}} \rho_{\mathrm{bro}}\right]
$$

where $\rho_{\text {bro }}=\sum_{s} P_{s}|s \cdots s\rangle\langle s \cdots s|$ denotes a broadcast state [54]. Like the case of $(N+1)$ independent copies, this state has the property that if we take the partial trace over all except one of the subsystems, we always recover the original state $\rho$. Thus, locally, each copy is in state $\rho$, although, globally, they are in a quantum-correlated state. The multipoint joint probability distribution (1) of a dynamic Bayesian network may therefore be evaluated either using independent copies and postselection or directly as the outcomes of the operator $M_{\left\{x_{n}\right\}}$ on a broadcast state of correlated copies.

We now introduce a completely positive tracepreserving map, $\mathcal{E}(\bullet)=\sum_{\{i\}} E_{\{i\}} \bullet E_{\{i\}}^{\dagger}$, with Kraus operators $E_{\{i\}}=\sum_{r}|r r \cdots r\rangle\left\langle r i_{1} \cdots i_{N}\right|$ and collective index $\{i\}=\left\{i_{1} \cdots i_{N}\right\}$ labelling the eigenstates of the system, such that the broadcast state can be constructed from $(N+1)$ independent copies as $\rho_{\text {bro }}=\mathcal{E}\left(\otimes_{n} \rho\right)$ (see footnote ${ }^{1}$ ). Using the cyclic property of the trace, we obtain

$$
P\left(x_{0}, \cdots, x_{N}\right)=\operatorname{Tr}\left[J_{\left\{x_{n}\right\}}\left(\otimes_{n} \rho\right)\right]
$$

with the positive semidefinite operators $J_{\left\{x_{n}\right\}}=$ $\sum_{\{i\}} E_{\{i\}}^{\dagger} M_{\left\{x_{n}\right\}} E_{\{i\}}$. Since $\sum_{\left\{x_{n}\right\}} J_{\left\{x_{n}\right\}}=I$, they form a POVM [52]. The set of operators $J_{\left\{x_{n}\right\}}$ define the general quantum measurement of the path probability (1) of a dynamic Bayesian network on $(N+1)$ independent copies. There is a trade-off between $M_{\left\{x_{n}\right\}}$, which involves local measurements and post-selection, and $J_{\left\{x_{n}\right\}}$, which involves nonlocal measurements but requires no postselection.

It is interesting to compare the number of measurements needed to determine the joint probability distribution (1) using either multiple copies or standard tomographic methods [55] (we consider, for simplicity, the case of two times). Process tomography involves the measurement of $d^{4}-d^{2}$ observables (see ref. [55], sect. 8.4.2). This exponential scaling with the size $d$ of the system ( $d=2^{n}$ for $n$ spins) should be contrasted with the linear dependence obtained for the operators $M_{x_{1}, x_{0}}$, eq. (3), and $J_{x_{1}, x_{0}}$, eq. (5), which only require the measurement of $2 n$ observables (one per copy).

Connection with a no-go theorem for quantum work. - Reference [50] has recently examined general measurement schemes to evaluate the statistics of nonequilibrium work performed on coherent systems. In this instance, the observable $x$ is the energy of the system and the work distribution is given as the expectation $P(w)=\operatorname{Tr}\left[\left(\otimes_{n} \rho\right) W(w)\right]$, with the general work POVM $W(w)=\sum_{i j} \delta\left[w-\left(x_{j}-x_{i}\right)\right] J_{x}$. The main conclusion of

[^0]
[^0]:    ${ }^{1}$ The quantum channel $\mathcal{E}$ requires knowledge of the eigenstates of $\rho$, which is why it does not violate the so-called no-broadcasting theorem [54].

Table 1: Comparison of different approaches to characterize nonequilibrium work fluctuations in driven quantum systems: twopoint measurements [20-22], work operators [60,61], quasiprobabilities [62,63] and dynamic Bayesian networks [15-18]. Only the latter scheme yields work densities that are measurable, obey fluctuation relations and apply to quantum coherent systems.


ref. [50] is that no POVM exists such that i) the average work corresponds to the difference of average energy for closed quantum systems (first law) and ii) the work statistics agree with the two-point-measurement method for states with no coherence in the energy basis (classicalstate limit), even if multiple copies are accessible. In other words, it does not seem possible to simultaneously obey the first law of thermodynamics and respect the classicalstate limit in coherent systems. However, this result is based on the assumption that the measurement operator does not depend on the state $\rho$, that is, no information about the initial state is available. By contrast, we have here shown that the Bayesian-network approach allows the determination of the joint probability distribution (1), and, in turn, of the nonequilibrium work distribution for coherent (as well as correlated multipartite) systems, by relaxing this restriction and assuming that the eigenbasis of the system has been determined. In a sense, the hypothesis of state independence, which was based on a universality argument, thus seems too strong. As a matter of fact, even the evaluation of the classical work statistics along single trajectories in stochastic thermodynamics presupposes knowledge of the driven potential [19]. In addition, there exists many quantum protocols that require information about the eigenbasis of the system, from the two-point-measurement scheme [20-22] to optimal cloning [56,57] and quantum parameter estimation [58,59]. We further note that relaxing the assumption of state independence implies that the linearity of the work probability distribution with respect to convex combinations of initial states [50] does no longer hold in general, except when these states belong to the eigenbasis set.

Compared with other methods to specify quantum work distributions, such as the two-point-measurement scheme [20-22], the work-operator formalism [60,61] or the quasiprobability approach [62,63], the dynamic-Bayesiannetwork framework $[15,16,18]$ appears to be currently the only one leading to quantum work distributions that i) are measurable, that is, are described by a POVM, ii) satisfy nonequilibrium fluctuation theorems and iii) apply to coherent systems (table 1) [50]. It hence comes across as a powerful tool to study nonequilibrium quantum processes of composite systems.

Examples. - We next illustrate our results by computing the two-point path probability (1) for two thermodynamic examples for work extraction [64] and heat exchange [65]: a driven coherent qubit and a correlated pair of qubits at two different temperatures.

Driven coherent qubit. We consider the minimal example of a qubit with Hamiltonian $H_{t}=g_{t} \sigma_{z}$, whose gap is adiabatically varied from $g_{t_{0}}$ to $g_{t_{1}}$. The system is assumed to be initially in state $\rho=\rho_{\mathrm{th}}+a \sigma_{x} / 2$, with parameter $a$ and thermal distribution $\rho_{\mathrm{th}}=\exp \left(-\beta g_{0} \sigma_{z}\right) / Z$; here $Z=\operatorname{Tr}\left[\exp \left(-\beta g_{0} \sigma_{z}\right)\right]$ denotes the partition function at inverse temperature $\beta=1 / T$. The qubit exhibits coherences in the energy basis when $a \neq 0$. As a consequence, the eigenbasis $\left|s_{ \pm}\right\rangle$differs from the energy basis $\left|x_{ \pm}\right\rangle$ : we have $\left|s_{+}\right\rangle=\cos (\theta / 2)\left|x_{+}\right\rangle+\sin (\theta / 2)\left|x_{-}\right\rangle$and $\left|s_{-}\right\rangle=-\sin (\theta / 2)\left|x_{+}\right\rangle+\cos (\theta / 2)\left|x_{-}\right\rangle$, where $\tan \theta=a / b$, with $b=\operatorname{Tr}\left[\sigma_{z} \rho_{\mathrm{th}}\right]$. The corresponding probabilities are $P_{s_{ \pm}}=\left(1 \pm \sqrt{a^{2}+b^{2}}\right) / 2$.

When $a \neq 0$, four different paths may occur: $\mid x_{0}=$ $+\rangle \rightarrow\left|x_{1}= \pm\right\rangle$ and $\left|x_{0}=-\right\rangle \rightarrow\left|x_{1}= \pm\right\rangle$. According to eq. (2) the respective two-point path probabilities are

$$
\begin{aligned}
P( \pm, \pm)= & P_{s_{ \pm}}\left|\left\langle x_{ \pm} \mid s_{ \pm}\right\rangle\right|^{2}\left|\left\langle x_{ \pm}\right| U_{t_{1}} \mid s \pm\right\rangle\left.\right|^{2} \\
& +P_{s_{ \mp}}\left|\left\langle x_{ \pm} \mid s_{\mp}\right\rangle\right|^{2}\left|\left\langle x_{ \pm}\right| U_{t_{1}} \mid s_{\mp}\right\rangle\left.\right|^{2} \\
= & \frac{1 \pm b}{2}-\frac{a^{2}}{4\left(a^{2}+b^{2}\right)}
\end{aligned}
$$

and, similarly, $P( \pm, \mp)=a^{2} / 4\left(a^{2}+b^{2}\right)$. These formulas fully account for quantum coherence $(a \neq 0)$ in contrast to the two-point-measurement approach [20-22], which destroys coherences, effectively setting $a=0$ :

$$
P(+,+)_{\mathrm{TPM}}=\left\langle x_{+} \mid \rho \mid x_{+}\right\rangle\left|\left\langle x_{+}\right| U_{t_{1}} \mid x_{+}\right\rangle\left.\right|^{2}=\frac{e^{-\beta g_{0}}}{Z}
$$

Analogously, $\quad P(-,-)_{\mathrm{TPM}}=\exp \left(+\beta g_{0}\right) / Z$ and $P( \pm, \mp)_{\mathrm{TPM}}=0$. Figure 2 shows, as an illustration, that quantum coherence significantly affects the joint distribution $P(+,+)$, except for very low temperatures: $P(+,+)$ is in general smaller than $P(+,+)_{\text {TPM }}$ and plateaus at a constant value at high temperatures.

Correlated pair of qubits. We next consider a pair of qubits $A B$ in the initial global state $\rho_{A B}=\rho_{\mathrm{th}}\left(\beta_{A}\right) \otimes$

![img-1.jpeg](img-1.jpeg)

Fig. 2: Path probability $P(+,+)$, eq. (6), for a driven coherent qubit as a function of temperature $T$ for various values of the parameter $a$. The Bayesian network results $(a \neq 0)$ are generally smaller than that of the two-point-measurement scheme $(a=0)$, except for very low temperatures. They further plateau at a constant value for large temperatures.
![img-2.jpeg](img-2.jpeg)

Fig. 3: Path probability $P(+-,-+)$, eq. (9), for a pair of correlated qubits $A B$ as a function of the temperature $T_{B}$ for various values of the parameter $a$ (and constant $T_{A}=0.4$ ). The Bayesian network results $(a \neq 0)$ strongly differ from that of the two-point-measurement scheme $(a=0)$, except for very low temperatures, and exhibit nonmonotonic behavior.
$\rho_{\mathrm{th}}\left(\beta_{B}\right)+\alpha \sigma_{+} \otimes \sigma_{-}+\alpha^{*} \sigma_{-} \otimes \sigma_{+}$with $\rho_{\mathrm{th}}\left(\beta_{i}\right)=$ $\exp \left(-\beta_{i} \sigma_{z}\right) / Z_{i}(i=A, B), \alpha=i a\left(Z_{A} Z_{B}\right)^{-1}$ and $|a| \leq 1$. The two qubits are initially correlated when $a \neq 0$. As a consequence, the global eigenbasis $|s\rangle$ of $\rho_{A B}$ differs from the local eigenbasis $|x\rangle=| \pm \pm\rangle$ of $\rho_{A} \otimes \rho_{B}$.

The two qubits exchange energy during time $t_{1}$ by interacting via a partial SWAP, $U_{t_{1}}=(I+i S) / \sqrt{2}$, where $S$ is the swap operator, $S|\phi \psi\rangle=|\psi \phi\rangle$. We thus have $U_{t_{1}}| \pm \pm\rangle=\exp (i \pi / 4)| \pm \pm\rangle$ and $U_{t_{1}}| \pm \mp\rangle=(| \pm \mp\rangle$ $+i| \pm \pm\rangle) / \sqrt{2}$. We concretely compute the two-point joint probability distribution $P(+-,-+)$ of the dynamic Bayesian network for the local path $|+-\rangle \rightarrow|-+\rangle$ by evaluating the POVM given in eq. (8). Using $M_{(+-)(-+)}=$ $|+-\rangle\langle+-\mid \otimes U_{t_{1}}^{\dagger}|-+\rangle\langle-+\mid U_{t_{1}}$ and $E_{i}=\sum_{r}|r r\rangle\langle r i|$, with
$|r\rangle$ and $|i\rangle$ eigenvectors of $\rho_{A B}$, we evaluate $J_{(+-)(-+)}=$ $\sum_{i} E_{i}^{\dagger} M_{(+-)(-+)} E_{i}$ and obtain

$$
\begin{aligned}
J_{(+-)(-+)}= & \frac{1}{2\left\{4 a^{2}+[\exp (-\Delta \beta)-\exp (\Delta \beta)]^{2}\right\}} \\
& \times(|+-\rangle\langle+-\mid \otimes \mathbf{A}+|+-\rangle\langle-+\mid \otimes \mathbf{B} \\
& +|-+\rangle\langle+-\mid \otimes \mathbf{B}^{\dagger}+|-+\rangle\langle-+\mid \otimes \mathbf{C})
\end{aligned}
$$

with $\mathbf{A}=\left\{a^{2}+[\exp (-\Delta \beta)-\exp (\Delta \beta)-a]^{2}\right\} I_{4}, \mathbf{B}=$ $-a\left\{2 i a+(1-i)[\exp (-\Delta \beta)-\exp (\Delta \beta)]\right\} I_{4}$ and $\mathbf{C}=2 a^{2} I_{4}$. Taking the expectation value over two independent copies $\rho_{A B} \otimes \rho_{A B}$, we eventually find

$$
\begin{aligned}
P(+-,-+) & =\operatorname{Tr}\left[J_{(+-)(-+)} \rho_{A B} \otimes \rho_{A B}\right]= \\
& \frac{e^{-\Delta \beta}}{2 Z_{A} Z_{B}} \cdot \frac{a \gamma}{Z_{A} Z_{B}\left[\gamma+e^{2 \Delta \beta}\left(e^{2 \Delta \beta}+\xi\right)\right]}
\end{aligned}
$$

where we have defined $\xi=2 a^{2}+1$ and $\gamma=\exp (2 \Delta \beta) \xi+$ 1. Equation (12) entirely captures quantum correlations $(a \neq 0)$ between the two qubits at $t_{0}$ and $t_{1}$, contrary to the two-point-measurement result to which it reduces for $a=0$. Figure 3 displays the behavior of $P(+-,-+)$ as a function of $T_{B}$ for fixed $T_{A}$. We observe that quantum correlations have a nontrivial (nonmonotonic) influence on the path probability (1). These effects vanish again in the limit of low temperatures.

Conclusions. - We have introduced a general experimental scheme to extract a dynamic Bayesian network from multiple copies of a multipartite quantum system. We have specifically shown how to determine the multipoint path probability (1) from local measurements of independent copies combined with postselection. This joint probability characterizes the multi-time properties of a given local observable, fully including quantum coherence and quantum correlations, without requiring tomography. We have further argued that this protocol may be regarded as a global generalized measurement and derived the corresponding POVM, whose experimental implemenation does not entail any postprocessing. In view of its versatility, the present method can be implemented on many experimental platforms, including nuclear magnetic resonance [28], trapped ions [29], cold atoms [31] and superconducting qubits [32]. We thus expect it to find broad applications from quantum many-body physics and quantum information theory to nonequilibrium quantum thermodynamics.

We acknowledge financial support from the São Paulo Research Foundation (Grants No. 2017/07973-5 and No. 2017/50304-7) and from the German Science Foundation (DFG) (Grant No. FOR 2724).

Data availability statement: All data that support the findings of this study are included within the article (and any supplementary files).
