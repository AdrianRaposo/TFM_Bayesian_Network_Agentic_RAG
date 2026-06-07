# The impact of prior knowledge on causal structure learning 

Anthony C. Constantinou ${ }^{1} \cdot$ Zhigao Guo ${ }^{1} \cdot$ Neville K. Kitson ${ }^{1}$<br>Received: 25 October 2022 / Revised: 3 February 2023 / Accepted: 11 March 2023 /<br>Published online: 8 April 2023<br>© The Author(s) 2023


#### Abstract

Causal Bayesian networks have become a powerful technology for reasoning under uncertainty in areas that require transparency and explainability, by relying on causal assumptions that enable us to simulate hypothetical interventions. The graphical structure of such models can be estimated by structure learning algorithms, domain knowledge, or a combination of both. Various knowledge approaches have been proposed in the literature that enables us to specify prior knowledge that constrains or guides these algorithms. This paper introduces some novel, and also describes some existing, knowledge-based approaches that enable us to combine structure learning with knowledge obtained from heterogeneous sources. We investigate the impact of these approaches on structure learning across different algorithms, case studies and settings that we might encounter in practice. Each approach is assessed in terms of effectiveness and efficiency, including graphical accuracy, model fitting, complexity, and runtime; making this the first paper that provides a comparative evaluation of a wide range of knowledge approaches for structure learning. Because the value of knowledge depends on what data are available, we illustrate the results both with limited and big data. While the overall results show that knowledge becomes less important with big data due to higher learning accuracy rendering knowledge less important, some of the knowledge approaches are found to be more important with big data. Amongst the main conclusions is the observation that reduced search space obtained from knowledge does not always imply reduced computational complexity, perhaps because the relationships implied by the data and knowledge are in tension.


Keywords Bayesian networks $\cdot$ Causal discovery $\cdot$ Directed acyclic graphs $\cdot$ Domain knowledge $\cdot$ Knowledge-based constraints $\cdot$ Probabilistic graphical models

[^0]
[^0]:    囚 Anthony C. Constantinou
    a.constantinou@qmul.ac.uk
    Zhigao Guo
    zhigao.guo@qmul.ac.uk
    Neville K. Kitson
    n.k.kitson@qmul.ac.uk

    1 Bayesian Artificial Intelligence Research Lab, Machine Intelligence and Decision Systems (MInDS) Research Group, School of Electronic Engineering and Computer Science, Queen Mary University of London (QMUL), London E1 4NS, UK

# 1 Introduction 

Learning Bayesian Networks (BNs) involve constructing a graphical structure and parameterising its conditional distributions given the structure. The structure of a BN, also referred to as Causal BN (CBN) if the arcs are assumed to represent causation, can be determined by causal knowledge, learnt from data, or a combination of both. Problems with access to domain expertise tend to attract manual construction of CBN models, whereas automated construction is more prevalent in problems where knowledge is limited or highly uncertain, and structure learning is expected to provide insights that would otherwise remain unknown.

Automated causal discovery is hindered by difficulties that have significantly limited its impact in practise. Algorithms will often discover incorrect causal relationships for events that humans perceive as common sense. For example, an algorithm may discover that the music is influenced by the moves of the dancer, rather than concluding that the dancer is dancing to the music. Such counterintuitive causal links represent failures of causal common sense and raise questions as to whether machine learning is capable of achieving human-level causal understanding.

There are several important reasons that make causal discovery difficult. These include that it is not possible to learn all causal relationships from observational data alone, since the best an algorithm can do is to recover the causal structure up to its Markov equivalence class when learning from observational data. Moreover, the satisfactory performance the algorithms tend to achieve in clean synthetic experiments is rarely repeated in practice [17], and this is because real data are imperfect and tend to violate many of the assumptions on which these algorithms rely on, such as complete data, causal sufficiency, and error-free data, amongst others. Last but not least, exploring the search space of graphs is, in general, NP-hard.

Discovering reasonably accurate causal structure is very important in today's world, where automated decision-making is increasingly being questioned if it provides no transparency or explainability. Unlike black-box solutions, Pearl's do-calculus framework that relies on CBNs [39, 40] provides a clear mechanism for computing the effect of hypothetical interventions. In other words, we can use an optimisation function to determine the optimal intervention by manipulating variables within a causal model in a way that renders the manipulation of a given variable independent of its causes, thereby generating the effect of intervention only. While $d o$-calculus is a relatively simple and a powerful tool for simulating experimental data, its effectiveness directly relies on the accuracy of the underlying causal structure of the model; implying that structure learning accuracy has a direct effect on the accuracy of intervention.

If we expect algorithms to become rational modellers of a world that requires causal perception, then we may have to provide them with something more than an imperfect static observational data set. Structure learning constraints that embody causal knowledge represent one way of assisting algorithms to produce more accurate causal graphs. Because it is common to have some understanding of the underlying causal mechanisms of a given domain, practitioners often seek access to expert knowledge that can guide or constrain structure learning, effectively reducing the uncertainty of the BN models learnt from data.

This paper introduces some novel, and also describes some existing, knowledge-based approaches to investigate their effectiveness on structure learning, by applying them to multiple algorithms and case studies over varying degrees of data size and quantity of knowledge constraints. The paper is structured as follows: Sect. 2 provides a review of past relevant studies, Sect. 3 describes the knowledge approaches we have implemented, Sect. 4 describes the

algorithms we have modified to enable knowledge-based constraints to be incorporated into their structure learning process, Sect. 5 describes the simulation process and experiments, we present and discuss the results in Sect. 6, and concluding remarks are given in Sect. 7.

# 2 Review of past relevant studies 

The field of causal structure learning has seen important advances over the past few decades, particularly those coming from the constraint-based and score-based classes of learning. The relevant literature has evolved rapidly with innovations involving both constraint-based and score-based learning, which represent the two main classes of structure learning. Kitson et al. [30] provide an extensive survey of these algorithms.

The main difference between these two classes of learning is that constraint-based algorithms, such as the popular PC [47] and FCI [48] algorithms and their stable versions [13], tend to start with a fully connected graph and use conditional independence tests to eliminate and orientate some of those edges. On the other hand, score-based algorithms which include the well-established Greedy Equivalence Search (GES) by Chickering and Meek [11], Hill Climbing (HC) and TABU search [3, 27, 44], typically start from an empty graph and iteratively modify the graph to increase its objective score. In this paper, our focus will be on score-based algorithms, but also hybrid learning algorithms that combine the two above classes of learning.

There are different types of score-based algorithms. An important distinction between them involves whether the algorithm offers approximate or exact learning solutions. Exact score-based algorithms such as GOBNILP [20] and B\&B [22] tend to be based on combinatorial optimisation approaches in conjunction with sound pruning strategies that reduce the scale of combinatorial optimisation. In contrast, most approximate algorithms, including GES, HC and TABU discussed above, tend to rely on heuristics that iteratively traverse the search space of graphs through arc additions, reversals and removals, and move towards the graph that maximises a given objective function. While exact solutions guarantee to return the graph that maximises an objective function, this guarantee is subject to certain data assumptions and subject to limiting the maximum in-degree. Moreover, the use of exact learning approaches is typically limited to smaller networks due to their relatively high computational complexity. On the other hand, approximate algorithms are generally much faster and aim to return a high scoring graph that tends to get stuck at a local optimum, without limiting the maximum in-degree. In this paper, we will be focusing on such approximate learning solutions.

The need to account for causal knowledge when constructing or learning causal representation models is well documented [23]. There is also a lot of relevant work in the field of cognitive psychology on how causal induction constrains or guides human learning. For example, Tenenbaum et al. [49] propose a framework which they call causal grammar, about how we think in terms of causal representation and inference, and outlined a formal approach towards solving causal induction inspired by hierarchical Bayesian models. Griffiths and Tenenbaum [25] further build on this view and present a computational framework for the explanation of human causal induction. They use this to identify key aspects of abstract prior knowledge, to show how they provide the constraints that people may rely on when inferring causal structure, and apply it to different case studies to illustrate how explanations of causal learning can be presented. There is also work on how people choose interventions to learn causal systems. This includes the papers by Coenen et al. [12] who show that people make

decisions in an adaptive fashion where a trade-off is made between expected performance and cognitive effort, and by Bramley et al. [4] who propose a scheme to understand how people choose interventions to identify causation.

In the field of causal machine learning, many structure learning algorithms can be modified to account for causal knowledge that guides search towards a preferred causal structure, or restricts the search space of graphs that can be explored to those in which graphs contain or do not contain certain relationships. A knowledge approach that guides, rather than restricts, structure learning is often referred to as an approach that introduces soft constraints, whereas an approach that restricts learning towards specific graphs tends to be referred to as an approach that introduces hard constraints.

The work by Heckerman and Geiger [26] can be viewed as one of the earliest implementations of a soft constraint approach, where the structure learning process is modified to reward graphs that are closer to an initial best guess knowledge graph. In other studies, soft constraints are often implemented by assigning prior beliefs as probabilities to some of the possible relationships between pairs of variables, as described by Castelo and Siebes [7]. Likewise, the work of Amirkhani et al. [1] explored the same types of prior probabilities on edge inclusion or exclusion from multiple experts, applied to two variants of the score-based HC algorithm; one of the early implementations of HC in Bayesian Network Structure Learning (BNSL) can be found in [2]. Ibrahim et al. [28] looked at the problem of learning causal structure by augmenting the distribution of causal structures with a user model whose parameters account for possible biases of the expert. BCano et al. [6] presented a methodology that reduces the effort associated with knowledge elicitation by restricting the elicitation of prior knowledge to edges that cannot be reliably discerned from data, in addition to eliciting knowledge about the temporal order of the variables (this information was required by the algorithm), with application to structure learning via MCMC simulation. Masegosa and Moral [37] extended the work of Cano et al. [6] by removing the requirement of knowledge about the temporal order of the variables, thereby reducing elicitation effort at the expense of the algorithm exploring a larger search space of graphs. For practical reasons, the type of soft constraints that we consider in this paper involve those which do not require the user to assign probabilities.

Hard constraints, on the other hand, tend to be more popular and often easier to implement. One of the first implementations of hard constraints involves the score-based K2 algorithm [19] which assumes that the temporal order of the data variables is given, thereby restricting the search space of graphs to those consistent with the temporal ordering. Other relevant studies include the work of de Campos and Castellano [21] on measuring the effect of knowledge about the existence or absence of edges, in addition to node ordering constraints, with application to the score-based HC and constraint-based PC [48] algorithms. Incomplete temporal orderings, which involve providing temporal information for some of the variables available in the data were investigated by Ma et al. [36] with application to score-based learning and model-averaging. Chen et al. [10] investigated constraining edges in terms of ancestral, rather than parental, relationships and with application to score-based algorithms with a decomposable ${ }^{1}$ objective function, despite the ancestral constraints being non-decomposable; i.e., the ancestral relationships cannot be assigned independent scores in the same way the parental relationships can. Ancestral constraints were also investigated by Li and van Beek [33] who showed that algorithms using non-decomposable ancestral constraints can scale up to problems of 50 variables, with application to the score-based MINOBS algorithm [32] which is

[^0]
[^0]:    ${ }^{1}$ A decomposable objective function refers to a scoring process that can be decomposed into independent components. In the context of BNSL, a decomposable objective function assigns a score to each node in the graph, where the overall score of the graph is the sum over all individual node scores.

an approximate learning algorithm that otherwise scales up to thousands of variables. The work of Chen et al. [10] was recently further investigated by Wang et al. [50] who extended ancestral constraints to score-based learning that searches in the space of variable orderings. Lastly, Constantinou [15] introduced the assumption that all the variables that make up the input data are relevant, which in turn imposes a constraint on the learnt graph not to contain independent subgraphs or unconnected variables, to ensure the learnt model enables full propagation of evidence when applied in practice. Readers may also find helpful the works by Bramley et al. [5] and Rehder et al. [41], who study the role of time in causal learning in humans. The former study illustrates how participants can use the order in which events occurred to narrow down candidate causal structures, and the latter extends this idea to dynamic causal systems where causes continually influence their effects.

Structure learning freeware such as Tetrad [8, 9], bnlearn [43] and CaMML [31, 38] provide access to a range of soft and hard knowledge constraints that can guide or constrain structure learning. To the best of our knowledge, Tetrad is the structure learning freeware that supports the widest range of approaches that enable knowledge to be combined with data for causal discovery. All three, bnlearn, CaMML and Tetrad enable users to specify knowledge about required as well as forbidden edges. Tetrad also allows users to specify the temporal order of the variables, while CaMML enables users to specify a best-guess input graph [31, 38] as in [26].

While it seems plausible that the best approach to constructing a causal graph involves combining knowledge with machine learning, most real-world BN models published in the literature continue to rely entirely on knowledge or entirely on automation, despite the above efforts. Therefore, it is fair to say that the methods that combine knowledge with structure learning remain underused in practice. We often see applications of BNs that either rely on full automation, or entirely on expert systems, rather than combining these two approaches towards causal representation. Perhaps one of the reasons is because their combined effectiveness has not been adequately researched, which partly motivates this study.

# 3 The knowledge approaches implemented 

This section discusses and describes the knowledge approaches (both novel and existing) we have implemented in this study. All the knowledge approaches are made available in the Bayesys open-source BNSL system [14].

We begin by distributing and discussing the knowledge approaches we have implemented into relevant categories, and with reference to Table 1 which provides the complete list and description of these knowledge approaches. The categories are:
a) Direct relationships: this category represents existing approaches that capture information about direct relationships between nodes. Approaches Directed edge ${ }^{2}$ (DIR-EDG) and Forbidden edge ${ }^{3}$ (FOR-EDG), represent the most commonly used knowledge approach. On the other hand, Undirected edge (UND-EDG) is less common and indicates knowledge of an edge without knowledge about the direction of the edge.
b) Incomplete temporal order: we based our temporal definitions on those in Tetrad where variables are assigned to temporal tiers that represent a timeline. Variables assigned to higher-numbered tiers cannot be parents, but can be indirect causes such as ancestors,

[^0]
[^0]:    ${ }^{2}$ This is referred to as Required edge in Tetrad.
    ${ }^{3}$ This is identical to the TETRAD implementation but differs from bnlearn's blacklist function which can be viewed as a function that enables users to specify Forbidden Directed Edge.

Table 1 The knowledge approaches implemented in Bayesys [14] as part of this research paper


Table 1 (continued)


of variables assigned to lower-numbered tiers, with the option to prohibit arcs between variables that belong to the same tier. We specify the approaches Relaxed incomplete temporal order (REL-TEM) which prohibits edges between variables that violate the temporal tiers, and Strict incomplete temporal order (STR-TEM) which prohibits edges between variables that are within the same tier, in addition to what is prohibited by REL-TEM, as described in Table 1.

The term 'incomplete' implies that not all variables need to be specified in the temporal ordering, and those not included are not subject to any temporal restrictions. In implementing this approach, we found that limiting temporal constraints to parental relationships can be problematic. This is because graphs such as $A \rightarrow B \rightarrow C$ do not violate, for example, ordering $\left\{t_{1}=C, t_{2}=A\right\}$ when $A$ is specified to occur only after observing $C$. That is, while the temporal ordering does not allow $A$ to serve as a parent of $C$, it allows $A$ to serve as an ancestor ${ }^{4}$ of $C$. On this basis, we have extended the definition of temporal constraints to include ancestral relationships, in addition to parental relationships. This extended definition is applied to both REL-TEM and STR-TEM approaches. Figure 1 presents a set of examples illustrating under what circumstances arcs violate the ancestral, but not the parental, temporal ordering.

[^0]
[^0]:    ${ }^{4}$ If a complete node ordering is specified, then graphs consistent with that ordering will automatically be consistent with the ancestral relationships in that ordering. This applies to algorithms such as K2, but also to algorithms such as MINOBS which operate in the space of variable orderings even though an ordering is not given as an input. On the other hand, ancestral constraints need to be checked when an incomplete temporal ordering is given, and checking for ancestral relationships represents a computationally expensive task (Chen et al., 2016; Li and van Beek, 2018; Wang et al., 2021), as we also later illustrate in Sect. 6. This also explains why order-based algorithms designed to handle thousands of variables operate on complete, and not on incomplete, variable orderings.

![img-0.jpeg](img-0.jpeg)

Fig. 1 A set of different DAGs highlighting the arcs that violate the temporal constraints indicated in the bottom left corner, with reference to the two different types of incomplete temporal order

Although computationally less efficient, incomplete temporal order provides flexibility with knowledge elicited, which is why we explore this approach rather than an approach that requires that the full temporal order is given. For example, it would be unreasonable to force the user to provide full knowledge about the ordering of the variables, as this might substantially increase the knowledge elicitation effort as well as the risk of eliciting inaccurate knowledge.
c) Initial graph: this represents a far less common approach that involves guiding structure learning from a given best-guess initial graph, rather than from an empty or a fully connected graph (refer to INI-GRA in Table 1). The motivation here is to guide a structure learning algorithm into a potentially higher-scoring local maxima. In this paper, we define this approach as an initial graph that serves as the starting point in the search space of

DAGs and hence, it involves guiding structure learning from the input graph rather than towards the input graph.
d) Variables are relevant: this can be viewed as knowledge that the variables that make up the input data are relevant and hence, it imposes a constraint on the learnt graph not to contain independent subgraphs or unconnected variables (refer to VAR-REL in Table 1), similar to the structure learning feature in [15] discussed in Sect. 2. In this paper, this approach introduces additional arcs at the end of a structure learning process, where the additional arcs minimally decrease the given objective function, and this process continues until no independent subgraphs or nodes are present in the learnt graph.
e) Target node/s: this represents a novel approach that encourages structure learning to produce a higher number of parents, in this case viewed as potential causes, of targeted variables of interest (refer to TAR-VAR in Table 1). While this approach is not necessarily meant to improve the accuracy of a learnt graph, it can still be useful when working with high dimensional real data of limited sample size. This is because, in those scenarios, structure learning algorithms tend to produce sparse networks that represent an inadequate indication of the potential causes or parent nodes of targeted variables of interest.

This approach encourages structure learning to produce parent-sets of a higher size for targeted nodes by modifying the objective function to scale down the dimensionality penalty associated with the number of free parameters, as to encourage the discovery of more parents for given target nodes. Essentially, this approach exchanges a faster increase in dimensionality for a corresponding smaller increase in Log-Likelihood ( $L L$ ). In this paper, we employ the Bayesian Information Criterion (BIC) as the objective function for graph $G$ and data $D$, modified as $B I C_{T A R-V A R}$ to accept optional adjustments in the dimensionality penalty of a given target variable:

$$
B I C_{T A R-V A R}=L L(G \mid D)-\left(\frac{\log _{2} N}{2}\right) p
$$

where $N$ is the sample size of $D$, and $p$ is the number of free parameters in $G$, given

$$
p=\sum_{i}^{\mid V \mid}\left(\left(s_{i}-1\right) \prod_{j}^{\left|\pi_{v_{i}}\right|} q_{j}\right) / r_{i}
$$

where $V$ is the set of variables in graph $G,|V|$ is the size of set $V, s_{i}$ is the number of states of $v_{i}, \pi_{v_{i}}$ is the parent set of $v_{i},\left|\pi_{v_{i}}\right|$ is the size of set $\pi_{v_{i}}, q_{j}$ is the number of states of $v_{j}$ in parent set $\pi_{v_{i}}$, and $r_{i}$ is the new parameter used to diminish the free parameters penalty for targeted variables; i.e., $r=1$ for non-targeted variables and $r>1$, as determined by the user, for targeted variables.
f) Bayesian Decision Networks (BDNs): this category involves knowledge needed to produce graphs that can be parameterised and used as a BDN, also known as Influence Diagrams (IDs) [46]. While this category is often unrelated to structure learning, we have taken advantage of some of the knowledge needed to convert a BN into a BDN, to devise structural constraints. On this basis, we present this category as an additional knowledge approach that can be used to further constrain structure learning.

BDNs are extensions of BNs suitable for optimal decision-making based on the maximum expected utility criterion, and include additional types of nodes and edges, as well as some inferential constraints. In addition to the uncertain chance nodes, BDNs contain decision nodes represented by rectangles (these capture the available decision options), and

utility nodes represented by diamonds (these represent the variable whose value we want to minimise or maximise). BDNs also include Information arcs, in addition to conditional arcs, that enter decision nodes and indicate that a decision is rendered independent of its parent nodes. That is, decision options do not represent observations that need to be explained by their causes, although decisions are informed by their causes. Dashed arcs are used to indicate that a decision is informed by its parents. This is illustrated in Fig 2 that presents a hypothetical BDN where decision nodes 'Test' and 'Treatment' are informed by, although rendered independently of, 'Symptoms' and 'TestResult'. In this example, the best decision combination is the one that collectively minimises 'SideEffect' and maximises post-treatment effectiveness on 'DisPostTreat' and 'SymPostTreat'.

This means that information entailed by BDNs about decision and utility nodes can be used to impose some constraints during structure learning. Specifically, a decision node must have at least one child node, and a utility node must have at least one parent node. This information can be converted into structural constraints, which we later illustrate in Sect. 6 (refer to Fig 13). The implementation of BDN-based knowledge approaches is separated into two versions, which we define as Relaxed BDNs (REL-BDN) and Strict BDNs (STR-BDN) in Table 1. Approach REL-BDN represents the visual modifications needed to convert a BN into a BDN for a given set of decision and utility nodes, whereas STR-BDN imposes the graphical constraints discussed above. While BDNs have been around for a while, they have always involved manual construction and, to the best of our knowledge, this is the first study to automate their graphical construction.
![img-1.jpeg](img-1.jpeg)

Fig. 2 An example of an Influence Diagram/Bayesian Decision Network, inspired by Yet et al. [51, 52], where treatment decision is determined by expected utilities on side effects, post-treatment disease, and post-treatment symptoms

# 4 The algorithms modified to support knowledge-based constraints 

This section describes the five algorithms we have modified to enable them to account for the different types of knowledge constraints. The implementation of all five algorithms is made available in the Bayesys open-source BNSL system [14].

Specifically, we modified the five BNSL algorithms to be able to consider information related to each of the 10 knowledge approaches described in Sect. 3. The five algorithms are:
i. HC: The Hill-Climbing algorithm represents the simplest as well as one of the earliest score-based algorithms for structure learning [2, 27]. The starting point of the algorithm is typically an empty or a random graph. In this study, we start from an empty graph to eliminate randomisation, but also to be able to impose the knowledge constraints. HC investigates all possible neighbouring acyclic graphs by performing arc additions, reversals and removals at each iteration. It then applies the graph modification that maximises the objective score, and stops when the objective score no longer increases. The HC is an approximate algorithm that will often get stuck at a local maximum.
ii. TABU: This algorithm can be viewed as an extension of HC that permits exploring graphical modifications that decrease the objective score, and maintains a tabu list containing the most recently visited graphs to prevent the algorithm from returning to a graph that was previously visited [3]. In practice, this approach enables TABU to move into new graphical regions that may contain an improved local maximum. Because TABU cannot guarantee to return the highest scoring graph available in the search space, it is also an approximate learning algorithm.
iii. SaiyanH: This is a hybrid learning algorithm since it relies on both constraint-based and score-based learning strategies [15]. SaiyanH starts by drawing undirected edges between nodes that have the strongest marginal dependency, and then orientates those edges by performing a sequence of conditional independence tests, score-based tests, as well as exploring which orientations would maximise the effect of hypothetical interventions. It then performs tabu search with the restriction not to visit graphs that contain disjoint subgraphs. This learning strategy ensures that the learnt graph enables full propagation of evidence when then graph is parameterised.
iv. MAHC: The Model-Averaging Hill-Climbing algorithm combines two learning strategies with hill-climbing search [18]. MAHC starts by pruning the search space of graphs. The pruning strategy restricts the candidate parents for each node, and represents an aggressive version of those that are typically applied to combinatorial optimisation structure learning problems. Once a reduced search-space is obtained, it performs model averaging in the hill-climbing search process and moves to the neighbouring graph that maximises the average objective score, across that neighbouring graph and all its valid neighbouring graphs. The motivation here is that a model averaging process might be less sensitive to data noise, which is commonly present in real data.
v. GES: The Greedy Equivalence Search (GES) algorithm contains two learning phases, known as the forward and backward search phases [11]. The forward phase starts from an empty graph and, at each iteration, the edge that maximises the objective function is added to the graph. When no edge is found to further increase the objective score, GES enters the backward phase where edge removals are performed in the same way. The algorithm stops when no further edge removals increase the objective score.

To be able to measure the impact of knowledge consistently across all algorithms, we employ the same objective function, the BIC, for all algorithms. Moreover, because the knowledge approaches are implemented such that they constrain or guide the search-space

Table 2 An example of directed constraints based on the $20 \%$ rate of constraints for case study Alarm


The table shows how this information is encoded into an input data file which is read by an algorithm whenever the knowledge approach DIREDG is called
of DAGs, we apply all algorithms to the search-space of DAGs. This also applies to GES which is proposed for CPDAG-space exploration; i.e., we had to simplify GES by applying it to the search-space of DAGs without testing for score equivalence. This simplification was necessary since testing for equivalence in the DAG-space (as opposed to the smaller CPDAG-space in [11]) proved to be computationally expensive and led to most experiments failing to complete learning within the runtime limit.

Algorithms 1, 2, 3, 4, and 5 describe how each of these five algorithms was modified to account for the knowledge approaches enumerated in Table 1. Note that temporal knowledge is imposed either as REL-TEM or STR-TEM, and the same applies for knowledge relating to BDNs which is imposed either as REL-BDN or STR-BDN.

Each knowledge approach involves additional constraints that can be taken into consideration by a structure learning algorithm. This means that whenever a knowledge approach appears in the pseudocode of the five algorithms, it implies that the learning is constrained by the information present in the knowledge. As an example, Table 2 presents the constraints for DIR-EDG considered at the $20 \%$ rate of constraints for case study Alarm, and this format is followed by all the approaches. For example, the approach UND-EDG would involve columns referring to Var1 and Var2, whereas approach REL-BDN/STR-BDN involves data rows referring to Decision and Utility nodes, rather than Parent and Child nodes. The only approach that involves a rather different structural format is the REL-TEM/STR-TEM, which involves temporal constraints as configured in Table 3.

The implementation of the knowledge approaches can be summarised as follows:

Table 3 An example of temporal constraints based on the $20 \%$ rate of constraints for case study Alarm


The table shows how this information is encoded into an input data file which is read by an algorithm whenever the knowledge approach REL-TEM or STR-TEM is called

a) $H C, T A B U, M A H C$ and GES: Their initial empty graph can be replaced by INI-GRA or modified to incorporate DIR-EDG and UND-EDG;
b) SaiyanH: Its graph obtained by associational and constraint-based learning can be restricted to graphs that do not violate FOR-EDG, DIR-EDG, UND-EDG, REL-TEM or STR-TEM, and INI-GRA;
c) MAHC: Its pruning strategy can be restricted to Candidate Parent Sets (CPSs) that do not violate FOR-EDG, DIR-EDG, and REL-TEM or STR-TEM;
d) All five algorithms: Their heuristic search is restricted to graphs that do not violate FOREDG, DIR-EDG, UND-EDG, and REL-TEM or STR-TEM;
e) All five algorithms: Their objective function is modified to account for TAR-VAR;
f) $H C, T A B U, M A H C$ and GES: When these four algorithms complete learning, they can be forced to continue the heuristic search until the VAR-REL condition is met;
g) All five algorithms: When they complete learning, their graph can be converted into a BDN to satisfy REL-BDN;
h) All five algorithms: When they complete learning, they can be forced to extend the heuristic search until the learnt graph satisfies STR-BDN.

Algorithm 1: Hill-Climbing (HC) algorithm with additional pseudocode needed to account for the knowledge approaches highlighted in red font colour.
Input: dataset $D$, empty graph $G$, objective function $\mathrm{BIC}_{T A R-V A R}(G, D)$, max in-degree $M$, optional knowledge $K$ (DIR-EDG, UND-EDG, FOR-EDG, REL-TEM v STR-TEM, INI-GRA, VAR-REL, TAR-VAR, REL-BDN v STRBDN)
Output: DAG $G_{\max }$ that maximises $S_{G}=\mathrm{BIC}_{T A R-V A R}(G, D)$ in the search space of DAGs given $K$
1: if $K$ (INI-GRA) is not empty do $G=$ INI-GRA
3: else do $G+(K$ (DIR-EDG) v randomise direction of $K$ (UND-EDG) $) \vDash D A G, M$
4: do $S_{G}=\mathrm{BIC}_{T A R-V A R}(G, D), S_{\max }=S_{G}$ and $G_{\max }=G$
5: while $S_{\max }$ increases do
6: for every arc addition, reversal and removal in $G_{\max }$, bounded by CPSs, do
7: if $G_{\max } \vDash D A G, M, K$ (DIR-EDG, UND-EDG, FOR-EDG, REL-TEM v STR-TEM) do
8: $\quad S_{G_{n}}=\mathrm{BIC}_{T A R-V A R}\left(G_{n}, D\right)$
9: $\quad$ if $S_{G_{n}}>S_{\max }$ and $S_{G_{n}}>S_{G}$ do $G=G_{n}$, and $G_{\max }=G$
10: end for
11: if $S_{G}>S_{\max }$ do $S_{\max }=S_{G}$ and $G_{\max }=G$
12: end while
// Process for constraint VAR-REL; i.e., variables are relevant
13: if $K$ (VAR-REL) is not empty do
14: while independent subgraphs or unconnected variables in $G>1$ do
15: HC and return $G_{n}$ with an extra arc that minimally decreases $\mathrm{BIC}_{T A R-V A R}(G, D)$
16: $G=G_{n}$
17: end while
// Process for constraints REL-BDN v STR-BDN; i.e., Bayesian Decision Networks (BDNs)
18: if $K($ REL-BDN v STR-BDN $)$ is not empty do
19: convert learnt graph to a BDN graph
20: if $K($ STR-BDN $)$ is not empty do
21: while a Decision has no child $v$ a Utility has no parent in $G$ do
22: HC and return $G_{n}$ with an extra arc for a Decision/Utility that minimally decreases $\mathrm{BIC}_{T A R-V A R}(G, D)$
23: $\quad G=G_{n}$
24: end while

Algorithm 2: TABU algorithm with additional pseudocode needed to account for the knowledge approaches highlighted in red font colour.
Input: dataset $D$, empty graph $G$, objective function $\mathrm{BIC}_{\text {TAR-VAR }}(G, D)$, max in-degree $M$, optional knowledge $K$ (DIREDG, UND-EDG, FOR-EDG, REL-TEM v STR-TEM, INI-GRA, TAR-VAR, REL-BDN v STR-BDN)
Output: DAG $G_{\max }$ that maximises $S_{G}=\mathrm{BIC}_{\text {TAR-VAR }}(G, D)$ in the search space of DAGs given $K$
1: if $K$ (INI-GRA) is not empty do $G=$ INI-GRA
2: else do $G+(K$ (DIR-EDG) $\vee$ randomise direction of $K$ (UND-EDG) $) \triangleright D A G, M$
3: do HC (Algorithm 1) on $G$ and get $S_{\max }$ and $G_{\max }$
4: while $S_{\max }$ increases or for up to $|D|(|D|-1)$ times do
5: for each arc addition, reversal and removal in $G_{\max }$, bounded by CPSs, that produces $G_{n} \triangleright D A G$ do
6: find $G_{n}$ that minimally decreases $S_{\max }$ where $G_{n} \triangleright D A G, M, K$ (DIR-EDG, UND-EDG, FOR-EDG, REL-TEM v STR-TEM)
7: do HC (Algorithm 1) on $G_{n}$ and get $S_{n, \max }$ and $G_{n, \max }$
8: do $S_{n, \max }=\mathrm{BIC}_{\text {TAR-VAR }}\left(G_{n n}, D\right)$
9: if $S_{n, \max }>S_{\max }$ do $S_{\max }=S_{n, \max }$ and $G_{\max }=G_{n, \max }$
10: else do remove $G_{n}$ from the list of neighbours of $G_{\max }$
11: end for
12: end while
// Process for constraint VAR - REL; i.e., variables are relevant
13: if $K$ (VAR-REL) is not empty do
14: while independent subgraphs or unconnected variables in $G>1$ do
15: HC and return $G_{n}$ with an extra arc that minimally decreases $\mathrm{BIC}_{\text {TAR-VAR }}(G, D)$
16: $G=G_{n}$
17: end while
// Process for constraints REL-BDN v STR-BDN; i.e., Bayesian Decision Networks (BDNs)
18: if $K$ (REL-BDN v STR-BDN) is not empty do
19: convert learnt graph to a BDN graph
20: if $K$ (STR-BDN) is not empty do
21: while a Decision has no child $v$ a Utility has no parent in $G$ do
22: HC and return $G_{n}$ with an extra arc for a Decision/Utility that minimally decreases $\mathrm{BIC}_{\text {TAR-VAR }}(G, D)$
23: $G=G_{n}$
24: end while

Algorithm 3: Saiyan Hybrid (SaiyanH) algorithm with additional pseudocode needed to account for the knowledge approaches highlighted in red font colour. The MMD score and EMSG graph are described in Appendix A.
Input: dataset $D$, variable set $V$, empty graph $G$, objective function $\mathrm{BIC}_{T A R-V A R}(G, D)$, max in-degree $M$, optional knowledge $K$ (DIR-EDG, UND-EDG, FOR-EDG, REL-TEM v STR-TEM, INI-GRA, TAR-VAR, REL-BDN v STRBDN)
Output: DAG $G_{\max }$ that maximises $S_{G}=\operatorname{BIC}_{T A R-V A R}(G, D)$ in the search space of DAGs given $K$
// Phase 1: Associational learning
1: Get MMD score set for all possible edges
set max MMD score for edges in $K$ (DIR-EDG, UND-EDG, INI-GRA)
set min MMD score for edges in $K$ (FOR-EDG, REL-TEM v STR-TEM)
2: Produce EMSG given MMD
// Phase 2: Constraint-based learning
3: Get $M M D_{e}$ for all conditional dependency tests over $V$, excluding edges $K$ (DIR-EDG, INI-GRA, FOR-EDG)
4: Get classification set $C$ (cond. dependence/independence/insignificance) over $M M D_{e}$
5: Orientate edges given $K$ (DIR-EDG, INI-GRA) and $C$, where $\operatorname{EMSG} \vDash D A G, M, K$ (REL-TEM v STR-TEM)
6: for up to two times do
7: $\quad$ orientate edges given $\mathrm{BIC}_{T A R-V A R}(E M S G, D)$ where $\operatorname{EMSG} \vDash D A G, M, K($ REL-TEM v STR-TEM)
8: skip unoriented edges when both orientations produce $\operatorname{EMSG} \notin D A G, M, K($ REL-TEM v STR-TEM)
9: $\quad$ orientate edges given do-calculus where $\operatorname{EMSG} \vDash D A G, M, K($ REL-TEM v STR-TEM)
10: skip unoriented edges when both orientations produce $\operatorname{EMSG} \notin D A G, M, K($ REL-TEM v STR-TEM)
11: end for
// Phase 3: Score-based learning
12: Do TABU (Algorithm 2) given $D, E M S G, \operatorname{BIC}_{T A R-V A R}(G, D), M, K$ (DIR-EDG, UND-EDG, FOR-EDG, RELTEM v STR-TEM, INI-GRA, TAR-VAR, and constrain the search space of graphs to those that do not contain independent subgraphs or independent variables
// Process for constraints REL-BDN v STR-BDN; i.e., Bayesian Decision Networks (BDNs)
13: if $K($ REL-BDN v STR-BDN $)$ is not empty do
14: convert learnt graph to a BDN graph
15: if $K($ STR-BDN $)$ is not empty then
16: while a Decision has no child $v$ a Utility has no parent in $G$ do
17: HC and return $G_{n}$ with an extra arc for a Decision/Utility that minimally decreases $\operatorname{BIC}_{T A R-V A R}(G, D)$
18: $\quad G=G_{n}$
19: end while

Algorithm 4: Model-Averaging Hill-Climbing (MAHC) algorithm with additional pseudocode needed to account for the knowledge approaches highlighted in red font colour.
Input: dataset $D$, empty graph $G$, objective function $\mathrm{BIC}_{T A R-V A R}(G, D)$, max in-degree for pruning phase $M_{P}$, max indegree for structure learning phase $M_{S}$, optional knowledge $K$ (DIR-EDG, UND-EDG, FOR-EDG, REL-TEM v STR-TEM, INIGRA, VAR-REL, TAR-VAR, REL-BDN v STR-BDN).
Output: DAG $G_{\max }$ that maximises the average set of scores $S_{G}=\overline{S\left(G, G_{n}\right)}=\overline{\mathrm{BIC}_{T A R-V A R}\left(G, G_{n}, D\right)}$, where $G_{n}$ represents all the valid neighbours of $G$, in the search space of DAGs given $K$.

1: if $K$ (INI-GRA) is not empty do $G=$ INI-GRA
2: else do $G+(K$ (DIR-EDG) v randomise direction of $K$ (UND-EDG)) $\triangleright D A G, M$
3: Pre-process CPSs $\triangleright M_{P}$, and obtain edge set $F$ containing edges forbidden/pruned off
4: do $S_{G}=\overline{S\left(G, G_{n}\right)}, S_{\max }=S_{G}$ and $G_{\max }=G$
5: while $S_{\max }$ increases do
6: for every neighbour $G_{n}$ of $G_{\max }$ where $G_{n} \triangleright D A G, M_{S}, F, K$ (DIR-EDG, UND-EDG, FOR-EDG, REL-TEM v STR-TEM) do
7: $\quad$ add $\mathrm{BIC}_{T A R-V A R}\left(G_{n}, D\right)$ to a new set of objective scores $\boldsymbol{S}$
8: for every $G_{\mathrm{nn}}$ of $G_{\mathrm{n}}$ where $G_{\mathrm{nn}} \triangleright D A G, M_{S}, F, K$ (DIR-EDG, UND-EDG, FOR-EDG, REL-TEM v STR-TEM) do
9: $\quad$ add $\mathrm{BIC}_{T A R-V A R}\left(G_{\mathrm{nn}}, D\right)$ to the set of objective scores $\boldsymbol{S}$
10: end for
11: do $S_{G_{n}}=\overline{\boldsymbol{S}}$
12: if $S_{G_{n}}>S_{G}$ do $S_{G}=S_{G_{n}}$ and $G=G_{n}$
13: end for
14: if $S_{G}>S_{\max }$, do $S_{\max }=S_{G}$ and $G_{\max }=G$
15: end while
// Process for constraint VAR-REL; i.e., variables are relevant
16: if $K$ (VAR-REL) is not empty do
17: while independent subgraphs or unconnected variables in $G>1$ do
18: HC and return $G_{n}$ with an extra arc that minimally decreases $\mathrm{BIC}_{T A R-V A R}(G, D)$
19: $\quad G=G_{n}$
20: end while
// Process for constraints REL-BDN v STR-BDN; i.e., Bayesian Decision Networks (BDNs)
21: if $K$ (REL-BDN v STR-BDN) is not empty do
22: convert learnt graph to a BDN graph
23: if $K$ (STR-BDN) is not empty do
24: while a Decision has no child v a Utility has no parent in $G$ do
25: HC and return $G_{n}$ with an extra arc for a Decision/Utility that minimally decreases $\mathrm{BIC}_{T A R-V A R}(G, D)$
26: $\quad G=G_{n}$
27: end while

Algorithm 5: Greedy Equivalence Search (GES) algorithm applied to the DAG-space with additional pseudocode needed to account for the knowledge approaches highlighted in red font colour.
Input: dataset $D$, empty graph $G$, objective function $\mathrm{BIC}_{T A R-V A R}(G, D)$, max in-degree $M$, optional knowledge $K$ (DIR-EDG, UND-EDG, FOR-EDG, REL-TEM v STR-TEM, INI-GRA, VAR-REL, TAR-VAR, REL-BDN v STRBDN)
Output: DAG $G_{\max }$ that maximises $S_{G}=\mathrm{BIC}_{T A R-V A R}(G, D)$ in the search space of DAGs given $K$
1: if $K$ (INI-GRA) is not empty do $G=$ INI-GRA
2: else do $G+(K(\mathrm{DIR}-\mathrm{EDG})$ v randomise direction of $K(\mathrm{UND}-\mathrm{EDG})) \vDash D A G, M$
3: do $S_{G}=\mathrm{BIC}_{T A R-V A R}(G, D), S_{\max }=S_{G}$ and $G_{\max }=G$
4: while $S_{\max }$ increases do
5: for every arc addition in $G_{\max }$, bounded by CPSs, do
6: if $G_{\max } \vDash D A G, M, K$ (DIR-EDG, UND-EDG, FOR-EDG, REL-TEM v STR-TEM) do
7: $\quad S_{G_{n}}=\mathrm{BIC}_{T A R-V A R}\left(G_{n}, D\right)$
8: if $S_{G_{n}}>S_{\max }$ and $S_{G_{n}}>S_{G}$ do $G=G_{n}$, and $G_{\max }=G$
9: end for
10: if $S_{G}>S_{\max }$ do $S_{\max }=S_{G}$ and $G_{\max }=G$
11: end while
12: while $S_{\max }$ increases do
13: for every arc removal in $G_{\max }$ do
14: if $G_{\max } \vDash D A G, M, K$ (DIR-EDG, UND-EDG) do
15: $\quad S_{G_{n}}=\mathrm{BIC}_{T A R-V A R}\left(G_{n}, D\right)$
16: if $S_{G_{n}}>S_{\max }$ and $S_{G_{n}}>S_{G}$ do $G=G_{n}$, and $G_{\max }=G$
17: end for
18: if $S_{G}>S_{\max }$ do $S_{\max }=S_{G}$ and $G_{\max }=G$
19: end while
// Process for constraint VAR-REL; i.e., variables are relevant
20: if $K$ (VAR-REL) is not empty do
21: while independent subgraphs or unconnected variables in $G>1$ do
22: $\quad$ HC and return $G_{n}$ with an extra arc that minimally decreases $\mathrm{BIC}_{T A R-V A R}(G, D)$
23: $\quad G=G_{n}$
24: end while

# 5 Simulation and experiments 

The simulation and experiments cover a range of different possible situations one might encounter in practice. In summary, this section describes how each of the 10 knowledge approaches is applied, with varying levels of knowledge constraints, to each of the five algorithms described in Sect. 4. We consider graphical models that come from real case studies that vary in size and complexity, and use those models to generate synthetic data that vary in sample size under the assumption that the effect of knowledge might depend on the size of the available data.

We evaluate the impact of the first seven knowledge approaches enumerated in Table 1 empirically, determined by how they modify the learnt graph in relation to the ground truth graph. Each approach is evaluated independently, and the evaluation is based on constraints randomly sampled from the ground truth graph. The remaining three approaches TARVAR, REL-BDN and STR-BDN represent modelling preferences not necessarily assumed to improve causal structure, and because of this, it would be unreasonable to measure their usefulness in terms of graphical accuracy.

While continuous data has some advantages in terms of learning efficiency, our focus in this paper will be on discrete data that makes no assumptions about the underlying distributions

Table 4 The properties of the six networks


that generated the data, such as an assumption of normality. This is because real data sets are unlikely to be normally distributed, and typically capture many categorical variables. Moreover, all the networks considered in this study come from actual studies, and all the networks are discrete. Starting from the simplest case study, the six networks, which are taken from the Bayesys repository, ${ }^{5}$ are (a) the Asia network, (b) the Sports network, (c) the Property network, (d) the Alarm network, (e) the ForMed network, and (f) the Pathfinder network.

We consider these six networks suitable for this study for three reasons. Firstly, they represent real-world BNs from a wide range of disciplines taken from the literature, and this makes them appropriate for investigating the impact of knowledge. Secondly, we consider the size of these networks to be representative of most knowledge-based BNs that contain up to hundreds of variables; whereas larger networks containing thousands of variables are impractical for knowledge elicitation. Thirdly, the six networks offer a good range of old and new, as well as simple and complex, BNs that come from different domains. The properties of the six networks are depicted in Table 4, and show that the complexity of the networks ranges between 8 and 109 nodes, 8 and 195 arcs, 2 and 3.58 average degree, 2 and 6 maximum in-degree, and 18 and 71,890 free parameters that are used to approximate the dimensionality of a BN.

The experiments for the first seven knowledge approaches are based on synthetic data generated from the six BNs described above. All the six networks come with pre-defined parameters. Specifically, the networks Asia, Alarm and Pathfinder are based on knowledgebased parameters as defined in the relevant study that published the network, the parameters of the networks ForMed and Sports are based on real data, whereas the parameters of network Property were determined by clearly defined rules and regulating protocols involving property tax and other human-made housing market policies.

Synthetic data were sampled from these networks. Five sample sizes are considered for each network, ranging from 100 to 1 million samples; i.e., $10^{2}, 10^{3}, 10^{4}, 10^{5}$, and $10^{6}$. The different sample sizes enable us to investigate the impact of knowledge, on networks of varying complexity, given both limited and big data. Overall, the experiments associated with the first seven approaches are based on results obtained from learning 3245 graphs that required a total structure learning runtime of 44.89 days. Specifically, each of the ten knowledge approaches was applied to each of the five algorithms, with different rates of constraints as specified in Table 5, and in combination with the six case studies and five different sample sizes per case study.

[^0]
[^0]:    5 http://bayesian-ai.eecs.qmul.ac.uk/bayesys/.

Table 5 An example of the number of constraints simulated for each knowledge approach and rate combination, based on the Alarm network


Table 5 presents, as an example, the number of constraints simulated for the Alarm network, for each knowledge approach and corresponding rate of constraints combination. The rates of constraint selected are those deemed to be reasonable for each approach. For example, we assume that hard knowledge for approaches such as DIR-EDG is more likely to range between 5 and $50 \%$ of edges relative to those present in the true graph. Conversely, if a user decides to incorporate soft knowledge via INI-GRA, then it makes more sense that the rate of constraints would be higher and possibly ranging from 20 to $50 \%$. Therefore, comparisons about the impact of each of these approaches are measured overall, and across all rates of constraints sampled.

The constraints are randomly sampled from the ground truth graph. For example, the number of constraints in DIR-EDG and UND-EDG is determined relative to the number of edges in the true graph. Given that the Alarm network contains 46 edges, 23 of those edges are randomly selected as constraints when the rate is set to $50 \%$ (note the same edges are selected for both DIR-EDG and UND-EDG). For lower constraint rates, we sample part of those randomised at the $50 \%$ rate; e.g., at rate $20 \%$ we select the first nine edges of the 23 edges determined at $50 \%$ rate. While it can be argued that the number of forbidden edges (approach FOR-EDG) should be a percentage of the independencies (i.e., edges absent) in the ground truth graph, in an analogous approach to that used for edges present, we decided to follow the same quantities of constraints as in DIR-EDG and UND-EDG for consistency, but also because there are

$$
\frac{|V|(|V|-1)}{2}-a
$$

missing edges compared to the completely connected graph in a DAG, where $a$ is the number of edges and $V$ the variable set. For example, the Alarm network contains 620 missing edges, and it would represent an unrealistic scenario to sample $50 \%$ of those independencies as constraints.

Temporal information (i.e., approaches REL-TEM and STR-TEM) is trickier to sample and there are multiple ways this can be done. We followed a simple process where the number of tiers is determined by the DAG structure in which child nodes are always ordered under their parents, as illustrated in Fig. 3 with reference to the Sports network. We then sample a percentage of the variables (as opposed to edges) and assign them to a tier as illustrated in Fig. 3. Since temporal constraints require at least two variables as input, smaller networks such as Asia and Sports cannot be tested at lower rates of temporal constraints. This is because selecting just two, out of the eight or nine nodes available in the Asia and Sports networks respectively, corresponds to a rate higher than $5 \%$ and $10 \%$.

For INI-GRA we assume the rates of $20 \%$ and $50 \%$ (refer to Table 5) on the basis most users who select this approach would be intending to guess at least half of the graph. To enable unbiased comparisons between the different knowledge approaches, the experiments at the $50 \%$ rate reuse the same edges selected for the same rates in DIR-EDG and UND-EDG. Note that unlike the other approaches examined, INI-GRA represents a soft constraint that affects structure learning by specifying the starting position in the search space of graphs, and there is no guarantee it will preserve the input knowledge edge-set in the learnt output, unlike the DIR-EDG and UND-EDG approaches.

The remaining knowledge approaches operate somewhat differently than the rest. Specifically, approach VAR-REL involves no randomisation since it forces the algorithm to return a graph that contains no independent subgraphs or nodes. As a result, VAR-REL can be viewed as an approach that may constrain all of the variables, as indicated in Table 5. Moreover, it

![img-2.jpeg](img-2.jpeg)

Fig. 3 The ground truth graph of the Sports network with node rows corresponding to temporal tiers. The graph is generated in Bayesys which makes use of the Graphviz visualisation system [24]
also involves an unknown number of edges required to connect all the potentially independent subgraphs and nodes, indicated as ' $\geq 0$ ' under edge rate Varies in Table 5. Note this approach makes no difference to the output of SaiyanH, since it incorporates this approach by design.

Further to what has been discussed at the beginning of this section, the impact of approaches TAR-VAR, REL-BDN, and STR-BDN is not measured using synthetic data due to the nature of these approaches. Specifically, approach TAR-VAR is applied to two real health datasets where the target variables are driven by author needs, as indicated in the relevant publications $[16,29]$ which we discuss in more detail in Sect. 6, whereas the practicality of approaches REL-BDN and STR-BDN is shown via illustration of network modification.

# 6 Results and discussion 

The discussion of the results focuses on measuring the impact each knowledge approach has on structure learning. We investigate the impact of knowledge using different measures that tell us something about structure learning accuracy and model complexity, to answer the research questions discussed in Sect. 1. On this basis, the results are presented with a focus on the knowledge approaches and not with a focus on the algorithms, since the approaches

can be implemented in almost any algorithm. While each algorithm is expected to benefit differently, the general expectation is that the more accurate an algorithm is with a particular dataset, the less it is expected to benefit from knowledge.

We divide this section into three subsections. Section 6.1 presents the results from synthetic empirical evaluation of the first seven approaches described in Table 1, Sect. 6.2 illustrates the usefulness of TAR-VAR, and Sect. 6.3 the usefulness of REL-BDN and STR-BDN. To better understand the relative impact each knowledge approach has on each algorithm, Table 8 in "Appendix B" presents how each approach influences the learning performance of each algorithm under different measures.

Various criteria are used to evaluate the first seven approaches. To begin with, graphical accuracy is determined by three scoring metrics that quantify the accuracy of a learnt DAG with respect to the ground truth DAG. The first two metrics are the classic F1 and SHD scores. The third metric, the Balanced Scoring Function (BSF), is relatively new [17] and addresses the bias in graphical score present in other metrics. For example, the SHD score is known to be biased towards the sensitivity of identifying edges versus specificity. The BSF metric eliminates bias by taking into consideration all of the confusion matrix parameters, and balances the score between dependencies present and absent in the true graph. In practice, the BSF score ranges from -1 to 1 , where -1 corresponds to the worst possible graph; i.e., the reverse of the true graph that maximises False Positive (FP) and False Negative (FN) edges, and minimises True Positive (TP) and True Negative (TN) edges. Furthermore, 1 to the graph that matches the true graph, and 0 represents the ignorant case of an empty or a fully connected graph. It is calculated as follows:

$$
\mathrm{BSF}=0.5\left(\frac{\mathrm{TP}}{a}+\frac{\mathrm{TN}}{i}-\frac{\mathrm{FP}}{i}-\frac{\mathrm{FN}}{a}\right)
$$

where $a$ is the number of edges present and $i$ is the number of edges absent in the true graph, and $i$ is the output of Eq. 3; i.e., $i=\frac{|V|(|V|-1)}{2}-a$. Lastly, we assume that arc reversals generate half the penalty of arc deletions and arc additions, on the basis that an arc reversal represents correct dependency with incorrect directionality, and this assumption applies to all the three metrics.

Because structure learning algorithms tend to return a DAG which is consistent with the Complete Partial DAG (CPDAG), which represents a set of Markov equivalent DAGs, it is common to measure the performance of structure learning algorithms in terms of their ability to recover the true CPDAG, rather than the true DAG. This means that while CPDAG-based evaluation considers, for example, $A \rightarrow B \rightarrow C$ to be equivalent to both $A \leftarrow B \leftarrow C$ and $A \leftarrow B \rightarrow C$, a DAG evaluation does not. Because this paper focuses on the impact of knowledge, which we assume to be causal, we choose to measure this impact in terms of DAG structure so that we can differentiate between examples such as the above, since this is part of the purpose of considering knowledge. As we show in "Appendix C", however, a CPDAG-based evaluation generates very similar results to the DAG-based evaluation.

In addition to graphical accuracy, we measure the impact of knowledge in terms of model selection, using the BIC as defined in Eqs. 1 and 2 but excluding the optional term $r$ used for TAR-VAR, where a higher BIC score indicates a better model. We also consider the impact on the number of free parameters as defined in Eq. 2, as well as the difference in the number of arcs learnt. Lastly, we also measure the impact on runtime.

# 6.1 Evaluation of the first seven knowledge approaches in Table 1 

Figure 4 presents the average impact, with standard deviation superimposed, each of the first seven approaches had on the graphical accuracy of five algorithms and in terms of F1, BSF and SHD scores, as well as across all six case studies and five sample sizes. The impact is presented in terms of overall, as well as in terms of limited and big data. The motivation here was to investigate the usefulness of the knowledge approaches with different sample sizes relative to the complexity of the network. For example, the sample size of $10^{4}$ is considered
![img-3.jpeg](img-3.jpeg)

Fig. 4 The relative impact each knowledge approach has on structure learning performance, and over different rates of constraint, in terms of F1, BSF and SHD scores, where DIR-EDG is directed edges, UND-EDG is undirected edges, FOR-EDG is forbidden edges, REL-TEM is relaxed temporal order, STR-TEM is strict temporal order, INI-GRA is input graph, and VAR-REL is variables are relevant. Error lines represent standard deviation

'big' for the complexity of the Asia network, but 'limited' for the complexity of the Pathfinder network. For the networks Asia, Sports and Property, we assume a sample size of $10^{3}$ or lower represents limited data, whereas for the larger networks of Alarm, ForMed and Pathfinder we assume $10^{4}$ or lower represents limited data; sample sizes above these are assumed to represent big data (i.e., sufficient sample size).

The results suggest that the most useful approaches, in terms of improving the graphical accuracy of the learnt graph, are DIR-EDG, UND-EDG and INI-GRA, all of which involve information about edges, and approaches DIR-EDG and INI-GRA also include information about the direction of the edges. Approach DIR-EDG is the one that improves accuracy the most when performance is compared over the same rates of constraint, followed by approach INI-GRA which imposes soft constraints, and approach UND-EDG that entails less information than DIR-EDG and INI-GRA. Interestingly, when the data are limited, DIREDG at $50 \%$ rate outperforms INI-GRA at $50 \%$ rate, although this observation is relaxed or reverses for big data. This might be because when the algorithms explore the search space of DAGs with limited data, they are prone to less accurate model fitting scores and this presumably increases the level of modification the algorithms might perform on the initial graph, thereby the $50 \%$ input graph as a less effective soft constraint compared to the $50 \%$ rate of directed edges imposed as hard constraints.

On the other hand, the constraints that involve forbidden edges, either directly through approach FOR-EDG or indirectly through the temporal approaches REL-TEM and STRTEM, appear to be many times less effective compared to constraints that provide information about the presence of edges. This is not surprising since, in the case of temporal constraints, we are selecting relatively few edges to forbid from the relatively large number of edges absent in the ground truth graph. It is important to highlight that these constraints are found to be much more useful with big data rather than with limited data, and this is counterintuitive since knowledge is assumed to be more useful when available data are limited. Still, it can be explained by the fact that structure learning algorithms tend to produce a higher number of edges when trained with big data, and many of those edges could be false positives that these constraints may prohibit. On this basis, the observation that strict temporal order STR-TEM provides only marginal difference in impact relative to REL-TEM is not entirely surprising, since STR-TEM involves only a few more forbidden edges compared to those imposed by REL-TEM.

Lastly, VAR-REL is the only approach that tends to lower the accuracy of the learnt graphs. This result is not unexpected given that when this constraint was first introduced as a feature of SaiyanH, it was recognised that forcing the algorithm to connect all of the data variables implies that the additional forced edges may not be as accurate as those discovered unrestrictedly, and that the benefit of assuming the input variables are dependent comes in the form of practical usefulness by enabling full propagation of evidence [15]. In line with approaches FOR-EDG, REL-TEM and STR-TEM, approach VAR-REL has less detrimental effect with big data than limited data. This can be explained by the fact that less additional, but more accurate, forced edges are likely with big data, compared to the edges identified with limited data. Therefore, VAR-REL exchanges minor graphical accuracy for practical usefulness in the form of full propagation of evidence (not accounting for the accuracy of propagation), and where the risk of a negative effect on graphical accuracy decreases with sample size.

Figure 5 repeats the analysis of Fig. 4 and investigates the impact of constraints on the BIC score, the number of free parameters, and the number of arcs learnt. The higher standard deviation, including some inconsistencies observed in the results of UND-EDG could be due to randomisation; i.e., UND-EDG is the only approach that involves randomisation, since

![img-4.jpeg](img-4.jpeg)

Fig. 5 The relative impact each knowledge approach has on structure learning performance, and over different rates of constraint, in terms of BIC score, the number of free parameters, and the number of arcs learnt, where DIR-EDG is directed edges, UND-EDG is undirected edges, FOR-EDG is forbidden edges, REL-TEM is relaxed temporal order, STR-TEM is strict temporal order, INI-GRA is input graph, and VAR-REL is variables are relevant. Error lines represent standard deviation
the specified undirected edges are directed at random to form a valid initial graph. INI-GRA is the only approach that leads to meaningful improvements in the BIC score, although this improvement occurs only for big data. Moreover, the positive effect decreases at $50 \%$ rate of constraints; i.e., when the input graph matches the ground truth. Interestingly, while the impact on BIC appears to be rather marginal overall, it is considerably detrimental in the presence of limited data and further increases with the rate of constraints. This is because BIC is a model selection function that partly expresses how well the learnt distributions fit the data. Because the fitting between the learnt and observed distributions tends to increase with higher sample size, the constraints imposed in the presence of limited data force the

![img-5.jpeg](img-5.jpeg)

Fig. 6 The relative impact each knowledge approach has on structure learning runtime, and over different rates of constraint, where DIR-EDG is directed edges, UND-EDG is undirected edges, FOR-EDG is forbidden edges, REL-TEM is relaxed temporal order, STR-TEM is strict temporal order, INI-GRA is input graph, and VAR-REL is variables are relevant. Error lines represent standard deviation
learnt distributions to deviate from the observed distributions more strongly. This observation is also supported by the number of free parameters and the number of edges learnt, which both appear to increase faster when constraints are imposed with limited, as opposed to big, data; implying that the forced constraints must have increased the dimensionality penalty $p$ in BIC (refer to Eq. 2) faster than they increased the Log-Likelihood score (refer to Eq. 1).

Lastly, Fig. 6 repeats the previous analyses with reference to runtime. Overall, the results suggest that there is little benefit in runtime by imposing constraints in the process of structure learning. The only approach that appears to meaningfully reduce runtime is INI-GRA at $50 \%$ rate, and this is because it helps the algorithms to converge to a local or global maximum faster compared to starting from an empty graph. Overall, the results from runtime can be viewed as counterintuitive on the basis that constraints reduce the search space of graphs, and yet many of the constraints increase rather than decrease runtime. However, while it is true that the search space of graphs is reduced, there is no guarantee that the search space explored will be reduced. This is because the algorithms often explore only a minor proportion of the available search space, and the constraints might set up a tension between what the data indicate and what the constraints are trying to enforce, and this might cause the algorithms to explore different portions of the search space.

Moreover, the temporal approaches REL-TEM and STR-TEM appear to have significant negative repercussions on runtime. This is another result that may appear counterintuitive in the first instance. It is important to clarify that node-ordering algorithms that rely on complete information of the ordering of the variables, such as the K2 algorithm [19] generally reduce the search space of graphs from super-exponential to exponential [42] and hence, tend to reduce runtime ${ }^{6}$ considerably. Because the incomplete temporal ordering approaches implemented in this study extend the temporal checks to ancestral relationships for every graph explored, in addition to parental relationships, they increase computational complexity and runtime considerably, something which is avoided by algorithms such as K2 which assume a complete ordering.

[^0]
[^0]:    ${ }^{6}$ The computational complexity of node-ordering algorithms that do not rely on knowledge explore the graphs in different node-ordering spaces and hence, have a higher computational complexity than K2 depending on the number of node-orderings explored (Scanagatta, 2018).

# 6.2 Evaluation of knowledge approach TAR-VAR 

Approach TAR-VAR, which involves indicating one or more target variables of interest for which we would like to encourage the algorithm to discover more parents or causes, is evaluated using two real health datasets. These are (a) the forensic psychiatry dataset in [16] which captures data about released prisoners during and after release who suffer from serious mental health problems, and (b) the demographic and health survey dataset on livelihood factors associated with childhood diarrhoea in [29]. The forensic psychiatry dataset contains 56 variables and a sample size of 953 , thereby representing a case study with limited data, whereas the childhood diarrhoea dataset contains 28 variables and a sample size of 259,628, representing a case study with big data.

Both studies reported a variable deemed more important than all other variables. These are (a) the variable called Violence in the forensic psychiatry dataset which captures information about the risk of a prisoner becoming violent following their release into the community, and (b) the variable called DIA_HadDiarrhoea in the childhood diarrhoea dataset which captures information about whether a child had diarrhoea in two weeks preceding the survey data collection. Both studies focus on investigating the causal explanations with reference to the target variables. As described in Sect. 3, approach TAR-VAR enables us to relax the dimensionality penalty for variables of interest to discover a potentially higher number of causes, thereby improving its predictive accuracy and identification of intervention. This can be useful when algorithms produce too sparse a network, often due to limited data.

The dimensionality penalty is relaxed by increasing $r$ as defined in Eq. 2, where higher $r$ values encourage the algorithm to explore more complex Conditional Probability Tables (CPTs) for the target variable in terms of the number of free parameters, which in turn makes it more likely for the target variable to contain a higher number of parents in the learnt graph. Figure 7 presents the Markov blankets produced by HC, TABU and GES for target variable Violence (the first case study) over different $r$ inputs, including the standard scenario that involves no manipulation of the dimensionality penalty, when $r=1$. The Markov blanket of node Violence represents the node-set that contains all the information one needs to infer Violence, and consists of the parents of Violence, its children, and the parents of its children. Similarly, Figs. 8 and 9 present the results produced by SaiyanH and MAHC, respectively. These illustrations represent a classic example whereby available data are big in terms features and small in terms of sample size, and tend to produce sparse networks with smaller Markov blankets, such as those shown for case 'standard' in Figs. 7, 8, and 9. Sparse networks are often viewed inadequate for inference and intervention, and this is one of the reasons why practitioners often favour manual graphical construction of BN models applied to real data.

Table 6 presents information on how the number of free parameters is adjusted over the different $r_{i}$ inputs, and how they influence other parts of the network, with respect to the Markov blankets shown in Figs. 7, 8 and 9 across the five algorithms. The unweighted free parameter $p_{u}$ represents the number of free parameters when $r=1$ (i.e. the output is equal to the standard BIC when no variables are targeted as of interest), whereas the weighted $p_{w}$ represents the adjusted number of free parameters when $r>1$. For example, the dimensionality penalty of Violence is reduced from 16 to 8 when $r$ increases from 1 to 2 (i.e. divided by $r$ ) in all five algorithms, thereby encouraging structure learning to introduce one more parent of Violence as illustrated in Figs. 7, 8 and 9. While approach TAR-VAR is unlikely to modify other parts of the graph, since it is applied locally to a decomposable score such as the BIC, it is still possible for modifications other than those affecting the targeted variable to occasionally occur. Out of the 40 instances presented in Table 6, extra network modifications occurred in six of them. Three of those cases involve the TABU algorithm when

![img-6.jpeg](img-6.jpeg)

Fig. 7 The Markov blankets of target variable Violence produced by HC, TABU and GES (they produced the same Markov blankets), given the forensic psychiatry data, over different inputs $r_{i}$ while applying TAR-VAR (refer to Eq. 2)
![img-7.jpeg](img-7.jpeg)

Fig. 8 The Markov blankets of target variable Violence produced by SaiyanH, given the forensic psychiatry data, over different inputs $r_{i}$ while applying TAR-VAR (refer to Eq. 2)

![img-8.jpeg](img-8.jpeg)

Fig. 9 The Markov blankets of target variable Violence produced by MAHC, given the forensic psychiatry data, over different inputs $r_{i}$ while applying TAR-VAR (refer to Eq. 2)
$r_{i}=2,3,5$, the fourth case involves the SaiyanH algorithm when $r_{i}=4$, and the remaining two cases involve the MAHC algorithms when $r_{i}=2,8$. The additional modifications are minor and can be explained due to variability which arises by manipulating $B I C_{T A R-V A R}$ over different values of $r_{i}$, and this variability might cause $B I C_{T A R-V A R}$ to optimise at a neighbouring or at a slightly different graph.

Figures 10, 11, and 12, and Table 7 repeat the analysis of Figs. 7, 8 and 9 and Table 6, this time with application to the childhood diarrhoea dataset and with DIA_HadDiarrhoea set as the target variable. This represents a big data case study since it has a smaller number of variables and much larger sample size than the previous case study. The higher sample size partly explains why the Markov blankets in Figs. 10, 11, and 12 are more complex compared to those in Figs. 7, 8, and 9. This time, however, applying TAR-VAR on SaiyanH did not produce any additional edges for the target variable, whereas it did for the other three algorithms at a similar rate to the forensic psychiatry dataset. SaiyanH's Markov blanket ${ }^{7}$ remained static across the different $r_{i}$ inputs. This result can also be observed in Table 7 which shows that the unweighted number of free parameters $p_{u}$ remains static over $r_{i}$ for SaiyanH. The high sample size of the childhood diarrhoea dataset increases the Log-Likelihood component of the BIC score relative to the complexity component and in turn reduces the importance of $r_{i}$, thereby making it more difficult for changes in dimensionality penalty to have an impact on the learnt graph relative to the forensic psychiatry dataset.

The overall results suggest that TAR-VAR can also be useful in the presence of big data. Moreover, we found the influence of $r$ to be well-behaved in the sense that as $r$ increases so do the number of parents of the target variable, as one might hope.

[^0]
[^0]:    ${ }^{7}$ The Markov Blanket of SaiyanH was "BF_BreastfedMonths $\rightarrow$ DIA_HadDiarrhoea $\leftarrow$ GEO_Region".

Table 6 The impact on target variable Violence from the forensic psychiatry dataset over different inputs $r_{i}$, its parameters, inbound links and nearby graph, where $p_{u}$ is the unweighted (i.e., ignores $r_{i}$ ) number of free parameters of Violence, $p_{w}$ is the weighted (i.e., assumes $r_{i}$ ) number of free parameters of Violence, $p_{w g}$ is the weighted number of free parameters of the whole graph $S H D_{a}$ is the SHD score between the graph generated at $r_{i}$ and the graph generated without a target (i.e., when $r_{i}=1$ ), and $S H D_{b}$ is $S H D_{a}$ minus the additional parents of target variable Violence (i.e., it represents the number of graphical modifications occurred in the graph excluding the edges entering the target variable). Refer to Figs. 7, 8, and 9 for the corresponding Markov blankets of Violence


Table 6 (continued)


![img-9.jpeg](img-9.jpeg)

Fig. 10 The Markov blankets of target variable DIA_HadDiarrhoea produced by HC and TABU (they produced the same Markov blankets) given the childhood diarrhoea dataset, over different inputs $r_{i}$ while applying TARVAR (refer to Eq. 2)
![img-10.jpeg](img-10.jpeg)

Fig. 11 The Markov blankets of target variable DIA_HadDiarrhoea produced by MAHC given the childhood diarrhoea dataset, over different inputs $r_{i}$ while applying TAR-VAR (refer to Eq. 2)

# 6.3 Evaluation of knowledge approaches REL-BDN and STR-BDN 

Lastly, the effect of approaches REL-BDN and STR-BDN is illustrated graphically in Fig. 13, based on the Asia network with a sample size of $10^{4}$, and with application to the five algorithms HC, TABU, SaiyanH, MAHC and GES. BDNs are often developed manually and may include decision nodes not available in the data. However, it is possible for both decision and utility variables to be present in the data, and approaches REL-BDN and STR-BDN become useful under this scenario. With reference to Fig. 13, the graphs:
(a) in the first row represent the standard graphical output generated by each algorithm in the absence of constraints;
(b) in the second row represent the graphical outputs after applying REL-BDN to each of the algorithms, where in this hypothetical example node asia serves as the decision node and node smoke as the utility node;

![img-11.jpeg](img-11.jpeg)

Fig. 12 The Markov blankets of target variable DIA_HadDiarrhoea produced by GES given the childhood diarrhoea dataset, over different inputs $r_{i}$ while applying TAR-VAR (refer to Eq. 2)
(c) in the third row represent the graphical outputs after applying STR-BDN to each of the algorithms, for the same decision and utility nodes as in REL-BDN.

Note that nodes asia and smoke are constrained as decision and utility nodes, respectively, purely for illustration purposes. As shown in Fig. 13, the modifications applied by REL-BDN (second row) are restricted to visual representation and do not affect the graphical structure of the graph. Approach REL-BDN simply involves automatically reformatting the graphical output to incorporate knowledge of decisions and utilities present in the data, and converting conditional arcs entering decisions into informational arcs. On the other hand, approach STR-BDN (third row) constrains structure learning by requiring that decision nodes have at least one child, and utility nodes have at least one parent. These constraints are based on the assumption that decision nodes must have at least an effect node in the dataset, and utility nodes must have at least one cause in the data.

For example, Fig. 13 shows that HC with REL-BDN produces a graph in which decision node asia has no child, and this can be a problem in practice when we automatically convert learnt graphs into parameterised ${ }^{8}$ BDNs, since the specified decision node will have no effect in the network. On the other hand, the same HC algorithm ensures that node asia does have a child node when paired with STR-BDN. Note that while in the case of HC and SaiyanH this was achieved by introducing just one additional arc, in the case of TABU and MAHC this constraint was satisfied after adding two arcs. This is because STR-BDN forces the algorithm to keep adding arcs that minimally decrease the BIC score until both constraints are satisfied. Because the arc that minimises BIC will not necessarily be the arc that is needed for the constraint to be satisfied, multiple arcs may have to be introduced before the constraint is met, as in the example with TABU and MAHC.

[^0]
[^0]:    ${ }^{8}$ Our implementation has been extended to include parameterisation of the learnt BDN graphs into BDN models that have the appropriate file extensions to be loaded in the third-party BN software engines AgenaRisk and GeNIe. However, this is out of the scope of this paper. Details can be found in the Bayesys user manual (Constantinou, 2019).

Table 7 The impact on target variable DIA_HadDiarrhoea from the childhood diarrhoea dataset over different inputs $r_{i}$, its parameters, inbound links and nearby graph, where $p_{u}$ is the unweighted (i.e., ignores $r_{i}$ ) number of free parameters of DIA_HadDiarrhoea, $p_{w}$ is the weighted (i.e., assumes $r_{i}$ ) number of free parameters of DIA_HadDiarrhoea, $p_{w g}$ is the weighted number of free parameters of the whole graph, $S H D_{a}$ is the SHD score between the graph generated at $r_{i}$ and the graph generated without a target (i.e., when $r_{i}=1$ ), and $S H D_{b}$ is $S H D_{a}$ minus the additional parents of target variable Violence (i.e., it represents the number of graphical modifications occurred in the graph excluding the edges entering the target variable). Refer to Figs. 10, 11, and 12 for the corresponding Markov blankets of DIA_HadDiarrhoea

| $r_{i}$ for target
DIA_HadDiarrhoea | HC |  |  |  |  |  | TABU |  |  |  |  |  |  |

Table 7 (continued)


![img-12.jpeg](img-12.jpeg)

Fig. 13 The learnt Asia graphs produced by the five algorithms (a) in the absence of constraints shown on the left, $\mathbf{b}$ given approach REL-BDN with nodes asia and smoke set as decision and utility nodes, respectively, shown in the middle, and $\mathbf{c}$ given approach STR-BDN for the same decision and utility nodes shown on the right

# 7 Concluding remarks 

This paper introduced some novel and some existing knowledge approaches. In total, we have implemented and evaluated 10 knowledge approaches that impose soft or hard constraints on BNSL algorithms. These knowledge approaches enable users to perform BNSL by considering both data and knowledge that could be obtained from heterogeneous sources with different conceptual, contextual and typographical representation. The insights obtained through evaluation can be used to inform decision-making about which type of knowledge

might be most beneficial and under what data settings, and to answer the research questions discussed in Sect. 1.

The implementations are made available in the open-source Bayesys structure learning system [14]. The knowledge approaches have been tested by implementing them within the process of five structure learning algorithms available in Bayesys. We have evaluated the effectiveness and efficiency of these approaches by testing their impact on structure learning in terms of graphical accuracy, model fitting, complexity, and runtime, over various synthetic and real datasets with varied levels of complexity and sample size. To the best of our knowledge, this paper provides the first broad evaluation of different knowledge approaches for BNSL.

The results show that, amongst the knowledge approaches investigated, the most useful in terms of improving the graphical accuracy of the learnt graph is approach DIR-EDG (Directed edge) that captures information about the existence and direction of edges. DIREDG not only represents one of the most widely used knowledge approaches in the literature, but also represents one of the simplest approaches. As illustrated in Fig. 14 which provides a concluding summary, this is also true when we plot the gain in graphical accuracy relative to the number of edges or variables specified as constraints (i.e. the pieces of knowledge) imposed by the different knowledge approaches; although in this case the value of knowledge through the INI-GRA (Initial graph) approach is only marginally behind DIR-EDG (Directed Edge).

Furthermore, the results show that while most approaches become less effective in the presence of big data, presumably because learning accuracy increases with sample size thereby rendering knowledge less important, some approaches perform better still in the presence of big data. While this is counterintuitive, it is explained by the higher number of edges the algorithms generate when the input data are 'big'. In these cases, approaches that forbid edges,
![img-13.jpeg](img-13.jpeg)

Fig. 14 Concluding summary of the gain in graphical accuracy relative to the number of edges or variables specified as constraints imposed by each knowledge approach, as an average across all case studies and algorithms. In this plot, the graphical accuracy represents the average logarithmic fit across the F1, BSF and SHD metrics

for example, can help algorithms avoid discovering false positives edges; a phenomenon that becomes more prevalent with increasing sample size [34].

Amongst the main conclusions is the observation that reduced search space due to knowledge does not imply reduced computational complexity. In fact, our results suggest that in many cases the incorporation of knowledge increases runtime. While the increase in runtime can partly be explained by the additional computation needed to apply and search for constraints, it also suggests that the number of graphs explored increases, or that the actual graphs explored in the presence of constraints are more complex (i.e. contain a higher number of free parameters) which require a higher computational effort to be scored. This can happen when the constraints set up a tension between what the data indicate and what the constraints are trying to enforce, and which becomes more likely when the sample size of the input data is limited, irrespective of the accuracy of the constraints. As the BIC score comparisons show (refer to Fig. 5), incorporating knowledge tends to decrease score fitting while at the same time increase graphical accuracy. This phenomenon is particularly evidenced in the presence of limited data, where objective functions such as the BIC tend to be less effective.

This study comes with some limitations, all of which can also be viewed as directions for future research. Regarding the density and size of the networks, the analysis is based on networks containing up to hundreds of nodes, hundreds of edges, with an average degree up to 3.58 , a maximum in-degree up to 6 , and up to 71,890 free parameters. While we consider the selected networks to be well within the complexity range of most knowledge-based BNs found in the literature, our analysis did not consider denser networks containing thousands of variables, which are typically found in bioinformatics. These larger networks are out of the scope of this paper for two reasons. Firstly, networks of this size require specialised algorithms that maximise learning efficiency, often at the expense of accuracy, which are not considered in this paper. Secondly, and perhaps more importantly, it is well documented that knowledge elicitation can be time consuming even when applied to networks containing tens of variables. On this basis, we assume that it would be impractical to expect users to elicit knowledge for networks containing thousands of variables. Moreover, the impact of knowledge is investigated by applying the different knowledge approaches to the five algorithms that are available in Bayesys; three score-based algorithms, a model-averaging score-based algorithm, and a hybrid learning algorithm. While most of the results appear to be rather consistent across algorithms, we cannot claim that these results extend to all other algorithms. Lastly, all algorithms were employed using the BIC score as the objective function to ensure consistency in measuring the impact on objective scores. While the algorithms are found to behave similarly irrespective of the selection of the objective function [35], some algorithms may be more sensitive than others to the objective score in the presence of limited data [44].

It is important to highlight that knowledge elicitation comes with disadvantages, such as requiring access to expertise which tends to increase effort, cost, and project duration. Moreover, because knowledge can be subjective and inconsistent between experts, some problems may require access to multiple domain experts to reduce the uncertainty of knowledge elicited. Because of these reasons, we have avoided implementing approaches that require experts to provide subjective probabilities as prior beliefs, such as those covered in [1, 6, 7, 28, 37], and this can be viewed as a limitation of this study.

Lastly, most of the results presented in this study assume constraints sampled from ground truth graphs. While this assumption is in line with some other past studies, it influences the results in two conflicting ways. Firstly, because knowledge is sampled from the error-free ground truth graphs, their positive effect tends to be overestimated. Secondly, and in contrast to the first point, because structure learning is based on synthetic data which is known to

overestimate real-world performance, it tends to underestimate the benefits of knowledge since higher learning accuracy renders knowledge less useful. While it is not possible to know the relationship between these two conflicting effects, there is clearly a cancelling effect. Still, the results presented in this paper provide us with valuable insights in terms of how the impact of one knowledge approach relates to another, irrespective of the underlying knowledge and data assumptions discussed above.

Acknowledgements This research was supported by the EPSRC Fellowship project EP/S001646/1 on Bayesian Artificial Intelligence for Decision-Making under Uncertainty.

Author contributions Dr Anthony Constantinou: Conceptualization, Methodology, Software, Data curation, Formal analysis, Original draft preparation, Supervision, Funding acquisition. Dr Zhigao Guo: Conceptualization and Reviewing. Dr Neville Kitson: Conceptualization, Reviewing and Editing.

# Declarations 

Conflict of interest The authors declare no conflict of interest.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

## Appendix A: Supplementary description for SaiyanH

The material that follows is based on the description of SaiyanH presented in [15]. The Mean/Max/MeanMax Marginal Discrepancy $(M M D)$ score represents the discrepancy in marginal probabilities between prior and posterior distributions, and ranges from 0 to 1 where a higher score indicates a stronger dependency. For edge $A \leftrightarrow B$, the score $M M D(A \leftrightarrow B)$ is the average of scores $M M D_{M N}(A \leftrightarrow B)$ and $M M D_{M X}(A \leftrightarrow B)$, where $M N$ and $M X$ are mean and max marginal discrepancies. Specifically,

$$
M M D(A \leftrightarrow B)=\sum \sum_{m} M M D_{m}(A \leftrightarrow B) w
$$

where $\leftrightarrow$ represents the iterations over $\leftarrow$ and $\rightarrow, m$ represents the iterations over $M N$ and $M X$, and $w$ is the normalising constant 0.25 applied to the scores accumulated over the following four iterations:

$$
\begin{gathered}
M M D_{M N}(A \rightarrow B)=\left(\sum_{j}^{s_{A}}\left[\left(\sum_{i}^{s_{B}}\left|P\left(B_{i}\right)-P\left(B_{i} \mid A_{j}\right)\right|\right) / s_{B}\right]\right) / S_{A} \\
M M D_{M N}(A \leftarrow B)=\left(\sum_{i}^{s_{B}}\left[\left(\sum_{j}^{s_{A}}\left|P\left(A_{j}\right)-P\left(A_{j} \mid B_{i}\right)\right|\right) / S_{A}\right]\right) / s_{B} \\
M M D_{M X}(A \rightarrow B)=\left(\sum_{j}^{s_{A}} \max _{i}\left|P\left(B_{i}\right)-P\left(B_{i} \mid A_{j}\right)\right|\right) / S_{A}
\end{gathered}
$$

$$
M M D_{M X}(A \leftarrow B)=\left(\sum_{i}^{s_{B}} \max _{j}\left|P\left(A_{j}\right)-P\left(A_{j} \mid B_{i}\right)\right|\right) / s_{B}
$$

for each state $j$ in $A$ and state $i$ in $B$, and over the $S_{A}$ states in $A$ and $S_{B}$ states in $B$.
The Extended Maximum Spanning Graph (EMSG) is determined by the $M M D$ scores described above, and can be viewed a more complex version of the maximum spanning tree that preserves multiple connecting paths from one node to another (unlike the maximum spanning tree which preserves the single and most likely connecting path between nodes). Starting from a complete graph, the EMSG is produced by removing edges between two nodes $A$ and $B$ if and only if $A$ and $B$ share neighbour $C$ where

$$
M M D(A \leftrightarrow C)>M M D(A \leftrightarrow B)<M M D(B \leftrightarrow C)
$$

The order in which the edges are assessed for removal is from lowest to highest $M M D$ score.

# Appendix B: Supplementary results 

See Table 8 .

Table 8 The relative impact knowledge approaches have on structure learning performance, per algorithm, in terms of F1, BSF and SHD scores (overall), where DIR-EDG is directed edge constraints, UND-EDG is undirected edge constraints, FOR-EDG is forbidden edges, REL-TEM is relaxed temporal order, STR-TEM is strict temporal order, INI-GRA is input graph, and VAR-REL is variables are relevant. Positive percentages represent improvements


Table 8 (continued)


Table 8 (continued)


Table 8 (continued)


Table 8 (continued)


# Appendix C: Impact of knowledge on graphical scores 

See Fig. 15.
![img-14.jpeg](img-14.jpeg)

Fig. 15 The relative impact each knowledge approach has on structure learning performance, and over different rates of constraint, in terms of average graphical accuracy representing the average across F1, BSF and (invert) SHD scores. The graph on the left represents the DAG score results, and the graph on the right the CPDAG score results. Error lines represent standard deviation

## Appendix D: Glossary

See Table 9.

Table 9 Glossary of abbreviations, symbols, and knowledge approaches


Table 9 (continued)


Table 9 (continued)

