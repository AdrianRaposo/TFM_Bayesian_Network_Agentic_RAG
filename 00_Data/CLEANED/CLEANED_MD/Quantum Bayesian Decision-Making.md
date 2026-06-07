# Quantum Bayesian Decision-Making 

Michael de Oliveira ${ }^{1} \cdot$ Luis Soares Barbosa ${ }^{1}$<br>(c) The Author(s), under exclusive licence to Springer Nature B.V. 2021


#### Abstract

As a compact representation of joint probability distributions over a dependence graph of random variables, and a tool for modelling and reasoning in the presence of uncertainty, Bayesian networks are of great importance for artificial intelligence to combine domain knowledge, capture causal relationships, or learn from incomplete datasets. Known as a NP-hard problem in a classical setting, Bayesian inference pops up as a class of algorithms worth to explore in a quantum framework. This paper explores such a research direction and improves on previous proposals by a judicious use of the utility function in an entangled configuration. It proposes a completely quantum mechanical decision-making process with a proven computational advantage. A prototype implementation in Qiskit (a Pythonbased program development kit for the IBM Q machine) is discussed as a proof-of-concept.


Keywords Bayesian inference $\cdot$ Quantum algorithms $\cdot$ Quantum decision making

## 1 Motivation

Bayesian reasoning is widely used in machine learning and data science, as a powerful framework for probabilistic analysis, applications ranging from learning processes (Neal 1996) to pragmatic representations (Li et al. 2018). Broadly speaking, machine learning algorithms are able to learn from data, with the purpose of performing some tasks, without requiring explicit programming; in a sense outcomes are directly built by the sampled data. However, the current rate of data creation is almost exponential Al-Jarrah et al. (2015) (going, for example, from 3.5 million text messages per minute in 2016, to

[^0]
[^0]:    This work is financed by the ERDF-European Regional Development Fund through the Operational Programme for Competitiveness and Internationalisation-COMPETE 2020 Programme and by National Funds through the Portuguese funding agency, FCT, within project POCI-01-0145-FEDER-030947. The first author was further supported by project NORTE-01-0145-FEDER-000037, funded by Norte Portugal Regional Operational Programme (NORTE 2020), under the PORTUGAL 2020 Partnership Agreement.

    Michael de Oliveira
    michaeldeoliveira@live.com.pt
    Luis Soares Barbosa
    lsb@di.uminho.pt
    1 INL - Quantum Software Engineering, Universidade do Minho, Braga, Portugal

over 15 million in 2017), a fact that calls for radically new approaches and, most probably, new computational models and hardware to effectively deal with such numbers.

Can quantum computing bring some useful contribution to this state of affairs? On the one hand it is well known that building very large quantum-addressable classical memories is technologically very demanding, and will not be available soon. On the other, at least from a theoretical point of view, the question seems worth to discuss. Actually, even at its present, quite preliminar stage of development, quantum computing allows for a variety of speed ups with respect to classical algorithmic counterparts in e.g. information storage (Giovannetti et al. 2008), pattern recognition (Biamonte et al. 2016), and matrix inversion, the latter being a basic ingredient of several machine learning algorithms (Harrow et al. 2009). As a matter of fact, quantum algorithms, as the ones discussed in this paper, suggest radically different ways to approach old problems and to explore complexity boundaries. For example, to know whether for a concrete problem, as the size of the input parameter grows, one may asymptotically go faster with the use of a quantum memory than with purely classical states, is a question underlying many interesting problems from big-data to optimisation, or molecular synthesis.

The synergies between research lines in quantum technologies and Bayesian inference, in particular, seem promising. In one direction, a quantum processor can be expressed and studied as a Bayesian Network (Sakkaris 2016). In the reverse one, quantum mechanics can describe naturally probabilistic systems in physical terms. Reference (Mansinghka 2009), for example, describes very promising improvements on the implementation of approximate Bayesian inference routines resorting to physical stochastic logic gates building up hardware implementations of sampling algorithms. Quantum processors are, in a sense, part of such a family.

This paper is a step in this direction. Our starting point is a quantum version of a Bayesian inference algorithm introduced by Low et al. (2014) based on a square-root quantum speedup to rejection sampling on a Bayesian network, which avoids the use of an oracle. Note that an oracle-based version appeared previously in Ozols et al. (2013). This approach, revisited in Sect. 3, was implemented by us on Qiskit-the IBM opensource platform for quantum computing. Our main contribution, presented in Sect. 4, extends Low et al. algorithm to a decision-making setting: this incorporates an utility function which is applied before any observation of the quantum state which encodes the Bayesian network. The computational effort for the proposed solution and a simpler quantum solution are determined in Sect. 5. A proof-of-concept implementation Qiskit is discussed in Sect. 6. Finally, Sect. 7 concludes and points out a number of issues for future work. A background section-Sect.2-recalls the Bayesian inference problem and provides a brief overview of the basic intuitions underlying decision making.

# 2 Background 

### 2.1 Bayesian Inference

Bayesian inference is used to update the posterior probability distribution of some query variables given the value of the observed variables, also known as evidence variables (Russel and Norvig 2010). The conditional probability is given by

![img-0.jpeg](img-0.jpeg)

Fig. 1 Bayesian network over 5 variables

$$
P(A \mid B)=\frac{P(A, B)}{P(B)}
$$

These joint probabilities can be stored in a distribution table, but note that the dimension of the latter grows exponentially with the number of variables. This means that for most applications the table would be too large to be stored computationally. Alternatively, Bayesian networks, as in Fig. 1, allow for a compact representation of joint probability distributions (Darwiche 2008) as a directed acyclic graph structure. The advantage is that the space complexity of the representation can be made much smaller than in the general case, by exploiting conditional dependencies in the distribution, through the association to each graph node of a conditional probability table for each random variable, with directed edges representing conditional dependencies. For this reason, they are largely used in industrial applications. However, inference via a Bayesian Networks is still a NP-problem. Figure 1 depicts a toy Bayesian network relating a few variables encoding different sorts of activities and the possibility of a lung cancer diagnosis.

# 2.1.1 Inference 

Algorithms that infer over a Bayesian network compute joint probabilities using the following equation:

$$
P\left(x_{1}, \ldots, x_{n}\right)=\prod_{i=1}^{n} P\left(x_{i} \mid \operatorname{Parents}(X i)\right)
$$

The computational effort to determine this value is low because the number of values selected is linearly bounded by the number of variables. The envisaged joint probability, however, may not be defined for all variables. If such is the case, it is necessary to sum out over all undefined variables as in

$$
P\left(X_{1} \mid x_{2}, x_{3}\right)=\sum_{x_{4}} \sum_{x_{5}} P\left(X_{1}, x_{2}, x_{3}, x_{4}, x_{5}\right)
$$

Consequently, the number of values to sum out grows exponentially with the number of undefined variables. A well known algorithm for variable elimination algorithm works exactly in this way. Approximate algorithms, treading off consumption of computational resources for precision, are typically used to tackle this problem. Solutions are found faster

but may not be precise. The literature documents a bunch of approximate algorithms. In this paper we will focus on rejection sampling because the first part of the quantum inference algorithm discussed in the next section is a quantum analog to it. Rejection sampling is a popular method first systematised by von Neumann (1951), who curiously enough also developed the Hilbert space formalization of quantum mechanics and its logic.

Rejection sampling generates samples resorting to the probability distributions defined by the conditional probability tables as depicted in Fig. 1. The consequence of this generation process is that a certain configuration of values for the variables is only sampled with the associated probability:

$$
P\left(\text { Sample }<X_{1}=\text { true }, X_{2}=\text { false }>\right)=P\left(X_{1}=\text { true }, X_{2}=\text { false }\right)
$$

Under those circumstances, a conditional probability can be determined by:

$$
P\left(X_{1}=\operatorname{true} \mid X_{2}=\text { false }\right) \approx \frac{\# \operatorname{Samples}\left(X_{1}=\text { true }, X_{2}=\text { false }\right)}{\# \operatorname{Samples}\left(X_{2}=\text { false }\right)}
$$

Clearly, the precision of the query grows with the number of useful samples (\#Samples). It is important to notice that not all samples are useful since samples with different values for the evidence variables are not used.

# 2.1.2 Bayesian Networks for Decision Making 

Bayesian networks are equipped with an utility function in order to support decision-making processes. Its purpose is to quantify the utility of possible outcomes. The expected utility $(E U)$ of an outcome is the product of its probability and the associated utility value. Formally, to find the expected utility of some action $a$, one computes

$$
E U(a \mid e)=\sum_{r} P(\text { Result }=r \mid a, e) * U(r)
$$

If the $E U$ values of all feasible actions is known, it is possible to choose the 'best', or more profitable, one:

$$
\text { action }=\operatorname{argmax}_{a} E U(a \mid e)
$$

This is indeed the maximum expected utility principle; a rational entity is expected to choose the action with the greatest expected utility with respect to her set of beliefs (Russel and Norvig 2010).

The previous principle describes many algorithms and solutions used in artificial intelligence. For example, in reinforcement learning a great number of agents and robots are built on a process that attempts to find the optimal policy. This works with an instance of a Bayesian network (Markov decision process) and a more complex utility function (the so-called discounted reward function), where the agent also accounts for future rewards $\left(R\left(S_{t}\right)\right)$, which are reachable from the starting state. Further, it values present rewards over future rewards with the use of a discount factor $\gamma^{t}$.

$$
U_{\#}(s)=E\left[\sum_{t=0}^{\infty} \gamma^{t} R\left(S_{t}\right)\right]
$$

![img-1.jpeg](img-1.jpeg)

Fig. 2 Encoding circuit

Therefore, any algorithm that computes the best decision by Eqs. (6) and (7) has the potential to be applied to all other instances derived from the principal one, as a consequence of having the same computational pattern.

# 3 Quantum Bayesian Inference 

In brief, a quantum algorithm can be regarded as a targeted manipulation of a quantum state (realised as an assembly of qubits) with a subsequent measurement to retrieve relevant information. States are represented by column vectors of complex numbers whose sum of moduli squared is 1 , often represented in the so-called Dirac notation (Nielsen and Chuang 2010) as $|\Psi\rangle$. Typically, they correspond to linear combinations of basis states affected by complex coeficients, as in, for example, Eq. (9). The dynamics of a quantum system is represented by (the multiplication of the quantum state by) unitary matrices and is therefore reversible in time, as long as no measurement is involved. The reversal corresponds simply to a composition with the adjoint of the unitary matrix that represents forward evolution. Such an evolution can be expressed as a sequence of only a few elementary transformations represented as quantum gates, which only act on one or two qubits at a time. Therefore, quantum algorithms are widely formulated as circuits built of these elementary gates, as depicted, for example, in Fig 2.

A quantum algorithm for inference on Bayesian networks was introduced by Low et al. (2014), which, as mentioned above, is based on an improved quantum version of the Rejection Sampling algorithm. This algorithm is able to generate samples quadratically faster than the classical version, provided that the network is not too densely connected. The algorithm is divided into 3 stages, detailed in the sequel.

In the first stage, the Bayesian network is encoded into a quantum state. For this, a binary variable can be represented by a single qubit and the probabilities are mapped to the coefficients of the quantum state:

$$
$$

with the corresponding density matrix (Barnett 2009),

$$
\rho_{\Psi}=|\Psi\rangle\langle\Psi|=\left(\begin{array}{cc}
\alpha^{2} & \alpha * \beta \\
\alpha * \beta & \beta^{2}
\end{array}\right)
$$

Whenever two variables share an edge in the network they are related, and therefore not independent from each other, such a relationship is expressed through state entanglement. Entanglement represents a strong correlation between quantum states, therefore expressing shared information between different elements. The envisaged state is achieved though the application of a specific sort of gates-controlled rotations-to the state qubits. The fact that a rotation is controlled by another qubit permits the creation of entanglement between them. The amplitude of the rotation defines the value of the coefficients. For instance, a circuit that encodes the Bayesian network in Fig. 1 is represented in Fig 2.

The whole quantum state is equivalent to a superposition of all on entries of the original joint probability distribution table:

$$
\begin{aligned}
\left|\Psi^{\prime}\right\rangle= & \gamma_{1}^{2}\left|\operatorname{Var}_{1}=\text { true, } \operatorname{Var}_{2}=\text { true, } \ldots\right\rangle+\gamma_{2}^{2}\left|\operatorname{Var}_{1}=\text { true, } \operatorname{Var}_{2}=\text { false, } \ldots\right\rangle \\
& +\gamma_{3}^{2}\left|\operatorname{Var}_{1}=\text { false }, \operatorname{Var}_{2}=\text { true }, .\right\rangle+\gamma_{4}^{2}\left|\operatorname{Var}_{1}=\text { false }, \operatorname{Var}_{2}=\text { false }, \ldots\right\rangle \\
& +\cdots
\end{aligned}
$$

Afterward, a measurement ${ }^{1}$ to this state produces a sample, as in the Rejection Sampling algorithm, as the probability of each sample is the same as the one in the distribution:

$$
\begin{aligned}
& P\left(\operatorname{Var}_{1}=\text { true }, \operatorname{Var}_{2}=\text { true }, \ldots\right)=\operatorname{Tr}\left(P_{0} * \rho_{\Psi^{\prime}}\right) \\
& \quad=\left(\begin{array}{cccc}
1 & 0 & \cdots & 0 \\
0 & 0 & \cdots & 0 \\
\vdots & \vdots & \ddots & \cdots \\
0 & 0 & \cdots & 0
\end{array}\right) *\left(\begin{array}{cccc}
\gamma_{1}^{2} & \cdots & \cdots & \cdots \\
\cdots & \gamma_{2}^{2} & \cdots & \cdots \\
\cdots & \cdots & \ddots & \cdots \\
\cdots & \cdots & \cdots & \gamma_{n}^{2}
\end{array}\right)=\gamma_{1}^{2} * 1+\gamma_{2}^{2} * 0+\cdots+\gamma_{n}^{2} * 0=\gamma_{1}^{2}
\end{aligned}
$$

At this point, a quantum analog to Rejection Sampling is created. However, it is not an efficient way to do inference because every time we measure the state it collapses, and it is necessary to reconstruct the state entailing the need for a subsequent reconstruction.

In a second stage, the Amplitude Amplification algorithm (Brassard et al. 2000) is applied to amplify the states that have the right values for the evidence variable. It allows for a square root speed up in search problems, a fact that explains its relevance and ubiquity to many quantum programs. In our case, the quantum state that encodes the Bayesian network is divided into two orthogonal states, one where the evidence variables have the right value and another state where they lack it:

$$
\begin{aligned}
\left|\Psi_{\text {init }}\right\rangle= & \sqrt{P(e)}\left|\operatorname{Var}_{1}, \operatorname{Var}_{2}, \ldots, \text { evidences }\right\rangle \\
& +\sqrt{1-P(e)}\left|\operatorname{Var}_{1}, \operatorname{Var}_{2}, \ldots, \neg \text { evidences }\right\rangle
\end{aligned}
$$

Next, the amplitude amplification algorithm is applied to search for the state that has the right values for the evidence variables (Brassard et al. 2000).

[^0]
[^0]:    ${ }^{1}$ Notice, that the use of the density matrix notation with projectors is equivalent to the description of the measurement in the Dirac notation:

    $$
    \left\langle\operatorname{Var}_{1}=\text { true, } \operatorname{Var}_{2}=\text { true }, \ldots \mid \Psi^{\prime}\right\rangle \equiv \operatorname{Tr}\left(P_{0} * \rho_{\Psi^{\prime}}\right)
    $$

    The matrix density notation was not required, as we are not dealing with mixed quantum states. However, it helped, later on, to expose the main ideas more clearly.

Table 1 Classical versus quantum complexity


$$
\begin{aligned}
Q^{k} *\left|\Psi_{\text {init }}\right\rangle= & \cos \left(\frac{2 k+1}{2} * \theta\right)\left|\operatorname{Var}_{1}, \operatorname{Var}_{2}, \ldots, \text { evidences }\right\rangle \\
& +\sin \left(\frac{2 k+1}{2} * \theta\right)\left|\operatorname{Var}_{1}, \operatorname{Var}_{2}, \ldots, \neg e v i d e n c e s\right\rangle
\end{aligned}
$$

where $Q$ represent the operator that amplifies the selected elements, $k$ the number of iterations, and $\theta$ the initial probabilities,

$$
\theta=2 \sin ^{-1}(\sqrt{P(e)}) \quad \wedge \quad \theta=2 \cos ^{-1}(\sqrt{1-P(e)})
$$

then for the right number of iteration $\left(k^{\prime}\right)$, the final quantum state approximates with great probability to the pretended state,

$$
Q^{k^{\prime}} *\left|\Psi_{\text {init }}\right\rangle=\left|\Psi_{\text {final }}\right\rangle \approx\left|\operatorname{Var}_{1}, \operatorname{Var}_{2}, \ldots, \text { evidences }\right\rangle
$$

The last stage amounts simply to observe this state and use the result as a sample. In Table 1 we can see the comparison between the classical and the quantum versions. The latter exhibits a quadratic speed up but only if the Bayesian network is not too densely connected, meaning that $m$ the number of edges between the nodes $(n)$ is not to large. Otherwise the price of encoding it to a quantum state will be too high, as the corresponding term grows exponentially.

# 4 Quantum Decision-Making 

Clearly, a quantum computer could be used to work out the conditional probabilities with a quadratic speed up for decision problems, according to Eq. (16).

$$
E U(a \mid e)=\sum_{r} \underbrace{P(\text { Result }=r \mid a, e)}_{\text {Quantum }} * \underbrace{U(r)}_{\text {Classical }}
$$

In this section, however, we would like to propose a different approach which, in principle, will increase the advantage of having the quantum resources. The idea is quite simple: Instead of sampling the conditional probabilities, the quantum state remains unobserved until the utility function is applied. The intention is to apply a transformation to the outcome variable and look to what happens to the action variable. As both the outcome and the action variables are entangled, a transformation applied to the former will produce an effect on the latter.

The new algorithm modifies the process described in the previous section to infer a conditional probability by preventing the action variable to be used as an evidence variable. Thus, after an application of the amplitude amplification algorithm and tracing out the nonevidence variables $(N E)$, as nothing happens to them during the proposed process, we have,

$$
\begin{aligned}
\operatorname{tr}_{N E}\left(Q_{\text {Search }_{1}} \mid \Psi_{\text {init }}\right)\right)= & \left|\Psi_{A, R}\right\rangle=\gamma_{a, r} \mid a, r, \text { evidences }\rangle+\gamma_{a, \neg r} \mid a, \neg r, \text { evidences }\rangle \\
& +\gamma_{\neg a, r} \mid \neg a, r, \text { evidences }\rangle+\gamma_{\neg a, \neg r} \mid \neg a, \neg r, \text { evidences }\rangle
\end{aligned}
$$

or, equivalently,

$$
\left|\Psi_{A, R}\right\rangle=\left(\begin{array}{l}
\gamma_{a, r} \\
\gamma_{a, \neg r} \\
\gamma_{\neg a, r} \\
\gamma_{\neg a, \neg r}
\end{array}\right)
$$

describing only the states of the featured variables. The utility function $U(r)$ is then applied to this state $\left(\left|\Psi_{A, R}\right\rangle\right)$. Therefore, a quantum state $\left|\Psi_{U}\right\rangle$ isomorphic to the utility function will be created:

$$
U(R)=\left\{\begin{array}{l}
U(r) \\
U(\neg r) \rightarrow\left|\Psi_{U}\right\rangle=
\end{array} \frac{\sqrt{U(r)}}{\frac{n}{\sqrt{U(\neg r)}} \frac{n}{\sqrt{}}}
\right.
$$

where $n$ is a normalization term such that $\left\langle\Psi_{A, R} \mid \Psi_{A, R}\right\rangle$ sums up to 1 . Also, by creating both states in memory, the whole product state $\left|\Psi_{A, R}\right\rangle \otimes\left|\Psi_{U}\right\rangle$ becomes,

$$
\left|\Psi_{S y t}\right\rangle=\left|\Psi_{A, R}\right\rangle \otimes\left|\Psi_{U}\right\rangle=\left(\begin{array}{l}
\gamma_{a, r} \\
\gamma_{a, \neg r} \\
\gamma_{\neg a, r} \\
\gamma_{\neg a, \neg r}
\end{array}\right) \otimes\left(\begin{array}{l}
\frac{\sqrt{U(r)}}{\frac{n}{\sqrt{U(\neg r)}}}
\end{array}\right)=\left(\begin{array}{l}
\gamma_{a, r} * \frac{\sqrt{U(r)}}{\frac{n}{\sqrt{U(\neg r)}} \\
\gamma_{a, r} * \frac{\sqrt{U(\neg r)}}{\frac{n}{\sqrt{U(r)}}} \\
\gamma_{\neg a, r} * \frac{\sqrt{n}}{\sqrt{U(\neg r)}} \\
\gamma_{\neg a, r} * \frac{\sqrt{n}}{\frac{n}{\sqrt{U(r)}} \\
\gamma_{\neg a, \neg r} * \frac{\sqrt{n}}{\frac{n}{\sqrt{U(\neg r)}}}
\end{array}\right)
$$

Then, this state $\left|\Psi_{S y t}\right\rangle$ already contains the relevant terms where the Utility function is applied to the correct bases. All one has to do is to amplify them resorting again to amplitude amplification algorithm. For the example at hands, such is the case when $r \wedge r$ and $\neg r \wedge \neg r$ hold, yielding,

$$
Q_{\text {Search }_{2}}\left|\Psi_{S y t}\right\rangle \approx\left(\begin{array}{c}
\frac{\gamma_{a, r} * \sqrt{U(r)}}{n^{\prime}} \\
0 \\
0 \\
\gamma_{a, \neg r} * \sqrt{U(\neg r)} \\
\frac{\gamma_{\neg a, r} * \sqrt{U(r)}}{\gamma_{\neg a, r} * \sqrt{U(r)}} \\
\frac{n^{\prime}}{0} \\
0 \\
\frac{\gamma_{\neg a, \neg r} * \sqrt{U(\neg r)}}{n^{\prime}}
\end{array}\right)
$$

At this moment the amplitudes of the action variable hold the solution to the decision problem. To understand how the Results variable and the Utility function are traced out as follows,

$$
\begin{aligned}
\rho_{A} & =\operatorname{tr}_{R, U}\left(\rho_{S y t}\right) \\
& =\left(\left(\frac{\gamma_{a, r} * \sqrt{U(r)}+\gamma_{a, \neg r} * \sqrt{U(\neg r)}}{n^{\prime}}\right)^{2} \quad \cdots\right. \\
& \left.\quad \cdots \quad\left(\frac{\gamma_{\neg a, r} * \sqrt{U(r)}+\gamma_{\neg a, \neg r} * \sqrt{U(\neg r)}}{n^{\prime}}\right)^{2}\right)
\end{aligned}
$$

A measurement yields,

$$
P\left(a^{\prime}\right)=\operatorname{tr}\left(P_{0} * \rho_{S y t}\right)=\left(\begin{array}{ll}
1 & 0 \\
0 & 0
\end{array}\right) * \rho_{S y t}=\left(\frac{\gamma_{a, r} * \sqrt{U(r)}+\gamma_{a, \neg r} * \sqrt{U(\neg r)}}{n^{\prime}}\right)^{2}
$$

and,

$$
P\left(\neg a^{\prime}\right)=\operatorname{tr}\left(P_{1} * \rho_{S y t}\right)=\left(\begin{array}{ll}
0 & 0 \\
0 & 1
\end{array}\right) * \rho_{S y t}=\left(\frac{\gamma_{\neg a, r} * \sqrt{U(r)}+\gamma_{\neg a, \neg r} * \sqrt{U(\neg r)}}{n^{\prime}}\right)^{2}
$$

Combining the deduced probability of the action variable with,

$$
\gamma_{a, r}^{2}=P(a, r, \text { evidences })
$$

and

$$
P(r \mid a, \text { evidences })=\frac{P(a, r, \text { evidences })}{P(a, \text { evidences })}
$$

we conclude that

$$
\gamma_{a, r}^{2} \propto P(r \mid a, \text { evidences })
$$

and the transformation yields a state where

![img-2.jpeg](img-2.jpeg)

Fig. 3 Probability distribution of an action variable

$$
P\left(a_{i}^{\prime}\right)=\operatorname{tr}\left(P_{i} * \rho_{S y t}\right)=\frac{\gamma_{a_{i}, r_{1}}^{2} * U\left(r_{1}\right)+\gamma_{a_{i}, r_{2}}^{2} * U\left(r_{2}\right)+\cdots+\gamma_{a_{i}, r_{n}}^{2} * U\left(r_{n}\right)}{n^{\prime 2}}
$$

So, after applying there transformations the probability of some action $\left(a_{i}\right)$ is proportional to its expected utility [Eq. 6],

$$
\begin{gathered}
P\left(a_{i}^{\prime}\right) \propto E U\left(a_{i} \mid e\right) \\
P\left(a_{i}^{\prime}\right)=\varrho_{a_{i}} * E U\left(a_{i} \mid e\right)
\end{gathered}
$$

Finally, if initially the Bayesian networks respects,

$$
P(a \mid \text { evidences })=P(a)
$$

then

$$
P(r \mid a, \text { evidences })=\frac{P(r, a \mid \text { evidences })}{P(a)}
$$

and

$$
P\left(a_{i^{\prime}}\right)=P\left(a_{i}\right), i \neq i^{\prime}
$$

The constant of proportionality takes the following value for all actions:

$$
\varrho_{i^{\prime}}=\varrho_{i}=\frac{1}{n^{\prime 2} * P(a)}, \quad i \neq i^{\prime}
$$

Thus, the values of the proportionality constants $\varrho_{i}$ between all the Expected Utilities remain the same. This means that an action with a greater probability has a greater expected utility. Consequently, to choose the action with the greatest probability/utility (Fig. 3), it is enough to resort to a limited collection of samples, rather than obtaining first all the conditional probabilities. Moreover, this provides a more precise way of choosing an action because the sampling method always yields an approximation and the error affecting the computed values grows for every conditional probability determined.

![img-3.jpeg](img-3.jpeg)

Fig. 4 Bayesian network with an independent action node

Remember, that this decision process requires that Eq. (32) has to be initially true. This expresses the rational choice which considers all actions as equal at the beginning. In other words, the intelligent agent is not biased beforehand. Additionally, the action variable should be independent of the evidence variables as in Eq. (30), which means that the topology of the network has to be as in Fig. 4. This requirement ensures that the intelligent agent is not biased by the current state of his environment and performs his decisions in order to achieve the best outcome in the future state.

# 5 Complexity 

The purpose of this Section is to characterize computational complexity of the proposed algorithm and compare it to the solution that computes the conditional probabilities with use of the quantum inference algorithm (Eq. (16)). So, to simplify let us denote by Process A the new quantum algorithm and by Process B the second one.

Both algorithms generate samples to determine which is the best action. The number of operations $\left(I_{t}\right)$ in each algorithm is defined by the number of iterations per sample $\left(I_{s}\right)$ and the number of samples $(S)$ necessary, as in Eq. (34).

$$
I_{t}=S * I_{s}
$$

### 5.1 Number of Iterations

The number of iterations per sample of the two processes are defined by the number of Search iterations that are necessary to apply in each case. Also, the number of iterations necessary to find the goal state in a quantum search is defined by the probability of this state:

$$
I_{s}=\sqrt{\frac{1}{P(\text { state })}}
$$

For Process A, this is the probability of the state which has already the utility function applied to it,

$$
P(\text { state })=\sum_{r} U(r) * P(r, e)
$$

knowing that,

$$
1=\sum_{r} U(r)
$$

Assuming that any distribution is possible for $\mathrm{U}(\mathrm{r})$ and $\mathrm{P}(\mathrm{r}, \mathrm{e})$, we conclude that the probability can take any value between 0 and $\mathrm{P}(\mathrm{e})$. We also know that the mean value for $U(r)$ is:

$$
\frac{1}{N_{r}}
$$

where $N_{r}$ represents the dimension of the outcome variable. Thus, $\mathrm{P}(\mathrm{e}, \mathrm{r})$ can be described as:

$$
\frac{P(e)}{N_{r}}
$$

So the mean value for the product of the two values $U(r) * P(e, r)$ will be,

$$
\frac{P(e)}{N_{r}} * \frac{1}{N_{r}}=\frac{P(e)}{N_{r}^{2}}
$$

if they are independent, which is the case because the utility function is independent of the information present in the Bayesian Network. The mean value for the sum can be computed by the sum over the mean terms

$$
\operatorname{Mean}(P(\text { state }))=\sum_{r} \frac{P(e)}{N_{r}^{2}}=\frac{P(e) * N_{r}}{N_{r}^{2}}=\frac{P(e)}{N_{r}}
$$

This mean value for the probability will be used to define the number of steps:

$$
I_{s}=\sqrt{\frac{N_{r}}{P(e)}}
$$

defining in this way the number of iterations necessary to obtain a sample with Process A.
The same has to be done for Process B, where the probabilty of the goal state is

$$
P(\text { state })=P(e, a)
$$

In this case, we have to apply the requirements determined by Process A described in (30) and (32) in order to make a correct comparison at a later stage,

$$
P(e, a)=P(e) * P(a)=\frac{P(e)}{N_{a}}
$$

where $N_{a}$ is the dimension of the action variable. Finally, we estimate the number of iterations as

Fig. 5 Chi-square distributions with different degrees of freedom $(k)$
![img-4.jpeg](img-4.jpeg)

$$
I_{s}=\sqrt{\frac{N_{a}}{P(e)}}
$$

# 5.1.1 Number of Samples 

The next step is to obtain the number of samples necessary for each process. Recall that the simultaneous error terms for a Multinomial Distribution are:

$$
\left(p i-\pi_{i}\right)^{2}=\frac{A * \pi_{i}\left(1-\pi_{i}\right)}{N}, \quad(i=1,2, \ldots, k)
$$

The value A represents the upper $\alpha * 100$ th percentile of a Chi-Square Distribution (Fig. 5) with $\mathrm{k}-1$ degrees of freedom, $\pi_{i}$ represent the probability of category $\mathrm{i}, N$ is the number of samples, and the difference on the left side of the equation represents the error term (Goodman 1965).

Writing the same equation as a function of $N$, yields

$$
N=\frac{A * \pi_{i}\left(1-\pi_{i}\right)}{\delta^{2}},(i=1,2, \ldots, k)
$$

Equation (47), defines the number of samples necessary for Process A and Process B, since, both processes are sampling from a quantum state with multiple bases.

### 5.1.2 Total Number of Operations

The total number of operations is characterized by the product of the terms deduced in the previous sections and the number of operations necessary to encode the network as a quantum state. Additionally, Process B requires at least $2\left(N_{a}+N_{r}\right)$ operations to apply the Utility function and sum the respective terms for the expected utilities. Finally, the total number of operations for each process to solve the decision problem is shown in Table 2.

When the decision problem is totally defined all that it requires is to plug the number in the equation and look which process performs better. However, a comparison was

Table 2 Mean number of operations for each process


performed (as described in Appendix) and the relation between the computational effort is asymptotically over the term,

$$
\frac{\text { Process } B}{\text { ProcessA }} \geq \sqrt{\frac{N_{r}}{N_{a}}}
$$

This result shows that Process A is faster when the outcome variable has a greater dimension than the action variable. This is a quite normal scenario in real applications because the number of states in which an agent can transit is tremendously smaller than the possible states that his environment can evolve. Also, for a fixed number of action this process allows the agent to explore quadratically more outcomes with the same computational effort, making him a wiser decision maker.

Finally, this process can also be compared with a quantum version of decision networks (Russel and Norvig 2010), as discussed in Oliveira (2019). The results show that again the best process depends on the characteristics of the problem. Although, it is important to mention that process A solves a decision process that wants to sample an action from a distribution based on the expected utilities in a extremely efficient way with only one sample, this kind of decision processes could be used and studied for applications in reinforcement learning.

# 6 Proof-of-Concept Implementation 

The algorithm presented in Sect. 4 was implemented on the IBM Q quantum simulator as a proof-of-concept. At our disposal was the IBM 20-qubit machine, which is based on superconducting circuits (Steffen 2011). This machine specifies an error term associated with each gate used in a quantum circuit and a life-time for each qubit. So, as the number of gates grows the error of the outcome grows as well. The output of a circuit with a considerable number of gates would be majorly noise. Thus, the decision processes presented before, which is based on a search problem, would be impossible to compute with a manageable error term.

IBM's best quantum computer is not the only that fails to solve such problems. The best quantum devices, in the world, are not even near to solve problems related to search problems with a higher dimension. However, that does not mean that the current devices are completely useless. There are problems where a Noisy Intermediate-Scale Quantum (NISQ) devices may have an impact, in the near future (Preskill 2018). The applications

![img-5.jpeg](img-5.jpeg)

Fig. 6 Bayesian network over 3 variables. Node L represents the evidence variable, A the action variable and R the outcome variable
![img-6.jpeg](img-6.jpeg)

Fig. 7 Quantum circuit composed by rotations and controlled-rotations
of these NISQ devices are related to simulations in chemistry and many-body quantum physics. ${ }^{2}$

Over the last years, quantum devices have had a lot of progress. For example, the number of qubits are smoothly increasing, the gate errors are reducing (Schäfer et al. 2018) and entanglement between them is becoming stronger (Kues et al. 2017; Pirandola et al. 2006). This progress has been giving hope to construct a powerful universal quantum computer, which one day may have a great impact on our everyday life. But to validate results as pretended, in this section a classical simulator has to be used. However, the same simulator struggles to compute the outcomes, if the number of qubits used increases. As mentioned before the complexity to simulate a quantum computer on a classical computer is too high. Given that, a very simple Bayesian network (Fig. 6) was selected for the decision process.

The network was encoded to a quantum state with use of the technique presented in Low et al. (2014), producing the circuit shown in Fig. 7.

A value for the evidence variable $L$ was selected $(L=$ False $)$ and the following utility function,

$$
U(R)= \begin{cases}7, & R=r \\ 3, & R=\neg r\end{cases}
$$

was applied with use of the proposed algorithm. However, to compute the algorithm on IBM's quantum simulator, each part has be to converted in a concrete quantum circuit (Fig. 8). Every state has to be encoded, which in theory is simple with the use of rotations and controlled-rotations. The major difficulty exists when the rotation is controlled

[^0]
[^0]:    ${ }^{2}$ It is interesting to mention that the major companies investing in quantum computing are constructing devices based on different technologies. Microsoft devices are based on topological quantum computing (Nayak et al. 2008), while Intel is exploring spin qubits (Vandersypen et al. 2017).

![img-7.jpeg](img-7.jpeg)

Fig. 8 Circuit representation of the amplitude amplification algorithm for the decision-making process

Table 3 Comparison between theoretical and experimental results after sampling from the constructed state


by more than one qubit. In such cases, this operation has to be decomposed to simpler and available operations in the working framework. The existence of an equivalent circuit is guaranteed by the fact that the simulator is a universal quantum computer, meaning that it may perform any possible computation. In practice, there are tools to decompose complex operations into simpler ones (Vartiainen et al. 2004; Möttönen et al. 2004).

Finally, these circuits have to be built on "Qiskit" which runs on a "jupyter notebook" (Github link "Quantum Bayesian Decisions"). The circuits created are sent as a job to IBM's servers and the results are sent back to the client. For this example, a significant number of samples was generated. The number of samples for each state of the action variable must be similar to the theoretical probability. Table 3 shows that this is indeed the case: the experimental result is quite similar to the one foreseen by theory.

The small discrepancies pointed out in Table 3 can be explained by deficiencies of the implementation. First, note that the amplitude amplification algorithm is probabilistic, i.e. the result is never entirely precise. On the other hand, the number of iterations in the amplitude amplification algorithm was an integer number; thus, if $n . m$ non-integer iterations are required the usage of the value bellow $n$ or the one above $n+1$, generates a small variation. Actually, it is possible to perform a a quantum search with a non-integer number of iterations (Zekrifa et al. 2000), but this would not add relevance to this results.

# 7 Conclusions and Future Work 

A quantum algorithm which solves the generic decision-making problem was presented. It is a very curious solution for couple of reasons. First, it has a proven computational advantage over the classical and the semi-classical solutions when the parameters are in the correct relation. Secondly, it samples from a very particular probability distribution, which classically would require an tremendous amount of computational work to recreate. Moreover, it benefits from the structure of the data, which no classical algorithm could benefit from, making it a very interesting example to illustrating the differences between classical and quantum computations.

To support the theoretical work described the algorithm was implemented in IBM's quantum simulator as a proof-of-concept. The results were as in correspondence with what theory anticipated for the example chosen, further confirming the ideas presented.

As an extension to this work we propose a search for decision problems that take advantage by sampling from the probability distribution created by this solution. Also, the deci-sion-making process discussed here was related to a static model, in which, neither the utility function nor the Bayesian network change in time. It would be of interest to verify if the decision-making process could benefit from an additional learning process (Jonsson and Barto 2007; Robinson and Hartemink 2010; Tong and Koller 2001). Enabling an agent to adapt its behaviour to a changing environment, would probably result in better outcomes, raising the number of possible applications.

# Appendix 

## A Complexity Comparison

The decision-making processes we aim at comparing require inequality (50) to be satisfied. It assures that the decision maker chooses with certainty the best action.

$$
\forall_{n \backslash\{\max \}} E U\left(\text { action }_{\max }\right)-E U\left(\text { action }_{n}\right)>\delta_{\text {action }_{\max }}+\delta_{\text {action }_{n}}
$$

Thus, to compare Process A and Process B it is necessary to consider all terms that are different. Therefore, the error term $\delta_{a}$ for Process A is related to directly sampling values for the expected utilities, while in Process B the expected utility is determined indirectly. For this reason, in Process B it is necessary to apply error propagation rules:

$$
E U(a \mid e)+\delta_{E U(a \mid e)}=\sum_{R}\left(P\left(\text { Result }=r \mid a, e\right)+\delta_{b}\right) * U(r)
$$

Before applying error propagation to this equation, we need to normalize it so that $E U(a \mid e) / k$ is equal to $P(a)$.

$$
P(a)+\delta_{a}=\sum_{R}\left(P\left(\text { Result }=r \mid a, e\right)+\delta_{b}\right) * F(r)
$$

where the normalization function $(F(r))$ is expressed as,

$$
F(r)=\frac{U(r)}{\sum_{a} \sum_{r} U(r) * P(r \mid a, e)}
$$

Here, again, the mean value of $U(r)$ is used:

$$
\begin{gathered}
F(r)=\frac{U(r)}{\sum_{a} \sum_{r} P(r \mid a, e) * U(r)}=\frac{U(r)}{\sum_{a} \frac{1}{N_{r}}}=\frac{U(r)}{\frac{N_{a}}{N_{r}}}=\frac{N_{r} * U(r)}{N_{a}} \\
F(r)=\frac{1}{N_{a}}
\end{gathered}
$$

Expressing the equation that determines the error term $\delta_{a}$ as a function of the error term $\delta_{b}$ yields

$$
\delta_{a}=\sqrt{\sum_{R} \delta_{b}^{2} * F(r)^{2}}
$$

Using Eq. (55) we obtain:

$$
\delta_{a}=\sqrt{\sum_{R} \delta_{b}^{2} *\left(\frac{1}{N_{a}}\right)^{2}}
$$

Then, assuming that $\delta_{b}$ is similar, which is in favor of Process B because it minimizes the $\delta_{a}$ term:

$$
\delta_{a}=\sqrt{N_{r} * \delta_{b}^{2} *\left(\frac{1}{N_{a}}\right)^{2}}
$$

yielding,

$$
\delta_{a}=\left(\frac{\sqrt{N_{r}}}{N_{a}}\right) * \delta_{b}
$$

With the relation between the error terms determined, it is possible to compare the difference of the computational effort involved in both processes, assuming again the mean terms for the probabilities:

$$
\sqrt{\frac{N_{a}}{N_{r}}} * \frac{A_{r, \alpha} * \frac{1}{N_{r}} *\left(1-\frac{1}{N_{r}}\right) * \delta_{a}^{2} * N_{a}}{A_{a, \alpha} * \frac{1}{N_{a}} *\left(1-\frac{1}{N_{a}}\right) * \delta_{b}^{2}}+\frac{2 * N_{a} * N_{r}}{n * 2^{m} * \sqrt{\frac{N_{r}}{P(e)}} * \frac{A_{a, \alpha} * \frac{1}{N_{a}} *\left(1-\frac{1}{N_{a}}\right)}{\delta_{a}^{2}}}
$$

Let us call the term on the right,

$$
t_{1}=\frac{2 * N_{a} * N_{r}}{n * 2^{m} * \sqrt{\frac{N_{r}}{P(e)}} * \frac{A_{a, \alpha} * \frac{1}{N_{a}} *\left(1-\frac{1}{N_{a}}\right)}{\delta_{a}^{2}}}
$$

Using 59,

$$
\sqrt{\frac{N_{a}}{N_{r}}} * \frac{N_{r}}{N_{a}} * \frac{A_{r, \alpha} * \frac{1}{N_{r}} *\left(1-\frac{1}{N_{r}}\right)}{A_{a, \alpha} * \frac{1}{N_{a}} *\left(1-\frac{1}{N_{a}}\right)}+t_{1}
$$

also,

$$
\sqrt{\frac{N_{r}}{N_{a}}} * \frac{A_{r, \alpha} * \frac{1}{N_{r}} *\left(1-\frac{1}{N_{r}}\right)}{A_{a, \alpha} * \frac{1}{N_{a}} *\left(1-\frac{1}{N_{a}}\right)}+t_{1}
$$

and,

$$
\sqrt{\frac{N_{r}}{N_{a}}} * \frac{A_{r, \alpha} *\left(\frac{1}{N_{r}}-\frac{1}{N_{r}^{2}}\right)}{A_{a, \alpha} *\left(\frac{1}{N_{a}}-\frac{1}{N_{a}^{2}}\right)}+t_{1}
$$

From Inglot (2010) we obtain a lower bound for $A_{\alpha, k}$. Although these terms are different for distinct values of $\alpha$, we consider the one where $\alpha$ is not leaning to zero too fast. Thus,

$$
A_{\alpha, k} \geq k+2 * \log \frac{1}{\alpha}-\frac{5}{2}
$$

With this equation it is possible to define a better value for the difference between the computational efforts,

$$
\sqrt{\frac{N_{r}}{N_{a}}} * \frac{\left(N_{r}+2 * \log \frac{1}{\alpha}-\frac{7}{2}\right) *\left(\frac{1}{N_{r}}-\frac{1}{N_{r}^{2}}\right)}{\left(N_{a}+2 * \log \frac{1}{\alpha}-\frac{7}{2}\right) *\left(\frac{1}{N_{a}}-\frac{1}{N_{a}^{2}}\right)}+t_{1}
$$

As

$$
\lim _{N_{r} \rightarrow \infty}\left(N_{r}+2 * \log \frac{1}{\alpha}-\frac{7}{2}\right) *\left(\frac{1}{N_{r}}-\frac{1}{N_{r}^{2}}\right)=1
$$

and,

$$
\lim _{N_{a} \rightarrow \infty}\left(N_{a}+2 * \log \frac{1}{\alpha}-\frac{7}{2}\right) *\left(\frac{1}{N_{a}}-\frac{1}{N_{a}^{2}}\right)=1
$$

it is possible to approximate the expression to

$$
\sqrt{\frac{N_{r}}{N_{a}}} * \frac{\left(N_{r}+2 * \log \frac{1}{\alpha}-\frac{7}{2}\right) *\left(\frac{1}{N_{r}}-\frac{1}{N_{r}^{2}}\right)}{\left(N_{a}+2 * \log \frac{1}{\alpha}-\frac{7}{2}\right) *\left(\frac{1}{N_{a}}-\frac{1}{N_{a}^{2}}\right)}+t_{1} \approx \sqrt{\frac{N_{r}}{N_{a}}}+\frac{2 * N_{a} * \sqrt{N_{r} * P(e)} * \delta_{a}^{2}}{n * 2^{m}}
$$

Writing the term of $\delta_{a}$ as a function of its dimension and a factor that adjusts the precision,

$$
\delta_{a}=\frac{1}{c * N_{a}}
$$

we obtain,

$$
\sqrt{\frac{N_{r}}{N_{a}}}+\frac{2 * \sqrt{N_{r} * P(e)}}{N_{a} * c^{2} * n * 2^{m}}
$$

Rewriting this the expression as,

$$
\sqrt{\frac{N_{r}}{N_{a}}} *\left(1+\frac{2 * \sqrt{P(e)}}{\sqrt{N_{a}} * c^{2} * n * 2^{m}}\right)
$$

Because,

$$
\frac{2 * \sqrt{P(e)}}{\sqrt{N_{a}} * c^{2} * n * 2^{m}} \geq 0
$$

for any value of the composing variables, then,

$$
\sqrt{\frac{N_{e}}{N_{a}}} *\left(1+\frac{2 * \sqrt{P(e)}}{\sqrt{N_{a}} * c^{2} * n * 2^{m}}\right) \geq \sqrt{\frac{N_{e}}{N_{a}}}
$$

we prove that the relation between Process A and B is under bounded by,

$$
\sqrt{\frac{N_{e}}{N_{a}}}
$$
