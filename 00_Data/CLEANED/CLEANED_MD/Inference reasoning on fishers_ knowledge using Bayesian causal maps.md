# HAL open science 

## Inference reasoning on fishers' knowledge using Bayesian causal maps

Louis Bonneau de Beaufort, Karima Sedki, Guy Fontenelle

## To cite this version:

Louis Bonneau de Beaufort, Karima Sedki, Guy Fontenelle. Inference reasoning on fishers' knowledge using Bayesian causal maps. Ecological Informatics, 2015, 30, pp.345-355. 10.1016/j.ecoinf.2015.09.006 . hal-01231072

## HAL Id: hal-01231072 <br> https://hal.science/hal-01231072v1

Submitted on 19 Nov 2015

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# Inference reasoning on fishers' knowledge using bayesian causal maps 

Louis Bonneau de Beaufort ${ }^{1,2}$, Karima Sedki ${ }^{3}$, Guy Fontenelle ${ }^{2}$<br>${ }^{1}$ IRISA, UMR 6074, Rennes, France<br>${ }^{2}$ AGROCAMPUS OUEST, Rennes, France<br>${ }^{3}$ LIMICS, INSERM UMRS 1142, Paris, France


#### Abstract

Scientists and managers are not the only holders of knowledge regarding environmental issues: other stakeholders such as farmers or fishers do have empirical and relevant knowledge. Thus, new approaches for knowledge representation in the case of multiple knowledge sources, but still enabling reasoning, are needed. Cognitive maps and Bayesian networks constitute some useful formalisms to address knowledge representations. Cognitive maps are powerful graphical models for knowledge gathering or displaying. If they offer an easy means to express individuals judgments, drawing inferences in cognitive maps remains a difficult task. Bayesian networks are widely used for decision making processes that face uncertain information or diagnosis. But they are difficult to elicitate. To take advantage of each formalism and to overcome their drawbacks, Bayesian causal maps have been developed. In this approach, cognitive maps are used to build the network and obtain conditional probability tables. We propose here a complete framework applied on a real problem. From the different views of a group of shellfish dredgers about their activity, we derive a decision facilitating tool, enabling scenarios testing for fisheries management.


qualitative modelling, cognitive maps, bayesian networks, fisher's knowledge, fisheries management, qualitative decision support

# 1 Introduction 

### 1.1 Context

Most of environmental issues and management are currently based on scientific and/or technical knowledge. Other sources of knowledge (empirical or traditional) have been ignored or minimized for a long time. Nowadays, there is a trend to more incorporate all various perceptions, in particular coming from end-users like farmers or fishers, taking account of ground realities [Haggan et al. 2007], [Oliver et al. 2012]. In addition, decisions taken on these grounds should be more easily accepted by stakeholders, within a more effective management process: public participation is a key ingredient of good governance [Pita et al. 2010].

In a recent exploratory study regarding farms management decision support [Daydé et al. 2014], the authors emphasize the need to understand mental choice process because traditional decision support systems assumes idealized situation, with exhaustive knowledge, that does not necessarily exist. In real world, much processing is done in a qualitative manner.

This paper addresses some management issues related to scallop (Pecten maximus) dredging in the Bay of Brest (Western France). We aim here at building a model from fishers statements, considered accurate as a premise, in order to improve management decisions. The main contribution of this work is to show how stakeholders' knowledge can be used for qualitative decision support, through simple scenarios testing, and hence, to facilitate the making decision process.

The typical scallop dredging season in this bay runs from mid-October to late March, with three days of fishing allowed per week. During these periods, the scallops are sold alive. However, from time to time, an ASP toxin (amnesic shellfish poisoning) is detected within the bay, which forces all fishers to freeze their scallops, to be sold at a lower price. Scallop fishers have been experiencing the evolution of this natural resource and its environment for many decades. After an increasing fishing effort during the first half of the 20th century, the stock of scallops fell within a few years from an annual production of about 2500 tons in early 1960s to hundred tons in 1970s. A nursery program was thus initiated in the 1980s, thanks to the Tinduff hatchery leading to annual planting operations. Annual catches rose back to about 350 tons. Furthermore, a "shellfish fishing license" system was introduced in order to finance the hatchery program and to maintain a

limited fishing effort (less than 60 boats).

# 1.2 Working with and for stakeholders 

Stakeholders knowledge is intended here to be used to support stakeholders decision (fisheries board in the first place).

A recent paper, [Voinov and Bousquet 2010] reminds us that even if stakeholder collaboration has become part of nearly every modelling effort, their involvement has often been nominal. The authors nevertheless insist that decisions are implemented more easily and more successfully when they are driven by stakeholders. In their panorama of existing techniques, they recognize much promise in integrating cognitive mapping with bayesian networks.

Dealing with decision support, [Pielke 2003] insists on two different issues. First, conventional modeling and prediction approaches cannot simultaneously meet the needs of both science and decision making. He also raises the matter of uncertainty, that decision makers would like to quantify and reduce. But he advocates that a good model is not necessarily an accurate one. Here, prediction is part of a management decision process, it does not pretend to provide numerical or time-accurate prediction.

Whoever they are, using stakeholders knowledge usually means finding a way to deal with qualitative data, which was already noted 25 years ago: much ecological knowledge is qualitative and fuzzy, expressed verbally and diagrammatically [Rykiel 1989].

### 1.3 Prediction and complex systems

The common challenge of prediction about complex systems is to answer qualitative questions based on partial knowledge [Kuipers 1994]. Usually, these questions were answered through formulating and analyzing differential equations. But ordinary differential equations do not fit to qualitative reasoning: they assume complete and precise models of dynamic systems, which is unrealistic and sometimes unnecessary. Hence was advocated the use of qualitative differential equations.

Other works brought mathematical foundations for qualitative reasonning, and with different formalisms: signed algebra and order of magnitude for example. they have shown how qualitative simulation could be held. For [Travé-Massuyès et al. 2003] qualitative methods unified with numerical or statistical modeling approaches can outperform either pure qualitative or

pure quantitative approaches. Some recent works followed this path, like [Largouët et al. 2012], who used traditional trophic models relying on differential equations in order to build a qualitative model for a fishery. This model based on timed-automata, was successfully used for scenarios testing and possible futures querying. In fact, aquatic systems have been repeatedly modeled and analysed in a qualitative manner, with various approaches including loop annalysis [Dambacher et al. 2003], [Dambacher et al. 2009].

In our paper, we focus on qualitative models within decision-aid contexts, dealing with trends rather than precise output values.

# 1.4 From causal maps to bayesian networks 

Causal Maps (known also as Cognitive Maps, CMs for short) have often been used to model influences between heterogeneous elements of a given system. They have been used for ecosystems management [Hobbs et al. 2002], [Özesmi 2004], agro-systems [Papageorgiou 2009], coastal fishing management [Prigent et al. 2008] or farmers' risk assesment [Winsena 2013].

Causal maps, displayed as directed graphs, are generally defined as the beliefs of a person, for a particular domain [Axelrod 1976]. They represent variables and causal relations among variables within a decision problem, which enables to describe and capture a certain knowledge in a more comprehensive and less time-consuming manner than other methods [Sucheta et al. 2004]. The graphical construction of causal maps is usually easy, even when working with actors not familiarized with such approaches. Even people reluctant to any mathematical formalism can express their views in a qualitative manner.

However, our study main goal is to provide tools to facilitate decision making processes. Drawing inferences in CMs (i.e. obtaining new facts or conclusions from other information) is not an easy task [Laukkanen 1996]. Simple CMs allow a deductive reasoning that predicts an effect from a given cause. Thus, we can get responses about the effects of a given cause, try different scenarios and simulate their effects [Eden et al. 1992]. However, the task becomes very difficult when a CM contains loops, feedbacks or multiple paths. Moreover, even if deductive reasoning can be achieved, we cannot answer why an observed effect is produced. A second limitation in CMs comes from the impossibility to model the uncertainty within the variables.

Bayesian Networks (BN) are a well-established method for reasoning under uncertainty and making inferences [Pearl 1988] and [Pearl 2009]. They

allow to compute the probability of any variable given the state of some observed ones. They can be used either to perform abductive reasoning (i.e. diagnosing a cause given an effect), or for deductive reasoning (i.e. predicting an effect given a cause). Hence, they provide an efficient tool, used within a wide range of subjects, from ecological forecasting [Borsuk et al 2003] to criminal scenarios testing [Vlek et al. 2013]. However, the elicitation of the structure and parameters of a network in complex domains can be a tedious and time-consuming task.

Despite the limitations of each model, their combination called Bayesian Causal Map (BCM) offers a powerful tool [Shenoy and Nadkarni 2001]. This approach uses the initial CM in order to construct the structure of the BCM, but still define local probabilities from experts' knowledge. This might be impractical, because the notion of probability would not be well understood by domain experts. For the structure of the BCM, we follow the procedure described in [Shenoy and Nadkarni 2001]. Concerning the parameters of the BCM, we propose an automatic procedure, relying on the causal values associated to the relations in the CM.

After a short description of the modeling formalisms used in our study and a presentation of the detailed procedure (from fishers' interviews to BCM construction), we will then display our results for this specific study. Finally, we will discuss this approach by emphasizing some of its advantages and drawbacks.

# 2 Modeling formalism 

### 2.1 Cognitive maps

Cognitive or causal maps (CM) are directed graphs representing experts' knowledge. A map expresses individuals judgments, thinking or beliefs about a given situation. It is displayed by a network of causalities or influences among concepts [Chaib-draa 2002] and [Eden 1988], (Figure 1).

Three different components constitute a CM:

1. Concepts: in a cognitive map, a node represents a concept corresponding to a variable of the studied problem.
2. Causal relations: An arc between two concepts depicts a cause-effect (or cause-consequence) relation. If we have a causal relation from concept

![img-0.jpeg](img-0.jpeg)

Figure 1: Example of a simple causal map related to our study (three relations between four concepts).

A towards a concept B (the arrow pointing on B), then A is called a causal concept and B is called an effect concept. In the simplest maps, two kinds of causal relations can be distinguished:

- a positive relation indicates that an increase in the causal concept leads to an increase in the effect concept;
- a negative relation indicates that an increase in the causal concept leads to a decrease in the effect concept;

3. Causal values: Each positive or negative relation can be associated to a numerical value. For example, in fuzzy cognitive maps [Kosko 1986], continuous values in $[1,+1]$ are used. These values represent the relative strength of causal relations.

For example (Figure 1), the causal relation between the number of fishers and the shellfish catches is positive: the more numerous they are, the higher the catches will be. The negative relation between shellfish imports and shellfish catches, means that the higher the imports are the lower the catches will be.

In this paper, the causal values come from statements from stakeholders, in a qualitative manner. The following values have been retained: Low (-1 or +1 ), Medium $(-2$ or +2$)$ or High $(-3$ or +3$)$. These qualitative values are used because they are more intuitive for an elicitation purpose.

# 2.2 Enriched causal map formalism 

In the original cognitive map formalism, each positive or negative relation is assigned with only one value. Therefore, both possible changes (upward or downward) of a variable have opposite effects of the same order of magnitude. But in some cases, this is completely unrealistic: for instance, an increase in Amnesic Shellfish Poisonning toxin ( $A S P$ for short) will lead to a sharp decline of shellfish catches, because selling alive scallops will be prohibited. Instead, a decrease in $A S P$ will have no effect on shellfish catches. Therefore, as originally proposed in [Sedki and Bonneau 2012], we enrich the formalism by assigning two values to each causal relation $\left[V_{1}, V_{2}\right]$.

- $V_{1}$ represents the influence degree on the effect concept when the causal one decreases.
- $V_{2}$ represents the influence degree on the effect concept when the causal one increases.
$V_{1}$ and $V_{2}$ are numerical values, each one can be either positive, negative or null: Low (1 or +1 ), Medium ( 2 or +2 ), High $(3,+3)$ or Null (0). For example, if $V_{2}=3$, a small increase in the causal concept will induce a high increase in the effect concept.
![img-1.jpeg](img-1.jpeg)

Figure 2: An example of the new cognitive map formalism where the influence of $A S P$ on catches is asymmetric: the rise of $A S P$ will lead to a sharp drop of catches, as a decrease will have no effect.

### 2.3 Bayesian networks

Bayesian networks [Jensen and Nielsen 2007] are widely used for decision making, especially when dealing with uncertain information. They are prob-

abilistic models relying on two components:

1. A qualitative component that corresponds to the structure of the network which is represented as a directed acyclic graph (DAG). Each node represents a variable with its possible states, and each arc represents the conditional dependance between these variables.
2. A quantitative component that corresponds to the probability associated to each variable and is represented by Conditional Probability Tables (CPT). The CPTs quantify the uncertainty of variables within the context of its parents. Each variable contains the states of the event that it represents.

The CPT of a given variable includes probabilities of the variable $x$ being in a specific state $i$ given the states $j$ of its parents $P\left(x_{i} \mid x a_{j}\right)$.
![img-2.jpeg](img-2.jpeg)

Figure 3: Simple bayesian network in which shellfish catches depends on the other three variables, for which their present state is known: ASP analysis and shellfish imports are stable and number of fishers is increasing. For this combination of states, the most probable evolution is a shellfish catches rise.

In Figure 3, we have an example of a Bayesian Network (BN) with three variables that reflect the three concepts shown in Figure 2. Each variable displays three possible states: \{decreasing, stable, increasing\}, respectively noted $\{-, \sim,+\}$. There is no arc between the variables imports and number of fishers that are independent. On the other side, there is an arc from imports to catches and from number of fishers to catches, which means that variable catches depends on the other two. Therefore we need to specify a conditional probability distribution table.


Table 1: Expert given conditionnal probabilities of shellfish catches states associated to each possible combinations of the states of variables number of fishers and shellfish imports.

In the Table 1 example, (built from Figure 1) imports and number of fishers have inverse influences on catches, while imports have a lower effect. Thus, when imports increases and number of fishers decreases, the most likely state for catches becomes "decrease". With two variables $(v)$ and three possible states $(s)$ for each one, the usual approach requires an expert to set the nine $\left(s^{v}\right)$ probabilities' sets. The, eliciting all these probabilities becomes a tedious work when $v$ rises.

# 2.4 Ontology 

An ontology is a knowledge base that describes the general concepts of a domain and the relationships that may link these concepts. It is usually organized through a hierarchy of classes (providing an intuitive organization), storing the concepts as individuals, and can be enriched by potential relationships among them:

- lexical relations (synonym, hyponym, hypernym): ASP is-a desease;
- composition relations ("part of", "contains"): stones are-part-of the seabed;
- logical relations ("cause", "consequence"): ASP causes mortality;
- functional relations ("eat", "use", "live" ... ): starfish eats shellfish;

![img-3.jpeg](img-3.jpeg)

Figure 4: Small extract of an ontology, depicting different kinds of relations between concepts.

# 3 Methods 

Causal maps have the advantage to describe and capture the stakeholders knowledge in a comprehensive manner; hence, the modeling is closer to natural language. Unfortunately, they do not model uncertainty with variables, and they only allow limited forms of causal inferences. On the other hand, defining the conditional probabilities in bayesian network from experts is not an easy task, especially when the domain of variables is large and when the combinatory rises. Thus, in order to reduce the complexity of the elicitation step we propose to use the new cognitive map formalism and to transform it into a Bayesian Causal Map (BCM) for the reasoning step, as follows:

1. Sampling the experts' knowledge: causal maps are built to capture fishers' judgments and beliefs.
2. Deriving the summarized map. This step requires a merging procedure.
3. Building the structure of the BCM: a directed acyclic graph (DAG). The structure of the BCM is based on the previously constructed CM. This step requires to remove any loop or feedback.
4. Defining the associated parameters: the probability distributions. This step requires some operations in order to capture the semantic of causal values into conditional probabilities.

We describe the four steps in the following subsections.

# 3.1 Interview process and sample selection 

Several studies using cognitive maps, for example [Prigent et al. 2008] have highlighted the diversity of views held by different actors of a given system. In our study, we have kept unchanged the words or terms expressed by the 17 fishers, all scallop (Pecten maximus) dredgers, encountered in semistructured interviews. Each interview led to the construction of one cognitive map.

These semi-structured interviews addressed predefined themes with prepared open questions, but with flexibility regarding the order of these questions. This interview guideline addressed topics including several sub-themes. Each one contains one open question formulated to avoid any biased response. Three topics were proposed as follows:

- their own appreciation of scallops stocks within the bay,
- their views on the current system of management,
- their perception of the environment of their activity (physical environment, interactions with others).

The relevance and understanding of all prepared questions were first checked thanks to the local committee for marine fisheries and to biologist experts.

A sample is representative when additional interviews provide only very few new themes or concepts. As a consequence, it is impossible to know its size a priori. In a similar study, [Özesmi 2004], the authors have built the accumulation curve of new concepts, a posteriori, and showed that a sample effort between 15 and 20 was acceptable. Beyond this number, the appearance of new concepts in the additional cognitive maps was uncommon. Therefore, 17 fishers who represent about one third of all licensed dredgers, seemed sufficient. We made sure that the sample covered exhaustively some available criteria depicting the sampled population: age, home harbor, involvement in fishing management.

Furthermore, the bias introduced by the intervention of the investigator and any transcription errors were minimized by subsequent validation performed by the fishers.

### 3.2 Similarity measures for concepts comparison

In order to overcome semantic heterogeneity encountered when examining all causal maps, an ontology of fishing activities and environmental matters

in the bay of Brest was built. This approach has already been used with taxonomy-based ontologies only, as in [Prigent et al. 2008] for fisheries management. We used here a readily available ontology dealing with the rather specialized French concepts.

To compute the similarity between two concepts used by fishers to express their judgments and beliefs, we defined a degree of semantic relation, or semantic relatedness described by [Budanitsky and Hirst 2001] or [Resnik 1995]. This measure relies on the ontology, and considers two aspects. The first one relies on the shortest path between concepts: it concerns the minimum number of links connecting two concepts, and the nature of these links. The second one concerns the accuracy level of each concept. For example, Pecten maximus, the latin name for the "great scallop", is obviously much more accurate than environment. This accuracy level can be obtained looking at the concept in the ontology (position in the hierarchy, kind of neighborhood...) or using exogenous information (usually relying on a frequency analysis).

Let $L$ be the length of a path between two concepts in the ontology. $L$ is computed by adding the weights $\omega k_{i}$ associated to each $i$ relations of a kind $k$, used to build the path.

$$
L_{\text {path }}=\sum_{i \in \text { path }} \omega k_{i}
$$

A raw similarity (Rsim) between two concepts $X$ and $Y$ can be obtained from the shortest path length $L_{\overline{X Y}}$, provided an arbitrary threshold. Let $N$, be the length of the shortest path after which two concepts will be considered unrelated.

$$
\begin{cases}R \operatorname{sim}(X, Y)=0 & \text { if } \quad L_{\overline{X Y}}>N \\ \operatorname{Rsim}(X, Y)=1-L_{\overline{X Y}} / N & \text { otherwise }\end{cases}
$$

On the ontology example given on figure 4, the shortest path between starfish and shellfish depends on the weight assigned to each relation. If lexical relations are shorter $(\omega l=1)$ than functional relations $(\omega f=3)$, the shortest path will go through animal with a cumulated length $L=2$.

With $N=3, \operatorname{Rsim}($ starfish, shellfish $)=1-2 / 3$.
Let now $\rho_{X}$ and $\rho_{Y}$ be the accuracy level of $X$ and $Y$. In our case they are derived from the position of the concepts in the ontology, the extreme values being: a concept without children, very accurate $(\rho=1)$ and a concept

without parent, very general $(\rho=0)$. With $\rho \in[0,1]$, the similarity between them is caped by their accuracy level gap: $\operatorname{Asim}=1-\left|\rho_{X}-\rho_{Y}\right|$.

In our study, the considered similarity is the weakest one between the accuracy-based similarity and the shortest-path similarity:

$$
\operatorname{Sim}(X, Y)=\operatorname{Min}(\operatorname{Asim}(X, Y), \operatorname{Rsim}(X, Y))
$$

Back to our example, starfish and shellfish are equally accurate, thus:

$$
\begin{gathered}
\operatorname{Asim}(\text { starfish }, \text { shellfish })=1 \\
\operatorname{Sim}(\text { starfish }, \text { shellfish })=0.33
\end{gathered}
$$

Rsim relies on parameters ( $N$ and $\omega_{k}$ ) that have been adjusted using experts statements. For that purpose, a large number of pairs of concepts, all coming from the ontology, have been built by random selection. Experts were then asked to label each pair with a similarity value. Parameters were adjusted by minimizing the cumulative gap between expert's statements and computed similarity values.

# 3.3 Comparison between causal maps 

We aim at merging all original causal maps in a single synthetic one. But before this merging step, we must ensure that building a single knowledge summary makes sense: we must check that fishers' points of views are not contradictory. Or, if they prove to be contradictory, how many groups can be identified, each one leading ultimately to its own summary.

First a consistency checking can help spoting differences between points of view. In order not avoid miss understated relations, we have built the transitive closure of all causal maps. That is: the set of relations for each causal map is enriched with other relations that can be obtained by transitivity, as described in [Chauvin et al. 2008]: for example, if we know that import reduces market price and that market price reduces shellfish stock, we can assert that import rises shellfish stock. Then, we have looked for logical contradiction, that is relations between two similar concepts with the same direction but with an opposite sign. A few emerged and almost all of them could be explained by:

- different time-frame considerations,

- different physical or biological underlying processes.

These seemingly contradictory relations were therefore not retained as evidence of opposite points of view between fishers.

In a second time, we searched for significant similarity between causal maps.

Many classical comparison approaches [Markóczy and Goldberg 1995] were not appropriate because they rely on specific data sampling rules, or require exogenous information (not available for this study). The retained measure is inspired by [Lin 1998] with a formula relying on information content (IC). The general similarity between any two sets $A$ and $B$, noted $\operatorname{sim}(A, B)$, is computed as follows:

$$
\operatorname{sim}(A, B)=\frac{2 \times I C(A \cap B)}{I C(A)+I C(B)}
$$

Figure 5 gives an example of the computation detailed below.

- The information content of a single causal map $A$, noted $I C(A)$, can be computed as the cardinality of its own concepts $\left|\left\{C_{A}\right\}\right|$ and relations $\left|\left\{R_{A}\right\}\right|$, that is the sum of its number of concepts and number of relations: $I C(A)=\left|\left\{C_{A}\right\}\right|+\left|\left\{R_{A}\right\}\right|$
- The $A \cap B$ part reflects how often the two fishers responsible for drawing causal maps $A$ and $B$, are talking about the same subjects, and to what extent their views are similar on these subjects. When comparing two causal maps, the common part includes the commun concepts and the commun relations, for which the following rules were retained:

1. Two similar relations $(S R)$ have the same direction and the same sign (similar view).
2. Two opposed relations $(O R)$ have the same direction but opposite signs (opposite view).
3. Two relations between the same concepts but having opposite directions are unrelated.

Thus, $I C(A \cap B)$ is the number of commun concepts and relations between $A$ and $B$ minus the number of opposite relations.

Therefore, between two causal maps $A$ and $B$ :

$$
\operatorname{sim}(A, B)=\frac{2 \times\left(\left|\left\{C_{A B}\right\}\right|+\left|\left\{S R_{A B}\right\}\right|-\left|\left\{O R_{A B}\right\}\right|\right)}{\left|\left\{C_{A}\right\}\right|+\left|\left\{R_{A}\right\}\right|+\left|\left\{C_{B}\right\}\right|+\left|\left\{R_{B}\right\}\right|}
$$

![img-4.jpeg](img-4.jpeg)

Figure 5: Example of similarity computation between map A of size 5 (3 concepts, 2 relations) and map B of size 9 . They have three commun concepts (control, shellfish catches, shellfish stock), they have two similar relations (control $->$ shellfish catches, shellfish catches $->$ shellfish stock) and no opposed relation. Therefore $\operatorname{sim}(A, B)=2 *(3+2-0) /(5+9)=0.71$.

The similarities between all causal maps have been computed, to show typically small similarity values. It does not mean that fishers disagree: without contradiction, it shows that they just have different concerns.

# 3.4 Automatic clustering of causal maps 

Once a similarity metric is available, we can build a distance matrix, and try an automatic clustering of causal maps, in order to search for any regroupements in our sample.

We were able to use the $k$-medoids algorithm to automatically build clusters [Kaufman and Rousseeuw 1990]. This algorithm ${ }^{1}$ constructs a given number of clusters $(K)$, by using only the original similarity (or distance) matrix and, unlike $k$-means, without making assumption about it. It relies on the notion of "medoid", which is:

- a cluster's member (here a causal map),
- the closest neighbor to all clusters' members.

For a given number of clusters, all possible combinations of members are built. From them, is kept the one that displays the minimal sum of intracluster cumulated distances. K-medoids clustering was tried for k between 2 and 5 (i.e. tried with 2 to 5 clusters). None of these attempts gave clear results, isolation between clusters was poor: showing important clusters overlaping. Moreover, we tried to compare the obtained clusters with exogenous modal variables about fishers (age, home harbor, involvement in the fisheries management...). But we failed to find evidence of correlation (chi-squared statistical tests failed).

Hence, scallop dredgers own a consistent view of their business and environment. There is no apparent cleavage among them. Therefore a single causal map can be proposed to summarize their general views.

# 3.5 Maps synthesis 

Once we have decided to draw a single synthetized map, we still have to define what a synthesis is. The most simple synthesis may be:

- the sum, that is the sum of all concepts and relations, even if they are contradictory;
- the majority, obtained from the sum by applying threshold on occurrences of concepts or relations;
- the consensus, containing elements shared by all.

The amount of information in the sum contradicts the simplicity of the graphical formalism, while the consensus is meaningless because empty.

As stated by [Le Dorze et al. 2012] the synthetized map can ben seen as an agreement between fishers while offering a readable aggregation of

[^0]
[^0]:    ${ }^{1}$ Easily available through free statistical computing software $[\mathrm{R}]$.

![img-5.jpeg](img-5.jpeg)

Figure 6: Synthesis map displaying fishers' majority points of view.
information. Sticking to this definition, we choose to work with the simple majority only applied to relations (but relations rely on pairs of concepts).

Having no contradiction between causal maps, it was easy to obtain a sum. Slightly different concepts, such as "starfish" and "predators shell" were merged. Every similar relations were then pooled (and associated with their mean influence degrees). With 17 causal maps, the retained majority threshold was 8 , which was applied to filter the merged causal relations (figure 6). This synthesis was validated by further exchange with fishers and the fisheries board.

As presented in [Le Dorze et al. 2014], more elaborate merging methods exist, making use of preferences or explicit priorities between map makers.

# 3.6 Building a bayesian network 

As we construct the BCM from a cognitive map, its structure corresponds to the structure of the CM with some modifications in order to obtain a directed acyclic graph. [Shenoy and Nadkarni 2001] proposed a procedure to obtain the structure of the BCM from a cognitive map, particularly regarding the following points:

1. Conditional independence: In a CM, the existence of a relation between two variables induces that these variables are dependent. However, the absence of a relation between two variables does not imply independence (i.e., lack of dependence) between both these variables. In bayesian network (BN), the absence of a relation between variables implies that these variables are conditionally independent. Thus, causal relations should not be removed even if they seem redundant and increase the complexity (even if they can be easily obtained using transitivity).
2. Circular relations: Contrary to BNs that are acyclic graphs (tree like), CMs usually contain circular relations, depicting feedbacks for example. In these cases, the circular relations represent dynamic relations between variables over time. In such cases, the solution consists in separating the variables into two different time frames [Sucheta et al. 2004]. Namely, some relations in the cycle (or loop) belong to the present time frame while others belong to a future time frame.

Removing circular relations may require arbitrary choices. On the synthesis map (figure 6) three loops can be identified:

- a short feedback on shellfish stock: more spawners and hence more juveniles.
- another feedback on shellfish stock, through shellfish catches: a higher stock allows larger catches, but higher catches obviously reduce the stock.
- a long feedback on shellfish stock, through number of fishers and shellfish catches: larger catches make room for more fishers.

Obviously, the shellfish stock is an essential variable. Moreover, disjointing it on a time basis removes all feedbacks. But one could argue that shellfish

![img-6.jpeg](img-6.jpeg)

Figure 7: Proposed tree structure for the BCM. The removal of the feedback on shellfish stock led to the creation of two new concepts, representing the temporal dynamic of the stock : from initial shellfish stock to final shellfish stock.
catches are more valuable for fishers. Clearly, stating what is the target variable will determine the tree structure. In our case, the evolution of shellfish stock was the most important result the stakeholders were expecting, which led us to Figure 7.

The proposed tree structure enables us to follow the evolution of shellfish stocks from an initial state to a final state. This evolution responds to all inputs: predation, hatchery policy, quotas...

# 3.7 Computing combined probability tables 

Once defined the structure of the BCM, we must build the conditional probabilities tables (CPT) associated for each variable. In [Sucheta et al. 2004], the authors ask experts about the elicitation of the CPTs. We propose, as in [Sedki and Bonneau 2012], to take advantage of the causal values given in the CM to compute the conditional probabilities. But because we need to enable stable models (in fact the depicted system has been steady since the Tinduff hatchery opened in the late 90' and an annual planting system was introduced) we have enriched the original proposal. Stability implies that:

- each variable can be in a stable state,
- some variables may not leave a stable state easily.

Figure 8 illustrates the need for explicite inertia modelling, that can be stated as follows: when dealing with one relation among many important ones, and when this relation has a limited influence, it cannot lead to a certain change alone.
![img-7.jpeg](img-7.jpeg)

Figure 8: Market price receives a single, and of little importance, incoming relation. It might not be enough to ensure a change of its state, because other non elicited relations might exist (omitted for the sake of simplicity, or simply forgotten). Shellfish catches receives many incoming relations: in order to lead to a change of its state (with at least $P>0.5$ ), the cumulated influences has to reach a minimum threshold, called "inertia".

We therefore wish to ensure that:

- conflicting influences may lead to stability
- a single weak influence will not be enough to escape stability

The probability computation responds to the following constraints:

- The semantic of the causal values should be preserved. For example, the positive effect of number of fishers ( $N F$ in the following formula) on shellfish catches $(S C)$ is greater than the negative one of shellfish imports $(S I)$, implying that:

$$
P(S C=+|N F=+)>P(S C=-|S I=+)
$$

- The probability theory requires that:

$$
P(-)+P(\sim)+P(+)=1
$$

Variable without parents must be assigned on an a-priori basis. This has no impact on the inference process since regarding theses variables, we can introduce any desired observation (that is, we can assign a specific state to each variable). For the others, the procedure is described below.

Let $X$ be a variable for which we compute the CPT and let $Y_{i}$ be the parents of $X$. For a given combination of the $Y_{i}$ states, $E_{-}$is the sum of the negative effects, $E_{+}$is the sum of the positive effects. $E_{-}$and $E_{+}$are absolute values and can be seen as "influence degrees".

Considering what we have called "inertia" $(I)$, the Table 2 subsumes the single parent case $(Y->X)$.

Where a given variable $V$ has multiple parents, two opposite effects of the same strength will cancel each other. When these two effects are of different strength, only the part $E_{\sim}=\min \left(E_{+}, E_{-}\right)$will be cancelled, but still contributing to the stability of $V$. Moreover, the normalisation value is now $N=\max \left(I, E_{-}+E_{+}\right)$, which ensures stability when $E_{-}+E_{+}$is small (when only a small part of all potentially received influence is at work).

Therefore, for each possible combination of parent's states:

$$
\left\{\begin{array}{l}
P(X=+)=\left(E_{+}-E_{\sim}\right) / N \\
P(X=-)=\left(E_{-}-E_{\sim}\right) / N \\
P(X=\sim)=1-P(X=+)-P(X=-)
\end{array}\right.
$$


Table 2: Computed conditional probabilities in the three cases of a single parent relation, with inertia $I$ equal to the highest influence degree: $I=$ $\max \left(\left|E_{-}\right|,\left|E_{+}\right|\right)$.

This formula leads to the same values as the example given in Table 1 above. For example, with $I=3$, if the number of fishers rises while shellfish imports decreases, we have $E_{+}=2$ and $E_{-}=1$, Therefore $E_{\sim}=1$ and $N=3$. The resulting conditional probabilities would be:

$$
\left\{\begin{array}{l}
P(S C=+ \mid F N=+, S I=-)=1 / 3 \\
P(S C=- \mid F N=+, S I=-)=0 \\
P(S C=\sim \mid F N=+, S I=-)=2 / 3
\end{array}\right.
$$

# 3.8 Assessing probabilities for input variables 

Default probability values for input variables have been set using independant expert knowledge. However:

- for deductive reasoning purposes or scenarios testing, these probabilities will be replaced by observations (one of the possible states will be associated with a 1.00 probability value, all the others to 0.00 ),
- for abductive reasoning, default values have litle interest and equiprobability can be used.


## 4 Results

### 4.1 An homogeneous population

When looking at the Cognitive Maps, the major preoccupation (Figure 10) is clearly the importance of the hatchery, without distinction of age or home harbor among fishers.

![img-8.jpeg](img-8.jpeg)

Figure 9: Resulting bayesian network built using Netica, from Norsys Software [Netica]. The provided Java API was used in order to automatically build the combined probability tables. In this example, a stability assumption is made in order to set the probability values associated to each states of input variables.

# 4.2 Scenarios testing 

The objective of building the BCM remains:

- to evaluate the fishing activities by analyzing the state of some variables (for example the shellfish stocks) regarding observations about some facts or input variables (ASP, imports, etc.).
- to diagnose causes given an effect.

For example, what are the factors that may cause a decrease in number of fishers? (abductive reasoning)

We have devised a simple scenario (Figure 11): how can the shellfish stock increase, given that predation and licence number are steady. Such a scenario is obtained, from the bayesian network, by making some observations, that is by giving a $p=100 \%$ to the desired states. The probabilities of the all the other variables are then updated by propagation in the BCM.

Given a stable predation and number of fishing licence, how do we explain a rise of shellfish stock? Here, the most probable explanation should be that a rise of shellfish imports inducing a drop in the market price finally leads to a decline of shellfish catches.

![img-9.jpeg](img-9.jpeg)

Figure 10: Major preoccupations expressed by interviewed fishers. The hatchery comes first with 13 hits out of 17 .

# 4.3 Validation 

Usual models validation cover either the validation of the model by itself and output checking. Synthetized map and bayesian network were validated by stakeholders (but for obvious reasons, this validation applies more to the causal structure than to the conditional probability tables).

In a second time, different observations regarding input variables were applied to the model, in order to test it against qualitative knowledge given by all our experts ( 17 dredgers and 2 experts in biology of scallops). No contradiction was detected.

At last, the model sticks to historical scenarios for which outcomes are know.

We conclude that the proposed method looks efficient, and allows to easily analyze and understand the impact of the different variables.

![img-10.jpeg](img-10.jpeg)

Figure 11: With stable predation and licence number, how can be explained an increase in shellfish stock? The most probable explanation is a shellfish imports increase, leading to a market price decrease and therefore lower shellfish catches.

# 5 Discussion 

### 5.1 Related work

As noted in [Özesmi 2004], the use of expert systems is increasing in ecological modeling, either statistical, empirical or mechanistic models. Qualitative approaches have the advantage of being robust to data poor situations, and in many way are more flexible: no restriction on the number of experts, parameters of concepts, no required paramaters estimation. But it is important to state that the proposed method is not to be considered as a substitute. It is a complement to numerical approaches, and a needed tool when these models are not designed or serviceable for use by policy-makers [Kouwen et al. 2008].

Different technical approaches aim at working with stakeholders, albeit with a very broad spectrum of tools: from generic approach like agent-based modelling (be it a role-playing game or a computerized platform), to very specific or proprietary langages and systems like Stella ${ }^{\circledR}$ software. When requiering an active stakeholders' involvement, they are branded "participatory modelling" [Voinov and Bousquet 2010]. These works often aim at promoting communication and learning between agents, for example by link-

ing stakeholders and modellers in scenario studies [Vliet et al. 2010], not necessarily to provide inference tools: for many, the focus is on the process rather than on the product [Voinov and Bousquet 2010].

As a whole, it has been noted that these methods usually produce decisions of high technical quality, while also educating the public, eliciting public values, resolving conflict, and building trust in agencies [Beierle 2002].

Some have shown successful use of bayesian networks as a tool of public participatory modelling for management purpose [Henriksen et al. 2007]. But the authors insist on the need to adequately train the stakeholders (regarding probability theory) which is deemed unnecessary with our method.

Finally, a similar approach to ours can be found in [Kouwen et al. 2008], where qualitative bayesian networks are built, in which inference is enabled thanks to sign-propagation algorithms. But unfortunatly, sign propagation does not solve the problem of ambiguity in qualitative diagrams.

# 5.2 Tedious sampling and lexical modelling process 

The proposed sampling method requires an active participation of interviewed people. It might prove to be beyond their capabilities (too long or too formal). However, in some cases, it can be a by-product of a wider sampling process.

The interviewer can draw the cognitive maps by himself, from the answers he gets, or from his own observations. In a second time only, he can ask the interviewed people for a validation of their maps. The easily understandable formalism of cognitive mapping enables a smooth post-validation.

An ontology, comprising at least all the concepts (or variables) must be available. Creating it from scratch might be a tedious work. However, ontological modelling can be avoided or simplified:

- some comparable studies relies on rewritten cognitive maps using a restricted lexical field [Prigent et al. 2008], implying an easier task,
- suitable ontologies might be readily available, for example through the Agricultural Information Management Standards program of the FAO $[\mathrm{FAO}]$,
- a huge progress has been made in automatical ontological models' building, as shown in this experiment [Küçüka and Arslan 2014],

- direct similarity assesment methods have been proposed too, using huge corpus, namely Google [Cilibrasi and Vitányi 2007] or Wikipedia [Gabrilovich and Markovitch 2007].


# 5.3 Tricky merging in a wider community 

How to handle a less homogeneous population? How should conflicts between points of views be handled ? In our view this is the main setback of our approach.

Keeping all the originally expressed knowledge would be a very desirable feature. Belief functions, as defined by [Smet 1993], could be used to handle the associated uncertainties. However this has not been tried in the field so far, because of the much higher resulting combinatory and the lack of associated widespread inference software.

### 5.4 Subjective bayesian structure

Because environnemental issues carry a lot a feedbacks, multiple loops in the cognitive map might lead to combinatory difficulties when removing them, in order to build the bayesian network structure. In the other hand, removing loops remains the only way to enable decision making: the time frame becomes explicit (albeit symbolic, in a before / after representation). Therefore removing the indecision that plagues all efforts of qualitative reasoning on looped cognitive maps.
![img-11.jpeg](img-11.jpeg)

Figure 12: Qualitative reasoning trap, on a looped cognitive map: given a initial rise of number of fishers, without an explicit time frame, the changes in shellfish stocks cannot be predicted.

### 5.5 Accuracy and uncertainty

Finally, our approach does not provide accuracy nor uncertainty statements regarding predictions. We understand that it might be a desirable feature,

and that stakeholders might ask for confidence assesments. But this seems an unreachable goal without explicit rating of fishers reliability, and without contradiction in their statements.

Furthermore, if bayesian networks enable uncertainty modeling within variables' states, they do not in the causal structure itself, which is by nature deterministic. However, the probabilistic predictions offered here might help to give a realistic estimate of the chances of achieving desired outcomes [Borsuk et al 2003].

Because they efficiently apprehend the interactions between management actions and simple ecological responses, qualitative reasoning techniques started being advocated for dealing with ecological issues in the 1990s. The model we propose is not intended to predict future evolutions of the system : many potentially relevant aspects are not modelled either because they are unknown for the fishers or because they considered that they have no leverage on it (one can think of other possible uses of the bay, sewage and industrial wastes...). Nevertheless, it answers what is commonly expected from decision-support systems as described by [Zitec et al. 2009].

# 6 Conclusions 

Building causal maps from field experts' knowledge has now a long history. However, solving a given decision problem using causal maps is not straightforward. Bayesian networks are a well established method and they offer efficient algorithms for applying inferences. Many tools are readily available. But building bayesian networks requires a lot of expert knowledge and judgements to determine the variables of the problem and influences between theses variables. Moreover, it requires this knowledge in a very formal approach. Therefore, we proposed using a causal map to construct the model and set the conditional probabilities. Once the common causal map (CM) built we can transform it into a BCM which combines causal modeling techniques and bayesian probability theory.

The structure of the obtained BCM is derived from the CM with some modification regarding feedbacks (circular relation). The parameters of the BCM are obtained from the associated causal values in the CM.

We illustrated the proposed approach on a real decision problem which concerns the analysis of shellfish dredging in the rade de Brest. We conclude that using cognitive maps gives access to the raw perception of fishers and

that the BCM allows to analyze it and offers a simple management tool. Moreover, the graphic nature of the two used formalism enables an easy involvement of stakeholders.

A future work concerns the suppression of the first step that leads to the CM by fusion of individual cognitive maps and therefore leads to an impoverishment of the model.

# Acknowledgement 

This study was funded but the French Liteau program and was led in collaboration with Brest's LETG-Géomer laboratory [Gourmelon et al. 2013]. We also are grateful to G. Christiansen, and to all fishers and biologists, who contributed to this study.
