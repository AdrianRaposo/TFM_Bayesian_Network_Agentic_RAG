# Article 

## A Better Mechanistic Understanding of Big Data through an Order Search Using Causal Bayesian Networks

Changwon Yoo ${ }^{1, *}$, Efrain Gonzalez ${ }^{2}$ (D), Zhenghua Gong ${ }^{1}$ (D) and Deodutta Roy ${ }^{3}$ (D)

## check for updates

Citation: Yoo, C.; Gonzalez, E.; Gong, Z.; Roy, D. A Better Mechanistic Understanding of Big Data through an Order Search Using Causal Bayesian Networks. Big Data Cogn. Comput. 2022, 6, 56. https:// doi.org/10.3390/bdcc6020056

Academic Editor: Carson K. Leung
Received: 8 April 2022
Accepted: 10 May 2022
Published: 17 May 2022
Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (0)

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Department of Biostatistics, Florida International University, Miami, FL 33199, USA; zgong@fiu.edu
2 Department of Mathematics \& Statistics, University of South Florida, Tampa, FL 33620, USA; ehgonzalez@usf.edu
3 Department of Environmental Health Sciences, Florida International University, Miami, FL 33199, USA; droy@fiu.edu

* Correspondence: cyoo@fiu.edu

Abstract: Every year, biomedical data is increasing at an alarming rate and is being collected from many different sources, such as hospitals (clinical Big Data), laboratories (genomic and proteomic Big Data), and the internet (online Big Data). This article presents and evaluates a practical causal discovery algorithm that uses modern statistical, machine learning, and informatics approaches that have been used in the learning of causal relationships from biomedical Big Data, which in turn integrates clinical, omics (genomic and proteomic), and environmental aspects. The learning of causal relationships from data using graphical models does not address the hidden (unknown or not measured) mechanisms that are inherent to most measurements and analyses. Also, many algorithms lack a practical usage since they do not incorporate current mechanistic knowledge. This paper proposes a practical causal discovery algorithm using causal Bayesian networks to gain a better understanding of the underlying mechanistic process that generated the data. The algorithm utilizes model averaging techniques such as searching through a relative order (e.g., if gene $A$ is regulating gene $B$, then we can say that gene $A$ is of a higher order than gene $B$ ) and incorporates relevant prior mechanistic knowledge to guide the Markov chain Monte Carlo search through the order. The algorithm was evaluated by testing its performance on datasets generated from the ALARM causal Bayesian network. Out of the 37 variables in the ALARM causal Bayesian network, two sets of nine were chosen and the observations for those variables were provided to the algorithm. The performance of the algorithm was evaluated by comparing its prediction with the generating causal mechanism. The 28 variables that were not in use are referred to as hidden variables and they allowed for the evaluation of the algorithm's ability to predict hidden confounded causal relationships. The algorithm's predicted performance was also compared with other causal discovery algorithms. The results show that incorporating order information provides a better mechanistic understanding even when hidden confounded causes are present. The prior mechanistic knowledge incorporated in the Markov chain Monte Carlo search led to the better discovery of causal relationships when hidden variables were involved in generating the simulated data.

Keywords: mechanistic understanding; Bayesian analysis; machine learning; statistical data analysis; big data; systems biology

## 1. Introduction

The size of biomedical data, as well as the rate at which it is being produced, is increasing dramatically. The biomedical data is also being collected from many different sources, such as hospitals (clinical Big Data), laboratories (genomic and proteomic Big Data), and the internet (online Big Data). There is a growing need for statistically predictive causal discovery algorithms that incorporate the biological knowledge gained from modern statistical, machine learning, and informatics approaches used in the learning of

causal relationships from biomedical Big Data comprised of clinical, omics (genomic and proteomic), and environmental components.

While earlier available studies focus on statistical methods to infer causality [1-4], recent statistical machine learning methods have been introduced which aim at analyzing big datasets [5-18]. However, given many different types of clinical, genomic, and environmental data, it is rather uncommon to see statistical machine learning methods that utilize prior knowledge relevant to the mechanisms behind the phenomena which generates those different data types. The statistical machine learning methods that recognize that there are many variables which are not collected in the data, but are still related to the mechanisms which produced the data (hidden variables), are also limited. Furthermore, there is a lack of statistical methods that evaluate how well the methods perform at inferring causality when hidden confounded variables are present.

There are many aspects of causality, from its representation (syntax) to its semantics and many different related concepts to causality, e.g., theory of inferred causation, counterfactual analyses, incomplete interventions, confounding effect, etc. [1,9]. However, in learning mechanisms from a phenomenon with collected data, the goal is to infer cause and effect relationships among complicated knitted random variables in the dataset with reasonable confidence.

Thus, the focus in this study is on the learning of causal relationships among random variables in the collected data, particularly when using causal Bayesian networks (CBNs). CBNs are directed acyclic graphs in which each arc is interpreted as a direct causal influence between a parent node and a child node relative to the other nodes in the network [19]. CBNs consist of a structure (such as an example in Figure 1) and a set of probabilities that parameterize said structure (not shown). In general, for each variable there is a conditional probability of that variable given the states of its direct causes. Thus, the probability associated with Gliomas Grade is $P$ (Gliomas Grade $\mid$ PTNP1, LPL, EGFR). That is, we provide the probability distribution over the values of the Gliomas Grade conditioned on each of the possible expression levels of the genes PTNP1, LPL, and EGFR. For variables that have no direct causes in the network, a prior probability is specified. The causal Markov condition [9] specifies the conditional independence relationships which are represented by a causal network: Let $X$ and $Y$ be variables. Suppose that $Y$ is neither a direct nor an indirect effect of $X$. Then $X$ is independent of $Y$, conditioned on any state of the direct causes of $X$. The causal Markov condition permits the joint distribution of the $n$ variables in a CBN to be factored as follows [19]:

$$
P\left(x_{1}, x_{2}, \ldots, x_{n} \mid K\right)=\prod_{i=1}^{n} P\left(x_{i} \mid \pi_{i}, K\right)
$$

where $x_{i}$ denotes a state of variable $X_{i}, \pi_{i}$ denotes a joint state of the parents of $X_{i}$, and $K$ denotes background knowledge (prior probability). Since the initial research for a general Bayesian formulation for learning causal structure (including latent variables) and parameters from observational data using CBN [20,21], Bayesian causal discovery has become an active field of research in which numerous advances have been made [1,7,8,10,22,23].

CBNs have been suitable in analyzing Big Data sets consisting of different types of large data including clinical, genomic, and environmental data [8,12,23-29]. Such causal statistical models help to provide a more comprehensive understanding of human physiology and disease. More importantly, CBNs have been used as a natural way to express "causal" knowledge as a graph using nodes (representing random variables) and arcs (representing "causal" relationships). Indeed, there are many causal models made from existing causal knowledge-from simple and intuitive causal models (e.g., a model to predict whether neighbor is out [30], a sprinkler model [1], etc.), to expert causal models (e.g., a multiple diseases model [31], an ALARM monitoring system [32], etc.). The learning of causal relationships from data has been discussed in different articles [1,9,33], and this especially holds true for cases where researchers have used Bayesian Networks for learning structures [29,34-37]. Also, other algorithms, such as PC [9], K2 [5], and more recently

the Bayesian Inference for Directed Acyclic Graphs (BiDAG) [12], have been used to learn causal relationships from data.
![img-0.jpeg](img-0.jpeg)

Figure 1. A causal Bayesian networks example.
Earlier structure learning methods concentrated on model selection, where we select a model $M^{*}$ from

$$
M^{*}=\arg \max _{i} P\left(D \mid M_{i}\right)
$$

or

$$
M^{*}=\arg \max _{i} P\left(M_{i} \mid D\right)
$$

where we assume we have $p$ number of mutually exclusive models, $M_{1}, M_{2}, \ldots, M_{p}$ [38]. Later methods incorporated model averaging [29], where we summarize how likely a feature $F$ that is found in a subset of the models and is defined by a set of indices, $f \subseteq\{1,2, \ldots, p\}$ where $f$ includes those indices of the models where $F$ is observed. Thus, in model averaging, we calculate the probability of a feature $F$ as the following:

$$
\sum_{f} P\left(D \mid M_{f}\right)
$$

or

$$
\sum_{f} P P\left(M_{f} \mid D\right)
$$

However, most of the structure learning methods do not address hidden variables. Since we cannot observe all relevant variables in a natural phenomenon, to better learn the underlying mechanistic process from Big Data, we need to address and evaluate the learning of causal relationships with hidden variables.

In this paper, we show that searching through the order (we describe further about what we mean by "order" in the method section) of variables in CBNs can help provide a better understanding of the underlying mechanistic process that generated the data even in the presence of hidden variables. In addition, we propose a novel algorithm in searching through the order (we call it the PrePrior algorithm) which evidences a promising performance when attempting to learn the underlying mechanistic process from data containing hidden variables. The algorithm utilizes model averaging techniques such as searching through a relative order (e.g., if gene $A$ is regulating gene $B$, then we can say that gene $A$ is in a higher order than gene $B$ ) and incorporates relevant prior mechanistic knowledge to guide the Markov chain Monte Carlo (MCMC) search through the order.

# 2. Methods 

Given a CBN structure $S$ and a dataset $D$, the Bayesian scoring method that assesses how well the structure fits the given data can be calculated using a closed form [39]:

$$
P(D \mid S)=\prod_{i=1}^{n} \prod_{j=1}^{q_{i}} \frac{\Gamma\left(N^{\prime}{ }_{i j}\right)}{\Gamma\left(N^{\prime}{ }_{i j}+N_{i j}\right)} \prod_{k=1}^{c} \frac{\Gamma\left(N^{\prime}{ }_{i j k}+N_{i j k}\right)}{\Gamma\left(N^{\prime}{ }_{i j k}\right)}
$$

In the above scoring method, Dirichlet uniform parameter priors are used and parameter independence is assumed [40]; $n$ represents the number of variables in the structure; $q_{i}$ represents the number of configurations of the parents for a given variable $X i$; and $r_{i}$ represents the total amount of states for a variable $X i$. For example, if $X i$ is a binary random variable and it has two binary random variables as direct causes (parents), then $r_{i}$ is equivalent to two and $q_{i}$ is equivalent to four. $N_{i j k}$ represents the counts for a given variable $X i$ under a given parent configuration (indexed by $j$ ) and a given state (indexed by $k$ ) for variable $X i . N^{\prime}{ }_{i j k}$ represents the Dirichlet uniform prior, which in this case may be calculated as the following:

$$
N_{i j k}^{\prime}=\frac{1}{r_{i} q_{i}}
$$

The number of possible structures increases exponentially with the number of variables, and so the above formula is sufficient for determining the best BN when the number of variables in the CBN is small. However, when the number of variables is large, it becomes impossible to determine the best structure in this manner. The problem of finding the best CBN is NP-hard [41], and thus it is not always possible to find the best CBN that fits the data. This is the key limitation of model selection methods [38] when used as a means of extending our current mechanistic understanding through the learning of causal relationships from data.

The algorithm we introduce in this paper utilizes model averaging techniques, such as searching through a relative order [29] (e.g., cause is in a higher order than effect) and incorporating prior mechanistic knowledge to guide the MCMC (Markov Chain Monte Carlo) search through the order. An order describes the relationships between variables based on describing whether a variable can be a direct cause (parent) for another variable.

Definition 1. (Order $\succ): X_{i} \succ X_{j}$ iff $X_{j} \notin P a_{X i}$.
With the above definition of the order, we are stating that $X_{i}$ is considered to be of a higher order than $X_{j}$ if, and only if, $X_{j}$ cannot be found in the group of direct causes (parents) of $X_{i}$. A potential ordering for a list of three variables is $<X_{1}, X_{2}, X_{3}>$. This order implies that $X_{1}$ can be a direct cause (parent) of $X_{2}$ and/or $X_{3}$, but $X_{2}$ and $X_{3}$ cannot be direct causes (parents) of $X_{1}$. Similarly, $X_{2}$ can be a direct cause (parent) of $X_{3}$, but $X_{3}$ cannot be a direct cause (parent) of $X_{2}$. Note that any given order of random variables can better summarize mechanistic (causal) relationships than just one structure. For example, an order $\left\langle X_{1}, X_{2}, X_{3}\right\rangle$ includes the following three structures (Figure 2):
![img-1.jpeg](img-1.jpeg)

Figure 2. Three structures included in the order $<X_{1}, X_{2}, X_{3}>$.
Orders are useful because, in a manner similar to structures, they can be scored. Since an order represents a set of structures, it may be scored by summing over all structures consistent with the given order. This method for scoring an order is not efficient because it would require that we have a score for all structures that meet a given order. With that being the case, we consider an alternative method for scoring orders presented by Friedman and Koller [29], which uses the direct cause (parent) sets of variables. The equation for this scoring procedure is:

$$
P(D \mid O)=\prod_{i=1}^{n} \sum_{U \in U_{i,}} \prod_{j=1}^{d_{i, U}} \frac{\Gamma\left(N^{\prime}{ }_{i j}\right)}{\Gamma\left(N^{\prime}{ }_{i j}+N_{i j}\right)} \prod_{k=1}^{r_{i}} \frac{\Gamma\left(N^{\prime}{ }_{i j k}+N_{i j k}\right)}{\Gamma\left(N^{\prime}{ }_{i j k}\right)}
$$

The above equation is an expansion of Bayesian scoring presented by Heckerman [33]. Here, $O$ represents an ordering, $U_{i, o}$ represents the possible parent-sets for a given variable

under a given ordering, and $q_{i, \mathrm{U}}$ represents the possible configurations of the parents for a variable $i$ within a parent-set $U$. All other parameters in the equation are represented in the same manner as in Equation (6).

The benefit in scoring orders over scoring structures is that in the case where one is dealing with two or more variables, there are more structures than orders. For example, when the number of variables equals four, there are 543 structures but only 24 different orders.

An MCMC search is used to search through the orders. At any given MCMC search process, we have a current order (denote it as $o$ ) and a proposed order (denote it as $o^{\prime}$ ), and we decide whether the proposed order will take the place of the current order with a probability that is returned by a decision function $f\left(o, o^{\prime}\right)$. A proposed order is generated by either applying a local perturbation (i.e., swapping two variables in an order: for example, $\left\langle X_{1}, X_{2} \ldots X_{i} \ldots X_{j} \ldots X_{n}\right\rangle$ to $\left\langle X_{1}, X_{2} \ldots X_{i} \ldots X_{i} \ldots X_{n}\right\rangle$ ), or a global perturbation (i.e., aka a cutting the deck, swapping groups of variables in an order: for example, $<X_{1}, X_{2} \ldots$ $\left.X_{i}, X_{i+1} \ldots X_{n}>\right.$ to $\left.<X_{i+1} \ldots X_{n}, X_{1}, X_{2} \ldots X_{i}>\right)$. Initially, a random order is generated.

Friedman and Koller [29] propose the following two algorithms for MCMC search with different $f\left(o, o^{\prime}\right)$ :

- Random Algorithm

$$
\text { - } \quad \operatorname{Uses} f\left(o, o^{\prime}\right)=\min \left[1, \frac{P\left(D \mid o^{\prime}\right)}{P(D \mid o)}\right]
$$

- Prior Algorithm

$$
\text { - } \quad \operatorname{Uses} f\left(o, o^{\prime}\right)=\min \left[1, \frac{P\left(D \mid o^{\prime}\right) P\left(o^{\prime} \mid o\right)}{P(D \mid o) P\left(o \mid o^{\prime}\right)}\right]
$$

where $o, o^{\prime}$, and $D$ represent the current order that we are considering: a proposed order and a dataset, respectively.

We further propose a new algorithm called the PrePrior Algorithm with the following MCMC search with the same $f\left(o, o^{\prime}\right)$ as the Prior algorithm with an additional step:

- PrePrior Algorithm

- $\quad$ Uses $P\left(o^{\prime} \mid o\right)$ based on user defined prior to sample $o^{\prime}$
- $\quad$ Uses $f\left(o, o^{\prime}\right)=\min \left[1, \frac{P\left(D \mid o^{\prime}\right) P\left(o^{\prime} \mid o\right)}{P(D \mid o) P\left(o \mid o^{\prime}\right)}\right]$

Note that PrePrior algorithm generates proposed orders based on the prior, $P(o)$ and $P\left(o^{\prime}\right)$ that the user provides.

User's Prior of an Order. To specify a prior of mechanistic causal knowledge in terms of an order o (if $X$ is known to cause $Y$, we say $X$ has a higher order than $Y$, i.e., $X \succ Y$ ) or $P(o)$, we assume the following:
i. If no prior is provided, a uniform prior of any given order is assumed. For example, for a pairwise order of $X$ and $Y$, if no prior is provided then $P(X \prec Y)=P(Y \prec X)=0.5$. In general, for $n$ variables a uniform prior for any order $o$ is $P(o)=\frac{1}{n!}$.
ii. The prior of an order is specified as the probability of how likely it is compared to the uniform prior. For example, if prior publications show gene $Y$ is regulating gene $X$, a user might specify $P(X \prec Y)=0.9$ and if there have been studies suggesting that gene $Z$ is regulating gene $W$, a user might specify $P(W \prec Z)=0.6$.
For mechanism discovery, the correct discovery of the generating structure is the most important aspect of the algorithm. Datasets consisting of 50 and 1000 simulated observational cases from the ALARM Bayesian network were generated [27]. To see how well the algorithm correctly discovered the generating structure in the presence of hidden variables, we have selected two sets of nine variables each selected from 37 variables in the network. The first variable set is referred to as Close 9 variables (C9) and was created by selecting variables that were closely situated in the network (Figure 3a, all the grayed-out variables are hidden and not selected). The second variable set is referred to as Sparse 9 variables (S9) and was created by selecting variables that were relatively situated further in the network (Figure 3b, all the grayed-out variables are hidden and not selected).

![img-2.jpeg](img-2.jpeg)

Figure 3. Two sets of nine variables. All the grayed-out variables are hidden and not selected. (a) Close 9 variables (C9). (b) Sparse 9 variables (S9).

Another reason we have selected these nine variables was to see how well the causal discovery algorithms were predicting the four pairwise relationships shown in Figure 4. Distinguishing these four pairwise relationships is the first step in better understanding the mechanistic process involved in generating these datasets.

Different numbers of pairwise causal relationships are found in the Close 9 variables (C9) and Sparse 9 variables (S9) (Table 1). For example, in C9, TPR and VentLung are not confounded nor causally related (denoted as $\varnothing_{X Y}$ in Figure 4a), and TPR and HR are not confounded and causally related (denoted as $\varnothing_{X \rightarrow Y}$ in Figure 4b). In S9, ExpCO2 and Catechol are confounded but not causally related (denoted as $\mathrm{H}_{\mathrm{X}}$ in Figure 4c, ArtCO2 being a variable as H ), and ArtCO2 and VentAlv are confounded and causally related (denoted as $\mathrm{H}_{\mathrm{X} \rightarrow \mathrm{Y}}$ in Figure 4d where VentLung takes the role of H ).

![img-3.jpeg](img-3.jpeg)

Figure 4. Four pairwise causal relationships. H represents a variable that is shaded, meaning that it is present in the ALARM network but not introduced in the datasets using C9 and S9. Not confounded and not causally related is denoted as $\varnothing_{X Y}$ in (a). Not confounded and causally related is denoted as $\varnothing_{X \rightarrow Y}$ in (b). Confounded and not causally related is denoted as $\mathrm{H}_{X Y}$ in (c). Confounded and causally related is denoted as $\mathrm{H}_{X \rightarrow Y}$ in (d).

Table 1. Number of pairwise causal relationships in Close 9 variables (C9) and Sparse 9 variables (S9). H represents a variable that is shaded. (a) Close 9 variables (C9). (b) Sparse 9 variables (S9).


Two datasets were generated from each of the two sets of variables. Two of the datasets had 50 observational cases each and were named D50C9 and D50S9 because they were generated by the C9 and S9 sets of variables, respectively. The other two datasets had 1000 observational cases each and were named D1KC9 and D1KS9 because they were generated by the C9 and S9 sets of variables, respectively. Many biological mechanistic networks are not completely connected, i.e., each variable has limited (e.g., less than five) causes. As a result, we have limited the number of possible parents to five and scored all the possible orders using Equation (8). It took roughly one month to score all of the possible orders for the four datasets. The dataset of results is referred to as Dataset Global BDe Best Order. Dataset Global BDe Best Order contains information on all of the scores for all of the possible orders, and therefore we know which is the best order (and the best Bayesian networks structure) that will be identified if the BDe metric [5] (similar to Equation (8)) is used given the dataset.

The Random, Prior, and PrePrior algorithms were independently ran three times on D50C9 and D50S9 for $1 \mathrm{~h}, 2 \mathrm{~h}$, and 4 h ; and on D1KC9 and D1KS9 for $2 \mathrm{~h}, 4 \mathrm{~h}$, and 16 h . We have used five Linux machines to run in parallel of 522 total h (over 21 equivalent days) of runs.

The predictive performance is calculated as a pairwise causal distance from either generating the structure (denoted it as $S_{G}$ and shown in Figure 5) or the Dataset Global BDe Order. For each variable pair of $X$ and $Y$, let the underlying relationship between $X$ and $Y$ be denoted as $R_{X, Y}$ where $R_{X, Y} \in\{X \rightarrow Y, X \leftarrow Y, X($ none $) Y\}$. Let the likelihood score of $R_{X, Y}$ assessed from either the generating structure and Dataset Global BDe Order as $P_{G}\left(R_{X, Y}\right)$ and $P_{G}\left(D \mid R_{X, Y}\right)$ respectively, where $D \in\{$ D50C9, D50S9, D1KC9, D1KS9 $\}$. Note that we calculate.

$$
P_{G}\left(R_{X, Y}\right)=\left\{\begin{array}{l}
1 \text { if } R_{X, Y} \in S_{G} \\
0 \text { if } R_{X, Y} \notin S_{G}
\end{array}\right.
$$

and

$$
\begin{gathered}
P_{G}\left(D \mid R_{X, Y}\right)=\sum_{o \in O} \sum_{S_{o}} \delta_{S_{o}} P\left(D \mid S_{o}\right) P(D \mid o) \\
\delta_{S_{o}}=\left\{\begin{array}{l}
1 \text { if } R_{X, Y} \in S_{o} \\
0 \text { if } R_{X, Y} \notin S_{o}
\end{array}\right.
\end{gathered}
$$

where $O$ is the set of orders that satisfy $\frac{\sum_{O} P(D \mid O)}{\sum_{\Phi_{O}} P\left(D \mid \Phi_{O}\right)}>0.99$ and $S_{o}$ is the set of structures that satisfy an order $o \in O$ and $\frac{\sum_{S_{o}} P\left(D \mid S_{o}\right)}{\sum_{\Phi_{S_{o}}} P\left(D \mid \Phi_{S_{o}}\right)}>0.99$ for all possible orders (denote them as $\Phi_{O}$ ) and all possible structures that satisfies an order $o \in O$ (denote them as $\Phi_{S_{o}}$ ).
![img-4.jpeg](img-4.jpeg)

Figure 5. Generating Structures for Sparse 9 (a) and Close 9 (b) variables.
Additionally, we calculate $P^{S}{ }_{G}\left(D \mid R_{X, Y}\right)$.

$$
\begin{gathered}
P^{S}{ }_{G}\left(D \mid R_{X, Y}\right)=\sum_{S} \delta_{S} P(D \mid S) \\
\delta_{S}=\left\{\begin{array}{l}
1 \text { if } R_{X, Y} \in S \\
0 \text { if } R_{X, Y} \notin S
\end{array}\right.
\end{gathered}
$$

$S$ is the set of structures that satisfies $\frac{\sum_{S} P(D \mid S)}{\sum_{\Phi_{S}} P\left(D \mid \Phi_{S}\right)}>0.99$ for all possible structures (denote them as $\Phi_{S}$ ) from all possible orders.

We use $P^{S}{ }_{G}\left(D \mid R_{X, Y}\right)$ and $P_{G}\left(D \mid R_{X, Y}\right)$ for all $X$ and $Y$ to generate a consensus causal structure by drawing arcs between $X$ and $Y$ with the thickest arc when $P^{S}{ }_{G}\left(D \mid R_{X, Y}\right)$ or $P_{G}\left(D \mid R_{X, Y}\right)$ are above 0.9999 , and with the thinnest arc when $P^{S}{ }_{G}\left(D \mid R_{X, Y}\right)$ or $P_{G}\left(D \mid R_{X, Y}\right)$ are close to 0.0001 . If $P^{S}{ }_{G}(D \mid X \rightarrow Y)$ and $P^{S}{ }_{G}(D \mid Y \rightarrow X)$ both are less than 0.0001 , then no arcs are drawn between $X$ and $Y$.

We first compare generating causal structure and Dataset Global BDe Best Order by calculating the following:

$$
\begin{aligned}
& \sum_{R_{X, Y}}\left(P_{G}\left(R_{X, Y}\right)-P_{G}\left(D \mid R_{X, Y}\right)\right) \\
& \sum_{R_{X, Y}}\left(P_{G}\left(R_{X, Y}\right)-P^{S}{ }_{G}\left(D \mid R_{X, Y}\right)\right)
\end{aligned}
$$

These results will show us how the BDe metric approximates the generated causal structure given the generated datasets. In addition to comparing the predictive ability of these algorithms, we compared the causal structure predictive ability of the algorithms that use BDe metric with the Dataset Global BDe Best Order.

We report each Dataset Global BDe Best Order prediction using a Markov blanket of a variable (Catechol) appearing both from Close 9 variables (C9) and Sparse 9 variables (S9) and compared that with the Markov blanket of the Catechol from the generating structure.

Denote the probability of $R_{\mathrm{X}, \mathrm{Y}}$ predicted from an algorithm as $P_{A}\left(D \mid R_{\mathrm{X}, \mathrm{Y}}\right)$ and $P^{\mathrm{S}}{ }_{A}\left(D \mid R_{X, Y}\right)$. Note that $\mathrm{P}_{\mathrm{A}}\left(D \mid R_{\mathrm{X}, \mathrm{Y}}\right)$ is calculated the same way we calculated $P_{G}\left(D \mid R_{\mathrm{X}, \mathrm{Y}}\right)$ described above. We report the distance from the generating structure as

$$
\begin{aligned}
& \sum_{R_{X, Y}}\left(P_{G}\left(R_{X, Y}\right)-P_{A}\left(D \mid R_{X, Y}\right)\right) \\
& \sum_{R_{X, Y}}\left(P_{G}\left(R_{X, Y}\right)-P^{S}{ }_{A}\left(D \mid R_{X, Y}\right)\right)
\end{aligned}
$$

and the distance from the Dataset Global BDe Order as

$$
\begin{gathered}
\sum_{R_{X, Y}}\left(P_{G}\left(D \mid R_{X, Y}\right)-P_{A}\left(D \mid R_{X, Y}\right)\right) \\
\sum_{R_{X, Y}}\left(P^{S}{ }_{G}\left(D \mid R_{X, Y}\right)-P^{S}{ }_{A}\left(D \mid R_{X, Y}\right)\right)
\end{gathered}
$$

Note here we consider indirect causation to assess $R_{\mathrm{X}, \mathrm{Y}}$, i.e., we check whether $X$ appears as an ancestor of $Y$ (i.e., repeatedly applying parent-of $(Y)$ function-parent-of(parentof $(Y)$ ), parent-of(parent-of(parent-of $(Y))$ ) ... ), or whether $Y$ appears as an ancestor of $X$ in the overall network.

We report how well algorithms predict the Markov blanket of each variable in Close 9 variables (C9) and Sparse 9 variables (S9) (denote all Markov Blankets as $A_{\mathrm{M}}$ ) and compare with the Markov blanket of the variable from the Dataset Global BDe Best Order (denote all Markov Blankets as $G_{\mathrm{M}}$ ) by calculating the following distance:

$$
\begin{aligned}
& \sum_{g_{M} \in G_{M}} \sum_{a_{M} \in A_{M}} d\left(g_{M}, a_{M}\right) \\
& d\left(g_{M}, a_{M}\right)= \begin{cases}\left|P_{G}\left(D \mid g_{M}\right)-P_{A}\left(D \mid a_{M}\right)\right| & \text { if } g_{M} \equiv a_{M} \\
P_{G}\left(D \mid g_{M}\right) & \text { if } g_{M} \notin A_{M} \\
P_{A}\left(D \mid a_{M}\right) & \text { if } a_{M} \notin G_{M} \\
0 & \text { othewise }\end{cases} \\
& \sum_{g_{M} \in G_{M}} \sum_{a_{M} \in A_{M}} d^{S}\left(g_{M}, a_{M}\right) \\
& d^{S}\left(g_{M}, a_{M}\right)= \begin{cases}\left|P^{S}{ }_{G}\left(D \mid g_{M}\right)-P^{S}{ }_{A}\left(D \mid a_{M}\right)\right| & \text { if } g_{M} \equiv a_{M} \\
P^{S}{ }_{G}\left(D \mid g_{M}\right) & \text { if } g_{M} \notin A_{M} \\
P^{S}{ }_{A}\left(D \mid a_{M}\right) & \text { if } a_{M} \notin G_{M} \\
0 & \text { othewise }\end{cases}
\end{aligned}
$$

Note that $P_{G}\left(D \mid g_{M}\right)$ and $P_{A}\left(D \mid a_{M}\right)$ can be calculated by incorporating the order weight (as we calculated $P_{G}\left(D \mid R_{X, Y}\right)$ or $P_{A}\left(D \mid R_{X, Y}\right)$ by multiplying $P(D \mid O)$ ) and $P^{S}{ }_{G}\left(D \mid g_{M}\right)$ and $P^{S}{ }_{A}\left(D \mid a_{M}\right)$ can be calculated by not incorporating the order weight (as we calculated $P^{S}{ }_{G}\left(D \mid R_{X, Y}\right)$ or $P^{S}{ }_{A}\left(D \mid R_{X, Y}\right)$ by not multiplying $P(D \mid O)$ ).

We also report all algorithms' predicted performance, as how well they predict four causal pairwise relationships- $\varnothing_{\mathrm{X} \mathrm{Y}}, \varnothing_{\mathrm{X} \rightarrow \mathrm{Y}}, \mathrm{H}_{\mathrm{X} \mathrm{Y}}$, and $\mathrm{H}_{\mathrm{X} \rightarrow \mathrm{Y}}$-introduced in Table 1 by comparing the algorithm's prediction of $R_{\mathrm{X}, \mathrm{Y}} \in\{X \rightarrow Y, X \leftarrow Y, X($ none $) Y\}$ with the true underlying relationships $T_{\mathrm{X}, \mathrm{Y}} \in\left\{\varnothing_{\mathrm{X} \mathrm{Y}}, \varnothing_{\mathrm{X} \rightarrow \mathrm{Y}}, \mathrm{H}_{\mathrm{X} \mathrm{Y}}, \mathrm{H}_{\mathrm{X} \rightarrow \mathrm{Y}}\right\}$. In addition to the predictive performance, we also report the following for each $R_{\mathrm{X}, \mathrm{Y}}$ and for each $T_{\mathrm{X}, \mathrm{Y}}$ :

$$
\begin{aligned}
P_{A}\left(R_{X, Y} \mid T_{X, Y}\right) & =\frac{\sum_{X, Y} \delta_{T_{X, Y}} P_{A}\left(D \mid R_{X, Y}\right)}{\sum_{X, Y} \delta_{T_{X, Y}}} \\
P^{S}{ }_{A}\left(R_{X, Y} \mid T_{X, Y}\right) & =\frac{\sum_{X, Y} \delta_{T_{X, Y}} P^{S}{ }_{A}\left(D \mid R_{X, Y}\right)}{\sum_{X, Y} \delta_{T_{X, Y}}}
\end{aligned}
$$

$$
\delta_{T_{X, Y}}=\left\{\begin{array}{l}
1 \text { if true relationship is } T_{X, Y} \\
0 \text { if true relationship is not } T_{X, Y}
\end{array}\right.
$$

where $\sum_{X, Y} \delta_{T_{X, Y}}$ is the number of underlying true relationships (i.e., counts in Table 1). Finally, we report the percentage of the algorithm's most probable prediction of $R_{X, Y}$ given the true underlying true relationships $T_{X, Y}$ by calculating the following:

$$
\begin{gathered}
C_{A}\left(R_{X, Y} \mid T_{X, Y}\right)=\frac{\sum_{X, Y} \delta_{R_{X, Y}, T_{X, Y}}}{\sum_{X, Y} \delta_{T_{X, Y}}} \\
\delta_{R_{X, Y}, T_{X, Y}}=\left\{\begin{array}{lr}
1 & \text { if true relationship is } T_{X, Y} \text { and } R_{X, Y} \equiv \operatorname{argmax}_{r_{X, Y}} P_{A}\left(D \mid r_{X, Y}\right) \\
0 & \text { otherwise }
\end{array}\right. \\
C^{S}{ }_{A}\left(R_{X, Y} \mid T_{X, Y}\right)=\frac{\sum_{X, Y} \delta_{R_{X, Y}, T_{X, Y}}^{\prime}}{\sum_{X, Y} \delta_{T_{X, Y}}} \\
\delta_{R_{X, Y}, T_{X, Y}}^{\prime}=\left\{\begin{array}{lr}
1 & \text { if true relationship is } T_{X, Y} \text { and } R_{X, Y} \equiv \operatorname{argmax}_{r_{X, Y}} P^{S}{ }_{A}\left(D \mid r_{X, Y}\right) \\
0 & \text { otherwise }
\end{array}\right. \\
\delta_{T_{X, Y}}=\left\{\begin{array}{lr}
1 & \text { if true relationship is } T_{X, Y} \\
0 & \text { if true relationship is not } T_{X, Y}
\end{array}\right.
\end{gathered}
$$

We have also run other causal discovery algorithms, such as PC [9], K2 [5], and BiDAG [12] on the same datasets, i.e., 50 and 1000 cases for Sparse 9 variables (in D50S9 and D1KS9); and 50 and 1000 cases for Close 9 variables (in D50C9 and D1KC9). Since BiDAG could only incorporate binary random variables for learning, we converted all the variables in the datasets as continuous variables. This was done by adding normal noise with $\mu=0, \delta=0.01$ to each measurement of discrete data. The reason we have used these parameters for noise was that they have given the most consistent conditional independencies among the variables when we compared the original discrete data and converted continuous data.

# 3. Results 

Figure 6 reports the highest scored structure reported by BDe scores for each dataset. It is interesting to note that even with a large number of samples and a significantly more likely Global BDe Structure, i.e., for 1000 cases (D1KS9) and its BDe percentage structure score of $>99 \%$, it predicts incorrect mechanisms, e.g., HRBP is predicted as a cause of CO and CO is predicted as a cause of LVFailure (Figure 6c). However, the generating structure shows that HRBP is not a cause of CO (they are confounded by Catechol), and LVFailure is a cause of CO (Figure 5a). Another interesting result to notice is that even with many cases (i.e., 1000 cases), the highest BDe scored structure may obtain a mere $4 \%$ of the total BDe structure score.

Figure 7 shows consensus structures using $P^{S}{ }_{G}\left(D \mid R_{X, Y}\right)$ (without incorporating the order weight) for D50S9, D50C9, D1KS9, and D1KC9. The arcs thicknesses are based on $P^{S}{ }_{G}(D \mid X \rightarrow Y)$ or $P^{S}{ }_{G}(D \mid Y \rightarrow X)$. If $P^{S}{ }_{G}(D \mid X \rightarrow Y)$ is displayed as a percentage, then $P^{S}{ }_{G}(D \mid Y \rightarrow X)$ is also displayed as a percentage in the parentheses. If $P^{S}{ }_{G}(D \mid X \rightarrow Y)$ and $P^{S}{ }_{G}(D \mid Y \rightarrow X)$ both are less than 0.0001 , then no arcs are drawn between $X$ and $Y .>99$ or $\sim 0$ indicates where the pairwise causal relationship probability is greater than 0.9999 or less than 0.0001 , respectively. Similarly, Figure 8 shows consensus structures using $P_{G}\left(D \mid R_{X, Y}\right)$ (with incorporating the order weight) for D50S9, D50C9, D1KS9, and D1KC9.

![img-5.jpeg](img-5.jpeg)

Figure 6. The highest scored Global BDe Structure for (a) D50S9 (14.23\%), (b) D50C9 (15.71\%), (c) D1KS9 ( $>99 \%$ ) and (d) D1KC9 (4.03\%). BDe percentage score in the parentheses.

The Global BDe structure using D50S9 was marginally better (maximum likelihood of 0.1423 ) than other structures. All of the models incorrectly identified causal effects from LVFailure to VentAlv; from Catechol to ExpCO2; and from HRBP to CO when compared to the generating structure (Figure 5a). In D50S9, the consensus structures generated with the order weight (Figure 8a) and without the order weight (Figure 7a) were different than the Global BDe structure (Figure 6a). A significant difference between the consensus structures generated with the order weight (Figure 8a), and without the order weight (Figure 7a), was a causal relationship between Catechol to ExpCO2. The consensus structure generated with the order weight predicted $\mathrm{P}_{\mathrm{G}}(D \mid \operatorname{ExpCO2} \rightarrow$ Catechol $)=0.4803$ as the most probable relationship; however, the consensus structure generated without the order weight predicted $\mathrm{P}_{\mathrm{G}}(D \mid$ Catechol $\rightarrow \operatorname{ExpCO2})=0.4409$ as the most probable relationship, as the generating structure (Figure 3a) showed that Catechol and ExpCO2 had no direct causal influence between each other. It is also noteworthy that one of their common causes, VentAlv, was correctly predicted to be a common cause in both consensus structures. This showed that, to some extent, we can use the disagreement between the consensus structures generated with and without the order weight to identify confounded relationships without any direct causal relationship.

![img-6.jpeg](img-6.jpeg)

Figure 7. Consensus structure without the order weight for (a) D50S9, (b) D50C9, (c) D1KS9, and (d) D1KC9. Thicknesses of the arcs are based on the pairwise causal relationship probability that is presented as a label in percentage (the reverse causal relationship probability is presented in the parentheses). >99 and ~0 represent pairwise causal relationship probability greater than 0.9999 and less than 0.0001, respectively.

![img-7.jpeg](img-7.jpeg)

**Figure 8.** Consensus structure with the order weight for (a) D50S9, (b) D50C9, (c) D16S9, and (d) D16C9. Thicknesses of the arcs are based on the pairwise causal relationship probability that is presented as a label in percentage (the reverse causal relationship probability is presented in the parentheses). >99 and ~0 represent pairwise causal relationship probability greater than 0.9999 and less than 0.0001 respectively.

The Global BDe structure using D50C9 was marginally better (maximum likelihood of 0.1571) than other structures. In D50C9, the consensus structures generated with the order weight (Figure 8b) or without the order weight (Figure 7b) were slightly different than the Global BDe structure (Figure 6b). All models incorrectly identified causal effects.

from Anaphylaxis to ArtCO2; from InsuffAnesth to ArtCO2; and predicted a reversed causal direction of ArtCO2 and ExpCO2 compared to the generating structure (Figure 5b). Compared to the same 50 cases, D50S9, no significant differences were observed between the consensus structures generated with the order weight (Figure 8b) and without the order weight (Figure 7b).

Only in D1KS9, both consensus structures generated with (Figure 8c) or without the order weight (Figure 7c) agreed with the Global BDe structure (Figure 6c). This is not surprising because the Global BDe structure was significantly better ( $>0.9999$ ) than any other structures. However, all models incorrectly predicted the following three causal relationships: between CO and LVFailure (reversed causal prediction); between Intubation and ExpCO2 (missing causal prediction); and added between Catechol and BP (unnecessary causal prediction) compared to the generating structure (Figure 5a).

The Global BDe structure using D1KC9 was marginally better (maximum likelihood of 0.0403 ). Among the four datasets, it resulted in the lowest maximum likelihood, making D1KC9 the most difficult dataset to learn causal relationships from. All models incorrectly identified a causal effect from ArtCO2 to SaO2 (Figure 5b). In D1KC9, the consensus structures generated with the order weight (Figure 8d) and without the order weight (Figure 7d) were different than the Global BDe structure (Figure 6d). A significant difference between the consensus structures generated with the order weight (Figure 8d) and without the order weight (Figure 7d) was the prediction of a causal relationship between VentLung and ArtCO2. The consensus structure generated with the order weight predicted $\mathrm{P}_{\mathrm{G}}(D \mid$ ArtCO2 $\rightarrow$ VentLung $)=0.5556$ as being the most probable relationship; however, the consensus structure generated without the order weight predicted $\mathrm{P}_{\mathrm{G}}(D \mid$ VentLung $\rightarrow$ ArtCO2 $)=$ 0.6154 as being the most probable relationship. As the generating structure (Figure 3b) shows VentLung and ArtCO2 have a direct causal influence between each other and their common cause, Intubation is hidden in the dataset. This shows how difficult it is to learn reliable causal relationships among the upstream variables in which most of the confounded causes are hidden in the dataset.

We believe all these results are due to the omission of 28 variables and random sampling effects. Also, as the later results will show, with 50 cases, it is more difficult to learn the generating structure of C9, and with 1000 cases it is more difficult to learn the generating structure of S9.

Table 2 shows all the orders (from the total of $9!=362,880$ orders) that received a combined percentage score of $>99 \%$. Interestingly, the means were all $7.1429 \%$. However, depending on the dataset, the standard deviation of the scores were different. The data sampled from S9 tended to show tighter percentage scores among the orders than the data sampled from C9. This means that order scores from S9 had less impact than those from C9.

Table 2. Mean and Standard Deviation (S.D.) of the Dataset Global BDe Best Order percentage score.


Table 3 summarizes our claim that incorporating the ordering results can help us gain mechanistic knowledge. According to the distances, the BDe score had difficulties in learning the true underlying mechanisms from the generating structure with 50 cases of C9. However, by adding more samples, i.e., with 1000 cases of C9, we improved the ability to learn the true underlying mechanisms from the generating structure.

Table 3. Structure distances between the generating causal structure and the Dataset Global BDe Best Order.


Overall, the results shown in Table 3 illustrate that order weight improves in learning the true underlying mechanisms from the generating structure. In the 1000 cases of S9 (D1KS9), as it was mentioned earlier (shown in Figure 6c), there was only one structure that was significant in terms of BDe score (i.e., $>99 \%$ of the total BDe structure score). Because of this fact, all orders that were compliant with the dominating structure had a very similar score with a very tight margin, resulting in almost all the same order score (Table 2). Therefore, in this situation we can see why the order score will not improve in learning the true underlying mechanisms from the generating structure.

Tables 4 and 5 compare the structure distances between (1) the algorithm's predicted structures and the generated structures (Generated $\delta$ ), and (2) the algorithm's predicted structures and the best BDe structure scores (Global BDe $\delta$ ). In some sense, Generated $\delta$ measures how well the algorithm learns the underlying mechanism from a phenomenon, and Global BDe $\delta$ measures how well the algorithm estimates the best BDe (or BGe) score from the sample.

Table 4. Structure distances without the order weight. (a) 50 cases datasets. Dark shaded cells represent the lowest distance or variance in each timed run for the dataset; Bright shaded cells represent the second lowest distance or variance in each timed run for the dataset. (b) 1000 cases datasets. Dark shaded cells represent the lowest distance or variance in each timed run for the dataset; Bright shaded cells represent the second lowest distance or variance in each timed run for the dataset.
(a)


Table 4. Cont.


P: Prior, PP: PrePrior, SC: Strong Correct, WC: Weak Correct, SI: Strong Incorrect, WI: Weak Incorrect.

Table 5. Structure distances with the order weight. (a) 50 cases datasets. Dark shaded cells represent the lowest distance or variance in each timed run for the dataset; Bright shaded cells represent the second lowest distance or variance in each timed run for the dataset. (b) 1000 cases datasets. Dark shaded cells represent the lowest distance or variance in each timed run for the dataset; Bright shaded cells represent the second lowest distance or variance in each timed run for the dataset.


(b)


Table 5. Cont.


P: Prior, PP: PrePrior, SC: Strong Correct, WC: Weak Correct, SI: Strong Incorrect, WI: Weak Incorrect.
In 50 cases spanning Tables 4 a and 5 a, it is clear that all the MCMC ordering algorithms (Random, Prior, and PrePrior) outperformed constrained variant algorithms (BiDAG, K2, and PC) in terms of Generated $\delta$ and Global BDe $\delta$ with datasets D50S9 and D50C9. Also, in general, algorithms with the order weight predicted better in generating structures (i.e., lower Generated $\delta$ and Global BDe $\delta$,) with a higher confidence (i.e., lower variance.)

With the maximum hours ( 4 h ) run, Random and PrePrior converged on their predictions; however, Prior showed some variance in performance. We note that with a lesser number of hours ( 1 and 2 h ), PrePrior showed better performances (better predictions with confidence, i.e., less variance) than Random in D50S9 and comparable predictions in D50C9 (in 1 h run, Random Generated $\delta$ was 22.31 with variance of 0.302 , and PrePrior Weak Correct achieved Generated $\delta 22.65$ with a very low variance, 0.001 (Table 4a)).

The structure distances of 1000 cases are shown in Tables 4 b and 5 b . K2 showed the best Generated $\delta$ and Global BDe $\delta$ in D1KS9; however, its performance was the lowest among all the algorithms in D1KC9. We believe this was because, in D1KS9, as it was mentioned earlier (shown in Figure 6c), there was only one structure that was significant in terms of its BDe score ( $>99 \%$ of the total BDe structure scores).

The BiDAG performance in Global BDe $\delta$ in D1KS9 was the second best (next to K2's); however, Generated $\delta$ in D1KS9 was either comparable or worse than the MCMC ordering algorithms (Random, Prior, and PrePrior). It seems MCMC ordering algorithms need more than 16 h to converge, although structure distances were generally decreasing in D1KC9, however, that trend is questionable in D1KS9.

We could not find a general pattern as we saw in 50 cases that better predicted the generating structures (lower Generated $\delta$ and Global BDe $\delta$ ) with a higher confidence, i.e., a lower variance with order weight in 1000 cases. We believe this fact has to do with the results that we mentioned earlier, i.e., that MCMC ordering algorithms needs more than 16 h to converge.

With the outstanding performance of K2 in D1KS9 reported earlier, however, we must also mention the outstanding performance of the Prior algorithm with the Strong Correct

prior, which achieved a better performance that was statistically significant in a mere 2 h run in D1KC9. In D1KC9, all algorithms showed larger than ten for Generated $\delta$, except for Prior. Prior achieved lower than ten for Generated $\delta$ with a high confidence (variance of 8.136; significantly lower than the second lowest variance of 18.0 from BiDAG).

Tables 6 and 7 compare the Markov blanket distances between the algorithm's predicted Markov blanket of each variable in the structures (for short, we refer it to MB) and MB in the generated structure (Generated $\delta$ ), as well as the distance of the algorithm's predicted MB and the MB of the best BDe structure scores (Global BDe $\delta$ ).

Table 6. Markov blanket distances without the order weight. (a) 50 cases datasets. Dark shaded cells represent the lowest distance or variance in each timed run for the dataset; Bright shaded cells represent the second lowest distance or variance in each timed run for the dataset; Bright shaded cells represent the second lowest distance or variance in each timed run for the dataset.


Table 6. Cont.


P: Prior, PP: PrePrior, SC: Strong Correct, WC: Weak Correct, SI: Strong Incorrect, WI: Weak Incorrect. Table 7. Markov blanket distances with the order weight. (a) 50 cases datasets. Dark shaded cells represent the lowest distance or variance in each timed run for the dataset; Bright shaded cells represent the second lowest distance or variance in each timed run for the dataset; (b) 1000 cases datasets. Dark shaded cells represent the lowest distance or variance in each timed run for the dataset; Bright shaded cells represent the second lowest distance or variance in each timed run for the dataset.


Table 7. Cont.


(b)


P: Prior, PP: PrePrior, SC: Strong Correct, WC: Weak Correct, SI: Strong Incorrect, WI: Weak Incorrect.

In 50 cases from Tables 6a and 7a, it is clear that all the MCMC ordering algorithms (Random, Prior, and PrePrior) outperformed the constrained variant algorithms (BiDAG, K2, and PC) in Generated $\delta$ and Global BDe $\delta$ with datasets D50S9. In dataset D50C9, BiDAG was slightly better ( 16.0 vs. 16.19) in Generated $\delta$; however, it was significantly worse in Global BDe $\delta$. Also, in general, Generated $\delta$ and Global BDe $\delta$ of the algorithms with the order weight did not change much because the MB distances were low to begin with (Generated $\delta$ ranged from 16.00 to 16.53 , and with the order weight it ranged from 16.00 to 16.50 ; Global BDe $\delta$ ranged from 0.00 to 8.93 , and with the order weight it ranged from 0.00 to 5.03). We note that with the order weight, the 1 h runs in D50C9 showed lower Global BDe $\delta$ with a higher confidence, i.e., a lower variance.

With the maximum hour ( 4 h ) run, Random and PrePrior predictions converged; however, Prior showed some variance in its performance. We note that with a smaller number of hours ( 1 and 2 h ) runs, PrePrior showed better performances (better predictions with higher confidence (i.e., lower variance) than Random in D50S9, and comparable performances in D50C9 (in 1 h run, Random Generated $\delta$ was 16.17 with variance of 0.0 , PrePrior Weak Correct achieved Generated $\delta 16.16$ with a very low variance, 0.0 (Table 6a).

MB distances of 1000 cases are shown in Tables 6b and 7b. In D1KS9, PrePrior with Strong and Weak Prior achieved the best Generated $\delta(16.00)$ with a variance of 12.0. K2 showed the best Global BDe $\delta(0.0)$ in D1KS9. Also, in general, Generated $\delta$ and Global BDe $\delta$ of the algorithms with the order weight did not change much because the MB distances were low to begin with (Generated $\delta$ ranged from 7.99 to 18.0 , and with the order weight it ranged from 7.81 to 18.0; Global BDe $\delta$ ranged from 4.66 (excluding 0.0 from K2) to 13.83 (excluding 18.0 from BiDAG), and with the order weight it ranged from 4.80 (excluding 0.0 from K2) to 13.75 (excluding 18.0 from BiDAG)).

In D1KC9, most of the MCMC ordering algorithms (Random, Prior, and PrePrior) outperformed the constrained variant algorithms (BiDAG, K2, and PC) in Generated $\delta$ and Global BDe $\delta$. In 2 h runs, Prior with Weak Correct prior achieved the best Generated $\delta$ (7.99; the runner-up was PrePrior Weak Correct prior with 9.15) and Global BDe $\delta$ (5.82; the runner-up was PrePrior Weak Correct prior with 8.16); however, the most confident prediction came from PrePrior Weak Correct prior in Generated $\delta$ (0.912; the runner-up was Prior Weak Correct prior with 0.938).

Also, in D1KC9 with 4 h runs, PrePrior with Strong Correct prior achieved the best Generated $\delta$ (10.27; the runner-up was Random with 10.31) and Random achieved the best Global BDe $\delta$ (8.07; the runner-up was PrePrior Strong Correct prior with 9.97). In 16 h runs, Random achieved the best Generated $\delta$ (8.38; the runner-up was PrePrior Weak Correct prior with 9.43) and Global BDe $\delta$ (4.66; the runner-up was PrePrior Strong Correct prior with 7.26).

Tables 8 and 9 show algorithm's predicted probabilities of four causal pairwise relationships shown in Figure 4. In all four datasets, all the MCMC ordering algorithms (Random, Prior, and PrePrior) outperformed the constrained variant algorithms (BiDAG, and K2) in the confounded relationships $\mathrm{H}_{\mathrm{X}}$ ( no causal relationship) or $\mathrm{H}_{\mathrm{X} \rightarrow \mathrm{Y}}$ (causal relationship). K2 and BiDAG incorrectly predicted (with probability of 0.0 ) the true underlying confounded relationships: for example, with 1000 cases, using D1KS9, BiDAG predicted all the three true $\mathrm{H}_{\mathrm{X} \rightarrow \mathrm{Y}}$ relationships with a probability of 0.0 , and using D1KC9, BiDAG, and K2 predicted all of the four true $\mathrm{H}_{\mathrm{X}}$ Y relationships with probability of 0.0 . Typically, algorithms with the order weight tended to perform better in correctly predicting true causally independent relationships ( $\varnothing_{\mathrm{X}}$ and $\mathrm{H}_{\mathrm{X}}$ ) and performed worse in correctly predicting true causal predictions ( $\varnothing_{\mathrm{X} \rightarrow \mathrm{Y}}$ and $\mathrm{H}_{\mathrm{X} \rightarrow \mathrm{Y}}$ ).

Tables 10 and 11 show the algorithm's most probable prediction rates of four causal pairwise relationships shown in Figure 4. As it was noticed earlier in Tables 8 and 9, in all four datasets, all the MCMC ordering algorithms (Random, Prior, and PrePrior) outperformed the constrained variant algorithms (BiDAG, and K2) in confounded relationships $\mathrm{H}_{\mathrm{X}}$ ( no causal relationship) or $\mathrm{H}_{\mathrm{X} \rightarrow \mathrm{Y}}$ (causal relationship). Algorithms with the order weight changed most the probable prediction rates of the confounded and causally in-

dependent predictions $\left(\mathrm{H}_{\mathrm{X}} \mathrm{Y}\right)$ of MCMC ordering algorithms except PrePrior with Weak Correct prior in D50S9 (one relationship prediction of $\mathrm{Y} \rightarrow \mathrm{X}$ was changed to $\mathrm{X} \rightarrow \mathrm{Y}$ ). Another change by weighing order was noticed in D1KC9. There, algorithms with the order weight changed most the probable prediction rates of the confounded and causally independent predictions $\left(\mathrm{H}_{\mathrm{X}} \mathrm{Y}\right)$, and the confounded causal predictions $\left(\mathrm{H}_{\mathrm{X} \rightarrow \mathrm{Y}}\right)$ of PrePrior with Weak Correct prior. For $\mathrm{H}_{\mathrm{X} \mathrm{Y}}$, five relationships prediction of $\mathrm{X} \rightarrow \mathrm{Y}$ were correctly changed to the true underlying relationship, X Y ; and for $\mathrm{H}_{\mathrm{X} \rightarrow \mathrm{Y}}$, one relationship prediction of $\mathrm{Y} \rightarrow \mathrm{X}$ was correctly changed to the true underlying relationship, $\mathrm{X} \rightarrow \mathrm{Y}$.

Table 8. Algorithms' predicted probabilities of four causal pairwise relationships without the order weight. (a) Dataset for Sparse 9 variable with 50 cases (D50S9). Dark shaded cells represent the best prediction of the correct causal relationship; Bright shaded cells represent the second best prediction of the correct causal relationship. (b) Dataset for Close 9 variable with 50 cases (D50C9). Dark shaded cells represent the best prediction of the correct causal relationship; Bright shaded cells represent the second best prediction of the correct causal relationship. (c) Dataset for Sparse 9 variable with 1000 cases (D1KS9). Dark shaded cells represent the best prediction of the correct causal relationship; Bright shaded cells represent the second best prediction of the correct causal relationship. (d) Dataset for Close 9 variable with 1000 cases (D1KC9). Dark shaded cells represent the best prediction of the correct causal relationship; Bright shaded cells represent the second best prediction of the correct causal relationship.


Table 8. Cont.


Table 8. Cont.


Table 9. Algorithms' predicted probabilities of four causal pairwise relationships with the order weight. (a) Dataset for Sparse 9 variable with 50 cases (D50S9). Dark shaded cells represent the best prediction of the correct causal relationship; Bright shaded cells represent the second best prediction of the correct causal relationship. (b) Dataset for Close 9 variable with 50 cases (D50C9). Dark shaded cells represent the best prediction of the correct causal relationship; Bright shaded cells represent the second best prediction of the correct causal relationship. (c) Dataset for Sparse 9 variable with 1000 cases (D1KS9). Dark shaded cells represent the best prediction of the correct causal relationship; Bright shaded cells represent the second best prediction of the correct causal relationship. (d) Dataset for Close 9 variable with 1000 cases (D1KC9). Dark shaded cells represent the best prediction of the correct causal relationship; Bright shaded cells represent the second best prediction of the correct causal relationship; (e) Dataset for Close 9 variable with 50 cases (D50C9). Dark shaded cells represent the best prediction of the correct causal relationship; Bright shaded cells represent the second best prediction of the correct causal relationship.


**Table 9.** *Cont*.


Table 9. Cont.


Table 10. Algorithms' most probable prediction rates by four causal pairwise relationships without the order weight. (a) Dataset for Sparse 9 variable with 50 cases (D50S9). Dark shaded cells represent the best prediction of the correct causal relationship; Bright shaded cells represent the second best prediction of the correct causal relationship. (b) Dataset for Close 9 variable with 50 cases (D50C9). Dark shaded cells represent the best prediction of the correct causal relationship; Bright shaded cells represent the second best prediction of the correct causal relationship. (c) Dataset for Sparse 9 variable with 1000 cases (D1KS9). Dark shaded cells represent the best prediction of the correct causal relationship; Bright shaded cells represent the second best prediction of the correct causal relationship. (d) Dataset for Close 9 variable with 1000 cases (D1KC9). Dark shaded cells represent the best prediction of the correct causal relationship; Bright shaded cells represent the second best prediction of the correct causal relationship.


Table 10. Cont.


Table 10. Cont.


Table 11. Algorithms' most probable prediction rates by four causal pairwise relationships with the order weight. (a) Dataset for Sparse 9 variable with 50 cases (D50S9). Dark shaded cells represent the best prediction of the correct causal relationship; Bright shaded cells represent the second best prediction of the correct causal relationship. (b) Dataset for Close 9 variable with 50 cases (D50C9). Dark shaded cells represent the best prediction of the correct causal relationship; Bright shaded cells represent the second best prediction of the correct causal relationship. (c) Dataset for Sparse 9 variable with 1000 cases (D1KS9). Dark shaded cells represent the best prediction of the correct causal relationship; Bright shaded cells represent the second best prediction of the correct causal relationship. (d) Dataset for Close 9 variable with 1000 cases (D1KC9). Dark shaded cells represent the best prediction of the correct causal relationship; Bright shaded cells represent the second best prediction of the correct causal relationship.


Table 11. Cont.


Table 11. Cont.


# 4. Discussion and Future Work 

The results from this study show that learning causal relationships from data is difficult, especially because many variables are hidden to us whether we are aware of that or not. Many Big Data analytic methods have been dealing with Big Data characteristics, such as its large volume, its fast growth in size, or its variety of data types. However, as we have shown in this study, it is important to incorporate and develop causal discovery frameworks to discover underlying mechanistic processes from Big Data.

Searching through order of variables in CBN and incorporating likelihood of the order helped us better search through plausible underlying mechanistic processes even when hidden variables were present. Further incorporating the prior of the order in the search process (PrePrior algorithm) showed an increase in performance, especially when there were a limited number of cases available, than other published methods that did not incorporate the prior of the order. We believe combining different types of data, e.g., environmental, genomics, neurological, social media, etc., will further strengthen our capabilities of discovering underlying mechanistic processes from Big Data.

Our study was focused in discovering underlying mechanistic processes using a small number of variables, i.e., $<30$. It was practical to use a small number of variables because we were focused on understanding the effect of hidden variables when learning causal relationships from data. Thus, the results reported here should be interpreted under this premise. As it was pointed out earlier, our study is limited in telling what the effects of the other characteristics of Big Data can contribute to the discovery of underlying mechanistic processes. Moreover, understanding those characteristics effects and combination effects of them will lead us to develop novel methods that will revolutionize the future Big Data analytics.

PrePrior algorithm can be extended in many different directions. As it was shown, with 1000 cases, all MCMC ordering algorithm could not converge in their predictions. This aspect can be overcome by incorporating constraint-based methods in conjunction with the Bayesian MCMC sampling methods using BDe (or BGe) scores. This will enable us to analyze not only larger samples, but also larger number of variables, one of the hall mark characteristics of Big Data. Also, it will extend the causal discovery ability when we model hidden variables explicitly or implicitly into the PrePrior algorithm.

## 5. Conclusions

We have shown searching through order of variables in CBN and incorporating the likelihood of the order helped us better understand the underlying mechanistic process that

generated the data even when hidden variables were introduced in the experimental design. Also, a novel algorithm in searching through the order we proposed (PrePrior algorithm) showed promising performance in better learning the underlying mechanistic process that generated the data, especially confounded causal relationships with a reasonable number of samples $(\approx 50)$.

Author Contributions: Conceptualization, C.Y. and D.R.; methodology, C.Y.; software, E.G. and Z.G.; validation, E.G. and Z.G.; formal analysis, E.G. and Z.G.; investigation, C.Y, E.G. and Z.G.; resources, C.Y.; data curation, E.G. and Z.G.; writing-original draft preparation, C.Y.; writing-review and editing, C.Y., E.G. and D.R.; visualization, Z.G.; supervision, C.Y.; project administration, C.Y.; funding acquisition, C.Y. All authors have read and agreed to the published version of the manuscript.
Funding: C.Y., E.G. and Z.G. were funded by NIH SC3GM096948 grant.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: PrePrior and order searching algorithms were implemented in C++ using SMILE (Structural Modeling, Inference, and Learning Engine, Bayes Fusion LLC) C++ library. The package is available in SMLG (Statistical Machine Learning Group) GitHub at https://github. com/smlgfiuedu/Order-Score. (accessed on 7 April 2022). Also, all data is available in SMLG forum at http://smlg.fiu.edu/phpbb/viewtopic.php?f=87\&t=161. (accessed on 7 April 2022).
Conflicts of Interest: The authors declare no conflict of interest.

# Abbreviations 

The following abbreviations were used in this manuscript:
BiDAG Bayesian Inference for Directed Acyclic Graphs, a CBN search algorithm
BDe Bayesian Dirichlet prior
C9 Nine variables that were connected closely in ALARM Bayesian network
CBN Causal Bayesian Network
D1KC9 1000 observational cases generated from C9
D1KC9 1000 observational cases generated from S9
D50C9 50 observational cases generated from C9
D50S9 50 observational cases generated from S9
K2 A constraint based CBN search algorithm
MCMC Markov Chain Monte Carlo
NP-hard At least hard as nondeterministic polynomial time problem
PC A constraint based CBN search algorithm
PrePrior A new order searching algorithm that uses prior of order to search CBN
S9 Nine variables that were connected sparsely in ALARM Bayesian network
