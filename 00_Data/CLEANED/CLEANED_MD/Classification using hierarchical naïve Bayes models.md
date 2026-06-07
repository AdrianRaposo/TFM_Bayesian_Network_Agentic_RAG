# Classification using Hierarchical Naïve Bayes models 

Helge Langseth $\cdot$ Thomas D. Nielsen

Received: 1 July 2004 / Revised: 9 November 2005 / Accepted: 9 November 2005 /
Published online: 3 March 2006
Springer Science + Business Media, LLC 2006


#### Abstract

Classification problems have a long history in the machine learning literature. One of the simplest, and yet most consistently well-performing set of classifiers is the Naïve Bayes models. However, an inherent problem with these classifiers is the assumption that all attributes used to describe an instance are conditionally independent given the class of that instance. When this assumption is violated (which is often the case in practice) it can reduce classification accuracy due to "information double-counting" and interaction omission.

In this paper we focus on a relatively new set of models, termed Hierarchical Naïve Bayes models. Hierarchical Naïve Bayes models extend the modeling flexibility of Naïve Bayes models by introducing latent variables to relax some of the independence statements in these models. We propose a simple algorithm for learning Hierarchical Naïve Bayes models in the context of classification. Experimental results show that the learned models can significantly improve classification accuracy as compared to other frameworks.


Keywords Classification $\cdot$ Naïve Bayes models $\cdot$ Hierarchical models

## 1. Introduction

Classification is the task of predicting the class of an instance from a set of attributes describing that instance, i.e., to apply a mapping from the attribute space into a predefined

Editor: Peter Flach
H. Langseth ( $\square$ )

Department of Mathematical Sciences, Norwegian University of Science and Technology, N-7491, Trondheim, Norway
e-mail: helgel@math.ntnu.no
Present address: SINTEF Technology and Society, N-7465 Trondheim, Norway, email: helge.langseth@sintef.no
T. D. Nielsen

Department of Computer Science, Aalborg University, Fredrik Bajers Vej 7E, DK-9220, Aalborg ø, Denmark
e-mail: tdn@cs.auc.dk

set of classes. When learning a classifier we seek to generate such a mapping based on a database of labeled instances. Classifier learning, which has been an active research field over the last decades, can therefore be seen as a model selection process where the task is to find a single model, from some set of models, with the highest classification accuracy. The set of Naïve Bayes (NB) models (Duda \& Hart, 1973) is a family of particularly simple models which has shown to offer very good classification accuracy. NB models assume that all attributes are conditionally independent given the class. However, this assumption is clearly violated in many real-world problems; in such situations overlapping information may be given an unwarranted weight by the classifier (the information related to dependent attributes is treated as coming from independent sources). To resolve this problem, methods for handling the conditional dependence between the attributes have become a lively research area; these methods are typically grouped into three categories: Feature selection (Kohavi \& John, 1997), feature grouping (Kononenko, 1991; Pazzani, 1996a), and correlation modeling (Friedman et al., 1997).

The approach taken in this paper is based on correlation modeling using Hierarchical Naïve Bayes (HNB) models (Zhang, 2004b; Zhang et al., 2003), see also Langley (1993), Spirtes et al. (1993), Martin and VanLehn (1994), and Pazzani (1996b). HNBs are treeshaped Bayesian networks, with latent variables between the class node (the root of the tree) and the attributes (the leaves), see Fig. 1. The latent variables are introduced to relax some of the independence statements of the NB classifier. For example, in the HNB model shown in Fig. 1, the attributes $A_{1}$ and $A_{2}$ are not independent given $C$ because the latent variable $L_{1}$ is unobserved. Note that if there are no latent variables in the HNB, it reduces to an NB model.

The idea to use HNBs for classification was first explored by Zhang et al. (2003). However, they did not focus on classification accuracy, but rather on the generation of interesting latent structures. In particular, Zhang et al. (2003) search for the model maximizing the BIC score (a form of penalized log likelihood (Schwarz, 1978)), and such a global score function is not necessarily suitable for learning a classifier.

In this paper we focus on learning HNBs for classification: We propose a computationally efficient learning algorithm that is significantly more accurate than the system by Zhang et al. (2003) as well as several other state-of-the-art classifiers. The proposed algorithm endows the latent variables (including their state spaces) with an explicit semantics, which may allow the decision maker to inspect the rules that governs the classification of a particular instance; informally, a latent variable can be seen as aggregating the information from its children which is relevant for classification.

The remainder of this paper is organized as follows: In Section 2 we give a brief overview of some approaches to Bayesian classification, followed by an introduction to HNB models

Fig. 1 An HNB designed for classification. The class attribute $C$ is the root, and the attributes $\mathcal{A}=\left\{A_{1}, \ldots, A_{7}\right\}$ are leaf nodes. $L_{1}, L_{2}$ and $L_{3}$ are latent variables
![img-0.jpeg](img-0.jpeg)

in Section 3. In Section 4 we present an algorithm for learning HNB classifiers from data, and Section 5 is devoted to empirical results. Finally we make some concluding remarks in Section 6.

# 2. Bayesian classifiers 

A Bayesian network (BN) (Pearl, 1988; Jensen, 2001) is a powerful tool for knowledge representation, and it provides a compact representation of a joint probability distribution over a set of variables. Formally, a BN over a set of discrete random variables $\mathcal{X}=\left\{X_{1}, \ldots, X_{m}\right\}$ is denoted by $B=\left(B_{S}, \boldsymbol{\Theta}_{B_{S}}\right)$, where $B_{S}$ is a directed acyclic graph and $\boldsymbol{\Theta}_{B_{S}}$ is the set of conditional probabilities. To describe $B_{S}$, we let $\mathrm{pa}\left(X_{i}\right)$ denote the parents of $X_{i}$ in $B_{s}$, and $\operatorname{ch}\left(X_{i}\right)$ is the children of $X_{i}$ in $B_{s}$. We use $\operatorname{sp}\left(X_{i}\right)$ to denote the state space of $X_{i}$ (i.e., the set of values the variable $X_{i}$ can take), and for a set of variables we have $\operatorname{sp}(\mathcal{X})=\times_{X \in \mathcal{X}} \operatorname{sp}(X)$. We use the notation $X_{i} \Perp X_{j}$ to denote that $X_{i}$ is independent of $X_{j}$ and $X_{i} \Perp X_{j} \mid X_{k}$ for conditional independence of $X_{i}$ and $X_{j}$ given $X_{k}$. In the context of classification, we shall use $C$ to denote the class variable ( $\operatorname{sp}(C)$ is the set of possible classes), and $\mathcal{A}=\left\{A_{1}, \ldots, A_{n}\right\}$ is the set of attributes describing the possible instances to be classified.

When doing classification in a probabilistic framework, a new instance (described by $\boldsymbol{a} \in \operatorname{sp}(\mathcal{A})$ ) is classified to class $c^{*}$ according to:

$$
c^{*}=\arg \min _{c \in \operatorname{sp}(C)} \sum_{c^{\prime} \in \operatorname{sp}(C)} L\left(c \mid c^{\prime}\right) P\left(C=c^{\prime} \mid \boldsymbol{A}=\boldsymbol{a}\right)
$$

where $L(\cdot \mid \cdot)$ defines the loss function, i.e., $L\left(c \mid c^{\prime}\right)$ is the cost of classifying an instance to class $c$ when the correct class is $c^{\prime}$. The most commonly used loss function is the $0 / 1$-loss, defined such that $L\left(c \mid c^{\prime}\right)=0$ if $c^{\prime}=c$ and 1 otherwise. When using the $0 / 1$-loss function, the expression above can be rewritten as:

$$
c^{*}=\arg \max _{c \in \operatorname{sp}(C)} P(C=c \mid \boldsymbol{A}=\boldsymbol{a})
$$

which implies that an instance $\boldsymbol{a}$ is classified to the most probable class $c^{*}$ given that instance.

Since we rarely have access to $P(C=c \mid \boldsymbol{A}=\boldsymbol{a})$, learning a classifier amounts to estimating this probability distribution from a set of labeled training samples which we denote by $\mathcal{D}_{N}=\left\{\boldsymbol{D}_{1}, \ldots, \boldsymbol{D}_{N}\right\} ; N$ is the number of training instances and $\boldsymbol{D}_{i}=\left(c^{(i)}, a_{1}^{(i)}, \ldots, a_{n}^{(i)}\right)$ is the class and attributes of instance $i, i=1, \ldots, N$. Let $P\left(C=c \mid \boldsymbol{A}=\boldsymbol{a}, \mathcal{D}_{N}\right)$ be the a posteriori conditional probability for $C=c$ given $\boldsymbol{A}=\boldsymbol{a}$ after observing $\mathcal{D}_{N}$. Then an optimal Bayes classifier will classify a new instance with attributes $\boldsymbol{a}$ to class $c^{*}$ according to (see, e.g., Mitchell (1997)):

$$
c^{*}=\arg \min _{c \in \operatorname{sp}(C)} \sum_{c^{\prime} \in \operatorname{sp}(C)} L\left(c c^{\prime}\right) P\left(C=c^{\prime} \mid \boldsymbol{a}, \mathcal{D}_{N}\right)
$$

An immediate approach to calculate $P\left(C=c \mid \boldsymbol{A}=\boldsymbol{a}, \mathcal{D}_{N}\right)$ is to use a standard BN learning algorithm, where the training data is used to give each possible classifier a score which signals its appropriateness as a classification model. One such scoring function is based on the minimum description length (MDL) principle (Rissanen, 1978; Lam and Bacchus

1994):

$$
\operatorname{MDL}\left(B \mid \mathcal{D}_{N}\right)=\frac{\log N}{2}\left|\widehat{\boldsymbol{\Theta}}_{B_{S}}\right|-\sum_{i=1}^{N} \log \left(P_{B}\left(c^{(i)}, \boldsymbol{a}^{(i)} \mid \widehat{\boldsymbol{\Theta}}_{B_{S}}\right)\right)
$$

That is, the best scoring model is the one that minimizes $\operatorname{MDL}\left(\cdot \mid \mathcal{D}_{N}\right)$, where $\widehat{\boldsymbol{\Theta}}_{B_{S}}$ is the maximum likelihood estimate of the parameters in the model, and $\left|\widehat{\boldsymbol{\Theta}}_{B_{S}}\right|$ is the dimension of the parameter space (i.e., the number of free parameters in the model). However, as pointed out by Greiner et al. (1997) and Friedman et al. (1997) a "global" criterion like MDL may not be well suited for learning a classifier, as:

$$
\begin{aligned}
& \sum_{i=1}^{N} \log \left(P_{B}\left(c^{(i)}, \boldsymbol{a}^{(i)}, \widehat{\boldsymbol{\Theta}}_{B_{S}}\right)\right)= \\
& \quad \sum_{i=1}^{N} \log \left(P_{B}\left(c^{(i)} \mid \boldsymbol{a}^{(i)}, \widehat{\boldsymbol{\Theta}}_{B_{S}}\right)\right)+\sum_{i=1}^{N} \log \left(P_{B}\left(a_{1}^{(i)}, \ldots, a_{n}^{(i)}, \widehat{\boldsymbol{\Theta}}_{B_{S}}\right)\right)
\end{aligned}
$$

In the equation above, the first term on the right-hand side measures how well the classifier performs on $\mathcal{D}_{N}$, whereas the second term measures how well the classifier estimates the joint distribution over the attributes. Thus, only the first term is related to the classification task, and the latter term will therefore merely bias the model search; in fact, the latter term will dominate the score if $n$ is large. To overcome this problem, Friedman et al. (1997) propose to replace MDL with predictive MDL, $\mathrm{MDL}_{p}$, defined as:

$$
\operatorname{MDL}_{p}\left(B \mid \mathcal{D}_{N}\right)=\frac{\log N}{2}\left|\widehat{\boldsymbol{\Theta}}_{B_{S}}\right|-\sum_{i=1}^{N} \log \left(P_{B}\left(c^{(i)} \mid \boldsymbol{a}^{(i)}, \widehat{\boldsymbol{\Theta}}_{B_{S}}\right)\right)
$$

However, as also noted by Friedman et al. (1997), $\mathrm{MDL}_{p}$ cannot be calculated efficiently in general.

The argument leading to the use of $\mathrm{MDL}_{p}$ as a scoring function rests upon the asymptotic theory of statistics. That is, model search based on $\mathrm{MDL}_{p}$ is guaranteed to select the best classifier w.r.t. $0 / 1$-loss when $N \rightarrow \infty$. Unfortunately, though, the score may not be successful for finite datasets (Friedman, 1997). To overcome this potential drawback, Kohavi and John (1997) describe the wrapper approach. Informally, this method amounts to estimating the accuracy of a given classifier by cross-validation (based on the training data), and to use this estimate as the scoring function. The wrapper approach relieves the scoring function from being based on approximations of the classifier design, but at the potential cost of higher computational complexity. In order to reduce this complexity when learning a classifier, one approach is to focus on a particular sub-class of BNs. Usually, these sub-classes are defined by the set of independence statements they encode. For instance, one such restricted set of BNs is the Naïve Bayes models which assume that $A_{i} \Perp A_{j} \mid C$, i.e., that $P(C=c \mid \boldsymbol{A}=\boldsymbol{a}) \propto P(C=c) \prod_{i=1}^{n} P\left(A_{i}=a_{i} \mid C=c\right)$.

Even though the independence statements of the NB models are often violated in practice, these models have shown to provide surprisingly good classification results; the ranking of the classes may be correct even though the posterior conditional probability for the class variable is inaccurate. For instance, Zhang (2004a) shows that conditional dependences Springer

among the attributes do not affect classification accuracy as long as the dependences distribute evenly among the classes or if they cancel out. Other research into explaining the merits of the NB model has emphasized the difference between the $0 / 1$-loss function and the logloss, see e.g. Friedman (1997) and Domingos and Pazzani (1997). Friedman (p. 76, 1997) concludes:

Good probability estimates are not necessary for good classification; similarly, low classification error does not imply that the corresponding class probabilities are being estimated (even remotely) accurately.

The starting point of Friedman (1997) is that a classifier learned for a particular domain is a function of the training set. As the training set is considered a random sample from the domain, the classifier generated by a learner can be seen as a random variable; we shall use $\hat{P}(C=c \mid \boldsymbol{A})$ to denote the learned classifier. Friedman (1997) characterizes a (binary) classifier by its bias (i.e., $\mathbb{E}_{\mathcal{D}_{N}}[P(C \mid \boldsymbol{A})-\hat{P}(C \mid \boldsymbol{A})]$ ) and its variance (i.e., $\operatorname{Var}_{\mathcal{D}_{N}}(\hat{P}(C \mid \boldsymbol{A}))$ ); the expectations are taken over all possible training sets of size N. Friedman (1997) shows that in order to learn classifiers with low $0 / 1$-loss it may not be sufficient to simply focus on finding a model with negligible classifier bias; robustness in terms of low classifier variance can be just as important.

An example of a class of models where negligible asymptotic bias (i.e., fairly high model expressibility) is combined with robustness is the Tree Augmented Naïve Bayes (TAN) models, see Friedman et al. (1997). TAN models relax the NB assumption by allowing a more general correlation structure between the attributes. More specifically, a Bayesian network model is initially created over the variables in $\mathcal{A}$, and this model is designed such that each variable $A_{i}$ has at most one parent (that is, the structure is a directed tree). Afterwards, the class attribute is included in the model by making it the parent of each attribute. Friedman et al. (1997) use an adapted version of the algorithm by Chow and Liu (1968) to learn the classifier, and they prove that the structure they find is the TAN model which maximizes the likelihood of $\mathcal{D}_{N}$; the algorithm has time complexity $O\left(n^{2}(N+\log (n))\right)$. The TAN model has clearly more expressive power than the NB model (Jaeger, 2003), however, it can still not represent all correlation structures among the attributes. As an alternative we consider another class of models (called Hierarchical Naïve Bayes models) that can in principle model any such correlation structure.

# 3. Hierarchical Naïve Bayes models 

A special class of Bayesian networks is the so-called Hierarchical Naïve Bayes (HNB) models (Zhang et al., 2003), see also Kočka and Zhang (2002), and Zhang (2004b). An HNB is a tree-shaped Bayesian network with only discrete variables, and where the variables are partitioned into three disjoint sets: $\{C\}$ is the class variable, $\mathcal{A}$ is the set of attributes, and $\mathcal{L}$ is a set of latent (or hidden) variables. In the following we use $A$ to represent an attribute, whereas $L$ is used to denote a latent variable; $X$ and $Y$ denote variables that may be either attributes or latent variables. In an HNB the class variable $C$ is the root of the tree $(\operatorname{pa}(C)=\emptyset)$ and the attributes are at the leaves $(\operatorname{ch}(A)=\emptyset, \forall A \in \mathcal{A})$; the latent variables are all internal $(\operatorname{ch}(L) \neq \emptyset, \operatorname{pa}(L) \neq \emptyset, \forall L \in \mathcal{L})$. The use of latent variables allows conditional dependencies to be encoded in the model (as compared to, e.g., the NB model). For instance, by introducing a latent variable as a parent of the attributes $A_{i}$ and $A_{j}$, we can represent the (local) dependence statement $A_{i} \not \models A_{j} \mid C$ (see for instance $A_{1}$ and $A_{2}$ in Fig. 1). Being able

to model such local dependencies is particularly important for classification, as overlapping information would otherwise be double-counted:

Example 1. Consider a domain consisting of two classes $(C=0$ or $C=1)$, and two binary attributes $A_{1}$ and $A_{2}$. Assume that $A_{1}$ and $A_{2}$ always have the same value, i.e., $P\left(A_{1}=\right.$ $\left.A_{2}\right)=1$, and let $P\left(A_{i}=k \mid C=k\right)=3 / 5$, for $i=1,2, k=0,1$, and $P(C=0)=2 / 3$. Consequently, we have:

$$
\begin{aligned}
P(C=0 \mid \boldsymbol{A}=\mathbf{1}) & =\frac{P\left(A_{1}=1, A_{2}=1 \mid C=0\right) P(C=0)}{P\left(A_{1}=1, A_{2}=1\right)} \\
& =\frac{2 / 5 \cdot 2 / 3}{2 / 5 \cdot 2 / 3+3 / 5 \cdot 1 / 3}=\frac{4}{7}
\end{aligned}
$$

and therefore $P\left(C=0 \mid A_{1}=1, A_{2}=1\right)>P\left(C=1 \mid A_{1}=1, A_{2}=1\right)$. On the other hand, if we were to encode this domain in a Naïve Bayes structure, we would get:

$$
\begin{aligned}
P(C=0 \mid \boldsymbol{A}=\mathbf{1}) & =\frac{P\left(A_{1}=1, A_{2}=1 \mid C=0\right) P(C=0)}{\sum_{j} P\left(A_{1}=1, A_{2}=1 \mid C=j\right) \cdot P(C=j)} \\
& =\frac{P\left(A_{1}=1 \mid C=0\right) P\left(A_{2}=1 \mid C=0\right) P(C=0)}{\sum_{j} P\left(A_{1}=1 \mid C=j\right) P\left(A_{2}=1 \mid C=j\right) P(C=j)} \\
& =\frac{2 / 5 \cdot 2 / 5 \cdot 2 / 3}{2 / 5 \cdot 2 / 5 \cdot 2 / 3+3 / 5 \cdot 3 / 5 \cdot 1 / 3}=8 / 17
\end{aligned}
$$

hence $P\left(C=0 \mid A_{1}=1, A_{2}=1\right)<P\left(C=1 \mid A_{1}=1, A_{2}=1\right)$, which would revert the classification if $0 / 1$-loss is used.

Note that the HNB model reduces to the NB model in the special case when there are no latent variables.

When learning an HNB we can restrict our attention to the parsimonious HNB models; we need not consider models which encode a probability distribution that is also encoded by another model with fewer parameters. Formally, an HNB model, $M=\left(B_{S}, \Theta_{B_{S}}\right)$, with class variable $C$ and attribute variables $\mathcal{A}$ is said to be parsimonious if there does not exist another HNB model, $M^{\prime}=\left(B_{S}^{\prime}, \Theta_{B_{S}}^{\prime}\right)$, with the same class and attribute variables such that:
i) $M^{\prime}$ has fewer parameters than $M$, i.e., $\left|\Theta_{B_{S}}\right|>\left|\Theta_{B_{S}}^{\prime}\right|$.
ii) The probability distributions over the class and attribute variables are the same in the two models, i.e., $P_{M}(C, \boldsymbol{A})=P_{M^{\prime}}(C, \boldsymbol{A})$.

In order to obtain an operational characterization of these models, Zhang et al. (2003) define the class of regular HNB models. An HNB model is said to be regular if for any latent variable $L$, with neighbors (parent and children) $X_{1}, X_{2}, \ldots, X_{n}$, it holds that:

$$
$$

Strict inequality must hold whenever $L$ has only two neighbors and at least one of them is a latent node. ${ }^{1}$

Zhang et al. (2003) show that i) any parsimonious HNB model is regular, and ii) for a given set of class and attribute variables, the set of regular HNB model structures is finite. Observe that these two properties ensure that when searching for an HNB model we only need to consider regular HNB models and we need not deal with infinite search spaces. ${ }^{2}$

As opposed to other frameworks, such as NB or TAN models, an HNB can model any correlation among the attribute variables given the class by simply choosing the state spaces of the latent variables large enough (although this encoding is not necessarily done in a costeffective manner in terms of model complexity); note that the independence statements are not always represented explicitly in the graphical structure, but are sometimes only encoded in the conditional probability tables. On the other hand, the TAN model, for instance, is particularly efficient for encoding such statements but may fail to represent certain types of dependence relations among the attribute variables.

Example 2. Consider the classification rule " $\mathrm{C}=1$ if and only if exactly two out of the three binary attributes $A_{1}, A_{2}$ and $A_{3}$ are in state 1 ". Obviously, a Naïve Bayes model can not represent this statement, and neither can the TAN model; see Jaeger (2003) for a discussion regarding the expressibility of probabilistic classifiers.

On the other hand, an HNB can (somewhat expensively) do it as follows: As the only child of the binary class variable we introduce the latent variable L , with $\operatorname{sp}(L)=\{0,1 \ldots, 7\}$ and $\operatorname{ch}(L)=\left\{A_{1}, A_{2}, A_{3}\right\} . A_{j}(j=1,2,3)$ is given deterministically by its parent, and its CPT is defined s.t. $A_{j}=1$ iff bit $j$ equals 1 when the value of $L$ is given in binary representation. If, for instance, $L=5$ (101 in binary representation), then $A_{1}=1, A_{2}=0$, and $A_{3}=1$ (with probability 1). Thus, all information about the attributes is contained in $L$, and we can simply use the classification rule $C=1$ iff $L \in\{3,5,6\}$, which can be encoded by insisting that $P(L=l \mid C=0)$ is 0 for $l \in\{3,5,6\}$ and strictly positive otherwise, whereas $P(L=l \mid C=1)$ is strictly positive iff $l \in\{3,5,6\}$ and 0 otherwise.

More generally, by following the method above we see that any conditional correlation among the attributes can, in principle, be modeled by an HNB: Simply introduce a single latent variable $L$ having all the attributes as children and with the state space defined as $\operatorname{sp}(L)=\times_{i=1}^{n} \operatorname{sp}\left(A_{i}\right)$. Clearly, this structure can encode any conditional distribution over the attributes.

# 4. Learning HNB classifiers 

Learning an HNB model for classification has previously been explored by Zhang et al. (2003), with the aim of finding a scientific model with an interesting latent structure. Their method is based on a hill-climbing algorithm where the models are scored using the BIC score. However, a drawback of the algorithm is its high computational complexity, and, as discussed in Section 2, the type of scoring function being used does not necessarily facilitate

[^0]
[^0]:    ${ }^{1}$ We will not consider regular HNB models with singly connected latent variables.
    ${ }^{2}$ Note that Zhang et al. (2003) do not consider whether a regular model is parsimonious or not. When we later search the space of all regular models looking for a "good" classifier we may therefore not use the smallest search space that define all parsimonious HNB classifiers.

the identification of an accurate classifier. In particular, Zhang et al. (p. 284, 2003) state that
[...] the primary goal of this paper is to discover interesting latent variables rather than to improve classification accuracy.

In what follows we take a different approach as we focus on learning HNB models with the sole aim of obtaining an accurate classifier. ${ }^{3}$ We also demonstrate the feasibility of the algorithm in terms of its computational complexity, and we describe an inference procedure which is tailored for the learned models.

# 4.1. The main algorithm 

Our learning algorithm is based on a greedy search over the space of HNBs; we initiate the search with an HNB model, $H_{0}$, and learn a sequence $\left\{H_{k}\right\}, k=0,1, \ldots$ of HNB models. The search is conducted such that at each step $k$ we investigate the search boundary (denoted $\left.\mathcal{B}\left(H_{k}\right)\right)$ of the current model $H_{k}$, i.e., the set of models that can be reached from $H_{k}$ in a single step. We then score all models $H \in \mathcal{B}\left(H_{k}\right)$ and pick the best scoring one. This is repeated until no higher scoring model can be found.

The search boundary is defined such that the HNB structure is grown incrementally starting from the NB model. More specifically, if $\mathcal{L}_{k}$ is the set of latent variables in model $H_{k}$, then the set of latent variables in $H_{k+1}$, is enlarged such that $\mathcal{L}_{k+1}=\mathcal{L}_{k} \cup\{L\}$, where $L$ is a new latent variable. We restrict ourselves to only consider candidate latent variables which are parents of two variables $X$ and $Y$ where $\{X, Y\} \subseteq \operatorname{ch}(C)$ in $H_{k} .{ }^{4}$ Hence, we define $H_{k+1}$ as the HNB which is produced from $H_{k}$ by including a latent variable $L$ such that $\operatorname{pa}(L)=\{C\}$ and $\operatorname{pa}(X)=\operatorname{pa}(Y)=\{L\} ; H_{k+1}$ is otherwise structurally identical to $H_{k}$. Thus, the search boundary $\mathcal{B}\left(H_{k}\right)$ consists of all models where exactly one latent variable has been added to $H_{k}$; there is one such model in $\mathcal{B}\left(H_{k}\right)$ for each possible definition of the state space for the new latent variable. Note that since we use the NB model structure as our starting point $\left(H_{0}\right)$ each $H_{k}$ is a tree with a binary internal structure, i.e., any latent node $L^{\prime} \in \mathcal{L}_{k}$ has exactly two children but the class node $C$ may have up to $n$ children.

Unfortunately, since $\mathcal{B}\left(H_{k}\right)$ contains a model for each possible specification of the state space of each possible latent variable it is not computationally feasible to evaluate all the models in the search boundary. To overcome this problem we instead select $\kappa>1$ models (contained in $\mathcal{B}\left(H_{k}\right)$ ) to represent the search boundary, and then we evaluate these models. Specifically, when identifying a particular model in this set we proceed in two steps:

1) decide where to insert the latent variable;
2) define the state space of the latent variable.

In order to increase the robustness of the algorithm (e.g., in case of outliers), we pick the $\kappa>1$ models as follows: Randomly partition the training data $\mathcal{D}_{N}$ into $\kappa$ partly overlapping subsets, each containing $100(\kappa-1) / \kappa \%$ of the training data, and then use each of these subsets to approximate the best model in the search boundary (following the two-step procedure above). This results in a list of up to $\kappa$ different candidate models which are used to represent $\mathcal{B}\left(H_{k}\right)$. Note that when using the above two-step procedure for identifying a

[^0]
[^0]:    ${ }^{3}$ Since HNBs are only defined for discrete variables, all continuous variables should be discretized before the learning algorithm is deployed.
    ${ }^{4}$ Note that restricting the latent variables to only having two children does not afect the expressibility of the models.
    Springer

latent variable, we cannot use scoring functions such as the wrapper approach, MDL, or $\mathrm{MDL}_{p}$ in the first step since this step does not select a completely specified HNB.

From the set of models representing the search boundary we then select a model with a higher score than the current one; if no such model can be found, then the current model is returned. The score function is defined such that a high value corresponds to what is thought to be a model with good classification qualities (as measured by the average loss on unseen data), i.e., $\operatorname{Score}\left(H \mid \mathcal{D}_{N}\right)$ measures the "goodness" of $H$. In order to apply a score metric that is closely related to what the search algorithm tries to achieve, we use the wrapper approach by Kohavi and John (1997). That is, we use cross-validation (over the training set $\mathcal{D}_{N}$ ) to estimate an HNB's classification accuracy on unseen data; notice that the test set (if specified) is not used by the learner. To summarize, the structure of the algorithm can be outlined as follows:

# Algorithm 1. (Skeleton) 

1. Initiate model search with $H_{0}$.
2. Partition the training set into $\kappa$ subsets $\mathcal{D}^{(1)}, \ldots, \mathcal{D}^{(\kappa)}$.
3. For $k=0,1, \ldots, n-1:^{5}$
a) For $i=1, \ldots, \kappa$ :
i) Select a candidate latent variable $L^{(i)}$ according to $\mathcal{D}^{(i)}$.
ii) Select the state space of $L^{(i)}$.
iii) Define $H^{(i)}$ by "including" $L^{(i)}$ in $H_{k}$.
b) $H^{\prime}=\arg \max _{i=1, \ldots, \kappa} \operatorname{Score}\left(H^{(i)} \mid \mathcal{D}_{N}\right)$.
c) If $\operatorname{Score}\left(H^{\prime} \mid \mathcal{D}_{N}\right)>\operatorname{Score}\left(H_{k} \mid \mathcal{D}_{N}\right)$ then:

$$
H_{k+1} \leftarrow H^{\prime} ; k \leftarrow k+1
$$

else
return $H_{k}$.

## 4. Return $H_{n}$.

Before describing Step (i) and Step (ii) in detail, we recall that the algorithm starts out with an NB model, and that the goal is to introduce latent variables to improve upon that structure, i.e., to avoid "double-counting" of information when the independence statements of the NB model are violated.

### 4.1.1. Step (i): Finding a candidate latent variable

To facilitate the goal of the algorithm, a latent variable $L$ is proposed as the parent of $\{X, Y\} \subseteq \operatorname{ch}(C)$ if the data points towards $X \Perp Y \mid C$. That is, we consider variables that are strongly correlated given the class variable as indicating a promising position for including a latent variable; from this perspective there is no reason to introduce a latent variable as a parent of $X$ and $Y$ if $X \Perp Y \mid C$. Hence, the variables that have the highest correlation given the class variable may be regarded as the most promising candidate-pair. More specifically, we calculate the conditional mutual information given the class variable, $I(\cdot, \cdot \mid C)$, for all (unordered) pairs $\{X, Y\} \subseteq \operatorname{ch}(C) .{ }^{6}$ However, as $I(X, Y \mid C)$ is increasing in both $|\operatorname{sp}(X)|$

[^0]
[^0]:    ${ }^{5}$ Note that the search procedure ensures that we will at most make $n-1$ model selections (step $c$ ).
    ${ }^{6}$ One might also consider other measures for testing for conditional dependences.

and $|\operatorname{sp}(Y)|$ we cannot simply pick the pair $\{X, Y\}$ that maximizes $I(X, Y \mid C)$; this strategy would unintentionally bias the search towards latent variables with children having large state spaces. Instead we utilize that under the assumption that $X \Perp Y \mid C$ we have:

$$
2 N \cdot I(X, Y \mid C) \stackrel{\mathcal{L}}{\rightarrow} \chi_{v}^{2}
$$

where $v=|\operatorname{sp}(C)|(|\operatorname{sp}(X)|-1)(|\operatorname{sp}(Y)|-1)$, and $\xrightarrow{\mathcal{L}}$ means convergence in distribution as $N \rightarrow \infty$, see, e.g., Whittaker (1990). Finally, we let $i(X, Y)$ be the estimated value of $I(X, Y \mid C)$, and calculate

$$
Q\left(X, Y \mid \mathcal{D}_{N}\right)=P(Z \geq 2 N \cdot i(X, Y))
$$

where $Z$ is $\chi^{2}$ distributed with $v$ degrees of freedom, that is, $Q\left(X, Y \mid \mathcal{D}_{N}\right)$ gives the $p$-value of a hypothesis test of $H_{0}: X \Perp Y \mid C$. The pairs $\{X, Y\}$ are ordered according to these probabilities, such that the pair with the lowest probability is picked out. By selecting the pairs of variables according to $Q\left(X, Y \mid \mathcal{D}_{N}\right)$, the correlations are normalized w.r.t. the size differences in the state spaces.

Unfortunately, to greedily select a pair of highly correlated variables as the children of a new latent variable is not always the same as improving classification accuracy, as can be seen from the example below.

Example 3. Consider a classifier with binary attributes $\mathcal{A}=\left\{A_{1}, A_{2}, A_{3}\right\}$ (all with uniform marginal distributions) and target concept $C=1 \Leftrightarrow\left\{A_{1}=1 \wedge A_{2}=1\right\}$. Assume that $A_{1}$ and $A_{2}$ are marginally independent but that $P\left(A_{2}=A_{3}\right)=0.99$. It then follows that:

$$
P\left(Q\left(A_{2}, A_{3} \mid \mathcal{D}_{N}\right)<Q\left(A_{1}, A_{2} \mid \mathcal{D}_{N}\right)\right) \rightarrow 1
$$

as $N$ grows large (the uncertainty is due to the random nature of $\mathcal{D}_{N}$ ). Hence, the heuristic will not pick out $\left\{A_{1}, A_{2}\right\}$ which in a myopic sense appears to be most beneficial w.r.t. classification accuracy, but will propose to add a variable $L^{\prime}$ with children ch $\left(L^{\prime}\right)=\left\{A_{2}, A_{3}\right\}$. Luckily, as we shall see in Example 4, this does not necessarily affect classification accuracy.

# 4.1.2. Step (ii): Selecting the state space 

To find the cardinality of a latent variable $L$, we use an algorithm similar to the one by Elidan and Friedman (2001): Initially, the latent variable is defined such that $|\operatorname{sp}(L)|=$ $\prod_{X \in \operatorname{ch}(L)}|\operatorname{sp}(X)|$, where each state of $L$ corresponds to exactly one combination of the states of the children of $L$. Let the states of the latent variable be labeled $l_{1}, \ldots, l_{t}$. We then iteratively collapse two states $l_{i}$ and $l_{j}$ into a single state $l^{*}$ as long as this is "beneficial". This approach implies that a latent variable can be seen as aggregating the information from its children which is relevant for classification. Moreover, as we shall see later in this section, this semantic interpretation allows us to infer data for the latent variables due to the deterministic relations encoded in the model.

Now, ideally we would measure the benefit of collapsing two states using the wrapper approach, but as this is computationally expensive we shall instead use the $\mathrm{MDL}_{p}$ score to approximate the classification accuracy. Let $H^{\prime}=\left(B_{S}^{\prime}, \boldsymbol{\Theta}_{B_{S}^{\prime}}\right)$ be the HNB model obtained from a model $H=\left(B_{S}, \boldsymbol{\Theta}_{B_{S}}\right)$ by collapsing states $l_{i}$ and $l_{j}$. Then $l_{i}$ and $l_{j}$ should be collapsed if and only if $\Delta_{L}\left(l_{i}, l_{j} \mid \mathcal{D}_{N}\right)=\operatorname{MDL}_{p}\left(H \mid \mathcal{D}_{N}\right)-\operatorname{MDL}_{p}\left(H^{\prime} \mid \mathcal{D}_{N}\right)>0$. For each Springer

pair $\left(l_{i}, l_{j}\right)$ of states we therefore compute:

$$
\begin{aligned}
\Delta_{L}\left(l_{i}, l_{j} \mid \mathcal{D}_{N}\right)= & \operatorname{MDL}_{p}\left(H \mid \mathcal{D}_{N}\right)-\operatorname{MDL}_{p}\left(H^{\prime} \mid \mathcal{D}_{N}\right) \\
= & \frac{\log (N)}{2}\left(\left|\boldsymbol{\Theta}_{B_{S}}\right|-\left|\boldsymbol{\Theta}_{B_{S}^{\prime}}\right|\right) \\
& +\sum_{i=1}^{N}\left[\log \left(P_{H^{\prime}}\left(c^{(i)} \mid a^{(i)}\right)\right)-\log \left(P_{H}\left(c^{(i)} \mid a^{(i)}\right)\right)\right]
\end{aligned}
$$

For the second term we first note that:

$$
\begin{aligned}
\sum_{i=1}^{N}\left[\log \left(P_{H^{\prime}}\left(c^{(i)} \mid a^{(i)}\right)\right)-\log \left(P_{H}\left(c^{(i)} \mid a^{(i)}\right)\right)\right] & =\sum_{i=1}^{N} \log \frac{P_{H^{\prime}}\left(c^{(i)} \mid a^{(i)}\right)}{P_{H}\left(c^{(i)} \mid a^{(i)}\right)} \\
& =\sum_{D \in \mathcal{D}_{N}: f\left(D, l_{i}, l_{j}\right)} \log \frac{P_{H^{\prime}}\left(c^{D} \mid a^{D}\right)}{P_{H}\left(c^{D} \mid a^{D}\right)}
\end{aligned}
$$

where $f\left(D, l_{i}, l_{j}\right)$ is true if case $D$ includes either $\left\{L=l_{i}\right\}$ or $\left\{L=l_{j}\right\}$; cases that do not include these states cancel out. This is also referred to as local decomposability by Elidan and Friedman (2001), i.e., the gain of collapsing two states $l_{i}$ and $l_{j}$ is local to those states and it does not depend on whether or not other states have been collapsed. Note that in order to calculate $f(\cdot)$ we exploit that the deterministic relations between the latent variables and their children allows us to infer actual values for the latent variables for any configuration over the attributes (we shall return to this issue later in this section).

In order to avoid considering all possible combinations of the attributes we approximate the difference in predictive MDL as the difference w.r.t. the relevant subtree. The relevant subtree is defined by $C$ together with the subtree having $L$ as root: ${ }^{7}$

$$
\begin{aligned}
\sum_{D \in \mathcal{D}_{N}: f\left(D, l_{i}, l_{j}\right)} & \log \frac{P_{H^{\prime}}\left(c^{D} \mid a^{D}\right)}{P_{H}\left(c^{D} \mid a^{D}\right)} \\
& \approx \log \prod_{c \in \operatorname{sp}(C)}\left[\frac{\left(\frac{N\left(c, l_{i}\right)+N\left(c, l_{j}\right)}{N\left(l_{i}\right)+N\left(l_{j}\right)}\right)^{N\left(c, l_{i}\right)+N\left(c, l_{j}\right)}}{\left(\frac{N\left(c, l_{i}\right)}{N\left(l_{i}\right)}\right)^{N\left(c, l_{i}\right)} \cdot\left(\frac{N\left(c, l_{j}\right)}{N\left(l_{j}\right)}\right)^{N\left(c, l_{j}\right)}}\right]
\end{aligned}
$$

where $N(c, s)$ and $N(s)$ are the sufficient statistics. I.e., $N(c, s)$ is the number of cases in the database where $C=c$ and $L=s$, and $N(s)=\sum_{c \in \operatorname{sp}(C)} N(c, s)$ is the number of cases where $L=s$. We shall return to the accuracy of the approximation later in this section.

States are collapsed in a greedy manner, i.e., we find the pair of states with highest $\Delta_{L}\left(l_{i}, l_{j} \mid \mathcal{D}_{N}\right)$ and collapse those two states if $\Delta_{L}\left(l_{i}, l_{j} \mid \mathcal{D}_{N}\right)>0$. This is repeated (making use of local decomposability) until no states can be collapsed:

[^0]
[^0]:    ${ }^{7}$ The relevant subtree can also be seen as the part of the classifier structure that is directly affected by the potential collapse of the states $l_{i}$ and $l_{j}$.

# Algorithm 2. (Determine state space of $L$ ) 

1. Initiate state space such that $|\operatorname{sp}(L)|=\prod_{X \in \operatorname{ch}(L)}|\operatorname{sp}(X)|$.

Label the states such that each state corresponds to a unique combination of $\operatorname{ch}(L)$.
2. For each $l_{i}, l_{j} \in \operatorname{sp}(L)$ do:

Calculate $\Delta_{L}\left(l_{i}, l_{j} \mid \mathcal{D}_{N}\right)$.
3. Select $l_{i}^{\prime}, l_{j}^{\prime} \in \operatorname{sp}(L)$ such that $\Delta_{L}\left(l_{i}^{\prime}, l_{j}^{\prime} \mid \mathcal{D}_{N}\right)$ is maximized.
4. If $\Delta_{L}\left(l_{i}^{\prime}, l_{j}^{\prime} \mid \mathcal{D}_{N}\right)>0$ then:

Collapse states $l_{i}^{\prime}$ and $l_{j}^{\prime}$; goto 2 .
5. Return state space of $L$.

It should be noted that Elidan and Friedman (2001) initialize their search with one state in $L$ for each combination of the variables in the Markov blanket of $L$. However, since we are only interested in regular HNB models it is sufficient to consider the smaller set of variables defined by $\operatorname{ch}(L)$ (cf. Eq. 2). Actually, even with this set of variables we may still produce irregular HNB models, but as we use the difference in predictive MDL to guide the refinement of the state space we are guaranteed to arrive at a regular HNB as $N \rightarrow \infty .^{8}$

Example 4. (Example 3 cont'd) The state space of $L^{\prime}$ with $\operatorname{ch}\left(L^{\prime}\right)=\left\{A_{2}, A_{3}\right\}$ is collapsed by Algorithm 2 after $L^{\prime}$ is introduced. For large N the penalty term in $\mathrm{MDL}_{p}$ ensures that the state space will be collapsed to two states mirroring the states of $A_{2}$ because $L^{\prime}$ will not significantly change the predictive likelihood from what the model previously held (note that $P\left(C=c \mid A_{2}, A_{3}, \mathcal{D}_{N}\right) \approx P\left(C=c \mid A_{2}, \mathcal{D}_{N}\right)$ ). Hence, by introducing $L^{\prime}$ we get a more robust classifier, where the classification noise introduced by $A_{3}$ is removed; in this sense, the algorithm can be seen as incorporating a form of feature selection (Langley, 1994). The latent variable $L^{\prime \prime}$ with children $\operatorname{ch}\left(L^{\prime \prime}\right)=\left\{L^{\prime}, A_{1}\right\}$ will be introduced in the next iteration of Algorithm 1, and the target concept can eventually be learned.

Note that Algorithm 2 will only visit a subset of the HNB models in the search boundary, namely those where the latent variables are given (deterministically) by the value of their children. An important side-effect of this is that we can give a semantic interpretation to the state spaces of the latent variables in the models the algorithm generates: $L \in \mathcal{L}$ aggregates the information from its children which is relevant for classification. If, for example, $L$ is the parent of two binary variables $A_{1}$ and $A_{2}$, then Algorithm 2 is initiated such that $L$ 's state space is $\operatorname{sp}(L)=\left\{A_{1}=0 \wedge A_{2}=0, A_{1}=0 \wedge A_{2}=1, A_{1}=1 \wedge A_{2}=0, A_{1}=1 \wedge A_{2}=\right.$ 1\}. When the algorithm collapses states, we can still maintain an explicit semantics over the state space, e.g., if the first and second state is collapsed we obtain a new state defined as $\left(A_{1}=0 \wedge A_{2}=0\right) \vee\left(A_{1}=0 \wedge A_{2}=1\right)$, i.e., $A_{1}=0 .{ }^{9}$ Observe that this interpretation also implies that if the attributes have been produced by discretizing a collection of continuous variables (see, e.g., Fayyad \& Irani (1993)), then the latent variables can be seen as encoding a form of hierarchical discretization of the original variables.

An important aspect of the semantic interpretation, is that it allows us to infer data for the latent variables due to the deterministic relations encoded in the model. This fact provides us with a fast calculation scheme, as we "observe" all the variables in $\mathcal{A}$ and $\mathcal{L}$. It therefore also

[^0]
[^0]:    ${ }^{8}$ The problem with irregular HNB models appears when there exists a variable $X \in \operatorname{ch}(L)$ such that $|\operatorname{sp}(X)|>$ $|\operatorname{sp}(C)|$.
    ${ }^{9}$ Note that the semantics also allow the decision maker to inspect the "rules" that form the basis of a given classification. Through this insight she can e.g. consider whether the classification of the system should be overruled or accepted.
    Springer

follows that we can represent the HNB classifier using only the class variable and its children. Hence, the representation we will utilize is a Naïve Bayes structure where the "attributes" are represented by the variables which occur as children of the class variable in the HNB model. It is simple to realize that the number of free parameters required to represent this structure equals:

$$
\left|\Theta_{B_{S}}\right|=(|\operatorname{sp}(C)|-1)+|\operatorname{sp}(C)| \sum_{X \in \operatorname{ch}(C)}(|\operatorname{sp}(X)|-1)
$$

see also Kočka and Zhang (2002). Hence, the difference in predictive MDL (used in Algorithm 2) can be approximated by:

$$
\begin{aligned}
\Delta_{L}\left(l_{i}, l_{j}\right) & \approx \log _{2}(N) \frac{|\operatorname{sp}(C)|}{2} \\
& -\sum_{c \in \operatorname{sp}(C)} N\left(c, l_{i}\right) \log _{2}\left(\frac{N\left(c, l_{i}\right)}{N\left(c, l_{i}\right)+N\left(c, l_{j}\right)}\right) \\
& -\sum_{c \in \operatorname{sp}(C)} N\left(c, l_{j}\right) \log _{2}\left(\frac{N\left(c, l_{j}\right)}{N\left(c, l_{i}\right)+N\left(c, l_{j}\right)}\right) \\
& +N\left(l_{i}\right) \log \left(\frac{N\left(l_{i}\right)}{N\left(l_{i}\right)+N\left(l_{j}\right)}\right)+N\left(l_{j}\right) \log \left(\frac{N\left(l_{j}\right)}{N\left(l_{i}\right)+N\left(l_{j}\right)}\right)
\end{aligned}
$$

It can be shown that the approximation of Eq. (5) is exact if $P\left(\operatorname{ch}(C) \backslash\{L\} \mid L=l_{i}\right)=$ $P\left(\operatorname{ch}(C) \backslash\{L\} \mid L=l_{j}\right)$.

Finally, to summarize the steps discussed above (and formalize Step (i) and Step (ii) of Algorithm 1) we have the following algorithm:

# Algorithm 3. (Learn HNB classifier) 

1. Initiate model search with $H_{0}$.
2. Partition the training set into $\kappa$ partly overlapping subsets $\mathcal{D}^{(1)}, \ldots, \mathcal{D}^{(\kappa)}$.
3. For $k=0,1, \ldots, n-1$ :
a) For $i=1, \ldots, \kappa$ :
i) Let $\left\{X^{(i)}, Y^{(i)}\right\}=\arg \min _{\{X, Y\} \subseteq \operatorname{ch}(C)} Q\left(X, Y \mid \mathcal{D}^{(i)}\right)$
(i.e., $\left\{X^{(i)}, Y^{(i)}\right\} \subseteq \operatorname{ch}(C)$ in $H_{k}$ ), and define the latent variable $\left(L^{(i)}\right)$ with children $\operatorname{ch}\left(L^{(i)}\right)=\left\{X^{(i)}, Y^{(i)}\right\}$.
ii) Collapse the state space of $L^{(i)}$ (Algorithm 2 with $\mathcal{D}^{(i)}$ used in place of $\mathcal{D}_{N}$ ).
iii) Define $H^{(i)}$ by introducing $L^{(i)}$ into $H_{\mathrm{k}}$.
b) $H^{\prime}=\arg \max _{i=1, \ldots, \kappa} \operatorname{Score}\left(H^{(i)} \mid \mathcal{D}_{N}\right)$.
c) If $\operatorname{Score}\left(H^{\prime} \mid \mathcal{D}_{N}\right)>\operatorname{Score}\left(H_{k} \mid \mathcal{D}_{N}\right)$ then:

$$
H_{k+1} \leftarrow H^{\prime} ; k \leftarrow k+1
$$

else
return $H_{k}$.
4. Return $H_{a}$.

It is obvious that any conditional distribution $P\left(A_{1}, \ldots, A_{N} \mid C\right)$ is in principle reachable by the search algorithm but, as the score function is multi-modal over the search space, the search will in general only converge towards a local optimum.

For the results reported in Section 5 we have used $\kappa=10$. This value was chosen (somewhat arbitrarily) based on a preliminary analysis, which suggested that the behavior of the algorithm is rather insensitive to the particular value of this parameter. In fact, most of the $\kappa$ candidate models examined in Step 3b were identical (in our experiments there were typically $1-2$ unique models out of the $\kappa=10$ models that were generated).

As a last remark we note that one may also consider other ways of determining the state space of the latent variables. One immediate approach is to search for a suitable state space by fixing the number of states, and use some learning algorithm, see e.g., Dempster et al. (1977), Binder et al. (1997), or Wettig et al. (2003). This can be done greedily to maximize some performance criteria, like BIC, MDL or $\mathrm{MDL}_{p}$. However, to reduce the computational complexity of the algorithm, we have not considered this any further.

# 4.2. Inference in the learned model 

The algorithm for collapsing the state space of a latent variable is the source of the semantics for these nodes, and in turn the reason why we can represent the HNB as a Naïve Bayes model with aggregations in place of the attributes. This compact representation requires a "deterministic inference engine" to calculate $P(C \mid \boldsymbol{a})$, because the aggregations defined by the semantics of the latent variables can in general not be encoded by the conditional probability tables for the variables. Assume, for instance, that we have three binary variables $L, X, Y, \operatorname{ch}(L)=\{X, Y\}$, and " $L=1$ if and only if $X=Y$ ". This relationship cannot be encoded in the model $X \leftarrow L \rightarrow Y$, and to infer the state of the latent variable $L$ from $X$ and $Y$ we would therefore need to design a special inference algorithm which explicitly uses the semantics of L. To alleviate this potential drawback we can simply re-define the networkstructure such that standard Bayesian inference algorithms (Lauritzen \& Spiegelhalter, 1988; Shafer \& Shenoy, 1990; Madsen \& Jensen, 1998) can be used: Introduce a new latent variable $L^{\prime}$, and change the network structure such that $\operatorname{ch}(L)=\operatorname{pa}(X)=\operatorname{pa}(Y)=\left\{L^{\prime}\right\} ; L^{\prime}$ is equipped with at most one state for each possible combination of its children's states. This enlarged structure is capable of encoding any relation between $\{X, Y\}$ and $L$ using only the conditional probability tables specified in the network. Hence, the enlarged structure can be handled by any standard BN propagation algorithm, and since the structure is still an HNB (although not a parsimonious one) the inference can be performed extremely fast.

### 4.3. Time complexity of the learning algorithm

The complexity can be analyzed by considering the three steps that characterize the algorithm:

1. Find a candidate latent variable.
2. Find the state space of the candidate latent variable, and check if it is useful.
3. Iterate until no more candidate latent variables are accepted.

## Part 1

Proposing a candidate latent variable corresponds to finding the pair $\{X, Y\}$ of variables with the strongest correlation (Equation 3). There are at most $\left(n^{2}-n\right) / 2$ such pairs, where $n$ is the number of attribute variables. By calculating the conditional mutual information for a pair of variables as well as sorting the pairs (for future iterations) according to this measure we get the time complexity: $O\left(n^{2} \cdot(N+\log (n))\right)$. In the remainder of this analysis we shall consider Springer

$\log (n)$ to be negligible compared to $N$ hence, for Part 1 we get $O\left(n^{2} \cdot(N+\log (n))\right) \approx$ $O\left(n^{2} \cdot N\right)$.

# Part 2 

The time complexity of calculating the gain, $\Delta_{L}(\cdot, \cdot)$, of collapsing two states is simply $O(N)$, see Eq. 5. Due to local decomposability, the gain of collapsing two states has no effect on collapsing two other states, and there are therefore at most $\left(|\operatorname{sp}(L)|^{2}-|\operatorname{sp}(L)|\right) / 2$ such possible combinations to calculate initially. Next, when two states are collapsed, $\Delta_{L}(\cdot, \cdot)$ must be calculated for $|\operatorname{sp}(L)|-1$ new state combinations, and the collapsing is performed at most $|\operatorname{sp}(L)|-1$ times. The time complexity of finding the state space of a candidate latent variable is therefore $O\left(N \cdot|\operatorname{sp}(L)|^{2}+N \cdot|\operatorname{sp}(L)|(|\operatorname{sp}(L)|-1) / 2\right)=O\left(|\operatorname{sp}(L)|^{2} \cdot N\right)$.

Having found the cardinality of a candidate variable, say $L$, we test whether it should be included in the model using the wrapper approach. From the rule-based propagation method it is easy to see that the time complexity of this task is $O(n \cdot N)$. Thus, the time complexity of Part 2 is $O\left(\left(n+|\operatorname{sp}(L)|^{2}\right) \cdot N\right)$.

## Part 3

Each time a latent variable is introduced we would in principle need to perform the above steps again, and the time complexity would therefore be $n-1$ times the time complexities above. However, by exploiting locality some of the previous calculations can be reused.

Moreover, note that after having introduced a latent variable $L$ with children $X$ and $Y$, we cannot create another latent variable having either $X$ or $Y$ as a child (due to the structure of the HNB model). Thus, after having included a latent variable the cardinality of the resulting set of candidate pairs is reduced by $n-1$. This implies that we will perform at most $n-2$ re-initializations, and the overall time complexity of the algorithm is therefore $O\left(n^{2} \cdot N+n \cdot\left(n \cdot N+\left(|\operatorname{sp}(L)|^{2} \cdot N\right)\right)\right)=O\left(n^{2} \cdot|\operatorname{sp}(L)|^{2} \cdot N\right)$.

It is important to emphasize that the computational complexity is dependent on the cardinality of the latent variables. In the worst case, if none of the states are collapsed, then the cardinality of a latent variable $L$ is exponential in the number of leaves in the subtree having $L$ as root. However, this situation also implies that the leaves are conditionally dependent given the class variable, and that the leaves and the class variable do not exhibit any type of context-specific independence (Boutilier et al., 1996).

The time complexity observed in practice during the empirical study is summarized in Appendix A.

## 5. Empirical results

In this section we will investigate the merits of the proposed learning algorithm by using it to learn classifiers for a number of different datasets taken from the Irvine Machine Learning Repository (Blake \& Merz, 1998). The datasets were selected based on their previous usage in similar types of analysis, e.g., Friedman et al. (1997) and Grossman and Domingos (2004); see Table 1 for a summary of the 22 datasets used in this empirical study.

### 5.1. Accuracy results

We have compared the results of the HNB classifier to those of the Naïve Bayes model (Duda \& Hart, 1973), the TAN model (Friedman et al., 1997), the original HNB algorithm (Zhang et al. 2003), C5.0 (Quinlan, 1998), a standard implementation of logistic regression,

Table 1 Datasets used in the experiments


A summary of the 22 datasets used in the experiments: \#Att indicates the number of attributes; \#Cls is the number of classes; Size is the number of instances. 5-fold cross-validation was used for all datasets. Further details regarding the datasets can be found at the UCI Machine Learning Repository.
and neural networks with one hidden layer trained by back-propagation. ${ }^{10}$ As some of the learning algorithms (including Algorithm 3) require discrete variables, the attributes were discretized using the entropy-based method of Fayyad and Irani (1993). In addition, instances containing missing attribute-values were removed; all pre-processing was performed using MLC++ (Kohavi et al., 1994).

The accuracy results for the datasets are given in Appendix B (Table 4) and a summary can be seen in Table 2. In this table we report the number of datasets for which each classifier is the best overall (\#Winner). Note that the sum of these numbers is larger than the number of datasets because we have several ties. For a specific classifier, \#Draw is the number of datasets where the classifier is not the best overall, but is not significantly worse than the winner either (at the $10 \%$ level). The last three columns give the number of datasets for which the classifier is significantly poorer than the winner at $10 \%, 5 \%$, and $1 \%$ level, respectively (see Appendix B for more information). In particular, we note that the proposed HNB classifier achieves the best result, among all the classification algorithms, for 12 of the 22 datasets, and draws with the winner for 8 of the other ones. The HNB algorithm is significantly poorer than the winner (at $10 \%$ level) for only 2 of the 22 datasets. Finally,

Table 2 Summary of classification results


[^0]
[^0]:    ${ }^{10}$ We used Clementine (SPSS Inc., 2002) to generate the C5.0, logistic regression and neural network models. Springer

Fig. 2 gives a graphical illustration of the accuracy results of the proposed algorithm compared to the accuracy results of the algorithms mentioned above.

To help the interpretation of the results reported in Table 2 and Table 4 we ran all algorithms with their "basic" configurations, i.e., no optimization was performed. One notable exception is the TAN model, which was run both in its basic form and with a damping-factor equal to 5 virtual counts (this algorithm is denoted TAN-5 in Table 2 and Table 4). The computational complexity of the algorithm by Zhang et al. (2003) prevented us from obtaining results for this algorithm from the three most complex domains.
![img-1.jpeg](img-1.jpeg)

Fig. 2 Scatter plot of classification error for HNB and a selection of other classification systems. In each plot, a point represents a dataset. The HNB's classification error is given on the $y$-axis, whereas the other system's error is given on the $x$-axis. Hence, data points below the diagonal corresponds to datasets where the HNB is superior, whereas points above the diagonal are datasets where the HNB classifier is inferior to the other system

![img-2.jpeg](img-2.jpeg)

Fig. 3 The figures show the estimated learning curves for Algorithm 3 (solid line), TAN (dashed line) and Naïve Bayes (dotted line). Part (a) gives the results for the car database, and the results for the postop database are shown in part (b)

# 5.2. Learning curve 

We have analyzed the effect that the size of training data has on the classification accuracy of our learning algorithm; we shall use $\alpha(N)$ to denote the accuracy of a learning algorithm when trained on a database of size $N$. The relation between $N$ and $\alpha(N)$ (called the learning curve) can provide important insight into the workings of the algorithms. For example, it is well known that the Naïve Bayes algorithm learns fast (relatively "high" accuracy for "small" databases), but because of the strong learning bias it also has a tendency to converge too quickly such that even for "large" databases, the accuracy does not increase beyond a certain level, see also Ng and Jordan (2002).

To estimate the learning curve (of a given algorithm) for a specific dataset we first made a random sub-sampling (without replacement) of $N$ cases from that dataset. These cases were then used as training data for the algorithm in question, and the remaining cases were used as test data; this was repeated 10 times for each $N$. As an example, consider Fig. 3, which shows the learning curves for the car database and the postop database.

For the results shown in Fig. 3, we note that the proposed learning algorithm appears to generate classifiers with the same fast starting property as the Naïve Bayes classifier, but, at the same time, avoids the premature convergence problem of these classifiers.

To examine this further, we generated learning curves for all the datasets used in the experiments. To be able to compare the learning curves from, e.g., postop (with only 90 cases) to the results of chess (with 3199 cases), we first scaled the values on the $x$-axis to give the percentage of the full dataset that was used as the training set. ${ }^{11}$ Next, in order to compare the accuracy results for the different datasets we normalized the results such that the best accuracy result obtained (for all data sizes and all classification algorithms) would correspond to 100 "points", whereas the worst result was given a score of 0 "points". Finally, we calculated the score obtained on each dataset when $x$ percent of the available data was used. The averages of these values are shown on the $y$-axis in Fig. 4 (a and b) as a function of the percentage of the data used as training data; the empirical standard deviations are shown in Fig. 4(b) using error bars.

[^0]
[^0]:    ${ }^{11}$ The result obtained using, e.g., $60 \%$ of the postop database as training data should be compared to the result obtained using $60 \%$ of chess database as training data.
    Springer

![img-3.jpeg](img-3.jpeg)

Fig. 4 The Figures show the scaled learning curves for the proposed HNB algorithm (Algorithm 3), TAN, and Naive Bayes. The $x$-axis show the percentage of the database used to obtain the results, and on the $y$-axis we report the average scaled eficiency. Figure (a) shows a histogram representation (included for ease of interpretation) of the average results, whereas Figure (b) also shows the empirical standard deviation using error-bars (an error-bar indicates 1 standard deviation of the estimate)

Finally, Fig. 5 shows the average number of latent variables inserted by the learning algorithm as a function of the size of the training set. The results are from the car database, and are averaged over 10 runs. We can see that the algorithm has a built-in ability to avoid overfitting when working with this dataset; only a few latent variables are inserted when the size of the training set is small, and the algorithm seems to stabilize around 3 latent variables for $N \geq 1000$ training cases.

# 5.3. Semantic interpretation of latent structures 

In some domains the learned HNB models may contain a latent structure, which is amenable to interpretation. In this subsection we will consider the car dataset, a synthetic dataset
![img-4.jpeg](img-4.jpeg)

Fig. 5 The number of latent variables inserted by the proposed HNB algorithm (Algorithm 3), as a function of the size of the training set (the numbers are from the car domain)

![img-5.jpeg](img-5.jpeg)

Fig. 6 The learned HNB model for the car database with three latent variables
consisting of 1728 cases which describe the relationship between certain characteristics of a car and whether or not the car is "acceptable". We have chosen the car database due to its intuitive interpretation and because its specification also covers the gold standard model from which the data was generated. The states of the class attribute are unacceptable, acceptable, good and very-good, and the attributes describing the car are: number of doors (Doors), capacity in term of persons (Persons), size of luggage boot (Lug_boot), estimated safety of the car (Safety), buying price (Buying), and price of maintenance (Maint). When applying the algorithm to this database we obtain the model illustrated in Figure 6.

The nodes TechValue, SafetyPrDollar and Cost correspond to the latent variables identified by the algorithm; the names of these variables have manually been deduced from their usage in the model. For example, the node Cost summarizes the two types of monetary costs using the four states Cost $=$ very-high, Cost $=$ high, Cost $=$ medium and Cost $=$ low, where e.g. the state very - high encodes the following configurations of the attributes Maint and Buying:

$$
\begin{aligned}
& {[\text { (Maint }=\text { very-high) } \wedge(\text { Buying }=\text { very-high })]} \\
& \vee \\
& {[\text { (Maint }=\text { very-high) } \wedge(\text { Buying }=\text { high })]} \\
& \vee \\
& {[\text { (Maint }=\text { high }) \wedge(\text { Buying }=\text { very-high })]}
\end{aligned}
$$

The node SafetyPrDollar compares the safety level to the cost, and contains the six states very-high, high, good, medium, low and very low. For instance, SafetyPrDollar $=$ very-low specify [Safety $=$ low $\wedge$ Cost $=$ very-high].

We conclude this subsection by reiterating that Algorithm 3 has the sole purpose of generating HNB models that achieve high classification accuracy. The semantic interpretation presented above is therefore a spin-off of the model definition rather than a required feature of our learning algorithm. Hence, we do not claim that all HNB models will have interesting latent structures; rather we suggest that it may be worthwhile to examine an HNB's latent structure. In some cases, this will give a decision maker insight into the rules which govern

the classification of some instance, and may thereby increase the user's confidence in the model.

# 6. Concluding remarks and future work 

In this paper we have proposed an algorithm for learning hierarchical Naïve Bayes models for classification. Experimental results have shown that the learned classifiers offer results that are significantly better than those of other commonly used classification methods. Moreover, a number of existing tools may be able to improve the classification accuracy even further, e.g., supervised learning of the probability parameters (Wettig et al., 2003).

As part of future research, we recognize that Step 3a of Algorithm 3 may require further investigation. In this step we pick out $\kappa$ candidate models to represent the search boundary, and then select a single model from this set. We plan to investigate the way the candidates are selected. In particular, the structure of a candidate model is determined by a conditional independence test, which is not necessarily related to the classification accuracy. Other methods may be considered (e.g., exhaustive search), and they should be compared to the effectiveness of the proposed heuristic. In an initial investigation, where we compared our results with the results of performing an exhaustive search, the heuristic showed good performance, but this should be examined more closely before any conclusions can be drawn. The same point can be made regarding the way state spaces are selected (Algorithm 2): Other methods can be envisioned, including exhaustive search as well as search algorithms based on greedily maximizing some score function for a fixed number of states.

## Appendix

## A. Empirical complexity results

In practice, the main computational effort of our algorithm goes into calculating the conditional mutual information (CMI) between all pairs of variables given the class variable (Step 3a of Algorithm 3). To give an indication of the (relative) run time complexity of the algorithm, we report on the number of times the algorithm calculates CMI ("CMI; HNB" in Table 3). These numbers are easiest to interpret relative to the TAN algorithm (Friedman et al., 1997) that also relies on CMI calculations ("CMI; TAN" in Table 3 ), i.e., the TAN algorithm may be considered a baseline used for comparison. Finally, the ratio between these two numbers is listed as the "CMI ratio". The CMI ratio is bounded below by $\kappa$, the number of candidate models used to represent the search boundary (recall that $\kappa=10$ in our experiments), and is also roughly linear in this value. For ease of reference, we have included information regarding the number of attributes ("\#Att") of each dataset. We also give the number of latent variables inserted by the algorithm ("\#Latent"), both as a range as well as a mean plus standard deviation.

In our experiments, Algorithm 3 has running times that are between 6 and 25 times those of the TAN algorithm when $\kappa=10$ is kept fixed; the running times include both learning and inference w.r.t. the test dataset. In particular, a ratio below 10 occurs when the average number of latent variables inserted by the HNB algorithm is close to zero, i.e., when we are working with an NB model where the time complexity for inference is smaller than that of a TAN model. It should be noted that these run-time ratios should not to be taken literally, but

Table 3 Number of times the HNB and TAN algorithms calculate conditional mutual information for given datasets; $\kappa=10$


rather be seen as indications of the run-time complexity: our implementation of the HNB algorithm is far from optimized and is implemented with focus on debugging capabilities.

# B. Accuracy results 

The detailed accuracy results for all the datasets are shown in Table 4. For each dataset we have estimated the accuracy of each classifier (in percentage of instances which are correctly classified). We note that the true ability of each classifier can only be calculated "correctly" if we know the probability distribution $P(C, A)$. As we only have datasets of limited sizes available, the estimated accuracies are random variables (the uncertainty stems from the fact that a dataset is only a sample from this unknown distribution). We therefore give a standard deviation of the accuracy estimate. The numbers we present are the theoretical values calculated according to Kohavi (1995), and are not necessarily the same as the empirical standard deviations observed during cross-validation.

The uncertainty in the estimated accuracies forces us to use a statistical test to decide if one classifier is better than another on a particular domain. We use Nadeau and Bengio (2003)'s corrected resampled t-test. This test takes the calculated accuracy on each cross-validation fold into consideration, and thereby tries to minimize the uncertainty of the estimate outlined above; the same cross-validation folds were given to all classification algorithms. The best result for each dataset is given in boldface. Results that are significantly poorer than the best on a given dataset at $10 \%$-level are marked with '*' . Results significant at $5 \%$-level are marked with ' $\because$ ', and $1 \%$-level with ' $\bullet$ '.

Table 4 Classifier accuracies


Calculated accuracy for the 22 datasets used in the experiments; the results are given together with their theoretical standard deviation. The adjusted $t$-test of Nadeau and Bengio (2003) was used to compare the classifiers: Results that are significantly poorer than the best on a given dataset at $10 \%$-level are marked with "* '. Results significant at $5 \%$-level are marked with ${ }^{\circ \prime}$, and $1 \%$-level with ${ }^{\circ \prime}$.

Acknowledgments We have benefited from interesting discussions with the members of the Machine Intelligence group at Aalborg University, in particular Tomás Kočka, and Jiří Vomlel. We thank Nevin L. Zhang for his valuable insight and for giving us access to his implementation of the HNB learning algorithm by Zhang et al. (2003), and the anonymous reviewers for very helpful comments on an earlier version of the paper. Finally, we would like to thank Hugin Expert (http://www.hugin.com/) for giving us access to the Hugin Decision Engine, which forms the basis of our implementation.
