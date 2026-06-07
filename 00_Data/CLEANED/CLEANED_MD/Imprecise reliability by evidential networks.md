# HIAL open science 

## Imprecise reliability by evidential networks <br> Christophe Simon, Philippe Weber

## To cite this version:

Christophe Simon, Philippe Weber. Imprecise reliability by evidential networks. Proceedings of the Institution of Mechanical Engineers, Part O: Journal of Risk and Reliability, 2009, 223 (2), pp.119-131. 10.1243/1748006XJRR190 . hal-00340044

## HAL Id: hal-00340044 <br> https://hal.science/hal-00340044v1

Submitted on 19 May 2009

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# Imprecise reliability by evidential networks 

Christophe SIMON and Philippe WEBER*<br>October 3, 2008


#### Abstract

This article deals with an implementation of probist reliability problems in evidential networks to propagate imprecise probabilities expressed as fuzzy numbers. First, the problem of imprecise knowledge in reliability problems is described concerning system and data reprsentation. Then, the basics of the evidence theory and its use in a directed acyclic graph approach are given. The imprecise probist reliability of complex system by modelling the component failure probabilities as real, interval or fuzzy numbers is pointed out. Two numerical studies of systems are done. The results are discussed and some comparisons with a Monte-Carlo simulation and a fuzzy fault tree approach are made.


## 1 Introduction

In reliability studies, the probabilities involved are usually considered as precise and perfectly known. It is also supposed that all information on the behaviour of the system and its components concerning reliability. As Utkin wrote [1], this completeness assumes two main conditions:

- All probabilities or probability distributions are known or perfectly determinable.
- The system components are independent, i.e. all random variables which describe the component reliability behaviour are independent or alternatively, their dependence is precisely known.

With real systems, the first condition is seldom fulfilled [1]. Usually, the reliability assessments that are combined to describe systems and components come from various sources. Some information can be objective measures from relative frequencies or well-established models. Other information may be supplied by experts usually incorporating an epistemic uncertainty. In the first case, the probability model should be used $[2,3]$ to tackle this random nature of uncertainty. In the latter case, many uncertainty models can tackle the problem of imprecision. A pure probabilistic framework suggests that all uncertainties whether of a random or an epistemic nature should be represented in the same way. As mentioned by Baudrit and Dubois [4], uncertainties are neither random nor can be objectively quantified and model parameters are often incomplete. As suggested by Ferson or Helton [5, 6] distinct representation methods are needed to adequately tell variability from imprecision. Many representations exist

[^0]
[^0]:    *C. Simon and Ph. Weber are with the Research Centre on Automatic Control of Nancy, Nancyuniversity, CNRS, France.

and it is very difficult to cite all of them. The reader can be interested in papers concerning some of these representations like possibility theory [7], upper and lower probabilities [8], evidence theory [9], imprecise probabilities [10], fuzzy probabilities [11], Neumaier clouds [12] .

Imprecision can affect data for various reasons. Limbourg recounts in [13] that in early product development phases, epistemic uncertainties are encountered with incomplete component data, influencing factors, or vague estimations of failure functions provided by experts. In the same way, Baudrit [4] explains that for time and financial constraints, information regarding model parameters is often incomplete and experts give information according to their experience and intuition. So, a convenient way to represent uncertainty in reliability parameters can be intervals or fuzzy values. It induces reliability models of studied systems to deal with these representations.

To deal with epistemic and random uncertainties, the evidence theory has proven to be a well-suited framework [9]. It has been applied in various fields [14-16] for example in reliability studies [17-19]. This theory is rather close to the probability theory. As specified by Halpern [20, 21], a belief function can formally be defined as a function satisfying axioms which can be viewed as a weakening of the Kolmogorov axioms that characterize probability functions. Thus, it seems reasonable to understand a belief function as a generalized probability function [22].

The goal of this paper is to propose a graphical formalism allowing to model imprecise reliability with certain and uncertain probabilities (real, interval or fuzzy probabilities) and to show how to propagate the random and epistemic uncertainties in reliability models. For this purpose, directed acyclic graphs based on the Dempster-Shafer structure [18] are used. Section 2 defines system reliability models used and the representation of reliability parameters. Section 3 concerns the basics of evidence theory. Section 4 is dedicated to evidential networks and reliability models. Finally, section 5 deals with two numerical experiments and comparisons with a Monte-Carlo simulation and a fuzzy fault tree approach.

# 2 System and data description 

The problem of uncertainty in reliability modelling has led to several approaches defined by Cai [23-25]. To classify these approaches of reliability theories, Cai considers the different types of measures to describe the component behaviour and how to describe the component states. PROBIST reliability concerns systems with two state components and systems (functioning and malfunctioning: BInary STate) and probability measures (PRObability) to characterize the component and system behaviours. PROFUST reliability considers probability measures and fuzzy states. In POSFUST reliability possibility measures and fuzzy states are considered. The last case concerns POSBIST reliability with possibility measures and two state hypotheses. The problems involved in this study concern PROBIST reliability only. The components and the systems are supposed to have binary states with a functioning state $(U p)$ and a failure state (Down).

The data concerning the component performances are obtained from the manufacturer's documentations and are sometimes reinterpreted by experts or directly obtained from experts or from databases. They can take several forms like crisp, interval or fuzzy values depending on their source. As our approach concerns failure probabilities at a precise time, all information concerning the general performance of the components used like failure rates or MTTF should be translated in probabilities according to their

failure distribution. All these probabilities can be interpreted as fuzzy number even if the source provides crisp values or interval valued probabilities which are considered as a special case of fuzzy probabilities [26].

As the main idea of the paper is to handle imprecision on probabilities with fuzzy sets, let us recall some basic elements. A fuzzy set is a class of objects with a continuum of membership grades. Such a set is characterized by a membership function which assigns to each object a grade of membership ranging between 0 and 1 [27]. A fuzzy subset $\widetilde{A}$ on a universal set $U, U \neq \emptyset$ is uniquely determined by its membership function $\mu_{\widetilde{A}}: U \mapsto[0,1][27]$. The value $\mu_{\widetilde{A}}(X)$ represents the membership degree of $x$ to $\widetilde{A}$. The membership degree of an element $u$ of $U$ to $\widetilde{A}$ no longer belongs to $\{0,1\}$ but to the interval $[0,1]$. If $\mu_{\widetilde{A}}(X)=0, x$ does not belong at all to $\widetilde{A}$, if $\mu_{\widetilde{A}}(X)=1$, it belongs to it completely. If $0<\mu_{\widetilde{A}}(X)<1$ then the membership of $x$ to $\widetilde{A}$ is more or less complete.

A set $\operatorname{Supp} A=\left\{X \in U \mid \mu_{\widetilde{A}}(X)>0\right\}$ is called the support of $\widetilde{A}$. A set $\operatorname{Ker} A=$ $\left\{X \in U \mid \mu_{\widetilde{A}}(X)=1\right\}$ is the kernel of $\widetilde{A}$. If the kernel of $\widetilde{A}$ is nonempty $(\operatorname{Ker} A \neq \emptyset), \widetilde{A}$ is known as normalized. The sets $A^{\alpha}=\left\{X \in U \mid \mu_{\widetilde{A}}(X) \geq \alpha\right\}, \alpha \in[0,1]$ are called the $\alpha$-cuts of $\widetilde{A}$. The $\alpha$-cuts of $\widetilde{A}$ are nested, i.e. if $\alpha_{1} \geq \alpha_{2}$ then $A^{\alpha_{2}} \subseteq A^{\alpha_{1}}$.

A normalized fuzzy set $\widetilde{A}$ on the set of all real numbers $\mathbb{R}$ whose $\alpha$-cuts $A^{\alpha}$ are closed intervals and whose support $\operatorname{Supp} A$ is bounded, is called a fuzzy number. A fuzzy number $\widetilde{A}$ is defined on $[a, b]$ if $\operatorname{Supp} A \subseteq[a, b]$. If $x$ is a real continuous variable with membership function $\mu(x) \in[0,1]$, and satisfying the following conditions:

- $\mu(x)$ is piecewise continuous;
- $\mu(x)$ is convex;
- $\mu(x)$ is normalized (at least one value of $x_{0}$ such as $\mu\left(x_{0}\right)=1$ ).

Now, let us consider three real parameters $(m, a, b), m, a$ and $b$ are strictly positives, and two functions, noted $L$ and $R$, are defined on the real set $\mathbb{R}^{+}$, with values in $[0,1]$, upper semi-continuous, such as:

$$
\begin{aligned}
& L(0)=R(0)=1 \\
& L(1)=0 \text { or } \lim _{x \rightarrow m} L(x)=0 \\
& R(1)=0 \text { or } \lim _{x \rightarrow m} R(x)=0
\end{aligned}
$$

A fuzzy number $\widetilde{M}$ is $L-R$ type if its membership function $\mu_{\widetilde{M}}$ is defined by:

$$
\mu_{\widetilde{M}}(x)=\left\{\begin{array}{l}
R((x-m) / b) \text { if } x>m \\
L((m-x) / a) \text { if } x \leq m
\end{array}\right.
$$

Let us note $\widetilde{M}=(m, a, b)_{L R}$ a $L-R$ fuzzy number. $m$ is its modal value with $\mu_{\widetilde{M}}(m)=1, a$ is the left width of its support from $m$, also called the left spread, and $b$ the right width from $m$, also called the right spread, on the real axis (cf. figure 1). $L$ and $R$ are both functions which determine the membership function of $M$ respectively on the left and on the right of $m$. Here, $L$ and $R$ are linear functions.

Hence, to take into account the lack of knowledge on a probability value, a fuzzy probability can be represented by a fuzzy number if $0 \leq(m, a, b) \leq 1$ and $L$ and $R$ are two functions from $[0,1]$ to $[0,1]$. Of course, a probability interval and a singular

![img-0.jpeg](img-0.jpeg)

Figure 1: $L-R$ triangular fuzzy number
probability value are a special case of fuzzy probability and can be represented in the same way for a convenient computation in the same model.

According to the generic representation of imperfect probabilities as fuzzy numbers, the main problem is now to deal with the fuzzy probabilities inside the probist reliability model of the studied systems. A solution can be found by the nested interval valued probabilities according to the $\alpha$-cuts previously described and the evidence theory. The nested intervals represent the imprecision at an $\alpha$-level and the corresponding frames of discernment that support this representation. Then, the propagation of interval valued probabilities through a probist reliability model is solved by directed acyclic graphs supporting the frames of discernment which are called evidential networks.

# 3 Basics of evidence theory 

The evidence theory was initiated by Dempster [22], with his work on upper and lower bounds of a probability distribution family, then reinforced by Shafer [9]. Several models of imperfect data processing were proposed (e.g. upper and lower probabilities [10], the evidence theory [9], the Hint Model [28], the Transferable Belief Model [29]).

On a discrete finite space, the model suggested by Dempster and Shafer can be interpreted as a generalization of the probability theory where probabilities are assigned to sets in opposition to mutually exclusive singletons [30]. In the probability theory, a measure is assigned to only one possible event. On the other hand, in the evidence theory, a measure can be assigned to a set of events. However, when the information available allows the assignment of measures to single events (i.e. specific knowledge), the Dempster-Shafer model merges with the traditional formulation of probabilities. This information is called Bayesian evidence [31]. The closeness between these two models reinforces the interest of the evidence theory for applications initially handled by the probability theory.

### 3.1 Basic mass assignment

The main idea of the basic mass assignment is to allocate a measure between 0 and 1 to indicate the degree of belief about events or assumptions [9]. There may be several interpretations of these measures, which generate controversy on their use. The evidence

theory does not make the assumption of an unknown probability measurement but subjective beliefs based on non-specific information [32]. In the same way, Sentz [30] argues that it is not really a question of probabilities. However, many works are directed towards an objectivist approach of belief functions [33,34]. Thus, the term of basic probability assignment as that of basic mass assignment are both commonly read in the literature [35] to model the same assignment process. The probability theory as well as the evidence theory offers either an objectivist point of view or a subjectivist point of view of knowledge [32]. When the process is carried out on a large amount of data or directly starting from probabilities, the expression of basic probability assignment could be preferred [33,34]. Basic mass assignment is suitable in the treatment of knowledge from experts' opinions [36]. Ha Duong [32, p.70] argues about the unimportance of this interpretation problem, which occults a mathematical unit. In this article, the term of belief masses is used indifferently.

In the evidence theory, a set of mutually exclusive and exhaustive $q$ elements called the frame of discernment is considered and defined by:

$$
\Omega=\left\{H_{1}, H_{2}, \ldots, H_{q}\right\}
$$

$\Omega$ is the set of all possible issues where each issue or hypothesis $H_{i}$ can support any information from different sources. The information sources can distribute masses on every subset of the frame of discernment:
$A_{i} \in 2^{\Omega}:\left\{\emptyset, A_{1}=\left\{H_{1}\right\}, \ldots, A_{q}=\left\{H_{q}\right\}, A_{q+1}=\left\{H_{1}, H_{2}\right\}, \ldots, A_{2^{q}-1}=\left\{H_{1}, \ldots, H_{q}\right\}\right\}$.
An information source assigns a belief mass between 0 and 1 only on hypotheses on which it has a direct knowledge, i.e. it does not assign any belief mass to any subset of these hypotheses [37]. This process, called basic mass assignment, is represented by a function $m$ defined by:

$$
m: 2^{\Omega} \rightarrow[0,1]
$$

such as:

$$
m(\emptyset)=0
$$

and

$$
\sum_{A_{i} \in 2^{\Omega}} m\left(A_{i}\right)=1
$$

Each $A_{i}$ supporting $0<m\left(A_{i}\right) \leq 1$ is called a focal set. The constraint defined on $\emptyset$ by 6 is not mandatory. It supposes that all hypotheses $H_{i}$ are known, i.e. the problem is defined in the context of closed world assumption. The goal of $\emptyset$ is to formalize the fact that all hypotheses are not known. In this case, $m(\emptyset) \neq 0$ supports this consideration [38].

# 3.2 Belief and plausibility measures 

The upper and lower bounds of a probability interval can be defined from a belief mass distribution. This interval contains the probability of a set of hypotheses or focal sets and is bounded by two non-additive measures called belief (Bel) and plausibility (Pls) [39].

The measure of belief $\operatorname{Bel}\left(A_{i}\right)$ is the lower bound of probability of a focal set $A_{i}$. It is the sum of the belief masses of all subsets $B$ that contribute to $A_{i}$ such as $B \subseteq A_{i}$. The

![img-1.jpeg](img-1.jpeg)

Figure 2: Plausibility and belief measures and their complement [43]
upper bound of probability $\operatorname{Pls}\left(A_{i}\right)$ is the sum of all belief masses assigned to subsets $B$ such as $B \cap A_{i} \neq \emptyset . P l s\left(A_{i}\right)$ and $\operatorname{Bel}\left(A_{i}\right)$ are defined by the following equations:

$$
\begin{gathered}
\operatorname{Pls}\left(A_{i}\right)=\sum_{B\left|A_{i}\right| \cap B \neq \emptyset} m(B) \\
\operatorname{Bel}\left(A_{i}\right)=\sum_{B \mid B \subseteq A_{i}} m(B)
\end{gathered}
$$

It results in the bounding property defined by the following equation:

$$
\operatorname{Bel}\left(A_{i}\right) \leq \operatorname{Pr}\left(A_{i}\right) \leq \operatorname{Pls}\left(A_{i}\right)
$$

where $\operatorname{Pr}\left(A_{i}\right)$ defines the occurrence probability of $A_{i}$ but remains unknown. It can take any value in $\left[\operatorname{Bel}\left(A_{i}\right) \operatorname{Pls}\left(A_{i}\right)\right]$. The bounding property 10 is well known and has been defined since 1976 in the work of Shafer [9]. Many authors used it to connect the interval defined by $\left[\operatorname{Bel}\left(A_{i}\right) \operatorname{Pls}\left(A_{i}\right)\right]$ and the belief mass distribution [40-42].

Plausibility and belief measures are not dual because they are not additives within the meaning of the probability theory $\left(\operatorname{Bel}\left(A_{i}\right) \neq \operatorname{Pls}\left(A_{i}^{c}\right)\right)$ where $A_{i}^{c}$ is the complement of $A_{i}$ according to $\Omega$. However, the relations below can be established between $A_{i}$ and $A_{i}^{c}:$

$$
\operatorname{Bel}\left(A_{i}^{c}\right)=1-\operatorname{Pls}\left(A_{i}\right)
$$

and

$$
\operatorname{Pls}\left(A_{i}^{c}\right)=1-\operatorname{Bel}\left(A_{i}\right)
$$

with

$$
\operatorname{Bel}\left(A_{i}^{c}\right) \leq \operatorname{Pls}\left(A_{i}^{c}\right)
$$

$\left(\operatorname{Pls}\left(A_{i}\right)-\operatorname{Bel}\left(A_{i}\right)\right)$ describes the uncertainty concerning hypothesis $A_{i}$ represented by interval $\left[\operatorname{Bel}\left(A_{i}\right) \operatorname{Pls}\left(A_{i}\right)\right]$ (cf. figure 2).

From plausibility and belief measures, the basic mass assignment is computed by the Möbius transform [44]:

$$
m\left(A_{i}\right)=\sum_{B \mid B \subseteq A_{i}}(-1)^{\left|A_{i}\right|-|B|} \operatorname{Bel}(B)
$$

where $\left|A_{i}\right|$ is the cardinal of set $A_{i}$.

# 3.3 Probability intervals and belief mass assignment 

If the imprecision on a probability measure is described by an interval, the relation with a basic mass assignment is directly obtained by:

$$
\left[\underline{P}_{H_{i}} \bar{P}_{H_{i}}\right]=\left[\operatorname{Bel}\left(H_{i}\right) \operatorname{Pls}\left(H_{i}\right)\right]
$$

where $\underline{P}_{H_{i}}$ is the lower bound of probability of hypothesis $H_{i}, \bar{P}_{H_{i}}$ is the upper bound of probability with $i$ from 1 to $q$ the number of hypotheses. The transformation of a probability interval set $\left[P_{X}\right]$ of a random variable $X$ to a basic belief assignment $M_{X}$ is easily obtained by 8,9 and 14 . If :

$$
\left[P_{X}\right]=\left[\left[\underline{P}_{H_{1}^{X}} \bar{P}_{H_{1}^{X}}\right] \ldots\left[\underline{P}_{H_{q}^{X}} \bar{P}_{H_{q}^{X}}\right]\right]
$$

then

$$
\begin{aligned}
M_{X} & =\left[m(\emptyset) m\left(A_{1}^{X}\right) \ldots m\left(A_{i}^{X}\right) \ldots m\left(A_{2}^{X}-1\right)\right] \\
& =\left[\underline{P}_{B} \underline{P}_{A_{1}^{X}} \ldots \sum_{B \mid B \subset A_{i}^{X}}(-1)^{\left|A_{i}^{X}\right|-\left|B^{X}\right|} \underline{P}_{B^{X}} \ldots\right]
\end{aligned}
$$

with $A_{i}^{X} \in 2^{\Omega_{X}}$.
As argued by Smets [45], the knowledge of $\operatorname{Bel}\left(A_{i}^{X}\right)$ and $\operatorname{Pls}\left(A_{i}^{X}\right)$ measures is equal to the knowledge of the basic mass assignment on the frame of discernment.

### 3.4 Fuzzy probability and basic mass assignment

If the imprecision on a probability measure is described by a fuzzy probability, it is easy to compute all its nested intervals corresponding to the different $\alpha$-cuts of the fuzzy number. Thus, a set of nested upper and lower bounds of probabilities are obtained and the corresponding belief mass distribution for each level $\alpha$ can be computed:

$$
\left[P_{H_{i}}^{\alpha} \bar{P}_{H_{i}}^{\alpha}\right]=\left[P^{\alpha}\left(H_{i}\right) \bar{P}^{\alpha}\left(H_{i}\right)\right]=\left[\operatorname{Bel}^{\alpha}\left(H_{i}\right) \operatorname{Pls}^{\alpha}\left(H_{i}\right)\right]
$$

where $B e l^{\alpha}\left(H_{i}\right)$ is the lower bound of the fuzzy probability cut of level $\alpha$ and $\operatorname{Pls}^{\alpha}\left(H_{i}\right)$ the upper bound.

Thus, the belief mass distribution $M_{X}^{\alpha}$ at level $\alpha$ which describes a variable $X$ is computed from the probability interval distribution $\left[P_{X}^{\alpha}\right]$ on $\Omega_{X}$ by 8,9 and 14 :

$$
\left[P_{X}^{\alpha}\right]=\left(\left[\underline{P}_{H_{1}}^{\alpha} \bar{P}_{H_{1}}^{\alpha}\right], \ldots,\left[\underline{P}_{H_{q}}^{\alpha} \bar{P}_{H_{q}}^{\alpha}\right]\right)
$$

then

$$
\begin{aligned}
M_{X}^{\alpha} & =\left[m^{\alpha}\left(\left\{H_{1}\right\}\right) \ldots m^{\alpha}\left(\left\{H_{i}\right\}\right) \ldots m^{\alpha}\left(\left\{H_{1}, \ldots, H_{q}\right\}\right)\right] \\
& =\left[\underline{P}_{H_{1}}^{\alpha} \ldots, \sum_{H_{j} \mid H_{j} \subset H_{i}}(-1)^{\left|H_{i}\right|-\left|H_{j}\right|} \underline{P}_{H_{j}}^{\alpha} \ldots \sum_{H_{j} \mid H_{j} \subset H_{q}}(-1)^{\left|H_{q}\right|-\left|H_{j}\right|} \underline{P}_{H_{j}}^{\alpha}\right]
\end{aligned}
$$

By varying $\alpha \in[0,1]$ the fuzzy probabilities of a variable can be coded by a set of basic mass assignments.

# 4 Evidential networks to model reliability 

In complex system models for their reliability analysis, the variables, which represent the system, its components, its function, or the events of the system, are related to each other. These relations can be represented by conditional dependencies. In this section, we propose to define an evidential network to represent the conditional dependencies between variables in a frame of discernment integrating uncertainty as belief masses in the meaning of the evidence theory.

The proposed evidential networks are directed acyclic graphs, which represent uncertain knowledge in random and epistemic ways $[18,46]$. An evidential network is a couple: $G=((N, A), M)$, where $(N, A)$ represents the graph with $N$ the set of nodes, $A$ the set of edges and, $M$ the set of belief masses associated to each node. When a node is not a root node, i.e. when it has parent nodes, its belief mass distribution is defined by a conditional belief mass table quantifying the relation between the node and its parents. When a node is a root, an a priori belief mass table is defined.

A discrete random variable $X$ is represented by a node $X \in N$ with its frame of discernment $\Omega_{X}$ constituted by $q$ mutually exhaustive and exclusive hypotheses (cf. 3). The vector $M(X)$, also noted $M_{X}$, is the belief mass distribution over the $2^{q}$ focal sets $A_{i}^{X}$ (cf. 4). $M(X)$ is defined by the following equation:

$$
M(X)=\left[m(X \subseteq \emptyset) m\left(X \subseteq A_{1}^{X}\right) \ldots m\left(X \subseteq A_{i}^{X}\right) \ldots m\left(X \subseteq A_{2^{q}-1}^{X}\right)\right]
$$

with $m\left(X \subseteq A_{i}^{X}\right) \geq 0$ and $\sum_{A_{i}^{X} \mid A_{i}^{X} \in 2^{\Omega}} m\left(X \subseteq A_{i}^{X}\right)=1$, where $m\left(X \subseteq A_{i}^{X}\right)$ is the belief that variable $X$ verifies the hypotheses of focal element $A_{i}^{X}$.

When a node is a child node, $M$ is represented by its own conditional belief mass table. Each conditional belief mass table defines the relation between the belief masses assigned on the frame of discernment of the variable expressed by each parent node and the belief masses assigned on the child node frame of discernment. Figure 3 shows two nodes $X$ and $Y$ defined with the frame of discernment $2^{\Omega_{X}}:\left\{\emptyset, A_{1}^{X}, \ldots A_{M}^{X}\right\}$, $2^{\Omega_{Y}}:\left\{\emptyset, A_{1}^{Y}, \ldots A_{K}^{Y}\right\}$ and lies to a node $Z$ with its own frame of discernment $2^{\Omega_{Z}}$ : $\left\{\emptyset, A_{1}^{Z}, \ldots A_{L}^{Z}\right\}$. The conditional belief mass table of $Z$ is defined by conditional belief mass $M(Z \mid X, Y)$ for each hypothesis $A_{i}^{Z}$ given the focal sets of its parents $X$ and $Y$. For a root node, i.e. without parents like $X$ and $Y$, the belief mass table is a vector representing the a priori belief mass distribution defining the amount of belief that a variable verifies the hypotheses of the frame of discernment.
![img-2.jpeg](img-2.jpeg)

Figure 3: Elementary network: 2 parents, 1 child
To compute the marginal belief mass distributions of each node, inference algorithms are used. The exact inference is carried out by the algorithm proposed by Jensen based on the construction of a junction tree [47, pp. 76] as we proposed in [18]. This

algorithm updates the marginal belief mass distribution on each node given the knowledge introduced into the evidential network. The computation mechanism is based on the Bayes theorem, which is extended to the representation of uncertain information according to the framework of evidence theory. Specific evidence (Hard evidence) is modelled by a mass of 1 assigned to one focal element of the frame of discernment. Non-specific evidence (soft evidence) corresponds to a mass distribution on several focal elements of the frame of discernment.

When modelling probist reliability problems, the frame of discernment $(\Omega=\{\{U p\},\{D o w n\}\})$ becomes a Dempster-Shafer structure $\left(2^{\Omega}=\{\emptyset,\{U p\},\{D o w n\},\{U p, D o w n\}\}\right)$ which can be reduced to the three following hypotheses:

- $m\{U p\}$ : belief mass that the system is in operating condition,
- $m\{D o w n\}$ : belief mass that the system is in fail condition,
- $m\{U p$, Down $\}$ : belief mass that the system is exclusively in one of the previous conditions without distinguishing exactly which.

Under the assumptions of probist reliability, the studied components as well as the system can only be in one of the two operating conditions. This is a closed world problem [38] and the hypothesis $\emptyset$ does not carry any belief mass. In the analysis of reliability or risk integrating human factors, it can be interesting to assign a belief mass to $\emptyset$ to characterize the lack of completeness of assumptions (open world) on which the analysis is based rather than introducing a safety coefficient or a margin of probability on the global result in order to take into account the possible missed scenarios. In this study, the problem of reliability analysis of systems as a problem of closed world $(m(\emptyset)=0)$ is considered.

# 4.1 Modelling system reliability 

To model the reliability of systems by evidential networks, we transpose the approach suggested by Bobbio et al. [48, 49] to evidential networks. The goal is to convert a fault tree into an equivalent network with the hypothesis suggested by Guth [40] as presented in [18]. A fault tree describes the propagation process of a failure within the functional structure of a system. The reliability of the modelled system follows the assumptions of independence of the events and of coherence of the systems [50].

The reliability is described by 'AND', 'OR', ' $k$ out of $n$ ' gates combining the elementary events. To integrate the frame of discernment of the evidence theory, the evidential network models the truth tables of 'AND' gate (cf. table 1) and 'OR' gate (cf. table 2) [40] by conditional belief mass tables 3 and 4 [18].

Table 1: Truth table of a 'AND' gate


The conditional belief mass table representing a 'AND' gate is defined by table 3. $E_{X}$ corresponds to the state of the component $X, E_{Y}$ to the state of component $Y$, and $E_{X}, E_{Y}$ are the inputs of the 'AND' gate. $E_{Z}$ corresponds to the output of the gate. The conditional belief mass table of a 'OR' gate is defined by table 4.

Table 2: Truth table of a 'OR' gate


Table 3: Conditional belief mass table of a 'AND' gate


The conditional belief mass table can be adapted to gates with more inputs and to $k$ out of $n$ gates (cf. table 5). In addition, the coefficients of the conditional belief mass table take their value in $\{0,1\}$ since it is a translation of the truth tables of logical gates. These coefficients can take different values from $\{0,1\}$ if the modelling of different behaviours is expected, in particular when there is an uncertainty about the propagation of belief masses through the evidential network.

# 4.2 Belief and plausibility measures in evidential networks 

To compute belief and plausibility measures in an evidential network, it is necessary to apply 8 and 9 . When an evidential network is implemented in a tool respecting the additivity axiom, if the exact inference algorithm should compute Bel and Pls measures then it cannot be done in the same node. Simon and Weber [18] proposed to compute each measure on a focal element of a variable by two particular nodes (cf. figure 4). The node dedicated to compute $\operatorname{Bel}\left(A_{j}^{X}\right)$ is described by two hypotheses Believe and
![img-3.jpeg](img-3.jpeg)

Figure 4: Nodes to compute Bel and Pls measures.
Doubt according to the conditional belief mass table given on table 6.

Table 4: Conditional belief mass table of a 'OR' gate


The node dedicated to compute $\operatorname{Pls}\left(A_{j}^{k}\right)$ is described by hypotheses Plausibility et Disbelief according to table 7.

The structure of these nodes is generic. It is useful for the computation of belief and plausibility measures of each node of the network and for each hypothesis. Moreover, taking into account the bounding property (cf. 10), these nodes allow the definition of probability interval on any hypothesis of a studied variable.

# 5 Numerical studies 

In this section, we propose to study the reliability of two different systems in order to show the applicability of the method. The inference in evidential networks is made by the algorithm of exact inference defined in Bayesialab©. Evidential networks are directly modelled by using the graphic interface of this tool.

### 5.1 Bridge system

For this study, we have chosen a complex system concerning reliability as written by Villemeur [50] but with few components in order to facilitate the comprehension. The bridge system (cf. figure 5) was largely studied in the literature and Torres-Toledano [51] modelled its reliability with Bayesian networks. It is not a parallel-series system and its structure function contains repeated events. It consists of 5 components. Each component has two disjoint states $(\{U p\},\{D o w n\})$ for a probist reliability problem. The elementary events on these components are supposed to be independent. The system is homogeneous and no repair is considered.
![img-4.jpeg](img-4.jpeg)

Figure 5: Bridge system

Table 5: Conditional belief mass table of a ' 2 out of 3 ' gate


By enumerating the minimal cuts or the minimal success paths, the evidential network shown in figure 6 is obtained to evaluate the bridge system reliability. Each root node labelled $C_{i}$ contains the basic mass distribution according to the frame of discernment of each component $C_{i}$ as previously presented. Each child node contains the conditional mass tables according to the truth tables previously defined in section 4.1 according to the system structure function. From node $O R 3$ defining the system state, two nodes Pls and Bel are linked in order to compute the probability bounds on the system state $\{U p\}$ according to the conditional mass tables 6 and 7.

In the first part of this example, we propose to deal with crisp probabilities to obtain a reference value for the system reliability. The following values are considered for the probability of components to be in state $\{U p\}:: P^{\alpha}\left(C_{i \mid i \in\{1,2,5\}}=\{U p\}\right)=$ 0.81873 and $P^{\alpha}\left(C_{j \mid j \in\{3,4\}}=\{U p\}\right)=0.67032$ for all $\alpha$. Using 8,9 and 14 , we obtain the a priori belief mass distributions: $M_{C_{i}}^{\alpha}=[0.818730 .181270], \forall \alpha$ and $M_{C_{i}}^{\alpha}=$ $[0.670320 .329680], \forall \alpha$. The reader can note that there is no imprecision, thus the belief mass assigned to the epistemic state $\{U p$, Down $\}$ is 0 .

The propagation of the a priori belief masses through the network gives the system reliability $R=0.850134$ as shown in figure 6 . It has been shown in [18] that this value

Table 6: Conditional belief mass table of node $\operatorname{Bel}\left(A_{j}^{X}\right)$


Table 7: Conditional belief mass table of node $\operatorname{Pls}\left(A_{j}^{X}\right)$


is the exact value obtained from other evaluation methods like Markov chains.
Now, let us consider the imprecise value of probabilities as fuzzy probability in the bridge system reliability evaluation. The evidential network described in the previous section is used and the fuzzy probabilities are described by fuzzy numbers with the following values: $P\left(C_{i \mid i \in\{1,2,5\}}\right)=(0.81873,0.80252,0.98019)$ and $P\left(C_{j \mid j \in\{3,4\}}\right)=$ $(0.67032,0.65704,0.68386)$ as defined in section 2 . For each level $\alpha$, an a priori basic mass distribution for each parent node $C_{i}$ is computed according to 20 . The corresponding belief $\left(\operatorname{Bel}^{\alpha}(S=\{U p\})\right.$ ) and plausibility ( $\operatorname{Pls}^{\alpha}(S=\{U p\})$ ) measures for the system at each level $\alpha$ are obtained and the fuzzy probability of the system to be in state $U p$ is reconstructed by embodying all nested intervals obtained (Figure 7).

To show that fuzzy probabilities computed by the evidential network encompass the probability distribution given by a probabilistic approach, a crude Monte Carlo simulation has been done. As we have no information about the failure rate distribution any distribution can be used. For the sake of simplicity, a uniform distribution for each failure rate has been chosen. This choice is usual in probability framework but does not correctly express our ignorance about the real probability distribution of failure rates. It should be considered as a usual example. By the following equation, we compute the failure probability of each component $C_{i}$ :

$$
P_{C_{i}}=1-\exp \left(-\lambda_{i} * T_{i}\right)
$$

with $\lambda_{i} \mapsto U\left(\left[\underline{\lambda}_{i}, \bar{\lambda}_{i}\right]\right)$.
Our Monte Carlo simulation consists of sampling 1000 values of each failure rates according to uniform probability laws of failure rates. Then, the quintuplet $P_{C_{1}}, P_{C_{2}}, P_{C_{3}}, P_{C_{4}}, P_{C_{5}}$ is computed by 22 . The evidential network computes the failure probability distribution of the system $P_{S}$ by an exact inference from the failure probability distribution of the 5 components.

The resulting system failure probability distribution is shown in figure 8.
The histogram shown in figure 8 looks like a normal distribution. This result is regular according to the central limit theorem, which defines the combination of uniform laws through the network structure as a normal law. From the data, we note that the

![img-5.jpeg](img-5.jpeg)

Figure 6: Bridge system reliability by EN
![img-6.jpeg](img-6.jpeg)

Figure 7: System fuzzy failure probability

![img-7.jpeg](img-7.jpeg)

Figure 8: Histogram of Monte-Carlo simulation results
lower probability obtained on the system operating state is 0.8376 , the upper probability is 0.8627 and the average probability is 0.8502 . This average value is very close to the expected reliability value $R=0.8501$ previously computed.

In the results obtained from the Monte-Carlo simulation and the proposed approach, several elements are particularly interesting. First, the support of the fuzzy failure probability is $[0.83390 .8658]$, which corresponds to the upper and lower probabilities computed by the Monte-Carlo simulation ( $[0.83760 .8627]$ ). Moreover, obtaining a quintuplet of the component failure probabilities, which brings to these upper and lower values of the system failure probability by crude Monte Carlo simulation, is rare. So, the number of simulations must grow to obtain them or advanced Monte-Carlo simulations should be applied (Latin Hypercube Sampling for example). Secondly, the average value of the Monte Carlo simulation results converge towards the real reliability value $R=0.8501$. The value of the kernel of the fuzzy probability of the system operating state is $\operatorname{Kern} P_{s}=0.8501$. The evidential networks has computed the exact value.

# 5.2 Safety instrumented systems 

For this second example, we propose a comparison of our approach with a fuzzy fault tree approach dedicated to the performance evaluation of a safety instrumented system studied in [11]. The goal of the safety instrumented system is to reduce the probability of failure of the process under a referenced level $\left(P_{S I S} \leq 10^{-2} h^{-1}\right)$. For this purpose the structure of the safety instrumented system used and the process under control are given in figure 9 .

To evaluate the system performance, the fault tree in figure 10 and the fuzzy probabilities in table 8 have been used. According to the authors, events are independent and no repair is considered. Moreover, the rare event approximation is considered. More details can be obtained from [11].

In order to compare the resulting fuzzy probability of the safety instrumented system according to the method proposed in [11] and the result obtained from our approach, we encode the fuzzy probabilities in the evidential network given in figure 11 which is equivalent to the fault tree previously given. As it can be seen, the evidential

![img-8.jpeg](img-8.jpeg)

Figure 9: Process and its safety instrumented system
![img-9.jpeg](img-9.jpeg)

Figure 10: Fault tree and its SIS

Table 8: Truth table of a 'AND' gate


network is based on the minimal cut set obtained from the fault tree in figure 10.
![img-10.jpeg](img-10.jpeg)

Figure 11: Evidential network for SIS performance evaluation
Figure 12 gives the resulting fuzzy probability obtained from the fuzzy fault tree approach [11] in a large dotted line and the fuzzy probability obtained from the evidential network in a dotted line. Due to rare event approximation the fault tree approach doesn't give the exact most likely value ( $\operatorname{KernP}(\operatorname{SIS})$ ) whereas the fuzzy probability obtained from the evidential network gives the exact value. Moreover, the support of the fuzzy probability $(\operatorname{SuppP}(\operatorname{SIS})$ ) given from the evidential network is more tenuous than the one given by the fuzzy fault tree approach because of the repeated events involved in the minimal cut sets.

![img-11.jpeg](img-11.jpeg)

Figure 12: Performance comparison

# 6 Conclusion 

In this article, we address the problem of imprecision in the assessment of system reliability. For this purpose, we have proposed the use of the evidence theory in a network approach to easily tackle random and epistemic uncertainties as real, interval or fuzzy probabilities. We have defined the useful basics of the evidence theory and how it has been introduced in a directed acyclic graph to build an evidential network. Evidential networks are thus used to model reliability and two different systems were studied in order to show the performance of the proposed approach.

The proposed study has shown that evidential networks are an interesting tool to handle random and epistemic uncertainties in probist reliability of complex systems. It gives accurate results, and a powerful modelling approach to studying systems. Moreover, different representations of imprecise reliability parameters can be used (precise, interval or fuzzy values) and mixed in the same representation. The modelling approach proposed is not reduced to modelling uncertainties in reliability and can be used in a more general model of knowledge under uncertainties. However, the $\alpha$-cut approach used considers a dependence between sources of information/expert and further works should deal with other hypotheses of dependencies between sources.
