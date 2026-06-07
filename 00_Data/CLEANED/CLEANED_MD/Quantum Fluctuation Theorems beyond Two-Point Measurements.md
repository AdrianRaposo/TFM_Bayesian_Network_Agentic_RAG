# Quantum fluctuation theorems beyond two-point measurements 

Kaonan Micadei, ${ }^{1}$ Gabriel T. Landi, ${ }^{2}$ and Eric Lutz ${ }^{1}$<br>${ }^{1}$ Institute for Theoretical Physics I, University of Stuttgart, D-70550 Stuttgart, Germany<br>${ }^{2}$ Instituto de Física da Universidade de São Paulo, 05314-970 São Paulo, Brazil

We derive detailed and integral quantum fluctuation theorems for heat exchange in a quantum correlated bipartite thermal system using the framework of dynamic Bayesian networks. Contrary to the usual two-projective-measurement scheme that is known to destroy quantum features, these fluctuation relations fully capture quantum correlations and quantum coherence at arbitrary times.

Fluctuation theorems are fundamental generalizations of the second law of thermodynamics for small systems. While the entropy production $\Sigma$ is a nonnegative deterministic quantity for macroscopic systems, it becomes random at the microscopic scale owing to the presence of nonnegligible thermal [1,2] or quantum [3, 4] fluctuations. Detailed fluctuation theorems quantify the probability of occurrence of negative entropy production events via the general relation $P(\Sigma) / P(-\Sigma)=\exp (\Sigma)$ [5]. Integral fluctuation theorems take on the form $\langle\exp (-\Sigma)\rangle=$ 1 after integration over $\Sigma$. The concavity of the exponential function then implies that the entropy production is only positive on average, $\langle\Sigma\rangle \geq 0$. The generic validity of fluctuation theorems arbitrarily far from equilibrium makes them particularly useful in nonequilibrium physics. They have been extensively investigated for this reason, both theoretically and experimentally, for classical systems $[6,7]$. These studies have provided unique insight into the thermodynamics of microscopic systems, from colloidal particles to enzymes and molecular motors $[1,2]$.

The situation is more involved in the quantum regime. Quantum fluctuation theorems are commonly studied within the two-point-measurement (TPM) scheme [3, 4]. In this approach, the energy change, and in turn the entropy production, of a quantum system are determined for individual realizations by projectively measuring the energy at the beginning and at the end of a nonequilibrium protocol [8]. Equivalent formulations based on Ramsey-like interferometry [10, 11] and generalized measurements [12] have also been proposed. These methods were used to perform experimental tests of quantum fluctuations theorems, both for mechanically driven [13-15] and thermally driven [16] systems, using NMR, trappedion and cold-atom setups. The TPM procedure successfully captures the discrete quantum energy spectrum of the system, as well as its nonequilibrium quantum dynamics between the two measurements [9]. However, due to its projective nature, it completely fails to account for quantum correlations and quantum coherence, two central features of quantum theory, that may be present in initial and final states of the system. In that sense, the TPM scheme may thus be viewed as not fully quantum.

In this paper, we present detailed and integral quantum fluctuation theorems for heat exchange between
quantum correlated bipartite thermal systems using a dynamic Bayesian network approach [17, 18]. Global and local descriptions of a composite system usually differ because of quantum correlations. The dynamic Bayesian network offers a powerful framework to specify the local dynamics conditioned on the global states, hence preserving all the quantum properties of the system, including quantum correlations and quantum coherence, in contrast to the TPM strategy. Our findings reduce to the Jarzynski-Wójcik fluctuation theorem in the absence of correlations [19] and to the exchange fluctuation theorem of Jevtic and coworkers in the presence of classical correlations [20]. They additionally complement recent attempts to obtain fully quantum fluctuation theorems for mechanically driven systems [21-24] (see also Refs. [25, 26]).

In the following, we first derive a detailed quantum fluctuation theorem for the ratio of the probability of a conditional local trajectory of the system and its reverse. We show that it accounts both for quantum correlations (in the form of a stochastic quantum mutual information [27]) and for quantum coherence (in the form of a stochastic relative entropy of coherence [28]). We further identify a contribution to the entropy production that stems from the randomness of the conditional local trajectory. Moreover, we obtain a detailed fluctuation relation for the joint probability of all quantum contributions and demonstrate that each of them, as well as their sum, individually satisfies an integral fluctuation theorem. Finally, we derive a modified quantum fluctuation relation for the heat variable alone, valid for any intermediate times.

Dynamic Bayesian networks. We consider two arbitrary quantum systems, $A$ and $B$, with respective Hamiltonians $H_{A}$ and $H_{B}$, initially prepared in the joint state,

$$
\rho_{A B}(0)=\rho_{A}^{0} \otimes \rho_{B}^{0}+\chi_{A B}
$$

where $\rho_{i}^{0}=\exp \left(-\beta_{i} H_{i}\right) / Z_{i}(i=A, B)$ are local thermal Gibbs states at inverse temperatures $\beta_{i}$ and $Z_{i}=$ $\operatorname{tr}\left[\exp \left(-\beta_{i} H_{i}\right)\right]$ is the corresponding partition function (see Fig. 1). The operator $\chi_{A B}$ induces correlations between the two subsystems. It is assumed to satisfy $\operatorname{tr}_{i}\left[\chi_{A B}\right]=0$, so that the reduced states, $\rho_{i}(0)=$ $\operatorname{tr}_{j}\left[\rho_{A B}(0)\right]$, are locally thermal even though $A$ and $B$ are globally correlated [20]. This condition guarantees

that the local systems have a well defined temperature. Thermal contact between the two systems is established at $t=0$ by letting them interact via an energy conserving unitary transformation $U(t)$ verifying $[U(t), H_{A}+H_{B}]=0$. The global basis $\left|s_{n}\right\rangle$ at time $t_{n}$ is defined as $\rho_{A B}\left(t_{n}\right)=U\left(t_{n}\right) \rho_{A B}(0) U^{\dagger}\left(t_{n}\right)=\sum_{s} P_{s}\left|s_{n}\right\rangle\left\langle s_{n}\right|$, where $P_{s}$ is the initial population. On the other hand, the corresponding local bases, $\left|a_{n}\right\rangle$ and $\left|b_{n}\right\rangle$, follow from the decomposition of the reduced states, $\rho_{A}\left(t_{n}\right)=\sum_{a_{n}} P_{a_{n}}\left|a_{n}\right\rangle\left\langle a_{n}\right|$ and $\rho_{B}\left(t_{n}\right)=\sum_{b_{n}} P_{b_{n}}\left|b_{n}\right\rangle\left\langle b_{n}\right|$. We note that while the evolution of the global state is deterministic, with each eigenstate $\left|s\right\rangle$ simply evolving in time according to $U(t)\left|s\right\rangle$ and the initial populations $P_{s}$ kept fixed, that of the local (reduced) states is stochastic.

Our aim is to assess the statistics of the heat exchanged between $A$ and $B$ at any given time, accounting for all the quantum properties of the process, including quantum correlations and quantum coherence. This endeavor faces a number of mathematical and physical difficulties. Mathematically, the global state is not diagonal in the energy representation because of the nonvanishing correlations. As a result, the global and local bases are not mutually orthogonal, $\left\langle a_{n} b_{n} \mid s_{n}\right\rangle \neq \delta_{a_{n} b_{n}, s_{n}}$, making their relationship nontrivial, except when $\chi_{A B}=0$. The physical consequence is that the local bases, in which the exchanged heat variable is evaluated, do not contain the complete information about the composite system.

In order to solve these issues, we employ the tools of dynamic Bayesian networks which are widely used in computer science and statistics [17, 18]. They can be regarded as generalizations of hidden Markov models [29] which have been used to study classical fluctuation relations in the presence of hidden degrees of freedom [30, 31] (see also Refs. [32, 33]). These techniques allow the systematic analysis of probabilities of events conditioned on some other events. Concretely, at any given time $t_{n}$, the conditional probability of finding the local systems $A$ and $B$ in their respective energy eigenstates $\left|a_{n}\right\rangle$ and $\left|b_{n}\right\rangle$, given that the global system is in state $\left|s_{n}\right\rangle$, is,

$$
P\left(a_{n}, b_{n} \mid s_{n}\right)=\left|\left\langle a_{n} b_{n} \mid s_{n}\right\rangle\right|^{2}
$$

For any sequence of times, $t_{1}, t_{2}, \ldots t_{N}$, we may define a conditional trajectory $\Gamma=\left(s, a_{0}, b_{0}, a_{1}, b_{1}, \ldots, a_{N}, b_{N}\right)$ (see Fig. 2) and the corresponding path probability as,

$$
\mathcal{P}[\Gamma]=P_{s} P\left(a_{0}, b_{0} \mid s\right) P\left(a_{1}, b_{1} \mid s_{1}\right) \ldots P\left(a_{N}, b_{N} \mid s_{N}\right)
$$

The corresponding probability for the local trajectory is obtained by summing over all quantum trajectories $s$,

$$
\mathcal{P}\left(a_{0}, b_{0}, \ldots, a_{N}, b_{N}\right)=\sum_{s} \mathcal{P}[\Gamma]
$$

We may analogously introduce a reversed conditional local trajectory $\Gamma^{*}=\left(s^{*}, a_{N}, b_{N}, \ldots, a_{0}, b_{0}\right)$ with path probability $\mathcal{P}\left[\Gamma^{*}\right]=P_{s^{*}} \bar{P}\left(a_{N}, b_{N} \mid s^{*}\right) \ldots \bar{P}\left(a_{0}, b_{0} \mid s_{N}^{*}\right)$ where $\bar{P}\left(a_{n}, b_{n} \mid s_{N-n}^{*}\right)=\left|\left\langle a_{n} b_{n}\right| U^{\dagger}\left(t_{N-n}\right)\left|s^{*}\right\rangle\right|^{2}$.
![img-0.jpeg](img-0.jpeg)

Figure 1. Quantum correlated bipartite quantum system $A B$ in local thermal states at different temperatures. The initial joint state is of the form $\rho_{A B}(0)=\rho_{A}^{0} \otimes \rho_{B}^{0}+\chi_{A B}$ with Gibbs states, $\rho_{i}^{0}=\exp \left(-\beta_{i} H_{i}\right) / Z_{i}$ at inverse temperatures $\beta_{i}(i=A, B)$, and initial quantum correlations $\chi_{A B}$. During thermal interaction, the two arbitrary subsystems exchange the amount of stochastic heat $Q$.

For concreteness and simplicity, we shall next focus on the case of a two-time probability, taken to be the initial time $t=0$ and an arbitrary future time $t_{1}$. Generalizations to multiple times are straightforward. Marginalizing the conditional probability (3) over $a_{0}, b_{0}$ then yields,

$$
\mathcal{P}\left(a_{1}, b_{1}\right)=\sum_{s, a_{0}, b_{0}} \mathcal{P}[\Gamma]=\left\langle a_{1}, b_{1}\right| \rho_{A B}\left(t_{1}\right)\left|a_{1}, b_{1}\right\rangle
$$

which is the result one would have expected on physical grounds. We furthermore have the two probabilities $\mathcal{P}\left(a_{1}\right)=\sum_{b_{1}}\left\langle a_{1}, b_{1}\right| \rho_{A B}\left(t_{1}\right)\left|a_{1}, b_{1}\right\rangle$ and $\mathcal{P}\left(b_{1}\right)=$ $\sum_{a_{1}}\left\langle a_{1}, b_{1}\right| \rho_{A B}\left(t_{1}\right)\left|a_{1}, b_{1}\right\rangle$. Similarly, by only marginalizing over the global trajectory $s$, we obtain the path probability for the local trajectory $\left(a_{0}, b_{0}, a_{1}, b_{1}\right)$,

$$
\mathcal{P}\left(a_{0}, b_{0}, a_{1}, b_{1}\right)=\sum_{s} P_{s} P\left(a_{0}, b_{0} \mid s\right) P\left(a_{1}, b_{1} \mid s_{1}\right)
$$

Interestingly, these probabilities may also be cast in terms of the expectation value of a Choi matrix [37]. In the particular case where the initial state (1) is separable $\left(\chi_{A B}=0\right)$, global and local bases are identical, $|s\rangle=|a b\rangle$, and Eq. (6) reduces to the TPM result [19],

$$
\mathcal{P}\left(a_{0}, b_{0}, a_{1}, b_{1}\right)=P_{a}^{0} P_{b}^{0}\left|\left\langle a_{1}, b_{1}\right| U(t)\left|a_{0}, b_{0}\right\rangle\right|^{2}
$$

Expression (6) hence generally contains more information about the local quantum dynamics than Eq. (7).

Detailed quantum fluctuation theorem. We next derive a detailed fluctuation theorem for the ratio of forward and reversed conditional trajectories using Eq. (3),

$$
\frac{\mathcal{P}[\Gamma]}{\mathcal{P}\left[\Gamma^{*}\right]}=\frac{P_{s}}{P_{s^{*}}} \frac{P\left(a_{0}, b_{0} \mid s\right) P\left(a_{1}, b_{1} \mid s_{1}\right)}{\bar{P}\left(a_{1}, b_{1} \mid s^{*}\right) \bar{P}\left(a_{0}, b_{0} \mid s_{1}^{*}\right)}
$$

In order to obtain an explicit expression for the theorem, we begin by rewriting the first ratio in Eq. (8) as,

$$
\frac{P_{s}}{P_{s^{*}}}=\frac{P_{a_{0}} P_{b_{0}}}{P_{a_{1}} P_{b_{1}}} \exp \left(\ln \frac{P_{s}}{P_{a_{0}} P_{b_{0}}}-\ln \frac{P_{s^{*}}}{P_{a_{1}} P_{b_{1}}}\right)
$$

![img-1.jpeg](img-1.jpeg)

Figure 2. Dynamic Bayesian network. The global quantum trajectory is specified by the state |s(t)⟩ which evolves deterministically. At each instant tn, the conditional probability of finding the reduced systems, A and B, in their local energy eigenstates |aₙ,bₙ⟩, given the state |sn⟩, is specified by Eq. (2). The set of points (s,a0,b0,a1,b1,...) defines a conditional local trajectory Γ, with path probability P[Γ], Eq. (3), that accounts for the full quantum properties of the system.

where Paₙ and Pbₙ are the thermal occupations at time t1. This then leads to the quantum fluctuation relation,

$$
\frac{\mathcal{P}[\Gamma]}{\mathcal{P}\left[\Gamma^{*}\right]}=\exp\left(Q_{A}\Delta\beta+I_{0}-I_{1}-\Sigma_{A}-\Sigma_{B}+\gamma\right). \tag{10}
$$

We have here identified (i) the entropy production associated with heat exchange, QAΔβ = (Ea1-Ea0){βAβB}, where Eaₙ are the eigenenergies of Hₙ, (ii) the stochastic quantum mutual information, I0 = ln[Pₙ/PaₙPbₙ], that accounts for initial correlations between subsystems A and B, and (iii) the stochastic quantum mutual information, I1 = ln[Pₙ/Ψ(a1)Pfb1)], that characterizes quantum correlations at the final time. We have additionally introduced the stochastic quantum relative entropies, ΣA = ln[Ψ(a1)/Pa1] and ΣB = ln[Ψ(b1)/Pb1]. Finally, we have discerned a contribution to the entropy production, γ = ln[P(a0,b0|s)P(a1,b1|s1)/P(a1,b1|s*)P(a0,b0|s1⟩], that comes from the second ratio in Eq. (8). This term stems from the stochastic nature of the conditional dynamics, in analogy to the classical result of Ref. [34]. It vanishes on average, since the global dynamics is unitary and no extra energy is exchanged with an external bath.

Equation (10) is our first main result. It generalizes quantum fluctuation theorems for heat exchange beyond the standard TPM approach [19, 20]. To make this point more precise, we express the stochastic quantum mutual informations, I<sup>l</sup> = J<sup>l</sup> + C<sup>l</sup>, (l = 0,1), as a sum of the stochastic classical mutual information, J<sup>l</sup> = ln(Pa/lb1/Pa/lb1), and of the stochastic quantum relative entropy of coherence, C<sup>l</sup> = ln(Pₙ/Paₙb1), which is a proper measure of quantum coherence in a given basis [28]. The detailed fluctuation relation (10) therefore fully captures, at any time, the presence of quantum correlations between the two subsystems and of quantum coherence, in the heat statistics. It provides, in particular, an extension of the fluctuation theorem of Jarzynski and Wójcik, P[Γ]/P[Γ*] = exp(QAΔβ) [19] and of Jevtic and coauthors, P[Γ]/P[Γ*] = exp(QAΔβ - ΔJ) [20].

By evaluating the average of the logarithm of Eq. (10), we furthermore obtain an expression for the mean heat exchanged between the subsystems A and B,

$$
\langle Q_{A}\rangle\Delta\beta = \Delta\langle I \rangle + S(\rho_{A}| | \rho_{A}^{0}) + S(\rho_{B}| | \rho_{B}^{0}), \tag{11}
$$

in agreement with the results of Ref. [35]. Equation (11) indicates that the heat current may be reversed, thus flowing from cold to hot, when the initial correlations are such that Δ⟨I⟩ + S(ρA| |ρB⟩) + S(ρB| |ρB⟩) ≤ 0. This process is enabled by a trade-off between correlations and entropy [36]. The detailed fluctuation relation (10) extends this trade-off to the level of individual quantum realizations.

**Integral quantum fluctuation theorems.** An integral fluctuation relation that incorporates all the quantum contributions may be derived from Eq. (10) by integrating over all conditional trajectories Γ. We find,

$$
\langle \exp\left(Q_{A}\Delta\beta + I_{0} - I_{1} - \Sigma_{A} - \Sigma_{B} + \gamma\right) \rangle = 1. \tag{12}
$$

Interestingly, by using the rules of Bayesian networks, one may show that each contribution satisfies an individual quantum fluctuation theorem [37]. We have, for example,

$$
\begin{split}
\langle e^{-I_{0}}\rangle &= \sum_{\Gamma} \mathcal{P}[\Gamma] \exp \left( -\ln \frac{P_{s}}{P_{a_{0}}P_{b_{0}}} \right) \\
&= \sum_{s,a_{0},b_{0}} P(a_{0}, b_{0}|s) P_{a_{0}}P_{b_{0}} = \sum_{a_{0},b_{0}} P_{a_{0}}P_{b_{0}} = 1. \tag{14}
\end{split}
$$

In a similar fashion (see Ref. [37] for details), we obtain,

$$
\langle e^{-I_{l}}\rangle = \langle e^{-J_{l}}\rangle = \langle e^{-C_{l}}\rangle = \langle e^{-\Sigma_{l}}\rangle = \langle e^{-\gamma}\rangle = 1. \tag{15}
$$

We therefore conclude that contributions from both classical and quantum correlations, J<sup>l</sup> and I<sup>l</sup>, as well as from quantum coherence, C<sup>l</sup>, separately obey an integral fluctuation relation, generalizing the recent findings of Refs. [38, 39] for the quantum mutual information. Equation (15) is our second main result.

**Modified detailed quantum fluctuation theorem for heat.** The detailed fluctuation relation (10) is formulated in terms of the probabilities of forward and reversed conditional trajectories. However, it is often convenient, both from a theoretical and an experimental point of view, to express it as a function of the joint probability of the different variables that appear in the exponent [40–42]. To this end, it is important to separate variables according to their properties under time reversal [42]. We therefore introduce the odd (information) variable, K = I1 - I0 + ΣA + ΣB, and define the forward joint probability distribution of K, the odd variable Q and γ as P<sup>f</sup>(Q,K,γ) = ⟨δ(Q - Q[Γ])δ(K - K[Γ,s*])δ(γ - γ[Γ,s*])⟩. The corresponding reversed joint probability distribution is P<sup>r</sup>(-Q, -K,γ̇) = ⟨δ(Q - Q[Γ*])δ(K - K[Γ*,s])δ(γ - γ[Γ*,s])⟩ with γ̇[Γ,s*] = - ln(|⟨a<sup>0</sup> b<sup>0</sup> |s⟩|² |⟨a<sup>1</sup> b<sup>1</sup> |U<sup>1</sup> |s⟩|²)/(|⟨a<sup>1</sup> b<sup>1</sup> |s*⟩|² |⟨a<sup>0</sup> b<sup>0</sup> |U<sup>t</sup> |s*⟩|²). The relation (10) then implies the detailed quantum fluctuation theorem [37],

$$
\frac{P_{f}(Q, K, \gamma)}{P_{r}(-Q, -K, \gammȧ)} = \exp\left(Q\Delta\beta - K + \gamma\right). \tag{16}
$$

![img-2.jpeg](img-2.jpeg)

Figure 3. Generalized quantum fluctuation theorem for heat for the two-spin-1/2 example. a) Forward quantum heat distribution $P_f(Q)$ for the three values $(0, \pm Q_A)$ with (thick lines) and without (thin lines) initial quantum correlations $\chi_{AB}$, as a function of the thermal interaction $\tau$. b) Corresponding reversed heat distribution $P_r(Q)$. c) In the absence of initial correlations $(\alpha = 0)$, we have the Jarzynski-Wójcik relation $P_f(Q)/P_r(-Q) = \exp(Q\Delta\beta)$ (green dashed line). On the other hand, in the presence of initial quantum correlations $(\alpha \neq 0)$, we have the generalized fluctuation theorem, $P_f(Q)/P_r(-Q) = \exp(Q\Delta\beta)/\Psi(Q)$ [Eq. (17)] (purple solid line). The factor $\Psi(Q)$ encapsulates the quantum features of the correlations and modifies the $Q$-dependence.

In like manner, a more general fluctuation relation of the form (16) can be derived for all the individual quantum contributions by considering the joint probability distribution $P_f(Q, J_0, C_0, J_1, C_1, \Sigma_A, \Sigma_B, \gamma)$. Integrating Eq. (16) over $K$ and $\gamma$, we eventually arrive at the modified detailed quantum fluctuation relation for heat,

$$
\frac{P_f(Q)}{P_r(-Q)} = \frac{\exp(Q\Delta\beta)}{\Psi(Q)},
\tag{17}
$$

where the factor $\Psi(Q) = \int dK d\gamma \ P(K, \gamma|Q)e^{-K-\gamma}$ depends on the correlations between $Q$, $K$ and $\gamma$. In the absence of correlations between the two subsystems $A$ and $B$, we recover the Jarzynski-Wójcik result, $\Psi_{JW}(Q) = 1$ [19]. The presence of quantum correlations thus modifies the exponential dependence on the heat variable on the right-hand side of Eq. (17) through the function $\Psi(Q)$. This is our third main result.

Example. Our findings are valid for arbitrary quantum systems. As an illustration, we now consider the case of an initially quantum correlated two-spin-1/2 system with Hamiltonians $H_A = H_B = (1 - \sigma_z)/2$, where $\sigma_z$ is the usual Pauli operator. This system has been recently investigated experimentally in a Nuclear Magnetic Resonance setup in Ref. [35]. The correlation term in Eq. (1) is taken of the form $\chi_{AB} = \alpha |01\rangle\langle 10| + \alpha^* |10\rangle\langle 10|$ with parameter $\alpha$ [35]. The value $\alpha = 0$ corresponds to initially uncorrelated local systems. We choose $\alpha = -i \exp\left[-(\beta_A + \beta_B)/2\right] / (Z_A Z_B)$ for initial quantum correlations with nonzero geometric discord [35]. We let the two subsystems interact, and exchange the amount of heat $Q$, via the thermal operation $H_{int} = (\pi/2\tau) \left(\sigma_A^\top \sigma_B^- + \sigma_A^\top \sigma_B^\top\right)$ for a time $\tau$. The thermal interaction induces four transitions between the eigenstates of the two qubits, leading to three stochastic values of the heat, $Q = 0$ (twice) and $Q = \pm Q_A$, where $Q_A = (E_{a_1} - E_{a_0})$ is the energy variation of spin $A$.

We analytically solve the respective global and local spin dynamics, and determine the forward and reversed heat distributions, $P_f(Q) = \sum_{\Gamma} \delta(Q - Q[\Gamma]) P[\Gamma]$ and $P_r(-Q) = \sum_{\Gamma*} \delta(Q + Q[\Gamma^+]) P[\Gamma^+]$ [37]. The results are presented in Fig. 3 for $\exp(-\beta_A)/Z_A = 0.2$ and $\exp(-\beta_B)/Z_B = 0.3$. Figures 3ab show the forward and reversed quantum heat distributions for the three values $(0, \pm Q_A)$, with (thick lines) and without (thin lines) initial quantum correlations, as a function of the interaction $\tau$. We observe that the heat distributions depend explicitly on time and that the forward and reversed distributions are identical in the absence of initial correlations. Figure 3c displays the corresponding detailed quantum fluctuation relations for heat given by Eq. (17). Without initial correlations $(\alpha = 0)$, we recover the Jarzynski-Wójcik fluctuation theorem which corresponds to $\Psi_{JW}(Q) = 1$ (green dashed line). For $\alpha \neq 0$, the effect of the quantum correlations is clearly visible (purple solid line), modulating the $Q$-dependence via the function $\Psi(Q) \neq 1$.

Conclusions. We have used a dynamic Bayesian network approach to derive detailed and integral heat exchange fluctuation theorems for initially quantum correlated thermal bipartite systems. These fluctuation relations fully account for both quantum correlations.

and quantum coherence, two central quantum features, at arbitrary times, in contrast to the two-projectivemeasurement scheme. They provide much refined formulations of the second law of thermodynamics for small interacting quantum systems, compared to existing ones. We thus expect them to be useful for the study of far from equilibrium quantum thermodynamic systems.

Acknowledgements. We acknowledge financial support from the São Paulo Research Foundation (Grants No. 2017/07973-5 and No. 2017/50304-7) and from the German Science Foundation (DFG) (Grant No. FOR 2724).
[1] K. Sekimoto, Stochastic Energetics, (Springer, Berlin, 2010).
[2] U. Seifert, Stochastic thermodynamics, fluctuation theorems, and molecular machines, Rep. Prog. Phys. 75, 126001 (2012).
[3] M. Esposito, U. Harbola and S. Mukamel, Nonequilibrium fluctuations, fluctuation theorems, and counting statistics in quantum systems, Rev. Mod. Phys. 81, 1665 (2009).
[4] M. Campisi, P. Hänggi, and P. Talkner, Quantum Fluctuation Relations: Foundations and Applications, Rev. Mod. Phys., 83771 (2011).
[5] D. J. Evans and D. J. Searles, The Fluctuation Theorem, Advances in Physics 51, 1529 (2002).
[6] C. Jarzynski, Equalities and Inequalities: Irreversibility and the Second Law of Thermodynamics at the Nanoscale, Annu. Rev. Condens. Matter Phys. 2, 329 (2011).
[7] S. Ciliberto, R. Gomez-Solano, and A. Petrosyan, Fluctuations, Linear Response, and Currents in Out-ofEquilibrium Systems, Annu. Rev. Condens. Matter Phys. 4, 235 (2013).
[8] P. Talkner, E. Lutz, and P. Hänggi, Fluctuation theorems: Work is not an observable, Phys. Rev. E 75, 050102 (2007).
[9] C. Jarzynski, H. T. Quan, and S. Rahav, QuantumClassical Correspondence Principle for Work Distributions Phys. Rev. X 5, 031038 (2015).
[10] L. Mazzola, G. De Chiara, and M. Paternostro, Measuring the characteristic function of the work distribution, Phys. Rev. Lett. 110, 230602 (2013).
[11] R. Dorner, S. R. Clark, L. Heaney, R. Fazio, J. Goold, and V. Vedral, Extracting Quantum Work Statistics and Fluctuation Theorems by Single-Qubit Interferometry, Phys. Rev. Lett. 110, 230601 (2013).
[12] A. J. Roncaglia, F. Cerisola, and J. P. Paz, Work Measurement as a Generalized Quantum Measurement, Phys. Rev. Lett. 113, 250601 (2014).
[13] T. B. Batalhao, A. M. Souza, L. Mazzola, R. Auccaise, R. S. Sarthour, I. S. Oliveira, J. Goold, G. De Chiara, M. Paternostro, and R. M. Serra, Experimental reconstruction of work distribution and study of fluctuation relations in a closed quantum system, Phys. Rev. Lett. 113, 140601 (2014).
[14] S. An, J. Zhang, M. Um, D. Lv, Y. Lu, J. Zhang, Z. Yin, H. T. Quan, and K. Kim, Experimental test of the quantum Jarzynski equality with a trapped-ion system, Nature Phys. 11, 193 (2015).
[15] F. Cerisola, Y. Margalit, S. Machluf, A. J. Roncaglia, J.
P. Paz, and R. Folman, Using a quantum work meter to test non-equilibrium fluctuation theorems, Nature Commun. 8, 1241 (2017).
[16] S. Pal, T. S. Mahesh, B. K. Agarwalla, Experimental verification of quantum heat exchange fluctuation relation, arXiv:1811.07291.
[17] R. E. Neapolitan, Learning Bayesian Networks, (Prentice Hall, Upper Saddle River, 2003).
[18] A. Darwiche, Modeling and Reasoning with Bayesian Networks, (Cambridge University Press, Cambridge, 2009).
[19] C. Jarzynski and D. K. Wójcik, Classical and Quantum Fluctuation Theorems for Heat Exchange, Phys. Rev. Lett. 92, 230602 (2004).
[20] S. Jevtic, T. Rudolph, D. Jennings, Y. Hirono, S. Nakayama, and M. Murao, Exchange fluctuation theorem for correlated quantum systems, Phys. Rev. E 92, 042113 (2015).
[21] Á. M. Alhambra, L. Masanes, J. Oppenheim, and C. Perry, Fluctuating Work: From Quantum Thermodynamical Identities to a Second Law Equality, Phys. Rev. X 6, 041017 (2016).
[22] J. Åberg, Fully Quantum Fluctuation Theorems, Phys. Rev. X 8, 011019 (2018).
[23] J. J. Park, S. W. Kim, and V. Vedral, Fluctuation theorem for arbitrary quantum bipartite systems, arXiv:1705.01750.
[24] J. P. Santos, L. C. Céleri, G. T. Landi and M. Paternostro, The role of quantum coherence in non-equilibrium entropy production, npj Quantum Information 9, 23 (2019).
[25] G. Manzano, J. M. Horowitz, and J. M.?R. Parrondo,Quantum Fluctuation Theorems for Arbitrary Environments: Adiabatic and Nonadiabatic Entropy Production, Phys. Rev. X 8, 031037 (2018).
[26] H. Kwon and M.?S. Kim, Fluctuation Theorems for a Quantum Channel, Phys. Rev. X 9, 031029 (2019).
[27] M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information, (Cambridge University Press, Cambridge, 2000).
[28] T. Baumgratz, M. Cramer and M. B. Plenio, Quantifying Coherence, Phys. Rev. Lett. 113, 140401 (2014).
[29] R. L. Stratonovich, Conditional Markov Processes, Theory of Probability and its Applications 5, 156 (1960).
[30] K. Kawaguchi and Yo. Nakayama, Fluctuation theorem for hidden entropy production, Phys. Rev. E 88, 022147 (2013).
[31] J. Ehrich and A. Engel, Stochastic thermodynamics of interacting degrees of freedom: Fluctuation theorems for detached path probabilities, Phys. Rev. E 96, 042129 (2017).
[32] S. Ito and T. Sagawa, Information Thermodynamics on Causal Networks, Phys. Rev. Lett. 111, 180603 (2013).
[33] P. Strasberg and A. Winter, Stochastic thermodynamics with arbitrary interventions, arXiv:1905.07990.
[34] U. Seifert, Entropy production along a stochastic trajectory and an integral fluctuation theorem, Phys. Rev. Lett. 95, 040602 (2005).
[35] K. Micadei, J. P. S. Peterson, A. M. Souza, R. S. Sarthour, I. S. Oliveira, G. T. Landi, T. B. Batalhão, R. M. Serra, and E. Lutz, Reversing the direction of heat flow using quantum correlations, Nature Comm. 10, 2456 (2019).
[36] S. Lloyd, Use of mutual information to decrease entropy: implications for the second law of thermodynamics. Phys.

Rev. A 39, 5378 (1989).
[37] See Supplemental Material.
[38] V. Vedral, An information theoretic equality implying the Jarzynski relation, J. Phys. A: Math. Theor. 45, 272001 (2012).
[39] T. P. Xiong, L. L. Yan, F. Zhou, K. Rehan, D. F. Liang, L. Chen, W. L. Yang, Z. H. Ma, M. Feng, and V. Vedral, Experimental Verification of a Jarzynski-Related Information-Theoretic Equality by a Single Trapped Ion, Phys. Rev. Lett. 120, 010601 (2018).
[40] R. García-García, D. Domínguez, V. Lecomte, and A. B. Kolton, Unifying approach for fluctuation theorems from joint probability distributions, Phys. Rev. E 82, 030104(R)(2010).
[41] J. D. Noh and J.-M. Park, Fluctuation Relation for Heat, Phys. Rev. Lett. 108, 240603 (2012).
[42] S. Lahiri and A. M. Jayannavar, Derivation of not-socommon fluctuation theorems, Indian J. Phys. 89515 (2015).

# Supplemental Material: Quantum fluctuation theorems beyond two-point measurements 

## A. INTEGRAL FLUCTUATION THEOREMS

In this section, we present the derivations of the individual integral fluctuation theorems given in Eq. (15) of the main text. Special care should be paid to the order with which sums are evaluated.

We first start with the final stochastic mutual information $I_{1}$. We have,

$$
\begin{aligned}
& \left\langle e^{-I_{1}}\right\rangle=\sum_{\Gamma^{*}} P\left[\Gamma^{*}\right] \exp \left(-\ln \frac{P_{s^{*}}}{P_{a_{1}} P_{b_{1}}}\right) \\
& =\sum_{s *, a_{1}, b_{1}} \sum_{a_{0}, b_{0}}\left|\left\langle a_{1} b_{1} \mid s^{*}\right\rangle\right|^{2}\left|\left\langle a_{0} b_{0}\left|U^{\dagger}(t)\right| s^{*}\right\rangle\right|^{2} P_{a_{1}} P_{b_{1}} \\
& =\sum_{a_{1}, b_{1}} \sum_{s^{*}}\left|\left\langle a_{1} b_{1} \mid s^{*}\right\rangle\right|^{2} P_{a_{1}} P_{b_{1}}=\sum_{a_{1}, b_{1}} P_{a_{1}} P_{b_{1}}=1 .
\end{aligned}
$$

Replacing the reversed path $\Gamma^{*}$ with the forward path $\Gamma$, a similar calculation shows that the initial stochastic mutual information $I_{0}$ satisfies $\left\langle e^{-I_{0}}\right\rangle=1$. The classical component $J_{1}$ of the final stochastic mutual information verifies,

$$
\begin{aligned}
& \left\langle e^{-J_{1}}\right\rangle=\sum_{\Gamma^{*}} P\left[\Gamma^{*}\right] \exp \left(-\ln \frac{P\left(a_{1}, b_{1}\right)}{P_{a_{1}} P_{b_{1}}}\right) \\
& =\sum_{s^{*}, a_{1}, b_{1}} \sum_{a_{0}, b_{0}} P_{s^{*}}\left|\left\langle a_{1} b_{1} \mid s^{*}\right\rangle\right|^{2}\left|\left\langle a_{0} b_{0}\left|U^{\dagger}(t)\right| s^{*}\right\rangle\right|^{2} \frac{P_{a_{1}} P_{b_{1}}}{P\left(a_{1}, b_{1}\right)} \\
& =\sum_{a_{1}, b_{1}} \sum_{s^{*}} P_{s^{*}}\left|\left\langle a_{1} b_{1} \mid s^{*}\right\rangle\right|^{2} \frac{P_{a_{1}} P_{b_{1}}}{P\left(a_{1}, b_{1}\right)}=\sum_{a_{1}, b_{1}} P_{a_{1}} P_{b_{1}}=1 .
\end{aligned}
$$

On the other hand, the calculation for the final stochastic relative entropy of coherence $C_{1}$ reads,

$$
\begin{aligned}
& \left\langle e^{-C_{1}}\right\rangle=\sum_{\Gamma^{*}} P\left[\Gamma^{*}\right] \exp \left(-\ln \frac{P_{s^{*}}}{P\left(a_{1}, b_{1}\right)}\right) \\
& =\sum_{s^{*}, a_{1}, b_{1}} \sum_{a_{0}, b_{0}}\left|\left\langle a_{1} b_{1} \mid s^{*}\right\rangle\right|^{2}\left|\left\langle a_{0} b_{0}\left|U^{\dagger}(t)\right| s^{*}\right\rangle\right|^{2} P\left(a_{1}, b_{1}\right) \\
& =\sum_{a_{1}, b_{1}} \sum_{s^{*}}\left|\left\langle a_{1} b_{1} \mid s^{*}\right\rangle\right|^{2} P\left(a_{1}, b_{1}\right)=\sum_{a_{1}, b_{1}} P\left(a_{1}, b_{1}\right)=1 .
\end{aligned}
$$

As before, the integral fluctuation theorems for the initial stochastic classical mutual information $J_{0}$ and initial stochastic relative entropy coherence $C_{0}$ follow by taking the average over the forward path $\Gamma$.

We next turn to the local stochastic entropy productions, $\Sigma_{A}$ and $\Sigma_{B}$, during the forward process $\Gamma$. We find,

$$
\begin{aligned}
& \left\langle e^{-\Sigma_{A}}\right\rangle=\sum_{\Gamma} P[\Gamma] \exp \left(-\ln \frac{\mathcal{P}_{a_{1}}}{P_{a_{1}}}\right) \\
& =\sum_{s, a_{1}, b_{1}} \sum_{a_{0}, b_{0}} P_{s}\left|\left\langle a_{0} b_{0} \mid s\right\rangle\right|^{2}\left|\left\langle a_{1} b_{1} \mid U(t) \mid s\right\rangle\right|^{2} \frac{P_{a_{1}}}{\mathcal{P}_{a_{1}}} \\
& =\sum_{a_{1}, b_{1}} \sum_{s} P_{s}\left|\left\langle a_{1} b_{1} \mid U(t) \mid s\right\rangle\right|^{2} \frac{P_{a_{1}}}{\mathcal{P}_{a_{1}}}=\sum_{a_{1}} \sum_{b_{1}} \mathcal{P}\left(a_{1}, b_{1}\right) \frac{P_{a_{1}}}{\mathcal{P}_{a_{1}}}=\sum_{a_{1}} P_{a_{1}}=1
\end{aligned}
$$

and

$$
\begin{aligned}
& \left\langle e^{-\Sigma_{B}}\right\rangle=\sum_{\Gamma} P[\Gamma] \exp \left(-\ln \frac{\mathcal{P}_{b_{1}}}{P_{b_{1}}}\right) \\
& =\sum_{s, a_{1}, b_{1}} \sum_{a_{0}, b_{0}} P_{s}\left|\left\langle a_{0} b_{0} \mid s\right\rangle\right|^{2}\left|\left\langle a_{1} b_{1} \mid U(t) \mid s\right\rangle\right|^{2} \frac{P_{b_{1}}}{\mathcal{P}_{b_{1}}} \\
& =\sum_{a_{1}, b_{1}} \sum_{s} P_{s}\left|\left\langle a_{1} b_{1} \mid U(t) \mid s\right\rangle\right|^{2} \frac{P_{b_{1}}}{\mathcal{P}_{b_{1}}}=\sum_{b_{1}} \sum_{a_{1}} \mathcal{P}\left(a_{1}, b_{1}\right) \frac{P_{b_{1}}}{\mathcal{P}_{b_{1}}}=\sum_{b_{1}} P_{b_{1}}=1 .
\end{aligned}
$$

Finally, the stochastic entropy production $\gamma$ satisfies an integral fluctuation theorem when averaging over the forward trajectory $\Gamma$,

$$
\begin{aligned}
\left\langle e^{-\gamma}\right\rangle & =\sum_{\Gamma} P[\Gamma] \exp \left(-\ln \frac{\left.\left|\left\langle a_{0} b_{0}\right| s\right\rangle\right|^{2}\left|\left\langle a_{1} b_{1}\right| U(t)\right| s\right\rangle\left.\right|^{2}}{\left.\left|\left\langle a_{1} b_{1}\right| s^{*}\right\rangle\right|^{2}\left|\left\langle a_{0} b_{0}\right| U^{\dagger}(t)\right| s^{*}\right\rangle\left.\right|^{2}}\right) \\
& =\left(\sum_{s} P_{s}\right)\left(\sum_{a_{1}, b_{1}}\left|\left\langle a_{1} b_{1}\right| s^{*}\right\rangle\right|^{2}\right)\left(\sum_{a_{0}, b_{0}}\left|\left\langle a_{0} b_{0}\right| U^{\dagger}(t)\right| s^{*}\right\rangle\left.\right|^{2}\right)=1
\end{aligned}
$$

# B. DETAILED FLUCTUATION THEOREM 

We next summarize the derivation of the detailed fluctuation theorem (16) of the main text. In order to evaluate the ratio $P_{f}(Q, K, \gamma) / P_{r}(-Q,-K, \bar{\gamma})$, we need to consider that the forward trajectory $\Gamma$ is a function of $\left(s, a_{0}, b_{0}, a_{1}, b_{1}\right)$, while $Q[\Gamma]$ and $K$ and $\gamma$ are all functions of $\left(\Gamma, s^{*}\right)$. We first define,

$$
P_{f}\left(Q, K, \gamma \mid s^{*}\right)=\sum_{\Gamma} \delta(Q-Q[\Gamma]) \delta\left(K-K\left[\Gamma, s^{*}\right]\right) \delta\left(\gamma-\gamma\left[\Gamma, s^{*}\right]\right) P(\Gamma)
$$

which gives the probability of having $(Q, K, \gamma)$ when one starts the reverse process with a vector $\left|s^{*}\right\rangle$. We have,

$$
P_{f}(Q, K, \gamma)=\sum_{s^{*}} P\left(s^{*}\right) P_{f}\left(Q, K, \gamma \mid s^{*}\right)
$$

It then follows that,

$$
\begin{aligned}
P_{f}(Q, K, \gamma) & =\sum_{\Gamma, s^{*}} \delta(Q-Q[\Gamma]) \delta\left(K-K\left[\Gamma, s^{*}\right]\right) \delta\left(\gamma-\gamma\left[\Gamma, s^{*}\right]\right) P(\Gamma) P\left(s^{*}\right) \\
& =e^{Q \Delta \beta-K+\gamma} \sum_{\Gamma^{*}, s} \delta\left(Q+Q\left[\Gamma^{*}\right]\right) \delta\left(K+K\left[\Gamma^{*}, s\right]\right) \delta\left(\gamma-\bar{\gamma}\left[\Gamma^{*}, s\right]\right) P\left(\Gamma^{*}\right) P(s) \\
& =e^{Q \Delta \beta-K+\gamma} \sum_{s} P(s) P(-Q,-K, \bar{\gamma} \mid s)=e^{Q \Delta \beta-K+\gamma} P(-Q,-K, \bar{\gamma})
\end{aligned}
$$

where $\bar{\gamma}\left[\Gamma, s^{*}\right]=-\ln \frac{\left.\left|\left\langle a_{0} b_{0}\right| s\right\rangle\right|^{2}\left|\left\langle a_{1} b_{1}\right| U_{1}^{\dagger}\right| s\right\rangle\left.\right|^{2}}{\left.\left|\left\langle a_{1} b_{1}\right| s^{*}\right\rangle\right|^{2}\left|\left\langle a_{0} b_{0}\right| U_{1}\right| s^{*}\right\rangle\left.\right|^{2}}$.

## C. PATH PROBABILITY FOR THE LOCAL TRAJECTORY

The physics behind expression (6) of the main text for the path probability for the unconditional local trajectory can be made more transparent by introducing a transformation akin to the Choi matrix used in the theory of quantum operations [S1]. We introduce an auxiliary Hilbert space $A^{\prime} B^{\prime}$ and consider

$$
\Omega=\sum_{s} p_{s}|s\rangle\left\langle s\right|_{A B} \otimes|s\rangle\left\langle s\right|_{A^{\prime} B^{\prime}}
$$

We then construct the Choi matrix,

$$
\Lambda(t)=\left(I_{A B} \otimes \mathcal{E}_{A^{\prime} B^{\prime}}\right)(\Omega)
$$

where $\mathcal{E}(\rho)=U(t) \rho U^{\dagger}(t)$. With simple rearrangements, Eq. (6) of the main text may then be written as,

$$
\mathcal{P}\left(a, b, a^{\prime}, b^{\prime}\right)=\left\langle a, b, a^{\prime}, b^{\prime}\right| \Lambda(t)\left|a, b, a^{\prime}, b^{\prime}\right\rangle
$$

which is in the form of a standard quantum mechanical expectation value. Since $\Lambda(t)$ is both Hermitian and positive semi-definite, the probabilities $\mathcal{P}\left(a, b, a^{\prime}, b^{\prime}\right)$ are guaranteed to be positive and normalized.

# D. ANALYTICAL SOLUTION OF THE TWO-QUBIT EXAMPLE 

In this section, we provide the analytical solution for the two-spin example presented in the main text. For $\alpha=0$ the global initial state is $\rho_{A B}(0)=\operatorname{diag}\left(1, e^{-\beta_{B}}, e^{-\beta_{A}}, e^{-\beta_{A}-\beta_{B}}\right) /\left(Z_{A} Z_{B}\right)$ where the diagonal is with respect to the $\sigma_{z} \otimes \sigma_{z}$ basis. From Eq. (7) in the main text, the probability $P_{f}(Q)$ is given in this case by $P_{\Gamma}(Q)=$ $\sum_{b, b^{\prime}} \delta(Q-\Delta E) \mathcal{P}(a, b)\left|\left\langle a^{\prime}, b^{\prime}\right| U_{t}|a b\right\rangle\left.\right|^{2}$. Under the action of the unitary $U_{t}=e^{-i t H_{\text {int }}}$, the basis changes as follows,

$$
\begin{aligned}
& U|00\rangle=|00\rangle \\
& U|01\rangle=\cos \left(t \frac{\pi}{2 \tau}\right)|01\rangle-i \sin \left(t \frac{\pi}{2 \tau}\right)|10\rangle \\
& U|10\rangle=-i \sin \left(t \frac{\pi}{2 \tau}\right)|01\rangle+\cos \left(t \frac{\pi}{2 \tau}\right)|10\rangle \\
& U|11\rangle=|11\rangle
\end{aligned}
$$

Since initially the system $A$ is colder than system $B, Q=+Q_{A}$ when $|01\rangle \rightarrow|10\rangle$ and $Q=-Q_{A}$ when $|10\rangle \rightarrow|01\rangle$. We have, therefore,

$$
\begin{aligned}
P_{f}\left(Q=+Q_{A}\right) & =\mathcal{P}(0,1)\left|\langle 10| U_{t}|01\rangle\right|^{2}=\frac{e^{-\beta_{B}}}{Z_{A} Z_{B}} \sin ^{2}\left(t \frac{\pi}{2 \tau}\right) \\
P_{f}\left(Q=-Q_{A}\right) & =\mathcal{P}(1,0)\left|\langle 01| U_{t}|10\rangle\right|^{2}=\frac{e^{-\beta_{A}}}{Z_{A} Z_{B}} \sin ^{2}\left(t \frac{\pi}{2 \tau}\right) \\
P_{f}(Q=0) & =\sum a, b \mathcal{P}(a, b)\left|\langle a b| U_{t}|a b\rangle\right|^{2}=\frac{1+e^{-\beta_{A}-\beta_{B}}}{Z_{A} Z_{B}}+\frac{e^{-\beta_{A}}+e^{-\beta_{B}}}{Z_{A} Z_{B}} \cos ^{2}\left(t \frac{\pi}{2 \tau}\right)
\end{aligned}
$$

For the reversed path $\Gamma^{*}$, the replacement $U_{t} \rightarrow U_{t}^{\dagger}$ implies the replacement $t \rightarrow-t$. In the uncorrelated case, this has no effect on the heat distribution and we have accordingly $P_{f}(Q)=P_{r}(Q)$.

On the other hand, in the correlated case when $\alpha=-i \exp \left[-\left(\beta_{A}+\beta_{B}\right) / 2\right] / Z_{A} Z_{B}$, the initial state reads,

$$
\rho_{A B}(0)=\frac{1}{Z_{A} Z_{B}}|00\rangle\langle 00|+\frac{e^{-\beta_{A}}+e^{-\beta_{B}}}{Z_{A} Z_{B}}|\phi\rangle\langle\phi|+\frac{e^{-\beta_{A}-\beta_{B}}}{Z_{A} Z_{B}}|11\rangle\langle 11|
$$

with $|\phi\rangle=\left(e^{-\frac{\beta_{A}}{2}}|01\rangle+i e^{-\frac{\beta_{A}}{2}}|10\rangle\right) / \sqrt{e^{-\beta_{A}}+e^{-\beta_{B}}}$.
We have again, $Q=+Q_{A}$ when $|01\rangle \rightarrow|10\rangle$ and $Q=-Q_{A}$ when $|10\rangle \rightarrow|01\rangle$. As a result,

$$
\begin{aligned}
P_{f}\left(Q=+Q_{A}\right)= & \mathcal{P}(\phi)\left|\langle 01 \mid \phi\rangle\right|^{2}\left|\langle 10| U_{t} \mid \phi\rangle\right|^{2}=\frac{e^{-\beta_{B}}}{Z_{A} Z_{B}} \frac{\left[e^{-\frac{\beta_{A}}{2}} \cos \left(t \frac{\pi}{2 \tau}\right)-e^{-\frac{\beta_{B}}{2}} \sin \left(t \frac{\pi}{2 \tau}\right)\right]^{2}}{e^{-\beta_{A}}+e^{-\beta_{B}}} \\
P_{f}\left(Q=-Q_{A}\right)= & \mathcal{P}(\phi)\left|\langle 10 \mid \phi\rangle\right|^{2}\left|\langle 01| U_{t} \mid \phi\rangle\right|^{2}=\frac{e^{-\beta_{A}}}{Z_{A} Z_{B}} \frac{\left[e^{-\frac{\beta_{B}}{2}} \cos \left(t \frac{\pi}{2 \tau}\right)+e^{-\frac{\beta_{A}}{2}} \sin \left(t \frac{\pi}{2 \tau}\right)\right]^{2}}{e^{-\beta_{A}}+e^{-\beta_{B}}} \\
P_{f}(Q=0)= & \mathcal{P}(0,0)+\mathcal{P}(1,1)+\mathcal{P}(\phi)\left(|\langle 01 \mid \phi\rangle|^{2}\left|\langle 01| U_{t} \mid \phi\rangle\right|^{2}+\left|\langle 10 \mid \phi\rangle\right|^{2}\left|\langle 10| U_{t} \mid \phi\rangle\right|^{2}\right) \\
= & \frac{1+e^{-\beta_{A}-\beta_{B}}}{Z_{A} Z_{B}}+\frac{e^{-\beta_{A}}}{Z_{A} Z_{B}} \frac{\left[e^{-\frac{\beta_{A}}{2}} \cos \left(t \frac{\pi}{2 \tau}\right)-e^{-\frac{\beta_{B}}{2}} \sin \left(t \frac{\pi}{2 \tau}\right)\right]^{2}}{e^{-\beta_{A}}+e^{-\beta_{B}}}
\end{aligned}
$$

In general, except for $t=(0, \tau), P_{f}(Q) \neq P_{r}(Q)$.
[S1] M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information, (Cambridge University Press, Cambridge, 2000).