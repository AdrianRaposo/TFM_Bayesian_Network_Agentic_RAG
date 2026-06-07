# Relevant based structure learning for feature selection 

Hadi Zare ${ }^{\mathrm{a}, *}$, Mojtaba Niazi ${ }^{\mathrm{a}}$<br>${ }^{a}$ Faculty of New Sciences and Technologies, University of Tehran, Iran


#### Abstract

Feature selection is an important task in many problems occurring in pattern recognition, bioinformatics, machine learning and data mining applications. The feature selection approach enables us to reduce the computation burden and the falling accuracy effect of dealing with huge number of features in typical learning problems. There is a variety of techniques for feature selection in supervised learning problems based on different selection metrics. In this paper, we propose a novel unified framework for feature selection built on the graphical models and information theoretic tools. The proposed approach exploits the structure learning among features to select more relevant and less redundant features to the predictive modeling problem according to a primary novel likelihood based criterion. In line with the selection of the optimal subset of features through the proposed method, it provides us the Bayesian network classifier without the additional cost of model training on the selected subset of features. The optimal properties of our method are established through empirical studies and computational complexity analysis. Furthermore the proposed approach is evaluated on a bunch of benchmark datasets based on the well-known classification algorithms. Extensive experiments confirm the significant improvement of the proposed approach compared to the earlier works.


Keywords: Feature selection, Supervised learning, Relevant features, Mutual information, Structure learning, Graphical models

## 1. Introduction

Feature selection (or variable selection) has been considered as a primary step in machine learning, pattern recognition, and data mining fields. It is

[^0]
[^0]:    *Corresponding author

used in a variety of applied domains such as text classification, micro-array analysis and image processing. Nowadays with the explosion of massive online data, choosing an optimal subset of features is a very crucial step, [1, 2]. While predictive modeling with huge feature sets are common in recent years, it would be caused heavy computational burden, interpretation difficulty, and weak results based on curse of dimensionality [3, 4]. Not only the suitable feature selection process can provide efficient tools to remove irrelevant, redundant and noisy features, but it would improve the speed of learning phase and performance measures of the predictive task too. Based on learning language, the feature selection could be classified to supervised and unsupervised methods. Supervised feature selection approaches are mainly based on the relation between the features and the label to find the optimal feature sets [5] [6] [7][8] [9]. On the other hand, finding the optimal feature selection techniques for unsupervised problems are much harder than the supervised one's due to the ambiguous definition of the unsupervised learning, "discovering the interesting patterns from the data" [10] [11] [12][13][14]. Here we concentrate on the feature selection for the supervised learning problems.

If we let the original feature set $F=\left\{f_{1}, f_{2}, \ldots, f_{p}\right\}$ and the class variable as $Y$, the aim of feature selection process is to find the optimal subset $S \subset F$ such that it has the best predictive accuracy based on the validation performance criteria. Supervised feature selection process typically can be divided in four primary steps [15],
(i) Evaluation criteria
(ii) Search approaches
(iii) Stopping criterion
(iv) Validation methods

In evaluation step, a criterion should be designed carefully to test the relevancy between the selected subset of features and the class variable. Because of the exponential computational complexity of searching through the complete subsets of the original set of features, search procedure for generating candidate subsets of features to evaluate them are devised in search step. The search and evaluation on the candidate subset of features are continued until the stopping criterion holds. Finally the selected feature set usually

requires to be validated based on the dataset or prior domain expert knowledge. The evaluation criteria and search strategy are more important than the other steps in a feature selection process.

Based on different evaluation criteria, the feature selection techniques can be generally classified into three main types, the filter, the wrapper and the hybrid methods, [16] [15][17][18]. The straightforward approach for evaluation criteria is to measure directly the performance of a subset of features based on classification accuracy with the aid of a predictive classifier to select the best subset of features [19]. Although the most effective and optimal approach could be offered in a wrapper model, these techniques suffer from heavy computational burden of training classifier algorithms. The main idea of filter methods is the selection of the optimal features based on statistical or information theoretic evaluation criteria applied on the certain characteristics of the data without requirement of any classification algorithms. The hybrid (embedded) techniques that are somewhat similar but less computationally expensive compared to wrapper methods which measure optimal subset of features through the learning phase. Because of the time consuming of the wrappers and hybrid techniques, the filter methods are highly recommended for dealing with real applications using a variety of evaluation tools such as, the Markov blanket based for streaming dataset [7], fuzzy-rough sets for feature significance [20], heuristic relevance based approach [21], divergence criterion [22], and centrality based influence measure [12].

A variety of techniques are proposed for search strategies, such as exhaustive search [23], ranking based among the feature based on the relevancy to the class variable [24] [25] [26]. Because of the exponential computation time of exhaustive search approach and ignoring the redundant features in relevant ranking based methods, sequential greedy approaches are proposed to maximize the evaluation criteria in an iterative and incremental development manner [27][16]. Although the traditional forward greedy approaches are commonly used for dealing with huge number of features because of low computational burden and more robustness to over-fitting, they suffer from neglecting the impact of redundancy among features. Some methods [28] [6] have proposed the innovative information theoretic evaluation criteria in a sequential search vein to remedy the aforementioned problems.

Recently some feature selection methods are proposed for massive online dataset, where the number of features are increased with fixed number of observations, streaming cases or incremental observations [7][1][29] and in these works the evaluation criteria is based on the priorly defined probabilistic and

information theoretic concepts in [28, 6]. The main problems in these recent works could be categorized in threefold, computational burden, streaming setting and optimality criteria.

In this paper we propose a novel feature evaluation criteria in a filter approach based on structure learning and information theoretic tools that can be adopted for streaming dataset and non-streaming dataset. In line with the proposed approach, "structure learning for feature selection", hereafter called as SLFS, that allowed us to choose more relevant less redundant features carefully within a negligible loss of total feature information, the computation time is reduced compared to the earlier works such as $[6,7]$.

The structure of the paper is organized as follows. In Section 2, the related works on feature selection are reviewed and a motivation of the basic idea to solve the problem are presented. Section 3 is devoted to the theoretical foundation of the feature selection based on the Markov blanket approach and an overall scheme of our method. The proposed feature selection algorithms and their advantages compared to the previous ones are illustrated in Section 4. We present and describe the experimental results based on the state-ofthe art datasets through the SLFS algorithm compared to the earlier works in Section 5. Finally Section 6 discusses the results based on the proposed framework as well as conclusions and future works on the field.

# 2. Related works and Basic Idea 

### 2.1. Related works

Because of the importance of the feature selection problem, many researches have been done on various aspects of this fundamental topic. By the availability of massive number of features, reasonable to assume a large subset of features are either irrelevant or redundant for predictive modeling and only a small portion of relevant features yield more effective learning aims [17][15]. On the one hand, most of the earlier researches have been concentrated on finding relevant features based on the high dependency to the class labels [6][22][30]. On the other hand, for a wide variety of applications, such as genomic microarray analysis [31] [32], image representation [33], and text categorization [34][35], there exist high redundancy among the features. Hence the feature selection algorithm based only on the relevance criteria can be resulted in suboptimal set of features [19][26]. There are many research efforts to consider the feature selection criteria with the redundancy and relevancy simultaneously, Markov blanket based approach

[28][36], max-dependency and min redundancy based on mutual information [6], and meta-heuristic greedy search [5]. From the theoretical point of view, Markov blanket framework for feature selection would be yielded to the optimum subset of features and the remaining ones could be considered as redundant features. Because of the exponential computational complexity of finding the Markov blanket subset among the features, there exist a variety of efforts to approximate it such as linear correlation approach [37], and statistical $\chi^{2}$-square test [7]. Those works consider pairwise feature dependency rather than the joint consideration to find the Markov blanket.

# 2.2. Overall scheme of the idea 

First, we define the mutual information between two features $x, y$,

$$
\begin{aligned}
I(x ; y) & =\int_{x} \int_{y} P(x, y) \log \frac{P(x, y)}{P(x) P(y)} d x d y \\
& =H(x)-H(x \mid y)
\end{aligned}
$$

where $H(x)$ is the entropy of the $x$ and $H(x \mid y)$ is the conditional entropy of $x$ given $y,[38]$. The definition (1) of mutual information can be generalized for a vector of features $E=\left(f_{1}, f_{2}, \ldots, f_{m}\right)$ and class variable $Y$ as follows,

$$
I(E ; Y)=\iint_{E} \int_{Y} P\left(f_{1}, \ldots, f_{m}, Y\right) \log \frac{P\left(f_{1}, \ldots, f_{m}, Y\right)}{P\left(f_{1}\right) \ldots P\left(f_{m}\right) P(Y)} d f_{1} \cdots d f_{m} d Y
$$

By denoting the total feature set $F=\left\{f_{1}, f_{2}, \ldots, f_{p}\right\}$ and a selected subset of it as $S \subset F$, the optimal solution for a supervised feature selection is to reduce the size of selected features $S$ such that it produces the most prediction accuracy with the class variable [38],

$$
R=\min _{S \subset F}|S|-\lambda \cdot I(S ; Y)
$$

where $\lambda>0$ is a penalized constant. The main problem with this approach is twofold, the computation of the joint mutual information and the problem of remaining redundant when new features are added in each step via a greedy approach like [6]. Unlike to the stepwise selection and removal of the features, in line with the subset based strategy to investigate the optimal features, we propose a model based technique to find the optimum subset of features. The main idea of proposed method is to find the structure of directed graphical models among the features to provide a suitable framework for extraction of

the selected features based on the well-known Markov blanket vehicle. We have applied maximum likelihood approach for structure learning among the features that yields to a unique solution. The details of our approach are presented in the following sections.

# 3. Theoretical foundation for the proposed approach 

Because of our proposed method's dependency on Markov blanket and conditional independency concepts, the precise definitions are presented here based on $[39]$.

Definition 1. (conditional independence) Let $X, Y, Z$ be sets of discrete random variables. $X$ is conditionally independent of $Y$ given $Z, X \perp Y \mid Z$, if

$$
P(X=x \mid Y=y, Z=z)=P(X=x \mid Z=z) \quad \text { or } \quad P(Y=y, Z=z)=0
$$

If we denote the $f_{i} \in F$ and $S_{i}=F-\left\{f_{i}\right\}$, then the formal definitions of relevant and redundant features are as follows [37].

Definition 2. (Strongly relevant) A feature $f_{i}$ is said to be strongly relevant to the class variable $Y$ if and only if

$$
\nexists S_{i} \quad \text { such that } \quad P\left(Y \mid f_{i}, S_{i}\right)=P\left(Y \mid S_{i}\right)
$$

Definition 3. (Weakly relevant) A feature $f_{i}$ is said to be weakly relevant to the class variable $Y$ if and only if

$$
\exists S_{i} \quad \text { such that } \quad P\left(Y \mid f_{i}, S_{i}\right)=P\left(Y \mid S_{i}\right)
$$

Definition 4. (Irrelevant) A feature $f_{i}$ is said to be irrelevant to the class variable $Y$ if and only if

$$
\forall S_{i} \quad \text { such that } \quad P\left(Y \mid f_{i}, S_{i}\right)=P\left(Y \mid S_{i}\right)
$$

As stated in definitions, while strongly relevant features provide unique information about the class variable which are not attainable with the other features, weakly relevant features have information about the class variable attainable with the other features without losing probabilistic information. On the other hand, irrelevant features are not related to the class variable $Y$

and they should be removed from the modeling. Although the definition 3 states weakly relevant features maybe useful to the class variable and therefore including some of them in the optimal subset of features, the discrimination between these features is not clear based on the relevancy concept. In works of [28] and [37] the concept of redundant features based on the Markov blanket are proposed for solving the problem.

Definition 5. (Markov blanket) Let $M$ be a subset of $F$ and $f_{i} \in F,\left(f_{i} \notin\right.$ $M$ ), then $M$ is a Markov blanket of $f_{i}$ if and only if [39],

$$
f_{i} \perp F-f_{i}-M \mid M
$$

Definition 6. (Redundant) The feature $f_{i} \in F$ is said to redundant with respect to $Y$ if it has the following properties,
(i) Weakly relevant to the class variable
(ii) It has a Markov blanket $M_{i}$ such that $M_{i} \subset F-f_{i}$

In conclusion, the features can be classified into four disjoint types, i) strongly relevant, ii) non-redundant weakly relevant, iii) redundant, and iv) irrelevant features. The optimal subset of features comprises strongly relevant and non-redundant weakly relevant features. Our aim is to develop a structure learning approach to detect these two types of good features for classification tasks and provide a Bayesian network classifier generated by the selected features. The overall description of the SLFS method is shown in Figure 1.

# 4. The proposed Structure learning approach for feature selection 

Traditional machine learning techniques assume the independence relationship among the features due to the specification complexity of joint probability distribution among them. Probabilistic graphical models (PGM) provide a framework to assign the relationship among the features in a graph structure to represent the distribution from it on a straightforward manner and then use the joint distribution to answer the main query based on a probabilistic approach. Although, the graph structure of PGM should be specified by domain experts, this approach suffers from dealing with huge number of features in real applications. This problem has attracted many

![img-0.jpeg](img-0.jpeg)

Figure 1: The overall view of the proposed algorithm
researchers and a variety of techniques are proposed for identification of the dependencies among features in a graph structure, entitled as "Structure Learning" [10]. A variety of graph structures can be appeared based on the conditional independencies amidst features that the details of our approach for dealing with them are discussed in Sub Section 4.2. We propose an integrated approach for finding the suitable structure amid features which they satisfy to the relevancy and non-redundant weakly relevant conditions.

# 4.1. Structure learning based on maximum likelihood approach 

A well-known paradigm for structure learning is to apply maximum likelihood approach as the following,

$$
\begin{aligned}
L\left(\theta_{G}, G, F\right) & =\log P\left(F \mid \theta_{G}, G\right) \\
& =M \sum_{\mathrm{i}} \hat{I}\left(f_{i} ; p a\left(f_{i}\right)\right)-M \sum_{\mathrm{i}} \hat{H}\left(f_{i}\right)
\end{aligned}
$$

Where the parameters $F, M, p a\left(f_{i}\right), \hat{H}\left(f_{i}\right), \hat{I}\left(f_{i} ; p a\left(f_{i}\right)\right), G$, and $\theta_{G}$ are the set of all features, the size of $F$, the set of parents of $f_{i}$, the estimated

entropy of feature $f_{i}$, the estimated mutual information between features $f_{i}$ and $p a\left(f_{i}\right)$, the graph structure to be learned from data, and the set of parameters to be estimated for the computation of the joint probabilities amid features. The log-likelihood is used to simplify the calculations and for a proof of relation (4) one can see [10]. The identification of the redundant features requires the computation of the Markov blanket subsets of features that causes main computational complexities due to the estimation of joint probability distributions. We have exploited Bayesian networks as the optimal graph structures amidst features because of the straightforward identification of Markov blanket subsets through them. The main question is how to find a tree structure to discriminate between the redundant and non-redundant features. To answer this question, we propose a novel criteria for goodness of the structure,

$$
J=L-R
$$

where the main equation for $R,(3)$ is approximated based on [38],

$$
\begin{aligned}
& |S| \approx \sum_{i} I\left(f_{i} ; Y \mid p a\left(f_{i}\right), G\right) \\
& I(S ; Y) \approx \sum_{i} I\left(f_{i} ; Y \mid G\right)
\end{aligned}
$$

Hence, the relation (5) is changed as,

$$
J=\sum_{i}\left(I\left(f_{i} ; p a\left(f_{i}\right) \mid G\right)-H\left(f_{i} \mid G\right)\right)+\lambda \sum_{i}\left(I\left(f_{i} ; Y \mid G\right)-I\left(f_{i} ; Y \mid p a\left(f_{i}\right), G\right)\right)
$$

A forward approach for simultaneous selection of optimal subset of features and building up a tree Bayesian network (TBN) according to the main criteria (7) is proposed as follows. The primary aim of the proposed approach for create TBN is based on the maximization of $J$ value in (7). The TBN is built up according to the following principles,
(i) The order of arrivals of input features should not be important.
(ii) Maximize the relation (7).
(iii) Prune the features based on Markov blanket approach for Bayesian networks

Intuitively, the principles (i) to (iii) are given to, (i) enable our algorithm to function under incremental and online features, (ii) consistency with the main criteria $J$, and (iii) remove the redundant features according to Markov blanket.

# 4.2. TBN construction 

We have assumptions on TBN construction regrading the main criteria (7). If there is no edge between two features in the current stage of TBN, then the mutual information between them are negligible and skipped in the computation of $J$ for the next step of the algorithm. In addition, the Markov blanket for a feature is defined to be the set of consisting the features being in the lower depth(level) of the tree regarding it. The input feature is independent from the class given those features which have lower level in TBN based on Markov blanket definition.
At first, the irrelevant features identified and then removed from the remaining features. Formally $f_{i}$ is irrelevant if $\hat{I}\left(f_{i} ; Y\right)=0$. Based on our criteria (7), the input feature $f_{i}$ is irrelevant if it decreases the value of $J$, which can be written as the inequalities (8) based on relation (5),

$$
\hat{I}\left(f_{i} ; p a\left(f_{i}\right)\right)-\lambda \hat{I}\left(f_{i} ; Y \mid p a\left(f_{i}\right)\right)<0 \text { and } \lambda \hat{I}\left(f_{i} ; Y\right)-\hat{H}\left(f_{i}\right)<0
$$

where $p a\left(f_{j}\right)$ is denoted as the parent of feature $f_{i}$. The intuition behind the inequalities (8) comes from the definition of irrelevant features where we expect less information between an irrelevant feature and class variable than its and other features. Moreover we set $\lambda=1$ in this case for simplicity.

The TBN construction is based on weakly and strongly relevant features that can be classified into three states.

1. Connect the class and input feature: When the input features increase the main relation (7), the input feature is connected to the class $Y$ and considered as a strongly relevant one. Hence connect the input feature $f_{i}$ to the class variable $Y$ if it holds in (9),

$$
\lambda \hat{I}\left(f_{i} ; Y\right)-H\left(f_{i}\right)>\hat{I}\left(f_{i} ; p a\left(f_{i}\right)\right)-\lambda \hat{I}\left(f_{i} ; Y \mid p a\left(f_{i}\right)\right)
$$

where the $p a\left(f_{i}\right)$ is selected from those nodes that directly connected to $Y$ denoted by $S$,

$$
p a\left(f_{i}\right)=\arg \max _{f_{k} \in S} \hat{I}\left(f_{i} ; f_{k}\right)-\hat{I}\left(f_{i} ; Y \mid f_{k}\right)
$$

The state 1 is illustrated in Fig. 2.

![img-1.jpeg](img-1.jpeg)

Figure 2: Part(a): An input relevant feature $f_{i}$ connects to class $Y$ or a candidate parent of the TBN such as $p a\left(f_{i}\right)$. Part(b): An input feature $f_{i}$ satisfies in condition (9) which connects to $Y$.
![img-2.jpeg](img-2.jpeg)

Figure 3: Part(a): An input relevant feature $f_{i}$ connects to a candidate parent $f_{j}$ or a candidate parent between child set $f_{j}, f_{l}$. Part(b): An input feature $f_{i}$ satisfies in condition (11) which connects to $f_{j}$
2. Find the parent node for input feature: If the input feature $f_{i}$ does not satisfy in condition (9), then two scenarios appear. In first scenario, $f_{i}$ connects to the level (i) of TBN,

$$
\hat{I}\left(f_{i} ; f_{j}\right)-\hat{I}\left(f_{i} ; Y \mid f_{j}\right)>\hat{I}\left(f_{i} ; f_{k}\right)-\hat{I}\left(f_{i} ; Y \mid f_{k}\right)
$$

where the $f_{j}$ and $f_{k}$ are defined in (12),

$$
\begin{aligned}
& f_{j}=\arg \max _{f_{k} \in c h\left(p a\left(f_{j}\right)\right)} \hat{I}\left(f_{i} ; f_{k}\right)-\hat{I}\left(f_{i} ; Y \mid f_{k}\right) \\
& f_{k}=\arg \max _{f_{s} \in c h\left(f_{j}\right)} \hat{I}\left(f_{i} ; f_{s}\right)-\hat{I}\left(f_{i} ; Y \mid f_{s}\right)
\end{aligned}
$$

Also $f_{j}$ is the parent of $f_{k}$ and $c h\left(f_{j}\right)$ denotes the child set of $f_{j}$. In second scenario, the state 2 repeats, until the relation (11) is satisfied or reached to leaf in TBN. The Fig. 3 describes the state 2.
![img-3.jpeg](img-3.jpeg)

Figure 4: Part(a): Input feature $f_{i}$ with state conditions 2. Part(b): Swap position of $f_{i}$ with $f_{j}$ based on relation (13).
3. Swap input feature with the candidate parent: If relations in (13) hold then swap the position of $f_{i}$ with $f_{j}$ where $f_{j}$ is the candidate parent selected from previous state.

$$
\begin{aligned}
& \hat{I}\left(f_{i} ; Y\right)>\hat{I}\left(f_{j} ; Y\right) \\
& \hat{I}\left(f_{i} ; f_{j}\right)-\hat{I}\left(f_{i} ; Y \mid f_{j}\right)<\hat{I}\left(f_{i} ; f_{j}\right)-\hat{I}\left(f_{j} ; Y \mid f_{i}\right)
\end{aligned}
$$

The Fig. 4 describes the state (3). The theory behind state 3 is given in Theorem 1.
![img-4.jpeg](img-4.jpeg)

Figure 5: The description of $f_{i}, f_{j}$ and $f_{k}$ in Theorem 1

Theorem 1. Let $f_{k}, f_{j}$, and $f_{i}$ be nodes in TBN according to Fig. 5(a). If the relations (13) are satisfied, then the child node $f_{i}$ is swapped to $f_{j}$ to maximize the main criteria $J$ in (7), (see Fig. 5(b)). Moreover, the $f_{j}$ stays in this new position.

Proof. The sub tree in Fig. 5(b) is better than Fig. 5(a) in TBN structure based on $J$ which is easily seen that from (13).
To prove the second part of Theorem 1, first note that the child set of $f_{j}$ connects to $f_{i}$ based on swapping $f_{i}$ to $f_{j}$. The following relations hold for arbitrary $f_{i}, f_{j}$ and $Y$ (for the proof see [38]),

$$
\hat{I}\left(f_{j} ; Y \mid f_{i}\right)=\hat{I}\left(f_{i} ; Y \mid f_{j}\right)-\left(I\left(f_{i} ; Y\right)-\hat{I}\left(f_{j} ; Y\right)\right)
$$

Based on assumption (13) and relation (14) we have,

$$
\hat{I}\left(f_{j} ; Y \mid f_{i}\right)<I\left(f_{i} ; Y \mid f_{j}\right)
$$

Hence it follows,

$$
\hat{I}\left(f_{i} ; f_{j}\right)-\hat{I}\left(f_{i} ; Y \mid f_{j}\right)<\hat{I}\left(f_{i} ; f_{j}\right)-\hat{I}\left(f_{j} ; Y \mid f_{i}\right)
$$

We can write the relation (16) according to an immediate consequence of inequality (15),

$$
f_{i}=\arg \max _{\left\{l: f_{l} \in c h\left\{p a\left(f_{i}\right)\right\}\right\}} I\left(f_{l} ; f_{i}\right)-I\left(f_{j} ; Y \mid f_{l}\right)
$$

The relation (16) proves the preserving the $f_{j}$ in the new position after swapping.

# 4.3. The description of the SLFS algorithm 

The main scheme of the proposed SLFS algorithm is depicted in Algorithm 1 .

```
Algorithm 1 Structure Learning for Feature Selection (SLFS)
    Input: F, MAXDEPTH
    Output: TBN comprises of the selected subset of features
    repeat
        if IRR( f i) then
            remove( }\mp@subsup{f}{i}{}
            break
        else
            f}\mp@subsup{f}{j}{}=\operatorname{findParent}\left(f_{i},\operatorname{childSet}(Y)\right)
            if connnect( }\mp@subsup{f}{i}{},f_{j},Y)=Y\mathrm{ then
                TBN.E(Y,f}\mp@subsup{f}{i}{})=1
            else
                depth = 1
                repeat
                    if depth > MAXDEPTH then
                    remove( }\mp@subsup{f}{i}{}
                    break
                    end if
                    f}\mp@subsup{f}{k}{}=\operatorname{findParent}\left(f_{i},\operatorname{childSet}\left(f_{j}\right)\right)\mathrm{}
                    add = false
                    if connect( }\mp@subsup{f}{i}{},f_{j},f_{k})=f_{j}\mathrm{ then
                    add = true
                    TBN.E(f
                    end if
                    if swapCheck( }\mp@subsup{f}{i}{},f_{j})\mathrm{ then
                    TBN.swap( }\mp@subsup{f}{i}{},f_{j}\mathrm{ )
                    end if
                    depth = depth + 1
                    until add = false
                    end if
            end if
        until }\forall f_{i}\in F
```

The Algorithm 1 initially depends on the set of current available features $F$, maximum level of the tree $M A X D E P T H$, and the regularization parameter $\lambda$. In this algorithm first we check the irrelevant features with $I R R$ function depending on the $\lambda$ based on relation (8). Lines 6-29 explain the

Table 1: The time complexity of the main used algorithms, where $p, N,|S|$ and $K$ are the number of features, number of samples, size of selected features and maximum allowable size of selected candidate subset of features.


different situation for adding features according to State 1 to State 3. The findParent function finds a candidate parent for input feature $f_{i}$ according to relation (10). The connect function select a suitable parent for $f_{i}$ which maximize $J$ based on state conditions 1 and 2. Adding edge to TBN graph is performed by TBN.E. Function swapCheck checks the correctness of condition of swapping the position between two features in TBN based on State 3. The swap position between features is done by swap function. Lines 19-22 and lines 23-25 perform based upon State 2 and State 3. If a feature goes down the maximum depth of the TBN, MAXDEPTH according to the algorithm procedure, it is removed from the selected subset of features. Moreover, the features in the final TBN are considered as the Markov blanket of the removed features for the output variable $Y$.

# 4.4. Time complexity analysis 

We compare the SLFS algorithm to the earlier algorithms based on the time complexity. A summary of time complexity analysis is presented in Table 1. The main computational part of SLFS is the step of feature adding in TBN construction. The feature adding step consists up two elements. Comparison operation of the given feature with the other existing features in each depth level is done in first element. Second one is the calculation of mutual information between two features. If we assume that the maximum child for each existing node and the total levels of the TBN equal to $N C H$ and $M A X D E P T H$, then the total number of comparison is at most $N C H \times$ MAXDEPTH. So, the time complexity of the first element is at most $O(p)$ for each feature with the assumption $M A X D E P T H \ll p$ and $N C H \longrightarrow$ $p$. The time complexity of the second element is at most $O\left(N d^{2}\right)$ where $d$

Table 2: The description of the benchmark datasets used in our study, where $N$, and $p$ denote the number of samples, and number of features


is the number of distinct values of a discrete features. Hence, the overall computational complexity of the proposed method is $O\left(N p^{2} d^{2}\right)$ where $N$ is the number of samples. The practical assumptions on limits MAXDEPTH $\leq$ 5 and $N C H \leq 15$ reduce the time complexity of SLFS to $O\left(N p d^{2}\right)$. In fact, the SLFS benefits from the optimum time complexity versus the other works such as fast osfs [7], mrmr [6], and alpha-investing [40] based on relation $d<|S|<K$. While the computational complexity of the chisquare based method [41] is less than the SLFS algorithm, it suffers from the greedy ranking based approach. The proposed algorithm takes advantage the independency of learning algorithms in the feature selection process. In addition, the computational complexity of the SLFS method is much less than the wrapper-based evaluation techniques.

# 5. Experiments 

In this section we provide the experimental evaluation of the proposed approach versus the other well-known methods through a variety of different frequently used datasets.

### 5.1. Datasets description

To evaluate the proposed SLFS method, we have used a bunch of benchmark datasets which have been applied in many works such as $[21,7,6,37,5]$. The different datasets include small to large number of features and observations in two-category or multi-category classification problems. A summary

of the datasets are given in Table 2 available online from UCI repository [42]. ARCENE is a two-class classification dataset with continuous input variables to distinguish cancer versus normal patterns. BreastCancer data samples consist of visually assessed nuclear features of fine needle aspirates (FNAs) taken from patients' breasts. The aim is to predict the presence or absence of a malignant tumor from the FNA results based on real-valued input variables. Dexter is a two-class dataset with sparse continuous input variables to filter text corpus in "corporate acquisitions". Dorothea is a drug discovery dataset where chemical compounds represented by structural molecular features must be classified as active (binding to thrombin) or inactive. Isolet dataset contains 150 subjects who spoke the name of each letter of the alphabet twice. The aim of this study was to predict which lettername was spoken. Madelon is a two-category classification dataset presented in the feature selection challenge of NIPS 2003. This dataset suffers from the high dimensionality of number of features and samples simultaneously. Because of the mixing the data by adding noise, flipping labels, shifting and rescaling, it resulted in a hard dataset for feature selection task. The Voting data comprises voting information for 435 samples where each one is about a person voting on 16 issues. The aim is to classify a person as republican or democrat based on these categorical features. Yeast dataset contains information about a set of Yeast cells. The target is to specify the localization site of each cell among 10 possible alternatives. Letter is a dataset of 20000 black and white rectangular pixel displays of one of the 26 capital letters of English alphabet. The aim is to recognize the right letter for unseen observations of images. Most of these datasets are presented in feature selection challenge held in NIPS [43].

# 5.2. The experimental setting 

We compare our algorithm with the well-known methods, MRMR [6], OSFS [7], Alpha-investing [40] and Chi-Square [41] based on prediction accuracy. To compare the performance of proposed method with other feature selection algorithms 10 -fold cross-validation is used in our experiments. The discretization step of the proposed approach is performed based on [44].

We perform a case study on Isolet dataset with three different MAXDEPTH values to sensitivity analysis of the proposed approach on the MAXDEPTH parameter. Based on results in Table 3, the SLFS method is less sensitive to this parameter as a cut depth in TBN construction.

Table 3: The sensitivity analysis of SLFS algorithm to its parameters for Isolet dataset, where NCH, lambda, MAXDEPTH and NSF are largest number of child for each node, Value of $\lambda$ in primary criteria (7), the depth cut and the number of selected features.


Because of the search strategy of the SLFS method is independent of the classification algorithms, and so we expect that the proposed approach meet the good prediction accuracy based on the different classifiers. For this aim, three well-known classification algorithms, support vector machine (SVM) [45], k nearest neighbor (KNN) [3], and Naive Bayes (NB) [46] have been applied to test the algorithms.
![img-5.jpeg](img-5.jpeg)

Figure 6: The prediction accuracy with KNN $(\mathrm{K}=3)$ classifier on selected subset of features by the specified algorithms

# 5.3. Experimental results 

We apply KNN and SVM classifiers on the selected subset of features and report the average prediction accuracy in the performed experiments. In line

![img-6.jpeg](img-6.jpeg)

Figure 7: The prediction accuracy with KNN $(\mathrm{K}=5)$ classifier on subset of features by the specified algorithms
![img-7.jpeg](img-7.jpeg)

Figure 8: The prediction accuracy with KNN $(\mathrm{K}=7)$ classifier on subset of features by the specified algorithms
with the two used classifier on the selected subset of features in Fig. 6 to Fig 9, we compare our induced Bayesian network classifier, hereafter called as "BNSLFS", with NB applied on the selected subset of features from the other feature selection approaches presented in Fig. 10. The prediction accuracy, the number of correctly classified samples over the total number of samples, is used as the performance measure in the experiments. We have used 10 -fold cross validation techniques to get the average reported prediction accuracy.

In the plots, the x -axis denotes the dataset, and the y -axis denotes the average prediction accuracy based on 10 -fold cross validation on the selected subset of features by the specified feature selection algorithm.
![img-8.jpeg](img-8.jpeg)

Figure 9: The prediction accuracy with SVM classifier on subset of features by the specified algorithms

Fig. 6 to Fig. 8 show the results of the KNN based classifier with $K=$ $3,5,7$ run on the applied feature selection techniques. Fig. 6 shows the prediction accuracy of our method is better than the others based on 3NN classifier on the selected subset of features in the BreastCancer, Isolet, Voting, Yeast and Letter datasets. In addition, the SLFS is performed equally or slightly weaker than the other methods based on ARCENE, Madelon, Dorothea and Dexter in Fig. 6.

The results of the 5-NN classifier in Fig. 7 based on selected features of SLFS show superior or just as the other feature selection algorithms. In addition, the Fig. 8 shows that the SLFS based 7-NN classifier is superior to the other methods on the Isolete, Voting, BreastCancer, Dexter, Yeast and Letter dataset. In addition, the SLFS based 7-NN results are slightly weaker than the fast-osfs and fsmrmr methods based classifier on the Madelon dataset.

Fig. 9 shows the results of SVM classifier based on the feature selection techniques. We have used SVM classifier based on a linear polynomial kernel form LIBSVM software [47]. We can observe that the SVM based on SLFS method, performs better than the other SVM based feature selection techniques in BreastCancer, Isolet, Voting, and Dexter, Yeast and Letter.

Furthermore, the SLFS is performed equally or slightly weaker than the other methods based on ARCENE, Madelon, Dorothea in Fig. 9.
![img-9.jpeg](img-9.jpeg)

Figure 10: The prediction accuracy comparison between the Naive Bayes classifier on selected subset of features of the other specified algorithms and BNSLFS classifier on selected features obtained by our approach

In line with the aim of feature selection with the SLFS algorithm, the SLFS provides us an induced Bayesian network classifier (BNSLFS) on the training dataset. To compare with the other methods, the Naive Bayes is used for the other feature selection techniques. The results are presented in Fig. 10. These results show us the superiority of the BNSLFS than the other techniques for the ARCENE, Isolet, Yeast and Letter datasets.

The earlier results in Fig. 6 through Fig. 9 based on KNN and SVM classifiers showed us that the best performance of the classifiers based on our feature selection approach have been occurred on the multi-category datasets. Moreover, the BNSLFS is significantly better than the other techniques on the Isolet dataset comprising very noisy data that confirms the strength of graphical structure learning among the features through the process of SLFS method. Not only the BNSLFS classifier benefits from the no need of the added cost of classifier training on the selected subset of features, but its performance also shows reasonable accuracy as compared with the other well-known methods.

The Bayesian network structures can be used for knowledge discovery and density estimation tasks where the aim of the former is to discover the complex structure among features and the primary aim of the latter is to

![img-10.jpeg](img-10.jpeg)

Figure 11: The Bayesian networks of two datasets, BreastCancer in (a) and Voting in (b) with MAXDEPTH $=4$.

discover the features relationships to compute the joint distributions among them for learning tasks such as classification and model based clustering [10]. While in this study we focused on the structure learning for feature selection and classification aims, the proposed method can be applied for knowledge discovery task such as understanding the complex phenomenon including the genes and DNA arrays. Here, we present two graph structures for the "Voting" and "BreastCancer" datasets in Figure 11. The obtained Bayesian network for these datasets demonstrates the relationship among the selected features, and the strength of effects of them on the class variable. In line with the reduction of high dimensional dataset with huge number of features in the SLFS procedure, it can enable us to apply the Bayesian network for knowledge discovery and structure representation for illustration the complex phenomena.

# 6. Conclusion 

In this paper we have developed a novel feature selection technique based on integrating the structure learning and the Markov blanket optimal theoretical concept. While the typical feature selection methods have suffered from the greedy or pairwise methods for distinguishing between the redundant and non-redundant features, the SLFS approach allowed us to identify redundant features with the aid of TBN's. In line with the theoretical works for deriving the SLFS algorithm, the optimality of the selected features based on this approach was presented through a variety of benchmark datasets. The experimental results based on SVM and KNN classifiers trained on the selected subset of features, showed us the superiority of prediction accuracy of classification through the SLFS feature selection algorithm as compared with the other feature selection methods. In line with a better local optimum set of features according to the proposed approach rather than the other techniques, our feature selection approach was provided a Bayesian network classifier without the additional cost of classifier training on the selected features dissimilar to the typical supervised feature selection methods. Furthermore, the BNSLFS performance on the benchmark dataset showed the better or equal accuracy of it versus the Naive Bayes classifier on the selected features according to other feature selection methods.
There exist suggestions for future works to extend this research such as follows,

- Statistical significance of the selected features of the SLFS algorithm based on statistical hypothesis tests
- The comparison of the proposed approach with the other structure learning techniques such as Tree augmented Naive Bayes (TAN)
- Generalization of the other feature selection techniques through the framework of probabilistic graphical models

