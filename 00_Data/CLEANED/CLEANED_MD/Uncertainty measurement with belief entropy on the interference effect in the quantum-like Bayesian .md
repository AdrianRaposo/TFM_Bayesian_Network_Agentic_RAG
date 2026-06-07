# Uncertainty measurement with belief entropy on interference effect in Quantum-Like Bayesian Networks 

Zhiming Huang ${ }^{\mathrm{a}}$, Lin Yang ${ }^{\mathrm{b}}$, Wen Jiang ${ }^{\mathrm{a}, *}$<br>${ }^{a}$ School of Electronic and Information, Northwestern Polytechnical University, Xi'an 710072, China<br>${ }^{b}$ China Equipment System Engineering Company, Beijing, 100039


#### Abstract

Social dilemmas have been regarded as the essence of evolution game theory, in which the prisoner's dilemma game is the most famous metaphor for the problem of cooperation. Recent findings revealed people's behavior violated the Sure Thing Principle in such games. Classic probability methodologies have difficulty explaining the underlying mechanisms of people's behavior. In this paper, a novel quantum-like Bayesian Network was proposed to accommodate the paradoxical phenomenon. The special network can take interference into consideration, which is likely to be an efficient way to describe the underlying mechanism. With the assistance of belief entropy, named as Deng entropy, the paper proposes Belief Distance to render the model practical. Tested with empirical data, the proposed model is proved to be predictable and effective.


Keywords:
Bayesian Networks; Quantum Probability;Decision Making; Social dilemmas; belief entropy; Sure Thing Principle

[^0]
[^0]:    *Corresponding author: Wen Jiang, School of Electronics and Information, Northwestern Polytechnical University, Xi'an, Shannxi 710072, China. Tel: +862988431267. E-mail: jiangwen@nwpu.edu.cn.

# 1. Introduction 

Prisoner's dilemma game is a famous metaphor for the problem of cooperation, which is a critical issue in evolutionary game theory [8, 47]. If two players all defect, the payoff will be lower than if they all cooperates, as shown in Table 1. The paradoxical findings are shown in Table 2 , where the unknown part is not equal to the last column. The violation of The Sure thing Principle [57] shows humans break the law of classic probability when making decision under risk [12]. Many analytical mythologies have been made to the explanation of this phenomenon but the underlying mechanisms are still enigmatic. Nevertheless, the quantum theory seems to be a practical method to uncover the mystery lying behind this incredible phenomenon $[4,32]$.

The quantum theory has been applied in many filed including information theory [38], decision making system [49, 50], social and information networks [46, 51]. Busemeyer et al. [5, 33] proposed a Quantum Dynamical model based on a quantum version of a classical dynamical Markov model, which takes the process of making decisions into account of time evolution. The quantum-like approach developed by Khrennikov [21] is based on contextual probabilities which can be applied to many domains like cognitive science economics, game theory, etc [20, 22, 23]. Masanari et al. [1, 2] proposed a quantum-like model to simulate the brain function.Li et al. [26] proposed a quantum strategies into evolutionary games.

Though there are many models based on quantum probability theory, few of them are predictable. Inspired by the work [13, 30, 35], we propose a novel Bayesian Networks model based on quantum probability. This paper does not consider the noise effect in the quantum information systems [36, 37]. In this model, the violation of rational decision making in many experiments like Prisoner's dilemma game and the Two Stage Gambling game is characterized as interference effect between competing states. This paper regards

Table 1: Payoffs table


man's mental beliefs as wave functions. Before the final decision is made, all potential decisions coexists in man's mind. Such uncertainty is like superposition state of wave functions [29]. The interference effect is actually influenced by the partiality of the man towards to the decisions. Once the interference effect is determined, the man's behavior can be predicted and described by quantum probability theory. This paper proposes Belief Distance to measure the uncertainty with the assistance of belief entropy, named as Deng entropy. Uncertainty processing in decision making was firstly developed by Michle and Jean Yves [7] and the uncertainty can be measured based on distance [9, 28]. The knowledge to the uncertainty in decision making can help psychologists predict the behavior of humans with few fit errors. With the ability to compute the uncertainty of decision, the proposed model is predictable and simple for calculating.

# 2. Organization of this paper 

This paper is organized in the following manner. In section 3, basic mathematical preliminaries will be introduced. In this section, a kind of belief entropy, called Deng entropy, will be introduced, which plays an important role in the model. After that the Bayesian model based on quantum probability will be presented in section 4. Numerical examples will be illustrated in section to show how this model works. In the end, the proposed model will be compared with two models proposed in other literature to show its effectiveness.

Table 2: Experiment results of Prisoner's dilemma game from literature[30]


${ }^{1}$ The second column (Known to Defect) means the probability of the second player choose to betray when he/she knows the first player has chosen to betray. The third column(Known to Collaborate) means the probability of the second player choose to betray when he/she knows the first player has chosen to cooperate. The fourth column (Unknown) means the probability of the second player choose to betray without any information about the first player's action. The final column(Classical probability) means the probability calculated by the classic probability theory.

# 3. Preliminaries 

### 3.1. Belief Entropy

Many contributions [42-44] have been made to interpret quantum probability into Dempster-Shafer probability, in which basic belief assignment is used to describe the probability of an event[39, 58]. A new belief entropy, named as Deng entropy [11] is a measure of uncertainty of basic belief assignment $[10,19]$. Basic belief assignment(BBA) is widely used in the field of information fusion $[14,15,45]$ which has been applied in many fields like Failure Mode and Effect Analysis [16, 18], Fault Diagnose [17, 52] and so on.

Definition 3.1. Let $\theta=\left\{H_{1}, H_{2}, \ldots, H_{N}\right\}$ be a finite nonempty set of $N$ elements which is mutually exclusive and exhaustive. Denote $P(\theta)$ as the power set composed of $2^{N}$ elements of $\theta$. The basic belief assignments(BBAs) function is defined as a mapping of the power set $P(\theta)$ to the value between 0 and 1. $m: P(\theta) \rightarrow[0,1]$, which satisfies the following conditions:

$$
\begin{aligned}
& m(\emptyset)=0 \\
& \sum_{A \subseteq P(\theta)} m(A)=1
\end{aligned}
$$

where the mass $m(A)$ represents the support degree of evidence to event $A$.
Shannon entropy, also named as information entropy, is the expected value of the information contained in each message which can be modeled by any flow of information.

Definition 3.2. The Shannon entropy is defined as follows:

$$
H=-\sum_{i} P_{i} \log _{b} P_{i}
$$

where $P_{i}$ satisfies $\sum_{i} P_{i}=1, b$ is base of logarithm. When $b=2$, the unit of Shannon entropy is bit.

The Belief entropy, named as Deng entropy, is introduced here to measure the uncertainty degree of BBAs, which is defined by:

# Definition 3.3. 

$$
E_{d}=-\sum_{i} m(A) \log \frac{m(A)}{2^{|A|}-1}
$$

Where $m$ is the BBAs function, and $A$ is the element of $P(\theta),|A|$ is the cardinality of $A$. When $|A|$ is equal to 1 , the belief entropy will degenerate into Shannon entropy. The term $2^{|A|}-1$ represents the potential states in $A$.

Example 1 Assume there is a BBAs function $\mathrm{m}(\mathrm{a})=1$. The Shannon entropy and Deng entropy are computed as follows:

$$
\begin{aligned}
& H=-1 \times \log _{2} 1=0 \\
& E_{d}=-1 \times \log _{2} \frac{1}{2^{1}-1}=1
\end{aligned}
$$

This example shows if $|A|$ is equal to 1 , the belief entropy is similar with the classic Shannon entropy.

Example 2 Given a set $\Theta=\{a, b, c\}$ with $m(\{a\})=\frac{1}{2}$ and $m(\{b, c\})=\frac{1}{2}$. The Deng entropy will be:

$$
E_{d}=-\frac{1}{2} \times \log _{2} \frac{\frac{1}{2}}{2^{2}-1}
$$

The above examples show how Deng entropy works and overcomes the insufficiency of Shannon entropy when measuring the uncertainty in problems like Example 2.

### 3.2. The Classic Bayesian Network and the Quantum-like Bayesian Model

### 3.2.1. Classic Bayesian Network

A classic Bayesian Network is a kind of probabilistic directed acyclic graphical model, which has been successfully applied in the field of decision

![img-0.jpeg](img-0.jpeg)

Figure 1: An example of Bayesian Network
making [31]. In this model, a set of random variables and their conditional dependencies are represented via a directed acyclic graph. Each node that represents a variable is associated with a conditional probability table, as shown in Fig.1.

Definition 3.4. The full joint distribution of a Bayesian Network is defined by:

$$
\operatorname{Pr}\left(X_{1}, X_{2} \ldots, X_{n}\right)=\prod_{i=1}^{n} \operatorname{Pr}\left(X_{i} \mid \operatorname{Parents}\left(X_{i}\right)\right)
$$

where $X$ is the list of variables, Parents $\left(X_{i}\right)$ means nodes pointing to $X_{i}$. The model can answer any query with response of yes or no by using conditional probability formula and summing over all nuisance variables. For some query $X$, the inference is given by Eq.(5)

$$
\begin{gathered}
\operatorname{Pr}(X \mid e)=\alpha\left[\sum_{y \in Y} \operatorname{Pr}(X, e, y)\right] \\
\text { where } \alpha=\frac{1}{\sum_{x \in X} \operatorname{Pr}_{c}(X=x, e)}
\end{gathered}
$$

where $e$ is the list of observed variables (nodes) and $y$ is the remaining unobserved variables(nodes) in the network, the $\alpha$ is the normalization factor

for the distribution $\operatorname{Pr}(X \mid e)$ [34].
Example: Fig. 1 shows an example of Bayesian Network. Assume there are two servers $S 1$ and $S 2$ transmitting data packets to User. Apparently, the parent nodes of User are $S 1$ and $S 2$ and the parent node of $S 2$ is $S 1$. Each node has a conditional probability table which represents if a packet is transmitted successfully. If there is a query, for example, what is the probability when user successively receives one data packet. The inference is computed by Eq.(5) as follows:

$$
\begin{aligned}
& \operatorname{Pr}(\text { One Packet })=\alpha\{\operatorname{Pr}(S 2=T \mid S 1=F) * \operatorname{Pr}(S 1=F) \\
& +\operatorname{Pr}(S 2=F \mid S 1=T) * \operatorname{Pr}(S 1=T)\}=\alpha(0.3 * 0.1+0.3 * 0.9)=0.3 \alpha \\
& \operatorname{Pr}(\text { two or zero Packets })=\alpha\{\operatorname{Pr}(S 2=T \mid S 1=T) * \operatorname{Pr}(S 1=T) \\
& +\operatorname{Pr}(S 2=F \mid S 1=F) * \operatorname{Pr}(S 1=F)\}=\alpha(0.7 * 0.9+0.7 * 0.1)=0.7 \alpha \\
& \alpha=\frac{1}{\operatorname{Pr}(\text { One Packet })+\operatorname{Pr}(\text { two or zero Packets })}=1
\end{aligned}
$$

The above example shows the basic idea of Bayesian network and procedure of deriving inferences according to some queries.

# 3.2.2. Quantum-like Bayesian Model 

Bayesian networks can split complex problem into small modules that can be combined to perform inferences [3, 24]. The quantum-like Bayesian Model [30] replaces the real probability numbers in the classic probability Bayesian Network model with quantum probability amplitudes [25, 41].

The corresponding part of quantum-like Bayesian Network model to the application of Born's rule to Eq.(4) is:

$$
\operatorname{Pr}\left(X_{1}, \ldots, X_{n}\right)=\left|\prod_{i=1}^{n} \psi\left(X_{i} \mid \operatorname{Parents}\left(X_{i}\right)\right)\right|^{2}
$$

The quantum application of Born's rule to the classic marginal probability distribution Eq.(5) is defined by the equation below:

$$
\begin{gathered}
\operatorname{Pr}(X \mid e)=\partial\left|\sum_{Y} \prod_{x}^{N} \psi\left(X_{x} \mid \operatorname{Parents}\left(X_{x}\right), e, y\right)\right|^{2} \\
\text { Where } \quad \partial=\frac{1}{\sum_{x \in X} \operatorname{Pr}_{c}(X=x, e)}=1
\end{gathered}
$$

A quantum marginalization formula with interference effects [29] emerges when the Eq.(8) expands, as shown in below,

$$
\begin{aligned}
& \operatorname{Pr}(X \mid e)=\partial \sum_{i=1}^{|Y|} \left\lvert\, \prod_{x}^{N} \psi\left(X_{x} \mid \operatorname{Parents}\left(X_{x}\right), e, y=i\right)\right|^{2}+2 \cdot \text { Interference } \\
& \text { Interference }=\sum_{i=1}^{|Y|-1} \sum_{j=i+1}^{|Y|} \left\lvert\, \prod_{x}^{N} \psi\left(X_{x} \mid \operatorname{Parents}\left(X_{x}\right), e, y=i\right)\right. \mid \\
& \quad \left\lvert\, \prod_{x}^{N} \psi\left(X_{x} \mid \operatorname{Parents}\left(X_{x}\right), e, y=j\right)\right| \cdot \cos \left(\theta_{i}-\theta_{j}\right)
\end{aligned}
$$

Example: Fig. 2 shows an instance of Quantum-like Bayesian Network.
This network can only answer queries with yes or no answer, which are regarded as base vectors $\mid 0>$ and $\mid 1>$. Fig. 3 shows any actions the node will take can be seen as wave functions characterized by base vectors $\mid 0>$ and $\mid 1>$, as defined by:

$$
\begin{aligned}
& \left|T>=\cos \theta_{T}\right| 1>+\sin \theta_{T}\left|0>=\right. e^{j \theta_{T}} \\
& \left|F>=\cos \theta_{F}\right| 1>+\sin \theta_{F}\left|0>=\right. e^{j \theta_{F}}
\end{aligned}
$$

Thus, the decision vector for node $A$ is defined by:

$$
\left|\phi_{A}>=\psi_{A=T}\right| \mathrm{T}_{A}>+\psi_{A=F}\left|F_{A}>=\psi_{A=T} \cdot e^{j \theta_{T_{A}}}+\psi_{A=F} \cdot e^{j \theta_{F_{A}}}\right.
$$

![img-1.jpeg](img-1.jpeg)

Figure 2: An example of a Quantum-like Bayesian Network
where the action states $\mid F_{A}>$ and $\mid T_{A}>$ means the actions the node can take. The index $A$ in $\mid F_{A}>$ and $\mid T_{A}>$ represents this decision is made by node $A$.

In the same way, Decision vector for node $B$ is

$$
\left|\phi_{B}>={\psi_{B=T}} \mid \mathrm{T}_{B}>+\psi_{B=F} \mid F_{B}>={\psi_{B=T}} \cdot e^{j \theta_{T_{B}}}+\psi_{B=F} \cdot e^{j \theta_{F_{B}}}\right.
$$

For a query "what is the probability for B to adopt action T ?", the inference is computed by Eq.(8):

$$
\begin{aligned}
\operatorname{Pr}(T \mid A)= & \partial\left|\psi_{B=T} \cdot e^{j \theta_{T_{B}}} \cdot \psi_{A=T} \cdot e^{j \theta_{T_{A}}}+\psi_{B=T} \cdot e^{j \theta_{T_{B}}} \cdot \psi_{A=F} \cdot e^{j \theta_{F_{A}}}\right|^{2} \\
= & \partial\left|\psi_{B=T} \cdot \psi_{A=T} \cdot e^{j \theta_{1}}+\psi_{B=T} \cdot \psi_{A=F} \cdot e^{j \theta_{2}}\right|^{2} \\
= & \partial\left|\psi_{B=T} \cdot \psi_{A=T} \cdot e^{j \theta_{1}}+\psi_{B=T} \cdot \psi_{A=F} \cdot e^{j \theta_{2}}\right| \\
& \cdot\left|\psi_{B=T} \cdot \psi_{A=T} \cdot e^{j \theta_{1}}+\psi_{B=T} \cdot \psi_{A=F} \cdot e^{j \theta_{2}}\right|^{*} \\
= & \partial\left|\psi_{B=T} \cdot \psi_{A=T}\right|^{2}+\left|\psi_{B=T} \cdot \psi_{A=F}\right|^{2} \\
& + \psi_{B=T} \cdot \psi_{A=T} \cdot e^{j \theta_{1}} \cdot \psi_{B=T} \cdot \psi_{A=F} \cdot e^{-j \theta_{2}} \\
& +\psi_{B=T} \cdot \psi_{A=F} \cdot e^{j \theta_{2}} \cdot \psi_{B=T} \cdot \psi_{A=T} \cdot e^{-j \theta_{1}} \\
= & \partial\left|\psi_{B=T} \cdot \psi_{A=T}\right|^{2}+\left|\psi_{B=T} \cdot \psi_{A=F}\right|^{2}+ \\
& 2 \cdot\left|\psi_{B=T} \cdot \psi_{A=T} \cdot \psi_{B=T} \cdot \psi_{A=F}\right| \cdot \cos \left(\theta_{1}-\theta_{2}\right)
\end{aligned}
$$

$$
\begin{aligned}
\operatorname{Pr}(F \mid A)= & \partial\left|\psi_{B=F} \cdot \psi_{A=T}\right|^{2}+\left|\psi_{B=F} \cdot \psi_{A=F}\right|^{2}+ \\
& 2 \cdot\left|\psi_{B=F} \cdot \psi_{A=T} \cdot \psi_{B=F} \cdot \psi_{A=F}\right| \cdot \cos \left(\theta_{3}-\theta_{4}\right)
\end{aligned}
$$

where $\theta_{1}=\theta_{T_{B}}+\theta_{T_{A}}, \theta_{2}=\theta_{T_{B}}+\theta_{F_{A}}, \theta_{3}=\theta_{F_{B}}+\theta_{T_{A}}, \theta_{4}=\theta_{F_{B}}+\theta_{F_{A}}$.
Therefore, the answer to query is $\operatorname{Pr}(T \mid A)$ once the $\partial$ is determined by Eq.(9). This example illustrates the definition of Quantum-like Bayesian Network and the detail derivation of Eq.(10).

# 4. The proposed model 

Unlike the method in the literature [30], this paper proposes a new way to calculate the interference value in the quantum-like Bayesian Network model. The biggest difference is this paper replaces the term $\cos \left(\theta_{i}-\theta_{j}\right)$ in Eq.(10) with the uncertainty degree value $E_{d}$ calculated by Deng entropy. Deng entropy, also named as Belief entropy, is a powerful tool to measure the belief degree. The term $\cos \left(\theta_{i}-\theta_{j}\right)$ in Eq.(10) is a degree of belief uncertainty in the quantum interference term. When prisoner has no information about the other prisoner, his/her decision is influenced by his/her belief about the rival's decision. That's why the classic probability framework can not describe the game properly because to some extant the prisoner is not totally "ignorant" about the other prisoner but has his/her own belief about the other part. This uncertain belief causes the interference term in the Bayesian Network model, which seems to be variable because the human's mind is changeable and is hard to measure. However, many experiments in literatures have revealed that the human's belief was inclined to certain degree, which means the interference term has a tendency value. Once the degree of belief uncertainty could be measured, the model can be established to describe the behavior that violates the Sure Thing Principle. Here the Deng entropy is introduced to measure the belief degree and the results turns out to be fit for the model to describe the game.

# 4.1. Acquisition of Belief Degree 

This paper presents such a concept that the existing of interference term is because the prisoner's belief to the other prisoner. According to the classic probability theory, as analysed in the above section, the probability of a prisoner to defect the other under unknown condition should be equal to $\frac{1}{2}(\operatorname{Pr}(P 2=\operatorname{Defect} \mid P 1=$ Cooperate $)+\operatorname{Pr}(P 2=\operatorname{Defect} \mid P 1=\operatorname{Defect}))$. But the experiment results in literature denied this, which means the interference term truly affects. That's because actually the prisoner is not totally "ignorant" about the other, for he/she will predict the other prisoner's decision from his/her own perspective and then make self's decision. For every individual, every one has his/her own characteristics. When predicting other's decision from self's perspective, the result seems to be diverse. But it is known that there are something that is common for everyone called human nature which results in most people that they tend to have a same predication tendency.

Definition 4.1. Belief Degree is defined by:

$$
D_{b}=\cos \left(\theta_{i}-\theta_{j}\right)
$$

where $\theta_{i}$ and $\theta_{j}$ are angles in interference term in Eq.(10). Belief degree represents people's predication toward their opponents and their belief tendency to certain actions in prisoners' dilemma game.

This predication tendency or Belief Degree determines the value of interference term. According to the previous experiments shown in Table 2, the value of interference term is inclined to a certain value, which means there indeed exists predication tendency or Belief Degree. Hence the Belief Degree can be determined as shown in following.

The quantum marginalization formula comprises two parts, the classic probability term and interference term, as Eq.(10) shows. It is the interference term that equips the model with ability to accommodate the violation

![img-2.jpeg](img-2.jpeg)

Figure 3: vector representation
of Sure Thing Principle. In this section, Deng entropy will be introduced to calculate the belief uncertainty to obtain the interference value. Notice that the Eq.(11) has two basis states, as shown in Fig.3. There always be two vectors representation of Eq.(10), for the variable $X$ has two alternative value, $T$ and $F$.

$$
\left[\begin{array}{c}
\alpha_{T} \\
\beta_{T}
\end{array}\right]=\left[\begin{array}{c}
\psi_{P_{N}=T} \cdot \psi_{P_{\text {Parents }}=T} \\
\psi_{P_{N}=T} \cdot \psi_{P_{\text {Parents }}=F}
\end{array}\right]\left[\begin{array}{c}
\alpha_{F} \\
\beta_{F}
\end{array}\right]=\left[\begin{array}{c}
\psi_{P_{N}=F} \cdot \psi_{P_{\text {Parents }}=T} \\
\psi_{P_{N}=F} \cdot \psi_{P_{\text {Parents }}=F}
\end{array}\right]
$$

Before applying Deng entropy to obtain the uncertain term $\cos \left(\theta_{i}-\theta_{j}\right)$ in the interference term, we should process the data in Eq.(17) firstly. The vector representation of Eq.(17) is shown in Fig.4. As can be inferred from Eq.(14) and Eq.(15), two $\theta$ in the Fig. 4 have the same value. Though we have known the value of two pairs of $\alpha$ and $\beta$, the value of $\theta$ can hardly be determined through existing methods. One possible solution is just to regard $\cos \left(\theta_{i}-\theta_{j}\right)$ as an uncertain variable, which can be replaced by belief degree $D_{b}$. Hence once the belief degree is determined, the interference term is settled. The belief degree can be determined through belief entropy, which can calculate

![img-3.jpeg](img-3.jpeg)

Figure 4: vector representation of $\alpha$ and $\beta$
the uncertainty from Belief Distance.
Definition 4.2. The Belief Distance is defined by:

$$
\begin{aligned}
& B_{d_{X}}=\left|\alpha_{X}+\frac{\alpha_{X}-\beta_{X}}{\left|\alpha_{X}+\beta_{X}-1\right|}\right| \\
& \text { where }\left|\alpha_{X}-0.5\right|<\left|\beta_{X}-0.5\right|
\end{aligned}
$$

If $\left|\alpha_{X}-0.5\right| \geq\left|\beta_{X}-0.5\right|$, the position of $\alpha_{X}$ and $\beta_{X}$ should be switched.
The Belief Distance measuring the deviation from 0.5. If no information is provided, the value of $\alpha$ and $\beta$ would be 0.5 because node A has two actions with each amplitude $\sqrt{5}$ and so does node B. $\frac{\left|\alpha_{X}-\beta_{X}\right|}{\left|\alpha_{X}+\beta_{X}-1\right|}$ is actually a derivation of $\frac{\left|\alpha_{X}-0.5\right|-\left|\beta_{X}-0.5\right|}{\left|\alpha_{X}-0.5\right|+\left|\beta_{X}-0.5\right|}$.

Lemma 4.1. With the relative deviation information provided, Belief degree can be computed by Eq.(18) and Eq.(3):

$$
D_{b}=-E_{d}=\sum_{x} \mathrm{~B}_{d_{x}} \log \frac{\mathrm{~B}_{d_{x}}}{2^{\left|A_{i}\right|}-1}
$$

$\left|A_{i}\right|$ means the number of unobserved variables.

In quantum mechanics, the $\cos \left(\theta_{1}-\theta_{2}\right)$ is given by the inner product between two wave functions[6], which describes the subtraction of phases of the two wave function. Because it is difficult to compute $\cos \left(\theta_{i}-\theta_{j}\right)$ from geometric perspective, this paper just regards it as a variable which can be computed through belief entropy.

# 5. Numerical example 

In this section, the proposed method will be applied in the Bayesian Network model to analyze the average results presented in Table 2. The process could be summarized as below.

Step 1: Create the model for the problem: If nothing is told, the first participant in the Prisoner's dilemma game will choose Defect or Cooperate with probability of 0.5 . The reason we assume the probability equals to 0.5 is that the first participant in the model do not have parents and nothing is told to him/her. However, in the real situation, the participants will wonder the other participant's action and make decisions based on the judgement. Therefore the assumption that the probability 0.5 is uncertain. In the Eq.(19), $\left|A_{i}\right|$ means the number of variables whose decision are not sure. Under this situation, the first participant's decision assumed by us is not exactly certain, so the term $\left|A_{i}\right|$ will equal to 1 . With the data from Table 2, we can establish a model as shown in Fig.5;

Step 2: Compute the Belief distance: According to Fig.5, the Eq.(17) can be paraphrased as below:

$$
\left[\begin{array}{c}
\alpha_{T} \\
\beta_{T} \\
\alpha_{F} \\
\beta_{F}
\end{array}\right]=\left[\begin{array}{c}
\psi_{P_{N}=T} \cdot \psi_{P_{\text {Parents }}=T} \\
\psi_{P_{N}=T} \cdot \psi_{P_{\text {Parents }}=F}
\end{array}\right]=\left[\begin{array}{c}
\sqrt{0.5} \cdot \sqrt{0.26} \\
\sqrt{0.5} \cdot \sqrt{0.13}
\end{array}\right]=\left[\begin{array}{c}
0.3606 \\
0.2550 \\
\sqrt{0.5} \cdot \sqrt{0.74}
\end{array}\right]=\left[\begin{array}{c}
0.6083 \\
0.6595
\end{array}\right]
$$

![img-4.jpeg](img-4.jpeg)

Figure 5: Bayesian Network model for the Prisoners' dilemma game with the average results from Table 2

In this way, one can calculate the belief distance with Eq.(18). Here we take the calculation process of $\alpha_{F}$ and $\beta_{F}$ for example: notice that $\left|\beta_{T}-0.5\right|>$ $\left|\alpha_{T}-0.5\right|$. The Belief Distance for $\alpha_{F}$ and $\beta_{F}$ is:

$$
B_{d_{T}}=\left|0.6083+\frac{0.6083-0.6595}{|0.6083+0.6595-1|}\right|=0.41711
$$

And the Belief distance for $\alpha_{T}$ and $\beta_{T}$ can be computed in the same way:

$$
B_{d_{F}}=\left|0.3606+\frac{0.3606-0.2550}{|0.3606+0.2550-1|}\right|=0.63531
$$

Step 3: Calculate the belief degree using Deng entropy: In the Step 2 we obtain the Belief Distance $B_{d_{T}}$ and $B_{d_{F}}$. The Belief Distance represents the inner connection between two actions decided by the participants, as a reflection of a prisoner's belief to the other. The Deng entropy is an efficient tool to reveal this connection. In Step 1, we have analyzed that the term $\left|A_{i}\right|$ in the Eq.(19) equals to 1 . Hence the results of Eq.(19) is:

$$
D_{b}=-E_{d}=0.41711 \cdot \log \frac{0.41711}{2^{1}-1}+0.63531 \cdot \log \frac{0.63531}{2^{1}-1}=-0.9420
$$

The $D_{b}$ will replace the term $\cos \left(\theta_{i}-\theta_{j}\right)$ in the Eq.(10) to perform the

probabilistic interference.

$$
\begin{aligned}
& \operatorname{Pr}(P 2=\text { Defect })=\partial\left[\left|\psi_{P 2=D \mid P 1=D}\right|^{2}+\left|\psi_{P 2=D \mid P 1=C}\right|^{2}\right. \\
& +2 \cdot\left|\psi_{P 2=D \mid P 1=D}\right| \cdot\left|\psi_{P 2=D \mid P 1=C}\right| \cdot \cos \left(\theta_{1}-\theta_{2}\right) \\
& =\partial[0.5 \times 0.87+0.5 \times 0.74+2 \cdot \sqrt{0.5 \times 0.87} \cdot \sqrt{0.5 \times 0.74} \cdot-0.9420]
\end{aligned}
$$

$\operatorname{Pr}(P 2=$ Cooperate $)$ can be obtained i the same way:

$$
\begin{aligned}
& \operatorname{Pr}(P 2=\text { Defect })=\partial 0.04917 \\
& \operatorname{Pr}(P 2=\text { Cooperate })=\partial 0.02182
\end{aligned}
$$

And the final result is:

$$
\begin{aligned}
& \operatorname{Pr}(P 2=\text { Defect })=\frac{\partial 0.04917}{\partial 0.04917+\partial 0.02182}=0.6926 \\
& \operatorname{Pr}(P 2=\text { Defect })=\frac{\partial 0.02182}{\partial 0.04917+\partial 0.02182}=0.3074
\end{aligned}
$$

Compare the result with probability in Table 2, the model this paper proposes produces a result with fit error percentage of $8.2 \%$.

Fig. 6 shows the comparison of results from literature and prediction of model, from which we can see that the model prediction is coincident to the probability observed with little fit errors.

# 6. Conclusion 

Quantum Bayesian Network inherits inference ability from classic Bayesian network and has the ability to explain the violation of Sure Thing Principle. The model proposed by this paper successfully described the paradoxical phenomenon in Prisoners' dilemma game. Unlike other existing methods, the proposed model regards the violation as an effect of interference and utilizes the concept of "Belief Degree" to make prediction though belief entropy. the model is compared with two other Quantum models. The first model (model 1) is the Quantum Prospect Decision Theory(QPDT) model developed by

![img-5.jpeg](img-5.jpeg)

Figure 6: Comparison of results from the literature and results predicted by the model

Table 3: Comparison between proposed model and other two models in literature


${ }^{\text {Li and Taplin, } 20021}$ we use 3 experiments from literature[37] and number them with 1,2 and 3 after the authors' name.

Yukalov and Sornette[53-56]. In (QPDT) model, a static heuristic is used to predict the results. The second model is the Quantum-Like Bayesian Network proposed by Moreira[30], in which a dynamic heuristic is used to predict the results. From Table 3 we can clearly notice that the average fit errors of proposed model is smaller than other two models, which shows the new method for Quantum Bayesian Network proposed by this paper is effective and reliable. Fig. 7 visualizes the results from Table 2, from which we can see that the result predicted by the proposed method is occupying the least area of the bar.

The dilemma situation considered in this paper is prisoner's dilemma game with two strategies [40]. The dilemma strength [48] of the game dis-

![img-6.jpeg](img-6.jpeg)

Figure 7: Visualization of comparison results
cussed in this paper is $D g^{\prime}=D r^{\prime}=1$. There are also cases with dilemma strength different from $D g^{\prime}=D r^{\prime}=1$, depending on the payoff table to the players. Admittedly, the method proposed in this paper is designed to accommodate the paradoxical findings in dilemma strength $D g^{\prime}=D r^{\prime}=1$. Nevertheless, the method can well predict behaviours the player will take, as shown in Table 3. Comparing with other similar methods, the proposed Bayesian Network works with the least fit errors. In the prisoner's dilemma game, the prisoner will predict the other's action if he/she knows little about the rival. Therefore the probability of the prisoner to choose Defect under unknown case will be smaller than the value computed from the classic way. The Sure Thing Principle is violated because the belief in the prisoner's mind affects. On the other hand, the belief degree is not totally irregular. Lots of evidence have examined the value is closed within a small range. The advantages of Quantum-like Bayesian Network is it regards two strategies in people's mind as two wave functions, which will produce the interference effect. Hence, this paper proposes Belief Degree to represent the interfer-

ence effect and utilizes Belief Distance to calculate the deviation from totally uncertainty. The belief entropy will produce a corresponding Belief Degree according to Belief Distance. We analyze the Prisoners' dilemma game with the model that applied our method and the prediction results are close to the observed probability with little fit error. In the end, we compare the model with two models which use a parameter called heuristic to predict the probability. The comparison results shows the effectiveness and reliability of our method.

# 7. Acknowledgments 

The work is partially supported by National Natural Science Foundation of China (Grant No. 61671384), Natural Science Basic Research Plan in Shaanxi Province of China (Program No. 2016JM6018), Aviation Science Foundation (Program No. 20165553036).
