# Bridging Causal Relevance and Pattern Discriminability: Mining Emerging Patterns from High-Dimensional Data 

Kui Yu ${ }^{1}$, Wei Ding ${ }^{2}$, Hao Wang ${ }^{1}$, and Xindong Wu ${ }^{1,3}$


#### Abstract

It is a nontrivial task to build an accurate Emerging Pattern (EP) classifier from high-dimensional data because we inevitably face two challenges (1) how to efficiently extract a minimal set of strongly predictive EPs from an explosive number of candidate patterns, and (2) how to handle the highly sensitive choice of the minimal support threshold. In order to address these two challenges, we bridge causal relevance and EP discriminability (the predictive ability of emerging patterns) to facilitate EP mining and propose a new framework of mining EPs from high-dimensional data. In this framework, we study the relationships between causal relevance in a causal Bayesian network and EP discriminability in EP mining, and then reduce the pattern space of EP mining to direct causes and direct effects, or the Markov blanket of the class attribute in a causal Bayesian network. The proposed framework is instantiated by two EPs-based classifiers, CE-EP and MB-EP, where CE stands for direct Causes and direct Effects, and MB for Markov Blanket. Extensive experiments on a broad range of datasets validate the effectiveness of the CE-EP and MB-EP classifiers against other well-established methods, in terms of predictive accuracy, pattern numbers, running time, and sensitivity analysis.


Index Terms-Emerging Patterns, Causal Bayesian Networks, Causal Relevance, EP Discriminability

## 1 INTRODUCTION

Association rule mining seeks to find association patterns that meet predefined minimum support and confidence constraints from a given dataset [7, 23]. This problem is usually divided into two steps. The first is to find frequent itemsets whose supports exceed a predefined minimum support threshold; and the second is to generate association rules from those frequent itemsets with the constraint of minimal confidence [32-33]. Associative classification integrates association rule mining and classification [22, 35]. In associative classification, the consequent of an association rule is a class label, and the classifier is constructed using a set of association rules. This classifier is expected to produce accurate classifications and yield an interpretable model [3, 16]. Liu et al. [22] introduced CBA (Classification Based on Associations), the first associative classifier.

An illustrating example of association rules for classification is given in Table 1 using the Balloon dataset from the UCI machine learning repository [4], with the class attribute, inflated (T (true), F

[^0]
[^0]:    *A shorter, preliminary version of this paper with the title "Causal Associative Classification" was published in the Proceedings of the 11th IEEE International Conference on Data Mining (ICDM'11), pp. 914-923. Compared with the conference version of this paper, this journal version has been completely re-written with the following new materials: Tables 1 and 2 in Section 1; Section 2.2; Section 3.1; a new theoretical analysis of causal relevance in causal Bayesian networks and EP discriminability in EP mining in Section 4; the number of selected datasets has been increased from 20 to 36 in Section 5; new Sections 5.3 and 5.5 to have a detailed analysis on comparisons of the numbers of selected patterns and on sensitivity analysis on both predictive accuracy and numbers of selected patterns under seven minimum support thresholds, respectively; and new Sections 5.2.2, 5.6 and 5.7.
    ${ }^{1}$ Department of Computer Science, Hefei University of Technology, Hefei, 230009, China. E-mail: ykui713@ gmail.com, jsiwangh@hfut.edu.cn.
    ${ }^{2}$ Department of Computer Science, University of Massachusetts Boston, Boston, 02125, USA. E-mail: ding@cs.umb.edu.
    ${ }^{3}$ Department of Computer Science, University of Vermont, Burlington, 05405, USA. E-mail: xwu@cs.uvm.edu. ( $\infty$ corresponding author)

(false)), and 4 features: color (yellow, purple), size (large, small), act (stretch, dip) and age (adult, child). The dataset consists of 20 samples as listed in Table 3 of Section 3.1.

If we set the minimum support threshold to 0.2 and the minimum confidence threshold to 0.8 , the top five association rules mined from this dataset for classification are shown in Table 1.

TABLE 1 EXAMPLES OF CLASSIFICATION ASSOCIATION RULES


Later, Dong and Li proposed a new type of association patterns named Emerging Patterns (EPs for short) whose support values change significantly from one class to another [9]. Different from association rule mining, a data set is divided into several subsets by their class labels in EP mining. The ratio of the support of an itemset in one class and that of this itemset in a contrasting class is measured using the growth rate. Those patterns whose growth rates satisfy a predefined minimum threshold are called EPs. Hence, EPs represent strong contrasts between different classes of data. For example, to mine EPs from the Balloon dataset, this dataset is divided into two classes: inflated $=\mathrm{T}$ and inflated $=\mathrm{F}$ before mining, then the EPs of each class are mined from the corresponding class data, respectively, as shown in Table 2, under the minimum support threshold of 0.2 and a growth rate greater than 1.

TABLE 2 EXAMPLES OF EPS MINED FROM BALLOON DATASET


From the example above, we can see that EPs give more concise and understandable patterns than association rules. Moreover, the presence of EPs gives evidence about which class the object should belong to. Thus, the discovery process of EPs prefers classification. Dong et al. proposed the first EPsbased classifier, called CAEP (Classification by Aggregating Emerging Patterns)[10]. EPs-based classification has shown to be a powerful method for constructing accurate classifiers, even for imbalanced data [10-11, 13]. This paper focuses on mining EPs for classification.

Most associative classifiers are constructed in two steps: generating frequent patterns satisfying minimum support and confidence constraints, and then making predictions based on the selected patterns. Although many pruning strategies have been proposed, an explosive number of rules can still be discovered from high dimensional and dense data even using a rather high minimum support threshold. The large number of candidate rules makes it difficult to store, retrieve, prune, and sort them efficiently for classification. Furthermore, they hamper the understanding of the final classifiers, and even

lead to overfitting. Hence how to select a suitable minimum support threshold is not only a challenging problem, but also the key to control the performance of associative classifiers. A small support threshold could generate a large number of rules while a large value might prune many predictive rules and cause serious accuracy degradation.

As a special type of association mining, mining EPs from high-dimensional data also encounters the above challenging problem, especially with the advent of the emerging datasets with tens of thousands of features in many real-world applications, such as image processing, gene expression data, text data, etc. Thus, to effectively mine EPs from high-dimensional data, two challenging research issues need to be further explored:
(1) How to efficiently mine a minimal set of strongly predictive EPs from high-dimensional data; and
(2) How to deal with the highly sensitive choice of the minimal support threshold.

To battle these challenges, we propose a new framework for mining EPs from high-dimensional data by bridging causal relevance in causal Bayesian networks and EP discriminability (the predictive ability of EPs) in EP mining. More specifically, the causal relevance of a target node in causal Bayesian networks with respect to other nodes is divided into three categories, irrelevant nodes, Markov blanket (direct causes, direct effects and direct causes of the direct effects of the target node), and redundant nodes while the pattern space in EP mining with respect to EP discriminability is classified as non-EPs, strongly predictive EPs, and redundant EPs. Through studying the relationships between causal relevance in a causal Bayesian network and EP discriminability in EP mining, we bridge causal relevance and EP discriminability to reduce the pattern space in EP mining to the direct Causes and direct Effects (CE), or the Markov Blanket (MB) of the class attribute in causal Bayesian networks to facilitate EP mining in an innovative framework and mine EPs from high-dimensional data.

The main contributions of this paper are as follows:
(1) The paper gives a theoretical analysis of the relationships between causal relevance in causal Bayesian networks and EP discriminability in EP mining. With this theoretical framework, the pattern space in EP mining is reduced to the space of CE or MB of the class attribute in a causal Bayesian network instead of the combinations of all features, which greatly reduces computational cost and resource demand in the stage of EP mining.
(2) By bridging causal relevance with EP discriminability, mining EPs from the space of CE or MB of the class attribute in a causal Bayesian network, naturally endows EPs with strongly predictive ability, since the causal factors of a variable give a natural interpretation of the events occurring in real-world applications. Most importantly, in a causal Bayesian network, the CE or the MB of a target node is unique and minimal, and hence, our framework has a good chance to generate a minimum set of EPs.

(3) With the above innovative framework, two new EPs-based classifiers, CE-EP and MB-EP, are proposed. Extensive experiments on a broad range of datasets, including 24 UCI datasets and 12 very high-dimensional datasets, validate the effectiveness of the proposed approaches against other wellestablished methods, in terms of predictive accuracy, pattern numbers, and running time.
(4) The experiments of sensitivity analysis on seven minimum support thresholds demonstrate that the CE-EP and MB-EP classifiers not only can efficiently and effectively handle very high-dimensional data, but also are insensitive to the minimum support thresholds. Moreover, our experiments discover that the EPs-based classifiers are less sensitive to the minimum support threshold than the associative classifiers, and the choice of a suitable minimum support threshold is the key to control CBA and CMAR while it is not crucial to CAEP, especially to both CE-EP and MB-EP. Finally, our study of impact of the minimal growth-rate threshold illustrates that both CAEP and CE-EP classifiers are also less sensitive to the minimal growth-rate threshold.

The reminder of the paper is structured as follows. Section 2 reviews previous work. Section 3 provides the backgrounds on emerging patterns and causal Bayesian networks, and Section 4 bridges causal relevance with EP discriminability, and then presents a framework for mining EPs from highdimensional data. Experimental results are reported in Section 5, and we conclude in Section 6.

# 2 PREVIOUS WORK 

### 2.1 EPs-based Classifiers

Associative classification integrates association rule discovery and classification into a prediction model. Successful algorithms of associative classifiers include CBA [22], CMAR [19] and CPAR [36]. CBA (Classification Based on Association) uses an Apriori-like algorithm to generate a single rule-set and ranks the rules according to their confidence/support values. Then CBA adopts "one matching pattern determines the class of an instance" approach to select the best rule to be applied to each test instance. Based on CBA, Li et al. introduced CMAR (Classification based on Multiple-class Association Rule) that generates classification association rules through a FP-tree and uses multiple rules to perform the classification, while CPAR (Classification based on Predictive Association Rule) combines the advantages of both associative classification and traditional rule-based classification. Instead of generating a large number of candidate rules as in associative classification, CPAR adopts a greedy algorithm to generate rules directly from the training data.

Dong and Li introduced Emerging Patterns (EPs) to represent strong contrasts between different classes of data [9]. An emerging pattern is a multivariate pattern whose support value increases sharply from a background dataset to a target dataset. Compared to association rules, EPs capture emerging trends in time-stamped datasets, or useful contrasts between data classes [9, 28]. In addition, Jumping

Emerging Patterns (JEPs, as defined in Section 3.1) is a special type of EPs whose supports increase from zero in a background dataset to non-zero in a target dataset [17]. Like other patterns or rules composed of conjunctive combinations of attributes and values, EPs can be easily understood and used directly in a wide range of applications, such as predicting diseases [20], failure detection [24], and discovering knowledge in gene expression data [5, 12, 21].

EPs represent strong contrasts between different classes of data, and the presence of EPs in a query object gives some evidence about which class the object should belong to. Therefore, EPs have shown very successful results on constructing accurate and robust classifiers. In comparison with associative classifiers based on association rules, EPs-based classifiers use the aggregation of the discriminating power of the set of matching EPs to classify an instance. Dong et al. proposed the first EPs-based classifier, called CAEP (Classification by Aggregating Emerging Patterns)[10]. In fact, both CMAR and CPAR have adopted the idea of CAEP by using multiple rules instead of one rule to classify an instance. CAEP first discovers all the EPs from the training data for each class. When a new test instance is classified by aggregating the differentiating power of a set of EPs that apply, a score is computed for each class, and this test instance is classified to the class with the highest score. Based on CAEP, Li et al. proposed a JEP-classifier which is distinct from the CAEP classifier [17]. The JEP-classifier uses JEPs exclusively because JEPs discriminate between different classes more strongly than any other type of EPs. Since discovery of all EPs from the training data is time consuming, Li et al. [18] presented a lazy EPs-based classifier, called DeEPs, to improve the efficiency and accuracy of CAEP and JEP-classifier. Whenever a new test instance is considered, DeEPs uses it as a filter to remove irrelevant feature values in order to reduce the search space. Since an EP mining process of DeEPs is instance-based, all the training data has to be stored for re-learning during the entire classification process. Fan and Ramamohanarao proposed a robust EP-classifier named SJEP-classifier, exclusively using a strong JEP [11]. A strong JEP from the class $\mathrm{C}_{1}$ to the class $\mathrm{C}_{2}$ satisfies two conditions: (1)the support of itemset X is zero in $\mathrm{C}_{1}$ but non-zero in $\mathrm{C}_{2}$ and satisfies a minimal support threshold in $\mathrm{C}_{2}$, and (2) any proper subset of $X$ does not satisfy condition (1). The SJEP-classifier integrates the CP-tree data structure into the EP classifier, which uses far fewer JEPs than a JEP-classifier yet gets higher predictive accuracy than existing EPs-based classifiers.

Due to the limitation of the existing EP mining techniques, existing EP-based classifiers could not effectively handle datasets with more than sixty dimensions without prior feature set reduction using desktop computers of 2006 [25]. It is still a challenging research issue to build an accurate EPs-based classifier from a high-dimensional dataset. In this study, we bridge causal relevance in causal Bayesian networks and EP discriminability in EP mining to help construct accurate EPs-based classifiers from high-dimensional data.

# 2.2 Learning Causal Bayesian Networks from Data 

A causal Bayesian network is a Bayesian network in which each directed edge is described as a direct causal influence imposed on a child node by its parent nodes. Since structure learning of causal Bayesian networks in observational data is essentially the same as structure learning of Bayesian networks, learning Bayesian networks is one of the most common methods to explore causal relationships in the observed data [29, 31]. Structure learning methods of Bayesian networks include global and local learning approaches. A global learning approach attempts to uncover a complete Bayesian network over all model features, but it can only deal with no more than 300 features [6, 8].

A local learning approach without learning a complete Bayesian network has been considered as an effective means to handle hundreds of thousands of features [2,34]. The local learning focuses on two specific tasks: (a) identification of features that are direct causes and direct effects of the target of interest, and (b) discovery of the Markov blanket of the target of interest. For the first task, two major algorithms HITON_PC and MMPC were introduced by Aliferis et al. [2]. For the second task, the discovery of the Markov blanket of a target is to find the set of parents, children, and parents of the children for the target of interest in a faithful Bayesian network. Margaritis and Thrun first invented a sound algorithm, GS for discovery of the Markov blanket of a target [27]. Based on the GS algorithm, an IAMB algorithm was presented which guarantees to find the actual Markov blanket given enough training data and is more efficient than GS [1]. However, it still requires a sample size exponential in the size of the Markov blanket. Based on the IAMB algorithm, HITON_MB derived from HITON_PC, MMMB developed from MMPC, and PCMB have been introduced without requiring a sample set exponential to the size of the Markov blanket $[2,30]$.

## 3 DEFINITIONS AND NOTATIONS

### 3.1 Emerging Patterns

Assume we have a dataset D defined upon a set of N features $\left(\mathrm{F}_{1}, \mathrm{~F}_{2}, \ldots, \mathrm{~F}_{\mathrm{N}}\right)$ and the class attribute C . For every feature $\mathrm{F}_{\mathrm{i}}, \mathrm{i}=1, \ldots, \mathrm{~N}$, we assume it is in a discrete domain that we denote as $\operatorname{dom}\left(\mathrm{F}_{\mathrm{i}}\right)$. Let I be the set of all items, $\mathrm{I}=\mathrm{U}_{\mathrm{i}=1}^{\mathrm{N}} \operatorname{dom}\left(\mathrm{F}_{\mathrm{i}}\right)$. An itemset X is a subset of I and its support in D , denoted support ${ }_{D}(X)$, is defined as follows.

Definition 1. (Support) support $\left({ }_{D}(X)=\frac{\text { count }_{D}(X)}{|D|}\right.$
where count ${ }_{D}(X)$ is the number of instances in $D$ containing $X$ and $|D|$ is the number of instances in $D$.
Let $C=\left\{C_{1}, C_{2}, \ldots, C_{K}\right\}$ be a finite set of $K$ distinct class labels. The dataset $D$ can be partitioned into $D_{1}, D_{2}, \ldots, D_{K}$, where $D_{j}$ consists of instances with class label $C_{j}, j=1, \ldots, K$. The growth rate of $X$ from $D_{s}$ to $D_{m}(s, m=1, \ldots, K$ and $s \neq m)$ is defined as follows.

Definition 2. (GR: Growth Rate)[9] $\mathrm{GR}_{\mathrm{D}_{\mathrm{s}} \rightarrow \mathrm{D}_{\mathrm{m}}}(\mathrm{X})=\frac{\text { support }_{\mathrm{D}_{\mathrm{m}}}(\mathrm{X})}{\text { support }_{\mathrm{D}_{\mathrm{s}}}(\mathrm{X})}$. (1) If support ${ }_{\mathrm{D}_{\mathrm{m}}}(\mathrm{X})=0$ and support ${ }_{D_{s}}(X)=0$, then $G R_{D_{s} \rightarrow D_{m}}(X)=0$; and (2) if support ${ }_{D_{m}}(X) \neq 0$ but support ${ }_{D_{s}}(X)=0$, then $\mathrm{GR}_{\mathrm{D}_{\mathrm{s}} \rightarrow \mathrm{D}_{\mathrm{m}}}(\mathrm{X})=\infty$.
Definition 3. (EP: Emerging Pattern)[9] Given a threshold $\rho>1$, an EP from $\mathrm{D}_{\mathrm{s}}$ to $\mathrm{D}_{\mathrm{m}}$ is an itemset X where $\mathrm{GR}_{\mathrm{D}_{\mathrm{s}} \rightarrow \mathrm{D}_{\mathrm{m}}}(\mathrm{X}) \geq \rho$.
Definition 4. (JEP: Jumping Emerging Pattern) If $\mathrm{GR}_{\mathrm{D}_{\mathrm{s}} \rightarrow \mathrm{D}_{\mathrm{m}}}(\mathrm{X})=\infty$, the itemset X is called a Jumping EPfrom $\mathrm{D}_{\mathrm{s}}$ to $\mathrm{D}_{\mathrm{m}}$.

An EP e from $\mathrm{D}_{\mathrm{s}}$ to $\mathrm{D}_{\mathrm{m}}$ is called an EP e of $\mathrm{D}_{\mathrm{m}}$. The goal of EP mining is to extract the EP set $\mathrm{E}_{\mathrm{j}}$ for each class $C_{i}$ which consists of EPs from $D-D_{C_{i}}$ to $D_{C_{i}}$, given a pre-defined growth rate threshold $\rho$ and a minimum support threshold.
Definition 5. (Growth Rate Improvement)[37] Given an EP e, the growth rate improvement of e, Rateimp(e), is defined as the minimum difference between its growth rate and the growth rates of all of its subsets,

$$
\operatorname{Rateimp}(\mathrm{e})=\min \left(\forall \mathrm{e}^{\prime} \subset \mathrm{e}, \mathrm{GR}(\mathrm{e})-\mathrm{GR}\left(\mathrm{e}^{\prime}\right)\right)
$$

Definition 5 illustrates that a positive growth rate improvement threshold, Rateimp(e) $>0$, ensures a concise and representative set of EPs that are not subsumed by each other and consist of EPs with strong predictive power. Thus, the growth rate improvement can help to eliminate EPs that are uninteresting or redundant. Table 3 shows the Balloon dataset with the class attribute, inflated (T (true), F (false)), 4 features: color (yellow, purple), size (large, small), act (stretch, dip) and age (adult, child), 20 samples from the UCI machine learning repository [4], and act-r which is an artificial feature added by us that is redundant to act.

TABLE 3 THE BALLOON DATASET WITH AN INCLUSION OF REDUNDANT FEATURE act-r


An illustrating example is given in Tables 4 and 5 using the Balloon dataset. The minimum support threshold is 0.2 and the growth rate threshold is $\rho>1$. The candidate EPs are of two classes T (when the inflated is true) and F (when the inflated is false) with 20 samples and 4 features: color, size, act and age.

TABLE 4 THE CANDIDATE EPs FROM CLASS F TO CLASS T


TABLE 5 THE CANDIDATE EPs FROM CLASS T TO CLASS F


From Definition 3, in Table 4, both \{act=stretch\} and \{age=adult\} are EPs of class T. In Table 5, by Definition 5, we can see that $\{$ act=dip, age=child $\}$ is an EP of class F due to Rateimp $(\operatorname{act}=\operatorname{dip}, \operatorname{age}=$ child) $>0$.

When applying EPs to classification, the EP set of each class is used to decide to which class a test instance $t$ should belong. More specifically, we derive $k$ scores for $t$, one score per class, by feeding the EPs of each class into a scoring function, that is, label $(t)=\operatorname{argmax}_{C_{i} \in C} \operatorname{score}\left(t, C_{i}\right)$. The following definition provides the scoring function of the EPs-based classifier [10].

Definition 6 (Aggregate Score). Given an instance $t$ and a set $E_{i}$ of EPs of class $C_{i} \in \operatorname{dom}(C)$ mined from the training data, the aggregate score of $t$ for $C_{i}$ is defined as

$$
\operatorname{score}\left(t, C_{i}\right)=\sum_{e \in t, e \in E_{i}} \frac{G R_{D-D_{C_{i}}-D_{C_{i}}}(e)}{G R_{D-D_{C_{i}}-D_{C_{i}}}(e)+1} * \operatorname{support}_{C_{i}}(e)
$$

A potential problem in Definition 6 is that the number of EPs from different classes is likely unbalanced. If a class $C_{i}$ contains more EPs than another class $C_{j}$, a test instance tends to obtain higher scores for $C_{i}$ than for $C_{j}$, even if the test instance actually belongs to $C_{j}$. Thus, the score computed by Definition 6 cannot be directly used to classify a test instance. Dong et al. [11] presented a concept of a base score for class $C_{i}$, baseScore $\left(C_{i}\right)$, which was first calculated from the training instances of the class. With the base score, the new score of an instance $t$ for $C_{i}$, named normScore $\left(t, C_{i}\right)$, is defined as the ratio of the score, score $\left(\mathrm{t}, \mathrm{C}_{\mathrm{i}}\right)$, calculated by Definition 6 and the base score, baseScore $\left(\mathrm{C}_{\mathrm{i}}\right)$,

$$
\operatorname{normScore}\left(\mathrm{t}, \mathrm{C}_{\mathrm{i}}\right)=\frac{\operatorname{score}\left(\mathrm{t}, \mathrm{C}_{\mathrm{i}}\right)}{\text { baseScore }\left(\mathrm{C}_{\mathrm{i}}\right)}
$$

The class with the highest normScore wins and ties are broken by putting the test instance into the class with the largest population. One way to determine the base scores is that baseScore $\left(C_{i}\right)$ can be the median of the scores of the training instances of class $C_{i}$ [11]. For example, assume there are 5 training instances from each of the positive ( + ) and negative (-) classes; with all EPs of each class, assume the scores of the positive training instances computed by Definition 6 are 17.85, 18.61, 18.76, 19.75, 20.24, and the scores of the negatives are $7.8,7.87,8.20,8.57,8.61$. The (median) base scores for the positive and negative classes are 18.76 and 8.20 , respectively. Given a test instance $t$ (known to be from the

negative class) with scores 10.17 and 7.92 for the positive and negative classes respectively, we have normScore $(t,+)=10.17 / 18.76=0.54$ and normScore $(t,-)=7.92 / 8.2=0.97$. The instance $s$ is thus labeled as the negative class.

Later, Zhang et al. introduced a simpler score function based on information theory to avoid computing the base score for each class [38] and defined the score function of a test instance $t$ by Eq.(5).

$$
L\left(t \mid C_{i}\right)=-\sum_{k=1}^{p} \log _{2} P\left(X_{k} \mid C_{i}\right), X_{k} \in E_{i} \text { and } X_{k} \in t
$$

The test instance $t$ is assigned the class label $C_{i}$ when $L\left(t \mid C_{i}\right)$ is the minimum. Given an itemset $X$, $P\left(X \mid C_{i}\right)$ is approximately computed by Eq. (6).

$$
P\left(X \mid C_{i}\right)=\left(\left|X \cap C_{i}\right|+2 *\left(\frac{|X|}{|D|}\right)\right) /\left(\left|C_{i}\right|+2\right)
$$

where $\left|X \cap C_{i}\right|$ is the number of training instances belonging to class $C_{i}$ and containing $X,|X|$ is the total number of training instances containing $X,|D|$ is the total number of training instances, and $\left|C_{i}\right|$ is the number of training instances of class $C_{i}$. In addition, to ensure that we can always find a partition for an instance, all single-item itemsets of each class whether they satisfy the given thresholds or not are taken into account when Eq. (5) is used to classify a test instance.

# 3.2 Causal Bayesian Networks 

Discovery of causal relationships between events has found wide applications in science and technology. Since late 1980's, the work on formal theories of causality and causal induction by Spirtes, Pearl and others has been gaining ground [29, 31]. Since causal Bayesian networks provide a convenient framework for reasoning among random variables, to simplify our presentation, we focus on causal Bayesian networks to represent causal relationships between variables in this paper. Since a causal Bayesian network is a Bayesian network and its structural learning in observational data is essentially the same as structure learning of Bayesian networks, one of the most exciting prospects in the last two decades has been the possibility of using Bayesian networks to discover causal relationships among features in observed data [29, 31]. The words "node" and "feature" are used interchangeably in the rest of this paper.

Definition 7 (Bayesian Networks) Let P be a discrete joint probability distribution of a set of random nodes F via a directed acyclic graph G. We call the triplet $\langle F, G, P\rangle$ a (discrete) Bayesian network if $\langle F, G, P\rangle$ satisfies the Markov condition: every node is independent of any subset of its non-descendant nodes conditioned on its parents.

With the Markov condition, a Bayesian network encodes the joint probability P over a set of nodes $F=\left\{F_{1}, F_{2}, \ldots, F_{n}\right\}$ and decomposes the joint probability into a product of the conditional probability distributions over each node given its parents in G. Assuming $\mathrm{Pa}\left(\mathrm{F}_{\mathrm{i}}\right)$ is the set of parents of $\mathrm{F}_{\mathrm{i}}$ in G , the joint probability P is written as Eq. 7.

$$
P\left(F_{1}, F_{2}, \ldots, F_{n}\right)=\prod_{i=1}^{n} P\left(F_{i} \mid P a\left(F_{i}\right)\right)
$$

A simple Bayesian network is shown in Fig. 1 [14]. The number of possible values each node can take and the probabilities that are associated with this structure are not shown for better clarity.

Definition 8 (Faithfulness) A Bayesian network satisfies the faithfulness condition if and only if every conditional independence entailed by the directed acyclic graph $G$ is also present in the joint probability $P$.
![img-0.jpeg](img-0.jpeg)

Fig. 1. A simple example of a Bayesian network of Lung Cancer
Definition 9 (Causal Bayesian Networks) A causal Bayesian network is a Bayesian network $<F, G, P>$ with the additional semantics that for all $F_{i} \in F$ and $F_{j} \in F, i \neq j$, if a node $F_{i}$ is a parent of node $F_{j}$ in $G$, then $F_{i}$ is a direct cause for $F_{j}$.

Definition 10 (Causal Markov Condition) In a causal Bayesian network, if every node is independent of its non-effects (i.e., non-descendants) given its direct causes (i.e., parents), then the causal Markov condition holds.

The causal Markov condition permits the joint distribution of the features in a causal Bayesian network to be factored as in Eq. 7.

Definition 11 (Causal Faithfulness) A causal Bayesian network satisfies the faithfulness condition if it satisfies the faithfulness condition of Definition 8.

# 4 A FRAMEWORK OF MinING EPs FROM HIGH-DIMENSIONAL DATA 

### 4.1 Causal Relevance and EP Discriminability

It is infeasible to examine a search space covering all possible item combinations for high-dimensional and dense data. A potentially effective way to mine EPs from high-dimensional data is to avoid the combinations of all items. From Tables 4 to 5, we can see that the final set of EPs does not contain features size and color, since their corresponding EPs have no impact on the construction of accurate classifiers. Motivated by this observation, in this section, we bridge causal relevance in causal Bayesian networks and EP discriminability (the predictive ability of an EP) in EP mining to address the two challenges on the minimal strongly predictive EP set and the impact of the minimal support threshold.
With the causal Markov condition, we define the causal relevance of a target node in causal Bayesian networks with respect to other nodes in three categories, irrelevant nodes, Markov blanket, and redundant nodes as follows.

Definition 12 (Irrelevant Nodes) In a causal Bayesian network, if $F_{1}$ has no paths to connect with the target node $C$, node $F_{1}$ is an irrelevant node with respect to $C$, that is,

$$
\forall \mathrm{f} \in \operatorname{dom}\left(\mathrm{F}_{1}\right), \forall \mathrm{c} \in \operatorname{dom}(\mathrm{C}), \mathrm{P}\left(\mathrm{C}=\mathrm{c} \mid \mathrm{F}_{1}=\mathrm{f}\right)=\mathrm{P}(\mathrm{C}=\mathrm{c})
$$

In causal Bayesian networks, if a node $F_{1}$ has no path to a target node $C$, it doesn't carry any predictive information about $C$ at all, no matter what the context is. For example, let the node "Lung Cancer" be a target node in Fig. 1., node "Born an Even Day" in Fig. 1 is disconnected from "Lung Cancer", thus the pattern: \{"Born an Even Day"=yes\} or \{"Born an Even Day"=no\} cannot provide any predictive information to the target node of Lung Cancer.
Definition 13 (MB: Markov Blanket)[29] In a causal Bayesian network, the Markov blanket of a node $\mathrm{F}_{1}$, denoted as $\mathrm{MB}\left(\mathrm{F}_{1}\right)$, is the set of its direct causes, its direct effects and the direct causes of its direct effects (spouses).

For example, in Fig.1, the Markov blanket of node "Lung Cancer" includes direct causes: "Smoking" and "Genetics", direct effects: "Coughing" and "Fatigue", and direct cause of the direct effects (spouse): "Allergy".
Property 1[29] In causal Bayesian networks with causal faithfulness, the $\mathrm{MB}\left(\mathrm{F}_{1}\right)$ is unique and satisfies the following property:

$$
\forall S \in F-\left(M B\left(F_{1}\right) U\left\{F_{1}\right\}\right), P\left(F_{1} \mid M B\left(F_{1}\right), S\right)=P\left(F_{1} \mid M B\left(F_{1}\right)\right)
$$

This property says that the Markov blanket of a node $F_{1}$ is not only unique but also stores information about $F_{1}$ that cannot be obtained from any other nodes in causal Bayesian networks. For example, in Fig.1, if we know the information of the Markov blanket of "LungCancer", it shields "LungCancer" from other nodes. Thus, if we know the Markov blanket of "LungCancer", any nodes outside of it would be redundant. The redundant nodes in causal Bayesian networks are defined as follows.
Definition 14 (Redundant Nodes) In a causal Bayesian network, if a node $F_{1}$ has a path to connect with the target node $C$ but doesn't belong to $M B(C)$, then it is a redundant node with respect to $C$.

In a causal Bayesian network, if a node is redundant with respect to a target node $C$, the values of this node are fully determined by the $\mathrm{MB}(\mathrm{C})$. For example, with the causal Bayesian network in Fig.1, according to the causal Markov condition (see Definition 10), once all the direct causes of node "LungCancer" have been given, the values of its indirect causes are fully determined by their corresponding direct causes of node "LungCancer". Thus, the indirect causes of "Lung Cancer" don't bring any additional information to "Lung Cancer". For instance, increased "Anxiety" will increase "Smoking," but this cannot influence directly "LungCancer," when the value of "Smoking" is known in advance. Consequently, with two patterns for predicting whether a person suffers from lung cancer, \{"Smoking"=yes\} $\rightarrow\{$ "Lung Cancer" $=$ yes $\}$ and $\{$ "Anxiety" $=$ yes and "Smoking" $=$ yes $\} \rightarrow\{$ "Lung cancer" $=$ yes $\}$, from Fig. 1, it suffices to have \{"Smoking"=yes\} $\rightarrow\{$ "Lung Cancer" $=$ yes $\}$ as a predictive pattern, and we do not need

to know about "Anxiety." With the Markov blanket of a target node, other nodes in a causal Bayesian network become irrelevant or redundant nodes with respect to the target node.

In Fig. 2a, this Bayesian network is learned from the Balloon dataset in Table 3 without considering the artificial feature act_r (using the MMHC algorithm with the parameter alpha $=0.01$ [34]). We can see that both color and size are irrelevant to the class attribute inflated (in red color) while features act and age are both direct causes of the class attribute. In fact, in Tables 4 and 5, the EPs of both classes don't include features color and size. In Figure 2b, the Bayesian network is learned from the Balloon dataset with the artificial feature act_r that is redundant to act, as shown in Table 3. We can see that feature act_r is also a redundant node with respect to the class attribute inflated.
![img-1.jpeg](img-1.jpeg)

Fig. 2 (a) The Bayesian network learned from the Balloon dataset; (b) the Bayesian network learned from the Balloon dataset with the artificial feature act-r.

The above observations further motivate us to explore the potential relationships between causal relevance in a causal Bayesian network and EP discriminability in EP mining, as shown in Fig. 3, to handle EP mining from high-dimensional data. We give the following propositions to address these relationships.
![img-2.jpeg](img-2.jpeg)

Fig.3.Causal relevance and EP discriminability
Proposition 1. If $F_{i}$ is an irrelevant node with respect to the target node $C$ in a causal Bayesian network, then $\forall \mathrm{f} \in \operatorname{dom}\left(\mathrm{F}_{\mathrm{i}}\right)$, the pattern $\left\{\mathrm{F}_{\mathrm{i}}=\mathrm{f}\right\}$ is a non-EP.
Proof. Assume a dataset D has two classes $\mathrm{C}=\left\{\mathrm{C}_{\mathrm{p}}, \mathrm{C}_{\mathrm{n}}\right\}, \mathrm{D}_{\mathrm{p}}$ represents $\mathrm{C}_{\mathrm{p}}$ class data, $\mathrm{D}_{\mathrm{n}}$ represents $C_{n}$ class data, $\sup _{D_{p}}\left(F_{i}=f\right)$ is the support value of the itemset $\left\{F_{i}=f\right\}$ in $D_{p}$ and $\sup _{D_{n}}\left(F_{i}=f\right)$ is its support value in $D_{n}$. Then $\operatorname{GR}\left(F_{i}=f\right)$ from $D_{n}$ to $D_{p}$ is calculated as follows.

$$
\begin{aligned}
G R_{D_{n} \rightarrow D_{p}}\left(F_{i}=f\right) & =\sup _{D_{p}}\left(F_{i}=f\right) / \sup _{D_{n}}\left(F_{i}=f\right) \\
& =\mathrm{P}\left(F_{i}=f \mid \mathrm{C}=\mathrm{C}_{\mathrm{p}}\right) / \mathrm{P}\left(F_{i}=f \mid \mathrm{C}=\mathrm{C}_{\mathrm{n}}\right) \\
& =\frac{\mathrm{P}\left(F_{i}=f, \mathrm{C}=\mathrm{C}_{\mathrm{p}}\right)}{\mathrm{P}\left(\mathrm{C}=\mathrm{C}_{\mathrm{p}}\right)} / \frac{\mathrm{P}\left(F_{i}=f, \mathrm{C}=\mathrm{C}_{\mathrm{n}}\right)}{\mathrm{P}\left(\mathrm{C}=\mathrm{C}_{\mathrm{n}}\right)} \\
& =\frac{\mathrm{P}\left(\mathrm{C}=\mathrm{C}_{\mathrm{p}} \mid F_{i}=f\right) \mathrm{P}\left(F_{i}=f\right)}{\mathrm{P}\left(\mathrm{C}=\mathrm{C}_{\mathrm{p}}\right)} / \frac{\mathrm{P}\left(\mathrm{C}=\mathrm{C}_{\mathrm{n}} \mid F_{i}=f\right) \mathrm{P}\left(F_{i}=f\right)}{\mathrm{P}\left(\mathrm{C}=\mathrm{C}_{\mathrm{n}}\right)} \\
& =\frac{\mathrm{P}\left(\mathrm{C}=\mathrm{C}_{\mathrm{n}}\right)}{\mathrm{P}\left(\mathrm{C}=\mathrm{C}_{\mathrm{p}}\right)} \frac{\mathrm{P}\left(\mathrm{C}=\mathrm{C}_{\mathrm{p}} \mid F_{i}=f\right)}{\mathrm{P}\left(\mathrm{C}=\mathrm{C}_{\mathrm{n}} \mid F_{i}=f\right)}
\end{aligned}
$$

Since $F_{i}$ is an irrelevant node with respect to the target node $C$ in the causal Bayesian network, by Eq.(8), we get the following equation.

$$
\begin{aligned}
G R_{D_{n} \rightarrow D_{p}}\left(F_{i}\right. & \left.=f\right)=\frac{1-\mathrm{P}\left(\mathrm{C}=\mathrm{C}_{p}\right)}{\mathrm{P}\left(\mathrm{C}=\mathrm{C}_{p}\right)} \cdot \frac{\mathrm{P}\left(\mathrm{C}=\mathrm{C}_{\mathrm{p}} \mid F_{i}=f\right)}{1-\mathrm{P}\left(\mathrm{C}=\mathrm{C}_{\mathrm{p}} \mid F_{i}=f\right)} \\
& =1
\end{aligned}
$$

According to Definition 3 in Section 2.1, Proposition 1 is proven.
From Definition 5 in Section 2.1, for an EP e, if we can find an $\mathrm{e}^{\prime} \subset \mathrm{e}$ to make Rateimp(e) $\leq 0$, then e might be an uninteresting or redundant EP given its subset $\mathrm{e}^{\prime}$, and the EP e might be replaced by its subset $e^{\prime}$. Thus, avoiding generation of these redundant EPs in advance will improve search efficiency. We give Proposition 2 below to explain the relationships between redundant nodes in causal Bayesian networks and EP redundancy in EP mining.
Proposition 2. If a node $F_{i}$ is a redundant node to the target node $C$ in a causal Bayesian network and $M$ is the Markov blanket of C , then $\forall \mathrm{f} \in \operatorname{dom}\left(\mathrm{F}_{\mathrm{i}}\right)$, and there exists $\mathrm{m} \in \bigcup_{i=1}^{|\mathrm{M}|} \operatorname{dom}\left(\mathrm{M}_{\mathrm{i}}\right)$, such that the candidate EP of $\left\{\mathrm{F}_{\mathrm{i}}=\mathrm{f}, \mathrm{M}=\mathrm{m}\right\}$ is a redundant EP with respect to the EP of $\{\mathrm{M}=\mathrm{m}\}$.
Proof. Since $F_{i}$ is a redundant node with respect to $C$, by Property 1 , the following equation holds:

$$
\forall \mathrm{c} \in \operatorname{dom}(\mathrm{C}), \mathrm{P}(\mathrm{C}=\mathrm{c} \mid \mathrm{M}=\mathrm{m}, \mathrm{~F}_{\mathrm{i}}=\mathrm{f})=\mathrm{P}(\mathrm{C}=\mathrm{c} \mid \mathrm{M}=\mathrm{m})
$$

$G R\left(\mathrm{~F}_{\mathrm{i}}=\mathrm{f}, \mathrm{S}=\mathrm{s}\right)$ from $\mathrm{D}_{\mathrm{n}}$ to $\mathrm{D}_{\mathrm{p}}$ is calculated as follows.

$$
\begin{aligned}
G R_{D_{n} \rightarrow D_{p}}\left(F_{i}=\mathrm{f}, M=m\right) & =\sup _{D_{p}}\left(F_{i}=f, M=m\right) / \sup _{D_{n}}\left(F_{i}=f, M=m\right) \\
& =P\left(F_{i}=\mathrm{f}, M=m \mid \mathrm{C}=\mathrm{C}_{p}\right) / P\left(F_{i}=\mathrm{f}, M=m \mid \mathrm{C}=\mathrm{C}_{n}\right) \\
& =\frac{P\left(\mathrm{C}=\mathrm{C}_{p} \mid F_{i}=\mathrm{f}, M=m\right)}{P\left(\mathrm{C}=\mathrm{C}_{p}\right)} / \frac{P\left(\mathrm{C}=\mathrm{C}_{n} \mid F_{i}=\mathrm{f}, M=m\right)}{P\left(\mathrm{C}=\mathrm{C}_{n}\right)} \\
& =\frac{P\left(\mathrm{C}=\mathrm{C}_{p} \mid F_{i}=\mathrm{f}, M=m\right)}{P\left(\mathrm{C}=\mathrm{C}_{n} \mid F_{i}=\mathrm{f}, M=m\right)} \cdot \frac{P\left(\mathrm{C}=\mathrm{C}_{n}\right)}{P\left(\mathrm{C}=\mathrm{C}_{p}\right)}
\end{aligned}
$$

Since $F_{i}$ is a redundant node to $C$ in the causal Bayesian network, according to Eq.(10), we get the following equation.

$$
\begin{aligned}
G R_{D_{n} \rightarrow D_{p}}\left(F_{i}=\mathrm{f}, M=m\right)= & \frac{1-P\left(\mathrm{C}=\mathrm{C}_{n} \mid F_{i}=\mathrm{f}, M=m\right)}{P\left(\mathrm{C}=\mathrm{C}_{n} \mid F_{i}=\mathrm{f}, M=m\right)} \cdot \frac{P\left(\mathrm{C}=\mathrm{C}_{n}\right)}{P\left(\mathrm{C}=\mathrm{C}_{p}\right)} \\
= & \frac{1-P\left(\mathrm{C}=\mathrm{C}_{n} \mid M=m\right)}{P\left(\mathrm{C}=\mathrm{C}_{n} \mid M=m\right)} \cdot \frac{P\left(\mathrm{C}=\mathrm{C}_{n}\right)}{P\left(\mathrm{C}=\mathrm{C}_{p}\right)} \\
= & \frac{P\left(\mathrm{C}=\mathrm{C}_{p} \mid M=m\right)}{P\left(\mathrm{C}=\mathrm{C}_{n} \mid M=m\right)} \cdot \frac{P\left(\mathrm{C}=\mathrm{C}_{n}\right)}{P\left(\mathrm{C}=\mathrm{C}_{p}\right)} \\
= & \frac{P\left(M=m \mid \mathrm{C}=\mathrm{C}_{p}\right)}{P\left(M=m \mid \mathrm{C}=\mathrm{C}_{n}\right)} \\
= & G R_{D_{n} \rightarrow D_{p}}(M=m)
\end{aligned}
$$

Thus, we get $G R_{D_{n \rightarrow D_{p}}}\left(\mathrm{~F}_{\mathrm{i}}=\mathrm{f}, \mathrm{M}=\mathrm{m}\right)-G R_{D_{n \rightarrow D_{p}}}(\mathrm{M}=\mathrm{m})=0$. According Definition 5 in Section 2.1, we have proven Proposition 2.
With the results of Propositions 1 and 2, we can remove irrelevant and redundant nodes with respect to the class attribute in causal Bayesian networks to achieve the goal of pruning non-EPs and redundant EPs before EP mining. Thus, by removing irrelevant and redundant nodes in causal Bayesian networks, we can reduce the pattern space in EP mining to the space of the Markov blanket of the class attribute in a causal Bayesian network, and we get Proposition 3 as follows.

Proposition 3. The pattern space in EP mining for classification can be reduced to the space of the Markov blanket of the class attribute in causal Bayesian networks.

With Proposition 3, within the Markov blanket of the class attribute, both the direct causes and the direct effects have a direct connecting path to the class attribute while the direct causes of the direct effects (spouses) of the class attribute don't. Thus, in causal Bayesian networks, the spouses of the class attribute cannot individually predict the class attribute and may enhance the predictive power of the direct effects only when they join with the direct effects. With the causal Markov condition, direct causes joined with the direct effects give the highest predictive ability to predict the class attribute and a natural interpretation for what happens to the class attribute. For example, as indicated in Fig.1, the nodes "Smoking", "Genetics", "Coughing", and "Fatigue" give the most highly predictive ability to predict whether a person suffers from "Lung Cancer", while the node "Allergy" cannot individually predict "Lung Cancer". "Allergy" may enhance the predictive power of "Coughing" when it joins with "Coughing". Thus, the pattern space in EP mining can be naturally reduced to direct causes and direct effects of the class attribute in causal Bayesian networks, and then we obtain Proposition 4 as follows. Proposition 4. The pattern space in EP mining for classification can be further reduced to direct causes and direct effects of the class attribute in causal Bayesian networks.

# 4.2 Mining Emerging Patterns from High-dimensional Data 

With Propositions 1 to 4 above, we give a new framework for mining EPs with high-dimensional data, as shown in Fig. 4 with 4 steps. The key steps of our framework are (1) Step 1: identifying CE (direct Causes and direct Effects) or MB (the Markov Blanket) of the class attribute from data, and (2) Step 3: mining EPs from CE or MB space.

Step 1: Identifying CE and MB of the class attribute. As stated in Section 2.2, structure learning of causal Bayesian networks in observational data is essentially the same as structure learning of Bayesian networks. When the number of features is small, we can adopt existing Bayesian network structure learning algorithms to construct a complete Bayesian network, and then get the CE or MB of the class attribute. When there are tens of thousands of feature dimensions, learning a complete Bayesian network is simply impossible [8].

![img-3.jpeg](img-3.jpeg)

Fig. 4 The framework of building EPs-based classifiers from high-dimensional data
In fact, in our framework, both the CE approach and the MB approach only need to get the CE or MB of the class attribute, and don't need to distinguish which node is a direct cause, a direct effect, or a spouse from the CE set or MB set. Rather than recovering a complete Bayesian network among all features, our framework only uses local learning techniques to uncover cause-effect relationships between the class attribute and other nodes or to uncover the MB of the class attribute. Most importantly, in a causal Bayesian network with causal faithfulness, the CE or MB of a target is unique and minimal.

Therefore, no matter whether the number of features in a dataset is small or large, our framework adopts local learning techniques to capture the CE or the MB of the class attribute. For the CE approach of EP mining, there are two state-of-the-art local learning techniques, MMPC and HITON_PC (detailed descriptions in [2]). Since those two algorithms are complete under the assumption of causal faithfulness, we introduce the HITON_PC algorithm into our framework to get the CE of the class attribute without uncovering a complete Bayesian network. For the MB approach, the HITON_MB algorithm is used to get the MB of the class attribute [2] ${ }^{1}$. To identify the MB of the class attribute, the HITON_MB algorithm first discovers the CE of the class attribute by the HITON_PC algorithm and, then, identifies the spouses of the class attribute.

Step 3: Mining EPs from the pattern space of CE or MB of the class attribute. At step 3, with the CE or MB of the class attribute, our framework gives two approaches, CE approach to mine EPs from the space of direct causes and direct effects, and MB approach to mine EPs from the space of the Markov blanket. Since the CE or MB of the class attribute is unique and minimal in a causal Bayesian network, at step 3, we adopt the ConsEPMiner algorithm ${ }^{2}$ which is a level-wise, candidate generation-and-test approach to mine EPs [37]. The ConsEPMiner algorithm follows the set-enumeration tree search framework and the breadth-first search strategy, and mines EPs satisfying several constraints including the growth-rate improvement constraint. With the EPs mined by our two approaches, two classifiers, the CE-EP and MB-EP classifiers, are constructed, and they both use the score function defined by Eq. 5 in Section 3.1 for classification.

[^0]
[^0]:    ${ }^{1}$ The codes of HITON_PC and HITON_MB are available at http://www.dsl-lab.org/causal_explorer.
    ${ }^{2}$ The code of the ConsEPMiner algorithm is available at http://goanna.cs.rmit.edu.au/ zhang.

# 5 EXPERIMENTAL RESULTS 

### 5.1 Experimental Setup

In order to thoroughly evaluate the proposed framework, thirty six datasets (Table 6) are selected, including the UCI datasets (the first 24 datasets), very high-dimensional biomedical datasets (hiva, ovari-an-cancer, lymphoma, and breast-cancer), NIPS 2003 feature selection challenge datasets (madelon, arcene, dorothea, and dexter), and four frequently studied public microarray datasets (the last 4 datasets), respectively.

TABLE 6 \#: THE NUMBER OF FEATURES, SIZE: THE NUMBER OF INSTANCES


Our comparative study involves three types of comparisons, using ten-fold cross-validation on all datasets.

- Comparing CE-EP and MB-EP classifiers against a well-known EP classifier, CAEP [10] and a Strong Jumping EP classifier, SJEP [11].
- Comparing CE-EP and MB-EP classifiers with three well-known associative classifiers: CBA [22], CMAR [19] and CPAR [36].
- Comparing CE-EP and MB-EP classifiers with the state-of-the-art non-associative classifiers, including Naïve Bayes (NB), Knn, Decision Tree J48, SVM, Bagging and AdaBoost using their Weka implementations with default parameters [15].
To discretize continuous features, we use the discretization method in the Causal Explorer Toolkit provided by Aliferis et al. [1]. In the experiments, we set the minimum confidence threshold to 0.8 for CBA and CMAR, and set the growth rate to 20 for CAEP, CE-EP and MB-EP classifiers. To thoroughly test the impact of the support threshold values, we set seven minimum supports for CE-EP, MB-EP, CAEP, CBA, and CMAR, including $0.005,0.01,0.05,0.1,0.2,0.3$, and 0.4 , respectively. We select the best classification accuracy under the seven minimum supports as the results for our comparative study. The SJEP classifier uses the minimal support threshold suggested in the original paper [11]. The parameters

for CPAR are set the same as those reported in [36]. CBA, CMAR, and CPAR are implemented in the LUCS KDD Software Library in Java [26], while CE-EP, MB-EP and CAEP are implemented in C++. The experiments are performed on a Window 7 DELL workstation with an Intel Xeon 2.93 GHz processor and 12.0 GB RAM.

# 5.2 Comparison of Predictive Accuracy 

### 5.2.1. Comparing with Other 11 Classifiers

Tables 7 to 9 report the predictive accuracies of our two classifiers, CE-EP and MB-EP, in comparison with other eleven classifiers, including two EP, three associative and six non-associative classifiers on the thirty six benchmark datasets. We select the best predictive accuracy under the seven minimum supports as the results for our comparative study. The best results among all classifiers are highlighted in bold for each dataset and the symbol "/" denotes that the classifier runs out of memory due to a huge number of candidate patterns.

In Table 7, compared to CAEP and SJEP, CE-EP achieves the highest accuracy on twenty one datasets out of the thirty six datasets while CAEP and SJEP fail to deal with the twelve very high-dimensional datasets. On three datasets, diabetes, liver and pima, SJEP gets very low predictive accuracy, since there are not enough SJEPs in those datasets for classification. In Table 8, CBA, CMAR and CPAR only have results on the twenty four low dimensional datasets as they fail to deal with a high feature space. From Tables 7 and 8, we can see that CE-EP outperforms SJEP, CBA, CMAR, and CPAR. Table 9 compares the accuracy of our two classifiers against well-known classifiers such as Naive Bayes (NB), Decision Tree J48, Knn, SVM and two ensemble classifiers, Bagging and AdaBoost. In comparison with these six classifiers, CE-EP is significantly superior to NB, Knn, J48, Bagging and AdaBoost and very competitive with SVM on all the thirty six datasets in Table 9.

TABLE 7 COMPARISON OF PREDICTIVE ACCURACY (\%): CE-EP, MB-EP, SJEP, AND CAEP




TABLE 8 COMPARISON OF PREDICTIVE ACCURACY (\%): CE-EP, CBA, CMAR, AND CPAR


TABLE 9 COMPARISON OF PREDICTIVE ACCURACY (\%) WITH NON-ASSOCIATIVE CLASSIFIERS


TABLE 10 WIN/TIE/LOSS COUNTS OF CE-EP VS. THE OTHER 12 CLASSIFIERS (PAIRWISE T-TEST AT 95\% SIGNIFICANCE LEVEL)


To further investigate the classification results, we conduct paired t-tests at a $95 \%$ significance level and summarize the win/tie/lose counts of CE-EP against the other algorithms in Table 10 (note: if a classifier fails to run on a dataset while our method can do it, then our classifier wins ). With the summary of the win/tie/lose counts shown in Table 10, we can see that CE-EP usually outperforms CAEP, CBA, CMAR and CPAR. Meanwhile, the MB-EP classifier has extremely similar performance with CE-EP. In comparison with the well-known non-associative classifiers, CE-EP is significantly superior to NB, Knn,

J48, Bagging and AdaBoost, and is competitive with SVM on all the thirty six datasets.
The above empirical results demonstrate that mining EPs in the pattern space of direct causes and direct effects, or the Markov blanket of the class attribute can find high quality patterns which possess the most differentiating power. Most importantly, the CE-EP and MB-EP classifiers can not only handle very high-dimensional datasets such as the last twelve datasets in Table 6, but also produce very promising predictive accuracy.

Why do the EPs mined by CE-EP possess such high discriminating power? We use vote, a UCI dataset, as an illustrating example. The vote dataset has 16 features (attributes) and one class attribute. Each feature has two values, yea and nay, and the class attribute is divided into two classes: Democrat (D) and Republican (R). Tables 11 to 13 give the EPs of the two classes mined from the vote dataset by the CE-EP algorithm, respectively.

It is clear that the EPs in Tables 11 to 12 are constructed from features physician-fee-freeze, adoption-of-the-budget-resolution and synfuels-corporation-cutback, whose indices in the original vote dataset are 4, 3 and 11, respectively. The EPs constructed from these three features are highly discriminative as indicated by the high growth ratio GR(e). Note that Feature 4 is the direct cause of the class attribute while Features 3 and 11 are the direct effects of the class attribute in the causal Bayesian network learned from the vote dataset.

From the viewpoint of feature discriminability, the mutual information measure and the chi-squared test both show that Features 4, 3 and 11 are the most informative features among all of features with respect to the class attribute. This is consistent with the feature discriminability described in Table 13.

TABLE 11 THE EPS FROM CLASS R(REPUBLICAN) TO CLASS D (DEMOCRAT)


TABLE 12 THE EPS FROM CLASS D (DEMOCRAT) TO CLASS R (REPUBLICAN)


TABLE 13 FEATURE DISCRIMINABILITY OF FEATURES 4, 3 AND 11


Accordingly, we conclude that the EPs extracted from the pattern space of direct causes and direct effects are high-quality patterns and possess the most discriminative power. They are the best candidates to be used to construct a highly accurate classifier.

# 5.2.2 Comparing with Top-k Feature Ranking Methods 

For the last 12 high-dimensional datasets in Table 6, we further compare the CE-EP algorithm with the two top-k feature ranking methods, the mutual information (MI for short) measure and the chi-squared test (CHI for short). For both ranking methods, we select the top 20 and top 30 features respectively, and then use the selected features to train EP classifiers to get the benchmark results.

TABLE 14 THE PREDICTIVE ACCURACY (\%) OF CE-EP VS. CHI AND MI


For CE-EP, we set the support threshold to 0.2 and the growth rate threshold to 20. From Tables 14 to 16, we can see that CE-EP gets much better performance than both the CHI and MI methods on the predictive accuracy and the number of mined patterns (MI(20) or CHI(20) denotes the top 20 features selected by the MI or CHI method).

TABLE 15 WIN/TIE/LOSS (PAIRWISE T-TEST AT 95\% SIGNIFICANCE LEVEL)


TABLE 16 THE NUMBER OF MINED PATTERNS OF CE-EP VS. CHI AND MI


### 5.3 Comparison of the Number of Patterns

In this section, we compare the numbers of patterns selected by CE-EP and MB-EP with the CAEP, CBA and CMAR classifiers, as these five associative classifiers all focus on generating patterns with the support-confidence framework. We report the average numbers of patterns over all seven minimum support thresholds. Since on $w d b c, k r$-vs-kp, ionosphere, horse-colic and german, CAEP cannot run using all the support thresholds due to huge numbers of patterns, the numbers of patterns on these datasets is averaged over the available support thresholds.

As depicted in Tables 17 and 18, it is clear that the CE-EP and MB-EP classifiers select many fewer patterns than the CAEP, CBA and CMAR classifiers on all the datasets.

These results further illustrate that extracting the EPs from the space of direct causes and direct effects

or the Markov blanket of the class attribute not only gets a much smaller set of EPs but also achieves a higher predictive accuracy than the existing EPs-based and associative classifiers. Tables 17 to 18 also indicate that even with very high-dimensional datasets, the numbers of patterns selected by CE-EP and MB-EP don't change much in comparison with those on the twenty four low-dimensional datasets while CAEP, CBA, and CMAR cannot deal with those datasets, even with a rather high support threshold.

TABLE 17 COMPARISON OF NUMBERS OF PATTERNS (AVERAGE ON SEVEN SUPPORT THRESHOLDS): CE-EP, MB-EP, AND CAEP


TABLE 18 COMPARISON OF NUMBERS OF PATTERNS (AVERAGE ON SEVEN SUPPORT THRESHOLDS): CE-EP, MB-EP, CBA, AND CMAR


# 5.4 Comparison of Running Time of EP Classifiers 

Table 19 reports the average running time over seven minimum support thresholds of CE-EP and MB-EP against CAEP. The running time contains all execution time, including importing datasets, ten-fold cross validation learning and testing. The best result for each dataset is highlighted in bold. As stated in Section 5.3, since on wdbc, kr-vs-kp, ionosphere, horse-colic and german, CAEP cannot run under all the support thresholds, the running time for these datasets is averaged over the available support thresholds.

Table 19 shows that CE-EP and MB-EP are faster than CAEP on all the datasets. The running time of CAEP fluctuates a little among different datasets while CE-EP and MB-EP, especially CE-EP, have a very stable running time for both low and high dimensional datasets. On the dorothea dataset, the running time of MB-EP is greater than CE-EP due to the very large space of this dataset, up to 100,000 features.

TABLE 19 COMPARISON OF RUNNING TIME (AVERAGE ON SEVEN SUPPORT THRESHOLDS): CE-EP, MB-EP, AND CAEP


# 5.5 Sensitivity Analysis on Support Thresholds 

To further explore the performance of CE-EP, MB-EP, CAEP, CBA and CMAR, we conduct sensitivity analysis on the predictive accuracy and the number of selected patterns, of CE-EP, MB-EP, CAEP, CBA, and CMAR under seven minimum support threshold values in the following subsections.

TABLE 20 SENSITIVITY ANALYSIS ON PREDICTIVE ACCURACY (\%): CE-EP, MB-EP, AND CAEP


### 5.5.1 Sensitivity Analysis on CE-EP, MB-EP, and CAEP

Table 20 shows the change of predictive accuracy of CE-EP, MB-EP, and CAEP under seven support

thresholds, $0.005,0.01,0.05,0.1,0.2,0.3$, and 0.4 . In the second row of Table 20, "max", "min", and " $\Delta$ accu" denote the maximum predictive accuracy under seven support thresholds, minimum predictive accuracy under seven support thresholds and the difference between the maximum predictive accuracy and minimum predictive accuracy. From Table 20, we can see that on the predictive accuracy, CE-EP and MB-EP are less sensitive to the support thresholds than CAEP. For all datasets, both CE-EP and MB-EP are insensitive to the different support thresholds, even for those high-dimensional datasets. Furthermore, CE-EP is not only more insensitive, but also always achieves higher accuracy under all the seven support thresholds than CAEP. In fact, from Table 20, on the 24 UCI datasets, CAEP is also insensitive to the support thresholds except for the tictactoe dataset.

TABLE 21 SENSITIVITY ANALYSIS ON THE NUMBER OF PATTERNS: CE-EP, MB-EP, AND CAEP


Table 21 shows the change of the numbers of selected EPs of CE-EP, MB-EP, and CAEP under seven support thresholds. In the second row of Table 21, "max", "min", and "ratio" denote the maximum number of selected EPs under seven support thresholds, minimum number of selected EPs under seven support thresholds and the ratio of the maximum number of selected EPs and minimum number of selected EPs. As shown in Table 21, on the numbers of selected EPs, CE-EP and MB-EP are less sensitive to the support thresholds than CAEP. Both CE-EP and MB-EP are very insensitive to the different support

thresholds, even for those high-dimensional datasets, while CAEP is sensitive to the support thresholds on the 24 UCI datasets.

From Tables 20 to 21, we can conclude that on both low and high dimensional datasets, CE-EP and MB-EP are insensitive to the support thresholds on both predictive accuracy and the number of selected EPs. We can also come to the conclusion that EPs-based classifiers, CE-EP, MB-EP, and CAEP, are insensitive to the support thresholds on the predictive accuracy, although CE-EP and MB-EP are less sensitive to the support thresholds than CAEP. The explanation is that the EPs denote a strong contrast between classes, thus they have very strong differentiating power to predict each class. For example, although CAEP is sensitive to the support threshold on the number of selected EPs, this has little impact on its predictive accuracy.

# 5.5.2 Sensitivity Analysis on CE-EP, CBA, and CMAR 

Since MB-EP has an extremely similar performance with CE-EP, in the following subsections, we only have the sensitivity analysis on CE-EP, CBA and CMAR under seven support thresholds, $0.005,0.01,0.05,0.1$, $0.2,0.3$, and 0.4 . In Fig. 5, we plot the predictive accuracy of CE-EP, CBA and CMAR on the 24 UCI datasets in Table 6 with seven support thresholds.

As shown in Fig.5, CE-EP is less sensitive to the support thresholds than CBA and CMAR and always achieves a higher accuracy under all the seven support thresholds than CBA and CMAR on most datasets. The choice of the support thresholds is the key to both CBA and CMAR. For example, in Fig. 5, when the minimum support threshold is up to 0.3 or 0.4 , the corresponding accuracies of both CBA and CMAR are greatly reduced.

On some datasets, the accuracies of CBA and CMAR are even reduced to 0 , such as clever, diabetes, german, ks-vr-kp, liver, pima, promoters, spect and tictactoe. On the infant-mortality, spectf, and wdbc data sets, CBA doesn't work on all seven support thresholds due to the huge number of candidate patterns.

In Fig.6, we have a further sensitivity analysis of CE-EP, CBA, and CMAR on the number of selected patterns. We plot the numbers of selected patterns of CE-EP, CBA and CMAR on all 24 UCI datasets with the seven minimum support thresholds, $0.005,0.01,0.05,0.1,0.2,0.3$, and 0.4 . From Fig.6, we can see that the numbers of selected patterns of CBA and CMAR are sensitive to the support thresholds. With a small support threshold, CBA and CMAR select a large number of association rules. With the support threshold increasing, the number of selected rules is greatly reduced.

Along with Fig. 5, we can conclude that when the support threshold is small, CBA and CMAR can obtain a large number of association rules for classification to achieve good accuracy as shown in Fig. 5. When the support threshold is large, CBA and CMAR prune too many rules, including useful rules, which results in low predictive accuracy. For example, in Fig.5, when the minimum support threshold

moves up to 0.4 , on some datasets, the accuracies of CBA and CMAR are even reduced to 0 , such as clever, diabetes, german, ks-vr-kp, liver, pima, promoters, spect and tictactoe. The explanation is that CBA and CMAR can no longer select any rules under this minimum support threshold, as shown in Fig.6. From Figures 5 and 6, it is clear that with a small support threshold, a large number of association rules provide rich information for classification and make CBA and CMAR achieve high accuracy. But in this case, it is also difficult to store, retrieve and maintain a large number of candidate patterns for classification. For example, in Fig.6, on the infant-mortality, spectf, and wdbc datasets, CBA doesn't work under a small support threshold due to the huge number of rules.
![img-4.jpeg](img-4.jpeg)

Figure 5: Sensitivity analysis on predictive accuracy: CE-EP, CBA, and CMAR

![img-5.jpeg](img-5.jpeg)

Figure 6: Sensitivity analysis on the number of patterns: CE-EP, CBA, and CMAR

As for CE-EP, under all seven support thresholds, it not only selects a small set of EPs, but also is insensitive to the support threshold. Therefore, these results further validate the theoretical analysis of the relationships between causal relevance and EP discriminability. More specifically, when CE-EP mines the EPs from the space of the direct causes and direct effects of the class attribute, they can achieve strongly predictive EPs no matter whether the support threshold is small or large. This also explains why

the accuracy of CE-EP remains stable under the different support thresholds as shown in Fig. 5.

# 5.6 Sensitivity Analysis on the Minimal Grow-rate thresholds 

To explore the impact of the minimal grow-rate threshold on the performance of both CE-EP and CAEP, we conduct an analysis on the predictive accuracy of CE-EP and CAEP under seven minimum growth-rate thresholds, as shown in Figures 7 and 8, where GR stands for Growth Rate thresholds and the minimum support threshold is fixed at 0.1 . Since MB-EP has an extreme similar performance with CE-EP, we don't plot the performance of MB-EP under the seven minimum growth-rate thresholds. On infant, ionosphere, promoters and spectf, CAEP cannot run under all seven growth-rate thresholds, and therefore Fig. 7 plots the predictive accuracy of the other 20 low-dimensional datasets under the seven growth-rate thresholds. In Figure 8, the X-axis denotes all of the thirty six datasets corresponding to Table 6. Figures 7 to 8 show that both CAEP and CE-EP are not sensitive to the minimum growth-rate thresholds at all, especially CE-EP.
![img-6.jpeg](img-6.jpeg)

Figure 7: The impact of growth-rate thresholds on CAEP (The 20 datasets on the X-axis are: 1.australian, 2. breast-w, 3.crx, 4.cleve, 5.diabetes, 6.german,7. house-votes, 8.hepatitis, 9.horse-colic, 10. hypothyroid, 11.heart, 12.kr-vs-kp, 13.labor, 14. liver, 15.mushroom, 16. pima, 17.spect, 18.tictactoe, 19. vote, 20. wdbc).
![img-7.jpeg](img-7.jpeg)

Figure 8: The impact of growth rate thresholds on CE-EP

### 5.7 Summary on the Experimental Results

Based on the comparative study in Sections 5.2 to 5.6, we have the following findings:
(1) With the seven support thresholds, the experiments demonstrate that the EPs-based classifiers are less sensitive to the support thresholds than the associative classifiers. Especially, on the predictive accuracy, EPs-based classifiers, CE-EP, MB-EP and CAEP, are less sensitive than associative classifiers, CBA and CMAR. As for the number of selected patterns, CE-EP and MB-EP are less sensitive than CAEP, CBA and CMAR, while CAEP is less sensitive than CBA and CMAR. Thus, the choice of a suitable support threshold is the key to control CBA and CMAR while it is not crucial for CE-EP, MB-EP and CAEP. Moreover, the study on the minimal grow-rate

thresholds verifies that both CE-EP and CAEP are insensitive to the minimal grow-rate thresholds on the predictive accuracy.
(2) The CE-EP and MB-EP classifiers are more accurate than the five associative classifiers (CAEP, SJEP, CBA, CMAR, and CPAR) and the five state-of-the-art non-associative classifiers (NB, Knn, J48, Bagging, and AdaBoost), and are very competitive with SVM. Meanwhile, both our classifiers produce smaller numbers of EPs. Moreover, CAEP, SJEP, CBA, CMAR and CPAR cannot handle high-dimensional datasets. As for the running time, CE-EP and MB-EP are faster than CAEP on all datasets. This verifies our theoretical analysis of the relationships between causal relevance and EP discriminability to help avoid generating non-EPs or redundant EPs in advance.
(3) Both the CE-EP and MB-EP classifiers can handle very high feature dimensions well yet get very promising performance. Although the MB-EP classifier considers the information of direct causes of the direct effects of the class attribute, it gets extremely similar performance with the CE-EP classifier. This validates that the direct causes and direct effects of the class attribute in causal Bayesian networks give a natural interpretation of what happens to the class attribute, and then naturally endows EPs with strong discriminating power.

# 6 CONCLUSIONS 

How to mine EPs from high-dimensional data is a challenging issue in EP mining. Meanwhile, how to deal with high sensitivity to minimal support thresholds is another challenging problem. In this paper, we have brought causal relevance and EP discriminability together to reduce the pattern space of EP mining to the direct causes and direct effects or the Markov blanket of the class attribute in causal Bayesian networks, and proposed a new framework for building accurate EPs-based classifiers from high-dimensional data. Extensive experiments on a broad range of datasets have demonstrated the effectiveness of the proposed approach against other well-established methods, in terms of predictive accuracy, pattern numbers, running time, and sensitivity analysis on the minimal support thresholds and minimal grow-rate thresholds.

## ACKNOWLEDGMENTS

This work is supported by the National 863 Program of China (2012AA011005), the National 973 Program of China under grant 2013CB329604, the National Natural Science Foundation of China (61229301, 61070131, 61175051 and 61005007), the US National Science Foundation (CCF-0905337), and the US NASA Research Award (NNX09AK86G).
