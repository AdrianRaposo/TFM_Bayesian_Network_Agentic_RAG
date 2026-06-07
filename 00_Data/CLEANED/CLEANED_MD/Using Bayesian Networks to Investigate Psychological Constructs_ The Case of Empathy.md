# Using Bayesian Networks to Investigate Psychological Constructs: The Case of Empathy 

Psychological Reports<br>2022, Vol. 0(0) I-I3<br>(c) The Author(s) 2022<br>Article reuse guidelines:<br>sagepub.com/journals-permissions<br>DOI: IO.II77/0033294I22II467II<br>journals.sagepub.com/home/prx (c)SAGE

## Giovanni Briganti

University of Mons, Mons, Belgium; Université libre de Bruxelles, Brussels, Belgium; Harvard University, Cambridge, MA, USA

## Jean Decety

University of Chicago, Chicago, IL, USA

## Marco Scutari

Istituto Dalle Molle di Studi sull'Intelligenza Artificiale, Manno, Switzerland

## Richard J. McNally

Harvard University, Cambridge, MA, USA

## Paul Linkowski

Université libre de Bruxelles, Bruxelles, Belgium


#### Abstract

Network analysis is an emerging field for the study of psychopathology that considers constructs as arising from the interactions among their constituents. Pairwise effects among psychological components are often investigated by using this framework. Few studies have applied Bayesian networks, models that include directed interactions to perform causal inference on psychological constructs. Directed graphical models may be less straightforward to interpret in case the construct at hand does not contain symptoms but instead psychometric items from self-report measures. However, they may be useful in validating specific research questions that arise while using standard


[^0]
[^0]:    Corresponding Author:
    Giovanni Briganti, Chair of Artificial Intelligence and Digital Medicine, Faculty of Medicine, University of Mons, Avenue du Champs de Mars 6, 7000 Mons, Belgium
    Email: giovanni.briganti@hotmail.com

pairwise network models. In this study, we use Bayesian networks to investigate a well-known psychological construct, empathy from the Interpersonal Reactivity Index, in large two samples of 1973 university students from Belgium. Overall, our results support the hypotheses emphasizing empathic concern (i.e., sympathy) as causally important in the construct of empathy, and overall attribute the primacy of emotional components of empathy over their intellectual counterparts. Bayesian networks help researchers identify the plausible causal relationships in psychometric data, to gain new insight on the psychological construct under examination, help generate new hypotheses and provide evidence relevant to old ones.

# Keywords 

Bayesian networks, social constructs, empathy, network psychometrics, structure learning

Scientific theories in psychology seek to provide a mechanistic explanation for neurobehavioral functions in terms of structures, processes, and consequences (Decety \& Cacioppo, 2010). Psychological constructs facilitate the understanding and explanation of human behavior by enabling prediction, with a certain probability, of how an individual is likely to act in a certain situation. Psychological constructs vary in granularity and diverse attributes such as, inspiration (Thrash \& Elliot, 2003), recovery from psychiatric illness (Corrigan et al., 1999), word fluency (Ruff et al., 1997), identification with all humanity (McFarland et al., 2013), and ruralness (Melton, 1983). Some authors argue that mental disorders can be modeled as psychological constructs suitable for psychometric characterization (Cronbach \& Meehl, 1955; Fried, 2017). Because constructs address important phenomenological experiences, there exists a reciprocal interplay between the development of theory and empirical measures of the construct (Fried, 2020). Regardless of its popularity, a psychometric test must first earn evidence of its validity prior to its serving as the basis for interpreting its results (Decety et al., 2018) Most scales developed in recent decades and currently used in clinical practice depict psychological constructs from a common cause framework. That is, the construct itself is a hidden entity ("latent variable") that causes the values on measurable items embodied in the scale.

Psychological constructs such as self-regulation, morality, attachment, empathy, trust do not qualify as natural kinds localized in the brain (Kendler et al., 2011) but require disaggregation into their components while answering the challenge of avoiding narrow definitions that fail to capture the breadth of a function and vague concepts that may well resonate with lay knowledge and common sense but have little if any scientific validity and utility. In other terms, a complex view of mental disorders is needed: it is provided within the "network framework".

The network theory of mental disorders (Borsboom, 2017; McNally, 2016) has emerged as an alternative to the latent construct framework, and argues instead that

psychological constructs are complex systems ("networks") that arise from the pairwise interactions among their constituents (items, such as traits or symptoms). Network theory has been operationalized through its psychometric counterpart, network analysis (Borsboom \& Cramer, 2013) which provides a set of statistical techniques to model psychological constructs as networks composed of nodes (the items constituting the psychopathological construct) and edges (the connections among items). Networks are increasingly popular for the analysis of psychological constructs (Borsboom et al., 2021), such as personality (Costantini et al., 2015), health-related quality of life (Kossakowski et al., 2016), intelligence (van der Maas et al., 2006), attitudes (Dalege et al., 2017), and alexithymia (Briganti et al., 2020; Briganti \& Linkowski, 2020).

Pairwise Markov Random Fields, which include the Gaussian Graphical Models (partial correlation networks for continuous data), the Ising Model (for binary data), and Mixed Graphical Models (for mixed data) are the main group of statistical models used in the network literature: these models include nodes that mutually influence each other (Borsboom et al., 2021; Epskamp \& Fried, 2018; Marsman et al., 2018; van Borkulo et al., 2014). However, we may be limited in the causal interpretation of a psychological construct when using these models: since their edges are undirected, it is impossible to tell whether an item A is more likely to cause or be caused by another item B because the edges cannot encode this information.

We can overcome this limitation and retrieve the plausible causal relationships within psychological constructs by using Bayesian Networks (BNs) that also encode the direction of edges (Maathuis et al., 2018; Scutari \& Denis, 2021) and are among the founding principles of causal reasoning (Pearl, 2009; Pearl \& Mackenzie, 2018). BNs have been applied to a handful of empirical studies to investigate mental disorders, such as obsessive-compulsive disorder (Jones et al., 2018; McNally, Mair et al., 2017), psychosis (Moffa et al., 2017), dissociation (Cernis et al., 2021), paranoia (Bird et al., 2019), depression (Briganti, Scutari, \& Linkowski, 2021), posttraumatic stress disorder (McNally, Heeren et al., 2017) and bipolar disorder (McNally et al., 2021). Outside the strictly pathological spectrum, however, we know of only two studies on alexithymia (Briganti et al., 2020), and rumination (Bernstein et al., 2017).

What kind of questions concerning psychological constructs are answerable by using BNs? Indeed, it may seem less straightforward to interpret a directed edge between two items of a construct (e.g., intelligence) than it is with a mental disorder (e.g., depression). In this study, we used BNs to investigate the psychological construct of empathy. The construct of empathy is chosen as it is of interest to most clinicians, and because it was the object of a previous analysis involving networks (Briganti et al., 2018a).

Empathy is understood as the ability to perceive and be sensitive to others' emotions and the desire for their well-being (Decety et al., 2016). In a recent network study (Briganti et al., 2018a), the network structure of the Interpersonal Reactivity Index (IRI) was investigated. The IRI (Davis, 1980) is a self-report questionnaire that identifies empathy as composed of four factors: fantasy (the tendency to get involved in the actions and feelings of fictional characters), perspective taking (the tendency to

comprehend another person's point of view), empathic concern (the feeling of concern for a person in distress), and personal distress (the feeling of unease in stressful situations). In their analysis, Briganti et al. found that empathic concern items were highly contributive to the network's self-determination: they showed high centrality, i.e., interconnectedness with other items.

One recurring challenge in the network literature is whether highly central items are more likely to cause or to be caused by other items in the network (Fried \& Cramer, 2017). In the case of empathy, we want to answer the question "are empathic concern items more likely to cause than be caused by other items in the IRI?" We investigated this by learning BNs from the data set.

The current study is organized as follows. Firstly, we introduce the data set and methods used in this paper: Secondly, we investigate the BNs learned from the data. Thirdly, we discuss the results as well as their limitations and we will outline ways forward in the investigation of psychological constructs with BNs.

# Method 

## Data

The reanalysis of the two data sets with network analytic methods received ethics committee approval from the Comité d'Éthique hospitalo-facultaire Erasme-ULB (Ref. P2017/379).

Empathy Data Set. The empathy data set (Briganti et al., 2018a, 2018) is composed of 1973 French-speaking university students in Belgium who completed the 28 items of the IRI (Davis, 1980). The participants were 17-25 years old ( $M=19.6$ years, $S D=$ 1.6 years), $57 \%$ were women. Even though the full dataset included 1973 participants, only 1270 answered the full questionnaire, which was the only measurement tool for empathy used in the data collection. We dealt with missing data by using pairwise complete observations, i.e., using all available information from every subject. To estimate BNs from the empathy data set, we selected the 10 nodes that are most interconnected in the network. We started by re-estimating the network structure of the full data set 2000 times via nonparametric bootstrapping. We then extracted the top 10 items with the highest bootstrapped strength centrality (that is, the absolute sum of an item's connections). The 10 items are listed in Figure 1. Some of the items are reversed, but they are reverse-scored in the data set.

## Network Analysis

Software for Data Analysis. For the analysis, we used R version 4.1.1 (R Core Team, 2021). The packages bootnet (Epskamp et al., 2018) and qgraph (Epskamp et al., 2012) were used to prepare the data set, and the package bnlearn (Scutari, 2010) was used for learning the BNs.

![img-0.jpeg](img-0.jpeg)

Figure I. Bayesian Network including highly central empathy items from the Interpersonal Reactivity Index.

Network Estimation. A BN is composed of a directed acyclic graph (DAG) and a probability distribution. The DAG $\mathcal{G}=(V, A)$ consists of a set of nodes $V=$ $\left\{v_{1}, v_{2}, \ldots, v_{N}\right\}$ (where $N$ is the number of nodes), which represent variables (such as questionnaire items) and of a set of edges or $\operatorname{arcs} A=\left\{\left(v_{1}, v_{2}\right),\left(v_{2}, v_{3}\right), \ldots\right\}$ that represent all connections between two nodes. In the DAG, all edges are directed from a node $v_{i}$ (a parent node) to a node $v_{j}$ (a child node). The directed edges in a BN represent relationships of conditional probabilistic dependence and can also be interpreted as the plausible causal relationships in the data. To perform rigorous causal inference, however, a list of assumption should be verified, the three most important being (1) that a DAG is the generative process producing the data, (2) causal sufficiency, that is all the causes of a given variable are measured, and (3) faithfulness, that is all the variables connected in the BN are probabilistically dependent (Briganti, Scutari, \& McNally, 2021).

We use Gaussian BNs when the variables associated with the network nodes are continuous or treated as continuous: this is often the case for Likert data in network psychopathology (Briganti, Scutari, \& Linkowski, 2021). Gaussian BNs follow a multivariate normal probability distribution with mean $\mu$ and a variance-covariance matrix $\Sigma, X \sim N(\mu, \Sigma)$, with a precision matrix $\Omega$ computed as the inverse of the variance-covariance matrix $\Omega=\Sigma^{-1}$. The partial correlation coefficients model the residual correlation between two nodes after controlling all other nodes and are computed from the precision matrix as $\rho_{i j}=-\Omega_{i j} / \sqrt{\Omega_{i i} \Omega_{j j}}$ where $\Omega_{i j}$ is the element of $\Omega$. If $v_{i}$ and $v_{j}$ are "d-separated" in the DAG (that is, $v_{i}$ and $v_{j}$ are graphically separated by a set of nodes) the absence of an edge $v_{i} \rightarrow v_{j}$ in the DAG between the two nodes by

definition implies the conditional independence $\left(\rho_{i j}=0\right)$ between the two variables $X_{i}$ and $X_{j}$ given all subsets of the remaining variables.

We used structure learning algorithms to estimate the BN. In our case, we used the score-based "Hill-Climbing" (HC) greedy search algorithm (Russell \& Norvig, 2002) that assigns a Bayesian Information Criterion score to each candidate BN and then gradually chooses the network with the highest score through single edge additions, removals, and reversals. First, the algorithm chooses an initial candidate network structure $\mathcal{G}$ (it chooses by default the empty DAG) and computes its score $\operatorname{Score}(\mathcal{G})$. Second, it sets maxscore $=\operatorname{Score}(\mathcal{G})$. maxscore represents the maximum score computed from a network structure; the goal of the algorithm is to find a modified network structure that will have a higher score than maxscore, then updates maxscore until it finds the highest score possible. Third, the algorithm computes the score of the modified networks $\mathcal{G}^{*}$ obtained by every possible edge addition, deletion, or reversal that does not result in a cyclic network. If any $\mathcal{G}^{*}$ has $\operatorname{Score}\left(\mathcal{G}^{*}\right)>\operatorname{Score}(\mathcal{G})$, the new score is updated in maxscore $=\operatorname{Score}\left(\mathcal{G}^{*}\right)$ and $\mathcal{G}^{*}$ becomes the new candidate network. Finally, the algorithm returns the final network when no $\mathcal{G}^{*}$ has a higher score than $\mathcal{G}$.

Following the state-of-the-art procedures described in BN literature (Briganti, Scutari, \& Linkowski, 2021; Briganti, Scutari, \& McNally, 2021; Scutari \& Denis, 2021), we bootstrapped the learning of the BN 1000 times, and including in the final BN the edges that appeared in more than $85 \%$ of bootstrapped BNs and the edge directions that appeared in more than $50 \%$ of bootstrapped BNs.

# Results 

The BN learned from the empathy data is shown in Figure 1. Two main plausible causal chains appear in the DAG. The first path passes through E4 (Sometimes I don't feel very sorry for other people when they are having problems - Empathic Concern), E14 (Other people's misfortunes do not usually disturb me a great deal. - Empathic Concern), E12 (Becoming extremely involved in a good book or movie is somewhat rare for me - Fantasy), E26 (When I am reading an interesting story or novel, I imagine how I would feel if the events in the story were happening to me. - Fantasy). This path links items from Empathic Concern and Fantasy as respectively parents and child, underscoring the primacy of empathic concern (emotional component of empathy) over fantasy (intellectual component of empathy).

The second path passes through E19 (I am usually pretty effective in dealing with emergencies - Personal Distress), E24 (I tend to lose control during emergencies. Personal Distress), E8 (I try to look at everybody's side of a disagreement before I make a decision. - Perspective Taking) and E10 (I sometimes feel helpless when I am in the middle of a very emotional situation. - Personal Distress). The E9 node (When I see someone being taken advantage of, I feel kind of protective towards them - Empathic Concern) connects the first items of the two main chains, namely E4 and E14, from the first chain and E19 from the second chain to the end items of the opposite chain, namely

E8 and E10 for the second chain and E26 for the first chain. This path links items from Empathic concern and Personal Distress, both assuming parent roles, with items Perspective taking (an intellectual component of empathy), following the same pattern of the first path, that is, obtaining emotional components as more likely to be potential causes, and intellectual components as more likely to be potential effects in the empathy construct.

# Discussion 

Using BNs, we analyzed empathy as a complex system comprising plausible causal relations among its constitutive elements. We investigated the empathy construct from the IRI (Davis, 1980). Our goal was to provide a blueprint of questions answerable by using directed graphs in observational psychometric data.

The empathy BN supports hypotheses emphasizing empathic concern (i.e., sympathy, feeling of pity and sorrow for someone else's misfortunes) as causally important in the construct of empathy (Briganti et al., 2018a; Cliffordson, 2002). Empathic concern (or sympathy) is a major functional component in empathy, confirming the results of empirical studies, which plays a fundamental role in medicine (Decety, 2020; Decety et al., 2016; Gleichgerrcht \& Decety, 2013). In our sample, empathic concern items are not only parent nodes to fantasy items but also to perspective taking items, the two intellectual components of the empathy construct. Unsurprisingly, a similar major role is attributable to the personal distress family of items; personal distress is an emotional component of empathy associated with psychological problems linked to difficult situations, such as burnout (Decety \& Ickes, 2011; Decety \& Lamm, 2009; 2011; Eisenberg \& Eggum, 2009; Gleichgerrcht \& Decety, 2011; Hoffman, 1991; Thomas, 2013). Overall, our results underscore the primacy of the emotional component of empathy over its intellectual counterparts.

The empathy BN was composed of the top 10 items with highest centrality from the data, following the method of Briganti and colleagues (Briganti et al., 2019, 2020). In our case, the network highlighted causal relationships among specific items, potentially helpful for identifying specific "bridging" items that causally connect one domain to another (e.g., item E9 in Figure 1), which allowed proximal items of each chain to be causally connected to distal items of the opposite chain.

Our results should be interpreted considering several limitations. First: one or several assumptions of causal inference may be violated. For instance, causal sufficiency may be violated, if we consider that there are underlying latent variables that cause the items interacting in the network (such as empathy domains described in the IRI). This assumption transcends the purely psychometric level, as there may be sociological, environmental, economic, and even genetic factors contributing to constructs (Røysamb et al., 2018). This is why machine learning approaches to causal inference such as the one used in the study should, whenever possible, be informed by expert knowledge (Briganti, Scutari, \& Linkowski, 2021), even though agnostic approaches may be useful to mine unknown properties or to confirm prior knowledge.

Second, we limited our investigation to structure learning through score-based methods, namely the use of the Hill-Climbing algorithm. Although no structure learning algorithm outperforms others (Scutari et al., 2018), other algorithms within the score-based family, or algorithms from the constraint-based or hybrid families, may have yielded slightly different results (Briganti, Scutari, \& Linkowski, 2021).

Third, our sample comprised university students, which may limit the generalizability of our results. Future studies may endeavor to repeat the structure learning in different samples, such as patients with a given mental disorder (e.g., depression, anxiety, PTSD, bipolar disorders, psychosis, autism) or personalities (e.g., antisocial personality).

In conclusion, BNs allowed us to underscore some properties of empathy (primacy of its emotional components over its intellectual components) from a complex perspective. BNs enable the exploration of causal relationships among the elements constitutive of psychological constructs, suggest potential pathways forward, and test existing theoretical hypotheses.

# Author Contributions 

Giovanni Briganti: Conceptualization, Writing - Original Draft Preparation, Writing - Review \& Editing; Jean Decety: Writing - Review \& Editing; Marco Scutari: Writing - Review \& Editing; Richard J. McNally: Writing - Review \& Editing; Paul Linkowski: Data Collection, WritingReview \& Editing. This study was not pre-registered.

## Declaration of Conflicting Interests

The author(s) declared no potential conflicts of interest with respect to the research, authorship, and/or publication of this article.

## Funding

The author(s) disclosed receipt of the following financial support for the research, authorship, and/or publication of this article: The present study was supported by the Belgian National Funds for Scientific Research (grants 1.5.123.04, 1.5.175.06 and 3.4.553.01.F).

## ORCID iD

Giovanni Briganti (1) https://orcid.org/0000-0002-4038-3363

# Author Biographies 

Giovanni Briganti, MD, PhD, is associate professor and Chair of Artificial Intelligence and Digital Medicine at University of Mons, Belgium.

Jean Decety, PhD is full professor at University of Chicago.

Marco Scutari, PhD is senior researcher in Bayesian Networks and Graphical Models at Istituto Dalle Molli di Studi sull'Intelligenza Artificiale (IDSIA).

Richard J. McNally, PhD is full professor at the Department of Psychology, Harvard University.

Paul Linkowski, MD, PhD is emeritus professor at Université libre de Bruxelles.