# Article 

## Discriminatory Target Learning: Mining Significant Dependence Relationships from Labeled and Unlabeled Data

Zhi-Yi Duan ${ }^{1}$ (D), Li-Min Wang ${ }^{1}$ (D), Musa Mammadov ${ }^{2}$, Hua Lou ${ }^{3}$ and Ming-Hui Sun ${ }^{4, *}$<br>1 Key Laboratory of Symbolic Computation and Knowledge Engineering of Ministry of Education, Jilin University, Changchun 130012, China; duanzy17@mails.jlu.edu.cn (Z.-Y.D.); wanglim@jlu.edu.cn (L.-M.W.)<br>2 Faculty of Science, Engineering \& Built Environment, Deakin University Geelong, Burwood, VIC 3125, Australia; musa.mammadov@deakin.edu.au<br>3 Changzhou College of Information Technology, Changzhou 213164, China; louhua@ccit.js.cn<br>4 College of Computer Science and Technology, Jilin University, Changchun 130012, China<br>* Correspondence: smh@jlu.edu.cn; Tel.: +86-0431-8515-9403

Received: 27 April 2019; Accepted: 24 May 2019; Published: 26 May 2019


#### Abstract

Machine learning techniques have shown superior predictive power, among which Bayesian network classifiers (BNCs) have remained of great interest due to its capacity to demonstrate complex dependence relationships. Most traditional BNCs tend to build only one model to fit training instances by analyzing independence between attributes using conditional mutual information. However, for different class labels, the conditional dependence relationships may be different rather than invariant when attributes take different values, which may result in classification bias. To address this issue, we propose a novel framework, called discriminatory target learning, which can be regarded as a tradeoff between probabilistic model learned from unlabeled instance at the uncertain end and that learned from labeled training data at the certain end. The final model can discriminately represent the dependence relationships hidden in unlabeled instance with respect to different possible class labels. Taking $k$-dependence Bayesian classifier as an example, experimental comparison on 42 publicly available datasets indicated that the final model achieved competitive classification performance compared to state-of-the-art learners such as Random forest and averaged one-dependence estimators.


Keywords: Bayesian network; discriminatory target learning; unlabeled instance

## 1. Introduction

With the rapid development of computer technologies, business and government organizations create large amounts of data, which need to be processed and analyzed. Over the past decade, to satisfy the urgent need of mining knowledge hidden in the data, numerous machine learning models [1,2] (e.g., decision tree [3], Bayesian network [4,5], support vector machine [6] and Neural network [7]) have been proposed.

To mine all "right" knowledge that exist in a database, researchers mainly proposed two kinds of learning strategies to address this issue. (1) Increase structure complexity to represent more dependence relationships, e.g., convolutional neural network [8] and $k$-dependence Bayesian classifier (KDB) [9]. However, as structure complexity grows overfitting will inevitably appear, which will result in redundant dependencies and performance degradation. Sometimes the overly complex structures hide the internal working mechanism and make them criticized for being used as "black box". (2) Build ensemble of several individual members having relatively simple network structure, e.g., Random forest [10] and averaged one-dependence estimators (AODE) [11]. Ensembles can generally perform

better than any individual member. However, it is difficult or even impossible to give a clear semantic explanation of the combined result since the working mechanisms of individual members may differ greatly. In practice, people would rather use models with simple and easy-to-explain structures, e.g., decision tree [12] and Naive Bayes (NB) [13,14,15], although they may perform poorer.

Bayesian networks (BNs) have long been a popular medium for graphically representing the probabilistic dependencies, which exist in a domain. Recently, work in Bayesian methods for classification has grown enormously. Numerous Bayesian network classifiers (BNCs) [9,16,17,18,19,20] have been proposed to mine the significant dependence relationships implicated in training data. With solid theoretic support, they have strong potential to be effective for practical application in a number of massive and complex data-intensive fields such as medicine [21], astronomy [22], biology [23], and so on. A central concern for BNC is to learn conditional dependence relationships encoded in the network structure. Some BNCs, e.g., KDB, use conditional mutual information $I\left(X_{i} ; X_{j} \mid Y\right)$ to measure the conditional dependence relationships between $X_{i}$ and $X_{j}$, which is defined as follows [24],

$$
\begin{aligned}
I\left(X_{i} ; X_{j} \mid Y\right) & =\sum_{x_{i}} \sum_{x_{j}} \sum_{y} P\left(x_{i}, x_{j}, y\right) \log \frac{P\left(x_{i}, x_{j} \mid y\right)}{P\left(x_{i} \mid y\right) P\left(x_{j} \mid y\right)} \\
& =\sum_{x_{i}} \sum_{x_{j}} \sum_{y} I\left(x_{i} ; x_{j} \mid y\right)
\end{aligned}
$$

For example, $I\left(X_{i} ; X_{j} \mid Y\right)=0$ indicates that attributes $X_{i}$ and $X_{j}$ are conditionally independent. However, in practice, for any specific event or data point, the situation will be much more complex. Taking Waveform dataset as an example, attributes $X_{15}$ and $X_{16}$ are conditionally dependent, since $I\left(X_{15} ; X_{16} \mid Y\right)>0$ always holds. Figure 1 shows the distributions of $I\left(x_{15} ; x_{16} \mid y_{i}\right)$, where $i \in\{1,2,3\}$. As can be seen, there exist some positive values of $I\left(x_{15} ; x_{16} \mid y_{1}\right)$ and $I\left(x_{15} ; x_{16} \mid y_{2}\right)$. However, for the class label $y_{3}$, the negative or zero values of $I\left(x_{15} ; x_{16} \mid y_{3}\right)$ have a high proportion among all values. That is, for different class labels, the conditional dependence relationships may be different rather than invariant when attributes take different values. We argue that most BNCs (e.g., NB and KDB), which build only one model to fit training instances, cannot capture this difference and cannot represent the dependence relationships flexibly, especially hidden in unlabeled instances.
![img-0.jpeg](img-0.jpeg)

Figure 1. The distributions of $I\left(x_{15} ; x_{16} \mid y_{i}\right)$ on Waveform dataset, where $i \in\{1,2,3\}$. The x -axis represents the index of each instance, the $y$-axis represents the value of $I\left(x_{15} ; x_{16} \mid y_{i}\right)$.

The scientific data can be massive, and labeled training data may account for only a small portion. In this paper, we propose a novel learning framework, called discriminatory target learning, for achieving better classification performance and high-level of dependence relationships while not increasing structure complexity. KDB is taken as an example to illustrate the basic idea and prove the feasibility of discriminatory target learning. By redefining mutual information and conditional mutual information, we build a "precise" model $\mathrm{kdb}_{i}$ for each unlabeled instance $\mathbf{x}$ with respect to class label $y_{i}$. The ensemble of $\mathrm{kdb}_{i}$, i.e., $\mathrm{kdb}^{e}$, can finely describe the dependency relationships hidden in $\mathbf{x}$. The final ensemble of $\mathrm{kdb}^{e}$ and regular KDB can fully and discriminately describe the dependence relationships in training data and unlabeled instance.

The rest of the paper is organized as follows: Section 2 introduces some state-of-the-art BNCs. Section 3 introduces the basic idea of discriminatory target learning. Experimental study on 42 UCI machine learning datasets is presented in Section 4, including a comparison with seven algorithms. The final section draws conclusions and outlines some directions for further research.

# 2. Bayesian Network Classifiers 

The structure of a BN on the random variables $\left\{X_{1}, \cdots, X_{n}\right\}$ is a directed acyclic graph (DAG), which represents each attribute in a given domain as a node in the graph and dependencies between these attributes as arcs connecting the respective nodes. Thus, independencies are represented by the lack of arcs connecting particular nodes. BNs are powerful tools for knowledge representation and inference under conditions of uncertainty. BNs were considered as classifiers only after the discovery of NB, a very simple kind of BN on the basis of conditional independence assumption. It is surprisingly effective and efficient for inference [5]. The success of NB has led to the research of Bayesian network classifiers (BNCs), including tree-augmented naive Bayes (TAN) [16], averaged one-dependence estimators (AODE) [18] and $k$-dependence Bayesian classifier (KDB) [9,17].

Let each instance $\mathbf{x}$ be characterized with $n$ values $\left\{x_{1}, \cdots, x_{n}\right\}$ for attributes $\left\{X_{1}, \cdots, X_{n}\right\}$, and class label $y \in\left\{y_{1}, \cdots, y_{m}\right\}$ is the value of class variable $Y$. NB assumes that the predictive attributes are conditional independent of each other given the class label, that is

$$
P\left(x_{1}, \cdots, x_{n} \mid y\right)=\prod_{i=1}^{n} P\left(x_{i} \mid y\right)
$$

Correspondingly for any value pair of arbitrary two attributes $X_{i}$ and $X_{j}, P\left(x_{i}, x_{j} \mid y\right)=$ $P\left(x_{i} \mid y\right) P\left(x_{j} \mid y\right)$ always holds. From Equation (1) there will be $I\left(X_{i} ; X_{j} \mid Y\right)=0$ and this can explain why there exist no arc between attributes for NB. However, in the real world, it will be much more complex when considering different specific event or data point. We now formalize our notion of the spectrum of point dependency relationship in Bayesian classification.

Definition 1. For unlabeled data point $\boldsymbol{x}=\left\{x_{1}, \cdots, x_{n}\right\}$, the conditional dependence between $X_{i}$ and $X_{j}(1 \leq$ $i, j \leq n$ ) with respect to label $y$ on point $\boldsymbol{x}$ is measured by pointwise $y$-conditional mutual information, which is defined as follows,

$$
\begin{aligned}
I\left(x_{i} ; x_{j} \mid y\right) & =P\left(x_{i}, x_{j}, y\right) \log \frac{P\left(x_{i}, x_{j} \mid y\right)}{P\left(x_{i} \mid y\right) P\left(x_{j} \mid y\right)} \\
& =P\left(x_{i}, x_{j}, y\right) \log \frac{P\left(x_{i} \mid x_{j}, y\right)}{P\left(x_{i} \mid y\right)}
\end{aligned}
$$

Equation (2) is a modified version of pointwise conditional mutual information that is applicable to labeled data point [25]. By comparing Equations (1) and (2), $I\left(X_{i} ; X_{j} \mid Y\right)$ is a summation of expected values of $I\left(x_{i} ; x_{j} \mid y\right)$ given all possible values of $X_{i}, X_{j}$ and $Y$. The traditional BNCs, e.g., TAN and KDB, use $I\left(X_{i} ; X_{j} \mid Y\right)$ to roughly measure the conditional dependence between $X_{i}$ and $X_{j} . I\left(X_{i} ; X_{j} \mid Y\right)$ is non-negative, $I\left(X_{i} ; X_{j} \mid Y\right)>0$ iff $X_{i}$ and $X_{j}$ are conditionally dependent given $Y$. However, only considering $I\left(X_{i} ; X_{j} \mid Y\right)=0$ as the criterion for identifying the conditional independent relationship

is too strict for BN learning, which may lead to classification bias, since $I\left(x_{i} ; x_{j} \mid y\right) \leq 0$ may hold for specific data point $\mathbf{x}$. That may be the main reason why NB performs better in some research domains. To address this issue, in this paper $I\left(x_{i} ; x_{j} \mid y\right)$ is applied to measure the extent to which $X_{i}$ and $X_{j}$ are relatively conditionally dependent when $P\left(x_{i} \mid x_{j}, y\right)>P\left(x_{i} \mid y\right)$ or relatively conditionally independent or irrelevant when $P\left(x_{i} \mid x_{j}, y\right)<P\left(x_{i} \mid y\right)$, respectively.

Definition 2. For unlabeled data point $\boldsymbol{x}=\left\{x_{1}, \cdots, x_{n}\right\}$ with respect to label $y$, if $I\left(x_{i} ; x_{j} \mid y\right)>0(1 \leq i, j \leq$ $n)$, then $X_{i}$ and $X_{j}$ are $y$-conditionally dependent on point $\boldsymbol{x}$; if $I\left(x_{i} ; x_{j} \mid y\right)=0$, then they are $y$-conditionally independent on point $\boldsymbol{x}$; and if $I\left(x_{i} ; x_{j} \mid y\right)<0$, then they are $y$-conditionally irrelevant on point $\boldsymbol{x}$.

TAN maintains the structure of NB and allows each attribute to have at most one parent. Then, the number of arcs encoded in TAN is $n-1$. During the constructing procedure of maximum weighted spanning tree, TAN sorts the arcs between arbitrary attributes $X_{i}$ and $X_{j}$ by comparing $I\left(X_{i} ; X_{j} \mid Y\right)$, and adds them in turn to the network structure if no cycle appears. KDB further relaxes NB's independence assumption and can represent arbitrary degree of dependence while capturing much of the computational efficiency of NB. KDB first sorts attributes by comparing mutual information $I\left(X_{i} ; Y\right)$, which is defined as follows [24],

$$
I\left(X_{i} ; Y\right)=\sum_{x_{i}} \sum_{y} P\left(x_{i}, y\right) \log \frac{P\left(x_{i}, y\right)}{P\left(x_{i}\right) P(y)}
$$

Suppose the attribute order is $\left\{X_{1}, \cdots, X_{n}\right\}$. By comparing $I\left(X_{i} ; X_{j} \mid Y\right), X_{i}$ select its parents, e.g., $X_{j}$, from attributes that ranks before it in the order. KDB requires that $X_{i}$ must have $\min (i-1, k)$ parents and there will exist $\min (i-1, k)$ arcs between $X_{i}$ and its parents. The number of arcs encoded in KDB is $n k-\frac{k^{2}}{2}-\frac{k}{2}$ and will grow as $k$ grows. Thus, KDB can represent more dependency relationships than TAN. For TAN or KDB, they do not evaluate the extent to which the conditional dependencies are weak enough and should be neglected. They simply specify the maximum number of parents that attribute $X_{i}$ can have before structure learning. Some arcs corresponding to weak conditional dependencies will inevitably be added to the network structure. The prior and joint probabilities in Equations (1) and (3) will be estimated from training data as follows:

$$
\left\{\begin{array}{l}
P(y)=\frac{1}{N} \operatorname{Count}(Y=y) \\
P\left(x_{j}\right)=\frac{1}{N} \operatorname{Count}\left(X_{j}=x_{j}\right) \\
P\left(x_{j}, y\right)=\frac{1}{N} \operatorname{Count}\left(X_{j}=x_{j}, Y=y\right) \\
P\left(x_{i}, x_{j}, y\right)=\frac{1}{N} \operatorname{Count}\left(X_{i}=x_{i}, X_{j}=x_{j}, Y=y\right)
\end{array}\right.
$$

where $N$ is the number of training instances. Then, $P\left(x_{j} \mid y\right)$ and $P\left(x_{i}, x_{j} \mid y\right)$ in Equations (1) and (3) can be computed as follows:

$$
\left\{\begin{array}{l}
P\left(x_{j} \mid y\right)=\frac{P\left(x_{j}, y\right)}{P(y)} \\
P\left(x_{i}, x_{j} \mid y\right)=\frac{P\left(x_{i}, x_{j}, y\right)}{P(y)}
\end{array}\right.
$$

Sahami [9] suggested that, if $k$ is large enough to capture all "right" conditional dependencies that exist in a database, then a classifier would be expected to achieve optimal Bayesian accuracy. However, as $k$ grows, KDB will encode more weak dependency relationships, which correspond to smaller value

of $I\left(X_{i} ; X_{j} \mid Y\right)$. That increases the risk of occurrence of negative values of $I\left(x_{i} ; x_{j} \mid y\right)$ and may introduce redundant dependencies, which will mitigate the positive effect from significant dependencies that correspond to positive values of $I\left(x_{i} ; x_{j} \mid y\right)$. On the other hand, conditional mutual information $I\left(X_{i} ; X_{j} \mid Y\right)$ cannot finely measure the conditional dependencies hidden in different data points. The $\operatorname{arc} X_{i} \rightarrow X_{j}$ in BNC learned from training data corresponds to positive value of $I\left(X_{i} ; X_{j} \mid Y\right)$ and represents strong conditional dependence between $X_{i}$ and $X_{j}$. However, for specific labeled instance $\mathbf{d}=\left\{x_{1}, \cdots, x_{n}, y_{1}\right\}, I\left(x_{i} ; x_{j} \mid y_{1}\right) \leq 0$ may hold. Then, $X_{i}$ and $X_{j}$ are $y_{1}$-conditionally independent or irrelevant on point $\mathbf{d}$ and the arc $X_{i} \rightarrow X_{j}$ should be removed. For unlabeled instance, the possible dependency relationships between nodes may differ greatly with respect to different class labels.

Thus, BNCs with highly complex network structure do not necessarily beat those with simple ones. The conditional dependencies hold for training data in general do not necessarily hold for each instance. BNCs should discriminate between conditionally dependent and irrelevant relationship for different data points. Besides, BNC should represent all possible spectrums of point dependency relationship that correspond to different class labels for dependence analysis.

# 3. Discriminatory Target Learning 

In probabilistic classification, Bayes optimal classification suggests that, if we can determine the conditional probability distribution $P(y \mid \mathbf{x})$ with true distribution available, where $y$ is one of the $m$ class labels and $\mathbf{x}$ is the $n$-dimensional data point $\mathbf{x}=\left\{x_{1}, x_{2}, \cdots, x_{n}\right\}$ that represents an observed instance, then we could achieve the theoretically optimal classification. $P(y \mid \mathbf{x})$ can be described in an unrestricted Bayesian network, as shown in Figure 2a. By applying arc reversal, Shachter [26] proposed to produce the equivalent dependence structure, as shown in Figure 2b. The problem is reduced to estimating the conditional probability $P(\mathbf{x} \mid y)$. Figure 2a,b represents two inference processes that run in the opposite directions. Figure 2a indicates the causality that runs from the state of $\left\{X_{1}, \cdots, X_{n}\right\}$ (the cause) to the state of $Y$ (the effect). In contrast, if the causality runs in the opposite direction as shown in Figure 2b and the state of $Y$ (the effect) is uncertain, the dependencies between predictive attributes (the causes) should be tuned to match with different states of $Y$. That is, the restricted BNC shown in Figure 2b presupposes the class label first and then the conditional dependencies between attributes can verify the presupposition.
![img-1.jpeg](img-1.jpeg)

Figure 2. Example of (a) unrestricted BNC, and (b) restricted BNC.
For different class labels or presuppositions, the conditional dependencies should be different. It is not reasonable that, no matter what the effect (class label) is, the relationships between causes (predictive attributes) remain the same. Consider an unlabeled instance $\mathbf{x}=\left\{x_{1}, \cdots, x_{n}\right\}$; if $I\left(x_{i} ; x_{j} \mid y\right)>0$, then the conditional dependence between $X_{i}$ and $X_{j}$ on data point $\mathbf{x}$ with respect to class label $y$ is reasonable, otherwise it should be neglected. Since the class label for $\mathbf{x}$ is uncertain and there are $m$ labels available, we take $\mathbf{x}$ as the target and learn an ensemble of $m$ micro BNCs, i.e., $\mathrm{bnc}^{e}=\left\{\mathrm{bnc}_{1}, \cdots, \mathrm{bnc}_{m}\right\}$, each of them fully describes the conditional dependencies between attribute

values in $\mathbf{x}$ with respect to different class labels. The linear combiner is used for models that output real-valued numbers, thus is applicable for $\mathrm{bnc}^{e}$. The ensemble probability estimate for $\mathrm{bnc}^{e}$ is,

$$
\hat{P}\left(y_{i} \mid \mathbf{x}, \mathrm{bnc}^{e}\right)=\frac{P\left(y_{i}, \mathbf{x} \mid \mathrm{bnc}_{i}\right)}{\sum_{i=1}^{m} P\left(y_{i}, \mathbf{x} \mid \mathrm{bnc}_{i}\right)}
$$

$\mathrm{bnc}^{e}$ may overfit the unlabeled instance and underfit training data. In contrast, regular BNC learned from training data may underfit the unlabeled instance. Thus, they are complementary in nature. After training $\mathrm{bnc}^{e}$ and regular BNC, the final ensemble that estimates the class membership probabilities by averaging both predictions will be generated. The framework of discriminatory target learning is shown in Figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 3. The framework of discriminatory target learning.
Because in practice it is hardly possible to find the true distribution of $P(\mathbf{x} \mid y)$ from data, KDB approximates the estimation of $P(\mathbf{x} \mid y)$ by allowing for the modeling of arbitrarily complex dependencies between attributes. The pseudocode of KDB is shown in Algorithm 1.

```
Algorithm 1 Structure learning of KDB.
    Input: Training set \(\mathcal{T}\), parameter \(k\), vector \(I\left(X_{i} ; Y\right)(1 \leq i \leq n)\) and crosstab
        \(I\left(X_{i}, X_{j} \mid Y\right)(1 \leq i \neq j \leq n)\).
    Output: KDB, network structure.
    Let \(\mathcal{X}\) be a list of all \(X_{i}\) in descending order of \(I\left(X_{i} ; Y\right)\).
    \(\mathcal{V}=\{Y\} ; \mathcal{E}=\varnothing\);
    for \(i=1 \rightarrow n\) do
        \(\mathcal{V}=\mathcal{V} \cup \mathcal{X}[i] ;\)
        \(\mathcal{E}=\mathcal{E} \cup(Y \rightarrow \mathcal{X}[i])\);
    end
    for \(i=1 \rightarrow n\) do
        \(\hat{k}=k\);
        while ( \(\hat{k}>0\) ) do
            \(m=\arg \max _{j}\left\{I\left(\mathcal{X}[i] ; \mathcal{X}[j] \mid Y\right)\right\}(1 \leq j<i)\);
            \(\mathcal{E}=\mathcal{E} \cup\left(\mathcal{X}[j] \rightarrow \mathcal{X}[i]\right)\);
            \(\hat{k}=\hat{k}-1 ;\)
        end
    end
    \(\operatorname{return} \mathrm{KDB}\)
```

From the definition of $I\left(X_{i} ; Y\right)$ in Equation (3), we can have

$$
\begin{aligned}
I\left(X_{i} ; Y\right) & =\sum_{y} \sum_{x_{i}} P\left(x_{i}, y\right) \log \frac{P\left(x_{i}, y\right)}{P\left(x_{i}\right) P(y)} \\
& =\sum_{y} \sum_{x_{i}} P\left(x_{i}, y\right) \log \frac{P\left(y \mid x_{i}\right)}{P(y)}
\end{aligned}
$$

Definition 3. For unlabeled data point $\boldsymbol{x}=\left\{x_{1}, \cdots, x_{n}\right\}$, the dependence between $x_{i}(1 \leq i \leq n)$ and any given label $y$ is measured by pointwise $y$-mutual information, which is defined as follows,

$$
I\left(x_{i} ; y\right)=P\left(x_{i}, y\right) \log \frac{P\left(x_{i}, y\right)}{P\left(x_{i}\right) P(y)}=P\left(x_{i}, y\right) \log \frac{P\left(y \mid x_{i}\right)}{P(y)}
$$

Equation (8) is a modified version of pointwise mutual information that is applicable to labeled data point [25]. The prior and joint probabilities in Equations (2) and (8) will be estimated as follows

$$
\left\{\begin{array}{l}
\hat{P}(y)=\frac{1}{N+1}\left[\operatorname{Count}(Y=y)+\frac{1}{m}\right] \\
\hat{P}\left(x_{j}\right)=\frac{1}{N+1}\left[\operatorname{Count}\left(X_{j}=x_{j}\right)+\frac{1}{m}\right] \\
\hat{P}\left(x_{j}, y\right)=\frac{1}{N+1}\left[\operatorname{Count}\left(X_{j}=x_{j}, Y=y\right)+\frac{1}{m}\right] \\
\hat{P}\left(x_{i}, x_{j}, y\right)=\frac{1}{N+1}\left[\operatorname{Count}\left(X_{i}=x_{i}, X_{j}=x_{j}, Y=y\right)+\frac{1}{m}\right]
\end{array}\right.
$$

Conditional probabilities in Equations (2) and (8) can be estimated by:

$$
\left\{\begin{array}{l}
\hat{P}\left(x_{j} \mid y\right)=\frac{\hat{P}\left(x_{j}, y\right)}{\hat{P}(y)} \\
\hat{P}\left(x_{i}, x_{j} \mid y\right)=\frac{\hat{P}\left(x_{i}, x_{j}, y\right)}{\hat{P}(y)} \\
\hat{P}\left(y \mid x_{i}\right)=\frac{\hat{P}\left(x_{i}, y\right)}{\hat{P}\left(x_{i}\right)}
\end{array}\right.
$$

Similar to the Laplace correction [27], the main idea behind Equation (9) is equivalent to creating a "pseudo" training set $\mathcal{P}$ by adding to the training data a new instance $\left\{x_{1}, \cdots, x_{n}\right\}$ with multi-label by assuming that the probability that this new instance is in class $y$ is $1 / m$ for each $y \in\left\{y_{1}, \cdots, y_{m}\right\}$.

Definition 4. For unlabeled data point $\boldsymbol{x}=\left\{x_{1}, \cdots, x_{n}\right\}$ with respect to label $y$, if $I\left(x_{i} ; y\right)>0(1 \leq i \leq n)$, then $X_{i}$ is $y$-dependent on point $\boldsymbol{x}$; if $I\left(x_{i} ; y\right)=0$, then $X_{i}$ is $y$-independent on point $\boldsymbol{x}$; and if $I\left(x_{i} ; y\right)<0$, then $X_{i}$ is $y$-irrelevant on point $\boldsymbol{x}$.

KDB uses $I\left(X_{i} ; Y\right)$ to sort the attributes and $I\left(X_{i} ; X_{j} \mid Y\right)$ to measure the conditional dependence. Similarly, for unlabeled instance $\mathbf{x}=\left\{x_{1}, \cdots, x_{n}\right\}$, the corresponding micro KDB with respect to class label $y_{t}$, called $\mathrm{kdb}_{t}$, uses $I\left(x_{i} ; y_{t}\right)$ (see Equation (8)) to sort the attribute values and $I\left(x_{i} ; x_{j} \mid y_{t}\right)$ (see Equation (2)) to measure the conditional dependence. The learning procedure of $\mathrm{kdb}_{t}$ is shown in Algorithm 2.

```
Algorithm 2 Structure learning of \(\mathrm{kdb}_{t}\) with respect to class label \(y_{t}\).
    Input: Unlabeled instance \(t\), parameter \(k\), class label \(y_{t}\), vector \(I\left(x_{i} ; y_{t}\right)(1 \leq i \leq n)\) and
        \(\operatorname{crosstab} I\left(x_{i}, x_{j} \mid y_{t}\right)(1 \leq i \neq j \leq n)\).
    Output: \(\mathrm{kdb}_{t}\), network structure.
    Let \(\mathcal{X}\) be a list of all \(x_{i}\) in descending order of \(I\left(x_{i} ; y_{t}\right)\).
    \(\mathcal{V}=\{Y\} ; \mathcal{E}=\varnothing\);
    for \(i=1 \rightarrow n\) do
        \(\mathcal{V}=\mathcal{V} \cup \mathcal{X}[i] ;\)
        \(\mathcal{E}=\mathcal{E} \cup(Y \rightarrow \mathcal{X}[i])\);
    end
    for \(i=1 \rightarrow n\) do
        \(\hat{k}=k\);
        while \((\hat{k}>0)\) do
            \(m=\arg \max _{j}\left\{I\left(\mathcal{X}[i] ; \mathcal{X}[j] \mid y_{t}\right)\right\}(1 \leq j<i) ;\)
            if \((m>0)\) then
                \(\mathcal{E}=\mathcal{E} \cup\left(\mathcal{X}[j] \rightarrow \mathcal{X}[i]\right) ;\)
                \(\hat{k}=\hat{k}-1\);
            end
        end
    end
    end
return \(\mathrm{kdb}_{t}\)
```

Breiman [28] revealed that ensemble learning brings improvement in accuracy only to those "unstable" learning algorithms, in the sense that small variations in the training set would lead them to produce very different models. bnc ${ }^{e}$ is obviously an example of such learners. For individual members of $\mathrm{kdb}^{e}$, the difference in network structure is the result of change of $I\left(x_{i} ; y\right)$ or $I\left(x_{i} ; x_{j} \mid y\right)(1 \leq i \neq j \leq$ $n$ ), or, more precisely, the conditional probability defined in Equations (2) and (8). Given unlabeled instance $\mathbf{x}=\left\{x_{1}, \cdots, x_{n}\right\}$ and binary class labels $y_{1}$ and $y_{2}$, if $I\left(x_{i} ; y_{1}\right)>0$, i.e., $P\left(y_{1} \mid x_{i}\right)>P\left(y_{1}\right)$, then $X_{i}$ is $y_{1}$-dependent on $\mathbf{x}$. Because $P\left(y_{2}\right)=1-P\left(y_{1}\right)$ and $P\left(y_{2} \mid x_{i}\right)=1-P\left(y_{1} \mid x_{i}\right)$, we have

$$
\begin{aligned}
P\left(y_{1} \mid x_{i}\right)>P\left(y_{1}\right) & \Rightarrow 1-P\left(y_{1} \mid x_{i}\right)<1-P\left(y_{1}\right) \\
& \Rightarrow P\left(y_{2} \mid x_{i}\right)<P\left(y_{2}\right)
\end{aligned}
$$

and

$$
I\left(x_{i} ; y_{2}\right)=P\left(x_{i}, y_{2}\right) \log \frac{P\left(y_{2} \mid x_{i}\right)}{P\left(y_{2}\right)}<0
$$

Thus, $X_{i}$ is $y_{2}$-irrelevant on $\mathbf{x} . X_{i}$ plays totally different roles in the relationships with different class labels on the same instance. Supposing that before small variations in the training set $I\left(x_{i} ; y_{1}\right)>0$ and after that $I\left(x_{i} ; y_{1}\right)<0$, the attribute values will be resorted and correspondingly the network structures of $\mathrm{kdb}_{1}$ and $\mathrm{kdb}_{2}$ for $\mathbf{x}$ will change greatly. The sensitivity to the variation makes $\mathrm{kdb}^{e}$ finely describe the dependencies hidden in $\mathbf{x}$. Figure 4 shows examples of $\mathrm{kdb}_{1}$ and $\mathrm{kdb}_{2}$ corresponding to class labels $y_{1}$ and $y_{2}$, respectively. If the decision of the final ensemble is $y_{1}$, then we will use Figure 4a for dependence analysis. Otherwise, we will use Figure 4b instead. The attribute values annotated in black correspond to positive values of $I\left(x_{i} ; y_{t}\right)(t=1$ or 2$)$ and they should be focused on.

KDB requires training time complexity of $\mathcal{O}\left(n^{2} N m v^{2}\right)$ (dominated by the calculations of $\left.I\left(X_{i} ; X_{j} \mid Y\right)\right)$ and classification time complexity of $\mathcal{O}\left(n^{2} N m\right)$ [9] for classifying a single unlabeled instance, where $n$ is the number of attributes, $N$ is the number of data instances, $m$ is the number of class labels, and $v$ is the maximum number of discrete values that an attribute may take. Discriminatory target learning requires no additional training time, thus the training time complexity of final ensemble

is the same as that of regular KDB. At classification time it requires $\mathcal{O}\left(n^{2} N m\right)$ to calculate $I\left(x_{i} ; x_{j} \mid y\right)$, and the same time complexity for classifying a single unlabeled instance.
![img-3.jpeg](img-3.jpeg)

Figure 4. Example of (a) $\mathrm{kdb}_{1}$, and (b) $\mathrm{kdb}_{2}$.

# 4. Experiments and Results 

We compared the performance of our proposed methods $\mathrm{kdb}^{e}$ and $\mathrm{KDB}^{e}$ with several state-of-the-art classifiers. We analyzed the performance in terms of zero-one loss, root mean square error (RMSE), bias and variance on 42 natural domains from the UCI Machine Learning Repository [29]. These datasets are described in Table 1, in ascending order of number of instances. The structure of this section is as follows: we discuss our experimental methodology and evaluation function in details in Section 4.1. Section 4.2 includes comparisons with three classic single-structure BNCs, namely NB, TAN and KDB, as well as one ensemble BNC: AODE. Then, in Section 4.3, $\mathrm{KDB}^{e}$ is compared with Random Forest with 100 decision trees. Section 4.4 presents a global comparison of all learners considered by applying the Friedman and Nemenyi tests.

Table 1. Datasets. Imbalanced datasets are annotated with the symbol "*".


### 4.1. Experimental Methodology and Evaluation Function

The experiments for all BNCs used C++ software (NetBeans 8.0.2) specially designed to deal with classification problems. Each algorithm was tested on each dataset using 10-fold cross validation.

All experiments were conducted on a desktop computer with an Intel(R) Core(TM) i3-6100 CPU @ $3.70 \mathrm{GHz}, 64$ bits and 4096 MB of memory(Dell Vostro 2667, Changchun, China).

- Win/Draw/Lose (W/D/L) Record: When two algorithms were compared, we counted the number of datasets for which one algorithm performed better, equally well or worse than the other on a given measure. We considered there exists a significant difference if the output of a one-tailed binomial sign test was less than 0.05 .
- Missing Values: Missing values for qualitative attributes were replaced with modes, and those for quantitative attributes were replaced with means from the training data.
- Numeric Attributes: For each dataset, we used MDL (Minimum Description Length) discretization [30] to discretize numeric attributes.
- Dataset Sizes: Datasets were categorized in terms of their sizes. That is, datasets with instances $<1000, \geq 1000$ and $<10,000, \geq 10,000$ were denoted as small size, medium size and large size, respectively. We report results on these sets to discuss suitability of a classifier for datasets of different sizes.
- Zero-one loss: Zero-one loss can be used to measure the extent to which a learner correctly identifies the class label of an unlabeled instance. Supposing $y$ and $\hat{y}$ are the true class label and that generated by a learning algorithm, respectively, given $M$ unlabeled test instances, the zero-one loss function is defined as

$$
\xi(y, \hat{y})=\frac{\sum_{i=1}^{M} 1-\varrho\left(y_{i}, \hat{y}_{i}\right)}{M}
$$

where $\varrho\left(y_{i}, \hat{y}_{i}\right)=1$ if $y_{i}=\hat{y}_{i}$ and 0 otherwise.

- Bias and variance: The bias-variance decomposition proposed by Kohavi and Wolpert [31] provides valuable insights into the components of the zero-one loss of learned classifiers. Bias measures how closely the classifier can describe the decision boundary, which is defined as

$$
\text { bias }=\frac{1}{2} \sum_{\hat{y}, y \in Y}[P(\hat{y} \mid \mathbf{x})-P(y \mid \mathbf{x})]^{2}
$$

where $\mathbf{x}$ is the combination of any attribute value. Variance measures the sensitivity of the classifier to variations in the training data, which is defined as

$$
\text { variance }=\frac{1}{2}\left[1-\sum_{\hat{y} \in Y} P(\hat{y} \mid \mathbf{x})^{2}\right]
$$

- RMSE: For each instance, RMSE accumulates the squared error, where the error is the difference between 1.0 and the probability estimated by the classifier for the true class for the instance, and then computes the squared root of the mean of the sum, which is defined as

$$
R M S E=\sqrt{\frac{1}{s} \sum_{i=1}^{s}(1-P(\hat{y} \mid \mathbf{x}))^{2}}
$$

where $s$ is the sum of training instances.

# 4.2. $K D B^{e}$ Versus Classic BNCs 

We compared $\mathrm{KDB}^{e}$ with several classic BNCs, namely NB, TAN, KDB and AODE. Sahami [9] proposed the notion of $k$-dependence BNC, which allows each attribute $X_{i}$ to have a maximum of $k$ attributes as parents. NB and TAN are, respectively, 0 -dependence and 1 -dependence BNCs. To clarify the effect of dependence complexity, we set $k=2$ for both KDB and $\mathrm{KDB}^{e}$.

# 4.2.1. Zero-One Loss and RMSE Results 

The detailed results in terms of zero-one loss and RMSE are shown in Tables A1 and A2 in Appendix A, respectively. Tables 2 and 3 show W/D/L records summarizing the relative zero-one loss and RMSE of different BNCs. When $k=2$, NB, TAN and KDB can, respectively, represent 0 , $n-1$ and $2 n-3$ conditional dependencies, where $n$ is the number of predictive attributes. As shown in Table 1, since $n>3$ holds for all datasets, $2 n-3>n-1$ also holds. Thus, KDB can represent the largest number of dependencies among all. With respect to zero-one loss, NB represents no conditional dependencies due to its independence assumption and performed the worst in general. As the dependence degree or structure complexity increased, KDB was competitive compared to NB and TAN. AODE performed better than the other single-structure BNCs due to its ensemble mechanism. Surprisingly, $\mathrm{kdb}^{e}$ had significantly better zero-one loss performance than NB, TAN and KDB. When discriminatory target learning was introduced for discovery of dependencies that exist in different unlabeled instances, the final ensemble $\mathrm{KDB}^{e}$ could possess significant advantage over other classifiers. For example, $\mathrm{KDB}^{e}$ beat KDB in 26 domains and lost only in three in terms of zero-one loss. RMSE-wise, $\mathrm{KDB}^{e}$ still performed the best. For instance, $\mathrm{KDB}^{e}$ enjoyed a significant advantage over TAN (20/19/3). When compared to $\mathrm{KDB}, \mathrm{KDB}^{e}$ also achieved superior performance, with 17 wins and 5 losses.

Table 2. W/D/L comparison results of zero-one loss on all datasets.


Table 3. W/D/L comparison results of RMSE on all datasets.


To make the experimental results more intuitive, from the viewpoints of the ensemble mechanism and structure complexity, Figure 5a,c shows the comparisons of $\mathrm{KDB}^{e}, \mathrm{KDB}$ and AODE in terms of zero-one loss, whereas Figure 5b,d shows the comparisons for RMSE. The red squared symbols are used to indicate significant advantages of $\mathrm{KDB}^{e}$ over the other BNCs. In Figure 5a,b, only two points are far above the diagonal line, thus the negative effect caused by discriminatory target learning was negligible. In contrast, many more points are below the diagonal line, which means that discriminatory target learning worked effectively in most cases. A notable case is Waveform dataset, where discriminatory target learning helped to substantially reduce classification error, such as the reduction from 0.0256 to 0.0193 for zero-one loss and from 0.1145 to 0.0901 for RMSE. When comparing $\mathrm{KDB}^{e}$ with AODE, it can be seen in Figure 5c,d that there are still many points below the diagonal line, which means that $\mathrm{KDB}^{e}$ enjoyed a significant advantage over AODE. For example, a notable case is our largest dataset Localization, where the zero-one loss of $\mathrm{KDB}^{e}(0.2743)$ was much lower than that of AODE (0.3596).

![img-4.jpeg](img-4.jpeg)

Figure 5. Scatter plot of zero-one loss and RMSE comparisons for KDB<sup>r</sup>, KDB and AODE.

### 4.2.2. Bias and Variance Results

The detailed results in terms of bias and variance are shown in Tables A3 and A4 in Appendix A, respectively. The W/D/L records with respect to bias and variance results are shown in Tables 4 and 5, respectively. We can observe in Table 4 that ensemble classifiers, i.e., AODE and kdb<sup>r</sup>, performed better than TAN but worse than KDB, although these results were not always statistically significant. NB still performed the worst. High-dependence structure or ensemble construction strategy could help reduce the bias. Jointly applying both helped KDB<sup>r</sup> reduce bias significantly. For example, KDB<sup>r</sup> performed better than TAN (26/9/7) and KDB (11/27/4).

In terms of variance, since the network structures of NB and AODE are definite and irrelevant to the variation of the training data, the independence assumption helped reduce the variance significantly. KDB was the most sensitive to the variation in training data among all classifiers. As discussed in Section 3, discriminatory target learning made kdb<sup>r</sup> underfit training data and overfit the unlabeled instance. When kdb<sup>r</sup> was integrated with regular KDB, discriminatory target learning helped to reduce the variance and the final ensemble classifier, i.e., KDB<sup>r</sup>, performed the best only after NB and AODE.

Table 4. W/D/L comparison results of bias on all datasets.


Table 5. W/D/L comparison results of variance on all datasets.


# 4.2.3. Time Comparison 

We compared KDB $^{\text {e }}$ with the other classic BNCs in terms of training and classification time. Since kdb $^{\text {e }}$ is a part of $\mathrm{KDB}^{\mathrm{e}}$, we removed it in this experiment. Figure 6a,b shows the training and classification time comparisons for all BNCs. Each bar represents the sum of time on 42 datasets in a 10 -fold cross-validation experiment. No parallelization techniques were used in any case. As discussed in Section 3, discriminatory target learning requires no additional training time, thus the training time complexity of $\mathrm{KDB}^{\mathrm{e}}$ was the same as that of regular KDB. Due to the structure complexity, $\mathrm{KDB}^{\mathrm{e}}$ and KDB required a bit more time for training than the other BNCs. With respect to classification time, $\mathrm{KDB}^{\mathrm{e}}$ took a little more time than the other BNCs. The reason lies in that $\mathrm{KDB}^{\mathrm{e}}$ learned $\mathrm{kdb}^{\mathrm{e}}$ for each unlabeled test instance, while the other BNCs only needed to directly calculate the joint probabilities. In general, discriminatory target learning helped to significantly improve the classification performance of its base classifier at the cost of a small increase in time consumption, which is perfectly acceptable.
![img-5.jpeg](img-5.jpeg)

Figure 6. Training and classification time comparisons for BNCs.

### 4.3. KDB $^{\text {e }}$ Versus Random Forest

To further illustrate the performance of our proposed discriminatory target learning framework, we compared $\mathrm{KDB}^{\mathrm{e}}$ with a powerful learner, i.e., Random forest.Random forest (RF) is a combination of decision tree predictors, where each tree is trained on data selected at random but with replacement from the original data [10]. As the number of trees in the forest becomes large, the classification

error for forests tends to converge to a limit. RF is an effective tool in prediction. RF can process high-dimensional data (that is, data with a lot of features) without making feature selection. Furthermore, due to the random mechanism, RF has the capacity to deal with imbalanced datasets or data with numerous missing values. Moreover, the framework in terms of strength of the individual predictors and their correlations gives insight into the ability of the RF to predict [10]. Because of its high classification accuracy, RF has been applied to many scientific fields, e.g., ecology and agriculture [32]. In our experiment, RF with 100 decision trees was used. The detailed results of RF in terms of zero-one loss, RMSE, bias and variance can be found in Tables A1-A4 in Appendix A, respectively. Table 6 shows the W/D/L records with different dataset sizes. When zero-one loss was compared, $\mathrm{KDB}^{e}$ won more frequently than RF, especially on small and medium datasets. The results indicate $10 / 4 / 3$ on small datasets and $7 / 4 / 4$ on medium datasets. The reason may lie in that 100 decision trees are complex and tend to overfit the training data. RMSE-wise, $\mathrm{KDB}^{e}$ also performed better than RF, which is shown as 16 wins and 11 losses. Bias and variance comparison of $\mathrm{KDB}^{e}$ and RF (Table 6) suggested that $\mathrm{KDB}^{e}$ is a low variance and high bias classifier. One can expect it to work extremely well on small and medium datasets. This is evident in Table 6 showing the zero-one loss and RMSE comparisons. $\mathrm{KDB}^{e}$ beat RF on 26 datasets and lost on 12 datasets with respect to variance. Thus, the advantages of $\mathrm{KDB}^{e}$ over RF in terms of zero-one loss and RMSE could be attributed to the change in variance. Since the variance term increased as the algorithm became more sensitive to the change in labeled training data, obviously, discriminatory target learning helped to alleviate the negative effect caused by overfitting.

Table 6. W/D/L records between $\mathrm{KDB}^{e}$ and RF.


Besides, we display the time comparisons between $\mathrm{KDB}^{e}$ and RF in Figure 7. It is obvious that $\mathrm{KDB}^{e}$ enjoyed a great advantage over RF in terms of training time on datasets of all sizes. This advantage could be attributed to that $\mathrm{KDB}^{e}$ only learned a regular KDB for every dataset during the training phase while RF needed to train 100 decision trees. When comparing classification time, the performance of $\mathrm{KDB}^{e}$ and RF showed a slight reversal. Learning $\mathrm{kdb}^{e}$ for each unlabeled test instance made $\mathrm{KDB}^{e}$ take a bit more time than RF. However, when comparing on small and medium datasets, the advantage of RF over $\mathrm{KDB}^{e}$ was not significant. To conclude, on small and medium datasets, $\mathrm{KDB}^{e}$ had a significantly better zero-one loss performance and better RMSE than RF. This was packaged with $\mathrm{KDB}^{e}$ 's far superior training times and competitive classification times over RF, which makes $\mathrm{KDB}^{e}$ an excellent alternative to RF, especially for dealing with small and medium datasets.

![img-6.jpeg](img-6.jpeg)

Figure 7. Training and classification time comparisons between KDB*$^{e}$ and RF.

# 4.3.1. Discussion 

RF has been applied to several scientific fields and associated research areas [32], because of its high classification accuracy. However, RF is more negatively affected in terms of computation consumption (memory and time) by dataset sizes than BNCs [19]. Furthermore, due to the random mechanism, RF is sometimes criticized for difficulty giving a clear semantic explanation of the combined result that is outputted by numerous decision trees. In contrast, our proposed discriminatory target learning framework considers not only the dependence relationships that exist in the training data, but also that hidden in unlabeled test instances, which makes the final model highly interpretable. $\mathrm{KDB}^{e}$ outperformed RF in terms of zero-one loss, RMSE and variance, especially on small and medium size datasets, while RF beat $\mathrm{KDB}^{e}$ in terms of bias. Moreover, RF required substantially more time for training and $\mathrm{KDB}^{e}$ took a bit more time for classifying.

To illustrate the better interpretability of $\mathrm{KDB}^{e}$ than that of RF, we took medical diagnostic application as an example. The Heart-disease-c dataset (http://archive.ics.uci.edu/ml/datasets/ Heart+Disease) from UCI Machine Learning Repository was collected from Cleveland Clinic Foundation, containing 13 attributes and two class labels. The detailed description of this dataset is shown in Table 7. The zero-one loss results of KDB, RF and $\mathrm{KDB}^{e}$ are $0.2244,0.2212$ and 0.2079 , respectively. KDB learned from training data can describe the general conditional dependencies, while for a certain instance some of dependence relationships may hold instead of all the dependencies shown in KDB. In contrast, $\mathrm{kdb}^{e}$ can encode the most possible local conditional dependencies hidden in one single test instance. We argue that an ideal phenomenon is that KDB and $\mathrm{kdb}^{e}$ are complementary to each other for classification and they may focus on different key points. To prove this, randomly taking an instance from Heart-disease-c dataset as an example, the detail of this instance is shown as, $\mathcal{T}=\left\{x_{0}=57, x_{1}=1, x_{2}=3, x_{3}=150, x_{4}=168, x_{5}=0, x_{6}=0, x_{7}=174, x_{8}=0, x_{9}=\right.$ $\left.1.6, x_{10}=3, x_{11}=0, x_{12}=3\right\}$. Figures 8 and 9 show the structural difference between KDB and the submodels of $\mathrm{kdb}^{e}$. For KDB, by comparing mutual information $I(X ; Y),\left\{X_{6}, X_{1}, X_{12}\right\}$ are the first three key attributes for this dataset. There are 23 arcs in the structure of KDB which represent the conditional dependencies between predictive attributes. However, the values of $I\left(X_{8} ; X_{1} \mid Y\right)$, $I\left(X_{8} ; X_{6} \mid Y\right), I\left(X_{9} ; X_{1} \mid Y\right)$ and $I\left(X_{9} ; X_{6} \mid Y\right)$ are all 0 . For the instance $\mathcal{T}$, in Figure 9, we can easily find that the structure of $\mathrm{kdb}^{e}$ differed greatly from that of KDB. The true class label for $\mathcal{T}$ is $y_{1}$. KDB misclassified $\mathcal{T}$, while $\mathrm{KDB}^{e}$ correctly classified the instance. Thus, we can use Figure 9a for dependence analysis. By comparing the pointwise $y_{1}$-mutual information, $\left\{x_{12}, x_{11}, x_{7}\right\}$ are the first three key attribute values for $\mathcal{T}$. It is worth mentioning that $X_{1}$ ranked second in KDB, whereas $x_{1}$ ranked last in $\mathrm{kdb}_{y_{1}}$. Furthermore, there were only 15 arcs in $\mathrm{kdb}_{y_{1}}$, which means that some redundant dependencies were eliminated. In general, $\mathrm{KDB}^{e}$ could utilize the knowledge learned from

Table 7. Description of Heart-disease-c dataset.


![img-7.jpeg](img-7.jpeg)

Figure 8. The structure of KDB on Heart-disease-c dataset.
![img-8.jpeg](img-8.jpeg)

Figure 9. The structure of submodels of $\mathrm{kdb}^{e}$.

# 4.3.2. Imbalanced Datasets 

There are 15 imbalanced datasets in our experiments, which are annotated with the symbol "*" in Table 1. To prove that $\mathrm{KDB}^{e}$ has the capacity to deal with imbalanced datasets, we conducted a set of experiments to compare the performance of $\mathrm{KDB}^{e}$ with RF in terms of extended Matthews correlation coefficient (MCC). The MCC provides a balanced measure for skewed datasets by taking into account

the class distribution [33]. The classification results can be shown in the form of a confusion matrix as follows:

$$
\left[\begin{array}{ccc}
N_{11} & \cdots & N_{1 m} \\
\vdots & \ddots & \vdots \\
N_{m 1} & \cdots & N_{m m}
\end{array}\right]
$$

Each entry $N_{i i}$ of the matrix gives the number of instances, whose true class was $Y_{i}$ that were actually assigned to $Y_{i}$, where $1 \leq i \leq m$. Each entry $N_{i j}$ of the matrix gives the number of instances, whose true class was $Y_{i}$ that were actually assigned to $Y_{j}$, where $i \neq j$ and $1 \leq i, j \leq m$. Given the confusion matrix, the extended MCC can be calculated as follow,

$$
M C C=\frac{\sum_{m i j} N_{i j} N_{j m}-N_{i j} N_{m i}}{\sqrt{\sum_{i}\left(\sum_{j} N_{i j}\right)\left(\sum_{j^{\prime}, i^{\prime} \neq i} N_{i^{\prime} j^{\prime}}\right)} \sqrt{\sum_{i}\left(\sum_{j} N_{j i}\right)\left(\sum_{j^{\prime}, i^{\prime} \neq i} N_{j^{\prime} i^{\prime}}\right)}}
$$

Note that the MCC reaches its best value at 1, which represents a perfect prediction, and worst value at -1 , which indicates a total disagreement between the predicted and observed classifications. Figure 10 shows the scatter plot of $\mathrm{KDB}^{c}$ and RF in terms of MCC. We can see that many points fall close to the diagonal line, which means that $\mathrm{KDB}^{c}$ achieved competitive results compared with RF. Furthermore, there are three points far above the diagonal line, which means $\mathrm{KDB}^{c}$ enjoys significant advantages on these datasets. A notable case is Dis dataset annotated with red color, where the MCC of $\mathrm{KDB}^{c}(0.4714)$ was much higher than that of $\operatorname{RF}(0.3710)$. In general, $\mathrm{KDB}^{c}$ had the capacity to handle the imbalanced datasets.
![img-9.jpeg](img-9.jpeg)

Figure 10. The scatter plot of $\mathrm{KDB}^{c}$ and RF in terms of MCC. Dis dataset is annotated with red color, which is a notable case where $\mathrm{KDB}^{c}$ enjoys significant advantages.

# 4.4. Global Comparison of All Classifiers 

In this section, to assess whether the overall differences in performance of these learners was statistically significant, we employed the Friedman test [34] and the post-hoc Nemenyi test, as recommended by Demšar [35]. The Friedman test is a non-parametric test for multiple hypotheses testing. It ranks the algorithms for each dataset separately: the best performing algorithm getting the rank of 1 , the second best ranking 2 , and so on. In case of ties, average ranks are assigned. The

null-hypothesis is that all of the algorithms perform almost equivalently and there is no significant difference in terms of average ranks. The Friedman statistic can be computed as follows:

$$
\chi_{F}^{2}=\frac{12}{N t(t+1)} \sum_{j=1}^{t} R_{j}^{2}-3 N(t+1)
$$

where $R_{j}=\sum_{i} r_{i}^{j}$ and $r_{i}^{j}$ is the rank of the $j$ th of $t$ algorithms on the $i$ th of $N$ datasets. The Friedman statistic is distributed according to $\chi_{F}^{2}$ with $t-1$ degrees of freedom. Thus, for any pre-determined level of significance $\alpha$, the null hypothesis will be rejected if $\chi_{F}^{2}>\chi_{\alpha}^{2}$. The critical value of $\chi_{\alpha}^{2}$ for $\alpha=0.05$ with six degrees of freedom is 12.592 . The Friedman statistics of zero-one loss and RMSE were 53.65 and 60.49, which were both larger than 12.592. Hence, the null-hypotheses was rejected. According to the detailed results of rank shown in Tables A5 and A6 in Appendix A, Figure 11 plots the average ranks across all datasets, along with the standard deviation for each learner. When assessing the calibration of the probability estimates using zero-one loss, $\mathrm{KDB}^{e}$ obtained the lowest average rank of 2.5952 , followed by $\mathrm{kdb}^{e}$ with 3.5595 and RF with 3.7024 (very close to those for AODE). When assessing performance using RMSE, $\mathrm{KDB}^{e}$ still performed the best, followed by RF with 3.4285 and AODE with 3.7500 . We found NB at the other extreme on both measures, with average ranks 5.8690 and 5.9523 out of a total of seven learners.
![img-10.jpeg](img-10.jpeg)

Figure 11. Average ranks in terms of zero-one loss and RMSE for all learners.

Since we rejected the null-hypotheses, Nemenyi test was used to further analyze which pairs of algorithms were significantly different in terms of average ranks of the Friedman test. The performance of two classifiers is significantly different if their corresponding average ranks of the Friedman test differ by at least the critical difference $(C D)$ :

$$
C D=q_{\alpha} \sqrt{\frac{t(t+1)}{6 N}}
$$

where the critical value $q_{\alpha}$ for $\alpha=0.05$ and $t=7$ is 2.949 . Given seven algorithms and 42 datasets, we used Equation (16) to calculate $C D$ and the result is 1.3902 . The learners in Figure 12 are plotted on the red line on the basis of their average ranks, corresponding to the nodes on the top black line. If two algorithms had no significant difference, they were connected by a line. As shown in Figure 12a, we easily found that $\mathrm{KDB}^{e}$ had a significantly lower average zero-one loss rank than NB, TAN and KDB. $\mathrm{KDB}^{e}$ also achieved lower average zero-one loss rank than $\mathrm{kdb}^{e}, \mathrm{RF}$ and AODE, but not significantly so. When RMSE was considered, $\mathrm{KDB}^{e}$ still performed the best and the rank of $\mathrm{KDB}^{e}$ was significantly lower than that of KDB , providing solid evidence for the effectiveness of our proposed discriminatory target learning framework.
![img-11.jpeg](img-11.jpeg)

Figure 12. Nemenyi test in terms of zero-one loss and RMSE for all learners.

# 5. Conclusions 

Lack of explanatory insight into the relative influence of the random variables greatly restricts the application domain of machine learning techniques. By redefining mutual information and conditional information, the framework of discriminatory target learning can help fully and discriminately describe the dependency relationships in unlabeled instance and labeled training data. The $\mathrm{kdb}^{e}$ learned from unlabeled instance and regular KDB learned from training data are different but complementary in nature, which will help further improve the classification performance. Discriminatory target learning can be expected to play for different types of BNCs with different dependency complexities. Exploration of application of discriminatory target learning in other kinds of machine learning techniques, e.g., decision tree or support vector machine, is a further area for future work.

Author Contributions: Formal analysis, M.M.; Funding acquisition, M.-H.S.; Methodology, L.-M.W.; Resources, L.-M.W.; Validation, H.L.; Writing—original draft, Z.-Y.D.; Writing—review and editing, Z.-Y.D.

Acknowledgments: This work was supported by the National Science Foundation of China, Grant No. 61272209 and No. 61872164.
Conflicts of Interest: The authors declare no conflict of interest.

## Appendix A. Tables of the Experimental Section

The best results in each row of each table are annotated with bold font.

Table A1. Experimental results of average zero-one loss.


Table A2. Experimental results of average RMSE.


Table A2. Cont.


Table A3. Experimental results of average bias.


Table A3. Cont.


Table A4. Experimental results of average variance.


Table A4. Cont.


Table A5. Ranks in terms of zero-one loss of different learners.


Table A6. Ranks in terms of RMSE of different learners.

