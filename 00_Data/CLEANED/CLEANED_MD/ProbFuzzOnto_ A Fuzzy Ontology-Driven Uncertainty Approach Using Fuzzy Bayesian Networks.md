# ProbFuzzOnto: A Fuzzy Ontology-Driven Uncertainty Approach Using Fuzzy Bayesian Networks 

Ishak Riali ${ }^{1} \cdot$ Messaouda Fareh ${ }^{1} \cdot$ Fernando Bobillo ${ }^{2,3}$


#### Abstract

The need to deal with uncertain semantics is rising in importance in most of the important technology trends, and consequently, many proposals have emerged as solutions in recent years. Fuzzy ontologies were proposed to remedy the limitations of standard ontologies using fuzzy logic to deal with vague and imprecise knowledge. Nevertheless, fuzzy ontologies cannot deal with probabilistic knowledge which is an important characteristic of most real-world applications. This paper proposes a novel solution that aims at enhancing the knowledge representation and reasoning in fuzzy ontologies. Indeed, the proposed solution is a probabilistic extension of fuzzy ontologies with Fuzzy Bayesian Networks (FBN) that we named Probabilistic Fuzzy Ontologies (ProbFuzzOnto). It takes into account vague, imprecise, and probabilistic knowledge simultaneously. Moreover, this paper proposes a process to guide ontology engineers step by step in building ProbFuzzOnto. Also, it provides reasoning algorithms to drive implicit knowledge by utilizing explicit knowledge stored in a fuzzy ontology based on fuzzy Bayesian inference. To show the usefulness of the proposed solution, a case study in Renal Cancer is presented.


[^0]Keywords Semantic representation $\cdot$ Uncertain knowledge $\cdot$ Fuzzy ontologies $\cdot$ Fuzzy Bayesian networks

## 1 Introduction

During recent years, a growing interest and large adoption of ontologies gave birth to the true potential of implementing a broad range of high-quality intelligent and communicating systems. Smart cities, Semantic Web services, the Internet of Things (IOT) and e-health are among various domains which are benefited from ontologies [1, 2]. As a need to make intelligent tasks, these systems perform automated reasoning and ensure the interoperability between them in heterogeneous environments of connected devices based on the expressiveness of an ontology. Despite the undisputed success of classical ontologies, they cannot model and reason with uncertain knowledge affected by randomness, vagueness, etc., which is presented in many real-world domains.

Fuzzy ontologies have emerged as a suitable formalism to cope with the problem of representing and invoking knowledge that is fuzzy and imprecise that may be inherent in real-world domains. Recently, they have been effectively used and proved to be sound and effective in domains where vagueness is prevalent [3] However, they are incapable of handling the probabilistic knowledge inherent in the field.

Fuzzy Bayesian networks have been proposed as an extension of the classical ones. FBNs make it possible to deal with fuzzy and/or probabilistic events by representing a collection of random variables (crisp or fuzzy) and their probabilistic relationships. Uncertainty and imprecision can be propagated throughout the network, enabling a more complex inference than traditional crisp Bayesian


[^0]:    Fernando Bobillo
    fbobillo@unizar.es
    Ishak Riali
    ishakriali@gmail.com
    Messaouda Fareh
    farehm@gmail.com
    1 LRDSI Laboratory, Faculty of Sciences, University of Blida 1, Blida, Algeria
    2 University of Zaragoza, Zaragoza, Spain
    3 Aragon Institute of Engineering Research (I3A), Zaragoza, Spain

networks. Several studies have demonstrated the advantages of FBNs in a variety of fields and applications, including the contributions reported in [4-9]. In addition to that, it should be noted that to address uncertainty in ontologies, the World Wide Web Consortium (W3C) has encouraged using hybrid models [10]. Actually, there have been some previous approaches for hybrid ontologies: fuzzy and possibilistic logic [11], fuzzy logic and rough sets [12], and Fuzzy logic and Dempster-Shafer [13]. Nevertheless, there is little attention paid to using probabilistic and fuzzy logic to deal with uncertain knowledge in ontologies. With that in mind, in this study, we clarify how to exploit the capabilities of FBNs to deal with the uncertainty in ontologies.

The performances of intelligent and communicating systems depend on the quality of the knowledge representation and mechanisms of reasoning provided in the presence of uncertainty. However, as a matter of fact, vague, imprecise, and probabilistic knowledge are common characteristics of most real-world problems and typically they appear simultaneously in many domains that are usually sought to be dealt with, where the likelihood of an occurrence is dependent on a fuzzy value. [14].

To illustrate that, assume that we want to build an intelligent system to help the assignment of patients in the various departments of a hospital (see Fig. 1). This is based on the different information captured by the devices (temperature, blood pressure, blood sugar, etc.) fixed in the "Emergency room network". The inputs of the system (patient data) are real-valued data, which will be fuzzified (as usual in fuzzy systems) and represented semantically in a sophisticated format in a fuzzy ontology and then will be processed to predict the patient's disease. Based on the predicted disease, the system will predict the most appropriate department to treat the patient and the corresponding probability. In the "Processing of data" module, several decision rules involve probabilistic knowledge attached to vague knowledge. For instance:

- IF a patient's blood pressure value is very high, THEN it is probable that the patient has a cardiac disease.
- If a patient is very old, has joint pain, abdominal pain, and jaundice, THEN it is probable that he has liver cancer.
- IF a patient has tiredness, has headache, has aches, has pains, and very hot body temperature, THEN it is likely that he has COVID-19.

In the examples mentioned above, the values very high, very old, and very hot are vague terms, while the terms probable and likely are probabilistic quantifiers. Hence, the most important challenge to cope with such situations is to develop hybrid solutions for the Semantic Web that use both probabilistic models and fuzzy logic to efficiently handle the richness of these domains and applications in terms of uncertainty.

The above motivating examples raise the following challenges:

- How to model the probabilistic semantics of a given fuzzy ontology?
- How to answer probabilistic queries under fuzzy knowledge in a given fuzzy ontology?
In order to face the above-mentioned challenges, this paper introduces a novel solution that enables representing and reasoning with ontological knowledge in domains with a lot of uncertainty. It takes into consideration vague and probabilistic knowledge simultaneously by combining FBNs and fuzzy ontologies to take advantages of both models. The major contributions of this paper can be summarized as follows:
- We introduce a probabilistic extension of fuzzy ontologies using FBN.
- We propose a process that encompasses the general phases for building Probabilistic Fuzzy Ontologies. We show step by step how the construction of Probabilistic Fuzzy Ontologies can be done.
![img-0.jpeg](img-0.jpeg)

Fig. 1 Overview of an intelligent guidance system

- We demonstrate fuzzy Bayesian inference in our proposal, which enables probabilistic reasoning under fuzzy knowledge.
- We discuss a practical use case in the domain of renal cancer.

The remainder of this article is organized as follows. Firstly, preliminaries are presented in Sect. 2, and Sect. 3 discusses the related work. Next, we detail our proposal: Sect. 4 explains how to build probabilistic fuzzy ontologies, Sect. 5 details how to reason with them, and Sect. 6 evaluates our approach on a case study. Finally, Sect. 7 presents some conclusions and perspectives.

## 2 Preliminaries

In this section, we will provide a brief overview of some essential background knowledge that will be utilized in the subsequent parts of the paper. This includes fuzzy logic, fuzzy Bayesian networks, and fuzzy ontologies.

### 2.1 Fuzzy Logic

Fuzzy logic is considered the appropriate model to cope with vague knowledge, which is about the imprecision related to the content of an item of information [15]. Fuzzy logic extends classical binary logic. It allows an element to belong to a fuzzy set with a partial degree of membership and represents human reasoning in a formal way, where reasoning rules can be expressed in natural language. Formally, each fuzzy set $F$ is characterized by a membership function $\mu_{F}$.
Definition 1 (Membership function). A membership function $\mu_{F}$ for a fuzzy set $F$ on the universe of discourse $\Omega$ is defined formally as:
$\mu_{F}: \Omega \rightarrow[0,1]$.
The membership function can take any value between 0 and 1 , with 0 indicating no membership and 1 indicating full membership.

### 2.2 Fuzzy Bayesian Networks

A fuzzy Bayesian network is a probabilistic model that combines elements of fuzzy logic with Bayesian networks. Bayesian networks [16-18] are a type of probabilistic model that represents the causal dependencies between different variables and can be used to make predictions based on uncertain or incomplete information. They are often used in artificial intelligence and machine learning to represent and reason with complex systems or domains.

By combining elements of fuzzy logic with Bayesian networks, a fuzzy Bayesian network allows for the representation of fuzzy or imprecise evidence in a probabilistic graphical model. This can be useful in situations where the available evidence is fuzzy, or where there is a need to represent complex or nuanced concepts that do not fit neatly into a traditional, binary classification system. In fact, they make it possible to deal with fuzzy evidence when dealing with probabilistic situations.

Definition 2 (Fuzzy Bayesian networks [19]) A Fuzzy Bayesian network $F z$ is an acyclic graph $G=(V, B)$, where

1. $V=\left\{V_{1}, \ldots, V_{m}\right\}$ is a set of the nodes (represent variables) of G , with $\mathrm{V}=\Phi \cup \Psi$, where

- $\Phi=\left\{F_{1}, \ldots, F_{k}\right\}$ is the set of the fuzzy variables of $F z$.
- $\Psi=\left\{C_{1}, \ldots, C_{t}\right\}$ is the set of the crisp variables of $F z$.
- $\Phi$ and $\Psi$ are disjoint.

2. $B=\left\{\left(V_{i}, V_{j}\right)\right\}$, with $V_{i}, V_{j} \in V$, is a set of edges. Each $\left(V_{i}, V_{j}\right) \in B$ represents a conditional dependency between $V_{i}$ and $V_{j}$.
A fuzzy Bayesian network contains also:

- The probability distribution of $F z$.
- A finite set of the membership functions $M f=$ $\left\{\mu_{F z 1}, \mu_{F z 2}, \ldots, \mu_{F z f}\right\}$ used to fuzzify fuzzy nodes.
Each node $V_{i} \in V$ has a set of finite states $S_{i}=\left\{v_{1}^{i}, \ldots, v_{a}^{i}\right\}$. If $V_{i}$ is fuzzy, a membership function $\mu_{F z i} \in M f$ will be associated with each $v_{i} \in S_{i}$, to fuzzify it.

Each node $V_{i} \in V$ has a probabilistic distribution:

- Prior Probability: when a node is a root node, or,
- Conditional Probability Table (CPT): when a node has parents.

Definition 3 (A Prior Table) The prior table PriorTab(Z) of a node $Z \in V$ is a set of pairs $\left\{\left(z_{1}, P_{1}\right), \ldots,\left(z_{a}, P_{a}\right)\right\}$, that link each state $z_{i} \in S$ with its prior likelihood $P_{i}$, with:

- $P_{i} \in[0,1]$ : defines the prior probability value.
- And, $\sum_{i} P_{i}=1$.

Definition 4 (A Conditional Probability Table). Given a FBN $F z$, each node $\mathrm{Z} \in \mathrm{V}$ has a Conditional Probability Table $\operatorname{CdTab}(Z)$, which contains a set of conditional probabilities $\left\{\left(z_{1}, n o_{1}, v e_{1}, P_{1}\right), \ldots,\left(z_{a}, n o_{a}, v e_{a}, P_{a}\right)\right\}$, with:

- $z_{i} \in S$ : defines a state of the node Z .
- $n o_{i} \in V$ : defines the evidence about nodes.
- $v e_{i}$ : defines the states of the evidence nodes.

- $P_{i} \in[0,1]$ : is the value of conditional probability.

Definition 5 (Bayesian inference [19]) Given a FBN Fz, the aim of Bayesian inference is to compute the probability of a query node $Z_{i}$ based on a given evidence $\mathbf{e}$ (hard or fuzzy) on some evidence nodes $\left\{Z_{1}, \ldots, Z_{m}\right\} \subset V$. The challenge is to determine the likelihood probability of the following event using the Bayes theorem:
$P\left(Z_{i}=z_{j} \mid \mathbf{e}\right)=\frac{P\left(\mathbf{e} \mid Z_{i}=z_{j}\right) \cdot P\left(Z_{i}=z_{j}\right)}{P(\mathbf{e})}$.
Hard evidence, also known as strong evidence or conclusive evidence, refers to information that is clear, precise, and reliable. Hard evidence is typically objective and is not subject to interpretation or subjective bias. It is considered more reliable and persuasive than other types of evidence.

Examples of hard evidence include DNA evidence in a criminal case, eyewitness testimony, and physical evidence such as fingerprints or surveillance footage.

Definition 6 (Hard evidence [20]) Given a FBN Fz, a hard evidence he on a node $\mathbf{Z} \in F z$ is represented as a vector of size $a=|S|$. It contains:

- The value 1 at the position $i$ corresponds to a state $z_{i} \in S$, and
- The value 0 in the other positions.

Hard evidence is the formal way of saying that a particular node $Z$ can only possibly be in one state $z_{i}$. It is characterized by:
$\mathbf{h e}=\left(z_{0}=0, \ldots, z_{i}=\mathbf{1}, \ldots, z_{|S|}=0\right) \Rightarrow P\left(Z=z_{i} \mid \mathbf{h e}\right)=1$

Fuzzy evidence is a type of uncertain evidence, which refers to information that is incomplete or ambiguous. It is usually considered when hard evidence is insufficient. In a Fuzzy Bayesian network, fuzzy evidence allows quantifying the gradual membership of an observation to multiple states of the node being considered.

Definition 7 (Fuzzy evidence [19]) Given a FBN Fz, a fuzzy evidence on a node $Z$ for an observed value (val), is represented as a vector $U(Z)=\mu_{z_{1}}(\mathrm{val}): \mu_{z_{2}}(\mathrm{val}): \ldots$ : $\mu_{z_{m}}(\mathrm{val})$ of size $m$, where $\mu_{z_{i}}(\mathrm{val})$ is the membership degree of the observed value in the state $z_{i}$.

Lemma 1 [19] Given a fuzzy evidence e of a fuzzy node $Z$; each state's belief distribution $z_{k}$ is weighted according to its normalized degree of membership. It is formally computed as
$P\left(Z=z_{k} \mid e\right)=\lambda \cdot \mu_{z_{k}}(\mathrm{val}) \cdot P\left(Z=z_{k}\right)$,
where $k \in\{1,2, \ldots, L\}$ and $\lambda$ is a normalization constant.
$\lambda=1 / \sum_{j}^{L} P\left(Z=z_{j}\right) \cdot \mu_{z_{j}}(\mathrm{val})$

### 2.3 Fuzzy Ontology Web Language

A fuzzy ontology is a knowledge representation model that uses fuzzy logic to represent and reason about the concepts and relationships within a domain of knowledge. Fuzzy ontologies extend classical ontologies to model more complex and dynamic systems, where the boundaries between different concepts may be unclear or may change over time. In a fuzzy ontology, concepts, and relationships are represented as fuzzy sets, which allow for the representation of vagueness in the definition of a concept. We direct the reader to [3] for further information on the topic.

The Ontology Web Language (OWL2) is extended in order to enable fuzzy ontology representation. This extension is known as Fuzzy OWL 2 [21]. The semantics of fuzzy ontologies are encoded using OWL 2 annotation properties. A fuzzy ontology includes:

- Fuzzy concepts are classes that can have instances that partially belong to them. They appear in many realworld scenarios, where it is not possible or easy to give a precise definition of the concepts. Fuzzy concepts can be seen as a fuzzy set of individuals, where each individual is associated with a membership degree to the concept, usually measured in the interval $[0,1]$. For example, LowBloodPressure can represent the fuzzy set of low blood pressure and a person who has a blood pressure of 90/60 mm Hg has a LowBloodPressure with a degree of 0.8 . There can be atomic concepts and complex ones. For example, LowBloodPressure can be defined as a complex concept of the form Blood_pressure $\sqcap$ ЗhasBlood_pressure.lowBp, which denotes the intersection of two concepts: Blood_pressure and the class of people who has a low blood pressure.
- Fuzzy properties represent a partial relationship between two elements.
- On the one hand, fuzzy object properties are a way to express imprecise binary relationships between two individuals by assigning a degree of membership to the relationship. As an example, a fuzzy property called closeTo can be utilized to express imprecise statements like Region $A$ and Region $B$ are somewhat close (with a degree of 0.8).
- On the other hand, fuzzy data properties are utilized to determine the degree of association

between an entity and a data value, such as an integer number, or a string. For instance, hasBlood_pressure is a data property.

- Fuzzy datatypes are used to fuzzify the values of the data properties. For example, rather than stating that the blood pressure of a person $x$ is $90 / 60 \mathrm{~mm} \mathrm{Hg}$, we can associate $x$ with the fuzzy datatype lowBp. Fuzzy datatypes are typically represented using fuzzy sets of integer or real lines.
- Fuzzy modifiers: are employed to alter how fuzzy concepts and fuzzy datatypes are interpreted. A fuzzy modifier receives a membership degree as input and returns another degree, increased or weakened. For example, very fuzzy modifier is a weakening modifier.
- Fuzzy axioms are axioms that can partially hold. The concrete axiom types depend on the choice of the fuzzy ontology language. Classical ontologies typically include the following axioms:
- A concept assertion $I: C$ states that individual I belongs to concept C.
- A role assertion $\left(I_{1}, I_{2}\right): R$ states that $I_{1}$ and $I_{2}$ are related via object property $R$, whereas $(I, V): D$ states that $I$ has $V$ as the value of data property $D$.
- A concept subsumption axiom $C_{1} \sqsubseteq C_{2}$ states that $C_{1}$ is a subclass of (more specific than) $C_{2}$.
In fuzzy ontologies, fuzzy axioms make it possible to state that a fact (a concept or a role assertion) or the subsumption relationship between two concepts holds to a given degree. Given a classical axiom $\tau$, the fuzzy axiom $\left\langle\tau \geq \alpha\right.$ states that $\tau$ holds with a degree greater or equal than $\alpha \in(0,1]$.

Fuzzy ontologies can be used in several applications, including Decision support systems, Intelligent search engines, and Semantic web to enable computers to process information about a particular domain. They can also be combined with other types of ontologies, such as probabilistic ontologies, to provide a more complete representation of knowledge.

## 3 Related Work

In the last years, considerable attention has been paid to dealing with uncertainty in the most important technology trends such as Web services [22], e-healthcare [23], and the Internet of things (IoT) [24], Internet of Medical Things (IoMT) [25]. The combination of uncertainty with ontologies might be interesting in more domains [26].

This section examines some previous approaches similar to our work that extend the ontology web language OWL to
create so-called probabilistic ontologies using the semantics of Bayesian networks.

Authors in [27] proposed an extension of OWL called Bayes OWL. It offers a set of instructions for converting OWL ontologies to Bayesian networks and also suggests a technique for taking into account probability constraints found in the ontology while building the Bayesian network. In fact, it exploits available probabilistic data for creating the conditional probability table for every node in the BN. A limitation of this work is that the authors have focused only on the taxonomy of the concepts, and have ignored the non-taxonomic relations among the concepts.

In [28], researchers presented a new solution, called OntoBayes, which improves the knowledge representation in OWL and permits systems reason under uncertainty. Additional OWL classes have been established by the authors and can be used to annotate dependencies and probabilities in OWL. This extension allows representing the multi-valued random variable in OWL and a full joint probability distribution over them.

PR-OWL 2 [29, 30] was proposed as an extension of OWL ontologies to model and reason under uncertain knowledge in complicated real-world applications. It can encode probabilistic distributions on the interpretation of a related first-order model as well as recurring pattern based on the Multi-Entity Bayesian Network (MEBN) formalism [31]. Despite the robustness of PR-OWL 2 in terms of expressiveness, its use might be very tedious for non-expert users.

The method proposed in [32], allows constructing Bayesian networks based on existing domain ontologies. It consists of four steps, 1) Selection of relevant classes, individuals, and properties by the domain experts, 2) Creation of Bayesian network structure by the domain experts using step 1, 3) Construction of conditional probability tables which preserve semantic constraints of the ontology, and 4) Incorporation the factual information of the considered ontology. The main defect of this method is that the probabilistic knowledge was represented semantically in the ontology and the vague and imprecise knowledge are not considered.

In [33], authors have implemented a mobile agent platform, which uses both Ontology and Bayesian networks to predict if a given patient gets depressed or not. It uses an ontology model based on the terminology to describe depression and exploits a Bayesian network to infer the probability of becoming depressed or not.

A new approach called hybrid probabilistic ontology, which is built on hybrid Bayesian networks, is presented in the context of smart homes and can support semantics in machine-to-machine communication [34]. This approach has the advantage of enabling the ontology to handle distributions of both discrete and continuous quantities at the

Table 1 Comparison of the proposed approach and previous work


$\checkmark$ : criterion treated $\boldsymbol{X}$ : criterion not treated
same time. However, it is unable to reason with or cope with fuzzy ontological knowledge.

In [35], a technique for creating probabilistic ontologies has been created. This technique is built on traditional Bayesian networks to deal with probabilistic knowledge of classical ontologies. Only ontology instances and roles that entail uncertainty are converted using this technique into BN graphs. Unfortunately, this approach fails to handle vague knowledge while creating the CPTs and does not take into account missing data.

Lately, in [36] a new method is reported based on Bayesian networks. It aims to deal with incomplete knowledge in classical ontologies. Indeed, the proposed method allows the creation of a Bayesian network starting from a classical ontology with missing data with the intent to combine Bayesian inference with ontological inference.

Recent work is proposed to deal with fuzzy knowledge in probabilistic ontology encoded in PR-OWL 2 language in [37]. Authors have updated the ontology of PR-OWL 2 to allow representing fuzzy knowledge and to benefit from the capabilities of inference provided by Fuzzy MultiEntity Bayesian Networks [38].

Another relevant work is [39], where the logic $B E L$, a probabilistic extension of the $E L$ description logic based on classical Bayesian networks, is presented. Also, a Bayesian reasoner on ontologies based on BEL semantics is developed, which provides a way to represent and reason with the probabilistic subsumption of BEL.

Table 1 summarizes the previously discussed-related work, focusing on the modeling and reasoning services they offer.

- C1 indicates whether the solution deals with fuzzy knowledge in ontologies.
- C2 indicates whether the solution incorporates probabilistic knowledge within ontologies.
- C3 indicates whether or not the solution offers probabilistic reasoning.
- C4 indicates whether the solution provides probabilistic reasoning based on fuzzy evidence or not (Fuzzy Bayesian inference).
- C5 indicates whether the solution provides fuzzy reasoning with ontological knowledge, such as consistency, concept subsumption, concept satisfiability, etc.

The study of the related works made it possible to identify a set of limitations:

- The work reported by Riali et al. [37] is the closer work to the presented study. Indeed, both of them intend to deal with probabilistic knowledge and fuzzy knowledge simultaneously. Although the approach of Riali et al. is interesting, it does not allow for performing fuzzy reasoning with ontological knowledge. In contrast, this paper outlines a new approach considering all the criteria as mentioned above, notably fuzzy reasoning with ontological knowledge.
- Most methods have centered on using classical BNs to cope with the probabilistic knowledge in traditional ontologies. However, the fuzzy knowledge that may be associated with the nodes is not adequately handled by classical BNs.
- Most of the solutions are probabilistic extensions of OWL language. These solutions are restricted to handling only probabilistic knowledge; they do not take vague and imprecise knowledge into account.
- In a previous study [40], we proposed an approach to build a FBN from a fuzzy ontology. However, the mathematical formulation, the details of each construction step, and a real case study were not presented. In this paper, a new formulation, a detailed study with examples, a formal description of fuzzy probabilistic reasoning for ontological knowledge, and a case study in the domain of renal cancer with empirical validation are presented.


## 4 Probabilistic Fuzzy Ontology Web Language

This paper outlines a new solution to cope with uncertainty in ontologies, which consolidates fuzzy ontologies and fuzzy Bayesian networks to face rich uncertainty domains. It gives the possibility to manipulate uncertain and probabilistic knowledge simultaneously. Thus, it addresses the weaknesses of the existing-related work and it has the following outstanding features:

![img-1.jpeg](img-1.jpeg)

Fig. 2 The proposed process for modeling probabilistic knowledge on fuzzy ontologies
![img-2.jpeg](img-2.jpeg)

Fig. 3 a Trapezoidal function; $\mathbf{b}$ triangular function; $\mathbf{c}$ left-shoulder function; $\mathbf{d}$ right-shoulder function; and $\mathbf{e}$ linear function

- To the best of our knowledge, this is the first solution that takes into account probabilistic knowledge in fuzzy ontologies built on FBNs. It permits us to benefit from the advantages of FBN and fuzzy ontologies in terms of modeling and reasoning.
- It proposes a method for creating ProbFuzzOnto based on fuzzy ontologies encoded in Fuzzy OWL 2.
- All of the reasoning tasks that may be used with fuzzy ontologies are still available in our extension. Indeed, fuzzy ontologies are subsumed by our solution.
- It is a generic solution, which can be applied to deal with uncertainty in any domain of application, notably where probabilistic and fuzzy knowledge are involved together.
- The constraints and semantic knowledge that have been specified in the initial fuzzy ontology are also preserved.

The ProbFuzzOnto proposed in this paper is mainly based on extending fuzzy ontologies to cope with the probabilistic knowledge involved. This section introduces a process to guide the ontology engineer to create ProbFuz$z O n t o$ ontologies. Our method generates a ProbFuzzOnto ontology and a Fuzzy Bayesian network from an input fuzzy ontology, modeling the vague and probabilistic knowledge involved in the considered domain. It consists of four phases. The schematic view of our proposed process is shown in Fig. 2. In the following subsections, we present each phase.

### 4.1 Phase 1: Description of the Requirements

The goal of this phase is to clearly define the objective that must be accomplished through the construction of ProbFuzzOnto, thereby, justifying the need to develop the ProbFuzzOnto ontology for the studied problem and highlighting the main hypothesis and objectives. Based on this step, the ontology engineer could identify the probabilistic components that are relevant to the considered problem. Thus, the main objectives of this phase are:

- To describe the purpose to be achieved by creating a probabilistic fuzzy ontology for the domain in question.
- To pinpoint the scope of the probabilistic fuzzy ontology.
- To pinpoint the fuzzy ontology's probabilistic elements that are pertinent to the research problem.
- To identify the probabilistic relations between the probabilistic components of the fuzzy ontology.


### 4.2 Phase 2: Probabilistic Knowledge Design

The ultimate goal of this phase is to model the probabilistic knowledge encapsulated in the fuzzy ontology using a fuzzy Bayesian network which enables to answer to the requirements specified in the previous step. This is done by constructing a FBN, which encapsulates the domain's probabilistic knowledge. The construction is mainly based on exploiting as much as possible the components of the fuzzy ontology. Thus, the probabilistic knowledge design goes through three steps:

- Construct structure of fuzzy Bayesian networks (i.e., Structure learning).
- Estimate the CPTs (i.e., Parameters learning).
- Assign a membership function to each state belonging to a fuzzy node (i.e., States fuzzification).


## Structure learning

Our work deals with the probabilistic knowledge attached to the schema of a fuzzy ontology. In other terms, our approach permits us to cope with the uncertainty attached to the concepts and the roles of the fuzzy ontology (both the crisp and the fuzzy ones). The structure of the FBN depends on the requirements and it needs the intervention of both the ontology engineer and the domain knowledge expert.

In this study, we assume that not all the fuzzy components are probabilistic. For this reason, based on the requirements specified in phase 1 (Description of the requirements), the ontology engineer followed by the expertise of the domain knowledge expert has to identify the relevant concepts and roles that may involve probabilistic knowledge for the considered problem.

1. Nodes creation. Each pertinent concept will be represented as a node in the FBN.
2. States identification. The states of every generated node must be defined by the ontology engineer as well. For instance: Medium, Low, and High.
3. Arcs creation. An arc in the FBN will be created to represent each selected probabilistic role. However, the choice of the directions of the arcs is very important and influences the relationship dependency among the nodes and thus the correctness of the FBN semantics. In fact, this choice depends on several factors such as the studied problem. For this reason, the directions of the arcs are defined by the ontology engineer.

## Parameters learning

This step's goal is to estimate the Bayesian network's conditional probability tables (parameters, denoted $\Theta$ ). This task is usually done manually, guided by domain experts, which is very tedious and challenging, especially, in complex structures. The complexity of this task increases with the number of nodes, node states, and arcs in the FBN. For this reason, in this study, we employ machinelearning methods to infer the posterior distribution from the presented data.

Indeed, missing values and incomplete data are common in practice, and some random variables are never or only
partially observed (called latent variables). As a result, we use in this paper the most popular technique for estimating parameters from incomplete data. It is founded on the iterative EM (Expectation-Maximization) method developed by Dempster in [41].

The EM algorithm iteratively performs two steps: the Expectation (E) step and the Maximization (M) step. In the E-step, the algorithm uses the current estimates of the model parameters to compute the expected values of the complete data given the observed data. As for the M-step, the algorithm updates the estimates of the parameters by maximizing the expected likelihood of the complete data, based on the expected values computed in the E-step. This process is repeated until the estimates of the parameters no longer change significantly.

```
1 Initialize \(\Theta^{(0)}\) randomly at time \(t=0\)
2 repeat
3 Expectation: Use of the current parameters \(\Theta_{i, j, k}^{(t)}\) to estimate the
    expectation of the appearance of different configurations.
                            \(N_{i, j, k}^{*}=\sum_{i=1}^{n} P\left(X_{i}=x_{k}\right) P n\left(X_{i}\right)=x_{j}\)
4 Maximization: Estimate the new parameters by maximum likelihood
    using the expectation of the statistics obtained in the previous step.
                            \(\Theta_{i, j, k}^{(t+1)}=\frac{N_{i, j, k}^{*}}{\sum_{k} N_{i, j, k}^{*}}\)
4 until \(\Theta_{i, j, k}^{(t+1)}-\Theta_{i, j, k}^{(t)}<\xi\)
```

Algorithm 1 EM algorithm.

## States fuzzification

The aim of the final step of the probabilistic design phase is to assign to each state of each fuzzy node a fuzzy membership function. In order to exploit as much as possible the fuzzy representation in the Fuzzy OWL 2 ontology, we use the membership functions that are already defined in the fuzzy ontology (as fuzzy datatypes) to fuzzify the states of the FBN. Fuzzy membership functions proposed in [21] to define fuzzy datatypes are depicted in Fig 3. Example 1 shows how to represent a triangular fuzzy datatype in Fuzzy OWL 2.

Example 1 A fuzzy datatype with a triangular membership function can be represented in Fuzzy OWL 2 as follows:

In this fuzzy datatype, triangular represents the type of the membership function, and $\mathrm{a}, \mathrm{b}$, and c are its parameters.

Listing 1 Example of a fuzzy membership function in Fuzzy OWL2

```
<fuzzyOwl2 fuzzyType=datatype>
    <Datatype type="triangular" a="18" b="23" c="25" />
</fuzzyOwl2}>
```

![img-3.jpeg](img-3.jpeg)

Fig. 4 The upper ontology UOFBN

### 4.3 Phase 3: Integration of Probabilistic Knowledge

In the previous steps, the probabilistic knowledge of the fuzzy ontology was represented as a fuzzy Bayesian network model. However, this knowledge should be represented in a formal way, processable by machines. For this reason, we propose a formal Upper Ontology of FBN (UOFBN) to describe the concepts of fuzzy Bayesian networks and the relationships between them. This can be used to create a knowledge graph of FBN and its associated semantics, and then incorporate it into the fuzzy ontology.

The semantics of FBN can be represented using $U O F B N$, as shown in Fig. 4. It has the following classes and properties:

State class. The states associated with each node $n_{i}$ are represented as objects of this class. An individual $I_{s}$ will be created to represent each state $s_{i} \in S$. Additionally, via the object property hasState, $I_{s}$ is linked to the node $n_{i}$.

We define an object property called Attached, which links each state of a fuzzy node to its corresponding membership function, previously defined in a fuzzy datatype (refer to Example 2).

## Example 2

We will use the classes CondTab and PriorTab to represent the probability table of each node.

PriorTab. To represent the probability table of each root node, an individual of this class will be generated.

```
<owl:DatatypeProperty rdf:about="Attached">
    <rdfs:domain rdf:resource="State"/>
    <rdfs:range rdf:resource="@rdfs;Literal"/>
</owl:DatatypeProperty>
```

Node class. Individuals belonging to the class Node will represent the FBN's nodes. Indeed, the nodes in a FBN might be either crisp or fuzzy; to distinguish between the two types, we defined two subclasses of the class Node.

- The FuzzyNode class; individuals of this class aim at representing semantically each fuzzy node $f n_{i} \in \Phi$.
- The CrispNode class; individuals of this class aim at representing semantically each crisp node $c n_{j} \in \Psi$.

In addition, we created an object property hasParent, which represents the arcs between nodes.

Moreover, a set of prior probabilities $\mathrm{P}=$ $\left\{\right.$ Prior $\left._{1}, \ldots, \text { Prior }_{n}\right\}$ will be generated as individuals of the class PriorProb. The object property hasPriorTab will link these individuals with their respective tables.

Example 3 Let $P(n=s)=0.4$ be the prior probability of the event $\mathrm{n}==$ occurring. To represent this prior probability, we created a new individual Prior1 of the class PriorProb. It is represented in OWL as follows:

CondTab. To represent the probability table of each node with parents, an individual of this class will be created. Additionally, a collection of conditional probabilities

Listing 3 The semantic representation of the prior probability

```
<NamedIndividual rdf:about="Prior1">
    <rdf:type rdf:resource="PriorProb"/>
    <priorProbValue rdf:datatype="Θzsd:decimal">0.4</priorProbValue>
    <priorState rdf:datatype="Θzsd;string">s</priorState>
</NamedIndividual>
```

$\mathrm{C}=\left\{\operatorname{Cond}_{i}, \ldots, \operatorname{Cond}_{n}\right\}$ will be generated as individuals of the class CondProb. The object property hasCondTab will link these instances with their respective conditional tables.

Example 4 Consider the below conditional probability of a node $n$ in the state $s$ with its parents $n_{1}, n_{2}, n_{3}$ and $n_{4}$ :
$P\left(n=s \mid n_{1}=s_{1}, n_{2}=s_{2}, n_{3}=s_{3}, n_{4}=s_{4}\right)=0.8$
To represent this conditional probability, we created a new individual Cond1 of the class CondProb. It is represented in OWL as follows:

Additionally, in order to make a relation among the uncertainty modeled using the ontology UOFBN and the probabilistic elements of the fuzzy ontology, we created a

- Empirical Study: The ontology can be evaluated using real-world situations or data to evaluate its accuracy and effectiveness. It is worth noting that in our case study, we will use this strategy to validate our modeling.


## 5 Probabilistic Reasoning in Fuzzy Ontologies

This section describes how to reason with our probabilistic fuzzy ontology. Since our proposal extends the fuzzy ontology, if we ignore the probabilistic part, all reasoning tasks that can be applied to fuzzy ontologies using some

Listing 4 The semantic representation of the conditional probability

```
<NamedIndividual rdf:about="Cond1">
    <rdf:type rdf:resource="CondProb"/>
    <condState>s</condState>
    <EvidenceNodesList>n1,n2,n3,n4</EvidenceNodesList>
    <EvidenceStateList>s1,s2,s3,s4</EvidenceStateList>
    <condProbValue>0.8</condProbValue>
</NamedIndividual>
```

data property that we named defineProbKnowAbout. It maps the individuals of the class Node (nodes of the FBN) with their corresponding elements in the fuzzy ontology. This allows more compatibility among the upper ontology which models probabilistic knowledge and fuzzy ontology. The representation of the data property defineProbKnowAbout in OWL is given as follows:

### 4.4 Phase 4: Quality Validation

The quality of the probabilistic fuzzy ontology modeling can be validated through various strategies, such as:

- By a domain expert: An expert in the ontology domain can validate the modeling and review its accuracy, completeness, and consistency.
reasoner such as DeLorean (DEscription LOgic REasoner with vAgueNess) [42] or fuzzyDL [43, 44], are still applicable to ProbFuzzOnto. For instance: ontology consistency, concept subsumption, concept satisfiability, best satisfiability degree...

Moreover, our proposal uses the tools offered by the FBNs to provide mechanisms for representing probabilistic knowledge and deduce implicit knowledge from explicit knowledge stored in a fuzzy ontology.

According to Poole et al. [45], we should consider three types of uncertainty: the probability of existence, the probability distribution over the types of an individual, and the probability of property values. To do so, we proceed as follows:

[^0]
[^0]:    Listing 5 The representation of the data property defineProbKnowAbout in OWL
    <owl:DatatypeProperty rdf:about="defineProbKnowAbout">
    <rdfs:domain rdf:resource="Node"/>
    <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema\#anyURI"/>
    </owl:DatatypeProperty>

- Existence uncertainty: this task consists of quantifying the uncertainty about the real existence of an individual in the ontology. Indeed, this task is a question of verifying if an individual corresponds to a description that really exists.
According to [46], the reasoning on the existence of an individual consists in verifying the veracity of the property Exists (individual) for the individual request. If its value is true the individual really exists, otherwise it does not exist. This task can be formulated as follows:
Input: A fuzzy ontology $O$, An individual I
Task: Check whether the property Exists (I) is satisfied or not in the ontology $O$
Output: A Boolean value.
- Type uncertainty: determines the likelihood of a particular individual belonging to a particular class based on its properties and properties of others in the fuzzy ontology $O$. This task can be formulated as shown in Algorithm 2.

```
Input: Fuzzy Ontology \(O\), Concept C; Individual I.
Output: Probability \(p \in[0,1]\) that \(P((I: C>0))=\) true.
\(f^{*}:=\) Step 1: Evidence preparation */
\(\mathbf{e}=\emptyset\)
for each data property assertion of the form \((I, V): D\) in \(O\) do
    Retrieve the set of fuzzy datatypes \(F\) such that \(D\) belongs to \(F\) with a
        non-zero degree.
        if \(F\) is empty then
            Add a hard evidence:
            \(\mathbf{e}=\mathbf{e} \bigcup\left\{z_{0}=0, z_{1}=0, z_{2}=0, \ldots, z_{i}=1, \ldots, z_{|N|}=0\right\}\)
        else
            for each \(F_{i} \in F\) do
                Add a fuzzy evidence: \(\mathbf{e}=\mathbf{e} \bigcup=\mu_{z_{i}}(V): \mu_{z_{i}}(V): \ldots: \mu_{z_{i n}}(V)\).
for each object property assertion of the form \(\left(I_{1}, I_{2}\right): R\) in \(O\) do
    Add a hard evidence: \(\mathbf{e}=\mathbf{e} \bigcup=\left\{z_{R\left(I_{1}, I_{2}\right)}=1, z_{\text {Other }}=0\right\}\).
\(f^{*}:=\) Step 2. Formulate the query */
\(Q=P((I: C>0)=\) true \(\mid \mathbf{e})\)
\(f^{*}:=\) Step 3. Apply fuzzy Bayesian inference reasoning */
\(P\) : Preface fuzzy Bayesian inference using the evidence \(\mathbf{e}\)
\(p=\) Compute the probability using fuzzy Bayesian inference that \(Q\) holds
return \(p\).
```

Algorithm 2 Computing probability of an individual belonging to a concept in a fuzzy ontology.

Example 5 Suppose we have a fuzzy ontology representing professions and individuals' skills. We want to determine the probability that an individual, John, belongs to the concept DataScientist.

## - Input:

- Fuzzy Ontology O representing professions and skills.
- Concept C: DataScientist.
- Individual I: John.


## - Step 1: Evidence preparation.

- From John's skills scores, represented as data property assertions in O , and their membership degrees to the fuzzy datatypes in O , we can obtain Fuzzy Evidences:
- Data Analysis score is 70. The membership degrees to the fuzzy datatypes are the following ones: 0.7 to "High", 0.28 to "Medium", and 0.12 to "Low". Thus, the fuzzy evidence vector is represented as follows:

$$
\begin{aligned}
\mathbf{U}(\text { DataAnalysis })= & \mu_{\text {High }}(0.7): \mu_{\text {Medium }}(0.28): \\
& \mu_{\text {Low }}(0.12)
\end{aligned}
$$

- Machine Learning score is 80 . Now the membership degrees are 0.8 ("High"), 0.12 ("Medium"), and 0.08 ("Low"), so the fuzzy evidence vector is represented as follows:

$$
\begin{aligned}
\mathbf{U}(\text { MachineLearning })= & \mu_{\text {High }}(0.8): \mu_{\text {Medium }}(0.12): \\
& \mu_{\text {Low }}(0.08)
\end{aligned}
$$

* Additional hard evidence: John has a Bachelor's degree in Computer Science, represented as an object property assertion in O . The hard evidence vector could be represented as follows:

$$
\mathbf{h e}=\left(z_{\text {Bachelor'sinComputerScience }}=1, z_{\text {Other }}=0\right)
$$

- Step 2: Formulate the query. If $\mathbf{e}$ denotes the union of all previous evidences, the query is:
$Q=P(\langle$ John $:$ DataScientist $\rangle 0\rangle=$ true $\mid \mathbf{e}\rangle$
- Step 3: Apply fuzzy Bayesian inference reasoning. We apply fuzzy Bayesian inference to assess the likelihood of John belonging to the "Data Scientist" concept. The inference considers John's skills as a fuzzy evidence and his hard evidence of a Computer Science degree. After performing fuzzy Bayesian inference, we obtain a probability value, denoted as $p$. In this case, let's assume that the computed probability is $p=0.85$.
- Result. The algorithm returns the probability $\mathbf{0 . 8 5}$.
- Property values uncertainty: determine the likelihood of a particular individual possessing a certain property value based on its properties and properties of other individuals. We can distinguish two types of property values uncertainty, the first one is about data properties, while the second one is about object properties.

- Data property values uncertainty: this task aims to compute the likelihood that an individual $I$ possessing a data property $D$ with a given value $V$ in the fuzzy ontology $O$. It can be formulated as shown in Algorithm 3.

```
Input: Fuzzy Ontology \(O\), Data Property \(D\), Individual \(I\), Value \(V\).
Output: Probability \(p \in[0,1]\) that \(P(\langle D(I, V\rangle>0))=\) true.
\(f^{*} \triangleright\) Step 1: Evidence preparation */
\(\mathbf{e}=\emptyset\)
for each data property assertion of the form \((I, V): D\) in \(O\) do
    Retrieve the set of fuzzy datatypes \(F\) such that \(D\) belongs to \(F\) with a
        non-zero degree.
    if \(F\) is empty then
        Add a hard evidence:
        \(\mathbf{e}=\mathbf{e} \bigcup\left\{z_{0}=0, z_{1}=0, z_{2}=0, \ldots, z_{i}=1, \ldots, z_{|E|}=0\right\}\)
    else
        for each \(F_{i} \in F\) do
            Add a fuzzy evidence: \(\mathbf{e}=\mathbf{e} \bigcup=\mu_{z_{1}}(V): \mu_{z_{2}}(V): \ldots: \mu_{z_{m}}(V)\).
    \(f^{*} \triangleright\) Step 2. Formulate the query */
    \(Q=P(\langle D(I, V\rangle>0))=\) true \(\mid \mathbf{e}\)
    \(f^{*} \triangleright\) Step 3. Apply fuzzy Bayesian inference reasoning */
    Perform fuzzy Bayesian inference using the evidence \(\mathbf{e}\)
    \(p=\) Compute the probability using fuzzy Bayesian inference that \(Q\) holds
    return \(p\).
```

Algorithm 3 Computing probability of an individual having a data property with a given value in a fuzzy ontology.

Example 6 Following Example 5, assume that we want to determine the probability that John possesses the "Data Analysis" skill with a High score.

Input:

* Fuzzy Ontology O representing professions and skills.
* Data Property D: DataAnalysis.
* Individual I: John.
* Value V: High.

Step 1: Evidence preparation: it is the same as in Example 5.

Step 2: Formulate the query:
We want to calculate the probability that John possesses the "Data Analysis" skill with a High score, so our query is:
$Q=P(\langle$ DataAnalysis $\langle$ John, High $\rangle>0\rangle)=$ true $\mid \mathbf{e}\rangle$
Step 3: Apply fuzzy Bayesian inference reasoning:
We apply fuzzy Bayesian inference to assess the likelihood of John possessing the "Data Analysis" skill with a High score. This inference considers John's skills as a fuzzy evidence and his hard evidence of a Computer Science degree. After performing fuzzy Bayesian inference, we obtain a probability value, denoted as $p$. Let's assume that the computed probability is $p=0.85$.

Result: 0.85 would be the output of the algorithm.

- Object property values uncertainty: this task aims to compute the probability that two individuals $I_{1}$ and $I_{2}$
are linked via an object property $R$ with a given value $V$ in the fuzzy ontology $O$. It can be formulated as shown in Algorithm 4.

```
Input: Fuzzy Ontology \(O\), Object Property \(R\), Individuals \(I_{1}\) and \(I_{2}\), Given
    Value \(V\).
Output: Probability \(p \in[0,1]\) that \(P\left(\left\langle\left[R\left(I_{1}, I_{2}\right)>0\right)\right\rangle=\right.\) true .
\(f^{*} \triangleright\) Step 1: Evidence preparation */
\(\mathbf{e}=\emptyset\)
    \(D P=\left\{\left(I_{1}, V_{1}\right): D_{1} \in O\right\} \cup\left\{\left(I_{2}, V_{2}\right): D_{2} \in O\right\}\)
    for each data property assertion of the form \((I, V): D\) in \(D P\) do
        Retrieve the set of fuzzy datatypes \(F\) such that \(D\) belongs to \(F\) with a
            non-zero degree.
        if \(F\) is empty then
            Add a hard evidence:
            \(\mathbf{e}=\mathbf{e} \bigcup\left\{z_{0}=0, z_{1}=0, z_{2}=0, \ldots, z_{i}=1, \ldots, z_{|E|}=0\right\}\)
        else
            for each \(F_{i} \in F\) do
            Add a fuzzy evidence: \(\mathbf{e}=\mathbf{e} \bigcup=\mu_{z_{1}}(V): \mu_{z_{2}}(V): \ldots: \mu_{z_{m}}(V)\).
    for each object property assertion of the form \(\left(I_{1}, I_{2}\right): R\) in \(O\) do
        Add a hard evidence: \(\mathbf{e}=\mathbf{e} \bigcup=\left\langle z_{R\left(I_{1}, I_{2}\right)}=1, z_{\text {Other }}=0\right\rangle\).
    \(f^{*} \triangleright\) Step 2. Formulate the query */
    \(Q=P\left(\left\langle R\left(I_{1}, I_{2}\right)>0\right)\right\rangle=\) true \(\mid \mathbf{e}\rangle\)
    \(f^{*} \triangleright\) Step 3. Apply fuzzy Bayesian inference reasoning */
    Perform fuzzy Bayesian inference using the evidence \(\mathbf{e}\)
    \(p=\) Compute the probability using fuzzy Bayesian inference that \(Q\) holds
    return \(p\).
```

Algorithm 4 Probability of two individuals being linked via an object property in a fuzzy ontology.

## 6 Case Study: Building a ProbFuzzOnto for Renal Cancer Disease

As shown in Table 1, none of the previous approaches integrates both fuzzy ontologies and Bayesian networks. Indeed, our proposed approach can model several types of uncertainty at the same time, which are:

- Randomness (Stochastic): Random uncertainty refers to events or phenomena whose outcomes are inherently unpredictable. These uncertainties are typically described using probability distributions, where each possible outcome has an associated probability. In our system, this type is captured by the FBN.
Example related to our case of study: The response of a patient's kidney function to a particular treatment may vary unpredictably due to individual physiological differences or environmental factors.
- Fuzzy knowledge: Fuzzy knowledge, also known as linguistic uncertainty, appears in situations where the boundaries between categories or concepts are not sharply defined. Instead of clear distinctions, elements may partially belong to multiple categories simultaneously.
Example related to our case of study: Classifying the severity of RenalCancer (Kidney damage ) based on

Table 2 Details of the CKD data set


laboratory test results may involve fuzzy boundaries between categories such as "moderate", and "severe", as these classifications can depend on subjective interpretations of test values. This kind of knowledge is captured by the fuzzy ontology.

- Incompleteness: Incompleteness uncertainty occurs when the available information is insufficient to determine the state or outcome of a situation accurately. This can arise due to missing data, incomplete knowledge, or limitations in characterizing a system or phenomenon fully.
Example related to our case of study: Predicting the progression of chronic kidney disease in a patient may be challenging due to incomplete medical histories or limited access to longitudinal data tracking disease progression over time. In our system, this type can be treated by the FBN. It can answer queries even with incomplete data (when some variables are not observed in a data row).

The large ubiquity of inherent uncertainty associated with the medical field has led us to choose this field to present a case study on Renal Cancer (RC), which demonstrates the performances of our proposed solution. Indeed, we
constructed a ProbFuzzOnto for RC that we named ProbFuzzOnto-RC.

In this section, we first detail the original dataset (Sect. 6.1). Then, we build a fuzzy ontology (Sect. 6.2) and then a probabilistic fuzzy ontology (Sect. 6.3).

### 6.1 Data Set Description

RC affected 753 million people worldwide in 2016, including 417 million women and 336 million men [47]. In 2015, it resulted in 1.2 million deaths, compared to 409,000 in 1990 [48]. In fact, RC is a consequence of a group of disorders affecting the kidney cells that lead to the reduction or impossibility of the kidney to filter and dispose of blood waste. It is also the reduction of the capacity of the kidneys to control the balance of the body in water and mineral salts. In our study, we use the chronic kidney disease (CKD) dataset, ${ }^{1}$ collected from a hospital during nearly 2 months. The data set contains 400 samples, each sample has 24 predictive features ( 11 numerical features and 13 categorical features) and a categorical target variable (class) as presented in Table 2.

[^0]
[^0]:    ${ }^{1}$ http://archive.ics.uci.edu/ml/datasets/chronic_kidney_disease

![img-4.jpeg](img-4.jpeg)

Fig. 5 Renal cancer crisp ontology model

### 6.2 Fuzzy Ontology Construction

The main goal of this step is to create a fuzzy ontology that we named FuzzOnto-RC, which can represent data about patients, their risk factors, their symptoms, and their tests. We used the method suggested in [21] to create the fuzzy ontology, which comprises two steps:

In the first step, we have created a classical ontology using the free ontology editor Protégé. ${ }^{2}$ It includes four classes, which are:

- The individuals of the class Patient are the patients we seek to diagnose.
- The class Risk_Factor includes a set of subclasses, namely: age, hypertension (htn), the diabetes mellitus (dm), coronary artery disease (cad), and appetite (appt).
- The class Symptoms encompasses the following subclasses: the pedal edema (pe), the pus cell clumps (pcc), the blood urea (bu), and the anemia (ane).
- The class Test includes a set of subclasses, which are: blood pressure (bp), the specific gravity (sg), the albumin (alb), the sugar(su), the red blood cells (rbc), the pus cell (pc), the bacteria (ba), the blood glucose random (bgr), the serum creatinine (sc), the sodium(sod), the potassium (pot), the hemoglobin (hemo), the

[^0]packed cell volume ( $p c v$ ), the white blood cell count (wbcc), and the red blood cell count (rbcc).
The core ontology is illustrated in Fig. 5.
The fuzzy side of the ontology has been modeled using the Fuzzy OWL 2 plugin ${ }^{3}$ based on new annotations. Indeed, for each fuzzy data property, several fuzzy datatypes were annotated which are the possible values of the property in order to represent the vague knowledge using trapezoidal membership functions with the arguments listed in Table 3.

For example, the fuzzy class Blood_pressure can be represented by a set of subclasses, including LowBloodPressure, NormalBloodPressure and HighBloodPressure (illustrated in Fig. 6). These classes are defined in Description Logic (DL) as follows:

## LowBloodPressure $\equiv$ Blood_pressure $\square$ <br> $\exists$ hasBlood_pressure.lowBp

referring to a set of instances of Blood_pressure with values of the lowBp datatype,

## NormalBloodPressure $\equiv$ Blood_pressure $\square$ <br> $\exists$ hasBlood_pressure.normalBp

referring to a set of instances of Blood_pressure with values of the normalBp datatype, and

[^1]
[^0]:    ${ }^{2}$ http://protege.stanford.edu

[^1]:    ${ }^{3}$ https://protegewiki.stanford.edu/wiki/FuzzyOWL2

Table 3 Membership functions


HighBloodPressure $\equiv$ Blood_pressure $\square$
$\exists$ hasBlood_pressure.highBp
referring to a set of instances of Blood_pressure with values of the highBp datatype.

It is worth noting that Datil tool makes it possible to learn fuzzy datatypes from the numerical values of the data properties [49].

### 6.3 Probabilistic Fuzzy Ontology Construction

This section outlines the procedural steps involved in creating ProbFuzzOnto-RC.

### 6.3.1 Phase 1: Description of the Requirements

ProbFuzzOnto-RC was developed in response to a necessity for representation of the patients and their data as well as representing the probabilistic relationships among the appearance of RC in the patients with risk factors, symptoms, and tests. Thus, the main objective of ProbFuzzOnto-RC is to determine a patient's RC status using a list of evidence.

### 6.3.2 Phase 2: Probabilistic Knowledge Design

The goal of this phase is to use FBNs to model probabilistic knowledge of fuzzy Ontology. Indeed, this section outlines the three modeling steps.

## Structure learning

The fuzzy ontology's elements will be used for building the FBN's structure. Hence, Figure 7 provides the FBN's structure.

## Parameters learning

The conditional probability table of each node must be computed when the Bayesian network's structure is defined. In our study, the EM method is used to calculate the conditional probability tables for each node. The Bayesian network and its parameters are shown in Fig 8.

## States fuzzification

The states of each fuzzy node are fuzzified where a membership function (represented in a fuzzy datatype) is assigned to each one of them. For instance, Listing 6 shows the semantic fuzzification of the state Normalbp of the node $b p$ using the data property Attached. It links the state NormalBp with the fuzzy datatype normalBp.

Listing 6 Fuzzification of the state Normalbp of the node bp.

```
<DataPropertyAssertion>
    <DataProperty IRI="Attached"/>
    <NamedIndividual IRI="Normalbp"/>
    <Literal datatypeIRI="\&rdfs;Literal">normalBP</Literal>
</DataPropertyAssertion>
```

![img-5.jpeg](img-5.jpeg)

Fig. 6 The annotations properties of the classes LowBloodPressure, NormalBloodPressure, and HighBloodPressure

### 6.3.3 Phase 3: Integration of Probabilistic Knowledge

In this step, the uncertainty modeled by the creation of a FBN will be represented and described in the ontology $U O F B N$ and thereby merged and incorporated in the fuzzy ontology. The first step aims to represent the semantics of FBN in the ontology $U O F B N$; this is done by representing the elements of the FBN as instances and representing the relations among them by object properties assertions in the ontology $U O F B N$. After that, integrates the ontology $U O F B N$ in the fuzzy ontology. The resulting ontology probabilistic fuzzy ontology is illustrated in Fig. 9, which models the probabilistic knowledge of the fuzzy ontology.

Moreover, in this step the correspondences among the instances of the class Node of the ontology $U O F B N$ and the concepts of the fuzzy ontology are made using the data property defineProbKnowAbout. For example, the data property assertion illustrated in Listing 7 allows linking the node $b p$ with the class Blood_pressure.

We employ the k-fold cross-validation method in our experimentation. It is a well-known method for evaluating the performance of a machine-learning model. k-fold crossvalidation involves splitting the dataset into k subsets or folds of approximately equal size. The model is trained on $\mathrm{k}-1$ folds and evaluated on the remaining fold. This process is repeated k times, with each fold serving as the test set once.

We have carried out a series of tests, for each iteration we apply the fuzzy Bayesian inference and the classical Bayesian inference based on the information of each patient stored in the k part of the dataset. Subsequently, we compare the correspondence achieved by the fuzzy Bayesian inference and those by a manual classification and compare the correspondence obtained by the classical Bayesian inference and those by a manual classification (with the domain expert). After that, we compute the accuracy to assess the quality of the resulting classification of each type of inference.

```
Listing 7 Linking the node bp with the class Blood_pressure.
<DataPropertyAssertion>
    <DataProperty IRI="defineProbKnowAbout"/>
    <NamedIndividual IRI="bp"/>
    <Literal datatypeIRI="\&xsd;anyURI">Blood_pressure</Literal>
</DataPropertyAssertion>
```


### 6.4 Phase 4: Quality Validation

The fuzzy Bayesian inference engine of the probabilistic fuzzy ontology is quantitatively evaluated in this section. A prototype is implemented in Java, using GeNIe and SMILE. ${ }^{4}$ SMILE is written in $\mathrm{C}++$ as a software library for performing Bayesian inference. As for GeNIe, it is a graphical interface that facilitates using all provided functionalities of SMILE.

[^0]The obtained results are depicted in Fig. 10. The results demonstrate that the fuzzy Bayesian inference produces the outcomes compared to the classical approach for each value of K , this indicates that the prediction generated by the fuzzy Bayesian inference closely aligns with the prediction provided by the domain expert.

Table 4 shows a comparison with some recent works on the prediction of chronic kidney disease that use the same dataset as us. Our approach outperforms all of them in terms of accuracy except one. While the accuracy of our system is slightly worse than the accuracy in Islam et al. [53] ( 0.98 vs. 0.977 ), our approach offers a more comprehensive solution for modeling uncertain data using a semantic model.

These results highlight the effectiveness of our approach, which integrates ProbFuzzOnto ontology and


[^0]:    ${ }^{4}$ http://www.bayesfusion.com

![img-6.jpeg](img-6.jpeg)

Fig. 7 Structure of the fuzzy Bayesian network
![img-7.jpeg](img-7.jpeg)

Fig. 8 The fuzzy Bayesian network and its parameters

![img-8.jpeg](img-8.jpeg)

Fig. 9 Integration of the probabilistic knowledge

FBNs to capture complex relationships and uncertainties inherent in the data. Furthermore, our approach achieves this high accuracy while providing a holistic semantic
representation of the domain, enabling more informed decision-making in clinical settings. Thus, despite the slight difference in accuracy, the broader capabilities and advantages of our approach position it as a promising solution for predicting chronic kidney disease.

## 7 Conclusion

This article presents a novel solution that aims to address the need for a suitable representation and reasoning with ontological knowledge in domains with imprecision and uncertainty. Our proposal is the first solution merging fuzzy Bayesian networks with fuzzy ontologies to benefit from the strength of the two formalisms. In fact, a probabilistic extension of fuzzy ontologies called ProbFuzzOnto is developed in this paper that aims to enhance the expressivity and capability of reasoning of existing fuzzy ontologies to support probabilistic knowledge. On the one hand, it allows representing and incorporating formally the probabilistic knowledge in fuzzy ontologies in a way that it can be read and processed by machines. On the other hand, it combines the Fuzzy Bayesian network inference (updating probabilities over fuzzy evidence) and fuzzy reasoning with ontological knowledge (realization, concept satisfiability, etc.).

Moreover, the proposed solution is described by a general process that guides ontology engineers to build ProbFuzzOnto. Then, the fuzzy Bayesian inference process to reason with probabilistic knowledge over fuzzy evidence is presented. Besides, a case study on renal cancer was conducted to evaluate and demonstrate the effectiveness of the proposed solution in terms of expressivity and the power of reasoning. Indeed, the probabilistic knowledge is modeled and incorporated in the fuzzy ontology to raise its expressivity. Moreover, the experimental results have shown that the fuzzy Bayesian inference outperforms clearly the classical Bayesian inference. Our dataset is the first one combining fuzzy ontologies and probabilistic knowledge.

Our future plans include the development of an interactive Protégé-plugin that eases the creation of probabilistic fuzzy ontologies based on our proposed method. We would also like to evaluate our approach empirically in more real use cases. Moreover, it will be interesting to go further and improve our proposed solution using type-2

![img-9.jpeg](img-9.jpeg)

Fig. 10 Results of the inference

Table 4 Comparison of accuracy and techniques used


fuzzy ontologies [54] which are extensions of fuzzy ontologies where there is uncertainty regarding the definition of the membership functions.

Acknowledgements F. Bobillo was supported by the I+D+i project PID2020-113903RB-I00, funded by MCIN/AEI/10.13039/ 501100011033, and by project T42_23R (funded by Gobierno de Aragón). The authors are grateful to Azzedine Maandouche and Cherkelaine Ali for their technical help.

Funding Open Access funding provided thanks to the CRUE-CSIC agreement with Springer Nature.

Data availability The data that support the findings of this study are available in the UCI Machine Learning Repository (Chronic Kidney Disease)

## Declarations

Conflict of interest The authors affirm that there are no Conflict of interest to disclose. All co-authors have reviewed and endorsed the manuscript's contents, and no financial interests are to be reported.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons. org/licenses/by/4.0/.
