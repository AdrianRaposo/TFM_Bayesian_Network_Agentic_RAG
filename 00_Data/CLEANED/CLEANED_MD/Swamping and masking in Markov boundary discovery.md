# Swamping and masking in Markov boundary discovery 

Xuqing Liu ${ }^{1,2} \cdot$ Xinsheng Liu ${ }^{1}$


#### Abstract

This paper considers the problems of swamping and masking in Markov boundary discovery for a target variable. There are two potential reasons for swamping and masking: one is incorrectness of some conditional independence (CI) tests, and the other is violation of local composition. First, we explain why the incorrectness of CI tests may lead to swamping and masking, analyze how to reduce the incorrectness of CI tests, and build an algorithm called LRH under local composition. For convenience, we integrate the two existing algorithms, IAMB and KIAMB, and our LRH into an algorithmic framework called LCMB. Second, since LCMB may prematurely stop searching if local composition is violated, a theoretical improvement on LCMB is made as follows: we analyze how to resume the stopped search of LCMB, construct a corresponding algorithmic framework called WLCMB, and show that its correctness only needs a more relaxed condition than that of LCMB. Finally, we apply LCMB and WLCMB to a number of Bayesian networks. The experimental results reveal that LRH is much more efficient than the existing two LCMB algorithms and that WLCMB can further improve LCMB.


Keywords Bayesian network $\cdot$ Markov blanket $\cdot$ Markov boundary $\cdot$ Masking $\cdot$ Swamping

[^0][^1]
[^0]:    This research was supported by the National Natural Science Foundation of China (No.: 61374183) and the Humanistic and Social Science Foundation of Ministry of Education of China (No.: 12YJA630122).

    Editor: James Cussens.

    囚 Xinsheng Liu
    xsliu@nuaa.edu.cn
    Xuqing Liu
    liuxuqing688@163.com
    1 State Key Laboratory of Mechanics and Control of Mechanical Structures, Institute of Nano Science and Department of Mathematics, Nanjing University of Aeronautics and Astronautics, Nanjing 210016, China

    2 Faculty of Mathematics and Physics, Huaiyin Institute of Technology, Huai'an 223003, China

# 1 Introduction 

Markov blankets (Mb) and Markov boundaries (MB) are two basic concepts in Bayesian networks (BNs). For a target variable $T$, its Mb is a variable set conditioned on which all other variables are probabilistically independent of $T$, and its MB is a minimal Mb ; that is, an MB is the smallest set containing all variables carrying the information about $T$ that cannot be obtained from other variables (Pearl 1988).

The discovery of MBs plays a central role in feature selection (Pellet and Elisseeff 2008; Aliferis et al. 2010a, b; Fu and Desmarais 2010). Feature selection aims to identify the minimal subset of features required for probabilistic classification, with the following three-fold objective (Guyon and Elisseeff 2003): improving the prediction performance of the predictors, providing faster and more cost-effective predictors, and facilitating a better understanding of the underlying process that generated the data. Pearl (1988) showed the conditional probability for the target variable given other variables can be replaced by the one with an MB as the conditional set. Pellet and Elisseeff (2008) proved an MB is the theoretically optimal set of features if the faithfulness condition is satisfied. Further, under certain assumptions about the learner and the loss function, MB is the solution to the feature selection problem (Tsamardinos and Aliferis 2003; Masegosa and Moral 2012; Statnikov et al. 2013). Hence, MB discovery techniques are receiving more and more attention in recent years.

In the literature, there have been lots of MB discovery approaches, including independencebased and score-based ones, as well as some hybrid methods. This paper focuses on the former.

The Koller-Sahami (KS) algorithm, put forward by Koller and Sahami (1996), is the first technique of creating a framework used to define the theoretically optimal filter method for a feature selection problem. It provides no theoretical guarantees to soundness (Tsamardinos et al. 2003a). The grow-shrink (GS) algorithm, which was proposed by Margaritis and Thrun (1999, 2000), consists of the growing phase and the shrinking phase. In its growing phase, as long as there exists a variable conditionally dependent on the target given the candidate Markov blanket (CMb), this variable will be added to the CMb until no more such variables exist. All members of an MB as well as some false positives enter the CMb at the end of the growing phase. The shrinking phase detects those false positives and removes them. The GS algorithm was theoretically proven by Margaritis and Thrun (1999) to be correct under the assumption that all the conditional independence (CI) tests are correct. Here, a CI test for a hypothesis is said to be correct, if the corresponding statistical decision is correctly made by using a testing method.

Tsamardinos et al. (2003a) pointed out that GS uses a static and potentially inefficient heuristic in the growing phase, and then they presented a variant of GS called the incremental association Markov boundary (IAMB) algorithm by employing a dynamic heuristic: IAMB reorders the remaining variables by means of an association function at each iteration such that the spouses of the target can enter the CMb early and thus fewer false positives are added to the CMb during the growing phase. HITON (Aliferis et al. 2003) also uses a similar static but slightly more efficient heuristic compared to GS.

Similar dynamic heuristics are employed by some variants of IAMB (Tsamardinos and Aliferis 2003; Yaramakala and Margaritis 2005; Zhang et al. 2010). This strategy is also used by divide-and-conquer search techniques, such as the max-min Markov boundary algorithm (Tsamardinos et al. 2003b), the parents and children based Markov boundary (PCMB) algorithm (Peña et al. 2007), the breadth first search of Markov boundary algorithm introduced by

(Fu and Desmarais 2007), and the algorithms included in the algorithmic framework called GLL (Aliferis et al. 2010a).

Under the faithfulness condition, most of these algorithms efficiently retrieve an approximate MB. Peña et al. (2007) relaxed the faithfulness condition to the composition assumption. Based on this relaxation, they put forward a stochastic version of IAMB called KIAMB by introducing a randomization parameter $K \in[0,1]$. Here, $K$ specifies the trade-off between greediness and randomness in the search: KIAMB with $K=1$ coincides with IAMB which is completely greedy, while KIAMB with $K=0$ is a completely random approach expected to discover all the MBs of the target variable with a nonzero probability if running repeatedly for enough times. Further, Statnikov et al. (2013) relaxed the condition for IAMB (also suitable for KIAMB) to be correct to local composition. Another stochastic search technique is the Bayesian stochastic search of Markov boudaries algorithm (Masegosa and Moral 2012), which tries to get all MBs by running a large number of times; it provides some alternative results by scoring the different obtained solutions.

Usually, these algorithms perform well in MB discovery. However, there are two potential problems for them, either of which may lead to what we call swamping and masking in some situations, and such cases may frequently arise in practice. See (P1) and (P2) below for these two problems. Here, swamping means a true positive becomes a false negative, while masking means a true negative becomes a false positive. These two terminologies are often used for outlier detection (Ben-Gal 2005; Hadi et al. 2009): swamping means some non-outliers are identified as outliers, while masking means some outliers are not identified; outliers mask themselves by swamping some non-outliers. We borrow them here to characterize the two results of (P1) (P2) in MB discovery because of their similar behaviors in "masking" themselves and "swamping" others. Definition 2 gives the mathematical description for them.
P1 Incorrect CI tests may lead to swamping and masking. Each MB discovery algorithm assumes that all CI tests are correct. This assumption requires the data efficiency of an algorithm. The parents and children based algorithms, such as PCMB and the algorithms in the GLL framework, are data efficient but not time efficient; in contrast, IAMB and KIAMB are time efficient but not data efficient (Schlüter 2014). Once one or more false positives with spuriously high dependence on the target enter the CMb , the cascading errors (Bromberg and Margaritis 2009) caused by them may lead to the exclusion of some true positives. Example 1 provides an illustration.
P2 Violation of the faithfulness condition (or the local composition assumption) may also lead to swamping and masking. The faithfulness condition is usually required by the parents and children based algorithms (Peña et al. 2007; Aliferis et al. 2010a), while the relaxed assumption, local composition, is needed by IAMB and KIAMB. However, the faithfulness condition and the local composition assumption may be violated in practice. Example 2 illustrates this possibility.

Example 1 Yaramakala (2004) considered the following scenario: in a BN over $\left\{T, X, Y_{1}, Y_{2}\right.$, $Z\}$ with the graph given in (a) of Fig. 1 as its directed acyclic graph (DAG), the node $Z$ is a nonmember of the MB for the target $T$, but it may have the highest association with $T$ because there exist multiple paths for the flow of information between $T$ and $Z: T \rightarrow Y_{1} \rightarrow Z$ and $T \rightarrow Y_{2} \rightarrow Z$. In this case, $Z$ becomes the first node entering the CMb of IAMB. Peña et al. (2007) instantiated the same scenario to a problem of signal transmission and reception. Yaramakala (2004) and Peña et al. (2007) thought that there may be some true negatives entering the CMb in the growing phase such that the time cost increases. This is natural. However, a more important but neglected problem is that these false positives may bring some cascading errors (Bromberg and Margaritis 2009), which may further cause incorrectness of CI tests

![img-0.jpeg](img-0.jpeg)

Fig. 1 An illustration on why incorrect CI tests may lead to swamping and masking
and thus the exclusion of some true positives. For example, $Y_{1}$ or $Y_{2}$ may eventually become a false negative. Hence, it is meaningful to consider the problem of (P1), and what we can do is to prevent too many true negatives with spuriously high dependence on the target from entering the CMb in the growing phase.

Example 2 Consider a target variable $T$ which has three potential features $X, Y$, and $Z$. As we know, the total information about $T$ carried by $X$ and $Y$ can be decomposed into: (a) the unique information carried by $X$, (b) the unique information carried by $Y$, (c) the redundant information shared by $X$ and $Y$, and (d) the synergistic information carried jointly by $X$ and $Y$ (Williams and Beer 2010; Rauh et al. 2014). Assume $Z$ carries all of (a)(b)(c) and some (but not all) of (d). It follows that: (1) $Z$ has the highest association with $T$; (2) $T$ is conditionally independent of $X$ given $Z$; (3) $T$ is conditionally independent of $Y$ given $Z$; (4) $T$ is conditionally dependent on $\{X, Y\}$ given $Z$; (5) $T$ is conditionally independent of $Z$ given $X$ and $Y$. Then, $\{X, Y\}$ is the unique MB of $T$ in $\{T, X, Y, Z\}$. However, IAMB can not find this MB correctly. Specifically, in the growing phase of IAMB, $Z$ enters the CMb and then it excludes $X$ and $Y$; in the shrinking phase, $Z$ remains in the CMb. Similarly, it follows that KIAMB can not find $\{X, Y\}$ with a probability not $<66.67 \%$ for any value of $K \in[0,1]$. We no longer consider other above-mentioned algorithms because of the violation of the faithfulness condition. Therefore, it is meaningful to consider the problem of (P2).

These two examples indicate that both the incorrectness of some CI tests and the violation of local composition may lead to swamping and masking. This motivates us to build novel algorithms which are expected to (1) reduce the incorrectness of CI tests, and (2) overcome swamping and masking to a large extent in the case of violating the local composition assumption.

The remainder of this paper is organized as follows. Section 2 provides necessary preliminaries. Section 3 presents the IAMB and KIAMB algorithms, relaxes the notions of Mb and MB, and proves some new results for IAMB and KIAMB. Section 4 addresses the problem of (P1), puts forward a method of including as few true negatives as possible in the growing phase, and builds an algorithm called LRH, which is proven to be correct under the relaxed local composition assumption. The ALARM network is employed to show the data efficiency and time efficiency of LRH. In addition, this section gives a post-processing technique to reduce incorrectness of CI tests kept in the shrinking phase. For convenience, IAMB, KIAMB, and LRH are integrated into an algorithmic framework called LCMB. To resume the search stopped in the growing phase of LCMB, Sect. 5 considers (P2) and constructs an efficient algorithmic framework called WLCMB. The application to ALARM indicates WLCMB

can further improve LCMB in data efficiency. Section 6 applies LCMB and WLCMB to several large networks. Section 7 concludes this paper.

# 2 Preliminary 

In the paper, we denote a variable and its value by upper-case and lower-case letters in italics (e.g., $X, x$ ), a set of variables and its value by upper-case and lower-case bold letters in italics (e.g., $\boldsymbol{X}, \boldsymbol{x}$ ). The difference between $\boldsymbol{X}$ and $\boldsymbol{Y}$ is denoted by $\boldsymbol{X} \backslash \boldsymbol{Y}$. For brevity, we write $(\boldsymbol{X} \backslash \boldsymbol{Y}) \backslash \boldsymbol{Z}$ as $\boldsymbol{X} \backslash \boldsymbol{Y} \backslash \boldsymbol{Z}$. In addition, we use $|\boldsymbol{X}|$ to denote the number of variables involved in $X$.

Suppose we have a joint probability distribution $\mathbb{P}$ over $\boldsymbol{V} \triangleq\left\{X_{1}, \ldots, X_{p}\right\}$ and a DAG $\mathbb{G}$ with the variables in $\boldsymbol{V}$ as its nodes. We say $(\mathbb{G}, \mathbb{P})$ satisfies the Markov condition if every $X \in \boldsymbol{V}$ is conditionally independent of its nondescendants given its parents. Further, $(\mathbb{G}, \mathbb{P})$ is called a BN if it satisfies the Markov condition. Furthermore, $(\mathbb{G}, \mathbb{P})$ satisfies the faithfulness condition if, based on the Markov condition, $\mathbb{G}$ entails all and only CIs in $\mathbb{P}$ (Pearl 1988; Neapolitan 2004).

Denote $\boldsymbol{X} \Perp \boldsymbol{Y} \mid \boldsymbol{Z}$ (resp., $\boldsymbol{X} \not \boldsymbol{X} \mid \boldsymbol{Z}$ ), if $\boldsymbol{X}$ and $\boldsymbol{Y}$ are conditionally independent (resp., dependent) given $\boldsymbol{Z}$. The following properties describe the relations among CI statements (Pearl 1988; Statnikov et al. 2013). For any $\boldsymbol{X}, \boldsymbol{Y}, \boldsymbol{Z}, \boldsymbol{W} \subseteq \boldsymbol{V}$, we have (1) symmetry: $\boldsymbol{X} \Perp \boldsymbol{Y} \mid \boldsymbol{Z} \Leftrightarrow \boldsymbol{Y} \Perp \boldsymbol{X} \mid \boldsymbol{Z}$; (2) decomposition: $\boldsymbol{X} \Perp \boldsymbol{Y} \cup \boldsymbol{W} \mid \boldsymbol{Z}$ implies $\boldsymbol{X} \Perp \boldsymbol{Y} \mid \boldsymbol{Z}$ and $\boldsymbol{X} \Perp \boldsymbol{W} \mid \boldsymbol{Z}$; (3) weak union: $\boldsymbol{X} \Perp \boldsymbol{Y} \cup \boldsymbol{W} \mid \boldsymbol{Z}$ implies $\boldsymbol{X} \Perp \boldsymbol{Y} \mid \boldsymbol{Z} \cup \boldsymbol{W}$; (4) contraction: $\boldsymbol{X} \Perp \boldsymbol{Y} \mid \boldsymbol{Z} \cup \boldsymbol{W}$ and $\boldsymbol{X} \Perp \boldsymbol{W} \mid \boldsymbol{Z}$ imply $\boldsymbol{X} \Perp \boldsymbol{Y} \cup \boldsymbol{W} \mid \boldsymbol{Z}$. Further, if $\mathbb{P}$ is strictly positive, then besides (1) (4) we also have (5) intersection: $\boldsymbol{X} \Perp \boldsymbol{Y} \mid \boldsymbol{Z} \cup \boldsymbol{W}$ and $\boldsymbol{X} \Perp \boldsymbol{W} \mid \boldsymbol{Z} \cup \boldsymbol{Y}$ imply $\boldsymbol{X} \Perp \boldsymbol{Y} \cup \boldsymbol{W} \mid \boldsymbol{Z}$. Furthermore, if $\mathbb{P}$ is faithful to a DAG $\mathbb{G}$, then besides (1) (5) we also have (6) composition:

$$
\boldsymbol{X} \Perp \boldsymbol{Y} \mid \boldsymbol{Z} \& \boldsymbol{X} \Perp \boldsymbol{W} \mid \boldsymbol{Z} \Rightarrow \boldsymbol{X} \Perp \boldsymbol{Y} \cup \boldsymbol{W} \mid \boldsymbol{Z}
$$

As we know, faithfulness implies composition, but not vice versa. For composition, Statnikov et al. (2013) provided a relaxed version called local composition: we say $\boldsymbol{T} \subseteq \boldsymbol{V}$ satisfies the local composition property, if (1) holds for any $\boldsymbol{X}, \boldsymbol{Y}, \boldsymbol{Z} \subseteq \boldsymbol{V} \backslash \boldsymbol{T}$. We also say $\boldsymbol{T} \subseteq \boldsymbol{V}$ satisfies the local composition property with respect to some particular $\boldsymbol{Z} \subseteq \boldsymbol{V} \backslash \boldsymbol{T}$, if (1) holds for any $\boldsymbol{X}, \boldsymbol{Y} \subseteq \boldsymbol{V} \backslash \boldsymbol{Z} \backslash \boldsymbol{T}$.

Conditional mutual information (CMI) is one of the basic tools for testing CIs. Denote the CMI between $\boldsymbol{X}$ and $\boldsymbol{Y}$ conditioned on $\boldsymbol{Z}$ by $\mathbb{I}(\boldsymbol{X} ; \boldsymbol{Y} \mid \boldsymbol{Z})$. Then $\mathbb{I}(\boldsymbol{X} ; \boldsymbol{Y} \mid \boldsymbol{Z}) \geqslant 0$, with equality holding if and only if $\boldsymbol{X} \Perp \boldsymbol{Y} \mid \boldsymbol{Z}$ (Zhang and Guo 2006). For a practical problem, we cannot access to the true CMI; instead, we use its empirical estimate, denoted by $\mathbb{I}_{\boldsymbol{D}}(\boldsymbol{X} ; \boldsymbol{Y} \mid \boldsymbol{Z})$, based on the data $\boldsymbol{D}$ (Cheng et al. 2002). Note that $\mathbb{I}_{\boldsymbol{D}}(\boldsymbol{X} ; \boldsymbol{Y} \mid \boldsymbol{Z}) \geqslant 0$ also holds for any $\boldsymbol{X}, \boldsymbol{Y}, \boldsymbol{Z} \subseteq \boldsymbol{V}$. Denote the $G^{2}$ statistic by $G^{2}(\boldsymbol{X} ; \boldsymbol{Y} \mid \boldsymbol{Z}) \triangleq 2 n \cdot \mathbb{I}_{\boldsymbol{D}}(\boldsymbol{X} ; \boldsymbol{Y} \mid \boldsymbol{Z})$, which approximates to the chisquare variate with $r \triangleq\left(r_{\boldsymbol{X}}-1\right)\left(r_{\boldsymbol{Y}}-1\right) r_{\boldsymbol{Z}}$ degrees of freedom, namely $G^{2}(\boldsymbol{X} ; \boldsymbol{Y} \mid \boldsymbol{Z}) \dot{\sim} \chi^{2}(r)$, where $r_{\boldsymbol{\xi}}$ represents the number of configurations for $\boldsymbol{\xi}$ (de Campos 2006). Denote the $p$ value by $p_{\boldsymbol{D}}(\boldsymbol{X} ; \boldsymbol{Y} \mid \boldsymbol{Z})=\mathbb{P}\left\{\chi^{2}(r) \geqslant G^{2}(\boldsymbol{X} ; \boldsymbol{Y} \mid \boldsymbol{Z})\right\}$. Then, the $G^{2}$ test asserts $\boldsymbol{X} \Perp \boldsymbol{Y} \mid \boldsymbol{Z}$ if $p_{\boldsymbol{D}}(\boldsymbol{X} ; \boldsymbol{Y} \mid \boldsymbol{Z})>\alpha$ for a significance level $\alpha$, and concludes $\boldsymbol{X} \not \boldsymbol{\mu} \boldsymbol{Y} \mid \boldsymbol{Z}$ if $p_{\boldsymbol{D}}(\boldsymbol{X} ; \boldsymbol{Y} \mid \boldsymbol{Z}) \leqslant \alpha$. In this paper, $\alpha$ is set to be 0.05 . Accordingly, the negative $p$ value is used as the association function, $f_{\boldsymbol{D}}$, as Tsamardinos et al. (2006), Aliferis et al. (2010a, b), and Statnikov et al. (2013) did: $f_{\boldsymbol{D}}(\boldsymbol{X} ; \boldsymbol{Y} \mid \boldsymbol{Z}) \triangleq-\mathbb{P}\left\{\chi^{2}(r) \geqslant G^{2}(\boldsymbol{X} ; \boldsymbol{Y} \mid \boldsymbol{Z})\right\}$.

The chain rule for CMI (Cover and Thomas 2006) is useful to prove the main results of this paper: $\mathbb{I}\left(\boldsymbol{X} ; \boldsymbol{Y}_{1} \cup \boldsymbol{Y}_{2} \mid \boldsymbol{Z}\right)=\mathbb{I}\left(\boldsymbol{X} ; \boldsymbol{Y}_{1} \mid \boldsymbol{Z}\right)+\mathbb{I}\left(\boldsymbol{X} ; \boldsymbol{Y}_{2} \mid \boldsymbol{Z} \cup \boldsymbol{Y}_{1}\right)$ holds for any four sets of variables $\boldsymbol{X}, \boldsymbol{Y}_{1}, \boldsymbol{Y}_{2}$, and $\boldsymbol{Z}$ from $\boldsymbol{V}$. This formula remains valid if we replace $\mathbb{I}(\cdot)$ with $\mathbb{I}_{\boldsymbol{D}}(\cdot)$.

Fig. 2 The DAG of the ASIA network used to illustrate the notions of d-separation and MB
![img-1.jpeg](img-1.jpeg)

Another notion closely related to CI is d-separation (Pearl 1988; Neapolitan 2004). For a DAG $\mathbb{G}$ over $\boldsymbol{V}$, letting $\boldsymbol{X}, \boldsymbol{Y}, \boldsymbol{Z} \subseteq \boldsymbol{V}$ be disjoint, we say $\boldsymbol{Z}$ d-separates $\boldsymbol{X}$ and $\boldsymbol{Y}$ if it blocks every path between $\boldsymbol{X}$ and $\boldsymbol{Y}$, and if this is the case we write $\boldsymbol{X} \perp \boldsymbol{Y} \mid \boldsymbol{Z}$. Here, $\boldsymbol{Z}$ blocking a path $\mathfrak{p}$ means that $\mathfrak{p}$ has a head-to-tail node or a tail-to-tail node belonging to $\boldsymbol{Z}$, or that $\mathfrak{p}$ has a head-to-head node $C$ such that $C$ and its all descendants are not in $\boldsymbol{Z}$. As well known, $\boldsymbol{X} \perp \boldsymbol{Y} \mid \boldsymbol{Z} \Rightarrow \boldsymbol{X} \Perp \boldsymbol{Y} \mid \boldsymbol{Z}$, if $(\mathbb{G}, \mathbb{P})$ is a BN (Neapolitan 2004). This implication provides a convenient way of identifying CIs. For example, consider a BN with the graph presented in Fig. 2 as its DAG. Then, $X_{2}$ and $X_{8}$ are d-separated by $\left\{X_{4}, X_{5}\right\}$, meaning $X_{2} \perp X_{8} \mid\left\{X_{4}, X_{5}\right\}$ and thus $X_{2} \Perp X_{8} \mid\left\{X_{4}, X_{5}\right\} ; X_{3}$ and $X_{4}$ are d-separated by $\varnothing$, meaning $X_{3} \perp X_{4}$, so $X_{3} \Perp X_{4}$. Note that these two probabilistic CIs can not be directly derived from the Markov condition.

In what follows, the concepts of Mb and MB are presented (Pearl 1988; Neapolitan 2004).
Definition 1 For $T \in \boldsymbol{V}$, we call $\boldsymbol{M} \subseteq \boldsymbol{V} \backslash\{T\}$ a Markov blanket (Mb) of $T$ if $T \Perp \boldsymbol{V} \backslash \boldsymbol{M} \backslash\{T\} \mid \boldsymbol{M}$. Further, a Markov boundary (MB) of $\boldsymbol{T}$ is any Mb such that none of its proper subsets is an Mb of $T$.

According to Definition 1, an Mb, saying $\boldsymbol{M}$, of $T$ is a set of variables which can shield $T$ from all other variables, while an MB is a minimal Mb. Moreover, by means of the chain rule for CMI, it can be easily shown that $\mathbb{I}(T ; \boldsymbol{M})=\max _{\boldsymbol{N} \subseteq \boldsymbol{V} \backslash\{T\}} \mathbb{I}(T ; \boldsymbol{N})=\mathbb{I}(T ; \boldsymbol{V} \backslash\{T\})$, so $\boldsymbol{M}$ carries all information about $T$ carried by all the variables. Furthermore, the following results are well known in the literature (Pearl 1988; Neapolitan 2004; Statnikov et al. 2013): (a) if $(\mathbb{G}, \mathbb{P})$ is a BN, then for $T \in \boldsymbol{V}$ the set of its all parents, children, and spouses is an Mb of $T$ (we denote it by $\boldsymbol{M}_{T}$ ); (b) if $\mathbb{P}$ satisfies the intersection property, then $T$ has a unique MB; (c) if $(\mathbb{G}, \mathbb{P})$ satisfies the faithfulness condition, then $\boldsymbol{M}_{T}$ is the unique MB of $T$.

Consider again the BN with the graph presented in Fig. 2 as its DAG. In this BN, it is seen that $\boldsymbol{M}_{X_{4}} \triangleq\left\{X_{2}, X_{6}, X_{3}\right\}$ is an Mb of $X_{4}$; further, $\boldsymbol{M}_{X_{4}}$ is the unique MB of $X_{4}$ if the faithfulness condition is satisfied. Similarly, $\boldsymbol{M}_{X_{2}} \triangleq\left\{X_{4}, X_{5}\right\}$ is the unique MB of $X_{2}$ under the faithfulness condition.

Based on the notion of MB, we give the definition for swamping and masking:
Definition 2 (Swamping and masking) For $T \in \boldsymbol{V}$, let $\boldsymbol{M} \subseteq \boldsymbol{V} \backslash\{T\}$ be a true MB of $T$, $\boldsymbol{M}_{\mathbb{A}} \triangleq(\boldsymbol{M} \backslash \boldsymbol{X}) \cup \boldsymbol{Y}$ be the output of an MB discovery algorithm, $\mathbb{A}$, with $\boldsymbol{X} \subseteq \boldsymbol{M}$ and $\boldsymbol{Y} \subseteq \boldsymbol{V} \backslash \boldsymbol{M} \backslash\{T\}$. Assume $\boldsymbol{M}_{\mathbb{A}}$ is not an MB of $T$. Then, we say (1) swamping occurs with respect to $\boldsymbol{M}$, if $\boldsymbol{X} \neq \varnothing$; and (2) masking occurs with respect to $\boldsymbol{M}$, if $\boldsymbol{Y} \neq \varnothing$.

The MB of a target may not be unique. This is why we use "a" or "an" in Definition 2. This definition is applicable whether the MB is unique or not. Lemeire (2007) provided a case of violating the uniqueness of MB called information equivalence. $\boldsymbol{X}$ and $\boldsymbol{Y}$ are called information equivalent with respect to $T$ given $\boldsymbol{Z} \subseteq \boldsymbol{V} \backslash \boldsymbol{X} \backslash \boldsymbol{Y} \backslash\{T\}$ if the following four conditions hold: $T \not X \mid \boldsymbol{Z}, T \not Y \mid \boldsymbol{Z}, T \Perp \boldsymbol{X} \mid \boldsymbol{Y} \cup \boldsymbol{Z}$, and $T \Perp \boldsymbol{Y} \mid \boldsymbol{X} \cup \boldsymbol{Z}$.

# 3 Two typical algorithms and a further discussion 

In this section, we concisely present two typical MB discovery algorithms: IAMB (Tsamardinos et al. 2003a) and KIAMB (Peña et al. 2007). Then, we make a further discussion about them. Considering that these two algorithms are correct under the local composition assumption (Theorem 1) or the Markov local composition assumption (Definition 4), we put them into an algorithmic framework called LCMB. Here, "LC" means "Markov local composition".

IAMB is an enhanced variant of GS. Tsamardinos et al. (2003a) showed the correctness of IAMB under the faithfulness condition; Peña et al. (2007) relaxed the condition to the composition assumption; Statnikov et al. (2013) further relaxed the condition to the local composition assumption. The pseudo code for IAMB is described in Algorithm 1. In the

```
Algorithm 1: LCMB and its three instantiations: IAMB, KIAMB, and LRH
    Procedure: \(\boldsymbol{M} \leftarrow \mathrm{LCMB}(\mathrm{A} ; \boldsymbol{D}, T, \boldsymbol{W}, \boldsymbol{B})\)
    Input: A is a two-phase MB algorithm including the required parameters (for IAMB,
        \(\mathrm{A}=(\mathrm{IAMB})\); for KIAMB, \(\mathrm{A}=(\mathrm{KIAMB}, K)\), in which \(K \in[0,1]\) is a randomization
        parameter; for LRH, \(\mathrm{A}=(\mathrm{LRH}, k)\), in which \(k(\geqslant 1)\) is an integer denoting the number of
        nodes entering the CMb at each iteration); \(\boldsymbol{D}\) is a data matrix; \(T\) is a target; \(\boldsymbol{W}\) is a
        whitelist; \(\boldsymbol{B}\) is a blacklist.
    Output: The output, \(\boldsymbol{M}\), is an MB of \(T\) under the Markov local composition assumption.
    //main procedure:
        \(\boldsymbol{M} \leftarrow \operatorname{LCMB}(\mathrm{A} ; \boldsymbol{D}, T, \boldsymbol{W}, \boldsymbol{B})\)
    \(1 M \leftarrow \mathrm{FW}(\mathrm{A} ; \boldsymbol{D}, T, \boldsymbol{W}, \boldsymbol{B})\)
    \(2 M \leftarrow \mathrm{BW}(\boldsymbol{D}, T, \boldsymbol{M}, \boldsymbol{W})\)
    3 return \(M\)
    //IAMB: \(\boldsymbol{M} \leftarrow \operatorname{LCMB}((\) IAMB \() ; \boldsymbol{D}, T, \boldsymbol{W}, \boldsymbol{B})\)
    \(1 M \leftarrow \mathrm{FW}((\) IAMB \() ; \boldsymbol{D}, T, \boldsymbol{W}, \boldsymbol{B})\)
    \(2 M \leftarrow \mathrm{BW}(\boldsymbol{D}, T, \boldsymbol{M}, \boldsymbol{W})\)
    3 return \(M\)
    //KIAMB:
        \(\boldsymbol{M} \leftarrow \operatorname{LCMB}((\) KIAMB, \(K) ; \boldsymbol{D}, \boldsymbol{T}, \boldsymbol{W}, \boldsymbol{B})\)
    \(1 M \leftarrow \mathrm{FW}((\) KIAMB, \(K) ; \boldsymbol{D}, T, \boldsymbol{W}, \boldsymbol{B})\)
    \(2 M \leftarrow \mathrm{BW}(\boldsymbol{D}, T, \boldsymbol{M}, \boldsymbol{W})\)
    3 return \(M\)
    //LRH: \(\boldsymbol{M} \leftarrow \operatorname{LCMB}((\mathrm{LRH}, k) ; \boldsymbol{D}, \boldsymbol{T}, \boldsymbol{W}, \boldsymbol{B})\)
    \(1 M \leftarrow \mathrm{FW}((\mathrm{LRH}, k) ; \boldsymbol{D}, T, \boldsymbol{W}, \boldsymbol{B})\)
    \(2 M \leftarrow \mathrm{BW}(\boldsymbol{D}, T, \boldsymbol{M}, \boldsymbol{W})\)
    3 return \(M\)
    //growing phase of IAMB:
        \(\boldsymbol{M} \leftarrow \mathrm{FW}((\) IAMB \() ; \boldsymbol{D}, T, \boldsymbol{W}, \boldsymbol{B})\)
    \(1 M \leftarrow W\)
    2 while \(M\) has changed do
        \(Y \leftarrow \arg \max _{X \in \boldsymbol{V} \backslash \boldsymbol{M} \backslash \boldsymbol{B} \backslash\{T\}} f_{\boldsymbol{D}}(T ; X \mid \boldsymbol{M})\)
        if \(T \not X Y \mid M\) then
            \(\boldsymbol{M} \leftarrow \boldsymbol{M} \cup\{Y\}\)
        end
    7 end
    //growing phase of KIAMB:
        \(\boldsymbol{M} \leftarrow \mathrm{FW}((\) KIAMB, \(K) ; \boldsymbol{D}, T, \boldsymbol{W}, \boldsymbol{B})\)
```

```
1 \(\boldsymbol{M} \leftarrow \boldsymbol{W}\)
    2 while \(M\) has changed do
        \(M_{1} \leftarrow\{X \in V \backslash M \backslash B \backslash\{T\}: T \not X \mid M\}\)
        if \(M_{1} \neq \varnothing\) then
            \(M_{2} \leftarrow K^{ \pm}\)nodes randomly from \(M_{1}\)
            \(Y \leftarrow \arg \max _{X \in M_{2}} f_{\boldsymbol{D}}(T ; X \mid \boldsymbol{M})\)
            \(\boldsymbol{M} \leftarrow \boldsymbol{M} \cup\{Y\}\)
        end
    9 end
    //growing phase of LRH:
        \(\boldsymbol{M} \leftarrow \mathrm{FW}((\mathrm{LRH}, k) ; \boldsymbol{D}, T, \boldsymbol{W}, \boldsymbol{B})\)
    \(1 M \leftarrow W\)
    2 while \(M\) has changed do
        \(M_{1} \leftarrow\{X \in V \backslash M \backslash B \backslash\{T\}: T \not X \mid M\}\)
        if \(M_{1} \neq \varnothing\) then
            \(\boldsymbol{M}_{2} \leftarrow\) refined \(\boldsymbol{M}_{1}\) according to
            exclusion of SEI
            \(Y \leftarrow k^{ \pm}\)nodes from \(M_{2}\) with highest
            associations
            \(\boldsymbol{M} \leftarrow \boldsymbol{M} \cup \boldsymbol{Y}\)
        end
    9 end
    //shrinking phase: \(\boldsymbol{M} \leftarrow \mathrm{BW}(\boldsymbol{D}, T, \boldsymbol{M}, \boldsymbol{W})\)
    1 foreach \(X \in M \backslash W\) do
        if \(T \Perp X \mid M \backslash\{X\}\) then
            \(\boldsymbol{M} \leftarrow \boldsymbol{M} \backslash\{X\}\)
        end
    5 end
```

algorithm, the function $f_{D}$ denotes a heuristic measurement of the association between variables based on the data $\boldsymbol{D}$ (Tsamardinos et al. 2003a; Peña et al. 2007). Two widely used selections for $f_{D}$ are CMI (Cheng et al. 2002; Tsamardinos et al. 2003a) and the negative $p$ value (Tsamardinos et al. 2006; Aliferis et al. 2010a, b; Statnikov et al. 2013). This paper employs the latter. Yaramakala (2004) also suggested an equivalent version of the negative $p$ value.

KIAMB is a stochastic extension of IAMB. It embeds a randomization parameter $K \in[0,1]$ used to trade off greediness and randomness. If taking $K=1$, KIAMB reduces to IAMB. Peña et al. (2007) proved the correctness of KIAMB under the composition assumption. By the proof, the local composition assumption is sufficient for this algorithm to be correct. Its pseudo code is also described in Algorithm 1. In the growing phase of KIAMB, $K^{*}=$ $\max \left\{1,\left\lfloor\left|\boldsymbol{M}_{1}\right| \cdot K\right\rfloor\right\}$.

It is noted here that Algorithm 1 predefines a whitelist $\boldsymbol{W}$ and a blacklist $\boldsymbol{B}$, which can be determined by virtue of expert knowledge or empirical information. In the original IAMB and KIAMB, both $\boldsymbol{W}$ and $\boldsymbol{B}$ are taken as the empty set by default.

Recall that a CI test for a hypothesis is said to be correct if the corresponding statistical decision is correctly made by using a testing method. Based on this terminology, the correctness of IAMB and KIAMB is presented as follows (Tsamardinos et al. 2003a; Peña et al. 2007; Statnikov et al. 2013).

Theorem 1 (Correctness of IAMB and KIAMB) Assume $T$ satisfies the local composition assumption, and all CI tests are correct. Then (i) IAMB outputs an MB of $T$; (ii) KIAMB outputs an $M B$ of $T$ for any $K \in[0,1]$.

By this theorem and the two examples presented in Sect. 1, IAMB and KIAMB may fail to output an MB when some CI tests are incorrect or local composition is violated. In what follows, we give a naive definition for the outputs of these algorithms and then make a further discussion. Note that an MB can be equivalently defined to be any Mb such that $T \not N \mid \boldsymbol{M} \backslash \boldsymbol{N}$ holds for any nonempty $\boldsymbol{N} \subseteq \boldsymbol{M}$, in view of the contraction property and the decomposition property.

Definition 3 For $T \in \boldsymbol{V}$, we call $\boldsymbol{M} \subseteq \boldsymbol{V} \backslash\{T\}$ a weak Markov blanket (WMb) of $T$ if $T \Perp X \mid \boldsymbol{M}$ for any $X \in \boldsymbol{V} \backslash \boldsymbol{M} \backslash\{T\}$. Further, a weak Markov boundary (WMB) of $T$ is any WMb such that $T \not N \mid \boldsymbol{M} \backslash \boldsymbol{N}$ holds for any nonempty $\boldsymbol{N} \subseteq \boldsymbol{M}$.

This definition is introduced to characterize the true output of an existing MB discovery algorithm (such as IAMB or KIAMB) in the case that local composition is violated. One did not care about such a definition in the early literature because the faithfulness condition or the composition property (and thus local composition) was usually assumed to be a precondition in an MB algorithm; but this definition becomes necessary if we try to explore what are influencing the efficiency of the existing MB discovery algorithms. "Appendix 1" gives a further explanation about why we define the notion of WMB in this way. Clearly, a WMb is an Mb under local composition, while a WMB is an MB under the same assumption. The following theorem describes the relation between Definition 3 and Algorithm 1.

Theorem 2 Assume all CI tests are correct. Then IAMB or KIAMB for any $K \in[0,1]$ outputs a WMB of $T$.

Proof Denoting the output of IAMB or KIAMB at the end of the growing phase by $\boldsymbol{M}$, it is clear that $\boldsymbol{M}$ is a WMb, since $T \Perp \boldsymbol{X} \mid \boldsymbol{M}$ holds for any $X \in \boldsymbol{V} \backslash \boldsymbol{M} \backslash\{T\}$ owing to the exit

condition. Let the final output of either algorithm be $\boldsymbol{N} \subseteq \boldsymbol{M}$. Without loss of generality, assume that $\boldsymbol{M} \backslash \boldsymbol{N}=\left\{X_{1}, \ldots, X_{k}\right\}$ and that $k \geqslant 1$, in which $X_{1}, \ldots, X_{k}$ are removed from $\boldsymbol{M}$ in sequence, that is, $T \Perp X_{i} \mid \boldsymbol{M} \backslash\left\{X_{1}, \ldots, X_{i}\right\}$ holds for $i=1, \ldots, k$. By the chain rule for CMI, we have

$$
\begin{aligned}
\mathbb{I}(T ; \boldsymbol{M} \backslash \boldsymbol{N} \mid \boldsymbol{N}) & =\mathbb{I}\left(T ;\left\{X_{1}, \ldots, X_{k}\right\} \mid \boldsymbol{M} \backslash\left\{X_{1}, \ldots, X_{k}\right\}\right) \\
& =\sum_{i=k}^{1} \mathbb{I}\left(T ; X_{i} \mid \boldsymbol{M} \backslash\left\{X_{1}, \ldots, X_{i}\right\}\right)=0
\end{aligned}
$$

so $T \Perp \boldsymbol{M} \backslash \boldsymbol{N} \mid \boldsymbol{N}$, which combined with $T \Perp X \mid \boldsymbol{M}$ (or equivalently, $T \Perp X \mid(\boldsymbol{M} \backslash \boldsymbol{N}) \cup \boldsymbol{N}$ ) and the contraction property implies $T \Perp(\boldsymbol{M} \backslash \boldsymbol{N}) \cup\{X\} \mid \boldsymbol{N}$. By the decomposition property, this further means $T \Perp X \mid \boldsymbol{N}$ holds for any $X \in(\boldsymbol{V} \backslash \boldsymbol{M} \backslash\{T\}) \cup(\boldsymbol{M} \backslash \boldsymbol{N})=\boldsymbol{V} \backslash \boldsymbol{N} \backslash\{T\}$. Hence, $\boldsymbol{N}$ is WMb.

Finally, we prove $\boldsymbol{N}$ is a WMB. In fact, suppose there is some nonempty $\left\{Y_{1}, \ldots, Y_{\ell}\right\} \triangleq$ $\boldsymbol{Y} \subseteq \boldsymbol{N}$ such that $T \Perp \boldsymbol{Y} \mid \boldsymbol{N} \backslash \boldsymbol{Y}$. Here, the exit condition of the shrinking phase means $\ell \geqslant 2$. It follows that

$$
\begin{aligned}
0 & =\mathbb{I}(T ; \boldsymbol{Y} \mid \boldsymbol{N} \backslash \boldsymbol{Y})=\mathbb{I}\left(T ;\left\{Y_{1}, \ldots, Y_{\ell}\right\} \mid \boldsymbol{N} \backslash\left\{Y_{1}, \ldots, Y_{\ell}\right\}\right) \\
& =\mathbb{I}\left(T ;\left\{Y_{2}, \ldots, Y_{\ell}\right\} \mid \boldsymbol{N} \backslash\left\{Y_{1}, \ldots, Y_{\ell}\right\}\right)+\mathbb{I}\left(T ; Y_{1} \mid \boldsymbol{N} \backslash\left\{Y_{1}\right\}\right) \\
& \geqslant \mathbb{I}\left(T ; Y_{1} \mid \boldsymbol{N} \backslash\left\{Y_{1}\right\}\right) \geqslant 0
\end{aligned}
$$

Therefore, $\mathbb{I}\left(T ; Y_{1} \mid \boldsymbol{N} \backslash\left\{Y_{1}\right\}\right)=0$, which contradicts $T \not \leq Y_{1} \mid \boldsymbol{N} \backslash\left\{Y_{1}\right\}$ according to the exit condition of the shrinking phase. This indicates $\boldsymbol{N}$ is a WMB. The proof is completed.

Based on the notion of WMb, we relax the local composition assumption as follows:
Definition 4 (Markov local composition) We say $T \in \boldsymbol{V}$ satisfies the Markov local composition property, if $T$ satisfies the local composition property with respect to any WMb of $T$ or, equivalently, if every WMb of $T$ in $\boldsymbol{V}$ is an Mb .

As seen, IAMB and KIAMB remain correct under the Markov local composition assumption. This is why we call them both LCMB algorithms.

# 4 LRH algorithm: lessen swamping, resist masking, and highlight the true positives 

This section addresses the problem of (P1) posed in Sect. 1. First, we exemplify the situations that some CI tests are incorrect, even when the data size is large. Then, we analyze how to add as few false positives as possible to the CMb and thus to reduce the incorrectness of CI tests such that swamping and masking get alleviated. Finally, we present the resulting algorithm called LRH, which can lessen swamping, resist masking, and highlight the true positives.

### 4.1 An exemplification

Consider the well-known ALARM network (Beinlich et al. 1989), which is shown in Fig. 3. Observe that there are many situations of multiple channels for the flow of information. In these situations, IAMB may suffer swamping and masking caused by the incorrectness of some associated CI tests. For example, taking $T \triangleq X_{2}$ with $\boldsymbol{M}_{T} \triangleq\left\{X_{23}, X_{27}, X_{29}\right\}$ as its unique MB under the faithfulness condition, the detailed operating steps of discovering

![img-2.jpeg](img-2.jpeg)

Fig. 3 ALARM network with 37 nodes and 46 edges used to illustrate that the incorrectness of some CI tests may lead to swamping and masking due to the multiple channels for the flow of information. For example, $\left\{X_{23}, X_{27}, X_{29}\right\}$ is the unique MB of $X_{2}$ under the faithfulness condition. However, IAMB outputs an incorrect $\mathrm{MB},\left\{X_{4}, X_{18}, X_{23}\right\}$, while LRH outputs the true MB

Table 1 Details of IAMB for discovering the MB, $\left\{X_{23}, X_{27}, X_{29}\right\}$, of $T \triangleq X_{2}$ in the ALARM network with $\alpha=0.05$, based on a data set of size 5000


The association is taken as the negative $p$ value of the $G^{2}$-test. In the growing phase, IAMB adds the nodes $X_{1}, X_{4}, X_{18}$, and $X_{23}$ in sequence to the CMb ; in the shrinking phase, IAMB removes $X_{1}$ from the CMb . Thus, IAMB incorrectly outputs $\left\{X_{4}, X_{18}, X_{23}\right\}$ as the MB of $T$. The same result is returned when taking $\alpha$ as 0.01 or 0.005 or 0.001
the MB is presented in Table 1. Following the steps in the table, IAMB first adds $X_{1}, X_{4}$, $X_{18}$, and $X_{23}$ to the CMb , and then removes $X_{1}$. This algorithm outputs an incorrect MB, $\left\{X_{4}, X_{18}, X_{23}\right\}$, for the target $T$. As seen, swamping occurs since the two true positives, $X_{27}$

and $X_{29}$, become false negatives; masking also follows because the two true negatives, $X_{4}$ and $X_{18}$, become false positives by the end of the shrinking phase.

We now analyze why swamping and masking happen by virtue of Fig. 3. Note that $T$ contains the information propagated by $X_{23}, X_{27}$, and $X_{29}$. By means of these three nodes, there are no fewer than two disjoint links without any converging nodes for the flow of information between $T$ and one of $X_{1}, X_{4}$, and $X_{18}$. Specifically, we have

- $T \leftarrow X_{23}\left(\right.$ or $\left.X_{27}\right) \rightarrow X_{22} \rightarrow X_{1}$ and $T \leftarrow X_{29} \rightarrow X_{1}$ connect $T$ and $X_{1}$;
- $T \leftarrow X_{23}$ (or $X_{27}$ ) $\rightarrow X_{22} \rightarrow X_{4}$ and $T \leftarrow X_{29} \rightarrow X_{21} \rightarrow X_{15} \rightarrow X_{4}$ connect $T$ and $X_{4}$
- $T \leftarrow X_{29} \rightarrow X_{28} \rightarrow X_{18}$ and $T \leftarrow X_{23}\left(\right.$ or $\left.X_{27}\right) \rightarrow X_{22} \rightarrow X_{21} \rightarrow X_{19} \rightarrow X_{18}$ connect $T$ and $X_{18}$.

This means $X_{1}$ or $X_{4}$ or $X_{18}$ has higher association with $T$ than each of $X_{23}, X_{27}$, and $X_{29}$, so $X_{1}, X_{4}$, and $X_{18}$ enter the CMb in sequence in the growing phase. After adding $X_{23}$, the remaining two true positives (i.e., $X_{27}$ and $X_{29}$ ) are excluded, due to the incorrectness of the following two CI tests:

- The true CMI, $\mathbb{I}\left(T ; X_{27} \mid X_{1}, X_{4}, X_{18}, X_{23}\right) \approx 0.0331>0$, indicating $T \nless X_{27} \mid\left\{X_{1}, X_{4}\right.$, $\left.X_{18}, X_{23}\right\}$, but the $p$ value of the $G^{2}$-test, $p_{D}\left(T ; X_{27} \mid X_{1}, X_{4}, X_{18}, X_{23}\right) \approx 1.0000$, is far larger than $\alpha$, meaning the opposite assertion $T \Perp X_{27} \mid\left\{X_{1}, X_{4}, X_{18}, X_{23}\right\}$;
- The true CMI, $\mathbb{I}\left(T ; X_{29} \mid X_{1}, X_{4}, X_{18}, X_{23}\right) \approx 0.0352>0$, indicating $T \nless X_{29} \mid\left\{X_{1}, X_{4}\right.$, $\left.X_{18}, X_{23}\right\}$. On the other hand, $p_{D}\left(T ; X_{29} \mid X_{1}, X_{4}, X_{18}, X_{23}\right) \approx 1.0000 \gg \alpha$ asserts $T \Perp X_{29} \mid\left\{X_{1}, X_{4}, X_{18}, X_{23}\right\}$.

This explains why the incorrectness of some CI tests may lead to swamping. Further, in the shrinking phase, the two false positives, $X_{4}$ and $X_{18}$, can not be identified, because not all information about $T$ is shielded since $X_{27}$ and $X_{29}$ are excluded. This means masking may follow if swamping occurs.

This analysis shows the incorrectness of CI tests may bring swamping and masking. However, we need to use "all CI tests are correct" as a precondition for an MB algorithm. Hence, what we can do is to reduce the incorrectness of CI tests as far as possible. Considering an incorrect CI test is usually the case of accepting a false hypothesis (Cochran 1954; Bromberg and Margaritis 2009), a good MB algorithm should add as few false positives as possible to the CMb in the growing phase, because too many false positives may make the detection of a true dependence hard.

# 4.2 Method 

Example 1 presents a simplified scenario where swamping and masking happen due to the incorrectness of CI tests. By the graphical structure that (a) of Fig. 1 illustrates, the target $T$ propagates its information to $X, Y_{1}$, and $Y_{2}$. Then, $Y_{1}$ and $Y_{2}$ transmit the information to $Z$. In other words, $Z$ collects the information about $T$ through $Y_{1}$ and $Y_{2}$, so it may carry more information about $T$ than either $Y_{1}$ or $Y_{2}$. Mathematically, $\mathbb{I}(T ; Z) \geqslant \max \left\{\mathbb{I}\left(T ; Y_{1}\right), \mathbb{I}\left(T ; Y_{2}\right)\right\}$ may hold. This indicates $Z$ has spuriously high association with $T$. For a larger BN such as the ALARM network, there may be many similar nodes to $Z$. Hence, we can add as few false positives as possible to the CMb by identifying such nodes.

Suppose the transmission via $Y_{2}$ is blocked as (b) of Fig. 1 shows. That is, $T \rightarrow Y_{1} \rightarrow Z$ becomes the only remaining channel between $T$ and $Z$. In this case, the data-processing inequality (Cover and Thomas 2006) gives $\mathbb{I}\left(T ; Z \mid Y_{2}\right) \leqslant \mathbb{I}\left(T ; Y_{1} \mid Y_{2}\right)$. Similarly, if the transmission via $Y_{1}$ is blocked as shown in (c) of Fig. 1, then $\mathbb{I}\left(T ; Z \mid Y_{1}\right) \leqslant \mathbb{I}\left(T ; Y_{2} \mid Y_{1}\right)$. This

means $Z$ can no longer effectively collect the information about $T$ once one or more channels between $T$ and $Z$ are blocked, so $Y_{1}$ or $Y_{2}$ will enter the CMb before $Z$. Without loss of generality, suppose the CMb is obtained as $\boldsymbol{M} \triangleq\left\{X, Y_{1}\right\}$ after two steps of the growing phase. Then, further blocking implies $T \not X Y_{2}|\boldsymbol{M} \cup\{Z\}$ and $T \Perp Z|\boldsymbol{M} \cup\left\{Y_{2}\right\}$. Hence, $Y_{2}$ enters $\boldsymbol{M}$ and thus $\boldsymbol{M}=\left\{X, Y_{1}, Y_{2}\right\}$. Finally, $T \Perp Z \mid \boldsymbol{M}$, meaning the growing phase ends.

As seen, the method of blocking one or more information channels can add as few false positives as possible to the CMb in the growing phase, because the remaining information (after blocking information channels) about $T$ carried by one node is closer to the true unique information about $T$ carried by this node. Therefore, this method can reduce swamping and masking caused by the problem of (P1).

Motivated by this idea, denoting the CMb by $\boldsymbol{M}$, we select the subsequent additions according to the following selection-exclusion-inclusion (SEI) procedure:
(a) Selection Let $\boldsymbol{M}_{1} \triangleq\{X \in \boldsymbol{V} \backslash \boldsymbol{M} \backslash \boldsymbol{B} \backslash\{T\}: T \not X| \boldsymbol{M}\}$ be the set of all nodes having information channels reaching $T$ other than those through $\boldsymbol{M}$. The nodes in $\boldsymbol{M}_{1}$ are the candidates preparing to enter the CMb in the current step.
(b) Exclusion If $\boldsymbol{M}_{1}$ is empty, the shrinking phase ends; if $\left|\boldsymbol{M}_{1}\right|=1$, add the only node in $\boldsymbol{M}_{1}$ to $\boldsymbol{M}$ and then go to (a) of the next iteration; otherwise, the method of blocking information channels is used. Put $\boldsymbol{M}_{2} \triangleq\left\{X \in \boldsymbol{M}_{1}: T \not X|M \cup\{Z\}\right.$ holds for any $Z \in$ $\boldsymbol{N}_{X}$ \} and $\boldsymbol{M}_{3} \triangleq \boldsymbol{M}_{1} \backslash \boldsymbol{M}_{2}$, in which $\boldsymbol{N}_{X} \triangleq\left\{Y \in \boldsymbol{M}_{1} \backslash\{X\}: X \not Y|M\right\}$ denotes the set of all nodes having information channels reaching $T$ and $X$ other than those through $\boldsymbol{M}$. This heuristic is inspired by the notion of 1-step dependence coefficient (de Campos 2006; Martínez-Rodríguez et al. 2008; Lee et al. 2012). If $\boldsymbol{M}_{2}=\varnothing$, modify it as $\boldsymbol{M}_{2} \triangleq\{Y\}$ with $Y=\arg \max _{X \in \boldsymbol{M}_{1}} f_{\boldsymbol{D}}(T ; X \mid \boldsymbol{M})$. All nodes in $\boldsymbol{M}_{3}$ (with spuriously high dependence on $T$ ) are excluded. This step can effectively reduce the possibility of adding too many false positives to the CMb . A further discussion about the exclusion procedure is given in Sect. 7.
(c) Inclusion Let $\boldsymbol{Y}$ be a set of $k^{*} \triangleq \min \left\{k,\left|\boldsymbol{M}_{2}\right|\right\}$ nodes from $\boldsymbol{M}_{2}$ with the highest associations with $T$ : take

$$
g_{\boldsymbol{D}}\left(T ; X \mid \boldsymbol{M}, \boldsymbol{N}_{X}\right)=\min _{Z \in \boldsymbol{N}_{X}} f_{\boldsymbol{D}}(T ; X \mid \boldsymbol{M} \cup\{Z\})
$$

and let $\boldsymbol{Y}=\left\{X_{(1)}, \ldots, X_{\left(k^{*}\right)}\right\}$, with $g_{\boldsymbol{D}}\left(T ; X_{(1)} \mid \boldsymbol{M}, \boldsymbol{N}_{X_{(1)}}\right) \geqslant \cdots \geqslant g_{\boldsymbol{D}}\left(T ; X_{\left(\left|\boldsymbol{M}_{2}\right|\right)}\right.$ $\left|\boldsymbol{M}, \boldsymbol{N}_{X_{\left(\mid M_{2}\right)}}\right)$. Add the nodes in $\boldsymbol{Y}$ to $\boldsymbol{M}$. Here, $k(\geqslant 1)$ is the maximal number of nodes entering the CMb at each iteration. This paper uses $k=3$.

Repeat (a)(b)(c) until the exit condition stated in (b) is satisfied (i.e., $\boldsymbol{M}_{1}$ is empty). After that, refine $\boldsymbol{M}$ by virtue of the shrinking phase.

This is the basic method of designing the new algorithm, LRH (presented in the next subsection). It will be seen that the algorithm performs well in lessening swamping, resisting masking, and highlighting the true positives. This is why we call it the LRH algorithm.

# 4.3 LRH algorithm with application to the ALARM network 

By the description given in Sect.4.2, we present the LRH algorithm in Algorithm 1. LRH consists of two phases: in the growing phase, the SEI procedure is iteratively implemented to search an Mb which contains as few false positives as possible; in the shrinking phase, the Mb is refined to become an MB. Specifically, the selection, exclusion, and inclusion procedures of SEI are implemented in Line 3, Line 5, and Line 7, respectively, in the growing phase of LRH. As the following theorem shows, LRH is correct under the local composition assumption

or the Markov local composition assumption. Hence, LRH is also an LCMB algorithm. The proof of this theorem is similar to that of Theorem 2, so we omit it here.

Theorem 3 (Correctness of LRH) Assume all CI tests are correct. Then LRH outputs a WMb of $T$ for any $k \geqslant 1$. Further, if $T$ satisfies the (Markov) local composition assumption, then LRH outputs an MB of $T$.

Now we consider the computational complexities of the three LCMB algorithms. Usually, the number of CI tests can be employed to measure the complexity of a CI-based MB discovery algorithm (Tsamardinos et al. 2003a, 2006; Aliferis et al. 2010a). In this sense, IAMB and KIAMB have the same complexity $O\left(|\boldsymbol{V}| \cdot\left|\boldsymbol{M}_{T}\right|\right)$ in the average case. By direct analysis, the complexity of LRH is $O\left[\left(|\boldsymbol{V}|+\left|\boldsymbol{M}_{T}\right|^{2}\right) \cdot\left|\boldsymbol{M}_{T}\right| / k\right]$. As we can see, LRH may need more CI tests than IAMB or KIAMB in each iteration; however, there may be fewer iterations in the growing phase of LRH, since multiple nodes are allowed to enter the CMb in each iteration (see, e.g., Tables 1 and 2 for an illustration). Also, the shrinking phase may also need fewer iterations because LRH usually add fewer true negatives to the CMb than IAMB or KIAMB by the end of the growing phase. Therefore, LRH is also time efficient like IAMB and KIAMB.

To demonstrate how LRH works, we apply this algorithm to the ALARM network. The detailed operating steps of LRH for discovering the MB of $T \triangleq X_{2}$ are presented in Table 2. Following the steps in the table, LRH first adds $\left\{X_{29}, X_{23}, X_{21}\right\}$ and $\left\{X_{27}\right\}$ to the CMb , and then removes the only one false positive, $X_{21}$. As expected, the two nodes, $X_{4}$ and $X_{18}$, with spuriously high dependence on the target are successfully identified before the inclusion procedure of SEI and, therefore, they will no longer swamp the true positives, $X_{27}$ and $X_{29}$. In comparison, IAMB adds these two (plus another) nonmembers of the true MB, namely, $X_{1}$, $X_{4}$, and $X_{18}$; the two true positives, $X_{27}$ and $X_{29}$, are then swamped. Although $X_{1}$ is finally removed, $X_{4}$ and $X_{18}$ continue to mask themselves, so IAMB gives an incorrect output.

There are many other similar situations for this network. Table 3 lists the results of the three LCMB algorithms (i.e., IAMB, KIAMB, and LRH) for all the 37 nodes as targets. For KIAMB, we take $K$ as $0.2,0.5$, and 0.8 ; all results for each KIAMB are averaged over five runs. This table consists of two aspects: MB and relative efficiency (RE), in which the RE of an obtained $\mathrm{MB}, \boldsymbol{M}$, is defined as

$$
\operatorname{RE}_{\boldsymbol{D}}(\boldsymbol{M}, T) \triangleq \min \left\{\mathbb{I}_{\boldsymbol{D}}(T ; \boldsymbol{M}) / \mathbb{I}_{\boldsymbol{D}}\left(T ; \boldsymbol{M}_{T}\right), 1\right\}
$$

This statistic is a naive estimate for $\operatorname{RE}(\boldsymbol{M}, T) \triangleq \mathbb{I}(T ; \boldsymbol{M}) / \mathbb{I}\left(T ; \boldsymbol{M}_{T}\right)$, which measures the performance that $\boldsymbol{M}$ carries the information about $T$. Table 3 indicates that:

- LRH retrieves 21 and 3 Mbs ; IAMB retrieves 8 and 5 Mbs ; and KIAMB with $K=0.5$ or $K=0.8$ performs nearly as well as IAMB, while KIAMB with $K=0.2$ performs poorly. Further, LRH possesses 34 out of the 37 maximal REs; IAMB possesses 14 maximal REs; and KIAMB with $K$ taken as $0.2,0.5$, and 0.8 possess 5,12 , and 12 maximal REs, respectively. This indicates LRH improves on IAMB and KIAMB greatly. The results also reveal that it is reasonable to use RE to measure the performance that a potential MB carries the information about the target. In addition, it should be mentioned here that each LCMB algorithm outputs several Mbs (supersets of the true MBs) after implementing the BW function (see Algorithm 1 for details). This type of masking is the consequence of the incorrectness of some associated CI tests. The next subsection will discuss this issue and provides an effective post-processing technique, called PostBW, to alleviate this type of masking.
- There are 12 cases where LRH outputs a proper subset of the true MB, and 9 such cases for IAMB. As seen, in any one such case for IAMB, LRH also outputs a proper subset

Table 2 Details of LRH for discovering the MB of $T \triangleq X_{2}$ on the ALARM network with $k=3$ and $\alpha=0.05$, based on a data set of size 5000


Table 2 continued


Conclusion: LRH outputs $\left{X_{23}, X_{27}, X_{29}\right}$ as the MB of $T$, which is correct

The association is taken as the negative $p$ value of the $G^{2}$-test. In the growing phase, LRH adds the nodes $\left{X_{29}, X_{23}, X_{21}\right}$ and $\left{X_{27}\right}$ in sequence to the CMb ; in the shrinking phase, LRH removes $X_{21}$ from the CMb. Thus, LRH retrieves the true MB, $\left{X_{23}, X_{27}, X_{29}\right}$, of $T$. The same result is returned when taking $k$ as 1 or 2 or 4 or 5 and taking $\alpha$ as 0.01 or 0.005 or 0.001

Table 3 Results of the LCMB algorithms applied to the ALARM network based on a data set of size 5000 $(\alpha=0.05)$


The backcolors are specified as follows: " $\square$ " denotes here is the largest RE; " $\square$ " denotes the true MB is found; " $\square$ " denotes a proper subset of the true MB is found; " $\square$ " denotes an Mb (instead of an MB) is found; others have no backcolor
of the true MB ( 5 cases) or the true MB (4 cases), but not vice versa. Therefore, LRH performs better in lessening swamping than IAMB. Taking $X_{12}$ as the target for example, IAMB adds $X_{5}, X_{7}, X_{8}, X_{9}, X_{10}, X_{13}$, and $X_{34}$ to the CMb in its growing phase, and then removes $X_{5}, X_{7}, X_{8}$, and $X_{9}$ in its shrinking phase to output $\left\{X_{10}, X_{13}, X_{34}\right\}$ as the MB of $X_{12}$; LRH adds $X_{10}, X_{13}, X_{16}$, and $X_{34}$ to the CMb in the growing phase, and no nodes are removed in the shrinking phase. As seen, $X_{16}$ is a spouse node of $X_{12}$

Table 4 Average REs and RTs of the LCMB algorithms applied to the ALARM network based on 10 data sets of different sizes (from 500 to 5000): each result is averaged over all the 37 nodes as targets


The backcolor indicates the performance of each algorithm with black corresponding to the maximal RE and blue to the minimal (for each case of data size)
but IAMB fails to include it. This is because IAMB adds too many false positives (i.e., $X_{5}, X_{7}, X_{8}$, and $X_{9}$ ) in its growing phase such that the CI test for the true dependence $X_{12} \notin X_{16} \mid\left\{X_{5}, X_{7}, X_{8}, X_{9} X_{10}, X_{13}, X_{34}\right\}$ incorrectly accepts the false hypothesis. LRH outputs the true MB of $X_{12}$. Similarly, if taking $X_{25}$ as the target, IAMB also fails to include the spouse node $X_{24}$, while LRH can output the true MB, $\left\{X_{23}, X_{24}, X_{26}\right\}$.

- For IAMB, there are 15 cases in which the outputs excludes one or more true positives and includes some false positives. This means IAMB suffers swamping and masking severely. In comparison, LRH yields only one such output; it successfully prevents those spuriously dependent variables from entering the CMb in most situations by virtue of the SEI procedure. Therefore, the heuristic involved in SEI is effective in lessening swamping, resisting masking, and highlighting the true positives.

By the above results, although LRH needs the same conditions for its correctness as IAMB and KIAMB, this algorithm is expected to be of higher performance than the other two LCMB algorithms for most situations in collecting the information about the target. To check whether this assertion holds for various data sizes, we implement the three LCMB algorithms on the ALARM network based on 10 data sets of sizes from 500 to 5000. The first part of Table 4 presents the corresponding REs, in which each result is averaged over all the 37 nodes as targets; the results for KIAMB are averaged over five different runs. By the table, LRH performs much better than IAMB and KIAMB in all cases; it can collect over $96 \%$ of the information about the targets when $n=2000$. This shows the data efficiency of the LRH algorithm.

Additionally, the average running time (RT; in seconds) of each LCMB algorithm is listed in the second part of Table 4. By the table, there is no significant difference between the RT of LRH and that of IAMB and KIAMB. Therefore, all the three LCMB algorithms are time efficient.

# 4.4 PostBW: a post-processing technique 

As we know, any Mb (resp., WMb) of a target will become an MB (resp., WMB) after being processed by BW, if all the CI tests involved are correct. However, Table 3 reveals that some false positives may remain in the Mb if some CI tests are incorrect. This subsection puts forward a post-processing technique, called PostBW, to alleviate such a type of masking. This technique is pseudo-coded in Algorithm 2.

Theorem 4 Let $\boldsymbol{M}$ be any $W M b$ (resp., an Mb) of $T$. Then, $\boldsymbol{M}$ is a WMB (resp., MB) of $T$ if and only if, for any $X \in \boldsymbol{M}$, there is no $Y \in \boldsymbol{V} \backslash \boldsymbol{M} \backslash\{T\}$ such that

$$
\begin{gathered}
T \Perp X \mid(\boldsymbol{M} \backslash\{X\}) \cup\{Y\} \text { and } \\
T \Perp Y \mid \boldsymbol{M} \backslash\{X\}
\end{gathered}
$$

hold simultaneously.
Before presenting the proof, we explain why PostBW may work after implementing BW. In fact, if a WMb (resp., an Mb), $\boldsymbol{M}$, is not a WMB (resp., an MB) of $T$, then

$$
T \Perp X \mid \boldsymbol{M} \backslash\{X\}
$$

holds for some $X \in \boldsymbol{M}$. However, if the corresponding CI test is incorrect, $X$ will remain in $\boldsymbol{M}$ and thus masking occurs; in this case, the way of identifying false positives from a WMb or Mb by means of the BW procedure becomes invalid. Theorem 4 provides an alternative way for this purpose. Imagine that a false positive can enter the CMb in the growing phase because it possesses the aptitude of masking itself, and this false positive continues to mask itself in the shrinking phase. In this scenario, BW only employs the members of $\boldsymbol{M}$, so it may fail to identify all false positives; alternatively, PostBW employs the members and nonmembers of $\boldsymbol{M}$ simultaneously, so it may find some false positives that are accepted by BW. This is why PostBW may further work after implementing the BW procedure.

Proof We first prove the necessity. Suppose there is some $X \in \boldsymbol{M}$ and some $Y \in \boldsymbol{V} \backslash \boldsymbol{M} \backslash\{T\}$ such that (4) and (5) hold simultaneously. Then, $T \Perp\{X, Y\} \mid \boldsymbol{M} \backslash\{X\}$, in view of the contraction property, so (6) follows from the decomposition property. Consider the case that $\boldsymbol{M}$ is a WMb, that is, $T \Perp Z \mid \boldsymbol{M}$ holds for any $Z \in \boldsymbol{V} \backslash \boldsymbol{M} \backslash\{T\}$. Equivalently, we have $T \Perp Z \mid(\boldsymbol{M} \backslash\{X\}) \cup\{X\}$.

```
Algorithm 2: PostBW and InterPostBW
    Procedure: \(\boldsymbol{M} \leftarrow \operatorname{PostBW}(\boldsymbol{D}, T, \boldsymbol{M}, \boldsymbol{W}, \boldsymbol{B})\) and \(\boldsymbol{M} \leftarrow \operatorname{InterPostBW}(\boldsymbol{D}, T, \boldsymbol{M}, \boldsymbol{W}, \boldsymbol{B})\)
    Input: \(\boldsymbol{D}\) is a data matrix; \(T\) is the target; \(\boldsymbol{M}\) is a WMb (resp., an Mb ) of \(T ; \boldsymbol{W}\) is a whitelist; \(\boldsymbol{B}\) is a
        blacklist.
    Output: The output, \(\boldsymbol{M}\), is a WMB (resp., MB) of \(T\).
    \(/ / \boldsymbol{M} \leftarrow \operatorname{PostBW}(\boldsymbol{D}, T, \boldsymbol{M}, \boldsymbol{W}, \boldsymbol{B})\)
    while \(\boldsymbol{M}\) has changed do
        if \(\exists X \in \boldsymbol{M} \backslash \boldsymbol{W} \& Y \in \boldsymbol{V} \backslash \boldsymbol{M} \backslash \boldsymbol{B} \backslash\{T\}\) s.t.
            (4)(5) then
            \(\boldsymbol{M} \leftarrow \boldsymbol{M} \backslash\{X\}\)
        end
    end
    return \(\boldsymbol{M}\)
    \(/ / \boldsymbol{M} \leftarrow \operatorname{InterPostBW}(\boldsymbol{D}, T, \boldsymbol{M}, \boldsymbol{W}, \boldsymbol{B})\)
```

```
1 while \(\boldsymbol{M}\) has changed do
2 \(\quad \boldsymbol{M} \leftarrow \operatorname{BW}(\boldsymbol{D}, T, \boldsymbol{M}, \boldsymbol{W})\)
3 if \(\boldsymbol{M}\) has not changed then
4 if \(\exists X \in \boldsymbol{M} \backslash \boldsymbol{W} \& Y \in \boldsymbol{V} \backslash \boldsymbol{M} \backslash \boldsymbol{B} \backslash\{T\}\) s.t.
            (4)(5) then
            \(\boldsymbol{M} \leftarrow \boldsymbol{M} \backslash\{X\}\)
        end
    end
    8 end
    9 return \(\boldsymbol{M}\)
```

This combined with (6) and the contraction property implies $T \Perp\{Z, X\} \mid \boldsymbol{M} \backslash\{X\}$. Hence, $T \Perp U \mid \boldsymbol{M} \backslash\{X\}$ holds for any $U \in(\boldsymbol{V} \backslash \boldsymbol{M} \backslash\{T\}) \cup\{X\}=\boldsymbol{V} \backslash(\boldsymbol{M} \backslash\{X\}) \backslash\{T\})$. This contradicts that $\boldsymbol{M}$ is a WMB. In the case that $\boldsymbol{M}$ is an Mb , we can similarly verify $T \Perp \boldsymbol{V} \backslash(\boldsymbol{M} \backslash\{X\}) \backslash$ $\{T\} \mid \boldsymbol{M} \backslash\{X\}$, which contradicts that $\boldsymbol{M}$ is an MB. The proof of the necessity is completed.

Now we show the sufficiency. For any $X \in \boldsymbol{M}$ and $Y \in \boldsymbol{V} \backslash \boldsymbol{M} \backslash\{T\}$, (4) and (5) do not hold simultaneously. In other words, $\mathbb{I}(T ; X \mid(\boldsymbol{M} \backslash\{X\}) \cup\{Y\})>0$ or $\mathbb{I}(T ; Y \mid \boldsymbol{M} \backslash\{X\}>0$. On the other hand, $T \Perp Y \mid \boldsymbol{M}$ holds since $\boldsymbol{M}$ is a WMb (or an Mb ), so $\mathbb{I}(T ; Y \mid \boldsymbol{M})=0$. By the chain rule for CMI, we have

$$
\begin{aligned}
\mathbb{I}(T ; X \mid \boldsymbol{M} \backslash\{X\}) & =\mathbb{I}(T ;\{X, Y\} \mid \boldsymbol{M} \backslash\{X\})-\mathbb{I}(T ; Y \mid(\boldsymbol{M} \backslash\{X\}) \cup\{X\}) \\
& =\mathbb{I}(T ;\{X, Y\} \mid \boldsymbol{M} \backslash\{X\})-\mathbb{I}(T ; Y \mid \boldsymbol{M}) \\
& =\mathbb{I}(T ; Y \mid \boldsymbol{M} \backslash\{X\})+\mathbb{I}(T ; X \mid(\boldsymbol{M} \backslash\{X\}) \cup\{Y\})-0 \\
& >0 .
\end{aligned}
$$

Therefore, $T \npreceq X \mid \boldsymbol{M} \backslash\{X\}$ holds for any $X \in \boldsymbol{M}$. By Theorem 2 (resp., Theorem 1), $\boldsymbol{M}$ is a WMB (resp., an MB) of $T$. The proof of the sufficiency is also completed.

To examine the performance of PostBW, we apply this procedure to the Mbs of $X_{3}, X_{6}$, $X_{8}, X_{11}$, and $X_{32}$ outputted by IAMB and LRH (see Table 3 for details). All the false positives accepted by BW are identified by PostBW and all the true MBs for these five targets are correctly discovered, except that the MB of $X_{11}$ is obtained as $\left\{X_{34}, X_{36}\right\}$. This shows that PostBW improves on BW substantially.

The computational complexity will increase if using PostBW: this procedure needs to do $O\left(\left|\boldsymbol{V}\right| \cdot\left|\boldsymbol{M}_{T}\right|\right)$ extra CI tests. A feasible solution for alleviating the resulted computational cost is to interleave PostBW with BW. Following this idea, we first implement BW in each iteration, and then activate PostBW if BW stops (in each iteration). For convenience, we call this interleaved procedure to be InterPostBW, and present its pseudo code in Algorithm 2. Finally, we apply InterPostBW to the Mbs of $X_{3}, X_{6}, X_{8}, X_{11}$, and $X_{32}$ outputted by IAMB and LRH. The results indicate InterPostBW has the same performance as PostBW in the sense of RE but it needs less RT for most situations.

# 5 WLCMB algorithmic framework 

Section 4 considered the problem of (P1) and proposed the LRH algorithm. As we saw, LRH is time efficient and much more data efficient than IAMB and KIAMB. However, as Example 2 shows, the Markov local composition assumption may be violated in practice and, if this is the case, LRH and the other two LCMB algorithms will stop to search before finding a true MB. In this section, we consider the problem of (P2) as follows: analyze why swamping and masking occur in the case of violating the Markov local composition assumption, discuss how to overcome them by resuming the stopped search of LCMB, and build a corresponding algorithmic framework.

Recalling Example 2 considered in Sect. 1, IAMB incorrectly outputs $\{Z\}$ as the MB of $T$, meaning the two true positives (i.e., $X$ and $Y$ ) are swamped by $Z$, and the false positive (i.e., $Z$ ) successfully masks itself. This indicates the dynamic heuristic in the growing phase of IAMB may lead to swamping, which may further bring masking. Similarly, LRH incorrectly outputs $\{Z\}$ as the MB of $T$, so LRH is also invalid for this type of swamping and masking. We also find that KIAMB as a random version of IAMB may discover the true MB if implementing it repeatedly; but this possibility is low. In addition, GS may find the true MB but this

depends on the preassigned priority of variables checked in every search; swamping and masking will happen if, for example, the priority is " $Z, X, Y$ " or " $Z, Y, X$ ". Thus, LCMB may prematurely terminate the growing phase if the CMb shields $T$ from every remaining single variable.

Let $\boldsymbol{M}$ be a true MB of $T$ in $\boldsymbol{V}$, and $\boldsymbol{M}_{\mathbb{A}} \triangleq(\boldsymbol{M} \backslash \boldsymbol{X}) \cup \boldsymbol{Y}$ be the output of an MB discovery algorithm, $\mathbb{A}$. Under the assumption that all CI tests are correct, Theorems 2 and 3 show that $\boldsymbol{M}_{\mathbb{A}}$ is a WMB of $T$ in $\boldsymbol{V}$. Further, $\boldsymbol{M}_{\mathbb{A}}$ is not an MB (and thus also not an Mb), if the local composition assumption with respect to $\boldsymbol{M}_{\mathbb{A}}$ is violated. In this case, $\boldsymbol{X} \neq \varnothing$, so swamping must occur. The questions are then: (1) why some useful information about $T$ carried by some variables in $\boldsymbol{V} \backslash \boldsymbol{M} \backslash\{T\}$ can not be captured successfully by $\mathbb{A}$ ? (2) how to resume the stopped search of $\mathbb{A}$ ?

For convenience, we denote $\boldsymbol{X} \triangleq\left\{X_{i_{1}}, \ldots, X_{i_{k}}\right\}$. First, we note the following conclusions:

- $T \not \boldsymbol{X}\left|\boldsymbol{M}_{\mathbb{A}}\right.$ : On the one hand, $\boldsymbol{M}$ is an MB, meaning $T \Perp \boldsymbol{V} \backslash \boldsymbol{M} \backslash\{T\} \mid \boldsymbol{M}$, so $T \Perp \boldsymbol{V} \backslash(\boldsymbol{M} \cup$ $\left.\boldsymbol{Y}) \backslash\{T\}\right|(\boldsymbol{M} \cup \boldsymbol{Y})$ in view of the weak union property. Equivalently, we have $T \Perp \boldsymbol{V} \backslash\left(\boldsymbol{M}_{\mathbb{A}} \cup\right.$ $\boldsymbol{X}) \backslash\{T\} \mid\left(\boldsymbol{M}_{\mathbb{A}} \cup \boldsymbol{X}\right)$. On the other hand, $\boldsymbol{M}_{\mathbb{A}}$ is not an Mb. Suppose $T \Perp \boldsymbol{X} \mid \boldsymbol{M}_{\mathbb{A}}$, then the contraction property indicates

$$
\left.\begin{array}{l}
T \Perp \boldsymbol{V} \backslash\left(\boldsymbol{M}_{\mathbb{A}} \cup \boldsymbol{X}\right) \backslash\{T\} \mid\left(\boldsymbol{M}_{\mathbb{A}} \cup \boldsymbol{X}\right) \\
T \Perp \boldsymbol{X} \mid \boldsymbol{M}_{\mathbb{A}}
\end{array}\right\} \Rightarrow T \Perp \boldsymbol{V} \backslash \boldsymbol{M}_{\mathbb{A}} \backslash\{T\} \mid \boldsymbol{M}_{\mathbb{A}}
$$

which contradicts that $\boldsymbol{M}_{\mathbb{A}}$ is not an Mb of $T$. Hence, $T \not X \mid \boldsymbol{M}_{\mathbb{A}}$.

- $k \geqslant 2$, and $T \Perp X_{i_{k}} \mid \boldsymbol{M}_{\mathbb{A}}$ holds for any $\ell=1, \ldots, k: \boldsymbol{M}_{\mathbb{A}}$ is a WMB (and thus a WMb) of $T$.
- $T \not N\left|\boldsymbol{M}_{\mathbb{A}}\right| \boldsymbol{N}$ holds for any nonempty $\boldsymbol{N} \subseteq \boldsymbol{M}_{\mathbb{A}}$ : This is because $\boldsymbol{M}_{\mathbb{A}}$ is a WMB of $T$.

The first two conclusions mean those true positives in $\boldsymbol{X}$ are swamped by $\boldsymbol{M}_{\mathbb{A}}$; the idea of the third one will be used in Definition 5. As seen in Example 2, the local composition assumption will be violated, if $\boldsymbol{M}_{\mathbb{A}}$ contains all unique information and all redundant information about $T$ carried by each $X_{i_{k}}$ as well as some (but not all) synergistic information about $T$ carried jointly by $X_{i_{1}}, \ldots, X_{i_{k}}$. That synergistic information about $T$ carried jointly by $X_{i_{1}}, \ldots, X_{i_{k}}$ and also by $\boldsymbol{M}_{\mathbb{A}}$ swamps the remaining useful information about $T$ carried by $X_{i_{1}}, \ldots, X_{i_{k}}$ but not by $\boldsymbol{M}_{\mathbb{A}}$. In this sense, swamping occurs and the search of LCMB ends; masking may then follow.

Definition 5 (WMB-supplementary) For $T \in \boldsymbol{V}$, let $\boldsymbol{M}_{\mathbb{A}}$ be a WMB of $T$ in $\boldsymbol{V}$. For $\boldsymbol{S} \subseteq \boldsymbol{M}_{\mathbb{A}}$, we call $\boldsymbol{N}_{\boldsymbol{S}}\left(\subseteq \boldsymbol{V} \backslash \boldsymbol{M}_{\mathbb{A}} \backslash\{T\}\right)$ a WMB-supplementary of $\boldsymbol{S}$, if the following two conditions hold: (1) $\left(\boldsymbol{M}_{\mathbb{A}} \backslash \boldsymbol{S}\right) \cup \boldsymbol{N}_{\boldsymbol{S}}$ is a WMb of $T$ in $\boldsymbol{V} \backslash \boldsymbol{S}$; and (2) $T \not N \mid\left(\boldsymbol{M}_{\mathbb{A}} \backslash \boldsymbol{S}\right) \cup\left(\boldsymbol{N}_{\boldsymbol{S}} \backslash \boldsymbol{N}\right)$ holds for any nonempty $\boldsymbol{N} \subseteq \boldsymbol{N}_{\boldsymbol{S}}$, if $\boldsymbol{N}_{\boldsymbol{S}} \neq \varnothing$.

The analysis before Definition 5 provides a method of resuming the search of LCMB: if putting a set of all (or part) of nodes from $\boldsymbol{M}_{\mathbb{A}}$, say $\boldsymbol{S}$, into the blacklist temporarily, some swamped information may be detected, so the search can continue. For convenience, we call $\boldsymbol{S}$ a swamping set. Observing again Example 2, $X$ and $Y$ are no longer swamped if removing $Z$ temporarily. Example 3 presented in the appendix gives a similar inspiration. If we can find one swamping set, $\boldsymbol{S}$, then we remove it temporarily to search the variables swamped by $\boldsymbol{S}$.

In practice, we can not seek $\boldsymbol{S}$ directly; instead, we may check every possible subset of $\boldsymbol{M}_{\mathbb{A}}$. The resulted heuristic is as follows: for any nonempty $\boldsymbol{S} \subseteq \boldsymbol{M}_{\mathbb{A}}$, find a WMB-supplementary of it, $\boldsymbol{N}_{\boldsymbol{S}}$. (1) If $\boldsymbol{S}$ is a swamping set, some of those variables (saying $X_{i_{1}}, \ldots, X_{i_{k}}$ ) swamped by $\boldsymbol{S}$ may be found and thus enter $\boldsymbol{N}_{\boldsymbol{S}} . X_{i_{1}}, \ldots, X_{i_{k}}$ contain some synergistic information

about $T$, some of which is carried by $\boldsymbol{S}$ and thus by $\boldsymbol{M}_{\mathbb{A}}$, and some other may not be carried by $\boldsymbol{M}_{\mathbb{A}}$. This means $\boldsymbol{T} \Perp \boldsymbol{N}_{\boldsymbol{S}} \mid \boldsymbol{M}_{\mathbb{A}}$. (2) Conversely, if $\boldsymbol{S}$ is not a swamping set, then $\boldsymbol{T} \Perp \boldsymbol{N}_{\boldsymbol{S}} \mid \boldsymbol{M}_{\mathbb{A}}$. In this sense, if $\boldsymbol{T} \Perp \boldsymbol{N}_{\boldsymbol{S}} \mid \boldsymbol{M}_{\mathbb{A}}$ holds for every $\boldsymbol{S}\left(\subseteq \boldsymbol{M}_{\mathbb{A}}\right)$, we may think $T$ has no swamping set, so in this case it is reasonable to assume $T$ satisfies local composition with respect to such a $\mathrm{WMB}, \boldsymbol{M}_{\mathbb{A}}$. Otherwise, once a swamping set, $\boldsymbol{S}$, is found, the growing phase stopped in $\mathbb{A}$ may resume, and we can update $\boldsymbol{M}_{\mathbb{A}}$ based on $\boldsymbol{M}_{\mathbb{A}}$ and $\boldsymbol{S}$. Repeat this procedure until no swamping sets can be found. This is a potentially feasible solution to the problem of (P2).

Following this way, we construct an LCMB-based algorithmic framework called WLCMB. Here, "W" refers to as "weak"; we call it WLCMB because it can output an MB under the weak Markov local composition assumption defined as below.

Definition 6 (Weak Markov local composition) We say $T$ satisfies the weak Markov local composition property, if every $\mathrm{WMB}, \boldsymbol{M}_{\mathbb{A}}$, of $T$ satisfying the following condition is an MB of $T$ : any $\boldsymbol{S} \subseteq \boldsymbol{M}_{\mathbb{A}}$ has a WMB-supplementary $\boldsymbol{N}_{\boldsymbol{S}}$ such that $T \Perp \boldsymbol{N}_{\boldsymbol{S}} \mid \boldsymbol{M}_{\mathbb{A}}$.

The pseudo code of WLCMB is described in Algorithm 3. By the algorithm, WLCMB interleaves LCMB (i.e., Line 7 of Algorithm 3) with the search-resuming procedure (i.e., Line 9, and Line 10 of Algorithm 3) by virtue of the ImpWMB function. If taking $\mathbb{A}$ as IAMB, KIAMB, and LRH, the corresponding WLCMB algorithm will be called WIAMB, WKIAMB, and WLRH, respectively. Moreover, the BW procedure in Algorithm 3 can also be replaced with PostBW or InterPostBW.

Theorem 5 (Correctness of WLCMB) Assume all CI tests are correct. Then WLCMB outputs a WMB of $T$ for any LCMB algorithm taken from [IAMB, KIAMB, LRH]. Further, if $T$ satisfies the weak Markov local composition assumption, then WLCMB outputs an MB of $T$.

Proof Put $\boldsymbol{N}_{\boldsymbol{S}} \triangleq \boldsymbol{M}_{\boldsymbol{S}} \backslash(\boldsymbol{M} \backslash \boldsymbol{S})$, where $\boldsymbol{M}_{\boldsymbol{S}}$ is derived in Line 7 of Algorithm 3. Similar to the proofs of Theorems 2 and 3, it can be shown that $\boldsymbol{N}_{\boldsymbol{S}}$ is a WMB-supplementary of $\boldsymbol{S}$. Denote the outputs of Line 1, Line 7, Line 9, and Line 10 in the $k$-th iteration $(k \geqslant 1$, if possible) by $\boldsymbol{M}^{(0)}, \boldsymbol{M}_{\boldsymbol{S}}^{(k)}, \boldsymbol{M}_{\mathrm{FW}}^{(k)}$, and $\boldsymbol{M}^{(k)}$, respectively, before the iterated procedure ends. Then, by the fact that FW collects more information about $T$ while BW removes redundant variables only, we have $\mathbb{I}\left(T ; \boldsymbol{M}^{(0)}\right)<\mathbb{I}\left(T ; \boldsymbol{M}^{(1)}\right)$, and

```
Algorithm 3: WLCMB
    Procedure: \(\boldsymbol{M} \leftarrow \mathrm{WLCMB}(\mathbb{A} ; \boldsymbol{D}, T, \boldsymbol{W}, \boldsymbol{B})\)
    Input: \(\mathbb{A}\) is an LCMB algorithm;
    \(\boldsymbol{D}\) is a data matrix; \(T\) is the target; \(\boldsymbol{W}\) is a whitelist; \(\boldsymbol{B}\) is a blacklist.
    Output: The output, \(\boldsymbol{M}\), is an MB of \(T\) under the weak Markov local composition assumption.
    //main procedure: \(\boldsymbol{M} \leftarrow \mathrm{WLCMB}(\mathbb{A} ; \boldsymbol{D}, T, \boldsymbol{W}, \boldsymbol{B}) \quad 6\) foreach \(S \subseteq \boldsymbol{M} \backslash \boldsymbol{W}\) do
    \(1 \boldsymbol{M} \leftarrow \operatorname{LCMB}(\mathbb{A} ; \boldsymbol{D}, T, \boldsymbol{W}, \boldsymbol{B}) \quad 7 \quad \boldsymbol{M}_{\boldsymbol{S}} \leftarrow \operatorname{LCMB}(\mathbb{A} ; \boldsymbol{D}, T, \boldsymbol{M} \backslash \boldsymbol{S}, \boldsymbol{B} \cup \boldsymbol{S})\)
    2 while \(\boldsymbol{M}\) has changed do
        \(\boldsymbol{M} \leftarrow \operatorname{ImpWMB}(\mathbb{A} ; \boldsymbol{D}, T, \boldsymbol{M}, \boldsymbol{W}, \boldsymbol{B})\)
    4 end
    5 return \(\boldsymbol{M}\)
    //sub-routine:
        \(\boldsymbol{M} \leftarrow \operatorname{ImpWMB}(\mathbb{A} ; \boldsymbol{D}, T, \boldsymbol{M}, \boldsymbol{W}, \boldsymbol{B})\)
```

```
6 foreach \(S \subseteq M \backslash W\) do
    \(7 \quad M_{S} \leftarrow \operatorname{LCMB}(\mathbb{A} ; D, T, M \backslash S, B \cup S)\)
    8 if \(T \Perp M_{S} \backslash(M \backslash S) \mid M\) then
        \(M_{\mathrm{FW}} \leftarrow \mathrm{FW}(\mathbb{A} ; D, T, M_{S} \cup S, B)\)
        \(M \leftarrow \mathrm{BW}\left(D, T, M_{\mathrm{FW}}, W\right)\)
        break
        end
    end
    end
```

$$
\begin{array}{rlr}
\mathbb{I}\left(T ; \boldsymbol{M}^{(k-1)}\right) & & \\
& <\mathbb{I}\left(T ; \boldsymbol{M}^{(k-1)}\right)+\mathbb{I}\left(T ; \boldsymbol{M}_{S}^{(k)} \backslash\left(\boldsymbol{M}^{(k-1)} \backslash \boldsymbol{S}\right) \mid \boldsymbol{M}^{(k-1)}\right) & \left(\) " $<$ " is due to Line 8) \\
& =\mathbb{I}\left(T ; \left[\boldsymbol{M}_{S}^{(k)} \backslash\left(\boldsymbol{M}^{(k-1)} \backslash \boldsymbol{S}\right)\right] \cup \boldsymbol{M}^{(k-1)}\right) & \text { (using the chain rule for } C M I \text { ) } \\
& =\mathbb{I}\left(T ; \boldsymbol{M}_{S}^{(k)} \cup \boldsymbol{S}\right) & \text { (since } \boldsymbol{M}^{(k-1)} \backslash \boldsymbol{S} \subseteq \boldsymbol{M}_{S}^{(k)}\right) \\
& \leqslant \mathbb{I}\left(T ; \boldsymbol{M}_{\mathrm{PS}}^{(k)}\right) & \text { (" } \leqslant \text { " is due to Line 9) } \\
& =\mathbb{I}\left(T ; \boldsymbol{M}^{(k)}\right) & \text { (" }={ }^{\prime \prime} \text { is due to Line 10) }
\end{array}
$$

Therefore, the exit condition, $T \Perp \boldsymbol{N}_{\boldsymbol{S}} \mid \boldsymbol{M}$ holding for any $\boldsymbol{S} \subseteq \boldsymbol{M}$ shown in Line 8, will be satisfied after a number of iterations. Once the exit condition is satisfied, the weak Markov local composition assumption indicates that the output of WLCMB is then an MB of $T$. The proof is completed.

Recall Example 2 presented in Sect. 1, where the Markov local composition assumption is violated. Specifically, $T \Perp X \mid Z, T \Perp Y \mid Z, T \neq\{X, Y\} \mid Z$, and $T \Perp Z \mid\{X, Y\}$. Using the notations employed in the proof of Theorem 5, we have

- IAMB and WIAMB: First, IAMB outputs $\boldsymbol{M}^{(0)}=\{Z\}$, which is not the MB of $T$. Taking $\boldsymbol{S}=\{Z\} \subseteq \boldsymbol{M}^{(0)}$, we obtain $\boldsymbol{M}_{\boldsymbol{S}}^{(1)}=\{X, Y\}$, meaning $T \not \boldsymbol{M}_{\boldsymbol{S}}^{(1)} \backslash\left(\boldsymbol{M}^{(0)} \backslash \boldsymbol{S}\right) \mid \boldsymbol{M}^{(0)}$ (i.e., $T \not\{X, Y\} \mid Z$ ). Further, $\boldsymbol{M}_{\mathrm{PS}}^{(1)}=\{X, Y, Z\}$ and $\boldsymbol{M}^{(1)}=\{X, Y\}$. Similarly, $\boldsymbol{M}^{(2)}=$ $\{X, Y\}=\boldsymbol{M}^{(1)}$. Thus, WIAMB ends, outputing $\{X, Y\}$ correctly.
- KIAMB and WKIAMB: The output of KIAMB may be $\boldsymbol{M}^{(0)}=\{X, Y\}$ or $\boldsymbol{M}^{(0)}=\{Z\}$. In either case, WKIAMB can output the correct MB. The details are omitted here.
- LRH and WLRH: First, LRH selects $\{X, Y, Z\}$ and excludes $\{X, Y\}$ in its SEI procedure. Therefore, LRH outputs $\boldsymbol{M}^{(0)}=\{Z\}$. The remaining process of WLRH is similar to that of WIAMB. Finally, WLRH outputs $\{X, Y\}$ correctly.

This illustrates how WLCMB works when the Markov local composition assumption is violated.

To examine the performance of WLCMB algorithms, we apply them to the ALARM network. Table 5 presents the corresponding results, including the outputted MBs of WIAMB and WLRH for all the 37 nodes as targets. The REs of each WLCMB are also given. By Tables 3 and 5, it is concluded that each WLCMB improves on the corresponding LCMB substantially. Specifically, IAMB retrieves 8 and 5 MBs , and yields 15 incorrect outputs, while WIAMB retrieves 17 and 1 MBs , and yields 12 incorrect outputs; LRH gives $21,3 \mathrm{MBs}$, and only one incorrect output, while WLRH yields $25,1 \mathrm{MBs}$, and no incorrect outputs. The results also show WLRH performs best.

Similar to Table 4, the first part of Table 6 lists the average REs of the three WLCMB algorithms applied to the ALARM network based on the same 10 data sets, in which each result is averaged over all the 37 nodes as targets. Comparing Table 6 with Table 4, it is seen that WLCMB performs better than LCMB for all cases of data sizes and thus is more data efficient.

We mention that WLCMB has a higher computational complexity than LCMB: the complexity of WLCMB is that of the associated LCMB multiplied by $2^{|\boldsymbol{M}|}$ in the average case. Hence, WLCMB usually needs longer RT to yield a better output than LCMB. This can be seen from the second part of Table 6, which provides the average RT of the three WLCMB algorithms applied to the ALARM network. The experimental results on several large networks given in Sect. 6 also show this assertion. This means we should trade off the expected RE and RT before deciding to select which MB discovery algorithm in practice.

Table 5 Results of the WLCMB algorithms applied to the ALARM network based on a data set of size 5000 $(\alpha=0.05)$


The backcolors are the same as in Table 3

# 6 Experimental results on large networks 

Tables 4 and 6 showed the superiority of LRH over IAMB and KIAMB in discovering an MB of the target for small BNs. The results also demonstrated the effectiveness of our WLCMB algorithmic framework in further improving the data efficiency of LCMB. This section applies the algorithms to some large BNs, based on the data sets of size 5000 used by Tsamardinos et al. (2006) and Aliferis et al. (2010a). These data sets are available at http://www.dsl-lab.org/ supplements/JMLR2008/. The used networks are representatives of a wide range of problem domains; Table 7 lists the numbers of nodes and edges for them. Tsamardinos et al. (2006)

Table 6 Average REs and RTs of the WLCMB algorithms applied to the ALARM network based on 10 data sets of different sizes (from 500 to 5000): each result is averaged over all the 37 nodes as targets


and Aliferis et al. (2010a) provided more details about these networks and the used data sets. For each BN, we also use a data set of size 2500 randomly drawn from the original data set to evaluate the performance of the algorithms in data efficiency.

For each network, 10 nodes are randomly selected as targets. These targets are listed in Table 7. Besides the REs and RTs, we also compute the weighted area under ROC curve (AUC) based on the naive Bayes classifier. For the case of size 5000, we randomly select 4000 instances as the training set and use the others as the testing set; for the case of size 2500 , we randomly select 2000 and 500 out of 5000 instances as the training set and the testing set, respectively. Table 7 presents all the results. For each case, the AUC of the true $\mathrm{MB}, \boldsymbol{M}_{T}$, of the target is provided to compare how the performance of an algorithm is close to the best. Each result is averaged over that of the 10 targets. In addition, according to the recommendation of Peña et al. (2007) and the results given in Sects. 4 and 5, we take $K=0.8$ in KIAMB and WKIAMB.

Table 7 indicates our algorithms are applicable to large BNs. By the table, it is concluded that: (1) for the three LCMB algorithms, LRH performs best in the senses of RE and AUC; (2) for the three WLCMB algorithms, WLRH performs best in both senses; (3) for each LCMB and its corresponding WLCMB, the latter improves the data efficiency of the former. In addition, we note a natural conclusion that the results on the case of a larger data size are more desirable in most situations than that on the case of a smaller data size. In brief, LRH and WLRH have the best performances in solving (P1) and (P2), respectively. Considering that WLRH usually needs a longer RT than LRH as Sect. 5 analyzes, we should first trade off the RE and the RT in practice and then choose between these two algorithms.

# 7 Conclusion and discussions 

This paper considered two potential reasons for causing swamping and masking. For the problem of (P1) that incorrect CI tests may lead to swamping and masking, we proposed the LRH algorithm to alleviate the influence that swamping and masking brings under the local composition assumption. The application to the ALARM network shows the superiority of

Table 7 Results of LCMBs and WLCMBs applied to the six large BNs based on two data sets of sizes 5000 and 2500: average AUCs, average REs, and average RTs (in seconds)


LRH over the other two LCMB algorithms. For the problem of (P2) that the violation of local composition may also lead to swamping and masking, we put forward the WLCMB algorithmic framework. Theoretically, WLCMB can improve LCMB, because LCMB stops searching once local composition is violated with respect to the obtained WMb in the growing phase, while WLCMB may break this abnormal exit and then continues to search those swamped true positives. The further application to the ALARM network supports this theoretical argument.

Motivated by one referee, we mention that Tables 3 and 5 also indirectly reflect the frequencies of swamping and masking with respect to IAMB or LRH or WIAMB or WLRH. Specifically, in both tables, " $\square$ " indicates neither swamping nor masking; " $\square$ " indicates swamping (but no masking); " $\square$ " indicates masking (but no swamping); others indicate both swamping and masking. In this sense, Table 8 counts the frequencies that swamping or masking occurs when applied to the ALARM network based on the used data set of size 5000. The results reveal that LRH and WLRH perform much better than IAMB and WIAMB in lessening swamping and resisting masking. The results also show that WIAMB (resp., WLRH) improves IAMB (resp., LRH) to some extent.

As a remark, we mention here that we modify $\boldsymbol{M}_{2}$ in the exclusion procedure of SEI if, for any $X \in \boldsymbol{M}_{1}$, there is some $Z \in \boldsymbol{N}_{X}$ such that $T \Perp X|\boldsymbol{M} \cup\{Z\}$ holds. See Sect. 4.2 for details. In fact, in the case of modifying $\boldsymbol{M}_{2}$, there must be $\kappa(\geqslant 2)$ variables in $\boldsymbol{M}_{1}$ (without

Table 8 Frequencies of swamping and masking for LCMB and WLCMB when applied to the ALARM network


loss of generality, denote them by $X_{1}, \ldots, X_{\kappa}$ ) such that

$$
T \Perp X_{1} \mid \boldsymbol{M} \cup\left\{X_{2}\right\}, \quad \ldots, \quad T \Perp X_{\kappa-1} \mid \boldsymbol{M} \cup\left\{X_{\kappa}\right\}, \quad T \Perp X_{\kappa} \mid \boldsymbol{M} \cup\left\{X_{1}\right\}
$$

hold simultaneously. If $\kappa=\left|\boldsymbol{M}_{1}\right|$, then $\boldsymbol{M}_{2}$ is empty before it is modified, so the search will be stopped; however, $T \nmid X \mid \boldsymbol{M}$ holds for any $X \in \boldsymbol{M}_{1}$, meaning $\boldsymbol{M}$ needs more variables to shield $T$. In this case, we modify $\boldsymbol{M}_{2}$ as $\{Y\}$ with $Y=\arg \max _{X \in \boldsymbol{M}_{1}} f_{\boldsymbol{D}}(T ; X \mid \boldsymbol{M})$. This modification integrates the idea of IAMB such that LRH continues to search.

Here, we consider an alternative modification for $\boldsymbol{M}_{2}$ theoretically. Note that the CI statements given in (7) combined with $T \nmid X_{i} \mid \boldsymbol{M}(i=1, \ldots, \kappa)$ are similar to the definition for information equivalence (Lemeire et al. 2012). Now, we show $\mathbb{I}\left(T ; \boldsymbol{M} \cup\left\{X_{1}\right\}\right)=\ldots=$ $\mathbb{I}\left(T ; \boldsymbol{M} \cup\left\{X_{\kappa}\right\}\right)$, or equivalently,

$$
\mathbb{I}\left(T ; X_{1} \mid \boldsymbol{M}\right)=\cdots=\mathbb{I}\left(T ; X_{\kappa} \mid \boldsymbol{M}\right)
$$

In fact, by (7) and the chain rule for CMI, we have

$$
\begin{aligned}
\varrho \triangleq & \mathbb{I}\left(T ; X_{2} \mid \boldsymbol{M} \cup\left\{X_{1}\right\}\right)+\cdots+\mathbb{I}\left(T ; X_{\kappa} \mid \boldsymbol{M} \cup\left\{X_{\kappa-1}\right\}\right)+\mathbb{I}\left(T ; X_{1} \mid \boldsymbol{M} \cup\left\{X_{\kappa}\right\}\right) \\
= & {\left[\mathbb{I}\left(T ; X_{2} \mid \boldsymbol{M}\right)+\mathbb{I}\left(T ; X_{1} \mid \boldsymbol{M} \cup\left\{X_{2}\right\}\right)-\mathbb{I}\left(T ; X_{1} \mid \boldsymbol{M}\right)\right]+\cdots } \\
& +\left[\mathbb{I}\left(T ; X_{\kappa} \mid \boldsymbol{M}\right)+\mathbb{I}\left(T ; X_{\kappa-1} \mid \boldsymbol{M} \cup\left\{X_{\kappa}\right\}\right)-\mathbb{I}\left(T ; X_{\kappa-1} \mid \boldsymbol{M}\right)\right] \\
& +\left[\mathbb{I}\left(T ; X_{1} \mid \boldsymbol{M}\right)+\mathbb{I}\left(T ; X_{\kappa} \mid \boldsymbol{M} \cup\left\{X_{1}\right\}\right)-\mathbb{I}\left(T ; X_{\kappa} \mid \boldsymbol{M}\right)\right] \\
= & \mathbb{I}\left(T ; X_{2} \mid \boldsymbol{M}\right)-\mathbb{I}\left(T ; X_{1} \mid \boldsymbol{M}\right)+\cdots+\mathbb{I}\left(T ; X_{\kappa} \mid \boldsymbol{M}\right)-\mathbb{I}\left(T ; X_{\kappa-1} \mid \boldsymbol{M}\right)+\mathbb{I}\left(T ; X_{1} \mid \boldsymbol{M}\right) \\
& -\mathbb{I}\left(T ; X_{\kappa} \mid \boldsymbol{M}\right) \\
\equiv & 0
\end{aligned}
$$

Combined with the nonnegativity of CMI, we obtain

$$
\mathbb{I}\left(T ; X_{2} \mid \boldsymbol{M} \cup\left\{X_{1}\right\}\right)=\cdots=\mathbb{I}\left(T ; X_{\kappa} \mid \boldsymbol{M} \cup\left\{X_{\kappa-1}\right\}\right)=\mathbb{I}\left(T ; X_{1} \mid \boldsymbol{M} \cup\left\{X_{\kappa}\right\}\right)=0
$$

It follows from (7), (9) that

$$
\begin{aligned}
\mathbb{I}\left(T ;\left\{X_{1}, X_{2}\right\} \mid \boldsymbol{M}\right) & =\mathbb{I}\left(T ; X_{1} \mid \boldsymbol{M}\right)+\mathbb{I}\left(T ; X_{2} \mid \boldsymbol{M} \cup\left\{X_{1}\right\}\right)=\mathbb{I}\left(T ; X_{1} \mid \boldsymbol{M}\right) \\
& =\mathbb{I}\left(T ; X_{2} \mid \boldsymbol{M}\right)+\mathbb{I}\left(T ; X_{1} \mid \boldsymbol{M} \cup\left\{X_{2}\right\}\right)=\mathbb{I}\left(T ; X_{2} \mid \boldsymbol{M}\right)
\end{aligned}
$$

This means $\mathbb{I}\left(T ; X_{1} \mid \boldsymbol{M}\right)=\mathbb{I}\left(T ; X_{2} \mid \boldsymbol{M}\right)$. Similarly, we can show (8) holds for $\kappa \geqslant 2$.
In the sense of (8), we call $X_{1}, \ldots, X_{\kappa}$ to be multiple information equivalent with respect to $T$ given $\boldsymbol{M}$ if $T \nmid X_{i} \mid \boldsymbol{M}(i=1, \ldots, \kappa)$ and the CI statements contained in (7) hold. As seen, in the case of $\kappa=2$, the notion of multiple information equivalence reduces that of information equivalence proposed by Lemeire et al. (2012). Note that multiple information equivalence may exist in $\boldsymbol{M}_{1}$ even when $\boldsymbol{M}_{2}$ needs no modifications.

If multiple information equivalence exists, an alternative operation is to randomly take one variable from every such case to constitute a new $\boldsymbol{M}_{2}$, and other procedures of SEI remain unchanged. This idea may improve on the original SEI and thus LRH. Considering that this operation needs an extra computational complexity and that the occasions of multiple information equivalence are rare in practice, we discuss it no further.

# Appendix 1: Definition of WMB 

This appendix explains why we define WMB using Definition 3. For the definition of MB, it is easily verified that the following two statements are equivalent: (a) $\boldsymbol{M}$ is an Mb of $T$ and none of its proper subsets is an Mb of $T$; and (b) $\boldsymbol{M}$ is an Mb of $T$ and $T \not \subset \boldsymbol{N} \mid \boldsymbol{M} \backslash \boldsymbol{N}$ holds for any nonempty $\boldsymbol{N} \subseteq \boldsymbol{M}$. However, replacing "Mb" with "WMb" in (a)(b), the resulting statements, say ( $\mathrm{a}^{\prime}$ ) and ( $\mathrm{b}^{\prime}$ ), are no longer equivalent: ( $\mathrm{a}^{\prime}$ ) implies ( $\mathrm{b}^{\prime}$ ) but not vice versa. Here is a counterexample.

Example 3 Consider a target variable $T$ which has five potential features $X, Y, Z_{0}, Z_{1}$, and $Z_{2}$. Assume $Z_{0}$ carries all of (1) the unique information about $T$ carried by $X$, all of (2) the unique information about $T$ carried by $Y$, all of (3) the redundant information about $T$ shared by $X$ and $Y$, and some (but not all) of (4) the synergistic information about $T$ carried jointly by $X$ and $Y$; each of $Z_{1}$ and $Z_{2}$ carries some of (1), some of (2), some of (3), but neither $Z_{1}$ nor $Z_{2}$ contains (4); $Z_{1}$ and $Z_{2}$ jointly carry some (but not all) of (4), which is different from that $Z_{0}$ carries. Then, we have

$$
\begin{aligned}
& T \Perp X \mid Z_{0}, \quad T \Perp Y \mid Z_{0}, \quad T \Perp X \mid\left\{Z_{0}, Z_{1}, Z_{2}\right\}, \quad T \Perp Y \mid\left\{Z_{0}, Z_{1}, Z_{2}\right\}, \\
& T \Perp Z_{1} \mid Z_{0}, \quad T \Perp Z_{2} \mid Z_{0}, \quad T \not \subset\left\{Z_{1}, Z_{2}\right\} \mid Z_{0} \Rightarrow\left\{\begin{array}{l}
T \not \subset Z_{1} \mid\left\{Z_{0}, Z_{2}\right\} \\
T \not \subset Z_{2} \mid\left\{Z_{0}, Z_{1}\right\}
\end{array}\right. \\
& T \not \subset Z_{0} \mid\left\{Z_{1}, Z_{2}\right\} \Rightarrow\left\{\begin{array}{l}
T \not \subset\left\{Z_{0}, Z_{1}\right\} \mid Z_{2} \\
T \not \subset\left\{Z_{0}, Z_{2}\right\} \mid Z_{1}
\end{array}\right.
\end{aligned}
$$

It follows that:

- $\boldsymbol{M}_{1} \triangleq\left\{Z_{0}\right\}$ is a WMb of $T$; none of its proper subsets is a WMb of $T$ (i.e., $\varnothing$ is not a WMb of $T$ ); and $T \not \subset \boldsymbol{N} \mid \boldsymbol{M}_{1} \backslash \boldsymbol{N}$ holds for any nonempty $\boldsymbol{N} \subseteq \boldsymbol{M}_{1}$.
- $\boldsymbol{M}_{2} \triangleq\left\{Z_{0}, Z_{1}, Z_{2}\right\}$ is a WMb of $T ; T \not \subset \boldsymbol{N} \mid \boldsymbol{M}_{2} \backslash \boldsymbol{N}$ holds for any nonempty $\boldsymbol{N} \subseteq \boldsymbol{M}_{2}$; but its proper subset $\boldsymbol{M}_{1}$ is also a WMb of $T$, and none of the proper subsets of $\boldsymbol{M}_{1}$ is a WMb of $T$.
- $\mathbb{I}\left(T ; \boldsymbol{M}_{1}\right)<\mathbb{I}\left(T ; \boldsymbol{M}_{2}\right)$.

On the one hand, the implication, $\left(a^{\prime}\right) \Rightarrow\left(b^{\prime}\right)$, means a "WMB" defined by $\left(a^{\prime}\right)$ is minimal in the sense of ( $\left.b^{\prime}\right)$; on the other hand, Example 3 means a WMB, $\boldsymbol{M}$, defined by ( $\left.b^{\prime}\right)$ may have a proper subset satisfying ( $\mathrm{a}^{\prime}$ ) and this proper subset contains less information about $T$ than $\boldsymbol{M}$. In other words, a WMB defined by ( $\mathrm{b}^{\prime}$ ) can carry more information about $T$ than a "WMB" defined by ( $\mathrm{a}^{\prime}$ ). Recall that an MB is in the sense that (1) it is a refined Mb and it contains no any redundant variable, and (2) no information is lost when refining it. This motivates us to define the notion of WMB in a similar fashion: if $\boldsymbol{M}$ is a WMb and its subset, $\boldsymbol{N}$, is a WMB, then $\boldsymbol{N}$ should contain no redundant variables and should have the same mutual information with $T$ as $\boldsymbol{M}$. By the proof of Theorem 2, we get $\mathbb{I}(T ; \boldsymbol{M} \backslash \boldsymbol{N} \mid \boldsymbol{N})=0$, if using ( $\left.b^{\prime}\right)$ (and thus Definition 3) to define $\boldsymbol{N}$. This indicates

$$
\mathbb{I}(T ; \boldsymbol{M})=\mathbb{I}(T ; \boldsymbol{N})+\mathbb{I}(T ; \boldsymbol{M} \backslash \boldsymbol{N} \mid \boldsymbol{N})=\mathbb{I}(T ; \boldsymbol{N})
$$

so no information is lost. In comparison, Example 3 illustrates that $\boldsymbol{N}$ may lose some information if it is defined by ( $\mathrm{a}^{\prime}$ ). This explains why we define the notion of WMB using Definition 3 based on ( $\mathrm{b}^{\prime}$ ) instead of a definition based on ( $\mathrm{a}^{\prime}$ ).

# Appendix 2: Acronyms 

AUC the area under ROC curve.
BN Bayesian network.
BW the backward function for the shrinking phase of LCMB algorithms.
CI conditional independence.
CMb candidate Markov blanket; see, e.g., Line 5 in the grwoing phase of IAMB in Algorithm 1.
CMI conditional mutual information.
DAG directed acyclic graph.
FW the forward function for the growing phase of LCMB algorithms.
GLL generalized local learning: an algorithmic framework for local causal discovery and feature selection (Aliferis et al. 2010a).
GS grow-shrink algorithm (Margaritis and Thrun 1999, 2000).
HITON an MB discovery algorithm, pronounced hee-tón, from the Greek X $\tau \tau \omega \omega^{\prime}$, for "cover", "cloak", or "blanket" (Aliferis et al. 2003).
IAMB incremental association Markov boundary algorithm (Tsamardinos et al. 2003a). See Algorithm 1 for details.
InterPostBW an interleaved version of PostBW. Algorithm 2 describes its pseudo code.
ImpWMB a sub-routine of WLCMB. See Algorithm 3 for details.
KIAMB a stochastic variant of IAMB (Peña et al. 2007); Algorithm 1 gives its pseudo codes.
KS Koller-Sahami algorithm (Koller and Sahami 1996).
LCMB an algorithmic framework containing those MB algorithms that are correct under local composition or Markov local composition (Definition 4).
LRH our proposed algorithm, which is used to deal with the problem of (P1). See Algorithm 1 for details. This algorithm can lessen swamping, resist masking, and highlight the true positives.
Mb Markov blanket:we call $\boldsymbol{M}$ an Mb of $\boldsymbol{T}$ if $\boldsymbol{T} \Perp \boldsymbol{V} \backslash \boldsymbol{M} \backslash \boldsymbol{T} \mid \boldsymbol{M}$ (Definition 1).
MB Markov boundary: an MB of $\boldsymbol{T}$ is any Mb such that none of its proper subsets is an Mb of $\boldsymbol{T}$ (Definition 1).
PCMB parents and children based Markov boundary algorithm (Peña et al. 2007).
PostBW a post-processing techiniue used to improve BW. See Algorithm 2 for details
RT running time: the single CPU time implemented on an Intel i7-3612QM 2.1 GHz and Windows 7 with 64 bits.

RE relative efficiency: defined by (3).
SEI the key sub-routine of LRH: selection-exclusion-inclusion.
WLCMB our LCMB-based algorithmic framework, which is used to deal with the problem of (P2). Algorithm 3 describes the pseudo code. Each WLCMB algorithm is correct under the weak Markov local composition assumption.
WIAMB an instantiation of WLCMB, with A taking $\langle$ IAMB $\rangle$.
WKIAMB an instantiation of WLCMB, with A taking $\langle$ KIAMB, $K\rangle$.
WLRH an instantiation of WLCMB, with A taking $\langle\operatorname{LRH}, k\rangle$.
WMb weak Markov blanket: we call $\boldsymbol{M}$ a WMb of $T$ if $\boldsymbol{T} \Perp \boldsymbol{X} \mid \boldsymbol{M}$ holds for any $X \in \boldsymbol{V} \backslash \boldsymbol{M} \backslash\{T\}$ (Definition 3).
WMB weak Markov boundary: a WMB of $T$ is any WMb such that $\boldsymbol{T} \neq \boldsymbol{N}|\boldsymbol{M}| \boldsymbol{N}$ holds for any nonempty $\boldsymbol{N} \subseteq \boldsymbol{M}$; see Definition 3 and "Appendix 1" for details.
