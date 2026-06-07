# From Networks to Narratives: Bayes Nets and the Problems of Argumentation 

Anita Keshmirian ${ }^{1,2,6}$, Rafael Fuchs ${ }^{2,3(\boxtimes)}$, Yuan Cao ${ }^{1,4}$, Stephan Hartmann ${ }^{2}$, and Ulrike Hahn ${ }^{2,5}$<br>${ }^{1}$ Fraunhofer Institute for Cognitive Systems (IKS), Munich, Germany anita.keshmirian@gmail.com<br>${ }^{2}$ Munich Center for Mathematical Philosophy (MCMP) - LMU, Munich, Germany Rafael.Fuchs@campus.lmu.de<br>${ }^{3}$ Graduate School of Systemic Neurosciences (GSN) - LMU, Munich, Germany<br>${ }^{4}$ Technical University of Munich, Munich, Germany<br>${ }^{5}$ Birkbeck University of London, London, UK<br>${ }^{6}$ Forward College, Berlin, Germany


#### Abstract

Bayesian Belief Networks (BBNs) are gaining traction in practical fields such as law and medicine. Given this growing relevance, it is imperative to make Bayesian methodologies accessible to professionals in these fields, many of whom might lack formal training in probability calculus. Argumentation offers a promising avenue to achieve this. It serves a dual purpose: (i) generating an explanation of the important reasoning steps that occur in Bayesian inference and (ii) exploring the structure of complex problems, which can help to elicit a BBN representation. Since Bayesian probabilistic inference also provides clear normative criteria for argument quality, there is a tight conceptual connection between the argumentative structure of a problem and its representation as a BBN. The primary challenge is representing the argumentative structure that renders BBN inference transparent to non-experts. Here, we examine algorithmic approaches to extract argument structures from BBNs. We critically review three algorithms - each distinguished by its unique methodology in extracting and evaluating arguments. We show why these algorithms still fall short when it comes to elucidating intricate features of BBNs, such as "explaining away" [44] or other complex interactions between variables. We conclude by diagnosing the core issue and offering a forward-looking suggestion for enhancing representation in future endeavors.


Keywords: Bayesian Network $\cdot$ Argument Quality $\cdot$ Explainable AI

[^0]
[^0]:    Supported by Deutsche Forschungsgemeinschaft (DFG) - Project number 455912038 and the Bavarian Ministry for Economic Affairs, Regional Development, and Energy as part of a project to support the thematic development of the Fraunhofer Institute for Cognitive Systems IKS.
    A. Keshmirian and R. Fuchs-Equally contributed to this work.

# 1 Introduction 

At the heart of scientific discovery and societal progress lies a fundamental concept: argumentation. It plays a pivotal role not only in the realm of science for explanation, justification, and the discovery of scientific laws but also serves as the backbone of effective communication and decision-making across disciplines, making it indispensable for a well-functioning democracy.

What constitutes a good argument? This enduring question has fascinated scholars for centuries, yielding a diverse array of studies and theories (e.g., [7, $15,23,34,41,43]$, with a comprehensive review available in [13].

In recent decades, Bayesian argumentation has emerged as a significant methodological breakthrough, offering explicit, normatively grounded criteria for evaluating arguments' quality and inferential soundness [14]. Its foundational principle in practical and scientific reasoning $[1,2]$ and its focus on minimizing the retention of incorrect beliefs [32] mark it as a notable advance in argumentation theory.

A particularly promising tool within the Bayesian framework is Bayesian Belief Networks (BBNs). These probabilistic models visualize complex relationships between variables and their dependencies while enabling sophisticated inference and learning capabilities about uncertain outcomes [21,31]. This investigation zeroes in on three innovative algorithmic strategies-Sevilla [38], Timmer et al. [40], and Keppens [19] - for extracting and scrutinizing arguments within BBNs. By dissecting these methods, we aim to illuminate their strengths and limitations, advocating for a paradigm shift towards more effective argumentation methodologies. Our critical analysis highlights the challenges inherent in managing the 'Explaining Away' effect and the nuanced treatment of 'Soft Evidence', underscoring the need for a sophisticated understanding of evidential relations within BBNs.

The paper is structured as follows: We begin by exploring the fundamentals of BBNs, spotlighting their role in modeling argumentation through the lens of The Spider network $[4,33]$, an example network designed to test decision-making in uncertain contexts using BBNs $[4,33]$.

We then critically compare three algorithmic approaches to argument extraction, exposing ongoing challenges and the need for clearer methodologies to tackle the nuanced dynamics of argument strength and validity in interconnected systems. Our analysis emphasizes the crucial role of transparency and accessibility in these methodologies, aiming to demystify the complexities for both scholars and practitioners.

## 2 The Bayesian Approach to Argumentation

This section gives a brief overview of the Bayesian approach to argumentation. Section 2.1 outlines the motivation and generality of the Bayesian approach, highlighting important advances in developing formal tools. Section 2.2 introduces Bayesian Belief Networks (BBNs) as a powerful graphical tool within the

Bayesian framework, which can significantly simplify computations and help visualize relations of conditional (in)dependence. Finally, in Sect. 2.3, we present important challenges when it comes to explaining the reasoning with BBNs to non-experts. Here, we primarily focus on the Explaining Away effect and why it is difficult to grasp intuitively. The effect can be further modified by the presence of Soft Evidence, which raises the probability of an observation without becoming fully certain.

# 2.1 The Bayesian Framework 

Revisiting our primary query, we ask: what defines a compelling argument? The existence of argumentative fallacies shows that subjective (psychological) persuasiveness and objective argument quality can come apart. Fallacies were studied extensively in arguments that psychologically seem persuasive, but as we examine them, we realize that they should not convince us $[15,45]$.

However, interestingly, arguments that share the same form with other fallacious arguments can still be good arguments in a different context [11]. For instance, compare the two arguments: "We haven't discovered any extraterrestrial life so far. Therefore, there is no extraterrestrial life in our universe." versus "After several checks, we couldn't discover any technical problems with this engine. Therefore, the engine works." Both arguments have an analogous form, known as argument from ignorance: given the absence of evidence to the contrary, we accept the hypothesis. However, while the former argument seems quite strong (at least to the extent that the premise can grant the conclusion), the latter is entirely reasonable, and in fact, we (have to) rely on this kind of reasoning all the time. Arguments from ignorance-one example of many informal argument schemes - have been discussed in the literature $[12,30]$.

This underscores that argument quality in realistic scenarios isn't solely based on syntactic form. Approaches to argumentation focusing only on syntactic form or deductive validity overlook critical elements of real-world argumentation, such as belief dynamics, graded uncertainty about propositions, and the interaction of relevant factors. Arguments in real-world scenarios are shaped by uncertain evidence, the audience's prior beliefs, and information source reliability [12,14]. Thus, a purely deductive approach may not sufficiently address these real-world complexities.

This brings us to the necessity of a more adaptive approach. A probabilistic approach, capable of addressing uncertainty and still containing deductive validity as a limiting case, emerges as promising. This approach, while retaining the foundations of logic, extends its capabilities. It enables a more in-depth evaluation of informal arguments, like in our example above, while aligning more with the multifaceted nature of real-world discourse. Furthermore, a probabilistic approach can help to unify the large plethora of argument schemes [42] that have been identified in studies of informal logic [10], showing how Bayesian reasoning can be used to explain how, when, and why diverse argument schemes actually work. There are also generalizations of standard Bayesian updating, such as Jeffrey conditionalization [18], which allows for updating credences based

on uncertain evidence ${ }^{1}$, and distance-minimization approaches [8,9], which also enable updating on more complex, non-propositional constraints.

In a nutshell, the strength of an argument is a question of relevance, expressed in terms of probability- or belief change. Argument quality is assessed by considering how one's belief in a target proposition would change upon learning the particular premise- an idea aptly encapsulated in the slogan of "argumentation as learning" [8].

Finally, knowledge bases that determine dependencies between propositions or variables of interest can be graphically represented as BBNs, which are directed acyclic graphs equipped with a probability distribution (more on this right below). BBNs are not just widely used in scientific contexts (e.g., [28]); they have found increasingly widespread adoption in software systems in domains as diverse as law, medicine, risk analysis, engineering, or strategic decision-making (e.g., $[3,24]$ ). BBNs are popular because they can provide relatively simple, compact representations of complex problems. Crucially, BBNs can not only be learned from data under certain assumptions $[16,37]$ but are formulated in terms of the variables that figure in the discourse and theories of these domains. This contrasts with low-level, data-driven 'black box' systems and makes BBNs key candidates for the development of explainable AI systems (XAI) (regarding the difficulties of developing explanations for 'black box' systems see, e.g., [36] and for discussion of the broader role of argumentation for XAI see, e.g., [39]). Now, let us look more closely at BBNs' features and non-experts' difficulties understanding their dynamics.

# 2.2 Bayesian Belief Networks (BBNs) 

BBNs provide a graphically compact and computationally powerful representation of complex problem domains (for an example, see Fig. 1). BBNs are graphs with multiple nodes (variables), directed edges (relationship between variables), and no cycles. In these Directed Acyclic Graphs (DAGs), directed edges connect parent nodes to their downstream child nodes with a conditional probability table for each Parent-Child relationship. This allows a compact, computationally efficient encoding of the joint probability distribution as a product of conditional probabilities $[22,25]$. This specific feature is called the Markov property. It states that each node is conditionally independent of its non-descendants (i.e., ancestors or unrelated nodes) in the network, given its parents.

BBNs were shown to mitigate some frequent biases in reasoning under uncertainty $[4,29]$. Having an intuitively understandable tool is highly beneficial in the domains mentioned above because experts (e.g., in law) are not necessarily experts in probability calculus, and therefore, the quality of decisions can be improved by providing adequate and understandable explanations of correct probabilistic inferences.

Let us consider the following example, known as the 'Spider' scenario [33]:

[^0]
[^0]:    1 Without raising the probability of the observed variable to total certainty.

Imagine you're an intelligence analyst on the trail of a dangerous foreign spy known as 'the Spider.' Initial evidence suggests that the Spider might be hiding in a facility located in a neutral country, represented by the binary variable $S p$. Your mission is to collect more information to determine if your team should infiltrate the facility to apprehend the Spider. You receive reports from agents Emerson and Quinn indicating the Spider's presence in the facility (binary variables $E, Q$ ), known for their reliability (low false-positive and false-negative rates). However, you soon encounter telephone logs that suggest Emerson and Quinn could collaborate with the Spider (binary variable $L$ ), though there's a chance these logs are forgeries created by the Spider's allies to mislead. To effectively navigate this situation, you must synthesize all these pieces of evidence, particularly considering the potential disinformation $L=l$ that could affect the credibility of positive reports from Emerson and Quinn, $E=e$, and $Q=q$.
![img-0.jpeg](img-0.jpeg)

Fig. 1. The Spider Network

While a BBN's graphical representation makes the overall independence structure and potential causal relations directly visible, other, more indirect reasoning features still challenge humans. In the following, we present two exemplary features of BBNs that are hard to understand: uncertain (soft) evidence, explaining away, and synergistic interaction effects.

# 2.3 Explaining BBNs: Important Challenges 

Now, we present two factors that complicate the explanation of BBNs: Explaining Away and Soft Evidence. We start with the latter and then show how it affects Explaining Away (our main focus), which we introduce next.

Soft Evidence. refers to cases in which an event is not learned or observed with certainty (i.e., probability 1), but its probability only increases. This can also happen if a leaf node is observed, but we are interested in its effect on further upstream nodes. Hence, we must calculate the effects of intermediate nodes, whose probability is raised by observing the respective leaf nodes, but it still remains below certainty. Within the Bayesian framework, we can accommodate soft evidence as a case of Jeffrey conditionalization [18], but for the untrained

user, it may be difficult to track how the probability flow propagates without further visualization or explanation.

Notably, soft evidence can also reverse the explaining-away effect, which we explain next.

Explaining Away. is a particular (and potentially tricky) effect that occurs in collider networks $X \rightarrow Z \leftarrow Y$. The collider network represents a structure where an effect has several possible, unconditionally independent causes ${ }^{2}$. Suppose the effect $Z$ is observed, and the probability of one of the possible causes increases (say $X$ ). This can lead to a decrease in the probability of the alternative explanation - it is "explained away" by the presence of the first cause. Pearl [31] provides an intuitive example of this effect: Suppose your car's failed (variable $Z$ ), and the possible causes are either a dead battery $(X)$ or a blocked fuel pump $(Y)$. If you learn that the battery is dead, this is a sufficient explanation of your observation regarding $Z$ - if the fuel pump was blocked as well, this would be a very unlucky coincidence, and hence, you may think in this kind of situation that $X$ "explains away" $Y$. On the other hand, there are cases with a similar structure where we might be intuitively inclined to think that learning about one cause doesn't give us any further information regarding the other. So, what is going on here?

The general answer is that we can observe this effect in collider networks with binary variables $X, Y, Z$ (with values $x, \neg x$, i.e., the negation), equipped with a probability distribution that satisfies the following inequality:

$$
P(z \mid x, y) \cdot P(z \mid \neg x, \neg y)<P(z \mid \neg x, y) \cdot P(z \mid x, \neg y)
$$

If this holds, then observing $Z$ makes $X$ and $Y$ dependent in the following sense:

- If the probabilities of $X=x$ and $Y=y$ increase due to $Z=z$, then $P(x \mid z)>$ $P(x)$ and $P(y \mid z)>P(y)$.
- If either $Y=y$ or $X=x$ is observed in addition to $Z=z$, then $P(x \mid z, y) \leq$ $P(x \mid z)$ or (respectively) $P(y \mid z, x) \leq P(y \mid z)$.

The DAG by itself does not indicate whether this holds, which means that the user needs to understand the probabilistic relations or the graphical representation (or AI-generated verbal explanation) needs to be adequately extended to include this information understandably. For humans, explaining away often seems to be challenging to grasp. Several empirical studies have indicated subjects' tendency to under-update or contradict the prescription of explaining-away-reasoning (e.g., [35]). Thus, it is an important desideratum for explanatory algorithms to make this relation apparent to the user and, ideally, provide an explanation that fits the context of the application.

[^0]
[^0]:    ${ }^{2}$ Here, we are explicitly referring to uncoupled colliders, where there is no link between $X$ and $Y$.

Finally, as mentioned above, soft evidence can reverse 'explaining away' as follows. In a collider $X \rightarrow Z \leftarrow Y$, if there is soft evidence for $Z$, i.e., $P(Z=z)$ increases, then $X$ can confirm $Y$. This makes the intuitive understanding even more difficult because the BBN does not depict the probability flow. Hence, we need the relevant background knowledge to draw the correct inference from observing a BBN and facts about changing probabilities. An explainable algorithm thus has to provide the relevant background information and make it salient in the context of the given application scenario.

# 3 Algorithmic Approaches to Bayesian Argumentation 

This section reviews the relation between argument diagrams (ADs) and BBNs and three extant approaches to AD extraction from BBNs. Specifically, in Sect.3.1, we analyze general conceptual questions about the relation between ADs and BBNs, as well as general desiderata for explanatory or auxiliary ADs. In Sect.3.2, we present three extant approaches to argument extraction: the factor graphs by Sevilla [38], the support construction by Timmer [40], and the argument-diagram-extraction by Keppens [19]. In Sect.3.3, these algorithms are evaluated using the Spider example, which we introduced previously (Fig. 1). We find that these algorithms illuminate the connection between argument diagrams and BBNs, but ultimately, the main challenges identified in Sect. 2.3 remain unresolved. Further work combining different approaches and extended psychological research will be needed to develop a more comprehensive and theoretically wellfounded approach to explanatory reasoning with BBNs.

### 3.1 The Relation Between Argument Diagrams and Bayesian Networks

An argumentative problem-solving approach often helps to increase the understanding of complex problems. This also comes out in the social procedure of the BARD project [29], designed for the elicitation of BBN representations via group deliberation. We have already seen that BBNs (as mathematical objects) contain features that are intuitively challenging for laypeople, but when problems are posed within a context of practical argumentation, correct reasoning and intuitive understanding can be improved [17]. The interaction between inference in BBNs and argument diagramming techniques becomes interesting at this point. Experts in practical domains, e.g., in law, tend to understand argument diagrams better than causal models or BBNs [19,40]. At the same time, inference with BBNs provides a normative standard for correct reasoning under uncertainty. Therefore, BBNs and more informal argument diagramming techniques can exhibit synergies that benefit the general project of widening access to Bayesian reasoning resources.

Generally, the information exchange between BBNs and Argument diagrams (ADs) can go in both directions:

1. Elicitation (from ADs to BBNs): an argumentative exchange about a target domain or problem (represented as an AD) is mapped to a BBN. This requires an unambiguous mapping from input ADs and additional technical constraints (accounting for contextual and pragmatic factors in conversation) to BBNs.
2. Explanation (from BBNs to ADs): probabilistic inference in a BBN is transferred to an AD, which can then also serve as the basis for verbal explanations and be supplemented with quantitative impact measures (how much each premise or piece of evidence impacts the set of target variables or conclusions).

The literature on algorithmic argument generation and explainable AI has generated some approaches to algorithmic argument extraction from BBNs. In the following, we review frameworks by Sevilla 2021 [38], Timmer [40], and Keppens [19].

# 3.2 Introducing Three Extant Algorithms 

Sevilla (2021). This algorithm, developed by Jaime Sevilla [38], finds an approach to select a list of relevant and independent arguments from a BBN, given evidence nodes and a target node. The strength of each argument is computed by the logarithmic odds ratio, calculated after implementing the approximate message-passing algorithm to ascertain the relatively important arguments. The algorithm generates a factor graph [22] from a BBN with the nodes for all variables in the model and the factors representing the conditional probability tables. The nodes connected to the factors are part of the conditional probabilities. To prepare the message passing calculation, each observation node is initialized to a lopsided factor (only the known state with probability one and others with probability 0 ). In contrast, the remaining nodes are initialized to constant factors (under uniform distribution). After obtaining the factor graph, the messagepassing algorithm could estimate all message flows. Effects and strength of argument: An argument is indicated as a directed acyclic graph over a factor graph consisting of nodes and factors from observation to the target. The effect of each inference step in an argument defines how a preceding node affects the inferior node. The factor is multiplied by all premises as the message-passing algorithm and then divided by the factor itself to distinguish between the information obtained from the updates $\Delta$ and the information inherently embedded within the conditional probability table $\phi$.

The effect of a complete argument is calculated by recursively utilizing the Step Effect. The effects of all the parents of the factor are multiplied together to inherit the effect of an argument. The strength of an argument is introduced to compare the importance of all the arguments. It is the logarithmic odds of the argument that support the outcome. This measure of strength is a real-valued quantity, where its sign indicates whether the argument supports or opposes the outcome, and its magnitude quantifies the strength of the argument.

Argument independence: to decide whether simple arguments should be combined into one complex argument indicates to determine whether they are independent. More ordinarily, a list of arguments is independent if the effect of the union of arguments is equal to the product of the effects of simple arguments. To adjust the theory to reality, a list of arguments is approximately independent if the distance of effects is within a certain threshold.

The final output presented to the user is a text generated from basic blocks which take premises (evidence nodes) and a query node as input and give an evaluation of how much the given set of premises supports the probandum, with the logarithmic odds as a measure of argument strength (supplemented by a qualifier tag, such as 'weak inference' or 'strong inference').

Timmer (2017) focuses on the construction of support graphs from BBNs. Support graphs are trees with a given query node as their root, and the descendants on each branching layer consist of all the variables that directly affect their parent. This tree preserves the conditional independence structure, which entails that all Markov-equivalent DAGs map onto the same support graph. This approach promises that a tree, in which the conclusion is at the top, and the supporting evidence (premises) are on the layers below, is easier to interpret than a BBN, in which we sometimes have to reason 'backward' (e.g., from effects to possible causes, as in the explaining away effect). Due to the close connection between support graphs and BBNs, Timmer's construction promises to be a good candidate for elicitation, i.e., a stepwise translation of (informal) argument diagrams into BBNs. ${ }^{3}$

The variables are mapped from the BBN to the new structure to construct a support graph with the query node (conclusion) as a root. In doing so, the same variables occur multiple times on the tree. Therefore, to avoid the inclusion of false independencies and (in the extreme case) circular reasoning, a set of forbidden nodes is defined, whose purpose is to exclude these problematic instances. The set of descendants for each given node in the tree is then defined as the Markov blanket of the corresponding node in the BBN minus the set of forbidden variables. The algorithm terminates when no further nodes are added. Formally, the set $\mathcal{F}\left(V_{i}\right)$ of forbidden nodes for variable $V_{i}$ is defined as follows.

- $\mathcal{F}\left(V_{i}\right)=\left\{V_{i}\right\}$, if $V_{i}$ is the query node (root of the SG)
- Otherwise, if $V_{j}$ is a parent of $V_{i}$ in the SG:
- $\mathcal{F}\left(V_{i}\right)=\mathcal{F}\left(V_{j}\right) \cup\left\{V_{i}\right\}$, if $V_{i}$ is a parent of $V_{j}$ in the BBN
- $\mathcal{F}\left(V_{i}\right)=\mathcal{F}\left(V_{j}\right) \cup\left\{V_{i}\right\} \cup \operatorname{Par}\left(V_{i}\right)$, if $V_{i}$ is a child of $V_{j}$ in the BBN
- $\mathcal{F}\left(V_{i}\right)=\mathcal{F}\left(V_{j}\right) \cup\left\{V_{i}\right\} \cup \mathbf{C}_{i, j}$, otherwise, where $\mathbf{C}_{i, j}$ are the common children of $V_{i}, V_{j}$ in the BBN.

[^0]
[^0]:    ${ }^{3}$ In the interest of space, we cannot cover this aspect here, but we note that it is an interesting direction for future research.

Keppens (2013) considers arguments as consisting of observed variables. The input of the algorithm is a BBN, together with a query node (probandum), denoted as $H=h$, and a set of observations $\mathbf{O}=\left\{O_{1}=o_{1}, \ldots, O_{n}=o_{n}\right\}$ (the evidence). Given this initial set, the algorithm finds all nodes on a path between (i) one of the variables corresponding to observations and (ii) the probandum in the BBN. For these intermediate nodes, the algorithm calculates the most probable value (defined as $\arg \max _{v \in \operatorname{Im}(V)} P(v \mid \mathbf{O}, h)$ ), given the values of probandum and observations. Finally, the set of edges in Keppens' AD corresponds precisely to the set of edges of the BBN, but the edges in the baseline AD are inverted. This is due to the intended application to forensic reasoning, where we must standardly reason backward, from evidence (observations) to the most likely explanatory hypothesis (probandum).

Furthermore, Keppens' algorithm has additional features that potentially make his AD formalism more expressive than Timmer's. In particular, we point out the distinction between convergent and linked arguments. Convergent and linked arguments are arguments that share the same conclusion. Convergent arguments have independent sets of premises, while in linked arguments, there is dependence among the premises. Keppens' proposed criterion to distinguish between convergent and linked arguments is whether the variables corresponding to premises are d-separated by the conclusion in the BBN (if yes, the arguments are convergent; otherwise, they are linked). In the AD, these can be represented via a single hyper-edge ${ }^{4}$ that connects a set of linked (dependent) arguments to a single claim or separate edges pointing from individual convergent (independent) arguments to one conclusion.

The final step is decorating the inference links in the resulting AD with labels that indicate probative force. These are verbal descriptions ('strong', 'weak', 'certain' etc.) based on intervals of likelihood ratios.

# 3.3 Evaluating the Algorithms: Example Networks 

Let us examine how well these algorithms connect to BBNs, focusing on explanation (noting that exploring the potential of support graphs for elicitation remains for future work). We consider an example case, "The Spider" [4,33], to evaluate how well the algorithms fare regarding explanation. This example stands out for its prior demonstrations of challenging human and artificial agents with its nuanced scenario, often revealing areas of sub-optimal reasoning.

Sevilla: Sevilla's algorithm yields the output shown in Fig. 2. The algorithm can quantify individual support relations and provide an overall evaluation (not shown here). Still, it is not designed to show precisely how arguments interact. In particular, the dynamics related to explaining away do not appear, and the simple list of 'strength values' might look rather confusing to an untrained user. Furthermore, the algorithm produces artifacts that output irrelevant conclusions (such as the 'certain inference' in the last two paragraphs).

[^0]
[^0]:    ${ }^{4}$ a hyper-edge connects a set of nodes to another node or set of nodes.

```
We have observed that Sawyer is True.
That Sawyer is True is evidence that Spider is True (strong inference).
We have observed that Emersons is False.
That Emersons is False is evidence that Spider is True (weak inference).
We have observed that Quinns is False.
That Quinns is False is evidence that Spider is True (weak inference).
We have observed that Quinns is False.
That Quinns is False is evidence that Both is False or Both is True (certain inference).
That Both is False or Both is True is evidence that Spider is False or Spider is True (certain inference).
We have observed that Emersons is False.
That Emersons is False is evidence that Both is False or Both is True (certain inference).
That Both is False or Both is True is evidence that Spider is False or Spider is True (certain inference).
```

Fig. 2. Argument obtained from adding Emerson's and Quinn's reports as premises for the conclusion that the Spider is in the facility.

Timmer: Timmer's algorithm yields the output shown in Fig. 3. These support graphs are not particularly informative regarding the interaction between the evidence pieces. All of them are in the Markov blanket of $S p$. Therefore, all are directly relevant to the conclusion-but from the graph alone, we don't know how. In particular, the explaining away effect between $S p$ and $L$ that is triggered by increasing $P(S p=$ true $)$ via $W=$ true is not visible in the graph. Similarly, the support graph doesn't show how the explaining away relation changes under soft evidence: recall that soft evidence can reverse the explaining away effect. However, neither of these effects is visible in the support graph since its structure is always the same. Since the support graph is limited in this way, also a verbal explanation that is based only on information provided by the support graph (i.e., 'translating' the support graph into a textual explanation via some fixed scheme) cannot make these effects visible either-precisely because the relevant information is missing. Hence, the support graph does not add much explanatory power to the BBNs, except for clarifying which variables directly affect the target node.
![img-1.jpeg](img-1.jpeg)

Fig. 3. Full support graph with observed reports by Winter and Alpha in the Spider Network.

Keppens: The core structure of Keppens' argument diagram in this scenario looks as follows:

![img-2.jpeg](img-2.jpeg)

Fig. 4. Argument Diagram extracted with Keppens' algorithm.

In this argument diagram, the differentiation looks better than in Timmer's case because $L=$ true and $S p=$ true are depicted as alternative explanations of evidence pieces $E=$ false and $Q=$ false (represented as a bidirectional edge between nodes $L$ and $S p$ ). $E=$ false and $Q=$ false are linked arguments. Therefore, they are connected via a hyperedge to both alternative conclusions.

The limitations in Keppens' case primarily relate to the aggregation and the assignment of labels of probative force. When assessing how a specific piece of evidence influences the probability of the target node and when comparing the situation before and after observing that evidence, it is crucial to understand how the probative force of the total (aggregated) argument shifts concerning the target node. For example, if we start with the reports from Emerson and Quinn, their joint probative force for Spider being in the facility may be "strong." So, in the next step, we need to check how this assignment changes when we add Winter's (and other witnesses') reports. In the best case, the label changes (e.g., from "strong" to "very strong"), which, if not numerically precise, gives the user at least a qualitative understanding of how the respective variables in the BBN interact. However, the probability shift happens within the interval in the worst case. Thus, the final label may still say "strong" even though there was a shift from the lower bound of "strong" to the higher bound (i.e., almost "very strong"). Thus, it is still a non-trivial question of how this can be represented in an argument diagram without numerical values. A complete solution must include numerical values and verbal interpretations adequate for context.

Another limitation concerns the representation of linked arguments. In a collider $X \rightarrow Z \leftarrow Y$, an argument based on $X$ and $Z$ to the conclusion $Y$ is linked (the premises are not d-separated by the conclusion $Y$ ), but their roles are fundamentally different. While we can remove premise $X$, and still argue for/against some value of $Y$ only with $Z$, the reverse is impossible since $X$ and $Y$ are unconditionally independent. Thus, the classification of linked arguments must be refined for more advanced applications and faithful representation of BN relations in an explanatory argument diagram.

These results indicate that simple, static displays of AD still have limited explanatory power regarding dynamic interactions between evidence variables since probabilistic information flows back and forth in the BBN, as exemplified in the previous section. However, as illustrated by Keppens' none of these prob-

lems seem unsolvable. Thus, we are optimistic that future work (taking Keppens' algorithm as a starting point and refining it further) can solve at least a good portion of the persisting challenges. As Sevilla used, additional text generation seems indispensable to generate more complete explanations. However, the outputs produced by Sevilla's algorithm show that significant challenges still exist to come closer to a comprehensive solution.

Alternative methods for explaining Bayesian networks have also been proposed, for example, interactive graphical explanations that use color codings and node- and edge sizes to indicate interactions between variables (see, e.g., [20]). Suppose the graphical display of argument structures extracted from Bayesian networks can be useful. In that case, such an interactive approach might be better-but it is unclear whether this would have any value over just using a more colorful and interactive version of the Bayes net itself. However, the generation of text from argumentative seems promising because it goes beyond the graphical modality and adds a new dimension to help the user understand from a different perspective. Text can combine a linear path of reasoning with changing interactions, feedback, and back-and-forth that occurs as more information is introduced. This can be done on a high level (thus being able to handle large networks without getting lost) or in a more detailed way. So far, text-based algorithms are still undeveloped (no new recent approaches were presented besides Sevilla's), and thus, we believe that pushing this line of research will be fruitful in the future.

# 4 Limitation 

In this study, we selectively examined three diverse methodologies, acknowledging the existence of additional approaches that could further enrich our analysis. This deliberate choice allowed us to showcase a range of distinctly different methods, setting a foundation for comprehensively exploring this field. While our investigation focused on a carefully chosen example to illuminate specific challenges, it opens the door to examining other networks, particularly larger ones, in future studies. Our critical review of current algorithms lays the groundwork for future research to build upon, presenting an exciting opportunity to develop innovative solutions to the challenges we have highlighted.

This paper represents a significant stride towards refining our approach to Bayesian Belief Networks (BBNs) and their applications. At its heart, the comparison of three distinct approaches serves not only to highlight the current state of the art but also to spark a deeper inquiry into methodological enhancements. Notably, while our analysis suggests that translating a BBN into an argument structure could potentially deepen our understanding of probabilistic inferences, it also points to an intriguing area for future empirical investigation. This prospect underscores the forward-looking nature of our work, inviting further research to validate these claims and continue advancing the field in novel and meaningful directions. In non-written argumentation paradigms mentioned in the paper, we need to note that the cognitive capacity of human end

users is inherently limited, which presents a notable challenge to the scalability of graphical approaches, as their effectiveness might diminish when applied to larger and more complex models. Future research should consider a fundamental shift in approach, aligning more closely with the intricacies of argumentation and Bayesian reasoning. This would ensure that the powerful potential of BBNs can be fully harnessed in diverse real-world applications.

# 5 Conclusion 

In our exploration of algorithmic methods to extract and evaluate arguments from Bayesian Belief Networks (BBNs), we identified persistent challenges, particularly concerning the intricate features of BBNs. The difficulties in capturing nuances like interdependence underscore the complexities inherent to these probabilistic models. While these algorithms provide valuable insights and bring us closer to making Bayesian methodologies more comprehensible, our analysis indicates that more innovative approaches are needed. A holistic understanding of the argumentative structure is crucial for transparent BBN inference, especially for those without expert knowledge in probability calculus. As BBNs gain prominence in decision-making across disciplines, refining these algorithms is not just an academic endeavor but a practical necessity.

Acknowledgement. We thank the Deutsche Forschungsgemeinschaft (DFG) and the Fraunhofer Institute for Cognitive Systems IKS for supporting our research. We thank Dr. Narges Ahmidi and Alireza Zamanian for their insightful suggestions and valuable feedback on this paper.
