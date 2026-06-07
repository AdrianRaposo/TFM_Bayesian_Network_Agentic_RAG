# Computing, Artificial Intelligence and Information Technology 

## Bayesian network classifiers for identifying the slope of the customer lifecycle of long-life customers

Bart Baesens ${ }^{\text {a }}$, Geert Verstraeten ${ }^{\text {b }}$, Dirk Van den Poel ${ }^{\text {b,* }}$, Michael Egmont-Petersen ${ }^{\text {c }}$, Patrick Van Kenhove ${ }^{\text {b }}$, Jan Vanthienen ${ }^{\text {a }}$<br>${ }^{a}$ Department of Applied Economic Sciences, K.U. Leuven, Naamsestraat 69, B-3000 Leuven, Belgium<br>${ }^{\text {b }}$ Department of Marketing, Faculty of Economics and Business Administration, Ghent University, Hoveniersberg 24, B-9000 Ghent, Belgium<br>${ }^{\text {c }}$ Institute of Information and Computing Sciences, Utrecht University, Padualaan 14, De Uithof, The Netherlands<br>Received 18 December 2001; accepted 5 December 2002


#### Abstract

Undoubtedly, customer relationship management has gained its importance through the statement that acquiring a new customer is several times more costly than retaining and selling additional products to existing customers. Consequently, marketing practitioners are currently often focusing on retaining customers for as long as possible. However, recent findings in relationship marketing literature have shown that large differences exist within the group of long-life customers in terms of spending and spending evolution. Therefore, this paper focuses on introducing a measure of a customer's future spending evolution that might improve relationship marketing decision making. In this study, from a marketing point of view, we focus on predicting whether a newly acquired customer will increase or decrease his/her future spending from initial purchase information. This is essentially a classification task. The main contribution of this study lies in comparing and evaluating several Bayesian network classifiers with statistical and other artificial intelligence techniques for the purpose of classifying customers in the binary classification problem at hand. Certain Bayesian network classifiers have been recently proposed in the artificial intelligence literature as probabilistic white-box classifiers which allow to give a clear insight into the relationships between the variables of the domain under study. We discuss and evaluate several types of Bayesian network classifiers and their corresponding structure learning algorithms. We contribute to the literature by providing experimental evidence that: (1) Bayesian network classifiers offer an interesting and viable alternative for our customer lifecycle slope estimation problem; (2) the Markov Blanket concept allows for a natural form of attribute selection that was very effective for the application at hand; (3) the sign of the slope can be predicted with a powerful and parsimonious general, unrestricted Bayesian network classifier; (4) a set of three variables measuring the volume of initial purchases and the degree to which customers originally buy in different categories, are powerful predictors for estimating the sign of the slope, and might therefore provide desirable additional information for relationship marketing decision making.


(c) 2003 Elsevier B.V. All rights reserved.

[^0]
[^0]:    * Corresponding author. Tel.: +32-9-264-8980; fax: +32-9-264-4279.

    E-mail addresses: bart.baesens@econ.kuleuven.ac.be (B. Baesens), geert.verstraeten@rug.ac.be (G. Verstraeten), dirk.vandenpoel@rug.ac.be (D. Van den Poel), michael@cs.uu.nl (M. Egmont-Petersen), patrick.vankenhove@rug.ac.be (P. Van Kenhove), jan.vanthienen@econ.kuleuven.ac.be (J. Vanthienen).

## 1. Introduction

Undoubtedly, customer relationship management (CRM) has gained its importance through the statement that acquiring a new customer is several times more costly than retaining and selling additional products to existing customers [2,20,46]. This simple rule-of-thumb has led to what many authors refer to as 'the paradigm shift in marketing' $[4,25]$, implying that brand strategies are being replaced by customer strategies [3], and more and more voices rise to replace the traditional brand managers by customer (segment) managers [37,47]. Hence, it has become increasingly important to make informed marketing decisions on a customer level, and the customer loyalty of individual consumers has rapidly grown to become the focal point of relationship marketing (see, e.g., [22,31, $40,41])$.

In order to ensure the success of a CRM strategy, it is crucial that customers remain, at least to a certain extent, loyal to the company in case. However, recent research suggests large heterogeneity in terms of spending and spending evolution within the group of long-life customers [44]. Responding to this finding, in the following section of the paper, we elaborate upon the relevance of an accurate indication of a customer's future spending evolution for improving relationship marketing decision making for long-life customers. Consequently, we try to account for the heterogeneity within the group of long-life customers by adding information about estimated future spending evolutions.

In this study, we limit the focus to estimating whether newly acquired customers will increase or decrease their future spending. Whereas, to the best of our knowledge, no published study has attempted to forecast this variable, we argue in the following section that the recently evolving literature around the loyalty issue has motivated us to do so. To this end, we will use and compare different recently developed classification techniques for optimally classifying the customers into
the two relevant groups (i.e. customers with decreasing versus increasing spending). We hereby focus on techniques that besides yielding good classification accuracy also represent the marginal and conditional independence relations between the variables and how they jointly affect the classification decision.

In recent artificial intelligence literature, Bayesian networks have been suggested as probabilistic white-box models that are able to capture even higher-order dependencies between sets of variables. These networks can then also be efficiently adopted for classification purposes. In this paper, we will evaluate and compare several Bayesian network classifiers for the purpose of classifying customers in the binary classification problem at hand. Using the Naive Bayes classifier as a point of origin, we will gradually remove the restrictions put on the network structure and investigate Tree Augmented Naive Bayes classifiers (TANs) followed by completely unrestricted Bayesian network classifiers. Comparisons will be made with statistical and other artificial intelligence techniques. All classifiers will be evaluated by looking at their classification accuracy and the area under the receiver operating characteristic curve (AUROC). The latter basically illustrates the behavior of a classifier without regard to class distribution or misclassification cost, so it effectively decouples classification performance from these factors. Furthermore, we will also look at the complexity of the trained classifiers because from a marketing viewpoint, parsimonious, yet accurate and self-explanatory models are to be preferred.

This paper is organized as follows. In Section 2, we elaborate on the recent literature on relationship marketing that has provided motivation for investigating the predictability of the customer's spending evolution. To this end, we use Bayesian network classifiers which are discussed in Section 3. The design of the study, including both the data set description and the used performance criteria, are presented in Section 4. Section 5 presents the

results of the experiments. Finally, Section 6 concludes the paper.

## 2. Relevance of the estimation of a customer's spending evolution

Advocates of traditional relationship marketing attribute several advantages to loyal customers. Most importantly, these are expected to raise their spending (and contribution to the company) over their relationship with the company in case [43]. In the most optimistic settings, they are said to generate new customers by their positive word-of-mouth [22], ensure diminished costs to serve [31], exhibit reduced consumer price sensitivities [42] and have a salutary impact on the company's employees [43]. Since, from a database-driven approach, customer tenure (i.e. the length of a customer's relationship with a company) has often been used to approximate the loyalty construct [22,44,45], relationship marketing thrives on the idea that raising the length of the customer-company relationship is the main lever for a company's financial success [43].

Nevertheless, in their recent article, Reinartz and Kumar [45] report a series of studies across industries that challenges most claims of the loyalty advocates. In these studies, they have found no evidence to suggest that long-life customers with steady purchase behavior are necessarily cheaper to serve, less price sensitive, or more effective in bringing new business to the company, such as through word-of-mouth referrals. Additionally, in a previous article, Reinartz and Kumar [44] showed that the contributions of long-life customers were generally declining, although the analysis of this issue was not the focus of their discussion. Finally, the authors pointed out that, at least for a noncontractual setting, short-life but high-revenue customers accounted for a sizeable amount of profits for the mail-order company in case [44].

In the article mentioned above, Reinartz and Kumar clearly illustrate the pitfalls involved with spending a large slice of the marketing budget on customers that have been good customers in the past over a short-period of time, yet tend to show a decreasing spending pattern (i.e. customers that
have been labelled 'butterflies') [45]. In the example of a mail-order setting, it is generally known that repurchase behavior can-and has-effectively been modeled by using an (often linear) combination of RFM variables, representing the recency of a customer's last purchase, the average frequency of the customer's purchases and the average monetary value spent on the customer's purchase occasions [12,50]. Hence, the group of customers called 'butterflies', being customers with a high historical monetary value, will tend to be over selected for mailing campaigns [45]. An estimation of the future slope of the customer lifecycle (i.e. a customer's spending evolution) would then likely be able to deliver the required insights to the decision-making process and the understanding of the relationship between the slope and other variables, such as customer spending, might generate rich qualitative information for marketers. For instance, for this group of customers, the company might decide to attempt to improve its return on (direct) marketing investments by shifting its focus from long-term investments to investments or promotions on which a short-term return is possible. Alternatively, the company might even consider abandoning investments in these customers altogether. Thus, in this customer-based view, the a priori knowledge of the slope of the customer lifecycle would be useful information.

In this research study we limit our attention in terms of marketing contribution to proving that it is possible to predict the slope of the customer lifecycle of long-life customers. Accordingly, due to the limitations that are extensively documented in Section 7 of this paper, it is not within the scope of this paper to devise, implement and test an optimal marketing strategy for a specific company in case, nor for an array of companies in industries with different characteristics. In this attempt, we will compare different techniques for the estimation problem, which can in its essential form be transformed into a binary classification problem: 'Will newly acquired customers increase or decrease their spending after their first purchase experiences?'

In the marketing literature, binary classification problems have typically been tackled by using traditional statistical methods (e.g. discri-

minant analysis and logistic regression [2,50]), non-parametric statistical models (e.g. $k$-nearest neighbour [50] and decision trees [49,50]) and neural networks [2,50]. In this paper, we will adopt Bayesian network classifiers which have been recently introduced in the artificial intelligence literature. This is motivated by the fact that Bayesian network classifiers are probabilistic white-box models which facilitate a clear insight into the underlying dependencies pertaining to the domain under study. They are based on solid probabilistic reasoning and offer a great potential for knowledge discovery in data in a marketing context. Unfortunately, despite their attractive properties, their application for business decision making and marketing purposes is still limited. In the following section, we will elaborate on the basic concepts of Bayesian network classifiers and discuss some recently suggested structure learning algorithms.

## 3. Bayesian networks for classification

A Bayesian network (BN) represents a joint probability distribution over a set of discrete, stochastic variables. It is to be considered as a probabilistic white-box model consisting of a qualitative part specifying the conditional (in)dependencies between the variables and a quantitative part specifying the conditional probabilities of the data set variables [36]. Formally, a Bayesian network consists of two parts $B=\langle G, \Theta\rangle$. The first part $G$ is a directed acyclic graph consisting of nodes and arcs. The nodes are the variables $X_{1}, \ldots, X_{n}$ in the data set whereas the arcs indicate direct dependencies between the variables. The graph $G$ then encodes the independence relationships in the domain under investigation. The second part of the network, $\Theta$, represents the conditional probability distributions. It contains a parameter $\theta_{x_{i} \mid \Pi_{x_{i}}}=$ $P_{B}\left(x_{i} \mid \Pi_{x_{i}}\right)$ for each possible value $x_{i}$ of $X_{i}$, given each combination of the direct parent variables of $X_{i}, \Pi_{x_{i}}$ of $\Pi_{X_{i}}$, where $\Pi_{X_{i}}$ denotes the set of direct parents of $X_{i}$ in $G$. The network $B$ then represents the following joint probability distribution:
$P_{B}\left(X_{1}, \ldots, X_{n}\right)=\prod_{i=1}^{n} P_{B}\left(X_{i} \mid \Pi_{X_{i}}\right)=\prod_{i=1}^{n} \theta_{X_{i} \mid \Pi_{X_{i}}}$.
The first task when learning a Bayesian network is to find the structure $G$ of the network. Once we know the network structure $G$, the parameters $\Theta$ need to be estimated. In general, these two estimation tasks are performed separately. In this paper, we will use the empirical frequencies from the data $D$ to estimate these parameters: ${ }^{1}$
$\theta_{x_{i} \mid \Pi_{x_{i}}}=\hat{P}_{D}\left(x_{i} \mid \Pi_{x_{i}}\right)$.
It can be shown that these estimates maximise the log likelihood of the network $B$ given the data $D$ [21]. Note that these estimates might be further improved by a smoothing operation [21].

A Bayesian network is essentially a statistical model that makes it feasible to compute the (joint) posterior probability distribution of any subset of unobserved stochastic variables, given that the variables in the complementary subset are observed. This functionality makes it possible to use a Bayesian network as a statistical classifier by applying the winner-takes-all rule to the posterior probability distribution for the (unobserved) class node [15]. The underlying assumption behind the winner-takes-all rule is that all gains and losses are equal (for a discussion of this aspect see, e.g., [15]). In what follows, we will discuss several structure learning algorithms for developing Bayesian network classifiers.

### 3.1. The Naive Bayes classifier

A simple classifier, which in practice often performs surprisingly well, is the Naive Bayes classifier $[15,30,33]$. This classifier basically learns the class-conditional probabilities $P\left(X_{i}=x_{i} \mid C=c_{l}\right)$ of each variable $X_{i}$ given the class label $c_{l}$. A new test case $\left(X_{1}=x_{1}, \ldots, X_{n}=x_{n}\right)$ is then classified by using Bayes' rule to compute the posterior probability of each class $c_{l}$ given the vector of observed variable values:

$$
\begin{aligned}
& P\left(C=c_{l} \mid X_{1}=x_{1}, \ldots, X_{n}=x_{n}\right) \\
& \quad=\frac{P\left(C=c_{l}\right) P\left(X_{1}=x_{1}, \ldots, X_{n}=x_{n} \mid C=c_{l}\right)}{P\left(X_{1}=x_{1}, \ldots, X_{n}=x_{n}\right)}
\end{aligned}
$$

[^0]
[^0]:    ${ }^{1}$ Note that we hereby assume that the data set is complete, i.e. no missing values.

![img-0.jpeg](img-0.jpeg)

Fig. 1. The Naive Bayes classifier.
The simplifying assumption behind the Naive Bayes classifier then assumes that the variables are conditionally independent given the class label. Hence,
$P\left(X_{1}=x_{1}, \ldots, X_{n}=x_{n} \mid C=c_{l}\right)$

$$
=\prod_{i=1}^{n} P\left(X_{i}=x_{i} \mid C=c_{l}\right)
$$

This assumption simplifies the estimation of the class-conditional probabilities from the training data. Notice that one does not estimate the denominator in expression 3 since it is independent of the class. Instead, one normalises the nominator term $P\left(C=c_{l}\right) P\left(X_{1}=x_{1}, \ldots, X_{n}=x_{n} \mid C=c_{l}\right)$ to 1 over all classes. Naive Bayes classifiers are easy to construct since the structure is given a priori and no structure learning phase is required. The probabilities $P\left(X_{i}=x_{i} \mid C=c_{l}\right)$ are estimated by using the frequency counts for the discrete variables and a normal or kernel density based method for continuous variables [30]. Fig. 1 provides a graphical representation of a Naive Bayes classifier.

### 3.2. Tree Augmented Naive Bayes classifiers

In [21] Tree Augmented Naive Bayes classifiers (TANs) were presented as an extension of the Naive Bayes classifier. TANs relax the independence assumption by allowing arcs between the variables. An arc from variable $X_{i}$ to $X_{j}$ then implies that the impact of $X_{i}$ on the class variable also depends on the value of $X_{j}$. An example of a TAN is presented in Fig. 2. In a TAN network the class variable has no parents and each variable has as parents the class variable and at most one other variable. The variables are thus only allowed to
![img-1.jpeg](img-1.jpeg)

Fig. 2. The Tree Augmented Naive Bayes classifier.
form a tree structure. In [21], a procedure was presented to learn the optional arrows in the structure that forms a TAN network. This procedure is based on an earlier algorithm suggested by Chow and Liu (CL) [11]. The procedure consists of the following five steps.

1. Compute the conditional mutual information given the class variable $C, I\left(X_{i} ; X_{j} \mid C\right)$, between each pair of variables, $i \neq j$. $I\left(X_{i} ; X_{j} \mid C\right)$ is defined as follows:

$$
\begin{aligned}
& I\left(X_{i} ; X_{j} \mid C\right)=\sum_{x_{i}, x_{j}, c_{l}} P\left(X_{i}=x_{i}, X_{j}=x_{j}, C=c_{l}\right) \\
& \quad \times \log \frac{P\left(X_{i}=x_{i}, X_{j}=x_{j} \mid C=c_{l}\right)}{P\left(X_{i}=x_{i} \mid C=c_{l}\right) P\left(X_{j}=x_{j} \mid C=c_{l}\right)}
\end{aligned}
$$

This function is an approximation of the information that $X_{j}$ provides about $X_{i}$ (and vice versa) when the value of $C$ is known.
2. Build a complete undirected graph in which the nodes are the variables. Assign to each arc connecting $X_{i}$ to $X_{j}$ the weight $I\left(X_{i} ; X_{j} \mid C\right)$.
3. Build a maximum weighted spanning tree.
4. Transform the resulting undirected tree to a directed one by choosing a root variable and setting the direction of all arcs to be outward from it.
5. Add the classification node $C$ and draw an arc from $C$ to each $X_{i}$.

We used Kruskal's algorithm in step 3 to construct the maximum weighted spanning tree [32]. In [21], it was proven that the above procedure builds TANs that maximise the log likelihood of

the network given the training data and has time complexity $\mathrm{O}\left(n^{2} \cdot N\right)$ with $n$ the number of variables and $N$ the number of data points. Experimental results indicated that TANs outperform Naive Bayes with the same computational complexity and robustness [21].

### 3.3. General Bayesian Network classifiers

Many algorithms have been proposed that can learn the structure of a General Bayesian Network (GBN) from a set of (complete) data [5,29]. Some algorithms impose restrictions onto the direction of the arcs that connect the nodes whereas other algorithms omit such restrictions. In this paper, we use the learning algorithm of Cheng et al. [7,9], which assumes an a priori ordering of the variables. Before we discuss the different steps of this algorithm, we first elaborate on the concept of $d$ separation because this plays a pivotal role in the structure learning algorithm.

Let $X, Y$ and $Z$ be mutually disjoint sets of nodes in a directed acyclic graph $G$. The set $Y$ is said to $d$-separate the sets $X$ and $Z$ in $G$ if for every node $X_{i} \in X$ and every node $X_{j} \in Z$, every chain (of any directionality) from $X_{i}$ to $X_{j}$ in $G$ is blocked by $Y$ [51]. We say that a chain $s$ is blocked by a set of nodes $Y$ if $s$ contains three consecutive nodes $X_{1}$, $X_{2}, X_{3}$, for which one of the following conditions holds [51]:

1. $\operatorname{arcs} X_{1} \leftarrow X_{2}$ and $X_{2} \rightarrow X_{3}$ are on the chain $s$, and $X_{2} \in Y$
2. $\operatorname{arcs} X_{1} \rightarrow X_{2}$ and $X_{2} \rightarrow X_{3}$ or $X_{1} \leftarrow X_{2}$ and $X_{2} \leftarrow X_{3}$ are on the chain $s$, and $X_{2} \in Y$;
3. $\operatorname{arcs} X_{1} \rightarrow X_{2}$ and $X_{2} \leftarrow X_{3}$ are on the chain $s$ and $X_{2}$ and the descendants of $X_{2}$ are not in $Y$.

It can be shown that if sets of variables $X$ and $Z$ are $d$-separated by $Y$ in a directed acyclic graph $G$, then $X$ is independent of $Z$ conditional on $Y$ in every distribution compatible with $G[24,52]$. It is precisely this property that will be exploited in the algorithm of Cheng to learn the Bayesian network structure.

The algorithm consists of four phases. In a first phase, a draft of the network structure is made based on the mutual information between each
pair of nodes. The second and third phase then add and remove arcs based on the concept of $d$ separation and conditional independence tests. Finally, in the fourth phase, the Bayesian network is pruned and its parameters are estimated.

The algorithm proceeds as follows [7,9].

## Phase 1: Drafting

1. Initiate a graph $G(X, A)$ where $X=\left\{X_{1}\right.$, $\left.X_{2}, \ldots, X_{n}, C\right\}$ and $A=\{ \}$. Initiate two empty ordered sets $S$ and $R$.
2. Compute the (non-parametric) mutual information $I\left(X_{i} ; X_{j}\right)$ between each pair of variables where $X_{i}, X_{j} \in X, i \neq j . I\left(X_{i} ; X_{j}\right)$ is defined as follows:

$$
\begin{aligned}
I\left(X_{i} ; X_{j}\right)= & \sum_{x_{i}, x_{j}} P\left(X_{i}=x_{i}, X_{j}=x_{j}\right) \\
& \times \log \frac{P\left(X_{i}=x_{i}, X_{j}=x_{j}\right)}{P\left(X_{i}=x_{i}\right) P\left(X_{j}=x_{j}\right)}
\end{aligned}
$$

The mutual information $I\left(X_{i} ; X_{j}\right)$ is the amount of information gained about $X_{i}$ when $X_{j}$ is known, and vice versa $\left(I\left(X_{i} ; X_{j}\right)=\right.$ $I\left(X_{j} ; X_{i}\right)$ ). Hence, $I\left(X_{i} ; X_{j}\right)=0$ if and only if $X_{i}$ and $X_{j}$ are independent.
3. Sort all pairs of nodes where $I\left(X_{i} ; X_{j}\right)$ is greater than $\epsilon$ from large to small and put them into an ordered set $S$. In our experiments, we set $\epsilon=0.008$ which is an appropriate value for large data sets [9].
4. Add arcs to $A$ according to the first two pairs of nodes in $S$ and remove them from $S$. The direction of the arcs is decided by the a priori node ordering.
5. Get the first pair of nodes remained in $S$ and remove it from $S$. If there is no open path between the two nodes, add the corresponding arc to $A$. Otherwise, add the pair of nodes to the end of an ordered set $R$. Note that an open path is a chain with no collider nodes whereby a collider node is a node having two incoming arcs.
6. Repeat step 5 until $S$ is empty.

## Phase 2: Thickening

7. Get the first pair of nodes in $R$ and remove it from $R$.

8. Find a cut-set that can $d$-separate these two nodes in the current network. Use a conditional independence test (see Eq. (5)) to see if these two nodes are conditionally independent given the cut-set and using a threshold value of 0.008 . If so, go to the next step, otherwise, connect the pair of nodes by an arc.
9. Repeat step 7 until $R$ is empty.

## Phase 3: Thinning

10. For each arc in $A$, if there are other paths besides this arc between the two nodes, remove this arc from $A$ temporarily and find a cut-set that can $d$-separate the two nodes in the current network. Use a conditional independence test to see if the two nodes are conditionally independent given the cut-set and again using a threshold value of 0.008 . If so, remove the arc permanently, otherwise add the arc back to the network.

Phase 4: Prune and learn the parameters of the Bayesian network classifier
11. Find the Markov Blanket of the classification node. The Markov Blanket of a node $X_{i}$ consists of the union of $X_{i}$ 's parents, $X_{i}$ 's children and the parents of $X_{i}$ 's children [36].
12. Delete all the nodes that are outside the Markov Blanket.
13. Learn the parameters of the conditional probability tables and output the Bayesian network classifier.

Note that in steps 8 and 10, it is important to find cut-sets that are as small as possible in order to avoid conditional independence tests with large condition sets. In [1], a correct algorithm is presented to find minimum cut-sets between two nodes. In this paper, we will use the heuristic algorithm suggested by Cheng et al. [7].

It can be shown that when the values of the variables in the Markov Blanket of the classification node are observed, the posterior probability distribution of the classification node is independent of all other variables (nodes) not in the Markov Blanket [34]. Hence, in step 12, all vari-
ables outside the Markov Blanket can be safely deleted because they will have no impact on the classification node and thus will not affect the classification accuracy. In this way, the Markov Blanket results in a natural form of variable selection.

Note that this algorithm requires $\mathrm{O}\left(N^{2}\right)$ mutual information tests and is linear in the number of cases $N$. An extension has been presented in [8] in case no node ordering is given. In this paper, we will simply treat the classification node as the first node and order the other nodes based on their correlation with the classification node from large to small.

### 3.4. Multinet Bayesian network classifiers

Both TANs and GBNs assume that the relations between the variables are the same for all classes. A multinet Bayesian network allows for more flexibility and is composed of a separate, local network for each class and a prior probability distribution of the class node [10,21,23,28]. Thus, for each value $c_{i}$ of the classification node $C$ a Bayesian network structure $B_{i}$ is learned. The multinet $M$ then defines the following joint probability distribution:
$P_{M}\left(C, X_{1}, \ldots, X_{n}\right)=P_{C}(C) \cdot P_{B_{i}}\left(X_{1}, \ldots, X_{n}\right)$.
A new instance is then assigned to the class that maximises the posterior probability $P_{M}\left(C \mid X_{1}, \ldots\right.$, $X_{n}$ ) conform the winner-takes-all rule. Since we have
$P_{M}\left(C \mid X_{1}, \ldots, X_{n}\right)=\frac{P_{M}\left(C, X_{1}, \ldots, X_{n}\right)}{P_{M}\left(X_{1}, \ldots, X_{n}\right)}$,
and the denominator is the same for all classes, we can assign the instance to the class that maximises the value of Eq. (7). The term $P_{C}(C)$ may then be estimated by the empirical frequency of the class variable in the training set $\hat{P}_{D}(C)$. Note that for multinet classifiers the number of parameters that need to be estimated per training instance inevitably increases. As the parameters are estimated from a limited number of instances, learning a separate multinet structure per class instead of one overall structure results in more unreliable parameter estimates and, hence, a higher probability of

overgeneralization. This effect is closely related to the so-called peaking phenomenon, for a discussion see, e.g., [53].

In this paper, we consider both CL multinets and GBN multinets. CL multinets are multinets which are built using the procedure of Chow and Liu [11]. This is essentially the same procedure as the one outlined in Section 3.2 with the exception that step 5 is now omitted and in step 1 the conditional mutual information is replaced by the mutual information (see Eq. (6)). This procedure is then executed separately for each value $c_{i}$ of the class node $C$ using only the training data $D_{i}$ whereby $D_{i}$ contains all instances of $D$ for which $C=c_{i}$. The resulting multinet then consists of an ensemble of tree structured Bayesian networks. The GBN multinets are trained using the approach of Cheng discussed in Section 3.3 with the exception that the classification node is now omitted in the structure learning phase. Again, the algorithm is executed for each class on the corresponding training data.

## 4. Design of the study

### 4.1. Data set

We conducted our research on UPC scanner data of a large Belgian DIY (Do-It-Yourself) retail chain. The data we used for our models were all gathered by the customer loyalty cards, which have been in use since January 1995. Due to some restrictions (cf. infra), we were able to use four complete years of information.

Since we are interested in examining the behavior of long-life customers, we imposed three conditions on the data: firstly, we only used customers who started purchasing before February 1997. Secondly, to ensure the data was not leftcensored (i.e. to ensure the customers in our database really started their relationship with the company at the time of our first observation), we only used information of customers who had not purchased before. We thus used the first two years of information in the customer database only to check that the customers in our sample were new customers. Thirdly, using a database containing
eight six-month periods of information for all customers of the company, we have selected all customers who purchased in five or more periods. Hence, we arrived at a database containing an approximate sample of the company's long-life customers. In order to assess the quality of our models, we have randomly divided the database into two parts. While $2 / 3$ of the observations were used for learning the classifiers, the remaining $1 / 3$ was used as a test set for estimating the generalization behavior of the classifiers. Table 1 displays the characteristics of our data set.

By performing a linear regression model on the historical contributions of each customer, we were able to capture the slope of the lifecycle of each individual customer. This slope, after being discretised into positive or negative to represent increasing or decreasing spending, was henceforth used as the dependent variable in the study (SlopeSign). It is interesting to note that the finding of Reinartz and Kumar that the slope of longlife customers was generally decreasing [44] was validated in our study by the fact that only $28 \%$ of those customers in the database exhibited a positive slope. In this case, we have used a set of 15 continuous variables computed on the first six months of information, in order to predict the sign of the evolution of the customer's contribution (i.e. the customer lifecycle) for the remaining 42 months of the relationship. While the variables computed are presented in Table 2, the time schedule is given in Fig. 3.

The independent variables can be divided into four major logical groups. A first group of variables is constructed to measure the volume of the purchases the subject made during his or her first six months as a customer. These contain TotCont, TotRev, NumbArt and NumbTick. Note that the variable TotCont represents the intercept of the customer lifecycle. It is merely the first of the eight

Table 1
Data set characteristics


Table 2
Variables used in the study


data points forming the customer lifecycle. While this first set of attributes can be regarded as the "depth" of the customer purchases, the second group of variables contains the variables that measure the "broadness" of the purchases. These are DiffCat, DiffProd and MaxPerc. The latter variable contains the percentage of products bought in the product category in which the customer has bought most of his or her products. In this way, it can be seen as a skewness indicator, a large indicator meaning that the customer only buys a certain category of products from the company. A third group of variables captures the 'bargaining tendency' and 'price sensitivity' of the customer. The relevant variables here are PercDisc, ArtDisc, MeanMarg, MeanPrice and MaxPrice. Finally, three measures are introduced to value evolutions within the first six months. These are Lifec6m, LastCont and DateMaxPrice.

In order to train the Bayesian network classifiers, we discretised all variables by using the discretisation algorithm of Fayyad and Irani with the default options [19]. This algorithm uses an information entropy minimisation heuristic to
discretise the range of a continuous-valued attribute into multiple intervals. This discretisation procedure was performed using the Java Weka workbench. ${ }^{2}$ Table 3 depicts how the attributes in our data set were discretised into intervals.

### 4.2. Performance criteria for classification

The performance of all trained classifiers will be quantified using both the classification accuracy and the AUROC. The classification accuracy is undoubtedly the most commonly used measure of performance of a classifier. It simply measures the percentage of correctly classified (PCC) observations. However, it tacitly assumes equal misclassification costs and balanced class distributions [38]. The receiver operating characteristic curve (ROC) is a two-dimensional graphical illustration of the sensitivity ('true alarms') on the $Y$-axis versus 1-specificity on the $X$-axis ('false alarms') for various values of the classification threshold [16,48]. It basically illustrates the behavior of a classifier without regard to class distribution or misclassification cost. The AUROC then provides a simple figure-of-merit for the performance of the constructed classifier. An intuitive interpretation of the AUROC is that it provides an estimate of the probability that a randomly chosen instance of class 1 is correctly rated (or ranked) higher than a randomly selected instance of class 0 [26].

We will use McNemar's test to compare the PCCs of different classifiers [17]. This chi-squared test is based upon contingency table analysis to detect statistically significant performance differences between classifiers. In [14], it was shown that this test has acceptable Type I error which is the probability of incorrectly detecting a difference when no difference exists. While Hanley and McNeil described a method for comparing ROC curves derived from the same sample [27], De Long et al. [13] developed a non-parametric chisquared test by using the theory on generalized $U$ statistics and the method of structural components to estimate the covariance matrix of the AUROC. Hence, we will use the latter test to detect

[^0]
[^0]:    ${ }^{2}$ http://www.cs.waikato.ac.nz/ml/weka/.

![img-2.jpeg](img-2.jpeg)

Fig. 3. Time schedule of our empirical study.

Table 3 Discretisation of the attributes


statistically significant AUROC differences between classifiers.

## 5. Results

We compared and contrasted the performance of the Naive Bayes, TAN, CL multinet, GBN, GBN multinet, C4.5, C4.5rules, linear discriminant analysis (LDA) and quadratic discriminant analysis (QDA) classifiers on our marketing data set. We included the decision tree induction algorithm C4.5 and its rules variant, C4.5rules, because they are also white-box classifiers giving besides a classification decision also a clear explanation why the particular classification is being made [39]. LDA and QDA were included because they are well-known benchmark statistical classifiers. To train the Naive Bayes, TAN, and CL multinet classifiers, we used the Matlab toolbox of Kevin Murphy [35]. For the GBN and GBN multinet classifiers, we used the PowerPredictor software of Cheng [6]. Table 4 depicts the classification accuracy of all classifiers on both the training and test set. The best test set performance is in bold face and underlined and those not statistically different from it according to McNemar's test (using a significance level of $5 \%$ ) are in bold face. The GBN classifier achieved the highest classification accuracy on the test set. The classification accuracy of the TAN, C4.5 and LDA classifier was not statistically different from it. Table 5 depicts the AUROC of all classifiers and has the same setup as Table 4. Note that for the Bayesian network classifiers, the LDA and QDA classifier, the calculation of the AUROC values poses no problems since each of these classifiers yields class probabilities. For C4.5, we use the confidence at the

Table 4
Classification accuracy of the Bayesian network classifiers versus C4.5 and discriminant analysis


Table 5
Area under the receiver operating curve of the Bayesian network classificiers versus C4.5 and discriminant analysis


leaves as the class probability. For C4.5rules, we used the confidence of the first rule of the ordered C4.5rules rules set (ordered by class and then by confidence) that matches the instance as its class probability. In [18], it was shown that this is a feasible strategy for computing the AUROC of C4.5rules. Table 5 clearly indicates that the LDA classifier gave the best AUROC performance. However, there is no significant difference with the AUROC performance of the GBN and Naive Bayes classifier according to the test of De Long et al. and again using a significance level of $5 \%$. Observe from Tables 4 and 5 that both multinet classifiers, QDA and C4.5rules never achieved good performance in terms of PCC and AUROC. Note that for all Bayesian network classifiers, we also investigated the impact of smoothing the parameter estimates. However, no significant performance increase in terms of either the PCC or AUROC values were found with parameter smoothing.

Besides looking at the classification performance, we also investigated the complexity of the generated classification models because from a marketing viewpoint, easy to understand, parsimonious models are to be preferred. Table 6 presents the complexity of the generated Bayesian network and C4.5(rules) classifiers. We did not include LDA and QDA because they are basically mathematical models which give a rather limited insight into the relationships and patterns present in the domain under study. The Naive Bayes and TAN network classifiers did not prune any attributes because all attributes remained in the Markov Blanket of the classification node. The TAN added 14 arcs to the Naive Bayes classifier which resulted in a performance increase in terms of PCC (from 72.5 to 74.0 ) but a performance decrease in terms of AUROC (from 74.3 to 73.6). Hence, the effect of the added complexity was rather marginal in our case. Although the GBN multinet classifier seems attractive because of its simple structure, its performance according to Tables 4 and 5 was rather bad. Also the CL multinet classifier gave bad performance and has on top a complex structure. The tree induced by C4.5 is not easy to handle and interpret because of its large number of internal and leave nodes. Moreover, the C4.5 tree was able to prune only 2 of the 15 attributes. The rule set inferred by C4.5rules contains 18 rules. This might seem interesting but when considering Tables 4 and 5 the performance of C4.5rules in terms of both PCC and AUROC was rather bad. Note that while the C4.5 tree pruned two attributes, the

Table 6
Complexity of the Bayesian network classifiers and C4.5


C4.5rules rules set still contained all attributes. This can be explained by the fact that C4.5rules starts generating and pruning the rules from the unpruned C4.5 tree. The GBN classifier was able to prune 12 attributes, leaving only three attributes in the model. Only six arcs where necessary to efficiently model the dependencies between the attributes and the classification node. Furthermore, it gave also a very good performance in terms of PCC and AUROC on the test set. The structure of the GBN classifier is depicted in Fig. 4.

This figure clearly illustrates that it is a compact, parsimonious and yet powerful model for decision making. By using only three variables compiled from purchase records of the first six months of the customer lifecycle, we have provided evidence that, in our DIY case, the SlopeSign of a lifecycle of 48 months can be predicted with a classification accuracy of $75 \%$. The total contribution of the client (TotCont), the total number of articles bought (NumbArt) and the maximum percentage of products bought in one product family (MaxPerc) proved to be very powerful predictors for the sign of the customer lifecycle slope when using GBN classifiers. While the first two variables present a measure of the volume of the purchases made (the purchase "depth"), the latter variable is an estimator of the variety of product families bought (the purchase "broadness").

The knowledge that these variables are intensely related to the slope's evolution can be useful for marketing decision makers. In this Belgian DIY retail setting, the initial monetary amount spent at the company (TotCont) and the initial number of
![img-3.jpeg](img-3.jpeg)

Fig. 4. Unrestricted Bayesian network constructed for marketing case.
articles purchased (NumbArt) were found to be negatively related to the SlopeSign, whereas the maximum percentage of products purchased in one category (MaxPerc) was found to be positively related to the SlopeSign. This implies that customers that tend to increase their spending over their lifetime with the company initially spend less money on a lower number of articles, purchasing from a smaller set of product categories. Alternatively, customers spending a lot of money initially on a lot of articles and who purchase products across a lot of different categories tend to decrease their spending in the future. This information may prove valuable for the company in this case as a starting point for investigating why high-spending customers generally decrease their spending over time.

To conclude, we can state that Bayesian network classifiers are performing well in predicting the future customer evolution and are able to contribute to an increased understanding of the relationship between the investigated variable and the most relevant explanatory variables. Hence, we have reached our goal to illustrate that Bayesian network classifiers can be considered to be a useful tool in the toolbox of marketing analysts in this application of identifying the slope of the customer lifecycle of long-life customers.

## 6. Conclusions

In the theoretical part of this paper, we have argued that long-life/loyal customers have been regularly regarded as a homogeneous group of the most profitable customers of a company. Building on more recent findings, in this study, we have tried to acknowledge the heterogeneity in the group of long-life customers by dividing the group into two subparts, essentially consisting of customers increasing versus decreasing their spending over their relationship with the company in case. Hence, it was the goal of this study to predict the sign of the slope-being the output of the estimation of a linear customer lifecycle-at the individual customer level using Bayesian network classifiers based on information from initial purchase occasions.

Bayesian network classifiers have been recently proposed in the artificial intelligence literature as probabilistic white-box models which allow to give a clear insight into the relationships between the variables of the domain under study. Starting from the Naive Bayes classifier, we gradually removed the restrictions put on the network structure and investigated TANs and GBN classifiers. The latter were learnt using the algorithm of Cheng et al. We compared the classification accuracy and the AUROC of all Bayesian network classifiers with discriminant analysis and the widely used C4.5 and C4.5rules algorithms. It was shown that general, unrestricted Bayesian network classifiers have a good performance in terms of both measures. Furthermore, using the Markov Blanket concept allowed us to prune a lot of attributes resulting in a compact, parsimonious, yet powerful Bayesian network classifier for marketing decision making.

In summary, we contribute to the literature by providing experimental evidence that: (1) Bayesian network classifiers offer an interesting and viable alternative for our customer lifecycle slope estimation problem; (2) the Markov Blanket concept allows for a natural form of attribute selection that was very effective for the case at hand; (3) the sign of the slope can be predicted with a powerful and parsimonious GBN classifier; (4) a set of three variables measuring the volume of initial purchases and the degree to which customers originally buy in different categories, are a powerful set of predictors for estimating the sign of the slope.

## 7. Practical implications and issues for further research

While it has been the focus of this paper to demonstrate (i) the predictability of the sign of the slope and (ii) the performance of several Bayesian network classifiers versus statistical and other artificial intelligence techniques, here, we elaborate on possible applications of the knowledge of the sign of the slope for relationship marketing decision making. A number of future applications lie ahead. Firstly, the sign of the slope might prove to be a useful indicator in the decision upon the type or strength of the marketing investment that can
be used vis-à-vis a certain consumer. For example, a company organizing a membership club, with special service offerings, special promotions, etc. might only want to deliver these benefits to consumers that are worthy of such a large investment. Thus, knowing that certain consumers will decrease their spending might be important for improving the return on the relationship marketing investment. Alternatively, a company might have two marketing incentives of unequal cost (e.g. a special promotion versus a small gift). Also in this case, it could be useful to assess the future spending of a customer in order to allocate the desired incentive to each customer. Secondly, the estimations may be used in an aggregated way, as a monitor of e.g. customer-acquisition policies. In this way, the percentage of customers that are expected to raise their spending in the future can be compared for different acquisition strategies and campaigns in order to select those target markets with higher potential for establishing enduring relationships. An additional benefit is derived from the fact that it was possible to predict the evolutions very early in the relationships, so acquisition campaigns can be evaluated in a timeeffective way. Thirdly, the estimations might be used as a dimension for designing an a priori segmentation scheme for a company's customer base. Hence, it might be feasible to delineate a more customized customer strategy per segment. Two possible applications are summarized in Fig. 5. In the first segmentation scheme (a), the sign of the slope is used together with the tenure of customers in order to decide upon the relevant marketing message content and size. Whereas short-life customers only merit investments that can be regained during their limited relationship with the company, long-life customers might effectively be reached through more expensive marketing programs. For customers who are expected to increase the relationship with the company (who are likely to be more satisfied with the company in case) it might be beneficial to offer additional products according to their detected needs (detected e.g. through a cross-selling analysis) or extra value (e.g. through the membership to a club). Alternatively, customers who are expected to decrease their spending might be appropriately

![img-4.jpeg](img-4.jpeg)

Fig. 5. Summary of possible a priori segmentation schemes.
managed with a retention program (e.g. focused on complaint detection and complaint handling). In the second segmentation scheme (b), the intercept and the slope of the customer lifecycle are used to delineate the segmentation. Also in this case, argumentation could be found to use specific marketing strategies to target the segments, where it could be argued that not all segments merit targeting (e.g. the segment of customers that starts as low-spending customers and are expected to decrease their spending even further).

The desired outcome of this line of research could consist in suggesting an optimal CRM strategy to different segments. However, in order to test the optimality of the proposed strategies, one would have to design and implement an experiment allocating strategies randomly to customers. It can be argued that several important practical problems would arise when attempting to implement such a study.

Firstly, a company that has not been performing a broad range of different CRM strategies would have to make large marketing investments in designing an appropriate tactic for each strategic goal (e.g. customer retention through satisfaction research, complaint handling, or other tactics). Secondly, and crucially, for optimally allocating a customer to a strategy, it would be necessary to assign a sizeable part of the customer base randomly to each of the strategies, implying that by definition, customers will be targeted with strategies that are inappropriate for them, implying large marketing expenses with low return on
investment, confused and unsatisfied customer responses, especially within the group of highspending customers that has been proven to expect preferential (or at least reasonable) treatment compared to other customers [45]. While this experimental setting would likely provide rich information to researchers, the costs involved are, especially while marketing management is aware of the long-term potential of customers, of a magnitude that is not acceptable to managers. Thirdly, even if a company would be interested in researching such an optimal segmentation scheme, the generalization capacity would probably be low, considering the specificity of the tactics used. Hence, the scientific outcome of the study might only be reached when validated with several tactics for each strategy, driving the required investments even further. Finally, in order to assess the effect of the approach, the results of the study can only be expected after several years, in order to measure the changes in the slope of the customer lifecycle. The four factors mentioned above all add to the difficulties of funding, designing and implementing an optimal experimental study.

Further research is needed in two major directions. In the domain of marketing, the creation of variables having still better predictive capabilities for predicting the sign of the slope of the linear lifecycle is an interesting research topic. Alternatively, a replication of this study over different customer bases in diverse industries and countries might deliver an insight into the stability of the findings. Eventually, if resources would be

available, testing and comparing different strategies (e.g. the frameworks presented in Fig. 5) 'in-the-field' can determine the full potential of the usage of customer spending evolutions for marketing decision making. Considering the Bayesian network classifiers, additional research is needed to investigate the power of other structure learning algorithms. Also the presence of hidden variables in the Bayesian network forms an interesting topic for further research.
