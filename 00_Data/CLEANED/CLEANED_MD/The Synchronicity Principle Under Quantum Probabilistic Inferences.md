# QUT 

## Queensland University of Technology

Brisbane Australia

This may be the author's version of a work that was submitted/accepted for publication in the following source:

Pinto Moreira, Catarina \& Wichert, Andreas
(2015)

The synchronicity principle under quantum probabilistic inferences.
NeuroQuantology, 13(1), pp. 111-133.
This file was downloaded from: https://eprints.qut.edu.au/127311/

## (c) Consult author(s) regarding copyright matters

This work is covered by copyright. Unless the document is being made available under a Creative Commons Licence, you must assume that re-use is limited to personal use and that permission from the copyright owner must be obtained for all other uses. If the document is available under a Creative Commons License (or other specified license) then refer to the Licence for details of permitted re-use. It is a condition of access that users recognise and abide by the legal requirements associated with these rights. If you believe that this work infringes copyright please provide details by email to qut.copyright@qut.edu.au

Notice: Please note that this document may not be the Version of Record (i.e. published version) of the work. Author manuscript versions (as Submitted for peer review or as Accepted for publication after peer review) can be identified by an absence of publisher branding and/or typeset appearance. If there is any doubt, please refer to the published source.
https://doi.org/10.14704/nq.2015.13.1.788

# The Synchronicity Principle under Quantum Probabilistic Inferences 

## Catarina Moreira and Andreas Wichert

## ABSTRACT

We propose a new quantum Bayesian Network model in order to compute probabilistic inferences in decisionmaking scenarios. The application of a quantum paradigm to decision making generates interference effects that influence probabilistic inferences. These effects do not exist in a classical setting and constitute a major issue in the decision process, because they generate quantum parameters that highly increase with the amount of uncertainty of the problem. To automatically compute these quantum parameters, we propose a heuristic inspired by Jung's Synchronicity principle. Synchronicity can be defined by a significant coincidence that appears between a mental state and an event occurring in the external world. It is the occurrence of meaningful, but not causally connected events. We tested our quantum Bayesian Network together with the Synchronicity inspired heuristic in empirical experiments related to categorization/decision in which the law of total probability was being violated. Results showed that the proposed quantum model was able to simulate the observed empirical findings from the experiments. We then applied our model to a more general scenario and showed the differences between classical and quantum inferences in a Lung Cancer medical diagnosis Bayesian Network.

Key Words: Bayesian networks, decision making, quantum probability, synchronicity principle, quantum cognition
DOI Number: 10.14704/nq.2015.13.1.788
NeuroQuantology 2015; 1:111-133

## 1. Introduction

The present work proposes a new quantum Bayesian Network formalism to model complex systems for human decision-making. A Bayesian Network can be defined as an acyclic directed graph in which each node represents a random variable and each edge represents a direct causal influence from the source node to the target node (conditional dependencies). One problem with current probabilistic systems is that they cannot make reliable predictions in situations where the

[^0]laws of probability are being violated. These situations happen quite frequently in systems which try to model human decisions (Tversky and Kahnenman, 1974; Tversky and Kahneman, 1983; Tversky and Shafir, 1992; Aerts et al., 2004; Birnbaum, 2008).

The proposed Bayesian Network accommodates these violations, through the computation of quantum probabilistic inferences, using quantum interference effects. Additionally, we propose a heuristic that provides a possible interpretation of the quantum parameters that emerge from interference effects. The proposed heuristic also enables the automatic tuning of an exponential number of quantum parameters in more complex decision-making systems. This heuristic is inspired by Jung's Synchronicity principle, which corresponds to a significant


[^0]:    Corresponding author: Catarina Moreira
    Address: Instituto Superior Tecnico, INESC-ID, Av. Professor Cavaco Silva, 2744-016 Porto Salvo, Portugal.
    e-mail : catarina.p.moreira@ist.utl.pt
    Relevant conflicts of interest/financial disclosures: The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.
    Received: 25 September 2014; Accepted: 12 January 2015
    eISSN 1303-5150

coincidence that appears between a mental state and an event occurring in the external world (Martin et al., 2009). It is the occurrence of meaningfully, but not causally connected events. We argue that, with the Synchronicity principle, quantum parameters can code semantic similarities that can generate acausal connections between events.

The idea of combining Jung's theories with quantum theory is not new. For instance, Blutner and Hochnadel (2010) proposed a quantum model to represent Jung's theory of personality. A four dimensional Hilbert space representation with two qubits was used together with quantum projection operators. Limar (2012) studied Jung's Synchronicity and established a relation between this principle and the quantum entanglement phenomena.

Quantum cognition is a research field that aims at using the mathematical principles of quantum mechanics to model cognitive systems for human decision-making. Given that Bayesian probability theory is very rigid in the sense that it poses many constraints and assumptions (independence, set theory, etc.), it becomes too limited (or even impossible) to provide models that can capture human judgments and decisions, since people are constantly violating the laws of logic and probability theory (Busemeyer and Bruza, 2012).

Quantum probability theory benefits from many advantages towards its classical counterpart. It can represent events in vector spaces, and consequently take into account the problem of order of effects (Wang and Busemeyer, 2013; Trueblood and Busemeyer, 2011) and represent all events at the same time as a superposition. Psychologically, a superposition effect can be related to the feeling of confusion, uncertainty or ambiguity (Busemeyer and Bruza, 2012). Additionally, this vector space representation does not obey to the distributive axiom of Boolean logic and to the law of total probability. This enables the construction of more general models that can mathematically explain cognitive phenomena such as conjunction/disjunction errors (Busemeyer et al., 2011; Franco, 2009) or violations of the Sure Thing Principle (Pothos and Busemeyer, 2009; Khrennikov and Haven, 2009).

### 1.1 Motivation

The most important motivation of this work is to propose to exchange the Bayesian mathematical models that are currently being used in cognitive systems and replace it by a more generalized probability theory: the quantum theory. Note that we are not stating that human cognition is a quantum computer or can be simulated by quantum processes. Instead, we are just focusing on the mathematical implications of using an alternative probabilistic theory to model human decisions, just like in the previous works of (Busemeyer et al., 2006b, 2009; Pothos and Busemeyer, 2009).

The main problem of applying quantum formalisms to cognition is concerned with the number of free parameters, which emerge from interference effects. The more uncertainty the decision problem has, the more free quantum parameters the system will need to deal with. The automatic tuning of such parameters is still an open research question and efficient methods to automatically tune these parameters are practically inexistent. The current works of the literature have been only focusing in very small decision problems in order to avoid dealing with so many quantum parameters. Additionally, a true interpretation of these quantum parameters in the scope of quantum cognition is not very clear in the literature.

In order to accommodate human violations of probability theory, we were inspired by Jung's theories about the correlation of acausal events. We believe that when humans make decisions, the events that they try to combine in their minds are correlated by a shared meaning, rather than cause/effect relationships, just like stated by the representativeness heuristic (Kahneman et al., 1982; Tversky and Kahnenman, 1974).

The reason why we are turning to Bayesian Networks is because they are inspired in human cognition. It is easier for a human to combine pieces of evidence and to reason about them, instead of calculating all possible events and their respective beliefs. In the same way, Bayesian Networks also provide this link between human cognition and rational inductive inference. Instead of representing the full joint distribution, Bayesian Networks represent the decision problem in small modules that can be combined to perform inferences. Only the probabilities, which are actually needed to perform the

inferences are computed, reducing computational costs (Griffiths et al., 2008).

### 1.2 Contributions

The main contributions of the present work are the following:

- It is proposed a new approach for quantum Bayesian Networks that takes into account quantum interference effects. These effects enable the modulation of decision-making problems that can accommodate violations of the classical law of total probability.
- The present work is one of the first in the literature that proposes a method to address the problem of automatically tuning an exponential number of quantum parameters during probabilistic inferences. We propose a novel and simple approach inspired by Jung's Synchronicity principle to tune quantum parameters. It is assumed that during the reasoning process, human beliefs are correlated by a shared meaning, rather than cause/effect relationships.
- Inspired by Jung's Synchronicity principle, we also represent the cognitive decision problem through a semantic network (Osherson, 1995) in order to extract the events that share meaningful connections. We then propose to link semantic relations to synchronicity events and incorporate these meaningful connections into quantum probabilistic inferences.


### 1.3 Research Questions

With the present work, we intend to address the following research questions. An answer to these questions is given in Section 8. What is the meaning of quantum parameters in the realm of quantum cognitive systems? What is the advantage of the proposed approach? How can it make a difference towards the current wellestablished quantum models that have been proposed in the literature?

## 2. Quantum Probability Theory

Quantum probability was created in order to explain paradoxical findings that could not be addressed through traditional probability theory. More specifically, predictions concerned with
human decision making tend to violate the laws of classical probability (Tversky and Kahnenman, 1974; Tversky and Kahneman, 1983; Tversky and Shafir, 1992; Aerts et al., 2004; Birnbaum, 2008). Recent literature suggests that quantum probability can be used as a mathematical alternative to the classical theory and it is able to accommodate these violations, improving the probabilistic inferences (Aerts, 1995; Bordley, 1998; Busemeyer et al., 2006b; Mura, 2009; Lambert-Mogiliansky et al., 2009; Yukalov and Sornette, 2011; Aerts et al., 2011).

One can look at a cognitive quantum system model as a wave moving across time over the state space until a decision is made. In quantum theory, this is called an indefinite state, since the wave is not in a specific state at each time. It is in a superposition of states, that is, all states simultaneously. Once a decision is reached, uncertainty is resolved and the state becomes definite as if the wave had collapsed to a specific condition - a definite state (Busemeyer and Bruza, 2012).

### 2.1 Main Elements of Quantum Probability Theory

Quantum probability can be seen as a generalization of the Bayesian theory. Events are contained in Hilbert spaces, which correspond to a vector space of complex numbers (amplitudes) and enables the calculation of probabilities by a measurement: performing the squared magnitude of an amplitude. This representation allows events to interfere with each other, influencing their final probabilities. These interference effects generate a set of new parameters that can be used to either accommodate violations in Bayesian theory (Busemeyer and Bruza, 2012) or, as we claim in this work, to show an alternative way to perform and improve probabilistic inferences.

In this section we summarize the main elements of quantum probability theory. Appendix A describes these elements with more detail.

- Quantum Amplitudes: are represented by complex numbers. They contain a real part and an imaginary part and can be written in the form $a+i b$, where $a$ and $b$ represent the coordinates of a point in a complex plane and $i$ is the imaginary part. A complex

amplitude can also be represented in the form $|r| e^{i \theta}$, where $|r|=\sqrt{a^{2}+b^{2}}$ and $\theta$ corresponds to the angle that the point $(a, b)$ forms with the origin of the plane.

- Quantum System Space: corresponds to Hilbert Spaces. It can be viewed as a generalization and extension of the Euclidean space into spaces with any finite or infinite number or dimensions. It is a vector space defined over complex numbers and offers the structure of a dot product to enable the measurement of angles and lengths (Hirvensalo, 2003). The space is spanned by a set of orthonormal basis vectors. Together, these vectors form a basis for the space. Inferences are then calculated through similarities between vectors (Tversky and Kahneman, 1977; Krumhansl, 1978; Busemeyer and Diederich, 2010).
- Quantum Events: events correspond to a subspace spanned by a subset of the basis vectors contained in a complex Hilbert Space. Events can be orthonormal, that is, they can be mutually exclusive. Operations such as intersection and union of events are well defined if the events are spanned by the same set of basis vectors (Busemeyer and Bruza, 2012). In quantum theory, all the events contained in a Hilbert Space are defined through a superposition state which is represented by a state vector comprising the occurrence of all events.
- Quantum System State: corresponds to a probability function Pr which maps events into probability numbers, i.e., positive real numbers between 0 and 1. In quantum theory, this is given by the squared magnitude of the projection of the superposition state to the subspace containing the observed event


## 3. Quantum Interference Effects and Their Challenges

Quantum theory enables the modeling of the decision system as a wave moving over time across a state space until a final decision is made. Under this perspective, interference can be regarded as a chain of waves in a superposition state, coming from different directions. When these waves crash, one can experience a
destructive effect (one wave destroys the other) or a constructive effect (one wave merges with another). In either case, the final probabilities of each wave are affected.
![img-0.jpeg](img-0.jpeg)

Figure 1. The quantity $\theta$ corresponds to the difference between the phases of the two waves $\left(\psi_{1}=R e\left[e^{i \phi}\right]\right.$ and $\left.\psi_{A}=R e\left[e^{i(\phi+q)}\right]\right)$. This difference between wavefunctions has a very important physical meaning: the determination of how the waves will interfere with each other.

Interference effects can be naturally derived from the rules of complex numbers. The relation of some event $A$ between classical probability, $\operatorname{Pr}(A)$, and a quantum probability amplitude, $e^{i \phi_{A}} \psi_{A}$, is given by Born's rule Caves02 in Equation 1. A quantum amplitude corresponds to the amplitude of a wave. The term $e^{i \phi_{A}}$ is the phase of the amplitude just like illustrated in Figure 1.
$\operatorname{Pr}(A)=\left|e^{i \phi_{A}} \psi_{A}\right|^{2}$
Suppose that events $A_{1}, A_{2}, \ldots, A_{N}$ form a set of mutually disjoint events, such that their union is all in the sample space, $\Omega$, for any other event $B$. Then, the classical law of total probability can be formulated like in Equation 2.
$\operatorname{Pr}(B)=\sum_{i=1}^{N} \operatorname{Pr}\left(A_{i}\right) \operatorname{Pr}\left(B \mid A_{i}\right)$ where: $\sum_{i=1}^{N} \operatorname{Pr}\left(A_{i}\right)=1$

The quantum law of total probability can be derived through Equation 2 by applying Born's rule (Equation 1):
$\operatorname{Pr}(B)=\left|\sum_{a=1}^{N} e^{i \phi_{a}} \psi_{A_{a}} \psi_{B \mid A_{B}}\right|^{2} \quad \sum_{a=1}^{N}\left|e^{i \phi_{a}} \psi_{A_{a}}\right|^{2}=1$

Generalizing Equation 3 for $N$ events, the final quantum probabilistic interference formula, derived from the law of total probability, is given by (for detailed calculations, please refer to Appendix 11):

$$
\begin{aligned}
& P_{r}(B)=\sum_{i=1}^{N-1}\left|v_{A_{i}} v_{B i A_{i}}\right|^{2} \\
& +2 \sum_{i=1}^{N-2} \sum_{j=i+1}^{N}\left|v_{A_{j}} v_{B i A_{j}}\right|\left|v_{A_{j}} v_{B i A_{j}}\right| \cos \left(\theta_{i}-\theta_{j}\right)
\end{aligned}
$$

Following Equation 4, when $\cos \left(\theta_{i}-\theta_{j}\right)$ equals zero, then it is straightforward that quantum probability theory converges to its classical counterpart, because the interference term will be also zero.

For non-zero values, Equation 4 will produce interference effects that can affect destructively the classical probability (when the interference term in smaller than zero) or constructively (when it is bigger than zero). Additionally, Equation 4 will lead to a large amount of $\theta$ parameters when the number of events increases. For $N$ binary random variables, we will end up with $2^{N}$ parameters to tune.

## 4. Quantum Bayesian Network: Description of the Model

The model that we propose in this work comprises three stages:

- Extraction of a Semantic Network: Given the structure of a Bayesian Network representing the decision problem, we extract synchronized events through their meaning. The reason why we need to derive a semantic network comes from Jung's definition of Synchronicity. If there is no semantic extraction of the meaning of the events, then there cannot be any meaningful connection and no Synchronicity experienced. Under this paradigm, the quantum parameters can be interpreted as the semantic relation between these acausal events.
- The Synchronicity Heuristic: After designing the Semantic Network one can identify which events of the Bayesian network share meaningful connections. The Synchronicity heuristic will enable the automatic computation of the parameter $\theta$ associated to a pair of synchronized events.
- Inferences in a Quantum Bayesian Network: After computing all quantum $\theta$ parameters with the synchronicity heuristic, then one can perform quantum inferences in the Bayesian Network that take into account interference effects. These effects will enable the accommodation of the violations of the laws of probability theory that have been verified in many empirical experiments (Tversky and Shafir, 1992; Conte et al., 2009, 2007a).


### 4.1 Semantic Networks

A semantic network is often used for knowledge representation. It corresponds to a directed or undirected graph in which nodes represent concepts and edges reflect semantic relations. The extraction of the semantic network from the original Bayesian Network is a necessary step in order to find variables that are only connected in a meaningful way (and not necessarily connected by cause/effect), just like it is stated in the Synchronicity principle.

### 4.2 Inference in Bayesian Networks

Bayesian Networks are directed acyclic graphs in which each node represents a different random variable from a specific domain and each edge represents a direct influence from the source node to the target node. The graph represents independence relationships between variables and each node is associated with a conditional probability table which specifies a distribution over the values of a node given each possible joint assignment of values of its parents. The full joint distribution of a Bayesian Network (Russel and Norvig, 2010) is given by Equation 5. Variable $X$ is the list of variables.

$$
P_{r}\left(X_{i} \stackrel{\Delta}{\sim} X_{N}\right)=\prod_{i=1}^{N} P_{r}\left(X_{i} \mid \operatorname{Parents}\left(X_{i}\right)\right)
$$

The formula for computing classical exact inferences on Bayesian Networks is based on the full joint distribution. Let $e$ be the list of observed variables and let $Y$ be the remaining unobserved variables in the network. For some query $X$, the inference is given by Equation 6.

$\operatorname{Pr}_{e}(X \mid e)=\alpha \operatorname{Pr}_{e}(X, e)=\alpha\left[\sum_{y \in Y} \operatorname{Pr}_{e}(X, e, y)\right]$
Where $\alpha=\frac{1}{\sum_{x \in X} \operatorname{Pr}_{e}(X=x, e)}$
The summation is over all possible $y$, i.e., all possible combinations of values of the unobserved variables $y$. The $\alpha$ parameter, corresponds to the normalization factor for the distribution $\operatorname{Pr}(X \mid e)$ (Russel and Norvig, 2010).

The quantum counterpart of the full joint probability distribution (Equation 5) corresponds to Equation 7, in which $\left.\operatorname{QPr}\left(X_{i} \mid\right.\right.$ Parents $\left.\left(X_{i}\right)\right)$ corresponds to the quantum amplitude of the classical probability $\operatorname{Pr}\left(X_{i} \mid\right.$ Parents $\left.\left(X_{i}\right)\right)$.
$\operatorname{Pr}_{q}\left(X_{i} \right)^{=2}, X_{N}\right)=\left|\prod_{i=1}^{N} \operatorname{QPr}\left(X_{i} \mid\right.\right.$ Parents $\left.\left(X_{i}\right)\right) \|^{2}$
The quantum counterpart of the Bayesian exact inference formula corresponds to the application of Born's rule to Equation 6.
$\operatorname{Pr}_{q}(X \mid e)=\alpha\left|\sum_{x} \prod_{x=1}^{N} \operatorname{QPr}\left(X_{x} \mid\right.\right.$ Parents $\left.\left(X_{x}\right), e, y\right) \|^{2}$
Expanding Equation 8, it will lead to the quantum interference formula:
$\operatorname{Pr}_{q}(X \mid e)=$
$\alpha \sum_{i=1}^{|X|} \prod_{x}^{N} \operatorname{QPr}\left(X_{x} \mid\right.$ Parents $\left.\left(X_{x}\right), e, y=i\right) \|^{2}$
$+2 \cdot$ Interference
Interference $=$
$\sum_{i=1}^{|X|-1} \sum_{j=i+1}^{|X|} \prod_{x}^{N} \operatorname{QPr}\left(X_{x} \mid\right.$ Parents $\left.\left(X_{x}\right), e, y=i\right) \mid$
$\left|\prod_{x}^{N} \operatorname{QPr}\left(X_{x} \mid\right.\right.$ Parents $\left.\left(X_{x}\right), e, y=j\right) \mid \cdot \cos \left(\theta_{i}-\theta_{j}\right)$
Note that, in Equation 9, if one sets $\left(\theta_{i}-\theta_{j}\right)$ to $\pi / 2$, then $\cos \left(\theta_{i}-\theta_{j}\right)=0$, which means that the quantum Bayesian Network collapses to its classical counterpart.
4.3 The Synchronicity Principle as an Heuristic to Estimate Quantum Parameters
Jung's Synchronicity principle may occur as a
single event or a chain of related events and can be defined by a significant coincidence which appears between a mental state and an event occurring in the external world (matter) (Martin et al., 2009).

Inspired by Jung's ideas, the physicist Wolfgang Pauli proposed the exclusion principle. It states that quantum entities are in one of two possible forms: symmetric form and antisymmetric form. It is because of anti-symmetry that electrons are prevented from occupying the same energy states and forced to take up characteristic energy patterns around an atom without any apparent cause/effect relationship between them. Thus, Pauli had discovered an acausal connection principle that governs the fundamentals of quantum matter, suggesting that there is a deep connection between Jung's Synchronicity principles (Lindorff, 2004).

The heuristic that we propose in this work is also inspired in Jung's and Pauli's principles. It seeks to correlate acausal events in Bayesian Networks through the computation of the quantum parameters.

### 4.3.1 The Synchronicity Heuristic to Automatically Adjust Quantum Parameters in Quantum Inferences

We define the Synchronicity heuristic in a similar way to Jung's principle: two variables are said to be synchronized, if they share a meaningful connection between them. This meaningful connection can be obtained through a semantic network representation of the variables in question. This will enable the emergence of new meaningful connections that would be inexistent when considering only cause/effect relationships. The quantum parameters are then tuned in such a way that the angle formed by these two variables, in a Hilbert space, is the smallest possible, this way forcing acausal events to be correlated.

In the case of binary variables, the Synchronicity heuristic is associated with a set of two variables, which can be in one of four possible states. The Hilbert space is partitioned according to these four states, as exemplified in Figure 2. The angles formed by the combination of these four possible states are detailed in Table 1.

In the right extreme of the Hilbert space

represented in Figure 2, we encoded it as the occurrence of a pair of synchronized variables. So, when two synchronized variables occur, the smallest angle that these vectors make between each other corresponds to $\theta=0$. The most dissimilar vector corresponds to the situation where two synchronized variables do not occur. So, we set $\theta$ to be the largest angle possible that is $\pi$.


Table 1. Encoding of the Synchronized variables with their respective angles.
![img-1.jpeg](img-1.jpeg)

Figure 2. Two synchronized events forming an angle of $\mathrm{n} / 4$ between them.

The other situations correspond to the scenarios where one synchronized variable occurs and the other one does not. In Figure 2, the parameter $\theta$ is chosen according to the smallest angle that these two vectors, $i$ and $j$, make between each other, that is $\pi / 4$. We are choosing the smallest angle, because we want to correlate these two acausal events by forcing the occurrence of coincidences between them, just like described in the Synchronicity principle. The axis corresponding to $\pi / 2$ and $3 \pi / 2$ were ignored, because they correspond to classical probabilities $(\cos (\pi / 2)=\cos (3 \pi / 2)=0)$.

In the next sections, the proposed quantum Bayesian Network with the Synchronicity heuristic is applied in the empirical experiments performed by Busemeyer et al. (2009) (Section 5.1) and in a general medical diagnosis system to
determine whether a person has lung cancer or not (Section 5.2).

## 5 Experiments

In the work of Busemeyer et al. (2009), the authors performed an empirical experiment based on interactions between categorization and decision making. This experiment served as an empirical test to compare Markov and Quantum models.

The experiment can be summarized as follows. On each trial, participants were shown digitally modified pictures of faces. These faces were digitally modified under two characteristics: face width and lip thickness. This gave rise to two different face distributions: a narrow face distribution (with a narrow width and thick lips) and a wide face distribution (with a wide width and thin lips).

The participants had to categorize the faces as Good guy or Bad guy and/or choose the actions Attack or Withdraw. The following test conditions were performed: the C -then-D condition, the D -then- C condition, the D -alone and the C -alone conditions.

In the C-then-D condition, participants had to first perform a categorization of the face and then choose an action decision. In the D-then-C condition, participants had to select an action decision and then perform the categorization of the face. In the C -alone participants only performed the categorization of the face, whereas in the D -alone condition, participants had to choose an action decision towards the given face. For more details of how this experiment was conducted please refer to the work of Busemeyer et al. (2009).


Table 2. Empirical data collected in Busemeyer's C-then-D experiment.

The main results obtained with this experiment are discriminated in Table 2. In this table, $\operatorname{Pr}(G)$ is the probability of a participant categorizing a face as Good. $\operatorname{Pr}(A \mid G)$ is the probability of a participant deciding to Attack, given that the face was categorized as being Good. $\operatorname{Pr}(B)$ is the probability of a participant

categorizing a face as Bad. $\operatorname{Pr}(A \mid B)$ is the probability of choosing an Attack action, given that the face was categorized as Bad. Total Prob corresponds to the total probability through the formula $\operatorname{Pr}(A)=\operatorname{Pr}(A \mid G)+\operatorname{Pr}(B) \operatorname{Pr}(A \mid B)$. Finally, $\operatorname{Pr}(A)$ corresponds to the total probability observed in the experiment. In order to verify if the experiment accommodates the law of total probability, the values obtained in the columns Total Prob and $\operatorname{Pr}(A)$ should be similar. The Bayesian Networks corresponding to these experiments are presented in Figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 3. Bayesian Network representing the empirical results observed for the Narrow faces (left) and Wide faces (right) experiments reported on the work of Busemeyer et al. (2009).

As far as we know, there are no data in the literature concerned with complex decision making scenarios that end up violating the Sure Thing Principle. By complex, we mean scenarios that can be modeled by at least three random variables. In this simple experiment the Bayesian Network is the same as the semantic network, so it does not show the impact of the synchronicity principle as in the Lung Cancer experiment (Section 6). The purpose of this small experiment is to show a step-by-step application of the proposed Bayesian Network with the Synchronicity heuristic for the understanding of the reader.
5.1 Experiment 1: Classical Bayesian Networks vs Quantum Bayesian Networks
There are two main works in the literature that have contributed to the development and understanding of Quantum Bayesian Networks. One belongs to Tucci (1995) and the other to Leifer and Poulin (2008). Table 3 compares all approaches for the experiment conducted by Busemeyer et al. (2009).

In the work of Tucci (1995) it is argued that any classical Bayesian Network can be extended to a quantum one by replacing real probabilities with quantum complex amplitudes. This means that the factorization should be performed in the same way as in a classical Bayesian Network. So, the Bayesian Network on the left of Figure 3 could be represented by a Quantum Bayesian Network with the following matrices:

$$
\begin{aligned}
& \text { Node }_{0}=\left[\begin{array}{ll}
e^{i \theta_{1}} \sqrt{0.19} & e^{i \theta_{2}} \sqrt{0.81}
\end{array}\right] \\
& \text { Node }_{0}=\left[\begin{array}{ll}
e^{i \theta_{1}} \sqrt{0.43} & e^{i \theta_{2}} \sqrt{0.57} \\
e^{i \theta_{3}} \sqrt{0.63} & e^{i \theta_{4}} \sqrt{0.37}
\end{array}\right]
\end{aligned}
$$

One big problem with Tucci's work is concerned with the inexistence of any methods to set the phase parameters $e^{i \sigma}$. The author states that, one could have infinite Quantum Bayesian Networks representing the same classical Bayesian Network depending on the values that one chooses to set the parameters. This requires that one knows a priori which parameters would lead to the desired solution for each node queried in the network (which we never know). So, for these experiments, the model of Tucci (1995) cannot predict the results observed, since one does not have any information about the quantum parameters. Table 3 describes these results as c.p., that is, cannot predict.


Table 3. Comparison of various quantum Bayesian Networks from the literature with the proposed approach.

In the work of Leifer and Poulin (2008), the authors argue that, in order to develop a quantum Bayesian Network, it is required a quantum version of probability distributions, quantum marginal probabilities and quantum conditional probabilities (Table 4). The authors made a preliminary study of these concepts. Generally speaking, a quantum probability distribution corresponds to a density matrix contained in a Hilbert space, with the constraint that the trace of this matrix must sum to T. In quantum probability theory, a full joint distribution is given by a density matrix $p$. This matrix provides the probability distribution of all states that a Bayesian Network can have. The marginalization operation corresponds to a quantum partial trace (Nielsen and Chuang, 2000; Rieffel and Polak, 2011).

In the end, the proposed models fail to provide any advantage relative to the classical models, because they cannot take into account interference effects between random variables. So, they do not provide any advantages in modeling decision making problems that try to predict decisions that violate the laws of total probability.


Table 4. Relation between classical and quantum probabilities used in the work of Leifer and Poulin (2008).

### 5.2 Experiment 2: Quantum Dynamical Model vs Quantum Bayesian Networks

In the work of Busemeyer et al. (2009), the authors proposed a quantum dynamical Model that takes into account interference effects, which included a Hamiltonian that had several parameters formalizing typical decision process and also a quantum entanglement process. The categorization and decision processes were entangled (interdependent). Using this Hamiltonian, they derived a unitary transform that predicted the interference effects of categorization and decision. Additionally, the authors had to fit this Hamiltonian matrix using the observed probabilities. The quantum dynamical model requires the transition probability matrices to be double stochastic. That is, it requires that $\operatorname{Pr}\left(A_{1} / B\right)+\operatorname{Pr}\left(A_{2} / B_{i}\right)=1$ and $\operatorname{Pr}(A_{i} / B i)+\operatorname{Pr}\left(A_{i} / B_{2}\right)=1$. This constraint can be a problem, because it usually fails when modeling two-dimensional transition matrices (Busemeyer et al., 2009).

For the categorization experiment, their Quantum Dynamical Model was able to predict the observed data with an error of just $7.25 \%$. With the proposed quantum Bayesian Network with the Synchronicity heuristic, we were able to drop the error percentage to $3.72 \%$. Although the results are not statistically significant, this means that the proposed Bayesian Network is a more general and scalable model that has the same performance as well established quantum models from the literature. The calculations used to compute the probabilities in Table 5 are detailed in Appendix C.


Table 5. Comparison between the Quantum Dynamical Model and the proposed Bayesian Network.

The proposed Bayesian Network also offers three main advantages towards the Quantum Dynamical Model:

- Bayesian Networks do not have the problem of double stochasticity. The conditional probability tables can be set by making a direct mapping of the decision problem to the Bayesian Network. For instance, the Bayesian Networks in Figure 3 was built by directly gathering the probabilities collected in the experiment, which are detailed in Table 2.
- Ability to automatically compute the quantum parameters without the need of complex quantum elements such as differential equations, Schrödinger equation, and the definition of Hamiltonian matrices.
- The proposed model can be generalized for any number of events so this model is scalable for decision making problems with several random variables, just like it will be demonstrated in Section 6.

The creation of Hamiltonians, just like it was proposed in the work of Busemeyer et al. (2009), is a very complex problem. These Hamiltonians will grow exponentially with the amount of random variables in the problem. Moreover, the

operation used to compute a unitary matrix corresponds to a matrix exponentiation. This operation is computationally very heavy and hard to compute. It is still an open research topic in the Mathematics community and usually computer programs use approximation methods in order to perform the computations.

### 5.3 Overall Results

Table 6 shows the main differences between all models analyzed in this work. As we already concluded from Section 5.1, the quantum Bayesian Network proposed in the work of Tucci (1995) is not suitable for these types of problems, because the author has no mentions in how to set these parameters. He even argues that a classical Bayesian Network can be represented by an infinite number of quantum Bayesian Networks, depending on how one tunes the quantum parameters.

In the work of Leifer and Poulin (2008), the authors make a direct mapping from classical probability to quantum theory. By converting a full joint probability distribution into a density matrix, the authors are canceling the interference terms. Consequently, their model has the same performance as classical Bayesian Network, not bringing any advantages to the inference problems where the laws of probability are being violated.


Table 6. Comparison of the different models proposed in the literature.

Although the Quantum Dynamical Model proposed by Busemeyer et al. (2009); Pothos and Busemeyer (2009) suffers from the problem of fitting the Hamiltonian matrix and from double stochasticity, it can model events dynamically through time evolution, which is a property that a cognitive system benefits from. This capability is not possible in the quantum Bayesian Network that we propose in this work. The only way to represent time evolution would be by using Dynamical Bayesian Networks.

6 Application to More Complex Bayesian Networks
In this experiment, we apply the proposed quantum model in a medical decision making scenario using a Lung Cancer Bayesian Network model (Figure 5) inspired by the book of Korb and Nicholson (2011).

### 6.1 Deriving a Semantic Network

Consider the following scenario regarding Lung Cancer. Lung Cancer is a disease characterized by an uncontrolled cell growth in tissues of the lung, which can spread to other parts of the body. It is fairly known that environmental destruction, such as long-term air pollution or smoking, can cause Lung Cancer (Peto and Darby, 2000). In the semantic network in Figure 4, Air Pollution and Smoking derive both from the same concept Environmental Destruction. Although these variables are not causally connected, they share a meaningful connection. So, these two variables become synchronized. Moreover, a person with Lung Cancer manifests several symptoms, such as chest pain, coughing, dyspnea, etc.
![img-3.jpeg](img-3.jpeg)

Figure 4. Semantic Network for the Lung Cancer Bayesian Network.

Coughing and dyspnea, although not causally connected, share a meaningful connection, since they both derive from the concept Symptom. Therefore, these variables will also constitute another synchronized pair.

### 6.2 Inference in Quantum Bayesian Networks

After designing the semantic representation of our Bayesian Network and after extracting the synchronized variables, the full Bayesian Network for Lung Cancer is given by Figure 5. In this network, the classical probabilities and quantum probability amplitudes are represented by the functions $\operatorname{Pr}$ and $Q P R$, respectively. In order to make a fair comparison between both

classical and quantum inferences, the quantum probability amplitudes were obtained by converting the classical real probabilities into complex numbers (Equation 1). This mapping of probabilities has also been used in other works of the literature (Tucci, 1995; Leifer and Poulin, 2008).

### 6.3 Results and Discussion

In this section, it is presented the results obtained using classical and quantum inference over the Lung Cancer Bayesian Network in Figure 5.

The results are presented in two different groups: inference with no evidences observed (Section 6.4) and inference with one piece of evidence observed (Section 6.5).
![img-4.jpeg](img-4.jpeg)

Figure 5. Lung Cancer Bayesian Network.
6.4 Results with No Evidences Observed: Maximum Uncertainty
We queried each variable of the network in Figure 5 without providing any observation. We
performed the following queries: $\operatorname{Pr}($ Smoker=true), $\operatorname{Pr}($ Pollution=high), $\operatorname{Pr}($ LungCancer=positive), $\operatorname{Pr}($ Cough=high) and $\operatorname{Pr}($ Syspnea=true). We then extracted both classical and quantum inferences and represented the results in the graph in Figure 6.

When nothing is observed, quantum probabilities tend to increase and overcome their classical counterpart. All nodes of the Bayesian Network are in a superposition state and the probabilities of the nodes start to be modified due to the interference effects. If one looks at the nodes as waves crossing the network from different locations, these waves can crash between each other, causing them to be either destroyed or merged. This interference is controlled by the Synchronicity principle: acausal events which are meaningful connected, become correlated. The synchronized variable pairs, (Cough, Dyspnea) suffered constructive inference. On the other hand, for the other pair of synchronized variables (Pollution, Smoker), the Pollution variable suffered destructive interference, whereas Smoker suffered constructive interference. This means that, when nothing is known, this pair of variables should not be synchronized at all since they could not be correlated effectively. The variable Lung Cancer also suffered constructive interference, since it is influenced by the increase of the probabilities in its parent nodes.
![img-5.jpeg](img-5.jpeg)

Figure 6. Probabilities obtained using classical and quantum inferences for different queries for the Lung Cancer Bayesian Network (Figure 5).


Table 7. Probabilities obtained when performing inference on the Bayesian Network of Figure 5.
6.5 Results with One Piece of Evidence Observed
When one starts to provide information to the Bayesian Network, then the superposition state collapses into another superposition quantum state, affecting the configuration of the remaining possible states of the network. Moreover, by making some observation to the network, we are reducing the total amount of uncertainty and, consequently, the reduction of the waves crossing the network, and the amount of interferences.

Table 7 shows that synchronized pairs tend to increase together. When variable Dyspnea is observed, the synchronized pairs (Pollution, Smoker) tend to increase $12.31 \%$ and $11.37 \%$ towards their classical counterparts, respectively. So, under this scenario, acausal events such as Pollution and Smoker became highly correlated due to the Synchronicity principle and had a similar growth. The same phenomena can be verified when the variable Smoker is observed. Dyspnea and Cough tend to increase $26.68 \%$ and $11,72 \%$ towards their classical counterpart, respectively.

## 7 Related Work

Quantum physics was created in order to explain puzzling findings that classical physics was unable to model and explain. In the same way, there was a need to explain paradoxical findings in the domain of cognitive science that could not be addressed through a classical probability framework. In this sense, cognitive scientists turned to quantum probability in an attempt to explain these paradoxical findings.

### 7.1 Pioneering Quantum Models

When quantum theory was created, many researches argued that the concepts of quantum
mechanics could be used outside of the domains of physics. Quantum theory was a new alternative and a more general theory that enabled the modeling of probabilistic and dynamic systems. Many researchers were inspired to use the mathematics of quantum theory in their own research areas. For instance, in the pioneering work of Aerts and Durt (1994), the authors created a quantum model to take into account order of effects: the $\mathcal{E}$-model which can be defined as a quantum machine that corresponds to a two dimensional Hilbert space. Given an event in this quantum machine one can compute quantum like probabilities. The model also makes use of a parameter $\mathcal{E}$ that measures the total amount of uncertainty when computing the probabilities (Aerts, 1995, 1998; Aerts et al., 2011).

Most human decision making systems need to take into account the contextuality of the decision problem. This is one of the major reasons to support the usage of quantum mathematical formalisms to cognition. Quantum theory enables the representation of physical entities that change their state under the influence of certain contexts (or measurements). Based on this contextuality, Khrennikov proposed the Vaxjo model (Khrennikov, 2010, 2009b,a, 2004). This model corresponds to a general contextual probability space from which the classical and quantum probability models can be derived. However, the probabilities that emerge from the Vaxjo model for trigonometric spaces (i.e. quantum probabilities), do not provide a complete description of a quantum system, since it can violate the positivity axiom of probability theory. In this sense, it was proposed in the literature an algorithm that extends the Vaxjo model and is able to accommodate the positivity axiom. The algorithm proposed is the QuantumLike Representation Algorithm (QLRA) and was

proposed by Khrennikov (1999, 2001, 2003, 2005a, b).

Another pioneering work that attempted to apply quantum formalisms outside of the realm of physics corresponds to the work of Atmanspacher et al. (2002), in which the authors propose the generalized quantum theory. The authors suggested exploring the phenomena of entanglement in domains outside of physics by formalizing a general quantum theory. Other authors applied quantum paradigms to economics by generalizing the classical expected utility framework and proposed a quantum projective expected utility function that does not violate the laws of classical probability theory and can accommodate Allais and Ellsberg paradoxes (Mura, 2009; Danilov and LambertMogiliansky, 2010). In the work of Piotrowski (2001), the author applied quantum theory to the fields of game theory and economics and developed a principle to minimize financial risks.

In what concerns violations of probability theory, there are many paradoxical situations where the classical probability is unable to model. The most important paradoxes consist in violations of the Sure Thing principle and disjunctive and conjunctive effects.

### 7.2 Violations of the Sure Thing Principle

The Sure Thing Principle is a concept widely used in game theory and was originally introduced by Savage (1954). This principle is fundamental in the Bayesian probability theory and states that if one prefers action $A$ over $B$ under state of the world $X$, and if one also prefers $A$ over $B$ under the complementary state of the world $X$, then one should always prefer action $A$ over $B$ even when the state of the world is unspecified. Examples of violations of the Sure Thing Principle correspond to the Ellsberg paradox (Ellsberg, 1961), the twostage gambling game (Tversky and Shafir, 1992; Kuhberger et al., 2001; Lambdin and Burdsal, 2007) and the prisoner's dilemma game (Tversky and Shafir, 1992; Croson, 1999; Li and Taplin, 2002; Busemeyer et al., 2006a; Hristova and Grinberg, 2008; Conte et al., 2007b).

In what concerns the prisoner's dilemma game, many works in the literature have been proposed, which formalize the problem in a quantum approach. For instance, Pothos and Busemeyer (2009) proposed a quantum dynamic

Model for the prisoner's dilemma game. In their model, the authors represented the players' beliefs and actions as a superposition in a quantum state vector. When the player knew the information about the opponent's action, the superposition state collapsed into a new state that was compatible with the action chosen by the opponent. When the player did not know about the opponent's move, then the system involved through the application of unitary transformations. In Asano et al. (2010), the authors focus on irrational choices and developed a model based on the quantum superposition and interference principles for the prisoner dilemma game. After each play, the state is updated until it reaches equilibrium. In Cheon and Tahahashi (2010), the authors analyzed quantum conditional probabilities in the prisoner's dilemma game. In Accardi et al. (2009), the authors explored the impact of violations of probability theory in economics and analyze the two-stage gambling game and the prisoner's dilemma game under a quantum probabilistic point of view, by proposing a quantum Model to explain the paradoxical observations in these games. Finally, Asano et al. (2012) proposed a quantum Bayesian updating scheme based on the formalisms of quantum mechanics that represents mental states on a Hilbert state. Through the usage of projections, they were able to introduce a model that could explain the paradoxical findings of the two-stage gambling game (Tversky and Shafir, 1992). Another similar work that compares Bayes rule to its quantum counterpart corresponds to Busemeyer and Trueblood (2009).

### 7.3 Conjunction / Disjunction Errors

There are also many situations where it is verified either a conjunction or a disjunction fallacy. A conjunction error occurs when it is assumed that specific conditions are more probable than a single general one. A disjunction error, on the other hand, consists in assuming that the disjunction of two events is at least as likely as either of the events individually. Several works in the literature used quantum probabilistic models to address these fallacies. For instance, Franco (2009) developed a quantum probabilistic model to explain fallacies when making preferences over a set of events, more specifically, the conjunction fallacy. Busemeyer et al. (2011) also focused on quantum models to

explain conjunction and Croson (1999) focused on disjunction fallacies. The first experiments where these fallacies were observed to occur were performed by Tversky and Shafir (1992). An alternative model for conjunction and disjunction errors correspond to Tversky and Koehler (1994). The authors used support theory as a subjective probabilistic model that describes the way people make probability judgments. The main problem of their model is that support theory is able to successfully describe conjunction errors, but fails at explaining disjunction errors. Other models correspond to Gigerenzer and Hoffrage (1995); Gigerenzer and Goldstein (1996). Khrennikov (2006) also modeled mental processes through quantum probabilities, where the interference process plays an important role in the process of recognizing images (Conte et al., 2009).

## 8 Concluding Comments and Answers to Research Questions

In this work, we showed that it is possible to use quantum interference effects to model meaningful connected acausal events in a Bayesian Network, through Carl Jung's Synchronicity principle.

Note that Synchronicity is a concept that does not question or compete with the notion of causality. Instead, it maintains that just as events may be connected by a causal line, they may also be connected by meaning. Events attached by meaning do not need to have an explanation in terms of cause and effect. As Jung stated, Synchronicity may be seen as coincidences under the laws of probability theory. However, in the realm of quantum mechanics, prediction becomes uncertain, because very small quantities no longer behave in accordance with natural laws, such as causality (Jung and Pauli, 2012).

We tested our models in an empirical experiment conducted by Busemeyer et al. (2009) and we were able to demonstrate that the proposed quantum Bayesian Network together with the Synchronicity heuristic was able to simulate the results observed by the authors with an error percentage of $3.72 \%$. In the situation for the Wide faces in which the law of total probability was not being violated, we managed to reproduce the observed value with a $15.38 \%$ error.

In Section 1.3, we established a set of research questions that we would like to address with the present research work. Their answers are detailed below.

1. What is the meaning of quantum parameters in the realm of quantum cognitive systems?
When presented with a problem, in our mind, we perform a semantic categorization of the symbols that we extract from the given problem. When trying to perform inferences, these symbols which will be taken into account in our thoughts, have to be correlated somehow. Since our thoughts are abstract, cause/effect relationships might not be the most appropriate mechanisms to simulate interferences between them. The Synchronicity principle seems to fit more in this context, since our thoughts can relate to each other from meaningful connections, rather than cause/effect relationships.

In this sense, the quantum parameters that arise from interference effects, although under quantum mechanics they represent the shift of energy waves, in the realm of quantum cognition, they might represent the correlation between events (thoughts) in a meaningful acausal relationship.
2. What is the advantage of the proposed approach? How can it make a difference towards the current well established quantum models that have been proposed in the literature?
The proposed quantum Bayesian Network with the Synchronicity heuristic is one of the few works proposed in the literature, that attempts to provide a general model to automatically compute a set of quantum free parameters. It is a simple and general model that achieved competitive results towards the current state of the art (Section 7). Sections 5.1 and 5.2 demonstrated that classical probabilistic models are unable to perform predictions when the laws of probability are being violated. Moreover, the existing quantum Bayesian Networks do not take into account interference effects, and consequently also fail to make predictions under these circumstances.

The other quantum models that have been proposed (Pothos and Busemeyer, 2009; Khrennikov, 2010; Busemeyer et al., 2009) can only deal with very small problems. They are not

able to scale to cognitive or decision problems with more than two random variables. Moreover, these models do not provide any insights in how to tune quantum parameters. In the end, their models need to be manually fit in order to make accurate predictions.

## Acknowledgments

This work was supported by national funds through Fundação para a Ciência e a Tecnologia (FCT) with reference UID/CEC/50021/2013 and through the PhD grant SFRH/BD/92391/2013. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript. We would like to thank Professor Jerome Busemeyer for the discussion and valuable suggestions given for this work.

# Appendix 

## An Introduction to Quantum Probability Theory

In this section, we describe the main differences between classical and quantum probability theory through examples. The example analyzed concerns jury duty. Suppose you are a juror and you must decide whether a defendant is guilty or innocent. The following sections describe how the classical and quantum theory geometrically evolve in the inference process. All this analysis is based on the book of Busemeyer and Bruza (2012). Note that there are more differences between the quantum and classical theory. However, for the understanding of this work, only the presented concepts are important. For more information about quantum probability, the reader can refer to Busemeyer and Bruza (2012).

## A. 1 Space

In classical probability theory, events are contained in Sample Spaces. A Sample Space $\Omega$ corresponds to the set of all possible outcomes of an experiment or random trial (DeGroot and Schervish, 2011). For example, when judging whether a defendant is guilty or innocent, the sample space is given by $\Omega=($ Guilty, Innocent $)$.

In quantum probability theory, events are contained in Hilbert Spaces. A Hilbert Space $H$ can be viewed as a generalization and extension of the Euclidean space into spaces with any finite or infinite number or dimensions. It is a vector space defined over complex numbers and offers the structure of a dot product to enable the measurement of angles and lengths (Hirvensalo, 2003). The space is spanned by a set of orthonormal basis vectors $\mathrm{H}=($ \{Guilty $\rangle$, $\mid$ Innocent $\rangle)$. Together, these vectors form a basis for the space. Inferences are then calculated through similarities between vectors and events are defined by feature vectors just like in many cognitive systems (Tversky and Kahneman, 1977; Krumhansl, 1978; Busemeyer and Diederich, 2010).

## A. 2 Events

In classical probability theory, events can be defined by a set of outcomes to which a probability is assigned. They correspond to a subset of the sample space $\Omega$ from which they are contained in. Events can be mutually exclusive and they obey set theory. This means that operations such as intersection or union of events are well defined. Since they respect set theory, the distributive axiom is also defined between sets. In our example, Guilty or Innocent can be seen as two mutually exclusive events.

According to quantum probability theory, events correspond to a subspace spanned by a subset of the basis vectors contained in a complex Hilbert Space. Events can be orthonormal, that is, they can be mutually exclusive. Operations such as intersection and union of events are well defined if the events are spanned by the same set of basis vectors (Busemeyer and Bruza, 2012). In quantum theory, all the events contained in a Hilbert Space are defined through a superposition state which is represented by a state vector $|S\rangle$ comprising the occurrence of all events. In our example, $\mid$ Guilty $\rangle$ and $\mid$ Innocent $\rangle$ correspond to column vectors representing the main axis of the circle in Figure 7 (left). They are defined as follows:
$\mid$ Guilty $\rangle=\left[\begin{array}{l}1 \\ 0\end{array}\right] \quad \mid$ Innocent $\rangle=\left[\begin{array}{l}0 \\ 1\end{array}\right]$
etSSN 1303-5150
www.neuroquantology.com

In the left side of Figure 7, the superposition state $|S\rangle$ can be defined as follows.
$|S\rangle=\frac{e^{i \theta_{G}}}{\sqrt{2}}|G u i l t y\rangle+\frac{e^{i \theta_{I}}}{\sqrt{2}}|I n n o c e n t\rangle$
In Equation 10, one might be wondering what the $\frac{e^{i \theta}}{\sqrt{2}}$ values mean. They are called probability amplitudes. They correspond to the amplitudes of a wave and are described by complex numbers. A complex number is a number that can be expressed in the form $z=a+i b$, where $a$ and $b$ are real numbers and $i$ corresponds to the imaginary part, such that $i^{2}=-1$. Alternatively, a complex number can be described in the form $z=|r| e^{i \theta}$, where $|r|=\sqrt{a^{2}+b^{2}}$. The $e^{i \theta}$ term is defined as the phase of the amplitude and corresponds to the angle between the point expressed by $(a, b)$ and the origin of the plane. Under a quantum mechanical perspective, $\theta$ can also be seen as the shift of a wave. These amplitudes are related to classical probability by taking the squared magnitude of these amplitudes. This is achieved by multiplying the amplitude with its complex conjugate.
$\operatorname{Pr}(G u i l t y)=\left|\frac{e^{i \theta_{G}}}{\sqrt{2}}\right|^{2}=\left(\frac{e^{i \theta_{G}}}{\sqrt{2}}\right) \cdot\left(\frac{e^{i \theta_{G}}}{\sqrt{2}}\right)^{*}=\frac{e^{i \theta_{G}}}{\sqrt{2}} \cdot \frac{e^{-i \theta_{G}}}{\sqrt{2}}=e^{-i\left(\theta_{G}-\theta_{G}\right)}\left(\frac{1}{\sqrt{2}}\right)^{2}=0.5$
In quantum theory, it is required that the sum of the squared magnitudes of each amplitude equals 1. This axiom is called the normalization axiom and corresponds to the classical theory constraint that the probability of all events in a sample space should sum to one.

# A. 3 System State 

A system state is nothing more than a probability function Pr which maps events into probability numbers, i.e., positive real numbers between 0 and 1 .

In classical theory, the system state corresponds to exactly its definition. There is a function that is responsible to assign a probability value to the outcome of an event. If the event corresponds to the sample space, then the system state assigns a probability value of 1 to the event. If the event is empty, then it assigns a probability of 0 . In our example, if nothing else is told to the juror, then the probability of the defendant being guilty is $\operatorname{Pr}(G u i l t y)=0.5$.

In quantum theory, the probability of a defendant being |Guilty $\rangle$ is given by the squared magnitude of the projection of the superposition state $|S\rangle$ to the subspace containing the observed event |Guilty $\rangle$. Figure 7 (right) shows an example. If nothing is told to the juror about the guiltiness of a defendant, then, according to quantum theory, we start with a superposition state $|S\rangle$.

$$
$$

When someone asks whether the defendant is guilty, then we project the superposition state $|S\rangle$ into the relevant subspace, in this case the |Guilty $\rangle$ subspace $S_{G}$, just like shown in the right side of Figure 7. The probability is simply the squared magnitude of the projection, that is:

$$
\operatorname{Pr}(G u i l t y)=\left|S_{G}\right|^{2}=\left|\frac{e^{i \theta_{G}}}{\sqrt{2}}\right|^{2}=0.5
$$

Which has exactly the same outcome as in the classical theory.

Figure 7. of an event in a Hilbert
![img-6.jpeg](img-6.jpeg)
![img-7.jpeg](img-7.jpeg)

An example represented space by a superposition of the states [Guilty)and [Innocent) denoted by the quantum state [S) (left). Geometric representation of a projection into the Guilty subspace, where the superposition state $|S\rangle$ is projected into the [Guilty) subspace $S_{G}$ (right).

# B. Mathematical Derivation of Quantum Interference Terms 

Suppose that events $A_{1}, A_{2}, \ldots, A_{N}$ form a set of mutually disjoint events, such that their union is all in the sample space, $\Omega$, for any other event $B$. Then, the quantum law of total probability can be formulated like in Equation 12.

The quantum law of total probability can be derived through Equation 2 by applying Born's rule (Equation 1):
$\operatorname{Pr}(B)=\left|\sum_{x=1}^{N} e^{i \theta_{x}} \psi_{A_{x}} \psi_{B \mid A_{x}}\right|^{2} \quad \sum_{x=1}^{N}\left|e^{i \theta_{x}} \psi_{A_{x}}\right|^{2}=1$
For simplicity, we will expand Equation 12 for $\mathrm{N}=3$ and only later we will find the general formula for N events:
$\operatorname{Pr}(B)=\left|e^{i \theta_{1}} \psi_{A_{1}} \psi_{B \mid A_{1}}+e^{i \theta_{2}} \psi_{A_{2}} \psi_{B \mid A_{2}}+e^{i \theta_{3}} \psi_{A_{3}} \psi_{B \mid A_{3}}\right|^{2}$
Next, we compute the magnitude in Equation 13 by multiplying it with its complex conjugate:

$$
\begin{aligned}
\operatorname{Pr}(B)=\left(e^{i \theta_{1}} \psi_{A_{1}} \psi_{B \mid A_{1}}+e^{i \theta_{2}} \psi_{A_{2}} \psi_{B \mid A_{2}}+e^{i \theta_{3}} \psi_{A_{3}} \psi_{B \mid A_{3}}\right)\left(e^{i \theta_{1}} \psi_{A_{1}} \psi_{B \mid A_{1}}+e^{i \theta_{2}} \psi_{A_{2}} \psi_{B \mid A_{2}}\right. \\
\left.+e^{i \theta_{3}} \psi_{A_{3}} \psi_{B \mid A_{3}}\right)
\end{aligned}
$$

Expanding Equation 14,
$\operatorname{Pr}(B)$
$=e^{i \theta_{1}} \psi_{A_{1}} \psi_{B \mid A_{1}} e^{-i \theta_{1}} \psi_{A_{1}} \psi_{B \mid A_{1}}+e^{i \theta_{1}} \psi_{A_{1}} \psi_{B \mid A_{1}} e^{-i \theta_{2}} \psi_{A_{2}} \psi_{B \mid A_{2}}+e^{i \theta_{1}} \psi_{A_{1}} \psi_{B \mid A_{1}} e^{-i \theta_{3}} \psi_{A_{3}} \psi_{B \mid A_{3}}$
$+e^{i \theta_{2}} \psi_{A_{2}} \psi_{B \mid A_{2}} e^{-i \theta_{1}} \psi_{A_{1}} \psi_{B \mid A_{1}}+e^{i \theta_{2}} \psi_{A_{2}} \psi_{B \mid A_{2}} e^{-i \theta_{2}} \psi_{A_{2}} \psi_{B \mid A_{2}}+e^{i \theta_{2}} \psi_{A_{2}} \psi_{B \mid A_{2}} e^{-i \theta_{3}} \psi_{A_{3}} \psi_{B \mid A_{3}}$
$+e^{i \theta_{3}} \psi_{A_{3}} \psi_{B \mid A_{3}} e^{-i \theta_{1}} \psi_{A_{1}} \psi_{B \mid A_{1}}+e^{i \theta_{3}} \psi_{A_{3}} \psi_{B \mid A_{3}} e^{-i \theta_{2}} \psi_{A_{3}} \psi_{B \mid A_{3}}$
$+e^{i \theta_{3}} \psi_{A_{3}} \psi_{B \mid A_{3}} e^{-i \theta_{3}} \psi_{A_{3}} \psi_{B \mid A_{3}}$
Simplifying Equation 15, we obtain:
$\operatorname{Pr}(B)=\left|e^{i \theta_{1}} \psi_{A_{1}} \psi_{B \mid A_{1}}\right|^{2}+\left|e^{i \theta_{2}} \psi_{A_{2}} \psi_{B \mid A_{2}}\right|^{2}+\left|e^{i \theta_{3}} \psi_{A_{3}} \psi_{B \mid A_{3}}\right|^{2}+\operatorname{Interf}$
In Equation 16, one can see that it is composed by the classical law of total probability and by an interference term. This interference term corresponds to:

$$
\begin{aligned}
& \text { Interf }=e^{i \theta_{1}-i \theta_{2}} \psi_{A_{1}} \psi_{B \mid A_{1}} \psi_{A_{2}} \psi_{B \mid A_{2}}+e^{i \theta_{2}-i \theta_{1}} \psi_{A_{2}} \psi_{B \mid A_{2}} \psi_{A_{1}} \psi_{B \mid A_{1}}+e^{i \theta_{1}-i \theta_{3}} \psi_{A_{1}} \psi_{B \mid A_{1}} \psi_{A_{3}} \psi_{B \mid A_{3}} \\
& +e^{i \theta_{3}-i \theta_{1}} \psi_{A_{3}} \psi_{B \mid A_{3}} \psi_{A_{1}} \psi_{B \mid A_{1}}+e^{i \theta_{2}-i \theta_{2}} \psi_{A_{2}} \psi_{B \mid A_{2}} \psi_{A_{3}} \psi_{B \mid A_{3}} \\
& +e^{i \theta_{3}-i \theta_{2}} \psi_{A_{3}} \psi_{B \mid A_{3}} \psi_{A_{2}} \psi_{B \mid A_{2}}
\end{aligned}
$$

Knowing that

$$
\cos \left(\theta_{1}-\theta_{2}\right)=\frac{e^{i \theta_{1}-i \theta_{2}}+e^{i \theta_{2}-i \theta_{1}}}{2}
$$

Then, Equation 16 becomes

$$
\begin{aligned}
\operatorname{Pr}(B)=\left|e^{i \theta_{1}} \psi_{A_{1}} \psi_{B \mid A_{1}}\right|^{2}+\left|e^{i \theta_{1}} \psi_{A_{1}} \psi_{B \mid A_{1}}\right|^{2}+\left|e^{i \theta_{1}} \psi_{A_{1}} \psi_{B \mid A_{1}}\right|^{2}+2 \psi_{A_{1}} \psi_{B \mid A_{1}} \psi_{A_{2}} \psi_{B \mid A_{2}} \cos \left(\theta_{1}-\theta_{2}\right) \\
+2 \psi_{A_{1}} \psi_{B \mid A_{1}} \psi_{A_{2}} \psi_{B \mid A_{2}} \cos \left(\theta_{1}-\theta_{3}\right) \\
+2 \psi_{A_{2}} \psi_{B \mid A_{2}} \psi_{A_{3}} \psi_{B \mid A_{3}} \cos \left(\theta_{2}-\theta_{3}\right)
\end{aligned}
$$

Generalizing Equation 18 for $N$ events, the final probabilistic interference formula, derived from the law of total probability, is given by:
$\operatorname{Pr}(B)=\sum_{i=1}^{N}\left|\psi_{A_{i}} \psi_{B \mid A_{i}}\right|^{2}+2 \sum_{i=1}^{N} \sum_{j=i+1}^{N}\left|\psi_{A_{i}} \psi_{B \mid A_{i}}\right|\left|\psi_{A_{j}} \psi_{B \mid A_{j}}\right| \cos \left(\theta_{i}-\theta_{j}\right)$

# C Quantum Inference Problem using the Synchronicity Heuristic 

In this Appendix, it is presented the detailed calculations of the quantum parameters $\theta$ for the Bayesian Networks in Figure 3.

## C. 1 Quantum Inference in Bayesian Networks Using Synchronicity: Narrow Faces

The results observed in the empirical experiments of Busemeyer et al. (2009) can be represented in a Bayesian Network just like it is demonstrated on the left side of Figure 3 for Narrow faces and the right side of the same figure for Wide faces.

Since we only have two variables, categorization and decision, then we will use the proposed Synchronicity heuristic in order to attach a meaningful connection to these variables, besides the cause/effect connection that they share. The semantic network for this situation would be identical to the Bayesian Networks in Figure 3, so there is no need to represent it. We will synchronize the variables Categorization and Decision.

The first step to compute Bayesian inference consists in computing the full joint probability distribution. This corresponds to Equation 8. Table 8 shows the application of the full joint probability distribution formula to the Bayesian Network correspondent to the Narrow face experiment (left side of Figure 3).

One can look at the full joint probability distribution as a superposition of all possible quantum states of the Bayesian Network:

$$
$$


Table 8. Full joint probability distribution. $\operatorname{Pr}(\mathrm{C}, \mathrm{D})$ corresponds to the classical probability and $Q \operatorname{Pr}(C, D)$ corresponds to the respective quantum amplitude.

From the full joint probability distribution, one can easily compute the probability of Attack in the following way (using Equation 9). Note that $\alpha$ corresponds to the normalization factor and corresponds to $\alpha=\left[\operatorname{Pr}_{\text {quantum }}(\text { Attack })+\operatorname{Pr}_{\text {quantum }}(\text { Withdraw })\right]^{-1}$ :

$$
\begin{aligned}
& \operatorname{Pr}_{\text {quantum }}(\text { Attack })=\alpha|\operatorname{QPr}(C=\text { Good }, D=\text { Attack })+Q \operatorname{Pr}(C=\text { Bad }, D=\text { Attack })|^{2} \\
& \operatorname{Pr}_{\text {quantum }}(\text { Attack })=\alpha\left|\sqrt{0.0817} e^{i \theta_{A}}+\sqrt{0.5103} e^{i \theta_{C}}\right|^{2} \\
& \operatorname{Pr}_{\text {quantum }}(\text { Attack }) \\
& =\alpha\left[\left|\sqrt{0.0817} e^{i \theta_{A}}\right|^{2}+\left|\sqrt{0.5103} e^{i \theta_{A}}\right|^{2}\right. \\
& \left.+2\left|\sqrt{0.0817} e^{i \theta_{A}}\right|\left|\sqrt{0.5103} e^{i \theta_{A}}\right| \cos \left(\theta_{A}-\theta_{C}\right)\right] \\
& \operatorname{Pr}_{\text {quantum }}(\text { Attack })=\alpha\left[0.5920+0.4084 \cos \left(\theta_{A}-\theta_{C}\right)\right]
\end{aligned}
$$

In order to determine the normalization factor $\alpha$, one needs to compute the probability $\operatorname{Pr}_{\text {quantum }}$ (Withdraw) in the same way:

$$
\begin{aligned}
& \operatorname{Pr}_{\text {quantum }}(\text { Withdraw })=\alpha|\operatorname{QPr}(C=\text { Good }, D=\text { Withdraw })+Q \operatorname{Pr}(C=\text { Bad }, D=\text { Withdraw })|^{2} \\
& \operatorname{Pr}_{\text {quantum }}(\text { Withdraw })=\alpha\left|\sqrt{0.1083} e^{i \theta_{B}}+\sqrt{0.2997} e^{i \theta_{D}}\right|^{2}
\end{aligned}
$$

$$
\begin{aligned}
& \operatorname{Pr}_{\text {quantum }}(\text { Withdraw }) \\
& =\alpha\left[\left|\sqrt{0.1083} e^{i \theta_{B}}\right|^{2}+\left|\sqrt{0.2997} e^{i \theta_{D}}\right|^{2}\right. \\
& \left.+2\left|\sqrt{0.1083} e^{i \theta_{B}}\right|\left|\sqrt{0.2997} e^{i \theta_{D}}\right| \cos \left(\theta_{B}-\theta_{D}\right)\right] \\
& \operatorname{Pr}_{\text {quantum }}(\text { Withdraw })=\alpha\left[0.4080+0.3603 \cos \left(\theta_{B}-\theta_{D}\right)\right]
\end{aligned}
$$

# C.1.1 Application of the Synchronicity Heuristic 

In order to compute the probability of Attack, we used the first and the third rows of the full joint probability distribution (Table 8). The first row corresponds to the situation where both variables occur: Categorization = Good and Decision = Attack. The third row corresponds to the situation where only one of the variables occurs: Categorization = Bad (not good) and Decision = Attack. According to the proposed synchronicity heuristic, these situations can be represented by the Hilbert space on the left side of Figure 8. In order to compute the $\theta$ associated to the probability of making a Withdraw action, the same process is used and corresponds to the Hilbert space representation on the right of Figure 2.
![img-8.jpeg](img-8.jpeg)

Figure 8. Representation of the Synchronicity heuristic in the Hilbert Space. Vector $i$ corresponds to the event $C=$ Good, $D=$ Attack. Vector $j$ corresponds to the event $C=B a d, D=$ Attack. The computed angle for the Attack (left) and Withdraw (right) actions is $\theta=3 \pi / 4$.

Following Figure $8, \theta$ should be equal to $3 \pi / 4$ :
$\operatorname{Pr}_{\text {quantum }}(\text { Attack })=\alpha[0.5920+0.4084 \cos (3 \pi / 4)]=\alpha 0.3032$

$\operatorname{Pr}_{\text {quantum }}(\text { Withdraw })=\alpha[0.4080+0.3603 \cos (3 \pi / 4)]=\alpha 0.1532$
Then, we can compute the normalization factor $\alpha$ and arrive at the final probabilities.
$\alpha=\frac{1}{\operatorname{Pr}_{\text {quantum }}(\text { Attack })+\operatorname{Pr}_{\text {quantum }}(\text { Withdraw })}=\frac{1}{0.4564}$
$\operatorname{Pr}_{\text {quantum }}(\text { Attack })=\frac{0.3032}{0.4564}=0.6643 \quad \operatorname{Pr}_{\text {quantum }}(\text { Withdraw })=\frac{0.1532}{0.4564}=0.3357$
The probabilities computed using the classical probability theory are the following:
$\operatorname{Pr}_{\text {classic }}(\text { Attack })=0.5920 \quad \operatorname{Pr}_{\text {classic }}(\text { Wthdraw })=0.5920$
The probability of deciding an Attack that was observed in the experiments of Busemeyer et al. (2009) was 0.69 . Using a quantum Bayesian Network together with the synchronicity heuristic, we were able to simulate a similar result with a percentage error of $3.72 \%$. In the Quantum Dynamical Model proposed in Busemeyer et al. (2009), the authors predicted $\operatorname{Pr}($ Attack $)=0.74$, which corresponds to an error percentage of $7.25 \%$.

# C. 2 Quantum Inference in Bayesian Networks Using Synchronicity: Wide Faces 

In order to perform quantum inference in the experiment with Wide faces, we proceed in a similar way as before, by computing the full joint probability distribution of the Bayesian Network on the right side of Figure 3. As before, the full joint probability distribution can be mapped into a superposition state (Equation 33).
$|S\rangle=\sqrt{0.2952} e^{i \theta_{A}}|G A\rangle+\sqrt{0.5248} e^{i \theta_{B}}|G W\rangle+\sqrt{0.0954} e^{i \theta_{C}}|B W\rangle+\sqrt{0.0846} e^{i \theta_{D}}|B W\rangle$
From this superposition state, one can easily compute the probability of Attack in the following way (using Equation 9).
$\operatorname{Pr}_{\text {quantum }}(\text { Attack })=\alpha|\operatorname{QPr}(C=\text { Good }, D=\text { Attack })+Q \operatorname{Pr}(C=\text { Bad }, D=\text { Attack })|^{2}$
$\operatorname{Pr}_{\text {quantum }}(\text { Attack })=\alpha\left|\sqrt{0.2952} e^{i \theta_{A}}+\sqrt{0.0954} e^{i \theta_{C}}\right|^{2}$
$\operatorname{Pr}_{\text {quantum }}$ (Attack)

$$
\begin{aligned}
& =\alpha\left[\left|\sqrt{0.2952} e^{i \theta_{A}}\right|^{2}+\left|\sqrt{0.0954} e^{i \theta_{A}}\right|^{2}\right. \\
& \left.+2\left|\sqrt{0.2952} e^{i \theta_{A}}\right|\left|\sqrt{0.0954} e^{i \theta_{A}}\right| \cos \left(\theta_{A}-\theta_{C}\right)\right]
\end{aligned}
$$

$\operatorname{Pr}_{\text {quantum }}$ (Attack) $=\alpha\left[0.3906+0.0563 \cos \left(\theta_{A}-\theta_{C}\right)\right]$
In order to determine the normalization factor $\alpha$, one needs to compute the probability $\operatorname{Pr}_{\text {quantum }}$ (Withdraw) in the same way:

$$
\begin{aligned}
& \operatorname{Pr}_{\text {quantum }}(\text { Withdraw }) \\
& =\alpha|Q \operatorname{Pr}(C=\text { Good }, D=\text { Withdraw })+Q \operatorname{Pr}(C=\text { Bad }, D=\text { Withdraw })|^{2} \\
& \operatorname{Pr}_{\text {quantum }}(\text { Withdraw })=\alpha\left|\sqrt{0.5248} e^{i \theta_{B}}+\sqrt{0.0846} e^{i \theta_{D}}\right|^{2} \\
& \operatorname{Pr}_{\text {quantum }}(\text { Withdraw }) \\
& =\alpha\left[\left|\sqrt{0.5248} e^{i \theta_{B}}\right|^{2}+\left|\sqrt{0.0846} e^{i \theta_{D}}\right|^{2}\right. \\
& \left.+2\left|\sqrt{0.5248} e^{i \theta_{B}}\right|\left|\sqrt{0.0846} e^{i \theta_{D}}\right| \cos \left(\theta_{B}-\theta_{D}\right)\right]
\end{aligned}
$$

$\operatorname{Pr}_{\text {quantum }}(\text { Withdraw })=\alpha\left[0.6094+0.0888 \cos \left(\theta_{B}-\theta_{D}\right)\right]$

# C.2.1 Application of the Synchronicity Heuristic 

Just like before, to compute the probabilities of deciding an Attack, we used the first and the third rows of the full joint probability distribution in Table 8, representing the situations ( $C=$ Good, $D=$ Attack) and ( $C=B a d, D=$ Attack). In order to accommodate the law of total probability, the synchronicity heuristic needs to be applied. These situations are the same as the ones represented in the Narrow Faces (Figure 8). So the angle $\theta$ should be again: $3 \pi / 4$.
$\operatorname{Pr}_{\text {quantum }}(\text { Attack })=\alpha[0.3906+0.3356 \cos (3 \pi / 4)]=\alpha 0.1533$
$\operatorname{Pr}_{\text {quantum }}(\text { Withdraw })=\alpha[0.6094+0.4214 \cos (3 \pi / 4)]=\alpha 0.3114$
Knowing that:
$\alpha=\frac{1}{\operatorname{Pr}_{\text {quantum }}(\text { Attack })+\operatorname{Pr}_{\text {quantum }}(\text { Withdraw })} \frac{1}{0.4647}$
$\operatorname{Pr}_{\text {quantum }}(\text { Attack })=\frac{0.1533}{0.4647}=0.3300 \quad \operatorname{Pr}_{\text {quantum }}(\text { Withdraw })=\frac{0.3114}{0.4647}=0.6700$
For the Wide faces experiment, one obtained a difference of just 0.06 between the computed value and the classical probability value, corresponding to an error of $15.38 \%$. This means that the proposed model can also simulate the empirical results that were observed to converge to the classical probability theory in the experiments of Busemeyer et al. (2009).
$\operatorname{Pr}_{\text {classic }}(\text { Attack })=0.3906 \quad \operatorname{Pr}_{\text {classic }}(\text { Wthdraw })=0.6094$
