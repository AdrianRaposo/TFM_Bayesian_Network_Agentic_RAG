# Mining multi-dimensional concept-drifting data streams using Bayesian network classifiers 

Hanen Borchani ${ }^{\mathrm{a}, *}$, Pedro Larrañaga ${ }^{\mathrm{a}}$, João Gama ${ }^{\mathrm{b}}$ and Concha Bielza ${ }^{\mathrm{a}}$<br>${ }^{a}$ Computational Intelligence Group, Departamento de Inteligencia Artificial, Facultad de Informática, Universidad Politécnica de Madrid, Madrid, Spain<br>${ }^{\mathrm{b}}$ LIAAD-INESC Porto, Faculty of Economics, University of Porto, Porto, Portugal


#### Abstract

In recent years, a plethora of approaches have been proposed to deal with the increasingly challenging task of mining concept-drifting data streams. However, most of these approaches can only be applied to uni-dimensional classification problems where each input instance has to be assigned to a single output class variable. The problem of mining multi-dimensional data streams, which includes multiple output class variables, is largely unexplored and only few streaming multi-dimensional approaches have been recently introduced. In this paper, we propose a novel adaptive method, named Locally Adaptive-MB-MBC (LA-MB-MBC), for mining streaming multi-dimensional data. To this end, we make use of multi-dimensional Bayesian network classifiers (MBCs) as models. Basically, LA-MB-MBC monitors the concept drift over time using the average log-likelihood score and the Page-Hinkley test. Then, if a concept drift is detected, LA-MB-MBC adapts the current MBC network locally around each changed node. An experimental study carried out using synthetic multi-dimensional data streams shows the merits of the proposed method in terms of concept drift detection as well as classification performance.


## 1. Introduction

Nowadays, with the rapid growth of information technology, huge flows of records are generated and collected daily from a wide range of real-world applications, such as network monitoring, telecommunications data management, social networks, information filtering, fraud detection, etc. These flows are defined as data streams. Contrary to finite stationary databases, data streams are characterized by their concept-drifting aspect [37,39], which means that the learned concepts and/or the underlying data distribution are not stable and may change over time. Moreover, data streams pose many challenges to computing systems due to limited memory resources (i.e., the stream can not be fully stored in memory), and time (i.e., the stream should be continuously processed and the learned classification model should be ready at any time to be used for prediction).

In recent years, the field of mining concept-drifting data streams has received an increasing attention and a plethora of approaches have been developed and deployed in several applications [1,5,11,15,17,

[^0]
[^0]:    *Corresponding author: Hanen Borchani, Computational Intelligence Group, Departamento de Inteligencia Artificial, Facultad de Informática, Universidad Politécnica de Madrid, Boadilla del Monte, 28660 Madrid, Spain. Tel.: +34 913363675; Fax: +34 913524819; E-mail: hanen.borchani@upm.es.

39]. All proposed approaches have a main objective consisting of coping with the concept drift and maintaining the classification model up-to-date along the continuous flows of data. They are usually composed of a detection method to monitor the concept drift and an adaptation method used for updating the classification model over time.

However, most of the work within this field has only been focused on mining uni-dimensional data streams where each input instance has to be assigned to a single output class variable. The problem of mining multi-dimensional data streams, where each instance has to be simultaneously associated with multiple output class variables, remains largely unexplored and only few multi-dimensional streaming methods have been introduced [23|30|33|40].

In this paper, we present a new method for mining multi-dimensional data streams based on multidimensional Bayesian network classifiers (MBCs). The so-called Locally Adaptive-MB-MBC (LA-MB-MBC) extends the stationary MB-MBC algorithm [6] to tackle the concept-drifting aspect of data streams. Basically, LA-MB-MBC monitors the concept drift over time using the average log-likelihood score and the Page-Hinkley test. Then, if a concept drift is detected, LA-MB-MBC adapts the current MBC network locally around each changed node. An experimental study carried out using synthetic multi-dimensional data streams shows the merits of the proposed adaptive method in terms of concept drift detection and classification performance.

The remainder of this paper is organized as follows. Section 2 briefly defines the multi-dimensional classification problem, then introduces multi-dimensional Bayesian network classifiers. Section 3 discusses the concept drift problem, and Section 4 reviews the related work on mining multi-dimensional data streams. Next, Section 5 introduces the proposed method for change detection and local MBC adaptation. Sections 6 and 7 cover the experimental study presenting the used data, the evaluation metrics, and a discussion on the obtained results. Finally, Section 8 rounds the paper off with some conclusions and future works.

# 2. Background 

### 2.1. Multi-dimensional classification

In the traditional and more popular task of uni-dimensional classification, each instance in the data set is associated with a single class variable. However, in many real-world applications, more than one class variable may be required. That is, each instance in the data set has to be associated with a set of many different class variables at the same time. An example would be classifying movies at the online internet movie database (IMDb). In this case, a given movie may be classified simultaneously into three different categories, e.g. action, crime and drama. Additional examples may include a patient suffering from multiple diseases, a text document belonging to several topics, a gene associated with multiple functional classes, etc.

Hence, the multi-dimensional classification problem can be viewed as an extension of the unidimensional classification problem where simultaneous prediction of a set of class variables is needed. Formally, it consists of finding a function $f$ that predicts for each input instance given by a vector of $m$ features $\mathbf{x}=\left(x_{1}, \ldots, x_{m}\right)$, a vector of $d$ class values $\mathbf{c}=\left(c_{1}, \ldots, c_{d}\right)$, that is,

$$
\begin{aligned}
& f: \Omega_{X_{1}} \times \ldots \times \Omega_{X_{m}} \longrightarrow \Omega_{C_{1}} \times \ldots \times \Omega_{C_{d}} \\
& \mathbf{x}=\left(x_{1}, \ldots, x_{m}\right) \longmapsto \mathbf{c}=\left(c_{1}, \ldots, c_{d}\right)
\end{aligned}
$$

where $\Omega_{X_{i}}$ and $\Omega_{C_{j}}$ denote the sample spaces of each feature variable $X_{i}$, for all $i \in\{1, \ldots, m\}$, and each class variable $C_{j}$, for all $j \in\{1, \ldots, d\}$, respectively. Note that, we consider that all class and feature variables are discrete random variables such that $\left|\Omega_{X_{i}}\right|$ and $\left|\Omega_{C_{j}}\right|$ are greater than 1 .

When $\left|\Omega_{C_{j}}\right|=2$ for all $j \in\{1, \ldots, d\}$, i.e., all class variables are binary, the multi-dimensional classification problem is known as a multi-label classification problem [25,36,42]. A multi-label classification problem can be easily modeled as a multi-dimensional classification problem where each label corresponds to a binary class variable. However, modeling a multi-dimensional classification problem, that possibly includes non-binary class variables, as a multi-label classification problem may require a transformation over the data set to meet multi-label framework requirements.

Since our proposed method is general and can be applied to classification problems where class variables are not necessarily binary, we opt to use, unless mentioned otherwise, the term multi-dimensional classification as a more general concept.

# 2.2. Multi-dimensional Bayesian network classifiers 

A Bayesian network [22,28] over a finite set $\mathbf{U}=\left\{X_{1}, \ldots, X_{n}\right\}, n \geqslant 1$, of discrete random variables is a pair $\mathcal{B}=(\mathcal{G}, \times) . \mathcal{G}=(V, A)$ is a directed acyclic graph (DAG) whose vertices $V$ correspond to variables $X_{i}$ and whose arcs $A$ represent conditional dependence relationships between triplets of variables. $\Theta$ is a set of parameters such that each of its components $\theta_{x_{i} \mid \mathbf{p a}\left(x_{i}\right)}=P\left(x_{i} \mid \mathbf{p a}\left(x_{i}\right)\right)$ represents the conditional probability of each possible value $x_{i}$ of $X_{i}$ given a set value $\mathbf{p a}\left(x_{i}\right)$ of $\mathbf{P a}\left(X_{i}\right)$, where $\mathbf{P a}\left(X_{i}\right)$ denotes the set of parents of $X_{i}$ (nodes directed to $X_{i}$ ) in $\mathcal{G}$. The set of parameters $\Theta$ is organized in tables, referred to as conditional probability tables (CPTs). $\mathcal{B}$ defines a joint probability distribution over $\mathbf{U}$ factorized according to structure $\mathcal{G}$ given by:

$$
P\left(x_{1}, \ldots, x_{n}\right)=\prod_{i=1}^{n} P\left(x_{i} \mid \mathbf{p a}\left(x_{i}\right)\right)
$$

Two important definitions follow:
Definition 1. Two sets of variables $\mathbf{X}$ and $\mathbf{Y}$ are conditionally independent given some set of variables $\mathbf{Z}$, denoted as $I(\mathbf{X}, \mathbf{Y} \mid \mathbf{Z})$, iff $P(\mathbf{X} \mid \mathbf{Y}, \mathbf{Z})=P(\mathbf{X} \mid \mathbf{Z})$ for any assignment of values $\mathbf{x}, \mathbf{y}, \mathbf{z}$ of $\mathbf{X}, \mathbf{Y}, \mathbf{Z}$, respectively, such that $P(\mathbf{Z}=\mathbf{z})>0$.
Definition 2. A Markov blanket of a variable $X$, denoted as $M B(X)$, is a minimal set of variables with the following property: $I(X, \mathbf{S} \mid M B(X))$ holds for every variable subset $\mathbf{S}$ with no variables in $M B(X) \cup X$.

In other words, $M B(X)$ is a minimal set of variables conditioned by which $X$ is conditionally independent of all the remaining variables. Under the faithfulness assumption, ensuring that all the conditional independencies in the data distribution are strictly those entailed by $\mathcal{G}, M B(X)$ consists of the union of the set of parents, children, and parents of children (i.e., spouses) of $X$ [29]. For instance, as shown in Fig. 1, $M B(X)=\{A, B, C, D, E\}$ which consists of the union of $X$ parents $\{A, B\}$, its children $\{C, D\}$, and the parent of its child node $D$, i.e., $\{E\}$.

A multi-dimensional Bayesian networks classifier (MBC) is a Bayesian network specially designed to deal with the emerging problem of multi-dimensional classification.
Definition 3. An MBC [38] is a Bayesian network $\mathcal{B}=(\mathcal{G}, \times)$ where the structure $\mathcal{G}=(V, A)$ has a restricted topology. The set of $n$ vertices $V$ is partitioned into two sets: $V_{C}=\left\{C_{1}, \ldots, C_{d}\right\}, d \geqslant 1$, of class variables and $V_{X}=\left\{X_{1}, \ldots, X_{m}\right\}, m \geqslant 1$, of feature variables $(d+m=n)$. The set of arcs $A$ is partitioned into three sets $A_{C}, A_{X}$ and $A_{C X}$, such that:

![img-0.jpeg](img-0.jpeg)

Fig. 1. The Markov blanket of $X$ denoted $M B\langle X\rangle$ consists of the union of its parents $\{A, B\}$, its children $\{C, D\}$, and the parent $\{E\}$ of its child $D$.
![img-1.jpeg](img-1.jpeg)

Fig. 2. An example of an MBC structure.
$-A_{C} \subseteq V_{C} \times V_{C}$ is composed of the arcs between the class variables having a subgraph $\mathcal{G}_{C}=$ $\left(V_{C}, A_{C}\right)$ - class subgraph - of $\mathcal{G}$ induced by $V_{C}$.
$-A_{X} \subseteq V_{X} \times V_{X}$ is composed of the arcs between the feature variables having a subgraph $\mathcal{G}_{X}=$ $\left(V_{X}, A_{X}\right)$ - feature subgraph - of $\mathcal{G}$ induced by $V_{X}$.
$-A_{C X} \subseteq V_{C} \times V_{X}$ is composed of the arcs from the class variables to the feature variables having a subgraph $\mathcal{G}_{C X}=\left(V, A_{C X}\right)$ - bridge subgraph - of $\mathcal{G}$ induced by $V$ [4].

Classification with an MBC under a $0-1$ loss function is equivalent to solving the most probable explanation (MPE) problem, which consists of finding the most likely instantiation of the vector of class variables $\mathbf{c}^{*}=\left(c_{1}^{*}, \ldots, c_{d}^{*}\right)$ given an evidence about the input vector of feature variables $\mathbf{x}=$ $\left(x_{1}, \ldots, x_{m}\right)$. Formally,

$$
\mathbf{c}^{*}=\left(c_{1}^{*}, \ldots, c_{d}^{*}\right)=\arg \max _{c_{1}, \ldots, c_{d}} p\left(C_{1}=c_{1}, \ldots, C_{d}=c_{d} \mid \mathbf{x}\right)
$$

Example 1. An example of an MBC structure is shown in Fig. 2. The class subgraph $\mathcal{G}_{C}=\left(\left\{C_{1}\right.\right.$, $\left.\left.\ldots, C_{4}\right\}, A_{C}\right)$ such that $A_{C}$ consists of the two arcs between the class variables $C_{1}, C_{2}$, and $C_{3}$, the feature subgraph $\mathcal{G}_{X}=\left(\left\{X_{1}, \ldots, X_{8}\right\}, A_{X}\right)$ such that $A_{X}$ contains the three arcs between the feature variables, and finally, the bridge subgraph $\mathcal{G}_{C X}=\left(\left\{C_{1}, \ldots, C_{4}, X_{1}, \ldots, X_{8}\right\}, A_{C X}\right)$ such that $A_{C X}$ is composed of the eight arcs from the class variables to the feature variables. As an MPE problem, we have

$$
\begin{aligned}
\max _{c_{1}, \ldots, c_{4}} P\left(c_{1}, \ldots, c_{4} \mid \mathbf{x}\right)= & \max _{c_{1}, \ldots, c_{4}} P\left(c_{1} \mid c_{2}, c_{3}\right) P\left(c_{2}\right) P\left(c_{3}\right) P\left(c_{4}\right) \\
& \cdot P\left(x_{1} \mid c_{2}, x_{4}\right) P\left(x_{2} \mid c_{1}, c_{2}, x_{5}\right) P\left(x_{3} \mid c_{4}\right) P\left(x_{4} \mid c_{1}\right) \\
& \cdot P\left(x_{5}\right) P\left(x_{6} \mid c_{3}\right) P\left(x_{7} \mid c_{4}\right) P\left(x_{8} \mid c_{4}, x_{6}\right)
\end{aligned}
$$

# 3. Concept drift 

In uni-dimensional data streams, concept drift refers to the changes in the joint probability distribution $P(\mathbf{x}, c)$ which is the product of the class posterior distribution $P(c \mid \mathbf{x})$ and the feature distribution $P(\mathbf{x})$. Therefore, three types of concept drift can be distinguished [17,37]: conditional change (also known as real concept drift) if a change occurs in $P(c \mid \mathbf{x})$; feature change (also known as virtual concept drift) if a change occurs in $P(\mathbf{x})$; and dual change if changes occur in both $P(c \mid \mathbf{x})$ and $P(\mathbf{x})$.

Depending on the rate (also known as the extent or the speed) of change, concept drift can be also

categorized into either abrupt or gradual. An abrupt concept drift occurs at a specific time point by suddenly switching from one concept to another. On the contrary, in a gradual concept drift, a new concept is slowly introduced over an extended time period. An additional categorization is based on whether the concept drift is local or global. A concept drift is said to be local when it only occurs in some regions of the instance space (sub-spaces), and global when it occurs in the whole instance space [12].

Several additional concept drift categorizations may be found in literature such as the one proposed by Minku et al. [26] characterizing concept drifts according to different additional criteria, namely, severity (severe if no instance maintains its target class in the new concept, or intersected otherwise), frequency (periodic or non-periodic) and predictability (predictable or random). Concept drifts may be also reoccurring if previously seen concepts reappear (generally at irregular time intervals) over time, or novelties when some new variables or some of their respective states appear or disappear over time [16].

The same definitions and categorizations of uni-dimensional concept drift can be applied in the context of multi-dimensional data streams. In fact, the feature change involving only a change in $P(\mathbf{x})$ is exactly the same; whereas, for the conditional change, we have now a vector of $d$ class variables $\mathbf{C}=\left(C_{1}, \ldots, C_{d}\right)$ instead of a single class variable $C$, i.e., the conditional change may occur in the distribution $P(\mathbf{c} \mid \mathbf{x})$. Moreover, as previously, the change is called dual when both feature and conditional changes occur together. Furthermore, the multi-dimensional concept drift can be also categorized into abrupt or gradual depending on the rate of change, and into local or global depending on whether it occurs in some regions of the instance space or in the whole instance space, respectively.

Consequently, the main differences between the uni-dimensional and the multi-dimensional concept drifts consist mainly of the changes that may occur in the distribution and the dependence relationships between the class variables, as well as the distribution and the dependence relationships between each class variable and the set of feature variables.

Besides these categorizations, and in the context of streaming multi-label classification, Read et al. [33] discuss that concept drift may also involve a change in the label cardinality, that is, a change in the average number of labels associated with each instance computed as $\operatorname{LCard}=1 / N \sum_{l=1}^{N} \sum_{j=1}^{d} c_{j}^{(l)}$ with $c_{j}^{(l)} \in\{0,1\}$, where $N$ denotes the total number of instances and $d$ the number of labels (or binary class variables).

In addition, Xioufis et al. [40] consider that a multi-label data stream contains separate multiple targets (concepts) and each concept is likely to exhibit independently its own drift pattern. This assumption allows to track the drift of each concept separately using for instance the binary relevance method [18]. In fact, binary relevance proceeds by decomposing the multi-label learning problem into $d$ independent binary classification problems, such that each binary classification problem aims to predict a single label value. However, the main drawback of this assumption is the inability to deal with the correlations that concepts may have with each other and which may drift over time.

It is important to note that the different presented types of drift are not exhaustive and the categorizations discussed here are not mutually exclusive. In our case, we particularly deal with a local concept drift in multi-dimensional data streams. Moreover, as mentioned later in Section 6.1, we consider for the empirical study different rates for local concept drifts, i.e., either abrupt or gradual.

# 4. Related work 

In this section, we review the existing related works. All have been developed under the streaming multi-label classification setting, and can be viewed as extension of stationary multi-label methods to concept-drifting data streams.

Qu et al. [30] propose an ensemble of improved binary relevance (MBR) taking into account the dependency among labels. The basic idea is to add each classified label vector as a new feature participating in the classification of the other related labels. To cope with concept drifts, Qu et al. use a dynamic classifier ensemble jointly with a weighted majority voting strategy. No drift detection method is employed in MBR. In fact, the ensemble keeps a fixed number $K$ of base classifiers, and is updated continuously over time by adding new classifiers, trained on the recent data blocks, and discarding the oldest ones. Naive Bayes, C4.5 decision tree algorithm, and support vector machines (SVM) are used as different base classifiers to test the MBR method.

Xioufis et al. [40] tackle a special problem when dealing with multi-label data streams, namely class imbalance, i.e., the skewness in the distribution of positive and negative instances for all or some labels. In fact, each label in the stream may have more negative than positive instances, and some labels may have much more positive instances than others. To deal with this problem, the authors propose a multiple windows classifier (MWC) that maintains two windows of fixed size for each label: one for positive instances and one for negative ones. The size $N_{p}$ of the positive windows is a parameter of the approach and the size $N_{n}$ of the negative windows is determined using the formula $N_{n}=N_{p} / r$, where $r$ is another parameter of the approach, called distribution ratio. $r$ has the role of balancing the distribution of positive and negative instances in the union of the two windows. The authors assume an independent concept drift for each label, and use a binary relevance method [18] with $k$-nearest neighbors ( $k \mathrm{NN}$ ) as base classifier. No drift detection method is employed in MWC. Positive and negative windows of each label are updated continuously over time by including new incoming instances and removing older ones.

Moreover, Kong and Yu [23] propose also an ensemble-based method for multi-label stream classification. The idea is to use an ensemble of multiple random decision trees [41] where tree nodes are built by means of random selected testing variables and spliting values. The so-called Streaming Multi-lAbel Random Trees (SMART) algorithm does not include a change detection method. In fact, to handle concept drifts in the stream, the authors simply use a fading function on each tree node to gradually reduce the influence of historical data over time. The fading function consists of assigning to each old instance with time stamp $t_{i}$ a weight $w(t)=2^{-\left(t-t_{i}\right) / \lambda}$, where $t$ is the current time, and $\lambda$ is a parameter of the approach, called fading factor, indicating the speed of the fading effects. The higher the value of $\lambda$, the slower the weight of each instance will decay.

Finally, Read et al. [33] present a framework for generating synthetic multi-label data streams along with a novel multi-label streaming classification ensemble method based on Hoeffding trees. Their method, named EaHT ${ }_{P S}$, extends the single-label incremental Hoeffding tree (HT) classifier [10] by using a multi-label definition of entropy and by training multi-label pruned sets (PS) at each leaf node of the tree. To handle concept drifts, Read et al. use the ADWIN Bagging method [5] which consists of an online bagging method extended with an adaptive sliding window (ADWIN) as a change detector. When a concept drift is detected, the worst performing classifier of the ensemble of classifiers is replaced with a new classifier. Read et al. also introduce BRa, EaBR, EaPS, HTa methods, that extend respectively binary relevance (BR) [18], ensembles of BR (EBR) [32], ensembles of textttPS (EPS) [31], and multilabel Hoeffding trees (HT) [8] stationary methods by including ADWIN to detect the potential concept drifts.

The presented streaming multi-label methods are summarized in Table 1. Contrary to these methods, which are all based on a multi-label setting, requiring all the class variables to be binary, our proposed adaptive method has no constraints on the cardinalities of the class variables. Moreover, these methods either do not present any drift detection method (for instance, MBR [30], MWC [40] and SMART [23] approaches) or they use a drift detection method and keep updating an ensemble of classifiers over

Table 1
Summary of streaming multi-label classification methods


time by replacing the worst performing classifier with a new one when a drift is detected (such as EaHT ${ }_{P S}$ [33] using ADWIN algorithm as a change detector). In both cases, the concept drift cannot be detected locally, and the adaptation process is basically based on ensemble updating.

In our case, we only use a single model (i.e., MBC) and our proposed drift detection method performs locally: it is based on monitoring the average local log-likelihood of each node of the MBC network using the Page-Hinkley test. Being based on MBCs, our adaptive method presents also the merit of explicitly modeling the probabilistic dependence relationships among all variables through the graphical structure component.

# 5. Locally adaptive-MB-MBC method 

Before providing more details about the proposed approach, let us introduce the following notation. Let $\mathcal{D}=\left\{\mathcal{D}^{1}, \mathcal{D}^{2}, \ldots, \mathcal{D}^{s}, \ldots\right\}$ denote a multi-dimensional data stream that arrives over time in batches, such that $\mathcal{D}^{s}=\left\{\left(\mathbf{x}^{(1)}, \mathbf{c}^{(1)}\right), \ldots,\left(\mathbf{x}^{\left(N^{*}\right)}, \mathbf{c}^{\left(N^{*}\right)}\right)\right\}$ denotes the multi-dimensional batch stream received at step $s$, and containing $N^{s}$ instances. For each instance in the stream, the input vector $\mathbf{x}=\left(x_{1}, \ldots, x_{m}\right)$ of $m$ feature values is associated with an output vector $\mathbf{c}=\left(c_{1}, \ldots, c_{d}\right)$ of $d$ class values. For the sake of simplicity, and regardless of being class or feature variable, we denote by $V_{i}$ each variable in the MBC, $i=1, \ldots, n$, such that $n$ represents the total number of variables, i.e., $n=d+m$. Given an MBC learned from $\mathcal{D}^{s}$, denoted $M B C^{s}$, and a new incoming batch stream $\mathcal{D}^{s+1}$, the adaptive learning problem consists of firstly detecting possible concept drifts, then, if required, updating the current $M B C^{s}$, as $M B C^{s+1}$, to best fit the new distribution of $\mathcal{D}^{s+1}$.

In what follows, we start by presenting the proposed drift detection method in Section 5.1. Next, we introduce the MBC adaptation method in Section 5.2.

### 5.1. Drift detection method

The objective here is to continuously process the batches of data streams and detect the local concept drift when it occurs. As mentioned before, this local concept drift can also be either abrupt or gradual. Our proposed detection method is based on the average local log-likelihood score and the Page-Hinkley test, and is applied locally, i.e., to each variable in the MBC network.

![img-2.jpeg](img-2.jpeg)

Fig. 3. The evolution of the average local log-likelihood values of four different class variables, namely $C_{1}, C_{2}, C_{3}$, and $C_{4}$. (Colours are visible in the online version of the article; http://dx.doi.org/10.3233/IDA-160804)

# 5.1.1. The average local log-likelihood score 

The likelihood measures the probability of a data set $\mathcal{D}^{s}$ given the current multi-dimensional Bayesian network classifier. For convenience in the calculations, the logarithm of the likelihood is usually used:

$$
L L^{s}=\log P\left(D^{s} \mid \boldsymbol{\theta}^{s}\right)=\log \prod_{l=1}^{N^{s}} \prod_{i=1}^{n} P\left(v_{i}^{(l)} \mid \mathbf{p a}\left(v_{i}\right)^{(l)}, \boldsymbol{\theta}^{s}\right)=\sum_{i=1}^{n} \sum_{j=1}^{q_{i}} \sum_{k=1}^{r_{i}} \log \left(\theta_{i j k}^{s}\right)^{N_{i j k}^{s}}
$$

where $v_{i}^{(l)}, \mathbf{p a}\left(v_{i}\right)^{(l)}$ are respectively the values of variable $V_{i}$ and its parent set $\operatorname{Pa}\left(V_{i}\right)$ in the $l^{\text {th }}$ instance in $\mathcal{D}^{s} . r_{i}$ denotes the number of possible states of $V_{i}$, and $q_{i}$ denotes the number of possible configurations that the parent set $\operatorname{Pa}\left(V_{i}\right)$ can take. $N_{i j k}^{s}$ is the number of instances in $\mathcal{D}^{s}$ where variable $V_{i}$ takes its $k^{\text {th }}$ value and $\operatorname{Pa}\left(V_{i}\right)$ takes its $j^{\text {th }}$ configuration.

We consider then the average log-likelihood score in $\mathcal{D}^{s}$, which is equal to the original log-likelihood score $L L^{s}$ divided by the total number of instances $N^{s}$. This in fact will allow us to compare the likelihood of an MBC network based on different batch streams that may present different numbers of instances. Hence, using the maximum likelihood estimation for the parameters, $\hat{\theta}_{i j k}^{s}=\frac{N_{i j k}^{s}}{N_{i j}^{s}}$ where $N_{i j}^{s}=\sum_{k=1}^{r_{i}} N_{i j k}^{s}$ for every $i, \ldots, n$, the average log-likelihood can be expressed as follows:

$$
\overline{L L}^{s}=\sum_{i=1}^{n} \frac{1}{N^{s}} \sum_{j=1}^{q_{i}} \sum_{k=1}^{r_{i}} N_{i j k}^{s} \log \frac{N_{i j k}^{s}}{N_{i j}^{s}}
$$

Finally, since the change should be monitored on each variable, we use the average local log-likelihood of each variable $V_{i}$ in the network expressed as:

$$
\bar{l}_{i}^{s}=\frac{1}{N^{s}} \sum_{j=1}^{q_{i}} \sum_{k=1}^{r_{i}} N_{i j k}^{s} \log \frac{N_{i j k}^{s}}{N_{i j}^{s}}
$$

Example 2. To illustrate the key idea of using the average local log-likelihood to monitor the concept drift, we plot, in Fig. 3, the evolution of the average local log-likelihood values of four different class variables, namely, $C_{1}, C_{2}, C_{3}$, and $C_{4}$. As it can be observed, the average local log-likelihood values for $C_{2}$ and $C_{3}$ are stable over time, which means that there is no concept drift for both variables. However,

abrupt and gradual concept drifts could be detected for variables $C_{1}$ and $C_{4}$, respectively, as their corresponding average local log-likelihood values drop at block 10. In the next section, we will introduce how to detect this drift point using as input the average local log-likelihood values of each variable.

# 5.1.2. Change point detection 

In recent years, several change detection methods have been proposed to determine the point at which the concept drift occurs. As pointed out in [16], these methods can be categorized into four groups: i) methods based on sequential analysis such as the sequential probability ratio test; ii) methods based on control charts or statistical process control; iii) methods based on monitoring distributions on two different time-windows such as the ADWIN algorithm; and iv) contextual methods such as the splice system. More details about these methods and their references can be found in [16], Section 3.2.

In this work, In order to detect the change point, we make use of the Page-Hinkley (PH) test [20,27]. The PH test is a sequential analysis technique commonly used for change detection in signal processing, and has been proven to be appropriate for detecting concept drifts in data streams [34].

In particular, we apply the PH test in order to determine whether a sequence of average local loglikelihood values of a variable $V_{i}$ can be attributed to a single statistical law (null hypothesis); or it demonstrates a change in the statistical law underlying these values (change point). Let $\bar{l}_{i}^{1}, \ldots, \bar{l}_{i}^{s}$, denote the average local log-likelihood values for variavle $V_{i}$ computed with Eq. (5) using the first batch stream $\mathcal{D}^{1}$ till the last received one $\mathcal{D}^{s}$, respectively. To test the above hypothesis, the PH test considers first a cumulative variable $C U M_{i}^{s}$, defined as the cumulated difference between the obtained average local log-likelihood values and their mean till the current moment (i.e., the last batch $\mathcal{D}^{s}$ ):

$$
C U M_{i}^{s}=\sum_{t=1}^{s}\left(\bar{l}_{i}^{t}-\operatorname{mean}_{\bar{l}_{i}^{t}}-\delta\right)
$$

where mean $\underset{\bar{l}_{i}^{t}}{ }=\frac{1}{2} \sum_{h=1}^{t} \bar{l}_{i}^{h}$ denotes the mean of $\bar{l}_{i}^{1}, \ldots, \bar{l}_{i}^{t}$ values, and $\delta$ is a positive tolerance parameter corresponding to the magnitude of changes which are allowed. The maximum value $M A X_{i}^{s}$ of variable $C U M_{i}^{t}$ for $t=1, \ldots, s$, is then computed:

$$
M A X_{i}^{s}=\max \left\{C U M_{i}^{t}, t=1, \ldots, s\right\}
$$

Next, the PH value is computed as the difference between $M A X_{i}^{s}$ and $C U M_{i}^{s}$ :

$$
P H_{i}^{s}=M A X_{i}^{s}-C U M_{i}^{s}
$$

When this difference is greater than a given threshold $\lambda$ (i.e., $P H_{i}^{s}>\lambda$ ), the null hypothesis is rejected and the PH test alarms a change, otherwise, no change is signaled. Specifically, depending on the result of this test, two states can be distinguished:

- If $P H_{i}^{s} \leqslant \lambda$ then there is no concept drift: the distribution of the average local log-likelihood values is stable. The new batch $\mathcal{D}^{s}$ is deemed to come from the same distribution as the previous data set of instances.
- If $P H_{i}^{s}>\lambda$ then a concept drift is considered to have occurred: the distribution of the average local log-likelihood values is drifting. The new batch $\mathcal{D}^{s}$ is deemed to come from a different distribution than the previous data set of instances.
The threshold $\lambda$ is a parameter allowing to control the rate of false alarms. In general, small $\lambda$ values may increase the number of false alarms, whereas higher $\lambda$ values may lead to a fewer false alarms but may rise at the same time the risk of missing some concept drifts.

Note that, the PH test is designed here to detect decreases in the log-likelihood, since an increase in the log-likelihood score informs that the current MBC network still fits well the new data and thus no adaptation is required. In our case, each local PH test value, $P H_{i}^{s}$, allows us to check if a drift occurs or not at each considered variable $V_{i}$. This in fact will locally specify where (i.e., for which set of variables) the concept drift occurs. Afterwards, the challenge is to locally update the MBC structure, i.e., update only the parts that are in conflict with the the new incoming batch stream without re-learning the whole MBC from scratch.

# 5.2. Local MBC adaptation 

The objective here is to locally update the MBC network over time, so that if a concept drift occurs, only the changed parts in the current MBC are re-learned from the new incoming batch stream and not the whole network. This presents two main challenges: First, how to locally detect the changes, and second how to update the current MBC.

To deal with these challenges, we propose the Locally Adaptive-MB-MBC method, outlined by Algorithm 1. Given the current network $M B C^{s}$, the new incoming batch stream $D^{s+1}$, and the PH test parameters $\delta$ and $\lambda$, the local change detection firstly computes the average log-likelihood $\bar{l}_{i}^{s+1}$ of each variable $V_{i}$ using the new incoming batch stream $D^{s+1}$ (step 4), then computes the corresponding value $P H_{i}^{s+1}$ (step 5). Next, if this $P H_{i}^{s+1}$ value is higher than $\lambda$, then variable $V_{i}$ is added to the set of nodes to be changed (steps 6 to 8 ). Subsequently, whenever the resulting set of ChangedNodes is not empty, i.e., a drift is detected, then the UpdateMBC function, outlined by Algorithm 2, is invoked to locally update the current $M B C^{s}$ network (step 11); otherwise, we conclude that no drift is detected and the MBC network is kept unchanged (step 13).

```
Algorithm 1 Locally Adaptive-MB-MBC
    1. Input: Current \(M B C^{s}\), new multi-dimensional data stream \(D^{s+1}, \delta, \lambda\)
    2. ChangedNodes \(=\emptyset\)
    3. for every variable \(V_{i}\) do
    4. Compute the average local log-likelihood \(\bar{l}_{i}^{s+1}\) using Eq. (5)
    5. Compute the local PH test, \(P H_{i}^{s+1}\)
    6. if \(P H_{i}^{s+1}>\lambda\) then
    7. ChangedNodes \(\leftarrow\) ChangedNodes \(\cup\left\{V_{i}\right\}\)
    8. end if
    9. end for
10. if ChangedNodes \(\neq \emptyset\) then
11. \(M B C^{s+1} \leftarrow\) UpdateMBC(ChangedNodes, \(M B C^{s}, D^{s+1}, P C^{s}, M B^{s}\) )
12. else
13. \(M B C^{s+1} \leftarrow M B C^{s}\), i.e., no drift is detected
14. end if
15. return \(M B C^{s+1}\)
```

Before introducing the UpdateMBC algorithm, note that since the local log-likelihood computes the probability of each variable $V_{i}$ given the set of its parents in the MBC structure, then a detected change for a variable $V_{i}$ informs that the set of parents of the variable $V_{i}$ has changed due to either the removal of some existing parents or the inclusion of new parents:

- The removal of an existing parent means that this parent was strongly relevant to $V_{i}$ given $D^{s}$, and becomes either weakly relevant or irrelevant to $V_{i}$ given $D^{s+1}$. In other words, this parent was a member of the parent set, or more broadly a member of the parents-children set of $V_{i}$, but with respect to $D^{s+1}$, it does not pertain to the parents-children set of $V_{i}$.
- The inclusion of a new parent means that this parent was either weakly relevant or irrelevant to $V_{i}$ given $D^{s}$, and becomes strongly relevant to $V_{i}$ given $D^{s+1}$. In other words, this parent was not a member of the parents-children set of $V_{i}$, but with respect to $D^{s+1}$, it should be added as a new member of the parents-children set of $V_{i}$.
Recall that, variables are defined to be strongly relevant if they contain information about $V_{i}$ not found in all other remaining variables. That is, the strongly relevant variables are the members of the Markov blanket of $V_{i}$, and thereby, all the members in the parents-children set of $V_{i}$ are also strongly relevant to $V_{i}$. On the other hand, variables are said to be weakly relevant if they are informative but redundant, i.e., they consist of all the variables with an undirected path to $V_{i}$ which are not themselves members of the Markov blanket nor the parents-children set of $V_{i}$. Finally, variables are defined as irrelevant if they are not informative, and in this case, they consist of variables with no undirected path to $V_{i}[2,21]$.
Therefore, the intuition behind UpdateMBC algorithm, is basically to firstly learn with $D^{s+1}$ the new parents-children set of each changed node using the HITON-PC algorithm [2,3], determine the sets of its old and new adjacent nodes, and then locally update the MBC structure.

UpdateMBC is outlined by Algorithm 2. It takes as input the set of changed nodes, the current network $M B C^{s}$, the new incoming batch stream $D^{s+1}$, the parents-children sets of all variables $P C^{s}$, and the Markov blanket sets of all class variables $M B^{s}$. For each variable $V_{i}$ in the set of changed nodes, UpdateMBC initially learns from $D^{s+1}$ the new parents-children set of $V_{i}, P C\left(V_{i}\right)^{s+1}$, using HITONPC algorithm (step 3). Then, it determines the set of its old adjacent nodes, i.e., $\left\{P C\left(V_{i}\right)^{s} \backslash P C\left(V_{i}\right)^{s+1}\right.$ (step 4). The variables included in this set are variables that pertained to $P C\left(V_{i}\right)^{s}$ but do not pertain anymore to $P C\left(V_{i}\right)^{s+1}$, which means that they represent the set of variables that were strongly relevant to $V_{i}$ and have become either weakly relevant or irrelevant to $V_{i}$. In this case, for each variable OldAdj belonging to this set, the arc between it and $V_{i}$ is removed from $M B C^{s+1}$ (step 5), then, the parents-children and Markov blanket sets are updated accordingly. Specifically, the following rules are performed:

- Remove $V_{i}$ from the parents-children set of OldAdj (step 6): since the arc between $V_{i}$ and OldAdj was removed, $V_{i}$ does not pertain anymore to the parents-children set of OldAdj.
- If the old adjacent node OldAdj is a class variable, then update its Markov blanket $M B(O l d A d j)^{s+1}$ by removing from it the changed node $V_{i}$ and its parents that do not belong to the parents-children set $P C(O l d A d j)^{s+1}$ of OldAdj (steps 7 to 9 ).
- If the changed node $V_{i}$ is a class variable, then update its Markov blanket $M B\left(V_{i}\right)^{s+1}$ by removing from it the old adjacent node OldAdj and its parents that do not belong to the parents-children set of $V_{i}, P C\left(V_{i}\right)^{s+1}$ (steps 10 to 12).
- Update the Markov blanket of each class variable that belongs to the parent set of $V_{i}$, without being a parent nor a child of OldAdj, by removing from it the old adjacent node OldAdj (steps 13 to 15).
Subsequently, UpdateMBC determines the set of the new adjacent nodes of the changed node $V_{i}$, denoted as $\left\{P C\left(V_{i}\right)^{s+1} \backslash P C\left(V_{i}\right)^{s}\right.$ (step 17). The variables included in this set are variables that belong to $P C\left(V_{i}\right)^{s+1}$ but they were not previously in $P C\left(V_{i}\right)^{s}$, which means that they represent the set of variables that were weakly relevant or irrelevant to $V_{i}$ and become strongly relevant to $V_{i}$. Hence, new dependence relationships should be inserted between those variables and $V_{i}$ verifying at each insertion that no cycles are introduced. In this case, a new arc is inserted from each new adjacent node NewAdj to $V_{i}$ (step 18), then the parents-children and Markov blanket sets are updated accordingly. The following rules are performed:

```
Algorithm 2 UpdateMBC(ChangedNodes, \(M B C^{\prime \prime}, D^{\prime \prime+1}, P C^{\prime \prime}, M B^{\prime \prime}\) )
1. Initialization: \(M B C^{\prime \prime+1} \leftarrow M B C^{\prime \prime} ; P C^{\prime \prime+1} \leftarrow P C^{\prime \prime} ; M B^{\prime \prime+1} \leftarrow M B^{\prime \prime}\)
2. for every variable \(V_{i} \in\) ChangedNodes do
3. Learn \(P C\left(V_{i}\right)^{\prime \prime+1} \leftarrow \mathrm{HITON}-\mathrm{PC}\left(V_{i}\right)\)
    \#Determine the set of the old adjacent nodes of the changed node \(V_{i}\)
4. for every variable OldAdj \(\in\left\{P C\left(V_{i}\right)^{\prime \prime} \backslash P C\left(V_{i}\right)^{\prime \prime+1}\right.\) do
5. Remove the arc between OldAdj and \(V_{i}\) from \(M B C^{\prime \prime+1}\)
6. \(\quad P C(\) OldAdj \()^{\prime \prime+1} \leftarrow P C(\) OldAdj \()^{\prime \prime+1} \backslash\left\{V_{i}\right\}\)
7. if OldAdj \(\in V_{C}\) then
8. \(\quad M B(\) OldAdj \()^{\prime \prime+1} \leftarrow M B(\) OldAdj \()^{\prime \prime+1} \backslash\left\{V_{i} \cup\left\{\operatorname{Pa}\left(V_{i}\right)^{\prime \prime+1} \backslash P C(O l d A d j)^{\prime \prime+1}\right\}\right.\)
9. end if
10. if \(V_{i} \in V_{C}\) then
11. \(\quad M B\left(V_{i}\right)^{\prime \prime+1} \leftarrow M B\left(V_{i}\right)^{\prime \prime+1} \backslash\{\) OldAdj \(\cup\left\{\operatorname{Pa}(O l d A d j)^{\prime \prime+1} \backslash P C\left(V_{i}\right)^{\prime \prime+1}\right\}\)
12. end if
13. for every class \(H \in\left\{\operatorname{Pa}\left(V_{i}\right)^{\prime \prime+1} \backslash P C(O l d A d j)^{\prime \prime+1}\right.\) do
14. \(\quad M B(H)^{\prime \prime+1} \leftarrow M B(H)^{\prime \prime+1} \backslash\{\) OldAdj \(\}\)
15. end for
16. end for
    \#Determine the set of the new adjacent nodes of the changed node \(V_{i}\)
17. for every variable NewAdj \(\in\left\{P C\left(V_{i}\right)^{\prime \prime+1} \backslash P C\left(V_{i}\right)^{\prime \prime}\right.\) do
18. Insert an arc from NewAdj to \(V_{i}\) in \(M B C^{\prime \prime+1}\)
19. \(\quad P C(\) NewAdj \()^{\prime \prime+1} \leftarrow P C(\) NewAdj \()^{\prime \prime+1} \cup\left\{V_{i}\right\}\)
20. if NewAdj \(\in V_{C}\) then
21. \(\quad M B(\) NewAdj \()^{\prime \prime+1} \leftarrow M B(\) NewAdj \()^{\prime \prime+1} \cup\left\{V_{i} \cup \operatorname{Pa}\left(V_{i}\right)^{\prime \prime+1}\right\}\)
22. end if
23. if \(V_{i} \in V_{C}\) then
24. \(\quad M B\left(V_{i}\right)^{\prime \prime+1} \leftarrow M B\left(V_{i}\right)^{\prime \prime+1} \cup\{\) NewAdj \(\cup \operatorname{Pa}(\) NewAdj \()^{\prime \prime+1}\}\)
25. end if
26. for every class \(H \in\left\{\operatorname{Pa}\left(V_{i}\right)^{\prime \prime+1} \backslash\{\) NewAdj \(\cup P C(\) NewAdj \()^{\prime \prime+1}\right\}\) do
27. \(\quad M B(H)^{\prime \prime+1} \leftarrow M B(H)^{\prime \prime+1} \cup\{\) NewAdj \(\}\)
28. end for
29. end for
30. end for
31. Learn from \(D^{\prime \prime+1}\) new CPTs for nodes that have got a new parent set in \(M B C^{\prime \prime+1}\)
32. return \(M B C^{\prime \prime+1} ; P C^{\prime \prime+1} ; M B^{\prime \prime+1}\)
```

- Add $V_{i}$ to the parents-children set of NewAdj (step 19): since an arc was inserted between $V_{i}$ and NewAdj, $V_{i}$ becomes a member of the parents-children set of NewAdj.
- If the new adjacent node NewAdj is a class variable, then update its Markov blanket $M B($ NewAdj $)^{\prime \prime+1}$ by adding to it the changed node $V_{i}$ as well as its parent set $\operatorname{Pa}\left(V_{i}\right)$ (steps 20 to 22).
- If the changed node $V_{i}$ is a class, then update its Markov blanket $M B\left(V_{i}\right)^{\prime \prime+1}$ by adding to it NewAdj and its parent set $\operatorname{Pa}($ NewAdj $)$ (steps 23 to 25 ).
- Update the Markov blanket of each class variable that belongs to the parent set of $V_{i}$, without being a parent nor a child NewAdj, by adding to it the new adjacent node NewAdj (steps 26 to 28).

Table 2
$P C^{s}$ and $M B^{s}$ sets for the MBC structure shown in Fig. 2


![img-3.jpeg](img-3.jpeg)

Fig. 4. Example of an MBC structure including structural changes in comparison with the initial MBC structure in Fig. 2. Nodes $C_{1}, C_{4}, X_{2}$, and $X_{5}$, represented in dashed line, are characterized as changed nodes.

Finally, new conditional probability tables (CPTs) are learnt from $D^{s+1}$ for all the nodes that have got a new parent set in $M B C^{s+1}$ (step 31), and then the updated MBC network $M B C^{s+1}$, the sets $P C^{s+1}$ and $M B^{s+1}$ are returned in step 32 .

Note here that, all variables that belong to both $P C\left(V_{i}\right)^{s}$ and $P C\left(V_{i}\right)^{s+1}$ of a changed node $V_{i}$ do not trigger any kind of change. In fact, these variables were strongly relevant to $V_{i}$ and are still strongly relevant to $V_{i}$, so that the dependence relationships between them and $V_{i}$ remain the same. Moreover, the order of processing the changed nodes does not affect the final result, that is, independently of the order, the updated MBC network $M B C^{s+1}$ and the sets $P C^{s+1}$ and $M B^{s+1}$ will be the same by the end of the UpdateMBC algorithm. This is guaranteed because the identification of the old and new adjacent nodes is performed independently for each changed node, and thereby, it is not affected by the order nor by the results of other nodes. The updating process of $P C$ and $M B$ sets is also ensured via simple operations such as removing or adding variables, and hence, the order of variable removal or addition will not affect the final sets.

Example 3. To illustrate the Locally Adaptive-MB-MBC algorithm, let us first reconsider the structure shown in Fig. 2 as an example of an $M B C^{s}$ structure learnt from a batch stream $D^{s}$ using the MB-MBC algorithm [6]. Then, let assume that we receive afterwards a new batch stream $D^{s+1}$ generated from the $M B C^{s+1}$ structure shown in Fig. 4. Given both $M B C^{s}$ and $D^{s+1}$, the Locally Adaptive-MB-MBC algorithm starts by computing the average log-likelihood and the PH test for each variable in $M B C^{s}$. A change should be signaled for variables $C_{1}, C_{4}, X_{2}$, and $X_{5}$ by Algorithm 1, i.e., ChangedNodes $=\left\{C_{1}, C_{4}, X_{2}, X_{5}\right\}$. Then, the MBC network should be locally updated via the UpdateMBC algorithm (Algorithm 2).

![img-4.jpeg](img-4.jpeg)

Fig. 5. Markov blanket of node $C_{1}$ (a) before and (b) after change.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Markov blanket of node $C_{4}$ (a) before and (b) after change.
The UpdateMBC algorithm updates the local structure around each changed node, then updates accordingly the parents-children and Markov blanket sets. Note that UpdateMBC takes as input the current network $M B C^{s}$, the set of ChangedNodes, the new incoming batch stream $D^{s+1}$, as well as the current parents-children sets of all the variables $P C^{s}$, and the current Markov blankets sets of all the class variables $M B^{s}$, all represented in Table 2.

In what follows, we present a trace of UpdateMBC algorithm for each variable in the ChangedNodes set:

- The changed node $C_{1}$ (see Fig. 4): Firstly, we determine the new parents-children set of $C_{1}$ given $D^{s+1}$ using the HITON-PC algorithm (i.e., step 3 in Algorithm 2). We assume that HITON-PC detects the new parents-children set of $C_{1}$ correctly, so we should have $\operatorname{PC}\left(C_{1}\right)^{s+1}=\left\{C_{2}, X_{2}, X_{4}\right\}$. Next, we determine the set of old and new adjacent nodes for $C_{1}$.
* For the old adjacent nodes, the steps 5 to 15 in Algorithm 2 would be performed. In this case, we have $\operatorname{PC}\left(C_{1}\right)^{s} \backslash \operatorname{PC}\left(C_{1}\right)^{s+1}=\left\{C_{3}\right\}$, which means that $C_{1}$ has only $C_{3}$ as an old adjacent node. Thus, we start by removing the arc between $C_{1}$ and $C_{3}$ (step 5); update the parents-children set of $C_{3}$ as follows: $\operatorname{PC}\left(C_{3}\right)^{s+1}=\operatorname{PC}\left(C_{3}\right)^{s+1} \backslash\left\{C_{1}\right\}=\left\{X_{6}\right\}$ (step 6); then, since $C_{3}$ belongs to $V_{C}$, we proceed by updating also the Markov blanket of $C_{3}$ as follows: $M B\left(C_{3}\right)^{s+1}=M B\left(C_{3}\right)^{s+1} \backslash$ $\left\{C_{1} \cup\left\{\operatorname{Pa}\left(C_{1}\right)^{s+1} \backslash P C\left(C_{3}\right)^{s+1}\right\}\right\}$. As it can be seen, we have $\operatorname{Pa}\left(C_{1}\right)^{s+1} \backslash P C\left(C_{3}\right)^{s+1}=$ $\left\{C_{2}\right\}$, hence, $C_{2}$ should be removed from the Markov blanket of $C_{3}$, which results finally in: $M B\left(C_{3}\right)^{s+1}=M B\left(C_{3}\right)^{s+1} \backslash\left\{C_{1}, C_{2}\right\}=\left\{X_{6}\right\}$ (steps 7 to 9 ).
Moreover, since $C_{1}$ belongs to $V_{C}$, we update as well the Markov blanket of $C_{1}$, i.e., $M B\left(C_{1}\right)^{s+1}=M B\left(C_{1}\right)^{s+1} \backslash\left\{C_{3} \cup\left\{\operatorname{Pa}\left(C_{3}\right)^{s+1} \backslash P C\left(C_{1}\right)^{s+1}\right\}\right\}=\left\{C_{2}, X_{2}, X_{4}, X_{5}\right\}$ (steps 10 to 12 ).
Finally, we update the Markov blanket set of each class parent of $C_{1}$ (steps 13 to 15). In our case, we have only $C_{2}$ as parent of $C_{1}$, which does not pertain to $P C\left(C_{3}\right)$, thus $C_{3}$ should

![img-6.jpeg](img-6.jpeg)
(a)
![img-7.jpeg](img-7.jpeg)
(b)

Fig. 7. Parents-children set of node $X_{2}$ (a) before and (b) after change.
![img-8.jpeg](img-8.jpeg)
(a)
![img-9.jpeg](img-9.jpeg)
(b)

Fig. 8. Parents-children set of node $X_{5}$ (a) before and (b) after change.
be removed from the Markov blanket of $C_{2}$, that is, $M B\left(C_{2}\right)^{s+1}=M B\left(C_{2}\right)^{s+1} \backslash\left\{C_{3}\right\}=$ $\left\{C_{1}, X_{1}, X_{2}, X_{4}, X_{5}\right\}$.

* For the new adjacent nodes, we have $\operatorname{PC}\left(C_{1}\right)^{s+1} \backslash \operatorname{PC}\left(C_{1}\right)^{s}=\emptyset$. Thus, no new dependence relationships must be added for $C_{1}$.
- The changed node $C_{4}$ (see Fig. 6): The first step is to determine the new parents-children set of $C_{4}$ given $D^{s+1}$ and using the HITON-PC algorithm. As previously, we assume that HITON-PC detects the new parents-children set of $C_{4}$ correctly, so we should have $\operatorname{PC}\left(C_{4}\right)^{s+1}=\left\{C_{3}, X_{3}, X_{7}, X_{8}\right\}$.
* Next, we determine the set of old adjacent nodes, which in our case is empty, i.e, $\operatorname{PC}\left(C_{4}\right)^{s} \backslash$ $\operatorname{PC}\left(C_{4}\right)^{s+1}=\emptyset$.
* Then, the set of new adjacent nodes which is equal to $\operatorname{PC}\left(C_{4}\right)^{s+1} \backslash \operatorname{PC}\left(C_{4}\right)^{s}=\left\{C_{3}\right\}$. Consequently, we insert an arc from $C_{3}$ to $C_{4}$ (step 18), we update $\operatorname{PC}\left(C_{3}\right)^{s+1}=\operatorname{PC}\left(C_{3}\right)^{s+1} \cup\left\{C_{4}\right\}=$ $\left\{C_{4}, X_{6}\right\}$ (step 19), and $M B\left(C_{3}\right)^{s+1}=M B\left(C_{3}\right)^{s+1} \cup\left\{C_{4} \cup \operatorname{Pa}\left(C_{4}\right)^{s+1}\right\}=\left\{C_{4}, X_{6}\right\}$ (step 20 to 22). Similarly, update the Markov blanket set $M B\left(C_{4}\right)^{s+1}=M B\left(C_{4}\right)^{s+1} \cup\left\{C_{3} \cup \operatorname{Pa}\left(C_{3}\right)^{s+1}\right\}=$ $\left\{C_{3}, X_{3}, X_{7}, X_{8}, X_{6}\right\}$ (steps 23 to 25). $C_{4}$ has no more parents except $C_{3}$, so steps 26-28 in the UpdateMBC algorithm are not applied in this case.
- The changed node $X_{2}$ (see Fig. 7): As previously, the first step is to determine the new parentschildren set of $X_{2}$ given $D^{s+1}$ and using the HITON-PC algorithm. Assuming that HITON-PC detects the new parents-children set of $X_{2}$ correctly, we should have $\operatorname{PC}\left(X_{2}\right)^{s+1}=\left\{C_{1}, X_{7}\right\}$.
* Next, given that $\operatorname{PC}\left(X_{2}\right)^{s}=\left\{C_{1}, C_{2}, X_{5}\right\}$, the set of old adjacent nodes is determined as $\operatorname{PC}\left(X_{2}\right)^{s} \backslash \operatorname{PC}\left(X_{2}\right)^{s+1}=\left\{C_{2}, X_{5}\right\}$.
For the first old adjacent node $C_{2}$, we remove the arc between $C_{2}$ and $X_{2}$, we update $\operatorname{PC}\left(C_{2}\right)^{s+1}=\operatorname{PC}\left(C_{2}\right)^{s+1} \backslash\left\{X_{2}\right\}=\left\{C_{1}, X_{1}\right\}$, and we update $M B\left(C_{2}\right)^{s+1}=M B\left(C_{2}\right)^{s+1} \backslash$ $\left\{X_{2} \cup\left\{\operatorname{Pa}\left(X_{2}\right)^{s+1} \backslash \operatorname{PC}\left(C_{2}\right)^{s+1}\right\}\right\}$. Here $X_{2}$ has two parents namely $C_{1}$ and $X_{5}$ (in fact $X_{5}$ is not removed yet from the set of parents of $X_{2}$ because we start by processing the old adjacent variable $C_{2}$ ), and since $C_{1}$ pertains to $\operatorname{PC}\left(C_{2}\right)^{s+1}$, the only variables to be removed from $M B\left(C_{2}\right)^{s+1}$ are then $X_{2}$ and $X_{5}$, i.e., $M B\left(C_{2}\right)^{s+1}=\left\{C_{1}, X_{1}, X_{4}\right\}$.
For the second old adjacent node $X_{5}$, we remove the arc between $X_{5}$ and $X_{2}$, we update $\operatorname{PC}\left(X_{5}\right)^{s+1}=\operatorname{PC}\left(X_{5}\right)^{s+1} \backslash\left\{X_{2}\right\}=\emptyset$, then update the Markov blanket set for every class variable of $X_{2}$ that does not pertain to $\operatorname{PC}\left(X_{5}\right)^{s+1}$. In our case, $X_{2}$ has only $C_{1}$ as a class parent (because both $C_{2}$ and $X_{5}$ have been already removed), so its Markov blanket is modified as follows $M B\left(C_{1}\right)^{s+1}=M B\left(C_{1}\right)^{s+1} \backslash\left\{X_{5}\right\}=\left\{C_{2}, X_{2}, X_{4}\right\}$.
* For the new adjacent nodes, we have $\operatorname{PC}\left(X_{2}\right)^{s+1} \backslash \operatorname{PC}\left(X_{2}\right)^{s}=\left\{X_{7}\right\}$. Thus, we insert an arc from $X_{7}$ to $X_{2}$, update $\operatorname{PC}\left(X_{7}\right)^{s+1}=\operatorname{PC}\left(X_{7}\right)^{s+1} \cup\left\{X_{2}\right\}=\left\{C_{4}, X_{2}\right\}$, then update the Markov blanket set for every class variable of $X_{2}$ that does not pertain to $\operatorname{PC}\left(X_{7}\right)^{s+1}$. In our case, $X_{2}$ has only $C_{1}$ as a class parent, which is different from $X_{7}$ and not pertaining to $\operatorname{PC}\left(X_{7}\right)$, so its Markov blanket is modified as follows $M B\left(C_{1}\right)^{s+1}=M B\left(C_{1}\right)^{s+1} \cup\left\{X_{7}\right\}=\left\{C_{2}, X_{2}, X_{4}, X_{7}\right\}$.

- The changed node $X_{5}$ (see Fig. 8): The first step is to determine the new parents-children set of $X_{5}$ given $D^{s+1}$ and using the HITON-PC algorithm. Assuming that HITON-PC detects the new parents-children set of $X_{5}$ correctly, we obtain $P C\left(X_{5}\right)^{s+1}=\left\{C_{3}\right\}$.
* Then, given that $P C\left(X_{5}\right)^{s}=\left\{X_{2}\right\}$, we determine first the set of old adjacent nodes $P C\left(X_{5}\right)^{s} \backslash$ $P C\left(X_{5}\right)^{s+1}=\left\{X_{2}\right\}$. Since the changed variable $X_{2}$ has been processed before the changed node $X_{5}$, we can see that the arc between these two variables has been already removed during the previous phase. Moreover, $X_{5}$ has been already removed from $P C\left(X_{2}\right)^{s+1}$, so there is no change for $P C\left(X_{2}\right)^{s+1}=\left\{C_{1}, X_{7}\right\} . X_{5}$ at this step has no class parents, so steps 13-15 in the UpdateMBC algorithm are not applied in this case.
* For the new adjacent nodes, we have $P C\left(X_{5}\right)^{s+1} \backslash P C\left(X_{5}\right)^{s}=\left\{C_{3}\right\}$. Thus, we insert an arc from $C_{3}$ to $X_{5}$, update $P C\left(C_{3}\right)^{s+1}=P C\left(C_{3}\right)^{s+1} \cup\left\{X_{5}\right\}=\left\{C_{4}, X_{5}, X_{6}\right\}$, and update its Markov blanket set $M B\left(C_{3}\right)^{s+1}=M B\left(C_{3}\right)^{s+1} \cup\left\{X_{5}\right\}=\left\{C_{4}, X_{5}, X_{6}\right\} . X_{5}$ is not a class variable and has no more class parents except $C_{3}$, so no more changes have to be considered.
Note finally that, the changes performed on the local structure of each changed node lead as well to the changes of the PC and MB sets of some adjacent nodes such as, in our case, those of variables $C_{2}, C_{3}$ and $X_{7}$. However, some other variables do not present any change and their PC sets are kept the same, namely, $X_{1}, X_{3}, X_{4}, X_{6}$, and $X_{8}$. In addition, the order of processing the changed variables affects the order of the execution of some operations, however it does not affect the final result.


# 6. Experimental design 

### 6.1. Data sets

We will use the following data streams:

- Synthetic multi-dimensional data streams: We randomly generated a sequence of five MBC networks, such that the first MBC network is randomly defined on a set of $d=5$ class variables and $m=10$ feature variables. Then, each subsequent MBC network is obtained by randomly changing the dependence relationships around a percentage $p$ of nodes with respect to the preceding MBC network in the sequence. Depending on parameter $p$, we set three different configurations to test different rates of concept drift:
* Configuration 1: No concept drift ( $p=0 \%$ ). In this case, the same MBC network is used to sample the total number of instances in the sequence. This aims to generate a stationary data stream and allows us to verify the resilience of the proposed algorithm to false alarms.
* Configuration 2: Gradual concept drift ( $p=20 \%$ ). The percentage of changed nodes between each consecutive MBC networks is equal to $p=20 \%$. For each selected changed node, its parent set is modified by removing the existing parents and randomly adding new ones. For the parameters, new CPTs are randomly generated for the set of changed nodes presenting new parent sets, whereas the CPTs of the non-changed nodes are kept the same as the preceding MBC.
* Configuration 3: Abrupt concept drift ( $p=50 \%$ ). Similar to configuration 2, but we fixed the percentage of changed nodes between each consecutive MBC networks to $p=50 \%$.
Afterwards, for each configuration, 5000 instances are randomly sampled from each MBC network in the sequence, using the probabilistic logic sampling method [19], then concatenated to form a data stream of 25000 instances.

- SynT-drift data stream provided by Read et al. [33]: In order to compare our approach against existing multi-label stream classification methods (see Section 4), namely, BRa, EaBR, EaHT ${ }_{P S}$, EaPS, HTa, MBR, and MWC, we test our proposed adaptive methods on SynT-drift.
SynT-drift is a multi-label synthetic data stream including 1000000 instances with $d=8$ binary class variables and $m=30$ binary feature variables. It is sampled using the random tree generator proposed by Domingos and Hulten [10], that constructs a decision tree by choosing attributes at random to split, and assigning a random class label to each leaf. Once the tree is built, new examples are generated by assigning uniformly random values to attributes which then determine the class label via the tree.
Read et al. [33] included three concept drifts in SynT-drift of varying type, magnitude and extent. In the first drift, they changed only $10 \%$ of label dependencies. In the second drift, the underlying concept changes and more labels are associated on average with each instance (i.e., the label cardinality LCard changes from 1.8 to 3.0), and in the third drift, $20 \%$ of label dependencies change.


# 6.2. Evaluation metrics 

The synthetic data streams are processed by windows of instances, and the prequential setting [9|14] is used to evaluate the predictive performance of the MBC network on each window. In this setting, each incoming window is used for testing the MBC network before it is used for training, in such a way that the MBC network is always tested on instances that have not been seen before. We used the following metrics in order to assess the performance of the proposed adaptive method:

- Mean accuracy over the $d$ class variables. It is defined as a class-based measure where the accuracy is calculated separately for each class variable, then averaged across all the class variables:

$$
A c c_{m}=\frac{1}{d} \sum_{i=1}^{d} \frac{1}{N^{s}} \sum_{l=1}^{N^{s}} \delta\left(\hat{c}_{l i}, c_{l i}\right)
$$

where $N^{s}$ is the size of the testing data set, $\hat{c}_{l i}$ denotes the $C_{i}$ class value predicted by the multidimensional classifier for sample $l$, and $c_{l i}$ denotes its corresponding true value. $\delta\left(\hat{c}_{l i}, c_{l i}\right)=1$ if the predicted and true class values are equal, i.e., $\hat{c}_{l i}=c_{l i}$, and $\delta\left(\hat{c}_{l i}, c_{l i}\right)=0$ otherwise.

- Global accuracy over the $d$-dimensional class variable (also known as exact match [33]). It is considered as an instance-based measure where the accuracy is calculated separately for each instance in the testing data set, then averaged across all the instances:

$$
A c c_{g}=\frac{1}{N^{s}} \sum_{l=1}^{N^{s}} \delta\left(\hat{\mathbf{c}}_{l}, \mathbf{c}_{l}\right)
$$

In this more strict case, the ( $d$-dimensional) vector of predicted classes $\hat{\mathbf{c}}_{l}$ is compared to the vector of true classes $\mathbf{c}_{l}$, so that we have $\delta\left(\hat{\mathbf{c}}_{l}, \mathbf{c}_{l}\right)=1$ if both vectors are equal in all their components, i.e., $\hat{\mathbf{c}}_{l}=\mathbf{c}_{l}$, and $\delta\left(\hat{\mathbf{c}}_{l}, \mathbf{c}_{l}\right)=0$ otherwise.
Note that for experiments on SynT-drift data stream, the KLDiv and SHD evaluation are omitted since we do not have an original MBC network for this data. Moreover, as reported in [33], we compute the subset accuracy instead of the mean accuracy:

- Subset accuracy: This is an instance-based measure defined as a trade-off between the mean accuracy (which tends to be overly lenient) and the global accuracy (which tends to be overly strict). It alleviates the very strict global accuracy measure by taking into account the partial correctness of

the predicted class values and is computed as:

$$
A c c_{\text {subset }}=\frac{1}{N} \sum_{l=1}^{N} \frac{\left|\hat{\mathbf{c}}_{l} \cap \mathbf{c}_{l}\right|}{\left|\hat{\mathbf{c}}_{l} \cup \mathbf{c}_{l}\right|}
$$

- Kullback-Leibler Divergence (KLDiv) [24]: It measures the divergence between the learned MBC networks and the original ones. The lower the KLDiv values, the better the quality of the learning algorithm.
- Structural Hamming Distance (SHD) [35]: It compares the structure of the learned and the original MBC networks, and is defined as the number of operations required to make two completed partially DAGs (CPDAGs) match. The operations are add or delete an undirected edge, and add, delete, or reverse the orientation of an edge. Each of these operations is penalized with the same strength by increasing the SHD by 1. In our case, since all learned and original MBCs are DAGs, we build first the CPDAGs of both learned and original MBC DAGs using the DAG-to-CPDAG algorithm [7], then we compute the SHD metric. The lower the resulting SHD value is, the better the algorithm performed.
- Running time: It reports the cumulative learning plus testing times in seconds.


# 7. Experimental results 

For the first set of experiments, carried out using 15 variables ( 5 class variables with 3 possible values each, and 10 binary feature variables), we used the probabilistic logic sampling method [19] to randomly sample five different data streams for each configuration (i.e., for each $p=0 \%, p=20 \%$ and $p=50 \%$ ). Each generated data stream includes a total number of 25000 instances.

For the sake of comparison, we consider here the Globally Adaptive-MB-MBC (GA-MB-MBC) which is also based on the MB-MBC algorithm [6] but differs from LA-MB-MBC by dealing globally with concept drift, that is, it learns the whole $M B C^{s}$ network from scratch whenever a change is detected. Specifically, GA-MB-MBC, outlined in Algorithm 3, takes as input the current network $M B C^{s}$, the new incoming batch stream $D^{s+1}$, and the PH test parameters $\delta$ and $\lambda$. It starts by computing the average global log-likelihood $\overline{L L}^{s+1}$ using Eq. (4) (step 2), and the PH test value $P H^{s+1}$ for the whole MBC network (step 3). Next, if $P H^{s+1}$ is higher than $\lambda$, then a new network $M B C^{s+1}$ is learned from $D^{s+1}$ using the MB-MBC algorithm (step 5). Otherwise, i.e., $P H^{s} \leqslant \lambda$, the MBC network is kept unchanged (step 7).

```
Algorithm 3 Globally Adaptive-MB-MBC
    1. Input: Current \(M B C^{s}\), new multi-dimensional data stream \(D^{s+1}, \delta, \lambda\)
    2. Compute the global average log-likelihood \(\overline{L L}^{s+1}\) using Eq. (4)
    3. Compute \(P H^{s+1}\)
    4. if \(P H^{s+1}>\lambda\) then
    5. Learn a new network \(M B C^{s+1}\) from \(D^{s+1}\) using the MB-MBC algorithm.
    6. else
    7. \(M B C^{s+1} \leftarrow M B C^{s}\), i.e., no drift is detected
    8. end if
    9. return \(M B C^{s+1}\)
```

Table 3
Experimental results (mean $\pm$ std. dev.) over synthetic data with $p=0 \%$. Symbol represents statistically significantly better values


Table 4
Experimental results (mean $\pm$ std. dev.) over synthetic data with $p=20 \%$. Symbol represents statistically significantly better values


We applied both LA-MB-MBC and GA-MB-MBC using three different values of $\lambda$, namely $\lambda=1,5$, 10 , and four different block sizes, namely block $=400,700,1000,2000$. This in fact allows us to study the sensitivity of both algorithms with respect to the input parameter $\lambda$ and the block size, respectively. Tables 3-5 show the estimated performance results as mean values and standard deviations for each metric and each method over the five randomly generated data streams. The best result for each metric is written in bold.

In Table 3, presenting the results with $p=0 \%$ (i.e., stationary data streams), we can first notice the very low sensitivity of both algorithms with respect to $\lambda$ values. In fact, even if the best result for the mean accuracy is obtained with GA-MB-MBC with $\lambda=1$ and block $=1000$, and the best result for the global accuracy is obtained with GA-MB-MBC with $\lambda=1$ and block $=1000$ or block $=2000$, both algorithms LA-MB-MBC and GA-MB-MBC present similar predictive performance for the remaining $\lambda$

Table 5
Experimental results (mean $\pm$ std. dev.) over synthetic data with $p=$ $50 \%$. Symbol represents statistically significantly better values


Table 6
Experimental results over SynT-drift data


values (i.e., $\lambda=5$ and $\lambda=10$ ). Moreover, regarding the block size, as expected the best results are obtained with block $=1000$ and block $=2000$ instances; however, using blocks of 400 instances results in the worst results since having only a small number of instances may affect the quality of the learned MBCs. LA-MB-MBC and GA-MB-MBC show similar results as well for SHD, KLDiv, and running time. In order to study whether the differences in each metric performance are statistically significant or not, we performed a statistical comparison using the Friedman test followed by the Tukey-Kramer post-hoc test with a significance level $\alpha=0.05$. We represent the values that are statistically significantly better with the symbol $\bullet$ in Table 3. For all the comparisons, it turns out that only three values were statistically significantly better, which let us state once again that the performance of both algorithms is quite similar.

In Table 4, presenting the experimental results with a drift rate $p=20 \%$, LA-MB-MBC is performing the best with $\lambda=1$ and block $=1000$ for the mean accuracy, global accuracy and KLDiv. However, the best SHD result is obtained with GA-MB-MBC with $\lambda=1$ and block $=700$. In addition, contrary to results in Table $3(p=0 \%)$, we can observe that under a higher drift rate $(p=20 \%)$, both algo-

![img-10.jpeg](img-10.jpeg)

Fig. 9. Classification results with the drift rate $p=0 \%$ and $\lambda=1$. (Colours are visible in the online version of the article; http://dx.doi.org/10.3233/IDA-160804)
rithms become more sensitive to the $\lambda$ value. For both LA-MB-MBC and GA-MB-MBC algorithms, the best accuracies are obtained with $\lambda=1$ and block $=1000$, and as long as $\lambda$ increases, all the performance measures deteriorate. In fact, using higher $\lambda$ values, some concept drifts cannot be detected and consequently the model cannot be updated correctly; which may affect its performance over time. In this case, we can see that GA-MB-MBC is more sensitive since missing the detection of a drift affects the whole MBC network. In addition, as previously, using small blocks leads to worse results than the ones obtained with blocks 1000 or 2000. Finally, we can see that there are only few statistically significant differences (represented by $\bullet$ ) resulting from a statistical comparison of both algorithms using the Friedman test followed by the Tukey-Kramer post-hoc test with a significance level $\alpha=0.05$, i.e., both algorithms show similar predictive performance.

Table 5 shows the experimental results with a drift rate $p=50 \%$. We may observe here that the best accuracies were obtained with GA-MB-MBC with $\lambda=5$ and block $=1000$. In general, we can conclude here that, in all $\lambda$ values, GA-MB-MBC outperforms LA-MB-MBC in SHD and mean and global accuracies, however, LA-MB-MBC presents slightly better KI.Div values than GA-MB-MBC. The better performance of GA-MB-MBC compared to LA-MB-MBC can be explained by the fact that having $50 \%$ of drift affects a larger instance space (i.e., it can be viewed as a global change), and consequently it might be better to re-build all the MBC network rather than updating it locally.

In addition, we plot in Figs 9-11 the mean and global accuracy curves for LA-MB-MBC and GA-MB-MBC algorithms, with $\lambda=1$, block $=1000$, and $p$ equal to $0 \%, 20 \%$ and $50 \%$, respectively. For each curve, the X -axis represents the block number, and the Y -axis represents the classification accuracy. Note that we limited this part to $\lambda=1$, block $=1000$, as similar conclusions are reached with the remaining configurations including different $\lambda$ and block size values.

In Fig. 9, we can observe that LA-MB-MBC and GA-MB-MBC curves are almost superposed showing the similar performance of both algorithms, as well as their resilience to false alarms.

In Figs 10 and 11, we can first notice that both algorithms perform well in detecting the change at blocks 5, 10, 15 and 20. With $p=20 \%$ (Fig. 10) the change is more gradual, whereas, in Fig. 11 with $p=50 \%$, the change is abrupt and more important fluctuations in predictive performance are present. We can also see in Fig. 10 that LA-MB-MBC usually outperforms GA-MB-MBC in updating the MBC network and recuperating more quickly its performance. Nevertheless, with higher drift rate, i.e., $p=$ $50 \%$, GA-MB-MBC presents a slightly better performance than LA-MB-MBC.

![img-11.jpeg](img-11.jpeg)

Fig. 10. Classification results with the drift rate $p=20 \%$ and $\lambda=1$. (Colours are visible in the online version of the article; http://dx.doi.org/10.3233/IDA-160804)
![img-12.jpeg](img-12.jpeg)

Fig. 11. Classification results with the drift rate $p=50 \%$ and $\lambda=1$. (Colours are visible in the online version of the article; http://dx.doi.org/10.3233/IDA-160804)

In the second set of experiments with SynT-drift data streams, we compare both LA-MB-MBC and GA-MB-MBC algorithms against seven multi-label classification methods. Five of them, i.e., BRa, EaBR, $\mathrm{EaHT}_{P S}, \mathrm{EaPS}$ and HTa were proposed by [33], whereas MBR and MWC were proposed respectively in [30,40]. Similarly, as [33], we divide the stream into 20 windows and we report the average of subset and global accuracies across the data windows, as well as the cumulative running time in seconds. Note that both LA-MB-MBC and GA-MB-MBC are performed using $\lambda=1$. The obtained results are reported in Table 6.

For the subset accuracy, GA-MB-MBC performs better than LA-MB-MBC, and also better than any other method except MBR and EaHT ${ }_{P S}$. For the global accuracy, LA-MB-MBC performs better than all remaining methods except HTa. Although not the best, LA-MB-MBC presents a good performance even though SynT-drift data set is generated based on tree models, and as expected, methods based on Hoeffding trees (i.e., EaHT ${ }_{P S}$ and HTa) provide the best accuracy results. Nevertheless, the main shortcoming of our LA-MB-MBC algorithm is the running time which is slower than all remaining methods, and this is mainly due to the testing part that involves the computation of the most probable explanation.

# 8. Conclusion 

In this paper, we have presented a new method for mining multi-dimensional data streams, namely, LA-MB-MBC. Basically, LA-MB-MBC proceeds locally at the level of each node in the MBC network, that is, it monitors the average local log-likelihood of each node over time, then, whenever a concept drift is detected, it learns a new local structure for each changed node.

Experimental results on synthetic data streams including different rates of change were promising. In comparison against the GA-MB-MBC algorithm, LA-MB-MBC is shown to be resilient to false alarms, and also efficient in detecting the change points and adapting the MBC networks especially when there is a small percentage of change. Moreover, both considered methods show similar predictive performance and exhibit competitive accuracy results when compared with existing multi-label classification methods.

In the future, it will be interesting to investigate the use of different exact or approximate inference methods in order to alleviate the computational burden when calculating the most probable explanation.

# Acknowledgements 

This work has been partially supported by the Spanish Ministry of Economy and Competitiveness through the Cajal Blue Brain (C080020-09; the Spanish partner of the Blue Brain initiative from EPFL) and TIN2013-41592-P projects, by the Regional Government of Madrid through the S2013/ICE-2845-CASI-CAM-CM project, and by the European Union's Seventh Framework Programme (FP7/20072013) under grant agreement no. 604102 (Human Brain Project). The authors would like to thank Jesse Read for kindly providing the SynT-drift data stream.
