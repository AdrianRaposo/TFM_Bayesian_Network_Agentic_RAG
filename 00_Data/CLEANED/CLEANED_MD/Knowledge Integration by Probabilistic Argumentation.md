# Knowledge Integration by Probabilistic Argumentation 

Saung Hnin Pwint $\mathbf{O O}^{\dagger \mathrm{a})}$, Member, Nguyen Duy HUNG ${ }^{\dagger \mathrm{b})}$, and Thanaruk THEERAMUNKONG ${ }^{\dagger \mathrm{c})}$, Nonmembers


#### Abstract

SUMMARY While existing inference engines solved real world problems using probabilistic knowledge representation, one challenging task is to efficiently utilize the representation under a situation of uncertainty during conflict resolution. This paper presents a new approach to straightforwardly combine a rule-based system (RB) with a probabilistic graphical inference framework, i.e., naïve Bayesian network (BN), towards probabilistic argumentation via a so-called probabilistic assumption-based argumentation (PABA) framework. A rule-based system (RB) formalizes its rules into defeasible logic under the assumption-based argumentation (ABA) framework while the Bayesian network (BN) provides probabilistic reasoning. By knowledge integration, while the former provides a solid testbed for inference, the latter helps the former to solve persistent conflicts by setting an acceptance threshold. By experiments, effectiveness of this approach on conflict resolution is shown via an example of liver disorder diagnosis.


key words: knowledge integration, probabilistic argumentation, probabilistic graphical models and rules

## 1. Introduction

Knowledge integration (KI) is a process of incorporating new information into a body of existing knowledge [1] when a source is insufficient for making decision itself. In multiagent systems, agents integrate and share their knowledge to perform a common task [2]-[4]. In ontology integration, several ontologies are integrated for handling semantic heterogeneity and knowledge variation [5]-[8]. In BNs integration [9]-[12], a global BN is constructed by combining local BNs. However, conflict is a common problem when knowledge from multiple sources is combined. For example, a source has knowledge about that $A$ causes $B$ while another source has knowledge about that $B$ causes $A$. Unfortunately, conflicts make inconsistent decisions in multi-agent systems and inconsistent semantic information in ontologybased systems, triggering some cycles in BNs.

As a conflict resolution, conflict is assumed as a normalization factor of ignorance in Dempster's rule of combination [13] for merging evidences from independent sources. Unfortunately, Dempster's rule of combination cannot solve the problem of total conflict evidences since it

[^0]causes the combination result to be not applicable (N/A). So, [14] extends the Dempster's rule of combination by measuring conflict between two pieces of evidence as a coefficient. Moreover, several approaches [15]-[18] have been explored to investigate combination methods for integrating conflict evidences based on Dempster-Shafer theory (DST). However, the combination results may vary according to their baseline methods. Meanwhile, argumentation is a common sense of reasoning formalism and solves conflict by attacking arguments. It is used in several areas including decision making, knowledge integration, ontology, and multiagents, for providing accurate final decisions. There are several approaches [19]-[23], which use argumentation to solve the conflict while integrating knowledge. These approaches usually use single representation, such as either DST statements or argumentation statements. However, it is more efficient if we combine straightforwardly different notations, each of which has different strengths in its representation, resulting in improving total process performance. In fact, for combining different representations, it is difficult to detect whether the knowledge of these representations overlap with each other or not due to their different vocabularies in knowledge representation. For example, BN represents knowledge in the form of a directed acyclic graph while RB represents knowledge in the form of rules.

This paper presents a study on integration of two powerful but different presentations with augmentation-based conflict resolution, that is combination of rule-based (RB) and Bayesian network (BN) via probabilistic argumentation. In our approach, defeasible reasoning can be incorporated into the RB system using the ABA framework where any conflict can be solved using the ABA's semantic. Complementarily, the probabilistic inference can be achieved by querying the propositions based on evidences (observations) inside the BN. As one solution, it is possible to set up a rule iff probability of the proposition computed by the BN is greater than 0.5 , then the proposition is entailed by the framework. Otherwise, they conflict. To enable the combination of RB and BN, we propose to translate them into a common representation, say the probabilistic assumption-based argumentation (PABA) framework. So, we use the PABA framework as an identical representation since it captures both logical and probabilistic aspects. In the conflict resolution, we formalize them into their respective PABA frameworks and provide a combination way for integrating them into an integrated framework. Then, we infer the proposition into this integrated PABA framework


[^0]:    Manuscript received October 7, 2019.
    Manuscript revised February 20, 2020.
    Manuscript publicized May 1, 2020.
    ${ }^{\dagger}$ The authors are with the School of Information, Computer, and Communication Technology, Sirindhorn International Institute of Technology, Thammasat University, Pathum Thani, 12000, Thailand.
    a) E-mail: hnin.pwint172004@gmail.com
    b) E-mail: hung@siit.tu.ac.th
    c) E-mail: thanaruk@siit.tu.ac.th

    DOI: 10.1587/transinf.2019EDP7270

for computing the acceptable probability of the proposition. We show that our approach provides more reliable and better explainable results than each single individual representation. As an application area, we apply production rules of a rule-based approach that is implemented by LUCAS [24], [25] and a naïve BN that is generated from 100 patient-records [26]. They are concerned about diagnosis of liver disorders and biliary tracts. We evaluate our approach by inferring common diagnosis such as steatosis hepatitis and primary biliary cirrhosis.

Some related works are shown in Sect. 2 while some theoretical backgrounds are provided in Sect. 3. We describe overview of our approach with its applications, an RB and a naïve BN, in Sect. 4. How to restructure the RB into the ABA framework is described in Sect. 5. In Sect. 6, we show how to detect conflicts between the ABA framework and the naïve BN. In Sect. 7, we resolve the conflict by introducing the PABA framework, translating both RB and BN into this framework, and then conducting threshold-based inference. The experimental results are provided in Sect. 8. Some conclusions and future directions are given in Sect. 9.

## 2. Related Work

So far knowledge integration have been studied in several works including those related to multi-agent systems [3], [4], [27], and Bayesian inference systems [9]-[12], [19]. In [9], a method that handles an ancestral ordering shared by individual BNs, was developed to combine these BNs. The method removes some nodes from two original networks and combines these networks. In [10], a four-step algorithm was proposed to systematically combine the qualitative and the quantitative parts of the different probabilistic graphical models; Bayesian networks (BNs) and influence diagrams (IDs), for heart disease diagnosis. It reduces complexity of structural and quantitative (i.e., conditional distributions) combinations by removing some original dependencies between nodes. In [11], a method to recover the global structure from multiple local Bayesian networks without losing any domain information, was proposed. In [12], the authors presented the probabilistic models as Bayesian Knowledge Bases (BKBs) and proposed an algorithm called Bayesian knowledge fusion that allows easy aggregation and de-aggregation of information from multiple expert sources and facilitates multi-expert decision making by providing a framework in which all opinions can be preserved and reasoned over. In [28], an approach to translate logical knowledge into Bayesian networks was illustrated. In this approach, network composition is applied to build a uniform representation that supports both logical and probabilistic reasoning. In [29], an approach to fuse multiple knowledge sources in geo-spatial decision support systems, was proposed as probabilistic logic. In this work, the probability of a sentence (i.e., a query) was computed when a set of sentences is provided as evidences. Then the probabilistic logic is introduced to represent uncertainties in logical sentences and to reduce the computational complex- ity of coping with the semantics of the sentence. If multiple sources have conflicts in their knowledge, then it is difficult to be integrated. In propositional bases, conjunctive and disjunctive mergings are two ways to combine these bases depending on whether the bases are conflicting or not [30]. When the bases are not conflicting, the former is preferred to the latter, otherwise, the latter to the former.

Moreover, several approaches [15]-[18] have been explored to investigate hybrid methods for integrating conflict evidences based on Dempster-Shafer theory (DST). In [15], the authors applied Dempster-Shafer Theory (DST) to address the problems of combining information in recommender systems (RSs) such as non-sense combination problem, totally-conflicting combination problem, incomparable rating problem in RS. They analyzed six combination of methods, which are based on DST, and proposed two hybrid combination methods to solve existing conflict in massive functions. The first hybrid method combines the methods of Dubois and Prade's Rule of Combination and the method of Dempster's Rule of Combination. The other method combines Dempster's Rule of Combination and finds the average of rule combination. The results of the paper showed that these hybrid methods outperformed the baseline methods. In [16], the authors proposed a method based on DEMATEL for combining multiple conflicting evidences and reducing computational complexity in the combination. The relation between evidences is determined by constructing a similarity measure matrix. Then conflicting evidence was modified by calculating prominence and importance of evidence. Finally, the method computed the weighted average of evidences as a combination result based on Dempster's rule of combination.

In the past, the argument-based systems (ABSs) helps improve decision making process, particularly when the user provided enough evidences, even the decision was done in a realistic but complicate task [21]. In [19], the WebKIDSS framework was developed as an argumentationenabled knowledge integration in a decision support system in semantic web in order to solve conflicts which make incomplete and inconsistent semantic web information. In [20], argumentation was used instead of voting to develop a hybrid intelligent system for crop classification. It integrates expert knowledge and decisions of three bases classifiers; decision tree, support vector machine and neural network. Both knowledge and decisions are expressed as rules with defeasible logic programming in order to solve conflicts for providing accurate prediction in crop classification. When ontologies are incomplete and inconsistent, a decision support framework for ontology integration was developed in [22] using argumentation. It determines the membership status of individuals to concepts and provides a global understanding of the knowledge. In [31], preferencebased argumentation framework was proposed to solve conflicts by defining merging operators. In [32], a set of argumentation frameworks were combined by merging operators which generate a set of corresponding frameworks rather than a single one. The framework, called Pooling Infor-

mation from Several Agents (for short, PISA), was developed in [23] to enable classification using argumentation. Agents are participated in a dialectical process arguing for a given example to be classified based on their experience. In [33], a scheme of probabilistic argumentation was developed by combining logic and probability in argumentation. Their focus is an annotating logical formulas (rules) of a knowledge base with probability. So far, even the existing methods could solve real world problems using probabilistic knowledge representation, but there have been no methods that efficiently solve conflicts by integrating the representation under a situation of uncertainty. In this paper, we aim to invent a method to solve conflicts by integrating multiple types of knowledge representation under uncertainty.

## 3. Theoretical Backgrounds

This section provides the backgrounds of rule-based system (RB), Bayesian network (BN), and some argumentation frameworks.

### 3.1 A Rule-Based System

A rule-based system (RB) contains a set of production rules, having a set of conditions and a set of actions by using predicates ${ }^{\dagger}$, functions ${ }^{\dagger \dagger}$ and their negations. A predicate is an expression of the form either $t\left(p_{1}, \ldots, p_{n-1}, v_{1}\right)$ or $t\left(p_{1}, \ldots, p_{n-1},\left[v_{1}, \ldots, v_{m}\right]\right)$ where $t$ is a predicate-name, each $p_{i}$ is a parameter and each $v_{i}$ is a value. A function is an expression of the form of either $f\left(q_{1}, \ldots, q_{n}\right) \circ y_{1}$ or $f\left(q_{1}, \ldots q_{n}\right) \circ\left[y_{1} \ldots y_{m}\right]$ where $f$ is a function-name, each $q_{i}$ is parameter, $\circ$ is a mathematics operator (i.e., $\circ \in\{=,<, \leq,>$ $, \geq\})$ and each $y_{j}$ is a value. The symbol NOT, which is used in front of a predicate/function, is referred to the negation. The symbol AND (resp. OR) is used as conjunctive (resp. disjunctive) connectors between predicates and functions. A production rule is an expression of the following form:

## R: $x$ IF conditions THEN actions FI

where $x$ is a rule number. A set of production rules having common conditions are encoded in the following module where each $a_{s t}$ and $b_{h q}$ are conditions (i.e., functions/predicates/negations), each $c_{i}$ is an action (i.e., function/predicate/negation), and $x$ is a rule's number.


[^0]
### 3.2 A Bayesian Network

Definition 1: A Bayesian network is a pair, $\mathcal{N}=(\mathcal{G}, \mathcal{T})$ where $\mathcal{G}=(V, E)$ is a directed acyclic graph having a set of nodes; $V$, and a set of edges; $E$, and $\mathcal{T}$ is a set of conditional probabilities for all nodes.

The network is a probabilistic graphical model representing uncertainties. A node (random variable) $V_{i}$ has a set of exclusive or mutual exclusive values; $v_{1}, . ., v_{k}$ where $k>0$. The edge from nodes $V_{i}$ to $V_{j}$ represents the conditional dependency between them and $V_{i}$ is a parent of $V_{j}$. Let $\operatorname{Par}\left(V_{j}=v_{j}\right)$ be a set of parents of $V_{j}$ having a value of $v_{j}$. The joint probability distribution of nodes can be computed by the following equation.

$$
P\left(V_{1}=v_{1}, \ldots, V_{n}=v_{n}\right)=\prod_{i=1}^{n} P\left(V_{i}=v_{i} \mid \operatorname{Par}\left(V_{i}=v_{i}\right)\right)
$$

### 3.3 The Abstract Argumentation Framework

Definition 2: The abstract argumentation framework [34] is a pair, $\mathcal{A F}=(A r, A t t)$ where $A r$ is a set of arguments and $A t t \subseteq A r \times A r$ is a set of attacks ${ }^{\dagger \dagger \dagger}$ between arguments.

A set of arguments, $S \subseteq A r$, is conflict-free if it doesn't attack itself. Argument $A$ is acceptable w.r.t $S$ if any argument attacking the argument $A$ is attacked by arguments in $S$. Conflict-free set $S$ is admissible if each argument in $S$ is acceptable w.r.t $S . S$ is a complete extension if it is admissible and every argument in $S$ is acceptable w.r.t $S . S$ is a preferred extension if it is admissible and a maximal (w.r.t set inclusion) complete extension. $S$ is an ideal extension if it is admissible and contained in every preferred extension. Let $f(S)$ be a characteristic function that is denoted as $f(S)=\{A \in A r \mid A$ is acceptable w.r.t $S\}$. $S$ is a grounded extension iff it is admissible and the least fix-point of the characteristic function $f(S)$. An argument $A$ is credulously/grounded/ideally accepted w.r.t $\mathcal{A F}$ (i.e., $\mathcal{A F} \vdash_{x} A$ where $x \in\{c r, g r, i d\}$ ) if it is contained in a preferred/grounded/ideal extension of $\mathcal{A F}$ respectively. It is skeptically accepted by $\mathcal{A F}$, (i.e., $\mathcal{A F} \vdash_{s k} A$ ), if it belongs to all extensions of $\mathcal{A F}$.

### 3.4 The Assumption-Based Argumentation Framework

Let $\mathcal{L}$ be a language containing a non-empty set of literals: positive, negative (i.e., classical negation) and negation as failure. Underlying language $\mathcal{L}$, the assumption-based argumentation (ABA) framework [35] is an extension of Dung's abstract argumentation framework [34]. The ABA framework identifies sentences by means of inference rules supported by assumptions.
Definition 3: The ABA framework is a triple, $\mathcal{F}=$ $(\mathcal{A}, \mathcal{R}, \overline{ })$ where $\mathcal{A}$ is a set of assumptions, $\mathcal{R}$ is a set of

[^1]
[^0]:    ${ }^{\dagger}$ Predicate returns multiple values at the same time.
    ${ }^{\dagger \dagger}$ Function returns one value at a time.

[^1]:    ${ }^{\dagger \dagger}(A, B)$ is denoted that argument $A$ attacks argument $B$.

inference rules and ${ }^{-}$is a total mapping from each assumption to its contrary.

In ABA, the assumption never appears in the head of inference rule $r \in \mathcal{R}$ of the form $\alpha_{0} \leftarrow \alpha_{1}, \ldots, \alpha_{n}$ where $n \geq 0$. The inference rule is classified into defeasible rule and strict rule. The defeasible rule contains at least one assumption in the body of the rule while the strict rule does not contain assumption in the body of the rule. The strict rule without body of the rule of the form $\alpha \leftarrow$ is called a fact. An inference rule $r \in \mathcal{R}$ (resp. a subset of the set of inference rules $(R \subseteq \mathcal{R})$ ) can generate an argument concluding a proposition $\pi$, which is the head of the inference rule $r$ (resp. $r^{\prime} \in R$ ). The argument, which concludes the proposition $\pi \in \mathcal{L}$ and is supported by a set of assumptions $Q$, is denoted as $(Q, \delta, \pi)$ when there is a deduction $\delta$ from $\pi$ to $Q$. The detail backward deduction is referred to [35]. Reasonably, $(Q, \delta, \pi)$ is said to be $(Q, \pi)$. An argument $(Q, \pi)$ attacks argument $\left(Q^{\prime}, \pi^{\prime}\right)$ by attacking some assumptions in $Q^{\prime} . \pi$ is credulously/grounded/ideally accepted w.r.t ABA $\mathcal{F}$ (i.e., $\left.\mathcal{F} \vdash_{x \in\{c r, g r, i d\}} \pi\right)$ if the argument that concludes $\pi$ is contained in a credulous/grounded/ideal extension respectively. Also, it is skeptically accepted by $\mathcal{F}$, (i.e., $\left.\mathcal{F} \vdash_{s k} \pi\right)$, if the argument belongs to all extensions of $\mathcal{F}$.

### 3.5 The Probabilistic Assumption-Based Argumentation Framework

The Probabilistic assumption-based argumentation (PABA) framework [36], an extension of the ABA framework, is a class of probabilistic argumentation.

Definition 4: The PABA framework is a triple, $\mathcal{P}=$ $\left(\mathcal{A}_{p}, \mathcal{R}_{p}, \mathcal{F}\right)$ where $\mathcal{A}_{p}$ is a set of probabilistic assumptions, $\mathcal{R}_{p}$ is a set of probabilistic rules and $\mathcal{F}$ is an ABA framework.

The PABA framework contains probabilistic part consisting of $\mathcal{A}_{p}$ and $\mathcal{R}_{p}$ and the logical part consisting of $A B A$ $\mathcal{F}$. A possible world $\omega$ of PABA $\mathcal{P}$ is a maximal consistent subset of $\mathcal{A}_{p} \cup \neg \mathcal{A}_{p}$. A probabilistic rule in $\mathcal{R}_{p}$ is written as $\left[\alpha_{0}: x\right] \leftarrow \alpha_{1}, \ldots, \alpha_{n}$ (i.e., $n \geq 0$ ) where $\alpha_{0}$ is a probabilistic assumption and $x$ (i.e., $0 \leq x \leq 1$ ) is the probability of $\alpha_{0}$. Its compulsory rule is written as $\left[\neg \alpha_{0}: 1-x\right] \leftarrow \alpha_{1}, \ldots, \alpha_{n}$. If the probabilistic rules $r_{p}:\left[\alpha_{0}: x\right] \leftarrow \alpha_{1}, \ldots, \alpha_{n}$ and $r_{p}^{\prime}:\left[\alpha_{0}: y\right] \leftarrow \alpha_{1}^{\prime}, \ldots, \alpha_{m}^{\prime}$ (i.e., $x \neq y$ ) occur in $\mathcal{R}_{p}$ then $\operatorname{body}\left(r_{p}\right) \subseteq \operatorname{body}\left(r_{p}^{\prime}\right)$ or $\operatorname{body}\left(r_{p}^{\prime}\right) \subseteq \operatorname{body}\left(r_{p}\right)$. If an argument concludes probabilistic assumption $\alpha$ from a set of assumptions $Q$, it is called a probabilistic argument. Otherwise, it is a non-probabilistic argument. Let $Q$ and $Q^{\prime}$ be two sets of assumptions (i.e., $Q \neq Q^{\prime}$ ). We can say that an argument $\left(Q, \alpha\right)$ attacks another argument $\left(Q^{\prime}, \alpha^{\prime}\right)$ satisfying one of three conditions;

1. if $(Q, \alpha)$ is a non-probabilistic argument and $\alpha$ is a contrary of assumptions in $Q^{\prime}$
2. if both arguments are probabilistic arguments having

[^0]$Q^{\prime} \subset Q$
3. if argument $(Q, \alpha)$ concludes probabilistic assumption $\alpha$ and argument $\left(Q^{\prime},[\alpha: x]\right)$ concludes compulsory of the probabilistic assumption $\alpha^{\prime}$ with its probability.
Let PABA $\mathcal{P}$ be a probabilistic acyclic in its dependency graph and $\mathcal{W}$ be a set of all possible worlds of $\mathcal{P}$. $\mathcal{F}_{\omega}=(\mathcal{A}, \mathcal{R} \cup \mathcal{R}_{p} \cup\{\alpha \leftarrow \mid \alpha \in \omega\}, \overline{ })$ is defined as an ABA framework for each possible world $\omega$ of PABA $\mathcal{P}$. ABA $\mathcal{F}_{\omega}$ is also called the PABA $\mathcal{P}_{\omega}$ condition to $\omega$. The probability of an argument, which concludes a proposition $\pi$ being acceptable w.r.t $\mathcal{F}_{\omega}$, is computed as follows.

$$
\operatorname{Prob}(\pi)=\sum_{\omega \in \mathcal{W}: A B A \mathcal{F}_{\omega} \vdash \pi} P(\omega)
$$

According to [37], [38], Bayesian PABA framework is a subclass of the PABA framework when PABA $\mathcal{P}$ subsumes a Bayesian network $\mathcal{N}$ instead of $\mathcal{R}_{p}$ where $\mathcal{N}$ is developed using a probabilistic logic programming; especially Problog ${ }^{\dagger \dagger}$. Therefore, the probability of possible world $\omega$; $P(\omega)$, can be computed using the Eq. (1).
Definition 5: A Bayesian PABA is a triple, $\mathcal{P}=$ $\left(\mathcal{A}_{p}, \mathcal{N}, \mathcal{F}\right)$ where each $\alpha \in \mathcal{A}_{p}$ is a probabilistic assumption that corresponds to a node of Bayesian network $\mathcal{N}, \mathcal{N}$ is subsumed instead of probabilistic rules and $\mathcal{F}=(\mathcal{A}, \mathcal{R}, \overline{ })$ is an ABA framework iff it satisfies that $\alpha$ is not an assumption in $\mathcal{F}$ and doesn't occur in the head of any inference rule in $\mathcal{F}$.

## 4. Overview of Our Approach

This section starts with the application areas of our approach (i.e., an RB and a BN), which are concerned about diagnosis of liver disorders and biliary tracts. Then, this section explains the overview of our approach.

### 4.1 HEPAR-RB

HEPAR-RB is a rule-based system, which is developed by LUCAS [24], [25] regarding the diagnosis of liver disorders. HEPAR-RB has 178 production rules encoding in rule modules. We apply these production rules in our approach.
Example 1: Provided that the duration of a patient who suffers from liver disorder is chronic, if the patient abuses alcohol, then diagnoses are alcoholic hepatitis, alcoholic cirrhosis and steatosis hepatitis. If the patient is female, she is over 40 , she does not abuse alcohol and she feels either fatigue or generalized pruritus, then the diagnosis is primary biliary cirrhosis. These statements are written in two production rules in a rule module as below.

[^1]
[^0]:    ${ }^{\dagger} \bar{x}$ is the contrary of the assumption $x$ (i.e., $\bar{x}=\neg x$ ).

[^1]:    ${ }^{\dagger} \mathrm{https}$ ://dtai.cs.kuleuven.be/problog

![img-0.jpeg](img-0.jpeg)

Fig. 1 The segment of HEPAR-NBN
![img-1.jpeg](img-1.jpeg)

Fig. 2 The overview of our approach

PROVIDED duration(patient, complab, chronic) THEN
R:3680
IF biochemical signs (patient) $=$ "alcohol-abuse" THEN diagnosis(patient, "alcoholic-hepatitis") AND diagnosis(patient, "alcoholic-cirrhosis") AND diagnosis(patient, "steatosis-hepatitis")
FI
R:3850
IF sex(patient)=female AND age(patient) $>40$ AND disease_history(patient, "alcohol- abuse") AND complaint(patient, [fatigue, "generalized-pruritus"]) THEN diagnosis(patient, "primary-biliary- cirrhosis")
FI
END;

### 4.2 HEPAR Naïve Bayesian Network

A naïve BN is generated from 100 patients' records using Genie [39] to original Hepar BN developed by [26] and name it as HEPAR-NBN. The Fig. 1 shows the segment of HEPAR-NBN where pbc is referred to primary biliary cirrhosis to be classified.

### 4.3 System Architecture

Our approach takes HEPAR-RB and a dataset, which has 100 patient records, as inputs. The HEPAR-RB is translated into an ABA framework that is named as HEPARABA. Moreover, the dataset is learned to create a naïve BN (i.e., HEPAR-NBN). Given a set of evidences, a proposition is queried by HEPAR-ABA and HEPAR-NBN through argumentation and probabilistic reasoning, respectively. HEPAR-ABA and HEPAR-NBN conflict each other if HEPAR-ABA derives the proposition and HEPAR-NBN provides the probability of the proposition as less than or equal to 0.5 . Such conflict is solved by formalizing and integrating HEPAR-ABA and HEPAR-NBN into the integrated one using the PABA framework. Then, the proposition is also evaluated by the integrated PABA framework that calculates the acceptable probability of the proposition. The overview of our approach is shown in Fig. 2.

## 5. Structuring the RB by the ABA Framework

This section includes translation from an RB to an ABA framework for solving conflicts by ABA's semantic. There are two steps in translations: syntactic translation and semantic translation. In the first step, all production rules of the RB is transformed into logical implications. In the second step, these logical implications are transformed into inference rules ${ }^{\dagger}$ of the ABA framework by adding assumptions into the bodies of the rules, which become defeasible rules. Figure 3 illustrates the translation steps to structure the RB by the ABA framework. For example, an RB contains an production rule of the form IF b THEN a. In the first step, the production rule is transformed into logical implication of the form $a \leftarrow b$. In the second step, this implication
![img-2.jpeg](img-2.jpeg)

Fig. 3 Translation steps

[^0]
[^0]:    ${ }^{\dagger}$ The inference rule of the ABA framework is classified into strict rules and defeasible rules.

Table 1 Translating a RB's syntax to a logical syntax


Table 2 Translating a production rule to an inference rule


where $X=\left\{x_{1}, \ldots, x_{m}\right\}(m \geq 0)$ is a set and $\bigvee X=x_{1} \vee \ldots \vee x_{m}$ is disjunctive between elements of $X$.

Table 3 Translating RB's predicates to literals


Table 4 Translating RB's functions to literals


where $\circ \in\{<, \leq,>, \geq\}$ and in is an operator that checks whether a value is in a range.
is converted into a defeasible rule of the form $a \leftarrow b, \gamma_{a}$ where $\gamma_{a}$ is an assumption.

### 5.1 Syntactic Translation

Underlying language $\mathcal{L}$, the syntax of the RB is transformed into logical syntax as shown in Table 1. Every production rule of the RB is transformed into an inference rule as shown in Table 2. Predicates and functions of the RB are translated into literals as shown in Table 3 and Table 4 respectively.

Example 2: Let du be "duration", pa be "patient", cl be "complab", cr be "chronic", bsigns be "biochemicalsigns", diag be "diagnosis", aabuse be "alcoholabuse", acirr be "alcoholic-cirrhosis", steatosis be "steatosis-hepatitis", ahepat be "alcholic-hepatitis", sex be "sex", female be "female", age be "age", dise be "disease_history", comp be "complaint", fatigue be "fatigue", gpru be "generalized-pruritus" and pbc be "primary-biliary-cirrhosis". The production rules from Example 1 is translated into the following logical implications.


### 5.2 Semantic Translation

Underlying language $\mathcal{L}$, the RB is translated into an ABA framework, $\mathcal{F}=(\mathcal{A}, \mathcal{R}, \overline{\text { - }})$, for solving conflicts by ABA's semantic. In ABA $\mathcal{F}, \mathcal{A}=\left\{\gamma_{y} \mid \gamma_{y}\right.$ is a positive literal for rebutting an argument that concludes $\left.y\right\} \cup\{\varepsilon \mid \varepsilon$ is a positive atom for unknown value $\}$ is a set of assumptions (i.e., $\mathcal{A} \subset \mathcal{L})$. For each assumption $\alpha \in \mathcal{A}, \neg \alpha$ is a contrary of assumption $\alpha$ (i.e., $\bar{\alpha}=\neg \alpha$ ). $\mathcal{R}$ consists of three types of inference rules; defeasible, strict and fact. Let $R_{D}, R_{S}$ and $R_{O}$ be a set of defeasible rules, a set of strict rules and a set of evidences (i.e., observed facts) respectively.

For each logical implication of the form $y \leftarrow$ $\bigvee X_{1}, \ldots, \bigvee X_{n}$ that is syntactically transformed from the production rule of the RB, it is converted into the following defeasible rule by adding an assumption $\gamma_{y}$ in the body of the rule. Then the rule is added into $R_{D}$.

$$
y \leftarrow \bigvee X_{1}, \ldots, \bigvee X_{n}, \gamma_{y}
$$

If there is another defeasible rule $r^{\prime} \in R_{D}$ of the form $y^{\prime} \leftarrow \bigvee Y_{1}, . ., \bigvee Y_{m}, \gamma_{y^{\prime}}$ where $y^{\prime}$ contradicts $y$ (i.e., $\neg y=y$ ) then the following strict rule, which claims $\neg \gamma_{y}$ (i.e., contrary of the assumption $\gamma_{y}$ ), is added into $R_{S}$.

$$
\neg \gamma_{y} \leftarrow y^{\prime}
$$

For each assumption $\varepsilon \in \mathcal{A}$ of the form $f\left(p_{1}, \ldots\right.$, unknown $)$ for unknown value, the following strict rule, which claims $\neg f\left(p_{1}, \ldots\right.$, unknown $)$ (i.e., contrary of assumption $f\left(p_{1}, \ldots\right.$, unknown $\left.)\right)$, is added into $R_{S}$.

$$
\neg f\left(p_{1}, \ldots\right. \text {, unknown }) \leftarrow \bigvee_{1}^{m} f_{i}\left(p_{1}, \ldots, v_{i}\right)(1 \leq i \leq m)
$$

Let $O=\left\{o_{1}, \ldots, o_{n}\right\}$ is a set of literals for evidences (i.e., observed facts). For each $o \in O$, the following inference rule (i.e., a fact) is added into $R_{O}$.

$$
o \leftarrow
$$

Example 3: Suppose that HEPAR-ABA $\mathcal{F}=(\mathcal{A}, \mathcal{R}, \overline{\text { - }})$ is an ABA framework that is transformed from HEPAR-RB. $\mathcal{R}$ consists of the following rules from $R_{D}$ and $R_{S}$ and the inference rules from $R_{O}$ of Example 4.



$\mathcal{A}$ is the set of assumptions having $\left\{\gamma_{\text {diag }(p a, \text { steatosis })}\right.$, $\left.\gamma_{\text {diag }(p a, \text { abepat })}, \gamma_{\text {diag }(p a, \text { acirr })}, \gamma_{\text {diag }(p a, p b c)}}, \gamma_{\mathrm{wl}(p a, s i g)}, \gamma_{\neg \mathrm{wl}(p a, s i g)}}\right.$, $\left.\gamma_{\text {disor( } p a, b e g i n)}, \operatorname{rad}(p a\right.$, unknown) $\}$. Their contraries are as follows.

$$
\begin{aligned}
& \overline{\gamma_{\text {diag }(p a, \text { steatosis })}}=\neg \gamma_{\text {diag }(p a, \text { steatosis })} \\
& \overline{\gamma_{\text {diag }(p a, \text { abepat })}}=\neg \gamma_{\text {diag }(p a, \text { abepat })} \\
& \overline{\gamma_{\text {diag }(p a, \text { acirr })}}=\neg \gamma_{\text {diag }(p a, \text { acirr })} \\
& \overline{\gamma_{\text {diag }(p a, p b c)}}=\neg \gamma_{\text {diag }(p a, p b c)} \\
& \overline{\gamma_{\mathrm{wl}(p a, s i g)}}=\neg \gamma_{\mathrm{wl}(p a, s i g)} \\
& \overline{\gamma_{\text {disor }(p a, b e g i n)}}=\neg \gamma_{\text {disor }(p a, b e g i n)} \\
& \overline{\gamma_{\neg \mathrm{wl}(p a, s i g)}}=\neg \gamma_{\neg \mathrm{wl}(p a, s i g)} \\
& \overline{\operatorname{rad}(p a, \text { unknown })}=\neg \operatorname{rad}(p a, \text { unknown }) .
\end{aligned}
$$

For reasoning through the ABA framework, let $Q$ be a subset of $\mathcal{A}$ that supports an argument $A$ for concluding a proposition $\pi$. Argument $A$ is written as $(Q, \pi)$. If no argument attacks argument $A$ then argument $A$ is grounded acceptable w.r.t ABA $\mathcal{F}$ so the proposition $\pi$ is concluded.

Example 4: (Continue Example 3) Suppose that a set of evidences for HEPAR-ABA $\mathcal{F}$ is $O_{\mathcal{F}}=\{\operatorname{sex}(\mathrm{pa},$ female $)$, age(pa, 45), $\neg$ dise(pa, aabuse), comp(pa, fatigue) $\}$. Then the following rules of $R_{O}$ are added into $\mathcal{R}$ as facts.


According to HEPAR-ABA $\mathcal{F}$, there is no argument that concludes diag(pa, pbc). So, the argument isn't entailed by HEPAR-ABA $\mathcal{F}$ (i.e., $\mathcal{F} \neq_{x \in\{c r, g r, i d\}}$ diag(pa, pbc)).

## 6. Unifying the ABA $\mathcal{F}$ and the Naïve BN $\mathcal{N}$

Let $O_{\mathcal{F}}$ be a set of evidences for the ABA $\mathcal{F}, O_{\mathcal{N}}$ be a set of evidences for the naïve $\mathrm{BN} \mathcal{N}$, which is implemented using Problog. $O=O_{\mathcal{F}} \cup O_{\mathcal{N}}$ contains all evidences from $\mathcal{F}$ and $\mathcal{N}$. Underlying a language $\mathcal{L}$, vocabulary of $\mathcal{F}$ has literals of the form $f\left(p_{1}, \ldots, p_{n}\right)$ while vocabulary of $\mathcal{N}$ has nodevalue pairs of the form $v(x)$ where $v$ is a node of $\mathcal{N}$ and $x$ is a value of $v$. The problem is to determine correspondence between $\mathcal{F}$ and $\mathcal{N}$ based on specific domain. Querying a proposition $\pi$ to $\mathcal{F}$ and $\mathcal{N}, \pi$ is transformed into a literal denoted as $\pi_{\mathcal{F}}$ and a node-value pair denoted as $\pi_{\mathcal{N}}$. Intuitively, $\pi_{\mathcal{F}}$ and $\pi_{\mathcal{N}}$ are correspondence.

### 6.1 Interface Specification

This section describes interface specification as a solution to the previous problem. We apply online terminologies (SNOMED-CT and WordNet) to determine their correspondence by mapping from node-value pairs of the naïve $\mathrm{BN} \mathcal{N}$ to literals of the ABA $\mathcal{F}$.

Definition 6: Interface specification is triple, $\oplus=$ $\left(F^{\oplus}, N^{\oplus}, M^{\oplus}\right)$ where $F^{\oplus}$ is a set of literals of an $A B A \mathcal{F}$, $N^{\oplus}$ is a set of node-value pairs of a naïve $\mathrm{BN} \mathcal{N}$ and $M^{\oplus} \subseteq N^{\oplus} \times F^{\oplus}$ is a total mapping from $N^{\oplus}$ to $F^{\oplus}$.

The mapping proceeds according to the following steps of method MapFromBNtoABA.
(i) Assign an empty set into $M^{\oplus}$.
(ii) Take a node-pair $\delta \in N^{\oplus}$.
(iii) According to SNOMED-CT and WorldNet terminologies, determine whether literal $\theta \in F^{\oplus}$ corresponds nodevalue pair $\delta$ or not.
(iv) If they correspond then $(\delta, \theta)$ is added into $M^{\oplus}$.
(v) Until there is no literal in $F^{\oplus}$, go to step (iii).
(vi) Until there is no node-value pair in $N^{\oplus}$, go to step (ii).

Example 5: Suppose that we have an HEPAR-ABA $\mathcal{F}$ from Example 3 and Example 4 and HEPAR-NBN $\mathcal{N}$ as shown in Fig. 1. The total mapping from $\mathcal{N}$ to $\mathcal{F}$ is a set $M^{\oplus}=\{($ steatosis(present), diag(pa, steatosis)), (alcoholism(present), bsigns(pa, aabuse)), (alcoholism (present), dise(pa, aabuse)), (pbc(present), diag(pa, pbc)), (age(age31_50), age(pa, 45)), (sex(female), sex(pa, female)), (fatigue(present), comp(pa, fatigue)) $\}$.
So the ABA $\mathcal{F}$ and the naïve $\mathrm{BN} \mathcal{N}$ are correspondence.

### 6.2 Inferring Proposition from Evidences

When the propositions $\pi_{\mathcal{F}}$ and $\pi_{\mathcal{N}}$ are inferred by the ABA $\mathcal{F}$ and the naïve $\mathrm{BN} \mathcal{N}$ respectively, $\pi_{\mathcal{F}}$ and $\pi_{\mathcal{N}}$ are correspondence according to the mapping MapFromBNtoABA. There are four conditions to check whether $\mathcal{F}$ and $\mathcal{N}$ agree or conflict as shown in Table 5 where $x \in\{c r, g r, s k, i d\}$ is a semantic of the ABA framework.

Example 6: According to Example 4, there is no argument that concludes diag(pa, pbc) so HEPAR-ABA $\mathcal{F}$ doesn't entail diag(pa, pbc). Assume that a set of evidences for HEPAR-NBN $\mathcal{N}$ (see Fig. 1) is $O_{\mathcal{N}}=$ $\{$ age(age31_50), sex( female), alcoholism(absent), fatigue(present) $\}$. When we infer pbc(present) by HEPAR-NBN $\mathcal{N}$, the probability of pbc(present) given

Table 5 Reasoning by the ABA $\mathcal{F}$ and the naïve BN $\mathcal{N}$


$O_{\mathcal{N}}$ is 0.7 using Eq. (1). Therefore HEPAR-ABA $\mathcal{F}$ and HEPAR-NBN $\mathcal{N}$ conflict.

Suppose that we add $\mathrm{du}(\mathrm{pa}, \mathrm{cl}, \mathrm{cr})$ as an evidence into $O_{\mathcal{F}}$ (i.e., $O_{\mathcal{F}}=O_{\mathcal{F}} \cup\{\mathrm{du}(\mathrm{pa}, \mathrm{cl}, \mathrm{cr})\}$ ). Firstly, an inference rule of the form $\mathrm{du}(\mathrm{pa}, \mathrm{cl}, \mathrm{cr}) \leftarrow$ is added into $\mathcal{R}$. Secondly, an argument $\left(\left\{\gamma_{\text {diag( } p a, p b c}\right\}\right.$, diag( $\left.p a, p b c\right)$ ) is grounded acceptable by HEPAR-ABA $\mathcal{F}$ (i.e., $\mathcal{F} \vdash_{\text {gr }}$ diag(pa, pbc)). Thus, HEPAR-ABA $\mathcal{F}$ and HEPAR-BN $\mathcal{N}$ agree.

## 7. Conflict Resolution

Given the set of evidences $\mathcal{O}=O_{\mathcal{F}} \cup O_{\mathcal{N}}$, the ABA $\mathcal{F}$ and the naïve BN $\mathcal{N}$ conflict iff $\mathcal{F}$ entails (resp. doesn't entail) $\pi_{\mathcal{F}}$ while the probability of $\pi_{\mathcal{N}} ; P\left(\pi_{\mathcal{N}} \mid O_{\mathcal{N}}\right)$, is less than or equal to 0.5 (resp. greater than 0.5 ). We solve the conflicts by formalizing and integrating $\mathcal{F}$ and $\mathcal{N}$ using the PABA framework.

### 7.1 Structuring the ABA $\mathcal{F}$ and the Naïve BN $\mathcal{N}$ by the PABA Framework

The PABA framework includes probabilistic part (i.e., a set of probabilistic assumptions $\mathcal{A}_{p}$ and a set of probabilistic rules $\mathcal{R}_{p}$ ) and logical part (i.e., an ABA $\mathcal{F}$ ). At this point, we can formalize the $\operatorname{ABA} \mathcal{F}=(\mathcal{R}, \mathcal{A}, \overline{ })$ and the naïve BN $\mathcal{N}$ in their respective PABAs.

For the ABA $\mathcal{F}$, it does not contain uncertainties so there is no $\mathcal{A}_{p}$ and $\mathcal{R}_{p}$ (i.e., $\mathcal{A}_{p}=\emptyset$ and $\mathcal{R}_{p}=\emptyset$ ). A PABA framework that structures the $\operatorname{ABA} \mathcal{F}$ is $\mathcal{P}^{1}=(\emptyset, \emptyset, \mathcal{F})$.

Example 7: The PABA framework, which structures HEPAR-ABA $\mathcal{F}$ from Example 4, is denoted as HEPARPABA $\mathcal{P}^{1}$ in which its $\mathcal{A}_{p}$ and $\mathcal{R}_{p}$ are empties. So, the HEPAR-PABA is $\mathcal{P}^{1}=(\emptyset, \emptyset, \mathcal{F})$.

For the naïve $\mathrm{BN} \mathcal{N}$, it is concerned about uncertainties so a PABA framework that structures the naïve $\mathrm{BN} \mathcal{N}$ is $\mathcal{P}^{2}=\left(\mathcal{A}_{p}, \mathcal{N},(\emptyset, \emptyset, \emptyset)\right)$. Here, a node of $\mathcal{N}$ may has multiple values (i.e., mutual exclusive) so all node-value pairs ${ }^{1}$ of $\mathcal{N}^{6}$ (instead of nodes) is taken as probabilistic assumptions of $\mathcal{A}_{p} . \mathcal{N}^{7}$ is subsumed in $\mathcal{R}_{p}$. There is no ABA framework in $\mathcal{P}^{2}$ so its ABA framework is $(\emptyset, \emptyset, \emptyset)$. According to Definition 5, $\mathcal{P}^{2}=\left(\mathcal{A}_{p}, \mathcal{N},(\emptyset, \emptyset, \emptyset)\right)$ is a Bayesian PABA.

Example 8: Using the PABA framework, it structures HEPAR-NBN $\mathcal{N}$ of Fig. 1, and it is denoted as HEPAR-PABA $\mathcal{P}^{2}$. Let pbcp be pbc(present), pbcab be pbc(absent), sf be sex(female), sm be sex(male), alcop be alcoholism(present), aab be alcoholism(absent), age@ be age(age0_age30), age31 be age(age31_age50), age51 be age(age51_age65), age65 be age(age65_100), fp be fatigue(present), fab be fatigue(absent), amap be ama(present), amaab be ama(absent), spp be spiders(present), spab be spider(absent), pap be palms(present), paab be

[^0]palms(absent), hepp be hepatomegaly(present) and hepab be hepatomegaly(absent). And, they are taken as probabilistic assumptions of $\mathcal{A}_{p}$. HEPAR-NBN $\mathcal{N}$ is subsumed in $\mathcal{R}_{p}$ but the logical part of PABA $\mathcal{P}^{2}$ is empty. So, HEPAR-PABA $\mathcal{P}^{2}=\left(\mathcal{A}_{p}, \mathcal{N},(\emptyset, \emptyset, \emptyset)\right)$ is a Bayesian PABA framework.

### 7.2 Integrating Two PABA Frameworks

This section provides some extra notations. $O_{\mathcal{N}}=$ $\left\{o_{1}, \ldots, o_{k}\right\}$ and $O_{\mathcal{F}}=\left\{o_{k+1}, \ldots, o_{n}\right\}$ are sets of evidences for the naïve $\mathrm{BN} \mathcal{N}$ and the $\mathrm{ABA} \mathcal{F}$ respectively. $\pi$ is a proposition that is converted into $\pi_{\mathcal{F}}$ and $\pi_{\mathcal{N}}$ for inferring the ABA $\mathcal{F}$ and the naïve $\mathrm{BN} \mathcal{N}$ respectively. According to the method MapFromBNtoABA, $\pi_{\mathcal{F}}$ and $\pi_{\mathcal{N}}$ are correspondence and $O_{\mathcal{F}}$ and $O_{\mathcal{N}}$ are correspondence. $p\left(\pi_{\mathcal{N}}, o_{1}, \ldots, o_{k}\right)$ and $p\left(o_{1}, \ldots, o_{k}\right)$ are literals that is referred to the joint probability of $\pi_{\mathcal{N}}, o_{1}, \ldots, o_{k}$ and the marginal probability of $o_{1}, \ldots, o_{k}$ respectively. For instance, $\mathrm{p}(\mathrm{pbcp}$, age $31, \mathrm{sf}, \mathrm{aab}, \mathrm{fp})$ and $\mathrm{p}(\mathrm{age} 31, \mathrm{sf}, \mathrm{aab}, \mathrm{fp})$ are literals, which is referred to joint and marginal probabilities computed by BN's Eq. (1). $\operatorname{probid}(X, Y)^{\uparrow \uparrow \uparrow}$ is a literal that returns a probability $Y$ of $X$ being acceptable by a PABA framework. $\operatorname{pr}\left(\pi_{\mathcal{N}}, o_{1}, \ldots, o_{k}, Z\right)$ is a literal that is referred to the posterior probability of $\pi_{\mathcal{N}}$ given $o_{1}, \ldots, o_{k}$ where $Z$ is a probability between 0 and 1. $\operatorname{predict}\left(\pi_{\mathcal{N}}, o_{1}, \ldots, o_{k}, X\right)$ is a literal denoting that $\pi_{\mathcal{N}}$ is predicted to be true (resp. false) if $Z$ is greater than 0.5 (resp. if $Z$ is either less than or equal to 0.5 ) where $X \in\{$ true, false $\}$. is HasEvidence $\left(o_{1}, \ldots, o_{k}\right)$ is an atom for checking whether evidences, $o_{1}, \ldots, o_{k}$, are included in $O_{\mathcal{N}}$.

Now, we combine PABAs $\mathcal{P}^{1}=(\emptyset, \emptyset, \mathcal{F})$ and $\mathcal{P}^{2}=$ $\left(\mathcal{A}_{p}, \mathcal{N},(\emptyset, \emptyset, \emptyset)\right.$ ) into $\mathcal{P}^{r}=\left(\mathcal{A}_{p}^{r}, \mathcal{R}_{p}^{r}, \mathcal{F}^{\prime}\right)$, where $\mathcal{F}=$ $(\mathcal{R}, \mathcal{A}, \overline{\text { - })}$ and $\mathcal{F}^{\prime}=\left(\mathcal{R}^{\prime}, \mathcal{A}^{\prime}, \overline{ }^{\prime}\right)$ are ABA frameworks.

Definition 7: $\mathcal{P}^{r}=\left(\mathcal{A}_{p}^{r}, \mathcal{R}_{p}^{r}, \mathcal{F}^{\prime}\right)$ is a PABA framework, which integrates PABAs $\mathcal{P}^{1}=(\emptyset, \emptyset, \mathcal{F})$ and $\mathcal{P}^{2}=$ $\left(\mathcal{A}_{p}, \mathcal{N},(\emptyset, \emptyset, \emptyset)\right)$.

Example 9: (Continue to Example 6) Given a set of evidences $O=O_{\mathcal{F}} \cup O_{\mathcal{N}}$, HEPAR-ABA $\mathcal{F}$ from Example 3 to Example 4 and HEPAR-NBN (see Fig. 1) conflicts in querying whether a patient suffers primary biliary cirrhosis or not because $\mathcal{F}$ doesn't entail diag(pa, pbc) but probability of pbc given a set of evidences $O_{\mathcal{N}}$ is 0.7 (see Example 6). To solve such conflict, we combine HEPAR-PABAs $\mathcal{P}^{1}=(\emptyset, \emptyset, \mathcal{F})$ from Example 7 and $\mathcal{P}^{2}=\left(\mathcal{A}_{p}, \mathcal{N},(\emptyset, \emptyset, \emptyset)\right)$ from Example 8 into the integrated HEPAR-PABA $\mathcal{P}^{r}=$ $\left(\mathcal{A}_{p}^{r}, \mathcal{R}_{p}^{r}, \mathcal{F}^{\prime}\right)$ where $\mathcal{F}=\left(\mathcal{R}, \mathcal{A}, \overline{ }^{\prime}\right)$ and $\mathcal{F}^{\prime}=\left(\mathcal{R}^{\prime}, \mathcal{A}^{\prime}, \overline{ }^{\prime}\right)$ are ABA frameworks.
$\mathcal{A}_{p}$ of $\mathcal{P}^{2}$ is assigned into $\mathcal{A}_{p}^{r}$ of $\mathcal{P}^{r}$ so $\mathcal{A}_{p}^{r}$ consists of all probabilistic assumptions of $\mathcal{A}_{p} . \mathcal{N}$ of $\mathcal{P}^{2}$ is subsumed in place of $\mathcal{R}_{p}^{r}$ of $\mathcal{P}^{r}$. And $\mathcal{F}$ of $\mathcal{P}^{1}$ is assigned into $\mathcal{F}^{\prime}$ of $\mathcal{P}^{r}$. In $\operatorname{ABA} \mathcal{F}^{\prime}=\left(\mathcal{R}^{\prime}, \mathcal{A}^{\prime}, \overline{ }^{\prime}\right), \mathcal{R}^{\prime}$ consists of all rules of $\mathcal{R}$ of $\mathcal{F}$

[^1]
[^0]:    ${ }^{1}$ Node-value pair is written as $v(x)$ where $v$ is a node of $\mathcal{N}$ and $x$ is a value of $v$.
    ${ }^{1 \dagger} \mathcal{N}$ is implemented using Problog.

[^1]:    ${ }^{1}$ ) $\operatorname{probid}(X, Y)$ of PRENGINE [37], [38] is used for computing an acceptable probability $Y$ of $X$ by the PABA framework.

and the following additional rules.

- For literal $p\left(\pi_{N}, o_{1}, \ldots, o_{k}\right)$, we add the following inference rule is added into $\mathcal{R}^{\prime}$.

$$
p\left(\pi_{N}, o_{1}, \ldots, o_{k}\right) \leftarrow \pi_{N}, o_{1}, \ldots, o_{k}
$$

- For literal $p\left(o_{1}, \ldots, o_{k}\right)$, we add the following inference rule into $\mathcal{R}^{\prime}$.

$$
p\left(o_{1}, \ldots, o_{k}\right) \leftarrow o_{1}, \ldots, o_{k}
$$

- For literal $p r\left(\pi_{N}, o_{1}, \ldots, o_{k}, Z\right)$, we add the following inference rule into $\mathcal{R}^{\prime}$.

$$
\begin{gathered}
p r\left(\pi_{N}, o_{1}, \ldots, o_{k}, Z\right) \leftarrow \operatorname{probid}\left(p\left(\pi_{N}, o_{1}, \ldots, o_{k}\right), X\right) \\
\operatorname{probid}\left(p\left(o_{1}, \ldots, o_{k}\right), Y\right) \\
Z \text { is } X / Y
\end{gathered}
$$

- For each literal $\operatorname{predict}\left(\pi_{N}, o_{1}, \ldots, o_{k}, X\right)$, we add the following inference rules are added into $\mathcal{R}^{\prime}$.

$$
\begin{gathered}
\operatorname{predict}\left(\pi_{N}, o_{1}, \ldots, o_{k}, X\right) \leftarrow p r\left(\pi_{N}, o_{1}, \ldots, o_{k}, Z\right) \\
Z>0.5, X \text { is true } \\
\operatorname{predict}\left(\pi_{N}, o_{1}, \ldots, o_{k}, X\right) \leftarrow p r\left(\pi_{N}, o_{1}, \ldots, o_{k}, Z\right) \\
Z=<0.5, X \text { is false }
\end{gathered}
$$

- Since the naïve $\mathrm{BN} \mathcal{N}$ predicts either $\pi_{N}$ or $\neg \pi_{N}$ based on the set of evidences $O_{N}$, we create the following defeasible rules by putting two assumptions $\gamma_{b n \_ \text {predict }\left(\pi_{N}\right)}$ and $\gamma_{b n \_ \text {predict }\left(\neg \pi_{N}\right)}$ in the bodies of the rules respectively. And they are added into $\mathcal{R}^{\prime}$.

$$
\begin{gathered}
b n \_ \operatorname{predict}\left(\pi_{N}\right) \leftarrow \operatorname{predict}\left(\pi_{N}, o_{1}, \ldots, o_{k}, \text { true }\right) \\
\gamma_{b n \_ \operatorname{predict}\left(\pi_{N}\right)} \\
b n \_\operatorname{predict}\left(\neg \pi_{N}\right) \leftarrow \operatorname{predict}\left(\pi_{N}, o_{1}, \ldots, o_{k}, \text { false }\right) \\
\gamma_{b n \_\operatorname{predict}\left(\neg \pi_{N}\right)}
\end{gathered}
$$

- Similarly, since ABA $\mathcal{F}$ entails either $\pi_{\mathcal{F}}$ or $\neg \pi_{\mathcal{F}}$ based on the set of evidences $O_{\mathcal{F}}$, we create the following defeasible rules by putting two assumptions $\gamma_{\text {aba predict }\left(\pi_{\mathcal{F}}\right)}$ and $\gamma_{\text {aba predict }\left(\neg \pi_{\mathcal{F}}\right)}$ in the bodies of the rules respectively. And they are added into $\mathcal{R}^{\prime}$.

$$
\begin{aligned}
& \text { aba_predict }\left(\pi_{\mathcal{F}}\right) \leftarrow \pi_{\mathcal{F}}, \gamma_{\text {aba } \_ \text {predit }\left(\pi_{\mathcal{F}}\right)} \\
& \text { aba_predict }\left(\neg \pi_{\mathcal{F}}\right) \leftarrow \neg \pi_{\mathcal{F}}, \gamma_{\text {aba } \_ \text {predit }\left(\neg \pi_{\mathcal{F}}\right)}
\end{aligned}
$$

- Actually, we can say that the naïve $\mathrm{BN} \mathcal{N}$ predicts $\pi_{N}$ (resp. $\neg \pi_{N}$ ) is wrong if $\mathrm{ABA} \mathcal{F}$ entails $\neg \pi_{\mathcal{F}}$ (resp. $\pi_{\mathcal{F}}$ ) and $\mathcal{N}$ is insufficient. The following inference rules are added into $\mathcal{R}^{\prime}$.

$$
\begin{aligned}
& \neg \gamma_{b n \_ \text {predict }\left(\pi_{N}\right)} \leftarrow \neg \pi_{\mathcal{F}}, \sim b n \_ \text {sufficient } \\
& \neg \gamma_{b n \_ \text {predict }\left(\neg \pi_{N}\right)} \leftarrow \pi_{\mathcal{F}}, \sim b n \_ \text {sufficient }
\end{aligned}
$$

- Similarly, $\mathrm{ABA} \mathcal{F}$ predicts $\pi_{\mathcal{F}}$ (resp. $\neg \pi_{\mathcal{F}}$ ) is wrong if the naïve $\mathrm{BN} \mathcal{N}$ predicts $\neg \pi_{N}$ (resp. $\pi_{N}$ ) and $\mathcal{N}$ is sufficient. So we add the following defeasible rules into $\mathcal{R}^{\prime}$ in which we assume bn_sufficient as an assumption.

$$
\begin{aligned}
& \neg \gamma_{\text {aba predict }\left(\pi_{\mathcal{F}}\right)} \leftarrow \operatorname{predict}\left(\pi_{N}, o_{1}, \ldots, o_{k}, \text { false }\right) \\
& \text { bn_sufficient } \\
& \neg \gamma_{\text {aba predict }\left(\neg \pi_{\mathcal{F}}\right)} \leftarrow \operatorname{predict}\left(\pi_{N}, o_{1}, \ldots, o_{k}, \text { true }\right) \\
& \text { bn_sufficient }
\end{aligned}
$$

- The naïve $\mathrm{BN} \mathcal{N}$ is insufficient if evidences of $O_{N}$ aren't related to node-value pairs of $\mathcal{N}^{\oplus}$ or there is no evidences in $O_{N}$. Then we assume that evidences of $O_{N}$ are unknown. So, we add a defeasible rule of the form $\neg$ bn_sufficient $\leftarrow$ bn_evidence(unknown) into $\mathcal{R}^{\prime}$ where bn_evidence(unknown) is taken as an assumption.
- If $O_{N}$ contains node-value pairs of $\mathcal{N}^{\oplus}$ as a set of evidences then we can say that evidences of $O_{N}$ are known. So we add the following inference rule into $\mathcal{R}^{\prime}$.

$$
\begin{aligned}
\neg b n \_ \text {evidence(unknown) } & \leftarrow i s \text { HasEvidence }\left(o_{1}, \ldots\right. \\
& \left.o_{k}\right)
\end{aligned}
$$

- Since $\pi$ is the original proposition that is transformed into $\pi_{\mathcal{F}}$ and $\pi_{N}$, we infer $\pi$ as a query into $\operatorname{PABA} \mathcal{P}^{\prime}$. We added the following four inference rules into $\mathcal{R}^{\prime}$.

$$
\begin{aligned}
& \pi \leftarrow b n \_ \operatorname{predict}\left(\pi_{N}\right) \quad \neg \pi \leftarrow b n \_ \operatorname{predict}\left(\neg \pi_{N}\right) \\
& \pi \leftarrow a b a \_ \operatorname{predict}\left(\pi_{\mathcal{F}}\right) \quad \neg \pi \leftarrow a b a \_ \operatorname{predict}\left(\neg \pi_{\mathcal{F}}\right)
\end{aligned}
$$

$\mathcal{A}^{\prime}$ consists of all assumptions of $\mathcal{A}$ of $\mathcal{F}$ and new assumptions; $\gamma_{b n \_ \text {predict }\left(\pi_{N}\right)}, \gamma_{b n \_ \text {predict }\left(\neg \pi_{N}\right)}, \gamma_{\text {aba predict }\left(\pi_{\mathcal{F}}\right)}$, $\gamma_{\text {aba predict }\left(\neg \pi_{\mathcal{F}}\right)}$, bn_sufficient and bn_evidence(unknown). $\mathcal{F}^{\prime}$ contains contraries of $\mathcal{F}$ and additional contraries of new assumptions. The additional contraries are

$$
\begin{aligned}
& \overline{\gamma_{b n \_ \text {predict }\left(\pi_{N}\right)}}=\neg \gamma_{b n \_ \text {predict }\left(\pi_{N}\right)} \\
& \overline{\gamma_{b n \_ \text {predict }\left(\neg \pi_{N}\right)}}=\neg \gamma_{b n \_ \text {predict }\left(\neg \pi_{N}\right)} \\
& \overline{\gamma_{\text {aba predict }\left(\pi_{\mathcal{F}}\right)}}=\neg \gamma_{\text {aba predict }\left(\pi_{\mathcal{F}}\right)} \\
& \overline{\gamma_{\text {aba predict }\left(\neg \pi_{\mathcal{F}}\right)}}=\neg \gamma_{\text {aba predict }\left(\neg \pi_{N}\right)} \\
& \overline{b n \_ \text {sufficient }}=\neg b n \_ \text {sufficient and } \\
& \overline{\text { bn_evidence(unknown) }}=\neg \text { bn_evidence(unknown). }
\end{aligned}
$$

Example 10: (Continue Example 9) In the integrated HEPAR-PABA $\mathcal{P}^{\prime}=\left(\mathcal{A}_{p}^{\prime}, \mathcal{R}_{p}^{\prime}, \mathcal{F}^{\prime}\right), \mathcal{A}_{p}^{\prime}$ consists of all assumption of $\mathcal{A}_{p}$ (see Example 8). $\mathcal{R}_{p}^{\prime}$ subsumes $\mathcal{N}$ (see Fig. 1). Let pa_pbc be a proposition to be queried by $\mathcal{P}^{\prime}$. $\mathcal{R}^{\prime}$ contains all rules of $\mathcal{R}$ of HEPAR-ABA $\mathcal{F}$ (see. Example 3 and Example 4) and additional rules, which are as follows.



$\mathcal{A}^{\prime}$ contains all assumptions of $\mathcal{A}$ of HEPAR-ABA $\mathcal{F}$ and six new assumptions, which are $\gamma_{\text {bn.predict( } p b c p)}$, $\gamma_{\text {bn.predict }(\sim p b c p)}$, $\gamma_{\text {aba.predict(diag( } p a, p b c))}$, bn.sufficient and $\gamma_{\text {aba.predict }(\sim \text { diag }(\text { pa, pb }))}$ and bn.evidence(unknown). $\mathcal{F}^{\prime}$ contains contraries from $\mathcal{F}$ and the following contraries of new assumptions.

$$
\begin{aligned}
& \overline{\gamma_{\text {bn.predict }}(p b c p)}=\sim \gamma_{\text {bn.predict }(p b c p)} \\
& \overline{\gamma_{\text {bn.predict }(\sim p b c p)}}=\sim \gamma_{\text {bn.predict }(\sim p b c p)} \\
& \overline{\gamma_{\text {aba.predict }(\text { diag }(\text { pa, pb }))}}=\sim \gamma_{\text {aba.predict }(\text { diag }(\text { pa, pb })} \\
& \overline{\gamma_{\text {aba.predict }(\sim \text { diag }(\text { pa, pb })}}=\sim \gamma_{\text {aba.predict }(\sim \text { diag }(\text { pa, pb })} \\
& \overline{\text { bn.sufficient }}=\sim \text { bn.sufficient } \\
& \overline{\text { bn.evidence(unknown) }}=\sim \text { bn.evidence(unknown) }
\end{aligned}
$$

Using PRENGINE [37], [38], our approach is implemented to investigate a conflict resolution when ABA $\mathcal{F}$ and the naïve $\mathrm{BN} \mathcal{N}$ conflict each other. After PABAs $\mathcal{P}^{1}$ for $\mathrm{ABA} \mathcal{F}$ and $\mathcal{P}^{2}$ for the naïve $\mathrm{BN} \mathcal{N}$ have been combined into the integrated $\mathrm{PABA} \mathcal{P}^{\prime}$, the conflicts between $\mathrm{ABA} \mathcal{F}$ and the naïve $\mathrm{BN} \mathcal{N}$ are solved. Assume that probidIntegrate $\left(\pi, \pi_{\mathcal{F}}, \pi_{\mathcal{N}}, o_{1}, . ., o_{k}, R\right)$ is a literal that returns the probability $R$ of proposition $\pi$ which is entailed by the integrated $\mathrm{PABA} \mathcal{P}^{\prime}$.

Example 11: (Continue Example 10) Using PRENGINE [37], [38], proposition pa_pbc is being acceptable by the integrated HEPAR-PABA $\mathcal{P}^{\prime}$ with acceptable probability 1. When atom probidIntegrate(pa_pbc, $\operatorname{diag}(p a, p b c),[p b c p],[\operatorname{age} 31, s f, a a b, f p], R)$ is called, it results 0.73 . So, our approach determines that the diagnosis of the patient is PBC.

According to Definition 5, the integrated PABA $\mathcal{P}^{\prime}$ is a Bayesian PABA because it subsumes the naïve $\mathrm{BN} \mathcal{N}$ in $\mathcal{R}_{p}$ and probabilistic assumptions correspond to all nodes of $\mathcal{N}$ as node-value pairs. And $\mathrm{PABA} \mathcal{P}^{\prime}$ satisfies that each probabilistic assumption of $\mathcal{A}_{p}^{\prime}$ is not an assumption in $\mathcal{F}^{\prime}$ and doesn't occur in the head of any inference rule in $\mathcal{F}^{\prime}$.

## 8. Experimental Result

We implement our approach, which combines HEPAR-ABA and HEPAR-NBN (i.e., inputs of our approach), regrading to the diagnosis of liver disorders and biliary tract. HEPARABA is an ABA framework, which structures HEPAR-RB. HEPAR-RB is a rule-based system, which is developed by LUCAS [24], [25], having 178 rules about the diagnosis of liver disorders and biliary tracts. Meanwhile, we construct HEPAR-NBN (i.e., a naïve BN) by learning one hundred records $^{7}$ of liver disorders patients.

The testing dataset of our approach contains forty-two patients' records for primary biliary cirrhosis and seven patients' records for steatosis hepatitis in which two patients suffer both disorders. The dataset also includes fifty-three patients' records for other liver disorders. We evaluate our approach by comparing its performance with the performance of HEPAR-NBN and HEPAR-ABA testing on the diagnosis of primary biliary cirrhosis and steatosis hepatitis. We compute confusion matrix, recall, precision, f-measure and accuracy for each HEPAR-NBN, HEPAR-ABA and our approach. For the diagnosis of primary biliary cirrhosis, Table 6 and Table 7 show the confusion matrix and the results of recall, precision, f-measure and accuracy of HEPARNBN, respectively. Table 8 and Table 9 show the confusion matrix and the results of recall, precision, f-measure

Table 6 Confusion matrix of HEPAR-NBN for primary biliary cirrhosis


Table 7 Recall/precision/f-measure/accuracy of HEPAR-NBN for primary biliary cirrhosis


Table 8 Confusion matrix of HEPAR-ABA for primary biliary cirrhosis


Table 9 Recall/precision/f-measure/accuracy of HEPAR-ABA for primary biliary cirrhosis


[^0]
[^0]:    ${ }^{7}$ Using GENIE/SMILE software, one hundred patients' records are extracted from the orignal HEPAR-BN, which is developed by ONIESKO [26].

Table 10 Confusion matrix of our approach for primary biliary cirrhosis


Table 11 Recall/precision/f-measure/accuracy of our approach for primary biliary cirrhosis


Table 12 Confusion matrix of HEPAR-NBN for steatosis hepatitis


Table 13 Recall/precision/f-measure/accuracy of HEPAR-NBN for steatosis hepatitis


Table 14 Confusion matrix of HEPAR-ABA for steatosis hepatitis


Table 15 Recall/precision/f-measure/accuracy of HEPAR-ABA for steatosis hepatitis


and accuracy of HEPAR-ABA, respectively. Table 10 and Table 11 show the confusion matrix and the results of recall, precision, f-measure and accuracy of HEPAR-ABA, respectively. For the diagnosis of steatosis hepatitis, Let diag(pa, steat) be a proposition to be entailed by HEPARABA and pa_steat be a proposition to be entailed by our approach. Table 12 and Table 13 show the confusion matrix and the results of recall, precision, f-measure and accuracy of HEPAR-NBN, respectively. Table 14 and Table 15 show the confusion matrix and the results of recall, precision, f-measure and accuracy of HEPAR-ABA, respectively. Table 16 and Table 17 show the confusion matrix and the results of recall, precision, f-measure and accuracy of HEPAR-ABA, respectively.

The main objective of our approach is to combine total

Table 16 Confusion matrix of our approach for steatosis hepatitis


Table 17 Recall/precision/f-measure/accuracy of our approach for steatosis hepatitis


conflict and different knowledge representations efficiently, especially an RB and a naïve BN. So, our approach outperforms the other methods in the combination as a conflict resolution for these representations. One of the advantages of our approach is that the performance of HEPAR-NBN can be improved when the evidences for HEPAR-NBN are insufficient to predict liver disorders. In the base case, we assume that HEPAR-NBN does not have evidence to predict a diagnosis. Then the accuracy of HEPAR-NBN decreases to 0 . However, our approach predicts the liver disorder from HEPAR-ABA. So, the accuracy of our approach gets $82 \%$ and $80 \%$ for the diagnosis of primary biliary cirrhosis and steatosis hepatitis, respectively. We approve that our approach is comparative to the accuracy of the BN and more accurate than the result of the ABA framework.

## 9. Conclusion

Even there exist some frameworks on handling probability in logic programing, there are very few works on knowledge integration for probabilistic argumentation. We combine an ABA framework, which is converted from an RB, with a naïve BN using a probabilistic Argumentation, especially the PABA framework. Based on a specific domain, the ABA framework is certain, while the naïve BN covers uncertainties so we investigate an approach to integrate them. The conflict between the RB and the naïve BN is solved by the semantics of the PABA framework using PRENGINE [37], [38]. As an application area, we integrate HEPAR-RB and HEPAR-NBN, which are related to the diagnosis of liver disorders. However, our approach has two limitations. Our approach requires either a naïve BN or a dataset to generate the naïve BN. One limitation is that unreliable naïve BN or dataset may impact the performance of our approach. Another limitation is that mapping from the naïve Bayesian network to the ABA framework may vary based on the terminologies.

## Acknowledgments

We would like to offer our special thanks to Dr. Peter Lucas, Extraordinary professor of Artificial intelligence, Leiden Institute for Advanced Computer Science, Leiden University for his kindness and providing the HEPAR rule-based sys-

tem to be applied in this research.
