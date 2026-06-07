# Decision Making Under Uncertainty 

JUDEA PEARL<br>University of California at Los Angeles (judea@canai.cs.ucla.edu)

For machines to act plausibly under uncertainty, certain basic components must be provided:
(1) a rationality criterion for choosing one decision over another;
(2) a versatile specification language for encoding the available knowledge and the uncertainties involved; and
(3) effective computational algorithms for implementing the choices dictated by (1) and (2).
Although classical decision analysis provides a reasonable conceptual basis for rational choices (i.e., maximal expected utility), it fails to provide ma-chine-friendly schemes for representing, updating and reasoning with uncertain knowledge. Rule-based systems, on the other hand, although computationally attractive, provide no basis for rationality or coherence. Attempts to bridge this gap have led to the development of graphical models known as Bayesian networks [Pearl 1988], which combine semantic coherence with computational manageability. This note surveys the development of Bayesian networks, summarizes their semantic basis and assesses their properties and applications.

## OVERVIEW

Bayesian networks are directed acyclic graphs (DAGs) in which the nodes represent variables of interest (e.g., the temperature of a device, the gender of a patient, a feature of an object, or the occurrence of an event) and the links represent causal influences among the variables. The strength of an influence
is represented by conditional probabilities that are attached to each cluster of parent-child nodes in the network.

Figure 1 illustrates a simple yet typical Bayesian network. It describes the causal relationships among the season of the year $\left(X_{1}\right)$, whether rain falls $\left(X_{2}\right)$ during the season, whether the sprinkler is on $\left(X_{3}\right)$ during that season, whether the pavement would get wet $\left(X_{4}\right)$, and whether the pavement would be slippery $\left(X_{5}\right)$. All variables in this figure are binary, taking a value of either true or false, except the root variable $X_{1}$, which can take one of four values: spring, summer, fall, or winter. Here the absence of a direct link between $X_{1}$ and $X_{5}$, for example, captures our understanding that the influence of seasonal variations on the slipperiness of the pavement is mediated by other conditions (e.g., the wetness of the pavement).
As this example illustrates, a Bayesian network constitutes a model of the environment rather than, as in many other knowledge-representation schemes (e.g., logic, rule-based systems, and neural networks), a model of the reasoning process. It simulates, in fact, the causal mechanisms that operate in the environment, and thus enables us to answer a variety of queries, including: associational queries, such as "Having observed $A$, what can we expect of $B$ ?"; abductive queries, such as "What is the most plausible explanation for a given set of observations?"; and control queries, such as "What will happen if we intervene and act on the environment?" Answers to the first type of query depend only on probabilistic knowledge of the domain, whereas answers to the sec-

Copyright (c) 1996, CRC Press.

![img-0.jpeg](img-0.jpeg)

Figure 1. A Bayesian network representing causal influences among five variables.
ond and third types rely on the causal knowledge embedded in the network. Both types of knowledge, associative and causal, can effectively be represented and processed in Bayesian networks.

The associative facility of Bayesian networks may be used to model cognitive tasks such as object recognition, reading comprehension, and temporal projections. For such tasks, the probabilistic basis of Bayesian networks offers a coherent semantics for coordinating top-down and bottom-up inferences, thus bridging information from highlevel concepts (e.g., objects or words) and low-level percepts (e.g., object's parts or letter's features). This capability is important for achieving selective attention, that is, selecting the most informative next observation before actually making the observation. In certain structures, the coordination of these two modes of inference can be accomplished by parallel and distributed processes that communicate through the links in the network.

However, the most distinctive feature of Bayesian networks, stemming largely from their causal organization, is their ability to represent and respond to changing configurations, such as those produced by unexpected eventualities (e.g., disabled sprinkler) or external interventions (e.g., turning the sprinkler
on regardless of the season). Any local reconfiguration of the mechanisms in the environment can be translated, with only minor modification, into an isomorphic reconfiguration of the network topology.

For example, to represent a disabled sprinkler, we simply delete from the network all links incident to the node "Sprinkler." To represent a pavement covered by a tent, we simply delete the link between "Rain" and "Wet." These local deletion operations enable one to distinguish actions from observations, a facility lacking in rule-based systems. For example, the act of turning on the sprinkler will have no effect on our belief in rain (because the edge from $X_{3}$ to $X_{1}$ will be deleted), whereas the observation that the sprinkler is on will (and should) affect our belief in rain (by abductive inference, through $X_{1}$, that the season is probably dry). This flexibility of handling reconfiguration is often cited as the ingredient that marks the division between deliberative and reactive agents and that enables the former to manage novel situations instantaneously, without requiring retaining or adaptation.

The ability to coordinate bidirectional inferences filled a void in expert systems technology of the late 1970s, and it is in this area that Bayesian networks first flourished. Over the past ten years,

Bayesian networks have become a tool of great versatility and power, and they are now the most common representation scheme for probabilistic knowledge [Shafer 1990; Shachter 1990]. They have been used to aid in the diagnosis of medical patients and malfunctioning systems [Shafer 1990], to understand stories, to filter documents, to interpret pictures, to perform filtering, smoothing, and prediction, to facilitate planning in uncertain environments [Dean and Wellman 1991], and to study causation, nonmonotonicity [Goldszmidt 1995], action [Pearl 1994], change, and attention [Pearl 1988]. Most of these applications are described in Pearl [1988], Shafer [1990], and Dean and Wellman [1991].

## PROPERTIES

The basic properties and capabilities of Bayesian network can be summarized as follows.
(1) The graphical representation makes it easy to maintain consistency and completeness in probabilistic knowledge bases. It also prescribes modular procedures of knowledge acquisition that significantly reduce the number of assessments required.
(2) Independencies can be dealt with explicitly. They can be articulated by an expert, encoded graphically, read off the network, and reasoned about, yet they forever remain robust to numerical imprecision.
(3) The graphical representation uncovers opportunities for efficient computation. Distributed updating is feasible in knowledge structures that are rich enough to exhibit intercausal interactions (e.g., "explaining away"). And, when extended by clustering or conditioning, tree-propagation algorithms are capable of updating networks of arbitrary topology [Pearl 1988; Shafer 1990].
(4) The combination of predictive and abductive inferences resolves many problems encountered by first-generation expert systems and renders Bayesian networks a viable model for cognitive functions requiring both top-down and bottom-up inferences.
(5) The causal information encoded in Bayesian networks facilitates the analysis of action sequences, their consequences, their interaction with observations, and their expected utilities, and hence the synthesis of plans and strategies under uncertainty [Dean and Wellman 1991; Pearl 1994].
(6) The isomorphism between the topology of Bayesian networks and the stable mechanisms that operate in the environment facilitates modular reconfiguration of the network in response to changing conditions, and permits deliberative reasoning about novel situations.

## ALGORITHMS

The first algorithms proposed for probability updating in Bayesian networks used message-passing architecture and were limited to trees and singly connected networks [Kim 1983]. The idea was to assign each variable a simple processor, forced to communicate only with its neighbors, and to permit asynchronous back-and-forth message-passing until equilibrium was achieved. Coherent equilibrium can indeed be achieved this way, but only in singly connected networks, where an equilibrium state occurs in time proportional to the diameter of the network.

Many techniques have been developed and refined to extend the tree-propagation method to general, multiply connected networks. Among the most popular are Shachter's method of node elimination, Lauritzen and Spiegelhalter's method of clique-tree propagation, and the method of loop-cut conditioning (see Pearl [1988] and Shafer [1990]).

Although the task of updating probabilities in general networks is NP-hard, the complexity for each of the three methods cited is exponential in the size of the largest clique found in some triangulation of the network. It is fortunate that these complexities can be estimated prior to actual processing; when the estimates exceed reasonable bounds, an approximation method such as stochastic simulation [Pearl 1988] can be used instead. Learning techniques have also been developed for systematic updating of the conditional probabilities in the network, so as to match empirical data (see Spiegelhalter and Lauritzen in Shachter [1990]).

## FUTURE PROSPECTS

Current research efforts aim at the following objectives.
-Inferring network structures from raw data [Pearl and Verma 1994].
-Replacing numerical assessments with qualitative, order-of-magnitude abstractions of probabilities and utilities [Goldszmidt 1995].
-Combining the representational advantages of probabilistic networks with the expressive power of firstorder logic [Glesner and Koller 1995].
