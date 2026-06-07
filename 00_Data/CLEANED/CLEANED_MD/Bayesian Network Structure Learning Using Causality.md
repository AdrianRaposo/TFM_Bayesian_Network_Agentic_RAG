# Bayesian Network Structure Learning Using Causality 

Zhen Xu and Sargur N. Srihari<br>University at Buffalo, The State University of New York, USA<br>zxu8@buffalo.edu, srihari@cedar.buffalo.edu


#### Abstract

Bayesian Networks are probabilistic models of data that are useful to answer probabilistic queries. Since they are usually built by hand, algorithms to automatically learn their structure are lacking, particularly for large data sets encountered today. Existing algorithms use either local measures of deviation from independence or global likelihood measures. We tackle this problem from a new perspective using causality, which is a stronger measure than correlation. Integrating both the global and local views, the proposed algorithm learns a high quality Bayesian network without using any score-based searching. Given a partial directed acyclic graph, causal pairs with the highest accuracy are inferred with the fewest number of pairwise causal inferences. Specifically, with discrete data, the $\chi^{2}$ statistical test is used to identify the most dependent and possible causal pairs. Furthermore, the learned causality is forward-propagated. Experiments on handwriting data show that, besides the ability of causal inference, our algorithm performs better than two previous algorithms, one based on branch-and-bound search, and the other a greedy algorithm using $\chi^{2}$ tests and a log-loss function. The learned structure not only has lowest loss in representing the data, but also reveals underlying causal relationships which are useful for scientific discovery.


## I. INTRODUCTION

Bayesian Networks (BNs) are probabilistic graphical models that represent joint distributions of a set of variables efficiently in a factorized way [1]. A BN is a directed acyclic graph where nodes represent variables and directed edges represent dependency relationships. BNs are widely used in diagnosis, troubleshooting, data mining, etc; some examples are pathologist diagnose lymph node pathologies [1], printer troubleshooting and automobile troubleshooting [2]. Their advantages are in providing a relationship between variables that is easy to understand and in providing a compact form where the amount of data needed to represent the full joint distribution is reasonable.

BNs are largely constructed manually based on expert knowledge. Their use is to infer answers to probabilistic queries. However, with dynamically changing data sets it is useful to automatically learn their structures from data. BNs structure learning is a very active research area, which has three main approaches:

- The constraint-based approach [3], [4] finds a set of conditional independencies and learn the structure of BNs that admit these independencies. Since independencies are only partial properties of the data set, the constraint-based approach usually cannot learn the full structure.
- The score-based approach [1], [5]-[8] searches the
graph space and find the BN structure with the highest score. It is a model selection problem. Because the search space contains a super-exponential number of structures, the search problem is NP-hard [9] and many heuristic algorithms have been proposed.
- The Bayesian model averaging approach generates and averages a set of possible BN structures. Since the number of possible structures can be exponential, some approximation algorithms are devised.

We tackle this problem from a more interesting and fundamental perspective. Roughly speaking, the relationships between two variables are either independent or correlated. The correlation comes either from direct cause and effect relationship between these two variables or from the common cause of these two variables. Instead of using correlation to learn BNs structures the same way as traditional algorithms, we want to use causation to learn the BNs structures. Because causality is more fundamental than correlation, in common sense, the learned structure should be more natural and stable. In addition, it can be served as a good source for scientific discovery. Researchers can search and validate the underlying causality revealed by the learned structure.

## II. BN STRUCTURE LEARNING

A BN structure captures independencies that exist in the data to reduce the complexity of the probabilistic model. Methods to construct BNs use a deviation measure from independence and a score function.

## A. Deviation Measure

An independence test is used to test independency between two variables given observations. For categorical variables we can use Pearson's Chi-squared test to test the null hypothesis of independence. It is a goodness-of-fit test which measures the difference between observed frequency distribution and a theoretical distribution. For two multinomial variables $A$ and $B$ with distributions $P\left(A=a_{i}\right)$ and $P\left(B=b_{i}\right)$, and a data set $\mathcal{D}$ with M samples, we define $O\left[a_{i}, b_{j}\right]$ is the observed number of samples that $A=a_{i}$ and $B=b_{i}$, and $E\left[a_{i}, b_{j}\right]=$ $M P\left(a_{i}\right) P\left(b_{j}\right)$ is the expected number of samples. The $\chi^{2}$ test can be defined as:

$$
\chi^{2}(\mathcal{D})=\sum_{i, j} \frac{\left(O\left[a_{i}, b_{j}\right]-E\left[a_{i}, b_{j}\right]\right)^{2}}{E\left[a_{i}, b_{j}\right]}
$$

The bigger test value indicates more dependency between two variables.

## B. Score Function

One popular score function for BN learning is the negative log-likelihood, which is known as log-loss [1]. Given a data set $\mathcal{D}$ with $N$ i.i.d samples, the log-loss is defined as:

$$
l(\mathcal{D} \mid G)=-\sum_{i=1}^{n} \sum_{j=1}^{N} \log P\left(x_{i}[j] \mid \mathbf{x}_{\mathbf{p a}_{(1)}}[j]\right)
$$

where $x_{i}[j]$ is the value of the $i_{t h}$ variable (feature) in the $j_{t h}$ sample and $\mathbf{x}_{\mathbf{p a}_{(1)}}[j]$ are values of parents of $x_{i}$ in the $j_{t h}$ sample. It is the loss in terms of using the model to represent the true probability distribution. Since log-probabilities are negative the measure has the convenience of being a positive number.

This score is used by the B \& B algorithm and the greedy algorithm described next, but not by the proposed causal algorithm. It is only used to compare the the quality of the resulting structure, as described in section VI.

## C. Baseline Algorithms

Here we give brief descriptions of two BN structure learning algorithms used to benchmark the performance of the proposed algorithm (Section VI).

1) Branch and bound (B \& B) algorithm: This algorithm is a score-based approach, which leverages some useful properties of the scoring function to reduce the time and memory costs [10]. Specifically, it uses the minimum description length (MDL) as the score function, which is defined based on logloss and has the desirable decomposable property. Using this property, it builds cache in $O\left(n \cdot 2^{n}\right)$ time, where $n$ is the number of variables, to avoid redundant computation of logloss scores. The branch and bound approach makes it an any-time algorithm that can stop at the current best solution while showing an upper bound to global optimum. The time complexity of this algorithm is mainly bound to the cache constructing time. The experiment results are very good for both randomly generated data sets and certain public data sets.
2) Greedy algorithm: This uses both the local deviance measure of independence and global log-loss score [11]. It adds and orients one edge at a time while using $\chi^{2}$ statistics to set the order and log-loss score to decide the orientation. The time complexity of this algorithm is $O\left(c \cdot 2^{q}\right)$, where $n$ is the number of variables and $q$ is the maximum number of parents. Experiments on handwritten data show its good performance. Compared with these two algorithms, our algorithm does not use any global score in the process of structure learning. The log-loss score is only computed with learned BN structure in order to compare the performance among all three algorithms. Because causation is the most important and fundamental factor in correlation, the causal inference is sure to learn a good BN structure, that indirectly implies a good log-loss score. Our experiments in section VI show that the score for learned structure can even be better.

## III. CAUSALITY

Broadly speaking, two variables are either independent or correlated. Two variables are independent means the occurrence of one does not influence the probability of the
![img-0.jpeg](img-0.jpeg)

Fig. 1: The possible relationships between events A and B. (a) A is independent with B; (b) A causes B; (c) B causes A; (d) A and B has a common cause, yet they do not cause each other.
other. While two variables are correlated means there is a dependency relationships between these two. Particularly, the causation describe the causal and effect relationship between two variables. There are four possible relationships between two variables A and B [12]: A is independent with B; A causes B; B causes A; A and B are effects of a hidden common cause C, but they do not cause each other [13], as showed in Fig. 1. The independence is illustrated in Fig. 1(a). The correlation includes Fig. 1(b)-(d), while the causation includes Fig. 1(b),(c). from these figures, we can see the causation is more fundamental than correlation and correlation is a broader concept than causation. In most cases, correlation is a good hint to find the causation. While there are many standard statistical independence test to differentiate independency and correlation, it is hard to determine the causation. There are two directions of causal inference from global and local perspectives.

Observe that both causation and correlation are dependent relationships which can be excluded if two variables are independent. PC algorithm [14], which is named by inventors' initials, adopts the constraint-based approach to learn a partial directed acyclic graph (PDAG) which contains directed and undirected edges. This algorithm mainly contains two phases including edge-deleting and edges-orienting. It begins from an undirected complete graph and utilizes the independence test to delete edges. For example, if $X$ and $Y$ are independent, then it deletes edge $X-Y$. If $X \mid Z$ is conditional independent with $Y \mid Z$, then it deletes $X-Y$. The edge orienting phase mainly leverages the v-structure and DAG constraints. For example, if there are two edges $X-Y$ and $Y-Z, X$ is independent with $Z$ while $X \mid Y$ is not conditional independent with $Z \mid Y$, then it orients $X \rightarrow Y \leftarrow Z$. Apply the same procedure until there are no more edges can be oriented by v-structure and DAG constraints, and output the corresponding PDAG, which will still leave lots of edges undirected. The output of this algorithm contains lots of uncertainty and they confined the usefulness of the results for answering probabilistic queries and making predictions. On the other hand, the model-based approaches [15]-[18] infer the causality between two variables by modeling the data generating process. These approaches model the effect variable as a function of the cause variable and the additive noise. In order to break the symmetry and infer the causal relationship between two variables, they made some assumptions such as non-Gaussian noise, non-invertible functional relationship, etc. If the modeled functional relationship is the same as the real data generating process, then the additive noise should be independent with the cause variable. The limitations of model-base approaches come from high

computation complexity. It is only feasible to a very small graph and suffers from multiple hypothesis testing problem.

## IV. Proposed Method

The global and local views of causal inference can be combined to design a computationally efficient BN structure learning algorithm. At the beginning, the constraint-based approach is used to identify the PDAG efficiently, which contains a set of directed and undirected edges. The modelbased approach can be used to orient the undirected edges. This is a non-trivial task, because different undirected edges have different causal inference difficulties and accuracies, and they carry different amount causal information which can be used to orient other undirected edges. We need to decide the right order to orient undirected edges and the appropriate way of, With the intuition that the causation is a stronger dependent relationship, we use the $\chi^{2}$ statistical tests [19] to sort the undirected edges by their dependencies. After identifying the undirected edge with highest dependency, we use the model-based approach to causally orient this edge. with this extra piece of causal information, we apply the causal forward propagation algorithm to other undirected edges which can be oriented further. We repeat this procedure until all edges are causally oriented. Our algorithm uses both the efficiency and stability of the constraint-based method and the causal inference power of the model-based approach to find a BN with small uncertainty. The causal forward propagation algorithm can significant decrease the number of pairwise causal inference and thus save a lot of computations. Moreover, always choosing variable pair with highest dependency improves the accuracy because in common sense the strongest dependency signifies the causality which can be easily identified.

## A. Nonlinear Additive Noise Model

The nonlinear additive noise model [16] assumes the nonlinear causal relationship between cause and effect variables. It assumes non-invertible functional relationships between variables to break the symmetry and identify the causality. It models the data generating process as:

$$
x_{i}=f\left(\mathbf{x}_{\mathbf{P a}_{(i)}}\right)+e_{i}
$$

where $f$ is an arbitrary non-invertible function, $\mathbf{x}_{\mathbf{P a}_{(i)}}$ is a vector containing all the parents of $x_{i}$, and independent noise variable $e_{i}$ may have arbitrary probability densities $p\left(e_{i}\right)$. If the modeled function is the same as real data generating process, then the noise should be independent with the cause variables.

Given two observed variables $x$ and $y$. The algorithm first tests whether $x$ and $y$ are statistically independent. If they are not, the algorithm tests weather a model $y=f(x)+e$ is consistent with data. It contains several steps. Firstly, it does a nonlinear regression of $y$ on $x$ to get an estimate $\hat{f}$ of $f$. Then it calculates the corresponding residuals $\hat{e}=y-\hat{f}(x)$ and test whether $\hat{e}$ is independent of $x$. If so, it accepts $y=f(x)+e$; if not, it rejects it. The similar test decides whether the reverse model $x=g(y)+e$ fits the data. There are four possible results. Firstly, if $x$ and $y$ are mutually independent, there is no causal relationship between them. Secondly, if they are dependent and both directional models fit the data, then either model may be correct but we do not know which. Thirdly, if

```
Algorithm 1: \(\operatorname{CausalBN}(V, \mathcal{D})\)
    Input : Vertex Set \(V=\left\{v_{1}, v_{2}, \ldots, v_{n}\right\}\), data set \(\mathcal{D}\)
    Output : A causal Bayesian network \(G^{*}=\left\{V, E^{*}\right\}\)
    1 Compute PDAG \(G_{p}=\left\{V, E_{p}\right\}\) using Algorithm 2,
        within \(E_{p}\) there is a list of undirect edges \(E_{u}\);
        Compute pairwise \(\chi^{2}\) statistics for edge pairs \(E_{u}\);
    3 Sort \(E_{u}\) in descending order of \(\chi^{2}\) statistics;
    \(4 G^{*}=G_{p}\);
    while \(E_{u}\) is not empty do
        Choose edge \(e_{t} \in E_{u}\) with the highest \(\chi^{2}\) statistics;
        Infer the causal direct using additive noise model
        and orient \(e_{t}=\left\{v_{i} \rightarrow v_{j}\right\}\);
        Apply causal forward propagation, \(G^{*}=\)
        CausalForwardProp \(\left(G^{*}, e_{t}\right)\);
    8 return \(G^{*}\);
```

one of the directions is rejected and the other is accepted, a causal relationship is identified. Fourthly, neither model fits the data, which means the real data generating mechanism is more complex and we cannot use the proposed model to describe it.

## V. Structure Learning Algorithm

The BN structure learning algorithm based on causality has four main steps.

1) Use the PC algorithm [14] in Algorithm 2 to identify the PDAG which contains some undirected edges. PC algorithm starts with a complete undirected graph and uses conditional independence to eliminate or orient edges. The edge type for directed pair and undirected pair are expressed as $\rightarrow$ and - . Here we define two nodes are adjacent if there is a directed and undirected edge between them.
2) Use the $\chi^{2}$ test to sort the undirected edges based on their dependencies.
3) Orient the most dependent undirected pair using nonlinear additive noise model.
4) Apply causal forward propagation in Algorithm 3 to this oriented edge to orient other undirected edges recursively.
5) Repeat the similar procedure until al edges are oriented.

The complete algorithm is given in Algorithm 1.
The causal forward propagation uses four rules to propagate the causal information when we have a new directed edge. The first rule utilizes directed acyclic property to orient the edges. Note that the circle contains undirected edge does not violate directed acyclic property. The other three rules orient the undirected edge by preventing introducing a new v-structure. Because in PC algorithm, we already use the conditional independency to identify all the possible v-structures completely, so we can use this property to oriented edges. The second rule is straightforward. For the third rule, if we orient $\left\{v_{j}-v_{k}\right\}$ as $\left\{v_{j} \rightarrow v_{k}\right\}$, then by DAG constraints, we must orient $v_{k}$ and $v_{i}$ as $\left\{v_{i} \rightarrow v_{k}\right\}$, and $\left\{v_{l} \rightarrow v_{k}\right\}$ for $v_{k}$ and $v_{l}$. It will produce new v-structure. For the fourth rule, if we orient $\left\{v_{j}-v_{k}\right\}$ as $\left\{v_{j} \rightarrow v_{k}\right\}$, then there must be two directed edges

Algorithm 2: Outline of PC-algorithm
Input : Vertex Set $V=\left\{v_{1}, v_{2}, \ldots, v_{n}\right\}$, significance level $\alpha$
Output : A PDAG $G_{P}$
1 Form the complete undirected graph G on the vertex set V ;
2 Test conditional and marginal independencies at a given significance level $\alpha$. Remove one edge between the adjacent pair if there is certain independent relationship between them;
3 Orient v-structures by conditional independence information;
while There are still edges can be oriented by the following rules do
4 If $X \rightarrow Y, Y-Z, X$ and $Z$ are not adjacent, then oriented $Y-Z$ as $Y \rightarrow Z$;
5 If $X-Y$, and there is a directed path from $X$ to $Y$, then orient $X-Y$ as $X \rightarrow Y$;
6 return $G_{P}$;
$\left\{v_{i} \rightarrow v_{k}\right\}$ and $\left\{v_{l} \rightarrow v_{k}\right\}$ to obey the DAG property, it will produce new v-structure.

The time complexity of our algorithm mainly comes from the PC algorithm. In Algorithm 1, PC algorithm in step 1 takes $\frac{n^{2}(n-1)^{k-1}}{(k-1)!}$ time in the worst case [14], where $n$ is the number of variables, and $k$ is the maximal degree of any vertex. Step 2 takes $O\left(n^{2}\right)$, step 3 takes time $O\left(n^{2} \log (n)\right)$. In addition, the while loop runs at most $O\left(n^{2}\right)$ times, within which steps 5 and 6 only take $O(1)$ time. The Algorithm 3 in step 7 needs further consideration. Assume there is no recursion, the first for loop in Algorithm 3 runs $O\left(n^{2}\right)$ times, the codes within run $O(1)$ time. The second for loop runs $O\left(n^{2}\right)$ times, the codes within run $O\left(n^{2}\right)$ time. The third and fourth for loops run $O\left(n^{2}\right)$ times, the codes within run $O\left(n^{4}\right)$ time. So the whole algorithm without recursion runs in $O\left(n^{6}\right)$ time. Note that there are at most $O\left(n^{2}\right)$ undirected edges, so there are at most $O\left(n^{2}\right)$ recursions. Each recursion orients one undirected edge, at the same time, it reduces one while loop. So the whole while loop takes $O\left(n^{8}\right)$ time. The whole Algorithm 1 takes $\frac{n^{2}(n-1)^{k-1}}{(k-1)!}$ time in the worst case.

## VI. Performance Evaluation

We describe here the performance of the proposed causal structure learning algorithm in terms of log-loss, which measures how well the proposed model fits the data. We use two handwriting data sets, both involving writing of the common word "and":

1) Samples from a representative adult population of the United States [20]. There are writing samples of about 1,500 writers containing both hand-printed and cursive writing styles. The data set contains 3,075 cursive "and" samples and 1,135 hand-print "and" samples, both of which have 9 features. The meaning of these features are in [11].
2) Handwriting samples of children from the first- to fifth-grades. There are 524 cursive "and" samples and 918 hand-print "and" samples. Each sample has 13

Algorithm 3: CausalForwardProp( $G, e)$
Input : A PDAG $G=\{V, E\}$ and a newly oriented edge $e=\left\{v_{i} \rightarrow v_{j}\right\}$
Output : A PDAG $G$ with less uncertainty
1 Orient $e$ in $E, E=E-\left\{v_{i}-v_{j}\right\}+\left\{v_{i} \rightarrow v_{j}\right\}$;
2 Remove $e$ from list $E_{u}$;
for Each edge $e_{1}=\left\{v_{m}, v_{n}\right\}$ in list $E_{u}$ do
$G_{1}=G$
Orient $e_{1}=\left\{v_{m} \rightarrow v_{n}\right\}$ in $G_{1}$;
if $\neg i s D A G\left(G_{1}\right)$ then
Orient $e_{1}=\left\{v_{n} \rightarrow v_{m}\right\}$
Apply causal forward propagation, $G=$ CausalForwardProp( $G, e_{1}$ );
$G_{1}=G$
Orient $e_{1}=\left\{v_{n} \rightarrow v_{m}\right\}$ in $G_{1}$;
if $\neg i s D A G\left(G_{1}\right)$ then
Orient $e_{1}=\left\{v_{m} \rightarrow v_{n}\right\}$
Apply causal forward propagation, $G=$ CausalForwardProp( $G, e_{1}$ );
for Each edge $e_{2}$ in list $E_{p}$ do
if There is an undirect edge $e_{2}=\left\{v_{j}-v_{k}\right\}$ and there is no edge between $v_{i}$ and $v_{k}$ then
Orient $e_{2}=\left\{v_{j} \rightarrow v_{k}\right\}$;
Apply causal forward propagation, $G=$ CausalForwardProp( $G, e_{2}$ );
for Each edge $e_{3}$ in list $E_{p}$ do
if There is a undirected edge $e_{3}=\left\{v_{j}-v_{k}\right\}$, there are one directed edge $\left\{v_{l} \rightarrow v_{j}\right\}$, and there are edges among $v_{k}$ and $v_{i}, v_{l}$ then
Orient $e_{3}=\left\{v_{k} \rightarrow v_{j}\right\}$;
Apply causal forward propagation, $G=$ CausalForwardProp( $G, e_{3}$ );
for Each edge $e_{4}$ in list $E_{p}$ do
if There is a undirected edge $e_{4}=\left\{v_{j}-v_{k}\right\}$, there are one directed edge $\left\{v_{l} \rightarrow v_{i}\right\}$, there are one edge between $v_{l}$ and $v_{k}$, and there are no edge between $v_{l}$ and $v_{j}$ then
Orient $e_{3}=\left\{v_{k} \rightarrow v_{j}\right\}$;
Apply causal forward propagation, $G=$ CausalForward $\operatorname{Prop}\left(G, e_{3}\right)$;
return $G$;
features. The meaning of these features can refer to [21].

We compare performance on these two data sets using (i) a state-of-art branch and bound algorithm (B \& B) [10], (ii) the greedy algorithm [11] introduced in section II-C, and (iii) the proposed Causal BN learning algorithm.

Table I shows the relative performance of different BN structure learning algorithms using the log-loss measure. A higher score signifies higher probability of the data set given the proposed model. The first two rows give the results with the first data set and the last two with the second data set. The first three columns show the data sets, writing styles, and the number of variables (features). The fourth column corresponds

![img-1.jpeg](img-1.jpeg)
(a)
(b)
![img-2.jpeg](img-2.jpeg)
(c)

Fig. 2: Bayesian network structures learned from data set 1 (nine variables corresponding to features of "and" that are cursively written): (a) greedy algorithm [11], (b) B \& B algorithm, (c) causal algorithm.

TABLE I: Comparison of four BN structure learning methods on four handwriting data sets. Each algorithm is evaluated using the log-loss (Eq. 2) on the data set. Causal algorithm performs best (lowest loss in representing the data).


to log-loss when all variables are independent (no edges in graph). The fifth column contains results from the BN structure learning algorithm in [11]. The sixth column contains results from the B \& B algorithm. BNs learned from "and" data set are shown in Fig. 2. From Table I, we can conclude that beside the ability of causal inference, the proposed algorithm performs better in BN structure learning and fits the data sets very well.

Some examples of causality learnt from the data are as follows:

- For cursive 'and' in set 1, the formation of staff of 'd' $\left(X_{6}\right)$, including tented, retracted, looped, etc, decides the formation of terminal stroke of 'd' $\left(X_{8}\right)$, which includes curved up, straight across, curved down, etc.

Fig. 3: Two variables ( $X_{6}$ and $X_{8}$ ) and their values in Data Set 1: Cursive 'and'. According to the learnt BN, formation of the staff of $d$ influences the terminal curve.


Fig. 4: Two variables and their values in Data Set 2: Hand-print 'and'. The $a-n$ relationship influences the $n-d$ relationship

The visual examples are showed in Fig. 3. We can see the shape of the character 'd' decides its last stroke.

- For hand-print 'and' in set 2, the 'a'-'d' relationship $\left(x_{11}\right)$, including taller, equal, or smaller, decides the ' $n$'-'d' relationship $\left(x_{12}\right)$ with the same values. The visual examples has shown in Fig. 4. Because people usually write a single word in one direction, the 'a'-'d' relationship decides ' $n$'-'d' relationship.
- For hand-print 'and' in set 2, the 'a'-'n' relationship $\left(x_{10}\right)$ decides the ' $n$'-'d' relationship $\left(x_{12}\right)$.


## VII. CONCLUSION

A new Bayesian network structure learning algorithm has been proposed. It is deterministic, computationally efficient and uses the principle of causality Given intuitions and limitations of both global and local causal inference algorithms, we solve a set of challenges to combine them to result in a better algorithm. Specifically, given the causal skeleton, we use the $\chi^{2}$ statistical test to identify the most dependent pair and perform the causal inference with strong accurate. After that, our causal forward propagation algorithm propagates the newly learned causal information in order to reduce the number of local causal inference. Experiments on handwritten data show that the algorithm provides better statistical models than two previous algorithms, the B \& B algorithm and a greedy algorithm. Moreover the resulting structure has the advantage of discovery of causality.
