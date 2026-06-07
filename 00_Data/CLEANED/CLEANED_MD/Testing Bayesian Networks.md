# Testing Bayesian Networks 

Clément L. Canonne Ilias Diakonikolas Daniel M. Kane Alistair Stewart ${ }^{* 15}$<br>January 28, 2020


#### Abstract

This work initiates a systematic investigation of testing high-dimensional structured distributions by focusing on testing Bayesian networks - the prototypical family of directed graphical models. A Bayesian network is defined by a directed acyclic graph, where we associate a random variable with each node. The value at any particular node is conditionally independent of all the other non-descendant nodes once its parents are fixed. Specifically, we study the properties of identity testing and closeness testing of Bayesian networks. Our main contribution is the first non-trivial efficient testing algorithms for these problems and corresponding informationtheoretic lower bounds. For a wide range of parameter settings, our testing algorithms have sample complexity sublinear in the dimension and are sample-optimal, up to constant factors.


[^0]
[^0]:    *An extended abstract of this work was presented at the 30th Conference on Learning Theory, COLT 2017 [CDKS17].
    ${ }^{\dagger}$ C. L. Canonne is with IBM Research; part of this work was performed while he was a postdoctoral fellow at Stanford University, and before that a graduate student at Columbia University.
    ${ }^{\ddagger}$ I. Diakonikolas is with the University of WisconsinMadison; this work was performed while he was at the University of Southern California.
    ${ }^{\S}$ A. Stewart is with Web3 Foundation; this work was performed while he was a postdoctoral researcher at the University of Southern California.
    ${ }^{4}$ D. M. Kane is with the University of California, San Diego.

# Contents 

1 Introduction ..... 4
1.1 Background ..... 4
1.2 This Work: Testing High-Dimensional Structured Distributions ..... 5
1.3 Related Work ..... 6
1.4 Basic Notation and Definitions ..... 7
2 Our Results and Techniques ..... 8
2.1 Main Results ..... 8
2.2 Organization ..... 11
2.3 Concurrent and Independent Work ..... 11
3 Preliminaries ..... 11
4 Testing Identity of Product Distributions ..... 14
4.1 Identity Testing Algorithm ..... 14
4.2 Sample Complexity Lower Bound for Identity Testing ..... 19
5 Testing Closeness of Product Distributions ..... 21
5.1 Closeness Testing Algorithm ..... 21
5.2 Sample Complexity Lower Bound for Closeness Testing ..... 29
5.3 Ruling Out Tolerant Testing Without Balancedness ..... 31
6 From Product Distributions to Bayes nets: an Overview ..... 32
7 Testing Identity of Fixed Structure Bayes Nets ..... 35
7.1 Identity Testing Algorithm ..... 35
7.2 Sample Complexity Lower Bound ..... 42
8 Testing Identity of Unknown Structure Bayes Nets ..... 43
8.1 Sample Complexity Lower Bound ..... 43
8.2 Identity Testing Algorithm against Non-Degenerate Bayes Nets ..... 48
8.2.1 The Case of Trees ..... 48
8.2.2 The Case of Bounded Degree ..... 52
9 Testing Closeness of Bayes Nets ..... 59
9.1 Fixed Structure Bayes Nets ..... 59
9.2 Unknown Structure Bayes Nets ..... 61
10 Identity and Closeness Testing for High-Degree Bayes Nets ..... 62
A Sample Complexity of Learning Bayesian Networks ..... 70
A. 1 Sample Complexity Upper Bound ..... 70
A. 2 Sample Complexity Lower Bound ..... 71
B Omitted Proofs from Section 4.2 ..... 72

C Omitted Proofs from Section 3 ..... 75
D Omitted Proofs from Sections 4.2 and 8.2 ..... 78

# 1 Introduction 

### 1.1 Background

Distribution testing has its roots in statistical hypothesis testing [NP33, LR05] and was initiated in [GR00, BFR ${ }^{+} 00$ ]. The paradigmatic problem in this area is the following: given sample access to an arbitrary distribution $P$ over a domain of size $N$, determine whether $P$ has some global property or is "far" from any distribution having the property. A natural way to solve this problem would be to learn the distribution in question to good accuracy, and then check if the corresponding hypothesis is close to one with the desired property. However, this testing-via-learning approach requires $\Omega(N)$ samples and is typically suboptimal. The main goal in this area is to obtain sampleoptimal testers - ideally, testers that draw $o(N)$ samples from the underlying distribution. During the past two decades, a wide range of properties have been studied, and we now have sample-optimal testers for many of these properties [Pan08, CDVV14, VV14, DK16, DGPP16].

We remark that even for the simplest properties, e.g., identity testing, at least $\Omega(\sqrt{N})$ many samples are required for arbitrary distributions over $N$ atoms. While this is an improvement over the $\Omega(N)$ samples required to learn the distribution, a sample upper bound of $O(\sqrt{N})$ is still impractical if $N$ is very large. For example, suppose that the unknown distribution is supported on $\{0,1\}^{n}$. For this high-dimensional setting, a sample complexity bound of $\Theta\left(2^{n / 2}\right)$ quickly becomes prohibitive, when the dimension increases. Notably, the aforementioned $\Omega(\sqrt{N})$ sample lower bound characterizes worst-case instances, which in many cases are unlikely to arise in real-world data. This observation motivates the study of testing structured distribution families, where significantly improved testers may be possible. Hence, the following natural question arises: Can we exploit the structure of the data to perform the desired testing task more efficiently?

A natural formalization of this question involves viewing the data as samples from a probabilistic model - a model that we believe represents the random process generating the samples. The usual assumption is that there exists a known family of probabilistic models - describing a set of probability distributions - and that the data are random samples drawn from an unknown distribution in the family. In this context, the distribution testing problem is the following: Let $\mathcal{C}$ be a family of probabilistic models. The testing algorithm has access to independent samples from an unknown $P \in \mathcal{C}$, and its goal is to output "yes" if $P$ has some property $\mathcal{P}$, and output "no" if the total variation distance, $d_{\mathrm{TV}}(P, Q) \stackrel{\text { def }}{=}(1 / 2)\|P-Q\|_{1}$, where $\|\cdot\|_{1}$ denotes the $L_{1}$-norm, is at least $\epsilon$ to every $Q \in \mathcal{C}$ that has property $\mathcal{P}$. The sample complexity of this structured testing problem depends on the underlying family $\mathcal{C}$, and we are interested in obtaining efficient algorithms that are sample optimal for $\mathcal{C}$.

More than a decade ago, Batu, Kumar, and Rubinfeld [BKR04] considered a specific instantiation of this broad question - testing the equivalence between two unknown discrete monotone distributions - and obtained a tester whose sample complexity is poly-logarithmic in the domain size. A recent sequence of works [DDS ${ }^{+} 13$, DKN15b, DKN15a] developed a framework to obtain sample-optimal estimators for testing the identity of structured distributions over total orders (e.g., univariate multi-modal or log-concave distributions). The main lesson of these works is that, under reasonable structural assumptions, the sample complexity of testing may dramatically improve becoming sub-logarithmic or even independent of the support size. Moreover, in all studied cases, one obtains testers with sub-learning sample complexity.

# 1.2 This Work: Testing High-Dimensional Structured Distributions 

This paper initiates a systematic investigation of testing properties of high-dimensional structured distributions. One of the most general formalisms to succinctly represent such distributions is provided by probabilistic graphical models [WJ08, KF09]. Graphical models compactly encode joint probability distributions in high dimensions. Formally, a graphical model is a graph where we associate a random variable with each node. The key property is that the edge-structure of the graph determines the dependence relation between the nodes.

The general problem of inference in graphical models is of fundamental importance and arises in many applications across several scientific disciplines, see [WJ08] and references therein. In particular, the task of learning graphical models has been extensively studied [Nea03, DSA11]. A range of information-theoretic and algorithmic results have been developed during the past five decades in various settings, see, e.g., [CL68, Das97, FY96, FGG97, FLN00, CGK ${ }^{+} 02$, Chi02, Mar03, AKN06, WRL06, AHHK12, SW12, LW12, DKS16b] for a few references. In contrast, the general question of testing graphical models has received less attention. We propose the following broad set of questions: ${ }^{1}$

Question 1. Let $\mathcal{C}$ be a family of high-dimensional graphical models and $\mathcal{P}$ be a property of $\mathcal{C}$. What is the sample complexity of testing whether an unknown $P \in \mathcal{C}$ has property $\mathcal{P}$ ? Can we develop testers for $\mathcal{P}$ with sub-learning sample complexity? Can we design sample-optimal and computationally efficient testers?

We believe that Question 1 points to a fundamental research direction that warrants study for its own sake. Moreover, as we explain in the following paragraphs, such estimation tasks arise directly in various practical applications across the data sciences, where sample efficiency is of critical importance. Hence, improved estimators for these tasks may have implications for the analysis of datasets in these areas.

For concreteness, Question 1 refers to a single unknown distribution that we have sample access to. We are also naturally interested in the broader setting of testing properties for collections of distributions in $\mathcal{C}$. Before we proceed to describe our contributions, a few comments are in order: As previously mentioned, for all global properties of interest (e.g., identity, independence, etc.), the sample complexity of testing the property is bounded from above by the sample complexity of learning an arbitrary distribution from $\mathcal{C}$. Hence, the overarching goal is to obtain testers that use fewer samples than are required to actually learn the model - or to prove that this is impossible. On a related note, in the well-studied setting of testing arbitrary discrete distributions, the main challenge has been to devise sample-optimal testers; the algorithmic aspects are typically straightforward. This is no longer the case in the high-dimensional setting, where the combinatorial structure of the underlying model may pose non-trivial algorithmic challenges.

In this work, we start this line of inquiry by focusing on testing Bayesian networks [Pea88] (Bayes nets or BN for brevity), the prototypical family of directed graphical models. Bayesian networks are used for modeling beliefs in many fields including robotics, computer vision, computational biology, natural language processing, and medicine [JN07, KF09]. Formally, a Bayesian network is defined by a directed acyclic graph (DAG) $\mathcal{S}=(V, E)$, where we associate a random variable with each node. Moreover, the value at any particular node is conditionally independent of all the other

[^0]
[^0]:    ${ }^{1}$ In what follows, by learning we refer to the task of, given i.i.d. samples from an arbitrary distribution $P \in \mathcal{C}$, outputting a hypothesis distribution $\hat{P}$ such that, with high probability, $P$ and $\hat{P}$ are close. The number of samples required for this task is then the sample complexity of learning $\mathcal{C}$.

non-descendant nodes once its parents are fixed. Hence, for a fixed topology, it suffices to specify each node's conditional distribution, for each configuration of its parents' values.

The main problems that we study in this setting are the related tasks of testing identity and closeness: In identity testing, we are given samples from an unknown Bayes net $P$ and we want to distinguish between the case that it is identical to versus significantly different from an explicitly given Bayes net $Q$. In closeness testing, we want to test whether two unknown Bayes nets $P, Q$ are identical versus significantly different. We believe that our techniques can be naturally adapted to test other related properties (e.g., independence), but we have not pursued this direction in the current paper. A related testing problem that we consider is that of structure testing: given samples from an unknown Bayes net $P$, we want to test whether it can be represented with a given graph structure $\mathcal{S}$ or is far from any Bayes net with this structure.

In the prior work on testing unstructured discrete distributions, the natural complexity measure was the domain size of the unknown distributions. For the case of Bayes nets, the natural complexity measures are the number of variables (nodes of the DAG) - denoted by $n$ - the maximum in-degree of the DAG - denoted by $d$ - and the alphabet size of the discrete distributions on the nodes. To avoid clutter in the expressions, we focus on the natural setting that the random variables associated with each node are Bernoulli's, i.e., the domain of the underlying distributions is $\{0,1\}^{n}$. (As we will point out, our bounds straightforwardly extend to the case of general alphabets with a necessary polynomial dependence on the alphabet size.)

We note that Bayes nets are a universal representation scheme: Any distribution over $\{0,1\}^{n}$ can be presented as a BN, if the maximum in-degree $d$ of the graph is unbounded. (Indeed, for $d=n-1$, one can encode all distributions over $\{0,1\}^{n}$.) In fact, as we will see, the sample complexity of testing scales exponentially with $d$. Therefore, an upper bound on the maximum in-degree is necessary to obtain non-trivial upper bounds. Indeed, the most interesting regime is the settting where the number of nodes $n$ is large and the degree $d$ is small. In applications of interest, this assumption will be automatically satisfied. In fact, as we explain in the following subsection, in many relevant applications the maximum in-degree is either 1 (i.e., the underlying graph is a tree) or bounded by a small constant.

# 1.3 Related Work 

We partition the related work intro three groups corresponding to research efforts by different communities.

Computer Science A large body of work in computer science has focused on designing statistically and computationally efficient algorithms for learning structured distributions in both low and high dimensions [Das99, FM99, AK01, VW02, CGG02, MR05, MV10, BS10, DDS12a, DDS12b, CDSS13, DDO ${ }^{+} 13$, CDSS14a, CDSS14b, HP15, ADLS17, DDS15, DDKT16, DKS15, DKS16a]. On the other hand, the vast majority of the literature in distribution property testing during the past two decades focused on arbitrary discrete distributions, where the main complexity measure was the domain size. See $\left[\mathrm{BFR}^{+} 00, \mathrm{BFF}^{+} 01\right.$, Bat01, BDKR02, BKR04, Pan08, VV11, DDS ${ }^{+} 13, \mathrm{ADJ}^{+} 11$, LRR11, ILR12, CDVV14, VV14, ADK15, CDGR18, DK16] for a sample of works, or [Rub12, Can15] for surveys.

A line of work [BKR04, DDS ${ }^{+} 13$, DKN15b, DKN15a] studied properties of one-dimensional structured distribution families under various "shape restrictions" on the underlying density. In the high-dimensional setting, Rubinfeld and Servedio [RS05] studied the identity testing problem

for monotone distributions over $\{0,1\}^{n}$. It was shown in [RS05] that poly $(n)$ samples suffice for the case of uniformity testing, but the more general problems of identity testing and independence testing require $2^{\Omega(n)}$ samples. Subsequently, Adamaszek, Cjumaj, and Sohler [ACS10] generalized these results to continuous monotone distributions over $[0,1]^{n}$. A related, yet distinct, line of work studied the problem of testing whether a probability distribution has a certain structure [BKR04, BFRV11, ADK15, CDGR18]. The sample complexity bounds in these works scale exponentially with the dimension.

Statistics The area of hypothesis testing for high-dimensional models has a long history in statistics and is currently an active topic of study. A sequence of early and recent works, starting with [Wei60, Bic69, LS93], has studied the problem of testing the equivalence between two nonparametric high-dimensional distributions in the asymptotic regime. In the parametric setting, Hotelling's T-squared statistic [Hot31] is the classical test for the equivalence of two highdimensional Gaussians (with known and identical covariance). However, Hotelling's test has the serious defect that it fails when the sample size is smaller than the dimension of the data [BS96]. Recent work has obtained testers that, under a high-dimensional Gaussian model (with known covariance), succeed in the sub-linear regime for testing identity [SD08] and closeness [CQ10]. A number of more recent works study properties of covariance matrices [CM13], regression [JM14], and linear independence testing [RISW16].

Applications The problems of testing identity and closeness of Bayesian networks arise in a number of applications where sample efficiency is critical [FLN00, GWJ03, SK03, Alm10, NLR11, RESG14, SM15, $\mathrm{YGM}^{+} 15$ ]. In bioinformatics applications (e.g., gene set analysis), each sample corresponds to an experiment that may be costly or ethically questionable $\left[\mathrm{YGM}^{+} 15\right]$. Specifically, $\left[\mathrm{YGM}^{+} 15\right]$ emphasizes the need of making accurate inferences on tree structured Bayesian networks, using an extremely small sample size - significantly smaller than the number of variables (nodes). [Alm10] studies the problem of testing closeness between two unknown Bayesian network models in the context of a biology application, where Bayes nets are used to model gene expression data. The motivation in [Alm10] comes from the need to compare network models for a common set of genes under varying phenotypes, which can be formulated as the problem of testing closeness between two unknown Bayes nets. As argued in [Alm10], due to the small sample size available, it is not feasible to directly learn each BN separately.

# 1.4 Basic Notation and Definitions 

Consider a directed acyclic graph (DAG), $\mathcal{S}$, with $n$ vertices that are topologically sorted, i.e., labelled from the set $[n] \stackrel{\text { def }}{=}\{1,2, \ldots, n\}$ so that all directed edges of $\mathcal{S}$ point from vertices with smaller label to vertices with larger label. A probability distribution $P$ over $\{0,1\}^{n}$ is defined to be a Bayesian network (or Bayes net) with dependency graph $\mathcal{S}$ if for each $i \in[n]$, we have that $\operatorname{Pr}_{X \sim P}\left[X_{i}=1 \mid X_{1}, \ldots, X_{i-1}\right]$ depends only on the values $X_{j}$, where $j$ is a parent of $i$ in $\mathcal{S}$. Such a distribution $P$ can be specified by its conditional probability table, i.e., the vector of conditional probabilities of $X_{i}=1$ conditioned on every possible combination of values to the coordinates of $X$ at the parents of $i$.

To formalize the above description, we use the following terminology. We will denote by $\operatorname{Par}(i)$ the set of parents of node $i$ in $\mathcal{S}$. For a vector $X=\left(X_{1}, \ldots, X_{n}\right)$ and a subset $A \subseteq[n]$, we use $X_{A}$

to denote the vector $\left(X_{i}\right)_{i \in A}$. We can now give the following definition:
Definition 1. Let $S$ be the set $\left\{(i, a): i \in[n], a \in\{0,1\}^{|\operatorname{Par}(i)|}\right\}$ and $s=|S|$. For $(i, a) \in S$, the parental configuration $\Pi_{i, a}$ is defined to be the event that $X_{\operatorname{Par}(i)}=a$. Once $\mathcal{S}$ is fixed, we may associate with a Bayesian network $P$ the conditional probability table $p \in[0,1]^{S}$ given by $p_{i, a}=\operatorname{Pr}_{X \sim P}\left[X_{i}=1 \mid \Pi_{i, a}\right]$, for $(i, a) \in S$. We note that the distribution $P$ is determined by $p$.

We will frequently index $p$ as a vector. That is, we will use the notation $p_{k}$, for $1 \leq k \leq s$, and the associated events $\Pi_{k}$, where each $k$ stands for an $(i, a) \in S$ lexicographically ordered.

# 2 Our Results and Techniques 

The structure of this section is as follows: In Section 2.1, we provide the statements of our main results in tandem with a brief explanation of their context and the relations between them. We outline the organization o the paper in Section 2.2, before discussion concurrent work in Section 2.3.

### 2.1 Main Results

The focus of this paper is on the properties of identity testing and closeness testing of Bayes nets. We give the first non-trivial efficient testing algorithms and matching information-theoretic lower bounds for these problems. For a wide range of parameter settings, our algorithms achieve sub-learning sample complexity and are sample-optimal (up to constant factors).

For concreteness, we consider Bayes nets over Bernoulli random variables. We note that our upper bounds straightforwardly extend to general alphabets with a polynomial dependence on the alphabet size (see Remark 2). Let $\mathcal{B N}_{n, d}$ denote the family of Bernoulli Bayes nets on $n$ variables such that the corresponding DAG has maximum in-degree at most $d$. For most of our results, we will think of the dimension $n$ as being large and the maximum degree $d$ as being comparably small (say, bounded from above by a constant or at most logarithmic in $n$ ).

For the inference problems of learning and testing Bayes nets, there are two versions of the problem: The first version corresponds to the setting where the structure of the graph is fixed (and known a priori to the algorithm). In the second version, both the graph and the parameters are unknown to the algorithm. We note that both versions of the problem are interesting, based on the application. The unknown structure setting is clearly at least as hard, and typically includes an algorithm for the fixed structure case plus additional algorithmic ingredients.

Before we give the statements of our main testing results, we state a nearly tight bound on the sample complexity of learning $\mathcal{B N}_{n, d}$. This bound will be used as a baseline to compare against our efficient testers:

Fact 1. The sample complexity of learning $\mathcal{B N}_{n, d}$, within total variation distance $\epsilon$, with confidence probability $9 / 10$, is: (i) $\widehat{\Theta}\left(2^{d} \cdot n / \epsilon^{2}\right)$, for all $d \leq n / 2$, in the fixed structure setting, and (ii) $\widehat{\Theta}\left(2^{d} \cdot n / \epsilon^{2}\right)$ in the unknown structure setting.

We give a proof of this fact in Appendix A. Fact 1 characterizes the sample complexity of learning Bayes nets (up to logarithmic factors). We remark that our information-theoretic upper bound for the fixed structure case also yields a simple computationally efficient algorithm. The unknown structure regime is much more challenging computationally. For this setting, we provide a nearly tight information-theoretic upper bound that is non-constructive. (The corresponding

algorithm runs in exponential time.) In fact, we note that no sample-optimal computationally efficient algorithm is known for unknown structure Bayes nets.

Our first main result concerns the fixed structure regime. For technical reasons, we focus on Bayes nets that satisfy a natural balancedness condition. Roughly speaking, our balancedness condition ensures that the conditional probabilities are bounded away from 0 and 1 , and that each parental configuration happens with some minimum probability. Formally, we have:

Definition 2. A Bayes net $P$ over $\{0,1\}^{n}$ with structure $\mathcal{S}$ is called $(c, C)$-balanced if, for all $k$, we have that (i) $p_{k} \in[c, 1-c]$, and (ii) $\operatorname{Pr}_{P}\left[\Pi_{k}\right] \geq C$.

Under a mild condition on the balancedness, we give sample-optimal and computationally efficient algorithms for testing identity and closeness of Bayes nets. Specifically, for the problem of identity testing against an explicit distribution, we require that the explicit distribution be balanced (no assumption is needed for the unknown Bayes net). For the problem of closeness testing, we require that one of the two unknown distributions be balanced. We are now ready to state our first main theorem:

Theorem 1 (Testing Identity and Closeness of Fixed-Structure Bayes Nets). For testing identity and closeness of fixed structure Bayes nets $P, Q$ with $n$ nodes and maximum in-degree $d$, there is an efficient algorithm that uses $O\left(2^{d / 2} \sqrt{n} / \epsilon^{2}\right)$ samples and, assuming that one of $P, Q$ is $(c, C)$-balanced with $c=\tilde{\Omega}(1 / \sqrt{n})$ and $C=\tilde{\Omega}\left(d \epsilon^{2} / \sqrt{n}\right)$, correctly distinguishes between the cases that $P=Q$ versus $\|P-Q\|_{1}>\epsilon$, with probability at least $2 / 3$. Moreover, this sample size is information-theoretically optimal, up to constant factors, for all $d<n / 2$, even for the case of uniformity testing.

The conceptual message of Theorem 1 is that, for the case of fixed structure, testing is informationtheoretically easier than learning. Specifically, our result establishes a quadratic gap between learning and identity testing, reminiscent of the analogous gap in the setting of unstructured discrete distributions. We remark here that the information-theoretic lower bounds of Fact 1 (i) hold even for Bayes nets with constant balancedness.

We now turn our attention to the case of unknown structure. Motivated by Theorem 1, it would be tempting to conjecture that one can obtain testers with sub-learning sample complexity in this setting as well. Our first main result for unknown structure testing is an information-theoretic lower bound, showing that this is not the case. Specifically, even for the most basic case of tree-structured Bays Nets $(d=1)$ with unknown structure, uniformity testing requires $\Omega\left(n / \epsilon^{2}\right)$ samples. It should be noted that our lower bound applies even for Bayes nets with constant balancedness. Formally, we have:

Theorem 2 (Sample Lower Bound for Uniformity Testing of Unknown Tree-Structured Bayes Nets). Any algorithm that, given sample access to a balanced tree-structured Bayes net $P$ over $\{0,1\}^{n}$, distinguishes between the cases $P=U$ and $\|P-U\|_{1}>\epsilon$ (where $U$ denotes the uniform distribution over $\{0,1\}^{n}$ ), with probability $2 / 3$, requires $\Omega\left(n / \epsilon^{2}\right)$ samples from $P$.

At the conceptual level, our above lower bound implies that in the unknown topology case - even for the simplest non-trivial case of degree-1 Bayes nets - identity testing is information-theoretically essentially as hard as learning. That is, in some cases, no tester with sub-learning sample complexity exists. We view this fact as an interesting phenomenon that is absent from the previously studied setting of testing unstructured discrete distributions.

Theorem 2 shows that testing Bayes nets can be as hard as learning. However, it is still possible that testing is easier than learning in most natural situations. For the sake of intuition, let us examine our aforementioned lower bound more carefully. We note that the difficulty of the problem originates from the fact that the explicit distribution is the uniform distribution, which can be thought of as having any of a large number of possible structures. We claim that this impediment can be circumvented if the explicit distribution satisfies some non-degeneracy conditions. Intuitively, we want these conditions to ensure robust identifiability of the structure: that is, that any (unknown) Bayes net sufficiently close to a non-degenerate Bayes net $Q$ must also share the same structure.

For tree structures, there is a very simple non-degeneracy condition. Namely, that for each node, the two conditional probabilities for that node (depending on the value of its parent) are non-trivially far from each other. For Bayes nets of degree more than one, our non-degeneracy condition is somewhat more complicated to state, but the intuition is still simple: By definition, nonequivalent Bayesian network structures satisfy different conditional independence constraints. Our non-degeneracy condition rules out some of these possible new conditional independence constraints, as far from being satisfied by the non-degenerate Bayesian network. Let $\gamma>0$ be a parameter quantifying non-degeneracy. Under our non-degeneracy condition, we can design a structure tester with the following performance guarantee:

Theorem 3 (Structure Testing for Non-Degenerate Bayes Nets). Let $\mathcal{S}$ be a structure of degree at most $d$ and $P$ be a degree at most $d$ Bayes net over $\{0,1\}^{n}$ with structure $\mathcal{S}^{\prime}$ whose underlying undirected graph has no more edges than $\mathcal{S}$. There is an algorithm that uses $O\left(\left(2^{d}+d \log n\right) / \gamma^{2}\right)$ samples from $P$, runs in time $O\left(n^{d+3} / \gamma^{2}\right)$, and distinguishes between the following two cases with probability at least 2/3: (i) $P$ can be expressed as a degree-d Bayes net with structure $\mathcal{S}$ that is $\gamma$-non-degenerate; or (ii) $P$ cannot be expressed as a Bayes net with structure $\mathcal{S}$.

By invoking the structure test of the above theorem, we can reduce the identity testing with unknown structure to the case of known structure, obtaining the following:

Theorem 4 (Testing Identity of Non-Degenerate Unknown Structure Bayes Nets). There exists an algorithm with the following guarantees. Let $Q$ be a degree-d Bayes net $Q$ over $\{0,1\}^{n}$, which is $(c, C)$ balanced and $\gamma$-non-degenerate for $c=\tilde{\Omega}(1 / \sqrt{n})$ and $C=\tilde{\Omega}\left(d \epsilon^{2} / \sqrt{n}\right)$. Given the description of $Q, \epsilon>0$, and sample access to a distribution $P$ promised to be a degree-d Bayes net with no more edges than $Q$, the algorithm takes $O\left(2^{d / 2} \sqrt{n} / \epsilon^{2}+\left(2^{d}+d \log n\right) / \gamma^{2}\right)$ samples from $P$, runs in time $O(n)^{d+3}\left(1 / \gamma^{2}+1 / \epsilon^{2}\right)$, and distinguishes with probability at least $2 / 3$ between (i) $P=Q$ and (ii) $\|P-Q\|_{1}>\epsilon$.

We remark that we can obtain an analogous result for the problem of testing closeness. See Section 9.
We have shown that, without any assumptions, testing is almost as hard as learning for the case of trees. An interesting question is whether this holds for high degrees as well. We show that for the case of high degree sub-learning sample complexity is possible. We give an identity testing algorithm for degree- $d$ Bayes nets with unknown structure, without balancedness or degeneracy assumptions. While the dependence on the number of nodes $n$ of this tester is suboptimal, it does essentially achieve the "right" dependence on the degree $d$, that is $2^{d / 2}$ :

Theorem 5 (Sample Complexity Upper Bound of Identity Testing). Given the description of a degree-d Bayes net $Q$ over $\{0,1\}^{n}, \epsilon>0$, and sample access to a degree-d Bayes net $P$, we can distinguish between the cases that $P=Q$ and $\|P-Q\|_{1}>\epsilon$, with probability at least $2 / 3$, using $2^{d / 2} \operatorname{poly}(n, 1 / \epsilon)$ samples from $P$.

(See Theorem 21 for a more detailed statement handling closeness testing as well.) The message of this result is that when the degree $d$ increases, specifically for $d=\Omega(\log n)$, the sample complexity of testing becomes lower than the sample complexity of learning. We also show an analogue of Theorem 5 for closeness testing of two unknown Bayes nets, under the additional assumption that we know the topological ordering of the unknown DAGs.

# 2.2 Organization 

This paper is organized as follows: In Section 3, we give the necessary definitions and tools we will require. Section 4 contains our matching upper and lower bounds for identity testing of product distributions, and is followed in Section 5 by our matching upper and lower bounds for closeness testing of product distributions. Section 6 then provides an overview of what is required to generalize these techniques from product distributions to Bayes nets, discussing at a high-level the following sections. In Section 7 we study the identity testing for Bayes nets with known structure: We give an identity tester that works under a mild balancedness condition on the explicit Bayes net distribution, and also show that the sample complexity of our algorithm is optimal, up to constant factors. In Section 8, we study the identity testing for unknown structure Bayes nets: We start by proving a sample complexity lower bound showing that, for the unknown structure regime, uniformity testing is information-theoretically as hard as learning - even for the case of trees. We then show that this lower bound can be circumvented under a natural non-degeneracy condition on the explicit Bayes net distribution. Specifically, we give an identity tester with sub-learning sample complexity for all low-degree non-degenerate Bayes nets. Our identity tester for unknown structure non-degenerate Bayes nets relies on a novel structure tester that may be of interest in its own right. Section 9 studies the corresponding closeness testing problems for both known and unknown structure Bayes nets. Finally, in Section 10 we consider the case of high-degree Bayes nets and obtain testers for identity and closeness of unknown-structure Bayes nets. Our testers in this section have optimal (and sub-learning) sample complexity as a function of the maximum in-degree $d$ and polynomial dependence in the dimension $n$.

### 2.3 Concurrent and Independent Work

Contemporaneous work by [DP17] studies the identity testing problem for Bayes nets with the same known graph structure. Using different arguments, they obtain a tester with sample complexity $\tilde{O}\left(2^{(3 / 4) d} \cdot n / \epsilon^{2}\right)$ and running time $O_{\epsilon}\left(n^{d+1}\right)$ for this problem. This sample bound is comparable to that of our Theorem 21 (that works without assumptions on the parameters), having the right dependence on $n, 1 / \epsilon$ (as follows from our Theorem 2 and Fact 1) and a sub-optimal dependence on the degree $d$. As previously mentioned, a sample complexity of $\Omega\left(n / \epsilon^{2}\right)$ is relevant for highdegree Bayes nets. For the case of low-degree (which is the main focus of our paper), one can straightforwardly obtain the same sample bound just by learning the distribution (Fact 1). [DP17] also obtain an $O\left(n^{1 / 2} / \epsilon^{2}\right)$ upper bound for testing identity against a known product, matching our Theorem 6. (This sample bound is optimal by our Theorem 7.)

## 3 Preliminaries

In this section, we provide the basic definitions and technical tools we shall use throughout this paper.

Basic Notation and Definitions The $L_{1}$-distance between two discrete probability distributions $P, Q$ supported on a set $A$ is defined as $\|P-Q\|_{1}=\sum_{x \in A}|P(x)-Q(x)|$. Our arguments will make essential use of related distance measures, specifically the Kullback-Leibler (KL) divergence, defined as $\mathrm{D}(P \| Q)=\sum_{x \in A} P(x) \log \frac{P(x)}{Q(x)}$, and the Hellinger distance, defined as $\mathrm{d}_{\mathrm{H}}(P, Q)=(1 / \sqrt{2}) \cdot \sqrt{\sum_{x \in A}(\sqrt{P(x)}-\sqrt{Q(x)})^{2}}$.

We write $\log$ and $\ln$ for the binary and natural logarithms, respectively, and by $H(X)$ the (Shannon) entropy of a discrete random variable $X$ (as well as, by extension, $H(P)$ for the entropy of a discrete distribution $P$ ). We denote by $I(X ; Y)$ the mutual information between two random variables $X$ and $Y$, defined as $I(X ; Y)=\sum_{x, y} \operatorname{Pr}[(X, Y)=(x, y)] \log \frac{\operatorname{Pr}[(X, Y)=(x, y)]}{\operatorname{Pr}[X=x] \operatorname{Pr}[Y=y]}$. For a probability distribution $P$, we write $X \sim P$ to indicate that $X$ is distributed according to $P$. For probability distributions $P, Q$, we will use $P \otimes Q$ to denote the product distribution with marginals $P$ and $Q$.

Identity and Closeness Testing We now formally define the testing problems that we study.
Definition 3 (Identity testing). An identity testing algorithm of distributions belonging to a class $\mathcal{C}$ is a randomized algorithm which satisfies the following. Given a parameter $0<\epsilon<1$ and the explicit description of a reference distribution $Q \in \mathcal{C}$, as well as access to independent samples from an unknown distribution $P \in \mathcal{C}$, the algorithm outputs either accept or reject such that the following holds:

- (Completeness) if $P=Q$, then the algorithm outputs accept with probability at least $2 / 3$;
- (Soundness) if $\|P-Q\|_{1} \geq \epsilon$, then the algorithm outputs reject with probability at least $2 / 3$.

Note that by the above definition the algorithm is allowed to answer arbitrarily if neither the completeness nor the soundness cases hold. The closeness testing problem is similar, except that now both $P, Q$ are unknown and are only available through independent samples.

Definition 4 (Closeness testing). A closeness testing algorithm of distributions belonging to a class $\mathcal{C}$ is a randomized algorithm which satisfies the following. Given a parameter $0<\epsilon<1$ and access to independent samples from two unknown distributions $P, Q \in \mathcal{C}$, the algorithm outputs either accept or reject such that the following holds:

- (Completeness) if $P=Q$, then the algorithm outputs accept with probability at least $2 / 3$;
- (Soundness) if $\|P-Q\|_{1} \geq \epsilon$, then the algorithm outputs reject with probability at least $2 / 3$.

Finally, we also consider a third related question, that of structure testing:
Definition 5 (Structure testing). Let $\mathcal{C}$ be a family of Bayes nets. A structure testing algorithm of Bayes nets belonging to $\mathcal{C}$ is a randomized algorithm which satisfies the following. Given a parameter $0<\epsilon<1$ and the explicit description of a DAG $\mathcal{S}$, as well as access to independent samples from an unknown $P \in \mathcal{C}$, the algorithm outputs either accept or reject such that the following holds:

- (Completeness) if $P$ can be expressed as a Bayes net with structure $\mathcal{S}$, then the algorithm outputs accept with probability at least $2 / 3$;

- (Soundness) if $\|P-Q\|_{1}>\epsilon$ for every $Q \in \mathcal{C}$ with structure $\mathcal{S}$, then the algorithm outputs reject with probability at least $2 / 3$.

In all cases the two relevant complexity measures are the sample complexity, i.e., the number of samples drawn by the algorithm, and the time complexity of the algorithm. The golden standard is to achieve sample complexity that is information-theoretically optimal and time-complexity linear in the sample complexity.

In this work, the family $\mathcal{C}$ will correspond to the family of Bayes nets over $\{0,1\}^{n}$, where we will impose an upper bound $d$ on the maximum in-degree of each node. For $d=0$, i.e., when the underlying graph has no edges, we obtain the family of product distributions over $\{0,1\}^{n}$.

Relations between Distances We will require a number of inequalities relating the $L_{1}$-distance, the KL-divergence, and the Hellinger distance between distributions. We state a number of inequalities relating these quantities that we will use extensively in our arguments. The simple proofs are deferred to Appendix C.

Recall that a binary product distribution is a distribution over $\{0,1\}^{n}$ whose coordinates are independent; and that such a distribution is determined by its mean vector. We have the following:

Lemma 1. Let $P, Q$ be binary product distributions with mean vectors $p, q \in(0,1)^{n}$. We have that

$$
2 \sum_{i=1}^{n}\left(p_{i}-q_{i}\right)^{2} \leq \mathrm{D}(P \| Q) \leq \sum_{i=1}^{n} \frac{\left(p_{i}-q_{i}\right)^{2}}{q_{i}\left(1-q_{i}\right)}
$$

In particular, if there exists $\alpha>0$ such that $q \in[\alpha, 1-\alpha]^{n}$, we obtain

$$
2\|p-q\|_{2}^{2} \leq \mathrm{D}(P \| Q) \leq \frac{1}{\alpha(1-\alpha)}\|p-q\|_{2}^{2}
$$

Recall that for any pair of distributions $P, Q$, Pinsker's inequality states that $\|P-Q\|_{1}^{2} \leq 2 \mathrm{D}(P \| Q)$. This directly implies the following:

Corollary 1. Let $P, Q$ be binary product distributions with mean vectors $p, q \in(0,1)^{n}$. We have that

$$
\|P-Q\|_{1}^{2} \leq 2 \sum_{i=1}^{n} \frac{\left(p_{i}-q_{i}\right)^{2}}{q_{i}\left(1-q_{i}\right)}
$$

The following lemma states an incomparable and symmetric upper bound on the $L_{1}$-distance, as well as a lower bound.

Lemma 2. Let $P, Q$ be binary product distributions with mean vectors $p, q \in(0,1)^{n}$. Then it holds that

$$
\min \left(c,\|p-q\|_{2}^{4}\right) \leq\|P-Q\|_{1}^{2} \leq 8 \sum_{i=1}^{n} \frac{\left(p_{i}-q_{i}\right)^{2}}{\left(p_{i}+q_{i}\right)\left(2-p_{i}-q_{i}\right)}
$$

for some absolute constant $c>0$. (Moreover, one can take $c=4\left(1-e^{-3 / 2}\right) \simeq 3.11$.)
While the above is specific to product distributions, we will require analogous inequalities for Bayes nets. We start with the following simple lemma:

Lemma 3. Let $P$ and $Q$ be Bayes nets with the same dependency graph. In terms of the conditional probability tables $p$ and $q$ of $P$ and $Q$, we have:

$$
2 \sum_{k=1}^{s} \operatorname{Pr}_{P}\left[\Pi_{k}\right]\left(p_{k}-q_{k}\right)^{2} \leq \mathrm{D}(P \| Q) \leq \sum_{k=1}^{s} \operatorname{Pr}_{P}\left[\Pi_{k}\right] \frac{\left(p_{k}-q_{k}\right)^{2}}{q_{k}\left(1-q_{k}\right)}
$$

Finally, we state an alternative bound, expressed with respect to the Hellinger distance between two Bayes nets:

Lemma 4 ([DKS16b, Lemma 4]). Let $P$ and $Q$ be Bayes nets with the same dependency graph. In terms of the conditional probability tables $p$ and $q$ of $P$ and $Q$, we have:

$$
\mathrm{d}_{\mathrm{H}}(P, Q)^{2} \leq 2 \sum_{k=1}^{s} \sqrt{\operatorname{Pr}_{P}\left[\Pi_{k}\right] \operatorname{Pr}_{Q}\left[\Pi_{k}\right]} \frac{\left(p_{k}-q_{k}\right)^{2}}{\left(p_{k}+q_{k}\right)\left(2-p_{k}-q_{k}\right)}
$$

# 4 Testing Identity of Product Distributions 

Before considering the general case of testing properties of Bayesian nets, we first provide in this section a sample-optimal efficient algorithm and a matching information-theoretic lower bound for the related, but simpler question of testing identity of product distributions over $\{0,1\}^{n}$ (the next section will focus on the harder problem of closeness testing, again for product distributions). Our results for this setting can be viewed as discrete analogues of testing identity and closeness of highdimensional spherical Gaussians, that have been studied in the statistics literature [Hot31, BS96, SD08, CQ10]. We note that the Gaussian setting is simpler since the total variation distance can be bounded by the Euclidean distance between the mean vectors, instead of the chi-squared distance.

The structure of this section is as follows: In Section 4.1, we give an identity testing algorithm for $n$-dimensional binary product distributions with sample complexity $O\left(\sqrt{n} / \epsilon^{2}\right)$. In Section 4.2, we show that this sample bound is information-theoretically optimal.

### 4.1 Identity Testing Algorithm

As mentioned above, here we are concerned with the problem of testing the identity of an unknown product $P$ with mean vector $p$ against an explicit product distribution $Q$ with mean vector $q$. Our tester relies on a statistic providing an unbiased estimator of $\sum_{i}\left(p_{i}-q_{i}\right)^{2} /\left(q_{i}\left(1-q_{i}\right)\right)$. Essentially, every draw from $P$ gives us an independent sample from each of the coordinate random variables. In order to relate our tester more easily to the analogous testers for unstructured distributions over finite domains, we consider $\operatorname{Poi}(m)$ samples from each of these coordinate distributions. From there, we construct a random variable $Z$ that provides an unbiased estimator of our chi-squared statistic, and a careful analysis of the variance of $Z$ shows that with $O\left(\sqrt{n} / \epsilon^{2}\right)$ samples we can distinguish between $P=Q$ and $P$ being $\epsilon$-far from $Q$; leading to the following theorem:

Theorem 6. There exists a computationally efficient algorithm ${ }^{2}$ which, given an explicit product distribution $Q$ (via its mean vector), and sample access to an unknown product distribution $P$ over $\{0,1\}^{n}$, has the following guarantees: For any $\epsilon>0$, the algorithm takes $O\left(\sqrt{n} / \epsilon^{2}\right)$ samples from $P$, and distinguishes with probability $2 / 3$ between the cases that $P=Q$ versus $\|P-Q\|_{1}>\epsilon$.

[^0]
[^0]:    ${ }^{2}$ Throughout this paper, we say an algorithm is computationally efficient if its running time is polynomial in the number of samples and the relevant parameters of the problem (i.e., $n$ and $\epsilon$ ).

Proof. Let $Q=Q_{1} \otimes \cdots \otimes Q_{n}$ be a known product distribution over $\{0,1\}^{n}$ with mean vector $q$, and $P=P_{1} \otimes \cdots \otimes P_{n}$ be an unknown product distribution on $\{0,1\}^{n}$ with unknown mean vector $p$. The goal is to distinguish, given independent samples from $P$, between $P=Q$, and $\|P-Q\|_{1}>\epsilon$.

Let $0<\gamma<1 / 2$. We say that a product distribution $P$ over $\{0,1\}^{n}$ is $\gamma$-balanced if its mean vector $p$ satisfies $p_{i} \in[\gamma, 1-\gamma]$ for all $i \in[n]$. To prove Theorem 6 , we can assume without loss of generality that $P, Q$ are $\gamma_{0}$-balanced for $\gamma_{0} \stackrel{\text { def }}{=} \frac{\epsilon}{16 n}$. Indeed, given sample access to a product distribution $P$, we can simulate access to the $\gamma_{0}$-balanced product distribution $P^{\prime}$ by re-randomizing independently each coordinate with probability $2 \gamma_{0}$, choosing it then to be uniform in $\{0,1\}$. That is, from each draw from $P$ (and the algorithm's own randomness) we can simulate a draw from $P^{\prime}=P_{1}^{\prime} \otimes \cdots \otimes P_{n}^{\prime}$, with

$$
P_{i}^{\prime}(0)=\left(1-2 \gamma_{0}\right) P_{i}(0)+\gamma_{0}, \quad P_{i}^{\prime}(1)=\left(1-2 \gamma_{0}\right) P_{i}(1)+\gamma_{0}
$$

for each $i \in[n]$. The resulting product distribution $P^{\prime}$ is $\gamma_{0}$-balanced, and satisfies $\left\|P-P^{\prime}\right\|_{1} \leq$ $n \cdot 2 \gamma_{0}=\frac{\epsilon}{8}$. Therefore, to test the identity of a product distribution $P$ against a product distribution $Q$ with parameter $\epsilon$, it is sufficient to test the identity of the $\gamma_{0}$-balanced product distributions $P^{\prime}, Q^{\prime}$ (with parameter $\frac{\epsilon}{2}$ ).

Preprocessing We also note that by flipping the coordinates $i$ such that $q_{i}>1 / 2$, we can assume that $q_{i} \in\left[\gamma_{0}, 1 / 2\right]$ for all $i \in[n]$. This can be done without loss of generality, as $q$ is explicitly given. For any $i$ such that $q_{i}>\frac{1}{2}$, we replace $q_{i}$ by $1-q_{i}$ and work with the corresponding distribution $Q^{\prime}$ instead. By flipping the $i$-th bit of all samples we receive from $P$, it only remains to test identity of the resulting distribution $P^{\prime}$ to $Q^{\prime}$, as all distances are preserved.

Proof of Correctness Let $m \geq 2716 \frac{\sqrt{n}}{\epsilon^{2}}$, and let $M_{1}, \ldots, M_{n}$ be i.i.d. $\operatorname{Poi}(m)$ random variables. We set $M=\max _{i \in[n]} M_{i}$ and note that $M \leq 2 m$ with probability $1-e^{-\Omega(m)}$ (by a union bound). We condition hereafter on $M \leq 2 m$ (our tester will reject otherwise) and take $M$ samples $X^{(1)}, \ldots, X^{(M)}$ drawn from $P$. We define the following statistic:

$$
W=\sum_{i=1}^{n} \frac{\left(W_{i}-m q_{i}\right)^{2}-W_{i}}{q_{i}\left(1-q_{i}\right)}
$$

where we write $W_{i} \stackrel{\text { def }}{=} \sum_{j=1}^{M_{i}} X_{i}^{(j)}$ for all $i \in[n]$. We note that the $W_{i}$ 's are independent, as $P$ is a product distribution and the $M_{i}$ 's are independent. The pseudocode for our algorithm is given in Figure 1. Our identity tester is reminiscent of the "chi-squared type" testers that have been designed for the unstructured univariate discrete setting [CDVV14, DKN15b, ADK15].

We start with a simple formula for the expected value of our statistic:
Lemma 5. $\mathbb{E}[W]=m^{2} \sum_{i=1}^{n} \frac{\left(p_{i}-q_{i}\right)^{2}}{q_{i}\left(1-q_{i}\right)}$.
Proof. Since $W_{i} \sim \operatorname{Poi}\left(m p_{i}\right)$ for all $i$, we can write

$$
\mathbb{E}\left[\left(W_{i}-m q_{i}\right)^{2}\right]=\mathbb{E}\left[W_{i}^{2}\right]-2 m q_{i} \mathbb{E}\left[W_{i}\right]+m^{2} q_{i}^{2}=m p_{i}+m^{2}\left(p_{i}-q_{i}\right)^{2}
$$

and therefore

$$
\mathbb{E}[W]=\sum_{i=1}^{n} \frac{\mathbb{E}\left[\left(W_{i}-m q_{i}\right)^{2}\right]-\mathbb{E}\left[W_{i}\right]}{q_{i}\left(1-q_{i}\right)}=m^{2} \sum_{i=1}^{n} \frac{\left(p_{i}-q_{i}\right)^{2}}{q_{i}\left(1-q_{i}\right)}
$$

Input Error tolerance $\epsilon$, dimension $n$, balancedness parameter $\gamma \geq \frac{\epsilon}{16 n}$, mean vector $q=$ $\left(q_{1}, \ldots, q_{n}\right) \in[\gamma, 1 / 2]^{n}$ of an explicit product distribution $Q$ over $\{0,1\}^{n}$, and sampling access to a product distribution $P$ over $\{0,1\}^{n}$.

- Set $\tau \leftarrow \frac{1}{4} \epsilon^{2}, m \leftarrow\left\lceil\frac{2716 \sqrt{n}}{\epsilon^{2}}\right\rceil$.
- Draw $M_{1}, \ldots, M_{n} \sim \operatorname{Poi}(m)$ independently, and let $M \leftarrow \max _{i \in[n]} M_{i}$.

If $M>2 m$ set $W=\tau m^{2}$
Else Take $M$ samples $X^{(1)}, \ldots, X^{(M)}$ from $P$. For $i \in[n]$, let $W_{i} \leftarrow \sum_{j=1}^{M_{i}} X_{i}^{(j)}$, and define

$$
W=\sum_{i=1}^{n} \frac{\left(W_{i}-m q_{i}\right)^{2}-W_{i}}{q_{i}\left(1-q_{i}\right)}
$$

If $W \geq \tau m^{2}$ return reject.
Otherwise return accept.

Figure 1: Identity testing: unknown product distribution $P$ against given product distribution $Q$.

As a corollary we obtain:
Claim 1. If $P=Q$ then $\mathbb{E}[W]=0$. Moreover, whenever $\|P-Q\|_{1}>\epsilon$ we have $\mathbb{E}[W]>\frac{1}{2} m^{2} \epsilon^{2}$.
Proof. The first part is immediate from the expression of $\mathbb{E}[W]$. The second follows from Corollary 1, as $m^{2}\|P-Q\|_{1}^{2} \leq 2 m^{2} \sum_{i=1}^{n} \frac{\left(p_{i}-q_{i}\right)^{2}}{q_{i}\left(1-q_{i}\right)}=2 \mathbb{E}[W]$.

We now proceed to bound from above the variance of our statistic. The completeness case is quite simple:
Claim 2. If $P=Q$, then $\operatorname{Var}[W] \leq 8 m^{2} n$.
Proof. Suppose that $P=Q$, i.e., $p=q$. From independence, we have that $\operatorname{Var}[W]=\sum_{i=1}^{n} \frac{\operatorname{Var}\left[\left(W_{i}-m q_{i}\right)^{2}-W_{i}\right]}{q_{i}^{2}\left(1-q_{i}\right)^{2}}$. Using the fact that $\mathbb{E}\left[\left(W_{i}-m q_{i}\right)^{2}-W_{i}\right]=0$, we get $\operatorname{Var}\left[\left(W_{i}-m q_{i}\right)^{2}-W_{i}\right]=\mathbb{E}\left[\left(\left(W_{i}-m q_{i}\right)^{2}-W_{i}\right)^{2}\right]=$ $2 m^{2} q_{i}^{2}$, where the last equality follows from standard computations involving the moments of a Poisson random variable. From there, recalling that $q_{i} \in(0,1 / 2]$ for all $i \in[n]$, we obtain $\operatorname{Var}[W]=2 m^{2} \sum_{i=1}^{n} \frac{1}{\left(1-q_{i}\right)^{2}} \leq 8 m^{2} n$.

For the soundness case, the following lemma bounds the variance of our statistic from above. We note that the upper bound depends on the balancedness parameter $\gamma$.
Lemma 6. We have that $\operatorname{Var}[W] \leq 16 n m^{2}+\left(\frac{32}{\gamma}+16 \sqrt{2 n} m\right) \mathbb{E}[W]+\frac{32}{\sqrt{\gamma}} \mathbb{E}[W]^{3 / 2}$.

Proof. For general $p, q$, we have that

$$
\begin{aligned}
\operatorname{Var}\left[\left(W_{i}-m q_{i}\right)^{2}-W_{i}\right] & =\mathbb{E}\left[\left(\left(W_{i}-m q_{i}\right)^{2}-W_{i}\right)^{2}\right]-m^{4}\left(p_{i}-q_{i}\right)^{4} \\
& =2 m^{2} p_{i}^{2}+4 m^{3} p_{i}\left(p_{i}-q_{i}\right)^{2}
\end{aligned}
$$

where as before the last equality follows from standard computations involving the moments of a Poisson random variable. This leads to

$$
\begin{aligned}
\operatorname{Var}[W] & =2 m^{2} \sum_{i=1}^{n} \frac{p_{i}^{2}}{q_{i}^{2}\left(1-q_{i}\right)^{2}}+4 m^{3} \sum_{i=1}^{n} \frac{p_{i}\left(p_{i}-q_{i}\right)^{2}}{q_{i}^{2}\left(1-q_{i}\right)^{2}} \\
& \leq 8 m^{2} \sum_{i=1}^{n} \frac{p_{i}^{2}}{q_{i}^{2}}+16 m^{3} \sum_{i=1}^{n} \frac{p_{i}\left(p_{i}-q_{i}\right)^{2}}{q_{i}^{2}}
\end{aligned}
$$

We handle the two terms separately, in a fashion similar to [ADK15, Lemma 2]. For the first term, we can write:

$$
\begin{aligned}
\sum_{i=1}^{n} \frac{p_{i}^{2}}{q_{i}^{2}} & =\sum_{i=1}^{n} \frac{\left(p_{i}-q_{i}\right)^{2}}{q_{i}^{2}}+\sum_{i=1}^{n} \frac{2 p_{i} q_{i}-q_{i}^{2}}{q_{i}^{2}}=\sum_{i=1}^{n} \frac{\left(p_{i}-q_{i}\right)^{2}}{q_{i}^{2}}+\sum_{i=1}^{n} \frac{2 q_{i}\left(p_{i}-q_{i}\right)+q_{i}^{2}}{q_{i}^{2}} \\
& =n+\sum_{i=1}^{n} \frac{\left(p_{i}-q_{i}\right)^{2}}{q_{i}^{2}}+\sum_{i=1}^{n} \frac{2\left(p_{i}-q_{i}\right)}{q_{i}}=n+\sum_{i=1}^{n} \frac{\left(p_{i}-q_{i}\right)^{2}}{q_{i}^{2}}+\sum_{i=1}^{n} \frac{2\left(p_{i}-q_{i}\right)}{q_{i}} \\
& \underset{(\text { AM-GM })}{ } n+\sum_{i=1}^{n} \frac{\left(p_{i}-q_{i}\right)^{2}}{q_{i}^{2}}+\sum_{i=1}^{n}\left(1+\frac{\left(p_{i}-q_{i}\right)^{2}}{q_{i}^{2}}\right)=2 n+2 \sum_{i=1}^{n} \frac{\left(p_{i}-q_{i}\right)^{2}}{q_{i}^{2}} \\
& \leq 2 n+\frac{2}{\gamma} \sum_{i=1}^{n} \frac{\left(p_{i}-q_{i}\right)^{2}}{q_{i}} \leq 2 n+\frac{4}{m^{2} \gamma} \mathbb{E}[W] .
\end{aligned}
$$

We bound the second term from above as follows:

$$
\begin{aligned}
\sum_{i=1}^{n} \frac{p_{i}\left(p_{i}-q_{i}\right)^{2}}{q_{i}^{2}} & \leq \sum_{i=1}^{n} \frac{p_{i}}{q_{i}} \cdot \frac{p_{i}\left(p_{i}-q_{i}\right)^{2}}{q_{i}} \\
& \leq \sqrt{\sum_{i=1}^{n} \frac{p_{i}^{2}}{q_{i}^{2}}} \sqrt{\sum_{i=1}^{n} \frac{\left(p_{i}-q_{i}\right)^{4}}{q_{i}^{2}}} \\
& \leq\left(\sqrt{2 n}+\frac{2}{m \sqrt{\gamma}} \sqrt{\mathbb{E}[W]}\right) \sum_{i=1}^{n} \frac{\left(p_{i}-q_{i}\right)^{2}}{q_{i}} \quad \text { (monotonicity of } \ell_{p} \text {-norms) } \\
& =\frac{1}{m^{2}}\left(\sqrt{2 n}+\frac{2}{m \sqrt{\gamma}} \sqrt{\mathbb{E}[W]}\right) \cdot \mathbb{E}[W]
\end{aligned}
$$

Overall, we obtain

$$
\begin{aligned}
\operatorname{Var}[W] & \leq 16 n m^{2}+\frac{32}{\gamma} \mathbb{E}[W]+16 m\left(\sqrt{2 n}+\frac{2}{m \sqrt{\gamma}} \sqrt{\mathbb{E}[W]}\right) \cdot \mathbb{E}[W] \\
& =16 n m^{2}+\left(\frac{32}{\gamma}+16 \sqrt{2 n} m\right) \mathbb{E}[W]+\frac{32}{\sqrt{\gamma}} \mathbb{E}[W]^{3 / 2}
\end{aligned}
$$

We are now ready to prove correctness.
Lemma 7. Set $\tau \stackrel{\text { def }}{=} \frac{\epsilon^{2}}{4}$. Then we have the following:

- If $\|P-Q\|_{1}=0$, then $\operatorname{Pr}\left[W \geq \tau m^{2}\right] \leq \frac{1}{3}$.
- If $\|P-Q\|_{1}>\epsilon$, then $\operatorname{Pr}\left[W<\tau m^{2}\right] \leq \frac{1}{3}$.

Proof. We start with the soundness case, i.e., assuming $\|P-Q\|_{1}>\epsilon$. In this case, Claim 1 implies $\mathbb{E}[W]>2 \tau m^{2}$. Since $\gamma \geq \frac{\epsilon}{16 n}$ and for $m \geq \frac{16}{\epsilon} \sqrt{2 n}$, Lemma 6 implies that

$$
\operatorname{Var}[W] \leq 16 n m^{2}+32 \sqrt{2 n} m \mathbb{E}[W]+32 \cdot 4 \sqrt{\frac{n}{\epsilon}} \mathbb{E}[W]^{3 / 2}
$$

By Chebyshev's inequality, we have that

$$
\begin{aligned}
\operatorname{Pr}\left[W<\tau m^{2}\right] & \leq \operatorname{Pr}\left[\mathbb{E}[W]-W>\frac{1}{2} \mathbb{E}[W]\right] \leq \frac{4 \operatorname{Var}[W]}{\mathbb{E}[W]^{2}} \\
& \leq \frac{64 n m^{2}}{\mathbb{E}[W]^{2}}+\frac{128 \sqrt{2 n} m}{\mathbb{E}[W]}+\frac{4 \cdot 128 \sqrt{n / \epsilon}}{\mathbb{E}[W]^{1 / 2}} \\
& \leq \frac{4 \cdot 64 n}{m^{2} \epsilon^{4}}+\frac{2 \cdot 128 \sqrt{2 n}}{m \epsilon^{2}}+\frac{4 \sqrt{2} \cdot 128 \sqrt{n}}{m \epsilon^{3 / 2}} \\
& \leq 128\left(\frac{2}{C^{2}}+\frac{5 \sqrt{2}}{C}\right)
\end{aligned}
$$

which is at most $1 / 3$ as long as $C \geq 2716$, that is $m \geq 2716 \frac{\sqrt{n}}{\epsilon^{2}}$.
Turning to the completeness, we suppose $\|P-Q\|_{1}=0$. Then, again by Chebyshev's inequality and Claim 2 we have that

$$
\operatorname{Pr}\left[W \geq \tau m^{2}\right]=\operatorname{Pr}\left[W \geq \mathbb{E}[W]+\tau m^{2}\right] \leq \frac{\operatorname{Var}[W]}{\tau^{2} m^{4}} \leq \frac{128 n}{\epsilon^{4} m^{2}}
$$

which is no more than $1 / 3$ as long as $m \geq 8 \sqrt{6} \frac{\sqrt{n}}{\epsilon^{2}}$.

Remark 1. We observe that the aforementioned analysis - specifically Claim 1 and Lemma 7 - can be adapted to provide some tolerance guarantees in the completeness case, that is it implies a tester that distinguishes between $\|P-Q\|_{1} \leq \epsilon^{\prime}$ and $\|P-Q\|_{1}>\epsilon$, where $\epsilon^{\prime}=O\left(\epsilon^{2}\right)$. This extension, however, requires the assumption that $Q$ be balanced: indeed, the exact dependence between $\epsilon^{\prime}$ and $\epsilon^{2}$ will depend on this balancedness parameter, leading to a tradeoff between tolerance and balancedness. Further, as shown in Section 5.3, this tradeoff is in fact necessary, as tolerant testing of arbitrary product distributions requires $\Omega(n / \log n)$ samples.

# 4.2 Sample Complexity Lower Bound for Identity Testing 

In this section, we prove our matching information-theoretic lower bound for identity testing. In Theorem 7, we give a lower bound for uniformity testing of a product distribution, while Theorem 8 shows a quantitatively similar lower bound for identity testing against the product distribution with mean vector $q=(1 / n, \ldots, 1 / n)$. To establish these lower bounds, we use the informationtheoretic technique from [DK16]: Given a candidate hard instance, we proceed by bounding from above the mutual information between appropriate random variables. More specifically, we construct an appropriate family of hard instances (distributions) and show that a set of $k$ samples taken from a distribution belonging to the chosen family has small shared information with whether or not the distributions are the same.

Theorem 7. There exists an absolute constant $\epsilon_{0}>0$ such that, for any $0<\epsilon \leq \epsilon_{0}$, the following holds: Any algorithm that has sample access to an unknown product distribution $P$ over $\{0,1\}^{n}$ and distinguishes between the cases that $P=U$ and $\|P-U\|_{1}>\epsilon$ with probability $2 / 3$ requires $\Omega\left(\sqrt{n} / \epsilon^{2}\right)$ samples.

Proof. As previously mentioned, we first define two distributions over product distributions $\mathcal{Y}, \mathcal{N}$ :

- $\mathcal{Y}$ is the distribution that puts probability mass 1 on the uniform distribution, $U=\operatorname{Bern}(1 / 2)^{\otimes n}$;
- $\mathcal{N}$ is the uniform distribution over the set

$$
\left\{\bigotimes_{j=1}^{n} \operatorname{Bern}\left(\frac{1}{2}+\frac{(-1)^{b_{j}} \epsilon}{\sqrt{n}}\right): b \in\{0,1\}^{n}\right\}
$$

Lemma 8. $\mathcal{N}$ is supported on distributions that are $\Omega(\epsilon)$-far from $U$.
Proof. The proof, deferred to Appendix B, proceeds by considering directly the quantity $\|P-U\|_{1}$ in order to obtain a lower bound, where $P \stackrel{\text { def }}{=} \bigotimes_{j=1}^{n} \operatorname{Bern}\left(\frac{1}{2}+\frac{\epsilon}{\sqrt{n}}\right)$; specifically, by focusing on the contribution to the distance from the points in the "middle layers" of the Boolean hypercube. (We note that an argument relying on the more convenient properties of the Hellinger distance with regard to product distributions, while much simpler, would only give a lower bound of $\Omega\left(\epsilon^{2}\right)$ - losing a quadratic factor.)

We will make a further simplification, namely that instead of drawing $k$ samples from $P=$ $P_{1} \otimes \cdots \otimes P_{n}$, the algorithm is given $k_{i}$ samples from each $P_{i}$, where $k_{1}, \ldots, k_{n}$ are independent $\operatorname{Poi}(k)$ random variables. This does not affect the lower bound, as this implies a lower bound on algorithms taking $k^{*} \stackrel{\text { def }}{=} \max \left(k_{1}, \ldots, k_{n}\right)$ samples from $P$ (where the $k_{i}$ 's are as above), and $k^{*} \geq \frac{k}{2}$ with probability $1-2^{-\Omega(n)}$. We now consider the following process: letting $X \sim \operatorname{Bern}(1 / 2)$ be a uniformly random bit, we choose a distribution $P$ over $\{0,1\}^{n}$ by

- Drawing $P \sim \mathcal{Y}$ if $X=0$, and;
- Drawing $P \sim \mathcal{N}$ if $X=1$;
- Drawing $k_{1}, \ldots, k_{n} \sim \operatorname{Poi}(k)$, and returning $k_{1}$ samples from $P_{1}, \ldots, k_{n}$ samples from $P_{n}$.

For $i \in[n]$, we write $N_{i}$ for the number of 1 's among the $k_{i}$ samples drawn from $P_{i}$, and let $N=\left(N_{1}, \ldots, N_{n}\right) \in \mathbb{N}^{n}$. We will invoke this standard fact, as stated in [DK16]:
Fact 2. Let $X$ be a uniform random bit and $Y$ a random variable taking value in some set $\mathcal{S}$. If there exists a function $f: \mathcal{S} \rightarrow\{0,1\}$ such that $\operatorname{Pr}[f(Y)=X] \geq 0.51$, then $I(X ; Y)=\Omega(1)$.

Proof. By Fano's inequality, letting $q=\operatorname{Pr}[f(Y) \neq X]$, we have $h(q)=h(q)+q \log (|\{0,1\}|-1) \geq$ $H(X \mid Y)$. This implies $I(X ; Y)=H(X)-H(X \mid Y)=1-H(X \mid Y) \geq 1-h(q) \geq 1-h(0.49) \geq$ $2 \cdot 10^{-4}$.

The next step is then to bound from above $I(X ; N)$, in order to conclude that it will be $o(1)$ unless $k$ is taken big enough and invoke Fact 2. By the foregoing discussion and the relaxation on the $k_{i}$ 's, we have that the conditioned on $X$ the $N_{i}$ are independent (with $N_{i} \sim \operatorname{Poi}\left(k p_{i}\right)$ ). Recall now that if $X, Y_{1}, Y_{2}$ are random variables such that $Y_{1}$ and $Y_{2}$ are independent conditioned on $X$, by the chain rule we have that

$$
H\left(\left(Y_{1}, Y_{2}\right) \mid X\right)=H\left(Y_{1} \mid X\right)+H\left(Y_{2} \mid X, Y_{1}\right)=H\left(Y_{1} \mid X\right)+H\left(Y_{2} \mid X\right)
$$

where the second equality follows from conditional independence, and therefore

$$
\begin{aligned}
I\left(X ;\left(Y_{1}, Y_{2}\right)\right) & =H\left(\left(Y_{1}, Y_{2}\right)\right)-H\left(\left(Y_{1}, Y_{2}\right) \mid X\right) \\
& =H\left(Y_{1}\right)+H\left(Y_{1} \mid Y_{2}\right)-\left(H\left(Y_{1} \mid X\right)+H\left(Y_{2} \mid X\right)\right) \\
& \leq H\left(Y_{1}\right)+H\left(Y_{1}\right)-\left(H\left(Y_{1} \mid X\right)+H\left(Y_{2} \mid X\right)\right) \\
& =\left(H\left(Y_{1}\right)-H\left(Y_{1} \mid X\right)\right)+\left(H\left(Y_{2}\right)-H\left(Y_{2} \mid X\right)\right) \\
& =I\left(X ; Y_{1}\right)+I\left(X ; Y_{2}\right)
\end{aligned}
$$

This implies that

$$
I(X ; N) \leq \sum_{i=1}^{n} I\left(X ; N_{i}\right)
$$

so that it suffices to bound each $I\left(X ; N_{i}\right)$ separately.
Lemma 9. Fix any $i \in[n]$, and let $X, N_{i}$ be as above. Then $I\left(X ; N_{i}\right)=O\left(k^{2} \epsilon^{4} / n^{2}\right)$.
Proof. The proof of this rather technical result can be found in Appendix B, and broadly proceeds as follows. The first step is to upper bound $I\left(X ; N_{i}\right)$ by a more manageable quantity, $\sum_{a=0}^{\infty} \operatorname{Pr}\left[N_{i}=a\right]\left(1-\frac{\operatorname{Pq} N_{i}=a \mid X=1}{\operatorname{Pq} N_{i}=a \mid X=0]}\right)^{2}$. After this, giving an upper bound on each summand can be done by performing a Taylor series expansion (in $\epsilon / \sqrt{n}$ ), relying on the expression of the momentgenerating function of the Poisson distribution to obtain cancellations of many low-order terms.

This lemma, along with Eq. (3), gives the desired result, that is

$$
I(X ; N) \leq \sum_{i=1}^{n} O\left(\frac{\epsilon^{4} k^{2}}{n^{2}}\right)=O\left(\frac{\epsilon^{4} k^{2}}{n}\right)
$$

which is $o(1)$ unless $k=\Omega\left(\sqrt{n} / \epsilon^{2}\right)$.

Theorem 8. There exists an absolute constant $\epsilon_{0}>0$ such that, for any $\epsilon \in\left(0, \epsilon_{0}\right)$, distinguishing $P=P^{*}$ and $\left\|P-P^{*}\right\|_{1}>\epsilon$ with probability $2 / 3$ requires $\Omega\left(\sqrt{n} / \epsilon^{2}\right)$ samples, where $P^{*} \stackrel{\text { def }}{=} \operatorname{Bern}(1 / n)^{\otimes n}$.

Proof. The proof will follow the same outline as that of Theorem 7 first defining two distributions over product distributions $\mathcal{Y}, \mathcal{N}$ :

- $\mathcal{Y}$ is the distribution that puts probability mass 1 on $P^{*}$;
- $\mathcal{N}$ is the uniform distribution over the set

$$
\left\{\bigotimes_{j=1}^{n} \operatorname{Bern}\left(\frac{1+(-1)^{b_{j}} \epsilon}{n}\right): b \in\{0,1\}^{n}\right\}
$$

Lemma 10. With probability $1-2^{-\Omega(n)}, \mathcal{N}$ is supported on distributions $\Omega(\epsilon)$-far from $P^{*}$.
Proof of Lemma 10. As for Lemma 8, using Hellinger distance as a proxy would only result in an $\Omega\left(\epsilon^{2}\right)$ lower bound on the distance, so we will compute it explicitly instead. The proof can be found in Appendix B.

The only ingredient missing to conclude the proof is the analogue of Lemma 9:
Lemma 11. Suppose $\frac{k \epsilon^{2}}{n} \leq 1$. Fix any $i \in[n]$, and let $X, N_{i}$ be as above. Then $I\left(X ; N_{i}\right)=$ $O\left(k^{2} \epsilon^{4} / n^{2}\right)$.

Proof. The proof is similar as that of [DK16, Lemma 3.3], replacing (their) $m n$ by (our) $n$. For completeness, we provide an alternative proof in Appendix D.

# 5 Testing Closeness of Product Distributions 

Our first set of results involves sample-optimal testers and matching information-theoretic lower bounds for testing closeness of product distributions over $\{0,1\}^{n}$ (recall that in Section 4, we settled the related question of identity testing of such product distributions). Specifically, in Section 5.1, we give a closeness testing algorithm for $n$-dimensional binary product distributions with sample complexity $O\left(\sqrt{n} / \epsilon^{2}\right)$; then, we show in Section 5.2 that this sample bound is information-theoretically optimal.

### 5.1 Closeness Testing Algorithm

Compared to identity, testing closeness between two unknown product distributions is somewhat more complicated and requires additional ideas. As is the case when comparing unknown discrete distributions on $[n]$, we have the difficulty that we do not know how to scale our approximations to the $\left(p_{i}-q_{i}\right)^{2}$ terms. We are forced to end up rescaling using the total number of samples drawn with $x_{i}=1$ as a proxy for $1 /\left(q_{i}\right)$. This leaves us with a statistic reminiscent of that used in [CDVV14], which can be shown to work with a related but more subtle analysis. First, in our setting, it is no longer the case that the sum of the $q_{i}$ 's is $O(1)$, and this ends up affecting the analysis, making our

sample complexity depend on $n^{3 / 4}$ instead of $n^{2 / 3}$ as in the unstructured case. Second, to obtain the optimal sample complexity as a function of both $n$ and $\epsilon$, we need to partition the coordinates into two groups based on the value of their marginals and apply a different statistic to each group. It turns out that the sample complexity of our closeness testing algorithm is $O\left(\max \left(n^{1 / 2} / \epsilon^{2}, n^{3 / 4} / \epsilon\right)\right)$ :

Theorem 9. There exists an efficient algorithm which, given sample access to two unknown product distributions $P, Q$ over $\{0,1\}^{n}$, has the following guarantees. For any $\epsilon \in(0,1)$, the algorithm takes $O\left(\max \left(\sqrt{n} / \epsilon^{2}, n^{3 / 4} / \epsilon\right)\right)$ samples from $P$ and $Q$, and distinguishes with probability $2 / 3$ between (i) $\|P-Q\|_{1}=0$ and (ii) $\|P-Q\|_{1}>\epsilon$.

The rest of this section is devoted to the proof of the above theorem.
Proof. Let $P, Q$ be two product distributions on $\{0,1\}^{n}$ with mean vectors $p, q \in[0,1]^{n}$. For $S \subseteq[n]$, we denote by $P_{S}$ and $Q_{S}$ the product distributions on $\{0,1\}^{|S|}$ obtained by restricting $P$ and $Q$ to the coordinates in $S$. Similarly, we write $p_{S}, q_{S} \in[0,1]^{|S|}$ for the vectors obtained by restricting $p, q$ to the coordinates in $S$, so that $P_{S}$ has mean vector $p_{S}$.

High-level Idea The basic idea of the algorithm is to divide the coordinates in two bins $U, V$ : one containing the indices where both distributions have marginals very close to 0 (specifically, at most $1 / m$, where $m$ is our eventual sample complexity), and one containing the remaining indices, on which at least one of the two distributions is roughly balanced. Since $P$ and $Q$ can only be far from each other if at least one of $\left\|P_{U}-Q_{U}\right\|_{1},\left\|P_{V}-Q_{V}\right\|_{1}$ is big, we will test separately each case. Specifically, we will apply two different testers: one " $\chi^{2}$-based tester" (with sample complexity $O\left(\sqrt{n} / \epsilon^{2}\right)$ ) to the "heavy bin" $U-$ which relies on the fact that the marginals of $P, Q$ on $U$ are balanced by construction - and one " $\ell_{2}$-tester" (with sample complexity $O\left(n^{3 / 4} / \epsilon\right)$ ) to the "light bin" $V$ - relying on the fact that $\left\|p_{V}\right\|_{2},\left\|q_{V}\right\|_{2}$ are small. The pseudocode of our algorithm is given in Figure 2.

Sample Complexity Hereafter, we let

$$
m \stackrel{\text { def }}{=} C \max \left(\frac{\sqrt{n}}{\epsilon^{2}}, \frac{n^{3 / 4}}{\epsilon}\right)
$$

for some absolute constant $C>0$ to be determined in the course of the analysis. We let $M_{1}, \ldots, M_{n}$ and $M_{1}^{\prime}, \ldots, M_{n}^{\prime}$ be i.i.d. Poi $(m)$ random variables, set $M=\max _{i \in[n]} M_{i}, M^{\prime}=\max _{i \in[n]} M_{i}^{\prime}$; and note that $M, M^{\prime} \leq 2 m$ with probability $1-e^{-\Omega(m)}$ (by a union bound). We will condition hereafter on the event that $M, M^{\prime} \leq 2 m$ and our tester will reject otherwise.
Without loss of generality, as in the previous sections, we will assume that $\frac{\epsilon}{16 n} \leq p_{i}, q_{i} \leq \frac{3}{4}$ for every $i \in[n]$. Indeed, this can be ensured by the simple preprocessing step below.

Preprocessing Using $O(\log n)$ samples from $P$ and $Q$, we can ensure without loss of generality that all $p_{i}, q_{i}$ are at most $3 / 4$ (with probability $9 / 10$ ). Namely, we estimate every $p_{i}, q_{i}$ to an additive $1 / 64$, and proceed as follows:

- If the estimate of $q_{i}$ is not within an additive $\pm \frac{1}{32}$ of that of $p_{i}$, we output reject and stop;
- If the estimate of $p_{i}$ is more than $43 / 64$, mark $i$ as "swapped" and replace $X_{i}$ by $1-X_{i}$ (for $P)$ and $Y_{i}$ by $1-Y_{i}$ (for $Q$ ) in all future samples.

Assuming correctness of the estimates (which holds with probability at least 9/10), if we pass this step then $\left|p_{i}-q_{i}\right|<\frac{1}{16}$ for all $i$. Moreover, if $i$ was not swapped, then it means that we had $p_{i} \leq 43 / 64+1 / 64<3 / 4$, and therefore $q_{i}<43 / 64+1 / 64+1 / 16=3 / 4$. Now, if we had $q_{i}>3 / 4$, then $p_{i}>3 / 4-1 / 16$ and the estimate of $p_{i}$ would be more than $3 / 4-1 / 16-1 / 64=43 / 64$.

Input Error tolerance $\epsilon \in(0,1)$, dimension $n$, and sampling access to two product distributions $P, Q$ over $\{0,1\}^{n}$.

- Preprocess $P, Q$ so that $q_{i} \leq \frac{3}{4}$ for all $i \in[n]$, return reject if a discrepancy appears.
- Set $m \stackrel{\text { def }}{=} C \max \left(\frac{\sqrt{n}}{\epsilon^{2}}, \frac{n^{3 / 4}}{\epsilon}\right)$.
- Define $M, M^{\prime}$ as follows: Draw $M_{1}, \ldots, M_{n}, M_{1}^{\prime}, \ldots, M_{n}^{\prime}$ i.i.d. $\operatorname{Poi}(m)$ random variables, and set $M=\max _{i \in[n]} M_{i}, M^{\prime}=\max _{i \in[n]} M_{i}^{\prime}$.
- Take $m$ samples from both $P$ and $Q$, and let $U^{\prime}, V^{\prime} \subseteq[n]$ be respectively the set of coordinates $i$ such that $X_{i}=1$ for at least one sample, and its complement.
If $\max \left(M, M^{\prime}\right)>2 m$, return reject.
- Take $M$ (resp. $M^{\prime}$ ) samples $X^{(1)}, \ldots, X^{(M)}$ from $P_{U^{\prime}}$ (resp. $Y^{(1)}, \ldots, Y^{\left(M^{\prime}\right)}$ from $Q_{U^{\prime}}$ ), and define

$$
W_{\text {heavy }}=\sum_{i \in U^{\prime}} \frac{\left(W_{i}-V_{i}\right)^{2}-\left(W_{i}+V_{i}\right)}{W_{i}+V_{i}}
$$

for $V_{i}, W_{i}$ defined as $W_{i}=\sum_{j=1}^{M_{i}} X_{i}^{(j)}$ and $V_{i}=\sum_{j=1}^{M_{i}^{\prime}} Y_{i}^{(j)}$ for all $i \in U^{\prime}$.
If $W_{\text {heavy }} \geq \frac{m \epsilon^{2}}{12000}$ return reject.

- Take $M$ (resp. $M^{\prime}$ ) samples $X^{\prime(1)}, \ldots, X^{\prime(M)}$ from $P_{V^{\prime}}$ (resp. $Y^{\prime(1)}, \ldots, Y^{\prime\left(M^{\prime}\right)}$ from $Q_{V^{\prime}}$ ), and define

$$
W_{\text {light }}=\sum_{i \in V^{\prime}}\left(\left(W_{i}^{\prime}-V_{i}^{\prime}\right)^{2}-\left(W_{i}^{\prime}+V_{i}^{\prime}\right)\right)
$$

for $V_{i}^{\prime}, W_{i}^{\prime}$ defined as $W_{i}^{\prime}=\sum_{j=1}^{M_{i}} X_{i}^{\prime(j)}, V_{i}^{\prime}=\sum_{j=1}^{M_{i}^{\prime}} Y_{i}^{\prime(j)}$ for all $i \in V^{\prime}$.
If $W_{\text {light }} \geq \frac{\epsilon^{2}}{600 n}$ return reject.
return accept.

Figure 2: Closeness testing between two unknown product distributions $P, Q$ over $\{0,1\}^{n}$.

Proof of Correctness For $m$ as above, define $U, V \subseteq[n]$ by $V \stackrel{\text { def }}{=}\left\{i \in[n]: \max \left(p_{i}, q_{i}\right)<\frac{1}{m}\right\}$ and $U \stackrel{\text { def }}{=}[n] \backslash V$. We start with the following simple claim:
Claim 3. Assume $\|P-Q\|_{1}>\epsilon$. Then, at least one of the following must hold: (i) $\left\|p_{V}-q_{V}\right\|_{2}^{2}>$ $\frac{\epsilon^{2}}{16 n}$, or (ii) $\sum_{i \in U} \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}}>\frac{\epsilon^{2}}{64}$.
Proof. Since $\epsilon<\|P-Q\|_{1} \leq\left\|P_{U}-Q_{U}\right\|_{1}+\left\|P_{V}-Q_{V}\right\|_{1}$, at least one of the two terms in the RHS

must exceed $\frac{\epsilon}{2}$. We now recall that, by Lemma 2, it holds that $\left\|P_{U}-Q_{U}\right\|_{1}^{2} \leq 8 \sum_{i \in U} \frac{\left(p_{i}-q_{i}\right)^{2}}{\left(p_{i}+q_{i}\right)\left(2-p_{i}-q_{i}\right)}$ and from the further assumption that $p_{i}, q_{i} \leq \frac{3}{4}$ that $\left\|P_{U}-Q_{U}\right\|_{1}^{2} \leq 16 \sum_{i \in U} \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}}$.
Using subadditivity and the Cauchy-Schwarz inequality, we also have

$$
\begin{aligned}
\left\|P_{V}-Q_{V}\right\|_{1} & \leq \sum_{i \in V}\left\|P_{i}-Q_{i}\right\|_{1}=2 \sum_{i \in V}\left|p_{i}-q_{i}\right| \\
& =2\left\|p_{V}-q_{V}\right\|_{1} \leq 2 \sqrt{|V|}\left\|p_{V}-q_{V}\right\|_{2} \\
& \leq 2 \sqrt{n}\left\|p_{V}-q_{V}\right\|_{2}
\end{aligned}
$$

from where we derive that $\left\|p_{V}-q_{V}\right\|_{2}^{2} \geq \frac{1}{4 n}\left\|P_{V}-Q_{V}\right\|_{1}^{2}$. This completes the proof.
We now define $U^{\prime}, V^{\prime} \subseteq[n]$ (our "proxies" for $U, V$ ) as follows: Taking $m$ samples from both $P$ and $Q$, we let $V^{\prime}$ be the set of indices which were never seen set to one in any sample, and $U^{\prime}$ be its complement. We have the following:
Claim 4. Assume $\|P-Q\|_{1}>\epsilon$. Then, at least one of the following must hold: (i) $\mathbb{E}\left[\left\|p_{V^{\prime}}-q_{V^{\prime}}\right\|_{2}^{2}\right]>$ $\frac{\epsilon^{2}}{150 n}$, or (ii) $\mathbb{E}\left[\sum_{i \in U^{\prime} \cap U} \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}}\right]>\frac{\epsilon^{2}}{128}$.
Proof. By definition, any fixed $i$ belongs to $V^{\prime}$ with probability $\left(1-p_{i}\right)^{m}\left(1-q_{i}\right)^{m}$, and so

$$
\begin{aligned}
\mathbb{E}\left[\left\|p_{V^{\prime}}-q_{V^{\prime}}\right\|_{2}^{2}\right] & =\sum_{i=1}^{n}\left(p_{i}-q_{i}\right)^{2} \cdot\left(1-p_{i}\right)^{m}\left(1-q_{i}\right)^{m} \geq \sum_{i \in V}\left(p_{i}-q_{i}\right)^{2} \cdot\left(1-p_{i}\right)^{m}\left(1-q_{i}\right)^{m} \\
& \geq\left(1-\frac{1}{m}\right)^{2 m} \sum_{i \in V}\left(p_{i}-q_{i}\right)^{2}=\left(1-\frac{1}{m}\right)^{2 m}\left\|p_{V}-q_{V}\right\|_{2}^{2} \\
& \geq \frac{1}{9}\left\|p_{V}-q_{V}\right\|_{2}^{2}
\end{aligned}
$$

for $m \geq 10$. Similarly,

$$
\begin{aligned}
\mathbb{E}\left[\sum_{i \in U^{\prime} \cap U} \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}}\right] & =\sum_{i \in U} \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}} \cdot\left(1-\left(1-p_{i}\right)^{m}\left(1-q_{i}\right)^{m}\right) \\
& \geq\left(1-\left(1-\frac{1}{m}\right)^{2 m}\right) \sum_{i \in U} \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}} \\
& \geq \frac{1}{2} \sum_{i \in U} \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}}
\end{aligned}
$$

and in both cases the proof follows by Claim 3.
We will require the following implication:
Claim 5. Assume $\|P-Q\|_{1}>\epsilon$. Then, at least one of the following must hold with probability at least $4 / 5$ (over the choice of $U^{\prime}, V^{\prime}$ ): (i) $\left\|p_{V^{\prime}}-q_{V^{\prime}}\right\|_{2}^{2}>\frac{\epsilon^{2}}{300 n}$, or (ii) $\sum_{i \in U^{\prime} \cap U} \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}}>\frac{\epsilon^{2}}{2000}$.

Proof. First, assume that $\left\|p_{V}-q_{V}\right\|_{2}^{2}>\frac{\epsilon^{2}}{16 n}$, and let $V^{\prime \prime}$ denote the random variable $V^{\prime} \cap V$. By (the proof of) Claim 4, we have $\mathbb{E}\left[\left\|p_{V^{\prime \prime}}-q_{V^{\prime \prime}}\right\|_{2}^{2}\right] \geq \frac{1}{9}\left\|p_{V}-q_{V}\right\|_{2}^{2}>\frac{\epsilon^{2}}{150 n}$. Writing $m^{2}\left\|p_{V^{\prime \prime}}-q_{V^{\prime \prime}}\right\|_{2}^{2}=$ $\sum_{i=1}^{n} m^{2}\left(p_{i}-q_{i}\right)^{2} \mathbf{1}_{i \in V^{\prime \prime}}$ (note that each summand is in $[0,1]$ ), we then get by a Chernoff bound that

$$
\operatorname{Pr}\left[\left\|p_{V^{\prime \prime}}-q_{V^{\prime \prime}}\right\|_{2}^{2}<\frac{\epsilon^{2}}{300 n}\right]<e^{-\frac{1}{8} \frac{m^{2} \epsilon^{2}}{150 n}}<e^{-\frac{C}{1200 \epsilon^{2}}}
$$

which is less than $1 / 5$ using our setting of $m$ (for an appropriate choice of the constant $C>0$ ).
Suppose now that $\sum_{i \in U} \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}}>\frac{\epsilon^{2}}{64}$. We divide the proof in two cases.

- Case 1: there exists $i^{*} \in U$ such that $\frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}}>\frac{\epsilon^{2}}{2000}$. Then $\operatorname{Pr}\left[\sum_{i \in U^{\prime} \cap U} \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}}>\frac{\epsilon^{2}}{2000}\right] \geq$ $\operatorname{Pr}\left[i^{*} \in U^{\prime}\right] \geq 1-\left(1-\frac{1}{m}\right)^{2 m}>\frac{4}{5}$.
- Case 2: $\frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}} \leq \frac{\epsilon^{2}}{2000}$ for all $i \in U$. Then, writing $X_{i} \stackrel{\text { def }}{=} \frac{2000}{\epsilon^{2}} \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}} \mathbf{1}_{i \in U^{\prime} \cap U} \in[0,1]$ for all $i \in[n]$, we have $\mathbb{E}\left[\sum_{i=1}^{n} X_{i}\right] \geq \frac{2000}{128}$ by Claim 4, and a multiplicative Chernoff bound ensures that

$$
\operatorname{Pr}\left[\sum_{i \in U^{\prime} \cap U} \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}}<\frac{\epsilon^{2}}{2000}\right] \leq \operatorname{Pr}\left[\sum_{i=1}^{n} X_{i}<1\right] \leq e^{-\frac{2000}{8128}}<\frac{1}{5}
$$

concluding the proof.
Finally, we will need to bound the expected $\ell_{2}$-norm of $p_{V^{\prime}}$ and $q_{V^{\prime}}$.
Claim 6. For $U^{\prime}, V^{\prime}$ defined as above, we have $\mathbb{E}\left[\left\|p_{V^{\prime}}\right\|_{2}^{2}\right], \mathbb{E}\left[\left\|q_{V^{\prime}}\right\|_{2}^{2}\right] \leq \frac{n}{m^{2}}$.
Proof. By symmetry, it is sufficient to bound $\mathbb{E}\left[\left\|p_{V^{\prime}}\right\|_{2}^{2}\right]$. We have

$$
\mathbb{E}\left[\left\|p_{V^{\prime}}^{2}\right\|_{2}\right]=\sum_{i=1}^{n} p_{i}^{2} \cdot\left(1-p_{i}\right)^{m}\left(1-q_{i}\right)^{m} \leq \sum_{i=1}^{n} p_{i}^{2} \cdot\left(1-p_{i}\right)^{m}
$$

Studying the auxiliary function $f: x \in[0,1] \mapsto x^{2}(1-x)^{m}$, we see that it achieves a maximum at $\frac{2}{m+2}$. We can then bound

$$
\mathbb{E}\left[\left\|p_{V^{\prime}}^{2}\right\|_{2}\right] \leq n \cdot f\left(\frac{2}{m+2}\right) \underset{m \rightarrow \infty}{\sim} \frac{4 n}{e^{2} m^{2}}
$$

and so $\mathbb{E}\left[\left\|p_{V^{\prime}}^{2}\right\|_{2}\right] \leq \frac{n}{m^{2}}$ for $m$ large enough (and this actually holds for any $m \geq 1$ ).
In what follows, we analyze our statistics $W_{\text {heavy }}$ and $W_{\text {light }}$, conditioning on $U^{\prime}, V^{\prime}$.

Case 1: discrepancy in $U^{\prime}$ We assume that Algorithm 2 reached the line where $W_{\text {heavy }}$ is computed, and show the following:
Lemma 12. If $P=Q$, then with probability at least $9 / 10$ we have $W_{\text {heavy }} \leq \frac{m \epsilon^{2}}{12000}$. Conversely, if $\sum_{i \in U \cap U^{\prime}} \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}}>\frac{\epsilon^{2}}{2000}$, then $W_{\text {heavy }} \geq \frac{m \epsilon^{2}}{12000}$ with probability at least $9 / 10$.
Proof. Recall that the $W_{i}$ 's are independent, as $P$ is a product distribution and the $M_{i}$ 's are independent. Similarly for the $V_{i}$ 's. We have:
Claim 7. If $P=Q$, then $\mathbb{E}\left[W_{\text {heavy }}\right]=0$. Moreover, if $\sum_{i \in U \cap U^{\prime}} \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}}>\frac{\epsilon^{2}}{2000}$, then $\mathbb{E}\left[W_{\text {heavy }}\right]>$ $\frac{m \epsilon^{2}}{6000}$.
Proof. Note that $W_{i} \sim \operatorname{Poi}\left(m p_{i}\right)$ and $V_{i} \sim \operatorname{Poi}\left(m q_{i}\right)$ for all $i \in U^{\prime}$. From there, we can compute (as in [CDVV14])

$$
\mathbb{E}\left[\frac{\left(W_{i}-V_{i}\right)^{2}-\left(W_{i}+V_{i}\right)}{W_{i}+V_{i}}\right]=m \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}}\left(1-\frac{1-e^{-m\left(p_{i}+q_{i}\right)}}{m\left(p_{i}+q_{i}\right)}\right)
$$

by first conditioning on $W_{i}+V_{i}$. This immediately gives the first part of the claim. As for the second, observing that $1-\frac{1-e^{-x}}{x} \geq \frac{1}{3} \min (1, x)$ for $x \geq 0$, and that $p_{i}+q_{i} \geq \frac{1}{m}$ for all $i \in U$, by definition we get

$$
\mathbb{E}\left[W_{\text {heavy }}\right]=m \sum_{i \in U^{\prime}} \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}}\left(1-\frac{1-e^{-m\left(p_{i}+q_{i}\right)}}{m\left(p_{i}+q_{i}\right)}\right) \geq \frac{1}{3} m \sum_{i \in U \cap U^{\prime}} \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}} \geq \frac{m \epsilon^{2}}{6000}
$$

We can now bound the variance of our estimator:
Claim 8. $\operatorname{Var}\left[W_{\text {heavy }}\right] \leq 2 n+5 m \sum_{i \in U^{\prime}} \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}} \leq 7 n+\frac{3}{5} \mathbb{E}\left[W_{\text {heavy }}\right]$. In particular, if $P=Q$ then $\operatorname{Var}\left[W_{\text {heavy }}\right] \leq 2 n$.

Proof. The proof of the first inequality is similar to that in [CDVV14, Lemma 5], with a difference in the final bound due to the fact that the $p_{i}$ 's and $q_{i}$ 's no longer sum to one. For completeness, we give the proof below.

First, note that by independence of the $V_{i}$ 's and $W_{i}$ 's, we have $\operatorname{Var}\left[W_{\text {heavy }}\right]=\sum_{i \in U^{\prime}} \operatorname{Var}\left[\frac{\left(W_{i}-V_{i}\right)^{2}-\left(W_{i}+V_{i}\right)}{W_{i}+V_{i}}\right]$, so it is sufficient to bound each summand individually. In order to do so, we split the variance calculation into two parts: the variance conditioned on $W_{i}+V_{i}=j$, and the component of the variance due to the variation in $j$. Writing for convenience

$$
f\left(W_{i}, V_{i}\right) \stackrel{\text { def }}{=} \frac{\left(W_{i}-V_{i}\right)^{2}-W_{i}-V_{i}}{W_{i}+V_{i}}
$$

we have that

$$
\operatorname{Var}[f(X, Y)] \leq \max _{j}(\operatorname{Var}[f(X, Y) \mid X+Y=j])+\operatorname{Var}[\mathbb{E}[f(X, Y) \mid X+Y=j]]
$$

We now bound the first term. Since $\left(W_{i}-V_{i}\right)^{2}=\left(j-2 V_{i}\right)^{2}$, and $V_{i}$ is distributed as $\operatorname{Bin}(j, \alpha)$ (where for conciseness we let $\alpha \stackrel{\text { def }}{=} \frac{q_{i}}{p_{i}+q_{i}}$ ), we can compute the variance of $\left(j-2 V_{i}\right)^{2}$ from standard

expressions for the moments of the Binomial distribution as $\operatorname{Var}\left[\left(j-2 V_{i}\right)^{2}\right]=16 j(j-1) \alpha(1-$ $\alpha)\left(\left(j-\frac{3}{2}\right)(1-2 \alpha)^{2}+\frac{1}{2}\right)$. Since $\alpha(1-\alpha) \leq \frac{1}{4}$ and $j-\frac{3}{2}<j-1<j$, this in turn is at most $j^{2}\left(2+4 j(1-2 \alpha)^{2}\right)$. Because the denominator is $W_{i}+V_{i}$ which equals $j$, we must divide this by $j^{2}$, make it 0 when $j=0$, and take its expectation as $j$ is distributed as $\operatorname{Poi}\left(m\left(p_{i}+q_{i}\right)\right)$. This leads to

$$
\operatorname{Var}\left[f\left(W_{i}, V_{i}\right) \mid W_{i}+V_{i}=j\right] \leq 2\left(1-e^{-m\left(p_{i}+q_{i}\right)}\right)+4 m \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}}
$$

We now consider the second component of the variance-the contribution to the variance due to the variation in the sum $W_{i}+V_{i}$. Since for fixed $j$, as noted above, we have $V_{i}$ distributed as $\operatorname{Bin}(j, \alpha)$, we have

$$
\begin{aligned}
\mathbb{E}\left[\left(W_{i}-V_{i}\right)^{2}\right] & =\mathbb{E}\left[j^{2}-4 j V_{i}+4 V_{i}^{2}\right] \\
& =j^{2}-4 j^{2} \alpha+4\left(j \alpha-j \alpha^{2}+j^{2} \alpha^{2}\right) \\
& =j^{2}(1-2 \alpha)^{2}+4 j \alpha(1-\alpha)
\end{aligned}
$$

We finally subtract $W_{i}+V_{i}=j$ and divide by $j$ to yield $(j-1)(1-2 \alpha)^{2}$, except with a value of 0 when $j=0$ by definition. However, note that replacing the value at $j=0$ with 0 can only lower the variance. Since the sum $j=W_{i}+V_{i}$ is drawn from a Poisson distribution with parameter $m\left(p_{i}+q_{i}\right)$, we thus have:

$$
\operatorname{Var}\left[\mathbb{E}\left[f\left(W_{i}, V_{i}\right) \mid W_{i}+V_{i}=j\right]\right] \leq m\left(p_{i}+q_{i}\right)(1-2 \alpha)^{4} \leq m\left(p_{i}+q_{i}\right)(1-2 \alpha)^{2}=m \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}}
$$

Summing the final expressions of the previous two paragraphs yields a bound on the variance of $f\left(W_{i} V_{i}\right)$ of

$$
2\left(1-e^{-m\left(p_{i}+q_{i}\right)}\right)+5 m \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}} \leq 2+5 m \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}}
$$

as $1-e^{-x} \leq 1$ for all $x$. This shows that

$$
\begin{aligned}
\operatorname{Var}\left[W_{\text {heavy }}\right] & \leq 2 n+5 m \sum_{i \in U^{\prime}} \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}}=2 n+5 m \sum_{i \in U^{\prime} \cap U} \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}}+5 m \sum_{i \in U^{\prime} \cap V} \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}} \\
& \leq 2 n+\frac{3}{5} \mathbb{E}\left[W_{\text {heavy }}\right]+5 m \sum_{i \in U^{\prime} \cap V} \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}}
\end{aligned}
$$

so it only remains to bound the last term. But by definition, $i \in V$ implies $0 \leq p_{i}, q_{i}<\frac{1}{m}$, from which

$$
5 m \sum_{i \in U^{\prime} \cap V} \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}} \leq 5 \sum_{i \in U^{\prime} \cap V} \frac{\left|p_{i}-q_{i}\right|}{p_{i}+q_{i}} \leq 5\left|U^{\prime} \cap V\right|
$$

which is itself at most $5 n$. This completes the proof.
With these two claims in hand, we are ready to conclude the proof of Lemma 12. We start with the soundness case, i.e. assuming $\sum_{i \in U \cap U^{\prime}} \frac{\left(p_{i}-q_{i}\right)^{2}}{p_{i}+q_{i}}>\frac{r^{2}}{2000}$. Then, by Chebyshev's inequality

and Claim 7 we have that

$$
\begin{aligned}
\operatorname{Pr}\left[W_{\text {heavy }}<\frac{m \epsilon^{2}}{12000}\right] & \leq \operatorname{Pr}\left[\mathbb{E}\left[W_{\text {heavy }}\right]-W_{\text {heavy }}>\frac{1}{2} \mathbb{E}\left[W_{\text {heavy }}\right]\right] \\
& \leq \frac{4 \operatorname{Var}\left[W_{\text {heavy }}\right]}{\mathbb{E}\left[W_{\text {heavy }}\right]^{2}} \\
& \leq \frac{28 n}{\mathbb{E}\left[W_{\text {heavy }}\right]^{2}}+\frac{12}{5 \mathbb{E}\left[W_{\text {heavy }}\right]} \\
& \leq \frac{9 \cdot 2000^{2} \cdot 28 n}{m^{2} \epsilon^{4}}+\frac{36 \cdot 2000}{5 \epsilon^{2} m} \\
& =O\left(\frac{n}{m^{2} \epsilon^{4}}+\frac{1}{\epsilon^{2} m}\right)
\end{aligned}
$$

We want to bound this quantity by $1 / 10$, for which it suffices to have $m>C \frac{\sqrt{n}}{\epsilon^{2}}$ for an appropriate choice of the absolute constant $C>0$ in our setting of $m$.

Turning to the completeness, assume that $\|P-Q\|_{1}=0$. Then, by Chebyshev's inequality, and invoking Claim 8 we have:

$$
\operatorname{Pr}\left[W \geq \frac{m \epsilon^{2}}{12000}\right]=\operatorname{Pr}\left[W \geq \mathbb{E}[W]+\frac{m \epsilon^{2}}{12000}\right] \leq \frac{36 \cdot 2000^{2} \operatorname{Var}[W]}{\epsilon^{4} m^{2}}=O\left(\frac{n}{\epsilon^{4} m^{2}}\right)
$$

which is no more than $1 / 10$ for the same choice of $m$. This establishes Lemma 12.
Case 2: discrepancy in $V^{\prime}$ We now assume that Algorithm 2 reached the line where $W_{\text {light }}$ is computed, and show the following:
Lemma 13. If $P=Q$, then with probability at least $9 / 10$ we have $W_{\text {light }} \leq \frac{\epsilon^{2}}{600 n}$. Conversely, if $\left\|p_{V^{\prime}}-q_{V^{\prime}}\right\|_{2}^{2}>\frac{\epsilon^{2}}{300 n}$, then $W_{\text {light }} \geq \frac{\epsilon^{2}}{600 n}$ with probability at least $9 / 10$.
Proof. We condition on $\left\|p_{V}^{\prime}\right\|_{2}^{2},\left\|q_{V}^{\prime}\right\|_{2}^{2} \leq \frac{20 n}{m^{2}}$, which by Claim 6, a union bound, and Markov's inequality happens with probability at least 19/20. The analysis is similar to [CDVV14, Section 3], observing that the $\left(V_{i}^{\prime}\right)_{i \in V^{\prime}},\left(W_{i}^{\prime}\right)_{i \in V^{\prime}}$ 's are mutually independent Poisson random variables, $V_{i}^{\prime}$ (resp. $W_{i}^{\prime}$ ) having mean $m p_{i}$ (resp. $m q_{i}$ ). Namely, following their analysis, the statistic $W_{\text {light }}$ is an unbiased estimator for $m^{2}\left\|p_{V^{\prime}}-q_{V^{\prime}}\right\|_{2}^{2}$ with variance

$$
\operatorname{Var}\left[W_{\text {light }}\right] \leq 8 m^{3} \sqrt{b}\left\|p_{V^{\prime}}-q_{V^{\prime}}\right\|_{2}^{2}+8 m^{2} b
$$

where $b \stackrel{\text { def }}{=} \frac{20 n}{m^{2}}$ is our upper bound on $\left\|p_{V}^{\prime}\right\|_{2}^{2},\left\|q_{V}^{\prime}\right\|_{2}^{2}$. From there, setting $\epsilon^{\prime} \stackrel{\text { def }}{=} \frac{\epsilon}{\sqrt{n}}$ and applying Chebyshev's inequality, we get that there exists an absolute constant $C^{\prime}>0$ such the completeness and soundness guarantees from the lemma holds with probability at least 19/20, provided that $m>C^{\prime} \frac{\sqrt{b}}{\epsilon^{\prime 2}}$, i.e.,

$$
m>C^{\prime} \frac{n}{\epsilon^{2}} \cdot \frac{\sqrt{20 n}}{m^{2}}=\sqrt{20} C^{\prime} \frac{n^{3 / 2}}{m \epsilon^{2}}
$$

Solving for $m$ shows that choosing $m \geq C \frac{n^{3 / 4}}{\epsilon}$ for some absolute constant $C>0$ is enough. A union bound then allows us to conclude the proof of the lemma, guaranteeing correctness with probability at least $1-\frac{1}{20}-\frac{1}{20}=\frac{9}{10}$ and concluding the proof of Lemma 13.
This establishes Theorem 9.

# 5.2 Sample Complexity Lower Bound for Closeness Testing 

In this section, we prove a matching information-theoretic lower bound for testing closeness of two unknown arbitrary product distributions; showing that, perhaps surprisingly, the sample complexity of Theorem 9 is in fact optimal, up to constant factors:

Theorem 10. There exists an absolute constant $\epsilon_{0}>0$ such that, for any $0<\epsilon \leq \epsilon_{0}$, the following holds: Any algorithm that has sample access to two unknown product distribution $P, Q$ over $\{0,1\}^{n}$ and distinguishes between the cases that $P=Q$ and $\|P-Q\|_{1}>\epsilon$ requires $\Omega\left(\max \left(\sqrt{n} / \epsilon^{2}, n^{3 / 4} / \epsilon\right)\right)$ samples.

Before delving into the proof, we give some intuition for the $n^{3 / 4}$ term of the lower bound lower bound. Recall that the hard family of instances for distinguishing discrete distributions over $[n]$ had (a) many "light" bins (domain elements) of probability mass approximately $1 / n$, where either $p_{i}=q_{i}$ on each bin or $p_{i}=q_{i}(1 \pm \epsilon)$ in each bin, and (b) a number of "heavy" bins where $p_{i}=q_{i} \approx 1 / k$ (where $k$ was the number of samples taken). The goal of the heavy bins, when designing these hard instances, was to "add noise" and hide the signal from the light bins. In the case of discrete distributions over $[n]$, we could only have $k$ such heavy bins. In the case of product distributions, there is no such restriction, and we can have $n / 2$ of them in our hard instance. The added noise leads to an increased sample complexity of testing closeness in the high-dimensional setting.

Proof. The first part of the lower bound, $\Omega\left(\sqrt{n} / \epsilon^{2}\right)$, follows from Theorem 7; we focus here on the second term, $\Omega\left(n^{3 / 4} / \epsilon\right)$, and consequently assume hereafter that $\sqrt{n} / \epsilon^{2}<n^{3 / 4} / \epsilon$. Let $k \geq 1$ be fixed, and suppose we have a tester that takes $k=o\left(n^{3 / 4} / \epsilon\right)$ samples: we will show that it can only be correct with vanishing probability. We will again follow the information-theoretic framework of [DK16] for proving distribution testing lower bounds, first defining two distributions over pairs of product distributions $\mathcal{Y}, \mathcal{N}$ :

- $\mathcal{Y}$ : for every $i \in[n]$, independently choose $\left(p_{i}, q_{i}\right)$ to be either $p_{i}=q_{i}=\frac{1}{k}$ with probability $1 / 2$, and $p_{i}=q_{i}=\frac{1}{n}$ otherwise; and set $P \stackrel{\text { def }}{=} \bigotimes_{j=1}^{n} \operatorname{Bern}\left(p_{i}\right), Q \stackrel{\text { def }}{=} \bigotimes_{j=1}^{n} \operatorname{Bern}\left(q_{i}\right)$.
- $\mathcal{N}$ : for every $i \in[n]$, independently choose $\left(p_{i}, q_{i}\right)$ to be either $p_{i}=q_{i}=\frac{1}{k}$ with probability $1 / 2$, and $\left(\frac{1+\epsilon}{n}, \frac{1-\epsilon}{n}\right)$ or $\left(\frac{1-\epsilon}{n}, \frac{1+\epsilon}{n}\right)$ uniformly at random otherwise; and set $P \stackrel{\text { def }}{=} \bigotimes_{j=1}^{n} \operatorname{Bern}\left(p_{i}\right)$, $Q \stackrel{\text { def }}{=} \bigotimes_{j=1}^{n} \operatorname{Bern}\left(q_{i}\right)$.

Note that in both $\mathcal{Y}$ and $\mathcal{N}$, with overwhelming probability the pairs $(P, Q)$ have roughly $n / 2$ marginals with (equal) parameter $1 / k$, and roughly $n / 2$ marginals with parameter $\Theta(1) / n$.
The following lemma is shown similarly to Lemma 10:
Lemma 14. With probability $1-2^{-\Omega(n)}$, a uniformly chosen pair $(P, Q) \sim \mathcal{N}$ satisfies $\|P-Q\|_{1}=$ $\Omega(\epsilon)$.

We will as before make a further simplification, namely that instead of drawing $k$ samples from $P=P_{1} \otimes \cdots \otimes P_{n}$ and $Q=Q_{1} \otimes \cdots \otimes Q_{n}$, the algorithm is given $k_{i}$ samples from each $P_{i}$ (resp. $k_{i}^{\prime}$ from $Q_{i}$ ), where $k_{1}, \ldots, k_{n}, k_{1}^{\prime}, \ldots, k_{n}^{\prime}$ are independent $\operatorname{Poi}(k)$ random variables. We now consider the following process: letting $X \sim \operatorname{Bern}(1 / 2)$ be a uniformly random bit, we choose a pair of distributions $(P, Q)$ (both $P$ and $Q$ being probability distributions over $\left\{0,1\right\}^{n}$ ) by

- Drawing $(P, Q) \sim \mathcal{Y}$ if $X=0$, and;
- Drawing $(P, Q) \sim \mathcal{N}$ if $X=1$;
- Drawing $k_{1}, k_{1}^{\prime}, \ldots, k_{n}, k_{n}^{\prime} \sim \operatorname{Poi}(k)$, and returning $k_{i}$ samples from each $P_{i}$ and $k_{i}^{\prime}$ samples from each $Q_{i}$

For $i \in[n]$, we let $N_{i}$ and $M_{i}$ denote respectively the number of 1's among the $k_{i}$ samples drawn from $P_{i}$ and $k_{i}^{\prime}$ samples drawn from $Q_{i}$, and write $N=\left(N_{1}, \ldots, N_{n}\right) \in \mathbb{N}^{n}$ (and $M \in \mathbb{N}^{n}$ for $Q$ ). The next step is then to upperbound $I(X ;(N, M))$, in order to conclude that it will be $o(1)$ unless $k$ is taken big enough and invoke Fact 2. By the foregoing discussion and the relaxation on the $k_{i}$ 's, we have that the conditioned on $X$ the $N_{i}$ 's (and $M_{i}$ 's) are independent (with $N_{i} \sim \operatorname{Poi}\left(k p_{i}\right)$ and $\left.M_{i} \sim \operatorname{Poi}\left(k q_{i}\right)\right)$. This implies that

$$
I(X ;(N, M)) \leq \sum_{i=1}^{n} I\left(X ;\left(N_{i}, M_{i}\right)\right)
$$

so that it suffices to bound each $I\left(X ;\left(N_{i}, M_{i}\right)\right)$ separately.
Lemma 15. Fix any $i \in[n]$, and let $X, N_{i}, M_{i}$ be as above. Then $I\left(X ;\left(N_{i}, M_{i}\right)\right)=O\left(k^{4} \epsilon^{4} / n^{4}\right)$.
Proof. By symmetry it is enough to consider only the case of $i=1$, so that we let $(A, B)=\left(N_{1}, M_{1}\right)$.
Since $A \sim \operatorname{Poi}\left(k p_{1}\right)$ and $B \sim \operatorname{Poi}\left(k q_{1}\right)$ with $\left(p_{1}, q_{1}\right)=(1 / k, 1 / k)$ or $\left(p_{1}, q_{1}\right)=(1 / n, 1 / n)$ uniformly if $X=0$, and

$$
\left(p_{1}, q_{1}\right)= \begin{cases}\left(\frac{1}{k}, \frac{1}{k}\right) & \text { w.p. } \frac{1}{2} \\ \left(\frac{1+\epsilon}{n}, \frac{1-\epsilon}{n}\right) & \text { w.p. } \frac{1}{4} \\ \left(\frac{1-\epsilon}{n}, \frac{1+\epsilon}{n}\right) & \text { w.p. } \frac{1}{4}\end{cases}
$$

if $X=1$, a computation similar as that of [DK16, Proposition 3.8] yields that, for any $i, j \in \mathbb{N}$

$$
\begin{aligned}
\operatorname{Pr}[(A, B)=(i, j) \mid X=0] & =\frac{1}{2 i!j!}\left(e^{-2 k / k}\left(\frac{k}{k}\right)^{i+j}+e^{-\frac{2 k}{n}}\left(\frac{k}{n}\right)^{i+j}\right) \\
& =\frac{1}{2 i!j!}\left(e^{-2}+e^{-\frac{2 k}{n}}\left(\frac{k}{n}\right)^{i+j}\right) \\
\operatorname{Pr}[(A, B)=(i, j) \mid X=1] & =\frac{1}{2 i!j!}\left(e^{-2 k / k}\left(\frac{k}{k}\right)^{i+j}+e^{-\frac{2 k}{n}}\left(\frac{k}{n}\right)^{i+j} \frac{(1+\epsilon)^{i}(1-\epsilon)^{j}+(1-\epsilon)^{i}(1+\epsilon)^{j}}{2}\right) \\
& =\frac{1}{2 i!j!}\left(e^{-2}+e^{-\frac{2 k}{n}}\left(\frac{k}{n}\right)^{i+j} \frac{(1+\epsilon)^{i}(1-\epsilon)^{j}+(1-\epsilon)^{i}(1+\epsilon)^{j}}{2}\right)
\end{aligned}
$$

Note in particular that for $0 \leq i+j \leq 1$, this implies that $\operatorname{Pr}[(A, B)=(i, j) \mid X=0]=\operatorname{Pr}[(A, B)=(i, j) \mid X=1]$.

From the above, we obtain

$$
\begin{aligned}
I(X ;(A, B)) & =O(1) \sum_{i, j \geq 0} \frac{(\operatorname{Pr}[(A, B)=(i, j) \mid X=0]-\operatorname{Pr}[(A, B)=(i, j) \mid X=1])^{2}}{\operatorname{Pr}[(A, B)=(i, j) \mid X=0]+\operatorname{Pr}[(A, B)=(i, j) \mid X=1]} \\
& =O(1) \sum_{i+j \geq 2} \frac{(\operatorname{Pr}[(A, B)=(i, j) \mid X=0]-\operatorname{Pr}[(A, B)=(i, j) \mid X=1])^{2}}{\operatorname{Pr}[(A, B)=(i, j) \mid X=0]+\operatorname{Pr}[(A, B)=(i, j) \mid X=1]} \\
& =O(1) \sum_{i+j \geq 2} e^{-\frac{i k}{n}} \frac{\left(\frac{k}{n}\right)^{2(i+j)}\left(1-\frac{\left((1+\epsilon)^{i}(1-\epsilon)^{j}+(1-\epsilon)^{i}(1+\epsilon)^{j}\right)}{2}\right)^{2}}{2 i!j!(2 e^{-2}+o(1))} \\
& =O\left((k \epsilon / n)^{4}\right)
\end{aligned}
$$

where the second-to-last inequality holds for $k=o(n)$. (Which is the case, as $\sqrt{n} / \epsilon^{2}<n^{3 / 4} / \epsilon$ implies that $n^{3 / 4} / \epsilon<n$, and we assumed $k=o\left(n^{3 / 4} / \epsilon\right)$.)

This lemma, along with Eq. (5), immediately implies the result:

$$
I(X ;(N, M)) \leq \sum_{i=1}^{n} O\left(\left(\frac{k \epsilon}{n}\right)^{4}\right)=O\left(\frac{k^{4} \epsilon^{4}}{n^{3}}\right)
$$

which is $o(1)$ unless $k=\Omega\left(n^{3 / 4} / \epsilon\right)$.

# 5.3 Ruling Out Tolerant Testing Without Balancedness 

In this section, we show that any tolerant identity testing algorithm for product distributions must have sample complexity near-linear in $n$ if the explicitly given distribution is very biased.

Theorem 11. There exists an absolute constant $\epsilon_{0}<1$ such that the following holds. Any algorithm that, given a parameter $\epsilon \in\left(0, \epsilon_{0}\right]$ and sample access to product distributions $P, Q$ over $\{0,1\}^{n}$, distinguishes between $\|P-Q\|_{1}<\epsilon / 2$ and $\|P-Q\|_{1}>\epsilon$ with probability at least $2 / 3$ requires $\Omega(n / \log n)$ samples. Moreover, the lower bound still holds in the case where $Q$ is known, and provided as an explicit parameter.

Proof. The basic idea will be to reduce to the case of tolerant testing of two arbitrary distributions $p$ and $q$ over $[n]$. In order to do this, we define the following function from distributions of one type to distributions of the other:

If $p$ is a distribution over $[n]$, define $F_{\delta}(p)$ to be the distribution over $\{0,1\}^{n}$ obtained by taking $\operatorname{Poi}(\delta)$ samples from $p$ and returning the vector $x$ where $x_{i}=1$ if and only if $i$ was one of these samples drawn. Note that, because of the Poissonization, $F_{\delta}(p)$ is a product distribution. We have the following simple claim:
Claim 9. For any $\delta \in(0,1]$ and distributions $p, q$ on $[n], d_{\mathrm{T} V}\left(F_{\delta}(p), F_{\delta}(q)\right)=\left(\delta+O\left(\delta^{2}\right)\right) d_{\mathrm{T} V}(p, q)$.
Proof. In one direction, we can take correlated samples from $F_{\delta}(p)$ and $F_{\delta}(q)$ by sampling $a$ from $\operatorname{Poi}(\delta)$ and then taking $a$ samples from each of $p$ and $q$, using these to generate our samples from $F_{\delta}(p), F_{\delta}(q)$. For fixed $a$, the variation distance between $F_{\delta}(p)$ and $F_{\delta}(q)$ conditioned on that value of $a$ is clearly at most $a d_{\mathrm{T} V}(p, q)$. Therefore, $d_{\mathrm{T} V}\left(F_{\delta}(p), F_{\delta}(q)\right) \leq \mathbb{E}[a] d_{\mathrm{T} V}(p, q)=\delta d_{\mathrm{T} V}(p, q)$.

In the other direction, note that $F_{\delta}(p)$ and $F_{\delta}(q)$ each have probability $\delta+O\left(\delta^{2}\right)$ of returning a vector of weight 1 . This is because $\operatorname{Poi}(\delta)=1$ with probability $\delta e^{-\delta}=\delta+O\left(\delta^{2}\right)$ and since $\operatorname{Poi}(\delta)>1$ with probability $O\left(\delta^{2}\right)$. Let $G(p)$ and $G(q)$ denote the distributions $F_{\delta}(p)$ and $F_{\delta}(q)$ conditioned on returning a vector of weight 1 . By the above, we have that $d_{\mathrm{T} V}\left(F_{\delta}(p), F_{\delta}(q)\right) \geq$ $\left(\delta+O\left(\delta^{2}\right)\right) d_{\mathrm{T} V}(G(p), G(q))$. Letting $p_{i}$ (resp. $q_{i}$ ) be the probability that $p$ (resp. $q$ ) assigns to $i \in[n]$, we get that for any fixed $i \in[n]$ the probability that $F_{\delta}(p)$ returns $e_{i}$ is

$$
\left(1-e^{-\delta p_{i}}\right) \prod_{j \neq i} e^{-\delta p_{j}}=\left(e^{\delta p_{i}}-1\right) \prod_{j=1}^{n} e^{-\delta p_{j}}
$$

Therefore $G(p)$ puts on $e_{i}$ probability proportional to $\left(e^{\delta p_{i}}-1\right)=\left(\delta+O\left(\delta^{2}\right)\right) p_{i}$. Similarly, the probability that $G(q)$ puts on $e_{i}$ is proportional to $\left(\delta+O\left(\delta^{2}\right)\right) q_{i}$ (where in both cases, the constant of proportionality is $\left.\left(\delta+O\left(\delta^{2}\right)\right)^{-1}\right)$. Therefore,

$$
\begin{aligned}
d_{\mathrm{T} V}(G(p), G(q)) & =\delta^{-1}(1+O(\delta)) \sum_{i=1}^{n}\left|\left(\delta+O\left(\delta^{2}\right)\right) p_{i}-\left(\delta+O\left(\delta^{2}\right)\right) q_{i}\right| \\
& =\delta^{-1}(1+O(\delta)) \sum_{i=1}^{n}\left(\delta\left|p_{i}-q_{i}\right|+O\left(\delta^{2}\right)\left(p_{i}+q_{i}\right)\right) \\
& =\delta^{-1}(1+O(\delta))\left(\delta d_{\mathrm{T} V}(p, q)+O\left(\delta^{2}\right)\right) \\
& =d_{\mathrm{T} V}(p, q)+O(\delta)
\end{aligned}
$$

Thus, $d_{\mathrm{T} V}\left(F_{\delta}(p), F_{\delta}(q)\right) \geq\left(\delta+O\left(\delta^{2}\right)\right) d_{\mathrm{T} V}(p, q)$. This completes the proof.
The above claim guarantees the existence of some constant $\delta_{0} \in(0,1]$ such that $d_{\mathrm{T} V}\left(F_{\delta_{0}}(p), F_{\delta_{0}}(q)\right) \in$ $\left[0.9 \delta_{0} d_{\mathrm{T} V}(p, q), 1.1 d_{\mathrm{T} V}(p, q)\right]$. However, it is known [VV11] that for any sufficiently small $\epsilon>0$ there exist distributions $p$ and $q$ over $[n]$ such that one must take at least $c \frac{n}{\log n}$ samples (where $c>0$ is an absolute constant) to distinguish between $d_{\mathrm{T} V}(p, q) \leq \epsilon /\left(2 \cdot 0.9 \delta_{0}\right)$ and $d_{\mathrm{T} V}(p, q) \geq \epsilon /\left(1.1 \delta_{0}\right)$. Given $q$ samples from $p$ and $q$ we can with high probability simulate $c^{\prime} q$ samples from $P=F_{\delta_{0}}(p)$ and $Q=F_{\delta_{0}}(q)$ (where $c^{\prime}=c^{\prime}\left(\delta_{0}\right)>0$ is another absolute constant). Therefore, we cannot distinguish between the cases $d_{\mathrm{T} V}(P, Q) \leq \epsilon / 2$ and $d_{\mathrm{T} V}(P, Q) \geq \epsilon$ in fewer than $c^{\prime} \cdot c \frac{n}{\log n}$, as doing so would enable us to distinguish between $p$ and $q$ with less than $c \frac{n}{\log n}$ samples - yielding a contradiction. Moreover, the above still holds when $q$ is explicitly known, specifically even when $q$ is taken to be the uniform distribution on $[n]$.

# 6 From Product Distributions to Bayes nets: an Overview 

In the following paragraphs, we describe how to generalize our previous results for product distributions to testing general Bayes nets. The case of known structure turns out to be manageable, and at a technical level a generalization of our testers for product distributions. The case of unknown structure poses various complications and requires a number of non-trivial new ideas.

Testing Identity and Closeness of Fixed Structure Bayes Nets Our testers and matching lower bounds for the fixed structure regime are given in Sections 7 and 9.1.

For concreteness, let us consider the case of testing identity of a tree-structured $(d=1)$ Bayes net $P$ against an explicit tree-structured Bayes net $Q$ with the same structure. Recall that we are using

as a proxy for the distance $\|P-Q\|_{1}$ an appropriate chi-squared-like quantity. A major difficulty in generalizing our identity tester for products is that the chi-squared statistic depends not on the probabilities of the various coordinates, but on the conditional probabilities of these coordinates based on all possible parental configurations. This fact produces a major wrinkle in our analysis for the following reason: while in the product distribution case each sample provides information about each coordinate probability, in the Bayes net case a sample only provides information about conditional probabilities for parental configurations that actually occurred in that sample.

This issue can be especially problematic to handle if there are uncommon parental configurations about which we will have difficulty gathering much information (with a small sized sample). Fortunately, the probabilities conditioned on such parental configurations will have a correspondingly smaller effect on the final distribution and thus, we will not need to know them to quite the same accuracy. So while this issue can be essentially avoided, we will require some technical assumptions about balancedness to let us know that none of the parental configurations are too rare. Using these ideas, we develop an identity tester for tree-structured Bayes nets that uses an optimal $\Theta\left(\sqrt{n} / \epsilon^{2}\right)$ samples. For known structure Bayes nets of degree $d>1$, the sample complexity will also depend exponentially on the degree $d$. Specifically, each coordinate will have as many as $2^{d}$ parental configurations. Thus, instead of having only $n$ coordinate probabilities to worry about, we will need to keep track of $2^{d} n$ conditional probabilities. This will require that our sample complexity also scale like $2^{d / 2}$. The final complexity of our identity and closeness testers will thus be $O\left(2^{d / 2} \sqrt{n} / \epsilon^{2}\right)$.

We now briefly comment on our matching lower bounds. Our sample complexity lower bound of $\Omega\left(\sqrt{n} / \epsilon^{2}\right)$ for the product case can be generalized in a black-box manner to yield a tight lower bound $\Omega\left(2^{d / 2} \sqrt{n} / \epsilon^{2}\right)$ for testing uniformity of degree- $d$ Bayes nets. The basic idea is to consider degree- $d$ Bayes nets with the following structure: The first $d$ nodes are all independent (with marginal probability $1 / 2$ each), and will form in some sense a "pointer" to one of $2^{d}$ arbitrary product distributions. The remaining $n-d$ nodes will each depend on all of the first $d$. The resulting distribution is now an (evenly weighted) disjoint mixture of $2^{d}$ product distributions on the $(n-d)$-dimensional hypercube. In other words, there are $2^{d}$ product distributions $p_{1}, \ldots, p_{2^{d}}$, and our distribution returns a random $i$ (encoded in binary) followed by a random sample form $p_{i}$. By using the fact that the $p_{i}$ 's can be arbitrary product distributions, we obtain our desired sample complexity lower bound.

Testing Identity and Closeness of Unknown Structure Bayes Nets As we show in Sections 8 and 9.2, this situation changes substantially when we do not know the underlying structure of the nets involved. In particular, we show that even for Bayes nets of degree-1 uniformity testing requires $\Omega\left(n / \epsilon^{2}\right)$ samples.

The lower bound construction for this case is actually quite simple: The adversarial distribution $P$ will be developed by taking a random matching of the vertices and making each matched pair of vertices randomly $1 \pm \epsilon / \sqrt{n}$ correlated. If the matching were known by the algorithm, the testing procedure could proceed by approximating these $n / 2$ correlations. However, not knowing the structure, our algorithm would be forced to consider all $\binom{n}{2}$ pairwise correlations, substantially increasing the amount of noise involved. To actually prove this lower bound, we consider the distribution $X$ obtained by taking $k$ samples from a randomly chosen $P$ and $Y$ from taking $k$ samples from the uniform distribution. Roughly speaking, we wish to show that $\chi^{2}(X, Y)$ is approximately 1. This amounts to showing that for a randomly chosen pair of distributions $P$

and $P^{\prime}$ from this family, we have that $\mathbb{E}\left[P^{k}(x) P^{\prime k}(x)\right]$ is approximately 1 . Intuitively, we show that this expectation is only large if $P$ and $P^{\prime}$ share many edges in common. In fact, this expectation can be computed exactly in terms of the lengths of the cycles formed by the graph obtained taking the union of the edges from $P$ and $P^{\prime}$. Noting that $P$ and $P^{\prime}$ typically share only about 1 edge, this allows us to prove our desired lower bound.

However, the hardness of the situation described above is not generic and can be avoided if the explicit distribution $Q$ satisfies some non-degeneracy assumptions. Morally, a Bayes nets $Q$ is nondegenerate if it is not close in variational distance to any other Bayes net of no greater complexity and non-equivalent underlying structure. For tree structures, our condition is that for each node the two conditional probabilities for that node (depending on the value of its parent) are far from each other.

If this is the case, even knowing approximately what the pairwise distributions of coordinates are will suffice to determine the structure. One way to see this is the following: the analysis of the Chow-Liu algorithm [CL68] shows that the tree-structure for $P$ is the maximum spanning tree of the graph whose edge weights are given by the shared information of the nodes involved. This tree will have the property that each edge, $e$, has higher weight than any other edge connecting the two halves of the tree. We show that our non-degeneracy assumption implies that this edge has higher weight by a noticeable margin, and thus that it is possible to verify that we have the correct tree with only rough approximations to the pairwise shared information of variables.

For Bayes nets of higher degree, the analysis is somewhat more difficult. We need a slightly more complicated notion of non-degeneracy, essentially boiling down to a sizeable number of notapproximately-conditionally-independent assumptions. For example, a pair of nodes can be positively identified as having an edge between them in the underlying graph if they are not conditionally independent upon any set of $d$ other nodes. By requiring that for each edge the relevant coordinate variables are not close to being conditionally independent, we can verify the identity of the edges of $\mathcal{S}$ with relatively few samples. Unfortunately, this is not quite enough, as with higher degree Bayesian networks, simply knowing the underlying undirected graph is not sufficient to determine its structure. We must also be able to correctly identify the so-called $\vee$-structures. To do this, we will need to impose more not-close-to-conditionally-independent assumptions that allow us to robustly determine these as well.

Assuming that $Q$ satisfies such a non-degeneracy condition, testing identity to it is actually quite easy. First one verifies that the distribution $P$ has all of its pairwise (or $(d+2)$-wise) probabilities close to the corresponding probabilities for $Q$. By non-degeneracy, this will imply that $P$ must have the same (or at least an equivalent) structure as $Q$. Once this has been established, the testing algorithms for the known structure can be employed.

Sample Complexity of Testing High-Degree Bayes Nets One further direction of research is that of understanding the dependence on degree of the sample complexity of testing identity and closeness for degree- $d$ Bayes nets without additional assumptions. For $d=1$, we showed that these problems can be as hard as learning the distribution. For the general case, we give an algorithm with sample complexity $2^{d / 2} \operatorname{poly}(n, 1 / \epsilon)$ for identity testing (and $2^{2 d / 3} \operatorname{poly}(n, 1 / \epsilon)$ for closeness testing). The conceptual message of this result is that, when the degree increases, testing becomes easier than learning information-theoretically. It is a plausible conjecture that the correct answer for identity testing is $\Theta\left(2^{d / 2} n / \epsilon^{2}\right)$ and for closeness testing is $\Theta\left(2^{2 d / 3} n / \epsilon^{2}\right)$. We suspect that our lower bound techniques can be generalized to match these quantities, but the constructions will

likely be substantially more intricate.
The basic idea of our $2^{d / 2} \operatorname{poly}(n, 1 / \epsilon)$ sample upper bound for identity testing is this: We enumerate over all possible structures for $P$, running a different tester for each of them by comparing the relevant conditional probabilities. Unfortunately, in this domain, our simple formula for the KLDivergence between the two distributions will no longer hold. However, we can show that using the old formula will be sufficient by showing that if there are large discrepancies when computing the KL-divergence, then there must be large gap between the entropies $H(P)$ and $H(Q)$ in a particular direction. As the gap cannot exist both ways, this suffices for our purposes.

# 7 Testing Identity of Fixed Structure Bayes Nets 

In this section, we prove our matching upper and lower bounds for testing the identity of Bayes nets with known graph structure. In Section 7.1, we describe an identity testing algorithm that uses $O\left(2^{d / 2} \sqrt{n} / \epsilon^{2}\right)$ samples, where $d$ is the maximum in-degree and $n$ the number of nodes (dimension). In Section 7.2, we show that this sample upper bound is tight, up to constant factors, even for uniformity testing.

### 7.1 Identity Testing Algorithm

In this section, we establish the upper bound part of Theorem 1 for identity, namely testing identity to a fixed Bayes net given sample access to an unknown Bayes net with the same underlying structure. In order to state our results, we recall the definition of balancedness of a Bayes net:

Definition 6. A Bayes net $P$ over $\{0,1\}^{n}$ with structure $\mathcal{S}$ is said to be $(c, C)$-balanced if, for all $k$, it is the case that (i) $p_{k} \in[c, 1-c]$ and (ii) $\operatorname{Pr}_{P}\left[\Pi_{k}\right] \geq C$.

Roughly speaking, the above conditions ensure that the conditional probabilities of the Bayes net are bounded away from 0 and 1 , and that each parental configuration occurs with some minimum probability. With this definition in hand, we are ready to state and prove the main theorem of this section:

Theorem 12. There exists a computationally efficient algorithm with the following guarantees. Given as input (i) a DAG $\mathcal{S}$ with $n$ nodes and maximum in-degree $d$ and a known $(c, C)$-balanced Bayes net $Q$ with structure $\mathcal{S}$, where $c=\tilde{\Omega}(1 / \sqrt{n})$ and $C=\tilde{\Omega}\left(d \epsilon^{2} / \sqrt{n}\right)$; (ii) a parameter $\epsilon>0$, and (iii) sample access to an unknown Bayes net $P$ with structure $\mathcal{S}$, the algorithm takes $O\left(2^{d / 2} \sqrt{n} / \epsilon^{2}\right)$ samples from $P$, and distinguishes with probability at least $2 / 3$ between the cases $P=Q$ and $\|P-Q\|_{1}>\epsilon$.

We choose $m \geq \alpha \frac{2^{d / 2} \sqrt{n}}{\epsilon^{2}}$, where $\alpha>0$ is an absolute constant to be determined in the course of the analysis. Let $\mathcal{S}$ and $Q$ be as in the statement of the theorem, for $c \geq \beta \frac{\log n}{\sqrt{n}} \geq \beta \frac{\log n}{m}$ and $C \geq \beta \frac{d+\log n}{m}$, for an appropriate absolute constant $\beta>0$.

Recall that $S$ denotes the set $\left\{(i, a): i \in[n], a \in\{0,1\}^{|\operatorname{Par}(i)|}\right\}$. By assumption, we have that $|\operatorname{Par}(i)| \leq d$ for all $i \in[n]$. For each $(i, a) \in S$, corresponding to the parental configuration $\Pi_{i, a}=\left\{X_{\operatorname{Par}(i)}=a\right\}$, we define the value $N_{i, a} \stackrel{\text { def }}{=} m \operatorname{Pr}_{Q}\left[\Pi_{i, a}\right] / \sqrt{2}$. Intuitively, $N_{i, a}$ is equal to a small constant factor times the number of samples satisfying $\Pi_{i, a}$ one would expect to see among $m$

independent samples, if the unknown distribution $P$ were equal to $Q$. We will also use the notation $p_{i, a} \stackrel{\text { def }}{=} \operatorname{Pr}\left[X_{i}=1 \mid X_{\operatorname{Par}(i)=a}\right]$, where $X \sim P$, and $q_{i, a} \stackrel{\text { def }}{=} \operatorname{Pr}\left[X_{i}=1 \mid X_{\operatorname{Par}(i)=a}\right]$, where $X \sim Q$.

Given $m$ independent samples $X^{(1)}, \ldots, X^{(m)}$ from a Bayes net $P$ with structure $\mathcal{S}$, we define the estimators $Z_{i, a}, Y_{i, a}$ for every $i \in[n], a \in\{0,1\}^{|\operatorname{Par}(i)|}$ as follows. For every $(i, a)$ such that the number of samples $X^{(j)}$ satisfying the configuration $\Pi_{i, a}$ is between $N_{i, a}$ and $2 N_{i, a}$ (that is, neither too few nor too many), we look only at the first $N_{i, a}$ such samples $X^{\left(j_{1}\right)}, \ldots, X^{\left(j_{N_{i, a}}\right)}$, and let

$$
\begin{aligned}
& Z_{i, a} \stackrel{\text { def }}{=} \sum_{\ell=1}^{N_{i, a}} \mathbf{1}_{\left\{X_{i}^{\left(j_{\ell}\right)}=1\right\}} \\
& Y_{i, a} \stackrel{\text { def }}{=} \sum_{\ell=1}^{N_{i, a}} \mathbf{1}_{\left\{X_{i}^{\left(j_{\ell}\right)}=0\right\}}
\end{aligned}
$$

We note that $Z_{i, a}+Y_{i, a}=N_{i, a}$ by construction. We then define the quantity
$W_{i, a} \stackrel{\text { def }}{=} \frac{\left(\left(1-q_{i, a}\right) Z_{i, a}-q_{i, a} Y_{i, a}\right)^{2}+\left(2 q_{i, a}-1\right) Z_{i, a}-q_{i, a}^{2}\left(Z_{i, a}+Y_{i, a}\right)}{N_{i, a}\left(N_{i, a}-1\right)} \mathbf{1}_{N_{i, a}>1}+\left(p_{i, a}-q_{i, a}\right)^{2} \mathbf{1}_{N_{i, a} \leq 1}$.
On the other hand, for every $(i, a)$ such that the number of samples $X^{(j)}$ satisfying the configuration $\Pi_{i, a}$ is less than $N_{i, a}$ or more than $2 N_{i, a}$, we continue as a thought experiment and keep on getting samples until we see $N_{i, a}$ samples with the right configuration, and act as above (although the actual algorithm will stop and output reject whenever this happens). From there, we finally consider the statistic $W$ :

$$
W \stackrel{\text { def }}{=} \sum_{i=1}^{n} \sum_{a \in\{0,1\}^{|\operatorname{Par}(i)|}} \frac{\operatorname{Pr}_{Q}\left[\Pi_{i, a}\right]}{q_{i, a}\left(1-q_{i, a}\right)} W_{i, a}
$$

Observe that the algorithm will output reject as soon as at least one parental configuration $\Pi_{i, a}$ was not seen enough times, or seen too many times, among the $m$ samples.

The pseudocode of our algorithm is given in the following figure.
Preprocessing We will henceforth assume that $q_{i, a} \leq \frac{1}{2}$ for all $(i, a) \in[n] \times\{0,1\}^{d}$. This can be done without loss of generality, as $Q$ is explicitly known. For any $i$ such that $q_{i, a}>\frac{1}{2}$, we replace $q_{i, a}$ by $1-q_{i, a}$ and work with the corresponding distribution $Q^{\prime}$ instead. By flipping the corresponding bit of all samples we receive from $P$, it only remains to test identity of the resulting distribution $P^{\prime}$ to $Q^{\prime}$, as all distances are preserved.

First Observation If $P=Q$, then we want to argue that with probability at least $9 / 10$ none of the $W_{i, a}$ 's will be such that too few samples satisfied $\Pi_{i, a}$ (as this will immediately cause rejection). To see why this is the case, observe that as long as $m \operatorname{Pr}_{Q}\left[\Pi_{i, a}\right] \geq \beta(d+\log n)$ (for an appropriate choice of absolute constant $\beta>0$ ), the number $m_{i, a}$ of samples satisfying $\Pi_{i, a}$ among the $m$ we draw will, by a Chernoff bound, such that $m_{i, a} \geq m \operatorname{Pr}_{Q}\left[\Pi_{i, a}\right] \geq N_{i, a}$ with probability at least $1-\frac{1}{2^{d} n} \cdot \frac{1}{10}$. A union bound over the at most $2^{d} n$ possible parental configurations will yield the desired conclusion. But the fact that $P=Q$ is $(c, C)$-balanced indeed implies that $\operatorname{Pr}_{Q}\left[\Pi_{i, a}\right] \geq C \geq \beta \frac{d+\log n}{m}$, the last inequality by our choice of $C$.

Therefore, it will be sufficient to continue our analysis, assuming that none of the $W_{i, a}$ 's caused rejection because of an insufficient number of samples satisfying $\Pi_{i, a}$. As we argued above, this

Input Error tolerance $\epsilon \in(0,1)$, dimension $n$, description $\mathcal{S}$ of a DAG with maximum in-degree $d$ and of a $(c, C)$-balanced Bayes net $Q$ with structure $\mathcal{S}$ (where $c \geq \beta \frac{\log n}{m}$ and $C \geq \beta \frac{d+\log n}{m}$ ), and sampling access to a distribution $P$ over $\{0,1\}^{n}$ with structure $\mathcal{S}$.

- Preprocess $Q$ so that $q_{i, a} \leq \frac{1}{2}$ for all $(i, a) \in[n] \times\{0,1\}^{d}$ (and apply the same transformation to all samples taken from $P$ )
- Set $m \leftarrow\left\lceil\alpha \frac{\sqrt{n}}{\epsilon^{2}}\right\rceil$, and take $m$ samples $X^{(1)}, \ldots, X^{(m)}$ from $P$.
- Let $N_{i, a} \leftarrow m \operatorname{Pr}_{Q}\left[\Pi_{i, a}\right] / \sqrt{2}$ for all $(i, a) \in[n] \times\{0,1\}^{d}$.
- Define $Z_{i, a}, Y_{i, a}, W_{i, a}$ as above, and $W \stackrel{\text { def }}{=} \sum_{i=1}^{n} \sum_{a \in\{0,1\}^{|\operatorname{Par}(i)|}} \operatorname{Pr}_{Q}\left[\Pi_{i, a}\right] \frac{W_{i, a}}{q_{i, a}\left(1-q_{i, a}\right)}$.
(At this point, if any configuration $\Pi_{i, a}$ was satisfied by less than $N_{i, a}$ or more than $2 N_{i, a}$ of the $m$ samples, then the algorithm has rejected already.)
If $W \geq \frac{\epsilon^{2}}{32}$ return reject.
Otherwise return accept.

Figure 3: Testing identity against a known-structure balanced Bayes net.
came at the cost of only $1 / 10$ of probability of success in the completeness case, and can only increase the probability of rejection, i.e., success, in the soundness case.

Moreover, in the analysis of the expectation and variance of $W$, we assume that for every $(i, a) \in S$, we have $\operatorname{Pr}_{P}\left[\Pi_{i, a}\right] \leq 4 \operatorname{Pr}_{Q}\left[\Pi_{i, a}\right]$. This is justified by the following two lemmas, which ensure respectively that if it is not the case, then we will have rejected with high probability (this time because too many samples satisfied $\Pi_{i, a}$ ); and that we still have not rejected (with high probability) if $P=Q$.

Lemma 16. Let $P$ be as in the statement of Theorem 12, and suppose there exists a parental configuration $\left(i^{*}, a^{*}\right) \in S$ such that $\operatorname{Pr}_{P}\left[\Pi_{i^{*}, a^{*}}\right]>4 \operatorname{Pr}_{Q}\left[\Pi_{i^{*}, a^{*}}\right]$. Then, with probability at least $9 / 10$, the number of samples $m_{i^{*}, a^{*}}$ satisfying $\Pi_{i^{*}, a^{*}}$ among the $m$ samples taken will be more than $2 N_{i^{*}, a^{*}}$.

Proof. This follows easily from a Chernoff bound, as

$$
\operatorname{Pr}\left[m_{i, a}<2 m \operatorname{Pr}_{Q}\left[\Pi_{i^{*}, a^{*}}\right]\right]<\operatorname{Pr}\left[m_{i, a}<\frac{1}{2} m \operatorname{Pr}_{P}\left[\Pi_{i^{*}, a^{*}}\right]\right]=\operatorname{Pr}\left[m_{i, a}<\frac{1}{2} \mathbb{E}\left[m_{i, a}\right]\right]
$$

and $\mathbb{E}\left[m_{i, a}\right]>\beta(d+\log n)$.
Lemma 17. Suppose $P=Q$. Then, with probability at least $9 / 10$, for every parental configuration $(i, a) \in S$ the number of samples $m_{i, a}$ satisfying $\Pi_{i, a}$ among the $m$ samples taken will be at most $2 N_{i, a}$.

Proof. This again follows from a Chernoff bound and a union bound over all $2^{d} n$ configurations, as we have $\operatorname{Pr}\left[m_{i, a}>2 m \operatorname{Pr}_{Q}\left[\Pi_{i, a}\right]\right]=\operatorname{Pr}\left[m_{i, a}>2 \mathbb{E}\left[m_{i, a}\right]\right]$, and $\mathbb{E}\left[m_{i, a}\right]>\beta(d+\log n)$.

Expectation and Variance Analysis We start with a simple closed form formula for the expectation of our statistic:

Lemma 18. We have that $\mathbb{E}[W]=\sum_{i, a} \operatorname{Pr}_{Q}\left[\Pi_{i, a}\right] \frac{\left(p_{i, a}-q_{i, a}\right)^{2}}{q_{i, a}\left(1-q_{i, a}\right)}$. (In particular, if $P=Q$ then $\mathbb{E}[W]=0$.)

Proof. Fix any $(i, a) \in S$. Since $Z_{i, a}$ follows a $\operatorname{Bin}\left(N_{i, a}, p_{i, a}\right)$ distribution, we get

$$
\begin{aligned}
\mathbb{E}\left[W_{i, a}\right] & =\frac{\mathbb{E}\left[\left(Z_{i, a}-q_{i, a} N_{i, a}\right)^{2}+\left(2 q_{i, a}-1\right) Z_{i, a}-q_{i, a}^{2} N_{i, a}\right]}{N_{i, a}\left(N_{i, a}-1\right)} \mathbf{1}_{N_{i, a}>1}+\mathbb{E}\left[\left(p_{i, a}-q_{i, a}\right)^{2}\right] \mathbf{1}_{N_{i, a} \leq 1} \\
& =\left(p_{i, a}-q_{i, a}\right)^{2} \mathbf{1}_{N_{i, a}>1}+\left(p_{i, a}-q_{i, a}\right)^{2} \mathbf{1}_{N_{i, a} \leq 1} \\
& =\left(p_{i, a}-q_{i, a}\right)^{2}
\end{aligned}
$$

giving the result by linearity of expectation. The last part follows from the fact that $p_{i, a}=q_{i, a}$ for all $(i, a)$ if $P=Q$.

As a simple corollary, we obtain:
Claim 10. If $\|P-Q\|_{1} \geq \epsilon$, then $\mathbb{E}[W] \geq \frac{\epsilon^{2}}{16}$.
Proof. The claim follows from Pinsker's inequality and Lemma 3, along with our assumption that $\operatorname{Pr}_{P}\left[\Pi_{i, a}\right] \leq 4 \cdot \operatorname{Pr}_{Q}\left[\Pi_{i, a}\right]$ for every $(i, a)$ :

$$
\begin{aligned}
\|P-Q\|_{1}^{2} & \leq 2 \mathrm{D}(P \| Q) \leq 2 \sum_{(i, a)} \operatorname{Pr}_{P}\left[\Pi_{i, a}\right] \frac{\left(p_{i, a}-q_{i, a}\right)^{2}}{q_{i, a}\left(1-q_{i, a}\right)} \\
& \leq 8 \sum_{(i, a)} \operatorname{Pr}_{Q}\left[\Pi_{i, a}\right] \frac{\left(p_{i, a}-q_{i, a}\right)^{2}}{q_{i, a}\left(1-q_{i, a}\right)}
\end{aligned}
$$

We now turn to bounding from above the variance of our statistic. This will be done by controlling the covariances and variances of the summands individually, and specifically showing that the former are zero. We have the following:

Claim 11. If $(i, a) \neq(j, b)$, then $\operatorname{Cov}\left(W_{i, a}, W_{i, b}\right)=0$; and the variance satisfies

$$
\operatorname{Var}\left[\frac{\operatorname{Pr}_{Q}\left[\Pi_{i, a}\right]}{q_{i, a}\left(1-q_{i, a}\right)} W_{i, a}\right] \leq \frac{4}{m} \operatorname{Pr}_{Q}\left[\Pi_{i, a}\right] \frac{p_{i, a}\left(1-p_{i, a}\right)}{q_{i, a}^{2}\left(1-q_{i, a}\right)^{2}}\left(p_{i, a}-q_{i, a}\right)^{2}+\frac{4}{m^{2}} \frac{p_{i, a}^{2}}{q_{i, a}^{2}\left(1-q_{i, a}\right)^{2}} \boldsymbol{1}_{N_{i, a}>1}
$$

(Moreover, if $P=Q$ then $\operatorname{Var}\left[\frac{\operatorname{Pr}_{Q}\left[\Pi_{i, a}\right]}{q_{i, a}\left(1-q_{i, a}\right)} W_{i, a}\right] \leq \frac{4}{m^{2}}$.)
Proof. The key point is to observe that, because of the way we defined the $Z_{i, a}$ 's and $Y_{i, a}$ 's (only considering the $N_{i, a}$ first samples satisfying the desired parental configuration), we have that $W_{i, a}$ and $W_{j, b}$ are independent whenever $(i, a) \neq(j, b)$. This directly implies the first part of the claim, i.e.,

$$
\operatorname{Cov}\left(W_{i, a}, W_{i, b}\right)=\mathbb{E}\left[\left(W_{i, a}-\mathbb{E}\left[W_{i, a}\right]\right)\left(W_{j, b}-\mathbb{E}\left[W_{j, b}\right]\right)\right]=0
$$

when $(i, a) \neq(j, b)$.
We then consider $\operatorname{Var}\left[\frac{\operatorname{Pr}_{Q}\left[\Pi_{i, a}\right]}{q_{i, a}\left(1-q_{i, a}\right)} W_{i, a}\right]$. Note that

$$
\mathbb{E}\left[W_{i, a}^{2}\right]=\frac{\mathbb{E}\left[\left(\left(Z_{i, a}-q_{i, a} N_{i, a}\right)^{2}+\left(2 q_{i, a}-1\right) Z_{i, a}-q_{i, a}^{2} N_{i, a}\right)^{2}\right]}{N_{i, a}^{2}\left(N_{i, a}-1\right)^{2}} \mathbf{1}_{N_{i, a}>1}+\left(p_{i, a}-q_{i, a}\right)^{4} \mathbf{1}_{N_{i, a} \leq 1}
$$

so that, writing $p, q, N, Z$ for $p_{i, a}, q_{i, a}, N_{i, a}, Z_{i, a}$ respectively (for readability), as well as $M \stackrel{\text { def }}{=} N-1$ :

$$
\begin{aligned}
\operatorname{Var}\left[\frac{\operatorname{Pr}_{Q}\left[\Pi_{i, a}\right]}{q(1-q)} W_{i, a}\right] & =\left(\frac{\operatorname{Pr}_{Q}\left[\Pi_{i, a}\right]}{q(1-q)}\right)^{2}\left(\mathbb{E}\left[W_{i, a}^{2}\right]-\mathbb{E}\left[W_{i, a}\right]^{2}\right)=\left(\frac{\operatorname{Pr}_{Q}\left[\Pi_{i, a}\right]}{q(1-q)}\right)^{2}\left(\mathbb{E}\left[W_{i, a}^{2}\right]-(p-q)^{4}\right) \\
& =\frac{\mathbb{E}\left[\left((Z-q N)^{2}+(2 q-1) Z-q^{2} N\right)^{2}-N^{2} M^{2}(p-q)^{4}\right]}{N^{2} M^{2} q^{2}(1-q)^{2}} \cdot \operatorname{Pr}_{Q}\left[\Pi_{i, a}\right]^{2} \mathbf{1}_{N>1} \\
& =\frac{\mathbb{E}\left[\left((Z-q N)^{2}+(2 q-1) Z-q^{2} N\right)^{2}-N^{2} M^{2}(p-q)^{4}\right]}{m^{2} M^{2} q^{2}(1-q)^{2}} \mathbf{1}_{N>1} \\
& =\frac{\mathbf{1}_{N>1}}{m^{2}} \frac{2 N p(1-p)}{M q^{2}(1-q)^{2}}\left((2 N-3) p^{2}+2 M q^{2}-4 M p q+p\right)
\end{aligned}
$$

If $p=q$, then this becomes $\operatorname{Var}\left[\frac{\operatorname{Pr}_{Q}\left[\Pi_{i, a}\right]}{q(1-q)} W_{i, a}\right]=\frac{1}{m^{2}} \frac{2 N}{N-1} \mathbf{1}_{N_{i, a}>1} \leq \frac{4}{m^{2}}$, providing the second part of the claim. In the general case, we can bound the variance as follows:

$$
\begin{aligned}
\operatorname{Var}\left[\frac{\operatorname{Pr}_{Q}\left[\Pi_{i, a}\right]}{q(1-q)} W_{i, a}\right] & =\frac{1}{m^{2}} \frac{2 N}{N-1} \frac{p(1-p)}{q^{2}(1-q)^{2}} \mathbf{1}_{N>1} \cdot\left(2(N-1)\left(p^{2}+q^{2}-2 p q\right)-p^{2}+p\right) \\
& =\frac{1}{m^{2}} \frac{2 N}{N-1} \frac{p(1-p)}{q^{2}(1-q)^{2}} \mathbf{1}_{N>1} \cdot\left(2(N-1)(p-q)^{2}+p(1-p)\right) \\
& =\frac{4 N}{m^{2}} \frac{p(1-p)}{q^{2}(1-q)^{2}}(p-q)^{2} \mathbf{1}_{N>1}+\frac{1}{m^{2}} \frac{2 N}{N-1} \frac{p^{2}(1-p)^{2}}{q^{2}(1-q)^{2}} \mathbf{1}_{N>1} \\
& \leq \frac{4 N}{m^{2}} \frac{p(1-p)}{q^{2}(1-q)^{2}}(p-q)^{2}+\frac{4}{m^{2}} \frac{p^{2}(1-p)^{2}}{q^{2}(1-q)^{2}} \mathbf{1}_{N>1} \\
& =\frac{4}{m} \operatorname{Pr}_{Q}\left[\Pi_{i, a}\right] \frac{p_{i, a}\left(1-p_{i, a}\right)}{q_{i, a}^{2}\left(1-q_{i, a}\right)^{2}}\left(p_{i, a}-q_{i, a}\right)^{2}+\frac{4}{m^{2}} \frac{p_{i, a}^{2}\left(1-p_{i, a}\right)^{2}}{q_{i, a}^{2}\left(1-q_{i, a}\right)^{2}} \mathbf{1}_{N_{i, a}>1} \\
& \leq \frac{4}{m} \operatorname{Pr}_{Q}\left[\Pi_{i, a}\right] \frac{p_{i, a}\left(1-p_{i, a}\right)}{q_{i, a}^{2}\left(1-q_{i, a}\right)^{2}}\left(p_{i, a}-q_{i, a}\right)^{2}+\frac{4}{m^{2}} \frac{p_{i, a}^{2}}{q_{i, a}^{2}\left(1-q_{i, a}\right)^{2}} \mathbf{1}_{N_{i, a}>1}
\end{aligned}
$$

This completes the proof.
Using this claim, we now state the upper bound it allows us to obtain:
Lemma 19. We have that $\operatorname{Var}[W] \leq 24 \frac{2^{d} n}{m^{2}}+26 \frac{\mathbb{E} W}{c m}$. (Moreover, if $P=Q$ we have $\operatorname{Var}[W] \leq 4 \frac{2^{d} n}{m^{2}}$.)
Proof. This will follow from Claim 11, which guarantees that if $P=Q, \operatorname{Var}[W] \leq 2^{d} n \cdot \frac{4}{m^{2}}=4 \frac{2^{d} n}{m^{2}}$. Moreover, in the general case,

$$
\operatorname{Var}[W] \leq \frac{4}{m} \sum_{(i, a)} \operatorname{Pr}_{Q}\left[\Pi_{i, a}\right] \frac{p_{i, a}\left(1-p_{i, a}\right)}{q_{i, a}^{2}\left(1-q_{i, a}\right)^{2}}\left(p_{i, a}-q_{i, a}\right)^{2}+\frac{4}{m^{2}} \sum_{(i, a)} \frac{p_{i, a}^{2}}{q_{i, a}^{2}\left(1-q_{i, a}\right)^{2}} \mathbf{1}_{N_{i, a}>1}
$$

We deal with the two terms separately, as follows:

- For the second term, we will show that

$$
\frac{4}{m^{2}} \sum_{(i, a)} \frac{p_{i, a}^{2}}{q_{i, a}^{2}\left(1-q_{i, a}\right)^{2}} \mathbf{1}_{N_{i, a}>1} \leq 24 \frac{2^{d} n}{m^{2}}+\frac{24 \mathbb{E}[W]}{c m}
$$

This follows from the following sequence of (in)equalities: first,

$$
\begin{aligned}
\sum_{(i, a)} \frac{p_{i, a}^{2}}{q_{i, a}^{2}\left(1-q_{i, a}\right)^{2}} \mathbf{1}_{N_{i, a}>1} & =\sum_{(i, a)} \frac{\left(p_{i, a}-q_{i, a}\right)^{2}}{q_{i, a}^{2}\left(1-q_{i, a}\right)^{2}} \mathbf{1}_{N_{i, a}>1}+\sum_{(i, a)} \frac{2 p_{i, a} q_{i, a}-q_{i, a}^{2}}{q_{i, a}^{2}\left(1-q_{i, a}\right)^{2}} \mathbf{1}_{N_{i, a}>1} \\
& =\sum_{(i, a)} \frac{\left(p_{i, a}-q_{i, a}\right)^{2}}{q_{i, a}^{2}\left(1-q_{i, a}\right)^{2}} \mathbf{1}_{N_{i, a}>1}+\sum_{(i, a)} \frac{2 q_{i, a}\left(p_{i, a}-q_{i, a}\right)+q_{i, a}^{2}}{q_{i, a}^{2}\left(1-q_{i, a}\right)^{2}} \mathbf{1}_{N_{i, a}>1} \\
& \leq 4 \cdot 2^{d} n+\sum_{(i, a)} \frac{\left(p_{i, a}-q_{i, a}\right)^{2}}{q_{i, a}^{2}\left(1-q_{i, a}\right)^{2}} \mathbf{1}_{N_{i, a}>1}+\sum_{(i, a)} \frac{2\left(p_{i, a}-q_{i, a}\right)}{q_{i, a}\left(1-q_{i, a}\right)^{2}} \mathbf{1}_{N_{i, a}>1} \mathbf{1}_{N_{i, a}>1} \\
& \leq 4 \cdot 2^{d} n+\sum_{(i, a)} \frac{\left(p_{i, a}-q_{i, a}\right)^{2}}{q_{i, a}^{2}\left(1-q_{i, a}\right)^{2}} \mathbf{1}_{N_{i, a}>1}+4 \sum_{(i, a)} \frac{p_{i, a}-q_{i, a}}{q_{i, a}\left(1-q_{i, a}\right)} \mathbf{1}_{N_{i, a}>1}
\end{aligned}
$$

Then, applying the AM-GM inequality we can continue with

$$
\begin{aligned}
\sum_{(i, a)} \frac{p_{i, a}^{2}}{q_{i, a}^{2}\left(1-q_{i, a}\right)^{2}} \mathbf{1}_{N_{i, a}>1} & \leq 4 \cdot 2^{d} n+\sum_{(i, a)} \frac{\left(p_{i, a}-q_{i, a}\right)^{2}}{q_{i, a}^{2}\left(1-q_{i, a}\right)^{2}} \mathbf{1}_{N_{i, a}>1}+2 \sum_{(i, a)}\left(1+\frac{\left(p_{i, a}-q_{i, a}\right)^{2}}{q_{i, a}^{2}\left(1-q_{i, a}\right)^{2}}\right) \mathbf{1}_{N_{i, a}>1} \\
& \leq 6 \cdot 2^{d} n+3 \sum_{(i, a)} \frac{\left(p_{i, a}-q_{i, a}\right)^{2}}{q_{i, a}^{2}\left(1-q_{i, a}\right)^{2}} \mathbf{1}_{N_{i, a}>1} \\
& \leq 6 \cdot 2^{d} n+\frac{6}{c} \sum_{(i, a)} \frac{\left(p_{i, a}-q_{i, a}\right)^{2}}{q_{i, a}\left(1-q_{i, a}\right)} \mathbf{1}_{N_{i, a}>1} \\
& \leq 6 \cdot 2^{d} n+\frac{6 m}{c} \sum_{(i, a)} \frac{N_{i, a}}{m} \frac{\left(p_{i, a}-q_{i, a}\right)^{2}}{q_{i, a}\left(1-q_{i, a}\right)} \mathbf{1}_{N_{i, a}>1} \\
& =6 \cdot 2^{d} n+\frac{6 m}{c} \sum_{(i, a)} \operatorname{Pr}_{Q}\left[\Pi_{i, a}\right] \frac{\left(p_{i, a}-q_{i, a}\right)^{2}}{q_{i, a}\left(1-q_{i, a}\right)} \mathbf{1}_{N_{i, a}>1} \\
& \leq 6 \cdot 2^{d} n+\frac{6 m}{c} \mathbb{E}[W]
\end{aligned}
$$

using our assumption that $q_{i, a} \leq \frac{1}{2}$ for all $(i, a)$.

- For the first term, we will establish that

$$
\frac{4}{m} \sum_{(i, a)} \operatorname{Pr}_{Q}\left[\Pi_{i, a}\right] \frac{p_{i, a}\left(1-p_{i, a}\right)}{q_{i, a}^{2}\left(1-q_{i, a}\right)^{2}}\left(p_{i, a}-q_{i, a}\right)^{2}
$$

is at most $\frac{2}{c m} \mathbb{E}[W]$. This is shown as follows:

$$
\begin{aligned}
\sum_{(i, a)} \operatorname{Pr}_{Q}\left[\Pi_{i, a}\right] \frac{p_{i, a}\left(1-p_{i, a}\right)\left(p_{i, a}-q_{i, a}\right)^{2}}{q_{i, a}^{2}\left(1-q_{i, a}\right)^{2}} & \leq \frac{1}{4} \sum_{(i, a)} \frac{1}{q_{i, a}\left(1-q_{i, a}\right)} \cdot \operatorname{Pr}_{Q}\left[\Pi_{i, a}\right] \frac{\left(p_{i, a}-q_{i, a}\right)^{2}}{q_{i, a}\left(1-q_{i, a}\right)} \\
& \leq \frac{1}{2 c} \sum_{(i, a)} \operatorname{Pr}_{Q}\left[\Pi_{i, a}\right] \frac{\left(p_{i, a}-q_{i, a}\right)^{2}}{q_{i, a}\left(1-q_{i, a}\right)} \\
& =\frac{1}{2 c} \mathbb{E}[W]
\end{aligned}
$$

Combining the above, we conclude that $\operatorname{Var}[W] \leq 24 \frac{2^{d} n}{m^{2}}+26 \frac{\mathbb{E}[W]}{c m}$.
We now have all the tools we require to establish the completeness and soundness of the tester.
Lemma 20 (Completeness). If $P=Q$, then the algorithm outputs accept with probability at least $2 / 3$.

Proof. We first note that, as per the foregoing discussion and Lemma 17, with probability at least $8 / 10$ we have between $N_{i, a}$ and $2 N_{i, a}$ samples for every parental configuration $(i, a) \in S$, and therefore have not outputted reject. By Chebyshev's inequality and Lemma 19,

$$
\operatorname{Pr}\left[W \geq \frac{\epsilon^{2}}{32}\right] \leq 4096 \frac{2^{d} n}{m^{2} \epsilon^{4}} \leq \frac{4}{30}
$$

for a suitable choice of $\alpha>0$. Therefore, by a union bound the algorithm will output reject with probability at most $\frac{4}{30}+\frac{2}{10}=\frac{1}{3}$.
Lemma 21 (Soundness). If $\|P-Q\|_{1} \geq \epsilon$, then the algorithm outputs reject with probability at least $2 / 3$.

Proof. As noted before, it is sufficient to show that, conditioned on having between $N_{i, a}$ and $2 N_{i, a}$ samples for every parental configuration and $\operatorname{Pr}_{P}\left[\Pi_{i^{*}, a^{*}}\right] \leq 4 \operatorname{Pr}_{Q}\left[\Pi_{i^{*}, a^{*}}\right]$ for all $(i, a)$, the algorithm rejects with probability at least $2 / 3+1 / 10=23 / 30$. Indeed, whenever too few or too many samples from a given parental configuration are seen the algorithm rejects automatically, and by Lemma 16 this happens with probability at least $9 / 10$ if some parental configuration is such that $\operatorname{Pr}_{P}\left[\Pi_{i^{*}, a^{*}}\right]>4 \operatorname{Pr}_{Q}\left[\Pi_{i^{*}, a^{*}}\right]$. Conditioning on this case, by Chebyshev's inequality,

$$
\begin{aligned}
\operatorname{Pr}\left[W \leq \frac{\epsilon^{2}}{32}\right] & \leq \operatorname{Pr}\left[|W-\mathbb{E}[W]| \geq \frac{1}{2} \mathbb{E}[W]\right] \leq \frac{4 \operatorname{Var}[W]}{\mathbb{E}[W]^{2}} \\
& \leq 96 \frac{2^{d} n}{m^{2} \mathbb{E}[W]^{2}}+104 \frac{1}{c m \mathbb{E}[W]}
\end{aligned}
$$

from Lemma 19. Since $\mathbb{E}[W] \geq \frac{\epsilon^{2}}{16}$ by Claim 10, we then get $\operatorname{Pr}\left[W \leq \frac{\epsilon^{2}}{32}\right]=O\left(\frac{2^{d} n}{m^{2} \epsilon^{4}}+\frac{1}{c m \epsilon^{2}}\right) \leq \frac{17}{30}$, again for a suitable choice of $\alpha>0$ and $\beta>0$ (recalling that $c \geq \beta \frac{\log n}{\sqrt{n}}$ ).

Remark 2. We note that we can reduce the problem of testing degree-d Bayes nets over alphabet $\Sigma$, to testing degree- $((d+1)\left\lceil\log _{2}(|\Sigma|)\right\rceil-1)$ Bayes nets over alphabet of size 2. First consider the

case where $|\Sigma|=2^{b}$. Then it suffices to have $n b$ bits in $n$ clusters of size $b$. Each cluster of $b$ will represent a single variable in the initial model with each of the $2^{b}$ possibilities denoting a single letter. Then each bit will need to potentially be dependent on each other bit in its cluster and on each bit in each cluster that its cluster is dependent on. Therefore, we need degree $(d+1) b-1$. Note that this operation preserves balancedness.

Now if $|\Sigma|$ is not a power of 2, we need to pad the alphabet. The obvious way to do this is to create a set of unused letters until the alphabet size is a power of 2. Unfortunately, this creates an unbalanced model. To create a balanced one, we proceed as follows: we split a number of the letters in $\Sigma$ in two. So, instead of having alphabet $a, b, c, \ldots$, we have $a_{1}, a_{2}, b_{1}, b_{2}, c, \ldots$. We make it so that when a word would have an a in a certain position, we map this to a new word that has either $a_{1}$ or $a_{2}$ in that position, each with equal probability. We note that this operation preserves $L_{1}$ distance, and maintains the balancedness properties.

# 7.2 Sample Complexity Lower Bound 

Here we prove a matching information-theoretic lower bound:
Theorem 13. There exists an absolute constant $\epsilon_{0}>0$ such that, for any $0<\epsilon \leq \epsilon_{0}$, the following holds: Any algorithm that has sample access to an unknown Bayes net $P$ over $\{0,1\}^{n}$ with known structure $\mathcal{S}$ of maximum in-degree at most $d<n / 2$, and distinguishes between the cases that $P=U$ and $\|P-U\|_{1}>\epsilon$ requires $\Omega\left(2^{d / 2} n^{1 / 2} / \epsilon^{2}\right)$ samples.

Proof. Our lower bound will be derived from families of Bayes nets with the following structure: The first $d$ nodes are all independent (and will in fact have marginal probability $1 / 2$ each), and will form in some sense a "pointer" to one of $2^{d}$ arbitrary product distributions. The remaining $n-d$ nodes will each depend on all of the first $d$. The resulting distribution is now an (evenly weighted) disjoint mixture of $2^{d}$ product distributions on the $(n-d)$-dimensional hypercube. In other words, there are $2^{d}$ product distributions $p_{1}, \ldots, p_{2^{d}}$, and our distribution returns a random $i$ (encoded in binary) followed by a random sample form $p_{i}$. Note that the $p_{i}$ can be arbitrary product distributions.

The unknown distribution $P$ to test is obtained as follows: let $X$ be a Bernoulli random variable with parameter $1 / 2$. If $X=0, P$ is the uniform distribution on $\{0,1\}^{n}$, i.e., each of the $2^{d}$ distributions $p_{i}$ is uniform on $\{0,1\}^{n-d}$. Otherwise, if $X=1$, then every $p_{i}$ is a product distribution on $\{0,1\}^{n-d}$ with, for each coordinate, a parameter chosen uniformly and independently to be either $\frac{1}{2}+\frac{\epsilon}{\sqrt{n}}$ or $\frac{1}{2}-\frac{\epsilon}{\sqrt{n}}$.

We will show that the shared information between a sample of size $o\left(2^{d / 2} n^{1 / 2} / \epsilon^{2}\right)$ and $X$ is small. In view of this, let $\sigma_{i}$ (for $1 \leq i \leq n-d$ ) be the set of indices of the samples that were drawn from $p_{i}$. Note that since $X$ is uncorrelated with the $\sigma_{i}$ 's, and as the $\sigma_{i}$ are a function of the samples, $I(X ; S)=I\left(X ; S \mid \sigma_{i}\right)$. This is because $I(X ; S))=H(X)-H(X \mid S)=H(X \mid$ $\left.\sigma_{i}\right)-H\left(X \mid S, \sigma_{i}\right)=I\left(X ; S \mid \sigma_{i}\right)$.

Now, for fixed $\sigma_{i}$, the samples we draw from $p_{i}$ are mutually independent of $X$. Let $S_{i}$ denote the tuple of these $\left|\sigma_{i}\right|$ samples. Thus, we have that $I\left(X ; S \mid \sigma_{i}\right) \leq \sum_{i} I\left(X ; S_{i} \mid \sigma_{i}\right)$. By the same analysis as in the proof of Theorem 7, this latter term is $O\left(\binom{\left|\sigma_{i}\right|}{2} \frac{\epsilon^{4}}{n}\right)$. Therefore,

$$
I\left(X ; S \mid \sigma_{i}\right) \leq \mathbb{E}\left[\sum_{i}\binom{\left|\sigma_{i}\right|}{2}\right] O\left(\frac{\epsilon^{4}}{n}\right)=O\left(\frac{m^{2} \epsilon^{4}}{n 2^{d}}\right)
$$

where we used the fact that $\left|\sigma_{i}\right|$ is $\operatorname{Bin}\left(m, 1 / 2^{d}\right)$ distributed. Note that the above RHS is $o(1)$ unless $m=\Omega\left(2^{d / 2} n^{1 / 2} / \epsilon^{2}\right)$, which completes the proof.

# 8 Testing Identity of Unknown Structure Bayes Nets 

In this section, we give our algorithms and lower bounds for testing the identity of low-degree Bayes nets with unknown structure. In Section 8.1, we start by showing that - even for the case of trees - uniformity testing of $n$-node Bayes nets requires $\Omega\left(n / \epsilon^{2}\right)$ samples. In Sections 8.2, we design efficient identity testers with sample complexity sublinear in the dimension $n$, under some non-degeneracy assumptions on the explicit Bayes net.

### 8.1 Sample Complexity Lower Bound

In this section, we establish a tight lower bound on identity testing of Bayes nets in the unknown structure case. Our lower bound holds even for balanced Bayes nets with a tree structure. In order to state our theorem, we first give a specialized definition of balancedness for the case of trees. We say that a Bayes net with tree structure is $c$-balanced if it satisfies $p_{k} \in[c, 1-c]$ for all $k$ (note that this immediately implies it is $(c, C)$-balanced).

Theorem 14. There exist absolute constants $c>0$ and $\epsilon_{0}>0$ such that, for any $\epsilon \in\left(0, \epsilon_{0}\right)$ and given samples from an unknown c-balanced Bayes net $P$ over $\{0,1\}^{n}$ with unknown tree structure, distinguishing between the cases $P=U$ and $\|P-U\|_{1}>\epsilon$ (where $U$ is the uniform distribution over $\{0,1\}^{n}$ ) with probability $2 / 3$ requires $\Omega\left(n / \epsilon^{2}\right)$ samples. (Moreover, one can take $c=1 / 3$.)

Hence, without any assumptions about the explicit distribution, identity testing is informationtheoretically as hard as learning. This section is devoted to the proof of Theorem 14.

Fix any integer $m \geq 1$. We will define a family of no-instances consisting of distributions $\left\{P_{\lambda}\right\}_{\lambda}$ over $\{0,1\}^{n}$ such that:

1. every $P_{\lambda}$ is $\epsilon$-far from the uniform distribution $U$ on $\{0,1\}^{n}:\left\|P_{\lambda}-U\right\|_{1}=\Omega(\epsilon)$;
2. every $P_{\lambda}$ is a Bayes net with a tree structure;
3. unless $m=\Omega\left(\frac{n}{\epsilon^{2}}\right)$, no algorithm taking $m$ samples can distinguish with probability $2 / 3$ between a uniformly chosen distribution from $\left\{P_{\lambda}\right\}_{\lambda}$ and $u$; or, equivalently, no algorithm taking one sample can distinguish with probability $2 / 3$ between $P_{\lambda}^{\otimes m}$ and $U^{\otimes m}$, when $P_{\lambda}$ is chosen uniformly at random from $\left\{P_{\lambda}\right\}_{\lambda}$.

The family is defined as follows. We let $\delta \stackrel{\text { def }}{=} \frac{\epsilon}{\sqrt{n}}$, and let a matching-orientation parameter $\lambda$ consist of (i) a matching $\lambda^{(1)}$ of $[n]$ (partition of $[n]$ in $\frac{n}{2}$ disjoint pairs $(i, j)$ with $i<j$ ) and (ii) a vector $\lambda^{(2)}$ of $\frac{n}{2}$ bits. The distribution $P_{\lambda}$ is then defined as the distribution over $\{0,1\}^{n}$ with uniform marginals, and tree structure with edges corresponding to the pairs $\lambda^{(1)}$; and such that for every $\lambda_{k}^{(1)}=(i, j) \in \lambda^{(1)}, \operatorname{cov}\left(X_{i}, X_{j}\right)=(-1)^{\lambda_{k}^{(2)}} \delta$.

Notation For $\lambda=\left(\lambda^{(1)}, \lambda^{(2)}\right)$ as above and $x \in\{0,1\}^{n}$, we define the agreement count of $x$ for $\lambda$, $c(\lambda, x)$, as the number of pairs $(i, j)$ in $\lambda^{(1)}$ such that $\left(x_{i}, x_{j}\right)$ "agrees" with the correlation suggested by $\lambda^{(2)}$. Specifically:

$$
c(\lambda, x) \stackrel{\text { def }}{=}\left|\left\{(i, j) \in[n]^{2}: \exists \ell \in[n / 2], \lambda_{\ell}^{(1)}=(i, j) \text { and }(-1)^{x_{i}+x_{j}}=(-1)^{\lambda_{\ell}^{(2)}}\right\}\right|
$$

Moreover, for $\lambda, \mu$ two matching-orientation parameters, we define the sets $A=A_{\lambda, \mu}, B=B_{\lambda, \mu}, C=$ $C_{\lambda, \mu}$ as

$$
\begin{aligned}
& A \stackrel{\text { def }}{=}\left\{(s, t) \in[n / 2]^{2}: \lambda_{s}^{(1)}=\mu_{\ell}^{(1)}, \quad \lambda_{s}^{(2)}=\mu_{\ell}^{(2)}\right\} \quad \text { (common pairs with same orientations) } \\
& B \stackrel{\text { def }}{=}\left\{(s, t) \in[n / 2]^{2}: \lambda_{s}^{(1)}=\mu_{\ell}^{(1)}, \quad \lambda_{s}^{(2)} \neq \mu_{\ell}^{(2)}\right\} \quad \text { (common pairs with different orientations) } \\
& C \stackrel{\text { def }}{=}\left(\lambda^{(1)} \cup \mu^{(1)}\right) \backslash(A \cup B) \\
& \text { (pairs unique to } \lambda \text { or } \mu \text { ) } \\
& \text { so that } 2(|A|+|B|)+|C|=n .
\end{aligned}
$$

Proof of Item 1 Fix any matching-orientation parameter $\lambda$. We have

$$
\begin{aligned}
& \left\|P_{\lambda}-U\right\|_{1}=\sum_{x \in\{0,1\}^{n}}\left|P_{\lambda}(x)-U(x)\right| \\
& =\sum_{x \in\{0,1\}^{n}}\left|U(x)(1+2 \delta)^{c(\lambda, x)}(1-2 \delta)^{\frac{n}{2}-c(\lambda, x)}-U(x)\right| \\
& =\frac{1}{2^{n}} \sum_{x \in\{0,1\}^{n}}\left|(1+2 \delta)^{c(\lambda, x)}(1-2 \delta)^{\frac{n}{2}-c(\lambda, x)}-1\right| \\
& =\frac{1}{2^{n}} \sum_{k=0}^{\frac{n}{2}} \sum_{x: c(\lambda, x)=k}\left|(1+2 \delta)^{k}(1-2 \delta)^{\frac{n}{2}-k}-1\right| \\
& =\frac{1}{2^{n}} \sum_{k=0}^{\frac{n}{2}} 2^{\frac{n}{2}}\binom{\frac{n}{2}}{k}\left|(1+2 \delta)^{k}(1-2 \delta)^{\frac{n}{2}-k}-1\right| \\
& =\sum_{k=0}^{\frac{n}{2}}\binom{\frac{n}{2}}{k}\left|\left(\frac{1+2 \delta}{2}\right)^{k}\left(\frac{1-2 \delta}{2}\right)^{\frac{n}{2}-k}-\frac{1}{2^{\frac{n}{2}}}\right| \\
& =2 d_{\mathrm{TV}}\left(\operatorname{Bin}\left(\frac{n}{2}, \frac{1}{2}\right), \operatorname{Bin}\left(\frac{n}{2}, \frac{1}{2}+\delta\right)\right) \\
& =\Omega(\epsilon),
\end{aligned}
$$

where the last equality follows from Lemma 8 .
Proof of Item 3 Let the distribution $Q$ over $\left(\{0,1\}^{n}\right)^{m}$ be the uniform mixture

$$
Q \stackrel{\text { def }}{=} \mathbb{E}_{\lambda}\left[P_{\lambda}^{\otimes m}\right]
$$

where $P_{\lambda}$ is the distribution on $\{0,1\}^{n}$ corresponding to the matching-orientation parameter $\lambda$. In particular, for any $x \in\{0,1\}^{n}$ we have

$$
P_{\lambda}(x)=U(x)(1+2 \delta)^{c(\lambda, x)}(1-2 \delta)^{\frac{n}{2}-c(\lambda, x)}
$$

with $U$ being the uniform distribution on $\{0,1\}^{n}$ and $c(\lambda, x)$, the agreement count of $x$ for $\lambda$, defined as before. Now, this leads to

$$
\frac{d P_{\lambda}}{d u}(x)=1+G(\lambda, x)
$$

where $G(\lambda, x) \stackrel{\text { def }}{=}(1-2 \delta)^{\frac{n}{2}}\left(\frac{1+2 \delta}{1-2 \delta}\right)^{c(\lambda, x)}-1$. For two matching-orientation parameters $\lambda, \mu$, we can define the covariance $\tau(\lambda, \mu) \stackrel{\text { def }}{=} \mathbb{E}_{x \sim U}[G(\lambda, x) G(\mu, x)]$. By the minimax approach (as in [Pol03, Chapter 3]), it is sufficient to bound the $L_{1}$-distance between $Q$ and $U^{\otimes m}$ by a small constant. Moreover, we have

$$
\left\|Q-U^{\otimes m}\right\|_{1} \leq \mathbb{E}_{\lambda, \mu}\left[\left(1+\tau(\lambda, \mu)\right)^{m}\right]-1
$$

and to show the lower bound it is sufficient to prove that the RHS is less than $\frac{1}{10}$ unless $m=\Omega\left(\frac{n}{\epsilon^{2}}\right)$. Setting $z \stackrel{\text { def }}{=} \frac{1+2 \delta}{1-2 \delta}$, we can derive, by expanding the definition

$$
\tau(\lambda, \mu)=1+(1-2 \delta)^{n} \mathbb{E}_{x \sim U}\left[z^{c(\lambda, x)+c(\mu, x)}\right]-2(1-2 \delta)^{\frac{n}{2}} \mathbb{E}_{x \sim U}\left[z^{c(\lambda, x)}\right]
$$

Since, when $x$ is uniformly drawn in $\{0,1\}^{n}, c(\lambda, x)$ follows a $\operatorname{Bin}\left(\frac{n}{2}, \frac{1}{2}\right)$ distribution, we can compute the last term as

$$
2(1-2 \delta)^{\frac{n}{2}} \mathbb{E}_{x \sim U}\left[z^{c(\lambda, x)}\right]=2(1-2 \delta)^{\frac{n}{2}}\left(\frac{1+z}{2}\right)^{\frac{n}{2}}=2(1-2 \delta)^{\frac{n}{2}} \frac{1}{(1-2 \delta)^{\frac{n}{2}}}=2
$$

where we used the expression of the probability-generating function of a Binomial. This leads to

$$
1+\tau(\lambda, \mu)=(1-2 \delta)^{n} \mathbb{E}_{x \sim U}\left[z^{c(\lambda, x)+c(\mu, x)}\right]=(1-2 \delta)^{n} z^{|B|} \mathbb{E}_{\alpha \sim \operatorname{Bin}\left(|A|, \frac{1}{2}\right)}\left[z^{2 \alpha}\right] \prod_{\substack{\sigma \text { cycle } \\|\sigma| \geq 4}} \mathbb{E}_{\alpha \sim \mathcal{B}_{\lambda, \mu}(\sigma)}\left[z^{\alpha}\right]
$$

where "cycle" and the probability distribution $\mathcal{B}_{\lambda, \mu}(\sigma)$ are defined as follows. Recall that $\lambda$ and $\mu$ define a weighted multigraph over $n$ vertices, where each vertex has degree exactly 2 , the edges are from the pairs $\lambda_{\iota}^{(1)}$ 's and $\mu_{\iota}^{(1)}$ 's, and the weights are in $\{0,1\}$ according to the $\lambda_{\iota}^{(2)}$ 's and $\mu_{\iota}^{(2)}$ 's. That multigraph $G_{\lambda, \mu}$ is better seen as the disjoint union of cycles (and indeed, $A \cup B$ corresponds to the cycles of length 2 , while $C$ corresponds to cycles of length at least 4).

For such a cycle $\sigma$ in $G_{\lambda, \mu}$, we let $\mathcal{B}_{\lambda, \mu}(\sigma)$ be the distribution below. If the number of negative covariances - the number of edges with label $\lambda_{\ell}^{(2)}=1$ or $\mu_{\ell}^{(2)}=1$ - along $\sigma$ is even (resp. odd), then $\mathcal{B}_{\lambda, \mu}(\sigma)$ is a $\operatorname{Bin}\left(|\sigma|, \frac{1}{2}\right)$ conditioned on being even (resp. odd).

Instead of the above, we first consider the related quantity with the conditioning removed (indeed, as we will see in Claim 12, this new quantity is within an $1+O\left(\epsilon^{2}\right)$ factor of the actual one): in what follows, all the expectations are taken over the random variable $\alpha$, distributed as

indicated in the subscript:

$$
\begin{aligned}
& 1+\tilde{\tau}(\lambda, \mu)=(1-2 \delta)^{n} z^{|B|} \mathbb{E}_{\operatorname{Bin}\left(|A|, \frac{1}{2}\right)}\left[z^{2 \alpha}\right] \prod_{\substack{\sigma \text { cycle } \\
|\sigma| \geq 4}} \mathbb{E}_{\operatorname{Bin}\left(|\sigma|, \frac{1}{2}\right)}\left[z^{\alpha}\right] \\
& =(1-2 \delta)^{n} z^{|B|} \mathbb{E}_{\operatorname{Bin}\left(|A|, \frac{1}{2}\right)}\left[z^{2 \alpha}\right] \mathbb{E}_{\operatorname{Bin}\left(\sum_{\sigma:|\sigma| \geq 4}|\sigma|, \frac{1}{2}\right)}\left[z^{\alpha}\right] \\
& =(1-2 \delta)^{n} z^{|B|} \mathbb{E}_{\operatorname{Bin}\left(|A|, \frac{1}{2}\right)}\left[z^{2 \alpha}\right] \mathbb{E}_{\operatorname{Bin}\left(|C|, \frac{1}{2}\right)}\left[z^{\alpha}\right] \\
& =(1-2 \delta)^{n} z^{|B|}\left(\frac{1+z^{2}}{2}\right)^{|A|}\left(\frac{1+z}{2}\right)^{|C|} \\
& =\left((1-2 \delta)^{2} z\right)^{|B|}\left((1-2 \delta)^{2} \frac{1+z^{2}}{2}\right)^{|A|} \underbrace{\left((1-2 \delta) \frac{1+z}{2}\right)^{|C|}}_{\begin{array}{c}
=1 \\
=1
\end{array}}
\end{aligned}
$$

Thus, we need to compute

$$
\mathbb{E}_{\lambda, \mu}\left[(1+\tilde{\tau}(\lambda, \mu))^{m}\right]=\mathbb{E}_{\lambda, \mu}\left[\left(1+4 \delta^{2}\right)^{m|A|}\left(1-4 \delta^{2}\right)^{m|B|}\right]=\mathbb{E}_{\lambda, \mu}\left[a^{|A|} b^{|B|}\right]
$$

where $a \stackrel{\text { def }}{=}\left(1+4 \delta^{2}\right)^{m}, b \stackrel{\text { def }}{=}\left(1-4 \delta^{2}\right)^{m}$. This leads to

$$
\begin{aligned}
\mathbb{E}_{\lambda, \mu}\left[(1+\tilde{\tau}(\lambda, \mu))^{m}\right] & =\mathbb{E}_{\lambda, \mu}\left[\mathbb{E}\left[a^{|A|} b^{|B|}\left||A|+|B|\right]\right]\right. \\
& =\mathbb{E}_{\lambda, \mu}\left[b^{|A|+|B|} \mathbb{E}\left[\left(\frac{a}{b}\right)^{|A|}| | A|+|B|\right]\right] \\
& =\mathbb{E}_{\lambda, \mu}\left[b^{|A|+|B|}\left(\frac{1+\frac{a}{b}}{2}\right)^{|A|+|B|}\right] \quad\left(\text { since }|A| \sim \operatorname{Bin}\left(|A|+|B|, \frac{1}{2}\right)\right) \\
& =\mathbb{E}_{\lambda, \mu}\left[\left(\frac{a+b}{2}\right)^{|A|+|B|}\right] \\
& =\mathbb{E}_{\lambda, \mu}\left[\left(\frac{\left(1+4 \delta^{2}\right)^{m}+\left(1-4 \delta^{2}\right)^{m}}{2}\right)^{|A|+|B|}\right]
\end{aligned}
$$

In particular, consider the following upper bound on $f(k)$, the probability that $|A|+|B| \geq k$ : setting $s \stackrel{\text { def }}{=} \frac{n}{2}$, for $0 \leq k \leq s$,

$$
\begin{aligned}
f(k) & =\operatorname{Pr}[|A|+|B| \geq k] \\
& \leq \frac{s!2^{s}}{(2 s)!} \cdot\binom{s}{k} \frac{(2 s-2 k)!}{(s-k)!2^{s-k}}=\frac{2^{k} k!}{(2 k)!} \frac{\binom{s}{k}^{2}}{\binom{2 s}{2 k}} \\
& =\frac{2^{k}}{k!} \frac{\binom{2(s-k)}{s-k}}{\binom{2 s}{s}}=\frac{2^{k}}{k!} \frac{\prod_{j=0}^{k-1}(s-j)^{2}}{\prod_{j=0}^{2 k-1}(2 s-j)} \\
& =\frac{1}{k!} \frac{\prod_{j=0}^{k-1}(s-j)}{\prod_{j=0}^{k-1}(2 s-2 j-1)} \leq \frac{1}{k!}
\end{aligned}
$$

Therefore, for any $z>1$, we have

$$
\begin{aligned}
\mathbb{E}_{\lambda, \mu}\left[z^{|A|+|B|}\right] & =\int_{0}^{\infty} \operatorname{Pr}\left[z^{|A|+|B|} \geq t\right] d t \\
& =\int_{0}^{\infty} \operatorname{Pr}\left[|A|+|B| \geq \frac{\ln t}{\ln z}\right] d t \\
& =1+\int_{1}^{\infty} \operatorname{Pr}\left[|A|+|B| \geq \frac{\ln t}{\ln z}\right] d t \\
& \leq 1+\int_{1}^{\infty} \operatorname{Pr}\left[|A|+|B| \geq\left\lfloor\frac{\ln t}{\ln z}\right\rfloor\right] d t \\
& \leq 1+\int_{1}^{\infty} \frac{d t}{\left\lfloor\frac{\ln t}{\ln z}\right\rfloor!} \leq 1+\int_{1}^{\infty} \frac{d t}{\Gamma\left(\frac{\ln t}{\ln z}\right)} \quad \text { (from our upper bound on } f(k)) \\
& =1+\int_{1}^{\infty} \frac{e^{u} d u}{\Gamma\left(\frac{u}{\ln z}\right)}
\end{aligned}
$$

Assuming now that $1<z \leq 1+\gamma$ for some $\gamma \in(0,1)$, from $\ln z<\gamma$ and monotonicity of the Gamma function we obtain

$$
\mathbb{E}_{\lambda, \mu}\left[z^{|A|+|B|}\right]=1+\int_{1}^{\infty} \frac{e^{u} d u}{\Gamma\left(\frac{u}{\gamma}\right)}=1+\gamma \int_{1 / \gamma}^{\infty} \frac{e^{\gamma v} d v}{\Gamma(v)} \leq 1+\gamma \int_{0}^{\infty} \frac{e^{v} d v}{\Gamma(v)} \leq 1+42 \gamma
$$

Suppose now $m \leq c \frac{n}{\epsilon^{2}}=\frac{4 c}{\delta^{2}}$, for some constant $c>0$ to be determined later. Then, by monotonicity

$$
z \frac{\operatorname{def}}{=} \frac{\left(1+4 \delta^{2}\right)^{m}+\left(1-4 \delta^{2}\right)^{m}}{2} \leq \frac{\left(1+4 \delta^{2}\right)^{\frac{4 c}{\delta^{2}}}+\left(1-4 \delta^{2}\right)^{\frac{8 c}{\delta^{2}}}} \leq \frac{e^{16 c}+e^{-16 c}}{2}<1+\frac{1}{42 \cdot 20} \stackrel{\text { def }}{=} 1+\gamma
$$

for $c<\frac{3}{1000}$. Therefore,

$$
\mathbb{E}_{\lambda, \mu}\left[(1+\tilde{\tau}(\lambda, \mu))^{m}\right]-1=\mathbb{E}_{\lambda, \mu}\left[z^{|A|+|B|}\right]-1<\frac{1}{20}
$$

as desired.
To conclude, we bound $\mathbb{E}_{\lambda, \mu}\left[(1+\tau(\lambda, \mu))^{m}\right]$ combining the above with the following claim:
Claim 12. Let $z \stackrel{\text { def }}{=} \frac{1+2 \delta}{1-2 \delta}$ as above. Then for any two matching-orientation parameters $\lambda, \mu$, we have

$$
\prod_{\sigma:|\sigma| \geq 4} \mathbb{E}_{\alpha \sim \mathcal{B}_{\lambda, \mu}(\sigma)}\left[z^{\alpha}\right] \leq e^{\frac{8 c^{4}}{n}} \cdot \mathbb{E}_{\alpha \sim \operatorname{Bin}\left(\sum_{\sigma:|\sigma| \geq 4}|\sigma|, \frac{1}{2}\right)}\left[z^{\alpha}\right]
$$

where $\mathcal{B}_{\lambda, \mu}(\sigma)$ is the probability distribution defined earlier.
Proof. Fix $\lambda, \mu$ as in the statement, and any cycle $\sigma$ in the resulting graph. Suppose first this is an "even" cycle:

$$
\mathbb{E}_{\alpha \sim \mathcal{B}_{\lambda, \mu}(\sigma)}\left[z^{\alpha}\right]=\mathbb{E}_{\alpha \sim \operatorname{Bin}\left(|\sigma|, \frac{1}{2}\right)}\left[z^{\alpha} \mid \alpha \text { even }\right]=\frac{1}{1 / 2} \sum_{k=0}^{|\sigma| / 2}\binom{|\sigma|}{2 k} z^{2 k}=\frac{(1+z)^{|\sigma|}+(1-z)^{|\sigma|}}{2^{|\sigma|}}
$$

Similarly, if $\sigma$ is an "odd" cycle, $\mathbb{E}_{\alpha \sim \mathcal{B}_{\lambda, \mu}(\sigma)}\left[z^{\alpha}\right]=\frac{(1+z)^{|\sigma|}-(1-z)^{|\sigma|}}{2^{|\sigma|}}$. We then obtain $\mathbb{E}_{\alpha \sim \mathcal{B}_{\lambda, \mu}(\sigma)}\left[z^{\alpha}\right] \leq$ $\mathbb{E}_{\alpha \sim \operatorname{Bin}\left(|\sigma|, \frac{1}{2}\right)}\left[z^{\alpha}\right]\left(1+\left|\frac{1-z}{1+z}\right|^{|\sigma|}\right)$, from which

$$
\begin{aligned}
\prod_{\sigma} \mathbb{E}_{\alpha \sim \mathcal{B}_{\lambda, \mu}(\sigma)}\left[z^{\alpha}\right] & \leq \prod_{\sigma} \mathbb{E}_{\alpha \sim \operatorname{Bin}\left(|\sigma|, \frac{1}{2}\right)}\left[z^{\alpha}\right]\left(1+\left|\frac{1-z}{1+z}\right|^{|\sigma|}\right) \\
& =\mathbb{E}_{\alpha \sim \operatorname{Bin}\left(\sum_{\sigma}|\sigma|, \frac{1}{2}\right)}\left[z^{\alpha}\right] \prod_{\sigma}\left(1+\left|\frac{1-z}{1+z}\right|^{|\sigma|}\right)
\end{aligned}
$$

We now bound the last factor: since $\left|\frac{1-z}{1+z}\right|=2 \delta=\frac{2 \epsilon}{\sqrt{n}}$ we have at most $\frac{n}{2}$ cycles, we get

$$
\prod_{\sigma:|\sigma| \geq 4}\left(1+\left|\frac{1-z}{1+z}\right|^{|\sigma|}\right)=\prod_{\sigma:|\sigma| \geq 4}\left(1+(2 \delta)^{|\sigma|}\right) \leq\left(1+16 \delta^{4}\right)^{\frac{n}{2}} \leq e^{8 \frac{\epsilon^{4}}{n}}
$$

as claimed.
With this result in hand, we can get the conclusion we want: for any $\lambda, \mu$,

$$
\begin{aligned}
1+\tau(\lambda, \mu) & =(1-2 \delta)^{n} z^{|B|} \mathbb{E}_{\alpha \sim \operatorname{Bin}\left(|A|, \frac{1}{2}\right)}\left[z^{2 \alpha}\right] \prod_{\substack{\sigma \text { cycle } \\
|\sigma| \geq 4}} \mathbb{E}_{\alpha \sim \mathcal{B}_{\lambda, \mu}(\sigma)}\left[z^{\alpha}\right] \\
& \leq e^{\frac{8 \epsilon^{4}}{n}}(1-2 \delta)^{n} z^{|B|} \mathbb{E}_{\alpha \sim \operatorname{Bin}\left(|A|, \frac{1}{2}\right)}\left[z^{2 \alpha}\right] \cdot \mathbb{E}_{\alpha \sim \operatorname{Bin}\left(\sum_{\sigma:|\sigma| \geq 4}|\sigma|, \frac{1}{2}\right)}\left[z^{\alpha}\right] \\
& =e^{\frac{8 \epsilon^{4}}{n}}(1+\tilde{\tau}(\lambda, \mu))
\end{aligned}
$$

from which

$$
\begin{aligned}
\mathbb{E}_{\lambda, \mu}\left[(1+\tau(\lambda, \mu))^{m}\right] & \leq e^{\frac{8 \epsilon^{4} m}{n}} \mathbb{E}_{\lambda, \mu}\left[(1+\tilde{\tau}(\lambda, \mu))^{m}\right] \\
& \leq e^{\frac{8 \epsilon^{4} m}{n}}\left(1+\frac{1}{20}\right) \\
& \leq e^{8 c \epsilon^{2}} \frac{21}{20}<1+\frac{1}{10}
\end{aligned}
$$

(as $c<\frac{3}{1000}$ and $\epsilon \leq 1$ )
concluding the proof: by (8), $\left\|Q-U^{\otimes m}\right\|_{1} \leq \frac{1}{10}$, for any $m<c \frac{n}{\epsilon^{2}}$.

# 8.2 Identity Testing Algorithm against Non-Degenerate Bayes Nets 

We start with the case of trees and then generalize to bounded degree.

### 8.2.1 The Case of Trees

In this section, we prove our result on testing identity of a tree structured Bayes net with unknown topology. Recall from Section 8.1 that a Bayes net with tree structure is said to be $c$-balanced if it satisfies $p_{k} \in[c, 1-c]$ for all $k$. We will require the following definition of non-degeneracy of a tree, which will be a simpler case of the definition we shall have for general Bayes nets (Definition 8):

Definition 7. For any $\gamma \in(0,1]$, we say a tree Bayes net $P$ over $\{0,1\}^{n}$ is $\gamma$-non-degenerate if for all $i \in[n]$,

$$
\left|\operatorname{Pr}\left[X_{i}=1 \mid X_{\operatorname{Par}(i)}=1\right]-\operatorname{Pr}\left[X_{i}=1 \mid X_{\operatorname{Par}(i)}=0\right]\right| \geq \gamma
$$

where $X \sim P$.
Roughly speaking, this definition states that the choice of the value of its parent has a significant influence on the probability of any node. With these definitions, we are ready to state and prove our result:
Theorem 15. There exists an efficient algorithm with the following guarantees. Given as input (i) a tree $\mathcal{S}$ over $n$ nodes and an explicit c-balanced, $\gamma$-non-degenerate Bayes net $Q$ with structure $\mathcal{S}$, where $c, \gamma=\Omega\left(1 / n^{a}\right)$ for some absolute constant $a>0$; (ii) parameter $\epsilon>0$, and (iii) sample access to a Bayes net $P$ with unknown tree structure, the algorithm takes $O\left(\sqrt{n} / \epsilon^{2}\right)$ samples from $P$, and distinguishes with probability at least $2 / 3$ between $P=Q$ and $\|P-Q\|_{1}>\epsilon$.

The algorithm follows a natural idea: (1) check that the unknown distribution $P$ indeed has, as it should, the same tree structure as the (known) distribution $Q$; (2) if so, invoke the algorithm of the previous section, which works under the assumption that $P$ and $Q$ have the same structure.

Therefore, to establish the theorem it is sufficient to show that (1) can be performed efficiently. Specifically, we will prove the following:
Theorem 16. There exists an algorithm with the following guarantees. For $\gamma \in(0,1), c \in(0,1 / 2)$, it takes as input an explicit c-balanced, $\gamma$-nondegenerate tree Bayes net $Q$ over $\{0,1\}^{n}$ with structure $\mathcal{S}(Q)$, and

$$
O\left(\frac{\log ^{2} \frac{1}{c}}{c^{6} \gamma^{4}} \log n\right)
$$

samples from an arbitrary tree Bayes net $P$ over $\{0,1\}^{n}$ with unknown structure $\mathcal{S}(P)$.

- If $P=Q$, the algorithm returns accept with probability at least $4 / 5$;
- If $\mathcal{S}(P) \neq \mathcal{S}(Q)$, the algorithm returns reject with probability at least $4 / 5$.

Note that the above theorem implies the desired result as long as $\frac{\log ^{2} \frac{1}{c}}{c^{6} \gamma^{4}}=O\left(\frac{\sqrt{n}}{c^{2} \log n}\right)$.
Proof of Theorem 16. We start by stating and proving lemmas that will be crucial in stating and analyzing the algorithm:
Fact 3. Given $\tau>0$ and sample access to a tree Bayes net $P$ over $\{0,1\}^{n}$, one can obtain with $O\left(\frac{\log n}{\tau^{2}}\right)$ samples estimates $\left(\hat{\mu}_{i}\right)_{i \in[n]},\left(\hat{\rho}_{i, j}\right)_{i, j \in[n]}$ such that, with probability at least $9 / 10$,

$$
\max \left(\max _{i \in[n]}\left|\hat{\mu}_{i}-\mathbb{E}\left[X_{i}\right]\right|, \max _{i, \in[n]}\left|\hat{\rho}_{i, j}-\mathbb{E}\left[X_{i} X_{j}\right]\right|\right) \leq \tau
$$

Proof. The fact follows immediately by an application of Chernoff bounds.
Lemma 22. Let $c \in(0,1 / 2]$. There exists a constant $\lambda$ and a function $f$ such that

$$
I\left(X_{i} ; X_{j}\right)=f\left(\mathbb{E}\left[X_{i}\right], \mathbb{E}\left[X_{j}\right], \mathbb{E}\left[X_{i} X_{j}\right]\right)
$$

for any c-balanced tree Bayes net $P$ over $\{0,1\}^{n}$ and $X \sim P$, where $f$ is $\lambda$-Lipschitz with respect to the $\|\cdot\|_{\infty}$ norm on the domain $\Omega_{c} \subseteq[0,1] \times[0,1] \times[0,1] \rightarrow[0,1]$ in which $\left(\mathbb{E}\left[X_{i}\right], \mathbb{E}\left[X_{j}\right], \mathbb{E}\left[X_{i} X_{j}\right]\right)_{i, j}$ then take values. Moreover, one can take $\lambda=16 \log \frac{1}{c}$.

Proof Sketch: Expanding the definition of mutual influence $I(X ; Y)$ of two random variables, it is not hard to write it as a function of $\mathbb{E}[X], \mathbb{E}[Y]$, and $\mathbb{E}[X Y]$ only. This function would not be Lipschitz on its entire domain, however. The core of the proof leverages the balancedness assumption to restrict its domain to a convenient subset $\Omega_{c} \subseteq[0,1] \times[0,1] \times[0,1]$, on which it becomes possible to bound the partial derivatives of $f$. We defer the details of the proof to Appendix D.

We now show the following crucial lemma establishing the following result: For any balanced Bayes net, the shared information between any pair of non-adjacent vertices $i, j$ is noticeably smaller than the minimum shared information between any pair of neighbors along the path that connects $i, j$.

Lemma 23. Let $c \in(0,1 / 2]$, and fix any c-balanced tree Bayes net $P$ over $\{0,1\}^{n}$ with structure $\mathcal{S}(Q)$. Then, for any distinct $i, j \in[n]$ such that $i \neq \operatorname{Par}(j)$ and $j \neq \operatorname{Par}(i)$, we have

$$
I\left(X_{i} ; X_{j}\right) \leq\left(1-2 c^{2}\right) \min _{\{k, \operatorname{Par}(k)\} \in \operatorname{path}(i, j)} I\left(X_{k} ; X_{\operatorname{Par}(k)}\right)
$$

where $X \sim P$. (and $\operatorname{path}(i, j)$ is a path between $i$ to $j$, of the form $i-\cdots-k-\cdots-j$, where each edge is of the form $(k, \operatorname{Par}(k)$ or $(\operatorname{Par}(k), k))$.

Proof. By induction and the data processing inequality, it is sufficient to prove the statement for a path of length 3, namely

$$
X_{i}-X_{k}-X_{j}
$$

The result will follow from a version of the strong data processing inequality (see e.g., [PW15], from which we borrow the notation $\left.\eta_{\mathrm{KL}}, \eta_{\mathrm{TV}}\right)$ : since $X_{i} \rightarrow X_{k} \rightarrow X_{j}$ forms a chain with the Markov property, we get $I\left(X_{i} ; X_{j}\right) \leq \eta_{\mathrm{KL}}\left(P_{X_{j} \mid X_{k}}\right) I\left(X_{i} ; X_{k}\right)$ from [PW15, Equation 17]. Now, by [PW15, Theorem 1], we have

$$
\eta_{\mathrm{KL}}\left(P_{X_{j} \mid X_{k}}\right) \leq \eta_{\mathrm{TV}}\left(P_{X_{j} \mid X_{k}}\right)=d_{\mathrm{TV}}\left(P_{X_{j} \mid X_{k}=0}, P_{X_{j} \mid X_{k}=1}\right)
$$

If $k=\operatorname{Par}(j)$ (in our Bayes net), then $d_{\mathrm{T} V}\left(P_{X_{j} \mid X_{k}=0}, P_{X_{j} \mid X_{k}=1}\right)=\left|p_{j, 0}-p_{j, 1}\right| \leq 1-2 c$ from the $c$-balancedness assumption. On the other hand, if $j=\operatorname{Par}(k)$, then by Bayes' rule it is easy to check that (again, from the $c$-balancedness assumption) $\operatorname{Pr}\left[X_{\operatorname{Par}(k)}=1 \mid X_{k}=a\right] \in\left[c^{2}, 1-c^{2}\right]$, and

$$
d_{\mathrm{T} V}\left(P_{X_{j} \mid X_{k}=0}, P_{X_{j} \mid X_{k}=1}\right)=\left|\operatorname{Pr}\left[X_{j}=1 \mid X_{k}=0\right]-\operatorname{Pr}\left[X_{j}=1 \mid X_{k}=1\right]\right| \leq 1-2 c^{2}
$$

Therefore, we get $I\left(X_{i} ; X_{j}\right) \leq\left(1-2 c^{2}\right) I\left(X_{i} ; X_{k}\right)$ as wanted; by symmetry, $I\left(X_{i} ; X_{j}\right) \leq(1-$ $\left.2 c^{2}\right) I\left(X_{j} ; X_{k}\right)$ holds as well.

Lemma 24. Let $c \in(0,1 / 2], \gamma \in(0,1)$, and fix any c-balanced, $\gamma$-nondegenerate tree Bayes net $P$ over $\{0,1\}^{n}$, with structure $\mathcal{S}(P)$. Then, there exists an absolute constant $\kappa$ such that for any $i \in[n]$ one has

$$
I\left(X_{i} ; X_{\operatorname{Par}(i)}\right) \geq \kappa
$$

where $X \sim P$. (Moreover, one can take $\kappa=\frac{c \gamma^{2}}{2 \ln 2}$.)

Proof. Fix any such $i$, and write $X=X_{i}, Y=X_{\operatorname{Par}(i)}$ for convenience; and set $u \stackrel{\text { def }}{=} \operatorname{Pr}[X=1]$, $v \stackrel{\text { def }}{=} \operatorname{Pr}[Y=1], a \stackrel{\text { def }}{=} \operatorname{Pr}[X=1 \mid Y=1]$, and $b \stackrel{\text { def }}{=} \operatorname{Pr}[X=1 \mid Y=0]$. We then have

$$
\begin{aligned}
I(X ; Y) & =\sum_{x, y \in\{0,1\}} \operatorname{Pr}[X=x, Y=y] \log \frac{\operatorname{Pr}[X=x, Y=y]}{\operatorname{Pr}[X=x] \operatorname{Pr}[Y=y]} \\
& =\sum_{x, y \in\{0,1\}} \operatorname{Pr}[X=x \mid Y=y] \operatorname{Pr}[Y=y] \cdot \log \frac{\operatorname{Pr}[X=x \mid Y=y]}{\operatorname{Pr}[X=x]} \\
& =(1-u)(1-b) \log \frac{1-b}{1-v}+(1-u) b \log \frac{b}{v}+u(1-a) \log \frac{1-a}{1-v}+u a \log \frac{a}{v} \\
& =u \varphi(a, v)+(1-u) \varphi(b, v)
\end{aligned}
$$

where $\varphi(x, y) \stackrel{\text { def }}{=} x \log \frac{x}{y}+(1-x) \log \frac{1-x}{1-y} \geq 0$ for $x, y \in[0,1]$ is the KL-divergence between two Bernoulli distributions with parameters $x, y$. From our assumptions of $c$-balanced and $\gamma$ nondegeneracy, we know that $u, v, a, b$ satisfy

$$
\begin{aligned}
& c \leq a, b, u, v \leq 1-c \\
& \gamma \leq|a-b|
\end{aligned}
$$

which leads to, noticing that $|a-b| \geq \gamma$ implies that at least one of $|a-v| \geq \frac{\gamma}{2},|b-v| \geq \frac{\gamma}{2}$ holds and that $\varphi(\cdot, v)$ is convex with a minimum at $v$ :

$$
I(X ; Y) \geq c(\varphi(a, v)+\varphi(b, v)) \geq c \min \left(\varphi\left(v-\frac{\gamma}{2}, v\right), \varphi\left(v+\frac{\gamma}{2}, v\right)\right) \geq \frac{1}{2 \ln 2} c \gamma^{2}
$$

using the standard lower bound of $\varphi(x, y) \geq \frac{2}{\ln 2}(x-y)^{2}$ on the KL-divergence.
The Algorithm With these in hand, we are ready to describe and analyze the algorithm underlying Theorem 16:

Let $\gamma \in(0,1), c \in(0,1 / 2)$ be fixed constants, and $Q$ be a known $c$-balanced, $\gamma$-nondegenerate tree Bayes net over $\{0,1\}^{n}$, with structure $\mathcal{S}(Q)$. Furthermore, let $P$ be an unknown tree Bayes net over $\{0,1\}^{n}$ with unknown structure $\mathcal{S}(P)$, to which we have sample access.

Let $\kappa=\kappa(c, \gamma)=\frac{c \gamma^{2}}{2 \ln 2}$ as in Lemma $24, c^{\prime} \stackrel{\text { def }}{=} \frac{c}{2}$, and $\lambda=\lambda\left(c^{\prime}\right)=16 \log \frac{2}{c}$ as in Lemma 22. In view of applying Lemma 23 later to $P$, set

$$
\tau \stackrel{\text { def }}{=} \frac{\kappa-\left(1-2 c^{\prime 2}\right) \kappa}{4 \lambda}=\frac{1}{64 \ln 2} \frac{c^{3} \gamma^{2}}{\log \frac{2}{c}}
$$

The algorithm then proceeds as follows. (Below, $X$ denotes a random variable distributed according to $P$.)

1. Take $m=O\left(\frac{\log n}{\tau^{2}}\right)$ samples from $P$, and use them to

- Estimate all $n^{2}$ marginals $\operatorname{Pr}\left[X_{i}=1 \mid X_{j}=a\right]$, and verify that they are all in $\left[c^{\prime}, 1-c^{\prime}\right]$ (ensuring that $P$ is $c^{\prime}$-balanced), with probability at least $9 / 10$. Else, return reject;
- Estimate all $\binom{n}{2}+n$ values of $\mathbb{E}\left[X_{i}\right]$ and $\mathbb{E}\left[X_{i} X_{j}\right]$ to an additive $\tau$, with probability at least $9 / 10$, as in Fact 3. (Call these estimates $\check{\mu}_{i}, \check{\rho}_{i, j}$.)

At the end of this step, we are guaranteed that $P$ is $c^{\prime}$-balanced (or else we have rejected with probability at least $9 / 10$ ).
2. Check that all $\hat{\mu}_{i}, \hat{\rho}_{i, j}$ 's are all within an additive $\tau$ of what they should be under $Q$. If so, return accept, else return reject.

Clearly, the algorithm only uses $O\left(\frac{\log ^{2} \frac{1}{\lambda}}{\epsilon^{6} \gamma^{4}} \log n\right)$ samples from $P$. We now establish its correctness: first, with probability at least $4 / 5$ by a union bound, all estimates performed in the first step are correct; we condition on that.

Completeness. If $P=Q$, then $P$ is $c$-balanced, and thus a fortiori $c^{\prime}$-balanced: the algorithm does not reject in the first step. Moreover, clearly all $\left(\hat{\mu}_{i}\right)_{i},\left(\hat{\rho}_{i, j}\right)_{i, j}$ are then within an additive $\tau$ of the corresponding values of $P=Q$, so the algorithm returns accept.

Soundness. By contrapositive. If the algorithm returns accept, then $P$ is $c^{\prime}$-balanced by the first step. Given our setting of $\tau$, by Lemma 22 our estimates $\left(\hat{\mu}_{i}\right)_{i},\left(\hat{\rho}_{i, j}\right)_{i, j}$ are such that all corresponding quantities

$$
\hat{I}_{i, j} \stackrel{\text { def }}{=} f\left(\hat{\mu}_{i}, \hat{\mu}_{j}, \hat{\rho}_{i, j}\right)
$$

are within $\tau \lambda=\frac{\kappa-\left(1-2 c^{\prime 2}\right) \kappa}{4}$ of the mutual informations $I\left(X_{i} ; X_{j}\right)$ for $P$. But then, by Lemma 23 this implies that the relative order of all $\hat{I}_{i, j}, \hat{I}_{i^{\prime}, j^{\prime}}$ is the same as that of $I\left(X_{i} ; X_{j}\right), I\left(X_{i^{\prime}} ; X_{j^{\prime}}\right)$. This itself implies that running the Chow-Liu algorithm on input these $\hat{I}_{i, j}$ 's would yield the same, uniquely determined tree structure $\mathcal{S}(P)$ as if running it on the actual $I\left(X_{i} ; X_{j}\right)$ 's. To see this, we note that the Chow-Liu algorithm works by computing a maximum-weight spanning tree (MST) with respect to the weights given by the pairwise mutual information. The claim follows from the fact that the MST only depends on the relative ordering of the edge-weights.
But since the $\left(\hat{\mu}_{i}\right)_{i},\left(\hat{\rho}_{i, j}\right)_{i, j}$ are also within an additive $\tau$ of the corresponding quantities for $Q$ (per our check in the second step), the same argument shows that running the Chow-Liu algorithm would result in the same, uniquely determined tree structure $\mathcal{S}(Q)$ as if running it on the actual mutual informations from $Q$. Therefore, $\mathcal{S}(P)=\mathcal{S}(Q)$, concluding the proof.

# 8.2.2 The Case of Bounded Degree 

In this section, we show how to test identity of unknown structure Bayesian networks with maximum in-degree $d$ under some non-degeneracy conditions. Intuitively, we want these conditions to ensure identifiability of the structure: that is, that any (unknown) Bayes net close to a non-degenerate Bayes net $Q$ must also share the same structure. To capture this notion, observe that, by definition, non-equivalent Bayes net structures satisfy different conditional independence constraints: our nondegeneracy condition is then to rule out some of these possible new conditional independence constraints, as far from being satisfied by the non-degenerate Bayes net. Formally, we have the following definition:

Definition 8 (Non-degeneracy). For nodes $X_{i}, X_{j}$, set of nodes $S$, and a distribution $P$ over $\{0,1\}^{n}$, we say that $X_{i}$ and $X_{j}$ are $\gamma$-far from independent conditioned on $X_{S}$ if for all distributions $Q$ over $\{0,1\}^{n}$ such that $d_{\mathrm{TV}}(P, Q)<\gamma$, it holds that $X_{i}$ and $X_{j}$ are not independent conditioned on $X_{S}$.

A Bayes net $P$ is then called $\gamma$-non-degenerate with respect to structure $\mathcal{S}$ and degree $d$ if for any nodes $X_{i}, X_{j}$ and set of nodes $S$ of size $|S| \leq d$ not containing $i$ or $j$ satisfying one of the following:
(i) $X_{i}$ is a parent of $X_{j}$,
(ii) $S$ contains a node $X_{k}$ that is a child of both $X_{i}$ and $X_{j}$,
(iii) $X_{i}$ is a grandparent of $X_{j}$ and there is a child of $X_{i}$ and parent of $X_{j}, X_{k}$, that is not in $S$,
(iv) $X_{i}$ and $X_{j}$ have a common parent $X_{k}$ that is not in $S$
we have that $X_{i}$ and $X_{j}$ are $\gamma$-far from independent conditioned on $X_{S}$ (where all relations are under structure $\mathcal{S}$ ).
![img-0.jpeg](img-0.jpeg)

Figure 4: The four possible conditions of Definition 8, from left (i) to right (iv). The black nodes are the ones in $S$, the red ones (besides $X_{i}, X_{j}$ ) are not in $S$.

We shall also require some terminology: namely, the definition of the skeleton of a Bayesian network as the underlying undirected graph of its structure. We can now state the main result of this section:

Theorem 17. There exists an algorithm with the following guarantees. Given the full description of a Bayes net $Q$ of degree at most $d$ which is $(c, C)$ balanced and $\gamma$-non-degenerate for $c=\tilde{\Omega}(1 / \sqrt{n})$ and $C=\tilde{\Omega}\left(d \epsilon^{2} / \sqrt{n}\right)$, parameter $\epsilon \in(0,1]$, and sample access to a distribution $P$, promised to be a Bayes net of degree at most $d$ whose skeleton has no more edges than $Q$ 's, the algorithm takes $O\left(2^{d / 2} \sqrt{n} / \epsilon^{2}+\left(2^{d}+d \log n\right) / \gamma^{2}\right)$ samples from $P$, runs in time $O(n)^{d+3}\left(1 / \gamma^{2}+1 / \epsilon^{2}\right)$, and distinguishes with probability at least $2 / 3$ between (i) $P=Q$ and (ii) $\|P-Q\|_{1}>\epsilon$.

In Lemma 26, we show that these non-degeneracy conditions are enough to ensure identifiability of the structure, up to equivalence. In Proposition 1, we give a test for conditional independence specialized to Bernoulli random variables. In the last part, we provide a test for showing whether a non-degenerate Bayes net has a given structure using this conditional independence test, establishing Theorem 18. We then can combine this structure test with our test for Bayes nets with known structure to obtain Theorem 17. This structure tester, which may be of independent interest, has the following guarantees,

Theorem 18. Let $\mathcal{S}$ be a structure of degree at most $d$ and $P$ be a Bayesian network with structure $\mathcal{S}^{\prime}$ that also has degree at most $d$ and whose skeleton has no more edges than $\mathcal{S}$. Suppose that $P$

either (i) can be expressed as a Bayesian network with structure $\mathcal{S}$ that is $\gamma$-non-degenerate with degree d; or (ii) cannot be expressed as a Bayesian network with structure $\mathcal{S}$. Then there is an algorithm which can decide which case holds with probability 99/100, given $\mathcal{S}, \gamma$, and sample access to $P$. The algorithm takes $O\left(\left(2^{d}+d \log n\right) / \gamma^{2}\right)$ samples and runs in time $O\left(n^{d+3} / \gamma^{2}\right)$.

Using the above theorem, we can prove the main result of this section:
Proof of Theorem 17. We first invoke the structure test given in Fig. 6. If it accepts, we run the known structure test given in Theorem 12. We accept only if both accept.

The correctness and sample complexity now both follow from Theorem 18 and Theorem 12. Specifically, if the structure test accepts, then with high probability, we have that $Q$ can be expressed as a Bayes net with the same structure as $P$, and thus we have the pre-conditions for the known structure test. If either test rejects, then $P \neq Q$.

Non-degeneracy and Equivalent Structures The motivation behind the $\gamma$-non-degeneracy condition is the following: if $Q$ is $\gamma$-non-degenerate, then for any Bayesian network $P$ with degree at most $d$ that has $d_{\mathrm{T} V}(P, Q)<\gamma$ we will argue that $P$ can be described using the same structure $\mathcal{S}$ as we are given for $Q$. Indeed, the structure $\mathcal{S}^{\prime}$ of $P$ will have the property that $\mathcal{S}$ and $\mathcal{S}^{\prime}$ both can be used to describe the same Bayesian networks, a property known as $I$-equivalence. It will then remain to make this algorithmic, that is to describe how to decide whether $P$ can be described with the same structure as $Q$ or whether $d_{\mathrm{T} V}(P, Q) \geq \gamma$. Assuming we have this decision procedure, then if the former case happens to hold we can invoke our existing known-structure tester (or reject if the latter case holds).

We will require for our proofs the following definition:
Definition 9 ( $\vee$-structure). For a structure $\mathcal{S}$, a triple $(i, j, k)$ is a $\vee$-structure (also known as an immorality) if $i$ and $j$ are parents of $k$ but neither $i$ nor $j$ is a parent of the other.

The following result, due to Verma and Pearl [VP91], will play a key role:
Lemma 25. Two structures $\mathcal{S}$ and $\mathcal{S}^{\prime}$ are I-equivalent if and only if they have the same skeleton and the same $\vee$-structures.

Note that, for general structures $\mathcal{S}, \mathcal{S}^{\prime}$, it may be possible to represent all Bayesian networks with structure $\mathcal{S}$ as ones with structure $\mathcal{S}^{\prime}$, but not vice versa. Indeed, this can easily be achieved by adding edges to $\mathcal{S}$ to any node (if any) with less than $d$ parents. This is the rationale for the assumption in Theorem 18 that $\mathcal{S}^{\prime}$ has no more edges than $\mathcal{S}$ : as this assumption is then required for $\mathcal{S}$ and $\mathcal{S}^{\prime}$ to be $I$-equivalent unless $d_{\mathrm{T} V}(P, Q) \geq \gamma$.

We now prove that any Bayesian network $Q$ satisfiying the conditions of Theorem 18 and being non-degenerate with respect to a structure can in fact be expressed as having that structure.

Lemma 26. Fix $\gamma>0$. If $Q$ is a Bayesian network with structure $\mathcal{S}^{\prime}$ of degree at most $d$ that is $\gamma$-non-degenerate with respect to a structure $\mathcal{S}$ with degree at most $d$ and $\mathcal{S}^{\prime}$ has no more edges than $\mathcal{S}$, then $\mathcal{S}$ and $\mathcal{S}^{\prime}$ are I-equivalent.

Note that $Q$ being $\gamma$-non-degenerate for some $\gamma>0$ is equivalent to a set of conditional independence conditions all being false, since if $X_{i}$ and $X_{j}$ are not conditionally independent with respect to $X_{S}$, then there is a configuration $a$ such that $\operatorname{Pr}_{Q}\left[X_{S}=a\right]>0$ and $I\left(X_{i} ; X_{j} \mid X_{S}=a\right) \geq 0$.

Proof. We first show that $\mathcal{S}$ and $\mathcal{S}^{\prime}$ have the same skeleton and then that they have the same $\vee$-structures. We need the following:
Claim 13. Let $S$ be the set of parents of $X_{i}$ in a Bayesian network $Q$ with structure $\mathcal{S}$. Let $X_{j}$ be a node that is neither in $S$ nor a descendant of $X_{i}$. Then $X_{i}$ and $X_{j}$ are independent conditioned on $X_{S}$.

Proof. Firstly, we note that there is a numbering of the nodes which is consistent with the DAG of $\mathcal{S}$ such that any $j \in S$ has $j<i$. Explicitly, we can move $X_{i}$ and all its descendants to the end of the list of nodes to obtain this numbering.

Letting $D \stackrel{\text { def }}{=}\{1, \ldots, i-1\}$, we have that, from the definition of Bayesian networks, $\operatorname{Pr}_{Q}\left[X_{i}=\right.$ $\left.1 \mid X_{D}=b\right]=\operatorname{Pr}_{Q}\left[X_{i}=1 \mid X_{S}=b_{S}\right]$ for all configurations $b$ of $D$. Then for any configuration $a$ of $S^{\prime} \stackrel{\text { def }}{=} S \cup\{j\}$, we have

$$
\begin{aligned}
\operatorname{Pr}_{P}\left[X_{j}=1 \mid X_{S^{\prime}}=a\right] & =\sum_{b: b_{S}=a} \operatorname{Pr}_{P}\left[X_{j}=1 \mid X_{D}=b\right] \operatorname{Pr}_{P}\left[X_{D}=b \mid X_{S^{\prime}}=a\right] \\
& =\operatorname{Pr}_{P}\left[X_{j}=1 \mid X_{S}=a_{S}\right] \sum_{b: b_{S}=a} \operatorname{Pr}_{P}\left[X_{D}=b \mid X_{S^{\prime}}=a\right] \\
& =\operatorname{Pr}_{P}\left[X_{j}=1 \mid X_{S}=a_{S}\right]
\end{aligned}
$$

concluding the proof.
Suppose for a contradiction that $(i, j)$ is an edge in the skeleton of $\mathcal{S}$ but not in $\mathcal{S}^{\prime}$. Without loss of generality, we may assume that $X_{j}$ is not a descendant of $X_{i}$ in $\mathcal{S}^{\prime}$ (since otherwise we can swap the roles of $i$ and $j$ in the argument). Then as $X_{i}$ is not in $S$, the set of parents of $X_{j}$ in $\mathcal{S}^{\prime}$, either, by Claim $13 X_{i}$ and $X_{j}$ are independent conditioned on $X_{S}$. However since one of $X_{i}$ and $X_{j}$ is a parent of the other in $\mathcal{S}$, condition (i) of $\gamma$-non-degeneracy gives that $X_{i}$ and $X_{j}$ are $\gamma$-far from independent conditioned on $X_{S}$. This is a contradiction, so all edges in the skeleton of $\mathcal{S}$ must be edges of $\mathcal{S}^{\prime}$. But by assumption $\mathcal{S}^{\prime}$ has no more edges than $\mathcal{S}$, and so they have the same skeleton.

Next we show that $i$ and $j$ have the same $\vee$-structures. Assume by contradiction that $(i, j, k)$ is a $\vee$-structure in $\mathcal{S}$ but not $\mathcal{S}^{\prime}$. Since $\mathcal{S}$ and $\mathcal{S}^{\prime}$ have the same skeleton, this cannot be because $X_{i}$ is the parent of $X_{j}$ or vice versa. Therefore, must be that at least one of $X_{i}$ or $X_{j}$ is the child of $X_{k}$ rather than its parent in $\mathcal{S}^{\prime}$. As before, without loss of generality we may assume that $X_{j}$ is not a descendant of $X_{i}$ in $\mathcal{S}^{\prime}$. This implies that $X_{k}$ cannot be a child of $X_{i}$, since then $X_{j}$ must be a child of $X_{k}$ and so a descendant of $X_{i}$. Thus $S$, the set of parents of $X_{i}$ in $\mathcal{S}^{\prime}$, contains $X_{k}$ but not $X_{j}$; and Claim 13 then implies that $X_{i}$ and $X_{j}$ are independent conditioned on $X_{S}$. However, in $\mathcal{S} X_{k}$ is the child of both $X_{i}$ and $X_{j}$ and so by condition (ii) of $\gamma$-non-degeneracy, we have that $X_{i}$ and $X_{j}$ are $\gamma$-far from independent conditioned on $X_{S}$. This contradiction shows that all $\vee$-structures in $\mathcal{S}$ are $\vee$-structures in $\mathcal{S}^{\prime}$ as well.

Finally, we assume for the sake of contradiction that $(i, j, k)$ is a $\vee$-structure in $\mathcal{S}^{\prime}$ but not $\mathcal{S}$. Again without loss of generality, we assume that $X_{j}$ is not a descendant of $X_{i}$ in $\mathcal{S}^{\prime}$; and let $S$ be the parents of $X_{i}$ in $\mathcal{S}^{\prime}$. Note that neither $X_{k}$ nor $X_{j}$ is in $S$ since this is a $\vee$-structure. Now by Claim $13, X_{i}$ and $X_{j}$ are independent conditioned on $X_{S}$. In $\mathcal{S}$, however, $(i, j, k)$ is not a $\vee$-structure yet $(i, k),(j, k)$ (but not $(i, j)$ ) are in the skeleton of $\mathcal{S}$. Thus at least one of $X_{i}$, $X_{j}$ is a child of $X_{k}$. If only one is a child, then the other must be $X_{k}$ 's parent. In the case of

two children, we apply condition (iv) and in the case of a parent and a child, we apply condition (iii) of $\gamma$-non-degeneracy. Either way, we obtain that, since $X_{k}$ is not in $S, X_{i}$ and $X_{j}$ are $\gamma$-far from independent conditioned on $X_{S}$. This contradiction shows that all $\vee$-structures in $\mathcal{S}^{\prime}$ are also $\vee$-structures in $\mathcal{S}$.

We thus have all the conditions for Lemma 25 to apply and conclude that $\mathcal{S}$ and $\mathcal{S}^{\prime}$ are $I$ equivalent.

Conditional Independence Tester We now turn to establishing the following proposition:
Proposition 1. There exists an algorithm that, given parameters $\gamma, \tau>0$, set of coordinates $S \subseteq$ $[n]$ and coordinates $i, j \in[n] \backslash S$, as well as sample access to a distribution $P$ over $\{0,1\}^{n}$, satisfies the following. With probability at least $1-\tau$, the algorithm accepts when $X_{i}$ and $X_{j}$ are independent conditioned on $X_{S}$ and rejects when no distribution $Q$ with $d_{\mathrm{TV}}(P, Q)<\gamma$ has this property (and may do either if neither cases holds). Further, the algorithm takes $O\left(\left(2^{d}+\log (1 / \tau)\right) / \gamma^{2}\right)$ samples from $P$ and runs in time $O\left(\left(2^{d}+\log (1 / \tau)\right) / \gamma^{2}\right)$.

Input $\gamma, \tau>0, i, j \in\{0,1\}^{n}, S \subseteq\{0,1\}^{n}$ with $i, j \notin S$, and sample access to a distribution $P$ on $\{0,1\}^{n}$.

- Take $O\left(\left(2^{d}+\log (1 / \tau)\right) / \gamma^{2}\right)$ samples from $P$. Let $\tilde{P}$ be the resulting empirical distribution.

For each configuration $a \in\{0,1\}^{|S|}$ of $S$,

- Compute the empirical conditional means $\mu_{i, a}=\mathbb{E}_{X \sim \tilde{P}}\left[X_{i} \mid X_{S}=a\right]$ and $\mu_{j, a}=\mathbb{E}_{X \sim \tilde{P}}\left[X_{j} \mid\right.$ $\left.X_{S}=a\right]$.
- Compute the conditional covariance $\operatorname{Cov}_{\tilde{P}}\left[X_{i}, X_{j} \mid X_{S}=a\right]=\mathbb{E}_{X \sim \tilde{P}}\left[\left(X_{i}-\mu_{i, a}\right)\left(X_{j}-\mu_{j, a}\right) \mid\right.$ $\left.X_{S}=a\right]$.

Compute the expected absolute value of the conditional covariance $\beta=\mathbb{E}_{Y \sim \tilde{P}}\left[\left|\operatorname{Cov}_{\tilde{P}}\left[X_{i}, X_{j} \mid X_{S}=\right.\right.\right.$ $\left.\left.Y_{S}\right]\right|\right]$.

If $\beta \leq \gamma / 3$, return accept
Else return reject.

Figure 5: Testing whether $X_{i}$ and $X_{j}$ are independent conditioned on $S$ or are $\gamma$-far from being so.

Proof. The algorithm is given in Fig. 5. Its sample complexity is immediate, and that the algorithm takes linear time in the number of samples is not hard to see. It remains to prove correctness.

To do so, define $D \stackrel{\text { def }}{=} S \cup\{i, j\}$. Let $P_{D}, \tilde{P}_{D}$ be the distributions of $X_{S}$ for $X$ distributed as $P, \tilde{P}$ respectively. Since $P_{D}$ is a discrete distribution with support size $2^{d+2}$, by standard results the empirical $\tilde{P}_{D}$ obtained from our $O\left(\left(2^{d+2}+\log 1 / \tau\right) / \gamma^{2}\right)$ samples is such that $d_{\mathrm{TV}}\left(P_{D}, \tilde{P}\right) \leq \gamma / 10$ with probability at least $1-\tau$. We hereafter assume that this holds.

Note that the distribution $P_{D}$ determines whether $P$ is such that $X_{i}$ and $X_{j}$ are independent conditioned on $S$ or is $\delta$-far from being so for any $\delta$. Thus if these two nodes are $\gamma$-far from being conditionally independent in $P$, then they are $\gamma$-far in $P_{D}$ and therefore are $9 \gamma / 10$-far in

$\tilde{P}_{D}$. We now need to show that the expected absolute value of the conditional covariance is a good approximation of the distance from conditional independence, which is our next claim:
Claim 14. For a distribution $Q$ on $\{0,1\}^{n}$, let $\gamma$ be the minimum $\gamma>0$ such that $X_{i}$ and $X_{j}$ are $\gamma$-far from independent conditioned on $X_{S}$ in $Q$. Let $\beta=\mathbb{E}_{Y \sim Q}\left[\left|\operatorname{Cov}_{Q}\left[X_{i}, X_{j} \mid X_{S}=Y_{S}\right]\right|\right]$. Then we have $\beta / 3 \leq \gamma \leq 2 \beta$.

Proof. For simplicity, we assume that $|D|=n$ and that we have only coordinates $i, j$ and $S$.
Firstly, we show that $\beta \leq \gamma$. By assumption, there is a distribution $R$ with $d_{\mathrm{TV}}(Q, R)=\gamma$ which has that $X_{i}$ and $X_{j}$ are independent conditioned on $X_{S}$. Thus $R$ has $\left|\operatorname{Cov}_{R}\left[X_{i}, X_{j} \mid X_{S}=a\right]\right|=0$ for all configurations $a$. Since $0 \leq\left|\operatorname{Cov}_{Q}\left[X_{i}, X_{j} \mid X_{S}=a\right]\right| \leq 1$, it follows that $\left|\beta-\mathbb{E}_{Y \sim R}\right|\left|\operatorname{Cov}_{Q}\left[X_{i}, X_{j} \mid\right.\right.$ $\left.\left.X_{S}=Y_{S}\right]\right||\mid \leq 3 d_{\mathrm{TV}}(Q, R)$ as $\operatorname{Cov}_{Q}\left[X_{i}, X_{j} \mid X_{S}=Y_{S}\right]=\mathbb{E}\left[X_{i} X_{j} \mid X_{S}=Y_{S}\right]-\mathbb{E}\left[X_{i} \mid X_{S}=\right.$ $\left.Y_{S}\right] \mathbb{E}\left[X_{j} \mid X_{S}=Y_{S}\right]$ and so $\beta \leq 3 \gamma$.

Next we need to show that $\beta \leq 2 \gamma$. To show this, we construct a distribution $S$ on $\{0,1\}^{n}$ with $d_{\mathrm{TV}}(Q, S)=2 \beta$ in which $X_{i}$ and $X_{j}$ are independent conditioned on $X_{S}$. Explicitly, for a configuration $a$ of $S$ and $b, c \in\{0,1\}$, we set
$\operatorname{Pr}_{S}\left[X_{S}=a, X_{i}=b, X_{j}=c\right] \stackrel{\text { def }}{=} \operatorname{Pr}_{Q}\left[X_{S}=a, X_{i}=b, X_{j}=c\right]+(-1)^{b+c} \operatorname{Cov}_{Q}\left[X_{i}, X_{j} \mid X_{S}=a\right] \operatorname{Pr}_{Q}\left[X_{S}=a\right]$.
For each configuration $a$, this increases two probabilities by $\left|\operatorname{Cov}_{Q}\left[X_{i}, X_{j} \mid X_{S}=a\right]\right| \operatorname{Pr}_{Q}\left[X_{S}=a\right]$ and decrease two probabilities by the same amount. Thus, provided that all probabilities are still non-negative (which we show below), $S$ is a distribution with $d_{\mathrm{TV}}(Q, S)=\sum_{a} 2\left|\operatorname{Cov}_{Q}\left[X_{i}, X_{j} \mid\right.\right.$ $\left.\left.X_{S}=a\right]\right| \operatorname{Pr}_{Q}\left[X_{S}=a\right]=2 \beta$.

Now consider the conditional joint distribution of $X_{i}, X_{j}$ for a given $a$. Let $p_{b, c} \stackrel{\text { def }}{=} \operatorname{Pr}_{Q}\left[X_{i}=\right.$ $\left.b, X_{j}=c \mid X_{S}=a\right]$. Then the conditional covariance $\operatorname{Cov}_{Q}\left[X_{i}, X_{j} \mid X_{S}=a\right]$, which we denote by $\alpha$ for simplicity here, is

$$
\begin{aligned}
\alpha & =\mathbb{E}\left[X_{i} X_{j} \mid X_{S}=a\right]-\mathbb{E}\left[X_{i} \mid X_{S}=a\right] \mathbb{E}\left[X_{j} \mid X_{S}=a\right] \\
& =p_{1,1}-\left(p_{1,0}+p_{1,1}\right)\left(p_{0,1}+p_{1,1}\right) \\
& =p_{1,1}\left(1-p_{1,0}-p_{0,1}-p_{1,1}\right)-p_{1,0} p_{0,1} \\
& =p_{1,1} p_{0,0}-p_{1,0} p_{0,1}
\end{aligned}
$$

In $S$, these probabilities change by $\alpha . p_{1,1}$ and $p_{0,0}$ are increased by $\alpha$ and $p_{0,1}$ and $p_{1,0}$ are decreased by it. Note that if $\alpha>0, p_{1,1}$ and $p_{0,0}$ are at least $p_{1,1} p_{0,0} \geq \alpha$ and when $\alpha<0, p_{0,1}$ and $p_{1,0}$ are at least $p_{1,0} p_{0,1} \geq-\alpha$. Thus all probabilities in $S$ are in $[0,1]$, as claimed.

A similar expression for the conditional covariance in $S$ to that for $\alpha$ above yields

$$
\begin{aligned}
\operatorname{Cov}_{S} & {\left[X_{i}, X_{j} \mid X_{S}=a\right] } \\
& =\left(p_{1,1}-\alpha\right)\left(p_{0,0}-\alpha\right)-\left(p_{1,0}+\alpha\right)\left(p_{0,1}+\alpha\right) \\
& =-\left(p_{0,0}+p_{1,1}+p_{0,1}+p_{1,0}\right) \alpha+p_{1,1} p_{0,0}-p_{1,0} p_{0,1} \\
& =p_{1,1} p_{0,0}-p_{1,0} p_{0,1}-\alpha=0
\end{aligned}
$$

Since $X_{i}$ and $X_{j}$ are Bernoulli random variables, the conditional covariance being zero implies that they are conditionally independent.

Completeness. Suppose by contrapositive that the algorithm rejects. Claim 14 implies that in $\tilde{P}$, $X_{i}$ and $X_{j}$ are $\gamma / 9$-far from independent conditioned on $X_{S}$. Thus they are $\gamma / 9$ far in $\tilde{P}_{D}$ and, since $d_{\mathrm{T} V}\left(P_{D}, \tilde{P}_{D}\right) \leq \gamma / 10$, this implies that they are not conditionally independent in $P_{D}$. Thus, in $P, X_{i}$ and $X_{j}$ are not independent conditioned on $X_{S}$.

Soundness. Now suppose that $X_{i}$ and $X_{j}$ are $\gamma$-far from independent conditioned on $X_{S}$ in $P$. Per the foregoing discussion, this implies that they are $(9 \gamma / 10)$-far from being so in $\tilde{P}_{D}$. Now Claim 14 guarantees that $\mathbb{E}_{Y \sim \tilde{P}}\left[\left|\operatorname{Cov}_{\tilde{P}}\left[X_{i}, X_{j} \mid X_{S}=Y_{S}\right]\right|\right] \leq 9 \gamma / 20>\gamma / 3$, and therefore the algorithm rejects in this case. This completes the proof of correctness.

Structure Tester Finally, we turn to the proof of Theorem 18, analyzing the structure testing algorithm described in Fig. 6.

Input $\gamma>0$, a structure $\mathcal{S}$ and a Bayesian network $P$

- Draw $O\left(\left(2^{d}+d \log n\right) / \gamma^{2}\right)$ samples from $P$. Call this set of samples $S$.

For each nodes $X_{i}, X_{j}$ and set $S$ of nodes with $|S| \leq d$ and $i, j \neq S$
If one of the following conditions holds in structure $\mathcal{S}$
(i) $X_{i}$ is the parent of $X_{j}$,
(ii) $S$ contains a node $X_{k}$ that is a child of both $X_{j}$ and $X_{j}$,
(iii) $X_{i}$ is a grandparent of $X_{j}$ and there is a child of $X_{i}$ and parent of $X_{j}, X_{k}$ that is not in $S$,
(iv) $X_{i}$ and $X_{j}$ have a common parent $X_{k}$ that is not in $S$

Then run the conditional independence tester of Proposition 1 (Fig. 5) using the set of samples $S$ to test whether $X_{i}$ and $X_{j}$ are independent conditioned on $X_{S}$.
If the conditional independence tester accepts, return reject.
Otherwise return accept.

Figure 6: Testing whether $P$ has structure as $\mathcal{S}$

Proof of Theorem 18. We first show correctness. There are at most $n^{d+2}$ possible choices of $X_{i}, X_{j}$ and $|S|$ and thus we run the conditional independence tester at most $n^{d+2}$ times. With $O\left(\left(2^{d}+\right.\right.$ $\left.d \log n) / \gamma^{2}\right)$ samples, each test gives an incorrect answer with probability no more than $\tau=n^{-\Omega(d)}$. With appropriate choice of constants we therefore have that all conditional independence tests are correct with probability $99 / 100$. We henceforth condition on this, i.e., that all such tests are correct.

Completeness. If $P$ is $\gamma$-non-degenerate with respect to structure $\mathcal{S}$ and degree $d$, then by the definition of non-degeneracy, for any $X_{i}, X_{j}$ and $S$ that satisfy one of conditions (i)-(iv) we have that $X_{i}$ and $X_{j}$ are $\gamma$-far from independent conditioned on $X_{S}$. Thus every conditional independence test rejects and the algorithm accepts.

Soundness. Now suppose by contrapositive that the algorithm accepts. For any $X_{i}, X_{j}$, and $S$ that satisfy one of conditions (i)-(iv), the conditional independence test must have rejected, that is any such $X_{i}$ and $X_{j}$ are not independent conditioned on such an $X_{S}$. Let $\gamma^{\prime}$ be the mimuimum over all $X_{i}, X_{j}$, and $S$ that satisfy one of conditions (i)-(iv) and distributions $Q$ over $\{0,1\}$ such that $X_{i}$ and $X_{j}$ are independent conditioned on $X_{S}$ in $Q$, of the total variation distance between $P$ and $Q$. Since there are only finitely many such combinations of $X_{i}, X_{j}$, and $S$, this $\gamma^{\prime}$ is positive. Thus $P$ is $\gamma^{\prime}$-non-degenerate with respect to $\mathcal{S}$ and $d$. Since we assumed that $P$ has a structure $\mathcal{S}^{\prime}$ with degree at most $d$ and whose skeleton has no more edges than that of $\mathcal{S}$, we can apply Lemma 26, which yields that $\mathcal{S}$ and $\mathcal{S}^{\prime}$ are $I$-equivalent. Thus $P$ can indeed be expressed as a Bayesian network with structure $\mathcal{S}$. This completes the proof of correctness.

To conclude, observe that we run the loop at most $n^{d+2}$ times, each using time at most $O\left(\left(2^{d}+\right.\right.$ $d \log n) / \gamma^{2}$ ). The total running time is thus $O\left(n^{d+3} / \gamma^{2}\right)$.

# 9 Testing Closeness of Bayes Nets 

### 9.1 Fixed Structure Bayes Nets

We now establish the upper bound part of Theorem 1 for closeness, namely testing closeness between two unknown Bayes nets with the same (known) underlying structure.

Theorem 19. There exists a computationally efficient algorithm with the following guarantees. Given as input (i) a DAG $\mathcal{S}$ with $n$ nodes and maximum in-degree d, (ii) a parameter $\epsilon>0$, and (iii) sample access to two unknown $(c, C)$-balanced Bayes nets $P, Q$ with structure $\mathcal{S}$, where $c=\tilde{\Omega}(1 / \sqrt{n})$ and $C=\tilde{\Omega}\left(d \epsilon^{2} / \sqrt{n}\right)$; the algorithm takes $O\left(2^{d / 2} \sqrt{n} / \epsilon^{2}\right)$ samples from $P$ and $Q$, and distinguishes with probability at least $2 / 3$ between the cases $P=Q$ and $\|P-Q\|_{1}>\epsilon$.

Proof. We choose $m \geq \alpha \frac{2^{d / 2} \sqrt{n}}{\epsilon^{2}}$, where $\alpha>0$ is an absolute constant to be determined in the course of the analysis. Let $\mathcal{S}$ and $P, Q$ be as in the statement of the theorem, for $c \geq \beta \frac{\log n}{\sqrt{n}} \geq \beta \frac{\log n}{m}$ and $C \geq \beta \frac{d+\log n}{m}$, for some other absolute constant $\beta>0$.

The algorithm proceeds as follows: first, taking $m$ samples from both $P$ and $Q$, it computes for each parental configuration $(i, a) \in[n] \times\{0,1\}^{d}$ the number of times $\hat{N}_{i, a}$ and $\hat{M}_{i, a}$ this configuration was observed among the samples, for respectively $P$ and $Q$. If for any $(i, a)$ it is the case that $\hat{N}_{i, a}$ and $\hat{M}_{i, a}$ are not within a factor 4 of each other, the algorithm returns reject. (Using the same number of samples, it also estimates $p_{i, a}$ and $q_{i, a}$ within an additive $1 / 3$, and applies the same standard transformation as before so that we can hereafter assume $p_{i, a}, q_{i, a} \leq 2 / 3$ for all $(i, a)$.)

Note that $\mathbb{E}\left[\hat{N}_{i, a}\right]=m \operatorname{Pr}_{P}\left[\Pi_{i, a}\right]$ and $\mathbb{E}\left[\hat{M}_{i, a}\right]=m \operatorname{Pr}_{Q}\left[\Pi_{i, a}\right]$; given the $C$-balancedness assumption and by Chernoff and union bounds, with probability at least $9 / 10$ we have that $\hat{N}_{i, a}$ and $\hat{M}_{i, a}$ are within a factor 2 of their expectation simultaneously for all $n 2^{d}$ parental configurations. We hereafter condition on this (and observe that this implies that if $P=Q$, then the algorithm rejects in the step above with probability at most $1 / 10$ ).

The algorithm now draws independently $n 2^{d}$ values $\left(M_{i, a}\right)_{(i, a)}$, where $M_{i, a} \sim \operatorname{Poi}\left(\hat{N}_{i, a}\right)$; and takes fresh samples from $P, Q$ until it obtains $M_{i, a}$ samples for each parental configuration $\Pi_{i, a}$ (for

each of the two distributions). If at any point the algorithm takes more than 10 m samples, it stops and returns reject.
(Again, note that by concentration (this time of Poisson random variables) ${ }^{3}$, our assumption that $\hat{N}_{i, a} \geq m \operatorname{Pr}_{P}\left[\Pi_{i, a}\right] / 2 \geq m C / 2=\beta(d+\log n)$ and a union bound, the algorithm will reject at this stage with probability at most $1 / 10$.)

Conditioning on not having rejected, we define for each parental configuration $\Pi_{i, a}$ the quantity $U_{i, a}$ (resp. $V_{i, a}$ ) as the number of samples from $P$ (resp. $Q$ ) among the first $M_{i, a}$ satisfying $\Pi_{i, a}$ for which $X_{i}=1$. In particular, this implies that $U_{i, a} \sim \operatorname{Poi}\left(p_{i, a} \hat{N}_{i, a}\right), V_{i, a} \sim \operatorname{Poi}\left(q_{i, a} \hat{N}_{i, a}\right)$ (and are independent), and that the random variables $W_{i, a}$ defined below:

$$
W_{i, a} \stackrel{\text { def }}{=} \frac{\left(U_{i, a}-V_{i, a}\right)^{2}-\left(U_{i, a}+V_{i, a}\right)}{U_{i, a}+V_{i, a}}
$$

are independent. We then consider the statistic $W$ :

$$
W \stackrel{\text { def }}{=} \sum_{i=1}^{n} \sum_{a \in\{0,1\}^{d}} W_{i, a}
$$

Claim 15. If $P=Q$, then $\mathbb{E}[W]=0$. Moreover, if $\|P-Q\|_{1}>\epsilon$ then $\mathbb{E}[W]>\frac{m \epsilon^{2}}{144}$.
Proof. We start by analyzing the expectation of $W_{i, a}$, for any fixed $(i, a) \in[n] \times\{0,1\}^{d}$. The same argument as Claim 15 leads to conclude that $\mathbb{E}\left[W_{i, a}\right]=0$ if $P=Q$ (proving the first part of the claim), and that otherwise we have

$$
\begin{aligned}
\mathbb{E}\left[W_{i, a}\right] & \geq \frac{\min (1, m c)}{3} \hat{N}_{i, a} \frac{\left(p_{i, a}-q_{i, a}\right)^{2}}{p_{i, a}+q_{i, a}} \\
& =\frac{1}{3} \hat{N}_{i, a} \frac{\left(p_{i, a}-q_{i, a}\right)^{2}}{p_{i, a}+q_{i, a}} \\
& \geq \frac{2}{9} \hat{N}_{i, a} \frac{\left(p_{i, a}-q_{i, a}\right)^{2}}{\left(p_{i, a}+q_{i, a}\right)\left(2-p_{i, a}-q_{i, a}\right)}
\end{aligned}
$$

(since $m c \geq \beta \log n \gg 1$ and $0<p_{i, a}, q_{i, a} \leq 2 / 3$ ). Summing over all $(i, a)$ 's and recalling that $\hat{N}_{i, a} \geq m \operatorname{Pr}_{P}\left[\Pi_{i, a}\right] / 2, \hat{N}_{i, a} \geq m \operatorname{Pr}_{Q}\left[\Pi_{i, a}\right] / 2$ yields the bound:

$$
\begin{aligned}
\mathbb{E}[W] & \geq \frac{m}{9} \sum_{(i, a)} \frac{\sqrt{\operatorname{Pr}_{P}\left[\Pi_{i, a}\right] \operatorname{Pr}_{Q}\left[\Pi_{i, a}\right]}\left(p_{i, a}-q_{i, a}\right)^{2}}{\left(p_{i, a}+q_{i, a}\right)\left(2-p_{i, a}-q_{i, a}\right)} \\
& \geq \frac{m}{18} \mathrm{~d}_{\mathrm{H}}(P, Q)^{2} \geq \frac{m}{18}\left(1-\sqrt{1-\frac{1}{4}\|P-Q\|_{1}^{2}}\right)
\end{aligned}
$$

(where we relied on Lemma 4 for the second-to-last inequality). This gives the last part of the claim, as the RHS is at least $\frac{m \epsilon^{2}}{144}$ whenever $\|P-Q\|_{1}^{2}>\epsilon^{2}$.

We now bound the variance of our estimator:

[^0]
[^0]:    ${ }^{3}$ Specifically, if $X \sim \operatorname{Poi}(\lambda)$ then we have $\operatorname{Pr}[|X-\lambda|>\lambda / 2]=e^{-\Omega(\lambda)}$.

Claim 16. $\operatorname{Var}[W] \leq n 2^{d+1}+5 \sum_{(i, a)} \hat{N}_{i, a} \frac{\left(p_{i, a}-q_{i, a}\right)^{2}}{p_{i, a}+q_{i, a}}=O\left(n 2^{d}+\mathbb{E}[W]\right)$. In particular, if $P=Q$ then $\operatorname{Var}[W] \leq n 2^{d+1}$.

Proof. We follow the proof of Claim 8 to analyze the variance of $W_{i, a}$, obtaining a bound of $\operatorname{Var}\left[W_{i, a}\right] \leq 2+5 \hat{N}_{i, a} \frac{\left(p_{i, a}-q_{i, a}\right)^{2}}{p_{i, a}+q_{i, a}}$. Invoking Eq. (9) and summing over all $(i, a) \in[n] \times\{0,1\}^{d}$ then lead to the desired conclusion.

The correctness of our algorithm will then follow for the two claims above:
Lemma 27. Set $\tau \stackrel{\text { def }}{=} \frac{\epsilon^{2}}{288}$. Then we have the following:

- If $\|P-Q\|_{1}=0$, then $\operatorname{Pr}[W \geq \tau a m] \leq \frac{1}{10}$.
- If $\|P-Q\|_{1}>\epsilon$, then $\operatorname{Pr}[W<\tau m] \leq \frac{1}{10}$.

Proof. We start with the soundness case,i.e. assuming $\|P-Q\|_{1}>\epsilon$, which by Claim 15 implies $\mathbb{E}[W]>2 \tau$. Then, by Chebyshev's inequality,

$$
\begin{aligned}
\operatorname{Pr}[W<\tau m] & \leq \operatorname{Pr}\left[\mathbb{E}[W]-W>\frac{1}{2} \mathbb{E}[W]\right] \leq \frac{4 \operatorname{Var}[W]}{\mathbb{E}[W]^{2}} \\
& \leq \frac{8 n 2^{d}}{\mathbb{E}[W]^{2}}+\frac{12}{5 \mathbb{E}[W]} \\
& =O\left(\frac{n 2^{d}}{\epsilon^{4} m^{2}}+\frac{1}{m \epsilon^{2}}\right)
\end{aligned}
$$

We want to bound this quantity by $1 / 10$, for which it is enough to have $\frac{n 2^{d}}{\epsilon^{4} m^{2}} \ll 1$ and $\frac{1}{m \epsilon^{2}} \ll 1$, which both hold for an appropriate choice of the absolute constant $\alpha>0$ in our setting of $m$.

Turning to the completeness, we suppose $\|P-Q\|_{1}=0$. Then, by Chebyshev's inequality, and invoking Claim 16,

$$
\begin{aligned}
\operatorname{Pr}[W \geq \tau m] & =\operatorname{Pr}[W \geq \mathbb{E}[W]+\tau m] \leq \frac{\operatorname{Var}[W]}{\tau^{2} m^{2}} \\
& =O\left(\frac{n 2^{d}}{\epsilon^{4} m^{2}}\right)
\end{aligned}
$$

which is no more than $1 / 10$ for the same choice of $m$.
Combining all the elements above concludes the proof, as by a union bound the algorithm is correct with probability at least $1-\left(\frac{1}{10}+\frac{1}{10}+\frac{1}{10}\right)>\frac{2}{3}$.

# 9.2 Unknown Structure Bayes Nets 

As for the case identity testing, we give a closeness tester for balanced non-degenerate Bayes Nets. An additional assumption that we require is that the ordering of the nodes in the corresponding DAGs is known to the algorithm. Formally, we show:

Theorem 20. There exists a computationally efficient algorithm with the following guarantees. Given as input (i) a parameter $\epsilon>0$, (ii) an ordering of nodes $\pi$, and (ii) sample access to unknown $\gamma$-non-degenerate, $(c, C)$-balanced Bayes nets $P, Q$ such the structures of $P$ and $Q$ give the same ordering $\pi$ to nodes, where $c=\tilde{\Omega}(1 / \sqrt{n})$ and $C=\tilde{\Omega}\left(d \epsilon^{2} / \sqrt{n}\right)$; the algorithm takes $N=O\left(2^{d / 2} \sqrt{n} / \epsilon^{2}+2^{d} / \gamma^{2}+d \log (n) / \gamma^{2}\right)$ samples from $P$ and $Q$, runs in time $n^{d} \operatorname{poly}(N)$, and distinguishes with probability at least $2 / 3$ between the cases $P=Q$ and $\|P-Q\|_{1}>\epsilon$.

Proof. The argument's idea is the following: we first test that $P$ and $Q$ have the same skeleton. Since they have the same ordering, that suffices to show that they have the same structure. If this is the case, then we use our known-structure tester.

In more detail, given the $\gamma$-non-degeneracy assumption, for each pair of coordinates $i, j$ and set of coordinates $S$ with $|S| \leq d$, we can, using the conditional independence tester from Proposition 1, test whether each of $P$ and $Q$ has $X_{i}$ and $X_{j}$ conditionally independent on $X_{S}$ or $\gamma$-far from it with $n^{-d-2} / 100$ probability of error in $O\left(\left(2^{d}+d \log (n)\right) / \gamma^{2}\right)$ samples. Running tests on the same samples for all $n^{d+2}$ combinations of $i, j, S$, we can with probability at least $99 / 100$ correctly classify which of the two cases holds, for all $i, j, S$ that are either conditionally independent or $\gamma$-far. We note that by non-degeneracy, there is an edge between $i$ and $j$ in the structure defining $P$ only if $X_{i}$ and $X_{j}$ are $\gamma$-far from independent conditioned on $X_{S}$ for all $S$ (i.e., if there is no edge then there must exist a $S$ such that $X_{i}$ and $X_{j}$ are conditionally independent on $X_{S}$ ). Therefore, assuming our conditional independence testers all answered as they should, we can use this to successfully identify the set of edges in the structure of $P$ (and thus, since we know the ordering, the entire structure).

Having determined the underlying structures of $P$ and $Q$, our tester rejects if these structures differ (as using Lemma 26, $\gamma$-non-degeneracy implies that neither can equal a Bayes net with nonequivalent structure and fewer edges). Otherwise, we run the tester from Theorem 19 (since we satisfy its assumptions) and return the result.

# 10 Identity and Closeness Testing for High-Degree Bayes Nets 

Finally, in this section we give testing algorithms for identity and closeness of degree- $d$ Bayes nets with unknown structure, without balancedness assumptions. Compared to the testing algorithm of Theorem 4 and Theorem 20 (which work under such assumptions) the dependence on the number of nodes $n$ the testers in this section are suboptimal, they achieve the "right" dependence on the degree $d$ (specifically, $2^{d / 2}$ for identity and $2^{2 d / 3}$ for closeness). Hence, these testers achieve sublearning sample complexity for the case that $d=\Omega(\log n)$.

Theorem 21. There exists two algorithms with the following guarantees:

- (Identity) Given the full description of a Bayes net $Q$ of degree at most d, parameter $\epsilon \in(0,1]$, and sample access to a distribution $P$ promised to be a Bayes net (i) of degree at most d and (ii) such that the structures of $P$ and $Q$ give the same ordering to nodes, the first takes $N=$ $2^{d / 2} \operatorname{poly}(n / \epsilon)$ samples from $P$, runs in time $n^{d} \operatorname{poly}(N)$, and distinguishes with probability at least $2 / 3$ between (i) $P=Q$ and (ii) $\|P-Q\|_{1}>\epsilon$.
- (Closeness) Given parameter $\epsilon \in(0,1]$, and sample access to two distributions $P, Q$ promised to be Bayes nets (i) of degree at most d and (ii) such that the structures of $P$ and $Q$ give the same ordering to nodes, the second takes $N=2^{2 d / 3} \operatorname{poly}(n / \epsilon)$ samples from $P$ and $Q$, runs

in time $n^{d} \operatorname{poly}(N)$, and distinguishes with probability at least $2 / 3$ between (i) $P=Q$ and (ii) $\|P-Q\|_{1}>\epsilon$.

Proof. We first establish the first part of the theorem, namely the existence of an identity testing algorithm with optimal dependence on the degree $d$. The algorithm is quite simple: it goes over each set $S \subseteq[n]$ of at most $d+1$ coordinates, and checks that for each of them it holds that the conditional distributions $P, S, Q_{S}$ are equal (versus $\left\|P_{S}-Q_{S}\right\|_{1}>\operatorname{poly}\left(\frac{\epsilon}{n}\right)$ ).

Since $P_{S}$ and $Q_{S}$ are supported on sets of size $O\left(2^{d}\right)$, and as there are only $O\left(n^{d+1}\right)$ such sets to consider, the claimed sample complexity suffices to run all tests correctly with probability $9 / 10$ overall (by a union bound).

The more difficult part is to argue correctness, that is to show that if the test accepts then one must have $\|P-Q\|_{1}<\epsilon$. To do so, assume (without loss of generality) that $H(P) \leq H(Q)$ : we will show that $\mathrm{D}(P \| Q)$ is small, which implies that the $L_{1}$ distance is as well.

Let the ordering of $P$ be coordinates $1,2,3, \ldots$ We note that $\mathrm{D}(P \| Q)=\sum_{i} \mathrm{D}\left(P_{i} \| Q_{i}\right.$ $\left.P_{1}, \ldots, P_{i-1}\right)$ (i.e. the expectation over $P_{1}, \ldots, P_{i-1}$ of the KL-divergence of the conditional distributions of $P_{i}$ and $Q_{i}$, conditioned on these $(i-1)$ coordinates). It thus suffices to show that each of these terms is small.

Let $S_{i}$ be the set of parents of node $i$ under $P$. We have that:

$$
\mathrm{D}\left(P_{i}\left\|Q_{i}\right| P_{1}, \ldots, P_{i-1}\right)=\mathrm{D}\left(P_{i}\left\|Q_{i}\right| P_{S_{i}}\right)+\mathbb{E}_{P_{1}, \ldots, P_{i-1}}\left[\mathrm{D}\left(Q_{i} \mid P_{S_{i}}\left\|Q_{i}\right| P_{1}, \ldots, P_{i-1}\right)\right]
$$

Further, note that the fact that the tester accepted implies that $\mathrm{D}\left(P_{i}\left\|Q_{i}\right| P_{S_{i}}\right)$ is small. Now, we have that

$$
\begin{aligned}
H(P) & =\sum_{i} H\left(P_{i} \mid P_{1}, \ldots, P_{i-1}\right)=\sum_{i} H\left(P_{i} \mid P_{S_{i}}\right) \\
H(Q) & =\sum_{i} H\left(Q_{i} \mid Q_{1}, \ldots, Q_{i-1}\right) \\
& =\sum_{i} H\left(Q_{i} \mid Q_{S_{i}}\right)-I\left(Q_{i} ; Q_{1}, \ldots, Q_{i-1} \mid Q_{S_{i}}\right)
\end{aligned}
$$

But since the $(d+1)$-wise probabilities are close, we have that $H\left(P_{i} \mid P_{S_{i}}\right)$ is close to $H\left(Q_{i} \mid Q_{S_{i}}\right)$ (up to an additive poly $(\epsilon / n))$. Therefore, for each $i$, we have that $I\left(Q_{i} ; Q_{1}, \ldots, Q_{i-1} \mid Q_{S_{i}}\right)=\operatorname{poly}(\epsilon / n)$. In order to conclude, let us compare $I\left(Q_{i} ; Q_{1}, \ldots, Q_{i-1} \mid Q_{S_{i}}\right)$ and $\mathbb{E}_{P_{1}, \ldots, P_{i-1}}\left[\mathrm{D}\left(Q_{i} \mid P_{S_{i}}\left\|Q_{i}\right.\right.\right.$ $\left.\left.P_{1}, \ldots, P_{i-1}\right)\right]$. The former is the sum, over assignments $y \in\{0,1\}^{i-1}$ consistent with an assignment $x \in\{0,1\}^{S_{i}}$, of

$$
\operatorname{Pr}\left[Q_{S_{i}}=x\right] H\left(Q_{i} \mid Q_{S_{i}}=x\right)+\operatorname{Pr}\left[Q_{1, \ldots, i-1}=y\right] H\left(Q_{i} \mid Q_{1, \ldots, i-1}=y\right)
$$

The latter is the sum over the same $y$ 's of

$$
\operatorname{Pr}\left[P_{S_{i}}=x\right] H\left(Q_{i} \mid Q_{S_{i}}=x\right)+\operatorname{Pr}\left[P_{1, \ldots, i-1}=y\right] H\left(Q_{i} \mid Q_{1, \ldots, i-1}=y\right)
$$

But because of the $d$-way probability similarities, the terms $\operatorname{Pr}\left[P_{S_{i}}=x\right]$ and $\operatorname{Pr}\left[Q_{S_{i}}=x\right]$ terms are very close, within an additive poly $(\epsilon / n)$.
(Here we use the extra assumption that $P$ and $Q$ use the same ordering.) Denote by $T_{i}$ the parents of $i$ under the topology of $Q$. Then $H\left(Q_{i} \mid Q_{1, \ldots, i-1}=y\right)$ depends only on the values of the

coordinates in $T_{i}$. Thus the last part of the sum is a sum over $z$ of $\operatorname{Pr}\left[Q_{T_{i}}=z\right] H\left(Q_{i} \mid Q_{T_{i}}=z\right)$ and $\operatorname{Pr}\left[P_{T_{i}}=z\right] H\left(Q_{i} \mid Q_{T_{i}}=z\right)$, which are also close by a similar argument. Thus,

$$
\begin{aligned}
\mathbb{E}_{P_{1}, \ldots, P_{i-1}} & {\left[\mathrm{D}\left(Q_{i} \mid P_{S_{i}} \| Q_{i} \mid P_{1}, \ldots, P_{i-1}\right)\right] } \\
& =I\left(Q_{i} ; Q_{1}, \ldots, Q_{i-1} \mid Q_{S_{i}}\right)+\operatorname{poly}(\epsilon / n) \\
& =\operatorname{poly}(\epsilon / n)
\end{aligned}
$$

This implies that $P, Q$ are close in KL-divergence, and therefore in $L_{1}$.
The second part of the theorem, asserting the existence of a closeness testing algorithm with optimal dependence on $d$, will be very similar. Indeed, by the proof above it suffices to check that the restrictions of $P$ and $Q$ to any set of $(d+3)$-coordinates are $\operatorname{poly}(\epsilon / n)$-close. Using known results [CDVV14], this can be done for any specific collection of $d+3$ coordinates with $N$ samples in $\operatorname{poly}(N)$ time, and high probability of success, implying the second part of the theorem.

# A Sample Complexity of Learning Bayesian Networks 

In this section, we derive tight bounds on the sample complexity of learning Bayes nets. Recall that $n$ will denote the number of nodes and $d$ the maximum in-degree; before stating the results and providing their proofs, we outline the high-level idea of the argument.

If the structure is known, there is a very simple learning algorithm involving finding the empirical values for the relevant conditional probabilities and constructing the Bayes net using those terms. By computing the expected KL-Divergence between this hypothesis and the truth, we can show that it is possible to learn an $\epsilon$-aproximation in $\tilde{O}\left(2^{d} n / \epsilon^{2}\right)$ samples. Learning a Bayes net with unknown structure seems substantially more challenging, but at least the sample complexity is no greater. In particular, we can simply go over all possible topologies and come up with one hypothesis for each, and use a standard tournament to pick out the correct one. Appendix A. 1 contains the details of both.

We also prove in Appendix A. 2 a matching lower bound (up to logarithmic factors). For this we can even consider Bayesian networks of fixed topology. In particular, we consider the topology where each of the last $(n-d)$-coordinates depend on all of the first $d$ (which we can assume to be uniform and independent). The distribution we end up with is what we call a disjoint mixture of $2^{d}$ product distributions. In particular for each of the $2^{d}$ possible combinations of the first $d$ coordinates, we have a (potentially different) product distribution over the remaining coordinates. In order to learn our final distribution we must learn at least half of these product distributions to $O(\epsilon)$ error. This requires that we obtain at least $\Omega\left((n-d) / \epsilon^{2}\right)$ samples from $\Omega\left(2^{d}\right)$ of the parts of our mixture. Thus, learning will require $\Omega\left(2^{d}(n-d) / \epsilon^{2}\right)$ ) total samples.

## A. 1 Sample Complexity Upper Bound

Known Structure The algorithm will return a Bayes net $Q$ with the same (known) structure as the unknown $P$. Define $p_{i, a}$ as the probability (under $P$ ) that the $i$-th coordinate is 1 , conditioned on the parental configuration for $i$ being equal to $a$ (denoted $\Pi_{i, a}$ ); and $q_{i, a}$ the corresponding parameter for our hypothesis $Q$.

Given this, the algorithm is simple. We set $m=O\left(\frac{2^{d} n}{\epsilon^{2}} \log \left(2^{d} n\right)\right)$, and consider separately two sets of configurations $(i, a)$ :

- the light ones, for which $p_{i, a}\left(1-p_{i, a}\right) \operatorname{Pr}_{P}\left[\Pi_{i, a}\right] \leq \frac{\epsilon}{2 n 2^{d}}$;
- the heavy ones, for which $p_{i, a}\left(1-p_{i, a}\right) \operatorname{Pr}_{P}\left[\Pi_{i, a}\right]>\frac{\epsilon}{2 n 2^{d}}$.

We take $m$ samples from $P$, and let $q_{i, a}$ be the empirical conditional probabilities. For any $(i, a)$ for which we see less than $\tau \stackrel{\text { def }}{=} O((\log n) / \epsilon)$ samples, we set $q_{i, a}=0$. Note that with high probability, for the right choice of constant in the definition of $\tau$, for all heavy configurations simultaneously the estimate $q_{i, a}$ will (i) not be set to zero; and (ii) be such that $q_{i, a}\left(1-q_{i, a}\right)$ is within a factor 2 of the real value $p_{i, a}\left(1-p_{i, a}\right)$. Conversely, each light configuration will either have $q_{i, a}$ be zero, or $q_{i, a}\left(1-q_{i, a}\right)$ within a factor 2 of $p_{i, a}\left(1-p_{i, a}\right)$.

Conditioned on this happening, we can analyze the error. Note first that by our definition of light configuration and the triangle inequality, the sum of $L_{1}$ error over all light configurations will be at most $\epsilon / 2$. We now bound the contribution to the error of the heavy configurations. (In what follows, we implicitly restrict ourselves to these.)

By Pinsker's inequality, $\|P-Q\|_{1}^{2} \leq 2 \mathrm{D}(P \| Q) \leq \sum_{(i, a)} \operatorname{Pr}_{P}\left[\Pi_{i, a}\right] \frac{\left(p_{i, a}-q_{i, a}\right)^{2}}{q_{i, a}\left(1-q_{i, a}\right)}$. It only remains to bound the expected KL-divergence via the above bound. For each pair $(i, a)$, on expectation we see $m \operatorname{Pr}_{P}\left[\Pi_{i, a}\right]$ samples satisfying the parental configuration. The expected squared error $\left(p_{i, a}-q_{i, a}\right)^{2}$ between $p_{i, a}$ and our estimate $q_{i, a}$ is then $O\left(\frac{p_{i, a}\left(1-p_{i, a}\right)}{m \operatorname{Pr}_{P}\left[\Pi_{i, a}\right]}\right)$ by a standard variance argument. This implies that the expected KL-divergence is bounded as

$$
\mathbb{E}[\mathrm{D}(P \| Q)]=\frac{1}{m} \sum_{(i, a)} O\left(\mathbb{E}\left[\frac{p_{i, a}\left(1-p_{i, a}\right)}{q_{i, a}\left(1-q_{i, a}\right)}\right]\right)
$$

and it will be sufficient to argue that $\frac{p_{i, a}\left(1-p_{i, a}\right)}{q_{i, a}\left(1-q_{i, a}\right)}=O(1)$ with high probability (as then the RHS will be bounded as $O\left(\frac{2^{d} n}{m}\right)$, and thus taking $m=O\left(2^{d} n / \epsilon^{2}\right)$ will be sufficient). It is enough to show that, with high probability, $q_{i, a}\left(1-q_{i, a}\right)$ is within a factor 2 of $p_{i, a}\left(1-p_{i, a}\right)$ simultaneously for all $(i, a)$; but this is exactly the guarantee we had due to the "heaviness" of the configuration. Therefore, the contribution to the squared $L_{1}$ error from the heavy configuration is $O\left(\frac{2^{d} n}{m}\right)=O\left(\frac{\epsilon^{2}}{d+\log n}\right) \ll \epsilon^{2}$. Gathering the two sources of error, we get an $L_{1}$-error at most $\epsilon$ with high probability, as claimed.

Unknown Structure For this upper bound, we reduce to the previous case of known structure. Indeed, there are only $N=n^{O(d n)}$ possible max-degree- $d$ candidate structures: one can therefore run the above algorithm (with probability of failure $9 / 10$ ) for each candidate structure on a common sample from $P$ of size $O\left(2^{d} n / \epsilon^{2}\right)$, before running a tournament (cf. [DDS12b, DDS15]) to select a hypothesis with error $O(\epsilon)$ (which is guaranteed to exist as, with probability at least $9 / 10$, the "right" candidate structure will generate a good hypothesis with error at most $\epsilon$ ). The total sample complexity will then be

$$
O\left(\frac{2^{d} n}{\epsilon^{2}}+\frac{\log N}{\epsilon^{2}}\right)=O\left(\frac{2^{d} n}{\epsilon^{2}}+\frac{d n \log n}{\epsilon^{2}}\right)
$$

which is $O\left(2^{d} n / \epsilon^{2}\right)$ for $d=\Omega(\log n)$.

# A. 2 Sample Complexity Lower Bound 

Our lower bound will be derived from families of Bayes nets with the following structure: The first $d$ nodes are all independent (and will in fact have marginal probability $1 / 2$ each), and will form in some sense a "pointer" to one of $2^{d}$ arbitrary product distributions. The remaining $n-d$ nodes will each depend on all of the first $d$. The resulting distribution is now an (evenly weighted) disjoint mixture of $2^{d}$ product distributions on the $(n-d)$-dimensional hypercube. In other words, there are $2^{d}$ product distributions $p_{1}, \ldots, p_{2^{d}}$, and our distribution returns a random $i$ (encoded in binary) followed by a random sample form $p_{i}$. Note that the $p_{i}$ can be arbitrary product distributions.

We show a lower bound of $\Omega\left(2^{d} n / \epsilon^{2}\right)$ lower bound for learning, whenever $d<(1-\Omega(1)) n$.
Let $\mathcal{C}_{\epsilon}$ be a family of product distributions over $\{0,1\}^{n-d}$ which is hard to learn, i.e., such that any algorithm learning $\mathcal{C}_{\epsilon}$ to accuracy $4 \epsilon$ which succeeds with probability greater than $1 / 2$ must

have sample complexity $\Omega\left(n / \epsilon^{2}\right)$. We will choose each $p_{i}$ independently and uniformly at random from $\mathcal{C}_{\epsilon}$.

Assume for the sake of contradiction that there exists an algorithm $\mathcal{A}$ to learn the resulting disjoint mixture of $p_{i}$ 's to error $\epsilon$ with $o\left(2^{d}(n-d) / \epsilon^{2}\right)$ samples. Without loss of generality, this algorithm can be thought of returning as hypothesis a disjoint union of some other distributions $q_{1}, \ldots, q_{2^{d}}$, in which case the error incurred is $\|p-q\|_{1}=\frac{1}{2^{d}} \sum_{i=1}^{2^{d}}\left\|p_{i}-q_{i}\right\|_{1}$.

By assumption on its sample complexity, for at least half of the indices $1 \leq i \leq 2^{d}$ the algorithm obtains $o\left(n / \epsilon^{2}\right)$ samples from $p_{i}$. This implies that in expectation, by the fact that $\mathcal{C}_{\epsilon}$ was chosen hard to learn, for at least half of these indices it will be the case that $\left\|p_{i}-q_{i}\right\|_{1}>16 \epsilon$ (as each of these $i$ 's is such that $\left\|p_{i}-q_{i}\right\|_{1}>16 \epsilon$ with probability at least $1 / 2$ ). This in turn shows that in expectation, $\|p-q\|_{1}=\frac{1}{2^{d}} \sum_{i=1}^{2^{d}}\left\|p_{i}-q_{i}\right\|_{1}>\frac{4 \epsilon}{3}=\epsilon$, leading to a contradiction.

# B Omitted Proofs from Section 4.2 

We give in this section the proofs of the corresponding lemmas from Section 4.2.
Proof of Lemma 8. By symmetry, it is sufficient to consider the distribution $P \stackrel{\text { def }}{=} \bigotimes_{j=1}^{n} \operatorname{Bern}\left(\frac{1}{2}+\frac{\epsilon}{\sqrt{n}}\right)$. We explicitly bound from below the expression of $\|P-U\|_{1}$ :

$$
\begin{aligned}
\|P-U\|_{1} & =\sum_{x \in\{0,1\}^{n}}\left|\left(\frac{1}{2}+\frac{\epsilon}{\sqrt{n}}\right)^{|x|}\left(\frac{1}{2}-\frac{\epsilon}{\sqrt{n}}\right)^{n-|x|}-\frac{1}{2^{n}}\right| \\
& =\frac{1}{2^{n}} \sum_{k=0}^{n}\binom{n}{k}\left|\left(1+\frac{2 \epsilon}{\sqrt{n}}\right)^{k}\left(1-\frac{2 \epsilon}{\sqrt{n}}\right)^{n-k}-1\right| \\
& \geq \frac{1}{2^{n}} \sum_{k=\frac{n}{2}+\sqrt{n}}^{\frac{n}{2}+2 \sqrt{n}}\binom{n}{k}\left|\left(1+\frac{2 \epsilon}{\sqrt{n}}\right)^{k}\left(1-\frac{2 \epsilon}{\sqrt{n}}\right)^{n-k}-1\right| \\
& \geq \frac{C}{\sqrt{n}} \sum_{k=\frac{n}{2}+\sqrt{n}}^{\frac{n}{2}+2 \sqrt{n}}\left|\left(1+\frac{2 \epsilon}{\sqrt{n}}\right)^{k}\left(1-\frac{2 \epsilon}{\sqrt{n}}\right)^{n-k}-1\right|
\end{aligned}
$$

where $C>0$ is an absolute constant. We handle each summand separately: fixing $k$, and writing $\ell \stackrel{\text { def }}{=} k-\frac{n}{2} \in[\sqrt{n}, 2 \sqrt{n}]$,

$$
\begin{aligned}
\left(1+\frac{2 \epsilon}{\sqrt{n}}\right)^{k}\left(1-\frac{2 \epsilon}{\sqrt{n}}\right)^{n-k} & =\left(1-\frac{4 \epsilon^{2}}{n}\right)^{n / 2}\left(\frac{1+\frac{2 \epsilon}{\sqrt{n}}}{1-\frac{2 \epsilon}{\sqrt{n}}}\right)^{\ell} \\
& \geq\left(1-\frac{4 \epsilon^{2}}{n}\right)^{n / 2}\left(\frac{1+\frac{2 \epsilon}{\sqrt{n}}}{1-\frac{2 \epsilon}{\sqrt{n}}}\right)^{\sqrt{n}} \\
& \xrightarrow[n \rightarrow \infty]{ } e^{4 \epsilon-2 \epsilon^{2}}
\end{aligned}
$$

so that each summand is bounded by a quantity that converges (when $n \rightarrow \infty$ ) to $e^{4 \epsilon-2 \epsilon^{2}}-1>$ $4 \epsilon-2 \epsilon^{2}>2 \epsilon$, implying that each is $\Omega(\epsilon)$. Combining the above gives

$$
\|P-U\|_{1} \geq \frac{C}{\sqrt{n}} \sum_{k=\frac{n}{2}+\sqrt{n}}^{\frac{n}{2}+2 \sqrt{n}} \Omega(\epsilon)=\Omega(\epsilon)
$$

as claimed.
Proof of Lemma 9. By symmetry it suffices to consider only the case of $i=1$, so that we let $A=N_{1}$. The first step is to bound from above $I(X ; A)$ by a more manageable quantity:
Fact 4. We have that

$$
I(X ; A) \leq \sum_{a=0}^{\infty} \operatorname{Pr}[A=a]\left(1-\frac{\operatorname{Pr}[A=a \mid X=1]}{\operatorname{Pr}[A=a \mid X=0]}\right)^{2}
$$

The proof of this fact is given in Appendix D. It will then be sufficient to bound the RHS, which we do next. Since $A \sim \operatorname{Poi}\left(k p_{1}\right)$ with $p_{1}=1 / 2$ if $X=0$ and uniformly $\frac{1}{2} \pm \frac{\epsilon}{\sqrt{n}}$ if $X=1$, a simple computation yields that

$$
\begin{aligned}
& \operatorname{Pr}[A=\ell \mid X=0]=e^{-k / 2} \frac{(k / 2)^{\ell}}{\ell!} \\
& \operatorname{Pr}[A=\ell \mid X=1]=e^{-k / 2} \frac{(k / 2)^{\ell}}{\ell!}\left(\frac{e^{-k \epsilon / \sqrt{n}}\left(1+2 \frac{\epsilon}{\sqrt{n}}\right)^{\ell}+e^{k \epsilon / \sqrt{n}}\left(1-2 \frac{\epsilon}{\sqrt{n}}\right)^{\ell}}{2}\right)
\end{aligned}
$$

Writing out $\varphi(\epsilon, \ell)=\frac{\operatorname{Pr}[A=\ell \mid X=1]}{\operatorname{Pr}[A=\ell \mid X=0]}$ as a function of $\epsilon / \sqrt{n}$, we see that it is even. Thus, expanding it as a Taylor series in $\alpha \stackrel{\text { def }}{=} \epsilon / \sqrt{n}$, the odd degree terms will cancel. Moreover, we can write

$$
\begin{aligned}
\sum_{\ell=0}^{\infty} \operatorname{Pr}[A=\ell](1-\varphi(\epsilon, A))^{2}= & \mathbb{E}_{A}\left[(1-\varphi(\epsilon, A))^{2}\right] \\
= & \frac{1}{2} \mathbb{E}_{A \sim \operatorname{Poi}(k / 2)}\left[(1-\varphi(\epsilon, A))^{2}\right] \\
& +\frac{1}{4} \mathbb{E}_{A \sim \operatorname{Poi}(k(1 / 2+\alpha))}\left[(1-\varphi(\epsilon, A))^{2}\right] \\
& +\frac{1}{4} \mathbb{E}_{A \sim \operatorname{Poi}(k(1 / 2-\alpha))}\left[(1-\varphi(\epsilon, A))^{2}\right]
\end{aligned}
$$

Now, we can rewrite

$$
\begin{aligned}
(1-\varphi(\epsilon, A))^{2} & =\left(1-\frac{e^{-k \alpha}(1+2 \alpha)^{\ell}+e^{k \alpha}(1-2 \alpha)^{\ell}}{2}\right)^{2} \\
& =1-\left(e^{-k \alpha}(1+2 \alpha)^{\ell}+e^{k \alpha}(1-2 \alpha)^{\ell}\right)+\frac{e^{-2 k \alpha}(1+2 \alpha)^{2 \ell}+2\left(1-4 \alpha^{2}\right)^{\ell}+e^{2 k \alpha}(1-2 \alpha)^{2 \ell}}{4}
\end{aligned}
$$

For $b \in\{-1,0,1\}$, we have $\mathbb{E}_{A \sim \operatorname{Poi}(k(1 / 2+b \alpha))}[1]=1$ (!), and (from the MGF of a Poisson distribution)

$$
\begin{aligned}
e^{-k \alpha} \mathbb{E}_{A \sim \operatorname{Poi}(k(1 / 2+b \alpha))}\left[(1+2 \alpha)^{A}\right] & =e^{b \cdot 2 \alpha^{2} k} \\
e^{k \alpha} \mathbb{E}_{A \sim \operatorname{Poi}(k(1 / 2+b \alpha))}\left[(1-2 \alpha)^{A}\right] & =e^{-b \cdot 2 \alpha^{2} k}
\end{aligned}
$$

as well as

$$
\begin{aligned}
e^{-2 k \alpha} \mathbb{E}_{A \sim \operatorname{Poi}(k(1 / 2+b \alpha))}\left[(1+2 \alpha)^{2 A}\right] & =e^{2 k \alpha^{2}(1+2 b+2 b \alpha)} \\
e^{2 k \alpha} \mathbb{E}_{A \sim \operatorname{Poi}(k(1 / 2+b \alpha))}\left[(1-2 \alpha)^{2 A}\right] & =e^{2 k \alpha^{2}(1-2 b+2 b \alpha)} \\
2 \mathbb{E}_{A \sim \operatorname{Poi}(k(1 / 2+b \alpha))}\left[\left(1-4 \alpha^{2}\right)^{A}\right] & =2 e^{-2 k \alpha^{2}-4 k b \alpha^{3}}
\end{aligned}
$$

Gathering the terms, we get

$$
\begin{aligned}
\mathbb{E}_{A}\left[(1-\varphi(\epsilon, A))^{2}\right]= & \frac{1}{16}\left(-4\left(e^{2 k \alpha^{2}}+e^{-2 k \alpha^{2}}\right)+e^{2 k \alpha^{2}(3+2 \alpha)}\right. \\
& +e^{2 k \alpha^{2}(-1+2 \alpha)}+2 e^{-2 k \alpha^{2}-4 k \alpha^{3}} \\
& \left.+e^{-2 k \alpha^{2}(1+2 \alpha)}+e^{2 k \alpha^{2}(3-2 \alpha)}+2 e^{-2 k \alpha^{2}+4 k \alpha^{3}}\right) \\
= & O\left(k^{2} \alpha^{4}\right)
\end{aligned}
$$

(Taylor series expansion in $\alpha$ )
giving that indeed $\sum_{\ell=0}^{\infty} \operatorname{Pr}[A=\ell](1-\varphi(\epsilon, A))^{2}=O\left(\frac{\epsilon^{4} k^{2}}{n^{2}}\right)$. This completes the proof.
Proof of Lemma 10. Using Hellinger distance as a proxy will only result in an $\Omega\left(\epsilon^{2}\right)$ lower bound on the distance, so we compute it explicitly instead: in what follows, $e^{(j)} \in\{0,1\}^{n}$ denotes the basis vector with $e_{i}^{(j)}=\mathbf{1}_{\{i=j\}}$. Fix any vector $b=\left(b_{1}, \ldots, b_{n}\right) \in\{0,1\}^{n}$ such that $|b| \in[n / 3,2 n / 3]$, and let $P$ be the corresponding distribution from the support of $\mathcal{N}$.

$$
\begin{aligned}
\left\|P-P^{*}\right\|_{1} & \geq \sum_{j=1}^{n}\left|P\left(e^{(j)}\right)-P^{*}\left(e^{(j)}\right)\right| \\
& =\sum_{j=1}^{n}\left|\frac{1+(-1)^{b_{j}} \epsilon}{n} \prod_{i \neq j}\left(1-\frac{1+(-1)^{b_{i}} \epsilon}{n}\right)-\frac{1}{n}\left(1-\frac{1}{n}\right)^{n-1}\right| \\
& =\frac{1}{n}\left(1-\frac{1}{n}\right)^{n-1} \sum_{j=1}^{n}\left|\left(1+(-1)^{b_{j}} \epsilon\right) \prod_{i \neq j}\left(1-\frac{(-1)^{b_{i}} \epsilon}{n-1}\right)-1\right|
\end{aligned}
$$

Each summand can be bounded from above as follows:

$$
\left(1-\frac{\epsilon}{n-1}\right)^{2 n / 3} \leq \prod_{i \neq j}\left(1-\frac{(-1)^{b_{i}} \epsilon}{n-1}\right) \leq\left(1+\frac{\epsilon}{n-1}\right)^{2 n / 3}
$$

where the last inequality follows from our assumption on $|b|$. In turn, this gives that

- If $b_{j}=0$,

$$
\left(1+(-1)^{b_{j}} \epsilon\right) \prod_{i \neq j}\left(1-\frac{(-1)^{b_{i}} \epsilon}{n-1}\right)-1 \geq(1+\epsilon)\left(1-\frac{\epsilon}{n-1}\right)^{2 n / 3}-1=\Omega(\epsilon)
$$

- If $b_{j}=1$,

$$
1-\left(1+(-1)^{b_{j}} \epsilon\right) \prod_{i \neq j}\left(1-\frac{(-1)^{b_{i}} \epsilon}{n-1}\right) \geq 1-(1-\epsilon)\left(1+\frac{\epsilon}{n-1}\right)^{2 n / 3}=\Omega(\epsilon)
$$

Since $\frac{1}{n}\left(1-\frac{1}{n}\right)^{n-1}=\frac{e^{-1}+o(1)}{n}$, we get $\left\|P-P^{*}\right\|_{1}=\Omega(\epsilon)$. The lemma now follows from the fact that a uniformly random $b \in\{0,1\}^{n}$ satisfies $|b| \in[n / 3,2 n / 3]$ with probability $1-2^{-\Omega(n)}$.

# C Omitted Proofs from Section 3 

We provide in this section the proofs of the inequalities stated in the preliminaries (Section 3).
Proof of Lemma 1. Using properties of the KL-divergence:

$$
\mathrm{D}(P \| Q)=\mathrm{D}\left(P_{1} \otimes \cdots \otimes P_{n} \| Q_{1} \otimes \cdots \otimes Q_{n}\right)=\sum_{i=1}^{n} \mathrm{D}\left(P_{i} \| Q_{i}\right)
$$

so it suffices to show that $2\left(p_{i}-q_{i}\right)^{2} \leq \mathrm{D}\left(P_{i} \| Q_{i}\right) \leq \frac{\left(p_{i}-q_{i}\right)^{2}}{q_{i}\left(1-q_{i}\right)}$ for all $i \in[n]$. Since $P_{i}=\operatorname{Bern}\left(p_{i}\right)$ and $Q_{i}=\operatorname{Bern}\left(q_{i}\right)$, we can write

$$
\mathrm{D}\left(P_{i} \| Q_{i}\right)=p_{i} \ln \frac{p_{i}}{q_{i}}+\left(1-p_{i}\right) \ln \frac{1-p_{i}}{1-q_{i}}
$$

Defining $f:(0,1)^{2} \rightarrow \mathbb{R}$ as $f(x, y) \stackrel{\text { def }}{=} x \ln \frac{x}{y}+(1-x) \ln \frac{1-x}{1-y}$, we thus have to show that $2(x-y)^{2} \leq$ $f(x, y) \leq \frac{(x-y)^{2}}{y(1-y)}$ for all $x, y \in(0,1)$.

We begin by the upper bound: fixing any $x, y \in(0,1)$ and setting $\delta \stackrel{\text { def }}{=} x-y$, we have

$$
\begin{aligned}
f(x, y) & =x \ln \left(1+\frac{\delta}{y}\right)+(1-x) \ln \left(1-\frac{\delta}{1-y}\right) \\
& \leq \frac{x}{y} \delta-\frac{1-x}{1-y} \delta=\frac{\delta^{2}}{y(1-y)}
\end{aligned}
$$

from $\ln (1+u) \leq u$ for all $u \in(-1, \infty)$.
Turning to the lower bound, we fix any $y \in(0,1)$ and consider the auxiliary function $h_{y}:(0,1) \rightarrow$ $\mathbb{R}$ defined by $h_{y}(x)=f(x, y)-2(x-y)^{2}$. From $h_{y}^{\prime \prime}(x)=\frac{(1-2 x)^{2}}{x(1-x)} \geq 0$, we get that $h_{y}$ is convex, i.e. $h_{y}^{\prime}$ is non-decreasing. Since $h_{y}^{\prime}(x)=\ln \frac{x(1-y)}{(1-x) y}-4(x-y)$, we have $h_{y}^{\prime}(y)=0$, and in turn we get that $h_{y}$ is non-increasing on $(0, y]$ and non-decreasing on $[y, 1)$. Since $h_{y}(y)=0$, this leads to $h_{y}(x) \geq 0$ for all $x \in(0,1)$, i.e. $f(x, y) \geq 2(x-y)^{2}$.

Proof of Lemma 2. Recall that for any pair of distributions, we have that $\mathrm{d}_{\mathrm{H}}(P, Q)^{2} \leq \frac{1}{2}\|P-Q\|_{1} \leq$ $\sqrt{2} \mathrm{~d}_{\mathrm{H}}(P, Q)$, where $\mathrm{d}_{\mathrm{H}}(P, Q)$ denotes the Hellinger distance between $P, Q$. Therefore, it is enough to show that

$$
\min \left(c^{\prime}, \frac{1}{4} \sum_{i=1}^{n}\left(p_{i}-q_{i}\right)^{2}\right) \leq \mathrm{d}_{\mathrm{H}}(P, Q)^{2} \leq \sum_{i=1}^{n} \frac{\left(p_{i}-q_{i}\right)^{2}}{q_{i}\left(1-q_{i}\right)}
$$

for some absolute constant $c^{\prime}>0$. (We will show $c^{\prime}=1-e^{-3 / 2} \simeq 0.78$.)
Since $P, Q$ are product measures,

$$
\mathrm{d}_{\mathrm{H}}(P, Q)^{2}=1-\prod_{i=1}^{n}\left(1-\mathrm{d}_{\mathrm{H}}\left(P_{i}, Q_{i}\right)^{2}\right)=1-\prod_{i=1}^{n}\left(\sqrt{p_{i} q_{i}}+\sqrt{\left(1-p_{i}\right)\left(1-q_{i}\right)}\right)
$$

We start with the lower bound. Noting that for any $x, y \in(0,1)$ it holds that

$$
\sqrt{x y}+\sqrt{(1-x)(1-y)} \leq 1-\frac{1}{2}(x-y)^{2}
$$

(e.g., by observing that the function $x \in(0,1) \mapsto 1-\frac{1}{2}(x-y)^{2}-(\sqrt{x y}+\sqrt{(1-x)(1-y)})$ is minimized at $y$, where it takes value 0 ), we get

$$
\begin{aligned}
\mathrm{d}_{\mathrm{H}}(P, Q)^{2} & \geq 1-\prod_{i=1}^{n}\left(1-\frac{1}{2}\left(p_{i}-q_{i}\right)^{2}\right) \\
& \geq \min \left(1-e^{-3 / 2}, \frac{1}{4} \sum_{i=1}^{n}\left(p_{i}-q_{i}\right)^{2}\right) \\
& =\min \left(1-e^{-3 / 2}, \frac{1}{4}\|p-q\|_{2}^{2}\right)
\end{aligned}
$$

where we relied on the inequality $1-\prod_{i=1}^{n}\left(1-x_{i}\right) \geq \frac{1}{2} \sum_{i=1}^{n} x_{i}$ for $\left(x_{1}, \ldots, x_{n}\right) \in[0,1]$ :

$$
1-\prod_{i=1}^{n}\left(1-x_{i}\right)=1-e^{\sum_{i=1}^{n} \ln \left(1-x_{i}\right)} \geq 1-e^{-\sum_{i=1}^{n} x_{i}} \geq 1-\left(1-\frac{1}{2} \sum_{i=1}^{n} x_{i}\right)
$$

(the last inequality being true for $\sum_{i=1}^{n} x_{i} \leq \frac{3}{2}$, i.e. $\|p-q\|_{2}^{2} \leq 3$ ).
Turning to the upper bound, the elementary inequality $2 \sqrt{x y}=x+y-(\sqrt{x}-\sqrt{y})^{2}, x, y>0$, gives that

$$
\sqrt{p_{i} q_{i}}+\sqrt{\left(1-p_{i}\right)\left(1-q_{i}\right)} \geq 1-\frac{\left(p_{i}-q_{i}\right)^{2}}{\left(p_{i}+q_{i}\right)\left(2-p_{i}-q_{i}\right)}=1-z_{i}
$$

Therefore,

$$
\begin{aligned}
\mathrm{d}_{\mathrm{H}}(P, Q)^{2} & \leq\left(1-\prod_{i=1}^{n}\left(1-z_{i}\right)\right) \leq \sum_{i=1}^{n} z_{i} \\
& =\sum_{i=1}^{n} \frac{\left(p_{i}-q_{i}\right)^{2}}{\left(p_{i}+q_{i}\right)\left(2-p_{i}-q_{i}\right)} \\
& \leq \sum_{i=1}^{n} \frac{\left(p_{i}-q_{i}\right)^{2}}{q_{i}\left(1-q_{i}\right)}
\end{aligned}
$$

where the third-to-last inequality follows from the union bound, and the last from the simple fact that $\left(p_{i}+q_{i}\right)\left(2-p_{i}-q_{i}\right) \geq q_{i}\left(1-q_{i}\right)$.

Proof of Lemma 3. Let $A$ and $B$ be two distributions on $\{0,1\}^{d}$. Then we have:

$$
\mathrm{D}(A \| B)=\sum_{x \in\{0,1\}^{d}} \operatorname{Pr}_{A}[x] \ln \frac{\operatorname{Pr}_{A}[x]}{\operatorname{Pr}_{B}[x]}
$$

For a fixed $i \in[d]$, the events $\Pi_{i, a}$ form a partition of $\{0,1\}^{d}$. Dividing the sum above into this partition, we obtain

$$
\begin{aligned}
\mathrm{D}(A \| B) & =\sum_{a} \sum_{x \in \Pi_{i, a}} \operatorname{Pr}_{A}[x] \ln \frac{\operatorname{Pr}_{A}[x]}{\operatorname{Pr}_{B}[x]} \\
& =\sum_{a} \operatorname{Pr}_{A}\left[\Pi_{i, a}\right] \cdot \sum_{x \in\{0,1\}^{d}} \operatorname{Pr}_{A}\left[\Pi_{i, a}\right.[x]\left(\ln \frac{\operatorname{Pr}_{A}\left[\Pi_{i, a}\right]}{\operatorname{Pr}_{B}\left[\Pi_{i, a}\right]}+\ln \frac{\operatorname{Pr}_{A\left[\Pi_{i, a}\right.}[x]}{\operatorname{Pr}_{B\left[\Pi_{i, a}\right.}[x]}\right) \\
& =\sum_{a} \operatorname{Pr}_{A}\left[\Pi_{i, a}\right]\left(\ln \frac{\operatorname{Pr}_{A}\left[\Pi_{i, a}\right]}{\operatorname{Pr}_{B}\left[\Pi_{i, a}\right]}+\mathrm{D}\left(A \mid \Pi_{i, a} \| B \mid \Pi_{i, a}\right)\right.
\end{aligned}
$$

Let $P_{\leq i}$ be the distribution over the first $i$ coordinates of $P$ and define $Q_{\leq i}$ similarly for $Q$. Let $P_{i}$ and $Q_{i}$ be the distribution of the $i$-th coordinate of $P$ and $Q$ respectively. We will apply the above to $P_{\leq i-1}$ and $P_{\leq i}$. First note that the $i$-th coordinate of $P_{\leq i} \mid \Pi_{i, a}$ and $Q_{\leq i} \mid \Pi_{i, a}$ is independent of the others, thus we have (which likely follows from standard results):

$$
\begin{aligned}
\mathrm{D}\left(P_{\leq i} \mid \Pi_{i, a} \| Q_{\leq i} \mid \Pi_{i, a}\right) & =\sum_{x \in\{0,1\}^{i}} \operatorname{Pr}_{P_{\leq i} \mid \Pi_{i, a}}[x] \ln \frac{\operatorname{Pr}_{P_{\leq i} \mid \Pi_{i, a}}[x]}{\operatorname{Pr}_{Q_{\leq i} \mid \Pi_{i, a}}[x]} \\
& =\sum_{x \in\{0,1\}^{i}} \operatorname{Pr}_{P_{\leq i-1} \mid \Pi_{i, a}}\left[x_{\leq i-1}\right] \operatorname{Pr}_{P_{i} \mid \Pi_{i, a}}\left[x_{i}\right] \cdot\left(\ln \frac{\operatorname{Pr}_{P_{\leq i-1} \mid \Pi_{i, a}}\left[x_{\leq i-1}\right]}{\operatorname{Pr}_{Q_{\leq i-1} \mid \Pi_{i, a}}\left[x_{\leq i-1}\right]}+\ln \frac{\operatorname{Pr}_{P_{i} \mid \Pi_{i, a}}\left[x_{i}\right]}{\operatorname{Pr}_{Q_{\leq i} \mid \Pi_{i, a}}\left[x_{i}\right]}\right) \\
& =\sum_{x \in\{0,1\}^{i-1}} \operatorname{Pr}_{P_{\leq i-1} \mid \Pi_{i, a}}[x] \ln \frac{\operatorname{Pr}_{P_{\leq i-1} \mid \Pi_{i, a}}[x]}{\operatorname{Pr}_{Q_{\leq i-1} \mid \Pi_{i, a}}[x]}+\sum_{y \in\{0,1\}} \operatorname{Pr}_{P_{i} \mid \Pi_{i, a}}[y] \ln \frac{\operatorname{Pr}_{P_{i} \mid \Pi_{i, a}}[y]}{\operatorname{Pr}_{Q_{\leq i} \mid \Pi_{i, a}}[y]} \\
& =\mathrm{D}\left(P_{\leq i-1} \mid \Pi_{i, a} \| Q_{\leq i-1} \mid \Pi_{i, a}\right)+\mathrm{D}\left(P_{i} \mid \Pi_{i, a} \| Q_{i} \mid \Pi_{i, a}\right)
\end{aligned}
$$

Thus, we have:

$$
\begin{aligned}
\mathrm{D}\left(P_{\leq i} \| Q_{\leq i}\right) & =\sum_{a} \operatorname{Pr}_{P_{\leq i}}\left[\Pi_{i, a}\right]\left(\ln \frac{\operatorname{Pr}_{P_{\leq i}}\left[\Pi_{i, a}\right]}{\operatorname{Pr}_{Q_{\leq i}}\left[\Pi_{i, a}\right]}+\mathrm{D}\left(P_{\leq i} \mid \Pi_{i, a} \| Q_{\leq i} \mid \Pi_{i, a}\right)\right. \\
& =\sum_{a} \operatorname{Pr}_{P_{\leq i}}\left[\Pi_{i, a}\right]\left(\ln \frac{\operatorname{Pr}_{P_{\leq i}}\left[\Pi_{i, a}\right]}{\operatorname{Pr}_{Q_{\leq i}}\left[\Pi_{i, a}\right]}+\mathrm{D}\left(P_{\leq i-1} \mid \Pi_{i, a} \| Q_{\leq i-1} \mid \Pi_{i, a}\right)+\mathrm{D}\left(P_{i} \mid \Pi_{i, a} \| Q_{i} \mid \Pi_{i, a}\right)\right) \\
& =\mathrm{D}\left(P_{\leq i-1} \| Q_{\leq i-1}\right)+\sum_{a} \operatorname{Pr}_{P}\left[\Pi_{i, a}\right] \mathrm{D}\left(P_{i} \mid \Pi_{i, a} \| Q_{i} \mid \Pi_{i, a}\right)
\end{aligned}
$$

By induction on $i$, we get

$$
\mathrm{D}(P \| Q)=\sum_{(i, a) \in S} \operatorname{Pr}_{P}\left[\Pi_{i, a}\right] \mathrm{D}\left(P_{i} \mid \Pi_{i, a} \| Q_{i} \mid \Pi_{i, a}\right)
$$

Now the distributions $P_{i} \mid \Pi_{i, a}$ and $Q_{i} \mid \Pi_{i, a}$ are Bernoulli random variables with means $p_{i, a}$ and $q_{i, a}$. For $p, q \in[0,1]$, we have:

$$
\operatorname{D}(\operatorname{Bern}(p) \| \operatorname{Bern}(q))=p \ln \frac{p}{q}+(1-p) \ln \frac{1-p}{1-q} \leq \frac{(p-q)^{2}}{q(1-q)}
$$

as in the proof of Claim 1. On the other hand, studying for instance the function $f_{q}:(0,1) \rightarrow \mathbb{R}$ defined by $f_{q}(p)=\frac{p \ln \frac{p}{q}+(1-p) \ln \frac{1-p}{1-q}}{(p-q)^{2}}$ (extended by continuity at $q$ ), we get

$$
f_{q}(p) \geq f_{q}(1-q) \geq 2
$$

for all $p, q \in(0,1)^{2}$. This shows the lower bound.

# D Omitted Proofs from Sections 4.2 and 8.2 

Fact (Fact 4).

$$
I(X ; A) \leq \sum_{a=0}^{\infty} \operatorname{Pr}[A=a]\left(1-\frac{\operatorname{Pr}[A=a \mid X=1]}{\operatorname{Pr}[A=a \mid X=0]}\right)^{2}
$$

Proof. For $a \in \mathbb{N}$, we write $p_{a}=\operatorname{Pr}[X=0 \mid A=a]$ and $q_{a}=\operatorname{Pr}[X=1 \mid A=a]$, so that $p_{a}+q_{a}=1$. By definition,

$$
\begin{aligned}
I(X ; A) & =\sum_{a=0}^{\infty} \operatorname{Pr}[A=a] \cdot \sum_{x \in\{0,1\}} \operatorname{Pr}[X=x \mid A=a] \log \frac{\operatorname{Pr}[X=x \mid A=a]}{\operatorname{Pr}[X=x]} \\
& =\sum_{a=0}^{\infty} \operatorname{Pr}[A=a] \cdot\left(p_{a} \log \frac{p_{a}}{\operatorname{Pr}[X=1]}+q_{a} \log \frac{q_{a}}{\operatorname{Pr}[X=0]}\right) \\
& =\sum_{a=0}^{\infty} \operatorname{Pr}[A=a]\left(p_{a} \log \left(2 p_{a}\right)+q_{a} \log \left(2 q_{a}\right)\right) \\
& =\sum_{a=0}^{\infty} \operatorname{Pr}[A=a]\left(\left(1-q_{a}\right) \log \left(1-q_{a}\right)+q_{a} \log \left(q_{a}\right)+1\right) \\
& \leq \sum_{a=0}^{\infty} \operatorname{Pr}[A=a]\left(1-\frac{q_{a}}{1-q_{a}}\right)^{2} \\
& =\sum_{a=0}^{\infty} \operatorname{Pr}[A=a]\left(1-\frac{q_{a}}{p_{a}}\right)^{2}
\end{aligned}
$$

where for the last inequality we rely on the fact that the binary entropy satisfies $h(x) \geq 1-$ $\left(1-\frac{x}{1-x}\right)^{2}$ for all $x \in[0,1)$.
Alternative proof of Lemma 11. We proceed as in the proof of Lemma 9, first writing

$$
\begin{aligned}
I(X ; A) & =\sum_{\ell=0}^{\infty} \operatorname{Pr}[A=a]\left(1-\frac{\operatorname{Pr}[A=a \mid X=1]}{\operatorname{Pr}[A=a \mid X=0]}\right)^{2} \\
& =\mathbb{E}_{A}\left[\left(1-\frac{\operatorname{Pr}[A=a \mid X=1]}{\operatorname{Pr}[A=a \mid X=0]}\right)^{2}\right]
\end{aligned}
$$

and noticing that $z_{a} \stackrel{\text { def }}{=} \frac{\operatorname{Pr}\left[A=a \mid X=1\right]}{\operatorname{Pr}[A=a \mid X=0]}=\frac{e^{-k \epsilon / n}(1+\epsilon)^{a}+e^{k \epsilon / n}(1-\epsilon)^{a}}{2}$. This leads to

$$
4\left(1-z_{a}\right)^{2}=4-4\left(e^{-\frac{k}{n} \epsilon}(1+\epsilon)^{a}+e^{\frac{k}{n} \epsilon}(1-\epsilon)^{a}\right)+\left(e^{-2 \frac{k}{n} \epsilon}(1+\epsilon)^{2 a}+e^{2 \frac{k}{n} \epsilon}(1-\epsilon)^{2 a}+2\left(1-\epsilon^{2}\right)^{a}\right)
$$

We also have, by definition of $A$, that for any $z \in \mathbb{R}$

$$
\begin{aligned}
\mathbb{E}_{A}\left[z^{A}\right] & =\frac{1}{2} \mathbb{E}_{A \sim \operatorname{Poi}\left(\frac{k}{n}\right)}\left[z^{A}\right]+\frac{1}{4} \mathbb{E}_{A \sim \operatorname{Poi}\left(\frac{k}{n}(1+\epsilon)\right)}\left[z^{A}\right]+\frac{1}{4} \mathbb{E}_{A \sim \operatorname{Poi}\left(\frac{k}{n}(1-\epsilon)\right)}\left[z^{A}\right] \\
& =\frac{1}{2} e^{\frac{k}{n}(z-1)}+\frac{1}{4} e^{\frac{k}{n}(1+\epsilon)(z-1)}+\frac{1}{4} e^{\frac{k}{n}(1-\epsilon)(z-1)}
\end{aligned}
$$

from the expression of the probability generating function of a Poisson random variable. For any $\beta \in\{-1,1\}$, we therefore have

$$
\begin{aligned}
4 e^{-\frac{k}{n} \beta \epsilon} \mathbb{E}_{A}\left[(1+\beta \epsilon)^{A}\right] & =2+e^{\frac{k}{n} \beta \epsilon^{2}}+e^{-\frac{k}{n} \beta \epsilon^{2}} \\
4 e^{-2 \frac{k}{n} \beta \epsilon} \mathbb{E}_{A}\left[(1+\beta \epsilon)^{2 A}\right] & =2 e^{\frac{k}{n} \epsilon^{2}}+e^{\frac{k}{n}\left((1+2 \beta) \epsilon^{2}+\epsilon^{3}\right)}+e^{\frac{k}{n}\left((1-2 \beta) \epsilon^{2}-\epsilon^{3}\right)}
\end{aligned}
$$

and

$$
4 \cdot 2 \mathbb{E}_{A}\left[\left(1-\epsilon^{2}\right)^{A}\right]=4 e^{\frac{k}{n} \epsilon^{2}}+2 e^{\frac{k}{n}\left(\epsilon^{2}+\epsilon^{3}\right)}+2 e^{\frac{k}{n}\left(\epsilon^{2}-\epsilon^{3}\right)}
$$

Combining Eq. (15) and the above, we obtain

$$
\begin{aligned}
16 \mathbb{E}_{A}\left[\left(1-z_{A}\right)^{2}\right]= & 16-4\left(4 e^{-\frac{k}{n} \epsilon} \mathbb{E}_{A}\left[(1+\epsilon)^{A}\right]+4 e^{\frac{k}{n} \epsilon} \mathbb{E}_{A}\left[(1-\epsilon)^{A}\right]\right) \\
& +\left(4 e^{-2 \frac{k}{n} \epsilon} \mathbb{E}_{A}\left[(1+\epsilon)^{2 A}\right]+4 e^{2 \frac{k}{n} \epsilon} \mathbb{E}_{A}\left[(1-\epsilon)^{2 A}\right]\right. \\
& \left.+8 \mathbb{E}_{A}\left[\left(1-\epsilon^{2}\right)^{A}\right]\right) \\
= & 8-8\left(e^{\frac{k}{n} \epsilon^{2}}+e^{-\frac{k}{n} \epsilon^{2}}\right)+\left(e^{\frac{k}{n} 3 \epsilon^{2}}+e^{-\frac{k}{n} \epsilon^{2}}+2 e^{\frac{k}{n} \epsilon^{2}}\right)\left(e^{\frac{k}{n} \epsilon^{3}}+e^{-\frac{k}{n} \epsilon^{3}}\right)
\end{aligned}
$$

A Taylor expansion of this expression (in $\frac{k \epsilon^{2}}{n}$ for the first two parentheses, and $\frac{k \epsilon^{3}}{n}$ for the last) shows that

$$
\mathbb{E}_{A}\left[\left(1-z_{A}\right)^{2}\right]=O\left(\frac{k^{2} \epsilon^{4}}{n^{2}}\right)
$$

as claimed.
Proof of Lemma 22. From the definition of $I(X ; Y)=\sum_{(x, y) \in\{0,1\}} \operatorname{Pr}[X=x, Y=y] \log \frac{\operatorname{Pr}[X=x, Y=y]}{\operatorname{Pr}[X=x] \operatorname{Pr}[Y=y]}$, it is straightforward to check that for $X, Y$ taking values in $\{0,1\}$

$$
\begin{aligned}
I(X ; Y)= & \mathbb{E}[X Y] \log \frac{\mathbb{E}[X Y]}{\mathbb{E}[X] \mathbb{E}[Y]} \\
& +(\mathbb{E}[X]-\mathbb{E}[X Y]) \log \frac{\mathbb{E}[X]-\mathbb{E}[X Y]}{\mathbb{E}[X](1-\mathbb{E}[Y])} \\
& +(\mathbb{E}[Y]-\mathbb{E}[X Y]) \log \frac{\mathbb{E}[Y]-\mathbb{E}[X Y]}{(1-\mathbb{E}[X]) \mathbb{E}[Y]} \\
& +(1-\mathbb{E}[X]-\mathbb{E}[Y]+\mathbb{E}[X Y]) \cdot \log \frac{1-\mathbb{E}[X]-\mathbb{E}[Y]+\mathbb{E}[X Y]}{(1-\mathbb{E}[X])(1-\mathbb{E}[Y])} \\
= & f(\mathbb{E}[X], \mathbb{E}[Y], \mathbb{E}[X Y])
\end{aligned}
$$

for $f$ defined by $f(x, y, z) \stackrel{\text { def }}{=} z \log \frac{z}{x y}+(x-z) \log \frac{x-z}{x(1-y)}+(y-z) \log \frac{y-z}{(1-x) y}+(1-x-y+$ $z) \log \frac{1-x-y+z}{(1-x)(1-y)}$.

The domain of definition of $f$ is the subset $\Omega \subseteq[0,1]^{3}$ defined by (recalling that $x, y, z$ correspond to $\mathbb{E}[X], \mathbb{E}[Y], \mathbb{E}[X Y]$ for $\left.X, Y \in\{0,1\}\right)$

$$
\begin{aligned}
& 0 \leq x, y \leq 1 \\
& 0 \leq z \leq \min (x, y) \\
& 0 \leq z \leq \sqrt{x y} \\
& 0 \leq 1+z-x-y
\end{aligned}
$$

Given the $c$-balancedness assumption on $P, \Omega_{c} \subseteq \Omega$ satisfies the further following constraints:

$$
\begin{aligned}
c & \leq x, y \leq 1-c \\
c^{2} & \leq \frac{z}{x}, \frac{z}{y} \leq 1-c^{2} \\
c^{2} & \leq \frac{1+z-x-y}{1-x}, \frac{1+z-x-y}{1-y} \leq 1-c^{2}
\end{aligned}
$$

by Baye's rule and recalling that $1+z-x-y$ corresponds to the three (equal) quantities $\operatorname{Pr}[X=0, Y=0]$, $\operatorname{Pr}[X=0 \mid Y=0] \operatorname{Pr}[Y=0], \operatorname{Pr}[Y=0 \mid X=0] \operatorname{Pr}[X=0]$; while $1-x, 1-y$ correspond to $\operatorname{Pr}[X=0], \operatorname{Pr}[Y=0]$ respectively.
One can then check that

$$
\begin{aligned}
& \frac{\partial f}{\partial x}(x, y, z)=\log \frac{(1-x)(x-z)}{x(1+z-x-y)} \\
& \frac{\partial f}{\partial y}(x, y, z)=\log \frac{(1-y)(y-z)}{y(1+z-x-y)} \\
& \frac{\partial f}{\partial z}(x, y, z)=\log \frac{z(1+z-x-y)}{(x-z)(y-z)}
\end{aligned}
$$

and therefore, on $\Omega_{c}$, that

$$
\begin{aligned}
\left\|\frac{\partial f}{\partial x}\right\|_{\infty} & =\left\|\frac{\partial f}{\partial y}\right\|_{\infty} \\
& \leq \sup _{(x, y, z) \in \Omega_{c}}\left|\log \frac{x-z}{x}\right|+\left|\log \frac{1+z-x-y}{1-x}\right| \\
& \leq 2 \log \frac{1}{c^{2}}=4 \log \frac{1}{c}
\end{aligned}
$$

Similarly,

$$
\begin{aligned}
\left\|\frac{\partial f}{\partial z}\right\|_{\infty} & \leq \sup _{(x, y, z) \in \Omega_{c}}\left|\log \frac{(x-z)(y-z)}{z}\right|+|\log (1+z-x-y)| \\
& \leq \sup _{(x, y, z) \in \Omega_{c}}\left|\log \frac{\left(1-c^{2}\right) y}{c^{4} x y}\right|+\left|\log \frac{1}{c^{2} x}\right| \\
& \leq \log \frac{1}{c^{5}}+\log \frac{1}{c^{3}}=8 \log \frac{1}{c}
\end{aligned}
$$

So overall, $f$ is $\lambda$-Lipschitz (with regard to the $\|\cdot\|_{\infty}$ norm) on $\Omega_{c}$, for $\lambda=\left\|\frac{\partial f}{\partial x}\right\|_{\infty}+\left\|\frac{\partial f}{\partial y}\right\|_{\infty}+\left\|\frac{\partial f}{\partial z}\right\|_{\infty} \leq$ $16 \log \frac{1}{c}$.