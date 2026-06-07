# Decision Making under Uncertainty through Extending 

## Influence Diagrams with Interval-valued Parameters

Abstract Influence Diagrams (IDs) are one of the most commonly used graphical and mathematical decision models for reasoning under uncertainty. In conventional IDs, both probabilities representing beliefs and utilities representing preferences of decision makers are precise point-valued parameters. However, it is usually difficult or even impossible to directly provide such parameters. In this paper, we extend conventional IDs to allow IDs with interval-valued parameters (IIDs), and develop a counterpart method of Copper's evaluation method to evaluate IIDs. IIDs avoid the difficulties attached to the specification of precise parameters and provide the capability to model decision making processes in a situation that the precise parameters cannot be specified. The counterpart method to Copper's evaluation method reduces the evaluation of IIDs into inference problems of IBNs. An algorithm based on the approximate inference of IBNs is proposed, extensive experiments are conducted. The experimental results indicate that the proposed algorithm can find the optimal strategies effectively in IIDs, and the interval-valued expected utilities obtained by proposed algorithm are contained in those obtained by exact evaluating algorithms.

Keywords: Decision making; Influence diagrams; Bayesian networks; Interval-valued parameters.

# 1 Introduction 

Influence diagrams (IDs) (Howard \& Matheson 1984) are one of the most common graphical and mathematical decision models used for reasoning under uncertainty. Because IDs represent and model the relationships between decisions, uncertainties and preferences of decision makers, and they can be evaluated to reveal optimal strategies for decision making situations, IDs have become an important area for research and have been widely used in various applications, such as risk analysis (Liu et al. 2010), disease diagnosis (De Castro et al. 2011), multi-criteria decision-making (Sedki \& Delcroix 2012), and recommender systems (Antonio et al. 2013).

An ID has a graphical component and a numerical component. The graphical component is a directed acyclic graph consisting of chance, decision and value nodes. These nodes are connected by directed arcs that represent influences amongst nodes. The numerical component, i.e. parameters of IDs, consists of probability distributions and utility functions associated with chance nodes and value nodes respectively. They represent quantifiable beliefs on the uncertainties and preference of a decision maker. In a conventional ID, parameters are precise point-valued probabilities and utility values. Those parameters are typically obtained from measurement, or expert judgment or partially reliable data sources (Cabañas et al. 2016). However, in many cases, it is usually difficult to measure or for experts to provide precise point-valued parameters (Hu et al., 2012), especially in the situation that the values of the variables themselves being imprecise. Therefore, it is desirable to extend conventional IDs for handling situations where values of variables or parameters are imprecise.

Extending conventional IDs with the capability to deal with interval values as parameters can help us to model and evaluate decision-making processes in the situation that the values of variables exist within a range. However, it is not a straightforward task. The first challenge is the extension of the probability theory that is the foundation of IDs. In situations that the values of variables are imprecise, we need considerate how to represent quantifiable beliefs and preferences with uncertainties for decision makers. Adopting probability intervals that are only

composed of pairs of values between 0 and 1 (Cano \& Moral 2002; Walley 1991) neglects theoretical probability semantics. The computation of the probability intervals themselves cannot be made with a theoretical basis, and the propagation of probability intervals during inferences cannot be guaranteed to be sound theoretically. Adopting interval probability instead of probability intervals can describe the semantics of imprecise probabilities and uncertain knowledge (Gilbert et al. 2003; Tanaka et al. 2004), but conventional concepts and definitions of interval probabilities, such as the intuitive concept and the canonical concept (Tanaka et al. 2004; Weichselberger 2000; Weichselberger \& Augustin 2003), do not satisfy the conditional probability and multiplication rules for many common scenarios, thus cannot be used to represent and infer probabilistic causal relationships amongst interval-valued variables directly. However, the bound-limited weak conditional interval probabilities proposed by Liu \& Yue (2011) satisfy the multiplication rule for joint probabilities and can be interpreted as interval probabilities. Therefore, beliefs regarding uncertainties for a decision maker can be represented quantifiably by bound-limited weak conditional interval probabilities. In this paper, we extend conventional IDs as influence diagrams with interval-valued parameters (IIDs), in which the probabilities associated with chance nodes are expressed via bound-limited weak conditional interval probabilities and the utilities associated with value nodes are expressed via interval values. This method avoids the difficulties attached to the specification of precise parameters, and provides the capability for modelling decision making processes in the situation where precise parameters cannot be specified, due to the values of the variables themselves being imprecise. In general, it is more likely for decision makers to specify interval-valued parameters than to provide point-valued parameters, therefore our approach extends the application domains for influence diagrams.

The second challenge to extend conventional IDs to the situation that values of variables are imprecise is the evaluation of IIDs, i.e. how to select a strategy with a maximal expected utility. The computation of expected utilities integrates the inference of probabilities into decisional computations. In IIDs, how to integrate the

inference of bound-limited weak conditional interval probabilities into decisional computations with interval-valued utilities is a crucial issue. As with evaluating conventional IDs, it is impracticable to evaluate each possible strategy directly and compare each expected utility, because the number of strategies grows exponentially in respect of the number of actions to be taken. Although researchers have developed a number of methods to evaluate conventional IDs, but these methods cannot be directly used to evaluate IIDs, thus there is a need to develop new evaluation methods for IIDs.

In this paper, we propose an indirect method to evaluate IIDs. The main idea is to transform an IID into a Bayesian networks with interval-valued probabilities (IBNs), and then select the strategy with the maximal interval-valued expected utility based on the inference of IBNs. Furthermore, we develop an algorithm and conduct extensive experiments in synthetic data sets and a real world case.

Our framework is novel and original in a way that the probabilities associated with chance nodes in IIDs are expressed via bound-limited weak conditional interval probabilities, and the evaluation of our IIDs is an indirect method based on the inference of IBNs. The bound-limited weak conditional interval probabilities satisfy the multiplication rule for joint probabilities and can be interpreted as interval probabilities. The indirect evaluation method avoids the computation on the cross product of all problem parameters, thus the efficiency of evaluation can be improved.

The main contributions of this study can be summarised as follows:

- The conventional IDs have been extended to as IIDs. This extension avoids the difficulties attached to the specification of precise parameters and provides the capability for modelling decision making processes in situations that the precise parameters are not available;
- An indirect evaluation method has been developed for IIDs. The developed method is based on the interferences of IBNs. The proposed approach enables one to use exact or approximate inference algorithms of IBNs to efficiently evaluate IIDs;
- An algorithm for evaluating IIDs is presented and extensive experiments are

conducted. To verify the feasibility and robustness of our approach, the experimental results of our methods are compared with those obtained by other methods. We also apply our methods to a real life case.

The remainder of this paper is organised as follows: Section 2 reviews of related literatures. Section 3 introduces the bound-limited weak conditional interval probabilities. Section 4 presents the IIDs. Section 5 introduces a method to evaluate IIDs. The experiments are presented in Section 6. Finally, Section 7 presents conclusions.

# 2 Related Work 

Related literatures can be grouped into three categories: probability theory, extensions of conventional IDs and the methods for evaluating IDs.

### 2.1 Probability theory

Probability theory is the foundation to BNs and IDs. Interval probability theory has been accepted as a formal method to represent uncertainties in an imprecise manner by typical interval values. The intuitive concept and the canonical concept are two concept proposed by Weichselberger \& Augustin (2003). The intuitive concept is used as the generalization of conditional probabilities, but it does not satisfy the multiplication rule for joint probability distribution. The canonical concept satisfied the multiplication rule, but it can not be interpreted as an interval probability in usual scenes. Liu \& Yue (2011) defined the bound-limited weak conditional interval probabilities that satisfy the multiplication rule for joint probabilities and can be interpreted as interval probabilities in the usual scene, so these interval probabilities can be used to represent and infer causal relationships amongst interval-valued variables. Liu \& Yue (2011) also gave a method for learning the BN structure from interval data and gave a Gibbs sampling algorithm for approximate inferences with interval probability parameters. This algorithm can effectively compute the bound-limited weak conditional interval probabilities for given the values of related nodes.

### 2.2 The extension of conventional IDs

In order to model more complex decision issues, the IDs proposed by Howard \& Matheson (1984) have been extended in many different ways. For example, Lauritzen \& Nilsson (2001) proposed limited memory IDs that relax the standard assumption in an ID of "no forgetting"; Garcia \& Sabbadin (2008) presented possibilistic influence diagrams (PIDs), which allows to model sequential decision making under uncertainty, when only ordinal data on transitions likelihood or preferences are available. Cobb \& Shenoy (2008) introduced MTE (Mixtures of truncated exponentials) IDs, in which all probability distributions and the joint utility function are represented by MTE potentials, and decision nodes are assumed to have discrete state spaces, thus MTE IDs can represent decision problems without restrictions on the relationships between continuous and discrete chance variables, without limitations on the distributions of continuous chance variables, and without limitations on the nature of utility functions. Zhou et al. (2013) presented game theory-based IDs (GIDs) by incorporating game theory into IDs. GIDs can model decision-making process in interactive scenarios because the choices of strategies made by other decision makers are also taken into account. In these studies, IDs have point-valued parameters.

Some attempts have been made to avoid difficulties attached to the specification of precise beliefs and preferences, for example, Guezguez et al. (2009) suggested that it is easier to express uncertainty qualitatively by ranking different states of the world, and that it may be more flexible to provide a preferential relation between different consequences rather than exact numerical values. Therefore, they extended conventional IDs as qualitative possibilistic IDs in which beliefs are quantified qualitatively via possibility distributions, and utilities are represented by a preferential relation between different consequences. Mateou et al. (2005) proposed Fuzzy influence diagrams (FIDs) that express the possible values of each node as fuzzy sets rather than probabilities, thus the dependence on probabilistic contribution is eliminated. Huang et al. (2007) extended conventional IDs as rough set-based IDs in which causal relationships amongst the nodes were expressed using rough sets. Hu et al. (2012) converted intervals of probabilities assigned by a group of experts into the point-valued probabilities to quantify the beliefs of decision makers. Breeze \& Fertig

(1990) developed interval influence diagrams where lower bounds of probability intervals are stored at each node. This method preserves both the probabilistic soundness and the graphical nature of conventional IDs. But the probability bounds calculated by this method quickly degrade during the propagation, thus resulting in the assignment of too wide probability intervals and jeopardizing the normative character of their decisions (Ramoni 1995). Ramoni (1995) proposed ignorant influence diagrams that are able to reason on the basis of incomplete information, and to incrementally refine the accuracy of their decisions as more information becomes available. Cabañas et al. (2016) extended IDs to intervals by replacing the probability potentials (PPs) and utility potentials (UPs), with an equal number of interval-valued probability potentials (IPPs) and interval-valued utility potentials (IUPs) defined over the same domains. The corresponding models are called IIDs. In the study of Cabañas et al (2016), an IID is equivalent to a collection of precise IDs, all with the same graph and set of variables, with PPs and UPs taking their values from the extensions of the IPPs and IUPs of the IID.

# 2.3 The methods for evaluating IDs 

Given an ID, a strategy defines the actions taken at each decision node, given the values of nodes available at that moment. Each strategy has a corresponding expected utility (De Campos \& Ji 2008) and the strategy with the maximal expected utility can be the optimal one. Evaluating an ID means to select a strategy with the maximal expected utility.

To evaluate conventional IDs, the direct and indirect methods have been proposed. The direct methods, such as arc reversal and variable elimination (Shachter 1986), compute directly on IDs, while the indirect methods transform IDs into other models, such as BNs (Cooper 1988; Shachter \& Poet, 1992; Zhang 1998) or decision trees (Howard \& Matheson 1984), and then the computations are carried out on transformed models. The use of decision trees for evaluation IDs does not use conditional independencies and direct evaluation requires a lot of probabilistic calculations which justify the great development of indirect methods initiated by Cooper (1988) for the particular case of influence diagrams with a unique value node

(Guezguez et al. 2009). The key idea of Cooper's method is to transform decision and value nodes of an ID into chance nodes to obtain a BN (Heckerman \& Wellman 1995), and then reduce the ID evaluation problem into a BN inference one.

On extended IDs, Lauritzen \& Nilsson (2001) selected strategies by passing messages in suitable junction trees. Garcia \& Sabbadin (2008) proposed a dedicated variable elimination algorithm for solving PID. MTE IDs are solved by variable elimination using a fusion algorithm (Cobb \& Shenoy 2008). GIDs are evaluated by genetic algorithm-based methods (Zhou et al. 2013). Guezguez et al. (2009) transformed qualitative possibilistic IDs into qualitative possibilistic networks (Ben Amor et al. 2003) based on possibility theory and made inference in these qualitative possibilistic networks. Mateou et al. (2005) employed fuzzy reasoning instead of probabilities, thus the need to calculate the cross product of all problem parameters is eliminated by using fuzzy casual relationships. Huang et al. (2007) evaluated rough set-based IDs based on rough sets theory. Breese \& Fertig (1990), Ramoni (1995) and Cabañas et al. (2016) evaluated their interval IDs based on arc reversal and variable elimination. In the framework of Cabañas et al., the interval dominance in the imprecise-probability jargon is adopted as the decision criterion, which rejects all the decisions leading to certainly sub-optimal strategies. Both reversing an arc and deleting a node are based on probabilities, so they must spent much time to calculate the cross product of all problem parameters.

Although existing researches (Breese \& Fertig 1990; Ramoni 1995; Cabañas et al. 2016) have extended conventional IDs to intervals, the study in this paper is different from the existing researches in two aspects. First of all, the probability theory used in this paper is the bound-limited weak conditional interval probabilities which have not been used in existing researches. Then, the evaluation method for IIDs in this study is an indirect method that reduces the IIDs evaluation problem into an IBN inference one, but the evaluation methods for IIDs in existing researches are direct methods that are based on arc reversal and variable elimination.

# 3 The Bound-limited Weak Conditional Interval Probabilities 

Let the universe of discourse $\Re$ be a continuous one-dimensional space. An interval value $\tilde{a}$ is defined as: $\tilde{a}=\left[a^{L}, a^{U}\right]=\left\{x \mid a^{L} \leq x \leq a^{U}, a^{L}, a^{U} \in \Re\right\}$, where $a^{L}$ and $a^{U}$ are the lower and upper bounds of $\tilde{a}$ respectively. Especially, $\tilde{a}$ degenerates as a real value if $a^{L}=a^{U}$. Let $A$ and $B$ be random variable with interval-valued sample data, $L(B)$ and $U(B)$ be the lower and upper probabilities respectively, $[L(A / B), U(A / B)]$ be the conditional interval probability of $A$ with respect to $B$, $[E L(A / B), E U(A / B)]$ be the extended weak conditional interval probability, $[C L(A / B), C U(A / B)]$ be the contracted conditional interval probability, and $[B L(A / B), B U(A / B)]$ be the bound-limited weak conditional interval probability. Liu \& Yue (2011) gave the definitions of these probabilities as follows:

$$
L(B)=\sum_{x_{i} \leq B} P\left(x_{i}\right), U(B)=\sum_{x_{i} \leq B \neq \phi} P\left(x_{i}\right), \text { where } x_{i} \text { is a sample in the sample space } \Omega
$$

$P\left(x_{i}\right)$ be the point-valued probability of $x_{i} ; L(A / B)=\frac{L(A B)}{L(A B)+U(B-A B)}$,
$U(A / B)=\frac{U(A B)}{U(A B)+L(B-A B)}$, where $L(A B)$ and $U(A B)$ are respectively the lower and upper probability that event $A$ and $B$ occur simultaneously, $L(B-A B)$ and $U(B-A B)$ are respectively the lower and upper probability that event $B$ occurs but $A$ and $B$ do not occur simultaneously; $E L(A / B)=\frac{L(A B)}{U(B)}, \quad E U(A / B)=\frac{U(A B)}{L(B)}$, $C L(A / B)=\frac{L(A B)}{L(B)}, C U(A / B)=\frac{U(A B)}{U(B)}$.

$$
L(A / B) \text { and } U(A / B) \text { do not satisfy the multiplication rule for joint probability }
$$

distributions, and when $A$ and $B$ are mutually independent, $L(A) \neq E L(A / B)$, $L(A) \neq C L(A / B)$ and $U(A) \neq E U(A / B), U(A) \neq C U(A / B)$. So, it is difficult to

make inferences on a BN based on the interval probabilities given above.
$B L(A / B)$ and $B U(A / B)$ are defined according to various cases of the relationships among $L(A), \quad U(A), L(A / B)$ and $U(A / B)$ :
(1) If $L(A) \leq L(A / B) \leq U(A / B) \leq U(A)$, then

$$
B L(A / B)=\max \{E L(A / B), L(A)\}, B U(A / B)=\min \{E U(A / B), U(A)\}
$$

(2) If $L(A / B) \leq L(A) \leq U(A) \leq U(A / B)$, then

$$
B L(A / B)=\min \{C L(A / B), L(A)\}, B U(A / B)=\max \{C U(A / B), U(A)\}
$$

(3) If $L(A / B) \leq L(A) \leq U(A / B) \leq U(A)$, then

$$
B L(A / B)=\min \{C L(A / B), L(A)\}, B U(A / B)=\min \{E U(A / B), U(A)\}
$$

(4) If $L(A) \leq L(A / B) \leq U(A) \leq U(A / B)$, then

$$
B L(A / B)=\max \{E L(A / B), L(A)\}, B U(A / B)=\max \{C U(A / B), U(A)\}
$$

(5) If $L(A) \leq U(A) \leq L(A / B) \leq U(A / B)$, then

$$
B L(A / B)=\max \{E L(A / B), U(A)\}, B U(A / B)=\min \{E U(A / B), 1\}
$$

(6) If $L(A / B) \leq U(A / B) \leq L(A) \leq U(A)$, then

$$
B L(A / B)=E L(A / B), \quad B U(A / B)=\min \{E U(A / B), L(A)\}
$$

where $0 \leq B L(A / B) \leq P(A / B) \leq B U(A / B) \leq 1$, and $B L(A / B)$ and $B U(A / B)$ satisfy the multiplication rules of probability distributions, i.e. :

$$
L(A B) \approx B L(A B)=L(A) B L(A / B), \quad U(A B) \approx B U(A B)=U(A) B U(A / B), \text { where }
$$

$L(A B)(U(A B))$ is not exactly equal to $B L(A / B)(B U(A / B))$, but a certain approximation. If $A$ is independent of $B$, then $B L(A / B)=B L(A)$, and $B U(A / B)=B U(A)$. The multiplication rules for bound-limited weak conditional interval joint probability imply that the joint probability distribution of the given random variables can be simplified on the basis of conditional independencies. This

guarantees that the probability distributions can be represented by BNs, and the probabilistic computation can be done by using inference of BNs.

# 4 Influence Diagrams with Interval-valued Parameters (IIDs) 

An IID consists of a graphical component and a numerical component. These two components are introduced in the following this section.

### 4.1 The Graphical Component

The graphical component is defined as a directed acyclic graph (DAG) denoted by $G=(\mathbf{N}, \mathbf{A})$, where $\mathbf{N}$ contains nodes representing the variables of the decision problem and $\mathbf{A}$ contains directed arcs representing local dependencies between variables. The nodes in $\mathbf{N}$ are partitioned into a set of chance nodes $\mathbf{C}=\left\{C^{1}, \ldots, C^{m}\right\}$, a set of decision nodes $\mathbf{D}=\left\{D^{1}, \ldots, D^{k}\right\}$, and a value node $V$ :

- Chance nodes, $C^{i} \in \mathbf{C}$, represent relevant uncertain factors for a decision problem. $C^{i}$ is drawn as a circle or oval. The lowercase $c$ denotes an instance of $C^{i}$, i.e. a state of $C^{i}$. All states of variable $C^{i}$ are denoted by $\operatorname{dom}\left(C^{i}\right)$.
- Decision nodes, $D^{i} \in \mathbf{D}$, represent actions available to a decision maker. $D^{i}$ is drawn as a rectangle. The lowercase $d$ denotes an action at $D^{i}$. All actions available at $D^{i}$ are denoted by $\operatorname{dom}\left(D^{i}\right)$.
- The value node, $V$, represents the integrated preference of a decision maker. $V$ is drawn as a diamond. The lowercase $v$ denotes a preference of $V$, called a utility value. All preferences are denoted by $\operatorname{dom}(V)$.

In this paper, the terms of both chance and decision variables can be used interchangeably with nodes.

In an IID, nodes with arcs are linked into a node are called the parents of this node, denoted by $\operatorname{Par}(\bullet) . \operatorname{Par}\left(D^{i}\right) \subseteq \mathbf{C} \cup \mathbf{D}$, specifies the variables whose values have been known before the action of $D^{i}$ is chosen; $\operatorname{Par}\left(C^{i}\right) \subseteq \mathbf{C} \cup \mathbf{D}$ specifies the variables on which the conditional probabilities of $C^{i}$ depends, via the bound-limited weak

conditional interval conditional probabilities $\bar{p}\left(C^{i} / \operatorname{Par}\left(C^{i}\right)\right) ; \operatorname{Par}(V) \subseteq \mathbf{C} \cup \mathbf{D}$ specifies the variables on which the preferences depends, via interval-valued utility $\bar{u}(\operatorname{Par}(V))$. While $\operatorname{par}(\bullet)$ denotes an instance of $\operatorname{Par}(\bullet)$, i.e. a configuration of the values of variables of $\operatorname{Par}(\bullet)$, where the symbol $\cdot$ may be $C^{i}, D^{i}$ or $V$.

# 4.2 The Numerical Component 

The numerical component of an IID is defined by an interval-valued conditional probability table (CPT) attached to each chance node and an interval-valued utility table attached to the value node.

- Each entry of a CPT attached to chance node $C^{i}$ specifies a bound-limited weak conditional interval conditional probability $\left[B L\left(c^{i} / \operatorname{par}\left(C^{i}\right)\right), B U\left(c^{i} / \operatorname{par}\left(C^{i}\right)\right)\right]$ to the instance $c^{i}$ of $C^{i}$. If $C^{i}$ is a root of the DAG, i.e. $\operatorname{Par}\left(C^{i}\right)=\phi$, the lower and upper probabilities $B L\left(c^{i}\right)$ and $B U\left(c^{i}\right)$ will be specified to each instance $c^{i}$ of $C^{i}$.
- Each entry of a utility table attached to a value node $V$ specifies an interval-valued utility $\left[u^{L}(\operatorname{par}(V)), u^{U}(\operatorname{par}(V))\right]$ to an instance $\operatorname{par}(V)$ of $\operatorname{Par}(V)$.

Decision nodes are not quantified, because decision nodes describe the deterministic actions of a decision maker, so it is not needed to specify the probabilities of decision nodes. The IIDs also need to satisfy the constraints that are required in conventional IDs. For example, the directed graph should not contain cycles, the value node cannot have children, decision variables are supposed to be totally ordered, according to a priori fixed ordering (this ordering should be consistent with any existing oriented path between decision nodes of the DAG), and IIDs satisfy the "no-forgetting" property, in the sense that the values of the variables that once to be "known" would never be "forgotten".

### 4.3 An Example

Example 1. Figure 1 (Cooper 1988) represents the graphic component of an IID, where $A, B$, and $C$ are chance nodes; $D$ is a decision node; $V$ is a value node.

The arcs from $A$ to $B$ and from $B$ to $C$ show that the status of $B$ and $C$ depend on the status of $A$ and $B$ respectively; the absence of an arc from $A$ to $C$ indicates that $C$ is conditionally independent on $A$ given the value of $B$; the arc from $C$ to $D$ shows that the action is chosen at $D$ knowing the status of $C$; the arcs from $D$ and $A$ to $V$ show that the utility values at $V$ depend on the action chosen at $D$ and on the status of $A$.

The CPTs attached to $A, B$, and $C$ and the utility table attached to $V$ are shown in Table 1, where the probabilities of $A, B$, and $C$ are bound-limited weak conditional interval probabilities and the utilities of $V$ are interval-valued utilities. In the conventional ID, they are point-valued probabilities and point-valued utilities. From this example, we can see that for the same decision modelling problem, the IIDs and the conventional ID have the same graphical components but different numerical components.
![img-0.jpeg](img-0.jpeg)

Figure 1 The graphic component of an IID

Table 1 The bound-limited weak conditional interval probabilities of $A, B$ and $C$ and the interval-valued utilities of $V$


# 5 Evaluating IIDs 

### 5.1 The Concepts on Evaluating IIDs

Let $D^{1}, \Lambda, D^{k}$ be decision nodes in an IID, a policy for $D^{i}$ be a mapping $\delta_{D^{i}}: \operatorname{dom}\left(\operatorname{Par}\left(D^{i}\right)\right) \rightarrow \operatorname{dom}\left(D^{i}\right)$. A strategy $\Delta$ is a vector of policies, one for each decision node, i.e. $\Delta=\left(\delta_{D^{i}}, \Lambda, \delta_{D^{k}}\right)$. Evaluating an IID means to find the optimal strategy $\Delta^{*}$, which maximizes the interval-valued expected utility of value node $V$.

Let $\tilde{p}(\bullet)=\left[B L(\bullet), B U(\bullet)\right]$ be the bound-limited weak conditional interval probability, $\tilde{u}(\operatorname{Par}(V))=\left[u^{L}(\operatorname{Par}(V)), u^{U}(\operatorname{Par}(V))\right]$ be the interval-valued utility of value node $V$, and $\mathbf{E}$ (set of evidences) be a set of chance nodes with known values and decision nodes whose decisions have already been made. Then, the interval-valued expected utility corresponding to a policy of $D^{i}, E \tilde{U}\left(\delta_{D^{i}}(\mathbf{E})\right)$, is defined as follow.

Definition 1. The interval-valued expected utility corresponding to a policy of a decision node. Given $\mathbf{E}$, for a policy of decision node $D^{i}$, the interval-valued expected utility $E \tilde{U}\left(\delta_{D^{i}}(\mathbf{E})\right)=\sum_{\operatorname{par}(V)} \tilde{p}\left(\operatorname{par}(V) / \mathbf{E}, \delta_{D^{i}}(\mathbf{E})\right) \times \tilde{u}(\operatorname{par}(V)) \quad$, where $\tilde{p}(A) \times \tilde{u}(B)=\left[\min \left(B L(A) \times u^{L}(B), B L(A) \times u^{U}(B), B U(A) \times u^{L}(B), B U(A) \times u^{U}(B)\right)\right.$, $\left.\max \left(B L(A) \times u^{L}(B), B L(A) \times u^{U}(B), B U(A) \times u^{L}(B), B U(A) \times u^{U}(B)\right)\right]$
$\tilde{u}(A)+\tilde{u}(B)=\left[u^{L}(A)+u^{L}(B), u^{U}(A)+u^{U}(B)\right]$.
Let $E \tilde{U}(A)=\left[a^{L}, a^{U}\right], \quad E \tilde{U}(B)=\left[b^{L}, b^{U}\right], \quad l_{\tilde{u}}=a^{U}-a^{L}, \quad l_{\tilde{\tilde{u}}}=b^{U}-b^{L}$, then $E \tilde{U}(A) \geq E \tilde{U}(B)$ if $\frac{\min \left(l_{\tilde{u}}+l_{\tilde{\tilde{u}}}, \max \left(a^{U}-b^{L}, 0\right)\right)}{l_{\tilde{u}}+l_{\tilde{\tilde{u}}}} \geq 0.5$.

Let the temporal order of an IID be denoted by $\mathbf{C}^{0} \pi D^{1} \pi \mathbf{C}^{1} \pi \Lambda D^{k} \pi \mathbf{C}^{k}$. The symbol $\pi$ denotes topological precedence. $\mathbf{C}^{i}(i=0, \ldots, k-1)$ includes the chance nodes directly preceding $D^{i+1}$ but not $D^{i} . \mathbf{C}^{k}$ includes the chance nodes that not having decision nodes amongst their direct successors. If a chance node is a direct predecessor of more than a decision node, it belongs to the set associated to the decision node with the smallest index $i . \mathbf{C}^{0} \cup \mathbf{C}^{1} \cup \mathbf{C}^{k}=\mathbf{C}$. The optimal policy for a decision node and the maximal interval-valued expected utility are defined as follows.

Definition 2. The optimal policy. Given $\mathbf{E}$, the optimal policy $\delta_{D^{i}}^{*}$ for $D^{i}$ is defined as: $\delta_{D^{i}}^{*}(\mathbf{E})=\arg \max _{D^{i}} \sum_{\mathbf{C}^{i}} \max _{D^{i+1}} \Lambda \max _{D^{i}} \sum_{\operatorname{par}(V)} \tilde{p}(\operatorname{par}(V) / \mathbf{E})) \times \tilde{u}(\operatorname{par}(V))$.

Definition 3. The maximal interval-valued expected utility $M \widetilde{E} U . M \widetilde{E} U$ is defined as: $M \widetilde{E} U=\sum_{\mathbf{C}^{i}} \max _{D^{i}} \Lambda \max _{D^{k}} \sum_{\operatorname{par}(V)} \tilde{p}(\operatorname{par}(V) / \mathbf{E}) \times \tilde{u}(\operatorname{par}(V))$.

The strategy that can induce $M \widetilde{E} U$ is the optimal strategy $\Delta^{*}$.

To find the optimal strategy $\Delta^{*}$, we first find the optimal policy $\delta_{D^{*}}^{*}$, and update the evidence $\mathbf{E}$ as $\mathbf{E} \cup\left\{\delta_{D^{*}}^{*}\right\}$. Then recursively find the optimal policy $\delta_{D^{*+1}}^{*}, \ldots, \delta_{D^{*}}^{*}$ in the same manner.

# 5.2 The Approach for Evaluating IIDs 

Amongst existing indirect methods for evaluating IDs, Cooper's method (1988) is a well known method. It represents the basis of existing indirect methods (Guezguez et al. 2009). The key idea of Cooper's method is to transform an ID into a BN and then to compute maximal expected utilities via the inference of the BN. Using a BN instead of a decision tree as a secondary structure to determine the optimal policy can use conditional independencies amongst variables. Moreover, it avoids heavy probabilistic computations required by a direct evaluation method. Guezguez et al. (2009) developed a possibilistic counterpart of Cooper's method (1988) for evaluating qualitative possibilistic IDs. This method transforms a qualitative possibilistic ID into a qualitative possibilistic network (Ben Amor et al., 2001), and makes inference in this qualitative possibilistic network using the appropriate propagation algorithms. Guezguez et al.'s method in qualitative possibilistic IDs inspired us to extend Cooper's method (1988) to evaluate IIDs. Our choice is reinforced by the fact that IBNs have been developed as well as their propagation algorithms (Liu \& Yue 2011). Therefore, to evaluate IIDs, we first transform IIDs into IBNs, and then compute interval-valued expected utilities based on the inferences of IBNs. This approach can be regarded as the counterpart of Cooper's method (1988) for evaluating IIDs.

Transforming IIDs into IBNs consists of transforming the decision nodes and the value node into chance nodes.

## - Transforming decision nodes into chance nodes

The decision node $D^{i}$ is presented as a circular node whose lower and upper probabilities are defined by Equation (1).

$$
B L\left(\delta_{D^{i}}=d\right)=B U\left(\delta_{D^{i}}=d\right)=\frac{1}{\left|\operatorname{dom}\left(D^{i}\right)\right|}, \forall d \in \operatorname{dom}\left(D^{i}\right), i=1, \ldots, k
$$

Where $\left|\operatorname{dom}\left(D^{i}\right)\right|$ is the number of possible actions that can be taken at $D^{i}$. The

arcs into $D^{1}$ will be ignored.

# - Transforming the value node into a chance node 

The value node $V$ is presented as a circular node with two states $v$ and $\neg v$, representing the desired and undesired outcomes respectively. The bound-limited weak conditional interval conditional probabilities of $V$ are defined by Equation (2).

$$
\begin{aligned}
& B L(V=v / \operatorname{par}(V))=\frac{u^{L}(\operatorname{par}(V))+k_{2}}{k_{1}}, \quad B U(V=v / \operatorname{par}(V))=\frac{u^{U}(\operatorname{par}(V))+k_{2}}{k_{1}} \\
& B L(V=\neg v / \operatorname{par}(V))=\frac{u^{U}(\operatorname{par}(V))+k_{3}}{-k_{1}}, B U(V=\neg v / \operatorname{par}(V))=\frac{u^{L}(\operatorname{par}(V))+k_{3}}{-k_{1}} \\
& \text { where } k_{1}=\max _{\operatorname{par}(V)}\left(u^{U}(\operatorname{par}(V))\right)-\min _{\operatorname{par}(V)}\left(u^{L}(\operatorname{par}(V))\right), \quad k_{1} \neq 0, \quad k_{2}=-\min _{\operatorname{par}(V)}\left(u^{L}(\operatorname{par}(V))\right) \\
& k_{3}=-\max _{\operatorname{par}(V)}\left(u^{U}(\operatorname{par}(V))\right)
\end{aligned}
$$

After transforming all decision nodes and the value node $V$ into chance nodes, the IIDs becomes an IBN.

Based on Equation (2), the interval-valued expected utility $E \tilde{U}\left(\delta_{D^{\prime}}(\mathbf{E})\right)$, defined in Definition 1, can be presented as Equation (3):

$$
\begin{aligned}
& E \tilde{U}\left(\delta_{D^{\prime}}(\mathbf{E})\right)=\sum_{\operatorname{par}(V)}\left[a^{L}, a^{U}\right] \times\left[k_{1} b^{L}-k_{2}, k_{1} b^{U}-k_{2}\right]=k_{1} \sum_{\operatorname{par}(V)}\left[a^{L}, a^{U}\right] \times\left[b^{L}, b^{U}\right]-k_{2} \sum_{\operatorname{par}(V)}\left[a^{L}, a^{U}\right] \\
& =k_{1} \sum_{\operatorname{par}(V)}\left[a^{L} \times b^{L}, a^{U} \times b^{U}\right]-k_{2} \sum_{\operatorname{par}(V)}\left[a^{L}, a^{U}\right]=k_{1} \tilde{p}(V=v / \mathbf{E})-k_{2}
\end{aligned}
$$

where $a^{L}=B L\left(\operatorname{par}(V) / \mathbf{E}, \delta_{D^{\prime}}(\mathbf{E})\right), \quad a^{U}=B U\left(\operatorname{par}(V) / \mathbf{E}, \delta_{D^{\prime}}(\mathbf{E})\right), \quad b^{L}=B L(V=v / \operatorname{par}(V))$, $b^{U}=B U(V=v / \operatorname{par}(V)), \quad \sum_{\operatorname{par}(V)}\left[a^{L}, a^{U}\right]=[1,1]$.

Equation (3) implies that $E \tilde{U}\left(\delta_{D^{\prime}}(\mathbf{E})\right)$ can be computed based on $\tilde{p}\left(V=v / \mathbf{E}, \delta_{D^{\prime}}(\mathbf{E})\right)$, which can be obtained by the inference of IBNs.

Example 2. The IBN transformed from the IID shown in Example 1 of Section 4.3 is shown in Figure 2.

If the evidence $\mathbf{E}$ is $C=c_{1}$, then $\tilde{p}\left(V=v / \mathbf{E}, \delta_{D}(\mathbf{E})=d_{1}\right)=[0.5,0.7693]$, $\tilde{p}\left(V=v / \mathbf{E}, \delta_{D}(\mathbf{E})=d_{2}\right)=[0.3846,0.61]$. According to Equation (3), we have $E \tilde{U}\left(\delta_{D}(\mathbf{E})=d_{1}\right)=[2,4.693] \quad, \quad E \tilde{U}\left(\delta_{D}(\mathbf{E})=d_{2}\right)=[0.843,3.1] \quad . \quad$ Because $E \tilde{U}\left(\delta_{D}(\mathbf{E})=d_{1}\right)>E \tilde{U}\left(\delta_{D}(\mathbf{E})=d_{2}\right)$, thus $\delta_{D}^{*}\left(C=c_{1}\right)=d_{1}$.

![img-1.jpeg](img-1.jpeg)

Figure 2 The IBN transformed from the IID shown in Example 1

# 5.3 The Algorithm for Evaluating IIDs 

In this section, we introduce the algorithm EAIID for evaluating IIDs, where the Algorithm 5.1 (proposed by Liu \& Yue (2011)), an approximate inference algorithm for IBNs, is used to obtain the bound-limited weak conditional interval conditional probabilities of the value node $V$ with respect to a policy $\delta_{D}$. Alternatively, it can be obtained by calling an exact inference algorithm for IBNs.

## Algorithm EAIID.

Input: an IID, the set of evidence nodes $\mathbf{E}$, and the configuration of values of the evidence nodes $\mathbf{e}$.

Output: the optimal strategy $\Delta^{*}$ and maximal interval-valued expected utility $M \bar{E} U$.
(1) Initialization:
(1.1) $\Delta=\phi, \quad k_{1}=\max _{p a r(V)}\left(u^{U}(p a r(V))\right)-\min _{p a r(V)}\left(u^{L}(p a r(V))\right)$
(1.2) $k_{2}=-\min _{p a r(V)}\left(u^{L}(p a r(V))\right), \quad k_{3}=-\max _{p a r(V)}\left(u^{U}(p a r(V))\right)$
(2) For $i=1$ to $k \quad / / k$ is the number of the decision nodes

Transforming decision nodes into chance nodes according to Equation (1)
(3) Transforming the value node into a chance node according to Equation (2)
(4) $I B N \leftarrow I I D$
(5) For $i=k$ to 1
(5.1) For each $d \in \operatorname{dom}\left(D^{i}\right)$

(5.1.1) $\tilde{p}\left(V / \mathbf{E}, \delta_{D^{\prime}}(\mathbf{E})=d\right)=$ Algorithm 5.1 (IBN)
(5.1.2) $E \tilde{U}\left(\delta_{D^{\prime}}(\mathbf{E})=d\right)=k_{1} \tilde{p}\left(V=v / \delta_{D^{\prime}}(\mathbf{E})=d\right)-k_{2}$
(5.2) $\delta_{D^{\prime}}^{*}(\mathbf{E})=\underset{d}{\arg \max } E \tilde{U}\left(\delta_{D^{\prime}}(\mathbf{E})=d\right), d \in \operatorname{dom}\left(D^{i}\right)$
(5.3) $\Delta=\Delta \cup\left\{\delta_{D^{\prime}}^{*}\right\}, \quad M \widetilde{E} U=E \tilde{U}\left(\delta_{D^{\prime}}^{*}(\mathbf{E})\right)$
(5.4) $\mathbf{E}=\mathbf{E} \cup\left\{D^{i}\right\}, \mathbf{e}=\mathbf{e} \cup\left\{d^{*}\right\}$
(5.5) $\tilde{p}\left(\delta_{D^{\prime}}^{*}(\mathbf{E})\right)=[1,1], \quad \tilde{p}\left(\delta_{D^{\prime}}(\mathbf{E})\right)=[0,0]$ for $\delta_{D^{\prime}}(\mathbf{E}) \neq \delta_{D^{\prime}}^{*}(\mathbf{E})$
(6) Output $\Delta$ and $M \widetilde{E} U$.

The time complexity of the algorithm EAIID is mainly determined by Step (5). The time complexity of Algorithm 5.1 is $O(m \times n)$, where $n=\|\mathbf{N}\|$ is the number of nodes in an IID, $m$ is the times of iterations that Algorithm 5.1 arrives at the convergence; the time complexity of step (5.2) is $O\left(\max \left(\left|\operatorname{dom}\left(D^{i}\right)\right|^{2}\right)\right) \quad(i=1,2, \Lambda, k)$; so the time complexity of algorithm EAIID is $O\left(k \times\left(\left(m \times n \times \max \left(\left|\operatorname{dom}\left(D^{i}\right)\right|\right)\right)+\max \left(\left|\operatorname{dom}\left(D^{i}\right)\right|^{2}\right)\right)\right) \quad(i=1,2, \Lambda, k)$, where $k$ is the number of decision nodes. Usually, $k \ll m,\left|\operatorname{dom}\left(D^{i}\right)\right| \ll m$.

# 6 Experimental Studies and Results 

In this section, we test the EAIID algorithm on four influence diagrams with different features: an ID with interval-valued probabilities and interval-valued utilities (denoted as "ID- $B c B v$ "), an ID with point-valued probabilities and point-valued utilities (denoted as "ID-PcPv"), an ID with point-valued probabilities and interval-valued utilities (denoted as "ID-PcBv"), and an ID with interval-valued probabilities and point-valued utilities (denoted as "ID-BcPv"). First, we evaluate the ID-BcBv to test whether the EAIID algorithm can find the optimal strategy, then we evaluate the ID-PcPv, the ID-PcBv and the ID-BcPv by representing each precise point-valued parameter (probability or utility) as an interval-valued parameter, such as [a, a] for the purpose of testing the effectiveness of the EAIID algorithm. The graphic components of four IDs used in all experiments are shown in Figure 1 of Section 4.3,

the numerical components of the four IDs used in experiments are different as shown in Tables 1, 4, 6 and 8.

Each evaluation is repeated 10 times, each of which consists of 100 iterations (because Algorithm 5.1 used in EAIID is a sample algorithm), and then the average lower and upper expected utilities in 100 iterations are taken as the evaluation results of each time. We further compute the average lower and upper expected utilities for 10 evaluation results (denoted as "EAIID"), and compare them with those obtained by other methods.

Variable elimination (VE) (Zhang \& Poole 1996) and arc reversal (AR) (Shachter 1986) are two standard approaches to IDs evaluation. Cabañas et al. (2016) adopted $V E$ and $A R$ schemes for IIDs evaluation by replacing the operations over point-valued potentials with the analogous operations for interval-valued potentials. In VE scheme, the procedure to eliminate a variable is based on the potentials including the variable to eliminate in their arguments are combined and the elimination is performed on the combined potential. When cope with IIDs, the last combination together with the elimination are performed. In $A R$ scheme, IIDs are evaluated by performing elimination of chance and decision variables and arc reversal. These extensions are achieved by local optimization tasks, reduced to linear programs. To avoid the unnecessarily large outer approximations produced in extended VE, Cabañas et al. (2016) also proposed a faster but less accurate procedure, which does not require linear programming. The latter approach gives an outer approximation analogous to the generalization of the AR algorithm proposed by Breeze \& Fertig (1990). In this section, we compare our method with the variable elimination by linear programming (denoted as " $V E_{l p}$ "), the faster outer approximation of $V E_{l p}$ (denoted as " $V E_{\text {outer }}$ ") and the arc reversal by linear programming (denoted as " $A R_{l p}$ ") (Cabañas et al. 2016).

In the following, Figure 3, 4, 5 and 6 present the expected utilities of EAIID in 10 experiments. In Figure (a) and (b), the evidence $\mathbf{E}$ is $C=c_{1}$, while $C=c_{2}$ in Figure (c) and (d). In Figure (a) and (c), the action taken at decision node $D$ is $d_{1}$, while $D=d_{2}$ in Figure (b) and (d). Table 3, 5, 7 and 9 show the comparison amongst results

obtained by $E A I I D$ and $V E_{l p}, V E_{\text {outer, }}$ and $A R_{l p}$. Each bold entry in these Tables is the maximal expect utility corresponding to the optimal strategy.

# 6.1 Results for ID-BcBv 

First, we evaluate the ID-BcBv, the parameters are shown in Table 1 of Section 4.3.
![img-2.jpeg](img-2.jpeg)

Figure 3 The evaluation results of the EAIID on the ID-BcBv
In Figure 3(a), the average lower and upper expected utilities are $\overline{E U}_{E A I I D}^{L}=2.082$ and $\overline{E U}_{E A I I D}^{U}=4.6$ respectively, $\Delta_{E A I I D}^{\prime}=\left(\delta_{D}\left(C=c_{1}\right)=d_{1}\right)$ in 10 evaluations, and the maximal errors between expected utility and the average of expected utility are $\mid \max \left(E U^{L}{ }_{E A I I D}\right)-\overline{E U}_{E A I I D}^{L} \mid=0.073$ and $\mid \max \left(E U^{U}{ }_{E A I I D}\right)-\overline{E U}_{E A I I D}^{U} \mid=0.041$ respectively. It indicates that both the fluctuations of lower and upper expected utilities are gentle. The results in Figure 3(b), (c) and (d) are similar. Thus, the EAIID algorithm is stable.

Table 3 indicates that the optimal strategies found by EAIID are same with those by other algorithms, but the expected utilities obtained by EAIID have narrower interval than those obtained by $V E_{l p}, V E_{\text {outer }}$ and $A R_{l p}$, i.e. $\left[E U^{L}{ }_{E A I I D}, E U_{E A I I D}^{U}\right] \subset\left[E U^{L}{ }_{V E_{l p}}, E U_{V E_{l p}}^{U}\right]$, $\left[E U^{L}{ }_{E A I I D}, E U_{E A I I D}^{U}\right] \subset\left[E U_{V E_{\text {outer }}}^{L}, E U_{V E_{\text {outer }}}^{U}\right],\left[E U^{L}{ }_{E A I I D}, E U_{E A I I D}^{U}\right] \subset\left[E U^{L}{ }_{A R_{l p}}, E U_{A R_{l p}}^{U}\right]$.

Table 3 The comparison amongst results obtained by the EAIID and other methods on the ID- $B c B v$


# 6.2 Results for ID-PcPv 

In the second test, we use the EAIID algorithm to evaluate the ID-PcPv, the parameters are shown in Table 4.

Table 4 The point-valued probabilities and point-valued utilities


![img-3.jpeg](img-3.jpeg)

Figure 4 The evaluation results of the EAIID on the ID-PcPv
Figure 4(a) (d) also indicate that both the lower and upper expected utilities have gentle fluctuations and the EAIID algorithm is stable.

Table 5 indicates that the optimal strategies found by EAIID are same with those by other algorithms, and the upper bounds of the expected utilities are very close to the lower bounds. It shows that the interval-valued results are converged to the precise

pointed-valued ones. This demonstrates the feasibility and suitability of our method for evaluating directly conventional IDs that is a special case of IIDs.

Table 5 The comparison amongst results obtained by the EAIID and other methods on the ID-PcPv


# 6.3 Results for ID-PcBv 

In the third test, we evaluate the ID-PcBv whose parameters are shown in Table 6.

Table 6 The point-valued probabilities and interval-valued utilities


![img-4.jpeg](img-4.jpeg)

Figure 5 The evaluation results of the EAIID on the ID-PcBv
Figure 5(a) (d) also indicate that both the lower and upper expected utilities have gentle fluctuations and the EAIID algorithm is stable.

Table 7 indicates that the optimal strategies found by EAIID are same with those by other algorithms, and the expected utilities obtained by EAIID are very close to those

by other algorithms. It indicates that our method can evaluate directly the ID-PcBv, the second special case of IIDs.

Table 7 The comparison amongst results obtained by the EAIID and other methods on the ID-PcBv


# 6.4 Results for ID-BcPv 

In the last test, we evaluate the ID-BcPv whose parameters are shown in Table 8.

Table 8 The bound-limited weak conditional interval probabilities and the point-valued utilities


![img-5.jpeg](img-5.jpeg)

Figure 6 The evaluation results of the EAIID on the ID-BcPv
Figure 6(a) (d) also indicate that both the lower and upper expected utilities have gentle fluctuations and the EAIID algorithm is stable.

Similar to the results for $I D-B c B v$, the optimal strategies found by EAIID are same with those by other algorithms, but the expected utilities obtained by EAIID have

narrower interval than those obtained by $V E_{l p}$ and $V E_{\text {outer }}$ and $A R_{l p}$,

Table 9 The comparison amongst results obtained by the EAIID and other methods on the ID-BcPv


Based on the above results, we can find that the IIDs proposed in this study and associated algorithms performed well under different circumstances. Thus IIDs provide a technical solution to model decision making processes in uncertain situations, such as where values of variables are represented by interval values.

# 6.5 A Case Study 

When Tangshan Smokeless Coal Mining Plc makes mining decisions (Liu 2007), it needs to analyse the different factors of risks involved and quantify the degrees of risks that are significant for the enterprise to avoid loss and obtain sustained gain. However, the risk analysis of a mining decision is a complex decision process. In general, the risks come from three aspects:
(1) The uncertainty of the natural conditions of mining, such as geological conditions, ore grades and ore reserves;
(2) The uncertainty of the social environment, such as market requirements, environment protection regulations and international competitions;
(3) The uncertainty of the mining technique factors, such as mining condition assessment information and related experience.

The factors that affect the mining risk analysis of mining decisions and the relationship amongst factors are represented by Figure 7.

![img-6.jpeg](img-6.jpeg)

Figure 7 Mining risk factors analysis

It is a common practice for Tangshan Plc to make assessments based on the estimated range values of these factors for risk analysis, because it is difficult to estimate precise values for these factors. Assume that each factor is represented by an interval-valued variable with two statuses. For example, the Geological conditions is represented by $G C$ whose status $g c_{1}=\left[\mathrm{a}_{1}, \mathrm{a}_{2}\right]$ means acceptable range and $g c_{2}=\left[\mathrm{a}_{3}, \mathrm{a}_{4}\right]$ means unacceptable range. The interval data of the mining risk factors is shown in Table 10 .

Because the values of the variables themselves are imprecise, the influences amongst variables need to be represented by interval conditional probabilities. In a similar way, the outcome of decision making is also represented by interval values.

Overall, the decision process of Tangshan are modelled by the IIDs shown in Figure 8 , where 12 ovals are chance nodes, the rectangle (DE) is the decision node, and the diamond (OC) is the value node representing the outcome of decision making. The bound-limited weak conditional interval probabilities calculated from Table 10 are shown in Tables 11-16. Table 17 shows the utilities of investment under different statuses of the Mining risk analysis (RA): the minimum and maximum revenue of investment are $\$ 700$ and $\$ 750$ million respectively when the status of risk is $r a_{1}$ (acceptable range), but the minimum and maximum loss of investment are $\$ 500$ and

$\$ 600$ million respectively when the status of risk is $r a_{2}$ (unacceptable range).
Table 10 The interval data of the mining risk factors


![img-7.jpeg](img-7.jpeg)

Figure 8 The graphic component of the IID for the decision making of mining

Table 11 The $[B L(G C), B U(G C)],[B L(O G), B U(O G)],[B L(O R), B U(O R)],[B L(M R), B U(M R)]$


Table 12 The $[B L(E P), B U(E P)],[B L(I C), B U(I C)],[B L(M C), B U(M C)],[B L(R E), B U(R E)]$


Table 13 The $[B L(N C / G C, O G, O R), B U(N C / G C, O G, O R)]$


Table 14 The $[B L(S E / M R, E P, I C), B U(S E / M R, E P, I C)]$


Table 15 The $[B L(T F / M C, R E), B U(T F / M C, R E)]$


Table 16 The $[B L(R A / N C, S E, T F, D E=d e_{1}), B U(R A / N C, S E, T F, D E)]$


Table 17 The utility $\left[u^{L}(R A, D E), u^{U}(R A, D E)\right]$ at the node $O C$


Based on the constructed IID, the optimal strategy that can result in the maximal interval-valued expected utility can be found by using the EAIID algorithm. For example, given the state of Geological conditions ( $G C$ ) in Table 11, interval-valued expected utility obtained by EAIID and VE algorithm (Cabañas et al. 2016) are shown in Table 18.

Table 18 The comparison amongst results obtained by the EAIID and $V E_{\text {ip }}$ on the IID of Figure 8


Table 18 indicates that the optimal strategies is $\Delta^{*}=\left(\delta_{D E}^{*}\left(G C=g c_{1}\right)=d e_{1}\right)$, i.e. Tangshan Plc should invest $\left(d e_{1}\right)$ under the evidence of $G C=g c_{1}$, while the optimal strategies is $\Delta^{*}=\left(\delta_{D E}^{*}\left(G C=g c_{2}\right)=d e_{2}\right)$, i.e. Tangshan Plc should not invest $\left(d e_{2}\right)$

under the evidence of $G C=g c_{2}$
From this case, we can see that the strategy making decision makers to obtain the maximal expect utility can be found, although variables related to the decision making have imprecise values. Thus the application areas of influence diagrams are expanded.

# 7 Conclusions 

It has been recognized that one of the three main approaches to describe uncertainties is interval analysis (Elishakoff \& Ohsaki 2010). Moreover, interval analysis has been considered as the most widely adopted analytic tool among non-probabilistic analysts. Extending influence diagrams with ability to process interval data provides a promising approach for decision making under uncertainty.

In this paper, IDs with point-valued parameters are extended as IDs with interval-valued parameters in which bound-limited weak conditional interval probabilities are used to represent beliefs, and interval values are used to represent the preferences of decision makers. This extension avoids the difficulties attached to the specification of precise parameter values, and provides a capability for modelling decision making processes in the situation that the precise parameter values cannot be obtained. Thus, the IIDs introduced in this paper can support decision making in more uncertain and complex situations.

In this paper, the task of evaluating of IIDs is converted into inference problems of IBNs. This conversion enables one to use exact or approximate inference algorithms of BNs to efficiently evaluate IIDs. We developed an indirect method and an algorithm to evaluate the IIDs. The developed method is a counterpart method of Cooper's evaluation method, and the developed algorithm can select strategies select with the maximal expected utility for decision makers. The comparative experiments with other methods and the application in a real life case verify the feasibility and robustness of our extended model and evaluation method.

There are a number of issues still require further investigation. A direct improvement of our approach is to extend our model and the proposed evaluation methods to deal with more than one value node in order to treat multi-objective

decision problems. Also, integrating game theory into IIDs, in order to provide more rational decision making in uncertain and interactive situations, is another direction requires further studies.

# Acknowledgments 

The authors would like to sincerely thank for Rafael Cabañas and Alessandro Antonucci of Department of Computer Science and Artificial Intelligence CITIC, University of Granada, Spain, for providing code developed in their work and their unreserved support for this study. We would like to thank anonymous reviewers for their valuable comments. This research was supported by the National Natural Science Foundation of China (61262069, 61472346), The Natural Science Foundation of Yunnan Province (2016FA026, 2015FB114), The Program for Young and Middle-aged Teachers of Yunnan University (WX173602), the Program for Innovative Research Team of Yunnan University (XT412011), and Program for Innovation Research Team (in Science and Technology) in University of Yunnan Province.
