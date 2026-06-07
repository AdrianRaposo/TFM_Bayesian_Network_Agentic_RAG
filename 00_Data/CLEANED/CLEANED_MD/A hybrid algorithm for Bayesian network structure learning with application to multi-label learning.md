# A hybrid algorithm for Bayesian network structure learning with application to multi-label learning 

Maxime Gasse, Alex Aussem*, Haytham Elghazel<br>Université de Lyon, CNRS<br>Université Lyon 1, LIRIS, UMR5205, F-69622, France


#### Abstract

We present a novel hybrid algorithm for Bayesian network structure learning, called H2PC. It first reconstructs the skeleton of a Bayesian network and then performs a Bayesian-scoring greedy hill-climbing search to orient the edges. The algorithm is based on divide-and-conquer constraint-based subroutines to learn the local structure around a target variable. We conduct two series of experimental comparisons of H2PC against Max-Min Hill-Climbing (MMHC), which is currently the most powerful state-of-the-art algorithm for Bayesian network structure learning. First, we use eight well-known Bayesian network benchmarks with various data sizes to assess the quality of the learned structure returned by the algorithms. Our extensive experiments show that H2PC outperforms MMHC in terms of goodness of fit to new data and quality of the network structure with respect to the true dependence structure of the data. Second, we investigate H2PC's ability to solve the multi-label learning problem. We provide theoretical results to characterize and identify graphically the so-called minimal label powersets that appear as irreducible factors in the joint distribution under the faithfulness condition. The multi-label learning problem is then decomposed into a series of multi-class classification problems, where each multi-class variable encodes a label powerset. H2PC is shown to compare favorably to MMHC in terms of global classification accuracy over ten multi-label data sets covering different application domains. Overall, our experiments support the conclusions that local structural learning with H2PC in the form of local neighborhood induction is a theoretically well-motivated and empirically effective learning framework that is well suited to multi-label learning. The source code (in $R$ ) of H2PC as well as all data sets used for the empirical tests are publicly available.


Keywords: Bayesian networks, Multi-label learning, Markov boundary, Feature subset selection.

## 1. Introduction

A Bayesian network (BN) is a probabilistic model formed by a structure and parameters. The structure of a BN is a directed acyclic graph (DAG), whilst its parameters are conditional probability distributions associated with the variables in the model. The problem of finding the DAG that encodes the conditional independencies present in the data attracted a great deal of interest over the last years (Rodrigues de Morais \& Aussem, 2010a; Scutari, 2010; Scutari \& Brogini, 2012; Kojima et al., 2010; Perrier et al., 2008; Villanueva \& Maciel, 2012; Peña, 2012; Gasse et al., 2012). The inferred DAG is very useful for many applications,

[^0]including feature selection (Aliferis et al., 2010; Peña et al., 2007; Rodrigues de Morais \& Aussem, 2010b), causal relationships inference from observational data (Ellis \& Wong, 2008; Aliferis et al., 2010; Aussem et al., 2012, 2010; Prestat et al., 2013; Cawley, 2008; Brown \& Tsamardinos, 2008) and more recently multi-label learning (DembczyÂski et al., 2012; Zhang \& Zhang, 2010; Guo \& Gu, 2011).

Ideally the DAG should coincide with the dependence structure of the global distribution, or it should at least identify a distribution as close as possible to the correct one in the probability space. This step, called structure learning, is similar in approaches and terminology to model selection procedures for classical statistical models. Basically, constraint-based (CB) learning methods systematically check the data for conditional independence relationships and use them as constraints to con-


[^0]:    *Corresponding author
    Email address: aaussem@univ-lyon1.fr (Alex Aussem)

struct a partially oriented graph representative of a BN equivalence class, whilst search-and-score (SS) methods make use of a goodness-of-fit score function for evaluating graphical structures with regard to the data set. Hybrid methods attempt to get the best of both worlds: they learn a skeleton with a CB approach and constrain on the DAGs considered during the SS phase.

In this study, we present a novel hybrid algorithm for Bayesian network structure learning, called H2PC ${ }^{1}$. It first reconstructs the skeleton of a Bayesian network and then performs a Bayesian-scoring greedy hillclimbing search to orient the edges. The algorithm is based on divide-and-conquer constraint-based subroutines to learn the local structure around a target variable. HPC may be thought of as a way to compensate for the large number of false negatives at the output of the weak PC learner, by performing extra computations. As this may arise at the expense of the number of false positives, we control the expected proportion of false discoveries (i.e. false positive nodes) among all the discoveries made in $\mathbf{P C}_{T}$. We use a modification of the Incremental association Markov boundary algorithm (IAMB), initially developed by Tsamardinos et al. in (Tsamardinos et al., 2003) and later modified by Jose Peña in (Peña, 2008) to control the FDR of edges when learning Bayesian network models. HPC scales to thousands of variables and can deal with many fewer samples $(n<q)$. To illustrate its performance by means of empirical evidence, we conduct two series of experimental comparisons of H2PC against Max-Min HillClimbing (MMHC), which is currently the most powerful state-of-the-art algorithm for BN structure learning (Tsamardinos et al., 2006), using well-known BN benchmarks with various data sizes, to assess the goodness of fit to new data as well as the quality of the network structure with respect to the true dependence structure of the data.

We then address a real application of H2PC where the true dependence structure is unknown. More specifically, we investigate H2PC's ability to encode the joint distribution of the label set conditioned on the input features in the multi-label classification (MLC) problem. Many challenging applications, such as photo and video annotation and web page categorization, can benefit from being formulated as MLC tasks with large number of categories (DembczyÂski et al., 2012; Read et al., 2009; Madjarov et al., 2012; Kocev et al., 2007; Tsoumakas et al., 2010b). Recent research in

[^0]MLC focuses on the exploitation of the label conditional dependency in order to better predict the label combination for each example. We show that local BN structure discovery methods offer an elegant and powerful approach to solve this problem. We establish two theorems (Theorem 6 and 7) linking the concepts of marginal Markov boundaries, joint Markov boundaries and so-called label powersets under the faithfulness assumption. These Theorems offer a simple guideline to characterize graphically : i) the minimal label powerset decomposition, (i.e. into minimal subsets $\mathbf{Y}_{L P} \subseteq \mathbf{Y}$ such that $\mathbf{Y}_{L P} \perp \mathbf{Y} \backslash \mathbf{Y}_{L P} \mid \mathbf{X}$ ), and ii) the minimal subset of features, w.r.t an Information Theory criterion, needed to predict each label powerset, thereby reducing the input space and the computational burden of the multilabel classification. To solve the MLC problem with BNs, the DAG obtained from the data plays a pivotal role. So in this second series of experiments, we assess the comparative ability of H 2 PC and MMHC to encode the label dependency structure by means of an indirect goodness of fit indicator, namely the $0 / 1$ loss function, which makes sense in the MLC context.

The rest of the paper is organized as follows: In the Section 2, we review the theory of BN and discuss the main BN structure learning strategies. We then present the H2PC algorithm in details in Section 3. Section 4 evaluates our proposed method and shows results for several tasks involving artificial data sampled from known BNs. Then we report, in Section 5, on our experiments on real-world data sets in a multi-label learning context so as to provide empirical support for the proposed methodology. The main theoretical results appear formally as two theorems (Theorem 8 and 9) in Section 5. Their proofs are established in the Appendix. Finally, Section 6 raises several issues for future work and we conclude in Section 7 with a summary of our contribution.

## 2. Preliminaries

We define next some key concepts used along the paper and state some results that will support our analysis. In this paper, upper-case letters in italics denote random variables (e.g., $X, Y$ ) and lower-case letters in italics denote their values (e.g., $x, y$ ). Upper-case bold letters denote random variable sets (e.g., $\mathbf{X}, \mathbf{Y}, \mathbf{Z}$ ) and lower-case bold letters denote their values (e.g., $\mathbf{x}, \mathbf{y}$ ). We denote by $\mathbf{X} \perp \mathbf{Y} \mid \mathbf{Z}$ the conditional independence between $\mathbf{X}$ and $\mathbf{Y}$ given the set of variables $\mathbf{Z}$. To keep the notation uncluttered, we use $p(\mathbf{y} \mid \mathbf{x})$ to denote $p(\mathbf{Y}=\mathbf{y} \mid \mathbf{X}=\mathbf{x})$.


[^0]:    ${ }^{1}$ A first version of HP2C without FDR control has been discussed in a paper that appeared in the Proceedings of ECML-PKDD, pages $58-73,2012$.

### 2.1. Bayesian networks

Formally, a BN is a tuple $<\mathcal{G}, P>$, where $\mathcal{G}=<$ $\mathbf{U}, \mathbf{E}>$ is a directed acyclic graph (DAG) with nodes representing the random variables $\mathbf{U}$ and $P$ a joint probability distribution in $\mathcal{U}$. In addition, $\mathcal{G}$ and $P$ must satisfy the Markov condition: every variable, $X \in \mathbf{U}$, is independent of any subset of its non-descendant variables conditioned on the set of its parents, denoted by $\mathbf{P a}_{i}^{\mathcal{G}}$. From the Markov condition, it is easy to prove (Neapolitan, 2004) that the joint probability distribution $P$ on the variables in $\mathbf{U}$ can be factored as follows :

$$
P(\mathcal{V})=P\left(X_{1}, \ldots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid \mathbf{P a}_{i}^{\mathcal{G}}\right)
$$

Equation 1 allows a parsimonious decomposition of the joint distribution $P$. It enables us to reduce the problem of determining a huge number of probability values to that of determining relatively few.

A BN structure $\mathcal{G}$ entails a set of conditional independence assumptions. They can all be identified by the $d$ separation criterion (Pearl, 1988). We use $X \perp_{\mathcal{G}} Y \mid \mathbf{Z}$ to denote the assertion that $X$ is d-separated from $Y$ given $\mathbf{Z}$ in $\mathcal{G}$. Formally, $X \perp_{\mathcal{G}} Y \mid \mathbf{Z}$ is true when for every undirected path in $\mathcal{G}$ between $X$ and $Y$, there exists a node $W$ in the path such that either (1) $W$ does not have two parents in the path and $W \in \mathbf{Z}$, or (2) $W$ has two parents in the path and neither $W$ nor its descendants is in $\mathbf{Z}$. If $<\mathcal{G}, P>$ is a $\mathrm{BN}, X \perp_{P} Y \mid \mathbf{Z}$ if $X \perp_{\mathcal{G}} Y \mid \mathbf{Z}$. The converse does not necessarily hold. We say that $<\mathcal{G}, P>$ satisfies the faithfulness condition if the d-separations in $\mathcal{G}$ identify all and only the conditional independencies in $P$, i.e., $X \perp_{P} Y \mid \mathbf{Z}$ iff $X \perp_{\mathcal{G}} Y \mid \mathbf{Z}$.

A Markov blanket $\mathbf{M}_{T}$ of $T$ is any set of variables such that $T$ is conditionally independent of all the remaining variables given $\mathbf{M}_{T}$. By extension, a Markov blanket of $T$ in $\mathbf{V}$ guarantees that $\mathbf{M}_{T} \subseteq \mathbf{V}$, and that $T$ is conditionally independent of the remaining variables in $\mathbf{V}$, given $\mathbf{M}_{T}$. A Markov boundary, $\mathbf{M B}_{T}$, of $T$ is any Markov blanket such that none of its proper subsets is a Markov blanket of $T$.

We denote by $\mathbf{P C}_{T}^{\mathcal{G}}$, the set of parents and children of $T$ in $\mathcal{G}$, and by $\mathbf{S P}_{T}^{\mathcal{G}}$, the set of spouses of $T$ in $\mathcal{G}$. The spouses of $T$ are the variables that have common children with $T$. These sets are unique for all $\mathcal{G}$, such that $<\mathcal{G}, P>$ satisfies the faithfulness condition and so we will drop the superscript $\mathcal{G}$. We denote by $\mathbf{d S e p}(X)$, the set that d-separates $X$ from the (implicit) target $T$.
Theorem 1. Suppose $<\mathcal{G}, P>$ satisfies the faithfulness condition. Then $X$ and $Y$ are not adjacent in $\mathcal{G}$ iff $\exists \mathbf{Z} \in$ $\mathbf{U} \backslash\{X, Y\}$ such that $X \perp Y \mid \mathbf{Z}$. Moreover, $\mathbf{M B}_{X}=$ $\mathbf{P C}_{X} \cup \mathbf{S P}_{X}$.

A proof can be found for instance in (Neapolitan, 2004).

Two graphs are said equivalent iff they encode the same set of conditional independencies via the dseparation criterion. The equivalence class of a DAG $\mathcal{G}$ is a set of DAGs that are equivalent to $\mathcal{G}$. The next result showed by (Pearl, 1988), establishes that equivalent graphs have the same undirected graph but might disagree on the direction of some of the arcs.

Theorem 2. Two DAGs are equivalent iff they have the same underlying undirected graph and the same set of $v$-structures (i.e. converging edges into the same node, such as $X \rightarrow Y \leftarrow Z$ ).

Moreover, an equivalence class of network structures can be uniquely represented by a partially directed DAG (PDAG), also called a DAG pattern. The DAG pattern is defined as the graph that has the same links as the DAGs in the equivalence class and has oriented all and only the edges common to the DAGs in the equivalence class. A structure learning algorithm from data is said to be correct (or sound) if it returns the correct DAG pattern (or a DAG in the correct equivalence class) under the assumptions that the independence tests are reliable and that the learning database is a sample from a distribution $P$ faithful to a DAG $\mathcal{G}$, The (ideal) assumption that the independence tests are reliable means that they decide (in)dependence iff the (in)dependence holds in $P$.

### 2.2. Conditional independence properties

The following three theorems, borrowed from Peña et al. (2007), are proven in Pearl (1988):

Theorem 3. Let $\mathbf{X}, \mathbf{Y}, \mathbf{Z}$ and $\mathbf{W}$ denote four mutually disjoint subsets of $\mathbf{U}$. Any probability distribution $p$ satisfies the following four properties: Symmetry $\mathbf{X} \perp \mathbf{Y} \mid \mathbf{Z} \Rightarrow \mathbf{Y} \perp \mathbf{X} \mid \mathbf{Z}$, Decomposition, $\mathbf{X} \perp(\mathbf{Y} \cup \mathbf{W}) \mid \mathbf{Z} \Rightarrow \mathbf{X} \perp \mathbf{Y} \mid \mathbf{Z}$, Weak Union $\mathbf{X} \perp(\mathbf{Y} \cup \mathbf{W}) \mid \mathbf{Z} \Rightarrow \mathbf{X} \perp \mathbf{Y} \mid(\mathbf{Z} \cup \mathbf{W})$ and Contraction, $\mathbf{X} \perp \mathbf{Y} \mid(\mathbf{Z} \cup \mathbf{W}) \wedge \mathbf{X} \perp \mathbf{W} \mid \mathbf{Z} \Rightarrow \mathbf{X} \perp(\mathbf{Y} \cup \mathbf{W}) \mid \mathbf{Z}$.

Theorem 4. If $p$ is strictly positive, then $p$ satisfies the previous four properties plus the Intersection property $\mathbf{X} \perp \mathbf{Y} \mid(\mathbf{Z} \cup \mathbf{W}) \wedge \mathbf{X} \perp \mathbf{W} \mid(\mathbf{Z} \cup \mathbf{Y}) \Rightarrow \mathbf{X} \perp(\mathbf{Y} \cup$ $\mathbf{W}) \mid \mathbf{Z}$. Additionally, each $\mathbf{X} \in \mathbf{U}$ has a unique Markov boundary, $\mathbf{M B}_{\mathbf{X}}$

Theorem 5. If $p$ is faithful to a DAG $\mathcal{G}$, then $p$ satisfies the previous five properties plus the Composition property $\mathbf{X} \perp \mathbf{Y} \mid \mathbf{Z} \wedge \mathbf{X} \perp \mathbf{W} \mid \mathbf{Z} \Rightarrow \mathbf{X} \perp(\mathbf{Y} \cup \mathbf{W}) \mid \mathbf{Z}$ and the local Markov property $X \perp\left(\mathbf{N D}_{X} \backslash \mathbf{P a}_{X}\right) \mid \mathbf{P a}_{X}$ for each $X \in \mathbf{U}$, where $\mathbf{N D}_{X}$ denotes the non-descendants of $X$ in $\mathcal{G}$.

### 2.3. Structure learning strategies

The number of DAGs, $\mathbb{G}$, is super-exponential in the number of random variables in the domain and the problem of learning the most probable a posteriori BN from data is worst-case NP-hard (Chickering et al., 2004). One needs to resort to heuristical methods in order to be able to solve very large problems effectively.

Both CB and SS heuristic approaches have advantages and disadvantages. CB approaches are relatively quick, deterministic, and have a well defined stopping criterion; however, they rely on an arbitrary significance level to test for independence, and they can be unstable in the sense that an error early on in the search can have a cascading effect that causes many errors to be present in the final graph. SS approaches have the advantage of being able to flexibly incorporate users' background knowledge in the form of prior probabilities over the structures and are also capable of dealing with incomplete records in the database (e.g. EM technique). Although SS methods are favored in practice when dealing with small dimensional data sets, they are slow to converge and the computational complexity often prevents us from finding optimal BN structures (Perrier et al., 2008; Kojima et al., 2010). With currently available exact algorithms (Koivisto \& Sood, 2004; Silander \& Myllymäki, 2006; Cussens \& Bartlett, 2013; Studený \& Haws, 2014) and a decomposable score like BDeu, the computational complexity remains exponential, and therefore, such algorithms are intractable for BNs with more than around 30 vertices on current workstations. For larger sets of variables the computational burden becomes prohibitive and restrictions about the structure have to be imposed, such as a limit on the size of the parent sets. With this in mind, the ability to restrict the search locally around the target variable is a key advantage of CB methods over SS methods. They are able to construct a local graph around the target node without having to construct the whole BN first, hence their scalability (Peña et al., 2007; Rodrigues de Morais \& Aussem, 2010b,a; Tsamardinos et al., 2006; Peña, 2008).

With a view to balancing the computation cost with the desired accuracy of the estimates, several hybrid methods have been proposed recently. Tsamardinos et al. proposed in (Tsamardinos et al., 2006) the MinMax Hill Climbing (MMHC) algorithm and conducted one of the most extensive empirical comparison performed in recent years showing that MMHC was the fastest and the most accurate method in terms of structural error based on the structural hamming distance. More specifically, MMHC outperformed both
in terms of time efficiency and quality of reconstruction the PC (Spirtes et al., 2000), the Sparse Candidate (Friedman et al., 1999b), the Three Phase Dependency Analysis (Cheng et al., 2002), the Optimal Reinsertion (Moore \& Wong, 2003), the Greedy Equivalence Search (Chickering, 2002), and the Greedy HillClimbing Search on a variety of networks, sample sizes, and parameter values. Although MMHC is rather heuristic by nature (it returns a local optimum of the score function), it is currently considered as the most powerful state-of-the-art algorithm for BN structure learning capable of dealing with thousands of nodes in reasonable time.

In order to enhance its performance on small dimensional data sets, Perrier et al. proposed in (Perrier et al., 2008) a hybrid algorithm that can learn an optimal BN (i.e., it converges to the true model in the sample limit) when an undirected graph is given as a structural constraint. They defined this undirected graph as a superstructure (i.e., every DAG considered in the SS phase is compelled to be a subgraph of the super-structure). This algorithm can learn optimal BNs containing up to 50 vertices when the average degree of the super-structure is around two, that is, a sparse structural constraint is assumed. To extend its feasibility to BN with a few hundred of vertices and an average degree up to four, Kojima et al. proposed in (Kojima et al., 2010) to divide the super-structure into several clusters and perform an optimal search on each of them in order to scale up to larger networks. Despite interesting improvements in terms of score and structural hamming distance on several benchmark BNs, they report running times about $10^{3}$ times longer than MMHC on average, which is still prohibitive.

Therefore, there is great deal of interest in hybrid methods capable of improving the structural accuracy of both CB and SS methods on graphs containing up to thousands of vertices. However, they make the strong assumption that the skeleton (also called super-structure) contains at least the edges of the true network and as small as possible extra edges. While controlling the false discovery rate (i.e., false extra edges) in BN learning has attracted some attention recently (Armen \& Tsamardinos, 2011; Peña, 2008; Tsamardinos \& Brown, 2008), to our knowledge, there is no work on controlling actively the rate of falsenegative errors (i.e., false missing edges).

### 2.4. Constraint-based structure learning

Before introducing the H2PC algorithm, we discuss the general idea behind CB methods. The induction of local or global BN structures is handled by CB methods

through the identification of local neighborhoods (i.e., $\mathbf{P C}_{X}$ ), hence their scalability to very high dimensional data sets. CB methods systematically check the data for conditional independence relationships in order to infer a target's neighborhood. Typically, the algorithms run either a $G^{2}$ or a $\chi^{2}$ independence test when the data set is discrete and a Fisher's Z test when it is continuous in order to decide on dependence or independence, that is, upon the rejection or acceptance of the null hypothesis of conditional independence. Since we are limiting ourselves to discrete data, both the global and the local distributions are assumed to be multinomial, and the latter are represented as conditional probability tables. Conditional independence tests and network scores for discrete data are functions of these conditional probability tables through the observed frequencies $\left\{n_{i j k} ; i=1, \ldots, R ; j=1, \ldots, C ; k=1, \ldots, L\right\}$ for the random variables $X$ and $Y$ and all the configurations of the levels of the conditioning variables $\mathbf{Z}$. We use $n_{i+k}$ as shorthand for the marginal $\sum_{j} n_{i j k}$ and similarly for $n_{i+k}, n_{++k}$ and $n_{+++}=n$. We use a classic conditional independence test based on the mutual information. The mutual information is an information-theoretic distance measure defined as

$$
M I(X, Y \mid \mathbf{Z})=\sum_{i=1}^{R} \sum_{j=1}^{C} \sum_{k=1}^{L} \frac{n_{i j k}}{n} \log \frac{n_{i j k} n_{++k}}{n_{i+k} n_{+j k}}
$$

It is proportional to the log-likelihood ratio test $G^{2}$ (they differ by a 2 n factor, where n is the sample size). The asymptotic null distribution is $\chi^{2}$ with $(R-1)(C-1) L$ degrees of freedom. For a detailed analysis of their properties we refer the reader to (Agresti, 2002). The main limitation of this test is the rate of convergence to its limiting distribution, which is particularly problematic when dealing with small samples and sparse contingency tables. The decision of accepting or rejecting the null hypothesis depends implicitly upon the degree of freedom which increases exponentially with the number of variables in the conditional set. Several heuristic solutions have emerged in the literature (Spirtes et al., 2000; Rodrigues de Morais \& Aussem, 2010a; Tsamardinos et al., 2006; Tsamardinos \& Borboudakis, 2010) to overcome some shortcomings of the asymptotic tests. In this study we use the two following heuristics that are used in MMHC. First, we do not perform $M I(X, Y \mid \mathbf{Z})$ and assume independence if there are not enough samples to achieve large enough power. We require that the average sample per count is above a user defined parameter, equal to 5 , as in
(Tsamardinos et al., 2006). This heuristic is called the power rule. Second, we consider as structural zero either case $n_{+j k}$ or $n_{i+k}=0$. For example, if $n_{+j k}=0$, we consider y as a structurally forbidden value for Y when $\mathrm{Z}=\mathrm{z}$ and we reduce R by 1 (as if we had one column less in the contingency table where $\mathrm{Z}=\mathrm{z}$ ). This is known as the degrees of freedom adjustment heuristic.

## 3. The H2PC algorithm

In this section, we present our hybrid algorithm for Bayesian network structure learning, called Hybrid HPC (H2PC). It first reconstructs the skeleton of a Bayesian network and then performs a Bayesianscoring greedy hill-climbing search to filter and orient the edges. It is based on a CB subroutine called HPC to learn the parents and children of a single variable. So, we shall discuss HPC first and then move to H2PC.

### 3.1. Parents and Children Discovery

HPC (Algorithm 1) can be viewed as an ensemble method for combining many weak PC learners in an attempt to produce a stronger PC learner. HPC is based on three subroutines: Data-Efficient Parents and Children Superset (DE-PCS), Data-Efficient Spouses Superset (DE-SPS), and Incremental Association Parents and Children with false discovery rate control (FDR-IAPC), a weak PC learner based on FDR-IAMB (Peña, 2008) that requires little computation. HPC receives a target node $T$, a data set $\mathcal{D}$ and a set of variables $\mathbf{U}$ as input and returns an estimation of $\mathbf{P C}_{T}$. It is hybrid in that it combines the benefits of incremental and divide-andconquer methods. The procedure starts by extracting a superset $\mathbf{P C S}_{T}$ of $\mathbf{P C}_{T}$ (line 1) and a superset $\mathbf{S P S}_{T}$ of $\mathbf{S P}_{T}$ (line 2) with a severe restriction on the maximum conditioning size $(\mathbf{Z}<=2)$ in order to significantly increase the reliability of the tests. A first candidate PC set is then obtained by running the weak PC learner called FDR-IAPC on $\mathbf{P C S}_{T} \cup \mathbf{S P S}_{T}$ (line 3). The key idea is the decentralized search at lines 4-8 that includes, in the candidate PC set, all variables in the superset $\mathbf{P C S}_{T} \backslash \mathbf{P C}_{T}$ that have $T$ in their vicinity. So, HPC may be thought of as a way to compensate for the large number of false negatives at the output of the weak PC learner, by performing extra computations. Note that, in theory, $X$ is in the output of FDR-IAPC $(Y)$ if and only if $Y$ is in the output of FDR-IAPC $(X)$. However, in practice, this may not always be true, particularly when working in high-dimensional domains (Peña, 2008). By loosening the criteria by which two nodes are

said adjacent, the effective restrictions on the size of the neighborhood are now far less severe. The decentralized search has a significant impact on the accuracy of HPC as we shall see in in the experiments. We proved in (Rodrigues de Morais \& Aussem, 2010a) that the original $\mathrm{HPC}(\mathrm{T})$ is consistent, i.e. its output converges in probability to $\mathbf{P C}_{T}$, if the hypothesis tests are consistent. The proof also applies to the modified version presented here.

We now discuss the subroutines in more detail. FDRIAPC (Algorithm 2) is a fast incremental method that receives a data set $\mathcal{D}$ and a target node $T$ as its input and promptly returns a rough estimation of $\mathbf{P C}_{T}$, hence the term "weak" PC learner. In this study, we use FDR-IAPC because it aims at controlling the expected proportion of false discoveries (i.e., false positive nodes in $\mathbf{P C}_{T}$ ) among all the discoveries made. FDR-IAPC is a straightforward extension of the algorithm IAMBFDR developed by Jose Peña in (Peña, 2008), which is itself a modification of the incremental association Markov boundary algorithm (IAMB) (Tsamardinos et al., 2003), to control the expected proportion of false discoveries (i.e., false positive nodes) in the estimated Markov boundary. FDR-IAPC simply removes, at lines 3-6, the spouses $\mathbf{S P}_{T}$ from the estimated Markov boundary $\mathbf{M B}_{T}$ output by IAMBFDR at line 1, and returns $\mathbf{P C}_{T}$ assuming the faithfulness condition.

The subroutines DE-PCS (Algorithm 3) and DE-SPS (Algorithm 4) search a superset of $\mathbf{P C}_{T}$ and $\mathbf{S P}_{T}$ respectively with a severe restriction on the maximum conditioning size $(|\mathbf{Z}|<=1$ in DE-PCS and $|\mathbf{Z}|<=2$ in DESPS) in order to significantly increase the reliability of the tests. The variable filtering has two advantages : i) it allows HPC to scale to hundreds of thousands of variables by restricting the search to a subset of relevant variables, and ii) it eliminates many true or approximate deterministic relationships that produce many false negative errors in the output of the algorithm, as explained in (Rodrigues de Morais \& Aussem, 2010b,a). DE-SPS works in two steps. First, a growing phase (lines 4-8) adds the variables that are d-separated from the target but still remain associated with the target when conditioned on another variable from $\mathbf{P C S}_{T}$. The shrinking phase (lines 9-16) discards irrelevant variables that are ancestors or descendants of a target's spouse. Pruning such irrelevant variables speeds up HPC.

### 3.2. Hybrid HPC (H2PC)

In this section, we discuss the SS phase. The following discussion draws strongly on (Tsamardinos et al., 2006) as the SS phase in Hybrid HPC and MMHC are exactly the same. The idea of constraining the search

## Algorithm $1 H P C$

Require: $T$ : target; $\mathcal{D}$ : data set; $\mathbf{U}$ : set of variables
Ensure: $\mathbf{P C}_{T}$ : Parents and Children of $T$
$1:\left\{\mathbf{P C S}_{T}, \mathbf{d S e p}\right\} \leftarrow D E-P C S(T, \mathcal{D}, \mathbf{U})$
$2: \mathbf{S P S}_{T} \leftarrow D E-S P S(T, \mathcal{D}, \mathbf{U}, \mathbf{P C S}_{T}, \mathbf{d S e p})$
$3: \mathbf{P C}_{T} \leftarrow F D R-I A P C\left(T, \mathcal{D},\left(T \cup \mathbf{P C S}_{T} \cup \mathbf{S P S}_{T}\right)\right)$
4: for all $X \in \mathbf{P C S}_{T} \backslash \mathbf{P C}_{T}$ do
5: if $T \in F D R-I A P C(X, \mathcal{D},\left(T \cup \mathbf{P C S}_{T} \cup \mathbf{S P S}_{T}\right)$ ) then
6: $\quad \mathbf{P C}_{T} \leftarrow \mathbf{P C}_{T} \cup X$
7: end if
8: end for

## Algorithm 2 FDR-IAPC

Require: $T$ : target; $D$ : data set; $\mathbf{U}$ : set of variables
Ensure: $\mathbf{P C}_{T}$ : Parents and children of $T$;

* Learn the Markov boundary of $T$
$1: \mathbf{M B}_{T} \leftarrow I A M B F D R(X, \mathcal{D}, \mathbf{U})$
* Remove spouses of $T$ from $\mathbf{M B}_{T}$
$2: \mathbf{P C}_{T} \leftarrow \mathbf{M B}_{T}$
3: for all $X \in \mathbf{M B}_{T}$ do
4: if $\exists \mathbf{Z} \subseteq\left(\mathbf{M B}_{T} \backslash X\right)$ such that $T \perp X \mid \mathbf{Z}$ then
5: $\quad \mathbf{P C}_{T} \leftarrow \mathbf{P C}_{T} \backslash X$
6: end if
7: end for

Algorithm 3 DE-PCS
Require: $T$ : target; $\mathcal{D}$ : data set; $\mathbf{U}$ : set of variables;
Ensure: $\mathbf{P C S}_{T}$ : parents and children superset of $T$; dSep: dseparating sets;

```
Phase I: Remove \(X\) if \(T \perp X\)
\(1: \mathbf{P C S}_{T} \leftarrow \mathbf{U} \backslash T\)
2: for all \(X \in \mathbf{P C S}_{T}\) do
    if \((T \perp X)\) then
        \(\mathbf{P C S}_{T} \leftarrow \mathbf{P C S}_{T} \backslash X\)
        \(\mathbf{d S e p}(X) \leftarrow \emptyset\)
    end if
end for
```

```
Phase II: Remove \(X\) if \(T \perp X \mid Y\)
8: for all \(X \in \mathbf{P C S}_{T}\) do
    for all \(Y \in \mathbf{P C S}_{T} \backslash X\) do
        if \((T \perp X \mid Y)\) then
            \(\mathbf{P C S}_{T} \leftarrow \mathbf{P C S}_{T} \backslash X\)
            \(\mathbf{d S e p}(X) \leftarrow Y\)
            break loop FOR
            end if
        end for
```

```
end for
```

```
Algorithm 4 DE-SPS
Require: \(T\) : target; \(\mathcal{D}:\) data set; \(\mathbf{U}:\) the set of variables;
    \(\mathbf{P C S}_{T}\) : parents and children superset of \(T ; \mathbf{d S e p}:\) d-
    separating sets;
Ensure: \(\mathbf{S P S}_{T}\) : Superset of the spouses of \(T\);
    \(\mathbf{S P S}_{T} \leftarrow \emptyset\)
    for all \(X \in \mathbf{P C S}_{T}\) do
        \(\mathbf{S P S}_{T}^{2} \leftarrow \emptyset\)
        for all \(Y \in \mathbf{U} \backslash\left\{T \cup \mathbf{P C S}_{T}\right\}\) do
            if \((T \perp Y) \mathbf{d S e p}(Y) \cup X)\) then
                \(\mathbf{S P S}_{T}^{2} \leftarrow \mathbf{S P S}_{T}^{2} \cup Y\)
            end if
            end for
            for all \(Y \in \mathbf{S P S}_{T}^{2}\) do
            for all \(Z \in \mathbf{S P S}_{T}^{2} \backslash Y\) do
                if \((T \perp Y \mid X \cup Z)\) then
                    \(\mathbf{S P S}_{T}^{2} \leftarrow \mathbf{S P S}_{T}^{2} \backslash Y\)
                    break loop FOR
                    end if
            end for
        end for
        \(\mathbf{S P S}_{T} \leftarrow \mathbf{S P S}_{T} \cup \mathbf{S P S}_{T}^{2}\)
    end for
Algorithm 5 Hybrid HPC
Require: \(\mathcal{D}\) : data set; \(\mathbf{U}\) : set of variables
Ensure: A DAG \(\mathcal{G}\) on the variables \(\mathbf{U}\)
    for all pair of nodes \(X, Y \in \mathbf{U}\) do
        Add X in \(\mathbf{P C}_{Y}\) and Add Y in \(\mathbf{P C}_{X}\) if \(X \in H P C(Y)\) and
        \(Y \in H P C(X)\)
    end for
    Starting from an empty graph, perform greedy hill-
    climbing with operators add-edge, delete-edge, reverse-
    edge. Only try operator add-edge \(X \rightarrow Y\) if \(Y \in \mathbf{P C}_{X}\)
```

to improve time-efficiency first appeared in the Sparse Candidate algorithm (Friedman et al., 1999b). It results in efficiency improvements over the (unconstrained) greedy search. All recent hybrid algorithms build on this idea, but employ a sound algorithm for identifying the candidate parent sets. The Hybrid HPC first identifies the parents and children set of each variable, then performs a greedy hill-climbing search in the space of BN. The search begins with an empty graph. The edge addition, deletion, or direction reversal that leads to the largest increase in score (the BDeu score with uniform prior was used) is taken and the search continues in a similar fashion recursively. The important difference from standard greedy search is that the search is constrained to only consider adding an edge if it was discovered by HPC in the first phase. We extend the greedy search with a TABU list (Friedman et al., 1999b). The list keeps the last 100 structures explored. Instead of applying the best local change, the best local change that results in a structure not on the list is performed in an attempt to escape local maxima. When 15 changes occur without an increase in the maximum score ever encountered during search, the algorithm terminates. The overall best scoring structure is then returned. Clearly, the more false positives the heuristic allows to enter candidate PC set, the more computational burden is imposed in the SS phase.

## 4. Experimental validation on synthetic data

Before we proceed to the experiments on real-world multi-label data with H 2 PC , we first conduct an experimental comparison of H 2 PC against MMHC on synthetic data sets sampled from eight well-known benchmarks with various data sizes in order to gauge the practical relevance of the H 2 PC . These BNs that have been previously used as benchmarks for BN learning algorithms (see Table 1 for details). Results are reported in terms of various performance indicators to investigate how well the network generalizes to new data and how well the learned dependence structure matches the true structure of the benchmark network. We implemented H 2 PC in $R$ (R Core Team, 2013) and integrated the code into the bnlearn package from (Scutari, 2010). MMHC was implemented by Marco Scutari in bnlearn. The source code of H 2 PC as well as all data sets used for the empirical tests are publicly available ${ }^{2}$. The threshold considered for the type I error of the test is 0.05 . Our experiments were carried out on PC with Intel(R)

[^0]
[^0]:    ${ }^{2}$ https://github.com/madbix/bnlearn-clone-3.4

Table 1: Description of the BN benchmarks used in the experiments.


$\operatorname{Core}(\mathrm{TM})$ i5-3470M CPU @3.20 GHz 4Go RAM running under Linux 64 bits.

We do not claim that those data sets resemble realworld problems, however, they make it possible to compare the outputs of the algorithms with the known structure. All BN benchmarks (structure and probability tables) were downloaded from the bnlearn repository ${ }^{3}$. Ten sample sizes have been considered: $50,100,200$, $500,1000,2000,5000,10000,20000$ and 50000. All experiments are repeated 10 times for each sample size and each BN. We investigate the behavior of both algorithms using the same parametric tests as a reference.

### 4.1. Performance indicators

We first investigate the quality of the skeleton returned by H 2 PC during the CB phase. To this end, we measure the false positive edge ratio, the precision (i.e., the number of true positive edges in the output divided by the number of edges in the output), the recall (i.e., the number of true positive edges divided the true number of edges) and a combination of precision and recall defined as $\sqrt{(1-\text { precision })^{2}+(1-\text { recall })^{2}}$, to measure the Euclidean distance from perfect precision and recall, as proposed in (Peña et al., 2007). Second, to assess the quality of the final DAG output at the end of the SS phase, we report the five performance indicators (Scutari \& Brogini, 2012) described below:

- the posterior density of the network for the data it was learned from, as a measure of goodness of fit. It is known as the Bayesian Dirichlet equivalent score (BDeu) from (Heckerman et al., 1995; Buntine, 1991) and has a single parameter, the equivalent sample size, which can be thought of as the size of an imaginary sample supporting the prior distribution. The equivalent sample size was set to 10 as suggested in (Koller \& Friedman, 2009);

[^0]- the BIC score (Schwarz, 1978) of the network for the data it was learned from, again as a measure of goodness of fit;
- the posterior density of the network for a new data set, as a measure of how well the network generalizes to new data;
- the BIC score of the network for a new data set, again as a measure of how well the network generalizes to new data;
- the Structural Hamming Distance (SHD) between the learned and the true structure of the network, as a measure of the quality of the learned dependence structure. The SHD between two PDAGs is defined as the number of the following operators required to make the PDAGs match: add or delete an undirected edge, and add, remove, or reverse the orientation of an edge.

For each data set sampled from the true probability distribution of the benchmark, we first learn a network structure with the H 2 PC and MMHC and then we compute the relevant performance indicators for each pair of network structures. The data set used to assess how well the network generalizes to new data is generated again from the true probability structure of the benchmark networks and contains 50000 observations.

Notice that using the BDeu score as a metric of reconstruction quality has the following two problems. First, the score corresponds to the a posteriori probability of a network only under certain conditions (e.g., a Dirichlet distribution of the hyper parameters); it is unknown to what degree these assumptions hold in distributions encountered in practice. Second, the score is highly sensitive to the equivalent sample size (set to 10 in our experiments) and depends on the network priors used. Since, typically, the same arbitrary value of this parameter is used both during learning and for scoring the learned network, the metric favors algorithms that use the BDeu score for learning. In fact, the BDeu score does not rely on the structure of the original, gold standard network at all; instead it employs several assumptions to score the networks. For those reasons, in addition to the score we also report the BIC score and the SHD metric.

### 4.2. Results

In Figure 1, we report the quality of the skeleton obtained with HPC over that obtained with MMPC (before the SS phase) as a function of the sample size. Results for each benchmark are not shown here in detail due to space restrictions. For sake of conciseness,


[^0]:    ${ }^{3}$ http://www.bnlearn.com/bnrepository

![img-0.jpeg](img-0.jpeg)

Figure 1: Quality of the skeleton obtained with HPC over that obtained with MMPC (after the CB phase). The 2 first figures present mean values aggregated over the 8 benchmarks. The 4 last figures present increase factors of HPC / MMPC, with the median, quartile, and most extreme values (green boxplots), along with the mean value (black line).

the performance values are averaged over the 8 benchmarks depicted in Table 1. The increase factor for a given performance indicator is expressed as the ratio of the performance value obtained with HPC over that obtained with MMPC (the gold standard). Note that for some indicators, an increase is actually not an improvement but is worse (e.g., false positive rate, Euclidean distance). For clarity, we mention explicitly on the subplots whether an increase factor $>1$ should be interpreted as an improvement or not. Regarding the quality of the superstructure, the advantages of HPC against MMPC are noticeable. As observed, HPC consistently increases the recall and reduces the rate of false negative edges. As expected this benefit comes at a little expense in terms of false positive edges. HPC also improves the Euclidean distance from perfect precision and recall on all benchmarks, while increasing the number of independence tests and thus the running time in the CB phase (see number of statistical tests). It is worth noting that HPC is capable of reducing by $50 \%$ the Euclidean distance with 50000 samples (lower left plot). These results are very much in line with other experiments presented in (Rodrigues de Morais \& Aussem, 2010a; Villanueva \& Maciel, 2012).

In Figure 2, we report the quality of the final DAG obtained with H2PC over that obtained with MMHC (after the SS phase) as a function of the sample size. Regarding BDeu and BIC on both training and test data, the improvements are noteworthy. The results in terms of goodness of fit to training data and new data using H2PC clearly dominate those obtained using MMHC, whatever the sample size considered, hence its ability to generalize better. Regarding the quality of the network structure itself (i.e., how close is the DAG to the true dependence structure of the data), this is pretty much a dead heat between the 2 algorithms on small sample sizes (i.e., 50 and 100), however we found H2PC to perform significantly better on larger sample sizes. The SHD increase factor decays rapidly (lower is better) as the sample size increases (lower left plot). For 50000 samples, the SHD is on average only $50 \%$ that of MMHC. Regarding the computational burden involved, we may observe from Table 2 that H2PC has a little computational overhead compared to MMHC. The running time increase factor grows somewhat linearly with the sample size. With 50000 samples, H2PC is approximately 10 times slower on average than MMHC. This is mainly due to the computational expense incurred in obtaining larger PC sets with HPC, compared to MMPC.

## 5. Application to multi-label learning

In this section, we address the problem of multilabel learning with H2PC. MLC is a challenging problem in many real-world application domains, where each instance can be assigned simultaneously to multiple binary labels (DembczyÄski et al., 2012; Read et al., 2009; Madjarov et al., 2012; Kocev et al., 2007; Tsoumakas et al., 2010b). Formally, learning from multi-label examples amounts to finding a mapping from a space of features to a space of labels. We shall assume throughout that $\mathbf{X}$ (a random vector in $\mathbb{R}^{d}$ ) is the feature set, $\mathbf{Y}$ (a random vector in $\{0,1\}^{n}$ ) is the label set, $\mathbf{U}=\mathbf{X} \cup \mathbf{Y}$ and $p$ a probability distribution defined over $\mathbf{U}$. Given a multi-label training set $\mathcal{D}$, the goal of multi-label learning is to find a function which is able to map any unseen example to its proper set of labels. From the Bayesian point of view, this problem amounts to modeling the conditional joint distribution $p(\mathbf{Y} \mid \mathbf{X})$.

### 5.1. Related work

This MLC problem may be tackled in various ways (Luaces et al., 2012; Alvares-Cherman et al., 2011; Read et al., 2009; Blockeel et al., 1998; Kocev et al., 2007). Each of these approaches is supposed to capture - to some extent - the relationships between labels. The two most straightforward meta-learning methods (Madjarov et al., 2012) are: Binary Relevance (BR) (Luaces et al., 2012) and Label Powerset (LP) (Tsoumakas \& Vlahavas, 2007; Tsoumakas et al., 2010b). Both methods can be regarded as opposite in the sense that BR does consider each label independently, while LP considers the whole label set at once (one multi-class problem). An important question remains: what shall we capture from the statistical relationships between labels exactly to solve the multilabel classification problem? The problem attracted a great deal of interest (DembczyÄski et al., 2012; Zhang \& Zhang, 2010). It is well beyond the scope and purpose of this paper to delve deeper into these approaches, we point the reader to (DembczyÄski et al., 2012; Tsoumakas et al., 2010b) for a review. The second fundamental problem that we wish to address involves finding an optimal feature subset selection of a label set, w.r.t an Information Theory criterion Koller \& Sahami (1996). As in the single-label case, multi-label feature selection has been studied recently and has encountered some success (Gu et al., 2011; Spolaôr et al., 2013).

![img-1.jpeg](img-1.jpeg)

Figure 2: Quality of the final DAG obtained with H 2 PC over that obtained with MMHC (after the SS phase). The 6 figures present increase factors of HPC / MMPC, with the median, quartile, and most extreme values (green boxplots), along with the mean value (black line).

Table 2: Total running time ratio $R$ (H2PC/MMHC). White cells indicate a ratio $R<1$ (in favor of H2PC), while shaded cells indicate a ratio $R>1$ (in favor of MMHC). The darker, the larger the ratio.


### 5.2. Label powerset decomposition

We shall first introduce the concept of label powerset that will play a pivotal role in the factorization of the conditional distribution $p(\mathbf{Y} \mid \mathbf{X})$.

Definition 1. $\mathbf{Y}_{L P} \subseteq \mathbf{Y}$ is called a label powerset iff $\mathbf{Y}_{L P} \perp \mathbf{Y} \backslash \mathbf{Y}_{L P} \mid \mathbf{X}$. Additionally, $\mathbf{Y}_{L P}$ is said minimal if it is non empty and has no label powerset as proper subset.

Let LP denote the set of all powersets defined over $\mathbf{U}$, and $\min \mathbf{L P}$ the set of all minimal label powersets. It is easily shown $\{\mathbf{Y}, \emptyset\} \subseteq \mathbf{L P}$. The key idea behind label powersets is the decomposition of the conditional distribution of the labels into a product of factors

$$
p(\mathbf{Y} \mid \mathbf{X})=\prod_{j=1}^{L} p\left(\mathbf{Y}_{L P_{j}} \mid \mathbf{X}\right)=\prod_{j=1}^{L} p\left(\mathbf{Y}_{L P_{j}} \mid \mathbf{M}_{L P_{j}}\right)
$$

where $\left\{\mathbf{Y}_{L P_{1}}, \ldots, \mathbf{Y}_{L P_{L}}\right\}$ is a partition of label powersets and $\mathbf{M}_{L P_{j}}$ is a Markov blanket of $\mathbf{Y}_{L P_{j}}$ in $\mathbf{X}$. From the above definition, we have $\mathbf{Y}_{L P_{i}} \perp \mathbf{Y}_{L P_{j}} \mid \mathbf{X}, \forall i \neq j$.

In the framework of MLC, one can consider a multitude of loss functions. In this study, we focus on a non label-wise decomposable loss function called the subset $0 / 1$ loss which generalizes the well-known $0 / 1$ loss from the conventional to the multi-label setting. The risk-minimizing prediction for subset $0 / 1$ loss is simply given by the mode of the distribution
(DembczyÂski et al., 2012). Therefore, we seek a factorization into a product of minimal factors in order to facilitate the estimation of the mode of the conditional distribution (also called the most probable explanation (MPE)):

$$
\max _{\mathbf{y}} p(\mathbf{y} \mid \mathbf{x})=\prod_{j=1}^{L} \max _{\mathbf{y}_{L P_{j}}} p\left(\mathbf{y}_{L P_{j}} \mid \mathbf{x}\right)=\prod_{j=1}^{L} \max _{\mathbf{y}_{L P_{j}}} p\left(\mathbf{y}_{L P_{j}} \mid \mathbf{m}_{L P_{j}}\right)
$$

The next section aims to obtain theoretical results for the characterization of the minimal label powersets $\mathbf{Y}_{L P_{j}}$ and their Markov boundaries $\mathbf{M}_{L P_{j}}$ from a DAG, in order to be able to estimate the MPE more effectively.

### 5.3. Label powerset characterization

In this section, we show that minimal label powersets can be depicted graphically when $p$ is faithful to a DAG,

Theorem 6. Suppose $p$ is faithful to a DAG $\mathcal{G}$. Then, $Y_{i}$ and $Y_{j}$ belong to the same minimal label powerset if and only if there exists an undirected path in $\mathcal{G}$ between nodes $Y_{i}$ and $Y_{j}$ in $\mathbf{Y}$ such that all intermediate nodes $Z$ are either (i) $Z \in \mathbf{Y}$, or (ii) $Z \in \mathbf{X}$ and $Z$ has two parents in $\mathbf{Y}$ (i.e. a collider of the form $Y_{p} \rightarrow X \leftarrow Y_{q}$ ).

The proof is given in the Appendix. We shall now address the following questions: What is the Markov boundary in $\mathbf{X}$ of a minimal label powerset? Answering

this question for general distributions is not trivial. We establish a useful relation between a label powerset and its Markov boundary in $\mathbf{X}$ when $p$ is faithful to a DAG,

Theorem 7. Suppose $p$ is faithful to a DAG $\mathcal{G}$. Let $\mathbf{Y}_{L P}=\left\{Y_{1}, Y_{2}, \ldots, Y_{n}\right\}$ be a label powerset. Then, its Markov boundary $\mathbf{M}$ in $\mathbf{U}$ is also its Markov boundary in $\mathbf{X}$, and is given in $\mathcal{G}$ by $\mathbf{M}=\bigcup_{j=1}^{n}\left\{\mathbf{P C}_{Y_{j}} \cup \mathbf{S P}_{Y_{j}}\right\} \backslash \mathbf{Y}$.

The proof is given in the Appendix.

### 5.4. Experimental setup

The MLC problem is decomposed into a series of multi-class classification problems, where each multiclass variable encodes one label powerset, with as many classes as the number of possible combinations of labels, or those present in the training data. At this point, it should be noted that the LP method is a special case of this framework since the whole label set is a particular label powerset (not necessarily minimal though). The above procedure can been summarized as follows:

1. Learn the BN local graph $\mathcal{G}$ around the label set;
2. Read off $\mathcal{G}$ the minimal label powersets and their respective Markov boundaries;
3. Train an independent multi-class classifier on each minimal LP, with the input space restricted to its Markov boundary in $\mathcal{G}$;
4. Aggregate the prediction of each classifier to output the most probable explanation, i.e. $\arg \max _{\mathbf{y}} p(\mathbf{y} \mid \mathbf{x})$.

To assess separately the quality of the minimal label powerset decomposition and the feature subset selection with Markov boundaries, we investigate 4 scenarios:

- BR without feature selection (denoted BR): a classifier is trained on each single label with all features as input. This is the simplest approach as it does not exploit any label dependency. It serves as a baseline learner for comparison purposes.
- BR with feature selection (denoted BR+MB): a classifier is trained on each single label with the input space restricted to its Markov boundary in $\mathcal{G}$. Compared to the previous strategy, we evaluate here the effectiveness of the feature selection task.
- Minimum label powerset method without feature selection (denoted MLP): the minimal label powersets are obtained from the DAG. All features are used as inputs.
- Minimum label powerset method with feature selection (denoted MLP+MB): the minimal label powersets are obtained from the DAG. the input space is restricted to the Markov boundary of the labels in that powerset.

We use the same base learner in each meta-learning method: the well-known Random Forest classifier (Breiman, 2001). RF achieves good performance in standard classification as well as in multi-label problems (Kocev et al., 2007; Madjarov et al., 2012), and is able to handle both continuous and discrete data easily, which is much appreciated. The standard RF implementation in $R$ (Liaw \& Wiener, 2002) ${ }^{4}$ was used. For practical purposes, we restricted the forest size of RF to 100 trees, and left the other parameters to their default values.

### 5.4.1. Data and performance indicators

A total of 10 multi-label data sets are collected for experiments in this section, whose characteristics are summarized in Table 3. These data sets come from different problem domains including text, biology, and music. They can be found on the Mulan ${ }^{5}$ repository, except for image which comes from Zhou ${ }^{6}$ (Maron \& Ratan, 1998). Let $\mathcal{D}$ be the multi-label data set, we use $|\mathcal{D}|, \operatorname{dim}(\mathcal{D}), L(\mathcal{D}), F(\mathcal{D})$ to represent the number of examples, number of features, number of possible labels, and feature type respectively. $D L(\mathcal{D})=||Y| \exists x:(x, Y) \in$ $\mathcal{D} \|$ counts the number of distinct label combinations appearing in the data set. Continues values are binarized during the BN structure learning phase.

Table 3: Data sets characteristics


The performance of a multi-label classifier can be assessed by several evaluation measures

[^0]
[^0]:    ${ }^{4}$ http://cran.r-project.org/web/packages/randomForest
    ${ }^{5}$ http://mulan.sourceforge.net/datasets.html
    ${ }^{6}$ http://lamda.nju.edu.cn/data_MIMLimage.ashx

(Tsoumakas et al., 2010a). We focus on maximizing a non-decomposable score function: the global accuracy (also termed subset accuracy, complement of the $0 / 1$-loss), which measures the correct classification rate of the whole label set (exact match of all labels required). Note that the global accuracy implicitly takes into account the label correlations. It is therefore a very strict evaluation measure as it requires an exact match of the predicted and the true set of labels. It was recently proved in (DembczyÂski et al., 2012) that BR is optimal for decomposable loss functions (e.g., the hamming loss), while non-decomposable loss functions (e.g. subset loss) inherently require the knowledge of the label conditional distribution. 10-fold cross-validation was performed for the evaluation of the MLC methods.

### 5.4.2. Results

Table 4 reports the outputs of H2PC and MMHC, Table 5 shows the global accuracy of each method on the 10 data sets. Table 6 reports the running time and the average node degree of the labels in the DAGs obtained with both methods. Figures 3 up to 7 display graphically the local DAG structures around the labels, obtained with H2PC and MMHC, for illustration purposes.

Several conclusions may be drawn from these experiments. First, we may observe by inspection of the average degree of the label nodes in Table 6 that several DAGs are densely connected, like scene or bibtex, while others are rather sparse, like genbase, medical, corel5k. The DAGs displayed in Figures 3 up to 7 lend themselves to interpretation. They can be used for encoding as well as portraying the conditional independencies, and the d-sep criterion can be used to read them off the graph. Many label powersets that are reported in Table 4 can be identified by graphical inspection of the DAGs. For instance, the two label powersets in yeast (Figure 3, bottom plot) are clearly noticeable in both DAGs. Clearly, BNs have a number of advantages over alternative methods. They lay bare useful information about the label dependencies which is crucial if one is interested in gaining an understanding of the underlying domain. It is however well beyond the scope of this paper to delve deeper into the DAG interpretation. Overall, it appears that the structures recovered by H2PC are significantly denser, compared to MMHC. On bibtex and enron, the increase of the average label degree is the most spectacular. On bibtex (resp. enron), the average label degree has raised from 2.6 to 6.4 (resp. from 1.2 to 3.3). This result is in nice agreement with the experiments in the previous section, as H2PC was shown to consistently reduce the rate of false negative
edges with respect to MMHC (at the cost of a slightly higher false discovery rate).

Second, Table 4 is very instructive as it reveals that on emotions, image, and scene, the MLP approach boils down to the LP scheme. This is easily seen as there is only one minimal label powerset extracted on average. In contrast, on genbase the MLP approach boils down to the simple BR scheme. This is confirmed by inspecting Table 5: the performances of MMHC and H2PC (without feature selection) are equal. An interesting observation upon looking at the distribution of the label powerset size shows that for the remaining data sets, the MLP mostly decomposes the label set in two parts: one on which it performs BR and the other one on which it performs LP. Take for instance enron, it can be seen from Table 4 that there are approximately 23 label singletons and a powerset of 30 labels with H 2 PC for a total of 53 labels. The gain in performance with MLP over BR, our baseline learner, can be ascribed to the quality of the label powerset decomposition as BR is ignoring label dependencies. As expected, the results using MLP clearly dominate those obtained using BR on all data sets except genbase. The DAGs display the minimum label powersets and their relevant features.

Third, H2PC compares favorably to MMHC. On scene for instance, the accuracy of MLP+MB has raised from $20 \%$ (with MMHC) to $56 \%$ (with H2PC). On yeast, it has raised from $7 \%$ to $23 \%$. Without feature selection, the difference in global accuracy is less pronounced but still in favor of H2PC. A Wilcoxon signed rank paired test reveals statistically significant improvements of H2PC over MMHC in the MLP approach without feature selection ( $p<0.02$ ). This trend is more pronounced when the feature selection is used ( $p<0.001$ ), using MLP-MB. Note however that the LP decomposition for H 2 PC and MMHC on yeast and image are strictly identical, hence the same accuracy values in Table 5 in the MLP column.

Fourth, regarding the utility of the feature selection, it is difficult to reach any conclusion. Whether BR or MLP is used, the use of the selected features as inputs to the classification model is not shown greatly beneficial in terms of global accuracy on average. The performance of BR and our MLP with all the features outperforms that with the selected features in 6 data sets but the feature selection leads to actual improvements in 3 data sets. The difference in accuracy with and without the feature selection was not shown to be statistically significant ( $p>0.20$ with a Wilcoxon signed rank paired test). Surprisingly, the feature selection did exceptionally well on genbase. On this data set, the increase in accuracy is the most impressive: it raised from

$7 \%$ to $98 \%$ which is atypical. The dramatic increase in accuracy on genbase is due solely to the restricted feature set as input to the classification model. This is also observed on medical, to a lesser extent though. Interestingly, on large and densely connected networks (e.g. bibtex, slashdot and corel5K), the feature selection performed very well in terms of global accuracy and significantly reduced the input space which is noticeable. On emotions, yeast, image, scene and genbase, the method reduced the feature set down to nearly $1 / 100$ its original size. The feature selection should be evaluated in view of its effectiveness at balancing the increasing error and the decreasing computational burden by drastically reducing the feature space. We should also keep in mind that the feature relevance cannot be defined independently of the learner and the model-performance metric (e.g., the loss function used). Admittedly, our feature selection based on the Markov boundaries is not necessarily optimal for the base MLC learner used here, namely the Random Forest model.

As far as the overall running time performance is concerned, we see from Table 6 that for both methods, the running time grows somewhat exponentially with the size of the Markov boundary and the number of features, hence the considerable rise in total running time on bibtex. H2PC takes almost 200 times longer on bibtex (1826 variables) and enron (1001 variables) which is quite considerable but still affordable ( 44 hours of single-CPU time on bibtex and 13 hours on enron). We also observe that the size of the parent set with H2PC is 2.5 (on bibtex) and 3.6 (on enron) times larger than that of MMHC (which may hurt interpretability). In fact, the running time is known to increase exponentially with the parent set size of the true underlying network. This is mainly due the computational overhead of greedy search-and-score procedure with larger parent sets which is the most promising part to optimize in terms of computational gains as we discuss in the Conclusion.

## 6. Discussion \& practical applications

Our prime conclusion is that H 2 PC is a promising approach to constructing BN global or local structures around specific nodes of interest, with potentially thousands of variables. Concentrating on higher recall values while keeping the false positive rate as low as possible pays off in terms of goodness of fit and structure accuracy. Historically, the main practical difficulty in the application of BN structure discovery approaches has been a lack of suitable computing resources and relevant accessible software. The number

Table 4: Distribution of the number and the size of the minimal label powersets output by H2PC (top) and MMHC (bottom). On each data set: mean number of powersets, minimum/median/maximum number of labels per powerset, and minimum/median/maximum number of distinct classes per powerset. The total number of labels and distinct labels combinations is recalled for convenience.


Table 5: Global classification accuracies using 4 learning methods (BR, MLP, BR+MB, MLP+MB) based on the DAG obtained with H2PC and MMHC. Best values between H2PC and MMHC are boldfaced.


Table 6: DAG learning time (in seconds) and average degree of the label nodes.


of variables which can be included in exact BN analysis is still limited. As a guide, this might be less than about 40 variables for exact structural search techniques (Perrier et al., 2008; Kojima et al., 2010). In contrast, constraint-based heuristics like the one presented in this study is capable of processing many thousands of features within hours on a personal computer, while maintaining a very high structural accuracy. H2PC and MMHC could potentially handle up to 10,000 labels in a few days of single-CPU time and far less by parallelizing the skeleton identification algorithm as discussed in (Tsamardinos et al., 2006; Villanueva \& Maciel, 2014).

The advantages in terms of structure accuracy and its ability to scale to thousands of variables opens up many avenues of future possible applications of H 2 PC in various domains as we shall discuss next. For example, BNs have especially proven to be useful abstractions in computational biology (Nagarajan et al., 2013; Scutari \& Nagarajan, 2013; Prestat et al., 2013; Aussem et al., 2012, 2010; Peña, 2008; Peña et al., 2005). Identifying the gene network is crucial for understanding the behavior of the cell which, in turn, can lead to better diagnosis and treatment of diseases. This is also of great importance for characterizing the function of genes and the proteins they encode in determining traits, psychology, or development of an organism. Genome sequencing uses high-throughput techniques like DNA microarrays, proteomics, metabolomics and mutation analysis to describe the function and interactions of thousands of genes (Zhang \& Zhou., 2006). Learning BN models of gene networks from these huge data is still a difficult task (Badea, 2004; Bernard \& Hartemink, 2005; Friedman et al., 1999a; Ott et al., 2004; Peer et al., 2001). In these studies, the authors had decide in advance which genes were included in the learning process, in all the cases less than 1000, and which genes were excluded from it (Peña,
2008). H2PC overcome the problem by focusing the search around a targeted gene: the key step is the identification of the vicinity of a node $X$ (Peña et al., 2005).

Our second objective in this study was to demonstrate the potential utility of hybrid BN structure discovery to multi-label learning. In multi-label data where many inter-dependencies between the labels may be present, explicitly modeling all relationships between the labels is intuitively far more reasonable (as demonstrated in our experiments). BNs explicitly account for such interdependencies and the DAG allows us to identify an optimal set of predictors for every label powerset. The experiments presented here support the conclusion that local structural learning in the form of local neighborhood induction and Markov blanket is a theoretically wellmotivated approach that can serve as a powerful learning framework for label dependency analysis geared toward multi-label learning. Multi-label scenarios are found in many application domains, such as multimedia annotation (Snoek et al., 2006; Trohidis et al., 2008), tag recommendation, text categorization (McCallum, 1999; Zhang \& Zhou., 2006), protein function classification (Roth \& Fischer, 2007), and antiretroviral drug categorization (Borchani et al., 2013).

## 7. Conclusion \& avenues for future research

We first discussed a hybrid algorithm for global or local (around target nodes) BN structure learning called Hybrid HPC (H2PC). Our extensive experiments showed that H 2 PC outperforms the state-of-the-art MMHC by a significant margin in terms of edge recall without sacrificing the number of extra edges, which is crucial for the soundness of the super-structure used during the second stage of hybrid methods, like the ones proposed in (Perrier et al., 2008; Kojima et al., 2010). The code of H 2 PC is open-source and publicly available online at https://github.com/madbix/bnlearn-clone-3.4. Second, we discussed an application of H 2 PC to the multi-label learning problem which is a challenging problem in many real-world application domains. We established theoretical results, under the faithfulness condition, in order to characterize graphically the so-called minimal label powersets that appear as irreducible factors in the joint distribution and their respective Markov boundaries. As far as we know, this is the first investigation of Markov boundary principles to the optimal variable/feature selection problem in multi-label learning. These formal results offer a simple guideline to characterize graphically : i) the minimal label powerset decomposition, (i.e. into minimal

subsets $\mathbf{Y}_{L P} \subseteq \mathbf{Y}$ such that $\mathbf{Y}_{L P} \pm \mathbf{Y} \backslash \mathbf{Y}_{L P} \mid \mathbf{X}$ ), and ii) the minimal subset of features, w.r.t an Information Theory criterion, needed to predict each label powerset, thereby reducing the input space and the computational burden of the multi-label classification. The theoretical analysis laid the foundation for a practical multi-label classification procedure. Another set of experiments were carried out on a broad range of multi-label data sets from different problem domains to demonstrate its effectiveness. H2PC was shown to outperform MMHC by a significant margin in terms of global accuracy.

We suggest several avenues for future research. As far as BN structure learning is concerned, future work will aim at: 1) ascertaining which independence test (e.g. tests targeting specific distributions, employing parametric assumptions etc.) is most suited to the data at hand (Tsamardinos \& Borboudakis, 2010; Scutari, 2011); 2) controlling the false discovery rate of the edges in the graph output by H2PC (Peña, 2008) especially when dealing with more nodes than samples, e.g. learning gene networks from gene expression data. In this study, H2PC was run independently on each node without keeping track of the dependencies found previously. This lead to some loss of efficiency due to redundant calculations. The optimization of the H2PC code is currently being undertaken to lower the computational cost while maintaining its performance. These optimizations will include the use of a cache to store the (in)dependencies and the use of a global structure. Other interesting research avenues to explore are extensions and modifications to the greedy search-and-score procedure which is the most promising part to optimize in terms of computational gains. Regarding the multilabel learning problem, experiments with several thousands of labels are currently been conducted and will be reported in due course. We also intend to work on relaxing the faithfulness assumption and derive a practical multi-label classification algorithm based on H2PC that is correct under milder assumptions underlying the joint distribution (e.g. Composition, Intersection). This needs further substantiation through more analysis.

## Acknowledgments

The authors thank Marco Scutari for sharing his bnlearn package in $R$. The research was also supported by grants from the European ENIAC Joint Undertaking (INTEGRATE project) and from the French RhôneAlpes Complex Systems Institute (IXXI).

## Appendix

Lemma 8. $\forall \mathbf{Y}_{L P_{i}}, \mathbf{Y}_{L P_{j}} \in \mathbf{L P}$, then $\mathbf{Y}_{L P_{i}} \cap \mathbf{Y}_{L P_{j}} \in \mathbf{L P}$.
Proof. To keep the notation uncluttered and for the sake of simplicity, consider a partition $\left\{\mathbf{Y}_{1}, \mathbf{Y}_{2}, \mathbf{Y}_{3}, \mathbf{Y}_{4}\right\}$ of $\mathbf{Y}$ such that $\mathbf{Y}_{L P_{i}}=\mathbf{Y}_{1} \cup \mathbf{Y}_{2}, \mathbf{Y}_{L P_{j}}=\mathbf{Y}_{2} \cup \mathbf{Y}_{3}$. From the label powerset assumption for $\mathbf{Y}_{L P_{i}}$ and $\mathbf{Y}_{L P_{j}}$, we have $\left(\mathbf{Y}_{1} \cup \mathbf{Y}_{2}\right) \pm\left(\mathbf{Y}_{3} \cup \mathbf{Y}_{4}\right) \mid \mathbf{X}$ and $\left(\mathbf{Y}_{2} \cup \mathbf{Y}_{3}\right) \pm$ $\left(\mathbf{Y}_{1} \cup \mathbf{Y}_{4}\right) \mid \mathbf{X}$. From the Decomposition, we have that $\mathbf{Y}_{2} \pm\left(\mathbf{Y}_{3} \cup \mathbf{Y}_{4}\right) \mid \mathbf{X}$. Using the Weak union, we obtain that $\mathbf{Y}_{2} \pm \mathbf{Y}_{1} \mid\left(\mathbf{Y}_{3} \cup \mathbf{Y}_{4} \cup \mathbf{X}\right)$. From these two facts, we can use the Contraction property to show that $\mathbf{Y}_{2} \pm$ $\left(\mathbf{Y}_{1} \cup \mathbf{Y}_{3} \cup \mathbf{Y}_{4}\right) \mid \mathbf{X}$. Therefore, $\mathbf{Y}_{2}=\mathbf{Y}_{L P_{i}} \cap \mathbf{Y}_{L P_{j}}$ is a label powerset by definition.

Lemma 9. Let $Y_{i}$ and $Y_{j}$ denote two distinct labels in $\mathbf{Y}$ and define by $\mathbf{Y}_{L P_{i}}$ and $\mathbf{Y}_{L P_{j}}$ their respective minimal label powerset. Then we have,
$\exists \mathbf{Z} \subseteq \mathbf{Y} \backslash\left\{Y_{i}, Y_{j}\right\},\left\{Y_{i}\right\} \pm\left\{Y_{j}\right\} \mid(\mathbf{X} \cup \mathbf{Z}) \Rightarrow \mathbf{Y}_{L P_{i}}=\mathbf{Y}_{L P_{j}}$
Proof. Let us suppose $\mathbf{Y}_{L P_{i}} \neq \mathbf{Y}_{L P_{j}}$. By the label powerset definition for $\mathbf{Y}_{L P_{i}}$, we have $\mathbf{Y}_{L P_{i}} \pm \mathbf{Y} \backslash \mathbf{Y}_{L P_{i}} \mid \mathbf{X}$. As $\mathbf{Y}_{L P_{i}} \cap \mathbf{Y}_{L P_{j}}=\emptyset$ owing to Lemma 8, we have that $Y_{j} \notin \mathbf{Y}_{L P_{i}} . \forall \mathbf{Z} \subseteq \mathbf{Y} \backslash\left\{Y_{i}, Y_{j}\right\}, \mathbf{Z}$ can be decomposed as $\mathbf{Z}_{i} \cup \mathbf{Z}_{j}$ such that $\mathbf{Z}_{i}=\mathbf{Z} \cap\left(\mathbf{Y}_{L P_{i}} \backslash\left\{Y_{i}\right\}\right)$ and $\mathbf{Z}_{j}=\mathbf{Z} \backslash \mathbf{Z}_{i}$. Using the Decomposition property, we have that $\left(\left\{Y_{i}\right\} \cup \mathbf{Z}_{i}\right) \pm\left(\left\{Y_{j}\right\} \cup \mathbf{Z}_{j}\right) \mid \mathbf{X}$. Using the Weak union property, we have that $\left\{Y_{i}\right\} \pm\left\{Y_{j}\right\} \mid(\mathbf{X} \cup \mathbf{Z})$. As this is true $\forall \mathbf{Z} \subseteq \mathbf{Y} \backslash\left\{Y_{i}, Y_{j}\right\}$, then $\nexists \mathbf{Z} \subseteq \mathbf{Y} \backslash\left\{Y_{i}, Y_{j}\right\},\left\{Y_{i}\right\} /$ $\pm\left\{Y_{j}\right\} \mid(\mathbf{X} \cup \mathbf{Z})$, which completes the proof.

Lemma 10. Consider $\mathbf{Y}_{L P}$ a minimal label powerset. Then, if $p$ satisfies the Composition property, $\mathbf{Z} \pm \mathbf{Y}_{L P} \backslash$ $\mathbf{Z} \mid \mathbf{X}$.

Proof. By contradiction, suppose a nonempty $\mathbf{Z}$ exists, such that $\mathbf{Z} \pm \mathbf{Y}_{L P} \backslash \mathbf{Z} \mid \mathbf{X}$. From the label powerset assumption of $\mathbf{Y}_{L P}$, we have that $\mathbf{Y}_{L P} \pm \mathbf{Y} \backslash \mathbf{Y}_{L P} \mid \mathbf{X}$ . From these two facts, we can use the Composition property to show that $\mathbf{Z} \pm \mathbf{Y} \backslash \mathbf{Z} \mid \mathbf{X}$ which contradicts the minimal label powerset assumption of $\mathbf{Y}_{L P}$. This concludes the proof.

Theorem 7. Suppose $p$ is faithful to a DAG $\mathcal{G}$. Then, $Y_{i}$ and $Y_{j}$ belong to the same minimal label powerset if and only if there exists an undirected path in $\mathcal{G}$ between nodes $Y_{i}$ and $Y_{j}$ in $\mathbf{Y}$ such that all intermediate nodes $Z$ are either (i) $Z \in \mathbf{Y}$, or (ii) $Z \in \mathbf{X}$ and $Z$ has two parents in $\mathbf{Y}$ (i.e. a collider of the form $Y_{p} \rightarrow X \leftarrow Y_{q}$ ).

Proor. Suppose such a path exists. By conditioning on all the intermediate colliders $Y_{k}$ in $\mathbf{Y}$ of the form $Y_{p} \rightarrow$ $Y_{k} \leftarrow Y_{q}$ along an undirected path in $\mathcal{G}$ between nodes $Y_{i}$ and $Y_{j}$, we ensure that $\exists \mathbf{Z} \subseteq \mathbf{Y} \backslash\left\{Y_{i}, Y_{j}\right\}, \overline{\operatorname{Step}}\left(Y_{i}, Y_{j} \mid\right.$ $\mathbf{X} \cup \mathbf{Z}$ ). Due to the faithfulness, this is equivalent to $\left\{Y_{i}\right\} \Perp\left\{Y_{j}\right\} \mid(\mathbf{X} \cup \mathbf{Z})$. From Lemma 9, we conclude that $Y_{i}$ and $Y_{j}$ belong to the same minimal label powerset. To show the inverse, note that owing to Lemma 10, we know that there exists no partition $\left\{\mathbf{Z}_{i}, \mathbf{Z}_{j}\right\}$ of $\mathbf{Z}$ such that $\left(\left\{Y_{i}\right\} \cup \mathbf{Z}_{i}\right) \Perp\left(\left\{Y_{j}\right\} \cup \mathbf{Z}_{j}\right) \mid \mathbf{X}$. Due to the faithfulness, there exists at least a link between $\left(\left\{Y_{i}\right\} \cup \mathbf{Z}_{i}\right)$ and $\left(\left\{Y_{j}\right\} \cup\right.$ $\left.\mathbf{Z}_{j}\right)$ in the DAG, hence by recursion, there exists a path between $Y_{i}$ and $Y_{j}$ such that all intermediate nodes $Z$ are either (i) $Z \in \mathbf{Y}$, or (ii) $Z \in \mathbf{X}$ and $Z$ has two parents in $\mathbf{Y}$ (i.e. a collider of the form $Y_{p} \rightarrow X \leftarrow Y_{q}$ ).

Theorem 8. Suppose $p$ is faithful to a DAG $\mathcal{G}$. Let $\mathbf{Y}_{L P} \equiv\left\{Y_{1}, Y_{2}, \ldots, Y_{n}\right\}$ be a label powerset. Then, its Markov boundary $\mathbf{M}$ in $\mathbf{U}$ is also its Markov boundary in $\mathbf{X}$, and is given in $\mathcal{G}$ by $\mathbf{M}=\bigcup_{j=1}^{n}\left\{\mathbf{P C}_{Y_{j}} \cup \mathbf{S P}_{Y_{j}}\right\} \backslash \mathbf{Y}$.

Proof. First, we prove that $\mathbf{M}$ is a Markov boundary of $\mathbf{Y}_{L P}$ in $\mathbf{U}$. Define $\mathbf{M}_{i}$ the Markov boundary of $Y_{i}$ in $\mathbf{U}$, and $\mathbf{M}_{i}^{\prime}=\mathbf{M}_{i} \backslash \mathbf{Y}$. From Theorem 5, $\mathbf{M}_{i}$ is given in $\mathcal{G}$ by $\mathbf{M}_{i}=\mathbf{P C}_{Y_{j}} \cup \mathbf{S P}_{Y_{j}}$. We may now prove that $\mathbf{M}_{1}^{\prime} \cup \cdots \cup \mathbf{M}_{n}^{\prime}$ is a Markov boundary of $\left\{Y_{1}, Y_{2}, \ldots, Y_{n}\right\}$ in $\mathbf{U}$. We show first that the statement holds for $n=2$ and then conclude that it holds for all $n$ by induction. Let $\mathbf{W}$ denote $\mathbf{U} \backslash\left(\mathbf{Y}_{1} \cup \mathbf{Y}_{2} \cup \mathbf{M}^{\prime}{ }_{1} \cup \mathbf{M}^{\prime}{ }_{2}\right)$, and define $\mathbf{Y}_{1}=\left\{Y_{1}\right\}$ and $\mathbf{Y}_{2}=\left\{Y_{2}\right\}$. From the Markov blanket assumption for $\mathbf{Y}_{1}$ we have $\mathbf{Y}_{1} \Perp \mathbf{U} \backslash\left(\mathbf{Y}_{1} \cup \mathbf{M}_{1}\right) \mid \mathbf{M}_{1}$ . Using the Weak Union property, we obtain that $\mathbf{Y}_{1} \Perp$ $\mathbf{W} \mid \mathbf{M}_{1}^{\prime} \cup \mathbf{M}_{2}^{\prime} \cup \mathbf{Y}_{2}$. Similarly we can derive $\mathbf{Y}_{2} \Perp$ $\mathbf{W} \mid \mathbf{M}_{2}^{\prime} \cup \mathbf{M}_{1}^{\prime} \cup \mathbf{Y}_{1}$. Combining these two statements yields $\mathbf{Y}_{1} \cup \mathbf{Y}_{2} \Perp \mathbf{W} \mid \mathbf{M}_{1}^{\prime} \cup \mathbf{M}_{2}^{\prime}$ due to the Intersection property. Let $\mathbf{M}=\mathbf{M}_{1}^{\prime} \cup \mathbf{M}_{2}^{\prime}$ the last expression can be formulated as $\mathbf{Y}_{1} \cup \mathbf{Y}_{2} \Perp \mathbf{U} \backslash\left(\mathbf{Y}_{1} \cup \mathbf{Y}_{2} \cup \mathbf{M}\right) \mid \mathbf{M}$ which is the definition of a Markov blanket of $\mathbf{Y}_{1} \cup \mathbf{Y}_{2}$ in $\mathbf{U}$. We shall now prove that $\mathbf{M}$ is minimal. Let us suppose that it is not the case, i.e., $\exists \mathbf{Z} \subset \mathbf{M}$ such that $\mathbf{Y}_{1} \cup \mathbf{Y}_{2} \Perp$ $\mathbf{Z} \cup\left(\mathbf{U} \backslash\left(\mathbf{Y}_{1} \cup \mathbf{Y}_{2} \cup \mathbf{M}\right)\right) \mid \mathbf{M} \backslash \mathbf{Z}$. Define $\mathbf{Z}_{1}=\mathbf{Z} \cap \mathbf{M}_{1}$ and $\mathbf{Z}_{2}=\mathbf{Z} \cap \mathbf{M}_{2}$, we may apply the Weak Union property to get $\mathbf{Y}_{1} \Perp \mathbf{Z}_{1} \mid(\mathbf{M} \backslash \mathbf{Z}) \cup \mathbf{Y}_{2} \cup \mathbf{Z}_{2} \cup(\mathbf{U} \backslash(\mathbf{Y} \cup \mathbf{M}))$ which can be rewritten more compactly as $\mathbf{Y}_{1} \Perp \mathbf{Z}_{1} \mid\left(\mathbf{M}_{1} \backslash \mathbf{Z}_{1}\right) \cup$ $\left(\mathbf{U} \backslash\left(\mathbf{Y}_{1} \cup \mathbf{M}_{1}\right)\right)$. From the Markov blanket assumption, we have $\mathbf{Y}_{1} \Perp \mathbf{U} \backslash\left(\mathbf{Y}_{1} \cup \mathbf{M}_{1}\right) \mid \mathbf{M}_{1}$. We may now apply the Intersection property on these two statements to obtain $\mathbf{Y}_{1} \Perp \mathbf{Z}_{1} \cup\left(\mathbf{U} \backslash\left(\mathbf{Y}_{1} \cup \mathbf{M}_{1}\right)\right) \mid \mathbf{M}_{1} \backslash \mathbf{Z}_{1}$. Similarly, we can derive $\mathbf{Y}_{2} \Perp \mathbf{Z}_{2} \cup\left(\mathbf{U} \backslash\left(\mathbf{Y}_{2} \cup \mathbf{M}_{2}\right)\right) \mid \mathbf{M}_{2} \backslash \mathbf{Z}_{2}$. From the Markov boundary assumption of $\mathbf{M}_{1}$ and $\mathbf{M}_{2}$, we have necessarily $\mathbf{Z}_{1}=\emptyset$ and $\mathbf{Z}_{2}=\emptyset$, which in turn
yields $\mathbf{Z}=\emptyset$. To conclude for any $n>2$, it suffices to set $\mathbf{Y}_{1}=\bigcup_{j=1}^{n-1}\left\{Y_{j}\right\}$ and $\mathbf{Y}_{2}=\left\{Y_{n}\right\}$ to conclude by induction.

Second, we prove that $\mathbf{M}$ is a Markov blanket of $\mathbf{Y}_{L P}$ in $\mathbf{X}$. Define $\mathbf{Z}=\mathbf{M} \cap \mathbf{Y}$. From the label powerset definition, we have $\mathbf{Y}_{L P} \Perp \mathbf{Y} \backslash \mathbf{Y}_{L P} \mid \mathbf{X}$. Using the Weak Union property, we obtain $\mathbf{Y}_{L P} \Perp \mathbf{Z} \mid \mathbf{U} \backslash\left(\mathbf{Y}_{L P} \cup \mathbf{Z}\right)$ which can be reformulated as $\mathbf{Y}_{L P} \Perp \mathbf{Z} \mid\left(\mathbf{U} \backslash\left(\mathbf{Y}_{L P} \cup\right.\right.$ $\mathbf{M})) \cup(\mathbf{M} \backslash \mathbf{Z})$. Now, the Markov blanket assumption for $\mathbf{Y}_{L P}$ in $\mathbf{U}$ yields $\mathbf{Y}_{L P} \Perp \mathbf{U} \backslash\left(\mathbf{Y}_{L P} \cup \mathbf{M}\right) \mid \mathbf{M}$ which can be rewritten as $\mathbf{Y}_{L P} \Perp \mathbf{U} \backslash\left(\mathbf{Y}_{L P} \cup \mathbf{M}\right) \mid(\mathbf{M} \backslash \mathbf{Z}) \cup \mathbf{Z}$. From the Intersection property, we get $\mathbf{Y}_{L P} \Perp \mathbf{Z} \cup\left(\mathbf{U} \backslash\left(\mathbf{Y}_{L P} \cup\right.\right.$ $\mathbf{M})) \mid \mathbf{M} \backslash \mathbf{Z}$. From the Markov boundary assumption of $\mathbf{M}$ in $\mathbf{U}$, we know that there exists no proper subset of $\mathbf{M}$ which satisfies this statement, and therefore $\mathbf{Z}=$ $\mathbf{M} \cap \mathbf{Y}=\emptyset$. From the Markov blanket assumption of $\mathbf{M}$ in $\mathbf{U}$, we have $\mathbf{Y}_{L P} \Perp \mathbf{U} \backslash\left(\mathbf{Y}_{L P} \cup \mathbf{M}\right) \mid \mathbf{M}$. Using the Decomposition property, we obtain $\mathbf{Y}_{L P} \Perp \mathbf{X} \backslash \mathbf{M} \mid \mathbf{M}$ which, together with the assumption $\mathbf{M} \cap \mathbf{Y}=\emptyset$, is the definition of a Markov blanket of $\mathbf{Y}_{L P}$ in $\mathbf{X}$.

Finally, we prove that $\mathbf{M}$ is a Markov boundary of $\mathbf{Y}_{L P}$ in $\mathbf{X}$. Let us suppose that it is not the case, i.e., $\exists \mathbf{Z} \subset \mathbf{M}$ such that $\mathbf{Y}_{L P} \Perp \mathbf{Z} \cup(\mathbf{X} \backslash \mathbf{M}) \mid \mathbf{M} \backslash \mathbf{Z}$ From the label powerset assumption of $\mathbf{Y}_{L P}$, we have $\mathbf{Y}_{L P} \Perp \mathbf{Y} \backslash \mathbf{Y}_{L P} \mid \mathbf{X}$ which can be rewritten as $\mathbf{Y}_{L P} \Perp \mathbf{Y} \backslash \mathbf{Y}_{L P} \mid(\mathbf{X} \backslash \mathbf{M}) \cup(\mathbf{M} \backslash \mathbf{Z}) \cup \mathbf{Z}$. Due to the Contraction property, combining these two statements yields $\mathbf{Y}_{L P} \Perp \mathbf{Z} \cup\left(\mathbf{U} \backslash\left(\mathbf{M} \cup \mathbf{Y}_{L P}\right) \mid \mathbf{M} \backslash \mathbf{Z}\right.$. From the Markov boundary assumption of $\mathbf{M}$ in $\mathbf{U}$, we have necessarily $\mathbf{Z}=\emptyset$, which suffices to prove that $\mathbf{M}$ is a Markov boundary of $\mathbf{Y}_{L P}$ in $\mathbf{X}$.

![img-2.jpeg](img-2.jpeg)

Figure 3: The local BN structures learned by MMHC (left plot) and H2PC (right plot) on a single cross-validation split, on Emotions and Yeast.

![img-3.jpeg](img-3.jpeg)

Figure 4: The local BN structures learned by MMHC (left plot) and H2PC (right plot) on a single cross-validation split, on Image and Scene.

![img-4.jpeg](img-4.jpeg)
(b) Genbase

Figure 5: The local BN structures learned by MMHC (left plot) and H2PC (right plot) on a single cross-validation split, on Slashdot and Genbase.

![img-5.jpeg](img-5.jpeg)

Figure 6: The local BN structures learned by MMHC (left plot) and H2PC (right plot) on a single cross-validation split, on Medical and Enron.

![img-6.jpeg](img-6.jpeg)

Figure 7: The local BN structures learned by MMHC (left plot) and H2PC (right plot) on a single cross-validation split, on Bibtex and Corel5k.
