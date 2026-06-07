# A Unified View of Causal and Non-causal Feature Selection 

Kui Yu<br>Lin Liu<br>Jiuyong Li<br>School of Information Technology and Mathematical Sciences<br>University of South Australia<br>Adelaide, 5095, SA, Australia

YKUI713@GMAIL.COM<br>Lin.Liu@unisa.edu.au<br>Jiuyong.Li@unisa.edu.au

Editor:


#### Abstract

In this paper, we aim to develop a unified view of causal and non-causal feature selection methods. The unified view will fill in the gap in the research of the relation between the two types of methods. Based on the Bayesian network framework and information theory, we first show that causal and non-causal feature selection methods share the same objective. That is to find the Markov blanket of a class attribute, the theoretically optimal feature set for classification. We then examine the assumptions made by causal and non-causal feature selection methods when searching for the optimal feature set, and unify the assumptions by mapping them to the restrictions on the structure of the Bayesian network model of the studied problem. We further analyze in detail how the structural assumptions lead to the different levels of approximations employed by the methods in their search, which then result in the approximations in the feature sets found by the methods with respect to the optimal feature set. With the unified view, we are able to interpret the output of non-causal methods from a causal perspective and derive the error bounds of both types of methods. Finally, we present practical understanding of the relation between causal and non-causal methods using extensive experiments with synthetic data and various types of real-word data.


Keywords: Causal feature selection, Non-causal feature selection, Mutual information, Markov blanket, Bayesian network

## 1. Introduction

Feature selection is to identify a subset of features (predictor variables) from the original features for model building or data understanding (Guyon and Elisseeff, 2003; Liu and Yu, 2005). In the big data era, feature selection is more pressing than ever, since highdimensional datasets have become ubiquitous in various applications (Zhai et al., 2014). For example, in cancer genomics, a gene expression dataset can contain tens of thousands of features (genes). For another example, the Webb Spam Corpus 2011 has a collection of approximately 16 million features for web spam detection (Wang et al., 2012). The high dimensionality not only incurs high computational cost and memory usage, but also deteriorates the generalization ability of prediction models (Brown et al., 2012). Therefore, many feature selection methods have been proposed, and they fall into three main categories, filter, wrapper, and embedded methods (Li et al., 2016). While filter feature se-

lection methods are classifier or prediction model agnostic, the other two types of methods are classifier dependent. With the rapid increase of high dimensional data, filter feature selection methods are attracting more attentions than ever, because of their fast processing speed, independence of prediction models, and robustness against overfitting (i.e. no bias on specific prediction models). In this paper, we focus on filter methods, and in the rest of this paper, feature selection refers to filter feature selection, unless otherwise mentioned.

In the last two decades, feature selection has been well studied and has achieved great successes in building high quality classification models. In classical feature selection, an input feature is considered as a strongly relevant feature, a weakly relevant feature, or an irrelevant feature with respect to a class attribute (Kohavi and John, 1997), and the methods aim to find the strongly relevant features of the class attribute. To achieve this goal, typically, a classical feature selection method will rank the features according to their relevance to the class attribute, and then iteratively selects for inclusion the top $\psi$ most relevant features (Guyon and Elisseeff, 2003).

An emerging feature selection approach is to identify a Markov blanket (MB) of the class attribute (Koller and Sahami, 1995; Guyon et al., 2007; Aliferis et al., 2010a,b). The notion of MB was invented by Pearl (Pearl, 1988, 2014) under the framework of causal Bayesian network (CBN). The MB of a variable in a CBN consists of its parents (direct causes), children (direct effects), and spouses (other parents of this variable's children) (For an exemplar MB, please see Figure 1 in Section 3). By tying feature predictive power and causality together, the MB discovery approach to feature selection can achieve more parsimonious feature subset than classical feature selection methods, thus lead to more interpretable and robust prediction models (Guyon et al., 2007). Since the MB discovery approach explicitly induces local causal relations between a class attribute and the features while classical feature selection methods do not, in this paper, we call the MB discovery approach causal feature selection while the classical (filter) feature selection approach noncausal feature selection (Guyon et al., 2007; Aliferis et al., 2010a).

A series of causal feature selection algorithms, such as IAMB (Tsamardinos and Aliferis, 2003), MMMB (Tsamardinos et al., 2003a), HITON-MB (Aliferis et al., 2003), PCMB (Peña et al., 2007), and STMB (Gao and Ji, 2017) have been developed. Tsamardinos et al. (Tsamardinos and Aliferis, 2003) were the first to build the connection between local causal discovery and feature selection, which opened the way to study the relation of causal and non-causal feature selection methods. Guyon et al. (Guyon et al., 2007) conducted a comparison of the motivations and pros/cons of causal and non-causal feature selection approaches. However, the analysis was at conceptual and general discussion level. Brown et al. (Brown et al., 2012) unified information theoretic feature selection methods. These pioneer work provides a basis of studying causal and non-causal feature selection methods. However, to the relations between the two major approaches to feature selection, the following fundamental questions are yet to be investigated:

- Firstly, what is the relation between the objectives of causal feature selection and non-causal feature selection, i.e. what is the relation between the set of all features strongly relevant to the class attribute and finding the MB of the class attribute?
- Secondly, driven by their respective objectives, how are the search strategies employed by the two types of feature selection methods different?

- Thirdly, what are the underlying assumptions leading to the different search strategies?

To answer these questions, in this paper, we develop a unified view of causal and noncausal feature selection by systematically studying the relation between the two approaches from the perspectives of their objective functions, assumptions, search strategies, and the error bounds by employing the Bayesian network framework and information theory. Specifically, we have made the following contributions in this paper:

- We derive a mutual information based representation of the optimal feature set for classification. Based on the representation, we develop a unified representation of the objective function of causal and non-causal feature selection by showing that both types of methods share the same objective.
- We analyze the assumptions made by the major causal and non-causal feature selection methods in their search for the feature set specified by the objective function. Our findings show that these assumptions can be unified under the Bayesian network framework, and the assumptions can be represented as different levels of restrictions on the structure of the Bayesian network model of the problem under consideration.
- We analyze the search strategies of the causal and non-causal feature selection methods, and discover that as a result of the different levels of assumptions, different search strategies have been taken by the methods, which then result in different levels of approximations of the optimal feature set.
- We analyze the output of non-causal feature selection methods from a causal perspective and derive the error bounds of the two major approaches to feature selection.
- We conduct extensive experiments using synthetic and real-world datasets to validate the relationship between the assumptions and approximations made by causal and non-causal feature selection methods, the causal interpretations of non-causal feature selection, and the derived error bounds of both types of feature selection methods.

In summary, we propose a unified view to bridge the gap in current understanding of the relation between causal and non-causal feature selection methods. With the unified view, we are able to understand the mechanisms of two major feature selection approaches, and thus to connect causality to predictive feature selection and interpret the output of non-causal methods using a causal framework. Moreover, by filling in the gap, we hope to leverage the cross-pollination between causal and non-causal feature selection to develop new methodologies promising to deliver more robust data analysis than each field could individually do.

The rest of the paper is organized as follows. Section 2 discusses the related work, and Section 3 presents the key notations and definitions. Section 4 analyzes the objective functions and the rationale of causal and non-causal feature selection methods. Section 5 identifies and examines the assumptions made by causal and non-causal feature selection methods and their corresponding search strategies. Section 6 discusses the error bounds of causal and non-causal feature selection methods. Section 7 presents the experiments and demonstrates how the developed unified view provides practical understanding the relations between causal and non-causal feature selection methods, and Section 8 concludes the paper.

# 2. Related work 

In this section, we will review causal and non-causal (filter) feature selection methods. Excellent reviews of non-causal feature selection (i.e. filter, embedded, wrapper) algorithms can be found in (Guyon and Elisseeff, 2003; Liu and Motoda, 2007; Brown et al., 2012; Li et al., 2016) and the reference therein.

### 2.1 Non-causal feature selection

A general filter feature selection method consists of two elements: a search strategy for feature subset generation and an evaluation criterion for measuring relevance of the features. This evaluation criterion is to estimate how useful a feature or a feature subset may be when used in a learning algorithm (e.g. a classifier). As the feature selection by a filter method is carried out separately from the process of learning a model, an effective evaluation criterion plays a key role in filter methods. In the past decades, different evaluation criteria have been proposed, such as those based on distance (Kira and Rendell, 1992; Robnik-Šikonja and Kononenko, 2003), mutual information (Bontempi and Meyer, 2010; Nguyen et al., 2014; Shishkin et al., 2016), dependency (Song et al., 2012), and consistency (Dash and Liu, 2003). Since mutual information is a general measure of feature relevance with several unique properties (Cover and Thomas, 2012), there has been a significant amount of work on mutual information-based feature selection methods developed in the past two decades (see (Brown et al., 2012; Vergara and Estévez, 2014) for an exhaustive list).

In this paper, we use mutual information as a basic tool to develop the unified view, so in this section, we focus on non-causal feature selection methods which are based on mutual information. Many advances in the field have been reported since the pioneer work of Lewis (Lewis, 1992) and Battiti (Battiti, 1994). Lewis proposed the MIM (Mutual Information Maximisation) criterion. MIM simply ranks the features in order of their MIM scores (i.e. the value of mutual information between a feature and the class attribute) and selects the top $\psi$ most relevant features from the original feature set. However, MIM only considers feature relevance. Then Battiti proposed the MIFS (Mutual information Feature Selection) criterion which not only considers feature relevance, but also adds a penalty for feature redundancy. MIFS uses a greedy search to select features sequentially (i.e. a single feature at a time), and iteratively constructs the final feature subset, as an alternative to the evaluation of the combinatorial explosion of all subsets of features.

Based on the MIFS criterion, many variants have been proposed. The representative algorithms include mRMR (Peng et al., 2005), CIFE (Lin and Tang, 2006), FCBF (Yu and Liu, 2004), mIMR (Bontempi and Meyer, 2010), and MRI (Wang et al., 2017). Yang and Moody proposed the JMI (Joint Mutual Information) criterion (Yang and Moody, 2000). Compared to the MIFS criterion, the JMI criterion considers complementary information between features by evaluating class-conditional relevance, to see if a feature would provide more predictive information when it is used jointly with other features in the prediction compared with the case when the feature is used alone. The IF (Vidal-Naquet and Ullman, 2003), DISR (Meyer et al., 2008), CMIM (Fleuret, 2004), and RelaxMRMR (Vinh et al., 2016) methods can be considered as the variants of the JMI criterion. Brown et al. (Brown et al., 2012) unified almost two decades of research on commonly used heuristics of mutual infor-

mation based feature selection methods into the framework of conditional likelihood maximisation.

Owing to the difficulty of estimating mutual information with high dimensional data, most existing mutual information-based methods use various low-order approximations for estimating mutual information. While those approximations have been successful in certain applications, they are heuristic in nature and lack theoretical guarantees. Thus, the main problems with the majority of mutual information-based methods are that in most cases it is unknown what consists an optimal feature selection solution independent of the type of models fitted, and under which conditions a filter method will output an optimal feature set for classification (Guyon et al., 2007; Aliferis et al., 2010a).

# 2.2 Causal feature selection 

As an emerging type of filter methods, causal feature selection has attracted much attention in recent years. By bringing causality into play, causal feature selection naturally provides causal interpretation about the relationships between features and the class attribute, enabling a better understanding of the mechanisms behind data. Compared to non-causal feature selection, causal feature selection has been shown to be theoretically optimal (Tsamardinos and Aliferis, 2003), and thus answers the questions of what consists an optimal feature selection solution and under which conditions a filter method will output an optimal feature for classification.

Causal feature selection is to find the MB of the class attribute in a causal Bayesian network (CBN), where an edge $X \rightarrow Y$ indicates that $X$ is a direct cause (parent) of $Y$, and Y is a direct effect (child) of X . Then the MB of a variable of interest, such as the class attribute, consists of direct causes, direct effects, and direct causes of the direct effects of the class attribute. Therefore, the MB of the class attribute provides a complete picture of the local causal structure around it and the MB is a minimal set of features which renders the class attribute statistically independent from all the remaining features conditioned on the MB (Pearl, 2014). Theoretically, the MB of the class attribute is the optimal feature subset for classification (Koller and Sahami, 1995; Tsamardinos and Aliferis, 2003). Accordingly, the discovery of the MB of a class attribute is actually a procedure of feature selection (Aliferis et al., 2010a).

Koller and Sahami (Koller and Sahami, 1995) were the first to introduce MBs to feature selection and proposed the Koller-Sahami (KS) algorithm. However, the KS algorithm is not guaranteed to find the actual MB. Margaritis and Thrun (Margaritis and Thrun, 2000) invented the first sound MB discovery algorithm, GS (Growing-Shrinking) for Bayesian network structure learning.

Tsamardinos and Aliferis (Tsamardinos and Aliferis, 2003) improved the GS algorithm and proposed a series of MB discovery algorithms for optimal feature selection, which led to the IAMB (Incremental Association-based MB) family of algorithms, such as IAMB, interIAMB, IAMBnPC (Tsamardinos et al., 2003b), and Fast-IAMB (Yaramakala and Margaritis, 2005).

However, given a variable of interest, the IAMB and its variants discover the parents and children (PC) and spouses simultaneously and do not distinguish PC from spouse during MB discovery. And these algorithms require a large number of data samples exponential to

the size of the MB of the variable, thus they would not be effective for MB discovery when a dataset has thousands of variables with a small-sized data samples.

Then a divide-and-conquer approach was proposed to mitigate the problem. The representative algorithms include HITION-MB (Aliferis et al., 2003, 2010a), MMMB (Tsamardinos et al., 2003a), PCMB (Peña et al., 2007), IPC-MB (Fu and Desmarais, 2008), and STMB (Gao and Ji, 2017). The ideas behind these algorithms are as follows. They firstly find the parents and children (PC) of a variable of interest. Then, they discover the variable's spouses. Thus, these methods can return both the PC and MB sets of the variable. How to efficiently and effectively find the PC set of a variable is the key to this type of approach. The PCsimple (Bühlmann et al., 2010), MMPC (Tsamardinos et al., 2006), HITON-PC (Aliferis et al., 2003), and semi-HITON-PC (Aliferis et al., 2010a) algorithms are for PC discovery.

# 3. Bayesian network, Markov blanket, and feature selection 

Let $C$ be the class attribute of interest, and $C$ has $\varphi$ distinct values (class labels), denoted as $c=\left\{c_{1}, c_{2}, \cdots, c_{\varphi}\right\}$ and $F=\left\{F_{1}, F_{2}, \cdots, F_{n}\right\}$ be the set of all $n$ distinct features. Assuming that a training dataset $D$ is defined by $D=\left\{\left(d_{i}, c_{i}\right), 1 \leq i \leq m, c_{i} \in c\right\}$, where $m$ is the number of data instances, $d_{i}$ is the $i$ th data instance which is a $n$-dimensional vector defined on $F$, and $c_{i}$ is a class label associated with $d_{i}$. For the convenience of presentation, we use $V$ to represent the set of all variables under consideration, i.e. $V=$ $F \cup\{C\}=\left\{V_{1}, V_{2}, \cdots, V_{n+1}\right\}$, where $V_{i}=F_{i}(1 \leq i \leq n)$, and $V_{n+1}=C$. For $\forall V_{i} \in V$, let $V \backslash V_{i}$ indicate the set $V \backslash\left\{V_{i}\right\}$, that is, all features excluding $V_{i}$. We use $V_{i} \Perp V_{j} \mid S$, where $i \neq j$ and $S \subseteq V \backslash\left\{V_{i}, V_{j}\right\}$, to denote that $V_{i}$ is conditionally independent of $V_{j}$ given $S$, and $V_{i} \Perp V_{j} \mid S$ to represent that $V_{i}$ is conditionally dependent on $V_{j}$ given $S$. The definition of conditional independence (and dependence) is given as follows.

Definition 1 (Conditional independence) Given two distinct variables $V_{i}, V_{j} \in V$ are said to be conditionally independent given a subset of variables $S \subseteq V \backslash\left\{V_{i}, V_{j}\right\}$ (i.e. $V_{i} \Perp$ $\left.V_{j} \mid S\right)$, if and only if $P\left(V_{i}, V_{j} \mid S\right)=P\left(V_{i} \mid S\right) P\left(V_{j} \mid S\right)$. Otherwise, $V_{i}$ and $V_{j}$ are conditionally dependent given $S$, i.e. $V_{i} \Perp V_{j} \mid S$.

### 3.1 Bayesian network and Markov blanket

In this section, we introduce the background knowledge related to causal feature selection, including the basics of Bayesian network, Markov blanket, and the aim of causal feature selection. Let $P(V)$ be the joint probability distribution over the set of all variables $V$, and $G=(V, E)$ represent a directed acyclic graph (DAG) with nodes $V$ and edges $E$, where an edge represents the direct dependence relationship between two variables. In a DAG, $V_{i} \rightarrow V_{j}$ denotes that $V_{i}$ is a parent of $V_{j}$ and $V_{j}$ is a child of $V_{i}$.

Definition 2 (Bayesian network) (Pearl, 2014) The triplet $\langle V, G, P(V)\rangle$ is called a Bayesian network if the Markov condition as defined in Definition 3 holds.

Definition 3 (Markov condition) (Pearl, 2014) For a DAG G, the Markov condition holds in $G$ if and only if every node of $G$ is independent of any subset of its non-descendants conditioned on its parents.

A Bayesian network encodes the joint probability over a set of variables $V$ and decomposes $P(V)$ into the product of the conditional probability distributions of the variables given their parents in $G$. Let $P a\left(V_{i}\right)$ be the set of parents of $V_{i}$ in $G$. Then, $P(V)$ can be written as

$$
P\left(V_{1}, V_{2}, \cdots, V_{n+1}\right)=\prod_{i=1}^{n+1} P\left(V_{i} \mid P a\left(V_{i}\right)\right)
$$

In this paper, we consider a causal Bayesian network, a Bayesian network in which an edge $V_{i} \rightarrow V_{j}$ indicates that $V_{i}$ is a direct cause of $V_{j}$ (Pearl, 2014; Spirtes et al., 2000). For simple presentation, however, we use the term Bayesian network instead of causal Bayesian network. In the following, we introduce the key concepts and assumptions related to Bayesian networks and Markov blankets.

Definition 4 (Faithfulness) (Pearl, 2014) Given a Bayesian network $<V, G, P(V)>,$ $G$ is faithful to $P(V)$ if and only if every conditional independence present in $P$ is entailed by $G$ and the Markov condition. $P(V)$ is faithful if and only if $G$ is faithful to $P(V)$.

Definition 5 (Causal sufficiency) (Pearl, 2014) Causal sufficiency assumes that any common cause of two or more variables in $V$ is also in $V$.

Definition 6 (d-separation) (Pearl, 2014) In a DAG G, a path $\pi$ is said to be $d$ separated by a set of nodes $S \subset V$ if and only if (1) $\pi$ contains a chain $V_{i} \rightarrow V_{\omega} \rightarrow V_{j}$ $\left(V_{i} \leftarrow V_{\omega} \leftarrow V_{j}\right)$ or a fork $V_{i} \leftarrow V_{\omega} \rightarrow V_{j}$ such that the middle node $V_{\omega}$ is in $S$, or (2) $\pi$ contains a v-structure $V_{i} \rightarrow V_{\omega} \leftarrow V_{j}$ such that $V_{\omega} \notin S$ holds and no descendants of $V_{\omega}$ are in $S$. A set $S$ is said to d-separate $V_{i}$ from $V_{j}$ if and only if $S$ blocks every path from $V_{i}$ to $V_{j}$.

Theorem 1 (Pearl, 2014; Spirtes et al., 2000) Given a Bayesian network $<V, G, P(V)\rangle$, under the faithfulness assumption, d-separation captures all conditional independence relations that are encoded in $G$, which implies that $V_{i}$ and $V_{j}$ in $G$ are d-separated by $S \subset$ $V \backslash\left\{V_{i}, V_{j}\right\}$, if and only if $V_{i}$ and $V_{j}$ are conditionally independent given $S$ in $P(V)$.

Theorem 1 concludes that under the assumption of faithfulness, conditional independence in a data distribution and d-separation in the corresponding DAG are equivalent.

Definition 7 (Markov blanket, MB) (Pearl, 2014) Under the faithfulness assumption, the $M B$ of a variable in a Bayesian network is unique and consists of its parents (direct causes), children (direct effects), and spouses (other parents of the variable's children).

Figure 1 gives an example of a MB in the Bayesian network of lung cancer (Guyon et al., 2007). The MB of the variable lung cancer comprises: Smoking and Gentics (parents), Coughing and Fatigue (children), and Allergy (spouse).

Given a dataset $D$ defined on $F \cup C$, causal feature selection aims to find the MB of the class attribute $C$ (denoted as $M B(C)$ ) from $D$ (Aliferis et al., 2010a). In the following, Proposition 1 illustrates the relations between parents and children in a Bayesian network, and Proposition 2 presents the idea of how to discover spouses.

![img-0.jpeg](img-0.jpeg)

Figure 1: An example of an MB in a lung-cancer Bayesian network

Proposition 1 (Spirtes et al., 2000) In a Bayesian network, there is an edge between the pair of nodes $V_{i}$ and $V_{j}$, if and only if $V_{i} \not L V_{j} \mid S$, for all $S \subseteq V \backslash\left\{V_{i}, V_{j}\right\}$.

Proposition 2 (Spirtes et al., 2000) In a Bayesian network, assuming that $V_{i}$ is adjacent to $V_{j}, V_{j}$ is adjacent to $V_{\omega}$, and $V_{i}$ is not adjacent to $V_{\omega}$ (e.g. $V_{i} \rightarrow V_{j} \leftarrow V_{\omega}$ ), if $\forall S \subseteq$ $V \backslash\left\{V_{i}, V_{j}, V_{\omega}\right\}, V_{i} \Perp V_{\omega} \mid S$ and $V_{i} \not L V_{\omega} \mid S \cup\left\{V_{j}\right\}$ hold, then $V_{i}$ is a spouse of $V_{\omega}$.

# 3.2 Feature relevancy and non-causal feature selection 

Non-causal feature selection categorizes a feature as strongly relevant, weakly relevant, or irrelevant to $C$ (Kohavi and John, 1997) based on the following definitions in terms of conditional independence.

Definition 8 (Strongly relevant feature) (Kohavi and John, 1997) $F_{i} \in F$ is strongly relevant to $C$, if and only if there exists an assignment $F=f=\left(f_{1}, \cdots, f_{i-1}, f_{i}, f_{i+1}, \cdots, f_{n}\right)$ and $C=c_{i}, c_{i} \in c$, such that $P(F=f)>0$ and $P\left(C=c_{i} \mid F=f\right) \neq P\left(C=c_{i} \mid F \backslash F_{i}=\right.$ $\left.\left(f_{1}, \cdots, f_{i-1}, f_{i+1}, \cdots, f_{n}\right)\right)$.

Definition 9 (Weakly relevant feature) (Kohavi and John, 1997) $F_{i} \in F$ is weakly relevant to $C$, if and only if $F_{i}$ is not a strongly relevant feature and there exist $S \subset F \backslash F_{i}$, and an assignment $F_{i}=f_{i}, C=c_{i}$ and $S=s$ such that $P\left(S=s, F_{i}=f_{i}\right)>0$ and $P\left(C=c_{i} \mid S=s, F_{i}=f_{i}\right) \neq P\left(C=c_{i} \mid S=s\right)$.

Definition 10 (Irrelevant feature) (Kohavi and John, 1997) $F_{i} \in F$ is irrelevant to $C$, if and only if for any $S \subseteq F \backslash F_{i}$, for any assignment of $F_{i}, S$ and $C$, denoted as $f_{i}, s$, and $c_{i}$, such that $P\left(C=c_{i} \mid S=s, F_{i}=f_{i}\right)=P\left(C=c_{i} \mid S=s\right)$.

A strongly relevant feature affects the conditional class distribution, and provides unique information about $C$, i.e. it cannot be replaced by other features. A weakly relevant feature is informative but redundant since it can be replaced by other features without losing information about $C$. An irrelevant feature does not bring any information about $C$ and should be discarded. Thus, given a dataset $D$ defined on $F \cup C$, non-causal (filter) feature selection aims to select all features that are strongly relevant to $C$ (Tsamardinos and Aliferis, 2003).

In addition to the above conditional probability based definitions, recently, an explanation of feature relevance based on mutual information was proposed (Brown et al., 2012;

Bell and Wang, 2000; Vergara and Estévez, 2014). Before discussing the explanation, we first introduce the concepts of mutual information below. Given variable $X$, the entropy of $X$ is defined as (Cover and Thomas, 2012).

$$
H(X)=-\Sigma_{x} P(x) \log P(x)
$$

The entropy of $X$ after observing values of another variable $Y$ is defined as

$$
H(X \mid Y)=-\Sigma_{y} P(y) \Sigma_{x} P(x \mid y) \log P(x \mid y)
$$

In Eq.(2) and Eq.(3), $P(x)$ is the prior probability of $X=x$ (i.e. the value $x$ that $X$ takes), and $P(x \mid y)$ is the posterior probability of $X=x$ given $Y=y$. According to Eq.(2) and Eq.(3), the mutual information between $X$ and $Y$, denoted as $I(X, Y)$, is defined as

$$
\begin{aligned}
I(X ; Y) & =H(X)-H(X \mid Y) \\
& =\Sigma_{x, y} P(x, y) \log \frac{P(x, y)}{P(x) P(y)}
\end{aligned}
$$

From Eq. (4), the conditional mutual information between $X$ and $Y$ give another feature $Z$ is defined as:

$$
\begin{aligned}
I(X ; Y \mid Z) & =H(X \mid Z)-H(X \mid Y Z) \\
& =\Sigma_{z \in Z} P(z) \Sigma_{x \in X, y \in Y} P(x, y \mid z) \log \frac{P(x, y \mid z)}{P(x \mid z) P(y \mid z)}
\end{aligned}
$$

Based on the above definitions mutual information, we have the following propositions.
Proposition 3 (Brown et al., 2012) $F_{i}$ is strongly relevant to $C$ if and only if $I\left(F_{i} ; C \mid F \backslash\right.$ $\left.F_{i}\right)>0$.

Proposition 4 (Brown et al., 2012) $F_{i}$ is weakly relevant to $C$ if and only if $I\left(F_{i} ; C \mid F \backslash\right.$ $\left.F_{i}\right)=0$ and $\exists S \subset F \backslash F_{i}$ such that $I\left(F_{i} ; C \mid S\right)>0$.

Proposition 5 (Brown et al., 2012) $F_{i}$ is irrelevant to $C$, if and only if $\forall S \subseteq F \backslash F_{i}$, $I\left(F_{i} ; C \mid S\right)=0$.

# 4. Causal and non-causal feature selection have the same objective 

To develop a unified view of causal feature selection and non-causal feature selection, in this section, we will show that the two types of feature selection, although originating from different fields, share the same objective. In order to derive this conclusion (in Section 4.2), firstly in Section 4.1, inspired by the work in (Brown et al. 2012), we propose a mutual information based description of the optimal feature set for classification (i.e. Eq.(12)), and then link the description to Bayes error rate of classification.

### 4.1 A mutual information based representation of the objective function of optimal feature selection

Given a dataset $D$ containing $C$ and $F$, (filter) feature selection can be formulated as the problem of finding a subset $S^{*} \subset F$ such that

$$
S^{*}=\underset{S \subset F}{\arg \max } P(C \mid S)
$$

i.e. finding a subset $S^{*}$ given which the conditional probability of $C$ is maximized (Guyon and Elisseeff, 2006; Brown et al., 2012).

Let $F=\{S \cup \bar{S}\}$ where $S$ denotes the selected feature set and $\bar{S}$ represents the remaining features, i.e. $F \backslash S$. Given a dataset $D$ of $m$ instances, let $p(C \mid S)$ denote the true class distribution and $q(C \mid S)$ represent the predicted class distribution given $S$, then the conditional likelihood of $C$ is $L(C \mid S, D)=\prod_{i=1}^{m} q\left(c_{i} \mid s_{i}\right)$, where $c_{i} \in c\left(c=\left\{c_{1}, c_{2}, \cdots, c_{\varphi}\right\}\right)$ represents the value of $C$ in the $i$-th data instance and $s_{i}$ denotes the value of feature set $S$ in the $i$-th data instance. The (scaled) conditional log-likelihood of $L(C \mid S, D)$ is calculated by

$$
\ell(C \mid S, D)=\frac{1}{m} \sum_{i=1}^{m} \log q\left(c_{i} \mid s_{i}\right)
$$

Eq.(7) can be re-written as Eq.(8) below (Brown et al., 2012) ${ }^{1}$.

$$
\ell(C \mid S, D)=\frac{1}{m} \sum_{i=1}^{m} \log \frac{q\left(c_{i} \mid s_{i}\right)}{p\left(c_{i} \mid s_{i}\right)}+\frac{1}{m} \sum_{i=1}^{m} \log \frac{p\left(c_{i} \mid s_{i}\right)}{p\left(c_{i} \mid f\right)}+\frac{1}{m} \sum_{i=1}^{m} \log p\left(c_{i} \mid f\right)
$$

By negating Eq.(8) and using $E$ to represent statistical expectation, we have:

$$
-\ell(C \mid S, D)=E\left\{\log \frac{p(c \mid s)}{q(c \mid s)}\right\}+E\left\{\log \frac{p(c \mid f)}{p(c \mid s)}\right\}-E\{\log p(c \mid f)\}
$$

On the right hand side of Eq.(9), the first term is the likelihood ratio between the true and predicted class distributions given $S$, averaged over the input data space. The second term equals to $I(C ; \bar{S} \mid S)$, that is, the conditional mutual information between $C$ and $\bar{S}$ given $S$ (Brown et al., 2012). The final term is $H(C \mid F)$ by Eq.(3), the conditional entropy of $C$ given all features, and is an irreducible constant.

Definition 11 (Kullback Leibler divergence) (Kullback and Leibler, 1951) The Kullback Leibler divergence between two probability distributions $P(X)$ and $Q(X)$ is defined as $K L(P(X) \| Q(X))=\Sigma_{x} P(x) \log \frac{P(x)}{Q(x)}=E_{x} \log \left\{\frac{P(X)}{Q(X)}\right\}$.

By Definition 11 and Eq.(9), we have

$$
\lim _{m \rightarrow \infty}-\ell(C \mid S, D)=K L(p(C \mid S) \| q(C \mid S))+I(C ; \bar{S} \mid S)+H(C \mid F)
$$

Since in Eq.(10), $K L(p(C \mid S) \| q(C \mid S))$ will approach zero with a large $m$. Based on Eq.(10), we see that for large $m$ minimizing $I(C ; \bar{S} \mid S)$ maximizes $L(C \mid S, D)$. By the chain rule of mutual information, Eq.(11) below holds.

$$
\begin{aligned}
I(C ; F) & =I(C ;\{S, \bar{S}\}) \\
& =I(C ; S)+I(C ; \bar{S} \mid S)
\end{aligned}
$$

Given the feature set $F$ and the class attribute $C$, if $I(C ; F)$ is fixed, then in Eq.(11), minimizing $I(C ; \bar{S} \mid S)$ is equivalent to maximizing $I(C ; S)$. If $I(C ; \bar{S} \mid S)=0$ holds, $I(C ; S)$ is maximized. Accordingly, by Eq.(10) and Eq.(11), maximizing $I(S ; C)$ is equivalent to

[^0]
[^0]:    1. Please refer to Section 3.1 of Brown et al. (2012) for the details on how to obtain Eq.(7) and Eq.(8).

maximizing the conditional likelihood of $C$ (i.e. equivalent to maximizing $P(C \mid S)$ ). Thus, using mutual information, the objective function of feature selection of Eq.(6) can be reformulated as Eq.(12) below.

$$
S^{*}=\underset{S \subset F}{\arg \max } I(C ; S)
$$

In the following, we will show that the feature set $S^{*}$ defined in Eq.(12) is the set of features that leads to the minimal Bayes error rate. For a given classification problem, the minimum achievable classification error by any classifier is called its Bayes error rate (Fukunaga, 2013). We choose the Bayes error rate for justifying Eq.(12) since it is the tightest possible classifier-independent lower-bound by depending on predictor features and the class attribute alone. Fano and Hellman et. al. (Fano, 1961; Tebbe and Dwyer, 1968; Hellman and Raviv, 1970) proposed the lower and upper bounds on the Bayes error rate, which connect the Shannon conditional entropy (Shannon, 2001) to the Bayes error rate.

Let $P_{\text {err }}$ represent the Bayes error rate, and the entropy $H\left(P_{\text {err }}\right)$ is defined as

$$
H\left(P_{e r r}\right)=-P_{e r r} \log P_{e r r}-\left(1-P_{e r r}\right) \log \left(1-P_{e r r}\right)
$$

Then given $C$ and $S$, Fano's lower bound of the Bayes error rate (Fano, 1961) is defined as Eq.(14) below.

$$
H(C \mid S) \leq H\left(P_{e r r}\right)+P_{e r r} \log (K-1)
$$

Let $H\left(P_{e r r}\right)^{-1}$ be the inverse of $H\left(P_{e r r}\right)$, the upper bound of the Bayes error rate for a binary classification problem $(\mathrm{K}=2)$ is given as Eq.(15) below (Tebbe and Dwyer, 1968; Hellman and Raviv, 1970).

$$
H\left(P_{e r r}\right)^{-1} \leq P_{e r r} \leq 1 / 2 H(C \mid S)
$$

Meanwhile, considering $H(C \mid F)=H(C)-I(C ; F)$ and $I(C ; \bar{S} \mid S)=I(C ; F)-I(C ; S)$, Eq.(10) is re-written as Eq.(16) below.

$$
\lim _{m \rightarrow \infty}-\ell(C \mid S, D)=K L(p(C \mid S) \| q(C \mid S))+H(C \mid S)
$$

In Eq.(16), with a large $m, K L(p(C \mid S) \| q(C \mid S))$ will approach zero. Thus, we conclude that minimizing $H(C \mid S)$, that is, the conditional entropy of the class attribute $C$ given the predictor feature set $S$, is equivalent to maximizing the conditional likelihood of $C$ or minimizing the Bayes error rate (from Eq.(15)). Since $H(C \mid S)=H(C)-I(C ; S)$, maximizing $I(C ; S)$ in Eq.(12) equals to minimizing the upper bound of $H(C \mid S)$, i.e. the upper bound of $P_{\text {err }}$. This thus justifies that the feature set selected by Eq.(12) for classification will best facilitate minimizing the Bayes error rate. Eq.(17) illustrates the relationships among $I(C ; S), P_{\text {err }}$, and $L(C \mid S, D)$ where both " $<=>$ " denote "equivalent to", respectively.

$$
\arg \min _{S \subset F} P_{e r r}(S)<=>\arg \max _{S \subset F} I(C ; S)<=>\arg \max _{S \subset F} L(C \mid S, D)
$$

# 4.2 The objectives of causal and non-causal feature selection are the same 

In this section, we will demonstrate that the Markov blanket of $C(M B(C))$ is the feature set that maximizes Eq.(12), and the set of strongly relevant features aimed by non-causal feature selection.

Lemma 1 (Pearl, 2014) $\forall S \subset F \backslash M B(C), P(C \mid M B(C), S)=P(C \mid M B(C))$.
Lemma $2 I(X ; Y) \geq 0$ with equality if and only if $P(X, Y)=P(X) P(Y)$.
Lemma $3 I(X ; Y \mid Z) \geq 0$ with equality if and only if $P(X, Y \mid Z)=P(X \mid Z) P(Y \mid Z)$.

Clearly, by Eq.(4) and Eq.(5), Lemmas 2 and 3 hold. Then according to Lemmas 1 to 3, Theorem 2 below illustrates that $M B(C)$ is the solution to Eq.(12).

Theorem $2 \forall S \subset F, I(C ; M B(C)) \geq I(C ; S)$ with equality if and only if $M B(C)=S$.
Proof: in the proof, we use $M B$ to represent $M B(C)$.
Case 1: $\forall S \subseteq F \backslash M B$, by Eq.(5), we have:

$$
I(C ; S \mid M B)=E_{\{C, S, M B\}} \log \frac{P(C, S \mid M B)}{P(C \mid M B) P(S \mid M B)}
$$

As $P(C, S \mid M B)=P(C \mid M B) P(S \mid M B), I(C ; S \mid M B)=0$. By the chain rule, $I((S, M B) ; C)=$ $I(C ; M B)+I(C ; S \mid M B)=I(C ; S)+I(C ; M B \mid S)$. Since $I(C ; S \mid M B)=0, I(C ; M B)=$ $I(C ; S)+I(C ; M B \mid S)$. By Lemmas 2 and 3, we get that $\forall S \subseteq F \backslash M B, I(C ; M B)>I(C ; S)$.

Case 2: $\forall S \subseteq M B$ and let $S^{\prime}=M B \backslash S$, by $I(C ; M B)-I(C ; S)=I\left(C ; S \cup S^{\prime}\right)-$ $I(C ; S)=I(C ; S)+I\left(C ; S^{\prime} \mid S\right)-I(C ; S)=I\left(C ; S^{\prime} \mid S\right)$, then $I(C ; M B) \geq I(C ; S)$ holds with equality if $S$ equals to $M B$.

Case 3: Let $S^{\prime} \subset M B$ and $S^{\prime \prime} \subset F \backslash M B$, and $S=S^{\prime} \cup S^{\prime \prime}$, by Eq.(18) below, $I(C ; S \mid M B)=0$. Then by $I(C ; M B)+I(C ; S \mid M B)=I(C ; S)+I(C ; M B \mid S)$, in the case, $I(C ; M B)>I(C ; S)$.

$$
\frac{P(C, S \mid M B)}{P(C \mid M B) P(S \mid M B)}=\frac{P\left(C, S^{\prime \prime}, M B\right)}{P(C \mid M B) P\left(S^{\prime \prime}, M B\right)}=\frac{P\left(C \mid S^{\prime \prime}, M B\right) P\left(S^{\prime \prime}, M B\right)}{P(C \mid M B) P\left(S^{\prime \prime}, M B\right))}=1
$$

By Cases 1 to $3, I(C ; M B) \geq I(C ; S)$ with equality holds if $S$ equals to $M B$.

Corollary 1 Under the faithfulness assumption, $\forall F_{i} \in F, F_{i}$ belongs to $M B(C)$, if and only if $F_{i}$ is a strongly relevant feature.

Proof: In the proof, we use $M B$ to represent $M B(C) . P C(C)$ denotes parents and children of $C$ and $S P(C)$ represents spouses of $C$.

We firstly prove that if $F_{i} \in M B, F_{i}$ is a strongly relevant feature. Since $M B=P C(C) \cup$ $S P(C)$ and $P C(C) \cap S P(C)=\emptyset$, then (1) $\forall F_{i} \in P C(C)$ and $\forall S \subseteq F \backslash F_{i}$, by Proposition 1, $I\left(F_{i} ; C \mid S\right)>0$, and thus, $I\left(F_{i} ; C \mid F \backslash F_{i}\right)>0$ holds; (2) $\forall F_{i} \in S P(C)$ via child $F_{\omega} \in P C(C)$, by Proposition 2, there exists a $S \subset F \backslash F_{i}$ such that $I\left(F_{i} ; C \mid S\right)=0$ but $I\left(F_{i} ; C \mid S \cup\left\{F_{\omega}\right\}\right)>0$. Then, $\forall F_{j} \in F \backslash\left\{F_{\omega}, F_{i}\right\}, I\left(F_{i} ; C \mid F \backslash F_{j}\right)=I\left(F_{i} ; C \mid\left\{S \cup F_{\omega}, F \backslash\left\{S \cup F_{\omega} \cup F_{i}\right\}\right\}\right)$. So if $F_{i} \in S P(C), I\left(F_{i} ; C \mid F \backslash F_{j}\right)>0$ holds. By Proposition 3, $F_{i}$ is a strongly relevant feature.

We now prove that a strongly relevant feature of $C$ must be in $M B$. If $F_{i}$ is a strongly relevant feature, by Proposition 3, $I\left(F_{i} ; C \mid F \backslash F_{i}\right)>0$. Assume $F_{i} \notin M B, S^{\prime}=F \backslash\left\{F_{i}\right\} \cup$ $M B$, and $S=F \backslash F_{i}=M B \cup S^{\prime}$, we have:

$$
\begin{aligned}
I\left(F_{i} ; C \mid F \backslash F_{i}\right) & =I\left(F_{i} ; C \mid S\right) \\
& =E_{\left\{C, S, F_{i}\right\}} \log \frac{P\left(C, F_{i} \mid S\right)}{P(C \mid S) P\left(F_{i} \mid S\right)} \\
& =E_{\left\{C, S, F_{i}\right\}} \log \frac{P\left(C, F_{i}, S\right)}{P(C \mid S) P\left(F_{i} \mid S\right) P(S)} \\
& =E_{\left\{C, S, F_{i}\right\}} \log \frac{P\left(C \mid F_{i}, S\right) P\left(F_{i} \mid S\right)}{P(C \mid S) P\left(F_{i} \mid S\right)} \\
& =E_{\left\{C, S, F_{i}\right\}} \log \frac{P\left(C \mid F_{i}, S\right)}{P(C \mid S)} \\
& =E_{\left\{C, S^{\prime}, M B, F_{i}\right\}} \log \frac{P\left(C \mid F_{i}, S^{\prime}, M B\right)}{P\left(C \mid S^{\prime}, M B\right)} \\
& =0
\end{aligned}
$$

This makes a contrary, and thus $F_{i} \in M B(C)$.
Accordingly, given a dataset $D$ defined on $F \cup C$, by the analysis above, we show that $M B(C)$ maximizes the objective function in Eq.(12) and it is the same as the set of strongly relevant features.

# 5. Causal and non-causal feature selection: assumptions and approximations 

For both causal and non-causal feature selection methods, finding a subset $S$ that maximizes $I(S ; C)$ (i.e. solving the objective function in Eq.(12)) is a challenging combinatorial optimization problem. An exhaustive search will be of $O\left(2^{n}\right)$ time complexity. Although restricting the maximum size of $S$ to $\varsigma(\varsigma<n)$ will reduce the time complexity to $O\left(\varsigma^{n}\right)$ where $\varsigma^{n}$ is the number of all subsets of $F$ containing $\varsigma$ or less features, the computational cost will still be high. Therefore, both causal and non-causal feature selection methods have adopted a greedy strategy by considering features one by one to optimize Eq.(12) (Aliferis et al., 2010a; Balagani and Phoha, 2010; Brown et al., 2012). That is, at each iteration, given the set $S$ currently selected, choose $X^{*} \in F \backslash S$ such that

$$
\begin{aligned}
X^{*} & =\arg \max _{X \in F \backslash S} I(S \cup X ; C) \\
& =\arg \max _{X \in F \backslash S}\{I(S ; C)+I(X ; C \mid S)\}
\end{aligned}
$$

As for all $X \in F \backslash S$, the first item in Eq.(20) is the same, finding $X^{*}$ becomes solving the following optimization problem:

$$
X^{*}=\underset{X \in F \backslash S}{\arg \max } I(X ; C \mid S)
$$

However, in Eq.(21), when the size of $S$ increases, computing the multidimensional mutual information becomes impractical because it demands a large number of training samples, exponential in the number of features in $S$. To tackle this challenge, different feature selection methods make different assumptions on the interactions (or dependency) between features in the underlying data distributions for the calculation of $I(X ; C \mid S)$.

As described previously, a Bayesian network provides a representation of the probabilistic dependence among a set of variables under consideration. This provides us the

![img-1.jpeg](img-1.jpeg)

Figure 2: An illustration of the Bayesian network structures corresponding to the structural assumptions made by the non-causal and causal feature selection methods
opportunity to unify the dependence assumptions made by the feature selection methods under the Bayesian network framework. In this paper, we propose a structure assumption approach to understanding the assumptions made by causal and non-causal feature selection methods and how these different levels of structural assumptions lead to the different approximations in their search for the solutions to Eq.(21).

In the following, firstly Section 5.1 provides a summary of our findings on the structural assumptions and how they are related to the approximations, then in Sections 5.2 and 5.3 we discuss the findings in detail by analyzing the assumptions and approximations made by the commonly used non-causal and causal feature selection methods.

# 5.1 Summary of findings 

### 5.1.1 Structural Assumptions and SEARCH strategies

As illustrated in Figure 2, we have found that the dependence/independence relationships among features assumed by both causal and non-causal feature selection methods can be represented as different restrictions to the structure of the Bayesian network model of the set of variables under study. Based on the assumed Bayesian network structures, causal and non-causal methods select the subset of features, $S \subset F$, with the conditional likelihood of the class attribute $C$ given $S, P(C \mid S)$ as close to $P(C \mid F)$ as possible.

Figure 3 summarizes the Bayesian network structure assumptions and search strategies used by causal and non-causal feature selection methods for the calculation of $I(X ; C \mid S)$. The number after each equation in Figure 3 are the same as the equation numbers given in Sections 5.2 and 5.3. From Figure 3, we see that a non-causal feature selection method firstly decomposes the multidimensional mutual information $I(X ; C \mid S)$ into three terms $\{I(X ; C)-I(S ; X)+I(S ; X \mid C)\}$ (See Eq.(22)), then calculates the multidimensional mutual information $\{-I(S ; X)+I(S ; X \mid C)\}$ using linear combination of low-order mutual information terms based on the respective naive Bayesian network assumption made on the dependence/independence between features. We call the assumptions made by non-causal feature selection methods the series of naive Bayesian network assumptions, because the assumptions can be represented by the family of Bayesian networks with the restricted structures as illustrated in Figures 2 (a), (b) and (c). For these naive Bayesian network structures, the class attribute has no parents while all the features each can only have a fixed number of parents, denoted as $k$-dependency (or $k$-DB) assumptions, where each feature can have at most other $k$ features as its parents (details in Section 5.2).

Figure 3: A road map of how causal and non-causal feature selection searches for $X^{*}$ in Eq. (21)
![img-2.jpeg](img-2.jpeg)

* With some algorithms, such as HITON-PC, the PC discovery and Spouse discovery steps are done interleavingly. Details see Section 5.3.2

Causal feature selection methods assume that one can learn from the given dataset a (general) Bayesian network without structural restrictions (as the example in Figure 2 (d)), and in the learnt Bayesian network, $X^{*}$ in Eq.(21) is a feature in the MB of the class attribute. Therefore, as shown in Figure 3, causal feature selection does not decompose $I(X ; C \mid S)$ for the use of any structural assumptions, and the assumptions made by causal feature selection are only those for a general Bayesian network and its learning, i.e. the Markov condition (Definition 3), the faithfulness (Definition 4), and causal sufficiency (Definition 5) assumptions. Unlike the non-causal feature selection methods, these assumptions do not pose any structural restrictions on a Bayesian network learnt from data (thus called the general Bayesian network assumptions in this paper).

# 5.1.2 Linking the Assumptions With APPROXIMATIONS 

We use the pyramid in Figure 4 (a) to visualize the difference in the strictness of the structural assumptions made by the different feature selection methods. We see that causal feature selection methods make the weakest assumptions (no restrictions on the structures of the Bayesian network), while the non-causal feature selection methods make assumptions with different levels of strictness in terms of the maximum number of parents that a feature can have in addition to the class attribute (the value of $k$ in Figure 4 (a)).

As a result of the differences in the strictness of the structural assumptions, the degree of the corresponding approximations taken by the feature selection methods in their calculation of the multidimensional mutual information $(I(X ; C \mid S))$ are different, and they can be visualized using an upside down pyramid (Figure 4 (b)). Causal feature selection methods, since having had no structural restrictions, take less approximations by calculating higher order mutual information between $X$ and $C$ conditioning on all or a subset of the already selected features $S$ (details of the conditioning sets are to be discussed in Section 5.3). Referring back to Figure 3, the non-causal feature selection methods eventually only look at the pairwise mutual information between $X$ and $C$ without conditioning on other features.

Therefore, in theory, the feature set obtained by a causal feature selection methods is closer to the optimal feature set, i.e. the MB of the class attribute. However, as we will see in later sections, in practice, causal feature selection does not always outperform non-causal feature selection, because the number of samples required by causal feature selection can be exponential in the number of features in $S$.

### 5.1.3 CAUSAL INTERPRETATION AND NON-CAUSAL FEATURE SELECTION

By representing the dependency between features and the class attribute using Bayesian network structures, we present a causal interpretation of the features selected by non-causal methods.

We have found that the non-causal feature selection methods prefer features within $M B(C)$ to the features not in $M B(C)$, which confirms that strongly relevant features belong to $M B(C)$ (i.e. Corollary 1). This finding provides a causal interpretation of the output of the non-causal feature selection methods and explains why non-causal feature selection also can achieve excellent classification results. This also provides a novel perspective to understand the relations between the two types of feature selection methods, and may motivate researchers to use the cross-pollination between causal and non-causal fea-

![img-3.jpeg](img-3.jpeg)

Figure 4: Strictness of structural assumptions and the corresponding level of approximations taken by causal and non-causal feature selection methods when calculating $I(X ; C \mid S)$ (a) the strictness of structural assumptions in terms of maximum number of parents a feature can have (excluding the class attribute). Names of typical methods are shown. (b) the level of approximations in terms of the size of conditioning set used in the calculation.
ture selection methods to develop novel methodologies promising to scalable local-to-global causal structure learning and feature selection with theoretical guarantees.

# 5.2 Non-causal feature selection: assumptions and approximations 

In this section, we will explore in detail the assumptions made by non-causal feature selection under the naive Bayesian network framework, and under the assumptions how the major existing non-causal feature selection algorithms produce the same result as Eq.(21).

By $I(X ; S ; C)=I(X ; S)-I(X ; S \mid C)=I(X ; C)-I(X ; C \mid S)$, we have:

$$
I(X ; C \mid S)=I(X ; C)-I(X ; S)+I(X ; S \mid C)
$$

The three terms on the right side of Eq.(22) have the following interpretation:

- $I(X ; C)$ corresponds to the relevancy of $X$ to $C$.
- $I(X ; S)$ represents the redundancy of $X$ with respect to $S$.
- $I(X ; S \mid C)$ indicates the class-conditional relevance, which considers the situation where a feature provides more predictive information by jointly with another feature than by itself with respect to $C$. Since $I((S, X) ; C)=I(S ; C)+I(X ; C \mid S)$, $I(X ; C \mid S)=I((S, X) ; C)-I(S ; C)$. In Eq.(22), when $I(X ; S)>I(X ; S \mid C), I(X ; C \mid S)<$ $I(X ; C)$ holds, and thus $I((S, X) ; C)<I(S ; C)+I(X ; C)$. This means that $X$ contains redundant information about $C$ when we add $X$ to $S$. When $I(X ; S)<I(X ; S \mid C)$,

$I(X ; C \mid S)>I(X ; C)$ holds, and thus $I((S, X) ; C)>I(S ; C)+I(X ; C)$. This indicates that $X$ and $S$ have a positive interaction and $I((S, X) ; C)$ provides more information than $I(S ; C)+I(C ; X)$.

By Eq.(22), Eq.(21) can be re-written as

$$
X^{*}=\underset{X \in F \backslash S}{\arg \max }\{I(X ; C)-I(X ; S)+I(X ; S \mid C)\}
$$

To reduce computational costs in the search for $X^{*}$ in Eq.(23), different non-causal feature selection methods make different assumptions, and thus adopt different level of approximations when calculating $I(X ; S)$ and $I(X ; S \mid C)$ by using a linear combination of low-order mutual information terms.

In the following, we will explore these assumptions and approximations of Eq.(23). Using a general Bayesian all features and the class attribute, we have

$$
P(C \mid F) \propto P(C \mid P a(C)) \prod_{i=1}^{n} P\left(F_{i} \mid P a\left(F_{i}\right)\right)
$$

A naive Bayesian network is a restricted Bayesian network, which considers the class attribute $C$ as a special variable that has no parents and each of the remaining variables in the network only has the class attribute $C$ and a fixed number of other features as its parents. Let $k$ represent the maximum number of parents (excluding the class attribute) a feature can have, we call the naive Bayesian network a $k$-dependency $(k-\mathrm{DB})$ naive Bayesian network. A 0-DB network (as illustrated in Figure 2 (a)) is the commonly know naive Bayes (NB) network (Maron and Kuhns, 1960; Minsky, 1961). A NB network assumes that each variable only has one parent, i.e. $C$, and all features are conditionally independent given $C$. A 1-DB network (as illustrated in Figure 2 (b)) is known as a Tree-Augmented Naive (TAN) Bayes network, which allows each variable to have at most one other feature in addition to $C$ as its parent. A 2-DB network ((see an example in Figure 2 (c)) relaxes NB's and TAN's independence assumptions by allowing each feature to have a maximum of two other features as parents to generalize to higher degrees of variable interactions.

Let $n c l \_p a\left(F_{i}\right)$ denote the set of parents of $F_{i}$ excluding the class attribute $C$, in a $k$-DB naive Bayesian network, Eq.(24) becomes

$$
P(C \mid F) \propto P(C) \prod_{i=1}^{n} P\left(F_{i} \mid C, n c l \_p a\left(F_{i}\right)\right),\left|n c l \_p a\left(F_{i}\right)\right|=k \&|p a(C)|=0
$$

# 5.2.1 Approximations under 0-DB(NB) Structural assumptions 

The following NB network assumption $(k=0)$ is often made by non-causal feature selection methods.

Assumption 1. In a NB network, $\forall F_{i}, F_{j} \in F$ and $i \neq j, F_{i}$ and $F_{j}$ are assumed to be conditionally independent given the class attribute $C$, that is, $P\left(F_{i}, F_{j} \mid C\right)=P\left(F_{i} \mid C\right) P\left(F_{j} \mid C\right)$.

By Assumption 1, Eq.(25) is transformed into

$$
P(C \mid F) \propto P(C) \prod_{i=1}^{n} P\left(F_{i} \mid C\right),\left|n c l \_p a\left(F_{i}\right)\right|=0 \&|p a(C)|=0
$$

By Assumption 1 and Eq.(26), in Eq.(23), the class-conditional relevancy $I(X ; S \mid C)$ is calculated as Eq.(27) as follows.

$$
\begin{aligned}
I(X ; S \mid C) & =E_{x, s, c} \log \frac{P(X, S \mid C)}{P(S \mid C) P(X \mid C)} \\
& =E_{x, s, c} \log \frac{P(S \mid C) P(X \mid C)}{P(S \mid C) P(X \mid C)} \\
& =0
\end{aligned}
$$

Then under Assumption 1 and Eq.(27), Eq.(23) becomes

$$
\underset{X \in F \backslash S}{\arg \max }\{I(X ; C)-I(X ; S)+I(X ; S \mid C)\}=\underset{X \in F \backslash S}{\arg \max }\{I(X ; C)-I(X ; S)\}
$$

Since the redundancy term $I(X ; S)=H(S)-H(S \mid X)$, and by the chain rule of entropy, we have $H(S \mid X)=\sum_{F_{i} \in S} H\left(F_{i} \mid F_{i-1}, \cdots, F_{1}, X\right)$. If we further employ Assumption 2 below to restrict the interactions between a feature in $S$ and a feature in $F \backslash S$, in Eq.(23), $I(X ; S)=0$ holds.

Assumption 2. For $\forall F_{i} \in S$ and $\forall F_{j} \in F \backslash S, P\left(F_{i}, F_{j}\right)=P\left(F_{i}\right) P\left(F_{j}\right)$.
By Assumptions 1 and 2, the objective function in Eq.(23) is simplified to the following, which is only based on the mutual information between a feature and the class attribute:

$$
X^{*}=\underset{X \in F \backslash S}{\arg \max } I(X ; C)
$$

The objective in Eq.(29) is the mutual information maximization (MIM) criterion initially presented in (Lewis, 1992).

Assumption 2 is a strong assumption that the features in $S$ and the features in $F \backslash$ $S$ are pairwise independent. To deal with the redundancy between features, we discuss Assumption 3 below, which is a less restrictive than Assumption 2.

Assumption 3. The selected features in $S$ are conditionally independent given an unselected feature $X \in F \backslash S$, that is, $P(S \mid X)=\prod_{i=1}^{|S|} P\left(F_{i} \mid X\right)\left(F_{i} \in S\right)$.

Since $I(X ; S)=H(S)-H(S \mid X)$, by the chain rule and Assumption 3, we have

$$
\begin{aligned}
I(X ; S) & =H(S)-\sum_{i=1}^{|S|} H\left(F_{i} \mid X\right) \\
& =H(S)-\sum_{i=1}^{|S|} H\left(F_{i}\right)+\sum_{i=1}^{|S|} I\left(F_{i} ; X\right)
\end{aligned}
$$

Since at each time, $\forall X \in F \backslash S$, the first two terms in Eq.(30) are the same, then $I(X ; S)$ is decomposed into a sum of pairwise mutual information terms. Further based on Assumption $1, I(X ; S \mid C)=0$, then the objective function in Eq.(23) becomes:

$$
X^{*}=\underset{X \in F \backslash S}{\arg \max }\left\{I(X ; C)-\sum_{i=1}^{|S|} I\left(F_{i} ; X\right)\right\}
$$

Eq.(31) is the criterion of "max-relevance and min-redundancy" (Peng et al., 2005). Based on Eq.(31), Battiti (Battiti, 1994) presents the following Mutual Information Feature Selection (MIFS) criterion:

$$
X^{*}=\underset{X \in F \backslash S}{\arg \max }\left\{I(X ; C)-\beta \sum_{i=1}^{|S|} I\left(F_{i} ; X\right)\right\}
$$

$\beta \in[0,1]$ in the MIFS criterion is a penalty for balancing the relevance and redundancy terms. When $\beta=0$, Eq.(32) becomes Eq.(29), that is, the MIM criterion. As $\beta=1$, Eq.(32) is reduced to Eq.(31). If $\beta=1 /|S|$, Eq.(32) becomes

$$
X^{*}=\underset{X \in F \backslash S}{\arg \max }\left\{I(X ; C)-\frac{1}{|S|} \sum_{i=1}^{|S|} I\left(F_{i} ; X\right)\right\}
$$

Eq.(33) is the mRMR (max-Relevance and Min-Redundancy) criterion presented in (Peng et al., 2005). Meanwhile, from Eq.(33), we can see that as the size of $S$ increases, Eq.(33) will tend asymptotically towards Eq.(29).

There are other feature selection methods based on the idea of max-relevance and minredundancy shown in Eq.(31), such as a representative algorithm, Fast Correlation Based Filter (FCBF) (Yu and Liu, 2004). FCBF divides the "max-relevance and min-redundancy" criterion into two steps, that is, the forward step (max-relevance) and backward step (minredundancy).

- Forward step: FCBF selects a subset of features $S$ that $\forall X \in S, I(C ; X)>0$, then sorts the features in $S$ by their mutual information with $C$ in descending order.
- Backward step: beginning with the first feature $X \in S$, if $\exists Y \in S \backslash X$ such that $I(X ; Y)>I(X ; C)$, then it removes $Y$ from $S$ as a redundant feature to $X$. The FCBF algorithm is terminated until the last feature in $S$ is checked.
At the forward step, FCBF only selects features that are relevant to $C$, and this implies Assumption 1. The backward step implies Assumption 3. At the backward step, for $X$, $Y \in S$, if $I(X ; C)>I(Y ; C)$ and $I(X ; Y)>I(X ; C)$, then $Y$ can be removed from $S$. FCBF does not need to specify the number of selected features in advance. Instead, FCBF uses a threshold $\delta(\delta>0)$ at the forward step and keeps features satisfying $I(C ; X) \geq \delta$.


# 5.2.2 Approximations with 1-DB(TAN) Structural assumptions 

Under Assumption 1, in Eq.(23), $I(X ; S \mid C)=0$ holds. A TAN Bayesian network relaxes Assumption 1 to allow each feature to be dependent on one other feature in addition to $C$ and makes the following assumption. Assumption 4 states that the features within $S$ are class-conditionally independent given an unselected feature $X \in F \backslash S$ and $C$.

Assumption 4. $\forall F_{i}, F_{j} \in S$ and $i \neq j, F_{i}$ and $F_{j}$ are assumed to be conditionally independent given an unselected feature $X \in F \backslash S$ and $C$, that is, $P\left(F_{i}, F_{j} \mid X, C\right)=$ $P\left(F_{i} \mid C, X\right) P\left(F_{j} \mid C, X\right)$.

Thus for a TAN Bayesian network, Eq.(25) becomes:

$$
P(C \mid F) \propto P(C) \prod_{F_{j} \in F, F_{i} \in F \backslash F_{j}} P\left(F_{i} \mid C, F_{j}\right),\left|n c L_{o} p a\left(F_{i}\right)\right|=1 \&\|p a(C)\|=0
$$

Then by the chain rule, we get $H(S \mid X, C)=\sum_{F_{i} \in S} H\left(F_{i} \mid X, C\right)$. By Eq.(27), $I(X ; S \mid C)=$ 0 only and if only Assumption 1 holds, and thus by Assumption 4, $I(X ; S \mid C)$ can be decomposed as follows.

$$
\begin{aligned}
I(X ; S \mid C) & =H(S \mid C)-H(S \mid X, C) \\
& =H(S \mid C)-\sum_{F_{i} \in S} H\left(F_{i} \mid X, C\right) \\
& =H(S \mid C)-\sum_{F_{i} \in S}\left\{H\left(F_{i} \mid C\right)-I\left(F_{i} ; X \mid C\right)\right\}
\end{aligned}
$$

Since $H(S \mid C)-\sum_{F_{i} \in S} H\left(F_{i} \mid C\right)$ in Eq.(35) is the same for $\forall F_{i} \in S$. Meanwhile, assuming that Assumption 3 holds for feature interactions between the selected features in $S$ and the unselected feature in $F \backslash S$, then by Eq.(30) (under Assumption 3) and Eq.(35) (under Assumption 4), Eq.(23) becomes:

$$
X^{*}=\underset{X \in F \backslash S}{\arg \max }\left\{I(X ; C)-\Sigma_{F_{i} \in S} I\left(X ; F_{i}\right)+\Sigma_{F_{i} \in S} I\left(X ; F_{i} \mid C\right)\right\}
$$

Brown et al. (Brown et al., 2012) have proposed that many mutual information-based non-causal feature selection methods can fit within the following parameterized criterion. $\beta$ and $\gamma$ play the role of balancing factors (in general $\beta \in[0,1]$ and $\gamma \in[0,1]$ ).

$$
X^{*}=\underset{X \in\{F \backslash S\}}{\arg \max }\left\{I(X ; C)-\beta \sum_{F_{i} \in S} I\left(X ; F_{i}\right)+\gamma \sum_{F_{i} \in S} I\left(X ; F_{i} \mid C\right)\right\}
$$

If $\beta=1 /|S|$ and $\gamma=1 /|S|$, then we have:

$$
X^{*}=\underset{X \in F \backslash S}{\arg \max }\left\{I(X ; C)-\frac{1}{|S|} \Sigma_{F_{i} \in S} I\left(X ; F_{i}\right)+\frac{1}{|S|} \Sigma_{F_{i} \in S} I\left(X ; F_{i} \mid C\right)\right\}
$$

Using Eq.(38) for feature selection, the representative algorithm is the JMI algorithm (Yang and Moody, 2000). If $\beta=1$ and $\gamma=1$, Eq.(37) is reduced to Eq.(36) used by the CIFE algorithm (Lin and Tang, 2006). The CMIM method (Fleuret, 2004) adopts an objective function as follows.

$$
X^{*}=\underset{X \in F \backslash S}{\arg \max }\left\{I(X ; C)-\max _{F_{i} \in S}\left\{I\left(X ; F_{i}\right)-I\left(X ; F_{i} \mid C\right)\right\}\right\}
$$

# 5.2.3 Approximations with 2-DB Structural assumptions 

To deal with a higher-order dependency between features, the recent work in (Vinh et al., 2016) calculates $I(X ; S)$ in Eq.(23) by exploring the 2-DB structure assumptions.

The 2-DB structure relaxes NB's and TAN's independence assumptions by allowing each feature to have at most two features as parents, i.e., $\left|n c l \_p a\left(F_{i}\right)\right|=2$, in addition to $C$, and makes the following assumptions.

Assumption 5a. $\forall F_{i} \in S$ and $\forall F_{j} \in S(i \neq j)$ are assumed to be conditionally independent given an unselected feature $X \in F \backslash S$ and any feature $Y \in F \backslash\left\{F_{i} \cup F_{j}\right\}$, that is, $P\left(F_{i}, F_{j} \mid X, Y\right)=P\left(F_{i} \mid X, Y\right) P\left(F_{j} \mid X, Y\right)$.

Assumption 5b. For $\exists F_{j} \in S$ and $\forall F_{i} \in F \backslash F_{j}$ are conditionally independent given an unselected feature $X \in F \backslash S$, that is, $P\left(F_{j}, F_{i} \mid X\right)=P\left(F_{i} \mid X\right) P\left(F_{j} \mid X\right)$.

Thus, with a 2-DB structure, Eq.(25) is transformed into Eq.(40).

$$
P(C \mid F) \propto P(C) \prod_{i=1\left(F_{i} \in F \backslash\left\{F_{j} \cup F_{\omega}\right\}\right)}^{n} P\left(F_{i} \mid C, F_{j}, F_{\omega}\right)),\left|n c l \_p a\left(F_{i}\right)\right|=2 \&|p a(C)|=0
$$

With the structure assumptions, the redundancy term $I(X ; S)$ in Eq.(23) is computed as follows. Since $I(X ; S)=H(S)-H(S \mid X)$ under Assumptions 5a and 5b, $H(S \mid X)$ is

calculated as follows.

$$
\begin{aligned}
H(S \mid X)= & -\sum_{i=1}^{|S|} \sum_{F_{1}, \cdots, F_{i}, X} P\left(F_{1}, \cdots, F_{i}, X\right) \log P\left(F_{i} \mid F_{i-1}, \cdots, F_{1}, X\right) \\
= & P\left(F_{1}, \cdots, F_{j}, X\right) \log P\left(F_{j} \mid F_{j-1}, \cdots, F_{1}, X\right) \\
& +\sum_{i=1(i \neq j)}^{|S|-1} P\left(F_{i-2}, \cdots, F_{1}, F_{j}, X\right) \log P\left(F_{i} \mid F_{i-2}, \cdots, F_{1}, F_{j}, X\right) \\
= & H\left(F_{j} \mid X\right)+\sum_{i=1, i \neq j}^{|S|-1} H\left(F_{i} \mid F_{j}, X\right)
\end{aligned}
$$

By Eq.(41), $I(X ; S)$ is decomposed as Eq.(42) as follows.

$$
\begin{aligned}
I(X ; S) & =H(S)-H(S \mid X) \\
& =H(S)-\left\{H\left(F_{j} \mid X\right)+\sum_{i=1, i \neq j}^{|S|-1} H\left(F_{i} \mid F_{j}, X\right)\right\} \\
& =H(S)-H\left(F_{j}\right)+I\left(F_{j} ; X\right)-\sum_{i=1, i \neq j}^{|S|-1}\left\{H\left(F_{i} \mid F_{j}\right)-I\left(\left(F_{i}, X \mid F_{j}\right)\right\}\right.
\end{aligned}
$$

In Eq.(42), at each iteration, for $\forall X \in F \backslash S, H(S)-H\left(F_{j}\right)-\sum_{i=1, i \neq j}^{|S|-1} H\left(F_{i} \mid F_{j}\right)$ is the same. Meanwhile, to avoid the need of checking which feature in $S$ satisfying Assumption 5 b , by averaging over all features in $S$, we have

$$
\begin{aligned}
X^{*} & =\underset{1}{\arg \max }_{X \in F \backslash S}\{I(X ; C)+H(S \mid C)-H(S \mid C, X) \\
& -\frac{1}{|S|} \Sigma_{F_{i} \in S}\left\{I\left(X ; F_{i}\right)+\Sigma_{F_{j} \in S, i \neq j} I\left(X ; F_{j} \mid F_{i}\right)\right\}
\end{aligned}
$$

If we employ Assumption 4 for $I(X ; S \mid C)$ in Eq.(43), we get the following objective function in Eq.(44) used by the RelaxMRMR algorithm proposed by (Vinh et al., 2016).

$$
\begin{aligned}
X^{*} & =\underset{-\frac{1}{|S|} \sum_{F_{i} \in S}\left\{I\left(X ; C\right)+\Sigma_{F_{i} \in S} I\left(X ; F_{i} \mid C\right)\right.}{ } \\
& \left.-\frac{1}{|S|} \Sigma_{F_{i} \in S}\left\{I\left(X ; F_{i}\right)+\Sigma_{F_{j} \in S, i \neq j} I\left(X ; F_{j} \mid F_{i}\right)\right\}\right\}
\end{aligned}
$$

# 5.2.4 Time COMPLEXITY AND SAMPLE REQUIREMENT OF NON-CAUSAL FEATURE SELECTION 

In this section, we will analyze the time complexity and sample requirement of non-causal feature selection methods. Under the $k$-DB structural assumption, the most common family of non-causal feature selection methods decompose Eq.(21) into different objective functions, such as Eq.(29), Eq.(31), Eq.(36), or Eq.(44), in a linear combination of low-order mutual information terms. By these objective functions, non-causal feature selection methods greedily select the $\psi$ features with the highest mutual information scores (Guyon and Elisseeff, 2003). The time complexity of non-causal feature selection methods depends on $\psi$. Solving Eq.(44) requires $O\left(\psi^{3} n\right)$ mutual information computations. Eq.(31) and Eq.(36) need $O\left(\psi^{2} n\right)$ pairwise comparisons, while Eq.(29) (the MIM criterion) only requires $O(n)$ pairwise comparisons. However, how to determine a good value of the user-defined parameter $\psi$ for optimal feature selection is not an easy problem.

The sample requirement of a non-causal feature selection method depends on the number of samples needed to assure reliable computation of mutual information or independence tests. With discrete data, $\chi^{2}$ (chi-square) test and $G^{2}$ test (a variant of chi-square test) are commonly used to determine the independence of two variables. For a reliable independence test between $X$ and $C$ given the current conditioning set $S$, the minimum number of data samples $N$ is:

$$
N \geq \xi \times r_{X} \times r_{C} \times r_{S}
$$

![img-4.jpeg](img-4.jpeg)

Figure 5: The three-way causal interactions and non-causal feature selection
where $r_{X}$ and $r_{C}$ represent the numbers of possibles values (i.e. levels) of $X$ and $C$ respectively, and $r_{S}=\prod_{i=1}^{|S|} r_{F_{i}}, F_{i} \in S$, i.e. the multiplication of the numbers of possible values of all features in $S . \xi$ is often set to 5 as suggested by Agresti (Agresti and Kateri, 2011). As $\xi$ is a constant, the lower bound of the required data samples $N$ is only determined by $r_{X}, r_{C}$, and $r_{S}$ where $r_{S}$ plays the key role in (45).

In the paper, since we formulate feature selection using mutual information, Eq.(46) below shows that the mutual information between two variables is proportional to the value of association of the two variables calculated by $G^{2}$ test (Yaramakala, 2004), which guarantees the correctness of using Eq.(45) above to discuss the sample requirement of non-causal feature selection methods.

$$
\frac{1}{2 N} G^{2}(X ; C)=I(X ; C) \& \frac{1}{2 N} G^{2}(X ; C \mid S)=I(X ; C \mid S)
$$

To obtain the lower bounds of required samples of the non-causal feature selection methods, assume $X_{\max }, Y_{\max }$, and $W_{\max }$ are the three features with the largest discrete values, then the minimum number of data samples required by Eq.(29) (MIM), Eq.(31) (MIFS, mRMR, and FCBF), Eq.(36) (JMI and CMIM), and Eq.(44) (RelaxMRMR) is bounded by $r_{X_{\max }} \times r_{C}, r_{X_{\max }} \times r_{Y_{\max }}, r_{X_{\max }} \times r_{Y_{\max }} \times r_{C}, r_{X_{\max }} \times r_{Y_{\max }} \times r_{W_{\max }}$, respectively. Since the existing major non-causal feature selection methods calculate $I(X ; C \mid S)$ using linear combination of low-order mutual information terms (i.e. the size of $S$ in $r_{S}$ in (45) is never bigger than 1), the sample requirement of non-causal feature selection is not high.

# 5.2.5 Discussion 

Let $X$ be the candidate feature under consideration, and $Y$ a previously selected feature. In Eq.(29), Eq.(31), Eq.(36), and Eq.(44), we can see that those methods only consider at most one of the selected features when evaluating $X$. Therefore, in the following, by representing the interactions among the three variables $X, Y$, and $C$ (class attribute) using Bayesian network structures from Figures 5 (a) to $5(\mathrm{~g})$, firstly, we discuss some properties between $X, Y$, and $C$, i.e. Properties 1 to 4 below. Secondly, with those properties, we will investigate the causal interpretations of Eq.(29), Eq.(31), Eq.(36), and Eq.(44). Through the discussion, we will show that the major non-causal feature selection methods driven by the simplified objective functions shown in Eq.(29), Eq.(31), Eq.(36), and Eq.(44) prefer direct causes, direct effects, and spouses of $C$ to the features which are not in $M B(C)$.

When $X$ and $Y$ are parents or children of $C$ as shown in Figures 5 (a) to (d), we have the following properties.

Property 1 If $X$ and $Y$ are both direct causes (parents) of $C$, i.e. the class attribute $C$ is a common-effect of the two features, as shown in Figure 5 (a), then (1) $I(X ; C)>I(X ; Y)$, (2) $I(X ; Y \mid C) \geq I(X ; Y)$, and (3) $I(X ; C)-I(X ; Y)+I(X ; Y \mid C)>0$.

Proof: According to Proposition 2, in the case shown in Figure 5 (a), $I(X ; Y)=0$ holds. Clearly, $I(X ; C)>I(X ; Y)$ if $I(X ; Y)=0$. By $I(X ; Y ; C)=I(X ; Y)-I(X ; Y \mid C)=$ $I(X ; C)-I(X ; C \mid Y)$, if $I(X ; Y)=0, I(X ; Y \mid C) \geq I(X ; Y)$ and $I(X ; C)-I(X ; Y)+$ $I(X ; Y \mid C)>0$ hold.

Property 2 In the causal chain interaction cases in Figures 5 (b) to (c) or the common cause interaction case in Figure 5 (d), where $X$ or $Y$ is a direct cause of $C$, i.e. $X, Y$ and $C$ form a causal chain or a direct effect of $C$ (i.e. $X$ and $Y$ are the common effect of $C$ ), (1) $I(X ; C)>I(X ; Y)$ and (2) $I(X ; C)-I(X ; Y)+I(X ; Y \mid C)>0$.

Proof: From Figures 5 (b) to (d), according to the Markov condition in Definition 3, $I(X ; Y \mid C)=0$. By $I(X ; Y \mid C)-I(X ; Y)=I(X ; C \mid Y)-I(X ; C), I(X ; C)>I(X ; Y)$ and $I(X ; C)-I(X ; Y)+I(X ; Y \mid C)>0$ hold.

Since $I((Y, X) ; C)=I(Y ; C)+I(X ; C \mid Y)$ and $I(X ; Y ; C)=I(X ; Y)-I(X ; Y \mid C)=$ $I(X ; C)-I(X ; C \mid Y)$, i.e. $I(X ; C \mid Y)=I(X ; C)-I(X ; Y)+I(X ; Y \mid C)$, we have $I((X, Y) ; C)=$ $I(Y ; C)+I(X ; C)-I(X ; Y)+I(X ; Y \mid C)$, or $I((X, Y) ; C)-I(Y ; C)=I(X ; C)-I(X ; Y)+$ $I(X ; Y \mid C)$. From Properties 1 and 2 above, we know that if $X$ a direct cause or a direct effect of $C, I(X ; C)-I(X ; Y)+I(X ; Y \mid C)>0$, therefore $I((X, Y) ; C)-I(Y ; C)>0$, indicating that in the case when $X$ is a direct cause or direct effect of $C, X$ and $Y$ together provide more information about $C$ than $Y$ alone does. When $X$ is a spouse of $C$ as shown in Figure 5 (e), we have the following property.

Property 3 If $X$ is a spouse of $C$ through $Y$ i.e. $Y$ is a child of both $X$ and $C$, as shown in Figure 5 (e), $I(X ; Y \mid C)>I(X ; Y)$ and $I(X ; C)-I(X ; Y)+I(X ; Y \mid C)>0$.

Proof: By Proposition 2, $I(X ; C)=0$ holds in Figure 1(e). Since $I(X ; Y \mid C)=$ $I(X ; Y)+I(X ; C \mid Y)-I(X ; C), I(X ; Y \mid C)>I(X ; Y)$ and $I(X ; C)-I(X ; Y)+I(X ; Y \mid C)>$ 0 holds.

Property 3 provides a causal interpretation for the class-conditional relevancy in Eq.(36). If $X$ is a spouse of $C$ and $Y$ is the common child of $X$ and $C, I(X ; Y \mid C)-I(Y ; X)>0$. Since $I((X, Y) ; C)=I(Y ; C)+I(X ; C)-I(X ; Y)+I(X ; Y \mid C)$, then even if $I(X ; C)=0$, $I((X, Y) ; C)$ provides more information than $I(Y ; C)$. This shows that although a spouse of $C$ is not a direct cause or a direct effect of $C$, from the viewpoint of class-conditional relevancy view, Property 3 confirms that the spouses of $C$ are strongly relevant features.

Property 4 If $Y$ is a direct cause or a direct effect of $C$, and $X$ is an indirect cause or an indirect effect of $Y$, as shown in Figures 5 (f) to (g), then (1) $I(X ; Y)>I(X ; C)$, (2) $I(X ; C)+I(X ; Y \mid C)-I(X ; Y)=0$, and (3) $I(Y ; C)>I(X ; C)$.

Proof: By the Markov condition, in Figures 5 (f) to (g), $I(X ; C \mid Y)=0$ holds. By $I(X ; Y \mid C)-I(X ; Y)=I(X ; C \mid Y)-I(X ; C), I(X ; Y) \geq I(X ; C)$ and $I(X ; C)+I(X ; Y \mid C)-$ $I(X ; Y)=0$. Then by $I(Y ; C \mid X)-I(Y ; C)=I(X ; C \mid Y)-I(X ; C), I(Y ; C)-I(X ; C)=$ $I(Y ; C \mid X)$. Since $I(Y ; C \mid X)>0, I(Y ; C)>I(X ; C)$ holds.

Table 1: Non-causal feature selection: objective functions and causal interpretations


With Properties 1 to 4, we analyze the causal interpretations of Eq.(29), Eq.(31), Eq.(36), and Eq.(44), and our observations are summarized in Table 1. These observations illustrate that the major non-causal feature selection methods prefer direct causes, direct effects, or spouses of $C$ to the features which are not in $M B(C)$ and further confirm that the strongly relevant features belong to $M B(C)$. Specifically, we get the following observations, and these observations will be validated by the experiments in Section 7.1.

- If $S$ is empty, $\forall X \in P C(C)$, i.e. $X$ is a direct cause or effect of $C$, for any of its ancestors or descendants $F_{i} \in F \backslash P C(C), I(X ; C)>I\left(F_{i} ; C\right)$ holds by Property 4. Thus, Eq.(29), Eq.(31), Eq.(36), and Eq.(44) will will add $C$ 's direct causes and effects first to $S$.
- With Properties 1 to 4, the term $I(X ; C)-I\left(X ; F_{i}\right)$ in Eq.(29), Eq.(31), Eq.(36), and Eq.(44) prefers direct causes and direct effects of $C$ (i.e. $P C(C)$ ), while the term $I\left(X ; F_{i} \mid C\right)$ in Eq.(36) and Eq.(44) prefers spouses of $C$. Specifically, MIFS, mRMR, FCBF that are based on or that employ Eq.(31) prefer the features $P C(C)$ to be added to $S$ and do not attempt to identify spouses of $C$, since Properties 1 to 2 state that only when both $X$ and $F_{i}$ belong to $P C(C), I(X ; C)>I\left(X ; F_{i}\right)$ holds. Eq.(36) and Eq.(44) attempt to discover not only $P C(C)$, but also spouses of $C$, since if $X$ is a spouse of $C$, there exists a feature $F_{i}$, i.e. the common child of $C$ and $X$, to make $I(X ; C)-I\left(X ; F_{i}\right)+I\left(X ; F_{i} \mid C\right)>0$.
- Assuming that currently $S=\left\{F_{i}\right\}$. If $F_{i} \in \operatorname{ch}(C)$, i.e. $F_{i}$ is a direct effect or a child of $C$. For two candidate features, $X \in P C(C)$ and $W$ which is a descendant of $C$ and $W \notin \operatorname{ch}(C)$, by Property 4, Eq.(29), Eq.(31), Eq.(36), and Eq.(44) would prefer $X$ to $W$. For example, assume that $X \rightarrow C \rightarrow F_{i} \rightarrow W$, then $I(X ; C)-I\left(X ; F_{i}\right)+$ $I\left(X ; F_{i} \mid C\right)>0$ by Property 1 and $I(W ; C)-I\left(W ; F_{i}\right)+I\left(W ; F_{i} \mid C\right)=0$. For MIFS and $\operatorname{mRMR}, I(X ; C)-I\left(X ; F_{i}\right)>0$ while $I(W ; C)-I\left(W ; F_{i}\right)<0$, and for FCBF, $I(X ; C)>I\left(X ; F_{i}\right)$ while $I\left(F_{i} ; C\right)>I(W ; C)$ and $I\left(W ; F_{i}\right)>I(W ; C)$. Thus, MIFS, mRMR, FCBF prefer $X$ to $W$. If $F_{i} \in p a(C), X \in P C(C), W$ is a ancestor of $C$ and

$W \notin p a(C)$ (for example, $W \rightarrow X \rightarrow C \rightarrow F_{i}$ ), for $X$ and $W$, with a similar analysis above, Eq.(29), Eq.(31), Eq.(36), and Eq.(44) would add $X$ to $S$.

# 5.3 Causal feature selection: assumptions and approximations 

As discussed at the beginning of Section 5 and in the previous sections, non-causal feature selection methods make assumptions on the dependency among features and the class attribute under the naive Bayesian network assumptions. Causal feature selection methods do not have such restrictions on the structure of the (causal) Bayesian network representing the dependence relationships of all the variables, including the class attribute and all features. However, in order to learn a (causal) Bayesian network or the local network structure around the class variable, causal feature selection methods employ the Markov condition (assumption) (Definition 3 in Section 3.1), faithfulness assumption (Definition 4 in Section 3.1) and causal sufficiency (Definition 5 in Section 3.1) for the correctness and causal meaning of the features selected.

Assuming $S$ is the feature set currently selected, $c h(C)$ is the children of $C, \operatorname{Des}(C)$ is the descendants of $C$, and $N D(C)$ is the ancestors of $C$, by the Markov condition, we can get the following properties.

Property 5 For an unselected feature $X \in F \backslash S$, if $X \in\{N D(C) \backslash p a(C)\})$ and $p a(C) \subseteq S$, $X$ is conditionally independent of $C$ given $S$, that is, $I(X ; C \mid S)=0$.

Property 6 For an unselected feature $X \in F \backslash S$, if $X \in\{\operatorname{Des}(C) \backslash c h(C)\})$ and $p a(X) \subseteq S$, $X$ is conditionally independent of $C$ given $S$, that is, $I(X ; C \mid S)=0$.

With the properties, most existing causal feature selection are designed to solve Eq.(21) (i.e. maximizing $I(X ; C \mid S)$ ) with a forward-backward strategy based on the below lemmas.

Lemma $4 \forall F_{i} \in P C(C)$ and $\forall S \subseteq F \backslash F_{i}, I\left(C ; F_{i} \mid S\right)>0$.
Proof: By Proposition 1, $\forall F_{i} \in P C(C)$ and $\forall S \subseteq F \backslash F_{i}, F_{i} \not L C \mid S$ holds. By Lemma 3, the lemma holds.

Lemma 5 If $F_{i}$ is a spouse of $C$ via $F_{j} \in \operatorname{ch}(C)$ (i.e. $F_{j}$ is a common child of $F_{i}$ and $C$ ), $\exists S \subseteq F \backslash\left\{F_{i}, F_{j}\right\}$ such that $I\left(C ; F_{i} \mid S\right)=0$ and $I\left(C ; F_{i} \mid F_{j} \cup S\right)>0$.

Proof: Since $C$ and $F_{i}$ are not directly connected by an edge, by Proposition 1, there must exist a subset $S$ such that $C$ and $F_{i}$ are independent given $S$, that is, $I\left(C ; F_{i} \mid S\right)=0$. By Proposition 2, $C$ and $F_{i}$ are conditionally dependent given any subset containing $F_{j}$, i.e. the common child of $F_{i}$ and $C$, thus, the lemma is proven.

In this section, we will analyze the search strategies taken by the existing causal feature selection methods for solving Eq.(21). All theorems and lemmas are discussed with the assumption that all independence tests (mutual information calculation) are reliable.

### 5.3.1 A simultaneous MB discovery strategy by conditioning on the entire $S$ FOR CALCULATING $I(X ; C \mid S)$ IN Eq.(21)

The simultaneous MB discovery strategy aims to find PC (parents and children) and spouses of $C$ simultaneously without distinguishing PC from spouses during the MB discovery.

This approach adopts the forward and backward steps to greedily discover $M B(C)$ for maximizing Eq.(21), i.e. sequentially maximizing $I(X ; C \mid S)(X \in F \backslash S)$ at the forward step (max-relevance) and minimizing $I(C ; Y \mid S \backslash Y)(Y \in S)$ at the backward step (minredundancy) by conditioning on the entire $S$ currently selected. This simultaneous discovery strategy has been employed by two representative algorithms, IAMB and InterIAMB (Tsamardinos et al., 2003b). The assumptions and search strategies of IAMB and inter-IAMB are discussed are follows.

IAMB. The forward and backward steps of IAMB for the sequential optimization of Eq.(21) are as follows.

- Forward step. At each iteration, $S$ is the set of features currently selected, and for each candidate feature within $F \backslash S$, the one satisfying $\arg \max _{X \in F \backslash S} I(X ; C \mid S)$ and $I(X ; C \mid S)>0$ is added to $S$. The forward step is terminated until $\forall X \in F \backslash S$, $I(C ; X \mid S)=0$.
- Backward step. IAMB sequentially removes from $S$ the false positive $Y \in S$ satisfying $I(C ; Y \mid S \backslash Y)=0$ until $\forall Y \in S, I(C ; Y \mid S \backslash Y)>0$.

The forward step will add all features in the true $M B(C)$ to $S$. Due to the greedily strategy, some false positives may enter $S$ at the forward step. For example, assuming $X \notin M B(C)$ and $\exists Y \in M B(C)$ such that $I(X ; C \mid S \cup Y)=0$. However, when checking $I(X ; C \mid S)$ and at this time $Y \notin S, I(C, X \mid S)>0$ holds and $X$ will be added to $S$. Thus, the backward step will remove all the false positives in $S$ by Properties 5 and 6.

Theorem 3 The output of IAMB is the optimal set $S^{*}$ in Eq.(12).
Proof: Assuming $\bar{S}$ denotes the set $F \backslash S$. At the forward step, at each iteration, $X \in F \backslash S$ is selected that satisfies Eq.(47) below.

$$
X^{*}=\arg \max _{X \in F \backslash S}\{I(S ; C)+I(C ; X \mid S)\}
$$

At each iteration, for all $X \in F \backslash S, I(S ; C)$ in Eq.(47) is the same. For the IAMB algorithm, by Eq.(47), at each iteration, maximizing $I(C ; X \mid S)$ is equivalent to maximizing $I((S, X) ; C)$. By $I(C ; F)=I(C ; S)+I(C ; \bar{S} \mid S)$, when $I(C ; \bar{S} \mid S)=0$, then $I(C ; S)$ is maximized. At the forward step, IAMB greedily maximizes $I(C ; X \mid S)$ until for $\forall X \in F \backslash S$, $I(C ; X \mid S)=0$. Then by Lemma 4, all parents and children of $C(P C(C))$ will be gradually added to $S$, while by Properties 5 and 6, the ancestors and descendants of $C$ may not be added to $S$. Let the set $S P(C)$ include all spouses of $C$, when all parents and children of $C$ are added to $S$, by Lemma $5, \forall X \in S P(C), I(X ; C \mid S)>0$, and thus all spouses of $C$ will be added to $S$ initially during the forward step. In any case, at the end of the forward step, all features in the true $M B(C)$ will have been added to $S$.

At the backward step, $\exists Y^{*} \in S$ to be removed from $S$ satisfies

$$
Y^{*}=\arg \min _{Y \in S} I(Y ; C \mid S \backslash Y)
$$

By Eq.(48), at each iteration, if $I(C ; Y \mid S \backslash Y)=0$, IAMB will remove $Y$ from $S$ until given any feature $Y \in F \backslash S, I(Y ; C \mid S \backslash Y)>0$. Then all false positives in $S$ are removed, and thus $S=M B(C)$. By Theorem 2, the theorem is proved.

Inter-IAMB. IAMB surfers from the problem of the addition of false positives to $S$ at the forward step, then makes the size of $S$ possibly become high-dimensional. The InterIAMB strategy mitigates the problem by interleaving the forward and backward steps of IAMB to keep $S$ as small as possible, then maximizes $I(C ; X \mid S)$ for $X \in F \backslash S$ and minimizes $I(C ; Y \mid S \backslash Y)$ for $Y \in S$ simultaneously.

Theorem 4 The output of Inter-IAMB is the optimal set $S^{*}$ in Eq.(12).
Proof: At each iteration, by Eq.(47), the forward step adds a new feature $X \in F \backslash S$ that maximizes $I(C ; X \mid S)$ to $S$. Once the new feature $X$ is added to $S$, the backward step is triggered immediately and removes features in $S$ (false positives) that minimize Eq.(48). By maximizing $I(C ; X \mid S)$ and minimizing $I(Y ; C \mid S \backslash Y)$ simultaneously, the strategy will convergence that for $\forall X \in F \backslash S, I(X ; C \mid S)=0$ and $\forall Y \in S, I(Y ; C \mid\{S \backslash Y\})>0$. After the backward step, $S=M B(C)$. Then by Theorem 2, the theorem is proved.

The time complexity of IAMB and Inter-IAMB above is measured in the number of conditional independence tests (association computations) executed. For IAMB and InterIAMB, the average time complexity is $O(n|S|)$ and the worst time complexity is $O\left(n^{2}\right)$ where $n$ is the total number of features and in the worst case with $|S|=n$.

Compare to non-causal feature selection, IAMB and Inter-IAMB both use the entire set of $S$ as the conditioning set for the calculation of $I(X ; C \mid S)$ at each iteration. By Eq.(45) in Section 5.2.4, assuming $S_{\max }$ is the largest conditioning set during MB search, thus the minimum number of data samples $N$ required by IAMB and Inter-IAMB is $r_{X_{\max }} \times r_{C} \times$ $r_{S_{\max }}$. Then the number of data instances required by IAMB and Inter-IAMB will increase exponentially in the size of $S$. To mitigate this drawback, in the next section, we will discuss a divide-and-conquer strategy.

# 5.3.2 A DIVIDE-AND-CONQUER STRATEGY BY CONDITIONING ON ALL SUBSETS OF $S$ FOR CALCULATING $I(X ; C \mid S)$ IN Eq.(21) 

The main idea behind a divide-and-conquer strategy is that: (1) finding $P C(C)$ and $S P(C)$ separately, and (2) using a feature-subset enumeration strategy to explore subsets of $S$ for discovering $P C(C)$ instead of conditioning on the entire set of $S$. That is, to calculate $I(C ; X \mid S)$, the divide-and-conquer strategy performs a search for a subset, $S^{\prime} \subseteq S$ such that if $X$ and $C$ are conditional independent given $S^{\prime}$, i.e. $I\left(C ; X \mid S^{\prime}\right)=0, X$ will not be added to $S$ and will never be considered as a candidate feature again. Then, the minimum number of data samples $N$ required by the divide-and-conquer strategy is $r_{X_{\max }} \times r_{C} \times r_{S^{\prime}}$ where $0 \leq\left|S^{\prime}\right| \leq\left|S_{\max }\right|$. Accordingly, on average, the divide-and-conquer strategy requires much smaller number of data samples than IAMB and Inter-IAMB. Specifically, the divide-and-conquer strategy mainly consists of the following two steps for solving Eq.(21).

- Discovering $P C(C)$. At each iteration, assuming $S$ is the set of features currently selected, for each candidate feature $X \in F \backslash S$, if $\exists S^{\prime} \subseteq S$ such that $X$ and $C$ conditional independent given $S^{\prime}$, i.e. $I\left(X ; C \mid S^{\prime}\right)=0, X$ is discarded and will never be considered as a candidate parent or child of $C$ again, otherwise $X$ is added to $S$. By Lemma 4, after this step, all parents and children will be added to $S$.
- Discovering $S P(C)$. By Lemmas 4 and $5, \forall X \in S P(C)$, there must exist a subset in $F \backslash\{X\}$ such that $X$ and $C$ are conditional independent given this subset. Therefore,

all spouses of $C$ cannot be added to $S$ at the PC discovery step. To find $S P(C)$, by Lemma $5, \forall X \in S$, the step employs the PC discovery step to find $P C(X)$, then for each feature $Y \in P C(X)$, if $\exists S^{\prime} \subseteq F \backslash\{Y, X\}$ such that $I\left(C ; Y \mid S^{\prime}\right)=0$ and $I\left(C ; Y \mid S^{\prime} \cup X\right)>0, Y \in S P(C)$.

There are four representative approaches to instantiate the divide-and-conquer strategy, i.e. max-min heuristic, simple max-heuristic, backward heuristic, and k-greedy heuristic. The representative algorithms include MMMB (Tsamardinos et al., 2003a), HITONMB (Aliferis et al., 2003), IPC-MB (Fu and Desmarais, 2008), and STMB (Gao and Ji, 2017).

1. The max-min heuristic. The representative algorithm using the strategy is the MMMB algorithm, which includes the following two steps.
(1) Discovering $P C(C)$ step. This step includes a forward step and a backward step to find $P C(C)$. To select the feature $X^{*} \in F \backslash S$ to maximize $I(C ; X \mid S)$, the forward and backward steps are implemented as follows.

- Forward step. The max-min heuristic selects the feature that maximizes the minimum correlation with $C$ conditioned on the subsets of $S$. Specifically, initially $S$ is an empty set, $\forall X \in F \backslash S$, the minimum correlation, denoted as $\operatorname{corr}(C ; X \mid S)$, between $C$ and $X$ conditioned on all possible subsets of $S$, is calculated as Eq.(49) below.

$$
\operatorname{corr}(C ; X \mid S)=\min _{S^{\prime} \subseteq S} I\left(C ; X \mid S^{\prime}\right)
$$

$X^{*} \in F \backslash S$ will be added to $S$ if $\operatorname{corr}\left(C ; X^{*} \mid S\right)>0$ and Eq.(50) below hold.

$$
X^{*}=\arg \max _{X \in\{F \backslash S\}} \operatorname{corr}(C ; X \mid S)
$$

The forward step stops until $\forall X \in F \backslash S, \operatorname{corr}(C ; X \mid S)=0$.

- Backward step. Each feature in $S$ selected at the forward step will be checked. If $\exists Y \in S$ satisfies Eq.(51) below, it will be removed from $S$ and never considered again.

$$
\exists S^{\prime} \subseteq S \backslash Y, I\left(C ; Y \mid S^{\prime}\right)=0
$$

(2) Discovering $S P(C)$ step. At the step, the max-min heuristic firstly finds the set of parents and children for each feature in $S$ found at the forward step. Assuming $X \in P C(C)$ and $Y \in P C(X)$, if $Y \notin P C(C)$ and $\exists S^{\prime} \subset F \backslash\{X, Y\}$ to make Eq.(52) below hold, then $Y$ is a spouse of $C$.

$$
I\left(C ; Y \mid S^{\prime}\right)=0 \text { and } I\left(C ; Y \mid S^{\prime} \cup X\right)>0
$$

2. Interleaving max-heuristic. The main difference between the max-heuristic and the interleaving max-heuristic is that in the discovering $P C(C)$ step, the interleaving maxheuristic interleaves the forward and backward steps to keep the size of $S$ as small as possible. The representative algorithm using the strategy is the HITON-MB algorithm.
(1) Discovering $P C(C)$ step. In the step, the interleaving max-heuristic uses a simpler forward strategy than the max-min heuristic. Before interleaving forward and backward steps, $\forall X \in F$, the interleaving max-heuristic computes $I(C ; X)$ and adds the features

![img-5.jpeg](img-5.jpeg)

Figure 6: An example of the false positive $D$ being added to $S$ in the discovering $P C(C)$ step using the max-min heuristic or its interleaving version
that satisfy $I(C ; X)>0$ to the candidate $P C(C)$ set, called $S P C(C)$, in descending order according to the value of $I(C ; X)$. If $I(C ; X)=0, X$ will be discarded and never considered as a candidate parent or child again. Then, initially $S$ is an empty set, and for each feature in $S P C(C)$, this strategy interleaves Eq.(53) and Eq.(54) as follows, until $S P C(C)$ is empty.

- Forward step. $\forall X \in S P C(C)$, if $X$ satisfies Eq.(53) below, it will be added to $S$.

$$
X^{*}=\arg \max _{X \in S P C(C)} I(C ; X)
$$

- Backward step. Once $X$ is added to $S$ at the forward step, the backward step is triggered. Specifically, $S P C(C)=S P C(C) \backslash X$, and $\forall Y \in S$, if $\exists S^{\prime} \subseteq S \backslash Y$ satisfies Eq.(54) below, $Y$ will be removed from $S$ and never considered again.

$$
I\left(C ; Y \mid S^{\prime}\right)=0
$$

(2) Finding spouses. The step is the same as the max-min heuristic in Eq.(52).

Comparing to the simultaneous discovery strategy to discover MBs in Section 5.2.1, the strategies in this section perform an subset search within $S$ instead of conditioning on the entire $S$. Thus, for the max-min heuristic and its interleaving version, the time complexity is $O\left(M|S|^{2} 2^{|S|}\right)$ where $|S|$ denotes the largest size of $S$ during forward and backward steps.

Theorem 5 Using the max-min heuristic or its interleaving version, in the discovering $P C(C)$ step, $P C(C) \subseteq S$ (Tsamardinos et al., 2006; Aliferis et al., 2010a).

Theorem 5 states that in addition to $P C(C)$, the output of the discovering $P C(C)$ step, i.e. $S$, may include some false positives. For example, in Figure 6, assuming $C$ is the target feature, $B, A$, and $D$ is a child, spouse, and descendant of $C$, respectively, $D$ will enter and remain in $S$ in the discovering $P C(C)$ step (Aliferis et al., 2010a). The explanation is as follows. $C$ and $D$ are dependent conditioning on the empty set, since the path $C \rightarrow B \rightarrow D$ d-connects $C$ and $D$. By conditioning on $\{B\}$, the path $C \rightarrow B \leftarrow A \rightarrow D$ d-connects $C$ and $D$ by Definition 6 .

To remove false positives from $S$, such as $D$, the two max-min heuristics employ a symmetry correction. The idea behind the symmetry correction is that in a Bayesian network, if $X \in P C(C)$, then $C \in P C(X)$. With the symmetry correction, in the discovering $P C(C)$ step, the work (Tsamardinos et al., 2006; Peña et al., 2007) proved that $S=P C(C)$. And

with symmetry corrections, the work (Aliferis et al., 2010a) proved that the output of the two max-min heuristics is $M B(C)$, that is, $S=M B(C)$, and thus Theorem 6 below holds.

Theorem 6 The output of the max-min heuristic (and its interleaving version) employed by MMMB (and HITON-MB) is the optimal set $S^{*}$ in Eq.(12) with symmetry correction.
3. The backward strategy. The IPC-MB (Fu and Desmarais, 2008) and STMB (Gao and Ji, 2017) algorithms only employ a backward step to discover $P C(C)$ instead of using a forwardbackward strategy. Initially, by setting $S=F$, the backward step removes features from $S$ one by one, instead of greedily adding features to $S$ one by one for maximizing $I(C ; S)$. Specifically, in the discovering $P C(C)$ step, for $\forall Y \in S$, if $\exists S^{\prime} \subseteq S \backslash Y$ and $\left|S^{\prime}\right|=0$ (i.e., the size of $S^{\prime}$ equals to 0 ) such that $I\left(Y ; C \mid S^{\prime}\right)=0, Y$ is removed from $S$. Otherwise, if $\exists S^{\prime} \subseteq S \backslash Y$ and $\left|S^{\prime}\right|=1$ such that $I\left(Y ; C \mid S^{\prime}\right)=0, Y$ is removed from $S$. The backward step continues in this way by performing level by level of the size of $S^{\prime}$, until the size of the current $S^{\prime}$ is larger than the size of the current $S$.

This backward strategy employed by IPC-MB also finds a superset of $P C(C)$, that is, $P C(C) \subseteq S$. Thus, IPC-MB embeds a symmetry correction in the spouse discovery stage to remove false positives in $S$. To find spouses, IPC-MB adopts the same idea with MMMB and HITON-MB.

STMB also employs the backward step to discover $P C(C)$. But STMB has two main differences against IPC-MB. Firstly, STMB finds $S P(C)$ in $F \backslash S$, instead of parents and children of each feature in $S$. Secondly, STMB uses the found spouses to remove false positives in $S$ found in the discovering $P C(C)$ step instead of using a symmetry correction during the $S P(C)$ discovery step. Specially, assuming $S$ found in the discovering $P C(C)$ step and $S P(C)=\emptyset$, the idea of discovering spouses are summarized below.

- Finding spouses and removing false parents and children from $S$ : for each feature $X \in F \backslash S$, if $\exists Y \in S$ and $\exists S^{\prime} \subset F \backslash\{X \cup Y\}$ s.t. $I\left(C ; X \mid S^{\prime}\right)=0$ and $I\left(C ; X \mid S^{\prime} \cup Y\right)>0$, then $X$ is added to $S P(C)$. Once $X$ is added to $S P(C)$, for each feature $Y \in S$, if $\exists S^{\prime} \subseteq\{S \cup X\} \backslash Y$ s.t. $I\left(C ; Y \mid S^{\prime}\right)=0$, then $Y$ and $X$ are removed from $S$ and $S P(C)$, respectively. The process terminates until all features in $F \backslash S$ are checked.
- Removing false positives from $S P(C)$ and $S$ : (1) $\forall X \in S P(C)$, if $I(X ; C \mid S \cup S P(C) \backslash$ $X)=0, X$ is removed from $S P(C)$; then (2) $\forall Y \in S$, if $I(Y ; C \mid S \cup S P(C) \backslash Y)=0$, $Y$ is removed from $S$.

IPC-MB and STMB have been proved that $\{S \cup S P(C)\}=M B(C)$ (Gao and Ji, 2017; Fu and Desmarais, 2008). Thus, IPC-MB and STMB greedily find the optimal set $S^{*}$ in Eq.(12). The time complexity of IPC-MB includes finding both $P C(C)$ and $S P(C)$, then the complexity is $O\left(n 2^{|S|}+|S| n 2^{|S|}\right)=O\left(|S| n 2^{|S|}\right)$ where $|S|$ is the largest size of conditional set during search. The worst time complexity of IPC-MB is $O\left(n 2^{n}+n^{2} 2^{|S|}\right)=$ $O\left(n^{2} 2^{|S|}\right)$ when all features are parents and children of $C$. For STMB, and the average time complexity is $O\left(n 2^{|S|}+|S||F \backslash S| 2^{|S|}\right)=O\left(|S||F \backslash S| 2^{|S|}\right)$, and the worst time complexity is $O\left(n 2^{n}+n^{2} 2^{|S|}\right)=O\left(n^{2} 2^{|S|}\right)$.
4. $\gamma$-greedy heuristic. In the discovering $P C(C)$ step, as the size of $S$ becomes large, it will be computationally expensive or prohibitive when we perform an exhaustive enumeration over all subsets of $S$. For example, to check whether $X$ is able to be added

![img-6.jpeg](img-6.jpeg)

Figure 7: (a) A NB to a selective NB (b) a TAN to a selective TAN (c) a 2-DB to selective 2-DB (d) a general Bayesian network to a MB-based Bayesian network classifier
to $S$, in the worst case, the total number of subsets checked is up to $2^{|S|}$. Accordingly, in the discovering $P C(C)$ step, MMMB, HITON-MB, IPC-MB and STMB employ a $\gamma$-greedy search method to mitigate this problem. The $\gamma$-greedy search checks all subsets of size less than or equal to a user-defined parameter $\gamma(0 \leq \gamma<|S|)$, that is, the maximum size of subsets needed to be checked. In the case of using the $\gamma$-greedy heuristic, MMMB, HITON-MB, IPC-MB and STMB return an approximate $M B(C)$ (Aliferis et al., 2010a).

# 5.4 Practical implication 

In Section 5.2 and Section 5.3, we discussed the Bayesian network structural assumptions and analyzed in detail how the assumptions led to the different levels of approximations employed by causal and non-causal feature selection methods for the calculation of $I(X ; C \mid S)$. With the structural assumptions, we are able to fill in the gap in our understanding of the relation between the two types of feature selection methods.

Firstly, the feature sets obtained by causal feature selection methods are closer to $M B(C)$ than non-causal feature selection methods. However, our analysis in Sections 5.2 and 5.3 shows that non-causal feature selection methods are much more computationally efficient and have lower sample requirement than causal feature selection methods. The choice of causal or non-causal feature selection methods depends on the size of the dataset under study.

Secondly, the strongly relevant features are the same as the MB of $C$. This may motivate us to leverage the advantages of both causal and non-causal feature selection methods to develop more efficient and robust new feature selection methods.

Thirdly, causal and non-causal feature selection methods implicitly reduce a full Bayesian network classifier to a selective Bayesian network classifier by selecting a subset of features $S$ to make the conditional likelihood $P(C \mid S)$ as close to $P(C \mid F)$ as possible, as shown in Figure 7.

# 6. Error Bounds 

In the section, we will discuss the error bounds of non-causal and causal feature selection for understanding the impact of assumptions and approximations made by the two types of methods on classification performance. Since both types of methods are independent of any classifiers, we will analyze the bounds of difference in the information gains between an approximate MB and an exact MB. In Section 3, Eq.(17) has presented that if a subset $S$ in $D$ maximizing $I(C ; S)$, then $S$ also maximizes $L(C \mid S, D)$ and minimizes $P_{\text {err }}$. Based on Eq.(17), using information gain, in the following, we will discuss the bounds of the difference between an approximate MB and an exact MB.

### 6.0.1 Conditioning on the full $S$ and its all subsets (exact MB discovery)

According to our analysis in Section 5.3, under certain assumptions, causal feature selection algorithms designed with conditioning on both the full $S$ and all of its subsets can find the exact $M B(C)$ from data. Moreover, the algorithms by conditioning on all subsets of $S$ are also able to find the exact $P C(C)$. As $I(C ; F \backslash M B(C) \mid M B(C))=0, I(C ; F)=$ $I(C ; M B(C))$. Since $H\left(P_{\text {err }}\right)^{-1} \leq P_{\text {ber }} \leq 1 / 2 H(C \mid F)$ (see Eq.(14)), Theorem 7 gives the minimum upper bound of $P_{\text {err }}$.

Theorem $7 P_{\text {err }} \leq 1 / 2 H(C \mid M B(C))$.
Proof: By Theorem 2, $\forall S \subseteq F, I(C ; M B(C)) \geq I(C ; S)$ holds. Since $H(C \mid M B(C))=$ $H(C)-I(C ; M B(C))$ and $H(C \mid S)=H(C)-I(C ; S)$, we get that $\forall S \subseteq F, H(C \mid M B(C)) \leq$ $H(C \mid S)$. By Eq.(15), the theorem is proven.

By Eq.(16), $\lim _{m \rightarrow \infty}-\ell(C \mid S, D)=K L(p(C \mid S) \| q(C \mid S))+H(C \mid S)$. As $m \rightarrow \infty$, $K L(p(C \mid S) \| q(C \mid S))$ will approach zero, and thus Eq.(55) presents that $H(C \mid M B(C))$ minimizes $-\ell(C \mid M B(C), D)$.

$$
\lim _{m \rightarrow \infty}-\ell(C \mid M B(C), D) \approx H(C \mid M B(C))
$$

If $S=P C(C)$ holds, by Theorem 2, $I(M B(C) ; C) \geq I(P C(C) ; C)$ holds. Thus, $H(C \mid M B(C)) \leq H(C \mid P C(C))$ holds, and Eq.(56) below gives the Bayes error rates of $P C(C)$, that is, $P_{\text {err }}(P C(C))$. Since $H(C \mid M B(C)) \leq H(C \mid P C(C))$, the upper bound in Eq.(56) is looser than that in Eq.(55).

$$
P_{\text {err }}(P C(C)) \leq 1 / 2 H(C \mid P C(C))
$$

Since $\lim _{m \rightarrow \infty}-\ell(C \mid P C(C), D) \approx H(C \mid P C(C))$, Eq.(57) below gives the upper bound of the conditional log-likelihood of $P C(C)$ in $D$, that is, $-H(C \mid M B(C))$.

$$
\lim _{m \rightarrow \infty} \ell(C \mid P C(C), D) \leq-H(C \mid M B(C))
$$

### 6.0.2 Conditioning on the Subsets of $S$ up to size $\gamma$ (Causal feature SElection).

As we discussed in Section 5.3, the $\gamma$-greedy search employed by causal feature selection methods may return an approximate $M B(C)$. Let $A M B(C) \subseteq F$ be an approximate MB

of $C$, by Theorem $2, H(C \mid M B(C)) \leq H(C \mid A M B(C))$ holds. Since Theorem 7 illustrates that $1 / 2 H(C \mid M B(C))$ is the minimum upper bound of $P_{\text {err }}$, thus, we get

$$
P_{\text {err }}(A M B(C)) \leq 1 / 2 H(C \mid M B(C))
$$

Since $\lim _{m \rightarrow \infty}-\ell(C \mid A M B(C), D) \approx H(C \mid A M B(C))$ holds, the upper bound of the conditional log-likelihood of any approximate MB of $C$ is

$$
\lim _{m \rightarrow \infty} \ell(C \mid A M B(C), D) \leq-H(C \mid M B(C))
$$

# 6.0.3 Conditioning on the Subset of size 0 or 1 (non-Causal feature SELECTION). 

As discussed in Section 5.2, non-causal feature selection algorithms attempt to find $P C(C)$ and some spouses of $C$. With different values of $\psi$ (i.e. the number of selected features), those strategies may return an approximate $M B(C)$, that is, a superset or a subset of $P C(C)$. In the following, we will focus on discussing the bounds of the superset or subset of $P C(C)$ found by non-causal feature selection methods.

Corollary 2 If $S 1 \subseteq F \backslash P C(C)$ and $S=P C(C) \cup S 1$,
(1) $-H(C \mid P C(C)) \leq \lim _{m \rightarrow \infty} \ell(C \mid S, D) \leq-H(C \mid M B(C))$;
(2) $1 / 2 H(C \mid M B(C)) \leq P_{\text {err }}(S) \leq 1 / 2 H(C \mid P C(C))$.

Proof: Assuming $\overline{P C(C)}=F \backslash P C(C)$ and $\bar{S}=F \backslash S$. Firstly, we prove that $I(C ; \overline{P C(C)} \mid P C(C)) \geq I(C ; \bar{S} \mid S)$ holds. By $I(C ; F)=I(P C(C) ; C)+I(C ; \overline{P C(C)} \mid P C(C))$, we get

$$
\begin{aligned}
I(C ; F) & =I((\bar{S}, S) ; C) \\
& =I(S ; C)+I(C ; \bar{S} \mid S) \\
& =I((P C(C), S 1) ; C)+I(C ; \bar{S} \mid S) \\
& =I(P C(C) ; C)+I(S 1 ; C \mid P C(C))+I(C ; \bar{S} \mid S)
\end{aligned}
$$

By the chain rule of mutual information, we can get

$$
I(S 1 ; C \mid P C(C))=\sum_{j=1}^{|S 1|} I\left(F_{j} ; C \mid F_{j-1}, \cdots, F_{1}, P C(C)\right)
$$

Since S1 only includes spouses, non-descendants and descendants of C. By Eq.(60) and Eq.(61), we get the following.

Case 1: if $\exists F_{j} \in S 1$ is a descendant of $C$ and $I\left(F_{j} ; C \mid F_{j-1}, \cdots, F_{1}, P C(C)\right)>0$, then $I(C ; \overline{P C(C)} \mid P C(C))>I(C ; \bar{S} \mid S)$ holds.

Case 2: if $\exists F_{j} \in S 1$ and $F_{j}$ is a spouse of $C$, then $I\left(F_{j} ; C \mid F_{j-1}, \cdots, F_{1}, P C(C)\right)>0$. Thus, $I(C ; \overline{P C(C)} \mid P C(C))>I(C ; \bar{S} \mid S)$ holds.

Case 3: if $F_{j} \in S 1$ is a non-descendant of $C$, by the Markov condition,
$I\left(F_{j} ; C \mid F_{j-1}, \cdots, F_{1}, P C(C)\right)=0$, then $I(C ; \overline{P C(C)} \mid P C(C))=I(C ; \bar{S} \mid S)$.
By $I(C ; S) \leq I(C ; M B(C)), I(C ; \bar{S} \mid S) \geq I(C ; \overline{M B(C)} \mid M B(C))$ holds. Then we get

$$
I(C ; \overline{P C} \mid P C(C)) \geq I(C ; \bar{S} \mid S) \geq I(C ; \overline{M B(C)} \mid M B(C))
$$

Then $I(C ; P C(C)) \leq I(C ; S) \leq I(C ; M B(C))$ holds. Thus, we get $H(C \mid P C(C)) \geq$ $H(C \mid S) \geq H(C \mid M B(C))$. Thus, (1) and (2) hold.

For a subset of $P C(C)$, assuming $S \subset P C(C), \bar{S}=F \backslash S$. If $P C(C)=\left\{S \cup S^{\prime}\right\}$, $I(C ; P C(C))=I(C ; S)+I\left(C, S^{\prime} \mid S\right)$. Since $I\left(C ; S^{\prime} \mid S\right)=\sum_{i=1}^{\left|S^{\prime}\right|} I\left(F_{i} ; C \mid F_{i-1}, \cdots, F_{1}, S\right)$ holds and $S^{\prime} \subset P C(C)$ ), then $I\left(C ; S^{\prime} \mid S\right)>0$. Thus, $I(C ; P C(C))>I(C ; S)$ holds. By $I(C ; F)=I(C ; P C(C))+I(C ; \overline{P C} \mid P C(C))$ and $I(C ; F)=I(C ; S)+I(C ; \bar{S} \mid S)$, then $I(C ; \overline{P C} \mid P C(C))<I(C ; \bar{S} \mid S)$. Accordingly, we can get the bounds between $S \subset P C(C)$ and $P C(C)$ in the following:

$$
\lim _{m \rightarrow \infty} \ell(C \mid S, D)<-H(C \mid P C(C)) \text { and } P_{\text {err }}(S)<1 / 2 H(C \mid P C(C))
$$

By the analysis above, we can see that the errors of causal and non-causal feature selection methods are bounded by $1 / 2 H(C \mid M B(C))$ and $1 / 2 H(C \mid P C(C))$, respectively. This indicates that the error bound of non-causal feature selection is looser than that of causal feature selection. Therefore, referring back to Figure 4, our analysis in this section validates that as causal feature selection methods make no assumption on the structure of the Bayesian network representing dependency of variables, their search strategies are able to find the exact $M B(C)$, while the strong assumptions made by non-causal feature selection methods lead to an approximate $M B(C)$ (referring back to Figure 3).

# 7. Experiments 

In this section, we will conduct extensive experiments to validate our findings of causal and non-causal feature selection, with the following focuses:

- In Section 7.1, we validate Theorem 2 in Section 4.2 (i.e. the MB of $C$ is the optimal set for feature selection), the discussion in Section 5.2.5 (causal interpretations of noncausal feature selection), and the proposed error bounds in Section 6 using a set of synthetic data sampled from a benchmark Bayesian network.
- In Section 7.2, as seen in the experiment results, we investigate the impact of different levels of approximations made by causal and non-causal feature selection methods on classification performance, the computational and accuracy performance of causal and non-causal feature selection methods, and the impact of data sample sizes on both methods using 25 various types of real-world datasets, including six datasets with large data samples, six datasets with extreme small samples, seven datasets with multiple classes, and six class-imbalanced datasets.

To carry out these validations, we have selected the following eight representative feature selection methods:

- Five representative causal feature selection methods, including three MB discovery algorithms, IAMB, HITON-MB, MMMB and two PC discovery algorithms, HITONPC and MMPC and we use the implementations of these algorithms obtained from http://www.dsl-lab.org/causal_explorer;
- Three representative non-causal feature selection algorithms: mRMR, JMI, and CMIM since these three algorithms provides better tradeoff in terms of accuracy and scalability than the other non-causal feature selection algorithms (especially with small-sized

![img-7.jpeg](img-7.jpeg)

Figure 8: The ALARM Bayesian network
data samples) (Brown et al., 2012). We use the implementations of mRMR, JMI, and CMIM obtained from https://github.com/Craigacp/FEAST.

To evaluate the selected features by each algorithm for classification, in all experiments, we use Naive Bayes classifier (NBC) and k-Nearest Neighbor (KNN) classifier since SVMs, Random Forests, and Decision trees implicitly embed a feature selection process into themselves while NB and KNN do not. All experiments were performed on a Window 7 Dell workstation with an Intel(R) Core(TM) i5-4570, 3.20GHz processor and 8.0GB RAM, and all eight feature selection methods under comparison are implemented in MATLAB, and NBC and KNN are implemented in MATLAB2014 Statistics Toolbox. In the tables in Section 7, the notation " $A \pm B$ " denotes that "A" is the average performance of an algorithm on a dataset, such as prediction accuracy, while "B" represents the corresponding standard deviations of the average performance.

# 7.1 Experiments using synthetic datasets 

In this section, we will validate $M B(C)$ is the optimal set for feature selection (Theorem 2 in Section 4.2) and the proposed error bounds in Section 6 using a set of synthetic data sampled from the ALARM (A Logical Alarm Reduction Mechanism) network, a benchmark and well-known Bayesian network modelling an alarm message system for patient monitoring (Beinlich et al., 1989). This network includes 37 variables and the complete structure of the network is shown in Figure 8. Since the MB of each variable can be read from the network, we are able to evaluate the performance of the feature selection methods against the true MBs.

In the ALARM network, we choose the "HR" (Heart Rate) variable as the class attribute for classification. The variable takes three class labels, "low", "normal", and "high", and has the largest MB among all variables, including one parent, four children, and three

Table 2: Prediction accuracy of true MB against causal and non-causal algorithms


Table 3: Precision and Recall of each algorithm for MB discovery


spouses. We randomly sampled 10 training datasets with 5,000 training cases (large-sized data samples) and 50 training cases (small-sized data samples) respectively. For each training dataset, we randomly sampled a testing dataset with 1,000 testing cases. The reported prediction accuracy is the average accuracy of a classifier using the feature sets selected over the 10 runs of a feature selection method on these 10 training datasets.

In all tables in Section 7.1, "TruePC" and "TrueMB" denote the ground-truths of PC and MB of "HR" in the network, respectively. For validating the discussion of causal interpretations of non-causal feature selection methods in Section 5.2.5, we use the following settings and evaluation metrics.

- We set the parameter $\psi$, i.e. the numbers of features selected by mRMR, JMI, and CMIM to the size of the true MB (or the true PC) of "HR" in the network, which is denoted as " $\psi=\mathrm{nMB}$ " (or " $\psi=\mathrm{nPC}$ ").
- We use the average precision and recall metrics using the feature sets selected over the 10 runs of a feature selection method on the 10 training datasets to observe the percentage of the MB (or the direct causes and direct effects) of "HR" included in the selected features (the output) of each algorithm. The precision metric is the number of true positives in the output (i.e. the variables in the output belonging to the true MB (or PC) of "HR" in the ALARM network) divided by the number of variables in the output of an algorithm. The recall metric is the number of true positives in the output divided by the number of true positives (the number of the true MB (or PC) of "HR" in the alarm network).
- We use the prediction accuracy, the ratio between the number of correct predictions and the total number of testing data samples to validate Theorem 2 presented in Section 4.2 and the error bounds proposed in Section 6.

Table 4: Number of parents and children (PC), spouses (SP), and false positives (FP)


Table 5: Prediction accuracy of true PC against causal and non-causal algorithms


# 7.1.1 Validation of Theorem 2 and the discussion in Section 5.2.5 

In this section, we will validate Theorem 2 (i.e. the MB of $C$ is the optimal set for feature selection), and the discussion of causal interpretations of non-causal feature selection in Section 5.2.5.

Validating Theorem 2. Table 2 reports the average prediction accuracies and standard deviations using the datasets containing 5,000 and 50 training cases, respectively. Table 2 states that using both KNN and NBC, the true MB of "HR" achieves the highest prediction accuracy than the feature subsets selected by IAMB, HITON-MB, MMMB, mRMR, CMIM, and JMI. Table 4 shows the number of parents and children (PC), spouses (SP), and false positives (FP) in the found feature set of each algorithm. These results indicate that classifiers using $M B(C)$ as the feature set achieve the best classifications results, which validates Theorem 2 in Section 4.2 .

From Tables 3 and 4, we can see that using 5000 cases, both MMMB and HITON-MB find the exact MB of "HR", and thus get the same prediction accuracy as the true MB of "HR", while the other four algorithms do not find the exact MB of "HR". In addition, from Table 4, we can see that except for IAMB, all feature sets found by the other five algorithms include all variables within the PC set of "HR". This explains why the IAMB, mRMR, JMI, and CMIM are very competitive on the prediction accuracy. CMIM and mRMR cannot find any spouses using 5000 cases.

Using 50 cases, in Table 2, mRMR gets the highest prediction accuracy among IAMB, MMMB, HITON-MB, CMIM, and JMI using both KNN and NBC, since it finds almost the same PC set as the other rivals, but achieves fewest false positives among all algorithms, as shown in Table 4. This shows that non-causal feature selection algorithms deal with smallsized data samples better than causal feature selection algorithms, which is consistent with our discussions of sample requirement in Section 5.

Validating the discussion presented in Section 5.2.5. Table 5 reports the prediction accuracies using MMPC, HITON-PC, mRMR, JMI, and CMIM, while Table 6

Table 6: Precision and Recall of each algorithm for PC discovery


![img-8.jpeg](img-8.jpeg)

Figure 9: mRMR and TurePC
illustrates the precision and recall of each algorithm for PC discovery. From Tables 4 to 6, we can see that the PC set of a target feature plays a key role in predicting the target. From Tables 5 to 6 , we can see that using 5000 cases (large-sized data samples), the three non-causal feature selection methods find the exact PC set of "HR", and thus they get the same prediction accuracy as the true PC set. Even using 50 cases (a small-sized data samples), Table 6 states that the three non-causal feature selection methods still prefer the features in the PC set of "HR". Therefore, Tables 4 to 6 provide strong evidence to support the discussion of causal interpretations of non-causal feature selection in Section 5.2.5.

# 7.1.2 VALIDATION OF ERROR BOUNDS IDENTIFIED IN SECTION 6 

In the section, we will examine the proposed error bounds in Section 6. To achieve the goal, we consider the prediction accuracy of the true PC set of "HR" as a baseline, since using the PC set of "HR", the prediction accuracy is almost the same as that using the MB set. Then we check the different prediction accuracies of different feature sets by varying the sizes of the selected feature sets by mMRM, CMIM, and JMI.
![img-9.jpeg](img-9.jpeg)

Figure 10: CMIM and TurePC

![img-10.jpeg](img-10.jpeg)

Figure 11: JMI and TurePC

From Figures 9 to 11, we can see that the prediction accuracies of mRMR, CMIM, and JMI are bounded by the prediction accuracy of the true PC set. The highest accuracy of the three algorithms was achieved with 5 to 8 selected features, where the PC set of "HR" includes 5 features and the true MB set has 8 features. Thus, those results further confirm the bounds proposed in Section 6.

# 7.2 Evaluation on real-world data 

In this section, we will conduct extensive experiments with 25 real-world datasets to examine the impact of different levels of approximations made by causal and non-causal methods on their performance, the time complexity of both methods, and the impacts of data sample sizes and different types of datasets on causal and non-causal feature selection algorithms, respectively. The 25 datasets are divided into four groups: (1) six datasets with large sample sizes and a small feature-to-sample ratio, i.e. "m $\gg \mathrm{n}$ "; (2) six datasets with a small sample-to-feature ratio, i.e. "m $\ll \mathrm{n}$ "; (3) seven datasets with multiple classes; (4) six datasets with extremely imbalanced class distributions.

In addition to prediction accuracy used in the previous section, we employ the following metrics to validate all the eight methods:

- Number of selected features;
- Computational efficiency (running time in seconds);
- AUC: Area Under the ROC (used for imbalanced datasets in Section 7.2.4);
- Kappa statistics.

The existing stability measures for feature selection always require that the two feature sets under comparison should contain the same number of features, but the eight feature selection methods used in the evaluation return different feature sets of different sizes. Thus, instead of comparing the stabilities of the features selected by the feature selection methods, in Section 7.2, we will use the Kappa statistics to measure the stability of a classifier built using the features selected by a feature selection method as an indication of the method's stability. The Kappa statistic is a measure of consistency amongst different raters, taking into account the agreement occurring by chance (Cohen, 1960). The statistic is standardized to lie on a -1 to 1 scale, where 1 is perfect agreement, 0 is exactly what would be expected by chance, and negative values indicate agreement less than chance. The detailed value

Table 7: Kappa statistic and its corresponding Kappa agreement


Table 8: Datasets with large sample sizes and a small feature-to-sample ratio


ranges of the Kappa statistics and their corresponding Kappa agreements are shown in Table 7 (Landis and Koch, 1977).

# 7.2.1 DATASETS WITH LARGE SAMPLE SIZES AND A SMALL FEATURE-TO-SAMPLE RATIO 

We select six datasets with of large numbers of samples and relatively small numbers of features from the UCI Machine Learning Repository (Bache and Lichman, 2013), as shown in Table 8. In the experiment, for mRMR, CMIM, and JMI, since it is hard to decide in advance a suitable parameter $\psi$, i.e., the number of selected features, for each of these algorithms, we set the user-defined values for $\psi$ to $5,10,15,20$, and 25 respectively for the algorithm and choose the feature subset with the highest prediction accuracy as the final feature set selected by the algorithm.

Tables 9 and 10 report the prediction accuracy of each algorithm using NBC and KNN, respectively. Table 9 illustrates that with NBC, the non-causal feature selection methods almost have the same performance as the causal feature selection algorithms. IAMB is a bit better than mRMR, CMIM, and JMI. Meanwhile, MMPC and HITON-PC achieve good performance. From Table 10, we can see that with KNN, MMMB and HITON-MB get better accuracy than mRMR, CMIM, and JMI.

Tables 11 and 12 report the Kappa statistic of each algorithm using KNN and NBC, respectively. From Table 11, we can see that MMPC and HITON-PC achieve better Kappa statistics than the other algorithms except for the madelon dataset. In Table 12, HITONMB and MMMB are better than the other algorithms, except for the madelon dataset. These results are consistent with those indicated by Tables 9 and 10.

Tables 14 shows the running time of each algorithm. Clearly, among all causal feature selection algorithms, IAMB is the fastest. However, MMPC, HITON-PC, HITON-MB, and MMMB need to check the subsets of the feature subset currently selected, therefore they show higher time complexity than IAMB. Moreover, by combining the running time in Tables 14 and the number of features selected in Table 13, we can see that more features are selected, more expensive the computations of MMPC, HITON-PC, HITON-MB, and MMMB are. Regarding the time complexity of the non-causal feature selection methods, as we discussed at the beginning of Section 5 and in Figure 4, mRMR, CMIM, and JMI use

![img-11.jpeg](img-11.jpeg)

Figure 12: Prediction accuracy with different values of $\psi$ using NBC
![img-12.jpeg](img-12.jpeg)

Figure 13: Prediction accuracy with different values of $\psi$ using KNN

Table 9: Prediction accuracy using NBC


Table 10: Prediction accuracy using KNN


pairwise comparisons, and thus are faster than all causal feature selection algorithms, and this is validated by the result in Table 14.

From Table 13, we can see that MMPC and HITON-PC select fewer features than MMMB and HITON-MB, while IAMB selects the fewest features among the eight algorithms. For the gisstee dataset, MMPC, HITON-PC, MMMB, and HITON-MB select significantly more features than the other algorithms, since the features in the dataset are highly correlated. IAMB only selects two features, because the conditioning set is large and requires large number of data samples, and thus may lead to unreliable many conditional tests. This also explains why the prediction accuracy of IAMB in Table 10 is significantly low than the other algorithms.

Finally, Figures 12 and 13 report the predication accuracy of the causal feature selection methods (with the highest prediction accuracy) in comparison with the three non-causal feature selection methods, mRMR, CMIM and JMI when the number of features selected by the three methods are varied. From Figures 12 and 13, we can see that, either with KNN or NBC, for all datasets except for madelon, causal feature selection method always outperforms all the three non-causal feature selection methods regardless the number of selected features specified for these non-causal methods. This result has demonstrated that causal feature selection methods, when the dataset contains sufficient large number of samples, the features selected by them would be closer to the optimal feature set, i.e. the MB of the class attribute.

Table 11: Kappa statistic using NBC


Table 12: Kappa statistic using KNN


# 7.2.2 DATASET WITH HIGH DIMENSIONALITY AND SMALL NUMBER OF DATA SAMPLES 

In this section, we will evaluate the eight feature selection methods using the six datasets with high dimensionality and relatively small numbers of samples. Table 15 provides a summary of the datasets. In the following tables reporting the results, "-" denotes that an algorithm fails to obtain any result with a dataset because of excessive running time. We will do the same for the experiments in Sections 7.2.3, 7.2.4, and ??. Since mRMR, CMIM, and JMI use a user-defined parameter $\psi$ to control the size of features selected and the datasets in Table 15 are high dimensionality, we set $\psi$ to the top $5,10,15, \cdots, 35$, and 40 respectively, then report the results about the feature subset with the highest prediction accuracy.

In Tables 16 and 17, we can see that using KNN and NBC, the non-causal feature selection methods, mRMR, CMIM, and JMI, all outperform the causal feature selection methods, MMPC, HITON-PC, MMMB, HITON-MB, and IAMB. This illustrates that with datasets of high dimensionality and small sample size, as the number of data instances is not enough to support causal feature selection algorithms for reliable conditional independence tests, whereas mRMR, CMIM, and JMI can cope with such datasets. This validates our analysis of sample requirement in Section 5.

In addition with mRMR, CMIM, and JMI, we can tune the parameter $\psi$ to control the size of the selected feature set for the trade-off between search efficiency and prediction accuracy. Accordingly, from Tables 18 and 19, mRMR, CMIM, and JMI can get

Table 13: Number of selected features ("A/B" denotes that "A" represents the number of features with the highest accuracy corresponding to an algorithm using NBC and "B" is the number of features with the highest accuracy corresponding to an algorithm using KNN)


Table 14: Running time (in seconds)


more stable features, as indicated by the better Kappa statistic than MMPC, HITONPC, MMMB, HITON-MB, and IAMB. Meanwhile, Table 20 shows that the computational costs of HITON-PC, MMMB, HITON-MB are very expensive and even prohibitive on some datasets, such as prostate, dorothea, and leukemia. The explanation is that the class attribute in each of the datasets may have a large PC set or MB set, as shown in Table 21, then this leads to that MMPC, HITON-PC, MMMB, and HITON-MB needs to check an exponential number of subsets.

Figures 14 and 15 report the predication accuracy of the causal feature selection methods (with the highest prediction accuracy) in comparison with the three non-causal feature selection methods, mRMR, CMIM and JMI when the number of features selected by the three methods are varied.

From Figures 14 and 15, we can see that, either with KNN or NBC, for all datasets, the three non-causal feature selection methods always outperforms most of causal feature selection methods. This result has demonstrated that causal feature selection methods, when the dataset contains high dimensionality and relatively small number of data samples, the causal feature selection methods is worse than non-causal feature selection methods.

The results in Figures 12, 13, 14, and 15 validate that on the one hand, with a large dataset with sufficient number of samples, causal feature selection methods tend to find an exact MB; on the other hand, non-causal feature selection methods can deal with datasets with a small number of data samples and high-dimensionality better.

# 7.2.3 DATASET WITH MULTIPLE CLASSES 

In this section, we will evaluate the eight feature selection methods using the seven datasets with multiple classes. Table 15 provides a summary of the datasets. As for mRMR, CMIM, and JMI, we set $\psi$ to the top $5,10,15,20$, and 25 , respectively, then report the results about the feature subset with the highest prediction accuracy.

Table 15: Dataset with high dimensionality and small data sample sizes


Table 16: Prediction accuracy using NBC


Table 17: Prediction accuracy using KNN


Table 18: Kappa statistic using NBC


![img-13.jpeg](img-13.jpeg)

Figure 14: Prediction accuracy with different values of $\psi$ using NBC

Table 19: Kappa statistic using KNN


Table 20: Running time (in seconds)


![img-14.jpeg](img-14.jpeg)

Figure 15: Prediction accuracy with different values of $\psi$ using KNN
Table 21: Number of selected features


From Tables 23 and 24, we can see that given a dataset with a small number of features and a large number of data instances, even if the dataset with a large number of classes, MMPC, HITON-PC, MMMB, and HITOM-MB have almost the same prediction accuracy as three non-causal feature selection, and even better than them on some datasets, such as the landsat dataset with six classes. Meanwhile, Tables 25 and 26 shows that MMPC, HITON-PC, MMMB, HITOM-MB, and IAMB achieve better Kappa statitic on the connect4, splice, waveform, and landsat datasets, using both KNN and NBC.

However, given a dataset with a very small number of data instances and a larger number of classes, MMPC, HITON-PC, MMMB, HITOM-MB, and IAMB fail to select any features due to data inefficiency, while mRMR, CMIM, and JMI seem to work well, especially CMIM. Tables 27 and 28 report the number of selected features and running time of each algorithm. We can see that as expected, mRMR, CMIM, and JMI are faster than MMPC, HITON-PC, MMMB, HITOM-MB, and IAMB.

Figures 16 and 17 report the predication accuracy of the causal feature selection methods (with the highest prediction accuracy) in comparison with the three non-causal feature selection methods, mRMR, CMIM and JMI when the number of features selected by the

Table 22: Dataset with multiple classes


Table 23: Prediction accuracy using NBC


three methods are varied. From 16 and 17, we can see that, either with KNN or NBC, given a dataset with multiple classes, if the dataset has a large number of data samples, causal feature selection can work well, and they perform better than non-causal feature selection on most of the datasets. However, if the dataset has not enough data samples, causal feature selection fails, while non-causal feature selection can work well on the dataset.

# 7.2.4 DATASET WITH IMBALANCED CLASSES 

In this section, we use six class-imbalanced datasets in Table 29 to examine the performance of causal and non-causal feature selection methods. For mRMR, CMIM, and JMI, we set $\psi$ to the top $5,10,15, \cdots, 25$, and 30 , then select the feature subset with the highest prediction accuracy as the reporting result.
![img-15.jpeg](img-15.jpeg)

Figure 16: AUC with different values of $\psi$ using NBC

Table 24: Prediction accuracy using KNN


![img-16.jpeg](img-16.jpeg)

Figure 17: AUC with different values of $\psi$ using KNN

From Tables 30 and 31, we can see that all the eight algorithms get good prediction accuracy, but each of them achieves a very low AUC, as seen from Tables 32 and 33. In addition, on both prediction accuracy and AUC, the five causal feature selection methods and the three non-causal feature selection algorithms achieve almost the same performance.

Table 25: Kappa statistic using NBC


Table 26: Kappa statistic uisng KNN


Table 27: Number of selected features


Table 28: Running time (in seconds)


Table 29: Class-imbalanced datasets


Table 30: Prediction accuracy using NBC


At the same time, as see from Tables 34 and 35, all the eight algorithms do not achieve better Kappa statistic regardless of using both KNN and NBC.

Tables 36 and 37 report the number of selected features and running time of each algorithm. We can see that MMMB and HITON-MB are the slowest algorithm among the nine algorithms under comparison. Thus, we can conclude that both the causal feature selection methods and non-causal feature selection algorithms cannot deal with class-imbalanced datasets well.

From Figures 18 and 19, when the number of selected features by mRMR, CMIM and JMI are varied, we can see that, either with KNN or NBC, given a class-imbalanced dataset, both non-causal feature selection and causal feature selection are not able to deal with the dataset well.

# 8. Conclusion 

In this paper, we have proposed a unified view to fill in the gap in the research of the relation between causal and non-causal feature selection methods. With this view, we have analyzed the mechanisms of both types of feature selection methods and have shown that both major approaches to feature selection use different strategies to discover the MB of a class attribute under different Bayesian network structural assumptions. In theory, the feature sets obtained by causal feature selection methods are closer to the MB of the class attribute than non-causal feature selection methods, while non-causal methods are more computationally efficient and need fewer data samples than causal methods. With this view, we have provided causal interpretations to the output of non-causal feature selection methods and analyzed the error bounds of causal and non-causal methods. In addition, we have conducted extensive experiments to validate our findings in the paper.

Table 31: Prediction accuracy using KNN


From the theoretical and experimental analysis in the paper, we can find that both types of feature selection still face many changes as listed below and we hope this paper can stimulate the interest of researchers in machine learning to develop new methods to address these challenges.

- Small sample size. Causal feature selection cannot deal with a dataset with high dimensionality and small sample size. Then how can we leverage non-causal feature selection to help causal feature selection to improve the computational performance and accuracy of causal feature selection methods for large dimensional problems and small sample sizes?
- Imbalanced classes. The majority of existing causal and non-causal feature selection methods cannot deal with datasets with imbalanced classes, which exist in many real-world applications. It is important to develop new feature selection methods to address this problem.
- Large-sized MBs. A large MB makes causal feature selection methods suffer from the data-inefficient or time-inefficient problem, Thus, it is essential for big data analysts to develop efficient causal feature selection methods for dealing with large MB containing hundreds of features.
- Selection of proper parameter values. It is a hard problem for non-causal feature selection to determine a suitable value of $\psi$. How do both types of feature selection methods benefit each other to solve the problem?
- Efficiency. Most local-to-global Bayesian network learning methods employ causal feature selection methods to learn MBs for constructing a causal structure skeleton. Can we leverage non-casual feature selection methods to improve the computational performance of local-to-global learning methods with theoretical guarantees?

