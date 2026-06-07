# Boosted Bayesian network classifiers 

Yushi Jing $\cdot$ Vladimir Pavlović $\cdot$ James M. Rehg

Received: 16 December 2005 / Revised: 21 November 2007 / Accepted: 5 May 2008 /
Published online: 15 August 2008
Springer Science+Business Media, LLC 2008


#### Abstract

The use of Bayesian networks for classification problems has received a significant amount of recent attention. Although computationally efficient, the standard maximum likelihood learning method tends to be suboptimal due to the mismatch between its optimization criteria (data likelihood) and the actual goal of classification (label prediction accuracy). Recent approaches to optimizing classification performance during parameter or structure learning show promise, but lack the favorable computational properties of maximum likelihood learning. In this paper we present boosted Bayesian network classifiers, a framework to combine discriminative data-weighting with generative training of intermediate models. We show that boosted Bayesian network classifiers encompass the basic generative models in isolation, but improve their classification performance when the model structure is suboptimal. We also demonstrate that structure learning is beneficial in the construction of boosted Bayesian network classifiers. On a large suite of benchmark data-sets, this approach outperforms generative graphical models such as naive Bayes and TAN in classification accuracy. Boosted Bayesian network classifiers have comparable or better performance in comparison to other discriminatively trained graphical models including ELR and BNC. Furthermore, boosted Bayesian networks require significantly less training time than the ELR and BNC algorithms.


Keywords Bayesian network classifiers $\cdot$ AdaBoost $\cdot$ Ensemble models $\cdot$ Structure learning

[^0]
[^0]:    Editor: Zoubin Ghahramani.
    Y. Jing ( $\boxtimes$ ) J.M. Rehg

    College of Computing, Georgia Institute of Technology, Atlanta, GA 30332, USA
    e-mail: yjing@cc.gatech.edu
    J.M. Rehg
    e-mail: rehg@cc.gatech.edu
    V. Pavlović

    Department of Computer Science, Rutgers University, Piscataway, NJ 08854, USA
    e-mail: vladimir@cs.rutgers.edu

# 1 Introduction 

A Bayesian network is an annotated directed graph that encodes the probabilistic relationships among variables of interest (Pearl 1988). The explicit representation of probabilistic relations can exploit the structure of the problem domain, making it easier to incorporate domain knowledge in the model design. In addition, a Bayesian network has a modular and intuitive graphical representation which is very beneficial in decomposing a large and complex problem representation into several smaller, self-contained models for tractability and efficiency. Furthermore, the probabilistic representation combines naturally with the EM algorithm to address problems with missing data. These advantages of Bayesian networks and generative models as a whole make them an attractive modeling choice.

In many problem domains where a Bayesian network is applicable and desirable, we may want to infer the label(s) for a subset of the variables (class variables) given an instantiation of the rest (attributes). Bayesian network classifiers (Friedman et al. 1997) model the conditional distribution of the class variables given the attributes and predict the class with the highest conditional probability. Bayesian network classifiers have been applied successfully in many application areas including computational molecular biology (Segal et al. 2003; Pavlović et al. 2002; Jojic et al. 2004), computer vision (Torralba et al. 2004; Rehg et al. 2003; Schneiderman 2004), relational databases (Friedman et al. 1999), text processing (Cutting et al. 1992; McCallum et al. 2000; Lafferty et al. 2001), audio processing (Rabiner and Juang 1993) and sensor fusion (Pavlović et al. 2000). Its simplest form, the naive Bayes classifier, has received a significant amount of attention (Langley et al. 1992; Duda and Hart 1973; Ng and Jordan 2002).

However, standard Maximum Likelihood (ML) parameter learning in Bayesian network classifiers tends to be suboptimal (Friedman et al. 1997). It optimizes the joint likelihood, rather than the conditional likelihood, a score more closely related to the classification task. Unlike the joint likelihood, however, the conditional likelihood cannot be expressed in a log linear form, therefore no closed form solution is available to compute the optimal parameters. Recently there has been substantial interest in discriminative training of generative models coupled with advances in discriminative optimization methods for complex probabilistic graphical models (Greiner and Zhou 2002; McCallum et al. 2000; Lafferty et al. 2001; Chelba and Acero 2004; Altun et al. 2003; Taskar et al. 2004).

If the selected model structure contains the structure from which the data is generated, the parameters that maximize the likelihood also maximize the conditional likelihood (see p. 159). For this reason, structure learning (Cooper and Herskovits 1992; Heckerman 1995; Friedman and Koller 2000; Chickering and Heckerman 1997; Heckerman et al. 1995; Lam and Bacchus 1992) can potentially be used to improve the classification accuracy. However, experiments show that learning an unrestricted Bayesian network fails to outperform naive Bayes in classification accuracy on a large sample of benchmark data (Friedman et al. 1997; Grossman and Domingos 2004). Friedman et al. (1997) attribute this to the mismatch between the structure selection criteria (data likelihood) and the actual goal for classification (label prediction accuracy). They proposed Tree Augmented Naive Bayes (TAN), a structure learning algorithm that learns a maximum spanning tree from the attributes, but incorporates a naive Bayes model as part of its structure to bias the model towards the estimation of the conditional distribution. On the other hand, Keogh and Pazzani (1999) proposed Augmented Naive Bayes (ANC) algorithm that uses the 0-1 loss function as the optimization criteria in its heuristic search for the best $k$-tree Bayesian network classifiers. Recently proposed BNC-2P (Grossman and Domingos 2004) uses the conditional likelihood as optimization criteria in its structure search and is shown to outperform naive Bayes, TAN, and

generatively trained unrestricted networks. Although the structures in TAN and BNC-2P are selected discriminatively, the parameters are trained via ML training for computational efficiency.

In this work, we propose a new approach to the discriminative training of Bayesian networks. Similar to a standard boosting approach, we recursively form an ensemble of classifiers. However in contrast to situations where the weak classifiers are trained discriminatively, the "weak classifiers" in our method are trained generatively to maximize the likelihood of weighted data. Our approach has two benefits. First, ML training of generative models is dramatically more efficient computationally than discriminative training. By combining maximum likelihood training with discriminative weighting of data, we obtain a computationally efficient method for the discriminative training of a general Bayesian network. Second, our classifiers are constructed from generative models. This is important in many practical problems where domain knowledge can be readily encoded in the structure of the generative model.

This paper makes five contributions:

1. We introduce Boosted Augmented Naive Bayes ( $b \mathrm{AN}$ ), an approach to improving the classification accuracy of generative models. We demonstrate that $b \mathrm{AN}$ 's classification accuracy on a large suite of benchmark datasets is comparable or superior to competing methods such as naive Bayes, TAN and ELR.
2. We investigate alternative training strategies for constructing boosted Bayesian network classifiers and introduce a novel algorithm $b \mathrm{AN}_{\text {mix }}$ as a more efficient alternative to $b \mathrm{AN}$ due to its heterogeneous assembly of structures.
3. We study the manner in which the complexity of the Bayesian network structure affects the classification accuracy of the final boosted ensemble by comparing $b \mathrm{AN}$ against $b$ BNC-2P, $b$ TAN, and other alternative boosted Bayesian network classifiers. Our experiments highlight the importance of structure learning.
4. We demonstrate that $b \mathrm{AN}$ and $b \mathrm{AN}_{\text {mix }}$ are significantly faster to train than competing algorithms including ELR and BNC-2P. To ensure fairness, we implemented $b \mathrm{NB}, b \mathrm{AN}$, TAN, BNC-2P, $b$ TAN, $b$ BNC-2P and ELR algorithms such that they share a common code base in $\mathrm{C}++$. We optimized the common code base for efficiency. In addition, we optimized the published BNC-2P method to improve its training speed.
5. We describe a multiclass extension of the $b \mathrm{AN}$ algorithm based on AdaBoost.MH and AdaBoost.M2. The results further demonstrate the advantages of structure selection.

A preliminary version of a portion of the results in this paper appeared in (Jing et al. 2005). This paper differs from (Jing et al. 2005) in the following areas. We provide a detailed comparison against five alternative boosted Bayesian network learning algorithms to demonstrate that structure learning is crucial to the ensemble classification accuracy. We also investigate the effect of combining heterogeneous mixture of Bayesian network structures into one ensemble and propose $b \mathrm{AN}_{\text {mix }}$ as a more efficient alternative to $b \mathrm{AN}$. We provide additional experiments with simulated datasets (generated from more complex structures) to highlight the capability of $b \mathrm{AN}$ to explore the structure of the data distribution. We supplement the analysis of training cost in (Jing et al. 2005) with a thorough empirical evaluations and comparisons (Sect. 7, Fig. 9 to Fig. 11). We include both AdaBoost.MH and AdaBoost.M2 variations in our analysis of multi-class $b \mathrm{AN}$ algorithm. Finally, we provide a graphical interpretation of boosted Bayesian network classifier in Fig. 12 in the appendix.

This paper is divided into 8 sections. Sections 1 through 3 review the formal notations of Bayesian networks and parameter learning methodologies. Section 4 introduces AdaBoost as an effective way to improve the classification accuracy of naive Bayes. Section 5 extends this work to structure learning and proposes the $b \mathrm{AN}$ and $b \mathrm{AN}_{\text {mix }}$ structure learning

algorithm. Sections 6 and 7 contain the experiments and analysis for boosted naive Bayes, $b \mathrm{AN}$ and $b \mathrm{AN}_{\text {mix }}$ structure learning algorithm. The last three sections contain related works, conclusions and acknowledgments.

# 2 Bayesian Network Classifier 

A Bayesian network $B$ is a directed acyclic graph that encodes a joint probability distribution over a set of random variables $\mathbf{X}=\left\{X_{1}, X_{2}, \ldots, X_{N}\right\}$ (Pearl 1988). It is defined by the pair $B=\{G, \theta\} . G$ is the structure of the Bayesian network. $\theta$ is the vector of parameters that quantifies the probabilistic model. $B$ represents a joint distribution $P_{B}(X)$, factored over the structure of the network where

$$
P_{B}(X)=\prod_{i=1}^{N} P_{B}\left(X_{i} \mid P a\left(X_{i}\right)\right)=\prod_{i=1}^{N} \theta_{X_{i} \mid P a\left(X_{i}\right)}
$$

We set $\theta_{x_{i} \mid P a\left(x_{i}\right)}$ equal to $P_{B}\left(x_{i} \mid P a\left(x_{i}\right)\right)$ for each possible value of $X_{i}$ and each possible instantiation of the parent of $X_{i}, P a\left(X_{i}\right) .{ }^{1}$ For notational simplicity, we define a one-to-one relationship between the parameter $\theta$ and the entries in the local Conditional Probability Table. Given a set of i.i.d. training data $D=\left\{x^{1}, x^{2}, x^{3}, \ldots, x^{M}\right\}$, the goal of learning a Bayesian network $B$ is to find a $\{G, \theta\}$ that accurately models the distribution of the data. The selection of $\theta$ is known as parameter learning and the selection of $G$ is known as structure learning.

The goal of a Bayesian network classifier is to correctly predict the label for class $X_{c} \in \mathbf{X}$ given a vector of attributes $X_{a}=\mathbf{X} \backslash X_{c}$. A Bayesian network classifier models the joint distribution $P\left(X_{c}, X_{a}\right)$ and converts it to conditional distribution $P\left(X_{c} \mid X_{a}\right)$. Prediction for $X_{c}$ can be obtained by applying an estimator to the conditional distribution. For example, Maximum a Posteriori estimator (MAP) can be used to select the label associated with the highest conditional probability.

## 3 Parameter learning

The Maximum Likelihood (ML) method is one of the most commonly used parameter learning techniques. It chooses the parameter values that maximize the Log Likelihood (LL) score, a measure of how well the model represents the data. Given a set of training data $D$ with $M$ samples and a Bayesian Network structure $G$ with $N$ nodes, the LL score is decomposed as:

$$
\mathrm{LL}_{\mathrm{G}}(\theta \mid D)=\sum_{j=1}^{M} \log P_{\theta}\left(D^{j}\right)=\sum_{j=1}^{M} \sum_{i=1}^{N} \log \theta_{x_{i}^{j} \mid p a\left(x_{i}\right)^{j}}
$$

[^0]
[^0]:    ${ }^{1}$ We use capital letters to represent random variable(s) and lowercase letters to represent their corresponding instantiations. Subscripts are used as variable indices and superscripts are used to index the training data. $P a\left(X_{i}\right)$ represents the parent node of $X_{i}, p a\left(X_{i}\right)$ represents an instantiation of $P a\left(X_{i}\right)$ and $p a\left(X_{i}\right)^{j}$ is the instantiated value of $P a\left(X_{i}\right)$ in the $j$-th training data. In this paper, we assume all of the variables are discrete and fully observed in the training data.

$$
=M \sum_{i=1}^{N} \sum_{\substack{x_{i} \in X_{i} \\ p a\left(x_{i}\right) \in P a\left(x_{i}\right)}} \widehat{P}_{D}\left(x_{i}, p a\left(x_{i}\right)\right) \log \theta_{x_{i} \mid p a\left(x_{i}\right)}
$$

$\mathrm{LL}_{G}(\theta \mid D)$ is maximized by simply setting each parameter $\theta_{x_{i} \mid P a\left(x_{i}\right)}$ to $\widehat{P}_{D}\left(x_{i} \mid P a\left(x_{i}\right)\right)$, the empirical distribution of the data $D$. For this reason, ML parameter learning is computationally efficient and very fast in practice.

However, the goal of a classifier is to accurately predict the label given the attributes, a function that is directly tied to the estimation of the conditional likelihood. Instead of maximizing the LL score, we would prefer to maximize the Conditional Log Likelihood (CLL) score. As pointed out in (Friedman et al. 1997), the LL score factors as

$$
\mathrm{LL}_{\mathrm{G}}(\theta \mid D)=\mathrm{CLL}_{\mathrm{G}}(\theta \mid D)+\sum_{j=1}^{M} \log P_{\theta}\left(x_{a}^{j}\right)
$$

where

$$
\begin{aligned}
\mathrm{CLL}_{\mathrm{G}}(\theta \mid D) & =\sum_{j=1}^{M} \log P_{\theta}\left(x_{c}^{i} \mid x_{a}^{j}\right) \\
& =M \sum_{\substack{x_{a} \in X_{a} \\
x_{c} \in X_{c}}} \widehat{P}_{D}\left(x_{c}, x_{a}\right) \log P_{\theta}\left(x_{c} \mid x_{a}\right)
\end{aligned}
$$

Given a network structure G that encapsulates the true structure of the data, parameters that maximize $\mathrm{LL}_{G}$ also maximize $\mathrm{CLL}_{G} \cdot{ }^{2}$ However, in practice the structure may be incorrect and ML learning will not optimize the CLL score, which can result in a suboptimal classification decision. ${ }^{3}$

An alternative approach is to directly optimize Eq. 3, which is maximized when

$$
P_{\theta}\left(x_{c} \mid x_{a}\right)=\frac{\theta_{x_{c}} \prod \theta_{x_{a} \mid P a\left(x_{a}\right)}}{\sum_{x_{a}} \theta_{x_{c}} \prod \theta_{x_{a} \mid P a\left(x_{a}\right)}}=\widehat{P}_{D}\left(x_{c} \mid x_{a}\right)
$$

For a generative model such as a Bayesian network, Eq. 4 cannot be expressed in log-linear form and has no closed form solution. A direct optimization approach requires computationally expensive numerical techniques. For example, the ELR method of (Greiner and Zhou 2002) uses gradient descent and line search to directly maximize the CLL score. However, this approach is unattractive in the presence of a large feature space, especially when used in conjunction with structure learning.

[^0]
[^0]:    ${ }^{2}$ The asymptotic properties of likelihood and conditional likelihood learning is discussed in greater detail in (Nadas 1983).
    ${ }^{3}$ If G is incorrect, maximizing $\mathrm{CLL}_{G}$ may also lead to poor performance. However, LL score is more sensitive than CLL since it requires correct knowledge of the features (Devroye et al. 1996).

# 4 Boosted parameter learning 

### 4.1 Ensemble model

Instead of maximizing the CLL score for a single Bayesian network model, we take the ensemble approach and maximize the classification performance of the ensemble Bayesian network classifier. For binary classification, given a class $x_{c}$ and the attributes $x_{a}$, an ensemble model has the general form:

$$
F_{x_{c}}\left(x_{a}\right)=\sum_{k=1}^{K} \beta_{k} f_{k, x_{c}}\left(x_{a}\right)
$$

and $f_{k, x_{c}}\left(x_{a}\right)$ is the classifier confidence on selecting label $x_{c}$ given $x_{a}$ during boosting iteration $k$, and $\beta_{k}$ is its corresponding weight. In the case where $x_{c} \in\{-1,1\}, f_{k, x_{c}}\left(x_{a}\right)$ is typically defined as the following: $f_{k, x_{c}}\left(x_{a}\right)=x_{c} f_{k}\left(x_{a}\right)$, where $f_{k}\left(x_{a}\right) \in\{-1,1\}$ is the output of each classifier given $x_{a}$, and $F\left(x_{a}\right)$ is the ensemble of $f\left(x_{a}\right)$. Equation 4.1 can be expressed as a conditional probability distribution over $X_{c}$ given the additive model F with logistic transformation:

$$
P_{F}\left(x_{c} \mid x_{a}\right)=\frac{\exp \left\{F_{x_{c}}\left(x_{a}\right)\right\}}{\sum_{x_{c}^{\prime} \in X_{c}} \exp \left\{F_{x_{c}^{\prime}}\left(x_{a}\right)\right\}}
$$

For binary classification, Eq. 5 is then updated as:

$$
P_{F}\left(x_{c} \mid x_{a}\right)=\frac{1}{1+\exp \left\{-2 x_{c} F\left(x_{a}\right)\right\}}
$$

Instead of directly optimizing CLL, we minimize the often used Exponential Loss Function (ELF) of the ensemble Bayesian network classifier. ELF is defined as:

$$
\mathrm{ELF}_{F}=\sum_{i=1}^{M} \exp \left\{-x_{c}^{i} F\left(x_{a}^{i}\right)\right\}
$$

Solving for $x_{c} F\left(x_{a}\right)$ in Eq. 6 and combining with Eq. 7, we have

$$
\begin{aligned}
\mathrm{ELF}_{F} & =\sum_{i=1}^{M} \exp \left\{\frac{1}{2} \log \frac{1-P_{F}\left(x_{c}^{i} \mid x_{a}^{i}\right)}{P_{F}\left(x_{c}^{i} \mid x_{a}^{i}\right)}\right\} \\
& =M \sum_{\substack{r a \in X_{a} \\
x_{c} \in X_{c}}} \tilde{P}_{D}\left(x_{c}, x_{a}\right) \sqrt{\frac{1}{P_{F}\left(x_{c}, x_{a}\right)}-1}
\end{aligned}
$$

Equation 9 is a differentiable upper bound on the classification error, and an approximation to the negative CLL score (Friedman et al. 2000). ${ }^{4}$

[^0]
[^0]:    ${ }^{4}$ The ELF criteria has been demonstrated to be an effective classification error minimization criteria, and to perform well on real data. A detailed comparison of ELR and CLL can be found in (Friedman et al. 2000).

Table 1 Boosted parameter learning algorithm


# 4.2 Boosted parameter learning 

An ensemble Bayesian network classifier takes the form $F_{\theta, \beta}$ where $\theta$ is a collection of parameters in the Bayesian network model and $\beta$ is the vector of hypothesis weights. We want to minimize $\mathrm{ELF}_{\theta, \beta}$ of the ensemble Bayesian network classifier as an alternative way to maximize the CLL score. We used Discrete AdaBoost algorithm, which is proven to greedily and approximately minimize the exponential loss function in Eq. 9 (Friedman et al. 2000).

At $k$-th iteration of boosting, the weighted data uniquely determines the parameters for each Bayesian network classifier $\theta_{k}$ and the hypothesis weights $\beta_{k}$ via efficient ML parameter learning, where

$$
\beta_{k}=0.5 \log \frac{1-\operatorname{Err}_{k}}{\operatorname{Err}_{k}}, \theta_{k}\left(x_{a} \mid x_{c}\right)=\widehat{P}_{D_{k}}\left(x_{a} \mid x_{c}\right)
$$

where $\operatorname{Err}_{k}$ is the classification error on the weighted data. The full algorithm is shown in Table 1. There is no guarantee that AdaBoost will find the global minimum of the ELF. Also, AdaBoost has been shown to be susceptible to label noise (Dietterich 2000; Bauer and Kohavi 1999). In spite of these issues, boosted classifiers tend to produce excellent results in practice (Schapire and Singer 2000; Drucker and Cortes 1996). Boosted Naive Bayes (bNB) has been previously shown to improve the classification accuracy of naive Bayes (Elkan 1997; Ridgeway et al. 1998).

## 5 Structure learning

Given training data $D$, structure learning is the task of finding a set of directed edges $G$ that best model the true density of the data. In order to avoid overfitting, Bayesian Scoring Function (Cooper and Herskovits 1992; Heckerman et al. 1995) and Minimal Description Length (MDL) (Lam and Bacchus 1992) are commonly used to evaluate candidate structures. The MDL score is asymptotically equivalent to the Bayesian scoring function in the large sample case and this paper will concentrate on the MDL score. MDL score is defined as

$$
\operatorname{MDL}(B \mid D)=\frac{\log |D|}{2}|B|-\operatorname{LL}(B \mid D)
$$

where $|B|$ is the total number of parameters in model $B$, and $|D|$ is the total number of training samples.

Table 2 Boosted augmented naive Bayes $(b \mathrm{AN})$

1. Given training data $D$, construct a complete graph $G_{f u l l}$ with attributes $X_{a}$ as vertices. Calculate $I_{p}\left(X_{a_{i}} ; X_{a_{j}} \mid X_{c}\right)$ for each pair of attributes $X_{a}, i \neq j$, where

$$
I_{p}\left(X_{a_{i}} ; X_{a_{j}} \mid X_{c}\right)=\sum_{\substack{x_{a_{i}} \in X_{a_{i}}} \\ x_{a_{j}} \in X_{a_{j}}, x_{c} \in X_{c}}} P\left(x_{a_{i}}, x_{a_{j}}, x_{c}\right) \log \frac{P\left(x_{a_{i}}, x_{a_{j}} \mid x_{c}\right)}{P\left(x_{a_{i}} \mid x_{c}\right) P\left(x_{a_{j}} \mid x_{c}\right)}
$$

2. Construct $G_{T A N}$ from $G_{f u l l}$ with $I_{p}$ as weights, set $G_{1}=$ naive Bayes.
3. For $s=1$ to $N-1$

- Parameter boosting using $G_{s}$ as base structure.
- Evaluate the classification accuracy for the current $G_{b \mathrm{AN}}$ on training data $D$, and terminate if it stops decreasing.
- Else, remove the edge $\left\{X_{a_{i}} X_{a_{j}}\right\}$ containing the largest conditional mutual information $I_{p}\left(X_{a_{i}} ; X_{a_{j}} \mid X_{c}\right)$ from $G_{T A N}$ and add it to $G_{s}$.
- $G_{s+1}=G_{s}$.

4. Ensemble output: sign $\sum_{k=1}^{K} \beta_{k} f\left(x_{a} \mid \theta_{k}, G_{s}\right)$, where $K$ is the number of classifiers in the ensemble with $G_{s}$ as base structure.

An exhaustive search over all structures against an evaluation function can in principle find the best Bayesian network model, but in practice, since the structure space is super exponential in the number of variables in the graph, it is not feasible in nontrivial networks. Several tractable heuristic approaches have been proposed to limit the search space. The algorithms K2 (Cooper and Herskovits 1992) and MCMC-K2 (Friedman and Koller 2000) define a node ordering such that a directed edge can only be added from a high ranking node to a low ranking node. Heckerman et al. (1995) proposed a hill-climbing local search algorithm to incrementally add, remove or reverse an edge until a local optimum is reached.

An additional structure penalty is to simply limit the number of parents an attribute can have. Friedman et al. (1997), based on the approach in (Chow and Liu 1968), proposed an efficient algorithm to construct an optimal Tree Augmented Naive Bayes (TAN) based on the conditional mutual information among the features. In comparison to TAN, Augmented Bayesian Network Classifier (ANC) (Keogh and Pazzani 1999), has the flexibility to add fewer edges to Naive Bayes. An example of ANC classifier is shown in Fig. 1. TAN can be considered as a special case of ANC. All of the methods (K2, Heckerman's method, ANC and TAN) utilize standard ML parameter learning for simplicity and efficiency.

# 5.1 Boosted augmented naive Bayes $(b \mathrm{AN})$ 

Although the training complexity of parameter boosting is within a constant factor (Elkan 1997) of ML learning, combining parameter boosting with exhaustive structure search is still impractical. Even with a constrained search space, hill-climbing search and K2 algorithm must consider a large number of structures.

On the other hand, ANC and TAN support efficient learning by limiting the number of parents per attribute to two. TAN augments a standard naive Bayes classifier by adding up to $N-1$ additional edges between attributes. The additional edges are constructed from a maximal weighted spanning tree with attributes as vertices. The weights are defined as the conditional mutual information $I_{p}\left(X_{a_{i}} ; X_{a_{j}} \mid X_{c}\right)$ between two attributes $X_{a_{i}}, X_{a_{j}}$ given the

Fig. 1 An example of ANC, the dotted edges are structural extensions to naive Bayes Augmented Naive Bayes

![img-0.jpeg](img-0.jpeg) class node $X_{c}$ where

$$
I_{p}\left(X_{a_{i}} ; X_{a_{j}} \mid X_{c}\right)=\sum_{\substack{x_{c} \in X_{c} \\ x_{a_{i}} \in X_{a_{i}} x_{a_{j}} \in X_{a_{j}}}} P\left(x_{a_{i}}, x_{a_{j}}, x_{c}\right) \log \frac{P\left(x_{a_{i}}, x_{a_{j}} \mid x_{c}\right)}{P\left(x_{a_{i}} \mid x_{c}\right) P\left(x_{a_{j}} \mid x_{c}\right)}
$$

TAN learning algorithm constructs the optimal tree-augmented network $B_{T}$ that maximizes $\operatorname{LL}\left(B_{T} \mid D\right)$. However, the TAN model adds a fixed number of edges regardless of the distribution of the training data. If we can find a simpler model to describe the underlying conditional distribution, then there is usually less chance of over-fitting.

Our $b \mathrm{AN}$ learning algorithm extends the TAN approach using parameter boosting. Starting from a naive Bayes model, at iteration $s, b \mathrm{AN}$ greedily augments the current structure with the $s$-th edge having the highest conditional mutual information. We call the resulting structure $b \mathrm{AN}^{s}$. We then minimize the ELF score of the $b \mathrm{AN}^{s}$ classifier with parameter boosting. $b \mathrm{AN}$ terminates when the added edge does not improve the classification accuracy of the training data. Since TAN contains $N-1$ augmenting edges, $b \mathrm{AN}$ in worst case evaluates $N-1$ structures. This complexity is linear in $N$, in comparison to the polynomial number of structures examined by K2 or Hill-Climbing algorithms. Moreover, we find that in practice (as shown in Table 4) that $b \mathrm{AN}$ usually only adds a small number of edges to naive Bayes, significantly fewer than the competing algorithms like TAN, BNC-2P and BNC-MDL. As a result, the base Bayesian network structure constructed from $b \mathrm{AN}$ usually contains fewer edges than other competing structure learning algorithms, making it computationally very efficient. The algorithm is shown in Table 2.

# 5.2 Boosted augmented naive Bayes with heterogeneous mixture of structures $\left(b \mathrm{AN}_{\text {mix }}\right)$ 

The $b$ AN learning algorithm constrains all weak classifiers to share a homogeneous structure. In our previous work (Jing et al. 2005), this constraint was chosen partially to facilitate comparison with other Bayesian network classifiers. As a result, structure selection can be seen as a wrapper function to the parameter boosting.

This section explores techniques in learning an ensemble Bayesian network classifier with heterogeneous structures. Choudhury et al. (2002) explored the idea of combining the re-weighting of training data with structure selection during each iteration of boosting for dynamic Bayesian networks.

In our work, we employ the greedy strategy of incrementally adding edges to the base structure during iterations of boosting. The greedy structure learning algorithm, named

$b \mathrm{AN}_{\text {mix }}$, starts by constructing a TAN structure similar to the one proposed in $b \mathrm{AN}$. We sort the edges in TAN based on their conditional mutual information in descending order. Starting with naive Bayes, we apply parameter boosting on the initial structure until the weighted error is higher than $\epsilon .{ }^{5}$ This step is analogous to the first step of $b \mathrm{AN}$ (up to $S=1$ ). Next, we augment the current structure with the next "best" edge from TAN. However, instead of restarting a new round of parameter boosting with a new structure, we retain the ensemble generated so far, but train the new and more complex structure on the re-weighted data. The addition of a more complex structure, by better capturing the underlying distribution of the data, usually reduces the weighted error and allows boosting to continue. We iterate this process until the new structure does not improve the classification accuracy. In effect, we are incrementally generating an ensemble of sparsely connected, heterogeneous mixture of Bayesian network classifiers. The psudocode for $b \mathrm{AN}_{\text {mix }}$ is shown in Table 3.

There are two basic strategies that underly the $b \mathrm{AN}_{\text {mix }}$ algorithm. First, in order to avoid overfitting, we select edges parsimoniously to maintain the sparsity of our generatively trained Bayesian network classifiers. An edge is added to the structure only when the existing weak classifier can no longer effectively classify the weighted samples. Our second strategy is to add edges with the highest conditional mutual information from TAN, under the assumption that those edges, by capturing the most important relationship information in the data, have the most potential to contribute to the classification accuracy.

To assess the effectiveness of these two strategies, we formulated two alternative training algorithms. The first algorithm, $b \mathrm{AN}_{m i x(1)}$, tests the first strategy. Rather than waiting for boosting to converge, $b \mathrm{AN}_{m i x(1)}$ adds a new edge to the existing structure at each iteration of boosting. Therefore, each structure is used exactly once (hence the name $b \mathrm{AN}_{m i x(1)}$ ). $b \mathrm{AN}_{m i x(1)}$ terminates when the classification accuracy does not improve, or when the maximum number of edges have been added. The second algorithm, $b \mathrm{AN}_{m i x(r)}$, tests a random structure selection strategy. Instead of selecting the edge with the best conditional mutual information from TAN, it randomly selects an edge from TAN to add to the existing Bayesian network. The next two sections provide a detailed analysis of these three algorithms and demonstrate that $b \mathrm{AN}_{\text {mix }}$ outperforms $b \mathrm{AN}_{m i x(1)}, b \mathrm{AN}_{m i x(r)}$ and has comparable performance to $b \mathrm{AN}$. However, $b \mathrm{AN}_{\text {mix }}$ is more efficient to train than $b \mathrm{AN}$.

We also implemented the MCMC variation of K2 from Friedman and Koller (2000) to study the effect of combining structure optimization with parameter boosting. K2 is a greedy search algorithm which uses a known ordering of the nodes and a maximum limit on the number of parents for any node to constrain the search, and the MCMC variant samples from the space of node orderings. As we show in Sect. 6, in spite of its tremendous computational cost, MCMC K2 did not yield superior classification accuracy than $b \mathrm{AN}_{\text {mix }}$, further confirming the observation by Grossman and Domingos (2004) that exhaustive structure optimization offers little classification improvement when combined with discriminative parameter learning.

# 6 Experiments 

We evaluated the performance of $b \mathrm{NB}$ and variations of $b \mathrm{AN}$ on 23 datasets from the UCI repository (Blake and Merz 1998) and two artificial data sets, Corral and Mofn, designed by Kohavi and John (1997). Friedman et al. (1997), Greiner and Zhou (2002), Grossman

[^0]
[^0]:    ${ }^{5}$ We use $\epsilon=0.45$ in our experiments as the stopping criterion to reduce the number of model boosting rounds. No significant change in accuracy was observed compared to $\epsilon=0.50$.

Table 3 Boosted augmented naive Bayes with mixed structure

1. Given a base structure $G$ and the training data $D$, where $M$ is the number of training cases. $D=\left\{x_{c}^{1} x_{a}^{1}, x_{c}^{2} x_{a}^{2}, \ldots, x_{c}^{M} x_{a}^{M}\right\}$ and $x_{c} \in\{-1,1\}$.
2. construct a complete graph $G_{f u l l}$ with attributes $X_{a}$ as vertices. Calculate $I_{p}\left(X_{a_{i}} ; X_{a_{j}} \mid X_{c}\right)$ for each pair of attributes $X_{a}, i \neq j$, where

$$
I_{p}\left(X_{a_{i}} ; X_{a_{j}} \mid X_{c}\right)=\sum_{\substack{x_{a_{i}} \in X_{a_{i}}} \\ x_{a_{j}} \in X_{a_{j}}, x_{c} \in X_{c}}} P\left(x_{a_{i}}, x_{a_{j}}, x_{c}\right) \log \frac{P\left(x_{a_{i}}, x_{a_{j}} \mid x_{c}\right)}{P\left(x_{a_{i}} \mid x_{c}\right) P\left(x_{a_{j}} \mid x_{c}\right)}
$$

3. Construct $G_{T A N}$ from $G_{f u l l}$ with $I_{p}$ as weights.
4. Initialize the training data weights with $w_{i}=1 / M, i=1,2, \ldots, M$
5. Set the initial Bayesian network structure as $G_{1}=$ naive Bayes, and $G_{b \mathrm{AN}_{\text {mix }}}=\{ \}$.
6. Repeat for $k=1,2, \ldots$

- Given $G_{k}, \theta_{k}$ is learned through ML parameter learning on the weighted data $D$ at iteration $k$.
- Compute the weighted error, $\operatorname{Err}_{w}\left(G_{k}\right)=E_{w}\left[1_{x_{c} \neq f_{\theta_{k}}}\left(x_{a}\right)\right], \beta_{k}=0.5 \log \frac{1-\operatorname{Err}_{w}\left(G_{k}\right)}{\operatorname{Err}_{w}\left(G_{k}\right)}$.
- $G_{b \mathrm{AN}_{\text {mix }}}=\left\{G_{b \mathrm{AN}_{\text {mix }}}, G_{k}\right\}$
- If $\operatorname{Err}_{w}\left(G_{k}\right) \leq \epsilon$, update weights $w_{i}=w_{i} \exp \left\{-\beta_{k} x_{c}^{i} f_{\theta_{k}}\left(x_{a}^{i}\right)\right\}$ and normalize.
- Else, if $\operatorname{Err}\left(G_{b \mathrm{AN}_{\text {mix }}}\right)$ calculated from the training data D remains the same, terminate the loop; or remove the edge with the highest $I_{p}\left(X_{a_{i}} ; X_{a_{j}} \mid X_{c}\right)$ from $G_{T A N}$ and add to $G_{k}$.
- Set $G_{k+1}=G_{k}$.

7. Ensemble output: $\operatorname{sign} \sum_{k} \beta_{k} f\left(x_{a} \mid \theta_{k}, G_{k}\right)$
and Domingos (2004) and Pernkopf and Bilmes (2005) used this group of data sets as benchmarks for Bayesian network classifiers. We used hold-out test for larger data sets and 5 fold cross validation for smaller sets. ${ }^{6}$ To ensure fairness, we used Dirichlet prior Bayesian smoothing, with parameters identical to the ones from page 18 of Friedman et al. (1997) for all classifiers when appropriate. The data preparation, experimental set-up as well as Bayesian smoothing are the same as those used by Friedman et al. for the evaluation of TAN (Friedman 1997). Since the Wilcoxon Signed-Ranks Test is demonstrated to provide the most unbiased evaluations for comparing methods across multiple datasets (Demsar 2006), we also used it to generate confidence scores. All algorithms are implemented in $\mathrm{C}++{ }^{7}$

The abbreviations for competing algorithms are described below:

- $\boldsymbol{b} \mathbf{A N}_{M H}, \boldsymbol{b} \mathbf{A N}_{M 2}$ : Boosted Augmented Naive Bayes trained via AdaBoost.MH and AdaBoost.M2 algorithm respectively.
- NB: Naive Bayes.
- TAN: Tree Augmented naive Bayes (Friedman et al. 1997).
- BNC-2P: Discriminative structure selection via CLL score (Grossman and Domingos 2004).
- $\mathbf{E L R}_{N B}, \mathbf{E L R}_{T A N}$ : NB and TAN with parameters optimized for conditional log likelihood as in Greiner and Zhou (2002).

[^0]
[^0]:    ${ }^{6}$ We used hold-out test for "chess", "letter", "mofn", "satimage", "segment", "shuttle", "waveform," and 5 folds cross validation for the rest. We removed the data points with missing values and used prediscretization step in manner described by Dougherty et al. (1995).
    ${ }^{7}$ The $\mathrm{C}++$ code can be found at www.cc.gatech.edu/cpl/projects/boosted_bnc.html.

# 6.1 $b \mathrm{NB}$ on UCI datasets 

Table 4 on lists the average testing error and confidence score for each algorithm. Figure 2 contains the scatter plots which compare $b \mathrm{NB}$ against $\mathrm{NB}, \mathrm{TAN}, \mathrm{ELR}_{N B}$ and BNC-2P. In each plot, points above the diagonal line $y=x$ correspond to data sets for which $b \mathrm{NB}$ outperforms the competing algorithm. The average testing error is shown next to the name of the method.

As shown in Fig. 2(a), $b \mathrm{NB}$ has lower average testing error than NB. Figures 2(b) and 2(d) show that $b \mathrm{NB}$ has comparable classification accuracy to TAN and $\mathrm{ELR}_{N B}$. Also, we find BNC-2P, a discriminative structure learning algorithm, to slightly outperform $b \mathrm{NB}$. However, we will demonstrate in Sect. 7 that $b \mathrm{NB}$ is significantly faster to train than ELR and BNC-2P.

## $6.2 b \mathrm{AN}$ on simulated dataset

We demonstrate that when the model structure is incorrect, $b \mathrm{NB}$ and $b \mathrm{AN}$ algorithm can significantly outperform their generative counterparts. In datasets where there are strong correlation among attributes, $b \mathrm{AN}$ tends to produce more accurate classification performance than $b \mathrm{NB}$ by having the ability to capture the relationships in the model structure.

We generated two collections of data from the two binary Bayesian network models depicted in Fig. 3. In Model A, the variables form a Markov chain. Model B is similar to model A except it introduces an additional complexity by adding an edge between the class variable and the last feature variable. We varied the number of attributes and their parameter values to generate 25 datasets with different distributions. Since the attributes are correlated, naive Bayes can sometimes give a suboptimal classification boundary.

Figures 4 and 5 contain the one-standard-deviation error bars produced from different classifiers evaluated on data generated from structures A and B respectively. Figures 4(a), 4(b), 5(a) and 5(b) show that $b \mathrm{NB}$ and $b \mathrm{AN}$ have lower average testing errors than NB. We want to point out that in 6 out of the 25 datasets, the suboptimal posterior estimation by naive Bayes did not result in label prediction error. In those datasets, NB, $b \mathrm{NB}$ and $b \mathrm{AN}$ have similar testing error.

As shown in Fig. 4(c), with data generated from structure A, the average testing error for $b \mathrm{AN}$ is only slightly higher than that of $b \mathrm{NB}$. This is largely due to the simplicity of the Markov-chain model: $b \mathrm{AN}$ selected $b \mathrm{NB}$ as the best model (adding 0 edges) in 20 out of the 25 datasets. On the other hand, when data is generated from more complex structure B, $b \mathrm{AN}$ significantly outperforms $b \mathrm{NB}$ shown in Fig. 5(c) by adding additional model structures.

## $6.3 b \mathrm{AN}$ on UCI dataset

Table 4 and Fig. 6 contain the testing error and confidence scores comparing $b \mathrm{AN}$ against other Bayesian network classifiers on the UCI data described in the beginning of Sect. 6. Table 4 also contains the average number of edges added for each of the classifiers given a dataset. We implemented two variations of $b \mathrm{AN}$ for multi-class classification tasks. $b \mathrm{AN}_{M H}$ breaks a $D$ class problem into $D$ sets of binary classification tasks. $b \mathrm{AN}_{M 2}$ directly applies the AdaBoost.M2 algorithm to build a single ensemble for the multi-class problem. ${ }^{8} b \mathrm{AN}_{M 2}$ and $b \mathrm{AN}_{M H}$ have comparable classification performance.

[^0]
[^0]:    ${ }^{8} b \mathrm{AN}_{M 2}$ and $b \mathrm{AN}_{M H}$ are essentially the same for binary classification.


Table 4 (Continued)


![img-1.jpeg](img-1.jpeg)

Fig. 2 Scatter plots for experiments on 25 sets of UCI and artificial benchmark data. We also measure the significance of the error difference in a specific datasets between two competing algorithms. The number of statistically significant "winners" are accumulated and placed in parenthesis next to the name of the algorithm
$b \mathrm{AN}_{M 2}$ and $b \mathrm{AN}_{M H}$ chose very different base structures in our empirical study. On average, $b \mathrm{AN}_{M 2}$ selects 1 to 15 more augmenting edges than $b \mathrm{AN}_{M H}$. This result is not surprising since AdaBoost.MH algorithm divides a potentially difficult multi-class problem into several relatively easier binary classification problems, each of which can be sufficiently classified with a sparser boosted Bayesian network. On the other hand, $b \mathrm{AN}_{M 2}$ fits a single ensemble to the multi-class problem, requiring more descriptive base structure. This further validates the need for structure selection in the construction of boosted Bayesian network classifiers.

From Figs. 6(b) and 6(c), we can see that $b \mathrm{AN}$ algorithm significantly outperforms naive Bayes and slightly outperforms TAN. Also, $b \mathrm{AN}$ algorithm outperforms $\mathrm{ELR}_{N B}$ and $\mathrm{ELR}_{T A N} . b \mathrm{AN}$ has comparable classification accuracy with BNC-2P algorithm.

Fig. 3 We generated two collections of simulated datasets from structures A and B. Since feature variables are correlated, Naive Bayes can often produce sub-optimal classification accuracies
![img-2.jpeg](img-2.jpeg)
![img-3.jpeg](img-3.jpeg)
![img-4.jpeg](img-4.jpeg)

Fig. 4 Scatter plots for data generated from Structure A shown in Fig. 3. Each point in the graph represents the classification error for one particular model setting. $b \mathrm{NB}$ and $b \mathrm{AN}$ outperform NB in 19 out of the 25 simulated datasets. In the remaining 6 datasets, the suboptimal posterior estimation by naive Bayes did not result in label prediction error

As shown in Table 4, the average testing errors for $b \mathrm{AN}$ and $b \mathrm{NB}$ are 0.142 and 0.155 respectively. The differences is significant under Wilcoxon Signed-rank test. $b \mathrm{AN}$ has lower average testing error (difference of $0.5 \%-5 \%$ ) than $b \mathrm{NB}$ in 16 out of the 25 datasets. Fig-

![img-5.jpeg](img-5.jpeg)

Fig. 5 Scatter plots for data generated from Structure B shown in Fig. 3. As shown in (c), $b \mathrm{AN}$ outperforms $b \mathrm{NB}$ outperform NB in 17 out of the 25 simulated datasets. This demonstrates the importance of structure selection in the construction of boosted Bayesian network classifiers. Both $b \mathrm{AN}$ and $b \mathrm{NB}$ outperform naive Bayes
ure 6(a) shows that $b \mathrm{AN}$ outperforms $b \mathrm{NB}$ in 5 out of the 5 datasets with significant error differences. Since $b \mathrm{AN}$ generalizes $b \mathrm{NB}$, in several datasets (Mofn, Iris), the structure chosen by $b \mathrm{AN}$ is very similar to $b \mathrm{NB}$ (with 0 to 1 augmented edges). $b \mathrm{AN}$ is more beneficial in datasets where the conditional dependencies among attributes are complex (Letter). This is an interesting result since it shows that combining discriminative structure learning with parameter optimization seems to improve classification accuracy.

We would like to mention that $b \mathrm{AN}$ tends to produce poorly calibrated conditional distributions (CLL score) on the testing data. This supports the observation by Niculescu-Mizil and Caruana (2005) that boosting tends to do poorly on the calibration task. BNC-2P, on the other hand, has been demonstrated to produce an accurate calibration of the conditional distribution of the data.

# 6.4 Alternative boosted Bayesian network classifier on UCI dataset 

In this section, we study the performance of different boosted Bayesian network classifiers on the UCI datasets. We also measured the level of variance (data noise) in each of the 25 UCI datasets with method described in (Kohavi and Wolpert 1996), shown next to the name of the datasets. The abbreviations for competing algorithms are described below:

- $\boldsymbol{b A N}$ : Boosted Augmented naive Bayes. Each of the Bayesian network classifier in the ensemble shares a common structure.
- $\boldsymbol{b A N}_{\text {mix }}$ : Boosted Augmented naive Bayes with heterogeneous structures in the ensemble.
- $\boldsymbol{b} \mathbf{N B}, \boldsymbol{b} \mathbf{T A N}$ and $\boldsymbol{b} \mathbf{B N C - 2 P}$ : Apply AdaBoost to Naive Bayes and structure selected by TAN and BNC-2P algorithm.
- $\boldsymbol{b} \mathbf{A} \mathbf{N}_{\text {mix(1) }}$ and $\boldsymbol{b} \mathbf{A} \mathbf{N}_{\text {mix( }}$ are two alternative training algorithm for $b \mathrm{AN}_{\text {mix }}$ proposed in Section 5.2.
- $\boldsymbol{b} \mathbf{A} \mathbf{N}_{M C M C(K 2)}$ combines parameter boosting with the MCMC variation of K2 structure learning algorithm.

As shown in Table 5 and Fig. 7, $b \mathrm{AN}$ and $b \mathrm{AN}_{\text {mix }}$ significantly outperformed other boosted Bayesian network classifiers including $b \mathrm{NB}, b \mathrm{TAN}, b \mathrm{BNC}-2 \mathrm{P}, b \mathrm{AN}_{\text {mix(1) }}$ and $b \mathrm{AN}_{\text {mix }(r)}$. We believe that the experiment results provide strong evidence to validate

![img-6.jpeg](img-6.jpeg)

Fig. 6 Scatter plots of classification errors on UCI datasets. We also measure the significance of the error difference for each datasets between two competing algorithms. The number of statistically significant "winners" are accumulated and placed in parentheses next to the name of the algorithm. $b \mathrm{AN}$ outperforms NB , TAN, ELR-NB, ELR-TAN, and $b \mathrm{NB}$, and is comparable with BNC-2P

Table 5 Testing errors and confidence scores on the UCI datasets. Since we did not observe a significant difference in classification accuracy between $b \mathrm{AN}_{M H}$ and $b \mathrm{AN}_{M 2}$, we used $b \mathrm{AN}_{M 2}$ in this set of experiments. " $\Leftarrow$ " indicates the cases where $b \mathrm{AN}_{M 2}$ outperforms the competing model in a statistically-significant manner under the given test


Table 5 (Continued)


![img-7.jpeg](img-7.jpeg)

Fig. 7 Scatter plots of classification difference on UCI datasets. We also measure the significance of error difference for each datasets between two competing algorithms. The number of statistically significant "winners" are accumulated and placed in parenthesis next to the name of the algorithm. $b \mathrm{AN}_{\text {mix }}$ outperforms $b \mathrm{NB}, b \mathrm{TAN}, b \mathrm{BNC}-2 \mathrm{P}, b \mathrm{NB}, b \mathrm{AN}_{\text {mix }(1)}, b \mathrm{AN}_{\text {mix }(r)}$ and is comparable with $b \mathrm{AN}$

Table 6 Classification error on the testing data. We divided the 25 datasets into three categories (each containing 7 to 9 sets) with respect to its classification variance (noise). For each category, the first row contains the testing error, and the second row is the error difference between each competing algorithm and $b \mathrm{AN}$ (positive differences correspond to lower error for $b \mathrm{AN}$ ). $b \mathrm{AN}$ significantly outperforms $b \mathrm{TAN}$ and $b \mathrm{BNC}-2 \mathrm{P}$ in datasets with variance by having a sparser structure. Also, $b \mathrm{AN}$ is relatively resistant to noise, demonstrated by having comparable performance with $b \mathrm{NB}$ in datasets with mid or high variances


the two basic strategies used in our formulation of boosted Bayesian network classifiers.

First, structures are beneficial in improving the performance of boosted Bayesian network classifiers. For example, $b \mathrm{AN}$ significantly outperformed $b \mathrm{NB}$, especially in data-sets where features are highly correlated with each other (such as Letter, etc). Also, $b \mathrm{AN}_{\text {mix }}$ significantly outperformed $b \mathrm{AN}_{\text {mix }(r)}$. We observed in the experiment that the edges randomly selected by $b \mathrm{AN}_{\text {mix }(r)}$ often did not improve the classification accuracy on the training data. As a result, $b \mathrm{AN}_{\text {mix }(r)}$ usually terminated in the early stage of structure selection, with similar classification performance and model structures as $b \mathrm{NB}$.

Second, since AdaBoost can overfit on noisy datasets, parsimonious structure selection provides the best compromise between modeling the structure of the data and controlling the classifier capacity. For example, both $b \mathrm{AN}$ and $b \mathrm{NB}$ significantly outperform $b \mathrm{BNC}-2 \mathrm{P}$ and $b \mathrm{TAN}$. This is also observed in the comparison between $b \mathrm{AN}_{\text {mix }}$ and $b \mathrm{AN}_{\text {mix }(1)}$. In noisy datasets like "Australian" and "crx", $b \mathrm{AN}_{\text {mix(1) }}$, having a larger number of edges, performs significantly worse than $b \mathrm{AN}_{\text {mix }}$. Table 6 divides the datasets into three categories based on the classification variance in the data. It is evident that $b \mathrm{AN}$ and $b \mathrm{AN}_{\text {mix }}$ significantly outperform $b \mathrm{TAN}$ and $b \mathrm{BNC} 2 \mathrm{P}$ in the noisy datasets in Table 6.

Also, the combination of structure optimization with boosting $b \mathrm{AN}_{\text {mcmc }(k 2)}$ does not outperforms $b \mathrm{AN}_{\text {mix }}$. On the contrary, $b \mathrm{AN}_{\text {mix }}$ slightly outperforms $b \mathrm{AN}_{\text {mcmc }(k 2)}$ on datasets with larger variance, an indication that $b \mathrm{AN}_{\text {mix }}$ is more resistant to overfitting.

# 7 Comparison of computational cost 

### 7.1 Computational complexity of $b \mathrm{NB}$ and $b \mathrm{AN}$

Given a naive Bayes classifier with $N$ attributes and training data with $M$ samples, the ML training complexity is $O(N M)$, which is optimal when every attribute is observed and used for classification. Parameter boosting for a naive Bayes model is $O(N M T)$ where $T$ is the number of iterations of boosting. In our experiments, boosting seems to give good performance with a constant number (10-30) of iterations irrespective of the number of attributes (ranging from 5 to 50). This is consistent with the finding of Elkan (1997).
$b \mathrm{AN}$ has a higher training complexity than $b \mathrm{NB}$. Step 1 in the $b \mathrm{AN}$ algorithm has the computational complexity $O\left(N^{2} M\right)$, where $N$ is the number of attributes and $M$ is the

amount of training data. Since we only add a maximum of $N-1$ edges to the network, steps 2-4 have a worst case complexity $O\left(N M T S_{\max }\right)$, where $S_{\max }$ is the number of structures analyzed. Therefore $b \mathrm{AN}$ has $O\left(N^{2} M+N M T S_{\max }\right)$ complexity. In our experiments, $b \mathrm{AN}$ evaluates a very small number of additional structures as base structure. ${ }^{9}$ Therefore, $b \mathrm{AN}$ is very efficient in practice.
$b \mathrm{AN}_{\text {mix }}$ on the other hand, has similar computational complexity as $b \mathrm{AN}$. However, since $b \mathrm{AN}_{\text {mix }}$ incrementally add new structures into the existing ensemble, $b \mathrm{AN}_{\text {mix }}$ does not evaluate each new structure in all $T$ steps as in $b \mathrm{AN}$. Therefore, the computational complexity for $b \mathrm{AN}_{\text {mix }}$ is $O\left(N^{2} M+N M T k S_{\max }\right)$, where $k<1$. We will show in the next section that $b \mathrm{AN}_{\text {mix }}$ indeed requires less classifier evaluations than $b \mathrm{AN}$.

# 7.2 Empirical analysis of computational cost 

The variations in possible optimization schemes make a theoretical comparison of the training cost for different Bayesian network classifiers challenging. Therefore we employ empirical training time in our analysis. All of the algorithms are implemented in C++ to share common code bases. The experiments were conducted on a cluster of 3 GHz machines.

BNC-2P has previously been shown to be computationally expensive in training (Pernkopf and Bilmes 2005). However, in cases where data the are fully observed, there are two ways to reduce the training cost. First, we can pre-compute the ML parameter values for all possible edges such that parameter learning given a structure becomes simple indexing. Second, since Heckerman's greedy structure search algorithm is an incremental process, we can avoid full inference in classifier evaluation by only partially updating the posterior. We denote the optimized implementation as BNC-2P-FAST. Figure 8 shows the training time comparison between BNC-2P-FAST and the original BNC algorithm on a small collection of UCI datasets. BNC-2P-FAST is roughly 2 orders of magnitude faster than BNC. However, the speedup is not possible when used in conjunction with the EM algorithm to handle missing data.

By taking advantage of the ensemble learning, boosted Bayesian network classifiers avoided the expensive process of structure and parameter optimization. Figure 9 shows the convergence rates for $b \mathrm{AN}$, ELR and BNC-2P-FAST algorithm on the "Chess" dataset. Compared with other UCI datasets, Chess data-set contains a large number of features, making parameter and structure optimization particularly expensive. Here, $b \mathrm{AN}$ is roughly 15 times faster than ELR and BNC-2P-FAST. This speedup is attributed to the lower training cost per iteration of boosting comparing with structure or parameter search. $b \mathrm{AN}$ only requires a single classifier evaluation for each iteration of boosting. On the other hand, both BNC-2P and ELR algorithm require numerous classifier evaluations (plus the costly computation of gradient for ELR).

A more detailed comparison is shown in Table 7. We divided the 25 datasets into two parts based on their relative sample size and number of attributes. ${ }^{10}$ We also itemized the individual training time for "large" datasets as shown in Figs. 10(a) and 10(b). As shown in Table 7, in larger datasets, $b \mathrm{NB}$ is roughly a factor of 20 faster than ELR and a factor of 50 faster than BNC-2P-FAST algorithm.

Also shown in Figs. 10(a) and 10(b), $b \mathrm{AN}$ is 2 to 5 times faster than ELR, and 2 to 20 times as fast as than BNC-2P-FAST. Also, BNC-2P-FAST is only applicable when all

[^0]
[^0]:    ${ }^{9}$ As shown in Table $4, b$ AN evaluates an average of less than 2 additional structures.
    ${ }^{10}$ We categorize datasets containing 2000 or more data points or 30 or more features as "large" datasets, the rest as "small" datasets.

Fig. 8 Training time for an optimized version of BNC algorithm based on caching the parameters for structure evaluation. As a result, the optimized version of BNC-2P (BNC-2P-FAST) enjoys 2 orders or magnitude improvement in training efficiency
![img-8.jpeg](img-8.jpeg)

Fig. 9 Classification error on the training data converges faster with $b \mathrm{AN}$ than ELR and BNC
![img-9.jpeg](img-9.jpeg)

Table 7 The training time comparison between $b \mathrm{AN}$ and competing algorithms, in seconds


We define large-dataset as those with more than 2000 data points or more than 30 features
data are fully observed. In case of missing data, we can only use BNC-2P, which has a computational cost roughly 2 orders of magnitude larger than $b \mathrm{AN}$. On the other hand, $b \mathrm{AN}$ can simply replace ML parameter learning with EM.

Figure 11 demonstrates that $b \mathrm{AN}_{\text {mix }}$ can significantly reduce the number of classifier evaluation in the construction of boosted Bayesian network classifiers. Instead of re-constructing a new ensemble at each iteration of structure search, $b \mathrm{AN}_{\text {mix }}$ keeps the

![img-10.jpeg](img-10.jpeg)
(a) $b \mathrm{NB}$ is roughly a factor of 20 faster than ELR and a factor of 50 faster than BNC-2P-FAST algorithm.
![img-11.jpeg](img-11.jpeg)
(b) $b \mathrm{AN}$ is 2 to 5 times faster than ELR, and 2 to 20 times faster than BNC-2P-FAST

Fig. 10 A break down of training time on large datasets

Bayesian network classifiers generated so far and the new structure only has to model the underlying distribution of data incorrectly classified by the previous classifiers. This strategy avoids reclassifying data points that are far away from boundaries with the new structure. Since $b \mathrm{AN}_{\text {mix }}$ and $b \mathrm{AN}$ are comparable in classification accuracy, we believe reduced computational complexity is the main benefit of $b \mathrm{AN}_{\text {mix }}$.

# 8 Discussion and conclusion 

This paper proposes a family of boosting models to improve Bayesian Network classifier framework to improve the classification accuracy of Bayesian network classifiers. Our experiments demonstrate that boosted parameter optimization in conjunction with greedy structure optimization can improve the classification performance. Unlike previous experiments results that combining ELR with structure learning (Greiner and Zhou 2002), we

![img-12.jpeg](img-12.jpeg)

Fig. 11 In cases where $b \mathrm{AN}$ augments naive Bayes with a significant number of edges ("letter", "satimage"), $b \mathrm{AN}_{\text {mix }}$ can significantly reduce the number of classifier evaluations by incrementing adding more complex structures into the ensemble, without re-starting boosting given each new structure
find significant benefit in combining parameter boosting with structure learning. However, full structure search at each stage of boosting can be both computationally expensive and counterproductive-better performance and less overfitting can be achieved when additional edges are gradually and parsimoniously added to the Bayesian network structure in the course of boosting.

We attribute the success of our approach to the following two reasons. First, $b \mathrm{AN}$ takes advantage of AdaBoost's resistance to over-fitting (Schapire and Singer 1999) and the variance reduction and bias reduction property of ensemble classifiers (Webb and Zheng 2004). Also, as a result of the parameter boosting, the base Bayesian network classifier constructed by $b \mathrm{AN}$ is simpler than BNC-2P and TAN. In our experiments, $b \mathrm{AN}$ adds 2 edges to naive Bayes on average while BNC-2P typically adds more than 10 edges.

We believe that the primary advantage of our approach is its simplicity and computational efficiency that scales well in datasets with large class cardinality and feature space dimension, coupled with its good performance in practice. Its use of weighted maximum likelihood parameter learning uniquely determines the parameters of the Bayesian network (in contrast to minimizing a non-convex loss function in ELR), providing an efficient mechanism for discriminative training.

One of the main advantages of using generative models for classification is the ease of encoding domain knowledge into the classifier design. $b \mathrm{AN}$ relies on the construction of TAN to provide an initial set of structure candidates. However, a user can readily translate his or her domain knowledge into a collection of structure candidates, from which the $b \mathrm{AN}$ algorithm forms the boosted Bayesian network classifier. In particular, in classification situations where domain information is potentially incomplete or noisy, instead of designing (or learning) a single model, the users may encode the most obvious (and likely to be correct) dependence relationships, while leaving the rest to the discriminative training via AdaBoost.

Our future work will focus on further studying the effects of combining boosting with Bayesian network structure selection. On important issue, in particular, is to understand the relationship between complex Bayesian network structures and the approximate decision boundaries learned by $b \mathrm{AN}$ from the data generated by those distributions.

Acknowledgements The authors would like to thank Matt Mullin for several fruitful discussions and for suggesting the chain-structured model in Fig. 3. We would like to thank S. Charles Brubaker for his help in constructing the factor graph in Fig. 12. We would also like to thank Pedro Domingos for his helpful suggestions on improving the speed and performance of the BNC-2P algorithm.

This material is based upon work which was supported in part by the National Science Foundation under NSF Grant IIS-0205507 and IIS-0413105.

# Appendix: Graphical representation of boosted Bayesian network classifier 

In Fig. 12, we present a graphical representation of boosted Bayesian network classifiers using a factor graph. In addition to the class variable $X_{c}$ and feature variables $X_{a}$, we introduce two sets of hidden variables, $W$ and $Z . W_{k} \in[0,1]$ corresponds to the estimated posterior of the Bayesian network classifier at the $k$ th iteration of boosting. $Z_{k} \in\{-1,1\}$ is the estimated class label after applying MAP estimation to $W_{k} .{ }^{11}$ For binary classification, we use $t$ as the threshold. The factorized functions are written as the following:

$$
\begin{aligned}
& f 1_{k}=\delta\left(w_{k}, \frac{P_{\theta_{k}}\left(x_{c}, x_{a}\right)}{\sum_{x_{c} \in X_{c}} P_{\theta_{k}}\left(x_{c}, x_{a}\right)}\right) \\
& f 2_{k}=\delta\left(z_{k}, \chi\left(w_{k}>t\right)\right), \quad \chi\left(w_{k}>t\right)=\left\{\begin{array}{ll}
1 & \text { if } w_{k}>t \\
-1 & \text { if } w_{k} \leq t
\end{array}\right\} \\
& f 3_{k}=\exp \left[\beta_{k} z_{k} x_{c}\right]
\end{aligned}
$$

The joint distribution of above factor graph can be written as the follows:

$$
\begin{aligned}
P^{*}\left(x_{c}, x_{a}\right) & =\sum_{z \in Z} \int_{w \in[0,1]} P^{*}\left(x_{c}, x_{a}, z, w\right) \\
& =\sum_{z \in Z} \int_{w \in[0,1]} \prod_{k} \exp \left[\beta_{k} z_{k} x_{c}\right] \delta\left(z_{k}, \chi\left(w_{k}>t\right)\right) \delta\left(w_{k}, P_{\theta_{k}}\left(x_{c} \mid x_{a}\right)\right)
\end{aligned}
$$

Fig. 12 Representing boosted naive Bayes (binary class) as factor graphs
![img-13.jpeg](img-13.jpeg)

[^0]
[^0]:    ${ }^{11}$ We want point out that variables $W$ and $Z$ are deterministic given the instantiation of the features.

$$
=\prod_{k} \exp \left[\beta_{k} \psi_{k} x_{c}\right], \quad \text { where } \psi_{k}=\chi\left(P_{\theta_{k}}\left(x_{c} \mid x_{a}\right)>t\right)
$$

where $\delta$ refers to Kronecker delta function.
The ratio of the conditional distribution can then be expressed as:

$$
\begin{aligned}
\frac{P^{*}\left(x_{c}=1 \mid x_{a}\right)}{P^{*}\left(x_{c}=-1 \mid x_{a}\right)} & =\frac{P^{*}\left(x_{c}=1, x_{a}\right)}{P^{*}\left(x_{c}=-1, x_{a}\right)}=\prod_{k} \frac{\exp \left[\beta_{k} \psi_{k}\right]}{\exp \left[-\beta_{k} \psi_{k}\right]}=\prod_{k} \exp \left[2 \beta_{k} \psi_{k}\right] \\
& =\prod_{k} \exp \left[\psi_{k} \log \frac{1-\operatorname{err}_{k}}{\operatorname{err}_{k}}\right]=\prod_{k}\left(\frac{1-\operatorname{err}_{k}}{\operatorname{err}_{k}}\right)^{\psi_{k}}
\end{aligned}
$$

Equation 15 represents the posterior ratio of Discrete AdaBoost. We want to also point out that given the values for $\psi$, Eq. 15 has similar functional form as naive Bayes under certain constraints. ${ }^{12}$
