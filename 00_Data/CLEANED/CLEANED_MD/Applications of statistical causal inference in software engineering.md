# Applications of statistical causal inference in software engineering. 

Julien Siebert ${ }^{a}$<br>${ }^{a}$ Data Science Department, Fraunhofer Institute for Experimental Software Engineering (IESE), Fraunhofer Platz 1, 67663 Kaiserslautern, Rhineland-Palatinate, Germany


#### Abstract

Context: The aim of statistical causal inference (SCI) methods is to estimate causal effects from observational data (i.e., when randomized controlled trials are not possible). In this context, Pearl's framework based on causal graphical models is an approach that has recently gained popularity and allows for explicit reasoning about issues related to spurious correlations. Objectives: Our primary goal is to understand to which extend and how Pearl's graphical framework is applied in software engineering (SE). Methods: We performed a systematic mapping study and analysed a total of 25 papers published between 2010 and 2022. Results: Our results show that the application of Pearl's SCI framework in SE is relatively recent and that the corresponding research community is fragmented. Most of the selected papers focus on software quality analysis. There is no clear and widespread community of practice (yet) on how to implement and evaluate SCI in SE. Conclusions: To the best of our knowledge this is the first time such a mapping study is done. We believe that SE practitioners might benefit from such a work, as it both provides an overview of the work and people involved in the application of causal inference methods, but also outlines the potential and limitations of such approaches.


Keywords: Causal Inference, Software Engineering, Causality, Graphical Causal Model

# 1. Introduction 

Empirical software engineering aims at studying and evaluating how people engineer software with the help of empirical research methods. This paper focuses on the application of one type of empirical methods, namely statistical causal inference (SCI, see section 2). Such methods have their roots in a number of applied fields (from AI to econometrics) and aim to provide a framework for making valid inferences about causal effects based on interventional or observational data. More specifically, we focus on SCI methods that use graphical models as developed by Pearl and colleagues [1, 2]. This framework has been shown to be equivalent of the potential-outcomes framework (also called the Neyman-Rubin Causal Model [3]) but enriches it by making use of an explicit causal structure called a graphical causal model. Making assumptions about causal effects explicit through a graphical structure has several advantages. First, it helps determine whether causal effects can be estimated and how they might be estimated (see section 2). It helps to find out whether an analysis might suffer from problems such as confounder or collider bias $[4,5,6]$. Finally, the hypotheses represented in the graphical causal model are amenable to falsification because they imply a certain set of independencies that can be tested in the data [2].

In short, causal graphical models can be seen as a basic building block of causal inference. However, they are relatively new compared to the potential outcomes framework, and methods for estimating causal effects from observational data that do not explicitly rely on a causal graphical model (such as matching, difference-in-differences, instrumental variables, or regression discontinuity, see $[7,8]$ ) existed long before the theory behind causal graphical models was invented. Furthermore, depending on the system under study, it may be difficult to obtain a sufficiently detailed causal graphical model: some influencing factors may not be directly measurable and only available through proxy data, or may even be unknown. A typical example in SE would be aspects such as "developer experience" or "effort and time to develop a given feature" [9].

The goal of this paper is to understand whether, how and by whom Pearl's framework for causal inference is applied in software engineering (SE) (see section 4 for the detailed research questions). We hope to provide an overview of the field that helps evaluating the potential and limitations of these SCI methods for SE. For that, we performed a literature survey following the guidelines from Kitchenham and Charters [10], and Wohlin [11]. We analysed

a total of 25 papers. To the best of our knowledge, this is the first time such a mapping study is done.

This paper is structured as follows. Section 2 provides a short introduction to SCI methodology. Section 3 provides a short analysis of the related work. Section 4 presents our search methodology, section 5 our analysis and section 6 our results. We discuss and conclude our work in both sections 7 and 8 .

# 2. Definitions 

### 2.1. Statistical Causal Inference (SCI)

Statistical causal inference focuses on estimating actual causal effects of an action (a treatment $T$ ) on a given observed system (an outcome $Y$ ) from data $[1,12,3]$. In general, the gold standard for estimating a causal effect is to perform randomized controlled trials in which the potential confounders ${ }^{1}$ are controlled for, through, e.g., randomization, so that their effects are balanced between the experimental and the control groups and that only the treatment differs between groups. However, when this is not feasible (e.g., for practicable or ethical reasons), causal effects have to be estimated from observational data (i.e., data that was not generated during randomized controlled trials). The fundamental problem with observational data is that we cannot have the same subject being treated and not being treated at the same time (following Pearl's notation and assuming a binary treatment, we cannot observe $P(Y \mid \operatorname{do}(T=0))$ and $P(Y \mid \operatorname{do}(T=1))$ at the same time) and the effect has to be estimated from available data (i.e., from $P(Y \mid T=0)$ and $P(Y \mid T=1))$. The challenge with observational data, assuming that all relevant variables have been captured, is that it can contain correlations induced by confounding factors that can bias the estimation of causal effects (see figure 2). For this reason, researchers in the field of statistical causal inference have developed methods to reduce the impact of confounding factors and separate spurious correlations from causal effects $[7,8]$. One of such approach is the use of graphical causal models together with the application of the do-calculus by Pearl et al. $[1,2]$.

[^0]
[^0]:    ${ }^{1} \mathrm{~A}$ confounder is a variable that both have an impact on the treatment and the outcome of interest. See figure 2.

# 2.2. Graphical causal models 

Graphical causal models are a way to represent hypotheses about causality in a given system. They take the form of a graph ${ }^{2}$ consisting of nodes representing the relevant variables (potentially measurable) and links representing a direct causal effect between two variables. For example, if a treatment $T$ is supposed to have a causal effect on an outcome $Y$, then both $T$ and $Y$ are represented as nodes and a link goes from $T$ and points towards $Y$. Variables can be either endogenous (they belong to the system under study) or exogenous (they are outside the system). Observed effects are usually represented by solid lines, while unobserved effects are represented by dashed lines. Figure 1 illustrates a simple example of a graphical causal model. Graphical models are interesting for different reasons. First, they make hypotheses about variables under study and their causal effects explicit. Second, they are used for identifying structures that lead to spurious correlations and need to be handled before estimation. Third, causal graphical models can be used as a visualization help to understand in which case other SCI methods (such as propensity score matching, difference-indifference, instrumental variables, etc.) are applicable (see section 2.5).
![img-0.jpeg](img-0.jpeg)

Figure 1: Example of a graphical causal model representation where a treatment $T$ causes an outcome $Y . T$ and $Y$ are endogenous variables. $U_{T}$ and $U_{Y}$ are exogenous variables (e.g., external noise).

### 2.3. Pearlian statistical causal inference methodology

The methodological process behind Pearl's SCI consists of three major steps: modeling, identification, estimation ${ }^{3}$. The first step (modeling) is

[^0]
[^0]:    ${ }^{2}$ Causal graphs are by definition directed acyclic graph and are sometimes referred to (causal) DAG.
    ${ }^{3}$ Pearl and Mackenzie introduced a 9 steps process (see Figure 1 in [2]). Sharma and Kiciman proposed 4 steps in [13]. Both resolve around the three steps mentioned above but introduce some more details and testing methods that are out of this paper's scope. For the sake of simplicity, we just introduce the three steps of modeling, identification and estimation.

to make causal assumptions explicit through the use of a graphical causal model. This causal model can either be obtained through domain expertise or extracted from data. In the latter case, the term "causal structure discovery" or "causal structure learning" is used (see $[14,15]$ ).

The second step (identification) is to find out whether a given causal effect can be estimated using the available data. The idea is to find out whether there are paths in the graph where a variable can influence both the treatment and the outcome of interest. These are called backdoor paths and are sources of spurious correlations if left "open" (see figure 2 for a visual example of how a backdoor path can be closed). Identifying such path requires identifying structures such as confounders, mediators, or colliders to understand which variable(s) should be controlled for [5]. Identification outputs an estimand for the causal effect under study. The main tool for causal identification is the do-calculus developed by Pearl and colleagues [16].

The third step (estimation) is to effectively estimate the identified causal effect based on the available data and the previously gained knowledge of which variables should be adjusted for. Estimation can be done using a variety of methods, from simple linear regression to more complex approaches such as T-learner, X-learner, double machine learning or causal random forests ${ }^{4}$.

Like any other analytical method, SCI based on a causal graphical model relies on certain assumptions. First, the graph should include all relevant influencing factors (measurable or not) for the problem at hand, as unknown confounders could make the analysis unreliable (this is called the unconfoundedness assumption). Second, the statistical properties implied by the graph (such as conditional independence) should represent those that exist in reality (this is called the Markov assumption). This means that the conditional independencies implied by the graph can be tested in the available data, making the causal graph amenable to falsification. Different assumptions also need to be considered in estimation methods. For example, the stable unit treatment value assumption (SUTVA) states that the outcome of a given unit should not change due to the treatment of other units. The positivity assumption states that for a given subgroup both treated and untreated individuals should be present [17, 3]. Finally, several tests have been

[^0]
[^0]:    ${ }^{4}$ The interested reader may wish to refer to Chapter 7 in [17] for an overview of estimation methods

proposed for refuting causal estimates, like placebo test (see [13]).
![img-1.jpeg](img-1.jpeg)

Figure 2: Graphical representation of a backdoor path where $C$ is a confounder that infuences both treatment $T$ and outcome $Y$. The backdoor path is $T \leftarrow C \rightarrow Y$. Estimating the effect of $T$ on $Y$ requires to "close" the backdoor. In the present case it can be done by adjusting for $C$. Following Pearl's notation and assuming that $T$ is binary, the causal effect of $T$ on $Y$ is written $P(Y=y \mid \operatorname{do}(T=0))-P(Y=y \mid \operatorname{do}(T=1))$. The do operator represents the fact that we intervene on the system by setting $T$ to a specific value. Adjusting for $C$ implies $P(Y=y \mid \operatorname{do}(T=0))=\Sigma_{c} P(Y=y \mid T=0, C=c) P(C=c)$ and $P(Y=y \mid \operatorname{do}(T=1))=\Sigma_{c} P(Y=y \mid T=1, C=c) P(C=c)$. The absence of do operators on the right-hand side of the equations tells us that we can estimate the causal effect from observational data alone: $P(Y=y \mid \operatorname{do}(T=0))-P(Y=y \mid \operatorname{do}(T=1))=\Sigma_{c} P(Y=y \mid T=$ $0, C=c) P(C=c)-\Sigma_{c} P(Y=y \mid T=1, C=c) P(C=c)$.

# 2.4. Relation to Bayesian networks and structural equation models 

The focus of this paper is on causal inference methods using graphical causal models, therefore it is necessary to sketch the distinction between these models and others like structural equations models and Bayesian networks.

The graphical models in SCI are indeed are very similar to Bayesian networks, with the constraints that an arrow represents a direct causal effect, and that no arrow implies that no direct causal effect exists between variables. The main difference lies in the inference process. While Bayesian networks allow for probabilistic inference and prediction based on correlations, causal inference requires an additional step, namely identification. As stated before, the identification step is to find out whether a given causal effect can be estimated using the available data and tells us which variable should be controlled for (see examples of good and bad controls in [5]).

Another type of graphical models are structural equation models (SEM), which represent cause and effects as equations. They sometimes use a specific symbol $:=$ to explicitly state that a variable is the cause of another one (for example $Y:=f(X)$ means that $X$ is a cause of $Y$ ), and that one cannot simply reverse the equation (e.g., $Y:=f(X)$ does not mean $X:=f^{-1}(Y)$ ). These models provide a functional form of the effect (e.g., linear, non-linear). In comparison, graphical causal models do not provide any functional form of

the effect (they are also called non-parametric). As such, structural equation models can be viewed as a subclass of graphical causal models, which in turn are themselves a subclass of Bayesian networks.

# 2.5. Other methods not explicitly based on a causal graphical model 

The use of causal graphical models is relatively recent (see Pearl's historical perspective in [2]), and the do-calculus can be seen as a theoretical cornerstone that allows for systematic reasoning about association and causal flows [5]. However, for some application cases, it may be difficult to obtain a sufficiently detailed graphical causal model for the do-calculus to be effective in providing a causal effect estimand. There are many causal inference methods that do not explicitly rely on the modelling, identification, estimation phases mentioned above. Some methods either compare treated and untreated individuals who are assumed to be similar except for treatment (such as matching or regression discontinuity), or modify their variables to make them more similar (like re-weighting methods). Other methods, such as event studies, difference-in-differences or synthetic control, attempt to model the counterfactual (i.e. what would have been the behaviour of the treated group if no treatment had been given) and measure the difference between reality and the assumed counterfactual. Finally, some methods, such as instrumental variables, work well for specific causal structures (see figure 3). In all cases, a causal graphical model helps understand when the method applies and whether the underlying assumption of a method still holds for a given application case (see how recent textbooks on causal inference make use of the causal graph to explain the assumptions behind estimations methods $[7,12,8])$.
![img-2.jpeg](img-2.jpeg)

Figure 3: Typical causal graph assumed by the instrumental variables estimation method. $C$ is an unobserved confounder. $I V$ is the instrumental variable. Note that for this method to work, there must be no open backdoor from $I V$ to $Y$.

# 3. Related Work 

### 3.1. Generic causal inference surveys

While technical SCI surveys typically focus on technical aspects (such as issues related to the type of data, like time-series [18] or geospatial data [19]) and are usually domain agnostic, they can provide insight into application domains and their corresponding use cases. For example, $[3,18]$ discusses the potential of SCI methods for specific application domains along with related research and lists benchmark datasets. Software engineering is not treated directly as an application domain in these papers. Furthermore only two benchmark data sets are related to software engineering and consist of social media usage (Blogger and Flickr). In both reviews [3, 20], the authors discuss applications of SCI that are relevant to the engineering of data-driven software components (SE4ML/SE4AI): fairness and explainability, or for improving machine learning in general (see also [21, 22]).

### 3.2. Reviews of SCI in other domains

Domain-specific surveys can provide information about the benefits and applicability of SCI methods within a particular domain. In [23], the authors discuss the use of graphical causal models for survey research and how these tools can shed light on issues such as selection bias and help to question current practice. In [24, 25, 26], the authors discuss the application of SCI in the medical field. While they also mention the mitigation of selection bias as one aspect where graphical models can help, they also mention the mitigation of spurious correlation as a major advantage of relying on SCI methods over correlational ones (this is also mentioned in other domains, see $[27,28])$. A canonical example of a spurious correlation reported in this field comes from experiments attempting to predict the likelihood of death from pneumonia using historical medical records. Counterintuitively, the analyses found that asthma lowered the risk of death, even though it is known to be a severe condition in people with pneumonia. This misleading effect occurred because the patients with asthma in the training data set were treated more drastically than other patients. This level of care is a confounding factor that, if not taken into account, could lead to the wrong decision [26, 29]. These reviews mention the other advantages, such as dealing with data drift or explainability [24, 25]. The arguments provided are consistent with those mentioned in the articles in the previous section. Finally, these domainspecific reviews highlight the challenges in applying SCI. Specifically for those

relating to graphical causal models, the main problem is to obtain such a graph. Another challenge mentioned is that SCI is not part of the traditional curricula in these fields.

# 3.3. Causal inference in Software Engineering 

It is not the first time that the application of a given analysis method in SE is reviewed. The application of Bayesian networks in SE is relatively well established. For example, de Sousa et al. [30] performed a mapping study in which they analysed 109 publications (from 1999 to 2018) focused on the application of Bayesian networks for software project management. Another mapping study was done by Misirli and Bener [31] with a focus on software quality prediction. Other systematic literature reviews and comparative analyses have also been performed [32, 33, 34]. However, none of these papers mention SCI as defined in section 2.

The work by Wong [35] focuses on challenges related to developing software for causal inference (which the author called "computational causal inference"). The focus is symmetrical to that of the current paper, in that Wong focuses on the application of SE for SCI, whereas we focus on the application of SCI for SE.

To the best of our knowledge, there is no similar review like ours. The closest we could find is an extensive related work section in [36] that refers to several papers using SCI in software testing but does not attempt to organize nor analyse them.

## 4. Methodology

### 4.1. Frame

### 4.1.1. Research questions

Our primary goal in this paper was to identify applications of SCI methods (as defined in section 2) in SE and to understand how these methods are used. We refined this goal into specific questions listed in table 1. We particularly focused on an analysis of the existing literature to answer our research questions. Table 3 lists the information, we extracted from the papers. Table 2 provides the detailed exclusion criteria. Note that we did not limit our literature search by date. However, as the do-calculus was only invented around 1995 [16], we did not expect to find any relevant paper before 2005 and would not have included any paper prior to 1995.


Table 1: Research Questions.


Table 2: Exclusion criteria.

# 4.1.2. Exclusion criteria 

### 4.1.3. Extracted information

To answer our research questions, we first extracted demographics like authors name, affiliation and type of publication. This helps learning about the structure of the research community using SCI in SE (RQ2). We extracted information about the SE use cases (RQ1). To answer RQ3 and RQ4, we extracted information about the SCI methods, the data sets and the libraries used. Finally, we extracted information about the evaluation of the results (RQ5). Table 3 provides an overview of the information collected.

### 4.2. Search and selection process

There are mainly two difficulties here. First, SE is a large field and filtering relevant papers (i.e., use cases that belong or do not to SE) can be challenging. For this, we relied upon categories of activities defined in the $\mathrm{SWEBOK}^{6}$. Second, SCI methods are relatively new and, in general, may be less well known than statistical data analysis methods. In addition,

[^0]
[^0]:    ${ }^{6}$ http://swebokwiki.org/Main_Page


Table 3: Information extracted.
graphical causal models are close relatives of Bayesian networks and methods such as the do-calculus could have been applied without direct reference to the generic term "causal inference".

The search process and selection followed four main steps: 1) establishing a set of seed documents, 2) consolidating a search query, 3) extending the query results with a snowballing phase, and 4) selecting the final set of relevant papers (see Figure 4). For the first three steps, the selection was done based on title and abstract screening. In the last step, the selection was done after full-read.
![img-3.jpeg](img-3.jpeg)

Figure 4: Search process overview.

# 4.2.1. Seed documents 

We started our search with a relatively simple query in Scopus ${ }^{7}$ completed with a snowballing phase (both backward and forward) in order to find

[^0]
[^0]:    ${ }^{7}$ https://www.scopus.com

a first set of seed papers. The following query: TITLE-ABS-KEY((\{causal inference\} OR \{causal discovery\} OR \{structure learning\}) AND (\{SE\})) was performed on 26.04.2022 and resulted in 42 documents among which 11 were judged relevant (after title and abstract screening).

A forward and backward snowballing pass was done on these first 11 documents. This led to 19 new relevant papers for a total of 30 seed papers.

These 30 articles were used, on the one hand, as seed articles (i.e., to test whether subsequent search queries would include these articles) and, on the other hand, to gather information about how researchers in the field of SE describe SCI and find interesting search terms that helped us find more relevant articles.

# 4.2.2. Search query 

In the next phase, we created a search query that would include our seed papers and return new potentiall relevant papers. We actually created two search queries (see figure 5). The first query looks for papers both mentioning SE and SCI. The second query looks for papers citing the work of Judea Pearl.

First query. As stated above, the first query is structured in two parts. Each part contains relevant keywords for each topic of interest and all keywords are separated by OR. Both parts are separated by AND.

The search for relevant query terms for both parts was done as follows. First, single SE terms were tested in conjunction with "causal inference". The SE terms were chosen both from the SWEBOK and from the seed papers. Then, we checked the number of papers returned by Scopus as well as their relevance to our research questions. The assumption was that the keywords return a higher ratio of relevant papers and that the constraint AND "causal inference" is generic enough to keep most of the relevant papers but focused enough to exclude many irrelevant ones.

A similar approach was taken for determining relevant keywords related to SCI. The chosen terms were taken from reviews and textbooks [37, 1, 17, $12,3]$ and consolidated with a short overview of the vocabulary used in the field of $\mathrm{SCI}^{8}$. Single causal inference terms were tested in conjunction with

[^0]
[^0]:    ${ }^{8}$ Here the author performed a search in Scopus using the query (TITLE("causal inference")) AND ("graph*"), extracted the main authors (i.e., authors having more than 5 documents within this query), extracted related and relevant topics using SciVal https://scival.com/ (Topic T.12463: "Chain Graph; Artificial Intelligence; Condi-

"Software Engineering" (i.e., adding AND "Software Engineering" to the query).

Table A. 8 gives the details of the queries tested and the related hits and relevant papers. The final query was built using the more encompassing terms (i.e., terms that provided more hits and more relevant papers but also included relevant papers from other queries). The final query is shown in figure 5 .

Second query. The second query targeted papers citing Pearl's work and mentioning "Software Engineering" and "causal inference" in their text. Scopus allows for searching through all the papers citing a given authors by using the author's scopus ID ("Pearl, Judea" 7101604154). The query is also shown in Figure 5.

# First query: 

```
TITLE-ABS-KEY( ("software engineering" OR "software test*" OR
"software quality" OR "fault local*" OR "AIOps") AND ("causal
inference" OR "propensity score" OR "counterfact*" OR "inverse
probability" OR "probability weigh*" ))
```


## Second query:

"Pearl, Judea" 7101604154
Refined to [( "causal inference" AND "software engineering" ) ]

Figure 5: Search queries.

### 4.2.3. Snowballing phase

These two queries returned 86 and 119 papers (as of 2022-11-15), out of it, a total of 53 distinct papers were judged relevant based on title and abstract

[^0]
[^0]:    tional Independence", Topic T.1910: "Observational Studies; Causal Inference; Propensity Score", and Topic T.22578: "Principal Stratification; Causal Effect; Outcome"), and finally extracted key phrases from these topics.

screening. These papers were used as seed for snowballing. Backward snowballing was done using Scopus directly. Forward snowballing was done using Google Scholar. Relevance of the papers was judged based upon title and abstract screening. We performed two snowballing phases. First, backward and forward snowballing was done on the first set of 53 papers. This led to 29 new papers (backward: 8, forward: 21). Second, backward and forward snowballing was done on this novel set of 29 papers. The snowballing phases allowed us to collect 95 potentially relevant papers.

After reading the papers completely, we excluded 25 papers. 18 papers were judged out of scope because they were not using SCI as defined in section 2 (EC1). One paper was not written in English (EC5), one paper was describing a software library (EC3), and there were two papers that we didn't have access to (EC4). One paper was a secondary study (a review) (EC7), one paper was a duplicate and one was a companion paper (EC8). This led to a total of 70 papers that we further analysed.

# 4.2.4. Papers categorization and final selection 

During the information extraction phase, we noticed that the articles fell into four distinct categories. The first category (C1), contains papers focusing only on the first step of causal inference (modeling) and do not mention the next two steps (identification and estimation). 22 papers are present in this category (cf. Table B.9). Note that in this category, many papers use the term causal analysis or causal inference when talking about causal structure discovery.

The second category (C2), contains papers focusing on counterfactual analysis (also called counterexamples or causality checking) but not doing causal inference as defined in section 2. Although, they make use of structural equation models (SEM) and the notion of counterfactual as defined by Halpern and Pearl [38], the papers in this category did not use SCI methods (at least none of the paper, we reviewed was mentioning either the different phases of causal inference or specific techniques like do-calculus for identification or specific estimation methods). 16 papers were classified as C2 (cf. Table B.10).

The third category (C3), contains papers doing causal inference without relying upon a graphical model. These papers use techniques (like propensity score matching or double machine learning) to handle confounding bias. Seven papers have been classified as C3 (cf. Table B.11).

The last category (C4), contains papers doing all three steps of causal

inference: modeling, identification, and estimation. 25 papers were classified as C4 (cf. Table B.12).

With regard to our research questions, we decided to exclude categories C1, C2, and C3 from further analysis. The reason is twofold. First, our paper focuses on the application of Pearl's framework for causal inference and the papers in C1, C2, and C3 categories do not entirely fulfill this requirement. Second, our search was primarily designed to find papers from the C4 category, and therefore, we suspect that the papers from categories C1, C2, and C3 are only a subset of what we could have found if we would have directly targeted either causal structure discovery, counterfactual analysis, or causal inference techniques not relying upon a causal graphical model.

# 5. Analysis 

### 5.1. Demographics and bibliometrics

The 25 papers classified in C4 have been written by a total of 60 distinct authors. Out of theses 60 persons, only 11 are listed as authors in more than 2 papers (see figure 6). From the coauthorship network, we obtained 13 distinct coauthors groups (i.e., authors having published together). The largest coauthors group (in terms of papers collected) accounts for 10 papers $[39,40,41,42,43,44,45,46,47,48]$ and is composed of the following persons: Baah, G.K. and Harrold, M.J. both from Georgia Institute of Technology Atlanta, GA; Bai, Z., Cao, F, Kucuk, Y., Shu, G., Sun, B., Sun, S-F., and Podgurski, A. from Case Western Reserve University, Cleveland, OH, USA; and Henderson, T.A.D. from Google Inc. Mountain View, CA, USA.

The next largest group of coauthors accounts for 4 papers [49, 50, 51, 52]. All the left 11 coauthors groups account each for a single paper. Figure 7a shows the number of papers published over time and Figure 7b provides an overview of the types of publications.

### 5.2. Use cases

From the 25 selected papers, we extracted the use cases and organized them into four groups: papers focusing on fault localization (G1, see section 5.2.1), on testing (G2, see section 5.2.2), on performance analysis (G3, see section 5.2.3), and papers reporting other use cases (G4, see section 5.2.4). Table 4 provides an overview of all four groups and figure 8 provides an overview of the evolution of the number of publications for each group.

![img-4.jpeg](img-4.jpeg)

Figure 6: Number of publications per authors. Only authors being listed in more than one paper are displayed.
![img-5.jpeg](img-5.jpeg)
(a) Evolution of the number of publications over time.
(b) Types of publication selected.

Figure 7: Overview of the evolution and the types of papers selected.


Table 4: Overview of the SE use cases for the 25 papers selected.

![img-6.jpeg](img-6.jpeg)

Figure 8: Number of publications over the years for each use case group.

# 5.2.1. Fault localization (G1) 

The first group includes 18 papers focused on fault localization. Fault localization is the task of automatically finding statements or other program elements that might potentially be the cause of a program failure.

Demographics. Out of the 16 papers, 10 papers have been published by a single group of coauthors (the group of Prof. Podgurski at Case Western Reserve University, Cleveland, OH, USA, and coauthors), from 2010 until $2021[39,40,41,42,43,44,45,46,47,48]$. The other 6 papers [53, 54, $55,49,56,57$ ] were published between 2012 and 2021, by distinct coauthors groups.

Almost all papers (14 out of 16) directly extend the work from Baah, Podgurski, and Harrold [39, 40, 41].
[49] proposes causal program dependence analysis (where causal inference is used to model the strength of program dependence relations) and applies it to fault localization. The work from Baah et al. [39, 40, 41] and Gore and Reynolds [55] are cited as related work.

Only one paper [56] in this category does not cite any of the other related work from this group. It focuses on fault localization in composite services.

Application of SCI. All the papers except for [56] focus the causal effect a given source code element might have on a failure. In [56], the focus lies on inputs/outputs relationships in composite services.

All papers except $[56,49]$ obtain a graphical causal models from analysis of the program structure (from control dependency or data dependency graph). Identification is done using the application of the backdoor criterion in order to reduce confounding bias. Estimation is done either through the application of linear regression, random forest, or matching techniques. Figure 9 gives more details about the type of graphical causal model used in this work.
![img-7.jpeg](img-7.jpeg)

Figure 9: Illustration of the types of graphical models used by Baah et al. [39, 40, 41]. The graphical causal model contains three types of nodes: the treatment $T_{s}$, the outcome $Y$ and confounders $X_{i}$ (nodes having an effect on both $Y$ and $T_{s}$ ). All variables are binary. The outcome variable $Y$ corresponds to the outcome of a given test ( 1 if it fails and is 0 otherwise); the treatment variable $T_{s}$ corresponds to the fact that a given statement $s$ was covered by the test or not; and finally the confounders are statements that both have an impact on $s$ (through control dependence), the corresponding variable is whether the confounding statements have been covered by the test. Identification is done using the back-door criterion and measuring the causal effect of a treatment $S$ on whether a test fails or pass is computed after adjusting for confounders.

The work from Lee et al. [49] focuses first on causal program dependency analysis (CPDA). The graphical causal model represents how likely a change to the value of a program element $s_{i}$ is going to cause a change to the value of another element $s_{j}$. This model is obtained from both the analysis of the source code and interventions (mutations). Authors apply this modeling technique to the problem of fault localization. The working hypothesis is that a faulty program element will have more impact on the output element in failing executions than in passing executions. Identification is done using the backdoor criterion and adjusting for confounders. Estimation is done but no explicit causal estimation method is mentioned.

As stated above, the work from Li et al. [56] differs from the others in this

group. It focuses on fault localization not in a given program but in service composition (i.e., in a set of interacting programs). The graphical causal model is obtained from the analysis and transformation of a service dependency graph: a graph representing services as nodes and service dependencies as links. Identification is done using the backdoor criterion. Estimation is also done but no explicit causal estimation method is mentioned.

Evaluation methods and data sets. Apart from [56], which performs a proof of concept relying upon simulated data, all other papers rely upon data sets containing programs, bugs (ground truth) and their corresponding tests suites that have been either collected for the purpose of the study or are publicly available (e.g., Defect4J, Siemens Suite, SIR). As these data sets contain a ground truth (past found bugs and the corresponding fault program elements), the papers are all performing benchmarks and compare different solutions or different versions of a solution with one another.

# 5.2.2. Testing (G2) 

The second group includes two papers $[36,50]$ focusing on testing. Software testing involves dynamic verification of the behaviour of a program against expected behaviour on a finite set of test cases. As such, fault localization (see section 5.2.1) can be considered as a subdomain of testing. The 2 papers reviewed apply causal inference for different testing methods: metamorphic testing and sensitivity analysis for [36], mutation testing for $[50]$.

Demographics. The work from Oh et al. [50] is about CPDA introduced in [49]. Two of the authors: Seongmin Lee and Shin Yoo are also coauthors of [49]. The work from Clark et al. [36] refers to many papers reviewed in the previous section. To the best of our knowledge this is their first paper reporting on the use of SCI for testing.

Application of SCI. In the paper [50], the focus lies on mutation testing. In mutation testing, small deleterious modifications are applied to program elements (called mutations), aiming at ensuring that a software test suite is capable of detecting a maximum of mutations. Strategies for choosing program elements to mutate are based upon their causal effect computed by the CPDA approach from [49]. Causal identification and estimation are the same as in [49].

In [36], the focus lies on testing scientific simulation software, or more precisely on testing the causal effects represented in the model being simulated. A graphical causal model is created in a semi-automated way (manual pruning by experts from the simulated system is required). Nodes are inputs and outputs of the simulation program. Identification is done using the backdoor criterion. The authors use regression and causal forest estimators as estimation methods.

Evaluation methods and data sets. In comparison to the previous use case, the papers deal with situations in which the ground truth is at best uncertain and at worst unknown. In [36], the authors provide a proof of concept using data being generated from three scientific simulations. In [50], the authors are comparing three heuristics for generating mutants using data from the SIR data set mentioned in section 5.2.1.

# 5.2.3. Performance modeling (G3) 

The third group includes four papers $[58,59,52,60]$ focusing on performance analysis. In $[58,59,60]$, the focus lies on performance debugging where the general goal is to understand which component of a system contributes to the measured performance and potentially to control for automated-decisions that impacts performance. [58] targets cloud computing, [59] highly configurable systems, and [60] video streaming. The work from Scholz et al. [52] is different as it aims at analysing the predictive performance of different faults prediction algorithms.

Demographics. All papers in this category are from different research groups. Only two authors, Richard Torkar and Robert Feldt, are coauthors of other papers, which we included and reviewed: [51] (see section 5.2.4) and [49] (see section 5.2.1).

The three papers $[58,59,60]$ cite other works that we collected, either from C1 (causal structure discovery), from C2 (counterfactual analysis), or from C4 (causal inference) [39, 54].

The paper [52] seem to belong to a somewhat adjacent research community and does not cite any of the papers we collected.

Application of SCI. Geiger et al. [58] aim at addressing two problems: 1) optimizing automated-decisions (that are made during the operation of a cloud server) that can impact performance (authors called it the control problem); 2) understanding which component of a system contributes to what extent

to the measured performance (authors called it the performance debugging problem). Both problems are formally defined within the language of counterfactuals and the authors propose a four-step method to solve both problems from getting a causal graph (here the authors stay relatively generic and propose to use a mix of randomized interventional experiments, observational data, and expert knowledge and refers to other related work), until estimating the causal effects. In their application examples, nodes in the causal graph represent system and network metrics.
[59] focus on the problem of understanding and estimating the impact of configuration options on performance. The graphical causal model is obtained via the use of a causal structure discover algorithm (FCI). Nodes in the graph represent configuration options and system and network performance metrics. Identification is done using the do-calculus (i.e., not limited to the backdoor criterion). Estimation methods are not directly mentioned but the paper refers to the following libraries ananke ${ }^{9}$ and causality ${ }^{10}$ for estimating the causal effects.
[60] focuses on analysing the performance of video streaming. The causal graph is obtained manually, and nodes represent network metrics. Identification is done using the backdoor criterion. The paper does not directly mention any estimation method.

Scholz and Torkar [52] aim at comparing the performances of different fault prediction algorithms. They use causal inference for the comparison but not directly for the fault localization and prediction (as in section 5.2.1). They generated the graphical causal model manually. The nodes represent the fault prediction algorithm to be compared (as treatment), evaluation metrics (as outcome), and project, language, LOC, and fix count. They applied the rules of do-calculus for the identification step. For the estimation, they used linear regression.

Evaluation methods and data sets. In this group all papers rely upon a ground truth that is either being simulated (as in $[58,60]$ ) or collected for the purpose of the study (as in $[59,52]$ ).

[^0]
[^0]:    ${ }^{9}$ https://ananke.readthedocs.io/en/latest/
    ${ }^{10}$ https://github.com/akelleh/causality

# 5.2.4. Other use cases (G4) 

The last group includes three papers, where the use cases were different from the other three groups. [51] applies causal inference methods to the problem of effort estimation. [61] reports on an early work on how to use SCI methods for building and evaluating software evolution theories. [62] is a short paper reporting on the usage of graphical causal models in the automotive industry.

Demographics. In [51], one of the coauthor also appears in another paper of this study [52] (see section 5.2.3). Both authors in [62], David Issa Mattos and Liu Yuchu are also coauthors of two papers, which we classified as C3 (doing causal inference without relying upon graphical causal models) [63, 64]. The work in [61] does not cross-cite any other paper in our study.

Application of SCI. [51] uses a graphical causal model (obtained manually), do-calculus for identification, and linear regression for estimation. The nodes in the graph represent code and project metrics taken from the International Software Benchmarking Standards Group (ISBSG) data set ${ }^{11}$.
[62] presents how graphical causal model are used at Volvo Cars. These graphs are obtained manually from domain experts. The paper does not mention how identification or estimation is done.
[61] reproduces the modeling assumptions of two existing studies with the help of a causal diagram (obtained manually). Unfortunately, the document does not specify whether and how the identification and estimation was done.

Evaluation and data sets. [51] is using data from the International Software Benchmarking Standards Group (ISBSG). The other two papers do not perform any evaluation.

### 5.3. Libraries

We extracted the names and URL of the libraries used in the selected papers. When the libraries were not mentioned but the paper provided an implementation repository, we analysed the repository dependencies. Our focus lies on libraries specific to SCI. We excluded libraries to perform regression tasks (like Ranger ${ }^{12}$ or Glmnet ${ }^{13}$ ), Bayesian probabilistic inference

[^0]
[^0]:    ${ }^{11}$ isbsg.org
    ${ }^{12}$ https://cran.r-project.org/web/packages/ranger/index.html
    ${ }^{13}$ https://cran.r-project.org/web/packages/glmnet/index.html

(like Pyro ${ }^{14}$ or Brms ${ }^{15}$ ), SEM (like Semopy ${ }^{16}$ ), and libraries to visualize or to manipulate graphs (like causalgraphicalmodels ${ }^{17}$ ). Table 5 provides an overview of the libraries mentioned in the selected papers.

The first thing we noticed, is that almost two thirds of the papers either did not mention any library (ten papers out of 25) or only mentioned using the R language ( 10 papers out of 25 ). The last five papers mentioned six distinct libraries related to SCI.


Table 5: Causal inference libraries used. The last column corresponds to the number of papers mentioning a given library.

# 6. Answers to our research questions 

### 6.1. RQ1: use cases

In section 5.2, we analysed the different SE use cases in which SCI had found an application. We clustered the use cases into four groups: fault localization (16 papers), testing (two papers), performance analysis (four papers) and other use cases (three papers). Most of the papers, which we collected were oriented towards the broader task of improving software quality.

### 6.2. RQ2: structure of the research community

Based upon our results (see section 5.1 and figure 8), we can say that the application of causal inference in SE is relatively young. The community of researchers applying SCI in SE seems to be fragmented. We could only

[^0]
[^0]:    ${ }^{14}$ https://github.com/pyro-ppl/pyro
    ${ }^{15}$ https://cran.r-project.org/web/packages/brms/index.html
    ${ }^{16}$ https://semopy.com/
    ${ }^{17}$ https://github.com/ijmbarr/causalgraphicalmodels

find one group of researchers (the group of prof. Podgurski and coauthors at Case Western Reserve University, Cleveland, OH, USA) that applied SCI over more than ten years. As already noted in section 5, there are not so many cross-references. Only one paper [36] provided an extensive state of the art (although focused on testing).

# 6.3. RQ3: causal methods 

In section 2, we provide a simplified SCI process with three main steps: modeling, identification and estimation.

### 6.3.1. Modeling

Concerning the modeling phase (building a graphical causal model), five papers used a manual approach $[60,52,51,61,62]$. One paper used an existing causal structure discovery algorithm (FCI) [59]. 20 papers have developed specific extraction methods for generating the graphical causal model in an automated way. One paper [36] used both an automated and an expert based (manual) approach for generating the graphical causal model.

### 6.3.2. Identification and Estimation

Almost all studied papers use the Backdoor criterion for identification (only two papers mention applying the rules of do-calculus without mentioning specific method like the Backdoor or the Frontdoor criteria). Estimation is then done, either through classical statistical estimation methods (e.g., linear regression or random forest) or matching techniques. Table 6 provides the details of the corresponding estimation methods and papers.


Table 6: Estimation methods for papers relying upon an explicit graphical causal model.

# 6.4. RQ4 and RQ5: Data sets, libraries and evaluation 

The results show that causal inference provides improvement, usually, through mitigating confounding bias (as illustrated by the benchmarks in $[45,50])$. Most of the reviewed papers use specific data sets that contains a ground truth for the specific use case at hand.

In section 5.3, we provided an overview of the libraries used. Many papers (20 out of 25 ) do not mention any specific SCI library. Out of these, 10 simply mention using R or using packages for regression (like linear regression or random forest). This can be explained by the fact that, for these papers, identification boils down to adjusting for the parents of the treatment variable under study. However, it must be noted that when the number of adjusted confounders increases, classical regression reaches its limits and specific estimation methods such as metalearners like X-learner might prove to perform better [65].

The distribution among the selected papers shows no particular preferred library and an equal mix between Python and R packages.

We have not been able to find any paper mentioning a specific benchmark data set dedicated to SCI in SE (as one could find in [3]).

## 7. Discussions

### 7.1. Application scope

Not all questions are aimed to be answered with a single tool. In his lecture and subsequent paper "Why Model?" [66], Epstein lists 17 different types of scientific questions (he called them modeling purposes). In order to situate the type of questions that can be answered with SCI methods, we can refer to Hernan et al. [67] and Pearl's ladder of causation [2]. Both frameworks highlight the difference between tasks that do not require the use of a causal model such as description: "what is $Y$ ?" and prediction "if I see $X$, what can I tell about $Y$ ?", and tasks that do require one such as intervention: "what if I do $X$, what is the effect on $Y$ ?" and counterfactuals "what if, in the same circumstances, instead of having done $X$, I had done $X^{\prime}$ ?". There is a hierarchical structure between these tasks, and Pearl showed that the formal tools used to answer a prediction question are not sufficient to answer an intervention question, and that the formal tools used to answer an intervention question are not sufficient to answer a counterfactual question $[2]$.

Some use cases in SE can be easily mapped to one of the four aforementioned tasks (description, prediction, intervention, and counterfactuals). For example, mutation testing is a typical example of a counterfactual analysis, as it involves testing a program under the same circumstances, but for a statement that has been mutated. Other questions like fault localization are not so obvious. At first, fault localization might seem like a prediction problem: given a program, predict which statement is more likely to induce a fault (i.e., its suspiciousness score). The papers reviewed in section 5.2.1 used the estimated causal effect of a statement on the failure of a given test to compute its suspiciousness score. There is no absolute correspondence between the SE use cases and the type of task (i.e. description, prediction, intervention and counterfactuals). Each task can be useful within a single use case. Each of these tasks simply has its limits and it is necessary to know how to recognize them and use the corresponding methods in the appropriate context.

# 7.2. Obtaining a causal graphical model 

To take full advantage of Pearl's SCI framework, a graphical causal model is required. This model can be obtained manually from domain experts or from previous experiments, it can be extracted from the software structure (e.g. from static code analysis, see section 5.2.1), or it can be learned from data (e.g. by mining software repositories or analysing logs, see also the papers classified as C 1 , see table B.9). The main purpose of such a graph is to reason about the presence of potential spurious correlations that may bias the analysis. It may not always be possible to obtain a detailed graph, as some influencing factors may not be directly measurable (such as "developer experience"), or in a high-dimensional setting it may be unclear what the causal structure looks like. In these cases, causal structure learning algorithms can help extract a causal structure from the data. It should be noted that there are different methods that rely on different assumptions, maybe the most important being whether we believe that all relevant variables have been measured or whether there are some unmeasured variables left. This is, for example, a major difference between two classical causal structure discovery algorithms: the PC algorithm, which assumes that there are no unobserved confounders, and FCI, which assumes the presence of unobserved confounders [14]. Even if the underlying causal graph is only partially known, it is already helpful to reason about potential bias and which estimation method might work (see section 2.5). As always with analysis methods, the devil is in the

![img-8.jpeg](img-8.jpeg)
(a) Confounder bias. $Z$ is a confounder and has an effect on both the treatment $T$ and the outcome $Y$. Not controlling for $Z$ will let spurious correlation flows along the path $\{T \leftarrow Z \rightarrow Y\}$.
![img-9.jpeg](img-9.jpeg)
(b) M-bias: controlling for the collider $Z$ will open a spurious correlation path $\{T \leftarrow A \rightarrow$ $Z \leftarrow B \rightarrow Y\}$ that is otherwise blocked.

Figure 10: Two typical examples of how bias can happen (see [5] for other examples).
detail, and several papers, such as $[68,6]$, remind us to be cautious about applying these methods without a proper understanding of their underlying assumptions (for an easy-to-read introduction to the pros and cons of the various SCI methods, see part 2 of [7]).

# 7.3. Reducing spurious correlation bias 

An argument made by many selected papers for the use of SCI methods over more traditional statistical inference techniques is the need to recognize and manage spurious correlation biases, for example confounder bias. A confounder is a variable that both has an impact on the treatment and the outcome of interest (see Figure 10a). Note that confounder bias is not the only bias that statistical causal methods can mitigate (another one is called M-bias, see Figure 10b), but to mitigate them, one needs a graphical causal model. The authors in [5] provide an analysis of typical bias and their corresponding graphical structure.

It is difficult to generalize the improvement provided by the application of SCI for all the use cases reviewed. Only in the case of fault localization (G1, see section 5.2.1), do we have enough evaluation results from independent researchers group. Out of 16 papers, 11 used a similar evaluation approach. They first compute the effectiveness of the proposed fault localization methods based on the EXAM score (also called cost). "EXAM score is the percentage of program statements a developer must examine, in nonincreasing order of their suspiciousness scores, before finding the fault" [45]. The evaluation is done by comparing several fault localization approaches on benchmark data sets (see the details in table 7). All these papers have shown that on average SCI methods improve fault localization in comparison to other more classical approaches.


Table 7: Details of the evaluations done in papers focusing on fault localization. Here only comparable papers from G1 are shown.

Relatively few papers have tried to analyse why SCI methods improve fault localization. First, Baah, Podgurski and Harrold [39] have shown that SCI can reduce confounding bias in fault localization scores. In their following work [41], the authors showed that using control dependence graphs does not capture all sources of confounders and that data dependencies need to be taken into account. A following work by Bai, Sun, and Podgurski analysed the impact of violating an important precondition for causal inference, called positivity [42]. Finally, in their most recent work, Küçük, Henderson, and Podgurski analysed the effect of covariate balance and imbalance on the performance fault localization methods. These papers provide us with an initial understanding of the benefits and limitations of SCI methods for fault location. Similar research will be needed to understand their potential and limitations in the context of other SE use cases.

# 7.4. Side effect: make some hypotheses explicit 

An important aspect to mention is that, in order to make use of SCI methods, it is necessary to make assumptions explicit: both about the aspects that are part of the system under study and about the assumed structure of the causal model. This point was also mentioned in two of our selected papers: $[51,62]$ and is a recuring theme in empirical research.

### 7.5. Implications for SE research

SCI methods belong to the toolkit of empirical research and are well suited for dealing with observational data. We believe, like [69], that in the future such methods will become more mainstream in SE research. However, it appears that these methods have been either relatively unknown until now or, if known, deemed unnecessary or too complicated to apply. One assumption is that the learning curve is relatively steep. It is only recently that books for a wider audience have been published (like $[2,12,7,8]$ ). Note that, in the data science and machine learning community several initiatives exist both from academia and industry to push forward the research and the application of SCI methods ${ }^{18}$. Chances are that these initiatives will spread to the SE community (if they haven't already) and that the learning curve will get shallower.

The main obstacle that we see for the application of SCI methods is to obtain a causal graphical model and the corresponding observational data.

[^0]
[^0]:    ${ }^{18}$ See for instance https://www.causalscience.org/ or https://www.pywhy.org/

Even if for some use cases it is possible to extract a causal graph automatically (like in $[49,45,59]$ ), very few papers have actually made their code available. This hinders both the reproducibility and learning of these methods. We also have not been able to find any data set specific to SE consisting of causal graphs and the corresponding observational data. For assessing SCI methods in SE, as well as for teaching them, it would be beneficial to have dedicated benchmark data sets where one could find ground truth data and the corresponding causal graphical model(s). A recommendation would be to gather causal graphs from the literature, starting with the application of Bayesian network in SE (see section 3) or papers in C1 (see table B.9).

After getting a causal graphical model, it is necessary to ensure that the assumptions behind SCI are met. We have encountered only few papers that discussed the applicability conditions of these methods. A further recommendation would be to gather both experience from researchers having applied SCI in SE in order to develop methodological guidelines and examples for applying SCI in SE.

Finally, researchers in the domain of causal inference has provided specific estimation methods (such as T-learner, X-learner, etc.) that have advantages over classical regression and matching techniques. Since not all of the selected papers made use of these particular techniques, it is not yet known what the effect of their use will be.

# 7.6. Threats to validity 

Research design validity. In this paper, we aimed at understanding how SCI methods have been applied in the field of SE. We conducted a mapping study, focusing on published literature (both peer-reviewed and non-peer-reviewed). This research design has its limits.

First, it is possible that researcher have applied causal inference methods but did not publish about it. It is also quite possible that researchers in the field of SE know about Pearl's framework for SCI, but did not consider to use it. A literature review process will never get this kind of information. Only interviews will.

Second, we have explicitly left out student work like master or PhD theses. The reason is that, although, theses are potentially interesting sources for understanding how a given method is applied, not all theses are freely available. During the search process, the only theses, we came across were from authors of papers already selected, and therefore we decided to leave them out.

Finally, we decided to include non-peer-reviewed work (in total 1 technical report and 4 preprints available on https://arxiv.org). Although, they were not subjected to a peer review process, the reason we kept them is that our interest is more in the methodology applied than in the final results.

Publication selection validity. It needs to be said, that it was relatively difficult to find relevant papers (as shown in 4). First, SE is a broad field, and it is possible that we might have missed some SE related aspects in our search process. Moreover, the boundaries between SE and artificial intelligence (AI) are somewhat blurred. For example, there are now many papers using causal inference for fairness (like $[70,71,72]$ ). Although, we found these papers during the selection process, we decided to leave them out considering them closer to AI than SE. To make matters worse, there is no standard vocabulary in SE for talking about causal inference. For instance, several papers from C1 (see table B.9) referred to causal structure discovery as "causal inference". Papers from C2 (see table B.10) referred to counterfactual analysis as "causal analysis" or "causal testing".

Furthermore, as our results show, the research community using SCI in SE seems to be fragmented, therefore the snowballing approach, we used to find new relevant papers also has its limits. To mitigate these risks, we used two different types of queries and applied two snowballing phases (see section 4). We stopped the snowballing after two rounds because we reached a saturation, i.e., further searches only resulted in articles that were already selected.

Finally, the selection has been done by a single person.
Data validity. For this paper, we tried as much as possible, to extract only factual information that is not subject to interpretation. We have not considered the quality of the publications. The reason is that our focus lies on the methods applied and less on the results achieved. Considering the value of SCI methods for the different use cases, almost all papers shows an improvement compared to their own benchmark (which raises the question of publication bias). Considering the fact that half of the papers ( 12 out of 25) were published from 2020 onwards, it is yet too early to judge properly the advantages of SCI methods. Only in fault localization, where the papers span from 2010 until now, and where independent groups of researchers have applied SCI methods can we estimate the pros and cons of SCI.

Data synthesis and conclusions validity. As already mentioned, this paper is the work of a single person. The main threat to validity comes from the expertise of the reviewer. To mitigate such bias, the findings were also presented to and discussed with some of the authors of the selected papers and within a working group on causal inference. None of the persons contacted could bring novel work to our attention. Obviously, this only consolidates the validity of the conclusion but does not remove completely the threats mentioned above.

# 8. Conclusion 

In this paper, we conducted a mapping study and selected 25 papers applying SCI methods in the SE domain. We focused specifically on Pearl's framework that rely upon graphical causal models. These methods are interesting when targeting problems requiring estimating causal effects from observational data. Our analysis shows that these techniques are not yet mainstream in SE research. By providing this overview, we hope to promote awareness of these methods, lay the groundwork for discussions on where and when to apply them, and eventually increase the number of applications of these methods in SE.

## Acknowledgement

The author would like to thank Nico Cappel, Niklas Gutting, and Ilir Hulaj for their preliminary work "Anwendungen von kausaler Inferenz in Software-Engineering" done during their SE Seminar at the Technical University of Kaiserslautern; Adam Trendowicz and Andreas Jedlitschka (Fraunhofer IESE, Kaiserslautern, Germany), and Andy Podgurski (Case Western Reserve University, Cleveland, OH, USA), for the useful discussions; and Patricia Kelbert for proofreading the manuscript.

# Appendix A. Keywords analysis details 


Table A.8: Queries used to determine the most relevant keywords. Each query was performed in Scopus on the 2nd of August 2022, targeting only Title, Abstract and Keywords (i.e., using TITLE-ABS-KEY ()). Each query takes the form TITLE-ABS-KEY((SE TERM) AND (CI TERM)).

# Appendix B. details of the four categories c1, c2, c3, and c4 


Table B.9: Papers classified as C1, focusing on modeling potential causal structures but not using identification and estimation techniques as defined in section 2 .


Table B.10: Papers classified as C2, focusing on counterfactual analysis but not relying upon any methods defined in section 2 .


Table B.11: Papers classified as C3, doing causal inference without relying upon a causal graphical model.


Table B.12: Papers classified as C4, applying the three steps of causal inference: modeling, identification and estimation.