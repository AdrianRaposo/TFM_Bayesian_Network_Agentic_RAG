# A symbolic algebra for the computation of expected utilities in multiplicative influence diagrams 

Manuele Leonelli ${ }^{1}$ (D) $\cdot$ Eva Riccomagno ${ }^{2} \cdot$ Jim Q. Smith ${ }^{3}$


#### Abstract

Influence diagrams provide a compact graphical representation of decision problems. Several algorithms for the quick computation of their associated expected utilities are available in the literature. However, often they rely on a full quantification of both probabilistic uncertainties and utility values. For problems where all random variables and decision spaces are finite and discrete, here we develop a symbolic way to calculate the expected utilities of influence diagrams that does not require a full numerical representation. Within this approach expected utilities correspond to families of polynomials. After characterizing their polynomial structure, we develop an efficient symbolic algorithm for the propagation of expected utilities through the diagram and provide an implementation of this algorithm using a computer algebra system. We then characterize many of the standard manipulations of influence diagrams as transformations of polynomials. We also generalize the decision analytic framework of these diagrams by defining asymmetries as operations over the expected utility polynomials.


Keywords Asymmetric decision problems $\cdot$ Computer algebra $\cdot$ Influence diagrams $\cdot$ Symbolic inference

Mathematics Subject Classification (2010) 68T37

[^0][^1]
[^0]:    Manuele Leonelli was funded by Capes, whilst J.Q. Smith was partly supported by EPSRC grant EP/K039628/1 and The Alan Turing Institute under EPSRC grant EP/N510129/1.

[^1]:    Manuele Leonelli
    manuele.leonelli@glasgow.ac.uk

    1 School of Mathematics and Statistics, University of Glasgow, Glasgow G12 8QW, UK
    2 Dipartimento di Matematica, Universita' degli Studi di Genova, Via Dodecaneso 35, 16146 Genova, Italia

    3 Department of Statistics, The University of Warwick, Coventry CV47AL, UK

# 1 Introduction 

Decision makers (DMs) are often required to choose in critical situations between a wide range of different alternatives. They need to consider the mutual influence of quantifications of different types of uncertainties, the relative values of competing objectives together with the consequences of the decisions they will make. They can thus benefit from an intuitive framework which draws together these uncertainties and values so as to better understand and evaluate the full consequences of the assumptions they are making. To this end, a variety of graphical models have been developed. The most important of these are Bayesian networks (BNs) [37, 44] and influence diagrams (IDs) [4, 26, 36], both of which provide an intuitive qualitative representation of the elements of the DM's problem together with relatively fast computational tools for the calculation of, respectively, probabilities and expected utilities (EUs) [27, 39, 44]. Although only the second class of models can be used to automatically select an optimal course of action, i.e. an EU maximizing decision, both BNs and IDs are invaluable decision support tools, enabling DMs to easily investigate the effect of their inputs to an output of interest.

Most of the algorithms for the computation of probabilities and EUs rely on a full specification of the model's parameters. Furthermore, commonly available software almost exclusively work numerically with complete elicitations. However, often in practice DMs might not be confident about the precision of their specifications, nor have available all such values. This may lead to non-robust decision making where the efficacy of decisions can change under small perturbations of the model's inputs. Symbolic approaches, not requiring full elicitations of the parameters, have proven useful in performing these types of input-output investigations, usually called sensitivity analyses, both in fully inferential and decision making contexts [1, 2, 14, 35]. A variety of symbolic methods for both inference and sensitivity analysis are now in place for BNs [10, 12]. However, the development of symbolic techniques for EU computations in IDs has been largely neglected. An exception is a recent paper [6] where decision network polynomials are defined in the context of Bayesian decision problems. These are piece-wise functions made of so-called pieces: multilinear polynomials having as indeterminates both probability and utility parameters. A new symbolic sensitivity technique is then developed in [6] based on differentiation and difference operators.

In this paper, we focus on a large class of IDs called multiplicative influence diagrams (MIDs), which include as a special case standard IDs equipped with additive utility factorizations, and fully characterize the polynomial structure of the EU pieces (Section 3). We then introduce a symbolic algorithm for their computation, based on simple matrix operations (Section 4), and its implementation in the computer algebra system Maple ${ }^{t n 1}$ (Appendix B). Because of the simplicity of the required operations, our algorithm is shown to have computational times comparable to those of standard numerical evaluation software for graphical models (Section 4.4). In contrast to standard software, which assumes an additive factorization between utility nodes, we also explicitly analyze cases when the more general class of multiplicative utility functions might be necessary [29, 30, 44]. We concentrate our study on the class of multiplicative factorizations because this provides some computational advantages over, for example, the more general class of multilinear utilities [30], whilst allowing for enough flexibility to model the DM's preferences in many real

[^0]
[^0]:    ${ }^{1}$ Maple is a trademark of Waterloo Maple Inc.

cases [22, 29]. This factorization turns out to be particularly efficient since it leads to a distributed propagation of EUs as shown in Proposition 1.

The symbolic definition of the ID's probabilities and utilities in Section 3 provides an elegant and efficient embellishment of the associated graphical representation of the decision problem, around which symbolic computations can then be carried out. In Sections 5 and 6 standard manipulations of IDs and asymmetries are characterised on this new polynomial representation. Importantly we demonstrate that, whilst graphical representations of asymmetries are rather more obscure than standard ID models, in our symbolic approach the imposition of asymmetries greatly simplifies the polynomial representation of the problem. The example in Section 7 then outlines the insights our approach can give to DMs through the comparison of different parameters' specifications. Our symbolic approach has the great advantage in such sensitivity studies that, by exploiting the known polynomial expression of the problem, one can simply plug-in different numerical specifications and instantaneously get the EU values. In standard numerical approaches on the other hand, the evaluation algorithm needs to be run for each combination of parameters considered. This can become quickly unfeasible even for rather small problems.

# 2 A review of symbolic approaches to decision making and support 

Symbolic inference and decision support techniques have already been used for the analysis of BN models. A symbolic definition of probabilities in BNs in terms of multilinear polynomials first appeared in [9]. Since then various inferential techniques have been developed $[11,18,24]$. Their most demonstrably useful application is in the process of validating models through sensitivity analyses. Two main approaches are adopted in practice. The first one is based on differentiation of the probability polynomials and is useful for the analysis of global changes of probability distributions [13, 14]. The second one concerns local changes studied via sensitivity functions [15, 23], which, because of the assumed multilinearity, are simple linear functions of the parameters of interest. Recently, symbolic methods have been extended to asymmetric models [24,33] where the associated polynomials might not exhibit regular multilinear structures as for BNs.

Although it is known that EUs in IDs also have a multilinear structure [21], symbolic methodologies for such models have not been studied consistently. Only recently the robustness of decision models has been analysed from a symbolic viewpoint in [6]. For the i-th available strategy, [6] defines the functions $u_{i}: \mathcal{X} \rightarrow \mathbb{R}$, where $\mathcal{X}$ is the parameter space, representing the EU of the associated strategy and called EU piece. The decision network polynomial is then defined as $\max _{i=1, \ldots, M} u_{i}(x)$, for $M$ available strategies, and represents the expected utility of the optimal strategy for the combination of parameters $x$.

However, no assumptions about the attributes of the problem entertaining various conditional utility or additive/preferential independences are utilized in [6], where a utility value is associated to each possible combination of decisions and realizations of random variables. Such assumptions, often encountered in applied decision analyses, are commonly encoded in a particular factorization of the utility function which then leads to fast and distributed algorithm for the computation of expected utilities. Thus, without formally acknowledging such independences a great amount of information about the preferences of the DM and computational efficiency can be lost. Furthermore, no details on how to compute the functions $u_{i}$ are given in [6]. In this paper we extend this symbolic framework by developing a distributed symbolic procedure for the computation of the EU pieces for utilities chosen in

the large class of multiplicative IDs [30, 44]. We further fully characterize symbolically the functions $u_{i}$ of the decision problem. This enables the application of the proposed methodology to robustness studies where certain parameters are treated as unknown. In Section 7 via an example we show how to exploit our definition for informing a DM about the optimization process. A full development of such symbolic optimization techniques is beyond the scope of this paper.

Of course the solution and investigation of both generic decision problems and influence diagrams can be performed outside of the full Bayesian symbolic paradigm and using uncertainty calculi that relax the assumption of an exact and complete probability specification. One of such proposals [8], is based on imprecise probabilities and consists of mapping the evaluation of an ID into an inferential problem in credal networks [17], solved using multilinear programming [7]. The objective function of such an optimization problem can be shown to be multilinear and to share many features with our polynomial representation of EUs, although within a different domain. Because of the use of imprecise probabilities the parameters of the decision problem can be specified only partially.

Symbolic evaluation methods have also been introduced for discrete and finite time decision Markov processes that do not require full parameters' elicitations (e.g. [31]). As an ID can always be cast as a Markov decision process, the evaluation methods originally designed for general Markov processes can be straightforwardly applied to IDs. A different approach is taken by the so called symbolic dynamic programming: for such a technique the sample space does not need to be fully specified [38, 47]. Again these methods have the capability of helping the DM to discover the most critical features of the decision problem where accurate specification of inputs is most necessary.

The methods reviewed above propose to automate decision making in a variety of frameworks and reasoning paradigms where DMs do not need to provide complete and/or exact parameters' specifications. These have proven to be successful and computationally efficient, but EU maximization is still most commonly applied within a standard probabilistic domain. Therefore, here we assume that the DM plans to behave as an EU maximizer and we will henceforth work entirely within this most standard framework.

# 3 Symbolic representation of influence diagrams 

In this paper, with the exception of Section 6, we consider those Bayesian decision problems that can be represented by an ID and are usually called uniform (or symmetric) [32, 44]. Let $n$ be a positive integer $\left(n \in \mathbb{Z}_{\geq 1}\right)$ and $\mathbb{D}$ and $\mathbb{V}$ be a partition of $[n]=\{1, \ldots, n\}$. Let $\left\{Y_{i}: i \in \mathbb{D}\right\}$ be a set of controlled (or decision) ${ }^{2}$ variables and $\left\{Y_{i}: i \in \mathbb{V}\right\}$ a set of non-controlled (or random) variables. As in standard ID representations, the set of decision variables is assumed to be totally ordered and the union of $\left\{Y_{i}: i \in \mathbb{V}\right\}$ and $\left\{Y_{i}: i \in \mathbb{D}\right\}$ to be totally ordered compatibly with a partial order on the random variables. Let $\preceq$ be the chosen ordering relationship. The ordering on the $Y_{i}$ 's is reflected by their indices, that is if $Y_{i} \preceq Y_{j}$ then $i<j$.

For $i \in[n]$ and $r_{i} \in \mathbb{Z}_{\geq 1}$, let $\left[r_{i}\right]_{0}=\left\{0, \ldots, r_{i}-1\right\}$ and $Y_{i}$ take values in $\mathcal{Y}_{i}=\left[r_{i}\right]_{0}$. For $A \subseteq[n]$, let the vector $Y_{A}=\left(Y_{i}\right)_{i \in A}$ take values in $\mathcal{Y}_{A}=\times_{i \in A} \mathcal{Y}_{i}$ and denote with $y_{A}$ a generic instantiations of $Y_{A}$. Examples of this notation are: the vector $Y_{[n]}$ includes all the variables, whilst $Y_{\mathbb{D}}$ and $Y_{\mathbb{V}}$ are the vectors of controlled and random variables respectively.

[^0]
[^0]:    ${ }^{2}$ With controlled variable we mean a variable set by the DM to take a particular value.

# 3.1 Multiplicative influence diagrams 

We consider the class of multiplicative IDs entertaining a multiplicative factorization over the utility nodes $U=\left(U_{1}, \ldots, U_{m}\right)^{\mathrm{T}}$ (see e.g. [30, 44]). For $i \in[m], U_{i}$ is a function onto $[0,1]$ defined on a subspace $\mathcal{Y}_{P_{i}}$ of $\mathcal{Y}_{[n]}$ where $P_{i} \subseteq[n]$ is assumed non empty.

Definition 1 A multiplicative influence diagram (MID) $G$ consists of three components: a directed acyclic graph (DAG) with vertex (or node) set $V(G)=Y_{[n]} \cup U$, a transition probability function related to the random variables $Y_{\mathbb{V}}$ and a multiplicative factorization function related to the $U$ nodes.

Example 1 Figure 1 presents an MID with $n=6, m=3, \mathbb{D}=\{1,4\}, \mathbb{V}=\{2,3,5,6\}$ and vertex set $V(G)=\left\{Y_{1}, \ldots, Y_{6}, U_{1}, \ldots, U_{3}\right\}$. There are two controlled variables, $Y_{1}$ and $Y_{4}$, four random variables, $Y_{2}, Y_{3}, Y_{5}$ and $Y_{6}$, and three utility nodes, $U_{1}, U_{2}$ and $U_{3}$. We adopt the convention by which decision variables and random variables are respectively framed with squares and circles. All variables are binary and take values in the spaces $\mathcal{Y}_{i}=\{0,1\}$, $i \in[6]$.

Next we describe the three components of an MID starting from its edge (or arc) set $E(G)$. For $i \in[n]$, the parent set of $Y_{i}$ is the sub-vector of $Y_{[n]}$ indexed by $\Pi_{i} \subset[i-1]$. For $i \in[m]$, the parent set of $U_{i}$ is the sub-vector $Y_{P_{i}}$ of $Y_{[n]}$ where $P_{i} \subseteq[n]$ is the non empty set mentioned above and thus each utility node has at least one parent. Furthermore any two $P_{i}$ 's are assumed disjoint so that each component of $Y_{[n]}$ is parent of at most one utility node. There are three types of edges in an MID:

1. those into $U$ vertices: for $i \in[m], U_{i}$ has no children and its parent set $Y_{P_{i}}$ is described above;
2. those into $\mathbb{D}$ vertices: for $i \in \mathbb{D}$, the parent set of $Y_{i}$ consists of the variables, controlled and non-controlled that are known when $Y_{i}$ is controlled;
3. those into $\mathbb{V}$ vertices: for $i \in \mathbb{V}$, the parent set of $Y_{i}$ is such that $Y_{i}$ is conditionally independent (with respect to the probability law in Definition 1) of the random variables preceding it given its parents and for all instantiations of decisions preceding $Y_{i}$.
Recalling that $\Pi_{i} \subset[i-1]$, Item (3) above can be formulated as $Y_{i} \Perp Y_{[i-1]} \mid Y_{\Pi_{i}}$, where $\Perp$ denotes the extended conditional independence operator [19]. This means that standard conditional independence, namely $Y_{i} \Perp Y_{[i-1] \cap \mathbb{V}} \mid Y_{\Pi_{i} \cap \mathbb{V}}$, holds for all instantiations of the decision variables $Y_{[i-1] \cap \mathbb{D}}$ preceding $Y_{i}$. The transition probability function for the random vector $Y_{\mathbb{V}}$ in Definition 1 is given in terms of probability density as the product of
![img-0.jpeg](img-0.jpeg)

Fig. 1 An MID consisting of two decision nodes, $Y_{1}$ and $Y_{4}$, four random nodes, $Y_{2}, Y_{3}, Y_{5}$ and $Y_{6}$, and three utility nodes, $U_{1}, U_{2}$ and $U_{3}$

$P_{i}\left(y_{i} \mid y_{\Pi_{i}}\right)=P\left(Y_{i}=y_{i} \mid Y_{\Pi_{i}}=y_{\Pi_{i}}\right)$ for $i \in \mathbb{V}$. Note that $y_{\Pi_{i}}$ includes instantiations of controlled variables as well as random variables.

Example 2 The edge set of the MID in Fig. 1 is such that no variable is observed before controlling $Y_{1}$, whilst $Y_{1}, Y_{2}$ and $Y_{3}$ are observed before controlling $Y_{4}$ since $\Pi_{4}=\{1,2,3\}$. Furthermore its DAG implies that $Y_{5} \Perp Y_{1}, Y_{2} \mid Y_{3}, Y_{4}$ and $Y_{6} \Perp Y_{1}, Y_{2}, Y_{3} \mid Y_{4}, Y_{5}$. The parent sets of the utility nodes are $P_{1}=\{3\}, P_{2}=\{5\}$ and $P_{3}=\{4,6\}$.

The third component of an MID is a utility function $U$ defined over $\mathcal{Y}_{[n]}$ as

$$
U\left(y_{[n]}\right)= \begin{cases}\sum_{i \in[m]} k_{i} U_{i}\left(y_{P_{i}}\right), & \text { if } h=0 \\ \sum_{I \in \mathcal{P}_{0}([m])} h^{n_{I}-1} \prod_{i \in I} k_{i} U_{i}\left(y_{P_{i}}\right), & \text { otherwise }\end{cases}
$$

where $k_{i} \in(0,1)$ is a criterion weight [30]; as mentioned above $U_{i}$ is a function of the random and decision variables in $Y_{P_{i}}$. It gives the contribution to the utility function of the controlled and random variables in $Y_{P_{i}}$ and it does so linearly if $h=0$, i.e. the first case of (1). It is worthwhile recalling that the $Y_{P_{i}}$ 's are disjoint. In the second case of (1) $h$ is the unique non-zero solution not smaller than minus one to

$$
1+h=\prod_{i \in[m]}\left(1+h k_{i}\right)
$$

and $\mathcal{P}_{0}(\cdot)$ denotes the power set without the empty set, $n_{I}$ is the number of elements in the set $I$. For $h=0$, the multiplicative factorisation of an MID, $U\left(y_{[n]}\right)$, is a weighted sum of the terms $U\left(y_{P_{i}}\right)$ : thus coinciding with the class of commonly used additive factorizations [29]. Therefore the methodology we develop here applies to utility factorizations of additive form, or additive IDs, as well. For $h \neq 0$ the function $U\left(y_{[n]}\right)$ is a linear combination of all square free products of the $U_{i}$ 's (excluding 1). The $h$ balances the weight of the interaction terms: the larger $h$ is, the bigger is the impact of high order terms.

Example 3 The multiplicative utility factorization associated to the MID in Fig. 1, for $h \neq 0$ and leaving the functions' arguments implicit, can be written as
$U=k_{1} U_{1}+k_{2} U_{2}+k_{3} U_{3}+h k_{1} k_{2} U_{1} U_{2}+h k_{1} k_{3} U_{1} U_{3}+h k_{2} k_{3} U_{2} U_{3}+h^{2} k_{1} k_{2} k_{3} U_{1} U_{2} U_{3}$.
This expression emphasizes the generality of multiplicative utilities, since an additive utility is obtained by setting $h=0$ and is the sum of the first three terms.

Item 1 above, describing the edges into the utility nodes, extends the total order over $Y_{[n]}$ to $V(G)$. Indeed for $i, j \in[m], U_{i}$ succeeds $U_{j}$ and $i>j$ if there exists a parent of $U_{i}$ which succeeds all parents of $U_{j}$ in the order $\preceq$ over $Y_{[n]}$ : formally, if there is a $k \in P_{i}$ such that for every $l \in P_{j}, k>l$. For $i \in[m]$, let $j_{i}$ be the highest index of $P_{i}$ and $\mathbb{J}=\left\{j_{1}, \ldots, j_{m}\right\}$. The set $\mathbb{J}$ of the greatest parents of the utility nodes in $\preceq$ is fundamental for the Algorithm 4.2 in Section 4.3 because it allows for the computation of the least number of expected utilities by processing a $U_{i}$ in the algorithm only when strictly necessary. The Maple ${ }^{\text {tu }}$ function CompJ in Appendix B. 1 computes the set $\mathbb{J}$ for a given MID. The totally ordered sequence of $V(G)$ is called decision sequence (DS) of the MID $G$ and is denoted by $S:=\left(Y_{1}, \ldots, Y_{j_{1}}, U_{1}, Y_{j_{1}+1}, \ldots, Y_{j_{m}}, U_{m}\right)$. As in [3], we do not introduce utility nodes only at the end of the DS. This enables us to base the choice of optimal decisions, through the algorithm given below, only on the values of the relevant attributes.

Example 4 The DS of the MID in Fig. 1 is $\left(Y_{1}, Y_{2}, Y_{3}, U_{1}, Y_{4}, Y_{5}, U_{2}, Y_{6}, U_{3}\right)$ with $j_{1}=3$, $j_{2}=5, j_{3}=6$ and thus $\mathbb{J}=\{3,5,6\}$.

# 3.2 Evaluation of MIDs 

In this section we set the background for an efficient symbolic algorithm for evaluating an MID, namely for computing the expected value of (1) for all possibile decisions $y_{\mathbb{D}} \in Y_{\mathbb{D}}$ and identifying a sequence of optimal decisions that maximizes it. We do this by exploiting the sequential structure of (1) which by linearity is transferred to its EU function. However, this can be done only for MIDs in extensive form [42], namely those MIDs whose topology is such that, for any index $j \in \mathbb{D}$, only variables that are known at the time the DM makes the decision $Y_{j}$ have an index lower than $j$. This is because the evaluation will output optimal decisions as functions of observed quantities only [44]. Extensive form is thus a property referring to the edges into the decision variables of an MID.

Definition 2 An MID $G$ is said to be in extensive form if $Y_{i}$ is a parent of $Y_{j}, j \in \mathbb{D}$, for all $i<j$.

Example 5 The MID in Fig. 1 is in extensive form since $\Pi_{4}=\{1,2,3\}$. If either the edge $\left(Y_{2}, Y_{4}\right)$ or $\left(Y_{3}, Y_{4}\right)$ were deleted then the MID would not be in extensive form.

We first study MIDs in extensive form and only in Section 5 we consider manipulations of non extensive MIDs which turn them into extensive form. Without loss of generality we assume that any vertex corresponding to a variable in $Y_{[n]}$ has at least one child. Indeed, random and controlled vertices with no children could simply be deleted from the graph without changing the outcome of the evaluation [32]. In Example 5 the only vertices with no children are utility nodes.

A typical way to evaluate an MID in extensive form is through a backward inductive algorithm on the vertices of the DAG. We present a computationally efficient version of this algorithm, which at each step only utilises the strictly necessary utility nodes. The identification of the optimal policy is based on the computation of the functions $\tilde{U}_{i}\left(y_{B_{i}}\right)$, $i \in[n]$, which are formally introduced in Proposition 1 and each of which depends only on the variables in $Y_{[n]}$ that are strictly required for an MID evaluation. For $i \in[n]$, the set

$$
B_{i}=\left\{\bigcup_{\substack{k \geq i \\ k \in \mathbb{V}}} \Pi_{k} \bigcup_{\substack{j \geq i \\ j \in \mathbb{J}}} P_{j}\right\} \backslash\{i, \ldots, n\}
$$

defines the index sets of the subset of $Y_{[n]}$ which appear as arguments of $\tilde{U}_{i}$. The function CompBi in Appendix B. 1 computes the $B_{i}$ 's given the definition of an MID. Specifically a set $B_{i}$ includes only indices smaller than $i$ that are either in the parent set of a random variable $Y_{k}, k>i$, following $Y_{i}$ in the DAG or in a set $P_{j}$ such that $U_{j}$ succeeds $Y_{i}$ in the DS of the MID.

Example 6 For the MID in Fig. 1 the set $B_{5}=\{3,4\}$ since $B_{5}=\left\{\Pi_{6} \cup \Pi_{5} \cup P_{3} \cup P_{2}\right\} \backslash\{5,6\}$, $\Pi_{6}=\{4,5\}, \Pi_{5}=\{3,4\}, P_{3}=\{4,6\} P_{2}=\{5\}$, whilst $B_{4}=\{3\}$ since $B_{4}=\left\{\Pi_{5} \cup \Pi_{6} \cup\right.$ $\left.P_{2} \cup P_{3}\right\} \backslash\{4,5,6\}=B_{5} \backslash\{4\}$.

Proposition 1 The optimal decision associated to an MID yields EU equal to $\bar{U}_{1}\left(y_{B_{1}}\right)$ obtained with a backward recursion as follows. For $i \in[n]$ the function $\bar{U}_{i}\left(y_{B_{i}}\right)$ is defined according to whether $Y_{i}$ is a decision or a random variable as

$$
\bar{U}_{i}\left(y_{B_{i}}\right)= \begin{cases}\bar{U}_{i, \mathbb{D}}\left(y_{B_{i}}\right), & \text { if } i \in \mathbb{D} \\ \bar{U}_{i, \mathbb{V}}\left(y_{B_{i}}\right), & \text { if } i \in \mathbb{V}\end{cases}
$$

and three cases are distinguished

1. for $i=n$ either

$$
\begin{aligned}
& \bar{U}_{n, \mathbb{D}}\left(y_{B_{n}}\right)=\max _{\mathcal{Y}_{n}} k_{m} U_{m}\left(y_{P_{m}}\right) \quad \text { or } \\
& \bar{U}_{n, \mathbb{V}}\left(y_{B_{n}}\right)=\sum_{y_{n} \in \mathcal{Y}_{n}} k_{m} U_{m}\left(y_{P_{m}}\right) P_{n}\left(y_{n} \mid y_{\Pi_{n}}\right)
\end{aligned}
$$

2. for $i \in[n-1], i \in \mathbb{J}$ and $i \in P_{i}$, then either

$$
\begin{aligned}
& \bar{U}_{i, \mathbb{D}}\left(y_{B_{i}}\right)=\max _{\mathcal{Y}_{i}}\left(h k_{l} U_{l}\left(y_{P_{l}}\right) \bar{U}_{i+1}\left(y_{B_{i+1}}\right)+k_{l} U_{l}\left(y_{P_{l}}\right)+\bar{U}_{i+1}\left(y_{B_{i+1}}\right)\right) \text { or } \\
& \bar{U}_{i, \mathbb{V}}\left(y_{B_{i}}\right)=\sum_{y_{i} \in \mathcal{Y}_{i}}\left(h k_{l} U_{l}\left(y_{P_{l}}\right) \bar{U}_{i+1}\left(y_{B_{i+1}}\right)+k_{l} U_{l}\left(y_{P_{l}}\right)\right. \\
& \left.+\bar{U}_{i+1}\left(y_{B_{i+1}}\right)\right) P_{i}\left(y_{i} \mid y_{\Pi_{i}}\right),
\end{aligned}
$$

3. for $i \in[n-1]$ and $i \notin \mathbb{J}$ either

$$
\begin{aligned}
& \bar{U}_{i, \mathbb{D}}\left(y_{B_{i}}\right)=\max _{\mathcal{Y}_{i}} \bar{U}_{i+1}\left(y_{B_{i+1}}\right) \quad \text { or } \\
& \bar{U}_{i, \mathbb{V}}\left(y_{B_{i}}\right)=\sum_{y_{i} \in \mathcal{Y}_{i}} \bar{U}_{i+1}\left(y_{B_{i+1}}\right) P_{i}\left(y_{i} \mid y_{\Pi_{i}}\right)
\end{aligned}
$$

All maxima and summations in Proposition 1 are over one $\mathcal{Y}_{i}$ sample space only. For example (3) consists of either a marginalization or a maximization over $\mathcal{Y}_{n}$ since $Y_{n}$ is a parent of $U_{m}$ by construction. The proof of Proposition 1 is in Appendix A.1. Since the algorithm in Proposition 1 consists of a backward inductive routine, its complexity is at best $O(n \exp (t))$ as in standard dynamic programming evaluation of influence diagrams [46], where $n$ is the number of vertices and $t$ is the so called treewidth of the ID [32].

Example 7 To illustrate Proposition 1, we follow the algorithm for the first three steps of the evaluation of the MID in Fig. 1. Since the variable with the highest index, $Y_{6}$, is random, the backward induction procedure in Proposition 1 starts using the summation case of (3), specifically

$$
\bar{U}_{6}\left(y_{B_{6}}\right)=\bar{U}_{6, \mathbb{V}}\left(y_{4}, y_{5}\right)=\sum_{y_{6} \in \mathcal{Y}_{6}} k_{3} U_{3}\left(y_{4}, y_{6}\right) P\left(y_{6} \mid y_{4}, y_{5}\right)
$$

Next the algorithm considers another random variable, $Y_{5}$. Since 5 is the highest (and only) index in $P_{2}$, the backward induction is based on the summation in (4), which in this case equals

$$
\bar{U}_{5}\left(y_{B_{5}}\right)=\sum_{y_{5} \in \mathcal{Y}_{5}}\left(h k_{2} U_{2}\left(y_{5}\right) \bar{U}_{6}\left(y_{B_{6}}\right)+k_{2} U_{2}\left(y_{5}\right)+\bar{U}_{6}\left(y_{B_{6}}\right)\right) P\left(y_{5} \mid y_{3}, y_{4}\right)
$$

The backward induction has now reached $Y_{4}$, the first decision node. Although $Y_{4}$ is an

argument of a utility function, it is not the highest index in $P_{3}$ and thus the algorithm uses (5) as

$$
\tilde{U}_{4}\left(y_{B_{4}}\right)=\tilde{U}_{4, \mathbb{D}}\left(y_{3}\right)=\max _{y_{4} \in \mathcal{Y}_{4}} \tilde{U}_{5}\left(y_{B_{5}}\right)
$$

We now arrange the EUs, that describe the effectiveness of the available decisions, in a vector as follows.

Definition 3 We define the EU vector $\tilde{U}_{i}, i \in[n]$, as

$$
\tilde{U}_{i}=\left(\tilde{U}_{i}\left(y_{B_{i}}\right)\right)_{y_{B_{i}} \in \mathcal{Y}_{B_{i}}}^{\mathrm{T}}
$$

# 3.3 Polynomial structure of expected utility 

Generalizing work in $[9,18]$, we introduce a symbolic representation of both the probabilities and the utilities of an MID. For $i \in \mathbb{V}, j \in[m], y \in \mathcal{Y}_{i}, \pi \in \mathcal{Y}_{\Pi_{i}}$ and $\sigma \in \mathcal{Y}_{P_{j}}$, we define the parameters

$$
p_{i y \pi}=P\left(Y_{i}=y \mid Y_{\Pi_{i}}=\pi\right) \quad \text { and } \quad \psi_{j \sigma}=U_{j}(\sigma)
$$

The first index of $p_{i y \pi}$ and $\psi_{j \sigma}$ refers to the random variable and utility vertex to which the parameter is related, respectively. The second index of $p_{i y \pi}$ relates to the state of the random variable, whilst the third one to the parents' instantiation. The second index of $\psi_{j \sigma}$ corresponds to the instantiation of the arguments of the utility function $U_{j}$. We take the indices within $\pi$ and $\sigma$ to be ordered from left to right in decreasing order, so that e.g. $p_{6101}$ for the diagram of Fig. 1 corresponds to $P\left(Y_{6}=1 \mid Y_{5}=0, Y_{4}=1\right)$. The probability and utility vectors are given by $p_{i}=\left(p_{i y \pi}\right)_{y \in \mathcal{Y}_{i}, \pi \in \mathcal{Y}_{\Pi_{i}}}^{\mathrm{T}}$ and $\psi_{j}=\left(\psi_{j \pi}\right)_{\pi \in \mathcal{Y}_{P_{j}}}^{\mathrm{T}}$, respectively. Parameters are listed within $p_{i}$ and $\psi_{j}$ according to a reverse lexicographic order over their indices [16]. ${ }^{3}$ In contrast to [6], we use different symbols for utilities and probabilities. This is not only because these are formally different, but also because sensitivity methods can be tailored for these two types of indeterminates separately [35].

Example 8 The symbolic parametrization of the MID in Fig. 1 is summarized in Table 1. This is completed by the definition of the criterion weights $k_{i}$ and $h$ as in (1)-(2). In Appendix B. 5 we report the symbolic definition of this MID using our Maple ${ }^{r n}$ code.

Because probabilities sum to one, for each $i$ and $\pi$ one of the parameters $p_{i y \pi}$ can be written as one minus the sum of the others. Another constraint is induced by (2) on the criterion weights. However, unless otherwise indicated, we take all the parameters to be unconstrained. Any unmodelled constraint can be added subsequently when investigating the geometric features of the admissible domains [35], i.e. regions of the parameters' space over which the preferred strategy does not change.

In the above parametrization, $\tilde{U}_{i}$ consists of a vector of polynomials expressed in the unknown quantities $p_{i j \pi}, \psi_{j \sigma}, k_{i}$ and $h$, whose characteristics are specified in Theorem 1.

Theorem 1 For an MID $G$ and $i \in[n]$, let $c_{i}=\prod_{j \in B_{i}} r_{j}, U_{l}$ be the first utility node following $Y_{i}$ in the $D S$ of $G$ and, for $l \leq j \leq m$, $w_{i j}$ be the number of random nodes

[^0]
[^0]:    ${ }^{3}$ Let $\alpha, \beta \in \mathbb{Z}^{n}$. We say that $\alpha$ precedes $\beta$ in reverse lexicographic order if the right-most non zero entry of $\alpha-\beta$ is positive.

Table 1 Parameterization associated to the MID in Fig. 1

$$
\begin{aligned}
& p_{2}=\left(p_{211}, p_{201}, p_{210}, p_{200}\right)^{\mathrm{T}} \\
& p_{3}=\left(p_{3111}, p_{3011}, p_{3101}, p_{3001}, p_{3110}, p_{3010}, p_{3100}, p_{3000}\right)^{\mathrm{T}} \\
& p_{5}=\left(p_{5111}, p_{5011}, p_{5101}, p_{5001}, p_{5110}, p_{5010}, p_{5100}, p_{5000}\right)^{\mathrm{T}} \\
& p_{6}=\left(p_{6111}, p_{6011}, p_{6101}, p_{6001}, p_{6110}, p_{6010}, p_{6100}, p_{6000}\right)^{\mathrm{T}} \\
& \psi_{1}=\left(\psi_{11}, \psi_{10}\right)^{\mathrm{T}}, \psi_{2}=\left(\psi_{21}, \psi_{20}\right)^{\mathrm{T}}, \psi_{3}=\left(\psi_{311}, \psi_{301}, \psi_{310}, \psi_{300}\right)^{\mathrm{T}}
\end{aligned}
$$

between $Y_{i}$ and $U_{j}$ (including $Y_{i}$ ) in the $D S$ of $G$. Then $\bar{U}_{i}$ is a vector of dimension $c_{i}$ whose entries are polynomials including, for $a=l, \ldots, m$ and $b=l, \ldots, a, r_{i b a}$ monomials $m_{i b a}$ of degree $d_{i b a}$, where

$$
r_{i b a}=\binom{a-l}{b-l} \prod_{j=i}^{j_{a}} r_{j}, \quad d_{i b a}=(b-l)+2(b-l+1)+w_{i a}, \quad m_{i b a}=h^{b-l} m_{i b a}^{\prime}
$$

with $m_{i b a}^{\prime}$ a square-free monomial of degree $2(b-l+1)+w_{i a}$.
The proof of Theorem 1 is given in Appendix A.2. Equation (7) defines the structure of the polynomials $\bar{U}_{i}$ of the EU. Specifically, a polynomial is specified once its coefficients and its support (i.e. monomials which form the polynomial) are known. By structure of a polynomial we mean the number of monomials in its support and the number of monomials having a certain degree (sum of exponents). An algorithm for computing the polynomials in Theorem 1 is presented in Section 4, whose operations utilise the polynomial structure of EUs. If the MID has one decision node only, then the entries of the EU vector correspond to the pieces defined in [6].

Example 9 For the MID of Fig. 1 the polynomial structure of the entries of $\bar{U}_{5}$ can be constructed as follows. From $B_{5}=\{3,4\}$ it follows that $c_{5}=4$. Thus, $\bar{U}_{5}$ is a column vector of dimension 4 . From $U_{2} \equiv U_{l}$ it follows that

$$
r_{522}=2, r_{523}=4, r_{533}=4, d_{522}=3, d_{523}=4, d_{533}=7
$$

using the fact that $w_{52}=1$ and $w_{53}=2$. All monomials are square-free because the index $b$ of $r_{i b a}$ in Theorem 1 is either equal to $l$ or $l+1$. Each entry of $\bar{U}_{5}$ is a square free polynomial of degree seven consisting of ten monomials: two of degree 3 , four of degree 4 and four of degree 7 .

Since additive utility factorizations can be seen as special cases of multiplicative ones by setting $h=0$, it follows that the EU polynomials of an additive ID are square-free.

Corollary 1 In the notation of Theorem 1, the $E U \bar{U}_{i}, i \in[n]$, of an additive ID $G$ is a vector of dimension $c_{i}$ whose entries are square free polynomials of degree $w_{i m}+2$ including, for $a=l, \ldots, m, r_{i a}$ monomials of degree $w_{i a}+2$, where $r_{i a}=\prod_{j=i}^{j_{a}} r_{j}$.

Proof This follows directly from Theorem 1, since an additive factorization can be derived by setting $n_{1}-1$, the exponent of $h$ in (1), equal to zero. This corresponds to fixing $b=l$ in Theorem 1.

So far we have assumed that the DM has not provided any numerical specification of the uncertainties and the values involved in the decision problem. This occurs for example

if the system is defined through sample distributions of data from different experiments, where probabilities are only known with uncertainty. But in practice sometimes the DM is able to elicit the numerical values of some parameters. These numerical values can then simply be substituted to the corresponding probability and utility parameters in the system of polynomials constructed in Theorem 1 employing e.g. a computer algebra system. In such a case the degree of the polynomials and possibly the number of their monomials can decrease dramatically. We present in Section 7 different plausible numerical specifications of the parameters associated with the MID in Fig. 1, and investigate how the outputs of the MID differ for the different quantifications.

# 4 The symbolic algorithm 

In this section we develop an algorithm based on three operations which exploit the polynomial structure of EUs and use only linear algebra calculus. The Maple ${ }^{T H}$ code for their implementation is reported in Appendix B.3. ${ }^{4}$ In contrast to other probabilistic symbolic algorithms (e.g. [10]), our procedure sequentially computes only monomials that are part of the EU polynomials and is thus much more efficient.

### 4.1 A new algebra for MIDs

We need to introduce two procedures entailing a change of dimension of probability, utility and EU vectors, named EUDuplicationPsi and EUDuplicationP. These are required in order to multiply parameters associated to compatible instantiations only, i.e. if the common conditioning variables associated to the parameters are instantiated to the same value.

Example 10 In Algorithm 4.2 we will need to compute the Schur (or element-wise) product $\circ$ between the probability vector $p_{6}$ and the utility vector $\psi_{3}$. However, as specified in Table 1, $p_{6}$ has length 8 , whilst $\psi_{3}$ has length 4 . This is because $Y_{5}$ is a parent of $Y_{6}$ but not an argument of $U_{3}$. EUDuplicationPsi will then be needed to transform $\psi_{3}$ to

$$
\left(\psi_{311}, \psi_{301}, \psi_{311}, \psi_{301}, \psi_{310}, \psi_{300}, \psi_{310}, \psi_{300}\right)
$$

so that $p_{6} \circ \psi_{3}$ equals to

$$
\begin{aligned}
& \left(\psi_{311} p_{6111}, \psi_{301} p_{6011}, \psi_{311} p_{6101}, \psi_{301} p_{6001}\right. \\
& \left.\psi_{310} p_{6110}, \psi_{300} p_{6010}, \psi_{310} p_{6100}, \psi_{300} p_{6000}\right)
\end{aligned}
$$

The above vector then only includes entries associated to compatible instantiations.
For conciseness, we detail here only the EUDuplicationPsi procedure and refer to Appendix B. 2 for the code of both procedures. The steps of EUDuplicationPsi are shown in Algorithm 4.1. For a vector $\psi$, let $\psi^{s, t}$ be the subvector of $\psi$ including the entries from $s \cdot(t-1)+1$ to $s \cdot t$, for suitable $s, t \in \mathbb{Z}_{\geq 1}$. For $i \in[n-1]$ and $j \in[m]$, the procedure takes 7 elements as input: an $\mathrm{EU} \tilde{U}_{i+1}$; the utility vector associated to the utility node preceding $Y_{i+1}, \psi_{j}$; their dimensions, $c_{i+1}$ and $b_{j}$; the sets $B_{i+1}$ and $P_{j}$; the dimensions of all the probability vectors of the MID, $r=\left(r_{1}, \ldots, r_{n}\right)^{\mathrm{T}}$.

[^0]
[^0]:    ${ }^{4}$ Some inputs of the Maple ${ }^{T H}$ functions in Appendix B. 3 are different from those used in this section which are chosen to illustrate the procedure as concisely as possible.

Algorithm $4.1 \mathrm{EUDUPlicationPSI}\left(\widetilde{\boldsymbol{U}}_{i+1}, \boldsymbol{\Psi}_{j}, B_{i+1}, P_{j}, \boldsymbol{r}, c_{i+1}, b_{j}\right)$


For all indices smaller than $i$ and not in $B_{i+1} \cap P_{j}$, Algorithm 4.1 computes a positive integer number $w_{k}$ equal to the product of the dimension of the probability vectors with index bigger than $k$ belonging to $B_{i+1} \cup P_{j}$. The index $k$ is either in $B_{i+1}$ or in $P_{j}$. When $k \in B_{i+1}$, each block of $w_{k}$ rows of $\psi_{j}$ is consecutively duplicated $r_{k}-1$ times.

The first of the three operations we introduce is EUMultiSum, which computes a weighted multilinear sum between a utility vector and an EU. In the algorithm of Section 4.3, an EUMultiSum operation is associated to every utility vertex of the MID. This operation is required to formally assess the impact of a utility vertex to the overall EU and corresponds to a symbolic version of the sums in (4). Let $P=\left\{P_{1}, \ldots, P_{m}\right\}$.

Definition 4 (EUMultiSum) For $i \in[n]$, let $\bar{U}_{i+1}$ be an EU vector and $\psi_{j}$ the utility vector of node $U_{j}, j \in[m]$, succeeding $Y_{i}$ in the DS. The EUMultiSum, $+{ }^{E U}$, between $\bar{U}_{i+1}$ and $\psi_{j}$ is defined as

1. $\bar{U}_{i+1}^{\prime}, \psi_{j}^{\prime} \leftarrow$ EUDuplicationPsi $\left(\bar{U}_{i+1}, \psi_{j}, B_{i+1}, P_{j}, r, c_{i+1}, b_{j}\right)$;
2. $h \cdot k_{j} \cdot\left(\bar{U}_{i+1}^{\prime} \circ \psi_{j}^{\prime}\right)+k_{j} \cdot \psi_{j}^{\prime}+\bar{U}_{i+1}^{\prime}$, where $\circ$ and $\cdot$ denote respectively the Schur (or element-wise) and the scalar products.

The second operation, EUMarginalization is applied to any random vertex of the MID. This operation is the symbolic equivalent of marginalizations (sums) $\sum_{y_{i} \in \mathcal{Y}_{i}}$ in Proposition 1, often called variable elimination in the literature [39].

Definition 5 (EUMarginalization) For $i \in \mathbb{V}$, let $\bar{U}_{i+1}$ be an EU vector and $p_{i}$ a probability vector. The EUMarginalization, $\Sigma^{E U}$, between $\bar{U}_{i+1}$ and $p_{i}$ is defined as

1. $\bar{U}_{i+1}^{\prime}, p_{i}^{\prime} \leftarrow$ EUDuplicationP $\left(\bar{U}_{i+1}, p_{i}, \Pi_{i}, P, r, B_{i+1}, \mathbb{J}\right)$;

2. $I_{i, \mathrm{~V}} \times\left(\bar{U}_{i+1}^{\prime} \circ p_{i}^{\prime}\right)$, where $\times$ is the standard matrix product and $I_{i, \mathrm{~V}}$ is a matrix with $c_{i+1} s_{i} / r_{i} \in \mathbb{Z}_{\geq 1}{ }^{5}$ rows and $c_{i+1} s_{i}$ columns defined as

$$
I_{i, \mathrm{~V}}=((10 \cdots 0)(01 \cdots 0) \cdots(00 \cdots 1))^{\mathrm{T}}
$$

where 1 and 0 denote row vectors of dimension $r_{i}$ with all entries equal to one and zero respectively and $s_{i}=\prod_{k \in\left\{\Pi_{i} \backslash B_{i+1}\right\}} r_{k}$.

The last operation is a selection of a decision policy $y_{i} \in \mathcal{Y}_{i}$ in $\bar{U}_{i+1}, i \in \mathbb{D}$, for every element of $\mathcal{Y}_{\Pi(i)}$.

Definition 6 (EUMaximization) For $i \in \mathbb{D}$, let $\bar{U}_{i+1}$ be an EU vector. An EUMaximization over $\mathcal{Y}_{i}, \max \frac{E U}{\mathcal{Y}_{i}}$, is defined by the following steps:

1. select a $y_{i}^{*}(\pi) \in \mathcal{Y}_{i}$, for $\pi \in \mathcal{Y}_{\Pi(i)}$;
2. $I_{i, \mathbb{D}} \times \bar{U}_{i+1}$, where $I_{i, \mathbb{D}}$ is a matrix with $c_{i+1} / r_{i} \in \mathbb{Z}_{\geq 1}$ rows and $c_{i+1}$ columns defined as

$$
I_{i, \mathbb{D}}=\left(\left(\begin{array}{llll}
e_{y_{i}^{*}(1)} & 0 & \cdots
\end{array}\right)\left(\begin{array}{llll}
0 & e_{y_{i}^{*}(2)} & \cdots
\end{array}\right)\left(\begin{array}{llll}
0 & 0 & \cdots & e_{y_{i}^{*}\left(c_{i+1} / r_{i}\right)}
\end{array}\right)\right)^{\mathrm{T}}
$$

where $e_{y_{i}^{*}(\pi)}, \pi \in\left[c_{i+1} / r_{i}\right]$, is a row vector of dimension $r_{i}$ whose entries are all zero but the one in position $y_{i}^{*}(\pi)$, which is equal to one.

Using the terminology of [2] and [25], EUMaximization finds its natural application in open-loop analyses, where one policy only is under scrutiny. In this case, the DM can simply fix the decision of interest and EUMaximization drops the polynomials associated to nonselected policies. ${ }^{6}$ Nevertheless, in closed-loop analyses, where policies can vary, and in standard evaluation methods the first item of Definition 6 is critical for EUMaximization. It is not within the scope of this paper to present a methodology to identify EU maximizing decisions. However, within our symbolic approach polynomial optimization and semialgebraic methods can be used to guide the optimization process [5]. In Section 7 we present an example of the insights that the symbolic definition gives during the maximization step of an evaluation.

Since all our operations simply consists of standard and matrix products, the complexity of the algorithm for the symbolic computation of EUs we introduce below can be deduced by establishing the number of multiplications associated to each EU-operation. Formally, an EUMultiSum consists of

$$
n_{i}^{\text {sum }}=c_{i+1} s_{i}\left(2+m_{i+1}\right)+1
$$

multiplications, where $m_{i+1}$ is the number of monomials in each entry of $\bar{U}_{i+1}, c_{i+1}$ is the dimension of $\bar{u}_{i+1}$ and $s_{i}$ is given in Definition 5. An EUMarginalization consists of

$$
n_{i}^{\operatorname{marg}}=c_{i+1} s_{i} m_{i+1}+\left(c_{i+1} s_{i}\right)^{2} / r_{i}
$$

multiplications (without considering the sparsity of the matrix $I_{i, \mathrm{~V}}$ ), where $r_{i}$ is the size of the sample space of $Y_{i}$. Exploiting the structure of the matrix $I_{i, \mathbb{D}}$, an EUMaximization can be coded so that it does not perform any multiplication.

[^0]
[^0]:    ${ }^{5}$ This is so since $c_{i+1}=r_{i} a_{i+1}$, for an $a_{i+1} \in \mathbb{Z}_{\geq 1}$.
    ${ }^{6}$ The Maple ${ }^{\text {TH }}$ function EUMaximization in Appendix B. 3 currently calls a subfunction Maximize, which randomly picks decisions. However, this can be modified to take into account a fixed policy given as input.

Therefore the EUMultiSum and EUMarginalization operations have complexity $O\left(n_{i}^{\text {sum }}\right)$ and $O\left(n_{i}^{\text {marg }}\right)$ respectively.

# 4.2 Polynomial interpretation of the operations 

Each of the above three operations changes the EU vectors and their entries in a specific way we formalize in Proposition 2.

Proposition 2 For $i \in[n-1]$, let $\tilde{U}_{i+1}$ be an EU vector whose entries have the polynomial structure of (7) and let $U_{j}$ be the vertex preceding $Y_{i+1}$ in the DS. Then in the notation of Theorem 1

- $\max _{\mathscr{D}_{i}} \tilde{U}_{i+1}$ has dimension $c_{i+1} / r_{i} \in \mathbb{Z}_{\geq 1}$ and its entries do not change polynomial structure;
- $\tilde{U}_{i+1}+{ }^{E U} \psi_{j}$ has dimension $c_{i+1} t_{i}$, where $t_{i}=\prod_{k \in\left[P_{j} \backslash B_{i+1}\right]} r_{k}$, and each of its entries consists of $r_{(i+1) b a}$ monomials of degree $d_{(i+1) b a}, r_{(i+1) b a}$ monomials of degree $d_{(i+1) b a}+3$ and one monomial of degree 2 ;
- $\tilde{U}_{i+1} \Sigma^{E U} p_{i}$ has dimension $c_{i+1} s_{i} / r_{i}$, where $s_{i}=\prod_{k \in\left[\Pi_{i} \backslash B_{i+1}\right]} r_{k}$, and each of its entries consists of $r_{i} r_{(i+1) b a}$ monomials of degree $d_{(i+1) b a}+1$.

This result directly follows from the definition of the above three operations. An illustration of Proposition 2 is given in Example 11 below.

### 4.3 An algorithm for the computation of an MID's expected utilities

The algorithm for the computation of an MID's EUs is given in Algorithm 4.2. It receives as input the DS of the MID, $S$, the sets $\mathbb{J}, \mathbb{V}$ and $\mathbb{D}$, and the vectors $p=\left(p_{1}, \ldots, p_{n}\right)^{\mathrm{T}}$, $\psi=\left(\psi_{1}, \ldots, \psi_{m}\right)^{\mathrm{T}}$ and $k=\left(k_{1}, \ldots, k_{m}, h\right)^{\mathrm{T}}$. The algorithm corresponds to a symbolic version of the backward induction procedure working over the elements of the DS explicated in Proposition 1. At each inductive step, a utility vertex is considered together with the variable that precedes it in the DS.
Algorithm 4.2 SYMBOLICEXPECTEDUTILITY $(\mathbb{J}, S, \boldsymbol{p}, \boldsymbol{\psi}, \boldsymbol{k}, \mathbb{V}, \mathbb{D})$

$$
\begin{aligned}
& \widetilde{\boldsymbol{U}}_{n+1}=(0) \\
& \text { for } k \leftarrow n \text { downto } 1 \\
& \text { do }\left\{\begin{array}{l}
\text { for } l \leftarrow m \text { downto } 1 \\
\text { then }\left\{\begin{array}{l}
\text { if } k=j_{l} \\
\text { then }\left\{\begin{array}{l}
\text { then } \\
\text { else }\left\{\begin{array}{l}
\widetilde{\boldsymbol{U}}_{k}=\max _{\mathscr{Y}_{k}}^{E U}\left(\widetilde{\boldsymbol{U}}_{k+1}+{ }^{E U} \boldsymbol{\psi}_{l}\right) \\
\text { else }\left\{\widetilde{\boldsymbol{U}}_{k}=\boldsymbol{p}_{k} \Sigma^{E U}\left(\widetilde{\boldsymbol{U}}_{k+1}+{ }^{E U} \boldsymbol{\psi}_{l}\right)\right.
\end{array}\right. \\
\text { return }\left(\widetilde{\boldsymbol{U}}_{1}\right)
\end{array}\right.
\end{aligned}
$$

In line (1) the $\mathrm{EU} \tilde{U}_{n+1}$ is initialized to (0), namely a vector of dimension one including a zero. Lines (2) and (3) index a reverse loop over the indices of the variables and the utility vertices respectively (starting from $n$ and $m$ ). If the current index corresponds to a variable

preceding a utility vertex in the DS (line 4), then the algorithm jumps to lines (5)-(7). Otherwise it jumps to lines (8)-(10). In the former case, the algorithm computes, depending on whether or not the variable is controlled (line 5), either an EUMaximization over $\mathcal{Y}_{k}$ (line 6) or an EUMarginalization (line 7) with $p_{k}$, jointly to an EUMultiSum with $\psi_{l}$. In the other case, EUMaximization and EUMarginalization operations are performed without EUMultiSum. The Maple ${ }^{\text {rn }}$ function SymbolicExpectedUtility in Appendix B. 4 is an implementation of Algorithm 4.2.

Example 11 For the MID in Fig. 1 the SymbolicExpectedUtility function first considers the random vertex $Y_{6}$ which precedes the utility vertex $U_{3}$ and therefore first calls the EUMultiSum function. For this MID

$$
P_{3}=\{4,6\}, t_{6}=4, \Pi_{6}=\{4,5\}, s_{6}=2
$$

Thus, first $\bar{U}_{7}$ is replicated four times (since $t_{6}=4$ ) via EUDuplicationPsi and

$$
\bar{U}_{7}+^{E U} \psi_{3}=\left(k_{3} \psi_{11} k_{3} \psi_{01} k_{3} \psi_{10} k_{3} \psi_{00}\right)^{\mathrm{T}}
$$

Then, the rhs of (8) is duplicated via EUDuplicationP (as $s_{6}=2$ ) and

$$
\bar{U}_{6}=I_{6, \mathrm{~V}} \times \bar{U}_{6}^{\prime} \circ p_{6}=\left(k_{3} \psi_{31 j} p_{61 i j}+k_{3} \psi_{30 j} p_{60 i j}\right)_{i, j=0,1}^{\mathrm{T}}
$$

where $\bar{U}_{6}^{\prime}$ is equal to the duplicated version of the rhs of (8). The vector $\bar{U}_{6}$ has dimension four and its entries include two monomials of degree 3 . Since the random vertex $Y_{5}$ is the unique parent of $U_{2}$ the SymbolicExpectedUtility function follows the same steps as before. EUMultiSum is called and

$$
\bar{U}_{5}^{\prime} \triangleq \bar{U}_{6}+^{E U} \psi_{2}=\left(h \cdot \bar{U}_{6}+1\right) \cdot k_{2} \circ\left(\psi_{21} \psi_{20} \psi_{21} \psi_{20}\right)^{\mathrm{T}}+\bar{U}_{6}
$$

The polynomial $\bar{U}_{5}^{\prime}$ is the sum of two monomials of degree 3 inherited from $\bar{U}_{6}$, of two monomials of degree 6 (from the first term on the rhs of (10)) and one monomial of degree 2 (from the last term on the rhs of (10)). Its dimension is equal to four since $c_{6}=4$ and $s_{5}=0$ (i.e. no EUDuplicationPsi is required). Thus, EUMultiSum manipulates the EU vector according to Proposition 2. The EUMarginalization function computes $\bar{U}_{5}=I_{5, \mathrm{~V}} \times$ $\left(\left(\bar{U}_{5}^{\prime} \bar{U}_{5}^{\prime}\right)^{\mathrm{T}} \circ p_{5}\right)$. Each entry of $\bar{U}_{5}$ has twice the number of monomials of the entries of $\bar{U}_{5}^{\prime}$ and each monomial of $\bar{U}_{5}$ has degree $d+1$, where $d$ is the degree of each monomial of $\bar{U}_{5}^{\prime}$ (whose entries are homogeneous polynomials). These vectors also have the same dimension since $t_{5}=2$ and $r_{5}=2$. Thus, this EUMarginalization changes the EU vector according to Proposition 2. The entry $\bar{U}_{5}\left(y_{3}, y_{4}\right)$, with $y_{3}, y_{4}=0,1$, of this EU can be shown to be equal to the sum of the terms in Table 2.

The algorithm then considers the controlled variable $Y_{4}$. Since $4 \notin \mathbb{J}, Y_{4}$ is not the argument of a utility function with the highest index and therefore the algorithm calls the EUMaximization function. Suppose the DM decides to fix $Y_{4}=1$ when $Y_{3}=1$ and $Y_{4}=0$ when $Y_{3}=0$. Then EUMaximization returns $\bar{U}_{4}=I_{4, \mathbb{D}} \times \bar{U}_{5}$, where $I_{4, \mathbb{D}}$ is a $2 \times 4$ matrix with ones in positions $(1,1)$ and $(2,4)$ and zeros otherwise. Proposition 2 is

Table 2 The utility funtion $\bar{U}_{5}$ is the sum of the three polynomials in this table

```
\(k_{2}\left(\psi_{21} p_{51 y_{4} y_{3}}+\psi_{20} p_{50 y_{4} y_{3}}\right)\)
\(k_{3}\left(\psi_{31 y_{4}} p_{611 y_{4}}+\psi_{30 y_{4}} p_{601 y_{4}}\right) p_{51 y_{4} y_{3}}+k_{3}\left(\psi_{31 y_{4}} p_{610 y_{4}}+\psi_{30 y_{4}} p_{600 y_{4}}\right) p_{50 y_{4} y_{3}}\)
\(h k_{2} k_{3}\left(\left(\psi_{31 y_{4}} p_{610 y_{4}}+\psi_{30 y_{4}} p_{600 y_{4}}\right) \psi_{20} p_{50 y_{4} y_{3}}+\left(\psi_{31 y_{4}} p_{611 y_{4}}+\psi_{30 y_{4}} p_{601 y_{4}}\right) \psi_{21} p_{51 y_{4} y_{3}}\right)
```

respected since the entries of $\tilde{U}_{4}$ have the same polynomial structure of those of $\tilde{U}_{5}$ and $\tilde{U}_{4}$ has dimension 2.

The SymbolicExpectedUtility function then applies in sequence the operations defined in Section 4.1. For the MID in Fig. 1 this sequentially computes the following quantities, assuming the DM fixed $Y_{1}=1$

$$
\begin{array}{ll}
\tilde{U}_{3}^{\prime}=h \cdot k_{1} \cdot \tilde{U}_{4} \circ \psi_{1}+\tilde{U}_{4}+k_{1} \cdot \psi_{1}, & \tilde{U}_{3}=I_{3, \mathbb{V}} \times\left(\left(\tilde{U}_{3}^{\prime} \tilde{U}_{3}^{\prime} \tilde{U}_{3}^{\prime} \tilde{U}_{3}^{\prime}\right)^{\mathrm{T}} \circ p_{3}\right) \\
\tilde{U}_{2}=I_{2, \mathbb{V}} \times\left(\tilde{U}_{3} \circ p_{2}\right), & \tilde{U}_{1}=(10) \times \tilde{U}_{2}
\end{array}
$$

The overall complexity of the algorithm can be formally deduced by counting the number of multiplications it involves. Given the number of such products for each of our EUoperations, the overall number of operations of Algorithm 4.2 is the sum of the multiplications of its operations and will depend on the topology of the ID network. Formally, letting

$$
n^{\mathrm{tot}}=\sum_{i \in[n]}\left(\mathbb{1}_{i \in \mathbb{V}} n_{i}^{\mathrm{marg}}+\mathbb{1}_{i \in \mathbb{J}} n_{i}^{\text {sum }}\right)
$$

where $\mathbb{1}$ denotes the indicator function, the overall complexity of our algorithm is $O\left(n^{\text {tot }}\right)$.

# 4.4 Simulation study 

To empirically investigate the complexity of the symbolic algorithm in Section 4.3, we perform a simulation study comprising of 5 IDs, whose features are summarized in Table 3 all with binary variables. We first produced a full symbolic definition of utilities and probabilities and then run our symbolic algorithm for both multiplicative and additive utility factorizations in Maple ${ }^{\text {m }}$. This gives as output the EU vectors $\tilde{U}_{i}$ associated to every random and decision nodes of the IDs. We also built the same networks using the GeNIe Modeler software of "BayesFusion, LLC" (freely available for academics at http://www. bayesfusion.com), which embeds numerical evaluation techniques for IDs. After building the networks in GeNIe, we specified numerical values for the probabilities and utilities and then ran the evaluation algorithm. It is important to highlight that GeNIe considers only additive factorizations between utility nodes.

The results of the study are summarized in Table 4. Whilst the memory allocated in Maple ${ }^{\text {m }}$ is almost identical for IDs with multiplicative and additive utility factorizations, the computation time as well as the number of monomials is much larger for MIDs. Comparing the computation times of GeNIe with those in Maple ${ }^{\text {m }}$, we notice that whilst these are of the same magnitude for smaller IDs, for larger networks GeNIe appears to become significantly

Table 3 Summaries of the IDs considered in the simulation study: Net. - ID identifier; Free par. - number of free parameters; \# $\mathbb{V}$ - number of random nodes; \# $\mathbb{D}$ - number of decision nodes; $m$ - number of utility nodes; \# $E(G)^{*}$ - number of edges without those into decision nodes; Avg. indegree - average number of edges directed into vertices (without decision nodes)


Table 4 Complexity summaries of the symbolic algorithms in Maple ${ }^{T H}$ and of the numerical algorithms in GeNIe: Mem. All. memory allocation; Time computation time; \# Mon. number of monomials of the final EU vectors $\hat{U}_{1}$


slower. However we underline that the two softwares produce different outputs: expected utility vectors with polynomial entries in Maple ${ }^{T H}$ and numerical evaluation of the ID in GeNIe.

Although the efficiency of the symbolic algorithms highly depends on the size of the network, the simulation study in this section shows that even with the current capabilities of general-purpose computer algebra softwares symbolic techniques in decision making problems of medium/large scale are usefully applicable. In particular for IDs embedding additive factorizations, computation times increase at a slower pace than in the other cases (GeNIe and MIDs) and could thus be efficiently implemented in much larger domains than those presented here. However, it is uncommon to perform sensitivity studies over networks much larger than those investigated here. We refer a discussion of the handling of massive networks in our symbolic framework to Section 8.

# 5 Modifying the topology of the MID 

Algorithm 4.2 works under the assumption that the MID is in extensive form whose importance was discussed in Section 3.2. It has been recognized that typically a DM will build an MID so that variables and decisions are ordered in the way they actually happen and this might not correspond to the order in which variables are observed. Thus, MIDs often are not in extensive form. But it is always possible to transform an MID into one in extensive form, although this might entail the loss of conditional independence structure. In Section 5.1 we consider two of the most common operations that can do this: edge reversal and barren node elimination.

In practice DMs often also include in the MID variables that subsequently turn out not to be strictly necessary for identifying an optimal policy. DMs are able to provide probabilistic judgements for conditional probability tables associated to an MID with variables describing the way they understand the unfolding of events. However their understanding usually includes variables that are redundant for the evaluation of the MID. In Section 5.2 we describe the polynomial interpretation of a criterion introduced in [42, 43] to identify a subgraph of the original MID whose associated optimal decision rule is the same as the one of the original MID.

### 5.1 Rules to transform an MID in extensive form

The two operations of arc reversal and barren node removal are often used in combination by first reversing the direction of some edges of the MID and then removing vertices that, consequently to the reversals, becomes barren, i.e. have no children [39].

Example 12 The MID on the left of Fig. 2 is a non-extensive variant of the MID in Fig. 1 not including the edge $\left(Y_{2}, Y_{4}\right)$. The MID in the centre of Fig. 2 is obtained by the reversal of the edge $\left(Y_{2}, Y_{3}\right)$ and the MID on the right of Fig. 2 is the network in extensive form obtained by deleting the barren node $Y_{2}$.

First we introduce a terminology to characterize a special pair of parent/child as in [11] for which edge reversals are simpler [36]. It is not the purpose of this paper to identify an optimal sequence of edge reversals, i.e. one yielding a simplified MID with the least number of vertices and edges. Instead we can use algorithms already devised for standard IDs to perform diagram transformations [40] by arc reversal and barren node removals. We say that $Y_{i}$ is the father of $Y_{j}$ and $Y_{j}$ its son if the edge set of the MID includes $\left(Y_{i}, Y_{j}\right)$ and there is no other path starting at $Y_{i}$ and terminating at $Y_{j}$ that connects them.

Example 13 For the MIDs in Fig. 2, both $Y_{4}$ and $Y_{5}$ are parents of $Y_{6}$, but only $Y_{5}$ is its father since there is the path $\left(Y_{4}, Y_{5}, Y_{6}\right)$. Notice that a vertex can have only one father but more than one son.

Proposition 3 The evaluation of an MID G provides the same optimal policy as the MID $G^{\prime}$ obtained by implementing any of the following manipulations:

- Arc Reversal: for $i, j \in \mathbb{V}$, if $Y_{i}$ is the father of $Y_{j}$ in $G$ reverse the $\operatorname{arc}\left(Y_{i}, Y_{j}\right)$ into $\left(Y_{j}, Y_{i}\right)$ and change the edge set as

$$
E\left(G^{\prime}\right)=E(G) \backslash\left\{\left(Y_{i}, Y_{j}\right)\right\} \cup\left\{\left(Y_{k}, Y_{i}\right): k \in\left\{\Pi_{j} \cup j\right\} \backslash i\right\} \cup\left\{\left(Y_{k}, Y_{j}\right): k \in \Pi_{i}\right\}
$$

- Barren Node Removal: for $i \in \mathbb{V}$, remove the vertex $Y_{i}$ if this has no children and transform the diagram according to the following rules:

$$
V\left(G^{\prime}\right)=V(G) \backslash\left\{Y_{i}\right\}, \quad E\left(G^{\prime}\right)=E(G) \backslash\left\{\left(Y_{k}, Y_{i}\right): k \in \Pi_{i}\right\}
$$

Arc reversal and barren node removal change the symbolic parametrization of the MID according to Proposition 4. After an arc reversal, the diagram $G^{\prime}$ includes the edge $\left(Y_{j}, Y_{i}\right)$ where $i<j$. Algorithm 4.2, and similarly the Maple ${ }^{t n}$ function SymbolicExpectedUtility, works through a backward induction over the indices of the variables and, by construction, always either marginalize or maximize a vertex before its parents. It cannot therefore be applied straightforwardly to the diagram $G^{\prime}$. We define here the adjusted Algorithm 4.2 which takes into account the reversal of an arc by, roughly speaking, switching the order in which the variables associated to the reversed edge are marginalized during the procedure. Specifically, in the adjusted Algorithm 4.2 a marginalization operation is performed over $Y_{i}$ at the $n-j+1$ backward inductive step, whilst for $Y_{j}$ this happens at the $n-i+1$ step. Therefore $\tilde{U}_{j}^{\prime}$ is the EU associated to $G^{\prime}$ after the
![img-1.jpeg](img-1.jpeg)

Fig. 2 Example of a sequence of manipulations of a non extensive form MID

marginalization of $Y_{i}$ and $\bar{U}_{i}^{\prime}$ is the EU after the marginalization of $Y_{j}$. Note that under this operation the sets $\mathbb{J}$ and $B_{i}, i \in[n]$, might change: we respectively call $\mathbb{J}^{\prime}$ and $B_{i}^{\prime}$ the ones associated to $G^{\prime}$.

Proposition 4 Under the conditions of Proposition 3, let $p_{i y \pi}^{\prime}$ and $\Pi_{i}^{\prime}$ be a parameter and a parent set associated to the diagram $G^{\prime}$ resulting from arc reversal and barren node removal:

- for $i, j \in \mathbb{V}$, if $\Pi_{i}^{\prime}$ and $\Pi_{j}^{\prime}$ are the parent sets of $Y_{i}$ and $Y_{j}$ after the reversal of the edge $\left(Y_{i}, Y_{j}\right)$, then the parametrization associated to $G^{\prime}$ is

$$
p_{i y_{i} \pi_{i}^{\prime}}^{\prime}=\frac{p_{j y_{j} \pi_{j}} p_{i y_{i} \pi_{i}}}{\sum_{y_{i} \in \mathcal{Y}_{i}} p_{j y_{j} \pi_{j}} p_{i y_{i} \pi_{i}}}, \quad p_{j y_{j} \pi_{j}^{\prime}}^{\prime}=\sum_{y_{i} \in \mathcal{Y}_{i}} p_{j y_{j} \pi_{j}} p_{i y_{i} \pi_{i}}
$$

for $\pi_{i} \in \mathcal{Y}_{\Pi_{i}}, \pi_{j} \in \mathcal{Y}_{\Pi_{j}}, \pi_{i}^{\prime} \in \mathcal{Y}_{\Pi_{i}^{\prime}}, \pi_{j}^{\prime} \in \mathcal{Y}_{\Pi_{j}^{\prime}}, y_{i} \in \mathcal{Y}_{i}$ and $y_{j} \in \mathcal{Y}_{j}$;

- for $i, j \in \mathbb{V}$, assume that after the reversal of the edges $\left(Y_{i}, Y_{j}\right)$, for every children $Y_{j}$ of $Y_{i}, Y_{i}$ is now a barren node and let $\Pi_{j \backslash i}=\Pi_{j} \backslash\{i\}$. Then
- in the new parametrization $p_{i}^{\prime}$ is deleted;
- in the old parametrization $p_{i}$ is deleted and $p_{j y_{j} \pi_{j \backslash i} 0}=\cdots=p_{j y_{j} \pi_{j \backslash i} r_{i}-1}$, for $y_{j} \in \mathcal{Y}_{j}, \pi_{j \backslash i} \in \mathcal{Y}_{\Pi_{j \backslash i}}$, where the fourth index of $p_{j y_{j} \pi_{j \backslash i}}$, $i \in\left[r_{i}-1\right]$, refers to the instantiation of $Y_{i}$.

The proof of this proposition is reported in Appendix A.3.
Example 14 Reversing the edge $\left(Y_{2}, Y_{3}\right)$ in the MID on the left of Fig. 2, by Proposition 4 we obtain:

$$
p_{3 y_{3} y_{1}}^{\prime}=p_{3 y_{3} 1 y_{1}} p_{21 y_{1}}+p_{3 y_{3} 0 y_{1}} p_{20 y_{1}}, \quad p_{2 y_{2} y_{3} y_{1}}^{\prime}=\frac{p_{3 y_{3} y_{2} y_{1}} p_{2 y_{2} y_{1}}}{p_{3 y_{3} 1 y_{1}} p_{21 y_{1}}+p_{3 y_{3} 0 y_{1}} p_{20 y_{1}}}
$$

for $y_{1}, y_{2}, y_{3} \in\{0,1\}$. Proposition 4 also specifies that the deletion of the vertex $Y_{2}$ as on the right of Fig. 2 simply corresponds to cancelling the vectors $p_{2}$ and $p_{2}^{\prime}$ and setting $p_{3 y_{3} 1 y_{1}}$ equal to $p_{3 y_{3} 0 y_{1}}$ for any $y_{1}, y_{3} \in\{0,1\}$.

Note that arc reversals, just as posterior probabilities in symbolic inferences, transform EUs into rational functions of multilinear polynomials. However, Proposition 4 suggests a straightforward model's reparametrization, which maps EUs back to polynomial functions. In addition, Proposition 4 shows that manipulations of the diagram change the polynomial structure of the EUs under the new parametrization $p^{\prime}$ that we formally study in Lemmas 1 and 2 below. We assume here for simplicity that $i \notin P_{j}, j \in[m]$. There is no loss of generality in this assumptions since arguments of utility functions cannot be deleted from the diagram without changing the result of the evaluation.

Lemma 1 Under the assumptions of Proposition 4 and in the notation of Theorem 1, suppose we reverse the arc $\left(Y_{i}, Y_{j}\right)$ in an MID $G$. Let $x$ be the smallest index in $\Pi_{i} \cup \Pi_{j}$. Evaluating $G$ using the adjusted Algorithm 4.2 the following holds:

1. if $j \notin \mathbb{J}$, then

- the entries of $\tilde{U}_{j}^{\prime}$ have $r_{i} r_{j b a} / r_{j} \in \mathbb{Z}_{\geq 1}{ }^{7}$ monomials of degree $d_{j b a}$; for $i<k<$ $j$, the entries of $\tilde{U}_{k}^{\prime}$ can have different polynomial structure from the ones of $\tilde{U}_{k}$ according to Proposition 2;
- the vectors $\tilde{U}_{k}^{\prime}, x<k \leq j$, have dimension $c_{k}=\prod_{s \in C_{k} \backslash\{k, \ldots, n\}} r_{s}$ where $C_{k}=$ $B_{k} \cup\left\{l:\left(Y_{l}, Y_{i}\right)\right.$ or $\left.\left(Y_{l}, Y_{j}\right) \in E\left(G^{\prime}\right)\right\}$;

2. if $j \in \mathbb{J} \cap \mathbb{J}^{\prime}$, then

- the entries of $\tilde{U}_{j}^{\prime}$ have $r_{i} r_{(j+1) b a}$ monomials of degree $d_{(j+1) b a}+1$ and, for $i<$ $k<j$, the entries of $\tilde{U}_{k}^{\prime}$ have a different polynomial structure from the ones of $\tilde{U}_{k}$ according to Proposition 2;
- for $x<k<j, \tilde{U}_{k}^{\prime}$ has dimension $a_{k}=\prod_{s \in\left[A_{k} \backslash\{k, \ldots, n\}\right\}} r_{s}$, with $A_{k}=C_{k} \cup P_{j_{j}}$;

3. if $j \notin \mathbb{J}^{\prime}$, suppose $j \in P_{t}$ and $s$ is the second highest index in $P_{t}$, then

- for $s<k \leq j$, the entries of $\tilde{U}_{k}^{\prime}$ have the polynomial structure specified in point 2 and dimension $a_{k}$;
- $i<k \leq s$, the entries of $\tilde{U}_{k}^{\prime}$ have the polynomial structure specified in point 1 and dimension $c_{k}$.
- for $x<k \leq i, \tilde{U}_{k}^{\prime}$ has dimension $c_{k}$ and the polynomial structure of its entries does not change;

The proof of this lemma is provided in Appendix A.4.
We next consider how a barren node removal changes the EU vectors.
Lemma 2 In the notation of Lemma 1, let $Y_{z}$ be the child of $Y_{i}$ in $G$ with the highest index and remove the barren node $Y_{i}$ in $G^{\prime}$. Then

- for $i<k \leq z, \tilde{U}_{k}^{\prime}$ has $c_{k} / r_{i}$ entries whose polynomial structure does not change;
- for $k \leq i, \tilde{U}_{k}^{\prime}$ has dimension $c_{k}$ and its entries have $r_{k b a} / r_{i}$ monomials of degree $d_{k b a}-$ 1 .

The proof of this lemma is provided in Appendix A.4.
Example 15 After the reversal of the edge $\left(Y_{2}, Y_{3}\right)$ from the network on the left of Fig. 2, the polynomial structure of the EUs associated to the original and manipulated diagrams is reported in Table 5 by $\tilde{U}_{i}$ and $\tilde{U}_{i}^{r}$ respectively. Since $Y_{3}$ is the only argument of $U_{1}$ we are in Item (2) of Lemma 1. The EU $\tilde{U}_{3}^{r}$ is obtained running the adjusted Algorithm 4.2 over the graph in the centre of Fig. 2 after the marginalization of $Y_{2}$. This can be noted to change according to Lemma 1, by comparing its structure to the one of $\tilde{U}_{4}$. Furthermore, $\tilde{U}_{2}^{r}$ and $\tilde{U}_{1}^{r}$ have the same polynomial structures as $\tilde{U}_{2}$ and $\tilde{U}_{1}$. The last 3 columns of the Table 5 show the polynomial structure of the EUs $\tilde{U}_{3}^{b}$ associated to the MID on the right of Fig. 2 which does not include $Y_{2}$. According to Lemma 1, $\tilde{U}_{3}^{b}$ has the same polynomial structure of $\tilde{U}_{3}$ and for each row of the table, the number of monomials with degree $d$ in $\tilde{U}_{1}^{b}$ is half the number of monomials of $\tilde{U}_{1}$ having degree $d+1$.

[^0]
[^0]:    ${ }^{7}$ This is so since $r_{j b a}=r^{\prime} r_{j}$ for some $r^{\prime} \in \mathbb{Z}_{\geq 1}$.

Table 5 Polynomial structure of the EUs for the original MID, $\tilde{U}_{j}$, for the one after the reversal of the arc $\left(Y_{2}, Y_{3}\right), \tilde{U}_{j}^{r}$ and for the one after the removal of the barren node $Y_{2}, \tilde{U}_{j}^{b}$. The symbol \# corresponds to the number of monomials, d. to the degree and s.f. to whether or not they are square free


# 5.2 The sufficiency principle 

After an MID has been transformed in extensive form according to the rules in Section 5.1, further manipulations can be applied to simplify its evaluation, such as the sufficiency principle, which mirrors the concept of sufficiency in statistics and is based on the concept of d-separation for DAGs [37] formally defined below.

We first introduce a few concepts from graph theory. The moralized graph $G^{M}$ of the MID $G$ is a graph with the same vertex set of $G$. Its directed edges include the directed edges of $G$ and an undirected edge between any two vertices which are not joined by an edge in $G$ but which are parents of the same child in $Y_{i}, i \in \mathbb{V}$. The skeleton of $G^{M}, \mathcal{S}\left(G^{M}\right)$, is a graph with the same vertex set of $G^{M}$ and an undirected edge between any two vertices $\left(Y_{i}, Y_{j}\right) \in V\left(G^{M}\right)$ if and only if there is a directed or undirected edge between $Y_{i}$ and $Y_{j}$ in $G^{M}$.

Definition 7 For any three disjoint subvectors $Y_{A}, Y_{B}, Y_{C} \in V\left(G^{M}\right), Y_{A}$ is $d$-separated from $Y_{C}$ by $Y_{B}$ in the moralized graph $G^{M}$ of an MID $G$ if and only if any path from any vertex $Y_{a} \in Y_{A}$ to any vertex $Y_{c} \in Y_{C}$ passes through a vertex $Y_{b} \in Y_{B}$ in its skeleton $\mathcal{S}\left(G^{M}\right)$.

Proposition 5 Let $j \in \mathbb{D}, i \in \mathbb{V} \cap \Pi_{j}$ and $C h_{i}$ be the index set of the children of $Y_{i}$. Then if $Y_{i}$ is d-separated from $\left\{U_{k}\right.$, for $k$ s.t. $\left.i \leq j_{k}\right\}$ by $\left\{Y_{k}: k \in\left\{\Pi_{j} \backslash i\right\}\right\} \cup\left\{Y_{k}: k \in \mathbb{D}\right\}$ in the MID $G$, the sufficiency principle guarantees that the evaluation of the graph $G^{\prime}$ provides the same optimal policy as $G$, where $G^{\prime}$ is such that $V\left(G^{\prime}\right)=V(G) \backslash\left\{Y_{i}\right\}$ and $E\left(G^{\prime}\right)$ is equal to

$$
E(G) \backslash\left\{\left(Y_{i}, Y_{j}\right): j \in C h_{i}\right\} \backslash\left\{\left(Y_{k}, Y_{i}\right): k \in \Pi_{i}\right\} \cup\left\{\left(Y_{k}, Y_{j}\right): j \in C h_{i}, k \in \Pi_{i}\right\}
$$

The sufficiency principle can be equally stated for a vector of variables [42, 43]. However, we can simply apply the criterion in Proposition 5 for each variable of the vector and obtain the same result.

Example 16 The MID in Fig. 1 is already moralized. Any path from $Y_{2}$ into $U_{i}, i \in[3]$, goes through both $Y_{3}$ and $Y_{4}$. By Proposition 5, we can delete $Y_{2}$ and the modified diagram

is given on the right of Fig. 2. This happens to be equal to the diagram resulting from the reversal of the $\operatorname{arc}\left(Y_{2}, Y_{3}\right)$ and the deletion of $Y_{2}$.

We now formalize how this principle changes our parametrization.
Proposition 6 Let $i, j, k \in \mathbb{V}$ and $G$ be an MID. Let $Y_{i}$ be a vertex removed after the application of the sufficiency principle to $G$ and $G^{\prime}$ the obtained MID. Assume $Y_{i}$ to be the father of $Y_{k}$ and a parent (not the father) of $Y_{j}$ in $G$ and let $\Pi_{k}^{\prime}$ be the parent set of a vertex $Y_{k}$ in $G^{\prime}$. Then the reparametrization of the MID with graph $G^{\prime}$ is

$$
\begin{aligned}
& p_{k y_{k} \pi_{k}^{\prime}}^{\prime}=\sum_{y_{i} \in \mathcal{Y}_{i}} p_{k y_{k} \pi_{k}} p_{i y_{i} \pi_{i}} \\
& p_{j y_{j} \pi_{j}^{\prime}}^{\prime}=\sum_{y_{j} \in \mathcal{Y}_{j}} p_{j y_{j} \pi_{j}} \frac{\prod_{l \in \Pi_{j} \backslash[i-1]} \sum_{\mathcal{Y}_{\Pi_{l} \cap \Pi_{k} \cap \Pi_{i}}} p_{l y_{l} \pi_{l}} p_{i y_{i} \pi_{i}}}{\sum_{y_{i} \in \mathcal{Y}_{i}} \prod_{l \in \Pi_{j} \backslash[i-1]} \sum_{\mathcal{Y}_{\Pi_{l} \cap \Pi_{k} \cap \Pi_{i}}} p_{l y_{l} \pi_{l}} p_{i y_{i} \pi_{i}}}
\end{aligned}
$$

The proof of this proposition is provided in Appendix A.5. Again, this new parametrization $p^{\prime}$ implies a change in the EU vectors.

Lemma 3 Assume the vertex $Y_{i}$ is removed using the sufficiency principle and that $Y_{j}$ is the child of $Y_{i}$ with the highest index. Under the notation of Theorem 1 the EU vectors in $G^{\prime}$ are such that

1. for $k<i$, the entries of $\tilde{U}_{k}^{\prime}$ have $r_{k b a} / r_{i}$ monomials of degree $d_{k b a}-1$, whilst for $k>i$ their structure does not change.
2. for $k \leq j, \tilde{U}_{k}$ has now dimension $\prod_{s \in C_{k}} r_{s}$, where $C_{k}=B_{k} \cup \Pi_{i} \backslash\{k, \ldots, n\}$, whilst for $k>j$ its dimension does not change.

Proof Item 1 of Lemma 3 is a straightforward consequence of Proposition 2, since the deletion of the vertex $Y_{i}$ entails one less EUMarginalization during Algorithm 4.2. Item 2 of Lemma 3 follows from the fact that the sets $B_{k}$ and $C_{k}$ only affect the dimension of the EU vectors.

Since the application of the sufficiency principle to the diagram of Fig. 1 provides the same output network as the one obtained from the reversal of the edge $\left(Y_{2}, Y_{3}\right)$ and the removal of $Y_{2}$, an illustration of these results can be found in Table 5.

# 6 Asymmetric decision problems 

The new symbolic representation of decision problems we introduce here enables us to concisely express a large amount of information that might not be apparent from an ID. Different types of extra information, often consisting of asymmetries of various kinds, have been explicitly modelled in graphical extensions of the ID model [3, 4, 20, 28, 41] and are found in the descriptions of many applied decision problems. Although providing a framework for the evaluation of more general decision problems, many of these extensions lose the intuitiveness and the simplicity associated with IDs. Within our symbolic approach we are able to elegantly and concisely characterize asymmetric decision problems through manipulations of the polynomials representing the ID's EU as we show next.

Asymmetries can be categorized in three classes. If the possible outcomes or decision options of a variable vary depending on the past, the asymmetry is called functional. If the very occurrence of a variable depends on the past, the asymmetry is said to be structural. Order asymmetries are present if $\left\{Y_{i}: i \in \mathbb{D}\right\}$ is not totally ordered. In this section we only deal with functional asymmetries. Heuristically, for a functional asymmetry the observation of $y_{A}, A \subset[n]$, restricts the space $\mathcal{Y}_{B}$ associated to a vector $Y_{B}$, such that $A \cap B=\emptyset$. This new space, $\mathcal{Y}_{B}^{\prime}$ say, is a subspace of $\mathcal{Y}_{B}$.

In Theorem 2 we characterize an asymmetry between two chance nodes and, depending on the stage of the evaluation, this may entail setting equal to zero monomials in either some or all the rows of the EU vector. We present the result for elementary asymmetries of the following form: if $Y_{i}=y_{i}$ then $Y_{j} \neq y_{j}$. Composite asymmetries are unions of simple asymmetries and the features of the EU vectors in more general cases can be deduced through a sequential application of Theorem 2.

Theorem 2 Let $G$ be an MID, $Y_{i}$ and $Y_{j}$ be two random variables with $j>i, U_{x}$ be the utility node following $Y_{j}$ in the DS. Assume the asymmetry $Y_{i}=y_{i} \Rightarrow Y_{j} \neq y_{j}$ holds and that $k$ and $z$ are the highest indices such that $j \in B_{k}$ and $i \in B_{z}$ and assume $k>j$. Then

- for $j<t \leq z, \tilde{U}_{t}$ has $\prod_{s \in B_{t} \backslash[i \cup j]} r_{s}$ rows with no monomials;
- for $i<t \leq j, \tilde{U}_{t}$ has $\prod_{s \in B_{t} \backslash[i]} r_{s}$ rows with polynomials all with a different structure. Specifically, these consists, in the notation of Theorem 1, of $s_{t b a}$ monomials of degree $d_{t b a}$, where, for $a=x, \ldots, m$ and $b=l, \ldots, a$,

$$
s_{t b a}=\left(\binom{a-x}{b-l}-1\right) \prod_{s=t}^{j_{a}} r_{s} / r_{j}
$$

- for $t \leq i$, each row of $\tilde{U}_{t}$ has in the notation of Theorem $1, f_{t b a}$ monomials of degree $d_{t b a}$, where for $a=x, \ldots, m$ and $b=l, \ldots, a$

$$
f_{t b a}=\left(\binom{a-x}{b-l}-1\right) \prod_{s=t}^{j_{a}} r_{s} /\left(r_{j} \cdot r_{i}\right)
$$

The proof of this theorem is provided in Appendix A.6. Corollary 2 gives a characterization of simple asymmetries between any two variables, whether they are controlled or non-controlled. This follows from Theorem 2 since controlled variables can be thought of as a special case of random ones.

Corollary 2 In the notation of Theorem 1 and under the assumptions of Theorem 2, with the difference that $Y_{i}$ and $Y_{j}$ are two variables, controlled or non-controlled, we have that

- for $j<t \leq z$, each row of $\tilde{U}_{t}$ has $\prod_{s \in B_{t} \backslash[i \cup j]} r_{s}$ rows with no monomials;
- for $i<t \leq j, \tilde{U}_{t}$ has at most $\prod_{s \in B_{t} \backslash[i]} r_{s}$ rows with polynomials all with a different structure. Specifically, these consists of between $s_{t b a}$ and $r_{t b a}$ monomials of degree $d_{t b a}$, for $a=x, \ldots, m$ and $b=l, \ldots, a$;
- for $t \leq i$, some rows of $\tilde{U}_{t}$ have a number of monomials of degree $d_{t b a}$ between $f_{t b a}$ and $r_{t b a}$, for $a=x, \ldots, m$ and $b=l, \ldots, a$.

Example 17 (Example 4 continued) Assume that the DM believes the decision problem is characterized by three composite asymmetries:

- if $Y_{1}$ was fixed to 1 , then $Y_{4}=1$ cannot be chosen;
- if either $Y_{2}$ or $Y_{3}$ were observed to be equal to 1 then $Y_{5}=1$;
- if $Y_{4}=1$ then both $Y_{5}$ and $Y_{6}$ are equal to 1 .

A graphical representation of these asymmetries is given in Fig. 3, in the form of a sequential influence diagram [28]. Asymmetries are represented as labels on new dashed arcs. If the asymmetry is composite, then vertices can be grouped through a dashed ellipse and dashed arcs can either start or finish by the side of these ellipses. Although this generalization of the MID in Fig. 1 graphically captures the asymmetries, most of its transparency is now lost. Instead asymmetries have the opposite effect on our polynomial representation of MIDs by greatly simplifying the structure of the EUs.

In this asymmetric framework the first row of $\bar{U}_{6}$ corresponds to $k_{3} \psi_{311} p_{6111}$, whilst its second row is empty. This is because according to Theorem 2 the monomial $k_{3} \psi_{301} p_{6011}$ in (9) is cancelled by the asymmetry $Y_{4}=1 \Rightarrow Y_{6}=1, k_{3} \psi_{311} p_{6101}$ by $Y_{4}=1 \Rightarrow Y_{5}=1$ and $k_{3} \psi_{301} p_{6001}$ by both asymmetries. The imposition of asymmetries further reduces from ten to three the number of monomials in $\bar{U}_{5}$ which becomes

$$
k_{3} \psi_{311} p_{6111} p_{511 i}+k_{2} \psi_{21} p_{511 i}+h k_{2} k_{3} \psi_{311} \psi_{21} p_{6111} p_{511 i}, \quad i=0,1
$$

Suppose the DM decided to fix $Y_{4}=0$ if $Y_{3}=1$ and $Y_{4}=1$ if $Y_{3}=0$. The entry of $\bar{U}_{3}$ for which $Y_{2}=1$ and $Y_{1}=1$ can be written as the sum of the terms

$$
\begin{gathered}
\left(k_{2} \psi_{21}+k_{3} \psi_{311} p_{6111}\left(1+k k_{2} \psi_{21}\right)\right) p_{5110} p_{3011}+k_{1}\left(\psi_{10} p_{3011}+\psi_{11} p_{3111}\right) \\
k k_{1} k_{3} \psi_{11} p_{5101} p_{3111}\left(\left(1+k_{2} \psi_{21}\right)\left(\psi_{300} p_{6010}+\psi_{310} p_{6110}\right)\right)
\end{gathered}
$$

This polynomial consists of only nine monomials. This compared with the number of monomials in the symmetric case, 42 (see Table 5), means that even in this small problem the number of monomials is decreased by over three quarters.

So the example above illustrates that under asymmetries the polynomial representation is simpler than standard methods but still able to inform decision centres about the necessary parameters to elicit. A more extensive discussion of the advantages of symbolic approaches in asymmetric contexts, although fully inferential ones, can be found in [24]. Finally it is
![img-2.jpeg](img-2.jpeg)

Fig. 3 Representation of the asymmetric version of the MID of Fig. 1 through a sequential influence diagram

possible to develop a variant of Algorithm 4.2 which explicitly takes into account the asymmetries of the problem during the computation of the EU vectors. Note that this approach would be computationally more efficient, since this would require the computation of a smaller number of monomials/polynomials.

# 7 An example 

In this section we study the polynomial features of the EUs associated to the MID in Fig 1. We focus on the selection of the decision variable $Y_{4}$ and consider two different scenarios in which the DM provides two different sets of information of the relevant parameters. In the first scenario the elicitation is complete, i.e. for each parameter the DM delivers the unique numerical value specified in the left hand side of Table 6. The second scenario combines unique probability specifications, symbolic parameters and qualitative information. Specifically the DM does not elicit $p_{5111}, p_{6001}, p_{6010}, p_{6011}$ and $\psi_{301}$, because e.g. there is strong uncertainty related to their values, specifies the two relationships $p_{5111}=p_{6011}$ and $p_{6001}=p_{6010}$ and assigns specific values to the remaining parameters as indicated in Table 6.

In the first scenario, using any standard propagation algorithm or by simply substituting the appropriate numerical values from Table 6 into the EU polynomial $\tilde{U}_{5}\left(y_{4}, y_{3}\right)$ from Table 2, the DM would be suggested to choose $Y_{4}=1$ if $Y_{3}=0$ and $Y_{4}=0$ if $Y_{3}=1$, since

$$
\tilde{U}_{5}(1,0)=0.4465, \tilde{U}_{5}(0,0)=0.4460 \text { and } \tilde{U}_{5}(1,1)=0.3074, \tilde{U}_{5}(0,1)=0.3755
$$

In an automated decision making process the DM might overlook the small difference in EU values when $Y_{3}=0$, which already suggests that small changes in parameters' values may lead to different preferred policies.

A symbolic study of EUs in the partial elicitation case of the second scenario can provide insights on why the DM's decision making may not be robust. Substituting the partial numeric specification in Table 6 into the polynomial from Table 2 yields

$$
\begin{aligned}
\tilde{U}_{5}\left(y_{4}, y_{3}\right) & =0.2 p_{50 y_{4} y_{3}}+0.4\left(\psi_{31 y_{4}} p_{611 y_{4}}+\psi_{30 y_{4}} p_{601 y_{4}}\right) p_{51 y_{4} y_{3}} \\
& +0.472\left(\psi_{31 y_{4}} p_{610 y_{4}}+\psi_{30 y_{4}} p_{600 y_{4}}\right) p_{50 y_{4} y_{3}}
\end{aligned}
$$

Table 6 Complete and partial specification of the parameters associated to MID in Fig. 1 for the optimization step over $Y_{4}$. By the sum-to-one condition $p_{6001}=p_{6010}$ is equivalent to $p_{6101}=p_{6110}$

## Parameters' specifications


![img-3.jpeg](img-3.jpeg)

Fig. 4 Admissible domains, expressed in the unknowns $\psi_{301}, p_{6001}$ and $p_{5111}$, for the combinations of parameters leading to a preferred decision $Y_{4}=0$ (coloured regions) and $Y_{4}=1$ (white regions) for the MID in Fig. 1 given the partial numeric specification in Table 6
which is further specialised in

$$
\begin{aligned}
& \hat{U}_{5}(1,1)=0.2\left(1-p_{5111}\right)+0.4 \psi_{301} p_{5111}^{2}+0.472 \psi_{301} p_{6001}\left(1-p_{5111}\right) \\
& \hat{U}_{5}(0,1)=0.100976+0.6192 p_{6001} \\
& \hat{U}_{5}(1,0)=0.16+0.08 \psi_{301} p_{5111}+0.3776 p_{6001} \\
& \hat{U}_{5}(0,0)=0.233984+0.6192 p_{6001}
\end{aligned}
$$

Under the partial specification scenario, the admissible domains when $Y_{3}=1$, namely $\arg \max \left\{\hat{U}_{5}(1,1), \hat{U}_{5}(0,1)\right\}$, are reported on the left hand side of Fig. 4 and the associated indifference surface is defined by the equation $\hat{U}_{5}(1,1)=\hat{U}_{5}(0,1)$. The right hand side of Fig. 4 shows the admissible domains when $Y_{3}=0$. For $Y_{3}=1$, the combination of values elicited by the DM is well inside the colored region, whilst for $Y_{3}=0$ it is very closed to the indifference surface defined by the points where the DM is indifferent between the two policies. The indifference surface for $Y_{3}=0$ is very smooth and regular since the associated variety is defined by a simple multilinear polynomial. Conversely, the surface for $Y_{3}=1$ exhibits more interesting features since the associated variety is defined by a quadratic function.

Additional information about the DM's decision problem can be gained by investigating the admissible domains defined by two parameters only, when the third one is fixed to the value chosen in the complete elicitation scenario. In Fig. 5 we report the regions for $Y_{3}=0$. The admissible domains are very "smooth" and the indifference surfaces are all monotonic functions. In all the plots the complete elicitation point is very close to the indifference curve and thus small perturbations of the parameters can lead to a different preferred policy. Much more robust is the DM's potential decision in the case $Y_{3}=1$, since all the complete elicitation points are well inside the admissible domains (reported in Fig. 6). Note how in this

Fig. 5 Admissible domains for subsets of 2 elements of the parameter space for $Y_{3}=0$, fixing the third to the value of the complete elicitation (colored for $Y_{4}=0$ and white for $Y_{4}=1$ )
![img-4.jpeg](img-4.jpeg)

Fig. 6 Admissible domains for subsets of 2 elements of the parameter space for $Y_{3}=1$, fixing the third to the value of the complete elicitation (colored for $Y_{4}=0$ and white for $Y_{4}=1$ )
![img-5.jpeg](img-5.jpeg)

case the admissible domains have a much more complex geometry, due to the polynomial structure of the indifference surface variety. We highlight a few points from this example:

- the geometry of the admissible regions has provided insights on the decision making process. In much more complex problems, tools of algebraic geometry [16] can still be used to guide DMs and to uncover even more surprising features;
- although other approaches allow for non exact probability specifications, our symbolic characterization provides a straightforward platform to input qualitative information, e.g. equality of two parameters, which entails a simple reparametrization of the problem;
- the symbolic approach is particularly efficient for this type of sensitivity studies since a DM can simply plug-in different combinations of values for the unknowns and instantaneously observe the results. In full numerical domains, the propagation of EUs would need to performed for each combination of values and this can become computationally very expensive;
- if, after robustness studies as the one in this example, the DM is still not convinced about a preferred course of action, our algorithm can be adapted to run separately for each admissible domain back to the root of the MID. In this way it would then output the admissible regions for each multivariate available policy together with its defining polynomial;
- the identification of the admissible domains consists of the solution of a system of polynomial inequalities. We are currently investigating these domains using semi-algebraic methods [5];
- all these methods are especially informative in asymmetric domains, since different policies can be associated to polynomial having very different properties. This is because, as shown in Theorem 2, in contast to standard MIDs, different policies can be associated with very differently structured polynomials.


# 8 Discussion 

With this work we have developed symbolic methods - currently being successfully applied to the analysis of probabilistic graphical models - to study MIDs. We have defined a complete toolkit to deal with standard operations for MIDs from a symbolic point of view, such as the computations of EUs, possible manipulations of the diagram and asymmetries. Whilst in open-loop analyses our symbolic definition finds its natural application, in closed-loop analyses the EU-Maximization operation becomes critical. In some specific cases, as illustrated through the example in Section 7, partial parameters' elicitations will allow the DM to perform such step. In more general cases we still need to formalize such maximization techniques for example by adopting semi-algebraic methods which have already proved successful in other applications [5]. We expect these to be particularly useful in asymmetric domains, since different polynomial structures can inform even more deeply the DM about the structure of the decision space.

We here provide a full report of an implementation of our methodology within an accessible computer algebra system. Of course when addressing very large problems generic tools can have difficulties handling the number of unknown variables that need to be stored in the computer memory and computations may become infeasible. However, there are ways around this memory problem. For example by imposing certain conditions on the model - formally discussed in [34] - computations can then be distributed. This can dramatically reduce complexity and make calculations again feasible albeit with the necessary addition of further software - designed for the particular application - which intelligently merges

together the outputs of the different contributing distributed components of the system: see also [45]. The simulations carried out in Section 4.4 and the example in Section 7 showed that the methodology and algorithm presented in this paper are competitive and allow for the analysis of more general classes of models than traditional methods. Implementations based on specialised programs rather than on a general purpose software like Maple ${ }^{r H}$ will enable the analysis of more complex MIDs.

Also in the case the variables take values in continuous spaces, EU exhibits a similar polynomial representation to the one discussed in this paper for discrete variables. In the continuous case the unknown quantities of the polynomials are low order moments. Examples of these polynomials are presented in [34]. Just as in the discrete case, the manipulations of the diagrams for policies with continuous variables and their associated asymmetries can be described as operations over the polynomials. A full study of the symbolic representation of EUs in a continuous domain will be reported in future work.

# Appendix A Proofs 

## A. 1 Proof of proposition 1

We develop the proof via backward induction over the random and decision vertices of the MID, starting from $Y_{n}$. Define, for $i \in[n]$,

$$
\hat{U}_{i}=\int_{\mathcal{Y}_{[n]_{i-1}^{\mathbb{V}}}} \max _{\mathcal{Y}_{[n]_{i-1}^{\mathbb{D}}}} \sum_{I \in \mathcal{P}_{[i([m])}} h^{n_{I}-1} \prod_{i \in I} k_{i} U_{i}\left(y_{P_{i}}\right) f\left(y_{[n]_{i-1}^{\mathbb{V}}} \mid y_{[i-1]}\right) \mathrm{d} y_{[n]_{i-1}^{\mathbb{V}}}
$$

where $[n]_{i-1}^{\mathbb{V}}=[n] \backslash[i-1] \cap \mathbb{V},[n]_{i-1}^{\mathbb{D}}=[n] \backslash[i-1] \cap \mathbb{D}$ and $\Pi_{[n]_{i-1}^{\mathbb{V}}}=\cup_{j \in[n]_{i-1}^{\mathbb{V}}} \Pi_{j}$. The quantity $\hat{U}_{i}$ corresponds to an overall EU score after having marginalized/maximized $Y_{i}, \ldots, Y_{n}$.

The DM's preferences are a function of $Y_{n}$ only through $k_{m} U_{m}\left(y_{P_{m}}\right)$, since by construction $n=j_{m} \in \mathbb{J}$. Therefore this quantity can be either maximized or marginalized as in (3) to compute $\tilde{U}_{n}\left(y_{B_{n}}\right)$. Note that $B_{n}$ includes only the indices of the variables $\tilde{U}_{n}$ formally depends on, since $B_{n}=P_{m} \backslash\{n\}$, if $n \in \mathbb{D}$, whilst $B_{n}=P_{m} \cup \Pi_{n} \backslash\{n\}$, if $n \in \mathbb{V}$. Then

$$
\hat{U}_{n}=\sum_{I \in \mathcal{P}_{[i([m])}} h^{n_{I}-1} \prod_{i \in I}\left(\mathbb{1}_{[i \neq n]}\left[k_{i} U_{i}\left(y_{P_{i}}\right)\right]+\mathbb{1}_{[i=n]}\left[\tilde{U}_{i}\left(y_{B_{i}}\right)\right]\right)
$$

Now consider $Y_{n-1}$. If $n-1 \notin \mathbb{J}$, then $\hat{U}_{n}$ is a function of $Y_{n-1}$ only through $\tilde{U}_{n}$. Therefore maximization and marginalization steps can be computed as in (5) to compute $\tilde{U}_{n-1}\left(y_{B_{n-1}}\right)$. Again $B_{n-1}$ includes the indices of the variables $\tilde{U}_{n-1}$ formally depends on, since $B_{n-1}=$ $P_{m} \backslash\{n, n-1\}$, if $n, n-1 \in \mathbb{D}, B_{n-1}=P_{m} \cup \Pi_{n} \cup \Pi_{n-1} \backslash\{n, n-1\}$, if $n, n-1 \in \mathbb{V}$, $B_{n-1}=P_{m} \cup \Pi_{n-1} \backslash\{n, n-1\}$, if $n \in \mathbb{D}$ and $n-1 \in \mathbb{V}, B_{n-1}=P_{m} \cup \Pi_{n} \backslash\{n, n-1\}$, if $n \in \mathbb{V}$ and $n-1 \in \mathbb{D}$. Then

$$
\hat{U}_{n-1}=\sum_{I \in \mathcal{P}_{[i([m])}} h^{n_{I}-1} \prod_{i \in I}\left(\mathbb{1}_{[i \neq n]} k_{i} U_{i}\left(y_{P_{i}}\right)+\mathbb{1}_{[i=n]} \tilde{U}_{i-1}\left(y_{B_{i-1}}\right)\right)
$$

Conversely, if $n-1 \in \mathbb{J}, \hat{U}_{n}$ is potentially a function of $Y_{n-1}$ through both $U_{m-1}\left(y_{P_{m-1}}\right)$ and $\tilde{U}_{n}\left(y_{B_{n}}\right)$ and note that $\tilde{U}_{n}$ can be written in this case as
$\hat{U}_{n}=\sum_{I \in \mathcal{P}_{0}([m-2])} h^{n_{I}-1} \prod_{i \in I} k_{i} U_{i}\left(y_{P_{i}}\right)+U_{m-1}^{\prime}+\left(\sum_{i \in \mathcal{P}_{0}([m-2])} h^{n_{i}-1} \prod_{i \in I} k_{i} U_{i}\left(y_{P_{i}}\right)\right) U_{m-1}^{\prime}$,
where

$$
U_{m-1}^{\prime}=h k_{m-1} U_{m-1}\left(y_{P_{m-1}}\right) \tilde{U}_{n}\left(y_{B_{n}}\right)+k_{m-1} U_{m-1}\left(y_{P_{m-1}}\right)+\tilde{U}_{n}\left(y_{B_{n}}\right)
$$

Therefore optimization and marginalization steps can be performed over $U_{m-1}^{\prime}$ as specified in the two (4) respectively. Then note that $\hat{U}_{n-1}$ can be written as

$$
\begin{aligned}
\hat{U}_{n-1} & =\sum_{I \in \mathcal{P}_{0}([m-2])} h^{n_{I}-1} \prod_{i \in I} k_{i} U_{i}\left(y_{P_{i}}\right)+\tilde{U}_{n-1}(\cdot)+\left(\sum_{i \in \mathcal{P}_{0}([m-2])} h^{n_{i}-1} \prod_{i \in I} k_{i} U_{i}\left(y_{P_{i}}\right)\right) \tilde{U}_{n-1}(\cdot) \\
& =\sum_{I \in \mathcal{P}_{0}([m-1])} h^{n_{I}-1} \prod_{i \in I}\left(\mathbb{1}_{\{i \neq n-1\}} k_{i} U_{i}\left(y_{P_{i}}\right)+\mathbb{1}_{\{i=n-1\}} \tilde{U}_{i}\left(y_{B_{i}}\right)\right)
\end{aligned}
$$

Now for a $j \in[n-2]$ and assuming with no loss of generality that $k$ is the index of a utility vertex such that $j_{k-1}<j \leq j_{k}$, we have that

$$
\tilde{U}_{j}=\sum_{I \in \mathcal{P}_{0}([k])} h^{n_{I}-1} \prod_{i \in I}\left(\mathbb{1}_{\{i \neq j\}} k_{i} U_{i}\left(y_{P_{i}}\right)+\mathbb{1}_{\{i=j\}} \tilde{U}_{i}\left(y_{B_{i}}\right)\right)
$$

Therefore at the following step, when considering $Y_{j-1}$, we can proceed as done with $Y_{n-1}$ by maximization and marginalization in (4)-(5) to compute $\tilde{U}_{j-1}$. Thus at the conclusion of the procedure, $\tilde{U}_{1}$ yields the EU of the optimal decision.

# A. 2 Proof of theorem 1 

For a subset $I \in \mathcal{P}_{0}([m])$, let $j_{I}$ be the index of the variable appearing before the utility vertex with index $U_{\max _{I}}$ in the decision sequence. Let $C_{i, I}=\left\{z \in \mathbb{V}: i \leq z \leq j_{I}\right\}$ and recall that $l$ is the index of the first utility node following $Y_{i}$ in the DS. The EU function

of (3)-(5) can be (less intuitively) written as $\tilde{U}_{i}\left(y_{B_{i}}\right)=\sum_{I \in \mathcal{P}_{0}(\{l, \ldots, m\})} \tilde{U}_{i, I}\left(y_{B_{i}}\right)$, where $\tilde{U}_{i, I}\left(y_{B_{i}}\right)$ is defined as

$$
\tilde{U}_{i, I}\left(y_{B_{i}}\right)=\sum_{I \in \mathcal{P}_{0}(\{l, \ldots, m\})} h^{n_{I}-1} \prod_{s \in I} k_{s} U_{s}\left(y_{P_{s}}\right) \sum_{y_{C_{i, I}} \in \mathcal{Y}_{C_{i, I}}} \prod_{j \in C_{i, I}} P\left(y_{j} \mid y_{\Pi_{j}}\right)
$$

The EU therefore depends on the power set of the indices of the utility vertices subsequent to $Y_{i}$ in the decision sequence. We can note that for any $I, J \in \mathcal{P}(\{l, \ldots, m\})$ such that $\# I=\# J$ and $U_{\max _{I}}=U_{\max _{J}}, \tilde{U}_{i, I}\left(y_{B_{i}}\right)$ and $\tilde{U}_{i, J}\left(y_{B_{i}}\right)$ have the same polynomial structure since $C_{i, I}=C_{i, J}$. Now for $a=l, \ldots, m$ and $b=l, \ldots, a$, by the properties of binomial coefficients, $\binom{a-l}{b-l}$ counts the number of elements $I \in \mathcal{P}_{0}(\{l, \ldots, m\})$ having $\# I=b-l+1$ and including $a$. Thus $r_{i b a}$ in (7) counts the correct number of monomials having a certain degree since $\mathcal{Y}_{C_{i, I}}=\times_{t \in C_{i, I}} \mathcal{Y}_{t}$. Further note that considering each combination of $b$ and $a$ in the ranges specified above, we count each element of $\mathcal{P}_{0}(\{l, \ldots, m\})$.

By having a closer look at $d_{i b a}$ in (7) it is easy to deduce the corresponding degree of these monomials. The first term of $d_{i b a},(b-l)$, computes the degree associated to the criterion weight $h$, since $b-l=n_{I}-1$ and the second term, $2(b-l+1)$, computes the degree associated to the product between the criterion weights $k_{s}$ and the utilities $U_{s}\left(y_{P_{s}}\right)$ for $s \in C_{i, I}$. The last term $w_{i a}$ corresponds to the degree deriving from the probabilistic part of (11), which is equal to the number of non-controlled vertices between $Y_{i}$ and $Y_{j_{\max _{I}}}$ (both included).

Since the set $B_{i}$ includes the arguments of $\tilde{U}_{i}\left(y_{B_{i}}\right)$ and $\mathcal{Y}=\times_{i \in[n]} \mathcal{Y}_{i}$, (6) guarantees that the dimension of the EU vector is $\prod_{t \in B_{i}} r_{t}$.

# A. 3 Proof of proposition 4 

After the reversal of the arc $\left(Y_{i}, Y_{j}\right)$ into $\left(Y_{j}, Y_{i}\right)$, the new parent sets of these two variables are $\Pi_{j}^{\prime}=\left\{\Pi_{j} \cup \Pi_{i} \backslash i\right\}$ and $\Pi_{i}^{\prime}=\left\{j \cup \Pi_{i} \cup \Pi_{j} \backslash i\right\}$. Call $\Pi_{j \backslash i}=\left\{\Pi_{j} \backslash i\right\}$. It then follows that

$$
\begin{aligned}
p_{i y_{i} \pi_{i}^{\prime}} & =P\left(y_{i} \mid y_{\Pi_{i}^{\prime}}\right)=P\left(y_{i} \mid y_{\Pi_{j \backslash i}}, y_{\Pi_{i}}, y_{j}\right)=\frac{P\left(y_{j} \mid y_{\Pi_{j \backslash i}}, y_{\Pi_{i}}, y_{i}\right) P\left(y_{i} \mid y_{\Pi_{j \backslash i}}, y_{\Pi_{i}}\right)}{P\left(y_{j} \mid y_{\Pi_{j \backslash i}}, y_{\Pi_{i}}\right)} \\
& =\frac{P\left(y_{j} \mid y_{\Pi_{j}}\right) P\left(y_{i} \mid y_{\Pi_{i}}\right)}{P\left(y_{j} \mid y_{\Pi_{j \backslash i}}, y_{\Pi_{i}}\right)}=\frac{P\left(y_{j} \mid y_{\Pi_{j}}\right) P\left(y_{i} \mid y_{\Pi_{i}}\right)}{\sum_{y_{i} \in \mathcal{Y}_{i}} P\left(y_{j} \mid y_{i}, y_{\Pi_{j \backslash i}}\right) P\left(y_{i} \mid y_{\Pi_{i}}\right)} \\
& =\frac{p_{j y_{j} \pi_{j}} p_{i y_{i} \pi_{i}}}{\sum_{y_{i} \in \mathcal{Y}_{i}} p_{j y_{j} \pi_{j}} p_{i y_{i} \pi_{i}}}
\end{aligned}
$$

and

$$
\begin{aligned}
p_{j y_{j} \pi_{j}^{\prime}}^{\prime} & =P\left(y_{j} \mid y_{\Pi_{j}^{\prime}}\right)=P\left(y_{j} \mid y_{\Pi_{j \backslash i}}, y_{\Pi_{i}}\right)=\sum_{y_{i} \in \mathcal{Y}_{i}} P\left(y_{j} \mid y_{\Pi_{j}}\right) P\left(y_{i} \mid y_{\Pi_{i}}\right) \\
& =\sum_{y_{i} \in \mathcal{Y}_{i}} p_{j y_{j} \pi_{j}} p_{i y_{i} \pi_{i}}
\end{aligned}
$$

The proof of the barren node removal easily follows from the fact that the vertex is not included anymore in the MID.

## A. 4 Proof of lemma 1 and 2

We first consider the arc reversal and the change of dimension of the vectors. If $j \notin \mathbb{J}$ the sets $B_{k}$ that are affected by the arc reversal are only the ones such that $k \in \Pi_{i} \cup \Pi_{j}$ and the

set $B_{k}^{\prime}$ simply takes into account the presence of the additional edges in $G^{\prime}$. If $j \in \mathbb{J}^{\prime}$ then the sets $B_{k}$ affected by the arc reversal are the ones such that $k \in \Pi_{i} \cup \Pi_{j} \cup P_{j_{j}}$ and the set $B_{k}^{\prime \prime}$ additionally takes into account that the indices in $P_{j_{j}}$ are included only before the EUMarginalization between $\tilde{U}_{i+1}$ and $p_{j}$. The final case is if $j \notin \mathbb{J}^{\prime}$, which can be seen as a combination of the previous two cases.

Now consider the polynomial structure of the entries after an arc reversal. If $j \notin \mathbb{J}$, then the adjusted Algorithm 4.2 simply computes an EUMarginalization between $\tilde{U}_{j+1}$ and $p_{i}$ instead of $p_{j}$. Therefore the entries of $\tilde{U}_{j}$ have $r_{j b a}^{\prime}=r_{i} r_{(j+1) b a} / r_{j}$ monomials of degree $d_{(j+1) b a}$ and, until the adjusted algorithm computes $\tilde{U}_{i}$, the change in the structure is propagated through the 'EUOperations'. If $j \in \mathbb{J}^{\prime} \cap \mathbb{J}$, then instead of an EUMultiSum and a EUMarginalization, now the algorithm only computes an EU-Marginalization and, as before, the change is propagated until $\tilde{U}_{i}$. As in the previous paragraph, the last case can be seen as combination of the previous two situations.

Consider now the deletion of the barren node $Y_{i}$. The set $B_{z}$ is the one with the highest index which includes $i$ in $G$. Thus, for $i<k \leq z, i \in B_{k}$ and $\tilde{U}_{k}$ is conditional on $Y_{i}=y_{i}$. The deletion of this vertex therefore implies that the dimension of the vector becomes $c_{k}^{\prime} / r_{i}$. For $k \leq i$, Algorithm 4.2 now performs one EUMarginalization less and, from Proposition 4.2, we deduce that $\tilde{U}_{k}^{\prime}$ has now $r_{k b a} / r_{i}$ monomials of degree $d_{k b a}-1$.

# A. 5 Proof of proposition 6 

Let $\Pi_{k \backslash i}=\Pi_{k} \backslash\{i\}$. If $Y_{i}$ is parent of $Y_{k}$ we have that

$$
\begin{aligned}
p_{k y_{k} \pi_{k}^{\prime}}^{\prime} & =P\left(y_{k} \mid y_{\Pi_{k}^{\prime}}\right)=P\left(y_{k} \mid y_{\Pi_{i}}, y_{\Pi_{k \backslash i}}\right)=\sum_{y_{i} \in \mathcal{Y}_{i}} P\left(y_{k} \mid y_{\Pi_{k}}, y_{\Pi_{i}}\right) P\left(y_{i} \mid y_{\Pi_{k \backslash i}}, y_{\Pi_{i}}\right) \\
& =\sum_{y_{i} \in \mathcal{Y}_{i}} P\left(y_{k} \mid y_{\Pi_{k}}\right) P\left(y_{i} \mid y_{\Pi_{i}}\right)=\sum_{y_{i} \in \mathcal{Y}_{i}} p_{k y_{k} \pi_{k}} p_{i y_{i} \pi_{i}}
\end{aligned}
$$

If $Y_{i}$ is a parent but not the parent of $Y_{j}$, then $P\left(y_{i} \mid y_{\Pi_{j \backslash i}}, y_{\Pi_{i}}\right)$ as in (12) can be written as

$$
\begin{aligned}
P\left(y_{i} \mid y_{\Pi_{j \backslash i}}, y_{\Pi_{i}}\right) & =P\left(y_{i} \mid y_{\Pi_{j} \backslash[i-1]}, y_{\Pi_{j} \cap[i-1]}, y_{\Pi_{i}}\right) \\
& =\frac{P\left(y_{\Pi_{j} \backslash[i-1]} \mid y_{i}, y_{\Pi_{j} \cap[i-1]}, y_{\Pi_{i}}\right) P\left(y_{i} \mid y_{\Pi_{i}}\right)}{\sum_{y_{i} \in \mathcal{Y}_{i}} P\left(y_{\Pi_{j} \backslash[i-1]} \mid y_{i}, y_{\Pi_{j} \cap[i-1]}, y_{\Pi_{i}}\right) P\left(y_{i} \mid y_{\Pi_{i}}\right)} \\
& =\frac{\prod_{l \in \Pi_{j} \backslash[i-1]} \sum_{\mathcal{Y}_{\Pi_{i} \cap \Pi_{j} \cap \Pi_{i}}} P\left(y_{l} \mid y_{\Pi_{l}}\right) P\left(y_{i} \mid y_{\Pi_{i}}\right)}{\sum_{y_{i} \in \mathcal{Y}_{i}} \prod_{l \in \Pi_{j} \backslash[i-1]} \sum_{\mathcal{Y}_{\Pi_{i} \cap \Pi_{j} \cap \Pi_{i}}} P\left(y_{l} \mid y_{\Pi_{l}}\right) P\left(y_{i} \mid y_{\Pi_{i}}\right)}
\end{aligned}
$$

## A. 6 Proof of theorem 2

For $i, j, k, l \in \mathbb{V}$ and $s, t \in[m]$, an asymmetry $Y_{t}=y_{i} \Rightarrow Y_{j}=y_{j}$ implies that any monomials that include terms of the form $p_{k y_{k} \pi_{k}}, \psi_{x \pi_{x}}, p_{k y_{k} \pi_{k}} p_{l y_{l} \pi_{l}}, \psi_{t \pi_{t}} \psi_{x \pi_{x}}$ and $p_{k y_{k} \pi_{k}} \psi_{x \pi_{x}}$ entailing both instantiations $y_{i}$ and $y_{j}$ are associated to a non possible combination of events, with $y_{k} \in \mathcal{Y}_{k}, \pi_{k} \in \mathcal{Y}_{\Pi_{k}}, y_{l} \in \mathcal{Y}_{l}, \pi_{l} \in \mathcal{Y}_{\Pi_{l}}, \pi_{t} \in \mathcal{Y}_{P_{t}}$ and $\pi_{s} \in \mathcal{Y}_{P_{s}}$. Thus these monomials have to be set equal to zero.

For $j<t \leq z, \tilde{U}_{t}$ has an associated set $B_{t}$ which includes both $i$ and $j$ and consequently $\prod_{s \in B_{t} \backslash[i \cup j]} r_{s}$ rows of the vector corresponds to the conditioning on $Y_{t}=y_{i}$ and $Y_{j}=y_{j}$. Therefore all the monomials in those rows have to be set equal to zero.

For $i<t \leq j$, the index $i$ is in the set $B_{t}$, whilst the variable $Y_{j}$ has been already EUMarginalized. Thus, there are only $\prod_{s \in B_{t} \backslash\{i\}} r_{s}$ rows conditional on the event $Y_{i}=y_{i}$. In those rows only some of the monomials are associated to the event $Y_{j}=y_{j}$. Specifically, the ones implying $Y_{j}=y_{j}$ can only be multiplying a term including a $\psi_{x} P_{x}$ from a utility vertex $U_{x}$ subsequent to $Y_{j}$ in the MID DS. We can deduce that there are $\prod_{i=t}^{j_{x}} r_{s} / r_{j}$ monomials of degree $d_{t b a}$ that include the case $Y_{j}=y_{j}$ in such entries of $\tilde{U}_{t}$, for $a=x, \ldots, m$ and $b=l, \ldots, a$ (using the notation of Theorem 1).

Lastly, if $t \leq i$, then the set $B_{t}$ does not include $i$ and $j$, which have been both EUMarginalized. Thus monomials including a combination of the events $Y_{j}=y_{j}$ and $Y_{i}=y_{i}$ appears in each row of $\tilde{U}_{t}$. Similarly as before, we can deduce that there are $\prod_{i=t}^{j_{x}} r_{s} /\left(r_{i} \cdot r_{j}\right)$ monomials of degree $d_{t b a}, a=x, \ldots, m, b=l, \ldots, a$, implying the event $Y_{i}=y_{i} \wedge Y_{j}=y_{j}$.

# Appendix B Maple code 

## B. 1 Initialization functions

```
### Required Packages ###
with(ArrayTools): with(LinearAlgebra):
### Computation of the highest index in each parent set of a utility node ###
# Inputs: PiU::table, parent sets of utility nodes; m::integer, num. utility nodes
# Output: J::list
CompJ := proc(PiU,m) local i,j:
for j to m do J[j] := max(PiU[J]) end do:
return convert(J,list): end proc:
### Computation of the indices of the argument of the EU at step i ###
# Inputs: PiU::table; PiV::table, parent sets of random nodes;
i::integer;
# n::integer, number of random nodes; J::list
# Output: Bi[i]::set
CompBi := proc(PiU,PiV,i,n,J) local Bi,part,j:
Bi[i], part := $\{\},\{ \}$ :
for j from i to n do
part := part union $\{j\}$ :
if member( $j, V)$ then Bi[i] := Bi[i] union PiV[j] end if:
if member(j,J,'l') then Bi[i] := Bi[i] union PiU[l] end if:
end do:
Bi[i] := Bi[i] minus part:
return Bi[i]:
end proc:
```
```
### Initialization of an MID ###
# Inputs: p::table, probability vectors; psi::table, utility vectors;
PiV::table;
# PiU::table; n::integer; m::integer
# Outputs: J::list; Bi::list; u::table, EU vectors
Initialize := proc(p, psi, PiV, PiU, n, m) local J, i, Bi, u:
J := CompJ(PiU, m):
for i to n do Bi[i] := CompBi(PiU, PiV, i, n, J) end do:
Bi[n+1], u[n+1] := {}, []:
return J, Bi, u:
end proc:
```

```
### Identification of an optimal policy (at random) ###
# Inputs: r::table; i::integer, index of the decision variable,
# t::integer, number of random draws
#Outputs: maxi::vector, optimal decisions
Maximize := proc(r, i, t) local maxi, l:
maxi := Vector(t, 0):
for l to t do maxi[l] := RandomTools[Generate](integer(range = 1 ..
r[i])) end do:
return maxi:
end proc:
```


# B. 2 EU duplications 

```
### EUDuplication of a utility vector and an EU vector ###
# Inputs: u::table; psi::table; j::integer; PiV::table; PiU::table;
# r::table, size of the decision and sample spaces; Bi::table; J::list
# Outputs: utemp::list, EUDuplicated version of u;
# psitemp::list, EUDuplicated version of psi
EUDuplicationPsi := proc(u, psi, j, PiV, PiU, r, Bi, J)
local i, uprime, psip, psit, utemp, x, sx, y, l, z:
i := max(PiU[j]):
uprime, psip, psit, utemp := [], [], psi[j], u[i+1]:
for x from max(Bi[i+1], PiU[j]) by -1 to 1 do
if member(x, (PiU[j] union Bi[i+1]) minus (PiU[j] intersect Bi[i+1]))
then sx := 1:
for y from x+1 to max(Bi[i+1], PiU[j]) do
if member(y, union(Bi[i+1], PiU[j])) then sx := sx*r[y] end if
end do:
if member(x, Bi[i+1]) then for l to Size(psit)[2]/sx do for z to r[x] do
psip := [op(psip),op(convert(convert(psit,list)[(l-1)*sx+1..1*sx],list))]
end do end do:
psit, psip := psip, []:

elif member(x, PiU[j]) then for l to Size(utemp)[2]/sx do for z to $r[x]$ do
uprime:=[op(uprime),op(convert(convert(utemp,list)[(l-1)*sx+1..1*sx], list))] end do end do:
utemp, uprime := uprime, []:
end if end if end do:
return utemp, psit:
end proc:
### EUDuplication of a probability vector and an EU vector ###
# Inputs: u::table; p::table; i::integer; PiV::table; PiU::table;
r::table; Bi::table; J::list
# Outputs: utemp::list, EUDuplicated version of u;
# ptemp::list, EUDuplicated version of p
EUDuplicationP := proc (u, p, i, PiV, PiU, r, Bi, J)
local uprime, pprime, ptemp, utemp, x, sx, y, l, z, Uni:
uprime, pprime, ptemp, utemp := [], [], p[i], u[i+1]:
if member(i, J) then member(i, J, 'j');
Uni := (Bi[i+1] union PiV[i]) union PiU[j]:
for $x$ from max(Uni) by -1 to 1 do
if member(x, Uni minus ((Bi[i+1] union PiU[j]) intersect (PiV[i]
union i))) then $s x:=1$;
for $y$ from $x+1$ to max(Uni) do if member(y, Uni) then
$s x:=s x * r[y]$ end if end do;
if member(x, union(Bi[i+1], PiU[j])) then
for l to Size(ptemp)[2]/sx do for z to r[x] do
pprime:=[op(pprime), op(convert(convert(ptemp,Array)[(l-1)*sx+1..1*sx], list))]
end do end do:
ptemp, pprime := pprime, []:
elif member(x, PiV[i]) then for l to Size(utemp)[2]/sx do
for $z$ to $r[x]$ do uprime:=[op(uprime), op(convert(convert(utemp,Array)
$[(l-1) * s x+1 . .1 * s x]$, list))]
end do end do:
utemp, uprime := uprime, []:
end if end if end do:
else for $x$ from max(Bi[i+1], PiV[i]) by -1 to 1 do
if member(x,(Bi[i+1] union PiV[i])minus(Bi[i+1] intersect (PiV[i]
union i))) then $s x:=1$;
for y from $x+1$ to max(Bi[i+1],PiV[i]) do if member(y,Bi[i+1] union
$\mathrm{PiV}[i])$ then $s x:=\operatorname{sx}^{*} r[y]$
end if end do:
if member(x, Bi[i+1]) then for l to Size(ptemp)[2]/sx do for z to $r[x]$ do
pprime:=[op(pprime), op(convert(convert(ptemp,Array)[(l-1)*sx+1..1*sx], list))]
end do end do:

ptemp, pprime := pprime, []:
elif member(x, PiV[i]) then for l to Size(utemp)[2]/sx do for z to $\mathrm{r}[\mathrm{x}]$ do
uprime:=[op(uprime), op(convert(convert(utemp,Array)[(l-1)*sx+1..1*sx], list))]
end do end do;
utemp, uprime := uprime, []:
end if end if end do end if:
utemp, ptemp := convert(utemp,Array), convert(ptemp,Array):
return utemp,ptemp: end proc:
```
# B. 3 EU operations 
```
### EuMultiSum between an EU vector and a utility vector ###
# Inputs: u::table; psi::table; j::integer; PiV::table; PiU::table;
# r::table; Bi::table; J::list
# Outputs: ut::list, EU vector after an EUMultiSum
EUMultiSum := proc(u, psi, j, PiV, PiU, r, Bi, J) local i, uprime, psip, ut; i := max(PiU[j]);
if $j=$ Size(convert(PiU, list), 2) then ut := k[j]* psi[j]:
else uprime, psip := EUDuplicationPsi(u, psi, j, PiV, PiU, r, Bi, J); ut := h* k[j]* psip* uprime + uprime + k[j]* psip end if:
return ut:
end proc:
### EUMarginalization over a sample space ###
# Inputs: u::table; p::table; i::integer; PiV::table; PiU::table;
r::table; Bi::table; J::list
# Outputs: ut::list, EU vector after EUMarginalization
EUMarginalization := proc (u, p, i, PiV, PiU, r, Bi, J)
local uprime, pprime, ut, cols, l, k:
uprime, pprime := EUDuplicationP(u, p, i, PiV, PiU, r, Bi, J): cols := Size(pprime)[2]:
ut := convert(ZeroVector(cols/r[i]), Array):
for l to (cols/r[i]) do for k to r[i] do ut[l] := ut[l]+
pprime[r[i]*(l-1)+k]*uprime[r[i]*(l-1)+k]:
end do end do:
return ut:
end proc:
### EUMaximization over a decision space ###
# Inputs: u::table; i::integer; r::table
# Outputs: u[i]::list, EU vector after
EUMaximization

EUMaximization := proc(u, i, r) local opt, l ;
opt := Maximize(r, i, Size(u[i+1])[2]/r[i]);
u[i] := Array([seq(0,1 in 1..Size(opt)[1])]):
for l to Size(opt)[1] do
u[i][l] := convert(u[i+1],Array)[r[i]* (1-1)+opt[l]] end do;
return u[i]:
end proc:
```
# B. 4 The symbolic algorithm 
```
### Symbolic evaluation algorithm for an MID ###
# Inputs: p::table; psi::table; PiV::table; PiU::table; n::integer; m : :integer;
# De::set, index set of the decision variables;
# V::set, index set of the random variables; r::table
# Output: eu::table, EU vectors;
SymbolicExpectedUtility := proc(p, psi, PiV, PiU, n, m, De, V, r)
local J, Bi, utemp, i, j, eu;
J, Bi, eu := Initialize(p, psi, PiV, PiU, n, m);
j:=m;
for i from n by -1 to 1 do if j=0 then if member(i, De) then eu[i]
:= EUMaximization(eu, i, r)
else eu[i] := EUMarginalization(eu, p, i, PiV, PiU, r, Bi, J) end if;
else if J[j]=i then if member(i, De) then
utemp[i+1] := EUMultiSum(eu, psi, j, PiV, PiU, r, Bi, J);
eu[i] := EUMaximization(utemp, i, r)
else
utemp[i+1] := EUMultiSum(eu, psi, j, PiV, PiU, r, Bi, J);
eu[i] := EUMarginalization(utemp, p, i, PiV, PiU, r, Bi, J)
end if;
j:=j-1
else if member(i, De) then eu[i] := EUMaximization(eu, i, r)
else eu[i] := EUMarginalization(eu, p, i, PiV, PiU, r, Bi, J) end if
end if end if end do;
return eu:
end proc:
```
## B. 5 Implementation of the example

Consider the MID in Fig. 1 with $n=6$ variables (decision or random nodes) and $m=3$ utility nodes.
```
### Definition of the MID ###
# number of variables and utility nodes
n := 6: m := 3: 

# V contains the indices of random nodes and De those of the decision nodes 
V := 2, 3, 5, 6: 
De := 1, 4:

# Conditional probabilities
Symbolic computation of expected utilities in influence diagrams 311
p[6] := [p6111, p6011, p6101, p6001, p6110, p6010, p6100, p6000]:
p[5] := [p5111, p5011, p5101, p5001, p5110, p5010, p5100, p5000]:
p[3] := [p3111, p3011, p3101, p3001, p3110, p3010, p3100, p3000]:
p[2] := [p211, p201, p210, p200]:

# Utility parameters
psi[1] := [psi11, psi10]:
psi[2] := [psi21, psi20]:
psi[3] := [psi311, psi301, psi310, psi300]:

# Parents of random nodes
PiV[2] := 1: 
PiV[3] := 1, 2: 
PiV[5] := 3, 4: 
PiV[6] := 4, 5:

# Parents of utility nodes
PiU[1] := 3: 
PiU[2] := 5: 
PiU[3] := 4, 6:

# Number of levels of the variables
r[1] := 2: 
r[2] := 2: 
r[3] := 2: 
r[4] := 2: 
r[5] := 2: 
r[6] := 2:

### Computation of the EU vectors ###
eu := SymbolicExpectedUtility(p, psi, PiV, PiU, n, m, De, V, r):

Example of the output of eu[1]:
[((k[1]*psi11+h*k[1]*psi11*((k[2]*psi21+h*k[2]*psi21*
(p6010*psi300*k[3]+p6110*psi310*k[3])+k[3]*psi300*p6010
+k[3]*psi310*p6110)*p5101+(k[2]*psi20+h*k[2]*psi20*(p6000*psi300*k[3]
+p6100*psi310*k[3])+k[3]*psi300*p6000+k[3]*psi310*p6100)*p5001)+
(k[2]*psi21+h*k[2]*psi21*(p6010*psi300*k[3]+p6110*psi310*k[3])
+k[3]*psi300*p6010+k[3]*psi310*p6110)*p5101+
(k[2]*psi20+h*k[2]*psi20*(p6000*psi300*k[3]+p6100*psi310*k[3])
+k[3]*psi300*p6000+k[3]*psi310*p6100)*p5001)*p3110+
(k[1]*psi10+h*k[1]*psi10*((k[2]*psi21+h*k[2]*psi21*(p6011*psi301*k[3]
+p6111*psi311*k[3])+k[3]*psi301*p6011+k[3]*psi311*p6111)*p5110+
(k[2]*psi20+h*k[2]*psi20*(p6001*psi301*k[3]+p6101*psi311*k[3])
+k[3]*psi301*p6001+k[3]*psi311*p6101)*p5010)+
(k[2]*psi21+h*k[2]*psi21*(p6011*psi301*k[3]+p6111*psi311*k[3])
+k[3]*psi301*p6011+k[3]*psi311*p6111)*p5110+
(k[2]*psi20+h*k[2]*psi20*(p6001*psi301*k[3]+p6101*psi311*k[3])
+k[3]*psi301*p6001+k[3]*psi311*p6101)*p5010)*p3010)*p210+
((k[1]*psi11+h*k[1]*psi11*((k[2]*psi21+h*k[2]*psi21*(p6010*psi300*k[3]
+p6110*psi310*k[3])+k[3]*psi300*p6010+k[3]*psi310*p6110)*p5101+
(k[2]*psi20+h*k[2]*psi20*(p6000*psi300*k[3]+p6100*psi310*k[3])
+k[3]*psi300*p6000+k[3]*psi310*p6100)*p5001)+
(k[2]*psi21+h*k[2]*psi21*(p6010*psi300*k[3]+p6110*psi310*k[3])
+k[3]*psi300*p6010+k[3]*psi310*p6110)*p5101+
(k[2]*psi20+h*k[2]*psi20*(p6000*psi300*k[3]+p6100*psi310*k[3])
+k[3]*psi300*p6000+k[3]*psi310*p6100)*p5001)*p3100+
(k[1]*psi10+h*k[1]*psi10*((k[2]*psi21+h*k[2]*psi21*
(p6011*psi301*k[3]+p6111*psi311*k[3])+k[3]*psi301*p6011+k[3]
psi311*p6111)*p5110+ (k[2]*psi20+h*k[2]*psi20*(p6001*psi301*k[3]+
p6101*psi311*k[3]) +k[3]*psi301*p6001+k[3]*psi311*p6101)*p5010)+
(k[2]*psi21+h*k[2]*psi21*(p6011*psi301*k[3]+p6111*psi311*k[3])
+k[3]*psi301*p6011+k[3]*psi311*p6111)*p5110+
(k[2]*psi20+h*k[2]*psi20*(p6001*psi301*k[3]+p6101*psi311*k[3])
+k[3]*psi301*p6001+k[3]*psi311*p6101)*p5010)*p3000)*p200]

```

Open Access This article is distributed under the terms of the Creative Commons Attribution 4.0 International License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made.
