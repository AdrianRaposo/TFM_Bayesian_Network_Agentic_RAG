# Article 

## Mixture-Based Probabilistic Graphical Models for the Label Ranking Problem ${ }^{\dagger}$

Enrique G. Rodrigo ${ }^{1,2}$ (D), Juan C. Alfaro ${ }^{1,2, * *}$, Juan A. Aledo ${ }^{2,3 *}$ and José A. Gámez ${ }^{1,2}$ (D)<br>check for updates

Citation: Rodrigo, E.G.; Alfaro, J.C.; Aledo, J.A.; Gámez, J.A. Mixture-Based Probabilistic Graphical Models for the Label Ranking Problem. Entropy 2021, 23, 420. https://doi.org/10.3390/ e23040420

Academic Editors: Rafael Rumí and Antonio Salmerón

Received: 9 March 2021
Accepted: 27 March 2021
Published: 31 March 2021

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (0)

Copyright: (c) 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Departamento de Sistemas Informáticos, Universidad de Castilla-La Mancha, 02071 Albacete, Spain; mail@enriquegrodrigo.com (E.G.R.); Jose.Gamez@uclm.es (J.A.G.)
2 Laboratorio de Sistemas Inteligentes y Minería de Datos, Instituto de Investigación en Informática de Albacete, 02071 Albacete, Spain; JuanAngel.Aledo@uclm.es
3 Departamento de Matemáticas, Universidad de Castilla-La Mancha, 02071 Albacete, Spain

* Correspondence: JuanCarlos.Alfaro@uclm.es
+ This is an extended version in proceedings of the 15th European Conference on Symbolic and Quantitative Approaches with Uncertainty, Belgrade, Serbia, 18-20 September 2019.


#### Abstract

The goal of the Label Ranking (LR) problem is to learn preference models that predict the preferred ranking of class labels for a given unlabeled instance. Different well-known machine learning algorithms have been adapted to deal with the LR problem. In particular, fine-tuned instance-based algorithms (e.g., k-nearest neighbors) and model-based algorithms (e.g., decision trees) have performed remarkably well in tackling the LR problem. Probabilistic Graphical Models (PGMs, e.g., Bayesian networks) have not been considered to deal with this problem because of the difficulty of modeling permutations in that framework. In this paper, we propose a Hidden Naive Bayes classifier (HNB) to cope with the LR problem. By introducing a hidden variable, we can design a hybrid Bayesian network in which several types of distributions can be combined: multinomial for discrete variables, Gaussian for numerical variables, and Mallows for permutations. We consider two kinds of probabilistic models: one based on a Naive Bayes graphical structure (where only univariate probability distributions are estimated for each state of the hidden variable) and another where we allow interactions among the predictive attributes (using a multivariate Gaussian distribution for the parameter estimation). The experimental evaluation shows that our proposals are competitive with the start-of-the-art algorithms in both accuracy and in CPU time requirements.


Keywords: mixture models; EM algorithm; Naive Bayes; probabilistic graphical models; label ranking; preference learning; machine learning

## 1. Introduction

Preferences are comparative judgments about a set of alternatives or choices. The Label Ranking (LR) problem [1-3] is a well-known non-standard supervised classification problem [4,5], whose goal is to learn preference models that predict the preferred ranking over a set of class labels for a given unlabeled instance. Practical applications of the LR problem are found in cases where an order of preference (or ranking) for the class labels is required given an input instance. Particular examples can be ranking a set of genes from their expression level, ranking the set of relevant topics for a given document, ranking a set of available machine learning algorithms for a given dataset and prediction task, etc. [6,7].

Formally, we consider a problem domain defined over $n$ predictive variables (also known as attributes), $X_{1}, \ldots, X_{n}$, and a class variable $C$ with $m$ labels, $\operatorname{dom}(C)=\left\{c_{1}, \ldots, c_{m}\right\}$. We are interested in predicting the ranking $\pi$ of the labels for an unlabeled instance $e_{t}=$ $\left(x_{1, t}, \ldots, x_{n, t}\right) \in \operatorname{dom}\left(X_{1}\right) \times \cdots \times \operatorname{dom}\left(X_{n}\right)$ given a dataset $\mathbf{D}=\left\{\left(x_{1, j}, \ldots, x_{n, j}, \pi_{j}\right)\right\}_{j=1}^{N}$ with $N$ labeled instances. Therefore, the LR problem consists in learning a LR-Classifier $\mathcal{C}$ from $\mathbf{D}$ which generalizes well on unseen data.

In other words, the goal of the LR problem is to induce a model able to predict a permutation of the class labels by taking advantage of all the available information during the learning process. Different approaches have been proposed to tackle this problem:

- Transformation methods. They transform the ranking-based prediction problem into a set of single-class classifiers, whose outcomes must be later aggregated in order to obtain a ranking. Various approaches have been considered, such as labelwise [8] and pairwise approaches [9,10], chain classifiers [11], etc.
- Adaptation methods. They adapt well-known machine learning algorithms to cope with the new class structure. Cheng et al. in [2] introduced a model-based algorithm that induces a decision tree (Label Ranking Trees (LRT)) and a model-free algorithm which uses $k$-nearest neighbors (Instance-Based Label Ranking (IBLR)). Other techniques, like association rules [12] or neural networks [13], have also been adapted.
- Ensemble methods. Recently, different tree-based aggregation approaches, such as Random Forests, Bagging predictors, and Boosting methods, have been successfully applied to the LR problem [14-17].
In this paper, we propose a new model-based LR-classifier which belongs to the adaptation methods family. Our motivation is twofold:
- Although fine-tuned instance-based algorithms have exhibited remarkable performance (especially when the model is trained with complete rankings), they may demand a great amount of computational resources (memory and time) during model selection and inference when the size of the dataset grows.
- Although Probabilistic Graphical Models (PGMs; e.g., Bayesian networks) [18,19] constitute a standard approach in machine learning, they have not been used in this problem because of the difficulty in coping with permutations in this framework [2,20]. In this work, we successfully introduce the use of PGMs to deal with the LR problem, obtaining results which are competitive with the state-of-the-art IBLR and LRT algorithms.
The proposed probabilistic LR-classifier relies on the use of a hybrid Bayesian network [21] where different probability distributions are used to conveniently model variables of a different nature: Multinomial for discrete variables, Gaussian for numerical variables, and Mallows for permutations [22]. The Mallows probability distribution is usually considered to model a set of permutations and, in fact, is the core of the decision tree algorithm (LRT) proposed in [2].

To overcome the constraints regarding the topology of the network when dealing with different types of variables, in the preliminary version of this study, we proposed a mixturebased structure where the root is a hidden discrete variable. In [23], we based our proposal on a Naive Bayes graphical structure, where only univariate probability distributions are estimated for each state of the hidden variable. Learning and inference schemes were also designed in [23], based on the use of well-known Expectation-Maximization (EM) algorithm for parameter estimation and a combination of probabilistic inference with the Kemeny Ranking Problem (KRP) [24], respectively. Nonetheless, the proposed methods performed somewhat unevenly when dealing with the different datasets. With this more comprehensive paper, we successfully overcome the main weaknesses of our former proposal. Specifically, the main contributions of this study are as follows:

- After identifying early stopping as the main problem in our previous learning algorithm (Method A), we propose a new learning scheme (see Method B in Section 3) to search for the number of components in the mixture.
- For our Hidden Naive Bayes model, we explore discretization as an alternative to modeling numerical variables as Gaussian distributions.
- We extend the complexity of the naive Bayes-based structure model in order to allow interactions among the predictive attributes. In this new model, only numerical predictive attributes are allowed, and interactions are managed by using a multivariate Gaussian distribution.

- We perform an exhaustive experimental analysis over the standard benchmark for the label ranking problem.

The rest of the paper is structured as follows. In Section 2, we review some basic notions needed to deal with rank data. In Section 3, we formally describe the proposed Hidden Naive Bayes (HNB) as well as the algorithms to induce it from data and to carry out inference. Then, in Section 4, we extend our proposal to allow interactions between the (numerical) predictive attributes, by using a multivariate Gaussian mixture. In Section 5, we set out the empirical study conducted to evaluate the methods designed in this paper. In Section 6, we briefly comment on some limitations of the presented approach. Finally, in Section 7, we provide the conclusions and future research lines.

# 2. Background 

In this section, we review the background to our proposal. In particular, we briefly describe some permutation-based notions, such as the Kemeny Ranking Problem [24] and the Mallows probability distribution [22]. We also revise the Naive Bayes model [18] and the two competing methods to tackle the LR problem used in this study: the Label Ranking Trees and the Instance-Based Label Ranking algorithms [2].

### 2.1. Kemeny Ranking Problem

Let $\mathbb{S}_{m}$ be the set of permutations defined over $m$ elements $\{1, \ldots, m\}$. The Kemeny Ranking Problem (KRP) [24] consists in obtaining the consensus permutation (mode) $\pi_{0} \in \mathbb{S}_{m}$ that best represents a sample with $N$ permutations $\Pi=\left\{\pi_{1}, \ldots, \pi_{N}\right\}, \pi_{i} \in \mathbb{S}_{m}$.

Formally, the KRP looks for the consensus permutation $\pi_{0} \in \mathbb{S}_{m}$ that minimizes

$$
\pi_{0}=\underset{\pi_{i} \in \mathbb{S}_{m}}{\operatorname{argmin}} \sum_{i=1}^{N} D\left(\pi_{0}, \pi_{i}\right)
$$

where $D(\pi, \tau), \pi, \tau \in \mathbb{S}_{m}$ is a distance measure between two permutations $\pi$ and $\tau$. Normally, the Kendall distance [25] is used, which counts the number of pairwise disagreements between the two permutations, and the (greedy) Borda count algorithm [26] is employed to solve the KRP, because of its trade-off between efficiency and accuracy. The Borda count algorithm basically assigns $m$ points to the item ranked first, $m-1$ to the second one, and so on. Once all the input rankings have been computed, the items are sorted according to the number of accumulated points.

When not all rankings are equally important, a weight can be associated with each one to reflect its relevance. Then, a generalized version of the Borda method called weighted Borda count is used, which basically balances the points received by a permutation taking its weight into account.

### 2.2. Kendall Rank Correlation Coefficient

In our learning process (see Section 3.3), the Kendall rank correlation coefficient $\tau_{K}$ is used as goodness score [27]. Given the class variable $C$ with $\operatorname{dom}(C)=\left\{c_{1}, \ldots, c_{m}\right\}$ and permutations $\pi_{1}, \pi_{2}$ of the values in $\operatorname{dom}(C)$, the $\tau_{K}$ Kendall rank correlation coefficient is given by

$$
\tau_{K}\left(\pi_{1}, \pi_{2}\right)=\frac{\sum_{i=1}^{m} \sum_{j=1}^{m} \beta_{1}^{i j} \cdot \beta_{2}^{i j}}{m \cdot(m-1)}
$$

where

$$
\beta_{k}^{i j}= \begin{cases}1, & \text { if } c_{i} \succ_{\pi_{k}} c_{j} \\ -1, & \text { if } c_{j} \succ_{\pi_{k}} c_{i} \\ 0, & \text { if } i=j\end{cases}
$$

for $k=1,2$. Here, $c_{i} \succ_{\pi_{k}} c_{j}$ means that $c_{i}$ is ranked before $c_{j}$ in $\pi_{k}$.

The $\tau_{K}$ Kendall rank correlation coefficient lies in the range $[-1,1]$. In particular, $\tau_{K}\left(\pi_{1}, \pi_{2}\right)=1$ means a total positive correlation between $\pi_{1}$ and $\pi_{2}\left(\pi_{1}=\pi_{2}\right)$, whereas $\tau_{K}\left(\pi_{1}, \pi_{2}\right)=-1$ indicates a total negative correlation (actually this occurs when $\pi_{1}$ is the inverse of $\pi_{2}$ ). Values of $\tau_{K}$ close to 0 mean a poor correlation between the permutations.

# 2.3. Mallows Probability Distribution 

The Mallows probability distribution (also known as the Mallows model) [22] is an exponential probability distribution over permutations based on distances. The Mallows model, $\mathcal{M}\left(\pi_{0}, \theta\right)$, is parametrized by two parameters: the central permutation (mode) $\pi_{0} \in \mathbb{S}_{m}$ and the spread parameter (dispersion) $\theta \in[0,+\infty)$. Given a distance $D$ in $\mathbb{S}_{m}$, the probability assigned to a permutation $\pi \in \mathbb{S}_{m}$ by the Mallows distribution $\mathcal{M}\left(\pi_{0}, \theta\right)$ is

$$
P\left(\pi ; \pi_{0}, \theta\right)=\frac{e^{-\theta \cdot D\left(\pi, \pi_{0}\right)}}{\Psi(\theta)}
$$

where $\Psi(\theta)$ is a normalization constant. The spread parameter $\theta$ quantifies the concentration of the distribution around $\pi_{0}$. For $\theta=0$, a uniform distribution is obtained, while for $\theta=+\infty$ the model assigns a probability of 1 to $\pi_{0}$ and of 0 to the rest of the permutations. Both $\pi_{0}$ and $\theta$ can be estimated accurately in polynomial time [28]. For consensus permutation $\left(\pi_{0}\right)$, the Borda count is usually employed. For the spread $(\theta)$, there is no closed form, so numerical algorithms (e.g., Newton-Raphson) are normally used.

In this study, we take the Kendall distance as $D$, which is the usual choice in the literature [2,29].

### 2.4. Naive Bayes

Naive Bayes (NB) models are well-known probabilistic classifiers based on the strong independence hypothesis that, given the class variable, every pair of features is considered conditionally independent [30]. This assumption allows an efficient factorization of the join probability distribution (see Equation (1)) as well as efficient learning and inference procedures. Figure 1 shows the graphical structure of an NB model.
![img-0.jpeg](img-0.jpeg)

Figure 1. Naive Bayes model structure.
Like most probabilistic classifiers, NB models follow the maximum a posteriori (MAP) principle, that is, they return the most probable class label given the input instance as evidence. Formally, given an input instance $e_{t}=\left(x_{1, t}, \ldots, x_{n, t}\right) \in \operatorname{dom}\left(X_{1}\right) \times \cdots \times \operatorname{dom}\left(X_{n}\right)$ and being $C$ the class variable with $\operatorname{dom}(C)=\left\{c_{1}, \ldots, c_{m}\right\}$, a Naive Bayes Classifier $\mathcal{C}$ returns

$$
\mathcal{C}\left(e_{t}\right)=\underset{c \in \operatorname{dom}(C)}{\operatorname{argmax}} P\left(c \mid e_{t}\right)=\underset{c \in \operatorname{dom}(C)}{\operatorname{argmax}} P\left(e_{t}, c\right)=\underset{c \in \operatorname{dom}(C)}{\operatorname{argmax}} \prod_{i=1}^{n} P\left(x_{i, t} \mid c\right) \cdot P(c)
$$

according to Bayes' theorem and the conditional independence hypothesis, respectively. The above conditional distributions may be multinomial for discrete attributes and Gaussian for continuous attributes.

### 2.5. Instance-Based Label Ranking

The Instance-Based Label Ranking (IBLR) algorithm [2] is based on the nearest neighbors estimation principle. It takes, as input, an instance $e_{t}$ to be classified, a training dataset $\mathbf{D}$ with $N$ labeled instances and the number of nearest neighbors $k \in \mathbb{N}^{+}, k \leq N$, to

be considered. Using an appropriate distance, the IBLR algorithm then compares the input instance with all the $N$ training ones, obtains the $k$ nearest neighbors from $\mathbf{D}, \mathbf{R}=$ $\left\{\left(x_{1, j}, \ldots, x_{n, j}, \pi_{j}\right)\right\}_{j=1}^{k}$, and takes the rankings associated with these instances, $\mathbf{R}_{\mathrm{I} 1}=$ $\left\{\pi_{j}\right\}_{j=1}^{k}$. Then, the IBLR algorithm applies the Borda count algorithm to the permutations in $\mathbf{R}_{\mathrm{I} 1}$ and the obtained consensus permutation $\pi_{0}$ is returned as output.

The main advantage of instance-based learning is its local behavior, which allows it to locally estimate a different target function for each new instance to be classified instead of estimating a single target function for the entire instance space. On the other hand, its main disadvantage is its high computational cost in the inference stage, as it must compare the input instance against all the instances in the training dataset.

# 2.6. Label Ranking Trees 

Decision trees are usually constructed by recursively partitioning the dataset. The Label Ranking Trees (LRT) algorithm [2] receives, at each call, a set of instances $\mathbf{R}=$ $\left\{\left(x_{1, j}, \ldots, x_{k, j}, \pi_{j}\right)\right\}_{j=1}^{s}$ with $1 \leq k \leq n$ and $2 \leq s \leq N$, and must decide whether to stop the recursive call by creating a leaf node, or go on with the branching process by splitting the received training dataset $\mathbf{R}$ into several subsets according to the value of an attribute $X_{i}$.

The stopping and splitting criteria used in LRT are as follows:

- Stopping criterion. If we consider $\mathbf{R}_{\mathrm{I} 1}=\left\{\pi_{j}\right\}_{j=1}^{s}$ as the rankings associated with the instances in $\mathbf{R}$, the LRT algorithm stops the splitting process and creates a leaf node if either of the following two conditions hold:
- All the rankings are consistent. For all the pairs of class labels $c_{u}, c_{v} \in \operatorname{dom}(C)$, they maintain the same preference relation $\left(c_{u} \succ c_{v}\right.$ or $\left.c_{v} \succ c_{u}\right)$ through all the rankings in $\mathbf{R}_{\mathrm{I} 1}$ which rank both $c_{u}$ and $c_{v}$.
- $s<2 m$. This condition is introduced as a pre-pruning operation to prevent overfitting.

The leaf created is labeled with the consensus ranking $\pi_{0}$ obtained by applying the Borda count algorithm over the rankings in $\mathbf{R}_{\mathrm{I} 1}$.

- $\quad$ Splitting criterion. The LRT algorithm uses the spread parameter $\theta$ of the Mallows model (see Section 2.3) to measure the scattering of the rankings associated with a partition with respect to the consensus one. Formally, given an attribute $X_{i}$ with domain $\operatorname{dom}\left(X_{i}\right)=\left\{x_{1}, \ldots, x_{r_{i}}\right\}$, the uncertainty associated with a partition $\left\{R_{1}, R_{2}, \ldots, R_{r_{i}}\right\}$ of $\mathbf{R}$ is inversely proportional to

$$
f\left(X_{i}\right)=f\left(R_{1}, \ldots, R_{r_{i}}\right\})=\sum_{j=1}^{r_{i}} \frac{\left|R_{j}\right| \cdot \theta_{j}}{|\mathbf{R}|}
$$

where $\theta_{j}$ is the spread parameter estimated from the rankings of the instances in $R_{j}$, which can be computed by means of standard numerical optimization methods [2,29]. The LRT algorithm proceeds in a standard way, that is, sorting the values of the attributes $X_{i}$ in $\mathbf{R}$ and analyzing all the possible thresholds $\lambda$. Thus, it deals with the resulting two-state discrete attribute $X_{i}^{\lambda}$ with domain $\operatorname{dom}\left(X_{i}^{\lambda}\right)=\left\{X_{i} \leq \lambda, X_{i}>\lambda\right\}$, and selects the threshold $\lambda$ of the attribute $X_{i}$ that maximizes (2).
Then, an instance is classified by following the path from the root to the corresponding leaf, selecting, at each decision node, the branch corresponding to the value of the attribute in the instance to be classified. Thus, once a leaf node is reached, the permutation assigned to the leaf node is returned.

# 3. Hidden Naive Bayes for Label Ranking 

In this section, we propose an NB-based model to deal with the LR problem. We start by defining the proposed PGM structure and then describe the parameter estimation process and two different methods for training the model.

### 3.1. Model Definition

To overcome the constraints regarding the topology of the network when dealing with different types of variables, the model proposed here combines an NB structure with a hidden (latent) variable.

This idea is not new, and has been used, for instance, for unsupervised clustering [21,31], to improve the performance (accuracy) of the base classifier [32], relax some of the independence statements increasing the classifier modeling capability [33-35], or obtain models for efficient probabilistic inference [36].

In this paper, the introduction of the hidden variable stems from the need to model the join probability distribution involving variables of a different nature: discrete, continuous, and permutation-based.

In the proposed NB model graphical structure, the root element of the model is a discrete hidden variable, which we will denote as $H$, with $\operatorname{dom}(H)=\left\{h_{1}, \ldots, h_{r_{H}}\right\}, r_{H}$ being the total number of mixture models. The rest of the variables are observed variables. We consider two types of observed variables:

- The feature variables, observed both in the training and in the test phase. We consider two kinds: discrete variables, denoted as $X_{j}, j=1, \ldots, n_{J}$ and $\operatorname{dom}\left(X_{j}\right)=$ $\left\{x_{j_{1}}, \ldots, x_{j_{r_{j}}}\right\}$, and continuous variables, denoted as $Y_{k}, k=1, \ldots, n_{K}$.
- The ranking variable, denoted as $\pi$, which takes values in $\mathbb{S}_{m}$, this being the set of permutations defined over the class labels $\left\{c_{1}, \ldots, c_{m}\right\}$. This variable is used only during the training stage and is the target to be inferred.

Figure 2 shows a plate-based representation of the proposed model with the different types of variables described above $\left(n=n_{J}+n_{K}\right)$. The model assumes that each of these variable types follows a different conditional distribution given the root variable:

- Discrete variables follow a Multinomial distribution,

$$
P\left(X_{j} \mid H\right) \rightsquigarrow P\left(X_{j} \mid H=h_{z}\right) \sim \operatorname{Mult}\left(\left\{p\left(x_{j_{i}}^{h_{z}}\right)\right\}_{i=1}^{r_{j}}\right), \quad z=1, \ldots, r_{H}
$$

- Continuous variables follow a Normal or univariate Gaussian distribution,

$$
P\left(Y_{k} \mid H\right) \rightsquigarrow P\left(Y_{k} \mid H=h_{z}\right) \sim \mathcal{N}\left(\mu_{k}^{h_{z}}, \sigma_{k}^{h_{z}}\right), \quad z=1, \ldots, r_{H}
$$

- The ranking variable follows a Mallows distribution,

$$
P(\pi \mid H) \rightsquigarrow P\left(\pi \mid H=h_{z}\right) \sim \mathcal{M}\left(\pi_{0}^{h_{z}}, \theta^{h_{z}}\right), \quad z=1, \ldots, r_{H}
$$

- The hidden variable follows a Multinomial distribution,

$$
P(H) \sim \operatorname{Mult}\left(\left\{p\left(h_{z}\right)\right\}_{z=1}^{r_{H}}\right)
$$

![img-1.jpeg](img-1.jpeg)

Figure 2. The proposed HNB model.

The parameters for each of the conditional distributions need to be estimated to perform inference using the model.

# 3.2. Parameter Estimation 

As is common in most machine learning papers, we assume i.i.d. data. Furthermore, we also assume complete data, i.e., without missing values, both in the predictive and in the ranking variables. If there are missing values in the training data, they must be imputed previously to learn the model. The ranking variable can be imputed as described in [2]. Thus, we only deal with a hidden variable, $H$, and base our approach on the use of the Expectation-Maximization (EM) algorithm to estimate jointly the parameters of both the observed and hidden variables.

The EM algorithm [37] consists of two steps: the expectation step (E step), where the values for the hidden variable are estimated, and the maximization step ( $M$ step), where the parameters for the conditional distributions are obtained. Below, we describe these steps:

- E step: Under the assumption that the parameters of the model $\left\{\mu_{k}^{h_{z}}, \sigma_{k}^{h_{z}}, p\left(x_{j_{i}}^{h_{z}}\right), \pi_{0}^{h_{z}}\right.$, $\left.\theta^{h_{z}}, p\left(h_{z}\right)\right\} k=1, \ldots, n_{K}, j=1, \ldots, n_{I}, i=1, \ldots, r_{j}, z=1, \ldots, r_{H}$, are known, the probability of an example $e_{t}=\left(x_{1, t}, \ldots, x_{n_{I}, t}, y_{1, t}, \ldots, y_{n_{K}, t}, \pi_{t}\right)$ being in a mixture $h_{z}$ is

$$
\begin{aligned}
P\left(h_{z} \mid x_{1, t}, \ldots, x_{n_{I}, t}, y_{1, t}, \ldots, y_{n_{K}, t}, \pi_{t}\right) & =\frac{1}{C} \cdot P\left(h_{z}\right) \cdot P\left(x_{1, t}, \ldots, x_{n_{I}, t}, y_{1, t}, \ldots, y_{n_{K}, t}, \pi_{t} \mid h_{z}\right) \\
& =\frac{1}{C} \cdot P\left(h_{z}\right) \cdot P\left(\pi_{t} \mid h_{z}\right) \cdot \prod_{j=1}^{n_{t}} P\left(x_{j, t} \mid h_{z}\right) \cdot \prod_{k=1}^{n_{K}} P\left(y_{k, t} \mid h_{z}\right) \\
& =\frac{1}{C} p\left(h_{z}\right) \cdot \frac{e^{-\theta^{h_{z}} \cdot D\left(\pi_{t}, \sigma_{k}^{h_{z}}\right)}}{\Psi\left(\theta^{h_{z}}\right)} \cdot \prod_{j=1}^{n_{t}} p\left(x_{j, t}^{h_{z}}\right) \cdot \prod_{k=1}^{n_{K}} \frac{1}{\sigma_{k}^{h_{z}} \sqrt{2 \pi}} e^{-\frac{1}{2}\left(\frac{\pi_{t} e^{-\theta^{h_{z}}}}{e^{-}}\right)^{2}}
\end{aligned}
$$

Here, $C=\sum_{z=1}^{r_{H}} P\left(h_{z}\right) \cdot P\left(x_{1, t}, \ldots, x_{n_{I}, t}, y_{1, t}, \ldots, y_{n_{K}, t}, \pi_{t} \mid h_{z}\right)$ is the normalization constant.

- M step: Under the assumption that the probabilities of belonging to each mixture for all examples are known, the parameters of the model can be estimated as follows:
- Multinomial parameters for the discrete variables. Each multinomial parameter $p\left(x_{j_{i}}^{h_{z}}\right)$ is estimated by using MLE, where the count for each instance is weighted by the probability of $H=h_{z}$ given the instance.
- Gaussian distribution parameters for the continuous variables. The parameters $\mu_{k}^{h_{z}}$ and $\sigma_{k}^{h_{z}}$ of the Gaussian distribution are estimated through MLE for each $H=h z$, weighting each instance by the probability of it being in the mixture.
- Mallows distribution parameters for the ranking variable. For each component of the mixture $h_{z}$ of $H$, a Mallows distribution $\mathcal{M}\left(\pi_{0}^{h_{z}}, \theta^{h_{z}}\right)$ must be estimated (see Section 2.3). In particular, $\pi_{0}^{h_{z}}$ is computed by applying a weighted version of the Borda count algorithm (points assigned to items are weighted by the probability of $H=h_{z}$ given the instance), and $\theta^{h_{z}}$ is calculated by using the Newton-Raphson numerical optimization method.
- The mixture model probabilities $P(H)$ are computed according to the weights $P\left(h_{z} \mid e_{t}\right)$ for each mixture $h_{z}$ of $H$ (see Equation (3)) by means of MLE.

Stopping condition: The EM algorithm can easily accommodate different types of stop conditions, most of them based on checking the convergence of some score (logarithm likelihood, accuracy, etc.).

### 3.3. Learning Process

In addition to the graphical structure and the parameter estimation already described, we also need to determine some kind of structural learning in order to find the inner structure of $H$, that is, its cardinality or number of states.

Basically, we follow a greedy technique by initializing $r_{H}$ to a certain number and then running consecutive executions of the EM algorithm with an increasing number of mixtures.

There are several points to discuss regarding the learning process: the initial value for $r_{H}$, the value used to increment $r_{H}$ between two consecutive iterations, the way the components of the mixture are initialized, and how the goodness of the model is evaluated and the final value of $r_{H}$ is selected. Below, we describe the two proposed schemes.

# 3.3.1. Method A: HNBE-LR 

First, we describe the scheme proposed in the preliminary (conference) version of this study [23], based on the learning process used in [36] and which basically wraps the EM method for parameter estimation. In Algorithm 1, we show our adaptation from the NB estimation algorithm [31] to the LR problem. The main characteristics of this method are as follows:

- It is a wrapper method. Thus, the data received is divided into training $T r$ and validation $T v$ datasets, using the Kendall coefficient $\tau_{K}$ to assess the models and parameterizations explored during the search.
- The search for the number of components of the mixture is carried out greedily. We start with an initial number of components $z_{0}$ and a new component is added at each iteration. However, low probability components are pruned both during the search and during the EM-based parameter estimation. The search stops when the obtained model does not improve the best one in a given number of consecutive iterations. The improvement is assessed by evaluating the current parameterized model over the training dataset $T r$.
- Every time a new component is added to the mixture, the model parameters corresponding to this component are initialized from a set of instances of $T r$ obtained by using sampling with replacement.
- For each number of components in the mixture $r_{H}$ tried, an EM is run for parameter estimation. After each iteration ( E and M steps), the model is evaluated using the Kendall coefficient $\tau_{K}^{T r}$ for the training data $T r$. A threshold on the difference between this value and the previous one is used to check convergence.
- When the number of components changes (either because of pruning low probability ones or because of the addition of a new one), the component weights are properly rescaled.


### 3.3.2. Method B: HNB-LR

The results obtained in [23] shed light on certain drawbacks. The main one is that the algorithm reaches the stopping condition too soon, which results in a small number of components for the mixture. As the authors in [36] noted, in contrast to clustering (e.g., AutoClass [31]), a high number of mixture components is required to obtain an accurate approximation of the joint probability estimation.

Bearing this in mind, and also that the number of different values tried for $r_{H}$ must be small for reasons of efficiency, we propose an alternative scheme that we call Method $B$. As in Method A, the main idea is to wrap the EM algorithm by a search procedure to look for the number of components to be included in the mixture. In order to do that, we introduce important design modifications. Algorithms 2 and 3 show the scheme of this approach. Below, we comment on their main characteristics and differences with respect to Method A.

- In Method B, low probability components are not pruned, and so the EM algorithm is carried out in the search process (see Algorithm 2). Furthermore, the convergence of the EM algorithm is checked by using the log-likelihood ( $L L$ ) of the data ( $T r$ ) given the model, that is, no wrapper evaluation is carried out to compute $\tau_{K}$ inside EM.
- The search process works in a wrapper style. Thus, we divide the data received into a training $T r$ and validation $T v$ datasets, and use $\tau_{K}$ to assess the models explored during the search.

```
Algorithm 1: Method A: HNBE-LR
    Data: \(T\) : Training dataset; \(z_{0}\) : Initial \#of components; \(\beta\) : Maximum \#of iterations
        allowed without improvement; \(\alpha\) : Minimum required improvement for each
        EM iteration; \(p\) : \#of cycles to prune low-weight components of the model.
    Result: The HNBE-LR model fully specified.
    Create a holdout partition \(\{\operatorname{Tr}, T v\}\) from \(T ; \operatorname{Tr}=\left\{e_{t}\right\}_{t=1}^{\mid T r} ;\)
    \(r_{H} \leftarrow z_{0}\);
    Initialize the model with \(r_{H}\) mixture components and compute all the model
        parameters from a sample with replacement of \(\operatorname{Tr}\);
    It \(\leftarrow 0 ;\)
    \(\tau_{K}^{T r} \leftarrow-1 ;\)
    \(\tau_{K}^{T v} \leftarrow-1 ;\)
    while (It \(<\beta\) ) do
        // EM - Parameter estimation
        improving \(\leftarrow\) true;
        \(\tau_{K}^{c} \leftarrow-1 ;\)
        while improving do
            // E step
            Update \(P\left(h_{z} \mid e_{t}\right), z=1, \ldots, r_{H}\) and \(t=1, \ldots,|\operatorname{Tr}|\) using Equation (3);
            // M step
            Compute model parameters as described in Section 3.2 (M-step);
            Every \(p\) cycles, prune low-weight components of the model and update \(r_{H}\);
            \(\tau_{K} \leftarrow\) Evaluate the model over Tr dataset;
            if \(\left(\tau_{K}-\tau_{K}^{c}\right)<\alpha\) then
                improving \(\leftarrow\) False;
            else
                \(\tau_{K}^{c} \leftarrow \tau_{K} ;\)
            end
        end
    Prune low-weight components of the model and update \(r_{H}\);
    \(\tau_{K} \leftarrow\) Evaluate the model over Tv dataset;
    if \(\left(\tau_{K}>\tau_{K}^{T v}\right)\) then
        best \(\leftarrow\) model;
        \(\tau_{K}^{T v} \leftarrow \tau_{K} ;\)
    end
    \(\tau_{K}^{T r} \leftarrow\) Evaluate the model over Tr dataset;
    if \(\left(\tau_{K}>\tau_{K}^{T r}\right)\) then
        \(\tau_{K}^{T r} \leftarrow \tau_{K} ;\)
        It \(\leftarrow 0 ;\)
    else
        It \(\leftarrow I t+1 ;\)
    end
    // Adding a new mixture component
    Re-scale mixture component weights by a factor \(\frac{r_{H}}{r_{H}+1} ;\)
    Add a new mixture component to the model with weight \(\frac{1}{r_{H}+1}\) and compute
        its parameters from a sample with replacement of Tr ;
    end
    return best;
```

- The search for the number of components is carried out greedily, but we now split it into two phases. The first is a forward search, where we evaluate the model with $r_{H}=2^{1}, 2^{2}, 2^{4}, \ldots, 2^{10}$. We then select the best value $r_{H}^{\prime}$ according to $\tau_{K}^{T v}$ and run a binary search between $\frac{r_{H}^{\prime}}{2}$ and $r_{H}^{\prime}$. Finally, the best value $r_{H}^{*}$ found in the binary

search (see Section 5.2) according to $\tau_{K}^{T_{D}}$ is returned as the number of components for our model.
The intuition behind this greedy search is to be efficient (at most, 20 values are tested) and to quickly try large values for $r_{H}$, as we identified this point as a shortcoming of Method A.

- Each time a new value for $r_{H}$ is tried, the process starts from scratch, that is, all the components are initialized simultaneously, instead of being added to the model as in Algorithm 1. To initialize the component parameters (probabilities and weights), $k$-means clustering processes [38] with $k=r_{H}$ are run, and the better one according to the minimal sum of distances between points and clusters centroids is selected. The instances associated with each cluster are used to initialize the corresponding mixture component.

```
Algorithm 2: Method: EM
    Data: \(\operatorname{Tr}=\left\{e_{t}\right\}_{t=1}^{|T r|}\) : Training data set; \(r_{H}\) : \#of mixture components; \(\beta\) : Maximum
        \#of iterations; \(\alpha\) : Minimum required improvement for each EM iteration; \(\gamma\) :
        \#of k-means clustering algorithm restarts.
    Result: The HNB-LR model fully specified.
    Initialize the model with \(r_{H}\) mixture components by using the best of \(\gamma\) restarts of
        the k-means clustering algorithm with \(k=r_{H}\);
    \(L L_{c} \leftarrow-\infty\);
    for \(i \leftarrow 0\) to \(\beta\) do
        // E step
        Update \(P\left(h_{z} \mid e_{t}\right), z=1, \ldots, r_{H}\) and \(t=1, \ldots,|\operatorname{Tr}|\) using Equation (3);
        // M step
        Compute model parameters as described in Section 3.2 (M-step);
        Compute \(L L\) for \(\operatorname{Tr}\) given the current model;
        if \(\left(L L-L L_{c}<\alpha\right)\) then
            // Early stopping because of convergence
            break;
        end
    end
    return model;
```


# 3.4. Inference Process 

In the inference process, the method needs to predict the ranking associated with a given instance $e_{t}$. In our proposal, the probability of a ranking $\pi_{s}$ given $e_{t}$ can be obtained by marginalizing out variables until we obtain an expression for the posterior probability

$$
P\left(\pi_{s} \mid e_{t}\right) \propto \sum_{z=1}^{r_{H}}\left(P\left(h_{z}\right) \cdot P\left(\pi_{s} \mid h_{z}\right) \cdot \prod_{j=1}^{n_{j}} P\left(x_{j, t} \mid h_{z}\right) \cdot \prod_{k=1}^{n_{k}} P\left(y_{k, t} \mid h_{z}\right)\right)
$$

The outcome can then be obtained by using the MAP principle, that is, choosing the ranking $\pi^{*}$ which maximizes the score

$$
\pi^{*}=\underset{\pi_{s} \in \mathbb{S}_{m}}{\operatorname{argmax}} P\left(\pi_{s} \mid e_{t}\right)
$$

However, due to the possible high cardinality of $\mathbb{S}_{m}$, we propose an approximate method:

1. Compute the probability a posteriori of each component of the mixture given the instance $e_{t}$ :

$$
P\left(h_{z} \mid e_{t}\right) \propto \prod_{j=1}^{n_{1}} P\left(x_{j, t} \mid h_{z}\right) \cdot \prod_{k=1}^{n_{k}} P\left(y_{k, t} \mid h_{z}\right)
$$

```
Algorithm 3: Method B: HNB-LR
    Data: \(T\) : Training dataset; \(\beta\) : Maximum \#of EM iterations; \(\alpha\) : Minimum required
        improvement for each EM iteration; \(\gamma\) : \#of k-means clustering algorithm
        restarts.
    Result: The HNB-LR model fully specified.
    Create a holdout partition \(\{\operatorname{Tr}, T v\}\) from \(T ; \operatorname{Tr}=\left\{e_{t}\right\}_{t=1}^{\mid T r}\);
    \(T_{K}^{T v} \leftarrow-1\);
    \(r_{H} \leftarrow 0\);
    // Forward search
    for \(i \leftarrow 1\) to 10 do
        model \(\leftarrow \operatorname{EM}\left(\operatorname{Tr}, 2^{i}, \alpha, \gamma\right)\);
        \(\tau_{K} \leftarrow\) Evaluate the model over \(T v\) dataset;
        if \(\left(\tau_{K}>\tau_{K}^{T v}\right)\) then
            \(r^{H} \leftarrow 2^{i}\);
        end
    end
    // Binary search
    \(r_{H} \leftarrow\) Get the best number of components by using a binary search in range \(\left[\frac{r_{H}}{2}\right.\)
        \(\left.r_{H}\right]\) with EM to learn the model and \(\tau_{K}\) over \(T v\) to evaluate;
    best \(\leftarrow \operatorname{EM}\left(T, r_{H}, \alpha, \gamma\right)\);
    return best;
```

2. Solve a generalized aggregation problem by using the weighted Borda count over the set of weighted rankings $\left\{\left(\pi_{0}^{h_{1}}, w_{1}\right), \ldots,\left(\pi_{0}^{h_{r_{H}}}, w_{r_{H}}\right)\right\}$, that is, the consensus rankings associated with the components of the mixture, and taking as weight $w_{z}$, the probability a posteriori computed for the mixture component $P\left(h_{z} \mid e_{t}\right)$.

# 4. Gaussian Mixture-Based Semi-Naive Bayes for Label Ranking 

In this section, we go one step further by allowing interactions between the predictive variables. However, in order to maintain the complexity of the learning process under control, we decided to use a model in which, apart from identifying the number of mixture components, no structural learning is needed. Our proposal falls in the so-called Semi-Naive Bayes approach [30,39], and we restrict our study to continuous predictive variables. This constraint is quite natural in the LR problem, as all the benchmark datasets contain only continuous variables. In the future, we plan to adapt our method to also allow discrete predictive attributes, which, in general, means learning constrained graphical structures by limiting the number of dependencies allowed [30] or even dealing with hybrid Bayesian networks [40]. Learning PGMs with hidden variables is not an easy task, but there are several approaches in the literature, most based on the use of the Structural EM (SEM) algorithm [41].

### 4.1. Model Definition

Once we limit our model to contain only continuous predictive attributes $Y_{1}, \ldots, Y_{n_{K}}$, $\pi$, and $H$, and also avoid structural learning apart from $n_{H}$, we have to deal with representing the interactions between the variables. We maintain the interaction between $\pi$ and the predictive variables to be channeled through the hidden variable $H$. Thus, explicit interactions are only allowed between the continuous attributes. As no structural learning of these relations is desired, we decided to model them by using a multivariate Gaussian distribution, $\mathcal{M} \mathcal{N}(\vec{\mu}, \Sigma)$. This has the advantage of having to estimate only $n_{K}{ }^{2}+n_{K}$ parameters, as $n_{K}$ are the values in the vector of means $\vec{\mu}$ and $n_{K}{ }^{2}$ in the covariance matrix.

In the literature, a Gaussian Mixture Model (GMM) [42] is a parametric probability density function represented as a weighted sum of Gaussian component densities, where each component density is a multivariate Gaussian function. Therefore, we take advantage

of the widely used GMM to plug them into our PGM to deal with the LR problem. In the literature, we can find several variants of the GMM, which differ in the way the covariance matrix is constrained or not constrained. In particular, the standard or full GMM estimates a covariance matrix for each component with no additional constraint. On the other hand, in the diag variant, such a covariance matrix is constrained to be diagonal, which is equivalent to the NB assumption. The third option is to use a tied covariance matrix, which means estimating an unconstrained covariance matrix, but using it for all the components.

Figure 3 shows the graphical representation of the proposed semi-naive Bayes (SNB) model, where the large node including all the continuous attributes emphasizes the idea of modeling them jointly. The difference regarding the HNB presented in Section 3 is that the continuous variables now follow a multivariate Gaussian distribution given the root variable

$$
P(Y \mid H) \rightsquigarrow P\left(Y \mid H=h_{z}\right) \sim \mathcal{M} \mathcal{N}\left(\vec{\mu}^{h_{z}}, \Sigma^{h_{z}}\right), \quad z=1, \ldots, r_{H}
$$

where $Y$ is the set of continuous variables $\left\{Y_{1}, \ldots, Y_{n_{K}}\right\}, \vec{\mu}$ is the vector of means for $Y_{1}, \ldots, Y_{n_{K}}$, and $\Sigma$ is the $n_{K} \times n_{K}$ covariance matrix.
![img-2.jpeg](img-2.jpeg)

Figure 3. The proposed GMSNB model.

# 4.2. Parameter Estimation 

As in the case of the proposed HNB algorithm, we use the EM algorithm to estimate the model parameters. Next, we point out the differences between this method and the univariate case (see Section 3.2).

- E step: Under the assumption that the parameters of the model $\left\{\vec{\mu}^{h_{z}}, \Sigma^{h_{z}}, \pi_{0}^{h_{z}}, \theta^{h_{z}}\right.$, $\left.p\left(h_{z}\right)\right\}, z=1, \ldots, r_{H}$, are known, the probability of an example $e_{t}=\left(y_{1, t}, \ldots, y_{n_{K}, t}, \pi_{t}\right)=$ $\left(\vec{y}_{t}, \pi_{t}\right)$ being in a mixture $h_{z}$ is

$$
\begin{aligned}
P\left(h_{z} \mid \vec{y}_{t}, \pi_{t}\right) & =\frac{1}{C} \cdot P\left(h_{z}\right) \cdot P\left(\vec{y}_{t}, \pi_{t} \mid h_{z}\right) \\
& =\frac{1}{C} \cdot P\left(h_{z}\right) \cdot P\left(\pi_{t} \mid h_{z}\right) \cdot P\left(\vec{y}_{t} \mid h_{z}\right) \\
& =\frac{1}{C} \cdot P\left(h_{z}\right) \cdot \mathcal{M}\left(\pi_{t}: \pi_{0}^{h_{z}}, \theta^{h_{z}}\right) \cdot \mathcal{M} \mathcal{N}\left(\vec{y}_{t}: \vec{\mu}^{h_{z}}, \Sigma^{h_{z}}\right)
\end{aligned}
$$

where $C=\sum_{z=1}^{r_{H}} P\left(h_{z}\right) P\left(\vec{y}_{t}, \pi_{t} \mid h_{z}\right)$ is the normalization constant and $\mathcal{M} \mathcal{N}\left(\vec{y}_{t}: \vec{\mu}^{h_{z}}, \Sigma^{h_{z}}\right)$ stands for the probability density function of the multinormal distribution with parameters $\vec{\mu}^{h_{z}}$ and $\Sigma^{h_{z}}$ given by

$$
\mathcal{M} \mathcal{N}\left(\vec{y}: \vec{\mu}^{h_{z}}, \Sigma^{h_{z}}\right)=\frac{1}{\sqrt{(2 \pi)^{n_{K}}|\Sigma|^{h_{z}}}} e^{-\frac{1}{2}\left(\vec{y}-\vec{\mu}^{h_{z}}\right)^{T}\left(\Sigma^{h_{z}}\right)^{-1}\left(\vec{y}-\vec{\mu}^{h_{z}}\right)}
$$

Here, $\vec{y}$ is a configuration of values for variables $\left(Y_{1}, \ldots, Y_{n_{K}}\right),|\Sigma|$ is the determinant of $\Sigma$, and -1 and $T$ denote the inverse and transpose matrix operators, respectively.

- M step: Under the assumption that the probabilities of belonging to each mixture for all the examples are known, the parameters of the model can be estimated as follows:

- Continuous variables. Empirical means and covariance matrices are calculated in the standard way, using each instance being weighted by $w_{t}^{h_{z}}=P\left(h_{z} \mid \vec{y}_{t}, \pi_{t}\right)$ according to the expressions

$$
\begin{gathered}
N^{h_{z}}=\sum_{t=1}^{N} w_{t}^{h_{z}} \\
\vec{\mu}^{h_{z}}=\frac{1}{N^{h_{z}}} \sum_{t=1}^{N} w_{t}^{h_{z}} \cdot \vec{y}_{t} \\
\Sigma^{h_{z}}=\frac{1}{N^{h_{z}}} \sum_{t=1}^{N} w_{t}^{h_{z}} \cdot\left(\vec{y}_{t}-\vec{\mu}^{h_{z}}\right) \times\left(\vec{y}_{t}-\vec{\mu}^{h_{z}}\right)^{T}
\end{gathered}
$$

Here, $\times$ stands for the usual matrix product.
In the tied case, where all the components share the same covariance matrix, $\Sigma$, it is estimated as [43] (p. 71):

$$
\Sigma=\frac{1}{N} \sum_{z=1}^{r_{H}} \sum_{t=1}^{N} w_{t}^{h_{z}} \cdot\left(\vec{y}_{t}-\vec{\mu}^{h_{z}}\right) \times\left(\vec{y}_{t}-\vec{\mu}^{h_{z}}\right)^{T}
$$

# 4.3. Learning Process 

Method B, described in Section 3.3, is used to estimate the number of components for the mixture $H$. To do so, Algorithm 2 is modified as follows:

- In the E step, Equation (5) is used instead of Equation (3).
- In the M step, the expressions in Section 4.2 are used instead of the respective ones in Section 3.2.


### 4.4. Inference Process

The same inference process is used as in the HNB model (see Section 3.4). The only difference is that we now compute the posterior probability of each component of the mixture given the instance $e_{t}$ by using the multivariate probability density function instead of Equation (4).

$$
P\left(h_{z} \mid e_{t}\right)=P\left(h_{z} \mid \vec{y}_{t}\right) \propto \frac{1}{\sqrt{(2 \pi)^{n_{K}}\left|\Sigma^{h_{z}}\right|}} e^{-\frac{1}{2}\left(\vec{y}-\vec{\mu}^{h_{z}}\right)^{T}\left(\Sigma^{h_{z}}\right)^{-1}\left(\vec{y}-\vec{\mu}^{h_{z}}\right)}
$$

## 5. Experimental Evaluation

In this section, we assess the mixture-based algorithms proposed to solve the LR problem. Below, we detail the datasets used, the algorithms tested, the methodology adopted, and the results obtained.

### 5.1. Datasets

Table 1 shows the main characteristics of the 21 datasets widely used as benchmark for the LR problem. The first 16 datasets were turned from multi-class (Type A) and regression (Type B) problems into the LR problem [2], while the last 5 datasets (Type R) correspond to real-world biological problems [10]. The columns \#rankings and max \#rankings represent the actual number of different rankings in the dataset and the maximum number of different rankings according to the number of classes (\#classes), respectively. In the 21 datasets considered, all the predictive attributes (features) are continuous variables. A more detailed description of the datasets is provided at: https:// scikit-fr.readthedocs.io/en/latest/user_ guide/datasets.html\#datasets (accessed on 29 March 2021).

# 5.2. Algorithms 

In this study, we considered the following algorithms:

- The IBLR algorithm introduced in [2] (see Section 2.5). To identify the nearest neighbors, the Euclidean distance was used. To compute the prediction, the permutations associated with the $k$-nearest neighbors were weighted according to the neighbor's (inverse) distance to the input instance. Although the IBLR algorithm belongs to the lazy paradigm of machine learning, we carried out model learning to select the number $k$ of nearest neighbors. We applied the following process using a fivefold cross-validation method ( $5-\mathrm{cv}$ ) over the training dataset to assess the goodness of each candidate value:

1. We started with $k=5$ and doubled it while the score was improving. From this process, we obtained $k_{l}$ and $k_{r}$, that is, the number of nearest neighbors leading to the best score (the penultimate value tested) and the one stopping the iterative process (the last value tested), respectively.
2. We applied a binary search in the range $\left[k_{l}, k_{r}\right]$. In this process, we took $k_{m}=$ $\left\lfloor\frac{k_{l}+k_{r}}{2}\right\rfloor$, and if the score improved for $k_{m}$ with respect to $k_{l}$, we then repeated this recursive process using the range $\left[k_{m}, k_{r}\right]$. Otherwise, the range $\left[k_{l}, k_{m}\right]$ was used.
We kept the number of nearest neighbors that led to the best score.

- The LRT algorithm introduced in [2] (see Section 2.6).
- The HNBE-LR algorithm introduced in [23] (see Section 3.3.1). Note that all the attributes of the datasets are continuous variables. Thus, the parameters of the model were estimated by means of Gaussian distribution parameters (HNBE-LR-G). The hyperparameter values were $z_{0}=5, \beta=1, \alpha=0.001, p=5$. The holdout for the training and validation datasets was $75 \% / 25 \%$.
- The HNB-LR algorithm (see Section 3.3.2). As in the previous case, we estimated the conditional probability distributions with Gaussian univariate distributions (HNB-LRG). Furthermore, we binned the continuous variables using equal-frequency (HNB-LR-F), equal-width (HNB-LR-W), and entropy-based [44] (HNB-LR-E) discretization techniques, estimating the parameters of the model with Multinomial distribution parameters. The number of bins was set to 5 for equal-width and equal-frequency cases. The holdout for the training and validation datasets was $80 \% / 20 \%$. The $\gamma$ value was fixed to 10 .
- The GMSNB-LR algorithm (see Section 4), with a different covariance matrix for each component, full approach (GMSNB-LR-F), and sharing the same covariance matrix between all the components of the mixture, tied approach (GMSNB-LR-T). The holdout for the training and validation datasets was $80 \% / 20 \%$. The $\gamma$ value was fixed to 10 .

Table 1. Description of the datasets.


# 5.3. Methodology 

We adopted the following design decisions:

- We used five repetitions of a tenfold cross-validation method $(5 \times 10-\mathrm{cv})$ to assess the algorithms.
- We used the Kendall rank correlation coefficient $\tau_{K}$ as goodness score: the higher, the better (see Section 2.2).
- To properly analyze the results, we carried out the standard statistical analysis procedure for machine learning [45,46], using the exreport tool [47]. The procedure is divided into two steps:

1. First, we carried out a Friedman test [48] with significance level $\alpha=0.05$. If the obtained $p$-value $\leq \alpha$, then we rejected the null hypothesis $H_{0}$ and concluded that at least one algorithm is not equivalent to the rest.
2. Second, once the previous step rejected $H_{0}$, we applied a post hoc test using the Holm's procedure [49] to discover the outstanding algorithms. This test compares all the algorithms against the control algorithm, that is, the one ranked first by the Friedman test.

- We executed the experiments on computers running the CentOS Linux 7 operating system with an Intel(R) Xeon(R) E5-2630 CPU running at 2.40 GHz , and with 16 GB of RAM memory.


### 5.4. Results

In this section, we present and analyze the results obtained. We focus on accuracy ( $\tau_{K}$ score) and CPU time.

### 5.4.1. Accuracy

First, we analyze the results obtained by the HNB-LR algorithms. The $\tau_{K}$ accuracy results for this family of algorithms are shown in Table 2. The cells contain the average and standard deviation over the test sets of the cross validation method for the rank correlation coefficient $\tau_{K}$ between the real and predicted permutations. The boldfaced values correspond to the algorithm(s) achieving the best mean accuracy for each dataset.

Table 2. Mean accuracy for each HNB-LR algorithm.


We base our analysis on the statistical procedure described in Section 5.3:

1. The $p$-value obtained in the Friedman test was $3.613 \times 10^{-5}$ ). Therefore, the null hypothesis $\left(H_{0}\right)$ was rejected, and at least one of the tested algorithms was different.
2. Table 3 shows the results for the post hoc test by taking HNB-LR-G, the algorithm ranked first by the Friedman test, as the control. The columns rank and $p$-value represent the ranking obtained by the Friedman test and the $p$-value adjusted by Holm's procedure, respectively. The columns win, tie, and loss contain the number of times that the control algorithm wins, ties, and loses with respect to the row-wise algorithm. The $p$-values for the non-rejected null hypothesis are boldfaced.

Table 3. Results of the post hoc test for the mean accuracy of HNB-LR algorithms.


According to these results and the statistical analysis performed, we can conclude the following.

- The HNBE-LR-G algorithm is the worst method. The reason is obvious if we analyze Table 4, where we show the number of components (on average) selected for each algorithm. It is clear that this number is too small for HNBE-LR-G, which clearly suffers from premature early stopping. Furthermore, we must recall that this algorithm is the only one which prunes low weight components during its performance. As a consequence, HNBE-LR-G does not obtain a good probability estimation.
- The HNB-LR-G algorithm is ranked first and is statistically different to the HNB-LR-W and HNBE-G algorithms. In the case of HNB-LR-W, the reason is not the number of

selected components, but the equal-width discretization carried out, which produces poor binning in comparison, for example, with the supervised entropy-based method.

- Although the HNB-LR-G algorithm is ranked first, the post hoc test reveals no significant difference with respect to the HNB-LR-E and HNB-LR-F algorithms. This opens the door to future research on more complex Bayesian network structures.
- As stated in [36], a large number of components are required to obtain a good probability estimation and, in our problem, a good ranking prediction.
Once we have determined that the best HNB-LR algorithms are HNB-LR-G, HNB-LR-E, and HNB-LR-F, we introduce the two algorithms allowing interactions among the predictive attributes in the study, that is, those based on the use of the multivariate Gaussian distribution to jointly model the (numerical) attributes: GMSNB-LR-F and GMSNB-LR-T. The results are shown in the two leftmost columns of Table 5. To complete the comparison, we also show the results for the two state-of-the-art LR classifiers [2] described in Sections 2.5 and 2.6.

Again, we applied the statistical analysis procedure described in Section 5.3, including also the three HNB-LR algorithms selected from the previous study:

1. The $p$-value obtained for the Friedman test was $2.503 \times 10^{-7}$. Therefore, we rejected the null hypothesis $\left(H_{0}\right)$, i.e., at least one algorithm is different to the rest.
2. As IBLR is ranked first by the Friedman test, we took it as the control and performed a post hoc test using Holm's procedure. Table 6 shows the results for the post hoc test.
Considering these results, we can conclude the following.

- The IBLR algorithm is ranked first, being statistically different to all the tested algorithms except GMSNB-LR-T. Note that IBLR is a fine-tuned algorithm, as can be observed from the number of neighbors selected for each dataset (see Table 4), which are far from standard values $(3,5, \ldots)$.
- The GMSNB-LR-T algorithm has a remarkable performance, being non-significantly different to IBLR. This is a very important finding because, as recognized in the literature, the instance-based algorithm generally outperforms the model-based algorithms, being necessary to use ensembles of the LRT algorithm to compete with it [14].
- The GMSNB-LR-T algorithm also has in its favor that it is able to cope with all the tested datasets, while the experiments for IBLR cannot finish in a maximum of 168 h (one week) for fried dataset (notice the empty cell in Table 5). As can be observed, fried is the largest dataset in our experiments, which reveals the disadvantage of using IBLR for larger domains.
- The GMSNB-LR-T algorithm behaves better than GMSNB-LR-F, which is also ranked behind HNB-LR-G. Two explanations are plausible for this behavior: First, the amount of data considered is limited, so it can be scarce for the estimation of many covariance matrices when the number of components grows. Second, it is well known that increasing the number of components can be enough to model the correlations between the features. In fact, if we observe Table 4, we realize that the numbers of components selected for GMSNB-LR-T and HNB-LR-G are noticeably greater than that selected for GMSNB-LR-F.

Table 4. Mean number of components for each mixture-based algorithm and mean number of nearest neighbors for the IBLR algorithm.


Table 5. Mean accuracy for the GMSNB-LR, IBLR, and LRT algorithms.


Table 6. Results of the post hoc test for the mean accuracy of the algorithms.


# 5.4.2. Time 

In this study, we consider model-based and instance-based machine learning algorithms, which clearly distribute the CPU time for the learning and inference steps differently. Although the CPU time for the whole process (learning from the training dataset and validating with test dataset) is generally reported, we separate the CPU time for the learning and inference steps because (i) a model is learnt once but queried many times and (ii) most real-world applications require online predictions but allow for offline fitting. Tables 7 and 8 show the average CPU time for the learning and inference steps. In light of these results, we can conclude the following.

- The HNBE-LR-G algorithm is the fastest method during the learning step because it suffers from premature early stopping, which gives rise to a fast but poor algorithm. On the other hand, the LRT algorithm is the fastest method during the inference step, which is a common situation for tree-based algorithms.
- The IBLR algorithm is faster than the HNB-LR and GMSNB-LR algorithms in the learning step. However, during inference, the IBLR algorithm computes the distance between the input instance and the instances in the training dataset, which clearly increases the CPU time required by the algorithm.
- The GMSNB-LR-F algorithm is generally faster than the GMSNB-LR-T algorithm, both in learning and inference. This is due to the number of components selected by the GMSNB-LR-F algorithm in comparison to the GMSNB-LR-T algorithm. In a similar way, the HNB-LR-G algorithm is faster than the HNB-LR-F, HNB-LR-W, and HNB-LR-E algorithms, as the the latter ones apply a discretization procedure prior to the learning and inference steps.

Table 7. Mean CPU time (in seconds) for the learning step of each algorithm.


Table 8. Mean CPU time (in seconds) for the inference step of each algorithm.


# 6. Limitations 

As observed in the previous section, allowing interactions between the predictive variables represents a crucial issue with respect to the univariate case. Actually, our mixturebased model emerges as competitive with IBLR. However, there are still some weaknesses in our study/proposal:

- The CPU time data shown in Table 7 suggest that our method does not scale as would be desirable. In fact, it seems that the number of instances has a greater influence on the CPU time than the number of variables. However, more analysis is needed to clarify this point. Feature subset selection and stratification could lead to scalability improvements.
- Interactions between the predictive variables are limited to the numerical ones. Allowing interactions among the discrete variables and also mixed interactions should be studied. The literature on Bayesian network classifiers [30,39] and hybrid Bayesian networks may help in this task [50].
- Currently, the method only works with complete rankings. Nevertheless, in real-world applications it is usual to allow the agent to rank only certain labels. We think our techniques can be adapted to deal with incomplete rankings.


## 7. Conclusions

This study explores the use of mixture-based algorithms to solve the LR problem. The main problem is to model the target variable, as it takes values in the set of permutations defined over the class variable. We solve this shortcoming by introducing a hidden variable as root, so all the variables can be modeled by using conditional distributions. In particular, we base our approach on the Naive Bayes structure, with the hidden variable being the root of the model. We then go a step further by allowing interactions between the (numerical) predictive variables, thus designing a Semi-Naive Bayes model. Learning algorithms based on the well-known EM estimation principle are proposed for both cases. The inference is designed as a combination of probabilistic inference and rank aggregation.

From the experimental evaluation, we observe that the Naive Bayes approach is comparable in score to the decision trees for the LR problem, while the Semi-Naive Bayes approach (in particular, the one sharing a single covariance matrix among all the components) outperforms the Naive Bayes and decision tree-based algorithms, being also competitive with the state-of-the-art model-free algorithm based on the nearest neighbors method (IBLR). The good performance of this algorithm (GMSNB-LR-T) with respect to IBLR is reinforced by its better behavior at the inference stage, where IBLR needs a great amount of time when facing large datasets.

As future research, we propose two possible extensions to this work: First, we plan to extend our approach to cope with incomplete data in the ranking variable, that is, cases in which not all the labels are ranked in the instances of the training set. In the literature, this step is solved by completing those rankings before learning the model. However, we think this step can be introduced in the EM algorithm. In fact, model-based algorithms have shown better behavior than model-free ones when learning from incomplete rankings, so open the door to future promising research. Second, we plan to extend the mixture-based algorithms to the LR problems whose target ranking is a partial or bucket order, that is, a ranking in which some labels can be tied. This problem, which is generally termed the Partial Label Ranking (PLR) problem [51,52], introduces new challenges, such as the infeasibility of using the Mallows distribution to model the target variable.

Author Contributions: Conceptualization, E.G.R., J.C.A., J.A.A., and J.A.G.; Formal analysis, E.G.R., J.C.A., J.A.A., and J.A.G.; Funding acquisition, J.A.G.; Investigation, E.G.R., J.C.A., J.A.A., and J.A.G.; Methodology, E.G.R., J.C.A., J.A.A., and J.A.G.; Software, E.G.R., and J.C.A.; Supervision, J.A.A. and J.A.G.; Validation, E.G.R., J.C.A., J.A.A., and J.A.G.; Writing—original draft, E.G.R., J.C.A., J.A.A., and J.A.G.; Writing-review and editing, E.G.R., J.C.A., J.A.A., and J.A.G.. All authors have read and agreed to the published version of the manuscript.

Funding: This study has been partially funded by the Spanish Government, FEDER funds and the JCCM through the projects PID2019-106758GB-C33/AEI/10.13039/501100011033, TIN2016-77902-C3-1-P, and SBPLY/17/180501/000493. Juan C. Alfaro has also been funded by the FPU scholarship FPU18/00181 by MCIU.

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: The running examples of the paper together with other basic models are available at: https://github.com/alfaro96/scikit-lr (accessed on 30 March 2021) .

Conflicts of Interest: The authors declare no conflict of interest.
