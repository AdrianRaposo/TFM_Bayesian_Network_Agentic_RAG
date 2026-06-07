# Psychological Methods 

## A Tutorial on Bayesian Networks for Psychopathology Researchers

Giovanni Briganti, Marco Scutari, and Richard J. McNally
Online First Publication, February 3, 2022. http://dx.doi.org/10.1037/met0000479

## CITATION

Briganti, G., Scutari, M., \& McNally, R. J. (2022, February 3). A Tutorial on Bayesian Networks for Psychopathology Researchers. Psychological Methods. Advance online publication. http://dx.doi.org/10.1037/met0000479

# A Tutorial on Bayesian Networks for Psychopathology Researchers 

Giovanni Briganti ${ }^{1,2}$, Marco Scutari ${ }^{3}$, and Richard J. McNally ${ }^{1}$<br>${ }^{1}$ Department of Psychology, Harvard University<br>${ }^{2}$ Laboratoire de Psychologie Médicale et Addictologie, Université libre de Bruxelles<br>${ }^{3}$ Istituto Dalle Molle di Studi sull'Intelligenza Artificiale (IDSIA), Lugano, Switzerland


#### Abstract

Bayesian Networks are probabilistic graphical models that represent conditional independence relationships among variables as a directed acyclic graph (DAG), where edges can be interpreted as causal effects connecting one causal symptom to an effect symptom. These models can help overcome one of the key limitations of partial correlation networks whose edges are undirected. This tutorial aims to introduce Bayesian Networks to identify admissible causal relationships in cross-sectional data, as well as how to estimate these models in R through three algorithm families with an empirical example data set of depressive symptoms. In addition, we discuss common problems and questions related to Bayesian networks. We recommend Bayesian networks be investigated to gain causal insight in psychological data.


## Translational Abstract

In the last decade, the network framework for the study of mental disorders has emerged as a new way of investigating mental disorders as issuing from interactions among their constituent symptoms. Network analysis is the statistical aspect of this framework, as researchers use nodes (symptoms) and edges (connections between symptoms) to model disorders: Usually, network structures encode pairwise interactions among symptoms. In this study, we introduce Bayesian networks, models that can identify admissible causal relationships in cross-sectional data, as well as a tutorial for applied researchers on how to estimate those models in R. In addition, we discuss common problems and questions related to Bayesian network models.

Keywords: Bayesian networks, directed acyclic graphs, network modeling, causal inference, tutorial

The last decade has seen the emergence of a new framework for the study of psychopathology: network theory, which conceptualizes an episode of disorder as issuing from interactions among its constituent symptoms (Borsboom, 2017; Borsboom \& Cramer, 2013). Network theory comes with a set of statistical techniques called network analysis, where the networks that represent interactions among symptoms are composed of nodes (the symptoms themselves) and edges (connections among symptoms). In contrast to social networks, whose nodes

[^0](persons) and edges (e.g., friendships) are observable, psychopathology networks require statistical estimation to discern the unobservable connections between symptoms. Most network structures in the psychopathology field encode pairwise interactions among symptoms (Epskamp \& Fried, 2018), and use a general class of models called pairwise Markov random fields.

Gaussian graphical models (GGMs), also called partial correlation networks, are the most common way of estimating network structures in many areas of psychopathology, such as posttraumatic stress disorder (Fried et al., 2018; McNally et al., 2015); depression (Briganti et al., 2021; Fried et al., 2016) and bipolar disorders (Curtiss et al., 2019). Other pairwise Markov random fields include Ising models to estimate pairwise interactions from binary data (Briganti \& Linkowski, 2020; Ising, 1925; Kruis \& Maris, 2016; van Borkulo et al., 2014) and mixed graphical models to deal with mixed data (Haslbeck \& Fried, 2017; Haslbeck \& Waldorp, 2016). However, the causal interpretation of these models is limited: because their edges are undirected, it is impossible to tell whether symptom X is more likely to cause or be caused by symptom Y because edges have no direction and thus cannot encode this information. Furthermore, assuming a partial correlation network when the underlying model contains directed edges can lead to spurious causal connections.

We can overcome these problems with the help of Bayesian networks (BNs), which are derived from the principles of causal


[^0]:    Giovanni Briganti (1) https://orcid.org/0000-0002-4038-3363
    Giovanni Briganti served as lead for the conceptualization, original draft preparation and writing - review and editing. Marco Scutari and Richard J. McNally contributed equally to writing - review and editing.

    The data and the code accompanying this tutorial are available in our repository on the Open Science Framework (https://osf.io/fne9m/), with information related to the package versions used to perform the different analyses.

    We thank Sacha Epskamp and Lourens Waldorp for their very insightful comments that allowed our article to greatly improve during the review process.

    Correspondence concerning this article should be addressed to Giovanni Briganti, Department of Psychology, Harvard University, 1232 William James Hall, 33 Kirkland Street, Cambridge, MA 02138-2044, United States. Email: giovanni.briganti@hotmail.com

reasoning (Pearl, 2009; Pearl \& Mackenzie, 2018). That is, they can ascertain both the direction and the magnitude of causal effects (Maathuis et al., 2018). BNs are defined by a directed acyclic graph (DAG) and by the joint probability distribution of the variables under investigation. The role of the DAG is to express the conditional independence relationships between the variables (nodes) by using graphical separation (Koller \& Friedman, 2009; Lauritzen, 1996; Pearl, 1988; Scutari \& Denis, 2021). In other words, if two variables are separated in the DAG by some other variables, they are independent in probability conditional on (that is, after controlling for) those other variables. Hence, the role of the probability distribution is to express the magnitude of the causal effects linking the variables that are not graphically separated. Because BNs contain only directed edges, they are ideal for modeling the admissible causal relationships in observational data, thereby complementing insights provided by partial correlation networks. BNs should not be confused with pairwise Markov random fields estimated with Bayesian methods: These have been recently introduced in the network psychopathology literature in both methodological and applied research (Briganti et al., 2020; Williams \& Mulder, 2020a, 2020b). Using BNs for rigorous causal inference requires several strong assumptions (Maathuis et al., 2018), such as the existence of a DAG underlying the data; sufficiency, that is, all the causes of a given variable are measured (which means that there are no latent variables and there is no selection bias); and faithfulness, that is, all the variables that are connected in a given way in the network are probabilistically dependent. To augment probabilistic inference with causal meaning the faithfulness and sufficiency assumptions need to be further strengthened into causal faithfulness and causal sufficiency, which will be discussed in more detail (see Structure Learning and Assumption Needed for Structure Learning sections). These assumptions of having an underlying DAG and causal sufficiency are difficult to verify in psychological data: For instance, we do not know whether symptoms from a checklist or psychometric measure or structured diagnostic interview assessing a mental disorder interact as a DAG except in very specific cases, such as the relationship between a traumatic event (the cause) and posttraumatic stress disorder (PTSD) symptoms (McNally et al., 2017). In most cases, such as depression, we do not know whether a given symptom unilaterally influences another (as in a DAG), whether two symptoms mutually influence each other (as in a partial correlation network), or whether there is one or more latent variables causing symptoms (as within the latent variable framework). The faithfulness assumption will likely be violated in a data set where the data generating process is such that $A \rightarrow B, B \rightarrow C, A \rightarrow C$, as the causal relationships are counterbalanced (Andersen, 2013; Cartwright \& McMullin, 1984).

The insights that BNs can bring to the field of network psychopathology can be helpful in various situations, such as performing inference on the network structure based on its estimates. Edge weights are used, for instance, to identify the most central (i.e., interconnected) nodes in a network (Elliott et al., 2019): Summing edge weights (strength centrality) or estimating the shared variance $R^{2}$ (predictability) are the two most common ways of gauging the importance of symptoms (Boccaletti et al.,

2006; Haslbeck \& Fried, 2017). Central symptoms are highly connected, with many connections or several strong ones. If such symptoms are the source of activation that maintains an episode of disorder, then successfully reducing their severity ought to cause a beneficial therapeutic cascade resulting in recovery from illness. Accordingly, they would be ideal therapeutic targets. Unfortunately, because the edges in partial correlation networks are undirected, it is impossible to tell whether a high-centrality symptom is the source of activation or the recipient of activation. Only if it is the source does it make sense to consider it a highpriority target for clinical intervention. Yet because they have often been theorized as potential targets for clinical intervention, centrality estimates are defined to operate on undirected networks and thus do not take edge directions into consideration. In other words, they do not ascertain whether central symptoms cause or are caused by many symptoms in the network; if a symptom is well-connected because it is highly controllable (that is, caused by several symptoms connected to it), acting on it is unlikely to affect other symptoms. Because interpreting network structures is an important part of any network study, complementing the study of interaction among symptoms with further causal insight is essential.

Only a handful of studies have applied BNs in psychopathology research. These studies have included dissociation (Cernis et al., 2021), self-harm (Hinze et al., 2021), paranoia (Bird et al., 2019), psychosis (Kuipers et al., 2019; Moffa et al., 2017), obsessive-compulsive disorder (Jones et al., 2018; McNally et al., 2017), bipolar disorder (McNally et al., 2021), rumination (Bernstein et al., 2017), depression (Briganti et al., 2021), PTSD (McNally et al., 2017), and alexithymia (Briganti et al., 2020). In these studies, BNs illuminated potential causal relations among symptoms in cross-sectional data sets. However, the authors often varied in their computational methods, thereby underscoring the need for an accessible tutorial reference for researchers keen to apply BNs to study mental disorders. The present work aims to fill this gap by introducing BNs, by providing key commands in the R environment for statistical computing (R Core Team, 2020) to estimate BNs from data, and by addressing the main strengths and limitations of BNs in psychopathology.

This tutorial builds on previous empirical studies that applied the two main approaches for estimating BNs: constraint-based algorithms (Briganti et al., 2020, 2021) and score-based (McNally et al., 2017, 2017; Moffa et al., 2017). This tutorial complements these applied works by offering a principled introduction to BNs and on how to interpret them in psychological data.

This article is structured as follows. First, we will introduce BNs and their main theoretical properties. We will then outline both constraint-based and score-based structure learning algorithms as well as their implementation in R, illustrating them with data and code. Finally, we will discuss the interpretation of BNs in observational studies as well as answer common questions researchers may have about BNs. More extended exposition on these topics appear in specialized textbooks (Koller \& Friedman, 2009; Neapolitan, 2004; Pearl, 2009; Scutari \& Denis, 2021) and in an accessible trade book for the general reader (Pearl \& Mackenzie, 2018).

## Bayesian Networks

## Definition

BNs are defined as the combination of a network structure, specifically a DAG, and a probability distribution. The DAG provides a high-level abstraction useful for qualitative reasoning in the context of exploratory analysis and for testing hypotheses about how symptoms relate to one another. The probability distributions of the symptoms quantify those relationships in terms of their magnitude and direction.

## Directed Acyclic Graphs

The network structure of a BN is a mathematical object $\mathcal{G}=$ $(V, A)$ consisting of a set of nodes $V=\left\{v_{1}, v_{2}, \ldots, v_{N}\right\}$ (where N is the number of nodes) and of a set of edges or arcs $A=$ $\left\{\left(v_{1}, v_{2}\right),\left(v_{2}, v_{3}\right), \ldots\right\}$ that represent all connections between two nodes. Given $V$, a graph is uniquely identified by $A$. In the case of a DAG, the edges can only be directed, that is, $\left(v_{i}, v_{j}\right) \neq\left(v_{j}, v_{i}\right), v_{i} \rightarrow v_{j}$, with the assumption that two nodes are only connected by one edge. In each edge $v_{i} \rightarrow v_{j}, v_{i}$ is called the "parent" node and $v_{j}$ is called the "child" node. DAGs are also acyclic: They do not contain any loops, that is, edges from a node to itself $v_{i} \rightarrow v_{i}$; or any cycle, that is, sequences of edges that start and end on the same node, such as $v_{i} \rightarrow v_{j} \rightarrow \ldots \rightarrow v_{k} \rightarrow v_{i}$. The primary role of the DAG in a BN is to express the set of conditional independence of relationships among variables (that is, variables that do not cause each other).

## Markov Blankets

The DAG of a BN is an independence map of the probability distribution of the variables $X_{i}$, which are represented in the networks by the nodes $v_{i}$; retrieving such a map means determining which nodes are conditionally (in)dependent. This is achieved by using $d$-separation, which defines graphical separation for DAGs and provides a way to algorithmically determine whether two nodes in a network are (in)dependent or conditionally (in)dependent (Geiger et al., 1990). Formally, two nodes $v_{i}$ and $v_{j}$ are $d$-separated by a conditioning set of nodes $\mathcal{S}$ if conditioning on all members of $\mathcal{S}$ block all paths (sequence of nodes and edges with $v_{i}$ as starting node and $v_{j}$ as ending node, that do not necessarily follow the direction indicated by edges) between $v_{i}$ and $v_{j}$. A collider does not generate an unconditional association between the variables that determine it (Greenland et al., 1999; Pearl, 1988). In Figure 1, three examples of a basic three-node DAG are illustrated, as well as how they differ in conditional independences.

The set $\mathcal{S}$ that makes a node $v_{i}$ independent of all other nodes in $G$ is known as the Markov blanket of $v_{i}$. By the Markov property, the Markov blanket includes a node's parents, children, and spouses, that is, children's other parents. The Markov blanket is useful in investigating a target node of interest while ignoring the rest of the BN; all nodes outside of the Markov blanket are independent from the node of interest after controlling for those in the Markov blanket itself.

## The Markov Property

If two nodes are not connected by an edge in a BN, then they are either independent or conditionally independent given some other nodes: this is called the local Markov property (Korb \& Nicholson, 2010; Lauritzen, 1996). The global Markov property is a stronger version of the local property and generalizes it to sets of variables: any two subsets of variables are conditionally independent given a separating subset (Föllmer, 1980; Lauritzen, 1996). Graphical separation implies probabilistic independence ${ }^{1}$

$$
v_{i} \Perp_{G} v_{j} \mid v_{k} \Rightarrow v_{i} \Perp_{P} v_{j} \mid v_{k}
$$

(where $\Perp_{G}$ means graphical separation and $\Perp_{P}$ probabilistic independence), making the network itself a clear representation of the conditional independence relationships between nodes. For this reason, the DAG is called an independence map of the variables.

The Markov property makes it possible to write ${ }^{2}$

$$
\operatorname{Pr}(\mathbf{X}, \boldsymbol{\Theta})=\prod_{i=1}^{N} \operatorname{Pr}\left(X_{i} \mid \Pi_{X_{i}} ; \Theta_{X_{i}}\right)
$$

decomposing the larger model $\operatorname{Pr}(\mathbf{X}, \boldsymbol{\Theta})$ into a set of smaller models $\operatorname{Pr}\left(X_{i} \mid \Pi_{X_{i}} ; \Theta_{X_{i}}\right)$, one for each variable $X_{i}$ conditional on its parents $\Pi_{X_{i}}$ in the DAG (Korb \& Nicholson, 2010), $\boldsymbol{\Theta}$ and $\Theta_{X_{i}}$ denote the parameters of the respective models. These smaller models are individually much simpler than $\operatorname{Pr}(\mathbf{X}, \boldsymbol{\Theta})$; and they are topical, in the sense that they focus on a single variable and its relations with variables that surround it in the DAG. This factorization follows from the Markov property of BNs, and it is only possible because of the absence of loops and cycles in the graph. Figure 2 represents a toy example Bayesian Network of four nodes from specific manic symptoms from the Young Mania Rating Scale (Young et al., 1978), and an example of how a probability distribution in a DAG is factorized (Briganti et al., 2021).

Figure 2 also shows a fundamental type of relationship in a BN, represented by the three nodes increased energy, language-thought disorder, and speech disorder. Both increased energy and lan-guage-thought disorder have an edge pointing to speech disorder and they are not adjacent, that is, they do not share an edge with one another. This pattern of edges is commonly known as a vstructure, or a collider, and it is one of the building blocks of BNs. In a collider $(A \rightarrow C \leftarrow B)$, four conditional independences are found: A and C are dependent, B and C are dependent, A and B are independent, and A and B are dependent conditional on C. This means that two independent variables, A and B, can become dependent when one conditions on C, because observing the common consequences of two independent causes can modify their probability (Pearl, 2009). The two causes $(A$ and $B)$ are therefore negatively partially correlated (if they are both positive or both negative), which is counterintuitive; conditioning on the common

[^0]
[^0]:    ${ }^{1}$ If two nodes $v_{i}$ and $v_{j}$ are separated in the graph, then their probabilities are also independent.
    ${ }^{2}$ The joint probability of the set of variables $X$ and its parameters is equal to the product of probabilities of each of the smaller models $\operatorname{Pr}\left(X_{i} \mid \Pi_{X_{i}} ; \Theta_{X_{i}}\right)$ for each variable $X_{i}$ given its parents $\Pi_{X_{i}}$ and its parameters $\Theta_{X_{i}}$.

Figure 1
Three Examples of DAGs
![img-0.jpeg](img-0.jpeg)

Note. The DAG on the left is also called a chain. The DAG in the middle is called a common cause model ( Z is the common cause of X and Y ). The DAG on the right is called a collider ( X and Y cause Z ). In the DAG on the left and the one in the middle, X and Y are not independent, but they are conditionally independent given Z . In the DAG on the right, X and Y are independent, but they are not conditionally independent given Z .
effect $(C)$ in the collider (that is, studying the associations while conditioning on the effect) leads to different estimates compared to studying the two causes individually. This phenomenon is known as collider bias (Berkson, 1946), and in network analysis it
is known to induce spurious edges among nodes, and likely affects the generalizability of results when applied to the wrong population (De Ron et al., 2019; McNally, 2021). DAGs are tools that can help researchers identify instances of collider bias.

Figure 2
An Example of Bayesian Network of Four Nodes
![img-1.jpeg](img-1.jpeg)

Note. Elevated Mood has two directed edges towards increased energy and language-thought disorder, and speech-disorder receives two directed edges from increased energy and language-thought disorder. Increased energy and language-thought disorder are d-separated given elevated mood and speech disorder. Elevated mood and speech disorder constitute the Markov blanket of both increased energy and language-thought disorder. Increased energy, language-thought disorder and speech disorder constitute a v-structure (collider). See the online article for the color version of this figure.

## Equivalence Classes

Although a factorization of the probability distribution of $X$ is uniquely identified by a DAG, a DAG is not uniquely identified by a factorization of the probability distribution. For instance, patterns of edges like $v_{j} \rightarrow v_{i} \rightarrow v_{k}, v_{j} \leftarrow v_{i} \leftarrow v_{k}$ and $v_{j} \leftarrow v_{i} \rightarrow v_{k}$ lead to equivalent probability distributions (see Appendix).

Hence, several edges in a DAG can be reversed without changing the conditional (in)dependence relationships in $X$. In other words, if no new v-structure (or cycle) is created, we are just producing equivalent DAG representations of the same set of conditional (in)dependence relationships. All such DAGs are then part of an equivalence class that is uniquely identified by the undirected graph underlying these DAGs and by the v-structures. The direction of other edges is either uniquely identified because one of two directions would introduce a new v-structure or a cycle (these are sometimes called compelled edges), or completely undetermined. This results into a completed partially directed graph (Castelletti et al., 2018; Chickering, 2002a).

## Probability Distributions for Bayesian Networks

In this section, we introduce the most common probability distributions used in BNs as well as their limitations.

The three most common probability distributions for BNs are discrete, ordinal, Gaussian, and conditional linear Gaussian (Scutari \& Denis, 2021). These probability distributions satisfy the following requirements: First, the structure of the BN should be learned efficiently from data by using statistical tests or goodness-of-fit measures; second, the BN should be flexible, that is, distributional assumptions should not be too strict; third, the BN should be easy to query to perform inference.

## Discrete and Ordinal Bayesian Networks

In discrete BNs, local distributions of $X_{i} \mid \Pi_{X_{i}}$ are composed of conditional probability tables for each node given all other parent nodes, that is, the configuration of values of its parents (Spirtes \& Meek, 1995). Learning the structure of BNs from discrete variables is particularly useful in the case of psychological data because most measurement tools are scored on Likert scales. Although using discrete variables is a helpful solution so that dependencies need not be linear, there may be some loss of information, particularly in the case of ordinal variables (such with Likert scales) that will be treated as categorical, because the ordinality of data is lost, as shown in the related domain of GGMs (Isvoranu \& Epskamp, 2021). Moreover, to deal with this problem, many applied researchers treat Likert data as continuous in estimating network models (Briganti et al., 2018, 2019). This is why investigators have tested how well one can estimate BNs from ordinal data (Cui et al., 2016; Luo et al., 2020; Musella, 2013; Tsagris et al., 2018).

## Gaussian Bayesian Networks

Gaussian BNs (which are different from Bayesian GGMs) follow a multivariate normal distribution with mean $\mu$ and a var-iance-covariance matrix $\sum_{i} X \sim N\left(\mu_{i} \sum\right)$, with a precision matrix $\Omega$ computed as the inverse of the variance-covariance matrix $\Omega=\sum^{-1}$.

The partial correlation coefficients $\rho_{i j}$, which model the residual correlation between two nodes after controlling all other nodes, are computed from the precision matrix as $\rho_{i j}=-\Omega_{i j} / \sqrt{\Omega_{i j} \Omega_{i j}}$ where $\Omega_{i j}$ is the element of $\Omega$. If $v_{i}$ and $v_{j}$ are d-separated in the DAG (or in the case of violation of the faithfulness assumption), the absence of an edge $v_{i} \rightarrow v_{j}$ in the DAG between the two nodes by definition implies the conditional independence $\left(\rho_{i j}=0\right)$ between the two variables $X_{i}$ and $X_{j}$ given all subsets of the remaining variables (we refer the reader to The Inductive Causation Algorithm section to have a better understanding on why going through all subsets of variables is necessary). From this, it follows that most edges of a Gaussian BN belong to a subspace of a GGM (a partial correlation network), except specific independence relationships, such as a collider structure. On the other hand, cycles can be represented in a GGM but not a Gaussian BN.

As for the local distributions, $X_{i} \mid \Pi_{X_{i}}$ are linear regression models with $\Pi_{X_{i}}$ acting as regressors. This assumes that all dependencies are linear (Grzegorczyk, 2010), a requisite for the distribution of $X$ to be multivariate normal. This may be advantageous in modeling Likert scales, but only if these scales are designed so that the items on the scale increase in linear increments (that is, Item 2 implies twice the intensity of Item 1, Item 3 implies three times the intensity of Item 1, and so forth). When this is not the case, the numbering of the items on the Likert scale leads the BN to incorrectly interpret the items as equidistant from each other and the resulting estimates of the $\rho_{i j}$ will be biased.

Gaussian BNs have two main limitations. First, few real-world multivariate data sets follow a multivariate Gaussian distribution (the same applies to partial correlation networks since the probability distribution is the same). Second, computing partial correlations can be challenging in data sets with a large number of variables because of singularities, that is, perfect linear relationships between two variables (Lin et al., 2014). Although exact linear correspondence rarely occurs, relationships that are almost singular may result in numerical precision issues and may make BNs difficult and time-consuming to learn.

## Conditional Linear Gaussian Bayesian Networks

Conditional linear gaussian BNs contain both discrete and continuous nodes and subsume both Discrete BNs and Gaussian BNs. In terms of local distributions, discrete nodes have conditional probability tables, whereas continuous nodes have a set of linear regression models, one for each configuration of the discrete parents, and with the continuous children as regressors (Cowell, 2005). In such networks, continuous nodes cannot be parents of discrete nodes, which is a strong limitation for treating mixed data: only a given set of edges can exist in the DAG, which is an important limitation on what models can be encoded by the network structure.

## Structure Learning of Bayesian Networks

Structure learning algorithms learn the structure of BNs from data, possibly integrating external expert knowledge if available. Constraint-based algorithms use statistical tests to learn conditional independence relationships (the constraints themselves); scorebased algorithms rank candidate DAGs based on some goodness-of-fit criterion; hybrid algorithms use conditional independence

tests to exclude most candidate DAGs, and then perform a scorebased search on those that are still under consideration. In addition, specific edges can be whitelisted (included) or blacklisted (excluded) in candidate DAGs by default based on prior knowledge: this helps the structure learning algorithm in its choice of good candidate models (Scutari \& Denis, 2021).

All algorithms in this section are implemented in the R package bnlearn (Scutari, 2010), Version 4.7. Two other packages that implement some algorithms for BNs are pcalg (Kalisch et al., 2012; Kalisch \& Bühlmann, 2007) and BiDAG (Suter et al., 2021).To showcase the functions and their output, we use a data set consisting of seven key items from the 20-item Zung Self-Rating Depression Scale (Zung, 1965) from 1,090 subjects. A detailed description of the data appears elsewhere (Briganti et al., 2021). In this case, we selected only seven nodes out of the 20 nodes in the scale to simplify the data visualization in the tutorial. The data and the code accompanying this tutorial are available in our repository on the Open Science Framework (https://osf.io/fne9m/; Briganti, 2021), with information related to the package versions used to perform the different analyses (Briganti et al., 2021). To read the data, one can use the following commands

```
library("readr")
data <- read_table("data.csv", sep=";", header=TRUE)
# this loads the data
```


## Assumptions in Structure Learning

Most structure learning algorithms make several fundamental assumptions (Dawid, 2010; De Campos \& Ji, 2011; Maathuis et al., 2018):

- The underlying structure that is to be learned is indeed a DAG.
- There is no selection bias and there are no latent or confounding variables, that is, all the common causes of all measured variables have been measured: this assumption is also known as causal sufficiency.
- Only the variables that are d-separated in a DAG will be independent, the others will be dependent: This assumption is also known as causal faithfulness, which is the converse of the Markov property.
- The only relationships between the random variables in $X$ should be conditional independencies, the only kind of relationships that can be encoded by BNs.
- Each node in the network must represent one random variable in $X$. There should not be multiple nodes which are deterministic functions of the same random variable in $X$ (such as a sum score of two variables). This is usually the case in psychological networks since separate symptoms are used as input.
- Observations must be independent realizations; if not, the network should be otherwise defined, such as a dynamic BN in the case of temporal dependence, because observations are not independent as a single subject is measured over multiple occasions (Song et al., 2009).
- The global probability distribution $P(X)$ must be strictly positive: that is, every combination of every possible value of the variables in $X$ must represent an event that is observable in principle; this is needed to have uniquely determined Markov blankets and therefore an identifiable model. This is always the case in psychological data, because we measure events that patients report (e.g., fatigue) or that we observe (e.g., crying).
Most, but not all, algorithms require satisfaction of these assumptions, and some are incapable of testing whether the assumptions hold. Algorithms in the fast causal inference (FCI) family are consistent when selection bias occurs or when a latent common cause is present. Using this kind of approach has multiple implications for drawing inferences. For instance, a directed edge from Node A to Node B in the presence of latent variables entails that A is a cause of B, but does not entail that A is a direct cause of B (Maathuis et al., 2018).

For examples of data sets where the assumption of independent realizations is violated due to temporal dependencies among variables, see studies on time-series networks (Bringmann et al., 2013; Epskamp, 2020) or panel data networks (Briganti et al., 2021).

## Stability in Structure Learning Algorithms

The structure of BNs may vary when performing a learning algorithm several times. For cross-sectional studies, it is desirable to study a "stable" network structure, that is, a set of edges and directions that is unlikely to vary. Stability is an important topic in network analysis: researchers need to study stable networks whose structure is likely to be influenced by factors such as sample size. For partial correlation networks, one can use bootstrapping methods to evaluate the stability of network estimates (Epskamp et al., 2018). It is possible to directly account for stability in structure learning in a similar way: The same algorithm learns a sufficiently large number of BNs from bootstrap samples and we only consider edges that appear in a proportion of BNs higher than some threshold. Previous empirical papers (Briganti et al., 2020, 2021) only included edges that appeared in more than $85 \%$ of networks (this is called strength), and whose direction appeared in more than $50 \%$ of networks (this is called minimum direction). We recommend that researchers only report stable BNs obtained in this way, and that they should use 100-200 bootstrap samples to ensure the proportion of BNs in which each edge appears are estimated accurately. In addition, the proportion of times each edge was included in the stable BNs can be reported.

## Constraint-Based Algorithms

Constraint-based algorithms are based on Pearl and Verm's (1991) work on causal graphical models. This class of algorithms identifies conditional independences (the "constraints") with statistical tests and connects nodes that are not independent. The algorithms determine the sequence of tests that will be applied to the data, typically starting from marginal tests (that is, not conditioning on any variable) and gradually increasing their complexity (adding conditioning variables) to maximize speed and statistical power while ensuring the accuracy of the learned networks.

## Tests for Conditional Independence

Two random variables $X$ and $Y$ are conditionally independent given a third random variable $Z$ if, given knowledge of $Z$, knowledge of whether $X$ occurs provides no information on the likelihood of $Y$ occurring, and knowledge of whether $Y$ occurs provides no information on the likelihood of $X$ occurring (Dawid, 1979). Testing for conditional independence is a necessary step for con-straint-based algorithms because conditional independence relationships themselves constitute the constraint. We hereby cite three default conditional independence test in bnlearn; further details appear in comprehensive reviews of the topic (Edwards, 2012). The asymptotic $\chi^{2}$ mutual information test is the default for categorical and mixed variables: It is an information-theoretic distance measure related to the deviance of the tested models and proportional to the log-likelihood ratio (the two differ by a factor), with the degrees of freedom equal to the number of free parameters in the two models (under the assumption that all parameters can be estimated). The Hotelling's exact test is the default for continuous variables: it is the multivariate version of the Student's $t$ for testing the null hypothesis that the correlation is null. The Jonckheere-Terpstra test is the default for ordinal variables: it is a trend test that generalizes the Wilcoxon test (which only tolerates one ordinal variable compared to a binary factor) to two ordinal variables. A comprehensive review of methods to test for conditional independence exceeds the scope of this tutorial, but appears in the bnlearn manual (Scutari, 2010).

## The Inductive Causation Algorithm

The inductive causation (IC) algorithm (Pearl \& Verma, 1991) was the first and simplest structure learning constraint-based algorithm. Although more modern algorithms are preferable for practical applications, all evolved from IC and thus share the same fundamental steps; hence we will describe IC in detail for illustrative purposes.

The algorithm starts from a complete graph in which each variable is connected to all other variables by an undirected edge. First, for each pair of variables $A$ and $B$ in $\mathbf{X}$, the algorithm searches for a set $\mathcal{S}_{A B}$ such that $A$ and $B$ are independent given $\mathcal{S}_{A B}$ and such that $A$ and $B$ are not part of it $\left(A, B \notin \mathcal{S}_{A B}\right)$. Edges between all such pair of variables are removed. The algorithm composes $\mathcal{S}_{A B}$ starting from a list of no variables (with an empty $\mathcal{S}_{A B}$ ) then each single variable other than $A$ and $B$ in $\mathbf{X}$, then with a combination of other variables, until all combinations have been tried to remove the edge. Because of this, algorithms derived from the IC have one weakness: the complexity in the number of nodes in a graph (Li et al., 2019). Second, for each pair of variables that are not connected by an edge but are both connected to a common neighbor $C$, the algorithm checks whether $C \in \mathcal{S}_{A B}$ : if $C \notin \mathcal{S}_{A B}$, then the direction of edge $A-C$ becomes $A \rightarrow C$ and that of edge $C-B$ becomes $C \leftarrow B$. Third, the direction of the edges that are still undirected is set following two rules: if $A$ is adjacent to $B$ and there is a strictly directed path from $A$ to $B$ (that is, all edges in the path are directed), then $A-B$ becomes $A \rightarrow B$; if $A$ and $B$ are not adjacent but $A \rightarrow C$ and $C-B$, then $C-B$ becomes $C \rightarrow B$. This step ends the algorithm which then returns the completed partially directed graph in which only those edge directions that can be uniquely identified from the data are represented.

The IC algorithm is implemented by the Peter and Clark (PC) algorithm (Spirtes et al., 1993), which starts from a saturated network and then performs tests that gradually increase the number of conditioning nodes. Constraint based algorithms treat BNs as perfect maps, ${ }^{3}$ that is

$$
A \Perp_{P} B \mid C \Rightarrow A \Perp_{G} B \mid C
$$

This is assumption is also called faithfulness, and it is analogous to causal faithfulness from a purely probabilistic perspective. This assumption cannot be empirically verified. However, the assumption has the advantage of not requiring a strictly positive $P(X)$ to have uniquely defined Markov blankets.

In the R package bnlearn Version 4.7 (Scutari, 2010), the PC algorithm is implemented in the pc.stable() function. To plot the graph in a consistent fashion with all other network analyses in psychological literature, we use the qgraph package Version 1.9 (Epskamp et al., 2012).

First, we load the necessary packages, that is, bnlearn and qgraph.

```
library("bnlearn") # this loads the bnlearn package
library("qgraph") # this loads the qgraph package
```

Second, we perform the PC algorithm to learn the structure of the BN.

BNpc $<-$ pc.stable(data) \# this performs the algorithm
qgraph (BNpc) \# this plots the network
Third, we obtain a stable BN.

```
BST<- boot. strength(data, # this includes the data set
    R = 200, # this sets the number of boots
    algorithm = "pc.stable") # this sets the algorithm
# note that boot. strength is likely to give warnings
```

Fourth, we include the edges that appear in $85 \%$ of networks and whose direction appears in more than $50 \%$ of networks, and we compute the averaged network.

```
bst1 <- BST[BST$strength > 0.85 & # this sets the strength
    BST$direction > 0.5,] # this sets the minimum
    direction
    avgnet1 <- averaged.network(BST,
    threshold = 0.85) ## compute the average
network
```

[^0]
[^0]:    ${ }^{3}$ The probabilistic independence of $A$ and $B$ given $C$ is true if and only if the graphical independence of $A$ and $B$ is true.

Figure 3
A BN Learned Through the PC Algorithm (Left) Compared With a Regularized Partial Correlation Network (Right)
DAG
![img-2.jpeg](img-2.jpeg)

GGM
![img-3.jpeg](img-3.jpeg)

Note. Edge thickness and color saturation denote the edge weight. See the online article for the color version of this figure.

Finally, we plot the averaged network with qgraph.
qgraph (avgnet1, layout="circle") \# this plots the network with qgraph

The resulting network can be visualized in Figure 3.

## Other Constraint-Based Algorithms

Other well-known constraint-based algorithms include the grow-shrink (GS) algorithm (Margaritis, 2003) and the incremental association (IAMB) sets of algorithms (Tsamardinos et al., 2003), which first learn the Markov blanket for each node in the network to reduce the number of tests required by the IC algorithm. The initial network is assumed not to have any edges.

BNgs $<-$ gs (data) \# this performs the GS algorithm
BNiamb $<-$ iamb (data) \# this performs the IAMB algorithm

## Score-Based Algorithms

Score-based structure learning algorithms assign a score to each candidate BN. Network scores focus on the DAG as a whole (as opposed to individual constraints) and are goodness-of-fit statistics that assess how well the DAG mirrors the dependence structure in the data (Scutari \& Denis, 2021). Two methods for scoring are the Bayesian information criterion (BIC) and posterior probabilities from flat priors (Daly et al., 2011; Friedman \& Koller, 2003; Geiger \& Heckerman, 2002; Goudie \& Mukherjee, 2016; Grzegorczyk \& Husmeier, 2008; Heckerman \& Geiger, 1995; Kuipers et
al., 2018b; Madigan et al., 1995; Pensar et al., 2020). Score-based algorithms are typically applications of heuristic search algorithms, which are not guaranteed to return the highest-scoring DAG. Exact search algorithms, which do provide this guarantee, are markedly slower than heuristic algorithms and are not feasible for many practical applications (Cussens, 2012; Koivisto \& Sood, 2004; Scanagatta et al., 2015; Suzuki, 2017). Hence, we will not consider them further.

## The Hill-Climbing Algorithm

The Hill-Climbing (HC) algorithm (Russell \& Norvig, 2002) is a greedy search algorithm that explores DAGs by single-edge additions, removals, and reversals. First, the algorithm chooses an initial candidate network structure $\mathcal{G}$ (it chooses by default the empty DAG) and computes its score $\operatorname{Score}(\mathcal{G})$. Second, it sets maxscore $=\operatorname{Score}(\mathcal{G}) .{ }^{4}$ Third, the algorithm computes the score of the modified networks $\mathcal{G}^{*}$ obtained by every possible edge addition, deletion or reversal that does not result in a cyclic network. If any $\mathcal{G}^{*}$ has $\operatorname{Score}\left(\mathcal{G}^{*}\right)>\operatorname{Score}(\mathcal{G})$, the new score is updated in maxscore $=\operatorname{Score}\left(\mathcal{G}^{*}\right)$ and $\mathcal{G}^{*}$ becomes the new candidate network. Finally, the algorithm returns the final network when no $\mathcal{G}^{*}$ has a higher score than $\mathcal{G}$.

BNhc $<-$ hc (data) \# this performs the HC algorithm

[^0]
[^0]:    ${ }^{4}$ maxscore represents the maximum score computed from a network structure; the goal of the algorithm is to find a modified network structure that will have a higher score than maxscore, then updates maxscore as it goes, until it finds the highest score possible.

## Other Score-Based Algorithms

Three well-known score-based algorithms include the greedy equivalence search (Chickering, 2002b), a HC algorithm over equivalence classes instead of graphs (which minimizes the search space), the tabu search (Glover, 1990), a modified HC algorithm that does not stop at the first DAG for which every possible edge addition, deletion, or reversal does not improve the score, but further explores the space of DAGs to find a better DAG; and genetic algorithms (inspired by evolutionary biology) that perturb (mutation) and combine (crossover) features through several generations of structures while retaining those yielding better scores (Davis, 1991).

BNtabu <- tabu(data) \# this performs the Tabu algorithm.

## Hybrid Algorithms

Hybrid algorithms combine the two previous classes of con-straint-based and score-based algorithms: They are the state of the art for many problems (Scutari \& Denis, 2021). They work by learning some conditional independence constraints to reduce the number of candidate networks prior to finding the network that maximizes a given score function (Kuipers et al., 2018a; Tsamardinos et al., 2006).

The sparse candidate algorithm (Friedman et al., 2013) was the first example of this approach in the literature. It is an iterative algorithm that restricts the parents of each variable to belong to a small subset of candidates. First, in a network $\mathcal{G}$, the algorithm restricts the candidate parents for a node $X_{i} \in \mathbf{X}$ to the parents of $X_{i}$ in $\mathcal{G}$ in a set $\mathbf{C}_{i}$. Second, the algorithm finds the network structure $\mathcal{G}^{*}$ that maximizes $\operatorname{Score}\left(\mathcal{G}^{*}\right)$ among the networks in which the parents of each node $X_{i}$ are included in the corresponding set $\mathbf{C}_{i}$, then sets the new network $\mathcal{G}^{*}=\mathcal{G}$. After the steps are repeated, the algorithm returns the graph $\mathcal{G}$.

The sparse candidate algorithm is implemented in the rsmax2 () function, which performs the step of restricting and maximizing only once as further steps rarely yield better DAGs (Friedman et al., 2013).

BNrs <- rsmax2 (data) \# this computes the rsmax2 algorithm.

## Common Issues to Consider When Learning BNs

## Choice of Algorithm

Which approach should psychopathologists choose to learn the structure of a BN? The number of possible configurations of algorithms, scores, conditional independence tests, and all the tuning parameters that accompany them is indeed overwhelming. A comprehensive simulation study showed that there were no systematic differences in performance or sensitivity to error in real-world data when comparing the three classes of learning algorithms (Scutari et al., 2018). If we consider individual algorithms, none consistently outperforms the others discussed here. This is also the case in our own example data set: The three classes of algorithms retrieve very similar structures, albeit with some differences in edge directions (see Figure 4). Another comprehensive comparison of different structure learning algorithms showed that choosing an algorithm also depends on its reliability and resilience, and that synthetic performance may overestimate real-world performance (Constantinou et al., 2021).

Although researchers should clearly present the algorithm chosen for structure learning and report the stable network structures, we recommend that they also perform the two other classes of structure learning algorithms as robustness checks. This would disclose the edge directions that vary among algorithms.

## Assumptions Needed for Causal Inference

BNs whose DAGs are in the same equivalence class are probabilistically indistinguishable: It is impossible to choose one over the other from data without resorting to additional expert knowledge. Therefore, inferring causal relationships from observational data should be done very carefully: The causal effects whose direction is supported by the data are those that correspond to edges with a defined direction in the completed partial DAG for the equivalence class.

Figure 4
BNs Learned With the Constraint-Based PC Algorithm (Left), the Score-Based HC Algorithm (Middle), and the Hybrid RS Algorithm (Right)
![img-4.jpeg](img-4.jpeg)

Furthermore, to defend a causal interpretation of a BN we need to satisfy three assumptions. First, each variable $X_{i}$ is conditionally independent of its direct and indirect effects and from other variables given its direct causes: this is known as the causal Markov assumption.

Second, there is a DAG faithful to the probability distribution of $X$ such that the dependencies arising from d-separations in the DAG are the only ones in the probability distribution. The faithfulness assumption for causal inference implies that any population produced by the DAG has the same conditional independence relationships obtained by applying d-separation to it. However, this assumption can be challenged by selection bias; that is, the population can be "unfaithful" to the DAG. When estimating DAGs representing the causal relationships among symptoms of mental disorders or psychological constructs, the population could be unfaithful to the DAG if it were estimated from a specific subsample. For example, a network structure of depressive symptoms in manic patients will show different conditional independence relationships than a network structure estimated from unipolar depressive patients. For further details concerning selection bias in network psychopathology, we refer to more complete overviews of the topic (De Ron et al., 2019; McNally, 2021).

Third, there must be no latent variable that acts as a confounding factor thus introducing spurious dependencies among the observed variables, which translate to spurious arcs in the BN A confounding variable A is such that, in a path $A \rightarrow B \rightarrow C, A \rightarrow C$ : this is also known as a backdoor path from $A$ to $C$. In psychological data sets, confounding variables are an important issue since in many cases all relevant variables are not measured or included in a model. This assumption also concerns many studies designed from a latent variable point of view whereby items or symptoms presumptively reflect unobserved factors that cause their emergence and covariance. A possible solution to help overcome this issue is eliminating topological overlap among nodes (Fried \& Cramer, 2017). That is, we can create composite variables to ensure that items tapping the same construct do not appear as individual, near-synonymous nodes. Hence, each node would constitute a composite variable representing a domain. This has been done with both gaussian graphical models and BNs (Briganti et al., 2019, 2020; Briganti \& Linkowski, 2019). Another way of reducing the number of network components is by using the goldbricker method in the networktools package (Jones, 2017) that identifies colinear network components (that is, topologically overlapping items).

These assumptions are difficult to verify in real-world settings, and the best solution to tackle them is by using blocking in a carefully planned experimental design to screen out confounding factors via randomization, which severs any incoming causal link between the randomized variables and possible exogenous effects, but it is never applied to cross-sectional network studies. In the best-case scenario, scientific experiments can identify a small set of BNs that plausibly fit the data from a causal point of view.

## What Kind of Data Are Needed for Learning?

The data used to learn the structure of a BN and to estimate its parameters are a key driver of the quality of the models we can obtain.

For structure learning, it is important that we have enough data to rank networks accurately using scores and to ensure that the conditional independence tests we use to assess constraints have sufficiently low rates of Type-I and Type-II errors. The ability of structure learning algorithms to recover from errors (that is, incorrectly including or excluding edges in the DAG) is limited, which makes it important to
limit the possibility of such errors occurring. For parameter learning, it is important to have enough data to detect the effect of the parents of each child and to estimate them with sufficient precision. In both cases, we may draw from existing literature on power and sample size calculations for linear and logistic regressions (Demidenko, 2007; Dupont \& Plummer, 1998). When the sign of the effect associated with each edge is important, we may complement traditional power calculations by assessing Type-S errors (Gelman \& Carlin, 2014). In both cases, it is important to remember that both structure and parameter learning operate at the level of the local distributions $X_{i} \mid \Pi_{X_{i}}$ : we only need a sample size large enough to handle the most complex of them. If we assume that the network we are estimating is sparse, so that all nodes have a limited number of parents (say, less than 5), then the sample size required to learn a BN does not necessarily scale with the number of variables.

The number of variables will still determine the computational speed of estimating the model. Different structure learning algorithms will entail different trade-offs between speed and accuracy (Scutari et al., 2018). However, in general the complexity of most structure learning is quadratic in the number of variables if we assume that the network we are trying to learn is sparse. In other words, heuristic score-based algorithms with compute $\mathrm{O}(\mathrm{N} 2)$ network scores, and constraint-based algorithms will perform $\mathrm{O}(\mathrm{N} 2)$ conditional independence tests. If we do not assume the sparsity of the network, then the complexity becomes larger $\mathrm{O}(\mathrm{cN})$ making it difficult to perform learning in the first place. Similar considerations pertain to parameter learning: If nodes have few parents, then local distributions will have few parameters and it is possible to estimate them efficiently.

Interestingly, the increase in the number of network scores or conditional independence tests evaluated during structure learning does not increase the likelihood of errors, as the literature on multiple error adjusting would suggest. It is widely recognized that all structure learning algorithms in this paper are empirically selfadjusting for multiplicity, even though no theoretical characterization of this phenomenon is available in the literature.

The quality of the data is also important. For instance, it is possible to learn BNs from incomplete data (that is, not all values are observed for all variables in all observations) by incorporating ex-pectation-maximization and other classic statistical techniques in structure and parameter learning (Scutari, 2020). It is also possible to learn BNs from the heterogeneous data that arise from trials in which observations are collected under different conditions or with different protocols (Azzimonti et al., 2020). However, handling such issues requires additional assumptions on how the data deviate from the aforementioned assumptions and it reduces power in both structure and parameter learning.

## Bayesian Networks or Pairwise Markov Random Fields?

Empirical researchers may ask whether it is better to perform a network analysis using BNs or pairwise Markov random fields, and how to compare the results from each approach. The difference between the two models from the example data set is shown in Figure 3.

Although pairwise Markov random fields allow for studying the interplay among different symptoms, and identify the most interconnected symptoms (Haslbeck \& Fried, 2017), they cannot distinguish whether the interconnected symptoms are more likely to cause or be caused by surrounding variables: BNs can identify which causal

relationships are admissible in the data set, and therefore complement the information given by current network inference measures estimated from pairwise Markov random fields, given the several critical assumptions, in particular the acyclicity and the absence of latent variables.

The same applies to colliders $(A \rightarrow C-B)$, which are important structures albeit scarcely discussed in the network literature: In pairwise Markov random fields, underlying collider structures can introduce spurious negative edges among variables (De Ron et al., 2019). This means researchers may conclude from a pairwise Markov random field that two symptoms $A$ and $B$ are negatively connected (that is, when Symptom $A$ is strong, Symptom $B$ is more likely to be weak, and vice versa) when in reality a BN may show an underlying collider structure that has $A$ and $B$ as unconnected parents of a third node $C$, if a BN is the true underlying structure.

Finally, researchers should choose the model (pairwise or directed) that fits best their study goal and design (Borsboom et al., 2021): For instance, researchers may prefer BNs for studying the effect of intervention as nodes in a network (Blanken et al., 2019; Kossakowski et al., 2019; Mooij et al., 2020).

## Assessing Goodness of Fit

It is common practice to assess how well a statistical model fits the data, as well as how well it predicts new data, to establish its practical relevance in the literature. This is more complicated for BNs than it is for classic statistical models for two reasons: their use of DAGs to model a multivariate distribution and the lack of a single variable of interest in learning.

First, it important to note that a network score assigned to specific DAG is not itself useful for assessing the goodness of fit of a single model. It is not defined on a normalized scale: It becomes larger and larger in magnitude as the sample size increases and can become smaller and smaller in magnitude the more values the variables can take. Network scores are only useful to compare different DAGs, which is their task in structure learning. Reporting network scores relative to a predetermined reference network can only be useful when such a network can be established in a rigorous way, which is not usually possible without substantial expert knowledge.

Bootstrap resampling and model averaging can reliably assess whether the edges in the BN are reliably supported by the data, rather than the result of statistical noise or measurement error. At a higher level, we can also check that most edges make sense to experts in the substantive domain (for example, PTSD), or blacklisting clinically implausible edges and compare the scores of BNs with and without such expert knowledge (McNally, 2016).

```
BST<-boot.strength(data, R=200,
    algorithm = "pc.stable,"
    debug = TRUE,
    cpdag = TRUE)
# compute the edge strengths
avgnet1 <- averaged.network(BST,
```

threshold $=.85$ )
\# compute the average network
astr1 <- arc. strength (avgnet1,
data,
"bic-g")
\# compute edge strengths
Checking the parameters of the BN is more straightforward, in the sense that each $\operatorname{Pr}\left(X_{i} \mid \Pi_{X_{i}}\right)$ is either a conditional probability table in discrete BNs (Spirtes \& Meek, 1995), a linear model in Gaussian BNs (Grzegorczyk, 2010) or a collection of linear models in conditional Gaussian BNs (Cowell, 2005), which have been all studied in detail in the statistics literature (Koller \& Friedman, 2009; Maathuis et al., 2018; Neapolitan, 2004; Pearl, 2009; Scutari \& Denis, 2021). There are substantial practical guidelines on how to assess goodness of fit in such cases. In a Gaussian BN, each parent is associated with a regression coefficient that expresses how its effect on the child increases or decreases for a unit change in that parent. Furthermore, the standard error associated with the node describes its noisiness in terms of the amount of variance that is not explained by the parents. In a discrete BN, conditional probabilities are assigned to each value that the node takes given the configuration of the values of its parents. In a conditional Gaussian BN, discrete nodes have the same parameters as the nodes of the discrete BN and continuous nodes have the same parameters as the nodes in a Gaussian BN, possibly in a mixture: Hence their interpretation is analogous. This does not, unfortunately, apply to the entire BN.

Finally, we can use BNs as expert systems and run queries on various combinations of nodes and check whether their answers make sense to domain experts. In this context, a query consists in computing the probability of some event involving some variable of interest taking place (for instance, a given score on a symptom X ) given some evidence on other variables (for instance, given scores on other symptoms Y and Z ). If experts can quantify their confidence in observing events under a set of specific circumstances, based on their domain knowledge, we can measure the discrepancy between their confidence and the BN's confidence as a measure of goodness-of-fit. This approach rests, of course, on the availability of reliable expert knowledge on the phenomenon being modeled because we are treating it as a surrogate of ground truth.

## Conclusion

This work contains an introduction to BNs as well as a tutorial on estimating them in R using the three main families of structurelearning algorithms: constraint-based, score-based, and hybrid algorithms. The network obtained contains directed edges, which can be interpreted as admissible causal relationships among symptoms of mental disorders under several assumptions. BNs are models that can complement the popular partial correlation networks in the broad framework proposed by the network theory of mental disorders (Borsboom, 2017).

The field of network analysis is new and uniform methods for investigating DAGs remain unestablished. Our tutorial aims to

offer an introduction to the topic as well as accessible methods to conduct these analyses.

# Appendix 

## Probabilistic Equivalency Between Patterns of Edges

## Patterns of Edges Like $v_{j} \rightarrow v_{i} \rightarrow v_{k}, v_{j} \leftarrow v_{i} \leftarrow v_{k}$ and $v_{j} \leftarrow v_{i} \rightarrow v_{k}$ Lead to Equivalent Probability Distributions

The product of the probability of $v_{j}$, the probability of $v_{i}$ given $v_{j}$ and the probability of $v_{k}$ given $v_{i}$, which describes the probability of $v_{j} \rightarrow v_{i} \rightarrow v_{k}$ is equal to: (a) the product of the probability of $v_{j}$, the joint probability of $v_{i}$ and $v_{j}$ divided by the probability of $v_{j}$, and the joint probability of $v_{i}$ and $v_{k}$ divided by the probability of $v_{i}$; (b) the product of the joint probability of $v_{i}$ and $v_{j}$ divided by the probability of $v_{i}$, and the joint probability of $v_{i}$ and $v_{k}$; (c) the product of the probability of $v_{i}$, the probability of $v_{j}$ given $v_{i}$, and the probability of $v_{k}$ given $v_{i}$, which describes the probability of $v_{j} \leftarrow v_{i} \rightarrow v_{k}$; (d) the product of the probability of $v_{k}$, the probability of $v_{j}$ given $v_{i}$, and the probability of $v_{i}$ given $v_{k}$, which describes the probability of $v_{j} \leftarrow v_{i} \leftarrow v_{k}$.

$$
\begin{gathered}
\underbrace{\operatorname{Pr}\left(v_{j}\right) \operatorname{Pr}\left(v_{i} \mid v_{j}\right) \operatorname{Pr}\left(v_{k} \mid v_{i}\right)}_{v_{j} \rightarrow v_{i} \rightarrow v_{k}}=\operatorname{Pr}\left(v_{j}\right) \frac{\operatorname{Pr}\left(v_{i}, v_{j}\right)}{\operatorname{Pr}\left(v_{j}\right)} \frac{\operatorname{Pr}\left(v_{i}, v_{k}\right)}{\operatorname{Pr}\left(v_{i}\right)}= \\
=\frac{\operatorname{Pr}\left(v_{i}, v_{j}\right)}{\operatorname{Pr}\left(v_{i}\right)} \operatorname{Pr}\left(v_{i}, v_{k}\right)=\underbrace{\operatorname{Pr}\left(v_{i}\right) \operatorname{Pr}\left(v_{j} \mid v_{i}\right)}_{\left.v_{j} \leftarrow v_{i} \rightarrow v_{k}\right.}
\end{gathered}
$$

$$
=\underbrace{\operatorname{Pr}\left(v_{k}\right) \operatorname{Pr}\left(v_{j} \mid v_{i}\right) \operatorname{Pr}\left(v_{i} \mid v_{k}\right)}_{v_{j} \leftarrow v_{i} \leftarrow v_{k}}
$$

Received February 1, 2021
Revision received November 23, 2021
Accepted December 6, 2021