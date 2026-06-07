# IDENTIFIABILITY IN CAUSAL BAYESIAN NETWORKS: A GENTLE INTRODUCTION 

## MARCO VALTORTA AND YIMIN HUANG

## QUERY SHEET

This page lists questions we have about your paper. The numbers displayed at left can be found in the text of the paper for reference. In addition, please review your paper as a whole for correctness.

Q1: Au: Please confirm this s/b Fig. 2
Q2: Au: What is " 16 "?
Q3: Au: Please provide the city of publication
Q4: Au: Please clarify what the 15 is for...issue number?
Q5: Au: What is " 12 "?
Q6: Au: Please clarify meaning of " 17 "
Q7: Au: Huang and Valtorta, 2006. Has two references Please specify which is $\mathrm{a}, \mathrm{b}$ ?
Q8: Au: Shpitser and Pearl, 2006. Has two references Please specify which is a,b?
Q9: Au: Tian and Pearl, 2002. Has two references Please specify which is a,b?
Q10: Au: Figure 8 not cited in text. Please check.

## TABLE OF CONTENTS LISTING

The table of contents for the journal will list your paper exactly as it appears below:

IDENTIFIABILITY IN CAUSAL BAYESIAN NETWORKS: A GENTLE INTRODUCTION
Marco Valtorta and Yimin Huang

# IDENTIFIABILITY IN CAUSAL BAYESIAN NETWORKS: A GENTLE INTRODUCTION 

MARCO VALTORTA and YIMIN HUANG<br>Department of Computer Science and Engineering, University of South Carolina

In this article we describe an important structure used to model causal theories and a related problem of great interest to semi-empirical scientists. A causal Bayesian network is a pair consisting of a directed acyclic graph (called a causal graph) that represents causal relationships and a set of probability tables, that together with the graph 10 specify the joint probability of the variables represented as nodes in the graph. We briefly describe the probabilistic semantics of causality proposed by Pearl for this graphical probabilistic model, and how unobservable variables greatly complicate models and their application. A common question about causal Bayesian networks is 15 the problem of identifying casual effects from nonexperimental data, which is called the identifability problem. In the basic version of this problem, a semi-empirical scientist postulates a set of causal mechanisms and uses them, together with a probability distribution on the observable set of variables in a domain of interest, to predict 20 the effect of a manipulation on some variable of interest. We explain this problem, provide several examples, and direct the readers to recent work that provides a solution to the problem and some of its extensions. We assume that the Bayesian network structure is given to us and do not address the problem of learning it from data 25 and the related statistical inference and testing issues.

# MOTIVATION 

Flash back to the late 1950s. Evidence was mounting that smoking was bad for one's health. In particular, some researchers postulated a causal link between smoking and lung cancer. Such a model could be represented by the graph of Fig. 1.

The intuitive meaning of the model in Fig. 1 is that there is a mechanism that relates cigarette smoking (node $X$ ) and lung cancer (node $Y$ ), in the sense that the probability of a person getting lung cancer is affected by that person smoking cigarettes. All that could be observed was a strong correlation between smoking and lung cancer, but the public health community of the 1950s suspected that the correlation was a manifestation of a causal link, and that therefore a manipulation of the smoking variable, namely by making smoking less pervasive, would lead to a reduction of the incidence of lung cancer in the population.

The model of Fig. 1, however, was not universally accepted, and in a way that has a profound impact on the expected value of public health policy efforts directed at reducing smoking in the general population. The distinguished British statistician R. A. Fisher suggested that this model was a manifestation of "an error... of an old kind, in arguing from correlation to causation," and proposed that the correlation between smoking and lung cancer could be explained by a genetic predisposition to smoking and lung cancer, as described in Fig. 2. Since the genotype (represented by node $U$ in the figure) was not observable at the time of Fisher's work, it appeared impossible to conclude that reducing smoking would have a positive effect on the prevalence of lung cancer. (The links from $U$ to $X$ and $Y$ are drawn dashed to emphasize that $U$ is unobservable.) By accepting Fisher's model, we would have to conclude that the effect of smoking on lung cancer is unidentifiable; i.e., it cannot be determined from statistics derived solely from variables that are in the model and that can be observed (such as $X$ and $Y$ ). Incidentally, studies involving identical twins (who presumably would have the same genetic predisposition to both smoking and lung cancer) were carried out in attempt to identify the causal effect of smoking on lung cancer, but at least Fisher was unconvinced that they settled the matter (Fisher 1958).

Figure 1. A simple causal model relating cigarette smoking and lung cancer.

![img-0.jpeg](img-0.jpeg)

Figure 2. R. A. Fisher's genotype model explaining the correlation between smoking and lung cancer.

Even in these very simple models, we can observe two important features of the causal graphs that we will formalize as causal Bayesian networks in the remainder of this article. First, the models relate variables (genotype, smoking, lung cancer) represented as nodes in a directed acyclic graph through directed edges or links (such as the edge from smoking to lung cancer) indicating a causal influence. The links from $U$ to $X$ and $Y$ are drawn dashed to emphasize that $U$ is unobservable. Second, in the first model, the joint probability of the variables can be represented by the product of the prior probability of smoking times the conditional probability of lung cancer given smoking. In the second model, the joint probability of genotype, smoking, and lung cancer can be represented by the product of the prior probability of the genotype, times the conditional probability of smoking given the genotype, times the conditional probability of the genotype and smoking. This decomposition is allowed by the fundamental rule of probability in the case of a joint distribution of two and three variables.

In the next section we define formally the key notion of causal Bayesian network. Following that, we discuss the concept of intervention and define an identifiability problem. We then present a proof of 80 unidentifiability for a particular causal Bayesian network and use different versions of smoking-lung cancer causal models to show why the identifiability problem is interesting and how it can be solved mathematically. Our conclusions consist mainly of a survey of the recent literature on the topic.

Disclaimers are in order. We do not claim that any of our specific examples are reflective of good domain knowledge. We are not interested in validating or repudiating causal assumptions specific to a domain. We assume that the domain knowledge is obtained somehow before our analysis. The framework described in this article is limited to answering 90 the question of whether a given set of assumptions is sufficient for quantifying causal effects from non-experimental data.

# CAUSAL BAYESIAN NETWORKS 

A Bayesian network (BN) is a graphical representation of the joint probability distribution of a set of discrete variables. The representation consists of a directed acyclic graph (DAG), prior probability tables for the nodes in the DAG that have no parents and conditional probabilities tables (CPTs) for the nodes in the DAG given their parents. As an example, consider the network in Fig. 3.

More formally, a Bayesian network is a pair composed of: (1) a multivariate probability distribution over $n$ random variables in the set $V=V_{1}, \ldots, V_{n}$, and (2) a directed acyclic graph (DAG) whose nodes are in one-to-one correspondence with $V_{1}, \ldots, V_{n}$. (Therefore, for the sake of convenience, we do not distinguish the nodes of a graph from variables of the distribution.)

Bayesian networks allow specification of the joint probability of a set of variables of interest in a way that emphasizes the qualitative aspects of the domain. The defining property of a Bayesian network is that the conditional probability of any node, given any subset of non-descendants, is equal to the conditional probability of that same node given the parents alone. The Chain rule for Bayesian networks (Neapolitan 1990) follows from the preceding definition: Let $P\left(V_{i} \mid \pi\left(V_{i}\right)\right)$ be the conditional probability of $V_{i}$ given its parents. (If there are no parents for $V_{i}$, let this be $P\left(V_{i}\right)$ ). If all the probabilities involved are nonzero, then $P(V)=\prod_{v \in V} P(v \mid \pi(v))$.

Three features of Bayesian networks are worth mentioning. First, the directed graph constrains the possible joint probability distributions
![img-1.jpeg](img-1.jpeg)

Figure 3. (a) Example Bayesian network, (b) variable states, and (c) conditional probability table for $B$ given $A$.

represented by a Bayesian network. For example, in any distribution consistent with the graph of Fig. 3, $D$ is conditionally independent of $A$ given $B$ and $C$. Also, $E$ is conditionally independent of any subset of the other variables given $C$.

Second, the explicit representation of constraints about conditional independence allows a substantial reduction in the number of parameters to be estimated. In the example, assume that the possible values of the five variables are as shown in Fig. 3(b). Then, the joint probability table $P(A, B, C, D, E)$ has $2 \times 3 \times 2 \times 4 \times 4=192$ entries. It would be very difficult to assess 191 independent parameters. However, the independence constraints encoded in the graph permit the factorization $P(A, B, C, D$, $E)=P(A) \times P(B \mid A) \times P(C \mid \mathrm{A}) \times P(D \mid B, C) \times P(E \mid C)$, which reduces the number of parameters to be estimated to $1+4+2+18+6=31$. The second term in the sum is the table for the conditional probability of $B$ given $A$. This probability is shown in Fig. 3(c); note that there are only four independent parameters to be estimated since the sum of values by column is one.

Thirdly, the Bayesian network representation allows a substantial (usually, dramatic) reduction in the time needed to compute marginals for each variable in the domain. The explicit representation of constraints on independence relations is exploited to avoid the computation of the full joint probability table in the computation of marginals both prior and conditioned on observations. Limitation of space prevents the description of the relevant algorithms; see Jensen (2001) for a discussion of the justly famous junction tree algorithm.

The most common operation on a Bayesian network is the computation of marginal probabilities, both unconditional and conditioned upon evidence. Marginal probabilities are also referred as beliefs in the literature (Pearl 1988). This operation is called probability updating, belief updating, or belief assignment.

A link between two nodes in a Bayesian network is often interpreted as a causal link. However, this is not necessarily the case. When each link in a Bayesian network is causal, then the Bayesian network is called a causal Bayesian network or Markovian model. Markovian models are popular graphical models for encoding distributional and causal relationships. To summarize, a Markovian model consists of a DAG $G$ over a set of variables $V=\left\{V_{1}, \ldots, V_{n}\right\}$, called a causal graph and a probability distribution over $V$, which has some constraints on it that will be specified precisely below. We use $V(G)$ to indicate that $V$ is the variable set of

graph $G$. If it is clear in the context, we also use $V$ directly. The interpretation of such kind of model consists of two parts. The probability distribution must satisfy two constraints. The first one is that each variable in the graph is independent of all its non-descendants given its direct parents. The second one is that the directed edges in $G$ represent causal influences between the corresponding variables. A Markovian model for which only the first constraint holds is called a Bayesian network, and its DAG is called a Bayesian network structure. This explains why Markovian models are also called causal Bayesian networks. As far as the second condition is concerned, some authors prefer to consider Eq. (3) (below) as definitional; others take Eq. (3) as following from more general considerations about causal links, and in particular the account of causality that requires that, when a variable is set, the parents of that variable be disconnected from it. A full discussion of this is beyond the scope of this article, but see Lauritzen (2001) and Pearl (2000).

In this article, capital letters, like $V$, are used for variable sets; lowercase letters, like $v$, stand for the instances of variable set $V$. Capital letters like $X, Y$, and $V_{i}$ are also used for single variables, and their values can be $x, y$, and $v_{i}$. Normally, we use $F(V)$ to denote a function on variable set $V$. An instance of this function is denoted as $F(V)(V=v)$, or $F(V)(v)$, or just $F(v)$. Each variable is in one-to-one correspondence to one node in the causal graph.

We use $P a\left(V_{i}\right)$ to denote parent node set of variable $V_{i}$ in graph $G$ and $p a\left(V_{i}\right)$ as an instance of $P a\left(V_{i}\right) . C h\left(V_{i}\right)$ is $V_{i}$ 's children node set; $c h\left(V_{i}\right)$ is an instance of $C h\left(V_{i}\right)$.

Based on the probabilistic interpretation, we get that the joint probability function $P(v)=P\left(v_{1}, \ldots, v_{n}\right)$ can be factorized as

$$
P(v)=\prod_{V_{i} \in V} P\left(v_{i} \mid p a\left(V_{i}\right)\right)
$$

From the joint probability, all marginal prior and posterior probabilities can be obtained, by marginalizing and conditioning. The notion of conditional probability is a well-defined and accepted one. The conditional probability of an event $S$ given an event $D$ is defined as

$$
P(S \mid D)=\frac{P(S, D)}{P(D)}
$$

This definition is actually an axiom of probability, which can be shown to hold in all useful interpretation of probability, including the

subjective Bayesian one (Neapolitan 1990). It is a tenet of applied Bayesian reasoning that beliefs are updated by conditioning when new knowledge is gained. There are, however, two kinds of updating in causal Bayesian networks, viz. updating by conditioning (also known as updating by observation) and updating by intervention.

Updating by conditioning is well-defined and understood, both in principle and algorithmically (Cooper 1990; Lauritzen 1996). There are free and commercial software packages, like Hugin, ${ }^{1}$ that perform update by conditioning on Bayesian networks in a very efficient manner in most practical cases. In the next section, we explain updating by intervention.

# INTERVENTIONS AND THE IDENTIFIABILITY PROBLEM 

The causal interpretation of a Markovian model enables us to predict intervention effects. Here, intervention means some kind of modification of factors in product (Fisher 1958). The simplest kind of 205 intervention is fixing a subset, $T \subseteq V$, of variables to some constants, $t$, denoted by $d o(T=t)$ or just $d o(t)$. Then, the post-intervention distribution

$$
P_{T}(V)(T=t, V=v)=P_{t}(v)
$$

is given by:

$$
P_{t}(v)=P(v \mid d o(t))=\left\{\begin{array}{ll}
\prod_{V_{i} \in V \backslash T} P\left(v_{i} \mid p a\left(V_{i}\right)\right) & v \text { consistant with } t \\
0 & v \text { inconsistant with } t
\end{array}\right.
$$

To stress the distinction between observation and intervention, we present a simple example based on the sneezing model of Fig. 4, originally presented in Pearl and Verma (1991), in which wiping one's nose (W) is caused by sneezing (S), which in turn is caused by either a cold (C) or hay fever (F), or both. To complete this causal Bayesian network, we give the probabilities in Table 1 and $P(C o l d)=(.2, .8)$, $P($ HayFever $)=(.1, .9)$, and $P($ WipingOne'sNose $\mid$ Sneezing $=y)=.9$.

We use this causal graph to compare the notions of observation and intervention. The initial probabilities for the four variables are shown in 220 Fig. 5. Suppose that it is observed that sneezing occurs. The probabilities of each variable in the network are updated as shown in Fig. 6.

[^0]
[^0]:    ${ }^{1}$ http://www.hugin.com/

![img-2.jpeg](img-2.jpeg)

Figure 4. A causal graph for sneezing.

Suppose now that we intervene and force sneezing. The connections between node Sneezing and its parents are cut, as indicated in the model of Fig. 7. Unlike the situation in which sneezing is observed, 225 the posterior probabilities of Cold and Hay Fever are unchanged.

We call interventions of the simple kind described so far in this section, which consist in fixing a subset of variables to some constants, crisp interventions. Referring to the sneezing causal graph, a simple example is setting the variable Sneezing to the value true (i.e., forcing sneezing to occur), by the administration of a perfectly effective sneezing powder. More complicated interventions can be described using the intervention graph or augmented model (Korb and Nicholson 2003), in the way originally described in Pearl (1993) and Pearl (2000). The intervention graph is formed by adding a parent to each node representing a 235 variable where intervention is contemplated. The brief discussion here follows the excellent presentation of Spirtes et al. (1993) very closely. The interested reader should consult that reference for more detail.

The effect of a crisp intervention $d o\left(X_{i}=x_{i}\right)$ can be encoded by adding to $G$ a link $F_{i} \rightarrow X_{i}$, where $F_{i}$ is a new variable taking values in $\left\{d o\left(x_{i}\right), \right.$ idle $\}, x_{i}$ ranges over the domain of $X_{i}$, and idle represents no

Table 1. Table for $P($ Sneezing $=y \mid$ Cold, Hay Fever $)$


![img-3.jpeg](img-3.jpeg)

Figure 5. Initial marginal probabilities for the sneezing model.
![img-4.jpeg](img-4.jpeg)

Figure 6. Marginal probabilities for the sneezing causal Bayesian network, after updating by conditioning on the evidence of sneezing.
![img-5.jpeg](img-5.jpeg)

Figure 7. The sneezing causal graph, after a crisp intervention that Forces sneezing to occur.

intervention. The new parent set of $X_{i}$ in the augmented network is $P a^{\prime}\left(X_{i}\right)=P a\left(X_{i}\right) \cup\left\{F_{i}\right\}$, and it is related to $X_{i}$ by the conditional probability.

$$
P\left(x_{i} \mid p a^{\prime}\left(X_{i}\right)\right)=\left\{\begin{array}{rl}
P\left(x_{i} \mid p a\left(X_{i}\right)\right. & \text { if } F_{i}=i d l e \\
0 & \text { if } F_{i}=d o\left(x_{i}^{\prime}\right) \text { and } x_{i} \neq x_{i}^{\prime} \\
1 & \text { if } F_{i}=d o\left(x_{i}^{\prime}\right) \text { and } x_{i}=x_{i}^{\prime}
\end{array}\right.
$$

The effect of the intervention $d o\left(x_{i}^{\prime}\right)$ is to transform the original probability function $P\left(X_{1}, \ldots, X_{n}\right)$ into a new probability function $P_{X_{i}=X_{i}^{\prime}}\left(X_{i}, \ldots, X_{n}\right)$, given by

$$
P_{X_{i}=X_{i}^{\prime}}\left(X_{i}, \ldots, X_{n}\right)=P^{\prime}\left(X_{1}, \ldots, X_{n} \mid F_{i}=d o\left(x_{i}^{\prime}\right)\right)
$$

where $P^{\prime}$ is the distribution specified by the augmented network 250 $G^{\prime}=G \cup\left\{F_{i} \rightarrow X_{i}\right\}$ and (4), with an arbitrary prior distribution on $F_{i}$. In general, by adding a hypothetical intervention link $F_{i} \rightarrow X_{i}$ to multiple nodes in $G$, we can construct an augmented probability function $P^{\prime}\left(X_{1}, \ldots, x_{n} ; F_{i}, \ldots, F_{n}\right)$, which allows for interventions beyond the setting of a subset of variable to constants. For a simple example related to the causal graph of Fig. 4, imagine administering an imperfectly effective sneezing power, which causes sneezing with probability $p$. This would be modeled by setting the prior probability of the value true for the forcing variable $F_{\text {Sneezing }}$ in the model of Fig. 9 to $p$.

In many cases, an empirical scientist faces the following question: 260 Can we estimate the post-intervention distribution under crisp intervention from non-experimental data? When all the variables in the model are observable, the answer for the question above is positive. But when some variables in $V$ are unobservable, things are much more complex, and the answer may be either positive or negative, depending on the structure of the causal Bayesian network and the relative
![img-6.jpeg](img-6.jpeg)

Figure 8. Intervention graph.

![img-7.jpeg](img-7.jpeg)

Figure 9. An intervention graph for the sneezing model of Fig. 4.
location of observable and unobservable variables. We give a detailed proof of unindentifiability for the key example of Fig. 10 in the next section.

# AN UNIDENTIFIABLE MODEL 

A simple example of unidentifiable model is R. A. Fisher's genotype model of the relation between smoking and lung cancer (Spirtes et al. 1993), which we briefly discussed in the first section of this article. R. A. Fisher suggested that the observed correlation between smoking $(X)$ and lung cancer $(Y)$ can be explained by some sort of carcinogenic 275 genotype $(U)$ that involves inborn craving for nicotine.

The carcinogenic genotype is presented by Fisher as a concept that has not been observed in nature, and it is therefore modeled as an unobservable variable. Intuitively, the effect of smoking on lung cancer is unidentifiable because we are not sure whether the observed response (lung cancer) is 280 due to our action (smoking) or to the confounder event (genotype) that triggers the action and simultaneously causes the response.
![img-8.jpeg](img-8.jpeg)

Figure 10. R. A. Fisher's genotype model explaining the correlation between smoking and lung cancer (Fig. 2, repeated here for the reader's convenience).

Formally, we show that the effect of smoking on lung cancer is unidentifiable in the following way. We show that, with a given observational distribution $P(x, y)$, it is possible to find two different causal Baye- 285 sian networks $M_{1}$ and $M_{2}$ that share the graph of Fig. 10, and such that $P^{M_{1}}(x, y)=P^{M_{2}}(x, y)$. As an extreme example, we can construct two drastically different models following the explanation that smoking is the cause of lung cancer (the part $a$ in Fig. 11) or carcinogenic genotype is the only cause of this fatal disease (the part $b$ in Fig. 11). Both of them satisfy the graph in Fig. 10. That is, Fig. 10 generalizes both graphs in Fig. 11, or, equivalently, the graphs in Fig. 11 are special cases of the graph in Fig. 10.

Our question about the smoking and lung cancer model of Fig. 10 is: If we intervene on variable $X$, which means we control the smoking 295 behavior, is unexperimental observational knowledge about smoking and lung-cancer (i.e., $P(x, y)$ ) sufficient to determine the probability of lung cancer? Mathematically, this problem can be explained as a question on the Markovian model of Fig. 10: If we know $P(x, y)$, which is the joint probability on observable variables $X, Y$, can we 300 calculate $P_{x}(y)$ for all $(x, y)$ ? Unfortunately, the answer to this question is negative.

The fact is that it is possible to create a model compatible with Fig. 11 part $a$ and another model compatible with Fig. 11 part $b$, both of them satisfying $P(x, y)$, but with different $P_{x}(y)$. We cannot get 305 the same $P_{x}(y)$ from these two models because for the first model, the intervention will change the probability of lung cancer but if the second model is correct, the behavior of smoking has no effect on lung cancer at all.

We now carry out the calculations in detail to show that the effect 310 of smoking on lung cancer is unidentifiable for the causal Bayesian network of Fig. 10. All variables are binary, and their states are denoted as 0 and 1 . For variable $U$, we assume $P(U=0)=P(U=1)=1 / 2$.
![img-9.jpeg](img-9.jpeg)

Figure 11. Different models compatible with the model of Fig. 10.

The conditional probability tables of variable $X$ and $Y$ in model $M 1$ are defined as below:




The conditional probability tables of variable $X$ and $Y$ in model $M_{2}$ defined as:




Note that, since $P(X, Y)=\Sigma_{U} P(Y \mid x, U) P(X \mid U) P(U)$, for both models $M_{1}$ and $M_{2}$, we obtain:


We also have $P_{X}(Y)=\Sigma_{U} P(Y \mid X, U) P(U)$ for both two models, and 325 for $M_{1}, P_{X=0}^{M_{1}}(Y=0)=0.45$, but for $M_{2}$, we have $P_{X=0}^{M_{2}}(Y=0)=0.40$.

We conclude that $P_{X}(Y)$ is unidentifiable in this causal graph.
We emphasize, again, that the models we use are not intended to be correct representations of domain knowledge: We use them simply to illustrate how they can be used in representing causal modeling assumptions, which have different bearing on the identifiability of causal effects.

![img-10.jpeg](img-10.jpeg)

Figure 12. Smoking (X) affects lung cancer (Y) through tar deposits (X).

In that spirit, we conclude the section by describing two more models that may match some researchers' understanding of the relation between smoking and lung cancer.

It is observed that smoking causes tar deposit on lung. So, with the evidence that genotype may cause lung cancer and smoking behavior, a researcher may establish a causal model about smoking $(X)$ and lung cancer $(Y)$ with $\operatorname{tar}(Z)$. See Fig. 12. Incidentally, R. A. Fisher himself seems to hint at such a model (Fisher 1958). This causal graph assumes that smoking cigarettes has no effect on the production of lung cancer except as mediated through tar deposits and that genotype has no effect on the amount of tar in the lungs except indirectly through cigarette smoking.

Finally, the causal graph of Fig. 13 adds to the causal graph of Fig. 12 the assumption that the production of tar deposits in the lung $(Z)$ is affected by pollution $\left(U_{1}\right)$, which also affects the propensity towards smoking $(X)$.

The causal effect of smoking on lung cancer $\left(P_{X}(Y)\right)$ is identifiable in the causal graph of Fig. 12, but unidentifiable in the causal graph of Fig. 13. We do not attempt to prove this claim in this article, and refer the reader to the references given in the next section for the algorithms needed to establish this claim and, in the case of Fig. 12, compute the value of the causal effect.
![img-11.jpeg](img-11.jpeg)

Figure 13. Air pollution $\left(\mathrm{U}_{1}\right)$ affects tar deposits $(\mathrm{Z})$ and the propensity to smoke $(\mathrm{X})$.

# CONCLUSION 

This article provides an introduction to the problem of inferring the strength of cause-and-effect relationships from a causal Bayesian network, emphasizing conceptual foundations and examples. In this concluding section, we provide a roadmap to the literature where proofs and algorithms are provided.

A causal Bayesian network consists of a causal graph, an acyclic directed graph expressing causal relationships, and a probability distri- 360 bution respecting the independence relation encoded by the graph. Because of the existence of unmeasured variables, the following identifiability questions arise: "Can we assess the strength of causal effects from nonexperimental data and casual relationships? And if we can, what is the total causal effect in terms of estimable quantities?"

The questions just given could partially be answered using graphical approaches due to Pearl and his collaborators. More precisely, graphical conditions have been devised to show whether a causal effect, that is, the joint response of any set $S$ of variables to interventions on a set $T$ of action variables, denoted $P_{T}(S)^{2}$ is identifiable or not. Those 370 results are summarized in Pearl (2000). For example, "back-door" and "front-door" criteria and do-calculus Pearl (1995); graphical criteria to identify $P_{T}(S)$ when $T$ is a singleton (Galles and Pearl 1995); graphical conditions under which it is possible to identify $P_{T}(S)$ where $T$ and $S$ are, possibly non-singleton, sets, subject to a special condition called Q-identifiability (Pearl and Robins 1995). Further study can be also found in Kuroki and Miyakawa (1999) and Robins (1997).

More recently, Tian and Pearl published a series of papers related to this topic (Tian and Pearl 2002; Tian and Pearl 2002; Tian and Pearl 2003). Their new methods combined the graphical character of causal graph and the algebraic definition of causal effect. They used both algebraic and graphical methods to identify causal effects. The basic idea is, first, to transfer causal graphs to semi-Markovian graphs Tian and Pearl (2002), then to use Algorithm 2 in Tian and Pearl (2003) (the Identify algorithm) to calculate the causal effects we want to know.

Tian and Pearl's method was a great contribution to this study area. But there were still some problems left. First, even though we believe, as Tian and Pearl do, that the semi-Markovian models obtained from the

[^0]
[^0]:    ${ }^{2}$ Pearl and Tian used notation $P(s \mid d o(t))$ and $P(s \mid \hat{t})$ in [6] and $P_{t}(S)$ in [13], [14]

Q9 transforming Projection algorithm in Tian and Pearl (2002) are equal to the original causal graphs, and therefore the causal effects should be the same in both models, still, to the best of our knowledge, there was no formal proof for this equivalence. Second, the completeness question of the Identify algorithm in Tian and Pearl (2003) was still open, so that it was unknown whether a causal effect was identifiable if that Identify algorithm failed.

In a series of papers, Huang and Valtorta $(2006 ; 2006)$ and, indepen- 395 Q8 dently, Shpitser and Pearl (2006) solved the open questions and several related ones. In particular, following Tian and Pearl's work, Huang and Valtorta (2006) solved the second question. They showed that the Identify algorithm Tian and Pearl used on semi-Markovian models is sound and complete. In Huang and Valtorta (2006), they followed the ideas Tian and Pearl presented in Tian and Pearl (2003), but instead of working on semi-Markovian models, they focused on general causal graphs directly, and their proofs showed, that Algorithm 2 in Tian and Pearl (2003) can also be used in general causal models, and that the algorithm is sound and complete, which means a causal effect is identifiable if and only if the given algorithm runs successfully and returns an expression that is the target causal effect in terms of observable quantities.

It is our hope that the reader will be motivated to study, implement, refine, and apply the algorithmic framework to causal modeling that Pearl pioneered and that, the authors believe, is ready to be put to the test of deployment in actual applications.
