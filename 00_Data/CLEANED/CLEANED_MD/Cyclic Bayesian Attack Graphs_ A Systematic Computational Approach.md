# Cyclic Bayesian Attack Graphs: A Systematic Computational Approach 

Isaac Matthews<br>Newcastle University<br>Newcastle upon Tyne, U.K.<br>I.J.Matthews2@ncl.ac.uk

John Mace<br>Newcastle University<br>Newcastle upon Tyne, U.K.

Sadegh Soudjani<br>Newcastle University<br>Newcastle upon Tyne, U.K.

Aad van Moorsel<br>Newcastle University<br>Newcastle upon Tyne, U.K.

Abstract-Attack graphs are commonly used to analyse the security of medium-sized to large networks. Based on a scan of the network and likelihood information of vulnerabilities, attack graphs can be transformed into Bayesian Attack Graphs (BAGs). These BAGs are used to evaluate how security controls affect a network and how changes in topology affect security. A challenge with these automatically generated BAGs is that cycles arise naturally, which make it impossible to use Bayesian network theory to calculate state probabilities. In this paper we provide a systematic approach to analyse and perform computations over cyclic Bayesian attack graphs. Our approach first formally introduces two commonly used versions of Bayesian attack graphs and compares their expressiveness. We then present an interpretation of Bayesian attack graphs based on combinational logic circuits, which facilitates an intuitively attractive systematic treatment of cycles. We prove properties of the associated logic circuit and present an algorithm that computes state probabilities without altering the attack graphs (e.g., remove an arc to remove a cycle). Moreover, our algorithm deals seamlessly with all cycles without the need to identify their types. A set of experiments using synthetically created networks demonstrates the scalability of the algorithm on computer networks with hundreds of machines, each with multiple vulnerabilities.

Index Terms-vulnerabilities, attack graphs, Bayesian networks, security risk assessment, probabilistic graphical models

## I. INTRODUCTION

An attack graph is a representation of a system and its vulnerabilities in the form of a directed acyclic graph. It models how a system's vulnerabilities can be leveraged during a single attack to progress through a network. In recent years, several authors have pursued to combine Bayesian statistics with attack graphs to automatically prioritise network vulnerabilities from a probabilistic view point, resulting in Bayesian Attack Graphs [1]-[8]. The literature discusses a variety of considerations when generating BAGs [9], [10], including using the Common Vulnerability Scoring System (CVSS) to associate probabilities with vulnerabilities [11]. This approach has received uptake in practical security analysis systems, in particular in MulVAL [12], which automatically generate BAGs from network scans and CVSS information.

Once a BAG has been generated it can be analysed in various ways. One approach is an exclusively static analysis, in order to identify the weakest areas of a network as well as identify quantitatively the risk that a certain asset will be compromised in the case of an attack. Further extensions to
this kind of analysis include the introduction of attack profiles to modify the probabilities; for example this could be done using the attack complexity metric in the CVSS base vector to determine the ease of an attack. One approach to this is detailed by Cheng et al. [13] along with a method to include dependency relationships between vulnerabilities. Another application of the BAG is as a dynamic risk assessment tool where an administrator can model new security controls and their effects on a network, as well as dynamically analyse a deployed network's most likely attack paths, that can be updated dependent on information from an intrusion detection system [14].

The majority of the techniques used to calculate probabilities for BAGs require that they do not contain 'cycles' but are allowed to have 'loops' [9], [11], [15]. Such acyclic BAGs follow the monotonicity principle, that an attacker will never return to a previous state. However, networks that arise in practice when using tools such as MulVAL routinely contain cycles. These cycles arise naturally, as we will illustrate in Section II-A for a canonical example.

To deal with cycles in BAGs, the existing literature suggest to remove edges from the graph to prevent the attacker backtracking [7], [11], [16]. There are a number of practical drawbacks to this approach, especially when carried out outside the analysis algorithm, thus altering the model. For instance, removing an edge can make reasoning about the graph for a cyber security professional confusing, if the graph is examined by hand to identify specific routes and there are edges missing for the calculations. In addition, avoiding cycles that occur when generating the BAG could be impractical and take a "substantial amount of time" [17] to ensure an edge is not cycle-causing whenever a new edge is being added to the graph.

In this paper we propose a systematic computational approach for analysing cyclic BAGs, combining formalising models (attack graphs, BAGs and variants) and their properties throughout. We integrate the resolution of cycles in the algorithm for computing state probabilities of the BAG. The benefit of our approach is twofold. First, we establish a more formal base for the discussion of attack graphs, (cyclic) BAGs and solution techniques for BAGs, something that has not been strongly developed in the literature thus far. Secondly, we provide a single unified solution algorithm for BAGs that

resolves the problem of cycles for any cyclic BAG, without altering the attack graph.

Our most significant contribution is a single unified solution to the static analysis of any BAG that does not modify the graph in any way while being able to run on graphs containing cycles. This can be used to properly analyse security threats to a network and correctly prioritise remediation steps. Moreover, when applied to acyclic BAGs, our solution provides exactly the same results identical with the outcome of approaches in the literature that deal only with the acyclic case, thus is a generalisation of these approaches.

More specifically, we first formalize two common types of attack graphs, and compare their expressiveness. The AND/OR style of attack graphs is the most powerful and is used subsequently throughout the paper. We then introduce a novel interpretation and formalization of attack graphs using combinational logic circuits that helps us reason about cycles more effectively. Combinational circuits allows one to capture intuitively the notion of subsequent visits to the same state, which we use to reason about cycles. We show that the types of cycles studied in the literature correspond to different ways in which probabilities change as a function of the visit count of a state.

Based on the formalization and the associated intuition, we derive an algorithm that handles cycles in BAGs regardless of their type in a natural manner. Due to the reasons mentioned above, the algorithm does not explicitly identify the edges in the attack graph that should be removed. Instead, it integrates the identification of cycles with the solution algorithm and then terminates the recursion. The algorithm is suitable for solving state probabilities in the BAG, and gives results for acyclic BAGs that are identical with the output of traditional solvers for acyclic BAGs.

To study the scalability of our algorithm, we generate synthetic BAGs of various size, in a manner similar to [3]. We conclude that the algorithm can be used with BAGs of size 15000 nodes with reasonable computation time, implying it can scale to be used with networks of at least 750 hosts each with 5 vulnerabilities.

The rest of this paper is organised as follows. Section II introduces the network architecture that will be used as a running example throughout the paper. It also provides the motivation for our contributions and discusses two common formalisms for the construction of BAGs, then relates and shows the equivalence between the two formalisms. Section III introduces Bayesian networks and relates the process of Variable Elimination for Bayesian networks to the calculation of probabilities in acyclic BAGs. Section IV shows how an attack graph can be interpreted as a deterministic combinational circuit with probabilistic inputs. Section V presents our unified solution for dealing with both cyclic and acyclic BAGs, and section VI details the experiments run for our solution on both common and simulated examples. Finally, related works and our conclusions are presented in Sections VII and VIII, respectively.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Network architecture used as a running example.

## II. Motivation and Problem Formulation

### A. Running Example

As a motivating example for this work, we will consider a network architecture that could be used in a small enterprise situation. It is an example that has been used in the literature [8], [18]. The architecture is shown in Figure 1. The network comprises of a Database server on the internal network. This can be accessed through an internal firewall by both the user Workstations and the Webserver, that exists in the demilitarized zone subnet. This Webserver connects to the Internet via an external firewall.

For this scenario, we suppose a vulnerability scan has been run on the network, revealing three vulnerabilities that are present. There is a MySQL vulnerability on the Database server, an Apache vulnerability on the Webserver, and an Internet Explorer vulnerability on the Workstations. The workstations are modelled as a single host and imagined to be all similarly set up and patched. This is not necessarily the case however, and will depend on the specific setup for the organization.

Figure 2 is the corresponding BAG for this situation. It is comprised of two node types; diamonds (OR nodes) represent a state that an attacker can be in like a certain level of privilege with respect to a host, and ellipses (AND nodes) are actions like exploiting a vulnerability or connecting to a host. Section II-B gives a formal definition of these nodes. For clarity, all Leaf nodes are removed so that the different routes to the Database server are easier to see, and have been numbered so they may be referred to (a description of each node can be found in Appendix B). The directed edges are dependencies, an OR node can be reached if any of the parents are reached, whereas an AND node can only be reached if every parent has been reached. The colours correspond to the colours in Figure 1; blue is a node that relates to the Workstations, green

![img-1.jpeg](img-1.jpeg)

Fig. 2. An excerpt of the BAG of the running example. Node colours correspond with the components of the network presented in Figure 1.

to the Webserver, and red to the Database server. Node 0 in white represents an attacker from the Internet.

A feature of this graph is the presence of *loops* that has been already studied in the literature. For instance, the sequence of nodes (11, 9, 8, 7, 6, 4, 3, 23, 11) forms a loop (cf. Definition 2.1). Another important aspect of the graph is the presence of *cycles*. For instance, the sequence of nodes (14, 12, 11, 9, 8, 7, 6, 21, 14) forms a cycle due to node 21 joining back to node 14. This cycle represents the fact that there are two different ways to gain access to a Workstation, and that once access is achieved a future state also allows a Workstation to be compromised. A user can simply access a malicious website, shown on the route along nodes 15 and 14, or alternatively an attacker could exploit the vulnerability on the Webserver (nodes 22, 8, 7, 6) and then compromise a website from there using the Webserver to gain access to the workstation.

Because this cycle can be entered into from multiple nodes (either 14 or 8), calculating the probability of an attacker reaching node 14, or indeed any other node in the cycle, cannot be done using basic approaches to solving BAGs. The *monotonicity principle*, which states that an attacker will always increase their privilege [19], cannot be used to remove the edge (between 21 and 14) either. This is because it is possible for an attacker to reach node 14 for the first time using the edge (21 to 14) that needs to be removed, if they enter the cycle travelling from node 22 to node 8. As such there is no loss of privilege and the graph cannot be simplified. Our approach performs the computation on the graph without the need for any simplification.

A more complete discussion of the scenario and attack graph, including the specific vulnerabilities, can be found in Appendix B.

### *B. BAG Formalisms*

In this section, we introduce two different attack graph formalisms widely used in the literature for modeling a network from the security perspective. The first one is proposed in [17] and the second one in [20]. We will then show in Section II-C that the second formalism is more general than the first one and work with that representation after this section. Note that both formalisms require the attack graph to be acyclic. We use these formalisms as a basis for generalising them to cyclic graphs. We first define cycles and loops in directed graphs.

*Definition 2.1:* Given a directed graph *G* = (*V, E*) with the set of nodes *V* and the set of edges *E* ⊂ *V* × *V*, a *cycle* is a sequence of nodes (*v*<sub>1</sub>, *v*<sub>2</sub>, ..., *v*<sub>*n*</sub>) such that (*v*<sub>*i*</sub>, *v*<sub>*i*+1</sub>) ∈ *E* for all *i* and *v*<sub>*n*</sub> = *v*<sub>1</sub>. The graph is called acyclic if it does not have any cycles. A *loop* is a sequence of nodes (*v*<sub>1</sub>, *v*<sub>2</sub>, ..., *v*<sub>*n*</sub>) such that *v*<sub>*n*</sub> = *v*<sub>1</sub> and for any *i*, either (*v*<sub>*i*</sub>, *v*<sub>*i*+1</sub>) ∈ *E* or (*v*<sub>*i*+1</sub>, *v*<sub>*i*</sub>) ∈ *E*.

Loops can be seen as cycles in the undirected version of the graph, i.e., when the pair (*v*, *v*<sup>0</sup>) is treated the same as (*v*<sup>0</sup>, *v*). According to Definition 2.1, any cycle is also a loop but in the sequel, we use the word 'loop' to refer to those that are not cycles. Moreover, an acyclic graph can still have loops. Most of the literature on BAGs is focused on acyclic graphs as defined next.

#### *1) Plain BAGs:*

*Definition 2.2:* An attack graph *G* is a directed graph *G* = (*E* ∪ *C*, *R*<sub>*r*</sub> ∪ *R*<sub>*i*</sub>) where *E* is a set of exploits, *C* a set of conditions, and *R*<sub>*r*</sub> ⊆ *C* × *E* and *R*<sub>*i*</sub> ⊆ *E* × *C*.

*Remark 1:* According to Definition 2.2, the attack graph is *bipartite*, i.e., the set of nodes of the graph is divided into two disjoint and independent sets *E* and *C* such that every edge can only connect a node from one to another. That is why the set of nodes is partitioned into a subset of *C* × *E* and a subset of *E* × *C*.

The edges connecting conditions to exploits have a particular meaning: all the conditions connected to an exploit must be satisfied in order to execute that exploit. This is the equivalent of taking the conjunction of the incoming conditions to the exploit. Similarly, any of the exploits connected to a condition can be used to satisfy that condition. This is equivalent to a disjunction between multiple exploits that satisfy the same condition. Such an interpretation together with individual scores assigned to the nodes fully characterises the attack model.

*Definition 2.3:* Given an *acyclic* attack graph *G* = (*E* ∪ *C*, *R*<sub>*r*</sub> ∪ *R*<sub>*i*</sub>), and an individual score assignment function *p* : *E* ∪ *C* → [0, 1], the cumulative score function *P* : *E* ∪ *C* → [0, 1] is defined as

$$
\begin{aligned}
P(e) &= p(e) \cdot \Pi_{c \in R_i(e)} P(c) \\
P(c) &= p(c), \quad \text{if } R_i(c) = \emptyset \\
P(c) &= p(c) \cdot \oplus_{e \in R_i(c)} P(e), \quad \text{if } R_i(c) \neq \emptyset,
\end{aligned}
\tag{1}
$$

where ⊕<sub>*e*∈*R*<sub>*i*</sub>(*e*) *P*(*e*) is the probability of the union of exploits in *R*<sub>*i*</sub>(*c*) and is computed assuming the exploits are independent.

The acyclic attack graph *G* = (*E* ∪ *C*, *R*<sub>*r*</sub> ∪ *R*<sub>*i*</sub>) together with the individual scores defines a *plain BAG*. Note that attack

graphs can in general have cycles but plain BAGs are defined with acyclic attack graphs.
2) AND/OR BAGs: The second formalism of BAG is defined by Ou [20] and is used in MulVAL [12].

Definition 2.4: A Bayesian attack graph is defined as a directed acyclic graph $\mathcal{G}=(\mathcal{V}, \mathcal{E})$ where nodes $\mathcal{V}$ are connected by edges $\mathcal{E}$. The set of nodes is comprised of three types of nodes, $\mathcal{V}=V_{l} \cup V_{a} \cup V_{o}$, and edges are defined as $e_{i j} \in E, e_{i j}=e\left(v_{i}, v_{j}\right)$ where each edge $e$ defines a mapping from node $v_{i}$ to node $v_{j}$.

The sets of nodes are defined as follows:

- $V_{l}$ : the leaves in the graph, having no parents, and represent specific configurations and conditions in the network; this includes information about programs running on a host, network connection information in the form of HACLs (host access control lists), and the existence of vulnerabilities.
- $V_{a}$ : the AND nodes, which have requisite conditions all of which have to be fulfilled in order to be accessed. In other words there is a conjunctive relationship between the parents of such a node. This set of nodes is used to represent specific actions that can be taken when the conditions are fulfilled; this can be something like movement between hosts when an attacker has fulfilled the prerequisite of access to one machine and there exists a configuration node for access between the two nodes, or could be the remote exploit of a specific vulnerability given remote access and the existence of the vulnerability as prerequisites.
- $V_{o}$ : the OR nodes, which have requisite conditions of which at least one must be fulfilled in order to be accessed. There is a disjunction between the parents of such a node. These are specific micro-states in the network that define something about an attacker's position in the system, for example the ability to execute arbitrary code on a specific host or network access to a specific host. A macro-state for an attacker would be an enumeration of these nodes demonstrating the privilege they have with respect to every host on the network.

Vulnerabilities in the network have a chance to be exploited when their preconditions are fulfilled, and by exploiting a vulnerability an attacker achieves a specific state. This state, once reached, may then afford the attacker a privilege level on the network that is a requirement for another exploit, or node. A chain of nodes in the network connected in this way represents an attack path or route.

We define the access probability $P(v)$ on the node $v$ as the likelihood of the node being reached in an attack situation.

Definition 2.5: For a given BAG $\mathcal{G}=(\mathcal{V}, \mathcal{E})$ and a local probability function $p: \mathcal{V} \rightarrow[0,1]$, the access probability $P: \mathcal{V} \rightarrow[0,1]$ is defined recursively using the access probabilities of all parents to the node in conjunction with
the local probability by

$$
P(v)= \begin{cases}p(v) & \text { if } v \in V_{l} \\ p(v) \prod_{v^{\prime} \in p a(v)} P\left(v^{\prime}\right) & \text { if } v \in V_{a} \\ p(v)\left[1-\prod_{v^{\prime} \in p a(v)}\left(1-P\left(v^{\prime}\right)\right)\right] & \text { if } v \in V_{o}\end{cases}
$$

where $p a(v)$ represents the parent set of the node $v \in \mathcal{V}$, $p a(v):=\left\{v^{\prime} \in \mathcal{V} \mid\left(v^{\prime}, v\right) \in \mathcal{E}\right\}$.
The access probability has a slightly different interpretation depending on the specifics of the node. For $v \in V_{o}, P(v)$ represents the probability that the attacker will achieve the state described by node $v$. For $v \in V_{a}, P(v)$ represents the probability that an attacker will travel along that specific route to reach the goal state that follows. For $v \in V_{l}, P(v)$ represents the probability of successful exploitation if the node defines a vulnerability, or is the probability that a specific entry-route will be used.

Remark 2: Access probabilities $P$ defined in (2) assume that probabilities $P\left(v_{p a}\right)$ are independent from each other and takes the product of these probabilities to find the access probability for their child node. This assumption is only true if the graph of the BAG does not have loops. Otherwise, $P(v)$ in (2) will only be an approximation of true access probabilities that can be computed using joint distributions to reflect the dependencies between the related events. One of these exact methods is Variable Elimination discussed in Section III-B.

## C. Relation Between the Two Formalisms

In the following proposition, we show that the AND/OR definition of BAGs is more general than plain BAGs, as it abstracts away the type of nodes being exploits or conditions. Instead, it puts emphasis on their role in the computation of access probabilities.

Proposition 2.6: Any plain BAG modelled as in Definitions 2.2-2.3 can be transformed into a BAG modelled as in Definitions 2.4-2.5.

Proof: Suppose we have a plain BAG with the acyclic attack graph $G=\left(E \cup C, R_{r} \cup R_{i}\right)$. Define the set of leaf nodes as $V_{l}:=\left\{c \in C \mid R_{i}(c)=\emptyset\right\}$, the set of OR nodes $V_{o}:=C \backslash V_{l}$, and the set of AND nodes $V_{a}:=E$. Take $\mathcal{V}=$ $V_{l} \cup V_{a} \cup V_{o}$ and $\mathcal{E}=R_{r} \cup R_{i}$. Then $\mathcal{G}=(\mathcal{V}, \mathcal{E})$ is an attack graph satisfying all the requirements of Definition 2.4. Note that attack graphs of AND/OR BAGs are not necessarily bipartite, which makes them more general than plain BAGs.

## III. COMPUTATION OF ACCESS PROBABILITIES

The main approach for computing access probabilities of all nodes is to translate the model into a Bayesian network (BN) and apply off-the-shelf techniques developed in the literature for BNs. We first provide the translation of the BAG into a BN in section III-A and then discuss variable elimination as one of the techniques for performing probability computations over BNs in section III-B.

### V-A BAG Translation to a Bayesian Network

*Definition 3.1:* A Bayesian network (BN) is a tuple $\mathfrak{B}=(\mathcal{V},\mathcal{E},\mathcal{T})$. The pair $(\mathcal{V},\mathcal{E})$ is a directed acyclic graph representing the structure of the network. The nodes in $\mathcal{V}$ are (discrete or continuous) random variables and the arcs in $\mathcal{E}$ represent the dependence relationships among the random variables. The set $\mathcal{T}$ contains conditional probability distributions (CPD) in forms of tables or density functions for discrete and continuous random variables, respectively.

In a BN, knowledge is represented in two ways: qualitatively, as dependencies between variables by means of a directed acyclic graph; and quantitatively, as conditional probability distributions attached to the dependence relationships. Each random variable $v_{i}\in\mathcal{V}$ is associated with a conditional probability distribution $\operatorname{Prob}(v_{i}|pa(v_{i}))$.

*Proposition 3.2:* Any BAG $\mathcal{G}=(\mathcal{V},\mathcal{E})$ as in Definition 2.4 with local probability function $p:\mathcal{V}\rightarrow[0,1]$ in Definition 2.5 can be translated into a BN $\mathfrak{B}=(\mathcal{V},\mathcal{E},\mathcal{T})$. The random variables in $\mathcal{V}$ are all Boolean and the probability tables in $\mathcal{T}$ are constructed as follows. For all $v \in V_{l}$,

$$
\operatorname{Prob}(v=1)=p(v) \quad \text { and } \quad \operatorname{Prob}(v=0)=1-p(v)
$$

For all $v \in V_{o}$, let $pa(v)=\mathbf{1}$ indicate that all variables in $pa(v)$ take value equal to one. Then,

$$
\left\{\begin{array}{l}
\operatorname{Prob}(v=1 \mid p a(v)=\mathbf{1})=p(v) \\
\operatorname{Prob}(v=1 \mid p a(v) \neq \mathbf{1})=0 \\
\operatorname{Prob}(v=0 \mid p a(v)=\mathbf{1})=1-p(v) \\
\operatorname{Prob}(v=0 \mid p a(v) \neq \mathbf{1})=1
\end{array}\right.
$$

For all $v \in V_{o}$, let $pa(v)=\mathbf{0}$ indicate that all variables in $pa(v)$ take value equal to zero. Then,

$$
\left\{\begin{array}{l}
\operatorname{Prob}(v=1 \mid p a(v)=\mathbf{0})=0 \\
\operatorname{Prob}(v=0 \mid p a(v)=\mathbf{0})=1 \\
\operatorname{Prob}(v=1 \mid p a(v) \neq \mathbf{0})=p(v) \\
\operatorname{Prob}(v=0 \mid p a(v) \neq \mathbf{0})=1-p(v)
\end{array}\right.
$$

Then if the BAG $\mathcal{G}$ does not have any loops, we get $P(v)=$ $\operatorname{Prob}(v=1)$ for all $v \in \mathcal{V}$ with access probabilities $P$ defined in (2).

Figure 3 illustrates the construction of probability tables for an AND node. In this figure, the local probabilities are $p(A)=0.7, p(B)=0.8$, and $p(C)=0.6$. The probability tables for $A$ and $B$ are constructed according to (3) and for $C$ according to (4).

## B. Variable Elimination

Based on the results of section III-A, the computation of access probabilities is equivalent to the computation of marginal probabilities $\operatorname{Prob}(v=1)$ in the associated BN. *Variable elimination* (VE) is a simple and general algorithm developed in the literature that computes exact values of these marginal probabilities (e.g., [21]). Given that the structure of the graph $(\mathcal{V}, \mathcal{E})$ models the independence between random variables associated with the nodes, we can obtain the joint distribution

![img-2.jpeg](img-2.jpeg)

Fig. 3. A simple BAG with the associated probability tables constructed according to Proposition 3.2. Local probabilities are $p(A)=0.7, p(B)=$ 0.8 , and $p(C)=0.6$.

![img-3.jpeg](img-3.jpeg)

Fig. 4. A subgraph of the running example indicating a loop.

of the variables as the product of the conditional probability tables $\prod_{v^{\prime} \in \mathcal{V}} \operatorname{Prob}\left(v^{\prime} \mid p a\left(v^{\prime}\right)\right)$. Then the marginal probabilities are computed by taking the sum over the unwanted variables:

$$
\operatorname{Prob}(v)=\sum_{v^{\prime} \neq v, v^{\prime} \in\{0,1\}} \prod_{v^{\prime} \in \mathcal{V}} \operatorname{Prob}\left(v^{\prime} \mid p a\left(v^{\prime}\right)\right)
$$

VE provides a procedure for the computation of the sumproduct in (6). The main goal of the algorithm is to specify at each iteration which tables to multiply and which variable to sum over. The reader may refer to the book [21, Chapter 9] for a detailed discussion on VE.

*Proposition 3.3:* The access probabilities of Definition 2.5 are equal to the marginal probabilities of the BN of Definition 3.1 obtained by variable elimination in the case that the BAG does not have any loops.

In the case that the BAG does have loops, the access probabilities will not necessarily be equal to the marginal probabilities calculated using VE. This can be shown by taking the first loop from Figure 2 and using the local probabilities shown in Figure 4, then marginalizing node 8 with VE and calculating the access probability for the same node using (2) of Definition 2.5. The former gives a probability of 0.7104 for node 8 being True; the latter gives 0.7795 . This discrepancy is due to nodes 15 and 22 being assumed to be independent while having a common ancestor (cf. Remark 2). In other words the probability at node 0 is being allowed to contribute more than it should to the final result, hence the higher calculated probability. This level of discrepancy is already studied in the literature: VE is known to give the exact values while other

![img-4.jpeg](img-4.jpeg)

Fig. 5. Logic gate representation of AND and OR nodes.

![img-5.jpeg](img-5.jpeg)

Fig. 6. A graph using definitions 2.4-2.5, with local probability in OR node C.

computational approaches give approximate values for BAGs with loops [22].

## IV. COMBINATIONAL CIRCUITS WITH PROBABILISTIC INPUTS

As one of the main contributions of this paper, we look at the attack graph from a different perspective and model it as a deterministic combinational circuit with probabilistic inputs. This interpretation paves the way towards including and analyzing cycles directly in the computation of access probabilities over attack graphs. Combinational circuits are mainly studied in the literature [23], [24] from the perspective of constructing a certain distribution on the output of the circuit by applying random inputs.

Let us enlarge the attack graph (V, E) with the set of nodes V = {v1, v2, …, vn} to an augmented attack graph (V̄, Ē) with nodes Ṽ := {v1, v2, …, vn, v1', v2', …, vn} and edges Ē := E ∪ {(v1', v1), …, (vn', vn)}. The augmented graph is obtained by adding one node v' for each node v ∈ V and connecting it directly to v. The added node v' has the role of modeling local probabilities at node v and renders the behaviour of this node non-probabilistic. Assuming a delay in the computation of the value of the node, we get one of the following two equations for each node:

$$
\begin{aligned}
v(k+1) &= g_o(pa(v)(k), v') \\
or \\
v(k+1) &= g_o(pa(v)(k), v'),
\end{aligned}
$$

![img-6.jpeg](img-6.jpeg)

Fig. 7. The graph of Figure 6 transformed into a graph with probabilities only on leaves.

where v(k+1) and pa(v)(k) indicate respectively the value of node v at k+1<sup>st</sup> iteration and the values of the parent nodes of V at k<sup>th</sup> iteration. The two functions g<sub>a</sub> and g<sub>o</sub> correspond to the AND node or the OR node respectively, and are depicted in Figure 5 using logic gates. Note that the Leaf nodes can be treated as either AND nodes or OR nodes.

A demonstration of enlarging an attack graph to make internal nodes behave in a non-probabilistic way can be seen in Figures 6 and 7. Figure 6 is an AND/OR BAG, with the probability table for the OR node shown to the right. We can move the local probability to a Leaf node, and as such all the internal probability tables simply become logical AND and OR tables. This is shown in Figure 7, where the equivalent BAG is shown, and the left and central probability tables can be recognised as logical OR and AND truth tables respectively, with the rightmost probability table containing the local probability on a leaf of the graph.

*Theorem 4.1:* The behaviour of an attack network can be modelled as a combinational circuit with probabilistic inputs. The value of the variables are changing according to the equation

$$
\begin{cases}
v_1(k+1) = g_1(pa(v_1)(k), v'_1) \\
v_2(k+1) = g_2(pa(v_2)(k), v'_2) \\
\vdots \\
v_n(k+1) = g_n(pa(v_n)(k), v'_n),
\end{cases} \tag{7}
$$

where k = 0, 1, 2, … models the progression of an attacker in gaining access to the nodes or satisfying conditions along the time axis, g<sub>i</sub> ∈ {g<sub>a</sub>, g<sub>o</sub>} for all i, with g<sub>a</sub>, g<sub>o</sub> defined according to Figure 5. The nodes v'<sub>i</sub> take values {0, 1} according to the local probabilities. The notation (k) is used for the k<sup>th</sup> iteration.

Access probabilities are equivalent to the computation of reachability probabilities over the augmented graph:

$$
\text{Prob}(v = 1) = \text{Prob}\{v(k) = 1 \text{ for some } k\}, \tag{8}
$$

where the probability is computed over all combination of values of $\left\{v_{1}^{\prime},v_{2}^{\prime},\ldots,v_{n}^{\prime}\right\} \in\{0,1\}^{n}$. Unlike previous formalisms that are not able to handle cycles, our new interpretation can easily encode cycles without the need for any modification.

Next we prove a property of this interpretation that helps in developing our algorithm for the computation of reachability probabilities in (8).

Proposition 4.2: The system of equations (7) is monotonically increasing, i.e., $v_{i}(k+1) \geq v_{i}(k)$ for any $k$ and $i$ and any instantiation of $\left\{v_{1}^{\prime}, v_{2}^{\prime}, \ldots, v_{n}^{\prime}\right\}$.

Proof: Fix an instantiation of $\left\{v_{1}^{\prime}, v_{2}^{\prime}, \ldots, v_{n}^{\prime}\right\}$. First we show that the function $g_{a}$ is monotonically increasing, which is the property that $g_{a}\left(w, v^{\prime}\right) \geq g_{a}\left(w^{\prime}, v^{\prime}\right)$ for any $w, w^{\prime}$ with $w \geq w^{\prime}$ element-wise. Note that $g_{a}\left(w^{\prime}, v^{\prime}\right)=0$ if an element of $w^{\prime}$ or $v^{\prime}$ is zero, which means the inequality holds. If all elements of $w^{\prime}$ and $v^{\prime}$ are one, then all elements of $w$ is also one, which means $g_{a}\left(w, v^{\prime}\right)=g_{a}\left(w^{\prime}, v^{\prime}\right)=1$ and the inequality holds.
Next we show that the function $g_{o}$ is monotonically increasing, which is the property that $g_{o}\left(w, v^{\prime}\right) \geq g_{o}\left(w^{\prime}, v^{\prime}\right)$ for any $w, w^{\prime}$ with $w \geq w^{\prime}$ element-wise. This holds due the identity $g_{o}\left(w, v^{\prime}\right)=1-g_{a}\left(1-w, 1-v^{\prime}\right)$ that the OR gate is the complement of the AND gate:
$w \geq w^{\prime} \Rightarrow 1-w \leq 1-w^{\prime}$
$\Rightarrow g_{a}\left(1-w, 1-v^{\prime}\right) \leq g_{a}\left(1-w^{\prime}, 1-v^{\prime}\right)$
$\Rightarrow 1-g_{a}\left(1-w, 1-v^{\prime}\right) \geq 1-g_{a}\left(1-w^{\prime}, 1-v^{\prime}\right)$
$\Rightarrow g_{a}\left(w, v^{\prime}\right) \geq g_{o}\left(w^{\prime}, v^{\prime}\right)$.
Now the claim follows inductively from the fact that initially $v(k)=0$ for $k=0$, and functions $g_{a}$ and $g_{b}$ are non-negative and monotonically increasing.

Theorem 4.3: The solution of (7) converges to a unique steady state in finite time, i.e., there is a time instance $k^{*}$ such that $v_{i}\left(k^{*}+1\right)=v_{i}\left(k^{*}\right)$ for any $i$ and any instantiation of $\left\{v_{1}^{\prime}, v_{2}^{\prime}, \ldots, v_{n}^{\prime}\right\}$.

## Theorem 4.4:

For an acyclic BAG with the time instance $k^{*}$ defined in the previous theorem, $\operatorname{Prob}\left(v\left(k^{*}\right)=1\right)$ is the same as the probability computed via Variable Elimination on the BAG. Furthermore, if the BAG does not have loops, this quantity is the same as access probabilities in (2).

Reachability probabilities $\operatorname{Prob}\left(v\left(k^{*}\right)=1\right)$ are well-defined on combinational circuits regardless of the existence of cycles. Therefore, the above theorem gives a nice direction for generalizing computations to cyclic BAGs. In the next section, we provide an algorithmic computation of probabilities while replacing the joint distributions with product of marginal distributions, similar to (2).

## V. Calculation on Cyclic BAGs

## A. Algorithmic Inference

We have created an algorithm to propagate probabilities through an attack graph and thus generate a BAG based on the probabilities assigned at the leaves of the graph. The algorithm, shown in Algorithm 1, works by detecting all attack paths that lead to a node. It moves through each step in each attack path collapsing cycles by the method previously discussed
(prevention of multiple instances of the same node from contributing to the probability multiple times) and calculating probabilities using the recursive conjunction and disjunction functions. Probabilities on a path are calculated fully for each node as the chance of a node being reached, but will not necessarily reflect its contribution to the proceeding nodes. In essence this means that when a node is being calculated, all the nodes that contribute to this probability are identified and only allowed to contribute to the final calculation once, thus ensuring that no nodes in a loop inflate the final probability by being counted multiple times. The order of calculation for the nodes does not matter and can be performed in a random order as contributions to a probability are explicitly calculated for each node every time.

The input to the algorithm is the graph with local probabilities. The pop (int) function used in the Disjunction and Conjunction functions in Algorithm 1 is a list function that returns the item, in this case a probability, at the given list index then removes it from the list.

This algorithm achieves a calculation for node probabilities that makes sense given the context of network security without the normal requirement for removing edges from the graphs. This means that attack routes on graphs can be better understood while also improving the versatility of graphs as extra portions can be added and the new nodes can be calculated correctly as no edges have been removed.

## B. Complexity of the Algorithm

The complexity of Algorithm 1 can be calculated as $O\left(n \times \max _{v}|\operatorname{Pr}(v)|\right)$ where $n$ is the number of nodes in the attack graph. In the worst case, when every added node is required to be present in the calculation of every other node, the complexity of the algorithm is $O\left(n^{2}\right)$. If the cyclicity of the graph is known, then the complexity becomes $O\left(n\left(c n+\max _{v}|\operatorname{Pr}(v)|\right)\right)$ where $0 \leq c \leq 1$ and $c$ is the portion of nodes that are in at least one cycle.

## C. Selection of Local Probabilities

In order to infer the access probabilities for the nodes passed to the algorithm, an initial set of local probabilities must be provided. These were originally generated from a simplistic evaluation of the ease to exploit a vulnerability (with non leaf local probabilities set to 1 as discussed earlier in Section 3.2). In order to determine the ease of access, the CVSS vector [25], [26] for the vulnerability is collected from NIST's National Vulnerability Database (NVD). Currently the Access Complexity (CVSSv2) or the Attack Complexity (CVSSv3) is used to define the probability of transitioning to a state. This is on a scale of Low, Medium and High for version 2 and Low and High for version 3, with High meaning there is a great deal of skill or timing required to exploit the vulnerability and as such is associated with the lowest probability scoring. A demonstration of how these values could inform the local probabilities is shown in Table I.

The local probabilities are taken from the contribution that the NVD gives to a vector score when calculating the

Input: Attack Graph; nodes $v$ in $V$ with local probability $p(v)$
Output: Bayesian Attack Graph; nodes $v$ in $V$ with access probability $P(v)$
for $v \in V$ :
$P(v)=$ RecursiveProbability $(v, v)$
def RecursiveProbability (node $v$, origin node $v_{\text {origin }}$ ) :
if $v \in V_{l}$ :
return $p(v)$
else:
for $v_{p a} \in V_{\text {parents }}$ :
if $v_{p a}$ is $v_{\text {origin }}:$ append 0 to p_list
elif $v_{p a}$ has been visited already :
if $v_{p a} \in V_{l}$ :
append $p\left(v_{p a}\right)$ to p_list
else:
append 0 to p_list
else:
append
RecursiveProbability ( $v_{p a}$, $v_{\text {origin }}$ ) to p_list
if $v \in V_{a}$ :
return Conjunction ( $p_{-}$list)
if $v \in V_{o}$ :
return Disjunction ( $p_{-}$list)
Disjunction (Probability List $P$ )
/* Calculating the disjunctive probabilities for OR nodes
Input: List of probabilities
Output: Disjunction of the probabilities
$\mathrm{p}=P \cdot \operatorname{pop}(0)$
if length of $P$ is larger than 1 :
recursive_p = Disjunction $(P)$
$\mathrm{p}=\mathrm{p}+$ recursive_p - recursive_p $\times \mathrm{p}$
elif length of $P$ is equal to 1 :
return $p+P[0]-p \times P[0]$
else:
return $p$
return $p$
Conjunction (Probability List $P$ )
/* Calculating the conjunctive probabilities for AND nodes
Input: List of probabilities
Output: Conjunction of the probabilities
$\mathrm{p}=P \cdot \operatorname{pop}(0)$
if length of $P$ is larger than 1 :
recursive_p = Conjunction $(P)$
$\mathrm{p}=$ recursive_p $\times \mathrm{p}$
elif length of $P$ is equal to 1 :
return $p \times P[0]$
else:
return $p$
return $p$
Algorithm 1: Propagating probabilities through the attack graph. The conjunctive and disjunctive functions correspond to calculating probabilities on OR and AND nodes, respectively.

TABLE I
COMPLEXITY SCORES AND THEIR LOCAL PROBABILITIES.


whole CVSS score. While this is a useful approximation, it is very abstract and ignores a great deal of the information that can be gleaned from the information available about the vulnerabilities. A discussion of this can be found in Section VII.

## VI. EXPERIMENTAL RESULTS

## A. Application to Simulated Networks

In order to test the practicality of the algorithm, it was implemented in Python, alongside a simulator that can generate attack graphs with cycles. This simulator builds a random attack graph with a specifiable quantity of cycles; it is given a percentage of cycles to artificially add, and ensures that the given percentage of OR nodes are involved in cycles (as this is where cycles originate, from the state of privileged access that allows potential future access to a vulnerability that has already been exploited). The graph is built out of nodes generated with a Leaf:AND:OR ratio of 50:35:15 in order to model the fact that approximately half a common attack graph comprises of configuration Leaf nodes, and there are fewer nodes representing states than there are representing attack steps (this is due to the fact that multiple different AND nodes can lead to the same OR node i.e. many actions can lead to the same state).

Attack graphs were simulated in increasing sizes, from 500 to 15000 in step sizes of 500 , and in four different groupings; ' $0 \%$ cyclic' where there are no cycles in the graph, ' $5 \%$ cyclic' where five percent of OR nodes are involved in cycles, ' $25 \%$ cyclic', and ' $100 \%$ cyclic' where every node, excluding Leaf nodes, is included in a cycle. Every situation was simulated five times, and the computation time required to complete exact inference using the algorithm was timed. These results are shown in Figure 8. Plotted are the average values for each amount of nodes, as well as range bars for the minimum and maximum values.

As can be seen, the algorithm can generate probabilities for graph sizes of at least 15000 nodes in the worst possible case in a moderate time frame, around 155 minutes. Thus the algorithm is suitable for use on medium-large sized networks, especially if modeling techniques like consolidating similar work stations into singles nodes is used. By way of comparison, an enterprise with 300 machines, each with an average of 5 vulnerabilities, would create a graph of around 6000 nodes. In a worst case situation regarding cycles, the probabilities could be calculated in approximately 600 seconds.

The effect of increasing the percentage of cycles at fixed node quantities was also examined, with results displayed in

![img-7.jpeg](img-7.jpeg)

Fig. 8. Time performance of Algorithm 1.

![img-8.jpeg](img-8.jpeg)

Fig. 9. Impact of cyclicity on the computation time.

Figure 9. Graphs were simulated with 1000, 3000 and 6000 nodes, with the percentage cycles being part of cycles is increased from 0 to 100 in steps of 10. The contribution of the cycles to the computation time increases with the quantity of cycles on the graph, up to an approximate 75% increase in computation time in the worst case in the ranges of nodes that we experimented with. This can be seen in both Figures 8-9 by comparing the results for 0% cyclicity with 100%. Including cycles seems like a somewhat expensive addition to graphs; however when any changes are to be modelled there will be no requirement to recompute the graph and as such the upfront cost will mean that only small portions of the graph will have to be computed after changes are made as the structure of the graph will be correct. In other words the upfront increase in time significantly reduces the cost of future adaptations and analyses of the graph.

### *B. Application to Realistic Networks*

To confirm the applicability of the results to realistic scenarios, we have implemented the algorithm on a collection of realistic networks. These are networks designed to replicate common real-life networking implementations for testing and modelling purposes. They are set up as a combination of virtual and real assets that function as an enterprise network, with different numbers of hosts and different vulnerabilities on each machine. These network scenarios return the same scan results that one would expect from running a vulnerability scan on the real network equivalent of the scenario.

We have considered three networks with respectively 10, 15, and 15 hosts; the first network comprises of a Linux database and workstation, an iOS device, a peripheral device that uses SMB and a Windows server, with all the remaining hosts being Windows workstations. The workstations have various commonly used applications installed (Chrome, iTunes, JDK) and are in various patching states. The other networks have similar enterprise topologies, see Appendix D for more details. Each network is scanned using a modified version of the OpenVAS vulnerability scanner [27], and then an attack graph is generated for each using MulVAL [12]. The number of nodes in the attack graphs generated from these networks is 1053, 2234 and 2341; all have naturally occurring cycles. This gives us attack graphs that are roughly 5% cyclic. The mean runtime of our algorithm is 3, 11, and 12 seconds, respectively. This runtime confirms the quantities reported in Figure 8: the simulations for attack graphs with 5% cyclicity and 1000 and 2000 nodes have mean runtimes of 2 and 18 seconds respectively when run on the same machine used for the realistic networks.

### *C. Evaluation on Examples from Literature*

To demonstrate the validity of our method we have applied Algorithm 1 on two common attack graphs from the literature; an acyclic graph generated from a scenario presented by Wang et al. [28], and the cyclic example in Figure 2 that was created by Ou et al. [20] and had probabilities calculated by Homer et al. by creating a larger equivalent graph that is acyclic [8]. The full demonstration of these comparisons can be seen in Appendix C. Once the acyclic example was converted from a plain BAG into an AND/OR BAG, our algorithm was run on both examples. The results were identical to the expected results in the other papers, demonstrating that this algorithm gives correct results for common network scenarios and generalises them to the larger class of cyclic BAGs.

### *D. Comparison with Exact Methods*

In order to verify and compare our results on acyclic graphs, we implemented the Variable Elimination algorithm of Section III-B on the simulated graphs that are acyclic. Due to the limitations of Variable Elimination, we implemented it on a series of small simulated graphs from 2 to 26 nodes, and compared the results with our algorithm. The average error of the quantities computed by our algorithm is ±0.011.

As can be seen in Figure 10, Variable Elimination despite being exact scales very poorly with one run on a 24 node graph taking approximately the same amount of time as a 11500 node run with our algorithm. Due to this poor scaling, the fact that Variable Elimination cannot run on cyclic graphs,

![img-9.jpeg](img-9.jpeg)

Fig. 10. Comparing computational time of our algorithm with Variable Elimination on acyclic graphs.

and the low average error from our algorithm, our approach is a much better choice for all practical applications.

## VII. RELATED WORK

Network vulnerability analysis using graph based approaches has been widely covered in the literature. A large body of work exists using attack graphs which propose approaches and tools for improved generation [17], [20], [29]–[31], visualization [32], [33], and analysis [19], [34], [35], or provide summaries of existing techniques [36]–[39]. Of the many types of attack graphs that exist, we have used dependency attack graphs, which facilitate understanding of the importance of individual vulnerabilities [40]. For a complete overview of the different techniques as well as a taxonomy for their formalisms we refer to Kordy et al. [38].

Bayesian network based network analysis has also been studied (e.g. [5], [10], [14], [15], [41]) as well as their generation. In particular, Choi et al. propose a method for deleting network edges from a Bayesian network in order to generate models through approximate inference [42]. In [22], Muñoz-González et al. apply an approximate inference approach called loopy belief propagation to Bayesian attack graphs and shows its performance compares favourably to the widely used exact inference technique, Junction Tree (JT). In [3] the authors explore an exact inference method using network clustering which they show enables the JT algorithm to become tractable and scale linearly with the number of nodes.

In order to improve the accuracy of these graphs, insightful local probabilities should be generated to maximise the information available to the Bayesian network. Doynikova and Kotenko demonstrate in [7] a more complex method for achieving more accurate results from CVSS data than simply using the complexity score, while also modelling attacks that do not rely on vulnerability exploitation through the use of the CAPEC list (Common Attack Pattern Enumeration and Classification), a taxonomy of different attack patterns described using the MITRE schema [43]. Cheng et al. model dependency relationships of the base metrics in the vectors and attempt to combine them in such a way that a user can weigh specific aspects for their local probability assignment [44].

A number of Markovian approaches have been taken to generate Bayesian attack graphs and facilitate vulnerability analysis and the design of optimal defence strategies. Jha et al. use a model checker to automatically generate attack graphs annotated with probabilities and analyse their vulnerabilities using Markov Decision Process (MDP) algorithms [45]. Mace et al. used a similar approach to find the optimal data collection strategies for accurate Bayesian attack graph input parameters (e.g. conditional probability tables) [46]. In [47] Piètre-Cambacédès et al. model attack trees as Boolean logic Driven Markov Processes (BDMP), suggesting they are dynamic and inherit readability and appropriation of attack trees but with mathematical properties reducing combinatorial problems and processing. Continuous Time Markov chains have been applied by Jhawar et al. to the Bayesian attack graph approach in order to analyse attack defence graphs, that is, attack graphs which define the modelling of defences in their specification. Wang et al. in [28], estimate attack states and define a cost-benefit heuristic to automatically infer optimal defences for attack graphs integrated with Hidden Markov Models while Miehling et al. [9] and Zhisheng et al. [48] assume the defender can only partially observe the attacker's capabilities at any given time, thereby modelling Bayesian Attack Graphs as partially observable Markov decision processes (POMDPs). In this sense a resulting defence strategy is both reactive and anticipatory.

Dealing with cycles in Bayesian attack graphs has also been tackled (e.g. [49], [50]). Kłopotek et al. who use Markov Chains, suggesting the state of a variable is not influenced by itself but rather the future state is influenced by the past one [51]. Doynikova and Kotenko consider the processing of three simple types of cycle in Bayesian attack graphs [7]. Two of the three types contain cycles between nodes at the same level in the graph structure. These are either removed once the probabilities to reach each node for the first time have been calculated, or enumerated as separate paths. The third type contains cycles between nodes at different levels of the graph structure. In this case, the cycle is simply removed under the backtracking assumption, that is an attacker does not come back to a node already exploited. In [1], Aguessy et al. present a Bayesian network-based extension to attack graphs, called a Bayesian Attack Model (BAM), which is capable of handling cycles by breaking them. The authors argue that using the backtracking assumption to break cycles suppresses possible attacker actions which cannot be known a priori. To keep all possible paths, the only way to break cycles is to enumerate all paths starting from every possible attack source. In other words, unfolding the cyclic graph structure to an equivalent acyclic graph structure such that each node appears exactly once in each path. This process causes a

combinatorial explosion in the number of nodes whilst the inference algorithm is shown to remains efficient only for networks of up to 70 hosts. Homer et al. suggest their approach correctly handles both cycles and shared dependencies in attack graphs, that is the probabilities along multiple paths leading to a node are dependent on each other [8]. The authors suggest enumerating all paths is unnecessary if data flow analysis is applied to the cyclic nodes enabling the same probabilities to be evaluated as on the unfolded graph. The data flow analysis process uses dynamic programming and other optimizations to avoid increasing computational complexity. The algorithm is limited by the number of nodes and paths within cycles which must be considered when calculating probability values and which can cause evaluation time to be exponential in the worst case. The evaluation is based on the number of nodes and vulnerabilities per node and does not consider how the number of cycles impacts computation. Wang et al. made a number of crucial observations about cyclic attack graphs and proposed a customized probabilistic reasoning method that can handle cycles in the calculation [28]. However, when combining probabilities from multiple attack paths, the method uses a formula that assumes the multiple probabilities are independent. Such dependency needs to be accounted for to prevent a distortion of results.

## VIII. CONCLUSION

In this paper we have created and demonstrated a systematic approach to analyse Bayesian attack graphs, including those with cycles. Since cycles naturally arise in BAGs that are generated from scanning software (e.g., using MulVAL), it is imperative to establish practical approaches to handle cyclic BAGs. We presented a formal treatment of the problem domain and introduced a solution algorithm that can be applied to any BAG, cyclic or acyclic. This results in a method by which Bayesian attack graphs can be automatically evaluated with respect to what states are available to an attacker and how easily they are reached. Our solution deals directly with the cycles and integrate cycle resolution with the computation of state probabilities without the need for identifying or differentiating the cycle types. Our approach does not alter the attack graph by removing edges to make it acyclic. Instead, we preserve all the information in the graph, and no potential attack routes are lost when new data is added to the graph.

Our computational approach is currently restricted to single state probabilities and cannot compute joint probabilities for multiple nodes. A solution that allows the computation of joint probabilities is a next step to further advance the presented approach to cyclic BAGs. Future work will also involve extending the local probability assignment to have a more meaningful value; a temporal metric can be included given that the longer a vulnerability is known about the more likely an exploit has been published for it, increasing the ease of an attack. Scaleable solution algorithms then need to be identified to automate the analysis of these graphs to prioritise fixing of vulnerabilities and identifying most vulnerable network hosts, with regard to their criticality to an enterprise. Finally,
although the proposed algorithm can handle large models, for yet larger networks approximate solutions could be considered.

## APPENDIX A

## ATTACK GRAPHS WITH CYCLES

As we discussed in Section II, most of the literature on BAG probability computations have focused on acyclic attack graphs. This constraint ensures the probabilities on the nodes become the chance that an attacker reaches the node at all. In other words, paths that are enabled by access to a node should not increase the probability that that same node is reached. We presented a running example and showed that cycles can occur in a number of situations. Thus, this property should be extended for each node on the pathway calculations.

In the following, we first discuss types of cycles mentioned in the literature and the methods currently used to deal with these cycles. Next we put these types of cycles into the perspective of our computational algorithm and show how they can be interpreted over the associated combinational circuit. We emphasise that our solution does not modify the graph in any way while being able to run on graphs containing cycles. Our solution deals directly with the cycles and integrate cycle resolution with the computation of state probabilities without the need for identifying or differentiating the cycle types.

## A. Handling Cycles

There are three main types of cycles in an attack graph [7], [11], and Figures 11 to 13 show what they look like based on Definition 2.4. The first cycle type, Figure 11, can be demonstrated as removable. This is because node 2 has two prerequisites and one of them, node 5, is only fulfilled given that node 2 has been accessed. As such node 2 can never be true and the cycle will never occur and does not aid our understanding or modelling of the graph.

Figure 12 shows the second type of cycle, one that cannot be trivially removed like the first. Node 3 can be fulfilled by

![img-10.jpeg](img-10.jpeg)

Fig. 11. Cycle of Type 1.

![img-11.jpeg](img-11.jpeg)

Fig. 12. Cycle of Type 2.

![img-12.jpeg](img-12.jpeg)

Fig. 13. Cycle of Type 3.

either 2 or 6 meaning that node 7 is reachable. Since node 6 can only be accessed after node 3 has been accessed, it should not contribute to the likelihood of reaching nodes 3, 4, 5 or 7. In essence the edge from node 6 to 3 could be removed from the graph, and this is the necessary step in current acyclic BAG techniques.

An important addition to this discussion is that while edge removal does work for the second type of cycle, it is perhaps not the preferred solution. Firstly removing the edge can make the graph less understandable from an engineering perspective, as logically if reaching a state allows access to another element that was a prerequisite to a previous state then that route is possible. Also, more importantly, removing an edge, the edge from node 6 to node 3 in our example, removes information that could be important in future. If it was desired that a new vulnerability be added to the graph, for example in such a way that it would transform Figure 12 into Figure 13, then a legitimate route would now be missing from the graph and from any new calculations. As such, preserving the structure of the graph is important for both future analysis and understanding.

The third type of cycle, Figure 13, shows a cycle that cannot be ignored or fixed through edge removal. It is the same in structure as the Type 2 cycle but a node in the cycle has an extra way of being accessed, meaning there are now multiple routes to reach node 3. This type of cycle should be dealt with by imagining probabilities are populations of attackers and as such the quantities on the nodes should represent unique attacker numbers ensuring we do not double count attackers moving through the graph. Practically for this simplistic example this will mean the probability at node 6 is the disjunction of attackers coming from node 7 and the attackers reaching node 4 for the first time, i.e. the initial population at node 1 minus any attackers lost moving through nodes 2 and 3.

### *B. Cycles in Combinational Circuits*

Using the combinational circuit paradigm introduced in section 4, we can formally describe the different types of cycle. The finiteness of k<sup>*</sup> mentioned in Theorem 4.3 enables us to unfold the logic circuit k<sup>*</sup> number of times. Let us denote

$$pa(v_i) = \{v_{i1}, v_{i2}, \dots, v_{i,m_i}\}.$$

The unfolding is done sequentially by replacing each v<sub>ij</sub>(k) in the right-hand side of (7) with function g<sub>z</sub>(pa(v<sub>z</sub>)(k − 1), v<sub>i</sub><sup>j</sup>) where v<sub>z</sub> is the node associated with v<sub>ij</sub>. Starting this process from k<sup>*</sup> and repeating it k<sup>*</sup> times gives us a full circuit as

$$
\begin{cases}
v_1(k^*) = f_1(v_1', v_2', \dots, v_n') \\
v_2(k^*) = f_2(v_1', v_2', \dots, v_n') \\
\vdots \\
v_n(k^*) = f_n(v_1', v_2', \dots, v_n'),
\end{cases}
$$

where f<sub>i</sub>'s are associated to the unfolded circuit with a directed graph that does not have any cycles. Unfortunately, the procedure of unfolding and probability computation over (9) is computationally intense but it is very helpful in giving an automatic characterisation of cycle types in BAGs discussed in the literature [7], [11].

Cycles of Type 1 are seen when the steady-state value of a node is zero: v<sub>i</sub>(k<sup>*</sup>) = 0 for some i and for any instantiation of {v<sub>1</sub><sup>i</sup>, v<sub>2</sub><sup>i</sup>, ..., v<sub>n</sub><sup>i</sup>}. This means that the node cannot be reached and can be safely eliminated from the analysis. Any incoming edges or outgoing edges to this node can also be eliminated. If this elimination results in breaking a specific cycle, that cycle is of Type 1.

Cycles of Type 2 need more elaboration and are defined with respect to nodes that v<sub>i</sub>(k<sup>*</sup>) = 1. Let k<sup>*</sup><sub>i</sub> be the earliest time that the value of node v<sub>i</sub> becomes one:

$$k_i^* = min_{k}\{k, v_i(k) = 1\} \text{ for } i \text{ with } v_i(k^*) = 1.\tag{10}$$

It is obvious that $k_{i}^{*}$ depends on the instantiation of $\left\{v_{1}^{\prime}, v_{2}^{\prime}, \ldots, v_{n}^{\prime}\right\}$ and is upper bounded by $k^{*}$. The computation of $\operatorname{prob}\left(v_{i}\left(k^{*}\right)=1\right)$ requires unfolding (9) for $k_{i}^{*}$ times. Nodes with the property that $v_{j}\left(k_{i}^{*}\right)=0$ can safely be removed together with their outgoing and incoming edges. These are the nodes that do not have any influence on node $v_{i}$. If such elimination results in breaking a cycle, that cycle is of Type 2. Note that the elimination is valid when we only need to compute access probabilities of $v_{i}$ (the definition is with respect to a particular node).

The previous two types of cycles require properties that should hold for any instantiation of $\left\{v_{1}^{\prime}, v_{2}^{\prime}, \ldots, v_{n}^{\prime}\right\}$. Cycles of Type 3 are the ones that do not fit in the definition of cycles of Type 2. Formally, for a given node $v_{i}$, a cycle is of Type 3 if there exists a node $v_{j}$ on the cycle and an instantiation of $\left\{v_{1}^{\prime}, v_{2}^{\prime}, \ldots, v_{n}^{\prime}\right\}$ such that $v_{j}\left(k_{i}^{*}-1\right)=1$. This means node $v_{j}$ on the cycle can influence the access probability of node $v_{i}$, thus cannot be removed.

As discussed above, cycles of Type 3 cannot be removed and requires a particular attention when performing the probability computations. In the next subsection, we demonstrate the computation on the running example and provide the full algorithm in Section V.

## C. Calculating Probabilities: Running Example

Here we discuss how a cycle's probabilities should be calculated, as is implemented in the algorithm in the following section. Figure 14 is an excerpt from the larger attack graph of the running example presented in Section II-A. It is a simple example of how a Type 3 cycle (see Figure 13) can exist in a real attack graph. This excerpt is a trivial demonstration of the simplest occurrences of cycles in real attack graphs. The cycle occurs because of the multiple routes that can be taken to reach node 14, where an Internet Explorer vulnerability on the Workstations can be exploited using an HTML document. A user may visit a malicious website, represented by the route from node 15 to 14 , or alternatively the Webserver could be targeted first, and used to provide the HTML document once it has been compromised, shown in the route through nodes $8,7,6,21$ and then 14 .

The cycle is further complicated by the fact that the Webserver can be accessed directly without going through the Workstations, in the route from node 22 to 8 . Without the edge $e_{22,8}$, the edge causing the cycle $\left(e_{21,14}\right)$ could be safely trimmed as the probability of the attacker reaching node 14 does not increase due to node 21 as node 14 is a prerequisite for node 21 to be reached. Node 22 entering the cycle part way through, however, will increase the probability of reaching node 14 at some point in an attack as node 15 being accessed is no longer a requirement.

The result of calculating the probability of reaching each node, performed by disregarding nodes that have already contributed, can be seen in Figure 15. In order to calculate probabilities within the cycle, all the parent nodes are collected exhaustively. Their contribution to the probability of the node in question is then performed according to the relationships defined by the graph, as in definition 2.5, with the caveat that any node in the parent set may only contribute once to the calculation. In this way, calculating the probability of node 12 on Figure 14 will involve the likelihood of any attacker reaching node 14 from node 15, and also the likelihood of an attacker reaching node 14 from node 21, but with the removal of node 15 's contribution to the probability of reaching node 21 as node 15 has already been included. In this way each nodes probability can be calculated without the removal of any edge, as a node causing a loop in one place may contribute to probabilities elsewhere on the graph and as such should only be disregarded in specific calculations where it's effects have already been calculated. The ability for a node to be present in multiple paths but contribute differing amounts demonstrates the idea that a recursive algorithm that identifies each node's contribution to a path would be a correct solution to this problem, preventing any node from contributing multiple times to the same path.

## APPENDIX B

## Full Example

The complete attack graph for the running example scenario can be seen in Figure 16, with the labels for the nodes written out below. An important note is the reason the cycle exists: the state at node 14, whereby a user on one of the Workstation machines access a malicious website, can be reached via two means. Firstly the user can simply visit a malicious website allowing the attacker to exploit CVE-2009-1918 that is in Internet Explorer on the Workstation. Alternatively, an attacker that has achieved the ability to execute code on the Web Server (node 6) can serve the user of a Workstation machine an HTML document that exploits CVE-2009-1918 and thus also achieves the state on node 14.

This cycle is made more complex due to the ability to access the Webserver without passing through the Workstations originally (visiting nodes 22 and 8 ). Because of this, reaching node 14 via node 21 will not always mean that the attacker is travelling backwards, and as such the monotonicity principle does not apply and the probability of reaching node 14 becomes more challenging to calculate.

The vulnerabilities in this scenario are as follow:

- CVE-2009-1918 ${ }^{1}$ on the Workstations - Internet Explorer vulnerability that allows an attacker to execute arbitrary code on the machine after the user accesses a website with purposely malformed elements that trigger memory corruption
- CVE-2006-3747 ${ }^{2}$ on the Webserver - Apache vulnerability that can be exploited to execute arbitrary code using crafted URLs and requires network access to exploit
- CVE-2009-2446 ${ }^{3}$ on the Database Server - MySQL vulnerability where an authenticated user can cause a denial of service and possibly execute arbitrary code

[^0]
[^0]:    ${ }^{1}$ https://nvd.nist.gov/vuln/detail/CVE-2009-1918
    ${ }^{2}$ https://nvd.nist.gov/vuln/detail/CVE-2006-3747
    ${ }^{3}$ https://nvd.nist.gov/vuln/detail/CVE-2009-2446

![img-13.jpeg](img-13.jpeg)

Fig. 14. The cycle of the BAG presented in Figure 2.
![img-14.jpeg](img-14.jpeg)

Fig. 15. The cycle of the BAG presented in Figure 2 with computed access probabilities.
![img-15.jpeg](img-15.jpeg)

Fig. 16. The BAG of the running example including leaf nodes.

Listing 1. MulVAL labels for Figure 16

```
0, "attackerLocated(internet)"
1, "execCode(dbServer,root)"
2, "RULE 2 (remote exploit of a server
program)"
3, "netAccess(dbServer,tcp,'3306')"
4, "RULE 5 (multi-hop access)"
5, "hacl(webServer,dbServer,
tcp,'3306')"
6, "execCode(webServer,apache)"
7, "RULE 2"
8, "netAccess(webServer,tcp,'80')"
9, "RULE 5"
10, "hacl(workStation,webServer,tcp,'80'"
11, "execCode(workStation,userAccount)"
12, "RULE 2"
13, "vulExists(workStation,'CVE-2009-1918',
IE,remoteExploit,privEscalation)"
14, "accessMaliciousInput(workStation,
user, IE)"
15, "malicious website"
16, "visit of malicious website"
17, "vulExists(dbServer,'CVE-2009-2446',
mySQL,remoteExploit,privEscalation)"
18, "vulExists(webServer,'CVE-2006-3747',
apache,remoteExploit,privEscalation)"
19, "visit of compromised website"
20, "hacl(internet, webServer, tcp, '80')"
21, "compromise of website"
22, "RULE 6 (direct network access"
23, "RULE 5"
24, "hacl(workStation,dbServer,tcp,'3306')
```


## APPENDIX C

## RESULTS OF ALGORITHM ON COMMON EXAMPLES

## A. Acyclic Example

The network scenario, in Figure 17, is moving from a Workstation to root access on a Database server through a Firewall and possibly via a File server depending on the attack path. There are three services running on Machine 1, the file server, and two services running on Machine 2, the target Database server. An attack graph has already been generated for this scenario but using a different schema, shown in Figure 18. Here it can be seen that there are three possible paths for achieving the goal of root access to Machine 2; the attacker can either edit the trusted host list on Machine 2 to gain enough access to the host in order to run the buffer overflow attack, or the attacker can attempt to reach the same privilege by changing the relationship between Machine 1 and Machine 2, either by initially editing Machine 1's trusted host list or by attempting a buffer overflow attack against Machine 1.

First, an AND/OR BAG was generated from the plain BAG in Figure 18 using the principles discussed in the paper. This involves moving all less than one local probabilities to the leaf nodes allowing easy logical calculation of the marginal probabilities at each node. The algorithm was then run on the new attack graph with the same probabilities associated with the vulnerabilities as allocated in the original example to generate a new Bayesian attack graph. This new graph, Figure 19, shows the same probabilities for each part of the

![img-16.jpeg](img-16.jpeg)

Fig. 17. Example of a network taken from [28].

![img-17.jpeg](img-17.jpeg)

Fig. 18. BAG of the network of Figure 17 which is acyclic [28].

graph. This demonstrates that the algorithm is correct for this common acyclic graph example.

## B. Probability computations on the running example

The probabilities are calculated and shown in Figure 20 by applying Algorithm 1 to the running example presented in Section II-A and described in appendix C. This graph has all the nodes displayed, including the leaf nodes that were trimmed for clarity through the rest of the paper.

## APPENDIX D

## REALISTIC NETWORKS

### A. 1053 Nodes

This network is a simple small enterprise setup, with several workstations, some servers, and a collection of peripheral devices. The full host inventory can be seen in table II.

### B. 2234 Nodes

This network is a more complex enterprise example, and includes a server running TWiki that all the workstations can

![img-18.jpeg](img-18.jpeg)

Fig. 19. Converted graph from Figure 18 using the equivalence shown in Section II-C

TABLE II

HOSTS AND SOFTWARE FOR THE 1053 NODE REALISTIC NETWORK.


access for collaboration. The full host inventory can be seen in table III.

TABLE III

HOSTS AND SOFTWARE FOR THE 2234 NODE REALISTIC NETWORK.


### C. 2341 Nodes

This network has similar hosts to the 2234 Node example, but introduces an outdated Windows XP machine to the network, along with a machine for web development and a Red Hat MRG machine. The full host inventory can be seen in table IV.

![img-19.jpeg](img-19.jpeg)

TABLE IV
Hosts and Software for the 2341 Node Realistic Network.


Fig. 20. Results of Algorithm 1 applied to the cyclic running example.