# Article 

## General and Local: Averaged $k$-Dependence Bayesian Classifiers

Limin Wang ${ }^{1, *}$, Haoyu Zhao ${ }^{2}$, Minghui Sun ${ }^{1}$ and Yue Ning ${ }^{1}$<br>${ }^{1}$ Key Laboratory of Symbolic Computation and Knowledge Engineering of Ministry of Education, Jilin University, ChangChun 130012, China; E-Mails: smh@jlu.edu.cn (M.S.); ningyue@jlu.edu.cn (Y.N.)<br>${ }^{2}$ School of Software, Jilin University, ChangChun 130012, China; E-Mail: zhaohw@jlu.edu.cn<br>* Author to whom correspondence should be addressed; E-Mail: wanglim@jlu.edu.cn;<br>Tel.: +86-431-85626892.<br>Academic Editors: Carlos Alberto de Bragança Pereira and Adriano Polpo

Received: 4 May 2015 / Accepted: 9 June 2015 / Published: 16 June 2015


#### Abstract

The inference of a general Bayesian network has been shown to be an NP-hard problem, even for approximate solutions. Although $k$-dependence Bayesian (KDB) classifier can construct at arbitrary points (values of $k$ ) along the attribute dependence spectrum, it cannot identify the changes of interdependencies when attributes take different values. Local KDB , which learns in the framework of KDB , is proposed in this study to describe the local dependencies implicated in each test instance. Based on the analysis of functional dependencies, substitution-elimination resolution, a new type of semi-naive Bayesian operation, is proposed to substitute or eliminate generalization to achieve accurate estimation of conditional probability distribution while reducing computational complexity. The final classifier, averaged $k$-dependence Bayesian (AKDB) classifiers, will average the output of KDB and local KDB. Experimental results on the repository of machine learning databases from the University of California Irvine (UCI) showed that AKDB has significant advantages in zero-one loss and bias relative to naive Bayes (NB), tree augmented naive Bayes (TAN), Averaged one-dependence estimators (AODE), and KDB. Moreover, KDB and local KDB show mutually complementary characteristics with respect to variance.


Keywords: $k$-dependence Bayesian classifier; substitution-elimination resolution; functionaldependency rules of probability

# 1. Introduction 

Bayesian networks (BNs), which were introduced by Pearl [1], can encode dependencies among all variables. Their success has led to a recent flurry of algorithms for learning BNs from data [2-5]. $B N=<N, A, \Theta>$ is a directed acyclic graph with a conditional probability distribution for each node, collectively represented by $\Theta$ that quantifies how much a node depends on its parents. Each node $n \in N$ represents a domain variable, and each arc $a \in A$ between nodes represents a probabilistic dependency. A BN can be used as a classifier that characterizes the joint distribution $P(\mathbf{x}, y)$ (In the following discussion, lower-case letters denote specific values taken by corresponding attributes. For instance, $x_{i}$ represents the event that $X_{i}=x_{i}$ ) of class variable $Y$ and a set of attributes $\mathbf{X}=\left\{X_{1}, X_{2}, \cdots, X_{n}\right\}$, and predicts the class label with the highest conditional probability. Denoting the parent nodes of $x_{i}$ by $P a\left(x_{i}\right)$, the joint distribution $P_{B}(\mathbf{x}, y)$ can be represented by factors over the network structure $B$, as follows:

$$
P_{B(\mathbf{x}, y)}=\prod_{i=1}^{n} P\left(x_{i} \mid P a\left(x_{i}\right)\right)
$$

The inference of a general BN has been shown to be an NP-hard problem [6] even for approximate solutions [7]. However, learning unrestricted BNs does not necessarily lead to a classifier with good performance. For example, naive Bayes (NB) [8] is the simplest BN, which considers only the dependence between each attribute $X_{i}$ and the class variable $Y$. However, Friedman et al. [9] observed that unrestricted BN classifiers do not outperform NB in a large sample of benchmark data sets. Many BN classifiers have been proposed to overcome the limitation of NB. One practical approach for structure learning is to impose some restrictions on the structures of BNs, for example, learning tree-like structures. Sahami [10] proposed to describe the limited dependence among variables within a general framework, which is called $k$-dependence Bayesian (KDB) classifier. Friedman et al. [9] proposed tree augmented naive Bayes (TAN), a structure-learning algorithm that learns a maximum spanning tree from the attributes. Conditional mutual information is applied in these two algorithms to measure the weight of arcs between predictive attributes. When data size becomes larger, the superiority in high-dependence representation helps KDB obtain better classification performance than TAN.

The key differences between Bayesian classifiers are their structure-learning algorithms. Many criteria, such as Bayesian scoring function [11], minimal description length (MDL) [12] and Akaike Information Criterion (AIC) [13], have been proposed to find out one global graph structure $B_{G}$ that best characterizes the true distribution of given data. Considering the time and space complexity overhead, only a limited number of conditional probabilities can be encoded in BN. All credible dependencies must be represented to obtain a more accurate estimation of the true joint distribution. However, these criteria can only approximately measure the overall interdependencies between attributes, but cannot identify the change of interdependencies when attributes take different values. Thus the candidate graph structures may have very close score values and are non-negligible in the posterior sense [14]. To extend the limited representation of $B_{G}$, some researchers proposed to aggregate several candidate BNs together. Averaged one-dependence estimators (AODE), which were proposed by Webb et al. [15], aggregate the predictions of all qualified restricted class of one-dependence estimators. Zheng et al. [16] proposed subsumption resolution (SR), to efficiently identify occurrences of the specialization-generalization relationship and eliminate generalizations at classification time. By introducing Functional Dependency (FD) analysis

into the learning procedures, the model interpretability and robustness of different Bayesian classifiers can be improved greatly. After eliminating highly dependent attribute values by applying FD analysis, the maximal spanning tree (MST) of TAN is rebuilt with the rest of the attribute values for each test instance. Correspondingly the extraneous effect caused by logical relationships between attribute values will be mitigated [17]. To evaluate the feasibility of integrating probabilistic reasoning and logical reasoning into the framework of AODE, we first select the branch nodes of MST as the super parents, then refine AODE by applying FD analysis to delete redundant children attribute [18].

In this paper, local mutual information and conditional local mutual information, which are deduced from classical information theory, are applied to build the local graph structure $B_{L} . B_{L}$ can be considered a complementary part of $B_{G}$, to describe local causal relationships. To construct classifiers at arbitrary points (values of $k$ ) along the attribute dependence spectrum, both $B_{L}$ and $B_{G}$ are built in the framework of KDB model. Substitution-elimination resolution (SER), a new type of semi-naive Bayesian operation is proposed to substitute or eliminate generalization to achieve accurate estimation of conditional probability distribution while reducing computational complexity. SER deals only with specific values and only in the context of other specific values. We prove that this adjustment is theoretically correct and demonstrate experimentally that it can considerably improve zero-one loss, bias and variance.

The remainder of this paper is organized as follows: Section 2 first proposes the background theoryinformation theory and functional dependency rules of probability, and then clarifies the rationality of SER. Section 3 introduces the basic ideas of KDB, local KDB and the proposed algorithm, averaged $k$-dependence Bayesian classifiers (AKDB), which averages the output of KDB and local KDB. Section 4 compares various approaches on data sets from the UCI Machine Learning Repository. Finally, Section 5 presents possible future work.

# 2. Background Theory and Related Research Work 

### 2.1. Information Theory

In the 1940s, Claude E. Shannon introduced information theory [19], the theoretical basis of modern digital communication. Although Shannon was principally concerned with the problem of electronic communications, the theory has a broader applicability. Many commonly used measures are based on the entropy of information theory and used in a variety of classification algorithms.

Definition 1. [19] Entropy of an attribute (or random variable) is a function that attempts to characterize its unpredictability. When given a discrete random variable $X$ with any possible value $x$ and probability distribution function $P(\cdot)$, entropy is defined as follows,

$$
H(X)=-\sum_{x \in X} P(x) \log _{2} P(x)
$$

Deterministic attributes have zero entropy as entropy measures the amount of uncertainty with which they take some values. Similar to the concept of conditional probability, conditional entropy $H(X \mid Y)$ may be understood as the amount of randomness in the random variable $X$ when the value of $Y$ is known.

Definition 2. [19] Given discrete random variables $X$ and $Y$ and their possible values $x$ and $y$, conditional entropy is defined as follows:

$$
H(X \mid Y)=-\sum_{x \in X} \sum_{y \in Y} P(x, y) \log _{2} P(x \mid y)
$$

Using the definition of entropy and conditional entropy, we can calculate the amount of information shared between two attributes. The stronger the correlation, the higher the value of mutual information will be.

Definition 3. [19] The mutual information (MI) $I(X ; Y)$ of two random variables is a measure of the mutual dependence of the variables and is defined as follows:

$$
I(X ; Y)=H(X)-H(X \mid Y)=\sum_{x \in X} \sum_{y \in Y} P(x, y) \log _{2} \frac{P(x, y)}{P(x) P(y)}
$$

Mutual information $I(X ; Y)$ between two attributes $X$ and $Y$ measures the expected reduction in entropy and is nonnegative, i.e., $I(X ; Y) \geq 0 . I(X ; Y)=0$ if they are independent and is maximized if $H(X \mid Y)=0$. Similar to the definition of conditional entropy, conditional mutual information $I(X ; Y \mid Z)$ indicates the amount of information shared between two attributes $X$ and $Y$ when all the values of attribute $Z$ are known.

Definition 4. [19] Conditional mutual information (CMI) $I(X ; Y \mid Z)$ is defined as follows:

$$
I(X ; Y \mid Z)=\sum_{x \in X} \sum_{y \in Y} \sum_{z \in Z} P(x, y, z) \log _{2} \frac{P(x, y \mid z)}{P(x \mid z) P(y \mid z)}
$$

Definition 5. Local mutual information (LMI) $I(X ; y)$ is defined to measure the reduction of entropy about variable $X$ after observing that $Y=y$, as follows:

$$
I(X ; y)=\sum_{x \in X} P(x, y) \log \frac{P(x, y)}{P(x) P(y)}
$$

Definition 6. Conditional local mutual information (CLMI) $I(x ; y \mid Z)$ is defined to measure the amount of information shared between two attribute values $x$ and $y$ when all the values of attribute $Z$ are known, as follows:

$$
I(x ; y \mid Z)=\sum_{z \in Z} P(x, y, z) \log \frac{P(x, y \mid z)}{P(x \mid z) P(y \mid z)}
$$

# 2.2. Functional Dependency Analysis and Substitution-Elimination Resolution 

Given a data set $D$, attribute value $y$ is functionally dependent on attribute value $x$, and $x$ functionally determines $y$ (in symbols $x \rightarrow y$ ). We demonstrated functional dependency rules of probability in $[17,18]$ to build a linkage between probabilistic inference and logical inference, and the following rules are mainly included:

- Representation equivalence of probability: Suppose two attribute values $\{x, y\}$ and $y$ can be inferred by $x$, i.e., the FD $x \rightarrow y$ holds, then the following joint probability distribution holds:

$$
P(x)=P(x, y)
$$

- Augmentation rule of probability: If FD $x \rightarrow y$ holds and $z$ is another attribute value, then the following joint probability distribution holds:

$$
P(x, z)=P(x, y, z)
$$

- Transitivity rule of probability: If FDs $x \rightarrow y$ and $y \rightarrow z$ hold, then the following joint probability distribution holds:

$$
P(x)=P(x, z)
$$

- Pseudo-transitivity rule of probability: If $y z \rightarrow \delta$ and $x \rightarrow y$ hold, then the following joint probability distribution holds:

$$
P(x, z)=P(x, z, \delta)
$$

Definition 7. A k-dependence Bayesian classifier ( $k$-DBC) is a BN that contains the structure of the naive Bayesian classifier and allows each attribute $X_{i}$ to have a maximum of $k$ attribute nodes as parents. Given attribute order $\left\{X_{1}, \cdots, X_{n}\right\}, \operatorname{Pa}\left(X_{i}\right)=\left\{Y, X_{d_{i}}\right\}$ where $X_{d_{i}}$ is a subset of $\left\{X_{1}, \cdots, X_{i-1}\right\}$, $\left|d_{i}\right|=\min \{i-1, k\}$ and $\operatorname{Pa}(y)=\varnothing$.
![img-0.jpeg](img-0.jpeg)

Figure 1. The $k$-dependence relationships between attributes inferred from KDB.

Learning the structure of a $k$-DBC actually means learning an order of variables and then adding arcs from a variable to all the variables ranked after it. In fact, given the order of variables, learning a $k$-DBC is relatively easier.

We consider a hypothetical example with four predictive attributes \{Pregnant, Gender, Familial Inheritance, and Breast Cancer\} and class variable \{Normal\}. When given different $k$ values, the corresponding $k$-DBC models are shown in Figure 1, where $X=\left\{X_{1}, X_{2}, X_{3}, X_{4}\right\}$ and $Y$ denote \{Pregnant, Gender, Familial Inheritance, Breast Cancer\} and class Normal, respectively.

Subsumption is a central concept in Inductive Logic Programming [20], where it is used to identify generalization-specialization relationships between clauses and to support the process of unifying clauses.

Definition 8. (Generalization and specialization) For two attribute values $x_{i}$ and $x_{j}$, if $P\left(x_{j} \mid x_{i}\right)=1.0$ then $x_{j}$ is a generalization of $x_{i}$ and $x_{i}$ is a specialization of $x_{j}$.

Suppose that Gender has two values: female and male, and Pregnant has two values: yes and no. If Pregnant $=$ yes, it follows that Gender $=$ female. Therefore, Gender $=$ female is a generalization of Pregnant $=$ yes, i.e., FD: $\{$ Gender $=$ female $\} \rightarrow\{$ Pregnant $=$ yes $\}$ holds.

Theorem 1. Substitution resolution: Suppose that for $k$-DBC the attribute order is $\left\{X_{1}, X_{2}, \cdots, X_{n}\right\}$ and $X_{i}(i>k)$ should select $k$ attributes as parents. If $x_{p}$ is a generalization of $x_{q}\left(x_{p}, x_{q} \in P a_{i}\right)$, then for $\forall x_{t} \notin P a_{i}(t<i), x_{t}$ as a substitute of $x_{p}$ will help achieve a more accurate approximate estimation of probability distribution.

Proof. For $k$-DBC, conditional probability $P\left(x_{i} \mid P a_{i}, y\right)$ can be considered an approximate estimation of $P\left(x_{i} \mid x_{1}, \cdots, x_{i-1}, y\right)$. Evidently, $P\left(x_{i} \mid P a_{i}, x_{t}, y\right)$ will be more accurate than $P\left(x_{i} \mid P a_{i}, y\right)$, where $x_{t} \notin P a_{i}$ and $t<i$. If $x_{p}$ is a generalization of $x_{q}\left(x_{p}, x_{q} \in P a_{i}\right)$, by applying the augmentation rule of probability we will have $P\left(x_{i} \mid P a_{i}, y\right)=P\left(x_{i} \mid P a_{i}-x_{p}, y\right)$, where " - " denotes set difference. To retain the $k$-dependence restriction, we need to select $x_{t}$ as a substitute of $x_{p}$.

The example presented in Figure 1 illustrates this relationship. The joint probability distribution of the full Bayesian classifier, as shown in Figure 1c, is expressed as follows:

$$
P(y, \mathbf{x})=P(y) P\left(x_{1} \mid y\right) P\left(x_{2} \mid y, x_{1}\right) P\left(x_{3} \mid y, x_{1}, x_{2}\right) P\left(x_{4} \mid y, x_{1}, x_{2}, x_{3}\right)
$$

In addition, the joint probability distribution of 2-DBC, as Figure 1b shows, is as follows,

$$
P(y, \mathbf{x})=P(y) P\left(x_{1} \mid y\right) P\left(x_{2} \mid y, x_{1}\right) P\left(x_{3} \mid y, x_{1}, x_{2}\right) P\left(x_{4} \mid y, x_{1}, x_{2}\right)
$$

By comparing Equation (12) and Equation (13) we can observe that, Equation (13) uses $P\left(x_{4} \mid y, x_{1}, x_{2}\right)$ to obtain an approximate estimation of $P\left(x_{4} \mid y, x_{1}, x_{2}, x_{3}\right)$. Gender $=$ female is a generalization of Pregnant $=$ yes. Thus, $P($ Gender $=$ female $\mid$ Pregnant $=$ yes $)=1$ or $P\left(x_{2} \mid x_{1}\right)=1$. By applying the augmentation rule of probability, we derive the following equations:

$$
\begin{aligned}
P\left(x_{4} \mid y, x_{1}, x_{2}, x_{3}\right) & =\frac{P\left(x_{4}, y, x_{1}, x_{2}, x_{3}\right)}{P\left(y, x_{1}, x_{2}, x_{3}\right)} \\
& =\frac{P\left(x_{4}, y, x_{1}, x_{3}\right)}{P\left(y, x_{1}, x_{3}\right)} \\
& =P\left(x_{4} \mid y, x_{1}, x_{3}\right)
\end{aligned}
$$

and

$$
\begin{aligned}
P\left(x_{3} \mid y, x_{1}, x_{2}\right) & =\frac{P\left(x_{3}, y, x_{1}, x_{2}\right)}{P\left(y, x_{1}, x_{2}\right)} \\
& =\frac{P\left(x_{3}, y, x_{1}\right)}{P\left(y, x_{1}\right)} \\
& =P\left(x_{3} \mid y, x_{1}\right)
\end{aligned}
$$

Equation (12) will change to be,

$$
P(y, \mathbf{x})=P(y) P\left(x_{1} \mid y\right) P\left(x_{2} \mid y, x_{1}\right) P\left(x_{3} \mid y, x_{1}\right) P\left(x_{4} \mid y, x_{1}, x_{3}\right)
$$

Thus for Equation (13), if we use $x_{3}$ to substitute $x_{2}$ in $P a_{4}$ and $\varnothing$ to substitute $x_{2}$ in $P a_{3}$, corresponding 2-DBC as shown in Figure 2a is just the same as the full Bayesian classifier for the instances where Pregnant $=$ yes holds. Thus we can obtain a more accurate estimation of $P(y, \mathbf{x})$ and the 2 -dependence restriction still retained.
![img-1.jpeg](img-1.jpeg)
(a) After substitution resolution
![img-2.jpeg](img-2.jpeg)
(b) After elimination resolution

Figure 2. The 2-dependence relationships between attributes after substitution-elimination resolution.

Theorem 2. Elimination resolution: For $\forall x_{p} \in P a_{i}$, if $x_{i}$ is a generalization of $x_{p}$, then $P\left(x_{i} \mid P a_{i}\right)=1.0$ and the factor $P\left(x_{i} \mid P a_{i}\right)$ will be eliminated from the joint probability distribution.

For example, Equations (12) and (13) both use the factor $P\left(x_{2} \mid x_{1}, y\right)$. If $x_{2}$ is a generalization of $x_{1}$, then, by applying the augmentation rule of probability, we derive the following equation:

$$
\begin{aligned}
P\left(x_{2} \mid x_{1}, y\right) & =\frac{P\left(x_{2}, y, x_{1}\right)}{P\left(y, x_{1}\right)} \\
& =\frac{P\left(y, x_{1}\right)}{P\left(y, x_{1}\right)}=1
\end{aligned}
$$

Thus, Equation (16) can be rewritten as follows:

$$
P(y, \mathbf{x})=P(y) P\left(x_{1} \mid y\right) P\left(x_{3} \mid y, x_{1}\right) P\left(x_{4} \mid y, x_{1}, x_{3}\right)
$$

The corresponding Bayesian structure is shown in Figure 2b. When two attributes are strongly related, the classifier may overweigh the inference from the two attributes, which results in prediction bias. FDs will help avoid this situation, and the high-dimensional representation or even entire classification model is simplified and improved.

# 3. KDB, Local KDB and AKDB 

KDB allows us to construct classifiers at arbitrary points (values of $k$ ) along the feature dependence spectrum, while also capturing most of the computational efficiency of the naive Bayesian model. Thus KDB presents an alternative to the general trend in BN learning algorithms that conducts an expensive search through the space of network structures.

KDB is supplied with both a database of pre-classified instances, DB , and the $k$ value for the maximum allowable degree of feature dependence. The KDB outputs a $k$-dependence Bayesian classifier with conditional probability tables determined from the input data. The algorithm is as follows:

## Algorithm 1 KDB.

1. For each attribute $X_{i}$, compute $M I, I\left(X_{i} ; Y\right)$, where $Y$ is the class.
2. Compute class CMI $I\left(X_{i} ; X_{j} \mid Y\right)$ for each pair of attributes $X_{i}$ and $X_{j}$, where $i \neq j$.
3. Let the used variable list, $S$, be empty.
4. Let the Bayesian network being constructed, $B N$, begin with a single class node, $Y$.
5. Repeat until $S$ includes all domain attributes
5.1. Select feature $X_{\max }$ which is not in $S$ and has the highest value $I\left(X_{\max } ; Y\right)$.
5.2. Add a node to $B N$ representing $X_{\max }$.
5.3. Add an arc from $Y$ to $X_{\max }$ in $B N$.
5.4. Add $m=\min (|S|, k)$ arcs from $m$ distinct attributes $X_{j}$ in $S$ with the highest value for $I\left(X_{\max } ; X_{j} \mid Y\right)$.
5.5. Add $X_{\max }$ to $S$.
6. Compute the conditional probability tables inferred by the structure of $B N$ by using counts from $D B$, and output $B N$.

From Definitions 3-6, we can obtain the following results:

$$
\left\{\begin{array}{l}
I\left(X_{i} ; Y\right)=\sum_{X_{i}} I\left(x_{i} ; Y\right) \\
I\left(X_{i} ; X_{j} \mid Y\right)=\sum_{X_{i}} \sum_{X_{j}} I\left(x_{i} ; x_{j} \mid Y\right)
\end{array}\right.
$$

$M I$ and $C M I$ are commonly applied to roughly measure the direct or conditional relationships between predictive attributes and class variable $Y$. However, in the real world, the relationships between attributes may differ significantly as the situation changes. For some instances attributes $A$ and $B$ are highly related. Meanwhile, for other instances, $A$ is independent of $B$, but highly related to attribute $Y$. Considering the relationships among attributes Gender, Pregnant and Breast Cancer, Gender = female and Breast Cancer=yes are highly related. By contrast, if Gender = female, then we cannot make any definite conclusion about the value of Pregnant, nor about the value of Gender if Breast Cancer= no. Note that traditional Bayesian classifier, e.g., KDB, which is learned based on classical information theory, cannot describe such interdependencies. However, LMI and CLMI can be used to identify the dynamic changes, thus making the final model much more flexible.

As shown in Figure 3, for the first instance, the attribute value $x_{2}$ is independent of other attribute values and the local relationship between $\left\{x_{1}, x_{3}\right\}$ and class variable $Y$ is just like a triangle. For the $i_{t h}$ instance, $\left\{x_{2}, x_{3}\right\}$ are independent of $Y$, and the local relationship between $x_{1}$ and $Y$ is just like an

oval. For the last instance, $x_{3}$ is independent of other attribute values and the local relationship between $\left\{x_{1}, x_{2}\right\}$ and $Y$ is just like a broken line. If all situations are considered together, then the overall relationship between attributes $\left\{X_{1}, X_{2}, X_{3}\right\}$ and class variable $Y$ is just like a rectangle.
![img-3.jpeg](img-3.jpeg)

Figure 3. The basic and local relationships among $\left\{X_{1}, X_{2}, X_{3}\right\}$ and $Y$.

KDB learns the basic relationships of full BN. In the first two learning steps of KDB, if $I(Y ; X)$ and $I\left(X_{i} ; X_{j} \mid Y\right)$ are replaced by $I(Y ; x)$ and $I\left(x_{i} ; x_{j} \mid Y\right)$ respectively, then the local KDB that describes the local relationships of each test instance can be inferred. On the basis of this, FD analysis is introduced into the learning procedure to improve model robustness.

The learning procedure of the local KDB is described as follows:
Algorithm 2 Local KDB.
For each test instance $\mathbf{x}=\left\{x_{1}, x_{2}, \cdots, x_{n}\right\}$

1. For each attribute value $x_{i} \in \mathbf{x}$, compute $L M I, I\left(x_{i} ; Y\right)$, where $Y$ is the class.
2. Compute CLMI $I\left(x_{i} ; x_{j} \mid Y\right)$ for each pair of attribute values $x_{i}$ and $x_{j}$, where $i \neq j$ and $x_{i}, x_{j} \in \mathbf{x}$.
3. Let the used variable list, $S$, be empty.
4. Let the Bayesian network being constructed, $B N$, begin with a single class node, $Y$.
5. Repeat until $S$ includes all attribute values
5.1. Select attribute value $x_{\max }$ which is not in $S$ and has the highest value $I\left(x_{\max } ; Y\right)$.
5.2. Add a node to $B N$ representing $x_{\max }$.
5.3. Add an arc from $Y$ to $x_{\max }$ in $B N$.
5.4. Add $m=\min (|S|, k)$ arcs from $m$ distinct attribute values $x_{j}$ in $S$ with the highest value for $I\left(x_{\max } ; x_{j} \mid Y\right)$.
5.5. Add $x_{\max }$ to $S$.
6. Apply SER to substitute generalization or eliminate redundant conditional probability.
7. Compute the conditional probability tables inferred by the structure of $B N$ by using counts from $D B$, and output $B N$.

The final classifier, AKDB, estimates the class membership probabilities by averaging KDB and local KDB classifiers. The basic idea of AKDB can be explained from the perspective of medical diagnosis. KDB describes the basic relationships between different symptoms that can be explained

by domain knowledge learned from book or in school. Meanwhile, the local KDB describes the possible relationships between different symptoms of a specific patient. To make a definite diagnosis, rich experience (which corresponds to robust KDB model) and flexible mind (which corresponds to dynamic local KDB model) are both necessary and important.

FDs require a method for inferring from the training data whether one attribute value is a generalization of another. FDs use the following criterion:

$$
\left|T_{x_{i}}\right|=\left|T_{x_{i}, x_{j}}\right| \geq l
$$

to infer that $x_{j}$ is a generalization of $x_{i}$, where $\left|T_{x_{i}}\right|$ is the number of training cases with value $x_{i},\left|T_{x_{i}, x_{j}}\right|$ is the number of training cases with both values, and $l$ is a user-specified minimum frequency. A large number of deterministic attributes, which are on the left side of the FD, will increase the risk of incorrect inference, and at the same time need more computer memory to store credible FDs. Consequently, only the one-one FDs are selected in our current work. Besides, as no formal method has been used to select an appropriate value for $l$, we use the same setting as that proposed by Webb [15], i.e., $l=100$, which is achieved from empirical studies.

The learning framework of local KDB is described as follows. During training time, FD analysis is applied to detect all possible specialization-generalization relationships. During classification time, local KDB first builds the basic network structure for each test instance $t$; then selects the specializationgeneralization relationships that hold in $t$, and applies SER to refine the network structure. From the definitions of local mutual information and FD we can see that, they both deal with attribute values rather than attributes. In the real world the interdependencies may be varied when attributes take different values. As for some test instances attributes $X_{i}$ and $X_{j}$ are independent, for other test instances $X_{i}$ may be dependent on $X_{j}$. Classical Bayesian classifiers, e.g., TAN and KDB, which build the network structure by computing mutual information and conditional mutual information, cannot resolve such situations. Whereas local KDB helps to remedy this limitation.

Another feature of our algorithm which makes it very suitable for data mining domains is its relatively small computational complexity. Computing the actual network structure of KDB requires $O\left(n^{2} m c v^{2}\right)$ time (dominated by Step 2) and that of Local KDB only requires $O\left(n^{2} m c\right)$ time, where $n$ is the number of attributes, $m$ is the number of training instances, $c$ is the number of classes, and $v$ is the average number of discrete values that an attribute may take. Moreover, classifying an instance both KDB and local KDB require $O(n c k)$ time. Forming the additional two-dimensional probability estimate table SER requires $O\left(m n^{2} v^{2}\right)$ time. Classification of a single instance requires considering each pair of attributes to detect dependencies and is of time complexity $O(c n)$.

# 4. Experiments 

### 4.1. Bias and Variance

The classification of each case in the test set is done by choosing, as class label, the value of the class variable that has the highest posterior probability. Classification accuracy is measured by the percentage of correct predictions on the test sets (i.e., using a zero-one loss function). Kohavi and Wolpert presented a bias-variance decomposition of the expected misclassification rate [21], which is a powerful tool from

sampling theory statistics for analyzing supervised learning scenarios. Suppose $y$ and $\hat{y}$ are the true class label and that generated by a learning algorithm, respectively, the zero-one loss function is defined as:

$$
\xi(y, \hat{y})=1-\delta(y, \hat{y})
$$

where $\delta(y, \hat{y})=1$ if $\hat{y}=y$ and zero otherwise. The bias term measures the squared difference between the average output of the target and the algorithm. This term is defined as follows:

$$
\text { bias }=\frac{1}{2} \sum_{\hat{y}, y \epsilon Y}[P(\hat{y} \mid \mathbf{x})-P(y \mid \mathbf{x})]^{2}
$$

where $\mathbf{x}$ is the combination of any attribute value. The variance term is a real valued non-negative quantity and equals zero for an algorithm that always makes the same guess regardless of the training set. The variance increases as the algorithm becomes more sensitive to changes in the training set. It is defined as follows:

$$
\text { variance }=\frac{1}{2}\left[1-\sum_{\hat{y} \epsilon Y} P(\hat{y} \mid \mathbf{x})^{2}\right]
$$

# 4.2. Statistical Results on UCI Data Sets 

In order to verify the efficiency and effectiveness of the proposed AKDB, we conduct experiments on 41 data sets from the UCI machine learning repository. Table 1 summarizes the characteristics of each data set, including the number of instances, attributes and classes. Large data sets with an instance number greater than 3000 are annotated with the symbol "*". Missing values for qualitative attributes are replaced with modes, and those for quantitative attributes are replaced with means from the training data. For each benchmark data set, numeric attributes are discretized using Minimum Description Length discretization [22]. The following techniques are compared:

- NB, standard naive Bayes.
- TAN, tree-augmented naive Bayes.
- AODE, AODE with subsumption resolution.
- KDB, standard $k$-dependence Bayesian classifier.
- TAN-FDA [17], a variation of TAN that rebuilds MST for each testing instance.
- AODE-SR [18], a variation of AODE that selects super parent and delete extraneous children attributes.
- LKDB (Local KDB), a variation of KDB that describes the local dependencies among attributes.
- AKDB, a combination of KDB and local KDB.

All algorithms were coded in MATLAB 7.0 on a Pentium 2.93 GHz/2GB RAM computer. Base probability estimates $P(y)$ and $P\left(x_{j} \mid y\right)$ with Laplace correction are defined as follows,

$$
\left\{\begin{array}{l}
\hat{P}(y)=\frac{\sum_{i=1}^{N} \delta\left(y_{i}, y\right)+1}{N+t} \\
\hat{P}\left(x_{j} \mid y\right)=\frac{\sum_{i=1}^{N} \delta\left(x_{i j}, x_{j}\right) \delta\left(y_{i}, y\right)+1}{\delta\left(y_{i}, y\right)+t_{j}}
\end{array}\right.
$$

where $N$ is the number of training instances, $t$ is the number of classes, $y_{i}$ is the class label of the $i_{t h}$ training instance, $t_{j}$ is the number of values of the $j_{t h}$ attribute, $x_{i j}$ is the $j_{t h}$ attribute value of the $i_{t h}$ training instance, $x_{j}$ is the $j_{t h}$ attribute value of the test instance, and $\delta(\cdot)$ is a binary function, which is one if its two parameters are identical and zero otherwise. Thus, $\sum_{i=1}^{N} \delta\left(y_{i}, y\right)$ is the frequency that the class label $y$ occurs in the training data and $\sum_{i=1}^{N} \delta\left(x_{i j}, x_{j}\right) \delta\left(y_{i}, y\right)$ is the frequency that the class label $y$ and the attribute value $x_{j}$ occurs simultaneously in the training data.

Table 2 presents for each data set the average zero-one loss, which is estimated by 10 -fold crossvalidation to obtain an accurate estimation of the average performance of an algorithm. The average bias and variance results are shown in Tables 3 and 4, respectively, in which only 15 large data sets are selected because of statistical significance. The average zero-one loss, bias or variance across multiple data sets provides a gross measure of relative performance. Statistically, a win/draw/loss (W/D/L) record is calculated for each pair of competitors $A$ and $B$ with respect to performance measure $M$. The record represents the number of data sets in which $A$ either beats, loses to or ties with $B$ on $M$. We assess a difference as significant if the outcome of a one-tailed binomial sign test is less than 0.05 . Tables 5, 6 and 7 show the W/D/L records that correspond to zero-one loss, bias and variance, respectively.

Allowing more dependencies for KDB reduces zero-one loss significantly more often than it increases. As more attributes are utilized for classification, the increase in the value of $k$ will help ensure that more causal relationships will appear and be expressed in the joint probability distribution. By contrast, the AODE family, e.g., AODE and AODE-SR, which utilize a restricted class of one-dependence estimators (ODEs), aggregates the predictions of all qualified estimators within this class. The superiority of AODE family over single-structure classifiers, e.g., TAN, TAN-FDA and KDB, that are learned on the basis of classical information theory, can be attributed to the superiority of the aggregating mechanism. From Table 5 we observed that, AKDB, which is the combination of KDB and local KDB, enjoys a significant zero-one loss advantage relative to other algorithms. Moreover, we applied Friedman test $(F T)$ [23,24], which is a non-parametric measure, to rank and compare the algorithms. $F T$ helps to compare and evaluate the overall prediction performance of different learning algorithms when dealing with numerous data sets. The best performing algorithm getting the rank of 1 , the second best rank $2, \cdots$. In case of ties, average ranks are assigned. Let $r_{i}^{j}$ be the rank of the $j$-th of $k$ algorithms on the $i$-th of $N$ data sets. $F T$ compares the average ranks of algorithms, $R_{j}=\frac{1}{N} \sum_{i} r_{i}^{j}$. The experimental results of $F T$ are shown in Table 8, from which we can see that, the order of these algorithms is \{AKDB, AODE-SR, AODE,TAN-FDA, LKDB, KDB, TAN, NB\} when comparing the experimental results on all data sets. Thus the effectiveness of AKDB is proved from the perspective of $F T$.

We need to further evaluate whether local KDB works as an effective complementary part of AKDB. The relative zero-one loss/bias/variance ratio $\varrho(\cdot)$ is proposed to measure the extent to which local KDB helps to improve the performance of KDB. A higher value of the ratio $\varrho(\cdot)$ corresponds to a smaller ratio of AKDB and KDB, which indicates the better performance of AKDB.

$$
\begin{cases}\varrho(Z)=1-\frac{\text { zero - one loss of } A K D B}{\text { zero - one loss of } K D B} \\ \varrho(B)=1-\frac{\text { bias of } A K D B}{\text { bias of } K D B} \\ \varrho(V)=1-\frac{\text { variance of } A K D B}{\text { variance of } K D B}\end{cases}
$$

Table 1. Data sets.


Table 2. Experimental results of $0-1$ loss.


Table 3. Experimental results of bias.


Table 4. Experimental results of variance.


Table 5. W/D/L comparison results of $0-1$ loss on all data sets.


Table 6. W/D/L comparison results of bias on large data sets.


Table 7. W/D/L comparison results of variance on large data sets.


The data sets, in which AODE performs better than KDB, are selected for comparison. Figures 4 and 5 show the experimental results of $\varrho(\cdot)$ with respect to zero-one loss, bias and variance. The index numbers of data sets in Figures 4 and 5, which correspond to that described in Table 1. From Figure 4, we can see clearly that, local KDB works for all the data sets regardless of whether the data size is small or large.

Table 8. Ranks of different classifiers.


Bias can be used to evaluate the extent to which the final model learned from training data fits the entire data set. From Table 6, we can see that the fitness of NB is the poorest because its structure is

definite regardless of the true data distribution. AKDB still performs the best, although the advantage is not significant. By calculating CMI from the global viewpoint and calculating CLMI from the local point, the aggregating mechanism can help AKDB make full use of the information that is supplied by the training data and test instance. The complicated relationship among attributes are measured and depicted from the viewpoint of information theory. Thus, performance robustness can be achieved. In two data sets, the KDB performs more poorly than AODE. From Figure 5, we observed that AKDB works in one data set.
![img-4.jpeg](img-4.jpeg)

Figure 4. The comparison results of relative zero-one loss ratio.
![img-5.jpeg](img-5.jpeg)

Figure 5. The comparison results of relative bias/variance ratio.

With respect to variance, NB performs the best among these algorithms because its network structure is definite and is therefore insensitive to changes in the training set, as shown in Table 7. By contrast, KDB performs the worst. When $k$ increases, the resulting network tends to have a complex structure. Thus, the network has high variance because of the inaccurate probability estimation caused by the limited amount of training data. Meanwhile, for the local KDB, only the attribute values in the test instance are needed to compute the CLMI. The negative effect caused by probability distribution will be mitigated significantly. Moreover, FDs are extracted from the entire data set and entirely unrelated to the training set. From Figure 5, we observed that the local KDB expresses significant complementary characteristics. Moreover, in 9 of 11 data sets, AKDB performs better than KDB.

# 5. Conclusions 

We propose to build a local KDB as a complementary part of KDB to describe some specific situations to retain the high-dependence representation characteristic of KDB and aggregating mechanism of AODE. The final model, AKDB, has shown its superiority from the comparison results of zero-one loss, bias, and variance. The local KDB is trained in the framework of KDB. Similarly, applying the basic idea of the current work to other high-dependence Bayesian classifiers is possible.

## Acknowledgments

This work was supported by the National Science Foundation of China (Grant No. 61272209, 61300145) and the Postdoctoral Science Foundation of China (Grant No. 2013M530980), Agreement of Science \& Technology Development Project, Jilin Province (No. 20150101014JC).

## Author Contributions

All authors have contributed to the study and preparation of the article. The 1st author conceived the idea, derived equations and wrote the paper. The 2nd author and the 3rd author did the analysis. The 4th author finish the programming work. All authors have read and approved the final manuscript.

## Conflicts of Interest

The authors declare no conflict of interest.
